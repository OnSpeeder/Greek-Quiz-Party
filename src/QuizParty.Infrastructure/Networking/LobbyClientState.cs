using QuizParty.Core.Lobby;

namespace QuizParty.Infrastructure.Networking;

public enum LobbyClientUpdate { Ignored, Rejected, Joined, Snapshot, RequestResult, MatchSnapshot, AnswerReceipt, CardReceipt }

public sealed class LobbyClientState
{
    private Guid _helloId;
    private LobbySnapshotDto? _snapshot;
    private readonly HashSet<Guid> _pending = new();
    public Guid? PlayerId { get; private set; }
    public Guid? ControllerId { get; private set; }
    private readonly Dictionary<int, MatchClientState> _matches = new();
    public int LastMatchSlot { get; private set; }
    public string LastReason { get; private set; } = "None";
    public MatchClientState Match => MatchForSlot(0);
    public MatchClientState MatchForSlot(int slot)
    {
        if (slot is < 0 or > 7) throw new ArgumentOutOfRangeException(nameof(slot));
        if (!_matches.TryGetValue(slot, out var state)) _matches.Add(slot, state = new());
        return state;
    }
    public IReadOnlyList<LobbyPlayerDto> OwnedPlayers => Array.AsReadOnly(_snapshot?.Players
        .Where(p => (p.ControllerId ?? p.PlayerId) == ControllerId).OrderBy(p => p.LocalSlot).ToArray() ?? []);
    public LobbySnapshotDto? Snapshot => _snapshot is null ? null : _snapshot with { Players = _snapshot.Players.ToArray() };

    public string BeginHello(string name, string platform, string pin = "")
    {
        _helloId = Guid.NewGuid();
        _snapshot = null;
        PlayerId = null;
        ControllerId = null;
        _pending.Clear();
        _matches.Clear(); LastMatchSlot = 0;
        LastReason = "None";
        return LobbyProtocol.Encode("ClientHello", Guid.Empty,
            new ClientHelloDto(LobbyProtocol.AppVersion, name, platform, pin), messageId: _helloId);
    }

    public string? CreateReady(bool ready, int slot = 0) => OwnedPlayers.Any(p => p.LocalSlot == slot)
        ? CreateRequest("SetReady", new ReadyRequestDto(ready, slot)) : null;
    public string? CreateAddLocal(string name, int slot) => LobbyProtocol.ValidName(name) && slot is >= 1 and <= 7 &&
        !OwnedPlayers.Any(p => p.LocalSlot == slot) ? CreateRequest("AddLocalPlayer", new AddLocalPlayerDto(name, slot)) : null;
    public string? CreateRemoveLocal(int slot) => slot != 0 && OwnedPlayers.Any(p => p.LocalSlot == slot)
        ? CreateRequest("RemoveLocalPlayer", new RemoveLocalPlayerDto(slot)) : null;
    public string? CreateStartRequest() => CreateRequest("StartGame", new StartRequestDto());

    private string? CreateRequest<T>(string type, T payload)
    {
        if (_snapshot?.Phase != "Lobby" || _pending.Count >= 16) return null;
        var id = Guid.NewGuid();
        _pending.Add(id);
        return LobbyProtocol.Encode(type, _snapshot.SessionId, payload, messageId: id);
    }

    public LobbyClientUpdate Apply(string json)
    {
        if (!LobbyProtocol.TryDecode(json, out var packet) || packet is null || packet.ProtocolVersion != LobbyProtocol.Version)
            return LobbyClientUpdate.Ignored;
        if (packet.MessageType == "ServerHello")
        {
            if (_helloId == Guid.Empty || packet.CorrelationId != _helloId || PlayerId is not null ||
                !LobbyProtocol.TryPayload<ServerHelloDto>(packet, out var hello) || hello is null)
                return LobbyClientUpdate.Ignored;
            if (!hello.Accepted)
            {
                LastReason = BoundedReason(hello.Reason);
                return LobbyClientUpdate.Rejected;
            }
            if (hello.PlayerId is not { } player || player == Guid.Empty || !ValidSnapshot(hello.Lobby) ||
                hello.Lobby!.SessionId != packet.SessionId || hello.ControllerId == Guid.Empty ||
                !hello.Lobby.Players.Any(item => item.PlayerId == player && !item.IsHost && item.LocalSlot == 0 &&
                    (item.ControllerId ?? item.PlayerId) == (hello.ControllerId ?? player)))
                return LobbyClientUpdate.Ignored;
            PlayerId = player;
            ControllerId = hello.ControllerId ?? player;
            _snapshot = hello.Lobby with { Players = hello.Lobby.Players.ToArray() };
            return LobbyClientUpdate.Joined;
        }
        if (_snapshot is null || packet.SessionId != _snapshot.SessionId) return LobbyClientUpdate.Ignored;
        if (packet.MessageType == "MatchSnapshot" && LobbyProtocol.TryPayload<MatchSnapshotDto>(packet, out var match) && match is not null &&
            OwnedPlayers.FirstOrDefault(p => p.LocalSlot == match.LocalSlot) is { } own && MatchForSlot(match.LocalSlot).ApplySnapshot(packet, _snapshot.SessionId, own.PlayerId))
        { LastMatchSlot = match.LocalSlot; return LobbyClientUpdate.MatchSnapshot; }
        if (packet.MessageType == "AnswerAccepted" && LobbyProtocol.TryPayload<AnswerReceiptDto>(packet, out var answer) && answer is not null &&
            OwnedPlayers.Any(p => p.LocalSlot == answer.LocalSlot) && MatchForSlot(answer.LocalSlot).ApplyReceipt(packet, _snapshot.SessionId))
        { LastMatchSlot = answer.LocalSlot; return LobbyClientUpdate.AnswerReceipt; }
        if (packet.MessageType == "CardResult" && LobbyProtocol.TryPayload<CardReceiptDto>(packet, out var card) && card is not null &&
            OwnedPlayers.Any(p => p.LocalSlot == card.LocalSlot) && MatchForSlot(card.LocalSlot).ApplyCardReceipt(packet, _snapshot.SessionId))
        { LastMatchSlot = card.LocalSlot; return LobbyClientUpdate.CardReceipt; }
        if (packet.MessageType == "LobbySnapshot" && LobbyProtocol.TryPayload<LobbySnapshotDto>(packet, out var next) &&
            ValidSnapshot(next) && next!.SessionId == _snapshot.SessionId && next.Revision > _snapshot.Revision &&
            next.Players.Any(player => player.PlayerId == PlayerId && (player.ControllerId ?? player.PlayerId) == ControllerId && player.LocalSlot == 0) &&
            !(_snapshot.Phase == "GameStarting" && (next.Phase != "GameStarting" || next.TeamMode != _snapshot.TeamMode)))
        {
            _snapshot = next with { Players = next.Players.ToArray() };
            foreach (var slot in _matches.Keys.Where(slot => !OwnedPlayers.Any(p => p.LocalSlot == slot)).ToArray()) _matches.Remove(slot);
            return LobbyClientUpdate.Snapshot;
        }
        if (packet.MessageType == "RequestResult" && packet.CorrelationId is { } correlation &&
            _pending.Contains(correlation) && LobbyProtocol.TryPayload<RequestResultDto>(packet, out var result) && result is not null)
        {
            _pending.Remove(correlation);
            LastReason = result.Accepted ? "None" : BoundedReason(result.Reason);
            return LobbyClientUpdate.RequestResult;
        }
        return LobbyClientUpdate.Ignored;
    }

    private static string BoundedReason(string? reason) => reason is { Length: > 0 and <= 40 } ? reason : "MalformedRequest";

    private static bool ValidSnapshot(LobbySnapshotDto? snapshot) => snapshot is not null && snapshot.SessionId != Guid.Empty &&
        snapshot.Revision > 0 && LobbyProtocol.ValidName(snapshot.RoomName) && snapshot.Phase is "Lobby" or "GameStarting" &&
        snapshot.Players is { Length: >= 1 and <= LobbySession.MaxPlayers } players &&
        players.All(player => player is not null && player.PlayerId != Guid.Empty && LobbyProtocol.ValidName(player.DisplayName) &&
            player.ControllerId != Guid.Empty && player.LocalSlot is >= 0 and <= 7 && (!player.IsHost || player.LocalSlot == 0) &&
            (snapshot.TeamMode ? player.TeamId is 1 or 2 : player.TeamId is null)) &&
        players.Count(player => player.IsHost) == 1 && players.Select(player => player.PlayerId).Distinct().Count() == players.Length &&
        players.GroupBy(p => p.ControllerId ?? p.PlayerId).All(group => group.Any(p => p.LocalSlot == 0) && group.Select(p => p.LocalSlot).Distinct().Count() == group.Count());
}

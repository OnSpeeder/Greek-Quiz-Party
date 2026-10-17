using QuizParty.Core.Lobby;

namespace QuizParty.Infrastructure.Networking;

public enum LobbyClientUpdate { Ignored, Rejected, Joined, Snapshot, RequestResult, MatchSnapshot, AnswerReceipt }

public sealed class LobbyClientState
{
    private Guid _helloId;
    private LobbySnapshotDto? _snapshot;
    private readonly HashSet<Guid> _pending = new();
    public Guid? PlayerId { get; private set; }
    public string LastReason { get; private set; } = "None";
    public MatchClientState Match { get; private set; } = new();
    public LobbySnapshotDto? Snapshot => _snapshot is null ? null : _snapshot with { Players = _snapshot.Players.ToArray() };

    public string BeginHello(string name, string platform)
    {
        _helloId = Guid.NewGuid();
        _snapshot = null;
        PlayerId = null;
        _pending.Clear();
        Match = new();
        LastReason = "None";
        return LobbyProtocol.Encode("ClientHello", Guid.Empty,
            new ClientHelloDto(LobbyProtocol.AppVersion, name, platform), messageId: _helloId);
    }

    public string? CreateReady(bool ready) => CreateRequest("SetReady", new ReadyRequestDto(ready));
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
                hello.Lobby!.SessionId != packet.SessionId || !hello.Lobby.Players.Any(item => item.PlayerId == player && !item.IsHost))
                return LobbyClientUpdate.Ignored;
            PlayerId = player;
            _snapshot = hello.Lobby with { Players = hello.Lobby.Players.ToArray() };
            return LobbyClientUpdate.Joined;
        }
        if (_snapshot is null || packet.SessionId != _snapshot.SessionId) return LobbyClientUpdate.Ignored;
        if (packet.MessageType == "MatchSnapshot" && PlayerId is { } playerId && Match.ApplySnapshot(packet, _snapshot.SessionId, playerId))
            return LobbyClientUpdate.MatchSnapshot;
        if (packet.MessageType == "AnswerAccepted" && Match.ApplyReceipt(packet, _snapshot.SessionId)) return LobbyClientUpdate.AnswerReceipt;
        if (packet.MessageType == "LobbySnapshot" && LobbyProtocol.TryPayload<LobbySnapshotDto>(packet, out var next) &&
            ValidSnapshot(next) && next!.SessionId == _snapshot.SessionId && next.Revision > _snapshot.Revision &&
            next.Players.Any(player => player.PlayerId == PlayerId) && !(_snapshot.Phase == "GameStarting" && next.Phase != "GameStarting"))
        {
            _snapshot = next with { Players = next.Players.ToArray() };
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
        players.All(player => player is not null && player.PlayerId != Guid.Empty && LobbyProtocol.ValidName(player.DisplayName)) &&
        players.Count(player => player.IsHost) == 1 && players.Select(player => player.PlayerId).Distinct().Count() == players.Length;
}

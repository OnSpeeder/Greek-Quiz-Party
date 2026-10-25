using QuizParty.Core.Game;
using QuizParty.Core.Players;

namespace QuizParty.Core.Lobby;

public enum LobbyError { None, InvalidPlayer, AlreadyJoined, RoomFull, GameStarted, UnknownConnection, NotHost, NotReady, InvalidTeam, CharacterTaken }
public sealed record LobbyPlayer(Player Player, bool IsHost, bool Ready, TeamId? TeamId = null);
public sealed record LobbySnapshot(long Revision, GamePhase Phase, IReadOnlyList<LobbyPlayer> Players, bool TeamMode = false);

/// <summary>Host-only roster; players are distinct from device connections and local slots.</summary>
public sealed class LobbySession
{
    public const int MaxPlayers = 8;
    public const int MinPartyPlayers = 2;
    public static readonly ConnectionId HostConnection = new(1);
    private readonly Dictionary<PlayerId, LobbyPlayer> _players = new();
    private GameStateMachine _state = new(GameAuthority.Host);
    private long _revision = 1;
    private bool _teamMode;
    public int Capacity { get; }
    public bool HostPlays { get; }
    public LobbySession(Player host, int maxPlayers = MaxPlayers) : this(host, maxPlayers, true) { }
    public static LobbySession WithoutHostPlayer(int maxPlayers = MaxPlayers) => new(null, maxPlayers, false);
    private LobbySession(Player? host, int maxPlayers, bool hostPlays)
    {
        if (maxPlayers is < MinPartyPlayers or > MaxPlayers) throw new ArgumentOutOfRangeException(nameof(maxPlayers));
        Capacity = maxPlayers; HostPlays = hostPlays;
        if (hostPlays) ArgumentNullException.ThrowIfNull(host);
        if (host is not null)
        {
            if (host.ConnectionId != HostConnection || (host.LocalSlot?.Value ?? 0) != 0) throw new ArgumentException("Host must own connection1/slot0.", nameof(host));
            _players.Add(host.Id, new(host with { Character = host.Character ?? CharacterId.Pink }, true, false));
        }
        _state.TryTransition(GameTrigger.Initialize); _state.TryTransition(GameTrigger.OpenLobby);
    }
    public LobbyError Join(Player player)
    {
        ArgumentNullException.ThrowIfNull(player);
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (player.ConnectionId is not { Value: > 1 } connection) return LobbyError.InvalidPlayer;
        if (FindPlayer(connection) is not null) return LobbyError.AlreadyJoined;
        return Add(player, primary: true);
    }
    public LobbyError AddLocal(Player player)
    {
        ArgumentNullException.ThrowIfNull(player);
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (player.ConnectionId is not { } connection || FindPlayer(connection) is null || player.LocalSlot is not { Value: >= 1 and <= 7 }) return LobbyError.InvalidPlayer;
        return Add(player, primary: false);
    }
    private LobbyError Add(Player player, bool primary)
    {
        var slot = player.LocalSlot?.Value ?? 0;
        if (_players.ContainsKey(player.Id) || (primary && slot != 0)) return LobbyError.InvalidPlayer;
        if (_players.Values.Any(p => p.Player.ConnectionId == player.ConnectionId && (p.Player.LocalSlot?.Value ?? 0) == slot)) return LobbyError.AlreadyJoined;
        if (_players.Count >= Capacity) return LobbyError.RoomFull;
        var character = player.Character ?? Enumerable.Range(0, Characters.Count).Select(i => (CharacterId)i)
            .First(id => _players.Values.All(p => p.Player.Character != id));
        if (!Characters.IsValid((int)character)) return LobbyError.InvalidPlayer;
        if (_players.Values.Any(p => p.Player.Character == character)) return LobbyError.CharacterTaken;
        player = player with { Character = character };
        var team = !_teamMode ? (TeamId?)null : LeastPopulatedTeam();
        _players.Add(player.Id, new(player, false, false, team)); _revision++; return LobbyError.None;
    }
    public LobbyError RemoveLocal(ConnectionId connection, LocalSlot slot)
    {
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (slot.Value == 0 || FindPlayer(connection, slot) is not { } id) return LobbyError.InvalidPlayer;
        _players.Remove(id); _revision++; return LobbyError.None;
    }
    public LobbyError SetReady(ConnectionId connection, bool ready, LocalSlot? slot = null)
    {
        if (FindPlayer(connection, slot) is not { } id) return LobbyError.UnknownConnection;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        var player = _players[id]; if (player.Ready == ready) return LobbyError.None;
        _players[id] = player with { Ready = ready }; _revision++; return LobbyError.None;
    }
    public LobbyError SetTeamMode(ConnectionId caller, bool enabled)
    {
        if (caller != HostConnection) return LobbyError.NotHost;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (_teamMode == enabled) return LobbyError.None;
        _teamMode = enabled; var index = 0;
        foreach (var id in _players.Keys.ToArray()) _players[id] = _players[id] with { TeamId = enabled ? (index++ % 2 == 0 ? TeamId.A : TeamId.B) : null };
        _revision++; return LobbyError.None;
    }
    public LobbyError SetTeam(ConnectionId caller, PlayerId player, TeamId team)
    {
        if (caller != HostConnection) return LobbyError.NotHost;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (!_teamMode || team is not (TeamId.A or TeamId.B) || !_players.TryGetValue(player, out var item)) return LobbyError.InvalidTeam;
        if (item.TeamId == team) return LobbyError.None;
        _players[player] = item with { TeamId = team }; _revision++; return LobbyError.None;
    }
    public TeamRoster? Teams() => !_teamMode ? null : new(_players.Keys, _players.Values.Select(p => new PlayerTeam(p.Player.Id, p.TeamId!.Value)));
    private TeamId LeastPopulatedTeam() => _players.Values.Count(p => p.TeamId == TeamId.A) <= _players.Values.Count(p => p.TeamId == TeamId.B) ? TeamId.A : TeamId.B;
    public LobbyError Start(ConnectionId caller)
    {
        if (caller != HostConnection) return LobbyError.NotHost;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (_players.Count < MinPartyPlayers || _players.Values.Any(player => !player.Ready)) return LobbyError.NotReady;
        if (_teamMode && _players.Values.Select(p => p.TeamId).Distinct().Count() != 2) return LobbyError.InvalidTeam;
        var error = _state.TryTransition(GameTrigger.StartGame);
        if (error != GameError.None) throw new InvalidOperationException($"Unexpected lobby transition: {error}");
        _revision++; return LobbyError.None;
    }
    public void Replay()
    {
        if (_state.Phase != GamePhase.GameStarting) throw new InvalidOperationException("No match to replay.");
        // Lobby admission has its own state machine; the match coordinator verifies GameOver.
        _state = new(GameAuthority.Host);
        _state.TryTransition(GameTrigger.Initialize); _state.TryTransition(GameTrigger.OpenLobby);
        foreach (var id in _players.Keys.ToArray()) _players[id] = _players[id] with { Ready = false };
        _revision++;
    }
    public bool Disconnect(ConnectionId connection)
    {
        if (connection == HostConnection) return false;
        var ids = _players.Values.Where(p => p.Player.ConnectionId == connection).Select(p => p.Player.Id).ToArray();
        foreach (var id in ids) _players.Remove(id);
        if (ids.Length != 0) _revision++;
        return ids.Length != 0;
    }
    public PlayerId? FindPlayer(ConnectionId connection, LocalSlot? slot = null) => _players.Values.FirstOrDefault(p =>
        p.Player.ConnectionId == connection && (p.Player.LocalSlot?.Value ?? 0) == (slot?.Value ?? 0))?.Player.Id;
    public LobbySnapshot GetSnapshot() => new(_revision, _state.Phase,
        Array.AsReadOnly(_players.Values.OrderBy(p => p.Player.ConnectionId!.Value.Value).ThenBy(p => p.Player.LocalSlot?.Value ?? 0).ToArray()), _teamMode);
}

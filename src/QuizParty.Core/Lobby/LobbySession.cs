using QuizParty.Core.Game;
using QuizParty.Core.Players;

namespace QuizParty.Core.Lobby;

public enum LobbyError { None, InvalidPlayer, AlreadyJoined, RoomFull, GameStarted, UnknownConnection, NotHost, NotReady }
public sealed record LobbyPlayer(Player Player, bool IsHost, bool Ready);
public sealed record LobbySnapshot(long Revision, GamePhase Phase, IReadOnlyList<LobbyPlayer> Players);

/// <summary>Host-only lobby rules; the adapter authenticates and assigns identities.</summary>
public sealed class LobbySession
{
    public const int MaxPlayers = 8;
    public const int MinPartyPlayers = 2;
    public static readonly ConnectionId HostConnection = new(1);
    private readonly Dictionary<ConnectionId, LobbyPlayer> _players = new();
    private readonly GameStateMachine _state = new(GameAuthority.Host);
    private long _revision = 1;

    public LobbySession(Player host)
    {
        ArgumentNullException.ThrowIfNull(host);
        if (host.ConnectionId != HostConnection) throw new ArgumentException("Host must own connection 1.", nameof(host));
        _players.Add(HostConnection, new(host, true, true));
        _state.TryTransition(GameTrigger.Initialize);
        _state.TryTransition(GameTrigger.OpenLobby);
    }

    public LobbyError Join(Player player)
    {
        ArgumentNullException.ThrowIfNull(player);
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (player.ConnectionId is not { Value: > 1 } connection ||
            _players.Values.Any(existing => existing.Player.Id == player.Id)) return LobbyError.InvalidPlayer;
        if (_players.ContainsKey(connection)) return LobbyError.AlreadyJoined;
        if (_players.Count >= MaxPlayers) return LobbyError.RoomFull;
        _players.Add(connection, new(player, false, false));
        _revision++;
        return LobbyError.None;
    }

    public LobbyError SetReady(ConnectionId connection, bool ready)
    {
        if (!_players.TryGetValue(connection, out var player)) return LobbyError.UnknownConnection;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (player.Ready == ready) return LobbyError.None;
        _players[connection] = player with { Ready = ready };
        _revision++;
        return LobbyError.None;
    }

    public LobbyError Start(ConnectionId caller)
    {
        if (caller != HostConnection) return LobbyError.NotHost;
        if (_state.Phase != GamePhase.Lobby) return LobbyError.GameStarted;
        if (_players.Count < MinPartyPlayers || _players.Values.Any(player => !player.Ready)) return LobbyError.NotReady;
        var error = _state.TryTransition(GameTrigger.StartGame);
        if (error != GameError.None) throw new InvalidOperationException($"Unexpected lobby transition: {error}");
        _revision++;
        return LobbyError.None;
    }

    public bool Disconnect(ConnectionId connection)
    {
        if (connection == HostConnection || !_players.Remove(connection)) return false;
        _revision++;
        return true;
    }

    public PlayerId? FindPlayer(ConnectionId connection) => _players.GetValueOrDefault(connection)?.Player.Id;

    public LobbySnapshot GetSnapshot() => new(_revision, _state.Phase,
        Array.AsReadOnly(_players.Values.OrderBy(player => player.Player.ConnectionId!.Value.Value).ToArray()));
}

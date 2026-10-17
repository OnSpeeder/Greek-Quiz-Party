using Godot;
using QuizParty.Core.Lobby;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Networking;

/// <summary>Reliable ENet adapter. Rules and wire validation live outside the scene.</summary>
public partial class LobbyTransport : Node
{
    public const int DefaultPort = 7777;
    private ENetMultiplayerPeer? _peer;
    private LobbyHost? _host;
    private LobbyClientState _client = new();
    private string _clientName = "";
    private int _generation;
    private readonly HashSet<long> _handshaken = new();
    private readonly HashSet<long> _closing = new();
    private string? _lastReadyRequest;
    public event Action<LobbySnapshotDto>? SnapshotChanged;
    public event Action<string>? StatusChanged;
    public bool IsHost => _host is not null;
    public Guid? LocalPlayerId => _host?.Snapshot().Players.Single(player => player.IsHost).PlayerId ?? _client.PlayerId;
    public LobbySnapshotDto? Snapshot => _host?.Snapshot() ?? _client.Snapshot;
    public int ClientProtocol { get; set; } = LobbyProtocol.Version;

    public override void _Ready()
    {
        Multiplayer.ConnectedToServer += OnConnected;
        Multiplayer.ConnectionFailed += OnConnectionFailed;
        Multiplayer.ServerDisconnected += OnServerDisconnected;
        Multiplayer.PeerConnected += OnPeerConnected;
        Multiplayer.PeerDisconnected += OnPeerDisconnected;
    }

    public Error Host(string roomName, string playerName, int port = DefaultPort)
    {
        if (!LobbyProtocol.ValidName(roomName) || !LobbyProtocol.ValidName(playerName) || port is < 1024 or > 65535)
            return Error.InvalidParameter;
        Stop();
        var peer = new ENetMultiplayerPeer();
        // Reserve a few bounded handshake slots so a full room can send RoomFull.
        var error = peer.CreateServer(port, LobbyHost.MaxTransportConnections);
        if (error != Error.Ok) { peer.Dispose(); return error; }
        _host = new(roomName, playerName, new MonotonicGameClock());
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        Emit("HostListening");
        Publish();
        return Error.Ok;
    }

    public Error Join(string address, string playerName, int port = DefaultPort)
    {
        if (!LobbyProtocol.ValidName(playerName) || string.IsNullOrWhiteSpace(address) || address.Length > 253 ||
            address.Any(char.IsWhiteSpace) || port is < 1024 or > 65535) return Error.InvalidParameter;
        Stop();
        _clientName = playerName;
        var peer = new ENetMultiplayerPeer();
        var error = peer.CreateClient(address, port);
        if (error != Error.Ok) { peer.Dispose(); return error; }
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        Emit("Connecting");
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree() && _client.PlayerId is null)
                Fail("ConnectionTimeout");
        };
        return Error.Ok;
    }

    public void SetReady(bool ready, bool repeatLastRequest = false)
    {
        if (_host is not null)
        {
            Emit(_host.SetHostReady(ready).ToString());
            Broadcast();
            return;
        }
        var json = repeatLastRequest ? _lastReadyRequest : _client.CreateReady(ready);
        if (json is null) return;
        _lastReadyRequest = json;
        RpcId(1, MethodName.ClientMessage, json);
    }

    public void StartGame()
    {
        if (_host is null) { Emit("NotHost"); return; }
        Emit(_host.Start().ToString());
        Broadcast();
    }

    // Used by regression to verify rejection at the real host RPC boundary.
    public void SendStartRequest()
    {
        var json = _client.CreateStartRequest();
        if (_host is null && json is not null) RpcId(1, MethodName.ClientMessage, json);
    }

    public void Stop()
    {
        _generation++;
        _host = null;
        _client = new();
        _handshaken.Clear();
        _closing.Clear();
        _lastReadyRequest = null;
        if (_peer is not null)
        {
            Multiplayer.MultiplayerPeer = new OfflineMultiplayerPeer();
            _peer.Close();
            _peer.Dispose();
            _peer = null;
        }
    }

    public override void _ExitTree()
    {
        Multiplayer.ConnectedToServer -= OnConnected;
        Multiplayer.ConnectionFailed -= OnConnectionFailed;
        Multiplayer.ServerDisconnected -= OnServerDisconnected;
        Multiplayer.PeerConnected -= OnPeerConnected;
        Multiplayer.PeerDisconnected -= OnPeerDisconnected;
        Stop();
    }

    private void OnConnected()
    {
        var json = _client.BeginHello(_clientName, OS.GetName());
        // Explicit incompatible header is only selected by the process test flag.
        if (ClientProtocol != LobbyProtocol.Version) json = json.Replace("\"ProtocolVersion\":1", $"\"ProtocolVersion\":{ClientProtocol}", StringComparison.Ordinal);
        RpcId(1, MethodName.ClientMessage, json);
    }

    private void OnPeerConnected(long connection)
    {
        if (_host is null) return;
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree() && !_handshaken.Contains(connection))
                DisconnectPeer(connection);
        };
    }

    private void OnPeerDisconnected(long connection)
    {
        if (_host is null) return;
        _handshaken.Remove(connection);
        _closing.Remove(connection);
        if (_host.Disconnect(connection)) { Emit("PlayerLeft"); Broadcast(); }
    }

    private void OnConnectionFailed() => Fail("ConnectionFailed");
    private void OnServerDisconnected() => Fail("ServerDisconnected");
    private void Fail(string reason) { Stop(); Emit(reason); }
    private void Emit(string reason) { GD.Print($"LOBBY STATUS {reason}"); StatusChanged?.Invoke(reason); }

    private void Publish()
    {
        var snapshot = Snapshot;
        if (snapshot is null) return;
        GD.Print($"LOBBY SNAPSHOT revision={snapshot.Revision} phase={snapshot.Phase} roster={string.Join('|', snapshot.Players.OrderBy(player => player.DisplayName, StringComparer.Ordinal).Select(player => $"{player.DisplayName}:{player.Ready}"))}");
        SnapshotChanged?.Invoke(snapshot);
    }

    private void Broadcast()
    {
        if (_host is null) return;
        foreach (var message in _host.Broadcast()) RpcId(message.ConnectionId, MethodName.ServerMessage, message.Json);
        Publish();
    }

    private void DisconnectPeer(long connection)
    {
        _peer?.DisconnectPeer((int)connection);
        OnPeerDisconnected(connection);
    }

    [Rpc(MultiplayerApi.RpcMode.AnyPeer, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ClientMessage(string json)
    {
        if (_host is null) return;
        var sender = Multiplayer.GetRemoteSenderId();
        if (_closing.Contains(sender)) return;
        var dispatch = _host.Handle(sender, json);
        foreach (var message in dispatch.Messages) RpcId(message.ConnectionId, MethodName.ServerMessage, message.Json);
        if (_host.GetPlayers().Any(player => player.ConnectionId?.Value == sender)) _handshaken.Add(sender);
        Publish();
        if (dispatch.DisconnectSender)
        {
            _closing.Add(sender);
            // Allow the reliable rejection receipt to flush before closing.
            var generation = _generation;
            GetTree().CreateTimer(0.25).Timeout += () =>
            {
                if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree()) DisconnectPeer(sender);
            };
        }
    }

    [Rpc(TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ServerMessage(string json)
    {
        if (_host is not null || Multiplayer.GetRemoteSenderId() != 1) return;
        var update = _client.Apply(json);
        if (update == LobbyClientUpdate.Rejected) { Fail(_client.LastReason); return; }
        if (update is LobbyClientUpdate.Joined or LobbyClientUpdate.Snapshot) Publish();
        if (update == LobbyClientUpdate.Joined) Emit("Joined");
        if (update == LobbyClientUpdate.RequestResult) Emit(_client.LastReason);
    }
}

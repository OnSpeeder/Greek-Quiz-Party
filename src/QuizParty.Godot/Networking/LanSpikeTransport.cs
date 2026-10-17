using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Networking;

/// <summary>ENet adapter for the isolated Phase 01 probe. No game rules or players.</summary>
public partial class LanSpikeTransport : Node
{
    public const int DefaultPort = 7777;
    private ENetMultiplayerPeer? _peer;
    private ProbeInbox _inbox = new();
    private bool _hosting;
    private bool _ready;
    private int _generation;
    private string? _pendingRequest;

    public event Action<string>? Trace;
    public event Action<bool>? ReadyChanged;
    public event Action<int>? Acknowledged;
    public int ClientProtocol { get; set; } = ProbeInbox.ProtocolVersion;

    public override void _Ready()
    {
        Multiplayer.ConnectedToServer += OnConnected;
        Multiplayer.ConnectionFailed += OnConnectionFailed;
        Multiplayer.ServerDisconnected += OnServerDisconnected;
        Multiplayer.PeerDisconnected += OnPeerDisconnected;
    }

    public Error Host(int port = DefaultPort)
    {
        Stop();
        if (port is < 1024 or > 65535) return Error.InvalidParameter;
        var peer = new ENetMultiplayerPeer();
        var result = peer.CreateServer(port, ProbeInbox.MaxClients);
        if (result != Error.Ok) { peer.Dispose(); return result; }
        _hosting = true;
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        Emit($"HOST_LISTENING port={port}");
        return Error.Ok;
    }

    public Error Join(string address, int port = DefaultPort)
    {
        Stop();
        address = address.Trim();
        if (address.Length is < 1 or > 253 || address.Any(char.IsWhiteSpace) || port is < 1024 or > 65535)
            return Error.InvalidParameter;
        var peer = new ENetMultiplayerPeer();
        var result = peer.CreateClient(address, port);
        if (result != Error.Ok) { peer.Dispose(); return result; }
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        Emit($"CLIENT_CONNECTING address={address} port={port}");
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (GodotObject.IsInstanceValid(this) && IsInsideTree() && generation == _generation && !_ready)
                Fail("CONNECTION_TIMEOUT");
        };
        return Error.Ok;
    }

    public void SendAction(bool repeatPending = false)
    {
        if (!_ready || _hosting) return;
        if (!repeatPending || _pendingRequest is null)
            _pendingRequest = Guid.NewGuid().ToString("N");
        RpcId(1, MethodName.ReceiveAction, ClientProtocol, _pendingRequest);
        Emit("CLIENT_ACTION_SENT");
    }

    public void Stop()
    {
        _generation++;
        _ready = false;
        _hosting = false;
        _pendingRequest = null;
        _inbox = new ProbeInbox();
        if (_peer is not null)
        {
            Multiplayer.MultiplayerPeer = new OfflineMultiplayerPeer();
            _peer.Close();
            _peer.Dispose();
            _peer = null;
        }
        ReadyChanged?.Invoke(false);
    }

    public override void _ExitTree()
    {
        Multiplayer.ConnectedToServer -= OnConnected;
        Multiplayer.ConnectionFailed -= OnConnectionFailed;
        Multiplayer.ServerDisconnected -= OnServerDisconnected;
        Multiplayer.PeerDisconnected -= OnPeerDisconnected;
        Stop();
    }

    private void OnConnected() => RpcId(1, MethodName.Hello, ClientProtocol, OS.GetName());
    private void OnConnectionFailed() => Fail("CONNECTION_FAILED");
    private void OnServerDisconnected() => Fail("SERVER_DISCONNECTED");
    private void OnPeerDisconnected(long id)
    {
        if (_hosting) { _inbox.Disconnect(id); Emit($"PEER_DISCONNECTED peer={id}"); }
    }

    private void Fail(string reason)
    {
        Stop();
        Emit(reason);
    }

    private void Emit(string message)
    {
        GD.Print($"LAN_SPIKE {message}");
        Trace?.Invoke(message);
    }

    [Rpc(MultiplayerApi.RpcMode.AnyPeer, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void Hello(int protocol, string platform)
    {
        if (!_hosting) return;
        var sender = Multiplayer.GetRemoteSenderId();
        var accepted = _inbox.TryHello(sender, protocol, platform);
        Emit($"HOST_HELLO peer={sender} accepted={accepted}");
        RpcId(sender, MethodName.HelloResult, accepted);
    }

    [Rpc(TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void HelloResult(bool accepted)
    {
        if (_hosting || Multiplayer.GetRemoteSenderId() != 1) return;
        if (!accepted) { Fail("HELLO_REJECTED"); return; }
        _ready = true;
        Emit("CLIENT_READY");
        ReadyChanged?.Invoke(true);
    }

    [Rpc(MultiplayerApi.RpcMode.AnyPeer, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ReceiveAction(int protocol, string requestId)
    {
        if (!_hosting) return;
        var sender = Multiplayer.GetRemoteSenderId();
        var receipt = _inbox.Receive(sender, protocol, requestId);
        if (!receipt.Accepted) { Emit($"HOST_ACTION_REJECTED peer={sender}"); return; }
        Emit($"HOST_ACTION peer={sender} count={receipt.HostCount} duplicate={receipt.Duplicate}");
        RpcId(sender, MethodName.ActionReceipt, requestId, receipt.HostCount);
    }

    [Rpc(TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ActionReceipt(string requestId, int hostCount)
    {
        if (_hosting || !_ready || Multiplayer.GetRemoteSenderId() != 1 ||
            requestId != _pendingRequest || hostCount < 1) return;
        Emit($"CLIENT_ACK count={hostCount}");
        Acknowledged?.Invoke(hostCount);
    }
}

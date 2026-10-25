using Godot;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Networking;

/// <summary>Nonblocking UDP adapter, independent of the gameplay peer and rules.</summary>
public partial class LanDiscovery : Node
{
    private readonly IGameClock _clock = new MonotonicGameClock();
    private PacketPeerUdp? _socket;
    private DiscoveryCatalog? _catalog;
    private DiscoveryReplyLimiter? _limiter;
    private Func<LobbySnapshotDto>? _hostSnapshot;
    private bool _requiresPin;
    private int _gamePort;
    private int _discoveryPort;
    private TimeSpan _nextProbe;
    private bool _scanFinished;
    private string[] _broadcasts = ["255.255.255.255"];
    private string _lastRooms = "";
    public event Action<IReadOnlyList<DiscoveredRoom>>? RoomsChanged;
    public event Action<string>? StatusChanged;
    public IReadOnlyList<DiscoveredRoom> Rooms => _catalog?.Rooms() ?? [];

    public override void _Ready()
    {
        var timer = new global::Godot.Timer { WaitTime = 0.1, Autostart = true };
        timer.Timeout += Poll;
        AddChild(timer);
    }

    public Error Advertise(Func<LobbySnapshotDto> snapshot, int gamePort, bool requiresPin, int discoveryPort = DiscoveryProtocol.DefaultPort)
    {
        Stop();
        if (discoveryPort is < 1024 or > 65535 || gamePort is < 1024 or > 65535) return Error.InvalidParameter;
        var error = Bind(discoveryPort);
        if (error != Error.Ok) { Emit("Unavailable"); return error; }
        _hostSnapshot = snapshot; _gamePort = gamePort; _requiresPin = requiresPin;
        _limiter = new(_clock);
        GD.Print($"DISCOVERY ADVERTISING port={discoveryPort} gamePort={gamePort} requiresPin={requiresPin}");
        return Error.Ok;
    }

    public Error Scan(int discoveryPort = DiscoveryProtocol.DefaultPort)
    {
        Stop();
        if (discoveryPort is < 1024 or > 65535) return Error.InvalidParameter;
        var error = Bind(0);
        if (error != Error.Ok) { Emit("Unavailable"); return error; }
        _discoveryPort = discoveryPort;
        // Limited broadcast can select a VPN/virtual adapter on Windows. Also probe
        // each active IPv4 subnet explicitly; replies still enter the same nonce gate.
        if (OS.HasFeature("windows"))
        {
            try
            {
                _broadcasts = NetworkInterface.GetAllNetworkInterfaces().Where(n => n.OperationalStatus == OperationalStatus.Up)
                    .SelectMany(n => n.GetIPProperties().UnicastAddresses)
                    .Where(a => a.Address.AddressFamily == AddressFamily.InterNetwork && !IPAddress.IsLoopback(a.Address))
                    .Select(a => SubnetBroadcast(a.Address, a.IPv4Mask)).Where(a => a is not null)
                    .Cast<string>().Append("255.255.255.255").Distinct().Take(16).ToArray();
            }
            catch (NetworkInformationException networkError) { GD.PushWarning($"Subnet discovery unavailable: {networkError.Message}"); }
        }
        _catalog = new(_clock); _catalog.BeginScan();
        _nextProbe = _clock.Now;
        RoomsChanged?.Invoke([]);
        Emit("Scanning");
        return Error.Ok;
    }

    private Error Bind(int port)
    {
        var socket = new PacketPeerUdp();
        var error = socket.Bind(port, "0.0.0.0", 32768);
        if (error != Error.Ok) { socket.Dispose(); return error; }
        socket.SetBroadcastEnabled(true);
        _socket = socket;
        return Error.Ok;
    }

    private void Poll()
    {
        if (_catalog?.Scanning == true && _clock.Now >= _nextProbe)
        {
            _nextProbe = _clock.Now + TimeSpan.FromSeconds(1);
            var sent = false;
            foreach (var address in _broadcasts)
            {
                sent |= Send(address, _discoveryPort, DiscoveryProtocol.Request(_catalog.Nonce));
                GD.Print($"DISCOVERY PROBE broadcast={address}");
            }
            if (!sent) { Emit("Unavailable"); Stop(); return; }
        }
        // Bound work per timer tick even under malformed-datagram floods.
        for (var count = 0; count < 16 && _socket is { } socket && socket.GetAvailablePacketCount() > 0; count++)
        {
            var packet = socket.GetPacket();
            if (socket.GetPacketError() != Error.Ok) continue;
            var source = socket.GetPacketIP(); var sourcePort = socket.GetPacketPort();
            if (_hostSnapshot is { } snapshot && DiscoveryProtocol.TryRequest(packet, out var request) && _limiter!.Allow(source))
                Send(source, sourcePort, DiscoveryProtocol.Response(request!.Nonce, snapshot(), _gamePort, _requiresPin));
            else if (_catalog?.Accept(packet, source) == true)
                GD.Print($"DISCOVERY REPLY source={source}");
        }
        if (_catalog is null) return;
        var rooms = _catalog.Rooms();
        var signature = string.Join('|', rooms.Select(r => $"{r.Address}:{r.Room.SessionId}:{r.Room.GamePort}:{r.Room.Players}:{r.Room.State}"));
        if (signature != _lastRooms) { _lastRooms = signature; RoomsChanged?.Invoke(rooms); }
        if (_catalog is not null && !_catalog.Scanning && !_scanFinished)
        { _scanFinished = true; Emit(rooms.Count == 0 ? "NoRooms" : "Finished"); }
    }

    public static string? SubnetBroadcast(IPAddress address, IPAddress mask)
    {
        var ip = address.GetAddressBytes(); var subnet = mask.GetAddressBytes();
        if (ip.Length != 4 || subnet.Length != 4 || subnet.All(b => b == 0) || subnet.All(b => b == 255) ||
            ip[0] is 0 or 127 or >= 224 || ip[0] == 169 && ip[1] == 254) return null;
        return new IPAddress(ip.Select((value, i) => (byte)(value | (byte)~subnet[i])).ToArray()).ToString();
    }

    private bool Send(string address, int port, byte[] bytes)
    {
        if (_socket is not { } socket) return false;
        var error = socket.SetDestAddress(address, port);
        if (error == Error.Ok) error = socket.PutPacket(bytes);
        if (error == Error.Ok) return true;
        GD.PushWarning($"Discovery UDP send failed: {error}");
        return false;
    }

    private void Emit(string reason) { GD.Print($"DISCOVERY STATUS {reason}"); StatusChanged?.Invoke(reason); }
    public void Stop()
    {
        _socket?.Close(); _socket?.Dispose(); _socket = null;
        _hostSnapshot = null; _catalog = null; _limiter = null; _scanFinished = false; _lastRooms = "";
        RoomsChanged?.Invoke([]);
    }
    public override void _ExitTree() => Stop();
}

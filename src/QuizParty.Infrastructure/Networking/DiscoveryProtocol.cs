using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using QuizParty.Core.Time;

namespace QuizParty.Infrastructure.Networking;

public sealed record DiscoveryRequest(string Type, int Protocol, Guid Nonce);
public sealed record DiscoveryAnnouncement(string Type, int Protocol, Guid Nonce, Guid SessionId,
    string RoomName, int GamePort, int Players, int MaxPlayers, bool RequiresPin, string AppVersion, string State);
public sealed record DiscoveredRoom(string Address, DiscoveryAnnouncement Room, TimeSpan LastSeen);

/// <summary>Small, strict, versioned UDP messages. No trusted address or secret is advertised.</summary>
public static class DiscoveryProtocol
{
    public const int DefaultPort = 7778;
    public const int MaxPacketBytes = 1024;
    private static readonly string[] RequestFields = ["Type", "Protocol", "Nonce"];
    private static readonly string[] ResponseFields = ["Type", "Protocol", "Nonce", "SessionId", "RoomName", "GamePort", "Players", "MaxPlayers", "RequiresPin", "AppVersion", "State"];
    private static readonly JsonSerializerOptions Options = new() { MaxDepth = 4, UnmappedMemberHandling = JsonUnmappedMemberHandling.Disallow };
    private static readonly UTF8Encoding Utf8 = new(false, true);

    public static byte[] Request(Guid nonce) => JsonSerializer.SerializeToUtf8Bytes(new DiscoveryRequest("quiz-discover", LobbyProtocol.Version, nonce), Options);
    public static byte[] Response(Guid nonce, LobbySnapshotDto lobby, int gamePort, bool requiresPin) =>
        JsonSerializer.SerializeToUtf8Bytes(new DiscoveryAnnouncement("quiz-host", LobbyProtocol.Version, nonce,
            lobby.SessionId, lobby.RoomName, gamePort, lobby.Players.Length, lobby.MaxPlayers, requiresPin, LobbyProtocol.AppVersion, lobby.Phase), Options);

    public static bool TryRequest(byte[] packet, out DiscoveryRequest? request) =>
        Read(packet, RequestFields, out request) && request is { Type: "quiz-discover", Protocol: LobbyProtocol.Version } && request.Nonce != Guid.Empty;

    public static bool TryResponse(byte[] packet, out DiscoveryAnnouncement? room) =>
        Read(packet, ResponseFields, out room) && room is { Type: "quiz-host", Protocol: LobbyProtocol.Version, MaxPlayers: >= 2 and <= 8,
            GamePort: >= 1024 and <= 65535, Players: >= 0 and <= 8, State: "Lobby" or "GameStarting" } &&
        room.Players <= room.MaxPlayers && room.Nonce != Guid.Empty && room.SessionId != Guid.Empty && LobbyProtocol.ValidName(room.RoomName) && room.AppVersion is { Length: > 0 and <= 32 };

    public static bool ValidSource(string address) => IPAddress.TryParse(address, out var ip) && ip.AddressFamily == AddressFamily.InterNetwork &&
        !ip.Equals(IPAddress.Any) && !ip.Equals(IPAddress.Broadcast) && ip.GetAddressBytes()[0] is > 0 and < 224;

    private static bool Read<T>(byte[] packet, string[] fields, out T? value) where T : class
    {
        value = null;
        if (packet.Length is 0 or > MaxPacketBytes) return false;
        try
        {
            var text = Utf8.GetString(packet);
            using var document = JsonDocument.Parse(text, new JsonDocumentOptions { MaxDepth = 4 });
            if (document.RootElement.ValueKind != JsonValueKind.Object) return false;
            foreach (var property in document.RootElement.EnumerateObject())
                if (property.Value.ValueKind == JsonValueKind.String) Utf8.GetByteCount(property.Value.GetString()!);
            var names = document.RootElement.EnumerateObject().Select(p => p.Name).ToArray();
            if (names.Length != fields.Length || !names.Order(StringComparer.Ordinal).SequenceEqual(fields.Order(StringComparer.Ordinal))) return false;
            value = JsonSerializer.Deserialize<T>(text, Options);
            return value is not null;
        }
        catch (JsonException) { return false; }
        catch (DecoderFallbackException) { return false; }
        catch (EncoderFallbackException) { return false; }
        // System.Text.Json rejects unpaired escaped UTF-16 during string access.
        catch (InvalidOperationException) { return false; }
    }
}

/// <summary>Only replies to the current short-lived nonce enter the bounded browser.</summary>
public sealed class DiscoveryCatalog(IGameClock clock)
{
    public static readonly TimeSpan ScanDuration = TimeSpan.FromSeconds(5);
    public static readonly TimeSpan RoomLifetime = TimeSpan.FromSeconds(6);
    public const int MaxRooms = 32;
    private readonly Dictionary<(Guid Session, string Address), DiscoveredRoom> _rooms = new();
    private TimeSpan _scanEnds;
    public Guid Nonce { get; private set; }
    public bool Scanning => Nonce != Guid.Empty && clock.Now < _scanEnds;

    public Guid BeginScan()
    {
        Nonce = Guid.NewGuid(); _scanEnds = clock.Now + ScanDuration;
        _rooms.Clear();
        return Nonce;
    }

    public bool Accept(byte[] packet, string sourceAddress)
    {
        Expire();
        if (!Scanning || !DiscoveryProtocol.ValidSource(sourceAddress) || !DiscoveryProtocol.TryResponse(packet, out var room) ||
            room!.Nonce != Nonce) return false;
        var address = IPAddress.Parse(sourceAddress).ToString();
        var key = (room.SessionId, address);
        if (_rooms.Count >= MaxRooms && !_rooms.ContainsKey(key)) return false;
        _rooms[key] = new(address, room, clock.Now);
        return true;
    }

    public IReadOnlyList<DiscoveredRoom> Rooms()
    {
        Expire();
        return Array.AsReadOnly(_rooms.Values.OrderBy(r => r.Room.RoomName, StringComparer.Ordinal).ThenBy(r => r.Address, StringComparer.Ordinal).ToArray());
    }

    private void Expire()
    { foreach (var key in _rooms.Where(p => clock.Now - p.Value.LastSeen >= RoomLifetime).Select(p => p.Key).ToArray()) _rooms.Remove(key); }
}

/// <summary>Bound reply amplification per source and globally; no timers from packets.</summary>
public sealed class DiscoveryReplyLimiter(IGameClock clock)
{
    private readonly Dictionary<string, int> _counts = new(StringComparer.Ordinal);
    private TimeSpan _window = clock.Now;
    private int _total;
    public bool Allow(string source)
    {
        if (!DiscoveryProtocol.ValidSource(source)) return false;
        if (clock.Now - _window >= TimeSpan.FromSeconds(1)) { _counts.Clear(); _total = 0; _window = clock.Now; }
        if (_total >= 32 || _counts.GetValueOrDefault(source) >= 4) return false;
        _counts[source] = _counts.GetValueOrDefault(source) + 1; _total++;
        return true;
    }
}

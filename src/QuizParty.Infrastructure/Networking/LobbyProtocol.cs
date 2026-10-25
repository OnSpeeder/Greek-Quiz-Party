using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace QuizParty.Infrastructure.Networking;

public sealed record LobbyEnvelope(int ProtocolVersion, string MessageType, Guid MessageId,
    Guid SessionId, Guid? CorrelationId, JsonElement Payload);
public sealed record ClientHelloDto(string AppVersion, string DisplayName, string Platform, string Pin = "", int? CharacterId = null, bool UsePreflight = false);
public sealed record RoomAccessRequestDto(string AppVersion, string Platform, string Pin);
public sealed record RoomAvailabilityRequestDto;
public sealed record RoomAccessResultDto(bool Accepted, string Reason, long Revision, int[] TakenCharacters);
public sealed record ReadyRequestDto([property: JsonRequired] bool Ready, int LocalSlot = 0);
public sealed record AddLocalPlayerDto(string DisplayName, [property: JsonRequired] int LocalSlot, int? CharacterId = null);
public sealed record RemoveLocalPlayerDto([property: JsonRequired] int LocalSlot);
public sealed record StartRequestDto;
public sealed record LobbyPlayerDto(Guid PlayerId, string DisplayName, bool IsHost, bool Ready,
    Guid? ControllerId = null, int LocalSlot = 0, int? TeamId = null, int? CharacterId = null);
public sealed record LobbySnapshotDto(Guid SessionId, long Revision, string RoomName, string Phase, LobbyPlayerDto[] Players, bool TeamMode = false);
public sealed record ServerHelloDto(bool Accepted, string Reason, Guid? PlayerId, LobbySnapshotDto? Lobby, Guid? ControllerId = null, int[]? TakenCharacters = null);
public sealed record RequestResultDto(bool Accepted, string Reason);
public sealed record LobbyOutbound(long ConnectionId, string Json);
public sealed record LobbyDispatch(IReadOnlyList<LobbyOutbound> Messages, bool DisconnectSender);

public static class LobbyProtocol
{
    public const int Version = 8;
    public const int MaxPacketBytes = 16384;
    public const int MaxNameLength = 32;
    public const string AppVersion = "0.8.0";
    private static readonly JsonSerializerOptions Options = new()
    {
        MaxDepth = 8,
        UnmappedMemberHandling = JsonUnmappedMemberHandling.Disallow
    };

    public static string Encode<T>(string type, Guid sessionId, T payload, Guid? correlationId = null, Guid? messageId = null) =>
        JsonSerializer.Serialize(new LobbyEnvelope(Version, type, messageId ?? Guid.NewGuid(), sessionId,
            correlationId, JsonSerializer.SerializeToElement(payload, Options)), Options);

    public static bool TryDecode(string json, out LobbyEnvelope? packet)
    {
        packet = null;
        if (string.IsNullOrEmpty(json) || json.Length > MaxPacketBytes || Encoding.UTF8.GetByteCount(json) > MaxPacketBytes) return false;
        try
        {
            var decoded = JsonSerializer.Deserialize<LobbyEnvelope>(json, Options);
            if (decoded is null || decoded.MessageId == Guid.Empty || decoded.MessageType is not
                ("ClientHello" or "SetReady" or "StartGame" or "ServerHello" or "RequestResult" or "LobbySnapshot" or
                 "SubmitAnswer" or "AdvanceMatch" or "MatchSnapshot" or "AnswerAccepted" or "ActivateCard" or "CardResult" or
                 "AddLocalPlayer" or "RemoveLocalPlayer" or "SetTeam" or "CheckRoom" or "RoomAvailability" or "RoomAccessResult") ||
                decoded.Payload.ValueKind != JsonValueKind.Object) return false;
            packet = decoded;
            return true;
        }
        catch (JsonException) { return false; }
    }

    public static bool TryPayload<T>(LobbyEnvelope packet, out T? payload) where T : class
    {
        try { payload = packet.Payload.Deserialize<T>(Options); return payload is not null; }
        catch (JsonException) { payload = null; return false; }
    }

    public static bool ValidName(string? value) => !string.IsNullOrWhiteSpace(value) && value.Length <= MaxNameLength &&
        value == value.Trim() && !value.Any(char.IsControl);
}

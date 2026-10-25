using System.Text.Json;
using QuizParty.Core.Lobby;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class LobbyProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } }
    private static LobbyHost Host(Clock? clock = null) => new("Ελληνική παρέα", "Οικοδεσπότης", clock ?? new());
    private static string Hello(string name = "Άννα", Guid? id = null) => LobbyProtocol.Encode("ClientHello", Guid.Empty,
        new ClientHelloDto(LobbyProtocol.AppVersion, name, "Windows"), messageId: id);
    private static LobbyEnvelope Decode(string json)
    {
        Assert.True(LobbyProtocol.TryDecode(json, out var packet));
        return packet!;
    }
    private static string Reason(LobbyDispatch dispatch)
    {
        var packet = Decode(dispatch.Messages[0].Json);
        if (packet.MessageType == "ServerHello")
        {
            Assert.True(LobbyProtocol.TryPayload<ServerHelloDto>(packet, out var hello));
            return hello!.Reason;
        }
        Assert.True(LobbyProtocol.TryPayload<RequestResultDto>(packet, out var result));
        return result!.Reason;
    }

    [Fact]
    public void TwoClientsObserveIdenticalRosterReadinessAndHostStartWithDistinctAssignedPlayers()
    {
        var host = Host();
        var first = new LobbyClientState();
        var second = new LobbyClientState();
        var firstJoin = host.Handle(2, first.BeginHello("Άννα", "Windows"));
        Assert.Equal(LobbyClientUpdate.Joined, first.Apply(firstJoin.Messages[0].Json));
        var secondJoin = host.Handle(3, second.BeginHello("Μαρία", "Android"));
        Assert.Equal(LobbyClientUpdate.Joined, second.Apply(secondJoin.Messages[0].Json));
        foreach (var message in secondJoin.Messages)
            if (message.ConnectionId == 2) first.Apply(message.Json);
        Assert.NotEqual(first.PlayerId, second.PlayerId);
        Assert.Equal(3, first.Snapshot!.Players.Length);
        var firstReady = host.Handle(2, first.CreateReady(true)!);
        foreach (var message in firstReady.Messages)
        {
            if (message.ConnectionId == 2) first.Apply(message.Json);
            if (message.ConnectionId == 3) second.Apply(message.Json);
        }
        var secondReady = host.Handle(3, second.CreateReady(true)!);
        foreach (var message in secondReady.Messages)
        {
            if (message.ConnectionId == 2) first.Apply(message.Json);
            if (message.ConnectionId == 3) second.Apply(message.Json);
        }
        host.SetHostReady(true);
        Assert.Equal(LobbyError.None, host.Start());
        foreach (var message in host.Broadcast())
        {
            if (message.ConnectionId == 2) first.Apply(message.Json);
            if (message.ConnectionId == 3) second.Apply(message.Json);
        }
        Assert.Equal("GameStarting", first.Snapshot!.Phase);
        Assert.Equal(JsonSerializer.Serialize(host.Snapshot()), JsonSerializer.Serialize(first.Snapshot));
        Assert.Equal(JsonSerializer.Serialize(first.Snapshot), JsonSerializer.Serialize(second.Snapshot));
        Assert.All(first.Snapshot.Players, player => Assert.True(player.Ready));
    }

    [Fact]
    public void DuplicateHelloAndReadyReturnOriginalReceiptsWithoutRepeatedMutations()
    {
        var host = Host();
        var hello = Hello();
        var joined = host.Handle(2, hello);
        var revision = host.Snapshot().Revision;
        var duplicate = host.Handle(2, hello);
        Assert.Equal(joined.Messages[0], Assert.Single(duplicate.Messages));
        Assert.Equal(revision, host.Snapshot().Revision);
        var ready = LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(true));
        var original = host.Handle(2, ready);
        var changedRevision = host.Snapshot().Revision;
        Assert.Equal(original.Messages[0], Assert.Single(host.Handle(2, ready).Messages));
        Assert.Equal(changedRevision, host.Snapshot().Revision);
        var altered = ready.Replace("true", "false", StringComparison.Ordinal);
        Assert.Equal("RequestConflict", Reason(host.Handle(2, altered)));
        Assert.True(host.Snapshot().Players.Single(player => !player.IsHost).Ready);
    }

    [Fact]
    public void ClientStartAndWrongSessionAndUnhandshakenChangesAreRejected()
    {
        var host = Host();
        Assert.Equal("HandshakeRequired", Reason(host.Handle(3,
            LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(true)))));
        host.Handle(2, Hello());
        Assert.Equal("WrongSession", Reason(host.Handle(2,
            LobbyProtocol.Encode("SetReady", Guid.NewGuid(), new ReadyRequestDto(true)))));
        Assert.Equal("NotHost", Reason(host.Handle(2, LobbyProtocol.Encode("StartGame", host.SessionId, new StartRequestDto()))));
        Assert.Equal("Lobby", host.Snapshot().Phase);
        Assert.False(host.Snapshot().Players.Single(player => !player.IsHost).Ready);
    }

    [Fact]
    public void IncompatibleVersionIsRejectedBeforeAdmission()
    {
        var host = Host();
        var request = Hello().Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", "\"ProtocolVersion\":99", StringComparison.Ordinal);
        var rejected = host.Handle(2, request);
        Assert.Equal("IncompatibleVersion", Reason(rejected));
        Assert.True(rejected.DisconnectSender);
        Assert.Single(host.Snapshot().Players);
    }

    [Theory]
    [InlineData("")]
    [InlineData(" ")]
    [InlineData(" leading")]
    [InlineData("trailing ")]
    [InlineData("line\nbreak")]
    public void InvalidNamesAreRejected(string name)
    {
        Assert.Equal("MalformedRequest", Reason(Host().Handle(2, Hello(name))));
    }

    [Fact]
    public void OversizedStringsPayloadsUnknownFieldsAndMissingReadyAreRejected()
    {
        var host = Host();
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, Hello(new string('a', 33)))));
        host.Handle(2, Hello());
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, LobbyProtocol.Encode("SetReady", host.SessionId, new { }))));
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, LobbyProtocol.Encode("SetReady", host.SessionId, new { Ready = true, PlayerId = Guid.NewGuid() }))));
        Assert.False(LobbyProtocol.TryDecode(new string('a', LobbyProtocol.MaxPacketBytes + 1), out _));
        Assert.False(LobbyProtocol.TryDecode(Hello() + new string('α', LobbyProtocol.MaxPacketBytes / 2), out _));
        var oversizedUtf8 = Hello("a").Replace("\"a\"", "\"" + new string('α', 9000) + "\"", StringComparison.Ordinal);
        Assert.True(oversizedUtf8.Length < LobbyProtocol.MaxPacketBytes);
        Assert.False(LobbyProtocol.TryDecode(oversizedUtf8, out _));
        Assert.False(LobbyProtocol.TryDecode("{bad-json", out _));
        Assert.False(LobbyProtocol.TryDecode("null", out _));
        Assert.False(LobbyProtocol.TryDecode("[]", out _));
        Assert.False(host.Snapshot().Players.Single(player => !player.IsHost).Ready);
    }

    [Fact]
    public void UnknownTypesBadMetadataAndMalformedPayloadTypesDoNotMutateRoster()
    {
        var host = Host();
        Assert.False(LobbyProtocol.TryDecode(LobbyProtocol.Encode("Unknown", Guid.Empty, new { }), out _));
        Assert.False(LobbyProtocol.TryDecode(LobbyProtocol.Encode("ClientHello", Guid.Empty, new { }, messageId: Guid.Empty), out _));
        Assert.False(LobbyProtocol.TryDecode(LobbyProtocol.Encode("ClientHello", Guid.Empty, new[] { 1, 2 }), out _));
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, LobbyProtocol.Encode("ClientHello", Guid.Empty,
            new ClientHelloDto("0.1", "Άννα", "Unsupported")))));
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, LobbyProtocol.Encode("ClientHello", Guid.Empty,
            new { AppVersion = "0.1", DisplayName = "Άννα", Platform = "Windows", PlayerId = Guid.NewGuid() }))));
        Assert.Single(host.Snapshot().Players);
    }

    [Fact]
    public void FullAndStartedRoomsRejectJoinsAndDisconnectFreesIdentityAndSeat()
    {
        var host = Host();
        for (var connection = 2; connection <= 8; connection++) Assert.Equal("None", Reason(host.Handle(connection, Hello($"Player{connection}"))));
        Assert.Equal("RoomFull", Reason(host.Handle(9, Hello())));
        var oldId = host.GetPlayers().Single(player => player.ConnectionId?.Value == 2).Id;
        Assert.True(host.Disconnect(2));
        Assert.False(host.Disconnect(2));
        Assert.Equal("None", Reason(host.Handle(2, Hello())));
        Assert.NotEqual(oldId, host.GetPlayers().Single(player => player.ConnectionId?.Value == 2).Id);
        for (var connection = 2; connection <= 8; connection++) host.Handle(connection,
            LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(true)));
        host.SetHostReady(true);
        Assert.Equal(LobbyError.None, host.Start());
        Assert.Equal("GameStarted", Reason(host.Handle(10, Hello())));
    }

    [Fact]
    public void RateLimitAndMalformedStrikeLimitRequestDisconnect()
    {
        var clock = new Clock();
        var host = Host(clock);
        var request = Hello();
        for (var index = 0; index < LobbyHost.MaxMessagesPerSecond; index++) Assert.False(host.Handle(2, request).DisconnectSender);
        Assert.True(host.Handle(2, request).DisconnectSender);
        clock.Now += TimeSpan.FromSeconds(1);
        Assert.False(host.Handle(2, request).DisconnectSender);
        Assert.False(host.Handle(3, "bad").DisconnectSender);
        Assert.False(host.Handle(3, "bad").DisconnectSender);
        Assert.True(host.Handle(3, "bad").DisconnectSender);
        Assert.True(host.Handle(1, request).DisconnectSender);
    }

    [Fact]
    public void PendingConnectionsAreBoundedAndDisconnectedCachesCanBeReused()
    {
        var host = Host();
        for (var connection = 2; connection < LobbyHost.MaxTransportConnections + 2; connection++)
            Assert.False(host.Handle(connection, Hello($"Player{connection}")).DisconnectSender);
        Assert.True(host.Handle(99, Hello()).DisconnectSender);
        host.Disconnect(2);
        Assert.False(host.Handle(99, Hello()).DisconnectSender);
    }

    [Fact]
    public void BoundedReceiptCacheDisconnectsRatherThanEvictingAndReapplyingOldRequests()
    {
        var clock = new Clock();
        var host = Host(clock);
        var hello = Hello();
        host.Handle(2, hello);
        for (var index = 1; index < LobbyHost.MaxRequestsPerConnection; index++)
        {
            clock.Now += TimeSpan.FromSeconds(1);
            Assert.False(host.Handle(2, LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(index % 2 == 0))).DisconnectSender);
        }
        clock.Now += TimeSpan.FromSeconds(1);
        var limited = host.Handle(2, LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(true)));
        Assert.True(limited.DisconnectSender);
        Assert.Equal("RequestLimit", Reason(limited));
        Assert.Equal("None", Reason(host.Handle(2, hello)));
    }

    [Fact]
    public void ClientRejectsUnsolicitedHelloWrongSessionAndStaleSnapshots()
    {
        var host = Host();
        var client = new LobbyClientState();
        var join = host.Handle(2, client.BeginHello("Άννα", "Windows"));
        var original = join.Messages[0].Json;
        var envelope = Decode(original);
        Assert.True(LobbyProtocol.TryPayload<ServerHelloDto>(envelope, out var payload));
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("ServerHello", host.SessionId, payload!, Guid.NewGuid())));
        Assert.Equal(LobbyClientUpdate.Joined, client.Apply(original));
        var before = client.Snapshot!;
        var otherSession = before with { SessionId = Guid.NewGuid(), Revision = 999 };
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("LobbySnapshot", otherSession.SessionId, otherSession)));
        host.Handle(3, Hello("Μαρία"));
        Assert.Equal(LobbyClientUpdate.Snapshot, client.Apply(host.Broadcast().First(message => message.ConnectionId == 2).Json));
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("LobbySnapshot", host.SessionId, before)));
        Assert.Equal(3, client.Snapshot!.Players.Length);
        var copy = client.Snapshot;
        copy.Players[0] = copy.Players[0] with { DisplayName = "tampered" };
        Assert.DoesNotContain(client.Snapshot!.Players, player => player.DisplayName == "tampered");
    }

    [Fact]
    public void ClientIgnoresMalformedSnapshotsUncorrelatedResultsAndDuplicatePlayerIds()
    {
        var host = Host();
        var client = new LobbyClientState();
        var join = host.Handle(2, client.BeginHello("Άννα", "Windows"));
        client.Apply(join.Messages[0].Json);
        var snapshot = host.Snapshot();
        var bad = snapshot with { Revision = 999, Players = [snapshot.Players[0], snapshot.Players[0]] };
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("LobbySnapshot", host.SessionId, bad)));
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("RequestResult", host.SessionId,
            new RequestResultDto(false, "NotHost"), Guid.NewGuid())));
        var request = client.CreateStartRequest()!;
        var rejection = host.Handle(2, request);
        Assert.Equal(LobbyClientUpdate.RequestResult, client.Apply(rejection.Messages[0].Json));
        Assert.Equal("NotHost", client.LastReason);
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(rejection.Messages[0].Json));
    }
}

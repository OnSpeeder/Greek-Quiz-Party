using System.Text;
using System.Text.Json;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class DiscoveryAndAdmissionTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100); }
    private static LobbySnapshotDto Lobby => new(Guid.NewGuid(), 1, "Ελληνική παρέα", "Lobby", [new(Guid.NewGuid(), "Host", true, true)]);
    private static string Reason(LobbyDispatch dispatch)
    {
        Assert.True(LobbyProtocol.TryDecode(dispatch.Messages[0].Json, out var packet));
        Assert.True(LobbyProtocol.TryPayload<ServerHelloDto>(packet!, out var hello));
        return hello!.Reason;
    }

    [Fact]
    public void BroadcastCodecRoundTripsGreekMetadataWithoutSecretsOrAdvertisedAddresses()
    {
        var nonce = Guid.NewGuid();
        Assert.True(DiscoveryProtocol.TryRequest(DiscoveryProtocol.Request(nonce), out var request));
        Assert.Equal(nonce, request!.Nonce);
        var bytes = DiscoveryProtocol.Response(nonce, Lobby, 17777, true);
        Assert.True(DiscoveryProtocol.TryResponse(bytes, out var room));
        Assert.Equal("Ελληνική παρέα", room!.RoomName); Assert.True(room.RequiresPin);
        Assert.Equal(17777, room.GamePort); Assert.Equal(nonce, room.Nonce);
        Assert.DoesNotContain("Address", Encoding.UTF8.GetString(bytes));
        Assert.DoesNotContain("Token", Encoding.UTF8.GetString(bytes));
        Assert.InRange(bytes.Length, 1, DiscoveryProtocol.MaxPacketBytes);
    }

    [Fact]
    public void InvalidPacketsAndSpoofedFieldsAreIgnoredWithoutExceptions()
    {
        var valid = Encoding.UTF8.GetString(DiscoveryProtocol.Response(Guid.NewGuid(), Lobby, 7777, false));
        var candidates = new[] { "null", "[]", "{}", "{bad", valid.Replace("\"GamePort\":7777", "\"GamePort\":0"),
            valid.Replace("\"Players\":1", "\"Players\":99"), valid.Replace("\"State\":\"Lobby\"", "\"State\":\"Other\""),
            valid.Replace($"\"Protocol\":{LobbyProtocol.Version}", "\"Protocol\":3"),
            valid.Replace("\"RequiresPin\":false,", ""), valid.Replace("\"GamePort\":7777", "\"GamePort\":7777,\"Address\":\"evil\""),
            valid.Replace("\"GamePort\":7777", "\"GamePort\":7777,\"GamePort\":7777"),
            valid.Replace("\"GamePort\":7777", "\"GamePort\":\"7777\""), new string('x', 1025) };
        foreach (var text in candidates) Assert.False(DiscoveryProtocol.TryResponse(Encoding.UTF8.GetBytes(text), out _), text);
        Assert.False(DiscoveryProtocol.TryResponse([0xff, 0xfe], out _));
        Assert.False(DiscoveryProtocol.TryResponse(Encoding.UTF8.GetBytes(valid.Replace(JsonSerializer.Serialize(Lobby.RoomName), "\"\\uD800\"")), out _));
        Assert.False(DiscoveryProtocol.TryRequest(DiscoveryProtocol.Request(Guid.Empty), out _));
        Assert.False(DiscoveryProtocol.TryResponse(DiscoveryProtocol.Response(Guid.Empty, Lobby, 7777, false), out _));
    }

    [Fact]
    public void CatalogUsesObservedSourceRequiresCurrentNonceAndExpiresRooms()
    {
        var clock = new Clock(); var catalog = new DiscoveryCatalog(clock);
        var nonce = catalog.BeginScan(); var lobby = Lobby;
        var response = DiscoveryProtocol.Response(nonce, lobby, 7777, false);
        Assert.True(catalog.Accept(response, "192.168.1.9")); Assert.True(catalog.Accept(response, "192.168.1.9"));
        Assert.Equal("192.168.1.9", Assert.Single(catalog.Rooms()).Address);
        Assert.False(catalog.Accept(response, "255.255.255.255"));
        Assert.False(catalog.Accept(response, "224.1.2.3")); Assert.False(catalog.Accept(response, "hostname"));
        Assert.False(catalog.Accept(DiscoveryProtocol.Response(Guid.NewGuid(), lobby, 7777, false), "192.168.1.8"));
        clock.Now += DiscoveryCatalog.ScanDuration;
        Assert.False(catalog.Accept(response, "192.168.1.9")); Assert.False(catalog.Scanning);
        clock.Now += DiscoveryCatalog.RoomLifetime; Assert.Empty(catalog.Rooms());
        catalog.BeginScan(); Assert.False(catalog.Accept(response, "192.168.1.9"));
    }

    [Fact]
    public void CatalogCapsRoomsAndUpdatesFullOrStartedState()
    {
        var catalog = new DiscoveryCatalog(new Clock()); var nonce = catalog.BeginScan(); var first = Lobby;
        Assert.True(catalog.Accept(DiscoveryProtocol.Response(nonce, first, 7777, true), "127.0.0.1"));
        for (var i = 1; i < DiscoveryCatalog.MaxRooms; i++) Assert.True(catalog.Accept(DiscoveryProtocol.Response(nonce, Lobby, 7777, false), "127.0.0.1"));
        Assert.False(catalog.Accept(DiscoveryProtocol.Response(nonce, Lobby, 7777, false), "127.0.0.1"));
        Assert.True(catalog.Accept(DiscoveryProtocol.Response(nonce, first with { Phase = "GameStarting" }, 17779, true), "127.0.0.1"));
        var updated = catalog.Rooms().Single(r => r.Room.SessionId == first.SessionId);
        Assert.Equal("GameStarting", updated.Room.State); Assert.Equal(17779, updated.Room.GamePort);
    }

    [Fact]
    public void DiscoveryRepliesAreRateLimitedPerSourceAndGlobally()
    {
        var clock = new Clock(); var limiter = new DiscoveryReplyLimiter(clock);
        for (var i = 0; i < 4; i++) Assert.True(limiter.Allow("127.0.0.1"));
        Assert.False(limiter.Allow("127.0.0.1")); Assert.False(limiter.Allow("0.0.0.0"));
        for (var i = 1; i <= 28; i++) Assert.True(limiter.Allow($"192.168.1.{i}"));
        Assert.False(limiter.Allow("192.168.2.1"));
        clock.Now += TimeSpan.FromSeconds(1); Assert.True(limiter.Allow("127.0.0.1"));
    }

    [Theory]
    [InlineData("")] [InlineData("1234")] [InlineData("012345")]
    public void ValidPinsAdmitAndNeverAppearInResponses(string pin)
    {
        var host = new LobbyHost("Room", "Host", new Clock(), pin: pin);
        var client = new LobbyClientState();
        var joined = host.Handle(2, client.BeginHello("Player", "Android", pin), "192.168.1.2");
        Assert.Equal("None", Reason(joined)); Assert.Equal(LobbyClientUpdate.Joined, client.Apply(joined.Messages[0].Json));
        Assert.Equal(pin.Length > 0, host.RequiresPin);
        foreach (var p in joined.Messages) Assert.DoesNotContain("\"Pin\"", p.Json);
    }

    [Theory]
    [InlineData("123")] [InlineData("1234567")] [InlineData("１２３４")] [InlineData("12 4")] [InlineData(null)]
    public void InvalidPinsAreBoundedAtHost(string? pin)
    {
        Assert.Throws<ArgumentException>(() => new RoomAdmission(pin!, new Clock()));
        var host = new LobbyHost("Room", "Host", new Clock(), pin: "0123");
        var request = LobbyProtocol.Encode("ClientHello", Guid.Empty, new ClientHelloDto("test", "Player", "Android", pin!));
        Assert.Equal("MalformedRequest", Reason(host.Handle(2, request))); Assert.Single(host.Snapshot().Players);
    }

    [Fact]
    public void WrongPinLimitSurvivesTransportReconnectAndDuplicateRequestsDoNotCountAgain()
    {
        var clock = new Clock(); var host = new LobbyHost("Room", "Host", clock, pin: "0123");
        var wrong = new LobbyClientState().BeginHello("Player", "Android", "9999");
        var response = host.Handle(2, wrong, "192.168.1.2"); Assert.Equal("WrongPin", Reason(response));
        for (var i = 0; i < 4; i++) Assert.Equal(response.Messages[0], Assert.Single(host.Handle(2, wrong, "192.168.1.2").Messages));
        host.Disconnect(2);
        for (var i = 0; i < 4; i++)
        {
            var connection = i + 3;
            Assert.Equal("WrongPin", Reason(host.Handle(connection, new LobbyClientState().BeginHello("Player", "Android"), "192.168.1.2")));
            host.Disconnect(connection);
        }
        var correct = new LobbyClientState().BeginHello("Player", "Android", "0123");
        Assert.Equal("PinRateLimited", Reason(host.Handle(10, correct, "192.168.1.2")));
        Assert.Equal("None", Reason(host.Handle(11, new LobbyClientState().BeginHello("Other", "Windows", "0123"), "192.168.1.3")));
        clock.Now += RoomAdmission.Window;
        Assert.Equal("None", Reason(host.Handle(12, new LobbyClientState().BeginHello("Player", "Android", "0123"), "192.168.1.2")));
    }

    [Fact]
    public void LobbyRejoinGetsFreshIdentityAndStartedMatchCannotBeReclaimed()
    {
        var host = new LobbyHost("Room", "Host", new Clock(), pin: "1234");
        var first = new LobbyClientState(); var second = new LobbyClientState();
        first.Apply(host.Handle(2, first.BeginHello("Phone", "Android", "1234")).Messages[0].Json);
        var original = first.PlayerId; host.Disconnect(2);
        second.Apply(host.Handle(3, second.BeginHello("Phone", "Android", "1234")).Messages[0].Json);
        Assert.NotEqual(original, second.PlayerId); Assert.False(host.Snapshot().Players.Single(p => !p.IsHost).Ready);
        host.Handle(3, second.CreateReady(true)!); host.Start(); host.Disconnect(3);
        Assert.Equal("GameStarted", Reason(host.Handle(4, new LobbyClientState().BeginHello("Phone", "Android", "1234"))));
    }

    [Fact]
    public void GlobalPinLimitIsBoundedAndClearsAtHostClockWindow()
    {
        var clock = new Clock(); var gate = new RoomAdmission("1234", clock);
        for (var i = 0; i < 100; i++) Assert.Equal("WrongPin", gate.Admit("9999", $"192.168.0.{i + 1}"));
        Assert.Equal("PinRateLimited", gate.Admit("1234", "192.168.1.1"));
        clock.Now += RoomAdmission.Window; Assert.Equal("None", gate.Admit("1234", "192.168.1.1"));
    }

    [Fact]
    public void MatchDepartureKeepsConfirmedScoreAndRejectsReentryAndOldAnswerReplay()
    {
        var clock = new Clock();
        var host = new LobbyHost("Room", "Host", clock, new("q", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Test only"));
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginHello("Phone", "Android")).Messages[0].Json);
        host.Handle(2, client.CreateReady(true)!); host.Start(); host.BeginMatch();
        foreach (var packet in host.BroadcastMatch()) client.Apply(packet.Json);
        var correct = Array.IndexOf(host.MatchSnapshot()!.Question.Answers, "yes");
        clock.Now += TimeSpan.FromSeconds(1);
        var answer = client.Match.CreateAnswer(correct)!;
        host.Handle(2, answer); host.Disconnect(2);
        var replay = host.Handle(2, answer);
        Assert.Contains("HandshakeRequired", replay.Messages[0].Json);
        Assert.Equal("GameStarted", Reason(host.Handle(3, new LobbyClientState().BeginHello("Phone", "Android"))));
        clock.Now += TimeSpan.FromSeconds(20); host.PollMatch(); host.PollMatch(); host.AdvanceMatch(); host.AdvanceMatch();
        var final = host.MatchSnapshot()!;
        Assert.Equal("GameOver", final.Phase);
        Assert.Equal(975, final.Scores.Single(s => s.PlayerId == client.PlayerId).Total);
        Assert.Equal(1, final.Statistics.Single(s => s.PlayerId == client.PlayerId).Correct);
    }
}

using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class RoomPreparationTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } }
    private static RoomAccessResultDto Access(LobbyDispatch dispatch)
    {
        Assert.True(LobbyProtocol.TryDecode(dispatch.Messages[0].Json, out var envelope));
        Assert.True(LobbyProtocol.TryPayload<RoomAccessResultDto>(envelope!, out var result));
        return result!;
    }
    private static ServerHelloDto Hello(LobbyDispatch dispatch)
    {
        Assert.True(LobbyProtocol.TryDecode(dispatch.Messages[0].Json, out var envelope));
        Assert.True(LobbyProtocol.TryPayload<ServerHelloDto>(envelope!, out var result));
        return result!;
    }

    [Fact]
    public void PinPreflightNeverCreatesPlayerOrRevealsAvailabilityOnFailureAndDuplicatesDoNotChargeAgain()
    {
        var host = new LobbyHost("Αίθουσα", "Host", new Clock(), pin: "1234");
        var client = new LobbyClientState();
        var bad = client.BeginAccess(host.SessionId, "0000", "Android");
        var first = host.Handle(2, bad, "phone");
        Assert.Equal("WrongPin", Access(first).Reason); Assert.Empty(Access(first).TakenCharacters);
        for (var i = 0; i < 6; i++) Assert.Equal(first.Messages[0].Json, host.Handle(2, bad, "phone").Messages[0].Json);
        Assert.Single(host.Snapshot().Players);
        var good = host.Handle(2, client.BeginAccess(host.SessionId, "1234", "Android"), "phone");
        Assert.True(Access(good).Accepted); Assert.Equal(new[] { 0 }, Access(good).TakenCharacters);
        Assert.Equal(LobbyClientUpdate.RoomAccess, client.Apply(good.Messages[0].Json));
        Assert.Null(client.PlayerId); Assert.Single(host.Snapshot().Players);
        var escaped = client.Access!.TakenCharacters; escaped[0] = 7;
        Assert.Equal(0, client.Access!.TakenCharacters[0]);
    }

    [Fact]
    public void TwoPreparedClientsRacingSameCharacterLoseAtomicallyAndCanRetryWithoutRenaming()
    {
        var host = new LobbyHost("Αίθουσα", "Host", new Clock());
        var a = new LobbyClientState(); var b = new LobbyClientState();
        Assert.Equal(LobbyClientUpdate.RoomAccess, a.Apply(host.Handle(2, a.BeginAccess(host.SessionId, "", "Windows")).Messages[0].Json));
        Assert.Equal(LobbyClientUpdate.RoomAccess, b.Apply(host.Handle(3, b.BeginAccess(host.SessionId, "", "Android")).Messages[0].Json));
        var requestA = a.BeginPreparedHello("Άννα", "Windows", 4)!;
        var requestB = b.BeginPreparedHello("Μαρία", "Android", 4)!;
        var won = host.Handle(2, requestA);
        Assert.Equal(LobbyClientUpdate.Joined, a.Apply(won.Messages[0].Json));
        var lost = host.Handle(3, requestB);
        Assert.Equal("CharacterTaken", Hello(lost).Reason);
        Assert.Equal(LobbyClientUpdate.Rejected, b.Apply(lost.Messages[0].Json));
        Assert.Contains(4, b.Access!.TakenCharacters); Assert.Null(b.PlayerId);
        Assert.Equal(lost.Messages[0].Json, host.Handle(3, requestB).Messages[0].Json);
        Assert.Equal(2, host.Snapshot().Players.Length);
        Assert.Equal(LobbyClientUpdate.Joined, b.Apply(host.Handle(3, b.BeginPreparedHello("Μαρία", "Android", 6)!).Messages[0].Json));
        Assert.Equal(3, host.Snapshot().Players.Select(p => p.CharacterId).Distinct().Count());
    }

    [Fact]
    public void PreparationIsConnectionBoundExpiresAndCannotBypassPin()
    {
        var clock = new Clock(); var host = new LobbyHost("Room", "Host", clock, pin: "1234");
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginAccess(host.SessionId, "1234", "Android")).Messages[0].Json);
        var forged = LobbyProtocol.Encode("ClientHello", Guid.Empty,
            new ClientHelloDto(LobbyProtocol.AppVersion, "Other", "Android", "", 3, true));
        Assert.Equal("AccessExpired", Hello(host.Handle(3, forged)).Reason);
        clock.Now = TimeSpan.FromMinutes(2);
        Assert.Equal("AccessExpired", Hello(host.Handle(2, client.BeginPreparedHello("Name", "Android", 3)!)).Reason);
        Assert.Single(host.Snapshot().Players);
        var old = client.BeginAccess(host.SessionId, "1234", "Android").Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", "\"ProtocolVersion\":7", StringComparison.Ordinal);
        Assert.True(host.Handle(4, old).DisconnectSender);
    }

    [Fact]
    public void MalformedCharactersAndSpoofedAvailabilityAreRejected()
    {
        var host = new LobbyHost("Room", "Host", new Clock());
        var invalid = LobbyProtocol.Encode("ClientHello", Guid.Empty, new ClientHelloDto(LobbyProtocol.AppVersion, "Name", "Android", "", 10));
        Assert.Equal("MalformedRequest", Hello(host.Handle(2, invalid)).Reason);
        var client = new LobbyClientState();
        var request = client.BeginAccess(host.SessionId, "", "Android");
        LobbyProtocol.TryDecode(request, out var envelope);
        foreach (var characters in new[] { new[] { 0, 0 }, new[] { 10 }, new[] { -1 } })
            Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("RoomAccessResult", host.SessionId,
                new RoomAccessResultDto(true, "None", 1, characters), envelope!.MessageId)));
        Assert.Equal(LobbyClientUpdate.RoomAccess, client.Apply(host.Handle(2, request).Messages[0].Json));
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(LobbyProtocol.Encode("RoomAccessResult", Guid.NewGuid(),
            new RoomAccessResultDto(true, "None", 2, [1]), envelope!.MessageId)));
    }
}

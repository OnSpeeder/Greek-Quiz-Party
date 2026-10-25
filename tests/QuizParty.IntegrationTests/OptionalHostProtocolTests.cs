using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Questions;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class OptionalHostProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } }
    [Fact]
    public void SpectatorHostAdvertisesEmptyRoomEnforcesCapacityAndReceivesNoPrivateProjection()
    {
        var clock = new Clock();
        var questions = Enumerable.Range(0, 12).Select(i => new QuestionDefinition("q" + i, "Test", ["A", "B", "C", "D"], 0, "history", 3, "E")).ToArray();
        var host = new LobbyHost("Room", "", clock, questions, new(10, strategy: new()), hostPlays: false, maxPlayers: 2);
        Assert.Empty(host.Snapshot().Players); Assert.False(host.Snapshot().HostPlays);
        Assert.True(DiscoveryProtocol.TryResponse(DiscoveryProtocol.Response(Guid.NewGuid(), host.Snapshot(), 7777, false), out var room));
        Assert.Equal(0, room!.Players); Assert.Equal(2, room.MaxPlayers);
        var clients = new[] { new LobbyClientState(), new LobbyClientState() };
        for (var i = 0; i < 2; i++)
        {
            var joined = host.Handle(i + 2, clients[i].BeginHello("Player" + i, "Android"));
            Assert.Equal(LobbyClientUpdate.Joined, clients[i].Apply(joined.Messages[0].Json));
            foreach (var packet in host.Broadcast()) clients[packet.ConnectionId - 2].Apply(packet.Json);
            host.Handle(i + 2, clients[i].CreateReady(true)!);
        }
        var third = new LobbyClientState();
        Assert.Equal(LobbyClientUpdate.Rejected, third.Apply(host.Handle(4, third.BeginHello("Third", "Windows")).Messages[0].Json));
        Assert.Equal("RoomFull", third.LastReason);
        Assert.Equal(LobbyError.None, host.Start());
        foreach (var p in host.Broadcast()) clients[p.ConnectionId - 2].Apply(p.Json);
        Assert.True(host.BeginMatch());
        void Sync()
        {
            foreach (var p in host.BroadcastMatch())
            {
                var client = clients[p.ConnectionId - 2];
                var expected = client.Match.Snapshot?.Revision == host.MatchSnapshot()!.Revision ? LobbyClientUpdate.Ignored : LobbyClientUpdate.MatchSnapshot;
                Assert.Equal(expected, client.Apply(p.Json));
            }
        }
        for (var q = 0; q < 10; q++)
        {
            var spectator = host.MatchSnapshot()!;
            Assert.Null(spectator.Private); Assert.Equal(2, spectator.Scores.Length);
            Assert.Null(spectator.Reveal);
            Assert.Equal(SubmissionError.UnknownPlayer, host.SubmitHostAnswer(0));
            Sync();
            Assert.All(clients, client => Assert.Equal(client.PlayerId, client.Match.Snapshot!.Private!.PlayerId));
            for (var i = 0; i < 2; i++)
            {
                var correct = Array.IndexOf(spectator.Question.Answers, "A");
                foreach (var p in host.Handle(i + 2, clients[i].Match.CreateAnswer(i == 0 ? correct : (correct + 1) % 4)!).Messages)
                    if (p.ConnectionId == i + 2) clients[i].Apply(p.Json);
            }
            Assert.True(host.PollMatch()); Assert.Null(host.MatchSnapshot()!.Private);
            Sync(); host.AdvanceMatch(); Sync(); host.AdvanceMatch(); Sync();
            if (host.MatchSnapshot()!.Phase == "RoundEnd") { host.AdvanceMatch(); Sync(); }
        }
        Assert.Equal("GameOver", host.MatchSnapshot()!.Phase); Assert.Null(host.MatchSnapshot()!.Private);
        Assert.Equal(2, host.MatchSnapshot()!.FinalStrategy!.Length);
    }
}

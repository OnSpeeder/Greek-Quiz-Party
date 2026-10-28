using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Questions;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class MatchFlowProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100); }
    [Theory]
    [InlineData(0)] [InlineData(120)]
    public void OwnedSeatVotesReplayAndNewMatchRemainAuthoritative(int seconds)
    {
        var clock = new Clock();
        var questions = Enumerable.Range(0, 8).Select(i => new QuestionDefinition("q" + i, "Synthetic " + i,
            ["yes", "no", "other", "last"], 0, "test", 1, "Facts", ["Fun fact"]));
        var host = new LobbyHost("Room", "", clock, questions.ToArray(), new MatchSettings(0, seconds, new StrategyRules()), hostPlays: false);
        var client = new LobbyClientState();
        void Deliver(IEnumerable<LobbyOutbound> packets) { foreach (var p in packets) client.Apply(p.Json); }
        Deliver(host.Handle(2, client.BeginHello("First", "Android")).Messages);
        Deliver(host.Handle(2, client.CreateAddLocal("Second", 1)!).Messages);
        void Start()
        {
            foreach (var slot in new[] { 0, 1 }) Deliver(host.Handle(2, client.CreateReady(true, slot)!).Messages);
            Assert.Equal(LobbyError.None, host.Start()); Deliver(host.Broadcast()); Assert.True(host.BeginMatch()); Deliver(host.BroadcastMatch());
        }
        Start();
        var oldQuestion = host.MatchSnapshot()!.Question.InstanceId;
        clock.Now += TimeSpan.FromSeconds(119);
        for (var slot = 0; slot < 2; slot++)
        {
            var own = client.MatchForSlot(slot);
            Deliver(host.Handle(2, own.CreateAnswer(Array.IndexOf(own.Snapshot!.Question.Answers, "yes"))!).Messages);
            Assert.Equal(slot + 1, host.MatchSnapshot()!.AnsweredPlayers!.Length);
            Assert.Null(client.Match.Snapshot!.Reveal);
        }
        Assert.True(host.PollMatch()); Deliver(host.BroadcastMatch());
        string Vote(int slot, bool end = false, string? phase = null, Guid? question = null) => LobbyProtocol.Encode("MatchVote", host.SessionId,
            new MatchVoteDto(question ?? oldQuestion, phase ?? host.MatchSnapshot()!.Phase, end, slot));
        var vote = Vote(0);
        Deliver(host.Handle(2, vote).Messages); var revision = host.MatchSnapshot()!.Revision;
        Deliver(host.Handle(2, vote).Messages); Assert.Equal(revision, host.MatchSnapshot()!.Revision);
        Deliver(host.Handle(2, Vote(7)).Messages); Assert.Equal("AnswerReveal", host.MatchSnapshot()!.Phase);
        Deliver(host.Handle(2, Vote(1)).Messages); Assert.Equal("Scoreboard", client.Match.Snapshot!.Phase);
        Deliver(host.Handle(2, Vote(0, phase: "AnswerReveal")).Messages); Assert.Empty(host.MatchSnapshot()!.ContinueVotes!);
        Deliver(host.Handle(2, Vote(0, true)).Messages); Assert.Equal("Scoreboard", host.MatchSnapshot()!.Phase);
        Deliver(host.Handle(2, Vote(1, true)).Messages); Assert.Equal("GameOver", client.Match.Snapshot!.Phase);
        var finalPacket = host.BroadcastMatch().First().Json;
        Assert.True(host.Replay()); Deliver(host.Broadcast());
        Assert.Null(client.Match.Snapshot); Assert.Null(host.MatchSnapshot());
        Assert.All(host.Snapshot().Players, p => Assert.False(p.Ready));
        Assert.Equal(LobbyClientUpdate.Ignored, client.Apply(finalPacket));
        Start();
        Assert.NotEqual(oldQuestion, client.Match.Snapshot!.Question.InstanceId);
        Deliver(host.Handle(2, Vote(0, phase: "Scoreboard", question: oldQuestion)).Messages);
        Assert.Equal("QuestionActive", host.MatchSnapshot()!.Phase); Assert.Empty(host.MatchSnapshot()!.ContinueVotes!);
    }
    [Fact]
    public void OlderVersionCannotJoinCurrentVersion()
    {
        var host = new LobbyHost("Room", "Host", new Clock());
        var request = new LobbyClientState().BeginHello("Old", "Android").Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", $"\"ProtocolVersion\":{LobbyProtocol.Version - 1}");
        var reply = host.Handle(2, request);
        Assert.True(reply.DisconnectSender); Assert.Contains("IncompatibleVersion", reply.Messages[0].Json);
    }

    [Fact]
    public void UnlimitedMatchOutlivesReceiptBudgetWithoutReapplyingRetiredIntents()
    {
        var clock = new Clock();
        var questions = Enumerable.Range(0, 720).Select(i => new QuestionDefinition("q" + i, "Synthetic " + i,
            ["yes", "no", "other", "last"], 0, "test", 1, "Facts")).ToArray();
        var host = new LobbyHost("Room", "", clock, questions, new(0, 0), hostPlays: false);
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginHello("First", "Android")).Messages[0].Json);
        host.Handle(2, LobbyProtocol.Encode("AddLocalPlayer", host.SessionId, new AddLocalPlayerDto("Second", 1)));
        foreach (var slot in new[] { 0, 1 }) host.Handle(2, LobbyProtocol.Encode("SetReady", host.SessionId, new ReadyRequestDto(true, slot)));
        host.Start(); Assert.True(host.BeginMatch());
        string? firstAnswer = null;
        void Send(string packet)
        {
            clock.Now += TimeSpan.FromSeconds(1);
            var reply = host.Handle(2, packet);
            Assert.False(reply.DisconnectSender); Assert.Contains("\"Accepted\":true", reply.Messages[0].Json);
        }
        for (var i = 0; i < 720; i++)
        {
            var question = host.MatchSnapshot()!.Question.InstanceId;
            for (var slot = 0; slot < 2; slot++)
            {
                var answer = LobbyProtocol.Encode("SubmitAnswer", host.SessionId, new AnswerRequestDto(question, slot, 1, slot));
                firstAnswer ??= answer; Send(answer);
            }
            Assert.True(host.PollMatch());
            foreach (var phase in new[] { "AnswerReveal", "Scoreboard" })
                foreach (var slot in new[] { 0, 1 }) Send(LobbyProtocol.Encode("MatchVote", host.SessionId, new MatchVoteDto(question, phase, false, slot)));
            if (i == 710)
            {
                clock.Now += TimeSpan.FromSeconds(1);
                var old = host.Handle(2, firstAnswer!);
                Assert.False(old.DisconnectSender); Assert.Contains("StaleQuestion", old.Messages[0].Json);
                Assert.Equal(0, host.MatchSnapshot()!.AcceptedAnswerCount);
            }
        }
        Assert.Equal("GameOver", host.MatchSnapshot()!.Phase); Assert.Equal(720, host.MatchSnapshot()!.QuestionNumber);
    }
}

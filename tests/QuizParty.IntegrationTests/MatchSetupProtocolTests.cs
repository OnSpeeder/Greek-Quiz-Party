using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class MatchSetupProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } }
    [Fact]
    public void HostFiltersCapacityBeforeStartAndClientAcceptsHardDifficultyHostScore()
    {
        var clock = new Clock();
        var questions = new[] {
            new QuestionDefinition("easy", "Easy", ["A", "B", "C", "D"], 0, "history", 1, "E"),
            new QuestionDefinition("hard", "Hard", ["A", "B", "C", "D"], 0, "science", 5, "E") };
        var host = new LobbyHost("Room", "Host", clock, questions, new(1));
        var client = new LobbyClientState();
        foreach (var p in host.Handle(2, client.BeginHello("Phone", "Android")).Messages.Where(p => p.ConnectionId == 2)) client.Apply(p.Json);
        Assert.False(host.Snapshot().Players.Single(p => p.IsHost).Ready);
        Assert.False(host.ConfigureMatch(new(1, difficulties: [5]), ["history"]));
        Assert.True(host.ConfigureMatch(new(1, difficulties: [5]), ["science"]));
        foreach (var p in host.Handle(2, client.CreateReady(true)!).Messages.Where(p => p.ConnectionId == 2)) client.Apply(p.Json);
        Assert.Equal(QuizParty.Core.Lobby.LobbyError.NotReady, host.Start());
        host.SetHostReady(true); host.Start();
        foreach (var p in host.Broadcast()) client.Apply(p.Json);
        Assert.True(host.BeginMatch());
        foreach (var p in host.BroadcastMatch()) Assert.Equal(LobbyClientUpdate.MatchSnapshot, client.Apply(p.Json));
        Assert.Equal(5, client.Match.Snapshot!.Question.Difficulty);
        Assert.Null(client.Match.Snapshot.Reveal);
        var correct = Array.IndexOf(host.MatchSnapshot()!.Question.Answers, "A");
        host.SubmitHostAnswer(correct);
        foreach (var p in host.Handle(2, client.Match.CreateAnswer(correct)!).Messages.Where(p => p.ConnectionId == 2)) client.Apply(p.Json);
        host.PollMatch();
        foreach (var p in host.BroadcastMatch()) Assert.Equal(LobbyClientUpdate.MatchSnapshot, client.Apply(p.Json));
        Assert.All(client.Match.Snapshot!.Scores, s => Assert.Equal(2000, s.Total));
    }
}

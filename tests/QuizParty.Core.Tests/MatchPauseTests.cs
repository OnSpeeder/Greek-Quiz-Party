using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class MatchPauseTests
{
    private static FullMatch Create(SessionFixture f, int seconds = 20) => new(f.Players, f.Clock,
        new SeededRandomSource(4), new[] { SessionFixture.Question }, new MatchSettings(1, seconds));

    [Fact]
    public void DisconnectFreezesHostClockAndReconnectCountsDownWithoutExtendingElapsedAnswerTime()
    {
        var f = new SessionFixture(); var match = Create(f); var q = match.Snapshot.Question!;
        f.Clock.Advance(TimeSpan.FromSeconds(5)); match.Disconnect(f.Players[2].Id);
        Assert.True(match.IsPaused); Assert.False(match.Poll());
        f.Clock.Advance(TimeSpan.FromHours(3));
        Assert.Equal(q.StartedAt + TimeSpan.FromSeconds(5), match.GameNow);
        Assert.Equal(SubmissionError.InvalidState, match.Submit(new(f.Players[0].Id, q.InstanceId, 0), f.Clock.Now));
        match.Reconnect(f.Players[2].Id); Assert.True(match.IsCountingDown);
        f.Clock.Advance(TimeSpan.FromSeconds(4)); Assert.False(match.Poll());
        f.Clock.Advance(TimeSpan.FromSeconds(1)); Assert.True(match.Poll()); Assert.False(match.IsPaused);
        Assert.Equal(q.StartedAt + TimeSpan.FromSeconds(5), match.GameNow);
        var correct = q.Answers.ToList().IndexOf("Αθήνα");
        foreach (var p in f.Players) Assert.Equal(SubmissionError.None, match.Submit(new(p.Id, q.InstanceId, correct), f.Clock.Now));
        Assert.True(match.Poll());
        Assert.Equal(875, match.Snapshot.Scores.Single(s => s.PlayerId == f.Players[0].Id).Total);
    }

    [Fact]
    public void ConnectedSeatsCanVoteToContinueAndMissingPlayerCanReturnMuchLater()
    {
        var f = new SessionFixture(); var match = Create(f, 0); var q = match.Snapshot.Question!;
        match.Disconnect(f.Players[2].Id); var pause = match.PauseId;
        Assert.Equal(GameError.InvalidTransition, match.ResumeVote(f.Players[0].Id, Guid.NewGuid()));
        Assert.Equal(GameError.None, match.ResumeVote(f.Players[0].Id, pause)); Assert.True(match.IsPaused);
        Assert.Equal(GameError.None, match.ResumeVote(f.Players[1].Id, pause)); Assert.False(match.IsPaused);
        foreach (var p in f.Players.Take(2)) Assert.Equal(SubmissionError.None, match.Submit(new(p.Id, q.InstanceId, 0), f.Clock.Now));
        Assert.True(match.Poll());
        f.Clock.Advance(TimeSpan.FromHours(12)); match.Reconnect(f.Players[2].Id);
        Assert.False(match.IsPaused); Assert.DoesNotContain(f.Players[2].Id, match.DisconnectedPlayers);
        Assert.True(match.Poll());
        var missing = match.Statistics.Single(s => s.PlayerId == f.Players[2].Id);
        Assert.Equal(1, missing.Wrong); Assert.Equal(0, missing.Unanswered);
    }

    [Fact]
    public void AnotherDisconnectCancelsCountdownAndInvalidatesOldVotes()
    {
        var f = new SessionFixture(); var match = Create(f);
        match.Disconnect(f.Players[2].Id); var old = match.PauseId;
        match.Reconnect(f.Players[2].Id); Assert.True(match.IsCountingDown);
        match.Disconnect(f.Players[1].Id); Assert.True(match.IsPaused); Assert.False(match.IsCountingDown);
        Assert.NotEqual(old, match.PauseId);
        Assert.Equal(GameError.InvalidTransition, match.ResumeVote(f.Players[0].Id, old));
        Assert.Equal(GameError.None, match.Resume()); Assert.False(match.IsPaused);
    }
}

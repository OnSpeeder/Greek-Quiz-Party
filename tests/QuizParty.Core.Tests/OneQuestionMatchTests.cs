using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class OneQuestionMatchTests
{
    [Fact]
    public void CompleteMatchLocksRevealsAndAwardsOnceThenHostAdvancesToFinal()
    {
        var fixture = new SessionFixture();
        var match = new OneQuestionMatch(fixture.Players, fixture.Clock, new SequenceRandom(3, 2, 1),
            SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration);
        Assert.Equal(GameError.InvalidTransition, match.Advance());
        foreach (var player in fixture.Players)
            Assert.Equal(SubmissionError.None, match.Submit(new(player.Id, SessionFixture.FirstInstance, 0), fixture.Clock.Now));
        Assert.Equal(GamePhase.QuestionLocked, match.Snapshot.Phase);
        Assert.Null(match.Snapshot.Reveal);
        Assert.True(match.Poll());
        Assert.Equal(GamePhase.AnswerReveal, match.Snapshot.Phase);
        Assert.All(match.Snapshot.Scores, score => Assert.Equal(1000, score.Total));
        var revision = match.Revision;
        Assert.False(match.Poll());
        Assert.Equal(revision, match.Revision);
        Assert.Equal(GameError.None, match.Advance());
        Assert.Equal(GamePhase.Scoreboard, match.Snapshot.Phase);
        Assert.Equal(GameError.None, match.Advance());
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase);
        Assert.Equal(GameError.InvalidTransition, match.Advance());
        Assert.False(match.Poll());
        Assert.All(match.Snapshot.Scores, score => Assert.Equal(1000, score.Total));
    }

    [Fact]
    public void DeadlineUsesHostClockAndUnansweredPlayersScoreZero()
    {
        var fixture = new SessionFixture();
        var match = new OneQuestionMatch(fixture.Players, fixture.Clock, new SequenceRandom(3, 2, 1),
            SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration);
        Assert.False(match.Poll());
        fixture.Clock.Advance(SessionFixture.Duration);
        Assert.False(match.Poll());
        Assert.Equal(SubmissionError.None, match.Submit(new(fixture.Players[0].Id, SessionFixture.FirstInstance, 0), fixture.Clock.Now));
        var revision = match.Revision;
        Assert.Equal(SubmissionError.AlreadyAnswered, match.Submit(new(fixture.Players[0].Id, SessionFixture.FirstInstance, 1), fixture.Clock.Now));
        Assert.Equal(revision, match.Revision);
        fixture.Clock.Advance(TimeSpan.FromTicks(1));
        Assert.Equal(SubmissionError.Late, match.Submit(new(fixture.Players[1].Id, SessionFixture.FirstInstance, 0), fixture.Clock.Now));
        Assert.True(match.Poll());
        Assert.Equal(GamePhase.QuestionLocked, match.Snapshot.Phase);
        Assert.True(match.Poll());
        Assert.Equal(500, match.Snapshot.Scores[0].Total);
        Assert.All(match.Snapshot.Scores.Skip(1), score => Assert.Equal(0, score.Total));
    }
}

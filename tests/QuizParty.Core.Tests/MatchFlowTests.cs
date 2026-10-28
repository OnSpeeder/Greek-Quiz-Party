using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class MatchFlowTests
{
    private static FullMatch Match(SessionFixture f, int count = 0, int seconds = 0, int deck = 4, bool speedScoring = true) =>
        new(f.Players, f.Clock, new SeededRandomSource(5), Enumerable.Range(0, deck).Select(i =>
            new QuestionDefinition("q" + i, "Question " + i, ["yes", "no", "other", "last"], 0, "test", 1, "Facts")), new(count, seconds, speedScoring: speedScoring));
    private static void Reveal(SessionFixture f, FullMatch match)
    {
        var question = match.Snapshot.Question!;
        foreach (var player in f.Players)
            Assert.Equal(SubmissionError.None, match.Submit(new(player.Id, question.InstanceId,
                question.Answers.ToList().IndexOf("yes")), f.Clock.Now));
        Assert.True(match.Poll());
    }
    [Fact]
    public void UntimedWaitsBeyondTwoMinutesAndCorrectAnswersReceiveOnlyBasePoints()
    {
        var f = new SessionFixture(); var match = Match(f);
        f.Clock.Advance(TimeSpan.FromHours(3)); Assert.False(match.Poll());
        Reveal(f, match);
        Assert.All(match.Snapshot.Reveal!.Players, p => Assert.Equal(500, p.Points));
        Assert.Equal(TimeSpan.MaxValue, match.Snapshot.Question!.Deadline);
    }
    [Theory]
    [InlineData(0, true, 550)]
    [InlineData(15, true, 525)]
    [InlineData(30, true, 500)]
    [InlineData(0, false, 500)]
    public void UntimedSpeedSettingUsesHostElapsedTime(int seconds, bool enabled, int points)
    {
        var f = new SessionFixture(); var match = Match(f, speedScoring: enabled);
        f.Clock.Advance(TimeSpan.FromSeconds(seconds)); Reveal(f, match);
        Assert.All(match.Snapshot.Reveal!.Players, p => Assert.Equal(points, p.Points));
    }
    [Theory]
    [InlineData(true, 875)]
    [InlineData(false, 500)]
    public void TimedSpeedSettingControlsTheExistingBonus(bool enabled, int points)
    {
        var f = new SessionFixture(); var match = Match(f, seconds: 20, speedScoring: enabled);
        f.Clock.Advance(TimeSpan.FromSeconds(5)); Reveal(f, match);
        Assert.All(match.Snapshot.Reveal!.Players, p => Assert.Equal(points, p.Points));
    }
    [Fact]
    public void UntimedSpeedBonusExcludesTimePausedForDisconnect()
    {
        var f = new SessionFixture(); var match = Match(f);
        f.Clock.Advance(TimeSpan.FromSeconds(5));
        match.Disconnect(f.Players[2].Id);
        f.Clock.Advance(TimeSpan.FromMinutes(10));
        Assert.Equal(GameError.None, match.Resume());
        var question = match.Snapshot.Question!;
        foreach (var player in f.Players.Take(2))
            Assert.Equal(SubmissionError.None, match.Submit(new(player.Id, question.InstanceId,
                question.Answers.ToList().IndexOf("yes")), f.Clock.Now));
        Assert.True(match.Poll()); Assert.True(match.Poll());
        Assert.All(match.Snapshot.Reveal!.Players.Where(p => p.AnswerIndex is not null), p => Assert.Equal(542, p.Points));
    }
    [Fact]
    public void ContinueRequiresEveryConnectedSeatAndDuplicateOrStaleVotesCannotAdvanceAgain()
    {
        var f = new SessionFixture(); var match = Match(f); Reveal(f, match);
        var id = match.Snapshot.Question!.InstanceId;
        var first = f.Players[0].Id;
        Assert.Equal(GameError.None, match.Vote(first, id, GamePhase.AnswerReveal, false));
        var revision = match.Revision;
        Assert.Equal(GameError.None, match.Vote(first, id, GamePhase.AnswerReveal, false)); Assert.Equal(revision, match.Revision);
        match.Vote(f.Players[1].Id, id, GamePhase.AnswerReveal, false);
        Assert.Equal(GamePhase.AnswerReveal, match.Snapshot.Phase);
        match.Vote(f.Players[2].Id, id, GamePhase.AnswerReveal, false);
        Assert.Equal(GamePhase.Scoreboard, match.Snapshot.Phase); Assert.Empty(match.ContinueVotes);
        Assert.Equal(GameError.InvalidTransition, match.Vote(first, id, GamePhase.AnswerReveal, false));
        match.Advance(); Assert.Equal(2, match.QuestionNumber);
        Assert.Equal(GameError.InvalidTransition, match.Vote(first, id, GamePhase.Scoreboard, true));
    }
    [Fact]
    public void UnanimousEndIsSeparateFromContinueAndAppliesFinalResults()
    {
        var f = new SessionFixture(); var match = Match(f); Reveal(f, match); match.Advance();
        var id = match.Snapshot.Question!.InstanceId;
        match.Vote(f.Players[0].Id, id, GamePhase.Scoreboard, true);
        match.Vote(f.Players[1].Id, id, GamePhase.Scoreboard, false);
        Assert.Equal(GamePhase.Scoreboard, match.Snapshot.Phase);
        match.Vote(f.Players[1].Id, id, GamePhase.Scoreboard, true);
        match.Vote(f.Players[2].Id, id, GamePhase.Scoreboard, true);
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase); Assert.Equal(3, match.Winners.Count);
        Assert.Equal(GameError.InvalidTransition, match.EndUnlimited());
    }
    [Fact]
    public void DisconnectPausesUntilResumedAndThenRemovesUntimedBlocker()
    {
        var f = new SessionFixture(); var match = Match(f);
        var q = match.Snapshot.Question!;
        foreach (var p in f.Players.Take(2)) match.Submit(new(p.Id, q.InstanceId, 0), f.Clock.Now);
        match.Disconnect(f.Players[2].Id);
        Assert.True(match.IsPaused); Assert.False(match.Poll());
        Assert.Equal(GameError.None, match.Resume());
        Assert.True(match.Poll()); Assert.True(match.Poll());
        match.Vote(f.Players[0].Id, q.InstanceId, GamePhase.AnswerReveal, false);
        match.Disconnect(f.Players[1].Id);
        Assert.True(match.IsPaused); Assert.Equal(GamePhase.AnswerReveal, match.Snapshot.Phase);
        match.Resume();
        Assert.Equal(GamePhase.Scoreboard, match.Snapshot.Phase);
    }
    [Fact]
    public void UnlimitedExhaustionEndsWithoutRepeatsAndHostMayOverrideVotes()
    {
        var f = new SessionFixture(); var match = Match(f, deck: 2); var ids = new HashSet<QuestionInstanceId>();
        for (var i = 0; i < 2; i++)
        { Assert.True(ids.Add(match.Snapshot.Question!.InstanceId)); Reveal(f, match); match.Advance(); match.Advance(); }
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase); Assert.True(match.ContentExhausted);
        var finite = Match(f, 1); Reveal(f, finite); finite.Advance();
        Assert.Equal(GameError.InvalidTransition, finite.EndUnlimited());
    }
    [Fact]
    public void TwoMinuteDeadlineAcceptsExactBoundaryAndRejectsLaterReceipts()
    {
        var f = new SessionFixture(); var match = Match(f, 1, 120);
        var q = match.Snapshot.Question!; f.Clock.Now = q.Deadline;
        Assert.Equal(SubmissionError.None, match.Submit(new(f.Players[0].Id, q.InstanceId, 0), f.Clock.Now));
        f.Clock.Advance(TimeSpan.FromTicks(1));
        Assert.NotEqual(SubmissionError.None, match.Submit(new(f.Players[1].Id, q.InstanceId, 0), f.Clock.Now));
    }
}

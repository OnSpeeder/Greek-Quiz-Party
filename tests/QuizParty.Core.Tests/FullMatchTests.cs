using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class FullMatchTests
{
    private static QuestionDefinition[] Questions(int count) => Enumerable.Range(0, count).Select(i =>
        new QuestionDefinition($"q{i:D3}", $"Test {i}", ["yes", "no", "other", "last"], 0, $"cat{i % 3}", i % 5 + 1, "Test only")).ToArray();
    private static int Correct(FullMatch match) => match.Snapshot.Question!.Answers.ToList().IndexOf("yes");
    private static void Reveal(FullMatch match)
    {
        Assert.True(match.Poll());
        Assert.Equal(GamePhase.AnswerReveal, match.Snapshot.Phase);
        Assert.False(match.Poll());
    }

    [Theory]
    [InlineData(10)] [InlineData(20)] [InlineData(30)]
    public void CompleteFourRoundsWithoutRepeatsAndKeepAccurateCumulativeStatistics(int count)
    {
        var fixture = new SessionFixture();
        var match = new FullMatch(fixture.Players, fixture.Clock, new SeededRandomSource(42), Questions(count), new(count));
        var instances = new HashSet<QuestionInstanceId>();
        var texts = new HashSet<string>();
        var rounds = new HashSet<int>();
        for (var q = 1; q <= count; q++)
        {
            Assert.Equal(q, match.QuestionNumber);
            Assert.True(instances.Add(match.Snapshot.Question!.InstanceId));
            Assert.True(texts.Add(match.Snapshot.Question.Text));
            rounds.Add(match.RoundNumber);
            fixture.Clock.Advance(TimeSpan.FromSeconds(2));
            var correct = Correct(match);
            Assert.Equal(SubmissionError.None, match.Submit(new(fixture.Players[0].Id, match.Snapshot.Question.InstanceId, correct), fixture.Clock.Now));
            Assert.Equal(SubmissionError.AlreadyAnswered, match.Submit(new(fixture.Players[0].Id, match.Snapshot.Question.InstanceId, correct), fixture.Clock.Now));
            Assert.Equal(SubmissionError.None, match.Submit(new(fixture.Players[1].Id, match.Snapshot.Question.InstanceId, (correct + 1) % 4), fixture.Clock.Now));
            fixture.Clock.Advance(TimeSpan.FromSeconds(19));
            Assert.True(match.Poll()); // Unanswered third player times out under host clock.
            Reveal(match);
            Assert.Equal(q * 950, match.Snapshot.Scores[0].Total);
            Assert.Equal(GameError.None, match.Advance());
            Assert.Equal(GameError.None, match.Advance());
            if (match.Snapshot.Phase == GamePhase.RoundEnd) Assert.Equal(GameError.None, match.Advance());
        }
        Assert.Equal(4, rounds.Count);
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase);
        Assert.Equal(fixture.Players[0].Id, Assert.Single(match.Winners));
        var winner = match.Statistics.Single(s => s.PlayerId == fixture.Players[0].Id);
        Assert.Equal(count, winner.Correct); Assert.Equal(count, winner.BestStreak);
        Assert.Equal(100, winner.Accuracy); Assert.Equal(2, winner.AverageResponseSeconds);
        Assert.Equal(count, match.Statistics.Single(s => s.PlayerId == fixture.Players[1].Id).Wrong);
        Assert.Equal(count, match.Statistics.Single(s => s.PlayerId == fixture.Players[2].Id).Unanswered);
        Assert.Equal(GameError.InvalidTransition, match.Advance());
    }

    [Fact]
    public void SuddenDeathNarrowsExactTiesUsesHostTimeAndExcludesOtherPlayers()
    {
        var f = new SessionFixture();
        var match = new FullMatch(f.Players, f.Clock, new SeededRandomSource(8), Questions(4), new(1));
        // First two tie for first, third is wrong.
        for (var i = 0; i < 3; i++) Assert.Equal(SubmissionError.None,
            match.Submit(new(f.Players[i].Id, match.Snapshot.Question!.InstanceId, i == 2 ? (Correct(match) + 1) % 4 : Correct(match)), f.Clock.Now));
        Reveal(match); match.Advance(); match.Advance();
        Assert.Equal(GamePhase.RoundEnd, match.Snapshot.Phase);
        Assert.True(match.IsTieBreaker); Assert.Equal(2, match.Eligible.Count);
        match.Advance();
        var id = match.Snapshot.Question!.InstanceId;
        Assert.Equal(SubmissionError.UnknownPlayer, match.Submit(new(f.Players[2].Id, id, Correct(match)), f.Clock.Now));
        foreach (var p in f.Players.Take(2)) Assert.Equal(SubmissionError.None, match.Submit(new(p.Id, id, Correct(match)), f.Clock.Now));
        Reveal(match); match.Advance(); match.Advance(); match.Advance(); // Exact receipt tie requires another unique question.
        Assert.Equal(3, match.QuestionNumber);
        id = match.Snapshot.Question!.InstanceId;
        f.Clock.Advance(TimeSpan.FromSeconds(1));
        Assert.Equal(SubmissionError.None, match.Submit(new(f.Players[1].Id, id, Correct(match)), f.Clock.Now));
        f.Clock.Advance(TimeSpan.FromTicks(1));
        Assert.Equal(SubmissionError.None, match.Submit(new(f.Players[0].Id, id, Correct(match)), f.Clock.Now));
        Reveal(match); match.Advance(); match.Advance();
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase);
        Assert.Equal(f.Players[1].Id, Assert.Single(match.Winners));
        Assert.Equal(1000, match.Snapshot.Scores[0].Total); Assert.Equal(1000, match.Snapshot.Scores[1].Total);
        Assert.Equal(1, match.Statistics.Single(s => s.PlayerId == f.Players[2].Id).Wrong);
    }

    [Fact]
    public void AllWrongTieContinuesUntilFiniteDeckExhaustionThenReportsSharedFirst()
    {
        var f = new SessionFixture();
        var match = new FullMatch(f.Players, f.Clock, new SeededRandomSource(8), Questions(2), new(1));
        for (var i = 0; i < 2; i++)
        {
            foreach (var p in f.Players) match.Submit(new(p.Id, match.Snapshot.Question!.InstanceId, (Correct(match) + 1) % 4), f.Clock.Now);
            Reveal(match); match.Advance(); match.Advance();
            if (match.Snapshot.Phase == GamePhase.RoundEnd) match.Advance();
        }
        Assert.Equal(GamePhase.GameOver, match.Snapshot.Phase);
        Assert.True(match.ContentExhausted); Assert.Equal(3, match.Winners.Count);
    }

    [Fact]
    public void SelectionIsSeededOrderIndependentMixedFilteredAndFinite()
    {
        var source = Questions(45);
        var a = new QuestionDeck(source, new SeededRandomSource(123), ["cat1"]);
        var b = new QuestionDeck(source.Reverse(), new SeededRandomSource(123), ["cat1"]);
        var ids = new HashSet<string>(); var levels = new HashSet<int>();
        for (var i = 0; i < 15; i++)
        {
            var question = a.Draw()!;
            Assert.Equal(question.Id, b.Draw()!.Id); Assert.Equal("cat1", question.CategoryId);
            Assert.True(ids.Add(question.Id)); if (i < 5) levels.Add(question.Difficulty);
        }
        Assert.Equal(5, levels.Count); Assert.Null(a.Draw()); Assert.Equal(0, a.Remaining);
        Assert.Throws<ArgumentException>(() => new QuestionDeck([source[0], source[0]], new SeededRandomSource(1)));
        Assert.Throws<ArgumentException>(() => new FullMatch(new SessionFixture().Players, new FakeClock(),
            new SeededRandomSource(1), source, new(20), ["cat1"]));
    }

    [Fact]
    public void EachQuestionHasNewDeadlineAndOldIntentsCannotConsumeNewSlot()
    {
        var f = new SessionFixture();
        var match = new FullMatch(f.Players, f.Clock, new SeededRandomSource(3), Questions(10), new(10, 10));
        var old = match.Snapshot.Question!;
        f.Clock.Advance(TimeSpan.FromSeconds(10));
        Assert.Equal(SubmissionError.None, match.Submit(new(f.Players[0].Id, old.InstanceId, Correct(match)), f.Clock.Now));
        Assert.False(match.Poll());
        f.Clock.Advance(TimeSpan.FromTicks(1)); Assert.True(match.Poll()); Reveal(match);
        match.Advance(); match.Advance();
        Assert.Equal(GamePhase.QuestionActive, match.Snapshot.Phase);
        Assert.Equal(f.Clock.Now, match.Snapshot.Question!.StartedAt);
        Assert.Equal(SubmissionError.StaleQuestion, match.Submit(new(f.Players[0].Id, old.InstanceId, 0), f.Clock.Now));
        Assert.Equal(0, match.Snapshot.AcceptedAnswerCount);
        Assert.Equal(SubmissionError.InvalidReceiveTime, match.Submit(new(f.Players[0].Id, match.Snapshot.Question.InstanceId, 0), f.Clock.Now + TimeSpan.FromTicks(1)));
    }

    [Fact]
    public void InjectedClockSeedAndInstanceIdsReplayEntireMatchDeterministically()
    {
        var first = new SessionFixture(); var second = new SessionFixture();
        FullMatch Create(SessionFixture f)
        {
            var counter = 0;
            return new(f.Players, f.Clock, new SeededRandomSource(123), Questions(10), new(10),
                nextInstance: () => new(new Guid(++counter, 0, 0, new byte[8])));
        }
        var a = Create(first); var b = Create(second);
        while (a.Snapshot.Phase != GamePhase.GameOver)
        {
            Assert.Equal(System.Text.Json.JsonSerializer.Serialize(a.Snapshot), System.Text.Json.JsonSerializer.Serialize(b.Snapshot));
            if (a.Snapshot.Phase == GamePhase.QuestionActive)
            {
                first.Clock.Advance(TimeSpan.FromSeconds(1)); second.Clock.Advance(TimeSpan.FromSeconds(1));
                for (var i = 0; i < 3; i++)
                {
                    a.Submit(new(first.Players[i].Id, a.Snapshot.Question!.InstanceId, i == 0 ? Correct(a) : (Correct(a) + 1) % 4), first.Clock.Now);
                    b.Submit(new(second.Players[i].Id, b.Snapshot.Question!.InstanceId, i == 0 ? Correct(b) : (Correct(b) + 1) % 4), second.Clock.Now);
                }
            }
            else if (a.Snapshot.Phase == GamePhase.QuestionLocked) { a.Poll(); b.Poll(); }
            else { a.Advance(); b.Advance(); }
        }
        Assert.Equal(a.Revision, b.Revision); Assert.Equal(a.Winners, b.Winners); Assert.Equal(a.Statistics, b.Statistics);
    }

    [Fact]
    public void WrongAndUnansweredResetStreakAndOnlyAcceptedResponsesEnterAverage()
    {
        var f = new SessionFixture();
        var match = new FullMatch(f.Players, f.Clock, new SeededRandomSource(1), Questions(10), new(10));
        bool?[] pattern = [true, true, false, true, null, true, true, true, false, true];
        foreach (var answer in pattern)
        {
            f.Clock.Advance(TimeSpan.FromSeconds(2));
            var id = match.Snapshot.Question!.InstanceId;
            match.Submit(new(f.Players[0].Id, id, Correct(match)), f.Clock.Now);
            match.Submit(new(f.Players[2].Id, id, (Correct(match) + 1) % 4), f.Clock.Now);
            if (answer is not null) match.Submit(new(f.Players[1].Id, id, answer.Value ? Correct(match) : (Correct(match) + 1) % 4), f.Clock.Now);
            else { f.Clock.Advance(TimeSpan.FromSeconds(19)); Assert.True(match.Poll()); }
            Reveal(match); match.Advance(); match.Advance();
            if (match.Snapshot.Phase == GamePhase.RoundEnd) match.Advance();
        }
        var stats = match.Statistics.Single(s => s.PlayerId == f.Players[1].Id);
        Assert.Equal(7, stats.Correct); Assert.Equal(2, stats.Wrong); Assert.Equal(1, stats.Unanswered);
        Assert.Equal(3, stats.BestStreak); Assert.Equal(70, stats.Accuracy);
        Assert.Equal(9, stats.Responses); Assert.Equal(2, stats.AverageResponseSeconds);
    }

    [Theory]
    [InlineData(0,20)] [InlineData(15,20)] [InlineData(20,4)] [InlineData(20,61)]
    public void InvalidSettingsAreRejected(int questions, int seconds) => Assert.Throws<ArgumentOutOfRangeException>(() => new MatchSettings(questions, seconds));
}

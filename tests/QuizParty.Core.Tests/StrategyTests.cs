using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class StrategyTests
{
    private sealed class FixedRandom(int value) : IRandomSource { public int Next(int upper) => Math.Min(value, upper - 1); }
    private sealed class Fixture
    {
        public SessionFixture Base { get; } = new();
        public FullMatch Match { get; }
        public Fixture(int card = 0, bool steal = false, bool missions = false, int seconds = 20)
        {
            var next = 100;
            Match = new(Base.Players, Base.Clock, new FixedRandom(card), Questions(35), new(30, seconds,
                new(Missions: missions, AllowSteal: steal)), nextCard: () => new Guid(++next, 0, 0, new byte[8]));
        }
        public StrategyPrivate Private(int player = 0) => Match.Private(Base.Players[player].Id)!;
        public int Correct => Match.Snapshot.Question!.Answers.ToList().IndexOf("yes");
        public CardError Play(int player, Guid card, PlayerId? target = null, string? category = null, TimeSpan? received = null) =>
            Match.Activate(new(Base.Players[player].Id, Match.Snapshot.Question!.InstanceId, card, target, category), received ?? Base.Clock.Now);
        public void Answer(bool firstCorrect = true, ConfidenceLevel confidence = ConfidenceLevel.Safe, bool othersCorrect = true)
        {
            var id = Match.Snapshot.Question!.InstanceId;
            for (var i = 0; i < 3; i++) Assert.Equal(SubmissionError.None, Match.Submit(new(Base.Players[i].Id, id,
                (i == 0 ? firstCorrect : othersCorrect) ? Correct : (Correct + 1) % 4, i == 0 ? confidence : ConfidenceLevel.Safe), Base.Clock.Now));
            Assert.True(Match.Poll()); Assert.Equal(GamePhase.AnswerReveal, Match.Snapshot.Phase);
        }
        public void Next()
        {
            Assert.Equal(GameError.None, Match.Advance()); Assert.Equal(GameError.None, Match.Advance());
            if (Match.Snapshot.Phase == GamePhase.RoundEnd) Assert.Equal(GameError.None, Match.Advance());
        }
        public void EarnCard() { for (var i = 0; i < 4; i++) { Answer(); Next(); } Assert.NotEmpty(Private().Hand); }
    }
    private static QuestionDefinition[] Questions(int count) => Enumerable.Range(0, count).Select(i => new QuestionDefinition(
        $"q{i:D3}", $"Test {i}", ["yes", "no", "other", "last"], 0, i % 2 == 0 ? "history" : "science", 5, "Test only")).ToArray();

    [Fact]
    public void ConfidencePenaltiesFloorTotalsAndLockOnFirstAcceptedSubmission()
    {
        var f = new Fixture();
        f.Answer(false, ConfidenceLevel.AllIn); Assert.Equal(0, f.Match.Snapshot.Scores[0].Total); f.Next();
        f.Answer(true, ConfidenceLevel.Confident); Assert.Equal(4000, f.Match.Snapshot.Scores[0].Total); f.Next();
        f.Answer(false, ConfidenceLevel.AllIn);
        Assert.Equal(-500, f.Match.Snapshot.Reveal!.Players[0].Points); Assert.Equal(3500, f.Match.Snapshot.Scores[0].Total); f.Next();
        var id = f.Match.Snapshot.Question!.InstanceId;
        Assert.Equal(SubmissionError.None, f.Match.Submit(new(f.Base.Players[0].Id, id, f.Correct, ConfidenceLevel.AllIn), f.Base.Clock.Now));
        Assert.Equal(SubmissionError.AlreadyAnswered, f.Match.Submit(new(f.Base.Players[0].Id, id, f.Correct, ConfidenceLevel.Safe), f.Base.Clock.Now));
        Assert.Equal(SubmissionError.InvalidConfidence, f.Match.Submit(new(f.Base.Players[1].Id, id, f.Correct, (ConfidenceLevel)4), f.Base.Clock.Now));
    }

    [Fact]
    public void StreakBonusesMeterThresholdHandLimitAndStackingCapAreHostCalculated()
    {
        var f = new Fixture();
        for (var i = 1; i <= 7; i++)
        {
            f.Answer();
            Assert.Equal(i >= 5 ? 2300 : i >= 3 ? 2200 : 2000, f.Match.Snapshot.Reveal!.Players[0].Points);
            Assert.InRange(f.Private().Meter, 0, 99); Assert.InRange(f.Private().Hand.Count, 0, 2);
            f.Next();
        }
        Assert.Equal(2, f.Private().Hand.Count);
        var card = f.Private().Hand.First(c => c.Kind == CardKind.DoublePoints);
        Assert.Equal(CardError.None, f.Play(0, card.Id));
        f.Answer(confidence: ConfidenceLevel.AllIn);
        Assert.Equal(12000, f.Match.Snapshot.Reveal!.Players[0].Points); // x3*x2*1.15 capped at6.
        Assert.False(f.Match.Poll());
        f.Next(); f.Answer(false); Assert.Equal(0, f.Private().Streak);
    }

    [Theory]
    [InlineData(0, CardKind.DoublePoints)] [InlineData(1, CardKind.FiftyFifty)]
    [InlineData(2, CardKind.ExtraTime)] [InlineData(3, CardKind.CategorySwap)]
    public void CardsAreOwnedConsumedOnlyAfterAcceptanceAndStaleOrDuplicateIntentsCannotReuse(int index, CardKind expected)
    {
        var f = new Fixture(index); f.EarnCard(); var card = f.Private().Hand[0];
        Assert.Equal(expected, card.Kind);
        Assert.Equal(CardError.UnknownCard, f.Play(1, card.Id));
        Assert.Equal(CardError.StaleQuestion, f.Match.Activate(new(f.Base.Players[0].Id, new(Guid.NewGuid()), card.Id), f.Base.Clock.Now));
        if (expected == CardKind.CategorySwap)
        {
            Assert.Equal(CardError.InvalidWindow, f.Play(0, card.Id)); f.Answer(); f.Match.Advance();
            var category = f.Private().SwapCategories.First();
            Assert.Equal(CardError.None, f.Play(0, card.Id, category: category));
        }
        else Assert.Equal(CardError.None, f.Play(0, card.Id));
        Assert.Equal(CardError.UnknownCard, f.Play(0, card.Id));
    }

    [Fact]
    public void FiftyFiftyIsPrivateHidesOnlyWrongAnswersAndCannotBeUsedAfterAnswer()
    {
        var f = new Fixture(1); f.EarnCard(); var card = f.Private().Hand[0];
        Assert.Equal(CardError.None, f.Play(0, card.Id));
        Assert.Equal(2, f.Private().HiddenAnswers.Count); Assert.DoesNotContain(f.Correct, f.Private().HiddenAnswers);
        Assert.Empty(f.Private(1).HiddenAnswers);
        Assert.Equal(SubmissionError.InvalidAnswerIndex, f.Match.Submit(new(f.Base.Players[0].Id, f.Match.Snapshot.Question!.InstanceId, f.Private().HiddenAnswers[0]), f.Base.Clock.Now));
        f.Answer(); f.Next(); Assert.Empty(f.Private().HiddenAnswers);
        var next = f.Private().Hand[0];
        Assert.Equal(SubmissionError.None, f.Match.Submit(new(f.Base.Players[0].Id, f.Match.Snapshot.Question!.InstanceId, f.Correct), f.Base.Clock.Now));
        Assert.Equal(CardError.AlreadyAnswered, f.Play(0, next.Id));
    }

    [Fact]
    public void ExtraTimeUsesPersonalHostDeadlineWithoutInflatingTimeBonusAndCutoffIsValidated()
    {
        var f = new Fixture(2); f.EarnCard(); var card = f.Private().Hand[0]; var original = f.Match.Snapshot.Question!;
        f.Base.Clock.Advance(TimeSpan.FromSeconds(17));
        Assert.Equal(CardError.None, f.Play(0, card.Id));
        Assert.Equal(original.Deadline + TimeSpan.FromSeconds(5), f.Private().Deadline);
        Assert.Equal(original.Deadline, f.Private(1).Deadline);
        f.Base.Clock.Advance(TimeSpan.FromSeconds(3)); Assert.False(f.Match.Poll());
        f.Base.Clock.Advance(TimeSpan.FromTicks(1)); Assert.False(f.Match.Poll());
        Assert.Equal(SubmissionError.Late, f.Match.Submit(new(f.Base.Players[1].Id, original.InstanceId, f.Correct), f.Base.Clock.Now));
        Assert.Equal(SubmissionError.None, f.Match.Submit(new(f.Base.Players[0].Id, original.InstanceId, f.Correct), f.Base.Clock.Now));
        // An already-answered extended player must not keep expired unanswered seats open.
        Assert.True(f.Match.Poll()); Assert.True(f.Match.Poll());
        Assert.Equal(1150, f.Match.Snapshot.Reveal!.Players[0].Points); // base500 * difficulty2 * streak1.15, no time bonus.
        f.Next(); card = f.Private().Hand[0]; f.Base.Clock.Advance(TimeSpan.FromSeconds(17) + TimeSpan.FromTicks(1));
        Assert.Equal(CardError.Late, f.Play(0, card.Id)); Assert.Contains(card, f.Private().Hand);
    }

    [Fact]
    public void CategorySwapChangesUpcomingCategoryWithoutRepeatsOrConsumptionOnInvalidRequest()
    {
        var f = new Fixture(3); f.EarnCard(); f.Answer(); f.Match.Advance();
        var card = f.Private().Hand[0];
        Assert.Equal(CardError.InvalidCategory, f.Play(0, card.Id, category: "not-enabled"));
        Assert.Contains(card, f.Private().Hand);
        var category = f.Private().SwapCategories.First();
        Assert.Equal(CardError.None, f.Play(0, card.Id, category: category));
        Assert.Empty(f.Private().SwapCategories);
        var previous = f.Match.Snapshot.Question!.Text;
        f.Match.Advance(); if (f.Match.Snapshot.Phase == GamePhase.RoundEnd) f.Match.Advance();
        Assert.Equal(category, f.Match.Snapshot.Question!.CategoryId); Assert.NotEqual(previous, f.Match.Snapshot.Question.Text);
    }

    [Fact]
    public void ShieldBlocksOneStealAndGlobalTargetLimitPreventsRepeatedVictim()
    {
        // Different injected RNG streams permit deterministic hand awards of each approved type.
        var random = new SwitchRandom(); var clock = new FakeClock(); var players = new SessionFixture().Players;
        var match = new FullMatch(players, clock, random, Questions(35), new(30, strategy: new(Missions: false, AllowSteal: true)));
        void Complete()
        {
            var correct = match.Snapshot.Question!.Answers.ToList().IndexOf("yes");
            foreach (var p in players) match.Submit(new(p.Id, match.Snapshot.Question.InstanceId, correct), clock.Now);
            match.Poll(); match.Advance(); match.Advance(); if (match.Snapshot.Phase == GamePhase.RoundEnd) match.Advance();
        }
        random.Value = 4; for (var i = 0; i < 3; i++) Complete();
        var shield = match.Private(players[0].Id)!.Hand.First(c => c.Kind == CardKind.Shield);
        Assert.Equal(CardError.None, match.Activate(new(players[0].Id, match.Snapshot.Question!.InstanceId, shield.Id), clock.Now));
        random.Value = 5; for (var i = 0; i < 3; i++) Complete();
        var steal = match.Private(players[0].Id)!.Hand.First(c => c.Kind == CardKind.Steal);
        var otherSteal = match.Private(players[1].Id)!.Hand.First(c => c.Kind == CardKind.Steal);
        var correctIndex = match.Snapshot.Question!.Answers.ToList().IndexOf("yes");
        foreach (var p in players) match.Submit(new(p.Id, match.Snapshot.Question.InstanceId, correctIndex), clock.Now);
        match.Poll(); match.Advance(); var total = match.Snapshot.Scores[0].Total;
        Assert.Equal(CardError.InvalidTarget, match.Activate(new(players[1].Id, match.Snapshot.Question.InstanceId, otherSteal.Id, players[1].Id), clock.Now));
        Assert.Equal(CardError.None, match.Activate(new(players[1].Id, match.Snapshot.Question.InstanceId, otherSteal.Id, players[0].Id), clock.Now));
        Assert.Equal(total, match.Snapshot.Scores[0].Total); Assert.False(match.Private(players[0].Id)!.Shield);
        Assert.Equal(CardError.InvalidTarget, match.Activate(new(players[0].Id, match.Snapshot.Question.InstanceId, steal.Id, players[0].Id), clock.Now));
        Assert.Equal(CardError.AlreadyTargeted, match.Activate(new(players[2].Id, match.Snapshot.Question.InstanceId,
            match.Private(players[2].Id)!.Hand.First(c => c.Kind == CardKind.Steal).Id, players[0].Id), clock.Now));
        Assert.Equal(CardError.None, match.Activate(new(players[0].Id, match.Snapshot.Question.InstanceId, steal.Id, players[2].Id), clock.Now));
        Assert.Equal(total + 100, match.Snapshot.Scores[0].Total);
    }
    private sealed class SwitchRandom : IRandomSource { public int Value; public int Next(int upper) => Math.Min(Value, upper - 1); }

    [Theory]
    [InlineData(0, MissionKind.Historian)] [InlineData(1, MissionKind.HotStreak)]
    [InlineData(2, MissionKind.Gambler)] [InlineData(3, MissionKind.Speedster)] [InlineData(4, MissionKind.Generalist)]
    public void EveryApprovedMissionProgressesOnlyOnItsOwnConditionAndCompletesOnce(int index, MissionKind kind)
    {
        var ids = new SessionFixture().Players.Select(p => p.Id).ToArray();
        var categories = new[] { "history", "history", "history", "science", "arts", "sports", "geography" };
        var questions = categories.Select((category, i) => new QuestionDefinition($"m{i}", "Test", ["a", "b", "c", "d"], 0, category, 1, "Test")).ToArray();
        var state = new StrategySession(ids, new FixedRandom(index), questions, new(Cards: false));
        Assert.Equal(kind, state.Private(ids[0], TimeSpan.Zero, []).Mission!.Kind);
        for (var i = 0; i < categories.Length; i++)
        {
            state.RecordResults(categories[i], 1, [new(ids[0], 0, true, 1000, TimeSpan.FromSeconds(1), ConfidenceLevel.AllIn),
                new(ids[1], 0, true, 1000, TimeSpan.FromSeconds(2)), new(ids[2], 1, false, 0, TimeSpan.FromSeconds(3))]);
        }
        Assert.True(state.Private(ids[0], TimeSpan.Zero, []).Mission!.Complete);
        Assert.False(state.Private(ids[2], TimeSpan.Zero, []).Mission!.Complete);
        if (kind is MissionKind.Speedster or MissionKind.Gambler) Assert.False(state.Private(ids[1], TimeSpan.Zero, []).Mission!.Complete);
        Assert.Equal(500, state.ApplyBonuses()[ids[0]]); Assert.Empty(state.ApplyBonuses());
    }

    [Fact]
    public void CategoryChangesCannotRemoveRemainingOpportunitiesForAssignedMissions()
    {
        var ids = new SessionFixture().Players.Select(p => p.Id).ToArray();
        var questions = Questions(10);
        var history = new StrategySession(ids, new FixedRandom(0), questions, new());
        Assert.False(history.MissionsPossible(questions.Where(q => q.CategoryId != "history").ToArray()));
        Assert.True(history.MissionsPossible(questions));
        var disabled = new StrategySession(ids, new FixedRandom(0), questions.Take(1).ToArray(), new());
        Assert.All(ids, id => Assert.Null(disabled.Private(id, TimeSpan.Zero, []).Mission));
    }

    [Fact]
    public void ArmedDoubleMovesToNextQuestionThenExpiresAndDisconnectedPlayersCannotAct()
    {
        var f = new Fixture(); f.EarnCard(); f.Answer(); f.Match.Advance();
        Assert.Equal(CardError.None, f.Play(0, f.Private().Hand[0].Id));
        f.Match.Advance(); if (f.Match.Snapshot.Phase == GamePhase.RoundEnd) f.Match.Advance();
        f.Answer(); Assert.Equal(4600, f.Match.Snapshot.Reveal!.Players[0].Points); f.Next();
        Assert.False(f.Private().DoublePoints);
        var card = f.Private().Hand[0];
        Assert.Equal(CardError.InvalidReceiveTime, f.Play(0, card.Id, received: f.Base.Clock.Now + TimeSpan.FromTicks(1)));
        f.Match.Disconnect(f.Base.Players[0].Id);
        Assert.Equal(CardError.UnknownPlayer, f.Play(0, card.Id));
        Assert.Equal(SubmissionError.UnknownPlayer, f.Match.Submit(new(f.Base.Players[0].Id, f.Match.Snapshot.Question!.InstanceId, f.Correct), f.Base.Clock.Now));
    }

    [Fact]
    public void ExtraTimeAcceptsExactPersonalDeadlineButRejectsNextTick()
    {
        foreach (var ticks in new[] { 0L, 1L })
        {
            var f = new Fixture(2); f.EarnCard(); Assert.Equal(CardError.None, f.Play(0, f.Private().Hand[0].Id));
            f.Base.Clock.Advance(TimeSpan.FromSeconds(25) + TimeSpan.FromTicks(ticks));
            Assert.Equal(ticks == 0 ? SubmissionError.None : SubmissionError.Late,
                f.Match.Submit(new(f.Base.Players[0].Id, f.Match.Snapshot.Question!.InstanceId, f.Correct), f.Base.Clock.Now));
        }
    }

    [Theory]
    [InlineData(0)] [InlineData(1)] [InlineData(2)] [InlineData(4)]
    public void EffectsCannotStackAndRejectedSecondCardRemainsInHand(int kind)
    {
        var f = new Fixture(kind, steal: true); f.EarnCard(); f.Answer(); f.Next();
        var cards = f.Private().Hand.ToArray(); Assert.Equal(2, cards.Length);
        Assert.Equal(CardError.None, f.Play(0, cards[0].Id));
        Assert.Equal(CardError.EffectActive, f.Play(0, cards[1].Id));
        Assert.Contains(cards[1], f.Private().Hand);
    }

    [Fact]
    public void SeedClockQuestionAndCardIdentifiersReplayStrategyStateDeterministically()
    {
        string Run()
        {
            var f = new SessionFixture(); var instance = 0; var card = 100;
            var match = new FullMatch(f.Players, f.Clock, new SeededRandomSource(12), Questions(10), new(10, strategy: new()),
                nextInstance: () => new(new Guid(++instance, 0, 0, new byte[8])), nextCard: () => new Guid(++card, 0, 0, new byte[8]));
            var observations = new List<string>();
            while (match.Snapshot.Phase != GamePhase.GameOver)
            {
                observations.Add(System.Text.Json.JsonSerializer.Serialize(f.Players.Select(p => match.Private(p.Id))));
                if (match.Snapshot.Phase == GamePhase.QuestionActive)
                {
                    var own = match.Private(f.Players[0].Id)!;
                    var usable = own.Hand.FirstOrDefault(c => c.Kind is CardKind.DoublePoints or CardKind.FiftyFifty or CardKind.ExtraTime);
                    if (usable is not null) Assert.Equal(CardError.None, match.Activate(new(f.Players[0].Id, match.Snapshot.Question!.InstanceId, usable.Id), f.Clock.Now));
                    var correct = match.Snapshot.Question!.Answers.ToList().IndexOf("yes");
                    f.Clock.Advance(TimeSpan.FromSeconds(1));
                    for (var i = 0; i < 3; i++) match.Submit(new(f.Players[i].Id, match.Snapshot.Question.InstanceId,
                        i == 0 ? correct : (correct + 1) % 4, i == 0 ? ConfidenceLevel.AllIn : ConfidenceLevel.Safe), f.Clock.Now);
                }
                else if (match.Snapshot.Phase == GamePhase.QuestionLocked) match.Poll();
                else match.Advance();
            }
            observations.Add(System.Text.Json.JsonSerializer.Serialize(new { match.Snapshot, match.FinalStrategy, match.Winners }));
            return string.Join('\n', observations);
        }
        Assert.Equal(Run(), Run());
    }

    [Fact]
    public void MissionPoolIsFeasiblePrivateAndAwardsBonusOnlyOnceBeforeRanking()
    {
        var f = new Fixture(0, missions: true);
        Assert.Equal(MissionKind.Historian, f.Private().Mission!.Kind);
        Assert.Empty(f.Match.FinalStrategy);
        for (var i = 0; i < 30; i++) { f.Answer(othersCorrect: false); f.Next(); }
        Assert.Equal(GamePhase.GameOver, f.Match.Snapshot.Phase);
        Assert.Equal(3, f.Match.FinalStrategy.Count);
        Assert.True(f.Match.FinalStrategy[0].Mission!.Complete);
        Assert.Equal(500, f.Match.FinalStrategy[0].MissionBonus);
        Assert.All(f.Match.FinalStrategy.Skip(1), p => Assert.Equal(0, p.MissionBonus));
        var scores = f.Match.Snapshot.Scores.ToArray(); f.Match.Advance(); Assert.Equal(scores, f.Match.Snapshot.Scores);
        var preview = new FullMatch(f.Base.Players, f.Base.Clock, new FixedRandom(0), Questions(1), new(1, strategy: new()));
        Assert.Null(preview.Private(f.Base.Players[0].Id)!.Mission);
    }
}

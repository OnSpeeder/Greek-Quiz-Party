using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Scoring;
using Xunit;

namespace QuizParty.Core.Tests;

public class MatchSetupTests
{
    [Theory]
    [InlineData(1, 501)] [InlineData(2, 501)] [InlineData(3, 752)]
    [InlineData(4, 1002)] [InlineData(5, 1002)]
    public void DifficultyScalesBaseTimeAndRoundsAwayFromZero(int difficulty, int expected) =>
        Assert.Equal(expected, DifficultyScore.Scale(501, difficulty));

    [Fact]
    public void DifficultySelectionIsCopiedBoundedAndDeckNeverLeaksOtherLevels()
    {
        var levels = new[] { 1, 4 };
        var settings = new MatchSettings(1, difficulties: levels); levels[0] = 5;
        Assert.Equal(new[] { 1, 4 }, settings.Difficulties);
        Assert.Throws<ArgumentException>(() => new MatchSettings(difficulties: []));
        Assert.Throws<ArgumentException>(() => new MatchSettings(difficulties: [6]));
        var questions = Enumerable.Range(1, 5).Select(d => new QuestionDefinition($"q{d}", "Q", ["A", "B", "C", "D"], 0, "test", d, "E"));
        var deck = new QuestionDeck(questions, new SeededRandomSource(12), difficulties: settings.Difficulties);
        Assert.Equal(2, deck.Remaining);
        Assert.Equal(new[] { 1, 4 }, deck.Upcoming(5).Select(q => q.Difficulty).Order());
    }

    [Fact]
    public void SelectedCardAndMissionPoolsAreCopiedAndOnlyEligibleSelectedItemsAreAssigned()
    {
        var f = new SessionFixture();
        var cards = new[] { CardKind.ExtraTime }; var missions = new[] { MissionKind.Gambler };
        var rules = new StrategyRules { EnabledCards = cards, EnabledMissions = missions };
        cards[0] = CardKind.Steal; missions[0] = MissionKind.Historian;
        var questions = Enumerable.Range(0, 10).Select(i => new QuestionDefinition($"q{i}", "Q", ["A", "B", "C", "D"], 0, "science", 3, "E")).ToArray();
        var session = new StrategySession(f.Players.Select(p => p.Id), new SeededRandomSource(42), questions, rules);
        var id = f.Players[0].Id;
        Assert.Equal(MissionKind.Gambler, session.Private(id, TimeSpan.Zero, []).Mission!.Kind);
        for (var i = 0; i < 10; i++) session.RecordResults("science", 3, [new(id, 0, true, 1000, TimeSpan.Zero, ConfidenceLevel.Safe)]);
        Assert.All(session.Private(id, TimeSpan.Zero, []).Hand, c => Assert.Equal(CardKind.ExtraTime, c.Kind));
        Assert.NotEmpty(session.Private(id, TimeSpan.Zero, []).Hand);
        var empty = new StrategySession([id], new SeededRandomSource(42), questions,
            new StrategyRules { EnabledCards = [], EnabledMissions = [] });
        for (var i = 0; i < 10; i++) empty.RecordResults("science", 3, [new(id, 0, true, 1000, TimeSpan.Zero, ConfidenceLevel.Safe)]);
        Assert.Empty(empty.Private(id, TimeSpan.Zero, []).Hand);
        Assert.Null(empty.Private(id, TimeSpan.Zero, []).Mission);
        var impossible = new StrategySession([id], new SeededRandomSource(42), questions,
            new StrategyRules { EnabledMissions = [MissionKind.Historian] });
        Assert.Null(impossible.Private(id, TimeSpan.Zero, []).Mission);
    }
}

using QuizParty.Core.Scoring;
using Xunit;

namespace QuizParty.Core.Tests;

public class ScoreCalculatorTests
{
    [Theory]
    [InlineData(0, 550)]
    [InlineData(15, 525)]
    [InlineData(30, 500)]
    [InlineData(1000, 500)]
    public void UntimedSpeedBonusIsSmallAndExpires(int seconds, int expected)
    {
        var calculator = new ScoreCalculator(new());
        Assert.Equal(expected, calculator.CalculateUntimed(true, TimeSpan.FromSeconds(seconds)));
        Assert.Equal(0, calculator.CalculateUntimed(false, TimeSpan.FromSeconds(seconds)));
    }

    [Theory]
    [InlineData(0, 1000)]
    [InlineData(1, 950)]
    [InlineData(5, 750)]
    [InlineData(9, 550)]
    [InlineData(10, 500)]
    public void CorrectAnswerUsesRemainingTime(int elapsedSeconds, int expected)
    {
        var calculator = new ScoreCalculator(new());
        Assert.Equal(expected, calculator.Calculate(true, TimeSpan.FromSeconds(elapsedSeconds), TimeSpan.FromSeconds(10)));
    }

    [Theory]
    [InlineData(0)]
    [InlineData(5)]
    [InlineData(10)]
    public void WrongAnswerAlwaysScoresZero(int elapsedSeconds)
    {
        Assert.Equal(0, new ScoreCalculator(new()).Calculate(false,
            TimeSpan.FromSeconds(elapsedSeconds), TimeSpan.FromSeconds(10)));
    }

    [Fact]
    public void BonusMidpointRoundsAwayFromZeroAndRulesAreConfigurable()
    {
        var calculator = new ScoreCalculator(new(baseCorrect: 20, timeBonusMax: 1));
        Assert.Equal(21, calculator.Calculate(true, TimeSpan.FromTicks(1), TimeSpan.FromTicks(2)));
        Assert.Equal(20, calculator.Calculate(true, TimeSpan.FromTicks(2), TimeSpan.FromTicks(2)));
        Assert.Equal(0, new ScoreCalculator(new(0, 0)).Calculate(true, TimeSpan.Zero, TimeSpan.FromTicks(1)));
    }

    [Fact]
    public void TickPrecisionAndLargeDurationDoNotOverflow()
    {
        var calculator = new ScoreCalculator(new());
        Assert.Equal(500, calculator.Calculate(true, TimeSpan.FromTicks(99999), TimeSpan.FromTicks(100000)));
        Assert.Equal(1000, calculator.Calculate(true, TimeSpan.Zero, TimeSpan.MaxValue));
    }

    [Theory]
    [InlineData(-1, 10)]
    [InlineData(11, 10)]
    [InlineData(0, 0)]
    [InlineData(0, -1)]
    public void InvalidTimingIsRejectedEvenForWrongAnswers(long elapsedTicks, long durationTicks)
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new ScoreCalculator(new()).Calculate(false,
            TimeSpan.FromTicks(elapsedTicks), TimeSpan.FromTicks(durationTicks)));
    }

    [Theory]
    [InlineData(-1, 500)]
    [InlineData(500, -1)]
    [InlineData(int.MaxValue, 1)]
    public void InvalidScoringParametersAreRejected(int baseCorrect, int timeBonusMax)
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new ScoringRules(baseCorrect, timeBonusMax));
    }
}

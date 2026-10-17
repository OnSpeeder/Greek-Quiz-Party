namespace QuizParty.Core.Scoring;

public sealed record ScoringRules
{
    public ScoringRules(int baseCorrect = 500, int timeBonusMax = 500)
    {
        ArgumentOutOfRangeException.ThrowIfNegative(baseCorrect);
        ArgumentOutOfRangeException.ThrowIfNegative(timeBonusMax);
        if ((long)baseCorrect + timeBonusMax > int.MaxValue)
            throw new ArgumentOutOfRangeException(nameof(timeBonusMax));
        BaseCorrect = baseCorrect;
        TimeBonusMax = timeBonusMax;
    }

    public int BaseCorrect { get; }
    public int TimeBonusMax { get; }
}

public sealed class ScoreCalculator(ScoringRules rules)
{
    public int Calculate(bool isCorrect, TimeSpan elapsed, TimeSpan duration)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(duration.Ticks);
        if (elapsed < TimeSpan.Zero || elapsed > duration) throw new ArgumentOutOfRangeException(nameof(elapsed));
        if (!isCorrect) return 0;
        // Decimal tick ratios avoid platform-dependent floating point midpoint behavior.
        var bonus = decimal.Round((decimal)rules.TimeBonusMax * (duration.Ticks - elapsed.Ticks) / duration.Ticks,
            0, MidpointRounding.AwayFromZero);
        return checked(rules.BaseCorrect + (int)bonus);
    }
}

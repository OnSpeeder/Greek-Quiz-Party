namespace QuizParty.Core.Scoring;

/// <summary>Approved difficulty bands; applied to positive base/time points before strategy.</summary>
public static class DifficultyScore
{
    public static int Scale(int raw, int difficulty)
    {
        ArgumentOutOfRangeException.ThrowIfNegative(raw);
        var multiplier = difficulty switch
        {
            1 or 2 => 1m,
            3 => 1.5m,
            4 or 5 => 2m,
            _ => throw new ArgumentOutOfRangeException(nameof(difficulty))
        };
        return checked((int)decimal.Round(raw * multiplier, 0, MidpointRounding.AwayFromZero));
    }
}

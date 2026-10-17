namespace QuizParty.Core.Randomness;

public interface IRandomSource
{
    /// <summary>Returns a value in [0, exclusiveUpperBound).</summary>
    int Next(int exclusiveUpperBound);
}

public sealed class SeededRandomSource(int seed) : IRandomSource
{
    private readonly Random _random = new(seed);
    public int Next(int exclusiveUpperBound)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(exclusiveUpperBound);
        return _random.Next(exclusiveUpperBound);
    }
}

using System.Diagnostics;

namespace QuizParty.Core.Time;

/// <summary>Host monotonic time since an arbitrary origin; never a client wall clock.</summary>
public interface IGameClock
{
    TimeSpan Now { get; }
}

public sealed class MonotonicGameClock : IGameClock
{
    private readonly Stopwatch _stopwatch = Stopwatch.StartNew();
    public TimeSpan Now => _stopwatch.Elapsed;
}

namespace QuizParty.Core.Time;

/// <summary>Monotonic match time excluding pauses, independent of presentation frames.</summary>
public sealed class PausableGameClock(IGameClock source) : IGameClock
{
    private TimeSpan _excluded;
    private TimeSpan? _pausedAt;
    public TimeSpan Now => (_pausedAt ?? source.Now) - _excluded;
    public bool IsPaused => _pausedAt is not null;
    public TimeSpan At(TimeSpan sourceTime) => sourceTime - _excluded;
    public void Pause() => _pausedAt ??= source.Now;
    public void Resume()
    {
        if (_pausedAt is not { } start) return;
        _excluded += source.Now - start;
        _pausedAt = null;
    }
}

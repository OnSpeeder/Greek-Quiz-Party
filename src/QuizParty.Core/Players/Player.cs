namespace QuizParty.Core.Players;

public readonly record struct PlayerId(Guid Value);
public readonly record struct ConnectionId(long Value);
public readonly record struct LocalSlot(int Value);

public sealed record Player
{
    public Player(PlayerId id, string displayName, ConnectionId? connectionId = null, LocalSlot? localSlot = null)
    {
        if (id.Value == Guid.Empty) throw new ArgumentException("Player ID must not be empty.", nameof(id));
        ArgumentException.ThrowIfNullOrWhiteSpace(displayName);
        if (displayName.Length > 32) throw new ArgumentOutOfRangeException(nameof(displayName));
        if (connectionId is { Value: <= 0 }) throw new ArgumentOutOfRangeException(nameof(connectionId));
        if (localSlot is { Value: < 0 or > 7 }) throw new ArgumentOutOfRangeException(nameof(localSlot));
        Id = id;
        DisplayName = displayName;
        ConnectionId = connectionId;
        LocalSlot = localSlot;
    }

    public PlayerId Id { get; }
    public string DisplayName { get; }
    public ConnectionId? ConnectionId { get; }
    public LocalSlot? LocalSlot { get; }
}

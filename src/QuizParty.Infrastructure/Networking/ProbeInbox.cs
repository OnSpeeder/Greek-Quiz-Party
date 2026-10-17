namespace QuizParty.Infrastructure.Networking;

/// <summary>Disposable Phase 01 probe contract, not a player roster or game domain.</summary>
public sealed class ProbeInbox
{
    public const int ProtocolVersion = 1;
    public const int MaxClients = 7;
    public const int MaxRequestsPerClient = 256;
    private readonly Dictionary<long, Dictionary<Guid, int>> _clients = new();

    public int AcceptedCount { get; private set; }

    public bool TryHello(long connectionId, int protocol, string platform)
    {
        if (connectionId <= 1 || protocol != ProtocolVersion ||
            platform is not ("Windows" or "Android" or "Linux" or "macOS"))
            return false;
        if (_clients.ContainsKey(connectionId))
            return true;
        if (_clients.Count >= MaxClients)
            return false;
        _clients.Add(connectionId, new Dictionary<Guid, int>());
        return true;
    }

    public ProbeReceipt Receive(long connectionId, int protocol, string requestId)
    {
        if (protocol != ProtocolVersion || !_clients.TryGetValue(connectionId, out var requests) ||
            string.IsNullOrEmpty(requestId) || requestId.Length != 32 ||
            !Guid.TryParseExact(requestId, "N", out var id) || id == Guid.Empty)
            return new ProbeReceipt(false, false, 0);
        if (requests.TryGetValue(id, out var previousCount))
            return new ProbeReceipt(true, true, previousCount);
        if (requests.Count >= MaxRequestsPerClient)
            return new ProbeReceipt(false, false, 0);
        var count = ++AcceptedCount;
        requests.Add(id, count);
        return new ProbeReceipt(true, false, count);
    }

    public void Disconnect(long connectionId) => _clients.Remove(connectionId);
}

public sealed record ProbeReceipt(bool Accepted, bool Duplicate, int HostCount);

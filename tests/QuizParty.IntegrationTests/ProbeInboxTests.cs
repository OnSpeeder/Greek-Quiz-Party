using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class ProbeInboxTests
{
    [Fact]
    public void DuplicateReturnsOriginalReceiptWithoutApplyingTwice()
    {
        var inbox = new ProbeInbox();
        Assert.True(inbox.TryHello(42, 1, "Android"));
        var request = Guid.NewGuid().ToString("N");
        Assert.Equal(new ProbeReceipt(true, false, 1), inbox.Receive(42, 1, request));
        Assert.Equal(new ProbeReceipt(true, true, 1), inbox.Receive(42, 1, request));
        Assert.Equal(1, inbox.AcceptedCount);
    }

    [Fact]
    public void RejectsUnregisteredMalformedAndIncompatibleRequests()
    {
        var inbox = new ProbeInbox();
        var request = Guid.NewGuid().ToString("N");
        Assert.False(inbox.Receive(42, 1, request).Accepted);
        Assert.False(inbox.TryHello(42, 2, "Android"));
        Assert.False(inbox.TryHello(1, 1, "Windows"));
        Assert.False(inbox.TryHello(42, 1, new string('x', 1000)));
        Assert.True(inbox.TryHello(42, 1, "Android"));
        Assert.False(inbox.Receive(42, 2, request).Accepted);
        Assert.False(inbox.Receive(42, 1, new string('a', 1000)).Accepted);
        Assert.False(inbox.Receive(42, 1, Guid.Empty.ToString("N")).Accepted);
        Assert.Equal(0, inbox.AcceptedCount);
    }

    [Fact]
    public void HandshakeRetryPreservesDeduplicationAndDisconnectRevokesAccess()
    {
        var inbox = new ProbeInbox();
        inbox.TryHello(42, 1, "Android");
        var request = Guid.NewGuid().ToString("N");
        inbox.Receive(42, 1, request);
        inbox.TryHello(42, 1, "Android");
        Assert.True(inbox.Receive(42, 1, request).Duplicate);
        inbox.Disconnect(42);
        Assert.False(inbox.Receive(42, 1, request).Accepted);
    }

    [Fact]
    public void BoundsClientsAndRequestsButStillAcknowledgesCachedDuplicates()
    {
        var inbox = new ProbeInbox();
        for (var connection = 2; connection < 2 + ProbeInbox.MaxClients; connection++)
            Assert.True(inbox.TryHello(connection, 1, "Android"));
        Assert.False(inbox.TryHello(99, 1, "Android"));
        var original = Guid.NewGuid().ToString("N");
        inbox.Receive(2, 1, original);
        for (var i = 1; i < ProbeInbox.MaxRequestsPerClient; i++)
            Assert.True(inbox.Receive(2, 1, Guid.NewGuid().ToString("N")).Accepted);
        Assert.False(inbox.Receive(2, 1, Guid.NewGuid().ToString("N")).Accepted);
        Assert.Equal(new ProbeReceipt(true, true, 1), inbox.Receive(2, 1, original));
    }
}

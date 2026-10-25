using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using QuizParty.Core.Game;
using Xunit;

namespace QuizParty.Core.Tests;

public class OptionalHostTests
{
    private static Player Player(int connection) => new(new(Guid.NewGuid()), "Player", new(connection), new(0));
    [Theory]
    [InlineData(2)] [InlineData(4)] [InlineData(8)]
    public void HostAuthorityDoesNotNeedAPlayerAndCapacityCountsOnlyRealPlayers(int capacity)
    {
        var lobby = LobbySession.WithoutHostPlayer(capacity);
        Assert.False(lobby.HostPlays); Assert.Empty(lobby.GetSnapshot().Players);
        Assert.Equal(LobbyError.UnknownConnection, lobby.SetReady(LobbySession.HostConnection, true));
        Assert.Equal(LobbyError.NotReady, lobby.Start(LobbySession.HostConnection));
        Assert.Equal(LobbyError.NotHost, lobby.Start(new(2)));
        for (var i = 2; i < capacity + 2; i++)
        {
            Assert.Equal(LobbyError.None, lobby.Join(Player(i)));
            Assert.Equal(LobbyError.None, lobby.SetReady(new(i), true));
        }
        Assert.Equal(capacity, lobby.GetSnapshot().Players.Count);
        Assert.Equal(LobbyError.RoomFull, lobby.Join(Player(capacity + 2)));
        Assert.Equal(LobbyError.None, lobby.Start(LobbySession.HostConnection));
        Assert.Equal(GamePhase.GameStarting, lobby.GetSnapshot().Phase);
    }
    [Fact]
    public void ParticipatingHostConsumesASeatAndCapacityIsBounded()
    {
        var lobby = new LobbySession(Player(1), 2);
        Assert.True(lobby.HostPlays); Assert.Single(lobby.GetSnapshot().Players);
        Assert.Equal(LobbyError.None, lobby.Join(Player(2)));
        Assert.Equal(LobbyError.RoomFull, lobby.Join(Player(3)));
        Assert.Throws<ArgumentOutOfRangeException>(() => LobbySession.WithoutHostPlayer(1));
        Assert.Throws<ArgumentOutOfRangeException>(() => LobbySession.WithoutHostPlayer(9));
    }
}

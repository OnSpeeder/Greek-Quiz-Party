using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using Xunit;

namespace QuizParty.Core.Tests;

public class LobbySessionTests
{
    private static Player Player(int connection) => new(new(new Guid(connection, 0, 0, new byte[8])),
        $"Παίκτης {connection}", new(connection), new(0));

    [Fact]
    public void PartyStartRequiresTwoPlayersAllReadyAndHostAuthority()
    {
        var lobby = new LobbySession(Player(1));
        Assert.Equal(GamePhase.Lobby, lobby.GetSnapshot().Phase);
        Assert.True(lobby.GetSnapshot().Players.Single().Ready);
        Assert.Equal(LobbyError.NotReady, lobby.Start(new(1)));
        Assert.Equal(LobbyError.None, lobby.Join(Player(2)));
        Assert.Equal(LobbyError.NotHost, lobby.Start(new(2)));
        Assert.Equal(LobbyError.NotReady, lobby.Start(new(1)));
        Assert.Equal(LobbyError.None, lobby.SetReady(new(2), true));
        Assert.Equal(LobbyError.None, lobby.SetReady(new(1), false));
        Assert.Equal(LobbyError.NotReady, lobby.Start(new(1)));
        Assert.Equal(LobbyError.None, lobby.SetReady(new(1), true));
        Assert.Equal(LobbyError.None, lobby.Start(new(1)));
        Assert.Equal(GamePhase.GameStarting, lobby.GetSnapshot().Phase);
        Assert.Equal(LobbyError.GameStarted, lobby.Start(new(1)));
        Assert.Equal(LobbyError.GameStarted, lobby.Join(Player(3)));
        Assert.Equal(LobbyError.GameStarted, lobby.SetReady(new(2), false));
    }

    [Fact]
    public void ReadySetterIsIdempotentAndOnlyChangesOwnedPlayer()
    {
        var lobby = new LobbySession(Player(1));
        lobby.Join(Player(2));
        lobby.Join(Player(3));
        var old = lobby.GetSnapshot();
        Assert.Equal(LobbyError.UnknownConnection, lobby.SetReady(new(99), true));
        Assert.Equal(LobbyError.None, lobby.SetReady(new(2), true));
        var changed = lobby.GetSnapshot();
        Assert.Equal(old.Revision + 1, changed.Revision);
        Assert.False(old.Players.Single(player => player.Player.ConnectionId == new ConnectionId(2)).Ready);
        Assert.False(changed.Players.Single(player => player.Player.ConnectionId == new ConnectionId(3)).Ready);
        Assert.Equal(LobbyError.None, lobby.SetReady(new(2), true));
        Assert.Equal(changed.Revision, lobby.GetSnapshot().Revision);
        Assert.Throws<NotSupportedException>(() => ((IList<LobbyPlayer>)old.Players).Clear());
    }

    [Fact]
    public void CapacityDuplicatesAndDisconnectsAreBounded()
    {
        var lobby = new LobbySession(Player(1));
        for (var connection = 2; connection <= 8; connection++) Assert.Equal(LobbyError.None, lobby.Join(Player(connection)));
        Assert.Equal(LobbyError.RoomFull, lobby.Join(Player(9)));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.Join(Player(1)));
        Assert.Equal(LobbyError.AlreadyJoined, lobby.Join(new(new(Guid.NewGuid()), "Άλλος", new(2))));
        var revision = lobby.GetSnapshot().Revision;
        Assert.False(lobby.Disconnect(new(1)));
        Assert.False(lobby.Disconnect(new(99)));
        Assert.True(lobby.Disconnect(new(2)));
        Assert.False(lobby.Disconnect(new(2)));
        Assert.Null(lobby.FindPlayer(new(2)));
        Assert.Equal(revision + 1, lobby.GetSnapshot().Revision);
        Assert.Equal(LobbyError.None, lobby.Join(Player(9)));
        Assert.Equal(8, lobby.GetSnapshot().Players.Count);
    }

    [Fact]
    public void HostAndRemoteConnectionIdentityCannotBeConfused()
    {
        Assert.Throws<ArgumentException>(() => new LobbySession(Player(2)));
        var lobby = new LobbySession(Player(1));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.Join(new(new(Guid.NewGuid()), "Local", localSlot: new(1))));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.Join(new(Player(1).Id, "Duplicate", new(2))));
        Assert.Single(lobby.GetSnapshot().Players);
    }
}

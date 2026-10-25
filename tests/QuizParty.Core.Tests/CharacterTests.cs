using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using Xunit;

namespace QuizParty.Core.Tests;

public class CharacterTests
{
    private static Player Player(long connection, int slot, CharacterId? character = null) =>
        new(new(Guid.NewGuid()), "Παίκτης", new(connection), new(slot), character);

    [Fact]
    public void ExplicitClaimsAreAtomicAcrossConnectionsAndLocalSlotsAndReleaseOnDeparture()
    {
        var lobby = new LobbySession(Player(1, 0, CharacterId.Yeti));
        Assert.Equal(LobbyError.CharacterTaken, lobby.Join(Player(2, 0, CharacterId.Yeti)));
        Assert.Equal(LobbyError.None, lobby.Join(Player(2, 0, CharacterId.Teal)));
        var revision = lobby.GetSnapshot().Revision;
        Assert.Equal(LobbyError.CharacterTaken, lobby.Join(Player(3, 0, CharacterId.Teal)));
        Assert.Equal(revision, lobby.GetSnapshot().Revision);
        Assert.Equal(LobbyError.CharacterTaken, lobby.AddLocal(Player(1, 1, CharacterId.Teal)));
        Assert.True(lobby.Disconnect(new(2)));
        Assert.Equal(LobbyError.None, lobby.Join(Player(3, 0, CharacterId.Teal)));
        Assert.Equal(LobbyError.None, lobby.AddLocal(Player(1, 1, CharacterId.Purple)));
        Assert.Equal(LobbyError.None, lobby.RemoveLocal(new(1), new(1)));
        Assert.Equal(LobbyError.None, lobby.AddLocal(Player(1, 1, CharacterId.Purple)));
    }

    [Fact]
    public void EightAutomaticProbePlayersReceiveEightDistinctCharacters()
    {
        var lobby = new LobbySession(Player(1, 0));
        for (var connection = 2; connection <= 8; connection++)
            Assert.Equal(LobbyError.None, lobby.Join(Player(connection, 0)));
        var characters = lobby.GetSnapshot().Players.Select(p => p.Player.Character).ToArray();
        Assert.All(characters, character => Assert.NotNull(character));
        Assert.Equal(8, characters.Distinct().Count());
        Assert.Equal(LobbyError.RoomFull, lobby.Join(Player(9, 0)));
    }
}

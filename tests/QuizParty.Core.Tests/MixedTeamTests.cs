using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class MixedTeamTests
{
    private static Player Player(int connection, int slot) => new(new(new Guid(connection * 100 + slot, 0, 0, new byte[8])),
        $"Player {connection}/{slot}", new(connection), new(slot));
    public static IEnumerable<object[]> Combinations => Enumerable.Range(2, 7).SelectMany(count => new[] { new object[] { count, false }, [count, true] });

    [Theory, MemberData(nameof(Combinations))]
    public void TwoToEightLocalOrMixedPlayersHaveIndependentSlotsReadinessAndTeams(int count, bool mixed)
    {
        var lobby = new LobbySession(Player(1, 0));
        var localCount = mixed ? count / 2 : count;
        for (var i = 1; i < localCount; i++) Assert.Equal(LobbyError.None, lobby.AddLocal(Player(1, i)));
        if (mixed)
        {
            Assert.Equal(LobbyError.None, lobby.Join(Player(2, 0)));
            for (var i = 1; i < count - localCount; i++) Assert.Equal(LobbyError.None, lobby.AddLocal(Player(2, i)));
        }
        var roster = lobby.GetSnapshot().Players;
        Assert.Equal(count, roster.Count); Assert.Single(roster, p => p.IsHost);
        Assert.Equal(count, roster.Select(p => (p.Player.ConnectionId, p.Player.LocalSlot)).Distinct().Count());
        Assert.Equal(LobbyError.NotReady, lobby.Start(new(1)));
        foreach (var p in roster) Assert.Equal(LobbyError.None, lobby.SetReady(p.Player.ConnectionId!.Value, true, p.Player.LocalSlot));
        Assert.Equal(LobbyError.NotHost, lobby.SetTeamMode(new(2), true));
        Assert.Equal(LobbyError.None, lobby.SetTeamMode(new(1), true));
        var teams = lobby.Teams()!;
        var scores = teams.Scores(roster.Select(p => new PlayerScore(p.Player.Id, p.Player.DisplayName, p.Player.LocalSlot!.Value.Value + 1)).ToArray());
        Assert.Equal(count, scores.Sum(s => s.Members.Count));
        Assert.Equal(roster.Sum(p => (long)p.Player.LocalSlot!.Value.Value + 1), scores.Sum(s => s.Total));
        Assert.Equal(LobbyError.None, lobby.Start(new(1)));
        Assert.Equal(LobbyError.GameStarted, lobby.AddLocal(Player(1, 7)));
        if (mixed)
        {
            Assert.True(lobby.Disconnect(new(2))); Assert.Equal(localCount, lobby.GetSnapshot().Players.Count);
            Assert.False(lobby.Disconnect(new(2))); Assert.False(lobby.Disconnect(new(1)));
        }
    }

    [Fact]
    public void SlotOwnershipCapacityRemovalAndHostOnlyTeamChangesAreValidated()
    {
        var lobby = new LobbySession(Player(1, 0)); lobby.Join(Player(2, 0));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.AddLocal(Player(3, 1)));
        Assert.Equal(LobbyError.None, lobby.AddLocal(Player(2, 1)));
        Assert.Equal(LobbyError.AlreadyJoined, lobby.AddLocal(new(new(Guid.NewGuid()), "Duplicate", new(2), new(1))));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.RemoveLocal(new(2), new(0)));
        Assert.Equal(LobbyError.InvalidPlayer, lobby.RemoveLocal(new(1), new(1)));
        Assert.Equal(LobbyError.None, lobby.RemoveLocal(new(2), new(1)));
        Assert.Equal(LobbyError.None, lobby.AddLocal(Player(2, 1)));
        Assert.False(lobby.GetSnapshot().Players.Single(p => p.Player.Id == Player(2, 1).Id).Ready);
        for (var i = 2; i < 7; i++) Assert.Equal(LobbyError.None, lobby.AddLocal(Player(2, i)));
        Assert.Equal(LobbyError.RoomFull, lobby.AddLocal(Player(1, 1)));
        lobby.SetTeamMode(new(1), true);
        Assert.Equal(LobbyError.NotHost, lobby.SetTeam(new(2), Player(1, 0).Id, TeamId.B));
        foreach (var p in lobby.GetSnapshot().Players) { lobby.SetTeam(new(1), p.Player.Id, TeamId.A); lobby.SetReady(p.Player.ConnectionId!.Value, true, p.Player.LocalSlot); }
        Assert.Equal(LobbyError.InvalidTeam, lobby.Start(new(1)));
        Assert.Equal(LobbyError.None, lobby.SetTeam(new(1), Player(2, 1).Id, TeamId.B));
        Assert.Equal(LobbyError.None, lobby.Start(new(1)));
        Assert.Equal(LobbyError.GameStarted, lobby.SetTeam(new(1), Player(2, 1).Id, TeamId.A));
    }

    private sealed class Fixture
    {
        public Player[] Players { get; } = Enumerable.Range(0, 4).Select(i => Player(i / 2 + 1, i % 2)).ToArray();
        public FakeClock Clock { get; } = new();
        public FullMatch Match { get; }
        public Fixture(int questions = 1, int available = 1, StrategyRules? strategy = null, int random = 0)
        {
            var teams = new TeamRoster(Players.Select(p => p.Id), Players.Select((p, i) => new PlayerTeam(p.Id, i < 2 ? TeamId.A : TeamId.B)));
            var content = Enumerable.Range(0, available).Select(i => new QuestionDefinition($"q{i}", $"Test {i}", ["yes", "no", "other", "last"], 0, "history", 5, "Test only"));
            Match = new(Players, Clock, new FixedRandom(random), content, new(questions, strategy: strategy), teams: teams);
        }
        public void Answer(int actor, bool correct = true, ConfidenceLevel confidence = ConfidenceLevel.Safe) => Assert.Equal(SubmissionError.None,
            Match.Submit(new(Players[actor].Id, Match.Snapshot.Question!.InstanceId,
                (Match.Snapshot.Question.Answers.ToList().IndexOf("yes") + (correct ? 0 : 1)) % 4, confidence), Clock.Now));
        public void RevealAndAdvance()
        {
            Assert.True(Match.Poll()); Match.Advance(); Match.Advance();
        }
    }
    private sealed class FixedRandom(int value) : IRandomSource { public int Next(int upper) => Math.Min(value, upper - 1); }

    [Fact]
    public void TeamAggregateWinsEvenWhenOpponentHasHighestIndividualScore()
    {
        var f = new Fixture(); f.Clock.Advance(TimeSpan.FromSeconds(10)); f.Answer(2);
        f.Clock.Advance(TimeSpan.FromSeconds(10)); f.Answer(0); f.Answer(1); f.Answer(3, false); f.RevealAndAdvance();
        Assert.Equal(GamePhase.GameOver, f.Match.Snapshot.Phase);
        Assert.Equal(new[] { TeamId.A }, f.Match.WinningTeams);
        Assert.Equal(f.Players.Take(2).Select(p => p.Id), f.Match.Winners);
        Assert.Equal(2000, f.Match.TeamScores[0].Total); Assert.Equal(1500, f.Match.TeamScores[1].Total);
        Assert.Equal(f.Players[2].Id, f.Match.Snapshot.Scores.MaxBy(s => s.Total)!.PlayerId);
    }

    [Theory]
    [InlineData(false)] [InlineData(true)]
    public void TiedTeamsUseHostReceiveTimesAndExhaustionKeepsBothTeams(bool exactTie)
    {
        var f = new Fixture(available: 2); for (var i = 0; i < 4; i++) f.Answer(i); f.RevealAndAdvance();
        Assert.True(f.Match.IsTieBreaker); Assert.Empty(f.Match.WinningTeams); f.Match.Advance();
        Assert.Equal(4, f.Match.Eligible.Count); var totals = f.Match.TeamScores.Select(t => t.Total).ToArray();
        f.Clock.Advance(TimeSpan.FromSeconds(1)); f.Answer(2);
        if (!exactTie) f.Clock.Advance(TimeSpan.FromTicks(1));
        f.Answer(0); f.Answer(1, false); f.Answer(3, false); f.RevealAndAdvance();
        Assert.Equal(GamePhase.GameOver, f.Match.Snapshot.Phase);
        Assert.Equal(exactTie ? new[] { TeamId.A, TeamId.B } : [TeamId.B], f.Match.WinningTeams);
        Assert.Equal(exactTie, f.Match.ContentExhausted); Assert.Equal(totals, f.Match.TeamScores.Select(t => t.Total));
        Assert.Equal(exactTie ? 4 : 2, f.Match.Winners.Count);
    }

    [Fact]
    public void TeamTotalsIncludeMissionBonusesAndStealCannotTargetTeammate()
    {
        var f = new Fixture(10, 10, new(Missions: false, AllowSteal: true), 5);
        for (var question = 0; question < 3; question++)
        { for (var i = 0; i < 4; i++) f.Answer(i); f.RevealAndAdvance(); if (f.Match.Snapshot.Phase == GamePhase.RoundEnd) f.Match.Advance(); }
        var card = f.Match.Private(f.Players[0].Id)!.Hand.First(c => c.Kind == CardKind.Steal);
        for (var i = 0; i < 4; i++) f.Answer(i); f.Match.Poll(); f.Match.Advance();
        var before = f.Match.TeamScores.Select(t => t.Total).ToArray();
        CardError Steal(int target) => f.Match.Activate(new(f.Players[0].Id, f.Match.Snapshot.Question!.InstanceId, card.Id, f.Players[target].Id), f.Clock.Now);
        Assert.Equal(CardError.InvalidTarget, Steal(1)); Assert.Contains(card, f.Match.Private(f.Players[0].Id)!.Hand);
        Assert.Equal(CardError.None, Steal(2)); Assert.Equal(before[0] + 100, f.Match.TeamScores[0].Total); Assert.Equal(before[1] - 100, f.Match.TeamScores[1].Total);
        var missions = new Fixture(10, 10, new(), 0);
        for (var q = 0; q < 10; q++)
        {
            for (var i = 0; i < 4; i++) missions.Answer(i, i < 2);
            missions.RevealAndAdvance(); if (missions.Match.Snapshot.Phase == GamePhase.RoundEnd) missions.Match.Advance();
        }
        Assert.Equal(GamePhase.GameOver, missions.Match.Snapshot.Phase);
        Assert.Equal(1000, missions.Match.FinalStrategy.Sum(s => s.MissionBonus));
        Assert.Equal(missions.Match.Snapshot.Scores.Take(2).Sum(s => s.Total), missions.Match.TeamScores[0].Total);
    }

    [Fact]
    public void MembershipMustCoverRosterExactlyOnceAndContainTwoTeams()
    {
        var players = new[] { Player(1, 0).Id, Player(1, 1).Id };
        Assert.Throws<ArgumentException>(() => new TeamRoster(players, [new(players[0], TeamId.A), new(players[1], TeamId.A)]));
        Assert.Throws<ArgumentException>(() => new TeamRoster(players, [new(players[0], TeamId.A), new(players[0], TeamId.B)]));
        var valid = new TeamRoster(players, [new(players[0], TeamId.A), new(players[1], TeamId.B)]);
        Assert.Throws<ArgumentException>(() => valid.ValidateRoster([players[0]]));
        Assert.Throws<OverflowException>(() => new TeamRoster([..players, Player(2, 0).Id],
            [new(players[0], TeamId.A), new(players[1], TeamId.A), new(Player(2, 0).Id, TeamId.B)])
            .Scores([new(players[0], "a", long.MaxValue), new(players[1], "b", 1), new(Player(2, 0).Id, "c", 0)]));
    }
}

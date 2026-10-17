using QuizParty.Core.Game;
using Xunit;

namespace QuizParty.Core.Tests;

public class GameStateMachineTests
{
    private static readonly (GamePhase From, GameTrigger Trigger, GamePhase To)[] Edges =
    [
        (GamePhase.Boot, GameTrigger.Initialize, GamePhase.MainMenu),
        (GamePhase.MainMenu, GameTrigger.OpenLobby, GamePhase.Lobby),
        (GamePhase.Lobby, GameTrigger.StartGame, GamePhase.GameStarting),
        (GamePhase.GameStarting, GameTrigger.BeginRound, GamePhase.RoundIntro),
        (GamePhase.RoundIntro, GameTrigger.BeginQuestion, GamePhase.QuestionActive),
        (GamePhase.QuestionActive, GameTrigger.LockQuestion, GamePhase.QuestionLocked),
        (GamePhase.QuestionLocked, GameTrigger.RevealAnswer, GamePhase.AnswerReveal),
        (GamePhase.AnswerReveal, GameTrigger.ShowScoreboard, GamePhase.Scoreboard),
        (GamePhase.Scoreboard, GameTrigger.NextQuestion, GamePhase.QuestionActive),
        (GamePhase.Scoreboard, GameTrigger.EndRound, GamePhase.RoundEnd),
        (GamePhase.RoundEnd, GameTrigger.BeginRound, GamePhase.RoundIntro),
        (GamePhase.RoundEnd, GameTrigger.FinishGame, GamePhase.GameOver),
        (GamePhase.GameOver, GameTrigger.ReturnToLobby, GamePhase.Lobby)
    ];

    // A complete linear route reaches every phase once; branches are exercised by the matrix.
    private static readonly GameTrigger[] Route =
    [
        GameTrigger.Initialize, GameTrigger.OpenLobby, GameTrigger.StartGame,
        GameTrigger.BeginRound, GameTrigger.BeginQuestion, GameTrigger.LockQuestion,
        GameTrigger.RevealAnswer, GameTrigger.ShowScoreboard, GameTrigger.EndRound, GameTrigger.FinishGame
    ];

    public static IEnumerable<object[]> TransitionCases()
    {
        foreach (var phase in Enum.GetValues<GamePhase>())
        foreach (var trigger in Enum.GetValues<GameTrigger>())
        {
            var edge = Edges.Where(edge => edge.From == phase && edge.Trigger == trigger).ToArray();
            yield return [phase, trigger, edge.Length == 1 ? edge[0].To : phase, edge.Length == 1];
        }
    }

    [Theory]
    [MemberData(nameof(TransitionCases))]
    public void EveryStateTriggerPairEitherTransitionsOrPreservesState(GamePhase source,
        GameTrigger trigger, GamePhase expected, bool allowed)
    {
        var machine = new GameStateMachine(GameAuthority.Host);
        foreach (var step in Route)
        {
            if (machine.Phase == source) break;
            Assert.Equal(GameError.None, machine.TryTransition(step));
        }
        Assert.Equal(source, machine.Phase);
        Assert.Equal(allowed ? GameError.None : GameError.InvalidTransition, machine.TryTransition(trigger));
        Assert.Equal(expected, machine.Phase);
    }

    [Fact]
    public void ClientsCannotAdvanceAuthorityAndUnknownTriggerIsRejected()
    {
        var client = new GameStateMachine(GameAuthority.Client);
        foreach (var trigger in Enum.GetValues<GameTrigger>())
            Assert.Equal(GameError.NotAuthoritative, client.TryTransition(trigger));
        Assert.Equal(GamePhase.Boot, client.Phase);
        var host = new GameStateMachine(GameAuthority.Host);
        Assert.Equal(GameError.InvalidTransition, host.TryTransition((GameTrigger)999));
        Assert.Equal(GamePhase.Boot, host.Phase);
    }
}

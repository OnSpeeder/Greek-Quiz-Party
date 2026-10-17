namespace QuizParty.Core.Game;

public enum GameAuthority { Host, Client }

public enum GamePhase
{
    Boot, MainMenu, Lobby, GameStarting, RoundIntro, QuestionActive,
    QuestionLocked, AnswerReveal, Scoreboard, RoundEnd, GameOver
}

public enum GameTrigger
{
    Initialize, OpenLobby, StartGame, BeginRound, BeginQuestion, LockQuestion,
    RevealAnswer, ShowScoreboard, NextQuestion, EndRound, FinishGame, ReturnToLobby
}

public enum GameError { None, NotAuthoritative, InvalidTransition, QuestionNotReady, InvalidQuestionInstance }

public sealed class GameStateMachine(GameAuthority authority)
{
    public GamePhase Phase { get; private set; } = GamePhase.Boot;

    public GameError TryTransition(GameTrigger trigger)
    {
        if (authority != GameAuthority.Host) return GameError.NotAuthoritative;
        GamePhase? target = (Phase, trigger) switch
        {
            (GamePhase.Boot, GameTrigger.Initialize) => GamePhase.MainMenu,
            (GamePhase.MainMenu, GameTrigger.OpenLobby) => GamePhase.Lobby,
            (GamePhase.Lobby, GameTrigger.StartGame) => GamePhase.GameStarting,
            (GamePhase.GameStarting, GameTrigger.BeginRound) => GamePhase.RoundIntro,
            (GamePhase.RoundEnd, GameTrigger.BeginRound) => GamePhase.RoundIntro,
            (GamePhase.RoundIntro, GameTrigger.BeginQuestion) => GamePhase.QuestionActive,
            (GamePhase.Scoreboard, GameTrigger.NextQuestion) => GamePhase.QuestionActive,
            (GamePhase.QuestionActive, GameTrigger.LockQuestion) => GamePhase.QuestionLocked,
            (GamePhase.QuestionLocked, GameTrigger.RevealAnswer) => GamePhase.AnswerReveal,
            (GamePhase.AnswerReveal, GameTrigger.ShowScoreboard) => GamePhase.Scoreboard,
            (GamePhase.Scoreboard, GameTrigger.EndRound) => GamePhase.RoundEnd,
            (GamePhase.RoundEnd, GameTrigger.FinishGame) => GamePhase.GameOver,
            (GamePhase.GameOver, GameTrigger.ReturnToLobby) => GamePhase.Lobby,
            _ => null
        };
        if (target is null) return GameError.InvalidTransition;
        Phase = target.Value;
        return GameError.None;
    }
}

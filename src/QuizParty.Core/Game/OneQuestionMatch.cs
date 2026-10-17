using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;

namespace QuizParty.Core.Game;

/// <summary>Host coordinator for the Phase 04 slice; no transport or fixture content.</summary>
public sealed class OneQuestionMatch
{
    private readonly GameSession _game;
    public long Revision { get; private set; } = 1;
    public GameSnapshot Snapshot => _game.GetSnapshot();

    public OneQuestionMatch(IEnumerable<Player> players, IGameClock clock, IRandomSource random,
        QuestionDefinition question, QuestionInstanceId instanceId, TimeSpan duration)
    {
        _game = new(GameAuthority.Host, players, clock, random);
        Require(_game.Initialize());
        Require(_game.OpenLobby());
        Require(_game.StartGame());
        Require(_game.BeginRound());
        Require(_game.StartQuestion(question, instanceId, duration));
    }

    public SubmissionError Submit(AnswerSubmission answer, TimeSpan hostReceivedAt)
    {
        var error = _game.SubmitAnswer(answer, hostReceivedAt);
        if (error == SubmissionError.None) Revision++;
        return error;
    }

    public bool Poll()
    {
        // Preserve a locked snapshot before revealing on the next host poll.
        if (_game.Phase == GamePhase.QuestionActive)
        {
            if (_game.CloseQuestion() != GameError.None) return false;
        }
        else if (_game.Phase == GamePhase.QuestionLocked) Require(_game.RevealAnswer());
        else return false;
        Revision++;
        return true;
    }

    public GameError Advance()
    {
        if (_game.Phase == GamePhase.AnswerReveal) Require(_game.ShowScoreboard());
        else if (_game.Phase == GamePhase.Scoreboard)
        {
            Require(_game.EndRound());
            Require(_game.FinishGame());
        }
        else return GameError.InvalidTransition;
        Revision++;
        return GameError.None;
    }

    private static void Require(GameError error)
    {
        if (error != GameError.None) throw new InvalidOperationException($"Unexpected match transition: {error}");
    }
}

using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Scoring;
using QuizParty.Core.Time;

namespace QuizParty.Core.Game;

/// <summary>
/// Host coordinator for the basic question flow. Invoke on one serialized host context.
/// Transport adapters must authenticate player ownership before submitting an intent.
/// </summary>
public sealed class GameSession
{
    private readonly GameAuthority _authority;
    private readonly GameStateMachine _machine;
    private readonly IGameClock _clock;
    private readonly IRandomSource _random;
    private readonly ScoreCalculator _scoring;
    private readonly Player[] _players;
    private readonly Dictionary<PlayerId, long> _scores;
    private readonly Dictionary<PlayerId, ReceivedAnswer> _answers = new();
    private readonly HashSet<QuestionInstanceId> _usedInstances = new();
    private QuestionInstance? _question;
    private QuestionResult? _reveal;

    public GameSession(GameAuthority authority, IEnumerable<Player> players, IGameClock clock,
        IRandomSource random, ScoringRules? scoringRules = null)
    {
        ArgumentNullException.ThrowIfNull(players);
        ArgumentNullException.ThrowIfNull(clock);
        ArgumentNullException.ThrowIfNull(random);
        _players = players.Take(9).ToArray();
        if (_players.Length is < 1 or > 8 || _players.Any(player => player is null) ||
            _players.Select(player => player.Id).Distinct().Count() != _players.Length)
            throw new ArgumentException("Provide one to eight players with distinct IDs.", nameof(players));
        _authority = authority;
        _machine = new(authority);
        _clock = clock;
        _random = random;
        _scoring = new(scoringRules ?? new ScoringRules());
        _scores = _players.ToDictionary(player => player.Id, _ => 0L);
    }

    public GamePhase Phase => _machine.Phase;
    public GameError Initialize() => _machine.TryTransition(GameTrigger.Initialize);
    public GameError OpenLobby() => _machine.TryTransition(GameTrigger.OpenLobby);

    public GameError StartGame()
    {
        var error = _machine.TryTransition(GameTrigger.StartGame);
        if (error != GameError.None) return error;
        foreach (var player in _players) _scores[player.Id] = 0;
        _question = null;
        _reveal = null;
        _answers.Clear();
        // Preserve instance IDs across rematches so an old packet cannot target a reused ID.
        return GameError.None;
    }

    public GameError BeginRound() => _machine.TryTransition(GameTrigger.BeginRound);

    public GameError StartQuestion(QuestionDefinition definition, QuestionInstanceId instanceId, TimeSpan duration)
    {
        if (_authority != GameAuthority.Host) return GameError.NotAuthoritative;
        if (Phase is not (GamePhase.RoundIntro or GamePhase.Scoreboard)) return GameError.InvalidTransition;
        if (instanceId.Value == Guid.Empty || _usedInstances.Contains(instanceId)) return GameError.InvalidQuestionInstance;
        ArgumentNullException.ThrowIfNull(definition);
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(duration.Ticks);
        var now = _clock.Now;
        if (now < TimeSpan.Zero || duration > TimeSpan.MaxValue - now)
            throw new ArgumentOutOfRangeException(nameof(duration));
        var question = new QuestionInstance(definition, instanceId, now, duration, _random);
        var error = _machine.TryTransition(Phase == GamePhase.Scoreboard ? GameTrigger.NextQuestion : GameTrigger.BeginQuestion);
        if (error != GameError.None) return error;
        _question = question;
        _reveal = null;
        _answers.Clear();
        _usedInstances.Add(instanceId);
        return GameError.None;
    }

    public SubmissionError SubmitAnswer(AnswerSubmission submission) => SubmitAnswer(submission, _clock.Now);

    /// <summary>hostReceivedAt must be captured on this host, never copied from a client packet.</summary>
    public SubmissionError SubmitAnswer(AnswerSubmission submission, TimeSpan hostReceivedAt)
    {
        if (_authority != GameAuthority.Host) return SubmissionError.NotAuthoritative;
        ArgumentNullException.ThrowIfNull(submission);
        var error = SubmissionValidator.Validate(submission, Phase, _question?.Presentation,
            _scores.ContainsKey(submission.PlayerId), _answers.ContainsKey(submission.PlayerId), hostReceivedAt, _clock.Now);
        if (error != SubmissionError.None) return error;
        _answers.Add(submission.PlayerId, new(submission.AnswerIndex, hostReceivedAt));
        if (_answers.Count == _players.Length) _machine.TryTransition(GameTrigger.LockQuestion);
        return SubmissionError.None;
    }

    public GameError CloseQuestion()
    {
        if (_authority != GameAuthority.Host) return GameError.NotAuthoritative;
        if (Phase != GamePhase.QuestionActive) return GameError.InvalidTransition;
        // Exact-deadline receipts are legal. Close only after that instant, or all answers.
        if (_answers.Count < _players.Length && _clock.Now <= _question!.Presentation.Deadline)
            return GameError.QuestionNotReady;
        return _machine.TryTransition(GameTrigger.LockQuestion);
    }

    public GameError RevealAnswer()
    {
        if (_authority != GameAuthority.Host) return GameError.NotAuthoritative;
        if (Phase != GamePhase.QuestionLocked) return GameError.InvalidTransition;
        var question = _question!;
        var results = _players.Select(player => CalculateResult(player.Id, question)).ToArray();
        // Calculate every total first so overflow cannot partially mutate the session.
        var totals = results.ToDictionary(result => result.PlayerId, result => checked(_scores[result.PlayerId] + result.Points));
        var error = _machine.TryTransition(GameTrigger.RevealAnswer);
        if (error != GameError.None) return error;
        foreach (var total in totals) _scores[total.Key] = total.Value;
        _reveal = new(question.Presentation.InstanceId, question.CorrectAnswerIndex,
            question.Explanation, Array.AsReadOnly(results));
        return GameError.None;
    }

    private PlayerQuestionResult CalculateResult(PlayerId playerId, QuestionInstance question)
    {
        if (!_answers.TryGetValue(playerId, out var answer)) return new(playerId, null, false, 0);
        var correct = answer.AnswerIndex == question.CorrectAnswerIndex;
        var view = question.Presentation;
        var points = _scoring.Calculate(correct, answer.ReceivedAt - view.StartedAt, view.Deadline - view.StartedAt);
        return new(playerId, answer.AnswerIndex, correct, points);
    }

    public GameError ShowScoreboard() => _machine.TryTransition(GameTrigger.ShowScoreboard);
    public GameError EndRound() => _machine.TryTransition(GameTrigger.EndRound);
    public GameError FinishGame() => _machine.TryTransition(GameTrigger.FinishGame);

    public GameError ReturnToLobby()
    {
        var error = _machine.TryTransition(GameTrigger.ReturnToLobby);
        if (error != GameError.None) return error;
        _question = null;
        _reveal = null;
        _answers.Clear();
        return GameError.None;
    }

    public GameSnapshot GetSnapshot() => new(Phase, _question?.Presentation, _answers.Count, _reveal,
        Array.AsReadOnly(_players.Select(player => new PlayerScore(player.Id, player.DisplayName, _scores[player.Id])).ToArray()));

    private sealed record ReceivedAnswer(int AnswerIndex, TimeSpan ReceivedAt);
}

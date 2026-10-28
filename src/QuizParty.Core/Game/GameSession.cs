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
    private readonly bool _scaleDifficulty;
    private readonly Player[] _players;
    private readonly Dictionary<PlayerId, long> _scores;
    private readonly Dictionary<PlayerId, ReceivedAnswer> _answers = new();
    private readonly HashSet<QuestionInstanceId> _usedInstances = new();
    private QuestionInstance? _question;
    private QuestionResult? _reveal;
    private HashSet<PlayerId>? _eligible;
    private bool _awardPoints = true;
    private readonly StrategySession? _strategy;
    private readonly Dictionary<PlayerId, TimeSpan> _deadlines = new();
    private readonly Dictionary<PlayerId, TimeSpan> _suspendedDeadlines = new();

    public GameSession(GameAuthority authority, IEnumerable<Player> players, IGameClock clock,
        IRandomSource random, ScoringRules? scoringRules = null, StrategySession? strategy = null, bool scaleDifficulty = false)
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
        _strategy = strategy;
        _scaleDifficulty = scaleDifficulty;
        if ((long)MaximumRawScore(scoringRules) * (scaleDifficulty ? 2 : 1) * (strategy is null ? 1 : StrategyRules.MaxMultiplier) > int.MaxValue)
            throw new ArgumentOutOfRangeException(nameof(scoringRules));
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

    public GameError StartQuestion(QuestionDefinition definition, QuestionInstanceId instanceId, TimeSpan duration,
        IReadOnlyCollection<PlayerId>? eligible = null, bool awardPoints = true, bool untimed = false)
    {
        if (_authority != GameAuthority.Host) return GameError.NotAuthoritative;
        if (Phase is not (GamePhase.RoundIntro or GamePhase.Scoreboard)) return GameError.InvalidTransition;
        if (instanceId.Value == Guid.Empty || _usedInstances.Contains(instanceId)) return GameError.InvalidQuestionInstance;
        ArgumentNullException.ThrowIfNull(definition);
        if (eligible is not null && (eligible.Count == 0 || eligible.Any(id => !_scores.ContainsKey(id)) ||
            eligible.Distinct().Count() != eligible.Count)) throw new ArgumentException("Invalid eligible players.", nameof(eligible));
        if (!untimed) ArgumentOutOfRangeException.ThrowIfNegativeOrZero(duration.Ticks);
        else if (duration != TimeSpan.Zero) throw new ArgumentOutOfRangeException(nameof(duration));
        var now = _clock.Now;
        if (now < TimeSpan.Zero || duration > TimeSpan.MaxValue - now)
            throw new ArgumentOutOfRangeException(nameof(duration));
        var question = new QuestionInstance(definition, instanceId, now, duration, _random);
        var error = _machine.TryTransition(Phase == GamePhase.Scoreboard ? GameTrigger.NextQuestion : GameTrigger.BeginQuestion);
        if (error != GameError.None) return error;
        _question = question;
        _reveal = null;
        _answers.Clear();
        _eligible = eligible?.ToHashSet();
        _awardPoints = awardPoints;
        _suspendedDeadlines.Clear();
        foreach (var player in _players) _deadlines[player.Id] = question.Presentation.Deadline;
        _strategy?.BeginQuestion();
        _usedInstances.Add(instanceId);
        return GameError.None;
    }

    public SubmissionError SubmitAnswer(AnswerSubmission submission) => SubmitAnswer(submission, _clock.Now);

    /// <summary>hostReceivedAt must be captured on this host, never copied from a client packet.</summary>
    public SubmissionError SubmitAnswer(AnswerSubmission submission, TimeSpan hostReceivedAt)
    {
        if (_authority != GameAuthority.Host) return SubmissionError.NotAuthoritative;
        ArgumentNullException.ThrowIfNull(submission);
        var presentation = _question?.Presentation;
        if (presentation is not null && _deadlines.TryGetValue(submission.PlayerId, out var deadline)) presentation = presentation with { Deadline = deadline };
        var error = SubmissionValidator.Validate(submission, Phase, presentation,
            _scores.ContainsKey(submission.PlayerId) && (_eligible?.Contains(submission.PlayerId) ?? true),
            _answers.ContainsKey(submission.PlayerId), hostReceivedAt, _clock.Now, _awardPoints && _strategy?.Rules.Confidence == true);
        if (error != SubmissionError.None) return error;
        if (_strategy?.HasHidden(submission.PlayerId, submission.AnswerIndex) == true) return SubmissionError.InvalidAnswerIndex;
        _answers.Add(submission.PlayerId, new(submission.AnswerIndex, hostReceivedAt, submission.Confidence));
        if (_answers.Count == (_eligible?.Count ?? _players.Length)) _machine.TryTransition(GameTrigger.LockQuestion);
        return SubmissionError.None;
    }

    public GameError CloseQuestion()
    {
        if (_authority != GameAuthority.Host) return GameError.NotAuthoritative;
        if (Phase != GamePhase.QuestionActive) return GameError.InvalidTransition;
        // Exact-deadline receipts are legal. Close only after that instant, or all answers.
        var lastDeadline = _players.Where(p => (_eligible?.Contains(p.Id) ?? true) && !_answers.ContainsKey(p.Id))
            .Select(p => Deadline(p.Id)).DefaultIfEmpty(TimeSpan.MinValue).Max();
        if (_answers.Count < (_eligible?.Count ?? _players.Length) && _clock.Now <= lastDeadline)
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
            question.Explanation, Array.AsReadOnly(results), question.FunFacts);
        if (_awardPoints) _strategy?.RecordResults(question.Presentation.CategoryId, question.Presentation.Difficulty, results);
        return GameError.None;
    }

    private PlayerQuestionResult CalculateResult(PlayerId playerId, QuestionInstance question)
    {
        if (!_answers.TryGetValue(playerId, out var answer)) return new(playerId, null, false, 0);
        var correct = answer.AnswerIndex == question.CorrectAnswerIndex;
        var view = question.Presentation;
        var duration = view.Deadline - view.StartedAt;
        var elapsed = answer.ReceivedAt - view.StartedAt;
        var raw = view.Deadline == TimeSpan.MaxValue
            ? _scoring.Calculate(correct, TimeSpan.FromSeconds(1), TimeSpan.FromSeconds(1))
            : _scoring.Calculate(correct, elapsed > duration ? duration : elapsed, duration);
        if (_scaleDifficulty) raw = DifficultyScore.Scale(raw, view.Difficulty);
        var points = _strategy?.Delta(playerId, correct, raw, answer.Confidence, _scores[playerId]) ?? raw;
        return new(playerId, answer.AnswerIndex, correct, _awardPoints ? points : 0, elapsed, answer.Confidence);
    }

    public IReadOnlyList<PlayerId> AnsweredPlayers => _answers.Keys.ToArray();
    internal void Disconnect(PlayerId player) { if (_deadlines.TryGetValue(player, out var deadline)) { _suspendedDeadlines[player] = deadline; _deadlines[player] = TimeSpan.Zero; } }
    internal void Reconnect(PlayerId player) { if (_suspendedDeadlines.Remove(player, out var deadline)) _deadlines[player] = deadline; }
    internal bool HasAnswered(PlayerId player) => _answers.ContainsKey(player);
    internal TimeSpan Deadline(PlayerId player) => _deadlines.GetValueOrDefault(player);
    internal int[] HideWrongAnswers()
    {
        var candidates = Enumerable.Range(0, 4).Where(i => i != _question!.CorrectAnswerIndex).ToList();
        var first = _random.Next(candidates.Count);
        if (first < 0 || first >= candidates.Count) throw new InvalidOperationException("Invalid random source.");
        var hidden = candidates[first]; candidates.RemoveAt(first);
        var second = _random.Next(candidates.Count);
        if (second < 0 || second >= candidates.Count) throw new InvalidOperationException("Invalid random source.");
        return [hidden, candidates[second]];
    }
    internal void ExtendDeadline(PlayerId player) => _deadlines[player] += TimeSpan.FromSeconds(StrategyRules.ExtraSeconds);
    internal int Transfer(PlayerId actor, PlayerId target)
    {
        if (_authority != GameAuthority.Host || Phase is not (GamePhase.Scoreboard or GamePhase.RoundEnd)) throw new InvalidOperationException("Transfer window closed.");
        var amount = (int)Math.Min(StrategyRules.StealPoints, _scores[target]);
        var updated = checked(_scores[actor] + amount);
        _scores[target] -= amount; _scores[actor] = updated;
        return amount;
    }
    internal void ApplyBonuses(IReadOnlyDictionary<PlayerId, int> bonuses)
    {
        if (_authority != GameAuthority.Host || Phase != GamePhase.Scoreboard) throw new InvalidOperationException("Bonus window closed.");
        var totals = bonuses.ToDictionary(p => p.Key, p => checked(_scores[p.Key] + p.Value));
        foreach (var pair in totals) _scores[pair.Key] = pair.Value;
    }
    private static int MaximumRawScore(ScoringRules? rules) => checked((rules?.BaseCorrect ?? 500) + (rules?.TimeBonusMax ?? 500));

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

    private sealed record ReceivedAnswer(int AnswerIndex, TimeSpan ReceivedAt, ConfidenceLevel Confidence);
}

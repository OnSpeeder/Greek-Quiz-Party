using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;

namespace QuizParty.Core.Game;

public sealed record MatchSettings
{
    public int QuestionCount { get; }
    public bool Unlimited => QuestionCount == 0;
    public TimeSpan QuestionDuration { get; }
    public StrategyRules? Strategy { get; }
    public IReadOnlyList<int> Difficulties { get; }
    public MatchSettings(int questionCount = 20, int questionSeconds = 20, StrategyRules? strategy = null, IEnumerable<int>? difficulties = null)
    {
        // One question remains an explicit content preview, not a full-game preset.
        if (questionCount is not (0 or 1 or 10 or 20 or 30 or 40 or 50)) throw new ArgumentOutOfRangeException(nameof(questionCount));
        if (questionSeconds != 0 && (questionSeconds is < 5 or > 120)) throw new ArgumentOutOfRangeException(nameof(questionSeconds));
        QuestionCount = questionCount;
        QuestionDuration = TimeSpan.FromSeconds(questionSeconds);
        Strategy = strategy;
        var levels = (difficulties ?? Enumerable.Range(1, 5)).Distinct().Order().ToArray();
        if (levels.Length == 0 || levels.Any(d => d is < 1 or > 5)) throw new ArgumentException("Select valid difficulty levels.", nameof(difficulties));
        Difficulties = Array.AsReadOnly(levels);
    }
}

public sealed record PlayerStatistics(PlayerId PlayerId, int Correct, int Wrong, int Unanswered,
    int BestStreak, long ResponseTicks, int Responses)
{
    public double Accuracy => Correct + Wrong + Unanswered == 0 ? 0 : 100.0 * Correct / (Correct + Wrong + Unanswered);
    public double AverageResponseSeconds => Responses == 0 ? 0 : TimeSpan.FromTicks(ResponseTicks / Responses).TotalSeconds;
}

/// <summary>Serialized host-only full-game coordinator; randomness and time are injected.</summary>
public sealed class FullMatch
{
    private readonly GameSession _game;
    private readonly QuestionDeck _deck;
    private readonly MatchSettings _settings;
    private readonly Func<QuestionInstanceId> _nextInstance;
    private readonly Func<Guid> _nextPause;
    private readonly Dictionary<PlayerId, PlayerStatistics> _stats;
    private readonly Dictionary<PlayerId, int> _streaks;
    private PlayerId[] _eligible;
    private PlayerId[] _winners = [];
    private readonly StrategySession? _strategy;
    private readonly PausableGameClock _clock;
    private readonly IGameClock _wallClock;
    private readonly HashSet<PlayerId> _connected;
    private readonly HashSet<PlayerId> _missingAtClose = [];
    private readonly HashSet<PlayerId> _resumeVotes = [];
    private TimeSpan? _resumeAt;
    public Guid PauseId { get; private set; }
    public bool IsPaused => _clock.IsPaused;
    public bool IsCountingDown => IsPaused && _resumeAt is not null;
    public TimeSpan GameNow => _clock.Now;
    public TimeSpan ResumeRemaining
    {
        get { var remaining = _resumeAt is { } at ? at - _wallClock.Now : TimeSpan.Zero; return remaining > TimeSpan.Zero ? remaining : TimeSpan.Zero; }
    }
    public IReadOnlyList<PlayerId> DisconnectedPlayers => _stats.Keys.Where(p => !_connected.Contains(p)).ToArray();
    public IReadOnlyList<PlayerId> ResumeVotes => _resumeVotes.ToArray();
    private bool _selectionSwapped;
    private string[]? _swapCategories;
    private readonly TeamRoster? _teams;
    private TeamId[] _winningTeams = [];
    public IReadOnlyList<TeamScore> TeamScores => _teams?.Scores(Snapshot.Scores) ?? [];
    public IReadOnlyList<TeamId> WinningTeams => Array.AsReadOnly(_winningTeams.ToArray());
    public StrategyRules? Strategy => _settings.Strategy;
    public IReadOnlyList<StrategyFinal> FinalStrategy => Snapshot.Phase == GamePhase.GameOver ? _strategy?.Final() ?? [] : [];
    public long Revision { get; private set; } = 1;
    public int QuestionNumber { get; private set; }
    public int TotalQuestions => _settings.QuestionCount;
    public int RoundNumber => _settings.Unlimited ? 1 : IsTieBreaker ? Math.Min(4, TotalQuestions) + 1 :
        Math.Min(Math.Min(4, TotalQuestions), (QuestionNumber * Math.Min(4, TotalQuestions) - 1) / TotalQuestions + 1);
    public bool IsTieBreaker { get; private set; }
    public bool ContentExhausted { get; private set; }
    public IReadOnlyList<PlayerId> Eligible => Array.AsReadOnly(_eligible.ToArray());
    public IReadOnlyList<PlayerId> Winners => Array.AsReadOnly(_winners.ToArray());
    public IReadOnlyList<PlayerStatistics> Statistics => Array.AsReadOnly(_stats.Values.ToArray());
    public GameSnapshot Snapshot => _game.GetSnapshot();

    public FullMatch(IEnumerable<Player> players, IGameClock clock, IRandomSource random,
        IEnumerable<QuestionDefinition> questions, MatchSettings settings,
        IReadOnlyCollection<string>? categories = null, Func<QuestionInstanceId>? nextInstance = null, Func<Guid>? nextCard = null,
        TeamRoster? teams = null, Func<Guid>? nextPause = null)
    {
        ArgumentNullException.ThrowIfNull(settings);
        _settings = settings;
        _deck = new(questions, random, categories, settings.Difficulties);
        if (_deck.Remaining < Math.Max(1, settings.QuestionCount)) throw new ArgumentException("Insufficient unique questions.", nameof(questions));
        _nextInstance = nextInstance ?? (() => new(Guid.NewGuid()));
        _nextPause = nextPause ?? Guid.NewGuid;
        _wallClock = clock;
        _clock = new(clock);
        var roster = players.ToArray();
        _teams = teams;
        teams?.ValidateRoster(roster.Select(p => p.Id));
        _connected = roster.Select(p => p.Id).ToHashSet();
        _strategy = settings.Strategy is null ? null : new StrategySession(roster.Select(p => p.Id), random, _deck.Upcoming(settings.Unlimited ? _deck.Remaining : settings.QuestionCount), settings.Strategy, nextCard);
        _game = new(GameAuthority.Host, roster, _clock, random, strategy: _strategy, scaleDifficulty: true);
        _eligible = Snapshot.Scores.Select(s => s.PlayerId).ToArray();
        _stats = _eligible.ToDictionary(id => id, id => new PlayerStatistics(id, 0, 0, 0, 0, 0, 0));
        _streaks = _eligible.ToDictionary(id => id, _ => 0);
        Require(_game.Initialize()); Require(_game.OpenLobby()); Require(_game.StartGame()); Require(_game.BeginRound());
        BeginQuestion();
    }

    public SubmissionError Submit(AnswerSubmission answer, TimeSpan hostReceivedAt)
    {
        if (!_connected.Contains(answer.PlayerId)) return SubmissionError.UnknownPlayer;
        if (IsPaused) return SubmissionError.InvalidState;
        var error = _game.SubmitAnswer(answer, _clock.At(hostReceivedAt));
        if (error == SubmissionError.None) Revision++;
        return error;
    }

    public void Disconnect(PlayerId player)
    {
        if (!_connected.Remove(player)) return;
        if (Snapshot.Phase == GamePhase.GameOver) return;
        _clock.Pause(); _resumeAt = null; _resumeVotes.Clear(); PauseId = _nextPause();
        _game.Disconnect(player);
        _continueVotes.Remove(player); _endVotes.Remove(player);
        Revision++;
    }
    public void Reconnect(PlayerId player)
    {
        if (!_stats.ContainsKey(player) || !_connected.Add(player)) return;
        if (Snapshot.Phase == GamePhase.GameOver) return;
        _game.Reconnect(player);
        if (IsPaused && _stats.Keys.All(_connected.Contains)) _resumeAt = _wallClock.Now + TimeSpan.FromSeconds(5);
        Revision++;
    }
    public GameError ResumeVote(PlayerId player, Guid pauseId)
    {
        if (!IsPaused || pauseId == Guid.Empty || PauseId != pauseId || !_connected.Contains(player) || IsCountingDown) return GameError.InvalidTransition;
        if (_resumeVotes.Add(player)) Revision++;
        if (_connected.Count > 0 && _connected.All(_resumeVotes.Contains)) Resume();
        return GameError.None;
    }
    public GameError Resume()
    {
        if (!IsPaused) return GameError.InvalidTransition;
        _clock.Resume(); _resumeAt = null; _resumeVotes.Clear(); PauseId = Guid.Empty; Revision++;
        TryConsensus();
        return GameError.None;
    }
    public IReadOnlyList<PlayerId> AnsweredPlayers => _game.AnsweredPlayers;
    public IReadOnlyList<PlayerId> ContinueVotes => _continueVotes.ToArray();
    public IReadOnlyList<PlayerId> EndVotes => _endVotes.ToArray();
    private readonly HashSet<PlayerId> _continueVotes = [];
    private readonly HashSet<PlayerId> _endVotes = [];
    private int RemainingNormal => _settings.Unlimited ? _deck.Remaining : TotalQuestions - QuestionNumber;
    public GameError Vote(PlayerId player, QuestionInstanceId question, GamePhase phase, bool endGame)
    {
        if (IsPaused || !_connected.Contains(player) || Snapshot.Question?.InstanceId != question || Snapshot.Phase != phase ||
            (endGame ? !_settings.Unlimited || phase != GamePhase.Scoreboard : phase is not (GamePhase.AnswerReveal or GamePhase.Scoreboard or GamePhase.RoundEnd)))
            return GameError.InvalidTransition;
        if ((endGame ? _endVotes : _continueVotes).Add(player)) Revision++;
        TryConsensus();
        return GameError.None;
    }
    private void TryConsensus()
    {
        if (_connected.Count == 0) return;
        if (_connected.All(_endVotes.Contains)) EndUnlimited();
        else if (_connected.All(_continueVotes.Contains)) Advance();
    }
    public GameError EndUnlimited()
    {
        if (IsPaused || !_settings.Unlimited || Snapshot.Phase != GamePhase.Scoreboard) return GameError.InvalidTransition;
        FinishNow(); Revision++; ClearVotes(); return GameError.None;
    }
    private void ClearVotes() { _continueVotes.Clear(); _endVotes.Clear(); }
    private void FinishNow()
    {
        if (_strategy is not null && !_strategy.BonusesApplied) _game.ApplyBonuses(_strategy.ApplyBonuses());
        var scores = Snapshot.Scores;
        _eligible = _teams is null ? scores.Where(s => s.Total == scores.Max(p => p.Total)).Select(s => s.PlayerId).ToArray()
            : _teams.PlayersIn(TeamScores.Where(t => t.Total == TeamScores.Max(p => p.Total)).Select(t => t.TeamId)).ToArray();
        _winners = _eligible.ToArray();
        _winningTeams = _teams is null ? [] : _eligible.Select(_teams.TeamOf).Distinct().Order().ToArray();
        ContentExhausted = _deck.Remaining == 0 && (_teams is null ? _winners.Length > 1 : _winningTeams.Length > 1);
        Require(_game.EndRound()); Require(_game.FinishGame()); _strategy?.EndGame();
    }
    public StrategyPrivate? Private(PlayerId player) => _strategy is null ? null : _strategy.Private(player, _game.Deadline(player),
        !IsTieBreaker && !_selectionSwapped && Snapshot.Phase is GamePhase.Scoreboard or GamePhase.RoundEnd ?
            Array.AsReadOnly(_swapCategories ??= _deck.SwapCategories(RemainingNormal, _strategy.MissionsPossible).Take(3).ToArray()) : Array.AsReadOnly(Array.Empty<string>()));

    public CardError Activate(CardIntent intent, TimeSpan receivedAt)
    {
        if (_strategy?.Rules.Cards != true || IsTieBreaker) return CardError.Disabled;
        if (!_connected.Contains(intent.Player) || !_eligible.Contains(intent.Player)) return CardError.UnknownPlayer;
        if (IsPaused) return CardError.InvalidWindow;
        receivedAt = _clock.At(receivedAt);
        if (Snapshot.Question?.InstanceId != intent.Question) return CardError.StaleQuestion;
        var card = _strategy.FindCard(intent.Player, intent.CardId);
        if (card is null) return CardError.UnknownCard;
        var active = _game.Phase == GamePhase.QuestionActive;
        var recap = _game.Phase is GamePhase.Scoreboard or GamePhase.RoundEnd;
        if (!active && !recap) return CardError.InvalidWindow;
        if (receivedAt > _clock.Now || receivedAt < Snapshot.Question.StartedAt) return CardError.InvalidReceiveTime;
        if (active && _game.HasAnswered(intent.Player)) return CardError.AlreadyAnswered;
        if (active && receivedAt > _game.Deadline(intent.Player)) return CardError.Late;
        if (card.Kind != CardKind.Steal && intent.Target is not null) return CardError.InvalidTarget;
        if (card.Kind != CardKind.CategorySwap && !string.IsNullOrEmpty(intent.Category)) return CardError.InvalidCategory;
        CardError error;
        switch (card.Kind)
        {
            case CardKind.DoublePoints:
                if (recap && RemainingNormal <= 0) return CardError.NoUpcomingQuestion;
                if (_strategy.HasDouble(intent.Player, active)) return CardError.EffectActive;
                _strategy.SetDouble(intent.Player, active); error = CardError.None; break;
            case CardKind.FiftyFifty:
                if (!active) return CardError.InvalidWindow;
                if (Private(intent.Player)!.HiddenAnswers.Count != 0) return CardError.EffectActive;
                _strategy.SetHidden(intent.Player, _game.HideWrongAnswers()); error = CardError.None; break;
            case CardKind.ExtraTime:
                if (!active || _settings.QuestionDuration == TimeSpan.Zero) return CardError.InvalidWindow;
                if (_strategy.ExtraUsed(intent.Player)) return CardError.EffectActive;
                if (receivedAt > Snapshot.Question.Deadline - TimeSpan.FromSeconds(StrategyRules.ExtraCutoffSeconds)) return CardError.Late;
                _game.ExtendDeadline(intent.Player); _strategy.SetExtra(intent.Player); error = CardError.None; break;
            case CardKind.CategorySwap:
                if (!recap) return CardError.InvalidWindow;
                if (RemainingNormal <= 0) return CardError.NoUpcomingQuestion;
                if (_selectionSwapped) return CardError.EffectActive;
                if (intent.Category is not { Length: > 0 and <= 128 } || !Private(intent.Player)!.SwapCategories.Contains(intent.Category) ||
                    !_deck.SwapNext(intent.Category, RemainingNormal, _strategy.MissionsPossible)) return CardError.InvalidCategory;
                _selectionSwapped = true; error = CardError.None; break;
            case CardKind.Shield:
                if (!_strategy.Rules.AllowSteal) return CardError.Disabled;
                if (_strategy.HasShield(intent.Player)) return CardError.EffectActive;
                _strategy.SetShield(intent.Player); error = CardError.None; break;
            case CardKind.Steal:
                error = Steal(intent, recap); break;
            default: return CardError.UnknownCard;
        }
        if (error == CardError.None)
        {
            _strategy.Consume(intent.Player, intent.CardId);
            if (card.Kind != CardKind.Steal) _strategy.Notice(intent.Player, card.Kind.ToString());
            Revision++;
        }
        return error;
    }

    private CardError Steal(CardIntent intent, bool recap)
    {
        if (_strategy?.Rules.AllowSteal != true) return CardError.Disabled;
        if (!recap) return CardError.InvalidWindow;
        if (intent.Target is not { } target || target == intent.Player || !_connected.Contains(target)) return CardError.InvalidTarget;
        if (_teams is not null && _teams.TeamOf(target) == _teams.TeamOf(intent.Player)) return CardError.InvalidTarget;
        if (_strategy.WasTargeted(target)) return CardError.AlreadyTargeted;
        if (Snapshot.Scores.Single(p => p.PlayerId == target).Total == 0) return CardError.NoEffect;
        if (_strategy.BlockSteal(target)) _strategy.Notice(intent.Player, "StealBlocked");
        else { _game.Transfer(intent.Player, target); _strategy.Notice(target, "StealLost"); _strategy.Notice(intent.Player, "Steal"); }
        return CardError.None;
    }

    public bool Poll()
    {
        if (IsPaused)
        {
            if (_resumeAt is not { } at || _wallClock.Now < at) return false;
            Resume(); return true;
        }
        if (_game.Phase == GamePhase.QuestionActive)
        {
            if (_game.CloseQuestion() != GameError.None) return false;
            _missingAtClose.UnionWith(_stats.Keys.Where(player => !_connected.Contains(player)));
        }
        else if (_game.Phase == GamePhase.QuestionLocked)
        {
            Require(_game.RevealAnswer());
            foreach (var result in Snapshot.Reveal!.Players.Where(p => _eligible.Contains(p.PlayerId)))
            {
                var old = _stats[result.PlayerId];
                var streak = result.IsCorrect ? _streaks[result.PlayerId] + 1 : 0;
                _streaks[result.PlayerId] = streak;
                _stats[result.PlayerId] = old with
                {
                    Correct = old.Correct + (result.IsCorrect ? 1 : 0),
                    Wrong = old.Wrong + (!result.IsCorrect && (result.AnswerIndex is not null || _missingAtClose.Contains(result.PlayerId)) ? 1 : 0),
                    Unanswered = old.Unanswered + (result.AnswerIndex is null && !_missingAtClose.Contains(result.PlayerId) ? 1 : 0),
                    BestStreak = Math.Max(old.BestStreak, streak),
                    ResponseTicks = checked(old.ResponseTicks + (result.ResponseTime?.Ticks ?? 0)),
                    Responses = old.Responses + (result.ResponseTime is null ? 0 : 1)
                };
            }
        }
        else return false;
        Revision++;
        return true;
    }

    public GameError Advance()
    {
        if (IsPaused) return GameError.InvalidTransition;
        if (_game.Phase == GamePhase.AnswerReveal) Require(_game.ShowScoreboard());
        else if (_game.Phase == GamePhase.RoundEnd) { Require(_game.BeginRound()); BeginQuestion(); }
        else if (_game.Phase == GamePhase.Scoreboard)
        {
            if (_settings.Unlimited)
            { if (_deck.Remaining == 0) FinishNow(); else BeginQuestion(); }
            else if (!IsTieBreaker && QuestionNumber < TotalQuestions)
            {
                var round = RoundNumber;
                var nextRound = ((QuestionNumber + 1) * Math.Min(4, TotalQuestions) - 1) / TotalQuestions + 1;
                if (nextRound != round) Require(_game.EndRound());
                else BeginQuestion();
            }
            else ResolveEnd();
        }
        else return GameError.InvalidTransition;
        ClearVotes();
        Revision++;
        return GameError.None;
    }

    private void ResolveEnd()
    {
        if (!IsTieBreaker)
        {
            if (_strategy is not null && !_strategy.BonusesApplied) _game.ApplyBonuses(_strategy.ApplyBonuses());
            if (_teams is null)
            {
                var top = Snapshot.Scores.Max(s => s.Total);
                _eligible = Snapshot.Scores.Where(s => s.Total == top).Select(s => s.PlayerId).ToArray();
            }
            else
            {
                var scores = TeamScores; var top = scores.Max(s => s.Total);
                _eligible = _teams.PlayersIn(scores.Where(s => s.Total == top).Select(s => s.TeamId)).ToArray();
            }
        }
        else
        {
            var correct = Snapshot.Reveal!.Players.Where(p => _eligible.Contains(p.PlayerId) && p.IsCorrect).ToArray();
            if (correct.Length > 0)
            {
                var fastest = correct.Min(p => p.ResponseTime!.Value);
                var fastestPlayers = correct.Where(p => p.ResponseTime == fastest).Select(p => p.PlayerId).ToArray();
                _eligible = _teams is null ? fastestPlayers : _teams.PlayersIn(fastestPlayers.Select(_teams.TeamOf)).ToArray();
            }
        }
        var finalistCount = _teams is null ? _eligible.Length : _eligible.Select(_teams.TeamOf).Distinct().Count();
        if (finalistCount == 1 || _deck.Remaining == 0)
        {
            _winners = _eligible.ToArray();
            _winningTeams = _teams is null ? [] : _eligible.Select(_teams.TeamOf).Distinct().Order().ToArray();
            ContentExhausted = finalistCount > 1;
            Require(_game.EndRound()); Require(_game.FinishGame());
            _strategy?.EndGame();
        }
        else { IsTieBreaker = true; Require(_game.EndRound()); }
    }

    private void BeginQuestion()
    {
        var question = _deck.Draw() ?? throw new InvalidOperationException("Question deck exhausted.");
        Require(_game.StartQuestion(question, _nextInstance(), _settings.QuestionDuration, _eligible, !IsTieBreaker, _settings.QuestionDuration == TimeSpan.Zero));
        _missingAtClose.Clear();
        foreach (var player in _stats.Keys.Where(player => !_connected.Contains(player))) _game.Disconnect(player);
        QuestionNumber++;
        _selectionSwapped = false;
        _swapCategories = null;
    }

    private static void Require(GameError error)
    { if (error != GameError.None) throw new InvalidOperationException($"Unexpected match transition: {error}"); }
}

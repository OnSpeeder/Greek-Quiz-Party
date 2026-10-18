using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;

namespace QuizParty.Core.Game;

public sealed record MatchSettings
{
    public int QuestionCount { get; }
    public TimeSpan QuestionDuration { get; }
    public StrategyRules? Strategy { get; }
    public MatchSettings(int questionCount = 20, int questionSeconds = 20, StrategyRules? strategy = null)
    {
        // One question remains an explicit content preview, not a full-game preset.
        if (questionCount is not (1 or 10 or 20 or 30)) throw new ArgumentOutOfRangeException(nameof(questionCount));
        if (questionSeconds is < 5 or > 60) throw new ArgumentOutOfRangeException(nameof(questionSeconds));
        QuestionCount = questionCount;
        QuestionDuration = TimeSpan.FromSeconds(questionSeconds);
        Strategy = strategy;
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
    private readonly Dictionary<PlayerId, PlayerStatistics> _stats;
    private readonly Dictionary<PlayerId, int> _streaks;
    private PlayerId[] _eligible;
    private PlayerId[] _winners = [];
    private readonly StrategySession? _strategy;
    private readonly IGameClock _clock;
    private readonly HashSet<PlayerId> _connected;
    private bool _selectionSwapped;
    private string[]? _swapCategories;
    public StrategyRules? Strategy => _settings.Strategy;
    public IReadOnlyList<StrategyFinal> FinalStrategy => Snapshot.Phase == GamePhase.GameOver ? _strategy?.Final() ?? [] : [];
    public long Revision { get; private set; } = 1;
    public int QuestionNumber { get; private set; }
    public int TotalQuestions => _settings.QuestionCount;
    public int RoundNumber => IsTieBreaker ? Math.Min(4, TotalQuestions) + 1 :
        Math.Min(Math.Min(4, TotalQuestions), (QuestionNumber * Math.Min(4, TotalQuestions) - 1) / TotalQuestions + 1);
    public bool IsTieBreaker { get; private set; }
    public bool ContentExhausted { get; private set; }
    public IReadOnlyList<PlayerId> Eligible => Array.AsReadOnly(_eligible.ToArray());
    public IReadOnlyList<PlayerId> Winners => Array.AsReadOnly(_winners.ToArray());
    public IReadOnlyList<PlayerStatistics> Statistics => Array.AsReadOnly(_stats.Values.ToArray());
    public GameSnapshot Snapshot => _game.GetSnapshot();

    public FullMatch(IEnumerable<Player> players, IGameClock clock, IRandomSource random,
        IEnumerable<QuestionDefinition> questions, MatchSettings settings,
        IReadOnlyCollection<string>? categories = null, Func<QuestionInstanceId>? nextInstance = null, Func<Guid>? nextCard = null)
    {
        ArgumentNullException.ThrowIfNull(settings);
        _settings = settings;
        _deck = new(questions, random, categories);
        if (_deck.Remaining < settings.QuestionCount) throw new ArgumentException("Insufficient unique questions.", nameof(questions));
        _nextInstance = nextInstance ?? (() => new(Guid.NewGuid()));
        _clock = clock;
        var roster = players.ToArray();
        _connected = roster.Select(p => p.Id).ToHashSet();
        _strategy = settings.Strategy is null ? null : new StrategySession(roster.Select(p => p.Id), random, _deck.Upcoming(settings.QuestionCount), settings.Strategy, nextCard);
        _game = new(GameAuthority.Host, roster, clock, random, strategy: _strategy);
        _eligible = Snapshot.Scores.Select(s => s.PlayerId).ToArray();
        _stats = _eligible.ToDictionary(id => id, id => new PlayerStatistics(id, 0, 0, 0, 0, 0, 0));
        _streaks = _eligible.ToDictionary(id => id, _ => 0);
        Require(_game.Initialize()); Require(_game.OpenLobby()); Require(_game.StartGame()); Require(_game.BeginRound());
        BeginQuestion();
    }

    public SubmissionError Submit(AnswerSubmission answer, TimeSpan hostReceivedAt)
    {
        if (!_connected.Contains(answer.PlayerId)) return SubmissionError.UnknownPlayer;
        var error = _game.SubmitAnswer(answer, hostReceivedAt);
        if (error == SubmissionError.None) Revision++;
        return error;
    }

    public void Disconnect(PlayerId player) => _connected.Remove(player);
    public StrategyPrivate? Private(PlayerId player) => _strategy is null ? null : _strategy.Private(player, _game.Deadline(player),
        !IsTieBreaker && !_selectionSwapped && Snapshot.Phase is GamePhase.Scoreboard or GamePhase.RoundEnd ?
            Array.AsReadOnly(_swapCategories ??= _deck.SwapCategories(TotalQuestions - QuestionNumber, _strategy.MissionsPossible).Take(3).ToArray()) : Array.AsReadOnly(Array.Empty<string>()));

    public CardError Activate(CardIntent intent, TimeSpan receivedAt)
    {
        if (_strategy?.Rules.Cards != true || IsTieBreaker) return CardError.Disabled;
        if (!_connected.Contains(intent.Player) || !_eligible.Contains(intent.Player)) return CardError.UnknownPlayer;
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
                if (recap && QuestionNumber >= TotalQuestions) return CardError.NoUpcomingQuestion;
                if (_strategy.HasDouble(intent.Player, active)) return CardError.EffectActive;
                _strategy.SetDouble(intent.Player, active); error = CardError.None; break;
            case CardKind.FiftyFifty:
                if (!active) return CardError.InvalidWindow;
                if (Private(intent.Player)!.HiddenAnswers.Count != 0) return CardError.EffectActive;
                _strategy.SetHidden(intent.Player, _game.HideWrongAnswers()); error = CardError.None; break;
            case CardKind.ExtraTime:
                if (!active) return CardError.InvalidWindow;
                if (_strategy.ExtraUsed(intent.Player)) return CardError.EffectActive;
                if (receivedAt > Snapshot.Question.Deadline - TimeSpan.FromSeconds(StrategyRules.ExtraCutoffSeconds)) return CardError.Late;
                _game.ExtendDeadline(intent.Player); _strategy.SetExtra(intent.Player); error = CardError.None; break;
            case CardKind.CategorySwap:
                if (!recap) return CardError.InvalidWindow;
                if (QuestionNumber >= TotalQuestions) return CardError.NoUpcomingQuestion;
                if (_selectionSwapped) return CardError.EffectActive;
                if (intent.Category is not { Length: > 0 and <= 128 } || !Private(intent.Player)!.SwapCategories.Contains(intent.Category) ||
                    !_deck.SwapNext(intent.Category, TotalQuestions - QuestionNumber, _strategy.MissionsPossible)) return CardError.InvalidCategory;
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
        if (_strategy.WasTargeted(target)) return CardError.AlreadyTargeted;
        if (Snapshot.Scores.Single(p => p.PlayerId == target).Total == 0) return CardError.NoEffect;
        if (_strategy.BlockSteal(target)) _strategy.Notice(intent.Player, "StealBlocked");
        else { _game.Transfer(intent.Player, target); _strategy.Notice(target, "StealLost"); _strategy.Notice(intent.Player, "Steal"); }
        return CardError.None;
    }

    public bool Poll()
    {
        if (_game.Phase == GamePhase.QuestionActive)
        { if (_game.CloseQuestion() != GameError.None) return false; }
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
                    Wrong = old.Wrong + (result.AnswerIndex is not null && !result.IsCorrect ? 1 : 0),
                    Unanswered = old.Unanswered + (result.AnswerIndex is null ? 1 : 0),
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
        if (_game.Phase == GamePhase.AnswerReveal) Require(_game.ShowScoreboard());
        else if (_game.Phase == GamePhase.RoundEnd) { Require(_game.BeginRound()); BeginQuestion(); }
        else if (_game.Phase == GamePhase.Scoreboard)
        {
            if (!IsTieBreaker && QuestionNumber < TotalQuestions)
            {
                var round = RoundNumber;
                var nextRound = ((QuestionNumber + 1) * Math.Min(4, TotalQuestions) - 1) / TotalQuestions + 1;
                if (nextRound != round) Require(_game.EndRound());
                else BeginQuestion();
            }
            else ResolveEnd();
        }
        else return GameError.InvalidTransition;
        Revision++;
        return GameError.None;
    }

    private void ResolveEnd()
    {
        if (!IsTieBreaker)
        {
            if (_strategy is not null && !_strategy.BonusesApplied) _game.ApplyBonuses(_strategy.ApplyBonuses());
            var top = Snapshot.Scores.Max(s => s.Total);
            _eligible = Snapshot.Scores.Where(s => s.Total == top).Select(s => s.PlayerId).ToArray();
        }
        else
        {
            var correct = Snapshot.Reveal!.Players.Where(p => _eligible.Contains(p.PlayerId) && p.IsCorrect).ToArray();
            if (correct.Length > 0)
            {
                var fastest = correct.Min(p => p.ResponseTime!.Value);
                _eligible = correct.Where(p => p.ResponseTime == fastest).Select(p => p.PlayerId).ToArray();
            }
        }
        if (_eligible.Length == 1 || _deck.Remaining == 0)
        {
            _winners = _eligible.ToArray();
            ContentExhausted = _eligible.Length > 1;
            Require(_game.EndRound()); Require(_game.FinishGame());
            _strategy?.EndGame();
        }
        else { IsTieBreaker = true; Require(_game.EndRound()); }
    }

    private void BeginQuestion()
    {
        var question = _deck.Draw() ?? throw new InvalidOperationException("Question deck exhausted.");
        Require(_game.StartQuestion(question, _nextInstance(), _settings.QuestionDuration, _eligible, !IsTieBreaker));
        QuestionNumber++;
        _selectionSwapped = false;
        _swapCategories = null;
    }

    private static void Require(GameError error)
    { if (error != GameError.None) throw new InvalidOperationException($"Unexpected match transition: {error}"); }
}

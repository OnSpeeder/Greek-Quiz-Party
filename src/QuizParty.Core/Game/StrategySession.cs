using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;

namespace QuizParty.Core.Game;

public enum CardKind { DoublePoints, FiftyFifty, ExtraTime, CategorySwap, Shield, Steal }
public enum MissionKind { Historian, HotStreak, Gambler, Speedster, Generalist }
public enum CardError { None, Disabled, UnknownPlayer, UnknownCard, StaleQuestion, InvalidWindow, AlreadyAnswered,
    Late, InvalidReceiveTime, EffectActive, InvalidTarget, AlreadyTargeted, NoEffect, InvalidCategory, NoUpcomingQuestion }
public sealed record CardInstance(Guid Id, CardKind Kind);
public sealed record CardIntent(PlayerId Player, QuestionInstanceId Question, Guid CardId, PlayerId? Target = null, string? Category = null);
public sealed record MissionView(MissionKind Kind, int Target, int Progress, bool Complete);
public sealed record StrategyPrivate(PlayerId Player, IReadOnlyList<CardInstance> Hand, IReadOnlyList<int> HiddenAnswers,
    TimeSpan Deadline, bool Shield, bool DoublePoints, int Streak, int Meter, MissionView? Mission,
    IReadOnlyList<string> SwapCategories, string Notice);
public sealed record StrategyFinal(PlayerId Player, MissionView? Mission, int MissionBonus, int CardsUsed,
    int ConfidentCorrect, int ConfidentWrong, int AllInCorrect, int AllInWrong);

/// <summary>Explicit initial balance; immutable settings, all randomness remains host-owned.</summary>
public sealed record StrategyRules(bool Confidence = true, bool Streaks = true, bool Cards = true,
    bool Missions = true, bool AllowSteal = false)
{
    // Copy caller collections so a running match cannot be changed from its setup UI.
    private IReadOnlyList<CardKind>? _enabledCards;
    private IReadOnlyList<MissionKind>? _enabledMissions;
    public IReadOnlyList<CardKind>? EnabledCards
    {
        get => _enabledCards;
        init => _enabledCards = value is null ? null : Array.AsReadOnly(value.Distinct().Select(k =>
            Enum.IsDefined(k) ? k : throw new ArgumentException("Unknown card.")).ToArray());
    }
    public IReadOnlyList<MissionKind>? EnabledMissions
    {
        get => _enabledMissions;
        init => _enabledMissions = value is null ? null : Array.AsReadOnly(value.Distinct().Select(k =>
            Enum.IsDefined(k) ? k : throw new ArgumentException("Unknown mission.")).ToArray());
    }
    public const int ConfidentPenalty = 250, AllInPenalty = 500, MaxMultiplier = 6;
    public const int MeterThreshold = 100, CorrectMeter = 20, DifficultyMeter = 5, StreakMeter = 10, HandLimit = 2;
    public const int ExtraSeconds = 5, ExtraCutoffSeconds = 3, StealPoints = 100, MissionBonus = 500;
}

/// <summary>Host-only personal state. Never serialize this object as a public snapshot.</summary>
public sealed class StrategySession
{
    private readonly Dictionary<PlayerId, PersonalState> _players;
    private readonly IRandomSource _random;
    private readonly Func<Guid> _newCard;
    private readonly HashSet<Guid> _usedCardIds = new();
    private readonly HashSet<PlayerId> _targeted = new();
    public StrategyRules Rules { get; }
    public bool BonusesApplied { get; private set; }

    public StrategySession(IEnumerable<PlayerId> players, IRandomSource random, IReadOnlyList<QuestionDefinition> normalQuestions,
        StrategyRules rules, Func<Guid>? newCard = null)
    {
        Rules = rules; _random = random; _newCard = newCard ?? Guid.NewGuid;
        _players = players.ToDictionary(id => id, _ => new PersonalState());
        var pool = new List<MissionKind>();
        if (normalQuestions.Count(q => q.CategoryId == "history") >= 3) pool.Add(MissionKind.Historian);
        if (rules.Streaks && normalQuestions.Count >= 4) pool.Add(MissionKind.HotStreak);
        if (rules.Confidence && normalQuestions.Count >= 2) pool.Add(MissionKind.Gambler);
        if (normalQuestions.Count >= 3) pool.Add(MissionKind.Speedster);
        if (normalQuestions.Select(q => q.CategoryId).Distinct().Count() >= 5) pool.Add(MissionKind.Generalist);
        pool.RemoveAll(kind => rules.EnabledMissions is not null && !rules.EnabledMissions.Contains(kind));
        if (rules.Missions && pool.Count > 0)
            foreach (var player in _players.Values) player.Mission = pool[Next(pool.Count)];
    }

    public void BeginQuestion()
    {
        foreach (var player in _players.Values)
        {
            player.Hidden.Clear(); player.ExtraUsed = false;
            player.DoubleCurrent = player.DoubleNext; player.DoubleNext = false; player.Notice = "None";
        }
    }

    public int Delta(PlayerId id, bool correct, int raw, ConfidenceLevel confidence, long total)
    {
        if (!correct)
        {
            var penalty = confidence switch { ConfidenceLevel.Confident => StrategyRules.ConfidentPenalty, ConfidenceLevel.AllIn => StrategyRules.AllInPenalty, _ => 0 };
            return -(int)Math.Min(total, penalty);
        }
        var player = _players[id];
        var streak = Rules.Streaks ? player.Streak + 1 : 0;
        var percentage = streak >= 5 ? 115 : streak >= 3 ? 110 : 100;
        var multiplier = Math.Min(StrategyRules.MaxMultiplier * 100, (int)confidence * (player.DoubleCurrent ? 2 : 1) * percentage);
        return checked((int)decimal.Round((decimal)raw * multiplier / 100, 0, MidpointRounding.AwayFromZero));
    }

    public void RecordResults(string category, int difficulty, IReadOnlyList<PlayerQuestionResult> results)
    {
        var correctTimes = results.Where(r => r.IsCorrect && r.ResponseTime is not null).Select(r => r.ResponseTime!.Value).ToArray();
        var fastest = correctTimes.Length == 0 ? TimeSpan.MaxValue : correctTimes.Min();
        foreach (var result in results)
        {
            var state = _players[result.PlayerId];
            if (result.AnswerIndex is not null)
            {
                if (result.Confidence == ConfidenceLevel.Confident) { if (result.IsCorrect) state.X2Correct++; else state.X2Wrong++; }
                if (result.Confidence == ConfidenceLevel.AllIn) { if (result.IsCorrect) state.X3Correct++; else state.X3Wrong++; }
            }
            state.Streak = result.IsCorrect ? state.Streak + 1 : 0;
            if (result.IsCorrect)
            {
                state.Categories.Add(category);
                if (state.Mission == MissionKind.Historian && category == "history") state.Progress++;
                if (state.Mission == MissionKind.Gambler && result.Confidence == ConfidenceLevel.AllIn) state.Progress++;
                if (state.Mission == MissionKind.Speedster && result.ResponseTime == fastest) state.Progress++;
                if (Rules.Cards)
                {
                    state.Meter += StrategyRules.CorrectMeter + StrategyRules.DifficultyMeter * difficulty + (state.Streak >= 5 && Rules.Streaks ? StrategyRules.StreakMeter : 0);
                    if (state.Meter >= StrategyRules.MeterThreshold) { state.Meter -= StrategyRules.MeterThreshold; Award(result.PlayerId); }
                    if (state.Streak == 7 && Rules.Streaks) Award(result.PlayerId);
                }
            }
            if (state.Mission == MissionKind.HotStreak) state.Progress = Math.Max(state.Progress, state.Streak);
            if (state.Mission == MissionKind.Generalist) state.Progress = state.Categories.Count;
            if (state.Mission is { } kind) state.Progress = Math.Min(Target(kind), state.Progress);
        }
    }

    private void Award(PlayerId id)
    {
        var state = _players[id];
        if (state.Hand.Count >= StrategyRules.HandLimit) return;
        CardKind[] pool = Rules.AllowSteal ? Enum.GetValues<CardKind>() : [CardKind.DoublePoints, CardKind.FiftyFifty, CardKind.ExtraTime, CardKind.CategorySwap];
        pool = pool.Where(kind => Rules.EnabledCards is null || Rules.EnabledCards.Contains(kind)).ToArray();
        if (pool.Length == 0) return;
        var kind = pool[Next(pool.Length)];
        var cardId = _newCard();
        if (cardId == Guid.Empty || !_usedCardIds.Add(cardId)) throw new InvalidOperationException("Card instance IDs must be fresh and nonempty.");
        state.Hand.Add(new(cardId, kind));
    }

    public CardInstance? FindCard(PlayerId id, Guid card) => _players.GetValueOrDefault(id)?.Hand.FirstOrDefault(c => c.Id == card);
    public bool HasHidden(PlayerId id, int index) => _players[id].Hidden.Contains(index);
    public bool ExtraUsed(PlayerId id) => _players[id].ExtraUsed;
    public bool HasDouble(PlayerId id, bool active) => active ? _players[id].DoubleCurrent : _players[id].DoubleNext;
    public bool HasShield(PlayerId id) => _players[id].Shield;
    public bool WasTargeted(PlayerId id) => _targeted.Contains(id);
    public void SetHidden(PlayerId id, IEnumerable<int> hidden) => _players[id].Hidden.UnionWith(hidden);
    public void SetExtra(PlayerId id) => _players[id].ExtraUsed = true;
    public void SetDouble(PlayerId id, bool active) { if (active) _players[id].DoubleCurrent = true; else _players[id].DoubleNext = true; }
    public void SetShield(PlayerId id) => _players[id].Shield = true;
    public bool BlockSteal(PlayerId target)
    {
        _targeted.Add(target);
        if (!_players[target].Shield) return false;
        _players[target].Shield = false; _players[target].Notice = "ShieldBlocked";
        return true;
    }
    public void Notice(PlayerId id, string notice) => _players[id].Notice = notice;
    public void Consume(PlayerId id, Guid card)
    {
        _players[id].Hand.RemoveAll(c => c.Id == card); _players[id].CardsUsed++;
    }

    public StrategyPrivate Private(PlayerId id, TimeSpan deadline, IReadOnlyList<string> swapCategories)
    {
        var player = _players[id];
        return new(id, Array.AsReadOnly(player.Hand.ToArray()), Array.AsReadOnly(player.Hidden.Order().ToArray()), deadline,
            player.Shield, player.DoubleCurrent || player.DoubleNext, player.Streak, player.Meter, Mission(player), swapCategories, player.Notice);
    }
    public IReadOnlyList<StrategyFinal> Final() => Array.AsReadOnly(_players.Select(p => new StrategyFinal(p.Key, Mission(p.Value),
        BonusesApplied && Mission(p.Value)?.Complete == true ? StrategyRules.MissionBonus : 0,
        p.Value.CardsUsed, p.Value.X2Correct, p.Value.X2Wrong, p.Value.X3Correct, p.Value.X3Wrong)).ToArray());
    public IReadOnlyDictionary<PlayerId, int> ApplyBonuses()
    {
        if (BonusesApplied) return new Dictionary<PlayerId, int>();
        BonusesApplied = true;
        return _players.Where(p => Mission(p.Value)?.Complete == true).ToDictionary(p => p.Key, _ => StrategyRules.MissionBonus);
    }
    public void EndGame() { foreach (var p in _players.Values) { p.Shield = false; p.DoubleCurrent = false; p.DoubleNext = false; } }

    public bool MissionsPossible(IReadOnlyList<QuestionDefinition> remaining)
    {
        foreach (var state in _players.Values)
        {
            if (state.Mission is not { } kind || state.Progress >= Target(kind)) continue;
            if (kind == MissionKind.Historian && state.Progress + remaining.Count(q => q.CategoryId == "history") < Target(kind)) return false;
            if (kind == MissionKind.Generalist && state.Categories.Union(remaining.Select(q => q.CategoryId)).Count() < Target(kind)) return false;
        }
        return true;
    }
    private static int Target(MissionKind kind) => kind switch { MissionKind.Historian or MissionKind.Speedster => 3, MissionKind.HotStreak => 4, MissionKind.Gambler => 2, _ => 5 };
    private static MissionView? Mission(PersonalState state) => state.Mission is { } kind ? new(kind, Target(kind), state.Progress, state.Progress >= Target(kind)) : null;
    private int Next(int bound)
    { var value = _random.Next(bound); return value >= 0 && value < bound ? value : throw new InvalidOperationException("Invalid random source."); }

    private sealed class PersonalState
    {
        public List<CardInstance> Hand { get; } = new();
        public HashSet<int> Hidden { get; } = new();
        public HashSet<string> Categories { get; } = new(StringComparer.Ordinal);
        public bool Shield, DoubleCurrent, DoubleNext, ExtraUsed;
        public int Streak, Meter, Progress, CardsUsed, X2Correct, X2Wrong, X3Correct, X3Wrong;
        public MissionKind? Mission;
        public string Notice = "None";
    }
}

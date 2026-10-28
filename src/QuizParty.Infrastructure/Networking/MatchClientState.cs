namespace QuizParty.Infrastructure.Networking;

/// <summary>Presentation state only. Never computes correctness, authoritative timing or points.</summary>
public sealed class MatchClientState
{
    private MatchSnapshotDto? _snapshot;
    private Guid? _pendingId;
    private int _pendingIndex;
    private Guid? _pendingCardMessage;
    private Guid _pendingCard;
    private readonly HashSet<Guid> _seenQuestions = new();
    private Guid _localPlayerId;
    public int? OwnAnswerIndex { get; private set; }
    public bool Pending => _pendingId is not null;
    public bool CardPending => _pendingCardMessage is not null;
    public string CardReason { get; private set; } = "None";
    public string LastReason { get; private set; } = "None";
    public MatchSnapshotDto? Snapshot => _snapshot is null ? null : Copy(_snapshot);

    public string? CreateAnswer(int index, int confidence = 1)
    {
        if (_snapshot?.Phase != "QuestionActive" || _snapshot.IsPaused || !_snapshot.EligiblePlayers.Contains(_localPlayerId) ||
            Pending || CardPending || OwnAnswerIndex is not null || _snapshot.AnsweredPlayers?.Contains(_localPlayerId) == true || index is < 0 or > 3 || confidence is < 1 or > 3 ||
            ((_snapshot.Strategy?.Confidence != true || _snapshot.IsTieBreaker) && confidence != 1) ||
            _snapshot.Private?.HiddenAnswers.Contains(index) == true) return null;
        _pendingId = Guid.NewGuid();
        _pendingIndex = index;
        return LobbyProtocol.Encode("SubmitAnswer", _snapshot.SessionId,
            new AnswerRequestDto(_snapshot.Question.InstanceId, index, confidence, _snapshot.LocalSlot), messageId: _pendingId);
    }

    public string? CreateCard(Guid card, Guid? target = null, string? category = null)
    {
        if (_snapshot?.Strategy?.Cards != true || _snapshot.IsPaused || _snapshot.IsTieBreaker || CardPending || Pending ||
            _snapshot.Phase is not ("QuestionActive" or "Scoreboard" or "RoundEnd") ||
            (_snapshot.Phase == "QuestionActive" && (OwnAnswerIndex is not null || _snapshot.AnsweredPlayers?.Contains(_localPlayerId) == true)) ||
            _snapshot.Private?.Hand.Any(c => c.Id == card) != true || category?.Length > 128) return null;
        _pendingCardMessage = Guid.NewGuid(); _pendingCard = card; CardReason = "Pending";
        return LobbyProtocol.Encode("ActivateCard", _snapshot.SessionId,
            new CardRequestDto(_snapshot.Question.InstanceId, card, target, category, _snapshot.LocalSlot), messageId: _pendingCardMessage);
    }

    public bool ApplyCardReceipt(LobbyEnvelope packet, Guid sessionId)
    {
        if (packet.SessionId != sessionId || _pendingCardMessage is null || packet.CorrelationId != _pendingCardMessage ||
            !LobbyProtocol.TryPayload<CardReceiptDto>(packet, out var receipt) || receipt is null || receipt.CardId != _pendingCard ||
            receipt.QuestionInstanceId != _snapshot?.Question.InstanceId || receipt.LocalSlot != _snapshot.LocalSlot) return false;
        _pendingCardMessage = null;
        CardReason = receipt.Accepted ? "None" : receipt.Reason is { Length: > 0 and <= 40 } ? receipt.Reason : "MalformedRequest";
        return true;
    }

    public bool ApplySnapshot(LobbyEnvelope packet, Guid sessionId, Guid localPlayerId)
    {
        if (packet.SessionId != sessionId || !LobbyProtocol.TryPayload<MatchSnapshotDto>(packet, out var next) ||
            !Valid(next, sessionId, localPlayerId) || next is null ||
            (_snapshot is not null && !Forward(_snapshot, next))) return false;
        if (_snapshot?.Question.InstanceId != next.Question.InstanceId)
        {
            if (!_seenQuestions.Add(next.Question.InstanceId)) return false;
            OwnAnswerIndex = null;
            _pendingId = null;
            _pendingCardMessage = null; CardReason = "None";
            LastReason = "None";
        }
        _snapshot = Copy(next);
        _localPlayerId = localPlayerId;
        return true;
    }

    public bool ApplyReceipt(LobbyEnvelope packet, Guid sessionId)
    {
        if (packet.SessionId != sessionId || _pendingId is null || packet.CorrelationId != _pendingId ||
            !LobbyProtocol.TryPayload<AnswerReceiptDto>(packet, out var receipt) || receipt is null ||
            receipt.QuestionInstanceId != _snapshot?.Question.InstanceId || receipt.LocalSlot != _snapshot.LocalSlot) return false;
        if (receipt.Accepted) OwnAnswerIndex = _pendingIndex;
        _pendingId = null;
        LastReason = receipt.Accepted ? "None" : receipt.Reason is { Length: > 0 and <= 40 } ? receipt.Reason : "MalformedRequest";
        return true;
    }

    private static int Rank(string phase) => phase switch
    {
        "QuestionActive" => 0, "QuestionLocked" => 1, "AnswerReveal" => 2, "Scoreboard" => 3,
        "RoundEnd" => 4, "GameOver" => 5, _ => -1
    };

    private static bool Forward(MatchSnapshotDto old, MatchSnapshotDto next)
    {
        if (next.Revision <= old.Revision || old.Phase == "GameOver" || next.TotalQuestions != old.TotalQuestions || next.Strategy != old.Strategy ||
            next.LocalSlot != old.LocalSlot || next.Scores.Any(s => old.Scores.FirstOrDefault(p => p.PlayerId == s.PlayerId)?.CharacterId != s.CharacterId) || !SameTeams(old.Teams, next.Teams) ||
            !old.Scores.Select(s => s.PlayerId).Order().SequenceEqual(next.Scores.Select(s => s.PlayerId).Order()) ||
            (next.Strategy is null && next.Scores.Any(s => s.Total < old.Scores.Single(p => p.PlayerId == s.PlayerId).Total)) ||
            (Rank(next.Phase) < 2 && next.Scores.Any(s => s.Total != old.Scores.Single(p => p.PlayerId == s.PlayerId).Total))) return false;
        if (next.QuestionNumber == old.QuestionNumber)
            return next.Question.InstanceId == old.Question.InstanceId && Rank(next.Phase) >= Rank(old.Phase);
        return next.QuestionNumber == old.QuestionNumber + 1 && Rank(old.Phase) >= 3 &&
            next.Phase == "QuestionActive" && next.Question.InstanceId != old.Question.InstanceId;
    }

    private static bool Valid(MatchSnapshotDto? next, Guid session, Guid localPlayer)
    {
        if (next is null || next.SessionId != session || next.Revision <= 0 || Rank(next.Phase) < 0 || next.HostNowTicks < 0 ||
            next.Question is not { } question || question.InstanceId == Guid.Empty || question.Text is not { Length: > 0 and <= 2048 } ||
            question.Answers is not { Length: 4 } answers || answers.Any(answer => string.IsNullOrWhiteSpace(answer) || answer.Length > 512) ||
            question.StartedAtTicks < 0 || question.DeadlineTicks <= question.StartedAtTicks ||
            (question.DeadlineTicks != long.MaxValue && question.DeadlineTicks - question.StartedAtTicks > 2 * TimeSpan.TicksPerMinute) ||
            next.Scores is not { Length: >= 1 and <= 8 } scores ||
            scores.Any(score => score is null || score.PlayerId == Guid.Empty || !LobbyProtocol.ValidName(score.DisplayName) || score.Total < 0 || score.CharacterId is { } character && !Core.Players.Characters.IsValid(character)) ||
            scores.Where(score => score.CharacterId is not null).Select(score => score.CharacterId).Distinct().Count() != scores.Count(score => score.CharacterId is not null) ||
            scores.Select(score => score.PlayerId).Distinct().Count() != scores.Length || !scores.Any(score => score.PlayerId == localPlayer) ||
            next.AcceptedAnswerCount < 0 || next.AcceptedAnswerCount > scores.Length ||
            question.CategoryId is not { Length: > 0 and <= 128 } || question.Difficulty is < 1 or > 5 ||
            next.TotalQuestions is not (0 or 1 or 10 or 20 or 30 or 40 or 50) || next.QuestionNumber < 1 ||
            next.RoundNumber is < 1 or > 5 || (next.IsTieBreaker != (next.TotalQuestions != 0 && next.QuestionNumber > next.TotalQuestions) && next.Phase != "RoundEnd") ||
            next.EligiblePlayers is not { Length: >= 1 and <= 8 } eligible || eligible.Distinct().Count() != eligible.Length ||
            eligible.Any(id => !scores.Any(s => s.PlayerId == id)) || next.Winners is not { Length: <= 8 } winners ||
            winners.Distinct().Count() != winners.Length || winners.Any(id => !eligible.Contains(id)) ||
            next.Statistics is not { Length: <= 8 } || next.LocalSlot is < 0 or > 7 || !ValidTeams(next) || !ValidStrategy(next, localPlayer) || !ValidVotes(next)) return false;
        if (next.Phase != "GameOver" && (winners.Length != 0 || next.Statistics.Length != 0 || next.ContentExhausted)) return false;
        if (next.Phase == "GameOver" && (winners.Length == 0 || next.Statistics.Length != scores.Length ||
            next.Statistics.Any(s => s is null || s.Correct < 0 || s.Wrong < 0 || s.Unanswered < 0 || s.BestStreak < 0 ||
                (long)s.Correct + s.Wrong + s.Unanswered > next.QuestionNumber || s.BestStreak > s.Correct ||
                (s.Responses < s.Correct || s.Responses > (long)s.Correct + s.Wrong) || s.ResponseTicks < 0 || (question.DeadlineTicks != long.MaxValue && s.ResponseTicks > (long)s.Responses * TimeSpan.TicksPerSecond * (next.Strategy is null ? 120 : 125))) ||
            !next.Statistics.Select(s => s.PlayerId).Order().SequenceEqual(scores.Select(s => s.PlayerId).Order()))) return false;
        if (Rank(next.Phase) < 2) return next.Reveal is null;
        var reveal = next.Reveal;
        return reveal is not null && reveal.CorrectAnswerIndex is >= 0 and <= 3 &&
            reveal.Explanation is { Length: > 0 and <= 4096 } &&
            (reveal.FunFacts is null || reveal.FunFacts.Length <= 5 && reveal.FunFacts.All(f => f is { Length: > 0 and <= 1024 })) &&
            reveal.Players is { } players && players.Length == scores.Length &&
            players.All(player => player is not null && player.AnswerIndex is null or >= 0 and <= 3 &&
                player.Points >= (next.Strategy is null ? 0 : -500) && player.Points <= (next.Strategy is null ? 2000 : 12000)) &&
            players.Select(player => player.PlayerId).Order().SequenceEqual(scores.Select(score => score.PlayerId).Order());
    }

    private static bool ValidVotes(MatchSnapshotDto next)
    {
        bool ValidIds(Guid[]? ids) => ids is null || ids.Length <= 8 && ids.Distinct().Count() == ids.Length &&
            ids.All(id => next.Scores.Any(s => s.PlayerId == id));
        return ValidIds(next.AnsweredPlayers) && ValidIds(next.ContinueVotes) && ValidIds(next.EndVotes) && ValidIds(next.DisconnectedPlayers) && ValidIds(next.ResumeVotes) &&
            (next.IsPaused ? next.PauseId is { } id && id != Guid.Empty : next.PauseId is null && !next.IsResuming && next.ResumeRemainingTicks == 0 && next.ResumeVotes is null or { Length: 0 }) &&
            next.ResumeRemainingTicks is >= 0 and <= 5 * TimeSpan.TicksPerSecond && (next.IsResuming || next.ResumeRemainingTicks == 0) &&
            (next.ResumeVotes is null || next.DisconnectedPlayers is null || !next.ResumeVotes.Intersect(next.DisconnectedPlayers).Any()) &&
            (next.AnsweredPlayers is null || next.AnsweredPlayers.Length == next.AcceptedAnswerCount) &&
            (next.ContinueVotes is null or { Length: 0 } || next.Phase is "AnswerReveal" or "Scoreboard" or "RoundEnd") &&
            (next.EndVotes is null or { Length: 0 } || next.TotalQuestions == 0 && next.Phase == "Scoreboard");
    }
    private static bool ValidMission(MissionDto? mission) => mission is null || mission.Kind is >= 0 and <= 4 &&
        mission.Target == (mission.Kind switch { 0 or 3 => 3, 1 => 4, 2 => 2, _ => 5 }) &&
        mission.Progress >= 0 && mission.Progress <= mission.Target && mission.Complete == (mission.Progress == mission.Target);

    private static bool SameTeams(TeamScoreDto[]? old, TeamScoreDto[]? next) => (old?.Length ?? 0) == (next?.Length ?? 0) &&
        (old is null || old.All(t => next!.Any(n => n.TeamId == t.TeamId && n.Members.SequenceEqual(t.Members))));
    private static bool ValidTeams(MatchSnapshotDto next)
    {
        var teams = next.Teams; var winners = next.WinningTeams;
        if (teams is null or { Length: 0 }) return winners is null or { Length: 0 };
        if (teams.Length != 2 || teams.Any(t => t is null || t.TeamId is not (1 or 2) || t.Total < 0 || t.Members is not { Length: >= 1 and <= 7 }) ||
            teams.Select(t => t.TeamId).Distinct().Count() != 2 ||
            !teams.SelectMany(t => t.Members).Order().SequenceEqual(next.Scores.Select(s => s.PlayerId).Order()) ||
            winners is not { Length: <= 2 } || winners.Distinct().Count() != winners.Length || winners.Any(t => t is not (1 or 2))) return false;
        return next.Phase != "GameOver" ? winners.Length == 0 : winners.Length != 0 &&
            teams.Where(t => winners.Contains(t.TeamId)).SelectMany(t => t.Members).Order().SequenceEqual(next.Winners.Order());
    }

    private static bool ValidStrategy(MatchSnapshotDto next, Guid owner)
    {
        var final = next.FinalStrategy;
        if (next.Strategy is not { } rules) return next.Private is null && (final is null or { Length: 0 });
        var own = next.Private;
        if (own is null || own.PlayerId != owner || own.Hand is not { Length: <= 2 } hand ||
            hand.Any(c => c is null || c.Id == Guid.Empty || c.Kind is < 0 or > 5 || (!rules.AllowSteal && c.Kind >= 4)) ||
            hand.Select(c => c.Id).Distinct().Count() != hand.Length || (!rules.Cards && hand.Length != 0) ||
            own.HiddenAnswers is not { Length: 0 or 2 } hidden || hidden.Any(i => i is < 0 or > 3) || hidden.Distinct().Count() != hidden.Length ||
            own.DeadlineTicks < next.Question.DeadlineTicks || (next.Question.DeadlineTicks != long.MaxValue && own.DeadlineTicks > next.Question.DeadlineTicks + TimeSpan.TicksPerSecond * 5) ||
            own.Streak < 0 || own.Streak > next.QuestionNumber || own.Meter is < 0 or >= 100 ||
            !ValidMission(own.Mission) || (!rules.Missions && own.Mission is not null) ||
            own.SwapCategories is not { Length: <= 3 } categories || categories.Any(c => c is not { Length: > 0 and <= 128 }) ||
            categories.Distinct().Count() != categories.Length || own.Notice is not { Length: > 0 and <= 40 } ||
            final is not { Length: <= 8 }) return false;
        if (next.Phase != "GameOver") return final.Length == 0;
        return final.Length == next.Scores.Length && final.All(s => s is not null && ValidMission(s.Mission) &&
            s.MissionBonus == (s.Mission?.Complete == true ? 500 : 0) && s.CardsUsed is >= 0 and <= 10000 &&
            s.ConfidentCorrect >= 0 && s.ConfidentWrong >= 0 && s.AllInCorrect >= 0 && s.AllInWrong >= 0 &&
            (long)s.ConfidentCorrect + s.ConfidentWrong + s.AllInCorrect + s.AllInWrong <= next.QuestionNumber) &&
            final.Select(s => s.PlayerId).Order().SequenceEqual(next.Scores.Select(s => s.PlayerId).Order());
    }

    private static MatchSnapshotDto Copy(MatchSnapshotDto value) => value with
    {
        AnsweredPlayers = value.AnsweredPlayers?.ToArray(), ContinueVotes = value.ContinueVotes?.ToArray(), EndVotes = value.EndVotes?.ToArray(),
        DisconnectedPlayers = value.DisconnectedPlayers?.ToArray(), ResumeVotes = value.ResumeVotes?.ToArray(),
        Question = value.Question with { Answers = value.Question.Answers.ToArray() }, Scores = value.Scores.ToArray(),
        EligiblePlayers = value.EligiblePlayers.ToArray(), Winners = value.Winners.ToArray(), Statistics = value.Statistics.ToArray(),
        Reveal = value.Reveal is null ? null : value.Reveal with { Players = value.Reveal.Players.ToArray() },
        Private = value.Private is not { } own ? null : own with
        { Hand = own.Hand.ToArray(), HiddenAnswers = own.HiddenAnswers.ToArray(), SwapCategories = own.SwapCategories.ToArray() },
        FinalStrategy = value.FinalStrategy?.ToArray(),
        Teams = value.Teams?.Select(t => t with { Members = t.Members.ToArray() }).ToArray(), WinningTeams = value.WinningTeams?.ToArray()
    };
}

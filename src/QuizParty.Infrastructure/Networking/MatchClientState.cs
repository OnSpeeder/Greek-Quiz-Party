namespace QuizParty.Infrastructure.Networking;

/// <summary>Presentation state only. Never computes correctness, authoritative timing or points.</summary>
public sealed class MatchClientState
{
    private MatchSnapshotDto? _snapshot;
    private Guid? _pendingId;
    private int _pendingIndex;
    private readonly HashSet<Guid> _seenQuestions = new();
    private Guid _localPlayerId;
    public int? OwnAnswerIndex { get; private set; }
    public bool Pending => _pendingId is not null;
    public string LastReason { get; private set; } = "None";
    public MatchSnapshotDto? Snapshot => _snapshot is null ? null : Copy(_snapshot);

    public string? CreateAnswer(int index)
    {
        if (_snapshot?.Phase != "QuestionActive" || !_snapshot.EligiblePlayers.Contains(_localPlayerId) ||
            Pending || OwnAnswerIndex is not null || index is < 0 or > 3) return null;
        _pendingId = Guid.NewGuid();
        _pendingIndex = index;
        return LobbyProtocol.Encode("SubmitAnswer", _snapshot.SessionId,
            new AnswerRequestDto(_snapshot.Question.InstanceId, index, 1), messageId: _pendingId);
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
            receipt.QuestionInstanceId != _snapshot?.Question.InstanceId) return false;
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
        if (next.Revision <= old.Revision || old.Phase == "GameOver" || next.TotalQuestions != old.TotalQuestions ||
            !old.Scores.Select(s => s.PlayerId).Order().SequenceEqual(next.Scores.Select(s => s.PlayerId).Order()) ||
            next.Scores.Any(s => s.Total < old.Scores.Single(p => p.PlayerId == s.PlayerId).Total) ||
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
            question.DeadlineTicks - question.StartedAtTicks > TimeSpan.TicksPerMinute ||
            next.Scores is not { Length: >= 1 and <= 8 } scores ||
            scores.Any(score => score is null || score.PlayerId == Guid.Empty || !LobbyProtocol.ValidName(score.DisplayName) || score.Total < 0) ||
            scores.Select(score => score.PlayerId).Distinct().Count() != scores.Length || !scores.Any(score => score.PlayerId == localPlayer) ||
            next.AcceptedAnswerCount < 0 || next.AcceptedAnswerCount > scores.Length ||
            question.CategoryId is not { Length: > 0 and <= 128 } || question.Difficulty is < 1 or > 5 ||
            next.TotalQuestions is not (1 or 10 or 20 or 30) || next.QuestionNumber is < 1 or > 10000 ||
            next.RoundNumber is < 1 or > 5 || (next.IsTieBreaker != (next.QuestionNumber > next.TotalQuestions) && next.Phase != "RoundEnd") ||
            next.EligiblePlayers is not { Length: >= 1 and <= 8 } eligible || eligible.Distinct().Count() != eligible.Length ||
            eligible.Any(id => !scores.Any(s => s.PlayerId == id)) || next.Winners is not { Length: <= 8 } winners ||
            winners.Distinct().Count() != winners.Length || winners.Any(id => !eligible.Contains(id)) ||
            next.Statistics is not { Length: <= 8 }) return false;
        if (next.Phase != "GameOver" && (winners.Length != 0 || next.Statistics.Length != 0 || next.ContentExhausted)) return false;
        if (next.Phase == "GameOver" && (winners.Length == 0 || next.Statistics.Length != scores.Length ||
            next.Statistics.Any(s => s is null || s.Correct < 0 || s.Wrong < 0 || s.Unanswered < 0 || s.BestStreak < 0 ||
                (long)s.Correct + s.Wrong + s.Unanswered > next.QuestionNumber || s.BestStreak > s.Correct ||
                s.Responses != (long)s.Correct + s.Wrong || s.ResponseTicks < 0 || s.ResponseTicks > (long)s.Responses * TimeSpan.TicksPerMinute) ||
            !next.Statistics.Select(s => s.PlayerId).Order().SequenceEqual(scores.Select(s => s.PlayerId).Order()))) return false;
        if (Rank(next.Phase) < 2) return next.Reveal is null;
        var reveal = next.Reveal;
        return reveal is not null && reveal.CorrectAnswerIndex is >= 0 and <= 3 &&
            reveal.Explanation is { Length: > 0 and <= 4096 } && reveal.Players is { } players && players.Length == scores.Length &&
            players.All(player => player is not null && player.AnswerIndex is null or >= 0 and <= 3 && player.Points >= 0) &&
            players.Select(player => player.PlayerId).Order().SequenceEqual(scores.Select(score => score.PlayerId).Order());
    }

    private static MatchSnapshotDto Copy(MatchSnapshotDto value) => value with
    {
        Question = value.Question with { Answers = value.Question.Answers.ToArray() }, Scores = value.Scores.ToArray(),
        EligiblePlayers = value.EligiblePlayers.ToArray(), Winners = value.Winners.ToArray(), Statistics = value.Statistics.ToArray(),
        Reveal = value.Reveal is null ? null : value.Reveal with { Players = value.Reveal.Players.ToArray() }
    };
}

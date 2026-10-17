namespace QuizParty.Infrastructure.Networking;

/// <summary>Presentation state only. Never computes correctness, authoritative timing or points.</summary>
public sealed class MatchClientState
{
    private MatchSnapshotDto? _snapshot;
    private Guid? _pendingId;
    private int _pendingIndex;
    public int? OwnAnswerIndex { get; private set; }
    public bool Pending => _pendingId is not null;
    public string LastReason { get; private set; } = "None";
    public MatchSnapshotDto? Snapshot => _snapshot is null ? null : Copy(_snapshot);

    public string? CreateAnswer(int index)
    {
        if (_snapshot?.Phase != "QuestionActive" || Pending || OwnAnswerIndex is not null || index is < 0 or > 3) return null;
        _pendingId = Guid.NewGuid();
        _pendingIndex = index;
        return LobbyProtocol.Encode("SubmitAnswer", _snapshot.SessionId,
            new AnswerRequestDto(_snapshot.Question.InstanceId, index, 1), messageId: _pendingId);
    }

    public bool ApplySnapshot(LobbyEnvelope packet, Guid sessionId, Guid localPlayerId)
    {
        if (packet.SessionId != sessionId || !LobbyProtocol.TryPayload<MatchSnapshotDto>(packet, out var next) ||
            !Valid(next, sessionId, localPlayerId) || next is null ||
            (_snapshot is not null && (next.Revision <= _snapshot.Revision || Rank(next.Phase) < Rank(_snapshot.Phase) ||
                next.Question.InstanceId != _snapshot.Question.InstanceId))) return false;
        _snapshot = Copy(next);
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
        "QuestionActive" => 0, "QuestionLocked" => 1, "AnswerReveal" => 2, "Scoreboard" => 3, "GameOver" => 4, _ => -1
    };

    private static bool Valid(MatchSnapshotDto? next, Guid session, Guid localPlayer)
    {
        if (next is null || next.SessionId != session || next.Revision <= 0 || Rank(next.Phase) < 0 || next.HostNowTicks < 0 ||
            next.Question is not { } question || question.InstanceId == Guid.Empty || question.Text is not { Length: > 0 and <= 2048 } ||
            question.Answers is not { Length: 4 } answers || answers.Any(answer => string.IsNullOrWhiteSpace(answer) || answer.Length > 512) ||
            question.StartedAtTicks < 0 || question.DeadlineTicks <= question.StartedAtTicks ||
            next.Scores is not { Length: >= 1 and <= 8 } scores ||
            scores.Any(score => score is null || score.PlayerId == Guid.Empty || !LobbyProtocol.ValidName(score.DisplayName) || score.Total < 0) ||
            scores.Select(score => score.PlayerId).Distinct().Count() != scores.Length || !scores.Any(score => score.PlayerId == localPlayer) ||
            next.AcceptedAnswerCount < 0 || next.AcceptedAnswerCount > scores.Length) return false;
        if (Rank(next.Phase) < 2) return next.Reveal is null && scores.All(score => score.Total == 0);
        var reveal = next.Reveal;
        return reveal is not null && reveal.CorrectAnswerIndex is >= 0 and <= 3 &&
            reveal.Explanation is { Length: > 0 and <= 4096 } && reveal.Players is { } players && players.Length == scores.Length &&
            players.All(player => player is not null && player.AnswerIndex is null or >= 0 and <= 3 && player.Points >= 0) &&
            players.Select(player => player.PlayerId).Order().SequenceEqual(scores.Select(score => score.PlayerId).Order());
    }

    private static MatchSnapshotDto Copy(MatchSnapshotDto value) => value with
    {
        Question = value.Question with { Answers = value.Question.Answers.ToArray() }, Scores = value.Scores.ToArray(),
        Reveal = value.Reveal is null ? null : value.Reveal with { Players = value.Reveal.Players.ToArray() }
    };
}

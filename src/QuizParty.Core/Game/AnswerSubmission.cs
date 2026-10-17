using QuizParty.Core.Players;
using QuizParty.Core.Questions;

namespace QuizParty.Core.Game;

public enum ConfidenceLevel { Safe = 1, Confident = 2, AllIn = 3 }

/// <summary>Mapped from a client intent by the host; contains no client timestamp or score.</summary>
public sealed record AnswerSubmission(PlayerId PlayerId, QuestionInstanceId QuestionInstanceId,
    int AnswerIndex, ConfidenceLevel Confidence = ConfidenceLevel.Safe);

public enum SubmissionError
{
    None, NotAuthoritative, UnknownPlayer, InvalidState, StaleQuestion,
    AlreadyAnswered, InvalidAnswerIndex, InvalidConfidence, TooEarly, Late, InvalidReceiveTime
}

public static class SubmissionValidator
{
    public static SubmissionError Validate(AnswerSubmission submission, GamePhase phase,
        QuestionPresentation? question, bool isEligible, bool alreadyAnswered, TimeSpan hostReceivedAt, TimeSpan hostNow)
    {
        if (!isEligible) return SubmissionError.UnknownPlayer;
        if (phase != GamePhase.QuestionActive || question is null) return SubmissionError.InvalidState;
        if (submission.QuestionInstanceId != question.InstanceId) return SubmissionError.StaleQuestion;
        if (alreadyAnswered) return SubmissionError.AlreadyAnswered;
        if (submission.AnswerIndex is < 0 or > 3) return SubmissionError.InvalidAnswerIndex;
        // Strategic confidence is deliberately deferred to Phase 08.
        if (submission.Confidence != ConfidenceLevel.Safe) return SubmissionError.InvalidConfidence;
        if (hostReceivedAt > hostNow) return SubmissionError.InvalidReceiveTime;
        if (hostReceivedAt < question.StartedAt) return SubmissionError.TooEarly;
        if (hostReceivedAt > question.Deadline) return SubmissionError.Late;
        return SubmissionError.None;
    }
}

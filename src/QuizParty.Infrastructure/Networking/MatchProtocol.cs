using System.Text.Json.Serialization;

namespace QuizParty.Infrastructure.Networking;

public sealed record AnswerRequestDto(Guid QuestionInstanceId, [property: JsonRequired] int AnswerIndex,
    [property: JsonRequired] int Confidence);
public sealed record AnswerReceiptDto(bool Accepted, string Reason, Guid QuestionInstanceId);
public sealed record MatchQuestionDto(Guid InstanceId, string Text, string[] Answers, string CategoryId,
    int Difficulty, long StartedAtTicks, long DeadlineTicks);
public sealed record MatchScoreDto(Guid PlayerId, string DisplayName, long Total);
public sealed record MatchPlayerResultDto(Guid PlayerId, int? AnswerIndex, bool IsCorrect, int Points);
public sealed record MatchRevealDto(int CorrectAnswerIndex, string Explanation, MatchPlayerResultDto[] Players);
public sealed record MatchStatisticsDto(Guid PlayerId, int Correct, int Wrong, int Unanswered,
    int BestStreak, long ResponseTicks, int Responses);
public sealed record MatchSnapshotDto(Guid SessionId, long Revision, string Phase, long HostNowTicks,
    MatchQuestionDto Question, int AcceptedAnswerCount, MatchScoreDto[] Scores, MatchRevealDto? Reveal,
    int QuestionNumber, int TotalQuestions, int RoundNumber, bool IsTieBreaker, Guid[] EligiblePlayers,
    Guid[] Winners, bool ContentExhausted, MatchStatisticsDto[] Statistics);

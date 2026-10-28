using System.Text.Json.Serialization;

namespace QuizParty.Infrastructure.Networking;

public sealed record MatchVoteDto(Guid QuestionInstanceId, string Phase, bool EndGame = false, int LocalSlot = 0);
public sealed record ResumeVoteDto(Guid PauseId, int LocalSlot = 0);
public sealed record AnswerRequestDto(Guid QuestionInstanceId, [property: JsonRequired] int AnswerIndex,
    [property: JsonRequired] int Confidence, int LocalSlot = 0);
public sealed record AnswerReceiptDto(bool Accepted, string Reason, Guid QuestionInstanceId, int LocalSlot = 0);
public sealed record MatchQuestionDto(Guid InstanceId, string Text, string[] Answers, string CategoryId,
    int Difficulty, long StartedAtTicks, long DeadlineTicks);
public sealed record MatchScoreDto(Guid PlayerId, string DisplayName, long Total, int? CharacterId = null);
public sealed record MatchPlayerResultDto(Guid PlayerId, int? AnswerIndex, bool IsCorrect, int Points);
public sealed record MatchRevealDto(int CorrectAnswerIndex, string Explanation, MatchPlayerResultDto[] Players, string[]? FunFacts = null);
public sealed record MatchStatisticsDto(Guid PlayerId, int Correct, int Wrong, int Unanswered,
    int BestStreak, long ResponseTicks, int Responses);
public sealed record StrategyRulesDto(bool Confidence, bool Streaks, bool Cards, bool Missions, bool AllowSteal);
public sealed record CardDto(Guid Id, int Kind);
public sealed record MissionDto(int Kind, int Target, int Progress, bool Complete);
public sealed record StrategyPrivateDto(Guid PlayerId, CardDto[] Hand, int[] HiddenAnswers, long DeadlineTicks,
    bool Shield, bool DoublePoints, int Streak, int Meter, MissionDto? Mission, string[] SwapCategories, string Notice);
public sealed record StrategyFinalDto(Guid PlayerId, MissionDto? Mission, int MissionBonus, int CardsUsed,
    int ConfidentCorrect, int ConfidentWrong, int AllInCorrect, int AllInWrong);
public sealed record CardRequestDto(Guid QuestionInstanceId, Guid CardId, Guid? Target = null, string? Category = null, int LocalSlot = 0);
public sealed record CardReceiptDto(bool Accepted, string Reason, Guid QuestionInstanceId, Guid CardId, int LocalSlot = 0);
public sealed record TeamScoreDto(int TeamId, long Total, Guid[] Members);
public sealed record MatchSnapshotDto(Guid SessionId, long Revision, string Phase, long HostNowTicks,
    MatchQuestionDto Question, int AcceptedAnswerCount, MatchScoreDto[] Scores, MatchRevealDto? Reveal,
    int QuestionNumber, int TotalQuestions, int RoundNumber, bool IsTieBreaker, Guid[] EligiblePlayers,
    Guid[] Winners, bool ContentExhausted, MatchStatisticsDto[] Statistics,
    StrategyRulesDto? Strategy = null, StrategyPrivateDto? Private = null, StrategyFinalDto[]? FinalStrategy = null,
    TeamScoreDto[]? Teams = null, int[]? WinningTeams = null, int LocalSlot = 0, Guid[]? AnsweredPlayers = null,
    Guid[]? ContinueVotes = null, Guid[]? EndVotes = null, bool IsPaused = false, Guid? PauseId = null,
    long ResumeRemainingTicks = 0, Guid[]? DisconnectedPlayers = null, Guid[]? ResumeVotes = null, bool IsResuming = false);

using QuizParty.Core.Players;
using QuizParty.Core.Questions;

namespace QuizParty.Core.Game;

public sealed record PlayerScore(PlayerId PlayerId, string DisplayName, long Total);
public sealed record PlayerQuestionResult(PlayerId PlayerId, int? AnswerIndex, bool IsCorrect, int Points,
    TimeSpan? ResponseTime = null, ConfidenceLevel Confidence = ConfidenceLevel.Safe);
public sealed record QuestionResult(QuestionInstanceId InstanceId, int CorrectAnswerIndex,
    string Explanation, IReadOnlyList<PlayerQuestionResult> Players, IReadOnlyList<string>? FunFacts = null);

/// <summary>Public domain view, not a network DTO. Correctness exists only in Reveal.</summary>
public sealed record GameSnapshot(GamePhase Phase, QuestionPresentation? Question,
    int AcceptedAnswerCount, QuestionResult? Reveal, IReadOnlyList<PlayerScore> Scores);

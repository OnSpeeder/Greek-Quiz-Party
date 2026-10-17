using System.Text.Json.Serialization;
using QuizParty.Core.Questions;

namespace QuizParty.Infrastructure.Networking;

public sealed record AnswerRequestDto(Guid QuestionInstanceId, [property: JsonRequired] int AnswerIndex,
    [property: JsonRequired] int Confidence);
public sealed record AnswerReceiptDto(bool Accepted, string Reason, Guid QuestionInstanceId);
public sealed record MatchQuestionDto(Guid InstanceId, string Text, string[] Answers, string CategoryId,
    int Difficulty, long StartedAtTicks, long DeadlineTicks);
public sealed record MatchScoreDto(Guid PlayerId, string DisplayName, long Total);
public sealed record MatchPlayerResultDto(Guid PlayerId, int? AnswerIndex, bool IsCorrect, int Points);
public sealed record MatchRevealDto(int CorrectAnswerIndex, string Explanation, MatchPlayerResultDto[] Players);
public sealed record MatchSnapshotDto(Guid SessionId, long Revision, string Phase, long HostNowTicks,
    MatchQuestionDto Question, int AcceptedAnswerCount, MatchScoreDto[] Scores, MatchRevealDto? Reveal);

/// <summary>Tiny permitted vertical-slice fixture, not production content/a reviewed question pack.</summary>
public static class VerticalSliceFixture
{
    public static QuestionDefinition Question => new("slice_capital_greece", "Ποια είναι η πρωτεύουσα της Ελλάδας;",
        ["Αθήνα", "Θεσσαλονίκη", "Πάτρα", "Ηράκλειο"], 0, "greece", 1,
        "Η Αθήνα είναι η πρωτεύουσα της Ελλάδας.");
}

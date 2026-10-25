using QuizParty.Core.Randomness;

namespace QuizParty.Core.Questions;

public readonly record struct QuestionInstanceId(Guid Value);

/// <summary>Host-only domain content. Never serialize this as a client snapshot.</summary>
public sealed class QuestionDefinition
{
    public QuestionDefinition(string id, string text, IEnumerable<string> answers,
        int correctAnswerIndex, string categoryId, int difficulty, string explanation,
        IEnumerable<string>? funFacts = null)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(id);
        ArgumentException.ThrowIfNullOrWhiteSpace(text);
        ArgumentNullException.ThrowIfNull(answers);
        ArgumentException.ThrowIfNullOrWhiteSpace(categoryId);
        ArgumentException.ThrowIfNullOrWhiteSpace(explanation);
        var copy = answers.Take(5).ToArray();
        if (copy.Length != 4 || copy.Any(string.IsNullOrWhiteSpace) || copy.Distinct(StringComparer.Ordinal).Count() != 4)
            throw new ArgumentException("Exactly four distinct nonblank answers are required.", nameof(answers));
        if (correctAnswerIndex is < 0 or > 3) throw new ArgumentOutOfRangeException(nameof(correctAnswerIndex));
        if (difficulty is < 1 or > 5) throw new ArgumentOutOfRangeException(nameof(difficulty));
        var facts = funFacts?.Where(f => !string.IsNullOrWhiteSpace(f)).Take(5).ToArray() ?? Array.Empty<string>();
        Id = id;
        Text = text;
        Answers = Array.AsReadOnly(copy);
        CorrectAnswerIndex = correctAnswerIndex;
        CategoryId = categoryId;
        Difficulty = difficulty;
        Explanation = explanation;
        FunFacts = Array.AsReadOnly(facts);
    }

    public string Id { get; }
    public string Text { get; }
    public IReadOnlyList<string> Answers { get; }
    public int CorrectAnswerIndex { get; }
    public string CategoryId { get; }
    public int Difficulty { get; }
    public string Explanation { get; }
    public IReadOnlyList<string> FunFacts { get; }
}

public sealed record QuestionPresentation(QuestionInstanceId InstanceId, string Text,
    IReadOnlyList<string> Answers, string CategoryId, int Difficulty, TimeSpan StartedAt, TimeSpan Deadline);

internal sealed class QuestionInstance
{
    public QuestionInstance(QuestionDefinition definition, QuestionInstanceId id,
        TimeSpan startedAt, TimeSpan duration, IRandomSource random)
    {
        var order = new[] { 0, 1, 2, 3 };
        for (var i = order.Length - 1; i > 0; i--)
        {
            var j = random.Next(i + 1);
            if (j < 0 || j > i) throw new InvalidOperationException("Random source returned an out-of-range value.");
            (order[i], order[j]) = (order[j], order[i]);
        }
        Presentation = new(id, definition.Text,
            Array.AsReadOnly(order.Select(index => definition.Answers[index]).ToArray()),
            definition.CategoryId, definition.Difficulty, startedAt, duration == TimeSpan.Zero ? TimeSpan.MaxValue : startedAt + duration);
        CorrectAnswerIndex = Array.IndexOf(order, definition.CorrectAnswerIndex);
        Explanation = definition.Explanation;
        FunFacts = definition.FunFacts;
    }

    public QuestionPresentation Presentation { get; }
    public int CorrectAnswerIndex { get; }
    public string Explanation { get; }
    public IReadOnlyList<string> FunFacts { get; }
}

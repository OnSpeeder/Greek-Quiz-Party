namespace QuizParty.Core.Questions;

public sealed record QuestionCategory(string Id, string NameKey);

/// <summary>Validated reviewed domain content; collections are detached and read-only.</summary>
public sealed class QuestionPack
{
    public QuestionPack(string locale, string version, IEnumerable<QuestionCategory> categories, IEnumerable<QuestionDefinition> questions)
    {
        Locale = locale;
        Version = version;
        Categories = Array.AsReadOnly(categories.ToArray());
        Questions = Array.AsReadOnly(questions.ToArray());
    }
    public string Locale { get; }
    public string Version { get; }
    public IReadOnlyList<QuestionCategory> Categories { get; }
    public IReadOnlyList<QuestionDefinition> Questions { get; }
}

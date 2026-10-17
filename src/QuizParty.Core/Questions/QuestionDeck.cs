using QuizParty.Core.Randomness;

namespace QuizParty.Core.Questions;

/// <summary>Host-owned, finite deck. Buckets mix categories/difficulties without replacement.</summary>
public sealed class QuestionDeck
{
    private readonly Queue<QuestionDefinition> _remaining;
    public int Remaining => _remaining.Count;

    public QuestionDeck(IEnumerable<QuestionDefinition> questions, IRandomSource random,
        IReadOnlyCollection<string>? categories = null)
    {
        ArgumentNullException.ThrowIfNull(questions);
        ArgumentNullException.ThrowIfNull(random);
        var source = questions.ToArray();
        if (source.Any(q => q is null) || source.Select(q => q.Id).Distinct(StringComparer.Ordinal).Count() != source.Length)
            throw new ArgumentException("Question IDs must be unique.", nameof(questions));
        var buckets = source.Where(q => categories is null || categories.Contains(q.CategoryId))
            .GroupBy(q => (q.CategoryId, q.Difficulty)).OrderBy(g => g.Key.CategoryId, StringComparer.Ordinal)
            .ThenBy(g => g.Key.Difficulty).Select(g => g.OrderBy(q => q.Id, StringComparer.Ordinal).ToList()).ToList();
        foreach (var bucket in buckets) Shuffle(bucket, random);
        var selected = new List<QuestionDefinition>();
        while (buckets.Count > 0)
        {
            Shuffle(buckets, random);
            foreach (var bucket in buckets) { selected.Add(bucket[^1]); bucket.RemoveAt(bucket.Count - 1); }
            buckets.RemoveAll(bucket => bucket.Count == 0);
        }
        _remaining = new(selected);
    }

    public QuestionDefinition? Draw() => _remaining.TryDequeue(out var question) ? question : null;

    private static void Shuffle<T>(IList<T> values, IRandomSource random)
    {
        for (var i = values.Count - 1; i > 0; i--)
        {
            var j = random.Next(i + 1);
            if (j < 0 || j > i) throw new InvalidOperationException("Invalid random source.");
            (values[i], values[j]) = (values[j], values[i]);
        }
    }
}

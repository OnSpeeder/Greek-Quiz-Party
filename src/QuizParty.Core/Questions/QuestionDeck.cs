using QuizParty.Core.Randomness;

namespace QuizParty.Core.Questions;

/// <summary>Host-owned, finite deck. Buckets mix categories/difficulties without replacement.</summary>
public sealed class QuestionDeck
{
    private readonly Queue<QuestionDefinition> _remaining;
    private readonly IRandomSource _random;
    public int Remaining => _remaining.Count;

    public QuestionDeck(IEnumerable<QuestionDefinition> questions, IRandomSource random,
        IReadOnlyCollection<string>? categories = null)
    {
        ArgumentNullException.ThrowIfNull(questions);
        ArgumentNullException.ThrowIfNull(random);
        _random = random;
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
    public IReadOnlyList<QuestionDefinition> Upcoming(int count) => Array.AsReadOnly(_remaining.Take(count).ToArray());
    public string[] SwapCategories(int normalRemaining, Func<IReadOnlyList<QuestionDefinition>, bool> feasible) =>
        _remaining.Select(q => q.CategoryId).Distinct(StringComparer.Ordinal).Where(c => SwapIndices(c, normalRemaining, feasible).Count > 0).Order(StringComparer.Ordinal).ToArray();
    public bool SwapNext(string category, int normalRemaining, Func<IReadOnlyList<QuestionDefinition>, bool> feasible)
    {
        var indices = SwapIndices(category, normalRemaining, feasible);
        if (indices.Count == 0) return false;
        var index = _random.Next(indices.Count);
        if (index < 0 || index >= indices.Count) throw new InvalidOperationException("Invalid random source.");
        var remaining = _remaining.ToArray(); var selected = indices[index];
        (remaining[0], remaining[selected]) = (remaining[selected], remaining[0]);
        _remaining.Clear(); foreach (var q in remaining) _remaining.Enqueue(q);
        return true;
    }
    private List<int> SwapIndices(string category, int count, Func<IReadOnlyList<QuestionDefinition>, bool> feasible)
    {
        var remaining = _remaining.ToArray(); var indices = new List<int>();
        if (count <= 0 || remaining.Length == 0 || remaining[0].CategoryId == category) return indices;
        for (var i = 1; i < remaining.Length; i++)
        {
            if (remaining[i].CategoryId != category) continue;
            (remaining[0], remaining[i]) = (remaining[i], remaining[0]);
            if (feasible(remaining.Take(count).ToArray())) indices.Add(i);
            (remaining[0], remaining[i]) = (remaining[i], remaining[0]);
        }
        return indices;
    }

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

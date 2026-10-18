using System.Globalization;
using System.Text;
using System.Text.Json;
using QuizParty.Core.Questions;

namespace QuizParty.Infrastructure.Content;

public sealed record ContentIssue(string File, string QuestionId, string Code, string Message, bool Warning = false);
public sealed record PackValidation(QuestionPack? Pack, IReadOnlyList<ContentIssue> Issues)
{
    public bool Success => Pack is not null && !Issues.Any(issue => !issue.Warning);
}

/// <summary>One validator for CLI, tests and packaged Godot. No engine/filesystem assumptions.</summary>
public static class QuestionPackLoader
{
    public const int MaxFileBytes = 4 * 1024 * 1024;
    public const int MaxFiles = 64;
    public const int MaxEncodedQuestionBytes = 7000;
    private static readonly string[] ManifestFields = ["schemaVersion", "locale", "packVersion", "categories"];
    private static readonly string[] QuestionFields = ["id", "text", "answers", "correctAnswerIndex", "categoryId", "difficulty", "explanation", "source", "locale", "tags", "status", "verifiedAt", "expiresAfter"];

    public static PackValidation Validate(string manifest, IReadOnlyDictionary<string, string> files, string expectedLocale,
        bool release = true, DateOnly? today = null)
    {
        var issues = new List<ContentIssue>();
        var categories = new List<QuestionCategory>();
        var questions = new List<QuestionDefinition>();
        var ids = new HashSet<string>(StringComparer.Ordinal);
        var texts = new List<(string Text, string Id)>();
        var distractors = new HashSet<string>(StringComparer.Ordinal);
        var version = "";
        var date = today ?? DateOnly.FromDateTime(DateTime.UtcNow);
        void Issue(string file, string id, string code, string message, bool warning = false) => issues.Add(new(file, id, code, message, warning));
        if (string.IsNullOrWhiteSpace(expectedLocale)) Issue("manifest.json", "", "locale", "Expected locale cannot be blank.");
        using (var doc = Parse(manifest, "manifest.json", Issue))
        {
            if (doc is not null)
            {
                var root = doc.RootElement;
                if (!Object(root, ManifestFields)) Issue("manifest.json", "", "schema", "Expected manifest object with known unique fields.");
                else
                {
                    if (!Integer(root, "schemaVersion", out var schema) || schema != 1) Issue("manifest.json", "", "version", "schemaVersion must be 1.");
                    if (Text(root, "locale") != expectedLocale) Issue("manifest.json", "", "locale", "Manifest locale differs from expected locale.");
                    version = Text(root, "packVersion");
                    if (!Version.TryParse(version, out _)) Issue("manifest.json", "", "version", "packVersion must be a dotted numeric version.");
                    if (!root.TryGetProperty("categories", out var array) || array.ValueKind != JsonValueKind.Array || array.GetArrayLength() is < 1 or > 128)
                        Issue("manifest.json", "", "categories", "Expected 1–128 categories.");
                    else foreach (var category in array.EnumerateArray())
                    {
                        var id = Text(category, "id");
                        var key = Text(category, "nameKey");
                        if (!Object(category, ["id", "nameKey"]) || !Identifier(id) || !Identifier(key) || categories.Any(value => value.Id == id))
                            Issue("manifest.json", id, "category", "Category requires unique id and nonblank nameKey.");
                        else categories.Add(new(id, key));
                    }
                }
            }
        }
        if (files.Count is < 1 or > MaxFiles) Issue("manifest.json", "", "files", "Expected 1–64 question JSON files.");
        foreach (var (file, json) in files.OrderBy(pair => pair.Key, StringComparer.Ordinal).Take(MaxFiles))
        {
            using var doc = Parse(json, file, Issue);
            if (doc is null) continue;
            if (doc.RootElement.ValueKind != JsonValueKind.Array || doc.RootElement.GetArrayLength() > 10000)
            { Issue(file, "", "schema", "Question file must be an array of at most 10000 questions."); continue; }
            foreach (var value in doc.RootElement.EnumerateArray())
            {
                var id = Text(value, "id");
                var before = issues.Count(issue => !issue.Warning);
                if (!Object(value, QuestionFields)) { Issue(file, id, "schema", "Question must be an object with known unique fields."); continue; }
                var text = Text(value, "text");
                var explanation = Text(value, "explanation");
                var category = Text(value, "categoryId");
                var status = Text(value, "status");
                if (!Identifier(id)) Issue(file, id, "id", "id must be a nonblank identifier (max 128).");
                else if (!ids.Add(id)) Issue(file, id, "duplicate-id", "Question ID is repeated across the pack.");
                if (string.IsNullOrWhiteSpace(text)) Issue(file, id, "text", "text is required.");
                if (string.IsNullOrWhiteSpace(explanation)) Issue(file, id, "explanation", "explanation is required.");
                if (Text(value, "locale") != expectedLocale) Issue(file, id, "locale", "Question locale differs from expected locale.");
                if (!categories.Any(item => item.Id == category)) Issue(file, id, "category", "categoryId must exist in manifest.");
                if (!Integer(value, "correctAnswerIndex", out var correct) || correct is < 0 or > 3) Issue(file, id, "correct-index", "correctAnswerIndex must be 0–3.");
                if (!Integer(value, "difficulty", out var difficulty) || difficulty is < 1 or > 5) Issue(file, id, "difficulty", "difficulty must be 1–5.");
                if (status is not ("draft" or "reviewed" or "rejected")) Issue(file, id, "status", "status must be draft/reviewed/rejected.");
                if (release && status != "reviewed") Issue(file, id, "unreviewed", "Release packs may contain only reviewed questions.");
                var answers = Array.Empty<string>();
                if (value.TryGetProperty("answers", out var list) && list.ValueKind == JsonValueKind.Array && list.GetArrayLength() == 4)
                    answers = list.EnumerateArray().Select(answer => answer.ValueKind == JsonValueKind.String ? answer.GetString()! : "").ToArray();
                if (answers.Length != 4 || answers.Any(string.IsNullOrWhiteSpace)) Issue(file, id, "answers", "Exactly four nonblank string answers required.");
                else if (answers.Select(Normalize).Distinct().Count() != 4) Issue(file, id, "duplicate-answer", "Answer choices must be distinct after normalization.");
                if (!string.IsNullOrWhiteSpace(text))
                {
                    var normalized = Normalize(text);
                    if (texts.Any(item => item.Text == normalized)) Issue(file, id, "duplicate-text", "Normalized question text is repeated.");
                    else if (texts.Any(item => Similar(item.Text, normalized))) Issue(file, id, "similar-text", "Question text is suspiciously similar to another entry.", true);
                    texts.Add((normalized, id));
                }
                if (text.Length > 300 || answers.Any(answer => answer.Length > 150)) Issue(file, id, "long-text", "Long question or answer; check layout.", true);
                if (text.Length > 2048 || explanation.Length > 4096 || answers.Any(answer => answer.Length > 512)) Issue(file, id, "wire-limit", "Text exceeds current game DTO bounds.");
                if (JsonSerializer.SerializeToUtf8Bytes(new { text, answers, explanation }).Length > MaxEncodedQuestionBytes) Issue(file, id, "wire-limit", "Encoded content exceeds reserved match packet budget.");
                var source = Text(value, "source");
                if (value.TryGetProperty("source", out var sourceValue) && sourceValue.ValueKind != JsonValueKind.String) Issue(file, id, "source", "source must be a string URL.");
                if (string.IsNullOrWhiteSpace(source)) Issue(file, id, "source", "Factual source is missing.", true);
                else if (!Uri.TryCreate(source, UriKind.Absolute, out var uri) || uri.Scheme is not ("https" or "http")) Issue(file, id, "source", "source must be an HTTP(S) URL.");
                if (value.TryGetProperty("tags", out var tags) && (tags.ValueKind != JsonValueKind.Array || tags.GetArrayLength() > 32 || tags.EnumerateArray().Any(tag => tag.ValueKind != JsonValueKind.String || !Identifier(tag.GetString()!))))
                    Issue(file, id, "tags", "tags must be at most 32 nonblank strings.");
                foreach (var field in new[] { "verifiedAt", "expiresAfter" })
                    if (value.TryGetProperty(field, out _))
                    {
                        if (!DateOnly.TryParseExact(Text(value, field), "yyyy-MM-dd", CultureInfo.InvariantCulture, DateTimeStyles.None, out var metadataDate)) Issue(file, id, "date", $"{field} must be YYYY-MM-DD.");
                        else if (field == "expiresAfter" && metadataDate < date || field == "verifiedAt" && metadataDate < date.AddYears(-2)) Issue(file, id, "stale", $"{field} indicates stale content.", true);
                    }
                if (text.Contains('\uFFFD') || explanation.Contains('\uFFFD') || answers.Any(answer => answer.Contains('\uFFFD'))) Issue(file, id, "encoding", "Replacement character found; inspect encoding.", true);
                if (answers.Length == 4 && correct is >= 0 and <= 3)
                {
                    var signature = string.Join('|', answers.Where((_, index) => index != correct).Select(Normalize).Order());
                    if (!distractors.Add(signature)) Issue(file, id, "distractors", "Repeated distractor set; check variety.", true);
                }
                if (issues.Count(issue => !issue.Warning) == before && status == "reviewed")
                    questions.Add(new(id, text, answers, correct, category, difficulty, explanation));
            }
        }
        if (questions.Count == 0 && !issues.Any(issue => !issue.Warning)) Issue("manifest.json", "", "empty", "Pack contains no reviewed playable questions.");
        var pack = issues.Any(issue => !issue.Warning) ? null : new QuestionPack(expectedLocale, version, categories, questions);
        return new(pack, issues.AsReadOnly());
    }

    public static PackValidation LoadDirectory(string directory, string locale, bool release = true)
    {
        try
        {
            var files = Directory.EnumerateFiles(directory, "*.json").Where(path => Path.GetFileName(path) != "manifest.json").Order().Take(MaxFiles + 1).ToArray();
            string Read(string path)
            {
                if (new FileInfo(path).Length > MaxFileBytes) throw new InvalidDataException($"File exceeds {MaxFileBytes} bytes: {path}");
                return new UTF8Encoding(false, true).GetString(File.ReadAllBytes(path)).TrimStart('\uFEFF');
            }
            return Validate(Read(Path.Combine(directory, "manifest.json")), files.ToDictionary(path => Path.GetFileName(path)!, Read), locale, release);
        }
        catch (Exception error) when (error is IOException or UnauthorizedAccessException or DecoderFallbackException)
        { return new(null, [new(directory, "", "read", error.Message)]); }
    }

    private static JsonDocument? Parse(string json, string file, Action<string, string, string, string, bool> issue)
    {
        if (Encoding.UTF8.GetByteCount(json) > MaxFileBytes) { issue(file, "", "size", "File too large.", false); return null; }
        JsonDocument? document = null;
        try
        {
            document = JsonDocument.Parse(json, new JsonDocumentOptions { MaxDepth = 16 });
            CheckUnicode(document.RootElement);
            return document;
        }
        catch (Exception error) when (error is JsonException or InvalidOperationException or ArgumentException)
        { document?.Dispose(); issue(file, "", "json", error.Message, false); return null; }
    }
    private static void CheckUnicode(JsonElement value)
    {
        if (value.ValueKind == JsonValueKind.String) _ = new UTF8Encoding(false, true).GetByteCount(value.GetString()!);
        else if (value.ValueKind == JsonValueKind.Array) foreach (var child in value.EnumerateArray()) CheckUnicode(child);
        else if (value.ValueKind == JsonValueKind.Object) foreach (var property in value.EnumerateObject())
            { _ = new UTF8Encoding(false, true).GetByteCount(property.Name); CheckUnicode(property.Value); }
    }
    private static bool Object(JsonElement value, string[] fields) => value.ValueKind == JsonValueKind.Object &&
        value.EnumerateObject().All(property => fields.Contains(property.Name, StringComparer.Ordinal)) &&
        value.EnumerateObject().Select(property => property.Name).Distinct().Count() == value.EnumerateObject().Count();
    private static string Text(JsonElement value, string name) => value.ValueKind == JsonValueKind.Object && value.TryGetProperty(name, out var item) && item.ValueKind == JsonValueKind.String ? item.GetString()! : "";
    private static bool Integer(JsonElement value, string name, out int result)
    { result = 0; return value.TryGetProperty(name, out var item) && item.ValueKind == JsonValueKind.Number && item.TryGetInt32(out result); }
    private static bool Identifier(string value) => !string.IsNullOrWhiteSpace(value) && value.Length <= 128 && !value.Any(char.IsControl);
    private static string Normalize(string value) => string.Join(' ', value.Normalize(NormalizationForm.FormC).Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries)).ToUpperInvariant();
    private static bool Similar(string first, string second)
    {
        var left = first.Split(' ').ToHashSet();
        var right = second.Split(' ').ToHashSet();
        return left.Count >= 4 && right.Count >= 4 && (double)left.Intersect(right).Count() / left.Union(right).Count() >= 0.8;
    }
}

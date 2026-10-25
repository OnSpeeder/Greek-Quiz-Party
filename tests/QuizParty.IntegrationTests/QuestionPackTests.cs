using System.Text;
using System.Text.Json.Nodes;
using QuizParty.Infrastructure.Content;
using Xunit;

namespace QuizParty.IntegrationTests;

public class QuestionPackTests
{
    private const string Manifest = """
        {"schemaVersion":1,"locale":"el-GR","packVersion":"1.0.0","categories":[{"id":"greece","nameKey":"CATEGORY_GREECE"}]}
        """;
    private static JsonObject Question() => JsonNode.Parse("""
        {"id":"test_1","text":"Ποια είναι η πρωτεύουσα της Ελλάδας;","answers":["Αθήνα","Πάτρα","Λάρισα","Χανιά"],"correctAnswerIndex":0,"categoryId":"greece","difficulty":1,"explanation":"Η Αθήνα είναι η πρωτεύουσα.","locale":"el-GR","status":"reviewed","source":"https://example.org/reference"}
        """)!.AsObject();
    private static PackValidation Validate(JsonObject question, bool release = true) => QuestionPackLoader.Validate(Manifest,
        new Dictionary<string,string> { ["greece.json"] = new JsonArray(question.DeepClone()).ToJsonString() }, "el-GR", release, new(2026,10,18));

    [Fact]
    public void IndexedSimilarityMatchesExhaustiveScanAcrossDifferentVocabularySizes()
    {
        var random = new Random(42);
        var prior = new List<HashSet<string>>(); var items = new JsonArray();
        var expected = new HashSet<string>(); var normalized = new HashSet<string>();
        for (var i = 0; i < 500; i++)
        {
            var words = Enumerable.Range(0, random.Next(2, 20)).Select(_ => "W" + random.Next(25)).ToHashSet();
            var text = string.Join(" ", words.Order());
            if (!normalized.Add(text)) continue;
            var id = "q" + i;
            if (words.Count >= 4 && prior.Any(previous => previous.Count >= 4 &&
                (double)previous.Intersect(words).Count() / previous.Union(words).Count() >= .8)) expected.Add(id);
            prior.Add(words);
            var item = Question(); item["id"] = id; item["text"] = text; items.Add(item);
        }
        var result = QuestionPackLoader.Validate(Manifest, new Dictionary<string, string> { ["test.json"] = items.ToJsonString() }, "el-GR");
        Assert.True(result.Success);
        Assert.Equal(expected.Order(), result.Issues.Where(issue => issue.Code == "similar-text").Select(issue => issue.QuestionId).Order());
    }

    [Fact]
    public void ValidReviewedPackPreservesGreekAndReturnsReadOnlyDomainContent()
    {
        var result = Validate(Question());
        Assert.True(result.Success);
        var pack = result.Pack!;
        Assert.Equal("Αθήνα", Assert.Single(pack.Questions).Answers[0]);
        Assert.Equal("CATEGORY_GREECE", Assert.Single(pack.Categories).NameKey);
        Assert.Throws<NotSupportedException>(() => ((IList<QuizParty.Core.Questions.QuestionDefinition>)pack.Questions).Clear());
    }

    [Fact]
    public void SimilarityWarningPreservesExactJaccardBoundaryAndDuplicatePriority()
    {
        var texts = new[] { "ένα δύο τρία τέσσερα", "ένα δύο τρία τέσσερα πέντε",
            "ένα δύο τρία έξι επτά οκτώ", "ένα  δύο τρία τέσσερα" };
        var items = new JsonArray();
        for (var i = 0; i < texts.Length; i++)
        {
            var question = Question(); question["id"] = "boundary_" + i; question["text"] = texts[i]; items.Add(question);
        }
        var result = QuestionPackLoader.Validate(Manifest, new Dictionary<string, string> { ["boundary.json"] = items.ToJsonString() }, "el-GR");
        Assert.Equal("boundary_1", Assert.Single(result.Issues.Where(issue => issue.Code == "similar-text")).QuestionId);
        Assert.Equal("boundary_3", Assert.Single(result.Issues.Where(issue => issue.Code == "duplicate-text")).QuestionId);
    }

    [Fact]
    public void FunFactsAreLoadedIntoQuestionDefinition()
    {
        var q = Question();
        q["funFacts"] = new JsonArray("Γεγονός 1", "Γεγονός 2");
        var result = Validate(q);
        Assert.True(result.Success);
        var def = Assert.Single(result.Pack!.Questions);
        Assert.Equal(2, def.FunFacts.Count);
        Assert.Equal("Γεγονός 1", def.FunFacts[0]);
    }

    [Fact]
    public void InvalidFunFactsAreRejected()
    {
        var q = Question();
        q["funFacts"] = new JsonArray("1", "2", "3", "4", "5", "6");
        var result = Validate(q);
        Assert.False(result.Success);
        Assert.Contains(result.Issues, issue => issue.Code == "fun-facts");
    }

    [Theory]
    [InlineData("id", "id")]
    [InlineData("text", "text")]
    [InlineData("answers", "answers")]
    [InlineData("correctAnswerIndex", "correct-index")]
    [InlineData("categoryId", "category")]
    [InlineData("difficulty", "difficulty")]
    [InlineData("explanation", "explanation")]
    [InlineData("locale", "locale")]
    [InlineData("status", "status")]
    public void MissingRequiredFieldsRejectPack(string field, string code)
    {
        var question = Question(); question.Remove(field);
        var result = Validate(question);
        Assert.False(result.Success);
        Assert.Contains(result.Issues, issue => issue.Code == code && !issue.Warning);
    }

    [Theory]
    [InlineData("correctAnswerIndex", -1, "correct-index")]
    [InlineData("correctAnswerIndex", 4, "correct-index")]
    [InlineData("difficulty", 0, "difficulty")]
    [InlineData("difficulty", 6, "difficulty")]
    public void InvalidIntegersRejectPack(string field, int value, string code)
    { var q = Question(); q[field] = value; Assert.Contains(Validate(q).Issues, issue => issue.Code == code && !issue.Warning); }

    [Fact]
    public void DraftRejectedAndDevelopmentNeverPromotesUnreviewedContent()
    {
        var draft = Question(); draft["status"] = "draft";
        Assert.Contains(Validate(draft).Issues, issue => issue.Code == "unreviewed");
        Assert.False(Validate(draft, false).Success);
        var reviewed = Question(); reviewed["id"] = "other"; reviewed["text"] = "Άλλη ερώτηση";
        var result = QuestionPackLoader.Validate(Manifest, new Dictionary<string,string> { ["mixed.json"] = new JsonArray(draft, reviewed).ToJsonString() }, "el-GR", false);
        Assert.True(result.Success); Assert.Single(result.Pack!.Questions);
    }

    [Theory]
    [InlineData("{bad")]
    [InlineData("null")]
    [InlineData("{}")]
    [InlineData("[null]")]
    [InlineData("[1]")]
    [InlineData("[{\"id\":\"\\uD800\"}]")]
    public void MalformedFilesReturnDiagnosticsWithoutCrashing(string json)
    { var result = QuestionPackLoader.Validate(Manifest, new Dictionary<string,string> { ["bad.json"] = json }, "el-GR"); Assert.False(result.Success); Assert.NotEmpty(result.Issues); }

    [Fact]
    public void DuplicateIdsAndNormalizedTextAcrossFilesAndAnswersAreRejected()
    {
        var first = Question(); var second = Question(); second["text"] = "  ΠΟΙΑ   ΕΙΝΑΙ Η ΠΡΩΤΕΥΟΥΣΑ ΤΗΣ ΕΛΛΑΔΑΣ; ";
        // Exact normalization retains Greek accents; use the same accented text with spacing.
        second["text"] = "  " + first["text"]!.GetValue<string>().Replace(" ", "  ") + " ";
        var result = QuestionPackLoader.Validate(Manifest, new Dictionary<string,string> {
            ["one.json"] = new JsonArray(first).ToJsonString(), ["two.json"] = new JsonArray(second).ToJsonString() }, "el-GR");
        Assert.Contains(result.Issues, issue => issue.Code == "duplicate-id");
        Assert.Contains(result.Issues, issue => issue.Code == "duplicate-text");
        var duplicateAnswers = Question(); duplicateAnswers["answers"] = new JsonArray("Αθήνα", " Αθήνα ", "Πάτρα", "Χανιά");
        Assert.Contains(Validate(duplicateAnswers).Issues, issue => issue.Code == "duplicate-answer");
    }

    [Fact]
    public void WrongTypesUnknownFieldsDuplicateFieldsAndManifestVersionAreRejected()
    {
        var q = Question(); q["difficulty"] = "1"; q["unknown"] = true;
        Assert.False(Validate(q).Success);
        foreach (var manifest in new[] { "null", "{}", Manifest.Replace("\"schemaVersion\":1", "\"schemaVersion\":2"), Manifest.Replace("\"schemaVersion\":1", "\"schemaVersion\":1,\"schemaVersion\":1"), Manifest.Replace("el-GR", "en-US") })
            Assert.False(QuestionPackLoader.Validate(manifest, new Dictionary<string,string> { ["q.json"] = new JsonArray(Question()).ToJsonString() }, "el-GR").Success);
        q = Question(); q["categoryId"] = "missing"; Assert.Contains(Validate(q).Issues, issue => issue.Code == "category");
    }

    [Fact]
    public void SourcesMetadataAndLengthProduceActionableDiagnostics()
    {
        var q = Question(); q.Remove("source"); q["verifiedAt"] = "2020-01-01"; q["text"] = new string('α',301);
        var result = Validate(q);
        Assert.True(result.Success);
        foreach (var code in new[] { "source", "stale", "long-text" }) Assert.Contains(result.Issues, issue => issue.Code == code && issue.Warning);
        q["expiresAfter"] = "not-date"; Assert.False(Validate(q).Success);
        q = Question(); q["text"] = new string('α',2049); Assert.Contains(Validate(q).Issues, issue => issue.Code == "wire-limit" && !issue.Warning);
    }

    [Fact]
    public void FilesystemReaderRejectsInvalidUtf8AndMissingManifest()
    {
        var directory = Path.Combine(Path.GetTempPath(), "quizparty-" + Guid.NewGuid());
        Directory.CreateDirectory(directory);
        try {
            Assert.False(QuestionPackLoader.LoadDirectory(directory, "el-GR").Success);
            File.WriteAllBytes(Path.Combine(directory,"manifest.json"), [0xff,0xfe,0xff]);
            Assert.False(QuestionPackLoader.LoadDirectory(directory, "el-GR").Success);
            File.WriteAllText(Path.Combine(directory,"manifest.json"), Manifest, new UTF8Encoding(false));
            File.WriteAllText(Path.Combine(directory,"q.json"), new JsonArray(Question()).ToJsonString());
            Assert.True(QuestionPackLoader.LoadDirectory(directory,"el-GR").Success);
        } finally { Directory.Delete(directory, true); }
    }
}

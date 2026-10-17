using QuizParty.Infrastructure.Content;

if (args.Length is < 1 or > 3 || args.Skip(1).Any(arg => arg != "--development" && !arg.StartsWith("--locale=", StringComparison.Ordinal)))
{
    Console.Error.WriteLine("Usage: QuestionValidator <pack-directory> [--locale=el-GR] [--development]");
    return 2;
}
var locale = args.FirstOrDefault(arg => arg.StartsWith("--locale=", StringComparison.Ordinal))?[9..] ?? "el-GR";
var result = QuestionPackLoader.LoadDirectory(args[0], locale, !args.Contains("--development"));
foreach (var issue in result.Issues)
    Console.WriteLine($"{(issue.Warning ? "WARNING" : "ERROR")} {issue.File} [{issue.QuestionId}] {issue.Code}: {issue.Message}");
Console.WriteLine(result.Success ? $"PASS: {result.Pack!.Questions.Count} reviewed questions; {result.Pack.Categories.Count} categories; {result.Pack.Locale} {result.Pack.Version}." : "FAIL: pack rejected.");
return result.Success ? 0 : 1;

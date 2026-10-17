using System.Text;
using Godot;
using QuizParty.Core.Questions;
using QuizParty.Infrastructure.Content;

namespace QuizParty.Presentation;

public static class QuestionPackContent
{
    public static QuestionPack Load()
    {
        const string root = "res://Content/el-GR/";
        string Read(string name)
        {
            using var file = global::Godot.FileAccess.Open(root + name, global::Godot.FileAccess.ModeFlags.Read);
            if (file is null || file.GetLength() > QuestionPackLoader.MaxFileBytes) throw new InvalidDataException($"Cannot read bounded content file: {name}");
            return new UTF8Encoding(false, true).GetString(file.GetBuffer((long)file.GetLength())).TrimStart('\uFEFF');
        }
        var names = DirAccess.GetFilesAt(root).Where(name => name.EndsWith(".json", StringComparison.Ordinal) && name != "manifest.json").ToArray();
        if (names.Length > QuestionPackLoader.MaxFiles) throw new InvalidDataException("Too many content files.");
        var result = QuestionPackLoader.Validate(Read("manifest.json"), names.ToDictionary(name => name, Read), "el-GR");
        if (!result.Success) throw new InvalidDataException(string.Join("; ", result.Issues.Where(issue => !issue.Warning).Select(issue => $"{issue.File}/{issue.QuestionId}: {issue.Code}")));
        GD.Print($"CONTENT LOADED locale={result.Pack!.Locale} version={result.Pack.Version} reviewed={result.Pack.Questions.Count}");
        return result.Pack;
    }
}

using System.Xml.Linq;
using Xunit;

namespace QuizParty.IntegrationTests;

public class ProjectConfigurationTests
{
    [Fact]
    public void AndroidTargetPreservesVerifiedFrameworkException()
    {
        var directory = new DirectoryInfo(AppContext.BaseDirectory);
        while (directory is not null && !File.Exists(Path.Combine(directory.FullName, "QuizParty.sln")))
            directory = directory.Parent;
        Assert.NotNull(directory);
        var project = XDocument.Load(Path.Combine(directory.FullName,
            "src", "QuizParty.Godot", "QuizParty.Godot.csproj"));
        var frameworks = project.Descendants("TargetFramework").ToArray();
        Assert.Contains(frameworks, element => element.Attribute("Condition") is null && element.Value == "net8.0");
        Assert.Contains(frameworks, element => element.Attribute("Condition")?.Value.Contains("android") == true && element.Value == "net9.0");
    }
}

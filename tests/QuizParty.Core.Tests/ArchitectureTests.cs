using System.Reflection;
using Xunit;

namespace QuizParty.Core.Tests;

public class ArchitectureTests
{
    [Fact]
    public void CoreAssemblyDoesNotReferenceGodotOrOuterLayers()
    {
        var assembly = Assembly.Load("QuizParty.Core");
        Assert.DoesNotContain(assembly.GetReferencedAssemblies(), reference =>
            reference.Name!.StartsWith("Godot", StringComparison.Ordinal) ||
            reference.Name.StartsWith("QuizParty.Infrastructure", StringComparison.Ordinal) ||
            reference.Name.StartsWith("QuizParty.Godot", StringComparison.Ordinal));
    }
}

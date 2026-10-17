using GdUnit4;
using Godot;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class FoundationSceneTests
{
    [TestCase]
    [RequireGodotRuntime]
    public void StartupSceneLoadsAndUsesResponsiveContainers()
    {
        var scene = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn");
        AssertThat(scene).IsNotNull();
        using var root = scene.Instantiate<Control>();
        AssertThat(root.GetNodeOrNull<CenterContainer>("Center")).IsNotNull();
        AssertThat(root.GetNode<Label>("Center/Content/Title").Text).IsEqual("APP_TITLE");
        AssertThat(root.GetNode<Label>("Center/Content/Status").Text).IsEqual("SETUP_READY");
        root.Free();
    }
}

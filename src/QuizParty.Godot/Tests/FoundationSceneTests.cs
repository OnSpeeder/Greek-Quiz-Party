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
        AssertThat(root.GetNode<Button>("Center/Content/LanSpike").CustomMinimumSize.Y >= 64).IsTrue();
        root.Free();
    }

    [TestCase]
    [RequireGodotRuntime]
    public void SpikeSceneSeparatesTransportAndHasTouchSizedControls()
    {
        var scene = ResourceLoader.Load<PackedScene>("res://Scenes/LanSpike.tscn");
        using var root = scene.Instantiate<Control>();
        AssertThat(root.GetNodeOrNull<Networking.LanSpikeTransport>("Transport")).IsNotNull();
        AssertThat(root.GetNode<Button>("Margin/Scroll/Content/Send").Disabled).IsTrue();
        AssertThat(root.GetNode<LineEdit>("Margin/Scroll/Content/Address").MaxLength).IsEqual(253);
        foreach (var name in new[] { "Host", "Join", "Send", "Disconnect", "Back" })
            AssertThat(root.GetNode<Button>("Margin/Scroll/Content/" + name).CustomMinimumSize.Y >= 64).IsTrue();
        root.Free();
    }
}

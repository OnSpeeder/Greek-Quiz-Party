using GdUnit4;
using Godot;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class FoundationSceneTests
{
    [TestCase]
    [RequireGodotRuntime]
    public void LobbyInitializesTouchSettingsAndRestoresRelayAfterSceneExit()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        var multiplayer = (SceneMultiplayer)tree.Root.Multiplayer;
        var previousRelay = multiplayer.ServerRelay;
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        AssertThat(multiplayer.ServerRelay).IsFalse();
        const string path = "Margin/Scroll/Content/MatchSettings/";
        var length = root.GetNode<OptionButton>(path + "Length");
        AssertThat(length.ItemCount).IsEqual(4);
        AssertThat(length.GetSelectedId()).IsEqual(1);
        AssertThat(length.CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(root.GetNode<OptionButton>(path + "Duration").GetSelectedId()).IsEqual(20);
        root.Free();
        AssertThat(multiplayer.ServerRelay).IsEqual(previousRelay);
    }

    [TestCase]
    [RequireGodotRuntime]
    public void MatchPanelComposesWithLobbyAndKeepsAnswersTouchSized()
    {
        var scene = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn");
        using var root = scene.Instantiate<Control>();
        var panel = root.GetNode<Presentation.MatchPanel>("Margin/Scroll/Content/MatchPanel");
        AssertThat(panel.Visible).IsFalse();
        for (var index = 0; index < 4; index++)
            AssertThat(panel.GetNode<Button>($"Answer{index}").CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(panel.GetNode<Button>("Continue").CustomMinimumSize.Y >= 64).IsTrue();
        root.Free();
    }

    [TestCase]
    [RequireGodotRuntime]
    public void LobbySceneSeparatesTransportAndBoundsTouchInputs()
    {
        var scene = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn");
        using var root = scene.Instantiate<Control>();
        AssertThat(root.GetNodeOrNull<Networking.LobbyTransport>("Transport")).IsNotNull();
        AssertThat(root.GetNodeOrNull<ScrollContainer>("Margin/Scroll")).IsNotNull();
        const string path = "Margin/Scroll/Content/";
        AssertThat(root.GetNode<LineEdit>(path + "PlayerName").MaxLength).IsEqual(32);
        AssertThat(root.GetNode<LineEdit>(path + "RoomName").MaxLength).IsEqual(32);
        AssertThat(root.GetNode<LineEdit>(path + "Address").MaxLength).IsEqual(253);
        AssertThat(root.GetNode<Button>(path + "Start").Disabled).IsTrue();
        foreach (var name in new[] { "Host", "Join", "Ready", "Start", "Disconnect", "Back" })
            AssertThat(root.GetNode<Button>(path + name).CustomMinimumSize.Y >= 64).IsTrue();
        root.Free();
    }

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

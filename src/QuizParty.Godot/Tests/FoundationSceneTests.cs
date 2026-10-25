using GdUnit4;
using Godot;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class FoundationSceneTests
{
    [TestCase]
    [RequireGodotRuntime]
    public async Task SharedDeviceHandoffHidesPreviousPlayerAndPreservesIndependentInputs()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            var transport = root.GetNode<Networking.LobbyTransport>("Transport");
            transport.DiscoveryPort = 19992;
            AssertThat(transport.Host("Local test", "Host", 19991)).IsEqual(Error.Ok);
            const string prefix = "Margin/Scroll/Content/";
            var editor = root.GetNode<Presentation.RosterEditor>(prefix + "RosterEditor");
            AssertThat(editor.GetNode<Button>("AddLocal").CustomMinimumSize.Y >= 64).IsTrue();
            editor.GetNode<LineEdit>("LocalName").Text = "Ελένη";
            editor.GetNode<Button>("AddLocal").EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.OwnedPlayers.Count).IsEqual(2);
            AssertThat(transport.OwnedPlayers.Single(p => p.LocalSlot == 1).Ready).IsFalse();
            transport.SetReady(true, localSlot: 1);
            editor.GetNode<CheckButton>("Teams").ButtonPressed = true;
            AssertThat(transport.Snapshot!.TeamMode).IsTrue(); transport.SetReady(true); transport.StartGame();
            var match = root.GetNode<Presentation.MatchPanel>(prefix + "MatchPanel");
            var controllers = match.GetNode<Presentation.LocalControllerPanel>("QuestionLayout/HostRail/LocalControllers");
            var strategy = match.GetNode<Presentation.StrategyPanel>("QuestionLayout/QuestionContent/Strategy");
            AssertThat(controllers.Open).IsFalse(); AssertThat(strategy.Visible).IsFalse();
            AssertThat(match.GetNode<Button>("QuestionLayout/QuestionContent/Answers/Answer0").Visible).IsFalse();
            controllers.FindChildren("*", "Button", true, false).OfType<Button>().First().EmitSignal(Button.SignalName.Pressed);
            AssertThat(controllers.Open).IsTrue(); AssertThat(strategy.Visible).IsTrue();
            strategy.GetNode<Button>("Top/Bets/Bet3").EmitSignal(Button.SignalName.Pressed);
            var correct = 0; // Handoff verifies independent submissions, regardless of the selected content.
            match.GetNode<Button>($"QuestionLayout/QuestionContent/Answers/Answer{correct}").EmitSignal(Button.SignalName.Pressed);
            AssertThat(controllers.Open).IsFalse(); AssertThat(strategy.Visible).IsFalse();
            AssertThat(transport.AnswerForSlot(0)).IsEqual(correct); AssertThat(transport.AnswerForSlot(1)).IsNull();
            controllers.FindChildren("*", "Button", true, false).OfType<Button>().Single(b => b.Text.Contains("Ελένη", StringComparison.Ordinal)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.ActiveSlot).IsEqual(1); AssertThat(controllers.Open).IsTrue();
            AssertThat(strategy.Confidence).IsEqual(1);
            AssertThat(transport.MatchSnapshot!.Private!.PlayerId).IsEqual(transport.OwnedPlayers.Single(p => p.LocalSlot == 1).PlayerId);
            match.GetNode<Button>($"QuestionLayout/QuestionContent/Answers/Answer{correct}").EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.AnswerForSlot(0)).IsEqual(correct); AssertThat(transport.AnswerForSlot(1)).IsEqual(correct);
            await root.ToSignal(tree.CreateTimer(0.15), global::Godot.Timer.SignalName.Timeout);
            AssertThat(transport.MatchSnapshot!.Phase).IsEqual("AnswerReveal"); transport.AdvanceMatch();
            controllers.FindChildren("*", "Button", true, false).OfType<Button>().Single(b => b.Text.Contains("Ελένη", StringComparison.Ordinal)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(controllers.Open).IsTrue(); AssertThat(strategy.Visible).IsTrue();
            transport.SelectLocalPlayer(0); AssertThat(controllers.Open).IsFalse(); AssertThat(strategy.Visible).IsFalse();
            strategy.Render(transport.MatchSnapshot!);
            strategy.GetNode<Button>("Top/Privacy").EmitSignal(Button.SignalName.Pressed);
            AssertThat(((VBoxContainer)strategy.FindChild("Private", true, false)).Visible).IsTrue();
            strategy.Render(transport.MatchSnapshot! with { SessionId = Guid.NewGuid() });
            AssertThat(((VBoxContainer)strategy.FindChild("Private", true, false)).Visible).IsFalse();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task StrategyRendersPersonalCardsAndUsesSafeConfidenceWhenDisabledOrTied()
    {
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<Control>();
        ((SceneTree)Engine.GetMainLoop()).Root.AddChild(root);
        var panel = root.GetNode<Presentation.StrategyPanel>("Margin/Scroll/Content/MatchPanel/QuestionLayout/QuestionContent/Strategy");
        var owner = Guid.NewGuid();
        var snapshot = new Infrastructure.Networking.MatchSnapshotDto(Guid.NewGuid(), 1, "QuestionActive", 0,
            new(Guid.NewGuid(), "Test", ["a", "b", "c", "d"], "history", 1, 0, TimeSpan.TicksPerSecond * 20),
            0, [new(owner, "Player", 1000)], null, 4, 10, 2, false, [owner], [], false, [],
            new(true, true, true, true, false), new(owner, [new(Guid.NewGuid(), 0), new(Guid.NewGuid(), 2)], [],
                TimeSpan.TicksPerSecond * 20, false, false, 3, 30, new(0, 3, 1, false), [], "None"), []);
        panel.Render(snapshot);
        var personal = panel.GetNode<VBoxContainer>("Private");
        AssertThat(personal.Visible).IsFalse();
        panel.GetNode<Button>("Top/Privacy").EmitSignal(Button.SignalName.Pressed);
        AssertThat(personal.Visible).IsTrue();
        var cards = personal.FindChildren("*", "Button", true, false).OfType<Button>().ToArray();
        AssertThat(panel.GetNode<OptionButton>("Top/Confidence").Visible).IsFalse();
        AssertThat(panel.GetNode<Button>("Top/Bets/Bet3").CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(panel.GetNode<Button>("Top/Bets/Bet3").AutowrapMode).IsEqual(TextServer.AutowrapMode.Off);
        AssertThat(cards.Length).IsEqual(2);
        AssertThat(cards.All(c => !c.Disabled && c.CustomMinimumSize.Y >= 64)).IsTrue();
        AssertThat(personal.FindChildren("*", "Label", true, false).Count >= 4).IsTrue();
        panel.GetNode<OptionButton>("Top/Confidence").Select(2); AssertThat(panel.Confidence).IsEqual(3);
        panel.Render(snapshot with { Strategy = null, Private = null });
        AssertThat(panel.Visible).IsFalse(); AssertThat(panel.Confidence).IsEqual(1);
        panel.Render(snapshot with { IsTieBreaker = true });
        AssertThat(panel.Confidence).IsEqual(1);
        AssertThat(personal.FindChildren("*", "Button", true, false).Any()).IsFalse();
        root.Free();
        var tree = (SceneTree)Engine.GetMainLoop();
        await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
    }

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
        var transport = root.GetNode<Networking.LobbyTransport>("Transport");
        var setup = root.GetNode<Presentation.MatchSetupPanel>("PresentationShell/MatchSetup");
        setup.ShowPage("setup");
        var choices = setup.FindChildren("Value*", "Button", true, false).OfType<Button>().ToArray();
        AssertThat(choices.Length).IsEqual(13); // Seven question counts and six timers.
        AssertThat(choices.All(b => b.CustomMinimumSize.Y >= 64)).IsTrue();
        AssertThat(choices.Single(b => b.Name == "Value1").ButtonPressed).IsTrue();
        AssertThat(transport.QuestionSeconds).IsEqual(20);
        AssertThat(((CheckButton)setup.FindChild("Strategy", true, false)).ButtonPressed).IsTrue();
        AssertThat(transport.AllowSteal).IsFalse();
        var strategy = root.GetNode<Presentation.StrategyPanel>("Margin/Scroll/Content/MatchPanel/QuestionLayout/QuestionContent/Strategy");
        AssertThat(strategy.GetNode<OptionButton>("Top/Confidence").ItemCount).IsEqual(3);
        AssertThat(strategy.GetNode<OptionButton>("Top/Confidence").CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(strategy.GetNode<Button>("Top/Privacy").CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(((VBoxContainer)strategy.FindChild("Private", true, false)).Visible).IsFalse();
        strategy.GetNode<OptionButton>("Top/Confidence").Select(2);
        AssertThat(strategy.Confidence).IsEqual(1); // Hidden/inactive strategy must always submit Safe.
        var pin = root.GetNode<LineEdit>("Margin/Scroll/Content/RoomPin");
        AssertThat(pin.Secret).IsTrue(); AssertThat(pin.MaxLength).IsEqual(6);
        AssertThat(pin.CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(root.GetNode<Button>("Margin/Scroll/Content/JoinFlow/RoomBrowser/Header/Refresh").CustomMinimumSize.Y >= 64).IsTrue();
        AssertThat(root.GetNodeOrNull<Networking.LanDiscovery>("Transport/Discovery")).IsNotNull();
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
            AssertThat(panel.GetNode<Button>($"Answers/Answer{index}").CustomMinimumSize.Y >= 64).IsTrue();
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
        AssertThat(root.GetNodeOrNull<ScrollContainer>("Center")).IsNotNull();
        AssertThat(root.GetNode<Label>("Center/Frame/Content/Title").Text).IsEqual("APP_TITLE");
        AssertThat(root.GetNode<Label>("Center/Frame/Content/Status").Text).IsEqual("UI_WELCOME");
        AssertThat(root.GetNode<Button>("Center/Frame/Content/LanSpike").CustomMinimumSize.Y >= 64).IsTrue();
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

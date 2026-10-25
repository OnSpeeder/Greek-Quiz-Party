using GdUnit4;
using Godot;
using QuizParty.Networking;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class MatchSetupTests
{
    [TestCase]
    public void DirectedDiscoveryUsesActualSubnetAndRejectsInvalidInterfaces()
    {
        AssertThat(LanDiscovery.SubnetBroadcast(System.Net.IPAddress.Parse("192.168.68.105"), System.Net.IPAddress.Parse("255.255.255.0"))).IsEqual("192.168.68.255");
        AssertThat(LanDiscovery.SubnetBroadcast(System.Net.IPAddress.Parse("10.20.3.4"), System.Net.IPAddress.Parse("255.255.0.0"))).IsEqual("10.20.255.255");
        AssertThat(LanDiscovery.SubnetBroadcast(System.Net.IPAddress.Loopback, System.Net.IPAddress.Parse("255.0.0.0"))).IsNull();
        AssertThat(LanDiscovery.SubnetBroadcast(System.Net.IPAddress.Parse("169.254.1.2"), System.Net.IPAddress.Parse("255.255.0.0"))).IsNull();
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task HostStartsUnreadyThreeColumnRosterAndFullSelectionPagesApplyToTransport()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>();
        tree.Root.AddChild(root);
        try
        {
            var transport = root.GetNode<LobbyTransport>("Transport"); transport.DiscoveryPort = 19772;
            AssertThat(transport.Host("Δοκιμή", "Φίλιππος", 19771)).IsEqual(Error.Ok);
            AssertThat(transport.OwnedPlayers.Single().Ready).IsFalse();
            transport.AddLocalPlayer("Ελένη", 1); transport.SetReady(true, localSlot: 1);
            transport.StartGame(); AssertThat(transport.MatchSnapshot).IsNull();
            var roster = root.GetNode<GridContainer>("Margin/Scroll/Content/RosterEditor/Players");
            AssertThat(roster.Columns).IsEqual(3);
            var ready = roster.FindChildren("*", "Button", true, false).OfType<Button>().First();
            AssertThat(ready.Text).IsEqual(""); AssertThat(ready.GetChildCount() > 0).IsTrue();
            ready.EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.OwnedPlayers.Single(p => p.IsHost).Ready).IsTrue();
            root.GetNode<Button>("PresentationShell/LobbyActions/GameSetup").EmitSignal(Button.SignalName.Pressed);
            var panel = root.GetNode<MatchSetupPanel>("PresentationShell/MatchSetup");
            AssertThat(panel.Visible).IsTrue(); AssertThat(root.GetNode<Control>("Margin").Visible).IsFalse();
            var difficulty = (Button)panel.FindChild("DifficultyLOW", true, false); difficulty.ButtonPressed = false;
            AssertThat(transport.EnabledDifficulties.SetEquals([3, 4, 5])).IsTrue();
            panel.ShowPage("categories");
            ((Button)panel.FindChild("None", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.EnabledCategories!.Count).IsEqual(0);
            ((Button)panel.FindChild("All", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.EnabledCategories.Count).IsEqual(12);
            panel.ShowPage("cards");
            ((Button)panel.FindChild("None", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.EnabledCards.Count).IsEqual(0);
            ((Button)panel.FindChild("Steal", true, false)).ButtonPressed = true;
            AssertThat(transport.AllowSteal).IsTrue(); AssertThat(transport.EnabledCards.Count).IsEqual(1);
            panel.ShowPage("missions");
            ((Button)panel.FindChild("None", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.EnabledMissions.Count).IsEqual(0);
            AssertThat(panel.Back()).IsTrue(); AssertThat(panel.CurrentPage).IsEqual("setup");
            AssertThat(panel.Back()).IsTrue(); AssertThat(root.GetNode<Control>("Margin").Visible).IsTrue();
            root.OpenMatchPage("rules"); AssertThat(panel.CurrentPage).IsEqual("rules");
            panel.Back();
            foreach (var id in transport.QuestionCategories.Select(c => c.Id)) AssertThat(LobbyIcons.Texture(id)).IsNotNull();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }
    [TestCase]
    [RequireGodotRuntime]
    public async Task DragStartingOnButtonScrollsPageWithoutActivatingButton()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var scroll = new ScrollContainer { Size = new(280, 180), HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled };
        tree.Root.AddChild(scroll);
        var column = new VBoxContainer { SizeFlagsHorizontal = Control.SizeFlags.ExpandFill }; scroll.AddChild(column);
        var clicked = 0;
        for (var i = 0; i < 6; i++)
        {
            var button = new Button { Text = "Test", CustomMinimumSize = new(200, 100) };
            button.Pressed += () => clicked++; column.AddChild(button);
        }
        scroll.AddChild(new PageDragScroll());
        try
        {
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
            var start = scroll.GlobalPosition + new Vector2(100, 75);
            using var press = new InputEventMouseButton { Position = start, GlobalPosition = start, ButtonIndex = MouseButton.Left, Pressed = true };
            scroll.GetViewport().PushInput(press, true);
            using var move = new InputEventMouseMotion { Position = start - new Vector2(0, 60), GlobalPosition = start - new Vector2(0, 60), Relative = new(0, -60), ButtonMask = MouseButtonMask.Left };
            scroll.GetViewport().PushInput(move, true);
            using var release = new InputEventMouseButton { Position = move.Position, GlobalPosition = move.GlobalPosition, ButtonIndex = MouseButton.Left };
            scroll.GetViewport().PushInput(release, true);
            AssertThat(scroll.ScrollVertical > 0).IsTrue(); AssertThat(clicked).IsEqual(0);
        }
        finally { scroll.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }

}

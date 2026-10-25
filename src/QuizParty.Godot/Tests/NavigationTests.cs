using GdUnit4;
using Godot;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class NavigationTests
{
    [TestCase]
    [RequireGodotRuntime]
    public async Task HomeBackOpensModalNoAndRepeatedBackRestoreHomeAndFocus()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = GD.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            var exit = shell.GetNode<Button>("Exit");
            AssertThat(exit.Text).IsEqual(""); AssertThat(exit.Icon).IsNotNull();
            AssertThat(exit.AccessibilityName.Length > 0).IsTrue();
            AssertThat(tree.QuitOnGoBack).IsFalse();
            shell.Notification((int)Node.NotificationWMGoBackRequest);
            AssertThat(shell.ExitConfirmationOpen).IsTrue();
            AssertThat(root.GetNode<Control>("Center").Visible).IsFalse();
            var modal = shell.GetNode<ExitConfirmation>("ExitConfirmation");
            var no = (Button)modal.FindChild("No", true, false);
            AssertThat(no.HasFocus()).IsTrue();
            for (var i = 0; i < 4; i++)
            {
                using var tab = new InputEventKey { Keycode = Key.Tab, PhysicalKeycode = Key.Tab, Pressed = true };
                root.GetViewport().PushInput(tab, true);
                await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
                AssertThat(modal.IsAncestorOf(root.GetViewport().GuiGetFocusOwner())).IsTrue();
            }
            no.EmitSignal(Button.SignalName.Pressed);
            AssertThat(shell.ExitConfirmationOpen).IsFalse();
            AssertThat(root.GetNode<Control>("Center").Visible).IsTrue();
            AssertThat(exit.HasFocus()).IsTrue();
            exit.EmitSignal(Button.SignalName.Pressed);
            AssertThat(shell.ExitConfirmationOpen).IsTrue();
            shell.NavigateBack();
            AssertThat(shell.ExitConfirmationOpen).IsFalse();
            shell.OpenSettings(); shell.NavigateBack();
            AssertThat(shell.SettingsOpen).IsFalse(); AssertThat(shell.ExitConfirmationOpen).IsFalse();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task ConfirmationOnlyConfirmsOnYesAndFitsBothOrientations()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = new Control(); tree.Root.AddChild(root);
        var modal = new ExitConfirmation(); root.AddChild(modal);
        var confirmed = 0; var cancelled = 0;
        modal.Confirmed += () => confirmed++; modal.Cancelled += () => cancelled++;
        try
        {
            AssertThat(ProjectSettings.GetSetting("display/window/handheld/orientation").AsInt32()).IsEqual(1);
            foreach (var size in new[] { new Vector2(480, 800), new Vector2(1152, 648), new Vector2(480, 800) })
            {
                root.Size = size; modal.Open();
                for (var i = 0; i < 4; i++) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
                var card = (Control)modal.FindChild("Card", true, false);
                AssertThat(card.GetGlobalRect().End.X <= size.X).IsTrue();
                AssertThat(card.GetGlobalRect().End.Y <= size.Y).IsTrue();
                AssertThat(confirmed).IsEqual(0);
            }
            ((Button)modal.FindChild("No", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(cancelled).IsEqual(1); AssertThat(confirmed).IsEqual(0);
            ((Button)modal.FindChild("Yes", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(confirmed).IsEqual(1);
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task LobbyBackClosesOptionsAndMatchBackOpensSettingsWithoutDisconnecting()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>();
        tree.Root.AddChild(root);
        const string path = "Margin/Scroll/Content/";
        try
        {
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            root.ShowSetupPage("join");
            var flow = root.GetNode<JoinFlow>(path + "JoinFlow");
            flow.ChooseRoom(new("127.0.0.1", new("quiz-host", Infrastructure.Networking.LobbyProtocol.Version, Guid.NewGuid(), Guid.NewGuid(), "Test", 19993, 1, 8, true, Infrastructure.Networking.LobbyProtocol.AppVersion, "Lobby"), TimeSpan.Zero));
            AssertThat(flow.PinOpen).IsTrue();
            shell.NavigateBack();
            AssertThat(flow.PinOpen).IsFalse();
            AssertThat(root.GetNode<RoomBrowser>(path + "JoinFlow/RoomBrowser").Visible).IsTrue();
            root.ShowSetupPage("create");
            var creation = root.GetNode<RoomCreationPanel>(path + "CreateRoom");
            AssertThat(((LineEdit)creation.FindChild("RoomPin", true, false)).IsVisibleInTree()).IsTrue();
            ((Button)creation.FindChild("Create", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(creation.IdentityOpen).IsTrue();
            shell.NavigateBack(); AssertThat(creation.IdentityOpen).IsFalse();
            AssertThat(((LineEdit)creation.FindChild("RoomPin", true, false)).IsVisibleInTree()).IsTrue();
            var transport = root.GetNode<Networking.LobbyTransport>("Transport");
            transport.DiscoveryPort = 19994;
            AssertThat(transport.Host("Navigation", "Host", 19993)).IsEqual(Error.Ok);
            transport.AddLocalPlayer("Guest", 1); transport.SetReady(true, localSlot: 1); transport.SetReady(true); transport.StartGame();
            AssertThat(transport.MatchSnapshot).IsNotNull();
            shell.NavigateBack(); AssertThat(shell.SettingsOpen).IsTrue();
            AssertThat(transport.MatchSnapshot).IsNotNull();
            shell.NavigateBack(); AssertThat(shell.SettingsOpen).IsFalse();
            AssertThat(shell.ExitConfirmationOpen).IsFalse();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }
}

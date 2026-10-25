using GdUnit4;
using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class JoinFlowTests
{
    [TestCase]
    public void PresentationPreviewFlagsNeverStartAnUnrequestedMatchConnection()
    {
        AssertThat(MatchProcessProbe.ShouldRun(["--match-ui-preview", "--match-ui-join", "--match-ui-landscape"])).IsFalse();
        AssertThat(MatchProcessProbe.ShouldRun(["--match-host"])).IsTrue();
        AssertThat(MatchProcessProbe.ShouldRun(["--match-join=127.0.0.1"])).IsTrue();
        AssertThat(MatchProcessProbe.ShouldRun(["--match-mixed", "--match-host"])).IsFalse();
    }
    private static DiscoveredRoom Room(int port, Guid session, bool pin = true) => new("127.0.0.1",
        new("quiz-host", LobbyProtocol.Version, Guid.NewGuid(), session, "Αίθουσα δοκιμής", port, 1, 8, pin, LobbyProtocol.AppVersion, "Lobby"), TimeSpan.Zero);

    private static async Task Wait(SceneTree tree, Func<bool> predicate)
    {
        var until = global::Godot.Time.GetTicksMsec() + 5000;
        while (!predicate() && global::Godot.Time.GetTicksMsec() < until) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        AssertThat(predicate()).IsTrue();
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task EightCharactersDisableTakenChoicesAndKeepSelectionsStableOnRefresh()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var picker = new CharacterPicker(); tree.Root.AddChild(picker);
        try
        {
            AssertThat(picker.GetChildren().OfType<Button>().Count()).IsEqual(8);
            picker.Select(6); picker.SetTaken([0, 1]); AssertThat(picker.Selected).IsEqual(6);
            AssertThat(picker.GetNode<Button>("Character0").Disabled).IsTrue();
            picker.Select(0); AssertThat(picker.Selected).IsEqual(6);
            picker.SetTaken([0, 1, 6]); AssertThat(picker.Selected).IsNull();
            AssertThat(picker.GetNode<Button>("Character6").Modulate.R < 1).IsTrue();
            for (var i = 0; i < 8; i++) AssertThat(GameArt.AvatarTexture(i)).IsNotNull();
        }
        finally { picker.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task PinPopupReturnsToRoomsOnWrongPinThenIdentityShowsLiveTakenCharactersAndJoinsOverEnet()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var hostRoot = new Control { Name = "JoinTestHost" }; tree.Root.AddChild(hostRoot);
        var hostApi = new SceneMultiplayer(); tree.SetMultiplayer(hostApi, hostRoot.GetPath());
        var host = new LobbyTransport { Name = "Transport", DiscoveryPort = 19882 }; hostRoot.AddChild(host);
        using var clientRoot = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>();
        clientRoot.Name = "JoinTestClient";
        var clientApi = new SceneMultiplayer(); tree.SetMultiplayer(clientApi, new("/root/JoinTestClient"));
        tree.Root.AddChild(clientRoot);
        var client = clientRoot.GetNode<LobbyTransport>("Transport");
        var flow = clientRoot.GetNode<JoinFlow>("Margin/Scroll/Content/JoinFlow");
        try
        {
            AssertThat(host.Host("Αίθουσα δοκιμής", "Host", 19881, "1234", 5)).IsEqual(Error.Ok);
            clientRoot.ShowSetupPage("join");
            flow.ChooseRoom(Room(19881, host.Snapshot!.SessionId));
            AssertThat(flow.PinOpen).IsTrue();
            var popup = clientRoot.GetNode<Control>("PresentationShell/PinPopup");
            var pin = (LineEdit)popup.FindChild("Pin", true, false);
            var submit = (Button)popup.FindChild("Confirm", true, false);
            pin.Text = "0000"; submit.EmitSignal(Button.SignalName.Pressed);
            await Wait(tree, () => flow.GetNode<Label>("Message").Visible && flow.GetNode<Label>("Message").Text.Contains("PIN", StringComparison.Ordinal));
            AssertThat(flow.IdentityOpen).IsFalse(); AssertThat(flow.PinOpen).IsFalse();
            AssertThat(host.Snapshot.Players.Length).IsEqual(1);
            flow.ChooseRoom(Room(19881, host.Snapshot.SessionId)); pin.Text = "1234"; submit.EmitSignal(Button.SignalName.Pressed);
            await Wait(tree, () => flow.IdentityOpen);
            AssertThat(host.Snapshot.Players.Length).IsEqual(1);
            var picker = flow.GetNode<CharacterPicker>("Identity/CharacterScroll/Characters");
            AssertThat(picker.GetNode<Button>("Character5").Disabled).IsTrue();
            flow.GetNode<LineEdit>("Identity/PlayerName").Text = "Ελένη"; picker.Select(7);
            AssertThat(flow.GetNode<Button>("Identity/JoinLobby").Text).IsEqual("");
            flow.GetNode<Button>("Identity/JoinLobby").EmitSignal(Button.SignalName.Pressed);
            await Wait(tree, () => client.LocalPlayerId is not null);
            AssertThat(client.OwnedPlayers.Single().CharacterId).IsEqual(7);
            AssertThat(host.Snapshot.Players.Length).IsEqual(2);
        }
        finally
        {
            clientRoot.Free(); hostRoot.Free();
            tree.SetMultiplayer(null!, new("/root/JoinTestClient")); tree.SetMultiplayer(null!, new("/root/JoinTestHost"));
            clientApi.Dispose(); hostApi.Dispose();
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }
}

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
    [RequireGodotRuntime]
    public async Task RejectingSavedGameDeliversAQueuedDepartureToTheHost()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        var directory = System.IO.Path.Combine(System.IO.Path.GetTempPath(), "quizparty-rejoin-test-" + Guid.NewGuid().ToString("N"));
        using var hostRoot = new Control { Name = "DepartureHost" }; tree.Root.AddChild(hostRoot);
        using var clientRoot = new Control { Name = "DepartureClient" }; tree.Root.AddChild(clientRoot);
        using var managerRoot = new Control { Name = "DepartureManager" }; tree.Root.AddChild(managerRoot);
        var hostApi = new SceneMultiplayer(); var clientApi = new SceneMultiplayer();
        tree.SetMultiplayer(hostApi, hostRoot.GetPath()); tree.SetMultiplayer(clientApi, clientRoot.GetPath());
        var hostLobby = new Node { Name = "Lobby" }; hostRoot.AddChild(hostLobby);
        var clientLobby = new Node { Name = "Lobby" }; clientRoot.AddChild(clientLobby);
        var host = new LobbyTransport { Name = "Transport", DiscoveryPort = 19962 }; hostLobby.AddChild(host);
        var client = new LobbyTransport { Name = "Transport" }; clientLobby.AddChild(client);
        try
        {
            host.UseSyntheticQuestions(1); host.StrategyEnabled = false;
            AssertThat(host.Host("Room", "Host", 19961)).IsEqual(Error.Ok);
            AssertThat(client.Join("127.0.0.1", "Phone", 19961)).IsEqual(Error.Ok);
            await Wait(tree, () => client.LocalPlayerId is not null);
            client.SetReady(true); host.SetReady(true);
            await Wait(tree, () => host.Snapshot?.Players.All(p => p.Ready) == true);
            host.StartGame(); await Wait(tree, () => client.MatchSnapshot is not null);
            var ticket = client.CurrentTicket!; client.Stop(); await Wait(tree, () => host.MatchSnapshot?.IsPaused == true);
            var store = new RejoinStore(directory); store.Save(ticket);
            var manager = new RejoinCoordinator { Name = "Manager", EnableForTests = true, StoreOverride = store }; managerRoot.AddChild(manager);
            var dialog = manager.GetNode<MatchDialog>("RejoinLayer/RejoinPrompt");
            AssertThat(dialog.Visible).IsTrue();
            dialog.Actions.GetNode<Button>("Leave").EmitSignal(Button.SignalName.Pressed);
            AssertThat(dialog.Visible).IsFalse(); AssertThat(store.Load()).IsNull();
            await Wait(tree, () => host.Snapshot?.Players.Length == 1 && store.Pending().Count == 0, 10000);
            AssertThat(host.MatchSnapshot!.Scores.Length).IsEqual(2);
        }
        finally
        {
            managerRoot.Free(); clientRoot.Free(); hostRoot.Free();
            tree.SetMultiplayer(null!, new("/root/DepartureClient")); tree.SetMultiplayer(null!, new("/root/DepartureHost"));
            clientApi.Dispose(); hostApi.Dispose();
            if (System.IO.Directory.Exists(directory)) System.IO.Directory.Delete(directory, true);
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task FreshTransportCanRejoinAndAnExplicitDepartureRevokesItsSeat()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var hostRoot = new Control { Name = "RestartHost" }; tree.Root.AddChild(hostRoot);
        using var clientRoot = new Control { Name = "RestartClient" }; tree.Root.AddChild(clientRoot);
        var hostApi = new SceneMultiplayer(); var clientApi = new SceneMultiplayer();
        tree.SetMultiplayer(hostApi, hostRoot.GetPath()); tree.SetMultiplayer(clientApi, clientRoot.GetPath());
        var host = new LobbyTransport { Name = "Transport", DiscoveryPort = 19952 }; hostRoot.AddChild(host);
        var client = new LobbyTransport { Name = "Transport" }; clientRoot.AddChild(client);
        try
        {
            host.UseSyntheticQuestions(1); host.StrategyEnabled = false;
            AssertThat(host.Host("Room", "Host", 19951)).IsEqual(Error.Ok);
            AssertThat(client.Join("127.0.0.1", "Phone", 19951)).IsEqual(Error.Ok);
            await Wait(tree, () => client.LocalPlayerId is not null);
            client.SetReady(true); host.SetReady(true);
            await Wait(tree, () => host.Snapshot?.Players.All(p => p.Ready) == true);
            host.StartGame(); await Wait(tree, () => client.MatchSnapshot is not null);
            var ticket = client.CurrentTicket!; var original = client.LocalPlayerId;
            AssertThat(ticket.IsValid).IsTrue(); client.Stop();
            await Wait(tree, () => host.MatchSnapshot?.IsPaused == true);
            client.Free();
            var fresh = new LobbyTransport { Name = "Transport" }; clientRoot.AddChild(fresh);
            AssertThat(fresh.Resume(ticket)).IsTrue();
            await Wait(tree, () => fresh.MatchSnapshot is not null, 8000);
            AssertThat(fresh.LocalPlayerId).IsEqual(original);
            fresh.Stop(); await Wait(tree, () => host.MatchSnapshot?.DisconnectedPlayers?.Contains(original!.Value) == true);
            var delivered = false;
            fresh.StatusChanged += status => { if (status == "DepartureDelivered") delivered = true; };
            AssertThat(fresh.DeliverDeparture(ticket)).IsEqual(Error.Ok);
            await Wait(tree, () => delivered, 8000);
            AssertThat(host.Snapshot!.Players.Length).IsEqual(1);
            AssertThat(host.MatchSnapshot!.Scores.Length).IsEqual(2);
        }
        finally
        {
            clientRoot.Free(); hostRoot.Free(); tree.SetMultiplayer(null!, new("/root/RestartClient")); tree.SetMultiplayer(null!, new("/root/RestartHost"));
            clientApi.Dispose(); hostApi.Dispose(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }

    [TestCase]
    [RequireGodotRuntime]
    public void RejoinTicketSurvivesReloadAndDepartureIsDurable()
    {
        var directory = System.IO.Path.Combine(System.IO.Path.GetTempPath(), "quizparty-rejoin-test-" + Guid.NewGuid().ToString("N"));
        try
        {
            var ticket = new RejoinTicket(Guid.NewGuid(), Guid.NewGuid(), Guid.NewGuid(), new string('A', 64), "127.0.0.1", 7777);
            var store = new RejoinStore(directory); store.Save(ticket);
            AssertThat(new RejoinStore(directory).Load()).IsEqual(ticket);
            store.QueueDeparture(ticket);
            AssertThat(store.Load()).IsNull(); AssertThat(new RejoinStore(directory).Pending().Single()).IsEqual(ticket);
            store.QueueDeparture(ticket); AssertThat(store.Pending().Count).IsEqual(1);
            store.RemovePending(ticket); AssertThat(store.Pending().Count).IsEqual(0);
        }
        finally { if (System.IO.Directory.Exists(directory)) System.IO.Directory.Delete(directory, true); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task HostSeesPauseAndCanResumeAfterPlayerDisconnects()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var hostRoot = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>();
        hostRoot.Name = "PauseTestHost";
        var hostApi = new SceneMultiplayer(); tree.SetMultiplayer(hostApi, new("/root/PauseTestHost")); tree.Root.AddChild(hostRoot);
        using var clientRoot = new Control { Name = "PauseTestClient" }; tree.Root.AddChild(clientRoot);
        var clientApi = new SceneMultiplayer(); tree.SetMultiplayer(clientApi, clientRoot.GetPath());
        var host = hostRoot.GetNode<LobbyTransport>("Transport"); host.DiscoveryPort = 19922;
        var client = new LobbyTransport { Name = "Transport" }; clientRoot.AddChild(client);
        try
        {
            host.UseSyntheticQuestions(1); host.StrategyEnabled = false;
            AssertThat(host.Host("Room", "Host", 19921)).IsEqual(Error.Ok);
            AssertThat(client.Join("127.0.0.1", "Phone", 19921)).IsEqual(Error.Ok);
            await Wait(tree, () => client.LocalPlayerId is not null);
            client.SetReady(true); host.SetReady(true);
            await Wait(tree, () => host.Snapshot?.Players.All(p => p.Ready) == true);
            host.StartGame(); await Wait(tree, () => client.MatchSnapshot is not null);
            client.Stop(); await Wait(tree, () => host.MatchSnapshot?.IsPaused == true);
            var modal = hostRoot.GetNode<MatchDialog>("Margin/Scroll/Content/MatchPanel/MatchDialogs/PauseDialog");
            AssertThat(modal.Visible).IsTrue();
            AssertThat(modal.Body.GetNode<Label>("Message").Text.Contains("Phone")).IsTrue();
            modal.Actions.GetNode<Button>("HostResume").EmitSignal(Button.SignalName.Pressed);
            AssertThat(host.MatchSnapshot!.IsPaused).IsFalse(); AssertThat(modal.Visible).IsFalse();
            var status = hostRoot.GetNode<Label>("Margin/Scroll/Content/MatchPanel/Departures");
            AssertThat(status.Visible).IsTrue(); AssertThat(status.Text.Contains("Phone")).IsTrue();
            AssertThat(status.Text.Contains("Αποσυνδεδεμένοι") || status.Text.Contains("Disconnected")).IsTrue();
        }
        finally
        {
            clientRoot.Free(); hostRoot.Free(); tree.SetMultiplayer(null!, new("/root/PauseTestClient")); tree.SetMultiplayer(null!, new("/root/PauseTestHost"));
            clientApi.Dispose(); hostApi.Dispose(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }
    [TestCase]
    [RequireGodotRuntime]
    public async Task InterruptedMatchReclaimsPlayerOverEnetAndHostClosureIsAnnounced()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var hostRoot = new Control { Name = "ReconnectTestHost" }; tree.Root.AddChild(hostRoot);
        using var clientRoot = new Control { Name = "ReconnectTestClient" }; tree.Root.AddChild(clientRoot);
        var hostApi = new SceneMultiplayer(); var clientApi = new SceneMultiplayer();
        tree.SetMultiplayer(hostApi, hostRoot.GetPath()); tree.SetMultiplayer(clientApi, clientRoot.GetPath());
        var host = new LobbyTransport { Name = "Transport", DiscoveryPort = 19912 }; hostRoot.AddChild(host);
        var client = new LobbyTransport { Name = "Transport" }; clientRoot.AddChild(client);
        var reconnected = false; var closed = false;
        client.StatusChanged += status => { if (status == "Reconnected") reconnected = true; if (status == "HostClosed") closed = true; };
        try
        {
            host.UseSyntheticQuestions(1); host.StrategyEnabled = false;
            AssertThat(host.Host("Room", "Host", 19911)).IsEqual(Error.Ok);
            AssertThat(client.Join("127.0.0.1", "Phone", 19911)).IsEqual(Error.Ok);
            await Wait(tree, () => client.LocalPlayerId is not null);
            var original = client.LocalPlayerId;
            client.SetReady(true); host.SetReady(true);
            await Wait(tree, () => host.Snapshot?.Players.All(p => p.Ready) == true);
            host.StartGame(); await Wait(tree, () => client.MatchSnapshot is not null);
            var connection = hostApi.GetPeers().Single();
            ((ENetMultiplayerPeer)hostApi.MultiplayerPeer).DisconnectPeer(connection);
            await Wait(tree, () => reconnected && client.MatchSnapshot is not null);
            AssertThat(client.LocalPlayerId).IsEqual(original);
            AssertThat(host.Snapshot!.Players.Length).IsEqual(2);
            AssertThat(client.MatchSnapshot!.IsPaused).IsTrue();
            AssertThat(client.MatchSnapshot.IsResuming).IsTrue();
            await Wait(tree, () => client.MatchSnapshot?.IsPaused == false, 8000);
            host.Stop(); await Wait(tree, () => closed);
        }
        finally
        {
            clientRoot.Free(); hostRoot.Free();
            tree.SetMultiplayer(null!, new("/root/ReconnectTestClient")); tree.SetMultiplayer(null!, new("/root/ReconnectTestHost"));
            clientApi.Dispose(); hostApi.Dispose();
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }
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

    private static async Task Wait(SceneTree tree, Func<bool> predicate, int timeoutMs = 5000)
    {
        var until = global::Godot.Time.GetTicksMsec() + (ulong)timeoutMs;
        while (!predicate() && global::Godot.Time.GetTicksMsec() < until) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        AssertThat(predicate()).IsTrue();
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task TenCharactersDisableTakenChoicesAndKeepSelectionsStableOnRefresh()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var picker = new CharacterPicker(); tree.Root.AddChild(picker);
        try
        {
            AssertThat(picker.GetChildren().OfType<Button>().Count()).IsEqual(10);
            picker.Select(6); picker.SetTaken([0, 1]); AssertThat(picker.Selected).IsEqual(6);
            AssertThat(picker.GetNode<Button>("Character0").Disabled).IsTrue();
            picker.Select(0); AssertThat(picker.Selected).IsEqual(6);
            picker.SetTaken([0, 1, 6]); AssertThat(picker.Selected).IsNull();
            AssertThat(picker.GetNode<Button>("Character6").Modulate.R < 1).IsTrue();
            for (var i = 0; i < 10; i++) AssertThat(GameArt.AvatarTexture(i)).IsNotNull();
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
            AssertThat(host.Host("Αίθουσα δοκιμής", "Host", 19881, "1234", 8)).IsEqual(Error.Ok);
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
            AssertThat(picker.GetNode<Button>("Character8").Disabled).IsTrue();
            flow.GetNode<LineEdit>("Identity/PlayerName").Text = "Ελένη"; picker.Select(9);
            AssertThat(flow.GetNode<Button>("Identity/JoinLobby").Text).IsEqual("");
            flow.GetNode<Button>("Identity/JoinLobby").EmitSignal(Button.SignalName.Pressed);
            await Wait(tree, () => client.LocalPlayerId is not null);
            AssertThat(client.OwnedPlayers.Single().CharacterId).IsEqual(9);
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

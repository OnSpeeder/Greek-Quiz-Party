using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

public partial class LobbyScreen : Control
{
    private LobbyTransport _transport = null!;
    private LineEdit _name = null!;
    private LineEdit _room = null!;
    private LineEdit _address = null!;
    private Button _host = null!;
    private Button _join = null!;
    private Button _ready = null!;
    private Button _start = null!;
    private Button _disconnect = null!;
    private GridContainer _actions = null!;
    private Label _roster = null!;
    private Label _status = null!;
    private MatchSetupPanel _matchSetup = null!;
    private LineEdit _pin = null!;
    private RoomBrowser _browser = null!;
    private JoinFlow _joinFlow = null!;
    private RoomCreationPanel _creation = null!;
    private RosterEditor _players = null!;
    private VBoxContainer _chooser = null!;
    private Button _switchPage = null!;
    private Button _manualIp = null!;
    private Button _pinOptions = null!;
    private string _page = "choose";
    private bool _setupVisible = true;
    private bool _manualOpen;
    private bool _pinOpen;
    private MatchDialog _reconnectDialog = null!;

    public override void _Ready()
    {
        AddChild(new ResponsiveCanvas());
        const string path = "Margin/Scroll/Content/";
        _transport = GetNode<LobbyTransport>("Transport");
        var reconnectLayer = new CanvasLayer { Name = "ReconnectLayer", Layer = 30 }; AddChild(reconnectLayer);
        _reconnectDialog = new MatchDialog { Name = "ReconnectDialog" }; reconnectLayer.AddChild(_reconnectDialog);
        _reconnectDialog.Body.AddChild(new Label { Text = "MATCH_RECONNECTING", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        var cancelReconnect = new Button { Text = "UI_NEW_PARTY", CustomMinimumSize = new(0, 64) };
        cancelReconnect.Pressed += ReturnHome; _reconnectDialog.Actions.AddChild(cancelReconnect);
        _name = GetNode<LineEdit>(path + "PlayerName");
        _room = GetNode<LineEdit>(path + "RoomName");
        _address = GetNode<LineEdit>(path + "Address");
        _host = GetNode<Button>(path + "Host");
        _join = GetNode<Button>(path + "Join");
        _ready = GetNode<Button>(path + "Ready");
        _start = GetNode<Button>(path + "Start");
        _disconnect = GetNode<Button>(path + "Disconnect");
        _host.ThemeTypeVariation = "PrimaryAction";
        _start.ThemeTypeVariation = "PrimaryAction";
        _roster = GetNode<Label>(path + "Roster");
        _status = GetNode<Label>(path + "Status");
        var content = GetNode<VBoxContainer>(path.TrimEnd('/'));
        _players = new RosterEditor { Name = "RosterEditor" };
        content.AddChild(_players); content.MoveChild(_players, _ready.GetIndex()); _players.Bind(_transport);
        _actions = new GridContainer { Name = "LobbyActions", Columns = 1 };
        content.AddChild(_actions); content.MoveChild(_actions, _start.GetIndex());
        _players.MoveAddActionTo(_actions); _start.Reparent(_actions); _disconnect.Reparent(_actions);
        _start.SizeFlagsHorizontal = SizeFlags.ExpandFill; _disconnect.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        Resized += () => _actions.Columns = Size.X > 850 ? 3 : 1;
        _actions.Columns = Size.X > 850 ? 3 : 1;
        _pin = new LineEdit { Name = "RoomPin", MaxLength = 6, Secret = true, PlaceholderText = "LOBBY_PIN",
            CustomMinimumSize = new Vector2(0, 64), VirtualKeyboardType = LineEdit.VirtualKeyboardTypeEnum.Number };
        content.AddChild(_pin); content.MoveChild(_pin, _host.GetIndex());
        foreach (var field in new[] { _name, _room, _pin, _address })
        {
            var label = new Label { Text = Tr(field == _name ? "UI_NAME_LABEL" : field == _room ? "UI_ROOM_LABEL" : field == _pin ? "UI_PIN_LABEL" : "SPIKE_ADDRESS"), AutowrapMode = TextServer.AutowrapMode.WordSmart };
            label.AddThemeFontSizeOverride("font_size", 18); label.AddThemeColorOverride("font_color", ShowtimeTheme.Cyan);
            content.AddChild(label); content.MoveChild(label, field.GetIndex());
            field.VisibilityChanged += () => label.Visible = field.Visible;
        }
        content.MoveChild(_status, _pin.GetIndex() + 1);
        _joinFlow = new JoinFlow { Name = "JoinFlow" };
        content.AddChild(_joinFlow); content.MoveChild(_joinFlow, _address.GetIndex());
        _joinFlow.Bind(_transport); _browser = _joinFlow.GetNode<RoomBrowser>("RoomBrowser");
        _creation = new RoomCreationPanel { Name = "CreateRoom" }; content.AddChild(_creation);
        content.MoveChild(_creation, _host.GetIndex());
        _creation.CreateRequested += request => ShowError(_transport.Host(request.RoomName, request.PlayerName,
            pin: request.Pin, character: request.Character, hostPlays: request.HostPlays, maxPlayers: request.MaxPlayers));
        _creation.StepChanged += () =>
        {
            GetNode<Label>(path + "Title").Text = _creation.IdentityOpen ? "HOST_IDENTITY_TITLE" : "UI_CREATE_TITLE";
            GetNode<ScrollContainer>("Margin/Scroll").ScrollVertical = 0;
        };
        _matchSetup = new MatchSetupPanel { Name = "MatchSetup", Visible = false };
        var shellHost = GetNode<PresentationShell>("PresentationShell");
        shellHost.AddChild(_matchSetup); _matchSetup.Bind(_transport);
        _matchSetup.Closed += () =>
        {
            GetNode<Control>("Margin").Show(); shellHost.SetNavigationCovered(false);
            if (_transport.Snapshot is { } snapshot && _transport.MatchSnapshot is null) Render(snapshot);
        };
        shellHost.ConfigureLobbyActions(() => OpenMatchPage("setup"), () => OpenMatchPage("rules"));
        GetNode<ScrollContainer>("Margin/Scroll").AddChild(new PageDragScroll());
        _chooser = new VBoxContainer { Name = "PartyChoice" };
        content.AddChild(_chooser); content.MoveChild(_chooser, 1);
        var crew = new TextureRect { Texture = GD.Load<Texture2D>("res://Art/showtime-crew-v2.png"),
            ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize, StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered,
            CustomMinimumSize = new(0, 160), MouseFilter = MouseFilterEnum.Ignore };
        _chooser.AddChild(crew);
        foreach (var mode in new[] { "create", "join" })
        {
            var button = new Button { Name = mode, Text = Tr(mode == "create" ? "UI_CREATE_PARTY" : "UI_JOIN_PARTY"),
                CustomMinimumSize = new(0, 88), ThemeTypeVariation = mode == "create" ? "PrimaryAction" : "" };
            button.Pressed += () => ShowSetupPage(mode); _chooser.AddChild(button);
        }
        _switchPage = new Button { Name = "ChangePath", Text = "SPIKE_BACK", Flat = true, Alignment = HorizontalAlignment.Left };
        _switchPage.AddThemeFontSizeOverride("font_size", 18);
        content.AddChild(_switchPage); content.MoveChild(_switchPage, _chooser.GetIndex() + 1);
        _switchPage.Pressed += () => ShowSetupPage("choose");
        _manualIp = new Button { Name = "ManualIp", Text = "UI_MANUAL_IP" };
        content.AddChild(_manualIp); content.MoveChild(_manualIp, _address.GetIndex());
        _manualIp.Pressed += () => { _manualOpen = !_manualOpen; ShowSetup(true); };
        _pinOptions = new Button { Name = "PinOptions", Text = "UI_PIN_OPTIONS", Flat = true };
        content.AddChild(_pinOptions); content.MoveChild(_pinOptions, _pin.GetIndex());
        _pinOptions.Pressed += () => { _pinOpen = !_pinOpen; ShowSetup(true); };
        if (PresentationShell.For(this) is { } shell) shell.SetLeaveAction(() =>
        { _transport.Stop(); Reset(); shell.CloseSettings(); });
        _join.Pressed += () => ShowError(_transport.Join(_address.Text.Trim(), _name.Text.Trim(), pin: _pin.Text));
        _ready.Pressed += () =>
        {
            var local = _transport.Snapshot?.Players.FirstOrDefault(player => player.PlayerId == _transport.LocalPlayerId);
            if (local is not null) _transport.SetReady(!local.Ready);
        };
        _start.Pressed += _transport.StartGame;
        _disconnect.Pressed += () => { _transport.Stop(); Reset(); };
        GetNode<Button>(path + "Back").Pressed += NavigateBack;
        _transport.SnapshotChanged += Render;
        _transport.StatusChanged += reason =>
        {
            if (reason == "Reconnecting") { _reconnectDialog.Show(); return; }
            if (reason == "Reconnected") { _reconnectDialog.Hide(); return; }
            if (reason is "HostClosed" or "ReconnectExpired" or "ServerDisconnected")
            { _reconnectDialog.Hide(); Callable.From(ReturnHome).CallDeferred(); return; }
            if (_transport.MatchSnapshot is not null) { _status.Hide(); return; }
            if (_page == "join" && _setupVisible) { _status.Hide(); return; }
            if (_transport.Snapshot is null && reason != "Connecting") Reset();
            if (reason == "Connecting") { _host.Disabled = true; _join.Disabled = true; _browser.Visible = false; _pin.Editable = false; }
            _status.Text = Tr("LOBBY_STATUS_" + reason);
            _status.Visible = reason is not ("Idle" or "Joined" or "HostListening");
            RevealStatus();
        };
        GetNode<MatchPanel>(path + "MatchPanel").Bind(_transport);
        _transport.MatchChanged += _ =>
        {
            _matchSetup.Dismiss();
            _players.Visible = false; _actions.Hide();
            GetNode<PresentationShell>("PresentationShell").ShowLobbyActions(false);
            foreach (var name in new[] { "Title", "Addresses", "Roster", "Ready", "Status", "Back" })
                GetNode<Control>(path + name).Visible = false;
        };
        GetNode<Label>(path + "Addresses").Text = string.Format(Tr("SPIKE_ADDRESSES"), string.Join(", ",
            IP.GetLocalAddresses().Where(ip => ip.StartsWith("192.168.", StringComparison.Ordinal) || ip.StartsWith("10.", StringComparison.Ordinal))));
        Reset();
        if (OS.IsDebugBuild())
        {
            var args = MatchProcessProbe.LaunchArguments().Select(a => a.StartsWith("--match-ui-", StringComparison.Ordinal) ? "--ui-" + a["--match-ui-".Length..] : a).ToArray();
            if (int.TryParse(args.FirstOrDefault(a => a.StartsWith("--ui-discovery-port=", StringComparison.Ordinal))?["--ui-discovery-port=".Length..], out var discoveryPort) && discoveryPort is >= 1024 and <= 65535)
                _transport.DiscoveryPort = discoveryPort;
            if (args.FirstOrDefault(a => a.StartsWith("--ui-lobby-page=", StringComparison.Ordinal)) is { } preview)
                Callable.From(() =>
                {
                    _transport.Host("Η παρέα μας", "Φίλιππος", 17861);
                    foreach (var (name, slot) in new[] { ("Ελένη", 1), ("Νίκος", 2), ("Μαρία", 3), ("Γιώργος", 4), ("Άννα", 5), ("Δήμητρα", 6), ("Κώστας", 7) })
                    { _transport.AddLocalPlayer(name, slot); if (slot % 2 == 1) _transport.SetReady(true, localSlot: slot); }
                    var page = preview["--ui-lobby-page=".Length..];
                    if (page != "roster") OpenMatchPage(page);
                }).CallDeferred();
            if (args.Contains("--ui-create") || args.Contains("--ui-create-identity")) ShowSetupPage("create");
            if (args.Contains("--ui-create-identity"))
            {
                ((Button)_creation.FindChild("Create", true, false)).EmitSignal(Button.SignalName.Pressed);
                _creation.GetNode<PlayerIdentityForm>("Identity").NameInput.Text = "Φίλιππος";
                _creation.GetNode<PlayerIdentityForm>("Identity").Characters.Select(1);
            }
            if (args.Contains("--ui-join")) ShowSetupPage("join");
        }
        AddChild(new LanProcessProbe { Name = "LanProbe" });
        AddChild(new MixedProcessProbe { Name = "MixedProbe" });
        if (OS.IsDebugBuild()) AddChild(new MatchFlowProcessProbe { Name = "MatchFlowProbe" });
    }

    private void Reset()
    {
        _host.Disabled = false;
        _join.Disabled = false;
        _ready.Disabled = true;
        _start.Disabled = true;
        _start.Visible = false;
        _matchSetup.Dismiss();
        _creation.Reset();
        GetNode<PresentationShell>("PresentationShell").ShowLobbyActions(false);
        _players.Visible = false; _actions.Hide();
        _name.Editable = true;
        _room.Editable = true;
        _address.Editable = true;
        _pin.Editable = true;
        ShowSetup(true);
        _roster.Text = "";
        _status.Text = Tr("LOBBY_STATUS_Idle");
        _status.Visible = false;
        GetNode<MatchPanel>("Margin/Scroll/Content/MatchPanel").Visible = false;
        foreach (var name in new[] { "Title", "Roster", "Ready", "Status" }) GetNode<Control>("Margin/Scroll/Content/" + name).Visible = true;
        _ready.Visible = false;
        _roster.Visible = false;
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = false;
        _disconnect.Visible = false;
    }

    private void ShowError(Error error)
    {
        if (error != Error.Ok) _status.Text = Tr(!RoomAdmission.ValidPin(_pin.Text) ? "LOBBY_STATUS_PinFormat" :
            error == Error.FileCorrupt ? "LOBBY_STATUS_ContentError" : "LOBBY_STATUS_InvalidInput");
        if (error != Error.Ok) { _status.Visible = true; RevealStatus(); }
    }

    private void RevealStatus() => Callable.From(() =>
    {
        if (GodotObject.IsInstanceValid(this) && IsInsideTree() && GodotObject.IsInstanceValid(_status) && _status.IsVisibleInTree())
            GetNode<ScrollContainer>("Margin/Scroll").EnsureControlVisible(_status);
    }).CallDeferred();

    private void Render(LobbySnapshotDto snapshot)
    {
        if (_transport.MatchSnapshot is not null) return;
        GetNode<MatchPanel>("Margin/Scroll/Content/MatchPanel").Visible = false;
        GetNode<ScrollContainer>("Margin/Scroll").VerticalScrollMode = ScrollContainer.ScrollMode.ShowNever;
        _players.Visible = true;
        foreach (var name in new[] { "Title", "Status" }) GetNode<Control>("Margin/Scroll/Content/" + name).Show();
        _pin.Text = "";
        ShowSetup(false);
        _host.Disabled = true;
        _join.Disabled = true;
        _name.Editable = false;
        _room.Editable = false;
        _address.Editable = false;
        _ready.Disabled = snapshot.Phase != "Lobby";
        _actions.Show();
        _start.Visible = _transport.IsHost;
        GetNode<PresentationShell>("PresentationShell").ShowLobbyActions(snapshot.Phase == "Lobby", _transport.IsHost);
        _start.Disabled = snapshot.Phase != "Lobby" || snapshot.Players.Length < 2 || snapshot.Players.Any(player => !player.Ready) ||
            _transport.IsHost && _transport.SelectedQuestionCapacity < Math.Max(1, _transport.QuestionCount) ||
            snapshot.TeamMode && snapshot.Players.Select(p => p.TeamId).Distinct().Count() != 2;
        _roster.Text = snapshot.RoomName + "\n" + string.Join("\n", snapshot.Players.Select(player =>
            $"{player.DisplayName}{(player.IsHost ? " — " + Tr("LOBBY_HOST_MARK") : "")} — {Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO")}"));
        _status.Text = Tr(snapshot.Phase == "GameStarting" ? "LOBBY_STATUS_GameStarting" : "LOBBY_STATUS_Joined");
        _status.Visible = false;
        _roster.Visible = false; _ready.Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Title").Text = snapshot.RoomName;
        _disconnect.Visible = true;
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = false;
    }

    private void ShowSetup(bool visible)
    {
        _setupVisible = visible;
        var create = visible && _page == "create";
        var join = visible && _page == "join";
        _chooser.Visible = visible && _page == "choose";
        _switchPage.Visible = visible && _page != "choose";
        _name.Visible = false;
        _room.Visible = false;
        _host.Visible = false;
        _address.Visible = false;
        _join.Visible = false;
        _pin.Visible = false;
        _pinOptions.Visible = false;
        _manualIp.Visible = false;
        _joinFlow.Visible = join;
        _creation.Visible = create;
        if (visible) _status.Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Addresses").Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Title").Text = Tr(create ? "UI_CREATE_TITLE" : join ? "UI_JOIN_TITLE" : "UI_PICK_PATH");
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = false;
        _switchPage.Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Title").Visible = !join;
    }

    public void ShowSetupPage(string page)
    {
        if (!_setupVisible || page is not ("choose" or "create" or "join")) return;
        _page = page;
        if (page == "create" && string.IsNullOrWhiteSpace(_room.Text)) _room.Text = Tr("UI_ROOM_DEFAULT");
        ShowSetup(true);
        if (page == "join") { _joinFlow.ShowRooms(); _transport.Discovery.Scan(_transport.DiscoveryPort); }
        GetNode<ScrollContainer>("Margin/Scroll").ScrollVertical = 0;
    }

    public void ResumePrevious(RejoinTicket ticket)
    {
        if (!_transport.Resume(ticket)) GD.PushWarning("Saved rejoin ticket was invalid.");
    }

    public void OpenMatchPage(string page)
    {
        if (_transport.MatchSnapshot is not null || _transport.Snapshot?.Phase != "Lobby" ||
            page != "rules" && !_transport.IsHost) return;
        GetNode<Control>("Margin").Hide();
        GetNode<PresentationShell>("PresentationShell").SetNavigationCovered(true);
        _matchSetup.Open(page);
    }

    public void ReturnHome()
    {
        _transport.Stop();
        var error = GetTree().ChangeSceneToFile("res://Scenes/Main.tscn");
        if (error != Error.Ok) GD.PushError($"Home navigation failed: {error}");
    }

    public void NavigateBack()
    {
        if (_transport.MatchSnapshot is not null)
        { PresentationShell.For(this)?.OpenSettings(); return; }
        if (_page == "join" && _setupVisible)
        { if (!_joinFlow.Back()) ReturnHome(); return; }
        if (_page == "create" && _setupVisible) { if (!_creation.Back()) ReturnHome(); return; }
        if (_matchSetup.Back()) return;
        if (!_setupVisible || _host.Disabled)
        { _transport.Stop(); Reset(); return; }
        if (_pinOpen) { _pinOpen = false; ShowSetup(true); return; }
        if (_manualOpen) { _manualOpen = false; ShowSetup(true); return; }
        if (_page != "choose") { ShowSetupPage("choose"); return; }
        ReturnHome();
    }
}

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
    private Label _roster = null!;
    private Label _status = null!;
    private VBoxContainer _settings = null!;
    private Label _capacity = null!;
    private OptionButton _length = null!;
    private VBoxContainer _categories = null!;
    private LineEdit _pin = null!;
    private RoomBrowser _browser = null!;
    private RosterEditor _players = null!;
    private VBoxContainer _chooser = null!;
    private Button _switchPage = null!;
    private Button _manualIp = null!;
    private Button _pinOptions = null!;
    private Button _ruleOptions = null!;
    private string _page = "choose";
    private bool _setupVisible = true;
    private bool _manualOpen;
    private bool _pinOpen;
    private bool _rulesOpen;

    public override void _Ready()
    {
        AddChild(new ResponsiveCanvas());
        const string path = "Margin/Scroll/Content/";
        _transport = GetNode<LobbyTransport>("Transport");
        _name = GetNode<LineEdit>(path + "PlayerName");
        _room = GetNode<LineEdit>(path + "RoomName");
        _address = GetNode<LineEdit>(path + "Address");
        _host = GetNode<Button>(path + "Host");
        _join = GetNode<Button>(path + "Join");
        _ready = GetNode<Button>(path + "Ready");
        _start = GetNode<Button>(path + "Start");
        _host.ThemeTypeVariation = "PrimaryAction";
        _start.ThemeTypeVariation = "PrimaryAction";
        _roster = GetNode<Label>(path + "Roster");
        _status = GetNode<Label>(path + "Status");
        var content = GetNode<VBoxContainer>(path.TrimEnd('/'));
        _players = new RosterEditor { Name = "RosterEditor" };
        content.AddChild(_players); content.MoveChild(_players, _ready.GetIndex()); _players.Bind(_transport);
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
        _browser = new RoomBrowser { Name = "RoomBrowser" };
        content.AddChild(_browser); content.MoveChild(_browser, _address.GetIndex());
        _browser.Bind(_transport.Discovery, room =>
        {
            if (room.Room.RequiresPin && _pin.Text.Length == 0)
            { _pinOpen = true; ShowSetup(true); _status.Text = Tr("LOBBY_STATUS_PinRequired"); _status.Visible = true; _pin.GrabFocus(); RevealStatus(); return; }
            _address.Text = room.Address;
            ShowError(_transport.Join(room.Address, _name.Text.Trim(), room.Room.GamePort, _pin.Text));
        });
        _settings = new VBoxContainer { Name = "MatchSettings" };
        GetNode<VBoxContainer>(path.TrimEnd('/')).AddChild(_settings);
        GetNode<VBoxContainer>(path.TrimEnd('/')).MoveChild(_settings, _start.GetIndex());
        _capacity = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _settings.AddChild(_capacity);
        var length = new OptionButton { Name = "Length", CustomMinimumSize = new Vector2(0, 64) };
        _length = length;
        length.AddItem(Tr("MATCH_PREVIEW"), 1);
        foreach (var count in new[] { 10, 20, 30 }) length.AddItem(string.Format(Tr("MATCH_LENGTH"), count), count);
        length.ItemSelected += index => _transport.QuestionCount = length.GetItemId((int)index);
        _settings.AddChild(length);
        var timer = new OptionButton { Name = "Duration", CustomMinimumSize = new Vector2(0, 64) };
        foreach (var seconds in new[] { 10, 20, 30, 60 }) timer.AddItem(string.Format(Tr("MATCH_DURATION"), seconds), seconds);
        timer.Select(1);
        timer.ItemSelected += index => _transport.QuestionSeconds = timer.GetItemId((int)index);
        _settings.AddChild(timer);
        var strategy = new CheckButton { Name = "Strategy", Text = "STRATEGY_ENABLED", ButtonPressed = true,
            CustomMinimumSize = new(0, 64) };
        var steal = new CheckButton { Name = "AllowSteal", Text = "STRATEGY_ALLOW_STEAL", CustomMinimumSize = new(0, 64) };
        strategy.Toggled += enabled => { _transport.StrategyEnabled = enabled; steal.Disabled = !enabled; };
        steal.Toggled += enabled => _transport.AllowSteal = enabled;
        _settings.AddChild(strategy); _settings.AddChild(steal);
        _categories = new VBoxContainer { Name = "Categories" };
        _settings.AddChild(_categories);
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
        _ruleOptions = new Button { Name = "RuleOptions", Text = "UI_RULES" };
        content.AddChild(_ruleOptions); content.MoveChild(_ruleOptions, _settings.GetIndex());
        _ruleOptions.Pressed += () =>
        {
            _rulesOpen = !_rulesOpen;
            _settings.Visible = _transport.IsHost && _rulesOpen;
            _players.ShowHostOptions(_rulesOpen);
        };
        if (PresentationShell.For(this) is { } shell) shell.SetLeaveAction(() =>
        { _transport.Stop(); Reset(); shell.CloseSettings(); });
        _host.Pressed += () => ShowError(_transport.Host(_room.Text.Trim(), _name.Text.Trim(), pin: _pin.Text));
        _join.Pressed += () => ShowError(_transport.Join(_address.Text.Trim(), _name.Text.Trim(), pin: _pin.Text));
        _ready.Pressed += () =>
        {
            var local = _transport.Snapshot?.Players.FirstOrDefault(player => player.PlayerId == _transport.LocalPlayerId);
            if (local is not null) _transport.SetReady(!local.Ready);
        };
        _start.Pressed += _transport.StartGame;
        GetNode<Button>(path + "Disconnect").Pressed += () => { _transport.Stop(); Reset(); };
        GetNode<Button>(path + "Back").Pressed += () => GetTree().ChangeSceneToFile("res://Scenes/Main.tscn");
        _transport.SnapshotChanged += Render;
        _transport.StatusChanged += reason =>
        {
            if (_transport.Snapshot is null && reason != "Connecting") Reset();
            if (reason == "Connecting") { _host.Disabled = true; _join.Disabled = true; _browser.Visible = false; _pin.Editable = false; }
            _status.Text = Tr("LOBBY_STATUS_" + reason);
            _status.Visible = reason is not ("Idle" or "Joined" or "HostListening");
            RevealStatus();
        };
        GetNode<MatchPanel>(path + "MatchPanel").Bind(_transport);
        _transport.MatchChanged += _ =>
        {
            _settings.Visible = false;
            _players.Visible = false;
            _ruleOptions.Visible = false;
            foreach (var name in new[] { "Title", "Addresses", "Roster", "Ready", "Start", "Status", "Disconnect", "Back" })
                GetNode<Control>(path + name).Visible = false;
        };
        GetNode<Label>(path + "Addresses").Text = string.Format(Tr("SPIKE_ADDRESSES"), string.Join(", ",
            IP.GetLocalAddresses().Where(ip => ip.StartsWith("192.168.", StringComparison.Ordinal) || ip.StartsWith("10.", StringComparison.Ordinal))));
        Reset();
        if (OS.IsDebugBuild())
        {
            var args = OS.GetCmdlineUserArgs();
            if (args.Contains("--ui-create")) ShowSetupPage("create");
            if (args.Contains("--ui-join")) ShowSetupPage("join");
        }
        AddChild(new LanProcessProbe { Name = "LanProbe" });
        AddChild(new MixedProcessProbe { Name = "MixedProbe" });
    }

    private void Reset()
    {
        _host.Disabled = false;
        _join.Disabled = false;
        _ready.Disabled = true;
        _start.Disabled = true;
        _start.Visible = false;
        _settings.Visible = false;
        _ruleOptions.Visible = false;
        _rulesOpen = false;
        _players.Visible = false;
        foreach (var child in _categories.GetChildren()) { _categories.RemoveChild(child); child.QueueFree(); }
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
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = _page == "choose";
        GetNode<Button>("Margin/Scroll/Content/Disconnect").Visible = false;
    }

    private void ShowError(Error error)
    {
        if (error != Error.Ok) _status.Text = Tr(!RoomAdmission.ValidPin(_pin.Text) ? "LOBBY_STATUS_PinFormat" :
            error == Error.FileCorrupt ? "LOBBY_STATUS_ContentError" : "LOBBY_STATUS_InvalidInput");
        if (error != Error.Ok) { _status.Visible = true; RevealStatus(); }
    }

    private void RevealStatus() => Callable.From(() =>
    {
        if (GodotObject.IsInstanceValid(this) && IsInsideTree() && GodotObject.IsInstanceValid(_status))
            GetNode<ScrollContainer>("Margin/Scroll").EnsureControlVisible(_status);
    }).CallDeferred();

    private void Render(LobbySnapshotDto snapshot)
    {
        if (_transport.MatchSnapshot is not null) return;
        _pin.Text = "";
        ShowSetup(false);
        _host.Disabled = true;
        _join.Disabled = true;
        _name.Editable = false;
        _room.Editable = false;
        _address.Editable = false;
        _ready.Disabled = snapshot.Phase != "Lobby";
        _start.Visible = _transport.IsHost;
        _settings.Visible = _transport.IsHost && snapshot.Phase == "Lobby" && _rulesOpen;
        _ruleOptions.Visible = _transport.IsHost && snapshot.Phase == "Lobby";
        _capacity.Text = string.Format(Tr("MATCH_CAPACITY"), _transport.AvailableQuestions);
        _length.Select(_length.GetItemIndex(_transport.QuestionCount));
        if (_transport.IsHost && _categories.GetChildCount() == 0)
        {
            _transport.EnabledCategories = _transport.QuestionCategories.Select(c => c.Id).ToHashSet();
            foreach (var category in _transport.QuestionCategories)
            {
                var toggle = new CheckButton { Text = Tr(category.NameKey), ButtonPressed = true, CustomMinimumSize = new Vector2(0, 64) };
                toggle.Toggled += enabled =>
                {
                    if (enabled) _transport.EnabledCategories?.Add(category.Id);
                    else _transport.EnabledCategories?.Remove(category.Id);
                };
                _categories.AddChild(toggle);
            }
        }
        _start.Disabled = snapshot.Phase != "Lobby" || snapshot.Players.Length < 2 || snapshot.Players.Any(player => !player.Ready) ||
            snapshot.TeamMode && snapshot.Players.Select(p => p.TeamId).Distinct().Count() != 2;
        _roster.Text = snapshot.RoomName + "\n" + string.Join("\n", snapshot.Players.Select(player =>
            $"{player.DisplayName}{(player.IsHost ? " — " + Tr("LOBBY_HOST_MARK") : "")} — {Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO")}"));
        _status.Text = Tr(snapshot.Phase == "GameStarting" ? "LOBBY_STATUS_GameStarting" : "LOBBY_STATUS_Joined");
        _status.Visible = false;
        _roster.Visible = false; _ready.Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Title").Text = snapshot.RoomName;
        GetNode<Button>("Margin/Scroll/Content/Disconnect").Visible = true;
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = false;
    }

    private void ShowSetup(bool visible)
    {
        _setupVisible = visible;
        var create = visible && _page == "create";
        var join = visible && _page == "join";
        _chooser.Visible = visible && _page == "choose";
        _switchPage.Visible = visible && _page != "choose";
        _name.Visible = create || join;
        _room.Visible = create;
        _host.Visible = create;
        _address.Visible = join && _manualOpen;
        _join.Visible = join && _manualOpen;
        _pin.Visible = (join || create) && _pinOpen;
        _pinOptions.Visible = create || join;
        _manualIp.Visible = join;
        _browser.Visible = join;
        if (visible) _status.Visible = false;
        GetNode<Label>("Margin/Scroll/Content/Addresses").Visible = join && _manualOpen;
        GetNode<Label>("Margin/Scroll/Content/Title").Text = Tr(create ? "UI_CREATE_TITLE" : join ? "UI_JOIN_TITLE" : "UI_PICK_PATH");
        GetNode<Button>("Margin/Scroll/Content/Back").Visible = visible && _page == "choose";
    }

    public void ShowSetupPage(string page)
    {
        if (!_setupVisible || page is not ("choose" or "create" or "join")) return;
        _page = page;
        if (page == "create" && string.IsNullOrWhiteSpace(_room.Text)) _room.Text = Tr("UI_ROOM_DEFAULT");
        ShowSetup(true);
        if (page == "join") _transport.Discovery.Scan();
        GetNode<ScrollContainer>("Margin/Scroll").ScrollVertical = 0;
    }

    public void ReturnHome()
    {
        _transport.Stop();
        var error = GetTree().ChangeSceneToFile("res://Scenes/Main.tscn");
        if (error != Error.Ok) GD.PushError($"Home navigation failed: {error}");
    }
}

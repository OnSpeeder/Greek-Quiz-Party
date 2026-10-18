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
        _roster = GetNode<Label>(path + "Roster");
        _status = GetNode<Label>(path + "Status");
        var content = GetNode<VBoxContainer>(path.TrimEnd('/'));
        _pin = new LineEdit { Name = "RoomPin", MaxLength = 6, Secret = true, PlaceholderText = Tr("LOBBY_PIN"),
            CustomMinimumSize = new Vector2(0, 64), VirtualKeyboardType = LineEdit.VirtualKeyboardTypeEnum.Number };
        content.AddChild(_pin); content.MoveChild(_pin, _host.GetIndex());
        content.MoveChild(_status, _pin.GetIndex() + 1);
        _browser = new RoomBrowser { Name = "RoomBrowser" };
        content.AddChild(_browser); content.MoveChild(_browser, _address.GetIndex());
        _browser.Bind(_transport.Discovery, room =>
        {
            if (room.Room.RequiresPin && _pin.Text.Length == 0)
            { _status.Text = Tr("LOBBY_STATUS_PinRequired"); _pin.GrabFocus(); RevealStatus(); return; }
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
        foreach (var seconds in new[] { 10, 20, 30 }) timer.AddItem(string.Format(Tr("MATCH_DURATION"), seconds), seconds);
        timer.Select(1);
        timer.ItemSelected += index => _transport.QuestionSeconds = timer.GetItemId((int)index);
        _settings.AddChild(timer);
        var strategy = new CheckButton { Name = "Strategy", Text = Tr("STRATEGY_ENABLED"), ButtonPressed = true,
            CustomMinimumSize = new(0, 64) };
        var steal = new CheckButton { Name = "AllowSteal", Text = Tr("STRATEGY_ALLOW_STEAL"), CustomMinimumSize = new(0, 64) };
        strategy.Toggled += enabled => { _transport.StrategyEnabled = enabled; steal.Disabled = !enabled; };
        steal.Toggled += enabled => _transport.AllowSteal = enabled;
        _settings.AddChild(strategy); _settings.AddChild(steal);
        _categories = new VBoxContainer { Name = "Categories" };
        _settings.AddChild(_categories);
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
            RevealStatus();
        };
        GetNode<MatchPanel>(path + "MatchPanel").Bind(_transport);
        _transport.MatchChanged += _ =>
        {
            _settings.Visible = false;
            foreach (var name in new[] { "Title", "Addresses", "Roster", "Ready", "Start", "Status" })
                GetNode<Control>(path + name).Visible = false;
        };
        GetNode<Label>(path + "Addresses").Text = string.Format(Tr("SPIKE_ADDRESSES"), string.Join(", ",
            IP.GetLocalAddresses().Where(ip => ip.StartsWith("192.168.", StringComparison.Ordinal) || ip.StartsWith("10.", StringComparison.Ordinal))));
        Reset();
        AddChild(new LanProcessProbe { Name = "LanProbe" });
    }

    private void Reset()
    {
        _host.Disabled = false;
        _join.Disabled = false;
        _ready.Disabled = true;
        _start.Disabled = true;
        _start.Visible = false;
        _settings.Visible = false;
        foreach (var child in _categories.GetChildren()) { _categories.RemoveChild(child); child.QueueFree(); }
        _name.Editable = true;
        _room.Editable = true;
        _address.Editable = true;
        _pin.Editable = true;
        ShowSetup(true);
        _roster.Text = "";
        _status.Text = Tr("LOBBY_STATUS_Idle");
        GetNode<MatchPanel>("Margin/Scroll/Content/MatchPanel").Visible = false;
        foreach (var name in new[] { "Title", "Roster", "Ready", "Status" }) GetNode<Control>("Margin/Scroll/Content/" + name).Visible = true;
    }

    private void ShowError(Error error)
    {
        if (error != Error.Ok) _status.Text = Tr(!RoomAdmission.ValidPin(_pin.Text) ? "LOBBY_STATUS_PinFormat" :
            error == Error.FileCorrupt ? "LOBBY_STATUS_ContentError" : "LOBBY_STATUS_InvalidInput");
        if (error != Error.Ok) RevealStatus();
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
        _settings.Visible = _transport.IsHost && snapshot.Phase == "Lobby";
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
        _start.Disabled = snapshot.Phase != "Lobby" || snapshot.Players.Length < 2 || snapshot.Players.Any(player => !player.Ready);
        _roster.Text = snapshot.RoomName + "\n" + string.Join("\n", snapshot.Players.Select(player =>
            $"{player.DisplayName}{(player.IsHost ? " — " + Tr("LOBBY_HOST_MARK") : "")} — {Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO")}"));
        _status.Text = Tr(snapshot.Phase == "GameStarting" ? "LOBBY_STATUS_GameStarting" : "LOBBY_STATUS_Joined");
    }

    private void ShowSetup(bool visible)
    {
        foreach (var control in new Control[] { _name, _room, _address, _host, _join }) control.Visible = visible;
        _pin.Visible = visible;
        _browser.Visible = visible;
        GetNode<Label>("Margin/Scroll/Content/Addresses").Visible = visible || _transport.IsHost;
    }
}

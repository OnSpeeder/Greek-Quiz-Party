using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Discovery -> PIN preflight -> identity -> atomic host admission.</summary>
public partial class JoinFlow : VBoxContainer
{
    private LobbyTransport _transport = null!;
    private RoomBrowser _browser = null!;
    private VBoxContainer _identity = null!;
    private LineEdit _name = null!;
    private CharacterPicker _characters = null!;
    private Button _join = null!;
    private Label _message = null!;
    private Control _pinOverlay = null!;
    private LineEdit _pin = null!;
    private Button _pinConfirm = null!;
    private DiscoveredRoom? _room;
    private bool _busy;
    public bool IdentityOpen => _identity.Visible;
    public bool PinOpen => _pinOverlay.Visible;
    public override void _Ready()
    {
        _browser = new RoomBrowser { Name = "RoomBrowser" }; AddChild(_browser);
        _message = new Label { Name = "Message", AutowrapMode = TextServer.AutowrapMode.WordSmart, Visible = false }; AddChild(_message);
        _identity = new VBoxContainer { Name = "Identity", Visible = false }; AddChild(_identity);
        _identity.AddChild(new Label { Text = "JOIN_IDENTITY", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _name = new LineEdit { Name = "PlayerName", PlaceholderText = "LOBBY_PLAYER_NAME", MaxLength = 32, CustomMinimumSize = new(0, 64) };
        _identity.AddChild(_name);
        _identity.AddChild(new Label { Text = "JOIN_CHARACTER", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _characters = new CharacterPicker { Name = "Characters" }; _identity.AddChild(_characters);
        _join = new Button { Name = "JoinLobby", Icon = GD.Load<Texture2D>("res://Art/join.svg"),
            IconAlignment = HorizontalAlignment.Center,
            AccessibilityName = Tr("JOIN_LOBBY"), TooltipText = Tr("JOIN_LOBBY"), CustomMinimumSize = new(0, 72), Disabled = true };
        _identity.AddChild(_join);
        _name.TextChanged += _ => UpdateJoin(); _characters.SelectionChanged += UpdateJoin;
        _join.Pressed += () =>
        {
            if (_characters.Selected is not { } character || _busy) return;
            _busy = _transport.JoinPrepared(_name.Text.Trim(), character); UpdateJoin();
        };
        BuildPin();
        var refresh = new global::Godot.Timer { WaitTime = 1, Autostart = true };
        refresh.Timeout += () => { if (IsVisibleInTree() && IdentityOpen && !_busy) _transport?.RefreshRoomAvailability(); };
        AddChild(refresh);
    }
    public void Bind(LobbyTransport transport)
    {
        _transport = transport; _browser.Bind(transport.Discovery, ChooseRoom);
        transport.RoomAccessChanged += OnAccess; transport.StatusChanged += OnStatus;
        if (OS.IsDebugBuild())
        {
            var args = MatchProcessProbe.LaunchArguments().Select(a => a.StartsWith("--match-ui-", StringComparison.Ordinal) ? "--ui-" + a["--match-ui-".Length..] : a).ToArray();
            var step = args.FirstOrDefault(a => a.StartsWith("--ui-join-step=", StringComparison.Ordinal))?["--ui-join-step=".Length..];
            if (step is not null) transport.Discovery.RoomsChanged += rooms =>
            {
                if (_room is not null) return;
                var room = rooms.FirstOrDefault(r => r.Room.RoomName == "LANTest");
                if (room is null || step == "rooms") return;
                ChooseRoom(room);
                if (step != "pin") { _pin.Text = "1234"; Prepare(); }
            };
        }
    }
    private void BuildPin()
    {
        _pinOverlay = new Control { Name = "PinPopup", Visible = false };
        // Child of the scene shell, outside the list's scrolling/clipping region.
        var shell = PresentationShell.For(this)!; shell.AddChild(_pinOverlay);
        _pinOverlay.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var dim = new ColorRect { Color = new(0, 0, 0, .78f) }; _pinOverlay.AddChild(dim); dim.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var margin = new MarginContainer { Name = "PinMargin" }; _pinOverlay.AddChild(margin);
        margin.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        foreach (var edge in new[] { "left", "right", "top", "bottom" }) margin.AddThemeConstantOverride("margin_" + edge, 24);
        var scroll = new ScrollContainer { HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled, FollowFocus = true }; margin.AddChild(scroll);
        var center = new CenterContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill, SizeFlagsVertical = SizeFlags.ExpandFill }; scroll.AddChild(center);
        var card = new PanelContainer(); center.AddChild(card);
        var fields = new VBoxContainer(); card.AddChild(fields);
        fields.AddChild(new Label { Text = "JOIN_PIN_PROMPT", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _pin = new LineEdit { Name = "Pin", Secret = true, MaxLength = 6, PlaceholderText = "JOIN_PIN_FIELD", VirtualKeyboardType = LineEdit.VirtualKeyboardTypeEnum.Number };
        fields.AddChild(_pin);
        var actions = new HBoxContainer(); fields.AddChild(actions);
        var cancel = new Button { Name = "Cancel", Text = "UI_SETTINGS_CANCEL", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _pinConfirm = new Button { Name = "Confirm", Icon = GD.Load<Texture2D>("res://Art/join.svg"), IconAlignment = HorizontalAlignment.Center, AccessibilityName = Tr("JOIN_CHECK_PIN"), TooltipText = Tr("JOIN_CHECK_PIN"), SizeFlagsHorizontal = SizeFlags.ExpandFill };
        actions.AddChild(cancel); actions.AddChild(_pinConfirm);
        cancel.Pressed += CancelPin; _pinConfirm.Pressed += Prepare;
        _pin.TextSubmitted += _ => Prepare();
        _pin.FocusNext = _pin.GetPathTo(_pinConfirm); _pin.FocusPrevious = _pin.GetPathTo(cancel);
        _pinConfirm.FocusNext = _pinConfirm.GetPathTo(cancel); _pinConfirm.FocusPrevious = _pinConfirm.GetPathTo(_pin);
        cancel.FocusNext = cancel.GetPathTo(_pin); cancel.FocusPrevious = cancel.GetPathTo(_pinConfirm);
        var keyboard = new global::Godot.Timer { WaitTime = .1, Autostart = true }; AddChild(keyboard);
        keyboard.Timeout += () =>
        {
            if (!GodotObject.IsInstanceValid(_pinOverlay) || !PinOpen) return;
            var scale = ResponsiveCanvas.PixelsPerUnit(GetWindow().Size, GetViewportRect().Size);
            margin.OffsetBottom = OS.HasFeature("android") ? -DisplayServer.VirtualKeyboardGetHeight() / Math.Max(.01f, scale) : 0;
            center.CustomMinimumSize = new(0, scroll.Size.Y);
            card.CustomMinimumSize = new(Math.Min(520, Math.Max(0, scroll.Size.X)), 0);
        };
    }
    public void ChooseRoom(DiscoveredRoom room)
    {
        _room = room; _message.Hide();
        if (room.Room.RequiresPin)
        {
            _pin.Text = ""; _pinOverlay.Show(); _browser.Hide();
            PresentationShell.For(this)?.SetNavigationCovered(true); _pin.GrabFocus();
        }
        else Prepare();
    }
    private void Prepare()
    {
        if (_room is null || _busy) return;
        if (_room.Room.RequiresPin && (_pin.Text.Length is < 4 or > 6 || !_pin.Text.All(c => c is >= '0' and <= '9')))
        { Fail("PinFormat"); return; }
        var pin = _room.Room.RequiresPin ? _pin.Text : "";
        ClosePin(); _busy = true; ShowMessage("LOBBY_STATUS_Connecting");
        var error = _transport.PrepareRoom(_room, pin);
        if (error != Error.Ok) Fail("ConnectionFailed");
    }
    private void ClosePin()
    {
        _pinOverlay.Hide(); _pin.Text = "";
        if (OS.HasFeature("android")) DisplayServer.VirtualKeyboardHide();
        PresentationShell.For(this)?.SetNavigationCovered(false);
    }
    private void CancelPin() { ClosePin(); _browser.Show(); }
    private void OnAccess(RoomAccessResultDto access)
    {
        var selected = _characters.Selected;
        _busy = _transport.JoinPending; _browser.Hide(); _identity.Show();
        _characters.SetTaken(access.TakenCharacters);
        if (selected is { } id && access.TakenCharacters.Contains(id)) ShowMessage("JOIN_CHARACTER_CONFLICT");
        else if (_message.Text == Tr("LOBBY_STATUS_Connecting")) _message.Hide();
        UpdateJoin();
    }
    private void OnStatus(string reason)
    {
        if (!IsVisibleInTree()) return;
        if (reason == "CharacterTaken")
        {
            _busy = false; _characters.Select(null); ShowMessage("JOIN_CHARACTER_CONFLICT"); UpdateJoin(); return;
        }
        if (reason is "Connecting" or "None" or "HostListening" or "Joined" or "PlayerLeft") return;
        Fail(reason);
    }
    private void ShowMessage(string key) { _message.Text = Tr(key); _message.Show(); }
    private void Fail(string reason)
    {
        _busy = false; ClosePin(); _identity.Hide(); _browser.Show();
        ShowMessage("LOBBY_STATUS_" + reason); _transport.Stop(); _transport.Discovery.Scan(_transport.DiscoveryPort);
    }
    private void UpdateJoin() => _join.Disabled = _busy || !LobbyProtocol.ValidName(_name.Text.Trim()) || _characters.Selected is null;
    public void ShowRooms()
    {
        _busy = false; _identity.Hide(); _browser.Show(); _message.Hide();
        if (PinOpen) ClosePin();
    }
    public bool Back()
    {
        if (PinOpen) { CancelPin(); return true; }
        if (IdentityOpen || _busy) { _transport.Stop(); ShowRooms(); _transport.Discovery.Scan(_transport.DiscoveryPort); return true; }
        return false;
    }
    public override void _ExitTree()
    {
        if (_transport is not null) { _transport.RoomAccessChanged -= OnAccess; _transport.StatusChanged -= OnStatus; }
        if (GodotObject.IsInstanceValid(_pinOverlay)) _pinOverlay.QueueFree();
    }
}

using Godot;

namespace QuizParty.Presentation;

/// <summary>Responsive device preferences view. Shell owns persistence, audio and modal privacy.</summary>
public partial class SettingsPanel : Control
{
    public event Action<PresentationPreferences>? PreferencesChanged;
    public event Action? CloseRequested;
    public event Action? PreviewRequested;
    public event Action? LeaveRequested;
    private PresentationPreferences _preferences = new();
    private MarginContainer _safe = null!;
    private PanelContainer _frame = null!;
    private PanelContainer _sign = null!;
    private VBoxContainer _layout = null!;
    private HBoxContainer _body = null!;
    private VBoxContainer _navigation = null!;
    private ScrollContainer _scroll = null!;
    private VBoxContainer _sections = null!;
    private VBoxContainer _mascotBay = null!;
    private SettingsMascot _mascot = null!;
    private TextureRect _plinth = null!;
    private Label _title = null!;
    private Label _status = null!;
    private Label _version = null!;
    private Label _volumeText = null!;
    private Label _previewHint = null!;
    private Label _detailTitle = null!;
    private Label _detailText = null!;
    private VBoxContainer _detail = null!;
    private VBoxContainer _detailActions = null!;
    private Button _cancel = null!;
    private Button _confirm = null!;
    private Button _close = null!;
    private Button _leave = null!;
    private OptionButton _language = null!;
    private HSlider _volume = null!;
    private readonly List<PanelContainer> _cards = [];
    private readonly List<Button> _tabs = [];
    private readonly Dictionary<string, CheckButton> _toggles = [];
    private readonly List<(Label Label, string Key)> _labels = [];
    private Control? _detailOpener;
    private Tween? _intro;
    private readonly List<Tween> _effects = [];
    private readonly List<TextureRect> _sparkles = [];
    private string? _detailKey;
    private int _active;
    private int _minimum = 64;
    private bool _built;
    private bool _leaveAvailable;
    private Theme? _skin;
    private HBoxContainer _header = null!;
    private Label _hint = null!;
    private GridContainer _audioGrid = null!;
    private GridContainer _gameplayGrid = null!;
    private GridContainer _actionBar = null!;
    private VBoxContainer _helpContent = null!;
    private readonly List<Button> _quickActions = [];
    public bool LandscapeLayout { get; private set; }
    public bool DetailOpen => _detail.Visible;
    public int ActiveSection => _active;

    public override void _Ready()
    {
        SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var scrim = new ColorRect { Color = new Color(0.06f, .03f, .15f, .36f), MouseFilter = MouseFilterEnum.Stop };
        AddChild(scrim); scrim.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        _safe = new MarginContainer { Name = "SafeMargin" };
        AddChild(_safe); _safe.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var outer = new VBoxContainer { Name = "Composition" }; _safe.AddChild(outer);
        _header = new HBoxContainer(); outer.AddChild(_header);
        _frame = new PanelContainer { Name = "Frame", SizeFlagsVertical = SizeFlags.ExpandFill }; outer.AddChild(_frame);
        _layout = new VBoxContainer(); _frame.AddChild(_layout);
        var header = _header;
        var sign = new PanelContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _sign = sign;
        header.AddChild(sign);
        _title = Label("UI_SETTINGS_BANNER");
        _title.HorizontalAlignment = HorizontalAlignment.Center;
        _title.VerticalAlignment = VerticalAlignment.Center;
        _title.AddThemeFontOverride("font", new FontVariation { BaseFont = ThemeDB.FallbackFont, VariationEmbolden = 1.6f });
        _title.AddThemeColorOverride("font_color", new Color("55cff5"));
        _title.AddThemeColorOverride("font_outline_color", ShowtimeTheme.Gold);
        _title.AddThemeConstantOverride("outline_size", 5);
        _title.AddThemeColorOverride("font_shadow_color", new Color("162b5e"));
        _title.AddThemeConstantOverride("shadow_offset_x", 5);
        _title.AddThemeConstantOverride("shadow_offset_y", 8); sign.AddChild(_title);
        _close = Button("Close", "UI_SETTINGS_BACK", "back"); header.AddChild(_close);
        _close.Pressed += () => { if (!Back()) CloseRequested?.Invoke(); };
        _hint = Label("UI_SETTINGS_HINT"); _hint.AddThemeFontSizeOverride("font_size", 16); _layout.AddChild(_hint);
        _body = new HBoxContainer { SizeFlagsVertical = SizeFlags.ExpandFill }; _layout.AddChild(_body);
        _navigation = new VBoxContainer { Name = "Navigation", SizeFlagsStretchRatio = .25f };
        _body.AddChild(_navigation);
        var sectionKeys = new[] { "UI_SETTINGS_AUDIO", "UI_SETTINGS_GAMEPLAY", "UI_SETTINGS_HELP" };
        var icons = new[] { "volume-high", "controller", "help" };
        for (var i = 0; i < sectionKeys.Length; i++)
        {
            var index = i;
            var tab = Button("Tab" + i, sectionKeys[i], icons[i]); tab.ToggleMode = true;
            tab.ThemeTypeVariation = "SettingsTab";
            tab.Pressed += () => SelectSection(index);
            _navigation.AddChild(tab); _tabs.Add(tab);
        }
        _scroll = new ScrollContainer { Name = "SectionsScroll", HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled,
            FollowFocus = true, FocusMode = FocusModeEnum.All,
            SizeFlagsHorizontal = SizeFlags.ExpandFill, SizeFlagsVertical = SizeFlags.ExpandFill };
        _body.AddChild(_scroll);
        _scroll.GuiInput += @event =>
        {
            if (@event is not InputEventKey { Pressed: true } key) return;
            var step = key.Keycode switch { Key.Down => 64, Key.Up => -64,
                Key.Pagedown => (int)_scroll.Size.Y, Key.Pageup => -(int)_scroll.Size.Y, _ => 0 };
            if (step != 0) { _scroll.ScrollVertical += step; _scroll.AcceptEvent(); }
        };
        _sections = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _scroll.AddChild(_sections);
        var audio = Card(sectionKeys[0]);
        _audioGrid = new GridContainer { Columns = 1 }; audio.AddChild(_audioGrid);
        var soundControls = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _audioGrid.AddChild(soundControls);
        var soundPreview = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _audioGrid.AddChild(soundPreview);
        AddToggle(soundControls, "Sound", "UI_SETTINGS_SFX", value => Change(_preferences with { Sound = value }));
        var volumeHeader = new HBoxContainer(); soundControls.AddChild(volumeHeader);
        var volumeLabel = Label("UI_VOLUME"); volumeLabel.SizeFlagsHorizontal = SizeFlags.ExpandFill; volumeHeader.AddChild(volumeLabel);
        _volumeText = new Label { Name = "VolumeValue", Text = "65%", CustomMinimumSize = new(74, 0) };
        _volumeText.SetMeta("presentation_no_wrap", true); volumeHeader.AddChild(_volumeText);
        _volume = new HSlider { Name = "Volume", MinValue = 0, MaxValue = 100, Step = 5,
            CustomMinimumSize = new(0, 64), FocusMode = FocusModeEnum.All, Scrollable = false };
        soundControls.AddChild(_volume);
        _volume.ValueChanged += value => Change(_preferences with { Volume = (float)value / 100 });
        _volume.GuiInput += @event =>
        {
            if (@event is InputEventKey { Pressed: true } key && key.Keycode is Key.Home or Key.End)
            { _volume.Value = key.Keycode == Key.Home ? 0 : 100; _volume.AcceptEvent(); }
        };
        var preview = Button("Preview", "UI_SOUND_PREVIEW", "volume-high"); soundPreview.AddChild(preview);
        preview.Pressed += () =>
        {
            if (_preferences.Sound && _preferences.Volume > 0) { PreviewRequested?.Invoke(); _mascot.React(false); }
        };
        _previewHint = Label("UI_SETTINGS_AUDIO_HINT"); _previewHint.AddThemeFontSizeOverride("font_size", 18); soundPreview.AddChild(_previewHint);
        var gameplay = Card(sectionKeys[1]);
        _gameplayGrid = new GridContainer { Columns = 1 }; gameplay.AddChild(_gameplayGrid);
        var languageControls = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _gameplayGrid.AddChild(languageControls);
        var accessibilityControls = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _gameplayGrid.AddChild(accessibilityControls);
        languageControls.AddChild(Label("UI_SETTINGS_LANGUAGE"));
        _language = new OptionButton { Name = "Language", CustomMinimumSize = new(0, 64), FitToLongestItem = false };
        _language.AddItem("Ελληνικά"); _language.AddItem("English"); languageControls.AddChild(_language);
        _language.ItemSelected += index => Change(_preferences with { Language = index == 0 ? "el_GR" : "en" });
        var languageHint = Label("UI_SETTINGS_LANGUAGE_HINT"); languageHint.AddThemeFontSizeOverride("font_size", 17); languageControls.AddChild(languageHint);
        AddToggle(accessibilityControls, "ReducedMotion", "UI_REDUCED_MOTION", value => Change(_preferences with { ReducedMotion = value }));
        AddToggle(accessibilityControls, "LargeText", "UI_LARGE_TEXT", value => Change(_preferences with { LargeText = value }));
        AddToggle(accessibilityControls, "HighContrast", "UI_HIGH_CONTRAST", value => Change(_preferences with { HighContrast = value }));
        var help = Card(sectionKeys[2]);
        _helpContent = help;
        foreach (var (name, key) in new[] { ("Credits", "UI_SETTINGS_CREDITS"), ("Privacy", "UI_SETTINGS_PRIVACY"),
            ("About", "UI_SETTINGS_ABOUT"), ("Reset", "UI_SETTINGS_RESET") })
        {
            var button = Button(name, key, name == "Reset" ? "gear" : "help"); help.AddChild(button);
            if (name != "About") _quickActions.Add(button);
            if (name == "Reset") button.ThemeTypeVariation = "SettingsReset";
            button.Pressed += () => ShowDetail(name, button);
        }
        _detail = new VBoxContainer { Name = "Detail", Visible = false, SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _sections.AddChild(_detail);
        _detailTitle = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart }; _detail.AddChild(_detailTitle);
        _detailTitle.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
        _detailTitle.AddThemeFontSizeOverride("font_size", 30);
        _detailText = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart }; _detail.AddChild(_detailText);
        _detailActions = new VBoxContainer(); _detail.AddChild(_detailActions);
        _cancel = Button("DetailBack", "UI_SETTINGS_BACK", "back"); _detailActions.AddChild(_cancel);
        _cancel.Pressed += () => Back();
        _confirm = Button("ConfirmReset", "UI_SETTINGS_CONFIRM_RESET", "gear"); _detailActions.AddChild(_confirm);
        _confirm.Pressed += () => { Change(new PresentationPreferences()); Back(); Sparkle(); _mascot.React(false); };
        _mascotBay = new VBoxContainer { Name = "MascotBay", MouseFilter = MouseFilterEnum.Ignore };
        _mascotBay.AddThemeConstantOverride("separation", 4);
        _body.AddChild(_mascotBay);
        var spacer = new Control { SizeFlagsVertical = SizeFlags.ExpandFill, MouseFilter = MouseFilterEnum.Ignore };
        _mascotBay.AddChild(spacer);
        _mascot = new SettingsMascot { Name = "Mascot", CustomMinimumSize = new(180, 220) }; _mascotBay.AddChild(_mascot);
        _plinth = new TextureRect { Texture = SettingsSkin.Texture("mascot-plinth"), CustomMinimumSize = new(180, 45),
            ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize, StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered,
            MouseFilter = MouseFilterEnum.Ignore }; _mascotBay.AddChild(_plinth);
        _actionBar = new GridContainer { Name = "QuickActions", Columns = 3 }; _layout.AddChild(_actionBar);
        _status = new Label { Name = "SaveStatus", AutowrapMode = TextServer.AutowrapMode.WordSmart }; _layout.AddChild(_status);
        _status.AddThemeFontSizeOverride("font_size", 17);
        _version = new Label { Name = "Version", AutowrapMode = TextServer.AutowrapMode.WordSmart }; _layout.AddChild(_version);
        _version.AddThemeFontSizeOverride("font_size", 16);
        _leave = Button("LeaveParty", "UI_LEAVE_PARTY"); _leave.Visible = false;
        _leave.Pressed += () => LeaveRequested?.Invoke(); _layout.AddChild(_leave);
        _built = true;
        Resized += Reflow;
        VisibilityChanged += () => { if (!Visible) StopEffects(); };
        Render(_preferences, 64);
    }

    private Label Label(string key)
    {
        var label = new Label { Text = key, AutowrapMode = TextServer.AutowrapMode.WordSmart,
            MouseFilter = MouseFilterEnum.Ignore };
        _labels.Add((label, key)); return label;
    }

    private static Button Button(string name, string key, string? icon = null) => new()
    {
        Name = name, Text = key, Icon = icon is null ? null : SettingsSkin.Texture("icon-" + icon),
        ExpandIcon = true, IconAlignment = HorizontalAlignment.Left, CustomMinimumSize = new(64, 64),
        SizeFlagsHorizontal = SizeFlags.ExpandFill, AutowrapMode = TextServer.AutowrapMode.WordSmart
    };

    private VBoxContainer Card(string key)
    {
        var frame = new PanelContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _sections.AddChild(frame); _cards.Add(frame);
        var content = new VBoxContainer(); frame.AddChild(content);
        var heading = Label(key); heading.AddThemeFontSizeOverride("font_size", 28);
        heading.AddThemeColorOverride("font_color", ShowtimeTheme.Gold); content.AddChild(heading);
        return content;
    }

    private void AddToggle(VBoxContainer parent, string name, string key, Action<bool> changed)
    {
        var row = new HBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; parent.AddChild(row);
        var label = Label(key); label.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        row.AddChild(label);
        var toggle = new SettingsToggle { Name = name, CustomMinimumSize = new(0, 64),
            AutowrapMode = TextServer.AutowrapMode.WordSmart, ExpandIcon = false };
        toggle.SetMeta("settings_key", key);
        toggle.Toggled += value => changed(value); row.AddChild(toggle); _toggles.Add(name, toggle);
    }

    private void Change(PresentationPreferences preferences)
    {
        var muted = _preferences.Sound && !preferences.Sound;
        PreferencesChanged?.Invoke(preferences);
        if (muted) _mascot.React(true);
    }

    public void Render(PresentationPreferences preferences, int minimum, string status = "")
    {
        var restyle = _skin is null || _preferences.LargeText != preferences.LargeText ||
            _preferences.HighContrast != preferences.HighContrast || _minimum != minimum;
        _preferences = preferences; _minimum = minimum;
        foreach (var button in FindChildren("*", "BaseButton", true, false).OfType<BaseButton>())
            button.CustomMinimumSize = new(minimum, minimum);
        _volume.CustomMinimumSize = new(minimum, minimum);
        if (restyle)
        {
            var previous = _skin; _skin = SettingsSkin.Create(preferences, minimum); Theme = _skin; previous?.Dispose();
            using StyleBox frameStyle = preferences.HighContrast
                ? ShowtimeTheme.Panel(new("080a16"), ShowtimeTheme.Ink, 3) : SettingsSkin.Slice("frame-main", 44, 40);
            _frame.AddThemeStyleboxOverride("panel", frameStyle);
            using var headerSkin = SettingsSkin.Slice("header-trim", 70, 12);
            headerSkin.SetTextureMargin(Side.Top, 18); headerSkin.SetTextureMargin(Side.Bottom, 18);
            using var plainHeader = ShowtimeTheme.Panel(new("080a16"), ShowtimeTheme.Ink);
            using var emptyHeader = new StyleBoxEmpty();
            _sign.AddThemeStyleboxOverride("panel", preferences.HighContrast ? plainHeader : emptyHeader);
            _title.AddThemeConstantOverride("outline_size", preferences.HighContrast ? 0 : 8);
            _title.AddThemeConstantOverride("shadow_offset_y", preferences.HighContrast ? 0 : 8);
            foreach (var card in _cards)
            {
                using StyleBox cardStyle = preferences.HighContrast
                    ? ShowtimeTheme.Panel(new("080a16"), ShowtimeTheme.Ink) : SettingsSkin.Slice("frame-card", 22, 20);
                card.AddThemeStyleboxOverride("panel", cardStyle);
            }
        }
        foreach (var (name, value) in new[] { ("Sound", preferences.Sound), ("ReducedMotion", preferences.ReducedMotion),
            ("LargeText", preferences.LargeText), ("HighContrast", preferences.HighContrast) })
        {
            var toggle = _toggles[name]; toggle.SetPressedNoSignal(value);
            toggle.Text = value ? "✓" : "–";
            toggle.CustomMinimumSize = new(168, minimum);
            toggle.TooltipText = Tr(value ? "UI_SETTINGS_ON" : "UI_SETTINGS_OFF");
            toggle.AccessibilityName = Tr(toggle.GetMeta("settings_key").AsString()) + ": " + toggle.TooltipText;
            ((SettingsToggle)toggle).Sync(preferences.ReducedMotion, preferences.HighContrast);
        }
        _volume.SetValueNoSignal(preferences.Volume * 100);
        _volumeText.Text = $"{preferences.Volume * 100:0}%";
        _volume.AccessibilityName = Tr("UI_VOLUME");
        _scroll.AccessibilityName = Tr("UI_SETTINGS_BANNER");
        _language.Select(preferences.Language == "en" ? 1 : 0);
        _language.AccessibilityName = Tr("UI_SETTINGS_LANGUAGE");
        _previewHint.Text = preferences.Sound && preferences.Volume > 0 ? "UI_SETTINGS_AUDIO_HINT" : "UI_SETTINGS_MUTED";
        _status.Text = status;
        _status.Visible = status.Length > 0;
        _version.Visible = !_status.Visible;
        var version = ProjectSettings.GetSetting("application/config/version", "").AsString();
        _version.Text = string.Format(Tr("UI_SETTINGS_VERSION"), string.IsNullOrWhiteSpace(version) ? Tr("UI_SETTINGS_DEVELOPMENT") : version)
            + "  ·  Godot " + Engine.GetVersionInfo()["string"].AsString();
        foreach (var (label, _) in _labels)
        {
            if (!label.HasThemeFontSizeOverride("font_size") || label == _title) continue;
            if (!label.HasMeta("settings_font")) label.SetMeta("settings_font", label.GetThemeFontSize("font_size"));
            label.AddThemeFontSizeOverride("font_size", (int)(label.GetMeta("settings_font").AsInt32() * (preferences.LargeText ? 1.2f : 1)));
        }
        RefreshDetail();
        if (preferences.ReducedMotion || preferences.HighContrast) StopEffects();
        Reflow();
    }

    public void SetLeaveAvailable() { _leaveAvailable = true; _leave.Show(); }

    public void Open()
    {
        Show(); _scroll.ScrollVertical = 0;
        SelectSection(_active);
        (LandscapeLayout ? _tabs[_active] : _close).GrabFocus();
        if (!_preferences.ReducedMotion)
        {
            _frame.PivotOffset = _frame.Size / 2; _frame.Scale = new(.96f, .96f); _frame.Modulate = new(1, 1, 1, 0);
            _intro = CreateTween().SetParallel();
            _intro.TweenProperty(_frame, "scale", Vector2.One, .2).SetTrans(Tween.TransitionType.Back).SetEase(Tween.EaseType.Out);
            _intro.TweenProperty(_frame, "modulate:a", 1f, .18);
        }
        _mascot.Wave();
    }

    public void Dismiss()
    {
        if (DetailOpen) Back();
        StopEffects(); Hide();
    }

    public void SelectSection(int index)
    {
        _active = Math.Clamp(index, 0, 2);
        UpdateSections();
        if (LandscapeLayout) _scroll.ScrollVertical = 0;
    }

    private void UpdateSections()
    {
        for (var i = 0; i < _cards.Count; i++)
        {
            _cards[i].Visible = !DetailOpen && (!LandscapeLayout || i == _active);
            _tabs[i].SetPressedNoSignal(i == _active);
            _tabs[i].Text = (i == _active ? "▸ " : "") + Tr(new[] { "UI_SETTINGS_AUDIO", "UI_SETTINGS_GAMEPLAY", "UI_SETTINGS_HELP_TAB" }[i]);
        }
    }

    private void Reflow()
    {
        if (!_built) return;
        var focus = GetViewport().GuiGetFocusOwner();
        var wide = Size.X >= (_preferences.LargeText ? 1100 : 900) && Size.X > Size.Y;
        if (wide && !LandscapeLayout && focus is not null)
            for (var i = 0; i < _cards.Count; i++)
                if (_cards[i].IsAncestorOf(focus)) _active = i;
        var changed = wide != LandscapeLayout;
        LandscapeLayout = wide;
        foreach (var edge in new[] { "left", "right", "top", "bottom" })
            _safe.AddThemeConstantOverride("margin_" + edge, wide ? 24 : 12);
        _navigation.Visible = wide && !DetailOpen;
        _leave.Visible = _leaveAvailable && !DetailOpen;
        var leaveParent = wide ? (Node)_header : _helpContent;
        if (_leave.GetParent() != leaveParent) _leave.Reparent(leaveParent);
        _leave.CustomMinimumSize = new(wide ? 180 : _minimum, _minimum);
        _leave.SizeFlagsHorizontal = wide ? SizeFlags.ShrinkEnd : SizeFlags.ExpandFill;
        _leave.Text = "UI_SETTINGS_LEAVE_SHORT";
        _leave.AccessibilityName = Tr("UI_LEAVE_PARTY");
        _navigation.CustomMinimumSize = new(wide ? 200 : 0, 0);
        _navigation.AddThemeConstantOverride("separation", 18);
        foreach (var tab in _tabs) tab.CustomMinimumSize = new(0, Math.Max(_minimum, wide ? 80 : 64));
        foreach (var tab in _tabs) tab.AddThemeFontSizeOverride("font_size", _preferences.LargeText ? 25 : 22);
        _title.AddThemeFontSizeOverride("font_size", wide ? 76 : _preferences.LargeText ? 38 : 40);
        _sign.CustomMinimumSize = new(0, wide ? 110 : 76);
        using StyleBox signStyle = _preferences.HighContrast
            ? ShowtimeTheme.Panel(new("080a16"), ShowtimeTheme.Ink)
            : wide ? new StyleBoxEmpty() : SettingsSkin.Slice("header-trim", 24, 10);
        _sign.AddThemeStyleboxOverride("panel", signStyle);
        _header.MoveChild(_close, wide ? 0 : 1);
        _hint.Visible = !wide;
        _audioGrid.Columns = wide && !_preferences.LargeText ? 2 : 1;
        _gameplayGrid.Columns = wide && Size.X >= 1400 && !_preferences.LargeText ? 2 : 1;
        _actionBar.Visible = wide && !DetailOpen;
        _actionBar.Columns = Size.X >= 1100 ? 3 : 2;
        foreach (var action in _quickActions)
        {
            if (action.Name == "Reset")
            {
                action.Text = wide ? "UI_SETTINGS_RESET_SHORT" : "UI_SETTINGS_RESET";
                action.AccessibilityName = Tr("UI_SETTINGS_RESET");
            }
            var parent = wide ? (Node)_actionBar : _helpContent;
            if (action.GetParent() != parent) action.Reparent(parent);
        }
        _close.Text = wide ? "UI_SETTINGS_BACK" : "";
        _close.AccessibilityName = Tr("UI_SETTINGS_BACK");
        _close.TooltipText = Tr("UI_SETTINGS_BACK");
        _close.SizeFlagsHorizontal = SizeFlags.ShrinkEnd;
        _close.CustomMinimumSize = new(wide ? Math.Max(160, _minimum) : _minimum, _minimum);
        _close.AddThemeFontSizeOverride("font_size", _preferences.LargeText ? 25 : 22);
        // Reparent only decoration; all focusable controls remain the same instances.
        var destination = wide ? (Node)_body : _layout;
        if (_mascotBay.GetParent() != destination) _mascotBay.Reparent(destination);
        _mascotBay.Visible = !_preferences.HighContrast && !DetailOpen && Size.Y >= 560;
        _mascotBay.CustomMinimumSize = new(wide ? 240 : 100, 0);
        _mascotBay.SizeFlagsHorizontal = wide ? SizeFlags.Fill : SizeFlags.ShrinkEnd;
        // Overlap the atlas's transparent foot gutter with the pedestal surface.
        _mascotBay.AddThemeConstantOverride("separation", wide ? -12 : -6);
        _mascot.CustomMinimumSize = wide ? new(240, 220) : new(100, 80);
        _plinth.CustomMinimumSize = wide ? new(240, 64) : new(100, 24);
        _mascot.Configure(!wide, _preferences.ReducedMotion || _preferences.HighContrast);
        UpdateSections();
        if (changed && focus is not null && IsAncestorOf(focus) && !focus.IsVisibleInTree())
            (wide ? _tabs[_active] : _toggles["Sound"]).GrabFocus();
        else if (changed && focus is not null && IsAncestorOf(focus) && focus.IsVisibleInTree() && !focus.HasFocus())
            focus.GrabFocus();
        if (focus is not null && _scroll.IsAncestorOf(focus) && focus.IsVisibleInTree())
            Callable.From(() => { if (GodotObject.IsInstanceValid(focus) && focus.IsInsideTree()) _scroll.EnsureControlVisible(focus); }).CallDeferred();
    }

    public void ShowDetail(string key, Control opener)
    {
        _detailOpener = opener; _detailKey = key; _detail.Show();
        _confirm.Visible = key == "Reset";
        _cancel.Text = key == "Reset" ? "UI_SETTINGS_CANCEL" : "UI_SETTINGS_BACK";
        RefreshDetail(); Reflow();
        (key == "Reset" ? _cancel : _close).GrabFocus(); _scroll.ScrollVertical = 0;
    }

    private void RefreshDetail()
    {
        if (_detailKey is null) return;
        var prefix = "UI_SETTINGS_" + _detailKey.ToUpperInvariant();
        _detailTitle.Text = prefix;
        _detailText.Text = _detailKey == "About" ? string.Format(Tr(prefix + "_BODY"), _version.Text)
            : Tr(prefix + "_BODY");
        if (_detailKey == "Credits") _detailText.Text += "\n\n" + EngineNotices();
    }

    private static string EngineNotices()
    {
        var notices = new System.Text.StringBuilder(Engine.GetLicenseText());
        foreach (var component in Engine.GetCopyrightInfo())
        {
            notices.AppendLine().AppendLine(component["name"].AsString());
            foreach (var part in component["parts"].AsGodotArray())
            {
                var info = part.AsGodotDictionary();
                foreach (var owner in info["copyright"].AsGodotArray()) notices.AppendLine(owner.AsString());
                notices.AppendLine(info["license"].AsString());
            }
        }
        foreach (var license in Engine.GetLicenseInfo())
            notices.AppendLine().AppendLine(license.Key.AsString()).AppendLine(license.Value.AsString());
        return notices.ToString();
    }

    public bool Back()
    {
        if (!DetailOpen) return false;
        _detail.Hide(); _detailKey = null; Reflow();
        if (_detailOpener is { } opener && GodotObject.IsInstanceValid(opener) && opener.IsVisibleInTree()) opener.GrabFocus();
        _detailOpener = null; return true;
    }

    private void Sparkle()
    {
        if (_preferences.ReducedMotion || _preferences.HighContrast) return;
        StopSparkles();
        for (var i = 0; i < 8; i++)
        {
            var star = new TextureRect { Texture = SettingsSkin.Texture("sparkle-gold"), Size = new(18, 18),
                Position = new(Size.X - 50, Size.Y - 60), MouseFilter = MouseFilterEnum.Ignore };
            AddChild(star); _sparkles.Add(star);
            var tween = star.CreateTween().SetParallel(); _effects.Add(tween);
            tween.TweenProperty(star, "position", star.Position + new Vector2(-25 - i * 14, -20 - (i % 3) * 18), .35);
            tween.TweenProperty(star, "modulate:a", 0f, .35);
            tween.Finished += () => { _effects.Remove(tween); _sparkles.Remove(star); star.QueueFree(); };
        }
    }

    private void StopSparkles()
    {
        foreach (var tween in _effects) if (tween.IsValid()) tween.Kill();
        _effects.Clear();
        foreach (var star in _sparkles) if (GodotObject.IsInstanceValid(star)) star.QueueFree();
        _sparkles.Clear();
    }

    private void StopEffects()
    {
        if (_intro?.IsValid() == true) _intro.Kill();
        _intro = null; _frame.Scale = Vector2.One; _frame.Modulate = Colors.White; StopSparkles();
    }

    public override void _ExitTree()
    {
        StopEffects(); Theme = null; _skin?.Dispose(); _skin = null;
    }
}

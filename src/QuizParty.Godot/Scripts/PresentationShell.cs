using Godot;

namespace QuizParty.Presentation;

/// <summary>Scene-owned presentation service. No global state, game rules or network intents.</summary>
public partial class PresentationShell : Control
{
    public string SettingsPath { get; set; } = "user://presentation.cfg";
    public PresentationPreferences Preferences { get; private set; } = new();
    private Control _root = null!;
    private SettingsPanel _overlay = null!;
    private Button _settings = null!;
    private AudioStreamPlayer _audio = null!;
    private readonly Dictionary<string, AudioStreamWav> _sounds = [];
    private readonly Dictionary<Control, Tween> _fades = [];
    private readonly List<Control> _hidden = [];
    private bool _previousQuitOnBack;
    public bool SettingsOpen => _overlay.Visible;
    public int MinimumTarget { get; private set; } = 64;

    public override void _Ready()
    {
        _root = (Control)GetParent();
        var previewArgs = OS.IsDebugBuild() ? MatchProcessProbe.LaunchArguments().Select(argument =>
            argument.StartsWith("--match-ui-", StringComparison.Ordinal) ? "--ui-" + argument["--match-ui-".Length..] : argument).ToArray() : [];
        if (previewArgs.Contains("--ui-greek")) TranslationServer.SetLocale("el_GR");
        if (OS.HasFeature("android"))
        {
            if (previewArgs.Contains("--ui-portrait")) DisplayServer.ScreenSetOrientation(DisplayServer.ScreenOrientation.Portrait);
            if (previewArgs.Contains("--ui-landscape")) DisplayServer.ScreenSetOrientation(DisplayServer.ScreenOrientation.Landscape);
        }
        _previousQuitOnBack = GetTree().QuitOnGoBack;
        GetTree().QuitOnGoBack = false;
        MouseFilter = MouseFilterEnum.Ignore;
        SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        Preferences = PresentationPreferences.Load(SettingsPath);
        if (previewArgs.Contains("--ui-preview")) Preferences = new();
        if (previewArgs.Contains("--ui-english")) Preferences = Preferences with { Language = "en" };
        if (previewArgs.Contains("--ui-greek")) Preferences = Preferences with { Language = "el_GR" };
        TranslationServer.SetLocale(Preferences.Language);
        _root.Theme = ShowtimeTheme.Create(Preferences);
        if (OS.IsDebugBuild() && OS.HasFeature("android")) GetTree().CreateTimer(.6).Timeout += () =>
        {
            if (!GodotObject.IsInstanceValid(this) || !IsInsideTree()) return;
            var scale = ResponsiveCanvas.PixelsPerUnit(GetWindow().Size, _root.GetViewportRect().Size);
            GD.Print($"PRESENTATION TOUCH dpi={DisplayServer.ScreenGetDpi()} scale={scale} window={GetWindow().Size} viewport={_root.GetViewportRect().Size} logicalMinimum={MinimumTarget} headerSize={_settings.Size} accessibilityBackend={AccessibilityServer.IsSupported()}");
        };
        var backdrop = new StageBackdrop { Name = "StageBackdrop", HighContrast = Preferences.HighContrast };
        _root.AddChild(backdrop); _root.MoveChild(backdrop, 0);
        backdrop.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        _audio = new AudioStreamPlayer { Name = "FeedbackAudio" };
        AddChild(_audio);
        _settings = new Button { Name = "Settings", Icon = GD.Load<Texture2D>("res://Art/settings.svg"), IconAlignment = HorizontalAlignment.Center, AccessibilityName = Tr("UI_SETTINGS"),
            TooltipText = Tr("UI_SETTINGS"), CustomMinimumSize = new(64, 64) };
        AddChild(_settings);
        _settings.SetAnchorsAndOffsetsPreset(LayoutPreset.TopRight);
        _settings.OffsetLeft = -84; _settings.OffsetRight = -20; _settings.OffsetTop = 12; _settings.OffsetBottom = 76;
        if (_root is not AppRoot)
        {
            var wordmark = new Label { Text = "APP_TITLE", MouseFilter = MouseFilterEnum.Ignore };
            wordmark.AddThemeFontSizeOverride("font_size", 28);
            wordmark.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
            AddChild(wordmark); wordmark.Position = new(28, 24); wordmark.Size = new(240, 52);
        }
        _settings.Pressed += OpenSettings;
        BuildSettings();
        StyleTree(_root);
        if (_root is AppRoot home) home.FitTitle();
        GetTree().NodeAdded += OnNodeAdded;
        // Explicit debug-only capture options never persist or alter gameplay.
        if (OS.IsDebugBuild())
        {
            var args = previewArgs;
            if (args.Any(a => a.StartsWith("--ui-", StringComparison.Ordinal)))
            {
                Apply(Preferences with { LargeText = args.Contains("--ui-large-text") || Preferences.LargeText,
                    HighContrast = args.Contains("--ui-high-contrast") || Preferences.HighContrast,
                    ReducedMotion = args.Contains("--ui-reduced-motion") || Preferences.ReducedMotion,
                    Sound = !args.Contains("--ui-mute") && Preferences.Sound }, persist: false);
                if (args.Contains("--ui-settings")) Callable.From(() =>
                {
                    if (!GodotObject.IsInstanceValid(this) || !IsInsideTree()) return;
                    OpenSettings();
                    if (args.Contains("--ui-gameplay")) _overlay.SelectSection(1);
                    if (args.Contains("--ui-help")) _overlay.SelectSection(2);
                }).CallDeferred();
                if (args.Contains("--ui-sound-preview")) GetTree().CreateTimer(.1).Timeout += () =>
                { if (GodotObject.IsInstanceValid(this) && IsInsideTree()) PlayCue("reveal"); };
                if (args.FirstOrDefault(a => a.StartsWith("--ui-capture=", StringComparison.Ordinal)) is { } capture)
                    _ = CaptureAsync(capture["--ui-capture=".Length..]);
            }
        }
    }

    private async Task CaptureAsync(string path)
    {
        try
        {
            await ToSignal(GetTree().CreateTimer(.45), global::Godot.Timer.SignalName.Timeout);
            if (!GodotObject.IsInstanceValid(this) || !IsInsideTree()) return;
            await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
            if (!GodotObject.IsInstanceValid(this) || !IsInsideTree()) return;
            using var image = GetViewport().GetTexture().GetImage();
            if (SettingsOpen) GD.Print($"SETTINGS layout={_overlay.LandscapeLayout} size={_overlay.Size} min={_overlay.GetCombinedMinimumSize()} frameMin={_overlay.GetNode<Control>("SafeMargin/Composition/Frame").GetCombinedMinimumSize()}");
            var error = image.SavePng(path);
            GD.Print($"PRESENTATION CAPTURE {error} {image.GetWidth()}x{image.GetHeight()}");
            GetTree().Quit(error == Error.Ok ? 0 : 1);
        }
        catch (Exception error) { GD.PushError($"Presentation capture failed: {error.Message}"); if (IsInsideTree()) GetTree().Quit(1); }
    }

    public static PresentationShell? For(Node node)
    {
        for (Node? current = node; current is not null; current = current.GetParent())
            if (current.GetNodeOrNull<PresentationShell>("PresentationShell") is { } shell) return shell;
        return null;
    }

    private void OnNodeAdded(Node node)
    {
        if (_root.IsAncestorOf(node)) StyleControl(node);
    }

    private void StyleTree(Node node)
    {
        StyleControl(node);
        foreach (var child in node.GetChildren()) StyleTree(child);
    }

    private void StyleControl(Node node)
    {
        if (node is not Control control) return;
        if (control is Button or LineEdit or Slider && !control.HasMeta("presentation_minimum"))
            control.SetMeta("presentation_minimum", control.CustomMinimumSize);
        if (control is Button button)
        {
            var baseline = button.GetMeta("presentation_minimum").AsVector2();
            button.CustomMinimumSize = new(Math.Max(MinimumTarget, baseline.X), Math.Max(MinimumTarget, baseline.Y));
            button.AutowrapMode = button.HasMeta("presentation_no_wrap") ? TextServer.AutowrapMode.Off : TextServer.AutowrapMode.WordSmart;
            button.FocusMode = FocusModeEnum.All;
            if (!button.HasMeta("presentation_hooked"))
            {
                button.SetMeta("presentation_hooked", true);
                button.Pressed += () => PlayCue("tap");
            }
        }
        if (control is LineEdit edit)
        {
            edit.CustomMinimumSize = new(0, Math.Max(MinimumTarget, edit.GetMeta("presentation_minimum").AsVector2().Y));
            // Full player names/IPs scroll within the field instead of forcing viewport width.
            edit.ExpandToTextLength = false;
            edit.AccessibilityName = Tr(edit.PlaceholderText);
        }
        if (control is Slider slider)
            slider.CustomMinimumSize = new(MinimumTarget, Math.Max(MinimumTarget, slider.GetMeta("presentation_minimum").AsVector2().Y));
        if (control is Label label) label.AutowrapMode = label.HasMeta("presentation_no_wrap") ? TextServer.AutowrapMode.Off : TextServer.AutowrapMode.WordSmart;
        if (control is ScrollContainer scroll) scroll.FollowFocus = true;
        if (!control.HasMeta("presentation_font") && control.HasThemeFontSizeOverride("font_size"))
            control.SetMeta("presentation_font", control.GetThemeFontSize("font_size"));
        if (control.HasMeta("presentation_font"))
            control.AddThemeFontSizeOverride("font_size", (int)Math.Round(control.GetMeta("presentation_font").AsInt32() * (Preferences.LargeText ? 1.2 : 1)));
    }

    private void BuildSettings()
    {
        _overlay = GD.Load<PackedScene>("res://Scenes/SettingsPanel.tscn").Instantiate<SettingsPanel>();
        _overlay.Name = "SettingsOverlay";
        _overlay.Visible = false;
        AddChild(_overlay);
        _overlay.PreferencesChanged += preferences => Apply(preferences);
        _overlay.CloseRequested += CloseSettings;
        _overlay.PreviewRequested += () => PlayCue("reveal");
        _overlay.Render(Preferences, MinimumTarget);
    }

    public void SetLeaveAction(Action action)
    {
        _overlay.LeaveRequested += action;
        _overlay.SetLeaveAvailable();
    }
    public void OpenSettings()
    {
        if (SettingsOpen) return;
        _hidden.Clear();
        // Hidden scene content cannot receive keyboard focus or reveal private panels behind settings.
        foreach (var control in _root.GetChildren().OfType<Control>().Where(c => c != this && c is not StageBackdrop && c.Visible))
        { _hidden.Add(control); control.Hide(); }
        _settings.Hide(); _overlay.Open();
    }

    public void CloseSettings()
    {
        if (!SettingsOpen) return;
        _overlay.Dismiss();
        foreach (var control in _hidden.Where(GodotObject.IsInstanceValid)) control.Show();
        _hidden.Clear(); _settings.Show(); _settings.GrabFocus();
    }

    public void UpdateInsets(Vector4 inset)
    {
        if (OS.HasFeature("android"))
        {
            var scale = ResponsiveCanvas.PixelsPerUnit(GetWindow().Size, _root.GetViewportRect().Size);
            var minimum = ResponsiveCanvas.MinimumLogicalTarget(DisplayServer.ScreenGetDpi(), scale);
            if (minimum != MinimumTarget)
            {
                MinimumTarget = minimum; _root.Theme = ShowtimeTheme.Create(Preferences, MinimumTarget);
                StyleTree(_root); _overlay.Render(Preferences, MinimumTarget);
            }
        }
        _settings.OffsetLeft = -20 - MinimumTarget - inset.Z; _settings.OffsetRight = -20 - inset.Z;
        _settings.OffsetTop = 12 + inset.Y; _settings.OffsetBottom = 12 + MinimumTarget + inset.Y;
        _overlay.OffsetLeft = inset.X; _overlay.OffsetTop = inset.Y;
        _overlay.OffsetRight = -inset.Z; _overlay.OffsetBottom = -inset.W;
    }

    public void Apply(PresentationPreferences preferences, bool persist = true)
    {
        Preferences = preferences;
        TranslationServer.SetLocale(preferences.Language);
        _settings.AccessibilityName = Tr("UI_SETTINGS"); _settings.TooltipText = Tr("UI_SETTINGS");
        _root.Theme = ShowtimeTheme.Create(Preferences, MinimumTarget);
        var backdrop = _root.GetNode<StageBackdrop>("StageBackdrop");
        backdrop.HighContrast = preferences.HighContrast; backdrop.QueueRedraw();
        StyleTree(_root);
        if (_root is AppRoot home) home.FitTitle();
        if (!Preferences.Sound || Preferences.Volume == 0) _audio.Stop();
        _audio.VolumeDb = Mathf.LinearToDb(Math.Max(.0001f, Preferences.Volume));
        if (Preferences.ReducedMotion)
        {
            foreach (var (control, tween) in _fades)
            { if (tween.IsValid()) tween.Kill(); if (GodotObject.IsInstanceValid(control)) control.Modulate = Colors.White; }
            _fades.Clear();
        }
        var error = persist ? preferences.Save(SettingsPath) : Error.Ok;
        _overlay.Render(preferences, MinimumTarget, !persist ? "" : error == Error.Ok ? "UI_SAVED" : "UI_SAVE_FAILED");
        if (error != Error.Ok) GD.PushWarning($"Presentation settings could not save: {error}");
    }

    public void Fade(Control control)
    {
        if (_fades.Remove(control, out var previous) && previous.IsValid()) previous.Kill();
        control.Modulate = Colors.White;
        if (Preferences.ReducedMotion || !control.IsInsideTree()) return;
        control.Modulate = new Color(1, 1, 1, .82f);
        var tween = control.CreateTween(); _fades[control] = tween;
        tween.TweenProperty(control, "modulate:a", 1.0, .16);
        tween.Finished += () => _fades.Remove(control);
    }

    public void PlayCue(string cue)
    {
        if (!Preferences.Sound || Preferences.Volume <= 0) return;
        if (cue == "tap" && _audio.Playing) return;
        if (!_sounds.TryGetValue(cue, out var stream)) _sounds[cue] = stream = CreateTone(cue);
        _audio.Stream = stream; _audio.VolumeDb = Mathf.LinearToDb(Preferences.Volume); _audio.Play();
    }

    private static AudioStreamWav CreateTone(string cue)
    {
        // Original soft sine arpeggios, generated locally; no downloaded/licensed audio assets.
        var notes = cue switch { "final" => new[] { 523.25, 659.25, 783.99, 1046.5 }, "reveal" => new[] { 523.25, 783.99 },
            "card" => new[] { 659.25, 880.0 }, _ => new[] { 440.0 } };
        var seconds = cue == "tap" ? .055 : .28;
        const int rate = 22050;
        var samples = (int)(rate * seconds); var data = new byte[samples * 2];
        for (var i = 0; i < samples; i++)
        {
            var time = (double)i / rate;
            var note = Math.Min(notes.Length - 1, (int)(time / seconds * notes.Length));
            var local = time % (seconds / notes.Length);
            var envelope = Math.Min(1, local / .008) * Math.Min(1, (seconds / notes.Length - local) / .025);
            var sample = (short)(Math.Sin(2 * Math.PI * notes[note] * time) * envelope * 6500);
            data[i * 2] = (byte)(sample & 255); data[i * 2 + 1] = (byte)((sample >> 8) & 255);
        }
        return new AudioStreamWav { Format = AudioStreamWav.FormatEnum.Format16Bits, MixRate = rate, Data = data };
    }

    public override void _UnhandledKeyInput(InputEvent @event)
    {
        if (SettingsOpen && @event is InputEventKey { Pressed: true, Keycode: Key.Escape })
        { if (!_overlay.Back()) CloseSettings(); GetViewport().SetInputAsHandled(); }
    }

    public override void _Notification(int what)
    {
        if (what == NotificationWMGoBackRequest && IsInsideTree())
        { if (SettingsOpen) { if (!_overlay.Back()) CloseSettings(); } else GetTree().Quit(); }
    }

    public override void _ExitTree()
    {
        GetTree().NodeAdded -= OnNodeAdded;
        GetTree().QuitOnGoBack = _previousQuitOnBack;
        foreach (var tween in _fades.Values) if (tween.IsValid()) tween.Kill();
        foreach (var sound in _sounds.Values) sound.Dispose();
    }
}

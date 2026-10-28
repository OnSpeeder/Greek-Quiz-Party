using Godot;

namespace QuizParty.Presentation;

/// <summary>Explicit fictional art benchmark, isolated from production match state.</summary>
public partial class LivingShowBenchmark : Control
{
    private RevealPerformance _performance = null!;
    private Label _answer = null!;
    private Label _joke = null!;
    private Label _eyebrow = null!;
    private Label _kicker = null!;
    private PanelContainer _answerCard = null!;
    private GridContainer _controls = null!;
    private AnswerShutter _shutter = null!;
    private bool _reduce;
    private bool _mute;
    private PresentationShell _shell = null!;
    private bool _lastReduced;
    private bool _lastSound;
    private float _lastVolume = -1;

    public override void _Ready()
    {
        var margin = new MarginContainer { Name = "Margin" }; AddChild(margin);
        margin.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var scroll = new ScrollContainer { HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled };
        margin.AddChild(scroll);
        var column = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill, SizeFlagsVertical = SizeFlags.ExpandFill };
        column.AddThemeConstantOverride("separation", 10); scroll.AddChild(column);
        _kicker = Text("SHOW_BENCHMARK", 14, ShowtimeTheme.Cyan); column.AddChild(_kicker);
        column.AddChild(Text("SHOW_TITLE", 32, ShowtimeTheme.Gold));
        _eyebrow = Text("SHOW_ANTICIPATION", 18, Colors.White); column.AddChild(_eyebrow);
        _answerCard = new PanelContainer { Name = "AnswerCard", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _answerCard.AddThemeStyleboxOverride("panel", QuizShowTheme.Card(new("211235"), ShowtimeTheme.Gold));
        column.AddChild(_answerCard);
        _answer = Text("SHOW_HIDDEN", 28, Colors.White); _answer.CustomMinimumSize = new(0, 52);
        _answer.VerticalAlignment = VerticalAlignment.Center; QuizShowTheme.StyleQuestion(_answer); _answerCard.AddChild(_answer);
        _shutter = new AnswerShutter { Name = "AnswerShutter", MouseFilter = MouseFilterEnum.Ignore };
        _answerCard.AddChild(_shutter);
        _performance = new RevealPerformance { Name = "Performance", SizeFlagsVertical = SizeFlags.ExpandFill, CustomMinimumSize = new(0, 220) };
        column.AddChild(_performance);
        _joke = Text("SHOW_CHALLENGE", 22, ShowtimeTheme.Gold); _joke.CustomMinimumSize = new(0, 66);
        _joke.VerticalAlignment = VerticalAlignment.Center; column.AddChild(_joke);
        var controls = new GridContainer { Name = "Controls", Columns = 2, SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _controls = controls;
        controls.AddThemeConstantOverride("h_separation", 12); controls.AddThemeConstantOverride("v_separation", 10); column.AddChild(controls);
        var replay = Button("SHOW_REPLAY"); replay.ThemeTypeVariation = "PrimaryAction"; controls.AddChild(replay);
        var home = Button("SHOW_HOME"); controls.AddChild(home);
        var reduce = Button("SHOW_REDUCE"); reduce.ToggleMode = true; controls.AddChild(reduce);
        var mute = Button("SHOW_MUTE"); mute.ToggleMode = true; controls.AddChild(mute);
        replay.Pressed += Replay;
        home.Pressed += () => GetTree().ChangeSceneToFile("res://Scenes/Main.tscn");
        reduce.Toggled += value => { _reduce = value; ApplyPreferences(); };
        mute.Toggled += value =>
        {
            _mute = value;
            _shell.Apply(_shell.Preferences with { Sound = !value }, persist: false);
            ApplyPreferences();
        };
        AddChild(new ResponsiveCanvas());
        _shell = GetNode<PresentationShell>("PresentationShell");
        _performance.BeatChanged += OnBeat;
        var args = MatchProcessProbe.LaunchArguments();
        _reduce = args.Contains("--match-show-reduced"); reduce.SetPressedNoSignal(_reduce);
        _mute = args.Contains("--match-show-muted"); mute.SetPressedNoSignal(_mute);
        Resized += Fit; Fit(); ApplyPreferences();
        Callable.From(Replay).CallDeferred();
        replay.GrabFocus();
        if (OS.IsDebugBuild()) StartCapture(args);
    }

    private void Fit()
    {
        if (_performance is null) return;
        var portrait = GetViewportRect().Size.X < GetViewportRect().Size.Y;
        _controls.Columns = portrait ? 2 : 4;
        _kicker.Visible = portrait || GetViewportRect().Size.Y >= 720;
        _eyebrow.Visible = portrait || GetViewportRect().Size.Y >= 720;
        _performance.CustomMinimumSize = new(0, portrait ? 230 : 210);
        var large = PresentationShell.For(this)?.Preferences.LargeText == true;
        _answer.AddThemeFontSizeOverride("font_size", large ? 32 : 28);
        _joke.AddThemeFontSizeOverride("font_size", large ? 25 : 22);
    }

    private static Label Text(string key, int size, Color color)
    {
        var label = new Label { Text = key, HorizontalAlignment = HorizontalAlignment.Center,
            AutowrapMode = TextServer.AutowrapMode.WordSmart, MouseFilter = MouseFilterEnum.Ignore };
        label.AddThemeFontSizeOverride("font_size", size); label.AddThemeColorOverride("font_color", color);
        label.AddThemeColorOverride("font_outline_color", new("120A2A")); label.AddThemeConstantOverride("outline_size", 4);
        return label;
    }

    private static Button Button(string key) => new() { Text = key, CustomMinimumSize = new(0, 64),
        SizeFlagsHorizontal = SizeFlags.ExpandFill, AutowrapMode = TextServer.AutowrapMode.WordSmart };

    private void OnBeat(bool answer, bool joke)
    {
        _answer.Text = answer ? "SHOW_ANSWER" : "SHOW_HIDDEN";
        _eyebrow.Text = answer ? "SHOW_REVEALED" : "SHOW_ANTICIPATION";
        _joke.Text = joke ? "SHOW_JOKE" : "SHOW_CHALLENGE";
        _answerCard.Modulate = answer ? Colors.White : new Color(.8f, .8f, .9f);
        _shutter.SetOpen(answer, _lastReduced);
        if (answer && !_lastReduced) _shell.Juice.PulseWinner(_answer);
    }

    private void Replay()
    {
        _shell.Juice.Finish(_answer); OnBeat(false, false); ApplyPreferences(); _performance.Replay();
    }

    private void ApplyPreferences()
    {
        var prefs = _shell.Preferences;
        _lastReduced = _reduce || prefs.ReducedMotion;
        _shell.Juice.SetReducedMotion(_lastReduced);
        _lastSound = !_mute && prefs.Sound; _lastVolume = prefs.Volume;
        _performance.Configure(_lastReduced, _lastSound, _lastVolume);
        if (_lastReduced) { _shell.Juice.Finish(_answer); _shutter.SetOpen(_performance.AnswerVisible, true); }
    }

    public override void _Process(double delta)
    {
        if (_shell is null) return;
        var prefs = _shell.Preferences;
        if (_lastReduced != (_reduce || prefs.ReducedMotion) || _shell.Juice.ReducedMotion != _lastReduced ||
            _lastSound != (!_mute && prefs.Sound) || _lastVolume != prefs.Volume)
            ApplyPreferences();
    }

    private async void StartCapture(string[] args)
    {
        var folder = args.FirstOrDefault(a => a.StartsWith("--match-show-capture=", StringComparison.Ordinal))?["--match-show-capture=".Length..];
        if (folder is null) return;
        try
        {
            DirAccess.MakeDirRecursiveAbsolute(folder);
            foreach (var (name, delay) in new[] { ("anticipation", .65), ("reveal", 1.05), ("joke", 1.5), ("settled", 2.5) })
            {
                await ToSignal(GetTree().CreateTimer(delay), global::Godot.Timer.SignalName.Timeout);
                if (!GodotObject.IsInstanceValid(this) || !IsInsideTree()) return;
                await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
                using var image = GetViewport().GetTexture().GetImage();
                var error = image.SavePng(folder + "/" + name + ".png");
                if (error != Error.Ok) throw new InvalidOperationException($"Capture failed: {error}");
                GD.Print($"SHOW CAPTURE {name} viewport={GetViewportRect().Size} answer={_performance.AnswerVisible} joke={_performance.JokeVisible}");
            }
            GetTree().Quit();
        }
        catch (Exception error) { GD.PushError(error.ToString()); GetTree().Quit(1); }
    }
}

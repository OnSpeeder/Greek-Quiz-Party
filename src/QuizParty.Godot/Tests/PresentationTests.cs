using GdUnit4;
using Godot;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class PresentationTests
{
    [TestCase]
    [RequireGodotRuntime]
    public void DisplayFontContainsGreekAccentsWithoutSystemFallback()
    {
        var font = GD.Load<FontFile>("res://Art/Fonts/Comfortaa-VariableFont_wght.ttf");
        foreach (var character in "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωάέήίόύώϊϋΐΰς")
            AssertThat(font.HasChar(character)).IsTrue();
        AssertThat(ShowtimeTheme.Create(new()).DefaultFont is FontVariation).IsTrue();
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task ReducedMotionFinishesPendingScoreAndEntranceButPreservesRevealCues()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = new Control(); tree.Root.AddChild(root);
        var juice = new ShowtimeJuice(); root.AddChild(juice);
        var answers = Enumerable.Range(0, 4).Select(_ => new Button { Size = new(160, 80) }).ToArray();
        foreach (var answer in answers) root.AddChild(answer);
        var score = new Label(); root.AddChild(score);
        try
        {
            juice.StaggerInControls(answers);
            AssertThat(answers[3].Scale.X).IsEqual(.85f);
            juice.TweenScoreLabel(score, 900, 100);
            juice.SetReducedMotion(true);
            AssertThat(score.Text).IsEqual(100L.ToString("N0"));
            AssertThat(answers.All(answer => answer.Scale == Vector2.One)).IsTrue();
            juice.Reveal(answers, 2);
            AssertThat(answers[2].Modulate.A).IsEqual(1f);
            AssertThat(answers[0].Modulate.A).IsEqual(.45f);
            await Frames(tree);
            AssertThat(answers[2].Scale).IsEqual(Vector2.One);
            juice.StaggerInControls(answers);
            AssertThat(answers.All(answer => answer.Modulate == Colors.White)).IsTrue();
            juice.SetReducedMotion(false);
            juice.TweenScoreLabel(score, 100, 1200);
            score.QueueFree();
            await Frames(tree); // Freed controls must cancel pending callbacks safely.
            juice.SetReducedMotion(true);
        }
        finally { root.Free(); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task LobbyUsesDiscoveryFirstJoinWithManualIpHiddenAndCreatePreserved()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>();
        tree.Root.AddChild(root);
        const string path = "Margin/Scroll/Content/";
        try
        {
            AssertThat(root.GetNode<Control>(path + "PartyChoice").Visible).IsTrue();
            AssertThat(root.GetNode<LineEdit>(path + "PlayerName").Visible).IsFalse();
            root.ShowSetupPage("create");
            var creation = root.GetNode<RoomCreationPanel>(path + "CreateRoom");
            AssertThat(((LineEdit)creation.FindChild("RoomName", true, false)).IsVisibleInTree()).IsTrue();
            AssertThat(((Button)creation.FindChild("Create", true, false)).IsVisibleInTree()).IsTrue();
            AssertThat(root.GetNode<RoomBrowser>(path + "JoinFlow/RoomBrowser").IsVisibleInTree()).IsFalse();
            AssertThat(((LineEdit)creation.FindChild("RoomPin", true, false)).IsVisibleInTree()).IsTrue();
            root.ShowSetupPage("join");
            AssertThat(root.GetNode<LineEdit>(path + "RoomName").Visible).IsFalse();
            AssertThat(root.GetNode<Button>(path + "Host").Visible).IsFalse();
            AssertThat(root.GetNode<RoomBrowser>(path + "JoinFlow/RoomBrowser").IsVisibleInTree()).IsTrue();
            AssertThat(root.GetNode<LineEdit>(path + "Address").Visible).IsFalse();
            AssertThat(root.GetNode<Button>(path + "ManualIp").Visible).IsFalse();
            AssertThat(root.GetNode<Button>(path + "Join").Visible).IsFalse();
            AssertThat(root.GetNode<LineEdit>(path + "PlayerName").Visible).IsFalse();
            AssertThat(root.GetNode<Button>(path + "JoinFlow/RoomBrowser/Header/Refresh").Text).IsEqual("");
            AssertThat(root.GetNode<PresentationShell>("PresentationShell").GetNode<Button>("Back").Text).IsEqual("");
        }
        finally { root.Free(); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public void DensePhoneTargetsRetain48DpAcrossOrientations()
    {
        var portrait = ResponsiveCanvas.PixelsPerUnit(new(1440, 3200), new(480, 1066.6666f));
        var landscape = ResponsiveCanvas.PixelsPerUnit(new(3200, 1440), new(1440, 648));
        AssertThat(Math.Abs(portrait - 3) < .01f).IsTrue();
        AssertThat(Math.Abs(landscape - 2.222222f) < .01f).IsTrue();
        AssertThat(ResponsiveCanvas.MinimumLogicalTarget(533, portrait)).IsEqual(64);
        AssertThat(ResponsiveCanvas.MinimumLogicalTarget(533, landscape)).IsEqual(72);
        foreach (var (dpi, scale) in new[] { (533f, 1440f / 648), (560f, 1440f / 648), (640f, 1440f / 648),
            (533f, 1440f / 480), (320f, 1080f / 648), (160f, 800f / 648) })
        {
            var minimum = ResponsiveCanvas.MinimumLogicalTarget(dpi, scale);
            AssertThat(minimum >= 64).IsTrue();
            AssertThat(minimum * scale * 160 / dpi >= 48).IsTrue();
        }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task SettingsKeyboardCycleStaysInsideModalAndBackRestoresFocus()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            shell.OpenSettings();
            var overlay = shell.GetNode<Control>("SettingsOverlay");
            for (var i = 0; i < 16; i++)
            {
                using var next = new InputEventKey { Keycode = Key.Tab, PhysicalKeycode = Key.Tab, Pressed = true };
                root.GetViewport().PushInput(next, true);
                using var release = new InputEventKey { Keycode = Key.Tab, PhysicalKeycode = Key.Tab };
                root.GetViewport().PushInput(release, true);
                await Frames(tree);
                var focus = root.GetViewport().GuiGetFocusOwner();
                AssertThat(focus is not null && overlay.IsAncestorOf(focus)).IsTrue();
            }
            shell.Notification((int)Node.NotificationWMGoBackRequest);
            AssertThat(shell.SettingsOpen).IsFalse();
            AssertThat(shell.GetNode<Button>("Settings").HasFocus()).IsTrue();
            shell.OpenSettings();
            using var escape = new InputEventKey { Keycode = Key.Escape, PhysicalKeycode = Key.Escape, Pressed = true };
            root.GetViewport().PushInput(escape, true);
            await Frames(tree);
            AssertThat(shell.SettingsOpen).IsFalse();
            AssertThat(shell.GetNode<Button>("Settings").HasFocus()).IsTrue();
        }
        finally { root.Free(); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public void PreferencesRoundTripAndRejectInvalidStoredTypes()
    {
        var path = $"user://presentation-test-{Guid.NewGuid():N}.cfg";
        try
        {
            var expected = new PresentationPreferences(false, .35f, true, true, true);
            AssertThat(expected.Save(path)).IsEqual(Error.Ok);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(expected);
            using var invalid = new ConfigFile();
            invalid.SetValue("ui", "volume", "loud");
            AssertThat(invalid.Save(path)).IsEqual(Error.Ok);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(new PresentationPreferences());
            invalid.SetValue("ui", "volume", 7.0);
            invalid.Save(path);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(new PresentationPreferences());
        }
        finally { DirAccess.RemoveAbsolute(ProjectSettings.GlobalizePath(path)); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task SettingsIsolateFocusPersistAndCancelActiveMotion()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        var shell = root.GetNode<PresentationShell>("PresentationShell");
        var path = $"user://presentation-ui-test-{Guid.NewGuid():N}.cfg";
        shell.SettingsPath = path;
        try
        {
            shell.OpenSettings();
            AssertThat(shell.SettingsOpen).IsTrue();
            AssertThat(root.GetNode<Control>("Center").Visible).IsFalse();
            var slider = (HSlider)shell.FindChild("Volume", true, false);
            AssertThat(slider.AccessibilityName.Length > 0).IsTrue();
            AssertThat(slider.CustomMinimumSize.Y >= 64).IsTrue();
            var label = root.GetNode<Label>("Center/Frame/Content/Title");
            shell.Apply(new(Sound: false));
            shell.Fade(label);
            AssertThat(label.Modulate.A < 1).IsTrue();
            shell.Apply(new(Sound: false, ReducedMotion: true, LargeText: true, HighContrast: true));
            AssertThat(label.Modulate.A).IsEqual(1f);
            AssertThat(root.Theme.DefaultFontSize).IsEqual(27);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(shell.Preferences);
            shell.PlayCue("final");
            AssertThat(shell.GetNode<AudioStreamPlayer>("FeedbackAudio").Playing).IsFalse();
            shell.CloseSettings();
            AssertThat(root.GetNode<Control>("Center").Visible).IsTrue();
            AssertThat(shell.GetNode<Button>("Settings").HasFocus()).IsTrue();
            shell.Fade(label);
            AssertThat(label.Modulate.A).IsEqual(1f);
        }
        finally
        {
            root.Free(); DirAccess.RemoveAbsolute(ProjectSettings.GlobalizePath(path));
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
        }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task AnswerGridAdaptsAndDynamicLongGreekButtonsStayTouchSized()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            var panel = root.GetNode<MatchPanel>("Margin/Scroll/Content/MatchPanel");
            panel.Visible = true;
            root.SetAnchorsAndOffsetsPreset(Control.LayoutPreset.TopLeft);
            // Exercise actual container layout at phone and TV widths, independent of headless window limits.
            root.Size = new(480, 800);
            await Frames(tree);
            AssertThat(panel.GetNode<GridContainer>("QuestionLayout/QuestionContent/Answers").Columns).IsEqual(1);
            var button = new Button { Text = "Μεγάλο ελληνικό κείμενο με τόνους και επεξήγηση για τη δοκιμή αναδίπλωσης" };
            root.GetNode<VBoxContainer>("Margin/Scroll/Content").AddChild(button);
            AssertThat(button.CustomMinimumSize.Y >= 64).IsTrue();
            AssertThat(button.AutowrapMode).IsEqual(TextServer.AutowrapMode.WordSmart);
            AssertThat(root.GetNode<ScrollContainer>("Margin/Scroll").FollowFocus).IsTrue();
            root.Size = new(1152, 648);
            await Frames(tree);
            AssertThat(panel.GetNode<GridContainer>("QuestionLayout/QuestionContent/Answers").Columns).IsEqual(2);
            AssertThat(shell.GetNode<Button>("Settings").CustomMinimumSize.Y >= 64).IsTrue();
            shell.Apply(new(LargeText: true), persist: false);
            AssertThat(panel.GetNode<Label>("QuestionLayout/QuestionContent/Question").GetThemeFontSize("font_size")).IsEqual(36);
            AssertThat(panel.GetNode<Button>("QuestionLayout/QuestionContent/Answers/Answer0").GetThemeFontSize("font_size")).IsEqual(31);
        }
        finally { root.Free(); await Frames(tree); }
    }

    private static async Task Frames(SceneTree tree)
    {
        for (var i = 0; i < 4; i++) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
    }
}

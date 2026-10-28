using GdUnit4;
using Godot;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class SettingsPageTests
{
    [TestCase]
    [RequireGodotRuntime]
    public void LegacyPreferencesMigrateLanguageAndInvalidLocalePreservesOtherValues()
    {
        var path = $"user://settings-migration-{Guid.NewGuid():N}.cfg";
        try
        {
            using var config = new ConfigFile();
            config.SetValue("ui", "sound", false); config.SetValue("ui", "volume", .25);
            config.Save(path);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(new PresentationPreferences(false, .25f));
            config.SetValue("ui", "language", 42); config.Save(path);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(new PresentationPreferences(false, .25f));
            var english = new PresentationPreferences(false, .25f, true, true, true, "en", false, "retro");
            AssertThat(english.Save(path)).IsEqual(Error.Ok);
            AssertThat(PresentationPreferences.Load(path)).IsEqual(english);
        }
        finally { DirAccess.RemoveAbsolute(ProjectSettings.GlobalizePath(path)); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task ResetRequiresConfirmationAndNestedBackNeverClosesTheParty()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        var shell = root.GetNode<PresentationShell>("PresentationShell");
        var path = $"user://settings-reset-{Guid.NewGuid():N}.cfg"; shell.SettingsPath = path;
        try
        {
            var original = new PresentationPreferences(false, .3f, true, true, true, "en");
            shell.Apply(original); shell.OpenSettings();
            var panel = shell.GetNode<SettingsPanel>("SettingsOverlay"); panel.SelectSection(2);
            var reset = (Button)panel.FindChild("Reset", true, false);
            reset.EmitSignal(Button.SignalName.Pressed);
            AssertThat(panel.DetailOpen).IsTrue();
            AssertThat(((Button)panel.FindChild("DetailBack", true, false)).HasFocus()).IsTrue();
            AssertThat(PresentationPreferences.Load(path)).IsEqual(original);
            shell.Notification((int)Node.NotificationWMGoBackRequest);
            AssertThat(shell.SettingsOpen).IsTrue(); AssertThat(panel.DetailOpen).IsFalse();
            AssertThat(reset.HasFocus()).IsTrue();
            reset.EmitSignal(Button.SignalName.Pressed);
            ((Button)panel.FindChild("ConfirmReset", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(shell.Preferences).IsEqual(new PresentationPreferences());
            AssertThat(PresentationPreferences.Load(path)).IsEqual(new PresentationPreferences());
            AssertThat(shell.SettingsOpen).IsTrue(); AssertThat(panel.DetailOpen).IsFalse();
            AssertThat(root.GetNode<Control>("Center").Visible).IsFalse();
        }
        finally { root.Free(); DirAccess.RemoveAbsolute(ProjectSettings.GlobalizePath(path)); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task LanguageReflowAndMutedPreviewPreserveSettingsAndFocus()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        var shell = root.GetNode<PresentationShell>("PresentationShell");
        var path = $"user://settings-layout-{Guid.NewGuid():N}.cfg"; shell.SettingsPath = path;
        try
        {
            root.SetAnchorsAndOffsetsPreset(Control.LayoutPreset.TopLeft); root.Size = new(1152, 648);
            shell.Apply(new PresentationPreferences()); shell.OpenSettings(); await Frames(tree);
            var panel = shell.GetNode<SettingsPanel>("SettingsOverlay");
            AssertThat(panel.LandscapeLayout).IsTrue();
            shell.SetLeaveAction(() => { });
            await Frames(tree);
            GD.Print($"SETTINGS BOUNDS frame={panel.GetNode<Control>("SafeMargin/Composition/Frame").GetGlobalRect()} panel={panel.GetGlobalRect()}");
            AssertThat(panel.GetNode<Control>("SafeMargin/Composition/Frame").GetGlobalRect().End.Y <= panel.GetGlobalRect().End.Y).IsTrue();
            var quickActions = (GridContainer)panel.FindChild("QuickActions", true, false);
            AssertThat(quickActions.Visible).IsTrue();
            AssertThat(((Button)panel.FindChild("Reset", true, false)).GetParent()).IsEqual(quickActions);
            var resetCount = panel.FindChildren("Reset", "Button", true, false).Count;
            AssertThat(resetCount).IsEqual(1);
            var resetAction = (Button)panel.FindChild("Reset", true, false);
            resetAction.GrabFocus(); root.Size = new(480, 800); await Frames(tree);
            AssertThat(resetAction.HasFocus()).IsTrue();
            root.Size = new(1152, 648); await Frames(tree);
            AssertThat(resetAction.HasFocus()).IsTrue();
            panel.SelectSection(1);
            var autoFit = (CheckButton)panel.FindChild("AutoFitQuestions", true, false);
            AssertThat(autoFit.ButtonPressed).IsTrue(); autoFit.ButtonPressed = false;
            AssertThat(PresentationPreferences.Load(path).AutoFitQuestions).IsFalse();
            var theme = (OptionButton)panel.FindChild("ThemeChoice", true, false);
            theme.EmitSignal(OptionButton.SignalName.ItemSelected, 2L);
            AssertThat(PresentationPreferences.Load(path).ThemeId).IsEqual("neon");
            AssertThat(root.GetNode<StageBackdrop>("StageBackdrop").ThemeId).IsEqual("neon");
            var language = (OptionButton)panel.FindChild("Language", true, false);
            language.GrabFocus(); language.EmitSignal(OptionButton.SignalName.ItemSelected, 1L);
            AssertThat(TranslationServer.GetLocale()).IsEqual("en");
            AssertThat(PresentationPreferences.Load(path).Language).IsEqual("en");
            AssertThat(language.HasFocus()).IsTrue();
            var toggle = (CheckButton)panel.FindChild("ReducedMotion", true, false);
            var soundToggle = (SettingsToggle)panel.FindChild("Sound", true, false);
            panel.SelectSection(0);
            soundToggle.ButtonPressed = false;
            AssertThat(soundToggle.Sliding).IsTrue();
            toggle.ButtonPressed = true;
            AssertThat(soundToggle.Sliding).IsFalse();
            AssertThat(((SettingsMascot)panel.FindChild("Mascot", true, false)).MotionActive).IsFalse();
            panel.SelectSection(1); language.GrabFocus();
            root.Size = new(480, 800); await Frames(tree);
            AssertThat(panel.LandscapeLayout).IsFalse(); AssertThat(language.HasFocus()).IsTrue();
            AssertThat(quickActions.Visible).IsFalse();
            AssertThat(((Button)panel.FindChild("Reset", true, false)).GetParent() == quickActions).IsFalse();
            AssertThat(panel.FindChildren("Reset", "Button", true, false).Count).IsEqual(1);
            // Portrait cards can be used without selecting their hidden landscape tab.
            panel.SelectSection(0); language.GrabFocus();
            root.Size = new(1152, 648); await Frames(tree);
            AssertThat(panel.ActiveSection).IsEqual(1); AssertThat(language.HasFocus()).IsTrue();
            root.Size = new(480, 800); await Frames(tree);
            AssertThat(panel.GetNode<Control>("SafeMargin/Composition/Frame").Size.X <= panel.Size.X).IsTrue();
            AssertThat(panel.GetNode<Control>("SafeMargin/Composition/Frame").Size.Y <= panel.Size.Y).IsTrue();
            var volume = (HSlider)panel.FindChild("Volume", true, false);
            volume.Value = 35; AssertThat(PresentationPreferences.Load(path).Volume).IsEqual(.35f);
            shell.Apply(shell.Preferences with { Sound = false });
            ((Button)panel.FindChild("Preview", true, false)).EmitSignal(Button.SignalName.Pressed);
            AssertThat(shell.GetNode<AudioStreamPlayer>("FeedbackAudio").Playing).IsFalse();
            shell.Apply(shell.Preferences with { HighContrast = true, LargeText = true }); await Frames(tree);
            AssertThat(((Control)panel.FindChild("MascotBay", true, false)).Visible).IsFalse();
            AssertThat(panel.GetNode<Control>("SafeMargin/Composition/Frame").Size.Y <= panel.Size.Y).IsTrue();
            AssertThat(volume.CustomMinimumSize.Y >= 64).IsTrue();
            panel.Render(shell.Preferences, 96); await Frames(tree);
            AssertThat(((Button)panel.FindChild("Close", true, false)).CustomMinimumSize.Y).IsEqual(96f);
            AssertThat(volume.CustomMinimumSize.Y).IsEqual(96f);
            root.Size = new(800, 480); await Frames(tree);
            AssertThat(panel.LandscapeLayout).IsFalse();
            AssertThat(panel.GetNode<Control>("SafeMargin/Composition/Frame").Size.Y <= panel.Size.Y).IsTrue();
            AssertThat(tree.Paused).IsFalse();
        }
        finally { root.Free(); DirAccess.RemoveAbsolute(ProjectSettings.GlobalizePath(path)); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task SaveFailureRemainsVisibleAndOfflineHelpHasARealReturnPath()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            shell.SettingsPath = $"user://missing-{Guid.NewGuid():N}/preferences.cfg";
            shell.OpenSettings(); shell.Apply(new PresentationPreferences(ReducedMotion: true));
            var panel = shell.GetNode<SettingsPanel>("SettingsOverlay");
            AssertThat(((Label)panel.FindChild("SaveStatus", true, false)).Text).IsEqual("UI_SAVE_FAILED");
            AssertThat(shell.Preferences.ReducedMotion).IsTrue();
            panel.SelectSection(2);
            foreach (var name in new[] { "Credits", "Privacy", "About" })
            {
                ((Button)panel.FindChild(name, true, false)).EmitSignal(Button.SignalName.Pressed);
                AssertThat(panel.DetailOpen).IsTrue();
                AssertThat(((Button)panel.FindChild("ConfirmReset", true, false)).Visible).IsFalse();
                shell.Notification((int)Node.NotificationWMGoBackRequest);
                AssertThat(panel.DetailOpen).IsFalse(); AssertThat(shell.SettingsOpen).IsTrue();
            }
        }
        finally { root.Free(); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task SettingsDragScrollsInPortraitAndLandscapeAndKeepsAccessibleIconNames()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = ResourceLoader.Load<PackedScene>("res://Scenes/Main.tscn").Instantiate<Control>();
        tree.Root.AddChild(root);
        try
        {
            root.SetAnchorsAndOffsetsPreset(Control.LayoutPreset.TopLeft);
            var shell = root.GetNode<PresentationShell>("PresentationShell");
            shell.Apply(new PresentationPreferences(ReducedMotion: true), persist: false);
            shell.OpenSettings();
            var panel = shell.GetNode<SettingsPanel>("SettingsOverlay");
            var scroll = (ScrollContainer)panel.FindChild("SectionsScroll", true, false);
            var drag = scroll.GetChildren().OfType<PageDragScroll>().Single();
            foreach (var size in new[] { new Vector2(480, 800), new Vector2(1152, 648) })
            {
                root.Size = size; panel.SelectSection(1); await Frames(tree);
                scroll.ScrollVertical = 0;
                var point = scroll.GetGlobalRect().GetCenter();
                using var down = new InputEventMouseButton { ButtonIndex = MouseButton.Left, Pressed = true, Position = point };
                using var move = new InputEventMouseMotion { Position = point - new Vector2(0, 180) };
                using var up = new InputEventMouseButton { ButtonIndex = MouseButton.Left, Pressed = false, Position = move.Position };
                drag._Input(down); drag._Input(move); drag._Input(up);
                AssertThat(scroll.ScrollVertical > 0).IsTrue();
            }
            var tab = (Button)panel.FindChild("Tab0", true, false);
            AssertThat(tab.Text).IsEqual(""); AssertThat(tab.AccessibilityName.Length > 0).IsTrue();
            AssertThat(((Button)panel.FindChild("Close", true, false)).Text).IsEqual("");
        }
        finally { root.Free(); await Frames(tree); }
    }

    [TestCase]
    [RequireGodotRuntime]
    public async Task MusicFollowsPhaseWithoutRestartAndHonorsMute()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = new Node(); tree.Root.AddChild(root);
        var music = new PartyMusic(); root.AddChild(music);
        try
        {
            AssertThat(PartyMusic.QuestionPhase(false, false, 8.1)).IsEqual("QuestionActive");
            AssertThat(PartyMusic.QuestionPhase(false, false, 8)).IsEqual("Urgent");
            AssertThat(PartyMusic.QuestionPhase(true, false, 0)).IsEqual("QuestionActive");
            AssertThat(PartyMusic.QuestionPhase(false, true, 2)).IsEqual("QuestionActive");
            music.SetPhase("Menu");
            AssertThat(music.CurrentTrack).IsEqual("menu");
            music.SetPhase("QuestionActive");
            AssertThat(music.CurrentTrack).IsEqual("question");
            var player = music.GetChildren().OfType<AudioStreamPlayer>().Single(p => p.Stream?.ResourcePath.EndsWith("question.wav", StringComparison.Ordinal) == true);
            music.SetPhase("QuestionLocked");
            AssertThat(player.Playing).IsTrue();
            music.SetPhase("Urgent"); AssertThat(music.CurrentTrack).IsEqual("tension");
            music.SetPhase("Scoreboard"); AssertThat(music.CurrentTrack).IsEqual("scoreboard");
            music.Configure(false, .65f);
            AssertThat(music.GetChildren().OfType<AudioStreamPlayer>().Any(p => p.Playing)).IsFalse();
            music.SetPhase("AnswerReveal");
            AssertThat(music.CurrentTrack).IsEqual("reveal");
            music.Configure(true, .65f);
            AssertThat(music.GetChildren().OfType<AudioStreamPlayer>().Any(p => p.Playing)).IsTrue();
            music.SetPhase("GameOver"); AssertThat(music.CurrentTrack).IsEqual("final");
        }
        finally { root.Free(); await Frames(tree); }
    }

    private static async Task Frames(SceneTree tree)
    {
        for (var i = 0; i < 5; i++) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
    }
}

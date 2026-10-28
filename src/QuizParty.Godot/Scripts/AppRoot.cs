using Godot;

namespace QuizParty.Presentation;

/// <summary>Localized front door; authoritative game rules belong in Core.</summary>
public partial class AppRoot : Control
{
    public override void _Ready()
    {
        AddChild(new ResponsiveCanvas());
        GetNode<Button>("Center/Frame/Content/LanSpike").Visible = false;
        var content = GetNode<VBoxContainer>("Center/Frame/Content");
        var crew = new TextureRect { Name = "StageCrew", Texture = GD.Load<Texture2D>("res://Art/showtime-crew-v2.png"),
            ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize, StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered,
            CustomMinimumSize = new(0, 150), MouseFilter = MouseFilterEnum.Ignore };
        content.AddChild(crew); content.MoveChild(crew, 1);
        GetNode<Label>("Center/Frame/Content/Status").Text = "UI_HOME_TAGLINE";
        GetNode<Button>("Center/Frame/Content/Lobby").Text = "UI_CREATE_PARTY";
        GetNode<Button>("Center/Frame/Content/Lobby").CustomMinimumSize = new(0, 80);
        GetNode<Button>("Center/Frame/Content/Lobby").ThemeTypeVariation = "PrimaryAction";
        var title = GetNode<Label>("Center/Frame/Content/Title");
        title.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
        title.AddThemeColorOverride("font_outline_color", new("180e38"));
        title.AddThemeConstantOverride("outline_size", 10);
        title.AddThemeColorOverride("font_shadow_color", new("4c236b"));
        title.AddThemeConstantOverride("shadow_offset_y", 5);
        title.AddThemeFontOverride("font", QuizShowTheme.DisplayFont());
        title.AutowrapMode = TextServer.AutowrapMode.Off;
        Resized += FitTitle;
        FitTitle();
        var join = new Button { Name = "JoinParty", Text = "UI_JOIN_PARTY", CustomMinimumSize = new(0, 72) };
        content.AddChild(join); join.Pressed += () => OpenLobby("join");
        // Explicit preview entry while the character-performance benchmark awaits review.
        if (OS.IsDebugBuild())
        {
            if (MatchProcessProbe.LaunchArguments().Contains("--match-show-preview") && !GetTree().HasMeta("living_show_launch_consumed"))
            {
                GetTree().SetMeta("living_show_launch_consumed", true);
                Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/LivingShowBenchmark.tscn")).CallDeferred();
            }
        }
        PresentationShell.For(this)?.Fade(GetNode<Label>("Center/Frame/Content/Title"));
        if (OS.IsDebugBuild() && MatchProcessProbe.LaunchArguments().Any(a =>
            a == "--match-flow-host" || a == "--match-flow-client" || a == "--match-ui-create" || a == "--match-ui-create-identity" || a.StartsWith("--match-ui-lobby-page=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        if (OS.IsDebugBuild() && MatchProcessProbe.LaunchArguments().Any(a => a.StartsWith("--lan-", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        if (MatchProcessProbe.LaunchArguments().Any(argument => argument == "--match-host" ||
            argument.StartsWith("--match-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        GD.Print("QuizParty: C# startup ready.");
        GetNode<Button>("Center/Frame/Content/LanSpike").Pressed += () =>
            GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn");
        GetNode<Button>("Center/Frame/Content/Lobby").Pressed += () => OpenLobby("create");
        if (OS.GetCmdlineUserArgs().Any(argument => argument == "--lobby-host" ||
            argument.StartsWith("--lobby-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        // Official export templates disallow command-line scene overrides. Route
        // explicit probe launch flags through the normal application entry scene.
        if (OS.GetCmdlineUserArgs().Any(argument => argument == "--spike-host" ||
            argument.StartsWith("--spike-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn")).CallDeferred();
    }

    public void FitTitle()
    {
        if (GetNodeOrNull<Label>("Center/Frame/Content/Title") is not { } title) return;
        var width = Math.Min(560, Math.Max(200, GetViewportRect().Size.X - 72));
        var measured = title.GetThemeFont("font").GetStringSize("QuizParty", fontSize: 72).X;
        title.AddThemeFontSizeOverride("font_size", Math.Clamp((int)(72 * (width - 20) / Math.Max(1, measured)), 32, 72));
        if (GetNodeOrNull<TextureRect>("Center/Frame/Content/StageCrew") is { } crew)
            crew.CustomMinimumSize = new(0, GetViewportRect().Size.X < GetViewportRect().Size.Y ? 148 : 118);
    }

    private void OpenLobby(string page)
    {
        var tree = GetTree();
        void Arrived()
        {
            tree.SceneChanged -= Arrived;
            (tree.CurrentScene as LobbyScreen)?.ShowSetupPage(page);
        }
        tree.SceneChanged += Arrived;
        var error = tree.ChangeSceneToFile("res://Scenes/Lobby.tscn");
        if (error != Error.Ok) { tree.SceneChanged -= Arrived; GD.PushError($"Lobby navigation failed: {error}"); }
    }
}

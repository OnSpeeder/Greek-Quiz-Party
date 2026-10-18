using Godot;

namespace QuizParty.Presentation;

/// <summary>Minimal startup probe; authoritative game rules belong in Core.</summary>
public partial class AppRoot : Control
{
    public override void _Ready()
    {
        AddChild(new ResponsiveCanvas());
        if (OS.IsDebugBuild() && MatchProcessProbe.LaunchArguments().Any(a => a.StartsWith("--lan-", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        if (MatchProcessProbe.LaunchArguments().Any(argument => argument == "--match-host" ||
            argument.StartsWith("--match-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        GD.Print("QuizParty: C# startup ready.");
        GetNode<Button>("Center/Content/LanSpike").Pressed += () =>
            GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn");
        GetNode<Button>("Center/Content/Lobby").Pressed += () =>
            GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn");
        if (OS.GetCmdlineUserArgs().Any(argument => argument == "--lobby-host" ||
            argument.StartsWith("--lobby-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/Lobby.tscn")).CallDeferred();
        // Official export templates disallow command-line scene overrides. Route
        // explicit probe launch flags through the normal application entry scene.
        if (OS.GetCmdlineUserArgs().Any(argument => argument == "--spike-host" ||
            argument.StartsWith("--spike-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn")).CallDeferred();
    }
}

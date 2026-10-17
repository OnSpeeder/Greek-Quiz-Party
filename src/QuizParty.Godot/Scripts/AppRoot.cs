using Godot;

namespace QuizParty.Presentation;

/// <summary>Minimal startup probe; authoritative game rules belong in Core.</summary>
public partial class AppRoot : Control
{
    public override void _Ready()
    {
        GD.Print("QuizParty: C# startup ready.");
        GetNode<Button>("Center/Content/LanSpike").Pressed += () =>
            GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn");
        // Official export templates disallow command-line scene overrides. Route
        // explicit probe launch flags through the normal application entry scene.
        if (OS.GetCmdlineUserArgs().Any(argument => argument == "--spike-host" ||
            argument.StartsWith("--spike-join=", StringComparison.Ordinal)))
            Callable.From(() => GetTree().ChangeSceneToFile("res://Scenes/LanSpike.tscn")).CallDeferred();
    }
}

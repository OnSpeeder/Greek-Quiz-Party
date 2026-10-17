using Godot;

namespace QuizParty.Presentation;

/// <summary>Minimal startup probe; authoritative game rules belong in Core.</summary>
public partial class AppRoot : Control
{
    public override void _Ready()
    {
        GD.Print("QuizParty: C# startup ready.");
    }
}

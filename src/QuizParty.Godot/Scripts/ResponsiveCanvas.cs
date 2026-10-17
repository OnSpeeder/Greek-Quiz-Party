using Godot;

namespace QuizParty.Presentation;

/// <summary>Choose a logical canvas for orientation; Containers handle the actual layout.</summary>
public partial class ResponsiveCanvas : Node
{
    private Window _window = null!;
    public override void _Ready()
    {
        _window = GetWindow();
        _window.SizeChanged += UpdateScale;
        UpdateScale();
    }

    private void UpdateScale() => _window.ContentScaleSize = _window.Size.X < _window.Size.Y
        ? new Vector2I(480, 800)
        : new Vector2I(1152, 648);

    public override void _ExitTree() => _window.SizeChanged -= UpdateScale;
}

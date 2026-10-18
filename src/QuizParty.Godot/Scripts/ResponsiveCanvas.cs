using Godot;

namespace QuizParty.Presentation;

/// <summary>Choose a logical canvas for orientation; Containers handle the actual layout.</summary>
public partial class ResponsiveCanvas : Node
{
    private Window _window = null!;
    private Control _root = null!;
    public static int MinimumLogicalTarget(float dpi, float pixelsPerUnit)
    {
        if (!float.IsFinite(dpi) || dpi <= 0) dpi = 160;
        if (!float.IsFinite(pixelsPerUnit) || pixelsPerUnit <= 0) pixelsPerUnit = 1;
        return Math.Max(64, (int)Math.Ceiling(48 * (double)dpi / 160 / pixelsPerUnit));
    }
    public static float PixelsPerUnit(Vector2I window, Vector2 viewport) =>
        Math.Min(window.X / Math.Max(1, viewport.X), window.Y / Math.Max(1, viewport.Y));
    public override void _Ready()
    {
        _window = GetWindow();
        _root = (Control)GetParent();
        _root.AddChild(new PresentationShell { Name = "PresentationShell" });
        _window.SizeChanged += UpdateScale;
        _root.Resized += UpdateMargins;
        UpdateScale();
    }

    private void UpdateScale()
    {
        var portrait = _window.Size.X < _window.Size.Y;
        _window.ContentScaleSize = portrait ? new Vector2I(480, 800) : new Vector2I(1152, 648);
        UpdateMargins();
    }

    private void UpdateMargins()
    {
        var portrait = _window.Size.X < _window.Size.Y;
        // Keep the scene in a readable column on wide TV displays; preserve vertical scrolling.
        var logicalWidth = _root.GetViewportRect().Size.X;
        var side = portrait ? 20 : Math.Max(32, (int)(logicalWidth - 1088) / 2);
        var inset = Vector4.Zero;
        if (OS.HasFeature("android"))
        {
            var safe = DisplayServer.GetDisplaySafeArea();
            var screen = DisplayServer.ScreenGetSize();
            var scale = _root.GetViewportRect().Size / (Vector2)screen;
            inset = new(safe.Position.X * scale.X, safe.Position.Y * scale.Y,
                Math.Max(0, screen.X - safe.End.X) * scale.X, Math.Max(0, screen.Y - safe.End.Y) * scale.Y);
        }
        var shell = _root.GetNodeOrNull<PresentationShell>("PresentationShell");
        shell?.UpdateInsets(inset);
        var header = Math.Max(92, (int)(shell?.MinimumTarget ?? 64) + 28);
        if (_root.GetNodeOrNull<MarginContainer>("Margin") is { } margin)
        {
            margin.AddThemeConstantOverride("margin_left", side + (int)inset.X);
            margin.AddThemeConstantOverride("margin_right", side + (int)inset.Z);
            margin.AddThemeConstantOverride("margin_top", header + (int)inset.Y);
            margin.AddThemeConstantOverride("margin_bottom", 24 + (int)inset.W);
        }
        if (_root.GetNodeOrNull<Control>("Center") is { } center)
        {
            center.OffsetLeft = 24 + inset.X; center.OffsetRight = -24 - inset.Z;
            center.OffsetTop = header + inset.Y; center.OffsetBottom = -24 - inset.W;
        }
        if (_root.GetNodeOrNull<VBoxContainer>("Center/Frame/Content") is { } menu)
            menu.CustomMinimumSize = new(Math.Min(560, Math.Max(0, logicalWidth - 64)), 0);
    }

    public override void _ExitTree()
    {
        _window.SizeChanged -= UpdateScale;
        _root.Resized -= UpdateMargins;
    }
}

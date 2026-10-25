using Godot;

namespace QuizParty.Presentation;

/// <summary>Scene-owned modal with a bounded reading area and fixed actions.</summary>
public partial class MatchDialog : Control
{
    public VBoxContainer Body { get; private set; } = null!;
    public GridContainer Actions { get; private set; } = null!;
    public override void _Ready()
    {
        SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        MouseFilter = MouseFilterEnum.Stop;
        var shade = new ColorRect { Color = new(0.025f, 0.015f, 0.08f, .9f) };
        AddChild(shade); shade.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var margin = new MarginContainer(); AddChild(margin);
        margin.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        foreach (var edge in new[] { "left", "right", "top", "bottom" }) margin.AddThemeConstantOverride("margin_" + edge, 24);
        var panel = new PanelContainer { SizeFlagsHorizontal = SizeFlags.ShrinkCenter, SizeFlagsVertical = SizeFlags.ShrinkCenter }; margin.AddChild(panel);
        void Fit()
        {
            var view = GetViewportRect().Size;
            panel.CustomMinimumSize = new(Math.Min(900, Math.Max(0, view.X - 48)), Math.Min(480, Math.Max(0, view.Y - 48)));
            if (Visible) Theme = PresentationShell.For(this)?.GetParent<Control>().Theme ?? ShowtimeTheme.Create(new());
        }
        Resized += Fit; VisibilityChanged += Fit; Fit();
        panel.AddThemeStyleboxOverride("panel", QuizShowTheme.Card(QuizShowTheme.Navy, ShowtimeTheme.Gold));
        var layout = new VBoxContainer(); panel.AddChild(layout);
        var scroll = new ScrollContainer { SizeFlagsVertical = SizeFlags.ExpandFill, HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled };
        layout.AddChild(scroll); scroll.AddChild(new PageDragScroll());
        Body = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; scroll.AddChild(Body);
        Actions = new GridContainer(); layout.AddChild(Actions);
        Hide();
    }
    public void Clear()
    {
        foreach (var container in new Container[] { Body, Actions })
            foreach (var child in container.GetChildren()) { container.RemoveChild(child); child.QueueFree(); }
    }
}

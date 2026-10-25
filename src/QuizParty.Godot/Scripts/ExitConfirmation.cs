using Godot;

namespace QuizParty.Presentation;

/// <summary>Localized, responsive confirmation; the owner decides when to quit.</summary>
public partial class ExitConfirmation : Control
{
    public event Action? Confirmed;
    public event Action? Cancelled;
    private PanelContainer _card = null!;
    private Button _no = null!;
    public override void _Ready()
    {
        SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var dim = new ColorRect { Color = new(0, 0, 0, .72f), MouseFilter = MouseFilterEnum.Stop };
        AddChild(dim); dim.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        var center = new CenterContainer(); AddChild(center);
        center.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        _card = new PanelContainer { Name = "Card" }; center.AddChild(_card);
        var column = new VBoxContainer(); _card.AddChild(column);
        var message = new Label { Text = "UI_EXIT_QUESTION", HorizontalAlignment = HorizontalAlignment.Center,
            AutowrapMode = TextServer.AutowrapMode.WordSmart };
        column.AddChild(message);
        var actions = new HBoxContainer(); column.AddChild(actions);
        _no = new Button { Name = "No", Text = "UI_NO", SizeFlagsHorizontal = SizeFlags.ExpandFill,
            CustomMinimumSize = new(64, 64), ThemeTypeVariation = "PrimaryAction" };
        var yes = new Button { Name = "Yes", Text = "UI_YES", SizeFlagsHorizontal = SizeFlags.ExpandFill,
            CustomMinimumSize = new(64, 64) };
        actions.AddChild(_no); actions.AddChild(yes);
        _no.Pressed += () => Cancelled?.Invoke();
        yes.Pressed += () => Confirmed?.Invoke();
        _no.FocusNext = _no.FocusPrevious = _no.GetPathTo(yes);
        yes.FocusNext = yes.FocusPrevious = yes.GetPathTo(_no);
        Resized += Reflow; Reflow();
    }
    private void Reflow() => _card.CustomMinimumSize = new(Math.Min(520, Math.Max(0, Size.X - 48)), 0);
    public void Open() { Show(); _no.GrabFocus(); }
}

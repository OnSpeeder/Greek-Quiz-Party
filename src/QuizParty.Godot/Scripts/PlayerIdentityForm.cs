using Godot;

namespace QuizParty.Presentation;

/// <summary>Shared name/character step. Only the character list may overflow.</summary>
public partial class PlayerIdentityForm : VBoxContainer
{
    public LineEdit NameInput { get; private set; } = null!;
    public CharacterPicker Characters { get; private set; } = null!;
    public ScrollContainer CharacterScroll { get; private set; } = null!;
    public override void _Ready()
    {
        SizeFlagsHorizontal = SizeFlags.ExpandFill;
        AddChild(new Label { Text = "UI_NAME_LABEL" });
        NameInput = new LineEdit { Name = "PlayerName", PlaceholderText = "LOBBY_PLAYER_NAME", MaxLength = 32,
            CustomMinimumSize = new(0, 64) }; AddChild(NameInput);
        AddChild(new Label { Text = "JOIN_CHARACTER" });
        CharacterScroll = new ScrollContainer { Name = "CharacterScroll", HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled,
            VerticalScrollMode = ScrollContainer.ScrollMode.ShowNever, FollowFocus = true };
        AddChild(CharacterScroll); CharacterScroll.AddChild(new PageDragScroll());
        Characters = new CharacterPicker { Name = "Characters", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        CharacterScroll.AddChild(Characters);
        var fit = new global::Godot.Timer { WaitTime = .1, Autostart = true }; AddChild(fit); fit.Timeout += Fit;
        Resized += Fit; VisibilityChanged += Fit;
    }
    private void Fit()
    {
        if (!IsVisibleInTree() || CharacterScroll is null) return;
        var siblings = GetChildren().OfType<Control>().Where(c => c.Visible && c != CharacterScroll).ToArray();
        var other = siblings.Sum(c => c.GetCombinedMinimumSize().Y) + siblings.Length * GetThemeConstant("separation");
        var scale = ResponsiveCanvas.PixelsPerUnit(GetWindow().Size, GetViewportRect().Size);
        var keyboard = OS.HasFeature("android") ? DisplayServer.VirtualKeyboardGetHeight() / Math.Max(.01f, scale) : 0;
        var bottom = GetViewportRect().Size.Y - 24 - keyboard;
        for (Node? parent = GetParent(); parent is not null; parent = parent.GetParent())
            if (parent is ScrollContainer outer) { bottom = Math.Min(bottom, outer.GetGlobalRect().End.Y); break; }
        var available = bottom - Math.Max(92, GlobalPosition.Y) - other;
        var height = Math.Max(64, Math.Min(Characters.GetCombinedMinimumSize().Y, available));
        CharacterScroll.CustomMinimumSize = new(0, height);
    }
}

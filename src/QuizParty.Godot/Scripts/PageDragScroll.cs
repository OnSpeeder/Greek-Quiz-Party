using Godot;

namespace QuizParty.Presentation;

/// <summary>Thresholded page dragging, including gestures beginning over a button.</summary>
public partial class PageDragScroll : Node
{
    private ScrollContainer _scroll = null!;
    private Vector2? _origin;
    private int _initial;
    private bool _dragging;
    private int _touch = -1;
    public override void _Ready() => _scroll = (ScrollContainer)GetParent();

    public override void _Input(InputEvent input)
    {
        if (!_scroll.IsVisibleInTree() || GetTree().GetNodesInGroup("match_modal").OfType<Control>()
            .Any(modal => modal.IsVisibleInTree() && !modal.IsAncestorOf(_scroll))) { Reset(); return; }
        if (input is InputEventScreenTouch touch)
        {
            if (touch.Pressed && _touch < 0 && Begin(touch.Position)) _touch = touch.Index;
            else if (!touch.Pressed && touch.Index == _touch) { End(); _touch = -1; }
        }
        else if (input is InputEventScreenDrag drag && drag.Index == _touch) Move(drag.Position);
        else if (_touch < 0 && input is InputEventMouseButton { ButtonIndex: MouseButton.Left } mouse)
        {
            if (mouse.Pressed) Begin(mouse.Position); else End();
        }
        else if (_touch < 0 && input is InputEventMouseMotion motion && _origin is not null) Move(motion.Position);
    }
    private bool Begin(Vector2 position)
    {
        if (!_scroll.GetGlobalRect().HasPoint(position) || _scroll.GetVScrollBar().MaxValue <= _scroll.Size.Y) return false;
        _origin = position; _initial = _scroll.ScrollVertical; _dragging = false;
        return true;
    }
    private void Move(Vector2 position)
    {
        if (_origin is not { } origin) return;
        if (!_dragging && (Math.Abs(position.Y - origin.Y) < 12 ||
            Math.Abs(position.Y - origin.Y) <= Math.Abs(position.X - origin.X))) return;
        _dragging = true;
        _scroll.ScrollVertical = _initial + (int)(origin.Y - position.Y);
        GetViewport().SetInputAsHandled();
    }
    private void End()
    {
        if (_dragging)
        {
            foreach (var button in _scroll.FindChildren("*", "BaseButton", true, false).OfType<BaseButton>())
                if (!button.ToggleMode) button.SetPressedNoSignal(false);
            GetViewport().SetInputAsHandled();
        }
        Reset();
    }
    private void Reset() { _origin = null; _dragging = false; _touch = -1; }
}

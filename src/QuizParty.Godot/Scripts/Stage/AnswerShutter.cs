using Godot;

namespace QuizParty.Presentation;

/// <summary>Decorative two-leaf answer prop. Native lettering remains beneath it.</summary>
public partial class AnswerShutter : Control
{
    private Tween? _tween;
    private float _opening;
    private bool _open;
    private Font _font = null!;

    public override void _Ready() { _font = QuizShowTheme.DisplayFont(); }

    public void SetOpen(bool open, bool immediate)
    {
        if (open == _open && !immediate) return;
        _open = open;
        if (_tween?.IsValid() == true) _tween.Kill();
        if (!open || immediate) { _opening = open ? 1 : 0; QueueRedraw(); return; }
        _tween = CreateTween();
        _tween.TweenMethod(Callable.From<float>(value => { _opening = value; QueueRedraw(); }),
            _opening, 1f, .32).SetTrans(Tween.TransitionType.Cubic).SetEase(Tween.EaseType.Out);
    }

    public override void _Draw()
    {
        var width = Size.X / 2 * (1 - _opening);
        if (width < .1f) return;
        var box = QuizShowTheme.Card(new("352254"), ShowtimeTheme.Gold);
        DrawStyleBox(box, new Rect2(0, 0, width, Size.Y));
        DrawStyleBox(box, new Rect2(Size.X - width, 0, width, Size.Y));
        if (_opening < .05f)
        {
            var text = "?";
            var size = _font.GetStringSize(text, fontSize: 38);
            DrawCircle(Size / 2, 31, new("211235"));
            DrawArc(Size / 2, 31, 0, Mathf.Tau, 64, ShowtimeTheme.Gold, 3, true);
            DrawString(_font, Size / 2 + new Vector2(-size.X / 2, 13), text, fontSize: 38, modulate: ShowtimeTheme.Gold);
        }
        box.Dispose();
    }

    public override void _ExitTree() { if (_tween?.IsValid() == true) _tween.Kill(); }
}

using Godot;

namespace QuizParty.Presentation;

/// <summary>Scene-owned cosmetic motion. Cancelling always restores the final readable state.</summary>
public partial class ShowtimeJuice : Node
{
    private readonly Dictionary<Control, (Tween Tween, Action Finish)> _active = [];
    public bool ReducedMotion { get; private set; }

    public void SetReducedMotion(bool reduced)
    {
        ReducedMotion = reduced;
        if (reduced) foreach (var control in _active.Keys.ToArray()) Finish(control);
    }

    public void Finish(Control control)
    {
        if (!_active.Remove(control, out var animation)) return;
        if (animation.Tween.IsValid()) animation.Tween.Kill();
        if (GodotObject.IsInstanceValid(control)) animation.Finish();
    }

    private Tween? Begin(Control control, Action final)
    {
        Finish(control);
        if (ReducedMotion || !control.IsInsideTree()) { final(); return null; }
        control.PivotOffset = control.Size / 2f;
        var tween = control.CreateTween().SetTrans(Tween.TransitionType.Cubic).SetEase(Tween.EaseType.Out);
        _active[control] = (tween, final);
        tween.Finished += () => { _active.Remove(control); final(); };
        if (!control.HasMeta("showtime_cleanup"))
        {
            control.SetMeta("showtime_cleanup", true);
            control.TreeExiting += () => Finish(control);
            control.Resized += () => control.PivotOffset = control.Size / 2f;
        }
        return tween;
    }

    public void StaggerInControls(IReadOnlyList<Button> controls)
    {
        for (var index = 0; index < controls.Count; index++)
        {
            var control = controls[index];
            control.Modulate = Colors.White;
            var tween = Begin(control, () => control.Scale = Vector2.One);
            if (tween is null) continue;
            control.Scale = Vector2.One * .85f;
            tween.TweenProperty(control, "scale", Vector2.One, .28).SetDelay(index * .06)
                .SetTrans(Tween.TransitionType.Back).SetEase(Tween.EaseType.Out);
        }
    }

    public void AttachTactileButtonFeedback(Button button)
    {
        void Bounce(float scale, bool settle)
        {
            if (button.Disabled) return;
            var tween = Begin(button, () => button.Scale = Vector2.One);
            if (tween is null) return;
            tween.TweenProperty(button, "scale", Vector2.One * scale, .10);
            if (settle) tween.TweenProperty(button, "scale", Vector2.One, .18).SetTrans(Tween.TransitionType.Back);
        }
        button.ButtonDown += () => Bounce(.95f, false);
        button.ButtonUp += () => Bounce(1.04f, true);
        button.MouseEntered += () => Bounce(1.04f, true);
        button.MouseExited += () => Finish(button);
        button.FocusExited += () => Finish(button);
    }

    public void PulseWinner(Control control)
    {
        var tween = Begin(control, () => control.Scale = Vector2.One);
        if (tween is null) return;
        tween.TweenProperty(control, "scale", Vector2.One * 1.08f, .18);
        tween.TweenProperty(control, "scale", Vector2.One, .22).SetTrans(Tween.TransitionType.Back);
    }

    public void Reveal(IReadOnlyList<Button> answers, int correct)
    {
        for (var i = 0; i < answers.Count; i++)
        {
            Finish(answers[i]);
            answers[i].Scale = Vector2.One;
            answers[i].Modulate = new(1, 1, 1, i == correct ? 1 : .45f);
        }
        PulseWinner(answers[correct]);
    }

    public void TweenScoreLabel(Label label, long from, long to)
    {
        var tween = Begin(label, () => label.Text = to.ToString("N0"));
        if (tween is null) return;
        label.Text = from.ToString("N0");
        // Interpolation is presentation only, never used as an authoritative score.
        tween.TweenMethod(Callable.From<double>(value => label.Text = ((long)Math.Round(value)).ToString("N0")),
            (double)from, (double)to, .6);
    }

    public override void _ExitTree()
    { foreach (var control in _active.Keys.ToArray()) Finish(control); }
}

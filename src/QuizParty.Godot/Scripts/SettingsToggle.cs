using Godot;

namespace QuizParty.Presentation;

/// <summary>Native accessible CheckButton with a decorative sliding thumb.</summary>
public partial class SettingsToggle : CheckButton
{
    private Control _visual = null!;
    private TextureRect _track = null!;
    private TextureRect _thumb = null!;
    private Texture2D _space = null!;
    private Texture2D _on = null!;
    private Texture2D _off = null!;
    private Tween? _slide;
    private bool? _lastState;
    public bool Sliding => _slide?.IsRunning() == true;

    public override void _Ready()
    {
        _space = SettingsSkin.Texture("switch-space");
        _on = SettingsSkin.Texture("switch-track-on");
        _off = SettingsSkin.Texture("switch-track-off");
        _visual = new Control { MouseFilter = MouseFilterEnum.Ignore };
        AddChild(_visual);
        _visual.SetAnchorsAndOffsetsPreset(LayoutPreset.CenterRight);
        _visual.OffsetLeft = -136; _visual.OffsetRight = -16; _visual.OffsetTop = -28; _visual.OffsetBottom = 28;
        _track = new TextureRect { MouseFilter = MouseFilterEnum.Ignore };
        _visual.AddChild(_track); _track.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        _thumb = new TextureRect { Texture = SettingsSkin.Texture("slider-thumb-idle"),
            MouseFilter = MouseFilterEnum.Ignore, Size = new(48, 48), Position = new(4, 4) };
        _visual.AddChild(_thumb);
        VisibilityChanged += () =>
        {
            if (IsVisibleInTree()) return;
            StopSlide(); _thumb.Position = new(ButtonPressed ? 68 : 4, 4);
        };
    }

    public void Sync(bool quiet, bool contrast)
    {
        _visual.Visible = !contrast;
        foreach (var state in new[] { "checked", "unchecked", "checked_disabled", "unchecked_disabled" })
        {
            if (contrast) RemoveThemeIconOverride(state);
            else AddThemeIconOverride(state, _space);
        }
        _track.Texture = ButtonPressed ? _on : _off;
        var target = new Vector2(ButtonPressed ? 68 : 4, 4);
        if (quiet || contrast || _lastState is null || !IsVisibleInTree())
        { StopSlide(); _thumb.Position = target; }
        else if (_lastState != ButtonPressed)
        {
            StopSlide(); _slide = CreateTween();
            _slide.TweenProperty(_thumb, "position", target, .16).SetTrans(Tween.TransitionType.Back).SetEase(Tween.EaseType.Out);
        }
        _lastState = ButtonPressed;
    }

    private void StopSlide()
    {
        if (_slide?.IsValid() == true) _slide.Kill();
        _slide = null;
    }

    public override void _ExitTree() => StopSlide();
}

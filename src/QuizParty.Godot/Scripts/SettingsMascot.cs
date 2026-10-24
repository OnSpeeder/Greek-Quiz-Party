using Godot;

namespace QuizParty.Presentation;

/// <summary>Decorative atlas poses and cancellable motion; never consumes input.</summary>
public partial class SettingsMascot : TextureRect
{
    private Texture2D _atlas = null!;
    private global::Godot.Timer _timer = null!;
    private Tween? _breathing;
    private bool _orange;
    private bool _quiet;
    private bool _configured;
    private AtlasTexture _poseTexture = null!;
    private int _phase;
    public int Pose { get; private set; }
    public bool MotionActive => _breathing?.IsRunning() == true;

    public override void _EnterTree()
    {
        _poseTexture = new AtlasTexture(); Texture = _poseTexture;
    }

    public override void _Ready()
    {
        MouseFilter = MouseFilterEnum.Ignore;
        ExpandMode = ExpandModeEnum.IgnoreSize;
        StretchMode = StretchModeEnum.KeepAspectCentered;
        _timer = new global::Godot.Timer { OneShot = true };
        AddChild(_timer);
        _timer.Timeout += OnTick;
        VisibilityChanged += Refresh;
        Resized += () => PivotOffset = Size / 2;
        Configure(false, true);
    }

    public void Configure(bool orange, bool quiet)
    {
        if (_configured && _orange == orange && _quiet == quiet) return;
        _configured = true;
        _orange = orange; _quiet = quiet;
        _atlas = GD.Load<Texture2D>($"res://Art/Settings/mascot-{(orange ? "orange" : "blue")}.png");
        Refresh();
    }

    private void Refresh()
    {
        StopMotion(); SetPose(0); _phase = 0;
        if (_quiet || !IsVisibleInTree() || !_timer.IsInsideTree()) return;
        _breathing = CreateTween().SetLoops();
        _breathing.TweenProperty(this, "scale", new Vector2(1.015f, 1.025f), 1.4).SetTrans(Tween.TransitionType.Sine);
        _breathing.TweenProperty(this, "scale", Vector2.One, 1.4).SetTrans(Tween.TransitionType.Sine);
        _timer.Start(2.8);
    }

    public void React(bool muted)
    {
        if (_quiet || !IsVisibleInTree()) return;
        SetPose(muted ? 2 : 3);
        _phase = 2; _timer.Start(.75);
    }

    public void Wave()
    {
        if (!_orange || _quiet || !IsVisibleInTree()) return;
        SetPose(2); _phase = 2; _timer.Start(.9);
    }

    private void OnTick()
    {
        if (_quiet || !IsVisibleInTree()) return;
        if (_phase == 0) { SetPose(1); _phase = 1; _timer.Start(.14); }
        else { SetPose(0); _phase = 0; _timer.Start(3.2); }
    }

    private void SetPose(int pose)
    {
        if (_atlas is null) return;
        Pose = pose;
        var cell = _atlas.GetSize() / 2;
        _poseTexture.Atlas = _atlas;
        _poseTexture.Region = new Rect2(new Vector2(pose % 2, pose / 2) * cell, cell);
    }

    private void StopMotion()
    {
        if (_breathing?.IsValid() == true) _breathing.Kill();
        _breathing = null; _timer?.Stop(); Scale = Vector2.One;
    }

    public override void _ExitTree()
    {
        StopMotion(); Texture = null; _poseTexture.Dispose(); _atlas = null!; _configured = false;
    }
}

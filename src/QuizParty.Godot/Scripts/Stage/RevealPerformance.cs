using Godot;

namespace QuizParty.Presentation;

/// <summary>Authored visual timeline; never selects answers or changes game time.</summary>
public partial class RevealPerformance : Control
{
    public const double Duration = 5.2;
    public bool AnswerVisible { get; private set; }
    public bool JokeVisible { get; private set; }
    public bool Playing => _player.IsPlaying();
    public event Action<bool, bool>? BeatChanged;
    private Node2D _stage = null!;
    private ShowPuppet _blue = null!;
    private ShowPuppet _orange = null!;
    private AnimationPlayer _player = null!;
    private AudioStreamPlayer _audio = null!;
    private bool _reduced;
    private bool _sound = true;
    private float _volume = .65f;

    public override void _Ready()
    {
        MouseFilter = MouseFilterEnum.Ignore;
        _stage = new Node2D { Name = "Cast" }; AddChild(_stage);
        _blue = new ShowPuppet { Name = "Blue", Blue = true, Position = new(230, 310) }; _stage.AddChild(_blue);
        _orange = new ShowPuppet { Name = "Orange", Position = new(670, 310) }; _stage.AddChild(_orange);
        _audio = new AudioStreamPlayer { Name = "PerformanceSound", Stream = GD.Load<AudioStream>("res://Art/LivingShow/reveal-sting.wav") };
        AddChild(_audio);
        _player = new AnimationPlayer { Name = "Choreography" }; AddChild(_player);
        var library = new AnimationLibrary(); library.AddAnimation("reveal", CreateClip());
        _player.AddAnimationLibrary("", library);
        _player.AnimationFinished += _ => SetBeat(true, true);
        Resized += Fit; Fit();
        SetProcess(true);
    }

    private void Fit()
    {
        var scale = Math.Min(Size.X / 780, Size.Y / 340);
        _stage.Scale = Vector2.One * scale;
        _stage.Position = new((Size.X - 900 * scale) / 2, (Size.Y - 340 * scale) / 2);
        QueueRedraw();
    }

    public override void _Draw()
    {
        if (_stage is null) return;
        foreach (var x in new[] { 230f, 670f })
        {
            var center = _stage.Position + new Vector2(x, 316) * _stage.Scale;
            DrawSetTransform(center, 0, new Vector2(1, .2f));
            DrawCircle(Vector2.Zero, 94 * _stage.Scale.X, new Color(.01f, .005f, .04f, .45f));
            DrawArc(Vector2.Zero, 110 * _stage.Scale.X, 0, Mathf.Tau, 64, new Color(1, .75f, .2f, .3f), 2, true);
        }
        DrawSetTransform(Vector2.Zero);
    }

    public void Configure(bool reducedMotion, bool sound, float volume)
    {
        _sound = sound; _volume = Math.Clamp(volume, 0, 1);
        _audio.VolumeDb = Mathf.LinearToDb(Math.Max(.0001f, _volume));
        if (!_sound || _volume == 0) _audio.Stop();
        if (reducedMotion && !_reduced) FinishImmediately();
        _reduced = reducedMotion;
    }

    public void Replay()
    {
        Stop(); _blue.ResetPose(); _orange.ResetPose();
        _blue.Position = new(230, 310); _orange.Position = new(670, 310);
        SetBeat(false, false);
        if (_reduced) { FinishImmediately(); return; }
        _player.Play("reveal"); _player.Advance(0);
        if (_sound && _volume > 0) _audio.Play();
    }

    public void Stop() { _player.Stop(); _audio.Stop(); }

    public void FinishImmediately()
    {
        Stop(); _blue.ResetPose(); _orange.ResetPose();
        _blue.Position = new(230, 310); _orange.Position = new(670, 310);
        _blue.SetExpression(1); _orange.SetExpression(2);
        SetBeat(true, true);
    }

    // Reading a presentation timeline is cosmetic. There is no clock/score authority here.
    public override void _Process(double delta)
    {
        if (!_player.IsPlaying()) return;
        var time = _player.CurrentAnimationPosition;
        _blue.SetExpression(time >= 1.4 ? 1 : 0);
        _orange.SetExpression(time < 1.45 ? 0 : time < 2.7 ? 1 : 2);
        SetBeat(time >= 1.4, time >= 2.7);
    }

    private void SetBeat(bool answer, bool joke)
    {
        if (answer == AnswerVisible && joke == JokeVisible) return;
        AnswerVisible = answer; JokeVisible = joke; BeatChanged?.Invoke(answer, joke);
    }

    private static Animation CreateClip()
    {
        var clip = new Animation { Length = Duration };
        Track(clip, "Cast/Blue:position", (0, new Vector2(160, 310)), (.5, new Vector2(230, 310)),
            (1.05, new Vector2(218, 316)), (1.4, new Vector2(250, 290)), (1.7, new Vector2(248, 310)),
            (2, new Vector2(248, 280)), (2.3, new Vector2(248, 310)), (3, new Vector2(230, 310)), (5.2, new Vector2(230, 310)));
        Track(clip, "Cast/Blue:rotation", (0, -.12f), (.5, 0f), (1.05, -.08f), (1.4, .08f), (1.8, 0f), (3, -.04f), (5.2, 0f));
        Track(clip, "Cast/Blue/Head:rotation", (0, .08f), (.6, -.08f), (1.05, -.16f), (1.5, .06f), (1.8, -.06f), (2.7, .12f), (3.4, -.03f), (5.2, 0f));
        Track(clip, "Cast/Blue/RightArm:rotation", (0, .25f), (.6, .1f), (1, .45f), (1.4, -.65f), (2.1, -.4f), (3, -.1f), (5.2, 0f));
        Track(clip, "Cast/Blue/LeftArm:rotation", (0, -.2f), (.7, .12f), (1.4, .4f), (1.9, .65f), (2.3, .3f), (3.4, 0f), (5.2, 0f));
        Track(clip, "Cast/Blue/Body:scale", (0, Vector2.One), (1.05, new Vector2(1.04f, .94f)), (1.4, new Vector2(.97f, 1.05f)), (1.8, Vector2.One), (5.2, Vector2.One));
        Track(clip, "Cast/Orange:position", (0, new Vector2(750, 310)), (.6, new Vector2(670, 310)),
            (1.3, new Vector2(655, 310)), (1.58, new Vector2(697, 296)), (1.9, new Vector2(690, 310)),
            (2.5, new Vector2(680, 324)), (3.3, new Vector2(670, 310)), (5.2, new Vector2(670, 310)));
        Track(clip, "Cast/Orange:rotation", (0, .12f), (.6, 0f), (1.3, -.08f), (1.65, .16f), (1.95, -.05f), (2.5, .07f), (3.4, 0f), (5.2, 0f));
        Track(clip, "Cast/Orange/Head:rotation", (0, -.08f), (.6, .04f), (1.3, -.12f), (1.58, .16f), (1.88, -.12f), (2.12, .1f), (2.5, .15f), (3.2, -.1f), (3.7, .03f), (5.2, 0f));
        Track(clip, "Cast/Orange/LeftArm:rotation", (0, .15f), (1.2, .25f), (1.6, .65f), (2.2, -.3f), (2.8, .5f), (3.5, .1f), (5.2, 0f));
        Track(clip, "Cast/Orange/RightArm:rotation", (0, -.1f), (1.2, -.2f), (1.6, -.7f), (2.2, .3f), (2.8, -.45f), (3.5, -.1f), (5.2, 0f));
        Track(clip, "Cast/Orange/Head:position", (0, new Vector2(0, -205)), (1.4, new Vector2(0, -205)),
            (1.65, new Vector2(0, -216)), (2.5, new Vector2(0, -192)), (3.3, new Vector2(0, -205)), (5.2, new Vector2(0, -205)));
        return clip;
    }

    private static void Track(Animation clip, string path, params (double Time, Variant Value)[] keys)
    {
        var index = clip.AddTrack(Animation.TrackType.Value);
        clip.TrackSetPath(index, path);
        clip.TrackSetInterpolationType(index, Animation.InterpolationType.Cubic);
        foreach (var key in keys) clip.TrackInsertKey(index, key.Time, key.Value);
    }

    public override void _ExitTree() { if (_player is not null) Stop(); }
}

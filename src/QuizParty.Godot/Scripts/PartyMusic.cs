using Godot;

namespace QuizParty.Presentation;

/// <summary>Scene-owned music that follows public game state, independent of game rules.</summary>
public partial class PartyMusic : Node
{
    private readonly AudioStreamPlayer[] _players = new AudioStreamPlayer[2];
    private readonly Dictionary<string, AudioStreamWav> _tracks = [];
    private Tween? _fade;
    private int _active;
    private string _track = "";
    private bool _enabled = true;
    private float _volume = .65f;
    public string CurrentTrack => _track;

    public override void _Ready()
    {
        for (var i = 0; i < _players.Length; i++)
        {
            _players[i] = new AudioStreamPlayer { Name = "Music" + i, VolumeDb = -80 };
            AddChild(_players[i]);
        }
    }

    public void Configure(bool enabled, float volume)
    {
        _enabled = enabled && volume > 0;
        _volume = Math.Clamp(volume, 0, 1);
        if (!_enabled)
        {
            if (_fade?.IsValid() == true) _fade.Kill();
            foreach (var player in _players) player.Stop();
        }
        else if (_track.Length > 0 && !_players[_active].Playing) StartTrack(_track);
        else if (_enabled)
        {
            if (_fade?.IsValid() == true) _fade.Kill();
            _players[1 - _active].Stop();
            _players[_active].VolumeDb = TargetDb();
        }
    }

    public static string QuestionPhase(bool untimed, bool paused, double seconds) =>
        !untimed && !paused && seconds <= 8 ? "Urgent" : "QuestionActive";

    public void SetPhase(string phase)
    {
        var track = phase switch
        {
            "QuestionActive" or "QuestionLocked" => "question",
            "Urgent" => "tension",
            "AnswerReveal" => "reveal",
            "Scoreboard" or "RoundEnd" => "scoreboard",
            "GameOver" => "final",
            _ => "menu"
        };
        if (_track == track) return;
        _track = track;
        if (_enabled) StartTrack(track);
    }

    private float TargetDb() => -10f + Mathf.LinearToDb(Math.Max(.0001f, _volume));

    private void StartTrack(string track)
    {
        if (_fade?.IsValid() == true) _fade.Kill();
        var previous = _players[_active];
        _active = 1 - _active;
        var next = _players[_active];
        next.Stop();
        if (!_tracks.TryGetValue(track, out var stream))
        {
            stream = GD.Load<AudioStreamWav>($"res://Art/Music/{track}.wav");
            stream.LoopMode = AudioStreamWav.LoopModeEnum.Forward;
            stream.LoopBegin = 0;
            stream.LoopEnd = stream.Data.Length / 2;
            _tracks.Add(track, stream);
        }
        next.Stream = stream;
        next.VolumeDb = -60;
        next.Play();
        _fade = CreateTween().SetParallel();
        _fade.TweenProperty(next, "volume_db", TargetDb(), .65);
        _fade.TweenProperty(previous, "volume_db", -60f, .65);
        _fade.Chain().TweenCallback(Callable.From(previous.Stop));
    }
    public override void _ExitTree()
    {
        if (_fade?.IsValid() == true) _fade.Kill();
        foreach (var player in _players)
        {
            player.Stop();
            player.Stream = null;
        }
        foreach (var stream in _tracks.Values) stream.Dispose();
        _tracks.Clear();
    }
}

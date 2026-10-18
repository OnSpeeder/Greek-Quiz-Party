using System.Text.Json;
using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;
using FileAccess = Godot.FileAccess;

namespace QuizParty.Presentation;

/// <summary>Opt-in debug/CLI regression, never enabled by normal game navigation.</summary>
public partial class MatchProcessProbe : Node
{
    public const string DeviceArgumentsPath = "user://phase04-test-args.json";
    private LobbyTransport _transport = null!;
    private string[] _args = [];
    private bool _auto;
    private bool _ready;
    private Guid _answered;
    private int _players = 2;
    private bool Live => GodotObject.IsInstanceValid(this) && IsInsideTree();

    // Android's exported launcher deliberately strips CLI extras. A debug-only,
    // app-private fixture enables actual-hardware regression without input injection.
    public static string[] LaunchArguments()
    {
        var original = OS.GetCmdlineUserArgs();
        if (original.Any(value => value.StartsWith("--match-", StringComparison.Ordinal) || value.StartsWith("--lan-", StringComparison.Ordinal)) ||
            !OS.IsDebugBuild() || !FileAccess.FileExists(DeviceArgumentsPath)) return original;
        using var file = FileAccess.Open(DeviceArgumentsPath, FileAccess.ModeFlags.Read);
        if (file is null || file.GetLength() > 4096) { GD.PushWarning("Invalid device test arguments file."); return original; }
        try
        {
            var values = JsonSerializer.Deserialize<string[]>(file.GetAsText());
            if (values is { Length: > 0 and <= 12 } && values.All(value => value is { Length: > 0 and <= 253 } &&
                (value.StartsWith("--match-", StringComparison.Ordinal) || value.StartsWith("--lan-", StringComparison.Ordinal))))
                return values;
        }
        catch (JsonException error) { GD.PushWarning($"Invalid device test arguments: {error.Message}"); }
        return original;
    }

    public override void _Ready()
    {
        _args = LaunchArguments();
        if (_args.Any(value => value.StartsWith("--match-", StringComparison.Ordinal))) Callable.From(Begin).CallDeferred();
    }

    private string? Argument(string prefix) => _args.FirstOrDefault(value => value.StartsWith(prefix, StringComparison.Ordinal))?[prefix.Length..];

    private void Begin()
    {
        _transport = GetParent().GetNode<LobbyTransport>("Transport");
        _auto = _args.Contains("--match-auto");
        if (!int.TryParse(Argument("--match-port=") ?? "7777", out var port) ||
            !int.TryParse(Argument("--match-players=") ?? "2", out _players) || _players is < 2 or > 8)
        { GetTree().Quit(2); return; }
        _transport.PlayMatch = true;
        if (int.TryParse(Argument("--match-fixture="), out var count)) _transport.UseSyntheticQuestions(count);
        _transport.SnapshotChanged += snapshot =>
        {
            if (!_auto || snapshot.Phase != "Lobby") return;
            if (_transport.IsHost && snapshot.Players.Length == _players && snapshot.Players.All(player => player.Ready)) _transport.StartGame();
            else if (!_transport.IsHost && !_ready) { _ready = true; _transport.SetReady(true); }
        };
        _transport.MatchChanged += OnMatch;
        var error = _args.Contains("--match-host")
            ? _transport.Host("QuizParty", Argument("--match-name=") ?? "Host", port)
            : _transport.Join(Argument("--match-join=") ?? "127.0.0.1", Argument("--match-name=") ?? "Phone", port);
        if (error != Error.Ok) { GD.Print($"MATCH START_ERROR {error}"); GetTree().Quit(2); }
        if (_auto) GetTree().CreateTimer(600).Timeout += () => { if (Live && _transport.MatchSnapshot?.Phase != "GameOver") GetTree().Quit(3); };
    }

    private void OnMatch(MatchSnapshotDto snapshot)
    {
        if (!_auto) return;
        if (snapshot.Phase == "QuestionActive" && _answered != snapshot.Question.InstanceId &&
            snapshot.EligiblePlayers.Contains(_transport.LocalPlayerId ?? Guid.Empty) && !_args.Contains("--match-unanswered"))
        {
            _answered = snapshot.Question.InstanceId;
            // Bots know this tiny fixture, not the shuffled index. This is never used by the UI.
            var correct = Array.IndexOf(snapshot.Question.Answers, "Αθήνα");
            if (correct < 0) correct = Array.IndexOf(snapshot.Question.Answers, "Σωστό");
            if (correct < 0) { GD.PushError("Bot does not recognize fixture."); GetTree().Quit(4); return; }
            var index = _args.Contains("--match-wrong") ? (correct + 1) % 4 : correct;
            var delay = double.TryParse(Argument("--match-delay="), System.Globalization.NumberStyles.Float,
                System.Globalization.CultureInfo.InvariantCulture, out var seconds) ? seconds : 0.25;
            GetTree().CreateTimer(Math.Clamp(delay, 0.05, 30)).Timeout += () =>
            {
                if (!Live || _transport.MatchSnapshot?.Question.InstanceId != snapshot.Question.InstanceId) return;
                _transport.SubmitAnswer(index);
                if (!_transport.IsHost) _transport.SubmitAnswer(index, repeatLastRequest: true);
            };
        }
        if (_transport.IsHost && snapshot.Phase is "AnswerReveal" or "Scoreboard" or "RoundEnd")
            GetTree().CreateTimer(_args.Contains("--match-fast") ? 0.05 : 1).Timeout += () =>
            { if (Live && _transport.MatchSnapshot?.Revision == snapshot.Revision) _transport.AdvanceMatch(); };
        if (snapshot.Phase == "GameOver")
        {
            GD.Print($"MATCH AUTO_PASS question={snapshot.Question.InstanceId} players={snapshot.Scores.Length}");
            foreach (var result in snapshot.Reveal!.Players)
            {
                var name = snapshot.Scores.Single(score => score.PlayerId == result.PlayerId).DisplayName;
                GD.Print($"MATCH RESULT player={name} answer={result.AnswerIndex?.ToString() ?? "none"} points={result.Points}");
            }
            // Leave the host alive while clients leave together: exercises batched
            // disconnect handling instead of hiding shutdown races behind host exit.
            if (!_args.Contains("--match-keep-open")) GetTree().CreateTimer(_transport.IsHost ? 4 : 2).Timeout += () => { if (Live) GetTree().Quit(); };
        }
        var capture = Argument("--match-capture=");
        if (capture is not null && snapshot.Phase == (Argument("--match-capture-phase=") ?? "GameOver")) Capture(capture);
    }

    private async void Capture(string path)
    {
        await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
        if (Live) GD.Print($"MATCH CAPTURE {GetViewport().GetTexture().GetImage().SavePng(path)}");
    }
}

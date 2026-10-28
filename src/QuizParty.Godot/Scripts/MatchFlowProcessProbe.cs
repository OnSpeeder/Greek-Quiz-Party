using System.Text.Json;
using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Explicit debug-only multi-process unanimity/replay regression.</summary>
public partial class MatchFlowProcessProbe : Node
{
    private LobbyTransport _transport = null!;
    private string[] _args = [];
    private bool _finished;
    private bool _addedLocal;
    private readonly HashSet<string> _scheduled = [];
    private bool Live => GodotObject.IsInstanceValid(this) && IsInsideTree();
    private string? Arg(string prefix) => _args.FirstOrDefault(a => a.StartsWith(prefix, StringComparison.Ordinal))?[prefix.Length..];
    public override void _Ready()
    {
        if (!OS.IsDebugBuild()) return;
        _args = MatchProcessProbe.LaunchArguments();
        if (!_args.Contains("--match-flow-host") && !_args.Contains("--match-flow-client")) return;
        Callable.From(Begin).CallDeferred();
    }
    private void Begin()
    {
        _transport = GetParent().GetNode<LobbyTransport>("Transport");
        if (!_args.Contains("--match-flow-default-discovery")) _transport.DiscoveryPort = 19864;
        _transport.StrategyEnabled = false;
        if (_args.Contains("--match-flow-host")) { _transport.UseSyntheticQuestions(10, _args.Contains("--match-flow-long")); _transport.QuestionCount = 0; _transport.QuestionSeconds = 0; }
        _transport.SnapshotChanged += OnLobby; _transport.MatchChanged += OnMatch;
        _transport.StatusChanged += status => GD.Print($"FLOW STATUS ms={Time.GetTicksMsec()} {status}");
        var port = int.Parse(Arg("--match-flow-port=") ?? "19863");
        var hostPlays = _args.Contains("--match-flow-host-plays");
        var error = _args.Contains("--match-flow-host")
            ? _transport.Host("Flow regression", hostPlays ? "Host" : "", port, hostPlays: hostPlays)
            : _transport.Join(Arg("--match-flow-address=") ?? "127.0.0.1", Arg("--match-flow-name=") ?? "Παίκτης", port);
        if (error != Error.Ok) { GD.PushError($"Flow start failed: {error}"); GetTree().Quit(6); }
        if (error == Error.Ok && _transport.IsHost && hostPlays) _transport.SetReady(true);
        var timeout = int.TryParse(Arg("--match-flow-timeout="), out var seconds) ? Math.Clamp(seconds, 60, 300) : 60;
        GetTree().CreateTimer(timeout).Timeout += () => { if (Live) GetTree().Quit(7); };
    }
    private void OnLobby(LobbySnapshotDto snapshot)
    {
        if (snapshot.Phase != "Lobby") return;
        if (_finished)
        {
            if (_scheduled.Add("replay"))
            {
                if (snapshot.Players.Length != 3 || snapshot.Players.Any(p => p.Ready) || _transport.MatchSnapshot is not null)
                { GD.PushError("Replay did not reset all participants."); GetTree().Quit(8); return; }
                GD.Print("FLOW REPLAY_PASS roster=3 ready=false match=null");
                GetTree().CreateTimer(_transport.IsHost ? 2 : 1).Timeout += () => { if (Live) GetTree().Quit(); };
            }
            return;
        }
        if (_transport.IsHost)
        {
            if (snapshot.Players.Length == 3 && snapshot.Players.All(p => p.Ready))
            { _transport.StartGame(); }
            return;
        }
        if (_args.Contains("--match-flow-local") && !_addedLocal)
        { _addedLocal = true; _transport.AddLocalPlayer("Τοπικός", 1); return; }
        foreach (var player in _transport.OwnedPlayers.Where(p => !p.Ready)) _transport.SetReady(true, localSlot: player.LocalSlot);
    }
    private void OnMatch(MatchSnapshotDto snapshot)
    {
        if (_scheduled.Add($"phase:{snapshot.Question.InstanceId}:{snapshot.Phase}"))
            GD.Print($"FLOW PHASE ms={Time.GetTicksMsec()} question={snapshot.QuestionNumber} phase={snapshot.Phase}");
        if (snapshot.Phase == "GameOver")
        {
            if (_finished) return; _finished = true;
            GD.Print("FLOW FINAL " + JsonSerializer.Serialize(snapshot.Scores.OrderBy(p => p.PlayerId)));
            Capture("final", .6);
            if (_transport.IsHost) GetTree().CreateTimer(1.5).Timeout += () => { if (Live) _transport.Replay(); };
            return;
        }
        if (_transport.IsHost)
        {
            if (snapshot.QuestionNumber == 1 && snapshot.Phase == "QuestionActive" && snapshot.AcceptedAnswerCount is > 0 and < 3) Capture("answering", .05);
            if (snapshot.Phase == "AnswerReveal") Capture("facts", 1.5);
            if (snapshot.Phase == "Scoreboard") { Capture("scoreboard", .3); Capture("scoreboard-end", 1.0); Capture("scoreboard-settled", 1.6); }
            if (!_args.Contains("--match-flow-host-plays")) return;
        }
        if (snapshot.Phase == "QuestionActive")
        {
            Capture("controller", .05);
            foreach (var player in _transport.OwnedPlayers)
            {
                if (!_scheduled.Add($"answer:{snapshot.Question.InstanceId}:{player.LocalSlot}")) continue;
                var delay = _args.Contains("--match-flow-stagger") ? _transport.IsHost ? .1 : _args.Contains("--match-flow-name=local") ? .4 : 2.0 : _args.Contains("--match-flow-local") ? .15 : .8;
                GetTree().CreateTimer(delay).Timeout += () =>
                { if (Live) _transport.SubmitAnswer(Array.FindIndex(snapshot.Question.Answers, answer => answer.StartsWith("Σωστό", StringComparison.Ordinal)), localSlot: player.LocalSlot); };
            }
        }
        if (snapshot.Phase is "AnswerReveal" or "Scoreboard")
        {
            Capture(snapshot.Phase == "AnswerReveal" ? "facts" : "scoreboard", snapshot.Phase == "AnswerReveal" ? 1.5 : .3);
            if (snapshot.Phase == "Scoreboard") { Capture("scoreboard-end", 1.0); Capture("scoreboard-settled", 1.6); }
            foreach (var player in _transport.OwnedPlayers)
            {
                if (!_scheduled.Add($"vote:{snapshot.Question.InstanceId}:{snapshot.Phase}:{player.LocalSlot}")) continue;
                var hold = _args.Contains("--match-flow-idle-scoreboard") && snapshot.Phase == "Scoreboard" && snapshot.QuestionNumber == 1;
                GetTree().CreateTimer(snapshot.Phase == "AnswerReveal" ? 2.1 : hold ? 15 : 1.1).Timeout += () =>
                {
                    if (!Live) return;
                    GD.Print($"FLOW VOTE ms={Time.GetTicksMsec()} question={snapshot.QuestionNumber} phase={snapshot.Phase} slot={player.LocalSlot}");
                    _transport.ContinueMatch(snapshot.Phase == "Scoreboard" && snapshot.QuestionNumber == 2, player.LocalSlot);
                };
            }
        }
    }
    private async void Capture(string name, double delay)
    {
        var folder = Arg("--match-flow-capture=");
        if (folder is null || DisplayServer.GetName() == "headless" || !_scheduled.Add("capture:" + name)) return;
        try
        {
            await ToSignal(GetTree().CreateTimer(delay), global::Godot.Timer.SignalName.Timeout);
            if (!Live) return;
            await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
            if (Live) GetViewport().GetTexture().GetImage().SavePng(folder + "/" + name + ".png");
        }
        catch (Exception error) { GD.PushError($"Flow capture failed: {error}"); if (Live) GetTree().Quit(9); }
    }
}

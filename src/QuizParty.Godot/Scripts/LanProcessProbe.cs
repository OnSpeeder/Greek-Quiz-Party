using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Explicit debug-only LAN acceptance driver; normal navigation never enables it.</summary>
public partial class LanProcessProbe : Node
{
    private LobbyTransport _transport = null!;
    private string[] _args = [];
    private bool _joining;
    private bool _ready;
    private bool _answered;
    private bool Live => GodotObject.IsInstanceValid(this) && IsInsideTree();
    private string? Argument(string prefix) => _args.FirstOrDefault(v => v.StartsWith(prefix, StringComparison.Ordinal))?[prefix.Length..];

    public override void _Ready()
    {
        if (!OS.IsDebugBuild()) return;
        _args = MatchProcessProbe.LaunchArguments();
        if (_args.Any(a => a.StartsWith("--lan-", StringComparison.Ordinal))) Callable.From(Begin).CallDeferred();
    }

    private void Begin()
    {
        _transport = GetParent().GetNode<LobbyTransport>("Transport");
        if (!int.TryParse(Argument("--lan-port=") ?? "7777", out var port) ||
            !int.TryParse(Argument("--lan-discovery-port=") ?? "7778", out var discoveryPort)) { GetTree().Quit(2); return; }
        _transport.DiscoveryPort = discoveryPort;
        _transport.PlayMatch = _args.Contains("--lan-match");
        _transport.StrategyEnabled = false;
        _transport.QuestionSeconds = 5;
        _transport.StatusChanged += OnStatus;
        _transport.MatchChanged += OnMatch;
        _transport.SnapshotChanged += snapshot =>
        {
            if (snapshot.Phase != "Lobby") return;
            if (!_transport.IsHost && !_ready) { _ready = true; _transport.SetReady(true); }
            if (_transport.IsHost && int.TryParse(Argument("--lan-start-players="), out var players) &&
                snapshot.Players.Length == players && snapshot.Players.All(p => p.Ready)) _transport.StartGame();
        };
        _transport.Discovery.RoomsChanged += rooms =>
        {
            foreach (var r in rooms) GD.Print($"LAN FOUND room={r.Room.RoomName} address={r.Address} port={r.Room.GamePort} players={r.Room.Players} requiresPin={r.Room.RequiresPin} state={r.Room.State}");
            if (_args.Contains("--lan-scan-only") || _joining) return;
            var room = rooms.FirstOrDefault(r => r.Room.State == "Lobby" && r.Room.Players < r.Room.MaxPlayers);
            if (room is null) return;
            _joining = true;
            Check(_transport.Join(room.Address, Argument("--lan-name=") ?? "Browser", room.Room.GamePort, Argument("--lan-pin=") ?? ""));
        };
        _transport.Discovery.StatusChanged += reason =>
        {
            if (reason is not ("NoRooms" or "Finished")) return;
            var count = _transport.Discovery.Rooms.Count;
            if (_args.Contains("--lan-scan-only"))
            {
                var expectedEmpty = _args.Contains("--lan-expect-empty");
                GD.Print($"LAN SCAN_PASS rooms={count}");
                if (!_args.Contains("--lan-stay")) GetTree().Quit(expectedEmpty == (count == 0) ? 0 : 2);
            }
            else if (!_joining) GetTree().Quit(2);
        };
        if (_args.Contains("--lan-host")) Check(_transport.Host("LANTest", Argument("--lan-name=") ?? "Host", port, Argument("--lan-pin=") ?? ""));
        else if (_args.Contains("--lan-find")) Check(_transport.Discovery.Scan(discoveryPort));
        else Check(_transport.Join(Argument("--lan-join=") ?? "127.0.0.1", Argument("--lan-name=") ?? "Manual", port, Argument("--lan-pin=") ?? ""));
        var capture = Argument("--lan-capture=");
        if (capture is not null) GetTree().CreateTimer(2).Timeout += () => { if (Live) Capture(capture); };
        GetTree().CreateTimer(45).Timeout += () => { if (Live && !_args.Contains("--lan-stay")) GetTree().Quit(3); };
    }

    private void Check(Error error)
    { if (error != Error.Ok) { GD.Print($"LAN START_ERROR {error}"); GetTree().Quit(2); } }

    private void OnStatus(string reason)
    {
        if (reason == "Joined")
        {
            GD.Print($"LAN JOINED player={_transport.LocalPlayerId}");
            if (!_args.Contains("--lan-stay") && !_args.Contains("--lan-leave-question"))
                GetTree().CreateTimer(1).Timeout += () => { if (Live) GetTree().Quit(); };
        }
        else if (reason == "ServerDisconnected") { GD.Print("LAN SERVER_LEFT match-cannot-resume"); GetTree().Quit(); }
        else if (reason is "WrongPin" or "PinRateLimited" or "GameStarted" or "RoomFull" or "IncompatibleVersion" or "ConnectionTimeout" or "ConnectionFailed")
        { if (!_args.Contains("--lan-stay")) GetTree().Quit(2); }
    }

    private void OnMatch(MatchSnapshotDto match)
    {
        if (!_transport.IsHost && match.Phase == "QuestionActive" && _args.Contains("--lan-leave-question"))
        {
            _transport.Stop(); GD.Print("LAN LEFT_QUESTION"); GetTree().Quit(); return;
        }
        if (_transport.IsHost && match.Phase == "QuestionActive" && !_answered)
        {
            _answered = true;
            var correct = Array.IndexOf(match.Question.Answers, "Αθήνα");
            GetTree().CreateTimer(0.1).Timeout += () => { if (Live) _transport.SubmitAnswer(correct); };
        }
        if (_transport.IsHost && match.Phase is "AnswerReveal" or "Scoreboard" or "RoundEnd")
            GetTree().CreateTimer(0.1).Timeout += () => { if (Live && _transport.MatchSnapshot?.Revision == match.Revision) _transport.AdvanceMatch(); };
        if (match.Phase == "GameOver") GD.Print("LAN MATCH_FINISHED disconnected-seat-timed-out");
    }

    private async void Capture(string path)
    {
        await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
        if (Live) GD.Print($"LAN CAPTURE {GetViewport().GetTexture().GetImage().SavePng(path)}");
    }
}

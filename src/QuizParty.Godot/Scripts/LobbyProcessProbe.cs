using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Opt-in process regression driver; does nothing during normal navigation.</summary>
public partial class LobbyProcessProbe : Node
{
    private LobbyTransport _transport = null!;
    private bool _auto;
    private bool _readySent;
    private bool _forbiddenSent;
    private string[] _arguments = [];

    public override void _Ready()
    {
        _arguments = OS.GetCmdlineUserArgs();
        if (!_arguments.Any(argument => argument.StartsWith("--lobby-", StringComparison.Ordinal))) return;
        // Parent view and transport subscriptions are initialized first.
        Callable.From(Begin).CallDeferred();
    }

    private string? Argument(string prefix) => _arguments.FirstOrDefault(value => value.StartsWith(prefix, StringComparison.Ordinal))?[prefix.Length..];

    private void Begin()
    {
        _transport = GetParent().GetNode<LobbyTransport>("Transport");
        _auto = _arguments.Contains("--lobby-auto");
        if (_auto) _transport.PlayMatch = false;
        _transport.SnapshotChanged += OnSnapshot;
        _transport.StatusChanged += reason =>
        {
            if (_auto && reason is "IncompatibleVersion" or "ConnectionTimeout" or "ConnectionFailed" or "GameStarted" or "RoomFull") GetTree().Quit(2);
            if (_auto && reason == "ServerDisconnected") { GD.Print("LOBBY AUTO_SERVER_LEFT"); GetTree().Quit(); }
            if (_auto && reason == "NotHost")
            {
                GD.Print("LOBBY AUTO_CLIENT_START_REJECTED");
                _transport.SetReady(true);
                _transport.SetReady(true, repeatLastRequest: true);
            }
        };
        if (!int.TryParse(Argument("--lobby-port=") ?? "7777", out var port) ||
            !int.TryParse(Argument("--lobby-protocol=") ?? LobbyProtocol.Version.ToString(), out var protocol)) { GetTree().Quit(2); return; }
        _transport.ClientProtocol = protocol;
        var error = _arguments.Contains("--lobby-host")
            ? _transport.Host("QuizParty", Argument("--lobby-name=") ?? "Host", port)
            : _transport.Join(Argument("--lobby-join=") ?? "127.0.0.1", Argument("--lobby-name=") ?? "Client", port);
        if (error != Error.Ok) { GD.Print($"LOBBY START_ERROR {error}"); GetTree().Quit(2); }
        if (_auto && _arguments.Contains("--lobby-cancel-join"))
        {
            GetTree().CreateTimer(0.1).Timeout += () => { if (IsLive) _transport.QueueFree(); };
            // Stay alive beyond the old join deadline to expose stale/freed callbacks.
            GetTree().CreateTimer(11).Timeout += () =>
            {
                if (!IsLive) return;
                GD.Print("LOBBY AUTO_CANCEL_PASS");
                GetTree().Quit();
            };
        }
        if (_auto) GetTree().CreateTimer(25).Timeout += () => { if (IsLive) GetTree().Quit(3); };
        var capture = Argument("--lobby-capture=");
        if (capture is not null) GetTree().CreateTimer(1).Timeout += () => { if (IsLive) Capture(capture); };
    }

    private async void Capture(string path)
    {
        await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
        if (!IsLive) return;
        var error = GetViewport().GetTexture().GetImage().SavePng(path);
        GD.Print($"LOBBY CAPTURE {error}");
    }

    private void OnSnapshot(LobbySnapshotDto snapshot)
    {
        if (!_auto) return;
        if (snapshot.Phase == "GameStarting")
        {
            GD.Print($"LOBBY AUTO_STARTED revision={snapshot.Revision} players={snapshot.Players.Length}");
            // Give every peer a chance to observe the same final revision before exiting.
            if (!_transport.IsHost && _arguments.Contains("--lobby-exit-start"))
                GetTree().CreateTimer(1).Timeout += () => { if (IsLive) GetTree().Quit(); };
            return;
        }
        if (_transport.IsHost)
        {
            if (snapshot.Players.Length == 3 && snapshot.Players.All(player => player.Ready)) _transport.StartGame();
        }
        else if (!_readySent)
        {
            _readySent = true;
            if (_arguments.Contains("--lobby-test-start") && !_forbiddenSent)
            {
                _forbiddenSent = true;
                _transport.SendStartRequest();
            }
            else
            {
                _transport.SetReady(true);
                _transport.SetReady(true, repeatLastRequest: true);
            }
        }
    }

    private bool IsLive => GodotObject.IsInstanceValid(this) && IsInsideTree();
}

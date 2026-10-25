using System.Text.Json;
using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Explicit debug-only mixed-controller playtest. Never active during normal navigation.</summary>
public partial class MixedProcessProbe : Node
{
    private LobbyTransport _transport = null!;
    private string[] _args = [];
    private int _localCount, _total;
    private readonly HashSet<int> _added = new(), _readied = new();
    private readonly HashSet<(Guid Question, int Slot)> _answered = new();
    private long _advanceRevision;
    private bool _finished;
    private bool Live => GodotObject.IsInstanceValid(this) && IsInsideTree();
    private string? Arg(string prefix) => _args.FirstOrDefault(a => a.StartsWith(prefix, StringComparison.Ordinal))?[prefix.Length..];
    public override void _Ready()
    {
        _args = MatchProcessProbe.LaunchArguments();
        if (OS.IsDebugBuild() && _args.Contains("--match-mixed")) Callable.From(Begin).CallDeferred();
    }
    private void Begin()
    {
        if (!int.TryParse(Arg("--match-local=") ?? "1", out _localCount) || _localCount is < 0 or > 8 || _localCount == 0 && !_args.Contains("--match-host") ||
            !int.TryParse(Arg("--match-players=") ?? "2", out _total) || _total is < 2 or > 8 ||
            !int.TryParse(Arg("--match-port=") ?? "7777", out var port)) { GetTree().Quit(2); return; }
        _transport = GetParent().GetNode<LobbyTransport>("Transport");
        _transport.DiscoveryPort = port == 65535 ? 65534 : port + 1;
        _transport.StrategyEnabled = _args.Contains("--match-strategy");
        _transport.AllowSteal = _args.Contains("--match-steal");
        _transport.DebugStrategySeed = int.TryParse(Arg("--match-seed="), out var seed) ? seed : 8;
        if (_args.Contains("--match-host") && int.TryParse(Arg("--match-fixture="), out var count)) _transport.UseSyntheticQuestions(count);
        var timer = new global::Godot.Timer { WaitTime = 0.05, Autostart = true };
        timer.Timeout += Think; AddChild(timer);
        var error = _args.Contains("--match-host") ? _transport.Host("Mixed test", Arg("--match-name=") ?? "Host", port, hostPlays: _localCount > 0) :
            _transport.Join(Arg("--match-join=") ?? "127.0.0.1", Arg("--match-name=") ?? "Phone", port);
        if (error != Error.Ok) { GD.PushError($"Mixed probe startup: {error}"); GetTree().Quit(2); }
        GetTree().CreateTimer(600).Timeout += () => { if (Live && !_finished) { GD.PushError("Mixed match timed out."); GetTree().Quit(3); } };
    }
    private void Think()
    {
        if (_finished || _transport.Snapshot is not { } lobby) return;
        if (lobby.Phase == "Lobby")
        {
            for (var slot = 1; slot < _localCount; slot++)
                if (!_transport.OwnedPlayers.Any(p => p.LocalSlot == slot) && _added.Add(slot))
                { _transport.AddLocalPlayer($"{Arg("--match-name=") ?? "Player"}{slot}", slot); return; }
            foreach (var own in _transport.OwnedPlayers)
                if (!own.Ready && _readied.Add(own.LocalSlot)) { _transport.SetReady(true, localSlot: own.LocalSlot); return; }
            if (!_transport.IsHost) return;
            if (_args.Contains("--match-teams") && !lobby.TeamMode) { _transport.SetTeamMode(true); return; }
            if (lobby.Players.Length != _total || lobby.Players.Any(p => !p.Ready)) return;
            if (lobby.TeamMode)
            {
                var hasOdd = lobby.Players.Any(p => p.LocalSlot % 2 == 1);
                for (var i = 0; i < lobby.Players.Length; i++)
                {
                    var expected = (hasOdd ? lobby.Players[i].LocalSlot : i) % 2 + 1;
                    if (lobby.Players[i].TeamId != expected) { _transport.AssignTeam(lobby.Players[i].PlayerId, expected); return; }
                }
            }
            _transport.StartGame(); return;
        }
        foreach (var own in _transport.OwnedPlayers)
        {
            var view = _transport.MatchForSlot(own.LocalSlot);
            if (view is null) continue;
            if (view.LocalSlot != own.LocalSlot || view.Private is { } personal && personal.PlayerId != own.PlayerId)
            { GD.PushError("Mixed owner privacy failure."); GetTree().Quit(4); return; }
            if (view.Phase == "QuestionActive" && view.EligiblePlayers.Contains(own.PlayerId) && _answered.Add((view.Question.InstanceId, own.LocalSlot)))
            {
                var local = own;
                GetTree().CreateTimer(0.12 + own.LocalSlot * 0.05 + (_transport.IsHost ? 0 : 0.2)).Timeout += () => Answer(local, view.Question.InstanceId);
            }
        }
        var snapshot = _transport.MatchSnapshot;
        if (snapshot is null) return;
        if (_transport.IsHost && snapshot.Phase is "AnswerReveal" or "Scoreboard" or "RoundEnd" && _advanceRevision != snapshot.Revision)
        {
            _advanceRevision = snapshot.Revision;
            GetTree().CreateTimer(0.25).Timeout += () =>
            { if (Live && _transport.MatchSnapshot?.Revision == snapshot.Revision) _transport.AdvanceMatch(); };
        }
        if (snapshot.Phase != "GameOver" || _transport.OwnedPlayers.Any(p => _transport.MatchForSlot(p.LocalSlot)?.Phase != "GameOver")) return;
        _finished = true;
        GD.Print($"MIXED OWN count={_transport.OwnedPlayers.Count} slots={string.Join('|', _transport.OwnedPlayers.Select(p => p.LocalSlot))}");
        var final = JsonSerializer.Serialize(new { snapshot.Scores, snapshot.Teams, snapshot.WinningTeams, snapshot.Winners, snapshot.Statistics, snapshot.FinalStrategy });
        GD.Print($"MIXED FINAL {final}");
        GD.Print($"MIXED DIGEST {Convert.ToHexString(System.Security.Cryptography.SHA256.HashData(System.Text.Encoding.UTF8.GetBytes(final)))}");
        GD.Print($"MIXED PASS players={snapshot.Scores.Length} questions={snapshot.QuestionNumber} teams={snapshot.Teams?.Length ?? 0}");
        if (Arg("--match-capture=") is { } capture) Capture(capture);
        if (!_args.Contains("--match-keep-open")) GetTree().CreateTimer(_transport.IsHost ? 3 : 1.5).Timeout += () => { if (Live) GetTree().Quit(); };
    }
    private async void Answer(LobbyPlayerDto player, Guid question)
    {
        try
        {
            if (!Live || _transport.MatchForSlot(player.LocalSlot) is not { Phase: "QuestionActive" } snapshot || snapshot.Question.InstanceId != question) return;
            var correct = Array.IndexOf(snapshot.Question.Answers, "Σωστό");
            if (correct < 0) correct = Array.IndexOf(snapshot.Question.Answers, "Αθήνα");
            if (correct < 0) throw new InvalidOperationException("Unknown synthetic fixture.");
            var card = snapshot.Private?.Hand.FirstOrDefault(c => c.Kind is 0 or 1 or 2 || c.Kind == 4 && !snapshot.Private.Shield);
            if (card is not null && !snapshot.IsTieBreaker)
            {
                _transport.ActivateCard(card.Id, localSlot: player.LocalSlot);
                for (var i = 0; i < 60 && Live && _transport.CardPendingForSlot(player.LocalSlot); i++)
                    await ToSignal(GetTree().CreateTimer(0.05), global::Godot.Timer.SignalName.Timeout);
                if (!Live) return;
                if (_transport.CardPendingForSlot(player.LocalSlot)) throw new TimeoutException("Mixed card receipt timeout.");
            }
            if (!Live || _transport.MatchForSlot(player.LocalSlot) is not { Phase: "QuestionActive" } current || current.Question.InstanceId != question) return;
            var isCorrect = snapshot.Teams is { Length: > 0 } teams ? teams.Single(t => t.Members.Contains(player.PlayerId)).TeamId == 1 : player.LocalSlot % 2 == 0;
            var confidence = snapshot.Strategy?.Confidence == true && !snapshot.IsTieBreaker ? isCorrect ? 3 : 2 : 1;
            _transport.SubmitAnswer(isCorrect ? correct : (correct + 1) % 4, confidence: confidence, localSlot: player.LocalSlot);
            if (!_transport.IsHost) _transport.SubmitAnswer(0, repeatLastRequest: true, localSlot: player.LocalSlot);
        }
        catch (Exception error) { GD.PushError($"Mixed bot failed: {error}"); GetTree().Quit(5); }
    }
    private async void Capture(string path)
    {
        await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
        if (Live) GD.Print($"MIXED CAPTURE {GetViewport().GetTexture().GetImage().SavePng(path)}");
    }
}

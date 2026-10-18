using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

public partial class MatchPanel : VBoxContainer
{
    private LobbyTransport? _transport;
    private MatchSnapshotDto? _snapshot;
    private ulong _receivedAtMs;
    private readonly Button[] _answers = new Button[4];
    private string _reason = "None";
    private Label _progress = null!;
    private Label _statistics = null!;
    private Label _departures = null!;
    private StrategyPanel _strategy = null!;

    public override void _Ready()
    {
        _progress = new Label { Name = "Progress", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_progress);
        MoveChild(_progress, 1);
        _statistics = new Label { Name = "Statistics", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_statistics);
        _departures = new Label { Name = "Departures", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_departures);
        MoveChild(_departures, 2);
        _strategy = new StrategyPanel { Name = "Strategy" };
        AddChild(_strategy); MoveChild(_strategy, GetNode<Button>("Answer0").GetIndex());
        for (var index = 0; index < 4; index++)
        {
            var choice = index;
            _answers[index] = GetNode<Button>($"Answer{index}");
            _answers[index].Pressed += () => _transport?.SubmitAnswer(choice, confidence: _snapshot?.IsTieBreaker == true ? 1 : _strategy.Confidence);
        }
        GetNode<Button>("Continue").Pressed += () => _transport?.AdvanceMatch();
        var timer = new global::Godot.Timer { WaitTime = 0.1, Autostart = true };
        timer.Timeout += UpdateCountdown;
        AddChild(timer);
    }

    public void Bind(LobbyTransport transport)
    {
        _transport = transport;
        transport.MatchChanged += Render;
        transport.MatchInputChanged += OnInputChanged;
        transport.SnapshotChanged += OnLobbyChanged;
        _strategy.Bind(transport);
        transport.CardInputChanged += OnCardInput;
    }
    private void OnCardInput(string reason) => UpdateControls();

    private void OnLobbyChanged(LobbySnapshotDto lobby)
    {
        if (_snapshot is null) return;
        var departed = _snapshot.Scores.Where(s => !lobby.Players.Any(p => p.PlayerId == s.PlayerId)).Select(s => s.DisplayName).ToArray();
        _departures.Text = departed.Length == 0 ? "" : string.Format(Tr("MATCH_DEPARTED"), string.Join(", ", departed));
    }

    private void OnInputChanged(string reason)
    {
        _reason = reason;
        if (_snapshot is { } snapshot) _strategy.Render(snapshot);
        UpdateControls();
    }

    private void Render(MatchSnapshotDto snapshot)
    {
        Visible = true;
        if (_snapshot?.Question.InstanceId != snapshot.Question.InstanceId) _reason = "None";
        _snapshot = snapshot;
        _strategy.Render(snapshot);
        if (_transport?.Snapshot is { } lobby) OnLobbyChanged(lobby);
        _receivedAtMs = global::Godot.Time.GetTicksMsec();
        GetNode<Label>("Question").Text = snapshot.Question.Text;
        GetNode<Label>("Heading").Text = Tr(snapshot.Phase == "GameOver" ? "MATCH_FINAL" : "MATCH_TITLE");
        _progress.Text = snapshot.IsTieBreaker ? Tr("MATCH_TIE") : string.Format(Tr("MATCH_PROGRESS"),
            snapshot.RoundNumber, snapshot.QuestionNumber, snapshot.TotalQuestions);
        _statistics.Text = snapshot.Phase != "GameOver" ? "" :
            string.Format(Tr(snapshot.ContentExhausted ? "MATCH_SHARED" : "MATCH_WINNER"), string.Join(", ",
                snapshot.Scores.Where(s => snapshot.Winners.Contains(s.PlayerId)).Select(s => s.DisplayName))) + "\n" +
            string.Join("\n", snapshot.Statistics.Select(s => string.Format(Tr("MATCH_STATS"),
                snapshot.Scores.Single(p => p.PlayerId == s.PlayerId).DisplayName, s.Correct, s.Wrong, s.Unanswered,
                s.Correct + s.Wrong + s.Unanswered == 0 ? 0 : 100.0 * s.Correct / (s.Correct + s.Wrong + s.Unanswered),
                s.Responses == 0 ? 0 : TimeSpan.FromTicks(s.ResponseTicks / s.Responses).TotalSeconds, s.BestStreak)));
        if (snapshot.Phase == "GameOver" && snapshot.FinalStrategy is { Length: > 0 } final)
            _statistics.Text += "\n" + string.Join("\n", final.Select(s => string.Format(Tr("STRATEGY_FINAL"),
                snapshot.Scores.Single(p => p.PlayerId == s.PlayerId).DisplayName,
                s.Mission is null ? Tr("STRATEGY_NO_MISSION") : Tr("STRATEGY_MISSION_" + (Core.Game.MissionKind)s.Mission.Kind),
                s.Mission?.Progress ?? 0, s.Mission?.Target ?? 0, s.MissionBonus, s.CardsUsed,
                s.ConfidentCorrect, s.ConfidentWrong, s.AllInCorrect, s.AllInWrong,
                s.ConfidentCorrect + s.ConfidentWrong == 0 ? 0 : 100.0 * s.ConfidentCorrect / (s.ConfidentCorrect + s.ConfidentWrong),
                s.AllInCorrect + s.AllInWrong == 0 ? 0 : 100.0 * s.AllInCorrect / (s.AllInCorrect + s.AllInWrong))));
        for (var i = 0; i < 4; i++) _answers[i].Text = $"{(char)('A' + i)}. {snapshot.Question.Answers[i]}";
        GetNode<Label>("Reveal").Text = snapshot.Reveal is null ? "" :
            string.Format(Tr("MATCH_CORRECT"), snapshot.Question.Answers[snapshot.Reveal.CorrectAnswerIndex]) + "\n" + snapshot.Reveal.Explanation;
        GetNode<Label>("Scores").Text = snapshot.Reveal is null ? "" : Tr("MATCH_SCORES") + "\n" +
            string.Join("\n", snapshot.Scores.OrderByDescending(score => score.Total).Select(score =>
                string.Format(Tr("MATCH_PLAYER_SCORE"), score.DisplayName, score.Total)));
        UpdateControls();
        UpdateCountdown();
    }

    private void UpdateControls()
    {
        if (_snapshot is null || _transport is null) return;
        var active = _snapshot.Phase == "QuestionActive";
        for (var i = 0; i < 4; i++)
        {
            _answers[i].Visible = _snapshot.Phase is "QuestionActive" or "QuestionLocked" or "AnswerReveal";
            _answers[i].Disabled = !active || !_snapshot.EligiblePlayers.Contains(_transport.LocalPlayerId ?? Guid.Empty) ||
                _transport.AnswerPending || _transport.CardPending || _transport.OwnAnswerIndex is not null ||
                _snapshot.Private?.HiddenAnswers.Contains(i) == true;
            _answers[i].Text = _snapshot.Private?.HiddenAnswers.Contains(i) == true && _snapshot.Reveal is null
                ? Tr("STRATEGY_HIDDEN").ToString() : $"{(char)('A' + i)}. {_snapshot.Question.Answers[i]}";
        }
        var next = GetNode<Button>("Continue");
        next.Visible = _transport.IsHost && _snapshot.Phase is "AnswerReveal" or "Scoreboard" or "RoundEnd";
        next.Text = Tr(_snapshot.Phase == "AnswerReveal" ? "MATCH_SHOW_SCORES" : "MATCH_CONTINUE");
        var key = _snapshot.Phase switch
        {
            "GameOver" => "MATCH_FINISHED", "Scoreboard" => "MATCH_SCORE_STATUS", "AnswerReveal" => "MATCH_REVEALED",
            "RoundEnd" => "MATCH_ROUND_END",
            "QuestionLocked" => "MATCH_LOCKED", _ => _transport.AnswerPending ? "MATCH_PENDING" :
                _transport.OwnAnswerIndex is not null ? "MATCH_ACCEPTED" : _reason is "None" or "Pending" ? "MATCH_CHOOSE" : "MATCH_ERROR_" + _reason
        };
        GetNode<Label>("Status").Text = Tr(key);
    }

    private void UpdateCountdown()
    {
        if (_snapshot is null || !Visible) return;
        var seconds = Math.Max(0, TimeSpan.FromTicks((_snapshot.Private?.DeadlineTicks ?? _snapshot.Question.DeadlineTicks) - _snapshot.HostNowTicks).TotalSeconds -
            (global::Godot.Time.GetTicksMsec() - _receivedAtMs) / 1000.0);
        GetNode<Label>("Countdown").Text = _snapshot.Phase == "QuestionActive"
            ? string.Format(Tr("MATCH_TIME"), (int)Math.Ceiling(seconds)) : "";
    }

    public override void _ExitTree()
    {
        if (_transport is null) return;
        _transport.MatchChanged -= Render;
        _transport.MatchInputChanged -= OnInputChanged;
        _transport.SnapshotChanged -= OnLobbyChanged;
        _transport.CardInputChanged -= OnCardInput;
    }
}

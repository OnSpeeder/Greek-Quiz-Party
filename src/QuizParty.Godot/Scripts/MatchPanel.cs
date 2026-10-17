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

    public override void _Ready()
    {
        for (var index = 0; index < 4; index++)
        {
            var choice = index;
            _answers[index] = GetNode<Button>($"Answer{index}");
            _answers[index].Pressed += () => _transport?.SubmitAnswer(choice);
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
    }

    private void OnInputChanged(string reason)
    {
        _reason = reason;
        UpdateControls();
    }

    private void Render(MatchSnapshotDto snapshot)
    {
        Visible = true;
        _snapshot = snapshot;
        _receivedAtMs = global::Godot.Time.GetTicksMsec();
        GetNode<Label>("Question").Text = snapshot.Question.Text;
        GetNode<Label>("Heading").Text = Tr(snapshot.Phase == "GameOver" ? "MATCH_FINAL" : "MATCH_TITLE");
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
            _answers[i].Disabled = !active || _transport.AnswerPending || _transport.OwnAnswerIndex is not null;
        }
        var next = GetNode<Button>("Continue");
        next.Visible = _transport.IsHost && _snapshot.Phase is "AnswerReveal" or "Scoreboard";
        next.Text = Tr(_snapshot.Phase == "AnswerReveal" ? "MATCH_SHOW_SCORES" : "MATCH_SHOW_FINAL");
        var key = _snapshot.Phase switch
        {
            "GameOver" => "MATCH_FINISHED", "Scoreboard" => "MATCH_SCORE_STATUS", "AnswerReveal" => "MATCH_REVEALED",
            "QuestionLocked" => "MATCH_LOCKED", _ => _transport.AnswerPending ? "MATCH_PENDING" :
                _transport.OwnAnswerIndex is not null ? "MATCH_ACCEPTED" : _reason is "None" or "Pending" ? "MATCH_CHOOSE" : "MATCH_ERROR_" + _reason
        };
        GetNode<Label>("Status").Text = Tr(key);
    }

    private void UpdateCountdown()
    {
        if (_snapshot is null || !Visible) return;
        var seconds = Math.Max(0, TimeSpan.FromTicks(_snapshot.Question.DeadlineTicks - _snapshot.HostNowTicks).TotalSeconds -
            (global::Godot.Time.GetTicksMsec() - _receivedAtMs) / 1000.0);
        GetNode<Label>("Countdown").Text = _snapshot.Phase == "QuestionActive"
            ? string.Format(Tr("MATCH_TIME"), (int)Math.Ceiling(seconds)) : "";
    }

    public override void _ExitTree()
    {
        if (_transport is null) return;
        _transport.MatchChanged -= Render;
        _transport.MatchInputChanged -= OnInputChanged;
    }
}

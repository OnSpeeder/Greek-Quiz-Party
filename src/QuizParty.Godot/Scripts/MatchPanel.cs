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
    private LocalControllerPanel _controllers = null!;
    private Label _teams = null!;
    private ProgressBar _timeBar = null!;
    private Label _winner = null!;
    private StandingsPanel _standings = null!;
    private Button _statisticsToggle = null!;
    private Button _newParty = null!;
    private bool _showStatistics;
    private ShowtimeStageView _stage = null!;

    public override void _Ready()
    {
        AddThemeConstantOverride("separation", 8);
        _stage = new ShowtimeStageView { Name = "ShowtimeStage", Visible = false };
        AddChild(_stage); MoveChild(_stage, 0);
        _progress = new Label { Name = "Progress", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_progress);
        MoveChild(_progress, 1);
        _winner = new Label { Name = "Winner", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _winner.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
        _winner.AddThemeFontSizeOverride("font_size", 32);
        AddChild(_winner); MoveChild(_winner, 2);
        _statistics = new Label { Name = "Statistics", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_statistics);
        _statisticsToggle = new Button { Name = "StatisticsToggle", Text = "UI_STATS_DETAILS", Flat = true };
        _statisticsToggle.Pressed += () => { _showStatistics = !_showStatistics; _statistics.Visible = _showStatistics; };
        AddChild(_statisticsToggle); MoveChild(_statisticsToggle, _statistics.GetIndex());
        _newParty = new Button { Name = "NewParty", Text = "UI_NEW_PARTY", ThemeTypeVariation = "PrimaryAction" };
        _newParty.Pressed += () =>
        {
            for (Node? node = GetParent(); node is not null; node = node.GetParent())
                if (node is LobbyScreen lobby) { lobby.ReturnHome(); return; }
        };
        AddChild(_newParty); MoveChild(_newParty, _statisticsToggle.GetIndex());
        _departures = new Label { Name = "Departures", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_departures);
        MoveChild(_departures, 2);
        _strategy = new StrategyPanel { Name = "Strategy" };
        AddChild(_strategy); MoveChild(_strategy, GetNode<GridContainer>("Answers").GetIndex());
        _controllers = new LocalControllerPanel { Name = "LocalControllers" };
        AddChild(_controllers); MoveChild(_controllers, _strategy.GetIndex());
        _teams = new Label { Name = "TeamScores", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_teams); MoveChild(_teams, GetNode<Label>("Scores").GetIndex());
        _standings = new StandingsPanel { Name = "Standings" };
        AddChild(_standings); MoveChild(_standings, GetNode<Label>("Scores").GetIndex());
        for (var index = 0; index < 4; index++)
        {
            var choice = index;
            _answers[index] = GetNode<Button>($"Answers/Answer{index}");
            _answers[index].ThemeTypeVariation = "Answer" + index;
            _answers[index].Icon = QuizShowTheme.AnswerBadge(index);
            _answers[index].CustomMinimumSize = new(0, 80);
            _answers[index].AddThemeFontSizeOverride("font_size", 26);
            _answers[index].Pressed += () => _transport?.SubmitAnswer(choice, confidence: _snapshot?.IsTieBreaker == true ? 1 : _strategy.Confidence);
        }
        GetNode<Button>("Continue").Pressed += () => _transport?.AdvanceMatch();
        GetNode<Button>("Continue").ThemeTypeVariation = "PrimaryAction";
        var timer = new global::Godot.Timer { WaitTime = 0.1, Autostart = true };
        timer.Timeout += UpdateCountdown;
        AddChild(timer);
        _timeBar = new ProgressBar { Name = "TimeBar", ShowPercentage = false, CustomMinimumSize = new(0, 12), MaxValue = 60 };
        AddChild(_timeBar); MoveChild(_timeBar, GetNode<Label>("Countdown").GetIndex() + 1);
        Resized += UpdateAnswerLayout;
        UpdateAnswerLayout();
        GetNode<Label>("Question").AddThemeStyleboxOverride("normal", ShowtimeTheme.Panel(new("211235"), ShowtimeTheme.Gold, 3));
        GetNode<Label>("Question").AddThemeFontSizeOverride("font_size", 30);
        GetNode<Label>("Question").HorizontalAlignment = HorizontalAlignment.Center;
        QuizShowTheme.StyleQuestion(GetNode<Label>("Question"));
        GetNode<Label>("Reveal").AddThemeStyleboxOverride("normal", QuizShowTheme.Card(QuizShowTheme.Plum, ShowtimeTheme.Cyan));
        // These explicit sizes are assigned after NodeAdded styling; register their
        // baselines so larger text applies both now and on later preference changes.
        foreach (var answer in _answers) QuizShowTheme.SetFontSize(answer, 26);
        QuizShowTheme.SetFontSize(GetNode<Label>("Question"), 30);
        var meta = new HBoxContainer { Name = "Meta" }; AddChild(meta); MoveChild(meta, 0);
        _progress.Reparent(meta); _progress.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        _progress.AddThemeColorOverride("font_color", ShowtimeTheme.Cyan);
        GetNode<Label>("Countdown").Reparent(meta);
        GetNode<Label>("Meta/Countdown").SetMeta("presentation_no_wrap", true);
        GetNode<Label>("Meta/Countdown").AutowrapMode = TextServer.AutowrapMode.Off;
        GetNode<Label>("Meta/Countdown").AddThemeStyleboxOverride("normal", ShowtimeTheme.Panel(new("291d35"), ShowtimeTheme.Gold));
        var clockStyle = (StyleBoxFlat)GetNode<Label>("Meta/Countdown").GetThemeStylebox("normal").Duplicate();
        clockStyle.ContentMarginTop = 4; clockStyle.ContentMarginBottom = 4;
        GetNode<Label>("Meta/Countdown").AddThemeStyleboxOverride("normal", clockStyle);
        GetNode<Label>("Meta/Countdown").AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
    }

    private void UpdateAnswerLayout()
    {
        var wide = Size.X >= 700;
        GetNode<GridContainer>("Answers").Columns = wide ? 2 : 1;
        _stage.Visible = wide && _transport?.IsHost == true && _snapshot?.Phase is "QuestionActive" or "QuestionLocked" or "AnswerReveal";
        // Keep confidence immediately before choices, but private cards after choices.
        if (_strategy is not null) _strategy.SetCompact(!wide);
    }

    public void Bind(LobbyTransport transport)
    {
        _transport = transport;
        transport.MatchChanged += Render;
        transport.MatchInputChanged += OnInputChanged;
        transport.SnapshotChanged += OnLobbyChanged;
        _strategy.Bind(transport);
        _controllers.Bind(transport); _controllers.Changed += OnControllerChanged;
        transport.CardInputChanged += OnCardInput;
    }
    private void OnCardInput(string reason)
    {
        UpdateControls();
        if (reason == "None") PresentationShell.For(this)?.PlayCue("card");
    }
    private void OnControllerChanged()
    { _reason = "None"; if (_transport?.MatchSnapshot is { } snapshot) Render(snapshot); }

    private void OnLobbyChanged(LobbySnapshotDto lobby)
    {
        if (_snapshot is null) return;
        var departed = _snapshot.Scores.Where(s => !lobby.Players.Any(p => p.PlayerId == s.PlayerId)).Select(s => s.DisplayName).ToArray();
        _departures.Text = departed.Length == 0 ? "" : string.Format(Tr("MATCH_DEPARTED"), string.Join(", ", departed));
        _departures.Visible = departed.Length > 0;
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
        var phaseChanged = _snapshot?.Phase != snapshot.Phase || _snapshot.Question.InstanceId != snapshot.Question.InstanceId;
        if (_snapshot?.Question.InstanceId != snapshot.Question.InstanceId) _reason = "None";
        _snapshot = snapshot;
        UpdateAnswerLayout();
        _stage.Render(snapshot.Scores, phaseChanged && snapshot.Phase == "AnswerReveal");
        _controllers.Refresh();
        _strategy.Render(snapshot);
        if (_transport?.Snapshot is { } lobby) OnLobbyChanged(lobby);
        _receivedAtMs = global::Godot.Time.GetTicksMsec();
        GetNode<Label>("Question").Text = snapshot.Question.Text;
        GetNode<Label>("Heading").Text = Tr(snapshot.Phase == "GameOver" ? "MATCH_FINAL" : "UI_QUESTION");
        GetNode<Label>("Heading").Visible = snapshot.Phase is not ("QuestionActive" or "QuestionLocked");
        _progress.Text = snapshot.IsTieBreaker ? Tr("MATCH_TIE") : string.Format(Tr("MATCH_PROGRESS"),
            snapshot.RoundNumber, snapshot.QuestionNumber, snapshot.TotalQuestions);
        var teamMode = snapshot.Teams is { Length: > 0 };
        var winnerNames = teamMode ? (snapshot.WinningTeams ?? []).Select(team => Tr("TEAM_" + team).ToString()) :
            snapshot.Scores.Where(s => snapshot.Winners.Contains(s.PlayerId)).Select(s => s.DisplayName);
        _teams.Text = snapshot.Reveal is null || !teamMode ? "" : string.Join("\n", snapshot.Teams!.Select(team =>
            string.Format(Tr("TEAM_SCORE"), Tr("TEAM_" + team.TeamId), team.Total, string.Join(", ",
                snapshot.Scores.Where(s => team.Members.Contains(s.PlayerId)).Select(s => s.DisplayName)))));
        _winner.Text = snapshot.Phase != "GameOver" ? "" :
            string.Format(Tr(teamMode ? snapshot.ContentExhausted ? "TEAM_SHARED" : "TEAM_WINNER" :
                snapshot.ContentExhausted ? "MATCH_SHARED" : "MATCH_WINNER"), string.Join(", ", winnerNames));
        _statistics.Text = snapshot.Phase != "GameOver" ? "" :
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
        for (var i = 0; i < 4; i++) _answers[i].Text = $"{Tr("UI_ANSWER_" + i)}   {snapshot.Question.Answers[i]}";
        GetNode<Label>("Reveal").Text = snapshot.Reveal is null ? "" :
            string.Format(Tr("MATCH_CORRECT"), snapshot.Question.Answers[snapshot.Reveal.CorrectAnswerIndex]) + "\n" + snapshot.Reveal.Explanation +
            (snapshot.Reveal.FunFacts is { Length: > 0 } ? "\n\n" + string.Join("\n", snapshot.Reveal.FunFacts.Select(f => "• " + f)) : "");
        GetNode<Label>("Scores").Text = snapshot.Reveal is null ? "" : Tr("MATCH_SCORES") + "\n" +
            string.Join("\n", snapshot.Scores.OrderByDescending(score => score.Total).Select(score =>
                string.Format(Tr("MATCH_PLAYER_SCORE"), score.DisplayName, score.Total)));
        UpdateControls();
        UpdateCountdown();
        foreach (var label in new[] { _winner, _statistics, _departures, _teams, GetNode<Label>("Reveal"), GetNode<Label>("Scores") })
            label.Visible = !string.IsNullOrWhiteSpace(label.Text);
        GetNode<Label>("Question").Visible = snapshot.Phase is "QuestionActive" or "QuestionLocked" or "AnswerReveal";
        GetNode<Label>("Reveal").Visible = snapshot.Phase == "AnswerReveal";
        GetNode<Label>("Scores").Visible = false;
        _standings.Visible = snapshot.Phase is "Scoreboard" or "RoundEnd" or "GameOver";
        if (_standings.Visible) _standings.Render(snapshot.Scores, snapshot.SessionId);
        _statistics.Visible = _showStatistics && snapshot.Phase == "GameOver";
        _statisticsToggle.Visible = snapshot.Phase == "GameOver";
        _newParty.Visible = snapshot.Phase == "GameOver";
        if (snapshot.Phase == "GameOver") GetNode<Label>("Status").Visible = false;
        if (phaseChanged && PresentationShell.For(this) is { } shell)
        {
            foreach (var answer in _answers) { shell.Juice.Finish(answer); answer.Scale = Vector2.One; answer.Modulate = Colors.White; }
            if (snapshot.Phase == "QuestionActive") shell.Juice.StaggerInControls(_answers);
            if (snapshot.Phase == "AnswerReveal" && snapshot.Reveal is { } reveal)
                shell.Juice.Reveal(_answers, reveal.CorrectAnswerIndex);
            // Only animate public text. Private panel hiding and answer input remain immediate.
            shell.Fade(snapshot.Phase == "GameOver" ? _winner : GetNode<Label>(snapshot.Reveal is null ? "Question" : "Reveal"));
            if (snapshot.Phase is "AnswerReveal" or "GameOver") shell.PlayCue(snapshot.Phase == "GameOver" ? "final" : "reveal");
            Callable.From(() =>
            {
                if (GodotObject.IsInstanceValid(this) && IsInsideTree() && IsVisibleInTree() &&
                    GetParent().GetParent() is ScrollContainer scroll) scroll.ScrollVertical = 0;
            }).CallDeferred();
        }
    }

    private void UpdateControls()
    {
        if (_snapshot is null || _transport is null) return;
        _controllers.Refresh();
        var active = _snapshot.Phase == "QuestionActive";
        _strategy.Visible = _controllers.Open && _snapshot.Strategy is not null && _snapshot.Phase is not ("GameOver" or "AnswerReveal");
        for (var i = 0; i < 4; i++)
        {
            _answers[i].Visible = _snapshot.Phase == "AnswerReveal" || (_controllers.Open || _transport.IsHost && _transport.OwnedPlayers.Count == 0) && _snapshot.Phase is "QuestionActive" or "QuestionLocked";
            _answers[i].Disabled = !active || !_snapshot.EligiblePlayers.Contains(_transport.LocalPlayerId ?? Guid.Empty) ||
                _transport.AnswerPending || _transport.CardPending || _transport.OwnAnswerIndex is not null ||
                _snapshot.Private?.HiddenAnswers.Contains(i) == true;
            _answers[i].Text = _snapshot.Private?.HiddenAnswers.Contains(i) == true && _snapshot.Reveal is null
                ? Tr("STRATEGY_HIDDEN").ToString() : $"{Tr("UI_ANSWER_" + i)}   {_snapshot.Question.Answers[i]}";
            if (_snapshot.Reveal?.CorrectAnswerIndex == i)
                _answers[i].Text = string.Format(Tr("UI_CORRECT_CHOICE"), _answers[i].Text);
            else if (_controllers.Open && _transport.OwnAnswerIndex == i)
                _answers[i].Text = string.Format(Tr("UI_CHOSEN"), _answers[i].Text);
            _answers[i].RemoveThemeStyleboxOverride("disabled");
            if (_snapshot.Reveal?.CorrectAnswerIndex == i)
                _answers[i].AddThemeStyleboxOverride("disabled", ShowtimeTheme.Panel(new("203e40"), ShowtimeTheme.Cyan, 3));
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
        GetNode<Label>("Status").Visible = _snapshot.Phase != "AnswerReveal" &&
            (!active || _transport.AnswerPending || _transport.OwnAnswerIndex is not null || _reason is not ("None" or "Pending"));
    }

    private void UpdateCountdown()
    {
        if (_snapshot is null || !Visible) return;
        var seconds = Math.Max(0, TimeSpan.FromTicks((_controllers.Open ? _snapshot.Private?.DeadlineTicks ?? _snapshot.Question.DeadlineTicks : _snapshot.Question.DeadlineTicks) - _snapshot.HostNowTicks).TotalSeconds -
            (global::Godot.Time.GetTicksMsec() - _receivedAtMs) / 1000.0);
        var active = _snapshot.Phase == "QuestionActive";
        GetNode<Label>("Meta/Countdown").Text = active
            ? string.Format(Tr(seconds <= 5 ? "UI_CLOCK_URGENT" : "UI_CLOCK"), (int)Math.Ceiling(seconds)) : "";
        GetNode<Label>("Meta/Countdown").AccessibilityName = string.Format(Tr("MATCH_TIME"), (int)Math.Ceiling(seconds));
        _timeBar.Visible = active;
        GetNode<Label>("Meta/Countdown").Visible = active;
        var deadline = _controllers.Open ? _snapshot.Private?.DeadlineTicks ?? _snapshot.Question.DeadlineTicks : _snapshot.Question.DeadlineTicks;
        _timeBar.MaxValue = Math.Max(1, TimeSpan.FromTicks(deadline - _snapshot.Question.StartedAtTicks).TotalSeconds);
        _timeBar.Value = Math.Max(0, seconds);
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

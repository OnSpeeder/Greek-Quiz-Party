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
    private BoxContainer _questionLayout = null!;
    private VBoxContainer _questionContent = null!;
    private VBoxContainer _hostRail = null!;
    private MatchDialog _revealDialog = null!;
    private MatchDialog _pauseDialog = null!;
    private MatchDialog _sourceDialog = null!;
    private GridContainer _voteActions = null!;
    private Button _replay = null!;
    private Guid _revealQuestion;
    private bool _revealReady;
    private ShowtimeStageView _stage = null!;
    private Texture2D _continueIcon = null!;
    private Texture2D _finishIcon = null!;
    internal Func<string, Error> SourceOpener { get; set; } = OS.ShellOpen;

    public override void _Ready()
    {
        AddThemeConstantOverride("separation", 6);
        _continueIcon = LobbyIcons.Texture("continue"); _finishIcon = LobbyIcons.Texture("finish");
        _revealDialog = new MatchDialog { Name = "RevealDialog" };
        var dialogs = new CanvasLayer { Name = "MatchDialogs", Layer = 20 }; AddChild(dialogs);
        dialogs.AddChild(_revealDialog);
        _pauseDialog = new MatchDialog { Name = "PauseDialog" }; dialogs.AddChild(_pauseDialog);
        _sourceDialog = new MatchDialog { Name = "SourceConfirmation" }; dialogs.AddChild(_sourceDialog);
        _sourceDialog.Body.AddChild(new Label { Name = "Prompt", Text = "MATCH_SOURCE_CONFIRM", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _sourceDialog.Body.AddChild(new Label { Name = "Url", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _sourceDialog.Body.AddChild(new Label { Name = "Error", Visible = false, AutowrapMode = TextServer.AutowrapMode.WordSmart });
        _sourceDialog.Actions.Columns = 2;
        var no = new Button { Name = "No", Text = "UI_NO", CustomMinimumSize = new(64, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
        var yes = new Button { Name = "Yes", Text = "UI_YES", CustomMinimumSize = new(64, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _sourceDialog.Actions.AddChild(no); _sourceDialog.Actions.AddChild(yes);
        no.FocusNext = no.FocusPrevious = no.GetPathTo(yes);
        yes.FocusNext = yes.FocusPrevious = yes.GetPathTo(no);
        no.Pressed += () => CloseSourceConfirmation();
        yes.Pressed += OpenSource;
        _voteActions = new GridContainer { Name = "VoteActions" }; AddChild(_voteActions);
        _replay = new Button { Name = "Replay", Text = "MATCH_REPLAY", ThemeTypeVariation = "PrimaryAction" };
        _replay.Pressed += () => _transport?.Replay(); AddChild(_replay);
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
        AddChild(_strategy); MoveChild(_strategy, Part<GridContainer>("Answers").GetIndex());
        _controllers = new LocalControllerPanel { Name = "LocalControllers" };
        AddChild(_controllers); MoveChild(_controllers, _strategy.GetIndex());
        _teams = new Label { Name = "TeamScores", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_teams); MoveChild(_teams, Part<Label>("Scores").GetIndex());
        _standings = new StandingsPanel { Name = "Standings" };
        AddChild(_standings); MoveChild(_standings, Part<Label>("Scores").GetIndex());
        for (var index = 0; index < 4; index++)
        {
            var choice = index;
            _answers[index] = Part<Button>($"Answers/Answer{index}");
            _answers[index].ThemeTypeVariation = "Answer" + index;
            _answers[index].Icon = QuizShowTheme.AnswerBadge(index);
            _answers[index].CustomMinimumSize = new(0, 80);
            _answers[index].AddThemeFontSizeOverride("font_size", 26);
            _answers[index].Pressed += () => _transport?.SubmitAnswer(choice, confidence: _snapshot?.IsTieBreaker == true ? 1 : _strategy.Confidence);
        }
        Part<Button>("Continue").Pressed += () => _transport?.ContinueMatch();
        Part<Button>("Continue").ThemeTypeVariation = "PrimaryAction";
        var timer = new global::Godot.Timer { WaitTime = 0.1, Autostart = true };
        timer.Timeout += UpdateCountdown;
        AddChild(timer);
        _timeBar = new ProgressBar { Name = "TimeBar", ShowPercentage = false, CustomMinimumSize = new(0, 12), MaxValue = 60 };
        AddChild(_timeBar); MoveChild(_timeBar, Part<Label>("Countdown").GetIndex() + 1);
        Resized += UpdateAnswerLayout;
        Resized += QueueHostFit;
        UpdateAnswerLayout();
        Part<Label>("Question").AddThemeStyleboxOverride("normal", ShowtimeTheme.Panel(new("211235"), ShowtimeTheme.Gold, 3));
        Part<Label>("Question").AddThemeFontSizeOverride("font_size", 30);
        Part<Label>("Question").HorizontalAlignment = HorizontalAlignment.Center;
        QuizShowTheme.StyleQuestion(Part<Label>("Question"));
        Part<Label>("Reveal").AddThemeStyleboxOverride("normal", QuizShowTheme.Card(QuizShowTheme.Plum, ShowtimeTheme.Cyan));
        // These explicit sizes are assigned after NodeAdded styling; register their
        // baselines so larger text applies both now and on later preference changes.
        foreach (var answer in _answers) QuizShowTheme.SetFontSize(answer, 26);
        QuizShowTheme.SetFontSize(Part<Label>("Question"), 30);
        var meta = new HBoxContainer { Name = "Meta" }; AddChild(meta); MoveChild(meta, 0);
        _progress.Reparent(meta); _progress.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        _progress.AddThemeColorOverride("font_color", ShowtimeTheme.Cyan);
        Part<Label>("Countdown").Reparent(meta);
        Part<Label>("Meta/Countdown").SetMeta("presentation_no_wrap", true);
        Part<Label>("Meta/Countdown").AutowrapMode = TextServer.AutowrapMode.Off;
        Part<Label>("Meta/Countdown").AddThemeStyleboxOverride("normal", ShowtimeTheme.Panel(new("291d35"), ShowtimeTheme.Gold));
        var clockStyle = (StyleBoxFlat)Part<Label>("Meta/Countdown").GetThemeStylebox("normal").Duplicate();
        clockStyle.ContentMarginTop = 4; clockStyle.ContentMarginBottom = 4;
        Part<Label>("Meta/Countdown").AddThemeStyleboxOverride("normal", clockStyle);
        Part<Label>("Meta/Countdown").AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
        ComposeQuestion();
    }

    private T Part<T>(string path) where T : Node => GetNodeOrNull<T>(path) ?? GetNode<T>("QuestionLayout/QuestionContent/" + path);
    private void ComposeQuestion()
    {
        _questionLayout = new BoxContainer { Name = "QuestionLayout", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _questionLayout.AddThemeConstantOverride("separation", 16); AddChild(_questionLayout); MoveChild(_questionLayout, 1);
        _questionContent = new VBoxContainer { Name = "QuestionContent", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _questionContent.AddThemeConstantOverride("separation", 8); _questionLayout.AddChild(_questionContent);
        _hostRail = new VBoxContainer { Name = "HostRail" }; _questionLayout.AddChild(_hostRail);
        foreach (var name in new[] { "Meta", "Question", "TimeBar", "Strategy", "Answers", "Status" }) GetNode(name).Reparent(_questionContent);
        _stage.Reparent(_hostRail); _controllers.Reparent(_hostRail);
        UpdateAnswerLayout();
    }
    private void UpdateAnswerLayout()
    {
        var wide = Size.X >= 700;
        var host = _transport?.IsHost == true;
        if (_progress is not null) QuizShowTheme.SetFontSize(_progress, wide ? 22 : 16);
        if (_questionLayout is not null)
        {
            _questionLayout.Visible = _snapshot is not null && _snapshot.Phase != "GameOver";
            _questionLayout.Vertical = !wide || !host;
            _hostRail.CustomMinimumSize = new(wide && host ? 210 : 0, 0);
            _hostRail.SizeFlagsHorizontal = wide && host ? SizeFlags.Fill : SizeFlags.ExpandFill;
            _stage.Columns = wide ? 2 : 4;
            _controllers.SetCompact(host, wide);
        }
        Part<GridContainer>("Answers").Columns = wide || host ? 2 : 1;
        _stage.Visible = _transport?.IsHost == true && _transport.OwnedPlayers.Count <= 1 && _snapshot?.Phase is "QuestionActive" or "QuestionLocked" or "AnswerReveal";
        // Keep confidence immediately before choices, but private cards after choices.
        if (_strategy is not null) _strategy.SetCompact(true);
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
        var disconnected = _snapshot.Scores.Where(s => _snapshot.DisconnectedPlayers?.Contains(s.PlayerId) == true &&
            lobby.Players.Any(p => p.PlayerId == s.PlayerId)).Select(s => s.DisplayName).ToArray();
        var messages = new List<string>();
        if (disconnected.Length > 0) messages.Add(string.Format(Tr("MATCH_DISCONNECTED_PLAYERS"), string.Join(", ", disconnected)));
        if (departed.Length > 0) messages.Add(string.Format(Tr("MATCH_DEPARTED"), string.Join(", ", departed)));
        _departures.Text = string.Join("\n", messages);
        _departures.Visible = messages.Count > 0;
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
        if (GetParent() is VBoxContainer content && content.GetParent() is ScrollContainer scroll)
        {
            // Keep a scrolling fallback for content that cannot fit at a readable size.
            scroll.VerticalScrollMode = ScrollContainer.ScrollMode.ShowNever;
            if (_snapshot?.Phase != snapshot.Phase || _snapshot.Question.InstanceId != snapshot.Question.InstanceId)
                scroll.ScrollVertical = 0;
            content.SizeFlagsVertical = SizeFlags.ExpandFill;
            foreach (var sibling in content.GetChildren().OfType<Control>().Where(c => c != this)) sibling.Hide();
        }
        var phaseChanged = _snapshot?.Phase != snapshot.Phase || _snapshot.Question.InstanceId != snapshot.Question.InstanceId;
        if (_snapshot?.Question.InstanceId != snapshot.Question.InstanceId)
        {
            _reason = "None";
            QuizShowTheme.SetFontSize(Part<Label>("Question"), 30);
            foreach (var answer in _answers) QuizShowTheme.SetFontSize(answer, 26);
        }
        _snapshot = snapshot;
        if (snapshot.Phase != "QuestionActive") PresentationShell.For(this)?.SetMusicPhase(snapshot.Phase);
        _standings.Observe(snapshot);
        UpdateAnswerLayout();
        _stage.Render(snapshot.Scores, phaseChanged && snapshot.Phase == "AnswerReveal", snapshot.AnsweredPlayers);
        _controllers.Refresh();
        _strategy.Render(snapshot);
        if (_transport?.Snapshot is { } lobby) OnLobbyChanged(lobby);
        _receivedAtMs = global::Godot.Time.GetTicksMsec();
        Part<Label>("Question").Text = snapshot.Question.Text;
        Part<Label>("Heading").Text = Tr(snapshot.Phase == "GameOver" ? "MATCH_FINAL" : snapshot.Phase is "Scoreboard" or "RoundEnd" ? "MATCH_SCORES" : "UI_QUESTION");
        Part<Label>("Heading").Visible = snapshot.Phase is "GameOver" or "Scoreboard" or "RoundEnd";
        _progress.Text = snapshot.IsTieBreaker ? Tr("MATCH_TIE") : string.Format(Tr("MATCH_PROGRESS"),
            snapshot.RoundNumber, snapshot.QuestionNumber, snapshot.TotalQuestions == 0 ? "∞" : snapshot.TotalQuestions.ToString());
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
        Part<Label>("Reveal").Text = snapshot.Reveal is null ? "" :
            string.Format(Tr("MATCH_CORRECT"), snapshot.Question.Answers[snapshot.Reveal.CorrectAnswerIndex]) + "\n" + snapshot.Reveal.Explanation +
            (snapshot.Reveal.FunFacts is { Length: > 0 } ? "\n\n" + string.Join("\n", snapshot.Reveal.FunFacts.Select(f => "• " + f)) : "");
        Part<Label>("Scores").Text = snapshot.Reveal is null ? "" : Tr("MATCH_SCORES") + "\n" +
            string.Join("\n", snapshot.Scores.OrderByDescending(score => score.Total).Select(score =>
                string.Format(Tr("MATCH_PLAYER_SCORE"), score.DisplayName, score.Total)));
        UpdateControls();
        UpdateCountdown();
        QueueHostFit();
        foreach (var label in new[] { _winner, _statistics, _departures, _teams, Part<Label>("Reveal"), Part<Label>("Scores") })
            label.Visible = !string.IsNullOrWhiteSpace(label.Text);
        Part<Label>("Question").Visible = snapshot.Phase is "QuestionActive" or "QuestionLocked" or "AnswerReveal";
        Part<Label>("Reveal").Visible = false;
        UpdateRevealDialog(phaseChanged);
        UpdatePauseDialog();
        Part<Label>("Scores").Visible = false;
        _standings.Visible = snapshot.Phase is "Scoreboard" or "RoundEnd" or "GameOver";
        if (_standings.Visible) _standings.Render(snapshot);
        _statistics.Visible = _showStatistics && snapshot.Phase == "GameOver";
        _statisticsToggle.Visible = snapshot.Phase == "GameOver";
        _newParty.Visible = snapshot.Phase == "GameOver";
        MoveChild(_voteActions, GetChildCount() - 1);
        MoveChild(_replay, GetChildCount() - 1); MoveChild(_newParty, GetChildCount() - 1);
        _replay.Visible = snapshot.Phase == "GameOver" && _transport?.IsHost == true;
        if (snapshot.Phase == "GameOver") Part<Label>("Status").Visible = false;
        if (phaseChanged && PresentationShell.For(this) is { } shell)
        {
            foreach (var answer in _answers) { shell.Juice.Finish(answer); answer.Scale = Vector2.One; answer.Modulate = Colors.White; }
            if (snapshot.Phase == "QuestionActive") shell.Juice.StaggerInControls(_answers);
            if (snapshot.Phase == "AnswerReveal" && snapshot.Reveal is { } reveal)
                shell.Juice.Reveal(_answers, reveal.CorrectAnswerIndex);
            // Only animate public text. Private panel hiding and answer input remain immediate.
            shell.Fade(snapshot.Phase == "GameOver" ? _winner : Part<Label>(snapshot.Reveal is null ? "Question" : "Reveal"));
            if (snapshot.Phase is "AnswerReveal" or "Scoreboard" or "GameOver")
                shell.PlayCue(snapshot.Phase == "GameOver" ? "final" : snapshot.Phase == "Scoreboard" ? "score" : "reveal");
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
        var active = _snapshot.Phase == "QuestionActive" && !_snapshot.IsPaused;
        _strategy.Visible = _controllers.Open && _snapshot.Strategy is not null && _snapshot.Phase is not ("GameOver" or "AnswerReveal");
        for (var i = 0; i < 4; i++)
        {
            _answers[i].Visible = _snapshot.Phase == "AnswerReveal" || (_controllers.Open || _transport.IsHost && _transport.OwnedPlayers.Count == 0) && _snapshot.Phase is "QuestionActive" or "QuestionLocked";
            _answers[i].Disabled = !active || !_snapshot.EligiblePlayers.Contains(_transport.LocalPlayerId ?? Guid.Empty) ||
                _transport.AnswerPending || _transport.CardPending || _transport.OwnAnswerIndex is not null ||
                _snapshot.AnsweredPlayers?.Contains(_transport.LocalPlayerId ?? Guid.Empty) == true ||
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
        var next = Part<Button>("Continue");
        next.Visible = false;
        RenderVotes(_voteActions, false);
        next.Text = Tr("MATCH_CONTINUE");
        var key = _snapshot.Phase switch
        {
            "GameOver" => "MATCH_FINISHED", "Scoreboard" => "MATCH_SCORE_STATUS", "AnswerReveal" => "MATCH_REVEALED",
            "RoundEnd" => "MATCH_ROUND_END",
            "QuestionLocked" => "MATCH_LOCKED", _ => _transport.AnswerPending ? "MATCH_PENDING" :
                _transport.OwnAnswerIndex is not null || _snapshot.AnsweredPlayers?.Contains(_transport.LocalPlayerId ?? Guid.Empty) == true ? "MATCH_ACCEPTED" : _reason is "None" or "Pending" ? "MATCH_CHOOSE" : "MATCH_ERROR_" + _reason
        };
        Part<Label>("Status").Text = Tr(key);
        Part<Label>("Status").Visible = _snapshot.Phase is not ("AnswerReveal" or "Scoreboard" or "RoundEnd") &&
            (!active || _transport.AnswerPending || _transport.OwnAnswerIndex is not null || _snapshot.AnsweredPlayers?.Contains(_transport.LocalPlayerId ?? Guid.Empty) == true || _reason is not ("None" or "Pending"));
    }

    private void UpdateCountdown()
    {
        if (_snapshot is null || !Visible) return;
        var elapsed = (global::Godot.Time.GetTicksMsec() - _receivedAtMs) / 1000.0;
        var seconds = Math.Max(0, TimeSpan.FromTicks((_controllers.Open ? _snapshot.Private?.DeadlineTicks ?? _snapshot.Question.DeadlineTicks : _snapshot.Question.DeadlineTicks) - _snapshot.HostNowTicks).TotalSeconds -
            (_snapshot.IsPaused ? 0 : elapsed));
        if (_snapshot.IsPaused && _snapshot.IsResuming && _pauseDialog.Body.GetNodeOrNull<Label>("Message") is { } countdown)
            countdown.Text = string.Format(Tr("MATCH_RESUME_COUNTDOWN"), Math.Max(1, (int)Math.Ceiling(TimeSpan.FromTicks(_snapshot.ResumeRemainingTicks).TotalSeconds - elapsed)));
        var active = _snapshot.Phase == "QuestionActive";
        var untimed = _snapshot.Question.DeadlineTicks == long.MaxValue;
        if (active) PresentationShell.For(this)?.SetMusicPhase(PartyMusic.QuestionPhase(untimed, _snapshot.IsPaused, seconds));
        Part<Label>("Meta/Countdown").Text = active
            ? untimed ? Tr("SETUP_UNTIMED").ToString() : string.Format(Tr(seconds <= 5 ? "UI_CLOCK_URGENT" : "UI_CLOCK"), (int)Math.Ceiling(seconds)) : "";
        Part<Label>("Meta/Countdown").AccessibilityName = untimed ? Tr("SETUP_UNTIMED").ToString() : string.Format(Tr("MATCH_TIME"), (int)Math.Ceiling(seconds));
        _timeBar.Visible = active && !untimed && _transport?.IsHost != true;
        Part<Label>("Meta/Countdown").Visible = active;
        var deadline = _controllers.Open ? _snapshot.Private?.DeadlineTicks ?? _snapshot.Question.DeadlineTicks : _snapshot.Question.DeadlineTicks;
        _timeBar.MaxValue = untimed ? 1 : Math.Max(1, TimeSpan.FromTicks(deadline - _snapshot.Question.StartedAtTicks).TotalSeconds);
        _timeBar.Value = untimed ? 0 : Math.Max(0, seconds);
    }

    private bool _fitQueued;
    private bool _fitReset = true;
    private Vector2 _fitViewport;
    public void RefreshQuestionFit()
    {
        _fitReset = true;
        QueueHostFit();
    }
    private void QueueHostFit()
    {
        if (_fitQueued || !IsInsideTree()) return;
        _fitQueued = true;
        Callable.From(FitHostQuestion).CallDeferred();
    }
    private void FitHostQuestion()
    {
        _fitQueued = false;
        if (_snapshot?.Phase is not ("QuestionActive" or "QuestionLocked" or "AnswerReveal") ||
            GetParent()?.GetParent() is not ScrollContainer scroll) return;
        var preferences = PresentationShell.For(this)?.Preferences;
        var large = preferences?.LargeText == true;
        var question = Part<Label>("Question");
        if (_fitReset || !_fitViewport.IsEqualApprox(scroll.Size))
        {
            _fitReset = false; _fitViewport = scroll.Size;
            QuizShowTheme.SetFontSize(question, 30);
            foreach (var answer in _answers) QuizShowTheme.SetFontSize(answer, 26);
            if (preferences?.AutoFitQuestions == false) return;
            QueueHostFit();
            return;
        }
        if (preferences?.AutoFitQuestions == false) return;
        var overflow = GetCombinedMinimumSize().Y > scroll.Size.Y + 1;
        if (!overflow) return;
        var changed = false;
        foreach (var control in _answers.Cast<Control>().Append(question))
        {
            var current = control.GetThemeFontSize("font_size");
            var minimum = large ? 22 : 18;
            if (current <= minimum) continue;
            control.AddThemeFontSizeOverride("font_size", current - 1); changed = true;
        }
        if (changed) QueueHostFit();
    }
    private void UpdateRevealDialog(bool phaseChanged)
    {
        if (_snapshot is not { Phase: "AnswerReveal" } snapshot)
        { _revealDialog.Hide(); _sourceDialog.Hide(); _revealReady = false; return; }
        if (_revealQuestion != snapshot.Question.InstanceId || phaseChanged)
        {
            _revealQuestion = snapshot.Question.InstanceId; _revealReady = false;
            _revealDialog.ClearBody();
            var question = _revealQuestion;
            GetTree().CreateTimer(1.2).Timeout += () =>
            {
                if (!GodotObject.IsInstanceValid(this) || !IsInsideTree() || _snapshot?.Phase != "AnswerReveal" || _snapshot.Question.InstanceId != question) return;
                _revealReady = true; ShowReveal();
            };
        }
        else if (_revealReady && !_sourceDialog.Visible) ShowReveal();
    }
    private void UpdatePauseDialog()
    {
        if (_snapshot is not { IsPaused: true } snapshot || _transport is null) { _pauseDialog.Hide(); return; }
        _sourceDialog.Hide();
        _pauseDialog.Actions.Columns = _transport.IsHost || _transport.OwnedPlayers.Count <= 1 ? 1 : 2;
        var context = $"{snapshot.PauseId}:{snapshot.IsResuming}";
        if (!_pauseDialog.HasMeta("pause_context") || _pauseDialog.GetMeta("pause_context").AsString() != context)
        {
            _pauseDialog.Clear(); _pauseDialog.SetMeta("pause_context", context);
            _pauseDialog.Body.AddChild(new Label { Name = "Message", AutowrapMode = TextServer.AutowrapMode.WordSmart });
            if (!snapshot.IsResuming)
            {
                if (_transport.IsHost)
                {
                    var button = new Button { Name = "HostResume", Text = "MATCH_RESUME_HOST", ThemeTypeVariation = "PrimaryAction", CustomMinimumSize = new(0, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
                    button.Pressed += () => _transport.ContinuePaused(); _pauseDialog.Actions.AddChild(button);
                }
                else foreach (var player in _transport.OwnedPlayers)
                {
                    var slot = player.LocalSlot;
                    var button = new Button { Name = "Resume" + slot, Text = _transport.OwnedPlayers.Count > 1 ? player.DisplayName + " · " + Tr("MATCH_CONTINUE") : Tr("MATCH_CONTINUE").ToString(),
                        ThemeTypeVariation = "PrimaryAction", CustomMinimumSize = new(0, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
                    button.Pressed += () => _transport.ContinuePaused(slot); _pauseDialog.Actions.AddChild(button);
                }
            }
        }
        var message = _pauseDialog.Body.GetNode<Label>("Message");
        var names = snapshot.Scores.Where(p => snapshot.DisconnectedPlayers?.Contains(p.PlayerId) == true).Select(p => p.DisplayName);
        message.Text = snapshot.IsResuming ? string.Format(Tr("MATCH_RESUME_COUNTDOWN"), 5) : string.Format(Tr("MATCH_PAUSED_DISCONNECTED"), string.Join(", ", names));
        if (!snapshot.IsResuming && !_transport.IsHost)
            foreach (var player in _transport.OwnedPlayers)
                if (_pauseDialog.Actions.GetNodeOrNull<Button>("Resume" + player.LocalSlot) is { } button)
                    button.Disabled = snapshot.ResumeVotes?.Contains(player.PlayerId) == true;
        _pauseDialog.Show(); _pauseDialog.MoveToFront();
    }
    private void ShowReveal()
    {
        if (_revealDialog.Body.GetChildCount() == 0 && _snapshot?.Reveal is { } reveal)
        {
            var answer = new Label { Name = "CorrectAnswer", Text = string.Format(Tr("MATCH_CORRECT"), _snapshot.Question.Answers[reveal.CorrectAnswerIndex]),
                AutowrapMode = TextServer.AutowrapMode.WordSmart };
            answer.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
            QuizShowTheme.SetFontSize(answer, 26); _revealDialog.Body.AddChild(answer);
            if (!string.IsNullOrWhiteSpace(reveal.Explanation))
            {
                var explanation = new Label { Name = "Explanation", Text = reveal.Explanation, AutowrapMode = TextServer.AutowrapMode.WordSmart };
                QuizShowTheme.SetFontSize(explanation, 24); _revealDialog.Body.AddChild(explanation);
            }
            if (QuizParty.Core.Questions.QuestionSource.IsValid(reveal.Source))
            {
                var source = new Button { Name = "Source", Icon = LobbyIcons.Texture("link"), ExpandIcon = true,
                    IconAlignment = HorizontalAlignment.Center, CustomMinimumSize = new(64, 64), SizeFlagsHorizontal = SizeFlags.ShrinkEnd,
                    TooltipText = Tr("MATCH_SOURCE"), AccessibilityName = Tr("MATCH_SOURCE") };
                source.AddThemeConstantOverride("icon_max_width", 28);
                source.Pressed += ShowSourceConfirmation; _revealDialog.Body.AddChild(source);
            }
            if (reveal.FunFacts is { Length: > 0 })
            {
                var heading = new Label { Name = "FunFactsHeading", Text = "MATCH_FUN_FACTS", AutowrapMode = TextServer.AutowrapMode.WordSmart };
                heading.AddThemeColorOverride("font_color", ShowtimeTheme.Cyan);
                QuizShowTheme.SetFontSize(heading, 25); _revealDialog.Body.AddChild(heading);
                var facts = new Label { Name = "FunFacts", Text = string.Join("\n", reveal.FunFacts.Select(f => "• " + f)),
                    AutowrapMode = TextServer.AutowrapMode.WordSmart };
                QuizShowTheme.SetFontSize(facts, 22); _revealDialog.Body.AddChild(facts);
            }
        }
        RenderVotes(_revealDialog.Actions, true);
        _revealDialog.Show();
        _revealDialog.MoveToFront();
    }
    private void ShowSourceConfirmation()
    {
        if (_snapshot is not { Phase: "AnswerReveal", IsPaused: false, Reveal: { } reveal } ||
            !QuizParty.Core.Questions.QuestionSource.IsValid(reveal.Source)) return;
        _revealDialog.Hide();
        _sourceDialog.Body.GetNode<Label>("Error").Hide();
        _sourceDialog.Body.GetNode<Label>("Url").Text = reveal.Source;
        _sourceDialog.Show(); _sourceDialog.MoveToFront();
        _sourceDialog.Actions.GetNode<Button>("No").GrabFocus();
    }

    public bool CloseSourceConfirmation()
    {
        if (!_sourceDialog.Visible) return false;
        _sourceDialog.Hide();
        if (_snapshot is { Phase: "AnswerReveal", IsPaused: false })
        {
            ShowReveal();
            _revealDialog.Body.GetNodeOrNull<Button>("Source")?.GrabFocus();
        }
        return true;
    }

    private void OpenSource()
    {
        if (_snapshot is not { Phase: "AnswerReveal", IsPaused: false, Reveal: { } reveal } ||
            !QuizParty.Core.Questions.QuestionSource.IsValid(reveal.Source)) { CloseSourceConfirmation(); return; }
        var error = SourceOpener(reveal.Source!);
        if (error == Error.Ok) CloseSourceConfirmation();
        else { var label = _sourceDialog.Body.GetNode<Label>("Error"); label.Text = "MATCH_SOURCE_ERROR"; label.Show(); }
    }

    private void RenderVotes(GridContainer container, bool reveal)
    {
        if (_snapshot is null || _transport is null) return;
        var visible = reveal ? _revealReady && _snapshot.Phase == "AnswerReveal" : _snapshot.Phase is "Scoreboard" or "RoundEnd";
        container.Visible = visible;
        container.Columns = _transport.IsHost || _transport.OwnedPlayers.Count <= 1 ? 1 : GetViewportRect().Size.X > 700 ? 4 : 2;
        if (!visible) { ClearActions(); return; }
        var context = $"{_snapshot.Question.InstanceId}:{_snapshot.Phase}:{_transport.IsHost}:{string.Join(',', _transport.OwnedPlayers.Select(p => p.LocalSlot))}";
        if (!container.HasMeta("vote_context") || container.GetMeta("vote_context").AsString() != context)
        { ClearActions(); container.SetMeta("vote_context", context); }
        var used = new HashSet<Node>();
        void ActionButton(string text, bool end, int? slot, bool disabled)
        {
            var name = $"Vote_{slot?.ToString() ?? "host"}_{end}";
            var button = container.GetNodeOrNull<Button>(name);
            if (button is null)
            {
                button = new Button { Name = name, ThemeTypeVariation = end ? "" : "PrimaryAction",
                    CustomMinimumSize = new(64, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
                button.Pressed += () => _transport.ContinueMatch(end, slot); container.AddChild(button);
            }
            button.Text = text; button.Disabled = disabled; used.Add(button);
        }
        if (_transport.IsHost)
        {
            ActionButton(Tr("MATCH_CONTINUE"), false, null, false);
            if (!reveal && _snapshot.TotalQuestions == 0 && _snapshot.Phase == "Scoreboard") ActionButton(Tr("MATCH_END_GAME"), true, null, false);
        }
        else
        {
            foreach (var player in _transport.OwnedPlayers)
            {
                ActionButton((_transport.OwnedPlayers.Count > 1 ? player.DisplayName + " · " : "") + Tr("MATCH_CONTINUE"), false, player.LocalSlot,
                    _snapshot.ContinueVotes?.Contains(player.PlayerId) == true);
                if (!reveal && _snapshot.TotalQuestions == 0 && _snapshot.Phase == "Scoreboard")
                    ActionButton(player.DisplayName + " · " + Tr("MATCH_END_GAME"), true, player.LocalSlot, _snapshot.EndVotes?.Contains(player.PlayerId) == true);
            }
        }
        var counts = container.GetNodeOrNull<HBoxContainer>("VoteCounts");
        if (counts is null) { counts = new HBoxContainer { Name = "VoteCounts", SizeFlagsHorizontal = SizeFlags.ExpandFill }; container.AddChild(counts); }
        used.Add(counts);
        var eligibleCount = _transport.Snapshot?.Players.Count(p => _snapshot.DisconnectedPlayers?.Contains(p.PlayerId) != true)
            ?? _snapshot.Scores.Count(p => _snapshot.DisconnectedPlayers?.Contains(p.PlayerId) != true);
        UpdateCount("ContinueCount", _continueIcon, "MATCH_VOTES", _snapshot.ContinueVotes?.Length ?? 0, eligibleCount);
        if (!reveal && _snapshot.TotalQuestions == 0 && _snapshot.Phase == "Scoreboard")
            UpdateCount("EndCount", _finishIcon, "MATCH_END_VOTES", _snapshot.EndVotes?.Length ?? 0, eligibleCount);
        if (counts.GetNodeOrNull<Control>("EndCount") is { } endCount) endCount.Visible = !reveal && _snapshot.TotalQuestions == 0 && _snapshot.Phase == "Scoreboard";
        foreach (var child in container.GetChildren().Where(c => !used.Contains(c))) { container.RemoveChild(child); child.QueueFree(); }
        void UpdateCount(string name, Texture2D icon, string key, int count, int total)
        {
            var row = counts.GetNodeOrNull<HBoxContainer>(name);
            if (row is null)
            {
                row = new HBoxContainer { Name = name, SizeFlagsHorizontal = SizeFlags.ExpandFill };
                row.AddChild(new TextureRect { Texture = icon, CustomMinimumSize = new(28, 28), ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
                    StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered, MouseFilter = MouseFilterEnum.Ignore });
                var label = new Label { Name = "Count", AutowrapMode = TextServer.AutowrapMode.Off };
                label.SetMeta("presentation_no_wrap", true); row.AddChild(label); counts.AddChild(row);
            }
            var text = string.Format(Tr(key), count, total);
            row.GetNode<Label>("Count").Text = $"{count}/{total}";
            row.TooltipText = text; row.AccessibilityName = text; row.Visible = true;
        }
        void ClearActions()
        {
            foreach (var child in container.GetChildren()) { container.RemoveChild(child); child.QueueFree(); }
            container.RemoveMeta("vote_context");
        }
    }

    public override void _ExitTree()
    {
        if (GodotObject.IsInstanceValid(_revealDialog)) _revealDialog.QueueFree();
        if (_transport is null) return;
        _transport.MatchChanged -= Render;
        _transport.MatchInputChanged -= OnInputChanged;
        _transport.SnapshotChanged -= OnLobbyChanged;
        _transport.CardInputChanged -= OnCardInput;
    }
}

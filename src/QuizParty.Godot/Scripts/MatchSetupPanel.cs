using Godot;
using QuizParty.Core.Game;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Scene-owned host configuration; Core receives a validated immutable copy at start.</summary>
public partial class MatchSetupPanel : PanelContainer
{
    private LobbyTransport _transport = null!;
    private VBoxContainer _body = null!;
    private Label _title = null!;
    private Label _capacity = null!;
    private GridContainer _grid = null!;
    private GridContainer? _links;
    private ScrollContainer _scroll = null!;
    private Button _back = null!;
    private string _page = "setup";
    public string CurrentPage => _page;
    public event Action? Closed;
    public override void _Ready()
    {
        SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
        AddThemeStyleboxOverride("panel", QuizShowTheme.Card(QuizShowTheme.Navy, QuizShowTheme.Gold));
        var layout = new VBoxContainer(); AddChild(layout);
        _title = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart };
        QuizShowTheme.SetFontSize(_title, 27); layout.AddChild(_title);
        _scroll = new ScrollContainer { Name = "PageScroll", SizeFlagsVertical = SizeFlags.ExpandFill,
            HorizontalScrollMode = ScrollContainer.ScrollMode.Disabled };
        layout.AddChild(_scroll); _scroll.AddChild(new PageDragScroll());
        _body = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _scroll.AddChild(_body);
        _body.AddThemeConstantOverride("separation", 8);
        _back = new Button { Name = "Done", Text = "SETUP_DONE", CustomMinimumSize = new(64, 64) };
        _back.Pressed += () => Back(); layout.AddChild(_back);
        Resized += Reflow;
    }
    public void Bind(LobbyTransport transport) => _transport = transport;
    public void Open(string page = "setup")
    {
        if (page != "rules" && !_transport.IsHost) return;
        Show(); ShowPage(page);
    }
    public bool Back()
    {
        if (!Visible) return false;
        if (_page is "categories" or "cards" or "missions") ShowPage("setup");
        else { Hide(); Closed?.Invoke(); }
        return true;
    }
    public void Dismiss() { Hide(); Closed?.Invoke(); }
    private Button Button(string name, string key, Action action, string? icon = null)
    {
        var button = new Button { Name = name, Text = key, SizeFlagsHorizontal = SizeFlags.ExpandFill,
            CustomMinimumSize = new(64, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart,
            Icon = icon is null ? null : LobbyIcons.Texture(icon), ExpandIcon = true };
        button.AddThemeConstantOverride("icon_max_width", 36);
        button.Pressed += action; return button;
    }
    private void Heading(string key)
    {
        var label = new Label { Text = key, AutowrapMode = TextServer.AutowrapMode.WordSmart };
        QuizShowTheme.SetFontSize(label, 19); _body.AddChild(label);
    }
    private static void IconHeading(Container parent, string key, string icon)
    {
        var heading = new HBoxContainer(); parent.AddChild(heading);
        heading.AddChild(new TextureRect { Texture = LobbyIcons.Texture(icon), CustomMinimumSize = new(28, 28),
            ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize, StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered,
            MouseFilter = MouseFilterEnum.Ignore });
        heading.AddChild(new Label { Text = key, AutowrapMode = TextServer.AutowrapMode.WordSmart });
    }
    private void Choices(string key, (int Value, string Text)[] options, int selected, Action<int> change, string icon)
    {
        var section = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _grid!.AddChild(section);
        IconHeading(section, key, icon);
        var row = new GridContainer { Columns = options.Length > 5 ? 4 : 3 }; section.AddChild(row);
        var group = new ButtonGroup();
        foreach (var (value, text) in options)
        {
            var button = Button("Value" + value, text, () => change(value));
            button.ToggleMode = true; button.ButtonGroup = group; button.SetPressedNoSignal(value == selected);
            QuizShowTheme.SetFontSize(button, 19); row.AddChild(button);
        }
    }
    public void ShowPage(string page)
    {
        _page = page;
        foreach (var child in _body.GetChildren()) { _body.RemoveChild(child); child.QueueFree(); }
        _title.Text = "SETUP_" + page.ToUpperInvariant();
        _back.Text = page is "setup" or "rules" ? "SETUP_DONE" : "SPIKE_BACK";
        _scroll.ScrollVertical = 0;
        _grid = new GridContainer { Name = "Options", Columns = 1, SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _grid.AddThemeConstantOverride("h_separation", 12); _grid.AddThemeConstantOverride("v_separation", 8);
        if (page == "setup") BuildSetup();
        else if (page == "rules")
        {
            _body.AddChild(_grid);
            Heading("SETUP_RULES_BODY");
        }
        else
        {
            var actions = new HBoxContainer(); _body.AddChild(actions);
            actions.AddChild(Button("All", "SETUP_ALL", () => SetAll(true)));
            actions.AddChild(Button("None", "SETUP_NONE", () => SetAll(false)));
            _body.AddChild(_grid);
            BuildSelection(page);
        }
        Reflow(); _back.GrabFocus();
    }
    private void BuildSetup()
    {
        _capacity = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart }; _body.AddChild(_capacity);
        _body.AddChild(_grid);
        Choices("SETUP_LENGTH", [(1, Tr("SETUP_PREVIEW")), (10, "10"), (20, "20"), (30, "30"), (40, "40"), (50, "50"), (0, Tr("SETUP_UNLIMITED"))],
            _transport.QuestionCount, count => { _transport.QuestionCount = count; RefreshCapacity(); }, "questions");
        Choices("SETUP_SECONDS", [(10, "10"), (20, "20"), (30, "30"), (60, "60"), (120, "120"), (0, Tr("SETUP_UNTIMED"))],
            _transport.QuestionSeconds, seconds => _transport.QuestionSeconds = seconds, "time");
        var speed = new CheckButton { Name = "SpeedScoring", Text = "SETUP_SPEED_SCORING", SizeFlagsHorizontal = SizeFlags.ExpandFill,
            CustomMinimumSize = new(64, 64), ButtonPressed = _transport.SpeedScoring };
        speed.Toggled += on => _transport.SpeedScoring = on; _grid.AddChild(speed);
        var difficulty = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _grid.AddChild(difficulty);
        IconHeading(difficulty, "SETUP_DIFFICULTY", "difficulty");
        var bands = new HBoxContainer(); difficulty.AddChild(bands);
        foreach (var (key, levels) in new[] { ("LOW", new[] { 1, 2 }), ("MEDIUM", new[] { 3 }), ("HIGH", new[] { 4, 5 }) })
        {
            var button = Button("Difficulty" + key, "SETUP_" + key, () => { });
            button.ToggleMode = true; button.SetPressedNoSignal(levels.All(_transport.EnabledDifficulties.Contains));
            QuizShowTheme.SetFontSize(button, 17);
            button.Toggled += on =>
            {
                foreach (var level in levels) { if (on) _transport.EnabledDifficulties.Add(level); else _transport.EnabledDifficulties.Remove(level); }
                RefreshCapacity();
            };
            bands.AddChild(button);
        }
        var strategy = new CheckButton { SizeFlagsHorizontal = SizeFlags.ExpandFill, Name = "Strategy", Text = "STRATEGY_ENABLED", ButtonPressed = _transport.StrategyEnabled };
        strategy.Toggled += on => _transport.StrategyEnabled = on; _grid.AddChild(strategy);
        var teams = new CheckButton { SizeFlagsHorizontal = SizeFlags.ExpandFill, Name = "Teams", Text = "TEAM_ENABLE", ButtonPressed = _transport.Snapshot?.TeamMode == true };
        teams.Toggled += _transport.SetTeamMode; _grid.AddChild(teams);
        var links = new GridContainer { Columns = 3 }; _links = links; _body.AddChild(links);
        foreach (var item in new[] { "categories", "cards", "missions" })
        {
            var count = item == "categories" ? _transport.EnabledCategories?.Count ?? _transport.QuestionCategories.Count :
                item == "cards" ? _transport.EnabledCards.Count : _transport.EnabledMissions.Count;
            var link = Button(item, Tr("SETUP_" + item.ToUpperInvariant()) + $"\n({count})", () => ShowPage(item), item);
            link.IconAlignment = HorizontalAlignment.Center; link.VerticalIconAlignment = VerticalAlignment.Top;
            QuizShowTheme.SetFontSize(link, 17); links.AddChild(link);
        }
        var icons = new HBoxContainer { Name = "CategorySummary" }; _body.AddChild(icons);
        foreach (var category in _transport.QuestionCategories.Where(c => _transport.EnabledCategories?.Contains(c.Id) != false))
            icons.AddChild(new TextureRect { Texture = LobbyIcons.Texture(category.Id), CustomMinimumSize = new(22, 28),
                SizeFlagsHorizontal = SizeFlags.ExpandFill, ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
                StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered, TooltipText = Tr(category.NameKey) });
        RefreshCapacity();
    }
    private void RefreshCapacity()
    {
        var count = _transport.SelectedQuestionCapacity;
        _capacity.Text = string.Format(Tr("SETUP_CAPACITY"), count, _transport.QuestionCount == 0 ? Tr("SETUP_UNLIMITED").ToString() : _transport.QuestionCount.ToString());
        _capacity.AddThemeColorOverride("font_color", QuizShowTheme.AnswerColor(count < Math.Max(1, _transport.QuestionCount) ? 0 : 3));
    }
    private void BuildSelection(string page)
    {
        if (page == "categories")
        {
            _transport.EnabledCategories ??= _transport.QuestionCategories.Select(c => c.Id).ToHashSet();
            foreach (var category in _transport.QuestionCategories)
                Tile(category.Id, category.Id == "cinema_tv" ? "SETUP_CINEMA" : category.NameKey, category.Id, _transport.EnabledCategories.Contains(category.Id), on =>
                { if (on) _transport.EnabledCategories.Add(category.Id); else _transport.EnabledCategories.Remove(category.Id); });
        }
        else if (page == "cards")
            foreach (var kind in Enum.GetValues<CardKind>())
                Tile(kind.ToString(), "SETUP_CARD_NAME_" + kind, "cards", _transport.EnabledCards.Contains(kind), on =>
                {
                    if (on) _transport.EnabledCards.Add(kind); else _transport.EnabledCards.Remove(kind);
                    _transport.AllowSteal = _transport.EnabledCards.Overlaps([CardKind.Shield, CardKind.Steal]);
                }, "SETUP_CARD_HELP_" + kind);
        else
            foreach (var kind in Enum.GetValues<MissionKind>())
                Tile(kind.ToString(), "SETUP_MISSION_NAME_" + kind, "missions", _transport.EnabledMissions.Contains(kind), on =>
                { if (on) _transport.EnabledMissions.Add(kind); else _transport.EnabledMissions.Remove(kind); }, "STRATEGY_MISSION_" + kind);
    }
    private void Tile(string id, string key, string icon, bool selected, Action<bool> change, string? description = null)
    {
        var tile = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _grid.AddChild(tile);
        var button = Button(id, "", () => { }, icon); button.ToggleMode = true;
        button.IconAlignment = HorizontalAlignment.Center; button.AddThemeConstantOverride("icon_max_width", 48);
        button.CustomMinimumSize = new(64, 80); button.SetPressedNoSignal(selected);
        var status = new Label { HorizontalAlignment = HorizontalAlignment.Center };
        void State(bool on)
        {
            status.Text = (on ? "✓ " : "○ ") + Tr(key);
            button.AccessibilityName = Tr(key) + ": " + Tr(on ? "LOBBY_READY_YES" : "LOBBY_READY_NO");
            button.TooltipText = Tr(key); button.Modulate = on ? Colors.White : new Color(1, 1, 1, .55f);
        }
        button.Toggled += on => { change(on); State(on); }; tile.AddChild(button); tile.AddChild(status);
        QuizShowTheme.SetFontSize(status, 17); State(selected);
        if (description is not null)
        {
            var label = new Label { Text = description, AutowrapMode = TextServer.AutowrapMode.WordSmart };
            QuizShowTheme.SetFontSize(label, 16); tile.AddChild(label);
        }
    }
    private void SetAll(bool on)
    {
        if (_page == "categories") _transport.EnabledCategories = on ? _transport.QuestionCategories.Select(c => c.Id).ToHashSet() : [];
        else if (_page == "cards") { _transport.EnabledCards = on ? Enum.GetValues<CardKind>().ToHashSet() : []; _transport.AllowSteal = on; }
        else _transport.EnabledMissions = on ? Enum.GetValues<MissionKind>().ToHashSet() : [];
        ShowPage(_page);
    }
    private void Reflow()
    {
        if (_grid is null) return;
        _grid.Columns = _page == "setup" ? (Size.X > 850 ? 2 : 1) : Size.X > 850 ? (_page == "categories" ? 4 : 3) : _page == "categories" ? 3 : 2;
        if (_page == "setup" && _links is not null) _links.Columns = Size.X < 850 && PresentationShell.For(this)?.Preferences.LargeText == true ? 1 : 3;
    }
}

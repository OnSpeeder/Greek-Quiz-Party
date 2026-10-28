using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Device-owned slot controls; the host validates every roster/team intent.</summary>
public partial class RosterEditor : VBoxContainer
{
    private LobbyTransport? _transport;
    private LineEdit _name = null!;
    private Button _add = null!;
    private CheckButton _teams = null!;
    private Label _hint = null!;
    private GridContainer _rows = null!;
    private bool _hostOptions;
    private bool _editing;
    private Button _addToggle = null!;
    private CharacterPicker _characters = null!;
    public override void _Ready()
    {
        Visible = false;
        _name = new LineEdit { Name = "LocalName", MaxLength = 32, PlaceholderText = "LOCAL_NAME", CustomMinimumSize = new(0, 64) };
        _add = new Button { Name = "AddLocal", Text = "LOCAL_ADD", CustomMinimumSize = new(0, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _characters = new CharacterPicker { Name = "LocalCharacter", Visible = false };
        _characters.SelectionChanged += UpdateAdd;
        _teams = new CheckButton { Name = "Teams", Text = "TEAM_ENABLE", CustomMinimumSize = new(0, 64) };
        _hint = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _rows = new GridContainer { Name = "Players", Columns = 3, SizeFlagsHorizontal = SizeFlags.ExpandFill };
        _rows.AddThemeConstantOverride("h_separation", 8); _rows.AddThemeConstantOverride("v_separation", 8);
        _addToggle = new Button { Name = "AddController", Text = "UI_ADD_CONTROLLER" };
        _addToggle.Pressed += () => { _editing = !_editing; _name.Visible = _editing; _add.Visible = _editing; _characters.Visible = _editing; if (_transport?.Snapshot is { } snapshot) Render(snapshot); };
        AddChild(_hint); AddChild(_rows); AddChild(_addToggle); AddChild(_name); AddChild(_characters); AddChild(_add); AddChild(_teams);
        _name.Visible = false; _add.Visible = false;
        _name.TextChanged += _ => UpdateAdd();
        _add.Pressed += () =>
        {
            if (_transport is null) return;
            var slot = Enumerable.Range(1, 7).FirstOrDefault(s => !_transport.OwnedPlayers.Any(p => p.LocalSlot == s));
            if (slot == 0) return;
            _transport.AddLocalPlayer(_name.Text.Trim(), slot, _characters.Selected); _name.Text = "";
        };
        _teams.Toggled += enabled => _transport?.SetTeamMode(enabled);
    }
    public void Bind(LobbyTransport transport)
    { _transport = transport; transport.SnapshotChanged += Render; }
    private void UpdateAdd() => _add.Disabled = _transport?.Snapshot is not { Phase: "Lobby" } snapshot || snapshot.Players.Length >= snapshot.MaxPlayers ||
        !LobbyProtocol.ValidName(_name.Text.Trim()) || _characters.Selected is null;
    private void Render(LobbySnapshotDto snapshot)
    {
        Visible = snapshot.Phase == "Lobby";
        if (!Visible || _transport is null) return;
        _characters.SetTaken(snapshot.Players.Where(p => p.CharacterId is not null).Select(p => p.CharacterId!.Value));
        if (_characters.Selected is null)
            _characters.Select(Enumerable.Range(0, QuizParty.Core.Players.Characters.Count).Where(id => snapshot.Players.All(p => p.CharacterId != id)).Select(id => (int?)id).FirstOrDefault());
        _addToggle.Visible = _transport.OwnedPlayers.Count > 0;
        UpdateAdd(); _teams.Visible = _transport.IsHost && _hostOptions; _teams.SetPressedNoSignal(snapshot.TeamMode);
        _hint.Text = string.Format(Tr("HOST_PLAYER_COUNT"), snapshot.Players.Length, snapshot.MaxPlayers);
        if (snapshot.TeamMode) _hint.Text += "\n" + Tr(snapshot.Players.Select(p => p.TeamId).Distinct().Count() == 2 ? "TEAM_HINT" : "TEAM_NEED_TWO");
        foreach (var child in _rows.GetChildren()) { _rows.RemoveChild(child); child.QueueFree(); }
        var owned = _transport.OwnedPlayers.Select(p => p.PlayerId).ToHashSet();
        var avatar = 0;
        foreach (var player in snapshot.Players)
        {
            var accent = snapshot.TeamMode ? QuizShowTheme.AnswerColor(player.TeamId == 2 ? 0 : 1) :
                QuizShowTheme.AnswerColor(player.Ready ? 3 : 2);
            var frame = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _rows.AddChild(frame);
            var ready = new Button { Name = "Player" + player.LocalSlot,
                CustomMinimumSize = new(0, 100), SizeFlagsHorizontal = SizeFlags.ExpandFill,
                AccessibilityName = player.DisplayName + ": " + Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO"),
                TooltipText = player.DisplayName + " · " + Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO") };
            ready.AddThemeStyleboxOverride("normal", QuizShowTheme.Card(QuizShowTheme.Plum, accent));
            frame.AddChild(ready);
            var card = new VBoxContainer { MouseFilter = MouseFilterEnum.Ignore }; ready.AddChild(card);
            card.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect);
            card.OffsetLeft = 20; card.OffsetRight = -20; card.OffsetTop = 12; card.OffsetBottom = -12;
            var symbols = new HBoxContainer { Alignment = BoxContainer.AlignmentMode.Center, MouseFilter = MouseFilterEnum.Ignore }; card.AddChild(symbols);
            symbols.AddChild(GameArt.Avatar(player.CharacterId ?? avatar++, 32));
            symbols.AddChild(new TextureRect { Texture = LobbyIcons.Texture(player.Ready ? "ready" : "waiting"),
                CustomMinimumSize = new(28, 32), ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
                StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered, MouseFilter = MouseFilterEnum.Ignore });
            var name = new Label { Text = player.DisplayName + (snapshot.TeamMode ? " · " + Tr("TEAM_" + player.TeamId) : ""),
                HorizontalAlignment = HorizontalAlignment.Center, AutowrapMode = TextServer.AutowrapMode.Off,
                TextOverrunBehavior = TextServer.OverrunBehavior.TrimEllipsis, MouseFilter = MouseFilterEnum.Ignore };
            name.SetMeta("presentation_no_wrap", true); QuizShowTheme.SetFontSize(name, 17); card.AddChild(name);
            if (owned.Contains(player.PlayerId))
                ready.Pressed += () => _transport.SetReady(!player.Ready, localSlot: player.LocalSlot);
            else ready.FocusMode = FocusModeEnum.None;
            if (_editing && owned.Contains(player.PlayerId) && player.LocalSlot != 0)
            {
                var remove = new Button { Text = "×", AccessibilityName = Tr("LOCAL_REMOVE"), TooltipText = Tr("LOCAL_REMOVE"), CustomMinimumSize = new(64, 64) };
                remove.Pressed += () => _transport.RemoveLocalPlayer(player.LocalSlot); frame.AddChild(remove);
            }
            if (_transport.IsHost && snapshot.TeamMode)
            {
                var team = new OptionButton { CustomMinimumSize = new(0, 64) };
                team.AddItem(Tr("TEAM_1"), 1); team.AddItem(Tr("TEAM_2"), 2); team.Select(player.TeamId == 2 ? 1 : 0);
                team.ItemSelected += index => _transport.AssignTeam(player.PlayerId, team.GetItemId((int)index)); frame.AddChild(team);
            }
        }
    }
    public void MoveAddActionTo(Node parent) { _addToggle.Reparent(parent); _addToggle.SizeFlagsHorizontal = SizeFlags.ExpandFill; }
    public void ShowHostOptions(bool visible) { _hostOptions = visible; _teams.Visible = visible && _transport?.IsHost == true; }
    public override void _ExitTree() { if (_transport is not null) _transport.SnapshotChanged -= Render; }
}

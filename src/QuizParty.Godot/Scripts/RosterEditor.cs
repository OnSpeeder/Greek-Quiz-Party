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
    private VBoxContainer _rows = null!;
    private bool _hostOptions;
    private bool _editing;
    private Button _addToggle = null!;
    public override void _Ready()
    {
        Visible = false;
        _name = new LineEdit { Name = "LocalName", MaxLength = 32, PlaceholderText = Tr("LOCAL_NAME"), CustomMinimumSize = new(0, 64) };
        _add = new Button { Name = "AddLocal", Text = Tr("LOCAL_ADD"), CustomMinimumSize = new(0, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _teams = new CheckButton { Name = "Teams", Text = Tr("TEAM_ENABLE"), CustomMinimumSize = new(0, 64) };
        _hint = new Label { AutowrapMode = TextServer.AutowrapMode.WordSmart };
        _rows = new VBoxContainer { Name = "Players" };
        _addToggle = new Button { Name = "AddController", Text = Tr("UI_ADD_CONTROLLER") };
        _addToggle.Pressed += () => { _editing = !_editing; _name.Visible = _editing; _add.Visible = _editing; };
        AddChild(_hint); AddChild(_rows); AddChild(_addToggle); AddChild(_name); AddChild(_add); AddChild(_teams);
        _name.Visible = false; _add.Visible = false;
        _name.TextChanged += _ => UpdateAdd();
        _add.Pressed += () =>
        {
            if (_transport is null) return;
            var slot = Enumerable.Range(1, 7).FirstOrDefault(s => !_transport.OwnedPlayers.Any(p => p.LocalSlot == s));
            if (slot == 0) return;
            _transport.AddLocalPlayer(_name.Text.Trim(), slot); _name.Text = "";
        };
        _teams.Toggled += enabled => _transport?.SetTeamMode(enabled);
    }
    public void Bind(LobbyTransport transport)
    { _transport = transport; transport.SnapshotChanged += Render; }
    private void UpdateAdd() => _add.Disabled = _transport?.Snapshot is not { Phase: "Lobby", Players.Length: < 8 } ||
        !LobbyProtocol.ValidName(_name.Text.Trim());
    private void Render(LobbySnapshotDto snapshot)
    {
        Visible = snapshot.Phase == "Lobby";
        if (!Visible || _transport is null) return;
        UpdateAdd(); _teams.Visible = _transport.IsHost && _hostOptions; _teams.SetPressedNoSignal(snapshot.TeamMode);
        _hint.Text = string.Format(Tr("UI_WAITING_COUNT"), snapshot.Players.Length);
        if (snapshot.TeamMode) _hint.Text += "\n" + Tr(snapshot.Players.Select(p => p.TeamId).Distinct().Count() == 2 ? "TEAM_HINT" : "TEAM_NEED_TWO");
        foreach (var child in _rows.GetChildren()) { _rows.RemoveChild(child); child.QueueFree(); }
        var owned = _transport.OwnedPlayers.Select(p => p.PlayerId).ToHashSet();
        var avatar = 0;
        foreach (var player in snapshot.Players)
        {
            var frame = new PanelContainer(); _rows.AddChild(frame);
            var card = new HBoxContainer(); frame.AddChild(card); card.AddChild(GameArt.Avatar(avatar++));
            var row = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; card.AddChild(row);
            row.AddChild(new Label { Text = player.DisplayName +
                (snapshot.TeamMode ? " — " + Tr("TEAM_" + player.TeamId) : ""), AutowrapMode = TextServer.AutowrapMode.WordSmart });
            if (owned.Contains(player.PlayerId))
            {
                var actions = new HBoxContainer(); row.AddChild(actions);
                var ready = new Button { Text = Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO"), CustomMinimumSize = new(0, 64), SizeFlagsHorizontal = SizeFlags.ExpandFill };
                ready.Pressed += () => _transport.SetReady(!player.Ready, localSlot: player.LocalSlot); actions.AddChild(ready);
                if (player.LocalSlot != 0)
                {
                    var remove = new Button { Text = "×", AccessibilityName = Tr("LOCAL_REMOVE"), TooltipText = Tr("LOCAL_REMOVE"), CustomMinimumSize = new(64, 64) };
                    remove.Pressed += () => _transport.RemoveLocalPlayer(player.LocalSlot); actions.AddChild(remove);
                }
            }
            else row.AddChild(new Label { Text = Tr(player.Ready ? "LOBBY_READY_YES" : "LOBBY_READY_NO"), AutowrapMode = TextServer.AutowrapMode.WordSmart });
            if (_transport.IsHost && snapshot.TeamMode)
            {
                var team = new OptionButton { CustomMinimumSize = new(0, 64) };
                team.AddItem(Tr("TEAM_1"), 1); team.AddItem(Tr("TEAM_2"), 2); team.Select(player.TeamId == 2 ? 1 : 0);
                team.ItemSelected += index => _transport.AssignTeam(player.PlayerId, team.GetItemId((int)index)); row.AddChild(team);
            }
        }
    }
    public void ShowHostOptions(bool visible) { _hostOptions = visible; _teams.Visible = visible && _transport?.IsHost == true; }
    public override void _ExitTree() { if (_transport is not null) _transport.SnapshotChanged -= Render; }
}

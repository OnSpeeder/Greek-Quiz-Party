using Godot;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Renders validated advertisements; admission still belongs to the host.</summary>
public partial class RoomBrowser : VBoxContainer
{
    private LanDiscovery? _discovery;
    private Action<DiscoveredRoom>? _join;
    private Label _status = null!;
    private VBoxContainer _rooms = null!;
    public override void _Ready()
    {
        AddChild(new Label { Text = Tr("DISCOVERY_TITLE") });
        var refresh = new Button { Name = "Refresh", Text = Tr("DISCOVERY_REFRESH"), CustomMinimumSize = new Vector2(0, 64) };
        refresh.Pressed += () => _discovery?.Scan();
        AddChild(refresh);
        _status = new Label { Name = "Status", Text = Tr("DISCOVERY_HELP"), AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_status);
        _rooms = new VBoxContainer { Name = "Rooms" };
        AddChild(_rooms);
    }

    public void Bind(LanDiscovery discovery, Action<DiscoveredRoom> join)
    {
        _discovery = discovery; _join = join;
        discovery.StatusChanged += OnStatus;
        discovery.RoomsChanged += Render;
    }

    private void OnStatus(string reason) => _status.Text = Tr("DISCOVERY_STATUS_" + reason);
    private void Render(IReadOnlyList<DiscoveredRoom> rooms)
    {
        if (rooms.Count == 0) _status.Text = Tr("DISCOVERY_STATUS_NoRooms");
        foreach (var child in _rooms.GetChildren()) { _rooms.RemoveChild(child); child.QueueFree(); }
        foreach (var room in rooms)
        {
            var state = room.Room.State != "Lobby" ? "DISCOVERY_STARTED" : room.Room.Players >= room.Room.MaxPlayers ? "DISCOVERY_FULL" :
                room.Room.RequiresPin ? "DISCOVERY_PIN" : "DISCOVERY_OPEN";
            var button = new Button
            {
                Text = string.Format(Tr("DISCOVERY_ROOM"), room.Room.RoomName, room.Room.Players, room.Room.MaxPlayers, Tr(state)),
                CustomMinimumSize = new Vector2(0, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart,
                Disabled = room.Room.State != "Lobby" || room.Room.Players >= room.Room.MaxPlayers
            };
            button.Pressed += () => _join?.Invoke(room);
            _rooms.AddChild(button);
        }
    }

    public override void _ExitTree()
    {
        if (_discovery is null) return;
        _discovery.StatusChanged -= OnStatus; _discovery.RoomsChanged -= Render;
    }
}

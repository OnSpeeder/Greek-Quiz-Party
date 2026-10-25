using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Presentation;

public sealed record RoomCreationRequest(string RoomName, string Pin, int MaxPlayers, bool HostPlays, string PlayerName, int Character);

/// <summary>No room is opened until the final create action succeeds.</summary>
public partial class RoomCreationPanel : VBoxContainer
{
    private GridContainer _fields = null!;
    private PlayerIdentityForm _identity = null!;
    private LineEdit _room = null!;
    private LineEdit _pin = null!;
    private OptionButton _capacity = null!;
    private CheckButton _hostPlays = null!;
    private Button _submit = null!;
    public bool IdentityOpen { get; private set; }
    public event Action<RoomCreationRequest>? CreateRequested;
    public event Action? StepChanged;
    public override void _Ready()
    {
        _fields = new GridContainer { Name = "RoomFields", SizeFlagsHorizontal = SizeFlags.ExpandFill }; AddChild(_fields);
        _room = new LineEdit { Name = "RoomName", MaxLength = 32, Text = Tr("UI_ROOM_DEFAULT"), PlaceholderText = "LOBBY_ROOM_NAME" };
        _pin = new LineEdit { Name = "RoomPin", MaxLength = 6, Secret = true, PlaceholderText = "HOST_PIN_HINT",
            VirtualKeyboardType = LineEdit.VirtualKeyboardTypeEnum.Number };
        _capacity = new OptionButton { Name = "Capacity" };
        foreach (var count in Enumerable.Range(2, 7)) _capacity.AddItem(count.ToString(), count);
        _capacity.Select(6);
        _hostPlays = new CheckButton { Name = "HostPlays", Text = "HOST_PLAYS", ButtonPressed = true };
        Field("UI_ROOM_LABEL", _room); Field("HOST_OPTIONAL_PIN", _pin); Field("HOST_CAPACITY", _capacity);
        _fields.AddChild(_hostPlays);
        _identity = new PlayerIdentityForm { Name = "Identity", Visible = false }; AddChild(_identity);
        _submit = new Button { Name = "Create", Text = "HOST_CONTINUE", ThemeTypeVariation = "PrimaryAction",
            CustomMinimumSize = new(0, 72), SizeFlagsHorizontal = SizeFlags.ExpandFill }; AddChild(_submit);
        _room.TextChanged += _ => Update(); _pin.TextChanged += _ => Update(); _hostPlays.Toggled += _ => Update();
        _identity.NameInput.TextChanged += _ => Update(); _identity.Characters.SelectionChanged += Update;
        _submit.Pressed += Submit; Resized += Reflow; Reflow(); Update();
    }
    private void Field(string key, Control field)
    {
        var column = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill }; _fields.AddChild(column);
        column.AddChild(new Label { Text = key }); field.SizeFlagsHorizontal = SizeFlags.ExpandFill; column.AddChild(field);
    }
    private void Reflow() => _fields.Columns = Size.X >= 850 ? 2 : 1;
    private void Update()
    {
        if (_submit is null) return;
        _submit.Text = IdentityOpen || !_hostPlays.ButtonPressed ? "LOBBY_HOST" : "HOST_CONTINUE";
        _submit.Disabled = !LobbyProtocol.ValidName(_room.Text.Trim()) || !RoomAdmission.ValidPin(_pin.Text) ||
            IdentityOpen && (!LobbyProtocol.ValidName(_identity.NameInput.Text.Trim()) || _identity.Characters.Selected is null);
    }
    private void Submit()
    {
        if (_submit.Disabled) return;
        if (_hostPlays.ButtonPressed && !IdentityOpen)
        {
            IdentityOpen = true; _fields.Hide(); _identity.Show(); _submit.Reparent(_identity);
            if (OS.HasFeature("android")) DisplayServer.VirtualKeyboardHide();
            Update(); StepChanged?.Invoke(); return;
        }
        if (OS.HasFeature("android")) DisplayServer.VirtualKeyboardHide();
        CreateRequested?.Invoke(new(_room.Text.Trim(), _pin.Text, _capacity.GetSelectedId(), _hostPlays.ButtonPressed,
            _hostPlays.ButtonPressed ? _identity.NameInput.Text.Trim() : "", _identity.Characters.Selected ?? 0));
    }
    public bool Back()
    {
        if (!IdentityOpen) return false;
        IdentityOpen = false; _submit.Reparent(this); _identity.Hide(); _fields.Show(); Update(); StepChanged?.Invoke(); return true;
    }
    public void Reset() { Back(); _pin.Text = ""; }
}

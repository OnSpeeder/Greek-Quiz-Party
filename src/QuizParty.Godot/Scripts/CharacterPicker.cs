using Godot;
using QuizParty.Core.Players;

namespace QuizParty.Presentation;

public partial class CharacterPicker : GridContainer
{
    private readonly List<Button> _buttons = [];
    private readonly HashSet<int> _taken = [];
    private ShaderMaterial _unavailable = null!;
    public int? Selected { get; private set; }
    public event Action? SelectionChanged;
    public override void _Ready()
    {
        _unavailable = new ShaderMaterial { Shader = new Shader { Code = """
            shader_type canvas_item;
            void fragment() {
                vec4 color = texture(TEXTURE, UV) * COLOR;
                float grey = dot(color.rgb, vec3(0.299, 0.587, 0.114));
                COLOR = vec4(vec3(grey), color.a);
            }
            """ } };
        AddThemeConstantOverride("h_separation", 12); AddThemeConstantOverride("v_separation", 12);
        for (var i = 0; i < Characters.Count; i++)
        {
            var id = i;
            var button = new Button { Name = "Character" + i, Icon = GameArt.AvatarTexture(i), ExpandIcon = true,
                CustomMinimumSize = new(0, 112), SizeFlagsHorizontal = SizeFlags.ExpandFill,
                IconAlignment = HorizontalAlignment.Center, AccessibilityName = Tr("CHARACTER_" + i),
                TooltipText = Tr("CHARACTER_" + i) };
            button.AddThemeConstantOverride("icon_max_width", 80);
            button.Pressed += () => Select(id);
            _buttons.Add(button); AddChild(button);
        }
        Resized += Layout; Layout(); Render();
    }
    private void Layout() => Columns = Size.X >= 700 ? 4 : 2;
    public void Select(int? character)
    {
        if (character is { } id && (!Characters.IsValid(id) || _taken.Contains(id))) return;
        if (Selected == character) return;
        Selected = character; Render(); SelectionChanged?.Invoke();
    }
    public void SetTaken(IEnumerable<int> taken)
    {
        _taken.Clear(); foreach (var id in taken) _taken.Add(id);
        if (Selected is { } selected && _taken.Contains(selected)) { Selected = null; SelectionChanged?.Invoke(); }
        Render();
    }
    private void Render()
    {
        for (var i = 0; i < _buttons.Count; i++)
        {
            var button = _buttons[i]; button.Disabled = _taken.Contains(i);
            button.Material = button.Disabled ? _unavailable : null;
            button.Modulate = button.Disabled ? new(.6f, .6f, .6f, .8f) : Colors.White;
            button.Text = Selected == i ? "✓" : "";
            button.ThemeTypeVariation = Selected == i ? "PrimaryAction" : "";
            button.AccessibilityName = Tr("CHARACTER_" + i) + (button.Disabled ? " — " + Tr("CHARACTER_TAKEN") : Selected == i ? " — " + Tr("CHARACTER_SELECTED") : "");
        }
    }
}

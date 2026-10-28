using Godot;

namespace QuizParty.Presentation;

/// <summary>Illustrated stage only; state stays in native UI layered above it.</summary>
public partial class StageBackdrop : Control
{
    private TextureRect? _art;
    private bool _highContrast;
    private string _themeId = "showtime";
    public string ThemeId
    {
        get => _themeId;
        set { _themeId = value; ApplyTheme(); QueueRedraw(); }
    }
    public bool HighContrast
    {
        get => _highContrast;
        set { _highContrast = value; if (_art is not null) _art.Visible = !value; QueueRedraw(); }
    }
    public override void _Ready()
    {
        MouseFilter = MouseFilterEnum.Ignore;
        _art = new TextureRect { Name = "StageArt", ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
            StretchMode = TextureRect.StretchModeEnum.KeepAspectCovered, MouseFilter = MouseFilterEnum.Ignore,
            Visible = !HighContrast, Modulate = new Color(.8f, .8f, .86f) };
        AddChild(_art); _art.SetAnchorsAndOffsetsPreset(LayoutPreset.FullRect); ApplyTheme();
        Resized += UpdateArt; UpdateArt();
    }
    private void ApplyTheme()
    {
        if (_art is null) return;
        _art.Modulate = _themeId switch
        {
            "studio" => new Color(.66f, .95f, 1f),
            "neon" => new Color(1f, .66f, 1f),
            "retro" => new Color(1f, .79f, .55f),
            _ => new Color(.8f, .8f, .86f)
        };
    }
    private void UpdateArt()
    {
        if (_art is null) return;
        _art.Texture = GD.Load<Texture2D>(Size.X < Size.Y ? "res://Art/showtime-stage-v2.png" : "res://Art/showtime-stage-wide-v2.png");
    }
    public override void _Draw() => DrawRect(new Rect2(Vector2.Zero, Size), ShowtimeTheme.Navy);
}

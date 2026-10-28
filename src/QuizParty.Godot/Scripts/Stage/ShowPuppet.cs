using Godot;

namespace QuizParty.Presentation;

/// <summary>Illustrated cutout rig. All transforms are cosmetic and scene-owned.</summary>
public partial class ShowPuppet : Node2D
{
    public bool Blue { get; set; }
    private readonly Sprite2D[] _faces = new Sprite2D[3];
    public Node2D Head { get; private set; } = null!;
    public Node2D LeftArm { get; private set; } = null!;
    public Node2D RightArm { get; private set; } = null!;
    public Node2D Body { get; private set; } = null!;

    public override void _Ready()
    {
        var atlas = GD.Load<Texture2D>($"res://Art/LivingShow/{(Blue ? "blue" : "orange")}-puppet.png");
        LeftArm = Joint("LeftArm", new(-58, -120));
        RightArm = Joint("RightArm", new(58, -120));
        Body = Joint("Body", new(0, -80));
        AddPart(Body, atlas, 0, 1, 170);
        Head = Joint("Head", new(0, -205));
        for (var i = 0; i < 3; i++) _faces[i] = AddPart(Head, atlas, i, 0, 216);
        // Atlas arms point inward/outward differently. Anchor at the shoulder,
        // behind the torso, so the seams remain concealed throughout rotation.
        var left = AddPart(LeftArm, atlas, Blue ? 2 : 1, 1, 142);
        left.Position = new(-48, 16);
        var right = AddPart(RightArm, atlas, Blue ? 1 : 2, 1, 142);
        right.Position = new(48, 16);
        SetExpression(0);
    }

    private Node2D Joint(string name, Vector2 position)
    {
        var node = new Node2D { Name = name, Position = position }; AddChild(node); return node;
    }

    private static Sprite2D AddPart(Node2D parent, Texture2D atlas, int column, int row, float width)
    {
        // Trim transparent margins without altering the generated source atlas.
        using var image = atlas.GetImage();
        var cell = new Rect2I(column * image.GetWidth() / 3, row * image.GetHeight() / 2,
            image.GetWidth() / 3, image.GetHeight() / 2);
        using var cropped = image.GetRegion(cell);
        var used = cropped.GetUsedRect();
        var texture = new AtlasTexture { Atlas = atlas, Region = new Rect2(cell.Position + used.Position, used.Size) };
        var sprite = new Sprite2D { Texture = texture, Scale = Vector2.One * (width / used.Size.X) };
        parent.AddChild(sprite); return sprite;
    }

    public void SetExpression(int expression)
    {
        for (var i = 0; i < _faces.Length; i++) _faces[i].Visible = i == expression;
    }

    public void ResetPose()
    {
        Rotation = 0; Scale = Vector2.One;
        Head.Rotation = 0; Head.Position = new(0, -205); Head.Scale = Vector2.One;
        LeftArm.Rotation = 0; RightArm.Rotation = 0; Body.Scale = Vector2.One;
        SetExpression(0);
    }
}

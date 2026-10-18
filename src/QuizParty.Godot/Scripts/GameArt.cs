using Godot;

namespace QuizParty.Presentation;

public static class GameArt
{
    public static TextureRect Avatar(int index, int size = 72)
    {
        var regions = new[] { new Rect2(0, 0, 600, 724), new Rect2(630, 0, 450, 724),
            new Rect2(1120, 0, 490, 724), new Rect2(1660, 0, 512, 724) };
        return new TextureRect { Texture = new AtlasTexture { Atlas = GD.Load<Texture2D>("res://Art/showtime-crew-v2.png"), Region = regions[index % 4] },
            CustomMinimumSize = new(size, size), ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
            StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered, MouseFilter = Control.MouseFilterEnum.Ignore };
    }
}

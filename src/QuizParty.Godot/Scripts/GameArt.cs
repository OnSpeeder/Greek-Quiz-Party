using Godot;

namespace QuizParty.Presentation;

public static class GameArt
{
    public static Texture2D AvatarTexture(int index)
    {
        if (index is < 0 or > 7) throw new ArgumentOutOfRangeException(nameof(index));
        if (index >= 4)
        {
            var atlas = GD.Load<Texture2D>("res://Art/showtime-extra-crew-v1.png");
            var size = atlas.GetSize() / 2;
            return new AtlasTexture { Atlas = atlas, Region = new Rect2(new Vector2((index - 4) % 2, (index - 4) / 2) * size, size) };
        }
        var regions = new[] { new Rect2(0, 0, 600, 724), new Rect2(630, 0, 450, 724),
            new Rect2(1120, 0, 490, 724), new Rect2(1660, 0, 512, 724) };
        return new AtlasTexture { Atlas = GD.Load<Texture2D>("res://Art/showtime-crew-v2.png"), Region = regions[index] };
    }

    public static TextureRect Avatar(int index, int size = 72) => new() { Texture = AvatarTexture(index),
            CustomMinimumSize = new(size, size), ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize,
            StretchMode = TextureRect.StretchModeEnum.KeepAspectCentered, MouseFilter = Control.MouseFilterEnum.Ignore };
}

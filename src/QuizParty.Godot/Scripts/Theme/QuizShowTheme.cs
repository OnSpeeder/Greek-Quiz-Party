using Godot;

namespace QuizParty.Presentation;

/// <summary>Shared Showtime recipe; settings may retain their illustrated skins.</summary>
public static class QuizShowTheme
{
    public static readonly Color Navy = new("0F0A26");
    public static readonly Color Plum = new("1E1442");
    public static readonly Color Gold = new("FFC83B");
    public static Color AnswerColor(int index) => new(index switch
    { 0 => "FF4B6E", 1 => "2B95FF", 2 => "FFB800", 3 => "1AD598", _ => throw new ArgumentOutOfRangeException(nameof(index)) });

    public static Font DisplayFont() => new FontVariation
    {
        BaseFont = GD.Load<FontFile>("res://Art/Fonts/Comfortaa-VariableFont_wght.ttf"),
        VariationEmbolden = .5f,
        VariationOpentype = new global::Godot.Collections.Dictionary { ["wght"] = 700f }
    };

    public static StyleBoxFlat Card(Color fill, Color border, int width = 3) => new()
    {
        BgColor = fill, BorderColor = border,
        BorderWidthLeft = width, BorderWidthRight = width, BorderWidthTop = width,
        BorderWidthBottom = width == 0 ? 0 : Math.Max(8, width),
        CornerRadiusTopLeft = 18, CornerRadiusTopRight = 18,
        CornerRadiusBottomLeft = 18, CornerRadiusBottomRight = 18,
        ShadowSize = width == 0 ? 0 : 8, ShadowOffset = new(0, 4), ShadowColor = new(0, 0, 0, .35f),
        ContentMarginLeft = 20, ContentMarginRight = 20, ContentMarginTop = 16, ContentMarginBottom = 16
    };

    // Geometry is an intentional redundant identifier, independent of font glyphs/color perception.
    public static Texture2D AnswerBadge(int index)
    {
        var shape = index switch
        {
            0 => "<path d='M24 3L45 24L24 45L3 24Z'/>",
            1 => "<circle cx='24' cy='24' r='21'/>",
            2 => "<path d='M24 3L46 44H2Z'/>",
            3 => "<rect x='4' y='4' width='40' height='40' rx='4'/>",
            _ => throw new ArgumentOutOfRangeException(nameof(index))
        };
        using var image = new Image();
        var error = image.LoadSvgFromString($"<svg xmlns='http://www.w3.org/2000/svg' width='48' height='48'><g fill='#{AnswerColor(index).ToHtml(false)}' stroke='#FFFFFF' stroke-width='2'>{shape}</g></svg>");
        if (error != Error.Ok) throw new InvalidOperationException($"Answer badge failed: {error}");
        return ImageTexture.CreateFromImage(image);
    }

    public static void StyleQuestion(Label question)
    {
        question.AutowrapMode = TextServer.AutowrapMode.WordSmart;
        question.AddThemeConstantOverride("outline_size", 4);
        question.AddThemeColorOverride("font_outline_color", new("120A2A"));
    }

    public static void SetFontSize(Control control, int size)
    {
        control.SetMeta("presentation_font", size);
        control.AddThemeFontSizeOverride("font_size", (int)Math.Round(size *
            (PresentationShell.For(control)?.Preferences.LargeText == true ? 1.2 : 1)));
    }
}

using Godot;

namespace QuizParty.Presentation;

public static class ShowtimeTheme
{
    public static readonly Color Navy = QuizShowTheme.Navy;
    public static readonly Color Cyan = new("71e3ef");
    public static readonly Color Gold = QuizShowTheme.Gold;
    public static readonly Color Ink = new("f6f5ff");

    public static StyleBoxFlat Panel(Color fill, Color border, int width = 3)
    {
        return QuizShowTheme.Card(fill, border, width);
    }

    public static Theme Create(PresentationPreferences preferences, int minimumTarget = 64)
    {
        var theme = new Theme { DefaultFontSize = preferences.LargeText ? 27 : 22,
            DefaultFont = QuizShowTheme.DisplayFont() };
        var surface = new Color(preferences.HighContrast ? "080a16" : preferences.ThemeId switch
        { "studio" => "14384b", "neon" => "391b4a", "retro" => "483020", _ => "242441" });
        var border = preferences.HighContrast ? Ink : new Color(preferences.ThemeId switch
        { "studio" => "5b9eb0", "neon" => "b36dbb", "retro" => "bd9562", _ => "62668d" });
        foreach (var type in new[] { "Button", "OptionButton", "CheckButton", "CheckBox" })
        {
            theme.SetStylebox("normal", type, Panel(surface, border));
            theme.SetStylebox("hover", type, Panel(new("303755"), Cyan));
            theme.SetStylebox("pressed", type, Panel(new("304052"), Gold, 3));
            theme.SetStylebox("disabled", type, Panel(new("1b1d32"), new("555974")));
            var focus = Panel(Colors.Transparent, Gold, 4);
            theme.SetStylebox("focus", type, focus);
            foreach (var state in new[] { "font_color", "font_hover_color", "font_pressed_color", "font_focus_color", "font_hover_pressed_color" })
                theme.SetColor(state, type, Ink);
            theme.SetColor("font_disabled_color", type, new("b9bbd1"));
        }
        theme.SetColor("font_color", "TooltipLabel", Ink);
        theme.SetFont("font", "TooltipLabel", theme.DefaultFont);
        theme.SetFontSize("font_size", "TooltipLabel", preferences.LargeText ? 22 : 18);
        var tooltip = Panel(Navy, Cyan, 2);
        tooltip.ContentMarginLeft = 12; tooltip.ContentMarginRight = 12;
        tooltip.ContentMarginTop = 8; tooltip.ContentMarginBottom = 8;
        theme.SetStylebox("panel", "TooltipPanel", tooltip);
        theme.SetColor("font_color", "Label", Ink);
        theme.SetColor("font_color", "LineEdit", Ink);
        theme.SetColor("font_placeholder_color", "LineEdit", new("c2c4dc"));
        theme.SetColor("caret_color", "LineEdit", Gold);
        theme.SetColor("selection_color", "LineEdit", new("46597b"));
        theme.SetStylebox("normal", "LineEdit", Panel(surface, border));
        theme.SetStylebox("focus", "LineEdit", Panel(Colors.Transparent, Gold, 4));
        theme.SetStylebox("panel", "PanelContainer", Panel(new("1b1c35"), border));
        theme.SetStylebox("panel", "PopupMenu", Panel(Navy, Cyan));
        theme.SetColor("font_color", "PopupMenu", Ink);
        theme.SetConstant("v_separation", "PopupMenu", Math.Max(22, minimumTarget - theme.DefaultFontSize));
        theme.SetConstant("separation", "VBoxContainer", 14);
        theme.SetConstant("separation", "HBoxContainer", 12);
        foreach (var (state, color) in new[] { ("background", new Color("242441")), ("fill", Cyan) })
        {
            var strip = Panel(color, color, 0);
            strip.ContentMarginTop = 0; strip.ContentMarginBottom = 0;
            strip.ContentMarginLeft = 0; strip.ContentMarginRight = 0;
            theme.SetStylebox(state, "ProgressBar", strip);
        }
        theme.SetTypeVariation("PrimaryAction", "Button");
        theme.SetStylebox("normal", "PrimaryAction", Panel(Gold, Gold));
        theme.SetStylebox("hover", "PrimaryAction", Panel(new("ffe6b1"), Ink));
        theme.SetStylebox("pressed", "PrimaryAction", Panel(Cyan, Cyan, 3));
        foreach (var state in new[] { "font_color", "font_hover_color", "font_pressed_color", "font_focus_color" })
            theme.SetColor(state, "PrimaryAction", Navy);
        var accents = Enumerable.Range(0, 4).Select(QuizShowTheme.AnswerColor).ToArray();
        for (var index = 0; index < accents.Length; index++)
        {
            var type = "Answer" + index;
            theme.SetTypeVariation(type, "Button");
            theme.SetStylebox("normal", type, Panel(new("141535"), accents[index], 3));
            theme.SetStylebox("hover", type, Panel(new("29234c"), Ink, 3));
            theme.SetStylebox("pressed", type, Panel(new("34345c"), Ink, 4));
            theme.SetStylebox("disabled", type, Panel(new("141535"), accents[index].Darkened(.15f), 2));
            theme.SetColor("font_disabled_color", type, Ink);
        }
        return theme;
    }
}

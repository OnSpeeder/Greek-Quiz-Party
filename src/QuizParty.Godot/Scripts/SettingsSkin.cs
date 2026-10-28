using Godot;

namespace QuizParty.Presentation;

/// <summary>Local settings skin; all lettering stays in native Godot controls.</summary>
public static class SettingsSkin
{
    private const string Art = "res://Art/Settings/";
    // Each page owns its resources. Reopening a page must not resurrect a cached
    // native texture whose previous C# wrapper was collected during scene cleanup.
    public static Texture2D Texture(string name) => ResourceLoader.Load<Texture2D>(
        Art + name + ".svg", cacheMode: ResourceLoader.CacheMode.Ignore);

    public static StyleBoxTexture Slice(string name, int margin, int padding = 18)
    {
        var box = new StyleBoxTexture { Texture = Texture(name) };
        foreach (var side in new[] { Side.Left, Side.Top, Side.Right, Side.Bottom })
        {
            box.SetTextureMargin(side, margin);
            box.SetContentMargin(side, padding);
        }
        return box;
    }

    public static Theme Create(PresentationPreferences preferences, int minimum)
    {
        var theme = ShowtimeTheme.Create(preferences, minimum);
        theme.SetConstant("separation", "VBoxContainer", 8);
        foreach (var type in new[] { "Button", "OptionButton", "CheckButton" })
            theme.SetConstant("icon_max_width", type, 32);
        if (preferences.HighContrast) return theme;
        theme.SetTypeVariation("SettingsTab", "Button");
        using var tab = QuizShowTheme.Card(new("20253e"), new("62668d"));
        using var activeTab = QuizShowTheme.Card(new("27414a"), ShowtimeTheme.Cyan);
        theme.SetStylebox("normal", "SettingsTab", tab);
        theme.SetStylebox("pressed", "SettingsTab", activeTab);
        theme.SetStylebox("hover_pressed", "SettingsTab", activeTab);
        theme.SetTypeVariation("SettingsReset", "Button");
        using var danger = QuizShowTheme.Card(new("502538"), QuizShowTheme.AnswerColor(0));
        theme.SetStylebox("normal", "SettingsReset", danger);
        foreach (var state in new[] { "normal", "hover", "pressed", "hover_pressed" })
        {
            using var empty = new StyleBoxEmpty();
            theme.SetStylebox(state, "CheckButton", empty);
        }
        theme.SetConstant("icon_max_width", "CheckButton", 120);
        theme.SetIcon("checked", "CheckButton", Texture("switch-on"));
        theme.SetIcon("unchecked", "CheckButton", Texture("switch-off"));
        theme.SetIcon("checked_disabled", "CheckButton", Texture("switch-on"));
        theme.SetIcon("unchecked_disabled", "CheckButton", Texture("switch-off"));
        using var track = Slice("slider-track", 8, 8);
        using var fill = Slice("slider-fill", 8, 8);
        theme.SetStylebox("slider", "HSlider", track);
        theme.SetStylebox("grabber_area", "HSlider", fill);
        theme.SetStylebox("grabber_area_highlight", "HSlider", fill);
        theme.SetIcon("grabber", "HSlider", Texture("slider-thumb-idle"));
        theme.SetIcon("grabber_highlight", "HSlider", Texture("slider-thumb-pressed"));
        theme.SetIcon("grabber_disabled", "HSlider", Texture("slider-thumb-disabled"));
        return theme;
    }
}

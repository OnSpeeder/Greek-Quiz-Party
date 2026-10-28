using Godot;

namespace QuizParty.Presentation;

/// <summary>Device-local presentation only; never influences rules or host clocks.</summary>
public sealed record PresentationPreferences(bool Sound = true, float Volume = 0.65f,
    bool ReducedMotion = false, bool LargeText = false, bool HighContrast = false, string Language = "el_GR", bool AutoFitQuestions = true,
    string ThemeId = "showtime")
{
    public static IReadOnlyList<string> ThemeIds { get; } = Array.AsReadOnly(new[] { "showtime", "studio", "neon", "retro" });
    public static PresentationPreferences Load(string path = "user://presentation.cfg")
    {
        using var config = new ConfigFile();
        var error = config.Load(path);
        if (error == Error.FileNotFound) return new();
        if (error != Error.Ok) { GD.PushWarning($"Presentation settings could not load: {error}"); return new(); }
        var defaults = new PresentationPreferences();
        var sound = config.GetValue("ui", "sound", defaults.Sound);
        var volume = config.GetValue("ui", "volume", defaults.Volume);
        var motion = config.GetValue("ui", "reduced_motion", defaults.ReducedMotion);
        var text = config.GetValue("ui", "large_text", defaults.LargeText);
        var contrast = config.GetValue("ui", "high_contrast", defaults.HighContrast);
        var language = config.GetValue("ui", "language", defaults.Language);
        var autoFit = config.GetValue("ui", "auto_fit_questions", defaults.AutoFitQuestions);
        var theme = config.GetValue("ui", "theme", defaults.ThemeId);
        if (sound.VariantType != Variant.Type.Bool || motion.VariantType != Variant.Type.Bool ||
            text.VariantType != Variant.Type.Bool || contrast.VariantType != Variant.Type.Bool || autoFit.VariantType != Variant.Type.Bool ||
            volume.VariantType is not (Variant.Type.Float or Variant.Type.Int) ||
            !float.IsFinite(volume.AsSingle()) || volume.AsSingle() is < 0 or > 1)
        { GD.PushWarning("Presentation settings invalid; using defaults."); return defaults; }
        var locale = language.VariantType == Variant.Type.String && language.AsString() is "el_GR" or "en"
            ? language.AsString() : defaults.Language;
        if (language.VariantType != Variant.Type.String || locale != language.AsString())
            GD.PushWarning("Presentation language invalid; using Greek.");
        var themeId = theme.VariantType == Variant.Type.String && ThemeIds.Contains(theme.AsString()) ? theme.AsString() : defaults.ThemeId;
        if (theme.VariantType != Variant.Type.String || themeId != theme.AsString()) GD.PushWarning("Presentation theme invalid; using Showtime.");
        return new(sound.AsBool(), volume.AsSingle(), motion.AsBool(), text.AsBool(), contrast.AsBool(), locale, autoFit.AsBool(), themeId);
    }

    public Error Save(string path = "user://presentation.cfg")
    {
        using var config = new ConfigFile();
        config.SetValue("ui", "sound", Sound);
        config.SetValue("ui", "volume", Volume);
        config.SetValue("ui", "reduced_motion", ReducedMotion);
        config.SetValue("ui", "large_text", LargeText);
        config.SetValue("ui", "high_contrast", HighContrast);
        config.SetValue("ui", "language", Language);
        config.SetValue("ui", "auto_fit_questions", AutoFitQuestions);
        config.SetValue("ui", "theme", ThemeId);
        return config.Save(path);
    }
}

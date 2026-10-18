using Godot;

namespace QuizParty.Presentation;

/// <summary>Device-local presentation only; never influences rules or host clocks.</summary>
public sealed record PresentationPreferences(bool Sound = true, float Volume = 0.65f,
    bool ReducedMotion = false, bool LargeText = false, bool HighContrast = false)
{
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
        if (sound.VariantType != Variant.Type.Bool || motion.VariantType != Variant.Type.Bool ||
            text.VariantType != Variant.Type.Bool || contrast.VariantType != Variant.Type.Bool ||
            volume.VariantType is not (Variant.Type.Float or Variant.Type.Int) ||
            !float.IsFinite(volume.AsSingle()) || volume.AsSingle() is < 0 or > 1)
        { GD.PushWarning("Presentation settings invalid; using defaults."); return defaults; }
        return new(sound.AsBool(), volume.AsSingle(), motion.AsBool(), text.AsBool(), contrast.AsBool());
    }

    public Error Save(string path = "user://presentation.cfg")
    {
        using var config = new ConfigFile();
        config.SetValue("ui", "sound", Sound);
        config.SetValue("ui", "volume", Volume);
        config.SetValue("ui", "reduced_motion", ReducedMotion);
        config.SetValue("ui", "large_text", LargeText);
        config.SetValue("ui", "high_contrast", HighContrast);
        return config.Save(path);
    }
}

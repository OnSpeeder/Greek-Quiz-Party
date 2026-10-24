# Settings study 03 — vector recreation

Self-contained Inkscape artwork following the supplied settings reference and
the current English mockup brief. All illustrations, including both mascots,
are vector paths; there are no embedded or linked raster images.

## Deliverables

| File | Purpose |
| --- | --- |
| `settings-study-03.svg` | Editable 2800 × 1400 sheet; landscape left, portrait right |
| `settings-study-03-outlined.svg` | Same sheet with all lettering converted to paths |
| `settings-landscape.svg` | Editable, exact 1920 × 1080 / 16:9 canvas |
| `settings-portrait.svg` | Editable, exact 675 × 1200 / 9:16 canvas |
| `settings-landscape-outlined.svg` | Portable landscape lettering |
| `settings-portrait-outlined.svg` | Portable portrait lettering |
| `*.png` | Inkscape rendered previews at the respective document dimensions |
| `validation.json` | Structural checks, dimensions and renderer version |

The editable masters use installed **Arial Rounded MT Bold** for controls and
**Impact** for dimensional titles. Use the outlined variants where those fonts
are unavailable. Keep the editable originals for copy changes.

## Layers and export

Open the editable master in Inkscape. Landscape and portrait are independent
top-level layers. Their child layers separate the stage, frames, navigation,
title, controls, actions, pedestal and mascots. Controls have individually
identified track, fill and thumb groups. Examples:

- `btn_back`, `btn_reset_all`, `btn_privacy_policy`, `btn_credits`, `btn_close`
- `tab_audio`, `tab_gameplay`, `tab_help_legal`
- `slider_music_track`, `slider_music_fill`, `slider_music_thumb`
- `slider_sfx_track`, `slider_sfx_fill`, `slider_sfx_thumb`
- `toggle_music`, `toggle_sfx`, `toggle_voice_over`, `toggle_haptic_feedback`
- `portrait_slider_music`, `portrait_slider_sfx`, `portrait_toggle_sfx`
- `portrait_language_selector`, `flag_uk`, `flag_us`, `btn_reset_to_default`
- `mascot_blue`, `mascot_blue_glasses`, `mascot_blue_arms`, `mascot_blue_paws`
- `mascot_orange`, `mascot_orange_wave`, `mascot_orange_face`

For a transparent engine texture, select the group in Inkscape's Export panel
and export **Selection**, or use:

```powershell
inkscape settings-study-03.svg --export-id=btn_reset_all --export-id-only --export-type=png --export-filename=reset-all.png
```

The original SVG contains SVG blur filters for cast shadows. Inkscape's PNG
exports bake those effects. Direct SVG import into an engine may render filters
or text differently; verify that import, or use the outlined source / PNG
selection export. Runtime import has not been tested for this art study.

## Reproduction and verification

Run `python scripts/create-settings-vector-study.py` from the repository root
to regenerate the three editable SVGs. Render with Inkscape 1.4.4. The portable
versions were produced with `--export-text-to-path --export-plain-svg`.

All six SVGs were parsed and checked for unique IDs, complete local references,
zero raster images and no external dependencies. All three PNGs were rendered
and visually inspected; the portable sheet was also rendered and compared with
the editable sheet. Both exact aspect ratios were checked. `git diff --check`
passed for this change.

This is a visual deliverable. The requested music, narration and haptic controls,
English labels, flags and values are illustrative artwork. It does not change
runtime behavior, production localization, phase acceptance or product scope.
The existing settings study and runtime files were preserved.

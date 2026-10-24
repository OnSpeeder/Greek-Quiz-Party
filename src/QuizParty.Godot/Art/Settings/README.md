# Settings artwork

## Integrated Inkscape study 02 — 2026-10-19

The current runtime frame/card, blue action buttons, arrow tabs, spectrum slider
and pedestal skins derive from `docs/design/settings-study-02/settings-study-02.svg`.
`scripts/export-settings-study-skin.py` reads that Inkscape master's gradient
definitions and produces text-free scalable components. The shared vector builder
now invokes this derivation last, so regeneration preserves the integrated skin.
Frame corner slices are 44px with 40-unit content padding to keep rivets away from
live text. Arrow tabs and reset buttons have dedicated Godot theme variations.
Character atlases and native localized lettering remain separate from the skins.

The mockup's illustrative music/voice/haptic controls are not fabricated runtime
features. Working SFX, language, accessibility and help/reset controls use the new
skin. All older provenance and raster master notes below still apply.

Original UI skin and two original mascot atlases produced on 2026-10-18 for the
Cartoon Showtime settings page. Localized text and interactions remain native
Godot controls. The supplied composite reference is kept outside runtime assets
in docs/design/concepts; no portion of it was copied into production textures.

## Editable vectors

All .svg files in this directory are the editable, self-contained vector masters
and production imports. Open them directly in Inkscape. Reproduce them with
scripts/build-settings-vectors.ps1 (PowerShell plus Python standard library).
The generator records exact geometry, gradients and export dimensions. Godot
rasterizes SVG on import; PNG exports are unnecessary for these controls.

- frame-main: 256x256; 44px slices; corner rivets remain in the corner slices.
- frame-card: 128x128; 22px slices.
- header-trim: 768x160; horizontal70 / vertical18 slices; no baked lettering.
- button-{normal,hover,pressed,active,disabled,danger}: 192x96; 24px slices.
- tab-{normal,active}: 256x112; 24px slices.
- switch-{on,off}: 120x56 complete static exports; switch-track-{on,off} and
  transparent switch-space support the native CheckButton's sliding-thumb view.
- slider-{track,fill}: 128x24; 8px slices. Thumb idle/pressed/disabled: 48x48.
- icon-{back,close,volume-high,volume-low,mute,gear,language,help,controller}: 32x32.
- mascot-plinth: 512x180. sparkle-gold: 32x32.

Normal/hover/pressed/active/disabled skin resources and native focus rings are
wired through SettingsSkin. High contrast uses plain native surfaces instead.

## Raster mascot atlases

mascot-blue.png and mascot-orange.png are transparent 2x2 pose sheets generated
with the built-in image generation tool. Original tool outputs are retained in
the user's generated_images folder; these production copies are self-contained.
They are original raster masters, not layered Blender/Inkscape character files.
No editable layered character source is claimed. Runtime AtlasTexture regions
use half the imported width/height, preserving the genuine alpha channel.
Final dimensions: blue 1254×1254; orange 1261×1247. Both have transparent corners
and fully clear central horizontal/vertical seam samples (alpha >20 count: zero).
The blue sheet was regenerated to repair a gutter crossing before production use.

| Cell | Blue glasses mascot | Orange mascot |
| --- | --- | --- |
| Top left | Idle | Idle |
| Top right | Blink | Blink |
| Bottom left | Ears covered | Wave |
| Bottom right | Celebrate | Celebrate |

SettingsMascot uses a shared atlas view per node, a breathing tween and a blink
 timer. Reduced motion/high contrast stops movement immediately. Orange waves on
portrait open; blue covers ears on mute, either celebrates on an audible test.
All decoration ignores input and lives in a reserved bay outside control bounds.

## Final built-in prompt set

### Blue atlas

Use case: stylized-concept. Asset type: transparent game sprite atlas for QuizParty settings, one 2x2 sheet of FOUR poses of the SAME cyan-blue fluffy cartoon monster with thick dark purple round glasses and a small quiff, matching the blue character in the supplied supporting identity reference. Four equal square cells in exact 2x2 grid, generous transparent padding, no grid lines. Top left friendly seated idle eyes open; top right seated blink eyes closed; bottom left covering own ears with both hands (glasses retained); bottom right cheerful celebration hands up. Full body with tiny feet, consistent proportions, seated root at same position in every cell. Polished hand-painted 2D cartoon game art, saturated cyan fur, navy outlines, soft ivory belly, expressive face. Transparent background with real alpha, no scenery, no podium, no text, no border, no UI, no shadow rectangle. All four isolated silhouettes completely within their own cells. Supporting input is identity/style reference, not edit target. Create original consistent poses.

### Orange atlas

Use case: stylized-concept. Asset type: transparent 2x2 game sprite sheet for QuizParty settings. Supporting input identity/style reference: use the orange/yellow quiff-haired whimsical monster from the crew. FOUR full-body poses of SAME orange monster, each in one equally sized square cell on exact 2x2 grid. Top left idle friendly seated smiling; top right seated blink eyes closed; bottom left seated waving one hand; bottom right seated celebration both hands up. Consistent proportions/pivot/foot baseline within each cell, fluffy golden-orange fur, ivory belly, dark violet outlines, polished hand-painted 2D cartoon console game style. Huge generous transparent gutters and margin, each whole silhouette inside its own cell. Genuine alpha transparent background, no grid lines, no text, no UI, no background, no podium, no shadow rectangle. Keep recognizable character identity, vary only pose/expression.

### Blue atlas registration repair (final production copy)

Use case: precise-object-edit. Edit target is the attached blue monster 2x2 sprite sheet. Preserve all four poses, colors, face identity, glasses, texture, expressions, and genuine alpha transparency. Fix ONLY production sprite registration: place the four FULL character silhouettes in four equally sized quadrants of a SQUARE transparent canvas, each sprite reduced to fit within the central 70% of its cell, with 15% fully transparent padding on every side of EVERY cell. The vertical and horizontal central seam must have a wide fully transparent gutter. No part of any pose may cross into a neighboring cell. Equal square cells, exactly two rows and two columns. Do not crop any hair, hands or feet. No labels, no outlines around cells, no grid, no background. Retain top-left idle, top-right blink, bottom-left hands over ears, bottom-right celebration.

# Living-show benchmark assets

Created 2026-10-26 for QuizParty. Status: benchmark candidate, awaiting human quality review.

- `blue-puppet.png`, `orange-puppet.png`: built-in image generation, based on the
  existing project `Art/showtime-crew-v2.png`; preserve blue/orange identities.
  Six-cell 1536×1024 RGBA atlases, consumed through trimmed Godot AtlasTextures.
  Actual zero-alpha area: blue 44.2%, orange 47.8%. Originals remain in Codex generated_images.
- Blue received a transparency-cleanup edit with the built-in tool; no manual painting claimed.
- `reveal-sting.wav`: original deterministic synthesized stereo 48 kHz PCM,
  authored by `scripts/build-show-audio.py`. No samples, voices or downloaded music.
  5.2 seconds, peak normalized to -3 dBFS before user volume. Listening approval remains open.
- Stage, font and theme reuse the existing project assets and their existing provenance.

## Blue generation prompt

Use case: identity-preserve. Create a production 2D cutout puppet asset sheet for QuizParty, using ONLY the BLUE furry monster with purple round glasses in the reference. Preserve blue tufted fur, glasses, large expressive eyes, ivory belly and polished illustrated rendering. Transparent background. 1536x1024 landscape sheet, exactly 3 columns by 2 rows, each cell separated by generous transparent gutters, no labels or grid lines. Top row: three separate complete HEADS including hair and glasses only, same scale, frontal slight three-quarter facing right: col1 friendly knowing smile; col2 eyes closed delighted grin; col3 surprised wide eyes open mouth. Bottom row: col1 headless armless pear-shaped blue torso with ivory belly and two small feet (whole silhouette); col2 detached left furry arm with open gesturing hand; col3 detached right furry arm with open presenting palm. Heads without neck or torso. Arms have round concealed shoulder joints and complete fingers. All six parts entirely inside their respective equal cells. Smooth clean alpha edges; rich shaded fur, consistent warm upper-left lighting, bold readable silhouettes. No backdrop, shadows cast outside parts, text, extra objects, duplicate figures, assembled character. This is a reusable character rig sheet not a mockup.

## Blue cleanup prompt

Remove all blue gradient background and glowing haze to genuine transparent alpha.
Preserve six parts unchanged, exact layout and proportions, clean alpha around fur,
glasses, fingers and feet. No baked background or checkerboard.

## Orange generation prompt

Production animation sprite atlas, actual TRANSPARENT ALPHA background, no colored background or glow. Use ONLY the ORANGE fluffy monster third from left in reference. Preserve bright golden orange tufted fur, ivory belly, reddish brown eyes, two little fangs, cheerful round identity. Exactly six isolated puppet parts in three equal columns by two rows on 1536x1024. Top row: three complete heads only, identical scale and slight three-quarter view facing LEFT: left cell confident happy smile; middle cell shocked wide eyes and small round open mouth; right cell sheepish sideways smile with raised eyebrow. Bottom row: left cell headless armless pear-shaped furry torso with ivory belly and two small feet; middle cell separate left arm with open hand; right cell separate right arm with open palm. Clear transparent gutters, every part entirely inside own cell, no overlaps. Rounded shoulders for rig joints. Rich polished hand-painted cartoon rendering like reference, clean silhouettes. NO TEXT, no grid, no scenery, NO BACKDROP, no cast shadows outside parts. All empty space must be transparent.

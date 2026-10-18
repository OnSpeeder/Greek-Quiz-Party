# Showtime v2 artwork

Created on 2026-10-18 with the **built-in image generation tool**, following the
user-selected Cartoon Showtime direction. These are background/character assets;
all titles, questions, answers, controls, timing and scores are native Godot UI.
No generated question content or editorial review was added.

| Production file | Output | Use |
| --- | --- | --- |
| showtime-stage-v2.png | 1024×1536 RGB | Portrait stage |
| showtime-stage-wide-v2.png | 1672×941 RGB | Landscape stage |
| showtime-crew-v2.png | 2172×724 RGBA | Home ensemble and atlas-based player cards |
| settings.svg | 28×28 SVG | Native, hand-authored settings symbol |

The PNGs are copied into this project from the built-in tool's generated-images
directory. Originals were retained. The character asset has genuine alpha
(range 0–255). `GameArt` selects atlas regions without changing the source image.
High contrast replaces stage artwork with a plain dark background. The old
showtime-crew.svg remains as a historical asset, not the current game presentation.

## Final prompt set

### Portrait stage

Use case: stylized-concept. Production game BACKGROUND asset for QuizParty, a premium playful Greek-first cartoon party trivia game. Create a polished 2D illustrated TV game-show stage in a portrait 2:3 canvas, 1024x1536 if possible. NOT a UI mockup: absolutely NO lettering, logo, text, numbers, buttons, cards, screens, answer boxes or interface. Deep midnight navy and aubergine stage, elegant curved purple proscenium arch at top and slim theatrical columns at outer edges, cyan and warm magenta spotlights near top outer corners, a few tiny golden comic sparks at margins, low rounded stage risers at bottom in deep indigo with cyan/gold edges. Premium expressive cartoon console game environment, clean confident illustrated shapes, subtle painterly polish, appealing dimension, not flat geometric wireframe. Upper 15% can have bright theatrical architecture. Central 70% is a very calm and dark navy/purple uninterrupted negative space for readable live Godot gameplay text layered later. Avoid busy central scenery, avoid harsh bloom or flashy casino look, no question-specific objects or answer hints, no astronomy or factual subject matter. Bottom 15% has a gently curved stage podium and restrained floor depth. Lighting must frame a UI without overpowering reading. This is reusable production artwork, no baked-in interface, no characters.

### Character ensemble

Use case: stylized-concept. Production transparent 2D game mascot asset for QuizParty, a premium family-and-friends cartoon trivia TV game show. A horizontal group portrait of FOUR original appealing colorful monster contestants, shown waist-up in four clearly separated equal-width zones on transparent background. Pink fluffy expressive creature with two short rounded horns waving and huge curious eyes; cyan-blue rounded geek creature with thick dark round spectacles and one raised eyebrow; warm orange-yellow small rounded creature with a fun quiff laughing; friendly lime-green creature with tiny backwards coral baseball cap giving a thumbs up. Distinct original designs, avoid copying established characters. Wide 3:1 composition, all four equal prominence and size, friendly mischievous personality, crisp hand-painted 2D animation game art with clean dark violet outlines, saturated pink cyan golden-yellow green palette and restrained rim light, expressive polished large faces. Keep whole silhouettes inside image with generous transparent gaps between characters and transparent padding at outer edges. No text, numbers, logos, signs, buttons, podiums, background, floor, drop-shadow rectangle, scenery or baked UI. No low-detail geometric placeholder faces. Readable at mobile size, playful but not preschool. This is an isolated sprite group with real alpha transparency intended to layer above a navy game-show stage.

### Landscape stage

Use case: stylized-concept. Production landscape BACKGROUND asset for QuizParty premium cartoon trivia TV game show. 16:9 wide image 1536x864 or 1920x1080. Fully illustrated polished 2D game environment: deep midnight navy and purple stage framed by slim gold-edged violet theatrical columns at left and right, curved proscenium across TOP outer border, small cyan and magenta stage spotlights at top corners. Bottom 15% contains a low curved indigo showtime podium with restrained cyan and warm gold edge lights. Refined hand-painted animation-style game art with playful theatrical personality, dimensional polished shapes. Central 70% calm uninterrupted very dark navy/aubergine negative space for live gameplay content to be layered later. Bright architectural detail stays only in the outer 10% of edges. No text, logos, signs, buttons, answer panels, screens, interface, characters, astronomical objects or objects that could hint at trivia answers. No glossy casino look, excessive bloom, flashing or photorealism. This must look like a premium family party-game stage rather than an office app background. No baked-in UI.

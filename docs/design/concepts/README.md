# Question screen visual exploration — 2026-10-17

Status: user selected **concept B** on 2026-10-17. See
[the chosen visual direction](../VISUAL_DIRECTION.md). No gameplay/UI implementation changed.
Generated with the built-in image generation tool. Both images use the same sample
Greek question, answer grid, countdown and player scores to compare directions.

- `cartoon-chaos-quizparty-v2.png`: bright illustrated cartoon-heavy treatment.
- `cartoon-showtime-quizparty-v2.png`: selected dark stage/game-show treatment.

Both current concepts carry the QuizParty name. The original renders are retained
in ignored `artifacts/before-quizparty-rename/concepts/` as historical references.
The prompts below use the current brand; the branding edits were made with the
built-in image generation tool, preserving the screen layout and illustrations.

Branding-edit prompt: replace only the upper-left logo with the exact name
"QuizParty", removing the old geographic qualifier. Preserve the style, layout,
Greek question/answers, players, scores, timer, characters and background.

Review notes: both are visual concepts, not final layouts. Question-specific artwork
must be replaced with generic category decoration during implementation so it cannot
hint at the answer (the first image's prominent red planet is unsuitable during this
sample question). Generated progress dots/lettering/spacing need deterministic UI
implementation and accessibility checks. The second image is glossier than requested;
reduce reflections/glow if this direction is chosen. Do not treat these raster images
as the actual UI or accept the sample question into reviewed production content.

## Generation prompts

### A

Use case: ui-mockup. Create ONE polished 16:9 landscape game-screen concept image, straight-on flat screen, filling the entire image, no device frame, no perspective. This is a Greek-first Windows/Android local party trivia game called QuizParty. A TV/desktop public question screen, viewed by friends and family. Professional, distinctive, playful 2D art that can realistically be built in Godot; excellent Greek typography, strong visual hierarchy and generous spacing. Illustrate the same fixed layout for a fair visual comparison: small wordmark QuizParty at top left; centered top progress "ΕΡΩΤΗΣΗ 4 / 10"; category pill "ΕΠΙΣΤΗΜΗ"; large centered question panel in the upper-middle; a large round countdown badge on its upper right reading "12"; four equally sized answer panels in a spacious two-column, two-row grid in the middle-lower screen; a bottom strip showing four small original expressive cartoon player avatars, names and scores. Text must be exact, readable, Greek with accents. Question: "Ποιος πλανήτης είναι γνωστός ως «Κόκκινος Πλανήτης»;". Answer panels: "Α  Άρης", "Β  Αφροδίτη", "Γ  Δίας", "Δ  Κρόνος". Bottom names and scores: "Έλενα  1250", "Νίκος  1000", "Μαρία  850", "Πέτρος  700". All four answers equally neutral: no correct answer revealed, no selection or green correctness highlight. No personal secret missions, card hands, or controller-only controls on this shared screen. No clutter over question/answers, no tiny labels, no photographs, no imitation of existing game brands, no watermark. The reading area must be calm and clear even when decorative edges are lively. This is a concept direction, not a production screenshot.
VARIANT A — cartoon-heavy game show, 75% cartoon party / 25% broadcast structure. Small tasteful external concept tag "A · CARTOON CHAOS" in the top margin. Warm buttery yellow and pale lavender backdrop; deep plum/navy outlines and text; punchy coral, cyan and violet accents. Tactile chunky rounded panels, hand-drawn but precise shapes, flat illustrated highlights and offset shadows, small comic starbursts and illustrated motion marks confined to outer corners. Four avatars are quirky geometric cartoon creatures with expressive faces, friendly but mischievous and age-inclusive. Main question panel is light cream. Answer panels are light pastel with consistent dark text, prominent A/B/Γ/Δ corner markers and generous padding. Gentle asymmetry in decoration only; question and answer grid remains aligned. Premium editorial cartoon illustration, coherent vector-like graphics, no excessive confetti. Make this stylish and playful, never preschool-like.

### B

Use case: ui-mockup. Create ONE polished 16:9 landscape game-screen concept image, straight-on flat screen, filling the entire image, no device frame, no perspective. This is a Greek-first Windows/Android local party trivia game called QuizParty. A TV/desktop public question screen, viewed by friends and family. Professional, distinctive, playful 2D art that can realistically be built in Godot; excellent Greek typography, strong visual hierarchy and generous spacing. Illustrate the same fixed layout for a fair visual comparison: small wordmark QuizParty at top left; centered top progress "ΕΡΩΤΗΣΗ 4 / 10"; category pill "ΕΠΙΣΤΗΜΗ"; large centered question panel in the upper-middle; a large round countdown badge on its upper right reading "12"; four equally sized answer panels in a spacious two-column, two-row grid in the middle-lower screen; a bottom strip showing four small original expressive cartoon player avatars, names and scores. Text must be exact, readable, Greek with accents. Question: "Ποιος πλανήτης είναι γνωστός ως «Κόκκινος Πλανήτης»;". Answer panels: "Α  Άρης", "Β  Αφροδίτη", "Γ  Δίας", "Δ  Κρόνος". Bottom names and scores: "Έλενα  1250", "Νίκος  1000", "Μαρία  850", "Πέτρος  700". All four answers equally neutral: no correct answer revealed, no selection or green correctness highlight. No personal secret missions, card hands, or controller-only controls on this shared screen. No clutter over question/answers, no tiny labels, no photographs, no imitation of existing game brands, no watermark. The reading area must be calm and clear even when decorative edges are lively. This is a concept direction, not a production screenshot.
VARIANT B — game-show-heavy cartoon hybrid, 65% broadcast stage / 35% cartoon personality. Small tasteful external concept tag "B · CARTOON SHOWTIME" in the top margin. Deep midnight navy and aubergine stage background; restrained cyan and magenta edge lighting; warm gold timer accents; subtle broad spotlights directed toward central panel, no blinding glow. Keep original expressive rounded geometric cartoon creature avatars, matching the friendly mischievous age-inclusive spirit. Clean confident geometric panels with restrained rounded bevels and subtle depth rather than realistic 3D. Crisp bright question text on a dark plum central panel; equally neutral dark answer panels with clear white text, distinctive letter markers and restrained bright border accents. Elegant scoreboard rail at bottom, punchy but legible. Decorative comic spark shapes and avatar facial reactions bring personality at the edges. Premium animated TV game-show art direction, strong readable 2D interface, no casino aesthetic, no metallic realism, no constant visual chaos.

# Chosen visual direction — Cartoon Showtime

Selected by the user on 2026-10-17: **concept B**, the dark TV game-show stage
with expressive cartoon avatars.

Reference: [cartoon-showtime-quizparty-v2.png](concepts/cartoon-showtime-quizparty-v2.png).
This is the visual target for future design work, not a finished production UI.

The game name is **QuizParty**. Use this exact spelling in titles and branding;
Greek remains the primary language rather than part of the product name.

## Visual principles

- Midnight navy and deep purple stage, with cyan, magenta and warm gold accents.
- Clear, spacious question panel and large answer panels with strong contrast.
- Bold, readable typography with full Greek character and accent support.
- Rounded, expressive cartoon avatars and playful card illustrations.
- Restrained lighting and glow; avoid relying on glossy reflections for polish.
- Calm reading/answering states; expressive reactions during reveals, card use
  and celebrations. Respect reduced motion and avoid color-only state cues.
- Generic category decoration during questions. Artwork must not suggest the
  correct answer. The sample concept's astronomy decorations are not mandatory.

## Platform and implementation boundaries

Settings-specific composition, skin, responsive layouts and asset production are
specified in [SETTINGS_PAGE.md](SETTINGS_PAGE.md), incorporating the user's
2026-10-18 settings reference. This supplements the shared direction; it does
not mark the settings redesign implemented or accepted.

- Shared TV/desktop screen emphasizes questions, countdown, reveals and scores.
- Phone layouts prioritize readable private controls and touch-friendly targets.
- Keep personal cards and secret missions private according to product/rules.
- Build responsive Godot UI with localized text and reusable components; do not
  use the generated mockup as a single baked interface texture.
- Start with 2D graphics; use Blender selectively when a specific asset benefits.
- Shared palette: navy #0F0A26, plum #1E1442, gold #FFC83B; answers coral
  #FF4B6E, blue #2B95FF, amber #FFB800, emerald #1AD598.
- Typography: bundled Comfortaa at weight 700, with verified Greek accent coverage.
- Reuse illustrated stage background and transparent cast cutouts; the wide host
  shows cast above the answer grid, while portrait prioritizes controls.
- Require actual viewport inspection beside the concept. Automated import/tests
  establish technical validity, never human visual approval.

Selecting this direction does not advance the implementation phase. Complete the
Phase 01 Windows/Android LAN spike before substantial visual production, as
required by AGENTS.md. Product scope and game rules remain owned by their existing
documents.

## Eight-character participation catalog

Stable character identities are Pink, Blue, Orange, Green, Purple, Yeti, Coral and
Teal. Preserve the original atlas and use the additional transparent atlas for
IDs 4–7. Do not recolor/reassign a player when roster ordering changes. Occupied
portraits are disabled and greyed; selection includes a check/accessibility state.
Discovery/PIN/identity use the same chunky surfaces and Greek display typography.

# Presentation and device settings

The first mobile candidate failed the user's visual QA: it looked like an app,
not a game. The replacement follows Cartoon Showtime with illustrated portrait
and landscape stages, expressive characters, bold type and framed answer panels.
The replacement is a review candidate; **visual/accessibility sign-off is open**.
Artwork and exact built-in generation prompts are in `src/QuizParty.Godot/Art/README.md`.
Godot's bundled font renders Greek; no font/audio/plugin dependency was added.

## Layout and feedback

- Logical canvases: 480×800 portrait and 1152×648 landscape, expanded for other
  aspect ratios. Containers, wrapping, vertical scrolling and Android safe-area
  insets keep controls in the viewport. Answer grid switches at 700 logical units.
- Buttons/inputs have at least 64 logical-unit height and density-aware 48dp
  Android targets, keyboard focus outlines,
  labelled inputs and scroll-to-focus behavior. Large text increases default
  type from 22 to 27 and scales explicit headings by 20%.
- Countdown includes remaining seconds, a proportional bar and a textual warning
  at five seconds. It only estimates presentation from the host snapshot; the
  host still determines deadlines and scoring.
- Accepted own selections and revealed correct answers have explicit text cues.
  Correctness cues only use revealed host data. Public results emphasize the
  winner and totals, with detailed statistics below in the scroll view.
- Cards/missions initially collapse on **all** devices. Tap the labelled button
  to open them. Existing local-player handoff/privacy curtains remain immediate.
- Home offers separate create/join paths. Setup fields are shown only for the
  chosen path; manual IP and optional PIN remain available. The waiting room uses
  character player cards with individual readiness; host rules start collapsed.
- Confidence uses native ×1/×2/×3 game chips with a textual risk explanation.
  Results show character score cards; detailed stats are expandable. New party
  returns through a normal transport shutdown. No authoritative rule changed.

## Settings

The 2026-10-19 Inkscape study is now integrated into the native settings view:
blue/gold dimensional live title above the frame, arrow sidebar tabs, tighter
gold/purple inset cards, spectrum volume track, larger landscape mascot and
desktop credits/privacy/reset action row. Portrait keeps stacked scrollable cards
and the waving mascot bay; larger text/high contrast preserve accessible controls.
`scripts/export-settings-study-skin.py` derives the skins from the editable master.

The next settings-page design and production asset plan are defined in
[`design/SETTINGS_PAGE.md`](design/SETTINGS_PAGE.md), integrating the user's
2026-10-18 illustrated reference with the existing Cartoon Showtime direction.
The redesign is implemented as a review candidate in `SettingsPanel.tscn` and
its C# view. Landscape uses left tabs and a blue mascot; portrait uses stacked
scrollable cards and a small orange mascot in a separate footer bay. Editable
gold/purple SVG skins and original transparent pose atlases are documented in
`Art/Settings/README.md`. No account options or new audio services were added.

Open **Ρυθμίσεις / Settings** from the top of the menu or lobby/match screen.
Sound effects, volume, reduced motion, larger text, high contrast and Greek/English
menu language save locally
to `user://presentation.cfg`. Invalid configuration falls back to defaults and
logs a warning; failed saves show a message and retain the in-memory preference.
Settings hide scene controls and isolate focus while open. Escape, Android Back
or Return to game closes settings. **Opening settings does not pause the match.**
Back first returns from a detail page or reset confirmation. Help & Legal contains
offline credits (including engine component notices/licenses), privacy information
and About with actual engine/build metadata. Reset asks for confirmation and resets
only presentation preferences; Cancel is initially focused. No music, narration,
haptic or screen-shake switches are shown without working underlying features.

Short original synthesized cues cover taps, accepted card use, reveal and final
results. Muting stops current audio immediately. No ticking loop, correctness
sound before reveal, background music, flashing or camera shake was added.
Public text fades last 160 ms and never block input. Reduced motion immediately
cancels fades and displays full-opacity text. High contrast removes stage beams.
Settings add a brief opening tween, sliding native switches and decorative mascot
blink/breathing/reactions. Reduced motion stops these immediately. High contrast
also replaces illustrated settings trims with plain outlined surfaces.

## Reproduce local captures

After building/importing the project:

```powershell
./scripts/capture-presentation.ps1 -View Menu -ReducedMotion
./scripts/capture-presentation.ps1 -View Lobby -Width 420 -Height 900 -LargeText
./scripts/capture-presentation.ps1 -View Create -Width 420 -Height 900
./scripts/capture-presentation.ps1 -View Join -Width 420 -Height 900
./scripts/capture-presentation.ps1 -View Settings -Width 420 -Height 900 -LargeText -HighContrast
./scripts/capture-presentation.ps1 -View Settings -SettingsSection Gameplay
./scripts/capture-presentation.ps1 -View Settings -SettingsSection Help -Locale en
./scripts/test-android-presentation.ps1 -StandardAppearance
./scripts/capture-match-presentation.ps1 -Phase QuestionActive -Strategy
./scripts/capture-match-presentation.ps1 -Phase GameOver -Strategy
```

The helper captures the actual Godot viewport in ignored `artifacts/phase10-*`.
Debug-only `--ui-*` launch options preview preferences without saving them.
Godot movie mode uses its own fixed canvas and is unsuitable for portrait layout
evidence; actual captures use `GetViewport().GetTexture().GetImage()` instead.
Movie mixed-audio recording can still verify nonzero cue output and silent mute.

## Deferred gates

The user reopened QA and rejected the initial visual pass on 2026-10-18. Physical
renders, automated keyboard/focus checks and contrast calculations are evidence,
not human touch/listening or assistive-technology approval. Windows Computer Use
capture failed; Android blocked injected taps. No permission or lock setting was
changed. Review the replacement on-device before signing it off.

Android target size uses actual window-pixels / logical-viewport scale. The
CanvasItem screen transform omitted content scaling on the tested phone and
initially enlarged controls incorrectly; that calculation was replaced. The
device capture helper waits for C# startup/display metrics, not the engine splash.
The 1,000+ question target remains deferred; production still has one reviewed
question. No Phase 11 work begins.

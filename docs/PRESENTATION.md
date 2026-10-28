# Presentation and device settings

## Living-show art benchmark — 2026-10-26

Creative direction and future welcome/lobby/reveal/finale treatments are defined
in `docs/design/LIVING_SHOW.md`. First implementation is the separate
`Scenes/LivingShowBenchmark.tscn`, available from debug home via `SHOW_OPEN`.
It contains a fictional answer and two reconstructed blue/orange cutout puppets,
three expressions each, independent head/arm/body joints, an authored 5.2-second
AnimationPlayer clip, a two-leaf answer shutter and original synthesized sound.
It reuses ShowtimeTheme/QuizShowTheme/ShowtimeJuice and the existing backdrop.

No match DTO or authoritative rule changes. The preview does not map these two
actors to actual winners/losers; that integration follows artistic review. Local
preview motion/mute controls do not persist preferences. Source prompts and audio
provenance are in `Art/LivingShow/PROVENANCE.md`. Native text uses localization keys.
Reduced motion exposes the final answer/joke immediately and cancels choreography.
Replaying cancels prior motion/audio; exiting frees scene-owned performance state.

The first mobile candidate failed the user's visual QA: it looked like an app,
not a game. The replacement follows Cartoon Showtime with illustrated portrait
and landscape stages, expressive characters, bold type and framed answer panels.
The replacement is a review candidate; **visual/accessibility sign-off is open**.
Artwork and exact built-in generation prompts are in `src/QuizParty.Godot/Art/README.md`.
Comfortaa Bold (bundled variable font, weight 700) renders Greek and accents.
Its OFL license is shipped and available in Settings credits; no new plugin is required.

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
  chosen path. Participation now uses discovery with optional PIN; manual IP is hidden. The waiting room uses
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

## Conversation review implementation — 2026-10-25

See `PDF_CONVERSATION_REVIEW.md` and `../harness/phase-10-pdf-review-plan.md`.
`QuizShowTheme` owns the palette, bold font, chunky lip/shadow recipe and redundant
geometric answer icons; `ShowtimeTheme` assembles the accessible theme variations.
`ShowtimeJuice` is scene-owned and cancels motion when reduced motion is enabled,
when a control leaves the tree, or when a new animation supersedes it. Answers
remain clickable throughout entrance. Reveal uses only the host's revealed index.
Recap totals interpolate over 0.6 seconds and retain exact authoritative endpoints,
including decreases; repeated snapshots do not restart the animation.

Wide hosts show the illustrated cast above a two-column answer grid. Portrait
controllers keep the question, clock, confidence and four stacked choices; lengthy
risk hints remain accessible via confidence tooltips/accessibility names. Cards and
missions stay behind the existing private toggle. Standings now appear at recap,
not alongside answer reveal. No fixed stage/answer percentage overrides long text
or touch target sizes. Shared-device handoff uses avatar buttons and retains its
immediate privacy boundary. Readiness and team borders supplement existing labels.

Art remains a 2D cutout composition using existing illustrated stage and cast
assets. New portraits, parallax, constant spotlight sweeps and additional external
3D generation services are not prerequisites for this implementation.

## Android rotation and Back navigation — 2026-10-25

Android launches with portrait as the project default, then enables Godot's Sensor
orientation mode. The OS rotates the same running scene; ResponsiveCanvas updates
logical dimensions, safe areas and density-aware hit targets. This respects the
phone's system auto-rotate setting; no device settings are changed. Explicit
portrait/landscape debug capture flags still lock only their preview run.

Android Back and desktop Escape follow the same navigation path: close exit
confirmation, return from a settings detail, close settings, then navigate the
current lobby/menu level. Back collapses optional PIN/rules sections
before leaving their menu. Back from a waiting room disconnects to setup; during
an active match it opens settings with the existing leave-game action, without
stopping the match. Back from the initial screen opens exit confirmation.

The initial screen has an icon-only exit button at the upper-left safe corner,
with localized tooltip/accessibility name. The responsive confirmation asks Yes/No;
No is initially focused, Back cancels it, and only Yes exits. Underlying controls
are hidden to prevent click/focus-through. Portrait and landscape preserve this
modal state. Preview with scripts/capture-presentation.ps1 -View Exit.

## Discovery-first participation — 2026-10-25

Home labels are «Δημιουργία» / «Συμμετοχή». JoinFlow renders rooms, optional PIN
popup, then name/eight-character choice. Back is an icon in the upper-left safe
corner; refresh sits beside «Διαθέσιμες Αίθουσες»; join uses an entering-door icon.
Icons have localized accessibility names/tooltips, without visible action text.
Room rows show name and joined/max; full/started rooms remain disabled.

CharacterPicker disables and dims occupied portraits and marks selection with a
check plus an accessible selected state. The host owns final uniqueness, including
host/local slots. A conflict keeps the name and refreshes choices. PIN errors
return to the room list. Opening PIN hides background browser and navigation
controls; focus remains within its form. The form is centered and scrollable.
Android keyboard height reduces the usable scroll region and keeps focus visible.

The original four portraits plus four original generated cutouts form one stable
catalog. Art/CHARACTERS.md records IDs, atlas layout and exact generation prompt.
Capture rooms/PIN/identity via scripts/capture-join-flow.ps1 at portrait/landscape
sizes, using a real local discovery/PIN host. Debug flags never affect normal play.

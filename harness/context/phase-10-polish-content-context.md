# Phase 10 — Presentation subset context — 2026-10-18

## Replacement delivered for review

The illustrated replacement is implemented and installed on physical Android.
Home/create/join/waiting, native answer panels/confidence chips and character
standings now follow the Cartoon Showtime direction. Portrait and wide stage
assets plus transparent mascot atlas were created with the built-in image tool;
exact prompts/provenance are in src/QuizParty.Godot/Art/README.md. Atlas crops
exclude neighboring characters and avatar identity follows original roster order.

Final verification: 365 tests (252 Core, 100 integration, 13 Godot), clean desktop
build, Windows/Android exports, verified APK signature, packaged Windows and
physical Android 5-player/20-question mixed team/strategy regressions passed.
Actual window/viewport density scaling yields >=48dp targets on the phone.
Final captures include the real exported Greek question and results screens.
Detailed evidence and limitations: docs/PHASE10_QA.md. Earlier pass below is history.

Visual approval and physical usability remain pending. Android reports no supported
Godot accessibility backend; TalkBack/full accessibility sign-off is not established.
The reviewed-question gate remains deferred. No Phase 11, push or publication.

## Latest status — mobile visual QA failed

The user rejected the installed mobile presentation as looking like an application
rather than a game, requesting a graphics/UI overhaul. This supersedes the earlier
deferred QA state: **no visual or accessibility sign-off is granted**. A second
implementation follows the already-approved Cartoon Showtime concept with
illustrated stage/mascot assets and game-focused screen composition. All prior
verification below is historical evidence, not acceptance of the redesign.
Question expansion remains deferred. No Phase 11 work is authorized.

QA also identified density-dependent Android touch targets; these now scale to
at least 48dp while retaining the 64 logical-unit floor. New keyboard focus-cycle,
Escape and Back tests passed. Computer Use failed twice with capture timeouts;
Android rejected injected taps with INJECT_EVENTS, and permissions were unchanged.
Initial automatic Android preview screenshots caught the engine splash because
startup was not awaited; exclude them from layout evidence. The preview helper
now waits for the C# presentation metrics marker before taking a screenshot.

## Approved boundary

The user authorized UI/audio/transitions/accessibility implementation only and
explicitly deferred manual TV/mobile layout QA, certifying no critical
accessibility/touch blockers and the 1,000+ reviewed-question criterion. The
original Phase 10 is therefore **open**, not fully accepted. No Phase 11 work,
push, commit, release signing or publication was performed. Work is local on main.

## Material decisions and files

- `PresentationShell.cs` is scene-owned via `ResponsiveCanvas`, not an autoload
  or mutable global. It applies `ShowtimeTheme.cs`, settings, feedback and static
  `StageBackdrop.cs` decoration. Theme uses Godot's bundled font and the approved
  Cartoon Showtime palette. `Art/showtime-crew.svg` is original vector decoration.
- `PresentationPreferences.cs` uses a local Godot ConfigFile with strict typed
  values and bounded volume. Missing/invalid configuration defaults safely;
  invalid data logs warnings, and save failures are visible in the settings UI.
  Stored at `user://presentation.cfg`; tests use unique temporary paths and clean
  them up. No NuGet/plugin/font/audio/service dependency was introduced.
- Sound: locally synthesized 16-bit sine arpeggios, scene-local audio player,
  modest default volume, immediate mute. Tap/card/reveal/final feedback is generic;
  no hidden correctness information is used. Short public-label fades are 160 ms,
  nonblocking, and immediately cancelled by reduced motion. No game clock pauses.
- High contrast suppresses stage beams; larger text changes theme default 22→27
  and explicit headings by 20%. Settings hide underlying root controls, isolate
  keyboard focus, restore it on close, and handle Escape/Android Back. Android
  safe-area insets are applied to match/lobby margins and the settings shell.
- `Main.tscn`/`AppRoot.cs` replace development-ready copy with a localized welcome
  and primary party action. Technical LAN probe navigation is debug-only.
- `LobbyScreen.cs` adds full field labels and primary host/start styling.
  `MatchPanel.tscn` adds `Answers` GridContainer; answer paths are now
  `Answers/Answer0`…`Answers/Answer3`, including corresponding test updates.
  Grid is one column below 700 logical units and two above. Empty detail rows
  disappear; winner/totals take priority in results. Countdown has seconds, a
  proportional bar and a textual five-second warning. Own selection/correctness
  have text cues; correctness only comes from the revealed host DTO.
- `StrategyPanel.cs` now initially collapses cards/missions for clients as well
  as hosts. This avoids burying phone answers and reduces accidental disclosure.
  The existing test now asserts initial collapse, opens the panel explicitly and
  retains all original card/mission checks. Local handoff behavior is preserved.
- `Localization/ui.csv` and imported translations contain the new Greek/English
  copy. Core, protocol/version and production question content did not change.

## Observed verification

- `dotnet restore QuizParty.sln`, final `dotnet build QuizParty.sln --no-restore`:
  success, zero warnings/errors. Desktop net8 restored after Android export;
  generated Core/infrastructure lockfile churn was restored to the clean baseline.
- `scripts/test.ps1 -IncludeGodot`: 252 Core + 100 infrastructure + 10 GdUnit
  tests passed (362 total), no failures/skips. Three new runtime tests exercise
  preferences roundtrip/invalid values, settings focus/persistence/mute/fade
  cancellation and actual phone/TV container widths with long Greek controls.
  Existing tests retained. Deliberate invalid settings emit two expected warnings;
  the established EditorSettings shutdown_adb_on_exit editor diagnostic remains.
  No orphan-node or new runtime error was observed in the final run.
- `scripts/test-network-match.ps1 -QuestionCount 20 -Strategy -Capture`: Windows
  host plus two clients completed all phases/four rounds with authoritative total
  agreement and duplicate-safe inputs. Final totals Host75731/Anna67286/Maria0.
  Synthetic fixtures only; no production questions generated or approved.
- Windows and Android debug exports succeeded. APK v2 signature verification
  passed. Packaged Windows startup printed `QuizParty: C# startup ready.` with
  empty runtime stderr. Exports retain the known engine teardown diagnostic.
- `scripts/test-network-mixed.ps1 -HostPlayers 2 -ClientPlayers 3 -Teams -Strategy
  -Packaged -Capture`: five logical players, 20 questions; both peers agreed on
  all final state. Team A212846/Team B0. Packaged runtime stderr clean.
- Engine-rendered captures inspected: 1152×648 desktop menu, 420×900 large-text
  menu/lobby, 420×900 high-contrast large-text settings, 800×480 large-text settings,
  portrait active client answers, desktop individual and packaged team results.
  Scroll views retain long content. These are automated visual observations,
  not human interaction/accessibility sign-off or new physical Android evidence.
- Actual engine mixed-audio WAV recording: signed 32-bit peak276887552 for cue;
  muted peak0. This verifies audio output/silence, not real-speaker listening QA.
- `git diff --check` passed. No remote CI run or workflow changes.

## Reproduction and evidence

See `docs/PRESENTATION.md` and `scripts/capture-presentation.ps1`. Debug `--ui-*`
preview flags never persist preferences. Godot movie mode initially produced
fixed-canvas cropped portrait frames; those are not layout evidence. The helper
uses actual viewport PNG capture instead. Movie audio is usable for signal checks.

Ignored evidence: `artifacts/phase10-build-final.log`, `phase10-restore-final.log`,
`phase10-tests-final.log`, `phase10-network-final.log`, `phase10-network/`,
`phase10-packaged-mixed.log`, `phase10-packaged-mixed/`, `phase10-export-*.log`,
`phase10-apk-verification.log`, `phase10-packaged-startup*.log`,
`phase10-audio-verification.log`, `phase10-audio-{tone,muted}.wav`,
`phase10-{menu,lobby,settings}-*/preview.png` and `phase10-diff-check.log`.

## Deferred work

### Inkscape study runtime integration — 2026-10-19

The user requested integrating study02 into the game. Runtime skins derive from
the actual Inkscape master's gradients through export-settings-study-skin.py;
the shared vector builder applies that derivation last. SettingsPanel now has
a dimensional blue/gold native title outside the main frame, gold arrow tabs,
compact inline toggles/spectrum slider, two-column Audio when space permits,
and desktop credits/privacy/reset actions with a larger mascot/pedestal.
Portrait keeps scrollable cards, a framed title and a small waving mascot bay.

Native controls are reparented rather than copied: quick actions move between
the desktop action row and portrait Help card, retaining focus and handlers.
Leave party moves to a compact desktop header action / portrait Help control.
Compact localized labels retain full accessible names. Save feedback replaces
metadata in the footer to avoid growing the modal beyond the viewport. Frame
padding and slices keep text away from rivets. Reduced motion/high contrast,
existing preference keys, language, reset confirmation and privacy remain intact.

Additional assertions cover single action instances, action focus over rotation
and frame bounds with Leave party present. Found/fixed header overflow and a
mascot timer starting while its child was outside the tree during reparent.
Native error-log review also caught stale cached texture handles when reopening
scenes. Skin loads now use page-owned resources and toggles reuse their own
texture references during state updates. Final assertions and native logs pass.
The mockup's music/voice/haptic illustrations remain absent until real services
exist. No Core/protocol/content change. Latest evidence: study integration entry
in build-log.md and docs/PHASE10_QA.md; human acceptance remains separate.

### Inkscape mockup follow-up — 2026-10-19

User rejected the implemented settings UI and explicitly requested Inkscape and
a high-fidelity side-by-side mockup. Delivered `docs/design/settings-study-02/`
with editable SVG, outlined SVG and PNG, using original vector framing and the
existing stage/character illustrations. Accessed configured Inkscape MCP through
local FastMCP stdio; its validate/gradient/convert tools succeeded. Inkscape1.4.4
rendered the previews and outlined export. Exact scope/provenance and reproduction
are in that folder's README. Runtime settings retain their prior implementation
and lack visual approval. No game code changed for this mockup-only request.

### Settings implementation follow-up — 2026-10-18

User authorized UI implementation and asset production after the specification.
`SettingsPanel.tscn` / `SettingsPanel.cs` replace the shell's inline settings
builder. The scene-owned shell still owns local persistence, audio and modal
privacy. No Core, domain, protocol or production question change was needed.

- Delivered 29 original editable SVGs plus original blue/orange four-pose atlases
  in `Art/Settings/`. Vector generator and exact built-in image prompts are in
  the repository. Final blue registration was repaired after seam inspection.
- Landscape tabs select one section; narrow/portrait displays all three cards in
  one scroll. Decoration has a separate bay. Rotation retains the focused
  setting's section, not only the last landscape tab. Insets and density targets
  propagate into all controls, including the header after rotation.
- Existing five preferences remain compatible. Added validated device-local
  `language` key (Greek default; English option), offline credits/engine component
  notices, privacy/About panels and Cancel-first presentation-only reset.
  Literal UI copy uses native translation keys rather than early translated text.
  Host question-pack language and gameplay state do not change.
- Native controls retain keyboard/focus/value semantics; switches animate only
  their visual thumb. Reduced motion cancels tweens/mascot loops; high contrast
  replaces artwork with plain outlined surfaces. Unsupported music, narration,
  haptics and shake controls are omitted.
- Fixed resource lifecycle/allocation issues found in iteration: keep a reusable
  atlas view, recreate it on decoration reparent, dispose owned styles/themes,
  and avoid rebuilding the settings skin on every slider value. Final test
  process exits cleanly; no failing test was removed or weakened.

Reproduction and observed verification: `docs/PHASE10_QA.md`, artwork README and
the settings implementation entry in `harness/build-log.md`. This is a review
candidate, not final human acceptance or completion of Phase 10.

### Settings design follow-up — 2026-10-18

The user supplied an additional settings art/UI prompt and composite image.
Integrated it into `docs/design/SETTINGS_PAGE.md` and linked it from the shared
visual direction, presentation guide and phase plan. Reference retained under
`docs/design/concepts/settings-page-reference.jfif`, outside exported game assets.
Only that composite was supplied; other image filenames in the prompt are not
available assets. Reference provenance is unverified; production artwork should
be original and editable, with localized live text rather than baked labels.

Scope for this follow-up is the requested specification and production asset
plan. Existing five preferences remain required; additional music/narration/
haptics/shake controls require actual services before exposure. The specification
also plans language selection, offline help/legal panels, actual version metadata
and confirmed presentation-only reset. No accounts or game-rule changes. No code,
new production artwork or runtime verification is claimed by this documentation
change. Implementation acceptance is tracked separately in the new specification.

Human TV/mobile readability/touch QA, accessibility blocker sign-off, physical
Android orientation/notch/Back/screen-reader/audio checks and reviewed content
scale remain unclaimed. The content gate still validates exactly one reviewed
Greek question. No full Phase 10 acceptance or release readiness is implied.
Further phase work requires separate user instruction/approval.


### Settings vector recreation — 2026-10-19

The latest user request is an Inkscape SVG recreation of the supplied
dual-orientation reference. Study03 is isolated in docs/design/settings-study-03/
and uses vector stage/mascots rather than embedded raster artwork. It keeps
the requested English copy and illustrative control states. Editable and
outlined master/orientation sources, PNG previews and validation evidence
are delivered. Controls, fills, knobs and mascot parts have distinct IDs.
No replacement of the existing runtime or new product behavior was requested
or implemented. Direct Godot SVG import is unverified; selection PNG exports
were observed and preserve shadow effects. Phase10 acceptance remains open.
# Conversation review — 2026-10-25

- The PDF's proposed Theme/Stage files were tracked empty placeholders. They now
  implement the recipe and scene-owned motion; existing ShowtimeTheme remains the
  preference-aware theme assembler. No Core/protocol changes.
- Comfortaa already existed but was unused. Load its variable font at weight 700,
  with 0.5 emboldening, include OFL in exports/credits, and test Greek glyphs.
- Initial capture before resource import failed to load the font; run Godot import
  before captures. Test builds also need global::Godot.Collections qualification
  because QuizParty.Godot.Tests introduces a sibling namespace.
- Fixed the ordinary wide capture's clipped lower row by reducing cast thumbnails
  to 64. Explicit question/answer font overrides now register their larger-text
  baseline even when assigned after NodeAdded. Reveal explanation gets a surface;
  duplicate status/confidence controls are hidden during reveal.
- Animation state belongs to PresentationShell.Juice, finishes on reduced motion
  and is cancelled on control exit. Wrong-answer dimming remains a static cue.
  Public scores are interpolated only for display, with exact endpoints; repeated
  snapshots reuse rendered standings. Do not infer other players' private answers.
- Keep optional art CLI probes, verified SDK and Compatibility renderer. No tracked
  bin/obj files were found. Keep masked PIN semantics and native layout flexibility.
- See docs/PDF_CONVERSATION_REVIEW.md for the complete assessment and build log
  for verification; human aesthetic/touch approval and content scale remain open.

## Android navigation follow-up — 2026-10-25

- User requested portrait-default automatic rotation, hierarchical Android Back,
  and icon-only home exit with Yes/No confirmation. Plan: phase-10-navigation-plan.md.
- project.godot sets handheld/orientation=1 (portrait). PresentationShell enables
  ScreenOrientation.Sensor at runtime unless a debug preview explicitly locks it.
  Actual Android reports SCREEN_ORIENTATION_FULL_USER; respects OS auto-rotate.
- Shell owns Back routing and exit modal. Lobby handles nested optional sections,
  disconnect-to-setup and in-match settings. Never quit from a non-home screen.
  ExitConfirmation emits events; shell calls Quit only from visible confirmation.
- Android sensor changed the running viewport from portrait to landscape during
  observation. Back, No (stay) and Yes (process exit) were exercised through device
  key input. No global Android settings were changed.
- Build cache caution: Android export restores net9.0 assets; restore before desktop
  build. Source/binary timestamps were inconsistent during this run, so an explicit
  Rebuild was used to refresh the preview assembly. Do not trust stale captures.

## Participation revision — 2026-10-25

- User approved discovery → optional PIN → name/eight unique characters → join;
  then explicitly removed manual-IP UI while retaining transport functionality.
  This supersedes the earlier user/AGENTS requirement to expose manual IP.
- Protocol v7 separates connection-bound two-minute preflight from actual player
  admission. No roster mutation/reservation on PIN success; final hello owns the
  atomic Core character claim. Conflict keeps the connection/name and returns
  current availability; refresh does not extend authorization.
- Typed Core character identity is copied to lobby and match DTOs; departed match
  participants retain their portrait via a fixed match map. Host and local slots
  share the same uniqueness rules. Nullable/default choices exist for retained
  direct/probe APIs, with host assignment; normal UI explicitly selects an ID.
- JoinFlow/CharacterPicker are native components. PIN is a shell-owned centered
  modal, with its own keyboard-safe scroll container; shell navigation/background
  controls are hidden. ResponsiveCanvas reserves keyboard height on Android and
  scrolls focus. Guard keyboard APIs on Windows/headless to avoid engine warnings.
- Generated four additional transparent portraits using built-in imagegen; exact
  prompt/layout/provenance in game Art/CHARACTERS.md. Output was 1254 square, not
  requested 1024; derive 627-pixel quadrants from actual dimensions.
- Existing large-content work was preserved. It exposed a stale greece.json CLI
  fixture and a UI test assuming Athens in every selected question. Updated fixture
  selection and kept the handoff test focused on independent valid submissions.
  Pre-tokenized similarity sets and kept exact duplicate/Jaccard checks, removing
  repeated per-pair token allocations that made room creation take ~66 seconds.
  Boundary regression retains warning/error semantics; no review state changed.
- Initial native ENet test had a mismatched host Transport node name; fixed the test
  harness path (production RPC paths unchanged). UI visibility tests now check
  actual visibility through parent JoinFlow. Failed/timeout logs are retained.
- Android fixture-only issue found while checking UI: MatchProcessProbe treated
  --match-ui-* preview flags as a match-role request, causing an unwanted localhost
  join/timeout when entering Lobby. Restrict it to actual --match-host/--match-join
  flags and cover this with a regression; normal navigation never starts a probe.
- Physical landscape safe-area inset moved Back into the fixed wordmark. Position
  the wordmark after the actual inset-aware Back rectangle instead of a fixed X.
- Physical Android LAN discovery, wrong/correct PIN, name typing with keyboard
  visible, character selection and final join to Windows were observed. No ADB
  network tunnel, device setting or permission change. Temporary debug fixture is
  removed after testing and normal sensor orientation is restored on relaunch.

## Lobby setup revision — 2026-10-25

Approved by the user: host starts unready; three players per row with icon readiness;
header icon actions for game setup and rules; full category/card/mission selection
pages. Difficulty is multi-select in three bands (1–2, 3, 4–5). User explicitly
approved positive base/time scoring multipliers ×1 / ×1.5 / ×2, before confidence,
streaks and cards; wrong penalties remain fixed. FullMatch applies these rules;
the legacy low-level GameSession API can still opt into unscaled scoring.

Selections are copied into immutable Core settings at match start. Deck filtering
(including sudden death and category swaps) keeps only selected difficulties and
categories. Card pools intersect the selected list with aggressive-card permission;
mission assignment intersects selected missions with actual feasibility. Empty card
or mission lists disable awards/assignments. Empty category/difficulty selections
cannot start. Selecting cards/mission pools does not reveal any private assignment.

The roster tile itself toggles readiness for an owned player. Local-player removal
is available when the add/edit local-player controls are open. Existing team
assignment controls remain available in team mode. Pages retain the shared theme,
scene-owned tactile feedback, localized Greek/English and minimum touch targets.
Scroll overflow supports thresholded dragging from buttons and page backgrounds.
No publishing, content review-state changes or phase advance was authorized.

Protocol compatibility advances to v8/app 0.8.0: positive per-question bounds rise
to 2,000 base / 12,000 strategy due to the approved difficulty multiplier. Existing
v7 clients would reject these valid reveals, so admission/discovery must reject
mixed protocol versions. No new private payload is broadcast and manual-IP API
remains intact. See `harness/phase-10-lobby-settings-plan.md`.

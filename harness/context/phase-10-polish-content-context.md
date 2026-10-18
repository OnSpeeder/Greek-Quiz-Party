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

Human TV/mobile readability/touch QA, accessibility blocker sign-off, physical
Android orientation/notch/Back/screen-reader/audio checks and reviewed content
scale remain unclaimed. The content gate still validates exactly one reviewed
Greek question. No full Phase 10 acceptance or release readiness is implied.
Further phase work requires separate user instruction/approval.

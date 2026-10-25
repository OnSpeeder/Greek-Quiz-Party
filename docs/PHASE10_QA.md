# Phase 10 replacement presentation QA — 2026-10-18

**Status: replacement implemented; visual approval and accessibility sign-off open.**
The user rejected the first installed mobile presentation as looking like an
application rather than a game. That candidate failed visual QA. This document
records the replacement's observed checks, not acceptance of its appearance.

## Replacement

Illustrated portrait/landscape Showtime stages and mascot artwork; focused home,
create/join and waiting screens; framed questions and colored answer panels;
compact confidence chips; character standings and collapsed detailed results.
All live text and controls remain native Godot UI. Settings retain mute/volume,
larger text, high contrast and reduced motion. High contrast removes decoration.
Assets and exact built-in generation prompts: [art manifest](../src/QuizParty.Godot/Art/README.md).
Core rules, protocol, host authority and reviewed question content are unchanged.

## Settings implementation follow-up — 2026-10-18

### Latest candidate: Inkscape study integration — 2026-10-19

Following the user's instruction, study02 is integrated into the native settings
page. The current candidate uses its blue/gold title, arrow tabs, gold-riveted
frames, spectrum track, compact controls and bottom action row. Reusable skins
derive from the editable Inkscape master; labels remain localized Godot text.
Supported preferences/help/reset stay functional; mockup-only music/voice/haptic
features are not exposed. Human visual/touch/audio/TV approval remains open.

Additional scene coverage checks desktop action-row / portrait Help reparenting,
one instance per action, focused action retention after rotation and modal bounds
with Leave party visible. These checks exposed and drove fixes for long header
labels and decoration timer lifecycle. Latest logs use the prefix
`artifacts/settings-study-`; earlier settings evidence below describes the prior
candidate, which the user rejected visually.

The integrated candidate passes 369 tests (252 Core + 100 integration + 17 Godot).
Bounds/focus assertions include Leave party and moving the actual reset action
between orientations. Logs are checked for native runtime errors as well as test
assertion results. The mascot timer is guarded against starting during reparent.
Page-owned switch textures avoid repeated loads during preference updates, and
fresh skin resource loads avoid stale C# resource handles when reopening scenes.
Windows debug export/settings capture and Android export/install/portrait plus
landscape renders are recorded in settings-study-export-*.log,
settings-study-packaged{,-errors}.log, settings-study-android-*.log and
settings-study-apk-signature.log. Expected EditorSettings export teardown
diagnostics remain documented. No Core/protocol/question-pack changes.

The additional settings reference is now implemented as a review candidate:
landscape navigation and blue mascot, portrait scrollable cards and orange
footer mascot, original gold/purple SVG skin, animated switches, live Greek/English
menu language, offline help/credits/privacy/About and confirmed presentation-only
reset. Existing sound/volume/accessibility preferences remain compatible.

369 tests pass (252 Core +100 integration +17 Godot), including migration/invalid
locale, reset cancellation/confirmation, nested Back, save failure, muted preview,
motion cancellation, density targets, reflow and retained language-control focus.
Local build is clean. Unsupported music/narration/haptics/shake controls are absent.

Inspected actual engine captures for Greek 1920×1080 Audio, 1280×720 Gameplay,
English 1152×648 Help, portrait 420×900, high-contrast/large-text portrait480×800,
and short landscape800×480. Physical Android portrait/landscape captures were
also inspected in standard and high-contrast/large-text modes. On the 533dpi
phone, minimum targets remain64 portrait/72 landscape logical units (>=48dp).
The high-contrast Back icon was bounded after device capture exposed oversizing.

Evidence: `artifacts/settings-tests-final.log`, `settings-build-final.log`,
`settings-export-{windows,android}-final.log`, `settings-android-*-final.log`,
`phase10-qa/android{,-standard}/`, and `phase10-settings-*/preview.png`.
Packaged five-player mixed local/LAN, teams + strategy,20 synthetic questions:
all peers agree; runtime stderr clean (`settings-network-final.log`).

Asset validation: both PNG atlases have real alpha and clear central seams.
Declared text/surface contrast pairs are4.98:1 or better (body13.65:1;
hover8.02:1; active6.54:1; high-contrast18.23:1). These source-palette checks and
render inspection do not certify assistive-technology support or all device states.
Source assets/final imagegen prompts: `src/QuizParty.Godot/Art/Settings/README.md`.

Human touch/drag/listening/TV readability, full screen-reader acceptance and the
full combination matrix remain open. Credits/privacy copy still needs release
review. Android's accessibility backend still reports unsupported. The settings
overhaul does not complete Phase10 or the deferred reviewed-content target.

## Observed evidence

| Check | Result |
| --- | --- |
| Local tests | 252 Core + 100 integration + 13 Godot = 365 passed; none failed/skipped |
| Final desktop restore/build | Passed, zero warnings/errors |
| Windows and Android debug exports | Passed; APK v2 signature verified; installed and launched |
| Packaged Windows mixed LAN | Five players, two devices, teams/strategy, 20 synthetic questions; matching results |
| Physical Android mixed LAN | Windows host + phone, 2+3 players, 20 synthetic questions; scores/teams/missions/statistics agree |
| Engine-rendered screens | Inspected home, create/join, settings, active question and results; portrait and landscape |
| Physical Android capture | Inspected both orientations for home/settings, plus landscape shared-player match |
| Keyboard/modal runtime checks | Tab stays inside settings; Escape/Back close and restore focus; preferences persist |
| Motion/audio controls | Reduced motion cancels active fades; mute stops stream; human listening pending |

Android density correction uses actual window pixels divided by logical viewport
size. On the observed 533-dpi Android 15 device, portrait scale 3 gives a 64-unit
minimum; landscape scale 2.222 gives 72. Settings targets measured 68×64 and 72×72.
This meets the [Android 48dp target guidance](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views).
Large text, long Greek labels and focus isolation have runtime coverage.

Representative actual exported screenshots:

- `artifacts/phase10-redesign-match-420x900-QuestionActive-packaged/preview.png`
- `artifacts/phase10-redesign-match-420x900-GameOver-packaged/preview.png`
- `artifacts/phase10-qa/android/portrait-menu.png`
- `artifacts/phase10-qa/android/landscape-settings.png`

Logs: `artifacts/phase10-redesign-tests-final.log`, `phase10-redesign-build-final.log`,
`phase10-redesign-export-windows.log`, `phase10-redesign-export-android.log`,
`phase10-redesign-apk-signature.log`, `phase10-redesign-packaged-mixed.log`,
`phase10-redesign-android-match.log` and `phase10-redesign-android-views.log`.
Existing editor shutdown diagnostics (EditorSettings/socket/StringName teardown)
remain in raw logs; the runtime test runner passed. No tests were weakened or skipped.

## Open acceptance checks

- User review of the replacement's visual direction on phone and TV/desktop.
- Physical tapping, scrolling, rotation, Android Back, speaker comfort and TV-distance readability.
- Assistive-technology review: the physical Android runtime reports
  `AccessibilityServer.IsSupported() == false`; TalkBack support is not established.
  Full accessibility sign-off cannot be claimed.

Windows Computer Use capture timed out twice. Android input injection was denied
by the OS. Neither limitation was bypassed, and automated input is not represented
as human usability approval. Screenshots establish rendering, not touch comfort.

Production content remains one reviewed question. Long matches above use explicit
synthetic debug fixtures; the 1,000+ reviewed-question gate remains deferred.
Phase 10 stays open. No Phase 11 work, push or publication was performed.
# Participation revision — 2026-10-25

New review candidate: discovery-first rooms/PIN/identity, eight unique host-owned
characters, icon-only Back/refresh/join, hidden manual-IP UI and keyboard-aware
Android scroll regions. See `harness/phase-10-join-flow-plan.md` and latest build
log for observed tests/captures. Prior visual acceptance status does not confer
approval of this revision. Human touch/accessibility review remains open.

## Lobby/setup viewport review — 2026-10-25

Implementation: `harness/phase-10-lobby-settings-plan.md`. Actual Windows Godot
captures are in `artifacts/lobby-settings/` (480×960 portrait, 1152×648 landscape).

Observed and corrected: initial narrow settings columns; a long cinema label
splitting inside a Greek word; overly tall player tiles; footer clipping in wide
lobby; full card descriptions making both layouts scroll unnecessarily; larger-text
summary links breaking words; and an unattached empty rules-page grid causing an
orphan-node/RID warning. Final focused Godot tests report no orphan warning.

Final observed compositions:
- Eight-player roster: three columns, all eight tiles and actions visible in both
  orientations. Full-tile own-player readiness, check/hourglass indicators and
  Greek names/accents are readable. Header gamepad (match setup), book (rules)
  and existing sliders (device settings) are separate actions.
- Default setup: length, timer, multi-select difficulty multipliers, strategy,
  teams, three selection links and category-icon summary fit both orientations.
- Categories: all 12 selectable pictograms and Greek labels fit portrait and
  landscape. Cards: six choices with concise descriptions fit both orientations.
  Missions: all five choices and objectives fit both orientations. Rules were
  inspected in portrait; the pinned bottom action remains available.
- Large-text portrait setup intentionally uses a single column for selection
  links and scrolls vertically. Dragging from a button is tested to scroll without
  activating it. Do not shrink accessible text to force everything onto one screen.

Runtime evidence is Windows Godot rendering, not a physical Android touch review.
No new APK was installed and no human visual/accessibility acceptance is claimed.
Import emits an engine EditorSettings/android-shutdown-on-exit diagnostic; runtime
captures after the orphan fix have empty error logs. Existing acceptance gates stay
open. Content and editorial review flags were not changed.

## Physical checkpoint before headless-host work — 2026-10-25

Installed a fresh APK on Android 15 model 23013PC75G. Inspected actual portrait menu,
landscape settings and active-match captures; Greek accents and touch controls fit.
LAN discovery, PIN checks, manual-IP regression, reconnect-as-new-identity and
host-exit checks passed in both host directions. A 20-question strategy match with
Android client passed authoritative state/statistics agreement. Evidence and fixed
startup/broadcast/disconnect regressions: `harness/build-log.md`.

This confirms the observed technical scenarios on this device. Human listening,
subjective visual approval and the newly requested tooltip/header/create-flow
corrections remain distinct work; no blanket accessibility certification is made.

## Optional host and compact creation — 2026-10-25

Actual Android portrait/landscape captures cover creation, shared player identity
and eight-player lobby. Inspected Greek labels, all eight characters, fixed submit
controls, hidden scrollbars and separated header actions. Native Windows tooltip
capture reads horizontally; long-text tooltip behavior has a viewport-bound test.
Physical touch verified both creation paths, including name entry with Android
keyboard and initial not-ready player. Ten-question team/strategy LAN matches passed
with Android and Windows each acting as the non-playing host. Logs, captures and
scope limits are recorded in harness/build-log.md. New debug APK installed on the
physical device; temporary launch fixtures are removed after verification.

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

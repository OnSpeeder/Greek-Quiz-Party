# Phase 04 context — One-question playable match

## Authorization and scope
- At user request committed/pushed existing Phase 03 changes as d23468b on main.
  Phase 04 work remains local; no final Phase 04 commit/push performed.
- Reused lobby/ENet and Phase 02 GameSession. Added Core OneQuestionMatch host
  coordinator, explicit match DTOs/MatchClientState, host router bridge and
  composable MatchPanel. No production packs/schema/dependencies/permissions added.
- Single tiny permitted Greek fixture (capital of Greece), host-shuffled four
  answers, 20-second question, Safe x1. Host is a player. No scoring/UI random
  selection on clients. Normal menu Start continues to question, reveal, scoreboard,
  final results. Host advances the last two stages; Back closes peer/returns menu.
- Match stays inside Lobby scene so /root/Lobby/Transport and ENet survive view
  changes. Legacy lobby-only process driver sets PlayMatch=false; normal UI defaults
  true. Existing regression was preserved, not weakened/skipped.

## Timing/privacy/protocol
- Protocol bumped 1 -> 2 (app version 0.2.0): Phase 03 clients cannot interpret
  match messages. Explicit v1 rejection test added. Probe remains separate v1.
- Answer intent has only instance ID/index/confidence; host maps actual sender
  to player and captures monotonic receipt before JSON parse. Core validates
  timing/eligibility/instance/one answer/range/confidence. Exact deadline allowed.
- Existing bounded cache returns identical private ack for same ID/JSON and never
  reapplies scores. Correctness/points/explanation absent from that ack. Active and
  locked match DTOs have null Reveal and zero totals. Client pending controls lock
  until receipt; authoritative locked/late states come from host.
- Poll timer only asks Core to progress: all answers or expired host clock locks,
  next poll reveals/scores once. Frame rate/delta is never used by Core scoring.
  Client countdown is estimated from HostNowTicks + local monotonic receipt only.
- Match and lobby revisions are separate. MatchClientState bounds/validates DTOs,
  rejects wrong sessions, stale/rollback snapshots and premature correctness;
  returns copied arrays. Displayed totals always come from host.
- Initial match eligibility is fixed. A departed player remains unanswered until
  deadline; lobby connected roster still updates. No reconnect/rematch/winner/
  tie-breaker or multi-question scheduling added; later phases own those rules.
- GdUnit's QuizParty.Godot.Tests namespace shadows qualified Godot in test builds;
  use global::Godot.Timer/Time where explicit qualification is required.
  Initial compile issues were fixed; no gates bypassed. A new midpoint test's
  fake elapsed was corrected to 10s for the actual 20s window (750-point assertion
  retained). No failing test was removed, skipped or weakened.

## Physical automation
- Connected Android 15/model 23013PC75G; LAN IPs verified as Windows .105 / phone
  .106 on 192.168.68.0/24. No network tunnel, firewall/VPN or input-injection changes.
- Godot template's own local Android tests confirm exported launcher strips CLI
  extras. Debug-only MatchProcessProbe may read app-private
  user://phase04-test-args.json (4096 bytes/12 bounded flags). Release code never
  reads it. Helper writes it through authorized ADB run-as, launches the normal
  exported alias and drives intents over actual LAN. No production defaults changed.
- scripts/test-android-match.ps1 always removes this fixture/screenshots in finally,
  stops its host and relaunches normal app. File absence and APK signature verified.
  This is physical automated runtime coverage, not manual tapping/UI interaction.

## Observed verification — 2026-10-18 Europe/Athens
- scripts/build.ps1: six projects, zero warnings/errors.
- scripts/test.ps1 -IncludeGodot: 195 Core + 31 integration + 4 scene tests passed,
  none failed/skipped; production rebuild clean. Core Godot-independence test passed.
- Source and packaged host/two-client normal + timeout match checks passed through
  QuestionActive/QuestionLocked/AnswerReveal/Scoreboard/GameOver with matching final
  revision, instance and scores. Explicit wrong/unanswered outcomes and duplicate
  answers checked. Source normal: Anna 993 / Host 995 / Maria 0, final revision 7.
- scripts/test-network-lobby.ps1 and test-network-spike.ps1 passed; smoke main-scene
  startup marker observed. Final Windows and Android debug exports passed.
- Final Android APK installed/launched; signature verifies. Physical correct,
  wrong and unanswered cases all passed against packaged Windows host. Exact
  excerpts/instance IDs/totals recorded in docs/MATCH_EVIDENCE.md (876/849, 876/0,
  876/0 respectively). Phone observed every phase, matching host revision 6.
- Inspected phone active/final and host final viewport captures. Greek content
  and both localized UIs rendered, answer targets readable. Normal phone launch
  restored after testing. No game/network runtime exceptions or engine errors seen.
- Existing editor/export shutdown_adb_on_exit diagnostic persists; not hidden or
  treated as proof of a clean editor log. No content-pack validator run: no JSON
  packs/schema changed; fixture invariants and behavior are covered by tests.
- git diff --check passed; new source/test/script whitespace scan clean. Reverted
  only generated restore/export lock-file churn; dependencies stayed unchanged.

## Boundary
Phase 04 acceptance met on physical Windows/Android hardware; stop. Phase 05
content loading/validator needs separate user approval. Broader device matrix,
manual touch play and full-match/reconnect behavior remain future coverage.

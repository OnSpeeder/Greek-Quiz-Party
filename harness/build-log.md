# Build Log

Append observed implementation and verification evidence here. Plans are not evidence.

## 2026-10-18 — Phase 09 — mixed local/LAN and Team Mode complete

- Baseline Phase 08 pushed as 5268832. Phase 09 changes stay local/uncommitted.
  Lobby keyed by PlayerId with unique connection/slot ownership; every device
  can own multiple players. Independent readiness/answers/cards/missions/stats,
  logical8-player cap and whole-device departure implemented. Two host-assigned
  nonempty teams use checked sums, team ranking/sudden death/shared exhaustion;
  strategy/mission bonuses count and Steal excludes teammates.
- Protocol 6/app 0.6.0 adds opaque controller grouping, slot intents and separate
  private snapshots/receipts per owner. No native connection IDs exposed.
  Duplicate-safe cache supports 2048 requests/2 MiB plus a bounded last record;
  rate 32/s and 16 KiB envelope stay. Existing7000-byte question budget still fits
  populated eight-player team finals. No dependencies/services/GitHub CI added.
- Localized composable roster/team controls and explicit handoff curtain added.
  Owner change/submission hides prior controls; confidence resets to Safe; new
  host session collapses private panel. Shared timer supports 60 seconds. Team
  standings/winners render host data. UI uses containers and 64-unit targets.
- Build clean, zero warnings/errors. Final local tests: 252 Core + 100
  Infrastructure + 7 Godot = 359 passed, none failed/skipped. Existing tests kept.
  New coverage includes 2–8 combinations, aggregation/ties, per-slot ownership,
  privacy/deadlines/removal,30-question 8-player wire play beyond 256 requests,
  cache bounds and team packet size. Actual Godot UI handoff/ready/answer/recap/
  session-reset actions passed. Deferred-node cleanup warnings fixed by awaiting
  frame deletion; checker was not disabled. Canonical/CLI content gates passed.
- Source 20-question team+strategy full matches passed: 2 local+3 remote slots;
  8 local (team A 290820/ B 0,21 cards);2 local+2/4 remote slots (A290709/ B 0,21 cards).
  Packaged5-player team+strategy passed (A212816/ B 0,16 cards); packaged8-player
  individual/base also passed. Every owner finished with matching public finals.
- Packaged base-preview regression passed Host994/Anna993/Maria0. Discovery/PIN
  regression passed actual broadcast/custom ports, admission/rate limits, manual
  IP, fresh rejoin, started metadata, host exit and safe match departure. Explicit
  startup smoke observed C# ready and clean runtime stderr.
- Windows/Android debug exports, APK signature verification, physical install
  Success/launcher Status:ok passed. Physical Android15/23013PC75G and Windows
  completed 20-question5-player team+strategy matches with both hosting roles.
  Windows host2/phone client3: A212833/ B 0, public-final digest6A677E39...56E9A08;
  Android host2/Windows client3: A212757/ B 0, digestD7B99967...CE9BDBB.
  Scores/team membership/winners/individual stats/missions/cards matched fully.
  SHA256 public-state comparisons avoid logcat line truncation. Greek desktop,
  phone handoff curtain and final team/score screens inspected; runtime clean.
- Phone runs sequential, fixtures/captures cleaned, normal app restored and
  Windows peers stopped. No network tunnel/touch injection/lock bypass/settings/
  permission/firewall change. Automated physical execution, not human touch QA.
  MCP bridge offline; runtime/GdUnit/captures used. Known Godot export teardown
  diagnostic retained. No other known blocking error.
- Logs/captures: artifacts/phase09-*.log and phase09-*/; exact commands/decisions
  in harness/context/phase-09-mixed-teams-context.md. Docs/protocol updated; no
  production questions changed. Generated platform-lock churn restored; diff
  whitespace check passes. Stop before Phase 10 UI/accessibility/content scale;
  separate user approval is required to begin it. No commit/push performed.

## 2026-10-18 — Phase 08 — strategy mechanics complete

- Started from pushed Phase 07 f6fe343; this phase stays local/uncommitted.
  Confidence x1/x2/x3 penalties/floor, capped streak bonuses, host-owned Chaos
  Meter/two-card hands, six approved cards and five feasible private missions
  implemented in pure Core. Exact balance/windows in GAME_DESIGN; optional
  Steal/Shield pool off by default. Mission bonus once before final ranking;
  strategy disabled in sudden death. No new dependencies, services or GitHub CI.
- Protocol 5/app 0.5.0 rejects earlier builds. Separate recipient snapshots keep
  hand/mission private. Host validates card ownership/phase/timing/target/category
  and correlated duplicate-safe receipts; disconnected actors cannot act. Client
  validates bounded views and accepts authoritative deductions after reveal.
- Localized responsive strategy controls, private-panel privacy toggle, personal
  timer, hidden choices and final mission/card/confidence results added. Host
  private panel collapsed; narrow button wraps. Review found and fixed stale x3
  selection after switching to base mode; runtime UI test covers the Safe guard.
- New eight-player strategy packet test observed 16975 bytes at the former
  10000-byte content budget. Tightened validator to7000, preserved16KiB envelope,
  kept an explicit regression rejecting the formerly valid oversized content,
  and tested populated missions/two cards/long Greek names/category/final stats.
  Content format/schema commentary updated. Existing reviewed question passes.
- scripts/build.ps1 clean, zero warnings/errors. Final scripts/test.ps1
  -IncludeGodot passed232 Core +88 Infrastructure +6 GdUnit =326, none
  failed/skipped. Canonical content and CLI-negative gates pass. No failing
  check removed/skipped/weakened. Deterministic replay covers clock/seed/question/
  card IDs; card/mission Core cases and full30-question wire cases pass.
- Source and packaged30-question strategy host/two-client playtests passed with
  all six cards accepted and identical final scores/winner/stats/strategy records.
  Source rev204 Host110031/Anna101639/Maria0; packaged rev207
  Host110031/Anna102132/Maria0. Default-pool packaged20 passed all four card kinds:
  rev141 Host75731/Anna67828/Maria0. Greek narrow/final screenshots inspected.
- Packaged base-preview and discovery/PIN regression passed: broadcast/custom
  port, admission/rate limits, manual IP, fresh rejoin, started metadata, host exit
  and graceful match departure. Startup explicitly waited for Godot process exit
  and observed 'QuizParty: C# startup ready.' with clean runtime stderr.
- Windows/Android debug exports and APK signature verification pass. Physical
  Android15/23013PC75G install/normal launch succeeded. Actual20-question LAN
  matches passed both hosting roles with identical final score/winner/stats and
  mission/card/confidence results: Windows-host aggressive rev116
  Host68208/Phone72012; Android-host aggressive rev116 Phone68211/Windows-player
  Host72023; default Windows-host final run rev122 Host68105/Phone74640.
  Both final-run players completed missions and used9 cards each. Screenshots
  inspected, no app runtime errors. One earlier extra default run was interrupted
  by overlapping test orchestration; preserved under
  artifacts/phase08-android-default-interrupted/ and isolated repeat passed.
- No ADB network tunnel/input injection/lock bypass/device settings/permission or
  firewall changes. Private argument fixture absence confirmed after cleanup;
  normal Android app restored, Windows peers stopped. Automated physical
  execution, not human touch-play acceptance. Known Godot export teardown
  shutdown_adb_on_exit diagnostic retained; no new blocking error.
- Evidence: artifacts/phase08-build.log, phase08-tests-final.log, phase08-runtime*
  .log, phase08-network*, phase08-android*, phase08-export-*.log and
  phase08-startup*.log; durable details in phase-08 strategy context. Generated
  platform lockfile churn restored; diff whitespace check passes. Production
  still has one human-reviewed question; all long fixtures synthetic. Stop at
  Phase 08. Phase 09 mixed local/LAN and teams requires separate user approval.

## 2026-10-18 — Phase 07 — discovery, PIN and graceful disconnect complete
- Baseline Phase 06 pushed as 153c835 before this approved phase. New changes
  remain local/uncommitted. No GitHub CI, dependencies or external services added.
- Implemented strict discovery codec/catalog/reply limiter, independent Godot
  UDP adapter, responsive room browser and optional masked PIN input. Protocol 4/
  app 0.4.0 intentionally rejects older versions. Host gate validates PIN and
  limits failed attempts by actual source IP across new transport connections;
  discovery broadcasts no PIN/hash/token. Manual IP uses the same admission gate.
- Selected the phase's allowed graceful-disconnect baseline: new lobby joins get
  fresh unready identity; started matches reject re-entry, preserve confirmed
  scores and expire missing answers. UI shows departed names and host-loss
  guidance. No token reclaim, match resumption or host migration is claimed.
- Build clean (zero warnings/errors). 208 Core + 79 Infrastructure + 5 Godot =
  292 tests passed, none failed/skipped. Full test script plus final extra
  confirmed-answer departure/replay test passed. Strict content/CLI gates pass;
  no content/schema changes. Logs: phase07-tests-final.log and
  phase07-integration-final.log. No failing check deleted/skipped/weakened.
- Source and packaged test-network-discovery.ps1 passed actual broadcast/custom
  game port, wrong/missing/correct PIN, limits across connections, manual IP,
  fresh lobby rejoin, started metadata, host exit, empty scan guidance and safe
  match departure. Departed Phone timed out unanswered; Host994/Phone0 at rev6.
- Packaged lobby regression passed. Source 20-question and packaged 30-question
  matches passed with identical results on host/two clients. Final packaged30:
  rev184, Host29911/Anna29818/Maria0. Root startup smoke passed.
- Windows/Android debug exports, APK signature verification, install Success and
  launch succeeded. scripts/test-android-discovery.ps1 passed physical Android
  15/23013PC75G Wi-Fi192.168.68.106 ↔ Windows Ethernet192.168.68.105 on real LAN
  game17789/discovery17790, with both devices hosting. Each broadcast-discovered
  the other, rejected wrong PIN and admitted correct PIN. Phone manual-IP rejoin
  got a new ID, then host exit was observed. No network tunnel/forwarding, input
  injection, firewall/device settings or Android permission change. Private debug
  arguments removed (run-as ls checked), temporary screen capture removed and
  normal app restored. Automated physical runtime, not human touch acceptance.
- Final screenshots inspected: Greek browser/PIN flag and departed-player
  message, readable phone wrong-PIN feedback beside input and Android host lobby.
  Evidence: artifacts/phase07-network*, phase07-android/, phase07-export-*.log
  and phase07-smoke.log. Runtime error scans clean. Known editor/export
  shutdown_adb_on_exit teardown diagnostic remains retained in logs.
- Production pack still contains one human-reviewed question; long regression
  content remains synthetic. LAN broadcast varies by router/device policy; manual
  IP remains available. No safe match resumption is enabled in this baseline.
- git diff --check and untracked-source whitespace checks passed; generated lock
  churn restored. Stop at Phase 07; Phase 08 strategy needs separate user approval.

## 2026-10-18 — Phase 06 — full game loop and selection complete
- Prior Phase 05 committed/pushed as 4b3d310 on origin/main. Phase 06 remains an
  ordinary uncommitted diff. GitHub CI remains disabled; no dependencies added.
- FullMatch/MatchSettings/QuestionDeck implement 10/20/30 questions, four rounds,
  category/difficulty mixing without repeats, per-question host deadlines,
  cumulative scoring, basic final stats and correctness/host-time sudden death.
  UI adds host settings, progress/recaps/stats. Protocol 3 intentionally rejects
  old clients and resets private input per question; correctness stays reveal-only.
- Final automated evidence: 208 Core + 62 Infrastructure + 5 Godot = 275 passed,
  zero failed/skipped. Full test script plus added final wire tie test passed.
  logs: artifacts/phase06-tests-final.log, phase06-integration-final.log. Build
  zero warnings/errors; strict canonical validator and CLI failure exit checks pass.
- Source 20-question host/two-client run: revision 124, Host 19941 / Anna 19879 /
  Maria 0. Packaged rendered 30-question run: revision 184, Host 29914 / Anna
  29793 / Maria 0, instance c8485e8e-4f5f-4285-9120-4fd4f5a78411. Each peer
  observed all four rounds and distinct questions; final winners/statistics equal.
  Packaged timeout also passed (Host 995 / Anna 993 / Maria 0, unanswered).
- Long-run shutdown exposed simultaneous-disconnect errors. Fixed application
  sends plus disabled unused SceneMultiplayer peer relay. Regression now keeps
  host alive through both client departures and requires clean error logs. Final
  source/packaged runs passed; source and packaged lobby regressions passed.
- Eight-player near-limit Greek content revealed a 17,197-byte final packet under
  the old allowance. Tightened shared content budget to 10KB, retaining 16KiB
  envelopes; regression rejects the old content and verifies a valid near-limit
  question fits eight-player final results. No failing checks removed or bypassed.
- Final Windows/Android exports pass. APK signature verification and ADB install
  Success observed; public launcher returned Status: ok. Physical long-match
  attempt could not initialize while phone was Dozing/locked; preserved logs in
  artifacts/phase06-android-20-asleep. After user wake/unlock, the physical run
  completed 20 distinct questions and all four rounds: revision 104, Host 19941 /
  Phone 19685, instance 3f4bd7d8-2c69-4bc6-85b8-b94ed8d2339d. Winner and all
  final statistics matched exactly; runtime error scans clean. Phone results
  screenshot inspected (readable score/stat rows and large controls). Logs and
  captures: artifacts/phase06-android-20/. Automated real-device play, not human
  touch verification. Earlier active capture caught reveal during the fast loop.
  Debug argument fixture was removed and normal launcher restored. No device
  lock bypass, touch injection, settings change or network tunnel used.
- Windows final screenshot inspected: readable Greek scores, winner and all
  three stat rows, touch-sized buttons, no clipping at 1152x720. Screenshot in
  artifacts/phase06-network-30-packaged/host-final.png. Smoke passed. Known Godot
  editor/export shutdown_adb_on_exit teardown diagnostic remains logged; final
  game runtime scans are clean.
- Production content remains one explicitly human-reviewed question. Long runs
  use labeled opt-in debug fixtures; normal 10/20/30 starts require more reviewed
  content and reject insufficient category capacity before lobby start.
- git diff --check passed; generated lock churn restored. Phase acceptance met
  with Windows and physical Android long-match evidence. Stop here; Phase 07
  discovery/PIN/reconnect needs the user's next explicit go-ahead.

## 2026-10-18 — Phase 05 — JSON question packs and validation complete
- Committed/pushed prior Phase 04 as ae46e15 at user request. New work local only.
- Shared strict manifest/question validator, CLI, immutable reviewed repository,
  category metadata/editor schemas and Godot PCK reader implemented. Removed
  hardcoded production fixture; build/test/smoke/export validate and stage JSON.
- Initial one-question pack has explicit user editorial approval, recorded in
  content/EDITORIAL.md with official source. No generated bulk library marked reviewed.
- Build zero warnings/errors. Tests 195 Core + 56 integration + 4 Godot = 255
  passed, none failed/skipped. Canonical strict validator passed. CLI draft failure
  exit 1 and invalid usage exit 2 observed. No failing test bypassed/weakened.
- Source and packaged host/two-client match passed. Final Windows/Android exports
  passed and include JSON. Physical phone installed/launched; Windows-host match
  loaded reviewed JSON and matched Host 876 / Phone 849 at final revision 6.
- Physical Android-host check directly loaded JSON from APK; matched PhoneHost 995 /
  Windows 992 at revision 6. Logs/screenshots preserved under phase05-android-*.
  Automated real LAN, no tunnel/input injection; private test arguments cleaned up.
- Smoke passed. Runtime error scans clean; existing editor/export teardown
  diagnostic remains documented. Protocol v2 unchanged, no new dependencies.
- git diff --check and new-source whitespace scan passed; generated lock churn
  restored. Scope is one reviewed question and working content pipeline, not a
  completed bulk question library. Stop; Phase 06 full loop needs separate approval.

## 2026-10-18 — Phase 04 — One-question playable match complete
- User-requested baseline commit/push: d23468b (Phase 03) on origin/main. New
  Phase 04 work remains local; no final commit/push performed. GitHub CI stays off.
- Implemented host Core one-question coordinator, dedicated match DTOs/client
  view state and responsive question/reveal/score/results panel. Reused existing
  lobby/ENet and Core scoring/validation; no new dependencies/production content.
- Production protocol 2 rejects old v1 clients. Host-derived player/receive time,
  instance/range/confidence/deadline/duplicate validation; no correctness/points
  before reveal or in private ack. Host alone advances scoreboard/final results.
- scripts/build.ps1: zero warnings/errors. scripts/test.ps1 -IncludeGodot: 195
  Core + 31 integration + 4 Godot scene tests passed; zero failed/skipped. Initial
  compile/test-fixture mistakes fixed; no tests removed, skipped or weakened.
- Source and packaged test-network-match.ps1 normal and timeout cases passed:
  all phases and identical final instance/revision/scores on host/two clients,
  repeated answers safe; wrong answer and unanswered result explicitly checked.
- Existing lobby and spike regressions passed. Startup smoke emitted C# marker.
  Final Windows/Android debug exports passed, APK signature verified.
- Real Android APK installed/launched; test-android-match.ps1 correct/wrong/
  unanswered cases passed over actual 192.168.68.x LAN to packaged Windows host.
  Same final scores on both peers: 876/849, 876/0, 876/0, final revision 6. Exact
  IDs/excerpts in docs/MATCH_EVIDENCE.md; screenshots inspected on phone/Windows.
- Physical play was automated through debug-only app-private test arguments,
  without ADB network tunnel/input injection/settings changes. Fixture removal
  verified and normal phone startup restored. Human touch play not claimed.
- No game/network runtime error observed; known editor/export-only teardown
  diagnostic remains visible/documented. Content JSON/schema unchanged.
- git diff --check passed; new source/test/script whitespace scan clean. Only
  generated lock-file churn reverted; no dependency changes.
- Docs/protocol updated; stop at Phase 04. Phase 05 content system requires
  separate approval. No broader Android/router matrix or full-game claim.

## 2026-10-18 — Phase 03 — Lobby and network protocol complete
- User-requested pre-phase commit/push: a2354ed on origin/main, containing Phase 02
  and CI removal. New Phase 03 work remains local; no final commit/push performed.
- Implemented Core lobby roster/ready/start rules; bounded production v1 DTOs,
  host router, request/session/ownership validation, duplicate/rate/cache guards
  and client snapshot validation. Separate ENet adapter and Greek/English lobby
  view support manual-IP join, ready controls, host-only start and disconnect.
- `scripts/build.ps1`: six-project build, zero warnings/errors.
- `scripts/test.ps1 -IncludeGodot`: 193 Core + 22 integration + 3 Godot tests passed,
  zero failed/skipped; production rebuild clean. Existing tests were preserved.
- `scripts/test-network-lobby.ps1` and `-Packaged`: both passed a real ENet host
  plus two clients with identical ready roster/start revision 6, duplicate setters,
  remote-start/late-join/version rejection, departure cleanup to revision 8,
  host exit, no-host timeout and freed-transport join timer cancellation.
- `scripts/test-network-spike.ps1` passed existing handshake/action/ack/duplicate/
  version/no-host regression. `scripts/smoke.ps1` observed the C# startup marker.
- Final Windows and Android debug exports passed. No physical Android lobby run
  claimed. Source and packaged process stderr checks were clean. Existing Godot
  editor/export teardown diagnostic remains documented, not hidden.
- Inspected Greek viewport captures at 1152x720 and 390x844. Fixed inherited
  portrait scaling and wrapped title; setup hides after connection. Final captures
  had empty stderr; original shader-cache diagnostic and canceled optional MCP
  debug helper are recorded explicitly in phase context.
- Documentation: NETWORK_PROTOCOL.md, docs/LOBBY.md, architecture/toolchain/testing
  guides and phase context. No dependencies/content/permission changes.
- `git diff --check` passed; new source/script whitespace scan clean. Restored
  generated lock-file churn only. GitHub CI remains off (API: zero workflows).
- Phase 03 ends at GameStarting. Stop; separate approval needed for Phase 04
  one-question Windows/Android playable slice.

## 2026-10-17 — Phase 02 — Core domain and state machine complete
- Working tree: prior user-approved CI removal preserved; no commit/push performed.
- Implemented pure C# host session/state machine, distinct identities, immutable
  public snapshots, shuffled question instances, host-time answer validation,
  duplicate/replay guards and configurable base/time scoring awarded once on reveal.
  Added monotonic clock/seeded randomness boundaries and deterministic fixtures.
- `./scripts/build.ps1`: restore and six-project build passed, zero warnings/errors.
- `./scripts/test.ps1`: 189 Core + 5 integration passed, zero failed/skipped.
- Explicit detailed lifecycle test passed and logged Boot-to-GameOver plus rematch,
  scores 1000/0/0 and single score award. This is observed in-memory Core execution.
- `git diff --check` passed; new Core/test source whitespace scan found no matches.
- No scene/protocol/content changes; no Godot/device gameplay claimed or required
  for this isolated phase. Existing Godot/LAN spike remains unchanged. Confidence
  x2/x3, streaks/cards/missions, tie-breakers and automatic scheduling remain later.
- Decisions/API details: docs/CORE_DOMAIN.md and Phase 02 context. Stop at Phase 02;
  separate user approval required before Phase 03 lobby/network work.

## 2026-10-17 — GitHub CI disabled by user request
- Disabled the remote Foundation checks workflow using GitHub CLI; API confirmed
  state `disabled_manually`. Removed `.github/workflows/ci.yml` locally.
- Updated project/testing/release/content requirements and agent instructions to
  use local verification. Prior CI entries below remain historical evidence;
  the pending Phase 01 remote recheck is no longer required.
- Local build/test/smoke/network scripts and all tests are unchanged. No game
  code changed; automated/runtime tests were not rerun for this documentation
  and workflow change. No commit or push performed.

## 2026-10-17 — Phase 01 CI startup follow-up
- Phase 01 b40e251 was pushed. Remote run 39066341871 passed restore/build and
  all xUnit tests but aborted at the existing 120-second Godot test-session limit.
  Individual test results were unavailable; no failing test was disabled.
- Fresh source-only local rebuild and all eight tests passed. Changed GdUnit
  process launch to use the actual Windows engine executable rather than its
  console wrapper, consistent with the export/network helpers; enabled detailed
  adapter logging for diagnosis. No application code or packaged assets changed.
- Kept every test and the same timeout. CI must be checked again after this fix.

## 2026-10-17 — Phase 01 — Windows/Android LAN technical spike complete
- User authorized pre-spike and post-spike commit/push. Baseline c710604 was pushed
  to origin/main before implementation; GitHub Actions 39065537445 passed.
- Implemented: separate localized spike scene, host/manual-IP join/send/disconnect,
  C# ENet adapter, bounded host probe validation and idempotent receipts. Pure Core
  remains independent of Godot; no lobby/gameplay/content systems were added.
- Build: scripts/build.ps1 -> 0 warnings, 0 errors.
- Tests: scripts/test.ps1 -IncludeGodot -> 8 passed (1 Core, 5 infrastructure/
  config, 2 scene tests), 0 failed/skipped. Production rebuild clean.
- Network regression: scripts/test-network-spike.ps1 passed independent-process
  hello/action/ack, duplicate count safety, protocol-version rejection and bounded
  unreachable-host failure. Added the same test to GitHub Actions.
- Exports: both final debug packages built; Android signature verifies; APK
  installed and launched on physical Android 15/model 23013PC75G. Windows packaged
  host launched through normal main-entry flags, not a prohibited scene override.
- Real LAN: user manually entered Windows Ethernet IP 192.168.68.105 from phone
  Wi-Fi 192.168.68.106. Host accepted hello and button action; phone displayed
  acknowledged count 1. No ADB reverse/forward network tunnel was used. ADB input
  injection was blocked by the device; the user operated the actual touch UI.
- Failure path: after terminating host, phone logged SERVER_DISCONNECTED.
- Final-build repeat: user rejoined and sent two actions, host counts 1/2 and
  phone acknowledgements 1/2 match. Phone acknowledgement screenshot inspected.
- Evidence: docs/LAN_SPIKE_EVIDENCE.md contains durable exact excerpts; phase context
  captures compatibility findings. Full ignored artifacts/phase01-* contain builds,
  local tests, network logs and phone screenshots. git diff --check passed.
- Limitations: one physical Android phone/home LAN tested. Two-phone and larger
  matrix coverage remain future work. Existing Godot editor/export teardown
  diagnostic persists; no game/network runtime errors observed. No firewall or
  VPN settings changed. No production lobby/discovery/reconnect or game rules.
- Phase boundary: Phase 01 acceptance met; stop here. Phase 02 needs separate user
  approval. Completion changes are committed/pushed under the approved workflow.

## 2026-10-17 — Product and project renamed to QuizParty
- User explicitly chose QuizParty, without the geographic qualifier. Greek-first
  language/content focus and selected Cartoon Showtime direction are preserved.
- Renamed root solution, six project folders/project files, Godot-local solution,
  namespaces, assembly references, runtime marker, app title/localization, export
  filenames and Android package ID (org.quizparty.game). Updated build/test/install
  helpers, architecture/content/setup/design docs, ignore/attribute paths and MCP
  project configuration. Private MCP backup retained outside Git.
- Both concept logos were edited using built-in image generation and inspected;
  current files are docs/design/concepts/cartoon-chaos-quizparty-v2.png and
  cartoon-showtime-quizparty-v2.png. Edit prompt is recorded in concept README.
  Originals and stale export/cache files remain recoverable in ignored artifacts.
- Restore/build: scripts/build.ps1 -> 0 warnings, 0 errors.
- Tests: scripts/test.ps1 -IncludeGodot -> 3 passed, 0 failed, 0 skipped;
  subsequent production rebuild -> 0 warnings, 0 errors.
- Runtime: scripts/smoke.ps1 and fresh Windows packaged executable emitted
  `QuizParty: C# startup ready.`. Windows and Android debug exports produced.
- Android: APK signature verifies; aapt confirms application-label QuizParty and
  package org.quizparty.game; archive contains renamed QuizParty assemblies and
  no old assembly names. ADB installation returned Success; launch Status: ok.
  Per-process logcat has renamed C# startup marker; screenshot visibly shows
  QuizParty on physical Android hardware. Earlier development app was not removed.
- Editor/MCP: reopened renamed project; stdio inspection and screenshot passed.
- Verification evidence: artifacts/rename-build.log, rename-tests.log,
  rename-smoke.log, rename-export-windows.log, rename-windows-runtime.log,
  rename-export-android.log, rename-android-install.log,
  rename-android-runtime.log, rename-android-screen.png, rename-mcp-check.log.
- Active-source old-name audit passed; historical entries below intentionally
  preserve actual past observations. Existing GitHub remote URL/history remain
  intact. Known Godot shutdown diagnostic persists as previously documented.
- git diff --check passed. No commit, push, remote rename or LAN phase performed.

## 2026-10-17 — Visual direction selected
- User selected concept B (Cartoon Showtime): dark game-show stage, clear panels,
  neon accents and expressive cartoon avatars.
- Recorded in docs/design/VISUAL_DIRECTION.md and linked from concept notes.
  No gameplay code, production assets or phase status changed.

## 2026-10-17 — Inkscape and Blender asset-tool readiness
- User authorized setting up both asset tools before discussing visual style.
- Observed existing installations: Inkscape 1.4.4 at Program Files/Inkscape/bin;
  Blender 5.2.2 LTS at E:/Blender Foundation/Blender 5.2. No reinstall/upgrade needed.
- Added tool-resolution and CLI wrappers; Blender is located through its Windows
  installation registry, supporting the existing custom drive without PATH edits.
- scripts/verify-asset-tools.ps1 passed: Inkscape exported a 512px PNG with Greek
  text; Blender saved a .blend, rendered a transparent 256px PNG using Cycles CPU,
  and exported a 2,052-byte GLB. Godot 4.7.2 imported SVG and GLB without errors.
- Both resulting PNGs were visually inspected. Final wrapper version commands
  succeeded. Evidence is ignored artifacts/asset-tools-verification.log and
  artifacts/asset-tools/ (source/export files, render, metadata, Godot import log).
- Documentation: docs/ASSET_WORKFLOW.md and docs/TOOLCHAIN_STATUS.md updated.
  Test assets do not define art direction and are not included in the game.
- No gameplay, production art, engine/plugin settings or user preferences changed.
  GPU rendering is unverified; repeatable CPU rendering and CLI automation work.
- git diff --check passed. Nothing committed, pushed or published.

## 2026-10-17 — Phase 00 / user-approved tooling gap fixes
- Commit/worktree: original main commit d34062c preserved; Git metadata moved to
  C:/chatgpt_projects/QuizParty/.git. No commit, push, or publication performed.
- Implemented: documented solution/project layout; nullable C#; SDK pin; responsive
  localized startup scene and C# probe; Compatibility rendering; root and Godot
  export solutions; test projects; build/test/smoke/export/install/doctor scripts;
  GitHub Actions baseline; pinned MIT editor addons; dependency/setup docs.
- GitHub: CLI 2.102.0 located at Program Files/GitHub CLI; user completed sign-in;
  auth status and API user query verified OnSpeeder. Origin URL preserved.
- Build: scripts/build.ps1 restored and built all six projects with 0 warnings,
  0 errors. Core has no Godot references.
- Clean-source verification: copied only Git-listed source files into ignored
  artifacts/clean-foundation (no .godot/bin/obj caches); build succeeded with
  0 warnings/0 errors, headless startup emitted the C# marker. Fresh source can
  build and start. Final git diff --check passed; only LF normalization notices
  appeared on generated solution/lock files.
- Tests: scripts/test.ps1 -IncludeGodot passed 1 Core architecture check, 1 project
  configuration check, and 1 real GdUnit C# scene test; none skipped. Production
  rebuild after tests succeeded. Adapter internal-build property propagation and
  copied Android source compilation failures were fixed, not bypassed.
- Godot runtime: headless startup emitted `GreekQuizParty: C# startup ready.`;
  editor opened, live MCP scene tree returned Main/Center/Content/Title/Status,
  and screenshot was captured and inspected. Both HTTP diagnostic and final
  configured stdio transport were exercised. Client catalog reload still required.
- Export templates: official 4.7.2 mono TPZ downloaded, SHA-512 compared against
  official SHA512-SUMS.txt, all 27 entries installed in matching template folder.
- Windows: debug export includes published .NET assemblies; packaged executable
  launched headless, emitted C# startup marker, and exited. Earlier incomplete
  package crashed due to missing assemblies; publish failure was traced to copied
  Android scripts and fixed by excluding android/**/*.cs from compilation.
- Android: official template requested platform 36/build-tools 36.1.0; installed
  those components. Export preset enables required ETC2/ASTC import and Gradle.
  ARM64 APK produced (97,030,092 bytes); apksigner v2 verifies; aapt confirms min
  SDK 24/target 36 and INTERNET permission. ZIP inspection confirms game/Core/
  infrastructure DLLs, Mono and Godot native libraries; no addon/test asset trees.
- Real phone: Android 15/model 23013PC75G connected and authorized. First install
  was rejected by device policy; user enabled/approved installation, then ADB
  returned Success. Launcher script was fixed to use public MAIN/LAUNCHER intent.
  Launch Status: ok; app resumed; per-process logcat contains C# startup marker;
  screenshot inspected showing the centered foundation display. No game startup
  exception observed. No LAN communication is claimed.
- Evidence: ignored artifacts/build-final.log, tests-final.log, smoke-final.log,
  export-windows-final.log, windows-runtime-final.log, export-android-final.log,
  android-install-retry.log, android-launch.log, android-runtime.log,
  mcp-stdio-check-final.log, editor-screenshot.png and android-screenshot.png.
- Known limitations: engine emits documented EditorSettings shutdown_adb_on_exit
  teardown diagnostic; export script retains it and fails other engine errors.
  SDK manager has an unrelated existing duplicate cmdline-tools/latest-2 directory.
  CI configuration has not been run remotely. QuestionValidator is explicitly a
  nonzero placeholder until Phase 05; no gameplay/content/networking implemented.
- Stop boundary: toolchain/foundation only. Next separately approved phase is
  Phase 01 LAN technical spike; device export/launch evidence may be reused.

## 2026-10-18 — Phase 10 — approved presentation subset delivered

- Commit/worktree: main; local, uncommitted presentation changes. No push/publication.
- Scope: user deferred manual TV/mobile layout QA, accessibility/touch blocker
  certification and 1,000+ reviewed questions. Full Phase 10 remains open.
- Implemented: Showtime theme/vector crew, responsive answer grid, safe margins,
  field labels, keyboard/touch controls, text countdown/reveal cues, clearer
  results, saved volume/mute/reduced-motion/large-text/high-contrast settings,
  original synthesized feedback and nonblocking 160ms fades. Cards/missions start
  collapsed on every device; host authority and local handoff/privacy stay intact.
- Verification: restore/build -> success, zero warnings/errors; test.ps1
  -IncludeGodot -> 252 Core +100 infrastructure +10 GdUnit passed, none skipped.
  Existing tests preserved; new runtime coverage for settings, focus, cancellation,
  mute and container resizing. Expected invalid-config warnings and established
  Godot EditorSettings shutdown_adb_on_exit diagnostic retained in raw logs.
- Source 20-question host/two-client strategy match -> pass, totals agree.
  Windows/Android debug exports -> success; APK v2 signature -> verifies.
  Packaged Windows startup -> observed marker/clean stderr. Packaged five-player
  mixed local/LAN team+strategy match -> 20 questions, both peers agree, A212846/B0.
- Runtime evidence: inspected desktop/portrait menus, lobby, large-text/high-contrast
  settings, active client answers and final individual/team screens. Actual engine
  mixed audio -> cue peak276887552, mute peak0 (signed 32-bit). No human touch,
  screen-reader, real-speaker listening or new physical Android QA is claimed.
- Evidence: artifacts/phase10-build-final.log, phase10-tests-final.log,
  phase10-network-final.log and phase10-network/, phase10-packaged-mixed.log and
  phase10-packaged-mixed/, phase10-export-*.log, phase10-apk-verification.log,
  phase10-packaged-startup*.log, phase10-audio-verification.log and phase10-*/preview.png.
- git diff --check -> pass. Desktop build restored after Android export; unrelated
  generated Core/infrastructure lockfile changes removed. Production content still
  exactly one reviewed question; automated existing content gates remain green.
- Context/guide: harness/context/phase-10-polish-content-context.md and
  docs/PRESENTATION.md. Stop at this approved subset; deferred gates stay open.
  Phase 11 requires separate approval. No remote CI/workflow changes.

## 2026-10-18 — Phase 10 visual QA rejection and replacement

- User rejected the first installed mobile presentation and requested a graphics/UI
  overhaul. No visual/accessibility sign-off was granted.
- Rebuilt home, focused create/join/waiting, framed answers/confidence chips and
  character standings with illustrated portrait/wide Showtime stages. Live controls
  remain native Godot. Built-in artwork provenance/prompts: Art/README.md.
- Fixed physical Android target scaling using actual window/viewport dimensions;
  observed 533dpi portrait minimum64 and landscape72, satisfying48dp. All preferences
  retained; no Core/protocol/content change or dependency addition.
- Final test.ps1 -IncludeGodot: 252 Core +100 integration +13 Godot passed, no skips.
  Desktop restore/build passed with zero warnings/errors. Expected invalid-config
  warnings and existing editor teardown diagnostics retained in raw logs.
- Windows and Android debug exports succeeded; APK v2 signature verifies. Installed
  on physical Android15. Inspected actual portrait/landscape home/settings captures.
- Packaged Windows and physical Android mixed LAN runs passed: 5 players, teams,
  strategy,20 synthetic questions; all scores/teams/missions/statistics agree.
  Android digest: 1F6A17558A7F2BDAC291C850E928661DF02AF8671F2DA8FDC309CC0E59AEE0FC.
- Real exported Greek QuestionActive/GameOver screenshots passed capture helpers.
  Evidence: artifacts/phase10-redesign-*.log and docs/PHASE10_QA.md.
- Windows capture timed out twice; Android injected input denied; no permission
  bypass. Human touch/audio/TV approval pending. Android Godot accessibility backend
  reports unsupported; TalkBack/full accessibility certification not established.
- Replacement awaits visual review. Phase10 open; content remains one reviewed
  question, expansion deferred. No Phase11, publication, push or remote CI change.
- Final git diff --check passed; generated Core/infrastructure lockfile churn removed.

## 2026-10-18 — Pre-commit verification

- User requested commit and push of the current Phase 10 presentation changes.
- scripts/build.ps1 passed; build completed with zero warnings/errors.
- scripts/test.ps1 -IncludeGodot passed: 252 Core, 100 integration and 13 Godot tests; production rebuild passed.
- Content validation/CLI gates passed as part of the scripts. Logs: artifacts/commit-build.log and artifacts/commit-tests.log (ignored local evidence).
- git diff --check passed. Outstanding Phase 10 manual acceptance/content gates remain documented above.

## 2026-10-18 — Settings specification and asset-plan integration

- Integrated the user's additional prompt and attached image into
  docs/design/SETTINGS_PAGE.md; linked the spec from the visual direction,
  presentation guide, active Phase 10 file and plan/context.
- Preserved the supplied reference under docs/design/concepts, outside runtime
  assets. Spec covers Greek-first native text, landscape navigation / portrait
  cards, density-aware targets, original sliced assets, mascot poses, accessible
  motion/input, existing preference compatibility and pending service dependencies.
- Documentation/reference change only; no game code, preferences, content,
  protocol or production UI assets changed. No build/runtime tests rerun.
- Verification: local spec/reference links and git diff --check passed. Settings
  implementation and original Phase 10 acceptance gates remain pending.

## 2026-10-18 — Settings UI implementation and original asset production

- User authorized implementing the integrated settings specification. Delivered
  SettingsPanel.tscn/C# view with landscape tabs, portrait cards, safe areas,
  gold/purple native UI skin and separate blue/orange mascot bays. Shell retains
  local persistence, audio and privacy; no Core/protocol/content change.
- Produced 29 editable SVG masters via scripts/build-settings-vectors.ps1 and
  two original transparent four-pose atlases using built-in imagegen. Final
  prompts/provenance/dimensions: Art/Settings/README.md. Both atlas central seams
  are clear; blue registration repaired before use. All SVGs parse as XML.
- Existing preferences preserved. Added validated Greek/English language field,
  native translation keys, offline help/credits/engine notices/privacy/About,
  real version metadata and Cancel-first presentation-only reset. Unsupported
  music/narration/haptic/shake controls are omitted. No new dependency added.
- Final scripts/test.ps1 -IncludeGodot: 252 Core +100 integration +17 Godot =369
  passed, zero failures/skips. Tests include old configs, invalid locale, save
  failure, confirmed/cancelled reset, nested Back, mute, motion cancellation,
  96-unit target propagation and focused-section retention across rotation.
- scripts/build.ps1 passed with zero warnings/errors and strict content/CLI gates
  passed. Production content remains one reviewed question. Earlier iteration
  resource-cleanup/reparent errors were fixed; final test process exits cleanly.
  Existing EditorSettings shutdown_adb_on_exit export/import diagnostic and
  deliberate invalid-config/save-failure test warnings remain in the logs.
- Windows/Android debug exports passed; final APK v2 signature verified and APK
  installed/launched on physical Android. Inspected standard and high-contrast/
  larger-text portrait/landscape settings captures. At533dpi targets remain
  64/72 logical units (>=48dp). Source captures cover Greek desktop Audio/Gameplay,
  English Help, portrait, larger text/high contrast and short landscape.
- Packaged Windows mixed local/LAN regression: 5 players, teams +strategy,
  20 synthetic questions, matching final scores/team sums/missions/statistics;
  runtime stderr clean. The outer shell initially inherited a stale native exit
  code despite the helper's PASS; inspected its complete PASS and both empty
  runtime error logs. No networking failure was hidden or test weakened.
- Declared text/surface contrast checks: body13.65:1, normal brightest4.98:1,
  hover8.02:1, active6.54:1, high contrast18.23:1. These do not confer human
  readability or accessibility certification.
- Evidence: artifacts/settings-{tests,build}-final.log,
  settings-export-{windows,android}-final.log, settings-apk-verification.log,
  settings-android-{standard,contrast}-final.log, settings-network-final.log,
  phase10-settings-*/preview.png and phase10-qa/android{,-standard}/.
- Desktop build restored after Android export; generated Core/infrastructure
  lockfile churn removed. git diff --check passed. No push or Phase11 work.
- Human touch/listening/TV review, full combination/assistive-technology QA,
  release review of credits/privacy and reviewed-content expansion remain open.
  Android accessibility backend reports unsupported. Phase10 remains open.

## 2026-10-19 — Rejected settings candidate; Inkscape visual study 02

- User rejected the prior settings UI and requested a new 16:9 side-by-side
  landscape/portrait mockup using Inkscape and its newly configured MCP.
- Delivered docs/design/settings-study-02/: editable 3200x1800 SVG, portable
  outlined SVG and full-size PNG. Reused stage/crew illustrations and existing
  orange wave pose; new vector frame/control layers, confetti and pedestal.
- Actual Inkscape MCP validate, gradient-stop edit and PNG convert succeeded via
  a local FastMCP stdio client. Inkscape1.4.4 rendered/outlined the SVG. Evidence:
  artifacts/settings-inkscape/mcp-finish.log and review.png. Corrected malformed
  tab paths, mascot viewport clipping and text encoding during visual iteration.
- XML/PNG dimensions and actual rendered composition inspected; git diff --check
  passed. No new game code/assets were installed into the runtime and no game
  tests were rerun for this visual-only deliverable. Phase10 remains open and
  neither the prior runtime visuals nor the new study has user sign-off.


## 2026-10-19 — Settings vector recreation / study 03

- Created docs/design/settings-study-03/ as a separate visual deliverable;
  preserved previous studies, runtime integration and unrelated local edits.
- Entire stage, controls, flags, pedestal and both mascots use vectors.
  Editable/outlined master plus exact 1920x1080 and 675x1200 SVG/PNG exports.
- Inkscape 1.4.4 rendered all three canvases; visually inspected composition
  and portable sheet. Corrected shadow blur, flag clipping and reset overlap.
- All six SVGs parsed: unique IDs, resolved local references, zero images,
  no external links; outlined versions contain zero text elements. Exact
  aspect ratios/PNG dimensions verified. Portable render differs only by
  minor outline antialiasing (mean channel difference below 0.001/255).
- Independently exported reset button and music thumb as transparent PNGs.
  Structural/render evidence: study folder validation.json. Generator:
  scripts/create-settings-vector-study.py. git diff --check passed.
- Art-only follow-up: no game code, content or protocol changes; game tests
  and runtime import were not rerun. Phase10 and human approval remain open.

## 2026-10-25 — Phase 10 — PDF conversation assessment and presentation revision
- Commit/worktree: local changes on 891f9fd, C:/chatgpt_projects/QuizParty; initially clean. No push/publication.
- Read all eight pages of the supplied conversation and checked recommendations against actual sources. Detailed accepted/adapted/rejected inventory: docs/PDF_CONVERSATION_REVIEW.md. Plan: harness/phase-10-pdf-review-plan.md.
- Implemented: filled empty theme/juice/stage placeholders; reused bold Greek Comfortaa with license/export/credits; centralized chunky styles and shaped answer icons; scene-owned cancellable tactile/entrance/reveal/score tweens; wide host cast vs compact portrait; framed strategy cards/meter and avatar handoff; labelled readiness/team borders; improved reveal readability and larger-text baselines.
- Preserved: Core, Infrastructure, protocol, SDK, renderer, masked PIN, existing art and optional asset tool probes. No tracked bin/obj found. Export-generated lockfile target churn restored to original content.
- Verification: scripts/build.ps1 and final production rebuild -> 0 warnings/errors. scripts/test.ps1 -IncludeGodot -> 252 Core + 100 integration + 19 Godot tests pass; final focused Godot run including larger-text assertions -> 19/19. Content validator and invalid-content CLI gates pass. Logs: artifacts/pdf-review-tests.log, pdf-review-godot-final.log, pdf-review-build-final.log.
- Test maintenance: existing card-action/privacy assertions retained; queries now search descendants because cards have deliberate PanelContainer wrappers. No test skipped or weakened. Added font coverage and reduced-motion/callback cleanup regression coverage.
- Runtime: actual host/client captures pass at 1152x648 QuestionActive, 420x900 QuestionActive/AnswerReveal/Scoreboard, large-text/high-contrast and motion-enabled QuestionActive. Logs: artifacts/pdf-review-{landscape,portrait,reveal,scoreboard,accessibility,motion}.log. No runtime stderr in passing captures.
- Visual critique: first landscape clipped the lower answer row; reduced cast height, recaptured and inspected all four choices within viewport. Reveal explanation originally crossed bright backdrop; added opaque panel and removed duplicate status/disabled strategy controls. Final portrait reveal and large-text/high-contrast captures inspected. Motion screenshot is not an animation trajectory/performance benchmark; automated tests exercise cancellation and exact endpoints.
- Packaging/device: scripts/export.ps1 -Platform Android and -Platform Windows pass. Font and OFL inclusion observed in export log. Updated APK installed and launched on connected Android device. scripts/test-android-presentation.ps1 -StandardAppearance passes all four portrait/landscape menu/settings captures; inspected portrait settings and landscape menu. scripts/test-android-match.ps1 -HostAddress 192.168.68.105 passes physical Android client + packaged Windows host over LAN, all phases/final agreement (Host 876, Phone 848); inspected physical active/final captures. Logs: artifacts/pdf-review-android-{export,install,presentation,match}.log and pdf-review-windows-export.log. Device interaction was automated, not human touch/listening QA.
- Initial issues resolved: pre-import capture could not load the previously unused font; imported before passing runs. Test-only namespace collision corrected with global::Godot.Collections. git diff --check EOF whitespace corrected; final gate passes.
- Existing diagnostic caveats: editor/export teardown still logs the documented EditorSettings shutdown_adb_on_exit error. GdUnit's separate editor-import process also logs socket-bind messages and an unclaimed Node StringName at shutdown; retained verbatim in logs, not represented as clean editor output. The runtime test runner and physical match pass without gameplay errors. No test/log failure filter was weakened.
- Known limitations: human visual/accessibility/touch sign-off, wider device coverage, motion aesthetics/performance benchmarks and 1,000+ reviewed questions remain open. No Phase 11 work begun. User visual review is the next phase-10 gate.

## 2026-10-25 — Phase 10 — Android rotation, Back and exit confirmation
- Worktree: existing local presentation changes preserved; no commit/push.
- Implemented: portrait launch + runtime Sensor orientation; hierarchical Back/Escape;
  in-match Back opens existing settings without disconnecting; home icon-only exit;
  localized responsive Yes/No modal with No focus and isolated underlying controls.
- Verification: build and explicit production Rebuild pass, zero warnings/errors.
  scripts/test.ps1 -IncludeGodot passes 252 Core, 100 integration, 22 Godot tests
  (374 total). Three new tests cover home Back/cancellation/focus, modal confirmation
  and rotation sizing, and lobby/match Back routing. Logs: artifacts/navigation-tests.log
  and navigation-build-final.log. Existing editor shutdown diagnostic remains as
  previously documented; no test weakened or skipped.
- Visual: actual 420x900 larger-text and 1152x648 exit-dialog captures inspected,
  plus home icon screenshot. Updated capture helper supports -View Exit. Initial
  captures were stale because desktop no-restore build encountered Android target
  assets; restore + explicit Rebuild corrected this. Final logs/captures:
  artifacts/navigation-exit-{portrait,landscape}.log and artifacts/phase10-exit-*.
- Device: Android export succeeded, APK installed and launched. Observed portrait
  startup and sensor-driven landscape rendering without restart. App's requested
  orientation reported FULL_USER. Physical captures: navigation-android-back.png
  (portrait home), navigation-android-confirmation.png (landscape modal),
  navigation-android-no.png (home after No). Actual injected Back opened modal;
  Enter on initially focused No kept process 24572 alive. Back, Tab, Enter chose
  Yes; pidof returned no process. Relaunched normally afterward. No device rotation
  setting or permission changed. Android export retains the existing engine
  EditorSettings shutdown warning. No broader performance claim.
- Rotation back to portrait is covered by scene-layout tests; a physical reverse
  rotation was not separately observed during this run. Human touch/visual and
  Phase 10 content gates remain open. git diff --check passes after final docs.

## 2026-10-25 — Phase 10 — discovery-first join and unique character admission
- Scope: user approved Creation/Participation labels, corner icon Back, rooms +
  count/icon refresh, optional PIN popup, name/eight-character selection, atomic
  conflict retry and Android keyboard visibility. User explicitly hid manual-IP
  UI while preserving its implementation. Plan: phase-10-join-flow-plan.md.
- Preserved preceding uncommitted presentation/content work. Baselines for touched
  components are in ignored artifacts/join-flow-baseline. No question edits,
  dependency additions, commit, push or publication in this task.
- Implemented Core typed character IDs/uniqueness for host, local and remote
  players; stable lobby/match DTO identities. v7 connection-bound, clock-expiring
  PIN preflight creates no roster member/reservation. Final claim handles races,
  duplicate requests, expiry and malformed input. Direct/manual transport remains.
- Implemented JoinFlow, CharacterPicker and centered keyboard-aware PIN modal;
  hidden occupied portraits use a greyscale material and disabled controls.
  Host/local selection uses the same catalog. Added Back/refresh/join vector icons,
  Greek/English text and accessibility labels; eight stable portrait identities.
- Built-in imagegen produced one four-portrait transparent atlas. Verified RGBA
  alpha and actual 1254x1254 size; project copy and exact prompt/provenance are in
  game Art/CHARACTERS.md and showtime-extra-crew-v1.png. Original art retained.
- Verification: local Core 254/254, Infrastructure 107/107, final Godot 25/25
  (386 tests). Full scripts/test.ps1 -IncludeGodot passed before the final one-test
  preview-role addition; final Godot suite then passed. No tests skipped/weakened.
  Logs: join-all-final.log, join-godot-final.log, join-build-production.log.
- Added explicit race/retry, PIN privacy/duplicate throttle, no preflight player,
  connection-bound expiry, malformed character/availability and old-version tests.
  GdUnit drives real isolated ENet host/client through wrong/correct PIN and final
  character claim. Existing UI assertions updated to approved hidden manual-IP UI.
- Real separate-process ENet host/two clients lobby regression passes, including
  readiness, duplicate safety, late/version rejection, departure/host loss,
  unreachable host and cancelled callback. Log: join-network-lobby.log.
- Desktop captures: real LAN discovery/PIN rooms, centered PIN and identity at
  420x900 and identity at 1152x648 inspected. Logs/captures: join-capture-*.log and
  artifacts/join-flow-*. Final icon centering/greyscale changes also observed on
  Android. No UI overflow in inspected name/choice layouts.
- Android: debug APK exported, installed, launched and then final revision exported/
  installed again. Actual LAN discovery to Windows at 192.168.68.105, wrong PIN
  returns to rooms with error, correct PIN shows identity, name entry and Purple
  selection admitted JoinTest at host roster revision 2. Physical landscape PIN
  and name fields visibly remain above the open Android keyboard. Back hid the
  keyboard while retaining name/selection screen. Captures: join-android-*.png;
  host/runtime logs preserved. No network tunnel, permissions or device-setting
  changes. Temporary fixture/screenshots removed and app relaunched normally.
- Physical QA found safe-area Back overlapping wordmark; wordmark now follows the
  actual inset-aware Back rectangle. Final installed screenshot confirms the fix.
  Fixture-only --match-ui-* flags also incorrectly started the old match probe;
  restricted it to actual host/join roles, added regression, and observed final
  preview produces discovery without phantom localhost connection/timeout.
- Initial verification blockers: existing content migration removed greece.json,
  so the CLI negative fixture now selects an actual question file with the same
  draft/usage failure assertions. Existing handoff test assumed an Athens answer;
  it now submits a valid index independent of content. Validator repeated token
  allocations caused ~66s room initialization and suite timeout; pre-tokenized
  sets retain exact duplicate/Jaccard rules, with a boundary/duplicate regression.
  New large pack validates with editorial warnings retained; no review status
  was changed by this task. Failed/timeout logs are retained in artifacts.
- Native ENet test initially used a different Transport node name from production;
  corrected test harness path. Guarded keyboard APIs on desktop/headless after
  initial captures reported unsupported-keyboard warnings. Final gameplay/capture
  logs are clean. The existing Godot editor/export shutdown_adb_on_exit diagnostic
  persists and is not represented as clean editor output.
- Docs updated: AGENTS, PRODUCT, ARCHITECTURE, NETWORK_PROTOCOL, README, TESTING,
  lobby/presentation/asset/visual/QA docs, current phase plan/context. Phase 10 human
  visual/accessibility acceptance remains open; no later phase begun. Final
  git diff --check passes. Matching v7 peers are required.
- Final Windows export also succeeded; packaged QuizParty.exe headless startup
  printed C# startup ready, exited 0 and produced empty runtime stderr. Evidence:
  join-windows-export.log and join-windows-smoke*.log.

### 2026-10-25 — user-approved lobby/setup revision

- Implemented initially unready host, three-column compact roster and icon ready
  states; own tile sends ready intent. Header actions open full game setup/rules.
  Full category/card/mission pages support individual/all/none selection, existing
  Greek catalogue pictograms, immutable host-selected pools and feasible missions.
- User explicitly approved Low 1–2 ×1, Medium 3 ×1.5, High 4–5 ×2. FullMatch filters
  selected difficulties and applies the multiplier before existing strategy. Wrong
  penalties, mission bonus and steals stay fixed. Host validates filtered capacity.
  Protocol/app moved to v8/0.8.0 because old clients reject the higher reveal bounds.
- Preserved pre-existing dirty work, custom themes/art, manual-IP transport,
  private assignment/answer handling, team and shared-controller behavior. No push,
  commit, publication, production-content editing or phase advance.
- Local verification: solution build passed; 261 Core tests and 108 infrastructure
  tests passed. Full Godot suite: 27 passed. After final layout/resource cleanup,
  both focused MatchSetup Godot tests passed without orphan warnings, followed by
  a successful production rebuild. Final solution build has no errors and two
  pre-existing xUnit2031 warnings in QuestionPackTests.
- ENet process regressions: lobby host + two clients passed (expected revisions
  now 7 at start and 9 after disconnects); 5-player/20-question teams+strategy mixed
  match passed; 3-player/30-question strategy+aggressive cards passed all six card
  activation assertions with identical host/client final scores. Initial 20-question
  seed-8 strategy run completed with agreed scores but did not award/use CategorySwap,
  failing that coverage assertion; it was not weakened or removed. Logs retained in
  artifacts/lobby-settings-network-*.log.
- Inspected actual portrait/landscape Godot captures and corrected clipping/wrapping,
  roster height/footer, card description overflow, and an unattached rules grid.
  See docs/PHASE10_QA.md. Final default pages fit the inspected viewports; larger
  text, player editing and team-control overflow use drag scrolling. Physical Android
  and human touch/accessibility acceptance remain outstanding; no new APK installed.
- `git diff --check` passed. Evidence: artifacts/lobby-settings-*.log,
  artifacts/lobby-settings/*.png and the Godot TRX. Editor import's Android shutdown
  EditorSettings diagnostic is recorded; final runtime screenshots have clean stderr.
- Follow-up: the 20-question strategy+all-six-cards process scenario passed with
  seed 42 and unchanged coverage assertions. Set the helper's default seed to 42
  so the standard 20-question coverage fixture draws/activates all required cards
  under the revised scoring/steal path; seed 8 remains selectable. The 30-question
  run above used seed 8. Final viewport stderr files were empty.

### 2026-10-25 — physical Android verification before host-role extension

User requested real hardware verification and a GitHub checkpoint before new
creation/headless/UI work. Exported fresh Windows and Android debug packages and
installed successfully on physical Android 15 model 23013PC75G. Physical menu and
settings captures in portrait/landscape were inspected: Greek accents, primary
controls, settings frame and mascot fit; no crash observed.

Hardware discovery checks found two real regressions, fixed before checkpoint:
- Runtime/editorial similarity checks scanned every previous question, delaying
  room creation with the existing 14,760-question collection. A rare-word posting
  index now narrows candidates while retaining the exact Jaccard >= .8 predicate.
  Exhaustive-equivalence regression and all 109 infrastructure tests pass; CLI
  QuestionValidator also passes, with editorial/layout warnings retained.
- Windows limited broadcast selected virtual/VPN adapters. Discovery now probes
  active IPv4 subnet broadcasts too, retaining nonce/source/rate validation. Delayed
  admission cleanup now checks transport membership before disconnecting a peer
  that has already gone. Directed-subnet/selection/drag Godot checks: 3 passed.

Physical LAN checks passed: discovery in both directions, both host PIN rejection
and admission, manual-IP transport, fresh identity on rejoin and host-exit behavior.
20-question strategy/aggressive-card match with Windows host/Android client passed;
both sides agreed on totals, winners, statistics, missions and card/confidence
results. Screenshots/logs: artifacts/pre-host-android-*.log,
artifacts/phase07-android/, artifacts/phase08-android-20-steal/ and
artifacts/phase10-qa/android-standard/. No ADB networking tunnel was used.

Existing content review flags and editorial assertions were preserved; validator
success is structural evidence, not a fresh factual review of 14,760 entries.
Pre-existing temporary tools/generators scripts are left locally, outside the
checkpoint; production JSON/art/source/docs changes are included. Known tooltip,
header overlap and creation-flow issues are explicitly the user's next requested
scope, not claimed fixed by this hardware checkpoint.
- Additional physical run passed with Android as host and packaged Windows as
  client: 20 questions, strategy, aggressive cards, identical authoritative totals
  and final personal results. Evidence: artifacts/pre-host-android-host-match.log and
  artifacts/phase08-android-20-steal-phone-host/. All debug argument fixtures cleaned.

## Optional-host verification — 2026-10-25

Core: 265 passed. Infrastructure: 110 passed, including v9 zero-player admission,
capacity, full match and observer privacy. Full Godot suite: 29 passed; final focused
creation/join/navigation/tooltip regression: 7 passed after final layout changes.
Production rebuild: zero warnings/errors. Local ENet matches passed with host0 /
remote2 and normal host2 / remote3. Physical Android 15 (23013PC75G) passed ten-question
team/strategy matches both as non-playing host and as two-slot client of a Windows
non-playing host; scores, teams, missions and statistics agreed. Evidence:
artifacts/optional-host-network-*.log, artifacts/optional-host-android-*.log and
artifacts/phase09-android-0-2{,-phone-host}/.

Physical touch creation also passed: host participation off creates an empty lobby;
on continues to name/character then creates AndroidHost with readiness false.
Observed Android keyboard, name input, character selection and submit. Captures and
logs: artifacts/optional-host/android-touch/. Inspected desktop native tooltip,
portrait/wide creation, identity and roster captures; icons no longer overlap,
selected character art has no central tick. Physical portrait/wide previews use
scripts/capture-android-creation.ps1 and artifacts/optional-host/android/.

Windows/Android debug exports and structural question validation pass. Existing
content layout/editorial warnings and known Godot EditorSettings shutdown warning
remain recorded; neither is a new runtime failure. No content review flags changed.
The pre-existing tools/generators directory stays untouched and untracked.
- Final production rebuild and Windows/Android exports completed; latest APK installed.
  Final six physical captures passed (optional-host-final-previews.log). Landscape
  identity shows all eight character illustrations and fixed Create action; overflow
  remains confined to the character list. Android temporary fixture absent and normal
  launch restored. git diff --check passed. Follow-up remains local after pushed
  checkpoint 05b7edd, matching the requested sequence.

## 2026-10-25 — match flow, unanimous progression and expanded game settings

Initial user-requested GitHub checkpoint: ba03339 pushed to origin/main. New scope
implemented within Phase10; see harness/phase-10-match-flow-plan.md and context.

Observed local verification:
- Restore and solution build passed. Production Godot rebuild: zero warnings/errors.
  Solution test-project build retains two pre-existing xUnit2031 analyzer warnings
  in QuestionPackTests (not suppressed).
- Core273 passed, infrastructure114 passed, Godot30 passed. Includes 40/50 full
  matches, exact120s/untimed timing, per-seat consensus/stale requests/disconnects,
  eight-local-seat host bounds in both orientations, delayed facts and replay.
- Unlimited720-question protocol regression crossed4,320 requests on one connection;
  old question receipts were safely retired and a replayed old answer rejected.
- Three-process real ENet flow passed from source and Windows package: observer
  host, two client connections/three logical seats, unanimous reveals/recaps,
  next question, unanimous End and same-room replay with all seats unready.
- Packaged ten-question mixed/strategy match (host0/client2) passed with identical
  final public results. Physical Android flow passed with two phone seats plus
  a Windows player and observer host; final totals and replay agreed on all peers.
- Reviewed host/portrait/modal/score/final captures; corrected concrete layout and
  UTF-8 findings described in docs/PHASE10_QA.md. No human sign-off claimed.
- Reviewed-only staging/QuestionValidator passes14,760 entries; existing editorial/
  layout warnings retained. No question or review flags changed. Windows/Android
  debug exports and Windows release export succeeded. Android APK installed and
  launched successfully on the attached physical device.
- Known Godot EditorSettings shutdown diagnostic remains in export logs. First
  discovery departure run failed due to a pre-existing Athens-only test bot reading
  the full production deck; probe now uses the existing synthetic fixture while
  keeping its score/departure assertions. Evidence logs remain in artifacts/.
- Evidence: artifacts/match-flow-{core,infrastructure,godot,build,process,packaged,
  mixed,discovery,android,export-windows,export-android,export-windows-release}.log.
  Guide: docs/EXPORT_GUIDE.el.md. Temporary physical debug arguments cleaned up.
  tools/generators remains untouched and untracked.

Final follow-up evidence: source and packaged discovery/manual-IP/PIN/departure
regressions both passed after repairing the synthetic fixture. Latest Godot suite
retains30/30, including suppression of late lobby statuses above an active match.
Inspected actual420x900 larger-text host question capture: all four touch-sized
answers fit without page scrolling, with readable Greek text and participant
status. Windows release startup exited0 with clean runtime stderr. Final Windows
debug/release and Android debug exports completed; final APK installed and the
physical flow repeated on the exact final build. Export teardown warning remains
the documented engine diagnostic, not a runtime failure. git diff --check passes.

# Build Log

Append observed implementation and verification evidence here. Plans are not evidence.

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

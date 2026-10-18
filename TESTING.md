# TESTING.md

## 1. Testing philosophy

A networked party game must be verified at several layers. Visual success in one manual session is not enough.

## 2. Test pyramid

### Layer A — Pure Core unit tests

Fastest and most numerous.

Test:

- score calculations,
- Confidence modifiers,
- streak transitions,
- mission progress,
- card validation/resolution,
- state-machine transitions,
- question selection/no-repeat logic,
- deterministic RNG behavior,
- answer-submission validation.

Preferred framework: xUnit or NUnit. Pick one and use consistently.

### Layer B — Infrastructure tests

Test:

- JSON loading,
- malformed content handling,
- settings persistence,
- validator behavior,
- protocol serialization/deserialization.

### Layer C — Godot integration tests

Use GdUnit4 where it provides value for C# and scene/UI behavior.

Test:

- scene startup,
- button/signal behavior,
- navigation,
- critical UI state,
- basic host/client scene integration,
- regressions around touch layout where automatable.

### Layer D — Network process tests

Launch host and clients as separate processes where practical.

The implemented lobby regression is `./scripts/test-network-lobby.ps1` (host + two
clients). After Windows export, also run with `-Packaged` to check normal packaged
startup. `./scripts/test-network-spike.ps1` preserves the earlier disposable probe.

Phase 07 adds `./scripts/test-network-discovery.ps1` (also `-Packaged -Capture`)
for actual UDP broadcast/custom port, PIN rejection/admission/reconnect limits,
manual IP, fresh lobby identity, started metadata, host exit and safe match
departure. `./scripts/test-android-discovery.ps1 -HostAddress <LAN-IP>` tests both
host roles over actual Wi-Fi/Ethernet, observes phone browser/error screens and
cleans up its opt-in debug argument fixture. Keep phone awake/unlocked. No tunnel
or injected touch input substitutes for LAN discovery evidence.

Phase 04 adds `./scripts/test-network-match.ps1` (also `-Packaged` and `-TimeoutCase`)
and the real-device helper `./scripts/test-android-match.ps1 -HostAddress <LAN-IP>`.
Verify full phase/score agreement, duplicate answers, wrong/unanswered outcomes,
and no correctness/score leakage before reveal. See docs/MATCH.md for hardware
automation setup and cleanup; automated phone play is not human touch verification.

Verify:

- handshake,
- lobby sync,
- answer submit,
- duplicate rejection,
- late-answer rejection,
- reconnect snapshot,
- match completion.

### Layer E — Real-device acceptance tests

Mandatory before Android release.

Use at least one physical Android device and preferably multiple hardware profiles.

## 3. Test conventions

- Given/When/Then naming where useful.
- Tests must not depend on wall-clock sleeps when a fake clock can be injected.
- Deterministic RNG in unit tests.
- Network tests use explicit timeouts and useful failure logs.
- A failing test must not be disabled just to make verification pass.

## 4. Core required test cases

### Score

- correct x1,
- correct x2,
- correct x3,
- wrong penalties,
- score floor behavior,
- time bonus boundaries,
- multiplier cap.

### State machine

- legal transitions succeed,
- illegal transitions fail,
- only host coordinator advances authoritative state.

### Submissions

- first legal answer accepted,
- second answer rejected/idempotent,
- invalid index rejected,
- stale question rejected,
- late answer rejected,
- invalid confidence rejected.

### Discovery and admission

- strict bounded UTF-8/JSON, exact fields/types, version and nonce rejection;
- observed source address, deduplication, 32-room cap and injected-clock expiry;
- reply rate limits, missing/wrong/malformed PIN and success without PIN leakage;
- per-address/global PIN limits across reconnects, duplicate receipts not charged;
- fresh lobby rejoin, active-match re-entry rejection and old-answer replay;
- confirmed score retained after departure, unanswered seats expire normally;
- host loss clearly closes clients; match resumption is not enabled.

### Cards

Each card gets:

- legal activation,
- illegal timing,
- ownership check,
- duplicate request,
- effect result,
- stacking/cap behavior.

## 5. Local content validation

Run QuestionValidator locally before release packaging. Any release-pack error blocks packaging.

scripts/validate-content.ps1 is the strict gate shared by build/test/smoke/export.
scripts/test-content-cli.ps1 verifies invalid-content/usage exit codes. Content
tests cover malformed/missing/unknown fields, cross-file duplicates, locales,
review status, Unicode, file reading and warnings. Human review is recorded in
content/EDITORIAL.md; tests cannot confer editorial approval.

## 6. Godot smoke test

At minimum:

- import project headless if supported,
- build C# solution,
- launch main scene or test runner,
- assert no immediate fatal error.

## 7. Android technical-spike acceptance test

Before major feature development:

1. Build Android APK from C# Godot project.
2. Install via ADB to real phone.
3. Launch successfully.
4. Windows hosts ENet session.
5. Android joins via manual IP.
6. Client sends a button action.
7. Host receives it.
8. Repeat with two Android clients if possible.

If this does not work reliably, stop and solve it before building higher layers.

## 8. Regression checklist for every milestone

- `dotnet build`
- `dotnet test`
- QuestionValidator if content changed
- Godot smoke/integration tests if UI/scene changed
- network test if protocol changed
- `git diff --check`

## 9. Performance tests

Before beta:

- 30-question match memory stability.
- UI FPS on target Android hardware.
- connect/disconnect repeated cycle.
- 8 simulated/logical players where possible.

Phase 06 deterministic tests cover 10/20/30-question completion, seeded filtered
selection, no-repeat/exhaustion, four rounds, cumulative statistics, host-clock
boundaries, stale input, sudden-death eligibility/correctness/host timing and full
replay with injected IDs. Wire tests cover 20/30 questions, input reset, old
receipts, snapshot rollback/version bounds and eight-player final packet size.
`test-network-match.ps1 -QuestionCount 20` and `-Packaged -QuestionCount 30`
use explicitly synthetic debug-only fixtures. No production questions are
generated or approved by these tests. `test-android-match.ps1 -HostAddress <IP>
-QuestionCount 20` checks distinct questions and final stats on actual hardware.

## 10. Release gate

Do not tag a release unless:

- build clean,
- tests green,
- validator green,
- Windows package launches,
- Android package launches on physical device,
- release checklist completed,
- known issues documented.

## Phase 08 strategy verification

Core StrategyTests cover confidence lock/penalties/floor, capped streak stacking,
meter/hand limits, every approved card, ownership/staleness/duplicate effects,
personal Extra Time boundaries/cutoff, swap feasibility/no-repeat, Shield/Steal
targeting and all five mission conditions/one-time bonus. Injected seed/clock/
question/card IDs replay complete strategy state deterministically.

StrategyProtocolTests run full 30-question matches for each card kind, including
per-recipient privacy, foreign-card spoofing, cached duplicate receipts, stale
receipts, negative totals deltas, malformed private views and final agreement.
Eight-player packet tests retain 16 KiB with a stricter 7000-byte content budget.
GdUnit checks strategy defaults, privacy collapse and touch-sized controls.

Additional process checks (explicit synthetic debug fixtures, no editorial approval):

~~~powershell
./scripts/test-network-match.ps1 -QuestionCount 30 -Strategy -Steal -Capture
./scripts/test-network-match.ps1 -Packaged -QuestionCount 30 -Strategy -Steal -Capture
./scripts/test-network-match.ps1 -Packaged -QuestionCount 20 -Strategy
./scripts/test-android-match.ps1 -HostAddress <LAN-IP> -QuestionCount 20 -Strategy -Steal
./scripts/test-android-match.ps1 -AndroidHost -HostAddress <PHONE-IP> -QuestionCount 20 -Strategy -Steal
~~~

Use -Seed for reproducible host RNG during fixture runs. Probes log successful
card uses and final mission/card/confidence records; scripts require all enabled
card kinds to be used and identical final authoritative results across peers.
Actual clock/network arrival times remain observed rather than deterministic.
Run base-match and discovery/PIN regressions after the protocol bump too.

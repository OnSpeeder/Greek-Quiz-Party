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

## 10. Release gate

Do not tag a release unless:

- build clean,
- tests green,
- validator green,
- Windows package launches,
- Android package launches on physical device,
- release checklist completed,
- known issues documented.

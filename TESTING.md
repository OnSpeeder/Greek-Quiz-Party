# TESTING.md

## Living-show benchmark (2026-10-26)

`LivingShowTests` verifies replay resets, timed reveal/joke ordering, immediate
reduced-motion completion, silent playback, cleanup, transparent puppet gutters
and audio duration. `scripts/capture-living-show.ps1` captures four real viewport
beats; use 1280×720, 420×900, `-LargeText`, and `-ReducedMotion`. Inspect the images.
`scripts/run-living-show.ps1` opens the interactive scene. Debug home also exposes
`SHOW_OPEN`. The preview is fictional and never connects to a match.

Device entry uses `--match-show-preview` through the existing debug-only private
argument fixture. Preserve existing device fixtures. Physical Android and human
animation/audio approval remain required; desktop portrait captures are not substitutes.

## Presentation revision checks (2026-10-25)

GdUnit verifies Greek glyph coverage in the shipped display font, larger-text
question/answer baselines, motion cancellation, exact score endpoints and cleanup
of animated controls. Existing private handoff/card tests remain mandatory.
`capture-match-presentation.ps1` also supports Scoreboard, -Motion, -LargeText and
-HighContrast. Inspect actual captures; passing scripts cannot confer visual QA.

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
- fresh lobby rejoin, token-bound active-match reclaim, expiry and old-answer replay;
- confirmed score retained after departure, unanswered seats expire normally;
- host closure returns clients home; a silent loss retries until the player leaves.

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

## Phase 09 mixed local/LAN and teams

MixedTeamTests exercise every 2–8 player count in local-only and mixed rosters,
per-slot readiness/capacity/removal/departure, host-only assignments, invalid team
membership, checked aggregation, a team win despite an opponent's higher personal
score, host-timed sudden death, shared exhaustion, strategy/mission sums and
teammate Steal rejection. MixedTeamProtocolTests cover multiple actors per
connection, forged/missing/out-of-range slots, foreign-card ownership, separate
private 50/50/deadlines, stale/removed slot state, defensive team copies,30-question
eight-player progression beyond 256 requests, cache byte bounds and final agreement.
Eight-player packet regression also runs with teams enabled.

Runtime GdUnit drives real local roster controls, readiness/team start, the
handoff curtain and two independent answer submissions, checks confidence reset,
recap access, explicit owner-change hiding and new-session privacy collapse.
Tests await deferred node deletion before checking cleanup; no orphan warnings
are ignored or checks disabled.

~~~powershell
./scripts/test-network-mixed.ps1 -Teams -Strategy -Capture
./scripts/test-network-mixed.ps1 -HostPlayers 8 -ClientPlayers 0 -Teams -Strategy -Port 17795
./scripts/test-network-mixed.ps1 -HostPlayers 2 -ClientPlayers 2 -SecondClientPlayers 4 -Teams -Strategy -Port 17797
./scripts/test-network-mixed.ps1 -Packaged -Teams -Strategy -Port 17801 -Capture
./scripts/test-network-mixed.ps1 -Packaged -HostPlayers 2 -ClientPlayers 6 -Port 17803
./scripts/test-android-mixed.ps1 -HostAddress <WINDOWS-IP> -HostPlayers 2 -ClientPlayers 3
./scripts/test-android-mixed.ps1 -AndroidHost -HostAddress <PHONE-IP> -HostPlayers 2 -ClientPlayers 3
~~~

Mixed probes are explicit debug-only --match-mixed launches with bounded
--match-local/--match-players and optional --match-teams/--match-strategy flags.
No bot is active in normal navigation. Synthetic fixtures confer no editorial
review. Final public-state SHA256 digests avoid Android logcat line truncation;
desktop helpers also compare full JSON and independently verify team sums.
Run base-match and discovery/PIN regressions after the protocol change.

## Participation revision verification

Core CharacterTests cover atomic explicit claims, host/local collisions, release
and eight automatic assignments. RoomPreparationTests cover no roster mutation
before final hello, PIN privacy/throttling duplicates, simultaneous competing
claims/retry, connection binding/expiry, malformed availability and v6 rejection.
GdUnit JoinFlowTests use isolated real ENet peers to drive wrong PIN, correct PIN,
identity, occupied portraits and final admission. Existing direct/manual transport
regressions stay; approved UI assertions now require the manual-IP control hidden.

capture-join-flow.ps1 uses an actual host and discovery, with rooms/pin/identity
captures in both orientations. Observe Android keyboard overlap on real hardware.
Question similarity checking pre-tokenizes each text while retaining exact duplicate
and Jaccard warning criteria; regression covers boundary/repeated whitespace. The
CLI draft fixture selects a real question file rather than the removed greece.json.
No content-review state is granted by these tests.

## Lobby setup revision checks (2026-10-25)

`MatchSetupTests` in Core covers selected difficulty copying/filtering, three-band
rounding, copied strategy pools, empty pools and impossible mission omission.
`MatchSetupProtocolTests` covers host-unready start blocking, filtered content
capacity and authoritative hard-question score reception without premature reveal.
Godot `MatchSetupTests` covers three-column readiness tiles, full-page navigation,
individual/all/none selection and thresholded dragging from a button without click.
Existing readiness fixtures now explicitly ready the host before intended starts.

Actual preview flags: `--ui-preview --ui-greek --ui-reduced-motion
--ui-lobby-page=setup` (or `roster/categories/cards/missions/rules`) with the existing
`--ui-capture=<absolute png path>`. They create debug-only local players, never new
production content. Capture normal and larger text in both orientations; inspect
Greek accents, clipping, privacy, touch targets and scrolling. No script replaces
physical Android/human usability sign-off.

## Optional host, creation and tooltip regression

OptionalHostTests cover absent host seat and 2–8 capacity. OptionalHostProtocolTests
cover v9 admission, full-match observer privacy and authoritative state. Godot
OptionalHostSceneTests exercises both create paths, back/PIN persistence, absent
selection tick, hidden native popup scrollbars, bounded short/long tooltips and
header non-overlap. PlayerIdentityForm is shared by creation and JoinFlow.
Physical capture helper: scripts/capture-android-creation.ps1. Live Android zero-seat
host matches: scripts/test-android-mixed.ps1 -HostPlayers 0 -RemotePlayers 2,
including reverse host direction. Preserve test fixtures and clean owned fixtures.

## Match-flow regression — 2026-10-25

MatchFlowTests covers untimed base-only scoring, 120-second exact deadlines,
consensus/duplicates/staleness, disconnects, host override and finite-deck
unlimited completion. Existing complete-match coverage extends to 40/50.
MatchFlowProtocolTests covers owned local slots, timed/untimed wire validation,
replay/fresh matches, v9 rejection and 720 questions beyond the receipt budget.
Previously invalid 0-count/61-second fixtures now test -1-count/121-second bounds
because the requested settings explicitly expand the legal domain.

MatchFlowSceneTests exercises eight local seats in both orientations, no-scroll
host question bounds, delayed modal/facts, host continuation and replay. Existing
privacy/touch/font tests retain their assertions at the new composable node paths.
Run scripts/test-network-flow.ps1 (-Packaged) for three players on two client
connections, including two owned local slots, unanimous Continue/End and replay.
It captures actual host/portrait controller views. scripts/test-android-flow.ps1
-HostAddress <Windows-LAN-IP> exercises that flow on physical Android. All probes
are explicitly opt-in debug fixtures and confer no question editorial approval.

## Reconnection and match interaction checks (2026-10-28)

ReconnectTests covers reserved multiple seats, accepted-answer protection, original
host deadline, invalid/duplicate tokens and expiry. JoinFlowTests exercises ENet
interruption, identity reclaim and graceful host closure. MatchSetupTests checks
thresholded dragging and isolation of the modal from the underlying page;
MatchFlowSceneTests verifies vote buttons survive same-phase snapshot updates in
both reveal and scoreboard. Physical Android Wi-Fi interruption and actual touch
usability remain required acceptance checks.

## Disconnect pause revision (2026-10-28)

MatchPauseTests uses an injected clock to check frozen question time, countdown,
manual quorum, unlimited reconnect delay, untimed completion and wrong results,
plus invalidated votes on a second disconnect. ReconnectTests checks per-slot
resume authorization, stale pause IDs, client reclaim after continuing, unchanged
scores and token privacy. GdUnit checks ENet reconnect and countdown timing.

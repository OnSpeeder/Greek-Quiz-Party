# ROADMAP.md

## Phase 0 — Repository foundation

Deliver:

- Git repository.
- solution/project skeleton.
- docs and agent harness.
- CI baseline.
- `.gitignore`.
- build commands verified.

Exit: clean clone can build skeleton.

## Phase 1 — Technical spike: Windows + Android + LAN

Deliver:

- Godot 4.7.2 .NET project.
- Windows launch/export.
- Android debug export/install.
- manual-IP ENet connection.
- one message/button round trip.

Exit: physical Android connects to Windows host reliably.

## Phase 2 — Core domain and state machine

Deliver:

- pure C# Core project.
- player/game/question primitives.
- authoritative state machine.
- fake clock/RNG abstractions.
- unit tests.

Exit: core flow is testable without Godot.

## Phase 3 — Lobby and networking protocol

Deliver:

- handshake.
- player roster.
- ready states.
- host start.
- version checks.
- snapshots.

Exit: several clients join and see identical lobby.

## Phase 4 — Vertical slice

Deliver:

- one hardcoded question.
- A/B/C/D answer.
- host validation.
- reveal.
- score.
- next/final screen.

Exit: complete one-question match across Windows + Android.

## Phase 5 — Content system

Deliver:

- JSON schema.
- repository loader.
- manifest/categories.
- validator CLI.
- 100–200 reviewed test questions.

Exit: no production question needs hardcoding.

## Phase 6 — Full game loop

Deliver:

- rounds.
- configurable game length.
- question selection/no-repeat.
- scoreboard.
- final stats.

Exit: stable 20–30 question basic match.

## Phase 7 — LAN discovery and reconnect

Deliver:

- UDP discovery.
- manual-IP fallback retained.
- room PIN.
- reconnect strategy or explicitly documented graceful-disconnect behavior.

Exit: normal home-network onboarding feels easy.

## Phase 8 — Strategic mechanics

Deliver in order:

1. Confidence.
2. Streaks.
3. Chaos Meter.
4. Initial 4 cards.
5. remaining approved cards.
6. Secret Missions.

Exit: all rules host-authoritative and unit tested.

## Phase 9 — Mixed local/LAN + teams

Deliver:

- distinct PlayerId/ConnectionId/LocalSlot.
- multiple local players.
- mixed remote/local roster.
- Team Mode.

Exit: target 2–8 player scenarios work.

## Phase 10 — UI/UX polish and content scale

Deliver:

- final visual language.
- responsive layouts.
- animations/transitions.
- audio/music.
- accessibility basics.
- controller/touch refinement.

- 1,000+ reviewed Greek questions.
- category balance.
- duplicate/staleness checks.
- editorial QA.

Exit: cohesive party-game feel on TV and phone, with content quality suitable for public release.

## Phase 11 — Beta hardening

Deliver:

- long-session tests.
- device matrix.
- network edge cases.
- performance profiling.
- crash fixes.
- balance tuning from playtests.

Exit: release candidate criteria met.

## Phase 12 — Packaging and v1.0

Deliver:

- Windows release package.
- Android APK/AAB.
- signing/release process.
- credits/licenses.
- release notes.
- final regression checklist.

Exit: v1.0 distributable.

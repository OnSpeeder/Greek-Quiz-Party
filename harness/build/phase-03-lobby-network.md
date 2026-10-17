# Phase 03 — Lobby and Network Protocol

## Goal

Implement protocol version/handshake, join/reject, player roster, ready state, lobby snapshot and host start.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

No LAN discovery yet; use manual IP. No cards/missions.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-03-lobby-network-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Multiple clients see consistent lobby; incompatible/wrong requests are rejected safely; integration tests or observed multi-process test evidence exists.

## Status

Complete locally on 2026-10-18. 218 local tests passed; source and packaged Windows
host/two-client ENet regressions passed. Windows/Android debug exports produced.
Physical Android lobby interaction remains unverified. See phase context/build log.
Phase 04 has not started.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

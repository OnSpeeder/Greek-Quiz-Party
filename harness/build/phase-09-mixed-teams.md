# Phase 09 — Mixed Local/LAN and Team Mode

## Status — complete locally, 2026-10-18

2–8 local/mixed players, multiple slots per controller, independent private
handoff controls and host-assigned two-team scoring/ties implemented. 359 tests
pass, including runtime UI interaction. Full source/packaged eight-player and
physical Android five-player matches with either hosting role passed.
Commit and push authorized after verification; stop before separately approved Phase 10.

## Goal

Implement multiple local players, mixed remote/local roster and Team Mode using separate player/connection/local-slot identities.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

Do not redesign network identity into one-player-per-connection assumptions.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-09-mixed-teams-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Target 2–8 player combinations work; team aggregation tests pass; host/phone controller experience is coherent.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

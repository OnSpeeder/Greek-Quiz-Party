# Phase 07 — LAN Discovery, PIN and Reconnect

## Goal

Add UDP discovery, room browser, room PIN, keep manual-IP fallback, and implement safe reconnect or documented graceful disconnect strategy.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

No Internet matchmaking.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-07-discovery-reconnect-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Discovery works on test LAN; manual IP still works; failure cases have clear UX; reconnect behavior is tested if enabled.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

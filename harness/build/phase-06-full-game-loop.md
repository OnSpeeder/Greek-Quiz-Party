# Phase 06 — Full Basic Game Loop

## Current status — 2026-10-18

Complete locally. 275 tests pass; source
20-question and packaged/rendered 30-question matches completed all four rounds
with matching host/client results and clean runtime logs. Android debug export,
signature, install and launch succeeded. After the user unlocked the phone,
physical Android completed 20 distinct questions over LAN with matching scores,
winner and final statistics. Screenshots inspected and debug arguments cleaned up.
Phase 06 remains uncommitted. Do not start Phase 07 automatically.
See phase context and build log for evidence and the one-reviewed-question limit.

## Goal

Implement multi-question rounds, game-length configuration, timers, no-repeat selection, scoreboards, final stats and tie-breaker baseline.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

No Chaos/Secret Missions until base loop is stable.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-06-full-game-loop-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

20–30 question match completes reliably; timer authority and selection tests pass.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

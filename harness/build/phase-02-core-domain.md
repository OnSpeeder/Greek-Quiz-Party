# Phase 02 — Core Domain and State Machine

## Goal

Implement pure C# game primitives, authoritative state machine, fake clock/randomness and initial scoring/submission validation tests.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

No final Godot UI and no full network protocol.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-02-core-domain-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Core has no Godot dependency; unit tests cover legal/illegal transitions and base scoring; build/test green.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

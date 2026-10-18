# Phase 08 — Confidence, Streaks, Chaos and Missions

## Status — complete locally, 2026-10-18

Confidence, capped streak scoring, Chaos Meter, six cards and five feasible
private missions implemented with host validation and localized controls.
326 tests pass; source/packaged full matches and physical Android full matches
with either device hosting passed. See phase context/build log for evidence.
Commit/push authorized after verification. Stop before Phase 09 without separate approval.

## Goal

Implement Confidence, streaks, Chaos Meter, approved cards and Secret Missions in incremental substeps.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

Do not add unapproved random effects or client-authoritative logic.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-08-strategy-mechanics-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Each mechanic has Core tests, host validation, clear UI state and full-match playtest evidence.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

# Phase 00 — Repository Foundation

## Goal

Create the repository skeleton, .NET solution/projects, empty Godot .NET project, baseline scripts/docs and CI foundation.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

Do not implement game mechanics, networking protocol or Android export beyond any minimal project configuration required for the skeleton.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-00-repository-foundation-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

A clean working tree can restore/build the solution; Godot project opens; `git diff --check` passes; repository structure matches ARCHITECTURE.md.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

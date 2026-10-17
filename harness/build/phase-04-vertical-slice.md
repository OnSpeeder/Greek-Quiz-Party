# Phase 04 — One-Question Vertical Slice

## Goal

Complete the smallest playable network match: lobby -> start -> one question -> answer -> reveal -> score -> final result.

## Read before implementation

- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

Question may be hardcoded fixture. No large content pack or advanced mechanics.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-04-vertical-slice-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

Windows host + Android client complete slice without desync; answer correctness and score are host-authoritative.

## Status

Complete locally on 2026-10-18. 230 automated tests passed; source/packaged
multi-process matches passed. A physical Android client and packaged Windows
host completed correct/wrong/unanswered matches over real LAN with matching final
scores. See docs/MATCH_EVIDENCE.md and phase context. Phase 05 has not started.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

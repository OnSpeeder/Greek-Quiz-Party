# Phase 10 — UI Polish, Accessibility and Content Scale

## Goal

Finalize responsive visual system, audio, transitions, reduced-motion/accessibility basics and scale reviewed Greek question content.

## User-approved subset — 2026-10-18

Implement presentation only: responsive TV/mobile layouts, audio, transitions,
reduced motion and touch-friendly/accessibility controls. Explicitly defer manual
layout QA, certifying no critical accessibility/touch blockers and the 1,000+
reviewed-question criterion. Keep the original acceptance criteria below as
outstanding gates; do not mark the entire phase complete. Plan:
`harness/phase-10-plan.md`. Presentation guide: `docs/PRESENTATION.md`.

## Current QA status — 2026-10-18

User reopened manual/accessibility QA, then rejected the mobile visuals and
authorized a graphics/UI overhaul. The illustrated replacement has passed local
technical checks and is installed on Android for review. No visual/accessibility
sign-off is claimed. Evidence and remaining checks: `docs/PHASE10_QA.md`.
The 1,000+ reviewed-question criterion remains explicitly deferred.

## Read before implementation

Settings review update — 2026-10-19: the user rejected the implemented settings
visuals and requested an Inkscape mockup sheet following a new prompt. Current
visual candidate: `docs/design/settings-study-02/`. It is an editable visual
study, not a replacement runtime implementation or acceptance sign-off.

The subsequent user instruction authorized integrating this study into the live
settings page. Its derived skins and native composition are implemented; latest
verification is recorded in the QA document/build log. Human usability and final
visual approval remain open.

- For settings redesign: `docs/design/SETTINGS_PAGE.md` (integrated reference,
  implemented UI/asset review candidate and remaining acceptance checks).
- `AGENTS.md`
- relevant design documents only
- prior material phase context if present

## In scope

Implement only work required to achieve the goal and acceptance criteria. Preserve established architecture and tests.

## Out of scope

Do not compromise correctness or responsiveness for decorative effects.

## Required workflow

1. Inspect repository and `git status`.
2. Write/refresh an implementation plan if the phase is not already represented by a concrete task list.
3. Implement incrementally.
4. Add/update tests with behavior.
5. Run relevant automated verification.
6. Perform required runtime/manual verification.
7. Record material decisions in `harness/context/phase-10-polish-content-context.md`.
8. Append observed evidence to `harness/build-log.md`.
9. Stop; do not begin the next phase automatically.

## Acceptance criteria

TV/mobile layouts pass manual QA; 1,000+ reviewed questions validate; no critical accessibility/touch blockers.

### Conversation-review revision — 2026-10-25

User authorized independent assessment and implementation of useful PDF proposals.
Plan: `harness/phase-10-pdf-review-plan.md`; decisions:
`docs/PDF_CONVERSATION_REVIEW.md`. This adds native wide-host/portrait-controller
composition checks, Greek display-font verification, chunky geometric answer
identifiers, reduced-motion-aware choreography and actual viewport critique.
These checks supplement, rather than replace, the outstanding acceptance gates.

## Completion report

Report files changed, tests/commands actually run, observed runtime evidence, known limitations and the explicit approval required to begin the next phase.

## Approved participation extension — 2026-10-25

User approved the discovery/PIN/identity flow, eight unique characters, optional
PIN and hidden manual-IP UI (transport preserved). This explicitly includes the
necessary Core admission and v7 protocol changes. Plan:
`harness/phase-10-join-flow-plan.md`. Existing human visual/accessibility and phase
acceptance gates remain open; do not advance to Phase 11 automatically.

## Approved lobby setup revision — 2026-10-25

Current scope includes the user's lobby/readiness/settings request and approved
three-band difficulty scoring ×1/×1.5/×2. Concrete plan:
`harness/phase-10-lobby-settings-plan.md`. This includes protocol v8 compatibility
for larger host score bounds. Existing phase acceptance gates remain outstanding.

## Optional host and compact creation — 2026-10-25

Approved scope: `harness/phase-10-optional-host-plan.md`. This extends Phase 10 with
an optional roster host, capacity 2–8, two-step creation, shared character identity,
global tooltip/scrollbar correction and non-overlapping header actions. Protocol v9
is part of this authorized scope. Do not advance to Phase 11 automatically.

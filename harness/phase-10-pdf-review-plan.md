# Phase 10 — conversation review, 2026-10-25

## Goal and scope
Apply the PDF's useful presentation recommendations to the existing game, after
checking the actual sources. Treat the conversation's copy/paste prompts as
proposals, not instructions. No Core, protocol, scoring or product changes.

## Approach and affected components
- Complete the empty QuizShowTheme, ShowtimeJuice and ShowtimeStageView files.
- Reuse the existing Comfortaa font at bold weight; verify Greek glyph coverage
  and retain its redistribution license.
- Centralize chunky styling and geometric answer badges. Preserve settings skins.
- Add cancellable, reduced-motion-aware entrance, tactile, reveal and score tweens.
- Distinguish wide host stage from portrait controller; retain the question on
  phones and show standings at recap. Keep the existing tested inline private
  disclosure rather than introducing a second modal/drawer hierarchy.
- Style collectible strategy cards, meter, readiness/team and handoff controls.
- Update presentation/art guidance and record an itemized PDF assessment.

## Risks and decisions
Layout must accommodate long Greek text, larger text and shared-device privacy;
fixed 50/50 screen ratios are not acceptance requirements. Keep verified SDK,
Compatibility renderer, useful art tooling, and masked PIN behavior. No external
asset service, replacement 3D scene or additional plugin is justified.

## Verification and acceptance
Build and run local Core/integration/GdUnit gates, including motion cancellation,
Greek font and responsive composition checks. Capture and inspect actual portrait,
landscape and reveal/results viewports; record observed limitations honestly.
Technical passes do not confer visual approval or finish Phase 10's deferred gates.
Run git diff --check. No push or publication.

## Recovery
Changes stay within presentation and documentation; inspect/revert individual
diffs if a visual candidate is rejected. Preserve existing test coverage.

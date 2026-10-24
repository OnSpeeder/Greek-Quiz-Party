# Phase 10 — Presentation implementation

## Goal and approved scope

Implement responsive TV/mobile presentation, audio, transitions and accessibility
settings. User approved this subset on 2026-10-18. Manual layout/touch QA,
certifying no critical accessibility blockers, and expansion to 1,000 reviewed
questions are explicitly deferred. Phase 10 as originally specified stays open.

## Components and approach

- Preserve Core, protocol, host authority, question packs and privacy boundaries.
- Reusable Godot theme and stage decoration follow docs/design/VISUAL_DIRECTION.md.
- Extend ResponsiveCanvas with adaptive safe margins and shared presentation shell.
- Add local persisted sound volume/mute, reduced motion, high contrast and larger
  text controls, accessible throughout normal screens. Corrupt settings use defaults.
- Brief decorative fades and event sounds must never delay input or reveal private
  information. Reduced motion cancels fades immediately; no flashing or camera shake.
- Preserve scene composition; update answer paths and tests together when adding
  the responsive GridContainer. Wrap Greek text, retain >=64 logical-unit touch
  targets and visible keyboard focus; scroll small viewports.

## Verification and acceptance for this subset

- Build, existing Core/infrastructure tests and GdUnit scene tests pass.
- Add focused runtime checks for settings, layout resizing and reduced motion.
- Observe engine startup and capture representative desktop/portrait screens.
- Verify Windows and Android debug exports; record actual results and limitations.
- git diff --check. Update phase context, build log and presentation guide.

## Risks and recovery

Large Greek text can grow controls; prefer wrapping and vertical scroll over clipping.
Settings remain device-local and never pause host deadlines. No new dependency or
external service. Recover by reverting presentation changes; no data migration,
protocol revision or content changes. Stop at Phase 10 boundary; do not push.

## Progress

- [x] Inspect clean worktree, existing scene composition and approved visual direction.
- [x] Implement shared theme, responsive shell and persisted preferences.
- [x] Add event audio and reduced-motion-compatible transitions.
- [x] Verify runtime, exports and document observed evidence/deferred gates.

Approved implementation subset delivered. Original Phase 10 acceptance gates
remain open as explicitly deferred; no Phase 11 work was started.

## QA follow-up authorized 2026-10-18

- [x] Inspect installed Android build, desktop/phone captures and text contrast.
- [x] Fix density-dependent Android touch sizing; retain >=48dp and >=64 logical units.
- [x] Exercise keyboard focus cycle, scroll reachability, Escape and Back paths in runtime tests; human input checks remain below.
- [x] Verify revised build/tests/exports and record bounded QA results.
- [ ] Obtain physical touch/rotation/listening and actual TV readability feedback.

Windows Computer Use capture timed out on both attempts; Android input injection
was denied by the OS. Do not change permissions or claim human checks passed.
Continue engine-driven checks and request direct user feedback on the installed app.

## Visual QA rejected — redesign authorized 2026-10-18

The user's hands-on feedback rejects the mobile presentation as an application
rather than a game and requests an overhaul of graphics and UI. Do not sign off
the prior visual pass. Implement the existing Cartoon Showtime direction with
production illustration assets, a game-like home screen, focused create/join
flows, a player waiting room and gameplay-first composition. Preserve all rules,
privacy, networking and accessibility settings. Keep reviewed content deferred.

- [x] Add illustrated portrait/wide stages and expressive mascot assets; live UI stays native.
- [x] Recompose home and separate lobby choice/create/join/waiting states.
- [x] Recompose question/meta/answers and visual standings, compact strategy controls.
- [x] Verify real rendered mobile/desktop states, interaction regressions and exports.
- [x] Record failed prior QA and present concrete replacement screens for review.

Replacement technical verification passed: 365 tests, both exports and real
Windows/Android mixed LAN regression. See docs/PHASE10_QA.md. Visual approval,
physical usability and accessibility sign-off remain open; stop at Phase 10.

## Settings reference integration — 2026-10-18

- [x] Integrate the user's additional settings prompt and attached reference into
  `docs/design/SETTINGS_PAGE.md`; preserve reference under `docs/design/concepts/`.
- [x] Define responsive composition, localized native UI, asset manifest, motion,
  input/privacy behavior and verification criteria against the existing build.
- [x] Implement the settings redesign, produce assets and complete automated
  verification; physical visual review and human acceptance remain open.

The user subsequently authorized implementation and asset production. The
composable settings view now has responsive sections, local language selection,
offline help/legal/About, confirmed presentation-only reset and animated original
mascots. Its 29 SVG masters and two pose atlases live under Art/Settings. Music, narration,
haptics and screen shake are not existing features; do not expose inert controls.
Retain SFX, reduced motion, larger text and high contrast. No phase advancement.

## Settings candidate rejected — Inkscape study, 2026-10-19

- [x] Create a closer landscape/portrait mockup sheet using Inkscape and the
  configured local Inkscape MCP; preserve the existing stage/mascot identities.
- [x] Deliver editable SVG, outlined portable SVG and full-size PNG under
  `docs/design/settings-study-02/`; validate and inspect actual Inkscape renders.

The implemented settings visuals were rejected. This latest request is a visual
mockup deliverable; no new runtime UI or unsupported setting behavior is implied.

## Inkscape study integration authorized — 2026-10-19

- [x] Derive reusable runtime SVG skins from the Inkscape master.
- [x] Integrate the dimensional title, sidebar tabs, compact controls, action row
  and mascot composition into the native settings panel.
- [x] Preserve one control instance across responsive reparenting, local
  preferences, privacy/focus, reset confirmation and reduced-motion/high-contrast.
- [x] Finish local/runtime/export evidence and present the integrated candidate.

Illustrative music/voice/haptic controls remain absent pending real services.
No game rules, protocol or question content changes; stop at Phase10.

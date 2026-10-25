# Lobby setup revision — 2026-10-25

User scope: host initially unready; three player tiles per row; icon ready states;
header game setup/rules actions; full setup and category/card/mission selection pages;
multi-select difficulty and host-authoritative difficulty scoring; responsive layouts
with drag scrolling when needed. Preserve current Showtime theme/art, private data,
manual-IP transport and all existing uncommitted work.

1. Extend immutable Core settings, filtered deck, selected strategy pools and scoring.
2. Add localized scene-owned setup/rules pages and intentional category icons.
3. Integrate header actions and compact roster; retain team/local-slot controls.
4. Update affected readiness fixtures explicitly; add filter/scoring/UI regression tests.
5. Build, Core/infrastructure/Godot tests and network regressions; inspect real portrait
   and landscape captures. Record observed results and limitations in context/build log.

Difficulty balance explicitly approved by user: three bands (1–2, 3, 4–5), ×1/×1.5/×2.
No content editorial status changes, publishing, commits or phase advance.

Verification completed: 261 Core, 108 infrastructure, 27 full Godot tests; final
focused Godot selection/drag checks 2/2 clean. ENet lobby, mixed teams, 30-question
all-card strategy (seed 8) and 20-question all-card strategy (seed 42) passed.
Actual Godot portrait/landscape captures reviewed; Android hardware/human approval
remains open. Evidence and limitations: `harness/build-log.md`, `docs/PHASE10_QA.md`.

# Phase 06 — full basic game loop

- Commit/push the completed Phase 05 baseline.
- Add immutable match settings, seeded category/difficulty mixing and no-repeat deck.
- Coordinate four rounds, question timers, cumulative scores, statistics and sudden death in Core.
- Extend/version network snapshots; reset private input on question changes; reject stale packets.
- Add host length/timer controls, progress/round recaps and final statistics in the responsive UI.
- Preserve the one-question reviewed preview. Reject insufficient production content before start.
- Verify 20/30 questions with explicitly synthetic debug fixtures, Core and wire tests,
  separate Godot processes and physical Android if available. Fixtures confer no editorial approval.
- Record decisions/evidence, update docs, stop at Phase 06 without committing the new phase.

Baseline decisions: four near-even rounds (remainder in later rounds); base scoring
unchanged until strategy/balancing work. Sudden death preserves regular totals,
uses only tied leaders and host receipt times; exhausted content yields an explicit
shared first place rather than repeating a question or looping forever.

Components: Core FullMatch/QuestionDeck and GameSession eligibility/receipt
durations; Infrastructure host/DTO/client state; Godot lobby/match panels and
opt-in probe; local network/device scripts, tests and protocol/content docs.
Out of scope: confidence multipliers, cards, missions, discovery, reconnect,
teams, new reviewed question volume and final-round score balancing.
Acceptance: automated selection/timer gates plus observed 20–30-question
completion across real game processes. Android gets the same rules/DTOs.
Risks: strict DTO changes require protocol 3; final results must fit 16KiB;
single-question production pack cannot prove long loops without test fixtures.
Recovery: Phase 05 is pushed as 4b3d310; new work remains an ordinary local diff.
No history rewrite, signing changes, services or dependencies are needed.

Implementation and verification completed, including the physical Android
20-question match after the user unlocked the phone. Evidence in build-log.md.

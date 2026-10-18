# Phase 08 — strategy mechanics

Baseline Phase 07 pushed as f6fe343. Implement incrementally: Core confidence
and capped streak scoring; host-owned meter/hand/cards; feasible private missions;
then versioned network intents/personalized views and responsive UI/playtests.

Use GAME_DESIGN starting penalties (x2 -250/x3 -500), zero total floor, 10% at
streak3/15% at5, total positive multiplier cap6. Meter100, gains20+5*difficulty
(+10 at streak5); consume threshold even if hand full, hand limit2, streak7
guarantees a card when space. Starting hands empty. No unapproved random effects.

Cards: Double Points before answer or armed during recap for next question;
50/50 before answer, wrong indices chosen privately by host; Extra Time +5s
activated with at least3s of base time left, once/question, no inflated time bonus;
Category Swap in recap before a remaining normal question, preserving feasible
missions/no repeats; Shield persists until one Steal or game end. Optional Steal
100 is OFF by default; when enabled each victim can be targeted once/match,
including shield-blocked attempts. Shield/Steal absent from pool when disabled.

Missions use approved examples only: Historian (3 history), Hot Streak4,
Gambler (2 correct x3), Speedster (fastest correct3), Generalist (5 categories).
Assign only feasible missions for selected normal questions/settings; none in
one-question preview. Bonus500 applied once at regular-game end before ranking.
No cards/strategy/missions during sudden death. Existing base-game profile stays
available for regression and host choice. Shared-screen private panel collapsed.

Expected components: Core Strategy types/resolver + GameSession/FullMatch/deck;
Infrastructure protocol/host/client validation and per-recipient snapshots;
Godot lobby strategy toggle and composable personal controls; tests/probes/docs.
Protocol bump required. Preserve manual IP, PIN/discovery and graceful departure.
No new dependencies/content/visual production/team mode/reconnect scope.

Verification: focused Core/wire tests per mechanic, privacy/ownership/idempotence/
deadline/floor/cap/mission feasibility; GdUnit UI and existing base regressions;
strategy-enabled 20–30-question process matches and actual Android playtest where
available. Record evidence/context, diff check, stop before Phase09. New work
remains local; no commit/push requested for this phase. Recover from pushed Phase07
baseline via normal edits, no destructive reset/history rewrite.

Completed 2026-10-18. Protocol 5/app 0.5.0; Category Swap offers up to three
host-approved categories (128-unit content identifiers). Encoded question budget
tightened from 10000 to 7000 bytes after observing a 16975-byte strategy final.
326 tests and source/packaged/physical full-match checks pass. Exact observed
evidence and limitations are in context/phase-08-strategy-mechanics-context.md
and build-log.md. No Phase 09 work or commit/push performed.

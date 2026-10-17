# Phase 02 context — Core domain and state machine

## Scope and decisions
- User approved Phase 02 only. Existing CI-removal edits were already present
  and preserved. No commit, push, new dependency or remote CI run was requested.
- Core remains net8.0 with no Godot/package reference. All changes are Core,
  Core tests and documentation. Existing Godot/LAN spike and production protocol
  are unchanged; there is no playable trivia UI yet.
- Implemented GameStateMachine structural edges and host GameSession contextual
  commands. GameSession exposes detached read-only snapshots rather than its
  internal collections. Domain snapshots must become separate transport DTOs in
  the networking phase. Correctness/explanation exist only after reveal.
- Fixed roster 1–8, supporting Solo and party. PlayerId/ConnectionId/LocalSlot
  remain separate, with multiple players allowed on one connection. Display name
  limit is 32 UTF-16 code units; future lobby validation should preserve this bound.
- Inject monotonic IGameClock and IRandomSource. Production BCL implementations
  use Stopwatch and seeded Random; tests use a manually advanced clock and exact
  draw sequence. Host-supplied instance IDs keep hidden GUID creation out of Core.
- Fisher–Yates shuffles answer indices and remaps correctness. QuestionDefinition
  validates basic domain invariants; it does not replace Phase 05 content validation.
- Base scoring defaults 500 + 0–500 time bonus, decimal tick ratio and midpoint
  away from zero. Scores mutate only once at reveal. Wrong/unanswered earn zero.
  Configurable scores are nonnegative; cumulative totals use checked long arithmetic.
- Phase 02 only permits Safe x1. x2/x3, streaks/cards/missions and tie-breaker
  mechanics are deliberately deferred; no strategic mechanic is claimed complete.
- Exact deadline accepted per existing protocol. Timeout closes strictly after
  deadline; all answers lock immediately. The optional explicit receipt overload
  takes host-captured time, never client time. Receipt time determines points even
  when host processing is delayed. Adapters must drain received intents before
  issuing a timeout close and serialize all domain commands.
- First answer wins, changed/duplicate attempts cannot replace it or its timestamp.
  Repeat reveal cannot award twice. Used instance IDs persist across rematches to
  prevent old-packet reuse; dispose the session at room end. Network identity
  authentication, request-ID receipts and reconnect remain later adapter work.

## Observed verification (2026-10-17, Europe/Athens)
- Incremental Core build: zero warnings/errors; first Core suite 172 passed.
- Final `./scripts/build.ps1`: restore/all six projects built, zero warnings/errors.
- Final `./scripts/test.ps1`: 189 Core + 5 integration passed, zero failed/skipped.
  Includes existing Core assembly dependency test, all 132 state/trigger pairs,
  client mutations, invalid construction/answers, privacy, shuffling and replay.
- Explicit no-build detailed run of BasicMatchRunsFromBootToGameOver test passed.
  Output observed: Boot -> Lobby -> QuestionActive -> timeout lock -> reveal ->
  scoreboard -> GameOver -> fresh game; scores 1000/0/0, reveal awarded once.
- `git diff --check` passed; new Core/test source whitespace scan found no matches.
- Runtime evidence is in-memory Core execution. No new Godot/Android gameplay
  acceptance claimed. Godot scene/network process tests were not rerun because
  this phase changes no scenes, adapters or protocol. Existing five integration
  tests passed against the new Core build. No content changed, so validator not run.

## Boundary
Phase 02 complete; stop. Phase 03 lobby/network implementation needs explicit
user approval. See docs/CORE_DOMAIN.md for transition/API integration details.

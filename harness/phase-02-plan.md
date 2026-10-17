# Phase 02 — Core domain and state machine

## Goal and scope
Implement the approved pure C# foundation: distinct player/connection/local-slot
identities, question definitions and instances, authoritative state transitions,
base scoring, answer validation, immutable public snapshots and deterministic tests.

## Approach and components
- Add domain types under `src/QuizParty.Core` and tests under
  `tests/QuizParty.Core.Tests`; use existing BCL/xUnit dependencies only.
- A host-owned GameSession coordinates a guarded GameStateMachine. Clients may
  render snapshots but cannot mutate a session configured as a client.
- Inject a monotonic IGameClock and IRandomSource. Host shuffles four answers;
  public snapshots omit correctness until reveal. Instance IDs are supplied by
  the host, keeping tests reproducible without hidden GUID generation.
- Validate eligible player, phase, question instance, duplicate, answer range,
  confidence and host receive time. Exact deadline is accepted (`<=` protocol).
  Capture receive time at the host adapter boundary; never accept a client clock.
- Score only on reveal, once: configurable 500 base + rounded 0–500 time bonus.
  Midpoints round away from zero; unanswered/wrong receive zero. Totals use long.
- Scope assumption: Phase 02 permits Safe x1 only. x2/x3, streaks, cards, missions,
  ties, multi-round scheduling and no-repeat selection remain their later phases.

## Out of scope
Godot UI/scene integration, production DTOs/transport/lobby, content loader/schema
changes, question packs and export changes. Existing CI-removal edits are retained.

## Verification and acceptance
- Tests cover every state/trigger pairing, client mutation rejection, full basic
  flow, malformed/duplicate/stale/late answers, exact deadlines, scoring boundaries,
  repeat reveal, snapshot privacy/immutability and deterministic answer shuffling.
- Run repository build and local tests; no Godot integration changed. Run an
  explicit Core flow test as runtime evidence, without claiming device gameplay.
- Core remains independent of Godot; build/tests green; `git diff --check` clean.
- Record observed commands/results and decisions in phase context/build log; stop
  before Phase 03. No commit/push is authorized for this phase.

## Risks and recovery
Host adapters must derive player ownership and supply actual host receive time;
Core cannot authenticate a network connection. Session commands are serialized on
one host execution context. No networking wire contract changes in this phase.
New code is isolated to Core/tests/docs; existing LAN spike remains unchanged.

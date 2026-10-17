# Core domain — Phase 02

`QuizParty.Core` targets .NET 8 and has no Godot or external package dependency.
This is the domain foundation used by Phase 04's `OneQuestionMatch` coordinator
and playable network slice. See [Match guide](MATCH.md) for the current Godot UI
and protocol bridge. No production question pack is implemented yet.

## Ownership and commands

Create a `GameSession` with `GameAuthority.Host`, a copied roster of 1–8 players,
an `IGameClock`, an `IRandomSource` and optional immutable `ScoringRules`.
One player supports Solo; the party roster remains capped at eight. Player names
are nonblank and at most 32 UTF-16 code units. `PlayerId`, `ConnectionId` and
`LocalSlot` are distinct. A connection can own multiple players with separate local
slots. There is no mutable lobby/ready/reconnect implementation yet.

Every mutating session command rejects client authority. This is a domain guard,
not transport authentication. A future host adapter must derive the player from
the actual connection/owned slot rather than trusting the packet's player ID.
Never give a client an RPC that invokes arbitrary host transition commands.

`GameStateMachine` checks structural edges; `GameSession` owns contextual checks,
question state, first accepted answers, score calculation and public snapshots.
Call the coordinator on one serialized host execution context. Render snapshots
without obtaining references to mutable host collections.

## Structural transitions

| Source | Command/trigger | Target |
| --- | --- | --- |
| Boot | Initialize | MainMenu |
| MainMenu | OpenLobby | Lobby |
| Lobby | StartGame | GameStarting |
| GameStarting or RoundEnd | BeginRound | RoundIntro |
| RoundIntro | StartQuestion / BeginQuestion | QuestionActive |
| Scoreboard | StartQuestion / NextQuestion | QuestionActive |
| QuestionActive | all eligible answers or CloseQuestion / LockQuestion | QuestionLocked |
| QuestionLocked | RevealAnswer | AnswerReveal |
| AnswerReveal | ShowScoreboard | Scoreboard |
| Scoreboard | EndRound | RoundEnd |
| RoundEnd | FinishGame | GameOver |
| GameOver | ReturnToLobby | Lobby |

Illegal transitions return `GameError` without changing state. Every command's
result must be checked by the caller. StartQuestion clears prior reveal/answers;
StartGame resets scores. Question instance IDs cannot be empty or reused during
the lifetime of a session, including rematches. Dispose the session at room end.
Round scheduling, question counts/selection, match configurations and tie-breakers
are not implemented here; later coordinators decide when to request those edges.

## Question privacy and randomness

`QuestionDefinition` is host-only content with four distinct answers, one valid
correct index, category, difficulty 1–5 and explanation. It is a domain subset,
not the JSON pack schema/loader or editorial validator scheduled for Phase 05.
The host supplies a unique `QuestionInstanceId` for each presentation. Starting
a question shuffles indices using injected Fisher–Yates randomness and remaps
the correct index. Input content and caller-owned lists are copied.

`GetSnapshot()` returns a public domain view, not a network DTO. While active or
locked it contains presentation, deadline, accepted answer count and old totals;
its `Reveal` is null. It contains no correct index, correctness flags or
explanation until `RevealAnswer()`. Reveal contains each player's selected index
(null means unanswered), correctness and awarded points. Snapshot collections are
read-only and existing snapshots do not change after later commands.

`SeededRandomSource` uses BCL Random for reproducibility within the pinned runtime;
it is not a cross-runtime persisted replay format. Tests can inject exact draws.

## Time, validation and duplicates

`IGameClock.Now` is monotonic host elapsed time; `MonotonicGameClock` uses
Stopwatch. Nothing depends on frame rate, sleeping, wall-clock time or client time.

SubmitAnswer validates eligible player, active phase, matching question instance,
first submission, index 0–3, Safe x1 confidence and host receipt time. Expected
rejections return `SubmissionError` and do not consume an answer slot. Subsequent
answers cannot replace the original answer or receipt, even with changed content.
There is no request-ID cache/wire acknowledgement contract yet; the one-answer
rule makes mutations duplicate-safe.

The normal overload captures host time immediately. A buffered adapter may supply
the time captured at its host receive boundary; it must never forward a client
timestamp. Receipts before start, after deadline or later than current host time
are rejected. Exact-deadline receipts are accepted, matching NETWORK_PROTOCOL.md.
Process received intents in order before a timeout-close command; a closed
question does not reopen to accept queued answers. CloseQuestion succeeds once
host time is strictly past deadline; all eligible answers lock immediately.

## Scoring

Phase 02 supports Safe x1 only. Wrong and unanswered answers award zero.
Confident x2, All-in x3 and undefined confidence values are rejected until the
strategic mechanics phase. No streak/card/mission effects or penalties are active.

Default correct points:

`500 + round(500 * (duration - hostElapsed) / duration)`

Thus correct answers at start, halfway and deadline earn 1000, 750 and 500.
Base and maximum bonus are configurable nonnegative integers. Rounding uses
decimal tick ratios with midpoint away from zero. Scores are awarded only on
reveal; a repeated reveal is rejected and cannot award points twice. Per-question
points are int and cumulative totals are long, with checked arithmetic. New totals
are calculated before mutation so overflow does not leave partially updated scores.

## Verification

Run `./scripts/build.ps1` and `./scripts/test.ps1` locally. The Core suite includes
the complete state/trigger matrix, client authority, a Boot-to-GameOver lifecycle,
rematch reset/replay protection, configured/base/time scoring, deadline boundaries,
delayed processing of host receipts, duplicates, invalid input, hidden correctness,
snapshot immutability, answer shuffle mapping and deterministic seeded results.
No new dependencies, Godot integration or hardware gameplay are needed for this
isolated phase. Device gameplay must be observed once later phases connect it.

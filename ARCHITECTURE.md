# ARCHITECTURE.md

## 1. Architectural objective

Keep the game rules deterministic, testable and independent of Godot while using Godot for presentation, lifecycle, input, audio and platform integration.

## 2. Proposed solution layout

```text
QuizParty/
├── src/
│   ├── QuizParty.Core/
│   ├── QuizParty.Infrastructure/
│   └── QuizParty.Godot/
├── tests/
│   ├── QuizParty.Core.Tests/
│   └── QuizParty.IntegrationTests/
├── content/
│   └── questions/el-GR/
├── tools/
│   └── QuizParty.QuestionValidator/
├── docs/
├── harness/
├── AGENTS.md
├── PLANS.md
└── QuizParty.sln
```

## 3. Dependency rule

`Core` must depend on **no Godot types**.

Recommended direction:

```text
Godot Presentation ───────┐
                          v
Infrastructure -------> Core
```

Core defines interfaces when inversion is useful. Infrastructure/Godot provide implementations.

## 4. QuizParty.Core

Pure C# domain logic.

Phase 02 implements the basic host session, state machine, question presentation,
base scoring and submission validation. See [Core domain](docs/CORE_DOMAIN.md) for
the implemented API, transition table, timing boundaries and later-phase work.

Phase 03 adds Core `LobbySession` for host roster/readiness/start rules,
Infrastructure `LobbyHost`/`LobbyClientState` with separate protocol DTOs, and a
Godot `LobbyTransport`/`LobbyScreen` adapter/view. The lobby state stops at
GameStarting; the Phase 04 bridge below continues gameplay outside the view.
See [Lobby guide](docs/LOBBY.md) and the implemented contract in NETWORK_PROTOCOL.md.

Phase 06 bridges to Core `FullMatch`, reusing `GameSession` scoring and
validation. `LobbyHost` maps the fixed roster and match DTOs; `MatchClientState`
only validates/renders received state. The composable `MatchPanel` keeps ENet
alive in the Lobby scene and sends intents through `LobbyTransport`. Godot's poll
timer requests Core progress; it never calculates authoritative time/points.

`QuestionDeck` filters categories and interleaves shuffled category/difficulty
buckets without replacement. `FullMatch` owns settings, four-round scheduling,
statistics and tie-break eligibility/winners. Only eligible participants count
toward question completion. Sudden death keeps normal totals and compares host
receipt durations. `OneQuestionMatch` remains a tested legacy Phase 04 API;
production uses `FullMatch`. No Godot reference was added to Core.

Suggested namespaces:

```text
Game/
Players/
Questions/
Rounds/
Scoring/
Cards/
Missions/
Teams/
Rules/
Randomness/
Time/
```

Important domain models:

- `GameSession`
- `GameConfiguration`
- `Player`
- `PlayerId`
- `Team`
- `Round`
- `QuestionDefinition`
- `QuestionInstance`
- `AnswerSubmission`
- `QuestionResult`
- `ScoreState`
- `ConfidenceLevel`
- `StreakState`
- `ChaosCard`
- `SecretMission`

Services:

- `GameStateMachine`
- `ScoreCalculator`
- `QuestionSelector`
- `SubmissionValidator`
- `ChaosCardResolver`
- `MissionEvaluator`

Interfaces:

```csharp
public interface IQuestionRepository { }
public interface IRandomSource { }
public interface IGameClock { }
public interface IGameEventSink { }
```

Do not add an interface for every class. Use interfaces at real boundaries.

## 5. QuizParty.Infrastructure

Phase 05 adds shared Content/QuestionPackLoader validation and immutable Core
QuestionPack/category models. The CLI uses strict filesystem UTF-8 reading; Godot
QuestionPackContent uses FileAccess inside res:// and calls the same validator.
Only a reviewed definition is injected into LobbyHost; production code contains
no trivia fallback. Canonical content is staged only after local validation.

Responsible for external concerns:

- JSON question loading.
- Save/settings persistence.
- Networking transport adapters where Godot dependency is avoidable.
- LAN discovery services.
- Logging adapters.
- Platform/device helpers.

If Godot APIs are required, implementation may live in `QuizParty.Godot/Networking` while the interface remains in Core/appropriate abstraction layer.

## 6. QuizParty.Godot

Godot project containing:

```text
Scenes/
UI/
Scripts/
Networking/
Audio/
Themes/
Localization/
Assets/
Autoloads/
```

Recommended autoloads should be few and focused:

- `AppRoot` / composition root
- `SceneRouter`
- `AudioService`
- `NetworkFacade` if lifecycle makes it appropriate

Avoid using autoloads as global dumping grounds.

## 7. Presentation pattern

Godot scene scripts should coordinate views, not own domain rules.

Bad:

```text
QuestionScreen.cs calculates score, picks next question, mutates player streak,
handles packets and writes settings.
```

Good:

```text
QuestionScreen.cs
  -> sends user intent to application/game coordinator
  -> renders immutable/DTO state
  -> plays animation/audio based on events
```

## 8. State machine

Authoritative game phases:

```text
Boot
MainMenu
Lobby
GameStarting
RoundIntro
QuestionActive
QuestionLocked
AnswerReveal
Scoreboard
RoundEnd
GameOver
```

Host is the only authority permitted to advance network game state.

Each transition must define:

- allowed source states,
- target state,
- trigger,
- validation,
- emitted authoritative event/snapshot.

## 9. Player identity model

Never conflate player and connection.

```csharp
public readonly record struct PlayerId(Guid Value);
public readonly record struct ConnectionId(long Value);
```

A player record can contain:

- PlayerId
- DisplayName
- ConnectionId? for remote player
- LocalSlot? for local player
- TeamId?
- IsHost
- Ready state
- reconnect token/session token server-side

One physical connection may eventually own more than one local player. Design data model so this is possible even if first network UI allows one player per phone.

## 10. Time

Core logic must not directly call wall-clock APIs everywhere.

Use an `IGameClock` or pass explicit timestamps/deadlines.

Network answer validity uses **host receive time**, not client-provided time.

Clients render countdown using synchronized/estimated server timing but do not decide whether an answer was late.

## 11. Randomness

Host owns authoritative randomness.

Use injectable `IRandomSource` in Core so tests can be deterministic.

Randomness covers:

- question order,
- card awards,
- mission selection,
- personalized 50/50 removal.

Optional seeded matches can be added for reproducibility.

## 12. Events and snapshots

Prefer explicit game events and snapshots over letting UI query mutable internal objects.

Examples:

- `LobbyChanged`
- `QuestionStarted`
- `AnswerAccepted`
- `QuestionClosed`
- `AnswerRevealed`
- `ScoreChanged`
- `CardAwarded`
- `MissionProgressed`
- `GameFinished`

## 13. Serialization

Network DTOs are separate from domain objects.

Do not serialize complex Godot nodes or internal classes directly.

Rules:

- version messages,
- use primitive/portable fields,
- validate every inbound DTO,
- avoid polymorphic deserialization from untrusted clients,
- bound string/list sizes.

## 14. Persistence

V1 persistence is local and minimal:

- settings,
- audio levels,
- accessibility preferences,
- optional local stats/high scores,
- last display name.

No database is required for MVP. Use JSON/config-style local storage unless profiling or product requirements justify SQLite later.

## 15. Logging

Use structured categories:

- App
- Network
- Game
- Content
- Persistence
- Platform

Never log secrets/reconnect tokens. Avoid logging whole packets in release builds.

## 16. Error handling

- Core: represent expected failures with results/domain errors where useful.
- Network: reject malformed/illegal messages without crashing.
- Content: fail fast with file/question identifiers.
- UI: show user-friendly error and offer retry/back.
- Development: preserve stack traces in logs.

## 17. Dependency policy

Prefer BCL + Godot APIs.

Every new NuGet/plugin dependency must have:

- purpose,
- license check,
- maintained status,
- platform compatibility,
- justification in PR/commit notes if non-trivial.

## 18. Coding style

- Nullable reference types enabled.
- `TreatWarningsAsErrors` considered for Core/tests after baseline is clean.
- `record` / immutable DTOs where appropriate.
- Small methods and focused classes.
- No service locator in domain code.
- No reflection-based magic unless justified.
- Async cancellation tokens for long-running async operations.

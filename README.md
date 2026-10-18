# QuizParty — Project Handoff Package

Product name: **QuizParty**.

Local setup and verification: see [docs/TOOLCHAIN_STATUS.md](docs/TOOLCHAIN_STATUS.md).
The root solution is `QuizParty.sln`; the Godot project is
`src/QuizParty.Godot/project.godot`. Core/desktop target .NET 8; Android
targets .NET 9 because Godot requires .NET 9 or later for C# Android export.

Implemented through Phase 08: platform/LAN foundation, pure C# game rules,
LAN room discovery/browser and optional PIN, manual-IP joining, four-round
matches, no-repeat selection, scoreboards, statistics and sudden-death ties. See
[Match guide](docs/MATCH.md) and [observed evidence](docs/MATCH_EVIDENCE.md).
Questions now load from validated JSON packs, with release gates and one explicitly
human-approved initial question. Normal play therefore offers a one-question
preview; 10/20/30-question starts require enough reviewed content in the selected
categories. Long-match regression uses explicit synthetic debug fixtures.
Disconnect handling is explicit: lobby rejoin creates a fresh seat; an active
match cannot be resumed. Discovery/PIN verified with Windows and physical Android
hosting in both directions. See [Lobby guide](docs/LOBBY.md).
Strategy now includes confidence bets, capped streak bonuses, Chaos Meter,
six host-validated cards and five feasible private missions. Optional Steal is
off by default. See [strategy rules](GAME_DESIGN.md#phase-08-implemented-strategy-balance).
Next is Phase 09: team mode and mixed local/LAN players.

This repository is intended to become a polished Greek-first party trivia game for **Windows and Android**, built with **Godot 4.7.2 .NET / C#**.

The defining product idea is not “another quiz app”. It is a **local-party game** that works offline, supports one-device play and LAN multiplayer, allows mixed local + remote players, and adds strategy through **Confidence Bets, Streaks, Chaos Cards, Secret Missions and team play**.

## Product pillars

1. **Easy to start** — no account and no Internet required for local/LAN play.
2. **Great party experience** — one PC/TV can act as the main screen while phones act as controllers.
3. **Knowledge + strategy** — speed matters, but confidence, timing and limited power-ups create comeback opportunities.
4. **Greek-first quality** — polished Greek UX, strong typography, accurate questions and proper localization architecture.
5. **Deterministic, testable core** — game rules live in pure C# and do not depend on Godot.
6. **Host-authoritative networking** — clients submit intent; the host owns truth, scoring and state transitions.
7. **AI-agent-friendly repository** — durable instructions, small phases, acceptance criteria and verification evidence.

## Target platforms

- Windows 10/11 x64
- Android phones/tablets
- Development platform: Windows
- Engine: Godot 4.7.2 .NET
- Language: C#
- .NET: .NET 8
- Renderer: Compatibility renderer for broad device support

> Important risk: C# Android export must be treated as an early technical spike. Do not build the full game before proving Windows ↔ Android LAN communication on real hardware.

## Start here

Read in this order:

1. `PRODUCT.md` — what we are building and what “done” means.
2. `GAME_DESIGN.md` — rules, modes, scoring and fun mechanics.
3. `ARCHITECTURE.md` — code boundaries, data flow and project structure.
4. `NETWORK_PROTOCOL.md` — authoritative host model and LAN protocol.
5. `CONTENT_FORMAT.md` — question packs and validator rules.
6. `TESTING.md` — test pyramid and release gates.
7. `ROADMAP.md` — full milestone sequence.
8. `PLANS.md` — how Codex must execute multi-step phases.
9. `AGENTS.md` — durable coding-agent rules.
10. `harness/build/` — one implementation phase at a time.

## Definition of final product

The first full release is complete when it provides:

- Local single-device and LAN multiplayer.
- 2–8 players.
- Mixed local + LAN players in the same match.
- Windows host and Android clients.
- Automatic LAN discovery plus manual-IP fallback.
- Optional room PIN.
- PC/TV main-screen mode with phones as controllers.
- Solo, Quick Game, Full Game and Team Mode.
- Multiple Greek categories and difficulty levels.
- At least 1,000 validated Greek questions before public release.
- Confidence x1/x2/x3 mechanic.
- Streak system.
- Chaos Cards.
- Secret Missions.
- Scoreboards, answer reveals and question explanations.
- Settings, audio, accessibility basics and localization infrastructure.
- Automated core tests, Godot integration tests and network tests.
- Windows packaging and Android APK/AAB release builds.
- Local build, test and content-validation gates that block release on failure.

## Non-goals for v1

- Internet matchmaking.
- User accounts.
- Cloud saves.
- Public competitive ranking.
- Microtransactions.
- Always-online DRM.
- Dedicated public servers.
- AI-generated live questions during a match.

Those can be evaluated only after the offline/LAN product is stable.

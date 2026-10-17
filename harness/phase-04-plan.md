# Phase 04 — One-question playable match

## Scope and approach
Baseline Phase 03 committed/pushed as d23468b at user request. Reuse lobby/ENet
and Core GameSession; add a focused host coordinator, separate match DTOs/client
presentation state and a composable question/reveal/score/results panel.
One tiny Greek fixture, 20-second question, Safe x1 only. Host answers as a player.
All answered or host deadline closes the question; host polling reveals/scores once.
Host advances reveal -> scoreboard -> final result. No rematch/scheduling/content
packs/strategy/discovery/reconnect. Disconnected players remain eligible/unanswered
until deadline; no identity reclaim. Host exit ends clients' session visibly.

## Protocol and boundaries
Production version becomes 2: old clients cannot consume match messages, so
reject v1 at hello. Probe remains version 1. Map sender to server-owned player;
never accept a score/player/client timestamp in answer DTO. Capture host receipt
before parsing. Existing bounded request cache makes answer retries idempotent.
No correctness/explanation/results in active/locked public packets or private ack.
Clients only render authoritative scores; countdown is presentation-only.

## Components
Core OneQuestionMatch; Infrastructure match DTOs/client state and LobbyHost bridge;
Godot transport/panel/probe, localization/scenes; deterministic Core/infrastructure
tests, scene tests and source/packaged multi-process match regression.
No new dependencies. Existing lobby/spike regressions stay meaningful.

## Verification and acceptance
Build + relevant xUnit/Godot tests; actual process question/answer/reveal/final
snapshot agreement; invalid/stale/duplicate/late input and version/ownership tests.
Windows/Android debug exports. Install final APK on connected physical phone;
observe real LAN host/client complete match, logs and screenshots. Ask user for
manual taps only if device input restrictions require them. Record actual evidence,
limitations and material decisions in phase context/build log. git diff --check.
Stop at Phase 04; no final commit/push or Phase 05 without user request.

## Risks/recovery
Keep ENet peer/path alive while switching panels; do not change network scene.
Serialize host intents and poll after ENet callbacks; monotonic clock owns timing.
Generation/validity guards cancel transport callbacks. Preserve prior tests and
baseline; new code remains isolated. No firewall/settings/credentials changes.

# Phase 03 — Lobby and networking

## Goal and scope
Implement production protocol v1 handshake/join/rejection, host-owned roster,
ready states, revisioned snapshots and host-only start over reliable ENet.
Baseline a2354ed (Phase 02 + CI removal) committed and pushed at user request.

## Components and approach
- Core LobbySession owns roster/readiness/start rules, separate from transport.
  Host is one participant, initially ready; party start requires 2–8 players and
  everyone ready. This is not Solo or mixed-local/team configuration work.
- Infrastructure contains explicit bounded JSON envelopes/payload DTOs, host
  request router/deduplication/rate limits and client snapshot validation. Sender
  identity comes from ENet, never a packet player ID. Use BCL only.
- Separate Lobby scene and C# view/transport. Keep the Phase 01 probe accessible.
  Responsive Containers, Greek/English localization, touch-friendly controls.
- Reliable ordered RPC path /root/Lobby/Transport. Handshake timeout, graceful
  disconnect cleanup, session-bound requests, monotonic snapshot revisions and
  duplicate-safe ready setters. Start advances only to GameStarting in this phase.
- Host start is local only; remote start requests are explicitly rejected.
- User request authorizes committing/pushing existing work before Phase 03.
  Leave new Phase 03 changes local for review; no final push requested explicitly.

## Non-goals
Discovery, PIN, reconnect tokens, teams/mixed local slots, content/gameplay,
polished final art. No protocol-version bump: this is the first production v1
implementation; the existing spike is explicitly a separate contract.

## Verification and acceptance
- Core rule tests; Infrastructure wire, invalid input, duplicates, session/version,
  bounded caches/rate, ownership/start and client snapshot tests.
- Full build, local xUnit/Godot scene tests, startup smoke, existing spike regression.
- New separate-process host/two-client ENet regression proves identical roster,
  readiness/start snapshots, version rejection, client-start rejection, disconnect
  cleanup and bounded no-host failure. Capture logs under ignored artifacts.
- Inspect Lobby scene/runtime through Godot MCP and capture a screenshot; check
  responsive layout. No new physical Android claim unless actually observed.
- Document protocol compatibility, API, limits, phase decisions/build evidence.
  `git diff --check`; stop at Phase 03.

## Risks / recovery
RPC node paths/signatures must match on both platforms. Bound packet bytes before
JSON parsing; fixed DTOs and no polymorphic deserialization. Disconnect abusive
or unhandshaken peers; bounded request storage. Close peers on scene exit.
No credentials/firewall changes required; test ports differ from normal UDP 7777.
New scene/components are isolated; preserve earlier Core/spike and existing tests.

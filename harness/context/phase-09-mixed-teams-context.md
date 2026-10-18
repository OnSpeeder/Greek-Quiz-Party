# Phase 09 — mixed local/LAN and Team Mode

Baseline Phase 08 committed/pushed as 5268832 on main. User approved Phase 09 only.
Implemented and verified; user subsequently authorized commit and push.
No dependencies, services or GitHub CI added.
Stop before Phase 10 (UI polish, accessibility and reviewed content scale).

## Architecture and material choices

- Core LobbySession now keys by PlayerId, with unique (ConnectionId, LocalSlot).
  The primary slot 0 is retained until the device disconnects; extra slots 1–7
  can be added/removed in lobby. Readiness belongs to each player, never to the
  whole connection. Eight is a logical-player limit, not a connection count.
  Disconnect removes every slot on that connection; started matches still keep
  fixed scores/confirmed answers and reject re-entry under the prior policy.
- Core Players/TeamRoster is immutable, validates exact roster coverage and
  two nonempty teams A/B, and sums individual scores with checked arithmetic.
  Host may enable/disable or reassign teams only in lobby. Initial assignment
  alternates; subsequent adds choose the smaller team. Uneven sizes are allowed
  and scores are not normalized. This was stated as the Phase 09 implementation
  assumption before implementation, along with shared-device handoff.
- FullMatch derives team standings from individual totals, including confidence
  deductions, card effects and mission bonuses before final ranking. Winning
  player IDs include every member of winning teams. A tied team's entire roster
  enters sudden death; fastest correct host receipt selects a team. Equal fastest
  receipts from different teams continue with all their members. All wrong/no
  answer continues. Exhaustion shares victory; normal totals stay unchanged.
  Steal rejects teammate targets. No discussion timer/custom team-name scope.
- Protocol 6/app 0.6.0 rejects 1–5. Server-generated opaque ControllerId groups
  players in public lobby data; native ConnectionId is never transmitted.
  AddLocalPlayer/RemoveLocalPlayer/SetReady/SubmitAnswer/ActivateCard are resolved
  against the actual transport sender and a bounded LocalSlot. No actor/team/
  score/time claims from clients are trusted; SetTeam from a client is NotHost.
- Lobby snapshots broadcast once per connection. Match snapshots are separate
  packets per owned player, selected by top-level LocalSlot, with that player's
  private view only. Answer/card receipts echo slot and correlate to the exact
  pending question/card/request. LobbyClientState keeps up to 8 independent
  MatchClientState objects, clears removed slots, and validates opaque groups,
  immutable teams, final winners and defensive copies. Slot0 convenience APIs
  preserve existing single-controller behavior. DTO defaults support singleton
  test fixtures; actual host snapshots always include controller UUIDs.
- Long shared-controller matches need more than 256 unique requests. Cache now
  bounds 2048 requests and 2 MiB encoded request/reply data per connection, plus at
  most one bounded final record before refusal. No evict-and-reapply behavior.
  Rate remains 32/s. The existing 7000-byte content allowance and 16 KiB packet max
  remain; populated eight-player team finals fit without changing content/schema.
- Godot RosterEditor provides per-device add/remove/ready and host team controls.
  LocalControllerPanel supplies an explicit claim/handoff curtain; submission,
  owner switch or a new question closes private controls. MatchPanel renders
  per-owner answer/pending/time state and public team scores/winners. Confidence
  resets on owner changes; new host sessions collapse the personal panel again.
  The same host question timer runs for all local players, with personal ExtraTime
  exceptions; a 60-second option supports larger shared groups. Containers,
  scrolling, Greek/English localization and 64-unit targets are preserved.
- Debug-only MixedProcessProbe and new network/Android helpers exercise real
  multi-slot play. Final public JSON includes scores/teams/winners/stats/strategy;
  SHA256 digest comparison handles Android's truncated logcat lines. Private
  owner views are checked separately rather than expected to match across slots.
  Normal navigation does not enable bots or synthetic questions.

## Observed checks, 2026-10-18

- scripts/build.ps1 clean, zero warnings/errors; canonical content passes.
- Final scripts/test.ps1 -IncludeGodot: 252 Core + 100 Infrastructure + 7 runtime
  Godot = 359 passed, none failed/skipped. Core covers every 2–8 local/mixed count,
  independent readiness/identity/capacity, team sums/winners/ties/exhaustion,
  strategy/mission totals, teammate Steal rejection and overflow.
- Wire coverage includes multiple slots/controller, foreign/malformed actor
  attempts, per-slot answers/cards/50–50/deadlines, removed identities, defensive
  copies,30-question eight-player play beyond 256 requests, byte limits and
  populated team packet bounds. All existing tests remain; no assertion was
  removed/skipped/weakened. Packet regression was extended to teams.
- Runtime GdUnit drives actual roster controls, Greek local-player creation,
  independent ready/team start, curtain claim/hiding, two answer submissions,
  confidence reset, recap access and new-session host privacy. Early deferred
  QueueFree orphan warnings were fixed by awaiting scene-frame cleanup in tests,
  not suppressing the checker. Final run contains no detected-node warnings.
- Source 20-question team+strategy runs passed: 2 host slots +3 on one client;
  8 local slots on one device (team A 290820/ B 0,21 cards);2 host +2/4 slots on two
  clients (team A 290709/ B 0,21 cards). Every logical player completed, separate
  private owners stayed correct, and public finals agreed.
- Packaged20-question5-player team+strategy passed: team A 212816/ B 0,16 cards.
  Packaged8-player individual/base match (2 host +6 client slots) passed. Base
  preview regression passed Host994/Anna993/Maria0; packaged discovery/PIN gate
  passed broadcast/custom ports/admission/rate/manual IP/rejoin/host exit and
  graceful match departure. Root startup explicitly waited for engine exit and
  observed 'QuizParty: C# startup ready.'; runtime stderr clean.
- Windows/Android debug exports succeeded; APK signature verification passed.
  Known Godot EditorSettings shutdown_adb_on_exit export teardown diagnostic is
  retained, with no new export failure. Android installation returned Success
  and normal launcher returned Status:ok. Godot MCP bridge was offline during
  this phase; real Godot runtime/GdUnit/captures supplied scene evidence.
- Physical Android15/model23013PC75G Wi-Fi192.168.68.106 and packaged Windows
  Ethernet192.168.68.105 passed 20-question5-player team+strategy matches both
  ways: Windows host2 slots/phone client3 slots, team A 212833/ B 0, final digest
  6A677E39C028C7BCDACADCE3D959994A81817B70D30F766DEE5F16EB156E9A08;
  Android host2 slots/Windows client3 slots, team A 212757/ B 0, digest
  D7B9996790F0829B3E310FC36053322C27929B6778AAE64E88FE2380DCE9BDBB.
  Both peers agreed on all public scores/team membership/winners/stats/missions/
  cards. Active phone capture showed the shared-device curtain and three local
  owners, without revealing their prior answers/private panels. Greek desktop
  and physical phone final score/team screens were inspected. No runtime errors.
- Helpers ran sequentially on the phone, removed private debug arguments and
  temporary captures, stopped their Windows peers and restored the normal app.
  run-as ls confirmed no argument file. No ADB forwarding/reverse tunnel, touch
  injection, lock bypass, device/firewall settings or permission changes.
- Evidence: artifacts/phase09-build.log, phase09-tests-final.log,
  phase09-runtime.log, phase09-local-eight.log, phase09-mixed-eight.log,
  phase09-packaged.log, phase09-individual-eight.log, phase09-base-regression.log,
  phase09-discovery-regression.log, phase09-export-*.log, phase09-startup*.log,
  phase09-android*-runtime.log and corresponding phase09-*/ snapshots/logs.
  Final diff/whitespace gates pass; generated platform lockfile churn restored.

## Remaining limitations / boundary

Normal content is still one human-reviewed Greek question. Long tests use
explicit synthetic debug fixtures and add no editorial approvals. More reviewed
content is required for normal10/20/30-question games. Physical coverage uses one
phone with multiple logical players, not multiple physical Android devices.
Handoff interaction is exercised by GdUnit and physical layouts observed; human
touch/balance/play-order evaluation remains later QA. Two fixed teams only; no
team discussion timer, secure reconnect or host migration added. Functional plain
visuals remain until separately approved Phase 10. No known blocking issue in the
approved phase; commit and push authorized after verification.

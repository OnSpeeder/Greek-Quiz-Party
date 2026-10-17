# Phase 03 context — Lobby and network protocol

## Authorization and scope
- User requested commit/push of existing changes, then Phase 03. Commit a2354ed
  (Phase 02 + user-requested CI removal) was pushed successfully to origin/main.
  Phase 03 changes remain local for review; no final Phase 03 commit/push performed.
- This phase implements the first production v1 lobby, separate from the retained
  Phase 01 probe. It ends at GameStarting. No question, answer, scoring, discovery,
  PIN/reconnect, mixed-local/team or final visual design implementation added.

## Architecture and integration decisions
- Core LobbySession owns the fixed party roster (host + up to 7 remote players),
  ready setters, revision and start rules. Host is initially ready; at least two
  players and all ready are required. Solo remains a separate later setup path.
- Infrastructure LobbyHost owns session/player assignment, session-bound request
  routing, receipt/rate bounds and conversion to explicit protocol DTOs. The Core
  lobby never serializes itself. LobbyClientState validates hello correlation,
  session/revision, roster shape and request result correlation. Snapshot arrays
  are copied before returning to views.
- Godot LobbyTransport derives sender from GetRemoteSenderId; it never accepts a
  payload player/connection identity. Only server ID 1 may send client snapshots.
  LobbyScreen only renders state and sends intents. Phase 04 must bridge the lobby
  roster/start to the existing gameplay GameSession without placing rules in UI.
- New composable Lobby scene uses the common /root/Lobby/Transport RPC path. Two
  reliable RPCs carry bounded JSON strings. Main menu retains the Phase 01 probe.
  AppRoot routes opt-in --lobby-* flags through normal exported main-scene startup.
- Names and room names are 1–32 UTF-16 code units, trimmed and without controls;
  input fields enforce lengths. Manual IP/hostname remains available (253 chars).
  JSON packets <=16,384 UTF-8 bytes, depth 8, fixed payloads, unknown fields rejected.
- One peer's ready setter affects only its server-bound player. Same exact ID/JSON
  returns original receipt; changed JSON with reused ID rejects. 256 receipts per
  connection are retained without eviction; hitting the bound disconnects rather
  than permitting old mutations to be reapplied. Rate: 32 messages/second; three
  malformed/conflicting-ID strikes disconnect. Full details in NETWORK_PROTOCOL.md.
- Twelve total ENet/host-router connection slots reserve admission capacity to
  reject a full 8-player lobby explicitly. Unhandshaken peers time out after 10s.
  Client join timeout is also 10s. Generation + Godot instance-validity guards
  cancel callbacks after stop/free; tested by freeing a join transport and waiting
  beyond its original deadline. Disconnect clears roster entry/cache and broadcasts.
- Host start is local only; a real remote StartGame RPC request is rejected NotHost.
  Start increments revision and publishes GameStarting via a snapshot, once. New
  joins/readiness reject after start. No gameplay eligibility/reconnect policy is
  implied by the connected roster being updated after GameStarting departures.
- The first portrait capture exposed the old desktop canvas shrinking controls.
  Reusable ResponsiveCanvas chooses logical 480x800 portrait or 1152x648 landscape,
  updates on window size/orientation, while Containers/scrolling handle layout.
  Setup fields hide after joining so roster/actions remain visible. UI keys have
  Greek and English translations; generated translation resources were refreshed.
- No new NuGet packages/plugins/services or Android permissions added. Core remains
  net8.0 and Godot-free; Android game export remains net9.0 per established constraint.

## Observed verification — 2026-10-18, Europe/Athens
- `scripts/build.ps1`: six projects built, zero warnings/errors.
- `scripts/test.ps1 -IncludeGodot`: 193 Core + 22 integration + 3 Godot scene tests
  passed (218 total), none failed/skipped; production rebuild zero warnings/errors.
  A minor test-analyzer collection-count warning was corrected, not suppressed.
- `scripts/test-network-lobby.ps1`: source-engine host/two-client ENet check passed.
- `scripts/export.ps1 -Platform Windows`, then
  `scripts/test-network-lobby.ps1 -Packaged`: final exported host/two-client check
  passed, including freed-join cancellation. Both source and packaged runs observed
  revision 6 with roster Anna:True|Host:True|Maria:True on all three processes,
  remote start rejection, duplicate ready setters, late/version rejection,
  departure cleanup to host-only revision 8, host exit and no-host timeout.
- `scripts/test-network-spike.ps1`: existing action/ack, duplicate, incompatible
  version and no-host checks passed. No game/network runtime stderr errors.
- `scripts/smoke.ps1`: import and main-scene startup passed; C# startup marker seen.
- Final Android debug export passed with new lobby/JSON components, including
  timer guards. APK generated under artifacts/exports/Android. No install/phone
  lobby interaction was performed or claimed. Phase 01 hardware evidence stands.
- Graphical Windows host/client captures inspected at 1152x720 and 390x844 in
  Greek. Both show all three ready players and start-confirmed status. Portrait
  title wraps and actions remain usable. Final screenshots:
  artifacts/phase03-desktop-final.png and artifacts/phase03-mobile-final.png.
- Original simultaneous graphical capture emitted a GLES shader-cache read
  diagnostic on the host. Repeated captures with one renderer at a time had empty
  stderr and rendered correctly; no application error was observed in final checks.
- Godot MCP info/toolset/scene inspection worked. Additional enabled mutation/
  screenshot toolsets were not exposed in this client catalog. The optional MCP
  debug-workflow helper stalled and was canceled; it is not counted as a passing
  check. Local scene tests, direct ENet processes and viewport captures supplied
  actual runtime evidence. No user editor process was terminated.
- The established EditorSettings shutdown_adb_on_exit diagnostic still appears
  only during editor/import/export teardown. Scripts retain it; it is not hidden
  or counted as a gameplay failure. Runtime network stderr checks passed.
- Protocol guide updated with first v1 compatibility contract and exact bounds.
  Raw logs/builds/screenshots remain ignored artifacts, not production content.
- `git diff --check` passed; new source/script whitespace scan found no matches.
  Restore/export-only lock-file churn was reverted to the committed baseline;
  no dependencies changed. After pushing its removal, GitHub API reports zero
  registered workflows and zero active workflows; CI remains off.

## Boundary and limits
Phase 03 acceptance met through local automated and real multi-process evidence.
No physical Android lobby or multiple-Android test is claimed. Phase 04 (one-question
vertical slice) requires separate user approval and Windows/Android gameplay
verification. Stop here. Do not re-enable GitHub CI.

# Phase 01 context — Windows/Android ENet spike

## Scope and architecture
- User approved Phase 01 and commit/push before and after it. Foundation commit
  c710604 was pushed first; its GitHub Actions run 39065537445 passed.
- Main foundation scene links to a separate LanSpike scene. LanSpikeScreen renders
  UI and sends intents; LanSpikeTransport owns Godot networking lifecycle/RPCs;
  Infrastructure.Networking.ProbeInbox validates version/connection/request IDs
  and deduplicates the disposable action. Core remains Godot-independent and no
  domain/game rules were added. This is not the future lobby implementation.
- Reliable ENet uses UDP 7777, max 7 clients; server ID 1 is authority. RPC nodes
  have the same /root/LanSpike/Transport path on both platforms. The probe protocol
  is separate from the planned production v1 contract (NETWORK_PROTOCOL.md).
- Host counts only new valid requests, returns original receipts for duplicates,
  caches at most 256 IDs per connection, and revokes access on disconnect.
- UI uses Containers/scrolling, localized labels and >=64-unit input targets.
  Send waits for an acknowledgement before permitting another UI press. Plain
  visuals are intentional Phase 01 scope, not the selected final art direction.

## Important platform findings
- Official Windows export templates reject a scene-path override on the command
  line (disable_path_overrides). Packaged host flags are routed by AppRoot through
  normal main-scene startup. Do not launch packaged builds with a positional scene.
- Export command: QuizParty.exe --headless -- --spike-host (port override optional).
- Android C# net9.0 export/install and Windows net8.0 export both work with the
  pinned SDK/engine. Existing INTERNET permission is sufficient on this phone.
- Phone model 23013PC75G / Android 15 blocks ADB input injection. User manually
  entered host IP and pressed the action button; ADB was used for install/logs/
  screenshots only. No port forwarding/reverse tunnel was used for LAN evidence.
- Real interfaces: Windows Ethernet 192.168.68.105, phone Wi-Fi 192.168.68.106.
  Windows had VPN adapters, but actual direct LAN routing succeeded. No firewall
  rules or VPN settings were changed. Firewall rule inspection lacked permission;
  actual ENet connection demonstrated it was not a blocker in this environment.
- Existing engine shutdown_adb_on_exit teardown diagnostic persists during import/
  export, as documented previously. Game/network process stderr was clean.

## Observed evidence (2026-10-17, Europe/Athens)
- Build: 0 warnings/errors. Automated tests: 1 Core + 5 Infrastructure/configuration
  + 2 Godot scene tests passed; none skipped.
- Separate-process ENet regression passed handshake/action/ack, duplicate same
  receipt without count increment, version-99 rejection and bounded no-host failure.
- Physical Android client at 23:16:04 logged CLIENT_READY, then at 23:16:09 logged
  CLIENT_ACTION_SENT and CLIENT_ACK count=1. Packaged Windows host logged matching
  HOST_HELLO accepted=True and HOST_ACTION count=1 duplicate=False.
- Phone screenshot was inspected: actual entered host IP, acknowledgement and host
  count 1 were visible. After host termination, phone logged SERVER_DISCONNECTED
  at 23:17:04. Both apps remained stable; no game/network startup exception observed.
- Final exports were regenerated and final Android APK installed/launched. Debug
  APK signature verified. Raw evidence remains under ignored artifacts/phase01-*;
  durable excerpts/acceptance record are in docs/LAN_SPIKE_EVIDENCE.md.
- Final-build repeat: manual join at 23:18:49, action acknowledgements 1 and 2 at
  23:18:50/23:18:53; matching packaged-host actions observed. User confirmed test.

## Boundary and limitations
One physical Android phone was available. Two Android clients and varied routers/
devices remain future coverage, not claimed verified. No production lobby,
discovery/PIN/reconnect, content, questions, score, cards, teams or missions exist.
Phase 02 requires separate approval; the Phase 01 action counter is not a score.

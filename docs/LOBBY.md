# Phase 03 lobby

From the main menu choose **Παιχνίδι στο τοπικό δίκτυο / LAN party lobby**.

1. Host enters their name and a room name, then creates the room (UDP 7777).
2. Other players on the same LAN enter their name and the host's LAN IP, then join.
   The host shows local addresses; select the actual LAN interface, not a VPN.
3. Remote players choose ready. The host can also change their ready state.
4. With at least two players and everyone ready, only the host can start.
5. Phase 04 now continues into the one-question match. See [Match guide](MATCH.md).
   The retained lobby-only regression explicitly stops at GameStarting.

Disconnect closes the current session on that device. Back returns to the main
menu and closes its peer. A host exit disconnects everyone. A departing client
is removed from the roster. Joining a started/full room and incompatible protocol
versions show rejection. Discovery/PIN/reconnect and mixed local/team UI are later
phases; manual IP remains supported.

Setup fields hide after connection so the roster and ready/start controls stay
visible. Containers/scrolling and orientation-aware logical canvases support
desktop landscape and phone portrait; all action targets are at least 64 logical
units. Plain visuals are intentional until the later UI/art phase.

## Local verification

```powershell
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
./scripts/test-network-lobby.ps1
./scripts/test-network-spike.ps1
./scripts/smoke.ps1
```

For exported Windows builds: `./scripts/export.ps1 -Platform Windows`, then
`./scripts/test-network-lobby.ps1 -Packaged`. This uses normal exported startup,
without scene-path overrides disallowed by official templates.

The lobby regression uses UDP 17778 and checks a host/two actual ENet client
processes on loopback. It does not substitute for a future physical Android lobby
test. Logs live in ignored `artifacts/phase03-network/`. Scene tests check bounded
inputs and touch-sized controls; protocol tests exercise JSON, session/ownership,
duplicates, rate/cache limits and client snapshots.

Opt-in launch flags route through normal AppRoot startup, including exports:
`--lobby-host` or `--lobby-join=IP`, `--lobby-name=Name`, `--lobby-port=7777`.
Pass flags after Godot's `--`. Test-only flags `--lobby-auto`,
`--lobby-test-start`, `--lobby-exit-start`, `--lobby-protocol=99` drive regression;
`--lobby-cancel-join` verifies a freed transport outlives no stale timeout callback;
they are never selected during normal menu navigation. `--lobby-capture=PATH`
captures a rendered viewport for visual inspection; use a graphical renderer.

See [protocol contract](../NETWORK_PROTOCOL.md) and the Phase 03 context/build log
for exact observed evidence and platform limits.

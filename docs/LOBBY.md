# LAN lobby, discovery and PIN

## Current user flow — 2026-10-25

1. Home: «Δημιουργία» / «Συμμετοχή».
2. Participation: «Διαθέσιμες Αίθουσες», icon-only Back/refresh, room name and count.
3. Protected room: PIN popup; wrong PIN returns to rooms with an error. Unprotected
   rooms skip the prompt. PIN is optional and rate limited, not encryption.
4. Successful host preflight opens name + eight-character selection. Occupied
   characters are greyed/disabled and refreshed. No player or reservation exists yet.
5. Icon-only join submits the final claim. Host resolves races; a losing claim
   stays at character selection with an error, refreshed choices and the name intact.
6. Host/shared-device players use the same character catalog and uniqueness rule.

Back closes the PIN popup or returns identity selection to rooms. From rooms it
returns home. Input fields stay scrollable above Android keyboard in either
orientation. Manual IP is intentionally absent from the normal menu; the retained
transport API and test probes still support it. All peers require production v7.

The sections below retain earlier implementation/test history. References to a
visible manual-IP control or entering the name before discovery describe the old
flow and are superseded by this section.


From the main menu choose **Παιχνίδι στο τοπικό δίκτυο / LAN party lobby**.

1. Host enters their name/room name and optionally a 4–6 digit PIN, then creates
   the room (game UDP 7777; discovery UDP 7778).
2. Other players enter their name, choose **Find rooms**, enter the room PIN if
   required, and select a room. Full/started rooms are disabled. If discovery
   finds nothing or fails, enter the host's LAN IP and use **Join by IP**.
   The host shows local addresses; select the actual LAN interface, not a VPN.
3. Each device can add extra local players (up to eight players total), remove
   its extra slots and mark each of its players ready independently. The primary
   slot stays until that device leaves. Host can enable Team Mode and assign
   each player to Team A/B; both teams must have players before starting.
4. With at least two players and everyone ready, only the host can start.
5. Start continues into the configured match. See [Match guide](MATCH.md).
   The retained lobby-only regression explicitly stops at GameStarting.

Disconnect closes the current session on that device. Back returns to the main
menu and closes its peer. A host exit disconnects everyone. A departing client
has all of its local players removed from the lobby roster. A lobby rejoin gets a fresh identity and must
set ready again. Active matches cannot be resumed: departed names are shown,
confirmed answers/scores stay, and missing answers expire normally. Host loss
shows room-closed guidance. This is Phase 07's graceful-disconnect baseline;
no reconnect token, seat reclaim or host migration is enabled.

PIN input is masked and optional. Both browser and manual joins use the same
host admission gate. Wrong/missing PIN is rejected; after five failed guesses
from one source within 30 seconds, wait up to 30 seconds before trying again.
PINs are not encryption. Discovery advertises only whether a PIN is required.
The browser searches for five seconds, expires stale rooms, and can be refreshed.
Discovery never replaces host-side capacity, state or compatibility checks.

Setup fields hide after connection so the roster and ready/start controls stay
visible. Containers/scrolling and orientation-aware logical canvases support
desktop landscape and phone portrait; all action targets are at least 64 logical
units. Plain visuals are intentional until the later UI/art phase.

## Local verification

```powershell
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
./scripts/test-network-lobby.ps1
./scripts/test-network-discovery.ps1 -Capture
./scripts/test-network-spike.ps1
./scripts/smoke.ps1
```

For exported Windows builds: `./scripts/export.ps1 -Platform Windows`, then
`./scripts/test-network-lobby.ps1 -Packaged`. This uses normal exported startup,
without scene-path overrides disallowed by official templates.

Also run `./scripts/test-network-discovery.ps1 -Packaged -Capture`. It checks real
UDP broadcast/custom port, wrong/missing/correct PIN, limits across reconnects,
manual fallback, fresh lobby identity, started metadata, host exit and a departed
match seat's timeout. No relay or Internet service is involved.

For actual awake/unlocked Android hardware after export/install:

```powershell
./scripts/test-android-discovery.ps1 -HostAddress <actual-Windows-LAN-IPv4>
```

The phone and Windows each host, broadcast-discover the other, reject wrong PIN
and admit correct PIN. Phone manual IP, fresh lobby rejoin and host exit are
checked. ADB only installs/launches, supplies app-private debug arguments and
observes logs/screenshots; no network tunnel, touch injection or settings changes.
The helper removes its private arguments/screenshots and restores normal startup.

The lobby regression uses UDP 17778 and checks a host/two actual ENet client
processes on loopback. Discovery evidence is in `artifacts/phase07-network*` and
actual phone evidence in `artifacts/phase07-android/`. Scene tests check bounded
inputs and touch-sized controls; protocol tests exercise JSON, session/ownership,
duplicates, rate/cache limits and client snapshots.

Opt-in launch flags route through normal AppRoot startup, including exports:
`--lobby-host` or `--lobby-join=IP`, `--lobby-name=Name`, `--lobby-port=7777`.
Pass flags after Godot's `--`. Test-only flags `--lobby-auto`,
`--lobby-test-start`, `--lobby-exit-start`, `--lobby-protocol=99` drive regression;
`--lobby-cancel-join` verifies a freed transport outlives no stale timeout callback;
they are never selected during normal menu navigation. `--lobby-capture=PATH`
captures a rendered viewport for visual inspection; use a graphical renderer.

Phase 07 debug-only flags: --lan-host / --lan-find / --lan-join=IP,
--lan-port=7777, --lan-discovery-port=7778, --lan-pin=TESTPIN,
--lan-scan-only, --lan-name=Name, --lan-stay, --lan-start-players=2,
--lan-match, --lan-leave-question, --lan-expect-empty, --lan-capture=PATH.
They route through normal AppRoot and the existing debug-only private argument
file on Android (12 flags/4096 bytes). Release builds ignore --lan-* automation.

See [protocol contract](../NETWORK_PROTOCOL.md) and the Phase 03 context/build log
for exact observed evidence and platform limits.

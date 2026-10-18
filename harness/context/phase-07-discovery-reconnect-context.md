# Phase 07 — discovery, PIN and graceful disconnect

Baseline Phase 06 pushed as 153c835. User approved Phase 07 only; new work stays
local/uncommitted and Phase 08 is not started. GitHub CI stays disabled.

## Chosen scope and architecture

Use the phase's explicitly permitted documented graceful-disconnect option.
No token recovery, automatic reconnect or host migration is enabled. In lobby,
departure clears seat/readiness/cache and rejoin creates a fresh PlayerId. During
a match, re-entry is rejected GameStarted, confirmed answers/scores remain, and
missing answers time out on the original host clock. MatchPanel compares the
authoritative connected lobby roster with fixed match scores and labels departed
names. Host loss ends clients with non-resumable-room guidance. This avoids
introducing partial identity/answer recovery into the fixed-roster coordinator.
Future reconnect work must explicitly implement/test secure identity reclaim.

Core game/scoring unchanged. Infrastructure owns bounded discovery codec,
catalog/clock and reply limiter, and RoomAdmission. Godot LanDiscovery owns an
independent PacketPeerUdp socket/timer, RoomBrowser renders rooms, LobbyTransport
keeps ENet authoritative. Dynamic controls use Containers, masked numeric PIN
input and 64 logical-unit targets. Status is beside PIN and scrolled into view.

## Discovery contract

Protocol 4/app 0.4.0, strict exact-field JSON. Version 1/2/3 incompatible. Separate
UDP 7778 by default, IPv4 bind 0.0.0.0. Browser binds an ephemeral port, sends real
255.255.255.255 broadcast at 1Hz for five seconds, host unicasts current metadata
to its source endpoint. No advertised address, PIN, hash or token. Use source IP
and advertised gameplay port on join. Hosts advertise Lobby/GameStarting; full/
started rows disable join. A discovery failure leaves ENet/manual IP usable.

1024-byte packets/depth 4; reject malformed/unknown/duplicate/missing fields,
bad Unicode, versions, IDs, bounds and types. Catalog current nonce only while
scan active, max 32 session/source pairs, dedup updates, six-second room TTL,
clear on refresh/stop/scene exit. Replies limited to four/source/second and 32
globally; poll consumes at most 16 datagrams per 100ms. No async background work
or additional dependencies. Existing gameplay socket lifecycle stays separate.

## PIN contract

ClientHello adds optional Pin (empty means no PIN supplied). Host validates empty
or 4–6 ASCII digits, hashes configured value in memory and uses fixed-time hash
comparison. PIN is admission convenience, not encryption. Never echo or log it;
discovery publishes RequiresPin only. Full/started/version rejection precedes PIN.
Five bad/missing guesses per actual ENet source IP per 30-second monotonic window
temporarily block even correct guesses; 100 global failures bound multi-address
attempts/state. Limits survive disconnect/new connection. Exact cached duplicate
requests do not charge twice. Native sender address is passed by LobbyTransport,
never accepted from client JSON. Existing handshake/rate/cache/ownership checks
remain. Open rooms still work with empty PIN, preserving manual-IP workflow.

## Verification and hardware

292 passing tests: 208 Core, 79 Infrastructure, 5 Godot. Full local test script
and final extra confirmed-answer departure regression passed. GdUnit checks
discovery composition, masked/bounded PIN and touch target alongside existing
scene/relay tests. No failing test skipped/weakened. A clean rebuild surfaced two
pre-existing nullable warnings in the Phase 06 test; snapshots already asserted
present now use explicit null suppression. Final builds have zero warnings/errors.

scripts/test-network-discovery.ps1 (source and -Packaged -Capture) passed actual
broadcast/custom game port, scan metadata, wrong/missing/correct PIN, rate limits
across new connections, manual IP, fresh lobby rejoin, started advertisements,
host exit, no-room fallback, match re-entry rejection and departed-seat timeout.
Packaged departure example: Host 994 / Phone 0, revision 6, Phone unanswered 1.
Packaged lobby and 30-question regressions passed (Host 29911 / Anna 29818 /
Maria 0, rev184); source 20-question regression also passed. Smoke passed.

Windows/Android exports, APK signature, install/launch passed. Physical Android
15/model 23013PC75G, Wi-Fi 192.168.68.106; Windows Ethernet 192.168.68.105.
scripts/test-android-discovery.ps1 -HostAddress 192.168.68.105 passed over actual
LAN on game17789/discovery17790. Phone broadcast-discovered Windows, rejected
wrong PIN, joined correct PIN and manual IP with a different fresh player ID,
then observed host exit. Windows broadcast-discovered phone host; phone rejected
wrong PIN and admitted Windows. No multicast permission/device settings/firewall
change, tunnel, network forwarding or input injection. Private debug arguments
and screenshots removed, normal app restored; removal checked with run-as ls.

Screenshots inspected: localized room/PIN flag, explicit wrong-PIN message beside
input, actual Android host roster and Greek departed-player banner on Windows.
Long pages use scrolling; no claim of human touch play or other router/device
coverage. Logs/screenshots: artifacts/phase07-network*, phase07-android,
phase07-tests-final.log, phase07-integration-final.log, phase07-smoke.log and
phase07-export-*.log. Known Godot editor/export shutdown_adb_on_exit teardown
diagnostic persists and is retained; game runtime error scans are clean.

## Regression drivers and future work

LanProcessProbe is explicit debug-only --lan-* automation. Android reuses the
existing app-private phase04-test-args.json mechanism (12 flags/4096 bytes), now
allowing --lan-* alongside --match-*. Normal navigation and release builds do
not enable LAN automation. Production data still has one reviewed question;
long matches remain synthetic test fixtures until more content is human-reviewed.

No new dependencies, services, content, permissions or signing changes. Safe
match resumption remains future work; LAN broadcast depends on network policy,
so manual IP is retained. Stop before separately approved Phase 08 strategy work.

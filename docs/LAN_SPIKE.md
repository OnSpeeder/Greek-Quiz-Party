# Phase 01 LAN technical spike

This disposable screen proves Windows/Android Godot C# + ENet compatibility.
It is intentionally plain and does not implement the selected final art direction,
production lobby, discovery or game rules.

## Run

1. Build/export using scripts/build.ps1 and scripts/export.ps1 for Windows/Android.
2. Install the Android APK using scripts/android-install.ps1; approve on the phone
   if its operating system requires installation confirmation.
3. Put PC and phone on the same home LAN. No internet/account is needed.
4. On Windows open **LAN connection test**, then **Start host**, or run
   `./scripts/run-spike-host.ps1 -Packaged` for a logged headless host on UDP 7777.
5. On Android open **LAN connection test**, enter the Windows LAN IPv4 address in
   the address field, and tap **Join by IP**. Use the PC's actual LAN interface,
   not a VPN/WSL address. No USB tunnel is part of this test.
6. After the connected status appears, tap **Send test action**. The host logs
   `HOST_ACTION ... count=1 duplicate=False`; the phone shows acknowledgement
   and the authoritative host count. Repeat to test additional actions.
7. Disconnect, rejoin or stop the host to observe the error/status paths.

Controls are localized in Greek/English and use Containers plus 64-unit minimum
input/button heights. The scene scrolls on smaller displays. Private LAN firewall
access for UDP 7777 may need OS approval; never disable the firewall globally.

## Automated checks

```powershell
./scripts/test.ps1 -IncludeGodot
./scripts/test-network-spike.ps1
./scripts/smoke.ps1
```

Network regression uses separate Godot processes on loopback UDP 17777. It checks
handshake/action/ack, duplicate safety, incompatible-version rejection and an
unreachable-host timeout.
Its scripts use bounded waits and fail on engine errors or absent evidence.
These checks do not substitute for the physical Android/manual-IP acceptance test.
Run this regression locally; GitHub CI is disabled by project decision.

The contract and compatibility boundary are documented in NETWORK_PROTOCOL.md.
Observed hardware results and any setup limitations belong in the Phase 01 context
and build log, not assumptions in this guide.

Observed Phase 01 acceptance is recorded in [LAN_SPIKE_EVIDENCE.md](LAN_SPIKE_EVIDENCE.md).

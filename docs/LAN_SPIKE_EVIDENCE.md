# Phase 01 observed acceptance evidence

Date: 2026-10-17 (Europe/Athens). Windows 10 host, Godot 4.7.2 .NET; physical
Android 15 phone, model 23013PC75G. Development APK package org.quizparty.game.

## Automated verification

- Restore/build: zero warnings, zero errors.
- Core tests: 1 passed. Infrastructure/configuration tests: 5 passed.
- Godot C# scene tests: 2 passed. No tests skipped.
- Separate-process Windows ENet test: passed handshake, action/ack, duplicate
  handling, incompatible protocol rejection, unreachable-host timeout.
- Main scene headless smoke: C# startup marker observed.

Duplicate/network test excerpts (same host action, two client submissions):

```text
LAN_SPIKE HOST_ACTION peer=210349041 count=1 duplicate=False
LAN_SPIKE HOST_ACTION peer=210349041 count=1 duplicate=True
LAN_SPIKE CLIENT_ACK count=1
LAN_SPIKE CLIENT_ACK count=1
LAN_SPIKE AUTO_PASS duplicate_ack_count=2
LAN_SPIKE HELLO_REJECTED
```

Peer IDs above are ephemeral transport connection IDs, not player identifiers.

## Actual LAN/hardware acceptance

- Windows debug executable exported and launched as the host, binding UDP 7777.
- Android APK exported, debug signature verified, installed and launched with ADB.
- User entered the Windows Ethernet IP in the phone UI and joined from Wi-Fi.
  USB was only used for installation and observation; no networking tunnel.
- Phone button press reached the Windows process and the host receipt reached
  the phone. The acknowledgement and host count were visually inspected.

Windows packaged host log:

```text
QuizParty: C# startup ready.
LAN_SPIKE HOST_LISTENING port=7777
LAN_SPIKE HOST_HELLO peer=1307341391 accepted=True
LAN_SPIKE HOST_ACTION peer=1307341391 count=1 duplicate=False
```

Android application log (local time):

```text
23:16:04.890 LAN_SPIKE CLIENT_CONNECTING address=192.168.68.105 port=7777
23:16:04.985 LAN_SPIKE CLIENT_READY
23:16:09.690 LAN_SPIKE CLIENT_ACTION_SENT
23:16:09.717 LAN_SPIKE CLIENT_ACK count=1
23:17:04.129 LAN_SPIKE SERVER_DISCONNECTED
```

The last line was observed after intentionally stopping the Windows host. No
firewall/VPN changes were needed. Full logs/screenshots/builds are local ignored
artifacts, with this text preserving reviewable evidence in the repository.

Final regenerated Windows/Android builds were then tested again. The user joined
and pressed the button twice; the Windows host recorded counts 1 and 2 for peer
2108548443. The final phone log recorded:

```text
23:18:49.141 LAN_SPIKE CLIENT_CONNECTING address=192.168.68.105 port=7777
23:18:49.202 LAN_SPIKE CLIENT_READY
23:18:50.786 LAN_SPIKE CLIENT_ACK count=1
23:18:53.410 LAN_SPIKE CLIENT_ACK count=2
```

The user confirmed completion of that repeat check. This is evidence for the
final implementation, including the wait-for-ack button state and normal-entry
packaged-host launch path.

## Limits

One real phone and one LAN were tested. Multiple Android clients, other routers,
production protocol, actual trivia gameplay and release-grade hardening are not
part of this phase. Existing documented editor/export teardown diagnostic remains;
no equivalent error occurred in the running network host/client.

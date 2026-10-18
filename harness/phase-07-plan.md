# Phase 07 — LAN discovery, PIN and graceful disconnect

Baseline: Phase 06 pushed as 153c835. Goal: discover LAN rooms, join through a
browser or manual IP with optional PIN, and make disconnect/rejoin behavior clear.

- Inspect current host/client/scene lifecycle and protocol; preserve existing rules.
- Infrastructure: bounded discovery codec, nonce/TTL room catalog and host rate
  limiter with injected clock; PIN admission validation/rate limiting across new
  transport connections. Protocol 4 because ClientHello gains PIN.
- Godot: separate UDP discovery node (7778 by default), dynamic host metadata,
  touch-friendly browser/refresh controls and shared masked PIN input. Joining a
  discovered entry uses its observed source address and advertised game port.
- Keep manual IP and ENet gameplay independent if UDP discovery is unavailable.
- Use the phase's documented graceful-disconnect variant: lobby rejoin creates a
  fresh identity/readiness; match seats/scores remain fixed and missing answers
  time out. Show departed players; host exit ends clients. No identity/answer
  reclaim tokens or automatic reconnect are enabled or claimed.
- Test malformed/oversized/version/nonce packets, room expiry/capacity, PIN
  missing/wrong/rate limits, secret non-disclosure, rejoin and match departures.
- Build, local tests/GdUnit, actual UDP + ENet process tests, manual-IP/full-loop
  regressions, Windows/Android export and actual phone LAN discovery/PIN checks.
- Update protocol/guide, phase context and observed build log; stop before Phase 08.

Out of scope: Internet matchmaking, relay services, new content and strategy.
Risks: LAN broadcast/firewall/router behavior and Android broadcast reception;
never silently replace a failed broadcast test with manual-IP evidence. Browser
discovery is untrusted metadata, never admission authorization. PIN is a LAN
admission convenience without encryption. No new dependency/service is planned.
Acceptance: discovery observed on test LAN, manual IP still verified, clear
failure/disconnect UX, all relevant local checks pass. Recovery: preserve pushed
Phase 06 baseline and keep new work as an ordinary local diff; no destructive Git.

Completed implementation and verification. Actual LAN broadcast/PIN admission
passed with both Windows and the physical phone hosting, including phone manual
IP/rejoin/host-exit cases. 292 tests pass. Evidence in phase context/build log.

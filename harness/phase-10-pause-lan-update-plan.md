# Phase 10 — pause on disconnect and LAN updates

1. Freeze host-owned game time and actions on match device loss; retain device identities for the match lifetime.
2. Resume on unanimous connected-seat votes or host override; when all missing seats return, run an authoritative five-second countdown. Missing players do not block untimed questions after override.
3. Add bounded protocol state, version compatibility, private-safe snapshots, localized responsive pause/countdown UX and reconnect retries.
4. Design a simple LAN update folder and startup client with platform-compatible package installation, integrity/authenticity, failure recovery and tests.
5. Verify core/integration/Godot/network and actual Windows/Android where possible; document evidence and limits.

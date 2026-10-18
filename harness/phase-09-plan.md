# Phase 09 — mixed local/LAN and teams

Baseline Phase 08 pushed as 5268832. Implement approved Phase 09 only; leave
changes local and stop before Phase 10. No new dependencies/services/GitHub CI.

1. Lobby roster keyed by PlayerId; unique (ConnectionId, LocalSlot). One host
   primary slot and up to eight total players. Every admitted device can add/remove
   extra slots and ready its own players. Disconnect removes that device's slots.
2. Two host-assigned teams A/B, both nonempty at start; uneven sizes permitted.
   Team totals sum individual scores including strategy/mission bonuses. Preserve
   individual stats. Team ties use fastest correct host receipt among tied-team
   members; equal fastest teams continue; exhausted content shares victory. No
   strategy in sudden death; Steal targets opponents only. No discussion timer.
3. Protocol 6/app 0.6.0: opaque controller grouping, bounded local-slot intents,
   per-slot match/receipt routing and owner-only private views. Keep slot 0 APIs,
   manual IP/PIN/discovery and graceful departure. Bound cache count/bytes for
   eight actors per connection; retain16KiB packets and verify team overhead.
4. Composable lobby slot/readiness/team controls and a shared-device match
   handoff/privacy curtain. Switching players hides prior inputs and missions.
   Single-player controllers retain existing UI. Host supplies team scores and
   winners. Localized responsive controls and touch targets throughout.
5. Core2–8 combinations/aggregation/ties/strategy, wire ownership/privacy/
   duplicates/disconnect/budget, Godot UI, source/packaged mixed/local/team full
   matches and physical Android checks. Record evidence/context/build log and
   required gates; production content unchanged. Stop at the phase boundary.

Completed locally 2026-10-18. Protocol 6/app 0.6.0. 359 tests passed; source 8-local
and 8-mixed, packaged mixed/team/individual, and physical Android 5-player full
matches with both hosting roles passed. See context/phase-09-mixed-teams-context.md
and build-log.md for observed evidence. User subsequently authorized commit and
push. Phase 10 remains unstarted.

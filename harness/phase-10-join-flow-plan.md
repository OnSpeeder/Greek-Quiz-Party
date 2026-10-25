# Phase 10 — discovery-first admission and unique characters

Approved 2026-10-25: Creation/Participation home labels; icon-only corner Back,
refresh and join; rooms list with count; optional PIN popup before identity;
name/eight-character selection; host-owned atomic uniqueness and conflict retry;
Android keyboard avoidance. Hide manual IP UI while retaining transport API.

## Approach
- Preserve existing uncommitted presentation/content changes. No content edits.
- Add typed character identity/host uniqueness in Core. Eight entries across host,
  remote and shared-device players; release characters on departure before start.
- Protocol v7: bounded preflight PIN/availability requests without player creation,
  followed by final hello with selected character. Retain direct Join API for
  probes/manual fallback; duplicates and rates use existing host request gate.
- Admission authorization bound to transport connection, expires by injected host
  clock, and never reserves a seat/character. Refresh availability before join;
  host resolves simultaneous final claims and returns refreshed availability.
- Composable JoinFlow/CharacterPicker/PIN popup in native Controls, preserving
  existing hosting and lobby/teams. All displays consume stable character IDs.
- Keyboard-safe scroll/insets based on DisplayServer keyboard height; no global
  Android setting change. Existing rotation and Back/modal rules apply.
- Four original transparent character assets matching existing art, generated
  with built-in imagegen. Keep prompts/provenance alongside the assets.

## Verification and acceptance
Core uniqueness and release; protocol preflight privacy, malformed/bounded payloads,
expiry, duplicates, old version rejection and racing character claims. Local
build/tests, real ENet process gate, GdUnit UI/back/greyed character/keyboard layout
checks, actual portrait/landscape screenshots and available physical Android
checks. Record evidence, failures and limitations in build log/context. Update
PRODUCT, architecture, protocol, lobby/presentation/visual/testing and phase docs.
No phase advancement, publishing or push. Recovery is per-file diff review;
do not revert preceding unrelated work.

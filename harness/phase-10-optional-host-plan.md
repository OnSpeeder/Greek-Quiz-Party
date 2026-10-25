# Phase 10 — optional host player and compact creation (2026-10-25)

Precondition completed: physical Android tests and GitHub checkpoint 05b7edd.
User scope: optional non-playing host, configurable maximum actual players (2–8),
compact room-first creation with always-visible optional PIN; participating hosts
continue to name/character identity then create. Remove selected-character central
checkmarks, repair all tooltips, hide all scrollbars while retaining scrolling, and
prevent overlapping lobby header buttons. Preserve private per-player data.

1. Separate host authority from an optional roster seat in Core/infrastructure;
   validate capacity, admission, ready/start, public observer snapshots and v9 wire.
2. Build compact create/identity steps; constrain character overflow to its list,
   reuse existing character picker/art and theme. Hide scrollbars globally and retain
   wheel/touch/drag. Fix tooltip sizing and header minimum-size layout.
3. Add pure, protocol and scene tests for zero-seat host, capacity, private state,
   workflow/back navigation, header bounds and tooltip behavior.
4. Verify local tests and actual portrait/landscape viewports, then physical Android
   flows and a host-without-player network match. Record evidence; stop at Phase 10.

Assumptions: host without a player is a rendered shared-screen coordinator, not a
console server; it occupies no player/character/team slot and receives no private
hand/mission. Existing minimum of two real players and maximum of eight remain.
The first checkpoint is already pushed; this follow-up stays separately reviewable.

# Local appearance themes — 2026-10-28

The device preference changes the interface palette and tint of the existing
illustrated stage. It is local to each screen and does not affect match state,
question content, answer colors, scoring or another player's device. The default
is Showtime. No new art or external dependencies are introduced.

| Theme | Surface / border | Stage treatment | Character |
| --- | --- | --- | --- |
| Showtime | #242441 / #62668d | original cool violet | Existing gold/cyan game show |
| Bright studio | #14384b / #5b9eb0 | cool blue and cyan lighting | Clear, energetic television studio |
| Midnight neon | #391b4a / #b36dbb | magenta-violet lighting | Saturated late-night show |
| Retro stage | #483020 / #bd9562 | warm amber lighting | Warm vintage studio |

Shared white text, gold primary actions and the four answer shapes/colors retain
recognition across themes. High contrast uses its existing fixed legibility
palette and suppresses decorative stage art. Reduced motion applies independently.
The settings page uses the shared theme and a single responsive composition with
compact header, section navigation, scrollable content and touch-sized controls;
the original illustrated mascot and toggle remain intentional accents.

QA: compare actual host and controller viewports, long Greek text, focus and
selected states, high contrast, and Android hardware. No visual sign-off is
implied by the palette definitions alone.

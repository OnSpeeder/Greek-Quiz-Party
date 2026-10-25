# Character catalog — 2026-10-25

Original IDs 0 Pink, 1 Blue, 2 Orange, 3 Green use the existing
`showtime-crew-v2.png` regions in GameArt. New IDs 4 Purple, 5 Yeti, 6 Coral,
7 Teal use `showtime-extra-crew-v1.png`, a 1254×1254 RGBA atlas with real alpha
(range 0–255), in four equal 627×627 quadrants, row-major. GameArt derives these
regions from dimensions rather than assuming the requested generation size.

Generated with the built-in imagegen tool on 2026-10-25. The original atlas was a
style reference, not an edit target. No asset service, runtime network or external
package was added. The original atlas is preserved. The output was inspected for
four distinct subjects, cell separation and transparent background, then copied
into this project. Character names are localization keys, never baked into art.

## Exact generation prompt

Use case: stylized-concept. Asset type: ONE transparent game character atlas for
QuizParty, a Greek party quiz game. The reference is a STYLE REFERENCE ONLY, not an
edit target. Create a polished 1024x1024 atlas with FOUR NEW DISTINCT friendly
furry monster bust portraits, arranged in a precise 2x2 grid of equal 512x512
cells. Each character entirely inside its own cell, transparent gutters at least
24px, never overlapping another cell. Match the reference's professional cartoon
rendering, expressive large eyes, richly shaded fur, dark purple outlines, warm
highlights, waist-up framing and welcoming personality. Top left: lilac-purple
round monster with one small central horn and star-shaped hair tuft, playful
wink. Top right: fluffy creamy-white yeti with two small rounded ears and a
turquoise bow tie, warm smile. Bottom left: coral-red furry monster with two short
antennae and thick dark eyebrows, cheerful toothy grin. Bottom right: deep-teal
furry monster with small fin-like ears and a sweeping forelock, confident friendly
smile. These must be recognizably different characters, not recolors of the
reference. Characters face the viewer, hands inside their own cell. Actual
transparent alpha background, no shadows outside portraits, no checkerboard, no
text, no labels, no logos, no frames, no scenery. This is ONE atlas resource
consumed as four equal-quadrant portraits.

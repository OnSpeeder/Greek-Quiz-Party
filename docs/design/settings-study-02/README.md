# Settings study 02 — Inkscape

Created 2026-10-19 following the user's rejection of the first implemented
settings UI and the new side-by-side visual mockup request.

- `settings-study-02.svg`: self-contained editable 3200×1800 (16:9) master.
  Four named Inkscape layers retain editable text, vector frames, bevels, rivets,
  controls, flags, confetti and pedestal details. Typography uses Impact.
- `settings-study-02-outlined.svg`: Inkscape export with lettering converted to
  paths for portability. Keep the editable master for copy changes.
- `settings-study-02.png`: full-size Inkscape MCP PNG export.

Inkscape 1.4.4 was used for rendering and outlining. The configured `uvx
inkscape_mcp` server was accessed using a local FastMCP stdio client because its
tools were not directly exposed in the chat. Actual successful MCP operations:
`inkscape_file(validate)`, `inkscape_gradient(set_stop_color)` and
`inkscape_file(convert, png)`. Local evidence: ignored
`artifacts/settings-inkscape/mcp-finish.log` and `review.png`.

Reproducible source geometry: `scripts/create-settings-mockup.py`. The MCP finish
sets the spectrum gradient's 100% stop to `#df64d3`, then exports PNG. All raster
references are embedded, so the delivered SVGs have no external image dependency.

Artwork sources: existing `showtime-stage-wide-v2.png`, `showtime-stage-v2.png`,
and the thoughtful blue character from `showtime-crew-v2.png`. The orange waving
pose reuses `Art/Settings/mascot-orange.png`, previously generated from that crew
identity. Raster illustrations remain raster; UI framing and details are vectors.
No 3D scene, mesh or new image generation was used for this study.

The English labels, duplicated “VOICE VOICE OVER”, flag capsule, illustrative
music/voice/haptic switches and tab icons follow the user's latest mockup prompt.
They are visual content, not new implemented features or product decisions.
No account options. Runtime localization/accessibility requirements still apply
to any later implementation. The previous Godot settings candidate remains
visually rejected; this study has no user sign-off yet.

The user subsequently requested integration into the game. Runtime skins now
derive from this master through `scripts/export-settings-study-skin.py`; text and
controls remain native/localized. The game exposes its supported SFX, language,
accessibility and help/reset controls instead of the mockup-only feature slots.
Latest runtime evidence is in `docs/PHASE10_QA.md` and the Phase10 build log.

Verified: MCP SVG validation, successful Inkscape renders, visual inspection of
the full composition, corrected clipping and tab paths, outlined export and
`git diff --check`. Game code was unchanged in this follow-up; no game tests or
new device export were needed for the mockup deliverable.

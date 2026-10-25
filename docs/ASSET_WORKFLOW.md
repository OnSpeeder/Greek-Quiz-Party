# Asset tools and workflow

Character-catalog update (2026-10-25): four additional original portraits were
generated with built-in imagegen against the existing style reference. The
project-bound RGBA atlas, dimensions, stable IDs and exact prompt are documented
in `src/QuizParty.Godot/Art/CHARACTERS.md`. No paid service or package was added.

Verified on 2026-10-17. Inkscape and Blender were already installed; no reinstall,
upgrade, paid dependency, additional plugin, or user-preference reset was needed.

| Tool | Verified version | Installed executable |
| --- | --- | --- |
| Inkscape | 1.4.4 (dcaf3e7) | C:/Program Files/Inkscape/bin/inkscape.com |
| Blender | 5.2.2 LTS | E:/Blender Foundation/Blender 5.2/blender.exe |

## Agent access

Use project helpers rather than assuming Blender is on PATH:

```powershell
./scripts/inkscape.ps1 --version
./scripts/blender.ps1 --version
./scripts/verify-asset-tools.ps1
```

`scripts/asset-tools.ps1` resolves installed tools using PATH, optional
`INKSCAPE_PATH` / `BLENDER_PATH`, conventional Inkscape location and Blender's
Windows installation registry. It supports the existing custom E: drive install.
No global PATH mutation is required. The agent can write SVG files and Blender
Python scripts and invoke the official command-line interfaces; no extra MCP is
needed for this workflow.

The verification script creates disposable files under ignored
`artifacts/asset-tools/`:

- Inkscape SVG-to-PNG export at 512px, including Greek text.
- Editable Blender `.blend` file.
- Transparent RGBA PNG rendered with Cycles on CPU (256px, eight samples).
- Selected-mesh glTF binary `.glb` export.
- A temporary Godot 4.7.2 import project importing both SVG and GLB, with no
  import errors. Both output images were visually inspected.

Blender runs with `--factory-startup` only for the temporary verification process;
it does not overwrite the user's startup file or preferences. CPU rendering was
verified; GPU rendering and any future third-party addons remain unverified.

## Future game assets

- Use Inkscape for editable vector icons, category marks, badges and card artwork.
- Keep actual UI labels in Godot localization resources, not baked into artwork.
  Greek text in the probe is an export/font check, not a UI-label pattern.
- Use Blender when chosen art needs 3D objects, mascots, trophies or rendered art.
- Keep editable `.blend` sources outside the Godot resource directory and export
  `.glb` into the game. This avoids making Blender a requirement for every game
  build or CI runner. Use transparent PNG for pre-rendered 2D art when appropriate.
- Test advanced SVG features against Godot; use a PNG export when fidelity requires
  rasterization. Keep simple icons vector-based where practical.
- Do not copy verification assets into the game. They establish tooling only;
  the selected Cartoon Showtime direction is defined in design/VISUAL_DIRECTION.md.

Official references:
- https://wiki.inkscape.org/wiki/Using_the_Command_Line
- https://docs.blender.org/manual/en/latest/advanced/command_line/launch/windows.html
- https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html

## Production quality boundary — 2026-10-25

The Blender/Inkscape wrappers and verification fixtures test tool access, export
and import, not artistic quality. They are not part of the game's build/test gate
and must not be used as proof that production artwork is approved. Keep them for
cleanup, export, reproducible vector skins and deliberate geometric icons.

Use the existing illustrated PNG cutouts/stage as the visual baseline. New complex
characters or stages need a visual reference and image/art production followed by
in-engine inspection; stacks of primitives are acceptable only as labelled
blockouts. Do not replace illustrated settings skins with generic flat boxes.
Keep editable sources, provenance/license and export dimensions with new assets.
External generation services require an actual asset need and dependency review;
no upload or paid service is implied by this workflow. A file-existence check alone
is insufficient: verify imports, texture transparency, bounds and device rendering.

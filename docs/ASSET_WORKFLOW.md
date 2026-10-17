# Asset tools and workflow

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
  the game's art direction has not been selected.

Official references:
- https://wiki.inkscape.org/wiki/Using_the_Command_Line
- https://docs.blender.org/manual/en/latest/advanced/command_line/launch/windows.html
- https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html

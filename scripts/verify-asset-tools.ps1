. "$PSScriptRoot/asset-tools.ps1"
$output = Join-Path $RepoRoot 'artifacts/asset-tools'
New-Item -ItemType Directory -Force $output | Out-Null
$svg = Join-Path $output 'vector-probe.svg'
@'
<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <rect x="32" y="32" width="448" height="448" rx="56" fill="#17263d"/>
  <path d="M160 120h192v96a96 96 0 0 1-192 0z M256 312v64 M192 392h128" fill="none" stroke="#f8c34b" stroke-width="20" stroke-linecap="round"/>
  <text x="256" y="450" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="28" fill="white">Δοκιμή εργαλείων</text>
</svg>
'@ | Set-Content -Encoding utf8 $svg
$inkscape = Get-Inkscape
$blender = Get-Blender
& $inkscape --version
Assert-Exit 'Inkscape version'
& $inkscape $svg --export-type=png "--export-filename=$output/vector-probe.png" --export-width=512
Assert-Exit 'SVG to PNG export'
& $blender --background --factory-startup --python-exit-code 1 --python "$PSScriptRoot/verify-blender-assets.py" -- $output
Assert-Exit 'Blender save/render/glTF export'

# A disposable import project proves exported assets can enter Godot without
# adding test models or selecting an art style for the game itself.
$probeProject = Join-Path $output 'godot-import'
New-Item -ItemType Directory -Force $probeProject | Out-Null
@'
config_version=5
[application]
config/name="Asset toolchain probe"
[rendering]
renderer/rendering_method="gl_compatibility"
'@ | Set-Content -Encoding utf8 "$probeProject/project.godot"
Copy-Item -LiteralPath $svg -Destination "$probeProject/vector-probe.svg" -Force
Copy-Item -LiteralPath "$output/model-probe.glb" -Destination "$probeProject/model-probe.glb" -Force
& (Get-Godot) --headless --path $probeProject --editor --import --quit 2>&1 |
    Tee-Object -FilePath "$output/godot-import.log"
Assert-Exit 'Godot asset import'
if (Select-String -Path "$output/godot-import.log" -Pattern 'ERROR:|SCRIPT ERROR:') {
    throw 'Godot asset import reported errors.'
}
foreach ($filename in @('vector-probe.png', 'model-probe.blend', 'model-probe.glb', 'render-probe.png', 'blender-version.json')) {
    $file = Get-Item -LiteralPath (Join-Path $output $filename)
    if ($file.Length -eq 0) { throw "Empty asset: $filename" }
}
foreach ($filename in @('vector-probe.svg.import', 'model-probe.glb.import')) {
    if (!(Test-Path -LiteralPath (Join-Path $probeProject $filename))) { throw "Missing Godot import: $filename" }
}
Write-Output "Asset toolchain verification passed. Evidence: $output"

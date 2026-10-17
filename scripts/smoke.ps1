. "$PSScriptRoot/common.ps1"
& "$PSScriptRoot/validate-content.ps1" -Stage
$godot = Get-Godot
& $godot --headless --path $GodotProject --editor --import --quit
Assert-Exit 'Godot import'
& $godot --headless --path $GodotProject --quit-after 60
Assert-Exit 'Startup smoke'

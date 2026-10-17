. "$PSScriptRoot/common.ps1"
$godot = Get-Godot
& $godot --headless --path $GodotProject --editor --import --quit
Assert-Exit 'Godot import'
& $godot --headless --path $GodotProject --quit-after 60
Assert-Exit 'Startup smoke'

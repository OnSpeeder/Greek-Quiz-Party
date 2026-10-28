# Open the isolated character-performance benchmark for human review.
. "$PSScriptRoot/common.ps1"
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
Start-Process $binary -WindowStyle Hidden -ArgumentList "--path `"$GodotProject`" --resolution 1440x900 -- --match-show-preview --match-ui-greek"

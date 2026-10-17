param([int]$Port = 7777, [switch]$Packaged)
. "$PSScriptRoot/common.ps1"
if ($Packaged) {
    & "$RepoRoot/artifacts/exports/Windows/QuizParty.console.exe" --headless -- --spike-host "--spike-port=$Port"
} else {
    & (Get-Godot) --headless --path $GodotProject res://Scenes/LanSpike.tscn -- --spike-host "--spike-port=$Port"
}
Assert-Exit 'LAN spike host'

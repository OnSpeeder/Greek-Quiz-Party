param([string]$Address = '127.0.0.1', [int]$Port = 7777, [switch]$Automatic)
. "$PSScriptRoot/common.ps1"
$extra = @()
if ($Automatic) { $extra += '--spike-auto' }
& (Get-Godot) --path $GodotProject res://Scenes/LanSpike.tscn -- "--spike-join=$Address" "--spike-port=$Port" @extra
Assert-Exit 'LAN spike client'

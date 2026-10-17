param([Parameter(ValueFromRemainingArguments = $true)][string[]]$ToolArguments)
. "$PSScriptRoot/asset-tools.ps1"
$binary = Get-Blender
& $binary @ToolArguments
Assert-Exit 'Blender'

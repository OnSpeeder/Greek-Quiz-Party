param([Parameter(ValueFromRemainingArguments = $true)][string[]]$ToolArguments)
. "$PSScriptRoot/asset-tools.ps1"
& (Get-Inkscape) @ToolArguments
Assert-Exit 'Inkscape'

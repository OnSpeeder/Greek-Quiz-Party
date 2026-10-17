$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path $PSScriptRoot -Parent
$GodotProject = Join-Path $RepoRoot 'src/QuizParty.Godot'

function Resolve-Tool([string]$Name, [string[]]$Candidates) {
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if ($command) { return $command.Source }
    foreach ($candidate in $Candidates) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) { return $candidate }
    }
    throw "Cannot find $Name. See docs/TOOLCHAIN_STATUS.md."
}

function Get-Godot {
    Resolve-Tool 'godot' @($env:GODOT_PATH, 'C:/Godot/godot_console.exe', 'C:/Godot/godot.exe')
}

function Assert-Exit([string]$Action) {
    if ($LASTEXITCODE -ne 0) { throw "$Action failed (exit $LASTEXITCODE)." }
}

param([int]$Width = 1440, [int]$Height = 900, [switch]$ReducedMotion, [switch]$LargeText)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/living-show/${Width}x$Height$(if ($ReducedMotion) { '-reduced' })$(if ($LargeText) { '-large' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$flags = '--match-show-preview --match-ui-preview --match-ui-greek'
if ($ReducedMotion) { $flags += ' --match-show-reduced' }
if ($LargeText) { $flags += ' --match-ui-large-text' }
$arguments = "--path `"$GodotProject`" --resolution ${Width}x$Height -- $flags --match-show-capture=`"$output`""
$process = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList $arguments -RedirectStandardOutput "$output/runtime.log" -RedirectStandardError "$output/errors.log"
try {
    if (!$process.WaitForExit(45000)) { throw 'Living-show capture timed out.' }
    if ($process.ExitCode -ne 0) { throw "Runtime failed. See $output/errors.log" }
    if ((Get-Item "$output/errors.log").Length -gt 0) { Get-Content "$output/errors.log"; throw 'Runtime diagnostics need review.' }
    if (!(Test-Path "$output/settled.png")) { throw 'Missing final viewport capture.' }
    Get-Content "$output/runtime.log"
} finally {
    if (!$process.HasExited) { $process.Kill() }
    $process.Dispose()
}

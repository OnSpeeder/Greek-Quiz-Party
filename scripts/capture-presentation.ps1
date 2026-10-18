param([ValidateSet('Menu','Lobby','Create','Join','Settings')][string]$View = 'Menu',
    [ValidateRange(320,7680)][int]$Width = 1152, [ValidateRange(320,7680)][int]$Height = 648, [switch]$LargeText,
    [switch]$HighContrast, [switch]$ReducedMotion, [switch]$SoundPreview, [switch]$Mute)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/phase10-$($View.ToLower())-${Width}x$Height$(if ($LargeText) { '-large' })$(if ($HighContrast) { '-contrast' })$(if ($Mute) { '-muted' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$scene = if ($View -in @('Lobby','Create','Join')) { 'res://Scenes/Lobby.tscn' } else { 'res://Scenes/Main.tscn' }
$flags = @('--ui-preview')
if ($ReducedMotion) { $flags += '--ui-reduced-motion' }
if ($View -eq 'Settings') { $flags += '--ui-settings' }
if ($View -eq 'Create') { $flags += '--ui-create' }
if ($View -eq 'Join') { $flags += '--ui-join' }
if ($LargeText) { $flags += '--ui-large-text' }
if ($HighContrast) { $flags += '--ui-high-contrast' }
if ($SoundPreview) { $flags += '--ui-sound-preview' }
if ($Mute) { $flags += '--ui-mute' }
# Capture the actual viewport. Godot movie mode fixes its own canvas size and
# cannot supply trustworthy portrait layout screenshots. Preferences never save.
$arguments = "--path `"$GodotProject`" $scene --resolution ${Width}x$Height --language el_GR -- $($flags -join ' ') --ui-capture=`"$output/preview.png`""
$process = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList $arguments `
    -RedirectStandardOutput "$output/runtime.log" -RedirectStandardError "$output/errors.log"
if (!$process.WaitForExit(30000)) { $process.Kill(); throw 'Presentation capture timed out.' }
if ($process.ExitCode -ne 0) { throw "Presentation capture exited $($process.ExitCode)." }
if ((Get-Item "$output/errors.log").Length -gt 0) { throw "Inspect $output/errors.log." }
$image = Get-Item -LiteralPath "$output/preview.png" -ErrorAction SilentlyContinue
if (!$image) { throw 'Renderer produced no PNG capture.' }
Write-Output "PASS: $($image.FullName)"

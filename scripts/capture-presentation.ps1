param([ValidateSet('Menu','Lobby','Create','Join','Settings','Exit')][string]$View = 'Menu',
    [ValidateRange(320,7680)][int]$Width = 1152, [ValidateRange(320,7680)][int]$Height = 648, [switch]$LargeText,
    [switch]$HighContrast, [switch]$ReducedMotion, [switch]$SoundPreview, [switch]$Mute,
    [ValidateSet('Audio','Gameplay','Help')][string]$SettingsSection = 'Audio',
    [ValidateSet('el_GR','en')][string]$Locale = 'el_GR',
    [ValidateSet('showtime','studio','neon','retro')][string]$Theme = 'showtime')
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/phase10-$($View.ToLower())-${Width}x$Height$(if ($LargeText) { '-large' })$(if ($HighContrast) { '-contrast' })$(if ($Mute) { '-muted' })"
if ($View -eq 'Settings') { $output += "-$($SettingsSection.ToLower())-$Locale" }
if ($Theme -ne 'showtime') { $output += "-$Theme" }
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$scene = if ($View -in @('Lobby','Create','Join')) { 'res://Scenes/Lobby.tscn' } else { 'res://Scenes/Main.tscn' }
$flags = @('--ui-preview')
if ($Theme -ne 'showtime') { $flags += "--ui-theme=$Theme" }
if ($ReducedMotion) { $flags += '--ui-reduced-motion' }
if ($View -eq 'Settings') { $flags += '--ui-settings' }
if ($View -eq 'Exit') { $flags += '--ui-exit-confirmation' }
if ($View -eq 'Settings' -and $SettingsSection -eq 'Gameplay') { $flags += '--ui-gameplay' }
if ($View -eq 'Settings' -and $SettingsSection -eq 'Help') { $flags += '--ui-help' }
if ($Locale -eq 'en') { $flags += '--ui-english' }
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
$null = $process.Handle
if (!$process.WaitForExit(30000)) { $process.Kill(); throw 'Presentation capture timed out.' }
if ($process.ExitCode -ne 0) { throw "Presentation capture exited $($process.ExitCode)." }
if ((Get-Item "$output/errors.log").Length -gt 0) { throw "Inspect $output/errors.log." }
$image = Get-Item -LiteralPath "$output/preview.png" -ErrorAction SilentlyContinue
if (!$image) { throw 'Renderer produced no PNG capture.' }
Write-Output "PASS: $($image.FullName)"

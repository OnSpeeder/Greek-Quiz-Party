param([ValidateSet('QuestionActive','AnswerReveal','Scoreboard','GameOver')][string]$Phase = 'QuestionActive',
    [int]$Width = 420, [int]$Height = 900, [switch]$Strategy, [switch]$Packaged,
    [switch]$Motion, [switch]$LargeText, [switch]$HighContrast)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/phase10-redesign-match-${Width}x$Height-$Phase$(if ($Packaged) { '-packaged' })"
if ($Motion) { $output += '-motion' }
if ($LargeText) { $output += '-large' }
if ($HighContrast) { $output += '-contrast' }
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$launch = "--path `"$GodotProject`""
if ($Packaged) { $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'; $launch = '' }
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
try {
    $strategyFlag = if ($Strategy) { '--match-strategy' } else { '' }
    $appearance = '--ui-preview --ui-greek'
    if (!$Motion) { $appearance += ' --ui-reduced-motion' }
    if ($LargeText) { $appearance += ' --ui-large-text' }
    if ($HighContrast) { $appearance += ' --ui-high-contrast' }
    $hostArgs = "$launch --resolution ${Width}x$Height --language el_GR -- $appearance --match-host --match-auto --match-fixture=1 --match-name=Ελένη --match-players=2 --match-port=17897 --match-delay=1 $strategyFlag --match-capture=`"$output/preview.png`" --match-capture-phase=$Phase --match-capture-delay=$(if ($Phase -eq 'AnswerReveal') { '1.5' } elseif ($Phase -eq 'Scoreboard' -or $Phase -eq 'GameOver') { '0.8' } else { '0.2' })"
    $hostProcess = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList $hostArgs -RedirectStandardOutput "$output/host.log" -RedirectStandardError "$output/host-errors.log"
    $processes.Add($hostProcess)
    $deadline = [DateTime]::UtcNow.AddSeconds(20)
    while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Preview host failed to start.' }
        Start-Sleep -Milliseconds 100
    }
    $clientProcess = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "$launch --headless -- --match-join=127.0.0.1 --match-auto --match-name=Νίκος --match-players=2 --match-port=17897 --match-delay=2" `
        -RedirectStandardOutput "$output/client.log" -RedirectStandardError "$output/client-errors.log"
    $processes.Add($clientProcess)
    foreach ($peer in $processes) {
        if (!$peer.WaitForExit(45000) -or $peer.ExitCode -ne 0) { throw 'Match preview did not complete.' }
    }
    foreach ($role in @('host','client')) {
        if ((Get-Item "$output/$role-errors.log").Length -gt 0) { throw "Inspect $output/$role-errors.log." }
        if (!(Select-String "$output/$role.log" -Pattern 'MATCH AUTO_PASS' -Quiet)) { throw 'Preview did not finish its match.' }
    }
    if (!(Test-Path "$output/preview.png")) { throw 'Match preview image is missing.' }
    Write-Output "PASS: actual host/client match and $Phase capture -> $output/preview.png"
} finally {
    foreach ($peer in $processes) { if (!$peer.HasExited) { $peer.Kill() }; $peer.Dispose() }
}

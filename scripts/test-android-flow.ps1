param([Parameter(Mandatory=$true)][string]$HostAddress, [int]$Port = 19873,
    [switch]$IdleScoreboard, [switch]$HostPlays, [switch]$LongQuestions, [switch]$StaggerScores)
. "$PSScriptRoot/common.ps1"
if ($HostAddress -notmatch '^\d{1,3}(\.\d{1,3}){3}$') { throw 'Supply the Windows LAN IPv4 address.' }
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$output = Join-Path $RepoRoot 'artifacts/match-flow-android'
New-Item -ItemType Directory -Force $output | Out-Null
$binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'
$peers = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
$fixture = 'files/phase04-test-args.json'
try {
    & $adb shell am force-stop org.quizparty.game
    $phoneArgs = @('--match-flow-client', '--match-flow-name=Phone', "--match-flow-address=$HostAddress", "--match-flow-port=$Port", '--match-flow-capture=user://', '--match-ui-greek', '--match-ui-portrait')
    if (!$HostPlays) { $phoneArgs += '--match-flow-local' }
    if ($HostPlays) { $phoneArgs += '--match-flow-host-plays' }
    if ($IdleScoreboard) { $phoneArgs += '--match-flow-idle-scoreboard' }
    if ($LongQuestions) { $phoneArgs += '--match-flow-long' }
    if ($StaggerScores) { $phoneArgs += '--match-flow-stagger' }
    (ConvertTo-Json -InputObject $phoneArgs -Compress) | & $adb shell run-as org.quizparty.game tee $fixture | Out-Null
    Assert-Exit 'Write Android flow fixture'
    foreach ($role in @('host', 'remote')) {
        $flags = if ($role -eq 'host') { '--match-flow-host' } else { '--match-flow-client --match-flow-name=Windows' }
        if ($HostPlays) { $flags += ' --match-flow-host-plays' }
        if ($IdleScoreboard) { $flags += ' --match-flow-idle-scoreboard' }
        if ($LongQuestions) { $flags += ' --match-flow-long' }
        if ($StaggerScores) { $flags += ' --match-flow-stagger' }
        $peer = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "--resolution 1280x720 --language el_GR -- --ui-preview --ui-greek $flags --match-flow-port=$Port" `
            -RedirectStandardOutput "$output/$role.log" -RedirectStandardError "$output/$role-errors.log"
        $null = $peer.Handle
        $peers.Add($peer)
        if ($role -eq 'host') {
            $deadline = [DateTime]::UtcNow.AddSeconds(25)
            while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
                if ($peer.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Android-flow host failed to listen.' }
                Start-Sleep -Milliseconds 100
            }
        }
    }
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game
    Assert-Exit 'Launch Android flow'
    $phonePid = (& $adb shell pidof -s org.quizparty.game).Trim()
    if (!$phonePid) { throw 'Android flow did not start.' }
    $deadline = [DateTime]::UtcNow.AddSeconds(75)
    do {
        & $adb logcat "--pid=$phonePid" -d -v time | Set-Content -Encoding utf8 "$output/phone.log"
        $phoneLog = Get-Content "$output/phone.log" -Raw
        if ([DateTime]::UtcNow -gt $deadline) { throw 'Android flow timed out.' }
        if ($phoneLog -notmatch 'FLOW REPLAY_PASS') { Start-Sleep -Milliseconds 250 }
    } while ($phoneLog -notmatch 'FLOW REPLAY_PASS')
    foreach ($peer in $peers) { if (!$peer.WaitForExit(10000) -or $peer.ExitCode -ne 0) { throw 'Windows flow peer failed.' } }
    $finals = @([regex]::Match($phoneLog, 'FLOW FINAL ([^\r\n]+)').Groups[1].Value)
    foreach ($role in @('host', 'remote')) {
        $log = Get-Content "$output/$role.log" -Raw
        if ($log -notmatch 'FLOW REPLAY_PASS') { throw "$role did not replay." }
        $finals += [regex]::Match($log, 'FLOW FINAL ([^\r\n]+)').Groups[1].Value
        if ((Get-Item "$output/$role-errors.log").Length -gt 0) { throw "$role runtime error." }
    }
    if (!$finals[0] -or ($finals | Select-Object -Unique).Count -ne 1) { throw 'Physical Android totals disagree.' }
    if ($phoneLog -match 'ERROR:|Unhandled exception|FATAL EXCEPTION') { throw 'Physical runtime errors observed.' }
    if ($IdleScoreboard -and $phoneLog -match 'FLOW STATUS ms=\d+ Reconnecting') { throw 'Phone unexpectedly reconnected during the idle scenario.' }
    foreach ($name in @('controller', 'facts', 'scoreboard', 'final')) {
        $encoded = & $adb shell run-as org.quizparty.game base64 "files/$name.png"
        Assert-Exit "Read Android $name capture"
        [IO.File]::WriteAllBytes("$output/$name.png", [Convert]::FromBase64String(($encoded -join '')))
    }
    $hostRole = if ($HostPlays) { 'playing host' } else { 'observer host' }
    Write-Output "PASS: physical Android client + Windows client + $hostRole; unanimous progress/end, identical totals and replay. $output"
} finally {
    & $adb shell run-as org.quizparty.game rm -f $fixture
    foreach ($peer in $peers) { if (!$peer.HasExited) { $peer.Kill() }; $peer.Dispose() }
    & $adb shell am force-stop org.quizparty.game
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
}

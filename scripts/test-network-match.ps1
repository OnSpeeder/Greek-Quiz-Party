param([int]$Port = 17781, [switch]$Packaged, [switch]$TimeoutCase)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot $(if ($Packaged) { 'artifacts/phase04-network-packaged' } else { 'artifacts/phase04-network' })
if ($TimeoutCase) { $output += '-timeout' }
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$baseArgs = "--headless --path `"$GodotProject`" --"
if ($Packaged) { $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'; $baseArgs = '--headless --' }
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
function Start-Match([string]$Name, [string]$Flags) {
    $process = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$baseArgs --match-port=$Port --match-auto $Flags" `
        -RedirectStandardOutput "$output/$Name.log" -RedirectStandardError "$output/$Name-errors.log"
    $processes.Add($process)
    return $process
}
try {
    $hostProcess = Start-Match 'host' '--match-host --match-name=Host --match-players=3'
    $deadline = [DateTime]::UtcNow.AddSeconds(15)
    while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Match host did not start.' }
        Start-Sleep -Milliseconds 100
    }
    $first = Start-Match 'first' '--match-join=127.0.0.1 --match-name=Anna'
    $lastFlag = if ($TimeoutCase) { '--match-unanswered' } else { '--match-wrong' }
    $second = Start-Match 'second' "--match-join=127.0.0.1 --match-name=Maria $lastFlag"
    foreach ($process in $processes) {
        if (!$process.WaitForExit(35000)) { throw 'Match process timed out.' }
        if ($process.ExitCode -ne 0) { throw "Match process exited $($process.ExitCode); inspect $output." }
    }
    $finals = @()
    foreach ($name in @('host','first','second')) {
        $lines = Get-Content "$output/$name.log"
        foreach ($phase in @('QuestionActive','QuestionLocked','AnswerReveal','Scoreboard','GameOver')) {
            if (!($lines | Select-String "phase=$phase" -Quiet)) { throw "$name missed $phase." }
        }
        $finals += ($lines | Where-Object { $_ -like '*phase=GameOver*' } | Select-Object -Last 1)
        if (!($lines | Select-String 'AUTO_PASS' -Quiet)) { throw "$name did not finish." }
    }
    if (($finals | Select-Object -Unique).Count -ne 1) { throw 'Final question/revision/scores disagree across peers.' }
    if ($finals[0] -notmatch 'scores=Anna:[1-9]\d*\|Host:[1-9]\d*\|Maria:0') { throw 'Correct/wrong or unanswered scoring is unexpected.' }
    $mariaResult = if ($TimeoutCase) { 'RESULT player=Maria answer=none points=0' } else { 'RESULT player=Maria answer=[0-3] points=0' }
    if (!(Select-String "$output/second.log" -Pattern $mariaResult -Quiet)) { throw 'Wrong/unanswered result was not observed.' }
    if (Select-String "$output/*errors.log" -Pattern 'ERROR:|SCRIPT ERROR:|Unhandled exception') { throw 'Engine/runtime errors observed.' }
    Write-Output "PASS: host and two clients completed active/locked/reveal/scoreboard/final with identical authoritative totals; duplicate answers safe. $($finals[0])"
} finally {
    foreach ($process in $processes) { if (!$process.HasExited) { Stop-Process -Id $process.Id }; $process.Dispose() }
}

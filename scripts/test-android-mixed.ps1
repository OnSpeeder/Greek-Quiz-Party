param([Parameter(Mandatory=$true)][string]$HostAddress, [switch]$AndroidHost,
    [ValidateRange(0,7)][int]$HostPlayers = 2, [ValidateRange(1,7)][int]$ClientPlayers = 3,
    [ValidateSet(10,20,30)][int]$QuestionCount = 20, [int]$Port = 17793)
. "$PSScriptRoot/common.ps1"
$total = $HostPlayers + $ClientPlayers
if ($total -lt 2 -or $total -gt 8 -or $HostAddress -notmatch '^\d{1,3}(\.\d{1,3}){3}$') { throw 'Supply host IPv4 and2–8 total players.' }
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$output = Join-Path $RepoRoot "artifacts/phase09-android-$HostPlayers-$ClientPlayers$(if ($AndroidHost) { '-phone-host' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'
$process = $null
$deviceFixture = 'files/phase04-test-args.json'
function Start-WindowsPeer {
    $role = if ($AndroidHost) { "--match-join=$HostAddress --match-local=$ClientPlayers" } else { "--match-host --match-local=$HostPlayers --match-fixture=$QuestionCount" }
    Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "--resolution 1152x900 --language el_GR -- --match-mixed --match-auto --match-teams --match-strategy --match-name=Windows --match-port=$Port --match-players=$total --match-keep-open --match-capture=$output/windows-final.png $role" `
        -RedirectStandardOutput "$output/windows.log" -RedirectStandardError "$output/windows-errors.log"
}
try {
    & $adb shell am force-stop org.quizparty.game
    $phoneSlots = if ($AndroidHost) { $HostPlayers } else { $ClientPlayers }
    $deviceArgs = @('--match-mixed','--match-auto','--match-teams','--match-strategy','--match-name=Phone',
        "--match-port=$Port", "--match-players=$total", "--match-local=$phoneSlots", '--match-keep-open')
    if ($AndroidHost) { $deviceArgs += @('--match-host', "--match-fixture=$QuestionCount") }
    else { $deviceArgs += "--match-join=$HostAddress" }
    (ConvertTo-Json -InputObject $deviceArgs -Compress) | & $adb shell run-as org.quizparty.game tee $deviceFixture | Out-Null
    Assert-Exit 'Write physical mixed debug arguments'
    $deadline = [DateTime]::UtcNow.AddSeconds(45 + 6 * $QuestionCount)
    if (!$AndroidHost) {
        $process = Start-WindowsPeer
        while (!(Select-String "$output/windows.log" -Pattern HostListening -Quiet)) {
            if ($process.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Windows mixed host failed to listen.' }; Start-Sleep -Milliseconds 100
        }
    }
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game
    Assert-Exit 'Launch physical mixed app'
    $phonePid = (& $adb shell pidof -s org.quizparty.game).Trim()
    if (!$phonePid) { throw 'Phone mixed app exited.' }
    if ($AndroidHost) {
        while (-not ((& $adb logcat "--pid=$phonePid" -d -v time) -match 'LOBBY STATUS HostListening')) {
            if ([DateTime]::UtcNow -gt $deadline) { throw 'Phone mixed host failed to listen.' }; Start-Sleep -Milliseconds 100
        }
        $process = Start-WindowsPeer
    }
    $activeCaptured = $false
    do {
        & $adb logcat "--pid=$phonePid" -d -v time | Set-Content -Encoding utf8 "$output/phone.log"
        $phoneLog = Get-Content "$output/phone.log" -Raw
        if (!$activeCaptured -and $phoneLog -match 'phase=QuestionActive') {
            & $adb shell screencap -p /sdcard/quizparty-phase09-active.png
            & $adb pull /sdcard/quizparty-phase09-active.png "$output/phone-active.png" | Out-Null
            $activeCaptured = $true
        }
        if ($process.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw "Physical mixed match timed out; inspect $output." }
        if ($phoneLog -notmatch 'MIXED PASS') { Start-Sleep -Milliseconds 250 }
    } while ($phoneLog -notmatch 'MIXED PASS')
    $windowsLog = Get-Content "$output/windows.log" -Raw
    $windowsHash = [regex]::Match($windowsLog, 'MIXED DIGEST [A-F0-9]{64}').Value
    $phoneHash = [regex]::Match($phoneLog, 'MIXED DIGEST [A-F0-9]{64}').Value
    if (!$windowsHash -or $windowsHash -ne $phoneHash) { throw 'Physical mixed authoritative finals disagree.' }
    if ($phoneLog -notmatch "MIXED OWN count=$phoneSlots " -or $phoneLog -notmatch "MIXED PASS players=$total questions=$QuestionCount teams=2") { throw 'Not every phone slot finished.' }
    $final = ([regex]::Match($windowsLog, 'MIXED FINAL ([^\r\n]*)').Groups[1].Value) | ConvertFrom-Json
    if ($final.Scores.Count -ne $total -or $final.Teams.Count -ne 2 -or ($final.FinalStrategy | Measure-Object CardsUsed -Sum).Sum -lt 1) { throw 'Missing logical players/teams/cards.' }
    foreach ($team in $final.Teams) {
        if ($team.Total -ne ($final.Scores | Where-Object { $team.Members -contains $_.PlayerId } | Measure-Object Total -Sum).Sum) { throw 'Physical team aggregate mismatch.' }
    }
    Start-Sleep -Milliseconds 400
    & $adb shell screencap -p /sdcard/quizparty-phase09-final.png
    & $adb pull /sdcard/quizparty-phase09-final.png "$output/phone-final.png" | Out-Null
    if (!(Test-Path "$output/windows-final.png")) { throw 'Windows final render missing.' }
    if ((Get-Content "$output/windows-errors.log" -Raw) -match 'ERROR:|Unhandled exception' -or $phoneLog -match 'ERROR:|SCRIPT ERROR:|Unhandled exception|FATAL EXCEPTION') { throw 'Physical mixed runtime errors observed.' }
    Write-Output "PASS: physical Android $(if ($AndroidHost) { 'host' } else { 'client' }), $total players ($HostPlayers+$ClientPlayers), $QuestionCount questions; all scores/teams/missions/stats match. $windowsHash"
} finally {
    & $adb shell run-as org.quizparty.game rm -f $deviceFixture
    & $adb shell rm -f /sdcard/quizparty-phase09-active.png /sdcard/quizparty-phase09-final.png
    if ($process) { if (!$process.HasExited) { Stop-Process -Id $process.Id }; $process.Dispose() }
    & $adb shell am force-stop org.quizparty.game
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
}

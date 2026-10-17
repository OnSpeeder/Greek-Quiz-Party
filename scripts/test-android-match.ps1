param([Parameter(Mandatory = $true)][string]$HostAddress, [int]$Port = 17783, [switch]$Wrong, [switch]$Unanswered)
. "$PSScriptRoot/common.ps1"
if ($HostAddress -notmatch '^\d{1,3}(\.\d{1,3}){3}$') { throw 'Supply the actual Windows LAN IPv4 address.' }
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$output = Join-Path $RepoRoot $(if ($Unanswered) { 'artifacts/phase04-android-timeout' } elseif ($Wrong) { 'artifacts/phase04-android-wrong' } else { 'artifacts/phase04-android' })
New-Item -ItemType Directory -Force $output | Out-Null
$binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'
$hostProcess = $null
$deviceFixture = 'files/phase04-test-args.json'
try {
    & $adb shell am force-stop org.quizparty.game
    $deviceArgs = @("--match-join=$HostAddress", "--match-port=$Port", '--match-name=Phone', '--match-auto', '--match-delay=6', '--match-keep-open')
    if ($Wrong) { $deviceArgs += '--match-wrong' }
    if ($Unanswered) { $deviceArgs += '--match-unanswered' }
    $json = ConvertTo-Json -InputObject $deviceArgs -Compress
    $json | & $adb shell run-as org.quizparty.game tee $deviceFixture | Out-Null
    Assert-Exit 'Write app-private debug test fixture'
    $hostProcess = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "--resolution 1152x720 --language el_GR -- --match-host --match-port=$Port --match-name=Host --match-auto --match-players=2 --match-delay=5 --match-keep-open --match-capture=$output/host-final.png" `
        -RedirectStandardOutput "$output/host.log" -RedirectStandardError "$output/host-errors.log"
    $deadline = [DateTime]::UtcNow.AddSeconds(45)
    while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Packaged LAN host did not start.' }
        Start-Sleep -Milliseconds 100
    }
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game
    Assert-Exit 'Launch physical Android app'
    $deviceAppPid = (& $adb shell pidof -s org.quizparty.game).Trim()
    if (!$deviceAppPid) { throw 'Android app did not stay running.' }
    $activeCaptured = $false
    do {
        & $adb logcat "--pid=$deviceAppPid" -d -v time | Set-Content -Encoding utf8 "$output/phone.log"
        $phoneLog = Get-Content "$output/phone.log" -Raw
        if (!$activeCaptured -and $phoneLog -match 'phase=QuestionActive') {
            & $adb shell screencap -p /sdcard/quizparty-phase04-active.png
            & $adb pull /sdcard/quizparty-phase04-active.png "$output/phone-active.png" | Out-Null
            $activeCaptured = $true
        }
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw "Physical match did not finish; inspect $output." }
        if ($phoneLog -notmatch 'MATCH AUTO_PASS') { Start-Sleep -Milliseconds 250 }
    } while ($phoneLog -notmatch 'MATCH AUTO_PASS')
    foreach ($phase in @('QuestionActive','QuestionLocked','AnswerReveal','Scoreboard','GameOver')) {
        if ($phoneLog -notmatch "phase=$phase") { throw "Physical phone missed $phase." }
    }
    $hostFinal = [regex]::Match((Get-Content "$output/host.log" -Raw), 'MATCH SNAPSHOT[^\r\n]*phase=GameOver[^\r\n]*').Value
    $phoneFinal = [regex]::Match($phoneLog, 'MATCH SNAPSHOT[^\r\n]*phase=GameOver[^\r\n]*').Value
    if (!$hostFinal -or $hostFinal -ne $phoneFinal) { throw 'Physical phone final snapshot disagrees with Windows host.' }
    if ($Unanswered -and $phoneLog -notmatch 'RESULT player=Phone answer=none points=0') { throw 'Physical timeout result was not observed.' }
    if ($Wrong -and $phoneLog -notmatch 'RESULT player=Phone answer=[0-3] points=0') { throw 'Physical wrong-answer result was not observed.' }
    if (!$Wrong -and !$Unanswered -and $hostFinal -notmatch 'scores=Host:[1-9]\d*\|Phone:[1-9]\d*') { throw 'Physical correct answer did not score.' }
    # Let Android draw the final container layout before taking its screenshot.
    Start-Sleep -Milliseconds 500
    & $adb shell screencap -p /sdcard/quizparty-phase04-final.png
    & $adb pull /sdcard/quizparty-phase04-final.png "$output/phone-final.png" | Out-Null
    $frameDeadline = [DateTime]::UtcNow.AddSeconds(5)
    while (!(Test-Path "$output/host-final.png")) { if ([DateTime]::UtcNow -gt $frameDeadline) { throw 'Host final capture missing.' }; Start-Sleep -Milliseconds 100 }
    if ((Get-Content "$output/host-errors.log" -Raw) -match 'ERROR:|Unhandled exception' -or $phoneLog -match 'ERROR:|SCRIPT ERROR:|Unhandled exception|FATAL EXCEPTION') { throw 'Runtime errors observed.' }
    Write-Output "PASS: physical Android -> packaged Windows over LAN $HostAddress; no ADB network tunnel. $hostFinal"
} finally {
    & $adb shell run-as org.quizparty.game rm -f $deviceFixture
    & $adb shell rm -f /sdcard/quizparty-phase04-active.png /sdcard/quizparty-phase04-final.png
    if ($hostProcess) { if (!$hostProcess.HasExited) { Stop-Process -Id $hostProcess.Id }; $hostProcess.Dispose() }
    & $adb shell am force-stop org.quizparty.game
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
}

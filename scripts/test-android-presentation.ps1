param([switch]$LeaveSettings, [switch]$StandardAppearance)
. "$PSScriptRoot/common.ps1"
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$output = Join-Path $RepoRoot 'artifacts/phase10-qa/android'
if ($StandardAppearance) { $output += '-standard' }
New-Item -ItemType Directory -Force $output | Out-Null
$policy = (& $adb shell dumpsys window policy | Out-String)
if ($policy -notmatch 'showing=false' -or $policy -notmatch 'interactiveState=INTERACTIVE_STATE_AWAKE') {
    throw 'Keep the phone awake and unlocked; this helper never changes lock/device settings.'
}
$fixture = 'files/phase04-test-args.json'
& $adb shell run-as org.quizparty.game test -e $fixture
if ($LASTEXITCODE -eq 0) { throw 'An existing debug argument fixture is present; preserve it and finish that run first.' }
try {
    foreach ($orientation in @('portrait','landscape')) {
        foreach ($view in @('menu','settings')) {
            & $adb shell am force-stop org.quizparty.game
            $preview = @('--match-ui-preview', '--match-ui-greek', "--match-ui-$orientation")
            if (!$StandardAppearance) { $preview += @('--match-ui-large-text', '--match-ui-reduced-motion') }
            if ($view -eq 'settings') {
                $preview += '--match-ui-settings'
                if (!$StandardAppearance) { $preview += '--match-ui-high-contrast' }
            }
            ConvertTo-Json -InputObject $preview -Compress | & $adb shell run-as org.quizparty.game tee $fixture | Out-Null
            Assert-Exit 'Write debug-only presentation preview arguments'
            & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
            Assert-Exit 'Launch presentation preview'
            $appPid = (& $adb shell pidof -s org.quizparty.game).Trim()
            if (!$appPid) { throw 'Android preview exited.' }
            $deadline = [DateTime]::UtcNow.AddSeconds(35)
            do {
                & $adb logcat "--pid=$appPid" -d -v time | Set-Content -Encoding utf8 "$output/$orientation-$view.log"
                $log = Get-Content "$output/$orientation-$view.log" -Raw
                if ([DateTime]::UtcNow -gt $deadline) { throw 'Preview did not reach C# startup and final display metrics.' }
                if ($log -notmatch 'PRESENTATION TOUCH') { Start-Sleep -Milliseconds 250 }
            } while ($log -notmatch 'PRESENTATION TOUCH')
            if ($log -match 'ERROR:|SCRIPT ERROR:|FATAL EXCEPTION|Unhandled exception') { throw 'Android runtime error; inspect preview logs.' }
            & $adb shell screencap -p /sdcard/quizparty-phase10-qa.png
            & $adb pull /sdcard/quizparty-phase10-qa.png "$output/$orientation-$view.png" | Out-Null
            Assert-Exit 'Capture physical screen'
        }
    }
    Write-Output "PASS: physical portrait/landscape menu/settings renders captured at $output. This is not human touch/listening sign-off."
} finally {
    & $adb shell run-as org.quizparty.game rm -f $fixture
    & $adb shell rm -f /sdcard/quizparty-phase10-qa.png
    if (!$LeaveSettings) {
        & $adb shell am force-stop org.quizparty.game
        & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
    }
}

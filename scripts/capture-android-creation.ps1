param([switch]$LargeText)
. "$PSScriptRoot/common.ps1"
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$output = Join-Path $RepoRoot 'artifacts/optional-host/android'
New-Item -ItemType Directory -Force $output | Out-Null
$fixture = 'files/phase04-test-args.json'
& $adb shell run-as org.quizparty.game test -e $fixture
if ($LASTEXITCODE -eq 0) { throw 'An existing device fixture must be preserved.' }
try {
    foreach ($orientation in @('portrait','landscape')) {
        foreach ($view in @('create','create-identity','lobby')) {
            & $adb shell am force-stop org.quizparty.game
            $preview = @('--match-ui-preview','--match-ui-greek','--match-ui-reduced-motion',"--match-ui-$orientation")
            if ($LargeText) { $preview += '--match-ui-large-text' }
            $preview += $(if ($view -eq 'lobby') { '--match-ui-lobby-page=roster' } else { "--match-ui-$view" })
            ConvertTo-Json -InputObject $preview -Compress | & $adb shell run-as org.quizparty.game tee $fixture | Out-Null
            & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
            $appPid = (& $adb shell pidof -s org.quizparty.game).Trim()
            $deadline = [DateTime]::UtcNow.AddSeconds(30)
            do {
                & $adb logcat "--pid=$appPid" -d -v time | Set-Content -Encoding utf8 "$output/$orientation-$view.log"
                $log = Get-Content "$output/$orientation-$view.log" -Raw
                if ([DateTime]::UtcNow -gt $deadline) { throw "Preview startup timed out: $view" }
                if ($log -notmatch 'PRESENTATION TOUCH') { Start-Sleep -Milliseconds 150 }
            } while ($log -notmatch 'PRESENTATION TOUCH')
            if ($log -match 'ERROR:|SCRIPT ERROR:|Unhandled exception|FATAL EXCEPTION') { throw "Runtime errors: $view" }
            & $adb shell screencap -p /sdcard/quizparty-optional-host.png
            & $adb pull /sdcard/quizparty-optional-host.png "$output/$orientation-$view.png" | Out-Null
        }
    }
    Write-Output "PASS: physical portrait/landscape create, identity and lobby captures: $output"
} finally {
    & $adb shell run-as org.quizparty.game rm -f $fixture
    & $adb shell rm -f /sdcard/quizparty-optional-host.png
    & $adb shell am force-stop org.quizparty.game
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
}

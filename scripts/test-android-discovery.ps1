param([Parameter(Mandatory = $true)][string]$HostAddress, [int]$Port = 17789, [int]$DiscoveryPort = 17790)
. "$PSScriptRoot/common.ps1"
if ($HostAddress -notmatch '^\d{1,3}(\.\d{1,3}){3}$') { throw 'Supply the actual Windows LAN IPv4 address.' }
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
if (!((& $adb shell dumpsys power) -match 'mWakefulness=Awake')) { throw 'Wake and unlock the phone before the physical LAN test.' }
$output = Join-Path $RepoRoot 'artifacts/phase07-android'
New-Item -ItemType Directory -Force $output | Out-Null
$binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
$deviceFixture = 'files/phase04-test-args.json'
$script:phonePid = ''
function Start-Windows([string]$Name, [string]$Flags) {
    $process = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "--headless -- --lan-port=$Port --lan-discovery-port=$DiscoveryPort $Flags" `
        -RedirectStandardOutput "$output/$Name.log" -RedirectStandardError "$output/$Name-errors.log"
    $processes.Add($process); return $process
}
function Launch-Phone([string[]]$Flags) {
    & $adb shell am force-stop org.quizparty.game
    $argsForPhone = @("--lan-port=$Port", "--lan-discovery-port=$DiscoveryPort", '--lan-stay') + $Flags
    $json = ConvertTo-Json -InputObject $argsForPhone -Compress
    $json | & $adb shell run-as org.quizparty.game tee $deviceFixture | Out-Null
    Assert-Exit 'Write debug phone arguments'
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
    Assert-Exit 'Launch phone'
    $script:phonePid = (& $adb shell pidof -s org.quizparty.game).Trim()
    if (!$script:phonePid) { throw 'Phone process did not remain alive.' }
}
function Wait-Phone([string]$Name, [string]$Pattern) {
    $deadline = [DateTime]::UtcNow.AddSeconds(20)
    do {
        & $adb logcat "--pid=$script:phonePid" -d -v time | Set-Content -Encoding utf8 "$output/$Name.log"
        if (Select-String "$output/$Name.log" -Pattern $Pattern -Quiet) { return }
        if ([DateTime]::UtcNow -gt $deadline) { throw "$Name did not log $Pattern; inspect $output." }
        Start-Sleep -Milliseconds 200
    } while ($true)
}
function Capture-Phone([string]$Name) {
    & $adb shell screencap -p /sdcard/quizparty-phase07.png
    & $adb pull /sdcard/quizparty-phase07.png "$output/$Name.png" | Out-Null
}
function Wait-Windows([System.Diagnostics.Process]$Process, [string]$Name, [string]$Pattern) {
    $deadline = [DateTime]::UtcNow.AddSeconds(15)
    while (!(Select-String "$output/$Name.log" -Pattern $Pattern -Quiet)) {
        if ($Process.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw "$Name missed $Pattern." }
        Start-Sleep -Milliseconds 100
    }
}
try {
    $server = Start-Windows 'windows-host' '--lan-host --lan-stay --lan-pin=1234'
    Wait-Windows $server 'windows-host' 'HostListening'
    Launch-Phone @('--lan-find', '--lan-scan-only', '--lan-name=Phone')
    Wait-Phone 'phone-browser' 'LAN SCAN_PASS rooms=1'
    if (!(Select-String "$output/phone-browser.log" -Pattern "LAN FOUND .*address=$HostAddress port=$Port .*requiresPin=True" -Quiet)) { throw 'Phone did not discover actual Windows LAN endpoint.' }
    Capture-Phone 'phone-browser'
    Launch-Phone @('--lan-find', '--lan-pin=9999', '--lan-name=Phone')
    Wait-Phone 'phone-wrong-pin' 'STATUS WrongPin'; Capture-Phone 'phone-wrong-pin'
    Launch-Phone @('--lan-find', '--lan-pin=1234', '--lan-name=Phone')
    Wait-Phone 'phone-discovered-join' 'LAN JOINED'; Capture-Phone 'phone-lobby'
    Launch-Phone @("--lan-join=$HostAddress", '--lan-pin=1234', '--lan-name=Phone')
    Wait-Phone 'phone-manual-join' 'LAN JOINED'
    $firstId = [regex]::Match((Get-Content "$output/phone-discovered-join.log" -Raw), 'LAN JOINED player=([^\r\n]+)').Groups[1].Value
    $secondId = [regex]::Match((Get-Content "$output/phone-manual-join.log" -Raw), 'LAN JOINED player=([^\r\n]+)').Groups[1].Value
    if (!$firstId -or !$secondId -or $firstId -eq $secondId) { throw 'Physical lobby rejoin did not assign a fresh identity.' }
    Stop-Process -Id $server.Id; $server.WaitForExit(5000) | Out-Null
    Wait-Phone 'phone-host-exit' 'LAN SERVER_LEFT match-cannot-resume'

    Launch-Phone @('--lan-host', '--lan-pin=1234', '--lan-name=PhoneHost')
    Wait-Phone 'phone-host' 'DISCOVERY ADVERTISING'
    $scan = Start-Windows 'windows-browser' '--lan-find --lan-scan-only'
    if (!$scan.WaitForExit(15000) -or $scan.ExitCode -ne 0) { throw 'Windows could not discover Android host.' }
    $wrong = Start-Windows 'windows-wrong-pin' '--lan-find --lan-pin=9999'
    if (!$wrong.WaitForExit(15000) -or $wrong.ExitCode -ne 2 -or !(Select-String "$output/windows-wrong-pin.log" -Pattern 'WrongPin' -Quiet)) { throw 'Android host did not reject wrong PIN.' }
    $client = Start-Windows 'windows-discovered-join' '--lan-find --lan-pin=1234 --lan-name=Windows --lan-stay'
    Wait-Windows $client 'windows-discovered-join' 'LAN JOINED'
    Wait-Phone 'phone-host' 'roster=PhoneHost:False\|Windows:True'; Capture-Phone 'phone-host-lobby'
    if (Select-String "$output/*errors.log","$output/phone-*.log" -Pattern 'ERROR:|SCRIPT ERROR:|Unhandled exception|FATAL EXCEPTION') { throw 'Runtime errors observed.' }
    Write-Output 'PASS: physical Android/Windows discover each other via actual LAN broadcast; both hosts reject wrong PIN and admit correct PIN; phone manual IP, fresh lobby rejoin and host-exit behavior verified. No network tunnel.'
} finally {
    & $adb shell run-as org.quizparty.game rm -f $deviceFixture
    & $adb shell rm -f /sdcard/quizparty-phase07.png
    foreach ($process in $processes) { if (!$process.HasExited) { Stop-Process -Id $process.Id }; $process.Dispose() }
    & $adb shell am force-stop org.quizparty.game
    & $adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game | Out-Null
}

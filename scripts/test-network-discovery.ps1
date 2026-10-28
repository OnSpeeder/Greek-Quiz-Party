param([int]$Port = 17787, [int]$DiscoveryPort = 17788, [switch]$Packaged, [switch]$Capture)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/phase07-network$(if ($Packaged) { '-packaged' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$baseArgs = "--headless --path `"$GodotProject`" --"
if ($Packaged) { $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'; $baseArgs = '--headless --' }
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
function Start-Lan([string]$Name, [string]$Flags) {
    $launch = $baseArgs
    if ($Capture -and $Name -in @('scan','host-match')) {
        $launch = $baseArgs -replace '--headless', '--resolution 1152x900 --language el_GR'
        $Flags += " --lan-capture=$output/$Name.png"
    }
    $process = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$launch --lan-port=$Port --lan-discovery-port=$DiscoveryPort $Flags" `
        -RedirectStandardOutput "$output/$Name.log" -RedirectStandardError "$output/$Name-errors.log"
    $processes.Add($process)
    return $process
}
function Wait-Log([System.Diagnostics.Process]$Process, [string]$Name, [string]$Pattern) {
    $deadline = [DateTime]::UtcNow.AddSeconds(15)
    while (!(Select-String "$output/$Name.log" -Pattern $Pattern -Quiet)) {
        if ($Process.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw "$Name did not log $Pattern. Inspect $output." }
        Start-Sleep -Milliseconds 100
    }
}
function Assert-ExitCode([System.Diagnostics.Process]$Process, [string]$Name, [int]$Code) {
    if (!$Process.WaitForExit(15000) -or $Process.ExitCode -ne $Code) { throw "$Name exit failed; expected $Code. Inspect $output." }
}
function Stop-Lan([System.Diagnostics.Process]$Process) {
    if (!$Process.HasExited) { Stop-Process -Id $Process.Id; $Process.WaitForExit(5000) | Out-Null }
}
try {
    $server = Start-Lan 'host' '--lan-host --lan-stay --lan-pin=1234'
    Wait-Log $server 'host' 'HostListening'
    $scan = Start-Lan 'scan' '--lan-find --lan-scan-only'
    Assert-ExitCode $scan 'scan' 0
    if (!(Select-String "$output/scan.log" -Pattern "LAN FOUND .*port=$Port .*requiresPin=True state=Lobby" -Quiet)) { throw 'Broadcast did not discover the PIN room/custom game port.' }
    $wrong = Start-Lan 'wrong' '--lan-find --lan-pin=9999'
    Assert-ExitCode $wrong 'wrong' 2
    if (!(Select-String "$output/wrong.log" -Pattern 'STATUS WrongPin' -Quiet)) { throw 'Discovered room did not reject wrong PIN.' }
    $missing = Start-Lan 'missing' '--lan-join=127.0.0.1'
    Assert-ExitCode $missing 'missing' 2
    if (!(Select-String "$output/missing.log" -Pattern 'STATUS WrongPin' -Quiet)) { throw 'Manual join bypassed the PIN.' }
    $found = Start-Lan 'found' '--lan-find --lan-name=Phone --lan-pin=1234'
    Assert-ExitCode $found 'found' 0
    $manual = Start-Lan 'manual' '--lan-join=127.0.0.1 --lan-name=Phone --lan-pin=1234'
    Assert-ExitCode $manual 'manual' 0
    $idA = [regex]::Match((Get-Content "$output/found.log" -Raw), 'LAN JOINED player=([^\r\n]+)').Groups[1].Value
    $idB = [regex]::Match((Get-Content "$output/manual.log" -Raw), 'LAN JOINED player=([^\r\n]+)').Groups[1].Value
    if (!$idA -or !$idB -or $idA -eq $idB) { throw 'Lobby rejoin did not create a fresh identity.' }
    foreach ($attempt in 1..4) {
        $rejected = Start-Lan "pin-$attempt" '--lan-join=127.0.0.1 --lan-pin=9999'
        Assert-ExitCode $rejected "pin-$attempt" 2
    }
    $limited = Start-Lan 'limited' '--lan-join=127.0.0.1 --lan-pin=1234'
    Assert-ExitCode $limited 'limited' 2
    if (!(Select-String "$output/limited.log" -Pattern 'PinRateLimited' -Quiet)) { throw 'Reconnect bypassed PIN rate limits.' }
    Stop-Lan $server

    $server = Start-Lan 'host-started' '--lan-host --lan-stay --lan-start-players=2'
    Wait-Log $server 'host-started' 'HostListening'
    $waiting = Start-Lan 'waiting' '--lan-join=127.0.0.1 --lan-stay'
    Wait-Log $waiting 'waiting' 'phase=GameStarting'
    $startedScan = Start-Lan 'started-scan' '--lan-find --lan-scan-only'
    Assert-ExitCode $startedScan 'started-scan' 0
    if (!(Select-String "$output/started-scan.log" -Pattern 'state=GameStarting' -Quiet)) { throw 'Started room metadata was not updated.' }
    Stop-Lan $server
    Assert-ExitCode $waiting 'waiting' 0
    if (!(Select-String "$output/waiting.log" -Pattern 'LAN SERVER_LEFT match-cannot-resume' -Quiet)) { throw 'No clear host-exit outcome.' }

    $server = Start-Lan 'host-match' '--lan-host --lan-stay --lan-start-players=2 --lan-match'
    Wait-Log $server 'host-match' 'HostListening'
    $departing = Start-Lan 'departing' '--lan-join=127.0.0.1 --lan-name=Phone --lan-leave-question'
    Assert-ExitCode $departing 'departing' 0
    Wait-Log $server 'host-match' 'LAN MATCH_PAUSED'
    $returning = Start-Lan 'returning' '--lan-join=127.0.0.1 --lan-name=Phone'
    Assert-ExitCode $returning 'returning' 2
    if (!(Select-String "$output/returning.log" -Pattern 'STATUS GameStarted' -Quiet)) { throw 'Match re-entry unexpectedly allowed.' }
    Wait-Log $server 'host-match' 'LAN MATCH_FINISHED disconnected-seat-timed-out'
    if (!(Select-String "$output/host-match.log" -Pattern 'phase=GameOver .*scores=Host:[1-9]\d*\|Phone:0' -Quiet)) { throw 'Disconnected seat did not expire safely.' }
    Stop-Lan $server

    $empty = Start-Lan 'empty' '--lan-find --lan-scan-only --lan-expect-empty'
    Assert-ExitCode $empty 'empty' 0
    if (!(Select-String "$output/empty.log" -Pattern 'STATUS NoRooms' -Quiet)) { throw 'Empty discovery did not give fallback guidance.' }
    if (Select-String "$output/*errors.log" -Pattern 'ERROR:|SCRIPT ERROR:|Unhandled exception') { throw 'Runtime errors observed.' }
    Write-Output 'PASS: actual UDP broadcast discovery/custom port, PIN rejection/admission/rate limits, manual IP, fresh lobby rejoin, started advertisements, host exit and safe match departure.'
} finally {
    foreach ($process in $processes) { Stop-Lan $process; $process.Dispose() }
}

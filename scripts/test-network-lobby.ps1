param([int]$Port = 17778, [switch]$Packaged)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot 'artifacts/phase03-network'
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$sceneArgs = "--headless --path `"$GodotProject`" --"
if ($Packaged) {
    $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'
    if (!(Test-Path -LiteralPath $binary)) { throw 'Export Windows before running packaged lobby checks.' }
    $sceneArgs = '--headless --'
    $output = Join-Path $RepoRoot 'artifacts/phase03-network-packaged'
    New-Item -ItemType Directory -Force $output | Out-Null
}
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()

function Start-LobbyProcess([string]$Name, [string]$Flags) {
    $process = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$sceneArgs --lobby-port=$Port --lobby-auto $Flags" `
        -RedirectStandardOutput "$output/$Name.log" -RedirectStandardError "$output/$Name-errors.log"
    $processes.Add($process)
    return $process
}

function Wait-Log([System.Diagnostics.Process]$Process, [string]$Name, [string]$Pattern, [int]$Seconds = 15) {
    $deadline = [DateTime]::UtcNow.AddSeconds($Seconds)
    while (!(Select-String -Path "$output/$Name.log" -Pattern $Pattern -Quiet)) {
        if ($Process.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw "$Name did not log $Pattern. Inspect $output." }
        Start-Sleep -Milliseconds 100
    }
}

function Assert-ProcessExit([System.Diagnostics.Process]$Process, [string]$Name, [int]$Expected) {
    if (!$Process.WaitForExit(15000)) { throw "$Name did not exit in time." }
    if ($Process.ExitCode -ne $Expected) { throw "$Name exit $($Process.ExitCode), expected $Expected. Inspect $output." }
}

try {
    $hostProcess = Start-LobbyProcess 'host' '--lobby-host --lobby-name=Host'
    Wait-Log $hostProcess 'host' 'HostListening'
    $first = Start-LobbyProcess 'first' '--lobby-join=127.0.0.1 --lobby-name=Anna --lobby-test-start --lobby-exit-start'
    $second = Start-LobbyProcess 'second' '--lobby-join=127.0.0.1 --lobby-name=Maria --lobby-exit-start'
    Wait-Log $hostProcess 'host' 'AUTO_STARTED revision=7 players=3'
    Wait-Log $first 'first' 'AUTO_STARTED revision=7 players=3'
    Wait-Log $second 'second' 'AUTO_STARTED revision=7 players=3'
    foreach ($name in @('host', 'first', 'second')) {
        if (!(Select-String "$output/$name.log" -Pattern 'phase=GameStarting roster=Anna:True\|Host:True\|Maria:True' -Quiet)) {
            throw "$name did not observe the same ready roster."
        }
    }
    if (!(Select-String "$output/first.log" -Pattern 'AUTO_CLIENT_START_REJECTED' -Quiet)) { throw 'Remote start was not rejected.' }
    # Start is terminal for this phase; new joins must fail even while peers still exist.
    $late = Start-LobbyProcess 'late' '--lobby-join=127.0.0.1 --lobby-name=Late'
    Assert-ProcessExit $late 'late' 2
    if (!(Select-String "$output/late.log" -Pattern 'STATUS GameStarted' -Quiet)) { throw 'Late join was not rejected.' }
    Assert-ProcessExit $first 'first' 0
    Assert-ProcessExit $second 'second' 0
    Wait-Log $hostProcess 'host' 'revision=9 phase=GameStarting roster=Host:True'
    $wrongVersion = Start-LobbyProcess 'rejected' '--lobby-join=127.0.0.1 --lobby-name=Rejected --lobby-protocol=99'
    Assert-ProcessExit $wrongVersion 'rejected' 2
    if (!(Select-String "$output/rejected.log" -Pattern 'IncompatibleVersion' -Quiet)) { throw 'Version mismatch was not rejected.' }
    Stop-Process -Id $hostProcess.Id
    $hostProcess.WaitForExit(5000) | Out-Null

    $exitHost = Start-LobbyProcess 'exit-host' '--lobby-host --lobby-name=Host'
    Wait-Log $exitHost 'exit-host' 'HostListening'
    $exitClient = Start-LobbyProcess 'exit-client' '--lobby-join=127.0.0.1 --lobby-name=Waiting'
    Wait-Log $exitClient 'exit-client' 'STATUS Joined'
    Stop-Process -Id $exitHost.Id
    $exitHost.WaitForExit(5000) | Out-Null
    Assert-ProcessExit $exitClient 'exit-client' 0
    if (!(Select-String "$output/exit-client.log" -Pattern 'AUTO_SERVER_LEFT' -Quiet)) { throw 'Client did not observe host exit.' }
    $unreachable = Start-LobbyProcess 'unreachable' '--lobby-join=127.0.0.1 --lobby-name=Waiting'
    Assert-ProcessExit $unreachable 'unreachable' 2
    if (!(Select-String "$output/unreachable.log" -Pattern 'ConnectionTimeout|ConnectionFailed' -Quiet)) { throw 'No bounded no-host error.' }
    $cancelled = Start-LobbyProcess 'cancelled' '--lobby-join=127.0.0.1 --lobby-name=Waiting --lobby-cancel-join'
    Assert-ProcessExit $cancelled 'cancelled' 0
    if (!(Select-String "$output/cancelled.log" -Pattern 'AUTO_CANCEL_PASS' -Quiet)) { throw 'Freed join transport callback was not safely canceled.' }
    if (Select-String "$output/*errors.log" -Pattern 'ERROR:|SCRIPT ERROR:|Unhandled exception') { throw 'Engine/runtime errors observed.' }
    Write-Output 'PASS: ENet host + two clients share roster/readiness/start revision 7; duplicate setters safe; remote start, late join and version rejected; disconnect cleanup, host exit, no-host timeout and freed join cancellation verified.'
} finally {
    foreach ($process in $processes) {
        if (!$process.HasExited) { Stop-Process -Id $process.Id; $process.WaitForExit(5000) | Out-Null }
        $process.Dispose()
    }
}

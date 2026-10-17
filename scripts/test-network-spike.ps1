param([int]$Port = 17777)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot 'artifacts/phase01-network'
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$sceneArgs = "--headless --path `"$GodotProject`" res://Scenes/LanSpike.tscn --"
$hostProcess = $null
try {
    $hostProcess = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$sceneArgs --spike-host --spike-port=$Port" `
        -RedirectStandardOutput "$output/host.log" -RedirectStandardError "$output/host-errors.log"
    $deadline = [DateTime]::UtcNow.AddSeconds(15)
    while (!(Select-String -Path "$output/host.log" -Pattern 'HOST_LISTENING' -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Probe host did not start.' }
        Start-Sleep -Milliseconds 100
    }
    $client = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$sceneArgs --spike-join=127.0.0.1 --spike-port=$Port --spike-auto" `
        -RedirectStandardOutput "$output/client.log" -RedirectStandardError "$output/client-errors.log"
    if (!$client.WaitForExit(25000)) { Stop-Process -Id $client.Id; throw 'Probe client timed out.' }
    if ($client.ExitCode -ne 0 -or !(Select-String "$output/client.log" -Pattern 'AUTO_PASS' -Quiet)) {
        throw "Round trip failed; inspect $output."
    }
    if (!(Select-String "$output/host.log" -Pattern 'count=1 duplicate=True' -Quiet) -or
        (Select-String "$output/host.log" -Pattern 'count=2' -Quiet)) { throw 'Duplicate action was not idempotent.' }

    $rejected = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$sceneArgs --spike-join=127.0.0.1 --spike-port=$Port --spike-protocol=99 --spike-auto" `
        -RedirectStandardOutput "$output/rejected.log" -RedirectStandardError "$output/rejected-errors.log"
    if (!$rejected.WaitForExit(25000)) { Stop-Process -Id $rejected.Id; throw 'Protocol rejection timed out.' }
    if ($rejected.ExitCode -ne 2 -or !(Select-String "$output/rejected.log" -Pattern 'HELLO_REJECTED' -Quiet)) {
        throw 'Incompatible protocol was not rejected.'
    }
    Stop-Process -Id $hostProcess.Id
    $hostProcess.WaitForExit(5000) | Out-Null
    $hostProcess = $null
    $unreachable = Start-Process $binary -WindowStyle Hidden -PassThru `
        -ArgumentList "$sceneArgs --spike-join=127.0.0.1 --spike-port=$Port --spike-auto" `
        -RedirectStandardOutput "$output/unreachable.log" -RedirectStandardError "$output/unreachable-errors.log"
    if (!$unreachable.WaitForExit(25000)) { Stop-Process -Id $unreachable.Id; throw 'Unreachable-host check timed out.' }
    if ($unreachable.ExitCode -ne 2 -or !(Select-String "$output/unreachable.log" -Pattern 'CONNECTION_TIMEOUT|CONNECTION_FAILED' -Quiet)) {
        throw 'Unreachable host did not produce a bounded connection failure.'
    }
    if (Select-String "$output/*errors.log" -Pattern 'ERROR:|SCRIPT ERROR:') {
        throw 'Network processes reported engine errors.'
    }
    Write-Output 'PASS: separate-process ENet handshake/action/ack, duplicate safety, protocol rejection, unreachable-host timeout.'
} finally {
    if ($hostProcess -and !$hostProcess.HasExited) { Stop-Process -Id $hostProcess.Id }
}

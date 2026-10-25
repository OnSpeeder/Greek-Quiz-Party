param([switch]$Packaged, [int]$Port = 19863)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/match-flow-process$(if ($Packaged) { '-packaged' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$launch = "--path `"$GodotProject`""
if ($Packaged) { $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'; $launch = '' }
$peers = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
try {
    foreach ($role in @('host', 'local', 'remote')) {
        $folder = Join-Path $output $role; New-Item -ItemType Directory -Force $folder | Out-Null
        $flags = if ($role -eq 'host') { '--match-flow-host' } else { "--match-flow-client --match-flow-name=$role" }
        if ($role -eq 'local') { $flags += ' --match-flow-local' }
        $size = if ($role -eq 'host') { '1280x720' } else { '420x900' }
        $peer = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "$launch --resolution $size --language el_GR -- --ui-preview --ui-greek --ui-reduced-motion $flags --match-flow-port=$Port --match-flow-capture=$folder" `
            -RedirectStandardOutput "$output/$role.log" -RedirectStandardError "$output/$role-errors.log"
        $peers.Add($peer)
        if ($role -eq 'host') {
            $deadline = [DateTime]::UtcNow.AddSeconds(25)
            while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
                if ($peer.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Flow host did not listen.' }
                Start-Sleep -Milliseconds 100
            }
        }
    }
    foreach ($peer in $peers) {
        if (!$peer.WaitForExit(45000) -or $peer.ExitCode -ne 0) { throw "Flow process failed; inspect $output." }
    }
    $finals = @()
    foreach ($role in @('host', 'local', 'remote')) {
        $log = Get-Content "$output/$role.log" -Raw
        if ($log -notmatch 'FLOW REPLAY_PASS roster=3 ready=false match=null') { throw "$role did not observe replay." }
        $finals += [regex]::Match($log, 'FLOW FINAL ([^\r\n]+)').Groups[1].Value
        if ((Get-Item "$output/$role-errors.log").Length -gt 0) { throw "$role runtime errors observed." }
    }
    if (!$finals[0] -or ($finals | Select-Object -Unique).Count -ne 1) { throw 'Flow scores disagree.' }
    Write-Output "PASS: host observer + two client connections / three seats; unanimous reveal, next question, end and room-preserving replay. $output"
} finally {
    foreach ($peer in $peers) { if (!$peer.HasExited) { $peer.Kill() }; $peer.Dispose() }
}

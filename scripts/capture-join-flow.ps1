param([ValidateSet('rooms','pin','identity')][string]$Step = 'identity',
    [int]$Width = 420, [int]$Height = 900, [switch]$LargeText)
. "$PSScriptRoot/common.ps1"
$output = Join-Path $RepoRoot "artifacts/join-flow-$Step-${Width}x$Height$(if ($LargeText) { '-large' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$hostProcess = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "--headless --path `"$GodotProject`" -- --lan-host --lan-stay --lan-pin=1234 --lan-port=17841 --lan-discovery-port=17842" `
    -RedirectStandardOutput "$output/host.log" -RedirectStandardError "$output/host-errors.log"
try {
    $deadline = [DateTime]::UtcNow.AddSeconds(20)
    while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Preview host did not start.' }
        Start-Sleep -Milliseconds 100
    }
    $large = if ($LargeText) { '--ui-large-text' } else { '' }
    $clientProcess = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "--path `"$GodotProject`" res://Scenes/Lobby.tscn --resolution ${Width}x$Height -- --ui-preview --ui-greek --ui-reduced-motion --ui-join --ui-join-step=$Step --ui-discovery-port=17842 $large --ui-capture=`"$output/preview.png`"" `
        -RedirectStandardOutput "$output/client.log" -RedirectStandardError "$output/client-errors.log"
    try {
        if (!$clientProcess.WaitForExit(20000) -or $clientProcess.ExitCode -ne 0) { throw 'Join preview failed.' }
        foreach ($role in @('host','client')) { if ((Get-Item "$output/$role-errors.log").Length -gt 0) { throw "Inspect $output/$role-errors.log" } }
        if (!(Test-Path "$output/preview.png")) { throw 'No viewport image produced.' }
        Write-Output "PASS: actual LAN discovery/PIN and $Step viewport -> $output/preview.png"
    } finally { if (!$clientProcess.HasExited) { $clientProcess.Kill() }; $clientProcess.Dispose() }
} finally { if (!$hostProcess.HasExited) { $hostProcess.Kill() }; $hostProcess.Dispose() }

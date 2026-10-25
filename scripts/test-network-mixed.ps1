param([int]$Port = 17791, [ValidateRange(0,8)][int]$HostPlayers = 2,
    [ValidateRange(0,7)][int]$ClientPlayers = 3, [ValidateRange(0,6)][int]$SecondClientPlayers = 0,
    [ValidateSet(10,20,30)][int]$QuestionCount = 20, [switch]$Teams, [switch]$Strategy,
    [switch]$Packaged, [switch]$Capture)
. "$PSScriptRoot/common.ps1"
$total = $HostPlayers + $ClientPlayers + $SecondClientPlayers
if ($total -lt 2 -or $total -gt 8 -or ($ClientPlayers -eq 0 -and $SecondClientPlayers -gt 0)) { throw 'Choose 2–8 total players.' }
$output = Join-Path $RepoRoot "artifacts/phase09-$HostPlayers-$ClientPlayers-$SecondClientPlayers$(if ($Teams) { '-teams' })$(if ($Packaged) { '-packaged' })"
New-Item -ItemType Directory -Force $output | Out-Null
$binary = (Get-Godot) -replace '_console\.exe$', '.exe'
$launch = "--headless --path `"$GodotProject`" --"
if ($Packaged) { $binary = Join-Path $RepoRoot 'artifacts/exports/Windows/QuizParty.exe'; $launch = '--headless --' }
$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
$names = [System.Collections.Generic.List[string]]::new()
function Start-Mixed([string]$Name, [string]$Flags) {
    $arguments = $launch
    if ($Capture -and $Name -eq 'host') { $arguments = $launch -replace '--headless', '--resolution 1152x900 --language el_GR'; $Flags += " --match-capture=$output/final.png" }
    if ($Teams) { $Flags += ' --match-teams' }
    if ($Strategy) { $Flags += ' --match-strategy' }
    $process = Start-Process $binary -WindowStyle Hidden -PassThru -ArgumentList "$arguments --match-mixed --match-auto --match-port=$Port --match-players=$total $Flags" `
        -RedirectStandardOutput "$output/$Name.log" -RedirectStandardError "$output/$Name-errors.log"
    $processes.Add($process); $names.Add($Name); return $process
}
try {
    $hostProcess = Start-Mixed 'host' "--match-host --match-name=Host --match-local=$HostPlayers --match-fixture=$QuestionCount"
    $deadline = [DateTime]::UtcNow.AddSeconds(20)
    while (!(Select-String "$output/host.log" -Pattern HostListening -Quiet)) {
        if ($hostProcess.HasExited -or [DateTime]::UtcNow -gt $deadline) { throw 'Mixed host did not listen.' }; Start-Sleep -Milliseconds 100
    }
    if ($ClientPlayers -gt 0) { $null = Start-Mixed 'first' "--match-join=127.0.0.1 --match-name=PhoneA --match-local=$ClientPlayers" }
    if ($SecondClientPlayers -gt 0) { $null = Start-Mixed 'second' "--match-join=127.0.0.1 --match-name=PhoneB --match-local=$SecondClientPlayers" }
    foreach ($process in $processes) {
        if (!$process.WaitForExit(30000 + 5000 * $QuestionCount)) { throw 'Mixed match timed out.' }
        if ($process.ExitCode -ne 0) { throw "Mixed process exited $($process.ExitCode); inspect $output." }
    }
    $finals = @($names | ForEach-Object { Get-Content "$output/$_.log" | Where-Object { $_ -like 'MIXED FINAL *' } | Select-Object -Last 1 })
    if (!$finals[0] -or ($finals | Select-Object -Unique).Count -ne 1) { throw 'Mixed final scores/teams/missions/stats disagree.' }
    $final = $finals[0].Substring('MIXED FINAL '.Length) | ConvertFrom-Json
    if ($final.Scores.Count -ne $total -or $final.Statistics.Count -ne $total) { throw 'Not every logical player completed.' }
    if ($Teams) {
        if ($final.Teams.Count -ne 2 -or $final.WinningTeams.Count -ne 1 -or $final.WinningTeams[0] -ne 1) { throw 'Unexpected team result.' }
        foreach ($team in $final.Teams) {
            $expected = ($final.Scores | Where-Object { $team.Members -contains $_.PlayerId } | Measure-Object Total -Sum).Sum
            if ($team.Total -ne $expected) { throw 'Team aggregate differs from individual totals.' }
        }
    }
    if ($Strategy -and ($final.FinalStrategy | Measure-Object CardsUsed -Sum).Sum -lt 1) { throw 'No strategy card used in mixed match.' }
    foreach ($name in $names) {
        $log = Get-Content "$output/$name.log" -Raw
        if ($log -notmatch "MIXED PASS players=$total questions=$QuestionCount ") { throw "$name did not complete the expected full match." }
    }
    if (Select-String "$output/*errors.log" -Pattern 'ERROR:|SCRIPT ERROR:|Unhandled exception') { throw 'Mixed runtime errors observed.' }
    if ($Capture -and !(Test-Path "$output/final.png")) { throw 'Mixed final capture missing.' }
    Write-Output "PASS: $total logical players ($HostPlayers local + $ClientPlayers/$SecondClientPlayers remote slots), $QuestionCount questions, teams=$Teams strategy=$Strategy; all peers agree. Evidence: $output"
} finally {
    foreach ($process in $processes) { if (!$process.HasExited) { Stop-Process -Id $process.Id }; $process.Dispose() }
}

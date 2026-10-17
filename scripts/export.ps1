param([ValidateSet('Windows', 'Android')][string]$Platform = 'Windows')
. "$PSScriptRoot/common.ps1"
& "$PSScriptRoot/validate-content.ps1" -Stage
$destination = Join-Path $RepoRoot "artifacts/exports/$Platform"
New-Item -ItemType Directory -Force $destination | Out-Null
$filename = if ($Platform -eq 'Android') { 'QuizParty.apk' } else { 'QuizParty.exe' }
$arguments = @('--headless', '--path', $GodotProject)
if ($Platform -eq 'Android' -and !(Test-Path "$GodotProject/android/build/build.gradle")) {
    $arguments += '--install-android-build-template'
}
$arguments += @('--export-debug', $Platform, (Join-Path $destination $filename))
$log = Join-Path $destination 'export.log'
$stdout = Join-Path $destination 'stdout.log'
$stderr = Join-Path $destination 'stderr.log'
# Wait for the exporter itself, not its long-lived ADB descendant or inherited pipes.
$quotedArguments = ($arguments | ForEach-Object { '"' + $_ + '"' }) -join ' '
$binary = Get-Godot
$directBinary = $binary -replace '_console\.exe$', '.exe'
if (Test-Path -LiteralPath $directBinary) { $binary = $directBinary }
$process = Start-Process -FilePath $binary -ArgumentList $quotedArguments -WindowStyle Hidden `
    -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
if (!$process.WaitForExit(600000)) {
    Stop-Process -Id $process.Id
    throw "$Platform export timed out after ten minutes. See $stdout and $stderr."
}
Get-Content $stdout, $stderr | Set-Content -Encoding utf8 $log
Get-Content $log
if ($process.ExitCode -ne 0) { throw "$Platform export failed (exit $($process.ExitCode)). See $log" }
# Godot 4.7.2 can return zero after a failed .NET publish. Inspect its diagnostics too.
$errors = Select-String -Path $log -Pattern '^ERROR:' | Where-Object {
    $_.Line -notlike '*EditorSettings not instantiated yet*export/android/shutdown_adb_on_exit*'
}
if ($errors) { throw "$Platform export reported errors. See $log" }
if (!(Test-Path (Join-Path $destination $filename))) { throw 'Export package was not produced.' }

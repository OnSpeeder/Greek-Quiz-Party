. "$PSScriptRoot/common.ps1"
git -C $RepoRoot rev-parse --show-toplevel
Assert-Exit 'Git root'
dotnet --list-sdks
Assert-Exit '.NET SDK inventory'
& (Get-Godot) --version
Assert-Exit 'Godot version'
$gh = Resolve-Tool 'gh' @('C:/Program Files/GitHub CLI/gh.exe')
& $gh --version
& $gh auth status
if ($LASTEXITCODE -ne 0) { Write-Warning 'GitHub CLI requires interactive sign-in.' }
& (Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")) devices
Assert-Exit 'ADB inventory'

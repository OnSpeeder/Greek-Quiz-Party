. "$PSScriptRoot/common.ps1"
$testDirectory = Join-Path $RepoRoot 'artifacts/phase05-cli'
New-Item -ItemType Directory -Force $testDirectory | Out-Null
Copy-Item "$RepoRoot/content/questions/el-GR/manifest.json" "$testDirectory/manifest.json" -Force
(Get-Content "$RepoRoot/content/questions/el-GR/greece.json" -Raw).Replace('"reviewed"', '"draft"') | Set-Content -Encoding utf8 "$testDirectory/draft.json"
dotnet run --no-build --project "$RepoRoot/tools/QuizParty.QuestionValidator" -- $testDirectory
if ($LASTEXITCODE -ne 1) { throw 'Release CLI did not reject draft content with exit 1.' }
dotnet run --no-build --project "$RepoRoot/tools/QuizParty.QuestionValidator" --
if ($LASTEXITCODE -ne 2) { throw 'Invalid CLI usage did not exit 2.' }
Write-Output 'PASS: content CLI rejects unreviewed content (1) and invalid usage (2).'

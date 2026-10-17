param([switch]$Stage)
. "$PSScriptRoot/common.ps1"
$source = Join-Path $RepoRoot 'content/questions/el-GR'
dotnet run --project "$RepoRoot/tools/QuizParty.QuestionValidator" -- $source --locale=el-GR
Assert-Exit 'Reviewed question pack validation'
if ($Stage) {
    $target = Join-Path $GodotProject 'Content/el-GR'
    New-Item -ItemType Directory -Force $target | Out-Null
    # Only this generated folder is synchronized; remove stale JSON files individually.
    foreach ($file in Get-ChildItem -LiteralPath $target -File -Filter '*.json') {
        if (!(Test-Path -LiteralPath (Join-Path $source $file.Name))) { Remove-Item -LiteralPath $file.FullName }
    }
    Get-ChildItem -LiteralPath $source -File -Filter '*.json' | Copy-Item -Destination $target -Force
}

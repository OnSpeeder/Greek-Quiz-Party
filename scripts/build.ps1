. "$PSScriptRoot/common.ps1"
Push-Location $RepoRoot
try {
    dotnet restore QuizParty.sln
    Assert-Exit 'Restore'
    dotnet build QuizParty.sln --no-restore
    Assert-Exit 'Build'
    & "$PSScriptRoot/validate-content.ps1" -Stage
} finally { Pop-Location }

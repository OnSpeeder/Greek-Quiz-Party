. "$PSScriptRoot/common.ps1"
Push-Location $RepoRoot
try {
    dotnet restore QuizParty.sln
    Assert-Exit 'Restore'
    dotnet build QuizParty.sln --no-restore
    Assert-Exit 'Build'
} finally { Pop-Location }

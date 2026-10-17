param([switch]$IncludeGodot)
. "$PSScriptRoot/common.ps1"
Push-Location $RepoRoot
try {
    dotnet test tests/QuizParty.Core.Tests --settings .runsettings
    Assert-Exit 'Core tests'
    dotnet test tests/QuizParty.IntegrationTests --settings .runsettings
    Assert-Exit 'Integration tests'
    if ($IncludeGodot) {
        $env:GODOT_BIN = Get-Godot
        & $env:GODOT_BIN --headless --path $GodotProject --editor --import --quit
        Assert-Exit 'Godot import'
        # The adapter launches its own build, which must inherit this property too.
        $previousGodotTests = $env:EnableGodotTests
        try {
            $env:EnableGodotTests = 'true'
            dotnet test "$GodotProject/QuizParty.Godot.csproj" --settings .runsettings
            Assert-Exit 'Godot tests'
        } finally { $env:EnableGodotTests = $previousGodotTests }
        # Restore a production assembly without test-only dependencies after the test run.
        dotnet build "$GodotProject/QuizParty.Godot.csproj" -t:Rebuild
        Assert-Exit 'Production rebuild'
    }
} finally { Pop-Location }

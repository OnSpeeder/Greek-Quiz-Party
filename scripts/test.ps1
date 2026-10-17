param([switch]$IncludeGodot)
. "$PSScriptRoot/common.ps1"
& "$PSScriptRoot/validate-content.ps1" -Stage
& "$PSScriptRoot/test-content-cli.ps1"
Push-Location $RepoRoot
try {
    dotnet test tests/QuizParty.Core.Tests --settings .runsettings
    Assert-Exit 'Core tests'
    dotnet test tests/QuizParty.IntegrationTests --settings .runsettings
    Assert-Exit 'Integration tests'
    if ($IncludeGodot) {
        $importBinary = Get-Godot
        & $importBinary --headless --path $GodotProject --editor --import --quit
        Assert-Exit 'Godot import'
        # The adapter manages and redirects a child process itself. Use the real
        # engine, avoiding the Windows console forwarding wrapper (also avoided
        # by exports/network tests) and its inherited-pipe shutdown behavior.
        $env:GODOT_BIN = $importBinary -replace '_console\.exe$', '.exe'
        if (!(Test-Path -LiteralPath $env:GODOT_BIN)) { $env:GODOT_BIN = $importBinary }
        # The adapter launches its own build, which must inherit this property too.
        $previousGodotTests = $env:EnableGodotTests
        try {
            $env:EnableGodotTests = 'true'
            dotnet test "$GodotProject/QuizParty.Godot.csproj" --settings .runsettings --logger 'console;verbosity=detailed'
            Assert-Exit 'Godot tests'
        } finally { $env:EnableGodotTests = $previousGodotTests }
        # Restore a production assembly without test-only dependencies after the test run.
        dotnet build "$GodotProject/QuizParty.Godot.csproj" -t:Rebuild
        Assert-Exit 'Production rebuild'
    }
} finally { Pop-Location }

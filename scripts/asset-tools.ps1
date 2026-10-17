. "$PSScriptRoot/common.ps1"

function Get-Inkscape {
    Resolve-Tool 'inkscape' @($env:INKSCAPE_PATH, 'C:/Program Files/Inkscape/bin/inkscape.com')
}

function Get-Blender {
    $candidates = @($env:BLENDER_PATH)
    # Respect custom installation drives rather than assuming Program Files.
    $registryRoots = @(
        'HKLM:/Software/Microsoft/Windows/CurrentVersion/Uninstall/*',
        'HKCU:/Software/Microsoft/Windows/CurrentVersion/Uninstall/*'
    )
    foreach ($registryRoot in $registryRoots) {
        $installs = Get-ItemProperty $registryRoot -ErrorAction SilentlyContinue |
            Where-Object { $_.DisplayName -eq 'Blender' -and $_.InstallLocation } |
            Sort-Object DisplayVersion -Descending
        foreach ($install in $installs) {
            $candidates += Join-Path $install.InstallLocation 'blender.exe'
        }
    }
    Resolve-Tool 'blender' $candidates
}

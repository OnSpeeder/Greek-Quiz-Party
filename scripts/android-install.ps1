param([string]$Serial, [switch]$LaunchOnly)
. "$PSScriptRoot/common.ps1"
$adb = Resolve-Tool 'adb' @("$env:LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe")
$deviceArgs = @()
if ($Serial) { $deviceArgs = @('-s', $Serial) }
if (!$LaunchOnly) {
    & $adb @deviceArgs install -r (Join-Path $RepoRoot 'artifacts/exports/Android/QuizParty.apk')
    Assert-Exit 'APK installation'
}
# Resolve the exported launcher alias rather than the non-exported GodotApp activity.
& $adb @deviceArgs shell am start -W -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p org.quizparty.game
Assert-Exit 'Android launch'

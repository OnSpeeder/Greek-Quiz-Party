# Original editable SVG masters. Re-run to reproduce the production UI skin.
$ErrorActionPreference = 'Stop'
$assetRoot = Join-Path (Split-Path $PSScriptRoot -Parent) 'src/QuizParty.Godot/Art/Settings'
New-Item -ItemType Directory -Force $assetRoot | Out-Null
function Write-Vector([string]$Name, [int]$Width, [int]$Height, [string]$Body) {
    $svg = "<svg xmlns=`"http://www.w3.org/2000/svg`" width=`"$Width`" height=`"$Height`" viewBox=`"0 0 $Width $Height`">$Body</svg>"
    [IO.File]::WriteAllText((Join-Path $assetRoot "$Name.svg"), $svg, [Text.UTF8Encoding]::new($false))
}
$defs = '<defs><linearGradient id="gold" x2="0" y2="1"><stop stop-color="#fff0b8"/><stop offset=".35" stop-color="#ffd580"/><stop offset=".7" stop-color="#d79838"/><stop offset="1" stop-color="#925019"/></linearGradient><linearGradient id="purple" x2="0" y2="1"><stop stop-color="#8b4cc1"/><stop offset=".5" stop-color="#603092"/><stop offset="1" stop-color="#35204e"/></linearGradient><linearGradient id="cyan" x2="0" y2="1"><stop stop-color="#71e3ef"/><stop offset="1" stop-color="#145eab"/></linearGradient></defs>'
$frame = $defs + '<rect x="3" y="5" width="250" height="250" rx="30" fill="#170c2b"/><rect x="5" y="3" width="246" height="246" rx="28" fill="url(#gold)"/><rect x="12" y="10" width="232" height="232" rx="23" fill="url(#purple)" stroke="#fff0b8" stroke-width="2"/><rect x="21" y="20" width="214" height="214" rx="17" fill="#392157" stroke="#b77bd3" stroke-width="2"/>'
foreach ($x in @(25,231)) { foreach ($y in @(25,231)) { $frame += "<circle cx=`"$x`" cy=`"$y`" r=`"7`" fill=`"url(#gold)`" stroke=`"#784120`" stroke-width=`"2`"/>" } }
Write-Vector 'frame-main' 256 256 $frame
Write-Vector 'frame-card' 128 128 ($defs + '<rect x="2" y="2" width="124" height="124" rx="22" fill="#231737" stroke="#c99149" stroke-width="3"/><rect x="7" y="7" width="114" height="114" rx="17" fill="#302047" stroke="#8551a6" stroke-width="2"/>')
foreach ($state in @('normal','hover','pressed','active','disabled')) {
    $fill = switch ($state) { 'hover' { '#14516c' } 'pressed' { '#3c2661' } 'active' { '#145e85' } 'disabled' { '#343141' } default { 'url(#purple)' } }
    $edge = if ($state -eq 'disabled') { '#8b8296' } else { 'url(#gold)' }
    Write-Vector "button-$state" 192 96 ($defs + "<rect x=`"2`" y=`"5`" width=`"188`" height=`"89`" rx=`"23`" fill=`"#190d2e`"/><rect x=`"3`" y=`"2`" width=`"186`" height=`"88`" rx=`"22`" fill=`"$edge`"/><rect x=`"9`" y=`"8`" width=`"174`" height=`"75`" rx=`"17`" fill=`"$fill`" stroke=`"#fff0b8`" stroke-width=`"1.5`"/><path d=`"M23 14H169`" stroke=`"#ffffff`" stroke-opacity=`".24`" stroke-width=`"3`" stroke-linecap=`"round`"/>")
}
Write-Vector 'header-trim' 768 160 ($defs + '<path d="M42 38Q60 16 95 20H673Q710 16 726 38L756 80 726 122Q710 145 673 140H95Q60 145 42 122L12 80Z" fill="url(#gold)" stroke="#724323" stroke-width="4"/><path d="M50 44Q60 30 96 31H672Q704 30 718 44L740 80 718 116Q704 130 672 129H96Q60 130 50 116L28 80Z" fill="url(#purple)" stroke="#fff0b8" stroke-width="3"/><circle cx="60" cy="80" r="7" fill="url(#gold)"/><circle cx="708" cy="80" r="7" fill="url(#gold)"/>')
foreach ($on in @($false,$true)) {
    $state = if ($on) { 'on' } else { 'off' }; $fill = if ($on) { 'url(#cyan)' } else { '#302047' }; $cx = if ($on) { 91 } else { 29 }
    Write-Vector "switch-$state" 120 56 ($defs + "<rect x=`"2`" y=`"2`" width=`"116`" height=`"52`" rx=`"26`" fill=`"$fill`" stroke=`"url(#gold)`" stroke-width=`"4`"/><circle cx=`"$cx`" cy=`"28`" r=`"22`" fill=`"url(#gold)`" stroke=`"#784120`" stroke-width=`"2`"/><circle cx=`"$cx`" cy=`"26`" r=`"16`" fill=`"#ffe4a0`"/>")
    Write-Vector "switch-track-$state" 120 56 ($defs + "<rect x=`"2`" y=`"2`" width=`"116`" height=`"52`" rx=`"26`" fill=`"$fill`" stroke=`"url(#gold)`" stroke-width=`"4`"/>")
}
Write-Vector 'switch-space' 120 56 '<rect width="120" height="56" fill="none"/>'
foreach ($state in @('idle','pressed','disabled')) {
    $fill = if ($state -eq 'disabled') { '#8b8296' } elseif ($state -eq 'pressed') { 'url(#cyan)' } else { 'url(#gold)' }
    Write-Vector "slider-thumb-$state" 48 48 ($defs + "<circle cx=`"24`" cy=`"25`" r=`"22`" fill=`"#321b41`"/><circle cx=`"24`" cy=`"23`" r=`"21`" fill=`"$fill`" stroke=`"#fff0b8`" stroke-width=`"2`"/><circle cx=`"24`" cy=`"22`" r=`"15`" fill=`"none`" stroke=`"#b9792d`" stroke-width=`"2`"/>")
}
Write-Vector 'slider-track' 128 20 ($defs + '<rect x="2" y="2" width="124" height="16" rx="8" fill="#1b1232" stroke="url(#gold)" stroke-width="3"/>')
Write-Vector 'slider-fill' 128 20 ($defs + '<rect x="2" y="2" width="124" height="16" rx="8" fill="url(#cyan)" stroke="url(#gold)" stroke-width="3"/>')
Write-Vector 'mascot-plinth' 512 160 ($defs + '<path d="M20 40H492V135Q256 177 20 135Z" fill="url(#purple)" stroke="#c99149" stroke-width="5"/><ellipse cx="256" cy="42" rx="240" ry="36" fill="url(#gold)" stroke="#fff0b8" stroke-width="4"/><path d="M64 92Q256 130 448 92" fill="none" stroke="#71e3ef" stroke-width="3"/>')
Write-Vector 'sparkle-gold' 32 32 '<path d="M16 1 20 12 31 16 20 20 16 31 12 20 1 16 12 12Z" fill="#ffd580"/>'
$icons = @{
    'close' = '<path d="m9 9 14 14m0-14L9 23"/>'
    'back' = '<path d="m13 6-9 9 9 9M5 15h14q9 0 9 10"/>'
    'volume-high' = '<path d="m15 5-8 6H3v10h4l8 6ZM20 10q6 6 0 12m5-17q10 11 0 22"/>'
    'volume-low' = '<path d="m15 5-8 6H3v10h4l8 6ZM21 11q5 5 0 10"/>'
    'mute' = '<path d="m15 5-8 6H3v10h4l8 6ZM21 11l8 10m0-10-8 10"/>'
    'gear' = '<path d="m12 3 1 4h6l1-4 5 3-2 4 3 5 4-1v6l-4-1-3 5 2 4-5 2-1-4h-6l-1 4-5-2 2-4-3-5-4 1v-6l4 1 3-5-2-4Z"/><circle cx="16" cy="16" r="5"/>'
    'language' = '<circle cx="16" cy="16" r="13"/><ellipse cx="16" cy="16" rx="6" ry="13"/><path d="M3 16h26M6 9h20M6 23h20"/>'
    'help' = '<circle cx="16" cy="16" r="13"/><path d="M12 11a4 4 0 1 1 7 3l-3 3v2m0 5v1"/>'
    'controller' = '<path d="M9 9h14q5 0 6 6l1 9q0 5-4 3l-6-5h-8l-6 5q-4 2-4-3l1-9q1-6 6-6Z M10 13v8m-4-4h8m8-3v1m4 3v1"/>'
}
foreach ($entry in $icons.GetEnumerator()) { Write-Vector "icon-$($entry.Key)" 32 32 ("<g fill=`"none`" stroke=`"#ffd580`" stroke-width=`"2.5`" stroke-linecap=`"round`" stroke-linejoin=`"round`">$($entry.Value)</g>") }
# Apply the integrated Inkscape study after generating shared icons/switch pieces.
& python "$PSScriptRoot/export-settings-study-skin.py"
if ($LASTEXITCODE -ne 0) { throw 'Inkscape study skin derivation failed.' }
Write-Output "Settings SVG masters regenerated in $assetRoot"

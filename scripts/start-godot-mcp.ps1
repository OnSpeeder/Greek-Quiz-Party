. "$PSScriptRoot/common.ps1"
# Optional local HTTP mode for diagnostics. Codex normally starts the configured
# stdio server itself. Stop HTTP mode before reloading Codex (both use port 9080).
$server = Resolve-Tool 'godot-editor-mcp' @("$env:USERPROFILE/.local/bin/godot-editor-mcp.exe")
$env:GODOT_MCP_TRANSPORT = 'http'
$env:GODOT_MCP_GODOT_BIN = Get-Godot
$env:GODOT_MCP_PROJECT_DIR = $GodotProject
& $server
Assert-Exit 'Godot MCP service'

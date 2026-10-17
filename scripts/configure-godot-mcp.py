"""Replace only the Godot MCP config; keep a private backup beside user config."""
import os
import re
import shutil
import tomllib
from pathlib import Path

config = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "config.toml"
original = config.read_text(encoding="utf-8")
backup = config.with_name("config.before-quizparty-toolchain.toml")
if backup.exists():
    raise SystemExit(f"Backup already exists: {backup}; refusing to overwrite it.")
shutil.copy2(config, backup)
updated = re.sub(r'(?ms)^\[mcp_servers\.godot-mcp(?:\.[^\]]+)?\]\s*\n.*?(?=^\[|\Z)', '', original)
binary = (Path.home() / ".local/bin/godot-editor-mcp.exe").as_posix()
project = (Path(__file__).resolve().parents[1] / "src/QuizParty.Godot").as_posix()
updated += f'''\n[mcp_servers.godot-mcp]
command = "{binary}"
startup_timeout_sec = 30

[mcp_servers.godot-mcp.env]
GODOT_MCP_GODOT_BIN = "C:/Godot/godot_console.exe"
GODOT_MCP_PROJECT_DIR = "{project}"
'''
tomllib.loads(updated)
config.write_text(updated, encoding="utf-8")
print(f"Configured live-editor MCP. Private backup: {backup}")

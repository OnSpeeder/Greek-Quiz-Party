"""Inspect the local Godot MCP service and save metadata (never screenshot base64)."""
import asyncio
import base64
import json
import sys
from pathlib import Path
from fastmcp import Client


async def main():
    target = "http://127.0.0.1:9090/mcp"
    if "--stdio" in sys.argv:
        target = {"mcpServers": {"godot": {
            "command": str(Path.home() / ".local/bin/godot-editor-mcp.exe"),
            "env": {
                "GODOT_MCP_GODOT_BIN": "C:/Godot/godot_console.exe",
                "GODOT_MCP_PROJECT_DIR": str(Path(__file__).resolve().parents[1] / "src/QuizParty.Godot"),
            },
        }}}
    async with Client(target) as client:
        tools = await client.list_tools()
        selected = [{"name": tool.name, "description": tool.description,
                     "inputSchema": tool.input_schema}
                    for tool in tools if any(word in tool.name for word in
                        ("scene_tree", "screenshot", "status", "toolset", "scene_open"))]
        Path("artifacts/mcp-tools.json").write_text(json.dumps(selected, indent=2), encoding="utf-8")
        enabled = await client.call_tool("godot_enable_toolset", {"category": "editor"})
        if enabled.is_error:
            raise RuntimeError(str(enabled))
        # Allow the editor addon's reconnect timer to see a freshly started server.
        for attempt in range(15):
            tree = await client.call_tool("godot_inspection_get_scene_tree", {}, raise_on_error=False)
            if not tree.is_error:
                break
            await asyncio.sleep(1)
        if tree.is_error:
            raise RuntimeError(str(tree))
        Path("artifacts/mcp-scene-tree.json").write_text(
            json.dumps(tree.structured_content, indent=2), encoding="utf-8")
        print("Live scene tree saved to artifacts/mcp-scene-tree.json")
        screenshot = await client.call_tool("godot_editor_capture_screenshot", {"timeout_ms": 10000})
        if screenshot.is_error:
            raise RuntimeError(str(screenshot))
        for block in screenshot.content:
            if block.type == "image":
                Path("artifacts/editor-screenshot.png").write_bytes(base64.b64decode(block.data))
                print("Editor screenshot saved to artifacts/editor-screenshot.png")
            elif block.type == "text":
                print(block.text[:1000])


asyncio.run(main())

# Development dependencies

These dependencies support the user-approved setup work. No runtime service or
paid dependency was added. Versions are pinned; do not update during a milestone
without rerunning the checks.

| Dependency | Version | Purpose / license / platform boundary |
| --- | --- | --- |
| Godot .NET SDK/editor/templates | 4.7.2 | MIT; required engine; matching official mono export templates verified using official SHA512-SUMS.txt |
| xUnit | 2.9.3 | Apache-2.0; pure .NET tests; test projects only |
| xUnit VS adapter | 3.1.5 | Apache-2.0; VSTest discovery; test projects only |
| Microsoft.NET.Test.Sdk | 17.14.1 | MIT; VSTest; test builds only |
| GdUnit4 addon | 6.2.2 | MIT; maintained upstream Godot editor test UI; vendored with LICENSE |
| gdUnit4.api / test.adapter | 5.1.0-rc5 / 3.1.1 | MIT; C# scene testing; opt-in EnableGodotTests only, excluded from Windows/Android production assemblies |
| hybridindie Godot MCP addon/server | 2026.10.15 | MIT; live editor inspection, screenshots, controlled editing; addon vendored, server installed using uv; development only |

The available GdUnit NuGet release predates the upstream source's published Godot
4.7 support matrix. This exact combination was verified by executing the C# scene
test on Godot 4.7.2; future scene tests must keep validating compatibility. We do
not suppress package incompatibility warnings or disable failing tests.

The MCP server runs on localhost. Its Python dependencies are isolated in uv's
tool environment; they are not bundled into the game. Both editor addons and
test scripts are excluded by the export presets. Godot's generated Android build
tree is excluded from C# compilation to prevent copied scripts compiling twice.

Upstream sources:
- https://github.com/hybridindie/godot-mcp/tree/2026.10.15
- https://github.com/godot-gdunit-labs/gdUnit4/tree/v6.2.2
- https://github.com/godot-gdunit-labs/gdUnit4Net
- https://github.com/xunit/xunit
- https://github.com/microsoft/vstest
- https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/c_sharp_basics.html

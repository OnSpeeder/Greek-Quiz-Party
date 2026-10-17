# CODEX_SETUP.md

This guide describes the recommended local Codex toolchain for developing QuizParty on Windows.

> The installed, tested setup is recorded in [TOOLCHAIN_STATUS.md](TOOLCHAIN_STATUS.md).
> Prefer its pinned versions and scripts over the generic installation examples below.

## Recommended model of operation

Use Codex locally from the project directory so it can access:

- repository files,
- PowerShell/terminal,
- `git` and optionally `gh`,
- `dotnet`,
- Godot executable,
- Android `adb`,
- the Godot MCP server.

Do **not** install a generic filesystem MCP just to let Codex edit the repo. Local Codex already has filesystem/shell capabilities. Add MCP only where it gives specialized access, especially the live Godot editor.

## 1. Install/update Codex CLI

Prerequisite: Node.js/npm available.

```powershell
npm install -g @openai/codex@latest
codex --version
codex doctor
```

Sign in when Codex prompts you. Current Codex clients can use your eligible ChatGPT plan; API-key workflows are separate when explicitly using the API.

## 2. Install base developer tools

Required executables in PATH:

```text
git
dotnet
godot
adb
java
node/npm
codex
```

Recommended extras:

```text
gh
uv (if using hybridindie Godot MCP via uv/Python tooling)
```

Verify:

```powershell
git --version
dotnet --info
java -version
adb version
node --version
npm --version
codex --version
```

Godot may not be globally on PATH by default. Either add its directory to PATH or configure a stable executable path/wrapper.

## 3. GitHub

Codex can use local `git`. For GitHub operations, the cleanest local option is GitHub CLI:

```powershell
gh auth login
gh auth status
```

Use HTTPS authentication unless you specifically prefer SSH.

Optional: install the GitHub plugin from Codex `/plugins` if you want connector-style issue/PR/CI workflows. Local `git`/`gh` is still necessary for normal repository work and observed command output.

## 4. OpenAI developer documentation MCP

Useful for Codex/OpenAI questions, not required for the game itself.

```powershell
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

The Codex CLI/IDE extension share MCP configuration.

## 5. Godot MCP — recommended specialized tool

Recommended implementation for this project: `hybridindie/godot-mcp` because it targets modern Godot, exposes live editor inspection/manipulation, screenshots, run/export capabilities and supports Windows.

Install Python 3.11+ and preferably `uv`.

Example server install:

```powershell
uv tool install godot-editor-mcp
```

or:

```powershell
pip install godot-editor-mcp
```

Then verify the command starts:

```powershell
godot-editor-mcp --help
```

Register with Codex as stdio MCP:

```powershell
codex mcp add godot -- godot-editor-mcp
codex mcp list
```

Equivalent user config is conceptually:

```toml
[mcp_servers.godot]
command = "godot-editor-mcp"
args = []
```

The user config on Windows is under `%USERPROFILE%\.codex\config.toml`.

### Godot addon

Install the matching Godot MCP addon into the Godot project from its documented release/Asset Library process, then enable it in:

`Project -> Project Settings -> Plugins`

Start the MCP server and open Godot. Confirm the plugin status panel reports a connection before asking Codex to edit scenes.

Pin a tested release/version instead of blindly updating during a milestone.

## 6. GdUnit4

Install inside Godot through AssetLib:

1. Open Godot project.
2. Open AssetLib.
3. Search `GdUnit4`.
4. Download/install.
5. Project -> Project Settings -> Plugins.
6. Enable GdUnit4.
7. Restart Godot if needed.

Use GdUnit4 for scene/UI integration tests. Keep pure game rules in normal .NET unit tests.

## 7. Android toolchain

Install:

- Android Studio or standalone Android SDK,
- Android SDK Platform Tools,
- required build tools/platform,
- JDK 17,
- Godot Android export templates compatible with your editor version.

Enable USB debugging on test device.

Verify:

```powershell
adb devices
```

Authorize the PC on the phone when prompted.

Codex does not need a special ADB MCP. It can execute `adb` through terminal access. This is simpler and produces direct logs.

Useful commands:

```powershell
adb devices
adb install -r path\to\app.apk
adb logcat
```

## 8. Godot command line

Expose a stable `godot` command to Codex.

Verify:

```powershell
godot --version
```

Later repository scripts should wrap common actions, for example:

```text
scripts/build.ps1
scripts/test.ps1
scripts/run-host.ps1
scripts/run-client.ps1
scripts/android-install.ps1
```

Prefer scripts checked into the repo over repeatedly asking the agent to remember long command sequences.

## 9. Project-specific Codex configuration

Run Codex from repository root:

```powershell
cd C:\path\to\QuizParty
codex
```

Codex automatically recognizes `AGENTS.md` repository guidance.

Use `harness/build/phase-XX-*.md` as the explicit task scope.

Recommended first prompt:

```text
Read AGENTS.md, PRODUCT.md, ARCHITECTURE.md, TESTING.md and
harness/build/phase-00-repository-foundation.md only as needed.
Inspect the current repository state and implement Phase 00.
Do not start Phase 01. Run the required verification and record evidence
in harness/build-log.md.
```

## 10. Screenshot/vision workflow

Use Godot MCP screenshot/editor tools when available. Codex itself can reason over screenshots supplied to the client, but for an autonomous edit-run-inspect loop the Godot MCP should expose the live editor/game screenshot capability.

Do not rely on screenshots alone for correctness; pair them with build/test logs.

## 11. Recommended permissions

Start conservatively. Allow Codex to edit the repository and run normal build/test commands, but require approval for:

- external publishing,
- destructive Git commands,
- release signing,
- secrets,
- system-wide changes,
- commands outside project/tool directories when unexpected.

## 12. What not to connect initially

Avoid adding overlapping tools with the same purpose.

Do not initially add:

- generic filesystem MCP,
- several different Godot MCPs simultaneously,
- database MCP (no DB is needed for v1),
- Play Store publishing automation,
- production signing-key tools,
- arbitrary browser automation.

Add capabilities only when a real milestone needs them.

## 13. Tool verification checklist

Before Phase 01, ask Codex to run/read only and report:

```text
codex --version
git --version
gh auth status
dotnet --info
godot --version
java -version
adb devices
codex mcp list
```

Then open Godot and verify Godot MCP by asking Codex to inspect the current scene tree and capture a screenshot without changing anything.

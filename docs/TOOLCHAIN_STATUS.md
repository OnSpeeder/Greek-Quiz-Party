# Verified local development setup

Verified on 2026-10-17. This is the foundation/toolchain setup, not the LAN spike
or a playable trivia game.

## Ready

Product/technical identity is now **QuizParty**. Current paths, commands and export
names below use the renamed projects. Earlier raw logs and build-log entries
retain the names actually observed before the rename. Android package ID is now
`org.quizparty.game`, so it installs separately from the earlier development APK.
The existing GitHub remote URL is preserved; no remote repository was renamed.

- Asset tools: Inkscape 1.4.4 and Blender 5.2.2 LTS are verified through executable
  version checks, SVG export, a Blender CPU render and GLB export, and clean Godot
  SVG/GLB import. See [ASSET_WORKFLOW.md](ASSET_WORKFLOW.md) for paths and helpers.

- Git metadata is at `C:/chatgpt_projects/QuizParty/.git`. Original commit
  `d34062c` and origin URL were preserved. Nothing was pushed or published.
- GitHub CLI 2.102.0 works at `C:/Program Files/GitHub CLI/gh.exe`.
  Authentication and `gh api user` succeeded for OnSpeeder. If an older app
  process has stale PATH, use that absolute path or `scripts/doctor.ps1`.
- Godot 4.7.2 .NET is at `C:/Godot`. The game project is
  `src/QuizParty.Godot/project.godot`, using Compatibility rendering.
- SDK 10.0.401 is pinned in `global.json`; Core, infrastructure and desktop target
  net8.0. Android targets net9.0, as required by Godot's C# Android export.
  The installed SDK successfully publishes that target; the game does not need
  to target net10.0 merely because SDK 10 is used to build it.
- Official matching mono export templates are installed under
  `%APPDATA%/Godot/export_templates/4.7.2.stable.mono`; official SHA-512 verified.
- JDK 17, Android platform 36 and build tools 36.1.0 are installed. Godot's local
  editor settings point to Java, the Android SDK and the existing debug keystore.
- xUnit checks and the C# GdUnit scene smoke test execute successfully.
- A fresh source-only copy restored, built with zero warnings/errors, and started
  headless without borrowing the project's local .godot/bin/obj caches.
- Windows debug export launches and prints `QuizParty: C# startup ready.`
- Android ARM64 debug APK is produced and its v2 signature verifies. It includes
  all three managed assemblies, the Mono runtime and Godot native library, and
  excludes editor addons/tests. Package ID: `org.quizparty.game`; min API 24,
  target API 36. Debug signing only; no production signing credentials added.
- APK installation succeeded on the connected physical Android 15 phone (model
  23013PC75G). Launch returned Status: ok; app-specific logcat contains the C#
  startup marker, and a screenshot showed the responsive foundation screen.
- Live editor scene-tree inspection and screenshot capture were observed using
  hybridindie Godot MCP 2026.10.15. Its MIT addon is enabled in the project.
  User MCP config replaces the old limited server and has a private backup at
  `%USERPROFILE%/.codex/config.before-quizparty-toolchain.toml`.

## Commands

Run from the workspace root in PowerShell:

```powershell
./scripts/doctor.ps1
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
./scripts/smoke.ps1
./scripts/export.ps1 -Platform Windows
./scripts/export.ps1 -Platform Android
./scripts/android-install.ps1 # requires one authorized, connected phone
git diff --check
```

The root `QuizParty.sln` builds all projects. Godot also requires the local
`src/QuizParty.Godot/QuizParty.Godot.sln` for editor publishing. Keep
both solutions in sync when adding game project references. Export packages and
raw logs are in ignored `artifacts/`.

## Remaining human/runtime gates

- Windows-to-phone LAN communication and gameplay/touch behavior remain Phase 01
  or later work. Successful APK installation/launch does not prove networking.
- Reload the Codex client/chat to load the replacement MCP tool catalog. The
  configured stdio server starts with Codex; open this Godot project so its addon
  can connect. Never run the optional HTTP diagnostic server at the same time.
- CI workflow is checked in under `.github/workflows/ci.yml`; its equivalent
  commands were run locally. No remote CI execution was claimed or requested.
- Godot 4.7.2 prints `EditorSettings not instantiated yet` for
  `export/android/shutdown_adb_on_exit` during editor/export teardown. This exact
  engine diagnostic is retained in logs and excluded from the export script's
  failure scan only after exit/package checks. All other `ERROR:` lines fail the
  export. Windows packaged runtime startup is clean. Do not interpret the known
  teardown diagnostic as a green engine log.
- Android SDK Manager reports a pre-existing duplicate command-line-tools
  `latest-2` directory. It did not block SDK installation or APK creation; it was
  left untouched to avoid changing unrelated tool installations.
- The question validator project is an explicit nonzero-exit placeholder for
  Phase 05. No content validation or future game behavior is claimed complete.

See `DEPENDENCIES.md` for dependency purpose, versions, licenses and boundaries.

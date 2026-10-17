# Phase 00 / toolchain context — 2026-10-17

## Product rename

User renamed the game to **QuizParty**. Current root solution is QuizParty.sln;
projects/namespaces use QuizParty.*, Godot path is src/QuizParty.Godot, Android
package is org.quizparty.game. Scripts, MCP path and concept branding are updated.
Fresh build, three tests, Windows runtime, Android export and actual Android launch
were verified after renaming. Historical build-log entries keep original names;
the GitHub remote was not renamed. Greek remains the initial primary language.

- User authorized fixing the tooling gaps and reporting each result. Scope covers
  foundation and export validation only; no LAN/gameplay implementation.
- Preserved Git history by relocating nested metadata to the workspace root.
  The duplicate nested `.gitattributes` was removed after preserving its root copy.
- Moved starter project to `src/QuizParty.Godot`; root solution builds all
  projects and Godot-local solution satisfies Godot C# export requirements.
- SDK 10.0.401 builds net8.0 Core/desktop and net9.0 Android. Android framework
  exception verified against official Godot docs and an actual successful publish.
- `EnableGodotTests=true` must be an inherited environment property: the GdUnit
  adapter invokes an internal dotnet build. Production rebuild removes test code
  and test-only dependencies. Generated adapter and Android trees are excluded
  from production compilation; Android's copied scripts otherwise cause CS0111.
- Export scripts inspect diagnostics: Godot can return zero after C# publish
  fails. Direct executable plus redirected files avoids console-wrapper waiting
  on ADB's inherited output pipe. Known engine teardown diagnostic is explicitly
  documented; other engine errors must fail the script.
- Current MCP HTTP process was temporary diagnostic infrastructure. Permanent
  Codex config uses the pinned server executable in stdio mode. Backup stays
  outside repository. A client reload is required to expose the new native tools.
- Dependencies and licensing are recorded in docs/DEPENDENCIES.md. Scene has only
  a localized, responsive foundation status display and C# startup probe.
- QuestionValidator is deliberately unimplemented and returns 2 rather than
  falsely validating content. Phase 01 still requires real phone + LAN evidence.
- Real Android 15 hardware is now authorized and was observed running the APK.
  Install required user approval on the phone; the original direct activity was
  non-exported, so scripts now resolve the public MAIN/LAUNCHER intent. C# startup
  marker and rendered screen verified. LAN communication remains unimplemented.

# Toolchain and repository setup plan

## Goal and scope
Resolve the tooling gaps identified on 2026-10-17: repository layout, reproducible
build/test scripts and CI, Godot editor inspection/screenshots, test frameworks,
and Windows/Android debug export readiness. This authorizes foundation work and
export-tool validation only; gameplay and the LAN technical spike remain out of scope.

## Approach and affected components
- Preserve the existing Git history while relocating its metadata to the workspace root.
- Move the starter Godot project into the documented architecture; create empty
  Core/Infrastructure, validator and test projects, without implementing future phases.
- Use .NET 8 for Core/desktop and the verified Android-required .NET 9 target.
- Pin and document test/editor dependencies and install matching export templates.
- Supply local scripts, a CI baseline, smoke tests, and evidence in the build log.
- Replace the limited Godot MCP configuration with the documented live-editor MCP;
  preserve a configuration backup outside Git.

## Risks and assumptions
- GitHub authentication and physical-phone authorization require the user's participation.
- Editor configuration may require a new chat/client reload for native MCP tools.
- Android APK/tool validation is not completion of Phase 01 LAN acceptance.
- No pushing, publishing, release signing, or game rules are included.

## Verification and acceptance
Restore/build the solution; execute real .NET and Godot scene smoke tests; import/open
the editor; observe scene-tree and screenshot access; export Windows and Android debug
packages where dependencies permit; run git diff --check. Record failures honestly.

## Recovery
Preserve original Git commits, starter files where moved, and a backup of modified
user MCP configuration. Generated packages/caches stay ignored. No history rewriting.

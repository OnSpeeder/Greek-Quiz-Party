# AGENTS.md

## Repository mission

Build a production-quality Greek-first Windows/Android party trivia game using Godot 4.7.2 .NET and C#. The final design is defined in the repository documents; do not invent product scope when a source document already owns the decision.

## Mandatory technology constraints

- Godot 4.7.2 .NET.
- C# for game/application code.
- .NET 8 unless a verified Godot/platform constraint requires adjustment.
- Windows + Android are required target platforms.
- Core game rules must remain independent of Godot.
- LAN gameplay is host-authoritative.
- JSON/data-driven question packs for v1.

## Read context selectively

Use:

- `PRODUCT.md` when deciding product behavior/scope.
- `GAME_DESIGN.md` for scoring, modes, cards and missions.
- `ARCHITECTURE.md` for code boundaries.
- `NETWORK_PROTOCOL.md` for networking.
- `CONTENT_FORMAT.md` when touching question packs/validator.
- `TESTING.md` when adding or verifying behavior.
- the current file under `harness/build/` for active phase.

Do not load every document for unrelated trivial edits.

## Architecture rules

1. `QuizParty.Core` must not reference Godot.
2. UI scripts render state and send intents; they do not own authoritative rules.
3. Client never calculates authoritative score.
4. Client never selects authoritative random outcomes.
5. Client must not receive correct answer before reveal.
6. Separate `PlayerId`, `ConnectionId` and `LocalSlot`.
7. Network DTOs are not domain objects.
8. Host receive time determines whether a network answer is timely.
9. Randomness and clocks must be injectable/testable in Core.
10. Avoid God classes and global mutable singletons.

## C# style

- Enable nullable reference types.
- Prefer clear domain types over magic integers/strings.
- Keep methods focused.
- Prefer immutable records/DTOs where appropriate.
- Use async cancellation tokens for cancellable operations.
- Do not swallow exceptions silently.
- Avoid reflection/dynamic unless there is a documented need.
- Follow existing formatting and analyzer configuration.

## Godot rules

- Use Containers/anchors for responsive UI; avoid hardcoded pixel positioning as the main layout strategy.
- Design for both TV/desktop landscape and mobile layouts.
- Keep scenes composable.
- Avoid putting business logic in `_Process`.
- Do not make frame rate affect timers/scoring.
- Use localization keys for user-facing UI text.
- Preserve touch-friendly hit targets.

## Networking rules

- Validate every client request on host.
- State-changing requests must be idempotent or duplicate-safe.
- Bound inbound strings/lists/indices.
- Preserve the manual-IP transport API and regression coverage. User decision (2026-10-25): hide manual-IP controls from the normal join UI; retain implementation for possible reintroduction.
- Protocol changes require tests and protocol-version compatibility review.
- Never trust client-supplied timestamps for scoring deadlines.

## Content rules

- Production questions live under `content/questions/<locale>/`.
- Do not bulk-generate and mark AI-produced questions as reviewed.
- Run QuestionValidator after content changes.
- Release packs must contain only reviewed questions.
- Preserve UTF-8 Greek characters and accents.

## Visual & UI Polish Rules (Showtime Direction)
1. **Typography & Greek Diacritics:** Never use the default Godot system font. All labels and buttons must use a bold, rounded display font that fully supports Greek (`el-GR`) accents (e.g., Rubik Bold/Black or Fredoka Bold). Question text must use `AutowrapMode.WordSmart` and a shadow/outline (`font_outline_size = 4`, `font_outline_color = #120A2A`).
2. **Sticker/Chunky Game-Show StyleBoxes:** Never use unstyled Buttons or flat 1px-border panels. Every interactive card and button must use a `StyleBoxFlat` with:
   - `CornerRadiusTopLeft/Right/BottomLeft/Right` = 18
   - `BorderWidthLeft/Top/Right` = 3, `BorderWidthBottom` = 8 (creates a 3D tactile button lip)
   - `ShadowSize` = 8, `ShadowOffset` = Vector2(0, 4), `ShadowColor` = Color(0, 0, 0, 0.35)
   - `ContentMarginLeft/Right` = 20, `ContentMarginTop/Bottom` = 16
3. **Distinct Answer Colors (Accessible):** Answer buttons A/B/C/D must each have a distinct high-contrast badge (A = Coral Red `#FF4B6E`, B = Electric Blue `#2B95FF`, C = Amber Gold `#FFB800`, D = Emerald `#1AD598`) plus a geometric shape/letter badge so colorblind players never rely on color alone.
4. **Mandatory Juice & Tweening (Unless Reduced Motion is On):**
   - Always set `PivotOffset = Size / 2f` before scaling any Control.
   - Stagger the entrance of the 4 Answer Buttons by `0.06s` each using `Tween.TransitionType.Back` and `Tween.EaseType.Out` (scale from `0.85` to `1.0` over `0.28s`).
   - On button hover/press, tween scale to `0.95` (press) and bounce to `1.04` (release).
   - During `AnswerReveal`, pulse the correct answer button (`Scale` 1.0 -> 1.08 -> 1.0) and dim wrong answers to `Modulate = new Color(1, 1, 1, 0.45f)`.
   - On `Scoreboard`, animate score numbers counting up over `0.6s` using `TweenMethod` rather than snapping instantly to the new integer.

## Tests

GitHub CI is disabled by user decision. Use local verification and record evidence;
do not require remote CI success or re-enable workflows unless the user asks.

For meaningful code changes, run the smallest relevant set plus required gates.

Typical commands after repository exists:

```powershell
dotnet restore
dotnet build
dotnet test
```

Also run:

- QuestionValidator when content/schema changes.
- Godot/GdUnit tests when scene/UI integration changes.
- network integration tests when protocol changes.
- `git diff --check` before reporting completion.

Never delete, skip or weaken a failing test merely to get green status without explaining and receiving approval.

## Android rule

Android C# networking/export is an early risk. Complete Phase 01 technical spike on real hardware before investing heavily in later systems.

## Dependency policy

Do not add new NuGet packages, Godot plugins or external services casually. Check purpose, maintenance, license and Windows/Android compatibility. Prefer built-in .NET/Godot capabilities.

## Security and secrets

Never commit:

- API tokens,
- GitHub tokens,
- signing keys,
- keystore passwords,
- personal SSH keys,
- MCP service secrets.

Use environment variables or platform credential stores.

## Git discipline

- Inspect `git status` before significant work.
- Keep unrelated changes separate.
- Never use destructive reset/clean/history rewrite without explicit user approval.
- Do not push or publish unless the user has asked for that action/workflow.
- Prefer small commits aligned to completed phases/features.

## Agent workflow

For every approved phase:

1. Read current phase file.
2. Inspect existing implementation before proposing replacement.
3. State any assumption that materially changes scope.
4. Implement incrementally.
5. Build/test as you go.
6. Capture material decisions in phase context.
7. Record verification evidence in build log.
8. Stop at phase boundary.

## Definition of “done”

A feature is not done because code was written. It is done only when:

- acceptance criteria are met,
- relevant automated tests pass,
- necessary manual/runtime verification was actually observed,
- no known blocking error is hidden,
- docs/protocol/content schema are updated if behavior changed.

## Tool usage guidance

When a Godot MCP server is available, use it for editor/scene inspection, controlled scene edits, running the project and screenshots when that is more reliable than editing `.tscn` text blindly. File edits and normal C# refactors may still use the filesystem/editor directly.

Use Git/GitHub tools only for repository workflows. Do not use them as a substitute for local build/test evidence.

## Visual verification workflow

- Reuse `QuizShowTheme`, `ShowtimeTheme` and scene-owned `ShowtimeJuice`; do not
  create a competing theme or motion system. Preserve custom illustrated skins.
- Use the approved cutout art/reference for characters and stages. Primitive
  geometry is a labelled blockout, not finished art. Blender/Inkscape scripts
  remain valid for asset cleanup, export and intentional icons/skins.
- Check distinct wide-host and portrait-controller compositions in actual Godot
  viewports. Keep questions readable on phones; never sacrifice privacy or touch
  targets for fixed percentage layouts. Respect larger text and reduced motion.
- Inspect captures for clipping, Greek accents, spacing and hierarchy; record
  concrete findings. Build/import/headless tests cannot grant visual sign-off.
- Prefer tweens for transient feedback; authored AnimationPlayer tracks remain
  appropriate when timeline choreography benefits. Neither tool guarantees taste.

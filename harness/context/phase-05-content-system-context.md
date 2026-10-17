# Phase 05 context — JSON packs and validator

## Scope and editorial decision
- Phase 04 baseline committed/pushed as ae46e15 at user request. New Phase 05
  work remains local; no final commit/push performed. GitHub CI remains off.
- User explicitly approved the existing Greek capital question's exact wording,
  options/correct answer/explanation as reviewed in this chat on 2026-10-18.
  The official Visit Greece source was checked. content/EDITORIAL.md records it.
  Initial pack contains one reviewed question, not 100–200 invented/reviewed items.
  Larger question volume remains human editorial work; no bulk generation done.

## Implementation decisions
- Core immutable QuestionPack/categories; shared Infrastructure QuestionPackLoader
  used by CLI and Godot. No new NuGet/plugin/service or Core Godot dependency.
- Canonical content/questions/el-GR contains manifest + JSON question arrays.
  content/schema provides editor schemas; shared C# validator owns additional
  cross-file/category/normalized-duplicate/review/wire-budget rules.
- Strict UTF-8 (optional BOM), malformed escaped Unicode/JSON, wrong/unknown/
  duplicate fields, invalid metadata/IDs/answers/index/difficulty/locale/category
  and draft release entries fail with file/question/code diagnostics. Warnings
  cover sources, dates, long text, similarity, encoding and repeated distractors.
- Bounds and exact schema are documented in CONTENT_FORMAT.md. Runtime dimensions
  and conservative encoded-content budget prevent oversized match packets.
- CLI defaults reviewed-only. Exit 0 valid / 1 content/read errors / 2 usage.
  Development may inspect mixed statuses but never returns drafts as playable.
  An empty reviewed set fails. No validator can substitute for factual human QA.
- Build/test/smoke/export run the strict gate and synchronize only JSON into
  ignored src/QuizParty.Godot/Content/el-GR. Explicit export include filter packs
  raw JSON. Stale generated JSON files are removed individually from that folder.
- Godot FileAccess reads inside res://, calls same validator, and injects first
  reviewed definition into host. There is no hardcoded production fallback; removed
  VerticalSliceFixture from Infrastructure and moved match-test fixture to tests.
  Missing/corrupt content rejects hosting with localized error, not a silent demo.
- Stable filename/array order supplies the single-question mode; anti-repeat/
  category scheduling belongs to Phase 06. Network DTOs/protocol remain unchanged
  at v2. Automated bots still know the tiny fixture for regression only.

## Observed checks — 2026-10-18 Europe/Athens
- Build passed, zero warnings/errors. Final test suite: 195 Core + 56 integration
  + 4 Godot tests = 255 passed, none failed/skipped. CLI negative checks observed
  draft failure exit 1 and invalid usage exit 2; strict canonical pack passed.
- Source match and exported Windows host/two-client match passed all phases with
  identical authoritative totals. Export log explicitly includes manifest.json
  and greece.json. Windows/Android debug exports passed after final parser changes.
- Updated APK installed/launched. Physical Android client vs packaged Windows
  host passed: question 000d53c0-3871-436b-b1ad-508efcaba2dc, revision 6,
  Host 876 / Phone 849. Host log confirms CONTENT LOADED locale=el-GR version=0.1.0
  reviewed=1. Preserved under artifacts/phase05-android-client/; screenshot inspected.
- Also tested physical Android as host to directly execute APK JSON FileAccess:
  CONTENT LOADED confirmed, question c99acb78-370c-43c3-88e6-330dc234812d, revision 6,
  PhoneHost 995 / Windows 992, identical on both peers. Logs under
  artifacts/phase05-android-host/. No runtime errors found. Same actual LAN .105/.106;
  no ADB networking tunnel or input injection. Temporary private test config removed
  in finally and normal phone startup restored. Automated, not human touch play.
- Startup smoke passed. Known editor/export shutdown_adb_on_exit diagnostic remains
  visible and unchanged; game/runtime checks were clean. No tests skipped/weakened.
- Generated lock-file churn restored; whitespace/diff check passed after removing
  an extra blank EOF left by deleting the old fixture. JSON/source staging ignored.

## Boundary
Phase 05 acceptance met: validated reviewed pack loads in source, Windows export
and actual Android APK. One initial reviewed question only; no larger library,
full-loop scheduling or broad device/router coverage claimed. Stop. Phase 06
requires separate user approval.

# Phase 05 — JSON content and validation

Baseline Phase 04 pushed as ae46e15. Implement strict versioned manifest/JSON
arrays, shared validator + immutable reviewed repository, CLI and local export
gates. Godot loads through FileAccess (res:// works in Windows/Android PCK), Core
remains engine-free. Stage canonical content/questions/el-GR into ignored Godot
Content before build/import/export; never maintain two edited sources.

Use one initial reviewed question to prove the system, not a bulk question library.
User explicitly approved the exact existing Greece-capital wording/options/answer/
explanation as reviewed on 2026-10-18; source checked against Visit Greece. Record
this editorial approval. Future questions stay draft until human review.

Validate schema/types/unknown or duplicate fields, version/locale/categories,
IDs/text/answers/index/difficulty/explanation/status and source metadata. Release
mode rejects any unreviewed entry. Warnings for long text, near duplicates, stale
dates, sources, encoding and repeated distractors. Fail closed, actionable paths.
Bound file sizes/counts; injectable text reader for Godot and filesystem readers.
No packages, protocol changes, full-game scheduling or new content volume target.

Test required errors, multi-file duplicate handling, normalized Greek/UTF-8,
strict reviewed loading, malformed input and CLI exit codes. Build, xUnit/Godot,
validator, source + packaged network match, Android export/physical match if
device remains available. Update docs/context/log, git diff --check, stop Phase 05.
No final commit/push authorized. Generated staging/lock churn remains uncommitted.

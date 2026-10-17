# PLANS.md — Codex Execution Plan Rules

This project is expected to be implemented through small, reviewable phases. Do not ask Codex to “build the whole game” in one run.

## 1. When to create/use an ExecPlan

Use an execution plan for:

- a roadmap phase,
- networking changes,
- new game mechanics,
- major refactors,
- platform/export changes,
- release work.

Tiny isolated fixes may skip a formal plan.

## 2. Source of truth

Before a phase, use only relevant files:

- `PRODUCT.md` for product scope,
- `GAME_DESIGN.md` for rules,
- `ARCHITECTURE.md` for boundaries,
- `NETWORK_PROTOCOL.md` for network behavior,
- `CONTENT_FORMAT.md` for question/content work,
- `TESTING.md` for verification,
- the selected `harness/build/phase-XX-*.md` for current scope.

Do not re-read every document for every tiny task.

## 3. Every phase plan must contain

- Goal.
- In scope.
- Out of scope.
- Files/components expected to change.
- Technical approach.
- Risks/assumptions.
- Tests/verification.
- Acceptance criteria.
- Rollback/recovery notes if risky.

## 4. Execution behavior

1. Inspect current repository state.
2. Confirm relevant instructions and phase file.
3. Implement only approved phase.
4. Build frequently.
5. Add tests with the behavior.
6. Run defined verification.
7. Record observed evidence in `harness/build-log.md`.
8. Stop when phase acceptance criteria are met or a real blocker is found.
9. Do not automatically begin the next phase.

## 5. Build log format

Append concise entries:

```text
## YYYY-MM-DD — Phase XX — title
- Commit/worktree: ...
- Implemented: ...
- Verification: command -> result
- Manual evidence: ...
- Known limitations: ...
- Next approval needed: ...
```

## 6. Phase context

For material decisions, create/update:

`harness/context/phase-XX-<slug>-context.md`

Record only information that future phases would otherwise need to rediscover: chosen APIs, compatibility constraints, important bugs/workarounds, protocol decisions and device observations.

## 7. Approval gates

Agent must require explicit user approval before:

- destructive Git history operations,
- pushing to a remote unless user has enabled that workflow,
- publishing releases,
- using production signing credentials,
- changing product scope,
- replacing a major architecture decision,
- adding a paid/external service dependency.

# CONTENT_FORMAT.md

## 1. Objective

Questions are external, validated content. Game code must not contain production trivia questions except tiny fixtures used by tests/demos.

## 2. Folder layout

```text
content/questions/
└── el-GR/
    ├── manifest.json
    ├── geography.json
    ├── history.json
    ├── science.json
    ├── greece.json
    └── ...
```

Future locales:

```text
en-US/
de-DE/
...
```

## 3. Question schema

Recommended JSON shape:

```json
{
  "id": "geo_gr_000001",
  "text": "Ποια είναι η πρωτεύουσα της Αυστραλίας;",
  "answers": ["Σίδνεϊ", "Μελβούρνη", "Καμπέρα", "Περθ"],
  "correctAnswerIndex": 2,
  "categoryId": "geography",
  "difficulty": 2,
  "explanation": "Η Καμπέρα είναι η πρωτεύουσα της Αυστραλίας.",
  "source": "https://...",
  "locale": "el-GR",
  "tags": ["oceania", "capitals"],
  "status": "reviewed"
}
```

## 4. Required fields

- `id`: globally unique stable ID.
- `text`: non-empty question text.
- `answers`: exactly 4 for v1 standard multiple choice unless a future question type explicitly changes schema.
- `correctAnswerIndex`: 0–3.
- `categoryId`: must exist in manifest.
- `difficulty`: integer 1–5.
- `explanation`: required for production content.
- `locale`: expected pack locale.
- `status`: draft / reviewed / rejected.

`source` should be required for factual claims in editorial workflow even if source URL is not always shown in-game.

## 5. Editorial quality rules

Questions must:

- have one unambiguously correct answer,
- avoid trick wording unless category explicitly permits it,
- avoid time-sensitive wording without a reference date,
- avoid defamation or unverifiable claims,
- use correct Greek spelling/accents,
- avoid duplicate semantic questions,
- use plausible distractors,
- avoid answer-length clues where possible,
- avoid repeatedly placing correct answer at same position; display order should be randomized by host anyway.

## 6. Time-sensitive facts

Store metadata when needed:

```json
{
  "verifiedAt": "2026-10-01",
  "expiresAfter": "2027-01-01"
}
```

The validator may warn or fail on stale content depending on category.

## 7. Manifest

`manifest.json` defines categories and pack metadata.

Example:

```json
{
  "schemaVersion": 1,
  "locale": "el-GR",
  "packVersion": "1.0.0",
  "categories": [
    { "id": "geography", "nameKey": "CATEGORY_GEOGRAPHY" },
    { "id": "history", "nameKey": "CATEGORY_HISTORY" }
  ]
}
```

## 8. Question Validator

Create `tools/QuizParty.QuestionValidator`.

It must fail CI on production packs for:

- duplicate IDs,
- invalid JSON/schema,
- invalid correct index,
- invalid difficulty,
- invalid/missing category,
- wrong locale,
- blank text/answers,
- duplicate answers inside one question,
- exact duplicate question text,
- missing explanation,
- unreviewed content in release packs.

Warnings:

- suspiciously similar question text,
- very long answer/question,
- stale verification date,
- missing source,
- unusual character encoding,
- repeated distractor patterns.

## 9. Semantic duplicate strategy

Phase 1: normalized text equality and token similarity heuristics.

Optional later: offline embedding/semantic tooling for editorial review. Do not make release builds depend on external AI APIs.

## 10. Content pipeline

1. Add draft question.
2. Run validator.
3. Manual factual/editorial review.
4. Mark `reviewed`.
5. Run validator + content tests.
6. Package with build.

## 11. Localization strings vs question content

UI strings use Godot localization keys (`.po` or supported localization resources).

Questions are locale-specific content packs because their wording, cultural relevance and distractors often need editorial adaptation rather than literal translation.

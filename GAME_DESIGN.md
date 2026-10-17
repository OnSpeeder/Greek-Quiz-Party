# GAME_DESIGN.md

## 1. Design goal

Create a trivia game where knowledge is primary but players repeatedly make interesting decisions. A player who knows many answers should usually win, but confidence choices, streaks and limited tactical cards should produce tension and comeback opportunities.

## 2. Standard Full Game structure

Recommended default:

1. Lobby and rule selection.
2. 3 normal rounds.
3. Score recap between rounds.
4. Final round with slightly higher scoring pressure.
5. Final results and statistics.

Configurable total questions: 10 / 20 / 30 / custom supported later.

## 3. Question flow

1. Host selects next question according to rules and anti-repeat logic.
2. `QuestionStarted` publishes public question data and a server deadline.
3. Player optionally chooses Confidence level.
4. Player submits one answer.
5. Host validates that submission is legal and timely.
6. When all eligible players answer or deadline expires, host closes question.
7. Host reveals correct answer and explanation.
8. Host calculates score, streaks, card effects and mission progress.
9. Clients receive authoritative result snapshot.
10. Continue to scoreboard or next question.

## 4. Categories

Initial categories:

- Ελλάδα
- Ιστορία
- Γεωγραφία
- Επιστήμη
- Τεχνολογία
- Κινηματογράφος & TV
- Μουσική
- Αθλητισμός
- Gaming
- Pop Culture
- Logic / Brain Teasers
- WTF Facts

Categories are data-driven and may be enabled/disabled by the host.

## 5. Difficulty

Use integer difficulty 1–5.

- 1: very easy / broad common knowledge
- 2: easy
- 3: medium
- 4: hard
- 5: expert

Default game should dynamically mix levels rather than present only one level. A future adaptive mode may tune question difficulty, but v1 should remain deterministic and transparent.

## 6. Base scoring

Exact values are balancing parameters, not hardcoded design constants.

Recommended starting model:

- Base correct score: 500.
- Time bonus: 0–500 based on remaining normalized time.
- Wrong base score: 0.
- Confidence modifier applies after base + time calculation.

Example formula:

`raw = baseCorrect + round(timeBonusMax * remainingTimeRatio)`

Then apply confidence and effects.

## 7. Confidence mechanic

Before or while answering, a player chooses one of:

- **Safe x1** — normal reward, no additional penalty.
- **Confident x2** — double positive score; configurable wrong-answer penalty.
- **All-in x3** — triple positive score; larger wrong-answer penalty.

Recommended starting balance:

- x1 correct: `raw`, wrong: `0`
- x2 correct: `raw * 2`, wrong: `-250`
- x3 correct: `raw * 3`, wrong: `-500`

Guardrails:

- Do not allow score below 0 in casual mode; make negative total score an optional advanced rule.
- Confidence selection becomes locked when answer is submitted.
- Host validates confidence value.

## 8. Streaks

Consecutive correct answers build a streak.

Suggested progression:

- 2 correct: visual feedback only.
- 3 correct: +10% scoring modifier.
- 5 correct: +15% and increased Chaos Meter gain.
- 7 correct: award or guarantee a Chaos Card if hand limit allows.

Wrong answer resets streak unless a future special effect says otherwise.

Streak design must avoid snowballing. Cap score multipliers.

## 9. Chaos Meter

Players gain meter primarily through correct answers, difficult questions and selected achievements.

When threshold is reached:

- meter consumes threshold amount,
- player receives a card if below hand limit,
- card selection may be random from an allowed weighted pool or deterministic according to mode.

Default card hand limit: 2.

## 10. Chaos Cards — v1 set

### Shield

Blocks one eligible hostile effect. Expires when consumed or at game end.

### Double Points

Applies x2 to the next eligible question. Must define stacking rules with Confidence; recommended total multiplier cap prevents extreme values.

### 50/50

On a four-choice question, hides two wrong answers for that player. Host chooses valid hidden answers and sends only the personalized presentation result.

### Extra Time

Adds a small amount of personal answer time if activated before a configured cutoff. Host remains authoritative.

### Category Swap

Before a round/question selection point, requests another allowed category. Host performs final selection.

### Target Bet / Steal

Optional and more socially aggressive. If included, use small capped values. Never allow repeated targeting to make one player unable to participate.

## 11. Card design rules

- Every effect has a precise activation window.
- Every effect is validated on host.
- A card is consumed only after host accepts activation.
- Duplicate network messages must be idempotent.
- UI clearly explains card effect before use.
- No card may reveal the correct answer directly.
- Randomness uses host-owned RNG.

## 12. Secret Missions

Each player may receive one hidden mission at match start.

Examples:

- Historian — answer 3 History questions correctly.
- Hot Streak — reach a streak of 4.
- Gambler — win two x3 Confidence bets.
- Speedster — be among fastest correct players 3 times.
- Generalist — answer correctly in 5 different categories.

Mission rules:

- Mission must be possible under selected rules/categories.
- Host assigns mission.
- Progress is authoritative on host.
- Mission identity is sent only to owning player until end-of-game reveal.
- Bonus should matter but not dominate total score.

## 13. Game modes

### Solo

Practice and personal high-score mode. No LAN required.

### Quick Game

10 questions, reduced interstitials, optional Confidence, usually no Secret Missions.

### Full Game

Complete ruleset.

### Team Mode

Players join teams. Individual input remains private; team score aggregates. Optional team discussion timer can be added later.

### Party Screen

Host/TV shows shared question, timers, reveal and scoreboard. Phones show private answer controls, personal cards and mission information.

## 14. Tie-breaker

If first place is tied after final scoring:

1. One or more sudden-death questions.
2. Only tied players are eligible.
3. Correctness first; if multiple correct, fastest validated host-receive time wins.
4. Continue if needed.

## 15. Anti-frustration rules

- Never eliminate a player early in default modes.
- Do not repeatedly target the last-place player.
- Keep card animations short and skippable/reduced-motion compatible.
- Provide explanations after questions but do not stall pacing.
- Host can disable aggressive cards.

## 16. Post-game stats

Display:

- final score,
- correct / wrong / unanswered,
- accuracy %,
- average response time,
- best streak,
- confidence success rate,
- categories strongest/weakest,
- cards used,
- mission result,
- fastest correct answers.

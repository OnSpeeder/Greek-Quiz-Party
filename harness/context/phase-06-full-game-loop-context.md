# Phase 06 — full loop and selection

Phase 05 committed/pushed to origin/main as 4b3d310 at user request. Phase 06
stays local until a new commit/push request. GitHub Actions remains disabled.

## Core

Production uses FullMatch around GameSession. MatchSettings permits 10/20/30
questions, plus an explicit one-question preview, and 5–60 seconds (UI 10/20/30).
The four rounds use the same base/time scoring; final-pressure balancing and
strategic modifiers are not invented in this baseline. Integer boundaries divide
questions nearly evenly; explicit RoundEnd recaps separate rounds.

QuestionDeck filters selected categories, sorts IDs for source-order independent
seeding, shuffles category/difficulty buckets and draws one per bucket each pass.
No replacement, repeat fallback or client selection. Injectable RNG/clock/instance
factory supports full deterministic replay. Every question gets fresh host times
and instance ID. GameSession now accepts a copied eligible set and optional
point suppression; it retains the original default behavior for existing callers.

FullMatch aggregates correct/wrong/unanswered, accepted response duration/count,
and best streak exactly once on reveal. Wrong/unanswered resets streak. Stats
include only questions where a player was eligible, including sudden death.
Accuracy includes unanswered questions; average time includes accepted answers.

Sudden death: only tied leaders answer, regular totals stay unchanged, fastest
correct host receipt wins. Exact fastest ties narrow eligible players; all wrong
or unanswered retains the eligible set. New unique questions continue while
available; deck exhaustion explicitly yields shared winners, not an infinite loop.
OneQuestionMatch remains a tested legacy API; production uses FullMatch.

## Wire and UI

Protocol 3/app 0.3.0 intentionally rejects protocol 1/2 because strict DTOs gain
ordinals, round, eligibility, winners, exhaustion and final-only aggregates.
Same RPC paths, authenticated sender/host receipt and duplicate caches. Pending
and accepted private input reset at each question; stale receipts cannot confirm
the next answer. Client phase ordering is per question and rejects ordinal
rollback/reused instances. Scores carry over, correctness remains reveal-only.

Host settings/category controls live in Containers inside the lobby scroll area.
MatchPanel renders progress, round recap, scores, winners and final stats. It
sends intents only. Spectators during sudden death cannot submit. Lobby updates
during a match do not re-show host Start/settings controls.

Eight-player boundary testing found a real 17,197-byte final packet with the old
12KB encoded-content allowance. Shared validator budget is now 10KB, preserving
the 16KiB envelope limit; test asserts old oversized content is rejected and a
near-new-limit validated question fits final results with eight long Greek names.

Simultaneous departures exposed two sends into closed ENet channels: application
lobby broadcast and SceneMultiplayer's automatic peer-relay disconnect notices.
Adapter checks connected state/allocated channels. Relay is disabled for the
lobby scene lifetime because every message already goes host↔client, then restored
on scene exit. GdUnit checks this lifecycle; process bots keep host alive until
both clients leave, and script requires both departure events with clean errors.
Godot behavior checked against local 4.7.2 API docs and upstream
[SceneMultiplayer source](https://github.com/godotengine/godot/blob/master/modules/multiplayer/scene_multiplayer.cpp).

## Content and regression boundaries

Production still has ONE explicitly human-reviewed question. Capacity is checked
before lobby start against selected categories. Longer matches require more
reviewed content; choosing an unsupported length gives a localized error.
No new questions were marked reviewed. UseSyntheticQuestions/--match-fixture
is guarded by OS.IsDebugBuild and explicit opt-in (10/20/30 plus five spare test
questions), with visible synthetic labels/log marker. Never count fixture runs
as a production content library. Normal host loading still validates packaged JSON.

Process regression supports -QuestionCount 20/30 and compares question count,
all four rounds, final scores, winners and aggregate statistics. Physical Android
helper supports the same long fixture and final-stat comparison; retains existing
app-private debug argument mechanism and cleanup. A phone-asleep attempt failed
to initialize graphics; logs preserved in artifacts/phase06-android-20-asleep.
After the user woke/unlocked it, the physical 20-question LAN run passed:
revision 104, Host 19941 / Phone 19685, instance
3f4bd7d8-2c69-4bc6-85b8-b94ed8d2339d. Both peers agreed on winner and all final
aggregates; phone logs cover rounds 1–4 and 20 distinct questions. Final screenshot
inspected: readable scores/stats and touch-sized controls. The earlier "active"
capture caught reveal because the accelerated bot loop advanced during capture.
No runtime errors observed. Private debug arguments removed and normal startup
restored. Automated physical runtime, not a human touch-play claim. No screen
lock was bypassed. Evidence: artifacts/phase06-android-20/.

Verification results are recorded in harness/build-log.md. No new dependencies,
services, signing changes, discovery, reconnect, cards or missions in this phase.

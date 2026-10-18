# Phase 08 — strategy mechanics

Approved phase only, starting from pushed Phase 07 commit f6fe343 on main.
User authorized commit/push after completion. No new dependencies, services or GitHub CI.
Stop here. Phase 09 (mixed local/LAN and teams) needs separate user approval.

## Implementation and decisions

- Core/Game/StrategySession owns confidence deltas, streak/meter/hand, approved
  card state, five mission conditions and one-time bonuses. FullMatch coordinates
  activation windows, connected actors/targets, mission-safe category swaps,
  ranking and sudden-death exclusion. GameSession uses personal host deadlines,
  preserved receipt confidence, score-floor deductions and atomic transfers.
  QuestionDeck supports no-repeat, mission-safe swaps. No Godot dependency.
- Exact balance is recorded in GAME_DESIGN's Phase 08 table. x2 wrong -250,
  x3 wrong -500, totals floor 0; streak 3 +10%, 5 +15%, total positive cap x6.
  Meter 100; correct gains 20+5*difficulty, plus10 at streak5+. Hand limit2,
  empty initially, consume thresholds even when full; streak7 grants if room.
- Double Points affects one normal question; 50/50 hides two wrong options
  privately; Extra Time adds5 personal seconds before the original deadline-3s
  cutoff, once/question, without extra time bonus. Category Swap accepts one
  global change per selection during recap and offers up to3 feasible alternate
  categories. It preserves remaining mission opportunities/no-repeat behavior.
- Optional Steal is OFF by default. Shield/Steal are absent from that default
  pool; enabling aggressive cards adds both. Steal transfers min(100,victim
  total) in recap; connected distinct target, each victim once globally/match,
  including shield-blocked attempts. Shield lasts until one attack or game end.
- Assign only approved feasible Historian/HotStreak/Gambler/Speedster/Generalist
  missions from the actual selected normal plan/settings; none in one-question
  preview. Tied fastest correct host receipt counts for Speedster. Completed
  missions award500 once before normal ranking. No strategy during sudden death.
- Infrastructure/Networking adds protocol5/app0.5.0 with strict compatibility
  rejection of1–4. MatchSnapshot is personalized per transport-bound player;
  never broadcast the host's hand/mission. ActivateCard supplies only instance,
  owned card ID and optional target/category. Correlated CardResult and existing
  request cache provide duplicate-safe acceptance, timing and consumption.
  Client presentation validates/copies bounded private/final views and clears
  pending cards on a new question. Confidence deductions/Steal may reduce totals
  after reveal; base-only monotonic validation remains.
- Encoded question text/answers/explanation budget decreased10000 ->7000 bytes
  after a new eight-player regression observed16975 bytes with the former bound.
  The16KiB packet maximum is preserved; tests include long Greek names/content,
  long category ID, two cards, full mission details and final statistics. No
  content was removed/approved. Existing reviewed Greek question still validates.
- Godot StrategyPanel is composable owner-only presentation, with confidence,
  meter/streak, effects, cards/target/category controls and mission progress.
  Host shared-screen panel starts collapsed; client can hide their panel.
  MatchPanel uses the personal timer, hidden choices and final mission/card/
  confidence results. Lobby toggles strategy and aggressive cards. Greek and
  English localization included; privacy button wraps on narrow layouts.
  Base/inactive/tie mode always submits Safe even after a prior x3 selection.
- MatchProcessProbe adds opt-in strategy/seeded synthetic test behavior and card
  receipts/final evidence. New AndroidHost switch in test-android-match supports
  the reversed physical-host check. Normal menu never enables bot flags.

## Observed verification, 2026-10-18

- scripts/build.ps1: clean, zero warnings/errors. Canonical reviewed pack passes.
- scripts/test.ps1 -IncludeGodot: 232 Core +88 Infrastructure +6 runtime GdUnit
  =326 passed; zero failed/skipped. Includes deterministic strategy replay,
  each card/mission, cap/floor/deadline boundaries, ownership/privacy, duplicate
  receipt handling, negative deltas, malformed snapshots, full wire matches,
  eight-player packet size and real strategy control rendering/base-mode guard.
  Logs: artifacts/phase08-build.log, phase08-tests-final.log.
- Source test-network-match -QuestionCount30 -Strategy -Steal -Capture passed:
  all six cards actually accepted, all peers agreed on winner/stats/strategy
  final; revision204, Host110031/Anna101639/Maria0.
- Packaged same30-question check passed: revision207,
  Host110031/Anna102132/Maria0. All six cards used successfully. Screenshot
  checked Greek narrow client layout, personal mission/meter/ExtraTime notice,
  and final results. Default pool packaged20 also passed: revision141,
  Host75731/Anna67828/Maria0, all four non-aggressive card kinds used.
  Evidence: artifacts/phase08-network-30-steal*, phase08-network-20-packaged/.
- Packaged base preview passed (Host994/Anna993/Maria0). Packaged discovery/PIN
  regression passed actual UDP broadcast/custom port, wrong/missing/correct PIN,
  rate limits/manual IP, fresh rejoin, started metadata, host exit and graceful
  match departure. Logs: phase08-base-packaged.log, phase08-discovery-packaged.log.
- Windows/Android debug exports and APK signature verification succeeded. Known
  Godot EditorSettings shutdown_adb_on_exit teardown diagnostic retained; no new
  export errors. Android install Success/normal launcher Status:ok observed.
- Physical Android15/model23013PC75G Wi-Fi192.168.68.106 and packaged Windows
  Ethernet192.168.68.105 completed actual20-question LAN matches both roles:
  Windows host/aggressive: rev116 Host68208/Phone72012; Android host/aggressive:
  rev116 Phone68211/Windows-player Host72023; final default Windows host run:
  rev122 Host68105/Phone74640. All matched final scores, winner, response stats,
  mission bonuses and confidence/card results on both devices. Default phone
  used9 cards, both completed a feasible mission. Screenshots inspected including
  responsive controls, readable final mission/bonus/card/success percentages.
  Evidence: artifacts/phase08-android-20*, phase08-android-*-runtime.log.
- One extra default phone run was interrupted by mistakenly overlapping the
  reverse-host setup just before its final receipt; this was orchestration error,
  not a gameplay pass. Original logs preserved in
  artifacts/phase08-android-default-interrupted/. Isolated repeat passed above.
- No ADB forward/reverse tunnel, touch injection, lock bypass, firewall/permission
  or device settings changes. Helpers removed private test arguments/screenshots,
  stopped Windows peers and restored the normal Android app. run-as ls confirmed
  no argument fixture. These are automated physical playtests, not human touch
  acceptance. Root startup smoke and diff whitespace check passed.

## Limits and follow-up

Production has only one human-reviewed Greek question; long tests use explicitly
labeled synthetic debug fixtures, never release-pack editorial approval. More
reviewed content is still required for normal10/20/30-question play. Balance has
deterministic/runtime coverage but still needs later human playtesting. Functional
plain UI remains until Phase10 art/visual direction. No team/mixed-local work,
safe match resumption or host migration was added. Existing Godot teardown
diagnostic remains known. Generated lockfile platform churn is restored only;
new localization resources/StrategyPanel UID are intentional. No blocking issue
known within this phase. Commit/push authorized after verification.

# Observed match evidence

## Phase 08 — strategy, 2026-10-18

326 tests passed (232 Core, 88 Infrastructure, 6 Godot runtime). Source and
packaged 30-question Windows host/two-client strategy matches used all six cards
successfully with identical authoritative final scores, mission bonuses and
strategy stats. Packaged 20-question default pool used all four enabled cards;
base preview and discovery/PIN/departure regressions also passed. Protocol is 5.

Windows/Android exports, APK signature verification and physical install/launch
passed. Actual LAN 20-question runs passed with both devices hosting:

| Host / rules | Observed final |
|---|---|
| Windows / Steal enabled | revision116; Host68208 / Phone72012 |
| Android / Steal enabled | revision116; Phone68211 / Windows player Host72023 |
| Windows / default strategy | revision122; Host68105 / Phone74640 |

Final scores, winner, response stats, missions/bonuses, cards used and confidence
results agreed across devices. In the default run both players completed their
feasible missions and used nine cards each. Rendered narrow Greek client and
physical Android active/final screens were inspected; no runtime errors observed.
Private fixtures were removed, normal app restored and Windows peers stopped.
One overlapping extra test interrupted a phone run; isolated repeat passed and
the interrupted evidence is retained rather than counted as a pass.

Evidence: artifacts/phase08-network*, phase08-android*, phase08-tests-final.log,
phase08-export-*.log. Full decisions/commands are in
[Phase 08 context](../harness/context/phase-08-strategy-mechanics-context.md).
Automated physical runs used labeled synthetic questions; human touch/balance
acceptance and more reviewed content remain later work. No network tunneling,
touch injection or device/firewall settings changes. Phase 09 not started.

## Phase 06 — full loop, 2026-10-18

275 automated tests passed (208 Core, 62 Infrastructure, 5 Godot). Source
20-question and packaged/rendered 30-question host/two-client runs completed all
four rounds with distinct questions and identical final scores, winner and stats.
Packaged timeout/lobby regressions also passed; runtime errors were clean after
fixing simultaneous-disconnect sends. Windows/Android exports and APK signature
verification passed. No new dependencies; protocol is now 3.

After the user woke/unlocked the phone, this command passed over actual LAN:

```powershell
./scripts/test-android-match.ps1 -HostAddress 192.168.68.105 -QuestionCount 20
```

The physical phone observed 20 distinct questions and rounds 1–4. Host and phone
agreed on revision 104, instance 3f4bd7d8-2c69-4bc6-85b8-b94ed8d2339d,
Host 19941 / Phone 19685, winner Host, and all final aggregates. Each player had
20 correct, zero wrong/unanswered, best streak 20; host average 0.11s and phone
0.63s as rendered. Final screenshot inspected: readable scores/stats and large
buttons. No app runtime errors. Debug argument removal and normal startup restored.
Evidence: artifacts/phase06-android-20/. Earlier asleep-phone failure remains
under phase06-android-20-asleep; no device lock was bypassed.

These are automated physical runtime observations, not human touch-play claims.
Long matches use explicitly labeled synthetic debug fixtures; production still
has one reviewed question and requires more reviewed content for long matches.
Phase 06 remains local/uncommitted; Phase 07 has not started.

## Phase 04 — historical observed match evidence

2026-10-18, Europe/Athens. Windows packaged host; physical Android 15 phone
(model 23013PC75G). Host Ethernet 192.168.68.105, phone Wi-Fi 192.168.68.106.
UDP 17783 over actual LAN. USB/ADB used only for install, app-private debug test
arguments, launch/logs/screenshots. No ADB network forwarding/reverse tunnel,
input injection, firewall changes or device-setting changes were used.

## Automated local and export checks

- Full solution restore/build: zero warnings/errors.
- Core 195 + Infrastructure/config 31 + Godot scene 4 tests passed (230 total),
  none failed/skipped. Production rebuild passed. Existing tests preserved.
- Source host/two-client match and timeout match passed all phases with identical
  final revision/question/scores. Packaged Windows variants also passed, including
  explicit wrong versus unanswered (`answer=none`) results and repeated answers.
- Existing lobby and spike process regressions passed; root startup smoke passed.
- Windows and Android debug exports produced. Final APK installed successfully,
  launcher Status: ok; APK signature verifies. No new dependencies/permissions.

## Physical Windows/Android outcomes

`scripts/test-android-match.ps1 -HostAddress 192.168.68.105`, then `-Wrong` and
`-Unanswered` each passed. The helper compares final trace values from both real
processes and requires each intermediate phase on the phone. Script removes its
debug fixture in finally and restores normal app startup; absence was checked.

| Physical case | Question instance | Host | Phone | Final revision |
| --- | --- | --- | --- | --- |
| Correct phone answer | 1936bf1d-a1a9-4893-9104-587da38b8cb4 | 876 | 849 | 6 |
| Wrong phone answer | 770f0cac-4bd0-4b57-b219-fd927c9584ea | 876 | 0 | 6 |
| Phone unanswered at deadline | 675440bf-c050-4e1e-b462-2ca7c0f322ab | 876 | 0 | 6 |

Correct-case excerpts from the physical phone (local time):

```text
00:20:48.570 MATCH SNAPSHOT revision=1 phase=QuestionActive ... scores=Host:0|Phone:0
00:20:54.583 MATCH RECEIPT reason=None
00:20:54.584 MATCH SNAPSHOT revision=3 phase=QuestionLocked ... scores=Host:0|Phone:0
00:20:54.604 MATCH SNAPSHOT revision=4 phase=AnswerReveal ... scores=Host:876|Phone:849
00:20:55.638 MATCH SNAPSHOT revision=5 phase=Scoreboard ... scores=Host:876|Phone:849
00:20:56.614 MATCH SNAPSHOT revision=6 phase=GameOver ... scores=Host:876|Phone:849
```

The packaged Windows host logged the exact same final instance/revision/totals.
Wrong-case phone result: `MATCH RESULT player=Phone answer=3 points=0`.
Timeout-case phone result: `MATCH RESULT player=Phone answer=none points=0`.
All active/locked public snapshots had zero totals and no reveal; wire tests
assert absence of correctness/explanation/result flags before reveal and in ack.

## Visual/runtime inspection and limits

Inspected actual phone active and settled final screenshots at 3200x1440 plus
Windows host final capture at 1152x720. Four touch-sized answer buttons, timer,
Greek question/answers, explanation and matching scores rendered. Phone system
locale selected English UI; host was Greek. Final phone screenshots wait for
Android layout to draw before capture. Scroll container handles shorter windows.

Raw evidence is ignored under artifacts/phase04-android/, phase04-android-wrong/,
phase04-android-timeout/ and phase04-network*; both export folders retain logs.
No game/network runtime errors observed; established editor/export-only
shutdown_adb_on_exit teardown diagnostic remains documented and visible in logs.

This is automated execution on one real phone/LAN, not human touch-play acceptance,
multiple Android clients or a broad router/device matrix. The bot knows the tiny
fixture for testing and never drives ordinary UI navigation. Only one-question
Safe x1 gameplay is claimed; no packs/full game/strategy/reconnect/teams.

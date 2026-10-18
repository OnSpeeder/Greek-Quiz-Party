# Playable basic game loop

Open the LAN lobby, create/join by IP, and mark everyone ready. The host starts
the round. Host and phones receive the same question and four shuffled choices.
Choose one answer; controls lock while its host confirmation arrives. Once all
eligible players answer or the configured deadline passes, the host reveals the answer,
explanation and authoritative scores. The host opens the scoreboard, continues
questions and round recaps, then final results/statistics. Back returns to the menu and closes the connection; create a new room
to play again.

The host chooses length (10/20/30), timer (10/20/30 seconds) and categories before
Start. Selection mixes category/difficulty buckets without repeats. Four rounds
use base/time scoring; tied leaders enter sudden death with correctness then
fastest host receipt deciding the winner. If unique content runs out during a
tie, results explicitly show shared first place. Stats count eligible questions,
including sudden death, with correct/wrong/unanswered, accuracy, average accepted
response time and best streak; sudden-death answers do not change regular totals.

The canonical Greek pack still has one human-approved question, so normal play
defaults to an explicit one-question preview. Longer starts fail visibly until
enough reviewed questions exist in selected categories. No content repeats to
fill a requested length. Strategy is enabled by default and can be disabled by
the host. Safe wrong answers and unanswered questions receive zero; confidence
bets can deduct points down to a zero total. English system locale uses English UI
with Greek fixture content; Greek localization is also provided. Plain visuals
remain intentional until the art/polish phase.

## Local verification

```powershell
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
./scripts/test-network-match.ps1
./scripts/test-network-match.ps1 -QuestionCount 20
./scripts/test-network-match.ps1 -TimeoutCase -Port 17782
./scripts/export.ps1 -Platform Windows
./scripts/test-network-match.ps1 -Packaged
./scripts/test-network-match.ps1 -Packaged -QuestionCount 30
./scripts/test-network-match.ps1 -Packaged -TimeoutCase -Port 17782
./scripts/test-network-lobby.ps1
./scripts/test-network-spike.ps1
./scripts/smoke.ps1
```

Production protocol is now 6, intentionally incompatible with versions 1–5.
The old lobby-only regression opts out of starting a match; normal menu Start
always enters gameplay. This preserves the lobby checks without skipping tests.

## Actual Android hardware regression

After Android export/install and a single authorized device connected:

```powershell
./scripts/export.ps1 -Platform Android
./scripts/android-install.ps1
./scripts/test-android-match.ps1 -HostAddress <actual-Windows-LAN-IPv4>
./scripts/test-android-match.ps1 -HostAddress <actual-Windows-LAN-IPv4> -QuestionCount 20
./scripts/test-android-match.ps1 -HostAddress <actual-Windows-LAN-IPv4> -Wrong
./scripts/test-android-match.ps1 -HostAddress <actual-Windows-LAN-IPv4> -Unanswered
```

The helper runs a packaged Windows host and the physical Android app over LAN.
ADB installs, launches, observes logs/captures and writes an opt-in debug-only
app-private argument fixture. It does not inject touch input, change device
settings or forward/reverse network ports. Automated bots know this tiny fixture's
answer text solely to verify correctness and host scoring; the ordinary UI never
uses that bot. This is physical runtime verification, not a human touch-play test.

Android's exported launcher strips arbitrary intent command-line extras. Debug
builds may therefore read `user://phase04-test-args.json` (<=4096 bytes, <=12 bounded
--match-* arguments). Release builds never read this fixture. It is not packaged
content or a settings feature. The script removes it in finally, clears its own
device screenshots, stops its host, and relaunches the normal app. No credentials,
signing settings or persistent preferences change.

Opt-in CLI flags: --match-host/--match-join=IP, --match-name=Name,
--match-port=17781, --match-auto, --match-players=2, --match-delay=seconds,
--match-wrong/--match-unanswered, --match-keep-open, --match-capture=PATH,
--match-capture-phase=QuestionActive (default GameOver). Pass after engine `--`.
Normal menu navigation selects none of these flags.

`--match-fixture=20` (also 10/30) enables labeled synthetic questions only in a
debug build; `--match-fast` shortens bot interstitials. These bypass editorial
content solely for long-loop regression. They add no reviewed pack entries and
are unavailable in release builds. Normal host loading still validates JSON.

See [observed hardware evidence](MATCH_EVIDENCE.md) and NETWORK_PROTOCOL.md.

## Strategy controls

Enable/disable strategy in the host lobby. Optional Steal also enables Shield and
starts off. Before answering select x1/x2/x3; the label states the wrong-answer
penalty. Confirmation locks the answer and confidence. Total score never goes
below zero; correct streaks add capped bonuses.

The personal panel shows your streak, Chaos Meter, two-card hand, active effects
and private mission progress. It starts collapsed on the host's shared screen.
Each card explains its timing; activate before submitting or during recap as
specified. Extra Time changes only your displayed timer. Category Swap offers
host-approved alternatives; Steal offers connected opponents and may reject an
already targeted victim. Receipt status explains accepted effects/rejections.
Only owning players receive private cards and missions. GameOver reveals every
mission outcome/bonus and confidence success/card-use statistics.

Normal navigation uses validated reviewed content. --match-strategy,
--match-steal and --match-seed=N are opt-in playtest flags; -Strategy/-Steal on the
network/Android scripts select them. These fixtures add no reviewed questions.

## Shared devices and teams

Create a room, then use Add player on this device for each extra local person.
Each has a separate ready button; the room still has a total limit of eight.
Removing an extra player in lobby discards that seat; Disconnect leaves with all
players from that device. Two or more players on just the host can play without
any remote joins.

Enable Team Mode in the host's roster editor and assign Team A/B. Both teams must
have players. Scores sum individual scores, including mission bonuses and
penalties; unequal sizes are allowed. Final results show team totals/winning team
as well as individual stats. Sudden death uses the fastest correct host receipt
among tied-team members, without changing normal totals.

When several players share a device, give it to the next person and tap Play as
their name. Personal controls stay behind the handoff curtain until claimed.
Submitting hides them; switching owners resets confidence to x1 and hides prior
personal controls. Select a player again during recap to use their recap cards.
The shared question timer keeps running; choose a longer timer (up to 60 seconds)
for larger shared groups. Phones with one player retain their normal controls.

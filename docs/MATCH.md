# One-question playable match

Open the LAN lobby, create/join by IP, and mark everyone ready. The host starts
the round. Host and phones receive the same question and four shuffled choices.
Choose one answer; controls lock while its host confirmation arrives. Once all
players answer or the 20-second deadline passes, the host reveals the answer,
explanation and authoritative scores. The host opens the scoreboard and final
results. Back returns to the menu and closes the connection; create a new room
to play again.

Phase 05 loads the first reviewed question from the canonical Greek JSON pack;
the initial pack contains one human-approved question. This is not a full game
mode. Safe x1 base/time scoring is implemented; multiple questions, confidence
multipliers, strategy and tie-breakers are later phases.
Wrong/unanswered players receive zero. English system locale uses English UI
with Greek fixture content; Greek localization is also provided. Plain visuals
remain intentional until the art/polish phase.

## Local verification

```powershell
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
./scripts/test-network-match.ps1
./scripts/test-network-match.ps1 -TimeoutCase -Port 17782
./scripts/export.ps1 -Platform Windows
./scripts/test-network-match.ps1 -Packaged
./scripts/test-network-match.ps1 -Packaged -TimeoutCase -Port 17782
./scripts/test-network-lobby.ps1
./scripts/test-network-spike.ps1
./scripts/smoke.ps1
```

Production protocol is now 2, intentionally incompatible with Phase 03's v1.
The old lobby-only regression opts out of starting a match; normal menu Start
always enters gameplay. This preserves the lobby checks without skipping tests.

## Actual Android hardware regression

After Android export/install and a single authorized device connected:

```powershell
./scripts/export.ps1 -Platform Android
./scripts/android-install.ps1
./scripts/test-android-match.ps1 -HostAddress <actual-Windows-LAN-IPv4>
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

See [observed hardware evidence](MATCH_EVIDENCE.md) and NETWORK_PROTOCOL.md.

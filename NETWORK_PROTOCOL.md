# NETWORK_PROTOCOL.md

## 1. Goals

- Reliable LAN party experience.
- Host-authoritative rules.
- No Internet dependency.
- Clear version compatibility.
- Tolerate malformed clients without crashing.
- Support Windows host and Android clients.

## 2. Transport split

### Gameplay transport

Use Godot High-Level Multiplayer with `ENetMultiplayerPeer` where suitable.

Default port proposal: **UDP 7777**.

### Discovery transport

Use separate UDP discovery channel.

Default port proposal: **UDP 7778**.

Ports must be configurable internally and may be user-configurable later.

## 3. Authority model

Host owns:

- game configuration,
- player roster,
- question order,
- answer deadline,
- correctness,
- score,
- streak,
- card inventory and effects,
- mission identity/progress,
- game state,
- authoritative random numbers.

Client may request/submit:

- join,
- ready toggle,
- display-name/avatar choice,
- answer,
- confidence choice,
- card activation,
- reconnect.

Client input is a request, never truth.

## 4. Protocol version

Current production version (match reconnection revision):

`ProtocolVersion = 12`

See the v12 contract below. Earlier phase contracts are retained as history.

Phase 03 used version 1; Phases 04–05 used version 2; Phase 06 used version 3.
Version 4 adds the optional PIN field to ClientHello and LAN discovery. Strict
unknown-field handling makes this intentionally incompatible; versions 1/2/3
are rejected at hello and ignored by discovery. The
disposable probe stays version 1.

Version is included in hello/discovery and preferably packet envelope.

Incompatible major protocol versions must not enter a match.

## 5. Message envelope

Logical DTO fields:

```text
ProtocolVersion
MessageType
MessageId
SessionId
SenderPlayerId? / SenderConnectionId derived server-side when possible
CorrelationId?
Payload
```

Do not trust a client-supplied sender ID if transport identity already determines sender.

## 6. Handshake

### ClientHello

Contains:

- protocol version,
- app version,
- desired display name,
- optional room PIN,
- reconnect token if reconnecting,
- platform label for diagnostics only.

### ServerHello

Contains:

- accepted/rejected,
- rejection reason,
- session ID,
- assigned player ID,
- lobby snapshot,
- reconnect token if used,
- server time reference if required.

## 7. Lobby messages

- `LobbySnapshot`
- `PlayerJoined`
- `PlayerLeft`
- `PlayerReadyChanged`
- `TeamChanged`
- `GameConfigurationChanged`
- `KickPlayer`
- `GameStarting`

Prefer snapshots after important mutations to simplify recovery from missed incremental UI events.

## 8. Question messages

### QuestionStarted — public payload

Send only what players may know:

- QuestionInstanceId
- question text or localization/content payload
- answers in display order
- category
- difficulty if shown
- deadline/server start time
- allowed mechanic state

**Do not send `CorrectAnswerIndex` before reveal.**

### SubmitAnswer

Client requests:

- QuestionInstanceId
- selected answer index
- selected Confidence level
- client request ID

Server validates:

1. sender maps to eligible player,
2. correct game state,
3. matching active question,
4. player has not already submitted,
5. answer index in range,
6. confidence is legal,
7. host receive time <= deadline,
8. request not previously processed.

### AnswerAccepted

Private acknowledgement to sender. Does not reveal correctness.

### QuestionClosed

Host declares answer window closed.

### AnswerReveal

Contains:

- correct answer index,
- explanation,
- source if displayed,
- per-player/public result summary according to presentation rules.

## 9. Cards

### ActivateCard request

Fields:

- CardInstanceId
- activation context/question ID
- target player/team if required
- RequestId

Host validates ownership, timing, target and stacking rules.

### CardResolved

Authoritative result, with public/private visibility rules.

## 10. Timers

Do not broadcast `10, 9, 8...` every second.

Host sends absolute/relative deadline info. Client animates locally.

Answer validity uses host receive time.

Periodic lightweight ping/pong may estimate offset/latency for UI only.

## 11. Discovery protocol

Client broadcasts a discovery request on UDP 7778.

Example logical request:

```json
{
  "Type": "quiz-discover",
  "Protocol": 4,
  "Nonce": "00000000-0000-0000-0000-000000000001"
}
```

Host responds directly to requester with bounded metadata:

```json
{
  "Type": "quiz-host",
  "Protocol": 4,
  "Nonce": "00000000-0000-0000-0000-000000000001",
  "SessionId": "00000000-0000-0000-0000-000000000002",
  "RoomName": "Fil's Party",
  "GamePort": 7777,
  "Players": 3,
  "MaxPlayers": 8,
  "RequiresPin": true,
  "AppVersion": "0.4.0",
  "State": "Lobby"
}
```

Do not trust an advertised address blindly if source endpoint provides the correct address.

## 12. Manual IP fallback

The transport retains manual IPv4/hostname joining and its regression probes. By explicit user decision (2026-10-25), the normal participation screen exposes discovery only; manual IP can be reintroduced without rebuilding the transport.

Provide clear errors:

- host not reachable,
- room full,
- wrong PIN,
- incompatible version,
- game already started,
- connection timed out.

## 13. Room PIN

PIN is an admission convenience, not strong cryptographic security.

- 4–6 digits recommended.
- Rate-limit repeated wrong attempts if practical.
- Do not claim PIN encrypts traffic.

## 14. Reconnect

During an active match the host reserves all seats on a disconnected device for
the life of the match, and the client retries until it reconnects or the user leaves.
The host pauses game time immediately. All connected seats may vote to resume, or
the host may override. If all disconnected seats return while paused, the host
begins a five-second countdown and then resumes. A player who returns after an
override rejoins the current state without pausing it again. A disconnected seat
does not block questions once the host or connected players have resumed, including
untimed questions; an unanswered disconnected seat is recorded as wrong.
Successful reclaim binds the original players and local slots to the new connection
and sends fresh per-seat authoritative snapshots. The host retains accepted answers
and rejects second submissions. Pause duration does not consume answer time.

Admission supplies a random 256-bit token privately to each device. Reconnect
requires that token, the session ID, a currently reserved disconnected device,
and a compatible protocol. Tokens stay in memory, are not included in public
snapshots or logs, and are invalid after match end or host shutdown.
They are bearer credentials on an unencrypted trusted LAN, not an Internet
authentication mechanism. Intentional host closure sends a reliable notice before
closing; clients return home. After a silent host failure the client keeps trying
until the player leaves. Reconnection cannot migrate or recreate a stopped host.

## 15. Idempotency

Every state-changing client request has a `RequestId`.

Host remembers recent processed IDs per connection/player for the match or a bounded window. Duplicate request returns same logical result or is ignored safely.

## 16. Packet validation

Bound:

- player-name length,
- room-name length,
- array sizes,
- string payload lengths,
- indices,
- enum values,
- message frequency.

Disconnect clients that repeatedly violate protocol in an obviously abusive way.

## 17. Network test matrix

Required before release:

- Windows host + Windows client.
- Windows host + one Android client.
- Windows host + at least two Android clients.
- 4+ simultaneous clients if devices/emulators available.
- Wi-Fi disconnect/reconnect.
- Host exits unexpectedly.
- Client exits during question.
- Late packet.
- Duplicate submit.
- Invalid answer index.
- Wrong protocol version.
- Discovery unavailable + manual IP succeeds.

## Phase 07 implemented LAN admission/disconnect (production v4)

Gameplay transport/RPC paths and Phase 06 match DTOs remain unchanged. Envelope
version 4/app 0.4.0 requires matching builds. ClientHello adds `Pin` (empty by
default); null, oversized, non-ASCII/non-digit or 1–3/7+ digit PINs are malformed.
Host optionally sets a 4–6 ASCII-digit PIN or leaves it empty. ServerHello remains
the correlated admission receipt. No PIN, hash or token is sent in snapshots,
discovery or diagnostic logs; the admission request itself is not encrypted.

`RoomAdmission` hashes the configured PIN in memory and compares fixed-size
hashes. Five wrong/missing guesses per source IP per 30-second monotonic window
block further attempts (`PinRateLimited`, including correct PIN) until reset;
100 failures globally bound guesses/state across new source addresses. The
ENet adapter supplies actual remote address to LobbyHost.Handle; never use a
packet field or connection ID as the address. Disconnecting does not reset this
gate. Exact duplicate request receipts do not count guesses twice. Other existing
message/rate/cache bounds remain. Wrong/missing valid-format PIN yields WrongPin.
Full/started/version checks reject before admission, and a PIN is a LAN admission
convenience, not encryption or a substitute for a trusted network.

Discovery uses a separate IPv4 PacketPeerUdp socket, host bound to UDP 7778,
browser bound to an ephemeral port. Broadcast to 255.255.255.255 once per second
for five seconds, then stop probing; manual-IP joining remains independent.
Hosts unicast replies to the observed source endpoint with current lobby metadata.
Host and scan ports are internally overridable; joining a row uses its advertised
game port. Discovery bind/send failure does not stop ENet hosting/manual joining.

The exact JSON fields above are required, case sensitive, with no extra/duplicate
fields. Limit 1024 bytes, strict UTF-8/escaped strings, JSON depth 4, matching
protocol, nonempty GUID nonce/session, valid room name (32), appVersion length
1–32, port 1024–65535, players 1–8, maxPlayers exactly 8, state Lobby/GameStarting.
Host replies at most four per source IP/second and 32 total/second; poll consumes
at most 16 packets per 100ms tick. No unbounded per-source state or packet work.

Browser accepts replies only for its active five-second nonce. Use the observed
IPv4 source, never a payload-provided address. Catalog holds at most 32 room/
source pairs, deduplicates updates, expires entries six seconds after last seen,
and clears on refresh/stop/scene exit. Incompatible, malformed or unsolicited
messages are ignored. Full/started entries are visible but disabled. Metadata is
untrusted; host handshake still validates PIN/capacity/state. No latency/ping
claim or Internet discovery is implemented.

Historical v4 graceful-disconnect policy (superseded for active matches by v11): lobby departure removes seat/readiness/cache; a new
join gets a new PlayerId and starts unready, even with the same name/address.
Once started, every re-entry is rejected GameStarted. A departed match player's
confirmed answer/score remains, and unsubmitted answers expire under the original
host deadline. MatchPanel labels departed names from authoritative lobby vs fixed
match roster. Replayed old answers cannot mutate a disconnected seat. Host loss
closes the match locally with explicit non-resumable-room guidance. No reservation,
identity reclaim, reconnect token, auto-reconnect or host migration is claimed.

Verification: DiscoveryAndAdmissionTests plus existing protocol/Core/Godot gates;
scripts/test-network-discovery.ps1 (also -Packaged -Capture) and actual hardware
scripts/test-android-discovery.ps1. See docs/LOBBY.md and its evidence/context.

## Phase 06 full-match additions (historical production v3)

All Phase 04 request types, receipt/ownership/deadline rules and RPC signatures
below are retained. MatchSnapshot additionally requires `QuestionNumber`,
`TotalQuestions`, `RoundNumber`, `IsTieBreaker`, `EligiblePlayers`, `Winners`,
`ContentExhausted`, `Statistics`. Array IDs refer to the fixed match roster.
Stats contain PlayerId, Correct, Wrong, Unanswered, BestStreak, ResponseTicks,
Responses. They are empty until GameOver. Accuracy/average formatting uses these
host aggregates; clients never calculate authoritative scoring or outcomes.
SceneMultiplayer peer relay is disabled while the lobby scene owns networking:
clients communicate only with the host, and the host sends explicit roster data.
This avoids native relay notices racing simultaneous ENet disconnects. The
adapter also verifies connected state/allocated channels before sending an RPC.

Questions advance with a new instance and increasing ordinal; normal totals carry
over while Reveal resets to null. Clients reject ordinal/phase rollback, reused
instances, roster replacement, decreasing scores and malformed/bounded progress.
Private pending/accepted input clears at the new question. An old receipt cannot
confirm a new answer, even if its exact request is replayed from the host cache.
Question deadlines span at most 60 seconds; configuration supports 10/20/30
questions (one-question preview) and category filtering. Capacity is checked
before leaving the lobby; host settings are local intents, not client commands.

Local AdvanceMatch supports Scoreboard -> next QuestionActive or RoundEnd,
RoundEnd -> next QuestionActive, and final GameOver. Four normal rounds divide
the configured question count nearly evenly. Round four uses base scoring in
this baseline; no final multiplier is specified yet. Sudden death uses only tied
leaders, new questions, unchanged regular totals and fastest correct host receipt.
Exact fastest ties continue among those players; all-wrong/unanswered continues
with the existing eligible set. Finite content exhaustion reports shared winners
and ContentExhausted instead of repeating content. No new protocol message is
needed. Safe x1 remains the only accepted confidence level.

The 16KiB envelope bound remains. Validator encoded-content budget is now 10KB
(was 12KB), reserving room for eight-player results and final statistics. The
eight-player Greek-name/near-budget content regression covers the final packet.

## Phase 04 one-question match (historical production v2)

Lobby fields and bounds below are retained, with envelope version 2 and app
version 0.2.0. Normal host Start now creates a Core OneQuestionMatch from the
server-owned lobby roster. It uses the permitted tiny Greek fixture, host-shuffled
answers and a 20-second monotonic host deadline. Lobby snapshots remain
GameStarting while separate match snapshots render the match. Keep the same ENet
peer and /root/Lobby/Transport RPC path throughout panel changes.

Additional message types:

- `SubmitAnswer`: required `QuestionInstanceId`, `AnswerIndex`, `Confidence`.
  No player ID, score or client timestamp. Only Safe 1 is accepted in this phase.
  Host captures receipt at entry to Handle before parsing and resolves player
  ownership from the actual connection. Host local input uses the same Core rule.
- `AnswerAccepted`: private correlated `Accepted`, `Reason`, `QuestionInstanceId`.
  Includes neither correctness nor points. Same exact request ID/JSON returns
  the original receipt without replacing the answer, timestamp or score.
- `MatchSnapshot`: `SessionId`, increasing `Revision`, `Phase`, `HostNowTicks`,
  `Question`, `AcceptedAnswerCount`, `Scores`, nullable `Reveal`. Domain objects
  are mapped to dedicated DTOs. Match revisions are independent of lobby revisions.
- Question: instance ID, text, four shuffled answers, category, difficulty,
  `StartedAtTicks`, `DeadlineTicks` (monotonic TimeSpan ticks, not wall-clock time).
  The client estimates a visual countdown from receipt; it never decides deadlines.
- Scores: player ID/name/host-calculated total, zero before reveal. Reveal is null
  during QuestionActive/QuestionLocked; no correct index/explanation/result flags
  appear in those packets. AnswerReveal and later include correct displayed index,
  explanation and each player's selected index (null = unanswered), correctness,
  and awarded points. No authoritative score calculation occurs on clients.
- `AdvanceMatch`: remote requests always reject NotHost. Local host advances
  AnswerReveal -> Scoreboard -> GameOver. No rematch, winner/tie-breaker logic or
  multiple-question scheduling is implemented by this slice.

All submitted answers or host time strictly past deadline locks the question.
A subsequent host poll reveals and scores once. Godot polls every 50ms after
normal network processing, but Core monotonic time and host receipts own validity
and score; no frame count/delta determines either. The existing exact-deadline
`<=` acceptance remains. A disconnected player's initial match slot remains and
expires unanswered; connected lobby membership is separate. Host exit terminates
clients visibly. Session/instance checks and initial roster prevent new/foreign
connections answering for someone else.

Clients reject wrong-session, stale/reordered/rollback match snapshots, malformed
question/rosters and premature reveal. A pending answer locks its local controls;
the correlated host receipt confirms submission without revealing correctness.
Snapshots return copies of arrays. The host remains the authority even if client
UI code is modified.

Tests: source and packaged host/two-client full/timeout matches; deterministic
Core/router privacy, invalid/stale/late/duplicate/ownership/version tests; physical
Android client against packaged Windows host over actual LAN. See docs/MATCH.md
and docs/MATCH_EVIDENCE.md for exact observed results and automation limitations.

## Phase 03 baseline production lobby v1 (historical contract)

This records the first production v1 implementation, now superseded by v2 above. The Phase 01 probe below is a
separate contract and remains accessible. No gameplay answer/card/discovery wire
messages are implemented yet; later additions require compatibility review.

### Transport and envelope

- Reliable ordered ENet RPCs on the identical `/root/Lobby/Transport` node path:
  `ClientMessage(string json)` (AnyPeer, host receives only) and
  `ServerMessage(string json)` (Authority, clients additionally require sender 1).
- Normal UDP port 7777; process regression 17778. One host participant plus up
  to seven admitted clients. Twelve total transport slots allow a bounded number
  of pending handshakes and explicit `RoomFull` rejections instead of silent failure.
- Exact case-sensitive envelope fields: `ProtocolVersion` (1), `MessageType`,
  `MessageId` (nonempty UUID), `SessionId` (UUID), `CorrelationId` (nullable UUID),
  `Payload` (JSON object). UUIDs use System.Text.Json's standard string encoding.
  Client `MessageId` serves as the logical RequestId. Replies correlate to it.
- At most 16,384 UTF-8 bytes per JSON packet (checked before parsing), depth 8,
  fixed DTOs and unknown-field rejection. No polymorphic deserialization.
- Names/room names: 1–32 UTF-16 code units, nonblank, trimmed, no control characters.
  AppVersion: 1–32 code units; informational, while ProtocolVersion gates compatibility.
  Platform: Windows/Android/Linux/macOS. Manual address: 1–253 characters without
  whitespace. Port: 1024–65535. Raw sender/connection ownership is never a payload.

### Handshake and snapshots

`ClientHello` has empty SessionId and null CorrelationId. Payload fields are
`AppVersion`, `DisplayName`, `Platform`. The host assigns a fresh PlayerId and
binds it to the actual ENet sender; the host owns connection 1 and local slot 0.
No PIN/token fields are accepted in this phase; these remain Phase 07 work.

`ServerHello` payload: `Accepted`, `Reason`, nullable `PlayerId`, nullable `Lobby`.
Success includes the assigned player and complete snapshot. Rejection includes
no player/snapshot. A client accepts only the hello correlated to its pending
request. Peers without a successful hello are disconnected after ten seconds.
Client join also has a ten-second timeout, canceled by generation on stop/rejoin.

`LobbySnapshot` payload: `SessionId`, increasing `Revision`, `RoomName`, `Phase`
(Lobby/GameStarting), `Players` (1–8). Each player has `PlayerId`, `DisplayName`,
`IsHost`, `Ready`. Exactly one host and distinct nonempty player IDs are required.
The public payload contains no connection IDs or reconnect credentials. Clients
reject wrong sessions, stale/equal revisions, malformed rosters and phase rollback.
Snapshots replace local presentation state; clients never calculate roster/start.

### Readiness, start and departure

`SetReady` payload contains required boolean `Ready`. It is a setter, not a
toggle; the host resolves the sender's own player. Only admitted connections with
the current SessionId and null CorrelationId may mutate readiness. The host's
local ready control passes the same domain rule. Host is initially ready; remote
players join unready. Identical setters do not increment the revision.

`RequestResult` payload: `Accepted`, `Reason`, correlated to the request. Clients
only consume results for their own bounded pending requests. Expected reasons
include None, IncompatibleVersion, MalformedRequest, HandshakeRequired,
WrongSession, RequestConflict, RequestLimit, AlreadyJoined, RoomFull,
GameStarted, NotHost, NotReady and UnknownConnection.

Start is local host intent. A wire `StartGame` request from a client is rejected
as NotHost. Start requires 2–8 players with everyone ready and advances the Core
lobby state once to GameStarting. A revisioned snapshot is the start notification;
Phase 03 stops there. Questions, round scheduling and the gameplay bridge belong
to Phase 04 and later. After start, new joins and readiness changes are rejected.

On client departure the host removes its lobby entry and per-connection caches
and broadcasts the new revision. Host departure closes clients with a visible
status. No seat reservation/token reclaim is claimed. GameStarting disconnect
snapshots reflect the connected roster, not future gameplay eligibility policy.

### Bounds and duplicates

Per connection: 256 retained request receipts, 32 inbound messages per monotonic
one-second window, three malformed-packet/conflicting-ID strikes. Exceeding the
rate/cache bound or strike limit requests disconnection. Duplicate messages count
towards rate limits. The same exact request ID and JSON returns the original
receipt without reapplying a mutation. Reusing an ID with changed JSON is rejected.
Caches never evict old ready requests and then reapply them; exhausting the bound
requires a new connection. Protocol mismatch requests disconnect immediately after
the rejection receipt is queued, with a short flush delay in the ENet adapter.
Invalid payloads are rejected and bounded by the same rate/cache limits; they do
not all count as malformed-packet strikes.

### Compatibility verification

`scripts/test-network-lobby.ps1` runs a real ENet host and two Windows clients:
same roster/readiness/start revision, repeated ready requests, remote-start
rejection, late join/version rejection, client cleanup, host exit and no-host
timeout and a freed transport's canceled join timer. Core and Infrastructure tests cover ownership, malformed/bounded JSON,
session checks, receipt cache/rate limits and client revision validation.
The host and clients must ship matching v1 RPC signatures and DTOs. Future optional
fields require deliberate compatibility/version review because unknown fields
are rejected. No new physical Android lobby test is claimed by these Windows tests.

## Phase 01 disposable LAN probe

The separate `LanSpike.tscn` scene uses reliable ENet RPCs on UDP 7777 (overridable
for process tests). This is a technical compatibility probe, not implementation of
the production v1 lobby/message envelope above. Its version is checked separately
as `ProbeInbox.ProtocolVersion = 1`; future production handshake implementation
must not assume these RPCs are the production protocol.

- Client `Hello(protocol, platform)`; host derives sender connection ID from RPC
  transport, bounds/validates platform, and sends `HelloResult(accepted)`.
- Only accepted connections may call `ReceiveAction(protocol, requestId)`.
  Request ID is exactly 32 hexadecimal characters representing a non-empty GUID.
  The action is implicit: a disposable test-button press; there is no score/player.
- Host returns `ActionReceipt(requestId, hostCount)` only to the submitting client.
  A duplicate returns the original count without incrementing it again.
- At most 7 clients and 256 unique actions per connection are retained. Disconnect
  removes that connection's accepted-session and duplicate cache. New connection
  IDs have no right to submit without a new hello. No reconnect/slot reclaim exists.
- Client accepts acknowledgements only from server ID 1, for its current request.
  Client cannot set host count. No answers, clocks or game RNG are exchanged.
- Join times out after ten seconds; host exit/failure is visible in the UI. Scene
  exit closes the peer. Automatic process tests have separate bounded timeouts.

Compatibility checks for this contract: valid round trip, duplicate handling,
unknown connection/invalid ID/version rejection, and wrong-version ENet client.
Godot RPC signatures and identical scene node paths must match on both platforms.

## Phase 08 implemented strategy contract (production v5)

Envelope version 5/app 0.5.0 deliberately rejects v1–4, including discovery's
embedded gameplay version. Strict unknown-field rejection, 16 KiB packet/depth 8,
ENet RPC signatures/paths, host receive timing, PIN/manual IP/discovery and the
graceful-disconnect policy remain. Peers must update together.

MatchSnapshot adds nullable Strategy (Confidence/Streaks/Cards/Missions/AllowSteal
booleans), nullable Private, and FinalStrategy (empty until GameOver). Base-only
games have null Strategy/Private and empty FinalStrategy. Rules cannot change
mid-match. **BroadcastMatch maps a separate snapshot for each transport-owned
PlayerId**; it must never broadcast the host's personalized snapshot.

Private contains only the recipient's PlayerId, Hand (0–2 Id/Kind cards),
HiddenAnswers (0 or 2 distinct indices), DeadlineTicks, Shield, DoublePoints,
Streak, Meter (0–99), nullable Mission, up to 3 SwapCategories (128 units each),
and bounded Notice. Card Kind: 0 DoublePoints, 1 FiftyFifty, 2 ExtraTime,
3 CategorySwap, 4 Shield, 5 Steal. Mission Kind: 0 Historian, 1 HotStreak, 2 Gambler,
3 Speedster, 4 Generalist, with Target/Progress/Complete. No correct answer,
foreign hand or foreign mission is included before reveal/game end.
Private deadlines range from base deadline through base+5 seconds.

SubmitAnswer accepts Confidence 1–3 only under enabled confidence rules and normal
play. A wrong answer's revealed Points may now be negative (minimum -500), while
totals remain nonnegative. Clients still enforce monotonic totals for base-only
games; strategy snapshots allow host deductions/Steal only after reveal. They
never compute authoritative scores. Base max question points 1000, strategy 6000.
Final accepted response statistics allow 65 seconds (base 60+personal 5).

ActivateCard payload: QuestionInstanceId, CardId, nullable Target, nullable
Category (max 128). No actor, kind, time, hidden indices or effect values. The host
resolves the actor from the admitted connection and the kind from that owner's
hand; validates session, current instance, connection/eligibility, phase,
answer lock, original/personal deadlines, effect stacking and target/category
rules; then consumes only accepted cards. Final category selection and 50/50
indices use host RNG. An active-match disconnect revokes future answer/card
intents while retaining the fixed score/answer roster.

CardResult is a private correlated receipt: Accepted, Reason,
QuestionInstanceId, CardId. Identical request ID/JSON returns the same cached
receipt without applying twice. Clients retain at most one pending activation;
correlation/card/question must all match. New questions clear pending card state;
old receipts cannot confirm a new card. Rejections include Disabled,
UnknownPlayer, UnknownCard, StaleQuestion, InvalidWindow, AlreadyAnswered, Late,
InvalidReceiveTime, EffectActive, InvalidTarget, AlreadyTargeted, NoEffect,
InvalidCategory, NoUpcomingQuestion, plus envelope/session/admission errors.

FinalStrategy contains PlayerId, nullable Mission, MissionBonus, CardsUsed,
ConfidentCorrect/Wrong, AllInCorrect/Wrong for each fixed-roster player, only at
GameOver. Client shape checks bound every list/index/enum/progress and return
defensive copies. The content validator's encoded text/answers/explanation budget
is now 7000 bytes (was 10000): the previous limit produced a 16975-byte eight-player
strategy final. Regression checks cover long Greek names/content, two cards,
complete missions, maximum category ID and populated final statistics while
retaining the 16 KiB bound. No signing/encryption/reconnect scope is added.

## Phase 09 implemented mixed-controller contract (production v6)

Protocol 6/app 0.6.0 deliberately rejects versions 1–5. Reliable ENet paths,
16KiB/depth8 bounds, host receipt timing, PIN/discovery/manual IP and graceful
disconnect remain. Discovery embeds the current gameplay version too.

LobbyPlayer adds opaque ControllerId, LocalSlot (0–7) and nullable TeamId (1/2).
LobbySnapshot adds TeamMode. Production controller IDs are host-generated UUIDs
for device groups, never transport connection IDs. ServerHello includes the
admitted controller ID and primary PlayerId. Client DTO defaults permit singleton
test fixtures; production always populates controller groups. The primary slot 0
cannot be removed individually. Each controller may own multiple PlayerIds.

New AddLocalPlayer contains DisplayName (same 1–32 trimmed-name rules) and required
LocalSlot 1–7. RemoveLocalPlayer contains required LocalSlot 1–7. SetReady,
SubmitAnswer and ActivateCard add LocalSlot (default 0). Host resolves the actor
by **actual source ConnectionId plus validated LocalSlot**. No client actor,
controller, score, team assignment or timestamp is accepted. Client SetTeam is
rejected NotHost; host team assignments are local validated intents. All add/
remove/team/ready changes are lobby-only and duplicate-safe.

Lobby broadcasts go once per remote connection, not once per player. Match
broadcasts send a separate MatchSnapshot per owned player with top-level
LocalSlot. Each packet contains only that player's Private view. AnswerAccepted
and CardResult echo LocalSlot and must match slot/question/correlation/card.
Client maintains at most eight MatchClientState instances; removed/replaced slots
cannot inherit old pending/private state. Owner switches preserve independent
confirmed answers and pending requests. Equal revisions for different slots are
separate views, never a reason to overwrite another actor's private data.

MatchSnapshot adds Teams (empty or two TeamId/Total/Members entries) and
WinningTeams (empty until GameOver). Membership partitions the fixed score roster
and remains immutable through the match. Team totals are host-calculated checked
sums; the client validates shapes and renders received totals. Team winners map
to all member PlayerIds in Winners. ExtraTime deadlines and 50/50 removals remain
per-player even when slots share a physical connection. Disconnect removes all
that connection's lobby slots and revokes all future match intents while keeping
fixed match scores/confirmed answers.

Receipt cache now retains up to 2048 requests/connection, with a 2 MiB encoded
request+reply byte gate (plus at most one bounded final record before refusal).
This supports eight actors' long matches without assuming one player/connection.
Old duplicate receipts are retained, never evicted and reapplied; new requests
over either bound reject RequestLimit/disconnect. 32 messages/second and malformed
strike limits remain. Tests cross 256 requests and exercise the byte gate.

The 7000-byte question-content budget is unchanged. Eight-player final packets
with team membership, two cards, full missions/Greek names/category/stats remain
within 16 KiB. No reconnect, encryption, transport identity exposure or new service.

## Participation revision — production v7 / app 0.7.0

All peers upgrade together. Versions 1–6 are rejected/ignored by handshake and
discovery. Existing reliable RPC paths, 16 KiB/depth8 bounds, receipt caching,
rate/PIN throttling, source ConnectionId and host receipt clocks remain.

### Preflight without admission

`CheckRoom` carries AppVersion (1–32), Platform (existing allowlist), and Pin
(empty or 4–6 ASCII digits), with the discovered SessionId. Wrong sessions,
started/full rooms and invalid/throttled PINs reject. Success authorizes only that
actual transport connection for two minutes on the injected host clock. It creates
no PlayerId, controller, roster mutation, character reservation or joined seat.
The connection cap remains 12; unadmitted peers time out. PIN is never broadcast.

`RoomAccessResult`, correlated to CheckRoom/RoomAvailability, carries Accepted,
Reason, Revision and TakenCharacters (0–8 distinct indices 0–7). A failed preflight
returns no occupied-character list. No correct answers/private gameplay are sent.
`RoomAvailability` has an empty payload, the same SessionId and requires unexpired
connection-bound authorization. It does not extend authorization. UI polls at
most once per second while choosing identity and not submitting a join.

### Final admission and uniqueness

ClientHello adds nullable CharacterId (0–7) and UsePreflight (default false).
UsePreflight=true requires the same connection's unexpired authorization; no PIN
is resent. Direct transport/probe joins retain the ordinary PIN gate. Omitted
character means host assigns a free character for retained direct/probe callers;
normal UI always supplies an explicit choice. This is a supported v7 behavior,
not wire compatibility with old versions.

Core assigns/validates characters atomically with roster mutation on the host
receive loop. Two final requests for one character produce one admission and one
CharacterTaken rejection. Rejected ServerHello includes refreshed TakenCharacters
only for an authorized preflight peer. That client stays connected, retains its
name and retries a fresh request with a different available character. Duplicate
requests return their original receipt and never create another player. Expired
access, full/start/disconnect errors return the UI to room selection.

LobbyPlayer and MatchScore add nullable CharacterId. Production host snapshots
always populate it; nullable supports explicitly synthetic/retained API fixtures.
Clients validate range and uniqueness when present; match identity cannot change
between snapshots. Match retains the roster's IDs for departed-player results.
AddLocalPlayer also accepts a character; host/local slots use the same Core gate.
Characters release on lobby departure/local removal, never by client speculation.

## Protocol v8 — lobby setup scoring compatibility (2026-10-25)

Current protocol: 8; app version: 0.8.0. Reject earlier versions at admission and
discovery as usual. DTO shape is unchanged. The host now starts unready. Match
setup filters questions by host-selected difficulty levels as well as categories;
card/mission pools stay host-owned and preserve private assignment routing.

Approved difficulty bands multiply positive base/time points by 1 / 1.5 / 2 before
strategy. Client reveal validation permits up to 2,000 base or 12,000 strategy points
per answer, with existing negative penalties unchanged. The client only validates
bounds and renders authoritative totals. v7's 1,000/6,000 reveal bounds would reject
valid v8 results, requiring the version increment despite unchanged payload shape.
Manual-IP joining and duplicate-safe ready/answer/card routing remain supported.

## Protocol v9 — optional host player and configurable capacity (2026-10-25)

Protocol 9 / app 0.9.0 adds `MaxPlayers` (2–8) and `HostPlays` to lobby snapshots.
The host identity is its authenticated transport connection, independent of a
roster seat. `HostPlays=false` means zero IsHost players; `true` means exactly one.
Empty waiting rooms are valid when the host does not play. Clients validate these
invariants and cannot mutate these room-creation fields after admission.
Discovery announces actual participant count (0–MaxPlayers) and the selected cap;
admission/preflight/local additions all enforce that cap. Version 8 is rejected,
since it requires a roster host, at least one advertised player and capacity 8.

The non-playing host receives a public match projection, never another player's
private hand, hidden options, mission or personal deadline. It cannot submit an
answer/card with connection1/slot0 when no such player exists. Remote broadcasts
retain one private projection per authenticated owned player. Existing strict
bounds, duplicate handling and host receive-time deadlines remain unchanged.

## Protocol v10 / app 0.10.0 — match-flow extension (2026-10-25)

All peers upgrade together; admission and discovery reject v9 and earlier.
MatchSnapshot adds bounded distinct AnsweredPlayers, ContinueVotes and EndVotes
GUID arrays (0–8 roster IDs), without answer choices before Reveal. AnsweredPlayers
length equals AcceptedAnswerCount. Continue votes exist only at AnswerReveal,
Scoreboard or RoundEnd; end votes only at unlimited Scoreboard.

MatchVote carries QuestionInstanceId, Phase, EndGame and LocalSlot (0–7). Host
resolves the seat through authenticated connection ownership, requires the exact
current instance/phase and an allowed action, and deduplicates each player's vote.
Request receipts remain message-ID duplicate-safe. All connected participants,
including each local seat, must agree; host-local authority may override. Votes
clear on transition and disconnected seats leave the quorum.

TotalQuestions accepts 0 (unlimited), 1,10,20,30,40,50. Unlimited question counters
are not restricted to 10,000. Timed duration is at most 120 seconds (125 with Extra
Time). DeadlineTicks=long.MaxValue is an explicit untimed sentinel; host retains
receipt-time validation and disables speed bonuses/Extra Time. Client arithmetic
guards this sentinel and permits untimed response statistics.

Host Replay accepts only GameOver, emits a higher-revision LobbySnapshot with
unchanged seats/teams/controllers and readiness false, and clears its match.
Clients accept this backward phase transition only after all received local
match projections reached GameOver, clear old per-slot state, and ignore old
match packets while in that returned lobby. New question instance IDs prevent
old answer/vote/card intents affecting the next match.

Unlimited matches may retire question-bound receipt entries for older instances
when the bounded cache fills; stale IDs are still rejected by Core. Generic
lobby mutation receipts retain their original lifetime bounds/disconnect policy.
The 720-question regression crosses 4,320 match requests on one connection.
Rate, packet/depth, ownership and manual-IP transport checks remain in force.

## Protocol v11 — match reconnection (2026-10-28)

All peers must upgrade together; v10 and earlier are rejected. ServerHello adds
ReconnectToken. Reconnect carries only the session-bound token; ReconnectResult
returns acceptance, the token, and the current lobby snapshot to that connection.
The host follows with private per-local-slot match projections. A reservation
cannot be reclaimed while connected, after expiry, for another session, or by an
invalid token. Receipt caches are per connection: question-bound answer/card/vote
rules remain authoritative and reject duplicate effects across a new connection.
The transport and manual-IP entry point remain intact. A host-owned RoomClosed RPC
is sent reliably before graceful shutdown. Host loss without this notice uses the
bounded retry path. See section 14 for timing, privacy and LAN limitations.

## Protocol v12 — disconnect pause (2026-10-28)

All peers upgrade together; version 11 is rejected. MatchSnapshot adds IsPaused,
PauseId, IsResuming, ResumeRemainingTicks, DisconnectedPlayers and ResumeVotes.
ResumeVote names the current unpredictable PauseId and owned LocalSlot, and is
validated/deduplicated by the host. A new disconnect invalidates old pause votes.
The host alone controls frozen logical game time, phase transitions and the five
second countdown; clients interpolate only presentation. Host receive timestamps
are converted to logical game time and no input is accepted while paused. After
manual resume the host ignores disconnected seats in untimed answer completion,
records unsubmitted disconnected players as wrong, and allows later token reclaim.
The normal question/vote/card ownership and correctness privacy rules still apply.

### Speed scoring compatibility review (2026-10-28)

The host may disable speed bonuses, or apply an untimed bonus of up to 10% of
the base score over 30 seconds of unpaused host time. The setting stays host-side
and immutable during the match; packets and the existing maximum reveal/total
bounds are unchanged. v12 clients already render host-supplied totals and accept
all resulting values, so this scoring-only revision does not require a protocol
version increment. The client never supplies elapsed time or calculates scores.

## Protocol v13 — restart reconnection and departure (2026-10-28)

All peers reject versions 12 and earlier. `AbandonReservation` carries a bounded
session-bound reconnect token. Only a currently reserved device may be abandoned;
connected devices return StillConnected. Abandonment removes all device-owned
lobby seats while retaining the match score roster, revokes the reconnect token,
and is duplicate-safe across connections for the lifetime of the match. Tokens
are never included in broadcast snapshots or logs. Fresh client state can restore
session/player/controller identifiers and the token and validate a new host
snapshot before accepting it. A fresh client can retry while the old transport is
still connected; the host distinguishes that case from an expired reservation.
The device stores the endpoint and minimum session credentials in its private
application data; no PIN, correct answer or private snapshot is saved. An explicit
decline is persisted separately and retried until the host confirms it or the
reservation no longer exists. Current LAN transport is not encrypted and does not
authenticate the host cryptographically. Physical restart and offline-delivery
verification remain release gates until observed on the target devices.

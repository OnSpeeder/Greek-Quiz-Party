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

Start with:

`ProtocolVersion = 1`

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
  "type": "quiz-discover",
  "protocol": 1,
  "nonce": "..."
}
```

Host responds directly to requester with bounded metadata:

```json
{
  "type": "quiz-host",
  "protocol": 1,
  "roomName": "Fil's Party",
  "gamePort": 7777,
  "players": 3,
  "maxPlayers": 8,
  "requiresPin": true,
  "appVersion": "0.1.0"
}
```

Do not trust an advertised address blindly if source endpoint provides the correct address.

## 12. Manual IP fallback

Join screen must support manual IPv4/hostname input for routers or environments where broadcast discovery is blocked.

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

Optional v1 flow:

1. Host marks player disconnected, keeps slot for grace period.
2. Client reconnects with opaque token.
3. Host validates token/session and connection status.
4. Host binds new connection to same player.
5. Host sends authoritative snapshot.
6. Host rejects duplicate answer submissions already processed.

Tokens must be unpredictable enough for LAN session use and must not be logged.

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

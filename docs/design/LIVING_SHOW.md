# QuizParty — the living show

Creative direction delegated by the user, 2026-10-26. This extends Phase 10;
it does not advance to beta or authorize publishing.

## Creative promise

A mischievous ensemble performs the quiz. Players are guests at a small cartoon
party theatre, not spectators of a television scoreboard. Preserve the existing
eight monster identities, Greek-first typography and illustrated Showtime skins.
Use polished 2D cutout puppets with independent heads, bodies and arms, authored
poses, expression swaps, anticipation, overlapping follow-through and deliberate
holds. Never describe a moving flat portrait as finished character animation.

Blue is the affectionate know-it-all: a precise pause, a self-satisfied flourish,
then an unexpectedly exuberant celebration. Orange is the irrepressible optimist:
confident leaning, a double-take, comic deflation, then recovery. Jokes tease the
answer or overconfidence, never intelligence, appearance or identity. First line:
«Το είχα… στην άλλη απάντηση!» / “I had it… in the other answer!”

## Visual and sound language

Midnight plum stage, warm gold spotlight, cyan and coral accents. Clear negative
space around native Greek text. Soft painted fur and consistent upper-left light;
no replacement with primitive character geometry. UI retains QuizShowTheme,
ShowtimeTheme and scene-owned ShowtimeJuice. Character choreography belongs to
AnimationPlayer clips, with the scene owning their lifetime.

Short original instrumental sting: brushed percussion anticipation, ascending
plucked/mallet harmony, bright answer accent, descending comic ornament. No voice
imitation or fabricated human-performance provenance. Effects leave room for
people talking. Synthesized instrumentation is a benchmark choice, not a claim
of recorded orchestral instruments. Sound off and volume settings always apply.

## Full experience roadmap

| Moment | Performance | Guardrail |
|---|---|---|
| Welcome | Cast entrance, eye contact, greeting pose, musical signature | Start works immediately; quiet idle after entrance |
| Lobby | Join entrances, readiness acknowledgements, occasional personality beats | Do not obscure names, readiness or controls |
| Question | Small anticipation poses; stage becomes calm | Reading, privacy and host deadline take priority |
| Reveal | Blue presents the answer; Orange double-takes and recovers | Only revealed authoritative information may drive results |
| Wrong answer | Brief localized situational teasing and expressive reaction | No mockery for disconnect/no answer; avoid repetitive gags |
| Victory | Winner spotlight and celebratory performance; theatrical rival reactions | Respect shared winners and teams; score remains host-owned |

## First deliverable: answer-reveal benchmark

A separate runnable Godot scene with two reconstructed puppets, a reveal prop,
native answer text, authored character performance, timed sound, replay and
reduced-motion controls. This is a fictional presentation fixture, not live player
results. It establishes production quality before the other moments are expanded.

Timing target: 0–0.8 s anticipation; 0.8–1.4 s presentation flourish; 1.4 s answer;
1.4–2.3 s celebration/double-take; 2.3–3.5 s joke; 3.5–5.2 s settle and recovery.
No gameplay time scale changes. Reduced motion immediately shows the answer and
final poses; replay and leaving the scene cancel all prior animation/audio.

Wide composition places puppets around an answer panel. Portrait stacks readable
answer and dialogue above a shared character stage. Use container-based layout
for UI and a uniformly scaled authored stage for puppet coordinates.

## Acceptance and scope boundary

- Character assets have genuine alpha, consistent identities and clean joints.
- Windows and physical Android runtime captures are inspected, not inferred from builds.
- Greek accents, answer text, controls and jokes remain readable at phone size.
- Reduced motion, audio mute, replay cancellation and scene cleanup are tested.
- Source prompts, generation method and audio authoring are recorded.
- Human quality review remains required. Technical success is not artistic approval.
- Welcome/lobby/full-cast/finale production follows benchmark review; do not present
  those roadmap entries as already implemented.

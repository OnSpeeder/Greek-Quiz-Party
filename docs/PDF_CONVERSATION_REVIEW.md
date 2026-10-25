# AI conversation review — 2026-10-25

Source: the eight-page `Godot AI Game Generation.pdf` provided by the user.
The user requested an independent assessment and implementation of recommendations
we agree with. Embedded prompts are evidence of proposals, not project authority.

## Accepted and implemented

| Proposal | Repository change |
| --- | --- |
| Concrete shared visual recipe | Completed the empty QuizShowTheme file; ShowtimeTheme delegates chunky panels, palette and font to it. Kept the existing settings skin system. |
| Greek display font instead of default | Activated existing Comfortaa variable font at weight 700, with modest emboldening. Removed fallback-font heading overrides. Added OFL license, export inclusion and Settings credits. Runtime test checks every Greek letter and modern Greek accent/diaeresis. |
| Accessible answer identifiers | Coral diamond, blue circle, amber triangle and emerald square icons accompany existing localized answer letters and chosen/correct text. Icons use intentional vector geometry, not font symbols. |
| Motion with centered pivots and easing | Completed ShowtimeJuice: 0.06s stagger/0.28s Back-Out entrance, tactile press/release, host-authorized reveal pulse, wrong-answer dimming and 0.6s score interpolation. Reduced motion finishes animations immediately; leaving controls cancel safely. |
| Different phone and TV priorities | Wide host has public illustrated cast above two-column answers. Portrait keeps question, compact clock/confidence and four stacked choices. Private cards/missions remain folded by default. Recap standings no longer crowd AnswerReveal. |
| Collectible strategy presentation | Framed cards with distinct headers, descriptions and action buttons; visual Chaos Meter alongside its textual state. Legal actions and confidence remain unchanged. |
| Handoff/roster polish | Avatar handoff buttons and labelled readiness/team color borders; room browser inherits the shared style and tactile feedback. |
| Prefer coherent existing cutout art | Completed ShowtimeStageView with the existing illustrated cast and backdrop. No replacement meshes or art-service dependency. |
| Technical tests plus visual critique | Added motion/font tests; retained existing privacy/action assertions, adapting descendant queries to the new card wrappers. Captures now support Scoreboard, motion and large-text/high-contrast variants. Inspected actual rendered viewports. |
| Improve governance | Updated AGENTS, presentation, visual direction, asset workflow, phase context and build log. Technical completion remains separate from human visual acceptance. |

## Disagreements and adaptations

1. **Delete Blender/Inkscape tooling or replace import checks with file existence:**
   disagree. Inspection shows these are optional toolchain probes, not game-build
   art generators. Cleanup, export, SVG skins and reproducible assets are useful.
   A valid file alone proves neither a successful import nor visual quality.
2. **Always forbid scene text editing, AnimationPlayer, procedural geometry or
   require HTML/Tailwind mockups:** disagree with blanket prohibitions. Use Godot
   MCP where it adds reliable inspection and captures; focused C# editing and
   reviewed scene files are valid. Timeline animation and intentional geometric
   badges also have legitimate uses. Mockups help exploration but native runtime
   rendering is necessary to assess this game's typography and containers.
3. **Switch SDK because global.json says 10:** no demonstrated defect. SDK and
   target framework differ. The repository records successful exports with the
   pinned SDK; current build/tests pass. No speculative toolchain downgrade.
4. **Remove allegedly tracked bin/obj files:** `git ls-files '*obj/*' '*bin/*'`
   returned none. Archive inclusion is not Git tracking. No destructive cleanup
   or Git index removal was warranted; review bundles should exclude caches.
5. **Repair allegedly stripped Greek strings:** the actual fixtures contain Greek
   names/answers and Unicode checks pass. No corruption was established locally.
6. **A master .tres is mandatory:** a centralized C# theme already exists and
   supports preferences. A second parallel theme would add drift. The empty
   proposed factory now supplies the existing assembler instead.
7. **Only the timer/confidence/answers on phones:** keep the question visible for
   phone-only/local play. Keep risk descriptions available; cards/missions remain
   behind the existing labelled privacy toggle, rather than adding redundant tabs.
   Retain the tested inline disclosure hierarchy rather than a second modal drawer.
8. **Fixed 50–55% stage and 45–50% controls:** adapt to content and available space.
   Long Greek questions and larger text must be allowed to scroll without shrinking
   touch targets. The initial wide capture clipped the lower row; reducing cast
   height fixed the ordinary landscape layout without shrinking answers.
9. **Display large PIN digits on the TV:** conflicts with the existing masked,
   transient PIN handling. No automatic disclosure or protocol change is justified.
10. **Always add SDFGI/SSAO, change renderer, or avoid all PBR:** these are not
    prerequisites for this 2D illustrated UI. Keep the verified Compatibility
    baseline; renderer/material choices need an actual 3D asset and device budget.
11. **External image-to-3D services and new pose atlases now:** no concrete missing
    asset requires them for this pass. Existing cutouts are usable. New production
    art should have a brief and review, not an automatic paid-service upload.
12. **Constant bobbing, parallax, spotlight sweeps and every-player lock-in reactions:**
    retain calm reading states and limited reveal feedback. Public DTOs do not
    justify inventing another player's lock-in state. Extra motion is not evidence
    of polish, and privacy/protocol changes are outside this presentation pass.
13. **Guaranteed 120 FPS on any Android, 30-second production models, and claims
    that agents always fail at geometry or are world-class web designers:** unsupported
    generalizations. Judge actual outputs and measure the target device. Neither a
    production-grade backend nor visual quality can be certified from a file tree.

## Scope and remaining gates

This is a Phase 10 presentation revision, not a replacement architecture, 3D game,
or release. Core, Infrastructure and the protocol are unchanged. The reviewed
content target and human visual/touch/accessibility approval remain open.
Observed verification and caveats are recorded in `../harness/build-log.md`.

# Settings page — Cartoon Showtime production specification

Status: implementation review candidate, 2026-10-18. The native settings view,
editable vector skin and original mascot pose atlases are implemented. Manual
usability/accessibility and final visual approval remain open.
It supplements `VISUAL_DIRECTION.md` and `../PRESENTATION.md` within Phase 10.

Latest integration — 2026-10-19: the user selected the Inkscape study for runtime
integration. The current candidate derives skins from `settings-study-02/`, uses
the larger dimensional title, arrow tabs, compact controls and desktop action
row. The composition notes below are the earlier design baseline; actual native
layout and current evidence are described in `../PRESENTATION.md` and
`../PHASE10_QA.md`. Functional/accessibility boundaries still apply.
`PRODUCT.md` owns product behavior and `ARCHITECTURE.md` owns code boundaries.
Godot 4.7.2 .NET / C# / .NET 8 and Windows + Android remain required.

## Reference and interpretation

User reference: [settings-page-reference.jfif](concepts/settings-page-reference.jfif),
supplied as `settings_page.jfif`. Use its theatrical composition, dimensional gold
trims, purple panels, cyan controls and expressive mascots. The reference is art
direction, not a screenshot of implemented behavior or a texture to stretch over
the screen. Its duplicated voice-over caption, English-only title, flag-only
language control and crowded bottom mascot are not production copy/layout.
Only this composite image was supplied; `image_0.png`, `image_1.png` and
`image_2.png` mentioned in the prompt are not additional available source assets.
Reference ownership/license is unverified; retain it as a design reference and
exclude it from exported game assets. Produce original trims and mascot poses.

Reuse `showtime-stage-v2.png`, `showtime-stage-wide-v2.png` and the character
identities in `showtime-crew-v2.png`. No login, registration, cloud profile or
account controls. All preferences are device-local. Opening settings never pauses
host deadlines, buffers answers or changes gameplay rules. Preserve hidden
private panels and the existing local-player handoff behavior on return.

## Visual composition

Stage → midnight scrim → gold-rimmed purple frame → inset settings cards → native
labels and controls → decorative mascot. Separate each layer so layout can grow.
Limit specular shine to borders; keep the reading surface calm and opaque.

| Token | Value / treatment |
| --- | --- |
| Stage navy | `#101329`, existing ShowtimeTheme.Navy |
| Reading surface | `#1B1C35`; proposed inset purple `#392157` |
| Decorative purple | Proposed `#7136A8`, confined to frame/tab surfaces |
| Gold | `#FFD580`, with proposed shadow `#9B581E` and highlight `#FFF0B8` |
| Cyan / text | `#71E3EF` / `#F6F5FF`, existing theme colors |
| Dim layer | Navy at initial 82% opacity; tune from actual stage captures |
| Shape | Chubby rounded panels, 22–28 logical-unit corners; restrained rivets |
| Focus | Separate solid 4-unit outline; visible on active and pressed controls |

Render the title as localized live text: **ΡΥΘΜΙΣΕΙΣ / SETTINGS**. Use a bold
Greek-capable font, gold face, blue outline and short dark offset shadow for a
dimensional sign. Put metallic ornament behind the label; never bake words into
an image. Preserve Greek accents and allow header height to grow at large text.
Body baseline is the current 22 units, 27 with larger text; headings approximately
32–48, title 40–64 as available space allows. Wrap before reducing text size.
These are initial art targets, subject to device and TV readability QA.

## Responsive composition

Use existing logical canvases (480×800 portrait, 1152×648 landscape), safe-area
insets and density-aware target calculation. Every interactive hit area is at
least the larger of 64 logical units and the existing Android 48dp equivalent.
Visual knobs may be smaller than their padded interactive regions.

**Landscape:** header across the top, left vertical Audio / Gameplay / Help &
Legal navigation, center-right scrollable content, footer below. Initial usable
width allocation: navigation 24%, content 56%, mascot 20%. Reserve a lower-right
mascot bay outside control bounds; a blue glasses monster sits on a small stage
plinth, facing inward. Cards use one label/control column in short landscape;
use two columns only when long Greek labels and focus rings fit. The content
scrolls independently while navigation and Close stay reachable.

**Portrait:** full-width header and Close, followed by a single vertical scroll
of three section cards. Use the same section order without duplicating settings
state. Each row stacks label above slider/value when needed. A small orange waving
mascot occupies a reserved bottom decorative bay; metadata precedes it in reading
order. No overlay across Reset, footer, scroll gestures or Android system areas.

Choose landscape navigation only when available width after safe insets is at
least 900 logical units and greater than height. Otherwise use stacked cards,
including narrow desktop windows and large-text layouts that cannot fit the
navigation. Rotation/reflow preserves values, active section, focused setting and
scrolls that setting into view. At small heights, reduce/hide decoration before
reducing control targets. Do not lock orientation for this page.

## Sections and behavior

| Section / control | Current support and production behavior |
| --- | --- |
| Audio — SFX | Existing Sound + Volume become clearly labelled SFX on/off and 0–100% slider; retain current default on, 65%, step 5. Keep stored keys compatible. |
| Audio — Test sound | Existing preview cue; explicit action, respects SFX mute/volume. Explain muted state rather than bypassing it. |
| Audio — Music | Requested design slot for toggle + volume; no music stream exists. Hide in shipping UI until an actual track, bus, persistence and mute behavior are implemented. |
| Audio — Voice-over | Requested toggle + volume slot; no narrated content exists. Hide until real narration and language coverage exist; UI language is a separate setting. |
| Audio — Haptics | Requested Android capability-dependent toggle; implement local persistence and feedback before exposing. Omit on Windows and unsupported devices; do not simulate availability. |
| Gameplay — Language | Requested selector: Ελληνικά / English, using names as the primary labels. Optional small flag art is supplementary. Existing translations are available, but a saved selector is new work. Refresh open UI/focus and fallback correctly; never change host questions or pack locale. |
| Gameplay — Reduced motion | Preserve existing preference/default. Explain that it removes movement and decorative effects. |
| Gameplay — Larger text | Preserve existing preference/default; reflow current page immediately. |
| Gameplay — High contrast | Preserve existing preference/default; remove artwork/glow behind text and give every state a clear outline/text cue. |
| Gameplay — Screen shake | Requested design slot; current game has no camera shake. Keep it absent while no effect exists. Any future local shake must also be disabled by reduced motion. |
| Help & Legal — Credits | Offline readable credits including artwork/audio provenance and required third-party notices. Needs authored content and a real detail panel. |
| Help & Legal — Privacy policy | Offline readable, accurate account of current local settings and LAN data handling; no invented web destination or certification claim. Needs reviewed copy. |
| Help & Legal — About | QuizParty name, actual build version, engine metadata and short offline/LAN description. |
| Help & Legal — Reset to default | Reset presentation preferences only after an explicit confirmation naming that scope. Cancel is initially focused; never clear parties, questions, progress or LAN settings. |

The table distinguishes existing behavior from new production requirements. Do
not show inert switches to satisfy a mockup. New controls require working local
services, migration/default handling and verification before being exposed.
Retain the existing Leave party action where available, separated from Reset and
Close. Closing settings returns to the game; it must not disconnect a player.

Footer: localized “Game version: {version}” and “Engine: Godot {engineVersion}”.
Read real build/engine metadata; `v1.0.0` is reference placeholder copy, not a
release assertion. If build metadata is missing, show “Development build”.

## Input, persistence and accessibility

Show explicit ON/OFF text and slider percentages. Use icon + label for tabs:
speaker (Audio), controller (Gameplay), question/document (Help & Legal), avoiding
the mismatched icons in the reference. Active tabs have a gold edge and marker,
not color alone. Include normal, hover, pressed, active, disabled and focus states.

Opening hides underlying interactive/private content, moves focus to the active
section and traps traversal in the modal. Back/Close, Escape and Android Back
close the foremost detail/confirmation first, then settings; restore the opener's
focus. Keyboard arrows adjust sliders by their configured step; Home/End set
endpoints. Touch works without hover. Drag cancellation/closing releases capture.
Decorations ignore mouse input and are excluded from accessibility traversal.

Save changes immediately using the existing `user://presentation.cfg` boundary.
Retain warnings, visible save-failure feedback and in-memory recovery. New fields
must load missing keys with defaults and validate types/ranges; old configs remain
valid. Reset updates all visible controls and persistence together. No continuous
announcements while dragging: expose the value and announce the settled value.
Use explicit accessible names, roles, values and reading order. Existing Android
accessibility-backend limitations remain a QA issue, not a certification claim.
Target 4.5:1 body-text and 3:1 large-text/control contrast in rendered captures;
measure all states rather than assuming palette values guarantee contrast.

## Godot composition and ownership

Extract a composable `SettingsPanel.tscn` from `PresentationShell.BuildSettings`;
the scene-owned shell remains the adapter for preferences/audio and modal privacy.
Suggested scene responsibilities, not implemented classes:

```text
SettingsPanel (Control, full anchors)
  Scrim (ColorRect, blocks background input)
  SafeMargin (MarginContainer, existing inset/target policy)
    Frame (PanelContainer, stretchable skin)
      Layout (VBoxContainer)
        Header (HBoxContainer: localized title, Close Button)
        Body (Container: landscape HBox / portrait VBox composition)
          Navigation (VBoxContainer, landscape only)
          Sections (ScrollContainer + VBoxContainer)
          MascotBay (Control, decoration only)
        Footer (VBoxContainer: save status, build metadata)
```

Reparent shared section views on reflow, or use one layout controller; avoid
creating separate copies with competing signal handlers. Use native Button,
CheckButton, HSlider, OptionButton and labels styled through Theme resources.
Use StyleBoxTexture / NinePatchRect for trims; keep content margins distinct from
slice margins. Containers own layout; animate an inner visual wrapper rather
than the container's geometry. C# emits preference intents and renders local
state. No Core/Godot dependency change, network DTO change or authoritative rule.

## Production asset manifest

Delivered root: `Art/Settings/`; SVGs are editable masters and runtime imports,
reproduced by `scripts/build-settings-vectors.ps1`. Raster masters are transparent
pose sheets; no layered character source is claimed. Exact dimensions/slices and
final prompts are in `Art/Settings/README.md`. The table below records design
targets; the artwork README records actual deliverables. SVG masters are Inkscape-compatible with
named layers, explicit viewBox, outlined decorative strokes and no linked files.
Export bitmap-only lighting/character work as transparent sRGB PNG; keep all
localized text native. Start with 2D; Blender is optional for a specific trim,
exported to the same 2D deliverable, with no runtime 3D requirement.

| Asset / suggested file | Master / export target | States and integration |
| --- | --- | --- |
| Main frame `frame-main` | SVG; 256×256 PNG if raster needed; 32px corner slices | Deep-purple bevel, gold double rim; normal/high-contrast variants. Rivets as separate corner decorations so they never stretch. |
| Section card `frame-card` | SVG; 128×128; 20px corner slices | Quieter purple/gold trim; opaque reading center. |
| Title ornament `header-trim` | SVG; 768×160 transparent export | Text-free metallic sign, blue shadow trim; localized title on top. |
| Tab/button skin `button-*` | SVG; 192×96; 24px corner slices | Normal, hover, pressed, active, disabled; separate focus border. Shared skins, native labels. |
| Switch `switch-track-*`, `switch-thumb-*` | SVG; 128×64 track, 56×56 thumb | On/off tracks, idle/pressed/disabled thumbs; text and focus remain native. |
| Slider `slider-track`, `slider-fill`, `slider-thumb-*` | SVG; 128×16 track with 8px end caps, 56×56 knob | Gold circular knob idle/pressed/disabled, cyan fill; do not stretch knob. |
| Icons `icon-{back,close,volume-high,volume-low,mute,gear,language,help,controller}` | Separate SVGs, 32×32 viewBox; optional 64px exports | One consistent rounded stroke style, monochrome tintable version plus gold decorative version. |
| Blue glasses mascot `mascot-blue-*` | Original layered master; transparent 768×1024 pose canvas | Idle, blink, ears-covered, celebrate, wave; stable pivot and identical canvas across poses. |
| Orange mascot `mascot-orange-*` | Original layered master; transparent 512×512 pose canvas | Idle, blink, wave and celebrate; silhouette fits portrait bottom bay. |
| Small plinth `mascot-plinth` | SVG or transparent 512×160 PNG | Decorative bay only; no baked character or text. |
| Sparkle `sparkle-gold` | SVG / 32×32 transparent PNG | Small optional pooled burst texture; no full-screen flash. |
| Scrim | Native ColorRect | No exported image required. |

Asset export gate: record source/provenance and export recipe, transparent-edge
inspection on light/dark backgrounds, clean slices without seams at minimum and
expanded sizes, crisp icons at 1×/2×, correct pivots, Android import compatibility,
and no baked text/controls. Prefer existing crew atlas as a static fallback;
new reactions need real pose artwork, not an unsupported animation claim.

## Animation and sound direction

| Event | Initial timing / behavior |
| --- | --- |
| Open | 180–220ms fade with visual wrapper 0.96→1, restrained back-out settle; input/focus available immediately. Optional short original/licensed curtain swoosh obeys mute. |
| Close | 120ms fade; restore focus/privacy promptly and cancel pending animation callbacks. |
| Hover / press | 80–110ms, visual-only 1.02 / 0.98 scale; never shrink target or displace neighboring controls. |
| Toggle | 140–180ms thumb slide, slight settle; stored state and accessible value change immediately. |
| Slider | Direct drag tracking; no interpolation lag. Optional thumb settle after release only. |
| Mascot idle | Subtle 2–3s breathing and occasional blink; local decoration only. |
| SFX/music off | Brief ears-covered pose when supported audio is turned off; mute takes effect before any feedback. |
| Test sound | Brief celebration with the explicit test cue, only when audible. |
| Reset confirmed / explicit action | At most 6–10 small gold sparkles, under 400ms, away from labels; no effects for every slider tick. |

Reduced motion cancels scale, bounce, particles and mascot loops immediately and
uses stable poses with instant state changes. High contrast disables glow and
decorative effects that compete with text. Avoid looping particles, shaders or
new dependencies; verify on the physical Android device. Stop/cancel tweens and
dispose transient audio/particle resources on close/free. No animation gates input.

## Implementation and acceptance checklist

- [x] Extract/recompose the settings scene while preserving existing controls,
  save behavior, modal focus, privacy and non-pausing host deadlines.
- [x] Produce/import original stretchable skin, icons and mascot poses; record
  provenance in the artwork README. Static fallback must work without animations.
- [x] Implement supported section navigation, live localization, offline help
  copy, truthful metadata and confirmed presentation-only reset.
- [x] Omit unavailable audio/haptic/shake controls. Actual services, assets and
  platform verification are required before exposing those controls.
- [x] Verify settings persistence/migration, invalid keys, save failure, reset
  cancel/confirm, audio mute/test, focus isolation/restoration, nested Back,
  orientation changes and immediate reduced-motion cancellation in Godot tests.
- [ ] Capture actual Windows 1920×1080 and 1280×720, narrow window, Android
  portrait/landscape with safe areas, and a short 800×480 layout. Repeat in Greek,
  English, larger text, high contrast and reduced motion; check every section.
- [ ] Observe physical Android taps/drags/rotation/Back, real-speaker audio and
  TV viewing-distance readability. Confirm mascot never blocks a target, focus
  ring or the longest Greek label. Test opening/closing during a live LAN match.
- [x] Run relevant local build/Godot tests and `git diff --check`; log actual
  evidence. Original Phase 10 accessibility/content acceptance gates stay open.

Unavailable audio/haptic/shake features are omitted, not implemented as inert
switches. This review candidate includes the supported settings, language,
offline help/About, confirmed reset and artwork. Automated evidence and outstanding
human acceptance are recorded in `../PHASE10_QA.md` and the Phase 10 build log.

## 2026-10-28 device settings recomposition

The supported controls were recomposed into a compact shared-theme header and
section cards; the selector adds Showtime, Studio, Neon and Retro, and automatic
question fitting defaults on. Existing controls, focus and stored preferences remain.
See THEMES.md. The previous exhaustive human/device matrix above remains open;
these changes do not turn earlier unchecked acceptance items into completed ones.

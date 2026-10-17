# Phase 01 — Windows/Android LAN technical spike

## Goal and scope
Prove the existing Godot 4.7.2 .NET builds can connect over real LAN using ENet,
manual host IP, and one client button action acknowledged by the Windows host.
User authorized a baseline commit/push first and another commit/push on completion.
Baseline c710604 was pushed to origin/main before implementation.

## Implementation
- Keep the foundation screen and add navigation to a disposable spike scene.
- Separate responsive C# view from a Godot ENet transport node.
- Put small, Godot-independent probe validation/deduplication in Infrastructure;
  do not build the future Core domain or production lobby/protocol.
- Use reliable RPCs, transport-derived sender IDs, bounded inputs, protocol check,
  bounded per-connection deduplication, host acknowledgement and visible failures.
- Add headless launch flags and a separate-process Windows regression script.
- Build/export Windows and Android; install on the physical phone; join through
  the actual Windows LAN IP, press the phone button, observe both host and client.

## Non-goals
Discovery, polished visual style, roster/ready/PIN/reconnect, questions, scoring,
cards, missions and gameplay state machine. Production protocol v1 is reserved;
the disposable spike contract is separately documented.

## Verification
Existing unit/scene tests plus probe validation tests, two-process loopback tests,
host exit/duplicate/protocol rejection checks where practical, Windows packaging,
actual Android install/launch/manual-IP/action/acknowledgement, git diff --check.
Use no ADB port forwarding or reverse tunnel as LAN acceptance evidence.

## Risks / recovery
Windows firewall or VPN routing can block UDP 7777. Diagnose before altering
network settings; any rule must be limited to the spike executable/port/private
LAN and documented. Never disable firewall/VPN globally. Preserve current app/data.
Record observed evidence and limitations in phase context and build log; stop at
Phase 01 and push the completed changes without starting Phase 02.

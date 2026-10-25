# Phase 10 — Android orientation and Back navigation

User-authorized scope: portrait default with sensor rotation, hierarchical Android
Back/Escape handling, and home-corner icon-only exit with Yes/No confirmation.
Preserve preceding uncommitted presentation work and Core/network rules.

Implementation: project portrait launch setting; scene shell enables sensor mode
unless an explicit debug capture locks orientation. Reuse responsive resize/safe
area handling. Shell routes Back through confirmation, settings and lobby menu
levels. In-match Back opens settings (existing leave action); it never quits.
Only home opens exit confirmation, with No initially focused, modal focus isolation
and localized labels. Confirmation adapts to rotation and larger text.

Verification: local build/GdUnit navigation, cancellation/focus and resize tests;
Godot viewport inspection; Android export/install and available device checks.
Record actual observations and any physical sensor/input limitations. No Phase 11.

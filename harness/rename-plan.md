# QuizParty rename plan

User-approved scope: rename the product and technical project identity to QuizParty,
including folders, solutions, projects, namespaces, app title, export filenames,
Android ID, scripts, current documentation, MCP path and concept branding.
Greek-first localization and the selected visual direction remain unchanged.

Preserve original Git history/remote and historical build evidence. Generated
caches/packages are not source and may retain old identifiers; create fresh
QuizParty exports and isolate stale Godot caches before verification. Keep original
concept images in ignored artifacts and reference new branded versions.

Verify restore/build, existing .NET/Godot tests, localized title, headless and
packaged Windows startup, Android export manifest/assemblies, active-source name
audit and git diff --check. Reinstall on hardware only if a device is available;
changing the Android ID creates a separate app and must not uninstall the old one.
No LAN spike, GitHub rename/push/publishing or gameplay changes are included.

# RELEASE.md

## 1. Release channels

- `dev` — local/internal only.
- `alpha` — feature incomplete, technical testers.
- `beta` — feature complete enough for external playtesting.
- `rc` — release candidate; no planned features added.
- `stable` — public v1.x.

Use semantic versioning where practical.

## 2. Windows packaging

Release artifact must:

- launch without developer SDK dependencies,
- include correct Godot runtime/export files,
- include content packs and localization,
- use release configuration,
- save user data only to platform-appropriate user-data directory,
- display version/build number.

Installer can be added after portable build is reliable.

## 3. Android packaging

Maintain separate debug and release flows.

Release requires:

- Android export templates/config validated for Godot .NET,
- INTERNET/network permissions required by game networking,
- unique application ID,
- proper version code/name,
- release signing key stored securely outside repository,
- APK for direct testing and AAB for store submission if publishing through Play Store.

Never commit release signing keys or passwords.

## 4. Pre-release checklist

- All CI checks green.
- Content validator green.
- No draft/unreviewed question in release pack.
- Windows host + Android client full match verified.
- Multi-client test completed.
- Manual-IP fallback verified.
- Discovery verified on typical home router.
- Settings persistence verified.
- Audio/mute verified.
- Reduced-motion setting verified.
- Greek fonts and diacritics verified.
- No debug overlay/log spam.
- License/credits updated for third-party assets.

## 5. Version compatibility

Application version and network protocol version are separate.

A patch release may keep same protocol version if wire behavior is compatible.

When compatibility breaks, increment protocol version and provide a clear join error.

## 6. Crash/log collection

For private testing, expose an easy way to locate/copy logs. Do not silently upload logs unless telemetry/privacy design is explicitly added later.

## 7. Store readiness

Before public Android store release prepare:

- icon/adaptive icon,
- screenshots,
- short/long Greek description,
- privacy disclosure,
- content rating,
- testing track,
- support/contact page,
- third-party notices.

## 8. Post-release

Patch priority:

1. crashes/data loss,
2. networking failures,
3. wrong answers/content errors,
4. game-breaking balance exploits,
5. UX polish.

Maintain changelog and reproducible release notes.

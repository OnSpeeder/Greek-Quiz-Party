# LAN updater implementation notes — work in progress

The game is not yet wired to an updater: no startup check, settings control,
update server or platform installer is available. Do not advertise this as a
working auto-update feature.

The infrastructure currently verifies a bounded RSA-PSS/SHA-256 signed manifest
and the downloaded package hash. The candidate fixed LAN endpoint is IPv4 port
8765, with windows.json/windows.zip and android.json/android.apk. A release
publisher must sign the manifest using a user-owned private key stored outside the
repository; the corresponding public key must be provisioned in the initially
installed application. A digest from an unsigned manifest is not authentication.

Before enabling this in the UI, implement and verify: a simple publisher/server
folder, safe public-key bootstrap and versioning, persisted device IP, asynchronous
startup status and network failure behavior, Windows staging/restart/rollback, and
Android installation through an appropriate content URI and system permission or
PackageInstaller. Android may require the device user to confirm installation;
APK updates must use the installed package's signing identity. Do not generate or
commit release private keys or claim unattended installation on ordinary Android.

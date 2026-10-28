using System.Net;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace QuizParty.Infrastructure.Updates;

public sealed record SignedUpdateManifest(string Payload, string Signature);
public sealed record UpdateDescriptor(string Version, string Platform, string FileName, long Size, string Sha256);

/// <summary>Verify a bounded signed LAN update before any package is executed.</summary>
public static class LanUpdateManifest
{
    public const long MaxPackageSize = 512L * 1024 * 1024;
    private static readonly JsonSerializerOptions Strict = new() { UnmappedMemberHandling = JsonUnmappedMemberHandling.Disallow, MaxDepth = 3 };
    public static bool ValidAddress(string value) => IPAddress.TryParse(value, out var ip) &&
        ip.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork &&
        !ip.Equals(IPAddress.Any) && !ip.Equals(IPAddress.Broadcast) && ip.GetAddressBytes()[0] is > 0 and < 224;

    public static bool TryVerify(string json, string publicKeyPem, string platform, Version installed, out UpdateDescriptor? update)
    {
        update = null;
        if (string.IsNullOrEmpty(json) || json.Length > 16384 || platform is not ("Windows" or "Android")) return false;
        try
        {
            var envelope = JsonSerializer.Deserialize<SignedUpdateManifest>(json, Strict);
            if (envelope?.Payload is not { Length: > 0 and <= 8192 } || envelope.Signature is not { Length: > 0 and <= 2048 }) return false;
            var payload = Convert.FromBase64String(envelope.Payload);
            var signature = Convert.FromBase64String(envelope.Signature);
            using var key = RSA.Create(); key.ImportFromPem(publicKeyPem);
            if (key.KeySize < 2048 || !key.VerifyData(payload, signature, HashAlgorithmName.SHA256, RSASignaturePadding.Pss)) return false;
            var candidate = JsonSerializer.Deserialize<UpdateDescriptor>(payload, Strict);
            if (candidate is null || !Version.TryParse(candidate.Version, out var version) || version.Build < 0 ||
                candidate.Platform != platform || candidate.FileName != (platform == "Windows" ? "windows.zip" : "android.apk") ||
                candidate.Size is <= 0 or > MaxPackageSize || candidate.Sha256 is not { Length: 64 } || !candidate.Sha256.All(Uri.IsHexDigit)) return false;
            if (version > new Version(installed.Major, installed.Minor, Math.Max(0, installed.Build), Math.Max(0, installed.Revision))) update = candidate;
            return true;
        }
        catch (Exception error) when (error is JsonException or FormatException or CryptographicException or ArgumentException) { return false; }
    }

    public static bool VerifyHash(ReadOnlySpan<byte> actual, string expectedHex)
    {
        try { return actual.Length == 32 && CryptographicOperations.FixedTimeEquals(actual, Convert.FromHexString(expectedHex)); }
        catch (FormatException) { return false; }
    }
}

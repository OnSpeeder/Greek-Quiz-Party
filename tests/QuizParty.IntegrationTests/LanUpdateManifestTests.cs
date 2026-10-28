using System.Security.Cryptography;
using System.Text.Json;
using QuizParty.Infrastructure.Updates;
using Xunit;
using System.Net;

namespace QuizParty.IntegrationTests;

public class LanUpdateManifestTests
{
    private sealed class Handler(Func<HttpRequestMessage, HttpResponseMessage> handle) : HttpMessageHandler
    {
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) => Task.FromResult(handle(request));
    }
    [Fact]
    public async Task DownloaderVerifiesSignedMetadataAndDeletesTamperedPackage()
    {
        using var key = RSA.Create(2048); var data = "valid package"u8.ToArray();
        var descriptor = new UpdateDescriptor("2.0.0", "Windows", "windows.zip", data.Length, Convert.ToHexString(SHA256.HashData(data)));
        var payload = JsonSerializer.SerializeToUtf8Bytes(descriptor);
        var manifest = JsonSerializer.Serialize(new SignedUpdateManifest(Convert.ToBase64String(payload),
            Convert.ToBase64String(key.SignData(payload, HashAlgorithmName.SHA256, RSASignaturePadding.Pss))));
        var tampered = false;
        using var client = new LanUpdateClient(new Handler(request => new HttpResponseMessage(HttpStatusCode.OK)
        { Content = request.RequestUri!.AbsolutePath.EndsWith(".json") ? new StringContent(manifest) : new ByteArrayContent(tampered ? "invalid pack!"u8.ToArray() : data) }));
        var update = await client.CheckAsync("127.0.0.1", key.ExportSubjectPublicKeyInfoPem(), "Windows", new Version(1, 0), CancellationToken.None);
        Assert.Equal(descriptor, update);
        var path = Path.Combine(Path.GetTempPath(), "quiz-update-" + Guid.NewGuid());
        try
        {
            await client.DownloadAsync("127.0.0.1", update!, path, CancellationToken.None);
            Assert.Equal(data, await File.ReadAllBytesAsync(path)); File.Delete(path);
            tampered = true;
            await Assert.ThrowsAsync<InvalidDataException>(() => client.DownloadAsync("127.0.0.1", update!, path, CancellationToken.None));
            Assert.False(File.Exists(path));
        }
        finally { if (File.Exists(path)) File.Delete(path); }
    }
    [Fact]
    public void OnlyAuthenticNewerBoundedPackageIsAccepted()
    {
        using var key = RSA.Create(2048); using var other = RSA.Create(2048);
        var descriptor = new UpdateDescriptor("1.2.0", "Android", "android.apk", 1234, new string('a', 64));
        var payload = JsonSerializer.SerializeToUtf8Bytes(descriptor);
        var signature = key.SignData(payload, HashAlgorithmName.SHA256, RSASignaturePadding.Pss);
        var envelope = JsonSerializer.Serialize(new SignedUpdateManifest(Convert.ToBase64String(payload), Convert.ToBase64String(signature)));
        Assert.True(LanUpdateManifest.TryVerify(envelope, key.ExportSubjectPublicKeyInfoPem(), "Android", new Version(1, 1), out var result));
        Assert.Equal(descriptor, result);
        Assert.False(LanUpdateManifest.TryVerify(envelope, other.ExportSubjectPublicKeyInfoPem(), "Android", new Version(1, 1), out _));
        Assert.False(LanUpdateManifest.TryVerify(envelope, key.ExportSubjectPublicKeyInfoPem(), "Windows", new Version(1, 1), out _));
        Assert.True(LanUpdateManifest.TryVerify(envelope, key.ExportSubjectPublicKeyInfoPem(), "Android", new Version(1, 2), out var current));
        Assert.Null(current);
        Assert.True(LanUpdateManifest.VerifyHash(SHA256.HashData("abc"u8), Convert.ToHexString(SHA256.HashData("abc"u8))));
        Assert.False(LanUpdateManifest.VerifyHash(SHA256.HashData("abc"u8), new string('0', 64)));
    }

    [Theory]
    [InlineData("192.168.1.10", true)] [InlineData("127.0.0.1", true)] [InlineData("0.0.0.0", false)]
    [InlineData("255.255.255.255", false)] [InlineData("example.com", false)] [InlineData("192.168.1.10:80", false)]
    public void UpdateAddressMustBeAnIpv4Address(string address, bool valid) => Assert.Equal(valid, LanUpdateManifest.ValidAddress(address));
}

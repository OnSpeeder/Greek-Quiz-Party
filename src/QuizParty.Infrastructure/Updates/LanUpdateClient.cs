using System.Net;
using System.Security.Cryptography;
using System.Text;

namespace QuizParty.Infrastructure.Updates;

/// <summary>Bounded LAN fetcher; installation remains a separate platform operation.</summary>
public sealed class LanUpdateClient : IDisposable
{
    private readonly HttpClient _http;
    public const int Port = 8765;
    public LanUpdateClient(HttpMessageHandler? handler = null)
    {
        _http = new HttpClient(handler ?? new HttpClientHandler { AllowAutoRedirect = false }) { Timeout = TimeSpan.FromMinutes(5) };
    }

    public async Task<UpdateDescriptor?> CheckAsync(string address, string publicKey, string platform, Version installed, CancellationToken cancellationToken)
    {
        if (!LanUpdateManifest.ValidAddress(address) || platform is not ("Windows" or "Android")) throw new ArgumentException("Invalid update endpoint or platform.");
        var uri = new UriBuilder("http", address, Port, platform == "Windows" ? "windows.json" : "android.json").Uri;
        using var response = await _http.GetAsync(uri, HttpCompletionOption.ResponseHeadersRead, cancellationToken).ConfigureAwait(false);
        if (response.StatusCode == HttpStatusCode.NotFound) return null;
        response.EnsureSuccessStatusCode();
        if (response.Content.Headers.ContentLength is > 16384) throw new InvalidDataException("Update manifest too large.");
        await using var stream = await response.Content.ReadAsStreamAsync(cancellationToken).ConfigureAwait(false);
        using var buffer = new MemoryStream(); var chunk = new byte[4096];
        while (true)
        {
            var count = await stream.ReadAsync(chunk, cancellationToken).ConfigureAwait(false); if (count == 0) break;
            if (buffer.Length + count > 16384) throw new InvalidDataException("Update manifest too large.");
            buffer.Write(chunk, 0, count);
        }
        var json = new UTF8Encoding(false, true).GetString(buffer.ToArray());
        return LanUpdateManifest.TryVerify(json, publicKey, platform, installed, out var update)
            ? update : throw new InvalidDataException("Update manifest is invalid or not newer.");
    }

    public async Task DownloadAsync(string address, UpdateDescriptor update, string newFilePath, CancellationToken cancellationToken)
    {
        if (!LanUpdateManifest.ValidAddress(address) || update.Platform is not ("Windows" or "Android") ||
            update.FileName != (update.Platform == "Windows" ? "windows.zip" : "android.apk") || update.Size is <= 0 or > LanUpdateManifest.MaxPackageSize)
            throw new ArgumentException("Invalid update package.");
        var uri = new UriBuilder("http", address, Port, update.FileName).Uri;
        using var response = await _http.GetAsync(uri, HttpCompletionOption.ResponseHeadersRead, cancellationToken).ConfigureAwait(false);
        response.EnsureSuccessStatusCode();
        if (response.Content.Headers.ContentLength is { } length && length != update.Size) throw new InvalidDataException("Unexpected package size.");
        var created = false;
        try
        {
            await using var source = await response.Content.ReadAsStreamAsync(cancellationToken).ConfigureAwait(false);
            await using var destination = new FileStream(newFilePath, FileMode.CreateNew, FileAccess.Write, FileShare.None, 65536, true);
            created = true;
            using var hash = IncrementalHash.CreateHash(HashAlgorithmName.SHA256);
            var buffer = new byte[65536]; long total = 0;
            while (true)
            {
                var count = await source.ReadAsync(buffer, cancellationToken).ConfigureAwait(false); if (count == 0) break;
                total += count; if (total > update.Size) throw new InvalidDataException("Update package too large.");
                hash.AppendData(buffer, 0, count); await destination.WriteAsync(buffer.AsMemory(0, count), cancellationToken).ConfigureAwait(false);
            }
            if (total != update.Size || !LanUpdateManifest.VerifyHash(hash.GetHashAndReset(), update.Sha256)) throw new InvalidDataException("Update package integrity check failed.");
        }
        catch { if (created) File.Delete(newFilePath); throw; }
    }
    public void Dispose() => _http.Dispose();
}

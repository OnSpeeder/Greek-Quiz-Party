using System.Security.Cryptography;
using System.Text;
using QuizParty.Core.Time;

namespace QuizParty.Infrastructure.Networking;

/// <summary>Optional LAN admission PIN; not encryption or an account credential.</summary>
public sealed class RoomAdmission
{
    public const int AttemptsPerAddress = 5;
    public static readonly TimeSpan Window = TimeSpan.FromSeconds(30);
    private readonly IGameClock _clock;
    private readonly byte[]? _pinHash;
    private readonly Dictionary<string, int> _failures = new(StringComparer.Ordinal);
    private TimeSpan _windowStart;
    private int _totalFailures;
    public bool RequiresPin => _pinHash is not null;

    public RoomAdmission(string pin, IGameClock clock)
    {
        if (!ValidPin(pin)) throw new ArgumentException("Use an empty PIN or four to six ASCII digits.", nameof(pin));
        _clock = clock;
        _windowStart = clock.Now;
        _pinHash = pin.Length == 0 ? null : SHA256.HashData(Encoding.ASCII.GetBytes(pin));
    }

    public static bool ValidPin(string? pin) => pin is not null && (pin.Length == 0 ||
        (pin.Length is >= 4 and <= 6 && pin.All(char.IsAsciiDigit)));

    public string Admit(string pin, string sourceAddress)
    {
        if (!ValidPin(pin) || string.IsNullOrEmpty(sourceAddress) || sourceAddress.Length > 64) return "MalformedRequest";
        if (!RequiresPin) return "None";
        if (_clock.Now - _windowStart >= Window)
        { _failures.Clear(); _totalFailures = 0; _windowStart = _clock.Now; }
        // Limit state and guesses across transport reconnects, including many addresses.
        if (_totalFailures >= 100 || _failures.GetValueOrDefault(sourceAddress) >= AttemptsPerAddress ||
            (!_failures.ContainsKey(sourceAddress) && _failures.Count >= 128)) return "PinRateLimited";
        if (CryptographicOperations.FixedTimeEquals(_pinHash!, SHA256.HashData(Encoding.ASCII.GetBytes(pin)))) return "None";
        _failures[sourceAddress] = _failures.GetValueOrDefault(sourceAddress) + 1;
        _totalFailures++;
        return "WrongPin";
    }
}

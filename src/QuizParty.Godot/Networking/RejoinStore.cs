using System.Text.Json;
using Godot;

namespace QuizParty.Networking;

/// <summary>Minimal local credential; never serialize a match snapshot or PIN.</summary>
public sealed record RejoinTicket(Guid Session, Guid Player, Guid Controller, string Token, string Address, int Port)
{
    public bool IsValid => Session != Guid.Empty && Player != Guid.Empty && Controller != Guid.Empty &&
        Token is { Length: 64 } && Token.All(Uri.IsHexDigit) && !string.IsNullOrWhiteSpace(Address) &&
        Address.Length <= 253 && !Address.Any(char.IsWhiteSpace) && Port is >= 1024 and <= 65535;
}

public sealed class RejoinStore(string directory)
{
    private string CurrentPath => Path.Combine(directory, "rejoin.json");
    private string PendingPath => Path.Combine(directory, "departures.json");
    private static readonly JsonSerializerOptions Options = new() { MaxDepth = 8 };

    public RejoinTicket? Load()
    {
        try
        {
            var ticket = Read<RejoinTicket>(CurrentPath);
            if (ticket is not null && !ticket.IsValid) throw new InvalidDataException("Invalid rejoin ticket.");
            return ticket;
        }
        catch (Exception error) when (error is IOException or UnauthorizedAccessException or JsonException)
        { GD.PushWarning($"Rejoin storage could not be read: {error.GetType().Name}"); return null; }
    }
    public IReadOnlyList<RejoinTicket> Pending()
    {
        if (!File.Exists(PendingPath)) return [];
        var tickets = Read<RejoinTicket[]>(PendingPath) ?? throw new InvalidDataException("Invalid pending departures.");
        if (tickets.Length > 8 || tickets.Any(t => t is null || !t.IsValid)) throw new InvalidDataException("Invalid pending departures.");
        return tickets;
    }
    public void Save(RejoinTicket ticket)
    {
        if (!ticket.IsValid) throw new ArgumentException("Invalid rejoin ticket.", nameof(ticket));
        Write(CurrentPath, ticket);
    }
    public void QueueDeparture(RejoinTicket ticket)
    {
        if (!ticket.IsValid) throw new ArgumentException("Invalid rejoin ticket.", nameof(ticket));
        var pending = Pending().ToList();
        if (!pending.Any(t => t.Session == ticket.Session && t.Player == ticket.Player)) pending.Add(ticket);
        if (pending.Count > 8) throw new InvalidOperationException("Too many pending departures.");
        Write(PendingPath, pending.ToArray());
        Clear();
    }
    public void RemovePending(RejoinTicket ticket)
    {
        var pending = Pending().Where(t => t.Session != ticket.Session || t.Player != ticket.Player).ToArray();
        if (pending.Length == 0) { if (File.Exists(PendingPath)) File.Delete(PendingPath); }
        else Write(PendingPath, pending);
    }
    public void Clear() { if (File.Exists(CurrentPath)) File.Delete(CurrentPath); }
    private static T? Read<T>(string path)
    {
        if (!File.Exists(path)) return default;
        if (new FileInfo(path).Length > 8192) throw new InvalidDataException("Rejoin file is too large.");
        return JsonSerializer.Deserialize<T>(File.ReadAllText(path), Options);
    }
    private static void Write<T>(string path, T data)
    {
        Directory.CreateDirectory(Path.GetDirectoryName(path)!);
        var temp = path + ".tmp";
        using (var stream = new FileStream(temp, FileMode.Create, System.IO.FileAccess.Write, FileShare.None))
        {
            JsonSerializer.Serialize(stream, data, Options); stream.Flush(true);
        }
        File.Move(temp, path, true);
    }
    public static RejoinStore Device() => new(ProjectSettings.GlobalizePath("user://"));
}

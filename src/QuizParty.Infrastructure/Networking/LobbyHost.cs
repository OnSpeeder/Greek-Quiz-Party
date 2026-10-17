using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using QuizParty.Core.Time;
using QuizParty.Core.Randomness;
using QuizParty.Core.Questions;

namespace QuizParty.Infrastructure.Networking;

/// <summary>Production v1 host router. Connection IDs must come from the transport.</summary>
public sealed class LobbyHost
{
    public const int MaxRequestsPerConnection = 256;
    public const int MaxMessagesPerSecond = 32;
    public const int MaxTransportConnections = 12;
    private readonly LobbySession _lobby;
    private readonly IGameClock _clock;
    private readonly Dictionary<long, PeerRequests> _peers = new();
    private OneQuestionMatch? _match;
    private readonly QuestionDefinition? _question;
    public Guid SessionId { get; } = Guid.NewGuid();
    public string RoomName { get; }

    public LobbyHost(string roomName, string hostName, IGameClock clock, QuestionDefinition? question = null)
    {
        if (!LobbyProtocol.ValidName(roomName)) throw new ArgumentException("Invalid room name.", nameof(roomName));
        if (!LobbyProtocol.ValidName(hostName)) throw new ArgumentException("Invalid host name.", nameof(hostName));
        ArgumentNullException.ThrowIfNull(clock);
        RoomName = roomName;
        _clock = clock;
        _question = question;
        _lobby = new(new(new(Guid.NewGuid()), hostName, LobbySession.HostConnection, new(0)));
    }

    public LobbySnapshotDto Snapshot()
    {
        var snapshot = _lobby.GetSnapshot();
        return new(SessionId, snapshot.Revision, RoomName, snapshot.Phase.ToString(), snapshot.Players.Select(player =>
            new LobbyPlayerDto(player.Player.Id.Value, player.Player.DisplayName, player.IsHost, player.Ready)).ToArray());
    }

    public LobbyError SetHostReady(bool ready) => _lobby.SetReady(LobbySession.HostConnection, ready);
    public LobbyError Start() => _lobby.Start(LobbySession.HostConnection);
    public bool BeginMatch()
    {
        if (_match is not null || _question is null || _lobby.GetSnapshot().Phase != GamePhase.GameStarting) return false;
        _match = new(GetPlayers(), _clock, new SeededRandomSource(Random.Shared.Next()), _question,
            new(Guid.NewGuid()), TimeSpan.FromSeconds(20));
        return true;
    }

    public MatchSnapshotDto? MatchSnapshot()
    {
        if (_match is null) return null;
        var game = _match.Snapshot;
        var question = game.Question!;
        return new(SessionId, _match.Revision, game.Phase.ToString(), _clock.Now.Ticks,
            new(question.InstanceId.Value, question.Text, question.Answers.ToArray(), question.CategoryId,
                question.Difficulty, question.StartedAt.Ticks, question.Deadline.Ticks), game.AcceptedAnswerCount,
            game.Scores.Select(score => new MatchScoreDto(score.PlayerId.Value, score.DisplayName, score.Total)).ToArray(),
            game.Reveal is null ? null : new(game.Reveal.CorrectAnswerIndex, game.Reveal.Explanation,
                game.Reveal.Players.Select(player => new MatchPlayerResultDto(player.PlayerId.Value,
                    player.AnswerIndex, player.IsCorrect, player.Points)).ToArray()));
    }

    public IReadOnlyList<LobbyOutbound> BroadcastMatch() => _match is null ? [] : _lobby.GetSnapshot().Players
        .Where(player => !player.IsHost).Select(player => new LobbyOutbound(player.Player.ConnectionId!.Value.Value,
            LobbyProtocol.Encode("MatchSnapshot", SessionId, MatchSnapshot()!))).ToArray();

    public bool PollMatch() => _match?.Poll() ?? false;
    public GameError AdvanceMatch() => _match?.Advance() ?? GameError.InvalidTransition;
    public SubmissionError SubmitHostAnswer(int index) => SubmitAnswer(1,
        new(_match?.Snapshot.Question?.InstanceId.Value ?? Guid.Empty, index, 1), _clock.Now);

    private SubmissionError SubmitAnswer(long connection, AnswerRequestDto answer, TimeSpan receivedAt)
    {
        if (_lobby.FindPlayer(new(connection)) is not { } playerId) return SubmissionError.UnknownPlayer;
        if (_match is null) return SubmissionError.InvalidState;
        return _match.Submit(new(playerId, new(answer.QuestionInstanceId), answer.AnswerIndex,
            (ConfidenceLevel)answer.Confidence), receivedAt);
    }
    public IReadOnlyList<Player> GetPlayers() => Array.AsReadOnly(_lobby.GetSnapshot().Players.Select(player => player.Player).ToArray());

    public IReadOnlyList<LobbyOutbound> Broadcast() => _lobby.GetSnapshot().Players
        .Where(player => !player.IsHost)
        .Select(player => new LobbyOutbound(player.Player.ConnectionId!.Value.Value,
            LobbyProtocol.Encode("LobbySnapshot", SessionId, Snapshot()))).ToArray();

    public bool Disconnect(long connection)
    {
        _peers.Remove(connection);
        return _lobby.Disconnect(new(connection));
    }

    public LobbyDispatch Handle(long connection, string json)
    {
        var receivedAt = _clock.Now;
        if (connection <= 1) return new([], true);
        if (!_peers.TryGetValue(connection, out var peer))
        {
            if (_peers.Count >= MaxTransportConnections) return new([], true);
            peer = new() { WindowStart = _clock.Now };
            _peers.Add(connection, peer);
        }
        if (_clock.Now - peer.WindowStart >= TimeSpan.FromSeconds(1))
        {
            peer.WindowStart = _clock.Now;
            peer.MessagesInWindow = 0;
        }
        if (++peer.MessagesInWindow > MaxMessagesPerSecond) return new([], true);
        if (!LobbyProtocol.TryDecode(json, out var packet) || packet is null) return new([], ++peer.Violations >= 3);
        if (peer.Processed.TryGetValue(packet.MessageId, out var previous))
        {
            if (previous.Request == json) return new([new(connection, previous.Reply)], false);
            return Reply(connection, packet, "RequestConflict", disconnect: ++peer.Violations >= 3);
        }
        if (peer.Processed.Count >= MaxRequestsPerConnection) return Reply(connection, packet, "RequestLimit", disconnect: true);
        if (packet.ProtocolVersion != LobbyProtocol.Version) return Reply(connection, packet, "IncompatibleVersion", disconnect: true);
        if (packet.CorrelationId is not null) return Reply(connection, packet, "MalformedRequest", disconnect: ++peer.Violations >= 3);
        var before = Snapshot().Revision;
        var matchBefore = _match?.Revision;
        string reply;
        if (packet.MessageType == "ClientHello")
        {
            var reason = Join(connection, packet, out var playerId);
            reply = LobbyProtocol.Encode("ServerHello", SessionId,
                new ServerHelloDto(reason == "None", reason, playerId, reason == "None" ? Snapshot() : null), packet.MessageId);
        }
        else
        {
            var reason = ValidateRequest(connection, packet, receivedAt);
            if (packet.MessageType == "SubmitAnswer")
            {
                LobbyProtocol.TryPayload<AnswerRequestDto>(packet, out var answer);
                reply = LobbyProtocol.Encode("AnswerAccepted", SessionId,
                    new AnswerReceiptDto(reason == "None", reason, answer?.QuestionInstanceId ?? Guid.Empty), packet.MessageId);
            }
            else reply = LobbyProtocol.Encode("RequestResult", SessionId, new RequestResultDto(reason == "None", reason), packet.MessageId);
        }
        peer.Processed.Add(packet.MessageId, new(json, reply));
        var messages = new List<LobbyOutbound> { new(connection, reply) };
        if (before != Snapshot().Revision) messages.AddRange(Broadcast());
        if (matchBefore != _match?.Revision) messages.AddRange(BroadcastMatch());
        return new(messages, false);
    }

    private string Join(long connection, LobbyEnvelope packet, out Guid? playerId)
    {
        playerId = null;
        if (packet.SessionId != Guid.Empty || !LobbyProtocol.TryPayload<ClientHelloDto>(packet, out var hello) || hello is null ||
            !LobbyProtocol.ValidName(hello.DisplayName) || hello.AppVersion is not { Length: > 0 and <= 32 } ||
            hello.Platform is not ("Windows" or "Android" or "Linux" or "macOS")) return "MalformedRequest";
        if (_lobby.FindPlayer(new(connection)) is not null) return "AlreadyJoined";
        var player = new Player(new(Guid.NewGuid()), hello.DisplayName, new(connection), new(0));
        var error = _lobby.Join(player);
        if (error == LobbyError.None) playerId = player.Id.Value;
        return error.ToString();
    }

    private string ValidateRequest(long connection, LobbyEnvelope packet, TimeSpan receivedAt)
    {
        if (_lobby.FindPlayer(new(connection)) is null) return "HandshakeRequired";
        if (packet.SessionId != SessionId) return "WrongSession";
        if (packet.MessageType is "StartGame" or "AdvanceMatch") return "NotHost";
        if (packet.MessageType == "SubmitAnswer")
        {
            if (!LobbyProtocol.TryPayload<AnswerRequestDto>(packet, out var answer) || answer is null) return "MalformedRequest";
            return SubmitAnswer(connection, answer, receivedAt).ToString();
        }
        if (packet.MessageType != "SetReady" || !LobbyProtocol.TryPayload<ReadyRequestDto>(packet, out var ready) || ready is null)
            return "MalformedRequest";
        return _lobby.SetReady(new(connection), ready.Ready).ToString();
    }

    private LobbyDispatch Reply(long connection, LobbyEnvelope packet, string reason, bool disconnect = false)
    {
        var json = packet.MessageType == "ClientHello"
            ? LobbyProtocol.Encode("ServerHello", SessionId, new ServerHelloDto(false, reason, null, null), packet.MessageId)
            : LobbyProtocol.Encode("RequestResult", SessionId, new RequestResultDto(false, reason), packet.MessageId);
        return new([new(connection, json)], disconnect);
    }

    private sealed record CachedReply(string Request, string Reply);
    private sealed class PeerRequests
    {
        public TimeSpan WindowStart { get; set; }
        public int MessagesInWindow { get; set; }
        public int Violations { get; set; }
        public Dictionary<Guid, CachedReply> Processed { get; } = new();
    }
}

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
    private readonly RoomAdmission _admission;
    public bool RequiresPin => _admission.RequiresPin;
    private readonly Dictionary<long, PeerRequests> _peers = new();
    private FullMatch? _match;
    private readonly IReadOnlyList<QuestionDefinition> _questions;
    private MatchSettings _settings = new(1);
    private string[]? _categories;
    private IRandomSource? _random;
    public Guid SessionId { get; } = Guid.NewGuid();
    public string RoomName { get; }

    public LobbyHost(string roomName, string hostName, IGameClock clock, QuestionDefinition? question = null, string pin = "")
    {
        if (!LobbyProtocol.ValidName(roomName)) throw new ArgumentException("Invalid room name.", nameof(roomName));
        if (!LobbyProtocol.ValidName(hostName)) throw new ArgumentException("Invalid host name.", nameof(hostName));
        ArgumentNullException.ThrowIfNull(clock);
        RoomName = roomName;
        _clock = clock;
        _admission = new(pin, clock);
        _questions = question is null ? [] : [question];
        _lobby = new(new(new(Guid.NewGuid()), hostName, LobbySession.HostConnection, new(0)));
    }

    public LobbyHost(string roomName, string hostName, IGameClock clock, IReadOnlyList<QuestionDefinition> questions,
        MatchSettings settings, string pin = "", IRandomSource? random = null) : this(roomName, hostName, clock, pin: pin)
    {
        _questions = Array.AsReadOnly(questions.ToArray());
        _settings = settings;
        _random = random;
    }

    public bool ConfigureMatch(MatchSettings settings, IReadOnlyCollection<string>? categories = null)
    {
        if (_match is not null || _lobby.GetSnapshot().Phase != GamePhase.Lobby ||
            _questions.Count(q => categories is null || categories.Contains(q.CategoryId)) < settings.QuestionCount) return false;
        _settings = settings;
        _categories = categories?.ToArray();
        return true;
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
        if (_match is not null || _questions.Count < _settings.QuestionCount || _lobby.GetSnapshot().Phase != GamePhase.GameStarting) return false;
        _match = new(GetPlayers(), _clock, _random ?? new SeededRandomSource(Random.Shared.Next()), _questions, _settings, _categories);
        return true;
    }

    public MatchSnapshotDto? MatchSnapshot(PlayerId? recipient = null)
    {
        if (_match is null) return null;
        var game = _match.Snapshot;
        var question = game.Question!;
        var own = _match.Private(recipient ?? GetPlayers().Single(p => p.ConnectionId == LobbySession.HostConnection).Id);
        var rules = _match.Strategy;
        return new(SessionId, _match.Revision, game.Phase.ToString(), _clock.Now.Ticks,
            new(question.InstanceId.Value, question.Text, question.Answers.ToArray(), question.CategoryId,
                question.Difficulty, question.StartedAt.Ticks, question.Deadline.Ticks), game.AcceptedAnswerCount,
            game.Scores.Select(score => new MatchScoreDto(score.PlayerId.Value, score.DisplayName, score.Total)).ToArray(),
            game.Reveal is null ? null : new(game.Reveal.CorrectAnswerIndex, game.Reveal.Explanation,
                game.Reveal.Players.Select(player => new MatchPlayerResultDto(player.PlayerId.Value,
                    player.AnswerIndex, player.IsCorrect, player.Points)).ToArray()),
            _match.QuestionNumber, _match.TotalQuestions, _match.RoundNumber, _match.IsTieBreaker,
            _match.Eligible.Select(id => id.Value).ToArray(), _match.Winners.Select(id => id.Value).ToArray(),
            _match.ContentExhausted, game.Phase == GamePhase.GameOver ? _match.Statistics.Select(s =>
                new MatchStatisticsDto(s.PlayerId.Value, s.Correct, s.Wrong, s.Unanswered, s.BestStreak,
                    s.ResponseTicks, s.Responses)).ToArray() : [],
            rules is null ? null : new(rules.Confidence, rules.Streaks, rules.Cards, rules.Missions, rules.AllowSteal),
            own is null ? null : new(own.Player.Value, own.Hand.Select(c => new CardDto(c.Id, (int)c.Kind)).ToArray(),
                own.HiddenAnswers.ToArray(), own.Deadline.Ticks, own.Shield, own.DoublePoints, own.Streak, own.Meter,
                Mission(own.Mission), own.SwapCategories.ToArray(), own.Notice),
            _match.FinalStrategy.Select(s => new StrategyFinalDto(s.Player.Value, Mission(s.Mission), s.MissionBonus,
                s.CardsUsed, s.ConfidentCorrect, s.ConfidentWrong, s.AllInCorrect, s.AllInWrong)).ToArray());
    }
    private static MissionDto? Mission(MissionView? mission) => mission is null ? null :
        new((int)mission.Kind, mission.Target, mission.Progress, mission.Complete);

    public IReadOnlyList<LobbyOutbound> BroadcastMatch() => _match is null ? [] : _lobby.GetSnapshot().Players
        .Where(player => !player.IsHost).Select(player => new LobbyOutbound(player.Player.ConnectionId!.Value.Value,
            LobbyProtocol.Encode("MatchSnapshot", SessionId, MatchSnapshot(player.Player.Id)!))).ToArray();

    public bool PollMatch() => _match?.Poll() ?? false;
    public GameError AdvanceMatch() => _match?.Advance() ?? GameError.InvalidTransition;
    public SubmissionError SubmitHostAnswer(int index, int confidence = 1) => SubmitAnswer(1,
        new(_match?.Snapshot.Question?.InstanceId.Value ?? Guid.Empty, index, confidence), _clock.Now);
    public CardError ActivateHostCard(CardRequestDto request) => ActivateCard(1, request, _clock.Now);

    private CardError ActivateCard(long connection, CardRequestDto request, TimeSpan receivedAt)
    {
        if (_lobby.FindPlayer(new(connection)) is not { } player) return CardError.UnknownPlayer;
        if (_match is null) return CardError.Disabled;
        if (request.Category?.Length > 128) return CardError.InvalidCategory;
        return _match.Activate(new(player, new(request.QuestionInstanceId), request.CardId,
            request.Target is { } target ? new PlayerId(target) : null, request.Category), receivedAt);
    }

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
        if (_lobby.FindPlayer(new(connection)) is { } player) _match?.Disconnect(player);
        _peers.Remove(connection);
        return _lobby.Disconnect(new(connection));
    }

    public LobbyDispatch Handle(long connection, string json, string sourceAddress = "local-adapter")
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
            var reason = Join(connection, packet, sourceAddress, out var playerId);
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
            else if (packet.MessageType == "ActivateCard")
            {
                LobbyProtocol.TryPayload<CardRequestDto>(packet, out var card);
                reply = LobbyProtocol.Encode("CardResult", SessionId,
                    new CardReceiptDto(reason == "None", reason, card?.QuestionInstanceId ?? Guid.Empty, card?.CardId ?? Guid.Empty), packet.MessageId);
            }
            else reply = LobbyProtocol.Encode("RequestResult", SessionId, new RequestResultDto(reason == "None", reason), packet.MessageId);
        }
        peer.Processed.Add(packet.MessageId, new(json, reply));
        var messages = new List<LobbyOutbound> { new(connection, reply) };
        if (before != Snapshot().Revision) messages.AddRange(Broadcast());
        if (matchBefore != _match?.Revision) messages.AddRange(BroadcastMatch());
        return new(messages, false);
    }

    private string Join(long connection, LobbyEnvelope packet, string sourceAddress, out Guid? playerId)
    {
        playerId = null;
        if (packet.SessionId != Guid.Empty || !LobbyProtocol.TryPayload<ClientHelloDto>(packet, out var hello) || hello is null ||
            !LobbyProtocol.ValidName(hello.DisplayName) || hello.AppVersion is not { Length: > 0 and <= 32 } ||
            hello.Platform is not ("Windows" or "Android" or "Linux" or "macOS") || !RoomAdmission.ValidPin(hello.Pin)) return "MalformedRequest";
        if (_lobby.FindPlayer(new(connection)) is not null) return "AlreadyJoined";
        var snapshot = _lobby.GetSnapshot();
        if (snapshot.Phase != GamePhase.Lobby) return "GameStarted";
        if (snapshot.Players.Count >= LobbySession.MaxPlayers) return "RoomFull";
        var admission = _admission.Admit(hello.Pin, sourceAddress);
        if (admission != "None") return admission;
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
        if (packet.MessageType == "ActivateCard")
        {
            if (!LobbyProtocol.TryPayload<CardRequestDto>(packet, out var card) || card is null) return "MalformedRequest";
            return ActivateCard(connection, card, receivedAt).ToString();
        }
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

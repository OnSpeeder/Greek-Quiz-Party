using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Players;
using QuizParty.Core.Time;
using QuizParty.Core.Randomness;
using QuizParty.Core.Questions;
using System.Text;

namespace QuizParty.Infrastructure.Networking;

/// <summary>Production v1 host router. Connection IDs must come from the transport.</summary>
public sealed class LobbyHost
{
    public const int MaxRequestsPerConnection = 2048;
    public const int MaxCachedBytes = 2 * 1024 * 1024;
    public const int MaxMessagesPerSecond = 32;
    public const int MaxTransportConnections = 12;
    private readonly LobbySession _lobby;
    private readonly IGameClock _clock;
    private readonly RoomAdmission _admission;
    public bool RequiresPin => _admission.RequiresPin;
    public bool HasRoomAccess(long connection) => _peers.TryGetValue(connection, out var peer) && peer.AdmittedUntil > _clock.Now;
    private readonly Dictionary<long, PeerRequests> _peers = new();
    private readonly Dictionary<long, Guid> _controllers = new() { [1] = Guid.NewGuid() };
    private FullMatch? _match;
    private readonly Dictionary<Guid, int> _matchCharacters = new();
    private readonly IReadOnlyList<QuestionDefinition> _questions;
    private MatchSettings _settings = new(1);
    private string[]? _categories;
    private IRandomSource? _random;
    public Guid SessionId { get; } = Guid.NewGuid();
    public string RoomName { get; }
    public Guid HostControllerId => _controllers[1];

    public LobbyHost(string roomName, string hostName, IGameClock clock, QuestionDefinition? question = null, string pin = "", int hostCharacter = 0, bool hostPlays = true, int maxPlayers = 8)
    {
        if (!LobbyProtocol.ValidName(roomName)) throw new ArgumentException("Invalid room name.", nameof(roomName));
        if (hostPlays && !LobbyProtocol.ValidName(hostName)) throw new ArgumentException("Invalid host name.", nameof(hostName));
        ArgumentNullException.ThrowIfNull(clock);
        RoomName = roomName;
        _clock = clock;
        _admission = new(pin, clock);
        _questions = question is null ? [] : [question];
        _lobby = hostPlays ? new(new(new(Guid.NewGuid()), hostName, LobbySession.HostConnection, new(0), (CharacterId)hostCharacter), maxPlayers)
            : LobbySession.WithoutHostPlayer(maxPlayers);
    }

    public LobbyHost(string roomName, string hostName, IGameClock clock, IReadOnlyList<QuestionDefinition> questions,
        MatchSettings settings, string pin = "", IRandomSource? random = null, int hostCharacter = 0, bool hostPlays = true, int maxPlayers = 8) : this(roomName, hostName, clock, pin: pin, hostCharacter: hostCharacter, hostPlays: hostPlays, maxPlayers: maxPlayers)
    {
        _questions = Array.AsReadOnly(questions.ToArray());
        _settings = settings;
        _random = random;
    }

    public bool ConfigureMatch(MatchSettings settings, IReadOnlyCollection<string>? categories = null)
    {
        if (_match is not null || _lobby.GetSnapshot().Phase != GamePhase.Lobby ||
            _questions.Count(q => (categories is null || categories.Contains(q.CategoryId)) && settings.Difficulties.Contains(q.Difficulty)) < Math.Max(1, settings.QuestionCount)) return false;
        _settings = settings;
        _categories = categories?.ToArray();
        return true;
    }

    public LobbySnapshotDto Snapshot()
    {
        var snapshot = _lobby.GetSnapshot();
        return new(SessionId, snapshot.Revision, RoomName, snapshot.Phase.ToString(), snapshot.Players.Select(player =>
            new LobbyPlayerDto(player.Player.Id.Value, player.Player.DisplayName, player.IsHost, player.Ready,
                _controllers[player.Player.ConnectionId!.Value.Value], player.Player.LocalSlot?.Value ?? 0, (int?)player.TeamId, (int?)player.Player.Character)).ToArray(), snapshot.TeamMode, _lobby.Capacity, _lobby.HostPlays);
    }

    public LobbyError SetHostReady(bool ready, int localSlot = 0) => localSlot is < 0 or > 7 ? LobbyError.InvalidPlayer : _lobby.SetReady(LobbySession.HostConnection, ready, new(localSlot));
    public LobbyError AddHostLocal(string name, int slot, int? character = null) => AddLocal(1, new(name, slot, character));
    public LobbyError RemoveHostLocal(int slot) => slot is < 1 or > 7 ? LobbyError.InvalidPlayer : _lobby.RemoveLocal(new(1), new(slot));
    public LobbyError SetTeamMode(bool enabled) => _lobby.SetTeamMode(new(1), enabled);
    public LobbyError AssignTeam(Guid player, int team) => _lobby.SetTeam(new(1), new(player), (TeamId)team);

    private LobbyError AddLocal(long connection, AddLocalPlayerDto request)
    {
        if (!LobbyProtocol.ValidName(request.DisplayName) || request.LocalSlot is < 1 or > 7 || request.CharacterId is { } character && !Characters.IsValid(character)) return LobbyError.InvalidPlayer;
        return _lobby.AddLocal(new(new(Guid.NewGuid()), request.DisplayName, new(connection), new(request.LocalSlot), (CharacterId?)request.CharacterId));
    }
    public LobbyError Start() => _lobby.Start(LobbySession.HostConnection);
    public bool BeginMatch()
    {
        if (_match is not null || _questions.Count < Math.Max(1, _settings.QuestionCount) || _lobby.GetSnapshot().Phase != GamePhase.GameStarting) return false;
        foreach (var player in GetPlayers()) _matchCharacters[player.Id.Value] = (int)player.Character!.Value;
        _match = new(GetPlayers(), _clock, _random ?? new SeededRandomSource(Random.Shared.Next()), _questions, _settings, _categories, teams: _lobby.Teams());
        return true;
    }

    public MatchSnapshotDto? MatchSnapshot(PlayerId? recipient = null)
    {
        if (_match is null) return null;
        var game = _match.Snapshot;
        var question = game.Question!;
        var owner = recipient ?? _lobby.FindPlayer(new(1));
        var player = owner is { } id ? GetPlayers().Single(p => p.Id == id) : null;
        // The non-playing host gets the public projection only, never another seat's hand/mission.
        var own = player is null ? null : _match.Private(player.Id);
        var rules = _match.Strategy;
        return new(SessionId, _match.Revision, game.Phase.ToString(), _clock.Now.Ticks,
            new(question.InstanceId.Value, question.Text, question.Answers.ToArray(), question.CategoryId,
                question.Difficulty, question.StartedAt.Ticks, question.Deadline.Ticks), game.AcceptedAnswerCount,
            game.Scores.Select(score => new MatchScoreDto(score.PlayerId.Value, score.DisplayName, score.Total, _matchCharacters[score.PlayerId.Value])).ToArray(),
            game.Reveal is null ? null : new(game.Reveal.CorrectAnswerIndex, game.Reveal.Explanation,
                game.Reveal.Players.Select(player => new MatchPlayerResultDto(player.PlayerId.Value,
                    player.AnswerIndex, player.IsCorrect, player.Points)).ToArray(),
                game.Reveal.FunFacts?.ToArray()),
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
                s.CardsUsed, s.ConfidentCorrect, s.ConfidentWrong, s.AllInCorrect, s.AllInWrong)).ToArray(),
            _match.TeamScores.Select(t => new TeamScoreDto((int)t.TeamId, t.Total, t.Members.Select(p => p.Value).ToArray())).ToArray(),
            _match.WinningTeams.Select(t => (int)t).ToArray(), player?.LocalSlot?.Value ?? 0, _match.AnsweredPlayers.Select(p => p.Value).ToArray(),
            _match.ContinueVotes.Select(p => p.Value).ToArray(), _match.EndVotes.Select(p => p.Value).ToArray());
    }
    private static MissionDto? Mission(MissionView? mission) => mission is null ? null :
        new((int)mission.Kind, mission.Target, mission.Progress, mission.Complete);

    public IReadOnlyList<LobbyOutbound> BroadcastMatch() => _match is null ? [] : _lobby.GetSnapshot().Players
        .Where(player => player.Player.ConnectionId != LobbySession.HostConnection).Select(player => new LobbyOutbound(player.Player.ConnectionId!.Value.Value,
            LobbyProtocol.Encode("MatchSnapshot", SessionId, MatchSnapshot(player.Player.Id)!))).ToArray();

    public bool PollMatch() => _match?.Poll() ?? false;
    public GameError Vote(long connection, MatchVoteDto request)
    {
        if (request.LocalSlot is < 0 or > 7 || request.Phase is not ("AnswerReveal" or "Scoreboard" or "RoundEnd") ||
            _lobby.FindPlayer(new(connection), new(request.LocalSlot)) is not { } player || _match is null)
            return GameError.InvalidTransition;
        return _match.Vote(player, new(request.QuestionInstanceId), Enum.Parse<GamePhase>(request.Phase), request.EndGame);
    }
    public GameError EndMatch() => _match?.EndUnlimited() ?? GameError.InvalidTransition;
    public bool Replay()
    {
        if (_match?.Snapshot.Phase != GamePhase.GameOver) return false;
        _lobby.Replay(); _match = null; _matchCharacters.Clear(); return true;
    }
    public GameError AdvanceMatch() => _match?.Advance() ?? GameError.InvalidTransition;
    public SubmissionError SubmitHostAnswer(int index, int confidence = 1, int localSlot = 0) => SubmitAnswer(1,
        new(_match?.Snapshot.Question?.InstanceId.Value ?? Guid.Empty, index, confidence, localSlot), _clock.Now);
    public CardError ActivateHostCard(CardRequestDto request) => ActivateCard(1, request, _clock.Now);

    private CardError ActivateCard(long connection, CardRequestDto request, TimeSpan receivedAt)
    {
        if (request.LocalSlot is < 0 or > 7 || _lobby.FindPlayer(new(connection), new(request.LocalSlot)) is not { } player) return CardError.UnknownPlayer;
        if (_match is null) return CardError.Disabled;
        if (request.Category?.Length > 128) return CardError.InvalidCategory;
        return _match.Activate(new(player, new(request.QuestionInstanceId), request.CardId,
            request.Target is { } target ? new PlayerId(target) : null, request.Category), receivedAt);
    }

    private SubmissionError SubmitAnswer(long connection, AnswerRequestDto answer, TimeSpan receivedAt)
    {
        if (answer.LocalSlot is < 0 or > 7 || _lobby.FindPlayer(new(connection), new(answer.LocalSlot)) is not { } playerId) return SubmissionError.UnknownPlayer;
        if (_match is null) return SubmissionError.InvalidState;
        return _match.Submit(new(playerId, new(answer.QuestionInstanceId), answer.AnswerIndex,
            (ConfidenceLevel)answer.Confidence), receivedAt);
    }
    public IReadOnlyList<Player> GetPlayers() => Array.AsReadOnly(_lobby.GetSnapshot().Players.Select(player => player.Player).ToArray());

    public IReadOnlyList<LobbyOutbound> Broadcast() => _lobby.GetSnapshot().Players
        .Where(player => player.Player.ConnectionId != LobbySession.HostConnection)
        .Select(player => player.Player.ConnectionId!.Value.Value).Distinct()
        .Select(connection => new LobbyOutbound(connection,
            LobbyProtocol.Encode("LobbySnapshot", SessionId, Snapshot()))).ToArray();

    public bool Disconnect(long connection)
    {
        if (connection <= 1) return false;
        foreach (var player in GetPlayers().Where(p => p.ConnectionId?.Value == connection)) _match?.Disconnect(player.Id);
        _peers.Remove(connection);
        _controllers.Remove(connection);
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
        if (_settings.Unlimited && _match?.Snapshot.Question is { } current &&
            (peer.Processed.Count >= MaxRequestsPerConnection || peer.CachedBytes >= MaxCachedBytes))
        {
            // Only question-bound intents can expire: the immutable instance ID prevents reapplication.
            // Lobby mutation receipts remain retained for the lifetime of the connection.
            foreach (var entry in peer.Processed.Where(p => p.Value.Question is { } id && id != current.InstanceId.Value).ToArray())
            {
                peer.CachedBytes -= Encoding.UTF8.GetByteCount(entry.Value.Request) + Encoding.UTF8.GetByteCount(entry.Value.Reply);
                peer.Processed.Remove(entry.Key);
            }
        }
        if (peer.Processed.Count >= MaxRequestsPerConnection || peer.CachedBytes >= MaxCachedBytes) return Reply(connection, packet, "RequestLimit", disconnect: true);
        if (packet.ProtocolVersion != LobbyProtocol.Version) return Reply(connection, packet, "IncompatibleVersion", disconnect: true);
        if (packet.CorrelationId is not null) return Reply(connection, packet, "MalformedRequest", disconnect: ++peer.Violations >= 3);
        var before = Snapshot().Revision;
        var matchBefore = _match?.Revision;
        string reply;
        if (packet.MessageType is "CheckRoom" or "RoomAvailability")
        {
            var reason = CheckRoom(peer, packet, sourceAddress);
            reply = LobbyProtocol.Encode("RoomAccessResult", SessionId,
                new RoomAccessResultDto(reason == "None", reason, Snapshot().Revision,
                    reason == "None" ? TakenCharacters() : []), packet.MessageId);
        }
        else if (packet.MessageType == "ClientHello")
        {
            var reason = Join(connection, packet, sourceAddress, out var playerId);
            reply = LobbyProtocol.Encode("ServerHello", SessionId,
                new ServerHelloDto(reason == "None", reason, playerId, reason == "None" ? Snapshot() : null,
                    reason == "None" ? _controllers[connection] : null,
                    peer.AdmittedUntil > _clock.Now ? TakenCharacters() : null), packet.MessageId);
        }
        else
        {
            var reason = ValidateRequest(connection, packet, receivedAt);
            if (packet.MessageType == "SubmitAnswer")
            {
                LobbyProtocol.TryPayload<AnswerRequestDto>(packet, out var answer);
                reply = LobbyProtocol.Encode("AnswerAccepted", SessionId,
                    new AnswerReceiptDto(reason == "None", reason, answer?.QuestionInstanceId ?? Guid.Empty, answer?.LocalSlot ?? 0), packet.MessageId);
            }
            else if (packet.MessageType == "ActivateCard")
            {
                LobbyProtocol.TryPayload<CardRequestDto>(packet, out var card);
                reply = LobbyProtocol.Encode("CardResult", SessionId,
                    new CardReceiptDto(reason == "None", reason, card?.QuestionInstanceId ?? Guid.Empty, card?.CardId ?? Guid.Empty, card?.LocalSlot ?? 0), packet.MessageId);
            }
            else reply = LobbyProtocol.Encode("RequestResult", SessionId, new RequestResultDto(reason == "None", reason), packet.MessageId);
        }
        Guid? boundQuestion = packet.MessageType is "SubmitAnswer" or "ActivateCard" or "MatchVote" &&
            packet.Payload.TryGetProperty("QuestionInstanceId", out var questionId) && questionId.ValueKind == System.Text.Json.JsonValueKind.String && questionId.TryGetGuid(out var parsedQuestion) ? parsedQuestion : null;
        peer.Processed.Add(packet.MessageId, new(json, reply, boundQuestion));
        peer.CachedBytes += Encoding.UTF8.GetByteCount(json) + Encoding.UTF8.GetByteCount(reply);
        var messages = new List<LobbyOutbound> { new(connection, reply) };
        if (before != Snapshot().Revision) messages.AddRange(Broadcast());
        if (matchBefore != _match?.Revision) messages.AddRange(BroadcastMatch());
        return new(messages, false);
    }

    private int[] TakenCharacters() => _lobby.GetSnapshot().Players.Select(p => (int)p.Player.Character!.Value).ToArray();

    private string CheckRoom(PeerRequests peer, LobbyEnvelope packet, string sourceAddress)
    {
        if (packet.SessionId != SessionId) return "WrongSession";
        if (Snapshot().Phase != "Lobby") return "GameStarted";
        if (Snapshot().Players.Length >= _lobby.Capacity) return "RoomFull";
        if (packet.MessageType == "RoomAvailability")
            return LobbyProtocol.TryPayload<RoomAvailabilityRequestDto>(packet, out _) && peer.AdmittedUntil > _clock.Now ? "None" : "AccessExpired";
        if (!LobbyProtocol.TryPayload<RoomAccessRequestDto>(packet, out var request) || request is null ||
            request.AppVersion is not { Length: > 0 and <= 32 } || request.Platform is not ("Windows" or "Android" or "Linux" or "macOS") ||
            !RoomAdmission.ValidPin(request.Pin)) return "MalformedRequest";
        var reason = _admission.Admit(request.Pin, sourceAddress);
        if (reason == "None") peer.AdmittedUntil = _clock.Now + TimeSpan.FromMinutes(2);
        return reason;
    }

    private string Join(long connection, LobbyEnvelope packet, string sourceAddress, out Guid? playerId)
    {
        playerId = null;
        if (packet.SessionId != Guid.Empty || !LobbyProtocol.TryPayload<ClientHelloDto>(packet, out var hello) || hello is null ||
            !LobbyProtocol.ValidName(hello.DisplayName) || hello.AppVersion is not { Length: > 0 and <= 32 } ||
            hello.Platform is not ("Windows" or "Android" or "Linux" or "macOS") || !RoomAdmission.ValidPin(hello.Pin) || hello.CharacterId is { } chosen && !Characters.IsValid(chosen)) return "MalformedRequest";
        if (_lobby.FindPlayer(new(connection)) is not null) return "AlreadyJoined";
        var snapshot = _lobby.GetSnapshot();
        if (snapshot.Phase != GamePhase.Lobby) return "GameStarted";
        if (snapshot.Players.Count >= _lobby.Capacity) return "RoomFull";
        var admission = hello.UsePreflight ? _peers[connection].AdmittedUntil > _clock.Now ? "None" : "AccessExpired" : _admission.Admit(hello.Pin, sourceAddress);
        if (admission != "None") return admission;
        var player = new Player(new(Guid.NewGuid()), hello.DisplayName, new(connection), new(0), (CharacterId?)hello.CharacterId);
        var error = _lobby.Join(player);
        if (error == LobbyError.None) { playerId = player.Id.Value; _controllers.Add(connection, Guid.NewGuid()); }
        return error.ToString();
    }

    private string ValidateRequest(long connection, LobbyEnvelope packet, TimeSpan receivedAt)
    {
        if (_lobby.FindPlayer(new(connection)) is null) return "HandshakeRequired";
        if (packet.SessionId != SessionId) return "WrongSession";
        if (packet.MessageType is "StartGame" or "AdvanceMatch" or "SetTeam") return "NotHost";
        if (packet.MessageType == "MatchVote")
            return LobbyProtocol.TryPayload<MatchVoteDto>(packet, out var vote) && vote is not null ? Vote(connection, vote).ToString() : "MalformedRequest";
        if (packet.MessageType == "AddLocalPlayer")
            return LobbyProtocol.TryPayload<AddLocalPlayerDto>(packet, out var add) && add is not null ? AddLocal(connection, add).ToString() : "MalformedRequest";
        if (packet.MessageType == "RemoveLocalPlayer")
            return LobbyProtocol.TryPayload<RemoveLocalPlayerDto>(packet, out var remove) && remove is { LocalSlot: >= 1 and <= 7 }
                ? _lobby.RemoveLocal(new(connection), new(remove.LocalSlot)).ToString() : "MalformedRequest";
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
        return ready.LocalSlot is < 0 or > 7 ? "MalformedRequest" : _lobby.SetReady(new(connection), ready.Ready, new(ready.LocalSlot)).ToString();
    }

    private LobbyDispatch Reply(long connection, LobbyEnvelope packet, string reason, bool disconnect = false)
    {
        var json = packet.MessageType == "ClientHello"
            ? LobbyProtocol.Encode("ServerHello", SessionId, new ServerHelloDto(false, reason, null, null), packet.MessageId)
            : LobbyProtocol.Encode("RequestResult", SessionId, new RequestResultDto(false, reason), packet.MessageId);
        return new([new(connection, json)], disconnect);
    }

    private sealed record CachedReply(string Request, string Reply, Guid? Question);
    private sealed class PeerRequests
    {
        public TimeSpan AdmittedUntil;
        public TimeSpan WindowStart { get; set; }
        public int MessagesInWindow { get; set; }
        public int Violations { get; set; }
        public int CachedBytes { get; set; }
        public Dictionary<Guid, CachedReply> Processed { get; } = new();
    }
}

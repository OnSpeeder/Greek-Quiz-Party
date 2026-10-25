using Godot;
using QuizParty.Core.Lobby;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Networking;

/// <summary>Reliable ENet adapter. Rules and wire validation live outside the scene.</summary>
public partial class LobbyTransport : Node
{
    public const int DefaultPort = 7777;
    private ENetMultiplayerPeer? _peer;
    private LobbyHost? _host;
    private LobbyClientState _client = new();
    private string _clientName = "";
    private string _clientPin = "";
    private int? _clientCharacter;
    private Guid _prepareSession;
    private bool _joiningPrepared;
    public RoomAccessResultDto? RoomAccess => _client.Access;
    public bool JoinPending => _joiningPrepared;
    public event Action<RoomAccessResultDto>? RoomAccessChanged;
    public LanDiscovery Discovery { get; private set; } = null!;
    public int DiscoveryPort { get; set; } = DiscoveryProtocol.DefaultPort;
    private int _generation;
    private readonly HashSet<long> _handshaken = new();
    private readonly HashSet<long> _closing = new();
    private string? _lastReadyRequest;
    private readonly Dictionary<int, string> _lastAnswers = new();
    private readonly Dictionary<int, string> _lastCards = new();
    private readonly Dictionary<int, int> _hostAnswers = new();
    private long _lastMatchRevision;
    private int _activeSlot;
    private int _lastPresentedSlot;
    private Guid _presentedQuestion;
    private bool? _previousRelay;
    private IReadOnlyList<Core.Questions.QuestionDefinition>? _debugQuestions;
    public int QuestionCount { get; set; } = 1;
    public int QuestionSeconds { get; set; } = 20;
    public bool StrategyEnabled { get; set; } = true;
    public bool AllowSteal { get; set; }
    public HashSet<int> EnabledDifficulties { get; set; } = [1, 2, 3, 4, 5];
    public HashSet<Core.Game.CardKind> EnabledCards { get; set; } = [Core.Game.CardKind.DoublePoints,
        Core.Game.CardKind.FiftyFifty, Core.Game.CardKind.ExtraTime, Core.Game.CardKind.CategorySwap];
    public HashSet<Core.Game.MissionKind> EnabledMissions { get; set; } = Enum.GetValues<Core.Game.MissionKind>().ToHashSet();
    private IReadOnlyList<Core.Questions.QuestionDefinition> _availableContent = [];
    public int SelectedQuestionCapacity => _availableContent.Count(q =>
        (EnabledCategories is null || EnabledCategories.Contains(q.CategoryId)) && EnabledDifficulties.Contains(q.Difficulty));
    public int? DebugStrategySeed { get; set; }
    public int AvailableQuestions { get; private set; }
    public IReadOnlyList<Core.Questions.QuestionCategory> QuestionCategories { get; private set; } = [];
    public HashSet<string>? EnabledCategories { get; set; }

    public void UseSyntheticQuestions(int count)
    {
        if (!OS.IsDebugBuild() || count is not (10 or 20 or 30)) throw new InvalidOperationException("Debug fixture only.");
        _debugQuestions = Enumerable.Range(1, count + 5).Select(i => new Core.Questions.QuestionDefinition(
            $"fixture_{i}", $"ΔΟΚΙΜΗ {i} — επιλέξτε «Σωστό»", ["Σωστό", "Λάθος Α", "Λάθος Β", "Λάθος Γ"],
            0, StrategyEnabled ? new[] { "history", "science", "arts", "sports", "geography" }[(i - 1) % 5] : "fixture",
            i % 5 + 1, "Συνθετική ερώτηση ελέγχου — δεν αποτελεί περιεχόμενο παιχνιδιού.")).ToArray();
        QuestionCount = count;
        GD.Print($"MATCH SYNTHETIC_FIXTURE count={count} debug-only; no reviewed content added");
    }
    public bool PlayMatch { get; set; } = true;
    public event Action<MatchSnapshotDto>? MatchChanged;
    public event Action<string>? MatchInputChanged;
    public MatchSnapshotDto? MatchSnapshot => IsHost && OwnedPlayers.Count == 0 ? _host!.MatchSnapshot() : MatchForSlot(_activeSlot);
    public bool AnswerPending => AnswerPendingForSlot(_activeSlot);
    public bool CardPending => CardPendingForSlot(_activeSlot);
    public event Action<string>? CardInputChanged;
    public int? OwnAnswerIndex => AnswerForSlot(_activeSlot);
    public int ActiveSlot => _activeSlot;
    public event Action? OwnedStateChanged;
    public event Action? LocalPlayerChanged;
    public IReadOnlyList<LobbyPlayerDto> OwnedPlayers => _host is null ? _client.OwnedPlayers : Array.AsReadOnly(
        _host.Snapshot().Players.Where(p => p.ControllerId == _host.HostControllerId).OrderBy(p => p.LocalSlot).ToArray());
    public MatchSnapshotDto? MatchForSlot(int slot) => slot is < 0 or > 7 ? null : _host is not null
        ? OwnedPlayers.FirstOrDefault(p => p.LocalSlot == slot) is { } own ? _host.MatchSnapshot(new Core.Players.PlayerId(own.PlayerId)) : null
        : _client.MatchForSlot(slot).Snapshot;
    public int? AnswerForSlot(int slot) => IsHost ? _hostAnswers.TryGetValue(slot, out var index) ? index : null : _client.MatchForSlot(slot).OwnAnswerIndex;
    public bool AnswerPendingForSlot(int slot) => !IsHost && _client.MatchForSlot(slot).Pending;
    public bool CardPendingForSlot(int slot) => !IsHost && _client.MatchForSlot(slot).CardPending;
    public bool SelectLocalPlayer(int slot)
    {
        if (!OwnedPlayers.Any(p => p.LocalSlot == slot)) return false;
        _activeSlot = slot; LocalPlayerChanged?.Invoke(); PublishMatch(); return true;
    }
    public event Action<LobbySnapshotDto>? SnapshotChanged;
    public event Action<string>? StatusChanged;
    public bool IsHost => _host is not null;
    public Guid? LocalPlayerId => OwnedPlayers.FirstOrDefault(p => p.LocalSlot == _activeSlot)?.PlayerId;
    public LobbySnapshotDto? Snapshot => _host?.Snapshot() ?? _client.Snapshot;
    public int ClientProtocol { get; set; } = LobbyProtocol.Version;

    public override void _Ready()
    {
        Discovery = new LanDiscovery { Name = "Discovery" };
        AddChild(Discovery);
        if (Multiplayer is SceneMultiplayer sceneMultiplayer)
        {
            _previousRelay = sceneMultiplayer.ServerRelay;
            // All game traffic goes through the host. Peer-to-peer relay also
            // sends native disconnect notices into concurrently closing channels.
            sceneMultiplayer.ServerRelay = false;
        }
        Multiplayer.ConnectedToServer += OnConnected;
        Multiplayer.ConnectionFailed += OnConnectionFailed;
        Multiplayer.ServerDisconnected += OnServerDisconnected;
        Multiplayer.PeerConnected += OnPeerConnected;
        Multiplayer.PeerDisconnected += OnPeerDisconnected;
        var poll = new global::Godot.Timer { WaitTime = 0.05, Autostart = true };
        poll.Timeout += () => { if (_host?.PollMatch() == true) BroadcastMatch(); };
        AddChild(poll);
    }

    public Error Host(string roomName, string playerName, int port = DefaultPort, string pin = "", int character = 0, bool hostPlays = true, int maxPlayers = 8)
    {
        if (hostPlays && (!Core.Players.Characters.IsValid(character) || !LobbyProtocol.ValidName(playerName)) || maxPlayers is < 2 or > 8 || !LobbyProtocol.ValidName(roomName) || port is < 1024 or > 65535 || !RoomAdmission.ValidPin(pin))
            return Error.InvalidParameter;
        Core.Questions.QuestionPack pack;
        try { pack = Presentation.QuestionPackContent.Load(); }
        catch (Exception contentError) when (contentError is IOException or System.Text.DecoderFallbackException)
        { GD.PushError($"Content unavailable: {contentError.Message}"); return Error.FileCorrupt; }
        Stop();
        var peer = new ENetMultiplayerPeer();
        // Reserve a few bounded handshake slots so a full room can send RoomFull.
        var error = peer.CreateServer(port, LobbyHost.MaxTransportConnections);
        if (error != Error.Ok) { peer.Dispose(); return error; }
        var questions = _debugQuestions ?? pack.Questions;
        AvailableQuestions = questions.Count;
        _availableContent = questions;
        EnabledCategories = null;
        QuestionCategories = _debugQuestions is null ? pack.Categories : questions.Select(q => q.CategoryId).Distinct()
            .Select(id => new Core.Questions.QuestionCategory(id, "MATCH_TEST_CATEGORY")).ToArray();
        _host = new(roomName, playerName, new MonotonicGameClock(), questions, new(1), pin,
            OS.IsDebugBuild() && DebugStrategySeed is { } seed ? new Core.Randomness.SeededRandomSource(seed) : null, character, hostPlays, maxPlayers);
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        var host = _host;
        Discovery.Advertise(host.Snapshot, port, host.RequiresPin, DiscoveryPort);
        Emit("HostListening");
        Publish();
        return Error.Ok;
    }

    public Error Join(string address, string playerName, int port = DefaultPort, string pin = "", int? character = null)
    {
        if (character is { } chosen && !Core.Players.Characters.IsValid(chosen) || !LobbyProtocol.ValidName(playerName) || string.IsNullOrWhiteSpace(address) || address.Length > 253 ||
            address.Any(char.IsWhiteSpace) || port is < 1024 or > 65535 || !RoomAdmission.ValidPin(pin)) return Error.InvalidParameter;
        Stop();
        _clientName = playerName;
        _clientCharacter = character;
        _clientPin = pin;
        var peer = new ENetMultiplayerPeer();
        var error = peer.CreateClient(address, port);
        if (error != Error.Ok) { peer.Dispose(); return error; }
        _peer = peer;
        Multiplayer.MultiplayerPeer = peer;
        Emit("Connecting");
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree() && _client.PlayerId is null && _client.Access?.Accepted != true)
                Fail("ConnectionTimeout");
        };
        return Error.Ok;
    }

    public Error PrepareRoom(DiscoveredRoom room, string pin)
    {
        var error = Join(room.Address, "Preview", room.Room.GamePort, pin);
        if (error == Error.Ok) _prepareSession = room.Room.SessionId;
        return error;
    }
    public bool JoinPrepared(string name, int character)
    {
        if (_joiningPrepared || _peer is null) return false;
        var json = _client.BeginPreparedHello(name, OS.GetName(), character);
        if (json is null) return false;
        _joiningPrepared = true; RpcId(1, MethodName.ClientMessage, json);
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (generation == _generation && IsInsideTree() && _joiningPrepared && _client.PlayerId is null) Fail("ConnectionTimeout");
        };
        return true;
    }
    public void RefreshRoomAvailability()
    {
        if (!_joiningPrepared && _client.RefreshAvailability() is { } json && _peer is not null)
            RpcId(1, MethodName.ClientMessage, json);
    }

    public void SetReady(bool ready, bool repeatLastRequest = false, int localSlot = 0)
    {
        if (_host is not null)
        {
            Emit(_host.SetHostReady(ready, localSlot).ToString());
            Broadcast();
            return;
        }
        var json = repeatLastRequest ? _lastReadyRequest : _client.CreateReady(ready, localSlot);
        if (json is null) return;
        _lastReadyRequest = json;
        RpcId(1, MethodName.ClientMessage, json);
    }

    public void AddLocalPlayer(string name, int slot, int? character = null)
    {
        if (_host is not null) { Emit(_host.AddHostLocal(name, slot, character).ToString()); Broadcast(); return; }
        var json = _client.CreateAddLocal(name, slot, character); if (json is not null) RpcId(1, MethodName.ClientMessage, json);
    }
    public void RemoveLocalPlayer(int slot)
    {
        if (_host is not null) { Emit(_host.RemoveHostLocal(slot).ToString()); Broadcast(); return; }
        var json = _client.CreateRemoveLocal(slot); if (json is not null) RpcId(1, MethodName.ClientMessage, json);
    }
    public void SetTeamMode(bool enabled)
    {
        if (_host is null) { Emit("NotHost"); return; }
        Emit(_host.SetTeamMode(enabled).ToString()); Broadcast();
    }
    public void AssignTeam(Guid player, int team)
    {
        if (_host is null) { Emit("NotHost"); return; }
        Emit(_host.AssignTeam(player, team).ToString()); Broadcast();
    }

    public void StartGame()
    {
        if (_host is null) { Emit("NotHost"); return; }
        if (EnabledDifficulties.Count == 0) { Emit("InsufficientContent"); return; }
        if (PlayMatch && !_host.ConfigureMatch(new(QuestionCount, QuestionSeconds,
            StrategyEnabled ? new Core.Game.StrategyRules(AllowSteal: AllowSteal)
            { EnabledCards = EnabledCards.ToArray(), EnabledMissions = EnabledMissions.ToArray() } : null,
            EnabledDifficulties), EnabledCategories)) { Emit("InsufficientContent"); return; }
        var result = _host.Start();
        Emit(result.ToString());
        Broadcast();
        if (result == LobbyError.None && PlayMatch && _host.BeginMatch()) BroadcastMatch();
    }

    public void SubmitAnswer(int index, bool repeatLastRequest = false, int confidence = 1, int? localSlot = null)
    {
        var slot = localSlot ?? _activeSlot;
        if (!OwnedPlayers.Any(p => p.LocalSlot == slot)) return;
        if (_host is not null)
        {
            var error = _host.SubmitHostAnswer(index, confidence, slot);
            if (error == Core.Game.SubmissionError.None) _hostAnswers[slot] = index;
            if (slot == _activeSlot) MatchInputChanged?.Invoke(error.ToString());
            BroadcastMatch();
            return;
        }
        var json = repeatLastRequest ? _lastAnswers.GetValueOrDefault(slot) : _client.MatchForSlot(slot).CreateAnswer(index, confidence);
        if (json is null) return;
        _lastAnswers[slot] = json;
        RpcId(1, MethodName.ClientMessage, json);
        if (slot == _activeSlot) MatchInputChanged?.Invoke("Pending");
        OwnedStateChanged?.Invoke();
    }

    public void ActivateCard(Guid card, Guid? target = null, string? category = null, bool repeatLastRequest = false, int? localSlot = null)
    {
        var slot = localSlot ?? _activeSlot;
        if (MatchForSlot(slot) is not { } snapshot) return;
        if (_host is not null)
        {
            var result = _host.ActivateHostCard(new(snapshot.Question.InstanceId, card, target, category, slot));
            GD.Print($"STRATEGY CARD_RECEIPT reason={result}");
            if (slot == _activeSlot) CardInputChanged?.Invoke(result.ToString()); BroadcastMatch(); return;
        }
        var json = repeatLastRequest ? _lastCards.GetValueOrDefault(slot) : _client.MatchForSlot(slot).CreateCard(card, target, category);
        if (json is null) return;
        _lastCards[slot] = json;
        RpcId(1, MethodName.ClientMessage, json); if (slot == _activeSlot) CardInputChanged?.Invoke("Pending");
        OwnedStateChanged?.Invoke();
    }

    public void AdvanceMatch()
    {
        if (_host is null) { MatchInputChanged?.Invoke("NotHost"); return; }
        var result = _host.AdvanceMatch();
        MatchInputChanged?.Invoke(result.ToString());
        BroadcastMatch();
    }

    public void SendAdvanceRequest()
    {
        if (_host is null && Snapshot is { } snapshot)
            RpcId(1, MethodName.ClientMessage, LobbyProtocol.Encode("AdvanceMatch", snapshot.SessionId, new StartRequestDto()));
    }

    // Used by regression to verify rejection at the real host RPC boundary.
    public void SendStartRequest()
    {
        var json = _client.CreateStartRequest();
        if (_host is null && json is not null) RpcId(1, MethodName.ClientMessage, json);
    }

    public void Stop()
    {
        _generation++;
        _host = null;
        _clientPin = ""; _clientCharacter = null; _prepareSession = Guid.Empty; _joiningPrepared = false;
        if (GodotObject.IsInstanceValid(Discovery)) Discovery.Stop();
        _client = new();
        _handshaken.Clear();
        _closing.Clear();
        _lastReadyRequest = null;
        _lastAnswers.Clear(); _lastCards.Clear(); _hostAnswers.Clear();
        _lastMatchRevision = 0;
        _activeSlot = 0; _lastPresentedSlot = 0;
        _presentedQuestion = Guid.Empty;
        if (_peer is not null)
        {
            Multiplayer.MultiplayerPeer = new OfflineMultiplayerPeer();
            _peer.Close();
            _peer.Dispose();
            _peer = null;
        }
    }

    public override void _ExitTree()
    {
        Multiplayer.ConnectedToServer -= OnConnected;
        Multiplayer.ConnectionFailed -= OnConnectionFailed;
        Multiplayer.ServerDisconnected -= OnServerDisconnected;
        Multiplayer.PeerConnected -= OnPeerConnected;
        Multiplayer.PeerDisconnected -= OnPeerDisconnected;
        Stop();
        if (_previousRelay is { } relay && Multiplayer is SceneMultiplayer sceneMultiplayer) sceneMultiplayer.ServerRelay = relay;
    }

    private void OnConnected()
    {
        var json = _prepareSession == Guid.Empty ? _client.BeginHello(_clientName, OS.GetName(), _clientPin, _clientCharacter) :
            _client.BeginAccess(_prepareSession, _clientPin, OS.GetName());
        _clientPin = "";
        // Explicit incompatible header is only selected by the process test flag.
        if (ClientProtocol != LobbyProtocol.Version) json = json.Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", $"\"ProtocolVersion\":{ClientProtocol}", StringComparison.Ordinal);
        RpcId(1, MethodName.ClientMessage, json);
    }

    private void OnPeerConnected(long connection)
    {
        if (_host is null) return;
        var generation = _generation;
        GetTree().CreateTimer(10).Timeout += () =>
        {
            if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree() && !_handshaken.Contains(connection))
            {
                if (_host?.HasRoomAccess(connection) == true) OnPeerConnected(connection);
                else DisconnectPeer(connection);
            }
        };
    }

    private void OnPeerDisconnected(long connection)
    {
        if (_host is null) return;
        _handshaken.Remove(connection);
        _closing.Remove(connection);
        if (_host.Disconnect(connection)) { Emit("PlayerLeft"); Broadcast(); }
    }

    private void OnConnectionFailed() => Fail("ConnectionFailed");
    private void OnServerDisconnected() => Fail("ServerDisconnected");
    private void Fail(string reason) { Stop(); Emit(reason); }
    private void Emit(string reason) { GD.Print($"LOBBY STATUS {reason}"); StatusChanged?.Invoke(reason); }

    private void Publish()
    {
        var snapshot = Snapshot;
        if (snapshot is null) return;
        if (!OwnedPlayers.Any(p => p.LocalSlot == _activeSlot)) _activeSlot = 0;
        GD.Print($"LOBBY SNAPSHOT revision={snapshot.Revision} phase={snapshot.Phase} roster={string.Join('|', snapshot.Players.OrderBy(player => player.DisplayName, StringComparer.Ordinal).Select(player => $"{player.DisplayName}:{player.Ready}"))}");
        SnapshotChanged?.Invoke(snapshot);
        OwnedStateChanged?.Invoke();
    }

    private void Broadcast()
    {
        if (_host is null) return;
        foreach (var message in _host.Broadcast()) SendToConnectedPeer(message);
        Publish();
    }

    private void SendToConnectedPeer(LobbyOutbound message)
    {
        // During a batch of disconnect events the lobby can still contain a peer
        // whose ENet channel has already closed. Never RPC into that channel.
        if (_peer is null || !Multiplayer.GetPeers().Contains((int)message.ConnectionId)) return;
        var peer = _peer.GetPeer((int)message.ConnectionId);
        if (peer.GetState() == ENetPacketPeer.PeerState.Connected && peer.GetChannels() > 0)
            RpcId(message.ConnectionId, MethodName.ServerMessage, message.Json);
    }

    private void PublishMatch()
    {
        var snapshot = MatchSnapshot;
        if (snapshot is null || snapshot.Revision <= _lastMatchRevision && _lastPresentedSlot == _activeSlot) return;
        if (_presentedQuestion != snapshot.Question.InstanceId)
        {
            _presentedQuestion = snapshot.Question.InstanceId;
            _hostAnswers.Clear(); _lastAnswers.Clear(); _lastCards.Clear();
        }
        _lastMatchRevision = snapshot.Revision;
        _lastPresentedSlot = _activeSlot;
        GD.Print($"MATCH SNAPSHOT revision={snapshot.Revision} phase={snapshot.Phase} question={snapshot.Question.InstanceId} scores={string.Join('|', snapshot.Scores.OrderBy(score => score.DisplayName, StringComparer.Ordinal).Select(score => $"{score.DisplayName}:{score.Total}"))}");
        GD.Print($"MATCH PROGRESS number={snapshot.QuestionNumber} total={snapshot.TotalQuestions} round={snapshot.RoundNumber} tie={snapshot.IsTieBreaker}");
        if (snapshot.Teams is { Length: > 0 }) GD.Print($"MATCH TEAMS scores={string.Join('|', snapshot.Teams.Select(t => $"{t.TeamId}:{t.Total}"))} winners={string.Join('|', snapshot.WinningTeams ?? [])}");
        if (snapshot.Phase == "GameOver") GD.Print($"MATCH FINAL winners={string.Join('|', snapshot.Winners.Order())} stats={string.Join('|',
            snapshot.Statistics.OrderBy(s => s.PlayerId).Select(s => $"{s.PlayerId}:{s.Correct}/{s.Wrong}/{s.Unanswered}/{s.BestStreak}/{s.ResponseTicks}/{s.Responses}"))}");
        MatchChanged?.Invoke(snapshot);
    }

    private void BroadcastMatch()
    {
        if (_host is null) return;
        foreach (var message in _host.BroadcastMatch()) SendToConnectedPeer(message);
        PublishMatch();
        OwnedStateChanged?.Invoke();
    }

    private void DisconnectPeer(long connection)
    {
        if (_peer?.GetConnectionStatus() == MultiplayerPeer.ConnectionStatus.Connected && Multiplayer.GetPeers().Contains((int)connection))
            _peer.DisconnectPeer((int)connection);
        OnPeerDisconnected(connection);
    }

    [Rpc(MultiplayerApi.RpcMode.AnyPeer, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ClientMessage(string json)
    {
        if (_host is null) return;
        var sender = Multiplayer.GetRemoteSenderId();
        if (_closing.Contains(sender)) return;
        var address = _peer?.GetPeer((int)sender).GetRemoteAddress() ?? "unknown";
        var dispatch = _host.Handle(sender, json, address);
        foreach (var message in dispatch.Messages) SendToConnectedPeer(message);
        if (_host.GetPlayers().Any(player => player.ConnectionId?.Value == sender)) _handshaken.Add(sender);
        Publish();
        PublishMatch();
        if (dispatch.DisconnectSender)
        {
            _closing.Add(sender);
            // Allow the reliable rejection receipt to flush before closing.
            var generation = _generation;
            GetTree().CreateTimer(0.25).Timeout += () =>
            {
                if (generation == _generation && GodotObject.IsInstanceValid(this) && IsInsideTree()) DisconnectPeer(sender);
            };
        }
    }

    [Rpc(TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
    private void ServerMessage(string json)
    {
        if (_host is not null || Multiplayer.GetRemoteSenderId() != 1) return;
        var update = _client.Apply(json);
        if (update == LobbyClientUpdate.RoomAccess)
        {
            if (_client.Access is not { Accepted: true } access) { Fail(_client.LastReason); return; }
            RoomAccessChanged?.Invoke(access); return;
        }
        if (update == LobbyClientUpdate.Rejected)
        {
            _joiningPrepared = false;
            if (_client.LastReason == "CharacterTaken" && _client.Access is { Accepted: true } access)
            { RoomAccessChanged?.Invoke(access); Emit("CharacterTaken"); return; }
            Fail(_client.LastReason); return;
        }
        if (update is LobbyClientUpdate.Joined or LobbyClientUpdate.Snapshot) Publish();
        if (update == LobbyClientUpdate.Joined) { _joiningPrepared = false; Emit("Joined"); }
        if (update == LobbyClientUpdate.RequestResult) Emit(_client.LastReason);
        if (update == LobbyClientUpdate.MatchSnapshot) { PublishMatch(); OwnedStateChanged?.Invoke(); }
        if (update == LobbyClientUpdate.AnswerReceipt)
        {
            var state = _client.MatchForSlot(_client.LastMatchSlot);
            GD.Print($"MATCH RECEIPT reason={state.LastReason}");
            if (_client.LastMatchSlot == _activeSlot) MatchInputChanged?.Invoke(state.LastReason);
            OwnedStateChanged?.Invoke();
        }
        if (update == LobbyClientUpdate.CardReceipt)
        {
            var state = _client.MatchForSlot(_client.LastMatchSlot);
            GD.Print($"STRATEGY CARD_RECEIPT reason={state.CardReason}");
            if (_client.LastMatchSlot == _activeSlot) CardInputChanged?.Invoke(state.CardReason);
            OwnedStateChanged?.Invoke();
        }
    }
}

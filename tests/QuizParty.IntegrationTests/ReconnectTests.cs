using QuizParty.Core.Questions;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class ReconnectTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100); }

    [Fact]
    public void AbandonReservationRevokesAllSeatsAndIsSafeToRetry()
    {
        var clock = new Clock();
        var question = new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact");
        var host = new LobbyHost("Room", "Host", clock, new[] { question }, new(1));
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginHello("Phone", "Android")).Messages[0].Json);
        foreach (var packet in host.Handle(2, client.CreateAddLocal("Second", 1)!).Messages.Where(p => p.ConnectionId == 2)) client.Apply(packet.Json);
        host.Handle(2, client.CreateReady(true)!); host.Handle(2, client.CreateReady(true, 1)!);
        host.SetHostReady(true); host.Start(); Assert.True(host.BeginMatch());
        var token = Assert.IsType<string>(client.ReconnectToken);
        var abandoned = LobbyProtocol.Encode("AbandonReservation", host.SessionId, new AbandonReservationDto(token));
        Assert.Contains("StillConnected", host.Handle(3, abandoned).Messages[0].Json);
        Assert.True(host.Suspend(2));
        var invalid = LobbyProtocol.Encode("AbandonReservation", host.SessionId, new AbandonReservationDto(new string('A', 64)));
        Assert.Contains("ReconnectUnavailable", host.Handle(4, invalid).Messages[0].Json);
        var accepted = LobbyProtocol.Encode("AbandonReservation", host.SessionId, new AbandonReservationDto(token));
        Assert.Contains("\"Accepted\":true", host.Handle(4, accepted).Messages[0].Json);
        Assert.Single(host.Snapshot().Players);
        Assert.Equal(3, host.MatchSnapshot()!.Scores.Length);
        var retry = LobbyProtocol.Encode("AbandonReservation", host.SessionId, new AbandonReservationDto(token));
        Assert.Contains("\"Accepted\":true", host.Handle(5, retry).Messages[0].Json);
        var reclaim = LobbyProtocol.Encode("Reconnect", host.SessionId, new ReconnectRequestDto(token));
        Assert.Contains("ReconnectUnavailable", host.Handle(6, reclaim).Messages[0].Json);
    }

    [Fact]
    public void FreshClientRestoresReservationWithoutPersistingOldPrivateSnapshots()
    {
        var clock = new Clock();
        var question = new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact");
        var host = new LobbyHost("Room", "Host", clock, new[] { question }, new(1));
        var original = new LobbyClientState();
        original.Apply(host.Handle(2, original.BeginHello("Phone", "Android")).Messages[0].Json);
        host.Handle(2, original.CreateReady(true)!); host.SetHostReady(true); host.Start(); Assert.True(host.BeginMatch());
        Assert.True(host.Suspend(2));
        var restored = new LobbyClientState();
        Assert.False(restored.RestoreReconnect(Guid.Empty, original.PlayerId!.Value, original.ControllerId!.Value, original.ReconnectToken!));
        Assert.True(restored.RestoreReconnect(host.SessionId, original.PlayerId.Value, original.ControllerId.Value, original.ReconnectToken!));
        Assert.Null(restored.Snapshot); Assert.Null(restored.Match.Snapshot);
        var packets = host.Handle(3, restored.BeginReconnect()!).Messages.Where(p => p.ConnectionId == 3).ToArray();
        Assert.Equal(LobbyClientUpdate.Reconnected, restored.Apply(packets[0].Json));
        foreach (var packet in packets.Skip(1)) restored.Apply(packet.Json);
        Assert.Equal(original.PlayerId, restored.PlayerId);
        Assert.Equal("QuestionActive", restored.Match.Snapshot!.Phase);
    }

    [Fact]
    public void ReconnectRestoresAllOwnedSeatsAndAcceptedAnswerWithoutExtendingDeadline()
    {
        var clock = new Clock();
        var questions = new[] { new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact") };
        var host = new LobbyHost("Room", "Host", clock, questions, new(1, 20));
        var client = new LobbyClientState();
        void Deliver(IEnumerable<LobbyOutbound> packets, long connection)
        { foreach (var packet in packets.Where(p => p.ConnectionId == connection)) client.Apply(packet.Json); }
        Deliver(host.Handle(2, client.BeginHello("Phone", "Android")).Messages, 2);
        var player = client.PlayerId;
        Deliver(host.Handle(2, client.CreateAddLocal("Second", 1)!).Messages, 2);
        foreach (var slot in new[] { 0, 1 }) Deliver(host.Handle(2, client.CreateReady(true, slot)!).Messages, 2);
        host.SetHostReady(true); host.Start(); Assert.True(host.BeginMatch());
        Deliver(host.Broadcast(), 2); Deliver(host.BroadcastMatch(), 2);
        var question = client.Match.Snapshot!.Question;
        Deliver(host.Handle(2, client.Match.CreateAnswer(0)!).Messages, 2);
        Assert.True(host.Suspend(2));
        Assert.Equal(3, host.Snapshot().Players.Length);
        var stale = LobbyProtocol.Encode("SubmitAnswer", host.SessionId, new AnswerRequestDto(question.InstanceId, 1, 1, 1));
        Assert.Contains("HandshakeRequired", host.Handle(2, stale).Messages[0].Json);
        var forged = LobbyProtocol.Encode("Reconnect", host.SessionId, new ReconnectRequestDto(new string('A', 64)));
        Assert.Contains("ReconnectUnavailable", host.Handle(3, forged).Messages[0].Json);
        clock.Now += TimeSpan.FromSeconds(5);
        var request = client.BeginReconnect()!;
        var response = host.Handle(4, request);
        Deliver(response.Messages, 4);
        Assert.Equal(player, client.PlayerId);
        Assert.Equal(2, client.OwnedPlayers.Count);
        Assert.Contains(player!.Value, client.Match.Snapshot!.AnsweredPlayers!);
        Assert.Null(client.Match.CreateAnswer(1));
        Assert.Equal(question.DeadlineTicks, client.MatchForSlot(1).Snapshot!.Private?.DeadlineTicks ?? client.MatchForSlot(1).Snapshot!.Question.DeadlineTicks);
        Assert.True(client.Match.Snapshot.IsResuming);
        clock.Now += TimeSpan.FromSeconds(5); Assert.True(host.PollMatch()); Deliver(host.BroadcastMatch(), 4);
        Assert.NotNull(client.MatchForSlot(1).CreateAnswer(1));
        Assert.Contains("StillConnected", host.Handle(5, request).Messages[0].Json);
    }

    [Fact]
    public void ReservationSurvivesLongDisconnectWhileMatchIsInProgress()
    {
        var clock = new Clock();
        var question = new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact");
        var host = new LobbyHost("Room", "Host", clock, new[] { question }, new(1));
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginHello("Phone", "Android")).Messages[0].Json);
        host.Handle(2, client.CreateReady(true)!); host.SetHostReady(true); host.Start(); Assert.True(host.BeginMatch());
        Assert.True(host.Suspend(2)); clock.Now += TimeSpan.FromSeconds(60);
        Assert.False(host.ExpireReservations()); Assert.Equal(2, host.Snapshot().Players.Length);
        clock.Now += TimeSpan.FromHours(8);
        Assert.Contains("\"Accepted\":true", host.Handle(3, client.BeginReconnect()!).Messages[0].Json);
    }

    [Fact]
    public void FinalSnapshotDoesNotChangeWhenADeviceLeaves()
    {
        var clock = new Clock();
        var question = new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact");
        var host = new LobbyHost("Room", "Host", clock, new[] { question }, new(1));
        var client = new LobbyClientState();
        client.Apply(host.Handle(2, client.BeginHello("Phone", "Android")).Messages[0].Json);
        host.Handle(2, client.CreateReady(true)!); host.SetHostReady(true); host.Start(); Assert.True(host.BeginMatch());
        host.SubmitHostAnswer(0);
        var instance = host.MatchSnapshot()!.Question.InstanceId;
        host.Handle(2, LobbyProtocol.Encode("SubmitAnswer", host.SessionId, new AnswerRequestDto(instance, 1, 1, 0)));
        host.PollMatch(); host.AdvanceMatch(); host.AdvanceMatch();
        Assert.Equal("GameOver", host.MatchSnapshot()!.Phase);
        var revision = host.MatchSnapshot()!.Revision;
        Assert.True(host.Suspend(2));
        Assert.Equal(revision, host.MatchSnapshot()!.Revision);
    }

    [Fact]
    public void OnlyConnectedOwnedSeatsCanVoteAndAResumedDeviceCanStillReclaim()
    {
        var clock = new Clock();
        var question = new QuestionDefinition("one", "Question", ["yes", "no", "other", "last"], 0, "test", 1, "Fact");
        var host = new LobbyHost("Room", "", clock, new[] { question }, new(1, 0), hostPlays: false);
        var first = new LobbyClientState(); var second = new LobbyClientState(); var missing = new LobbyClientState();
        foreach (var (connection, state, name) in new[] { (2, first, "First"), (3, second, "Second"), (4, missing, "Missing") })
        { state.Apply(host.Handle(connection, state.BeginHello(name, "Android")).Messages[0].Json); host.Handle(connection, state.CreateReady(true)!); }
        host.Start(); Assert.True(host.BeginMatch()); Assert.True(host.Suspend(4));
        var paused = host.MatchSnapshot()!; Assert.True(paused.IsPaused);
        string Vote(Guid id, int slot = 0) => LobbyProtocol.Encode("ResumeVote", host.SessionId, new ResumeVoteDto(id, slot));
        Assert.Contains("InvalidTransition", host.Handle(2, Vote(Guid.NewGuid())).Messages[0].Json);
        Assert.Contains("InvalidTransition", host.Handle(2, Vote(paused.PauseId!.Value, 1)).Messages[0].Json);
        host.Handle(2, Vote(paused.PauseId.Value)); Assert.True(host.MatchSnapshot()!.IsPaused);
        host.Handle(3, Vote(paused.PauseId.Value)); Assert.False(host.MatchSnapshot()!.IsPaused);
        clock.Now += TimeSpan.FromHours(3);
        Assert.Contains("\"Accepted\":true", host.Handle(5, missing.BeginReconnect()!).Messages[0].Json);
        Assert.False(host.MatchSnapshot()!.IsPaused);
    }
}

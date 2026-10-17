using System.Text.Json;
using QuizParty.Core.Game;
using QuizParty.Core.Lobby;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class MatchProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100); }
    private sealed class Fixture
    {
        public Clock Clock { get; } = new();
        public LobbyHost Host { get; }
        public LobbyClientState Client { get; } = new();
        public Fixture()
        {
            Host = new("Room", "Host", Clock);
            Deliver(Host.Handle(2, Client.BeginHello("Phone", "Android")));
            Deliver(Host.Handle(2, Client.CreateReady(true)!));
            Assert.Equal(LobbyError.None, Host.Start());
            foreach (var packet in Host.Broadcast()) Client.Apply(packet.Json);
            Assert.True(Host.BeginMatch());
            Sync();
        }
        public void Sync() { foreach (var packet in Host.BroadcastMatch()) Client.Apply(packet.Json); }
        public void Deliver(LobbyDispatch dispatch) { foreach (var packet in dispatch.Messages.Where(packet => packet.ConnectionId == 2)) Client.Apply(packet.Json); }
        public string Answer(int index, Guid? question = null, int confidence = 1) => LobbyProtocol.Encode("SubmitAnswer", Host.SessionId,
            new AnswerRequestDto(question ?? Host.MatchSnapshot()!.Question.InstanceId, index, confidence));
        public int Correct => Array.IndexOf(Host.MatchSnapshot()!.Question.Answers, "Αθήνα");
    }

    private static LobbyEnvelope Decode(string json) { Assert.True(LobbyProtocol.TryDecode(json, out var packet)); return packet!; }
    private static AnswerReceiptDto Receipt(LobbyDispatch dispatch)
    {
        Assert.True(LobbyProtocol.TryPayload<AnswerReceiptDto>(Decode(dispatch.Messages[0].Json), out var receipt));
        return receipt!;
    }

    [Fact]
    public void FullWireMatchKeepsCorrectnessPrivateUntilRevealAndClientsUseHostScores()
    {
        var fixture = new Fixture();
        var host = fixture.Host;
        var question = host.MatchSnapshot()!.Question;
        foreach (var packet in host.BroadcastMatch())
        {
            Assert.DoesNotContain("CorrectAnswerIndex", packet.Json);
            Assert.DoesNotContain("Explanation", packet.Json);
            Assert.DoesNotContain("IsCorrect", packet.Json);
        }
        fixture.Clock.Now += TimeSpan.FromSeconds(10);
        var request = fixture.Client.Match.CreateAnswer(fixture.Correct)!;
        Assert.True(fixture.Client.Match.Pending);
        var reply = host.Handle(2, request);
        Assert.True(Receipt(reply).Accepted);
        Assert.DoesNotContain("Correct", reply.Messages[0].Json);
        fixture.Deliver(reply);
        Assert.False(fixture.Client.Match.Pending);
        Assert.Equal(fixture.Correct, fixture.Client.Match.OwnAnswerIndex);
        Assert.Null(fixture.Client.Match.CreateAnswer(fixture.Correct));
        Assert.Equal(SubmissionError.None, host.SubmitHostAnswer((fixture.Correct + 1) % 4));
        fixture.Sync();
        Assert.Equal("QuestionLocked", fixture.Client.Match.Snapshot!.Phase);
        Assert.Null(fixture.Client.Match.Snapshot.Reveal);
        Assert.True(host.PollMatch());
        fixture.Sync();
        Assert.Equal("AnswerReveal", fixture.Client.Match.Snapshot!.Phase);
        Assert.Equal(750, fixture.Client.Match.Snapshot.Scores.Single(score => score.DisplayName == "Phone").Total);
        Assert.Equal(0, fixture.Client.Match.Snapshot.Scores.Single(score => score.DisplayName == "Host").Total);
        Assert.Equal(GameError.None, host.AdvanceMatch());
        fixture.Sync();
        Assert.Equal("Scoreboard", fixture.Client.Match.Snapshot.Phase);
        Assert.Equal(GameError.None, host.AdvanceMatch());
        fixture.Sync();
        Assert.Equal("GameOver", fixture.Client.Match.Snapshot.Phase);
        Assert.Equal(question.InstanceId, fixture.Client.Match.Snapshot.Question.InstanceId);
        Assert.Equal(JsonSerializer.Serialize(host.MatchSnapshot()!), JsonSerializer.Serialize(fixture.Client.Match.Snapshot));
    }

    [Theory]
    [InlineData(-1, 1, "InvalidAnswerIndex")]
    [InlineData(4, 1, "InvalidAnswerIndex")]
    [InlineData(0, 0, "InvalidConfidence")]
    [InlineData(0, 3, "InvalidConfidence")]
    public void InvalidAnswersAreRejectedWithoutConsumingPlayerSlot(int index, int confidence, string reason)
    {
        var fixture = new Fixture();
        Assert.Equal(reason, Receipt(fixture.Host.Handle(2, fixture.Answer(index, confidence: confidence))).Reason);
        Assert.Equal(0, fixture.Host.MatchSnapshot()!.AcceptedAnswerCount);
        Assert.True(Receipt(fixture.Host.Handle(2, fixture.Answer(fixture.Correct))).Accepted);
    }

    [Fact]
    public void DuplicateReceiptIsStableAndChangedOrStaleOrSpoofedAnswersNeverMutate()
    {
        var fixture = new Fixture();
        Assert.Equal("StaleQuestion", Receipt(fixture.Host.Handle(2, fixture.Answer(0, Guid.NewGuid()))).Reason);
        var spoof = LobbyProtocol.Encode("SubmitAnswer", fixture.Host.SessionId, new
            { QuestionInstanceId = fixture.Host.MatchSnapshot()!.Question.InstanceId, AnswerIndex = 0, Confidence = 1, PlayerId = Guid.NewGuid() });
        Assert.Equal("MalformedRequest", Receipt(fixture.Host.Handle(2, spoof)).Reason);
        var request = fixture.Answer(fixture.Correct);
        var original = fixture.Host.Handle(2, request);
        var revision = fixture.Host.MatchSnapshot()!.Revision;
        fixture.Clock.Now += TimeSpan.FromSeconds(2);
        Assert.Equal(original.Messages[0], Assert.Single(fixture.Host.Handle(2, request).Messages));
        Assert.Equal(revision, fixture.Host.MatchSnapshot()!.Revision);
        Assert.Equal("AlreadyAnswered", Receipt(fixture.Host.Handle(2, fixture.Answer((fixture.Correct + 1) % 4))).Reason);
        Assert.Equal(1, fixture.Host.MatchSnapshot()!.AcceptedAnswerCount);
    }

    [Fact]
    public void HostReceiptDeadlineLateAndDisconnectedOrForeignSessionsAreValidated()
    {
        var fixture = new Fixture();
        fixture.Clock.Now += TimeSpan.FromSeconds(20);
        Assert.True(Receipt(fixture.Host.Handle(2, fixture.Answer(fixture.Correct))).Accepted);
        Assert.False(fixture.Host.PollMatch());
        fixture.Clock.Now += TimeSpan.FromTicks(1);
        Assert.Equal(SubmissionError.Late, fixture.Host.SubmitHostAnswer(fixture.Correct));
        Assert.True(fixture.Host.PollMatch());
        Assert.True(fixture.Host.PollMatch());
        Assert.Equal(500, fixture.Host.MatchSnapshot()!.Scores.Single(score => score.DisplayName == "Phone").Total);
        var foreign = LobbyProtocol.Encode("SubmitAnswer", Guid.NewGuid(), new AnswerRequestDto(Guid.NewGuid(), 0, 1));
        Assert.Equal("WrongSession", Receipt(fixture.Host.Handle(2, foreign)).Reason);
        fixture.Host.Disconnect(2);
        Assert.Equal("HandshakeRequired", Receipt(fixture.Host.Handle(2, fixture.Answer(0))).Reason);
    }

    [Fact]
    public void ClientCannotAdvanceAndOldProtocolCannotJoin()
    {
        var fixture = new Fixture();
        var rejected = fixture.Host.Handle(2, LobbyProtocol.Encode("AdvanceMatch", fixture.Host.SessionId, new StartRequestDto()));
        Assert.True(LobbyProtocol.TryPayload<RequestResultDto>(Decode(rejected.Messages[0].Json), out var result));
        Assert.Equal("NotHost", result!.Reason);
        var old = LobbyProtocol.Encode("ClientHello", Guid.Empty, new ClientHelloDto("0.1.0", "Old", "Windows"))
            .Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", "\"ProtocolVersion\":1", StringComparison.Ordinal);
        var dispatch = fixture.Host.Handle(3, old);
        Assert.True(dispatch.DisconnectSender);
        Assert.True(LobbyProtocol.TryPayload<ServerHelloDto>(Decode(dispatch.Messages[0].Json), out var hello));
        Assert.Equal("IncompatibleVersion", hello!.Reason);
    }

    [Fact]
    public void ClientRejectsPrematureRevealRollbackWrongSessionAndMutableSnapshots()
    {
        var fixture = new Fixture();
        var valid = fixture.Host.MatchSnapshot()!;
        var premature = valid with { Revision = 999, Reveal = new(0, "secret", []) };
        Assert.Equal(LobbyClientUpdate.Ignored, fixture.Client.Apply(LobbyProtocol.Encode("MatchSnapshot", fixture.Host.SessionId, premature)));
        var foreign = valid with { SessionId = Guid.NewGuid(), Revision = 999 };
        Assert.Equal(LobbyClientUpdate.Ignored, fixture.Client.Apply(LobbyProtocol.Encode("MatchSnapshot", foreign.SessionId, foreign)));
        var mutated = fixture.Client.Match.Snapshot!;
        mutated.Question.Answers[0] = "tampered";
        Assert.DoesNotContain("tampered", fixture.Client.Match.Snapshot!.Question.Answers);
        fixture.Clock.Now += TimeSpan.FromSeconds(21);
        fixture.Host.PollMatch();
        fixture.Host.PollMatch();
        fixture.Sync();
        Assert.Equal(LobbyClientUpdate.Ignored, fixture.Client.Apply(LobbyProtocol.Encode("MatchSnapshot", fixture.Host.SessionId, valid with { Revision = 999 })));
    }
}

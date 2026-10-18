using System.Text.Json;
using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class MixedTeamProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(10); }
    private sealed class FixedRandom(int value = 0) : IRandomSource { public int Next(int upper) => Math.Min(value, upper - 1); }
    private sealed class Fixture
    {
        public Clock Clock { get; } = new();
        public LobbyHost Host { get; }
        public LobbyClientState Client { get; } = new();
        public int Requests { get; private set; }
        public Fixture(int hostSlots = 2, int clientSlots = 2, int count = 1, bool strategy = false, int random = 0)
        {
            var questions = Enumerable.Range(0, count + 2).Select(i => new QuestionDefinition($"q{i}", $"Test {i}",
                ["yes", "no", "other", "last"], 0, "history", 5, "Synthetic only")).ToArray();
            Host = new("Room", "Host", Clock, questions, new(count, strategy: strategy ? new StrategyRules() : null), random: new FixedRandom(random));
            for (var slot = 1; slot < hostSlots; slot++) { Assert.Equal(Core.Lobby.LobbyError.None, Host.AddHostLocal($"Host{slot}", slot)); Host.SetHostReady(true, slot); }
            Send(Client.BeginHello("Phone", "Android"));
            for (var slot = 1; slot < clientSlots; slot++) Send(Client.CreateAddLocal($"Phone{slot}", slot)!);
            foreach (var own in Client.OwnedPlayers) Send(Client.CreateReady(true, own.LocalSlot)!);
            Host.SetTeamMode(true); Deliver(Host.Broadcast());
        }
        public LobbyDispatch Send(string json)
        {
            Requests++; var dispatch = Host.Handle(2, json); Deliver(dispatch.Messages); Assert.False(dispatch.DisconnectSender); return dispatch;
        }
        public void Deliver(IEnumerable<LobbyOutbound> messages) { foreach (var p in messages.Where(m => m.ConnectionId == 2)) Client.Apply(p.Json); }
        public void Sync() => Deliver(Host.BroadcastMatch());
        public void Start() { Assert.Equal(Core.Lobby.LobbyError.None, Host.Start()); Deliver(Host.Broadcast()); Assert.True(Host.BeginMatch()); Sync(); }
        public void Advance() { Host.AdvanceMatch(); Sync(); }
        public int Correct => Array.IndexOf(Host.MatchSnapshot()!.Question.Answers, "yes");
    }

    [Theory]
    [InlineData(1, 1)] [InlineData(2, 3)] [InlineData(4, 4)] [InlineData(1, 7)]
    public void MultipleSlotsHaveIndependentAnswersAndOnlyOneLobbyBroadcastPerConnection(int hostCount, int phoneCount)
    {
        var f = new Fixture(hostCount, phoneCount);
        Assert.Equal(phoneCount, f.Client.OwnedPlayers.Count); Assert.Single(f.Host.Broadcast());
        Assert.Equal(hostCount + phoneCount, f.Host.Snapshot().Players.Length);
        Assert.Equal(2, f.Host.Snapshot().Players.Select(p => p.ControllerId).Distinct().Count());
        Assert.DoesNotContain("ConnectionId", Assert.Single(f.Host.Broadcast()).Json);
        f.Start(); Assert.Equal(phoneCount, f.Host.BroadcastMatch().Count);
        var first = f.Client.Match.CreateAnswer(f.Correct)!;
        var wrongSlot = LobbyProtocol.Encode("AnswerAccepted", f.Host.SessionId,
            new AnswerReceiptDto(true, "None", f.Host.MatchSnapshot()!.Question.InstanceId, 7),
            JsonSerializer.Deserialize<LobbyEnvelope>(first)!.MessageId);
        Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(wrongSlot)); Assert.Null(f.Client.Match.OwnAnswerIndex);
        f.Send(first); Assert.Equal(f.Correct, f.Client.Match.OwnAnswerIndex);
        foreach (var own in f.Client.OwnedPlayers.Skip(1))
        { Assert.Null(f.Client.MatchForSlot(own.LocalSlot).OwnAnswerIndex); f.Send(f.Client.MatchForSlot(own.LocalSlot).CreateAnswer(f.Correct)!); }
        foreach (var host in f.Host.GetPlayers().Where(p => p.ConnectionId?.Value == 1)) Assert.Equal(SubmissionError.None, f.Host.SubmitHostAnswer(f.Correct, localSlot: host.LocalSlot!.Value.Value));
        f.Sync(); f.Host.PollMatch(); f.Sync(); f.Advance(); f.Advance();
        while (f.Host.MatchSnapshot()!.Phase != "GameOver") // Resolve any exact team tie using the finite reserve.
        {
            f.Advance(); f.Clock.Now += TimeSpan.FromSeconds(21); f.Host.PollMatch(); f.Host.PollMatch(); f.Sync(); f.Advance(); f.Advance();
        }
        foreach (var own in f.Client.OwnedPlayers)
        {
            var match = f.Client.MatchForSlot(own.LocalSlot).Snapshot!; Assert.Equal("GameOver", match.Phase);
            Assert.Equal(JsonSerializer.Serialize(f.Host.MatchSnapshot()!.Teams), JsonSerializer.Serialize(match.Teams));
            Assert.Equal(f.Host.MatchSnapshot()!.WinningTeams, match.WinningTeams);
        }
    }

    [Fact]
    public void SlotsCannotSpoofForeignActorsOrChangeTeamsAndDisconnectRevokesEverySlot()
    {
        var f = new Fixture(); f.Start();
        var question = f.Host.MatchSnapshot()!.Question.InstanceId;
        foreach (var slot in new[] { -1, 2, 8, int.MaxValue })
        {
            var rejected = f.Send(LobbyProtocol.Encode("SubmitAnswer", f.Host.SessionId, new AnswerRequestDto(question, f.Correct, 1, slot)));
            Assert.Contains("UnknownPlayer", rejected.Messages[0].Json);
        }
        Assert.Contains("NotHost", f.Send(LobbyProtocol.Encode("SetTeam", f.Host.SessionId, new { PlayerId = f.Client.PlayerId, TeamId = 2 })).Messages[0].Json);
        var spoof = f.Send(LobbyProtocol.Encode("SubmitAnswer", f.Host.SessionId,
            new { QuestionInstanceId = question, AnswerIndex = f.Correct, Confidence = 1, LocalSlot = 0, PlayerId = f.Host.Snapshot().Players[0].PlayerId }));
        Assert.Contains("MalformedRequest", spoof.Messages[0].Json); Assert.Equal(0, f.Host.MatchSnapshot()!.AcceptedAnswerCount);
        Assert.True(f.Host.Disconnect(2)); Assert.Equal(2, f.Host.GetPlayers().Count);
        Assert.False(f.Host.Disconnect(1)); Assert.Equal(2, f.Host.Snapshot().Players.Length);
        foreach (var slot in new[] { 0, 1 }) Assert.Contains("HandshakeRequired", f.Host.Handle(2,
            LobbyProtocol.Encode("SubmitAnswer", f.Host.SessionId, new AnswerRequestDto(question, f.Correct, 1, slot))).Messages[0].Json);
    }

    [Fact]
    public void ThirtyQuestionEightPlayerWireMatchKeepsPrivateHandsAndSupportsMoreThan256Requests()
    {
        var f = new Fixture(2, 6, 30, strategy: true); f.Start();
        for (var q = 0; q < 30; q++)
        {
            f.Clock.Now += TimeSpan.FromSeconds(1);
            foreach (var own in f.Client.OwnedPlayers)
            {
                var state = f.Client.MatchForSlot(own.LocalSlot); var view = state.Snapshot!;
                Assert.Equal(own.LocalSlot, view.LocalSlot); Assert.Equal(own.PlayerId, view.Private!.PlayerId);
                Assert.Empty(view.FinalStrategy!); Assert.DoesNotContain("CorrectAnswerIndex", f.Host.BroadcastMatch().First(p => JsonSerializer.Deserialize<LobbyEnvelope>(p.Json)!.Payload.GetProperty("LocalSlot").GetInt32() == own.LocalSlot).Json);
                var card = view.Private.Hand.FirstOrDefault();
                if (card is not null)
                {
                    var other = f.Client.OwnedPlayers.First(p => p.LocalSlot != own.LocalSlot);
                    Assert.DoesNotContain(card.Id, f.Client.MatchForSlot(other.LocalSlot).Snapshot!.Private!.Hand.Select(c => c.Id));
                    var request = state.CreateCard(card.Id)!; var receipt = f.Send(request).Messages[0];
                    f.Send(request); Assert.False(state.CardPending); Assert.Equal("None", state.CardReason);
                    Assert.Equal(receipt.Json, f.Host.Handle(2, request).Messages[0].Json);
                }
                f.Send(state.CreateAnswer(f.Correct)!);
            }
            foreach (var own in f.Host.GetPlayers().Where(p => p.ConnectionId?.Value == 1))
                f.Host.SubmitHostAnswer(f.Correct, own.LocalSlot!.Value.Value == 0 ? 3 : 1, own.LocalSlot.Value.Value);
            f.Sync(); f.Host.PollMatch(); f.Sync(); f.Advance(); f.Advance();
            if (f.Host.MatchSnapshot()!.Phase == "RoundEnd") f.Advance();
        }
        Assert.True(f.Requests > 256); Assert.Equal("GameOver", f.Client.Match.Snapshot!.Phase);
        Assert.Equal(f.Host.MatchSnapshot()!.WinningTeams, f.Client.Match.Snapshot.WinningTeams);
        foreach (var own in f.Client.OwnedPlayers)
        {
            var final = f.Client.MatchForSlot(own.LocalSlot).Snapshot!;
            Assert.Equal(8, final.FinalStrategy!.Length); Assert.Equal(8, final.Statistics.Length);
            Assert.Equal(JsonSerializer.Serialize(f.Host.MatchSnapshot()!.Scores), JsonSerializer.Serialize(final.Scores));
        }
        Assert.All(f.Host.BroadcastMatch(), p => Assert.True(LobbyProtocol.TryDecode(p.Json, out _)));
    }

    [Fact]
    public void AddedRemovedSlotsAndMalformedControllerGroupsDoNotReusePrivatePresentation()
    {
        var f = new Fixture(); var old = f.Client.OwnedPlayers.Single(p => p.LocalSlot == 1).PlayerId;
        f.Send(f.Client.CreateRemoveLocal(1)!); Assert.Single(f.Client.OwnedPlayers);
        f.Send(f.Client.CreateAddLocal("Replacement", 1)!); Assert.NotEqual(old, f.Client.OwnedPlayers.Single(p => p.LocalSlot == 1).PlayerId);
        Assert.Null(f.Client.MatchForSlot(1).Snapshot); Assert.Null(f.Client.CreateRemoveLocal(0));
        var snapshot = f.Host.Snapshot();
        var bad = snapshot with { Revision = snapshot.Revision + 1, Players = snapshot.Players.Select(p => p.LocalSlot == 1 ? p with { LocalSlot = 0 } : p).ToArray() };
        Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(LobbyProtocol.Encode("LobbySnapshot", f.Host.SessionId, bad)));
        Assert.Equal(2, f.Client.OwnedPlayers.Count);
    }

    [Fact]
    public void TeamMembershipCopiesCannotMutateClientState()
    {
        var f = new Fixture(); f.Start();
        var copy = f.Client.Match.Snapshot!; copy.Teams![0].Members[0] = Guid.Empty;
        Assert.DoesNotContain(Guid.Empty, f.Client.Match.Snapshot!.Teams!.SelectMany(t => t.Members));
    }

    [Theory]
    [InlineData(1)] [InlineData(2)]
    public void PersonalHiddenAnswersAndExtendedDeadlinesDoNotCrossSlots(int kind)
    {
        var f = new Fixture(count: 10, strategy: true, random: kind); f.Start();
        for (var q = 0; q < 3; q++)
        {
            f.Clock.Now += TimeSpan.FromSeconds(1);
            foreach (var own in f.Client.OwnedPlayers) f.Send(f.Client.MatchForSlot(own.LocalSlot).CreateAnswer(f.Correct)!);
            f.Host.SubmitHostAnswer(f.Correct); f.Host.SubmitHostAnswer(f.Correct, localSlot: 1);
            f.Sync(); f.Host.PollMatch(); f.Sync(); f.Advance(); f.Advance(); if (f.Host.MatchSnapshot()!.Phase == "RoundEnd") f.Advance();
        }
        var zero = f.Client.Match; var one = f.Client.MatchForSlot(1);
        var card = zero.Snapshot!.Private!.Hand[0]; Assert.Equal(kind, card.Kind);
        Assert.Contains("UnknownCard", f.Send(LobbyProtocol.Encode("ActivateCard", f.Host.SessionId,
            new CardRequestDto(zero.Snapshot.Question.InstanceId, card.Id, LocalSlot: 1))).Messages[0].Json);
        f.Send(zero.CreateCard(card.Id)!);
        if (kind == 1)
        {
            Assert.Equal(2, zero.Snapshot!.Private!.HiddenAnswers.Length); Assert.Empty(one.Snapshot!.Private!.HiddenAnswers);
            Assert.Null(zero.CreateAnswer(zero.Snapshot.Private.HiddenAnswers[0]));
        }
        else
        {
            Assert.Equal(one.Snapshot!.Private!.DeadlineTicks + TimeSpan.TicksPerSecond * 5, zero.Snapshot!.Private!.DeadlineTicks);
            f.Clock.Now += TimeSpan.FromSeconds(20) + TimeSpan.FromTicks(1);
            var late = f.Send(one.CreateAnswer(f.Correct)!); Assert.Contains("Late", late.Messages[0].Json);
            f.Send(zero.CreateAnswer(f.Correct)!); Assert.Equal(f.Correct, zero.OwnAnswerIndex); Assert.Null(one.OwnAnswerIndex);
        }
    }

    [Fact]
    public void ReceiptCacheHasAByteBoundEvenBelowTheCountLimit()
    {
        var f = new Fixture(); var limited = false;
        for (var i = 0; i < 200; i++)
        {
            f.Clock.Now += TimeSpan.FromSeconds(1);
            var result = f.Host.Handle(2, LobbyProtocol.Encode("AddLocalPlayer", f.Host.SessionId, new AddLocalPlayerDto(new string('a', 15000), 7)));
            if (!result.DisconnectSender) continue;
            Assert.Contains("RequestLimit", result.Messages[0].Json); limited = true; break;
        }
        Assert.True(limited); Assert.Equal(4, f.Host.Snapshot().Players.Length);
    }
}

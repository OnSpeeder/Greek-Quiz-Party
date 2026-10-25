using System.Text.Json;
using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using Xunit;

namespace QuizParty.IntegrationTests;

public class StrategyProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(10); }
    private sealed class FixedRandom(int value) : IRandomSource { public int Next(int upper) => Math.Min(value, upper - 1); }
    private sealed class Fixture
    {
        public Clock Clock { get; } = new();
        public LobbyHost Host { get; }
        public LobbyClientState Client { get; } = new();
        public Fixture(int card = 0)
        {
            var categories = new[] { "history", "science", "arts", "sports", "geography" };
            var questions = Enumerable.Range(0, 35).Select(i => new QuestionDefinition($"q{i}", $"Synthetic {i}",
                ["yes", "no", "other", "last"], 0, categories[i % 5], 5, "Test only")).ToArray();
            Host = new("Room", "Host", Clock, questions, new(30, strategy: new(AllowSteal: true)), random: new FixedRandom(card));
            Deliver(Host.Handle(2, Client.BeginHello("Phone", "Android")));
            Host.SetHostReady(true);
            Deliver(Host.Handle(2, Client.CreateReady(true)!)); Host.Start();
            foreach (var p in Host.Broadcast()) Client.Apply(p.Json);
            Assert.True(Host.BeginMatch()); Sync();
        }
        public void Deliver(LobbyDispatch dispatch)
        { foreach (var p in dispatch.Messages.Where(p => p.ConnectionId == 2)) Client.Apply(p.Json); }
        public void Sync()
        { foreach (var p in Host.BroadcastMatch()) Client.Apply(p.Json); Assert.Equal(Host.MatchSnapshot()!.Revision, Client.Match.Snapshot!.Revision); }
        public void Answer(bool last = false)
        {
            Clock.Now += TimeSpan.FromSeconds(1);
            var correct = Array.IndexOf(Host.MatchSnapshot()!.Question.Answers, "yes");
            Deliver(Host.Handle(2, Client.Match.CreateAnswer(correct, 3)!));
            Assert.Equal(SubmissionError.None, Host.SubmitHostAnswer(last ? (correct + 1) % 4 : correct)); Sync();
            Host.PollMatch(); Sync(); Host.AdvanceMatch(); Sync();
        }
        public void Next()
        {
            Host.AdvanceMatch(); Sync();
            if (Host.MatchSnapshot()!.Phase == "RoundEnd") { Host.AdvanceMatch(); Sync(); }
        }
        public void Earn() { for (var i = 0; i < 3; i++) { Answer(); Next(); } }
    }

    [Theory]
    [InlineData(0)] [InlineData(1)] [InlineData(2)] [InlineData(3)] [InlineData(4)] [InlineData(5)]
    public void FullStrategyMatchRoutesEachCardPrivatelyAndDuplicateRequestsApplyOnce(int kind)
    {
        var f = new Fixture(kind); f.Earn();
        var own = f.Client.Match.Snapshot!.Private!; var hostOwn = f.Host.MatchSnapshot()!.Private!;
        Assert.Equal(f.Client.PlayerId, own.PlayerId); Assert.NotEqual(hostOwn.PlayerId, own.PlayerId);
        Assert.DoesNotContain(own.Hand[0].Id, hostOwn.Hand.Select(c => c.Id));
        Assert.Equal(kind, own.Hand[0].Kind);
        var publicPacket = Assert.Single(f.Host.BroadcastMatch()).Json;
        Assert.DoesNotContain("CorrectAnswerIndex", publicPacket); Assert.DoesNotContain(hostOwn.Hand[0].Id.ToString(), publicPacket);
        var spoof = LobbyProtocol.Encode("ActivateCard", f.Host.SessionId,
            new CardRequestDto(f.Host.MatchSnapshot()!.Question.InstanceId, hostOwn.Hand[0].Id));
        Assert.Contains("UnknownCard", f.Host.Handle(2, spoof).Messages[0].Json);
        if (kind is 3 or 5) f.Answer();
        var snapshot = f.Client.Match.Snapshot!;
        var request = f.Client.Match.CreateCard(own.Hand[0].Id,
            kind == 5 ? hostOwn.PlayerId : null, kind == 3 ? snapshot.Private!.SwapCategories.First() : null)!;
        Assert.NotNull(request); Assert.True(f.Client.Match.CardPending);
        var first = f.Host.Handle(2, request); f.Deliver(first); var revision = f.Host.MatchSnapshot()!.Revision;
        var duplicate = f.Host.Handle(2, request); f.Deliver(duplicate);
        Assert.Equal(first.Messages[0].Json, duplicate.Messages[0].Json); Assert.Equal(revision, f.Host.MatchSnapshot()!.Revision);
        Assert.False(f.Client.Match.CardPending); Assert.Equal("None", f.Client.Match.CardReason);
        Assert.DoesNotContain(own.Hand[0].Id, f.Client.Match.Snapshot!.Private!.Hand.Select(c => c.Id));
        if (kind == 1) { Assert.Equal(2, f.Client.Match.Snapshot.Private!.HiddenAnswers.Length); Assert.Empty(f.Host.MatchSnapshot()!.Private!.HiddenAnswers); }
        if (kind == 2) Assert.Equal(f.Host.MatchSnapshot()!.Question.DeadlineTicks + TimeSpan.TicksPerSecond * 5, f.Client.Match.Snapshot.Private!.DeadlineTicks);
        if (kind is 3 or 5) f.Next();
        while (f.Host.MatchSnapshot()!.Phase != "GameOver") { f.Answer(last: true); f.Next(); }
        var final = f.Client.Match.Snapshot!;
        Assert.Equal(30, final.QuestionNumber); Assert.Equal(2, final.FinalStrategy!.Length);
        Assert.Equal(1, final.FinalStrategy.Single(s => s.PlayerId == f.Client.PlayerId).CardsUsed);
        Assert.Equal(JsonSerializer.Serialize(f.Host.MatchSnapshot()!.Scores), JsonSerializer.Serialize(final.Scores));
        Assert.Equal(JsonSerializer.Serialize(f.Host.MatchSnapshot()!.FinalStrategy), JsonSerializer.Serialize(final.FinalStrategy));
    }

    [Fact]
    public void ConfidencePenaltyCanReduceAuthoritativeTotalsAndIsReflectedByClient()
    {
        var f = new Fixture(); f.Answer(); f.Next();
        var old = f.Client.Match.Snapshot!.Scores.Single(s => s.PlayerId == f.Client.PlayerId).Total;
        var correct = Array.IndexOf(f.Host.MatchSnapshot()!.Question.Answers, "yes");
        f.Deliver(f.Host.Handle(2, f.Client.Match.CreateAnswer((correct + 1) % 4, 3)!));
        f.Host.SubmitHostAnswer(correct); f.Sync(); f.Host.PollMatch(); f.Sync();
        Assert.Equal(-500, f.Client.Match.Snapshot!.Reveal!.Players.Single(p => p.PlayerId == f.Client.PlayerId).Points);
        Assert.Equal(old - 500, f.Client.Match.Snapshot.Scores.Single(s => s.PlayerId == f.Client.PlayerId).Total);
    }

    [Fact]
    public void MalformedPrivateStateAndUnrequestedReceiptsAreRejectedWithoutMutatingPresentation()
    {
        var f = new Fixture(); f.Earn(); var snapshot = f.Client.Match.Snapshot!;
        foreach (var bad in new[] {
            snapshot with { Private = snapshot.Private! with { PlayerId = Guid.NewGuid() } },
            snapshot with { Private = snapshot.Private! with { Hand = [new(Guid.Empty, 0)] } },
            snapshot with { Private = snapshot.Private! with { HiddenAnswers = [0, 0] } },
            snapshot with { Private = snapshot.Private! with { DeadlineTicks = long.MaxValue } },
            snapshot with { Private = snapshot.Private! with { Mission = new(99, 1, 1, true) } },
            snapshot with { Private = null }, snapshot with { FinalStrategy = [new(Guid.NewGuid(), null, 0, 0, 0, 0, 0, 0)] }
        }) Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(LobbyProtocol.Encode("MatchSnapshot", f.Host.SessionId, bad with { Revision = 999 })));
        var copy = f.Client.Match.Snapshot!; copy.Private!.Hand[0] = new(Guid.Empty, 0);
        Assert.NotEqual(Guid.Empty, f.Client.Match.Snapshot!.Private!.Hand[0].Id);
        var unsolicited = LobbyProtocol.Encode("CardResult", f.Host.SessionId,
            new CardReceiptDto(true, "None", snapshot.Question.InstanceId, snapshot.Private!.Hand[0].Id), Guid.NewGuid());
        Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(unsolicited));
        var old = f.Client.Match.CreateCard(snapshot.Private!.Hand[0].Id)!;
        var receipt = f.Host.Handle(2, old).Messages[0]; // Simulate receipt delayed until the next question.
        f.Clock.Now += TimeSpan.FromSeconds(21); f.Host.PollMatch(); f.Host.PollMatch(); f.Sync();
        f.Host.AdvanceMatch(); f.Sync(); f.Next();
        Assert.False(f.Client.Match.CardPending); Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(receipt.Json));
        var disconnected = f.Host.MatchSnapshot()!.Private!.Hand[0]; f.Host.Disconnect(2);
        Assert.Contains("HandshakeRequired", f.Host.Handle(2, LobbyProtocol.Encode("ActivateCard", f.Host.SessionId,
            new CardRequestDto(f.Host.MatchSnapshot()!.Question.InstanceId, disconnected.Id))).Messages[0].Json);
    }
}

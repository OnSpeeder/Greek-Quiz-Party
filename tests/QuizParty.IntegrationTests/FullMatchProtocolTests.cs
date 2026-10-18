using System.Text.Json;
using QuizParty.Core.Game;
using QuizParty.Core.Questions;
using QuizParty.Core.Time;
using QuizParty.Infrastructure.Networking;
using QuizParty.Infrastructure.Content;
using Xunit;

namespace QuizParty.IntegrationTests;

public class FullMatchProtocolTests
{
    private sealed class Clock : IGameClock { public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100); }
    private sealed class Fixture
    {
        public Clock Clock { get; } = new();
        public LobbyHost Host { get; }
        public LobbyClientState Client { get; } = new();
        public Fixture(int count)
        {
            var questions = Enumerable.Range(1, count + 2).Select(i => new QuestionDefinition($"q{i}", $"Synthetic {i}",
                ["yes", "no", "other", "last"], 0, "test", i % 5 + 1, "Synthetic explanation")).ToArray();
            Host = new("Test", "Host", Clock, questions, new(count));
            Deliver(Host.Handle(2, Client.BeginHello("Phone", "Android")));
            Deliver(Host.Handle(2, Client.CreateReady(true)!));
            Host.Start(); foreach (var p in Host.Broadcast()) Client.Apply(p.Json);
            Assert.True(Host.BeginMatch()); Sync();
        }
        public void Deliver(LobbyDispatch dispatch) { foreach (var p in dispatch.Messages.Where(p => p.ConnectionId == 2)) Client.Apply(p.Json); }
        public void Sync() { foreach (var p in Host.BroadcastMatch()) Assert.Equal(LobbyClientUpdate.MatchSnapshot, Client.Apply(p.Json)); }
        public int Correct => Array.IndexOf(Host.MatchSnapshot()!.Question.Answers, "yes");
    }

    [Theory]
    [InlineData(20)] [InlineData(30)]
    public void LongWireMatchResetsInputsRejectsStalePacketsAndClientsAgreeWithHost(int count)
    {
        var f = new Fixture(count);
        var seen = new HashSet<Guid>();
        string? previousRequest = null;
        for (var i = 1; i <= count; i++)
        {
            var snapshot = f.Host.MatchSnapshot()!;
            Assert.True(seen.Add(snapshot.Question.InstanceId));
            Assert.Equal(i, f.Client.Match.Snapshot!.QuestionNumber);
            Assert.Null(f.Client.Match.OwnAnswerIndex); Assert.False(f.Client.Match.Pending);
            foreach (var p in f.Host.BroadcastMatch())
            {
                Assert.DoesNotContain("CorrectAnswerIndex", p.Json); Assert.DoesNotContain("Explanation", p.Json);
                Assert.True(LobbyProtocol.TryDecode(p.Json, out _));
            }
            if (previousRequest is not null)
            {
                f.Deliver(f.Host.Handle(2, previousRequest)); // Cached old receipt must not change this question's input.
                Assert.Null(f.Client.Match.OwnAnswerIndex);
                var stale = LobbyProtocol.Encode("SubmitAnswer", f.Host.SessionId,
                    new AnswerRequestDto(Guid.NewGuid(), f.Correct, 1));
                f.Deliver(f.Host.Handle(2, stale)); Assert.Equal(0, f.Host.MatchSnapshot()!.AcceptedAnswerCount);
            }
            f.Clock.Now += TimeSpan.FromSeconds(1);
            var request = f.Client.Match.CreateAnswer(f.Correct)!;
            Assert.True(f.Client.Match.Pending);
            f.Deliver(f.Host.Handle(2, request)); f.Deliver(f.Host.Handle(2, request));
            previousRequest = request;
            Assert.Equal(f.Correct, f.Client.Match.OwnAnswerIndex);
            Assert.Equal(SubmissionError.None, f.Host.SubmitHostAnswer((f.Correct + 1) % 4));
            f.Sync(); Assert.True(f.Host.PollMatch()); f.Sync();
            Assert.Equal(i * 975, f.Client.Match.Snapshot!.Scores.Single(s => s.DisplayName == "Phone").Total);
            f.Host.AdvanceMatch(); f.Sync(); f.Host.AdvanceMatch(); f.Sync();
            if (f.Host.MatchSnapshot()!.Phase == "RoundEnd") { f.Host.AdvanceMatch(); f.Sync(); }
        }
        Assert.Equal("GameOver", f.Client.Match.Snapshot!.Phase);
        Assert.Equal(count, f.Client.Match.Snapshot.Statistics.Single(s => s.PlayerId == f.Client.PlayerId).Correct);
        Assert.Equal(JsonSerializer.Serialize(f.Host.MatchSnapshot()), JsonSerializer.Serialize(f.Client.Match.Snapshot));
    }

    [Fact]
    public void ClientRejectsQuestionRollbackReusedInstanceRosterChangesAndMalformedProgress()
    {
        var f = new Fixture(10);
        var first = f.Host.MatchSnapshot()!;
        var request = f.Client.Match.CreateAnswer(f.Correct)!;
        f.Deliver(f.Host.Handle(2, request)); f.Host.SubmitHostAnswer((f.Correct + 1) % 4); f.Sync();
        f.Host.PollMatch(); f.Sync(); f.Host.AdvanceMatch(); f.Sync(); f.Host.AdvanceMatch(); f.Sync();
        var current = f.Host.MatchSnapshot()!;
        foreach (var bad in new[]
        {
            first with { Revision = 999 }, current with { Revision = 999, QuestionNumber = 4 },
            current with { Revision = 999, Question = current.Question with { InstanceId = first.Question.InstanceId } },
            current with { Revision = 999, EligiblePlayers = null! }, current with { Revision = 999, Statistics = null! },
            current with { Revision = 999, Scores = [] }, current with { Revision = 999, TotalQuestions = 15 },
            current with { Revision = 999, Winners = [Guid.NewGuid()] }
        }) Assert.Equal(LobbyClientUpdate.Ignored, f.Client.Apply(LobbyProtocol.Encode("MatchSnapshot", f.Host.SessionId, bad)));
        var mutable = f.Client.Match.Snapshot!; mutable.EligiblePlayers[0] = Guid.Empty;
        Assert.DoesNotContain(Guid.Empty, f.Client.Match.Snapshot!.EligiblePlayers);
    }

    [Fact]
    public void ProtocolTwoIsExplicitlyRejectedAndCapacityCanBeCheckedBeforeLobbyStart()
    {
        var f = new Fixture(10);
        var json = f.Client.BeginHello("Old", "Android").Replace($"\"ProtocolVersion\":{LobbyProtocol.Version}", "\"ProtocolVersion\":2", StringComparison.Ordinal);
        var rejected = f.Host.Handle(3, json);
        Assert.True(rejected.DisconnectSender); Assert.Contains("IncompatibleVersion", rejected.Messages[0].Json);
        var host = new LobbyHost("Room", "Host", new Clock(), [new("one", "Question", ["a", "b", "c", "d"], 0, "test", 1, "Explanation")], new(1));
        Assert.False(host.ConfigureMatch(new(20))); Assert.Equal("Lobby", host.Snapshot().Phase);
        Assert.False(host.ConfigureMatch(new(1), [])); Assert.True(host.ConfigureMatch(new(1), ["test"]));
    }

    [Theory]
    [InlineData(false, false)] [InlineData(true, false)] [InlineData(true, true)]
    public void LargestContentBudgetStillFitsEightPlayerFinalPacket(bool strategy, bool teams)
    {
        var clock = new Clock();
        const string manifest = """{"schemaVersion":1,"locale":"el-GR","packVersion":"1.0.0","categories":[{"id":"test","nameKey":"CATEGORY_TEST"}]}""";
        PackValidation Validate(int explanationLength, int textLength = 1000) => QuestionPackLoader.Validate(manifest,
            new Dictionary<string,string> { ["test.json"] = JsonSerializer.Serialize(new[] { new {
                id = "q", text = new string('α', textLength), answers = new[] { "a", "b", "c", "d" }, correctAnswerIndex = 0,
                categoryId = "test", difficulty = 1, explanation = new string('β', explanationLength), locale = "el-GR", status = "reviewed"
            } }) }, "el-GR");
        // Phase08's private/final details made a previously valid 10KB question exceed16KiB.
        Assert.Contains(Validate(150, 1500).Issues, issue => issue.Code == "wire-limit" && !issue.Warning);
        Assert.Contains(Validate(470).Issues, issue => issue.Code == "wire-limit" && !issue.Warning);
        var valid = Validate(150); Assert.True(valid.Success, string.Join(';', valid.Issues));
        var host = new LobbyHost("Room", new string('Ω', 32), clock, valid.Pack!.Questions.Single());
        for (var i = 2; i <= 8; i++)
        {
            var client = new LobbyClientState();
            foreach (var p in host.Handle(i, client.BeginHello(new string('Ω', 31) + i, "Android")).Messages.Where(p => p.ConnectionId == i)) client.Apply(p.Json);
            host.Handle(i, client.CreateReady(true)!);
        }
        Assert.True(host.ConfigureMatch(new(1, strategy: strategy ? new StrategyRules() : null)));
        host.SetTeamMode(teams);
        host.Start(); host.BeginMatch(); clock.Now += TimeSpan.FromSeconds(21); host.PollMatch(); host.PollMatch();
        host.AdvanceMatch(); host.AdvanceMatch();
        Assert.Equal("GameOver", host.MatchSnapshot()!.Phase);
        foreach (var packet in host.BroadcastMatch()) Assert.True(LobbyProtocol.TryDecode(packet.Json, out _), $"Oversized final packet: {System.Text.Encoding.UTF8.GetByteCount(packet.Json)}");
        if (strategy)
        {
            var final = host.MatchSnapshot()!;
            var own = final.Private!;
            // Fill the additional bounded fields: longest Unicode category, two cards,
            // complete missions and nonzero confidence/card statistics for every player.
            final = final with { QuestionNumber = 30, TotalQuestions = 30,
                Question = final.Question with { CategoryId = new string('Ω', 128) },
                Private = own with { Hand = [new(Guid.NewGuid(), 0), new(Guid.NewGuid(), 1)], Mission = new(4, 5, 5, true), Streak = 30, Meter = 99 },
                FinalStrategy = final.Scores.Select(s => new StrategyFinalDto(s.PlayerId, new(4, 5, 5, true), 500, 30, 10, 5, 10, 5)).ToArray(),
                Statistics = final.Scores.Select(s => new MatchStatisticsDto(s.PlayerId, 20, 10, 0, 20, 19500000000, 30)).ToArray() };
            var encoded = LobbyProtocol.Encode("MatchSnapshot", host.SessionId, final);
            Assert.True(LobbyProtocol.TryDecode(encoded, out _), $"Oversized populated strategy final: {System.Text.Encoding.UTF8.GetByteCount(encoded)}");
        }
    }

    [Fact]
    public void SuddenDeathWireKeepsTotalsAndMakesOtherPlayersSpectators()
    {
        var clock = new Clock();
        var questions = Enumerable.Range(1, 3).Select(i => new QuestionDefinition($"q{i}", $"Synthetic {i}",
            ["yes", "no", "other", "last"], 0, "test", 1, "Test only")).ToArray();
        var host = new LobbyHost("Test", "Host", clock, questions, new(1));
        var clients = new[] { new LobbyClientState(), new LobbyClientState() };
        void Deliver(IEnumerable<LobbyOutbound> packets)
        { foreach (var p in packets) clients[(int)p.ConnectionId - 2].Apply(p.Json); }
        for (var i = 0; i < 2; i++)
        {
            Deliver(host.Handle(i + 2, clients[i].BeginHello($"Phone{i}", "Android")).Messages);
            Deliver(host.Handle(i + 2, clients[i].CreateReady(true)!).Messages);
        }
        host.Start(); Deliver(host.Broadcast()); Assert.True(host.BeginMatch()); Deliver(host.BroadcastMatch());
        var correct = Array.IndexOf(host.MatchSnapshot()!.Question.Answers, "yes");
        host.SubmitHostAnswer(correct);
        Deliver(host.Handle(2, clients[0].Match.CreateAnswer(correct)!).Messages);
        Deliver(host.Handle(3, clients[1].Match.CreateAnswer((correct + 1) % 4)!).Messages);
        host.PollMatch(); Deliver(host.BroadcastMatch());
        host.AdvanceMatch(); Deliver(host.BroadcastMatch()); host.AdvanceMatch(); Deliver(host.BroadcastMatch());
        Assert.True(clients[0].Match.Snapshot!.IsTieBreaker);
        host.AdvanceMatch(); Deliver(host.BroadcastMatch());
        Assert.Null(clients[1].Match.CreateAnswer(0));
        var now = host.MatchSnapshot()!;
        var spoof = host.Handle(3, LobbyProtocol.Encode("SubmitAnswer", host.SessionId, new AnswerRequestDto(now.Question.InstanceId, 0, 1)));
        Assert.Contains("UnknownPlayer", spoof.Messages[0].Json);
        correct = Array.IndexOf(now.Question.Answers, "yes");
        clock.Now += TimeSpan.FromSeconds(1);
        Deliver(host.Handle(2, clients[0].Match.CreateAnswer(correct)!).Messages);
        clock.Now += TimeSpan.FromTicks(1); host.SubmitHostAnswer(correct); Deliver(host.BroadcastMatch());
        host.PollMatch(); Deliver(host.BroadcastMatch()); host.AdvanceMatch(); Deliver(host.BroadcastMatch());
        host.AdvanceMatch(); Deliver(host.BroadcastMatch());
        Assert.Equal("GameOver", clients[0].Match.Snapshot!.Phase);
        Assert.Equal(clients[0].PlayerId, Assert.Single(clients[0].Match.Snapshot!.Winners));
        Assert.Equal(1000, clients[0].Match.Snapshot!.Scores.Single(s => s.PlayerId == clients[0].PlayerId).Total);
        Assert.Equal(1, clients[1].Match.Snapshot!.Statistics.Single(s => s.PlayerId == clients[1].PlayerId).Wrong);
    }
}

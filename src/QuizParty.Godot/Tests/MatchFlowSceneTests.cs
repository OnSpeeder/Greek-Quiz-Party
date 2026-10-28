using GdUnit4;
using Godot;
using QuizParty.Networking;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class MatchFlowSceneTests
{
    [TestCase]
    [RequireGodotRuntime]
    public async Task EightLocalSeatsFitHostQuestionAndRevealWaitsBeforeModalReplayRestoresLobby()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>(); tree.Root.AddChild(root);
        try
        {
            var transport = root.GetNode<LobbyTransport>("Transport");
            transport.DiscoveryPort = 19842; transport.StrategyEnabled = true; transport.UseSyntheticQuestions(1, source: "https://example.org/fact");
            AssertThat(transport.Host("Flow", "Host", 19841)).IsEqual(Error.Ok);
            foreach (var slot in Enumerable.Range(1, 7)) { transport.AddLocalPlayer("Player " + slot, slot); transport.SetReady(true, localSlot: slot); }
            transport.SetReady(true); transport.StartGame();
            transport.SetReady(true); // A late lobby request must not place lobby status above a live match.
            AssertThat(root.GetNode<Label>("Margin/Scroll/Content/Status").Visible).IsFalse();
            var panel = root.GetNode<MatchPanel>("Margin/Scroll/Content/MatchPanel");
            var scroll = root.GetNode<ScrollContainer>("Margin/Scroll");
            AssertThat(panel.GetNode<MatchDialog>("MatchDialogs/RevealDialog").Body.GetNodeOrNull<Button>("Source")).IsNull();
            foreach (var size in new[] { new Vector2(1152, 648), new Vector2(480, 800) })
            {
                root.Size = size;
                for (var i = 0; i < 8; i++) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
                AssertThat(scroll.VerticalScrollMode).IsEqual(ScrollContainer.ScrollMode.ShowNever);
                var controllers = panel.GetNode<LocalControllerPanel>("QuestionLayout/HostRail/LocalControllers");
                controllers.FindChildren("*", "Button", true, false).OfType<Button>().First(b => !b.Disabled).EmitSignal(Button.SignalName.Pressed);
                for (var i = 0; i < 5; i++) await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
                var layout = panel.GetNode<Control>("QuestionLayout").GetGlobalRect();
                AssertThat(layout.End.Y <= scroll.GetGlobalRect().End.Y + 1).IsTrue();
                AssertThat(layout.End.X <= scroll.GetGlobalRect().End.X + 1).IsTrue();
            }
            var snapshot = transport.MatchSnapshot!;
            var correct = Array.IndexOf(snapshot.Question.Answers, "Σωστό");
            for (var slot = 0; slot < 8; slot++) transport.SubmitAnswer(slot == 0 ? correct : (correct + 1) % 4, localSlot: slot);
            await tree.ToSignal(tree.CreateTimer(.3), global::Godot.Timer.SignalName.Timeout);
            var modal = panel.GetNode<MatchDialog>("MatchDialogs/RevealDialog");
            AssertThat(transport.MatchSnapshot!.Phase).IsEqual("AnswerReveal"); AssertThat(modal.Visible).IsFalse();
            await tree.ToSignal(tree.CreateTimer(1.3), global::Godot.Timer.SignalName.Timeout);
            AssertThat(modal.Visible).IsTrue();
            AssertThat(modal.Body.GetNode<Label>("CorrectAnswer").Text.Contains("Σωστό")).IsTrue();
            AssertThat(modal.Body.GetNode<Label>("FunFactsHeading").Text).IsEqual("MATCH_FUN_FACTS");
            AssertThat(modal.Body.GetNode<Label>("FunFacts").Text.Contains("fun fact")).IsTrue();
            var source = modal.Body.GetNode<Button>("Source");
            string? opened = null; panel.SourceOpener = url => { opened = url; return Error.Ok; };
            source.EmitSignal(Button.SignalName.Pressed);
            var confirm = panel.GetNode<MatchDialog>("MatchDialogs/SourceConfirmation");
            AssertThat(confirm.Visible).IsTrue(); AssertThat(modal.Visible).IsFalse();
            AssertThat(confirm.Body.GetNode<Label>("Url").Text).IsEqual("https://example.org/fact");
            confirm.Actions.GetNode<Button>("No").EmitSignal(Button.SignalName.Pressed);
            AssertThat(opened).IsNull(); AssertThat(modal.Visible).IsTrue();
            source.EmitSignal(Button.SignalName.Pressed);
            panel.SourceOpener = _ => Error.CantOpen;
            confirm.Actions.GetNode<Button>("Yes").EmitSignal(Button.SignalName.Pressed);
            AssertThat(confirm.Body.GetNode<Label>("Error").Visible).IsTrue();
            root.GetNode<PresentationShell>("PresentationShell").NavigateBack();
            AssertThat(confirm.Visible).IsFalse(); AssertThat(modal.Visible).IsTrue();
            panel.SourceOpener = url => { opened = url; return Error.Ok; };
            source.EmitSignal(Button.SignalName.Pressed);
            confirm.Actions.GetNode<Button>("Yes").EmitSignal(Button.SignalName.Pressed);
            AssertThat(opened).IsEqual("https://example.org/fact"); AssertThat(modal.Visible).IsTrue();
            var heldButton = modal.Actions.GetChildren().OfType<Button>().First();
            transport.ContinueMatch(localSlot: 1);
            AssertThat(modal.Actions.GetChildren().OfType<Button>().First() == heldButton).IsTrue();
            modal.Actions.GetChildren().OfType<Button>().First().EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.MatchSnapshot!.Phase).IsEqual("Scoreboard"); AssertThat(modal.Visible).IsFalse();
            var standings = panel.GetNode<StandingsPanel>("Standings");
            AssertThat(standings.GetNode<HBoxContainer>("Podium").GetChildCount()).IsEqual(3);
            AssertThat(standings.GetNode<VBoxContainer>("Remaining").GetChildCount()).IsEqual(5);
            var scoreboardButton = panel.GetNode<GridContainer>("VoteActions").GetChildren().OfType<Button>().First();
            transport.ContinueMatch(localSlot: 1);
            AssertThat(panel.GetNode<GridContainer>("VoteActions").GetChildren().OfType<Button>().First() == scoreboardButton).IsTrue();
            await tree.ToSignal(tree.CreateTimer(1.2), global::Godot.Timer.SignalName.Timeout);
            var podium = standings.GetNode<HBoxContainer>("Podium");
            AssertThat(podium.GetChildren().OfType<PanelContainer>().Count(card => card.GetNode<Label>("Content/Rank").Text == "#1")).IsEqual(1);
            AssertThat(podium.GetChildren().OfType<PanelContainer>().Count(card => card.GetNode<Label>("Content/Rank").Text == "#2")).IsEqual(2);
            transport.AdvanceMatch(); AssertThat(transport.MatchSnapshot!.Phase).IsEqual("GameOver");
            panel.GetNode<Button>("Replay").EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.MatchSnapshot).IsNull(); AssertThat(transport.Snapshot!.Phase).IsEqual("Lobby");
            AssertThat(panel.Visible).IsFalse(); AssertThat(transport.Snapshot.Players.Length).IsEqual(8);
            AssertThat(transport.Snapshot.Players.All(p => !p.Ready)).IsTrue();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }
}

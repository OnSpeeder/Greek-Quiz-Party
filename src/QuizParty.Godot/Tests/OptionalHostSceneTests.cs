using GdUnit4;
using Godot;
using QuizParty.Networking;
using QuizParty.Presentation;
using static GdUnit4.Assertions;

namespace QuizParty.Godot.Tests;

[TestSuite]
public class OptionalHostSceneTests
{
    [TestCase]
    [RequireGodotRuntime]
    public async Task CompactCreationUsesOptionalHostIdentityAndPersistentPin()
    {
        var tree = (SceneTree)Engine.GetMainLoop();
        using var root = GD.Load<PackedScene>("res://Scenes/Lobby.tscn").Instantiate<LobbyScreen>(); tree.Root.AddChild(root);
        try
        {
            root.ShowSetupPage("create");
            var creation = root.GetNode<RoomCreationPanel>("Margin/Scroll/Content/CreateRoom");
            var transport = root.GetNode<LobbyTransport>("Transport"); transport.DiscoveryPort = 19762;
            var pin = (LineEdit)creation.FindChild("RoomPin", true, false); pin.Text = "1234";
            AssertThat(pin.IsVisibleInTree()).IsTrue();
            var capacity = (OptionButton)creation.FindChild("Capacity", true, false); capacity.Select(0);
            var submit = (Button)creation.FindChild("Create", true, false);
            AssertThat(submit.Text).IsEqual("HOST_CONTINUE"); submit.EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.Snapshot).IsNull(); AssertThat(creation.IdentityOpen).IsTrue();
            var identity = creation.GetNode<PlayerIdentityForm>("Identity");
            identity.NameInput.Text = "Ελένη"; identity.Characters.Select(3);
            AssertThat(identity.Characters.GetNode<Button>("Character3").Text).IsEqual("");
            AssertThat(identity.Characters.GetNode<Button>("Character3").ThemeTypeVariation.ToString()).IsEqual("PrimaryAction");
            root.NavigateBack(); AssertThat(creation.IdentityOpen).IsFalse(); AssertThat(pin.Text).IsEqual("1234");
            ((CheckButton)creation.FindChild("HostPlays", true, false)).ButtonPressed = false;
            AssertThat(submit.Text).IsEqual("LOBBY_HOST"); submit.EmitSignal(Button.SignalName.Pressed);
            AssertThat(transport.IsHost).IsTrue(); AssertThat(transport.OwnedPlayers.Count).IsEqual(0);
            AssertThat(transport.Snapshot!.Players.Length).IsEqual(0); AssertThat(transport.Snapshot.MaxPlayers).IsEqual(2);
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
            await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame);
            var settings = root.GetNode<Button>("PresentationShell/Settings");
            var rules = root.GetNode<Button>("PresentationShell/LobbyActions/GameRules");
            var setup = root.GetNode<Button>("PresentationShell/LobbyActions/GameSetup");
            AssertThat(settings.GetGlobalRect().Intersects(rules.GetGlobalRect())).IsFalse();
            AssertThat(rules.GetGlobalRect().Intersects(setup.GetGlobalRect())).IsFalse();
            foreach (var scroll in root.FindChildren("*", "ScrollContainer", true, false).OfType<ScrollContainer>())
                AssertThat(scroll.GetPath() + ":" + scroll.VerticalScrollMode).IsEqual(scroll.GetPath() + ":" + (scroll.VerticalScrollMode == ScrollContainer.ScrollMode.Disabled ? ScrollContainer.ScrollMode.Disabled : ScrollContainer.ScrollMode.ShowNever));
            var tooltip = new Label { ThemeTypeVariation = "TooltipLabel", Text = "Ρυθμίσεις παιχνιδιού" }; root.AddChild(tooltip);
            AssertThat(tooltip.AutowrapMode).IsEqual(TextServer.AutowrapMode.Off);
            AssertThat(tooltip.GetCombinedMinimumSize().X > 100).IsTrue();
            var longTooltip = new Label { ThemeTypeVariation = "TooltipLabel", Text = string.Join(" ", Enumerable.Repeat("Μεγάλο ελληνικό όνομα και κατάσταση", 8)) }; root.AddChild(longTooltip);
            AssertThat(longTooltip.AutowrapMode).IsEqual(TextServer.AutowrapMode.WordSmart);
            AssertThat(longTooltip.CustomMinimumSize.X <= 420).IsTrue();
        }
        finally { root.Free(); await tree.ToSignal(tree, SceneTree.SignalName.ProcessFrame); }
    }
}

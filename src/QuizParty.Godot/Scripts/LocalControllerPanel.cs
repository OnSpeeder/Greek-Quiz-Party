using Godot;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Explicit handoff curtain. It never decides eligibility or confirms an answer.</summary>
public partial class LocalControllerPanel : VBoxContainer
{
    private LobbyTransport? _transport;
    private Guid _question;
    public bool Open { get; private set; }
    public event Action? Changed;
    public override void _Ready() => Visible = false;
    public void Bind(LobbyTransport transport)
    { _transport = transport; transport.OwnedStateChanged += Refresh; transport.LocalPlayerChanged += Close; }
    public void Close() { Open = false; Changed?.Invoke(); }
    public void Refresh()
    {
        if (_transport is null) return;
        var snapshot = _transport.MatchSnapshot;
        var multiple = _transport.OwnedPlayers.Count > 1;
        Visible = multiple && snapshot?.Phase is "QuestionActive" or "QuestionLocked" or "Scoreboard" or "RoundEnd";
        if (snapshot is null) { Open = false; return; }
        if (_question != snapshot.Question.InstanceId) { _question = snapshot.Question.InstanceId; Open = false; }
        if (!multiple) Open = _transport.OwnedPlayers.Count == 1;
        else if (snapshot.Phase is "QuestionActive" or "QuestionLocked" && (_transport.AnswerPending || _transport.OwnAnswerIndex is not null)) Open = false;
        foreach (var child in GetChildren()) { RemoveChild(child); child.QueueFree(); }
        if (!Visible) return;
        AddChild(new Label { Text = "LOCAL_HANDOFF_HINT", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        foreach (var player in _transport.OwnedPlayers)
        {
            var confirmed = _transport.AnswerForSlot(player.LocalSlot) is not null;
            var button = new Button { Text = string.Format(Tr(confirmed && snapshot.Phase == "QuestionActive" ? "LOCAL_SUBMITTED" : "LOCAL_PLAY_AS"), player.DisplayName),
                CustomMinimumSize = new(0, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart };
            button.Icon = GameArt.AvatarTexture(player.CharacterId ?? player.LocalSlot);
            button.ExpandIcon = true;
            button.AddThemeConstantOverride("icon_max_width", 56);
            button.ThemeTypeVariation = "PrimaryAction";
            button.Disabled = snapshot.Phase != "Scoreboard" && snapshot.Phase != "RoundEnd" &&
                (confirmed || _transport.AnswerPendingForSlot(player.LocalSlot) || !snapshot.EligiblePlayers.Contains(player.PlayerId) || snapshot.Phase != "QuestionActive");
            button.Pressed += () =>
            {
                _transport.SelectLocalPlayer(player.LocalSlot);
                Open = true; Changed?.Invoke();
            };
            AddChild(button);
        }
        if (Open)
        {
            var hide = new Button { Text = "LOCAL_HIDE", CustomMinimumSize = new(0, 64) };
            hide.Pressed += Close; AddChild(hide);
        }
    }
    public override void _ExitTree()
    {
        if (_transport is null) return;
        _transport.OwnedStateChanged -= Refresh; _transport.LocalPlayerChanged -= Close;
    }
}

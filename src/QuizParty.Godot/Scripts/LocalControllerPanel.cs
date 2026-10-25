using Godot;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Explicit handoff curtain. It never decides eligibility or confirms an answer.</summary>
public partial class LocalControllerPanel : VBoxContainer
{
    private LobbyTransport? _transport;
    private Guid _question;
    private bool _compact;
    private bool _wide;
    public void SetCompact(bool compact, bool wide) { _compact = compact; _wide = wide; }
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
        Visible = multiple && (snapshot?.Phase is "QuestionActive" or "QuestionLocked" || snapshot?.Strategy is not null && snapshot.Phase is "Scoreboard" or "RoundEnd");
        if (snapshot is null) { Open = false; return; }
        if (_question != snapshot.Question.InstanceId) { _question = snapshot.Question.InstanceId; Open = false; }
        if (!multiple) Open = _transport.OwnedPlayers.Count == 1;
        else if (snapshot.Phase is "QuestionActive" or "QuestionLocked" && (_transport.AnswerPending || _transport.OwnAnswerIndex is not null)) Open = false;
        foreach (var child in GetChildren()) { RemoveChild(child); child.QueueFree(); }
        if (!Visible) return;
        AddChild(new Label { Text = "LOCAL_HANDOFF_HINT", AutowrapMode = TextServer.AutowrapMode.WordSmart });
        var players = new GridContainer { Columns = _compact ? (_wide ? 2 : 4) : 1, SizeFlagsHorizontal = SizeFlags.ExpandFill };
        AddChild(players);
        foreach (var player in _transport.OwnedPlayers)
        {
            var confirmed = _transport.AnswerForSlot(player.LocalSlot) is not null;
            var button = new Button { Text = string.Format(Tr(confirmed && snapshot.Phase == "QuestionActive" ? "LOCAL_SUBMITTED" : "LOCAL_PLAY_AS"), player.DisplayName),
                CustomMinimumSize = new(0, 64), AutowrapMode = TextServer.AutowrapMode.WordSmart };
            button.Icon = GameArt.AvatarTexture(player.CharacterId ?? player.LocalSlot);
            button.ExpandIcon = true;
            button.AddThemeConstantOverride("icon_max_width", _compact ? 28 : 56);
            if (_compact) { QuizShowTheme.SetFontSize(button, 15); button.Text = player.DisplayName + (_transport.MatchSnapshot?.AnsweredPlayers?.Contains(player.PlayerId) == true ? " ✓" : " ○"); }
            button.ThemeTypeVariation = "PrimaryAction";
            button.Disabled = snapshot.Phase != "Scoreboard" && snapshot.Phase != "RoundEnd" &&
                (confirmed || _transport.AnswerPendingForSlot(player.LocalSlot) || !snapshot.EligiblePlayers.Contains(player.PlayerId) || snapshot.Phase != "QuestionActive");
            button.Pressed += () =>
            {
                _transport.SelectLocalPlayer(player.LocalSlot);
                Open = true; Changed?.Invoke();
            };
            button.SizeFlagsHorizontal = SizeFlags.ExpandFill;
            players.AddChild(button);
        }
        if (Open)
        {
            if (_compact) { players.Hide(); GetChild<Label>(0).Hide(); }
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

using Godot;
using QuizParty.Core.Game;
using QuizParty.Infrastructure.Networking;
using QuizParty.Networking;

namespace QuizParty.Presentation;

/// <summary>Owner-only presentation. All card effects and decisions come from host snapshots.</summary>
public partial class StrategyPanel : VBoxContainer
{
    private LobbyTransport? _transport;
    private MatchSnapshotDto? _snapshot;
    private Guid _question;
    private Guid _owner;
    private Guid _session;
    private bool _initialized;
    private string _reason = "None";
    private OptionButton _confidence = null!;
    private Button _privacy = null!;
    private VBoxContainer _private = null!;
    private Label _status = null!;
    public int Confidence => _snapshot?.Strategy?.Confidence == true && !_snapshot.IsTieBreaker ? _confidence.GetSelectedId() : 1;

    public override void _Ready()
    {
        _confidence = new OptionButton { Name = "Confidence", CustomMinimumSize = new(0, 64) };
        foreach (var value in new[] { 1, 2, 3 }) _confidence.AddItem(Tr("STRATEGY_CONFIDENCE_" + value), value);
        AddChild(_confidence);
        _privacy = new Button { Name = "Privacy", Text = Tr("STRATEGY_PRIVATE"), CustomMinimumSize = new(0, 64),
            AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_privacy);
        _private = new VBoxContainer { Name = "Private", Visible = false };
        AddChild(_private);
        _privacy.Pressed += () => _private.Visible = !_private.Visible;
        _status = new Label { Name = "CardStatus", AutowrapMode = TextServer.AutowrapMode.WordSmart };
        AddChild(_status);
    }

    public void Bind(LobbyTransport transport)
    {
        _transport = transport;
        transport.CardInputChanged += OnCardInput;
    }
    private void OnCardInput(string reason) { _reason = reason; if (_snapshot is { } snapshot) Render(snapshot); }

    public void Render(MatchSnapshotDto snapshot)
    {
        _snapshot = snapshot;
        Visible = snapshot.Strategy is not null && snapshot.Phase != "GameOver";
        if (_transport is null || !Visible || snapshot.Private is not { } own) return;
        if (_session != snapshot.SessionId)
        { _session = snapshot.SessionId; _initialized = false; _owner = Guid.Empty; _question = Guid.Empty; }
        if (!_initialized) { _private.Visible = !_transport.IsHost; _initialized = true; }
        if (_question != snapshot.Question.InstanceId || _owner != own.PlayerId)
        { _question = snapshot.Question.InstanceId; _owner = own.PlayerId; _confidence.Select(0); _reason = "None"; }
        _confidence.Visible = snapshot.Strategy!.Confidence && !snapshot.IsTieBreaker;
        _confidence.Disabled = snapshot.Phase != "QuestionActive" || _transport.OwnAnswerIndex is not null ||
            _transport.AnswerPending || _transport.CardPending || !snapshot.EligiblePlayers.Contains(own.PlayerId);
        _status.Text = _reason == "None" ? (own.Notice == "None" ? "" : Tr("STRATEGY_NOTICE_" + own.Notice)) :
            Tr("STRATEGY_CARD_" + _reason);
        foreach (var child in _private.GetChildren()) { _private.RemoveChild(child); child.QueueFree(); }
        AddText(string.Format(Tr("STRATEGY_PROGRESS"), own.Streak, own.Meter));
        if (own.Shield) AddText(Tr("STRATEGY_SHIELD_ACTIVE"));
        if (own.DoublePoints) AddText(Tr("STRATEGY_DOUBLE_ACTIVE"));
        if (own.Mission is { } mission) AddText(string.Format(Tr("STRATEGY_MISSION"),
            Tr("STRATEGY_MISSION_" + (MissionKind)mission.Kind), mission.Progress, mission.Target));
        else AddText(Tr("STRATEGY_NO_MISSION"));
        if (snapshot.IsTieBreaker) { AddText(Tr("STRATEGY_TIE_DISABLED")); return; }
        if (own.Hand.Length == 0) AddText(Tr("STRATEGY_EMPTY_HAND"));
        foreach (var card in own.Hand)
        {
            var kind = (CardKind)card.Kind;
            AddText(Tr("STRATEGY_DESCRIPTION_" + kind));
            OptionButton? options = null;
            Guid[] targets = [];
            if (kind == CardKind.CategorySwap)
            {
                options = new OptionButton { CustomMinimumSize = new(0, 64) };
                foreach (var category in own.SwapCategories) options.AddItem(CategoryName(category));
                _private.AddChild(options);
            }
            if (kind == CardKind.Steal)
            {
                options = new OptionButton { CustomMinimumSize = new(0, 64) };
                var ownTeam = snapshot.Teams?.FirstOrDefault(t => t.Members.Contains(own.PlayerId));
                var others = snapshot.Scores.Where(s => s.PlayerId != own.PlayerId && ownTeam?.Members.Contains(s.PlayerId) != true &&
                    _transport.Snapshot?.Players.Any(p => p.PlayerId == s.PlayerId) == true).ToArray();
                targets = others.Select(p => p.PlayerId).ToArray();
                foreach (var player in others) options.AddItem(player.DisplayName);
                _private.AddChild(options);
            }
            var active = snapshot.Phase == "QuestionActive";
            var recap = snapshot.Phase is "Scoreboard" or "RoundEnd";
            var available = (kind switch
            {
                CardKind.FiftyFifty or CardKind.ExtraTime => active,
                CardKind.CategorySwap => recap && own.SwapCategories.Length != 0,
                CardKind.Steal => recap && targets.Length != 0,
                _ => active || recap
            }) && (!active || _transport.OwnAnswerIndex is null);
            var button = new Button { Text = Tr("STRATEGY_USE_" + kind), CustomMinimumSize = new(0, 64),
                AutowrapMode = TextServer.AutowrapMode.WordSmart,
                Disabled = !available || _transport.CardPending || _transport.AnswerPending };
            button.Pressed += () => _transport.ActivateCard(card.Id,
                kind == CardKind.Steal && options!.Selected >= 0 ? targets[options.Selected] : null,
                kind == CardKind.CategorySwap && options!.Selected >= 0 ? own.SwapCategories[options.Selected] : null);
            _private.AddChild(button);
        }
    }
    private string CategoryName(string id)
    {
        var key = _transport!.QuestionCategories.FirstOrDefault(c => c.Id == id)?.NameKey ?? "STRATEGY_CATEGORY_" + id;
        var translated = Tr(key).ToString();
        return translated == key ? id : translated;
    }
    private void AddText(string text) => _private.AddChild(new Label { Text = text, AutowrapMode = TextServer.AutowrapMode.WordSmart });
    public override void _ExitTree() { if (_transport is not null) _transport.CardInputChanged -= OnCardInput; }
}

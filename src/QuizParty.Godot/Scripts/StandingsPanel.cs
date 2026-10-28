using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Presentation;

/// <summary>Public host-supplied scores, with presentation-only ranking and animation.</summary>
public partial class StandingsPanel : VBoxContainer
{
    private Guid _session;
    private Guid _question;
    private Guid _animatedQuestion;
    private readonly Dictionary<Guid, long> _starting = [];
    private readonly Dictionary<Guid, long> _lastShown = [];
    private string _renderKey = "";
    private int _generation;

    public void Observe(MatchSnapshotDto snapshot)
    {
        if (_session != snapshot.SessionId)
        {
            _session = snapshot.SessionId; _question = Guid.Empty; _animatedQuestion = Guid.Empty;
            _starting.Clear(); _lastShown.Clear(); _renderKey = "";
        }
        if (snapshot.Phase == "QuestionActive" && _question != snapshot.Question.InstanceId)
        {
            _question = snapshot.Question.InstanceId; _starting.Clear();
            foreach (var score in snapshot.Scores) _starting[score.PlayerId] = score.Total;
        }
    }

    public void Render(MatchSnapshotDto snapshot)
    {
        Observe(snapshot);
        var scores = snapshot.Scores;
        var key = snapshot.Question.InstanceId + ":" + string.Join("|", scores.Select(s => $"{s.PlayerId}:{s.DisplayName}:{s.Total}"));
        if (key == _renderKey) return;
        _renderKey = key;
        var generation = ++_generation;
        var firstRecap = snapshot.Phase == "Scoreboard" && _animatedQuestion != snapshot.Question.InstanceId;
        var haveStartingScores = _question == snapshot.Question.InstanceId && scores.All(s => _starting.ContainsKey(s.PlayerId));
        var animateRecap = firstRecap && haveStartingScores && PresentationShell.For(this)?.Preferences.ReducedMotion != true;
        if (firstRecap) _animatedQuestion = snapshot.Question.InstanceId;
        var initial = animateRecap ? scores.OrderByDescending(s => _starting[s.PlayerId]).ThenBy(s => s.PlayerId).ToArray()
            : scores.OrderByDescending(s => s.Total).ThenBy(s => s.PlayerId).ToArray();
        var target = scores.OrderByDescending(s => s.Total).ThenBy(s => s.PlayerId).ToArray();
        foreach (var child in GetChildren()) { RemoveChild(child); child.QueueFree(); }
        var podium = new HBoxContainer { Name = "Podium", SizeFlagsHorizontal = SizeFlags.ExpandFill, Alignment = BoxContainer.AlignmentMode.Center };
        podium.AddThemeConstantOverride("separation", 6); AddChild(podium);
        var remaining = new VBoxContainer { Name = "Remaining", SizeFlagsHorizontal = SizeFlags.ExpandFill };
        remaining.AddThemeConstantOverride("separation", 4); AddChild(remaining);
        var cards = new Dictionary<Guid, PanelContainer>();
        foreach (var score in scores)
        {
            var card = new PanelContainer { Name = "Player_" + score.PlayerId.ToString("N"), SizeFlagsHorizontal = SizeFlags.ExpandFill,
                SizeFlagsVertical = SizeFlags.ShrinkEnd };
            var content = new BoxContainer { Name = "Content", Vertical = true, SizeFlagsHorizontal = SizeFlags.ExpandFill };
            content.AddThemeConstantOverride("separation", 2); card.AddChild(content);
            var rank = new Label { Name = "Rank", HorizontalAlignment = HorizontalAlignment.Center, AutowrapMode = TextServer.AutowrapMode.Off };
            rank.SetMeta("presentation_no_wrap", true); QuizShowTheme.SetFontSize(rank, 18); content.AddChild(rank);
            var avatar = GameArt.Avatar(score.CharacterId ?? Array.FindIndex(scores, item => item.PlayerId == score.PlayerId), 40);
            avatar.SizeFlagsHorizontal = SizeFlags.ShrinkCenter; content.AddChild(avatar);
            var name = new Label { Name = "PlayerName", Text = score.DisplayName, HorizontalAlignment = HorizontalAlignment.Center,
                AutowrapMode = TextServer.AutowrapMode.WordSmart };
            QuizShowTheme.SetFontSize(name, 16); content.AddChild(name);
            var total = new Label { Name = "Total", HorizontalAlignment = HorizontalAlignment.Center, AutowrapMode = TextServer.AutowrapMode.Off };
            total.SetMeta("presentation_no_wrap", true); total.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
            QuizShowTheme.SetFontSize(total, 25); content.AddChild(total);
            var result = snapshot.Reveal?.Players.FirstOrDefault(p => p.PlayerId == score.PlayerId);
            var delta = new Label { Name = "Delta", Text = result is null ? "" : result.Points > 0 ? "+" + result.Points : result.Points.ToString(),
                HorizontalAlignment = HorizontalAlignment.Center, AutowrapMode = TextServer.AutowrapMode.Off };
            delta.SetMeta("presentation_no_wrap", true); delta.AddThemeColorOverride("font_color", ShowtimeTheme.Cyan);
            QuizShowTheme.SetFontSize(delta, 15); content.AddChild(delta);
            cards.Add(score.PlayerId, card);
            total.Text = score.Total.ToString("N0");
            // Add before tweening so Godot has a scene-owned animation target.
        }
        Arrange(initial, animateRecap ? _starting : null);
        foreach (var score in scores)
        {
            var total = cards[score.PlayerId].GetNode<Label>("Content/Total");
            var from = animateRecap ? _starting[score.PlayerId] : _lastShown.GetValueOrDefault(score.PlayerId, score.Total);
            if (from != score.Total) PresentationShell.For(this)?.Juice.TweenScoreLabel(total, from, score.Total);
            _lastShown[score.PlayerId] = score.Total;
        }
        if (animateRecap && !initial.Select(s => s.PlayerId).SequenceEqual(target.Select(s => s.PlayerId)))
            GetTree().CreateTimer(.65).Timeout += () =>
            {
                if (!GodotObject.IsInstanceValid(this) || !IsInsideTree() || generation != _generation) return;
                var old = cards.ToDictionary(c => c.Key, c => c.Value.GlobalPosition);
                Arrange(target, null);
                Callable.From(() =>
                {
                    if (!GodotObject.IsInstanceValid(this) || !IsInsideTree() || generation != _generation) return;
                    foreach (var (id, card) in cards)
                        if (GodotObject.IsInstanceValid(card)) PresentationShell.For(this)?.Juice.MoveFrom(card, old[id]);
                }).CallDeferred();
            };

        void Arrange(MatchScoreDto[] order, IReadOnlyDictionary<Guid, long>? values)
        {
            var top = order.Take(3).ToArray();
            var visual = top.Length == 3 ? new[] { top[1], top[0], top[2] } : top;
            foreach (var score in order)
            {
                var index = Array.FindIndex(order, s => s.PlayerId == score.PlayerId);
                var value = values?.GetValueOrDefault(score.PlayerId) ?? score.Total;
                var rank = 1 + order.Count(other => (values?.GetValueOrDefault(other.PlayerId) ?? other.Total) > value);
                var card = cards[score.PlayerId]; var parent = index < 3 ? (Node)podium : remaining;
                if (card.GetParent() is null) parent.AddChild(card);
                else if (card.GetParent() != parent) card.Reparent(parent);
                var style = QuizShowTheme.Card(new("1b1c35"), rank == 1 ? ShowtimeTheme.Gold : new Color("62668d"));
                style.ContentMarginLeft = 6; style.ContentMarginRight = 6; style.ContentMarginTop = 6; style.ContentMarginBottom = 6;
                card.AddThemeStyleboxOverride("panel", style);
                card.CustomMinimumSize = new(0, index < 3 ? rank == 1 ? 155 : rank == 2 ? 137 : 120 : 0);
                card.GetNode<BoxContainer>("Content").Vertical = index < 3;
                card.GetNode<Label>("Content/PlayerName").SizeFlagsHorizontal = index < 3 ? SizeFlags.Fill : SizeFlags.ExpandFill;
                card.GetNode<Label>("Content/Rank").Text = $"#{rank}";
            }
            for (var i = 0; i < visual.Length; i++) podium.MoveChild(cards[visual[i].PlayerId], i);
            foreach (var (score, i) in order.Skip(3).Select((s, i) => (s, i))) remaining.MoveChild(cards[score.PlayerId], i);
        }
    }
}

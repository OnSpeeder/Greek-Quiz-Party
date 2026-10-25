using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Presentation;

/// <summary>Visual public standings. It never calculates or predicts a score.</summary>
public partial class StandingsPanel : GridContainer
{
    private Guid _session;
    private readonly Dictionary<Guid, long> _totals = [];
    private string _renderKey = "";
    public override void _Ready()
    {
        AddThemeConstantOverride("h_separation", 12); AddThemeConstantOverride("v_separation", 12);
        Resized += UpdateColumns; UpdateColumns();
    }
    private void UpdateColumns() => Columns = Size.X >= 800 ? 4 : 2;
    public void Render(MatchScoreDto[] scores, Guid session = default)
    {
        if (_session != session) { _session = session; _totals.Clear(); _renderKey = ""; }
        var key = string.Join("|", scores.Select(s => $"{s.PlayerId}:{s.DisplayName}:{s.Total}"));
        if (key == _renderKey) return;
        _renderKey = key;
        foreach (var child in GetChildren()) { RemoveChild(child); child.QueueFree(); }
        foreach (var score in scores.OrderByDescending(score => score.Total))
        {
            var card = new PanelContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill };
            AddChild(card);
            var column = new VBoxContainer(); card.AddChild(column);
            column.AddChild(GameArt.Avatar(score.CharacterId ?? Array.FindIndex(scores, player => player.PlayerId == score.PlayerId), 112));
            var name = new Label { Text = score.DisplayName, HorizontalAlignment = HorizontalAlignment.Center,
                AutowrapMode = TextServer.AutowrapMode.WordSmart };
            name.AddThemeFontSizeOverride("font_size", 18); column.AddChild(name);
            var total = new Label { Text = score.Total.ToString("N0"), HorizontalAlignment = HorizontalAlignment.Center };
            total.AddThemeFontSizeOverride("font_size", 30); total.AddThemeColorOverride("font_color", ShowtimeTheme.Gold);
            column.AddChild(total);
            var previous = _totals.GetValueOrDefault(score.PlayerId);
            _totals[score.PlayerId] = score.Total;
            PresentationShell.For(this)?.Juice.TweenScoreLabel(total, previous, score.Total);
        }
    }
}

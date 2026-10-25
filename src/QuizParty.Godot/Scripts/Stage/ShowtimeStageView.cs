using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Presentation;

/// <summary>Public cast cutouts for the wide host. Never reads private answers or missions.</summary>
public partial class ShowtimeStageView : HBoxContainer
{
    private string _castKey = "";
    public void Render(MatchScoreDto[] scores, bool react)
    {
        var key = string.Join("|", scores.Select(score => $"{score.PlayerId}:{score.DisplayName}"));
        if (_castKey != key)
        {
            _castKey = key;
            foreach (var child in GetChildren()) { RemoveChild(child); child.QueueFree(); }
            for (var i = 0; i < scores.Length; i++)
            {
                var cast = new VBoxContainer { SizeFlagsHorizontal = SizeFlags.ExpandFill };
                AddChild(cast);
                cast.AddChild(GameArt.Avatar(scores[i].CharacterId ?? i, 64));
                var name = new Label { Text = scores[i].DisplayName, HorizontalAlignment = HorizontalAlignment.Center,
                    AutowrapMode = TextServer.AutowrapMode.WordSmart };
                name.AddThemeFontSizeOverride("font_size", 16); cast.AddChild(name);
            }
        }
        if (react && Visible)
            foreach (var cast in GetChildren().OfType<Control>()) PresentationShell.For(this)?.Juice.PulseWinner(cast);
    }
}

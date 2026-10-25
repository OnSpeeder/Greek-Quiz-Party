using Godot;
using QuizParty.Infrastructure.Networking;

namespace QuizParty.Presentation;

/// <summary>Public cast cutouts for the wide host. Never reads private answers or missions.</summary>
public partial class ShowtimeStageView : GridContainer
{
    private string _castKey = "";
    public void Render(MatchScoreDto[] scores, bool react, Guid[]? answered = null)
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
                cast.AddChild(GameArt.Avatar(scores[i].CharacterId ?? i, 36));
                var name = new Label { Text = scores[i].DisplayName, HorizontalAlignment = HorizontalAlignment.Center,
                    AutowrapMode = TextServer.AutowrapMode.WordSmart };
                name.AddThemeFontSizeOverride("font_size", 14); cast.AddChild(name);
                cast.AddChild(new Label { Name = "Answered", HorizontalAlignment = HorizontalAlignment.Center });
            }
        }
        for (var i = 0; i < scores.Length; i++)
        {
            var status = GetChild(i).GetNode<Label>("Answered");
            status.Text = Tr(answered?.Contains(scores[i].PlayerId) == true ? "MATCH_PLAYER_ANSWERED" : "MATCH_PLAYER_WAITING");
            QuizShowTheme.SetFontSize(status, 13);
            status.AddThemeColorOverride("font_color", answered?.Contains(scores[i].PlayerId) == true ? ShowtimeTheme.Cyan : Colors.White);
        }
        if (react && Visible)
            foreach (var cast in GetChildren().OfType<Control>()) PresentationShell.For(this)?.Juice.PulseWinner(cast);
    }
}

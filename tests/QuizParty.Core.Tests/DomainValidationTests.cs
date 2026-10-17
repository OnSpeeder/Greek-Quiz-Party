using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using Xunit;

namespace QuizParty.Core.Tests;

public class DomainValidationTests
{
    [Theory]
    [InlineData(-1)]
    [InlineData(4)]
    public void QuestionRejectsInvalidCorrectIndex(int correctIndex)
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new QuestionDefinition("id", "text",
            ["a", "b", "c", "d"], correctIndex, "category", 1, "explanation"));
    }

    [Theory]
    [InlineData(0)]
    [InlineData(6)]
    public void QuestionRejectsInvalidDifficulty(int difficulty)
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new QuestionDefinition("id", "text",
            ["a", "b", "c", "d"], 0, "category", difficulty, "explanation"));
    }

    [Fact]
    public void QuestionRejectsMalformedChoicesAndCopiesCallerCollection()
    {
        foreach (var choices in new string[][]
        {
            [], ["a", "b", "c"], ["a", "b", "c", "d", "e"],
            ["a", "b", "c", "a"], ["a", "b", "c", " "], ["a", "b", "c", null!]
        })
            Assert.Throws<ArgumentException>(() => new QuestionDefinition("id", "text", choices, 0, "category", 1, "explanation"));
        var original = new[] { "α", "β", "γ", "δ" };
        var question = new QuestionDefinition("id", "Ερώτηση", original, 2, "category", 3, "Εξήγηση");
        original[2] = "changed";
        Assert.Equal("γ", question.Answers[2]);
        Assert.Throws<NotSupportedException>(() => ((IList<string>)question.Answers)[2] = "changed");
    }

    [Theory]
    [InlineData(0)]
    [InlineData(1)]
    [InlineData(2)]
    [InlineData(3)]
    public void RequiredQuestionStringsCannotBeBlank(int blankField)
    {
        var fields = new[] { "id", "text", "category", "explanation" };
        fields[blankField] = " ";
        Assert.Throws<ArgumentException>(() => new QuestionDefinition(fields[0], fields[1],
            ["a", "b", "c", "d"], 0, fields[2], 1, fields[3]));
    }

    [Fact]
    public void PlayerIdentityAndPresentationInputsAreValidated()
    {
        var id = new PlayerId(Guid.Parse("10000000-0000-0000-0000-000000000001"));
        Assert.Throws<ArgumentException>(() => new Player(default, "Άννα"));
        Assert.Throws<ArgumentException>(() => new Player(id, " "));
        Assert.Throws<ArgumentOutOfRangeException>(() => new Player(id, new string('a', 33)));
        Assert.Throws<ArgumentOutOfRangeException>(() => new Player(id, "Άννα", new(0)));
        Assert.Throws<ArgumentOutOfRangeException>(() => new Player(id, "Άννα", localSlot: new(-1)));
        Assert.Throws<ArgumentOutOfRangeException>(() => new Player(id, "Άννα", localSlot: new(8)));
    }

    [Fact]
    public void SessionRejectsEmptyOversizedNullAndDuplicateRosters()
    {
        var fixture = new SessionFixture();
        GameSession Create(IEnumerable<Player> players) => new(GameAuthority.Host, players, fixture.Clock, new SeededRandomSource(0));
        Assert.Throws<ArgumentException>(() => Create([]));
        Assert.Throws<ArgumentException>(() => Create([fixture.Players[0], fixture.Players[0]]));
        Assert.Throws<ArgumentException>(() => Create([null!]));
        Assert.Throws<ArgumentException>(() => Create(Enumerable.Repeat(fixture.Players[0], 9)));
        var players = Enumerable.Range(1, 8).Select(index => new Player(new(new Guid(index, 0, 0, new byte[8])), $"Player {index}")).ToArray();
        Assert.Equal(8, Create(players).GetSnapshot().Scores.Count);
    }

    [Fact]
    public void MultiplePlayersCanShareOneConnectionWithSeparateLocalSlotsAndCopiedRoster()
    {
        var fixture = new SessionFixture();
        var snapshot = fixture.Session.GetSnapshot();
        Assert.Equal(fixture.Players[1].ConnectionId, fixture.Players[2].ConnectionId);
        Assert.NotEqual(fixture.Players[1].LocalSlot, fixture.Players[2].LocalSlot);
        fixture.Players[0] = fixture.Players[1];
        Assert.Equal("Άννα", fixture.Session.GetSnapshot().Scores[0].DisplayName);
        Assert.Equal(3, snapshot.Scores.Count);
    }

    [Fact]
    public void InvalidQuestionTimingDoesNotChangeStateOrConsumeInstanceId()
    {
        var fixture = new SessionFixture();
        fixture.Session.Initialize();
        fixture.Session.OpenLobby();
        fixture.Session.StartGame();
        fixture.Session.BeginRound();
        Assert.Equal(GameError.InvalidQuestionInstance,
            fixture.Session.StartQuestion(SessionFixture.Question, default, SessionFixture.Duration));
        foreach (var duration in new[] { TimeSpan.Zero, TimeSpan.FromTicks(-1), TimeSpan.MaxValue })
            Assert.Throws<ArgumentOutOfRangeException>(() =>
                fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, duration));
        Assert.Equal(GamePhase.RoundIntro, fixture.Session.Phase);
        Assert.Equal(GameError.None,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration));
    }

    [Fact]
    public void EmptyQuestionCanExpireAndNoScoreFallsBelowZero()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        fixture.Clock.Advance(SessionFixture.Duration + TimeSpan.FromTicks(1));
        Assert.Equal(GameError.None, fixture.Session.CloseQuestion());
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.All(fixture.Session.GetSnapshot().Reveal!.Players, result =>
        {
            Assert.Null(result.AnswerIndex);
            Assert.Equal(0, result.Points);
        });
        Assert.All(fixture.Session.GetSnapshot().Scores, score => Assert.Equal(0, score.Total));
    }

    [Fact]
    public void OldQuestionInstanceCannotBeReusedInARematch()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        fixture.Clock.Advance(SessionFixture.Duration + TimeSpan.FromTicks(1));
        fixture.Session.CloseQuestion();
        fixture.Session.RevealAnswer();
        fixture.Session.ShowScoreboard();
        fixture.Session.EndRound();
        fixture.Session.FinishGame();
        fixture.Session.ReturnToLobby();
        fixture.Session.StartGame();
        fixture.Session.BeginRound();
        Assert.Equal(GameError.InvalidQuestionInstance,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration));
        Assert.Equal(GamePhase.RoundIntro, fixture.Session.Phase);
        Assert.Equal(GameError.None,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.SecondInstance, SessionFixture.Duration));
    }

    [Fact]
    public void AnswerOutsideActiveQuestionIsRejected()
    {
        var fixture = new SessionFixture();
        var answer = new AnswerSubmission(fixture.Players[0].Id, SessionFixture.FirstInstance, 0);
        Assert.Equal(SubmissionError.InvalidState, fixture.Session.SubmitAnswer(answer));
        fixture.BeginQuestion();
        foreach (var index in Enumerable.Range(0, 3)) fixture.Session.SubmitAnswer(fixture.Answer(index));
        Assert.Equal(SubmissionError.InvalidState, fixture.Session.SubmitAnswer(answer));
        fixture.Session.RevealAnswer();
        Assert.Equal(SubmissionError.InvalidState, fixture.Session.SubmitAnswer(answer));
    }

    [Fact]
    public void SeededRandomEnforcesExclusiveUpperBound()
    {
        var random = new SeededRandomSource(42);
        Assert.Throws<ArgumentOutOfRangeException>(() => random.Next(0));
        Assert.Throws<ArgumentOutOfRangeException>(() => random.Next(-1));
        for (var i = 0; i < 50; i++) Assert.InRange(random.Next(4), 0, 3);
    }
}

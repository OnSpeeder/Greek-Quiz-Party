using System.Text.Json;
using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Scoring;
using Xunit;
using Xunit.Abstractions;

namespace QuizParty.Core.Tests;

public class GameSessionTests(ITestOutputHelper output)
{
    [Fact]
    public void BasicMatchRunsFromBootToGameOverWithCorrectWrongAndUnansweredPlayers()
    {
        var fixture = new SessionFixture();
        var session = fixture.Session;
        fixture.BeginQuestion();
        var started = session.GetSnapshot();
        Assert.Equal(SubmissionError.None, session.SubmitAnswer(fixture.Answer()));
        fixture.Clock.Advance(TimeSpan.FromSeconds(5));
        Assert.Equal(SubmissionError.None, session.SubmitAnswer(fixture.Answer(1, (fixture.CorrectIndex + 1) % 4)));
        Assert.Equal(GameError.QuestionNotReady, session.CloseQuestion());
        Assert.All(session.GetSnapshot().Scores, score => Assert.Equal(0, score.Total));
        Assert.Null(session.GetSnapshot().Reveal);
        fixture.Clock.Advance(TimeSpan.FromSeconds(5) + TimeSpan.FromTicks(1));
        Assert.Equal(GameError.None, session.CloseQuestion());
        Assert.Null(session.GetSnapshot().Reveal);
        Assert.Equal(GameError.None, session.RevealAnswer());
        var revealed = session.GetSnapshot();
        Assert.Equal("Η Αθήνα είναι η πρωτεύουσα της Ελλάδας.", revealed.Reveal!.Explanation);
        Assert.Equal(1000, revealed.Scores[0].Total);
        Assert.Equal(0, revealed.Scores[1].Total);
        Assert.Equal(0, revealed.Scores[2].Total);
        Assert.True(revealed.Reveal.Players[0].IsCorrect);
        Assert.False(revealed.Reveal.Players[1].IsCorrect);
        Assert.NotNull(revealed.Reveal.Players[1].AnswerIndex);
        Assert.Null(revealed.Reveal.Players[2].AnswerIndex);
        Assert.Equal(GameError.InvalidTransition, session.RevealAnswer());
        Assert.Equal(1000, session.GetSnapshot().Scores[0].Total);
        Assert.Equal(GameError.None, session.ShowScoreboard());
        Assert.Equal(GameError.None, session.EndRound());
        Assert.Equal(GameError.None, session.FinishGame());
        Assert.Equal(GamePhase.GameOver, session.Phase);
        // Previously obtained snapshots remain unchanged after host mutations.
        Assert.Equal(GamePhase.QuestionActive, started.Phase);
        Assert.All(started.Scores, score => Assert.Equal(0, score.Total));
        Assert.Null(started.Reveal);
        Assert.Equal(GameError.None, session.ReturnToLobby());
        Assert.Null(session.GetSnapshot().Question);
        Assert.Null(session.GetSnapshot().Reveal);
        Assert.Equal(GameError.None, session.StartGame());
        Assert.All(session.GetSnapshot().Scores, score => Assert.Equal(0, score.Total));
        output.WriteLine("Observed Core flow: Boot -> Lobby -> QuestionActive -> timeout lock -> reveal -> scoreboard -> GameOver -> fresh game; totals 1000/0/0, reveal awarded once.");
    }

    [Fact]
    public void AllEligibleAnswersLockImmediatelyAndNextQuestionAndRoundAreSupported()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        foreach (var index in Enumerable.Range(0, 3))
            Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(fixture.Answer(index)));
        Assert.Equal(GamePhase.QuestionLocked, fixture.Session.Phase);
        Assert.Null(fixture.Session.GetSnapshot().Reveal);
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.Equal(GameError.None, fixture.Session.ShowScoreboard());
        Assert.Equal(GameError.InvalidQuestionInstance,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration));
        Assert.Equal(GameError.None,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.SecondInstance, SessionFixture.Duration));
        Assert.Equal(0, fixture.Session.GetSnapshot().AcceptedAnswerCount);
        Assert.Null(fixture.Session.GetSnapshot().Reveal);
        Assert.Equal(SubmissionError.StaleQuestion, fixture.Session.SubmitAnswer(fixture.Answer() with
            { QuestionInstanceId = SessionFixture.FirstInstance }));
        foreach (var index in Enumerable.Range(0, 3))
            Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(fixture.Answer(index)));
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.All(fixture.Session.GetSnapshot().Scores, score => Assert.Equal(2000, score.Total));
        Assert.Equal(GameError.None, fixture.Session.ShowScoreboard());
        Assert.Equal(GameError.None, fixture.Session.EndRound());
        Assert.Equal(GameError.None, fixture.Session.BeginRound());
        Assert.Equal(GamePhase.RoundIntro, fixture.Session.Phase);
    }

    [Fact]
    public void DuplicateSubmissionCannotReplaceTheFirstAnswerOrChangeReceiptTime()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        var first = fixture.Answer();
        Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(first));
        fixture.Clock.Advance(TimeSpan.FromSeconds(4));
        Assert.Equal(SubmissionError.AlreadyAnswered, fixture.Session.SubmitAnswer(first));
        Assert.Equal(SubmissionError.AlreadyAnswered, fixture.Session.SubmitAnswer(first with { AnswerIndex = (first.AnswerIndex + 1) % 4 }));
        Assert.Equal(1, fixture.Session.GetSnapshot().AcceptedAnswerCount);
        fixture.Clock.Advance(TimeSpan.FromSeconds(7));
        Assert.Equal(GameError.None, fixture.Session.CloseQuestion());
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.Equal(1000, fixture.Session.GetSnapshot().Scores[0].Total);
    }

    [Theory]
    [InlineData(-1)]
    [InlineData(4)]
    [InlineData(int.MaxValue)]
    [InlineData(int.MinValue)]
    public void InvalidAnswerIndexDoesNotConsumeSubmission(int index)
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        Assert.Equal(SubmissionError.InvalidAnswerIndex, fixture.Session.SubmitAnswer(fixture.Answer() with { AnswerIndex = index }));
        Assert.Equal(0, fixture.Session.GetSnapshot().AcceptedAnswerCount);
        Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(fixture.Answer()));
    }

    [Theory]
    [InlineData(0)]
    [InlineData(2)]
    [InlineData(3)]
    [InlineData(4)]
    [InlineData(-1)]
    public void UndefinedAndDeferredConfidenceLevelsAreRejected(int confidence)
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        Assert.Equal(SubmissionError.InvalidConfidence,
            fixture.Session.SubmitAnswer(fixture.Answer() with { Confidence = (ConfidenceLevel)confidence }));
        Assert.Equal(0, fixture.Session.GetSnapshot().AcceptedAnswerCount);
    }

    [Fact]
    public void UnknownPlayerAndStaleQuestionAreRejectedWithoutChangingState()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        Assert.Equal(SubmissionError.UnknownPlayer, fixture.Session.SubmitAnswer(fixture.Answer() with { PlayerId = default }));
        Assert.Equal(SubmissionError.StaleQuestion,
            fixture.Session.SubmitAnswer(fixture.Answer() with { QuestionInstanceId = default }));
        Assert.Equal(0, fixture.Session.GetSnapshot().AcceptedAnswerCount);
        Assert.Equal(GameError.InvalidTransition, fixture.Session.RevealAnswer());
        Assert.Equal(GameError.InvalidTransition, fixture.Session.FinishGame());
        Assert.Equal(GameError.InvalidTransition,
            fixture.Session.StartQuestion(SessionFixture.Question, SessionFixture.SecondInstance, SessionFixture.Duration));
        Assert.Equal(GamePhase.QuestionActive, fixture.Session.Phase);
    }

    [Fact]
    public void ExactDeadlineIsAcceptedAndOneTickLaterIsRejected()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        fixture.Clock.Advance(SessionFixture.Duration);
        Assert.Equal(GameError.QuestionNotReady, fixture.Session.CloseQuestion());
        Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(fixture.Answer()));
        fixture.Clock.Advance(TimeSpan.FromTicks(1));
        Assert.Equal(SubmissionError.Late, fixture.Session.SubmitAnswer(fixture.Answer(1)));
        Assert.Equal(GameError.None, fixture.Session.CloseQuestion());
        Assert.Equal(SubmissionError.InvalidState, fixture.Session.SubmitAnswer(fixture.Answer(2)));
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.Equal(500, fixture.Session.GetSnapshot().Scores[0].Total);
        Assert.Equal(0, fixture.Session.GetSnapshot().Scores[1].Total);
    }

    [Fact]
    public void CapturedHostReceiptDeterminesScoreRatherThanProcessingTime()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        var receipt = fixture.Clock.Now + TimeSpan.FromSeconds(2);
        fixture.Clock.Advance(TimeSpan.FromSeconds(11));
        Assert.Equal(SubmissionError.None, fixture.Session.SubmitAnswer(fixture.Answer(), receipt));
        Assert.Equal(GameError.None, fixture.Session.CloseQuestion());
        Assert.Equal(GameError.None, fixture.Session.RevealAnswer());
        Assert.Equal(900, fixture.Session.GetSnapshot().Scores[0].Total);
    }

    [Fact]
    public void ReceiptsBeforeStartOrInFutureAreRejected()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        Assert.Equal(SubmissionError.TooEarly,
            fixture.Session.SubmitAnswer(fixture.Answer(), fixture.Clock.Now - TimeSpan.FromTicks(1)));
        Assert.Equal(SubmissionError.InvalidReceiveTime,
            fixture.Session.SubmitAnswer(fixture.Answer(), fixture.Clock.Now + TimeSpan.FromTicks(1)));
        Assert.Equal(0, fixture.Session.GetSnapshot().AcceptedAnswerCount);
    }

    [Fact]
    public void EveryClientMutationIsRejected()
    {
        var fixture = new SessionFixture(GameAuthority.Client);
        var session = fixture.Session;
        Assert.Equal(GameError.NotAuthoritative, session.Initialize());
        Assert.Equal(GameError.NotAuthoritative, session.OpenLobby());
        Assert.Equal(GameError.NotAuthoritative, session.StartGame());
        Assert.Equal(GameError.NotAuthoritative, session.BeginRound());
        Assert.Equal(GameError.NotAuthoritative, session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration));
        Assert.Equal(SubmissionError.NotAuthoritative, session.SubmitAnswer(new(fixture.Players[0].Id, SessionFixture.FirstInstance, 0)));
        Assert.Equal(GameError.NotAuthoritative, session.CloseQuestion());
        Assert.Equal(GameError.NotAuthoritative, session.RevealAnswer());
        Assert.Equal(GameError.NotAuthoritative, session.ShowScoreboard());
        Assert.Equal(GameError.NotAuthoritative, session.EndRound());
        Assert.Equal(GameError.NotAuthoritative, session.FinishGame());
        Assert.Equal(GameError.NotAuthoritative, session.ReturnToLobby());
        Assert.Equal(GamePhase.Boot, session.Phase);
        Assert.All(session.GetSnapshot().Scores, score => Assert.Equal(0, score.Total));
    }

    [Fact]
    public void SnapshotsDoNotExposeCorrectnessUntilRevealAndCollectionsCannotBeMutated()
    {
        var fixture = new SessionFixture();
        fixture.BeginQuestion();
        var snapshot = fixture.Session.GetSnapshot();
        var json = JsonSerializer.Serialize(snapshot);
        Assert.DoesNotContain("CorrectAnswer", json);
        Assert.DoesNotContain("Explanation", json);
        Assert.DoesNotContain("IsCorrect", json);
        Assert.Throws<NotSupportedException>(() => ((IList<string>)snapshot.Question!.Answers)[0] = "tampered");
        Assert.Throws<NotSupportedException>(() => ((IList<PlayerScore>)snapshot.Scores).Clear());
        fixture.Clock.Advance(SessionFixture.Duration + TimeSpan.FromTicks(1));
        fixture.Session.CloseQuestion();
        Assert.DoesNotContain("CorrectAnswer", JsonSerializer.Serialize(fixture.Session.GetSnapshot()));
        fixture.Session.RevealAnswer();
        var reveal = fixture.Session.GetSnapshot().Reveal!;
        Assert.Throws<NotSupportedException>(() => ((IList<PlayerQuestionResult>)reveal.Players).Clear());
        Assert.Contains("CorrectAnswerIndex", JsonSerializer.Serialize(fixture.Session.GetSnapshot()));
        Assert.Null(snapshot.Reveal);
    }

    [Fact]
    public void SeedAndClockProduceIdenticalPublicStateAndResults()
    {
        var first = new SessionFixture();
        var second = new SessionFixture();
        foreach (var fixture in new[] { first, second })
        {
            fixture.BeginQuestion();
            fixture.Clock.Advance(TimeSpan.FromSeconds(3));
            foreach (var index in Enumerable.Range(0, 3)) fixture.Session.SubmitAnswer(fixture.Answer(index));
            fixture.Session.RevealAnswer();
        }
        Assert.Equal(JsonSerializer.Serialize(first.Session.GetSnapshot()), JsonSerializer.Serialize(second.Session.GetSnapshot()));
        Assert.All(first.Session.GetSnapshot().Scores, score => Assert.Equal(850, score.Total));
    }

    [Fact]
    public void InjectedShufflePreservesCorrectAnswerMappingAndSourceContent()
    {
        var fixture = new SessionFixture(random: new SequenceRandom(0, 0, 0));
        fixture.BeginQuestion();
        Assert.Equal(new[] { "Πάτρα", "Λάρισα", "Χανιά", "Αθήνα" }, fixture.Session.GetSnapshot().Question!.Answers);
        foreach (var index in Enumerable.Range(0, 3)) fixture.Session.SubmitAnswer(fixture.Answer(index, 3));
        fixture.Session.RevealAnswer();
        Assert.Equal(3, fixture.Session.GetSnapshot().Reveal!.CorrectAnswerIndex);
        Assert.All(fixture.Session.GetSnapshot().Reveal!.Players, result => Assert.True(result.IsCorrect));
    }

    [Fact]
    public void SessionUsesConfiguredBaseAndTimeBonus()
    {
        var fixture = new SessionFixture();
        var session = new GameSession(GameAuthority.Host, [fixture.Players[0]], fixture.Clock,
            new SeededRandomSource(1), new ScoringRules(100, 20));
        session.Initialize();
        session.OpenLobby();
        session.StartGame();
        session.BeginRound();
        session.StartQuestion(SessionFixture.Question, SessionFixture.FirstInstance, SessionFixture.Duration);
        var correct = session.GetSnapshot().Question!.Answers.ToList().IndexOf("Αθήνα");
        fixture.Clock.Advance(TimeSpan.FromSeconds(5));
        Assert.Equal(SubmissionError.None, session.SubmitAnswer(new(fixture.Players[0].Id, SessionFixture.FirstInstance, correct)));
        Assert.Equal(GameError.None, session.RevealAnswer());
        Assert.Equal(110, session.GetSnapshot().Scores[0].Total);
    }
}

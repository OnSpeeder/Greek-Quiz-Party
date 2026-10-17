using QuizParty.Core.Game;
using QuizParty.Core.Players;
using QuizParty.Core.Questions;
using QuizParty.Core.Randomness;
using QuizParty.Core.Time;
using Xunit;

namespace QuizParty.Core.Tests;

internal sealed class FakeClock : IGameClock
{
    public TimeSpan Now { get; set; } = TimeSpan.FromSeconds(100);
    public void Advance(TimeSpan amount) => Now += amount;
}

internal sealed class SequenceRandom(params int[] values) : IRandomSource
{
    private int _index;
    public int Next(int exclusiveUpperBound)
    {
        var value = values[_index++];
        Assert.InRange(value, 0, exclusiveUpperBound - 1);
        return value;
    }
}

internal sealed class SessionFixture
{
    public static readonly TimeSpan Duration = TimeSpan.FromSeconds(10);
    public static readonly QuestionInstanceId FirstInstance = new(Guid.Parse("20000000-0000-0000-0000-000000000001"));
    public static readonly QuestionInstanceId SecondInstance = new(Guid.Parse("20000000-0000-0000-0000-000000000002"));
    public static QuestionDefinition Question => new("test_geography", "Ποια είναι η πρωτεύουσα;",
        ["Αθήνα", "Πάτρα", "Λάρισα", "Χανιά"], 0, "geography", 1, "Η Αθήνα είναι η πρωτεύουσα της Ελλάδας.");

    public FakeClock Clock { get; } = new();
    public Player[] Players { get; } =
    [
        new(new(Guid.Parse("10000000-0000-0000-0000-000000000001")), "Άννα", localSlot: new(0)),
        new(new(Guid.Parse("10000000-0000-0000-0000-000000000002")), "Νίκος", new(42), new(0)),
        new(new(Guid.Parse("10000000-0000-0000-0000-000000000003")), "Μαρία", new(42), new(1))
    ];
    public GameSession Session { get; }

    public SessionFixture(GameAuthority authority = GameAuthority.Host, IRandomSource? random = null)
    {
        Session = new(authority, Players, Clock, random ?? new SeededRandomSource(123));
    }

    public void BeginQuestion()
    {
        Assert.Equal(GameError.None, Session.Initialize());
        Assert.Equal(GameError.None, Session.OpenLobby());
        Assert.Equal(GameError.None, Session.StartGame());
        Assert.Equal(GameError.None, Session.BeginRound());
        Assert.Equal(GameError.None, Session.StartQuestion(Question, FirstInstance, Duration));
    }

    public AnswerSubmission Answer(int playerIndex = 0, int? answerIndex = null) =>
        new(Players[playerIndex].Id, Session.GetSnapshot().Question!.InstanceId,
            answerIndex ?? CorrectIndex);

    public int CorrectIndex => Session.GetSnapshot().Question!.Answers.ToList().IndexOf("Αθήνα");
}

namespace QuizParty.Core.Players;

public enum CharacterId { Pink, Blue, Orange, Green, Purple, Yeti, Coral, Teal }

public static class Characters
{
    public const int Count = 8;
    public static bool IsValid(int value) => value is >= 0 and < Count;
}

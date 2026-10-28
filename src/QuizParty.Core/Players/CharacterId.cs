namespace QuizParty.Core.Players;

public enum CharacterId { Pink, Blue, Orange, Green, Purple, Yeti, Coral, Teal, Gold, Lavender }

public static class Characters
{
    public const int Count = 10;
    public static bool IsValid(int value) => value is >= 0 and < Count;
}

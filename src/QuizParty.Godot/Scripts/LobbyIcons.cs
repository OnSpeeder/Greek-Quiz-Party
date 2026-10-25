using Godot;

namespace QuizParty.Presentation;

/// <summary>Intentional line pictograms for lobby controls and the existing category catalogue.</summary>
public static class LobbyIcons
{
    public static Texture2D Texture(string id)
    {
        var shape = id switch
        {
            "ready" => "<circle cx='32' cy='32' r='27' fill='#1AD598'/><path d='m17 32 10 10 20-22' stroke='#0F0A26'/>",
            "waiting" => "<circle cx='32' cy='32' r='27' stroke='#FFB800'/><path d='M23 18h18m-18 28h18M24 18c0 14 16 14 16 28M40 18c0 14-16 14-16 28' stroke='#FFB800'/>",
            "rules" => "<path d='M7 12q13-6 25 2 12-8 25-2v41q-13-6-25 0-12-6-25 0ZM32 14v39M14 23h10m-10 9h10m16-9h10m-10 9h10'/>",
            "categories" or "geography" => "<circle cx='32' cy='32' r='26'/><ellipse cx='32' cy='32' rx='12' ry='26'/><path d='M7 25h50M7 39h50'/>",
            "greece" => "<path d='M9 58V7h47v34H9M9 18h47M9 29h47M9 40h47M9 7h20v22H9m10-22v22M9 18h20'/>",
            "history" => "<path d='M7 53h50M11 18h42L32 6ZM14 24v23m12-23v23m12-23v23m12-23v23'/>",
            "science" => "<ellipse cx='32' cy='32' rx='29' ry='11'/><ellipse cx='32' cy='32' rx='29' ry='11' transform='rotate(60 32 32)'/><ellipse cx='32' cy='32' rx='29' ry='11' transform='rotate(120 32 32)'/><circle cx='32' cy='32' r='3' fill='#FFC83B'/>",
            "technology" => "<rect x='15' y='15' width='34' height='34' rx='6'/><rect x='24' y='24' width='16' height='16'/><path d='M23 7v8m18-8v8M23 49v8m18-8v8M7 23h8m-8 18h8m34-18h8m-8 18h8'/>",
            "cinema_tv" => "<rect x='5' y='16' width='39' height='35' rx='5'/><path d='m44 28 15-9v30l-15-9M13 7l9 9M33 7l-9 9'/>",
            "music" => "<path d='M25 45V15l28-7v30M25 24l28-7'/><ellipse cx='16' cy='47' rx='9' ry='7' fill='#FFC83B'/><ellipse cx='44' cy='40' rx='9' ry='7' fill='#FFC83B'/>",
            "sports" => "<circle cx='32' cy='32' r='26'/><path d='m32 19 13 9-5 16H24l-5-16ZM32 19V6M19 28 7 23m17 21-7 10m23-10 7 10m-2-26 12-5'/>",
            "setup" or "gaming" => "<path d='M20 20h24q9 0 12 13l4 15q1 10-8 7L40 45H24L12 55q-9 3-8-7l4-15q3-13 12-13Z'/><path d='M16 29v13m-6-6h13m20-5h1m7 7h1'/>",
            "pop_culture" => "<path d='m32 5 8 17 19 3-14 14 3 20-16-9-17 9 3-20L4 25l20-3Z'/>",
            "logic" => "<path d='M8 8h19q-6 15 5 15T37 8h19v19q-15-6-15 5t15 5v19H37q6-15-5-15t-5 15H8V37q15 6 15-5T8 27Z'/>",
            "wtf_facts" => "<circle cx='32' cy='32' r='26'/><path d='M23 22q0-13 15-8 14 8-4 18v6M34 47v2'/>",
            "cards" => "<rect x='13' y='8' width='38' height='48' rx='6'/><path d='m32 18 5 10 11 2-8 8 2 11-10-5-10 5 2-11-8-8 11-2Z'/>",
            "missions" => "<circle cx='32' cy='32' r='25'/><circle cx='32' cy='32' r='15'/><path d='m32 32 25-25M44 7h13v13'/>",
            _ => "<path d='m32 8 24 24-24 24L8 32Z'/><circle cx='32' cy='32' r='9'/>"
        };
        using var image = new Image();
        var error = image.LoadSvgFromString($"<svg xmlns='http://www.w3.org/2000/svg' width='64' height='64'><g fill='none' stroke='#FFC83B' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'>{shape}</g></svg>");
        if (error != Error.Ok) throw new InvalidOperationException($"Lobby icon {id}: {error}");
        return ImageTexture.CreateFromImage(image);
    }
}

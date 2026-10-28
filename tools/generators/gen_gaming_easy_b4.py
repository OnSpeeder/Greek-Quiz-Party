# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_easy_361",
        "text": "Ποιο είναι το επίσημο κύριο επάγγελμα του Mario στα περισσότερα κλασικά παιχνίδια της Nintendo;",
        "correct": "Υδραυλικός (Plumber)",
        "distractors": ["Μαραγκός", "Ηλεκτρολόγος", "Κηπουρός"],
        "explanation": "Αν και στο αρχικό Donkey Kong (1981) ξεκίνησε ως μαραγκός με το όνομα Jumpman, στο Mario Bros. (1983) καθιερώθηκε οριστικά ως Ιταλοαμερικανός υδραυλικός που ταξιδεύει μέσα από σωλήνες αποχέτευσης.",
        "funFacts": [
            "Ο Mario απέκτησε το επάγγελμα του υδραυλικού επειδή το παιχνίδι Mario Bros. διαδραματιζόταν στους υπονόμους της Νέας Υόρκης.",
            "Το 2017 η Nintendo ανέφερε προσωρινά στην ιστοσελίδα της ότι ο Mario είχε 'αποσυρθεί' από την υδραυλική, αλλά επανέφερε σύντομα τον επίσημο τίτλο του."
        ],
        "source": "https://en.wikipedia.org/wiki/Mario",
        "tags": ["gaming", "mario", "nintendo", "lore", "characters"]
    },
    {
        "id": "gaming_easy_362",
        "text": "Για ποιο λόγο ο Shigeru Miyamoto σχεδίασε τον Mario με μουστάκι και καπέλο στο αρχικό παιχνίδι 'Donkey Kong' (1981);",
        "correct": "Λόγω περιορισμών ανάλυσης pixel για να ξεχωρίζει η μύτη και τα μαλλιά",
        "distractors": ["Επειδή βασίστηκε στον ιδιοκτήτη της εταιρείας", "Για να φαίνεται μεγαλύτερος σε ηλικία", "Λόγω απαίτησης της αμερικανικής αγοράς"],
        "explanation": "Στα 8-bit γραφικά των 16x16 pixels ήταν αδύνατο να σχεδιαστεί εκφραστικό στόμα ή κινούμενα μαλλιά, οπότε το μουστάκι και το καπέλο έλυσαν το πρόβλημα κομψά.",
        "funFacts": [
            "Οι τιράντες με τα έντονα χρώματα προστέθηκαν επίσης για να ξεχωρίζουν τα χέρια του όταν έτρεχε και πηδούσε.",
            "Το όνομα 'Mario' δόθηκε προς τιμήν του Mario Segale, του ιδιοκτήτη των αποθηκών της Nintendo of America."
        ],
        "source": "https://en.wikipedia.org/wiki/Mario",
        "tags": ["gaming", "mario", "nintendo", "history", "design"]
    },
    {
        "id": "gaming_easy_363",
        "text": "Ποιο είναι το ιερό χρυσό κειμήλιο που αποτελείται από τρία ενωμένα ισόπλευρα τρίγωνα στη σειρά 'The Legend of Zelda';",
        "correct": "Triforce (Τρίforce)",
        "distractors": ["Master Core", "Sacred Relic", "Golden Crest"],
        "explanation": "Το Triforce δημιουργήθηκε από τις τρεις χρυσές θεότητες (Din, Nayru, Farore) κατά τη δημιουργία του κόσμου της Hyrule και μπορεί να πραγματοποιήσει οποιαδήποτε ευχή.",
        "funFacts": [
            "Κάθε τρίγωνο αντιπροσωπεύει μία αρετή: Δύναμη (Power), Σοφία (Wisdom) και Θάρρος (Courage).",
            "Το σύμβολο του Triforce είναι πανομοιότυπο με το ιστορικό οικόσημο (mon) της ιαπωνικής φυλής Hōjō."
        ],
        "source": "https://en.wikipedia.org/wiki/Triforce",
        "tags": ["gaming", "zelda", "nintendo", "triforce", "lore"]
    },
    {
        "id": "gaming_easy_364",
        "text": "Ποιο κομμάτι του Triforce κατέχει παραδοσιακά ο Link στη σειρά 'The Legend of Zelda';",
        "correct": "Triforce of Courage (Τρίγωνο του Θάρρους)",
        "distractors": ["Triforce of Wisdom (Σοφίας)", "Triforce of Power (Δύναμης)", "Triforce of Hope (Ελπίδας)"],
        "explanation": "Ο Link ενσαρκώνει την αρετή του Θάρρους (Courage), η πριγκίπισσα Zelda τη Σοφία (Wisdom) και ο πολέμαρχος Ganon τη Δύναμη (Power).",
        "funFacts": [
            "Όταν ένα άτομο με ακάθαρτη καρδιά αγγίζει το πλήρες Triforce, αυτό διασπάται στα τρία και ο επίδοξος κάτοχος κρατά μόνο την αρετή που εκτιμά περισσότερο.",
            "Το σύμβολο του Triforce λάμπει στο πίσω μέρος της παλάμης των εκλεκτών κατόχων του."
        ],
        "source": "https://en.wikipedia.org/wiki/Triforce",
        "tags": ["gaming", "zelda", "nintendo", "link", "triforce"]
    },
    {
        "id": "gaming_easy_365",
        "text": "Ποια είναι η πατρίδα και το χωριό από όπου ξεκινά το ταξίδι του ο Ash Ketchum στην περιοχή Kanto της σειράς 'Pokémon';",
        "correct": "Pallet Town",
        "distractors": ["Cerulean City", "Viridian City", "Lavender Town"],
        "explanation": "Το Pallet Town (Masara Town στην Ιαπωνία) είναι ένα ήσυχο χωριό όπου βρίσκεται το εργαστήριο του καθηγητή Oak και το σπίτι του Ash.",
        "funFacts": [
            "Στα ιαπωνικά το όνομα της πόλης είναι Masara Town, που παραπέμπει στο λευκό χρώμα (καμβάς για νέες αρχές).",
            "Στα πρώτα παιχνίδια Red & Blue, το Pallet Town αποτελείται από μόλις δύο σπίτια και το εργαστήριο."
        ],
        "source": "https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red_and_Blue",
        "tags": ["gaming", "pokemon", "nintendo", "pallet_town"]
    },
    {
        "id": "gaming_easy_366",
        "text": "Ποιο είναι το όνομα του διάσημου διδύμου κακοποιών της Team Rocket που απαγγέλλει συνεχώς το μότο του συνοδευόμενο από ένα ομιλούν Meowth;",
        "correct": "Jessie και James (Musashi & Kojiro)",
        "distractors": ["Butch και Cassidy", "Giovanni και Ariana", "Archer και Petrel"],
        "explanation": "Η Jessie και ο James είναι τα κωμικά μέλη της Team Rocket που προσπαθούν μάταια να κλέψουν τον Pikachu του Ash σε εκατοντάδες επεισόδια και spin-off παιχνίδια (π.χ. Pokémon Yellow).",
        "funFacts": [
            "Στα ιαπωνικά ονομάζονται Musashi και Kojiro, προς τιμήν των διάσημων ιστορικών Ιαπώνων σαμουράι Miyamoto Musashi και Sasaki Kojiro.",
            "Τα ονόματα Jessie και James επιλέχθηκαν στην αγγλική μεταγλώττιση προς τιμήν του διαβόητου Αμερικανού παράνομου Jesse James."
        ],
        "source": "https://en.wikipedia.org/wiki/Team_Rocket",
        "tags": ["gaming", "pokemon", "team_rocket", "anime"]
    },
    {
        "id": "gaming_easy_367",
        "text": "Ποια είναι τα τρία θρυλικά πουλιά (Legendary Birds) της πρώτης γενιάς Pokémon στην περιοχή Kanto;",
        "correct": "Articuno, Zapdos και Moltres",
        "distractors": ["Raikou, Entei και Suicune", "Lugia, Ho-Oh και Skarmory", "Pidgeot, Fearow και Dodrio"],
        "explanation": "Τα τρία μυθικά πουλιά αντιπροσωπεύουν τον Πάγο (Articuno), τον Ηλεκτρισμό (Zapdos) και τη Φωτιά (Moltres).",
        "funFacts": [
            "Τα ονόματά τους τελειώνουν στα ισπανικά αριθμητικά ένα, δύο, τρία: Artic-UNO, Zap-DOS, Mol-TRES.",
            "Στο Pokémon Platinum και στο Pokémon The Movie 2000, τα τρία πουλιά ελέγχονται από τον κυρίαρχο των θαλασσών Lugia."
        ],
        "source": "https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon",
        "tags": ["gaming", "pokemon", "nintendo", "legendary"]
    },
    {
        "id": "gaming_easy_368",
        "text": "Στο σύμπαν του 'Halo', ποιος ήταν ο αρχικός πραγματικός σκοπός για τον οποίο οι αρχαίοι Forerunners κατασκεύασαν τα δαχτυλίδια Halo;",
        "correct": "Να εξαλείψουν όλη τη συνειδητή ζωή στον γαλαξία ώστε να λιμοκτονήσει το παράσιτο Flood",
        "distractors": ["Να λειτουργήσουν ως διαστημικά καταφύγια αποικισμού", "Να παραγάγουν απεριόριστη ενέργεια σύντηξης", "Να πολεμήσουν τις δυνάμεις του Covenant"],
        "explanation": "Τα δαχτυλίδια Halo είναι υπερόπλα μαζικής καταστροφής έσχατης ανάγκης: εκπέμπουν ακτινοβολία που σκοτώνει κάθε οργανισμό με νευρικό σύστημα για να στερήσουν τροφή από το Flood.",
        "funFacts": [
            "Κάθε εγκατάσταση Halo έχει διάμετρο 10.000 χιλιομέτρων και διαθέτει δική της ατμόσφαιρα και οικοσυστήματα στην εσωτερική της επιφάνεια.",
            "Υπήρχαν συνολικά 7 ενεργά δαχτυλίδια Halo στον γαλαξία."
        ],
        "source": "https://en.wikipedia.org/wiki/Halo_(megastructure)",
        "tags": ["gaming", "halo", "xbox", "lore", "sci_fi"]
    },
    {
        "id": "gaming_easy_369",
        "text": "Ποιο στούντιο ανάπτυξης δημιούργησε αρχικά τη σειρά 'Halo' πριν ανεξαρτητοποιηθεί και δημιουργήσει το franchise 'Destiny';",
        "correct": "Bungie",
        "distractors": ["343 Industries", "Epic Games", "Infinity Ward"],
        "explanation": "Η Bungie ανέπτυξε τα Halo: Combat Evolved, Halo 2, Halo 3, ODST και Reach, πριν παραδώσει τα ηνία στην 343 Industries και προχωρήσει στο Destiny.",
        "funFacts": [
            "Το Halo ξεκίνησε αρχικά το 1999 ως παιχνίδι στρατηγικής πραγματικού χρόνου (RTS) για υπολογιστές Mac και παρουσιάστηκε στη σκηνή από τον Steve Jobs.",
            "Η Microsoft εξαγόρασε την Bungie το 2000 κάνοντας το Halo τον κεντρικό τίτλο λανσαρίσματος του πρώτου Xbox."
        ],
        "source": "https://en.wikipedia.org/wiki/Bungie",
        "tags": ["gaming", "bungie", "halo", "destiny", "industry"]
    },
    {
        "id": "gaming_easy_370",
        "text": "Ποιος είναι ο πρωταγωνιστής του 'Grand Theft Auto IV' (2008), ένας βετεράνος πολέμου από την Ανατολική Ευρώπη που φτάνει στη Liberty City;",
        "correct": "Niko Bellic",
        "distractors": ["Roman Bellic", "Packie McReary", "Little Jacob"],
        "explanation": "Ο Niko Bellic μεταναστεύει στην Αμερική πιστεύοντας τα ψέματα του ξαδέλφου του Roman για πλούτη και πολυτέλεια, μόνο για να βρεθεί μπλεγμένος στον υπόκοσμο.",
        "funFacts": [
            "Ο ξάδελφος Roman έγινε διάσημος επειδή τηλεφωνούσε συνεχώς στον Niko ρωτώντας αν θέλει να πάνε για μπόουλινγκ ('Hey Niko, let's go bowling!').",
            "Το GTA IV ήταν το πρώτο παιχνίδι της Rockstar που χρησιμοποίησε τη μηχανή RAGE μαζί με το πρωτοποριακό σύστημα φυσικής κίνησης Euphoria."
        ],
        "source": "https://en.wikipedia.org/wiki/Niko_Bellic",
        "tags": ["gaming", "gta", "rockstar", "gta_iv", "characters"]
    },
    {
        "id": "gaming_easy_371",
        "text": "Ποιος είναι ο κεντρικός πρωταγωνιστής στο αριστουργηματικό γουέστερν 'Red Dead Redemption 2' (2018) της Rockstar Games;",
        "correct": "Arthur Morgan",
        "distractors": ["John Marston", "Dutch van der Linde", "Bill Williamson"],
        "explanation": "Ο Arthur Morgan είναι το δεξί χέρι του Dutch van der Linde και βασικό στέλεχος της συμμορίας που προσπαθεί να επιβιώσει στη δύση της Άγριας Δύσης στα τέλη του 19ου αιώνα.",
        "funFacts": [
            "Τον Arthur Morgan υποδύθηκε ο ηθοποιός Roger Clark, κερδίζοντας το βραβείο Best Performance στα The Game Awards 2018.",
            "Το ημερολόγιο του Arthur περιέχει πανέμορφα σκίτσα και προσωπικές σκέψεις που ενημερώνονται δυναμικά καθώς ο παίκτης εξερευνά τον κόσμο."
        ],
        "source": "https://en.wikipedia.org/wiki/Arthur_Morgan_(Red_Dead)",
        "tags": ["gaming", "red_dead_redemption", "rockstar", "arthur_morgan"]
    },
    {
        "id": "gaming_easy_372",
        "text": "Ποια διάσημη ατάκα επαναλαμβάνουν συχνά οι φρουροί στις πόλεις του 'The Elder Scrolls V: Skyrim';",
        "correct": "I used to be an adventurer like you, then I took an arrow in the knee",
        "distractors": ["Stop right there, criminal scum!", "Stay awhile and listen", "Praise the Sun!"],
        "explanation": "Η φράση 'Κάποτε ήμουν κι εγώ ένας τυχοδιώκτης σαν εσένα, μέχρι που δέχτηκα ένα βέλος στο γόνατο' έγινε ένα από τα μεγαλύτερα παγκόσμια memes στην ιστορία του gaming.",
        "funFacts": [
            "Η ατάκα γράφτηκε από τον Emil Pagliarulo της Bethesda απλώς για να δώσει λίγη προσωπικότητα και υπόβαθρο στους ανώνυμους φρουρούς.",
            "Αν ο παίκτης κλέψει έστω και ένα γλυκό (sweetroll), οι φρουροί σχολιάζουν ειρωνικά: 'Let me guess... someone stole your sweetroll?'."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
        "tags": ["gaming", "skyrim", "bethesda", "memes", "rpg"]
    },
    {
        "id": "gaming_easy_373",
        "text": "Ποιο ιαπωνικό στούντιο ανάπτυξης είναι υπεύθυνο για τη δημιουργία των παιχνιδιών 'Dark Souls', 'Bloodborne' και 'Elden Ring';",
        "correct": "FromSoftware",
        "distractors": ["Capcom", "Square Enix", "Kojima Productions"],
        "explanation": "Η FromSoftware, υπό την καλλιτεχνική καθοδήγηση του Hidetaka Miyazaki, δημιούργησε το εξαιρετικά επιδραστικό είδος παιχνιδιών 'Soulsborne'.",
        "funFacts": [
            "Η FromSoftware ιδρύθηκε το 1986 αρχικά ως εταιρεία ανάπτυξης λογισμικού γραφείου πριν στραφεί στα βιντεοπαιχνίδια με το King's Field το 1994.",
            "Η σειρά παιχνιδιών μάχης με γιγάντια mecha 'Armored Core' ανήκει επίσης στη FromSoftware."
        ],
        "source": "https://en.wikipedia.org/wiki/FromSoftware",
        "tags": ["gaming", "fromsoftware", "dark_souls", "elden_ring", "industry"]
    },
    {
        "id": "gaming_easy_374",
        "text": "Ποιος διάσημος συγγραφέας του 'A Song of Ice and Fire' (Game of Thrones) συνεργάστηκε με τον Hidetaka Miyazaki για τη μυθολογία του 'Elden Ring';",
        "correct": "George R. R. Martin",
        "distractors": ["J. K. Rowling", "Brandon Sanderson", "Neil Gaiman"],
        "explanation": "Ο George R. R. Martin έγραψε την ιστορία του αρχαίου παρελθόντος, τη δημιουργία των Ημίθεων και τη δυναστεία της Βασίλισσας Marika στον κόσμο των Lands Between.",
        "funFacts": [
            "Ο Martin δήλωσε ότι εντυπωσιάστηκε βαθιά από το τελικό αποτέλεσμα του παιχνιδιού και το χαρακτήρισε έργο τέχνης.",
            "Όλα τα ονόματα των κύριων ημίθεων στο παιχνίδι ξεκινούν με τα αρχικά του συγγραφέα: G, R, M (Godfrey, Godwyn, Radagon, Rennala, Ranni, Malenia, Miquella κ.ά.)."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "tags": ["gaming", "elden_ring", "fromsoftware", "george_rr_martin"]
    },
    {
        "id": "gaming_easy_375",
        "text": "Πώς ονομάζεται το πιστό φασματικό άλογο που ιππεύει ο Tarnished για να διασχίσει τον τεράστιο ανοιχτό κόσμο του 'Elden Ring';",
        "correct": "Torrent",
        "distractors": ["Shadowmere", "Roach", "Agro"],
        "explanation": "Το Torrent δίνεται στον παίκτη από τη Melina και μπορεί να κάνει διπλό άλμα στον αέρα και να χρησιμοποιεί πνευματικές στήλες ανέμου (Spiritsprings) για να πηδάει ψηλούς γκρεμούς.",
        "funFacts": [
            "Ο παίκτης καλεί το Torrent χρησιμοποιώντας το αντικείμενο Spectral Steed Whistle (Φασματική Σφυρίχτρα).",
            "Στο expansion 'Shadow of the Erdtree' αποκαλύπτονται περισσότερες λεπτομέρειες για τη σύνδεση του Torrent με τον Miquella."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "tags": ["gaming", "elden_ring", "fromsoftware", "torrent"]
    },
    {
        "id": "gaming_easy_376",
        "text": "Στο παιχνίδι 'Portal', ποια περίφημη φράση είναι γραμμένη ως προειδοποίηση στους τοίχους των μυστικών δωματίων από τον Doug Rattmann;",
        "correct": "The cake is a lie (Το κέικ είναι ψέμα)",
        "distractors": ["The portal is closed", "GLaDOS is watching", "There is no exit"],
        "explanation": "Η GLaDOS υπόσχεται διαρκώς στην Chell ότι στο τέλος των δοκιμασιών την περιμένει νόστιμο κέικ, αλλά οι τοίχοι αποκαλύπτουν ότι πρόκειται για παγίδα θανάτου.",
        "funFacts": [
            "Η φράση 'The cake is a lie' έγινε μία από τις πιο αναγνωρίσιμες εκφράσεις της σύγχρονης ποπ κουλτούρας και του ίντερνετ.",
            "Στο τέλος των τίτλων τέλους του Portal, η κάμερα δείχνει όντως ένα σοκολατένιο κέικ με ένα αναμμένο κεράκι σε ένα σκοτεινό δωμάτιο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_cake_is_a_lie",
        "tags": ["gaming", "portal", "valve", "memes"]
    },
    {
        "id": "gaming_easy_377",
        "text": "Στο 'Half-Life 2', ποια δυστοπική πόλη της Ανατολικής Ευρώπης βρίσκεται υπό την κατοχή της διαγαλαξιακής αυτοκρατορίας Combine;",
        "correct": "City 17",
        "distractors": ["City 13", "Rapture", "Midgar"],
        "explanation": "Ο Gordon Freeman φτάνει με το τρένο στον κεντρικό σταθμό της City 17, όπου δεσπόζει ο τεράστιος ουρανοξύστης Citadel του Dr. Wallace Breen.",
        "funFacts": [
            "Ο καλλιτεχνικός διευθυντής Viktor Antonov σχεδίασε την City 17 αντλώντας έμπνευση από την αρχιτεκτονική της γενέτειράς του, Σόφιας στη Βουλγαρία.",
            "Η σκηνή όπου ένας φρουρός Combine διατάζει τον Gordon Freeman 'Pick up that can' έγινε κλασικό gaming σημείο αναφοράς."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2",
        "tags": ["gaming", "half_life", "valve", "city_17", "fps"]
    },
    {
        "id": "gaming_easy_378",
        "text": "Ποιος είναι ο συνιδρυτής και διευθύνων σύμβουλος (CEO) της εταιρείας Valve, γνωστός στους gamers με το παρατσούκλι 'Gaben';",
        "correct": "Gabe Newell",
        "distractors": ["Tim Sweeney", "Todd Howard", "John Carmack"],
        "explanation": "Ο Gabe Newell εγκατέλειψε τη Microsoft το 1996 για να ιδρύσει τη Valve Corporation μαζί με τον Mike Harrington, δημιουργώντας το Half-Life και το Steam.",
        "funFacts": [
            "Ο Newell έγινε αντικείμενο λατρείας και memes στην κοινότητα των PC gamers, ιδιαίτερα κατά τις περιόδους των μεγάλων εκπτώσεων Steam Sales.",
            "Ένα από τα διαρκή αστεία στο ίντερνετ είναι ότι η Valve και ο Gabe Newell δεν μπορούν να μετρήσουν μέχρι το 3 (Half-Life 3, Portal 3, Left 4 Dead 3)."
        ],
        "source": "https://en.wikipedia.org/wiki/Gabe_Newell",
        "tags": ["gaming", "valve", "steam", "gabe_newell", "industry"]
    },
    {
        "id": "gaming_easy_379",
        "text": "Ποια φορητή συσκευή gaming (handheld PC) κυκλοφόρησε η Valve το 2022, επιτρέποντας στους παίκτες να παίζουν τα παιχνίδια του Steam οπουδήποτε;",
        "correct": "Steam Deck",
        "distractors": ["Steam Link", "Steam Machine", "Steam Controller"],
        "explanation": "Το Steam Deck τρέχει το λειτουργικό σύστημα SteamOS (βασισμένο σε Linux) και χρησιμοποιεί το επίπεδο συμβατότητας Proton για να τρέχει παιχνίδια Windows χωρίς πρόβλημα.",
        "funFacts": [
            "Διαθέτει δύο επιφάνειες αφής (trackpads) κάτω από τους μοχλούς για να υποστηρίζει παιχνίδια στρατηγικής που απαιτούν ποντίκι.",
            "Το 2023 η Valve κυκλοφόρησε μια αναβαθμισμένη έκδοση με οθόνη OLED και μεγαλύτερη διάρκεια μπαταρίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Steam_Deck",
        "tags": ["gaming", "valve", "steam_deck", "hardware", "handheld"]
    },
    {
        "id": "gaming_easy_380",
        "text": "Στο παιχνίδι 'Left 4 Dead', ποιο ειδικό μολυσμένο ζόμπι ξερνάει πράσινη χολή πάνω στους επιζώντες, τυφλώνοντάς τους και προσελκύοντας ορδές ζόμπι;",
        "correct": "Boomer",
        "distractors": ["Hunter", "Smoker", "Tank"],
        "explanation": "Ο Boomer είναι ένα παχύσαρκο ζόμπι γεμάτο αέρια και εκρηκτική χολή· αν πυροβοληθεί από κοντά, εκρήγνυται πασαλείβοντας τους πάντες γύρω του.",
        "funFacts": [
            "Η χολή του Boomer περιέχει ισχυρές φερομόνες που εξαγριώνουν τα απλά ζόμπι και τα κάνουν να επιτίθενται τυφλά σε όποιον έχει λερωθεί.",
            "Οι παίκτες μπορούν να σπρώξουν τον Boomer με το όπλο τους πριν τον πυροβολήσουν για να αποφύγουν την έκρηξη εξ επαφής."
        ],
        "source": "https://en.wikipedia.org/wiki/Left_4_Dead",
        "tags": ["gaming", "left_4_dead", "valve", "zombies", "fps"]
    },
    {
        "id": "gaming_easy_381",
        "text": "Στο 'Left 4 Dead', ποιο επικίνδυνο θηλυκό ζόμπι κλαίει καθισμένο στο σκοτάδι και επιτίθεται φονικά μόνο αν κάποιος την πλησιάσει ή τη φωτίσει;",
        "correct": "The Witch (Η Μάγισσα)",
        "distractors": ["Spitter", "Charger", "Jockey"],
        "explanation": "Η Witch είναι εξαιρετικά ευαίσθητη στο φως των φακών και στους θορύβους· αν εξαγριωθεί ('Startled'), ορμάει με τεράστια ταχύτητα και ρίχνει τον παίκτη αναίσθητο με ένα μόνο χτύπημα.",
        "funFacts": [
            "Οι έμπειροι παίκτες μπορούν να την εξοντώσουν ακαριαία με μια καλά τοποθετημένη βολή καραμπίνας στο κεφάλι από απόσταση αναπνοής (τεχνική 'Crowning').",
            "Η ανατριχιαστική μουσική που ακούγεται όταν πλησιάζεις μια Witch αλλάζει τόνο ανάλογα με το πόσο εκνευρισμένη είναι."
        ],
        "source": "https://en.wikipedia.org/wiki/Left_4_Dead",
        "tags": ["gaming", "left_4_dead", "valve", "monsters"]
    },
    {
        "id": "gaming_easy_382",
        "text": "Ποιο είναι το όνομα του γιγάντιου βιολογικού υπερόπλου με τη μακριά καπαρντίνα και τον εκτοξευτή πυραύλων που κυνηγάει τη Jill Valentine στο 'Resident Evil 3';",
        "correct": "Nemesis",
        "distractors": ["Mr. X (Tyrant)", "William Birkin", "Albert Wesker"],
        "explanation": "Ο Nemesis-T Type προγραμματίστηκε από την Umbrella Corporation με μοναδική αποστολή να εξολοθρεύσει όλα τα εναπομείναντα μέλη της ομάδας S.T.A.R.S.",
        "funFacts": [
            "Κάθε φορά που εντοπίζει τη Jill Valentine, βγάζει έναν χαρακτηριστικό ανατριχιαστικό βρυχηθμό προφέροντας τη λέξη 'S.T.A.R.S....'.",
            "Σε αντίθεση με τους προηγούμενους Tyrants, ο Nemesis διατηρεί αρκετή νοημοσύνη ώστε να χειρίζεται βαριά πυροβόλα όπλα και ρουκετοβόλα."
        ],
        "source": "https://en.wikipedia.org/wiki/Nemesis_(Resident_Evil)",
        "tags": ["gaming", "resident_evil", "capcom", "nemesis", "survival_horror"]
    },
    {
        "id": "gaming_easy_383",
        "text": "Ποιο καιρικό φαινόμενο καλύπτει μόνιμα τους δρόμους της στοιχειωμένης πόλης 'Silent Hill', κρύβοντας απόκοσμα τέρατα;",
        "correct": "Πυκνή ομίχλη (Thick Fog)",
        "distractors": ["Σφοδρή καταιγίδα", "Χιονοθύελλα", "Αμμοθύελλα"],
        "explanation": "Η χαρακτηριστική πυκνή ομίχλη του Silent Hill δημιουργήθηκε αρχικά από την Team Silent στο πρώτο PlayStation για να καλύψει τους περιορισμούς απόστασης σχεδιασμού (draw distance).",
        "funFacts": [
            "Η ομίχλη έγινε τόσο αναπόσπαστο στοιχείο της ψυχολογικής ατμόσφαιρας τρόμου που διατηρήθηκε σε όλα τα μετέπειτα παιχνίδια της σειράς.",
            "Όταν χτυπάει η σειρήνα της πόλης, ο κόσμος μεταμορφώνεται στον εφιαλτικό 'Otherworld' με σκουριασμένα σίδερα και αίμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill",
        "tags": ["gaming", "silent_hill", "konami", "survival_horror"]
    },
    {
        "id": "gaming_easy_384",
        "text": "Ποιο είναι το πιο εμβληματικό τέρας της σειράς 'Silent Hill' που κουβαλάει ένα τεράστιο μαχαίρι και έχει ένα μεταλλικό γεωμετρικό κράνος;",
        "correct": "Pyramid Head (Τριγωνοκέφαλος)",
        "distractors": ["Nemesis", "Slender Man", "Licker"],
        "explanation": "Ο Pyramid Head πρωτοεμφανίστηκε στο 'Silent Hill 2' (2001) ως εκδήλωση της ενοχής και της επιθυμίας του James Sunderland να τιμωρηθεί για τις πράξεις του.",
        "funFacts": [
            "Ο σχεδιαστής Masahiro Ito δημιούργησε τον Pyramid Head θέλοντας ένα τέρας με κρυμμένο πρόσωπο που να εμπνέει απόλυτο πόνο και μηχανική βία.",
            "Το γιγάντιο όπλο που σέρνει στο πάτωμα κάνοντας έναν ανατριχιαστικό μεταλλικό ήχο ονομάζεται Great Knife."
        ],
        "source": "https://en.wikipedia.org/wiki/Pyramid_Head",
        "tags": ["gaming", "silent_hill", "konami", "monsters", "pyramid_head"]
    },
    {
        "id": "gaming_easy_385",
        "text": "Ποιο είναι το όνομα της έξυπνης μικρότερης αδελφής του Crash Bandicoot που κρατάει πάντα ένα ροζ λάπτοπ και οδηγεί θαλάσσιο τζετ-σκι;",
        "correct": "Coco Bandicoot",
        "distractors": ["Tawna Bandicoot", "Nina Cortex", "Pasadena O'Possum"],
        "explanation": "Η Coco Bandicoot πρωτοεμφανίστηκε στο 'Crash Bandicoot 2: Cortex Strikes Back' (1997) και αποτελεί τον εγκέφαλο της οικογένειας Bandicoot.",
        "funFacts": [
            "Η Coco αντικατέστησε την Tawna (την κοπέλα του Crash από το πρώτο παιχνίδι) επειδή η Sony θεωρούσε τον αρχικό σχεδιασμό της Tawna υπερβολικά προκλητικό για παιδιά.",
            "Στο Crash Bandicoot 4: It's About Time, η Coco είναι πλήρως διαθέσιμη ως εναλλακτικός χαρακτήρας σε κάθε πίστα."
        ],
        "source": "https://en.wikipedia.org/wiki/Crash_Bandicoot",
        "tags": ["gaming", "crash_bandicoot", "playstation", "coco", "characters"]
    },
    {
        "id": "gaming_easy_386",
        "text": "Ποιο είναι το όνομα της χρυσής λιβελούλας που συνοδεύει τον Spyro the Dragon και αλλάζει χρώμα δείχνοντας τα επίπεδα της υγείας του;",
        "correct": "Sparx",
        "distractors": ["Navi", "Tatl", "Aku Aku"],
        "explanation": "Ο Sparx προστατεύει τον Spyro: είναι κίτρινος με πλήρη υγεία, γίνεται μπλε με το πρώτο χτύπημα, πράσινος με το δεύτερο και εξαφανίζεται αν δεχτεί τρίτο χτύπημα.",
        "funFacts": [
            "Ο Sparx ανακτά την υγεία του όταν ο Spyro καίει μικρά ζωάκια (πεταλούδες, πρόβατα) στις πίστες.",
            "Ο Sparx βοηθάει επίσης μαζεύοντας αυτόματα τους πολύτιμους λίθους (gems) που βρίσκονται γύρω από τον Spyro."
        ],
        "source": "https://en.wikipedia.org/wiki/Spyro_the_Dragon",
        "tags": ["gaming", "spyro", "insomniac", "playstation", "characters"]
    },
    {
        "id": "gaming_easy_387",
        "text": "Ποιος Ιάπωνας θεός του κεραυνού προστατεύει το Earthrealm και καθοδηγεί τους ήρωες στη σειρά 'Mortal Kombat';",
        "correct": "Raiden",
        "distractors": ["Fujin", "Liu Kang", "Shang Tsung"],
        "explanation": "Ο Raiden είναι ο Αιώνιος Θεός του Κεραυνού, αναγνωρίσιμος από το κωνικό ψάθινο καπέλο του, τις λευκές ρόμπες και τις αστραπές που εκτοξεύει από τα χέρια του.",
        "funFacts": [
            "Η διάσημη επίθεση 'Torpedo' του Raiden, όπου πετάει οριζόντια στον αέρα σπρώχνοντας τον αντίπαλο, συνοδεύεται από ακατάληπτες πολεμικές κραυγές.",
            "Στην ταινία Mortal Kombat του 1995, τον Raiden υποδύθηκε ο διάσημος ηθοποιός Christopher Lambert."
        ],
        "source": "https://en.wikipedia.org/wiki/Raiden_(Mortal_Kombat)",
        "tags": ["gaming", "mortal_kombat", "raiden", "fighting"]
    },
    {
        "id": "gaming_easy_388",
        "text": "Ποια είναι η νεαρή ανθοπώλης των παραγκουπόλεων του Midgar και τελευταία απόγονος των αρχαίων Cetra στο 'Final Fantasy VII';",
        "correct": "Aerith Gainsborough",
        "distractors": ["Tifa Lockhart", "Yuffie Kisaragi", "Rinoa Heartilly"],
        "explanation": "Η Aerith (γνωστή αρχικά ως Aeris στη δυτική έκδοση) έχει τη δύναμη να επικοινωνεί με τον πλανήτη και κρατάει το White Materia που μπορεί να καλέσει το Holy.",
        "funFacts": [
            "Η μοίρα της Aerith στα χέρια του Sephiroth στο τέλος του πρώτου CD αποτελεί ίσως την πιο πολυσυζητημένη και συγκινητική σκηνή στην ιστορία των RPGs.",
            "Το μουσικό θέμα της ('Aerith's Theme') θεωρείται από τα κορυφαία αριστουργήματα του συνθέτη Nobuo Uematsu."
        ],
        "source": "https://en.wikipedia.org/wiki/Aerith_Gainsborough",
        "tags": ["gaming", "final_fantasy", "square_enix", "aerith", "characters"]
    },
    {
        "id": "gaming_easy_389",
        "text": "Ποιο είναι το όνομα του μπαρ που διαχειρίζεται η Tifa Lockhart στις φτωχογειτονιές του Sector 7 στο 'Final Fantasy VII';",
        "correct": "7th Heaven",
        "distractors": ["Moxxi's", "The Drunken Clam", "The Slaughtered Lamb"],
        "explanation": "Το μπαρ 7th Heaven λειτουργεί ως βιτρίνα αλλά και ως μυστικό αρχηγείο της αντιστασιακής οργάνωσης AVALANCHE του Barret Wallace.",
        "funFacts": [
            "Κάτω από το μπαρ υπάρχει ένας μυστικός ανελκυστήρας που οδηγεί στο υπόγειο δωμάτιο επιχειρήσεων.",
            "Η Tifa είναι ειδική στις πολεμικές τέχνες και πολεμάει αποκλειστικά με γροθιές και κλωτσιές χρησιμοποιώντας ειδικά γάντια."
        ],
        "source": "https://en.wikipedia.org/wiki/Tifa_Lockhart",
        "tags": ["gaming", "final_fantasy", "square_enix", "tifa"]
    },
    {
        "id": "gaming_easy_390",
        "text": "Ποιο ήταν το μέγιστο επίπεδο (level cap) που μπορούσε να φτάσει ένας χαρακτήρας στην αρχική έκδοση (Vanilla) του 'World of Warcraft' (2004);",
        "correct": "Επίπεδο 60 (Level 60)",
        "distractors": ["Επίπεδο 50", "Επίπεδο 70", "Επίπεδο 100"],
        "explanation": "Στο αρχικό World of Warcraft, το ταξίδι μέχρι το επίπεδο 60 απαιτούσε εβδομάδες ή μήνες παιχνιδιού, ανοίγοντας τον δρόμο για τα raids 40 παικτών όπως το Molten Core.",
        "funFacts": [
            "Το πρώτο expansion, The Burning Crusade (2007), αύξησε το ανώτατο όριο στο επίπεδο 70.",
            "Το raid Molten Core απαιτούσε 40 παίκτες άριστα συντονισμένους για να νικήσουν τον Ragnaros the Firelord."
        ],
        "source": "https://en.wikipedia.org/wiki/World_of_Warcraft",
        "tags": ["gaming", "world_of_warcraft", "blizzard", "mmorpg"]
    },
    {
        "id": "gaming_easy_391",
        "text": "Ποιος θρυλικός ηγέτης των Ορκ (Warchief) απελευθέρωσε τον λαό του και ίδρυσε το έθνος Durotar στο 'Warcraft III';",
        "correct": "Thrall (Go'el)",
        "distractors": ["Grom Hellscream", "Garrosh Hellscream", "Gul'dan"],
        "explanation": "Ο Thrall, μεγαλωμένος ως σκλάβος μονομάχος από ανθρώπους, έγινε Σαμάνος και οδήγησε τη Νέα Ορδή στην ήπειρο Kalimdor ιδρύοντας την πρωτεύουσα Orgrimmar.",
        "funFacts": [
            "Ο Thrall κρατούσε το θρυλικό πολεμικό σφυρί Doomhammer και φορούσε τη μαύρη πανοπλία του Orgrim Doomhammer.",
            "Τη φωνή του Thrall δάνεισε για πολλά χρόνια ο συνδημιουργός του σύμπαντος του Warcraft, Chris Metzen."
        ],
        "source": "https://en.wikipedia.org/wiki/Warcraft_III:_Reign_of_Chaos",
        "tags": ["gaming", "warcraft", "blizzard", "thrall", "lore"]
    },
    {
        "id": "gaming_easy_392",
        "text": "Ποια είναι η ανθρώπινη τηλεπαθητική πράκτορας 'Ghost' που προδόθηκε από τους συμμάχους της και μεταλλάχθηκε στη 'Βασίλισσα των Λεπίδων' (Queen of Blades) στο 'StarCraft';",
        "correct": "Sarah Kerrigan",
        "distractors": ["Nova Terra", "Selendis", "Mira Han"],
        "explanation": "Η Sarah Kerrigan εγκαταλείφθηκε από τον Arcturus Mengsk στον πλανήτη Tarsonis, αιχμαλωτίστηκε από τα Zerg και μεταμορφώθηκε στην πανίσχυρη ηγέτιδα του σμήνους.",
        "funFacts": [
            "Η Kerrigan θεωρείται ένας από τους πιο περίπλοκους και εμβληματικούς αντι-ήρωες στην ιστορία των στρατηγικών παιχνιδιών.",
            "Στο StarCraft II: Heart of the Swarm, οι παίκτες ελέγχουν άμεσα την Kerrigan σε αποστολές τύπου RPG ενδυναμώνοντας τις ικανότητές της."
        ],
        "source": "https://en.wikipedia.org/wiki/Sarah_Kerrigan",
        "tags": ["gaming", "starcraft", "blizzard", "kerrigan", "rts"]
    },
    {
        "id": "gaming_easy_393",
        "text": "Στο παιχνίδι 'Overwatch', ποιος είναι ο Ιάπωνας cyborg νίντζα που πετάει shurikens και ξεχύνεται με το σπαθί Dragonblade;",
        "correct": "Genji Shimada",
        "distractors": ["Hanzo Shimada", "Kiriko Kamori", "Zenyatta"],
        "explanation": "Ο Genji τραυματίστηκε θανάσιμα από τον αδελφό του Hanzo, αλλά διασώθηκε από την Overwatch και μετατράπηκε σε πανίσχυρο κυβερνοπολεμιστή.",
        "funFacts": [
            "Όταν ενεργοποιεί το Dragonblade, ο Genji φωνάζει στα ιαπωνικά: 'Ryūjin no ken wo kurae!' (Γεύσου το σπαθί του θεού δράκου!).",
            "Ο πνευματικός του μέντορας είναι ο πανσοφός Omnic μοναχός Zenyatta."
        ],
        "source": "https://en.wikipedia.org/wiki/Genji_(Overwatch)",
        "tags": ["gaming", "overwatch", "blizzard", "genji", "characters"]
    },
    {
        "id": "gaming_easy_394",
        "text": "Ποιος είναι ο αδελφός του Genji στο 'Overwatch', ένας αριστοτέχνης τοξότης που επικαλείται δύο γιγάντιους πνευματικούς δράκους με το τόξο του;",
        "correct": "Hanzo Shimada",
        "distractors": ["Genji Shimada", "Torbjörn", "Reaper"],
        "explanation": "Ο Hanzo εξορίστηκε από τη φατρία του λόγω της ενοχής του για τη φονική σύγκρουση με τον αδελφό του και ταξιδεύει στον κόσμο τελειοποιώντας την τοξοβολία του.",
        "funFacts": [
            "Η κραυγή της απόλυτης ικανότητάς του είναι: 'Ryū ga waga teki wo kurau!' (Δράκε, κατάπιε τους εχθρούς μου!).",
            "Τα βέλη του περιλαμβάνουν βέλη ανίχνευσης (Sonic Arrow) και βέλη ταχείας ριπής (Storm Arrows)."
        ],
        "source": "https://en.wikipedia.org/wiki/Characters_of_Overwatch#Hanzo",
        "tags": ["gaming", "overwatch", "blizzard", "hanzo", "characters"]
    },
    {
        "id": "gaming_easy_395",
        "text": "Τι σήμαινε αρχικά το ακρωνύμιο 'DS' στην εξαιρετικά επιτυχημένη φορητή κονσόλα Nintendo DS (2004);",
        "correct": "Dual Screen (Διπλή Οθόνη) ή Developers' System",
        "distractors": ["Digital System", "Direct Screen", "Dynamic Series"],
        "explanation": "Το Nintendo DS διέθετε δύο οθόνες (με την κάτω οθόνη να είναι οθόνη αφής με γραφίδα stylus) και έγινε η δεύτερη κονσόλα με τις περισσότερες πωλήσεις στην ιστορία.",
        "funFacts": [
            "Το Nintendo DS πούλησε πάνω από 154 εκατομμύρια μονάδες παγκοσμίως, μένοντας ελάχιστα πίσω από το PlayStation 2.",
            "Διέθετε ενσωματωμένο μικρόφωνο και ασύρματη σύνδεση Wi-Fi με τη δωρεάν εφαρμογή συνομιλίας PictoChat."
        ],
        "source": "https://en.wikipedia.org/wiki/Nintendo_DS",
        "tags": ["gaming", "nintendo", "nintendo_ds", "handheld", "consoles"]
    },
    {
        "id": "gaming_easy_396",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού χειριστηρίου κίνησης της κονσόλας Nintendo Wii που έμοιαζε με τηλεχειριστήριο τηλεόρασης;",
        "correct": "Wii Remote (ή Wiimote)",
        "distractors": ["Nunchuk", "Wii U GamePad", "Sixaxis"],
        "explanation": "Το Wii Remote περιλάμβανε επιταχυνσιόμετρα και οπτικό αισθητήρα υπερύθρων, επιτρέποντας στον παίκτη να κινεί το χέρι του για να χτυπά μπαλιές του τένις ή να ρίχνει βέλη.",
        "funFacts": [
            "Επειδή πολλοί παίκτες πέταγαν κατά λάθος το χειριστήριο πάνω στην τηλεόραση, η Nintendo πρόσθεσε ειδικά λουράκια καρπού και καλύμματα σιλικόνης.",
            "Το συνοδευτικό αναλογικό εξάρτημα με τον μοχλό που συνδεόταν με καλώδιο ονομαζόταν Nunchuk."
        ],
        "source": "https://en.wikipedia.org/wiki/Wii_Remote",
        "tags": ["gaming", "nintendo", "wii", "hardware", "controller"]
    },
    {
        "id": "gaming_easy_397",
        "text": "Στο δημοφιλές παιχνίδι 'Minecraft', ποιο είναι το σπάνιο μπλε ορυκτό βαθιά στη γη που χρησιμοποιείται για την κατασκευή πανίσχυρων εργαλείων και πανοπλιών;",
        "correct": "Διαμάντι (Diamond)",
        "distractors": ["Σμαράγδι (Emerald)", "Χρυσός (Gold)", "Κόκκινη πέτρα (Redstone)"],
        "explanation": "Τα διαμάντια εξορύσσονται στα βαθύτερα επίπεδα του κόσμου του Minecraft και αποτελούσαν παραδοσιακά το ισχυρότερο υλικό εξοπλισμού πριν την προσθήκη του Netherite.",
        "funFacts": [
            "Χρειάζεται αξίνα από σίδηρο (iron pickaxe) ή καλύτερη για να εξορυχθεί ένα διαμάντι χωρίς να καταστραφεί.",
            "Τα σμαράγδια (emeralds) στο Minecraft χρησιμοποιούνται κυρίως ως νόμισμα για συναλλαγές με τους χωρικούς (villagers)."
        ],
        "source": "https://en.wikipedia.org/wiki/Minecraft",
        "tags": ["gaming", "minecraft", "mojang", "items"]
    },
    {
        "id": "gaming_easy_398",
        "text": "Ποιο είναι το όνομα του τελικού αφεντικού δράκου που ζει στη διάσταση 'The End' στο 'Minecraft';",
        "correct": "Ender Dragon",
        "distractors": ["Wither", "Elder Guardian", "Warden"],
        "explanation": "Ο Ender Dragon είναι ο βασικός τελικός στόχος του Minecraft· νικώντας τον, εμφανίζονται οι τίτλοι τέλους του παιχνιδιού και ανοίγει η πύλη για τα End Cities.",
        "funFacts": [
            "Ο Ender Dragon θεραπεύεται συνεχώς από τους κρυστάλλους End Crystals που βρίσκονται στην κορυφή ψηλών πυλώνων οψιδιανού.",
            "Όταν ο παίκτης νικήσει τον δράκο, αποκτά το αυγό του (Dragon Egg) και 68 επίπεδα εμπειρίας (XP)."
        ],
        "source": "https://en.wikipedia.org/wiki/Minecraft",
        "tags": ["gaming", "minecraft", "mojang", "bosses"]
    },
    {
        "id": "gaming_easy_399",
        "text": "Ποιος είναι ο παχύσαρκος κροκόδειλος-βασιλιάς των Kremlings και κύριος κακός στη σειρά 'Donkey Kong Country';",
        "correct": "King K. Rool",
        "distractors": ["Bowser", "King Boo", "Tiki Tong"],
        "explanation": "Ο King K. Rool είναι ο αρχηγός των Kremlings που φοράει χρυσό στέμμα και κόκκινη κάπα, κλέβοντας διαρκώς τις μπανάνες του Donkey Kong.",
        "funFacts": [
            "Στο Donkey Kong Country 2 εμφανίζεται μεταμφιεσμένος σε πειρατή ως Kaptain K. Rool.",
            "Το 'K. Rool' είναι λογοπαίγνιο με την αγγλική λέξη 'cruel' (σκληρός/βάναυσος)."
        ],
        "source": "https://en.wikipedia.org/wiki/King_K._Rool",
        "tags": ["gaming", "donkey_kong", "rare", "nintendo", "villains"]
    },
    {
        "id": "gaming_easy_400",
        "text": "Ποιο μαρσιποφόρο ζώο που φοράει γάντια του μποξ εμφανίζεται ως μαχητής στη σειρά 'Tekken';",
        "correct": "Καγκουρό (Roger)",
        "distractors": ["Αρκούδα", "Πάντα", "Τίγρης"],
        "explanation": "Ο Roger είναι ένα γενετικά τροποποιημένο καγκουρό με γάντια πυγμαχίας που πρωτοεμφανίστηκε στο Tekken 2.",
        "funFacts": [
            "Στο Tekken 5 εμφανίζεται η σύζυγός του Roger Jr., η οποία πολεμά με το μικρό της καγκουρό μέσα στον μάρσιπό της.",
            "Η σειρά Tekken περιλαμβάνει επίσης άλλους ασυνήθιστους μαχητές ζώων, όπως τις αρκούδες Kuma και Panda."
        ],
        "source": "https://en.wikipedia.org/wiki/List_of_Tekken_characters#Roger",
        "tags": ["gaming", "tekken", "bandai_namco", "fighting"]
    },
    {
        "id": "gaming_easy_401",
        "text": "Ποιος είναι ο πιο διάσημος κωδικός (cheat code) στη σειρά 'The Sims' που προσθέτει αυτόματα 50.000 Simoleons στο ταμείο της οικογένειας;",
        "correct": "motherlode",
        "distractors": ["rosebud", "kaching", "showmethemoney"],
        "explanation": "Ο κωδικός 'motherlode' έγινε θρύλος στο The Sims 2, 3 και 4, επιτρέποντας στους παίκτες να χτίζουν αμέσως πολυτελείς επαύλεις.",
        "funFacts": [
            "Στο αρχικό The Sims (2000), ο πιο γνωστός κωδικός για χρήματα ήταν το 'rosebud' που έδινε 1.000 Simoleons.",
            "Το εικονικό νόμισμα του The Sims ονομάζεται Simoleon και συμβολίζεται με το σύμβολο §."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Sims",
        "tags": ["gaming", "the_sims", "ea", "maxis", "cheats"]
    },
    {
        "id": "gaming_easy_402",
        "text": "Ποια καλοσυνάτη νεράιδα χαρίζει στον Rayman νέες ικανότητες (όπως γροθιά και αιώρηση) στο αρχικό παιχνίδι 'Rayman' (1995);",
        "correct": "Betilla the Fairy",
        "distractors": ["Ly the Fairy", "Navi", "Tinkerbell"],
        "explanation": "Η Betilla εμφανίζεται μετά από ορισμένες πίστες και δίνει στον Rayman δυνάμεις όπως την τηλεσκοπική γροθιά και την ικανότητα να πετάει με τα μαλλιά του.",
        "funFacts": [
            "Στο Rayman Origins (2011), η Betilla και οι αδελφές της σχεδιάστηκαν ξανά με μοντέρνο καρτουνίστικο στυλ.",
            "Στο Rayman 2: The Great Escape, τον ρόλο της νεράιδας-συμμάχου αναλαμβάνει η Ly the Fairy."
        ],
        "source": "https://en.wikipedia.org/wiki/Rayman_(video_game)",
        "tags": ["gaming", "rayman", "ubisoft", "characters"]
    },
    {
        "id": "gaming_easy_403",
        "text": "Ποιο είναι το βασικό εργαλείο που χρειάζεται ο παίκτης στο 'Minecraft' για να εξορύξει πέτρα, κάρβουνο και μεταλλεύματα;",
        "correct": "Αξίνα (Pickaxe)",
        "distractors": ["Τσεκούρι", "Φτυάρι", "Τσάπα"],
        "explanation": "Η αξίνα (pickaxe) είναι το πιο απαραίτητο εργαλείο στο Minecraft, φτιαγμένη αρχικά από ξύλο και αναβαθμιζόμενη σε πέτρα, σίδηρο, διαμάντι και νεθερίτη.",
        "funFacts": [
            "Αν σπάσεις πέτρα με γυμνά χέρια ή με λάθος εργαλείο, το μπλοκ σπάει πολύ αργά και δεν αφήνει πίσω του κανένα υλικό.",
            "Η αξίνα αποτελεί το κεντρικό σύμβολο του λογότυπου και της ταυτότητας του Minecraft."
        ],
        "source": "https://en.wikipedia.org/wiki/Minecraft",
        "tags": ["gaming", "minecraft", "mojang", "items"]
    },
    {
        "id": "gaming_easy_404",
        "text": "Σε ποιον τίτλο της σειράς 'Call of Duty' πρωτοεμφανίστηκε το εξαιρετικά δημοφιλές survival mode ενάντια σε ζόμπι ('Nazi Zombies');",
        "correct": "Call of Duty: World at War (2008)",
        "distractors": ["Call of Duty 4: Modern Warfare", "Call of Duty: Black Ops", "Call of Duty 2"],
        "explanation": "Το Zombies mode αναπτύχθηκε μυστικά από την Treyarch ως easter egg μετά τους τίτλους τέλους του World at War με τον χάρτη 'Nacht der Untoten'.",
        "funFacts": [
            "Η επιτυχία του mode ήταν τόσο απροσδόκητη ώστε εξελίχθηκε σε βασικό πυλώνα των παιχνιδιών Black Ops με πλούσιο lore και χαρακτήρες.",
            "Το τραγούδι του μυστηριώδους κουτιού (Mystery Box) έγινε ένα από τα πιο αναγνωρίσιμα ηχητικά jingles της σειράς."
        ],
        "source": "https://en.wikipedia.org/wiki/Call_of_Duty:_World_at_War",
        "tags": ["gaming", "call_of_duty", "activision", "treyarch", "zombies"]
    },
    {
        "id": "gaming_easy_405",
        "text": "Ποιο σύμβολο μετράει το επίπεδο καταδίωξης από την αστυνομία (Wanted Level) στη σειρά παιχνιδιών 'Grand Theft Auto';",
        "correct": "Αστέρια (Stars)",
        "distractors": ["Χειροπέδες", "Σειρήνες", "Κρανία"],
        "explanation": "Στο GTA, το Wanted Level μετριέται με αστέρια (από 1 έως 5 ή 6). Όσο περισσότερα αστέρια αποκτά ο παίκτης, τόσο πιο επιθετικές μονάδες στέλνονται (SWAT, FBI, στρατός με τανκς).",
        "funFacts": [
            "Στο GTA San Andreas και στο GTA IV υπήρχαν έως 6 αστέρια καταδίωξης, ενώ στο GTA V το ανώτατο όριο μειώθηκε σε 5 αστέρια.",
            "Ο παίκτης μπορεί να σβήσει τα αστέρια βάφοντας το αυτοκίνητό του σε ένα συνεργείο Pay 'n' Spray."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto",
        "tags": ["gaming", "gta", "rockstar", "mechanics"]
    },
    {
        "id": "gaming_easy_406",
        "text": "Ποια εξελικτική πέτρα (Evolution Stone) χρειάζεται να χρησιμοποιήσει ένας εκπαιδευτής για να εξελίξει τον Pikachu σε Raichu στο 'Pokémon';",
        "correct": "Thunder Stone (Πέτρα Κεραυνού)",
        "distractors": ["Fire Stone", "Water Stone", "Moon Stone"],
        "explanation": "Ο Pikachu δεν εξελίσσεται σε Raichu απλώς ανεβαίνοντας επίπεδα, αλλά απαιτεί την άμεση έκθεση σε μια Thunder Stone.",
        "funFacts": [
            "Στο anime, ο Pikachu του Ash αρνείται πεισματικά να αγγίξει την Thunder Stone επειδή θέλει να νικήσει δυνατούς αντιπάλους με τις δικές του δυνάμεις.",
            "Στη 2η γενιά (Gold & Silver) αποκαλύφθηκε η προηγούμενη μωρουδιακή μορφή του Pikachu, το Pichu."
        ],
        "source": "https://en.wikipedia.org/wiki/Pikachu",
        "tags": ["gaming", "pokemon", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_407",
        "text": "Πώς ονομάζεται η ειδική προστατευτική στολή επικίνδυνων περιβαλλόντων που φοράει ο Gordon Freeman στη σειρά 'Half-Life';",
        "correct": "HEV Suit (Hazardous EnVironment Suit)",
        "distractors": ["Power Suit", "Nanosuit", "Praetor Suit"],
        "explanation": "Η στολή HEV Suit (μοντέλο Mark IV στο Half-Life 1, Mark V στο Half-Life 2) διαθέτει ενσωματωμένο μετρητή Geiger, φακό και σύστημα αυτόματης χορήγησης μορφίνης.",
        "funFacts": [
            "Η ρομποτική φωνή της στολής ενημερώνει τον Gordon για ζωτικές μετρήσεις με φράσεις όπως 'Major fracture detected' ή 'Morphine administered'.",
            "Η στολή φορτίζεται στους ειδικούς σταθμούς τοίχου της Black Mesa και του Combine."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_(video_game)",
        "tags": ["gaming", "half_life", "valve", "gordon_freeman"]
    },
    {
        "id": "gaming_easy_408",
        "text": "Ποιο είναι το διαβόητο επίπεδο στο αρχικό arcade 'Pac-Man' όπου η δεξιά πλευρά της οθόνης διαλύεται σε ακατανόητα σύμβολα (Split-Screen Glitch);",
        "correct": "Επίπεδο 256",
        "distractors": ["Επίπεδο 100", "Επίπεδο 99", "Επίπεδο 500"],
        "explanation": "Λόγω υπερχείλισης ακεραίου 8-bit (integer overflow), ο υπολογιστής προσπαθεί να σχεδιάσει 256 φρούτα στο κάτω μέρος, γεμίζοντας τη μισή οθόνη με σκουπίδια μνήμης και καθιστώντας αδύνατη τη συνέχεια.",
        "funFacts": [
            "Το τέλειο σκορ στο Pac-Man (Perfect Game) είναι ακριβώς 3.333.360 πόντοι, τρώγοντας κάθε τελεία, φρούτο και φάντασμα μέχρι την οθόνη θανάτου.",
            "Ο πρώτος άνθρωπος που πέτυχε επίσημα το τέλειο σκορ ήταν ο Billy Mitchell το 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Pac-Man",
        "tags": ["gaming", "pac_man", "arcade", "glitch", "retro"]
    },
    {
        "id": "gaming_easy_409",
        "text": "Ποιος είναι ο Αμερικανός μαχητής με την κόκκινη στολή καράτε και τα ξανθά μαλλιά, αδελφικός φίλος και αντίζηλος του Ryu στο 'Street Fighter';",
        "correct": "Ken Masters",
        "distractors": ["Guile", "Dan Hibiki", "Luke Sullivan"],
        "explanation": "Ο Ken Masters προπονήθηκε μαζί με τον Ryu υπό τον δάσκαλο Gouken, αναπτύσσοντας παρόμοιες κινήσεις αλλά με έμφαση στις φλεγόμενες γροθιές Shoryuken.",
        "funFacts": [
            "Στο αρχικό Street Fighter (1987), ο Ken ήταν απλώς ο χαρακτήρας του δεύτερου παίκτη (Player 2) με πανομοιότυπα στατιστικά με τον Ryu.",
            "Ο Ken προέρχεται από εξαιρετικά πλούσια οικογένεια ξενοδόχων των ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/Ken_Masters",
        "tags": ["gaming", "street_fighter", "capcom", "ken", "fighting"]
    },
    {
        "id": "gaming_easy_410",
        "text": "Στο κλασικό παιχνίδι 'Super Mario Bros.', ποιο power-up επιτρέπει στον Mario να πετάει μπάλες φωτιάς στους εχθρούς;",
        "correct": "Fire Flower (Λουλούδι της Φωτιάς)",
        "distractors": ["Super Leaf", "Ice Flower", "Fire Mushroom"],
        "explanation": "Το Fire Flower μετατρέπει τον Mario σε Fire Mario, αλλάζοντας τη στολή του σε λευκή με κόκκινες τιράντες και δίνοντάς του την ικανότητα να εκτοξεύει αναπηδούσες πύρινες σφαίρες.",
        "funFacts": [
            "Οι μπάλες φωτιάς μπορούν να νικήσουν σχεδόν όλους τους εχθρούς, συμπεριλαμβανομένου και του ίδιου του Bowser.",
            "Το Fire Flower ήταν το πρώτο αντικείμενο στην ιστορία της σειράς Mario που άλλαζε τα ρούχα και την εμφάνιση του ήρωα."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Bros.",
        "tags": ["gaming", "mario", "nintendo", "items"]
    }
]

questions = []
for q in raw_questions:
    opts = [q["correct"]] + q["distractors"]
    random.shuffle(opts)
    c_idx = opts.index(q["correct"])
    questions.append({
        "id": q["id"],
        "categoryId": "gaming",
        "difficulty": 1,
        "locale": "el-GR",
        "text": q["text"],
        "answers": opts,
        "correctAnswerIndex": c_idx,
        "explanation": q["explanation"],
        "funFacts": q["funFacts"],
        "source": q["source"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": q["tags"]
    })

if __name__ == "__main__":
    print(f"Loaded {len(questions)} questions for gaming_easy batch 4.")
    validate_and_append("gaming", "easy", 1, questions)

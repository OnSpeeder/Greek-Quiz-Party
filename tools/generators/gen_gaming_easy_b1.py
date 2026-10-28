# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_easy_211",
        "text": "Ποιο είναι το όνομα του πιστού πράσινου δεινόσαυρου και συντρόφου του Super Mario που πρωτοεμφανίστηκε στο 'Super Mario World' (1990);",
        "correct": "Yoshi",
        "distractors": ["Bowser", "Toad", "Koopa"],
        "explanation": "Ο Yoshi έκανε το ντεμπούτο του στο Super Mario World για το SNES το 1990 και μπορεί να τρώει εχθρούς με τη μακριά του γλώσσα.",
        "funFacts": [
            "Ο δημιουργός του Mario, Shigeru Miyamoto, ήθελε έναν δεινόσαυρο ήδη από το πρώτο Super Mario Bros., αλλά το NES δεν είχε αρκετή επεξεργαστική ισχύ.",
            "Το πλήρες επιστημονικό/φανταστικό όνομα του χαρακτήρα είναι T. Yoshisaur Munchakoopas."
        ],
        "source": "https://en.wikipedia.org/wiki/Yoshi",
        "tags": ["gaming", "nintendo", "mario", "yoshi", "characters"]
    },
    {
        "id": "gaming_easy_212",
        "text": "Ποιο είναι το όνομα της διάσημης αρχαιολόγου και πρωταγωνίστριας της σειράς βιντεοπαιχνιδιών 'Tomb Raider';",
        "correct": "Lara Croft",
        "distractors": ["Jill Valentine", "Claire Redfield", "Samus Aran"],
        "explanation": "Η Lara Croft δημιουργήθηκε από τη βρετανική εταιρεία Core Design το 1996 και αποτελεί μία από τις πιο εμβληματικές ηρωίδες στην ιστορία των βιντεοπαιχνιδιών.",
        "funFacts": [
            "Το αρχικό όνομα που είχε προταθεί για την ηρωίδα ήταν Laura Cruz.",
            "Η Lara Croft κατέχει ρεκόρ Guinness ως η πιο επιτυχημένη ανθρώπινη γυναικεία φιγούρα σε βιντεοπαιχνίδι."
        ],
        "source": "https://en.wikipedia.org/wiki/Lara_Croft",
        "tags": ["gaming", "tomb_raider", "lara_croft", "characters"]
    },
    {
        "id": "gaming_easy_213",
        "text": "Ποιο είναι το χρώμα του χαρακτήρα Pac-Man στο κλασικό arcade παιχνίδι της Namco;",
        "correct": "Κίτρινο",
        "distractors": ["Κόκκινο", "Μπλε", "Πράσινο"],
        "explanation": "Ο Pac-Man είναι ένας κίτρινος κυκλικός χαρακτήρας που τρώει τελείες (pellets) μέσα σε έναν λαβύρινθο αποφεύγοντας φαντάσματα.",
        "funFacts": [
            "Ο σχεδιαστής Toru Iwatani εμπνεύστηκε το σχήμα του Pac-Man κοιτάζοντας μια πίτσα από την οποία έλειπε ένα κομμάτι.",
            "Το αρχικό ιαπωνικό όνομα ήταν Puck Man, αλλά άλλαξε για να αποφευχθούν βανδαλισμοί στις καμπίνες arcade."
        ],
        "source": "https://en.wikipedia.org/wiki/Pac-Man",
        "tags": ["gaming", "arcade", "pac_man", "namco", "retro"]
    },
    {
        "id": "gaming_easy_214",
        "text": "Ποια εταιρεία δημιούργησε και κυκλοφόρησε την κονσόλα PlayStation το 1994 στην Ιαπωνία;",
        "correct": "Sony",
        "distractors": ["Microsoft", "Sega", "Nintendo"],
        "explanation": "Η Sony κυκλοφόρησε το πρώτο PlayStation στην Ιαπωνία τον Δεκέμβριο του 1994, κάνοντας επανάσταση στα τρισδιάστατα γραφικά και τα CD-ROM.",
        "funFacts": [
            "Το PlayStation ξεκίνησε αρχικά ως κοινό εγχείρημα συνεργασίας μεταξύ Sony και Nintendo για την προσθήκη CD-ROM στο SNES.",
            "Έγινε η πρώτη οικιακή κονσόλα στην ιστορία που ξεπέρασε τις 100 εκατομμύρια πωλήσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/PlayStation_(console)",
        "tags": ["gaming", "playstation", "sony", "consoles"]
    },
    {
        "id": "gaming_easy_215",
        "text": "Στο παιχνίδι 'Minecraft', ποιο πράσινο πλάσμα πλησιάζει σιωπηλά τον παίκτη και εκρήγνυται κάνοντας χαρακτηριστικό ήχο σφυρίγματος;",
        "correct": "Creeper",
        "distractors": ["Zombie", "Enderman", "Skeleton"],
        "explanation": "Το Creeper είναι ένα από τα πιο διάσημα εχθρικά mobs του Minecraft που εκρήγνυται όταν πλησιάσει αρκετά τον παίκτη.",
        "funFacts": [
            "Το Creeper δημιουργήθηκε από ένα τυχαίο σφάλμα κώδικα του Notch όταν προσπαθούσε να μοντελοποιήσει ένα γουρούνι και έβαλε ανάποδα το ύψος με το μήκος.",
            "Τα Creepers φοβούνται τις γάτες και τους οσελότους και τρέχουν μακριά τους."
        ],
        "source": "https://en.wikipedia.org/wiki/Creeper_(Minecraft)",
        "tags": ["gaming", "minecraft", "mojang", "creeper"]
    },
    {
        "id": "gaming_easy_216",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή της σειράς 'The Legend of Zelda' που φοράει παραδοσιακά πράσινο χιτώνα;",
        "correct": "Link",
        "distractors": ["Zelda", "Ganon", "Navi"],
        "explanation": "Ο Link είναι ο βασικός ήρωας της σειράς The Legend of Zelda, ενώ η Zelda είναι η πριγκίπισσα του βασιλείου της Hyrule.",
        "funFacts": [
            "Ονομάστηκε 'Link' επειδή ο Miyamoto ήθελε να λειτουργεί ως συνδετικός κρίκος (link) ανάμεσα στον παίκτη και τον κόσμο του παιχνιδιού.",
            "Ο Link σχεδιάστηκε παραδοσιακά ως αριστερόχειρας μέχρι την εποχή του Nintendo Wii."
        ],
        "source": "https://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)",
        "tags": ["gaming", "zelda", "nintendo", "link", "characters"]
    },
    {
        "id": "gaming_easy_217",
        "text": "Ποιο franchise παιχνιδιών ποδοσφαίρου της EA Sports μετονομάστηκε σε 'EA Sports FC' το 2023;",
        "correct": "FIFA",
        "distractors": ["PES", "Football Manager", "Virtua Striker"],
        "explanation": "Η σειρά παιχνιδιών FIFA της EA Sports μετονομάστηκε σε EA Sports FC μετά τη λήξη της συνεργασίας αδειοδότησης με τη διεθνή ομοσπονδία FIFA το 2023.",
        "funFacts": [
            "Το πρώτο παιχνίδι της σειράς κυκλοφόρησε το 1993 με τίτλο 'FIFA International Soccer'.",
            "Η σειρά FIFA συγκαταλέγεται στα franchise αθλητικών παιχνιδιών με τις μεγαλύτερες πωλήσεις όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/EA_Sports_FC",
        "tags": ["gaming", "ea_sports", "fifa", "sports", "football"]
    },
    {
        "id": "gaming_easy_218",
        "text": "Ποιος είναι ο εμβληματικός στρατιώτης Spartan με την πράσινη πανοπλία και το κράνος που πρωταγωνιστεί στη σειρά 'Halo';",
        "correct": "Master Chief (John-117)",
        "distractors": ["Marcus Fenix", "Doom Slayer", "Gordon Freeman"],
        "explanation": "Ο Master Chief Petty Officer John-117 είναι ο κεντρικός πρωταγωνιστής της σειράς Halo, της ναυαρχίδας της Microsoft για το Xbox.",
        "funFacts": [
            "Τη φωνή του Master Chief δανείζει σταθερά ο Αμερικανός ηθοποιός Steve Downes.",
            "Η πιστή τεχνητή νοημοσύνη που τον συνοδεύει στις αποστολές του ονομάζεται Cortana."
        ],
        "source": "https://en.wikipedia.org/wiki/Master_Chief_(Halo)",
        "tags": ["gaming", "halo", "xbox", "master_chief", "fps"]
    },
    {
        "id": "gaming_easy_219",
        "text": "Στο παιχνίδι 'Sonic the Hedgehog', τι συλλέγει ο Sonic στις πίστες για να προστατεύεται από τους εχθρούς και να μην χάνει ζωή;",
        "correct": "Χρυσά δαχτυλίδια (Golden Rings)",
        "distractors": ["Χρυσά νομίσματα", "Μανιτάρια", "Κόκκινα μήλα"],
        "explanation": "Ο Sonic μαζεύει χρυσά δαχτυλίδια (rings)· αν δεχτεί χτύπημα χάνει τα δαχτυλίδια του, αλλά αν χτυπηθεί χωρίς να έχει κανένα δαχτυλίδι χάνει ζωή.",
        "funFacts": [
            "Αν ο Sonic συγκεντρώσει 100 δαχτυλίδια σε μια πίστα κερδίζει αυτόματα μία επιπλέον ζωή.",
            "Τα Chaos Emeralds είναι τα 7 μαγικά πετράδια που του επιτρέπουν να μεταμορφωθεί σε Super Sonic."
        ],
        "source": "https://en.wikipedia.org/wiki/Sonic_the_Hedgehog",
        "tags": ["gaming", "sega", "sonic", "platformer"]
    },
    {
        "id": "gaming_easy_220",
        "text": "Ποιο διάσημο παιχνίδι παζλ με γεωμετρικά σχήματα (τετρόμινο) που πέφτουν δημιουργήθηκε από τον Alexey Pajitnov το 1984;",
        "correct": "Tetris",
        "distractors": ["Puyo Puyo", "Columns", "Breakout"],
        "explanation": "Το Tetris δημιουργήθηκε στη Σοβιετική Ένωση από τον Alexey Pajitnov και έγινε παγκόσμιο φαινόμενο, ιδιαίτερα με την κυκλοφορία του στο Game Boy το 1989.",
        "funFacts": [
            "Η διάσημη μουσική επένδυση του Tetris στο Game Boy (Type A) είναι βασισμένη στο ρωσικό παραδοσιακό τραγούδι 'Korobeiniki'.",
            "Το όνομα Tetris προέρχεται από το ελληνικό αριθμητικό 'τέτρα' (καθώς κάθε κομμάτι αποτελείται από 4 τετράγωνα) και τη λέξη 'τένις'."
        ],
        "source": "https://en.wikipedia.org/wiki/Tetris",
        "tags": ["gaming", "tetris", "puzzle", "retro"]
    },
    {
        "id": "gaming_easy_221",
        "text": "Ποιο είναι το εικονικό Pokémon ηλεκτρικού τύπου με κίτρινο τρίχωμα και ουρά σε σχήμα κεραυνού που είναι η μασκότ του franchise;",
        "correct": "Pikachu",
        "distractors": ["Raichu", "Charmander", "Squirtle"],
        "explanation": "Ο Pikachu είναι το πιο διάσημο Pokémon και η επίσημη μασκότ της σειράς, πιστός σύντροφος του Ash Ketchum στο anime.",
        "funFacts": [
            "Το όνομα Pikachu είναι συνδυασμός του 'pika' (ιαπωνικός ονοματοποιητικός ήχος για την ηλεκτρική σπίθα) και 'chu' (ο ήχος του ποντικιού).",
            "Η σχεδιάστρια Atsuko Nishida βάσισε αρχικά το σχέδιο του Pikachu σε έναν σκίουρο και όχι σε ποντίκι."
        ],
        "source": "https://en.wikipedia.org/wiki/Pikachu",
        "tags": ["gaming", "pokemon", "nintendo", "pikachu"]
    },
    {
        "id": "gaming_easy_222",
        "text": "Στο παιχνίδι battle royale 'Fortnite' της Epic Games, ποιο είναι το εικονικό νόμισμα που χρησιμοποιούν οι παίκτες για αγορές skins;",
        "correct": "V-Bucks",
        "distractors": ["Robux", "Minecoins", "Riot Points"],
        "explanation": "Τα V-Bucks (Vindertech Bucks) είναι το ψηφιακό νόμισμα του Fortnite που χρησιμοποιείται για την αγορά Battle Pass, skins, emotes και καλλυντικών αντικειμένων.",
        "funFacts": [
            "Το Fortnite ξεκίνησε αρχικά ως συνεργατικό παιχνίδι επιβίωσης ενάντια σε ζόμπι (Save the World) πριν προστεθεί το δωρεάν Battle Royale mode.",
            "Οι παίκτες ξεκινούν κάθε αγώνα πηδώντας από το Battle Bus με αλεξίπτωτο ή ανεμόπτερο."
        ],
        "source": "https://en.wikipedia.org/wiki/Fortnite",
        "tags": ["gaming", "fortnite", "epic_games", "battle_royale"]
    },
    {
        "id": "gaming_easy_223",
        "text": "Ποιο είναι το κύριο όπλο μάχης σώμα με σώμα που χρησιμοποιεί ο Gordon Freeman στη σειρά επιστημονικής φαντασίας 'Half-Life';",
        "correct": "Λοστός (Crowbar)",
        "distractors": ["Αλυσοπρίονο", "Μαχαίρι μάχης", "Ρόπαλο"],
        "explanation": "Ο κόκκινος λοστός (crowbar) είναι το πιο εμβληματικό αντικείμενο και αρχικό όπλο του θεωρητικού φυσικού Gordon Freeman στο Half-Life.",
        "funFacts": [
            "Ο λοστός χρησιμοποιείται τόσο για να σπάει ξύλινα κουτιά και εμπόδια όσο και για άμυνα ενάντια στα headcrabs.",
            "Στο Half-Life 2, ο Barney Calhoun παραδίδει στον Gordon τον λοστό του λέγοντας τη διάσημη ατάκα 'Man at work!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_(video_game)",
        "tags": ["gaming", "valve", "half_life", "gordon_freeman", "fps"]
    },
    {
        "id": "gaming_easy_224",
        "text": "Ποια διάσημη σειρά παιχνιδιών της Capcom επικεντρώνεται στην επιβίωση ενάντια σε ζόμπι και τη σατανική φαρμακευτική εταιρεία Umbrella Corporation;",
        "correct": "Resident Evil",
        "distractors": ["Silent Hill", "Dead Space", "Left 4 Dead"],
        "explanation": "Το Resident Evil (γνωστό στην Ιαπωνία ως Biohazard) όρισε τον όρο 'survival horror' το 1996 με τις περιπέτειες των μελών της ομάδας S.T.A.R.S. στη Raccoon City.",
        "funFacts": [
            "Στην Ιαπωνία ονομάζεται Biohazard, αλλά το όνομα άλλαξε στη Δύση επειδή υπήρχε ήδη κατοχυρωμένο εμπορικό σήμα με αυτό το όνομα.",
            "Το πρώτο Resident Evil διαδραματιζόταν στην ανατριχιαστική έπαυλη Spencer στα περίχωρα της Raccoon City."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil",
        "tags": ["gaming", "capcom", "resident_evil", "survival_horror"]
    },
    {
        "id": "gaming_easy_225",
        "text": "Ποια είναι η πατρίδα και το βασίλειο στο οποίο εκτυλίσσονται οι περισσότερες περιπέτειες του Super Mario και της Princess Peach;",
        "correct": "Mushroom Kingdom (Βασίλειο των Μανιταριών)",
        "distractors": ["Hyrule", "Kanto", "Corneria"],
        "explanation": "Το Mushroom Kingdom είναι η φανταστική χώρα όπου ζουν τα Toads και κυβερνάται από την Princess Peach, συχνός στόχος επιθέσεων του Bowser.",
        "funFacts": [
            "Οι κάτοικοι του βασιλείου ονομάζονται Toads και έχουν κεφάλια σε σχήμα καπέλου μανιταριού.",
            "Στο πρώτο παιχνίδι Super Mario Bros., ο Bowser είχε μετατρέψει τους κατοίκους του βασιλείου σε τούβλα με μαύρη μαγεία."
        ],
        "source": "https://en.wikipedia.org/wiki/Mushroom_Kingdom",
        "tags": ["gaming", "mario", "nintendo", "mushroom_kingdom"]
    },
    {
        "id": "gaming_easy_226",
        "text": "Στο παιχνίδι 'Portal' (2007) της Valve, ποιο είναι το όνομα της σαρκαστικής τεχνητής νοημοσύνης που καθοδηγεί και δοκιμάζει την παίκτρια Chell;",
        "correct": "GLaDOS",
        "distractors": ["Cortana", "SHODAN", "EDI"],
        "explanation": "Η GLaDOS (Genetic Lifeform and Disk Operating System) είναι η τεχνητή νοημοσύνη των εργαστηρίων Aperture Science, γνωστή για το μαύρο χιούμορ και την υπόσχεση για 'κέικ'.",
        "funFacts": [
            "Τη φωνή της GLaDOS δανείζει η τραγουδίστρια και ηθοποιός Ellen McLain.",
            "Το τραγούδι των τίτλων τέλους 'Still Alive', γραμμένο από τον Jonathan Coulton, έγινε τεράστια viral επιτυχία."
        ],
        "source": "https://en.wikipedia.org/wiki/GLaDOS",
        "tags": ["gaming", "portal", "valve", "glados"]
    },
    {
        "id": "gaming_easy_227",
        "text": "Ποιο είναι το όνομα του Σπαρτιάτη πολεμιστή και κεντρικού ήρωα της σειράς 'God of War' που εκδικείται τους θεούς του Ολύμπου;",
        "correct": "Kratos",
        "distractors": ["Ares", "Deimos", "Atreus"],
        "explanation": "Ο Kratos, γνωστός και ως το 'Φάντασμα της Σπάρτης' (Ghost of Sparta), είναι ο πρωταγωνιστής του God of War ο οποίος αργότερα μετακομίζει στη σκανδιναβική μυθολογία.",
        "funFacts": [
            "Το λευκό χρώμα στο δέρμα του Kratos οφείλεται στις στάχτες της δολοφονημένης οικογένειάς του που κόλλησαν πάνω του ως κατάρα.",
            "Στα παιχνίδια της σκανδιναβικής εποχής (2018, Ragnarök), ο Kratos αποκαλεί τον γιο του Atreus συχνά απλώς 'Boy'."
        ],
        "source": "https://en.wikipedia.org/wiki/Kratos_(God_of_War)",
        "tags": ["gaming", "god_of_war", "playstation", "kratos", "action"]
    },
    {
        "id": "gaming_easy_228",
        "text": "Ποιο είναι το όνομα της φορητής κονσόλας της Nintendo που κυκλοφόρησε το 1989 με ασπρόμαυρη/πρασινωπή οθόνη και έγινε παγκόσμια επιτυχία;",
        "correct": "Game Boy",
        "distractors": ["Game Gear", "Atari Lynx", "PlayStation Portable"],
        "explanation": "Το Game Boy σχεδιάστηκε από την ομάδα του Gunpei Yokoi και κυκλοφόρησε από τη Nintendo το 1989, πουλώντας πάνω από 118 εκατομμύρια μονάδες μαζί με το Game Boy Color.",
        "funFacts": [
            "Ένα Game Boy επέζησε από βομβαρδισμό στρατώνα στον Πόλεμο του Κόλπου και συνέχιζε να λειτουργεί κανονικά εκτιθέμενο στο Nintendo World Store.",
            "Η τεράστια επιτυχία του οφειλόταν σε μεγάλο βαθμό στο ότι συμπεριλάμβανε το παιχνίδι Tetris στη συσκευασία του."
        ],
        "source": "https://en.wikipedia.org/wiki/Game_Boy",
        "tags": ["gaming", "nintendo", "game_boy", "handheld", "retro"]
    },
    {
        "id": "gaming_easy_229",
        "text": "Ποια διάσημη σειρά παιχνιδιών πάλης της Capcom περιλαμβάνει τους μαχητές Ryu, Ken Masters, Chun-Li και Guile;",
        "correct": "Street Fighter",
        "distractors": ["Tekken", "Mortal Kombat", "Fatal Fury"],
        "explanation": "Το Street Fighter, ιδιαίτερα με το ιστορικό Street Fighter II (1991), έθεσε τις βάσεις για όλα τα σύγχρονα competitive fighting games.",
        "funFacts": [
            "Η Chun-Li θεωρείται η πρώτη πρωταγωνίστρια γυναίκα μαχήτρια σε παιχνίδι ένας-εναντίον-ενός.",
            "Η ειδική κίνηση Hadoken (κύμα ενέργειας) του Ryu εκτελείται με κίνηση τέταρτου κύκλου προς τα εμπρός και γροθιά."
        ],
        "source": "https://en.wikipedia.org/wiki/Street_Fighter",
        "tags": ["gaming", "capcom", "street_fighter", "fighting"]
    },
    {
        "id": "gaming_easy_230",
        "text": "Ποιος είναι ο κύριος αντίπαλος και αρχέγονος εχθρός του Crash Bandicoot που φοράει κίτρινη στολή με το γράμμα 'N' στο μέτωπο;",
        "correct": "Doctor Neo Cortex",
        "distractors": ["Doctor Eggman", "Aku Aku", "Ripper Roo"],
        "explanation": "Ο Doctor Neo Cortex είναι ο τρελός επιστήμονας που δημιούργησε τον Crash Bandicoot μέσω μεταλλάξεων και αποτελεί τον κύριο κακό της σειράς.",
        "funFacts": [
            "Η σειρά Crash Bandicoot αναπτύχθηκε αρχικά από τη Naughty Dog για το πρώτο PlayStation.",
            "Η μαγική μάσκα που προστατεύει τον Crash ονομάζεται Aku Aku, ενώ ο δίδυμος κακός αδελφός της ονομάζεται Uka Uka."
        ],
        "source": "https://en.wikipedia.org/wiki/Doctor_Neo_Cortex",
        "tags": ["gaming", "crash_bandicoot", "playstation", "naughty_dog"]
    },
    {
        "id": "gaming_easy_231",
        "text": "Στο παιχνίδι 'Among Us', πώς ονομάζονται οι παίκτες που πρέπει να σαμποτάρουν το σκάφος και να εξοντώσουν κρυφά το υπόλοιπο πλήρωμα;",
        "correct": "Impostors (Απατεώνες)",
        "distractors": ["Traitors", "Hunters", "Spies"],
        "explanation": "Στο κοινωνικό παιχνίδι μυστηρίου Among Us, οι κανονικοί παίκτες είναι Crewmates και οι κρυφοί δολοφόνοι είναι Impostors.",
        "funFacts": [
            "Το παιχνίδι κυκλοφόρησε το 2018 αλλά γνώρισε εκρηκτική παγκόσμια επιτυχία το 2020 κατά τη διάρκεια της πανδημίας χάρη σε Twitch streamers.",
            "Οι παίκτες μπορούν να συγκαλέσουν Emergency Meeting πατώντας το μεγάλο κόκκινο κουμπί στην καφετέρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Among_Us",
        "tags": ["gaming", "among_us", "innersloth", "indie", "multiplayer"]
    },
    {
        "id": "gaming_easy_232",
        "text": "Ποιο είναι το είδος του ζώου που πρωταγωνιστεί στη σειρά παιχνιδιών 'Sonic the Hedgehog' της Sega;",
        "correct": "Σκαντζόχοιρος (Hedgehog)",
        "distractors": ["Αλεπού", "Έχιδνα", "Κουνέλι"],
        "explanation": "Ο Sonic είναι ένας μπλε ανθρωπόμορφος σκαντζόχοιρος με την ικανότητα να τρέχει με υπερηχητική ταχύτητα.",
        "funFacts": [
            "Πριν επιλεγεί ο σκαντζόχοιρος, η Sega εξέταζε ως πιθανή μασκότ έναν αρμαδίλλο, έναν σκίουρο, ακόμη και έναν άντρα με πιτζάμες που έμοιαζε στον Theodore Roosevelt.",
            "Ο καλύτερος φίλος του Sonic, ο Tails, είναι αλεπού με δύο ουρές, ενώ ο Knuckles είναι έχιδνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_(character)",
        "tags": ["gaming", "sonic", "sega", "characters"]
    },
    {
        "id": "gaming_easy_233",
        "text": "Ποιο είναι το όνομα του διάσημου franchise παιχνιδιών προσομοίωσης ζωής της Maxis όπου οι χαρακτήρες μιλούν τη γλώσσα 'Simlish';",
        "correct": "The Sims",
        "distractors": ["Animal Crossing", "Second Life", "Stardew Valley"],
        "explanation": "Το The Sims δημιουργήθηκε από τον Will Wright και κυκλοφόρησε από την Electronic Arts το 2000, αποτελώντας ένα από τα πιο επιτυχημένα παιχνίδια προσομοίωσης όλων των εποχών.",
        "funFacts": [
            "Ο πράσινος περιστρεφόμενος κρύσταλλος που αιωρείται πάνω από το κεφάλι των Sims ονομάζεται Plumbob.",
            "Η γλώσσα Simlish επινοήθηκε σκόπιμα με ασυναρτησίες ώστε οι παίκτες να φαντάζονται μόνοι τους τους διαλόγους και να μην κουράζονται από επαναλήψεις."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Sims",
        "tags": ["gaming", "the_sims", "ea", "simulation", "maxis"]
    },
    {
        "id": "gaming_easy_234",
        "text": "Ποια επαναστατική υβριδική κονσόλα κυκλοφόρησε η Nintendo το 2017, που μπορεί να παιχτεί τόσο στην τηλεόραση όσο και ως φορητή;",
        "correct": "Nintendo Switch",
        "distractors": ["Wii U", "Nintendo 3DS", "GameCube"],
        "explanation": "Το Nintendo Switch κυκλοφόρησε τον Μάρτιο του 2017 με αποσπώμενα χειριστήρια Joy-Con και έγινε μία από τις πιο επιτυχημένες κονσόλες στην ιστορία.",
        "funFacts": [
            "Τα χειριστήρια Joy-Con διαθέτουν εξελιγμένη τεχνολογία δόνησης που ονομάζεται HD Rumble.",
            "Οι κάρτες παιχνιδιών του Switch είναι επιστρωμένες με μια εξαιρετικά πικρή ουσία (benzoate denatonium) για να αποτρέπεται η κατάποσή τους από μικρά παιδιά."
        ],
        "source": "https://en.wikipedia.org/wiki/Nintendo_Switch",
        "tags": ["gaming", "nintendo", "switch", "consoles"]
    },
    {
        "id": "gaming_easy_235",
        "text": "Ποιο είναι το όνομα του γορίλα που ρίχνει βαρέλια στο κλασικό arcade παιχνίδι του 1981 της Nintendo όπου πρωτοεμφανίστηκε ο Mario;",
        "correct": "Donkey Kong",
        "distractors": ["King K. Rool", "Diddy Kong", "Bowser"],
        "explanation": "Στο Donkey Kong (1981), ο Jumpman (ο μετέπειτα Mario) έπρεπε να ανεβεί σκαλωσιές πηδώντας πάνω από κυλιόμενα βαρέλια για να σώσει την Pauline.",
        "funFacts": [
            "Ο Shigeru Miyamoto επέλεξε τη λέξη 'Donkey' πιστεύοντας ότι στα αγγλικά σήμαινε 'πεισματάρης' ή 'κουτός'.",
            "Στο αρχικό παιχνίδι ο Mario ονομαζόταν απλώς Jumpman και ήταν μαραγκός, όχι υδραυλικός."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_(video_game)",
        "tags": ["gaming", "arcade", "donkey_kong", "nintendo", "retro"]
    },
    {
        "id": "gaming_easy_236",
        "text": "Στο παιχνίδι 'Mortal Kombat', ποια διάσημη φράση ακούγεται από τον εκφωνητή στο τέλος της μάχης πριν την εκτέλεση ενός Fatality;",
        "correct": "Finish Him! (ή Finish Her!)",
        "distractors": ["Game Over!", "KO!", "Fight!"],
        "explanation": "Η φράση 'Finish Him!' ή 'Finish Her!' καλεί τον νικητή παίκτη να πραγματοποιήσει μια θεαματική και βίαιη τελική κίνηση (Fatality) στον ζαλισμένο αντίπαλο.",
        "funFacts": [
            "Το Mortal Kombat (1992) των Ed Boon και John Tobias οδήγησε άμεσα στη δημιουργία του συστήματος ηλικιακής διαβάθμισης ESRB λόγω της βίας του.",
            "Ο χαρακτήρας Scorpion έγινε διάσημος για την κραυγή 'Get over here!' όταν πετάει το δόρυ-αλυσίδα του."
        ],
        "source": "https://en.wikipedia.org/wiki/Mortal_Kombat",
        "tags": ["gaming", "mortal_kombat", "fighting", "midway"]
    },
    {
        "id": "gaming_easy_237",
        "text": "Ποιο είναι το όνομα του ροζ, σφαιρικού ήρωα της Nintendo που μπορεί να εισπνέει εχθρούς και να αντιγράφει τις δυνάμεις τους;",
        "correct": "Kirby",
        "distractors": ["Jigglypuff", "Wartortle", "Ditto"],
        "explanation": "Ο Kirby δημιουργήθηκε από τον Masahiro Sakurai για το στούντιο HAL Laboratory και έκανε το ντεμπούτο του στο Game Boy το 1992.",
        "funFacts": [
            "Ο Kirby πήρε το όνομά του προς τιμήν του John Kirby Jr., του Αμερικανού δικηγόρου που υπερασπίστηκε επιτυχώς τη Nintendo στη δίκη με τη Universal για το Donkey Kong.",
            "Αρχικά ο Kirby ήταν απλώς ένα πρόχειρο στρογγυλό placeholder γραφικό μέχρι να σχεδιαστεί ο κανονικός χαρακτήρας."
        ],
        "source": "https://en.wikipedia.org/wiki/Kirby_(character)",
        "tags": ["gaming", "kirby", "nintendo", "characters"]
    },
    {
        "id": "gaming_easy_238",
        "text": "Ποια σειρά βιντεοπαιχνιδιών δράσης της Ubisoft περιλαμβάνει τους Assassins, τους Templars και τη συσκευή εικονικής μνήμης Animus;",
        "correct": "Assassin's Creed",
        "distractors": ["Prince of Persia", "Watch Dogs", "Far Cry"],
        "explanation": "Το Assassin's Creed ξεκίνησε το 2007 και εξιστορεί τη μακραίωνη σύγκρουση μεταξύ της Αδελφότητας των Ασασίνων και των Ναϊτών Ιπποτών σε διάφορες ιστορικές εποχές.",
        "funFacts": [
            "Το παιχνίδι ξεκίνησε αρχικά ως spin-off σχέδιο με τίτλο 'Prince of Persia: Assassins'.",
            "Η χαρακτηριστική κίνηση όπου ο ασασίνος πηδάει από ψηλά κτίρια μέσα σε ένα κάρο με άχυρα ονομάζεται 'Leap of Faith'."
        ],
        "source": "https://en.wikipedia.org/wiki/Assassin%27s_Creed",
        "tags": ["gaming", "assassins_creed", "ubisoft", "action"]
    },
    {
        "id": "gaming_easy_239",
        "text": "Ποια είναι η πλατφόρμα ψηφιακής διανομής παιχνιδιών για ηλεκτρονικούς υπολογιστές που αναπτύχθηκε από τη Valve και κυκλοφόρησε το 2003;",
        "correct": "Steam",
        "distractors": ["Epic Games Store", "Origin", "GOG"],
        "explanation": "Το Steam ξεκίνησε ως εργαλείο αυτόματης ενημέρωσης για παιχνίδια όπως το Counter-Strike και εξελίχθηκε στη μεγαλύτερη ψηφιακή πλατφόρμα gaming για PC στον κόσμο.",
        "funFacts": [
            "Όταν κυκλοφόρησε το Half-Life 2 το 2004, απαιτούσε υποχρεωτικά εγκατάσταση του Steam, προκαλώντας έντονες αντιδράσεις τότε στους παίκτες.",
            "Το Steam κατέχει ρεκόρ ταυτόχρονων συνδεδεμένων χρηστών που ξεπερνά τα 38 εκατομμύρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Steam_(service)",
        "tags": ["gaming", "steam", "valve", "pc"]
    },
    {
        "id": "gaming_easy_240",
        "text": "Ποιο είναι το όνομα του μικρού μοβ δράκου που είναι φίλος με τη λιβελούλα Sparx και πρωταγωνιστεί σε κλασικά platformers του PlayStation;",
        "correct": "Spyro the Dragon",
        "distractors": ["Charizard", "Bahamut", "Ridley"],
        "explanation": "Ο Spyro δημιουργήθηκε από την Insomniac Games για το πρώτο PlayStation το 1998 και διακρίνεται για την ικανότητά του να εκπνέει φωτιά και να κουτουλάει με τα κέρατά του.",
        "funFacts": [
            "Ο Stewart Copeland, ντράμερ του θρυλικού συγκροτήματος The Police, συνέθεσε το soundtrack των πρώτων παιχνιδιών Spyro.",
            "Αρχικά ο Spyro σχεδιαζόταν να είναι πράσινος, αλλά άλλαξε σε μοβ για να ξεχωρίζει από τα γρασίδια των πιστών."
        ],
        "source": "https://en.wikipedia.org/wiki/Spyro_the_Dragon",
        "tags": ["gaming", "spyro", "playstation", "insomniac", "platformer"]
    },
    {
        "id": "gaming_easy_241",
        "text": "Στο παιχνίδι 'Grand Theft Auto V', σε ποια φανταστική πόλη που βασίζεται στο Λος Άντζελες διαδραματίζεται η ιστορία;",
        "correct": "Los Santos",
        "distractors": ["Liberty City", "Vice City", "San Fierro"],
        "explanation": "Το GTA V διαδραματίζεται στην πολιτεία San Andreas και κυρίως στην πόλη Los Santos, μια σατιρική απόδοση του πραγματικού Λος Άντζελες της Καλιφόρνια.",
        "funFacts": [
            "Το GTA V είχε τρεις εναλλασσόμενους πρωταγωνιστές: τον Michael, τον Franklin και τον Trevor.",
            "Έβγαλε πάνω από 1 δισεκατομμύριο δολάρια μέσα στις πρώτες τρεις ημέρες κυκλοφορίας του, σπάζοντας όλα τα ρεκόρ της βιομηχανίας ψυχαγωγίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto_V",
        "tags": ["gaming", "gta", "rockstar", "los_santos", "open_world"]
    },
    {
        "id": "gaming_easy_242",
        "text": "Ποιο είναι το επαναστατικό παιχνίδι σκοποβολής πρώτου προσώπου (FPS) του 1993 από την id Software με ήρωα τον 'Doom Slayer' στον πλανήτη Άρη;",
        "correct": "Doom",
        "distractors": ["Quake", "Wolfenstein 3D", "Unreal"],
        "explanation": "Το Doom των John Carmack και John Romero εκτόξευσε τη δημοτικότητα των 3D first-person shooters και του δικτυακού deathmatch σε όλο τον κόσμο.",
        "funFacts": [
            "Το πιο ισχυρό όπλο στο παιχνίδι ονομάζεται BFG 9000 (Big Fucking Gun).",
            "Η φράση 'Can it run Doom?' έγινε παγκόσμιο meme, καθώς προγραμματιστές έχουν τρέξει το παιχνίδι σε εκτυπωτές, φούρνους μικροκυμάτων και ψηφιακά θερμόμετρα."
        ],
        "source": "https://en.wikipedia.org/wiki/Doom_(1993_video_game)",
        "tags": ["gaming", "doom", "id_software", "fps", "retro"]
    },
    {
        "id": "gaming_easy_243",
        "text": "Ποιο είναι το όνομα του αδελφού του Super Mario που φοράει πράσινη μπλούζα και καπέλο με το γράμμα 'L';",
        "correct": "Luigi",
        "distractors": ["Wario", "Waluigi", "Toad"],
        "explanation": "Ο Luigi είναι ο δίδυμος αλλά ψηλότερος αδελφός του Mario και πρωταγωνιστεί στη δική του σειρά παιχνιδιών 'Luigi's Mansion'.",
        "funFacts": [
            "Στο Luigi's Mansion, ο Luigi χρησιμοποιεί μια τροποποιημένη ηλεκτρική σκούπα που ονομάζεται Poltergust 3000 για να αιχμαλωτίζει φαντάσματα.",
            "Το 2013 ανακηρύχθηκε επίσημα από τη Nintendo ως 'The Year of Luigi' για να γιορταστούν τα 30 χρόνια από το ντεμπούτο του."
        ],
        "source": "https://en.wikipedia.org/wiki/Luigi",
        "tags": ["gaming", "mario", "luigi", "nintendo", "characters"]
    },
    {
        "id": "gaming_easy_244",
        "text": "Ποιο εξαιρετικά δημοφιλές παιχνίδι για κινητά τηλέφωνα περιλαμβάνει το πέταγμα θυμωμένων πουλιών με σφεντόνα ενάντια σε πράσινα γουρούνια;",
        "correct": "Angry Birds",
        "distractors": ["Flappy Bird", "Fruit Ninja", "Cut the Rope"],
        "explanation": "Το Angry Birds αναπτύχθηκε από τη φινλανδική εταιρεία Rovio Entertainment το 2009 και έγινε παγκόσμιο φαινόμενο σε smartphones.",
        "funFacts": [
            "Το κόκκινο κεντρικό πουλί ονομάζεται Red, το κίτρινο τριγωνικό πουλί είναι ο Chuck και το μαύρο εκρηκτικό είναι ο Bomb.",
            "Τα πράσινα γουρούνια σχεδιάστηκαν πράσινα επειδή την εποχή ανάπτυξης του παιχνιδιού υπήρχε η επιδημία της γρίπης των χοίρων."
        ],
        "source": "https://en.wikipedia.org/wiki/Angry_Birds",
        "tags": ["gaming", "angry_birds", "rovio", "mobile"]
    },
    {
        "id": "gaming_easy_245",
        "text": "Ποιο διάσημο RPG φαντασίας της Bethesda Game Studios (The Elder Scrolls V) ξεκινά με τον παίκτη να ξυπνά ως αιχμάλωτος σε ένα κάρο;",
        "correct": "Skyrim",
        "distractors": ["Oblivion", "Morrowind", "Fallout 3"],
        "explanation": "Το The Elder Scrolls V: Skyrim κυκλοφόρησε το 2011 (11/11/11) και αφηγείται την ιστορία του Dragonborn (Dovahkiin) στην παγωμένη επαρχία Skyrim.",
        "funFacts": [
            "Η ατάκα 'Hey you, you're finally awake' από την εισαγωγή έγινε ένα από τα πιο γνωστά memes στο διαδίκτυο.",
            "Η πιο διάσημη δρακοκραυγή (Dragon Shout) του παιχνιδιού είναι το 'Fus Ro Dah' (Unrelenting Force)."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
        "tags": ["gaming", "skyrim", "bethesda", "rpg", "elder_scrolls"]
    },
    {
        "id": "gaming_easy_246",
        "text": "Ποιο είναι το όνομα του εμβληματικού ρομπότ με τη μπλε πανοπλία της Capcom που πολεμά τα κακόβουλα ρομπότ του Dr. Wily;",
        "correct": "Mega Man (Rockman)",
        "distractors": ["Metroid", "Bomberman", "Astro Boy"],
        "explanation": "Ο Mega Man (γνωστός στην Ιαπωνία ως Rockman) δημιουργήθηκε από την Capcom το 1987 και έχει την ικανότητα να αποκτά τα όπλα των Robot Masters που νικάει.",
        "funFacts": [
            "Σχεδιάστηκε μπλε επειδή η παλέτα χρωμάτων του NES είχε τις περισσότερες διαβαθμίσεις στο μπλε χρώμα.",
            "Ο πιστός σκύλος-ρομπότ του ονομάζεται Rush και μπορεί να μεταμορφώνεται σε ελατήριο, τζετ ή υποβρύχιο."
        ],
        "source": "https://en.wikipedia.org/wiki/Mega_Man",
        "tags": ["gaming", "capcom", "mega_man", "nes", "retro"]
    },
    {
        "id": "gaming_easy_247",
        "text": "Στο παιχνίδι ποδοσφαίρου με αυτοκίνητα 'Rocket League', ποιο είναι το βασικό αντικείμενο που οι παίκτες προσπαθούν να στείλουν στα αντίπαλα δίχτυα;",
        "correct": "Μια γιγάντια μπάλα",
        "distractors": ["Ένα μεταλλικό puck", "Μια βόμβα", "Ένας κρύσταλλος"],
        "explanation": "Το Rocket League της Psyonix συνδυάζει πυραυλοκίνητα ακροβατικά αυτοκίνητα με ποδόσφαιρο, όπου οι παίκτες χτυπούν μια υπερμεγέθη μπάλα για να σκοράρουν.",
        "funFacts": [
            "Ο προκάτοχος του Rocket League είχε τον εξαιρετικά μακροσκελή τίτλο 'Supersonic Acrobatic Rocket-Powered Battle-Cars'.",
            "Τα οχήματα μπορούν να κάνουν διπλά άλματα, να πετάξουν στον αέρα με boost και να οδηγήσουν πάνω στους τοίχους της αρένας."
        ],
        "source": "https://en.wikipedia.org/wiki/Rocket_League",
        "tags": ["gaming", "rocket_league", "psyonix", "sports"]
    },
    {
        "id": "gaming_easy_248",
        "text": "Ποιος είναι ο διάσημος κυνηγός τεράτων (Witcher) με τα λευκά μαλλιά και τα δύο σπαθιά στη σειρά 'The Witcher' της CD Projekt Red;",
        "correct": "Geralt of Rivia (Γκέραλτ της Ρίβια)",
        "distractors": ["Vesemir", "Eskel", "Dandelion"],
        "explanation": "Ο Geralt της Ρίβια, γνωστός και ως 'Λευκός Λύκος', είναι ο πρωταγωνιστής της σειράς παιχνιδιών The Witcher, βασισμένης στα βιβλία του Andrzej Sapkowski.",
        "funFacts": [
            "Κουβαλάει δύο σπαθιά στην πλάτη του: ένα ατσάλινο για ανθρώπους και ζώα, και ένα ασημένιο για μαγικά τέρατα.",
            "Το The Witcher 3: Wild Hunt (2015) κέρδισε πάνω από 250 βραβεία Game of the Year παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Geralt_of_Rivia",
        "tags": ["gaming", "the_witcher", "cd_projekt_red", "geralt", "rpg"]
    },
    {
        "id": "gaming_easy_249",
        "text": "Ποιο είναι το όνομα του δημοφιλούς παιχνιδιού match-3 της King με καραμέλες και γλυκά που έκανε θραύση στο Facebook και τα κινητά τηλέφωνα;",
        "correct": "Candy Crush Saga",
        "distractors": ["Bejeweled", "Cookie Jam", "Farm Heroes Saga"],
        "explanation": "Το Candy Crush Saga κυκλοφόρησε το 2012 από την εταιρεία King και έγινε ένα από τα πιο κερδοφόρα και παιγμένα mobile games όλων των εποχών.",
        "funFacts": [
            "Αν συνδυάσεις πέντε καραμέλες του ίδιου χρώματος σε ευθεία γραμμή, δημιουργείς μια σοκολατένια βόμβα με πολύχρωμες πέρλες.",
            "Η μητρική εταιρεία King εξαγοράστηκε από την Activision Blizzard το 2016 έναντι 5,9 δισεκατομμυρίων δολαρίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Candy_Crush_Saga",
        "tags": ["gaming", "candy_crush", "king", "mobile", "puzzle"]
    },
    {
        "id": "gaming_easy_250",
        "text": "Ποιο ήταν το πρώτο επιτυχημένο εμπορικά βιντεοπαιχνίδι arcade της Atari (1972) που προσομοίωνε το πινγκ-πονγκ με δύο γραμμές και μια κουκκίδα;",
        "correct": "Pong",
        "distractors": ["Breakout", "Space Invaders", "Asteroids"],
        "explanation": "Το Pong δημιουργήθηκε από τον Allan Alcorn υπό την καθοδήγηση του Nolan Bushnell στην Atari και αποτέλεσε τον θεμέλιο λίθο της βιομηχανίας των video games.",
        "funFacts": [
            "Το πρωτότυπο μηχάνημα εγκαταστάθηκε σε μια τοπική παμπ (Andy Capp's Tavern) στην Καλιφόρνια και μπλόκαρε από τα πάρα πολλά κέρματα που έριχναν οι θαμώνες.",
            "Η Atari ιδρύθηκε από τους Nolan Bushnell και Ted Dabney το 1972."
        ],
        "source": "https://en.wikipedia.org/wiki/Pong",
        "tags": ["gaming", "pong", "atari", "arcade", "retro"]
    },
    {
        "id": "gaming_easy_251",
        "text": "Ποιο είναι το όνομα της διαγαλαξιακής κυνηγού επικηρυγμένων με τη διάσημη πορτοκαλοκίτρινη Power Suit στη σειρά 'Metroid' της Nintendo;",
        "correct": "Samus Aran",
        "distractors": ["Jill Valentine", "Joanna Dark", "Bayonetta"],
        "explanation": "Η Samus Aran είναι η πρωταγωνίστρια της σειράς Metroid. Στο τέλος του πρώτου παιχνιδιού (1986), αποκαλύφθηκε προς έκπληξη των παικτών ότι κάτω από την πανοπλία κρυβόταν μια γυναίκα.",
        "funFacts": [
            "Η αποκάλυψη του φύλου της Samus στο αρχικό Metroid του NES εξαρτιόταν από το πόσο γρήγορα τερμάτιζε ο παίκτης το παιχνίδι.",
            "Η Samus μεγάλωσε με την αρχαία εξωγήινη φυλή των Chozo, οι οποίοι της έδωσαν το DNA τους και την προηγμένη στολή της."
        ],
        "source": "https://en.wikipedia.org/wiki/Samus_Aran",
        "tags": ["gaming", "metroid", "nintendo", "samus_aran"]
    },
    {
        "id": "gaming_easy_252",
        "text": "Στο παιχνίδι 'Overwatch' της Blizzard, ποια Βρετανίδα ηρωίδα με διπλά πιστόλια μπορεί να τηλεμεταφέρεται και να γυρίζει τον χρόνο πίσω;",
        "correct": "Tracer (Lena Oxton)",
        "distractors": ["Widowmaker", "D.Va", "Mercy"],
        "explanation": "Η Tracer είναι η κεντρική μασκότ του Overwatch και μπορεί να κάνει Dash (Blink) και να ανακαλεί την προσωπική της χρονική γραμμή (Recall).",
        "funFacts": [
            "Η διάσημη ατάκα της είναι 'Cheers, love! The cavalry's here!'.",
            "Η συσκευή στο στήθος της που σταθεροποιεί τη μοριακή της δομή στον χρόνο ονομάζεται Chronal Accelerator και σχεδιάστηκε από τον γορίλα-επιστήμονα Winston."
        ],
        "source": "https://en.wikipedia.org/wiki/Tracer_(Overwatch)",
        "tags": ["gaming", "overwatch", "blizzard", "tracer", "fps"]
    },
    {
        "id": "gaming_easy_253",
        "text": "Ποιο είναι το όνομα του άπληστου ρακούν-επιχειρηματία στη σειρά 'Animal Crossing' που δίνει στεγαστικά δάνεια στον παίκτη;",
        "correct": "Tom Nook",
        "distractors": ["K.K. Slider", "Isabelle", "Blathers"],
        "explanation": "Ο Tom Nook (Tanukichi στην Ιαπωνία) είναι ένας ιαπωνικός σκύλος-ρακούν (tanuki) που διαχειρίζεται τα καταστήματα και τα στεγαστικά δάνεια στο Animal Crossing.",
        "funFacts": [
            "Το νόμισμα του παιχνιδιού που χρησιμοποιείται για την αποπληρωμή των δανείων του Tom Nook ονομάζεται Bells.",
            "Τα ανίψια του (ή μαθητευόμενοι), Timmy και Tommy, αναλαμβάνουν αργότερα το παντοπωλείο Nook's Cranny."
        ],
        "source": "https://en.wikipedia.org/wiki/Tom_Nook",
        "tags": ["gaming", "animal_crossing", "nintendo", "tom_nook"]
    },
    {
        "id": "gaming_easy_254",
        "text": "Ποιο ιστορικό παιχνίδι στρατηγικής της Ensemble Studios και της Microsoft περιλαμβάνει φράσεις όπως 'Wololo' από τους ιερείς;",
        "correct": "Age of Empires",
        "distractors": ["Warcraft", "Command & Conquer", "StarCraft"],
        "explanation": "Το Age of Empires (1997) και το Age of Empires II (1999) είναι από τα πιο αγαπημένα real-time strategy (RTS) παιχνίδια, όπου οι ιερείς προσηλυτίζουν εχθρικές μονάδες φωνάζοντας 'Wololo'.",
        "funFacts": [
            "Ο ήχος 'Wololo' έγινε ένα από τα πιο αναγνωρίσιμα ηχητικά memes στην κουλτούρα του PC gaming.",
            "Στο Age of Empires II, οι παίκτες προχωρούν μέσα από τέσσερις ιστορικές εποχές: Dark Age, Feudal Age, Castle Age και Imperial Age."
        ],
        "source": "https://en.wikipedia.org/wiki/Age_of_Empires",
        "tags": ["gaming", "age_of_empires", "microsoft", "rts", "pc"]
    },
    {
        "id": "gaming_easy_255",
        "text": "Ποια είναι η δημοφιλής πλατφόρμα δημιουργίας και φιλοξενίας παιχνιδιών από χρήστες όπου το εσωτερικό νόμισμα ονομάζεται Robux;",
        "correct": "Roblox",
        "distractors": ["Minecraft", "Krunker", "Garry's Mod"],
        "explanation": "Το Roblox κυκλοφόρησε το 2006 από τους David Baszucki και Erik Cassel και επιτρέπει σε εκατομμύρια δημιουργούς να προγραμματίζουν δικά τους παιχνίδια στη γλώσσα Luau.",
        "funFacts": [
            "Ο διάσημος ήχος θανάτου του Roblox 'Oof' έγινε εξαιρετικά δημοφιλής πριν αφαιρεθεί λόγω πνευματικών δικαιωμάτων.",
            "Πολλά παιχνίδια μέσα στο Roblox, όπως το 'Adopt Me!' και το 'Brookhaven', έχουν συγκεντρώσει δεκάδες δισεκατομμύρια επισκέψεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Roblox",
        "tags": ["gaming", "roblox", "metaverse", "online"]
    },
    {
        "id": "gaming_easy_256",
        "text": "Ποιος είναι ο κύριος κακός και βασιλιάς των Koopas που απάγει συνεχώς την πριγκίπισσα Peach στα παιχνίδια Mario;",
        "correct": "Bowser",
        "distractors": ["Wario", "King Boo", "Kamek"],
        "explanation": "Ο Bowser (γνωστός στην Ιαπωνία ως King Koopa) είναι ένα γιγάντιο οπλισμένο ερπετό με αγκάθια στο καβούκι που εκπνέει φωτιά.",
        "funFacts": [
            "Ο Bowser έχει έναν γιο που ονομάζεται Bowser Jr., ο οποίος συχνά οδηγεί το Koopa Clown Copter.",
            "Στο Super Mario 64, ο Mario νικάει τον Bowser πιάνοντάς τον από την ουρά, περιστρέφοντάς τον και πετώντας τον σε βόμβες."
        ],
        "source": "https://en.wikipedia.org/wiki/Bowser",
        "tags": ["gaming", "mario", "nintendo", "bowser", "villains"]
    },
    {
        "id": "gaming_easy_257",
        "text": "Ποια εταιρεία κυκλοφόρησε την κονσόλα Mega Drive (γνωστή στη Βόρεια Αμερική ως Genesis) το 1988;",
        "correct": "Sega",
        "distractors": ["Nintendo", "Sony", "Atari"],
        "explanation": "Το Sega Genesis / Mega Drive ήταν η 16-bit κονσόλα της Sega που κονταροχτυπήθηκε σφοδρά με το Super Nintendo στη δεκαετία του '90.",
        "funFacts": [
            "Η καμπάνια προώθησης της κονσόλας στις ΗΠΑ έγινε διάσημη με το σύνθημα 'Genesis does what Nintendon't'.",
            "Η κονσόλα διαφήμιζε τη λειτουργία 'Blast Processing' για να τονίσει τη μεγάλη ταχύτητα του Sonic the Hedgehog."
        ],
        "source": "https://en.wikipedia.org/wiki/Sega_Genesis",
        "tags": ["gaming", "sega", "consoles", "genesis", "mega_drive", "retro"]
    },
    {
        "id": "gaming_easy_258",
        "text": "Ποιο είναι το όνομα του δημοφιλούς party game της Mediatonic όπου 60 παίκτες-ζελεδάκια διαγωνίζονται σε τρελές κούρσες εμποδίων;",
        "correct": "Fall Guys",
        "distractors": ["Stumble Guys", "Gang Beasts", "Human: Fall Flat"],
        "explanation": "Το Fall Guys (αρχικά Fall Guys: Ultimate Knockout) κυκλοφόρησε το 2020 αντλώντας έμπνευση από τηλεοπτικά παιχνίδια όπως το Takeshi's Castle και το Wipeout.",
        "funFacts": [
            "Το αντικείμενο του πόθου στον τελικό γύρο κάθε αγώνα είναι το περίφημο Crown (Στέμμα).",
            "Οι χαρακτήρες είναι εμπνευσμένοι από πολύχρωμα ζελεδάκια (jellybeans) και συχνά σκοντάφτουν με αστείο τρόπο."
        ],
        "source": "https://en.wikipedia.org/wiki/Fall_Guys",
        "tags": ["gaming", "fall_guys", "mediatonic", "party_game", "multiplayer"]
    },
    {
        "id": "gaming_easy_259",
        "text": "Ποιο είναι το όνομα του πιστού φίλου του Sonic the Hedgehog, της πορτοκαλί αλεπούς με τις δύο ουρές που μπορεί να πετάει;",
        "correct": "Miles 'Tails' Prower",
        "distractors": ["Knuckles the Echidna", "Shadow the Hedgehog", "Silver the Hedgehog"],
        "explanation": "Ο Tails (Miles Prower) πρωτοεμφανίστηκε στο Sonic the Hedgehog 2 (1992) και είναι ένας ιδιοφυής μηχανικός που πετάει περιστρέφοντας τις δύο ουρές του σαν έλικα ελικοπτέρου.",
        "funFacts": [
            "Το πραγματικό του όνομα 'Miles Prower' είναι λογοπαίγνιο με τη φράση 'miles per hour' (μίλια την ώρα).",
            "Ο Tails πιλοτάρει επίσης το χαρακτηριστικό κόκκινο διπλάνο του Sonic, το Tornado."
        ],
        "source": "https://en.wikipedia.org/wiki/Tails_(character)",
        "tags": ["gaming", "sonic", "sega", "tails", "characters"]
    },
    {
        "id": "gaming_easy_260",
        "text": "Στο παιχνίδι 'League of Legends' της Riot Games, πώς ονομάζεται ο κύριος χάρτης 5 εναντίον 5 όπου διεξάγονται οι περισσότεροι αγώνες;",
        "correct": "Summoner's Rift",
        "distractors": ["Howling Abyss", "Twisted Treeline", "Crystal Scar"],
        "explanation": "Το Summoner's Rift είναι το εμβληματικό πεδίο μάχης του League of Legends με τρεις λωρίδες (top, mid, bot) και την περιοχή της ζούγκλας (jungle).",
        "funFacts": [
            "Ο ισχυρότερος ουδέτερος στόχος στη ζούγκλα του χάρτη είναι ο Baron Nashor (αναγραμματισμός του Roshan από το DotA).",
            "Ο τελικός στόχος κάθε ομάδας είναι η καταστροφή του Nexus της αντίπαλης βάσης."
        ],
        "source": "https://en.wikipedia.org/wiki/League_of_Legends",
        "tags": ["gaming", "league_of_legends", "riot_games", "moba", "esports"]
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
    print(f"Loaded {len(questions)} questions for gaming_easy batch 1.")
    validate_and_append("gaming", "easy", 1, questions)

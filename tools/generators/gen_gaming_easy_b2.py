# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_easy_261",
        "text": "Ποιο είναι το όνομα του κόκκινου φαντάσματος στο κλασικό arcade παιχνίδι 'Pac-Man', το οποίο ακολουθεί επίμονα τον παίκτη;",
        "correct": "Blinky",
        "distractors": ["Pinky", "Inky", "Clyde"],
        "explanation": "Ο Blinky (με το ιαπωνικό παρατσούκλι Akabei ή Shadow) είναι το κόκκινο φάντασμα που καταδιώκει άμεσα και επιθετικά τον Pac-Man.",
        "funFacts": [
            "Κάθε ένα από τα 4 φαντάσματα έχει διαφορετικό αλγόριθμο τεχνητής νοημοσύνης (AI): ο Blinky κυνηγάει, ο Pinky προσπαθεί να στήσει ενέδρα, ο Inky κινείται απρόβλεπτα και ο Clyde περιπολεί.",
            "Όταν απομένουν λίγες τελείες στην πίστα, ο Blinky αυξάνει την ταχύτητά του, μια κατάσταση γνωστή ως 'Cruise Elroy'."
        ],
        "source": "https://en.wikipedia.org/wiki/Pac-Man",
        "tags": ["gaming", "pac_man", "arcade", "namco", "retro"]
    },
    {
        "id": "gaming_easy_262",
        "text": "Στο κλασικό παιχνίδι 'Super Mario Bros.' (1985), τι πρέπει να πιάσει ο Mario στο τέλος κάθε πίστας για να ολοκληρώσει το επίπεδο;",
        "correct": "Τον ιστό της σημαίας (Flagpole)",
        "distractors": ["Ένα χρυσό αστέρι", "Ένα μαγικό δαχτυλίδι", "Ένα σεντούκι θησαυρού"],
        "explanation": "Στο τέλος κάθε κανονικής πίστας του Super Mario Bros., ο Mario πηδάει στον ιστό της σημαίας του κάστρου· όσο πιο ψηλά πιάσει τον ιστό, τόσο περισσότερους πόντους κερδίζει.",
        "funFacts": [
            "Αν ο Mario πιάσει την κορυφή του ιστού, κερδίζει 5.000 πόντους και ακούγονται πυροτεχνήματα.",
            "Τα πυροτεχνήματα ενεργοποιούνται αν το τελευταίο ψηφίο του χρονομέτρου είναι 1, 3 ή 6 τη στιγμή που αγγίζει τον ιστό."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Bros.",
        "tags": ["gaming", "mario", "nintendo", "nes", "platformer"]
    },
    {
        "id": "gaming_easy_263",
        "text": "Ποιο είναι το όνομα του μικρού πιθήκου με το κόκκινο καπέλο και το μπλουζάκι με το αστέρι που συνοδεύει τον Donkey Kong στο 'Donkey Kong Country';",
        "correct": "Diddy Kong",
        "distractors": ["Funky Kong", "Cranky Kong", "Dixie Kong"],
        "explanation": "Ο Diddy Kong είναι ο ανιψιός και πιστός συνεργάτης του Donkey Kong, γνωστός για την ευκινησία του και τα ταχύτερα άλματά του.",
        "funFacts": [
            "Το Donkey Kong Country αναπτύχθηκε από τη βρετανική εταιρεία Rare και εντυπωσίασε τη βιομηχανία το 1994 με τα προσχεδιασμένα 3D γραφικά του (pre-rendered CGI).",
            "Ο Cranky Kong, ο ηλικιωμένος γορίλας με το μπαστούνι, είναι σύμφωνα με το lore ο αρχικός Donkey Kong του arcade του 1981."
        ],
        "source": "https://en.wikipedia.org/wiki/Diddy_Kong",
        "tags": ["gaming", "donkey_kong", "rare", "nintendo", "snes"]
    },
    {
        "id": "gaming_easy_264",
        "text": "Ποιο από τα παρακάτω είναι το αρχικό Pokémon τύπου φωτιάς (Fire starter) στην πρώτη γενιά (Red/Blue);",
        "correct": "Charmander",
        "distractors": ["Bulbasaur", "Squirtle", "Pikachu"],
        "explanation": "Στα Pokémon Red & Blue, ο καθηγητής Oak δίνει στον παίκτη την επιλογή ανάμεσα στον Bulbasaur (Grass), τον Squirtle (Water) και τον Charmander (Fire).",
        "funFacts": [
            "Ο Charmander έχει μια φλόγα στην άκρη της ουράς του, η οποία αν σβήσει εντελώς, το Pokémon πεθαίνει.",
            "Η τελική του εξέλιξη είναι ο Charizard, ένα από τα πιο δημοφιλή πλάσματα σε όλη την ιστορία του franchise."
        ],
        "source": "https://en.wikipedia.org/wiki/Charmander",
        "tags": ["gaming", "pokemon", "game_boy", "nintendo", "charmander"]
    },
    {
        "id": "gaming_easy_265",
        "text": "Ποιο είναι το θρυλικό μαγικό σπαθί που κρατάει ο Link στη σειρά παιχνιδιών 'The Legend of Zelda';",
        "correct": "Master Sword",
        "distractors": ["Buster Sword", "Soul Edge", "Excalibur"],
        "explanation": "Το Master Sword (γνωστό και ως Blade of Evil's Bane) είναι το ιερό σπαθί που μπορεί να νικήσει το κακό και τον Ganon, συχνά τοποθετημένο σε ένα βάθρο στο Lost Woods ή τον Temple of Time.",
        "funFacts": [
            "Το Master Sword πρωτοεμφανίστηκε στο 'The Legend of Zelda: A Link to the Past' (1991) για το Super Nintendo.",
            "Στο Skyward Sword αποκαλύπτεται ότι μέσα στο σπαθί κατοικεί το πνεύμα Fi, που δημιουργήθηκε από τη θεά Hylia."
        ],
        "source": "https://en.wikipedia.org/wiki/Master_Sword",
        "tags": ["gaming", "zelda", "nintendo", "master_sword", "link"]
    },
    {
        "id": "gaming_easy_266",
        "text": "Στη σειρά αγώνων ταχύτητας 'Mario Kart', ποιο διαβόητο αντικείμενο με φτερά στοχεύει αυτόματα και ανατινάζει τον παίκτη που βρίσκεται στην 1η θέση;",
        "correct": "Μπλε καβούκι (Spiny Shell / Blue Shell)",
        "distractors": ["Κόκκινο καβούκι", "Πράσινο καβούκι", "Χρυσό μανιτάρι"],
        "explanation": "Το μπλε αγκαθωτό καβούκι με φτερά (Blue Shell) πετάει πάνω από την πίστα και εκρήγνυται πάνω στον πρωτοπόρο του αγώνα, ανατρέποντας την κατάταξη.",
        "funFacts": [
            "Το μπλε καβούκι πρωτοεμφανίστηκε στο Mario Kart 64 το 1996 για να αποτρέψει το να ξεφεύγει πολύ μπροστά ο πρώτος παίκτης.",
            "Στο Mario Kart 8, ο παίκτης στην πρώτη θέση μπορεί να καταστρέψει το μπλε καβούκι αν χρησιμοποιήσει την Κόρνα (Super Horn)."
        ],
        "source": "https://en.wikipedia.org/wiki/Blue_shell",
        "tags": ["gaming", "mario_kart", "nintendo", "blue_shell"]
    },
    {
        "id": "gaming_easy_267",
        "text": "Ποια είναι τα χαρακτηριστικά δίδυμα όπλα με αλυσίδες δεμένες στους πήχεις του Kratos στα κλασικά παιχνίδια 'God of War';",
        "correct": "Blades of Chaos",
        "distractors": ["Leviathan Axe", "Blade of Olympus", "Spear of Sparta"],
        "explanation": "Τα Blades of Chaos σφυρηλατήθηκαν στα βάθη του Κάτω Κόσμου από τον Άρη και κάηκαν πάνω στα χέρια του Kratos ως σύμβολο της υποταγής του στον Θεό του Πολέμου.",
        "funFacts": [
            "Οι αλυσίδες των λεπίδων ήταν καυτές και έλιωσαν τη σάρκα των καρπών του Kratos όταν τις δέχτηκε.",
            "Στο God of War (2018), ο Kratos αναγκάζεται να ξεθάψει ξανά τις παλιές λεπίδες του από το πάτωμα του σπιτιού του για να σώσει τον γιο του στο Helheim."
        ],
        "source": "https://en.wikipedia.org/wiki/Kratos_(God_of_War)",
        "tags": ["gaming", "god_of_war", "playstation", "kratos", "weapons"]
    },
    {
        "id": "gaming_easy_268",
        "text": "Στο 'Resident Evil 2' (1998), σε ποιο εμβληματικό κτίριο περνάει το μεγαλύτερο μέρος της περιπέτειάς του ο Leon S. Kennedy;",
        "correct": "Στο Αστυνομικό Τμήμα της Raccoon City (R.P.D.)",
        "distractors": ["Στο Γενικό Νοσοκομείο", "Στο Δημαρχείο της Πόλης", "Στον Σιδηροδρομικό Σταθμό"],
        "explanation": "Ο Leon Kennedy φτάνει στη Raccoon City για την πρώτη μέρα του ως αστυνομικός και καταφεύγει στο κεντρικό αστυνομικό τμήμα (R.P.D.), το οποίο ήταν παλιό μουσείο τέχνης.",
        "funFacts": [
            "Το αστυνομικό τμήμα ήταν σχεδιασμένο ως πρώην μουσείο τέχνης, εξηγώντας τους περίτεχνους γρίφους, τα αγάλματα και τις ειδικές κλειδαριές.",
            "Η συμπρωταγωνίστρια του παιχνιδιού Claire Redfield φτάνει στην πόλη αναζητώντας τον αδελφό της, Chris Redfield."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_2",
        "tags": ["gaming", "resident_evil", "capcom", "survival_horror", "leon_kennedy"]
    },
    {
        "id": "gaming_easy_269",
        "text": "Πώς ονομάζονται τα γεωμετρικά σχήματα που αποτελούνται από τέσσερα συνδεδεμένα τετράγωνα στο παιχνίδι 'Tetris';",
        "correct": "Τετρόμινο (Tetrominoes)",
        "distractors": ["Πεντόμινο", "Πολύγωνα", "Ντόμινο"],
        "explanation": "Κάθε κομμάτι στο Tetris ονομάζεται τετρόμινο (tetromino) και υπάρχουν ακριβώς 7 δυνατοί συνδυασμοί σχημάτων: I, J, L, O, S, T και Z.",
        "funFacts": [
            "Το τετρόμινο σε σχήμα ευθείας γραμμής (I-piece) είναι το μοναδικό κομμάτι που μπορεί να σβήσει τέσσερις σειρές ταυτόχρονα, πετυχαίνοντας ένα 'Tetris'.",
            "Η εταιρεία The Tetris Company τυποποίησε επίσημα τα χρώματα των 7 κομματιών το 2001."
        ],
        "source": "https://en.wikipedia.org/wiki/Tetromino",
        "tags": ["gaming", "tetris", "puzzle", "geometry"]
    },
    {
        "id": "gaming_easy_270",
        "text": "Στο σύμπαν του 'Half-Life', ποια μικρά παρασιτικά εξωγήινα πλάσματα πηδούν και γαντζώνονται στα κεφάλια ανθρώπων μετατρέποντάς τους σε ζόμπι;",
        "correct": "Headcrabs",
        "distractors": ["Facehuggers", "Metroids", "Antlions"],
        "explanation": "Τα Headcrabs προέρχονται από τη συνοριακή διάσταση Xen και προσκολλώνται στο κρανίο του θύματος, ελέγχοντας το νευρικό του σύστημα και μεταλλάσσοντάς το σε ζόμπι.",
        "funFacts": [
            "Στο Half-Life 2, ο επιστήμονας Dr. Isaac Kleiner έχει ένα εξημερωμένο και αποστειρωμένο headcrab ως κατοικίδιο που ονομάζεται Lamarr.",
            "Αν αντιστραφούν οι κραυγές των ζόμπι στο Half-Life 2, ακούγονται απελπισμένες ανθρώπινες κραυγές για βοήθεια."
        ],
        "source": "https://en.wikipedia.org/wiki/Headcrab",
        "tags": ["gaming", "half_life", "valve", "monsters", "fps"]
    },
    {
        "id": "gaming_easy_271",
        "text": "Ποια καινοτομία στο χειριστήριο του Nintendo 64 (1996) καθιέρωσε τον ακριβή έλεγχο κίνησης 360 μοιρών στα τρισδιάστατα βιντεοπαιχνίδια;",
        "correct": "Ο αναλογικός μοχλός (Analog Control Stick)",
        "distractors": ["Η οθόνη αφής", "Ο σταυρός κατεύθυνσης (D-Pad)", "Τα πλήκτρα αφής"],
        "explanation": "Το Nintendo 64 εισήγαγε τον κεντρικό αναλογικό μοχλό, ο οποίος επέτρεπε στον παίκτη να κινεί τον Mario στο Super Mario 64 με πλήρη ευελιξία και μεταβαλλόμενη ταχύτητα.",
        "funFacts": [
            "Λόγω του μίνι παιχνιδιού στο Mario Party όπου οι παίκτες περιστρέφανε γρήγορα τον μοχλό με την παλάμη, η Nintendo πρόσφερε ειδικά προστατευτικά γάντια.",
            "Το χειριστήριο είχε επίσης υποδοχή για το Rumble Pak, που εισήγαγε την ανάδραση δόνησης στις οικιακές κονσόλες."
        ],
        "source": "https://en.wikipedia.org/wiki/Nintendo_64_controller",
        "tags": ["gaming", "nintendo", "n64", "hardware", "controller"]
    },
    {
        "id": "gaming_easy_272",
        "text": "Ποιος είναι ο κόκκινος χαρακτήρας-έχιδνα με τις αιχμηρές γροθιές και φύλακας του Master Emerald στη σειρά 'Sonic the Hedgehog';",
        "correct": "Knuckles the Echidna",
        "distractors": ["Shadow the Hedgehog", "Vector the Crocodile", "Espio the Chameleon"],
        "explanation": "Ο Knuckles πρωτοεμφανίστηκε ως αντίπαλος στο Sonic the Hedgehog 3 (1994) και μπορεί να σκαρφαλώνει σε τοίχους και να γλιστράει στον αέρα.",
        "funFacts": [
            "Ο Knuckles ζει στο αιωρούμενο νησί Angel Island και προστατεύει το πανίσχυρο Master Emerald.",
            "Αρχικά παραπλανήθηκε από τον Dr. Robotnik πιστεύοντας ότι ο Sonic και ο Tails ήθελαν να κλέψουν το σμαράγδι."
        ],
        "source": "https://en.wikipedia.org/wiki/Knuckles_the_Echidna",
        "tags": ["gaming", "sonic", "sega", "knuckles", "characters"]
    },
    {
        "id": "gaming_easy_273",
        "text": "Ποιος είναι ο πρωταγωνιστής του 'Grand Theft Auto: San Andreas' (2004) που επιστρέφει στη γειτονιά του Grove Street μετά τον θάνατο της μητέρας του;",
        "correct": "Carl 'CJ' Johnson",
        "distractors": ["Tommy Vercetti", "Claude Speed", "Niko Bellic"],
        "explanation": "Ο CJ επιστρέφει στο Los Santos το 1992 και επανασυνδέεται με τη συμμορία Grove Street Families μαζί με τον αδελφό του Sweet και τους Big Smoke και Ryder.",
        "funFacts": [
            "Η ατάκα 'Ah shit, here we go again' που λέει ο CJ στην αρχή του παιχνιδιού έγινε ένα από τα πιο διάσημα ιντερνετικά memes.",
            "Το GTA: San Andreas εισήγαγε μηχανισμούς RPG, επιτρέποντας στον παίκτη να αλλάζει το σωματικό βάρος και τη μυϊκή μάζα του CJ μέσω γυμναστικής και φαγητού."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas",
        "tags": ["gaming", "gta", "rockstar", "san_andreas", "cj"]
    },
    {
        "id": "gaming_easy_274",
        "text": "Ποιος είναι ο παράνομος καουμπόι και κεντρικός πρωταγωνιστής του ιστορικού γουέστερν 'Red Dead Redemption' (2010) της Rockstar Games;",
        "correct": "John Marston",
        "distractors": ["Arthur Morgan", "Dutch van der Linde", "Micah Bell"],
        "explanation": "Ο πρώην παράνομος John Marston εξαναγκάζεται από ομοσπονδιακούς πράκτορες να κυνηγήσει τα παλιά μέλη της συμμορίας του για να σώσει την οικογένειά του.",
        "funFacts": [
            "Στο prequel 'Red Dead Redemption 2' (2018), ο κεντρικός χαρακτήρας είναι ο Arthur Morgan, ενώ ο Marston εμφανίζεται ως βασικό μέλος της συμμορίας.",
            "Ο ειδικός μηχανισμός στόχευσης σε αργή κίνηση στα παιχνίδια Red Dead ονομάζεται 'Dead Eye'."
        ],
        "source": "https://en.wikipedia.org/wiki/Red_Dead_Redemption",
        "tags": ["gaming", "red_dead_redemption", "rockstar", "western", "action"]
    },
    {
        "id": "gaming_easy_275",
        "text": "Στη σειρά 'Dark Souls' της FromSoftware, σε ποιο ασφαλές σημείο ανάπαυσης κάθονται οι παίκτες για να γεμίσουν ζωή και φιαλίδια Estus;",
        "correct": "Στο Bonfire (Φωτιά)",
        "distractors": ["Στον Βωμό (Altar)", "Στο Συντριβάνι", "Στη Σκηνή"],
        "explanation": "Τα bonfires είναι τα σημεία ανάπαυσης και respawn στο Dark Souls. Όταν ο παίκτης ξεκουράζεται σε αυτά, γεμίζουν τα Estus Flasks αλλά ανασταίνονται όλοι οι απλοί εχθροί στον κόσμο.",
        "funFacts": [
            "Το σύμβολο του bonfire με το σπαθί καρφωμένο μέσα στις στάχτες αποτελεί το πιο αναγνωρίσιμο σήμα της σειράς Soulsborne.",
            "Η περίφημη φράση 'Praise the Sun!' προέρχεται από τον ιππότη Solaire of Astora."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "fromsoftware", "action_rpg", "bonfire"]
    },
    {
        "id": "gaming_easy_276",
        "text": "Ποια είναι τα δύο χρώματα των πυλών που μπορεί να ανοίξει η συσκευή Portal Gun στο παιχνίδι 'Portal' της Valve;",
        "correct": "Μπλε και πορτοκαλί",
        "distractors": ["Κόκκινο και πράσινο", "Κίτρινο και μοβ", "Μαύρο και άσπρο"],
        "explanation": "Το Aperture Science Handheld Portal Device ανοίγει δύο συνδεδεμένες χωρικές πύλες: μία μπλε και μία πορτοκαλί, επιτρέποντας άμεση τηλεμεταφορά μεταξύ τους.",
        "funFacts": [
            "Ο βασικός νόμος διατήρησης της ορμής στο Portal συνοψίζεται στη φράση: 'Momentum, a function of mass and velocity, is conserved between portals'.",
            "Το Companion Cube, ένα διακοσμητικό κιβώτιο με καρδούλες, έγινε ένα από τα πιο αγαπημένα αντικείμενα των φίλων του παιχνιδιού."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_(video_game)",
        "tags": ["gaming", "portal", "valve", "puzzle", "physics"]
    },
    {
        "id": "gaming_easy_277",
        "text": "Στο παιχνίδι 'Minecraft', ποια καυτή, επικίνδυνη υπόγεια διάσταση γεμάτη λάβα επισκέπτεται ο παίκτης φτιάχνοντας πύλη από οψιδιανό (obsidian);",
        "correct": "The Nether (Κάτω Κόσμος)",
        "distractors": ["The End", "The Aether", "The Abyss"],
        "explanation": "Το Nether είναι μια διαβολική διάσταση γεμάτη λίμνες λάβας, Blazes, Ghasts και Piglins, απαραίτητη για τη συλλογή υλικών πριν το ταξίδι στο The End.",
        "funFacts": [
            "Αν προσπαθήσεις να κοιμηθείς σε κρεβάτι μέσα στο Nether, το κρεβάτι εκρήγνυται ακαριαία με τεράστια ισχύ.",
            "Ένα βήμα στο Nether ισοδυναμεί με απόσταση 8 μπλοκ στον κανονικό κόσμο (Overworld), χρησιμεύοντας για γρήγορα ταξίδια."
        ],
        "source": "https://en.wikipedia.org/wiki/Minecraft",
        "tags": ["gaming", "minecraft", "mojang", "nether"]
    },
    {
        "id": "gaming_easy_278",
        "text": "Ποια είναι η διάσημη ανοδική γροθιά-δράκος που εκτελούν ο Ryu και ο Ken στη σειρά 'Street Fighter';",
        "correct": "Shoryuken (Dragon Punch)",
        "distractors": ["Hadoken", "Tatsumaki Senpukyaku", "Sonic Boom"],
        "explanation": "Το Shoryuken είναι η απόλυτη αντιαεροπορική κίνηση των Ryu και Ken, όπου ο μαχητής εκτινάσσεται στον αέρα με μια πανίσχυρη γροθιά.",
        "funFacts": [
            "Η λέξη Shoryuken μεταφράζεται στα ιαπωνικά ως 'Γροθιά του Ανερχόμενου Δράκου'.",
            "Μια εσφαλμένη μετάφραση της νικητήριας ατάκας του Ryu στο Street Fighter II ('You must defeat Sheng Long to stand a chance') δημιούργησε έναν από τους διασημότερους αστικούς μύθους στα video games."
        ],
        "source": "https://en.wikipedia.org/wiki/Street_Fighter",
        "tags": ["gaming", "street_fighter", "capcom", "fighting", "shoryuken"]
    },
    {
        "id": "gaming_easy_279",
        "text": "Πόσα χρωματιστά πλήκτρα (frets) υπήρχαν στο λαιμό του πλαστικού χειριστηρίου-κιθάρας στα κλασικά παιχνίδια 'Guitar Hero';",
        "correct": "5",
        "distractors": ["3", "4", "6"],
        "explanation": "Το χειριστήριο του Guitar Hero είχε πέντε κουμπιά στο μπράτσο (πράσινο, κόκκινο, κίτρινο, μπλε και πορτοκαλί) και έναν μοχλό χτυπήματος (strum bar).",
        "funFacts": [
            "Η πρώτη έκδοση του Guitar Hero (2005) αναπτύχθηκε από την Harmonix και κυκλοφόρησε από τη RedOctane για το PlayStation 2.",
            "Όταν ο παίκτης πετύχαινε μια σειρά από φωτεινές νότες, γέμιζε το 'Star Power' το οποίο ενεργοποιούνταν σηκώνοντας την κιθάρα κάθετα."
        ],
        "source": "https://en.wikipedia.org/wiki/Guitar_Hero",
        "tags": ["gaming", "guitar_hero", "music", "harmonix", "activision"]
    },
    {
        "id": "gaming_easy_280",
        "text": "Ποια εταιρεία είναι η δημιουργός και εκδότρια της επιτυχημένης σειράς χορευτικών παιχνιδιών 'Just Dance';",
        "correct": "Ubisoft",
        "distractors": ["Electronic Arts", "Konami", "Activision"],
        "explanation": "Το Just Dance κυκλοφόρησε για πρώτη φορά από την Ubisoft το 2009 στο Nintendo Wii και εξελίχθηκε σε ετήσιο παγκόσμιο franchise.",
        "funFacts": [
            "Το όνομα του παιχνιδιού είναι εμπνευσμένο από το ομώνυμο τραγούδι επιτυχίας της Lady Gaga.",
            "Είναι ένα από τα ελάχιστα franchises που συνέχισε να κυκλοφορεί νέες εκδόσεις για την αρχική κονσόλα Nintendo Wii μέχρι και το 2020."
        ],
        "source": "https://en.wikipedia.org/wiki/Just_Dance_(video_game_series)",
        "tags": ["gaming", "just_dance", "ubisoft", "party_game"]
    },
    {
        "id": "gaming_easy_281",
        "text": "Ποιο παιχνίδι αθλημάτων περιλαμβανόταν δωρεάν στη συσκευασία της κονσόλας Nintendo Wii και παρουσίαζε τα αθλήματα τένις, μπόουλινγκ και γκολφ;",
        "correct": "Wii Sports",
        "distractors": ["Wii Fit", "Wii Play", "Mario Tennis"],
        "explanation": "Το Wii Sports (2006) επέδειξε τις δυνατότητες αισθητήρων κίνησης του Wii Remote και έγινε ένα από τα παιχνίδια με τις μεγαλύτερες πωλήσεις στην ιστορία.",
        "funFacts": [
            "Χάρη στη συμπερίληψή του με την κονσόλα, ξεπέρασε τα 82 εκατομμύρια αντίτυπα.",
            "Έγινε δημοφιλές σε οίκους ευγηρίας και νοσοκομεία ως μέσο ήπιας άσκησης και φυσικοθεραπείας για ηλικιωμένους."
        ],
        "source": "https://en.wikipedia.org/wiki/Wii_Sports",
        "tags": ["gaming", "wii_sports", "nintendo", "wii", "sports"]
    },
    {
        "id": "gaming_easy_282",
        "text": "Ποιο είναι το αγαπημένο εξωτικό φρούτο που συλλέγει ο Crash Bandicoot στις πίστες των παιχνιδιών του;",
        "correct": "Wumpa Fruit (Φρούτο Γουάμπα)",
        "distractors": ["Μπανάνα", "Μάνγκο", "Καρύδα"],
        "explanation": "Ο Crash μαζεύει φρούτα Wumpa (που μοιάζουν με συνδυασμό μήλου και ροδάκινου)· συλλέγοντας 100 από αυτά κερδίζει μία επιπλέον ζωή.",
        "funFacts": [
            "Πολλοί παίκτες νόμιζαν λανθασμένα ότι τα φρούτα Wumpa ήταν μήλα λόγω του κόκκινου-πορτοκαλί χρώματός τους.",
            "Στο Crash Team Racing, αν μαζέψεις 10 φρούτα Wumpa, τα όπλα και το καρτ σου γίνονται σημαντικά πιο ισχυρά ('Juiced up')."
        ],
        "source": "https://en.wikipedia.org/wiki/Crash_Bandicoot",
        "tags": ["gaming", "crash_bandicoot", "playstation", "naughty_dog", "items"]
    },
    {
        "id": "gaming_easy_283",
        "text": "Στη σειρά 'Halo', πώς ονομάζεται η εχθρική θεοκρατική συμμαχία εξωγήινων φυλών που πολεμά την ανθρωπότητα;",
        "correct": "The Covenant (Η Διαθήκη)",
        "distractors": ["The Flood", "The Banished", "The Reapers"],
        "explanation": "Το Covenant είναι μια θεοκρατική στρατιωτική συμμαχία εξωγήινων (Grunts, Elites, Jackals, Brutes) που λατρεύει τους αρχαίους Forerunners και τα δαχτυλίδια Halo.",
        "funFacts": [
            "Τα μέλη του Covenant πιστεύουν ότι η ενεργοποίηση των δαχτυλιδιών Halo θα οδηγήσει στο 'Μεγάλο Ταξίδι' (The Great Journey), αγνοώντας ότι στην πραγματικότητα εξοντώνει όλη τη συνειδητή ζωή στο γαλαξία.",
            "Ο επίλεκτος πολεμιστής Elite που αργότερα συμμαχεί με τον Master Chief είναι ο Arbiter (Thel 'Vadam)."
        ],
        "source": "https://en.wikipedia.org/wiki/Covenant_(Halo)",
        "tags": ["gaming", "halo", "xbox", "fps", "lore"]
    },
    {
        "id": "gaming_easy_284",
        "text": "Ποιο είναι το όνομα του ήρωα χωρίς χέρια και πόδια, που έχει μόνο κεφάλι, κορμό, παλάμες και παπούτσια, δημιουργία του Michel Ancel για την Ubisoft;",
        "correct": "Rayman",
        "distractors": ["Glover", "Earthworm Jim", "Plok"],
        "explanation": "Ο Rayman δημιουργήθηκε το 1995 και ο ιδιαίτερος σχεδιασμός του χωρίς άκρα επιλέχθηκε αρχικά για τεχνικούς λόγους εξοικονόμησης επεξεργαστικής ισχύος στα animations.",
        "funFacts": [
            "Ο Rayman μπορεί να περιστρέφει τα μαλλιά του σαν έλικα για να αιωρείται στον αέρα (Helicopter hair).",
            "Από τον κόσμο του Rayman ξεπήδησαν αργότερα τα θεότρελα κουνέλια Rabbids."
        ],
        "source": "https://en.wikipedia.org/wiki/Rayman",
        "tags": ["gaming", "rayman", "ubisoft", "platformer", "characters"]
    },
    {
        "id": "gaming_easy_285",
        "text": "Ποιος είναι ο διάσημος πράκτορας ειδικών αποστολών και ειδικός στο stealth που πρωταγωνιστεί στη σειρά 'Metal Gear Solid';",
        "correct": "Solid Snake",
        "distractors": ["Sam Fisher", "Agent 47", "Gabriel Logan"],
        "explanation": "Ο Solid Snake (δημιουργία του Hideo Kojima) είναι ο θρυλικός στρατιώτης της μονάδας FOXHOUND που αναλαμβάνει μυστικές αποστολές αποτροπής πυρηνικών επιθέσεων.",
        "funFacts": [
            "Ο Snake χρησιμοποιεί συχνά ένα απλό χάρτινο κουτί (cardboard box) για να κρύβεται και να μετακινείται απαρατήρητος μπροστά από τους φρουρούς.",
            "Τη φωνή του Solid Snake στις αγγλικές εκδόσεις δάνεισε ο ηθοποιός και σεναριογράφος David Hayter."
        ],
        "source": "https://en.wikipedia.org/wiki/Solid_Snake",
        "tags": ["gaming", "metal_gear", "konami", "hideo_kojima", "stealth"]
    },
    {
        "id": "gaming_easy_286",
        "text": "Ποιο είναι το παραδοσιακό ιερό μαστίγιο που χρησιμοποιεί η οικογένεια Belmont για να πολεμήσει τον Δράκουλα στη σειρά 'Castlevania';",
        "correct": "Vampire Killer",
        "distractors": ["Morning Star", "Holy Cross", "Alucard Sword"],
        "explanation": "Το Vampire Killer είναι το αγιασμένο μαστίγιο της οικογένειας Belmont, φτιαγμένο από αλχημεία για να εξολοθρεύει βρικόλακες και πλάσματα του σκότους.",
        "funFacts": [
            "Το πρώτο Castlevania κυκλοφόρησε από την Konami το 1986 για το Famicom Disk System και το NES.",
            "Ο γιος του Δράκουλα που επαναστατεί ενάντια στον πατέρα του ονομάζεται Alucard (το όνομα Dracula γραμμένο ανάποδα)."
        ],
        "source": "https://en.wikipedia.org/wiki/Castlevania",
        "tags": ["gaming", "castlevania", "konami", "retro", "weapons"]
    },
    {
        "id": "gaming_easy_287",
        "text": "Στο παιχνίδι 'Counter-Strike' της Valve, ποιος είναι ο βασικός στόχος της ομάδας των Terrorists στους χάρτες 'de_' (π.χ. de_dust2);",
        "correct": "Να τοποθετήσουν και να πυροδοτήσουν τη βόμβα C4",
        "distractors": ["Να διασώσουν τους ομήρους", "Να καταλάβουν τη σημαία", "Να συνοδεύσουν το φορτίο"],
        "explanation": "Στους χάρτες απασφάλισης βόμβας (Bomb Defusal), οι Τρομοκράτες προσπαθούν να τοποθετήσουν το C4 στα σημεία A ή B, ενώ οι Αντιτρομοκράτες (CTs) προσπαθούν να τους εμποδίσουν ή να την εξουδετερώσουν.",
        "funFacts": [
            "Το Counter-Strike ξεκίνησε το 1999 ως δωρεάν τροποποίηση (mod) του Half-Life από τους Minh Le και Jess Cliffe.",
            "Ο χάρτης de_dust2 σχεδιάστηκε από τον David Johnston και είναι ένας από τους πιο πολυπαιγμένους multiplayer χάρτες στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Counter-Strike",
        "tags": ["gaming", "counter_strike", "valve", "fps", "esports"]
    },
    {
        "id": "gaming_easy_288",
        "text": "Στο παιχνίδι επιβίωσης 'Subnautica' (2018), σε ποιο περιβάλλον εξελίσσεται σχεδόν ολόκληρη η περιπέτεια του μοναδικού επιζώντα;",
        "correct": "Στους ωκεανούς ενός εξωγήινου υδάτινου πλανήτη",
        "distractors": ["Σε μια έρημο ενός κόκκινου πλανήτη", "Σε έναν παγωμένο διαστημικό σταθμό", "Στα βάθη μιας σκοτεινής σπηλιάς"],
        "explanation": "Ο παίκτης συντρίβεται με το διαστημόπλοιο Aurora στον υδάτινο πλανήτη 4546B και πρέπει να εξερευνήσει κοραλλιογενείς υφάλους και σκοτεινά βάθη για να επιβιώσει.",
        "funFacts": [
            "Το μεγαλύτερο υποβρύχιο σκάφος που μπορεί να κατασκευάσει ο παίκτης ονομάζεται Cyclops.",
            "Τα γιγάντια αρπακτικά Reaper Leviathans χρησιμοποιούν ηχοεντοπισμό για να εντοπίζουν τα θύματά τους στα θολά νερά."
        ],
        "source": "https://en.wikipedia.org/wiki/Subnautica",
        "tags": ["gaming", "subnautica", "survival", "indie"]
    },
    {
        "id": "gaming_easy_289",
        "text": "Ποιο είναι το χαρακτηριστικό κρυφό όπλο που φέρουν στον καρπό τους οι εκπαιδευμένοι δολοφόνοι στη σειρά 'Assassin's Creed';",
        "correct": "Η κρυφή λεπίδα (Hidden Blade)",
        "distractors": ["Το δηλητηριώδες βέλος", "Το μαχαίρι ρίψης", "Η μικρή βαλλίστρα"],
        "explanation": "Η κρυφή λεπίδα (Hidden Blade) είναι το σήμα κατατεθέν των Assassins, επιτρέποντας αθόρυβες εκτελέσεις από κοντινή απόσταση χωρίς να προκαλεί υποψίες.",
        "funFacts": [
            "Στα πρώτα χρόνια της Αδελφότητας, οι δολοφόνοι έκοβαν τον παράμεσο του χεριού τους για να επιτρέπουν την ομαλή έξοδο της λεπίδας και ως ένδειξη αφοσίωσης.",
            "Ο Leonardo da Vinci τροποποίησε τον μηχανισμό στο Assassin's Creed II ώστε ο Ezio Auditore να μην χρειάζεται να ακρωτηριάσει το δάχτυλό του."
        ],
        "source": "https://en.wikipedia.org/wiki/Assassin%27s_Creed",
        "tags": ["gaming", "assassins_creed", "ubisoft", "weapons"]
    },
    {
        "id": "gaming_easy_290",
        "text": "Στο παιχνίδι 'Pokémon', ποιος βασικός τύπος υπερτερεί έναντι του τύπου Φωτιάς (Fire);",
        "correct": "Νερό (Water)",
        "distractors": ["Χορτάρι (Grass)", "Έντομο (Bug)", "Πάγος (Ice)"],
        "explanation": "Στον θεμελιώδη μηχανισμό πέτρα-ψαλίδι-χαρτί του Pokémon, το Νερό σβήνει τη Φωτιά, η Φωτιά καίει το Χορτάρι και το Χορτάρι απορροφά το Νερό.",
        "funFacts": [
            "Στην 1η γενιά υπήρχαν 15 τύποι Pokémon, ενώ αργότερα προστέθηκαν οι τύποι Steel, Dark και Fairy.",
            "Ο τύπος Fairy προστέθηκε στην 6η γενιά (X/Y) κυρίως για να εξισορροπήσει την υπεροχή των ισχυρών δράκων (Dragon-type)."
        ],
        "source": "https://en.wikipedia.org/wiki/Gameplay_of_Pok%C3%A9mon",
        "tags": ["gaming", "pokemon", "mechanics", "nintendo"]
    },
    {
        "id": "gaming_easy_291",
        "text": "Στο 'Mario Kart', τι συμβαίνει στο καρτ ενός οδηγού όταν πατήσει πάνω σε μια πεταμένη φλούδα μπανάνας;",
        "correct": "Κάνει σβούρα (spin out) και χάνει ταχύτητα",
        "distractors": ["Ανατινάζεται ψηλά στον αέρα", "Συρρικνώνεται σε μέγεθος", "Παγώνει σε ένα κομμάτι πάγου"],
        "explanation": "Η μπανανόφλουδα είναι κλασικό αμυντικό αντικείμενο στο Mario Kart που κάνει τα αντίπαλα οχήματα να περιστρέφονται ανεξέλεγκτα και να χάνουν χρόνο.",
        "funFacts": [
            "Οι έμπειροι παίκτες κρατούν τη μπανάνα πίσω από το καρτ τους πατώντας παρατεταμένα το κουμπί για να μπλοκάρουν τα κόκκινα και πράσινα καβούκια.",
            "Στο Mario Kart: Double Dash!! του GameCube, ο Donkey Kong και ο Diddy Kong είχαν ως ειδικό αντικείμενο μια γιγάντια μπανανόφλουδα (Giant Banana)."
        ],
        "source": "https://en.wikipedia.org/wiki/Mario_Kart",
        "tags": ["gaming", "mario_kart", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_292",
        "text": "Ποιο ανεξάρτητο παιχνίδι δράσης του Studio MDHR (2017) έγινε διάσημο για το χειροποίητο εικαστικό του στυλ κινουμένων σχεδίων της δεκαετίας του 1930;",
        "correct": "Cuphead",
        "distractors": ["Bendy and the Ink Machine", "Hollow Knight", "Celeste"],
        "explanation": "Το Cuphead σχεδιάστηκε εξ ολοκλήρου με παραδοσιακή τεχνική animation στο χέρι, αντλώντας έμπνευση από τα πρώτα κινούμενα σχέδια των στούντιο Fleischer και Walt Disney.",
        "funFacts": [
            "Κάθε καρέ animation σχεδιάστηκε και μελανώθηκε στο χέρι σε χαρτί πριν ψηφιοποιηθεί.",
            "Το soundtrack του παιχνιδιού ηχογραφήθηκε ζωντανά από αυθεντική ορχήστρα τζαζ (big band jazz)."
        ],
        "source": "https://en.wikipedia.org/wiki/Cuphead",
        "tags": ["gaming", "cuphead", "indie", "art_style"]
    },
    {
        "id": "gaming_easy_293",
        "text": "Ποιος είναι ο κεντρικός ήρωας του 'Final Fantasy VII' (1997) με τα ξανθά καρφωτά μαλλιά και το τεράστιο σπαθί Buster Sword;",
        "correct": "Cloud Strife",
        "distractors": ["Squall Leonhart", "Tidus", "Zidane Tribal"],
        "explanation": "Ο Cloud Strife είναι πρώην μέλος της επίλεκτης ομάδας SOLDIER που εντάσσεται στην οικολογική αντιστασιακή οργάνωση AVALANCHE στην πόλη Midgar.",
        "funFacts": [
            "Το Buster Sword του Cloud κληροδοτήθηκε από τον φίλο και μέντορά του, Zack Fair.",
            "Το Final Fantasy VII στο PlayStation 1 απλωνόταν σε 3 οπτικούς δίσκους CD-ROM λόγω των πολυάριθμων κινηματογραφικών cutscenes."
        ],
        "source": "https://en.wikipedia.org/wiki/Cloud_Strife",
        "tags": ["gaming", "final_fantasy", "square_enix", "cloud_strife", "rpg"]
    },
    {
        "id": "gaming_easy_294",
        "text": "Ποιος είναι ο διαβόητος κακός του 'Final Fantasy VII' με τα μακριά ασημένια μαλλιά και το σπαθί Masamune;",
        "correct": "Sephiroth",
        "distractors": ["Kefka Palazzo", "Kuja", "Ultimecia"],
        "explanation": "Ο Sephiroth είναι ο απόλυτος κακός του Final Fantasy VII, γεννημένος από πειράματα με τα κύτταρα της εξωγήινης οντότητας Jenova.",
        "funFacts": [
            "Το μουσικό θέμα μάχης του Sephiroth, το 'One-Winged Angel' του Nobuo Uematsu, περιλαμβάνει επικούς λατινικούς χορωδιακούς στίχους.",
            "Η σκηνή όπου ο Sephiroth στέκεται μέσα στις φλόγες του καιόμενου χωριού Nibelheim είναι μια από τις πιο αναγνωρίσιμες εικόνες στο gaming."
        ],
        "source": "https://en.wikipedia.org/wiki/Sephiroth_(Final_Fantasy)",
        "tags": ["gaming", "final_fantasy", "square_enix", "sephiroth", "villains"]
    },
    {
        "id": "gaming_easy_295",
        "text": "Στο παιχνίδι 'Doom' (2016) και 'Doom Eternal', ποιο εργαλείο σώμα με σώμα χρησιμοποιεί ο Slayer για να κόψει δαίμονες στη μέση και να κερδίσει πυρομαχικά;",
        "correct": "Αλυσοπρίονο (Chainsaw)",
        "distractors": ["Τσεκούρι", "Σπαθί πλάσματος", "Βαριοπούλα"],
        "explanation": "Το αλυσοπρίονο είναι βασικός πυλώνας του κύκλου μάχης των σύγχρονων Doom: σκοτώνοντας έναν δαίμονα με αυτό, το τέρας εκρήγνυται σε πλήθος πυρομαχικών για όλα τα όπλα.",
        "funFacts": [
            "Το αλυσοπρίονο εμφανίστηκε για πρώτη φορά στο αρχικό Doom του 1993 με την αστεία περιγραφή 'Finders keepers!'.",
            "Στο Doom Eternal, το αλυσοπρίονο αναπληρώνει αυτόματα ένα απόθεμα καυσίμου με την πάροδο του χρόνου ώστε ο παίκτης να μην ξεμένει ποτέ οριστικά από σφαίρες."
        ],
        "source": "https://en.wikipedia.org/wiki/Doom_(2016_video_game)",
        "tags": ["gaming", "doom", "id_software", "fps", "weapons"]
    },
    {
        "id": "gaming_easy_296",
        "text": "Ποιες είναι οι τρεις μοναδικές φυλές που συγκρούονται στο ιστορικό παιχνίδι στρατηγικής 'StarCraft' (1998) της Blizzard;",
        "correct": "Terran, Zerg και Protoss",
        "distractors": ["Human, Orc και Undead", "Alliance, Horde και Burning Legion", "Nod, GDI και Scrin"],
        "explanation": "Το StarCraft έθεσε το πρότυπο της ασύμμετρης ισορροπίας στο RTS με τους ανθρώπους Terran, τα βιολογικά έντομα Zerg και τους προηγμένους εξωγήινους Protoss.",
        "funFacts": [
            "Ο όρος 'Zerg Rush' μπήκε στο λεξικό της πληροφορικής και της καθημερινότητας για να περιγράψει τη μαζική επίθεση με πάμφθηνες μονάδες.",
            "Το StarCraft έγινε εθνικό άθλημα στη Νότια Κορέα με επαγγελματικά τηλεοπτικά κανάλια και γεμάτα στάδια από θεατές."
        ],
        "source": "https://en.wikipedia.org/wiki/StarCraft_(video_game)",
        "tags": ["gaming", "starcraft", "blizzard", "rts", "esports"]
    },
    {
        "id": "gaming_easy_297",
        "text": "Στο 'The Witcher 3: Wild Hunt', πώς ονομάζει σταθερά ο Geralt το πιστό του άλογο που ιππεύει σε όλη την ήπειρο;",
        "correct": "Roach (Πλότκα)",
        "distractors": ["Shadowmere", "Epona", "Agro"],
        "explanation": "Ο Geralt ονομάζει όλα τα άλογά του 'Roach' (Płotka στα πολωνικά, που παραπέμπει σε μικρό ποταμίσιο ψάρι).",
        "funFacts": [
            "Στο The Witcher 3, οι παίκτες μπορούν να καλέσουν το άλογο σφυρίζοντας, αν και μερικές φορές λόγω bugs εμφανιζόταν πάνω στις στέγες σπιτιών.",
            "Η CD Projekt Red έκανε αυτοσαρκαστικό χιούμορ με το bug της στέγης σε κάρτες του Gwent και ειδικά βίντεο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
        "tags": ["gaming", "the_witcher", "cd_projekt_red", "geralt"]
    },
    {
        "id": "gaming_easy_298",
        "text": "Ποιος θρυλικός Ιάπωνας σχεδιαστής της Nintendo δημιούργησε μερικά από τα διασημότερα franchises όλων των εποχών, όπως Mario, Zelda και Donkey Kong;",
        "correct": "Shigeru Miyamoto",
        "distractors": ["Hideo Kojima", "Shinji Mikami", "Tetsuya Nomura"],
        "explanation": "Ο Shigeru Miyamoto εντάχθηκε στη Nintendo ως καλλιτέχνης το 1977 και θεωρείται από πολλούς ως ο 'πατέρας των σύγχρονων βιντεοπαιχνιδιών'.",
        "funFacts": [
            "Ο Miyamoto εμπνεύστηκε τον κόσμο του The Legend of Zelda από τις εξερευνήσεις που έκανε ως παιδί στα δάση και τις σπηλιές γύρω από το Κιότο.",
            "Του απαγορεύτηκε από τη διοίκηση της Nintendo να πηγαίνει στη δουλειά με το ποδήλατο για λόγους ασφαλείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Shigeru_Miyamoto",
        "tags": ["gaming", "nintendo", "miyamoto", "industry", "creators"]
    },
    {
        "id": "gaming_easy_299",
        "text": "Ποιος μαχητής νίντζα της σειράς 'Mortal Kombat' ελέγχει τον πάγο και παγώνει τους αντιπάλους του στη μάχη;",
        "correct": "Sub-Zero",
        "distractors": ["Scorpion", "Reptile", "Raiden"],
        "explanation": "Ο Sub-Zero είναι ο αρχι-αντίπαλος του Scorpion και ανήκει στη φυλή των Lin Kuei, χρησιμοποιώντας κρυοκινητικές δυνάμεις.",
        "funFacts": [
            "Το διαβόητο Fatality του Sub-Zero στο πρώτο παιχνίδι περιλάμβανε το ξερίζωμα του κρανίου και της σπονδυλικής στήλης του αντιπάλου.",
            "Ο αρχικός Sub-Zero (Bi-Han) σκοτώθηκε και μεταμορφώθηκε στον Noob Saibot, ενώ ο νεότερος αδελφός του Kuai Liang πήρε τον μανδύα του Sub-Zero."
        ],
        "source": "https://en.wikipedia.org/wiki/Sub-Zero_(Mortal_Kombat)",
        "tags": ["gaming", "mortal_kombat", "sub_zero", "fighting"]
    },
    {
        "id": "gaming_easy_300",
        "text": "Ποιο είναι το ανεξάρτητο RPG του 2015 από τον Toby Fox, όπου ο παίκτης μπορεί να ολοκληρώσει ολόκληρο το παιχνίδι χωρίς να σκοτώσει κανέναν εχθρό;",
        "correct": "Undertale",
        "distractors": ["Deltarune", "Omori", "EarthBound"],
        "explanation": "Στο Undertale, ο παίκτης μπορεί να διαλέξει το μονοπάτι του Ειρηνιστή (Pacifist Run), μιλώντας και κάνοντας παρέα με τα τέρατα αντί να πολεμά.",
        "funFacts": [
            "Ο Toby Fox δημιούργησε σχεδόν ολόκληρο το παιχνίδι μόνος του, συμπεριλαμβανομένου του πολυβραβευμένου soundtrack με το κομμάτι 'Megalovania'.",
            "Το παιχνίδι θυμάται τις επιλογές του παίκτη ακόμα και αν κάνει reset ή κλείσει το παράθυρο του υπολογιστή."
        ],
        "source": "https://en.wikipedia.org/wiki/Undertale",
        "tags": ["gaming", "undertale", "indie", "toby_fox", "rpg"]
    },
    {
        "id": "gaming_easy_301",
        "text": "Στο arcade παιχνίδι 'Pac-Man', τι τρώει ο Pac-Man στις γωνίες του λαβύρινθου ώστε τα φαντάσματα να γίνουν μπλε και ευάλωτα;",
        "correct": "Power Pellets (Ενισχυτικές κάψουλες)",
        "distractors": ["Κεράσια", "Φράουλες", "Κλειδιά"],
        "explanation": "Όταν ο Pac-Man καταναλώσει μία από τις τέσσερις Power Pellets στις γωνίες, τα φαντάσματα γίνονται σκούρα μπλε και προσπαθούν να διαφύγουν, επιτρέποντάς του να τα φάει για επιπλέον πόντους.",
        "funFacts": [
            "Το πρώτο φάντασμα που τρώγεται δίνει 200 πόντους, το δεύτερο 400, το τρίτο 800 και το τέταρτο 1.600 πόντους.",
            "Όταν ένα φάντασμα φαγωθεί, μένουν μόνο τα μάτια του, τα οποία επιστρέφουν τρέχοντας στο κεντρικό κλουβί για να αναγεννηθεί."
        ],
        "source": "https://en.wikipedia.org/wiki/Pac-Man",
        "tags": ["gaming", "pac_man", "namco", "arcade", "retro"]
    },
    {
        "id": "gaming_easy_302",
        "text": "Ποιο μαγικό μανιτάρι στο 'Super Mario Bros.' κάνει τον Mario να μεγαλώνει σε μέγεθος και να σπάει τούβλα;",
        "correct": "Super Mushroom (Κόκκινο Μανιτάρι)",
        "distractors": ["1-Up Mushroom", "Poison Mushroom", "Mini Mushroom"],
        "explanation": "Το κλασικό κόκκινο Super Mushroom μετατρέπει τον μικρό Mario σε Super Mario, επιτρέποντάς του να αντέξει ένα επιπλέον χτύπημα χωρίς να χάσει ζωή.",
        "funFacts": [
            "Το πράσινο μανιτάρι (1-Up Mushroom) χαρίζει μία επιπλέον ζωή στον παίκτη.",
            "Η έμπνευση για τα μαγικά μανιτάρια που αλλάζουν το μέγεθος του ήρωα προήλθε εν μέρει από την 'Αλίκη στη Χώρα των Θαυμάτων'."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Bros.",
        "tags": ["gaming", "mario", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_303",
        "text": "Ποιοι είναι οι τρεις βασικοί πόροι κατασκευών που συλλέγουν οι παίκτες στο 'Fortnite' σπάζοντας αντικείμενα με την αξίνα τους;",
        "correct": "Ξύλο, πέτρα και μέταλλο",
        "distractors": ["Ξύλο, χρυσός και διαμάντι", "Χώμα, σίδερο και γυαλί", "Πλαστικό, τούβλο και ατσάλι"],
        "explanation": "Στο Fortnite, οι παίκτες χρησιμοποιούν ξύλο (wood), πέτρα (stone/brick) και μέταλλο (metal) για να χτίσουν τοίχους, ράμπες, πατώματα και πυραμίδες κατά τη διάρκεια των μαχών.",
        "funFacts": [
            "Το μέταλλο έχει τη μεγαλύτερη αντοχή αλλά χρειάζεται τον περισσότερο χρόνο για να χτιστεί πλήρως.",
            "Το 2022, η Epic Games εισήγαγε μόνιμα τη λειτουργία 'Zero Build' που αφαίρεσε εντελώς το χτίσιμο, προσελκύοντας εκατομμύρια νέους παίκτες."
        ],
        "source": "https://en.wikipedia.org/wiki/Fortnite",
        "tags": ["gaming", "fortnite", "epic_games", "battle_royale"]
    },
    {
        "id": "gaming_easy_304",
        "text": "Ποιες είναι οι δύο αντίπαλες παρατάξεις στον κόσμο του MMORPG 'World of Warcraft' της Blizzard;",
        "correct": "Alliance (Συμμαχία) και Horde (Ορδή)",
        "distractors": ["Empire και Republic", "Templars και Assassins", "Sentinels και Scourge"],
        "explanation": "Στο World of Warcraft, οι παίκτες επιλέγουν ανάμεσα στη Συμμαχία (Humans, Night Elves, Dwarves κ.ά.) και την Ορδή (Orcs, Undead, Tauren κ.ά.).",
        "funFacts": [
            "Η κραυγή 'For the Horde!' ή 'For the Alliance!' αποτελεί κοινό σημείο αναγνώρισης μεταξύ των παικτών σε conventions.",
            "Το παιχνίδι έφτασε στο αποκορύφωμά του τους 12 εκατομμύρια ταυτόχρονους συνδρομητές κατά την επέκταση Wrath of the Lich King (2010)."
        ],
        "source": "https://en.wikipedia.org/wiki/World_of_Warcraft",
        "tags": ["gaming", "world_of_warcraft", "blizzard", "mmorpg"]
    },
    {
        "id": "gaming_easy_305",
        "text": "Ποιο επιτυχημένο battle royale shooter πρώτου προσώπου ανέπτυξε η Respawn Entertainment στο σύμπαν του Titanfall το 2019;",
        "correct": "Apex Legends",
        "distractors": ["Valorant", "PUBG", "Hyper Scape"],
        "explanation": "Το Apex Legends κυκλοφόρησε ξαφνικά χωρίς καμία προηγούμενη διαφήμιση τον Φεβρουάριο του 2019 και απέκτησε 25 εκατομμύρια παίκτες μέσα στην πρώτη εβδομάδα.",
        "funFacts": [
            "Εισήγαγε το σύστημα 'Ping', μια πρωτοποριακή μέθοδο μη-λεκτικής επικοινωνίας μεταξύ συμπαικτών που αντιγράφηκε από όλα τα άλλα παιχνίδια του είδους.",
            "Εισήγαγε επίσης τη δυνατότητα αναβίωσης εξοντωμένων συμπαικτών στα Respawn Beacons."
        ],
        "source": "https://en.wikipedia.org/wiki/Apex_Legends",
        "tags": ["gaming", "apex_legends", "respawn", "ea", "battle_royale"]
    },
    {
        "id": "gaming_easy_306",
        "text": "Ποιος είναι ο σκύλος μουσικός στο 'Animal Crossing' που κάθεται σε ένα σκαμπό με την ακουστική του κιθάρα και παίζει τραγούδια;",
        "correct": "K.K. Slider (Totakeke)",
        "distractors": ["Tom Nook", "Blathers", "Rover"],
        "explanation": "Ο K.K. Slider είναι ένας λευκός σκύλος ράτσας Jack Russell terrier που επισκέπτεται την πόλη ή το νησί για να δώσει συναυλίες και να χαρίσει δίσκους βινυλίου.",
        "funFacts": [
            "Ο χαρακτήρας είναι βασισμένος στον πραγματικό συνθέτη της μουσικής του παιχνιδιού, Kazumi Totaka (εξ ου και το ιαπωνικό όνομα Totakeke).",
            "Το μυστικό τραγούδι 'Totaka's Song' κρύβεται σχεδόν σε κάθε παιχνίδι της Nintendo στο οποίο εργάστηκε ο Totaka."
        ],
        "source": "https://en.wikipedia.org/wiki/K.K._Slider",
        "tags": ["gaming", "animal_crossing", "nintendo", "music"]
    },
    {
        "id": "gaming_easy_307",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή της κλασικής σειράς 'Uncharted' του PlayStation που ψάχνει χαμένους θησαυρούς όπως το El Dorado;",
        "correct": "Nathan Drake",
        "distractors": ["Victor Sullivan", "Sam Drake", "Rafe Adler"],
        "explanation": "Ο Nathan Drake είναι ένας γοητευτικός και πνευματώδης τυχοδιώκτης που ισχυρίζεται ότι είναι απόγονος του διάσημου Άγγλου εξερευνητή Sir Francis Drake.",
        "funFacts": [
            "Τον ρόλο του Nathan Drake ενσάρκωσε ο ηθοποιός Nolan North με performance capture και φωνή.",
            "Ο πιστός μέντορας και φίλος του ονομάζεται Victor 'Sully' Sullivan."
        ],
        "source": "https://en.wikipedia.org/wiki/Nathan_Drake_(character)",
        "tags": ["gaming", "uncharted", "playstation", "naughty_dog", "nathan_drake"]
    },
    {
        "id": "gaming_easy_308",
        "text": "Ποιο διάσημο παιχνίδι σκοποβολής της Blizzard διαθέτει έναν γορίλα-γενετιστή από τη σεληνιακή αποικία που ονομάζεται Winston;",
        "correct": "Overwatch",
        "distractors": ["StarCraft", "Destiny", "Team Fortress 2"],
        "explanation": "Ο Winston είναι ένας εξαιρετικά ευφυής, γενετικά τροποποιημένος γορίλας και επιστήμονας που κρατάει ένα Tesla Cannon και φοράει γυαλιά όρασης.",
        "funFacts": [
            "Το αγαπημένο σνακ του Winston είναι το φυστικοβούτυρο (peanut butter).",
            "Πήρε το όνομά του από τον ανθρώπινο μέντορά του στη Σελήνη, Dr. Harold Winston."
        ],
        "source": "https://en.wikipedia.org/wiki/Winston_(Overwatch)",
        "tags": ["gaming", "overwatch", "blizzard", "characters"]
    },
    {
        "id": "gaming_easy_309",
        "text": "Ποιο δημοφιλές παιχνίδι για κινητά τηλέφωνα από την Epic Games / Chair Entertainment (2010) εστίαζε σε μάχες με σπαθί μέσω κινήσεων αφής (swipes);",
        "correct": "Infinity Blade",
        "distractors": ["Fruit Ninja", "Shadow Fight", "Temple Run"],
        "explanation": "Το Infinity Blade υπήρξε ορόσημο για τα γραφικά σε φορητές συσκευές iOS, χρησιμοποιώντας την Unreal Engine 3 με χειρισμό αφής για μπλοκαρίσματα και κοψίματα.",
        "funFacts": [
            "Ήταν το πρώτο παιχνίδι για κινητά που χρησιμοποίησε την ισχυρή μηχανή γραφικών Unreal Engine.",
            "Η πλοκή βασιζόταν σε έναν κύκλο διαδοχικών γενεών ηρώων (Bloodlines) που πολεμούσαν τον God King."
        ],
        "source": "https://en.wikipedia.org/wiki/Infinity_Blade",
        "tags": ["gaming", "mobile", "ios", "epic_games", "unreal_engine"]
    },
    {
        "id": "gaming_easy_310",
        "text": "Στο παιχνίδι 'The Last of Us' (2013) της Naughty Dog, ποιο είδος μύκητα προκαλεί την καταστροφική πανδημία που μεταλλάσσει τους ανθρώπους;",
        "correct": "Cordyceps (Κόρντισεπς)",
        "distractors": ["T-Virus", "Las Plagas", "Green Poison"],
        "explanation": "Η λοίμωξη εγκεφάλου Cordyceps (CBI) βασίζεται σε πραγματικό παρασιτικό μύκητα που μολύνει μυρμήγκια και έντομα στη φύση ελέγχοντας τον εγκέφαλό τους.",
        "funFacts": [
            "Οι πιο επικίνδυνοι τυφλοί μολυσμένοι στο παιχνίδι ονομάζονται Clickers επειδή χρησιμοποιούν κλικ για ηχοεντοπισμό.",
            "Η 14χρονη Ellie είναι το μοναδικό γνωστό άτομο με φυσική ανοσία στον μύκητα."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Last_of_Us",
        "tags": ["gaming", "the_last_of_us", "naughty_dog", "playstation", "story"]
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
    print(f"Loaded {len(questions)} questions for gaming_easy batch 2.")
    validate_and_append("gaming", "easy", 1, questions)

# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_easy_311",
        "text": "Ποιος είναι ο κύριος κακός της σειράς 'Sonic the Hedgehog', ένας τρελός επιστήμονας με τεράστιο μουστάκι που παγιδεύει ζωάκια σε ρομπότ;",
        "correct": "Doctor Ivo 'Eggman' Robotnik",
        "distractors": ["Doctor Neo Cortex", "Doctor Wily", "Doctor Bosconovitch"],
        "explanation": "Ο Dr. Robotnik (γνωστός στην Ιαπωνία ως Dr. Eggman λόγω του αυγοειδούς σχήματος του σώματός του) είναι ο αιώνιος εχθρός του Sonic.",
        "funFacts": [
            "Ο Dr. Eggman έχει IQ 300 και ονειρεύεται να φτιάξει τη δική του δυστοπική πόλη, την Eggmanland.",
            "Το όνομα Eggman ήταν το αρχικό ιαπωνικό όνομα του χαρακτήρα, ενώ στη Δύση είχε βαφτιστεί Robotnik μέχρι να ενοποιηθούν τα ονόματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Doctor_Eggman",
        "tags": ["gaming", "sonic", "sega", "eggman", "villains"]
    },
    {
        "id": "gaming_easy_312",
        "text": "Ποιος είναι ο κίτρινος αντίζηλος του Mario με το μοβ παντελόνι που λατρεύει το σκόρδο, το χρυσάφι και έχει μουστάκι σε σχήμα ζιγκ-ζαγκ;",
        "correct": "Wario",
        "distractors": ["Waluigi", "Bowser", "Kamek"],
        "explanation": "Ο Wario σχεδιάστηκε από τον Hiroji Kiyotake ως η κακόβουλη και πληθωρική αντίθεση του Mario, κάνοντας το ντεμπούτο του στο 'Super Mario Land 2' (1992).",
        "funFacts": [
            "Το όνομα Wario είναι συνδυασμός του ονόματος Mario και της ιαπωνικής λέξης 'warui' που σημαίνει 'κακός'.",
            "Ο Wario πρωταγωνιστεί στη δημοφιλή σειρά micro-games 'WarioWare' όπου οι παίκτες λύνουν αστραπιαία παζλ ελάχιστων δευτερολέπτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Wario",
        "tags": ["gaming", "mario", "wario", "nintendo", "characters"]
    },
    {
        "id": "gaming_easy_313",
        "text": "Ποιο είναι το αγαπημένο φαγητό του Donkey Kong που συλλέγουν οι παίκτες σε όλα τα παιχνίδια του για να κερδίσουν ζωές;",
        "correct": "Μπανάνες",
        "distractors": ["Καρύδες", "Μήλα", "Ανανάδες"],
        "explanation": "Οι μπανάνες είναι το κατεξοχήν έμβλημα και νόμισμα του Donkey Kong· συλλέγοντας 100 μπανάνες, ο παίκτης ανταμείβεται με μια επιπλέον ζωή.",
        "funFacts": [
            "Στο Donkey Kong Country, ολόκληρη η ιστορία ξεκινά επειδή οι Kremlings έκλεψαν τον τεράστιο θησαυρό με τις μπανάνες της οικογένειας Kong.",
            "Στο Donkey Kong 64, κάθε μέλος της οικογένειας Kong μαζεύει μπανάνες διαφορετικού χρώματος (π.χ. ο DK κίτρινες, ο Diddy κόκκινες)."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_Country",
        "tags": ["gaming", "donkey_kong", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_314",
        "text": "Από ποια ευρωπαϊκή χώρα κατάγεται η εταιρεία βιντεοπαιχνιδιών CD Projekt Red, δημιουργός των σειρών 'The Witcher' και 'Cyberpunk 2077';",
        "correct": "Πολωνία",
        "distractors": ["Σουηδία", "Γερμανία", "Τσεχία"],
        "explanation": "Η CD Projekt Red ιδρύθηκε στη Βαρσοβία της Πολωνίας το 2002 από τους Marcin Iwiński και Michał Kiciński.",
        "funFacts": [
            "Η εταιρεία ξεκίνησε τη δεκαετία του '90 εισάγοντας και μεταφράζοντας αμερικανικά PC games σε CD-ROM για την πολωνική αγορά.",
            "Η επιτυχία της σειράς The Witcher ήταν τόσο μεγάλη ώστε ο Πολωνός πρωθυπουργός δώρισε αντίτυπο του παιχνιδιού στον Πρόεδρο των ΗΠΑ Μπαράκ Ομπάμα."
        ],
        "source": "https://en.wikipedia.org/wiki/CD_Projekt",
        "tags": ["gaming", "cd_projekt_red", "industry", "poland"]
    },
    {
        "id": "gaming_easy_315",
        "text": "Ποιο κλασικό παιχνίδι προσομοίωσης πολεοδομίας και διαχείρισης πόλεων δημιούργησε ο Will Wright για τη Maxis το 1989;",
        "correct": "SimCity",
        "distractors": ["Cities: Skylines", "Civilization", "RollerCoaster Tycoon"],
        "explanation": "Το SimCity έβαλε τον παίκτη στον ρόλο του δημάρχου και πολεοδόμου, ορίζοντας οικιστικές, εμπορικές και βιομηχανικές ζώνες και αντιμετωπίζοντας φυσικές καταστροφές.",
        "funFacts": [
            "Ο Wright εμπνεύστηκε το SimCity όταν συνειδητοποίησε ότι διασκέδαζε περισσότερο σχεδιάζοντας χάρτες με τον level editor παρά παίζοντας το ίδιο το παιχνίδι ελικοπτέρου Raid on Bungeling Bay.",
            "Οι αρχικοί εκδότες απέρριψαν το SimCity επειδή 'δεν είχε ξεκάθαρο τρόπο να κερδίσεις ή να χάσεις'."
        ],
        "source": "https://en.wikipedia.org/wiki/SimCity",
        "tags": ["gaming", "simcity", "maxis", "simulation", "retro"]
    },
    {
        "id": "gaming_easy_316",
        "text": "Ποια είναι η μακροβιότερη σειρά αγώνων αυτοκινήτων της Electronic Arts, γνωστή για τις παράνομες κόντρες δρόμου και τις καταδιώξεις με την αστυνομία;",
        "correct": "Need for Speed",
        "distractors": ["Gran Turismo", "Forza Motorsport", "Burnout"],
        "explanation": "Το Need for Speed ξεκίνησε το 1994 και γνώρισε τεράστια επιτυχία με τίτλους όπως το Underground (2003) και το Most Wanted (2005).",
        "funFacts": [
            "Το Need for Speed: Underground επηρεάστηκε έντονα από την κουλτούρα του tuning και την ταινία 'The Fast and the Furious'.",
            "Η σειρά έχει πουλήσει πάνω από 150 εκατομμύρια αντίτυπα παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Need_for_Speed",
        "tags": ["gaming", "need_for_speed", "ea", "racing"]
    },
    {
        "id": "gaming_easy_317",
        "text": "Ποιος είναι ο στρατιωτικός τίτλος και το όνομα του προσαρμόσιμου πρωταγωνιστή στην τριλογία επιστημονικής φαντασίας 'Mass Effect';",
        "correct": "Commander Shepard",
        "distractors": ["Captain Price", "Master Chief", "Marcus Fenix"],
        "explanation": "Ο/Η Commander Shepard είναι ο πρώτος άνθρωπος Spectre της Citadel και κυβερνήτης του διαστημοπλοίου SSV Normandy που μάχεται ενάντια στους Reapers.",
        "funFacts": [
            "Ο παίκτης μπορεί να επιλέξει αν ο Shepard θα είναι άντρας ή γυναίκα, με τους θαυμαστές να λατρεύουν την ερμηνεία της Jennifer Hale ως 'FemShep'.",
            "Το σύστημα ηθικής του παιχνιδιού χωρίζεται σε πράξεις Paragon (ευγενής/ιδεαλιστής) και Renegade (αμείλικτος/πραγματιστής)."
        ],
        "source": "https://en.wikipedia.org/wiki/Commander_Shepard",
        "tags": ["gaming", "mass_effect", "bioware", "rpg", "sci_fi"]
    },
    {
        "id": "gaming_easy_318",
        "text": "Στο ατμοσφαιρικό shooter 'BioShock' (2007), πώς ονομάζεται η υποθαλάσσια δυστοπική πόλη που έχτισε ο Andrew Ryan;",
        "correct": "Rapture",
        "distractors": ["Columbia", "City 17", "Midgar"],
        "explanation": "Η Rapture χτίστηκε στον πυθμένα του Ατλαντικού Ωκεανού ως καταφύγιο καλλιτεχνών και επιστημόνων μακριά από κυβερνήσεις και θρησκείες, αλλά κατέρρευσε λόγω της κατάχρησης της ουσίας ADAM.",
        "funFacts": [
            "Οι μικρές κοπέλες που μαζεύουν ADAM ονομάζονται Little Sisters και προστατεύονται από τερατώδεις δύτες με τρυπάνια, τους Big Daddies.",
            "Η φράση 'Would you kindly' αποτελεί μια από τις διασημότερες ανατροπές (plot twists) στην ιστορία των σεναρίων βιντεοπαιχνιδιών."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock",
        "tags": ["gaming", "bioshock", "2k_games", "fps", "rapture"]
    },
    {
        "id": "gaming_easy_319",
        "text": "Στο 'BioShock Infinite' (2013), σε ποια ιπτάμενη πόλη ανάμεσα στα σύννεφα ταξιδεύει ο Booker DeWitt για να σώσει την Elizabeth;",
        "correct": "Columbia",
        "distractors": ["Rapture", "Olympus", "Skyloft"],
        "explanation": "Η Columbia είναι μια εντυπωσιακή πόλη που αιωρείται στους ουρανούς μέσω γιγάντιων μπαλονιών και κβαντικής αιώρησης, υπό την ηγεσία του θρησκευτικού ηγέτη Zachary Comstock.",
        "funFacts": [
            "Η Elizabeth διαθέτει τη μοναδική υπερφυσική ικανότητα να ανοίγει ρήγματα (tears) σε παράλληλες διαστάσεις και χρονικές περιόδους.",
            "Το γιγάντιο ρομποτικό πουλί που φυλάει την Elizabeth ονομάζεται Songbird."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock_Infinite",
        "tags": ["gaming", "bioshock", "columbia", "fps", "ken_levine"]
    },
    {
        "id": "gaming_easy_320",
        "text": "Ποια περίφημη φράση εμφανίζεται με μεγάλα κόκκινα γράμματα στην οθόνη κάθε φορά που ο παίκτης χάνει στη σειρά 'Dark Souls';",
        "correct": "YOU DIED",
        "distractors": ["GAME OVER", "DEFEAT", "MISSION FAILED"],
        "explanation": "Η επιγραφή 'YOU DIED' έχει γίνει το σήμα κατατεθέν της ασυμβίβαστης δυσκολίας και της φιλοσοφίας μάθησης μέσω δοκιμής και σφάλματος της FromSoftware.",
        "funFacts": [
            "Όταν ο παίκτης πεθαίνει στο Dark Souls, αφήνει πίσω του μια πράσινη κηλίδα αίματος (bloodstain) με όλες τις ψυχές που κουβαλούσε.",
            "Αν πεθάνει ξανά πριν προλάβει να ανακτήσει τις ψυχές του, αυτές χάνονται για πάντα."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "fromsoftware", "memes"]
    },
    {
        "id": "gaming_easy_321",
        "text": "Ποιο είναι το απαραίτητο σφαιρικό εργαλείο που χρησιμοποιούν οι εκπαιδευτές για να πιάνουν και να μεταφέρουν άγρια πλάσματα στο 'Pokémon';",
        "correct": "Poké Ball (Πόκεμπολ)",
        "distractors": ["Master Disc", "Capture Capsule", "Orb Ring"],
        "explanation": "Η Poké Ball είναι η βασική σφαίρα αιχμαλωσίας των Pokémon, χωρισμένη σε κόκκινο άνω ημισφαίριο και λευκό κάτω ημισφαίριο με κεντρικό κουμπί.",
        "funFacts": [
            "Η ισχυρότερη μπάλα στο παιχνίδι είναι η Master Ball, η οποία έχει ποσοστό επιτυχίας 100% και πιάνει οποιοδήποτε Pokémon χωρίς εξαίρεση.",
            "Υπάρχουν δεκάδες παραλλαγές Poké Balls, όπως η Ultra Ball, η Great Ball, η Net Ball και η Timer Ball."
        ],
        "source": "https://en.wikipedia.org/wiki/Pok%C3%A9mon",
        "tags": ["gaming", "pokemon", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_322",
        "text": "Στο 'Half-Life 2' (2004), ποιο καινοτόμο όπλο χειρισμού φυσικής επιτρέπει στον Gordon Freeman να σηκώνει και να εκτοξεύει βαριά αντικείμενα;",
        "correct": "Gravity Gun (Όπλο Βαρύτητας)",
        "distractors": ["Portal Gun", "Plasma Rifle", "Gauss Gun"],
        "explanation": "Το Zero Point Energy Field Manipulator (Gravity Gun) επιτρέπει στον παίκτη να αρπάζει βαρέλια, κιβώτια ή λεπίδες πριονιού και να τα εκσφενδονίζει εναντίον εχθρών.",
        "funFacts": [
            "Η χρήση του Gravity Gun αναδείκνυε τη μηχανή φυσικής Havok, η οποία αποτέλεσε τεχνολογικό άλμα για τη βιομηχανία το 2004.",
            "Στο τέλος του παιχνιδιού, το όπλο υπερφορτίζεται σε μπλε χρώμα και αποκτά τη δύναμη να εκτοξεύει απευθείας ανθρώπους εχθρούς Combine."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2",
        "tags": ["gaming", "half_life", "valve", "weapons", "physics"]
    },
    {
        "id": "gaming_easy_323",
        "text": "Σε ποια ιστορική δεκαετία και πόλη είναι βασισμένο το στιλ και η μουσική ατμόσφαιρα του 'Grand Theft Auto: Vice City' (2002);",
        "correct": "Δεκαετία του 1980 στο Μαϊάμι",
        "distractors": ["Δεκαετία του 1970 στη Νέα Υόρκη", "Δεκαετία του 1990 στο Λος Άντζελες", "Δεκαετία του 1960 στο Λονδίνο"],
        "explanation": "Το Vice City διαδραματίζεται το 1986 και αποτελεί φόρο τιμής στην ταινία 'Ο Σημαδεμένος' (Scarface) και τηλεοπτικές σειρές όπως το 'Miami Vice'.",
        "funFacts": [
            "Ο πρωταγωνιστής Tommy Vercetti φοράει ένα χαρακτηριστικό τιρκουάζ χαβανέζικο πουκάμισο με φοίνικες.",
            "Τη φωνή του Tommy Vercetti δάνεισε ο διάσημος ηθοποιός του Χόλιγουντ Ray Liotta."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City",
        "tags": ["gaming", "gta", "vice_city", "rockstar", "open_world"]
    },
    {
        "id": "gaming_easy_324",
        "text": "Ποιο αντικείμενο στο 'Super Mario Bros.' κάνει τον Mario να αναβοσβήνει με χρώματα και να είναι προσωρινά άτρωτος σε όλους τους εχθρούς;",
        "correct": "Super Star (Αστέρι)",
        "distractors": ["Fire Flower", "Super Leaf", "Mega Mushroom"],
        "explanation": "Το Super Star (ή Starman) χαρίζει στον Mario προσωρινή ατρωσία και αυξημένη ταχύτητα, καταστρέφοντας κάθε εχθρό με το απλό άγγιγμα.",
        "funFacts": [
            "Όταν ο Mario παίρνει το αστέρι, αλλάζει η μουσική της πίστας σε ένα ταχύρυθμο, κεφάτο μουσικό θέμα.",
            "Η ατρωσία δεν προστατεύει τον Mario από πτώση σε γκρεμό ή από εξάντληση του χρόνου της πίστας."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Bros.",
        "tags": ["gaming", "mario", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_325",
        "text": "Ποια είναι τα τέσσερα γεωμετρικά σύμβολα που βρίσκονται στα κύρια κουμπιά του επίσημου χειριστηρίου του PlayStation;",
        "correct": "Τρίγωνο, Κύκλος, Σταυρός (Χ) και Τετράγωνο",
        "distractors": ["Α, Β, Χ και Υ", "1, 2, 3 και 4", "Ρόμβος, Αστέρι, Κύκλος και Τρίγωνο"],
        "explanation": "Ο σχεδιαστής Teiyu Goto επέλεξε τα τέσσερα σύμβολα δίνοντας σε καθένα νόημα: το Τρίγωνο συμβολίζει οπτική γωνία/κατεύθυνση, το Τετράγωνο έγγραφο/χάρτη, ο Κύκλος 'ναι' και ο Σταυρός 'όχι'.",
        "funFacts": [
            "Στην Ιαπωνία, ο Κύκλος παραδοσιακά χρησιμοποιούνταν για επιβεβαίωση και το 'X' για ακύρωση, ενώ στη Δύση ίσχυε το αντίστροφο μέχρι το PS5.",
            "Με το PlayStation 5, η Sony καθιέρωσε παγκοσμίως το κουμπί 'X' ως το πλήκτρο επιβεβαίωσης."
        ],
        "source": "https://en.wikipedia.org/wiki/PlayStation_controller",
        "tags": ["gaming", "playstation", "sony", "hardware", "controller"]
    },
    {
        "id": "gaming_easy_326",
        "text": "Ποια είναι τα τέσσερα γράμματα που αντιστοιχούν στα βασικά κουμπιά των χειριστηρίων του Xbox της Microsoft;",
        "correct": "A, B, X, Y",
        "distractors": ["A, B, C, D", "X, Y, Z, W", "1, 2, 3, 4"],
        "explanation": "Τα κουμπιά του χειριστηρίου του Xbox είναι τα A (πράσινο), B (κόκκινο), X (μπλε) και Y (κίτρινο).",
        "funFacts": [
            "Η διάταξη αυτή των γραμμάτων είχε χρησιμοποιηθεί αρχικά από τη Nintendo στο Super Nintendo (SNES), αλλά με διαφορετικά χρώματα και αντίστροφη θέση.",
            "Το αρχικό ογκώδες χειριστήριο του πρώτου Xbox (2001) ήταν γνωστό στους gamers με το παρατσούκλι 'The Duke'."
        ],
        "source": "https://en.wikipedia.org/wiki/Xbox_controller",
        "tags": ["gaming", "xbox", "microsoft", "hardware", "controller"]
    },
    {
        "id": "gaming_easy_327",
        "text": "Ποιο είναι το χαρακτηριστικό φυσικό σχήμα της κονσόλας Nintendo GameCube (2001) που περιλάμβανε και πλαστική λαβή μεταφοράς στο πίσω μέρος;",
        "correct": "Κύβος (Cube)",
        "distractors": ["Πυραμίδα", "Κύλινδρος", "Σφαίρα"],
        "explanation": "Το GameCube σχεδιάστηκε ως ένας συμπαγής κύβος σε μοβ (Indigo) ή μαύρο χρώμα και χρησιμοποιούσε ειδικά mini-DVD των 8 εκατοστών.",
        "funFacts": [
            "Ο ήχος εκκίνησης του GameCube αλλάζει αν κρατάς πατημένο το κουμπί 'Z' στο χειριστήριο, παίζοντας έναν ήχο πιθήκου ή ένα γιαπωνέζικο θέμα καμπούκι.",
            "Τα μικρά οπτικά δισκάκια mini-DVD χωρούσαν 1,5 GB δεδομένων και επιλέχθηκαν για την καταπολέμηση της πειρατείας."
        ],
        "source": "https://en.wikipedia.org/wiki/GameCube",
        "tags": ["gaming", "gamecube", "nintendo", "hardware", "retro"]
    },
    {
        "id": "gaming_easy_328",
        "text": "Ποια είναι η ταχύτατη κλωτσιά της Chun-Li στο 'Street Fighter' όπου κλωτσάει δεκάδες φορές μέσα σε ελάχιστα δευτερόλεπτα;",
        "correct": "Hyakuretsukyaku (Lightning Legs / Αστραπιαία Πόδια)",
        "distractors": ["Spinning Bird Kick", "Kikoken", "Senpusha"],
        "explanation": "Το Hyakuretsukyaku εκτελείται πατώντας επανειλημμένα και ταχύτατα τα κουμπιά κλωτσιάς, κάνοντας τα πόδια της Chun-Li να μοιάζουν με θολή ακτίνα χτυπημάτων.",
        "funFacts": [
            "Η Chun-Li είναι αξιωματικός της Interpol που αναζητά δικαιοσύνη για τη δολοφονία του πατέρα της από τον M. Bison.",
            "Η ανάποδη περιστροφική κλωτσιά της στον αέρα ονομάζεται Spinning Bird Kick."
        ],
        "source": "https://en.wikipedia.org/wiki/Chun-Li",
        "tags": ["gaming", "street_fighter", "capcom", "chun_li", "fighting"]
    },
    {
        "id": "gaming_easy_329",
        "text": "Πώς ονομάζεται το παγκόσμιο τουρνουά πολεμικών τεχνών που διοργανώνει η οικογένεια Mishima στη σειρά παιχνιδιών 'Tekken';",
        "correct": "The King of Iron Fist Tournament",
        "distractors": ["World Warrior Tournament", "Mortal Kombat Tournament", "Battle Coliseum"],
        "explanation": "Στο Tekken της Bandai Namco, ο Heihachi Mishima και η Mishima Zaibatsu χρηματοδοτούν το τουρνουά King of Iron Fist με έπαθλο τον έλεγχο της πανίσχυρης πολυεθνικής εταιρείας.",
        "funFacts": [
            "Ο Heihachi Mishima έχει τη διαβόητη συνήθεια να πετάει τα μέλη της οικογένειάς του (τον Kazuya και τον Jin) από γκρεμούς και μέσα σε ηφαίστεια.",
            "Το Tekken 3 στο πρώτο PlayStation είναι ένα από τα πιο επιτυχημένα και αγαπημένα 3D fighting games στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Tekken",
        "tags": ["gaming", "tekken", "bandai_namco", "fighting"]
    },
    {
        "id": "gaming_easy_330",
        "text": "Ποιο αρχαίο πνευστό μουσικό όργανο χρησιμοποιεί ο Link στο ομώνυμο αριστούργημα του Nintendo 64 (1998) για να αλλάζει τον καιρό και να ταξιδεύει στον χρόνο;",
        "correct": "Οκαρίνα (Ocarina)",
        "distractors": ["Φλάουτο", "Άρπα", "Πανδούρα"],
        "explanation": "Στο 'The Legend of Zelda: Ocarina of Time', ο παίκτης μαθαίνει διάφορες μελωδίες στην Ocarina of Time πατώντας συνδυασμούς κουμπιών του N64 controller.",
        "funFacts": [
            "Το παιχνίδι θεωρείται από πολλούς κριτικούς ως ένα από τα σπουδαιότερα βιντεοπαιχνίδια όλων των εποχών, με την υψηλότερη βαθμολογία στο Metacritic (99/100).",
            "Η 'Μελωδία του Χρόνου' (Song of Time) και η 'Μελωδία των Καταιγίδων' (Song of Storms) είναι μερικά από τα πιο αξιομνημόνευτα κομμάτια του Koji Kondo."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time",
        "tags": ["gaming", "zelda", "nintendo", "ocarina_of_time", "n64"]
    },
    {
        "id": "gaming_easy_331",
        "text": "Στη σειρά 'Metroid', ποια εμβληματική αναβάθμιση επιτρέπει στη Samus Aran να κουλουριάζεται σε μια μικρή σφαίρα και να περνά από στενά περάσματα;",
        "correct": "Morph Ball (Maru Mari)",
        "distractors": ["Screw Attack", "Space Jump", "Varia Suit"],
        "explanation": "Το Morph Ball επιτρέπει στη Samus να συμπτύσσει την πανοπλία της σε μια μικρή σφαίρα διαμέτρου ενός μέτρου για να εξερευνά στενούς αεραγωγούς και να αφήνει βόμβες.",
        "funFacts": [
            "Ο μηχανισμός του Morph Ball εφευρέθηκε επειδή οι δημιουργοί δυσκολεύονταν να προγραμματίσουν ένα ρεαλιστικό animation μπουσουλήματος (crawling) στο NES.",
            "Ενώ βρίσκεται σε μορφή Morph Ball, η Samus μπορεί να αναπηδά χρησιμοποιώντας το ωστικό κύμα των δικών της βομβών (Bomb Jumping)."
        ],
        "source": "https://en.wikipedia.org/wiki/Metroid",
        "tags": ["gaming", "metroid", "nintendo", "samus_aran", "mechanics"]
    },
    {
        "id": "gaming_easy_332",
        "text": "Στο παιχνίδι 'Team Fortress 2' της Valve, ποιο είναι το αγαπημένο βαρύ πολυβόλο (Minigun) του ρωσικής καταγωγής Heavy Weapons Guy;",
        "correct": "Sasha",
        "distractors": ["Natascha", "Vera", "Katya"],
        "explanation": "Ο Heavy αποκαλεί χαϊδευτικά το βασικό του Minigun 'Sasha' και καυχιέται ότι 'κοστίζει 400.000 δολάρια για να πυροβολεί για μόλις 12 δευτερόλεπτα'.",
        "funFacts": [
            "Ο Heavy λατρεύει επίσης τα σάντουιτς, κρατώντας το αντικείμενο Sandvich που του αναπληρώνει πλήρως την υγεία.",
            "Το Team Fortress 2 καθιέρωσε την εικονική οικονομία ανταλλαγής ψηφιακών καπέλων (hat trading) στο Steam."
        ],
        "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
        "tags": ["gaming", "team_fortress_2", "valve", "fps"]
    },
    {
        "id": "gaming_easy_333",
        "text": "Ποιο είναι το διάσημο ψηφιακό παιχνίδι καρτών στρατηγικής της Blizzard που διαδραματίζεται στον κόσμο του Warcraft;",
        "correct": "Hearthstone",
        "distractors": ["Magic: The Gathering Arena", "Gwent", "Artifact"],
        "explanation": "Το Hearthstone (αρχικά Hearthstone: Heroes of Warcraft) κυκλοφόρησε το 2014 και έκανε τα digital collectible card games (CCG) εξαιρετικά δημοφιλή παγκοσμίως.",
        "funFacts": [
            "Το παιχνίδι ξεκινά με τον χαρούμενο χαιρετισμό του ξενοδόχου (Innkeeper): 'Busy night, but there's always room for another!'.",
            "Οι παίκτες χτίζουν τράπουλες 30 καρτών γύρω από έναν κεντρικό ήρωα όπως ο Jaina Proudmoore ή ο Thrall."
        ],
        "source": "https://en.wikipedia.org/wiki/Hearthstone",
        "tags": ["gaming", "hearthstone", "blizzard", "card_game", "warcraft"]
    },
    {
        "id": "gaming_easy_334",
        "text": "Ποια σειρά σκοτεινών action-RPG της Blizzard διαδραματίζεται στον κόσμο του Sanctuary και επικεντρώνεται στη μάχη ενάντια στον Άρχοντα του Τρόμου;",
        "correct": "Diablo",
        "distractors": ["Warcraft", "StarCraft", "Baldur's Gate"],
        "explanation": "Το Diablo (1996) όρισε το είδος του isometric action RPG / hack and slash, όπου οι παίκτες εξερευνούν μπουντρούμια και συλλέγουν λάφυρα (loot).",
        "funFacts": [
            "Ο διάσημος αστικός μύθος για το μυστικό επίπεδο με τις αγελάδες (Secret Cow Level) ξεκίνησε ως φήμη στο πρώτο Diablo και υλοποιήθηκε επίσημα στο Diablo II.",
            "Ο ηλικιωμένος σοφός Deckard Cain έμεινε στην ιστορία με τη φράση 'Stay awhile and listen!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_(video_game_series)",
        "tags": ["gaming", "diablo", "blizzard", "action_rpg"]
    },
    {
        "id": "gaming_easy_335",
        "text": "Ποια Ελβετίδα γιατρός και ηρωίδα υποστήριξης στο 'Overwatch' διαθέτει φτερά αγγέλου και τη διάσημη ατάκα 'Heroes never die!';",
        "correct": "Mercy (Dr. Angela Ziegler)",
        "distractors": ["Ana", "Moira", "Brigitte"],
        "explanation": "Η Mercy είναι θεραπεύτρια που χρησιμοποιεί το Caduceus Staff για να αποκαθιστά υγεία ή να ενισχύει τη ζημιά των συμπαικτών της και μπορεί να τους ανασταίνει.",
        "funFacts": [
            "Στην αρχική έκδοση του Overwatch, η απόλυτη ικανότητα (Ultimate) της Mercy μπορούσε να αναστήσει ολόκληρη την ομάδα των 5 συμπαικτών ταυτόχρονα.",
            "Η στολή της ονομάζεται Valkyrie suit και της επιτρέπει να γλιστρά ομαλά στον αέρα."
        ],
        "source": "https://en.wikipedia.org/wiki/Mercy_(Overwatch)",
        "tags": ["gaming", "overwatch", "blizzard", "mercy", "characters"]
    },
    {
        "id": "gaming_easy_336",
        "text": "Ποιο φυτό παράγει μονάδες ηλιακού φωτός (Sun) στο δημοφιλές παιχνίδι στρατηγικής 'Plants vs. Zombies' της PopCap Games;",
        "correct": "Ηλιοτρόπιο (Sunflower)",
        "distractors": ["Peashooter", "Wall-nut", "Cherry Bomb"],
        "explanation": "Το Sunflower παράγει τακτικά ήλιους που είναι απαραίτητοι για να μπορέσει ο παίκτης να αγοράσει και να φυτέψει άλλα αμυντικά φυτά στον κήπο.",
        "funFacts": [
            "Ο εκκεντρικός γείτονας που πουλάει αναβαθμίσεις στον παίκτη από το πορτ-μπαγκάζ του αυτοκινήτου του ονομάζεται Crazy Dave.",
            "Το τραγούδι των τίτλων τέλους 'Zombies on Your Lawn' συντέθηκε από τη Laura Shigihara και έγινε viral hit."
        ],
        "source": "https://en.wikipedia.org/wiki/Plants_vs._Zombies_(video_game)",
        "tags": ["gaming", "plants_vs_zombies", "popcap", "strategy"]
    },
    {
        "id": "gaming_easy_337",
        "text": "Στο mobile παιχνίδι 'Subway Surfers', από ποιον προσπαθούν να ξεφύγουν οι νεαροί χαρακτήρες τρέχοντας πάνω στις ράγες του τρένου;",
        "correct": "Από έναν επιθεωρητή τρένων και το σκυλί του",
        "distractors": ["Από ένα ρομπότ ασφαλείας", "Από έναν οδηγό τρένου", "Από έναν αντίπαλο δρομέα"],
        "explanation": "Ο πρωταγωνιστής Jake πιάνεται να κάνει γκράφιτι σε ένα βαγόνι και αρχίζει να τρέχει στις γραμμές του μετρό για να ξεφύγει από τον αυστηρό επιθεωρητή (Inspector).",
        "funFacts": [
            "Το Subway Surfers έγινε το πρώτο παιχνίδι στην ιστορία του Google Play Store που ξεπέρασε το 1 δισεκατομμύριο λήψεις.",
            "Κάθε λίγες εβδομάδες το παιχνίδι αλλάζει πόλη στο πλαίσιο του 'World Tour' (π.χ. Τόκιο, Παρίσι, Αθήνα, Ρίο)."
        ],
        "source": "https://en.wikipedia.org/wiki/Subway_Surfers",
        "tags": ["gaming", "subway_surfers", "mobile", "endless_runner"]
    },
    {
        "id": "gaming_easy_338",
        "text": "Ποιο απλό και εθιστικό mobile παιχνίδι της Halfbrick Studios (2010) ζητούσε από τους παίκτες να κόβουν καρπούζια, μπανάνες και μήλα με το δάχτυλό τους;",
        "correct": "Fruit Ninja",
        "distractors": ["Fruit Slicer", "Blade Master", "Ninja Cut"],
        "explanation": "Στο Fruit Ninja, διάφορα φρούτα πετιούνται στην οθόνη και ο παίκτης τα κόβει σέρνοντας το δάχτυλό του σαν σπαθί κατάνα, αποφεύγοντας τις εκρηκτικές βόμβες.",
        "funFacts": [
            "Το παιχνίδι δημιουργήθηκε από την αυστραλιανή εταιρεία Halfbrick Studios και ξεπέρασε τα 300 εκατομμύρια downloads.",
            "Αν ο παίκτης χτυπήσει μια βόμβα στο Classic mode, το παιχνίδι τελειώνει ακαριαία."
        ],
        "source": "https://en.wikipedia.org/wiki/Fruit_Ninja",
        "tags": ["gaming", "fruit_ninja", "mobile", "casual"]
    },
    {
        "id": "gaming_easy_339",
        "text": "Ποιο είναι το όνομα του πιλότου-αλεπού και αρχηγού της επίλεκτης ομάδας Star Fox στο διαστημικό shooter της Nintendo;",
        "correct": "Fox McCloud",
        "distractors": ["Falco Lombardi", "Slippy Toad", "Peppy Hare"],
        "explanation": "Ο Fox McCloud πιλοτάρει το διαστημόπλοιο Arwing πολεμώντας τις δυνάμεις του σατανικού Andross στο πλανητικό σύστημα Lylat.",
        "funFacts": [
            "Η περίφημη συμβουλή του Peppy Hare 'Do a barrel roll!' έγινε ένα από τα πιο θρυλικά memes του διαδικτύου.",
            "Το πρώτο Star Fox στο SNES (1993) χρησιμοποίησε το πρωτοποριακό τσιπ Super FX για να αποδώσει 3D πολυγωνικά γραφικά."
        ],
        "source": "https://en.wikipedia.org/wiki/Fox_McCloud",
        "tags": ["gaming", "star_fox", "nintendo", "characters", "sci_fi"]
    },
    {
        "id": "gaming_easy_340",
        "text": "Ποιος φουτουριστικός οδηγός αγώνων της σειράς 'F-Zero' είναι διάσημος για την πανίσχυρη γροθιά φωτιάς 'Falcon Punch' στο Super Smash Bros.;",
        "correct": "Captain Falcon",
        "distractors": ["Samus Aran", "Fox McCloud", "Little Mac"],
        "explanation": "Ο Captain Falcon είναι κυνηγός επικηρυγμένων και πιλότος του αγωνιστικού σκάφους Blue Falcon στους διαγαλαξιακούς αγώνες ταχύτητας F-Zero.",
        "funFacts": [
            "Η κίνηση 'Falcon Punch' δεν υπήρχε στα αρχικά racing παιχνίδια F-Zero, αλλά δημιουργήθηκε ειδικά για το Super Smash Bros. στο N64.",
            "Το πρώτο F-Zero (1990) αξιοποίησε την τεχνολογία Mode 7 του Super Nintendo για να προσομοιώσει ψευδο-3D κίνηση εδάφους."
        ],
        "source": "https://en.wikipedia.org/wiki/Captain_Falcon",
        "tags": ["gaming", "f_zero", "nintendo", "captain_falcon", "racing"]
    },
    {
        "id": "gaming_easy_341",
        "text": "Ποιο διάσημο franchise συνδυάζει τους χαρακτήρες της Disney (Mickey, Donald, Goofy) με τους ήρωες του 'Final Fantasy' της Square Enix;",
        "correct": "Kingdom Hearts",
        "distractors": ["Disney Infinity", "Epic Mickey", "World of Final Fantasy"],
        "explanation": "Το Kingdom Hearts δημιουργήθηκε από τον Tetsuya Nomura και ακολουθεί τον νεαρό Sora που ταξιδεύει σε διάφορους κόσμους κινουμένων σχεδίων της Disney.",
        "funFacts": [
            "Η αρχική ιδέα της συνεργασίας προέκυψε όταν στελέχη της Square και της Disney συναντήθηκαν τυχαία σε ένα ασανσέρ στο Τόκιο.",
            "Το όπλο του Sora έχει το σχήμα ενός γιγάντιου κλειδιού και ονομάζεται Keyblade."
        ],
        "source": "https://en.wikipedia.org/wiki/Kingdom_Hearts",
        "tags": ["gaming", "kingdom_hearts", "square_enix", "disney", "rpg"]
    },
    {
        "id": "gaming_easy_342",
        "text": "Ποιο είναι το όνομα του βασικού πρωταγωνιστή της σειράς 'Kingdom Hearts' που κρατάει το μυθικό Keyblade;",
        "correct": "Sora",
        "distractors": ["Riku", "Roxas", "Kairi"],
        "explanation": "Ο Sora ξεκινά την περιπέτειά του από τα Destiny Islands παρέα με τον Donald Duck και τον Goofy για να σώσει τους κόσμους από τα πλάσματα Heartless.",
        "funFacts": [
            "Το όνομα 'Sora' σημαίνει 'Ουρανός' στα ιαπωνικά, ενώ του φίλου του 'Riku' σημαίνει 'Γη' και της 'Kairi' σημαίνει 'Θάλασσα'.",
            "Ο Sora προστέθηκε ως ο τελευταίος DLC μαχητής στο Super Smash Bros. Ultimate μετά από παγκόσμια ψηφοφορία των παικτών."
        ],
        "source": "https://en.wikipedia.org/wiki/Sora_(Kingdom_Hearts)",
        "tags": ["gaming", "kingdom_hearts", "sora", "characters"]
    },
    {
        "id": "gaming_easy_343",
        "text": "Στη σειρά 'Monster Hunter' της Capcom, ποιος είναι ο εμβληματικός δράκος-αρπακτικό με τα κόκκινα φτερά, γνωστός και ως 'Βασιλιάς των Ουρανών';",
        "correct": "Rathalos",
        "distractors": ["Diablos", "Zinogre", "Tigrex"],
        "explanation": "Ο Rathalos είναι η κλασική μασκότ της σειράς Monster Hunter από το 2004, ενώ το θηλυκό αντίστοιχό του ονομάζεται Rathian.",
        "funFacts": [
            "Οι παίκτες κυνηγούν τον Rathalos για να μαζέψουν λέπια, νύχια και ουρά, ώστε να κατασκευάσουν την ισχυρή πανοπλία Rathalos Armor.",
            "Η σειρά Monster Hunter είναι τόσο δημοφιλής στην Ιαπωνία που ορισμένες εταιρείες έδιναν άδεια στους υπαλλήλους τους κατά την ημέρα κυκλοφορίας νέου τίτλου."
        ],
        "source": "https://en.wikipedia.org/wiki/Monster_Hunter",
        "tags": ["gaming", "monster_hunter", "capcom", "action"]
    },
    {
        "id": "gaming_easy_344",
        "text": "Ποιος είναι ο μηχανικός και πρωταγωνιστής του διαστημικού survival horror 'Dead Space' που φοράει στολή εξόρυξης RIG και Plasma Cutter;",
        "correct": "Isaac Clarke",
        "distractors": ["Gordon Freeman", "John Carver", "Samus Aran"],
        "explanation": "Ο Isaac Clarke στέλνεται στο διαστημόπλοιο εξόρυξης USG Ishimura για επισκευές και ανακαλύπτει ότι το πλήρωμα έχει σφαγιαστεί και μεταλλαχθεί σε φρικιαστικά Necromorphs.",
        "funFacts": [
            "Το όνομά του αποτελεί συνδυασμό δύο διάσημων συγγραφέων επιστημονικής φαντασίας: του Isaac Asimov και του Arthur C. Clarke.",
            "Στο πρώτο παιχνίδι (2008), ο βασικός κανόνας επιβίωσης ήταν ο διαμελισμός των άκρων των τεράτων και όχι οι βολές στο κεφάλι."
        ],
        "source": "https://en.wikipedia.org/wiki/Isaac_Clarke",
        "tags": ["gaming", "dead_space", "ea", "survival_horror", "sci_fi"]
    },
    {
        "id": "gaming_easy_345",
        "text": "Ποιο είναι το μεγάλο κίτρινο πουλί που χρησιμεύει ως υποζύγιο και μασκότ στη σειρά παιχνιδιών 'Final Fantasy';",
        "correct": "Chocobo (Τσοκόμπο)",
        "distractors": ["Moogle", "Cactuar", "Tonberry"],
        "explanation": "Τα Chocobo είναι μεγάλα πουλιά (που θυμίζουν στρουθοκάμηλο) με χαρακτηριστική κραυγή 'Kweh!' ή 'Wark!' τα οποία οι παίκτες ιππεύουν για γρήγορη μετακίνηση.",
        "funFacts": [
            "Στο Final Fantasy VII, οι παίκτες μπορούν να εκτρέφουν και να διασταυρώνουν Chocobos για να αποκτήσουν το θρυλικό Χρυσό Chocobo που περνάει πάνω από βουνά και ωκεανούς.",
            "Το χαρούμενο μουσικό θέμα των Chocobo εμφανίζεται με διαφορετικές παραλλαγές σε σχεδόν κάθε τίτλο της σειράς."
        ],
        "source": "https://en.wikipedia.org/wiki/Chocobo",
        "tags": ["gaming", "final_fantasy", "square_enix", "chocobo"]
    },
    {
        "id": "gaming_easy_346",
        "text": "Ποιο μικρό πλασματάκι με φτερά νυχτερίδας και μια κόκκινη μπάλα (pom-pom) στο κεφάλι λέει συνεχώς 'Kupo' στο 'Final Fantasy';",
        "correct": "Moogle",
        "distractors": ["Chocobo", "Cactuar", "Carbuncle"],
        "explanation": "Τα Moogles είναι αξιαγάπητα μαγικά πλάσματα που συχνά λειτουργούν ως ταχυδρόμοι, έμποροι ή σημεία αποθήκευσης προόδου (save points) στη σειρά Final Fantasy.",
        "funFacts": [
            "Η λέξη Moogle είναι μετάφραση του ιαπωνικού 'Moguri', που είναι συνδυασμός των λέξεων mogura (τυφλοπόντικας) και kōmori (νυχτερίδα).",
            "Στο Final Fantasy IX, τα Moogles διαχειρίζονται ένα παγκόσμιο δίκτυο αλληλογραφίας που ονομάζεται Mognet."
        ],
        "source": "https://en.wikipedia.org/wiki/Moogle",
        "tags": ["gaming", "final_fantasy", "square_enix", "moogle"]
    },
    {
        "id": "gaming_easy_347",
        "text": "Ποια είναι η βασική πόλη και έδρα της κακόβουλης εταιρείας ηλεκτρικής ενέργειας Shinra Electric Power Company στο 'Final Fantasy VII';",
        "correct": "Midgar",
        "distractors": ["Junon", "Costa del Sol", "Wutai"],
        "explanation": "Η Midgar είναι μια κυκλική βιομηχανική μητρόπολη χωρισμένη σε οκτώ τομείς, όπου οι πλούσιοι ζουν στην άνω πλατφόρμα και οι φτωχοί στις παραγκουπόλεις από κάτω.",
        "funFacts": [
            "Η Shinra αντλεί την ενέργεια Mako απευθείας από τα σπλάχνα του πλανήτη, απομυζώντας την ίδια τη ροή της ζωής (Lifestream).",
            "Το πρώτο μέρος του Final Fantasy VII Remake (2020) διαδραματίζεται αποκλειστικά μέσα στην πόλη Midgar."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VII",
        "tags": ["gaming", "final_fantasy", "square_enix", "midgar"]
    },
    {
        "id": "gaming_easy_348",
        "text": "Στο παιχνίδι 'Borderlands' της Gearbox Software, σε ποιον άγονο και επικίνδυνο πλανήτη ψάχνουν οι Vault Hunters για εξωγήινους θησαυρούς;",
        "correct": "Pandora",
        "distractors": ["Promethea", "Eden-6", "Elpis"],
        "explanation": "Ο πλανήτης Pandora είναι ένας αφιλόξενος κόσμος γεμάτος ληστές (bandits), ψυχοπαθείς και άγρια θηρία, όπου κρύβονται τα μυθικά θησαυροφυλάκια (Vaults).",
        "funFacts": [
            "Ο μικρός υπερκινητικός κίτρινος ρομποτικός βοηθός που υποδέχεται τον παίκτη ονομάζεται Claptrap.",
            "Το παιχνίδι συνδύασε μοναδικά το gameplay ενός first-person shooter με εκατομμύρια τυχαία παραγόμενα όπλα (looter-shooter)."
        ],
        "source": "https://en.wikipedia.org/wiki/Borderlands_(video_game)",
        "tags": ["gaming", "borderlands", "gearbox", "fps", "looter_shooter"]
    },
    {
        "id": "gaming_easy_349",
        "text": "Ποιο κλασικό 2D platformer της Konami (1987) με δύο κομάντο έγινε διάσημο για τον ιστορικό κωδικό 'Konami Code' που έδινε 30 ζωές;",
        "correct": "Contra",
        "distractors": ["Metal Gear", "Castlevania", "Gradius"],
        "explanation": "Στο Contra, οι κομάντο Bill Rizer και Lance Bean πολεμούν εξωγήινες δυνάμεις· πατώντας τον Konami Code στην αρχική οθόνη, ο παίκτης αποκτούσε 30 ζωές αντί για 3.",
        "funFacts": [
            "Ο περίφημος κωδικός Konami Code είναι: Πάνω, Πάνω, Κάτω, Κάτω, Αριστερά, Δεξιά, Αριστερά, Δεξιά, B, A.",
            "Στην Ευρώπη, λόγω των αυστηρών νόμων λογοκρισίας για τη βία στη Γερμανία, το παιχνίδι κυκλοφόρησε με ρομπότ αντί για ανθρώπους και τον τίτλο 'Probotector'."
        ],
        "source": "https://en.wikipedia.org/wiki/Contra_(video_game)",
        "tags": ["gaming", "contra", "konami", "retro", "nes"]
    },
    {
        "id": "gaming_easy_350",
        "text": "Στο παιχνίδι 'Portal 2' (2011), ποιος είναι ο φλύαρος, αδέξιος σφαιρικός πυρήνας τεχνητής νοημοσύνης που βοηθάει αρχικά την Chell να αποδράσει;",
        "correct": "Wheatley",
        "distractors": ["GLaDOS", "Space Core", "Cave Johnson"],
        "explanation": "Ο Wheatley (με τη φωνή του Βρετανού κωμικού Stephen Merchant) είναι ένας πυρήνας προσωπικότητας σχεδιασμένος αρχικά για να παράγει τις πιο ανόητες αποφάσεις.",
        "funFacts": [
            "Όταν ο Wheatley αναλαμβάνει τον έλεγχο των εργαστηρίων της Aperture, μεθάει από τη δύναμη και μετατρέπεται στον βασικό κακό του παιχνιδιού.",
            "Η GLaDOS μετατρέπεται προσωρινά σε μπαταρία πατάτας (potatOS) και συμμαχεί με την Chell για να τον σταματήσουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Wheatley_(Portal)",
        "tags": ["gaming", "portal", "valve", "wheatley", "puzzle"]
    },
    {
        "id": "gaming_easy_351",
        "text": "Στο παιχνίδι 'Team Fortress 2', ποια κατηγορία (class) μπορεί να μεταμφιέζεται σε μέλος της αντίπαλης ομάδας και να μαχαιρώνει πισώπλατα (backstab);",
        "correct": "Spy (Κατάσκοπος)",
        "distractors": ["Sniper", "Scout", "Demoman"],
        "explanation": "Ο Γάλλος Spy χρησιμοποιεί ένα ρολόι αορατότητας, μια συσκευή σαμποτάζ (Sapper) και ένα μαχαίρι πεταλούδα για να εξοντώνει άμεσα εχθρούς με πισώπλατο χτύπημα.",
        "funFacts": [
            "Ένα επιτυχές backstab από τον Spy προκαλεί ζημιά ίση με το 600% της τρέχουσας υγείας του θύματος, εξασφαλίζοντας ακαριαίο θάνατο.",
            "Ο Pyro είναι ο μεγαλύτερος φυσικός αντίπαλος του Spy, καθώς η φωτιά αποκαλύπτει αμέσως την αορατότητα και τις μεταμφιέσεις του."
        ],
        "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
        "tags": ["gaming", "team_fortress_2", "valve", "spy", "fps"]
    },
    {
        "id": "gaming_easy_352",
        "text": "Στο 'Mario Kart', πώς συμπεριφέρεται το πράσινο καβούκι (Green Shell) όταν εκτοξεύεται από τον οδηγό;",
        "correct": "Κινείται σε απόλυτα ευθεία γραμμή και αναπηδά στους τοίχους",
        "distractors": ["Ακολουθεί αυτόματα το προπορευόμενο καρτ", "Εκρήγνυται αμέσως μόλις αγγίξει το έδαφος", "Πέφτει από ψηλά σαν αλεξίπτωτο"],
        "explanation": "Σε αντίθεση με το κόκκινο καβούκι που κλειδώνει πάνω στον στόχο, το πράσινο καβούκι ταξιδεύει σε ευθεία γραμμή και μπορεί να χτυπήσει ακόμα και τον ίδιο τον παίκτη αν αναπηδήσει πίσω.",
        "funFacts": [
            "Ο παίκτης μπορεί να εκτοξεύσει το πράσινο καβούκι είτε προς τα εμπρός είτε προς τα πίσω κρατώντας τον μοχλό προς τα πίσω.",
            "Τα τρία πράσινα καβούκια (Triple Green Shells) περιστρέφονται γύρω από το καρτ, λειτουργώντας και ως προστατευτική ασπίδα."
        ],
        "source": "https://en.wikipedia.org/wiki/Mario_Kart",
        "tags": ["gaming", "mario_kart", "nintendo", "items"]
    },
    {
        "id": "gaming_easy_353",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο 'BioShock Infinite' που προσλαμβάνεται για να 'φέρει το κορίτσι και να σβήσει το χρέος του';",
        "correct": "Booker DeWitt",
        "distractors": ["Jack", "Andrew Ryan", "Frank Fontaine"],
        "explanation": "Ο Booker DeWitt είναι πρώην πράκτορας των Pinkertons που ταξιδεύει στην ιπτάμενη πόλη Columbia το 1912 για να εντοπίσει και να διασώσει την Elizabeth.",
        "funFacts": [
            "Η διάσημη φράση ανάθεσης της αποστολής του είναι: 'Bring us the girl, and wipe away the debt'.",
            "Τη φωνή του Booker DeWitt ενσάρκωσε ο καταξιωμένος ηθοποιός φωνής Troy Baker."
        ],
        "source": "https://en.wikipedia.org/wiki/Booker_DeWitt",
        "tags": ["gaming", "bioshock", "booker_dewitt", "fps"]
    },
    {
        "id": "gaming_easy_354",
        "text": "Ποιο είναι το όνομα του κυβερνήτη και μέντορα του Nathan Drake στη σειρά 'Uncharted' που καπνίζει πούρα και έχει χαρακτηριστικό μουστάκι;",
        "correct": "Victor 'Sully' Sullivan",
        "distractors": ["Sam Drake", "Harry Flynn", "Charlie Cutter"],
        "explanation": "Ο Victor Sullivan είναι ο πατρικός φίλος, μέντορας και συνεργάτης του Nathan Drake σε όλες τις παράτολμες αρχαιολογικές του εξορμήσεις.",
        "funFacts": [
            "Ο Sully γνώρισε για πρώτη φορά τον έφηβο Nathan Drake στην Καρθαγένη της Κολομβίας, όπως αποκαλύπτεται στο Uncharted 3.",
            "Το χαρακτηριστικό υδροπλάνο του Sully στα πρώτα παιχνίδια ονομάζεται Hog Wild."
        ],
        "source": "https://en.wikipedia.org/wiki/List_of_Uncharted_characters#Victor_Sullivan",
        "tags": ["gaming", "uncharted", "playstation", "naughty_dog", "characters"]
    },
    {
        "id": "gaming_easy_355",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο franchise 'Assassin's Creed II', ο οποίος ξεκινά ως νεαρός ευγενής στη Φλωρεντία της Αναγέννησης;",
        "correct": "Ezio Auditore da Firenze",
        "distractors": ["Altaïr Ibn-La'Ahad", "Connor Kenway", "Edward Kenway"],
        "explanation": "Ο Ezio Auditore είναι ο κεντρικός ήρωας της τριλογίας Assassin's Creed II, Brotherhood και Revelations, ακολουθώντας τη ζωή του από έφηβο μέχρι τα γηρατειά του.",
        "funFacts": [
            "Ο Ezio αναπτύσσει στενή φιλία με τον Leonardo da Vinci, ο οποίος αποκρυπτογραφεί αρχαίους κώδικες και του κατασκευάζει όπλα και ιπτάμενες μηχανές.",
            "Η τριλογία του Ezio θεωρείται ευρέως ως η χρυσή εποχή της σειράς Assassin's Creed."
        ],
        "source": "https://en.wikipedia.org/wiki/Ezio_Auditore_da_Firenze",
        "tags": ["gaming", "assassins_creed", "ubisoft", "ezio", "characters"]
    },
    {
        "id": "gaming_easy_356",
        "text": "Ποιο είναι το όνομα του πρώτου ιστορικού πρωταγωνιστή ασασίνου στο αρχικό 'Assassin's Creed' (2007) κατά την εποχή της Γ' Σταυροφορίας;",
        "correct": "Altaïr Ibn-La'Ahad",
        "distractors": ["Ezio Auditore", "Bayek of Siwa", "Haytham Kenway"],
        "explanation": "Ο Altaïr Ibn-La'Ahad ήταν μέλος της Αδελφότητας των Ασασίνων στους Αγίους Τόπους (Ιερουσαλήμ, Δαμασκός, Άκρα) υπό την καθοδήγηση του Al Mualim.",
        "funFacts": [
            "Το όνομα Altaïr σημαίνει 'Αυτός που πετάει' ή 'Αετός' στα αραβικά.",
            "Στο πρώτο παιχνίδι, ο Altaïr πέθαινε αμέσως μόλις έπεφτε στο νερό, κάτι που διορθώθηκε με τον Ezio στα επόμενα παιχνίδια."
        ],
        "source": "https://en.wikipedia.org/wiki/Alta%C3%AFr_Ibn-La%27Ahad",
        "tags": ["gaming", "assassins_creed", "ubisoft", "altair", "characters"]
    },
    {
        "id": "gaming_easy_357",
        "text": "Στο παιχνίδι 'Overwatch', ποιος πρώην DJ από τη Βραζιλία πατινάρει πάνω σε τοίχους και θεραπεύει τους συμπαίκτες του με μουσική;",
        "correct": "Lúcio",
        "distractors": ["Baptiste", "Zenyatta", "Lifeweaver"],
        "explanation": "Ο Lúcio Correia dos Santos χρησιμοποιεί ηχητική τεχνολογία για να παίζει μουσικά κομμάτια που είτε επιταχύνουν (Speed Boost) είτε θεραπεύουν (Crossfade Heal) την ομάδα του.",
        "funFacts": [
            "Η χαρακτηριστική του ικανότητα Wall Ride του επιτρέπει να γλιστράει πάνω σε κατακόρυφους τοίχους με εξαιρετική ταχύτητα.",
            "Η απόλυτη ικανότητά του (Sound Barrier) προσφέρει τεράστιες προσωρινές ασπίδες σε όλους τους συμμάχους όταν χτυπάει το έδαφος ('Drop the beat!')."
        ],
        "source": "https://en.wikipedia.org/wiki/Characters_of_Overwatch#L%C3%BAcio",
        "tags": ["gaming", "overwatch", "blizzard", "lucio", "characters"]
    },
    {
        "id": "gaming_easy_358",
        "text": "Στο παιχνίδι 'God of War' (2018), ποιο μαγικό παγωμένο τσεκούρι χρησιμοποιεί ο Kratos, το οποίο επιστρέφει στο χέρι του σαν μπούμερανγκ;",
        "correct": "Leviathan Axe (Τσεκούρι Λεβιάθαν)",
        "distractors": ["Blades of Chaos", "Blade of Olympus", "Draupnir Spear"],
        "explanation": "Το Leviathan Axe σφυρηλατήθηκε από τους νάνους αδελφούς Brok και Sindri για τη σύζυγο του Kratos, Faye, και μπορεί να παγώνει εχθρούς και μηχανισμούς.",
        "funFacts": [
            "Ο Kratos μπορεί να πετάξει το τσεκούρι σε οποιαδήποτε απόσταση και να το ανακαλέσει στο χέρι του πατώντας το κουμπί Triangle.",
            "Οι δημιουργοί ξόδεψαν μήνες τελειοποιώντας το 'βάρος' και την αίσθηση του τσεκουριού κατά την επιστροφή του στο χέρι."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_(2018_video_game)",
        "tags": ["gaming", "god_of_war", "playstation", "weapons", "kratos"]
    },
    {
        "id": "gaming_easy_359",
        "text": "Ποιο είναι το όνομα του νεαρού γιου του Kratos που τον συνοδεύει με το τόξο του στις περιπέτειες της σκανδιναβικής μυθολογίας;",
        "correct": "Atreus",
        "distractors": ["Deimos", "Baldur", "Magni"],
        "explanation": "Ο Atreus βοηθά τον πατέρα του μεταφράζοντας αρχαίες ρουνικές επιγραφές και ρίχνοντας μαγικά βέλη στους εχθρούς.",
        "funFacts": [
            "Στο τέλος του God of War (2018), αποκαλύπτεται ότι το όνομα που του είχαν δώσει οι Γίγαντες (Jötnar) ήταν Loki.",
            "Ο ηθοποιός Sunny Suljic ενσάρκωσε τον Atreus τόσο στη φωνή όσο και στο motion capture."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_(2018_video_game)",
        "tags": ["gaming", "god_of_war", "playstation", "atreus", "characters"]
    },
    {
        "id": "gaming_easy_360",
        "text": "Ποια είναι η επίσημη ονομασία του χειριστηρίου της κονσόλας PlayStation 5 που διαθέτει απτική ανάδραση (haptic feedback) και δυναμικές σκανδάλες;",
        "correct": "DualSense",
        "distractors": ["DualShock 5", "Sixaxis", "Play Controller"],
        "explanation": "Το DualSense αντικατέστησε τη σειρά DualShock στο PS5, εισάγοντας εξελιγμένη απτική ανάδραση και προσαρμοστικές σκανδάλες (adaptive triggers) με αντίσταση.",
        "funFacts": [
            "Οι προσαρμοστικές σκανδάλες μπορούν να προσομοιώσουν την αντίσταση ενός τεντωμένου τόξου ή το μπλοκάρισμα ενός όπλου.",
            "Η υφή στο πίσω μέρος του DualSense αποτελείται από 40.000 μικροσκοπικά ανάγλυφα σύμβολα του PlayStation (τρίγωνα, κύκλους, σταυρούς και τετράγωνα)."
        ],
        "source": "https://en.wikipedia.org/wiki/DualSense",
        "tags": ["gaming", "playstation", "hardware", "controller", "ps5"]
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
    print(f"Loaded {len(questions)} questions for gaming_easy batch 3.")
    validate_and_append("gaming", "easy", 1, questions)

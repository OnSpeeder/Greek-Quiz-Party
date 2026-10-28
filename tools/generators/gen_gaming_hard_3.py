# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_101",
        "text": "Στο 'Metal Gear Solid 3: Snake Eater' (2004), ποια ασυνήθιστη σκηνή χωρίς κανέναν διάλογο ή εχθρούς διαρκεί σχεδόν δύο ολόκληρα λεπτά, συνοδευόμενη μόνο από την a cappella εκτέλεση του κεντρικού τραγουδιού;",
        "correct": "Η ανάβαση στη γιγάντια μεταλλική σκάλα του Krasnogorje",
        "distractors": [
            "Η διάσχιση της κρεμαστής γέφυρας Dolinovodno",
            "Η κατάδυση στο ποτάμι των φαντασμάτων του The Sorrow",
            "Η αναμονή στο κελί της φυλακής του Groznyj Grad"
        ],
        "explanation": "Η περιβόητη σκάλα του Snake Eater είναι μια τεράστια κάθετη ανάβαση στο βουνό. Ο Hideo Kojima τη σχεδίασε ως έναν διαλογιστικό καθαρμό πριν την τελική κορύφωση, όπου ακούγεται μόνο η φωνή της Cynthia Harrell στο 'Snake Eater'.",
        "funFacts": [
            "Εάν ο παίκτης καλέσει τηλεφωνικά στον ασύρματο τη Sigint ή την Para-Medic κατά την ανάβαση, δεν λαμβάνει καμία απάντηση.",
            "Η σκηνή της σκάλας έγινε ένα από τα πιο αναγνωρίσιμα και αγαπημένα cult memes ολόκληρης της σειράς Metal Gear."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_3:_Snake_Eater",
        "tags": ["gaming", "metal_gear", "kojima", "playstation2", "easter_egg"]
    },
    {
        "id": "gaming_hard_102",
        "text": "Ποιο ήταν το όνομα της επαναστατικής μηχανής adventure games που δημιούργησαν οι Ron Gilbert και Aric Wilmunder το 1987 για το 'Maniac Mansion', εξυπηρετώντας δεκάδες κλασικά παιχνίδια της LucasArts;",
        "correct": "SCUMM (Script Creation Utility for Maniac Mansion)",
        "distractors": [
            "AGI (Adventure Game Interpreter)",
            "SCI (Sierra Creative Interpreter)",
            "GrimE (Grim Edit)"
        ],
        "explanation": "Το SCUMM επέτρεψε τη δημιουργία διαδραστικών περιπετειών χωρίς απευθείας προγραμματισμό σε χαμηλό επίπεδο γλώσσας. Χρησιμοποιήθηκε σε αριστουργήματα όπως Monkey Island, Day of the Tentacle, Sam & Max και Indiana Jones.",
        "funFacts": [
            "Το διάσημο μπαρ 'SCUMM Bar' στο πρώτο νησί του Monkey Island (Mêlée Island) πήρε το όνομά του ως φόρο τιμής στη μηχανή.",
            "Σήμερα όλα αυτά τα παιχνίδια τρέχουν σε σύγχρονους υπολογιστές και κινητά χάρη στον εξομοιωτή ανοιχτού κώδικα ScummVM."
        ],
        "source": "https://en.wikipedia.org/wiki/SCUMM",
        "tags": ["gaming", "lucasarts", "scumm", "ron_gilbert", "adventure"]
    },
    {
        "id": "gaming_hard_103",
        "text": "Ποιος θρυλικός Νοτιοκορεάτης επαγγελματίας παίκτης του 'StarCraft: Brood War', γνωστός ως 'The Emperor of Terran' (BoxeR), θεωρείται ο πατέρας των σύγχρονων esports;",
        "correct": "Lim Yo-hwan (BoxeR)",
        "distractors": [
            "Lee Young-ho (Flash)",
            "Lee Jae-dong (Jaedong)",
            "Song Byung-gu (Stork)"
        ],
        "explanation": "Ο Lim Yo-hwan (BoxeR) έφερε επανάσταση στη στρατηγική των Terran με απίστευτο micro-management (Bunker Rush, Dropship tactics) και έγινε εθνικός σταρ στη Νότια Κορέα με εκατομμύρια θαυμαστές και τηλεοπτικά συμβόλαια.",
        "funFacts": [
            "Ο BoxeR ίδρυσε την κορυφαία ομάδα esports SK Telecom T1 (γνωστή σήμερα ως T1), η οποία αργότερα κυριάρχησε και στο League of Legends με τον Faker.",
            "Το επίσημο fan club του BoxeR στη Νότια Κορέα αριθμούσε πάνω από 600.000 εγγεγραμμένα μέλη."
        ],
        "source": "https://en.wikipedia.org/wiki/Lim_Yo-hwan",
        "tags": ["gaming", "esports", "starcraft", "boxer", "korea"]
    },
    {
        "id": "gaming_hard_104",
        "text": "Στο MMORPG 'EverQuest' το 2003, ποιο μυθικό boss (ένας αρχαίος δράκος γνωστός ως 'The Sleeper' / Kerafyrm) θεωρούνταν απόλυτα ανίκητο από τους δημιουργούς, αλλά σκοτώθηκε μετά από 3ωρη μάχη από τη συμμαχία 3 guilds;",
        "correct": "Kerafyrm the Sleeper (στον server Rallos Zek)",
        "distractors": [
            "Lord Nagafen",
            "Lady Vox",
            "Trakanon the Undead"
        ],
        "explanation": "Ο Kerafyrm σχεδιάστηκε για να ξυπνήσει, να σκοτώσει τα πάντα στο πέρασμά του και να εξαφανιστεί για πάντα. Στον PvP server Rallos Zek, σχεδόν 200 παίκτες ενώθηκαν και τον σκότωσαν με αδιάκοπη χρήση resurrect και pet aggro.",
        "funFacts": [
            "Κατά τη διάρκεια της πρώτης προσπάθειας, οι game masters της Sony Online Entertainment έκαναν despawn τον δράκο πιστεύοντας ότι οι παίκτες εκμεταλλεύονταν bug, προκαλώντας τεράστια εξέγερση.",
            "Η SOE απολογήθηκε την επόμενη μέρα, επανέφερε τον Sleeper και οι παίκτες τον νίκησαν νόμιμα χωρίς exploits."
        ],
        "source": "https://en.wikipedia.org/wiki/EverQuest",
        "tags": ["gaming", "everquest", "mmo", "sleeper", "history"]
    },
    {
        "id": "gaming_hard_105",
        "text": "Ποιο καινοτόμο σύστημα κάμερας εισήγαγε ο Shinji Mikami στο 'Resident Evil 4' (2005), το οποίο εγκατέλειψε τις στατικές κάμερες και καθόρισε ολόκληρο το είδος των third-person action games;",
        "correct": "Κάμερα πάνω από τον ώμο (Over-the-shoulder third-person camera)",
        "distractors": [
            "Πλήρως ελεύθερη isometric rotating camera",
            "Κάμερα πρώτου προσώπου με dynamic crosshair",
            "Κινηματογραφική pan-and-scan camera"
        ],
        "explanation": "Η τοποθέτηση της κάμερας ακριβώς πίσω από τον ώμο του Leon Kennedy με στόχευση laser έφερε επανάσταση, επηρεάζοντας άμεσα τίτλους όπως Gears of War, Dead Space, Mass Effect, Uncharted και The Last of Us.",
        "funFacts": [
            "Ο δημιουργός του Gears of War, Cliff Bleszinski, δήλωσε δημόσια ότι χωρίς το Resident Evil 4 το Gears of War δεν θα υπήρχε ποτέ στη μορφή που το γνωρίζουμε.",
            "Το RE4 ακυρώθηκε και ξανασχεδιάστηκε τέσσερις διαφορετικές φορές πριν την τελική του κυκλοφορία στο Nintendo GameCube."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_4",
        "tags": ["gaming", "resident_evil", "mikami", "gamecube", "mechanics"]
    },
    {
        "id": "gaming_hard_106",
        "text": "Ποιος βασικός μηχανισμός όπλων στο shooter 'Gears of War' (Epic Games, 2006) αντάμειβε τον παίκτη με ταχύτερη επαναγέμιση και ενισχυμένη ζημιά αν πατούσε το κουμπί reload την κατάλληλη χρονική στιγμή;",
        "correct": "Active Reload",
        "distractors": [
            "Tactical Chambering",
            "Burst Prime",
            "Precision Venting"
        ],
        "explanation": "Το σύστημα Active Reload εμφάνιζε έναν δείκτη που κινούνταν κατά μήκος μιας μπάρας. Εάν ο παίκτης πατούσε RB στη λευκή ζώνη, ο γεμιστήρας έμπαινε ακαριαία με bonus damage, ενώ αν αστοχούσε, το όπλο μπλόκαρε (jammed).",
        "funFacts": [
            "Το Gears of War ήταν ο κύριος τίτλος βιτρίνας για τη μηχανή γραφικών Unreal Engine 3 της Epic Games.",
            "Το όπλο 'Lancer' με το ενσωματωμένο αλυσοπρίονο σχεδιάστηκε από τον Cliff Bleszinski και έγινε ένα από τα πιο αναγνωρίσιμα όπλα στην ιστορία του Xbox."
        ],
        "source": "https://en.wikipedia.org/wiki/Gears_of_War_(video_game)",
        "tags": ["gaming", "gears_of_war", "epic_games", "xbox", "mechanics"]
    },
    {
        "id": "gaming_hard_107",
        "text": "Ποιος κορυφαίος ηθοποιός του Χόλιγουντ (γνωστός από το 'Apocalypse Now' και το 'The West Wing') δάνεισε τη φωνή και την εμφάνισή του στον 'Illusive Man' στο 'Mass Effect 2' (2010);",
        "correct": "Martin Sheen",
        "distractors": [
            "Keith David",
            "Lance Henriksen",
            "Michael Hogan"
        ],
        "explanation": "Ο Martin Sheen ενσάρκωσε τον αινιγματικό ηγέτη της οργάνωσης Cerberus με μοναδική ένταση, καπνίζοντας αδιάκοπα μπροστά από ένα τεράστιο παράθυρο με θέα ένα ετοιμοθάνατο άστρο.",
        "funFacts": [
            "Ο Sheen ηχογράφησε όλες τις ατάκες του χωρίς να έχει παίξει ποτέ video game, εντυπωσιασμένος όμως από την ποιότητα του σεναρίου του Drew Karpyshyn.",
            "Το Mass Effect 2 κέρδισε δεκάδες βραβεία Game of the Year και θεωρείται από πολλούς η κορυφαία στιγμή της BioWare."
        ],
        "source": "https://en.wikipedia.org/wiki/Mass_Effect_2",
        "tags": ["gaming", "bioware", "mass_effect", "voice_acting", "sci_fi"]
    },
    {
        "id": "gaming_hard_108",
        "text": "Ποιο βίντεο από το World of Warcraft το 2005 έγινε ένα από τα πιο διάσημα viral βίντεο στην ιστορία του διαδικτύου, όταν ένας παίκτης χάλασε το σχολαστικό πλάνο του guild του φωνάζοντας το όνομά του και ορμώντας σε δωμάτιο γεμάτο δράκους;",
        "correct": "Leeroy Jenkins (Ben Schulz)",
        "distractors": [
            "Onyxia Wipe Animation",
            "Serenity Now Funeral Raid",
            "Funeral of Faye"
        ],
        "explanation": "Ο Ben Schulz (ως Paladin Leeroy Jenkins) επέστρεψε από το AFK, φώναξε 'Leeerooooy Jenkins!' και όρμησε στο Rookery του Upper Blackrock Spire, παρασύροντας όλη την ομάδα του σε έναν ξεκαρδιστικό θάνατο.",
        "funFacts": [
            "Η Blizzard τίμησε το γεγονός προσθέτοντας επίσημο τίτλο επιτεύγματος (Achievement) 'Jenkins' και κάρτα Leeroy Jenkins στο Hearthstone.",
            "Η τελευταία ατάκα του Leeroy στο βίντεο ('At least I have chicken') γράφτηκε στην ιστορία της ποπ κουλτούρας."
        ],
        "source": "https://en.wikipedia.org/wiki/Leeroy_Jenkins",
        "tags": ["gaming", "warcraft", "blizzard", "meme", "history"]
    },
    {
        "id": "gaming_hard_109",
        "text": "Πόσα χρόνια διήρκεσε η ανάπτυξη του 'Team Fortress 2' (1998-2007) της Valve, ξεκινώντας ως ρεαλιστικός στρατιωτικός εξομοιωτής (Brotherhood of Arms) πριν καταλήξει σε cartoon αισθητική εμπνευσμένη από τον J.C. Leyendecker;",
        "correct": "9 χρόνια",
        "distractors": [
            "5 χρόνια",
            "12 χρόνια",
            "7 χρόνια"
        ],
        "explanation": "Το TF2 θεωρούνταν 'vaporware' για σχεδόν μια δεκαετία. Η Valve απέρριψε τον ρεαλισμό και υιοθέτησε ένα μοναδικό στυλ γραφικών εμπνευσμένο από τις διαφημιστικές εικονογραφήσεις της δεκαετίας του 1960 και ταινίες κατασκόπων.",
        "funFacts": [
            "Η Valve δημιούργησε τη θρυλική σειρά animation 'Meet the Team' για να παρουσιάσει τις 9 κλάσεις του παιχνιδιού.",
            "Το TF2 ήταν ο τίτλος που καθιέρωσε το οικονομικό μοντέλο microtransactions με καπέλα (hat economy) στο Steam."
        ],
        "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
        "tags": ["gaming", "valve", "team_fortress", "fps", "history"]
    },
    {
        "id": "gaming_hard_110",
        "text": "Ποιο φιλοσοφικό JRPG της Square το 1998 από τον Tetsuya Takahashi απορρίφθηκε αρχικά ως πολύ σκοτεινό για σενάριο του Final Fantasy VII και εξελίχθηκε σε αυτόνομο τίτλο με γιγάντια mecha (Gears);",
        "correct": "Xenogears",
        "distractors": [
            "Xenosaga",
            "Chrono Cross",
            "Vagrant Story"
        ],
        "explanation": "Ο Takahashi και η σύζυγός του Soraya Saga έγραψαν μια ιστορία γεμάτη αναφορές στον Jung, τον Freud, τον Νίτσε και τον γνωστικισμό. Το δεύτερο CD του παιχνιδιού περιείχε κυρίως αφήγηση σε πολυθρόνα λόγω έλλειψης χρόνου και budget.",
        "funFacts": [
            "Ο Takahashi ίδρυσε αργότερα τη Monolith Soft και δημιούργησε τις σειρές Xenosaga και Xenoblade Chronicles για τη Nintendo.",
            "Το Xenogears αποτελούσε σύμφωνα με το lore το 'Episode V' μιας επικής ιστορίας έξι μερών που δεν ολοκληρώθηκε ποτέ."
        ],
        "source": "https://en.wikipedia.org/wiki/Xenogears",
        "tags": ["gaming", "square", "xenogears", "rpg", "philosophy"]
    },
    {
        "id": "gaming_hard_111",
        "text": "Ποια τεχνική ιδιαιτερότητα του υλικού της κονσόλας Sega Saturn (1994) έκανε τον τρισδιάστατο προγραμματισμό εξαιρετικά δύσκολο σε σύγκριση με το PlayStation 1;",
        "correct": "Η χρήση τετράπλευρων (quads) αντί για τρίγωνα και οι δύο παράλληλοι επεξεργαστές SH-2",
        "distractors": [
            "Η έλλειψη μονάδας κινητής υποδιαστολής (FPU)",
            "Ο περιορισμός της κάρτας βίντεο σε ασπρόμαυρα textures",
            "Η υποχρεωτική χρήση ειδικής κασέτας BIOS για 3D γραφικά"
        ],
        "explanation": "Ενώ όλη η βιομηχανία στράφηκε στα πολύγωνα τριγώνων, το Saturn σχεδίαζε παραμορφωμένα τετράπλευρα (quadrilaterals). Ο συνδυασμός δύο CPUs χωρίς ενιαία διαχείριση μνήμης δυσκόλευε αφάνταστα τους προγραμματιστές τρίτων εταιρειών.",
        "funFacts": [
            "Ο Yu Suzuki παραδέχτηκε ότι μόνο ένας στους 100 προγραμματιστές μπορούσε να αξιοποιήσει πλήρως τις δυνατότητες του Sega Saturn.",
            "Παρά τις δυσκολίες στο 3D, το Saturn ήταν η απόλυτη υπερδύναμη της εποχής στα 2D sprites, ειδικά με την κάρτα 4MB RAM Expansion."
        ],
        "source": "https://en.wikipedia.org/wiki/Sega_Saturn",
        "tags": ["gaming", "sega", "saturn", "hardware", "retro"]
    },
    {
        "id": "gaming_hard_112",
        "text": "Ποιο μυθικό RPG του Sega Saturn (4 CDs) από την Team Andromeda κυκλοφόρησε το 1998 σε ελάχιστα αντίτυπα στη Δύση, με τον πηγαίο κώδικά του να χάνεται οριστικά μετά το κλείσιμο της ομάδας;",
        "correct": "Panzer Dragoon Saga (Azel: Panzer Dragoon RPG)",
        "distractors": [
            "Shining Force III",
            "Magic Knight Rayearth",
            "Dragon Force"
        ],
        "explanation": "Το Panzer Dragoon Saga απέσπασε διθυραμβικές κριτικές για τη μάχη σε 360 μοίρες πάνω σε δράκο και τον μελαγχολικό του κόσμο, αλλά κυκλοφόρησε στο τέλος της ζωής του Saturn σε λιγότερα από 20.000 αντίτυπα στη Δύση.",
        "funFacts": [
            "Τα αυθεντικά αντίτυπα του Panzer Dragoon Saga στο eBay πωλούνται σήμερα για πάνω από 1.000 ευρώ.",
            "Η απώλεια του πηγαίου κώδικα καθιστά αδύνατη μια άμεση επανακυκλοφορία (remaster), απαιτώντας πλήρες remake από την αρχή."
        ],
        "source": "https://en.wikipedia.org/wiki/Panzer_Dragoon_Saga",
        "tags": ["gaming", "sega", "saturn", "panzer_dragoon", "rare"]
    },
    {
        "id": "gaming_hard_113",
        "text": "Ποια πρωτοποριακή μέθοδο προ-αποδοσμένων γραφικών χρησιμοποίησε η Rare στο 'Donkey Kong Country' (1994), χρησιμοποιώντας πανάκριβους σταθμούς εργασίας Silicon Graphics;",
        "correct": "ACM (Advanced Computer Modelling) - μετατροπή 3D μοντέλων σε 2D sprites 16-bit",
        "distractors": [
            "Vector Morphing σε πραγματικό χρόνο",
            "Dynamic Texture Mapping με το τσιπ Super FX",
            "Ray-casting με πίνακα voxel"
        ],
        "explanation": "Η Rare μοντελοποίησε τους χαρακτήρες και τις ζούγκλες σε πανίσχυρους υπολογιστές SGI Challenge και στη συνέχεια συμπίεσε τις αποδόσεις σε 2D sprites, κάνοντας το SNES να μοιάζει με κονσόλα επόμενης γενιάς 32-bit.",
        "funFacts": [
            "Ο Shigeru Miyamoto φέρεται να σχολίασε αρχικά με πικρία ότι οι παίκτες προτιμούσαν τα φανταχτερά γραφικά από το καλό gameplay, αν και αργότερα επαίνεσε το παιχνίδι.",
            "Το Donkey Kong Country πούλησε πάνω από 9 εκατομμύρια αντίτυπα, αναζωογονώντας τις πωλήσεις του Super Nintendo απέναντι στα CD-ROM add-ons της Sega."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_Country",
        "tags": ["gaming", "snes", "rare", "donkey_kong", "graphics"]
    },
    {
        "id": "gaming_hard_114",
        "text": "Ποιο arcade παιχνίδι της Sega το 1993 από τον Yu Suzuki υπήρξε το πρώτο fighting game στην ιστορία με πλήρως πολυγωνικούς τρισδιάστατους (3D) χαρακτήρες;",
        "correct": "Virtua Fighter",
        "distractors": [
            "Tekken",
            "Battle Arena Toshinden",
            "Fighting Vipers"
        ],
        "explanation": "Το Virtua Fighter έτρεχε στην πλακέτα Sega Model 1. Αντί για sprites, χρησιμοποίησε επίπεδα (flat-shaded) 3D πολύγωνα, εισάγοντας ρεαλιστικές πολεμικές τέχνες και φυσική αντί για fireballs και υπερφυσικές δυνάμεις.",
        "funFacts": [
            "Η Sony αναγνώρισε επίσημα ότι η επιτυχία του Virtua Fighter στα arcades ήταν ο καταλύτης που την έπεισε να στραφεί ολοκληρωτικά στο 3D για το PlayStation.",
            "Χαρακτήρες όπως ο Akira Yuki και ο Jacky Bryant έγιναν εμβληματικές μορφές των arcades."
        ],
        "source": "https://en.wikipedia.org/wiki/Virtua_Fighter_(video_game)",
        "tags": ["gaming", "sega", "virtua_fighter", "yu_suzuki", "arcade"]
    },
    {
        "id": "gaming_hard_115",
        "text": "Ποιο ιστορικό arcade racing της Sega (1994) στην πλακέτα Model 2 προσέφερε φωτορεαλιστικά 3D textures στα 60 frames το δευτερόλεπτο και τραγούδια από τον Takenobu Mitsuyoshi ('Daytona, let's go away!');",
        "correct": "Daytona USA",
        "distractors": [
            "Sega Rally Championship",
            "Ridge Racer",
            "OutRunners"
        ],
        "explanation": "Το Daytona USA έθεσε νέα πρότυπα στα arcade racers με texture filtering, προηγμένο force feedback τιμόνι και υποστήριξη δικτύωσης έως και 8 καμπινών arcade για ταυτόχρονους αγώνες.",
        "funFacts": [
            "Ο συνθέτης Takenobu Mitsuyoshi ηχογράφησε μόνος του τα ξεκαρδιστικά και ενεργητικά φωνητικά του soundtrack.",
            "Υπήρξε μία από τις πιο κερδοφόρες arcade καμπίνες όλων των εποχών παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Daytona_USA_(video_game)",
        "tags": ["gaming", "sega", "daytona_usa", "arcade", "music"]
    },
    {
        "id": "gaming_hard_116",
        "text": "Ποιο real-time strategy παιχνίδι του Chris Taylor (Cavedog Entertainment, 1997) εισήγαγε για πρώτη φορά 3D έδαφος, φυσική υπολογισμού τροχιάς βλημάτων και απεριόριστη παραγωγή μονάδων βασισμένη σε ροή πόρων (Energy & Metal);",
        "correct": "Total Annihilation",
        "distractors": [
            "Command & Conquer: Tiberian Sun",
            "Warzone 2100",
            "Dark Reign"
        ],
        "explanation": "Το Total Annihilation ξεπέρασε τα τεχνικά όρια της εποχής: τα κανόνια υπολόγιζαν ύψος, απόσταση και εμπόδια, ενώ τα συντρίμμια των κατεστραμμένων μονάδων παρέμεναν στο πεδίο και μπορούσαν να ανακυκλωθούν για μέταλλο.",
        "funFacts": [
            "Το ορχηστρικό soundtrack συντέθηκε από τον Jeremy Soule (ο οποίος αργότερα έγραψε τη μουσική των The Elder Scrolls) και ηχογραφήθηκε με πλήρη συμφωνική ορχήστρα.",
            "Ο Chris Taylor δημιούργησε αργότερα τον πνευματικό διάδοχο Supreme Commander (2007)."
        ],
        "source": "https://en.wikipedia.org/wiki/Total_Annihilation",
        "tags": ["gaming", "rts", "total_annihilation", "cavedog", "pc"]
    },
    {
        "id": "gaming_hard_117",
        "text": "Ποιο επαναστατικό διαστημικό RTS της Relic Entertainment (1999) ήταν το πρώτο που προσέφερε πραγματική κίνηση και μάχη σε πλήρεις τρεις διαστάσεις (πλήρεις έξι βαθμοί ελευθερίας - 6DOF);",
        "correct": "Homeworld",
        "distractors": [
            "Haegemonia: Legions of Iron",
            "Conquest: Frontier Wars",
            "Star Wars: Empire at War"
        ],
        "explanation": "Στο Homeworld, τα σκάφη δεν κινούνταν σε επίπεδη 2D επιφάνεια αλλά σε οποιοδήποτε σημείο του τρισδιάστατου διαστημικού χώρου. Η επική ιστορία της επιστροφής των Kushan στον μητρικό τους πλανήτη Hiigara συγκίνησε εκατομμύρια παίκτες.",
        "funFacts": [
            "Η χρήση του 'Adagio for Strings' του Samuel Barber στην καταστροφή του πλανήτη Kharak θεωρείται μία από τις πιο ανατριχιαστικές στιγμές στην ιστορία των PC games.",
            "Τα σκάφη που επιβίωναν από κάθε αποστολή μεταφέρονταν στην επόμενη, κάνοντας κάθε απώλεια κρίσιμη."
        ],
        "source": "https://en.wikipedia.org/wiki/Homeworld",
        "tags": ["gaming", "homeworld", "relic", "rts", "sci_fi"]
    },
    {
        "id": "gaming_hard_118",
        "text": "Ποιο χαρακτηριστικό του UI (User Interface) στο survival horror 'Dead Space' (Visceral Games, 2008) εξάλειψε πλήρως τα παραδοσιακά μενού στην οθόνη, ενσωματώνοντας όλες τις πληροφορίες στον ίδιο τον κόσμο;",
        "correct": "Diegetic UI (μπάρα ζωής κατά μήκος της σπονδυλικής στήλης RIG και ολογράμματα όπλων)",
        "distractors": [
            "Αόρατο HUD με παλμούς δόνησης στο χειριστήριο",
            "Μίνι χάρτης αποτυπωμένος στο έδαφος με ίχνη αίματος",
            "Φωνητική ενημέρωση από τον κεντρικό υπολογιστή του Ishimura"
        ],
        "explanation": "Το Dead Space δεν είχε floating στοιχεία στην οθόνη. Η ζωή του Isaac Clarke φαινόταν στη σπονδυλική του στήλη, το οξυγόνο στην πλάτη του, τα πυρομαχικά σε ψηφιακή οθόνη πάνω στο όπλο και ο χάρτης ως τρισδιάστατο ολόγραμμα μπροστά του.",
        "funFacts": [
            "Ο Isaac Clarke πήρε το όνομά του από δύο κορυφαίους συγγραφείς επιστημονικής φαντασίας: τον Isaac Asimov και τον Arthur C. Clarke.",
            "Οι εχθροί Necromorphs απαιτούσαν στρατηγικό διαμελισμό των άκρων (strategic dismemberment) αντί για τα κλασικά headshots."
        ],
        "source": "https://en.wikipedia.org/wiki/Dead_Space_(2008_video_game)",
        "tags": ["gaming", "dead_space", "horror", "ui", "visceral"]
    },
    {
        "id": "gaming_hard_119",
        "text": "Ποιο μηχανισμό μάχης εισήγαγε το 'Bloodborne' (FromSoftware, 2015) για να ανταμείψει το επιθετικό στυλ παιχνιδιού, επιτρέποντας στον κυνηγό να ανακτήσει χαμένη ζωή αν χτυπούσε άμεσα τον εχθρό;",
        "correct": "Το σύστημα Rally (Regain system)",
        "distractors": [
            "Το σύστημα Blood Echo Surge",
            "Το Poise Counter",
            "Το Visceral Drain"
        ],
        "explanation": "Όταν ο παίκτης δέχεται ζημιά στο Bloodborne, η μπάρα ζωής εμφανίζει ένα πορτοκαλί τμήμα που υποχωρεί σταδιακά. Εάν επιτεθεί στον εχθρό μέσα σε λίγα δευτερόλεπτα, επαναφέρει τη ζωή του, ενθαρρύνοντας τη συνεχή επίθεση αντί για υποχώρηση.",
        "funFacts": [
            "Τα 'Trick Weapons' (όπως το Saw Cleaver και το Threaded Cane) είχαν δύο διαφορετικές μορφές που μπορούσαν να αλλάξουν ενδιάμεσα στα combos με το πάτημα του L1.",
            "Η ατμόσφαιρα του Bloodborne ξεκινά ως βικτοριανός γοτθικός τρόμος και μετατρέπεται σταδιακά σε καθαρό κοσμικό τρόμο εμπνευσμένο από τον H.P. Lovecraft."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodborne",
        "tags": ["gaming", "bloodborne", "fromsoftware", "miyazaki", "mechanics"]
    },
    {
        "id": "gaming_hard_120",
        "text": "Στο αριστούργημα 'NieR: Automata' (2017) του Yoko Taro, τι ζητείται από τον παίκτη να θυσιάσει οριστικά για να βοηθήσει έναν εντελώς άγνωστο παίκτη στο τελικό Ending E;",
        "correct": "Ολόκληρο το αρχείο αποθήκευσης (save file) και όλη την πρόοδο του παιχνιδιού",
        "distractors": [
            "Όλα τα όπλα και τα upgrades που μάζεψε στα 3 playthroughs",
            "Τη δυνατότητα να ξεκλειδώσει το trophy του Platinum",
            "Τον χαρακτήρα 2B από το ρόστερ του κεφαλαίου"
        ],
        "explanation": "Στο Ending E, τα credits μετατρέπονται σε ένα αδύνατο bullet-hell shmup. Όταν ο παίκτης δεχτεί βοήθεια από άλλα σκάφη παικτών, το παιχνίδι τον ρωτά αν είναι διατεθειμένος να διαγράψει για πάντα τα saves του ώστε το δικό του σκάφος να σώσει κάποιον άλλον.",
        "funFacts": [
            "Το παιχνίδι ρωτάει τον παίκτη έξι διαδοχικές φορές για να βεβαιωθεί ότι κατανοεί πως τα δεδομένα του θα χαθούν ανεπιστρεπτί.",
            "Το NieR: Automata διαθέτει συνολικά 26 διαφορετικά τέλη (ένα για κάθε γράμμα του λατινικού αλφαβήτου A-Z)."
        ],
        "source": "https://en.wikipedia.org/wiki/Nier:_Automata",
        "tags": ["gaming", "nier_automata", "yoko_taro", "square_enix", "design"]
    },
    {
        "id": "gaming_hard_121",
        "text": "Ποιο ανεξάρτητο puzzle platformer του 2008 από τον Jonathan Blow συνέβαλε καθοριστικά στην έκρηξη της σύγχρονης indie επανάστασης, χρησιμοποιώντας μηχανισμούς χειρισμού του χρόνου;",
        "correct": "Braid",
        "distractors": [
            "Limbo",
            "Super Meat Boy",
            "Fez"
        ],
        "explanation": "Στο Braid ο πρωταγωνιστής Tim αναζητά μια πριγκίπισσα σε κόσμους όπου ο χρόνος κυλά ανάποδα, συνδέεται με τη χωρική κίνηση ή δημιουργεί παράλληλες σκιές, αποκαλύπτοντας στο τέλος ένα βαθύ μεταφορικό νόημα για τη δημιουργία της ατομικής βόμβας.",
        "funFacts": [
            "Ο Jonathan Blow χρηματοδότησε το Braid με προσωπικές οικονομίες 200.000 δολαρίων και η τεράστια επιτυχία του στο Xbox Live Arcade του επέτρεψε να αναπτύξει το 'The Witness' (2016).",
            "Τα ζωγραφισμένα στο χέρι γραφικά του παιχνιδιού φιλοτεχνήθηκαν από τον καλλιτέχνη David Hellman."
        ],
        "source": "https://en.wikipedia.org/wiki/Braid_(video_game)",
        "tags": ["gaming", "braid", "indie", "jonathan_blow", "puzzle"]
    },
    {
        "id": "gaming_hard_122",
        "text": "Ποιο indie διαμάντι του Phil Fish (Polytron, 2012) περιστρεφόταν γύρω από έναν 2D κόσμο που μπορούσε να περιστραφεί σε τέσσερις τρισδιάστατες γωνίες 90 μοιρών;",
        "correct": "Fez",
        "distractors": [
            "Braid",
            "Cave Story",
            "Spelunky"
        ],
        "explanation": "Στο Fez ο Gomez αποκτά ένα μαγικό κόκκινο φέσι που του αποκαλύπτει την 3η διάσταση. Ο παίκτης περιστρέφει τον κόσμο κατά 90 μοίρες, ευθυγραμμίζοντας απομακρυσμένες πλατφόρμες για να λύσει γρίφους.",
        "funFacts": [
            "Το παιχνίδι περιείχε μια ολόκληρη κρυφή γλώσσα με ιερογλυφικά και ένα σύστημα αρίθμησης βασισμένο σε βάση 4 (quaternary).",
            "Η ταραχώδης πενταετής ανάπτυξη του Fez καταγράφηκε λεπτομερώς στο διάσημο ντοκιμαντέρ 'Indie Game: The Movie'."
        ],
        "source": "https://en.wikipedia.org/wiki/Fez_(video_game)",
        "tags": ["gaming", "fez", "indie", "phil_fish", "puzzle"]
    },
    {
        "id": "gaming_hard_123",
        "text": "Ποιος δημιουργός πέρασε τεσσεράμισι χρόνια δουλεύοντας μόνος του 10-12 ώρες την ημέρα, δημιουργώντας τα γραφικά, τον κώδικα, τη μουσική και το σενάριο του παγκόσμιου φαινομένου 'Stardew Valley' (2016);",
        "correct": "Eric Barone (ConcernedApe)",
        "distractors": [
            "Lucas Pope",
            "Toby Fox",
            "Edmund McMillen"
        ],
        "explanation": "Ο Eric Barone εμπνεύστηκε από τη σειρά Harvest Moon και ανέπτυξε εξ ολοκλήρου μόνος του το Stardew Valley σε C#. Το παιχνίδι έχει πουλήσει πάνω από 30 εκατομμύρια αντίτυπα παγκοσμίως.",
        "funFacts": [
            "Κατά τη διάρκεια της ανάπτυξης, η κοπέλα του Barone τον στήριζε οικονομικά καθώς εκείνος δούλευε ως ταξιθέτης σε θέατρο μερικής απασχόλησης.",
            "Ο Barone συνέχισε να κυκλοφορεί τεράστια δωρεάν updates περιεχομένου για χρόνια μετά την κυκλοφορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Stardew_Valley",
        "tags": ["gaming", "stardew_valley", "concernedape", "indie", "simulation"]
    },
    {
        "id": "gaming_hard_124",
        "text": "Ποιο θρυλικό, εξαιρετικά πολύπλοκο roguelike/management simulator των αδελφών Tarn και Zach Adams (Bay 12 Games), φτιαγμένο αρχικά με χαρακτήρες ASCII, αποτέλεσε την κύρια έμπνευση για τη δημιουργία του Minecraft;",
        "correct": "Dwarf Fortress (Slaves to Armok: God of Blood Chapter II)",
        "distractors": [
            "NetHack",
            "Cataclysm: Dark Days Ahead",
            "Rogue"
        ],
        "explanation": "Το Dwarf Fortress εξομοιώνει γεωλογία, ροή υγρών, θερμοκρασία, ψυχολογία και ανατομία με ανατριχιαστική λεπτομέρεια (προσομοιώνοντας μέχρι και βλέφαρα και δάχτυλα). Αποκτήθηκε από το MoMA ως έκθεμα ιστορίας της τέχνης.",
        "funFacts": [
            "Το επίσημο σύνθημα της κοινότητας του παιχνιδιού είναι 'Losing is fun!' (Το να χάνεις έχει πλάκα).",
            "Το 2022 κυκλοφόρησε επίσημη έκδοση στο Steam με ανανεωμένα γραφικά και mouse support, κάνοντας τους αδελφούς Adams εκατομμυριούχους μέσα σε μία εβδομάδα."
        ],
        "source": "https://en.wikipedia.org/wiki/Dwarf_Fortress",
        "tags": ["gaming", "dwarf_fortress", "indie", "ascii", "simulation"]
    },
    {
        "id": "gaming_hard_125",
        "text": "Ποιο μοναδικό μηχανισμό μάχης είχε το cult JRPG 'EarthBound' (Mother 2, 1994) του Shigesato Itoi, επιτρέποντας στον παίκτη να σώσει έναν χαρακτήρα από θανάσιμο χτύπημα αν προλάβαινε να θεραπευτεί πριν μηδενιστεί ο αριθμός;",
        "correct": "Οδόμετρο κυλιόμενων αριθμών HP (Rolling HP Odometer)",
        "distractors": [
            "Guts Revival Roll",
            "Time Freeze Shield",
            "Psychic Barrier Charge"
        ],
        "explanation": "Όταν ένας χαρακτήρας δεχόταν ζημιά 500 πόντων ενώ είχε 200, οι πόντοι ζωής δεν έπεφταν ακαριαία στο μηδέν αλλά κυλούσαν προς τα κάτω σαν μηχανικό κοντέρ αυτοκινήτου, δίνοντας στον παίκτη χρόνο να νικήσει τη μάχη ή να χρησιμοποιήσει healing.",
        "funFacts": [
            "Ο Shigesato Itoi είναι διάσημος κειμενογράφος, δοκιμιογράφος και ηθοποιός φωνής στην Ιαπωνία (η φωνή του πατέρα στο 'My Neighbor Totoro' του Studio Ghibli).",
            "Η αμερικανική διαφημιστική καμπάνια του EarthBound με το σύνθημα 'This game stinks!' και κάρτες scratch-and-sniff με μυρωδιά σκουπιδιών θεωρείται από τις πιο αποτυχημένες στην ιστορία της Nintendo."
        ],
        "source": "https://en.wikipedia.org/wiki/EarthBound",
        "tags": ["gaming", "snes", "earthbound", "nintendo", "rpg"]
    },
    {
        "id": "gaming_hard_126",
        "text": "Στο αριστούργημα 'Shadow of the Colossus' (2005), πώς σχεδιάστηκε η τεχνητή νοημοσύνη του αλόγου Agro από τον Fumito Ueda ώστε να μοιάζει με αληθινό ζώο;",
        "correct": "Το άλογο ακολουθεί φυσικά τα μονοπάτια και αποφεύγει εμπόδια μόνο του, αντί να είναι 'όχημα' με άμεση κατεύθυνση",
        "distractors": [
            "Το άλογο κουράζεται και αρνείται να τρέξει αν δεν ταϊστεί με φρούτα",
            "Το άλογο τρομάζει από τους κολοσσούς και τρέχει αυτόματα προς την αντίθετη κατεύθυνση",
            "Το άλογο μπορεί να ελεγχθεί μόνο με σφυρίγματα και όχι με τα χαλινάρια"
        ],
        "explanation": "Ο Ueda ήθελε το άλογο να έχει δική του προσωπικότητα. Ο παίκτης δεν οδηγεί το άλογο σαν αυτοκίνητο, αλλά του δίνει παροτρύνσεις, ενώ το Agro στρίβει μόνο του γύρω από δέντρα, γκρεμούς και βράχους.",
        "funFacts": [
            "Η σκηνή στην ετοιμόρροπη γέφυρα πριν τον 16ο κολοσσό όπου το Agro σώζει τον Wander θεωρείται από τις πιο δραματικές στιγμές του gaming.",
            "Το άλογο ονομάστηκε Agro, αλλά στα ιαπωνικά προσφωνείται ως 'Kurou' (Μαύρο)."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_of_the_Colossus",
        "tags": ["gaming", "shadow_of_the_colossus", "ueda", "playstation2", "ai"]
    },
    {
        "id": "gaming_hard_127",
        "text": "Ποιο ψυχολογικό νόημα αντιπροσωπεύει το εμβληματικό τέρας Pyramid Head (Red Pyramid Thing) στο αριστούργημα ψυχολογικού τρόμου 'Silent Hill 2' (2001);",
        "correct": "Την υποσυνείδητη επιθυμία του James Sunderland να τιμωρηθεί για τον θάνατο της συζύγου του Mary",
        "distractors": [
            "Την ενσάρκωση του αρχαίου θεού Valtiel της αίρεσης του Silent Hill",
            "Το φάντασμα του προηγούμενου επικεφαλής δήμιου της πόλης",
            "Τους σεξουαλικούς φόβους της Angela Orosco"
        ],
        "explanation": "Ο σχεδιαστής πλασμάτων Masahiro Ito δημιούργησε τον Pyramid Head αποκλειστικά ως εκδηλωμένη εκδήλωση της ενοχής και της ανάγκης για αυτοτιμωρία του James Sunderland, λόγος για τον οποίο το τέρας αυτοκτονεί όταν ο James αποδέχεται την πράξη του.",
        "funFacts": [
            "Ο Masahiro Ito εξέφρασε συχνά τη λύπη του για το γεγονός ότι η Konami μετέτρεψε τον Pyramid Head σε γενικό 'μπαμπούλα' της σειράς σε μεταγενέστερα παιχνίδια και ταινίες.",
            "Το Silent Hill 2 διαθέτει 6 διαφορετικά τέλη, συμπεριλαμβανομένου του ξεκαρδιστικού 'Dog Ending' όπου ένας σκύλος Shiba Inu χειρίζεται τα πάντα από ένα δωμάτιο ελέγχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_2",
        "tags": ["gaming", "silenthill", "konami", "horror", "pyramid_head"]
    },
    {
        "id": "gaming_hard_128",
        "text": "Ποιος Ιάπωνας δημιουργός σχεδίασε το 'The Legend of Zelda: Majora's Mask' (2000), ολοκληρώνοντας την ανάπτυξη ενός από τα πιο σκοτεινά παιχνίδια της Nintendo μέσα σε μόλις 14 μήνες;",
        "correct": "Eiji Aonuma",
        "distractors": [
            "Shigeru Miyamoto",
            "Takashi Tezuka",
            "Kensuke Tanabe"
        ],
        "explanation": "Ο Shigeru Miyamoto προκάλεσε τον Aonuma να φτιάξει ένα Master Quest για το Ocarina of Time ή ένα εντελώς νέο Zelda μέσα σε έναν μόνο χρόνο. Ο Aonuma επέλεξε το νέο παιχνίδι, επινοώντας τον επαναλαμβανόμενο κύκλο των 3 ημερών στην Termina.",
        "funFacts": [
            "Ο Aonuma παραδέχτηκε ότι έβλεπε συνεχώς εφιάλτες ότι τον καταδίωκε η πτώση της Σελήνης λόγω της αφόρητης πίεσης του χρονοδιαγράμματος.",
            "Κάθε κάτοικος του Clock Town έχει ένα αυστηρό πρόγραμμα 72 ωρών με τις δικές του προσωπικές αγωνίες μπροστά στο επικείμενο τέλος του κόσμου."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Majora%27s_Mask",
        "tags": ["gaming", "zelda", "nintendo64", "aonuma", "majoras_mask"]
    },
    {
        "id": "gaming_hard_129",
        "text": "Ποιος κορυφαίος concept artist και art director (σχεδιαστής της City 17 στο Half-Life 2) σχεδίασε τη φαλαινοθηρική steampunk πόλη Dunwall στο 'Dishonored' (2012) της Arkane Studios;",
        "correct": "Viktor Antonov",
        "distractors": [
            "Moebius (Jean Giraud)",
            "Syd Mead",
            "H.R. Giger"
        ],
        "explanation": "Ο Βούλγαρος καλλιτέχνης Viktor Antonov δημιούργησε την εκπληκτική αισθητική του Dunwall, συνδυάζοντας το βικτοριανό Λονδίνο του 19ου αιώνα με φουτουριστική τεχνολογία που τροφοδοτείται από λάδι φάλαινας (whale oil).",
        "funFacts": [
            "Το σύστημα 'Chaos' του Dishonored άλλαζε τον κόσμο: όσο περισσότερους ανθρώπους σκότωνε ο Corvo Attano, τόσο περισσότεροι αρουραίοι, πανούκλα και κλαίοντες (weepers) εμφανίζονταν στην πόλη.",
            "Ο παίκτης μπορεί να τερματίσει ολόκληρο το Dishonored χωρίς να σκοτώσει ούτε έναν άνθρωπο, εξουδετερώνοντας ακόμα και τους βασικούς στόχους με ποιητικές εναλλακτικές τιμωρίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Dishonored",
        "tags": ["gaming", "dishonored", "arkane", "viktor_antonov", "stealth"]
    },
    {
        "id": "gaming_hard_130",
        "text": "Ποιο boss στο αρχικό 'Dark Souls' (2011) παραδέχτηκε δημόσια ο Hidetaka Miyazaki ότι αποτελεί το μεγαλύτερο σχεδιαστικό λάθος και αποτυχία της καριέρας του;",
        "correct": "The Bed of Chaos (Η Κοιτίδα του Χάους)",
        "distractors": [
            "Dragon Slayer Ornstein & Executioner Smough",
            "Capra Demon",
            "Ceaseless Discharge"
        ],
        "explanation": "Το Bed of Chaos στο Lost Izalith βασιζόταν σε platforming μηχανισμούς και σαρώσεις χεριών που έριχναν τον παίκτη σε τρύπες του δαπέδου για στιγμιαίο θάνατο, αποκλίνοντας πλήρως από τη φιλοσοφία μάχης της σειράς Souls.",
        "funFacts": [
            "Λόγω πίεσης χρόνου πριν την κυκλοφορία, ολόκληρη η περιοχή Lost Izalith έμεινε ημιτελής με δεκάδες αντίγραφα δεινοσαύρων (Bounding Demons) τοποθετημένα πρόχειρα στη λάβα.",
            "Είναι το μοναδικό boss στο Dark Souls όπου η πρόοδος καταστροφής των δύο πυρήνων αποθηκεύεται ακόμη κι αν ο παίκτης πεθάνει."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "fromsoftware", "miyazaki", "bosses"]
    },
    {
        "id": "gaming_hard_131",
        "text": "Ποιος μοναδικός μηχανισμός του 'Demon's Souls' (2009) άλλαζε τα στατιστικά των εχθρών, άνοιγε μυστικά περάσματα και εμφάνιζε Black Phantoms ανάλογα με το αν ο παίκτης πέθαινε σε ανθρώπινη μορφή;",
        "correct": "World Tendency (Τάση Κόσμου: Pure White ή Pure Black)",
        "distractors": [
            "Humanity Meter",
            "Insight Level",
            "Hollowing Curse"
        ],
        "explanation": "Στο World Tendency, κάθε θάνατος του παίκτη σε μορφή σώματος (Body Form) έσπρωχνε τον κόσμο προς το Pure Black, κάνοντας τους εχθρούς εξαιρετικά ισχυρούς αλλά αυξάνοντας το drop rate σπάνιων αντικειμένων (όπως το Pure Bladestone).",
        "funFacts": [
            "Πολλοί έμπειροι παίκτες αυτοκτονούσαν σκόπιμα στο ασφαλές Nexus για να παίζουν στους κόσμους μόνο ως ψυχές (Soul Form), ώστε να μην αλλοιώνουν την τάση του κόσμου προς το μαύρο.",
            "Οι servers της Sony επηρέαζαν επίσης το World Tendency παγκοσμίως σε ειδικά events (π.χ. Halloween)."
        ],
        "source": "https://en.wikipedia.org/wiki/Demon%27s_Souls",
        "tags": ["gaming", "demons_souls", "fromsoftware", "mechanics", "playstation"]
    },
    {
        "id": "gaming_hard_132",
        "text": "Ποιο τραγούδι-ορόσημο της μάχης με τον Sans στο 'Undertale' (2015) είχε αρχικά συντεθεί από τον Toby Fox το 2008 για ένα ROM hack του EarthBound ('Halloween Hack');",
        "correct": "Megalovania",
        "distractors": [
            "Hopes and Dreams",
            "Bonetrousle",
            "Death by Glamour"
        ],
        "explanation": "Ο Toby Fox συνέθεσε το Megalovania για το EarthBound Halloween Hack, το χρησιμοποίησε αργότερα στο webcomic Homestuck και τελικά το απογείωσε στο Undertale, κάνοντάς το ένα από τα πιο διάσημα video game tracks του 21ου αιώνα.",
        "funFacts": [
            "Το Megalovania παίχτηκε επίσημα ενώπιον του Πάπα Φραγκίσκου στο Βατικανό το 2022 από μια ομάδα τσίρκου.",
            "Ο Toby Fox ανέπτυξε σχεδόν ολόκληρο το Undertale μόνος του χρησιμοποιώντας τη μηχανή GameMaker: Studio."
        ],
        "source": "https://en.wikipedia.org/wiki/Undertale",
        "tags": ["gaming", "undertale", "toby_fox", "music", "indie"]
    },
    {
        "id": "gaming_hard_133",
        "text": "Ποιο διάσημο platformer του 2018 από τη Maddy Thorson ανέπτυξε μια τεράστια κοινότητα speedrunning γύρω από ακραίες τεχνικές κίνησης όπως το 'Wavedashing' και το 'Hyper Dashing';",
        "correct": "Celeste",
        "distractors": [
            "Super Meat Boy",
            "The End Is Nigh",
            "VVVVVV"
        ],
        "explanation": "Στο Celeste η Madeline σκαρφαλώνει το βουνό Celeste αντιμετωπίζοντας τις κρίσεις πανικού και την κατάθλιψή της. Το wavedashing (dash διαγώνια στο έδαφος και άλμα) διδάσκεται επίσημα στο εξαιρετικά δύσκολο Chapter 9 (Farewell).",
        "funFacts": [
            "Το συγκλονιστικό soundtrack του Celeste συντέθηκε από τη Lena Raine, η οποία αργότερα συνέθεσε μουσική και για το Minecraft.",
            "Το παιχνίδι ξεκίνησε ως ένα πρωτότυπο 30 επιπέδων που φτιάχτηκε μέσα σε 4 ημέρες για την εικονική κονσόλα PICO-8."
        ],
        "source": "https://en.wikipedia.org/wiki/Celeste_(video_game)",
        "tags": ["gaming", "celeste", "indie", "platformer", "speedrun"]
    },
    {
        "id": "gaming_hard_134",
        "text": "Ποιο studio από την Αδελαΐδα της Αυστραλίας, αποτελούμενο από μόλις τρία άτομα (Team Cherry), δημιούργησε το αριστουργηματικό hand-drawn metroidvania 'Hollow Knight' (2017);",
        "correct": "Team Cherry (Ari Gibson, William Pellen, Jack Vine)",
        "distractors": [
            "Moon Studios",
            "Housemarque",
            "Motion Twin"
        ],
        "explanation": "Η Team Cherry χρηματοδότησε το Hollow Knight μέσω Kickstarter μαζεύοντας μόλις 57.000 δολάρια Αυστραλίας, δημιουργώντας έναν τεράστιο, σκοτεινό και μελαγχολικό υπόγειο κόσμο εντόμων (Hallownest) με δεκάδες bosses.",
        "funFacts": [
            "Όλα τα animations και τα περιβάλλοντα του Hollow Knight σχεδιάστηκαν παραδοσιακά στο χέρι από τον Ari Gibson.",
            "Η αναμονή για το sequel 'Hollow Knight: Silksong' έγινε ένα από τα πιο διάσημα memes σε όλες τις παρουσιάσεις Nintendo Direct και Xbox Showcases."
        ],
        "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
        "tags": ["gaming", "hollow_knight", "team_cherry", "indie", "metroidvania"]
    },
    {
        "id": "gaming_hard_135",
        "text": "Ποιο ήταν το πρώτο παιχνίδι στη σειρά Pokémon (Generation II, Gold & Silver, 1999) που εισήγαγε τα εξαιρετικά σπάνια 'Shiny Pokémon' με διαφορετικό χρωματισμό και λάμψη;",
        "correct": "Pokémon Gold και Silver (με το εμβληματικό Red Gyarados στη Lake of Rage)",
        "distractors": [
            "Pokémon Ruby και Sapphire",
            "Pokémon Yellow",
            "Pokémon Crystal"
        ],
        "explanation": "Στη δεύτερη γενιά, η πιθανότητα εμφάνισης ενός Shiny Pokémon στη φύση ήταν 1 στις 8.192 (καθοριζόταν από συγκεκριμένους συνδυασμούς Individual Values / DVs). Το Κόκκινο Gyarados ήταν το πρώτο εγγυημένο Shiny στην ιστορία.",
        "funFacts": [
            "Στη Generation VI (X και Y), η βασική πιθανότητα για shiny Pokémon αυξήθηκε σε 1 στις 4.096.",
            "Η μέθοδος Masuda (αναπαραγωγή Pokémon διαφορετικών γλωσσικών εκδόσεων) αυξάνει δραστικά τις πιθανότητες γέννησης shiny."
        ],
        "source": "https://en.wikipedia.org/wiki/Pok%C3%A9mon_Gold_and_Silver",
        "tags": ["gaming", "pokemon", "gameboy", "nintendo", "shiny"]
    },
    {
        "id": "gaming_hard_136",
        "text": "Ποιο πρωτοποριακό first-person parkour action game της DICE (2008) χρησιμοποίησε το 'Runner Vision' (έντονο κόκκινο χρώμα σε σωλήνες, ράμπες και πόρτες) για να καθοδηγεί τον παίκτη χωρίς να διακόπτεται η ορμή του;",
        "correct": "Mirror's Edge",
        "distractors": [
            "Brink",
            "Titanfall",
            "Dying Light"
        ],
        "explanation": "Στο Mirror's Edge η Faith Connors τρέχει στις ταράτσες μιας αποστειρωμένης ουτοπικής πόλης. Το Runner Vision επισήμαινε με ζωηρό κόκκινο χρώμα τα αντικείμενα αλληλεπίδρασης, επιτρέποντας στον παίκτη να διατηρεί το momentum χωρίς να χάνεται.",
        "funFacts": [
            "Η DICE χρησιμοποίησε το σύστημα φωτισμού Beast για να δημιουργήσει την εκθαμβωτική, κατάλευκη μινιμαλιστική αισθητική της πόλης.",
            "Το τραγούδι των τίτλων 'Still Alive' ερμηνεύτηκε από τη Σουηδή τραγουδίστρια Lisa Miskovsky και έγινε τεράστια επιτυχία."
        ],
        "source": "https://en.wikipedia.org/wiki/Mirror%27s_Edge",
        "tags": ["gaming", "mirrors_edge", "dice", "parkour", "ea"]
    },
    {
        "id": "gaming_hard_137",
        "text": "Στο 'Assassin's Creed' (2007), ποια ήταν η εξήγηση στο lore για το γεγονός ότι ο Altaïr Ibn-La'Ahad πέθαινε ακαριαία μόλις έπεφτε σε βαθύ νερό;",
        "correct": "Σφάλμα κώδικα (glitch) στο λογισμικό της μηχανής Animus 1.0",
        "distractors": [
            "Το βάρος της πανοπλίας και των κρυφών λεπίδων του",
            "Το παιδικό τραύμα του Altair και η υδροφοβία του",
            "Η απαγόρευση του νερού από το δόγμα των Ασσασίνων"
        ],
        "explanation": "Επειδή η ομάδα ανάπτυξης της Ubisoft δεν πρόλαβε να προγραμματίσει animations κολύμβησης για το πρώτο παιχνίδι, έγραψαν στο lore ότι το Animus 1.0 είχε ένα bug που αποσυγχρόνιζε τον πρόγονο μόλις βρεχόταν. Ο Ezio στο AC2 μπορούσε να κολυμπήσει κανονικά χάρη στο 'Animus 2.0'.",
        "funFacts": [
            "Το Assassin's Creed ξεκίνησε την ανάπτυξή του ως spin-off του Prince of Persia με τίτλο 'Prince of Persia: Assassins'.",
            "Ο Altair έκοβε το παράμεσο δάχτυλό του για να μπορεί να εκτείνεται η κρυφή λεπίδα (Hidden Blade) χωρίς να το τραυματίζει."
        ],
        "source": "https://en.wikipedia.org/wiki/Assassin%27s_Creed_(video_game)",
        "tags": ["gaming", "assassins_creed", "ubisoft", "lore", "animus"]
    },
    {
        "id": "gaming_hard_138",
        "text": "Ποιο tactical RPG της Sega στο PlayStation 3 (2008) χρησιμοποίησε την πανέμορφη μηχανή γραφικών CANVAS, κάνοντας κάθε καρέ του παιχνιδιού να μοιάζει με κινούμενη υδατογραφία σχεδιασμένη με χρωματιστά μολύβια;",
        "correct": "Valkyria Chronicles (Senjō no Valkyria)",
        "distractors": [
            "Resonance of Fate",
            "Eternal Sonata",
            "Ni no Kuni"
        ],
        "explanation": "Η מכανή CANVAS της Sega απέδιδε απαλά παστέλ χρώματα, περιγράμματα μολυβιού και ηχομιμητικές λέξεις (ονοματοποιίες όπως 'DODODODO') που εμφανίζονταν στην οθόνη σαν ιαπωνικό manga κατά τη διάρκεια των μαχών.",
        "funFacts": [
            "Το σύστημα μάχης BLiTZ συνδύαζε turn-based στρατηγική στον χάρτη με real-time κίνηση τρίτου προσώπου κατά τον έλεγχο κάθε στρατιώτη.",
            "Η ιστορία διαδραματίζεται σε μια εναλλακτική εκδοχή της Ευρώπης της δεκαετίας του 1930 (Europa) με επίκεντρο το μικρό πριγκιπάτο της Gallia."
        ],
        "source": "https://en.wikipedia.org/wiki/Valkyria_Chronicles",
        "tags": ["gaming", "sega", "valkyria_chronicles", "playstation3", "art"]
    },
    {
        "id": "gaming_hard_139",
        "text": "Ποιο franchise παιχνιδιών platform της Sega δημιουργήθηκε το 1991 ως η επίσημη απάντηση στον Mario της Nintendo, με τον Yuji Naka να προγραμματίζει έναν πρωτοποριακό αλγόριθμο ομαλής περιστροφής σε καμπύλες και loop-de-loops;",
        "correct": "Sonic the Hedgehog",
        "distractors": [
            "Alex Kidd",
            "Ristar",
            "Dynamite Headdy"
        ],
        "explanation": "Ο Yuji Naka ανέπτυξε έναν αλγόριθμο φυσικής που επέτρεπε σε ένα sprite να κινείται σε καμπύλες επιφάνειες και να διατηρεί την ορμή του σε ανάποδους βρόχους 360 μοιρών. Ο σχεδιαστής Naoto Ohshima δημιούργησε τον μπλε σκαντζόχοιρο Sonic.",
        "funFacts": [
            "Ο Sonic σχεδιάστηκε μπλε για να ταιριάζει με το μπλε εταιρικό λογότυπο της Sega, ενώ τα κόκκινα παπούτσια του εμπνεύστηκαν από τις μπότες του Michael Jackson στο άλμπουμ Bad.",
            "Το Sega Genesis διαφημίστηκε στην Αμερική με το θρυλικό σλόγκαν 'Genesis does what Nintendon't' χάρη στην ταχύτητα του Sonic (Blast Processing)."
        ],
        "source": "https://en.wikipedia.org/wiki/Sonic_the_Hedgehog",
        "tags": ["gaming", "sega", "sonic", "genesis", "retro"]
    },
    {
        "id": "gaming_hard_140",
        "text": "Για ποιο λόγο ο Shigeru Miyamoto δεν μπόρεσε να συμπεριλάβει τον δεινόσαυρο Yoshi στο αρχικό 'Super Mario Bros.' (1985) στο NES, αναμένοντας την κυκλοφορία του SNES και του 'Super Mario World' (1990);",
        "correct": "Λόγω των τεχνικών περιορισμών μνήμης και επεξεργασίας sprites του NES",
        "distractors": [
            "Επειδή η Nintendo δεν είχε κατοχυρώσει τα εμπορικά δικαιώματα για δεινόσαυρους",
            "Λόγω διαφωνίας με τον σχεδιαστή χαρακτήρων Shigefumi Hino",
            "Επειδή ο Mario προοριζόταν αρχικά να καβαλάει ένα μηχανικό άλογο"
        ],
        "explanation": "Ο Miyamoto ήθελε από την αρχή ο Mario να ιππεύει έναν δεινόσαυρο. Το NES όμως δεν μπορούσε να διαχειριστεί ταυτόχρονα το μεγάλο sprite του Mario πάνω σε άλλο πλάσμα χωρίς σοβαρό flickering και πτώση framerate, κάτι που έγινε εφικτό μόνο με το ισχυρότερο hardware του Super Nintendo.",
        "funFacts": [
            "Το πλήρες επίσημο όνομα του Yoshi σύμφωνα με οδηγό της Nintendo είναι 'T. Yoshisaur Munchakoopas'.",
            "Στο αρχικό σχέδιο του Super Mario World, ο Mario δεν έδειχνε με το δάχτυλο μπροστά αλλά χτυπούσε απαλά τον Yoshi στο πίσω μέρος του κεφαλιού για να βγάλει τη γλώσσα του."
        ],
        "source": "https://en.wikipedia.org/wiki/Yoshi",
        "tags": ["gaming", "mario", "yoshi", "nintendo", "snes"]
    },
    {
        "id": "gaming_hard_141",
        "text": "Ποιο ιστορικό fighting game της Capcom (1998) εισήγαγε το σύστημα των τριών 'ISMs' (A-ISM, V-ISM, X-ISM), επιτρέποντας στους παίκτες να διαλέγουν διαφορετικό στυλ σούπερ κινήσεων και custom combos;",
        "correct": "Street Fighter Alpha 3",
        "distractors": [
            "Street Fighter III: 2nd Impact",
            "Capcom vs. SNK 2",
            "Super Street Fighter II Turbo"
        ],
        "explanation": "Στο Street Fighter Alpha 3, το X-ISM πρόσφερε απλή παραδοσιακή μπάρα SF2 με μεγάλη ζημιά, το A-ISM τη στάνταρ μπάρα 3 επιπέδων της σειράς Alpha, και το V-ISM τα περίφημα Custom Combos που επέτρεπαν ελεύθερη αλυσίδα χτυπημάτων.",
        "funFacts": [
            "Το V-ISM κυριάρχησε στα τουρνουά υψηλού επιπέδου επειδή επέτρεπε άπειρα ή σχεδόν αναπόφευκτα unblockable combos σε έμπειρα χέρια.",
            "Η έκδοση του PlayStation 1 περιλάμβανε το τεράστιο single-player mode 'World Tour' όπου ο παίκτης δυνάμωνε τον μαχητή του."
        ],
        "source": "https://en.wikipedia.org/wiki/Street_Fighter_Alpha_3",
        "tags": ["gaming", "street_fighter", "capcom", "fighting_games", "mechanics"]
    },
    {
        "id": "gaming_hard_142",
        "text": "Ποιο ήταν το πρώτο fighting game της σειράς Tekken (1997 στα arcades, 1998 στο PS1) που εισήγαγε ουσιαστική τρισδιάστατη κίνηση στο βάθος με ελαφρύ πάτημα πάνω/κάτω (sidestepping) και παρουσίασε για πρώτη φορά τον Jin Kazama;",
        "correct": "Tekken 3",
        "distractors": [
            "Tekken 2",
            "Tekken Tag Tournament",
            "Tekken 4"
        ],
        "explanation": "Το Tekken 3 μείωσε το ύψος των αλμάτων και καθιέρωσε το sidestep, κάνοντας τη μάχη πραγματικά τρισδιάστατη. Πούλησε πάνω από 8 εκατομμύρια αντίτυπα στο PlayStation 1 και θεωρείται ένα από τα κορυφαία fighting games όλων των εποχών.",
        "funFacts": [
            "Το Tekken 3 περιλάμβανε δύο θρυλικά minigames: το Tekken Force (side-scrolling beat 'em up) και το Tekken Ball (beach volley με μπουνιές).",
            "Ο Dr. Bosconovitch και ο μικροσκοπικός δεινόσαυρος Gon ήταν μυστικοί ξεκλείδωτοι χαρακτήρες στην έκδοση του PS1."
        ],
        "source": "https://en.wikipedia.org/wiki/Tekken_3",
        "tags": ["gaming", "tekken", "namco", "playstation", "fighting_games"]
    },
    {
        "id": "gaming_hard_143",
        "text": "Ποια διάσημη σειρά ιαπωνικών rhythm arcade games της Konami, που ξεκίνησε το 1998, έφερε επανάσταση στα arcades παγκοσμίως απαιτώντας από τους παίκτες να πατούν φωτιζόμενα βέλη με τα πόδια σε μια μεταλλική πλατφόρμα;",
        "correct": "Dance Dance Revolution (DDR)",
        "distractors": [
            "Pump It Up",
            "ParaParaParadise",
            "In the Groove"
        ],
        "explanation": "Το Dance Dance Revolution της θυγατρικής BEMANI της Konami δημιούργησε ένα παγκόσμιο πολιτιστικό φαινόμενο, συνδυάζοντας ηλεκτρονική dance μουσική (Dancemania Eurobeat) με έντονη σωματική άσκηση.",
        "funFacts": [
            "Το DDR εντάχθηκε σε προγράμματα φυσικής αγωγής σε εκατοντάδες σχολεία στις ΗΠΑ για την καταπολέμηση της παιδικής παχυσαρκίας.",
            "Κορυφαίοι παίκτες μπορούν να εκτελέσουν πάνω από 10-15 βήματα το δευτερόλεπτο σε τραγούδια επιπέδου 'Megalovania' ή 'MAX 300'."
        ],
        "source": "https://en.wikipedia.org/wiki/Dance_Dance_Revolution",
        "tags": ["gaming", "konami", "bemani", "ddr", "arcade"]
    },
    {
        "id": "gaming_hard_144",
        "text": "Στο 'SimCity 2000' (1993) της Maxis, ποιο μυστηριώδες μήνυμα εμφανιζόταν συχνά στην οθόνη φόρτωσης και έγινε εσωτερικό αστείο σε όλα τα μετέπειτα παιχνίδια του Will Wright και της Maxis;",
        "correct": "Reticulating Splines",
        "distractors": [
            "Simulating Citizens",
            "Constructing Arcologies",
            "Calibrating Disasters"
        ],
        "explanation": "Ο Will Wright παραδέχτηκε ότι η φράση 'Reticulating Splines' δεν σήμαινε απολύτως τίποτα στον κώδικα του παιχνιδιού. Απλώς ακουγόταν εντυπωσιακή και επιστημονική, γι' αυτό και την έβαλαν για να διασκεδάζει τους παίκτες κατά το loading.",
        "funFacts": [
            "Η φράση εμφανίστηκε έκτοτε σχεδόν σε κάθε παιχνίδι The Sims, SimCity και Spore.",
            "Στο SimCity 2000 οι παίκτες μπορούσαν να χτίσουν τεράστιες φουτουριστικές αυτάρκεις πόλεις μέσα σε ένα μόνο κτίριο, γνωστές ως Arcologies."
        ],
        "source": "https://en.wikipedia.org/wiki/SimCity_2000",
        "tags": ["gaming", "maxis", "simcity", "will_wright", "humor"]
    },
    {
        "id": "gaming_hard_145",
        "text": "Ποιος διάσημος ηχητικός ψαλμός των ιερέων στο αρχικό 'Age of Empires' (1997) της Ensemble Studios έγινε ένα από τα πιο αναγνωρίσιμα ηχητικά memes στην ιστορία του PC gaming κατά τη μεταστροφή εχθρικών μονάδων;",
        "correct": "Wololo (Ayoyo / Wololo)",
        "distractors": [
            "Roggan",
            "Erectus",
            "Habadacus"
        ],
        "explanation": "Όταν ένας ιερέας του Age of Empires πλησίαζε μια εχθρική μονάδα για να την προσηλυτίσει, έψαλλε το 'Wololo', αλλάζοντας το χρώμα της μονάδας στο χρώμα της δικής του ομάδας.",
        "funFacts": [
            "Η φράση 'Wololo' ηχογραφήθηκε από μέλη της ομάδας ανάπτυξης της Ensemble Studios στο μπάνιο των γραφείων τους για καλύτερη ακουστική αντήχηση.",
            "Η Microsoft συμπεριέλαβε το Wololo ως ειδικό cheat code και taunt (#30) σε όλες τις επανεκδόσεις Definitive Edition."
        ],
        "source": "https://en.wikipedia.org/wiki/Age_of_Empires_(video_game)",
        "tags": ["gaming", "age_of_empires", "microsoft", "meme", "rts"]
    },
    {
        "id": "gaming_hard_146",
        "text": "Ποιο franchise παιχνιδιών δράσης stealth της Konami, δημιουργία του Hideo Kojima το 1987 στο MSX2, γεννήθηκε αρχικά επειδή το hardware του υπολογιστή δεν μπορούσε να υποστηρίξει ταυτόχρονα πολλούς πυροβολισμούς και εχθρούς στην οθόνη;",
        "correct": "Metal Gear",
        "distractors": [
            "Snatcher",
            "Policenauts",
            "Castlevania"
        ],
        "explanation": "Η Konami ζήτησε από τον νεαρό Kojima να φτιάξει ένα action πολεμικό shooter. Επειδή το MSX2 είχε όριο στα sprites ανά γραμμή και κολλούσε όταν έπεφταν σφαίρες, ο Kojima σκέφτηκε να φτιάξει ένα παιχνίδι όπου ο στόχος δεν θα ήταν να πυροβολείς, αλλά να αποφεύγεις τη μάχη.",
        "funFacts": [
            "Η αρχική έμπνευση του Kojima για την απόδραση και την αποφυγή των φρουρών ήταν η κλασική πολεμική ταινία 'Η Μεγάλη Απόδραση' (The Great Escape, 1963).",
            "Το κουτί από χαρτόνι (Cardboard Box) εμφανίστηκε ήδη από το πρώτο Metal Gear του 1987 ως μέσο απόκρυψης."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_(video_game)",
        "tags": ["gaming", "metal_gear", "kojima", "msx", "stealth"]
    },
    {
        "id": "gaming_hard_147",
        "text": "Ποια διάσημη μέθοδος σωτηρίας εφαρμόζεται στο puzzle game 'Ico' (2001) της Sony Japan, όπου ο παίκτης μπορεί να αποθηκεύσει την πρόοδό του μόνο αν καθίσει μαζί με τη Yorda σε ένα συγκεκριμένο αντικείμενο;",
        "correct": "Σε έναν πέτρινο καναπέ / παγκάκι για δύο άτομα",
        "distractors": [
            "Μπροστά σε ένα αναμμένο τζάκι",
            "Δίπλα σε ένα ιερό άγαλμα περιστεριού",
            "Μέσα σε μια ξύλινη βάρκα στη λίμνη"
        ],
        "explanation": "Για να κάνει save ο παίκτης στο Ico, έπρεπε να οδηγήσει τη Yorda σε έναν πέτρινο καναπέ και να καθίσουν δίπλα-δίπλα. Το animation τους έδειχνε να αποκοιμιούνται απαλά ο ένας δίπλα στον άλλον.",
        "funFacts": [
            "Εάν ο Ico καθίσει μόνος του στον καναπέ χωρίς τη Yorda, δεν μπορεί να αποθηκεύσει το παιχνίδι.",
            "Το ευρωπαϊκό εξώφυλλο του Ico ζωγραφίστηκε από τον ίδιο τον Fumito Ueda, εμπνευσμένο άμεσα από το σουρεαλιστικό στυλ του Giorgio de Chirico."
        ],
        "source": "https://en.wikipedia.org/wiki/Ico",
        "tags": ["gaming", "ico", "ueda", "playstation2", "art"]
    },
    {
        "id": "gaming_hard_148",
        "text": "Ποια ήταν η πρώτη εμπορική οικιακή κονσόλα video games στην ιστορία, σχεδιασμένη από τον Ralph Baer και την ομάδα του στη Sanders Associates και κυκλοφορημένη το 1972;",
        "correct": "Magnavox Odyssey",
        "distractors": [
            "Atari 2600",
            "Fairchild Channel F",
            "Coleco Telstar"
        ],
        "explanation": "Η Magnavox Odyssey (βασισμένη στο πρωτότυπο 'Brown Box' του Ralph Baer) δεν είχε επεξεργαστή ή λογισμικό, αλλά αναλογικά και ψηφιακά κυκλώματα από τρανζίστορ και διόδους. Χρησιμοποιούσε πλαστικές διαφάνειες που κολλούσαν στην οθόνη της τηλεόρασης για χρώμα και γραφικά.",
        "funFacts": [
            "Ο Ralph Baer αναγνωρίζεται παγκοσμίως ως ο 'Πατέρας των Βιντεοπαιχνιδιών' και τιμήθηκε με το Εθνικό Μετάλλιο Τεχνολογίας των ΗΠΑ.",
            "Η Odyssey συνοδευόταν από χάρτινα χρήματα, ζάρια και κάρτες ερωτήσεων, συνδυάζοντας το ηλεκτρονικό παιχνίδι με επιτραπέζιο."
        ],
        "source": "https://en.wikipedia.org/wiki/Magnavox_Odyssey",
        "tags": ["gaming", "odyssey", "ralph_baer", "retro", "history"]
    },
    {
        "id": "gaming_hard_149",
        "text": "Ποιο arcade shooter της Taito το 1979 (δημιουργία του Tomohiro Nishikado) θεωρείται το πρώτο παιχνίδι στην ιστορία που εμφάνισε ορατή γραμμή υγείας (Health Bar) και cutscenes μεταξύ επιπέδων;",
        "correct": "Space Chaser",
        "distractors": [
            "Galaxian",
            "Asteroids",
            "Lunar Lander"
        ],
        "explanation": "Αν και συχνά πιστώνεται στο Dragon Buster (1984) της Namco για τα action platformers, το Space Chaser της Taito χρησιμοποίησε πρώτο ένα γραφικό μετρητή καυσίμων/ζωής που μειωνόταν και απλές μεταβάσεις cutscenes.",
        "funFacts": [
            "Το 'Dragon Buster' (1984) ήταν εκείνο που καθιέρωσε οριστικά τη μπάρα ζωής στα action RPGs.",
            "Πριν την εμφάνιση της μπάρας υγείας, σχεδόν όλα τα arcade παιχνίδια λειτουργούσαν με σύστημα άμεσου θανάτου σε ένα χτύπημα (one-hit kill) και αριθμό ζωών."
        ],
        "source": "https://en.wikipedia.org/wiki/Health_(game_mechanic)",
        "tags": ["gaming", "arcade", "taito", "mechanics", "history"]
    },
    {
        "id": "gaming_hard_150",
        "text": "Ποιο franchise παιχνιδιών δράσης της Capcom σχεδίασε ο Tokuro Fujiwara το 1985 (Ghosts 'n Goblins), διαβόητο για την εξωφρενική δυσκολία του και το γεγονός ότι απαιτούσε από τον παίκτη να τερματίσει το παιχνίδι δύο συνεχόμενες φορές για να δει το πραγματικό τέλος;",
        "correct": "Ghosts 'n Goblins (Makaimura)",
        "distractors": [
            "Ghouls 'n Ghosts",
            "Castlevania",
            "Ninja Gaiden"
        ],
        "explanation": "Στο τέλος του πρώτου playthrough, το παιχνίδι ενημερώνει ψυχρά τον παίκτη ότι η μάχη ήταν μια 'ψευδαίσθηση του Σατανά' και τον στέλνει πίσω στην αρχή του πρώτου επιπέδου. Μόνο νικώντας ξανά ολόκληρο το παιχνίδι με το όπλο Goddess Bracelet ξεκλείδωνε το αληθινό τέλος.",
        "funFacts": [
            "Ο Arthur χάνει την πανοπλία του με ένα χτύπημα και τρέχει φορώντας μόνο το χαρακτηριστικό πουά εσώρουχό του.",
            "Θεωρείται ευρέως ένα από τα πιο σαδιστικά δύσκολα παιχνίδια στην ιστορία των arcade και του NES."
        ],
        "source": "https://en.wikipedia.org/wiki/Ghosts_%27n_Goblins",
        "tags": ["gaming", "capcom", "ghosts_n_goblins", "arcade", "retro"]
    },
    {
        "id": "gaming_hard_151",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού online marketplace στο 'Diablo III' (2012) που επέτρεπε στους παίκτες να αγοράζουν και να πωλούν in-game όπλα με πραγματικά χρήματα, προκαλώντας τεράστιες αντιδράσεις μέχρι την οριστική κατάργησή του από τη Blizzard;",
        "correct": "Real-Money Auction House (RMAH)",
        "distractors": [
            "Sanctuary Black Market",
            "Battle.net Item Exchange",
            "Gold & Gear Bazaar"
        ],
        "explanation": "Το Real-Money Auction House κατέστρεψε την εμπειρία εύρεσης loot, καθώς ήταν ευκολότερο να αγοράσει κανείς εξοπλισμό με ευρώ ή δολάρια παρά να παίξει. Ο σκηνοθέτης Josh Mosqueira το κατάργησε πλήρως με το expansion 'Reaper of Souls' (2014).",
        "funFacts": [
            "Ένα σπάνιο όπλο (Echoing Fury) πουλήθηκε στο Auction House για το ποσό-ρεκόρ των 14.000 δολαρίων ΗΠΑ.",
            "Η Blizzard παραδέχτηκε αργότερα ότι το RMAH ήταν το μεγαλύτερο σχεδιαστικό λάθος στην ιστορία του franchise Diablo."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_III",
        "tags": ["gaming", "blizzard", "diablo", "controversy", "economy"]
    },
    {
        "id": "gaming_hard_152",
        "text": "Στο 'Portal' (2007), ποιο αντικείμενο ζητά η GLaDOS από τον παίκτη να ρίξει στον αποτεφρωτήρα (Incinerator) στο Test Chamber 17, δημιουργώντας μια από τις πιο παράδοξα συναισθηματικές στιγμές του παιχνιδιού;",
        "correct": "Το Weighted Companion Cube",
        "distractors": [
            "Την ελαττωματική πυργίσκο (Defective Turret)",
            "Τη φωτογραφία της Chell",
            "Το ραδιόφωνο εκπομπής σήματος"
        ],
        "explanation": "Το Weighted Companion Cube με τις ροζ καρδιές συντρόφευε την Chell στους γρίφους του Chamber 17. Η GLaDOS την ανάγκασε να το αποτεφρώσει για να προχωρήσει, λέγοντας: 'Ευθανατώσατε τον πιστό σας Companion Cube ταχύτερα από οποιονδήποτε άλλο υποψήφιο'.",
        "funFacts": [
            "Το achievement για την αποτέφρωση του κύβου ονομάζεται σαρκαστικά 'Fratricide' (Αδελφοκτονία).",
            "Στο Portal 2, στο τέλος του παιχνιδιού, η GLaDOS επιστρέφει στην Chell έναν καψαλισμένο αλλά άθικτο Companion Cube."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_(video_game)",
        "tags": ["gaming", "portal", "valve", "glados", "companion_cube"]
    },
    {
        "id": "gaming_hard_153",
        "text": "Ποιο ήταν το όνομα της επαναστατικής τεχνολογίας γραφικών που ανέπτυξε η 3dfx Interactive το 1996 με την κάρτα 'Voodoo 1', ξεκινώντας την εποχή της τρισδιάστατης επιτάχυνσης υλικού στα PC games;",
        "correct": "Glide API",
        "distractors": [
            "Direct3D",
            "OpenGL MiniGL",
            "RenderWare"
        ],
        "explanation": "Το Glide API ήταν ένα proprietary interface προγραμματισμού σχεδιασμένο ειδικά για το τσιπ Voodoo της 3dfx. Προσέφερε εκπληκτικό texture filtering, fogging και φωτισμό σε παιχνίδια όπως το Quake και το Tomb Raider χωρίς επιβάρυνση της CPU.",
        "funFacts": [
            "Η αρχική Voodoo 1 ήταν κάρτα μόνο για 3D και απαιτούσε ειδικό εξωτερικό καλώδιο pass-through συνδεδεμένο με την κανονική 2D κάρτα γραφικών του υπολογιστή.",
            "Η 3dfx εξαγοράστηκε τελικά από την ανταγωνίστριά της NVIDIA το 2000, ενσωματώνοντας πολλές από τις πατέντες της στη σειρά GeForce."
        ],
        "source": "https://en.wikipedia.org/wiki/3dfx_Interactive",
        "tags": ["gaming", "hardware", "3dfx", "voodoo", "pc"]
    },
    {
        "id": "gaming_hard_154",
        "text": "Ποιο είναι το όνομα του εμβληματικού ηχητικού εφέ που ακούγεται όταν ένας εχθρός εντοπίζει τον Solid Snake στη σειρά 'Metal Gear Solid', συνοδευόμενο από ένα κόκκινο θαυμαστικό πάνω από το κεφάλι του φρουρού;",
        "correct": "Alert Sound (Spotted / Alert SFX)",
        "distractors": [
            "Evasion Chime",
            "Caution Stinger",
            "Danger Ping"
        ],
        "explanation": "Ο χαρακτηριστικός διαπεραστικός ήχος ορχηστρικού κρούσης μαζί με το κόκκινο θαυμαστικό '!' πάνω από το κεφάλι του εχθρού σχεδιάστηκε από τον sound designer Kazuki Muraoka και αποτελεί το πιο διάσημο ηχητικό εφέ συναγερμού στον κόσμο.",
        "funFacts": [
            "Το ηχητικό εφέ χρησιμοποιείται ευρέως ως ήχος ειδοποίησης μηνυμάτων σε κινητά τηλέφωνα παγκοσμίως.",
            "Όταν ο Snake κρύβεται στο κουτί και ο φρουρός πλησιάζει αλλά δεν τον βρίσκει, το θαυμαστικό αντικαθίσταται από ένα μπλε ερωτηματικό '?'."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid",
        "tags": ["gaming", "metal_gear", "kojima", "audio", "sfx"]
    },
    {
        "id": "gaming_hard_155",
        "text": "Ποιος Ιάπωνας συνθέτης δημιούργησε τα αξεπέραστα soundtracks των παιχνιδιών 'The Legend of Zelda' και 'Super Mario Bros.', καθορίζοντας τη μουσική ταυτότητα της Nintendo για τέσσερις δεκαετίες;",
        "correct": "Koji Kondo",
        "distractors": [
            "Nobuo Uematsu",
            "Yasunori Mitsuda",
            "Hirokazu Tanaka"
        ],
        "explanation": "Ο Koji Kondo συνέθεσε το Overworld Theme του Super Mario Bros. και το εμβληματικό Main Theme του The Legend of Zelda εκμεταλλευόμενος στο έπακρο τα 5 μονοφωνικά κανάλια ήχου του τσιπ Ricoh 2A03 του NES.",
        "funFacts": [
            "Το Overworld Theme του Super Mario Bros. είναι το πρώτο μουσικό κομμάτι βιντεοπαιχνιδιού στην ιστορία που εισήχθη στο Εθνικό Μητρώο Ηχογραφήσεων της Βιβλιοθήκης του Κογκρέσου των ΗΠΑ.",
            "Ο Kondo συνέθεσε τη μουσική του Super Mario World χρησιμοποιώντας αποκλειστικά παραλλαγές του ίδιου βασικού μοτίβου σε διαφορετικούς ρυθμούς για κάθε πίστα."
        ],
        "source": "https://en.wikipedia.org/wiki/Koji_Kondo",
        "tags": ["gaming", "nintendo", "koji_kondo", "music", "mario"]
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
        "difficulty": 5,
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 3.")
    validate_and_append("gaming", "hard", 5, questions)

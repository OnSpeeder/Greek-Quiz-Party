# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_011",
        "text": "Στο κλασικό arcade παιχνίδι 'Space Invaders' (1978) του Tomohiro Nishikado, σε τι οφειλόταν η σταδιακή αύξηση της ταχύτητας των εξωγήινων καθώς μειωνόταν ο αριθμός τους στην οθόνη;",
        "correct": "Στο ότι ο επεξεργαστής είχε λιγότερα γραφικά sprites να σχεδιάσει σε κάθε κύκλο",
        "distractors": [
            "Σε έναν αλγόριθμο τεχνητής νοημοσύνης που σχεδιάστηκε σκόπιμα για κλιμάκωση δυσκολίας",
            "Σε έναν χρονιστή που μείωνε το frame delay ανάλογα με τα hit points",
            "Σε περιορισμό της μνήμης ROM που ανάγκαζε το παιχνίδι να παρακάμπτει ρουτίνες ήχου"
        ],
        "explanation": "Ο Nishikado σχεδίασε το υλικό μόνος του. Ο επεξεργαστής Intel 8080 δυσκολευόταν να σχεδιάσει και τους 55 εξωγήινους ταυτόχρονα. Καθώς ο παίκτης τους κατέστρεφε, ο φόρτος μειωνόταν και το παιχνίδι έτρεχε στη φυσική, ταχύτερη ταχύτητά του.",
        "funFacts": [
            "Ο Nishikado παρατήρησε ότι το παιχνίδι γινόταν πιο συναρπαστικό όσο επιταχυνόταν και αποφάσισε να μην προσθέσει τεχνητή καθυστέρηση στον κώδικα.",
            "Η τεράστια επιτυχία του Space Invaders στην Ιαπωνία προκάλεσε προσωρινή έλλειψη κερμάτων των 100 γεν στην αγορά."
        ],
        "source": "https://en.wikipedia.org/wiki/Space_Invaders",
        "tags": ["gaming", "retro", "arcade", "space_invaders", "hardware"]
    },
    {
        "id": "gaming_hard_012",
        "text": "Ποιος βασικός μηχανισμός του εμβληματικού 'Street Fighter II' (1991) ανακαλύφθηκε ως μη ηθελημένο σφάλμα (bug) στον κώδικα ακύρωσης κινήσεων από τον Noritaka Funamizu, αλλά διατηρήθηκε στο τελικό παιχνίδι;",
        "correct": "Τα Combos (συνεχόμενα αδιάκοπα χτυπήματα)",
        "distractors": [
            "Το Parry (απόκρουση ακριβείας)",
            "Το Stun / Dizzy (ζάλη μετά από χτυπήματα)",
            "Τα Super Combos (ειδικές μπάρες ενέργειας)"
        ],
        "explanation": "Ο παραγωγός Noritaka Funamizu παρατήρησε ότι κατά την εκτέλεση ειδικών κινήσεων μπορούσε να ακυρωθεί το animation ενός απλού χτυπήματος, επιτρέποντας δεύτερο χτύπημα χωρίς αντίδραση του αντιπάλου. Θεώρησε το timing τόσο δύσκολο που πίστεψε ότι κανείς δεν θα το εκμεταλλευόταν.",
        "funFacts": [
            "Ο όρος 'combo' καθιερώθηκε επίσημα ως μηχανισμός από την Capcom στο 'Super Street Fighter II' με ειδικό μετρητή στην οθόνη.",
            "Το Street Fighter II κυκλοφόρησε στην επαναστατική arcade πλακέτα CP System (CPS-1) της Capcom."
        ],
        "source": "https://en.wikipedia.org/wiki/Street_Fighter_II",
        "tags": ["gaming", "capcom", "street_fighter", "mechanics", "esports"]
    },
    {
        "id": "gaming_hard_013",
        "text": "Για ποιο λόγο η Nintendo αναγκάστηκε να συμπεριλάβει δωρεάν το ακριβό εξάρτημα Expansion Pak των 4MB RAM σε κάθε αντίτυπο του 'Donkey Kong 64' (1999);",
        "correct": "Λόγω ενός άλυτου memory leak bug που κράσαρε το παιχνίδι μόνο στην απλή κονσόλα",
        "distractors": [
            "Λόγω συμφωνίας αδειοδότησης για την τεχνολογία ήχου Dolby Surround",
            "Επειδή η ROM των 32MB δεν μπορούσε να αποσυμπιεστεί σε λιγότερη μνήμη",
            "Λόγω απαίτησης της Silicon Graphics για την απόδοση δυναμικού φωτισμού"
        ],
        "explanation": "Η Rare αντιμετώπισε ένα μυστηριώδες memory leak bug που κράσαρε το παιχνίδι μετά από ώρες παιχνιδιού στην εργοστασιακή μνήμη των 4MB του N64. Η μόνη οικονομικά βιώσιμη λύση πριν την ημερομηνία κυκλοφορίας ήταν η προσθήκη του Expansion Pak των 8MB συνολικής μνήμης.",
        "funFacts": [
            "Το κόστος της προσθήκης του Expansion Pak σε εκατομμύρια αντίτυπα κόστισε στη Rare και τη Nintendo τεράστια ποσά σε περιθώριο κέρδους.",
            "Το Donkey Kong 64 κατέχει Ρεκόρ Γκίνες για τον μεγαλύτερο αριθμό συλλεκτικών αντικειμένων (collectibles) σε παιχνίδι πλατφόρμας."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_64",
        "tags": ["gaming", "nintendo64", "rare", "donkey_kong", "bugs"]
    },
    {
        "id": "gaming_hard_014",
        "text": "Ποιο διάσημο συμβάν στο MMORPG 'World of Warcraft' το 2005 μελετήθηκε επιστημονικά από επιδημιολόγους και το CDC ως μοντέλο εξάπλωσης πραγματικών πανδημιών;",
        "correct": "Το περιστατικό Corrupted Blood (Μολυσμένο Αίμα)",
        "distractors": [
            "Η Πανούκλα των Undead στο Lordaeron",
            "Η Επιδημία των Silithid στο Ahn'Qiraj",
            "Η Κατάρα του Hakkar στο Zul'Aman"
        ],
        "explanation": "Στο raid Zul'Gurub, το debuff 'Corrupted Blood' μεταδόθηκε έξω από το dungeon όταν κυνηγοί απέσυραν και ξανακάλεσαν τα κατοικίδιά τους σε μεγάλες πόλεις όπως το Ironforge, σκοτώνοντας εκατομμύρια παίκτες.",
        "funFacts": [
            "Επιδημιολόγοι όπως ο Eric Lofgren χρησιμοποίησαν τα δεδομένα συμπεριφοράς των παικτών για να μελετήσουν την ανθρώπινη αντίδραση σε πανδημίες όπως ο COVID-19.",
            "Η Blizzard αναγκάστηκε να κάνει πολλαπλά hard resets στους servers και τελικά να αλλάξει τον κώδικα ώστε το debuff να μην επηρεάζει κατοικίδια."
        ],
        "source": "https://en.wikipedia.org/wiki/Corrupted_Blood_incident",
        "tags": ["gaming", "warcraft", "blizzard", "mmo", "science"]
    },
    {
        "id": "gaming_hard_015",
        "text": "Ποιο είναι το γνωστό glitch στο επίπεδο 256 του αρχικού arcade 'Pac-Man' (1980), όπου η δεξιά πλευρά της οθόνης γεμίζει με ακατάληπτους χαρακτήρες και αριθμούς;",
        "correct": "Kill Screen (λόγω υπερχείλισης ακεραίου 8-bit στα 256 επίπεδα)",
        "distractors": [
            "MissingNo Screen",
            "Split Maze Crash",
            "Ghost Glitch"
        ],
        "explanation": "Ο μετρητής επιπέδων αποθηκευόταν σε έναν 8-bit καταχωρητή. Στο επίπεδο 255 ο μετρητής έφτανε στο μέγιστο και στο επόμενο επίπεδο (256) προκαλούσε integer overflow (υπερχείλιση στο 0), διαβάζοντας δεδομένα μνήμης ως sprites φρούτων.",
        "funFacts": [
            "Ένα 'τέλειο παιχνίδι' (Perfect Game) στο Pac-Man απαιτεί ακριβώς 3.333.360 πόντους, τρώγοντας κάθε κουκκίδα, φρούτο και φάντασμα χωρίς να χαθεί ούτε μία ζωή μέχρι το split screen.",
            "Ο πρώτος άνθρωπος που πέτυχε επίσημα καταγεγραμμένο τέλειο σκορ ήταν ο Billy Mitchell το 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Pac-Man",
        "tags": ["gaming", "pacman", "arcade", "glitch", "retro"]
    },
    {
        "id": "gaming_hard_016",
        "text": "Πώς κατάφερε ο θρυλικός Satoru Iwata να χωρέσει ολόκληρη την περιοχή Kanto μαζί με την Johto στις κασέτες Game Boy των 'Pokémon Gold και Silver' (1999);",
        "correct": "Έγραψε έναν εξαιρετικά αποδοτικό αλγόριθμο συμπίεσης γραφικών σε assembly",
        "distractors": [
            "Αύξησε το hardware memory bank controller σε MBC5",
            "Αφαίρεσε όλα τα animations των Pokémon από τις μάχες",
            "Μείωσε τα χρώματα της παλέτας από 56 σε 16"
        ],
        "explanation": "Η Game Freak δυσκολευόταν να χωρέσει έστω και μόνο την Johto στην κασέτα. Ο Satoru Iwata ανέλυσε τον κώδικα και επανασχεδίασε τα εργαλεία συμπίεσης, απελευθερώνοντας τόσο χώρο ώστε χώρεσε ολόκληρη η προηγούμενη περιφέρεια Kanto.",
        "funFacts": [
            "Ο Iwata είχε μεταφέρει μόνος του τον κώδικα μάχης των Pokémon Red και Green στο Nintendo 64 για το Pokémon Stadium μέσα σε μία μόνο εβδομάδα, χωρίς αρχική τεκμηρίωση.",
            "Ο Iwata έγινε αργότερα ο τέταρτος πρόεδρος της Nintendo, καθοδηγώντας την εποχή του Nintendo DS και του Wii."
        ],
        "source": "https://en.wikipedia.org/wiki/Satoru_Iwata",
        "tags": ["gaming", "nintendo", "pokemon", "iwata", "programming"]
    },
    {
        "id": "gaming_hard_017",
        "text": "Στο 'Metal Gear Solid' (1998) για το PlayStation, ποιο μοναδικό τέχνασμα έπρεπε να χρησιμοποιήσει ο παίκτης για να νικήσει το αφεντικό Psycho Mantis που 'διάβαζε τις κινήσεις του μυαλού του';",
        "correct": "Να αλλάξει τη σύνδεση του χειριστηρίου στη θύρα Controller Port 2",
        "distractors": [
            "Να αφαιρέσει την κάρτα μνήμης (Memory Card) κατά τη διάρκεια της μάχης",
            "Να πατήσει pause και να ρυθμίσει τη φωτεινότητα της οθόνης στο ελάχιστο",
            "Να εξοπλιστεί με το κουτί από χαρτόνι (Cardboard Box)"
        ],
        "explanation": "Ο Hideo Kojima σχεδίασε τον Psycho Mantis να διαβάζει τα inputs από το Controller Port 1. Συνδέοντας το χειριστήριο στο Port 2, ο Mantis δεν μπορούσε να προβλέψει τις κινήσεις του Solid Snake.",
        "funFacts": [
            "Ο Psycho Mantis διάβαζε επίσης τα saves της Memory Card και σχολίαζε άλλα παιχνίδια της Konami που είχε παίξει ο παίκτης, όπως το Castlevania: Symphony of the Night.",
            "Εάν ο παίκτης δεν είχε δεύτερο χειριστήριο ή δεν καταλάβαινε το κόλπο, μετά από αρκετές αποτυχημένες προσπάθειες μπορούσε να καταστρέψει τα αγάλματα στο δωμάτιο για να τον νικήσει."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid",
        "tags": ["gaming", "kojima", "metal_gear", "playstation", "design"]
    },
    {
        "id": "gaming_hard_018",
        "text": "Ποιο διάσημο αγωνιστικό συμβάν στο τουρνουά EVO 2004, γνωστό ως 'Moment #37' ή 'Daigo Parry', θεωρείται η κορυφαία στιγμή στην ιστορία των esports;",
        "correct": "Ο Daigo Umehara μπλόκαρε 15 διαδοχικά hits του Super Art της Chun-Li με 1 pixel ζωής",
        "distractors": [
            "Ο Justin Wong κέρδισε με perfect στον τελικό γύρο του Marvel vs Capcom 2",
            "Ο Tokido εκτέλεσε Raging Demon μέσα από fireball στον αέρα",
            "Ο SonicFox άλλαξε χαρακτήρα στο τελευταίο match point του Mortal Kombat"
        ],
        "explanation": "Στο Street Fighter III: 3rd Strike, ο Daigo Umehara (Ken) με σχεδόν μηδενική ζωή εκτέλεσε 15 συνεχόμενα parry ακριβείας στον αέρα και στο έδαφος απέναντι στο Houyoku-sen της Chun-Li (Justin Wong) και αντεπιτέθηκε κερδίζοντας τον αγώνα.",
        "funFacts": [
            "Το parry στο 3rd Strike απαιτεί πάτημα του μοχλού προς τα εμπρός ακριβώς τη στιγμή του χτυπήματος (εντός παραθύρου 2-4 frames), χωρίς περιθώριο λάθους.",
            "Το βίντεο της αναμέτρησης με τις κραυγές του εκστασιασμένου κοινού έγινε το πρώτο viral βίντεο στην ιστορία των ανταγωνιστικών fighting games."
        ],
        "source": "https://en.wikipedia.org/wiki/Evo_Moment_37",
        "tags": ["gaming", "evo", "street_fighter", "daigo", "esports"]
    },
    {
        "id": "gaming_hard_019",
        "text": "Ποιος ήταν ο τεχνικός λόγος για τον οποίο η ομάδα ανάπτυξης του αρχικού 'Silent Hill' (1999) στο PlayStation 1 κάλυψε ολόκληρη την πόλη με πυκνή ομίχλη και σκοτάδι;",
        "correct": "Για να κρύψει το περιορισμένο draw distance και τις αδυναμίες επεξεργασίας του PS1",
        "distractors": [
            "Για να μειώσει τον όγκο των textures που φορτώνονταν από το CD-ROM",
            "Για να αποφύγει την ανάγκη σχεδιασμού ουρανού και καιρικών φαινομένων",
            "Επειδή το σύστημα φωτισμού υποστήριζε μόνο μονόχρωμα εφέ σκιών"
        ],
        "explanation": "Το PlayStation 1 δεν μπορούσε να αποδώσει τρισδιάστατα περιβάλλοντα σε μεγάλη απόσταση χωρίς σοβαρή πτώση του ρυθμού ανανέωσης. Η Team Silent μετέτρεψε αυτόν τον τεχνικό περιορισμό σε σήμα κατατεθέν της ατμόσφαιρας τρόμου του franchise.",
        "funFacts": [
            "Το soundtrack και ο ηχητικός σχεδιασμός του Akira Yamaoka συνέβαλαν τα μέγιστα στην ψυχολογική πίεση του παίκτη μέσα στην ομίχλη.",
            "Η Team Silent απαρτιζόταν από μέλη της Konami που είχαν αποτύχει σε προηγούμενα projects και είχαν συγκεντρωθεί σε μια ομάδα με ελάχιστες αρχικές προσδοκίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_(video_game)",
        "tags": ["gaming", "silenthill", "konami", "horror", "playstation"]
    },
    {
        "id": "gaming_hard_020",
        "text": "Ποιος θρυλικός σχεδιαστής παιχνιδιών και μηχανικός της Nintendo επινόησε το D-pad (σταυρό κατευθύνσεων), δημιούργησε το Game Boy και ήταν μέντορας του Shigeru Miyamoto;",
        "correct": "Gunpei Yokoi",
        "distractors": [
            "Hiroshi Yamauchi",
            "Masayuki Uemura",
            "Genyo Takeda"
        ],
        "explanation": "Ο Gunpei Yokoi δημιούργησε τη σειρά Game & Watch όπου πρωτοεμφανίστηκε το D-pad, σχεδίασε το Game Boy και εφάρμοσε τη φιλοσοφία 'Lateral Thinking with Withered Technology' (πλάγια σκέψη με ώριμη/φθηνή τεχνολογία).",
        "funFacts": [
            "Ο Yokoi παρήγαγε επίσης τα κλασικά παιχνίδια Metroid και Kid Icarus.",
            "Μετά την εμπορική αποτυχία του Virtual Boy το 1995 αποχώρησε από τη Nintendo και σχεδίασε τη φορητή κονσόλα WonderSwan για την Bandai."
        ],
        "source": "https://en.wikipedia.org/wiki/Gunpei_Yokoi",
        "tags": ["gaming", "nintendo", "gameboy", "yokoi", "hardware"]
    },
    {
        "id": "gaming_hard_021",
        "text": "Στο 'Super Mario 64' (1996), ποιος διάσημος μηχανισμός επιτρέπει στους speedrunners να αποκτήσουν θεωρητικά άπειρη αρνητική ταχύτητα και να περάσουν μέσα από τοίχους και κλειδωμένες πόρτες;",
        "correct": "Backwards Long Jump (BLJ)",
        "distractors": [
            "Reverse Wall Kick",
            "Infinite Triple Jump",
            "Slide Glitch Acceleration"
        ],
        "explanation": "Στο Backwards Long Jump, το παιχνίδι δεν θέτει ανώτατο όριο στην αρνητική ταχύτητα όταν ο Mario εκτελεί μακρινό άλμα προς τα πίσω πάνω σε ανηφόρα ή σκαλοπάτια, εκτοξεύοντας την ταχύτητά του σε τεράστιες τιμές.",
        "funFacts": [
            "Η Nintendo διόρθωσε το BLJ στην ιαπωνική επανέκδοση Shindou Version και στις μεταγενέστερες εκδόσεις του Super Mario 64.",
            "Χάρη στο BLJ, το παιχνίδι μπορεί να τερματιστεί με ακριβώς 0 αστέρια αντί των 70 που απαιτούνται κανονικά."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_64",
        "tags": ["gaming", "mario", "nintendo64", "speedrun", "glitch"]
    },
    {
        "id": "gaming_hard_022",
        "text": "Ποιο σύστημα ρόλων (RPG mechanics) σχεδιάστηκε για το αρχικό 'Fallout' (1997) από τον Tim Cain, αφού η Interplay έχασε τα δικαιώματα του επιτραπέζιου συστήματος GURPS;",
        "correct": "S.P.E.C.I.A.L.",
        "distractors": [
            "D20 System",
            "F.A.T.E.",
            "V.A.T.S."
        ],
        "explanation": "Το SPECIAL αποτελεί ακρωνύμιο των βασικών χαρακτηριστικών: Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck. Δημιουργήθηκε εκτάκτως όταν η Steve Jackson Games απέσυρε την άδεια του GURPS λόγω της βίας στο Fallout.",
        "funFacts": [
            "Ο Tim Cain έγραψε μόνος του τη βασική μηχανή του αρχικού Fallout σε διάστημα έξι μηνών πριν συγκροτηθεί η πλήρης ομάδα ανάπτυξης.",
            "Η αρχική επιλογή ονόματος για το σύστημα ήταν 'ACELIPS' πριν καταλήξουν στο ευφυές SPECIAL."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout_(video_game)",
        "tags": ["gaming", "fallout", "interplay", "rpg", "special"]
    },
    {
        "id": "gaming_hard_023",
        "text": "Ποια διάσημη ναυμαχία στο MMORPG 'EVE Online' το 2014 είχε ως αποτέλεσμα την καταστροφή 75 τιτάνων (Titans) και υπολογίστηκε ότι προκάλεσε πραγματικές υλικές ζημιές άνω των 300.000 δολαρίων ΗΠΑ;",
        "correct": "Η Μάχη του B-R5RB (Bloodbath of B-R5RB)",
        "distractors": [
            "Η Μάχη του Asakai",
            "Η Πολιορκία του 9-4RP2",
            "Η Σφαγή του Jita"
        ],
        "explanation": "Η σύγκρουση στο σύστημα B-R5RB ξέσπασε όταν μια συμμαχία ξέχασε να πληρώσει ένα αυτόματο τέλος συντήρησης του διαστημικού σταθμού, προκαλώντας μια 21ωρη τιτάνια σύγκρουση με συμμετοχή πάνω από 7.500 παικτών.",
        "funFacts": [
            "Οι προγραμματιστές της CCP Games ενεργοποίησαν το σύστημα 'Time Dilation' (διαστολή χρόνου) επιβραδύνοντας το παιχνίδι στο 10% της κανονικής ταχύτητας για να μην καταρρεύσουν οι servers.",
            "Η CCP Games ανήγειρε ένα μόνιμο ψηφιακό μνημείο ('Titanomachy') μέσα στον χώρο του παιχνιδιού στο ακριβές σημείο της μάχης."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodbath_of_B-R5RB",
        "tags": ["gaming", "eve_online", "mmo", "battles", "history"]
    },
    {
        "id": "gaming_hard_024",
        "text": "Ποια ομάδα τριών κορυφαίων δημιουργών, γνωστή ως 'Dream Project', ένωσε τις δυνάμεις της για την ανάπτυξη του θρυλικού JRPG 'Chrono Trigger' (1995);",
        "correct": "Hironobu Sakaguchi, Yuji Horii και Akira Toriyama",
        "distractors": [
            "Yoshinori Kitase, Tetsuya Nomura και Nobuo Uematsu",
            "Shigeru Miyamoto, Takashi Tezuka και Koji Kondo",
            "Yasumi Matsuno, Akihiko Yoshida και Hitoshi Sakimoto"
        ],
        "explanation": "Το 'Dream Team' ένωσε τον δημιουργό του Final Fantasy (Sakaguchi), τον δημιουργό του Dragon Quest (Horii) και τον διάσημο δημιουργό του Dragon Ball (Toriyama) σε μια ιστορική συνεργασία των τότε ανταγωνιστικών εταιρειών Square και Enix.",
        "funFacts": [
            "Ο συνθέτης Yasunori Mitsuda εργάστηκε τόσο σκληρά στο soundtrack του Chrono Trigger που κατέρρευσε από έλκος στομάχου, με τον Nobuo Uematsu να ολοκληρώνει τα υπόλοιπα κομμάτια.",
            "Το Chrono Trigger περιείχε 13 διαφορετικά τέλη, πρωτοπορώντας με τη λειτουργία 'New Game+'."
        ],
        "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
        "tags": ["gaming", "snes", "chrono_trigger", "square", "rpg"]
    },
    {
        "id": "gaming_hard_025",
        "text": "Ποιος κορυφαίος συγγραφέας επιστημονικής φαντασίας (συγγραφέας του 'Ender's Game') έγραψε τους πανέξυπνους στίχους για τις προσβολές στο 'Insult Sword Fighting' του 'The Secret of Monkey Island' (1990);",
        "correct": "Orson Scott Card",
        "distractors": [
            "Douglas Adams",
            "Terry Pratchett",
            "Neil Gaiman"
        ],
        "explanation": "Ο Ron Gilbert κάλεσε τον Orson Scott Card στα γραφεία της Lucasfilm Games στο Skywalker Ranch για να γράψει τις κωμικές προσβολές και ανταπαντήσεις που χρησιμοποιούσαν οι πειρατές στις μονομαχίες με σπαθιά.",
        "funFacts": [
            "Μία από τις διασημότερες προσβολές είναι: 'You fight like a dairy farmer!' με την απάντηση: 'How appropriate! You fight like a cow!'.",
            "Ο Ron Gilbert εμπνεύστηκε τις ξιφομαχίες από παλιές ταινίες του Errol Flynn, όπου οι πειρατές μιλούσαν διαρκώς προσβάλλοντας ο ένας τον άλλον αντί να χτυπούν."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Secret_of_Monkey_Island",
        "tags": ["gaming", "lucasarts", "monkey_island", "adventure", "writing"]
    },
    {
        "id": "gaming_hard_026",
        "text": "Ποια πρωτοποριακή μέθοδο χρησιμοποίησε ο Jordan Mechner για να αποδώσει τις εξαιρετικά ρεαλιστικές κινήσεις του πρωταγωνιστή στο αρχικό 'Prince of Persia' (1989);",
        "correct": "Rotoscoping (βιντεοσκόπηση του αδελφού του και σχεδίαση καρέ-καρέ)",
        "distractors": [
            "Motion capture με οπτικούς αισθητήρες σε στούντιο",
            "Stop-motion animation με πήλινες φιγούρες",
            "Procedural inverse kinematics σε mainframe"
        ],
        "explanation": "Ο Mechner βιντεοσκόπησε τον 15χρονο αδελφό του David να τρέχει, να πηδάει και να σκαρφαλώνει φορώντας άσπρα ρούχα, και στη συνέχεια αντέγραψε τα καρέ με το χέρι στον υπολογιστή Apple II.",
        "funFacts": [
            "Ο Mechner χρησιμοποίησε παρόμοια τεχνική για τις σκηνές ξιφομαχίας, αντιγράφοντας σκηνές από την κλασική χολιγουντιανή ταινία 'Οι Περιπέτειες του Ρομπέν των Δασών' (1938).",
            "Ο πηγαίος κώδικας του Prince of Persia θεωρούνταν χαμένος για δεκαετίες μέχρι που ο πατέρας του Mechner τον βρήκε σε μια κούτα το 2012."
        ],
        "source": "https://en.wikipedia.org/wiki/Prince_of_Persia_(1989_video_game)",
        "tags": ["gaming", "retro", "apple2", "prince_of_persia", "animation"]
    },
    {
        "id": "gaming_hard_027",
        "text": "Ποιο ήταν το αρχικό όνομα της πρωταγωνίστριας Lara Croft στο 'Tomb Raider' (1996), προτού ο σχεδιαστής Toby Gard αποφασίσει να την κάνει Βρετανίδα αριστοκράτισσα;",
        "correct": "Laura Cruz (Νοτιοαμερικανίδα μισθοφόρος)",
        "distractors": [
            "Sara Croft",
            "Elena Drake",
            "Rachel Stone"
        ],
        "explanation": "Η αρχική ιδέα της Core Design ήταν μια σκληροτράχηλη Νοτιοαμερικανίδα με το όνομα Laura Cruz. Η Eidos ζήτησε πιο 'φιλικό προς τη Βρετανία' προφίλ, και η ομάδα βρήκε το επίθετο Croft ψάχνοντας στον τηλεφωνικό κατάλογο του Derby.",
        "funFacts": [
            "Ο Toby Gard παραιτήθηκε από την Core Design μετά την κυκλοφορία του πρώτου παιχνιδιού λόγω διαφωνιών για τη σεξουαλικοποίηση του χαρακτήρα στις διαφημιστικές καμπάνιες.",
            "Το χαρακτηριστικό μέγεθος του στήθους της Lara Croft προέκυψε τυχαία όταν ο Gard αύξησε κατά λάθος τις αναλογίες του μοντέλου κατά 150% στο πρόγραμμα 3D."
        ],
        "source": "https://en.wikipedia.org/wiki/Lara_Croft",
        "tags": ["gaming", "tomb_raider", "lara_croft", "playstation", "design"]
    },
    {
        "id": "gaming_hard_028",
        "text": "Ποια διάσημη λειτουργία του θρυλικού 'GoldenEye 007' (1997) στο Nintendo 64 προστέθηκε μυστικά από έναν μόνο προγραμματιστή τον τελευταίο μήνα της ανάπτυξης χωρίς έγκριση από τη διοίκηση;",
        "correct": "Το 4-Player Split-Screen Multiplayer mode",
        "distractors": [
            "Το επίπεδο δυσκολίας '00 Agent'",
            "Το Paintball Mode cheat",
            "Η πίστα 'Facility' με το διάσημο άνοιγμα εξαερισμού"
        ],
        "explanation": "Ο Steve Ellis προγραμμάτισε τη λειτουργία multiplayer split-screen μέσα σε λίγες εβδομάδες χωρίς επίσημη έγκριση. Όταν την έδειξε στην υπόλοιπη ομάδα, ενθουσιάστηκαν τόσο που αποφάσισαν να τη συμπεριλάβουν στο τελικό παιχνίδι.",
        "funFacts": [
            "Το multiplayer του GoldenEye 007 καθόρισε τα console first-person shooters και ήταν υπεύθυνο για το μεγαλύτερο μέρος της τεράστιας επιτυχίας του τίτλου.",
            "Ο χαρακτήρας Oddjob απαγορευόταν άτυπα μεταξύ φίλων επειδή το χαμηλό του ύψος δυσκόλευε τη στόχευση με το σύστημα auto-aim."
        ],
        "source": "https://en.wikipedia.org/wiki/GoldenEye_007_(1997_video_game)",
        "tags": ["gaming", "nintendo64", "goldeneye", "fps", "rare"]
    },
    {
        "id": "gaming_hard_029",
        "text": "Στο πρωτοποριακό horror παιχνίδι 'Sweet Home' (1989) της Capcom στο Famicom, ποιος διάσημος σκηνοθέτης video games βασίστηκε για να δημιουργήσει αργότερα το 'Resident Evil' (1996);",
        "correct": "Shinji Mikami",
        "distractors": [
            "Keiji Inafune",
            "Hideki Kamiya",
            "Tokuro Fujiwara"
        ],
        "explanation": "Ο Tokuro Fujiwara (σκηνοθέτης του Sweet Home) ανέθεσε στον Shinji Mikami να φτιάξει ένα πνευματικό διάδοχο του Sweet Home. Το αρχικό Resident Evil σχεδιάστηκε ως remake του Sweet Home πριν εξελιχθεί σε αυτόνομο τίτλο.",
        "funFacts": [
            "Μηχανισμοί όπως η έπαυλη, οι γρίφοι, τα animation ανοίγματος θυρών για το φόρτωμα δωματίων και η περιορισμένη διαχείριση inventory προήλθαν απευθείας από το Sweet Home.",
            "Το Sweet Home δεν κυκλοφόρησε ποτέ επίσημα στη Δύση λόγω της γραφικής βίας και των στοιχείων gore για τα μέτρα του NES."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_(1996_video_game)",
        "tags": ["gaming", "resident_evil", "capcom", "horror", "origins"]
    },
    {
        "id": "gaming_hard_030",
        "text": "Ποιο μαθηματικό πρόβλημα γραφικών 3D έλυσε ο John Carmack στο 'Doom 3' (2004) με μια πρωτοποριακή μέθοδο υπολογισμού σκιών όγκου σε πραγματικό χρόνο, γνωστή ως 'Carmack's Reverse';",
        "correct": "Stencil Shadow Volumes (αναστροφή του βάθους Z-pass σε Z-fail)",
        "distractors": [
            "Ray-Traced Ambient Occlusion",
            "Radiosity Lightmapping",
            "Parallax Occlusion Mapping"
        ],
        "explanation": "Το Carmack's Reverse (Z-fail stencil shadow) επέτρεψε τον τέλειο υπολογισμό σκιών χωρίς artifacts όταν η κάμερα του παίκτη βρισκόταν μέσα στον όγκο της σκιάς. Ανακαλύφθηκε ανεξάρτητα και κατοχυρώθηκε με πατέντα από την Creative Technology.",
        "funFacts": [
            "Λόγω της πατέντας της Creative Labs, η id Software αναγκάστηκε να υπογράψει συμφωνία υποστήριξης της τεχνολογίας ήχου EAX 4.0 για να αποφύγει δικαστικές διαμάχες.",
            "Ο John Carmack δημοσίευσε τη λύση του στο διαδίκτυο πριν συνειδητοποιήσει ότι άλλοι ερευνητές είχαν ήδη καταθέσει πατέντα."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_volume#Depth_fail_(Carmack's_Reverse)",
        "tags": ["gaming", "carmack", "doom", "programming", "graphics"]
    },
    {
        "id": "gaming_hard_031",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού physics puzzle student game από το DigiPen Institute of Technology, του οποίου ολόκληρη η εξαμελής ομάδα προσλήφθηκε από τη Valve για να δημιουργήσει το 'Portal' (2007);",
        "correct": "Narbacular Drop",
        "distractors": [
            "Tag: The Power of Paint",
            "Perspective",
            "Quantum Conundrum"
        ],
        "explanation": "Ο Gabe Newell είδε την παρουσίαση του 'Narbacular Drop' (όπου μια πριγκίπισσα άνοιγε πύλες σε μπουντρούμι) και προσέλαβε αμέσως όλη την ομάδα μαθητών για να ενσωματώσουν τον μηχανισμό στη Source Engine, δημιουργώντας το Portal.",
        "funFacts": [
            "Μια άλλη ομάδα φοιτητών του DigiPen που έφτιαξε το 'Tag: The Power of Paint' προσλήφθηκε επίσης από τη Valve για να φτιάξει τους μηχανισμούς γέλης (gels) στο Portal 2.",
            "Η φωνή της GLaDOS ανήκει στην τραγουδίστρια και ηθοποιό Ellen McLain."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_(video_game)",
        "tags": ["gaming", "portal", "valve", "history", "physics"]
    },
    {
        "id": "gaming_hard_032",
        "text": "Ποιος σχεδιαστής και παραγωγός επινόησε τη φιλοσοφία του 'Design by Subtraction' (αφαίρεση περιττών στοιχείων UI και διαλόγων) για τα αριστουργήματα 'Ico' (2001) και 'Shadow of the Colossus' (2005);",
        "correct": "Fumito Ueda",
        "distractors": [
            "Keita Takahashi",
            "Tetsuya Mizuguchi",
            "Goichi Suda (Suda51)"
        ],
        "explanation": "Ο Fumito Ueda αφαίρεσε μπάρες ζωής, inventory, χάρτες και περιττούς διαλόγους ώστε ο παίκτης να συνδεθεί συναισθηματικά με τους χαρακτήρες και το περιβάλλον αποκλειστικά μέσω gameplay.",
        "funFacts": [
            "Στο Ico, η Yorda και ο Ico μιλούν διαφορετικές επινοημένες γλώσσες, ενισχύοντας την ανάγκη επικοινωνίας μέσω της φυσικής επαφής (κράτημα χεριού).",
            "Ο Hidetaka Miyazaki δήλωσε ότι το Ico ήταν το παιχνίδι που τον ενέπνευσε να παρατήσει την καριέρα του στην Oracle και να γίνει game designer."
        ],
        "source": "https://en.wikipedia.org/wiki/Fumito_Ueda",
        "tags": ["gaming", "ico", "shadow_of_the_colossus", "playstation", "design"]
    },
    {
        "id": "gaming_hard_033",
        "text": "Στο 'Castlevania: Symphony of the Night' (1997), ποιο μυστικό στοιχείο διπλασίαζε τη διάρκεια του παιχνιδιού και αποκάλυπτε το πραγματικό τέλος της ιστορίας;",
        "correct": "Το Ανεστραμμένο Κάστρο (Inverted Castle) που παιζόταν ανάποδα στο ταβάνι",
        "distractors": [
            "Ο δεύτερος υπόγειος λαβύρινθος της Carmilla",
            "Ο Πύργος του Ρολογιού των Παράλληλων Διαστάσεων",
            "Η Αρένα των 100 Δοκιμασιών του Richter"
        ],
        "explanation": "Φορώντας τα Holy Glasses στη μάχη με τον Richter, ο Alucard μπορούσε να καταστρέψει τη σφαίρα του Shaft και να τηλεμεταφερθεί στο Inverted Castle, όπου ολόκληρος ο χάρτης του κάστρου παιζόταν ανάποδα με νέα αφεντικά και όπλα.",
        "funFacts": [
            "Ο βοηθός σκηνοθέτη Koji Igarashi (Iga) άντλησε έμπνευση από τη σειρά The Legend of Zelda για την εξερεύνηση και την απόκτηση νέων ικανοτήτων.",
            "Ο αρχικός διάλογος του Richter και του Dracula ('What is a man? A miserable little pile of secrets!') έγινε ένα από τα πιο διάσημα internet memes."
        ],
        "source": "https://en.wikipedia.org/wiki/Castlevania:_Symphony_of_the_Night",
        "tags": ["gaming", "castlevania", "playstation", "konami", "metroidvania"]
    },
    {
        "id": "gaming_hard_034",
        "text": "Ποιο ήταν το πρώτο home console video game στην ιστορία που περιείχε ένα επίσημα τεκμηριωμένο 'Easter Egg', τοποθετημένο κρυφά από τον προγραμματιστή Warren Robinett;",
        "correct": "Adventure (1979) στο Atari 2600",
        "distractors": [
            "Pitfall! (1982)",
            "Haunted House (1981)",
            "Yars' Revenge (1982)"
        ],
        "explanation": "Επειδή η Atari αρνούνταν να αναγράφει τα ονόματα των δημιουργών στα παιχνίδια, ο Warren Robinett έκρυψε ένα μυστικό δωμάτιο στο 'Adventure'. Μεταφέροντας μια 'αόρατη κουκκίδα' (gray dot), εμφανιζόταν το μήνυμα 'Created by Warren Robinett'.",
        "funFacts": [
            "Όταν η Atari ανακάλυψε το Easter egg, το παιχνίδι είχε ήδη πουλήσει εκατοντάδες χιλιάδες αντίτυπα και το κόστος επανακατασκευής των ROMs ήταν απαγορευτικό.",
            "Το Easter Egg του Robinett αποτελεί κεντρικό στοιχείο πλοκής στο μυθιστόρημα και την ταινία 'Ready Player One'."
        ],
        "source": "https://en.wikipedia.org/wiki/Adventure_(1979_video_game)",
        "tags": ["gaming", "atari", "retro", "easter_egg", "history"]
    },
    {
        "id": "gaming_hard_035",
        "text": "Ποιο διάσημο real-time strategy παιχνίδι της Westwood Studios το 1992 καθιέρωσε τα σύγχρονα θεμέλια του είδους RTS (resource harvesting, βάσεις, mini-map, faction asymmetry);",
        "correct": "Dune II: The Building of a Dynasty",
        "distractors": [
            "Command & Conquer",
            "Warcraft: Orcs & Humans",
            "Herzog Zwei"
        ],
        "explanation": "Το Dune II του Brett Sperry καθόρισε τη σύγχρονη φόρμουλα RTS (συλλογή Spice, κατασκευή κτιρίων, fog of war και μάχες μεταξύ Atreides, Harkonnen και Ordos), επηρεάζοντας άμεσα τη δημιουργία του Warcraft και του C&C.",
        "funFacts": [
            "Ο όρος 'Real-Time Strategy' επινοήθηκε από τον ίδιο τον Brett Sperry για να περιγράψει το παιχνίδι στον εμπορικό τύπο.",
            "Στο Dune II ο παίκτης μπορούσε να επιλέξει μόνο μία μονάδα τη φορά, καθώς το drag-box selection πολλαπλών μονάδων επινοήθηκε αργότερα στο Command & Conquer."
        ],
        "source": "https://en.wikipedia.org/wiki/Dune_II",
        "tags": ["gaming", "rts", "westwood", "dune", "retro"]
    },
    {
        "id": "gaming_hard_036",
        "text": "Ποια πρωτοποριακή τεχνητή νοημοσύνη (AI) εφάρμοσε η Valve στους στρατιώτες HECU Marines στο αρχικό 'Half-Life' (1998), δημιουργώντας την ψευδαίσθηση συντονισμένης τακτικής μάχης;",
        "correct": "Squad/Flocking Behavior και ηχητική κάλυψη με ρίψη χειροβομβίδων",
        "distractors": [
            "Νευρωνικά δίκτυα ενισχυτικής μάθησης (Q-learning)",
            "Πλήρως scripted triggers σε κάθε γωνία του χάρτη",
            "A* Pathfinding με απεριόριστη γνώση της θέσης του παίκτη"
        ],
        "explanation": "Οι στρατιώτες του Half-Life δεν είχαν παντογνωσία. Χρησιμοποιούσαν αισθητήρες οπτικής επαφής, αντάλλασσαν ραδιοφωνικά μηνύματα, έριχναν χειροβομβίδες για να αναγκάσουν τον παίκτη να βγει από την κάλυψη και εκτελούσαν κυκλωτικές κινήσεις.",
        "funFacts": [
            "Ο προγραμματιστής AI Steve Bond ανέπτυξε ένα σύστημα όπου οι στρατιώτες αξιολογούσαν δυναμικά τη διάταξη του χώρου και τις διαθέσιμες καλύψεις.",
            "Το Half-Life κέρδισε πάνω από 50 βραβεία 'Game of the Year' και έφερε επανάσταση στην αφήγηση ιστορίας χωρίς cutscenes."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_(video_game)",
        "tags": ["gaming", "valve", "halflife", "ai", "fps"]
    },
    {
        "id": "gaming_hard_037",
        "text": "Ποια ήταν η πρώτη κονσόλα στην ιστορία των video games που διέθετε ενσωματωμένο σκληρό δίσκο (HDD) 8GB και θύρα Ethernet για online gaming ως βασικό εξοπλισμό;",
        "correct": "Xbox (Microsoft, 2001)",
        "distractors": [
            "PlayStation 2 (Sony)",
            "Sega Dreamcast",
            "Nintendo GameCube"
        ],
        "explanation": "Το αρχικό Xbox της Microsoft κυκλοφόρησε με ενσωματωμένο σκληρό δίσκο 8GB (ή 10GB) και κάρτα δικτύου Ethernet 10/100, θέτοντας τα θεμέλια για την υπηρεσία Xbox Live το 2002.",
        "funFacts": [
            "Ο σκληρός δίσκος εξάλειψε την ανάγκη αγοράς ξεχωριστών καρτών μνήμης για saves και επέτρεψε caching για γρηγορότερα loading times.",
            "Το αρχικό πρωτότυπο της κονσόλας κατασκευάστηκε κυριολεκτικά από εξαρτήματα υπολογιστή Dell και ονομαζόταν 'DirectX Box'."
        ],
        "source": "https://en.wikipedia.org/wiki/Xbox_(console)",
        "tags": ["gaming", "xbox", "microsoft", "hardware", "history"]
    },
    {
        "id": "gaming_hard_038",
        "text": "Ποιο soundtrack συνέθεσε ο Frank Klepacki για τη σειρά 'Command & Conquer: Red Alert' (1996), με τον διάσημο στρατιωτικό industrial metal ρυθμό;",
        "correct": "Hell March",
        "distractors": [
            "Act on Instinct",
            "Grinder",
            "Soviet March"
        ],
        "explanation": "Το 'Hell March' με τον ήχο στρατιωτικών μπότων που παρελαύνουν, γερμανικά παραγγέλματα και βαριά κιθαριστικά riffs έγινε το απόλυτο μουσικό θέμα της σειράς Red Alert.",
        "funFacts": [
            "Ο Frank Klepacki έγραψε το κομμάτι μέσα σε μία μόνο μέρα, προορίζοντάς το αρχικά για το sequel του αρχικού Command & Conquer.",
            "Το χαρακτηριστικό παράγγελμα στην αρχή του κομματιού είναι 'Die Waffen, legt an!' (Ετοιμάστε τα όπλα!)."
        ],
        "source": "https://en.wikipedia.org/wiki/Command_%26_Conquer:_Red_Alert",
        "tags": ["gaming", "command_and_conquer", "music", "klepacki", "rts"]
    },
    {
        "id": "gaming_hard_039",
        "text": "Ποια διάσημη εταιρεία video games ιδρύθηκε το 1995 στο Έντμοντον του Καναδά από τρεις απόφοιτους ιατρικής (Ray Muzyka, Greg Zeschuk και Augustine Yip);",
        "correct": "BioWare",
        "distractors": [
            "Relic Entertainment",
            "Radical Entertainment",
            "Silicon Knights"
        ],
        "explanation": "Οι τρεις γιατροί χρηματοδότησαν την ίδρυση της BioWare με χρήματα από την ιατρική τους πρακτική. Στη συνέχεια δημιούργησαν τα Baldur's Gate, Neverwinter Nights, Star Wars: Knights of the Old Republic και Mass Effect.",
        "funFacts": [
            "Το πρώτο τους ιατρικό project ήταν ένα εκπαιδευτικό λογισμικό γαστρεντερολογίας πριν στραφούν στα video games.",
            "Η μηχανή Infinity Engine που ανέπτυξαν για το Baldur's Gate (1998) αναβίωσε πλήρως τα ισομετρικά RPGs στο PC."
        ],
        "source": "https://en.wikipedia.org/wiki/BioWare",
        "tags": ["gaming", "bioware", "rpg", "history", "canada"]
    },
    {
        "id": "gaming_hard_040",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού παιχνιδιού περιπέτειας των αδελφών Robyn και Rand Miller (Cyan Worlds, 1993), που υπήρξε το κορυφαίο σε πωλήσεις PC game παγκοσμίως μέχρι το The Sims (2002);",
        "correct": "Myst",
        "distractors": [
            "Riven",
            "The 7th Guest",
            "Gabriel Knight"
        ],
        "explanation": "Το Myst πούλησε πάνω από 6 εκατομμύρια αντίτυπα και θεωρείται ο κύριος υπεύθυνος για την καθιέρωση των οδηγών CD-ROM στα οικιακά PC της δεκαετίας του 1990.",
        "funFacts": [
            "Ολόκληρο το Myst σχεδιάστηκε σε υπολογιστές Macintosh Quadra χρησιμοποιώντας το πρόγραμμα HyperCard.",
            "Οι αδελφοί Miller υποδύθηκαν οι ίδιοι τους ρόλους των αδελφών Sirrus και Achenar στα βίντεο FMV του παιχνιδιού."
        ],
        "source": "https://en.wikipedia.org/wiki/Myst",
        "tags": ["gaming", "myst", "pc", "adventure", "cdrom"]
    },
    {
        "id": "gaming_hard_041",
        "text": "Ποιος Ιάπωνας δημιουργός και επικεφαλής της Polyphony Digital πέρασε 5 χρόνια αναπτύσσοντας το αρχικό 'Gran Turismo' (1997) στο PlayStation με πρωτοφανή φυσική εξομοίωσης;",
        "correct": "Kazunori Yamauchi",
        "distractors": [
            "Yu Suzuki",
            "Ken Kutaragi",
            "Shinya Arimoto"
        ],
        "explanation": "Ο Yamauchi ξεκίνησε την ανάπτυξη του Gran Turismo με μόλις επτά άτομα. Το παιχνίδι πούλησε σχεδόν 11 εκατομμύρια αντίτυπα, όντας το πιο επιτυχημένο παιχνίδι σε πωλήσεις στην ιστορία του PlayStation 1.",
        "funFacts": [
            "Ο Yamauchi είναι επαγγελματίας οδηγός αγώνων ταχύτητας και έχει κερδίσει την κατηγορία του στον διάσημο αγώνα 24 Ωρών του Nürburgring.",
            "Κάθε ήχος κινητήρα στο Gran Turismo ηχογραφήθηκε ζωντανά από πραγματικά αυτοκίνητα σε δυναμόμετρο."
        ],
        "source": "https://en.wikipedia.org/wiki/Gran_Turismo_(1997_video_game)",
        "tags": ["gaming", "gran_turismo", "yamauchi", "playstation", "simulation"]
    },
    {
        "id": "gaming_hard_042",
        "text": "Ποιο ήταν το όνομα του ακυρωμένου μηχανισμού διασύνδεσης κασετών που σχεδίασε η Rare για το 'Banjo-Kazooie' (1998) και 'Donkey Kong 64', ο οποίος εκμεταλλευόταν την παραμονή δεδομένων στη RAM μετά το σβήσιμο της κονσόλας;",
        "correct": "Stop 'N' Swop",
        "distractors": [
            "Lock-On Technology",
            "Memory Swap Link",
            "RAM Retention Bridge"
        ],
        "explanation": "Το Stop 'N' Swop απαιτούσε από τον παίκτη να βγάλει την κασέτα εν ώρα λειτουργίας και να βάλει μια άλλη μέσα σε 1 δευτερόλεπτο. Η Nintendo απαγόρευσε τη λειτουργία επειδή οι νεότερες αναθεωρήσεις του N64 διέγραφαν τη RAM ταχύτερα και υπήρχε κίνδυνος βλάβης.",
        "funFacts": [
            "Στο Banjo-Kazooie έμειναν κλειδωμένα τα 6 μυστηριώδη χρωματιστά αυγά και το παγωμένο κλειδί (Ice Key), εξάπτοντας τη φαντασία των παικτών για χρόνια.",
            "Η λειτουργία υλοποιήθηκε τελικά επίσημα στις επανεκδόσεις των παιχνιδιών στο Xbox Live Arcade το 2008."
        ],
        "source": "https://en.wikipedia.org/wiki/Stop_%27N%27_Swop",
        "tags": ["gaming", "nintendo64", "rare", "banjo_kazooie", "hardware"]
    },
    {
        "id": "gaming_hard_043",
        "text": "Ποιο ήταν το πρώτο online 3D MMORPG που κυκλοφόρησε σε οικιακή κονσόλα (Sega Dreamcast, 2000), δημιουργία της Sonic Team υπό τον Yuji Naka;",
        "correct": "Phantasy Star Online",
        "distractors": [
            "EverQuest Online Adventures",
            "Final Fantasy XI",
            "Monster Hunter"
        ],
        "explanation": "Το Phantasy Star Online έφερε την επανάσταση των online co-op RPGs στις κονσόλες, υποστηρίζοντας τετραπλό co-op μέσω του ενσωματωμένου modem 56k του Dreamcast.",
        "funFacts": [
            "Διέθετε ένα πρωτοποριακό σύστημα αυτόματης μετάφρασης συμβόλων και φράσεων ('Word Select') που επέτρεπε σε Ιάπωνες, Αμερικανούς και Ευρωπαίους να επικοινωνούν απρόσκοπτα.",
            "Η Sega κυκλοφόρησε ειδικό πληκτρολόγιο για το Dreamcast ειδικά για να διευκολύνει το chat στο PSO."
        ],
        "source": "https://en.wikipedia.org/wiki/Phantasy_Star_Online",
        "tags": ["gaming", "dreamcast", "sega", "phantasy_star", "mmo"]
    },
    {
        "id": "gaming_hard_044",
        "text": "Ποιο σύστημα ήχου και ακουστικής προσομοίωσης ανέπτυξε η Looking Glass Studios για το 'Thief: The Dark Project' (1998), καθιστώντας τον ήχο κρίσιμο μηχανισμό επιβίωσης;",
        "correct": "Δυναμική διάδοση ήχου ανάλογα με τα υλικά επιφάνειας και τα ανοίγματα των θυρών",
        "distractors": [
            "Προηχογραφημένα MP3 cues βασισμένα σε triggers απόστασης",
            "Μονοφωνικά footstep samples με τυχαία διακύμανση pitch",
            "Ακουστικό ray-tracing σε ειδική κάρτα επιτάχυνσης DSP"
        ],
        "explanation": "Η Dark Engine υπολόγιζε πώς ο ήχος των βημάτων του Garrett και των φρουρών ταξίδευε μέσα από δωμάτια, διαδρόμους, ανοιχτές πόρτες και υλικά (πλακάκι, ξύλο, χαλί), επιτρέποντας στον παίκτη να εντοπίζει εχθρούς πίσω από τοίχους.",
        "funFacts": [
            "Ο Garrett μπορούσε να χρησιμοποιήσει βέλη με βρύα (moss arrows) για να καλύψει θορυβώδεις μεταλλικές επιφάνειες και να βαδίζει αθόρυβα.",
            "Το Thief θεωρείται ο πατέρας των σύγχρονων stealth παιχνιδιών πρώτου προσώπου."
        ],
        "source": "https://en.wikipedia.org/wiki/Thief:_The_Dark_Project",
        "tags": ["gaming", "thief", "looking_glass", "stealth", "audio"]
    },
    {
        "id": "gaming_hard_045",
        "text": "Ποιος Ιάπωνας δημιουργός της Capcom σκηνοθέτησε το αρχικό 'Devil May Cry' (2001), το οποίο ξεκίνησε αρχικά ως μια πρώιμη πειραματική έκδοση του 'Resident Evil 4';",
        "correct": "Hideki Kamiya",
        "distractors": [
            "Shinji Mikami",
            "Keiji Inafune",
            "Yoshinori Ono"
        ],
        "explanation": "Ο Hideki Kamiya ανέπτυσσε μια έκδοση του RE4 με πρωταγωνιστή τον υπεράνθρωπο Tony. Ο Shinji Mikami έκρινε ότι το γρήγορο, υπερβολικό action στυλ απομακρυνόταν από το survival horror και πρότεινε να γίνει εντελώς νέο franchise.",
        "funFacts": [
            "Ο Kamiya ίδρυσε αργότερα την PlatinumGames και δημιούργησε τα Bayonetta, Okami και The Wonderful 101.",
            "Το σύστημα 'Style Ranking' (Dull, Cool, Bravo, Absolute, Stylish) επιβράβευε την ποικιλία των combos χωρίς ο παίκτης να δέχεται χτυπήματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Devil_May_Cry_(video_game)",
        "tags": ["gaming", "capcom", "devil_may_cry", "kamiya", "action"]
    },
    {
        "id": "gaming_hard_046",
        "text": "Ποιο franchise της Nintendo ήταν τόσο δημοφιλές στην Ιαπωνία ώστε γεννήθηκε ο αστικός μύθος ότι η ιαπωνική κυβέρνηση ψήφισε νόμο που απαγόρευε την κυκλοφορία των παιχνιδιών του σε εργάσιμες ημέρες;",
        "correct": "Dragon Quest (Enix)",
        "distractors": [
            "Final Fantasy",
            "Pokémon",
            "Monster Hunter"
        ],
        "explanation": "Μετά την κυκλοφορία του Dragon Quest III την Τετάρτη 10 Φεβρουαρίου 1988, πάνω από 300 μαθητές συνελήφθησαν για κοπάνα από το σχολείο περιμένοντας στις ουρές. Η Enix αποφάσισε εθελοντικά να κυκλοφορεί τα επόμενα παιχνίδια μόνο Σάββατα.",
        "funFacts": [
            "Δεν υπήρξε ποτέ επίσημος νόμος της Δίαιτας (Κοινοβουλίου), αλλά η συμφωνία της Enix τηρήθηκε ευλαβικά για δεκαετίες.",
            "Το slime, το εμβληματικό χαμογελαστό μπλε τέρας του Dragon Quest, σχεδιάστηκε από τον Akira Toriyama."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon_Quest",
        "tags": ["gaming", "dragon_quest", "japan", "enix", "urban_legend"]
    },
    {
        "id": "gaming_hard_047",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού text adventure (διαδραστική μυθοπλασία) του 1977 από τους Will Crowther και Don Woods, που αποτέλεσε την απαρχή ολόκληρου του είδους των adventure games;",
        "correct": "Colossal Cave Adventure (γνωστό και ως ADVENT)",
        "distractors": [
            "Zork",
            "Mystery House",
            "The Hitchhiker's Guide to the Galaxy"
        ],
        "explanation": "Το Colossal Cave Adventure γράφτηκε σε Fortran για υπολογιστές PDP-10. Βασίστηκε στη χαρτογράφηση του πραγματικού σπηλαίου Mammoth Cave στο Κεντάκι, εμπλουτισμένο με στοιχεία Dungeons & Dragons.",
        "funFacts": [
            "Η μαγική λέξη 'XYZZY' που χρησιμοποιούσε ο παίκτης για να τηλεμεταφερθεί έγινε κλασικό μυστικό σύνθημα στην κουλτούρα των χάκερ και των video games.",
            "Από αυτό το παιχνίδι πήρε το όνομά του ολόκληρο το είδος των 'Adventure' games."
        ],
        "source": "https://en.wikipedia.org/wiki/Colossal_Cave_Adventure",
        "tags": ["gaming", "retro", "text_adventure", "pdp10", "history"]
    },
    {
        "id": "gaming_hard_048",
        "text": "Ποιο εμβληματικό shooter της id Software το 1996 εισήγαγε πλήρη 3D rendering με πολυγωνικά μοντέλα (αντί για 2D sprites) και καθιέρωσε το TCP/IP δικτυακό παιχνίδι με client-side prediction;",
        "correct": "Quake",
        "distractors": [
            "Duke Nukem 3D",
            "Unreal",
            "Doom II"
        ],
        "explanation": "Ο John Carmack έγραψε τη μηχανή του Quake (Quake engine) εξ ολοκλήρου σε πραγματικό 3D με lightmaps και z-buffering. Με το QuakeWorld (1996) εισήγαγε το client-side prediction, επιτρέποντας ομαλό online gaming σε συνδέσεις dial-up.",
        "funFacts": [
            "Το soundtrack και τα ηχητικά εφέ του Quake δημιουργήθηκαν από τον Trent Reznor των Nine Inch Nails, με το λογότυπο 'NIИ' να εμφανίζεται στα κουτιά των πυρομαχικών του nailgun.",
            "Το Quake γέννησε την κουλτούρα του competitive deathmatch esports και του machinima (κινηματογράφηση μέσα σε game engines)."
        ],
        "source": "https://en.wikipedia.org/wiki/Quake_(video_game)",
        "tags": ["gaming", "quake", "id_software", "carmack", "fps"]
    },
    {
        "id": "gaming_hard_049",
        "text": "Ποιο franchise παιχνιδιών στρατηγικής της Sid Meier (MicroProse, 1991) καθιέρωσε το είδος '4X', προσκαλώντας τον παίκτη να 'χτίσει μια αυτοκρατορία που θα αντέξει στη δοκιμασία του χρόνου';",
        "correct": "Civilization",
        "distractors": [
            "Colonization",
            "Alpha Centauri",
            "Master of Orion"
        ],
        "explanation": "Το Civilization δημιούργησε τη φόρμουλα των 4X (eXplore, eXpand, eXploit, eXterminate), επιτρέποντας στον παίκτη να καθοδηγήσει έναν πολιτισμό από την Εποχή του Χαλκού έως τη Διαστημική Εποχή.",
        "funFacts": [
            "Το διάσημο φαινόμενο 'Nuclear Gandhi' (όπου ο ειρηνιστής Γκάντι εκτόξευε πυρηνικά) ξεκίνησε ως αστικός μύθος για δήθεν integer underflow bug, αλλά έγινε σκόπιμο easter egg στα νεότερα sequels.",
            "Το Civilization είναι διάσημο για το σύνδρομο 'Just one more turn' (Μόνο έναν γύρο ακόμα) που κρατά τους παίκτες άγρυπνους μέχρι το πρωί."
        ],
        "source": "https://en.wikipedia.org/wiki/Civilization_(video_game)",
        "tags": ["gaming", "civilization", "sid_meier", "strategy", "4x"]
    },
    {
        "id": "gaming_hard_050",
        "text": "Ποιο είναι το όνομα του διάσημου chip ειδικών γραφικών (coprocessor) που σχεδίασε η Argonaut Games και ενσωματώθηκε στην κασέτα του 'Star Fox' (1993) για το Super Nintendo;",
        "correct": "Super FX",
        "distractors": [
            "DSP-1",
            "Cx4",
            "SA-1"
        ],
        "explanation": "Το τσιπ Super FX (σχεδιασμένο από τον Jez San και την ομάδα της Argonaut) ήταν ένας επεξεργαστής RISC 16-bit που αναλάμβανε τον υπολογισμό των 3D πολυγώνων και τη σχεδίασή τους στο frame buffer του SNES.",
        "funFacts": [
            "Το Super FX ήταν στην πραγματικότητα ταχύτερο και ισχυρότερο από τον κύριο επεξεργαστή της ίδιας της κονσόλας Super Nintendo.",
            "Χρησιμοποιήθηκε επίσης σε αναβαθμισμένη έκδοση (Super FX 2) στο Super Mario World 2: Yoshi's Island και στο Doom."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_FX",
        "tags": ["gaming", "snes", "star_fox", "super_fx", "hardware"]
    },
    {
        "id": "gaming_hard_051",
        "text": "Στο 'The Legend of Zelda: Ocarina of Time' (1998), ποιο dungeon έγινε διαβόητο μεταξύ των παικτών για τη δυσκολία πλοήγησης, την αλλαγή στάθμης νερού και το συνεχές άνοιγμα του μενού για τις Iron Boots;",
        "correct": "Water Temple (Ναός του Νερού)",
        "distractors": [
            "Shadow Temple",
            "Spirit Temple",
            "Forest Temple"
        ],
        "explanation": "Ο Ναός του Νερού απαιτούσε συνεχείς μεταβολές της στάθμης του νερού σε 3 επίπεδα και εξοπλισμό των Iron Boots μέσα από το μενού παύσης, κάνοντας τον Shigeru Miyamoto και τον Eiji Aonuma να ζητήσουν δημόσια συγγνώμη.",
        "funFacts": [
            "Στο 3DS remake (2011), η Nintendo πρόσθεσε φωτεινούς οδηγούς στους τοίχους και επέτρεψε τον άμεσο εξοπλισμό των Iron Boots μέσω της οθόνης αφής χωρίς παύση.",
            "Στο Water Temple ο Link αντιμετώπιζε έναν από τους πιο εμβληματικούς mini-bosses της σειράς, τον Dark Link."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time",
        "tags": ["gaming", "zelda", "nintendo64", "water_temple", "design"]
    },
    {
        "id": "gaming_hard_052",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού first-person immersive sim της Looking Glass Studios (1994) με σκηνοθέτη τον Doug Church και villain την κακόβουλη τεχνητή νοημοσύνη SHODAN;",
        "correct": "System Shock",
        "distractors": [
            "Deus Ex",
            "BioShock",
            "Ultima Underworld"
        ],
        "explanation": "Το System Shock έθεσε τα θεμέλια των σύγχρονων immersive sims με 3D φυσική, ηχητικά αρχεία καταγραφής (audio logs) και μη γραμμική εξερεύνηση στον διαστημικό σταθμό Citadel.",
        "funFacts": [
            "Η SHODAN (φωνή της Terri Brosius) θεωρείται από τους κορυφαίους κακούς στην ιστορία των video games.",
            "Το παιχνίδι επηρέασε άμεσα τίτλους όπως τα Deus Ex, BioShock, Dead Space και Prey."
        ],
        "source": "https://en.wikipedia.org/wiki/System_Shock",
        "tags": ["gaming", "system_shock", "shodan", "looking_glass", "pc"]
    },
    {
        "id": "gaming_hard_053",
        "text": "Ποιο επαναστατικό physics puzzle game του 2004 από τη Valve έδειξε τη δύναμη της μηχανής Havok Physics μέσα από το 'Gravity Gun' (Zero Point Energy Field Manipulator);",
        "correct": "Half-Life 2",
        "distractors": [
            "Portal",
            "F.E.A.R.",
            "Crysis"
        ],
        "explanation": "Το Half-Life 2 ενσωμάτωσε τη φυσική ως κεντρικό πυλώνα του gameplay. Το Gravity Gun επέτρεπε στον Gordon Freeman να σηκώνει αντικείμενα του περιβάλλοντος (από κιβώτια μέχρι πριονωτούς δίσκους) και να τα εκτοξεύει ως φονικά όπλα.",
        "funFacts": [
            "Η πίστα 'Ravenholm' σχεδιάστηκε ειδικά για να αναδείξει τις δυνατότητες του Gravity Gun σε ένα περιβάλλον γεμάτο ζόμπι και παγίδες.",
            "Το Half-Life 2 ήταν το πρώτο παιχνίδι που απαιτούσε υποχρεωτική εγκατάσταση της πλατφόρμας Steam, προκαλώντας τότε έντονες αντιδράσεις στους παίκτες."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2",
        "tags": ["gaming", "valve", "halflife2", "physics", "steam"]
    },
    {
        "id": "gaming_hard_054",
        "text": "Ποιο studio ανάπτυξης δημιούργησε το 'Demon's Souls' (2009) για το PlayStation 3, γεννώντας το παγκόσμιο φαινόμενο του είδους 'Soulslike' υπό την καθοδήγηση του Hidetaka Miyazaki;",
        "correct": "FromSoftware",
        "distractors": [
            "Team Ninja",
            "Capcom",
            "PlatinumGames"
        ],
        "explanation": "Το project του Demon's Souls θεωρούνταν εσωτερικά αποτυχημένο μέχρι που ο Hidetaka Miyazaki ανέλαβε τη διεύθυνση, άλλαξε τη φιλοσοφία της δυσκολίας και δημιούργησε ένα σκοτεινό action RPG χωρίς συμβιβασμούς.",
        "funFacts": [
            "Ο τότε πρόεδρος των Sony Worldwide Studios, Shuhei Yoshida, έπαιξε το παιχνίδι πριν την κυκλοφορία και το χαρακτήρισε αρχικά 'απίστευτα κακό παιχνίδι', αρνούμενος να το εκδώσει στη Δύση.",
            "Η επιτυχία του Demon's Souls μέσω εισαγωγών οδήγησε στη δημιουργία του Dark Souls και στην παγκόσμια καταξίωση της FromSoftware."
        ],
        "source": "https://en.wikipedia.org/wiki/Demon%27s_Souls",
        "tags": ["gaming", "fromsoftware", "miyazaki", "souls", "playstation"]
    },
    {
        "id": "gaming_hard_055",
        "text": "Ποιο ήταν το όνομα της επαναστατικής arcade πλακέτας που κυκλοφόρησε η SNK το 1990, επιτρέποντας στους ιδιοκτήτες arcades να αλλάζουν έως και 6 παιχνίδια με απλές κασέτες (cartridges);",
        "correct": "Neo Geo MVS (Multi Video System)",
        "distractors": [
            "Capcom CPS-2",
            "Sega Model 2",
            "Namco System 22"
        ],
        "explanation": "Το Neo Geo MVS έφερε επανάσταση στα arcades μειώνοντας δραστικά το κόστος για τους καταστηματάρχες. Η οικιακή του έκδοση, το Neo Geo AES, ήταν ακριβώς το ίδιο arcade hardware σε οικιακή κονσόλα.",
        "funFacts": [
            "Οι κασέτες του Neo Geo AES κόστιζαν συχνά πάνω από 200-300 δολάρια η καθεμία λόγω του τεράστιου μεγέθους μνήμης ROM ('100 Mega Shock').",
            "Το Neo Geo φιλοξένησε θρυλικές σειρές fighting games όπως τα The King of Fighters, Fatal Fury, Samurai Shodown και Metal Slug."
        ],
        "source": "https://en.wikipedia.org/wiki/Neo_Geo_(system)",
        "tags": ["gaming", "arcade", "snk", "neogeo", "hardware"]
    },
    {
        "id": "gaming_hard_056",
        "text": "Στο 'Final Fantasy VI' (1994) στο SNES, ποια σκηνή θεωρείται ένα από τα μεγαλύτερα καλλιτεχνικά επιτεύγματα των 16-bit games, με συνθέτη τον Nobuo Uematsu;",
        "correct": "Η Σκηνή της Όπερας (Aria di Mezzo Carattere)",
        "distractors": [
            "Η Καταστροφή του Κόσμου από τον Kefka",
            "Ο Χορός των Chocobo",
            "Η Τελική Μάχη με το Dancing Mad"
        ],
        "explanation": "Στη σκηνή της όπερας, η Celes αναλαμβάνει τον ρόλο της τραγουδίστριας Maria. Ο Uematsu συνέθεσε μια πλήρη οπερατική άρια εξομοιώνοντας την ανθρώπινη φωνή μέσω του chip ήχου SPC700 του SNES.",
        "funFacts": [
            "Ο Uematsu έγραψε το κομμάτι χωρίς να γνωρίζει αν το hardware του SNES θα μπορούσε να υποστηρίξει φωνητικά samples, καταφεύγοντας σε συνθετικά φωνήεντα.",
            "Η σκηνή αποτέλεσε έμπνευση για την καθιέρωση συμφωνικών συναυλιών video game μουσικής παγκοσμίως (Distant Worlds)."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VI",
        "tags": ["gaming", "final_fantasy", "snes", "music", "uematsu"]
    },
    {
        "id": "gaming_hard_057",
        "text": "Ποιο ήταν το όνομα της μυστηριώδους οντότητας στο MMORPG 'Ultima Online' που δολοφονήθηκε από έναν παίκτη με το όνομα Rainz κατά τη διάρκεια της beta δοκιμής το 1997, σοκάροντας τον δημιουργό Richard Garriott;",
        "correct": "Lord British (ο αθάνατος βασιλιάς του κόσμου)",
        "distractors": [
            "Lord Blackthorn",
            "Mondain the Wizard",
            "The Avatar"
        ],
        "explanation": "Ο Richard Garriott (ως Lord British) απευθυνόταν στους παίκτες πιστεύοντας ότι ο χαρακτήρας του είχε god mode. Ένας server crash όμως είχε απενεργοποιήσει την αθανασία του, και ο Rainz τον σκότωσε επιτόπου με ένα ξόρκι φωτιάς (Fire Field).",
        "funFacts": [
            "Ο Garriott αρχικά δεν πίστευε ότι πέθανε μέχρι που είδε το πτώμα του Lord British στο πάτωμα.",
            "Η δολοφονία του Lord British θεωρείται μία από τις πιο διάσημες στιγμές στην ιστορία των διαδικτυακών εικονικών κόσμων."
        ],
        "source": "https://en.wikipedia.org/wiki/Lord_British#Assassination_of_Lord_British",
        "tags": ["gaming", "ultima_online", "garriott", "mmo", "history"]
    },
    {
        "id": "gaming_hard_058",
        "text": "Ποιο επαναστατικό FPS της Bungie το 2001 όρισε τη σύγχρονη διάταξη των dual-stick χειριστηρίων στις κονσόλες, την αναγεννώμενη ασπίδα και το όριο των δύο όπλων;",
        "correct": "Halo: Combat Evolved",
        "distractors": [
            "Medal of Honor: Frontline",
            "Red Faction",
            "TimeSplitters"
        ],
        "explanation": "Το Halo σχεδιάστηκε αποκλειστικά γύρω από τον κανόνα των '30 δευτερολέψεων διασκέδασης' (πυροβολισμός, χειροβομβίδα, χτύπημα σώμα με σώμα), αποδεικνύοντας ότι τα FPS μπορούν να παίζονται άψογα με χειριστήριο.",
        "funFacts": [
            "Το Halo ξεκίνησε αρχικά την ανάπτυξή του ως real-time strategy παιχνίδι για υπολογιστές Mac και παρουσιάστηκε επίσημα από τον Steve Jobs το 1999 πριν εξαγοραστεί η Bungie από τη Microsoft.",
            "Το 'Warthog' έγινε ένα από τα πιο αναγνωρίσιμα οχήματα στην ιστορία των video games χάρη στο καινοτόμο σύστημα οδήγησης με τον μοχλό της κάμερας."
        ],
        "source": "https://en.wikipedia.org/wiki/Halo:_Combat_Evolved",
        "tags": ["gaming", "halo", "bungie", "xbox", "fps"]
    },
    {
        "id": "gaming_hard_059",
        "text": "Ποιο διάσημο παιχνίδι περιπέτειας της LucasArts (1998) σε σκηνοθεσία Tim Schafer συνδύασε τη μεξικανική γιορτή Día de los Muertos με στοιχεία film noir και jazz μουσική;",
        "correct": "Grim Fandango",
        "distractors": [
            "Full Throttle",
            "Day of the Tentacle",
            "Sam & Max Hit the Road"
        ],
        "explanation": "Στο Grim Fandango ο παίκτης ελέγχει τον Manny Calavera, έναν ταξιδιωτικό πράκτορα ψυχών στο Land of the Dead. Ήταν το πρώτο παιχνίδι της LucasArts που χρησιμοποίησε 3D χαρακτήρες πάνω σε προ-αποδοσμένα 2D υπόβαθρα (GrimE engine).",
        "funFacts": [
            "Παρά τις διθυραμβικές κριτικές, οι χαμηλές πωλήσεις του Grim Fandango συνέβαλαν στην παρακμή των adventure games μεγάλου προϋπολογισμού στα τέλη της δεκαετίας του '90.",
            "Το εξαιρετικό soundtrack του Peter McConnell ηχογραφήθηκε με ζωντανή ορχήστρα jazz και mariachi."
        ],
        "source": "https://en.wikipedia.org/wiki/Grim_Fandango",
        "tags": ["gaming", "lucasarts", "grim_fandango", "adventure", "schafer"]
    },
    {
        "id": "gaming_hard_060",
        "text": "Ποιο παιχνίδι δράσης της Sega στο Dreamcast (1999) από τον Yu Suzuki υπήρξε το πιο ακριβό video game στην ιστορία της εποχής του (κόστους άνω των 47 εκατομμυρίων δολαρίων), πρωτοπορώντας με ανοιχτό κόσμο, πλήρη κύκλο ημέρας/νύχτας και Quick Time Events (QTE);",
        "correct": "Shenmue",
        "distractors": [
            "Yakuza",
            "Virtua Fighter 3",
            "Jet Set Radio"
        ],
        "explanation": "Το Shenmue ξεκίνησε ως 'Project Berkeley' (ένα Virtua Fighter RPG για το Sega Saturn) πριν μεταφερθεί στο Dreamcast. Εισήγαγε τον όρο 'FREE' (Full Reactive Eyes Entertainment) και καθιέρωσε τα μοντέρνα QTEs.",
        "funFacts": [
            "Κάθε χαρακτήρας στην πόλη της Yokosuka είχε το δικό του μοναδικό καθημερινό πρόγραμμα, φωνή και σπίτι.",
            "Για να αποσβέσει το κόστος παραγωγής του, υπολογίστηκε ότι κάθε κάτοχος Sega Dreamcast στον πλανήτη θα έπρεπε να αγοράσει το παιχνίδι δύο φορές."
        ],
        "source": "https://en.wikipedia.org/wiki/Shenmue_(video_game)",
        "tags": ["gaming", "sega", "dreamcast", "shenmue", "open_world"]
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 1.")
    validate_and_append("gaming", "hard", 5, questions)

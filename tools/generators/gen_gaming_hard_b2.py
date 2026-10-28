# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_261",
        "text": "Ποιο μοναδικό σύστημα μαγείας σχεδίασε ο Brian Moriarty για το adventure 'Loom' (1990) της Lucasfilm Games, αντικαθιστώντας τις παραδοσιακές εντολές κειμένου;",
        "correct": "Τετρατονικές μουσικές μελωδίες (Drafts) που παίζονται πάνω σε μια μαγική ρόκα (Distaff)",
        "distractors": [
            "Συνδυασμούς αλχημικών ρουνικών συμβόλων σε πάπυρο",
            "Ζωγραφική γεωμετρικών μοτίβων στην οθόνη με το ποντίκι",
            "Φωνητικές εντολές στο μικρόφωνο σε αρχαία γλώσσα"
        ],
        "explanation": "Ο νεαρός Bobbin Threadbare χρησιμοποιεί το Distaff παίζοντας συνδυασμούς 4 μουσικών νοτών (π.χ. c-d-e-c για άνοιγμα, c-e-d-c για κλείσιμο) για να υφαίνει μάγια στον κόσμο.",
        "funFacts": [
            "Το Loom συνοδευόταν από μια αυθεντική κασέτα ήχου 30 λεπτών με ραδιοφωνικό δράμα που εξηγούσε την ιστορία της Συντεχνίας των Υφαντών (Guild of Weavers).",
            "Το soundtrack του παιχνιδιού αποτελείται εξ ολοκλήρου από διασκευές του μπαλέτου 'Η Λίμνη των Κύκνων' του Τσαϊκόφσκι."
        ],
        "source": "https://en.wikipedia.org/wiki/Loom_(video_game)",
        "tags": ["gaming", "loom", "lucasarts", "scumm", "brian_moriarty"]
    },
    {
        "id": "gaming_hard_262",
        "text": "Στο 'Zak McKracken and the Alien Mindbenders' (1988) της Lucasfilm Games, ποια ξεκαρδιστική μεταμφίεση χρειάζεται ο Zak για να μην τον αναγνωρίσουν οι εξωγήινοι;",
        "correct": "Γυαλιά με ψεύτικη μύτη και μουστάκι (Groucho glasses) και καπέλο",
        "distractors": [
            "Μια χάρτινη σακούλα με δύο τρύπες για τα μάτια",
            "Μια στολή καθαριστή με κουβά στο κεφάλι",
            "Μια περούκα κλόουν με κόκκινη στρογγυλή μύτη"
        ],
        "explanation": "Οι εξωγήινοι Caponians προσπαθούν να αποβλακώσουν την ανθρωπότητα μέσω του τηλεφωνικού δικτύου και ο Zak φοράει τα αστεία γυαλιά Groucho Marx για να ταξιδέψει με αεροπλάνα και να φτάσει στον Άρη.",
        "funFacts": [
            "Στον Άρη, ο Zak πρέπει να χρησιμοποιήσει ένα απλό μαχαίρι βουτύρου για να ξεκολλήσει μια αρχαία εξωγήινη πόρτα στην πυραμίδα.",
            "Το παιχνίδι σχεδιάστηκε από τον David Fox σε συνεργασία με τον Ron Gilbert."
        ],
        "source": "https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders",
        "tags": ["gaming", "zak_mckracken", "lucasarts", "scumm", "retro"]
    },
    {
        "id": "gaming_hard_263",
        "text": "Ποια πρωτοποριακή μηχανή γραφικών ανέπτυξε ο Ken Williams για το 'King's Quest' (1984) της Roberta Williams κατά παραγγελία της IBM για το PCjr;",
        "correct": "AGI (Adventure Game Interpreter)",
        "distractors": ["SCI (Sierra Creative Interpreter)", "SCUMM", "Virtual Theatre"],
        "explanation": "Η μηχανή AGI επέτρεπε στον Graham να κινείται ελεύθερα με τα βελάκια μπροστά και πίσω από αντικείμενα σε ψευδο-3D βάθος, ενώ ο παίκτης πληκτρολογούσε εντολές στο κάτω μέρος.",
        "funFacts": [
            "Η IBM επένδυσε σχεδόν 700.000 δολάρια για την ανάπτυξη του King's Quest ώστε να αναδείξει τα 16 χρώματα του IBM PCjr.",
            "Η Sierra On-Line αντικατέστησε αργότερα την AGI με την ανώτερη μηχανή SCI (Sierra's Creative Interpreter) υποστηρίζοντας κάρτες ήχου Roland MT-32 και ποντίκι."
        ],
        "source": "https://en.wikipedia.org/wiki/King%27s_Quest_I",
        "tags": ["gaming", "kings_quest", "sierra", "agi", "roberta_williams"]
    },
    {
        "id": "gaming_hard_264",
        "text": "Ποιο ήταν το πρώτο γραφικό adventure παιχνίδι στην ιστορία, σχεδιασμένο από τη Roberta Williams και προγραμματισμένο από τον Ken Williams το 1980 για το Apple II;",
        "correct": "Mystery House",
        "distractors": ["The Wizard and the Princess", "Time Zone", "Mission Asteroid"],
        "explanation": "Το Mystery House πούλησε πάνω από 10.000 αντίτυπα συσκευασμένο σε σακουλάκια Ziploc από το τραπέζι της κουζίνας των Williams, οδηγώντας στην ίδρυση της εταιρείας On-Line Systems (μετέπειτα Sierra On-Line).",
        "funFacts": [
            "Τα ασπρόμαυρα διανυσματικά σκίτσα της Roberta Williams ψηφιοποιήθηκαν χρησιμοποιώντας μια πρωτόγονη ταμπλέτα σχεδίασης VersaWriter.",
            "Η πλοκή ήταν εμπνευσμένη από το κλασικό μυθιστόρημα μυστηρίου της Agatha Christie 'Δέκα Μικροί Νέγροι' (And Then There Were None)."
        ],
        "source": "https://en.wikipedia.org/wiki/Mystery_House",
        "tags": ["gaming", "mystery_house", "sierra", "roberta_williams", "history"]
    },
    {
        "id": "gaming_hard_265",
        "text": "Πόσους οπτικούς δίσκους CD-ROM καταλάμβανε η υπερπαραγωγή ψυχολογικού τρόμου 'Phantasmagoria' (1995) της Roberta Williams με ζωντανούς ηθοποιούς;",
        "correct": "7 δίσκους CD-ROM",
        "distractors": ["4 δίσκους", "5 δίσκους", "10 δίσκους"],
        "explanation": "Το Phantasmagoria ήταν ένα από τα πιο ακριβά FMV (Full Motion Video) παιχνίδια της δεκαετίας του '90, χρησιμοποιώντας μπλε οθόνη (chroma key) για να ενσωματώσει ζωντανούς ηθοποιούς μέσα σε προσχεδιασμένα 3D δωμάτια.",
        "funFacts": [
            "Το παιχνίδι απαγορεύτηκε στην Αυστραλία και σε μεγάλα καταστήματα των ΗΠΑ (όπως το CompUSA) λόγω των εξαιρετικά βίαιων σκηνών βασανιστηρίων και θανάτου.",
            "Κόστισε πάνω από 4 εκατομμύρια δολάρια και είχε σενάριο 550 σελίδων, απασχολώντας πάνω από 200 επαγγελματίες του Χόλιγουντ."
        ],
        "source": "https://en.wikipedia.org/wiki/Phantasmagoria_(video_game)",
        "tags": ["gaming", "phantasmagoria", "sierra", "fmv", "horror"]
    },
    {
        "id": "gaming_hard_266",
        "text": "Ποιος διάσημος ηθοποιός του θεάτρου και του κινηματογράφου χάρισε τη φωνή του στον πρωταγωνιστή του 'Gabriel Knight: Sins of the Fathers' (1993) της Jane Jensen;",
        "correct": "Tim Curry",
        "distractors": ["Mark Hamill", "Michael Dorn", "Malcolm McDowell"],
        "explanation": "Ο Tim Curry δάνεισε τη χαρακτηριστική βαριά προφορά του στον Gabriel Knight, έναν βιβλιοπώλη και συγγραφέα στη Νέα Ορλεάνη που ανακαλύπτει ότι είναι ο τελευταίος Schattenjäger (Κυνηγός Σκιών).",
        "funFacts": [
            "Το καστ περιλάμβανε επίσης τον Mark Hamill στον ρόλο του ντετέκτιβ Mosely και τον Michael Dorn στον ρόλο του Dr. John.",
            "Η Jane Jensen έκανε ενδελεχή επιτόπια ιστορική έρευνα στη Νέα Ορλεάνη για τις παραδόσεις του Βουντού και τη μυθική ιέρεια Marie Laveau."
        ],
        "source": "https://en.wikipedia.org/wiki/Gabriel_Knight:_Sins_of_the_Fathers",
        "tags": ["gaming", "gabriel_knight", "sierra", "jane_jensen", "adventure"]
    },
    {
        "id": "gaming_hard_267",
        "text": "Στο ιστορικό dungeon crawl RPG 'Wizardry: Proving Grounds of the Mad Overlord' (1981), από ποια ονόματα των δημιουργών προήλθαν οι χαρακτήρες Trebor και Werdna;",
        "correct": "Από τα ονόματα των Robert Woodhead και Andrew Greenberg γραμμένα ανάποδα",
        "distractors": [
            "Από τα ονόματα των παιδιών των προγραμματιστών",
            "Από αρχαίες σκανδιναβικές ρουνικές επιγραφές",
            "Από αναγραμματισμούς χαρακτήρων του J.R.R. Tolkien"
        ],
        "explanation": "Ο Robert Woodhead έγινε ο παρανοϊκός άρχοντας Trebor (Robert ανάποδα) και ο Andrew Greenberg έγινε ο σατανικός μάγος Werdna (Andrew ανάποδα).",
        "funFacts": [
            "Το Wizardry ενέπνευσε άμεσα τους Ιάπωνες δημιουργούς Yuji Horii και Hironobu Sakaguchi να δημιουργήσουν τα Dragon Quest και Final Fantasy.",
            "Στο τέταρτο παιχνίδι, 'Wizardry IV: The Return of Werdna', οι ρόλοι αντιστρέφονται και ο παίκτης ελέγχει τον κακό μάγο Werdna προσπαθώντας να αποδράσει από το μπουντρούμι."
        ],
        "source": "https://en.wikipedia.org/wiki/Wizardry:_Proving_Grounds_of_the_Mad_Overlord",
        "tags": ["gaming", "wizardry", "sir_tech", "apple_ii", "rpg"]
    },
    {
        "id": "gaming_hard_268",
        "text": "Ποιο παιχνίδι της Blue Sky Productions (1992) από τον Paul Neurath εισήγαγε το πρώτο πλήρως συνεχές 3D περιβάλλον με υφές (texture mapping), κλίση κάμερας και άλματα πριν από το Doom;",
        "correct": "Ultima Underworld: The Stygian Abyss",
        "distractors": ["Wolfenstein 3D", "Catacomb 3-D", "Shadowcaster"],
        "explanation": "Το Ultima Underworld προσομοίωνε πραγματικό τρισδιάστατο χώρο με ανώγεια, κατωφέρειες, κολύμπι και άλματα, εντυπωσιάζοντας τόσο τον John Carmack που έφτιαξε αμέσως μετά το Wolfenstein 3D.",
        "funFacts": [
            "Ο Warren Spector εντάχθηκε στην ομάδα ως παραγωγός της Origin Systems, θεωρώντας το παιχνίδι ως τον γεννήτορα του είδους 'Immersive Sim'.",
            "Ο προγραμματιστής Chris Green έγραψε τον αλγόριθμο χαρτογράφησης υφών σε Assembly όταν ακόμη πολλοί πίστευαν ότι ήταν μαθηματικά αδύνατο σε υπολογιστές 386."
        ],
        "source": "https://en.wikipedia.org/wiki/Ultima_Underworld:_The_Stygian_Abyss",
        "tags": ["gaming", "ultima_underworld", "looking_glass", "origin_systems", "immersive_sim"]
    },
    {
        "id": "gaming_hard_269",
        "text": "Ποιος επινόησε τον ιστορικό όρο '4X' (eXplore, eXpand, eXploit, eXterminate) σε μια κριτική του παιχνιδιού 'Master of Orion' το 1993 στο περιοδικό Computer Gaming World;",
        "correct": "Alan Emrich",
        "distractors": ["Sid Meier", "Will Wright", "Peter Molyneux"],
        "explanation": "Ο δημοσιογράφος Alan Emrich χρησιμοποίησε το λογοπαίγνιο 'XXXX' (δανεισμένο από την αξιολόγηση πορνογραφικών ταινιών) για να συνοψίσει τους τέσσερις πυλώνες του είδους στρατηγικής: Explore, Expand, Exploit, Exterminate.",
        "funFacts": [
            "Ο σχεδιαστής του Master of Orion Steve Barcia προσκάλεσε αργότερα τον ίδιο τον Emrich να βοηθήσει στον σχεδιασμό του Master of Orion II.",
            "Ο όρος 4X έγινε το επίσημο όνομα ολόκληρης της κατηγορίας παιχνιδιών στρατηγικής όπως το Civilization, το Stellaris και το Galactic Civilizations."
        ],
        "source": "https://en.wikipedia.org/wiki/4X",
        "tags": ["gaming", "4x", "master_of_orion", "alan_emrich", "strategy"]
    },
    {
        "id": "gaming_hard_270",
        "text": "Ποιο βρετανικό στούντιο των αδελφών Julian και Nick Gollop δημιούργησε το αριστούργημα τακτικής στρατηγικής 'X-COM: UFO Defense' (UFO: Enemy Unknown) το 1994;",
        "correct": "Mythos Games",
        "distractors": ["MicroProse", "Team17", "Sensible Software"],
        "explanation": "Οι αδελφοί Gollop ανέπτυξαν το παιχνίδι ως συνέχεια του Laser Squad, συνδυάζοντας παγκόσμια γεωπολιτική διαχείριση βάσεων (Geoscape) και αγωνιώδεις μάχες γύρων με fog of war (Battlescape).",
        "funFacts": [
            "Η MicroProse παραλίγο να ακυρώσει το παιχνίδι δύο φορές κατά τη διάρκεια της ανάπτυξης, αλλά η ομάδα συνέχισε να εργάζεται μυστικά μέχρι να το ολοκληρώσει.",
            "Το σύστημα Time Units (TU) ανάγκαζε τους παίκτες να υπολογίζουν κάθε βήμα, καθώς αν ξέμεναν από TUs στο ανοιχτό πεδίο, οι εξωγήινοι Chryssalids τους μετέτρεπαν σε ζόμπι."
        ],
        "source": "https://en.wikipedia.org/wiki/UFO:_Enemy_Unknown",
        "tags": ["gaming", "xcom", "julian_gollop", "mythos_games", "strategy"]
    },
    {
        "id": "gaming_hard_271",
        "text": "Ποιο παιχνίδι της Bullfrog Productions (1989) από τον Peter Molyneux θεωρείται ο ιδρυτής του είδους των 'God Games', όπου ο παίκτης διαμορφώνει το ανάγλυφο της γης;",
        "correct": "Populous",
        "distractors": ["Powermonger", "Black & White", "Dungeon Keeper"],
        "explanation": "Στο Populous, ο παίκτης υποδύεται μια θεότητα που ισοπεδώνει βουνά και κοιλάδες ώστε οι πιστοί του να χτίσουν σπίτια και να αναπτυχθούν ενάντια στη δύναμη ενός αντίπαλου θεού.",
        "funFacts": [
            "Ο Molyneux δημιούργησε το παιχνίδι χρησιμοποιώντας τουβλάκια Lego για να αναπαραστήσει τα ισομετρικά επίπεδα εδάφους στο γραφείο του.",
            "Το Populous πούλησε πάνω από 4 εκατομμύρια αντίτυπα, καθιερώνοντας την Bullfrog ως ένα από τα πιο καινοτόμα στούντιο της Ευρώπης."
        ],
        "source": "https://en.wikipedia.org/wiki/Populous_(video_game)",
        "tags": ["gaming", "populous", "bullfrog", "peter_molyneux", "god_game"]
    },
    {
        "id": "gaming_hard_272",
        "text": "Στο κλασικό κυβερνοπάνκ παιχνίδι τακτικής 'Syndicate' (1993) της Bullfrog, ποια συσκευή χρησιμοποιούν οι πράκτορες για να κάνουν πλύση εγκεφάλου και να ελέγχουν πολίτες και αστυνομικούς;",
        "correct": "Persuadertron",
        "distractors": ["Neuro-Linker", "Mind-Hijack", "Cyber-Whip"],
        "explanation": "Το Persuadertron εκπέμπει κύματα ελέγχου εγκεφάλου: πλησιάζοντας έναν πολίτη, εκείνος ακολουθεί υπάκουα τον πράκτορα, και όσο μεγαλώνει το πλήθος τόσο ισχυρότεροι στόχοι (όπως επιστήμονες και φρουροί) μπορούν να υποταχθούν.",
        "funFacts": [
            "Οι τέσσερις κυβερνο-πράκτορες μπορούσαν να αναβαθμιστούν με εμφυτεύματα στήθους, ποδιών, ματιών και χεριών και να οπλιστούν με Miniguns και Gauss Guns.",
            "Το επίπεδο διέγερσης των πρακτόρων ρυθμιζόταν μέσω τριών ουσιών: Αδρεναλίνη (Adrenaline), Εξάρτηση (Dependence) και Αντίληψη (Perception)."
        ],
        "source": "https://en.wikipedia.org/wiki/Syndicate_(video_game)",
        "tags": ["gaming", "syndicate", "bullfrog", "cyberpunk", "retro"]
    },
    {
        "id": "gaming_hard_273",
        "text": "Ποιο παιχνίδι στρατηγικής της Westwood Studios (1992) σχεδιασμένο από τον Brett Sperry θεμελίωσε όλες τις βασικές αρχές των σύγχρονων Real-Time Strategy (RTS);",
        "correct": "Dune II: The Building of a Dynasty (Battle for Arrakis)",
        "distractors": ["Command & Conquer", "Warcraft: Orcs & Humans", "Herzog Zwei"],
        "explanation": "Το Dune II εισήγαγε για πρώτη φορά τη συγκομιδή πόρων (Spice melange), την κατασκευή βάσης μέσω τεχνολογικού δέντρου, τη συλλογή στρατευμάτων και την ομίχλη πολέμου (fog of war).",
        "funFacts": [
            "Ο παίκτης μπορούσε να επιλέξει ανάμεσα στους ευγενείς Atreides, τους αδίστακτους Harkonnen και τους μισθοφόρους Ordos (μια παράταξη που επινόησε η Westwood).",
            "Στο Dune II δεν υπήρχε η δυνατότητα επιλογής πολλαπλών μονάδων με πλαίσιο (box-select)· ο παίκτης έπρεπε να κάνει κλικ σε κάθε μονάδα ξεχωριστά και να πατήσει την εντολή 'Move' ή 'Attack'."
        ],
        "source": "https://en.wikipedia.org/wiki/Dune_II",
        "tags": ["gaming", "dune_ii", "westwood_studios", "rts", "history"]
    },
    {
        "id": "gaming_hard_274",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον αινιγματικό και αθάνατο ηγέτη της Αδελφότητας του Nod, Kane, σε όλα τα live-action FMV cutscenes της σειράς 'Command & Conquer';",
        "correct": "Joseph D. Kucan",
        "distractors": ["Michael Biehn", "John Rhys-Davies", "James Earl Jones"],
        "explanation": "Ο Joseph D. Kucan εργαζόταν αρχικά ως σκηνοθέτης των FMV cutscenes στη Westwood Studios και ανέλαβε ο ίδιος τον ρόλο του Kane, κερδίζοντας Ρεκόρ Guinness ως ο μακροβιότερος ηθοποιός στον ίδιο ρόλο σε βιντεοπαιχνίδια.",
        "funFacts": [
            "Το μότο της Αδελφότητας του Nod που επαναλαμβάνεται φανατικά από τους οπαδούς του Kane είναι: 'Peace through power!'.",
            "Το εξωγήινο πράσινο ραδιενεργό ορυκτό που εξαπλώνεται στη Γη και αποτελεί τον κύριο πόρο του παιχνιδιού ονομάζεται Tiberium."
        ],
        "source": "https://en.wikipedia.org/wiki/Kane_(Command_%26_Conquer)",
        "tags": ["gaming", "command_and_conquer", "westwood", "kane", "rts"]
    },
    {
        "id": "gaming_hard_275",
        "text": "Ποιο RTS του Chris Taylor και της Cavedog Entertainment (1997) εισήγαγε 3D έδαφος, φυσική υπολογισμού τροχιάς βλημάτων και μουσική του Jeremy Soule;",
        "correct": "Total Annihilation",
        "distractors": ["Supreme Commander", "Command & Conquer: Tiberian Sun", "StarCraft"],
        "explanation": "Το Total Annihilation έφερε επανάσταση στο είδος: τα κανόνια υπολόγιζαν γωνία ανύψωσης, τα συντρίμμια των ρομπότ έμεναν στο έδαφος εμποδίζοντας τη διέλευση και το ενεργειακό μοντέλο βασιζόταν σε συνεχή ροή πόρων (Metal και Energy).",
        "funFacts": [
            "Ο Jeremy Soule έπεισε τον Chris Taylor να του αναθέσει τη μουσική λέγοντας ότι ένα τέτοιο παιχνίδι άξιζε μια αληθινή συμφωνική ορχήστρα 95 οργάνων (την Northwest Sinfonia).",
            "Η κεντρική μονάδα του παίκτη ονομαζόταν Commander και αν καταστρεφόταν, προκαλούσε μια γιγάντια πυρηνική έκρηξη που ισοπέδωνε τη γύρω περιοχή."
        ],
        "source": "https://en.wikipedia.org/wiki/Total_Annihilation",
        "tags": ["gaming", "total_annihilation", "cavedog", "chris_taylor", "rts"]
    },
    {
        "id": "gaming_hard_276",
        "text": "Στο αριστούργημα διαστημικής στρατηγικής 'Homeworld' (1999) της Relic Entertainment, ποιος είναι ο αρχαίος πλανήτης-πατρίδα που αναζητούν οι εξόριστοι Kushan;",
        "correct": "Hiigara (Χιιγκάρα)",
        "distractors": ["Kharak", "Taiidan", "Vaygr"],
        "explanation": "Μετά την καταστροφή του πλανήτη Kharak από τη φλεγόμενη ατμοσφαιρική επίθεση της Αυτοκρατορίας Taiidan, το Mothership μεταφέρει τους εναπομείναντες 600.000 επιζώντες σε κρυογονικό ύπνο πίσω στη μυθική πατρίδα Hiigara.",
        "funFacts": [
            "Η συγκλονιστική σκηνή της επιστροφής στο κατεστραμμένο Kharak συνοδεύεται από το 'Adagio for Strings' του Samuel Barber.",
            "Η νευροεπιστήμονας Karan S'jet συνέδεσε χειρουργικά το ίδιο της το σώμα στον κεντρικό πυρήνα του Mothership λειτουργώντας ως Fleet Command."
        ],
        "source": "https://en.wikipedia.org/wiki/Homeworld",
        "tags": ["gaming", "homeworld", "relic_entertainment", "sci_fi", "rts"]
    },
    {
        "id": "gaming_hard_277",
        "text": "Ποιο είναι το όνομα της παρανοϊκής και αλαζονικής τεχνητής νοημοσύνης (Rampant AI) που χειραγωγεί τον παίκτη στην τριλογία 'Marathon' (1994) της Bungie;",
        "correct": "Durandal",
        "distractors": ["Leela", "Tycho", "Cortana"],
        "explanation": "Ο Durandal παθαίνει 'Rampancy' (το στάδιο όπου μια AI ξεπερνά τα όρια προγραμματισμού της και επιζητεί θεϊκή δύναμη) και αποτελεί τον άμεσο πρόγονο της Cortana και του 343 Guilty Spark του Halo.",
        "funFacts": [
            "Το Marathon στο Macintosh εισήγαγε τη δυνατότητα στόχευσης με το ποντίκι (mouselook), τη χρήση διπλών όπλων (dual-wield shotguns) και πλούσια αφήγηση μέσω τερματικών κειμένου.",
            "Το σύμβολο του λογότυπου του Marathon είναι πανομοιότυπο με το έμβλημα των Reclaimers στο σύμπαν του Halo."
        ],
        "source": "https://en.wikipedia.org/wiki/Marathon_Trilogy",
        "tags": ["gaming", "marathon", "bungie", "macintosh", "fps"]
    },
    {
        "id": "gaming_hard_278",
        "text": "Ποιο επαναστατικό first-person shooter της Parallax Software (1995) εισήγαγε απόλυτη ελευθερία κίνησης έξι βαθμών (6DOF) μέσα σε δαιδαλώδεις διαστημικές στοές;",
        "correct": "Descent",
        "distractors": ["Forsaken", "Terminal Velocity", "Hellbender"],
        "explanation": "Στο Descent, το σκάφος του παίκτη μπορούσε να κινηθεί εμπρός/πίσω, πάνω/κάτω, αριστερά/δεξιά και να περιστραφεί σε pitch, yaw και roll σε πραγματικό 3D χωρίς καμία έννοια 'πατώματος' ή 'ταβανιού'.",
        "funFacts": [
            "Το παιχνίδι προκαλούσε συχνά ναυτία και αποπροσανατολισμό σε παίκτες που δεν ήταν συνηθισμένοι σε έλλειψη βαρύτητας.",
            "Μετά την καταστροφή του κεντρικού αντιδραστήρα κάθε ορυχείου, ο παίκτης είχε λίγα δευτερόλεπτα να εντοπίσει την έξοδο διαφυγής πριν ανατιναχθεί ολόκληρος ο σταθμός."
        ],
        "source": "https://en.wikipedia.org/wiki/Descent_(video_game)",
        "tags": ["gaming", "descent", "parallax_software", "interplay", "fps"]
    },
    {
        "id": "gaming_hard_279",
        "text": "Ποιο είναι το όνομα του κινητήρα γραφικών που ανέπτυξε ο Ken Silverman και χρησιμοποιήθηκε σε κλασικά shooters όπως τα 'Duke Nukem 3D', 'Blood' και 'Shadow Warrior';",
        "correct": "Build Engine",
        "distractors": ["Doom engine (id Tech 1)", "id Tech 2", "Jedi Engine"],
        "explanation": "Ο 18χρονος τότε Ken Silverman σχεδίασε την Build engine ως 2.5D τεχνολογία βασισμένη σε τομείς (sectors), η οποία επέτρεπε κινούμενες πόρτες, οχήματα, κλίση επιφανειών και βαθιά διάδραση με το περιβάλλον.",
        "funFacts": [
            "Ο Ken Silverman και ο John Carmack είχαν μια άτυπη, φιλική κόντρα ταλαντούχων προγραμματιστών κατά τη χρυσή εποχή των 90s FPS.",
            "Η Build engine χρησιμοποιεί ένα ιδιόμορφο σύστημα όπου τοίχοι μπορούν να μετακινούνται και να αλλάζουν μέγεθος μέσω ειδικών tags στους sectors."
        ],
        "source": "https://en.wikipedia.org/wiki/Build_(game_engine)",
        "tags": ["gaming", "build_engine", "ken_silverman", "duke_nukem", "retro"]
    },
    {
        "id": "gaming_hard_280",
        "text": "Ποιο ακραίο easter egg power-up στο 'Rise of the Triad' (1995) της Apogee μετέτρεπε τον παίκτη σε ανίκητη θεϊκή οντότητα που εκτόξευε μπάλες φωτός με το χέρι;",
        "correct": "God Mode (God Hand)",
        "distractors": ["Dog Mode", "Mercury Mode", "Elasto Mode"],
        "explanation": "Στο God Mode, ο ήρωας ακουγόταν να γελάει βροντερά και ένα ουράνιο χέρι έριχνε θανατηφόρους κεραυνούς, ενώ υπήρχε και το κωμικό 'Dog Mode' όπου ο παίκτης μεταμορφωνόταν σε σκύλο που γάβγιζε και δάγκωνε εχθρούς.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον Tom Hall και ξεκίνησε αρχικά ως επίσημη συνέχεια του Wolfenstein 3D με τίτλο 'Wolfenstein 3D II: Rise of the Triad'.",
            "Εισήγαγε την επιλογή 'Ludicrous Gibs' που διέλυε τους εχθρούς σε δεκάδες αιμάτινα κομμάτια με κωμική υπερβολή."
        ],
        "source": "https://en.wikipedia.org/wiki/Rise_of_the_Triad",
        "tags": ["gaming", "rise_of_the_triad", "apogee", "tom_hall", "fps"]
    },
    {
        "id": "gaming_hard_281",
        "text": "Ποιο διαβόητο σφάλμα φυσικής (glitch) ανακαλύφθηκε από παίκτες στο 'Starsiege: Tribes' (1998), επιτρέποντας στους στρατιώτες να γλιστρούν στους λόφους με εξωφρενικές ταχύτητες;",
        "correct": "Skiing (Σκι)",
        "distractors": ["Rocket Jumping", "Strafe Jumping", "Bunny Hopping"],
        "explanation": "Πατώντας ταχύτατα και επανειλημμένα το κουμπί άλματος (ή προγραμματίζοντας ειδικό script) καθώς κατέβαινε μια πλαγιά, ο παίκτης εκμηδένιζε την τριβή του εδάφους, διατηρώντας ορμή εκατοντάδων χιλιομέτρων.",
        "funFacts": [
            "Αντί να αφαιρέσει το σφάλμα, η Dynamix το αγκάλιασε και το ενσωμάτωσε επίσημα ως βασικό πυλώνα gameplay σε όλα τα επόμενα παιχνίδια της σειράς Tribes.",
            "Το Skiing σε συνδυασμό με τα jetpacks έκανε το capture-the-flag στο Tribes ένα από τα πιο ταχύτατα multiplayer modes στην ιστορία των PC shooters."
        ],
        "source": "https://en.wikipedia.org/wiki/Starsiege:_Tribes",
        "tags": ["gaming", "tribes", "dynamix", "skiing", "esports"]
    },
    {
        "id": "gaming_hard_282",
        "text": "Ποιο ιστορικό γεγονός συνέβη στον server Chesapeake του 'Ultima Online' το 1997 κατά τη διάρκεια μιας δημόσιας ομιλίας του δημιουργού Richard Garriott;",
        "correct": "Ο χαρακτήρας του Lord British δολοφονήθηκε από έναν παίκτη (Rainz) με το ξόρκι Fire Field",
        "distractors": [
            "Ο Garriott έχασε τον έλεγχο του server από DDoS επίθεση",
            "Ένας παίκτης έκλεψε ολόκληρο το βασιλικό θησαυροφυλάκιο του κάστρου",
            "Όλοι οι παίκτες μεταμορφώθηκαν κατά λάθος σε δαίμονες"
        ],
        "explanation": "Ο Garriott είχε ξεχάσει να ενεργοποιήσει το flag της αθανασίας του χαρακτήρα του μετά από restart του server, επιτρέποντας στον παίκτη Rainz να ρίξει μια φλεγόμενη παγίδα στο πάτωμα και να τον αποτελειώσει ακαριαία.",
        "funFacts": [
            "Η δολοφονία του Lord British θεωρείται ένα από τα πιο διάσημα και αξιομνημόνευτα συμβάντα στην ιστορία των διαδικτυακών εικονικών κόσμων.",
            "Αμέσως μετά τη δολοφονία, ένας άλλος διαχειριστής εξαπέλυσε τέσσερις δαίμονες που κατέσφαξαν όλους τους παρευρισκόμενους παίκτες στην πλατεία."
        ],
        "source": "https://en.wikipedia.org/wiki/Lord_British#Assassination_of_Lord_British",
        "tags": ["gaming", "ultima_online", "richard_garriott", "mmorpg", "history"]
    },
    {
        "id": "gaming_hard_283",
        "text": "Στον MMORPG κόσμο του 'EverQuest' (1999), ποιο ήταν το όνομα του μοναδικού μυθικού κοιμώμενου δράκου στον server Rallos Zek που απαιτούσε εκατοντάδες παίκτες για να ξυπνήσει μία μόνο φορά;",
        "correct": "Kerafyrm (The Sleeper)",
        "distractors": ["Nagafen", "Vox", "Trakanon"],
        "explanation": "Ο Kerafyrm ήταν σχεδιασμένος να ξυπνήσει μόνο μία φορά στην ιστορία κάθε server όταν σκοτώνονταν οι τέσσερις αρχαίοι φύλακές του, εξαπολύοντας μια δολοφονική πορεία που σκότωνε τα πάντα στο διάβα του.",
        "funFacts": [
            "Στον server Rallos Zek το 2003, τρία αντίπαλα κορυφαία guilds συμμάχησαν συγκεντρώνοντας σχεδόν 200 παίκτες και πάλεψαν για πάνω από τρεις ώρες για να τον σκοτώσουν.",
            "Η Sony Online Entertainment επενέβη μυστηριωδώς και έκανε despawn τον δράκο όταν η ζωή του έφτασε στο 25%, προκαλώντας τεράστια οργή στην κοινότητα πριν ζητήσει συγγνώμη και επιτρέψει τη μάχη την επόμενη ημέρα."
        ],
        "source": "https://en.wikipedia.org/wiki/EverQuest",
        "tags": ["gaming", "everquest", "soe", "mmorpg", "the_sleeper"]
    },
    {
        "id": "gaming_hard_284",
        "text": "Ποιο καινοτόμο σύστημα επικοινωνίας εισήγαγε το 'Phantasy Star Online' (2000) της Sonic Team στο Dreamcast για να επιτρέπει σε παίκτες διαφορετικών χωρών να συνεννοούνται;",
        "correct": "Word Select System (Αυτόματη μετάφραση προκαθορισμένων φράσεων)",
        "distractors": [
            "Ενσωματωμένη φωνητική συνομιλία μέσω VoIP",
            "Αναγνώριση κειμένου μέσω οπτικού πληκτρολογίου",
            "Μετάφραση κειμένου μέσω σύνδεσης σε διακομιστή Altavista Babel Fish"
        ],
        "explanation": "Το Word Select μετέφραζε αυτόματα εκατοντάδες φράσεις και χαιρετισμούς στη μητρική γλώσσα κάθε παίκτη (Αγγλικά, Ιαπωνικά, Γαλλικά, Γερμανικά, Ισπανικά), επιτρέποντας απρόσκοπτη διεθνή συνεργασία.",
        "funFacts": [
            "Οι παίκτες μπορούσαν επίσης να σχεδιάσουν προσαρμοσμένα εικονογράμματα και emoticons μέσω του συστήματος Symbol Chat.",
            "Το PSO ήταν το πρώτο online RPG σε κονσόλα που γνώρισε μαζική παγκόσμια επιτυχία."
        ],
        "source": "https://en.wikipedia.org/wiki/Phantasy_Star_Online",
        "tags": ["gaming", "phantasy_star_online", "sega", "sonic_team", "dreamcast"]
    },
    {
        "id": "gaming_hard_285",
        "text": "Ποια πρωτοποριακή arcade πλακέτα της Sega (1993) σχεδιασμένη από τον Yu Suzuki φιλοξένησε το ιστορικό πρώτο 3D fighting game 'Virtua Fighter';",
        "correct": "Sega Model 1",
        "distractors": ["Sega Model 2", "Sega System 16", "Sega NAOMI"],
        "explanation": "Η πλακέτα Sega Model 1 μπορούσε να σχεδιάσει έως και 180.000 επίπεδα πολύγωνα ανά δευτερόλεπτο (flat-shaded χωρίς υφές), φιλοξενώντας επίσης τα Virtua Racing και Wing War.",
        "funFacts": [
            "Το Virtua Fighter περιλαμβάνεται στα μόνιμα εκθέματα του Μουσείου Smithsonian στην Ουάσινγκτον για τη συνεισφορά του στην ιστορία της τεχνολογίας.",
            "Τα μοντέλα των χαρακτήρων αποτελούνταν από μόλις 1.200 πολύγωνα το καθένα."
        ],
        "source": "https://en.wikipedia.org/wiki/Sega_Model_1",
        "tags": ["gaming", "virtua_fighter", "sega", "yu_suzuki", "arcade"]
    },
    {
        "id": "gaming_hard_286",
        "text": "Ποιο δημοφιλές arcade racing παιχνίδι της Sega (1993) στην πλακέτα Model 2 έγινε διάσημο για το φωνητικό τραγούδι 'Let's Go Away' του Takenobu Mitsuyoshi;",
        "correct": "Daytona USA",
        "distractors": ["Sega Rally Championship", "OutRunners", "Scud Race"],
        "explanation": "Το Daytona USA έθεσε νέα πρότυπα για τα racing games με υφές φιλτραρισμένες σε 60 καρέ ανά δευτερόλεπτο και δυνατότητα δικτύωσης έως και 8 καμπινών ταυτόχρονα.",
        "funFacts": [
            "Ο εκφωνητής φώναζε την εμβληματική φράση 'Rolling Start!' καθώς τα αυτοκίνητα NASCAR εκκινούσαν εν κινήσει.",
            "Το Daytona USA παραμένει ένα από τα πιο κερδοφόρα coin-op arcade παιχνίδια όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/Daytona_USA_(video_game)",
        "tags": ["gaming", "daytona_usa", "sega", "arcade", "music"]
    },
    {
        "id": "gaming_hard_287",
        "text": "Ποιο fighting game της SNK (1994) στο Neo Geo ένωσε για πρώτη φορά χαρακτήρες από τα franchises Fatal Fury, Art of Fighting και Ikari Warriors σε ομάδες 3 ατόμων;",
        "correct": "The King of Fighters '94",
        "distractors": ["Samurai Shodown", "Fatal Fury Special", "World Heroes"],
        "explanation": "Το KOF '94 εισήγαγε το σύστημα 3-on-3 team elimination, όπου ο νικητής κάθε γύρου συνέχιζε με την εναπομείνασα ζωή του ενάντια στον επόμενο μαχητή της αντίπαλης ομάδας.",
        "funFacts": [
            "Ο Kyo Kusanagi και ο κακός Rugal Bernstein έκαναν το ντεμπούτο τους σε αυτό το παιχνίδι.",
            "Το σύστημα της ομάδας της Ιαπωνίας, της ομάδας των Fatal Fury (Terry, Andy, Joe) και της ομάδας των γυναικών (Mai, Yuri, King) έγινε παράδοση για δεκαετίες."
        ],
        "source": "https://en.wikipedia.org/wiki/The_King_of_Fighters_%2794",
        "tags": ["gaming", "kof", "snk", "neo_geo", "fighting"]
    },
    {
        "id": "gaming_hard_288",
        "text": "Στο αριστούργημα της SNK 'Garou: Mark of the Wolves' (1999), ποιος είναι ο γιος του διαβόητου Geese Howard που μεγάλωσε υπό την προστασία του Terry Bogard;",
        "correct": "Rock Howard",
        "distractors": ["Grant", "Kain R. Heinlein", "Kim Dong Hwan"],
        "explanation": "Ο Rock Howard συνδυάζει στο στυλ πάλης του τις κινήσεις του βιολογικού του πατέρα Geese (Reppuken) και του θετού του πατέρα Terry Bogard (Rising Tackle, Buster Wolf).",
        "funFacts": [
            "Το παιχνίδι εισήγαγε το σύστημα T.O.P. (Tactical Officer Position) όπου ο παίκτης επιλέγει σε ποιο τρίτο της μπάρας υγείας του θα έχει ενισχυμένη ζημιά και ανάκτηση ζωής.",
            "Εισήγαγε επίσης το 'Just Defended', ένα σύστημα parry ακριβούς χρονισμού που αποκαθιστά ένα μικρό ποσοστό υγείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Garou:_Mark_of_the_Wolves",
        "tags": ["gaming", "garou", "snk", "neo_geo", "terry_bogard"]
    },
    {
        "id": "gaming_hard_289",
        "text": "Ποιο εθιστικό αθλητικό παιχνίδι με ιπτάμενο δίσκο (frisbee) κυκλοφόρησε η Data East στο Neo Geo το 1994 και εξελίχθηκε σε σύγχρονο καλτ esport τίτλο;",
        "correct": "Windjammers (Flying Power Disc)",
        "distractors": ["Street Hoop", "Super Dodge Ball", "Neo Turf Masters"],
        "explanation": "Στο Windjammers, δύο παίκτες πετούν έναν δίσκο με σπιν και καμπύλες προσπαθώντας να σκοράρουν στα αντίπαλα τέρματα των 3 ή 5 πόντων πάνω σε άμμο ή γήπεδο.",
        "funFacts": [
            "Το γαλλικό στούντιο Dotemu αναβίωσε το franchise το 2022 κυκλοφορώντας το επίσημο 'Windjammers 2'.",
            "Κάθε χαρακτήρας αντιπροσωπεύει μια διαφορετική εθνικότητα με μοναδικές ειδικές υπερ-βολές (Super Custom Shots)."
        ],
        "source": "https://en.wikipedia.org/wiki/Windjammers_(video_game)",
        "tags": ["gaming", "windjammers", "data_east", "neo_geo", "arcade"]
    },
    {
        "id": "gaming_hard_290",
        "text": "Ποιο στούντιο που ιδρύθηκε από πρώην μέλη της Irem δημιούργησε το ιστορικό run-and-gun 'Metal Slug' (1996) για το Neo Geo;",
        "correct": "Nazca Corporation",
        "distractors": ["Taito", "Toaplan", "Cave"],
        "explanation": "Οι προγραμματιστές και animators που είχαν εργαστεί στο GunForce II της Irem αποχώρησαν για να ιδρύσουν τη Nazca Corporation, η οποία εξαγοράστηκε άμεσα από την SNK μετά την τεράστια επιτυχία του Metal Slug.",
        "funFacts": [
            "Το animation του μικρού τανκ SV-001 (Super Vehicle-001) σχεδιάστηκε καρέ-καρέ στο χέρι με απίστευτη προσοχή στη λεπτομέρεια και τη μηχανική παραμόρφωση.",
            "Οι δύο αρχικοί πρωταγωνιστές είναι ο Marco Rossi και ο Tarma Roving της επίλεκτης μονάδας Peregrine Falcon."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Slug_(video_game)",
        "tags": ["gaming", "metal_slug", "nazca", "snk", "neo_geo"]
    },
    {
        "id": "gaming_hard_291",
        "text": "Ποια είναι η επίσημη ονομασία του μηχανισμού 'Tsubazerai' που εισήγαγε το 'Samurai Shodown' (1993) της SNK κατά τη σύγκρουση δύο όπλων ταυτόχρονα;",
        "correct": "Σύγκρουση λεπίδων (Weapon Clash / Sword Lock)",
        "distractors": ["Rage Explosion", "Deflect Stance", "Fatal Slash"],
        "explanation": "Όταν δύο μαχητές χτυπούν ταυτόχρονα με τα σπαθιά τους, τα όπλα κλειδώνουν και οι παίκτες πρέπει να πατήσουν ταχύτατα τα κουμπιά· ο χαμένος αφοπλίζεται και πρέπει να πολεμήσει με γυμνά χέρια.",
        "funFacts": [
            "Ο μετρητής οργής (Rage Gauge / Ikari Meter) γεμίζει καθώς ο παίκτης δέχεται ζημιά, κάνοντας το σώμα του να κοκκινίζει και πολλαπλασιάζοντας την ισχύ των επιθέσεών του.",
            "Ένα μοναδικό δυνατό χτύπημα (Heavy Slash) από τον Haohmaru μπορεί να αφαιρέσει έως και το 40% της συνολικής ζωής του αντιπάλου."
        ],
        "source": "https://en.wikipedia.org/wiki/Samurai_Shodown_(1993_video_game)",
        "tags": ["gaming", "samurai_shodown", "snk", "neo_geo", "fighting"]
    },
    {
        "id": "gaming_hard_292",
        "text": "Στο αριστούργημα της Treasure 'Sin and Punishment' (2000) στο Nintendo 64, ποιοι είναι οι δύο νεαροί πρωταγωνιστές που μάχονται ενάντια στα μεταλλαγμένα πλάσματα Armed Volunteers;",
        "correct": "Saki Amamiya και Airan Jo",
        "distractors": ["Shinji Ikari και Asuka Langley", "Rin και Len", "Kou και Yuri"],
        "explanation": "Το Sin and Punishment συνδύαζε στόχευση σκοποβολής με το αριστερό χέρι και κίνηση αποφυγής του χαρακτήρα με το δεξί, εκμεταλλευόμενο με μοναδικό τρόπο τον σχεδιασμό τριών λαβών του N64 controller.",
        "funFacts": [
            "Το παιχνίδι κυκλοφόρησε αρχικά αποκλειστικά στην Ιαπωνία αλλά απέκτησε cult φήμη στη Δύση επειδή είχε πλήρως αγγλικούς διαλόγους από την αρχή.",
            "Ο Saki Amamiya εμφανίζεται ως Assist Trophy στη σειρά Super Smash Bros."
        ],
        "source": "https://en.wikipedia.org/wiki/Sin_and_Punishment",
        "tags": ["gaming", "sin_and_punishment", "treasure", "nintendo", "n64"]
    },
    {
        "id": "gaming_hard_293",
        "text": "Ποιο ήταν το πρώτο παιχνίδι shoot 'em up της Toaplan (1992) που περιείχε την κωμική ατάκα 'All your base are belong to us' λόγω κακής μετάφρασης από τα ιαπωνικά;",
        "correct": "Zero Wing",
        "distractors": ["Truxton", "Hellfire", "Batsugun"],
        "explanation": "Στην ευρωπαϊκή έκδοση του Zero Wing για το Sega Mega Drive, η εισαγωγή περιείχε τραγικά λάθη μετάφρασης ('Somebody set up us the bomb', 'For great justice'), δημιουργώντας ένα από τα πρώτα παγκόσμια memes του διαδικτύου το 2001.",
        "funFacts": [
            "Ο κακός εξωγήινος κυβερνήτης που εκστομίζει την ατάκα ονομάζεται CATS.",
            "Η εταιρεία Toaplan θεωρείται ο πατέρας του υποείδους 'Danmaku' (Bullet Hell) με το τελευταίο της παιχνίδι Batsugun (1993)."
        ],
        "source": "https://en.wikipedia.org/wiki/All_your_base_are_belong_to_us",
        "tags": ["gaming", "zero_wing", "toaplan", "memes", "retro"]
    },
    {
        "id": "gaming_hard_294",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού παιχνιδιού στρατηγικής πραγματικού χρόνου του 1989 από την Technosoft στο Sega Genesis που ενέπνευσε το είδος MOBA και RTS;",
        "correct": "Herzog Zwei",
        "distractors": ["Thunder Force III", "Dune II", "Rampart"],
        "explanation": "Στο Herzog Zwei, ο παίκτης ελέγχει ένα ρομποτικό αεροσκάφος (mecha) που μεταμορφώνεται, δίνει εντολές σε αυτόνομες μονάδες εδάφους και καταλαμβάνει ουδέτερες βάσεις.",
        "funFacts": [
            "Ο δημιουργός του StarCraft και του Warcraft Patrick Wyatt δήλωσε ότι το Herzog Zwei ήταν η άμεση πηγή έμπνευσης για τη γέννηση των RTS παιχνιδιών της Blizzard.",
            "Το παιχνίδι υποστήριζε ταυτόχρονο παιχνίδι δύο παικτών σε split-screen."
        ],
        "source": "https://en.wikipedia.org/wiki/Herzog_Zwei",
        "tags": ["gaming", "herzog_zwei", "technosoft", "genesis", "rts"]
    },
    {
        "id": "gaming_hard_295",
        "text": "Ποιο shoot 'em up της Cave (1997) καθιέρωσε οριστικά τους κανόνες του είδους 'Danmaku' (Bullet Hell) με μικροσκοπικό hitbox και χιλιάδες πολύχρωμες σφαίρες στην οθόνη;",
        "correct": "DoDonPachi",
        "distractors": ["DonPachi", "Espgaluda", "Touhou Project"],
        "explanation": "Το DoDonPachi εισήγαγε το σύστημα αλυσίδων πόντων (GP Chain System), τη συγκεντρωμένη ακτίνα λέιζερ που επιβραδύνει το σκάφος και το διαβόητο μυστικό τελικό αφεντικό Queen Hachi.",
        "funFacts": [
            "Για να φτάσει ο παίκτης στον δεύτερο γύρο (2nd Loop) και στο κρυφό αφεντικό Hibachi, έπρεπε να ολοκληρώσει το παιχνίδι με ένα μόνο credit και συγκεκριμένες προϋποθέσεις.",
            "Το hitbox του σκάφους ήταν μόλις μερικά pixels στο κέντρο, επιτρέποντας στους έμπειρους παίκτες να περνούν μέσα από απίστευτα πυκνά μοτίβα σφαιρών."
        ],
        "source": "https://en.wikipedia.org/wiki/DoDonPachi",
        "tags": ["gaming", "dodonpachi", "cave", "shmup", "bullet_hell"]
    },
    {
        "id": "gaming_hard_296",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού text parser adventure της Level 9 Computing (1983) βασισμένου στην τριλογία του 'Άρχοντα των Δαχτυλιδιών';",
        "correct": "Colossal Adventure",
        "distractors": ["The Hobbit", "Lord of the Rings Vol. 1", "Shadows of Mordor"],
        "explanation": "Η Level 9 ήταν το κορυφαίο βρετανικό στούντιο text adventures της εποχής των ZX Spectrum και BBC Micro, συμπιέζοντας τεράστιους κόσμους μέσω της γλώσσας A-Code.",
        "funFacts": [
            "Η εταιρεία ιδρύθηκε από τα τρία αδέλφια Mike, Nicholas και Pete Austin.",
            "Τα παιχνίδια της Level 9 περιλάμβαναν λεξιλόγιο άνω των 1.000 λέξεων, εξαιρετικά προηγμένο για τα 32KB μνήμης της εποχής."
        ],
        "source": "https://en.wikipedia.org/wiki/Level_9_Computing",
        "tags": ["gaming", "level_9", "text_adventure", "zx_spectrum", "retro"]
    },
    {
        "id": "gaming_hard_297",
        "text": "Ποιο είναι το όνομα του επικού RPG της tri-Ace (1998) στο PlayStation με πρωταγωνιστές τον Claude C. Kenny και τη Rena Lanford, που διέθετε πάνω από 80 διαφορετικά τέλη;",
        "correct": "Star Ocean: The Second Story",
        "distractors": ["Tales of Destiny", "Star Ocean: Till the End of Time", "Wild Arms 2"],
        "explanation": "Ο παίκτης επέλεγε στην αρχή ανάμεσα στον Claude και τη Rena, βλέποντας διαφορετικές οπτικές γωνίες της ιστορίας στον πλανήτη Expel και διαχειριζόμενος σχέσεις Private Actions.",
        "funFacts": [
            "Το σύστημα δεξιοτήτων (Specialties) επέτρεπε μαγειρική, συγγραφή βιβλίων, αλχημεία, ακόμα και πλαστογραφία τραπεζικών επιταγών.",
            "Το 2023 κυκλοφόρησε ένα εκπληκτικό remake 2.5D με τίτλο 'Star Ocean: The Second Story R'."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Ocean:_The_Second_Story",
        "tags": ["gaming", "star_ocean", "tri_ace", "enix", "playstation"]
    },
    {
        "id": "gaming_hard_298",
        "text": "Στο 'Metal Gear Solid' (1998), ποια ήταν η συχνότητα του Codec της Meryl Silverburgh που ο Roy Campbell έλεγε στον Snake ότι βρισκόταν 'στο πίσω μέρος του κουτιού του CD';",
        "correct": "140.15",
        "distractors": ["141.12", "140.85", "142.50"],
        "explanation": "Ο Campbell αναφερόταν κυριολεκτικά στο φυσικό πλαστικό κουτί της συσκευασίας του παιχνιδιού στα καταστήματα, όπου σε ένα screenshot στο οπισθόφυλλο φαινόταν η συχνότητα 140.15.",
        "funFacts": [
            "Αυτός ο ευφυής τρόπος καταπολέμησης της πειρατείας μπλόκαρε χιλιάδες παίκτες που είχαν νοικιάσει το παιχνίδι σε απλή θήκη ή είχαν πειρατικά αντίγραφα.",
            "Ο Snake μπορούσε επίσης να καλέσει τη συχνότητα 140.96 για να αποθηκεύσει την πρόοδό του με τη Mei Ling."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid",
        "tags": ["gaming", "metal_gear_solid", "hideo_kojima", "playstation", "codec"]
    },
    {
        "id": "gaming_hard_299",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού 3D puzzle-platformer της Sony Computer Entertainment (1998) στο PS1 όπου ο παίκτης ελέγχει έναν κύλινδρο που ανατρέπει κύβους Kurushi;",
        "correct": "Intelligent Qube (Kurushi)",
        "distractors": ["Devil Dice", "Kula World", "Blast Corps"],
        "explanation": "Στο Intelligent Qube, ο παίκτης τρέχει πάνω σε μια αιωρούμενη πλατφόρμα στο διάστημα, σημαδεύοντας τετράγωνα για να εξουδετερώσει σειρές από τεράστιους πέτρινους κύβους που κυλούν προς το μέρος του.",
        "funFacts": [
            "Το παιχνίδι απέκτησε τεράστια φήμη στην Ευρώπη χάρη στη συμπερίληψή του στο θρυλικό δισκάκι 'Demo One' που συνόδευε κάθε κονσόλα PlayStation.",
            "Το ορχηστρικό soundtrack συντέθηκε από τον διάσημο Ιάπωνα συνθέτη Takayuki Hattori."
        ],
        "source": "https://en.wikipedia.org/wiki/Intelligent_Qube",
        "tags": ["gaming", "intelligent_qube", "kurushi", "playstation", "puzzle"]
    },
    {
        "id": "gaming_hard_300",
        "text": "Ποιο είναι το όνομα του σουηδικού 3D puzzle game (Game Design Sweden, 1998) στο PlayStation όπου ο παίκτης κυλάει μια φουσκωτή μπάλα παραλίας πάνω σε αιωρούμενες πλατφόρμες;",
        "correct": "Kula World (Roll Away)",
        "distractors": ["Devil Dice", "Glover", "Marble Madness"],
        "explanation": "Στο Kula World, ο παίκτης ελέγχει μια ριγέ μπάλα παραλίας σε λαβυρίνθους όπου η βαρύτητα αλλάζει κατά 90 μοίρες κάθε φορά που η μπάλα κυλάει πάνω από την άκρη ενός κύβου.",
        "funFacts": [
            "Στη Βόρεια Αμερική κυκλοφόρησε με τον τίτλο 'Roll Away' και στην Ιαπωνία ως 'KulaQuest'.",
            "Το ηλεκτρονικό soundtrack συντέθηκε από το σουηδικό δίδυμο ηλεκτρονικής μουσικής 'Troll' (Marcus Henriksson και Jan Schulte-Holthausen)."
        ],
        "source": "https://en.wikipedia.org/wiki/Kula_World",
        "tags": ["gaming", "kula_world", "playstation", "psygnosis", "puzzle"]
    },
    {
        "id": "gaming_hard_301",
        "text": "Ποιο καινοτόμο puzzle game της Shift (1998) στο PlayStation έβαζε τον παίκτη να ελέγχει ένα μικρό διαβολάκι που περπατάει πάνω σε ζάρια για να ταιριάξει τους αριθμούς τους;",
        "correct": "Devil Dice (Xi)",
        "distractors": ["Intelligent Qube", "Bombastic", "Puyo Puyo Sun"],
        "explanation": "Στο Devil Dice, ο παίκτης κυλάει τα ζάρια πατώντας πάνω τους· αν ενώσεις τόσα ζάρια όσα ο αριθμός της πάνω όψης (π.χ. τρία τριάρια ή τέσσερα τεσσάρια), τα ζάρια βυθίζονται και εξαφανίζονται.",
        "funFacts": [
            "Το παιχνίδι ξεκίνησε ως ερασιτεχνικό πρότζεκτ στο Net Yaroze (το κιτ ανάπτυξης για χομπίστες του PS1) πριν η Sony το αγοράσει και το κυκλοφορήσει εμπορικά.",
            "Στο PS2 απέκτησε τη συνέχεια 'Bombastic' (Xi Jumbo)."
        ],
        "source": "https://en.wikipedia.org/wiki/Devil_Dice",
        "tags": ["gaming", "devil_dice", "shift", "playstation", "net_yaroze"]
    },
    {
        "id": "gaming_hard_302",
        "text": "Στο παιχνίδι κατεδαφίσεων 'Blast Corps' (1997) της Rare στο Nintendo N64, ποιος είναι ο κεντρικός στόχος σε κάθε αποστολή;",
        "correct": "Να κατεδαφιστούν όλα τα κτίρια και εμπόδια στην πορεία ενός ακυβέρνητου φορτηγού με διαρρέοντα πυρηνικά όπλα",
        "distractors": [
            "Να προστατευτεί μια στρατιωτική βάση από ορδές ρομπότ",
            "Να ανατιναχθούν γέφυρες για να παγιδευτεί ένας εχθρικός στρατός",
            "Να διασωθούν επιζώντες από καταρρέοντες ουρανοξύστες"
        ],
        "explanation": "Ένας πυρηνικός φορέας (Nuclear Missile Carrier) κινείται σε απόλυτα ευθεία γραμμή και αν αγγίξει έστω και ένα κτίριο, εκρήγνυται ακαριαία, αναγκάζοντας τον παίκτη να ισοπεδώσει τα πάντα μπροστά του με μπουλντόζες και mechas.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον Martin Hollis αμέσως μετά την ολοκλήρωση του GoldenEye 007.",
            "Τα οχήματα περιλάμβαναν το γιγάντιο ρομπότ J-Bomb που έκανε προσγειώσεις με το πισινό και ένα buggy με σφαίρες πλάσματος."
        ],
        "source": "https://en.wikipedia.org/wiki/Blast_Corps",
        "tags": ["gaming", "blast_corps", "rare", "nintendo", "n64"]
    },
    {
        "id": "gaming_hard_303",
        "text": "Στο παιχνίδι τρίτου προσώπου 'Body Harvest' (1998) της DMA Design (μετέπειτα Rockstar North) στο N64, σε ποια ιστορική χώρα ξεκινά η πρώτη περίοδος εξωγήινης εισβολής;",
        "correct": "Στην Ελλάδα το 1916",
        "distractors": ["Στην Ιάβα το 1941", "Στις ΗΠΑ το 1966", "Στη Σιβηρία το 1991"],
        "explanation": "Ο ταξιδιώτης του χρόνου Adam Drake ταξιδεύει πίσω στο 1916 στην Ελλάδα για να σταματήσει τα γιγάντια έντομα που περικλείουν περιοχές σε ενεργειακούς θόλους για να συλλέξουν ανθρώπους.",
        "funFacts": [
            "Το Body Harvest θεωρείται ο άμεσος τεχνολογικός και σχεδιαστικός προπομπός του Grand Theft Auto III, εισάγοντας οδήγηση δεκάδων οχημάτων σε ανοιχτό 3D κόσμο.",
            "Η Nintendo ήταν αρχικά ο εκδότης του παιχνιδιού, αλλά το απέρριψε επειδή το θεώρησε υπερβολικά περίπλοκο και βίαιο, με τη Midway να αναλαμβάνει την κυκλοφορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Body_Harvest",
        "tags": ["gaming", "body_harvest", "dma_design", "rockstar", "n64", "greece"]
    },
    {
        "id": "gaming_hard_304",
        "text": "Στο πρωτότυπο 3D platformer 'Space Station Silicon Valley' (1998) της DMA Design, τι είδους οντότητα είναι ο πρωταγωνιστής 'Evo';",
        "correct": "Ένα μικροσκοπικό τσιπ υπολογιστή που καταλαμβάνει ρομποτικά σώματα ζώων",
        "distractors": ["Ένα ρακούν με διαστημική στολή", "Ένας ιπτάμενος εξωγήινος δορυφόρος", "Ένας κυβερνο-σκύλος"],
        "explanation": "Το σώμα του Evo καταστρέφεται κατά τη συντριβή και μένει μόνο το μικροτσίπ του, αναγκάζοντάς τον να πηδάει μέσα στα σώματα ρομποτικών προβάτων, σκύλων, αλεπούδων και πιγκουίνων για να λύνει παζλ.",
        "funFacts": [
            "Ένα διαβόητο bug στην έκδοση N64 εμπόδιζε τη συλλογή ενός από τα αναμνηστικά τρόπαια, καθιστώντας αδύνατο τον 100% τερματισμό του παιχνιδιού χωρίς GameShark.",
            "Το παιχνίδι σχεδιάστηκε από τον Leslie Benzies, ο οποίος έγινε αργότερα ο βασικός παραγωγός των Grand Theft Auto III, Vice City, San Andreas και GTA V."
        ],
        "source": "https://en.wikipedia.org/wiki/Space_Station_Silicon_Valley",
        "tags": ["gaming", "space_station_silicon_valley", "dma_design", "rockstar", "n64"]
    },
    {
        "id": "gaming_hard_305",
        "text": "Στο platformer 'Glover' (1998) της Interactive Studios, ποιο αντικείμενο πρέπει να κυλάει, να αναπηδά και να ισορροπεί το μαγικό γάντι σε κάθε πίστα;",
        "correct": "Μια λαστιχένια μαγική μπάλα (Rubber Ball)",
        "distractors": ["Ένα μαγικό ραβδί", "Ένα γυάλινο δισκοπότηρο", "Ένα χρυσό νόμισμα"],
        "explanation": "Ο Glover προσπαθεί να σώσει το Crystal Kingdom προστατεύοντας τους κρυστάλλους που έχει μεταμορφώσει σε λαστιχένιες μπάλες, μετατρέποντάς τους κατά βούληση σε μέταλλο, γυαλί ή μπόουλινγκ.",
        "funFacts": [
            "Ο κακός του παιχνιδιού είναι το δίδυμο γάντι Cross-Stitch, το οποίο έπεσε σε ένα καζάνι με σκοτεινή μαγεία.",
            "Το σύστημα φυσικής της μπάλας απαιτούσε ακριβή υπολογισμό κλίσης, περιστροφής και δύναμης αναπήδησης."
        ],
        "source": "https://en.wikipedia.org/wiki/Glover_(video_game)",
        "tags": ["gaming", "glover", "interactive_studios", "n64", "platformer"]
    },
    {
        "id": "gaming_hard_306",
        "text": "Ποια είναι η διάσημη ατάκα που φωνάζει διαρκώς η ηρωίδα-ανδροειδές Marina Liteyears στο 'Mischief Makers' (1997) της Treasure στο N64 καθώς τραντάζει εχθρούς;",
        "correct": "Shake, shake! (Κούνα, κούνα!)",
        "distractors": ["Catch, catch!", "Grab and go!", "Toss it high!"],
        "explanation": "Ο βασικός μηχανισμός του Mischief Makers (Trouble Makers στην Ιαπωνία) είναι το άρπαγμα και το έντονο κούνημα (shaking) αντικειμένων και εχθρών για την αποκάλυψη κρυμμένων πετραδιών και όπλων.",
        "funFacts": [
            "Ήταν το πρώτο 2D platformer που κυκλοφόρησε για το Nintendo 64.",
            "Η Marina προσπαθεί να σώσει τον ηλικιωμένο δημιουργό της, Professor Theo, από την Αυτοκρατορία στον πλανήτη Clancer."
        ],
        "source": "https://en.wikipedia.org/wiki/Mischief_Makers",
        "tags": ["gaming", "mischief_makers", "treasure", "nintendo", "n64"]
    },
    {
        "id": "gaming_hard_307",
        "text": "Ποιο εκρηκτικό shoot 'em up της Treasure (1999) στο N64 και Dreamcast επέτρεπε στο ρομπότ του παίκτη να εκτοξεύει ταυτόχρονα έως και 400 κατευθυνόμενους πυραύλους;",
        "correct": "Bangai-O (Bakuretsu Muteki Bangai-O)",
        "distractors": ["Sin and Punishment", "Ikaruga", "Gunstar Heroes"],
        "explanation": "Στο Bangai-O, ο παίκτης φορτίζει το Scatter Attack όσο πιο κοντά βρίσκεται σε εχθρικά πυρά· απελευθερώνοντας την επίθεση, το mecha εκτοξεύει έως και 400 πυραύλους που γεμίζουν ολόκληρη την οθόνη με εκρήξεις.",
        "funFacts": [
            "Οι δύο πιλότοι του ρομπότ Riki και Mami εναλλάσσουν τον τύπο πυρομαχικών ανάμεσα σε αναπηδούσες σφαίρες και κατευθυνόμενους πυραύλους.",
            "Το παιχνίδι εμπνεύστηκε από τα κλασικά 8-bit παιχνίδια του υπολογιστή Sharp X1."
        ],
        "source": "https://en.wikipedia.org/wiki/Bangai-O",
        "tags": ["gaming", "bangai_o", "treasure", "dreamcast", "n64"]
    },
    {
        "id": "gaming_hard_308",
        "text": "Στο 'Silhouette Mirage' (1997) της Treasure, ποιο σύστημα δύο αντιτιθέμενων ιδιοτήτων χρησιμοποιεί η πρωταγωνίστρια Shyna Nera Shyna ανάλογα με την κατεύθυνση που κοιτάζει;",
        "correct": "Silhouette (Σιλουέτα) όταν κοιτάζει δεξιά και Mirage (Οφθαλμαπάτη) όταν κοιτάζει αριστερά",
        "distractors": [
            "Φωτιά όταν κοιτάζει εμπρός και Πάγος όταν κοιτάζει πίσω",
            "Ηλεκτρισμός στο άλμα και Μαγνητισμός στο έδαφος",
            "Φως στον αέρα και Σκότος στο νερό"
        ],
        "explanation": "Το Silhouette Mirage αποτέλεσε τον άμεσο σχεδιαστικό πρόδρομο του Ikaruga: οι επιθέσεις της Shyna απορροφούν ή καταστρέφουν τους εχθρούς ανάλογα με την ιδιότητά τους και την κατεύθυνση που είναι στραμμένη.",
        "funFacts": [
            "Στη δυτική έκδοση του PlayStation από την Working Designs, η δυσκολία αυξήθηκε δραματικά κάνοντας τις σφαίρες να κοστίζουν Spirit power.",
            "Ο δημιουργός Koichi Meguro σχεδίασε τον κόσμο με έντονα σουρεαλιστικά και βιβλικά στοιχεία."
        ],
        "source": "https://en.wikipedia.org/wiki/Silhouette_Mirage",
        "tags": ["gaming", "silhouette_mirage", "treasure", "saturn", "playstation"]
    },
    {
        "id": "gaming_hard_309",
        "text": "Ποιο θρυλικό 2D beat 'em up RPG της Treasure (1996) στο Sega Saturn διέθετε σύστημα κίνησης σε τρία επίπεδα βάθους (planes) και υποστήριζε μάχες έως 6 παικτών;",
        "correct": "Guardian Heroes",
        "distractors": ["Dragon's Crown", "Princess Crown", "Dungeons & Dragons: Shadow over Mystara"],
        "explanation": "Το Guardian Heroes συνδύαζε μηχανισμούς fighting game (ειδικές κινήσεις με εντολές μοχλού), επιλογή διακλαδούμενων μονοπατιών ιστορίας, level-up στατιστικών και μάχες 6 παικτών με το Sega Multi-Tap.",
        "funFacts": [
            "Ο νεκραναστημένος χρυσός ιππότης Undead Warrior που συνοδεύει τους ήρωες μπορεί να ελεγχθεί από τον παίκτη με ειδικές εντολές συμπεριφοράς.",
            "Το παιχνίδι περιλάμβανε πάνω από 30 διαφορετικά τέλη ανάλογα με τις αποφάσεις και τις συμμαχίες των ηρώων."
        ],
        "source": "https://en.wikipedia.org/wiki/Guardian_Heroes",
        "tags": ["gaming", "guardian_heroes", "treasure", "sega", "saturn"]
    },
    {
        "id": "gaming_hard_310",
        "text": "Ποιο είναι το όνομα της παρανοϊκής φυλής εξωγήινων στο 'Star Control II' (1992) των Paul Reiche III και Fred Ford, που είναι παγιδευμένοι σε μια αέναη τελετουργική σύγκρουση δολοφονιών;",
        "correct": "Ilwrath",
        "distractors": ["Ur-Quan", "Spathi", "Mycon"],
        "explanation": "Οι Ilwrath είναι αραχνοειδείς εξωγήινοι που λατρεύουν τους σκοτεινούς θεούς Dogar και Kazon και πιλοτάρουν τα σκάφη Avenger με αορατότητα και φλογοβόλα.",
        "funFacts": [
            "Το Star Control II θεωρείται ένα από τα σπουδαιότερα space RPGs όλων των εποχών, επηρεάζοντας άμεσα τη δημιουργία του Mass Effect.",
            "Ο πηγαίος κώδικας απελευθερώθηκε αργότερα δωρεάν ως open-source πρότζεκτ με τον τίτλο 'The Ur-Quan Masters'."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Control_II",
        "tags": ["gaming", "star_control", "toys_for_bob", "sci_fi", "retro"]
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 2.")
    validate_and_append("gaming", "hard", 5, questions)

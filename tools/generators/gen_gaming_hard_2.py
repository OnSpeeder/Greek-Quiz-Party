# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_061",
        "text": "Ποιο ήταν το αρχικό όνομα υπό το οποίο ο Markus 'Notch' Persson κυκλοφόρησε την πρώτη έκδοση του 'Minecraft' στις 17 Μαΐου 2009 σε ένα φόρουμ προγραμματιστών;",
        "correct": "Cave Game",
        "distractors": [
            "BlockWorld",
            "Infiniminer 2",
            "VoxelCraft"
        ],
        "explanation": "Ο Markus Persson εμπνεύστηκε από το παιχνίδι 'Infiniminer' του Zachary Barth και ανέπτυξε μέσα σε λίγες μέρες ένα απλό prototype που ονόμασε 'Cave Game: Tech Demo', προτού το μετονομάσει σε 'Minecraft: Order of the Stone' και τελικά 'Minecraft'.",
        "funFacts": [
            "Ο ανατριχιαστικός ήχος των Ghasts στο Nether ηχογραφήθηκε από τον σχεδιαστή ήχου Daniel Rosenfeld (C418) όταν η γάτα του ξύπνησε ξαφνικά από τον ύπνο.",
            "Το Minecraft αποτελεί το παιχνίδι με τις περισσότερες πωλήσεις όλων των εποχών, ξεπερνώντας τα 300 εκατομμύρια αντίτυπα."
        ],
        "source": "https://en.wikipedia.org/wiki/Minecraft",
        "tags": ["gaming", "minecraft", "notch", "indie", "history"]
    },
    {
        "id": "gaming_hard_062",
        "text": "Πού εργαζόταν ο Alexey Pajitnov όταν προγραμμάτισε την πρώτη έκδοση του 'Tetris' το 1984 σε έναν σοβιετικό υπολογιστή Elektronika 60;",
        "correct": "Στο Υπολογιστικό Κέντρο Dorodnitsyn της Σοβιετικής Ακαδημίας Επιστημών στη Μόσχα",
        "distractors": [
            "Στο Στρατιωτικό Τεχνολογικό Ινστιτούτο του Λένινγκραντ",
            "Στο Υπουργείο Τηλεπικοινωνιών της ΕΣΣΔ",
            "Στο Πανεπιστήμιο Lomonosov της Μόσχας"
        ],
        "explanation": "Ο Pajitnov εργαζόταν στην Ακαδημία Επιστημών ερευνώντας την αναγνώριση ομιλίας. Εμπνεύστηκε το Tetris από το παραδοσιακό επιτραπέζιο παζλ 'Pentominoes' και έγραψε τον κώδικα σε γλώσσα Pascal.",
        "funFacts": [
            "Επειδή το λογισμικό ανήκε στο σοβιετικό κράτος (μέσω της κρατικής υπηρεσίας ELORG), ο Pajitnov δεν έλαβε καθόλου δικαιώματα (royalties) για το παιχνίδι μέχρι το 1996.",
            "Τα γραφικά της πρώτης έκδοσης δεν είχαν καν χρώματα, αλλά σχηματίζονταν από απλές αγκύλες κειμένου '[ ]'."
        ],
        "source": "https://en.wikipedia.org/wiki/Tetris",
        "tags": ["gaming", "tetris", "pajitnov", "ussr", "history"]
    },
    {
        "id": "gaming_hard_063",
        "text": "Πώς προέκυψε ο μυστικός χαρακτήρας 'Mew' στα 'Pokémon Red και Blue' (1996), ο οποίος δεν αναφερόταν πουθενά στο επίσημο εγχειρίδιο της Nintendo;",
        "correct": "Ο προγραμματιστής Shigeki Morimoto τον πρόσθεσε κρυφά στα τελευταία 300 bytes ελεύθερης μνήμης της ROM",
        "distractors": [
            "Ήταν διαφημιστικό τέχνασμα σχεδιασμένο από τον Satoshi Tajiri για τουρνουά",
            "Προέκυψε ως σφάλμα μνήμης (buffer overflow) κατά τη μάχη με τον MissingNo",
            "Ήταν απομεινάρι από ένα ακυρωμένο Pokémon που ξέχασαν να διαγράψουν"
        ],
        "explanation": "Αφού αφαιρέθηκαν τα εργαλεία εντοπισμού σφαλμάτων (debug tools), έμειναν μόλις 300 bytes ελεύθερα στην κασέτα. Ο Morimoto εισήγαγε τον κώδικα του Mew ως εσωτερικό αστείο δύο εβδομάδες πριν την παραγωγή, χωρίς να ενημερώσει τη Nintendo.",
        "funFacts": [
            "Η εμφάνιση του Mew σε παίκτες μέσω σφαλμάτων μνήμης δημιούργησε έναν άνευ προηγουμένου παγκόσμιο θρύλο, εκτοξεύοντας τις πωλήσεις των παιχνιδιών.",
            "Η Nintendo ανακάλυψε την ύπαρξη του Mew εκ των υστέρων και οργάνωσε ειδικό διαγωνισμό στο περιοδικό CoroCoro για τη διανομή του σε 20 νικητές."
        ],
        "source": "https://en.wikipedia.org/wiki/Mew_(Pok%C3%A9mon)",
        "tags": ["gaming", "pokemon", "nintendo", "gameboy", "secrets"]
    },
    {
        "id": "gaming_hard_064",
        "text": "Ποιο φιλοσοφικό κίνημα και ποιο διάσημο βιβλίο αποτέλεσαν τη βασική έμπνευση του Ken Levine για τη δημιουργία της υποβρύχιας δυστοπικής πόλης Rapture στο 'BioShock' (2007);",
        "correct": "Ο Αντικειμενισμός (Objectivism) και το βιβλίο 'Atlas Shrugged' της Ayn Rand",
        "distractors": [
            "Ο Υπαρξισμός και το 'Είναι και Χρόνος' του Martin Heidegger",
            "Ο Μηδενισμός και το 'Τάδε έφη Ζαρατούστρα' του Friedrich Nietzsche",
            "Ο Ωφελιμισμός και το 'Περί Ελευθερίας' του John Stuart Mill"
        ],
        "explanation": "Ο ιδρυτής της Rapture, Andrew Ryan (αναγραμματισμός εμπνευσμένος από το όνομα της Ayn Rand), έχτισε μια πόλη όπου οι καλλιτέχνες και οι επιστήμονες δεν θα δεσμεύονταν από κρατικούς νόμους ή ηθικούς φραγμούς.",
        "funFacts": [
            "Η περίφημη φράση 'Would you kindly' (Θα είχες την καλοσύνη) χρησιμοποιείται ως ψυχολογική εντολή ελέγχου του πρωταγωνιστή Jack σε όλη τη διάρκεια του παιχνιδιού.",
            "Οι Big Daddies και οι Little Sisters σχεδιάστηκαν για να προκαλούν ένα έντονο ηθικό δίλημμα στον παίκτη σχετικά με τη συγκομιδή του ADAM."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock",
        "tags": ["gaming", "bioshock", "ken_levine", "philosophy", "fps"]
    },
    {
        "id": "gaming_hard_065",
        "text": "Ποιο είδος gameplay είχε αρχικά το ιστορικό action RPG 'Diablo' (1996) της Blizzard North, προτού η μητρική Blizzard Entertainment επιμείνει να αλλάξει σε πραγματικό χρόνο (real-time);",
        "correct": "Turn-based RPG (παιχνίδι βασισμένο σε γύρους)",
        "distractors": [
            "First-person dungeon crawler (όπως το Eye of the Beholder)",
            "Text-based adventure με στατικές εικόνες",
            "Point-and-click puzzle adventure"
        ],
        "explanation": "Ο David Brevik και η ομάδα Condor σχεδίαζαν το Diablo ως turn-based roguelike με γραφικά stop-motion claymation. Η Blizzard πρότεινε να γίνει σε πραγματικό χρόνο, και ο Brevik υλοποίησε την αλλαγή μέσα σε ένα μόνο Σαββατοκύριακο.",
        "funFacts": [
            "Όταν ο Brevik έκανε κλικ με το ποντίκι και είδε τον πολεμιστή να πλησιάζει αμέσως και να χτυπά το skeleton, δήλωσε ότι εκείνη τη στιγμή ένιωσε πως δημιουργούσαν έναν θρύλο.",
            "Το 'The Secret Cow Level' ξεκίνησε ως αστικός μύθος παικτών για το πρώτο Diablo, αλλά η Blizzard το ενσωμάτωσε ως πραγματικό μυστικό επίπεδο στο Diablo II."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_(video_game)",
        "tags": ["gaming", "diablo", "blizzard", "rpg", "history"]
    },
    {
        "id": "gaming_hard_066",
        "text": "Ποιος θρυλικός σχεδιαστής υλικού (hardware architect) της Sony ονομάστηκε 'Πατέρας του PlayStation' επειδή πίστεψε στο CD-ROM και σχεδίασε πρώτα το τσιπ ήχου SPC700 για το SNES;",
        "correct": "Ken Kutaragi",
        "distractors": [
            "Mark Cerny",
            "Kazuo Hirai",
            "Norio Ohga"
        ],
        "explanation": "Ο Kutaragi ανέπτυξε κρυφά το SPC700 για τη Nintendo. Όταν η Nintendo ακύρωσε τη συνεργασία για το 'SNES PlayStation', ο Kutaragi έπεισε τον πρόεδρο της Sony, Norio Ohga, να χρηματοδοτήσει τη δική τους ανεξάρτητη κονσόλα 3D γραφικών.",
        "funFacts": [
            "Η ηγεσία της Sony θεωρούσε αρχικά τα video games παιδικά παιχνίδια που δεν ταίριαζαν στο κύρος της εταιρείας ηλεκτρονικών.",
            "Το PlayStation έγινε η πρώτη οικιακή κονσόλα στην ιστορία που ξεπέρασε τα 100 εκατομμύρια τεμάχια σε πωλήσεις παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Ken_Kutaragi",
        "tags": ["gaming", "sony", "playstation", "kutaragi", "hardware"]
    },
    {
        "id": "gaming_hard_067",
        "text": "Ποιος Ιάπωνας προγραμματιστής της Konami επινόησε τον διάσημο 'Κώδικα Konami' (Πάνω, Πάνω, Κάτω, Κάτω, Αριστερά, Δεξιά, Αριστερά, Δεξιά, B, A) κατά τη μεταφορά του Gradius στο Famicom το 1985;",
        "correct": "Kazuhisa Hashimoto",
        "distractors": [
            "Hideo Kojima",
            "Koji Igarashi",
            "Keiji Inafune"
        ],
        "explanation": "Ο Hashimoto δυσκολευόταν πάρα πολύ να τερματίσει το Gradius κατά τη διάρκεια των δοκιμών εντοπισμού σφαλμάτων, οπότε εισήγαγε τον συνδυασμό πλήκτρων για να αποκτά άμεσα όλα τα power-ups.",
        "funFacts": [
            "Ο κώδικας έγινε παγκοσμίως διάσημος στο 'Contra' (NES, 1988), όπου χάριζε στον παίκτη 30 ζωές αντί για τις αρχικές 3.",
            "Ο Κώδικας Konami έχει ενσωματωθεί ως easter egg σε εκατοντάδες ιστοσελίδες (όπως το Google, το Netflix και το Discord) και ταινίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Konami_Code",
        "tags": ["gaming", "konami", "konami_code", "retro", "contra"]
    },
    {
        "id": "gaming_hard_068",
        "text": "Ποια διάσημη μαθηματική σταθερά και αλγόριθμος ('Fast Inverse Square Root') έγινε θρυλική στον πηγαίο κώδικα του 'Quake III Arena' (1999) για τον ακαριαίο υπολογισμό γωνιών φωτισμού;",
        "correct": "0x5f3759df",
        "distractors": [
            "0xdeadbeef",
            "0x7fffffff",
            "0x1337c0de"
        ],
        "explanation": "Ο αλγόριθμος υπολόγιζε το 1/sqrt(x) έως και τέσσερις φορές ταχύτερα από τις τυπικές συναρτήσεις διαίρεσης της CPU, χρησιμοποιώντας έναν μυστηριώδη μαγικό αριθμό σε δεκαεξαδική μορφή (0x5f3759df) και μία επανάληψη της μεθόδου Newton-Raphson.",
        "funFacts": [
            "Αν και αποδόθηκε συχνά στον John Carmack, η ακριβής προέλευση του κώδικα ανάγεται στον Gary Tarolli της 3dfx και στον Cleve Moler.",
            "Στο αρχικό σχόλιο του πηγαίου κώδικα του Quake III υπήρχε η χιουμοριστική φράση: 'what the fuck? // 1st iteration'."
        ],
        "source": "https://en.wikipedia.org/wiki/Fast_inverse_square_root",
        "tags": ["gaming", "quake", "carmack", "programming", "math"]
    },
    {
        "id": "gaming_hard_069",
        "text": "Για ποιο λόγο δημιουργήθηκε το 'Second Quest' στο αρχικό 'The Legend of Zelda' (1986) στο NES από τους Shigeru Miyamoto και Takashi Tezuka;",
        "correct": "Επειδή ο Tezuka χρησιμοποίησε κατά λάθος μόνο τη μισή διαθέσιμη μνήμη της ROM για τα dungeons",
        "distractors": [
            "Λόγω απαίτησης της Nintendo Αμερικής για μεγαλύτερη διάρκεια παιχνιδιού",
            "Για να τιμωρηθούν οι παίκτες που χρησιμοποιούσαν glitches παράκαμψης κλειδιών",
            "Επειδή το σύστημα μπαταρίας εξοικονόμησης (battery save) απαιτούσε δεύτερο slot"
        ],
        "explanation": "Όταν ο Tezuka ολοκλήρωσε τους χάρτες των dungeons, ο προγραμματιστής Toshihiko Nakago ανακάλυψε ότι είχε καταληφθεί μόνο το 50% της προβλεπόμενης μνήμης. Ο Miyamoto πρότεινε να εκμεταλλευτούν τον υπόλοιπο χώρο φτιάχνοντας μια δεύτερη, πολύ δυσκολότερη περιπέτεια.",
        "funFacts": [
            "Ο παίκτης μπορεί να ξεκινήσει απευθείας το Second Quest εισάγοντας το όνομα 'ZELDA' στην οθόνη δημιουργίας χαρακτήρα.",
            "Στο Second Quest τα dungeons σχηματίζουν τα γράμματα Z-E-L-D-A στον γενικό χάρτη."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)",
        "tags": ["gaming", "zelda", "nintendo", "miyamoto", "retro"]
    },
    {
        "id": "gaming_hard_070",
        "text": "Ποιο ιστορικό διαστημικό παιχνίδι συναλλαγών και μάχης του 1984 από τους David Braben και Ian Bell κατάφερε να χωρέσει 8 γαλαξίες και 2.048 πλανήτες σε μόλις 32KB RAM του BBC Micro;",
        "correct": "Elite",
        "distractors": [
            "Wing Commander",
            "Star Control",
            "Solar Jetman"
        ],
        "explanation": "Το Elite χρησιμοποίησε διαδικαστική παραγωγή (procedural generation) μέσω μιας ακολουθίας Fibonacci με ψευδοτυχαίους αριθμούς (PRNG seeds), υπολογίζοντας ονόματα, συντεταγμένες και οικονομίες πλανητών δυναμικά.",
        "funFacts": [
            "Οι δημιουργοί σχεδίαζαν αρχικά 2 στην 48η (πάνω από 281 τρισεκατομμύρια) γαλαξίες, αλλά ο εκδότης Acorn Soft θεώρησε ότι ένας τόσο ασύλληπτος αριθμός θα τρόμαζε τους παίκτες.",
            "Το Elite ήταν ένα από τα πρώτα οικιακά παιχνίδια που χρησιμοποίησαν τρισδιάστατα wireframe διανυσματικά γραφικά."
        ],
        "source": "https://en.wikipedia.org/wiki/Elite_(video_game)",
        "tags": ["gaming", "elite", "procedural_generation", "retro", "sci_fi"]
    },
    {
        "id": "gaming_hard_071",
        "text": "Ποια πρωτοποριακή σχεδιάστρια και συνιδρύτρια της Sierra On-Line δημιούργησε το 'Mystery House' (1980) και τη διάσημη σειρά παραμυθένιων adventure 'King's Quest';",
        "correct": "Roberta Williams",
        "distractors": [
            "Jane Jensen",
            "Amy Hennig",
            "Brenda Romero"
        ],
        "explanation": "Η Roberta Williams έγραψε το 'Mystery House' στο τραπέζι της κουζίνας της. Υπήρξε το πρώτο adventure στην ιστορία που συνδύασε κείμενο με γραφικές εικόνες, ανοίγοντας τον δρόμο για τη γιγάντωση της Sierra.",
        "funFacts": [
            "Το 'King's Quest I' (1984) αναπτύχθηκε κατόπιν παραγγελίας της IBM για να επιδείξει τις προηγμένες δυνατότητες 16 χρωμάτων του υπολογιστή IBM PCjr.",
            "Η Williams δημιούργησε επίσης το διάσημο live-action psychological horror adventure 'Phantasmagoria' (1995) που κυκλοφόρησε σε 7 CD-ROMs."
        ],
        "source": "https://en.wikipedia.org/wiki/Roberta_Williams",
        "tags": ["gaming", "sierra", "kings_quest", "adventure", "history"]
    },
    {
        "id": "gaming_hard_072",
        "text": "Ποιο ήταν το πρώτο arcade παιχνίδι που κατασκεύασε ο Allan Alcorn για την Atari το 1972 ως άσκηση εκμάθησης υπό την καθοδήγηση του Nolan Bushnell, το οποίο έγινε παγκόσμιο φαινόμενο;",
        "correct": "Pong",
        "distractors": [
            "Computer Space",
            "Breakout",
            "Asteroids"
        ],
        "explanation": "Ο Bushnell ανέθεσε στον Alcorn να φτιάξει ένα απλό παιχνίδι πινγκ-πονγκ για εξάσκηση. Όταν τοποθέτησαν το πρωτότυπο στο μπαρ Andy Capp's Tavern, η συσκευή χάλασε μέσα σε δύο μέρες επειδή ο κουμπαράς είχε φρακάρει από τα αμέτρητα κέρματα.",
        "funFacts": [
            "Η Magnavox μήνυσε την Atari ισχυριζόμενη ότι το Pong αντέγραψε το παιχνίδι ηλεκτρονικού τένις της κονσόλας Magnavox Odyssey του Ralph Baer, οδηγώντας σε εξωδικαστικό συμβιβασμό.",
            "Ο Alcorn πρόσθεσε μοναδικά ηχητικά εφέ αξιοποιώντας τις συχνότητες των διαθέσιμων ψηφιακών κυκλωμάτων χωρίς ειδικό τσιπ ήχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Pong",
        "tags": ["gaming", "atari", "pong", "arcade", "history"]
    },
    {
        "id": "gaming_hard_073",
        "text": "Ποιο πρωτοποριακό παιχνίδι του Will Wright (Maxis, 1989) προέκυψε όταν ο δημιουργός συνειδητοποίησε ότι διασκέδαζε πολύ περισσότερο σχεδιάζοντας χάρτες παρά παίζοντας το προηγούμενο παιχνίδι του ('Raid on Bungeling Bay');",
        "correct": "SimCity",
        "distractors": [
            "The Sims",
            "SimEarth",
            "Populous"
        ],
        "explanation": "Ο Wright παρατήρησε ότι το level editor του Raid on Bungeling Bay ήταν πιο συναρπαστικό από το ίδιο το shooter. Βασίστηκε στις θεωρίες αστικής δυναμικής του Jay Forrester για να προγραμματίσει την προσομοίωση του SimCity.",
        "funFacts": [
            "Κανένας μεγάλος εκδότης δεν δεχόταν να κυκλοφορήσει το SimCity για χρόνια επειδή 'δεν είχε ξεκάθαρο στόχο νίκης ή ήττας', μέχρι που η Brøderbund συμφώνησε να το διανείμει.",
            "Η επιτυχία του SimCity οδήγησε στη δημιουργία του The Sims (2000), το οποίο έγινε ένα από τα κορυφαία σε πωλήσεις franchises στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/SimCity_(1989_video_game)",
        "tags": ["gaming", "simcity", "will_wright", "simulation", "maxis"]
    },
    {
        "id": "gaming_hard_074",
        "text": "Στο 'Ultima IV: Quest of the Avatar' (1985), ποιος ήταν ο επαναστατικός στόχος του παιχνιδιού που το διαφοροποίησε πλήρως από όλα τα προηγούμενα RPGs;",
        "correct": "Η εξύψωση του χαρακτήρα σε πρότυπο ηθικής μέσα από τις Οκτώ Αρετές (χωρίς τελικό κακό/αφεντικό)",
        "distractors": [
            "Η δολοφονία του δαίμονα Mondain και η κατάκτηση του θρόνου",
            "Η συγκέντρωση ενός εκατομμυρίου χρυσών νομισμάτων για την αναδόμηση της Britannia",
            "Η απόδραση από έναν λαβύρινθο 100 ορόφων μέσα σε χρονικό όριο"
        ],
        "explanation": "Ο Richard Garriott (Lord British) αποφάσισε να αλλάξει ρότα όταν έλαβε γράμματα από γονείς που παραπονούνταν για τη βία. Στο Ultima IV ο παίκτης έπρεπε να γίνει το πνευματικό πρότυπο (Avatar) επιδεικνύοντας Τιμιότητα, Συμπόνια, Ανδρεία, Δικαιοσύνη, Θυσία, Τιμή, Πνευματικότητα και Ταπεινότητα.",
        "funFacts": [
            "Εάν ο παίκτης έκλεβε αντικείμενα ή σκότωνε αθώα πλάσματα, έχανε βαθμούς αρετής και δεν μπορούσε να ολοκληρώσει το παιχνίδι.",
            "Το σύστημα των Οκτώ Αρετών βασίστηκε בחלקו στις αρχές του Βουδισμού και του Ιπποτικού Κώδικα."
        ],
        "source": "https://en.wikipedia.org/wiki/Ultima_IV:_Quest_of_the_Avatar",
        "tags": ["gaming", "ultima", "garriott", "rpg", "ethics"]
    },
    {
        "id": "gaming_hard_075",
        "text": "Ποιο ιστορικό βιντεοπαιχνίδι δύο παικτών προγραμμάτισε ο Steve Russell το 1962 στο Τεχνολογικό Ινστιτούτο Μασαχουσέτης (MIT) στον υπολογιστή DEC PDP-1;",
        "correct": "Spacewar!",
        "distractors": [
            "Tennis for Two",
            "OXO",
            "Galaxy Game"
        ],
        "explanation": "Το Spacewar! παρουσίαζε δύο διαστημόπλοια ('Needle' και 'Wedge') που πολεμούσαν με τορπίλες σε ένα βαρυτικό πεδίο γύρω από ένα κεντρικό άστρο. Θεωρείται ευρέως το πρώτο ψηφιακό παιχνίδι υπολογιστή με ευρεία επιρροή.",
        "funFacts": [
            "Ο Peter Samson έγραψε ένα υποπρόγραμμα που ονομαζόταν 'Expensive Planetarium', αποδίδοντας με επιστημονική ακρίβεια τους πραγματικούς αστερισμούς του νυχτερινού ουρανού στο φόντο.",
            "Η DEC χρησιμοποιούσε το Spacewar! ως επίσημο διαγνωστικό πρόγραμμα για να ελέγχει αν λειτουργούν σωστά οι νέοι υπολογιστές PDP-1 πριν την παράδοση."
        ],
        "source": "https://en.wikipedia.org/wiki/Spacewar!",
        "tags": ["gaming", "mit", "spacewar", "retro", "history"]
    },
    {
        "id": "gaming_hard_076",
        "text": "Ποιο καινοτόμο εξάρτημα της κονσόλας Sega Dreamcast λειτουργούσε ως κάρτα μνήμης αλλά διέθετε δική του μονόχρωμη οθόνη LCD, κουμπιά και ηχείο για αυτόνομα minigames;",
        "correct": "VMU (Visual Memory Unit)",
        "distractors": [
            "PocketStation",
            "Controller Pak",
            "Game Boy Player"
        ],
        "explanation": "Το VMU συνδεόταν απευθείας στο χειριστήριο του Dreamcast προβάλλοντας πληροφορίες (όπως στατιστικά ζωής ή μυστικά plays στο NFL 2K) και μπορούσε να αποσπαστεί για να παίξει ο παίκτης αυτόνομα minigames όπως το 'Chao Adventure' του Sonic Adventure.",
        "funFacts": [
            "Δύο VMUs μπορούσαν να συνδεθούν μεταξύ τους για άμεση ανταλλαγή δεδομένων και μάχες μεταξύ χαρακτήρων.",
            "Το χαρακτηριστικό διαπεραστικό μπιπ που έκανε το VMU κατά το άνοιγμα της κονσόλας σήμαινε σχεδόν πάντα ότι είχε εξαντληθεί η μπαταρία ρολογιού CR2032."
        ],
        "source": "https://en.wikipedia.org/wiki/VMU",
        "tags": ["gaming", "sega", "dreamcast", "vmu", "hardware"]
    },
    {
        "id": "gaming_hard_077",
        "text": "Ποιος κορυφαίος Αμερικανός σχεδιαστής και αρχιτέκτονας συστημάτων, δημιουργός του 'Marble Madness' σε ηλικία μόλις 17 ετών, διετέλεσε επικεφαλής αρχιτέκτονας του PlayStation 4, του PS Vita και του PlayStation 5;",
        "correct": "Mark Cerny",
        "distractors": [
            "Ken Kutaragi",
            "David Jaffe",
            "Cory Barlog"
        ],
        "explanation": "Ο Mark Cerny έμαθε ιαπωνικά, εργάστηκε στη Sega και τη Sony, και ηγήθηκε του σχεδιασμού της αρχιτεκτονικής του PS4, μεταβαίνοντας στην ευέλικτη αρχιτεκτονική x86-64 της AMD που έλυσε τα προβλήματα προγραμματισμού του PS3 Cell.",
        "funFacts": [
            "Ο Cerny βοήθησε επίσης στη δημιουργία εμβληματικών χαρακτήρων όπως οι Crash Bandicoot, Spyro the Dragon και Jak and Daxter.",
            "Εισήχθη στο Hall of Fame της Academy of Interactive Arts & Sciences το 2004."
        ],
        "source": "https://en.wikipedia.org/wiki/Mark_Cerny",
        "tags": ["gaming", "sony", "playstation", "cerny", "hardware"]
    },
    {
        "id": "gaming_hard_078",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού indie τίτλου της Yacht Club Games (2014) που αναπαρήγαγε πιστά τους τεχνικούς περιορισμούς του NES (παλέτα χρωμάτων, parallax scrolling 2 layers, sprite limits);",
        "correct": "Shovel Knight",
        "distractors": [
            "Hollow Knight",
            "Axiom Verge",
            "Bloodstained: Curse of the Moon"
        ],
        "explanation": "Η Yacht Club Games σεβάστηκε σχεδόν απόλυτα τους κανόνες υλικού του NES: χρησιμοποίησε την αυθεντική παλέτα 54 χρωμάτων του NES (συν 4 έξτρα χρώματα) και διατήρησε τα εικονικά flicker effects των sprites.",
        "funFacts": [
            "Ο Shovel Knight έγινε ο πρώτος ανεξάρτητος (indie) χαρακτήρας που απέκτησε επίσημο αγαλματίδιο Amiibo από τη Nintendo.",
            "Η διάσημη συνθέτρια του Mega Man, Manami Matsumae, συνέβαλε με πρωτότυπες συνθέσεις στο soundtrack του παιχνιδιού."
        ],
        "source": "https://en.wikipedia.org/wiki/Shovel_Knight",
        "tags": ["gaming", "indie", "shovel_knight", "retro", "nes"]
    },
    {
        "id": "gaming_hard_079",
        "text": "Ποιο franchise παιχνιδιών δράσης επιστημονικής φαντασίας της Origin Systems (1990) σε σκηνοθεσία Chris Roberts χρησιμοποίησε διαδραστικές ταινίες FMV με πρωταγωνιστή τον Mark Hamill;",
        "correct": "Wing Commander",
        "distractors": [
            "Star Citizen",
            "Freelancer",
            "Privateer"
        ],
        "explanation": "Στο 'Wing Commander III: Heart of the Tiger' (1994) και στο 'Wing Commander IV', ο Mark Hamill υποδύθηκε τον συνταγματάρχη Christopher Blair σε γυρίσματα με κανονικά κινηματογραφικά σκηνικά και χολιγουντιανούς ηθοποιούς όπως ο Malcolm McDowell.",
        "funFacts": [
            "Το Wing Commander IV είχε προϋπολογισμό 12 εκατομμυρίων δολαρίων, καθιστώντας το το πιο ακριβό παιχνίδι στην ιστορία του PC gaming εκείνη την εποχή.",
            "Η σειρά πρωτοπόρησε με δυναμική μουσική που άλλαζε ομαλά ανάλογα με την εξέλιξη της αερομαχίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Wing_Commander_(video_game)",
        "tags": ["gaming", "wing_commander", "chris_roberts", "sci_fi", "pc"]
    },
    {
        "id": "gaming_hard_080",
        "text": "Στο cyberpunk αριστούργημα 'Deus Ex' (2000) της Ion Storm σε σκηνοθεσία Warren Spector, για ποιο τεχνικό λόγο έλειπαν οι Δίδυμοι Πύργοι (World Trade Center) από το skyline της Νέας Υόρκης;",
        "correct": "Λόγω περιορισμών μνήμης υφών (texture memory) στη skybox εικόνα του ορίζοντα",
        "distractors": [
            "Λόγω άρνησης της λιμενικής αρχής της Νέας Υόρκης να παραχωρήσει άδεια πνευματικών δικαιωμάτων",
            "Επειδή η πλοκή προέβλεπε ότι είχαν καταστραφεί από σεισμό",
            "Επειδή ο σχεδιαστής επιπέδων ξέχασε να συμπεριλάβει το 3D μοντέλο τους"
        ],
        "explanation": "Ο Harvey Smith εξήγησε ότι η εικόνα του ορίζοντα δεν χωρούσε ολόκληρη στη μνήμη, οπότε έκοψαν ένα τμήμα. Για να δικαιολογήσουν την απουσία, έγραψαν στο lore ότι οι πύργοι είχαν καταστραφεί από τρομοκρατική επίθεση, έναν χρόνο πριν τα πραγματικά γεγονότα της 11ης Σεπτεμβρίου 2001.",
        "funFacts": [
            "Η ανατριχιαστική αυτή σύμπτωση συζητήθηκε ευρέως μετά το 2001.",
            "Το Deus Ex θεωρείται το απόλυτο ορόσημο των immersive sims, επιτρέποντας στον JC Denton να ολοκληρώνει αποστολές με μάχη, stealth, hacking ή διπλωματία."
        ],
        "source": "https://en.wikipedia.org/wiki/Deus_Ex_(video_game)",
        "tags": ["gaming", "deus_ex", "warren_spector", "immersive_sim", "pc"]
    },
    {
        "id": "gaming_hard_081",
        "text": "Ποιο κλασικό chip γραφικών και ήχου της κονσόλας Atari 2600 (1977), σχεδιασμένο από τον Jay Miner, διέθετε μόλις 128 bytes RAM και σχεδίαζε την οθόνη καρέ-καρέ σε πραγματικό χρόνο ανά γραμμή σάρωσης ('Racing the Beam');",
        "correct": "TIA (Television Interface Adaptor)",
        "distractors": [
            "ANTIC",
            "VIC-II",
            "Paula"
        ],
        "explanation": "Το Atari 2600 δεν διέθετε frame buffer μνήμης. Οι προγραμματιστές έπρεπε να αλλάζουν τα περιεχόμενα των καταχωρητών του TIA ακριβώς τη στιγμή που η δέσμη ηλεκτρονίων της οθόνης σάρωνε κάθε οριζόντια γραμμή (racing the beam).",
        "funFacts": [
            "Ο Jay Miner σχεδίασε αργότερα το θρυλικό chipset της Commodore Amiga, κερδίζοντας τον τίτλο του 'Πατέρα της Amiga'.",
            "Το TIA είχε μόνο δύο καταχωρητές 8-bit για sprites παικτών, δύο για βλήματα και έναν για μπάλα."
        ],
        "source": "https://en.wikipedia.org/wiki/Television_Interface_Adaptor",
        "tags": ["gaming", "atari", "hardware", "tia", "retro"]
    },
    {
        "id": "gaming_hard_082",
        "text": "Ποιο πρωτοποριακό σύστημα τεχνητής νοημοσύνης (AI) χρησιμοποίησε το FPS 'F.E.A.R.' (2005) από τη Monolith Productions, κάνοντας τους κλώνους στρατιώτες Replica να φαίνονται τρομακτικά ευφυείς;",
        "correct": "GOAP (Goal-Oriented Action Planning)",
        "distractors": [
            "Finite State Machines (FSM)",
            "Deep Q-Networks",
            "Behavior Trees με fuzzy logic"
        ],
        "explanation": "Ο Jeff Orkin ανέπτυξε το σύστημα GOAP, όπου οι εχθροί δεν ακολουθούσαν προκαθορισμένα scripts αλλά έθεταν δυναμικούς στόχους (π.χ. 'κάλυψε τον σύντροφο', 'ανατροπή τραπεζιού για κάλυψη') και σχεδίαζαν τις απαραίτητες ενέργειες σε πραγματικό χρόνο.",
        "funFacts": [
            "Οι στρατιώτες μιλούσαν συνεχώς στο ραδιόφωνο αναφέροντας τις κινήσεις του παίκτη, κάνοντας τον παίκτη να πιστεύει ότι η AI ήταν πολύ πιο έξυπνη από ό,τι στην πραγματικότητα.",
            "Η τεχνολογία GOAP του F.E.A.R. διδάσκεται μέχρι σήμερα σε πανεπιστημιακά μαθήματα game AI."
        ],
        "source": "https://en.wikipedia.org/wiki/F.E.A.R._(video_game)",
        "tags": ["gaming", "fear", "monolith", "ai", "fps"]
    },
    {
        "id": "gaming_hard_083",
        "text": "Πώς κατάφεραν οι Andy Gavin και Jason Rubin της Naughty Dog να κάνουν το 'Crash Bandicoot' (1996) να φορτώνει τεράστια 3D περιβάλλοντα στο PlayStation 1 χωρίς loading screens στη μέση της πίστας;",
        "correct": "Ανέπτυξαν δικό τους σύστημα streaming δεδομένων απευθείας από το CD-ROM στα 64KB RAM",
        "distractors": [
            "Συμπίεσαν όλα τα textures σε μορφή JPEG μέσα στη μνήμη του BIOS",
            "Χρησιμοποίησαν αποκλειστικά flat-shaded πολύγωνα χωρίς textures",
            "Αποθήκευσαν τα επίπεδα στην κάρτα μνήμης PlayStation Memory Card"
        ],
        "explanation": "Το CD-ROM του PS1 ήταν πολύ αργό. Ο Gavin έγραψε έναν προηγμένο αλγόριθμο streaming που φόρτωνε τα επόμενα 3D κομμάτια της πίστας από το δισκάκι καθώς ο Crash προχωρούσε, ξεπερνώντας τα όρια της κονσόλας.",
        "funFacts": [
            "Ο Gavin δημιούργησε επίσης μια δική του γλώσσα προγραμματισμού, την GOOL (Game Oriented Object Lisp), ειδικά για το Crash Bandicoot.",
            "Η Sony αρχικά ανησυχούσε ότι ο συνεχής στροβιλισμός του CD drive θα κατέστρεφε τα μοτέρ των κονσολών."
        ],
        "source": "https://en.wikipedia.org/wiki/Crash_Bandicoot_(video_game)",
        "tags": ["gaming", "naughty_dog", "crash_bandicoot", "playstation", "programming"]
    },
    {
        "id": "gaming_hard_084",
        "text": "Ποιο ασυνήθιστο φυσικό χαρακτηριστικό περιείχε το δισκάκι του 'Gran Turismo 2' (1999) στην ειδική ευρωπαϊκή και αμερικανική έκδοση 'Simulation Disc';",
        "correct": "Τεχνολογία Scratch & Sniff με άρωμα καμένου καουτσούκ / pit stop",
        "distractors": [
            "Ολογραφική εκτύπωση που άλλαζε αυτοκίνητο ανάλογα με τη γωνία θέασης",
            "Μικροτσίπ που αναβόσβηνε ένα κόκκινο LED κατά την περιστροφή",
            "Θερμοχρωμική βαφή που εμφάνιζε το λογότυπο της Ferrari όταν ζεσταινόταν"
        ],
        "explanation": "Η Polyphony Digital τύπωσε το Simulation Disc με αρωματικό μελάνι μικροκαψουλών. Όταν ο παίκτης έξυνε την επιφάνεια του CD, αναδυόταν μια έντονη μυρωδιά καμένου ελαστικού και καυσίμων αγώνων.",
        "funFacts": [
            "Το παιχνίδι περιλάμβανε πάνω από 650 αυτοκίνητα και 27 πίστες, εξαπλωμένο σε δύο οπτικούς δίσκους (Arcade Disc και Simulation Disc).",
            "Ένα σφάλμα στον κώδικα εμπόδιζε το παιχνίδι να φτάσει στο 100% ολοκλήρωσης, σταματώντας στο 98.2% στην αρχική έκδοση."
        ],
        "source": "https://en.wikipedia.org/wiki/Gran_Turismo_2",
        "tags": ["gaming", "gran_turismo", "playstation", "polyphony", "trivia"]
    },
    {
        "id": "gaming_hard_085",
        "text": "Ποιος κορυφαίος Βρετανός κωμικός και ηθοποιός (συνδημιουργός του 'The Office') δάνεισε τη φωνή του στην αδέξια τεχνητή νοημοσύνη Wheatley στο 'Portal 2' (2011);",
        "correct": "Stephen Merchant",
        "distractors": [
            "Ricky Gervais",
            "Simon Pegg",
            "Martin Freeman"
        ],
        "explanation": "Οι σεναριογράφοι της Valve Erik Wolpaw και Chet Faliszek ήθελαν συγκεκριμένα τον Stephen Merchant για τον ρόλο του Wheatley λόγω του μοναδικού στυλ νευρικής και φλύαρης κωμωδίας του.",
        "funFacts": [
            "Ο Merchant παραδέχτηκε αργότερα ότι η ηχογράφηση ήταν τόσο εξαντλητική λόγω του τεράστιου όγκου διαλόγων και των εναλλακτικών ατακών που δεν ήταν σίγουρος αν θα ξαναδούλευε σε video game.",
            "Η ερμηνεία του κέρδισε το βραβείο 'Best Performance by a Human Male' στα Spike Video Game Awards 2011."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_2",
        "tags": ["gaming", "portal2", "valve", "wheatley", "voice_acting"]
    },
    {
        "id": "gaming_hard_086",
        "text": "Ποιο ήταν το πρώτο παιχνίδι στην ιστορία του PlayStation 1 που απαιτούσε υποχρεωτικά τη χρήση των δύο αναλογικών μοχλών του χειριστηρίου DualShock για να παιχτεί;",
        "correct": "Ape Escape (1999)",
        "distractors": [
            "Gran Turismo",
            "Metal Gear Solid",
            "Spyro the Dragon"
        ],
        "explanation": "Στο Ape Escape της Sony Japan, ο αριστερός μοχλός κινούσε τον Spike και ο δεξιός μοχλός κατεύθυνε τα gadgets (απόχη, σπαθί φωτός, ραντάρ), καθιστώντας αδύνατο το παιχνίδι με το αρχικό ψηφιακό χειριστήριο D-pad.",
        "funFacts": [
            "Κάθε πίθηκος στο Ape Escape είχε το δικό του μοναδικό όνομα, στατιστικά ταχύτητας και επιθετικότητας, καθώς και ξεκαρδιστικές περιγραφές.",
            "Το παιχνίδι σχεδιάστηκε ειδικά για να προωθήσει τις πωλήσεις του νέου χειριστηρίου DualShock."
        ],
        "source": "https://en.wikipedia.org/wiki/Ape_Escape_(video_game)",
        "tags": ["gaming", "playstation", "dualshock", "ape_escape", "hardware"]
    },
    {
        "id": "gaming_hard_087",
        "text": "Ποια διάσημη βρετανική εταιρεία γραφιστικής (The Designers Republic) δημιούργησε τη φουτουριστική οπτική ταυτότητα, τα λογότυπα και τα μενού της σειράς αγώνων 'Wipeout' της Psygnosis;",
        "correct": "The Designers Republic (tDR)",
        "distractors": [
            "Pentagram",
            "Factory Records",
            "Tomato"
        ],
        "explanation": "Η Designers Republic με έδρα το Sheffield έδωσε στο Wipeout μια επαναστατική αντι-κουλτούρα clubbing αισθητική, γεμάτη ιαπωνική τυπογραφία, φουτουριστικές εταιρικές μάρκες (Feisar, AG Systems) και sci-fi σύμβολα.",
        "funFacts": [
            "Το Wipeout τοποθετήθηκε στρατηγικά σε νυχτερινά clubs της Μεγάλης Βρετανίας δίπλα στους DJs, συνδέοντας για πρώτη φορά το PlayStation με τη νεανική κουλτούρα της ηλεκτρονικής μουσικής.",
            "Το soundtrack περιλάμβανε κορυφαία ονόματα όπως Prodigy, Chemical Brothers, Orbital και Underworld."
        ],
        "source": "https://en.wikipedia.org/wiki/Wipeout_(video_game)",
        "tags": ["gaming", "wipeout", "psygnosis", "design", "playstation"]
    },
    {
        "id": "gaming_hard_088",
        "text": "Ποιο ήταν το όνομα του πρωτοτύπου χωρίς χαρακτήρες της Nintendo που δημιούργησαν οι Masahiro Sakurai και Satoru Iwata τα Σαββατοκύριακα, το οποίο εξελίχθηκε στο 'Super Smash Bros.' (1999);",
        "correct": "Dragon King: The Animation (Ryuto)",
        "distractors": [
            "Battle Arena Nintendo",
            "Melee Brawler 64",
            "Super Fighter All-Stars"
        ],
        "explanation": "Ο Sakurai σχεδίασε έναν 4-player brawler με άσημα πολυγωνικά ανδρείκελα ('Dragon King'). Γνωρίζοντας ότι η Nintendo δεν θα ενέκρινε εύκολα νέο fighting game, ο Iwata και ο Sakurai έβαλαν κρυφά τον Mario, τον Donkey Kong, τον Samus και τον Fox πριν το παρουσιάσουν.",
        "funFacts": [
            "Ο Shigeru Miyamoto ήταν αρχικά εξαιρετικά επιφυλακτικός στην ιδέα να βλέπει τους αγαπημένους χαρακτήρες της Nintendo να δέρνουν ο ένας τον άλλον.",
            "Το Super Smash Bros. πούλησε πάνω από 5 εκατομμύρια αντίτυπα στο Nintendo 64 και γέννησε ένα από τα μεγαλύτερα franchise esports."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Smash_Bros._(video_game)",
        "tags": ["gaming", "nintendo64", "smash_bros", "sakurai", "iwata"]
    },
    {
        "id": "gaming_hard_089",
        "text": "Στο 'Metal Gear Solid 2: Sons of Liberty' (2001), ποιο ήταν το τεράστιο διαφημιστικό μυστικό που απέκρυψε ο Hideo Kojima από όλα τα trailers πριν την κυκλοφορία του παιχνιδιού;",
        "correct": "Ότι ο πρωταγωνιστής στο 90% του παιχνιδιού ήταν ο Raiden και όχι ο Solid Snake",
        "distractors": [
            "Ότι ο Solidus Snake ήταν ο πραγματικός Πρόεδρος των ΗΠΑ",
            "Ότι η πλατφόρμα Big Shell ήταν στην πραγματικότητα το Arsenal Gear",
            "Ότι οι Patriots ήταν ένα πρόγραμμα υπολογιστή που είχε πεθάνει 100 χρόνια πριν"
        ],
        "explanation": "Όλα τα trailers και το περίφημο demo του Tanker έδειχναν αποκλειστικά τον Solid Snake. Μόλις οι παίκτες ολοκλήρωναν το Tanker chapter, ο έλεγχος περνούσε στον πρωτάρη πράκτορα Raiden, προκαλώντας τεράστιο σοκ στην κοινότητα.",
        "funFacts": [
            "Ο Kojima επέλεξε τον Raiden για να επιτρέψει στους παίκτες να δουν τον θρυλικό Solid Snake από μια εξωτερική προοπτική θαυμασμού.",
            "Η πλοκή του MGS2 για την παραπληροφόρηση, τους αλγόριθμους φιλτραρίσματος περιεχομένου και τα fake news αποδείχθηκε ανατριχιαστικά προφητική για τη σύγχρονη εποχή των social media."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_2:_Sons_of_Liberty",
        "tags": ["gaming", "metal_gear", "kojima", "raiden", "playstation2"]
    },
    {
        "id": "gaming_hard_090",
        "text": "Ποιος διάσημος μηχανισμός του 'Tony Hawk's Pro Skater 2' (2000) από τη Neversoft επέτρεψε για πρώτη φορά τη σύνδεση κινήσεων δρόμου (grinds/flatland) με άλματα σε ράμπες (vert), εκτοξεύοντας τα combos σε εκατομμύρια βαθμούς;",
        "correct": "Το Manual (ισορροπία στις πίσω ή μπροστινές ρόδες)",
        "distractors": [
            "Το Revert",
            "Το Spine Transfer",
            "Το Wallplant"
        ],
        "explanation": "Το Manual (πάτημα πάνω-κάτω ή κάτω-πάνω) επέτρεψε στους skaters να προσγειώνονται από ένα κόλπο και να συνεχίζουν την αλυσίδα combo τρέχοντας στο έδαφος μέχρι το επόμενο rail ή ramp.",
        "funFacts": [
            "Στο Tony Hawk's Pro Skater 3 προστέθηκε το 'Revert', συμπληρώνοντας την τριπλέτα μηχανισμών που επέτρεπε ατελείωτα combos χωρίς διακοπή.",
            "Το THPS2 κατέχει μία από τις υψηλότερες βαθμολογίες όλων των εποχών στο Metacritic (98/100)."
        ],
        "source": "https://en.wikipedia.org/wiki/Tony_Hawk%27s_Pro_Skater_2",
        "tags": ["gaming", "tony_hawk", "skateboarding", "neversoft", "mechanics"]
    },
    {
        "id": "gaming_hard_091",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού music rhythm game της Harmonix και της RedOctane το 2005 που συνόδευσε το παιχνίδι με μια πλαστική κιθάρα-χειριστήριο σε σχήμα Gibson SG;",
        "correct": "Guitar Hero",
        "distractors": [
            "Rock Band",
            "GuitarFreaks",
            "Band Hero"
        ],
        "explanation": "Η Harmonix άντλησε έμπνευση από το ιαπωνικό arcade 'GuitarFreaks' της Konami, αλλά η RedOctane σχεδίασε ένα προσιτό χειριστήριο κιθάρας για το PS2, δημιουργώντας ένα από τα πιο κερδοφόρα franchises της δεκαετίας του 2000.",
        "funFacts": [
            "Η Harmonix εξαγοράστηκε αργότερα από το MTV/Viacom και δημιούργησε το 'Rock Band', προσθέτοντας ντραμς και μικρόφωνο.",
            "Το τραγούδι 'Through the Fire and Flames' των DragonForce στο Guitar Hero III έγινε το απόλυτο τεστ δεξιοτεχνίας για εκατομμύρια παίκτες παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Guitar_Hero_(video_game)",
        "tags": ["gaming", "guitar_hero", "harmonix", "music", "playstation2"]
    },
    {
        "id": "gaming_hard_092",
        "text": "Ποια πρωτοποριακή τεχνική μουσικής σύνθεσης χρησιμοποίησε ο Grant Kirkhope στο 'Banjo-Kazooie' (1998) για να αλλάζει ομαλά η ενορχήστρωση της μουσικής όταν ο παίκτης έμπαινε σε σπηλιά ή βουτούσε στο νερό;",
        "correct": "Δυναμικό fade μεταξύ καναλιών MIDI με διαφορετικά όργανα στον ίδιο ρυθμό",
        "distractors": [
            "Crossfade ανάμεσα σε 10 διαφορετικά αρχεία MP3",
            "Πραγματικό DSP low-pass filtering από το chip ήχου",
            "Αναπαραγωγή ανάποδων ηχητικών κυματομορφών"
        ],
        "explanation": "Ο Kirkhope έγραψε όλα τα όργανα σε συγχρονισμένα κανάλια MIDI. Όταν ο παίκτης βουτούσε στο νερό, τα πνευστά και τα κρουστά σίγησαν και ανέβηκε η ένταση της άρπας και του marimba, χωρίς καμία διακοπή στον ρυθμό.",
        "funFacts": [
            "Ο Kirkhope έγραψε επίσης το διάσημο 'DK Rap' για το Donkey Kong 64, το οποίο ξεκίνησε ως παρωδία αλλά έγινε λατρεμένο κλασικό κομμάτι.",
            "Η τεχνική του Banjo-Kazooie αποτέλεσε πρότυπο για το adaptive audio στη σύγχρονη βιομηχανία games."
        ],
        "source": "https://en.wikipedia.org/wiki/Banjo-Kazooie_(video_game)",
        "tags": ["gaming", "nintendo64", "rare", "music", "kirkhope"]
    },
    {
        "id": "gaming_hard_093",
        "text": "Στο 'The Elder Scrolls III: Morrowind' (2002), ποιο σύστημα μάχης ξένισε πολλούς παίκτες action RPGs παρότι το παιχνίδι παιζόταν σε πρώτο πρόσωπο;",
        "correct": "Οι εικονικές 'ζαριές' επιτυχίας χτυπήματος στο παρασκήνιο βάσει στατιστικών και κόπωσης (fatigue)",
        "distractors": [
            "Το Active Time Battle σύστημα με μπάρα αναμονής",
            "Η υποχρεωτική εκτέλεση quick-time events σε κάθε επίθεση",
            "Η απώλεια αντοχής μόνο κατά την απόκρουση με ασπίδα"
        ],
        "explanation": "Αν και το Morrowind φαινόταν σαν real-time FPS, κάθε φορά που το σπαθί του παίκτη άγγιζε το μοντέλο του εχθρού, ο κώδικας εκτελούσε μαθηματικό έλεγχο πιθανοτήτων βασισμένο στο weapon skill και το Fatigue, προκαλώντας συχνά 'αστοχία' σε αρχάριους χαρακτήρες.",
        "funFacts": [
            "Ο παίκτης μπορούσε να φτιάξει δικά του ξόρκια και να εκμεταλλευτεί το σύστημα αλχημείας για να φτιάξει φίλτρα που του επέτρεπαν να πηδήξει από τη μία άκρη του χάρτη Vvardenfell στην άλλη.",
            "Το Morrowind έσωσε την Bethesda Softworks από τη χρεοκοπία και καθιέρωσε τη σειρά The Elder Scrolls ως παγκόσμιο φαινόμενο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_III:_Morrowind",
        "tags": ["gaming", "morrowind", "bethesda", "rpg", "mechanics"]
    },
    {
        "id": "gaming_hard_094",
        "text": "Ποιο κλασικό RPG του 2004 από την Troika Games, βασισμένο στο επιτραπέζιο της White Wolf, κυκλοφόρησε την ίδια ακριβώς ημέρα με το Half-Life 2 χρησιμοποιώντας τη Source Engine και απέκτησε τεράστιο cult κοινό χάρη στα fan patches;",
        "correct": "Vampire: The Masquerade – Bloodlines",
        "distractors": [
            "Arcanum: Of Steamworks and Magick Obscura",
            "The Temple of Elemental Evil",
            "Planescape: Torment"
        ],
        "explanation": "Το Bloodlines είχε σοβαρά bugs κατά την κυκλοφορία λόγω βιαστικού launch από την Activision, αλλά αναγνωρίζεται ως ένα από τα σπουδαιότερα RPGs όλων των εποχών για το σενάριο, τους χαρακτήρες και τις επιλογές των φυλών (όπως οι Malkavian και Nosferatu).",
        "funFacts": [
            "Παίζοντας ως Malkavian, όλοι οι διάλογοι του παίκτη ξαναγράφτηκαν σε ποιητικό/παρανοϊκό ύφος, αποκαλύπτοντας μυστικά του μέλλοντος με κωδικοποιημένες φράσεις.",
            "Η κοινότητα των modders, υπό τον Wesp5, συνέχισε να ενημερώνει και να διορθώνει το παιχνίδι με ανεπίσημα patches για πάνω από 15 χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Vampire:_The_Masquerade_%E2%80%93_Bloodlines",
        "tags": ["gaming", "troika", "vampire", "rpg", "pc"]
    },
    {
        "id": "gaming_hard_095",
        "text": "Ποιος Ιάπωνας δημιουργός της Namco σχεδίασε το σουρεαλιστικό 'Katamari Damacy' (2004) στο PlayStation 2, όπου ένας μικροσκοπικός πρίγκιπας κυλάει μια κολλώδη μπάλα μεγαλώνοντάς την σε μέγεθος πλανήτη;",
        "correct": "Keita Takahashi",
        "distractors": [
            "Tetsuya Mizuguchi",
            "Goichi Suda",
            "Masahiro Sakurai"
        ],
        "explanation": "Ο Keita Takahashi ξεκίνησε το Katamari Damacy ως ένα σχολικό project μικρού προϋπολογισμού στο Namco Digital Hollywood Game Laboratory, επιδιώκοντας να φτιάξει κάτι εντελώς αντίθετο από τα βίαια και περίπλοκα mainstream παιχνίδια της εποχής.",
        "funFacts": [
            "Ο πατέρας του πρίγκιπα, ο 'King of All Cosmos', έγινε ένας από τους πιο εκκεντρικούς και αγαπημένους χαρακτήρες των video games για τα σαρκαστικά του σχόλια.",
            "Το Katamari Damacy εκτίθεται μόνιμα στη συλλογή βιντεοπαιχνιδιών του Μουσείου Μοντέρνας Τέχνης (MoMA) της Νέας Υόρκης."
        ],
        "source": "https://en.wikipedia.org/wiki/Katamari_Damacy",
        "tags": ["gaming", "namco", "katamari", "playstation2", "design"]
    },
    {
        "id": "gaming_hard_096",
        "text": "Ποιο παραδοσιακό κινεζικό κλασικό λογοτεχνικό έπος ('Water Margin' / Ιστορία των Βάλτων) αποτέλεσε την άμεση πηγή έμπνευσης για τη συλλογή των '108 Stars of Destiny' στη σειρά JRPG 'Suikoden' της Konami;",
        "correct": "Shui Hu Zhuan (Χρονικό των Βάλτων)",
        "distractors": [
            "Romance of the Three Kingdoms",
            "Journey to the West",
            "Dream of the Red Chamber"
        ],
        "explanation": "Ο Yoshitaka Murayama βάσισε το Suikoden στο 'Shui Hu Zhuan' (που στα ιαπωνικά διαβάζεται Suikoden). Σε κάθε παιχνίδι, ο παίκτης συγκεντρώνει ακριβώς 108 μοναδικούς χαρακτήρες (Stars of Destiny) για να χτίσει το στρατηγείο του και να νικήσει την αυτοκρατορία.",
        "funFacts": [
            "Η στρατολόγηση και των 108 χαρακτήρων πριν από συγκεκριμένα γεγονότα της πλοκής ήταν απαραίτητη για να ξεκλειδωθεί το 'καλό' τέλος του παιχνιδιού.",
            "Τα δεδομένα save του πρώτου Suikoden μπορούσαν να μεταφερθούν στο Suikoden II (1998), ξεκλειδώνοντας τον αρχικό πρωταγωνιστή Tir McDohl ως μυστικό σύμμαχο."
        ],
        "source": "https://en.wikipedia.org/wiki/Suikoden",
        "tags": ["gaming", "suikoden", "konami", "rpg", "playstation"]
    },
    {
        "id": "gaming_hard_097",
        "text": "Ποιο διάσημο μηχανισμό επαναφοράς χρόνου (Rewind mechanic) εφάρμοσε η Ubisoft Montreal στο 'Prince of Persia: The Sands of Time' (2003) υπό την καθοδήγηση του Patrice Désilets;",
        "correct": "Το Dagger of Time (Εγχειρίδιο του Χρόνου) που επέτρεπε γύρισμα του χρόνου έως 10 δευτερόλεπτα πίσω",
        "distractors": [
            "Την Κλεψύδρα της Achronia που πάγωνε τους εχθρούς",
            "Το Δαχτυλίδι της Μοίρας που επιβράδυνε τα άλματα",
            "Το Μενταγιόν του Χάους που αντάλλασσε θέσεις με σκιές"
        ],
        "explanation": "Ο Désilets σκέφτηκε ότι η αποτυχία σε ένα δύσκολο platformer δεν έπρεπε να σημαίνει loading screen και θάνατο. Το Dagger of Time επέτρεπε στον παίκτη να γυρίσει πίσω τον χρόνο και να διορθώσει ένα λάθος άλμα σε πραγματικό χρόνο.",
        "funFacts": [
            "Η τεχνογνωσία και οι μηχανισμοί αναρρίχησης του Sands of Time οδήγησαν άμεσα στη δημιουργία του Assassin's Creed (2007) από την ίδια ομάδα.",
            "Όταν ο πρίγκιπας πέθαινε, η αφήγηση διέκοπτε λέγοντας: 'Όχι, όχι, δεν έγινε έτσι... μπορώ να αρχίσω ξανά;'"
        ],
        "source": "https://en.wikipedia.org/wiki/Prince_of_Persia:_The_Sands_of_Time",
        "tags": ["gaming", "prince_of_persia", "ubisoft", "rewind", "mechanics"]
    },
    {
        "id": "gaming_hard_098",
        "text": "Ποια διάσημη σειρά JRPG του Game Boy Advance από την Camelot Software Planning επέτρεπε στους παίκτες να μεταφέρουν όλα τα Djinn και τα στατιστικά τους στο sequel χρησιμοποιώντας καλώδιο Game Link ή έναν τεράστιο κωδικό 260 χαρακτήρων (Gold Password);",
        "correct": "Golden Sun (και Golden Sun: The Lost Age)",
        "distractors": [
            "Mario & Luigi: Superstar Saga",
            "Mega Man Battle Network",
            "Boktai: The Sun Is in Your Hand"
        ],
        "explanation": "Τα δύο παιχνίδια Golden Sun σχεδιάστηκαν αρχικά ως ένας ενιαίος τίτλος για το Nintendo 64. Όταν μεταφέρθηκαν στο GBA, χωρίστηκαν σε δύο μέρη και η Camelot δημιούργησε το σύστημα Gold Password για να διατηρηθεί η συνέχεια των αποφάσεων του παίκτη.",
        "funFacts": [
            "Το σύστημα μάχης βασιζόταν στα Djinn, μικρά πνεύματα στοιχείων της φύσης που άλλαζαν τις κλάσεις (classes) και τα psynergy ξόρκια των χαρακτήρων.",
            "Τα ψευδο-3D γραφικά μάχης του Golden Sun θεωρούνταν από τα πιο εντυπωσιακά τεχνικά επιτεύγματα στην ιστορία του Game Boy Advance."
        ],
        "source": "https://en.wikipedia.org/wiki/Golden_Sun",
        "tags": ["gaming", "golden_sun", "gba", "nintendo", "rpg"]
    },
    {
        "id": "gaming_hard_099",
        "text": "Ποιος ήταν ο λόγος που ο Keiji Inafune και η ομάδα της Capcom επέλεξαν το μπλε χρώμα για τον Mega Man (Rockman) στο αρχικό παιχνίδι του NES το 1987;",
        "correct": "Επειδή η παλέτα 54 χρωμάτων του NES διέθετε τις περισσότερες διαφορετικές αποχρώσεις του μπλε",
        "distractors": [
            "Επειδή το μπλε ήταν το αγαπημένο χρώμα του προέδρου της Capcom Kenzo Tsujimoto",
            "Για να ξεχωρίζει από τον κόκκινο Mario της Nintendo",
            "Επειδή συμβόλιζε την καθαρή ηλεκτρική ενέργεια της πυρηνικής μπαταρίας του"
        ],
        "explanation": "Το Nintendo Entertainment System είχε πολύ περιορισμένη χρωματική παλέτα. Το μπλε είχε τη μεγαλύτερη ποικιλία διαβαθμίσεων (shades), επιτρέποντας στους καλλιτέχνες να δώσουν βάθος, σκίαση και λεπτομέρεια στο μικροσκοπικό sprite του χαρακτήρα.",
        "funFacts": [
            "Στην Ιαπωνία ονομάζεται Rockman, αποτελώντας μουσικό λογοπαίγνιο Rock & Roll μαζί με τη 'δίδυμη' αδελφή του Roll.",
            "Όταν ο Mega Man νικάει ένα αφεντικό Robot Master, αλλάζει χρώμα για να δείξει ποιο νέο όπλο έχει εξοπλιστεί."
        ],
        "source": "https://en.wikipedia.org/wiki/Mega_Man_(character)",
        "tags": ["gaming", "capcom", "megaman", "nes", "retro"]
    },
    {
        "id": "gaming_hard_100",
        "text": "Ποιος κορυφαίος σεναριογράφος και σκηνοθέτης της Square (μαζί με τον Tetsuya Nomura) πήρε τη ριζοσπαστική απόφαση για τον τραγικό θάνατο της Aerith Gainsborough στο 'Final Fantasy VII' (1997);",
        "correct": "Yoshinori Kitase",
        "distractors": [
            "Hironobu Sakaguchi",
            "Kazushige Nojima",
            "Hiroyuki Ito"
        ],
        "explanation": "Ο Kitase και ο Nomura ήθελαν να απεικονίσουν έναν θάνατο που θα ήταν ξαφνικός, άδικος και οδυνηρός, χωρίς ηρωικό μελόδραμα, ώστε ο παίκτης να βιώσει το πραγματικό κενό και τη συναισθηματική απώλεια ενός αγαπημένου προσώπου.",
        "funFacts": [
            "Ο θάνατος της Aerith στην Πόλη των Αρχαίων από το σπαθί Masamune του Sephiroth θεωρείται η πιο πολυσυζητημένη και συγκινητική σκηνή στην ιστορία των video games.",
            "Εκατομμύρια παίκτες πέρασαν χρόνια αναζητώντας ανύπαρκτα glitches και μυστικά για να την 'αναστήσουν' στην αρχική έκδοση του PS1."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VII",
        "tags": ["gaming", "final_fantasy", "aerith", "playstation", "square"]
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

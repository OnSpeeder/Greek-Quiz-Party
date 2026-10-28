# -*- coding: utf-8 -*-
"""
Generator for gaming_medium questions: Batch 4 (gaming_med_161 to gaming_med_210)
50 questions total.
Target correctAnswerIndex distribution:
  0: 12
  1: 12
  2: 13
  3: 13
Total = 50
"""

import sys
from base_generator import append_questions

NEW_QUESTIONS = [
    # 161
    {
        "id": "gaming_med_161",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο κλασικό παιχνίδι «Shadow of the Colossus», ποιο είναι το όνομα του πιστού αλόγου του πρωταγωνιστή Wander;",
        "answers": ["Agro", "Epona", "Phobos", "Shadowfax"],
        "correctAnswerIndex": 0,
        "explanation": "Το πιστό άλογο του Wander ονομάζεται Agro και παίζει κρίσιμο ρόλο τόσο στις μετακινήσεις όσο και στην αντιμετώπιση αρκετών Κολοσσών.",
        "funFacts": [
            "Ο δημιουργός Fumito Ueda σχεδίασε την κίνηση του Agro ώστε να μοιάζει με αληθινό ζώο που αντιδρά αυτόνομα στο έδαφος και όχι απλά σαν όχημα.",
            "Η συγκινητική σκηνή στη γέφυρα πριν τον τελικό Κολοσσό θεωρείται μία από τις πιο εμβληματικές στιγμές στην ιστορία των βιντεοπαιχνιδιών."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_of_the_Colossus",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "playstation", "adventure"]
    },
    # 162
    {
        "id": "gaming_med_162",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Resident Evil 4» (2005), πώς αποκαλείται επίσημα ο εχθρός με το αλυσοπρίονο και τη λινάτσα στο κεφάλι στο ισπανικό χωριό;",
        "answers": ["Nemesis", "Dr. Salvador", "Jack Baker", "Mr. X"],
        "correctAnswerIndex": 1,
        "explanation": "Ο εμβληματικός Ganado που κρατάει αλυσοπρίονο και φοράει κουκούλα από λινάτσα αναφέρεται επίσημα ως Dr. Salvador.",
        "funFacts": [
            "Ο ήχος του αλυσοπρίονου του Dr. Salvador αποτελεί έναν από τους πιο αναγνωρίσιμους και τρομακτικούς ήχους στο survival horror είδος.",
            "Στο Resident Evil 4, μία μόνο επιτυχημένη επίθεση από το αλυσοπρίονό του οδηγεί σε άμεσο αποκεφαλισμό του Leon S. Kennedy."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_4",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "resident-evil", "horror"]
    },
    # 163
    {
        "id": "gaming_med_163",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «BioShock Infinite», ποιο γιγάντιο μηχανικό πλάσμα φρουρεί την Elizabeth και λειτουργεί ως φύλακας του πύργου της στην Columbia;",
        "answers": ["Big Daddy", "Handyman", "Songbird", "Motorized Patriot"],
        "correctAnswerIndex": 2,
        "explanation": "Το Songbird είναι ένα τεράστιο μηχανικό πτηνό που λειτουργούσε ως ο μοναδικός σύντροφος αλλά και δεσμοφύλακας της Elizabeth στον πύργο της.",
        "funFacts": [
            "Το Songbird ελέγχεται και ηρεμεί μέσω συγκεκριμένων μουσικών συχνοτήτων που παίζονται σε ένα ειδικό σφυρίχτρα-όργανο.",
            "Η σχέση της Elizabeth με το Songbird συνδυάζει στοιχεία στοργής και έντονου φόβου, δημιουργώντας ένα ψυχολογικό σύνδρομο αιχμαλωσίας."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock_Infinite",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "bioshock"]
    },
    # 164
    {
        "id": "gaming_med_164",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο πρώτο «Mass Effect», ποιο αρχαίο σκάφος ήταν η ναυαρχίδα του Saren Arterius και αποδείχθηκε ότι ήταν ένα ζωντανό Reaper;",
        "answers": ["Destiny Ascension", "Harbinger", "Collector Cruiser", "Sovereign"],
        "correctAnswerIndex": 3,
        "explanation": "Το Sovereign (γνωστό και ως Nazara) ήταν το πρώτο Reaper που αντιμετώπισε ο Commander Shepard, λειτουργώντας αρχικά ως η ναυαρχίδα του αποστάτη Spectre Saren.",
        "funFacts": [
            "Ο διάλογος του Sovereign στον πλανήτη Virmire («You exist because we allow it, and you will end because we demand it») θεωρείται ένας από τους πιο ανατριχιαστικούς στην ιστορία του RPG.",
            "Το Sovereign προσπάθησε να ενεργοποιήσει χειροκίνητα το Citadel relay ώστε να καλέσει τον υπόλοιπο στόλο των Reapers από το σκοτεινό διάστημα."
        ],
        "source": "https://en.wikipedia.org/wiki/Mass_Effect_(video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "mass-effect"]
    },
    # 165
    {
        "id": "gaming_med_165",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο αρχικό παιχνίδι «Fallout» (1997), ποιο κρίσιμο εξάρτημα στέλνεται να βρει ο Vault Dweller στην Wasteland για να σώσει το Vault 13;",
        "answers": ["Water Chip", "G.E.C.K.", "Platinum Chip", "Fusion Core"],
        "correctAnswerIndex": 0,
        "explanation": "Ο πρωταγωνιστής ξεκινά την αποστολή του επειδή χάλασε το Water Chip (τσιπ καθαρισμού νερού) του Vault 13, απειλώντας τους κατοίκους με αφυδάτωση.",
        "funFacts": [
            "Ο παίκτης είχε αρχικά ένα αυστηρό χρονικό όριο 150 ημερών εντός του παιχνιδιού για να βρει το Water Chip πριν πεθάνουν όλοι στο Vault 13.",
            "Το G.E.C.K. (Garden of Eden Creation Kit) έγινε το κύριο αντικείμενο αναζήτησης στο επόμενο παιχνίδι, το Fallout 2."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout_(video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "fallout"]
    },
    # 166
    {
        "id": "gaming_med_166",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Half-Life 2», ποιος ιδιόρρυθμος ιερέας καθοδηγεί και βοηθάει τον Gordon Freeman στην παγιδευμένη πόλη Ravenholm;",
        "answers": ["Barney Calhoun", "Πατέρας Grigori", "Eli Vance", "Arne Magnusson"],
        "correctAnswerIndex": 1,
        "explanation": "Ο πατέρας Grigori είναι ο μοναδικός επιζών ιερέας στο Ravenholm, ο οποίος κατασκεύασε θανατηφόρες παγίδες ενάντια στα ζόμπι και τα headcrabs.",
        "funFacts": [
            "Ο πατέρας Grigori χρησιμοποιεί μια τροποποιημένη καραμπίνα Winchester την οποία αποκαλεί χαϊδευτικά «Annabelle».",
            "Η φωνή και τα γέλια του Grigori αντηχούν σε όλο το κεφάλαιο «We Don't Go To Ravenholm...», που αποτελεί φόρο τιμής στο survival horror."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "valve"]
    },
    # 167
    {
        "id": "gaming_med_167",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Portal 2», σε ποιο απροσδόκητο αντικείμενο συνδέεται προσωρινά η μονάδα τεχνητής νοημοσύνης της GLaDOS από τον Wheatley;",
        "answers": ["Σε μια οθόνη χειρός", "Σε έναν κύβο συντροφιάς", "Σε μια πατάτα", "Σε έναν πυρσό ασφαλείας"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Wheatley αντικαθιστά την GLaDOS στον κεντρικό υπολογιστή και συνδέει τη συνείδησή της σε μια μπαταρία πατάτας (Potato GLaDOS ή PotatOS).",
        "funFacts": [
            "Ως πατάτα, η GLaDOS λειτουργεί με ελάχιστη ηλεκτρική ενέργεια, κάτι που την εμποδίζει να χρησιμοποιεί τις προηγμένες λειτουργίες εξόντωσης.",
            "Η φωνή της Ellen McLain υπέστη ειδική επεξεργασία για να ακούγεται πιο αδύναμη και χαμηλόφωνη όταν η GLaDOS είναι συνδεδεμένη στην πατάτα."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "puzzle", "valve"]
    },
    # 168
    {
        "id": "gaming_med_168",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο παιχνίδι «Dishonored» (2012), ποια φονική επιδημία αποδεκατίζει τον πληθυσμό της βιομηχανικής πόλης Dunwall;",
        "answers": ["Γρίπη του αίματος", "Μαύρος θάνατος", "Μόλυνση από φάλαινες", "Πανώλη των αρουραίων"],
        "correctAnswerIndex": 3,
        "explanation": "Η πόλη Dunwall μαστίζεται από την πανώλη των αρουραίων (Rat Plague), η οποία μετατρέπει τα θύματα σε επιθετικά πλάσματα που αποκαλούνται Weepers.",
        "funFacts": [
            "Όσο περισσότερους ανθρώπους σκοτώνει ο παίκτης ως Corvo (High Chaos), τόσο αυξάνεται ο αριθμός των αρουραίων και των Weepers στην πόλη.",
            "Η πανώλη αποκαλύπτεται ότι εισήχθη σκόπιμα στην πόλη από τον Spymaster Hiram Burrows για να αφανίσει τις κατώτερες κοινωνικές τάξεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Dishonored",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "stealth", "bethesda"]
    },
    # 169
    {
        "id": "gaming_med_169",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Silent Hill 3», ποια είναι η πραγματική ταυτότητα και το αρχικό όνομα της πρωταγωνίστριας Heather Mason;",
        "answers": ["Cheryl Mason", "Mary Shepherd", "Alessa Gillespie", "Maria"],
        "correctAnswerIndex": 0,
        "explanation": "Η Heather είναι στην πραγματικότητα η μετενσάρκωση της Cheryl Mason και της Alessa Gillespie, υιοθετημένη από τον Harry Mason μετά το πρώτο παιχνίδι.",
        "funFacts": [
            "Ο Harry Mason άλλαξε το όνομά της από Cheryl σε Heather και έβαψε τα μαλλιά της ξανθά για να την κρύψει από τη λατρεία του Silent Hill.",
            "Το Silent Hill 3 αποτελεί άμεση συνέχεια της ιστορίας του αρχικού Silent Hill του 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_3",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "horror", "silent-hill"]
    },
    # 170
    {
        "id": "gaming_med_170",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Warcraft III», ποιο ισχυρό δαιμονικό τεχνούργημα κατανάλωσε ο Illidan Stormrage για να αποκτήσει τη δαιμονική του μορφή;",
        "answers": ["Το Μάτι του Sargeras", "Το Κρανίο του Gul'dan", "Το Σκήπτρο του Sargeras", "Το Frostmourne"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Illidan κατανάλωσε τις ενέργειες από το Κρανίο του Gul'dan (Skull of Gul'dan) στο Felwood, αποκτώντας τεράστια δαιμονικά κέρατα και φτερά.",
        "funFacts": [
            "Η πράξη του Illidan έσωσε τα δάση του Felwood από τη διαφθορά της Burning Legion, αλλά οδήγησε στην εξορία του από τον αδελφό του, Malfurion.",
            "Αργότερα, στο expansion The Burning Crusade του World of Warcraft, το Skull of Gul'dan είναι ένα από τα πιο περιζήτητα trinkets από το Black Temple."
        ],
        "source": "https://en.wikipedia.org/wiki/Illidan_Stormrage",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rts", "warcraft"]
    },
    # 171
    {
        "id": "gaming_med_171",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Elden Ring», ποια μυστηριώδης τετράχειρη μάγισσα δίνει στον πρωταγωνιστή το κουδούνι Spirit Calling Bell στην εκκλησία Church of Elleh;",
        "answers": ["Melina", "Fia", "Ranni", "Malenia"],
        "correctAnswerIndex": 2,
        "explanation": "Η μάγισσα Ranni (παρουσιαζόμενη αρχικά με το ψευδώνυμο Renna) συναντά τον παίκτη στην εκκλησία Elleh και του χαρίζει το Spirit Calling Bell.",
        "funFacts": [
            "Το questline της Ranni είναι ένα από τα μεγαλύτερα στο παιχνίδι και οδηγεί σε ένα από τα πιο δημοφιλή φινάλε, το «Age of the Stars».",
            "Το πραγματικό της σώμα πέθανε κατά τη «Night of the Black Knives» και η ψυχή της κατοικεί σε μια τεχνητή κούκλα φτιαγμένη κατ' εικόνα της μέντοράς της."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "fromsoftware"]
    },
    # 172
    {
        "id": "gaming_med_172",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο αρχικό «Dark Souls», ποιος ηγεμόνας θυσίασε τον εαυτό του για να παρατείνει την Age of Fire και αποτελεί το τελικό boss του παιχνιδιού;",
        "answers": ["Vendrick", "Manus, Father of the Abyss", "Soul of Cinder", "Gwyn, Lord of Cinder"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Lord Gwyn συνέδεσε την ψυχή του με τη First Flame και μετατράπηκε στο εξασθενημένο Lord of Cinder στο Kiln of the First Flame.",
        "funFacts": [
            "Η μουσική επένδυση της μάχης του Gwyn αποτελείται αποκλειστικά από μια μελαγχολική μελωδία πιάνου χωρίς καθόλου μαύρα πλήκτρα.",
            "Σε αντίθεση με τα περισσότερα μεγάλα bosses της σειράς, ο Gwyn μπορεί να εξουδετερωθεί με την τεχνική του parry."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "dark-souls", "fromsoftware"]
    },
    # 173
    {
        "id": "gaming_med_173",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο αρχικό «Dead Space» (2008), ποιο είναι το όνομα του τεράστιου εξορυκτικού σκάφους (Planet Cracker) όπου εκτυλίσσεται ο εφιάλτης του Isaac Clarke;",
        "answers": ["USG Ishimura", "USG Kellion", "USG O'Bannon", "USG Valor"],
        "correctAnswerIndex": 0,
        "explanation": "Το USG Ishimura ήταν το πρώτο και μεγαλύτερο πλοίο εξόρυξης πλανητών, το οποίο μολύνθηκε από τα θανατηφόρα Necromorphs.",
        "funFacts": [
            "Το USG Kellion ήταν το μικρό σκάφος συντήρησης με το οποίο έφτασε ο Isaac Clarke στο Ishimura για την αποστολή διάσωσης.",
            "Τα πρώτα γράμματα των τίτλων των 12 κεφαλαίων του αρχικού Dead Space σχηματίζουν την ακροστιχίδα «N-I-C-O-L-E-I-S-D-E-A-D»."
        ],
        "source": "https://en.wikipedia.org/wiki/Dead_Space_(2008_video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "horror", "sci-fi"]
    },
    # 174
    {
        "id": "gaming_med_174",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Metal Gear Solid» (1998) για το PlayStation, ποια ήταν η ραδιοσυχνότητα του Codec για να επικοινωνήσει ο Snake με τη Meryl;",
        "answers": ["141.12", "140.15", "140.85", "140.96"],
        "correctAnswerIndex": 1,
        "explanation": "Η συχνότητα της Meryl ήταν 140.15. Για να τη βρει ο παίκτης, έπρεπε να κοιτάξει το πίσω μέρος της πραγματικής φυσικής θήκης του CD του παιχνιδιού.",
        "funFacts": [
            "Ο συνταγματάρχης Campbell έλεγε στον Snake να κοιτάξει «το πίσω μέρος του κουτιού του CD», μπερδεύοντας πολλούς παίκτες που έψαχναν μέσα στο παιχνίδι.",
            "Αυτός ο έξυπνος μηχανισμός 4ου τοίχου σχεδιάστηκε από τον Hideo Kojima τόσο ως easter egg όσο και ως μέτρο κατά της πειρατείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_(1998_video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "stealth", "playstation"]
    },
    # 175
    {
        "id": "gaming_med_175",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο βιντεοπαιχνίδι «Batman: Arkham City», ποιο μεταλλαξιογόνο δηλητήριο έχει μολύνει θανάσιμα το αίμα του Joker και του Batman;",
        "answers": ["Venom", "Fear Toxin", "Titan", "Joker Venom"],
        "correctAnswerIndex": 2,
        "explanation": "Το Titan ήταν μια υπερ-συμπυκνωμένη παραλλαγή του Venom που χρησιμοποίησε ο Joker στο Arkham Asylum, προκαλώντας του όμως ανίατη τοξική δηλητηρίαση.",
        "funFacts": [
            "Ο Joker μολύνει σκόπιμα τον Batman με το δηλητηριασμένο αίμα του για να τον αναγκάσει να αναζητήσει το αντίδοτο από τον Mr. Freeze.",
            "Η ασθένεια του Joker και η απελπισμένη αναζήτηση θεραπείας αποτελούν τον κεντρικό κινητήριο μοχλό της πλοκής του Arkham City."
        ],
        "source": "https://en.wikipedia.org/wiki/Batman:_Arkham_City",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action", "batman"]
    },
    # 176
    {
        "id": "gaming_med_176",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο roguelike παιχνίδι «Hades» της Supergiant Games, ποιος πιστός τρικέφαλος σκύλος φρουρεί την έξοδο από το Σπίτι του Άδη;",
        "answers": ["Όρθρος", "Χάρων", "Λερναία Ύδρα", "Κέρβερος"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Κέρβερος κοιμάται στο House of Hades και ο Zagreus μπορεί να τον χαϊδέψει ανά πάσα στιγμή, ενώ αργότερα τον συναντά ως εμπόδιο στο Temple of Styx.",
        "funFacts": [
            "Στο Temple of Styx, ο Zagreus δεν πολεμά τον Κέρβερο αλλά του προσφέρει μια λαχταριστή λιχουδιά (Satyr Sack) για να τον αφήσει να περάσει ειρηνικά.",
            "Υπάρχει ειδικό επίτευγμα (achievement) στο παιχνίδι για το αν χαϊδέψεις τον Κέρβερο τουλάχιστον 10 φορές."
        ],
        "source": "https://en.wikipedia.org/wiki/Hades_(video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "roguelike", "indie"]
    },
    # 177
    {
        "id": "gaming_med_177",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο ανεξάρτητο RPG «Undertale», ποιος είναι ο ενθουσιώδης σκελετός αδελφός του Sans που λατρεύει τα μακαρόνια και θέλει να μπει στη Βασιλική Φρουρά;",
        "answers": ["Papyrus", "Undyne", "Asgore", "Toriel"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Papyrus είναι ο καλοκάρδος σκελετός που στήνει γρίφους στο Snowdin, μαγειρεύει μακαρόνια και ονειρεύεται να γίνει μέλος της Royal Guard.",
        "funFacts": [
            "Το όνομα και οι διάλογοι του Papyrus γράφονται στην ομώνυμη γραμματοσειρά Papyrus, ακριβώς όπως και του αδελφού του Sans στην Comic Sans.",
            "Εάν ο παίκτης επιλέξει την οδό της ειρήνης (Pacifist Run), μπορεί να βγει ραντεβού με τον Papyrus στο σπίτι του."
        ],
        "source": "https://en.wikipedia.org/wiki/Undertale",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "indie", "rpg"]
    },
    # 178
    {
        "id": "gaming_med_178",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Hollow Knight», ποια είναι η ευκίνητη προστάτιδα του Hallownest που πολεμά με βελόνα και κλωστή και είναι η πρωταγωνίστρια του «Silksong»;",
        "answers": ["Cloth", "Hornet", "Iselda", "Myla"],
        "correctAnswerIndex": 1,
        "explanation": "Η Hornet είναι η πριγκίπισσα-προστάτιδα του Hallownest, κόρη του Pale King και της Herrah the Beast, οπλισμένη με μια κοφτερή βελόνα.",
        "funFacts": [
            "Η διάσημη ιαχή της Hornet κατά τη μάχη («Shaw!» και «Git gud!» όπως την άκουσαν χιουμοριστικά οι παίκτες) έγινε viral meme στην κοινότητα.",
            "Το sequel Hollow Knight: Silksong ανακοινώθηκε αρχικά ως downloadable content (DLC) αλλά επεκτάθηκε σε αυτόνομο πλήρες παιχνίδι."
        ],
        "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "metroidvania", "indie"]
    },
    # 179
    {
        "id": "gaming_med_179",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο platformer παιχνίδι «Celeste», πώς ονομάζεται συνήθως από την κοινότητα και το παιχνίδι η σκοτεινή εκδοχή της Madeline που ενσαρκώνει τις ανασφάλειές της;",
        "answers": ["Shadow Madeline", "Part of Me", "Badeline", "Dark Mirror"],
        "correctAnswerIndex": 2,
        "explanation": "Αν και στους διαλόγους αναφέρεται συχνά ως «Part of You», η σκοτεινή πλευρά της Madeline ονομάζεται επισήμως Badeline στα αρχεία και τους συντελεστές.",
        "funFacts": [
            "Στο τέλος της ιστορίας, η Madeline μαθαίνει να μην πολεμά την Badeline αλλά να συνεργάζεται μαζί της, αποκτώντας τη δυνατότητα διπλού dash.",
            "Το Celeste απέσπασε διθυραμβικές κριτικές για τον ευαίσθητο και ρεαλιστικό τρόπο με τον οποίο απεικόνισε το άγχος και την κατάθλιψη."
        ],
        "source": "https://en.wikipedia.org/wiki/Celeste_(video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "platformer", "indie"]
    },
    # 180
    {
        "id": "gaming_med_180",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο ατμοσφαιρικό παιχνίδι «Bloodborne» της FromSoftware, ποια αρχαία βικτοριανή/γοτθική πόλη αποτελεί το κύριο σκηνικό της ιστορίας;",
        "answers": ["Cainhurst", "Lothric", "Byrgenwerth", "Yharnam"],
        "correctAnswerIndex": 3,
        "explanation": "Η πόλη Yharnam είναι γνωστή για τη θαυματουργή θεραπεία αίματος, η οποία όμως προκάλεσε την εξάπλωση μιας μάστιγας που μετατρέπει τους κατοίκους σε κτήνη.",
        "funFacts": [
            "Η αρχιτεκτονική του Yharnam είναι εμπνευσμένη από ιστορικές πόλεις της Κεντρικής Ευρώπης, κυρίως την Πράγα και το Λονδίνο της βικτοριανής εποχής.",
            "Το παιχνίδι ξεκινά τη νύχτα του κυνηγιού (The Hunt), όπου οι Κυνηγοί αναλαμβάνουν να καθαρίσουν τους δρόμους από τα τέρατα."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodborne",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fromsoftware", "playstation"]
    },
    # 181
    {
        "id": "gaming_med_181",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «The Witcher 3: Wild Hunt», ποιος είναι ο πανίσχυρος αυτοκράτορας του Nilfgaard και βιολογικός πατέρας της Ciri;",
        "answers": ["Emhyr var Emreis", "Radovid V", "Foltest", "Henselt"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Emhyr var Emreis, γνωστός και ως «Η Λευκή Φλόγα που Χορεύει στους Τύμβους των Εχθρών του», αναθέτει στον Geralt να βρει τη χαμένη του κόρη Ciri.",
        "funFacts": [
            "Στην αγγλική έκδοση του The Witcher 3, τη φωνή του αυτοκράτορα Emhyr δανείζει ο διάσημος ηθοποιός Charles Dance (γνωστός ως Tywin Lannister).",
            "Ανάλογα με τις επιλογές του παίκτη στην ιστορία, η Ciri μπορεί στο τέλος να διαδεχθεί τον πατέρα της στον θρόνο της αυτοκρατορίας του Nilfgaard."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "witcher"]
    },
    # 182
    {
        "id": "gaming_med_182",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Red Dead Redemption 2», πώς ονομάζεται η συμμορία παρανόμων της οποίας ηγετικό στέλεχος είναι ο Arthur Morgan;",
        "answers": ["O'Driscoll Boys", "Van der Linde", "Del Lobo Gang", "Murfree Brood"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Arthur Morgan ανήκει στη συμμορία Van der Linde, η οποία ιδρύθηκε και διοικείται από τον χαρισματικό αλλά ασταθή Dutch van der Linde.",
        "funFacts": [
            "Ο Dutch van der Linde και ο Hosea Matthews μεγάλωσαν τον Arthur Morgan σχεδόν σαν γιο τους από την ηλικία των 15 ετών.",
            "Η περίφημη φράση του Dutch «I have a plan» («Έχω ένα σχέδιο») έγινε ένα από τα πιο αναγνωρίσιμα memes στη σύγχρονη κοινότητα του gaming."
        ],
        "source": "https://en.wikipedia.org/wiki/Red_Dead_Redemption_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rockstar", "open-world"]
    },
    # 183
    {
        "id": "gaming_med_183",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «God of War» (2018), ποιο γιγάντιο φίδι της σκανδιναβικής μυθολογίας κοιμάται στη Λίμνη των Εννέα και γίνεται σύμμαχος του Kratos;",
        "answers": ["Níðhögg", "Fenrir", "Jörmungandr", "Surtr"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Jörmungandr, το Φίδι του Κόσμου (World Serpent), είναι τόσο τεράστιο που τυλίγεται γύρω από ολόκληρο το Midgard και μιλάει μια αρχαία ξεχασμένη γλώσσα.",
        "funFacts": [
            "Όταν ο Kratos και ο Atreus ξυπνούν για πρώτη φορά τον Jörmungandr, η στάθμη του νερού στη λίμνη πέφτει αποκαλύπτοντας νέες περιοχές.",
            "Σύμφωνα με τη μυθολογία, στη μάχη του Ragnarök ο Jörmungandr χτυπιέται τόσο δυνατά από τον Thor που ταξιδεύει πίσω στον χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_(2018_video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "playstation", "action"]
    },
    # 184
    {
        "id": "gaming_med_184",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο σύμπαν του «Horizon Zero Dawn», ποια υπολειτουργία (sub-function) του συστήματος GAIA ήταν υπεύθυνη για τον σχεδιασμό και την παραγωγή των μηχανών;",
        "answers": ["HADES", "MINERVA", "AETHER", "HEPHAESTUS"],
        "correctAnswerIndex": 3,
        "explanation": "Ο HEPHAESTUS ήταν υπεύθυνος για τα αυτόνομα εργοστάσια (Cauldrons) που σχεδίαζαν και παρήγαγαν τις ρομποτικές μηχανές για την αποκατάσταση της βιόσφαιρας.",
        "funFacts": [
            "Όταν τα υποσυστήματα απελευθερώθηκαν από το GAIA, ο HEPHAESTUS θεώρησε τους ανθρώπους απειλή και άρχισε να κατασκευάζει επιθετικές μηχανές μάχης.",
            "Όλα τα υποσυστήματα του Project Zero Dawn πήραν τα ονόματά τους από θεότητες της αρχαίας ελληνικής μυθολογίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Horizon_Zero_Dawn",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "playstation"]
    },
    # 185
    {
        "id": "gaming_med_185",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο battle royale παιχνίδι «Apex Legends», ποια είναι η απόλυτη ικανότητα (Ultimate Ability) της Wraith που συνδέει δύο σημεία στον χάρτη;",
        "answers": ["Dimensional Rift", "Into the Void", "Voices from the Void", "Void Walker"],
        "correctAnswerIndex": 0,
        "explanation": "Το Dimensional Rift επιτρέπει στη Wraith να ανοίγει δύο πύλες (portals) για 45 δευτερόλεπτα, επιτρέποντας σε όλη την ομάδα της να ταξιδέψει με ασφάλεια.",
        "funFacts": [
            "Κατά τη διάρκεια του τρεξίματος για την τοποθέτηση της πύλης, η ταχύτητα κίνησης της Wraith αυξάνεται σημαντικά.",
            "Η παθητική ικανότητα της Wraith, Voices from the Void, την προειδοποιεί φωνητικά όταν κάποιος εχθρός τη στοχεύει με όπλο."
        ],
        "source": "https://en.wikipedia.org/wiki/Apex_Legends",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "battle-royale", "fps"]
    },
    # 186
    {
        "id": "gaming_med_186",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «League of Legends», ποιο ουδέτερο τέρας κατοικεί στη φωλιά του Baron πριν το 20ό λεπτό του αγώνα στο Summoner's Rift;",
        "answers": ["Scuttle Crab", "Rift Herald", "Elder Dragon", "Cloud Drake"],
        "correctAnswerIndex": 1,
        "explanation": "Το Rift Herald (γνωστό και ως Shelly) εμφανίζεται στη φωλιά του Baron και όταν εξοντωθεί, μπορεί να κληθεί από την ομάδα για να γκρεμίσει εχθρικούς πύργους.",
        "funFacts": [
            "Το Rift Herald χορεύει αν η ομάδα που το επικαλέστηκε καταστρέψει το αντίπαλο Nexus όσο αυτό είναι ζωντανό στον χάρτη.",
            "Στο 20:00 του αγώνα, το Rift Herald αποχωρεί αναγκαστικά από το pit για να δώσει τη θέση του στον Baron Nashor."
        ],
        "source": "https://en.wikipedia.org/wiki/League_of_Legends",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "moba", "esports"]
    },
    # 187
    {
        "id": "gaming_med_187",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Dota 2», ποιο εμβληματικό αντικείμενο προσφέρει ενεργή ανοσία σε μαγικά ξόρκια (Spell Immunity / Debuff Immunity) κατά τη διάρκεια των ομαδικών μαχών;",
        "answers": ["Monkey King Bar", "Butterfly", "Black King Bar", "Daedalus"],
        "correctAnswerIndex": 2,
        "explanation": "Το Black King Bar (BKB) είναι ένα από τα πιο κρίσιμα αντικείμενα στο Dota 2, καθώς προστατεύει τον ήρωα από τα περισσότερα disables και μαγικά ξόρκια.",
        "funFacts": [
            "Κάθε φορά που χρησιμοποιείται το BKB, η διάρκεια της προστασίας του μειώνεται σταδιακά (από 9 δευτερόλεπτα σε τουλάχιστον 6).",
            "Το αντικείμενο πήρε το όνομά του από μια παλιά συντεχνία (clan) του Defense of the Ancients στο Warcraft III."
        ],
        "source": "https://en.wikipedia.org/wiki/Dota_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "moba", "esports"]
    },
    # 188
    {
        "id": "gaming_med_188",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο κλασικό shooter «Team Fortress 2», ποια κατηγορία χαρακτήρα (class) έχει την ικανότητα να μεταμφιέζεται σε μέλος της αντίπαλης ομάδας;",
        "answers": ["Scout", "Sniper", "Engineer", "Spy"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Spy προέρχεται από τη Γαλλία και διαθέτει ένα Disguise Kit που του επιτρέπει να παίρνει τη μορφή οποιουδήποτε μέλους της αντίπαλης ομάδας.",
        "funFacts": [
            "Εκτός από τη μεταμφίεση, ο Spy διαθέτει ρολόι αορατότητας και ένα μαχαίρι με το οποίο εκτελεί άμεσο backstab (πισώπλατο χτύπημα).",
            "Η Valve κυκλοφόρησε το διάσημο animated βίντεο «Meet the Spy» το 2009, το οποίο συγκέντρωσε δεκάδες εκατομμύρια προβολές."
        ],
        "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "valve"]
    },
    # 189
    {
        "id": "gaming_med_189",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στους επίσημους ανταγωνιστικούς αγώνες του «Counter-Strike: Global Offensive», πόσα δευτερόλεπτα διαρκεί ο χρονοδιακόπτης της βόμβας (C4) μετά την τοποθέτησή της;",
        "answers": ["40 δευτερόλεπτα", "35 δευτερόλεπτα", "45 δευτερόλεπτα", "30 δευτερόλεπτα"],
        "correctAnswerIndex": 0,
        "explanation": "Στους επίσημους αγώνες competitive του CS:GO ο χρονοδιακόπτης της C4 έχει ρυθμιστεί στα 40 δευτερόλεπτα (ενώ ο γύρος διαρκεί 1 λεπτό και 55 δευτερόλεπτα).",
        "funFacts": [
            "Για την απενεργοποίηση της βόμβας (defuse) απαιτούνται 10 δευτερόλεπτα χωρίς kit ή 5 δευτερόλεπτα με Defuse Kit.",
            "Παλαιότερα, στα επαγγελματικά τουρνουά ίσχυε χρονόμετρο 35 δευτερολέπτων πριν η Valve τυποποιήσει τα 40 δευτερόλεπτα για όλους στα τέλη του 2015."
        ],
        "source": "https://en.wikipedia.org/wiki/Counter-Strike:_Global_Offensive",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "esports"]
    },
    # 190
    {
        "id": "gaming_med_190",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «StarCraft II: Legacy of the Void», ποιο είναι το όνομα του αρχαίου τεράστιου πλοίου-κιβωτού των Protoss που λειτουργεί ως ναυαρχίδα του Artanis;",
        "answers": ["Hyperion", "Spear of Adun", "Leviathan", "Gantrithor"],
        "correctAnswerIndex": 1,
        "explanation": "Το Spear of Adun είναι ένα αρχαίο πλοίο-κιβωτός (arkship) που κατασκευάστηκε στη χρυσή εποχή των Protoss και επανενεργοποιήθηκε από τον Artanis.",
        "funFacts": [
            "Μέσα από το Spear of Adun, ο παίκτης μπορεί να ξεκλειδώσει και να αναβαθμίσει υπερόπλα υποστήριξης τροχιάς για τις αποστολές του.",
            "Τα άλλα δύο αδελφά πλοία-κιβωτοί που κατασκευάστηκαν ήταν το Memory of Nezin και το Shield of Aiur, τα οποία είχαν καταστραφεί."
        ],
        "source": "https://en.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rts", "starcraft"]
    },
    # 191
    {
        "id": "gaming_med_191",
        "category": "gaming",
        "difficulty": 3,
        "question": "Ποιο expansion του «World of Warcraft» εισήγαγε στο παιχνίδι την κλάση των Monk και την ανθρωπόμορφη φυλή των Pandaren;",
        "answers": ["Cataclysm", "Warlords of Draenor", "Mists of Pandaria", "Wrath of the Lich King"],
        "correctAnswerIndex": 2,
        "explanation": "Το «Mists of Pandaria» (2012) ήταν το 4ο expansion του World of Warcraft και πρόσθεσε την ήπειρο της Pandaria, την κλάση Monk και τους Pandaren.",
        "funFacts": [
            "Οι Pandaren ήταν αρχικά ένα πρωταπριλιάτικο αστείο της Blizzard το 2002 για το Warcraft III πριν προστεθούν κανονικά στο σύμπαν.",
            "Οι Pandaren ήταν η πρώτη ουδέτερη φυλή που επέτρεπε στον παίκτη να επιλέξει αν θα ενταχθεί στην Alliance ή στο Horde."
        ],
        "source": "https://en.wikipedia.org/wiki/World_of_Warcraft:_Mists_of_Pandaria",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "mmorpg", "warcraft"]
    },
    # 192
    {
        "id": "gaming_med_192",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στη σειρά «Diablo», ποιος Αρχάγγελος της Δικαιοσύνης βοήθησε τους θνητούς ενάντια στους Prime Evils και κατέστρεψε το διεφθαρμένο Worldstone;",
        "answers": ["Imperius", "Auriel", "Malthael", "Tyrael"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Tyrael είναι ο Αρχάγγελος της Δικαιοσύνης που πέταξε το ξίφος του, El'druin, στο Worldstone στο τέλος του Diablo II: Lord of Destruction.",
        "funFacts": [
            "Στο Diablo III, ο Tyrael απαρνείται τα φτερά και την αθανασία του για να γίνει θνητός, διαμαρτυρόμενος για την απραξία των άλλων αγγέλων.",
            "Η καταστροφή του Worldstone από τον Tyrael ήταν απαραίτητη επειδή ο Baal το είχε διαφθείρει ανεπανόρθωτα."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_(series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "diablo"]
    },
    # 193
    {
        "id": "gaming_med_193",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Final Fantasy VII», ποια πανίσχυρη πολυεθνική εταιρεία ελέγχει τη μητρόπολη Midgar και απομυζά την ενέργεια Mako από τον πλανήτη;",
        "answers": ["Shinra Electric Power Company", "Avalanche Industries", "Junon Megacorp", "SOLDIER Global"],
        "correctAnswerIndex": 0,
        "explanation": "Η Shinra Electric Power Company είναι η σκοτεινή εταιρεία που λειτουργεί ως de facto κυβέρνηση και αποστραγγίζει τη ζωτική ενέργεια (Lifestream) του πλανήτη.",
        "funFacts": [
            "Ο Cloud Strife ξεκινά το παιχνίδι ως μισθοφόρος που δουλεύει για την οικολογική αντιστασιακή οργάνωση AVALANCHE ενάντια στη Shinra.",
            "Η Shinra διαθέτει δικό της στρατό και επίλεκτη μονάδα γενετικά ενισχυμένων πολεμιστών με την ονομασία SOLDIER."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VII",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "final-fantasy"]
    },
    # 194
    {
        "id": "gaming_med_194",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο JRPG «Persona 5», ποιο είναι το όνομα της αρχικής Persona που αφυπνίζει ο πρωταγωνιστής (Joker);",
        "answers": ["Captain Kidd", "Arsène", "Carmen", "Zorro"],
        "correctAnswerIndex": 1,
        "explanation": "Η αρχική Persona του Joker είναι ο Arsène, εμπνευσμένος από τον διάσημο φανταστικό αριστοκράτη-λωποδύτη Arsène Lupin του Maurice Leblanc.",
        "funFacts": [
            "Όλες οι αρχικές Personas των Phantom Thieves είναι εμπνευσμένες από διάσημους ιστορικούς ή λογοτεχνικούς παρανόμους και επαναστάτες.",
            "Ο Arsène εμφανίζεται με ψηλό καπέλο, κόκκινο κουστούμι και τεράστια μαύρα φτερά."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_5",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "jrpg", "playstation"]
    },
    # 195
    {
        "id": "gaming_med_195",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «NieR: Automata», ποιος ανδροειδής ανιχνευτής (Scanner model) συνοδεύει και υποστηρίζει την πρωταγωνίστρια 2B στις αποστολές της στη Γη;",
        "answers": ["YoRHa No. 2 Model A (A2)", "YoRHa No. 4 Model B", "9S (YoRHa No. 9 Model S)", "YoRHa No. 8 Model S"],
        "correctAnswerIndex": 2,
        "explanation": "Ο 9S (YoRHa No. 9 Model S) είναι ο αναγνωριστικός ανδροειδής που ειδικεύεται στην παραβίαση συστημάτων (hacking) και συνοδεύει τη μάχιμη 2B.",
        "funFacts": [
            "Στο δεύτερο playthrough (Route B) του NieR: Automata, ο παίκτης ελέγχει απευθείας τον 9S, ξεκλειδώνοντας τον μηχανισμό hacking.",
            "Το NieR: Automata σκηνοθετήθηκε από τον Yoko Taro και διαθέτει 26 διαφορετικά φινάλε (από το A έως το Z)."
        ],
        "source": "https://en.wikipedia.org/wiki/Nier:_Automata",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "square-enix"]
    },
    # 196
    {
        "id": "gaming_med_196",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Monster Hunter: World», ποιο τεράστιο Elder Dragon καλυμμένο με μυτερά αγκάθια αποτελεί το εμβληματικό τέρας του εξωφύλλου;",
        "answers": ["Velkhana", "Kushala Daora", "Teostra", "Nergigante"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Nergigante είναι ο «Extinction Dragon», ένα πανίσχυρο τέρας που τρέφεται με άλλα Elder Dragons και έχει την ικανότητα να αναγεννά τα αγκάθια του.",
        "funFacts": [
            "Τα αγκάθια του Nergigante ξεκινούν λευκά και ευάλωτα, αλλά αν ο παίκτης δεν τα σπάσει έγκαιρα, μαυρίζουν και γίνονται σχεδόν αδιαπέραστα.",
            "Το Monster Hunter: World έγινε το παιχνίδι με τις περισσότερες πωλήσεις στην ιστορία της Capcom, ξεπερνώντας τα 20 εκατομμύρια αντίτυπα."
        ],
        "source": "https://en.wikipedia.org/wiki/Monster_Hunter:_World",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "capcom"]
    },
    # 197
    {
        "id": "gaming_med_197",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Dragon Age: Inquisition», ποιος ξωτικός μάγος και μελετητής του Fade αποκαλύπτεται στο τέλος ότι είναι η αρχαία θεότητα Fen'Harel (Dread Wolf);",
        "answers": ["Solas", "Dorian Pavus", "Varric Tethras", "Cullen Rutherford"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Solas είναι ένας φαινομενικά απλός αποστάτης ξωτικός μάγος που βοηθά την Ιερά Εξέταση, αλλά αποκαλύπτεται ως ο αρχαίος Fen'Harel.",
        "funFacts": [
            "Η λέξη «Solas» στην αρχαία γλώσσα των ξωτικών (Elvhenan) σημαίνει «υπερηφάνεια».",
            "Η ιστορία του Solas και το σχέδιό του να καταστρέψει το Veil αποτελούν το κεντρικό θέμα του sequel Dragon Age: The Veilguard."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon_Age:_Inquisition",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "bioware"]
    },
    # 198
    {
        "id": "gaming_med_198",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Sekiro: Shadows Die Twice», ποιος είναι ο θετός πατέρας του Wolf, ο οποίος τον εκπαίδευσε στους κώδικες των Shinobi;",
        "answers": ["Isshin Ashina", "Owl (Ukonzaemon Usui)", "Genichiro Ashina", "Ο Γλύπτης (Sculptor)"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Owl (Ukonzaemon Usui) είναι ο πονηρός και πανύψηλος shinobi που βρήκε τον νεαρό Wolf σε ένα πεδίο μάχης και τον ανέθρεψε ως γιο και εκτελεστή.",
        "funFacts": [
            "Στο κρίσιμο σημείο της ιστορίας στην κορυφή του κάστρου Ashina, ο παίκτης καλείται να επιλέξει αν θα υπακούσει τον Owl ή τον νεαρό Άρχοντα Kuro.",
            "Αν ο παίκτης επιλέξει να υπακούσει τον Owl, ξεκλειδώνει το σκοτεινό τέλος «Shura» όπου ο Wolf εξοντώνει τους πάντες."
        ],
        "source": "https://en.wikipedia.org/wiki/Sekiro:_Shadows_Die_Twice",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action", "fromsoftware"]
    },
    # 199
    {
        "id": "gaming_med_199",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο πειρατικό παιχνίδι «Sea of Thieves», ποιος διαβόητος σκελετός καπετάνιος και άρχοντας της φωτιάς αποτελεί έναν από τους κύριους εχθρούς των θαλασσών;",
        "answers": ["Captain Briggsy", "Gold Hoarder", "Captain Flameheart", "Captain Graymarrow"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Captain Flameheart είναι ο πανίσχυρος πειρατής σκελετός του οποίου το φλεγόμενο κεφάλι εμφανιζόταν συχνά στους ουρανούς καλώντας στόλους φαντασμάτων.",
        "funFacts": [
            "Ο Flameheart είναι ο ηγέτης της φατρίας Reaper's Bones, η οποία ενθαρρύνει τις συγκρούσεις PvP μεταξύ των πληρωμάτων.",
            "Οι παίκτες μπορούν να πολεμήσουν τη ναυαρχίδα του, το Burning Blade, σε επικές ναυμαχίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Sea_of_Thieves",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "multiplayer", "pirates"]
    },
    # 200
    {
        "id": "gaming_med_200",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο παιχνίδι επιβίωσης «Subnautica», ποιο γιγάντιο αρπακτικό Leviathan με κόκκινα-λευκά χρώματα και τέσσερις δαγκάνες τρομοκρατεί τους παίκτες κοντά στο Aurora;",
        "answers": ["Ghost Leviathan", "Sea Dragon Leviathan", "Reefback Leviathan", "Reaper Leviathan"],
        "correctAnswerIndex": 3,
        "explanation": "Το Reaper Leviathan έχει μήκος περίπου 55 μέτρα και επιτίθεται αιφνιδιαστικά στους παίκτες και τα υποβρύχιά τους χρησιμοποιώντας ηχοεντοπισμό.",
        "funFacts": [
            "Σύμφωνα με το lore του Subnautica, αν ακούσεις το ουρλιαχτό του Reaper Leviathan, σημαίνει ότι ήδη σε έχει εντοπίσει.",
            "Το Reaper Leviathan μπορεί να αρπάξει το υποβρύχιο Seamoth του παίκτη και να το συνθλίψει μέσα σε λίγα δευτερόλεπτα."
        ],
        "source": "https://en.wikipedia.org/wiki/Subnautica",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "survival", "indie"]
    },
    # 201
    {
        "id": "gaming_med_201",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο παιχνίδι στρατηγικής «Civilization VI», ποια ιστορική Σπαρτιάτισσα βασίλισσα αποτελεί μία από τις εναλλακτικές ηγέτιδες του ελληνικού πολιτισμού;",
        "answers": ["Γοργώ", "Ολυμπιάδα", "Αρτεμισία", "Κλεοπάτρα"],
        "correctAnswerIndex": 0,
        "explanation": "Η Γοργώ (Gorgo), βασίλισσα της Σπάρτης και σύζυγος του Λεωνίδα, είναι ηγέτιδα της Ελλάδας στο Civ VI με έμφαση στον πολιτισμό μέσω στρατιωτικών νικών.",
        "funFacts": [
            "Η ειδική της ικανότητα «With Your Shield or On It» δίνει Culture κάθε φορά που μια ελληνική μονάδα νικά μια εχθρική μονάδα.",
            "Ο άλλος ηγέτης της Ελλάδας στο βασικό Civilization VI είναι ο Αθηναίος Περικλής."
        ],
        "source": "https://en.wikipedia.org/wiki/Civilization_VI",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "strategy", "history"]
    },
    # 202
    {
        "id": "gaming_med_202",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο κλασικό παιχνίδι στρατηγικής «Age of Empires II», ποια είναι η μοναδική στρατιωτική μονάδα του Κάστρου (Unique Unit) των Βυζαντινών;",
        "answers": ["Βαράγγος Φρουρός", "Κατάφρακτος", "Στρατιώτης του Τάγματος", "Παλαντίνος"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Κατάφρακτος (Cataphract) είναι η μοναδική μονάδα του βυζαντινού πολιτισμού στο AoE II, ένα βαριά θωρακισμένο ιππικό εξαιρετικά αποτελεσματικό ενάντια σε πεζικό.",
        "funFacts": [
            "Με την αναβάθμιση Logistica στο Imperial Age, οι Κατάφρακτοι προκαλούν ζημιά περιοχής (trample damage) σε όλες τις γύρω μονάδες πεζικού.",
            "Οι Βυζαντινοί στο παιχνίδι διαθέτουν επίσης φθηνότερα κτίρια και φθηνότερες αμυντικές μονάδες trash units (spearmen, skirmishers, camels)."
        ],
        "source": "https://en.wikipedia.org/wiki/Age_of_Empires_II",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rts", "history"]
    },
    # 203
    {
        "id": "gaming_med_203",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο συνεργατικό παιχνίδι ληστειών «Payday 2», ποιος είναι ο μυστηριώδης εγκέφαλος και συντονιστής που καθοδηγεί τη συμμορία μέσω ασυρμάτου;",
        "answers": ["Dallas", "Wolf", "Bain", "Hoxton"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Bain είναι ο ιδρυτής του δικτύου Crime.net και ο επιχειρησιακός εγκέφαλος που βρίσκει συμβόλαια και δίνει οδηγίες στους ληστές κατά τη διάρκεια των αποστολών.",
        "funFacts": [
            "Ο Bain είναι επίσης ο συγγραφέας του «The Guide of Bain», ενός μυστικού βιβλίου που περιέχει κώδικες και θεωρίες συνωμοσίας.",
            "Στο τέλος της ιστορίας του Payday 2, η πραγματική ταυτότητα και η μοίρα του Bain συνδέονται με ένα βαθύ υπερφυσικό μυστήριο."
        ],
        "source": "https://en.wikipedia.org/wiki/Payday_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "coop"]
    },
    # 204
    {
        "id": "gaming_med_204",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο τακτικό shooter «Tom Clancy's Rainbow Six Siege», ποιος Βρετανός αμυντικός χειριστής (operator) του SAS τοποθετεί συσκευές παρεμβολής σημάτων (Signal Disruptors);",
        "answers": ["Smoke", "Thatcher", "Sledge", "Mute"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Mute (Mark Chandar) χρησιμοποιεί Signal Disruptors για να μπλοκάρει τις ηλεκτρονικές συσκευές επικοινωνίας, τα drones και τα τηλεχειριζόμενα εκρηκτικά των επιτιθέμενων.",
        "funFacts": [
            "Ο Mute έγινε δεκτός στο Πανεπιστήμιο του Cambridge σε ηλικία μόλις 14 ετών λόγω της ιδιοφυΐας του στα ηλεκτρονικά.",
            "Οι συσκευές του Mute μπορούν να αποτρέψουν το άνοιγμα ενισχυμένων τοίχων από το Exothermic Charge της Thermite."
        ],
        "source": "https://en.wikipedia.org/wiki/Tom_Clancy%27s_Rainbow_Six_Siege",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "tactical-shooter", "esports"]
    },
    # 205
    {
        "id": "gaming_med_205",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο sandbox παιχνίδι «Terraria», ποιο τερατώδες boss του Κάτω Κόσμου (Underworld) πρέπει να νικηθεί για να μεταβεί ο κόσμος στο μόνιμο Hardmode;",
        "answers": ["Wall of Flesh", "Eye of Cthulhu", "Skeletron", "Moon Lord"],
        "correctAnswerIndex": 0,
        "explanation": "Η νίκη επί του Wall of Flesh στον Κάτω Κόσμο απελευθερώνει τα αρχαία πνεύματα του φωτός και του σκότους, ενεργοποιώντας το Hardmode στο Terraria.",
        "funFacts": [
            "Για να καλέσει ο παίκτης το Wall of Flesh, πρέπει να πετάξει μια κούκλα Guide Voodoo Doll στη λάβα του Underworld, θυσιάζοντας τον Guide.",
            "Το Wall of Flesh καταλαμβάνει ολόκληρο το κατακόρυφο ύψος της οθόνης και κινείται ασταμάτητα προς μία κατεύθυνση πιέζοντας τον παίκτη."
        ],
        "source": "https://en.wikipedia.org/wiki/Terraria",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "sandbox", "indie"]
    },
    # 206
    {
        "id": "gaming_med_206",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Star Wars Jedi: Fallen Order», ποιο είναι το όνομα του μικρού droid που γίνεται πιστός σύντροφος του Cal Kestis;",
        "answers": ["R2-D2", "BD-1", "BB-8", "Chopper"],
        "correctAnswerIndex": 1,
        "explanation": "Το BD-1 είναι ένα μικρό δίποδο droid εξερεύνησης που κάθεται στον ώμο του Cal, παρέχοντάς του ενέσεις θεραπείας (stim canisters) και ξεκλειδώνοντας πόρτες.",
        "funFacts": [
            "Το όνομα BD σημαίνει «Buddy Droid» και σχεδιάστηκε για να θυμίζει κατοικίδιο ζώο στην αλληλεπίδρασή του με τον πρωταγωνιστή.",
            "Πριν συναντήσει τον Cal Kestis, το BD-1 άνηκε στον Jedi Master Eno Cordova, ο οποίος είχε σβήσει προσωρινά τη μνήμη του για λόγους ασφαλείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars_Jedi:_Fallen_Order",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-adventure", "star-wars"]
    },
    # 207
    {
        "id": "gaming_med_207",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο ψυχολογικό θρίλερ «Alan Wake» της Remedy Entertainment, ποια υπερφυσική δύναμη καταλαμβάνει τους κατοίκους και τα αντικείμενα του Bright Falls;",
        "answers": ["The Taken", "The Hiss", "The Dark Presence", "The Black Rock"],
        "correctAnswerIndex": 2,
        "explanation": "Η Σκοτεινή Παρουσία (The Dark Presence) είναι μια αρχαία κακόβουλη οντότητα που κατοικεί στη λίμνη Cauldron Lake και μετατρέπει ανθρώπους σε Taken.",
        "funFacts": [
            "Το φως (από φακούς, φωτοβολίδες και προβολείς) είναι το μοναδικό μέσο που μπορεί να αφαιρέσει την ασπίδα σκότους από τους εχθρούς πριν πυροβοληθούν.",
            "Η ιστορία του Alan Wake συνδέεται άμεσα με το παιχνίδι Control μέσω του Remedy Connected Universe."
        ],
        "source": "https://en.wikipedia.org/wiki/Alan_Wake",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "thriller", "remedy"]
    },
    # 208
    {
        "id": "gaming_med_208",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο παιχνίδι «Control» (2019), πώς ονομάζεται ο παραφυσικός μπρουταλιστικός ουρανοξύστης στη Νέα Υόρκη που στεγάζει τα κεντρικά γραφεία του FBC;",
        "answers": ["The Federal Spire", "The Concrete Tower", "The Oceanview Motel", "The Oldest House"],
        "correctAnswerIndex": 3,
        "explanation": "Το The Oldest House είναι ένας Τόπος Δύναμης (Place of Power) με μεταβαλλόμενη εσωτερική γεωμετρία, ο οποίος παραμένει αόρατος στους απλούς ανθρώπους.",
        "funFacts": [
            "Το Oldest House είναι εμπνευσμένο από το πραγματικό κτίριο 33 Thomas Street στο Μανχάταν, έναν εμβληματικό ουρανοξύστη χωρίς παράθυρα.",
            "Μέσα στο κτίριο απαγορεύονται αυστηρά οι σύγχρονες τεχνολογίες (όπως κινητά τηλέφωνα) επειδή η παραφυσική ενέργεια τείνει να τις καταστρέφει βίαια."
        ],
        "source": "https://en.wikipedia.org/wiki/Control_(video_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-adventure", "remedy"]
    },
    # 209
    {
        "id": "gaming_med_209",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο RPG «Cyberpunk 2077», ποιο είναι το όνομα του θρυλικού ροκ συγκροτήματος του οποίου τραγουδιστής και κιθαρίστας ήταν ο Johnny Silverhand;",
        "answers": ["Samurai", "Tyger Claws", "Lizzy Wizzy", "Maelstrom"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Samurai ήταν το εμβληματικό chrome rock συγκρότημα της Night City με ηγέτες τον Johnny Silverhand και τον Kerry Eurodyne.",
        "funFacts": [
            "Τα αυθεντικά τραγούδια των Samurai στο παιχνίδι γράφτηκαν και εκτελέστηκαν από το σουηδικό punk-rock συγκρότημα Refused.",
            "Το διάσημο λογότυπο των Samurai με τον δαίμονα Onimask κοσμεί το πίσω μέρος του μπουφάν του πρωταγωνιστή V."
        ],
        "source": "https://en.wikipedia.org/wiki/Cyberpunk_2077",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "cyberpunk", "cd-projekt-red"]
    },
    # 210
    {
        "id": "gaming_med_210",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «The Elder Scrolls V: Skyrim», ποιος είναι ο αρχαίος δράκος και ηγέτης των Greybeards που ζει στην απομονωμένη κορυφή του Throat of the World;",
        "answers": ["Alduin", "Paarthurnax", "Odahviing", "Durnehviir"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Paarthurnax είναι ο δράκος αδελφός του Alduin που πρόδωσε τους άλλους δράκους για να διδάξει στους ανθρώπους το Thu'um (Dragon Shouts).",
        "funFacts": [
            "Τη φωνή του Paarthurnax στο Skyrim δανείζει ο Charles Martinet, η θρυλική αυθεντική φωνή του Super Mario.",
            "Η αποστολή των Blades που ζητά από τον Dragonborn να σκοτώσει τον Paarthurnax παραμένει ένα από τα πιο αμφιλεγόμενα ηθικά διλήμματα στο Skyrim."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "skyrim"]
    },
    # 211
    {
        "id": "gaming_med_211",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο tactical RPG «Fire Emblem: Three Houses», ποιος οίκος της Ακαδημίας των Αξιωματικών έχει ως αρχηγό τον Dimitri Alexandre Blaiddyd;",
        "answers": ["Black Eagles", "Golden Deer", "Blue Lions", "Ashen Wolves"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Dimitri είναι ο πρίγκιπας του Holy Kingdom of Faerghus και ο ηγέτης του οίκου Blue Lions (Μπλε Λέοντες) στο Garreg Mach Monastery.",
        "funFacts": [
            "Κάθε οίκος εκπροσωπεί ένα από τα τρία μεγάλα κράτη της ηπείρου Fódlan.",
            "Το Fire Emblem: Three Houses ήταν το πρώτο Fire Emblem για οικιακή κονσόλα μετά το Radiant Dawn στο Nintendo Wii."
        ],
        "source": "https://en.wikipedia.org/wiki/Fire_Emblem:_Three_Houses",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "tactical-rpg", "nintendo"]
    },
    # 212
    {
        "id": "gaming_med_212",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Grand Theft Auto IV», ποιος είναι ο υπερβολικά αισιόδοξος ξάδελφος του Niko Bellic που τον καλεί διαρκώς να πάνε για μπόουλινγκ;",
        "answers": ["Brucie Kibbutz", "Little Jacob", "Packie McReary", "Roman Bellic"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Roman Bellic είναι ο ξάδελφος του Niko στη Liberty City που διαχειρίζεται μια αποτυχημένη επιχείρηση ταξί και τηλεφωνεί συχνά προτείνοντας μπόουλινγκ.",
        "funFacts": [
            "Οι συνεχείς κλήσεις του Roman για μπόουλινγκ («Hey cousin! Want to go bowling?») έγναν ένα από τα πιο διάσημα memes στο διαδίκτυο.",
            "Ανάλογα με την τελική επιλογή του παίκτη (Deal ή Revenge), ο Roman μπορεί να επιβιώσει ή να δολοφονηθεί την ημέρα του γάμου του."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto_IV",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "open-world", "rockstar"]
    },
    # 213
    {
        "id": "gaming_med_213",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο action RPG «Nioh» της Team Ninja, ποιος ιστορικός Άγγλος ναυτικός που έγινε σαμουράι στην Ιαπωνία είναι ο κύριος πρωταγωνιστής;",
        "answers": ["William Adams", "Edward Kenway", "Thomas Glover", "Richard Cox"],
        "correctAnswerIndex": 0,
        "explanation": "Ο πρωταγωνιστής βασίζεται στον William Adams, τον ιστορικό πρώτο Δυτικό που χρίστηκε Σαμουράι από τον Shogun Tokugawa Ieyasu.",
        "funFacts": [
            "Ο William στο παιχνίδι ακολουθεί τον αλχημιστή Edward Kelley στην Ιαπωνία της περιόδου Sengoku για να ανακτήσει το πνεύμα-φύλακά του, Saoirse.",
            "Η ανάπτυξη του Nioh ξεκίνησε αρχικά το 2004 βασισμένη σε ένα ημιτελές σενάριο του διάσημου σκηνοθέτη Akira Kurosawa."
        ],
        "source": "https://en.wikipedia.org/wiki/Nioh",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "action-rpg", "team-ninja"]
    },
    # 214
    {
        "id": "gaming_med_214",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Overwatch», ποιο είναι το πραγματικό όνομα και επάγγελμα της Hana Song πριν ενταχθεί στη μονάδα MEKA της Νότιας Κορέας;",
        "answers": ["Πιλότος μαχητικών", "Επαγγελματίας παίκτρια esports (D.Va)", "Επιστήμονας ρομποτικής", "Μηχανικός λογισμικού"],
        "correctAnswerIndex": 1,
        "explanation": "Η D.Va (Hana Song) ήταν παγκόσμια πρωταθλήτρια στα esports (συγκεκριμένα στο StarCraft) πριν επιστρατευτεί για να πιλοτάρει τα mechs της MEKA.",
        "funFacts": [
            "Η D.Va μεταδίδει ζωντανά τις μάχες της ενάντια στις επιθέσεις των Omnics στους εκατομμύρια οπαδούς της στο διαδίκτυο.",
            "Η απόλυτη ικανότητά της (Self-Destruct) της επιτρέπει να ανατινάξει το mech της προκαλώντας τεράστια ζημιά σε ακτίνα."
        ],
        "source": "https://en.wikipedia.org/wiki/D.Va_(Overwatch)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "overwatch"]
    },
    # 215
    {
        "id": "gaming_med_215",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Deus Ex: Human Revolution», ποιο είναι το διάσημο απόφθεγμα του πρωταγωνιστή Adam Jensen σχετικά με τις κυβερνο-αναβαθμίσεις του;",
        "answers": ["I am the future", "I never asked for this", "Evolution has begun", "My body is a weapon"],
        "correctAnswerIndex": 1,
        "explanation": "Το «I never asked for this» («Δεν το ζήτησα ποτέ αυτό») είναι η εμβληματική φράση του Adam Jensen, καθώς οι βιονικές αναβαθμίσεις του έγιναν για να σωθεί η ζωή του χωρίς τη συγκατάθεσή του.",
        "funFacts": [
            "Η φράση έγινε άμεσα viral meme στο διαδίκτυο μετά την κυκλοφορία του trailer του Human Revolution το 2011.",
            "Τη χαρακτηριστική βαθιά και βραχνή φωνή του Jensen χαρίζει ο Καναδός ηθοποιός Elias Toufexis."
        ],
        "source": "https://en.wikipedia.org/wiki/Deus_Ex:_Human_Revolution",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "cyberpunk", "rpg"]
    },
    # 216
    {
        "id": "gaming_med_216",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Ghost of Tsushima», ποιος είναι ο πιστός θείος του Jin Sakai και άρχοντας της νήσου Τσουσίμα που επιμένει στην τήρηση του κώδικα των Σαμουράι;",
        "answers": ["Lord Shimura", "Sensei Ishikawa", "Khotun Khan", "Kenji"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Lord Shimura είναι ο Jito (άρχοντας) της Tsushima και θείος του Jin Sakai, ο οποίος απορρίπτει τις ανορθόδοξες τακτικές του «Φαντάσματος».",
        "funFacts": [
            "Η σύγκρουση ανάμεσα στην άκαμπτη τιμή του Shimura και την ανάγκη του Jin να σώσει τον λαό του με κάθε μέσο αποτελεί την καρδιά του σεναρίου.",
            "Το παιχνίδι περιλαμβάνει ειδική λειτουργία «Kurosawa Mode» με ασπρόμαυρο φίλτρο προς τιμήν του σκηνοθέτη Akira Kurosawa."
        ],
        "source": "https://en.wikipedia.org/wiki/Ghost_of_Tsushima",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "playstation", "action-adventure"]
    },
    # 217
    {
        "id": "gaming_med_217",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο platformer «Super Mario Odyssey», ποια είναι η μαγική οντότητα σε μορφή καπέλου που συνεργάζεται με τον Mario και του επιτρέπει να παίρνει τον έλεγχο πλασμάτων;",
        "answers": ["Tiara", "Bowser Jr.", "Cappy", "Toadsworth"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Cappy είναι ένα πλάσμα από το Bonneton του Cap Kingdom που παίρνει τη μορφή του παραδοσιακού κόκκινου καπέλου του Mario.",
        "funFacts": [
            "Η αδελφή του Cappy, η Tiara, έχει απαχθεί από τον Bowser μαζί με την πριγκίπισσα Peach για τον εξαναγκαστικό γάμο τους.",
            "Η ικανότητα «Capture» επιτρέπει στον Mario να ελέγχει δεκάδες διαφορετικούς εχθρούς και αντικείμενα, μέχρι και έναν γιγάντιο T-Rex."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Odyssey",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "mario", "nintendo"]
    },
    # 218
    {
        "id": "gaming_med_218",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο αστυνομικό RPG «Disco Elysium», ποια φανταστική παράκτια πόλη και συγκεκριμένα ποια φτωχή συνοικία της αποτελεί το σκηνικό των ερευνών του ντετέκτιβ;",
        "answers": ["Dunwall", "Gothic District", "Karnaca", "Revachol (Martinaise)"],
        "correctAnswerIndex": 3,
        "explanation": "Η υπόθεση εκτυλίσσεται στη συνοικία Martinaise της μητρόπολης Revachol, μιας άλλοτε ένδοξης πόλης που σημαδεύτηκε από αποτυχημένη επανάσταση.",
        "funFacts": [
            "Ο πρωταγωνιστής ξυπνά με πλήρη αμνησία μετά από ένα καταστροφικό μεθύσι, έχοντας χάσει το όπλο, το σήμα και το ίδιο του το όνομα.",
            "Το παιχνίδι περιέχει πάνω από ένα εκατομμύριο λέξεις διαλόγου και κέρδισε τέσσερα βραβεία στα The Game Awards 2019."
        ],
        "source": "https://en.wikipedia.org/wiki/Disco_Elysium",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "rpg", "indie"]
    },
    # 219
    {
        "id": "gaming_med_219",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο franchise «Halo», ποια είναι η επίσημη ονομασία του εξωσκελετού μάχης υψηλής τεχνολογίας που φοράει ο Master Chief (John-117);",
        "answers": ["Nanosuit", "MJOLNIR Powered Assault Armor", "HEV Suit", "Praetor Suit"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Master Chief φοράει την πανοπλία MJOLNIR Powered Assault Armor, η οποία μπορεί να χρησιμοποιηθεί με ασφάλεια μόνο από γενετικά ενισχυμένους SPARTAN-II υπερστρατιώτες.",
        "funFacts": [
            "Η πανοπλία MJOLNIR διαθέτει νευρωνική διασύνδεση με τον εγκέφαλο του φορέα και μπορεί να φιλοξενήσει τεχνητές νοημοσύνες όπως η Cortana.",
            "Πήρε το όνομά της από το θρυλικό σφυρί του θεού Thor στη σκανδιναβική μυθολογία."
        ],
        "source": "https://en.wikipedia.org/wiki/Master_Chief_(Halo)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "xbox"]
    },
    # 220
    {
        "id": "gaming_med_220",
        "category": "gaming",
        "difficulty": 3,
        "question": "Στο «Doom» (2016) και «Doom Eternal», ποια είναι η ονομασία της αρχαίας προστατευτικής πανοπλίας που φοράει ο Doom Slayer;",
        "answers": ["MJOLNIR Armor", "Nanosuit 2.0", "Praetor Suit", "Berserker Armor"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Doom Slayer φοράει την Praetor Suit, μια αδιαπέραστη αρχαία πανοπλία που σφυρηλατήθηκε στην Κόλαση και απορροφά ενέργεια Argent από τους δαίμονες.",
        "funFacts": [
            "Σύμφωνα με το lore, η στολή σφυρηλατήθηκε από έναν αποστάτη δαίμονα γνωστό ως «The Wretch».",
            "Η Praetor Suit βρέθηκε μαζί με τον Doom Slayer μέσα σε μια σφραγισμένη σαρκοφάγο στο Kadingir Sanctum."
        ],
        "source": "https://en.wikipedia.org/wiki/Doom_Slayer",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["gaming", "fps", "doom"]
    }
]

# We need 50 questions in total: from gaming_med_161 through gaming_med_210.
# The array currently has 60 items (161 to 220). Let's trim to exactly 50 items (161 to 210)!
BATCH_QUESTIONS = NEW_QUESTIONS[:50]

def verify_and_append():
    if len(BATCH_QUESTIONS) != 50:
        raise ValueError(f"Expected 50 questions, got {len(BATCH_QUESTIONS)}")

    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    ids = set()
    for q in BATCH_QUESTIONS:
        idx = q["correctAnswerIndex"]
        counts[idx] = counts.get(idx, 0) + 1
        ids.add(q["id"])

    print(f"Batch distribution: {counts}")
    print(f"IDs count: {len(ids)}, from {min(ids)} to {max(ids)}")

    append_questions("content/questions/el-GR/gaming_medium.json", BATCH_QUESTIONS)

if __name__ == "__main__":
    verify_and_append()

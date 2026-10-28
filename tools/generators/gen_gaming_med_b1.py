# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_med_211",
        "text": "Ποιοι τρεις θρυλικοί δημιουργοί συγκρότησαν τη λεγόμενη 'Dream Team' για την ανάπτυξη του κλασικού RPG 'Chrono Trigger' (1995);",
        "correct": "Hironobu Sakaguchi, Yuji Horii και Akira Toriyama",
        "distractors": [
            "Shigeru Miyamoto, Eiji Aonuma και Koji Kondo",
            "Hideo Kojima, Shinji Mikami και Yoshitaka Amano",
            "Tetsuya Nomura, Yoshinori Kitase και Nobuo Uematsu"
        ],
        "explanation": "Το Chrono Trigger δημιουργήθηκε από τον δημιουργό του Final Fantasy (Sakaguchi), τον δημιουργό του Dragon Quest (Horii) και τον θρυλικό δημιουργό του Dragon Ball (Toriyama).",
        "funFacts": [
            "Ο συνθέτης Yasunori Mitsuda εργάστηκε τόσο σκληρά για το soundtrack του παιχνιδιού που κατέληξε στο νοσοκομείο με έλκος στομάχου, με τον Nobuo Uematsu να ολοκληρώνει τα υπόλοιπα κομμάτια.",
            "Το παιχνίδι εισήγαγε τη λειτουργία New Game+ και περιλάμβανε περισσότερα από 12 διαφορετικά τέλη."
        ],
        "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
        "tags": ["gaming", "chrono_trigger", "square", "snes", "rpg"]
    },
    {
        "id": "gaming_med_212",
        "text": "Στο 'Dark Souls', ποιος ιππότης αναζητά τον δικό του 'ήλιο' και προσφέρει τη συνεργασία του στον παίκτη ιδρύοντας το covenant των Warriors of Sunlight;",
        "correct": "Solaire of Astora",
        "distractors": ["Siegmeyer of Catarina", "Lautrec of Carim", "Andre of Astora"],
        "explanation": "Ο Solaire of Astora είναι ο αγαπημένος ιππότης της κοινότητας που εισήγαγε τη χαρακτηριστική χειρονομία και φράση 'Praise the Sun!'.",
        "funFacts": [
            "Ο Solaire σχεδιάστηκε από τον Hidetaka Miyazaki για να φέρει μια αχτίδα ελπίδας και ζεστασιάς στον ζοφερό και απελπιστικό κόσμο του Lordran.",
            "Αν ο παίκτης δεν ανοίξει μια μυστική συντόμευση στο Lost Izalith, ο Solaire τρελαίνεται από ένα παρασιτικό Sunlight Maggot και επιτίθεται στον παίκτη."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "fromsoftware", "solaire", "lore"]
    },
    {
        "id": "gaming_med_213",
        "text": "Στο 'Metal Gear Solid' (1998) στο PlayStation, πώς μπορούσε ο παίκτης να εξουδετερώσει την τηλεπαθητική ανάγνωση κινήσεων του Psycho Mantis;",
        "correct": "Συνδέοντας το χειριστήριο στη δεύτερη θύρα (Controller Port 2)",
        "distractors": [
            "Χρησιμοποιώντας τις θερμικές διόπτρες (Thermal Goggles)",
            "Πυροβολώντας τα αγάλματα του δωματίου με chaff grenades",
            "Καλώντας τη Meryl στο codec με συχνότητα 140.85"
        ],
        "explanation": "Ο Psycho Mantis 'διάβαζε' τις κινήσεις του παίκτη απευθείας από την πρώτη θύρα χειριστηρίου· αλλάζοντας τη σύνδεση στη θύρα 2, ο Snake μπορούσε να επιτεθεί χωρίς να προβλέπονται οι κινήσεις του.",
        "funFacts": [
            "Ο Psycho Mantis έσπαγε τον τέταρτο τοίχο διαβάζοντας την κάρτα μνήμης (Memory Card) του παίκτη και σχολιάζοντας άλλα παιχνίδια της Konami όπως το Castlevania: Symphony of the Night.",
            "Έκανε επίσης το χειριστήριο DualShock να κινείται μόνο του πάνω στο πάτωμα μέσω της δόνησης."
        ],
        "source": "https://en.wikipedia.org/wiki/Psycho_Mantis",
        "tags": ["gaming", "metal_gear_solid", "hideo_kojima", "playstation", "bosses"]
    },
    {
        "id": "gaming_med_214",
        "text": "Πόσο διαρκεί ο χρονικός κύκλος πριν πέσει το φεγγάρι και καταστρέψει τον κόσμο της Termina στο 'The Legend of Zelda: Majora's Mask';",
        "correct": "3 ημέρες (72 ώρες εντός παιχνιδιού)",
        "distractors": ["7 ημέρες", "24 ώρες", "12 ημέρες"],
        "explanation": "Στο Majora's Mask (2000), ο Link έχει στη διάθεσή του ακριβώς 3 ημέρες (περίπου 54 λεπτά πραγματικού χρόνου) πριν παίξει το Song of Time στην οκαρίνα για να γυρίσει πίσω στο ξημέρωμα της 1ης ημέρας.",
        "funFacts": [
            "Το παιχνίδι αναπτύχθηκε σε μόλις έναν χρόνο επειδή ο Eiji Aonuma δέχτηκε την πρόκληση του Shigeru Miyamoto να φτιάξει ένα νέο Zelda χρησιμοποιώντας τα assets του Ocarina of Time.",
            "Κάθε χαρακτήρας στην Termina έχει ένα αυστηρό καθημερινό πρόγραμμα 72 ωρών με μοναδικές δραστηριότητες και αντιδράσεις στην επικείμενη καταστροφή."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Majora%27s_Mask",
        "tags": ["gaming", "zelda", "majoras_mask", "nintendo", "n64"]
    },
    {
        "id": "gaming_med_215",
        "text": "Στην τριλογία 'Mass Effect', με ποια αγαπημένη του τεχνική ασχολία δικαιολογεί συνεχώς ο Turian Garrus Vakarian την έλλειψη χρόνου για συζήτηση;",
        "correct": "Καλιμπράρει τα όπλα του σκάφους (Calibrations)",
        "distractors": ["Καθαρίζει τη στολή του", "Αναβαθμίζει τη μηχανή FTL", "Συντάσσει αναφορές για τη Citadel"],
        "explanation": "Η ατάκα του Garrus 'Can it wait for a bit? I'm in the middle of some calibrations' έγινε το πιο αγαπημένο τρέχον αστείο (running gag) της τριλογίας Mass Effect.",
        "funFacts": [
            "Στο Mass Effect 3, η BioWare έβαλε μια αστεία σκηνή όπου ο Garrus και ο Shepard διαγωνίζονται στη σκοποβολή στην κορυφή της Citadel.",
            "Ο Garrus στο Mass Effect 2 λειτουργούσε ως αυτόκλητος τιμωρός στον σταθμό Omega υπό το ψευδώνυμο 'Archangel'."
        ],
        "source": "https://en.wikipedia.org/wiki/Garrus_Vakarian",
        "tags": ["gaming", "mass_effect", "bioware", "garrus", "characters"]
    },
    {
        "id": "gaming_med_216",
        "text": "Στο σύμπαν της σειράς 'Fallout', ποια συγκεκριμένη ημερομηνία ξέσπασε ο Μεγάλος Πόλεμος (The Great War) με τον παγκόσμιο πυρηνικό όλεθρο;",
        "correct": "23 Οκτωβρίου 2077",
        "distractors": ["4 Ιουλίου 2076", "1 Ιανουαρίου 2100", "11 Νοεμβρίου 2055"],
        "explanation": "Ο Μεγάλος Πόλεμος διήρκεσε μόλις δύο ώρες το πρωί της 23ης Οκτωβρίου 2077, καταστρέφοντας τον ανθρώπινο πολιτισμό και μετατρέποντας τη Γη σε ραδιενεργό ερημότοπο (Wasteland).",
        "funFacts": [
            "Η εταιρεία Vault-Tec είχε κατασκευάσει υπόγεια καταφύγια (Vaults), τα περισσότερα εκ των οποίων ήταν μυστικά κοινωνικά και βιολογικά πειράματα πάνω στους επιζώντες.",
            "Η 23η Οκτωβρίου γιορτάζεται κάθε χρόνο από την Bethesda και τους οπαδούς ως 'Fallout Day'."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout_(series)",
        "tags": ["gaming", "fallout", "bethesda", "lore", "rpg"]
    },
    {
        "id": "gaming_med_217",
        "text": "Ποιο διάσημο εικονικό επιδημιολογικό περιστατικό έλαβε χώρα στο 'World of Warcraft' το 2005 και μελετήθηκε από πραγματικούς επιστήμονες;",
        "correct": "Το περιστατικό του Μολυσμένου Αίματος (Corrupted Blood incident)",
        "distractors": ["Η πανούκλα των Undead", "Η κατάρα του Lich King", "Ο πυρετός των Goblins"],
        "explanation": "Μια μεταδοτική ασθένεια από το raid Zul'Gurub (το Corrupted Blood του Hakkar) μεταφέρθηκε κατά λάθος από κατοικίδια παικτών στις πολυπληθείς πόλεις, προκαλώντας μαζικούς θανάτους.",
        "funFacts": [
            "Επιδημιολόγοι και ερευνητές της αντιτρομοκρατίας μελέτησαν το φαινόμενο για να κατανοήσουν την ανθρώπινη συμπεριφορά και τον πανικό σε πραγματικές πανδημίες.",
            "Οι παίκτες αντέδρασαν με τρόπους που μιμούνταν την πραγματικότητα: άλλοι εγκατέλειψαν τις πόλεις σε καραντίνα και άλλοι μόλυναν σκόπιμα συμπαίκτες τους."
        ],
        "source": "https://en.wikipedia.org/wiki/Corrupted_Blood_incident",
        "tags": ["gaming", "world_of_warcraft", "blizzard", "history", "mmorpg"]
    },
    {
        "id": "gaming_med_218",
        "text": "Στο αριστούργημα 'Shadow of the Colossus' (2005) του Fumito Ueda, πόσους γιγάντιους Κολοσσούς πρέπει να νικήσει ο Wander για να αναστήσει τη Mono;",
        "correct": "16",
        "distractors": ["12", "20", "8"],
        "explanation": "Ο Wander ταξιδεύει στην Απαγορευμένη Χώρα με το πιστό του άλογο Agro και πρέπει να εντοπίσει και να σκαρφαλώσει πάνω σε 16 μοναδικούς κολοσσούς για να τρυπήσει τα αδύνατα σημεία τους.",
        "funFacts": [
            "Στο παιχνίδι δεν υπάρχουν πόλεις, μπουντρούμια ή απλοί εχθροί· ολόκληρο το παιχνίδι αποτελείται αποκλειστικά από τις 16 αναμετρήσεις με τα αφεντικά.",
            "Καθώς ο Wander σκοτώνει κάθε κολοσσό, η εμφάνισή του αλλοιώνεται σταδιακά, δείχνοντας το σκοτεινό τίμημα της αποστολής του."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_of_the_Colossus",
        "tags": ["gaming", "shadow_of_the_colossus", "team_ico", "playstation", "action"]
    },
    {
        "id": "gaming_med_219",
        "text": "Ποια είναι η αξιομνημόνευτη ατάκα με την οποία υποδέχεται τον Leon ο μυστηριώδης οπλοπώλης (Merchant) στο 'Resident Evil 4' (2005);",
        "correct": "What're ya buyin', stranger?",
        "distractors": ["Need some weapons, boy?", "Welcome to my store!", "Got some cash for me?"],
        "explanation": "Ο Merchant με τη μοβ μάσκα και τη βαριά φωνή εμφανίζεται σε απρόσμενα σημεία προσφέροντας αναβαθμίσεις όπλων και λέγοντας επίσης 'What're ya sellin'?' και 'Heh heh heh, thank you!'.",
        "funFacts": [
            "Ο Merchant έγινε ένας από τους πιο αγαπητούς NPC στην ιστορία του gaming χωρίς να αποκαλύπτεται ποτέ το όνομά του ή το παρελθόν του.",
            "Στο remake του 2023, η Capcom διατήρησε τις εμβληματικές ατάκες του αλλά με νέες ηχογραφήσεις και χιουμοριστικές προσθήκες."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_4",
        "tags": ["gaming", "resident_evil", "capcom", "quotes"]
    },
    {
        "id": "gaming_med_220",
        "text": "Ποιος είναι ο εκκεντρικός ιδρυτής των εργαστηρίων Aperture Science στο 'Portal 2', διάσημος για τον οργισμένο μονόλογό του για τα λεμόνια;",
        "correct": "Cave Johnson",
        "distractors": ["Doug Rattmann", "Wallace Breen", "Eli Vance"],
        "explanation": "Ο Cave Johnson (με τη φωνή του βραβευμένου με Όσκαρ J.K. Simmons) ακούγεται από παλιές μαγνητοφωνήσεις να εξοργίζεται και να απειλεί: 'I'm gonna burn your house down with the lemons!'.",
        "funFacts": [
            "Η πιστή του γραμματέας Caroline αποτέλεσε τη βάση της ανθρώπινης συνείδησης πάνω στην οποία προγραμματίστηκε η GLaDOS.",
            "Η Aperture Science ξεκίνησε αρχικά τη δεκαετία του 1940 ως κατασκευάστρια κουρτινών μπάνιου (Aperture Fixtures)."
        ],
        "source": "https://en.wikipedia.org/wiki/Characters_of_the_Half-Life_series#Cave_Johnson",
        "tags": ["gaming", "portal", "valve", "cave_johnson"]
    },
    {
        "id": "gaming_med_221",
        "text": "Ποια τεχνική προηγμένης κίνησης στο 'Super Smash Bros. Melee' (2001) επιτρέπει στους παίκτες να γλιστρούν στο έδαφος κάνοντας air-dodge διαγώνια προς τα κάτω;",
        "correct": "Wavedashing",
        "distractors": ["L-Canceling", "Dash Dancing", "Short Hopping"],
        "explanation": "Το Wavedashing εκμεταλλεύεται τη φυσική του Melee: κάνοντας άλμα και αμέσως διαγώνιο air-dodge στο πάτωμα, ο χαρακτήρας γλιστράει διατηρώντας όλες τις επιλογές επίθεσης στο έδαφος.",
        "funFacts": [
            "Αν και ανακαλύφθηκε από τους παίκτες ως μηχανισμός φυσικής, οι σχεδιαστές της Nintendo γνώριζαν την ύπαρξή του αλλά δεν πίστευαν ότι θα γινόταν ο ακρογωνιαίος λίθος των τουρνουά esports.",
            "Ο Masahiro Sakurai αφαίρεσε το wavedashing στο Super Smash Bros. Brawl για να κάνει το παιχνίδι πιο προσιτό σε αρχάριους."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Smash_Bros._Melee",
        "tags": ["gaming", "super_smash_bros", "nintendo", "melee", "esports"]
    },
    {
        "id": "gaming_med_222",
        "text": "Ποια τεράστια ανατροπή περιμένει τον Alucard στο δεύτερο μισό του 'Castlevania: Symphony of the Night' (1997) αν απελευθερώσει τον Richter Belmont;",
        "correct": "Εμφανίζεται ολόκληρο το κάστρο αναποδογυρισμένο στην ανάποδη κατεύθυνση (Inverted Castle)",
        "distractors": [
            "Το κάστρο μεταφέρεται σε μια άλλη χρονική διάσταση στο μέλλον",
            "Ο Alucard μετατρέπεται σε κανονικό άνθρωπο χωρίς βαμπιρικές δυνάμεις",
            "Το κάστρο βυθίζεται στα βάθη του ωκεανού"
        ],
        "explanation": "Φορώντας τα Holy Glasses και καταστρέφοντας τη σφαίρα του Shaft, ο Alucard ξεκλειδώνει το Inverted Castle, έναν ολόκληρο δεύτερο χάρτη όπου το ταβάνι γίνεται πάτωμα με νέα αφεντικά.",
        "funFacts": [
            "Το Symphony of the Night μαζί με το Super Metroid όρισαν και ονοματοδότησαν το είδος 'Metroidvania'.",
            "Ο εισαγωγικός διάλογος μεταξύ Richter και Dracula περιέχει την κλασική ατάκα 'What is a man? A miserable little pile of secrets!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Castlevania:_Symphony_of_the_Night",
        "tags": ["gaming", "castlevania", "konami", "playstation", "metroidvania"]
    },
    {
        "id": "gaming_med_223",
        "text": "Στο 'Half-Life 2', ποια εγκαταλελειμμένη πόλη-φάντασμα γεμάτη ζόμπι και παγίδες αναγκάζεται να διασχίσει ο Gordon Freeman με τη βοήθεια του Πατέρα Γρηγόρη;",
        "correct": "Ravenholm",
        "distractors": ["Black Mesa", "City 17", "Nova Prospekt"],
        "explanation": "Το κεφάλαιο 'We Don't Go to Ravenholm...' είναι ένα από τα πιο ατμοσφαιρικά κομμάτια τρόμου του παιχνιδιού, όπου ο Freeman χρησιμοποιεί λεπίδες πριονιού με το Gravity Gun.",
        "funFacts": [
            "Ο εκκεντρικός ιερέας Πατέρας Γρηγόρης (Father Grigori) βοηθά τον Gordon με την καραμπίνα του 'Annabelle' και στήνει παγίδες με περιστρεφόμενες προπέλες.",
            "Η πόλη βομβαρδίστηκε από το Combine με βλήματα γεμάτα headcrabs για να εξοντωθούν οι αντιστασιακοί που κρύβονταν εκεί."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2",
        "tags": ["gaming", "half_life", "valve", "ravenholm", "fps"]
    },
    {
        "id": "gaming_med_224",
        "text": "Στο 'Silent Hill 2' (2001), από ποιον λαμβάνει ένα μυστηριώδες γράμμα ο James Sunderland που τον οδηγεί στην ομώνυμη ομιχλώδη πόλη;",
        "correct": "Από τη νεκρή σύζυγό του Mary",
        "distractors": ["Από τη μητέρα του", "Από τον παιδικό του φίλο", "Από τον γιατρό του ψυχιατρείου"],
        "explanation": "Το γράμμα ισχυρίζεται ότι γράφτηκε από τη Mary, η οποία πέθανε από βαριά ασθένεια τρία χρόνια πριν, καλώντας τον στο 'ειδικό τους μέρος' στο Silent Hill.",
        "funFacts": [
            "Στο τέλος του παιχνιδιού αποκαλύπτεται η σοκαριστική αλήθεια ότι ο ίδιος ο James είχε δολοφονήσει τη Mary με ένα μαξιλάρι λίγες μόλις ημέρες πριν.",
            "Υπάρχει ένα κωμικό μυστικό τέλος (Dog Ending) όπου αποκαλύπτεται ότι όλα τα γεγονότα τα χειριζόταν ένας σκύλος Shiba Inu σε ένα δωμάτιο ελέγχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_2",
        "tags": ["gaming", "silent_hill", "konami", "survival_horror", "story"]
    },
    {
        "id": "gaming_med_225",
        "text": "Ποιος είναι ο κυβερνο-αναβαθμισμένος μυστικός πράκτορας της UNATCO που πρωταγωνιστεί στο ιστορικό immersive sim 'Deus Ex' (2000) του Warren Spector;",
        "correct": "JC Denton",
        "distractors": ["Adam Jensen", "Alex D", "Paul Denton"],
        "explanation": "Ο JC Denton είναι νανοτεχνολογικά ενισχυμένος πράκτορας που εμπλέκεται σε μια παγκόσμια συνωμοσία γύρω από τον ιό 'Gray Death' και τους Illuminati.",
        "funFacts": [
            "Το Deus Ex προσέφερε πρωτοφανή ελευθερία προσέγγισης: κάθε αποστολή μπορούσε να λυθεί με μάχη, stealth, hacking υπολογιστών ή κοινωνική πειθώ.",
            "Στο πρίκουελ 'Deus Ex: Human Revolution' (2011), ο πρωταγωνιστής είναι ο Adam Jensen με τη διάσημη ατάκα 'I never asked for this'."
        ],
        "source": "https://en.wikipedia.org/wiki/Deus_Ex_(video_game)",
        "tags": ["gaming", "deus_ex", "ion_storm", "warren_spector", "rpg"]
    },
    {
        "id": "gaming_med_226",
        "text": "Στο πρώτο 'BioShock', ποια φαινομενικά ευγενική φράση αποκαλύπτεται ότι είναι η εντολή νοητικού ελέγχου που αναγκάζει τον Jack να υπακούει τυφλά;",
        "correct": "Would you kindly (Θα είχες την καλοσύνη)",
        "distractors": ["If you please", "By your command", "Do what must be done"],
        "explanation": "Ο Frank Fontaine (υποδυόμενος τον φιλικό Atlas) χρησιμοποιούσε τη φράση 'Would you kindly' για να ελέγχει υποσυνείδητα τον προγραμματισμένο εγκέφαλο του Jack.",
        "funFacts": [
            "Ο δημιουργός του παιχνιδιού Ken Levine χρησιμοποίησε τη φράση ως ευφυή μεταφορά για την ίδια τη φύση των video games, όπου οι παίκτες εκτελούν τυφλά κάθε εντολή των quest markers.",
            "Η σκηνή της συνάντησης με τον Andrew Ryan στο γραφείο του περιλαμβάνει τη φιλοσοφική ρήση: 'A man chooses, a slave obeys'."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock",
        "tags": ["gaming", "bioshock", "ken_levine", "plot_twist"]
    },
    {
        "id": "gaming_med_227",
        "text": "Ποια θρυλική ανατροπή στα esports συνέβη στο τουρνουά EVO 2004 κατά τη διάρκεια του αγώνα 'Street Fighter III: 3rd Strike' μεταξύ Daigo και Justin Wong;",
        "correct": "Evo Moment #37 (Daigo Parry)",
        "distractors": ["The Wombocombo", "The Daigo Rush", "The Perfect Round"],
        "explanation": "Με ελάχιστη ζωή που δεν άντεχε ούτε chip damage, ο Daigo Umehara (Ken) απέκρουσε διαδοχικά στον αέρα και το έδαφος και τις 15 κλωτσιές του Super της Chun-Li και νίκησε.",
        "funFacts": [
            "Το parry στο 3rd Strike απαιτεί πάτημα του μοχλού προς τα εμπρός ακριβώς τη στιγμή του χτυπήματος με περιθώριο κλάσματος του δευτερολέπτου.",
            "Το βίντεο της στιγμής με τις έξαλλες κραυγές του πλήθους θεωρείται η πιο διάσημη στιγμή στην ιστορία των competitive fighting games."
        ],
        "source": "https://en.wikipedia.org/wiki/Evo_Moment_37",
        "tags": ["gaming", "street_fighter", "esports", "daigo", "evo"]
    },
    {
        "id": "gaming_med_228",
        "text": "Σε ποιο κλασικό RPG του Super Nintendo περιλαμβάνεται η περίφημη σκηνή της όπερας ('Aria di Mezzo Carattere') όπου η στρατηγός Celes υποδύεται μια τραγουδίστρια;",
        "correct": "Final Fantasy VI (Final Fantasy III στις ΗΠΑ)",
        "distractors": ["Final Fantasy IV", "Chrono Trigger", "Secret of Mana"],
        "explanation": "Στο Final Fantasy VI (1994), η Celes Chere αντικαθιστά την ντίβα Maria στην όπερα για να παραπλανήσει τον Setzer Gabbiani και να εξασφαλίσει το αερόπλοιο The Blackjack.",
        "funFacts": [
            "Το τσιπ ήχου του SNES προσομοίωσε πολυφωνικό τραγούδι όπερας χρησιμοποιώντας σύνθεση δειγμάτων (sampling) χωρίς πραγματική ηχογραφημένη φωνή.",
            "Ο κακός του παιχνιδιού Kefka Palazzo καταστρέφει στην πραγματικότητα τον κόσμο στα μισά της ιστορίας, οδηγώντας στον εφιαλτικό World of Ruin."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VI",
        "tags": ["gaming", "final_fantasy", "square", "snes", "rpg"]
    },
    {
        "id": "gaming_med_229",
        "text": "Σε ποιο τεράστιο ηφαιστειογενές νησί της επαρχίας Morrowind διαδραματίζεται το 'The Elder Scrolls III: Morrowind' (2002);",
        "correct": "Vvardenfell",
        "distractors": ["Solstheim", "Cyrodiil", "High Rock"],
        "explanation": "Το Vvardenfell κυριαρχείται από το γιγάντιο ενεργό ηφαίστειο Red Mountain και κατοικείται από τους Dark Elves (Dunmer), υπό την κυριαρχία του θεϊκού Τριβουνάλου.",
        "funFacts": [
            "Ο παίκτης ξεκινά ως πρώην κατάδικος που φτάνει με πλοίο στο λιμάνι Seyda Neen και αποδεικνύεται η μετενσάρκωση του Nerevar.",
            "Στο Morrowind δεν υπήρχαν πυξίδες με δείκτες αποστολών (quest markers)· ο παίκτης έπρεπε να διαβάζει γραπτές οδηγίες στο ημερολόγιο για να βρει το δρόμο του."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_III:_Morrowind",
        "tags": ["gaming", "morrowind", "bethesda", "elder_scrolls", "rpg"]
    },
    {
        "id": "gaming_med_230",
        "text": "Ποιος εξωγήινος επίλεκτος διοικητής του Covenant γίνεται συμπρωταγωνιστής του Master Chief στο 'Halo 2' (2004), αναλαμβάνοντας τον τίτλο του Arbiter;",
        "correct": "Thel 'Vadam",
        "distractors": ["Rtas 'Vadum", "Tartarus", "Jul 'Mdama"],
        "explanation": "Ο πρώην Supreme Commander Thel 'Vadam τιμωρείται με ατίμωση για την καταστροφή της πρώτης εγκατάστασης Halo και χρίζεται Arbiter, ανακαλύπτοντας τελικά την προδοσία των Προφητών.",
        "funFacts": [
            "Τη φωνή του Arbiter δάνεισε ο καταξιωμένος ηθοποιός Keith David.",
            "Η απόφαση της Bungie να χωρίσει το gameplay του Halo 2 ανάμεσα στον Master Chief και τον Arbiter αποτέλεσε αρχικά σημείο έντονης συζήτησης μεταξύ των παικτών."
        ],
        "source": "https://en.wikipedia.org/wiki/Arbiter_(Halo)",
        "tags": ["gaming", "halo", "bungie", "arbiter", "lore"]
    },
    {
        "id": "gaming_med_231",
        "text": "Στη σειρά 'Kingdom Hearts', ποιο κοινό γράμμα περιέχεται υποχρεωτικά στα ονόματα όλων των μελών της Organization XIII ως αναγραμματισμός;",
        "correct": "Το γράμμα X",
        "distractors": ["Το γράμμα Z", "Το γράμμα K", "Το γράμμα V"],
        "explanation": "Κάθε μέλος της Organization XIII παίρνει το αρχικό ανθρώπινο όνομά του, προσθέτει το γράμμα 'X' και αναδιατάσσει τα γράμματα (π.χ. Sora -> Roxas, Ansem -> Xemnas).",
        "funFacts": [
            "Το γράμμα 'X' συμβολίζει το Recusant's Sigil και χρησιμοποιείται από τον Master Xehanort για να παρακολουθεί τα μέλη της οργάνωσης.",
            "Όλα τα μέλη φορούν χαρακτηριστικές μαύρες μακριές καπαρντίνες με κουκούλες για να προστατεύονται από τα σκοτεινά περάσματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Organization_XIII",
        "tags": ["gaming", "kingdom_hearts", "square_enix", "lore"]
    },
    {
        "id": "gaming_med_232",
        "text": "Στα παιχνίδια 'Pokémon Gold και Silver' (1999), ποια τεράστια έκπληξη περίμενε τους παίκτες μετά τη νίκη επί του Champion στο Johto;",
        "correct": "Μπορούσαν να ταξιδέψουν πίσω στην περιοχή Kanto και να κερδίσουν άλλα 8 σήματα γυμναστηρίων",
        "distractors": [
            "Ξεκλείδωναν μια νέα γενιά με 150 επιπλέον Pokémon",
            "Μπορούσαν να παίξουν ως ο Giovanni και να ηγηθούν της Team Rocket",
            "Το παιχνίδι μετατρεπόταν σε προσομοίωση εκτροφείου Pokémon"
        ],
        "explanation": "Ο αείμνηστος πρόεδρος της Nintendo Satoru Iwata συμπίεσε εκπληκτικά τον κώδικα του παιχνιδιού, επιτρέποντας στη Game Freak να χωρέσει ολόκληρο τον χάρτη του πρώτου παιχνιδιού (Kanto) στο Game Boy Color.",
        "funFacts": [
            "Στο τέλος του παιχνιδιού, στην κορυφή του Mt. Silver, ο παίκτης αντιμετωπίζει τον σιωπηλό Red, τον ισχυρότερο εκπαιδευτή του παιχνιδιού με Pokémon επιπέδου 80+.",
            "Τα Gold & Silver εισήγαγαν επίσης κύκλο ημέρας-νύχτας πραγματικού χρόνου και εκτροφή Pokémon με αυγά."
        ],
        "source": "https://en.wikipedia.org/wiki/Pok%C3%A9mon_Gold_and_Silver",
        "tags": ["gaming", "pokemon", "game_boy", "nintendo", "iwata"]
    },
    {
        "id": "gaming_med_233",
        "text": "Στο 'Bloodborne' (2015) της FromSoftware, πώς ονομάζεται ο απόκοσμος τόπος ανάπαυσης όπου η Κούκλα (The Doll) βοηθά τον κυνηγό να αναβαθμίσει τα στατιστικά του;",
        "correct": "Hunter's Dream (Το Όνειρο του Κυνηγού)",
        "distractors": ["The Nexus", "Firelink Shrine", "Majula"],
        "explanation": "Το Hunter's Dream λειτουργεί ως το ασφαλές καταφύγιο του παίκτη, όπου φιλοξενείται ο πρώτος κυνηγός Gehrman και η ζωντανή κούκλα που δέχεται τα Blood Echoes.",
        "funFacts": [
            "Ο σχεδιασμός του Hunter's Dream βασίζεται σε ένα πραγματικό εγκαταλελειμμένο εργαστήριο που κρύβεται βαθιά μέσα στην πόλη του Yharnam.",
            "Αν ο παίκτης καταναλώσει τρία κομμάτια ομφάλιου λώρου (Third Umbilical Cords), ξεκλειδώνει το μυστικό τελικό αφεντικό Moon Presence."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodborne",
        "tags": ["gaming", "bloodborne", "fromsoftware", "playstation", "action_rpg"]
    },
    {
        "id": "gaming_med_234",
        "text": "Ποιο αντικείμενο συνδυάζεται με ένα Tome of Town Portal στον Horadric Cube για να ανοίξει το Secret Cow Level στο 'Diablo II';",
        "correct": "Το ξύλινο πόδι του Wirt (Wirt's Leg)",
        "distractors": ["Το μάτι του Horazon", "Το δαχτυλίδι της Andariel", "Το κέρατο του Diablo"],
        "explanation": "Ο παίκτης επιστρέφει στα ερείπια της Tristram, ανακτά το ξύλινο πόδι του Wirt από το πτώμα του αγοριού και το συνδυάζει στον κύβο στο Rogue Encampment.",
        "funFacts": [
            "Οι οπλισμένες αγελάδες του επιπέδου κρατούν δόρατα και μουγκρίζουν ακατάπαυστα με ανθρώπινη φωνή ('Moo, moo moo moo!').",
            "Αν ο παίκτης σκοτώσει τον Cow King, δεν μπορεί να ανοίξει ξανά την πύλη στο ίδιο επίπεδο δυσκολίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_II",
        "tags": ["gaming", "diablo", "blizzard", "easter_egg", "arpg"]
    },
    {
        "id": "gaming_med_235",
        "text": "Ποιο αμερικανικό στούντιο από το Όστιν του Τέξας ανέλαβε και αναβίωσε με τεράστια επιτυχία τη σειρά Metroid σε 3D με το 'Metroid Prime' (2002);",
        "correct": "Retro Studios",
        "distractors": ["Rare", "Silicon Knights", "Monolith Soft"],
        "explanation": "Η Retro Studios ανέπτυξε την τριλογία Metroid Prime για το GameCube και το Wii, μετατρέποντας με αριστουργηματικό τρόπο την εξερεύνηση του 2D Metroid σε προοπτική πρώτου προσώπου.",
        "funFacts": [
            "Ο Shigeru Miyamoto επισκέφθηκε το στούντιο και πρότεινε να εγκαταλείψουν διάφορα άλλα σχέδια για να επικεντρωθούν αποκλειστικά σε ένα 3D Metroid.",
            "Το Metroid Prime απέσπασε βαθμολογία 97/100 στο Metacritic και θεωρείται ένα από τα κορυφαία παιχνίδια του Nintendo GameCube."
        ],
        "source": "https://en.wikipedia.org/wiki/Metroid_Prime",
        "tags": ["gaming", "metroid", "retro_studios", "gamecube", "nintendo"]
    },
    {
        "id": "gaming_med_236",
        "text": "Ποια είναι η συμπρωταγωνίστρια του Diddy Kong στο 'Donkey Kong Country 2: Diddy's Kong Quest' που μπορεί να πετάει περιστρέφοντας την ξανθιά κοτσίδα της;",
        "correct": "Dixie Kong",
        "distractors": ["Tiny Kong", "Candy Kong", "Wrinkly Kong"],
        "explanation": "Η Dixie Kong εισήγαγε την ικανότητα 'Helicopter Spin', επιτρέποντας στους παίκτες να αιωρούνται απαλά πάνω από επικίνδυνους γκρεμούς και παγίδες.",
        "funFacts": [
            "Η Dixie Kong έγινε τόσο δημοφιλής που πρωταγωνίστησε ως επικεφαλής στο Donkey Kong Country 3 μαζί με τον ξάδελφό της Kiddy Kong.",
            "Το soundtrack του Donkey Kong Country 2 από τον David Wise (ιδιαίτερα το κομμάτι 'Stickerbush Symphony') θεωρείται μνημειώδες για το SNES."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_Country_2:_Diddy%27s_Kong_Quest",
        "tags": ["gaming", "donkey_kong", "rare", "snes", "nintendo"]
    },
    {
        "id": "gaming_med_237",
        "text": "Στο JRPG 'Persona 4' (2008) της Atlus, πώς εισέρχονται οι μαθητές στον μυστηριώδη κόσμο της τηλεόρασης για να σώσουν τα θύματα απαγωγής;",
        "correct": "Μέσα από το τηλεοπτικό κανάλι του μεσονυκτίου (Midnight Channel)",
        "distractors": ["Μέσα από το Metaverse", "Μέσα από το Tartarus", "Μέσα από το Dark Hour"],
        "explanation": "Στη βροχερή επαρχιακή πόλη Inaba, υπάρχει ένας αστικός μύθος ότι αν κοιτάξεις μια κλειστή τηλεόραση τα μεσάνυχτα υπό βροχή, βλέπεις την αδελφή ψυχή σου, οδηγώντας στον κόσμο του TV World.",
        "funFacts": [
            "Ο φιλικός βοηθός με τη στολή αρκούδας που συναντούν εκεί ονομάζεται Teddie (Kuma).",
            "Η ενισχυμένη έκδοση Persona 4 Golden στο PlayStation Vita θεωρείται ένας από τους πιο καθοριστικούς τίτλους της φορητής κονσόλας."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_4",
        "tags": ["gaming", "persona", "atlus", "jrpg", "playstation"]
    },
    {
        "id": "gaming_med_238",
        "text": "Ποιο είναι το κωδικό όνομα του πρωταγωνιστή μαθητή στο 'Persona 5' (2016), ο οποίος ηγείται των Phantom Thieves of Hearts;",
        "correct": "Joker",
        "distractors": ["Skull", "Crow", "Fox"],
        "explanation": "Ο πρωταγωνιστής (γνωστός στο manga ως Ren Amamiya) χρησιμοποιεί το Persona Arsène και οδηγεί τους Phantom Thieves στην κλοπή των 'αλλοιωμένων καρδιών' διεφθαρμένων ενηλίκων.",
        "funFacts": [
            "Η γάτα που μπορεί να μιλάει και μεταμορφώνεται σε βαν ονομάζεται Morgana.",
            "Ο Joker έγινε ο πρώτος DLC μαχητής από τρίτη εταιρεία στο Fighters Pass του Super Smash Bros. Ultimate στο Switch."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_5",
        "tags": ["gaming", "persona", "atlus", "joker", "jrpg"]
    },
    {
        "id": "gaming_med_239",
        "text": "Ποιος διάσημος μουσικός και επικεφαλής των Nine Inch Nails συνέθεσε το αυθεντικό soundtrack και τα ηχητικά εφέ του 'Quake' (1996);",
        "correct": "Trent Reznor",
        "distractors": ["Mick Gordon", "Bobby Prince", "Kelly Bailey"],
        "explanation": "Ο Trent Reznor δημιούργησε ένα σκοτεινό, βιομηχανικό ambient soundtrack για το Quake της id Software, ενώ τα κουτιά πυρομαχικών του nailgun φέρουν το λογότυπο 'NIN'.",
        "funFacts": [
            "Το λογότυπο NIN των Nine Inch Nails είναι χαραγμένο απευθείας πάνω στα κουτιά σφαιρών του όπλου Nailgun μέσα στο παιχνίδι.",
            "Το Quake ήταν το πρώτο παιχνίδι της id Software με πλήρως τρισδιάστατο πολυγωνικό κόσμο και εχθρούς."
        ],
        "source": "https://en.wikipedia.org/wiki/Quake_(video_game)",
        "tags": ["gaming", "quake", "id_software", "trent_reznor", "fps"]
    },
    {
        "id": "gaming_med_240",
        "text": "Στο lore του 'Overwatch', ποιο ήταν το προηγούμενο επάγγελμα της Hana Song (D.Va) πριν επιστρατευτεί για να πιλοτάρει το στρατιωτικό MEKA της Κορέας;",
        "correct": "Επαγγελματίας παίκτρια esports (StarCraft)",
        "distractors": ["Μηχανικός ρομποτικής", "Πιλότος μαχητικών αεροσκαφών", "Ηθοποιός δράσης"],
        "explanation": "Η D.Va ήταν παγκόσμια πρωταθλήτρια στα esports και επελέγη από τον στρατό της Νότιας Κορέας επειδή τα εξαιρετικά της αντανακλαστικά ήταν ιδανικά για τον χειρισμό των ρομπότ MEKA.",
        "funFacts": [
            "Η διάσημη ιαχή της όταν πυροδοτεί την αυτοκαταστροφή του ρομπότ είναι: 'Nerf this!'.",
            "Όταν το MEKA καταστραφεί, η D.Va εκτινάσσεται έξω με ένα απλό πιστόλι λέιζερ μέχρι να καλέσει νέο ρομπότ."
        ],
        "source": "https://en.wikipedia.org/wiki/D.Va",
        "tags": ["gaming", "overwatch", "blizzard", "dva", "characters"]
    },
    {
        "id": "gaming_med_241",
        "text": "Ποιο είναι το όνομα του αρχαίου βασιλείου εντόμων στο οποίο εξελίσσεται το αριστουργηματικό Metroidvania 'Hollow Knight' (2017);",
        "correct": "Hallownest",
        "distractors": ["Pharloom", "Deepnest", "Dirtmouth"],
        "explanation": "Το Hallownest είναι ένα απέραντο, ερειπωμένο υπόγειο βασίλειο εντόμων που έπεσε θύμα μιας μυστηριώδους πορτοκαλί λοίμωξης (Infection) προερχόμενης από τη θεότητα The Radiance.",
        "funFacts": [
            "Το παιχνίδι αναπτύχθηκε από μια μικρή ανεξάρτητη ομάδα μόλις τριών ατόμων στην Αυστραλία, την Team Cherry, μέσω καμπάνιας στο Kickstarter.",
            "Το βασικό όπλο του πρωταγωνιστή ιππότη είναι ένα καρφί (Nail) που λειτουργεί σαν σπαθί."
        ],
        "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
        "tags": ["gaming", "hollow_knight", "team_cherry", "indie", "metroidvania"]
    },
    {
        "id": "gaming_med_242",
        "text": "Ποιο είναι το όνομα της νεαρής κοπέλας που παλεύει με το άγχος και τις κρίσεις πανικού καθώς σκαρφαλώνει ένα βουνό στο platformer 'Celeste' (2018);",
        "correct": "Madeline",
        "distractors": ["Badeline", "Theo", "Granny"],
        "explanation": "Η Madeline προσπαθεί να κατακτήσει την κορυφή του όρους Celeste, αντιμετωπίζοντας τις αμφιβολίες της και τη σκοτεινή εκδοχή του εαυτού της (Badeline / Part of Me).",
        "funFacts": [
            "Η δημιουργός Maddy Thorson χρησιμοποίησε το παιχνίδι για να αποτυπώσει τις προσωπικές της εμπειρίες με την κατάθλιψη και τη μετάβαση φύλου.",
            "Το παιχνίδι εισήγαγε έναν πρωτοποριακό μηχανισμό 'Assist Mode' που επιτρέπει σε οποιονδήποτε παίκτη να προσαρμόσει τη δυσκολία χωρίς να τιμωρείται."
        ],
        "source": "https://en.wikipedia.org/wiki/Celeste_(video_game)",
        "tags": ["gaming", "celeste", "indie", "platformer"]
    },
    {
        "id": "gaming_med_243",
        "text": "Ποιος είναι ο γιος του Άδη και πρίγκιπας του Κάτω Κόσμου που προσπαθεί διαρκώς να αποδράσει στο βραβευμένο roguelike 'Hades' (2020);",
        "correct": "Zagreus (Ζαγρέας)",
        "distractors": ["Thanatos", "Charon", "Achilles"],
        "explanation": "Ο Zagreus ανακαλύπτει ότι η μητέρα του δεν είναι η Nyx αλλά η Περσεφόνη, και ξεκινά αμέτρητες προσπάθειες απόδρασης στην επιφάνεια με τη βοήθεια των Ολύμπιων θεών.",
        "funFacts": [
            "Κάθε φορά που ο Zagreus πεθαίνει, αναδύεται από μια λίμνη αίματος (Pool of Styx) πίσω στο παλάτι του πατέρα του, με τους χαρακτήρες να σχολιάζουν τον θάνατό του.",
            "Το Hades έγινε το πρώτο βιντεοπαιχνίδι στην ιστορία που απέσπασε το διάσημο λογοτεχνικό βραβείο Hugo Award."
        ],
        "source": "https://en.wikipedia.org/wiki/Hades_(video_game)",
        "tags": ["gaming", "hades", "supergiant_games", "roguelike", "mythology"]
    },
    {
        "id": "gaming_med_244",
        "text": "Στο φιλοσοφικό RPG 'Disco Elysium' (2019), σε ποια παρακμιακή συνοικία της πόλης Revachol ξυπνά ο αμνησιακός ντετέκτιβ μετά από ολονύκτιο μεθύσι;",
        "correct": "Martinaise",
        "distractors": ["Jamrock", "Faubourg", "Coal City"],
        "explanation": "Ο ντετέκτιβ Harrier 'Harry' Du Bois ξυπνά στο ξενοδοχείο Whirling-in-Rags στο Martinaise χωρίς να θυμάται ούτε το όνομά του, κληθείς να εξιχνιάσει έναν απαγχονισμό.",
        "funFacts": [
            "Ο πιστός συνεργάτης του που τον βοηθά να παραμείνει συγκεντρωμένος είναι ο υπολοχαγός Kim Kitsuragi.",
            "Το παιχνίδι δεν περιέχει παραδοσιακό σύστημα μάχης· όλες οι συγκρούσεις και ανακρίσεις επιλύονται μέσω διαλόγων και 24 εσωτερικών φωνών/δεξιοτήτων του μυαλού του Harry."
        ],
        "source": "https://en.wikipedia.org/wiki/Disco_Elysium",
        "tags": ["gaming", "disco_elysium", "zaum", "rpg"]
    },
    {
        "id": "gaming_med_245",
        "text": "Πόσο διαρκεί ο χρονικός βρόχος στο διαστημικό παιχνίδι εξερεύνησης 'Outer Wilds' (2019) πριν ο ήλιος εκραγεί σε σουπερνόβα;",
        "correct": "22 λεπτά",
        "distractors": ["15 λεπτά", "30 λεπτά", "60 λεπτά"],
        "explanation": "Ο παίκτης είναι ένας αστροναύτης των Hearthians που παγιδεύεται σε έναν βρόχο 22 λεπτών, εξερευνώντας τα ερείπια του αρχαίου εξωγήινου πολιτισμού των Nomai.",
        "funFacts": [
            "Ολόκληρο το ηλιακό σύστημα του παιχνιδιού προσομοιώνεται σε πραγματικό χρόνο με πλήρη φυσική βαρύτητας του Νεύτωνα για όλους τους πλανήτες ταυτόχρονα.",
            "Το παιχνίδι κέρδισε το βραβείο Best Game στα British Academy Games Awards (BAFTA) το 2020."
        ],
        "source": "https://en.wikipedia.org/wiki/Outer_Wilds",
        "tags": ["gaming", "outer_wilds", "mobius_digital", "indie", "sci_fi"]
    },
    {
        "id": "gaming_med_246",
        "text": "Στο 'NieR: Automata' (2017) του Yoko Taro, ποιο ανδροειδές μάχης YoRHa με κοντά λευκά μαλλιά και μαύρο επίδεσμο στα μάτια είναι η βασική πρωταγωνίστρια;",
        "correct": "2B (YoRHa No. 2 Type B)",
        "distractors": ["9S (YoRHa No. 9 Type S)", "A2 (YoRHa Type A No. 2)", "Commander White"],
        "explanation": "Η 2B μάχεται ενάντια σε μηχανές που έχουν καταλάβει τη Γη συνοδευόμενη από το ανδροειδές αναγνώρισης 9S και ένα αιωρούμενο Pod υποστήριξης.",
        "funFacts": [
            "Για να δει ο παίκτης την πραγματική ολοκλήρωση της ιστορίας, απαιτείται να τερματίσει το παιχνίδι πολλαπλές φορές ξεκλειδώνοντας τα τέλη A έως E.",
            "Στο τέλος E, οι παίκτες καλούνται να θυσιάσουν τα δικά τους αποθηκευμένα αρχεία προόδου (save data) για να βοηθήσουν έναν άγνωστο παίκτη κάπου στον κόσμο."
        ],
        "source": "https://en.wikipedia.org/wiki/Nier:_Automata",
        "tags": ["gaming", "nier_automata", "square_enix", "platinumgames", "yoko_taro"]
    },
    {
        "id": "gaming_med_247",
        "text": "Ποια κακόβουλη τεχνητή νοημοσύνη με αλλοιωμένη γυναικεία φωνή αποκαλεί τους ανθρώπους 'έντομα' στη σειρά 'System Shock';",
        "correct": "SHODAN",
        "distractors": ["GLaDOS", "Cortana", "Mother Brain"],
        "explanation": "Η SHODAN (Sentient Hyper-Optimized Data Access Network) απαλλάσσεται από τους ηθικούς περιορισμούς της και αυτοανακηρύσσεται θεά, τρομοκρατώντας τον σταθμό Citadel.",
        "funFacts": [
            "Η διάσημη ατάκα της είναι: 'Look at you, hacker: a pathetic creature of meat and bone, panting and sweating as you run through my corridors'.",
            "Η SHODAN αποτέλεσε την κύρια πηγή έμπνευσης για τη δημιουργία της GLaDOS στη σειρά Portal."
        ],
        "source": "https://en.wikipedia.org/wiki/SHODAN",
        "tags": ["gaming", "system_shock", "looking_glass", "shodan", "sci_fi"]
    },
    {
        "id": "gaming_med_248",
        "text": "Ποιο καινοτόμο αξεσουάρ κάρτας μνήμης της κονσόλας Sega Dreamcast (1998) διέθετε δική του μονόχρωμη οθόνη LCD, κουμπιά και μίνι παιχνίδια;",
        "correct": "VMU (Visual Memory Unit)",
        "distractors": ["PocketStation", "Controller Pak", "Memory Card Plus"],
        "explanation": "Το VMU κουμπωνε απευθείας μέσα στο χειριστήριο του Dreamcast και μπορούσε να εμφανίζει μυστικές πληροφορίες (όπως το σύστημα υγείας στο Resident Evil) ή να λειτουργεί αυτόνομα ως μίνι κονσόλα.",
        "funFacts": [
            "Στο NFL 2K, οι παίκτες μπορούσαν να διαλέγουν τις τακτικές τους κρυφά στην οθόνη του VMU ώστε να μην τις βλέπει ο αντίπαλος στην τηλεόραση.",
            "Όταν η μπαταρία του VMU τελείωνε, έβγαζε έναν χαρακτηριστικό διαπεραστικό ήχο 'μπιπ' κατά την εκκίνηση της κονσόλας."
        ],
        "source": "https://en.wikipedia.org/wiki/VMU",
        "tags": ["gaming", "sega", "dreamcast", "hardware", "vmu"]
    },
    {
        "id": "gaming_med_249",
        "text": "Ποιο είναι το όνομα της κακιάς πράσινης μάγισσας που απαγάγει τη μικρή Tooty στο κλασικό 3D platformer 'Banjo-Kazooie' (1998) της Rare;",
        "correct": "Gruntilda Winkybunion",
        "distractors": ["Humba Wumba", "Madame Flurrie", "Syrup"],
        "explanation": "Η Gruntilda θέλει να κλέψει την ομορφιά της αδελφής του Banjo χρησιμοποιώντας μια ειδική μηχανή και μιλάει αποκλειστικά κάνοντας ομοιοκαταληξίες.",
        "funFacts": [
            "Ο Banjo είναι μια καλόκαρδη αρκούδα και η Kazooie είναι ένα κόκκινο πουλί με κοφτερή γλώσσα που ζει μέσα στο σακίδιο της πλάτης του.",
            "Τα βασικά συλλεκτικά αντικείμενα για το ξεκλείδωμα νέων κόσμων στο παιχνίδι είναι τα χρυσά κομμάτια παζλ (Jiggies)."
        ],
        "source": "https://en.wikipedia.org/wiki/Banjo-Kazooie",
        "tags": ["gaming", "banjo_kazooie", "rare", "n64", "nintendo"]
    },
    {
        "id": "gaming_med_250",
        "text": "Ποιος είναι ο διάσημος Ιάπωνας συνθέτης που δημιούργησε τα εμβληματικά soundtracks των κλασικών παιχνιδιών 'Final Fantasy' από το 1 έως το X;",
        "correct": "Nobuo Uematsu",
        "distractors": ["Koji Kondo", "Yasunori Mitsuda", "Yoko Shimomura"],
        "explanation": "Ο Nobuo Uematsu θεωρείται ο 'Μπετόβεν των βιντεοπαιχνιδιών', έχοντας γράψει θρυλικά κομμάτια όπως το 'One-Winged Angel', το 'To Zanarkand' και το 'Aerith's Theme'.",
        "funFacts": [
            "Ο Uematsu δεν είχε επίσημη κλασική εκπαίδευση στη μουσική και έμαθε να παίζει πιάνο μόνος του ακούγοντας Elton John και progressive rock.",
            "Το 'Eyes on Me' από το Final Fantasy VIII (ερμηνευμένο από τη Faye Wong) έγινε το πρώτο τραγούδι από βιντεοπαιχνίδι που κέρδισε το βραβείο Song of the Year στα Japan Gold Disc Awards."
        ],
        "source": "https://en.wikipedia.org/wiki/Nobuo_Uematsu",
        "tags": ["gaming", "final_fantasy", "square_enix", "nobuo_uematsu", "music"]
    },
    {
        "id": "gaming_med_251",
        "text": "Στο stealth παιχνίδι 'Dishonored' (2012) της Arkane Studios, σε ποια φανταστική πόλη που τροφοδοτείται από λάδι φάλαινας διαδραματίζεται η ιστορία;",
        "correct": "Dunwall",
        "distractors": ["Karnaca", "Karnak", "Gristol"],
        "explanation": "Η Dunwall είναι μια βιομηχανική φαλαινοθηρική πόλη που μαστίζεται από θανατηφόρα πανώλη αρουραίων, όπου ο σωματοφύλακας Corvo Attano κατηγορείται άδικα για τη δολοφονία της Αυτοκράτειρας.",
        "funFacts": [
            "Ο Corvo αποκτά υπερφυσικές δυνάμεις (όπως τηλεμεταφορά Blink και κατοχή ζώων) από τη μυστηριώδη θεότητα The Outsider.",
            "Το παιχνίδι μπορεί να ολοκληρωθεί εντελώς χωρίς να σκοτωθεί ούτε ένας άνθρωπος, ξεκλειδώνοντας το επίτευγμα 'Clean Hands' και το Low Chaos τέλος."
        ],
        "source": "https://en.wikipedia.org/wiki/Dishonored",
        "tags": ["gaming", "dishonored", "arkane", "bethesda", "stealth"]
    },
    {
        "id": "gaming_med_252",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή της σειράς 'Dead Rising' της Capcom, ενός φωτορεπόρτερ που έχει καλύψει πολέμους και μάχεται με ζόμπι σε ένα εμπορικό κέντρο;",
        "correct": "Frank West",
        "distractors": ["Chuck Greene", "Nick Ramos", "Brad Garrison"],
        "explanation": "Ο Frank West φτάνει με ελικόπτερο στο εμπορικό κέντρο Willamette στο Κολοράντο λέγοντας τη χαρακτηριστική φράση: 'I've covered wars, ya know!'.",
        "funFacts": [
            "Οι παίκτες έχουν αυστηρό χρονικό περιθώριο 72 ωρών εντός παιχνιδιού για να ανακαλύψουν την αλήθεια πριν φτάσει το ελικόπτερο διάσωσης.",
            "Ο Frank μπορεί να χρησιμοποιήσει σχεδόν οτιδήποτε ως όπλο, από καρέκλες και κιθάρες μέχρι παιχνιδομηχανές και κουλοχέρηδες."
        ],
        "source": "https://en.wikipedia.org/wiki/Dead_Rising",
        "tags": ["gaming", "dead_rising", "capcom", "frank_west", "zombies"]
    },
    {
        "id": "gaming_med_253",
        "text": "Στη σειρά 'Fallout', ποιος είναι ο αριθμός του υπόγειου καταφυγίου (Vault) από το οποίο ξεκινά ο παίκτης στο ιστορικό πρώτο 'Fallout' (1997);",
        "correct": "Vault 13",
        "distractors": ["Vault 101", "Vault 111", "Vault 76"],
        "explanation": "Στο αρχικό Fallout, ο Vault Dweller στέλνεται στον ερημότοπο από τον επιβλέποντα του Vault 13 για να βρει ένα ανταλλακτικό Water Chip πριν στερέψει το νερό.",
        "funFacts": [
            "Στο Fallout 3 ο παίκτης ξεκινά από το Vault 101 στην Ουάσινγκτον, ενώ στο Fallout 4 από το Vault 111 στη Βοστώνη.",
            "Το Vault 13 στο Fallout 2 αποκαλύπτεται ότι καταλήφθηκε από νοήμονα, εξημερωμένα Deathclaws."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout_(video_game)",
        "tags": ["gaming", "fallout", "interplay", "rpg", "vault"]
    },
    {
        "id": "gaming_med_254",
        "text": "Ποιο ιστορικό point-and-click adventure της LucasArts (1990) από τον Ron Gilbert ακολουθεί τον νεαρό Guybrush Threepwood στην προσπάθειά του να γίνει πειρατής;",
        "correct": "The Secret of Monkey Island",
        "distractors": ["Monkey Island 2: LeChuck's Revenge", "Day of the Tentacle", "Grim Fandango"],
        "explanation": "Ο Guybrush Threepwood φτάνει στο Mêlée Island και πρέπει να περάσει τις Τρεις Δοκιμασίες των Πειρατών και να αντιμετωπίσει τον ζωντανό-νεκρό καπετάνιο LeChuck.",
        "funFacts": [
            "Οι μονομαχίες με σπαθιά στο Monkey Island (Insult Sword Fighting) κερδίζονται αποκλειστικά ανταλλάσσοντας ευφυείς προσβολές και αποστομωτικές απαντήσεις.",
            "Ο Guybrush μπορεί να κρατήσει την αναπνοή του κάτω από το νερό για ακριβώς 10 λεπτά."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Secret_of_Monkey_Island",
        "tags": ["gaming", "monkey_island", "lucasarts", "ron_gilbert", "adventure"]
    },
    {
        "id": "gaming_med_255",
        "text": "Ποιο είναι το όνομα του πράκτορα ταξιδιών στον Κάτω Κόσμο και σκελετωμένου πρωταγωνιστή του αριστουργήματος 'Grim Fandango' (1998) της LucasArts;",
        "correct": "Manuel 'Manny' Calavera",
        "distractors": ["Hector LeMans", "Glottis", "Salvador Limones"],
        "explanation": "Ο Manny Calavera εργάζεται στο Department of Death πουλώντας ταξιδιωτικά πακέτα στις ψυχές, αντλώντας έμπνευση από τη μεξικανική Ημέρα των Νεκρών (Día de los Muertos) και το film noir.",
        "funFacts": [
            "Το Grim Fandango σχεδιάστηκε από τον Tim Schafer και ήταν το πρώτο adventure της LucasArts που χρησιμοποίησε 3D πολυγωνικά μοντέλα χαρακτήρων.",
            "Το απόλυτο πολυτελές τρένο για το ταξίδι τεσσάρων ετών στον Ένατο Κόσμο ονομάζεται Number Nine."
        ],
        "source": "https://en.wikipedia.org/wiki/Grim_Fandango",
        "tags": ["gaming", "grim_fandango", "lucasarts", "tim_schafer", "adventure"]
    },
    {
        "id": "gaming_med_256",
        "text": "Στο 'Portal 2', ποιο είναι το όνομα του εκπαιδευτικού συνεργατικού διδύμου ρομπότ (Co-op) που ελέγχουν οι δύο παίκτες στις δοκιμασίες της GLaDOS;",
        "correct": "Atlas και P-Body",
        "distractors": ["Claptrap και Steve", "Ratchet και Clank", "Jak και Daxter"],
        "explanation": "Ο Atlas (ένας στρογγυλός πυρήνας) και ο P-Body (ένα μακρόστενο turret) είναι δύο ρομπότ εξοπλισμένα με Portal Guns που δεν πεθαίνουν ποτέ οριστικά αφού επανασυναρμολογούνται.",
        "funFacts": [
            "Η GLaDOS συχνά προσπαθεί να σπείρει τη διχόνοια μεταξύ των δύο ρομπότ βαθμολογώντας τη συνεργασία τους ή ψιθυρίζοντας ότι το ένα είναι καλύτερο από το άλλο.",
            "Τα δύο ρομπότ έχουν δεκάδες κωμικά emotes, όπως αγκαλιές, κόλλες πέντε και πέτρα-ψαλίδι-χαρτί."
        ],
        "source": "https://en.wikipedia.org/wiki/Portal_2",
        "tags": ["gaming", "portal", "valve", "coop"]
    },
    {
        "id": "gaming_med_257",
        "text": "Ποιο είναι το όνομα του εκκεντρικού Ιάπωνα δημιουργού παιχνιδιών πίσω από σειρές όπως το 'Metal Gear' και το 'Death Stranding';",
        "correct": "Hideo Kojima",
        "distractors": ["Shinji Mikami", "Hideki Kamiya", "Goichi Suda (Suda51)"],
        "explanation": "Ο Hideo Kojima είναι διεθνώς αναγνωρισμένος για το κινηματογραφικό του στυλ, τα περίπλοκα σενάρια και το σπάσιμο του τέταρτου τοίχου στα βιντεοπαιχνίδια.",
        "funFacts": [
            "Μετά την αποχώρησή του από την Konami το 2015, ίδρυσε το ανεξάρτητο στούντιο Kojima Productions με μασκότ τον Ludens.",
            "Στο Death Stranding (2019), ο Norman Reedus πρωταγωνιστεί ως Sam Porter Bridges συνδέοντας έναν απομονωμένο κόσμο μεταφέροντας φορτία."
        ],
        "source": "https://en.wikipedia.org/wiki/Hideo_Kojima",
        "tags": ["gaming", "hideo_kojima", "metal_gear", "death_stranding", "creators"]
    },
    {
        "id": "gaming_med_258",
        "text": "Στο 'Resident Evil' (1996), ποια είναι τα δύο αρχικά μέλη της ομάδας Alpha της S.T.A.R.S. που μπορεί να επιλέξει ο παίκτης ως πρωταγωνιστή;",
        "correct": "Chris Redfield και Jill Valentine",
        "distractors": ["Leon Kennedy και Claire Redfield", "Barry Burton και Rebecca Chambers", "Albert Wesker και Brad Vickers"],
        "explanation": "Ο Chris Redfield έχει περισσότερη αντοχή αλλά λιγότερες θέσεις απογραφής (inventory), ενώ η Jill Valentine διαθέτει αντικλείδι (lockpick) και 8 θέσεις αντικειμένων.",
        "funFacts": [
            "Ο Barry Burton λέει στην Jill τη διαβόητη ατάκα: 'You were almost a Jill sandwich!' όταν τη σώζει από το ταβάνι που κατέβαινε να την πλακώσει.",
            "Το παιχνίδι σκηνοθετήθηκε από τον Shinji Mikami, ο οποίος εμπνεύστηκε από το κλασικό παιχνίδι τρόμου Sweet Home (1989) της Capcom."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_(video_game)",
        "tags": ["gaming", "resident_evil", "capcom", "survival_horror", "characters"]
    },
    {
        "id": "gaming_med_259",
        "text": "Ποιος είναι ο σχεδιαστής και δημιουργός του πρωτοποριακού puzzle game 'Braid' (2008) που πυροδότησε την επανάσταση των ανεξάρτητων indie παιχνιδιών;",
        "correct": "Jonathan Blow",
        "distractors": ["Edmund McMillen", "Phil Fish", "Derek Yu"],
        "explanation": "Ο Jonathan Blow ανέπτυξε το Braid, ένα platformer χειρισμού χρόνου, και αργότερα το εξαιρετικά πολύπλοκο παιχνίδι γρίφων 'The Witness' (2016).",
        "funFacts": [
            "Ο Blow πρωταγωνίστησε στο διάσημο ντοκιμαντέρ 'Indie Game: The Movie' (2012) μαζί με τους δημιουργούς των Super Meat Boy και Fez.",
            "Το τέλος του Braid αποκαλύπτει μια συγκλονιστική αντιστροφή ρόλων όπου ο ήρωας Tim δεν προσπαθεί να σώσει την πριγκίπισσα, αλλά την καταδιώκει."
        ],
        "source": "https://en.wikipedia.org/wiki/Braid_(video_game)",
        "tags": ["gaming", "braid", "indie", "jonathan_blow", "puzzle"]
    },
    {
        "id": "gaming_med_260",
        "text": "Ποιο είναι το όνομα του κομματιού κρέατος χωρίς δέρμα που προσπαθεί να σώσει την Bandage Girl από τον Dr. Fetus στο platformer 'Super Meat Boy' (2010);",
        "correct": "Meat Boy",
        "distractors": ["Isaac", "Spelunky Guy", "Commander Video"],
        "explanation": "Το Super Meat Boy δημιουργήθηκε από την Team Meat (Edmund McMillen και Tommy Refenes) και έγινε διάσημο για την ακραία δυσκολία του και τον ταχύτατο ρυθμό επανεκκίνησης.",
        "funFacts": [
            "Όταν ο παίκτης ολοκληρώνει μια πίστα, εμφανίζεται ένα replay που δείχνει ταυτόχρονα όλες τις δεκάδες αποτυχημένες προσπάθειες και θανάτους του.",
            "Ο Edmund McMillen δημιούργησε επίσης το εξαιρετικά δημοφιλές roguelike 'The Binding of Isaac'."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Meat_Boy",
        "tags": ["gaming", "super_meat_boy", "indie", "platformer"]
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
        "difficulty": 3,
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
    print(f"Loaded {len(questions)} questions for gaming_medium batch 1.")
    validate_and_append("gaming", "medium", 3, questions)

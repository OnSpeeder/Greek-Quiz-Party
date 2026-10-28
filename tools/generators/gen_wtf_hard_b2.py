import sys
from base_generator import validate_and_append

# Ensure stdout handles UTF-8 on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Batch 2: IDs wtf_facts_hard_261 to wtf_facts_hard_310 (50 questions)
# Difficulty = 5, Category = wtf_facts
questions = [
    {
        "id": "wtf_facts_hard_261",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο υποθετικό είδος ύλης αποτελείται από πάνω, κάτω και παράδοξα κουάρκ και πιστεύεται ότι μπορεί να είναι πιο σταθερό από την κανονική πυρηνική ύλη;",
        "answers": ["Παράξενη ύλη (Strange matter)", "Σκοτεινή ύλη", "Αντιύλη", "Υπεραγώγιμη ύλη"],
        "correctAnswerIndex": 0,
        "explanation": "Η παράξενη ύλη (strange matter) υποτίθεται ότι περιέχει σχεδόν ίσο αριθμό από πάνω, κάτω και παράδοξα κουάρκ και σύμφωνα με την υπόθεση Bodmer-Witten ίσως είναι η πραγματική θεμελιώδης κατάσταση της ύλης.",
        "funFacts": [
            "Μικρές ποσότητες αυτής της ύλης ονομάζονται παράξενα σωματίδια ή strangelets.",
            "Αν ένα strangelet συγκρουστεί με κανονικό πυρήνα, υποθετικά θα μπορούσε να τον μετατρέψει επίσης σε παράξενη ύλη."
        ],
        "source": "https://en.wikipedia.org/wiki/Strange_matter",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "physics", "quantum_mechanics"]
    },
    {
        "id": "wtf_facts_hard_262",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Πώς ονομάζεται στην αστροφυσική η υπερπυκνή δομή ύλης στο εσωτερικό των αστέρων νετρονίων που σχηματίζει σχήματα σαν μακαρόνια ή λαζάνια;",
        "answers": ["Κβαντικό υγρό", "Πυρηνικά ζυμαρικά (Nuclear pasta)", "Πλάσμα κουάρκ", "Βαρυτικός κρύσταλλος"],
        "correctAnswerIndex": 1,
        "explanation": "Τα πυρηνικά ζυμαρικά (nuclear pasta) είναι θεωρητικός τύπος εκφυλισμένης ύλης στον φλοιό των αστέρων νετρονίων, όπου οι έντονες δυνάμεις σχηματίζουν επίπεδα ή ραβδοειδή σχήματα που μοιάζουν με ζυμαρικά.",
        "funFacts": [
            "Θεωρούνται ένα από τα σκληρότερα υλικά στο σύμπαν, με μέτρο ελαστικότητας δισεκατομμύρια φορές μεγαλύτερο από του χάλυβα.",
            "Οι αστροφυσικοί χρησιμοποιούν ονόματα όπως 'gnocchi', 'spaghetti' και 'lasagna' για τις διάφορες φάσεις συμπίεσης."
        ],
        "source": "https://en.wikipedia.org/wiki/Nuclear_pasta",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astrophysics", "neutron_stars"]
    },
    {
        "id": "wtf_facts_hard_263",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο βαρύ στοιχείο με ατομικό αριθμό 118 προβλέπεται ότι δεν έχει ευδιάκριτους ηλεκτρονιακούς φλοιούς λόγω σχετικιστικών επιδράσεων;",
        "answers": ["Τενέσιο", "Μοσκόβιο", "Νιχόνιο", "Ογκανέσσιο"],
        "correctAnswerIndex": 3,
        "explanation": "Στο ογκανέσσιο (στοιχείο 118), τα ηλεκτρόνια κινούνται με ταχύτητες κοντά στο φως, με αποτέλεσμα οι ηλεκτρονιακοί φλοιοί να επεκτείνονται και να εμφανίζονται σχεδόν ομοιόμορφα κατανεμημένοι σαν 'αέριο Thomas-Fermi'.",
        "funFacts": [
            "Αν και ανήκει στα ευγενή αέρια, προβλέπεται ότι σε θερμοκρασία δωματίου είναι στερεό.",
            "Είναι το βαρύτερο στοιχείο που έχει συντεθεί επιτυχώς έως σήμερα."
        ],
        "source": "https://en.wikipedia.org/wiki/Oganesson",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "chemistry", "elements"]
    },
    {
        "id": "wtf_facts_hard_264",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο μυστικό στρατιωτικό πρόγραμμα των ΗΠΑ της δεκαετίας του 1950 στόχευε στην κατασκευή ενός πυρηνοκίνητου πυραύλου κρουζ χαμηλού ύψους (SLAM);",
        "answers": ["Project Rover", "Project Pluto", "Project Orion", "Project Timberwind"],
        "correctAnswerIndex": 1,
        "explanation": "Το Project Pluto ανέπτυξε τον κινητήρα Tory-IIC, έναν πυρηνικό αυλοωθητή (ramjet) χωρίς θωράκιση, σχεδιασμένο να πετά με Mach 3 σε χαμηλό ύψος διασκορπίζοντας ραδιενέργεια και ωστικά κύματα.",
        "funFacts": [
            "Ο πύραυλος θα προκαλούσε ανυπολόγιστες ζημιές απλώς περνώντας πάνω από κατοικημένες περιοχές λόγω του υπερηχητικού ωστικού κύματος.",
            "Το πρόγραμμα ακυρώθηκε το 1964 μετά την επιτυχή ανάπτυξη των διηπειρωτικών βαλλιστικών πυραύλων (ICBM)."
        ],
        "source": "https://en.wikipedia.org/wiki/Project_Pluto",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "military_history", "nuclear"]
    },
    {
        "id": "wtf_facts_hard_265",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο ιαπωνικό αλιευτικό σκάφος εκτέθηκε σε θανατηφόρα ραδιενεργό τέφρα μετά την πυρηνική δοκιμή Castle Bravo στο Μπικίνι το 1954;",
        "answers": ["Daigo Fukuryu Maru", "Taiyo Maru", "Shinano Maru", "Ryusei Maru"],
        "correctAnswerIndex": 0,
        "explanation": "Το Daigo Fukuryu Maru ('Τυχερός Δράκος Νο. 5') βρισκόταν εκτός της επίσημης ζώνης κινδύνου, αλλά η έκρηξη ήταν 2,5 φορές ισχυρότερη από το αναμενόμενο (15 μεγατόνοι αντί για 6), ρυπαίνοντας το πλήρωμα με ραδιενέργεια.",
        "funFacts": [
            "Ο ασυρματιστής Aikichi Kuboyama πέθανε λίγους μήνες αργότερα, προκαλώντας τεράστιο κύμα αντιπυρηνικών διαδηλώσεων στην Ιαπωνία.",
            "Το περιστατικό αποτέλεσε μία από τις κύριες εμπνεύσεις για τη δημιουργία της ταινίας 'Godzilla' το 1954."
        ],
        "source": "https://en.wikipedia.org/wiki/Daigo_Fukury%C5%AB_Maru",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "nuclear_history", "japan"]
    },
    {
        "id": "wtf_facts_hard_266",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Σε ποιο πολυτελές ξενοδοχείο της Δυτικής Βιρτζίνια κατασκευάστηκε μυστικό υπόγειο καταφύγιο για το Κογκρέσο των ΗΠΑ (Project Greek Island);",
        "answers": ["The Breakers", "The Greenbrier", "Waldorf Astoria", "The Broadmoor"],
        "correctAnswerIndex": 1,
        "explanation": "Το Project Greek Island ήταν ένα τεράστιο υπόγειο καταφύγιο σκαμμένο κάτω από το ξενοδοχείο The Greenbrier, σχεδιασμένο να στεγάσει ολόκληρο το Κογκρέσο σε περίπτωση πυρηνικού πολέμου.",
        "funFacts": [
            "Το καταφύγιο παρέμεινε ενεργό και πλήρως εξοπλισμένο για πάνω από 30 χρόνια υπό άκρα μυστικότητα.",
            "Αποκαλύφθηκε το 1992 από άρθρο της Washington Post, οδηγώντας στον άμεσο παροπλισμό του."
        ],
        "source": "https://en.wikipedia.org/wiki/Project_Greek_Island",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "cold_war", "bunkers"]
    },
    {
        "id": "wtf_facts_hard_267",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το βαθύτερο γνωστό υποβρύχιο σπήλαιο (καταβόθρα) στον κόσμο, με βάθος τουλάχιστον 450 μέτρων;",
        "answers": ["Hranice Abyss", "Dean's Blue Hole", "Dragon Hole", "Great Blue Hole"],
        "correctAnswerIndex": 0,
        "explanation": "Το Hranice Abyss στην Τσεχία επιβεβαιώθηκε το 2020 ότι εκτείνεται σε βάθος τουλάχιστον 450 μέτρων (πιθανόν έως και 1.000 μ.), καθιστώντας το το βαθύτερο πλημμυρισμένο σπήλαιο στον πλανήτη.",
        "funFacts": [
            "Το 2016 ένα τηλεκατευθυνόμενο υποβρύχιο όχημα (ROV) έφτασε στα 404 μέτρα πριν τελειώσει το καλώδιο του.",
            "Το νερό του σπηλαίου είναι κορεσμένο με διοξείδιο του άνθρακα, καθιστώντας το ελαφρώς όξινο."
        ],
        "source": "https://en.wikipedia.org/wiki/Hranice_Abyss",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "geography", "caves"]
    },
    {
        "id": "wtf_facts_hard_268",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο ήταν το πρώτο συνθετικό νανοϋλικό που κατείχε το ρεκόρ της χαμηλότερης πυκνότητας για στερεό σώμα, όντας κατά 99,8% αέρας;",
        "answers": ["Αεροπήκτωμα (Aerogel)", "Γραφένιο", "Νανοσωλήνες άνθρακα", "Ζεόλιθος"],
        "correctAnswerIndex": 0,
        "explanation": "Το πυριτικό αεροπήκτωμα (aerogel), γνωστό και ως 'παγωμένος καπνός', δημιουργήθηκε από τον Samuel Kistler το 1931 και αποτελείται σχεδόν εξ ολοκλήρου από αέρα, παρέχοντας εκπληκτική θερμομόνωση.",
        "funFacts": [
            "Χρησιμοποιήθηκε από τη NASA στην αποστολή Stardust για τη σύλληψη σωματιδίων από την ουρά του κομήτη Wild 2 χωρίς να καταστραφούν.",
            "Ένα κομμάτι αερογέλης μπορεί να αντέξει βάρος χιλιάδες φορές μεγαλύτερο από το δικό του."
        ],
        "source": "https://en.wikipedia.org/wiki/Aerogel",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "materials_science", "chemistry"]
    },
    {
        "id": "wtf_facts_hard_269",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος ερασιτέχνης εφευρέτης δημιούργησε το μυστηριώδες θερμοανθεκτικό υλικό 'Starlite' που άντεχε θερμοκρασίες πυρηνικής έκρηξης αλλά δεν αποκάλυψε ποτέ τη συνταγή;",
        "answers": ["Maurice Ward", "Troy Hurtubise", "Thomas Townsend Brown", "John Hutchison"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Maurice Ward, ένας πρώην κομμωτής από το Γιορκσάιρ, επινόησε το 'Starlite' τη δεκαετία του 1980. Το υλικό μπορούσε να αντέξει θερμοκρασίες άνω των 10.000 °C και δέσμες λέιζερ χωρίς να καεί.",
        "funFacts": [
            "Σε διάσημη επίδειξη στο BBC, ένα αυγό καλυμμένο με Starlite έμεινε άθικτο και ωμό κάτω από φλόγα οξυγονοκόλλησης για λεπτά.",
            "Ο Ward αρνήθηκε να πουλήσει τη φόρμουλα σε μεγάλες αεροδιαστημικές εταιρείες επειδή ζητούσε ποσοστό 51% και πέθανε το 2011 παίρνοντας το μυστικό μαζί του."
        ],
        "source": "https://en.wikipedia.org/wiki/Starlite",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "materials_science", "inventions"]
    },
    {
        "id": "wtf_facts_hard_270",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο φαινόμενο της κβαντικής φυσικής περιγράφει την παραγωγή πραγματικών φωτονίων από το κενό λόγω επιταχυνόμενου καθρέφτη;",
        "answers": ["Δυναμικό φαινόμενο Casimir", "Φαινόμενο Meissner", "Φαινόμενο Aharonov-Bohm", "Φαινόμενο Kondo"],
        "correctAnswerIndex": 0,
        "explanation": "Στο δυναμικό φαινόμενο Casimir (dynamical Casimir effect), τα όρια του κενού που κινούνται με σχετικιστικές ταχύτητες μετατρέπουν τα εικονικά σωματίδια του κβαντικού κενού σε πραγματικά παρατηρήσιμα φωτόνια.",
        "funFacts": [
            "Προβλέφθηκε θεωρητικά το 1970 και παρατηρήθηκε πειραματικά για πρώτη φορά το 2011 χρησιμοποιώντας υπεραγώγιμο κύκλωμα SQUID.",
            "Διαφέρει από το στατικό φαινόμενο Casimir, το οποίο απλώς προκαλεί ελκτική δύναμη μεταξύ ακίνητων πλακών."
        ],
        "source": "https://en.wikipedia.org/wiki/Casimir_effect#Dynamical_Casimir_effect",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "quantum_mechanics", "physics"]
    },
    {
        "id": "wtf_facts_hard_271",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο αέριο προκάλεσε την καταστροφή στο Lake Nyos του Καμερούν το 1986, σκοτώνοντας πάνω από 1.700 ανθρώπους μέσα σε λίγες ώρες;",
        "answers": ["Μονοξείδιο του άνθρακα", "Μεθάνιο", "Υδρόθειο", "Διοξείδιο του άνθρακα"],
        "correctAnswerIndex": 3,
        "explanation": "Μια λιμναία έκρηξη (limnic eruption) απελευθέρωσε ξαφνικά εκατοντάδες χιλιάδες τόνους διοξειδίου του άνθρακα (CO2) που ήταν διαλυμένοι στα βαθιά νερά της λίμνης Nyos, πνίγοντας τα γύρω χωριά.",
        "funFacts": [
            "Το σύννεφο αερίου ήταν βαρύτερο από τον αέρα και κύλησε στις κοιλάδες με ταχύτητα έως 50 χλμ/ώρα.",
            "Εγκαταστάθηκαν ειδικοί σωλήνες αποgasification που αντλούν συνεχώς νερό από τον πυθμένα για να αποτρέψουν μελλοντική συσσώρευση."
        ],
        "source": "https://en.wikipedia.org/wiki/Lake_Nyos_disaster",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "geology", "disasters"]
    },
    {
        "id": "wtf_facts_hard_272",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο χημικό στοιχείο έχει την υψηλότερη θερμοκρασία τήξης από όλα τα καθαρά στοιχεία (περίπου 3.422 °C);",
        "answers": ["Βολφράμιο", "Άνθρακας", "Ταντάλιο", "Όσμιο"],
        "correctAnswerIndex": 0,
        "explanation": "Το βολφράμιο (W) έχει το υψηλότερο σημείο τήξης από όλα τα μέταλλα και στοιχεία στους 3.422 °C (ο άνθρακας εξαχνώνεται υπό κανονική πίεση στους 3.642 °C χωρίς να λιώνει σε υγρό).",
        "funFacts": [
            "Χρησιμοποιήθηκε εκτεταμένα στα νήματα των λαμπτήρων πυρακτώσεως ακριβώς λόγω αυτής της αντοχής στη θερμότητα.",
            "Το σουηδικό του όνομα σημαίνει 'βαριά πέτρα' (tung sten)."
        ],
        "source": "https://en.wikipedia.org/wiki/Tungsten",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "chemistry", "materials"]
    },
    {
        "id": "wtf_facts_hard_273",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το ισχυρότερο υπεροξύ που έχει συντεθεί ποτέ, με οξύτητα δισεκατομμύρια φορές ισχυρότερη από το καθαρό θειικό οξύ;",
        "answers": ["Φθοροαντιμονικό οξύ", "Τριφθορομεθανοσουλφονικό οξύ", "Μαγικό οξύ", "Υπερχλωρικό οξύ"],
        "correctAnswerIndex": 0,
        "explanation": "Το φθοροαντιμονικό οξύ (HSbF6) είναι το ισχυρότερο γνωστό υπεροξύ, περίπου 2×10^19 φορές ισχυρότερο από το 100% θειικό οξύ, και μπορεί να πρωτονιώσει ακόμα και υδρογονάνθρακες.",
        "funFacts": [
            "Διαβρώνει σχεδόν τα πάντα, συμπεριλαμβανομένου του γυαλιού, και αποθηκεύεται μόνο σε ειδικά δοχεία πολυτετραφθοροαιθυλενίου (Teflon).",
            "Αντιδρά εκρηκτικά με το νερό απελευθερώνοντας εξαιρετικά τοξικά αέρια υδροφθορίου."
        ],
        "source": "https://en.wikipedia.org/wiki/Fluoroantimonic_acid",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "chemistry", "acids"]
    },
    {
        "id": "wtf_facts_hard_274",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο παράδοξο της θερμοδυναμικής διατυπώθηκε το 1867 για να αμφισβητήσει τον δεύτερο θερμοδυναμικό νόμο μέσω ενός νοητού όντος που διαχωρίζει μόρια;",
        "answers": ["Ο Δαίμονας του Laplace", "Ο Δαίμονας του Maxwell", "Η γάτα του Schrödinger", "Το παράδοξο του Fermi"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Δαίμονας του Maxwell (Maxwell's demon) είναι ένα νοητό πείραμα όπου ένα ον επιτρέπει στα ταχύτερα μόρια να περάσουν σε ένα δοχείο και στα πιο αργά στο άλλο, φαινομενικά μειώνοντας την εντροπία.",
        "funFacts": [
            "Η λύση του παραδόξου από τον Rolf Landauer έδειξε ότι η διαγραφή πληροφορίας στη μνήμη του δαίμονα αναπόφευκτα παράγει εντροπία.",
            "Αυτό συνέδεσε για πρώτη φορά άμεσα τη θεωρία πληροφορίας με τη θερμοδυναμική (Αρχή του Landauer)."
        ],
        "source": "https://en.wikipedia.org/wiki/Maxwell%27s_demon",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "physics", "thermodynamics"]
    },
    {
        "id": "wtf_facts_hard_275",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το μοναδικό γνωστό φυσικό παράδειγμα αυτοσυντηρούμενου πυρηνικού αντιδραστήρα σχάσης που λειτούργησε στη Γη πριν από 2 δισεκατομμύρια χρόνια;",
        "answers": ["Αντιδραστήρας Oklo", "Κρατήρας Chicxulub", "Ορυχείο Shinkolobwe", "Καλντέρα Toba"],
        "correctAnswerIndex": 0,
        "explanation": "Στο Oklo της Γκαμπόν, φυσικές συγκεντρώσεις ουρανίου-235 και υπόγειων υδάτων δημιούργησαν φυσικούς πυρηνικούς αντιδραστήρες που παρήγαγαν ενέργεια για εκατοντάδες χιλιάδες χρόνια.",
        "funFacts": [
            "Ανακαλύφθηκε το 1972 όταν Γάλλοι επιστήμονες διαπίστωσαν ότι το ουράνιο από το ορυχείο είχε ανεξήγητα χαμηλότερη περιεκτικότητα σε ουράνιο-235.",
            "Τα πυρηνικά απόβλητα από τη φυσική σχάση παρέμειναν εγκλωβισμένα στο πέτρωμα για δύο δισεκατομμύρια χρόνια χωρίς να διαρρεύσουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Natural_nuclear_fission_reactor",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "geology", "nuclear_physics"]
    },
    {
        "id": "wtf_facts_hard_276",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο σοβιετικό αεροσκάφος τύπου 'εκρανοπλάνο' ήταν γνωστό στις δυτικές μυστικές υπηρεσίες ως το 'Τέρας της Κασπίας';",
        "answers": ["A-90 Orlyonok", "KM (Korabl Maket)", "Bartini Beriev VVA-14", "Lun-class"],
        "correctAnswerIndex": 1,
        "explanation": "Το πειραματικό εκρανοπλάνο KM (Korabl Maket), μήκους 92 μέτρων, πετούσε λίγα μέτρα πάνω από την επιφάνεια του νερού εκμεταλλευόμενο το φαινόμενο επίδρασης εδάφους (ground effect) με ταχύτητες άνω των 500 χλμ/ώρα.",
        "funFacts": [
            "Όταν οι αμερικανικοί κατασκοπευτικοί δορυφόροι το εντόπισαν στην Κασπία Θάλασσα το 1966, δεν μπορούσαν να καταλάβουν αν ήταν αεροπλάνο ή πλοίο.",
            "Τα αρχικά 'KM' ερμηνεύτηκαν από τους αναλυτές της CIA ως 'Kaspian Monster'."
        ],
        "source": "https://en.wikipedia.org/wiki/Caspian_Sea_Monster",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "aviation", "soviet_union"]
    },
    {
        "id": "wtf_facts_hard_277",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο μυστηριώδες ακουστικό σήμα πολύ χαμηλής συχνότητας καταγράφηκε από το NOAA στον Ειρηνικό Ωκεανό το 1997 και αργότερα αποδόθηκε σε ρηγματώσεις παγόβουνων;",
        "answers": ["Julia", "Bloop", "Upsweep", "Slow Down"],
        "correctAnswerIndex": 1,
        "explanation": "Το Bloop ήταν ένας εξαιρετικά ισχυρός υποβρύχιος ήχος που ανιχνεύτηκε σε απόσταση χιλιάδων χιλιομέτρων. Αρχικά θεωρήθηκε βιολογικής προέλευσης, αλλά το 2012 επιβεβαιώθηκε ότι προήλθε από σεισμό πάγου (icequake) στην Ανταρκτική.",
        "funFacts": [
            "Λόγω της τεράστιας έντασής του, πολλοί λάτρεις του μυστηρίου το είχαν συνδέσει με το τέρας του H.P. Lovecraft, τον Cthulhu.",
            "Τα υδρόφωνα του SOSUS που το κατέγραψαν είχαν αρχικά σχεδιαστεί για τον εντοπισμό σοβιετικών υποβρυχίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloop",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "oceanography", "acoustics"]
    },
    {
        "id": "wtf_facts_hard_278",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια είναι η παλαιότερη γνωστή υπολογιστική συσκευή που χρησιμοποιούσε περίπλοκο σύστημα γραναζιών για την πρόβλεψη αστρονομικών φαινομένων;",
        "answers": ["Ο Μηχανισμός των Αντικυθήρων", "Ο Αστρολάβος της Αλεξάνδρειας", "Το Ωρολόγιο του Κτησίβιου", "Το Σφαιροποιητήριο του Αρχιμήδη"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μηχανισμός των Αντικυθήρων (χρονολογείται γύρω στο 150-100 π.Χ.) περιείχε τουλάχιστον 30 χάλκινα γρανάζια και υπολόγιζε τις θέσεις του Ήλιου, της Σελήνης, τις εκλείψεις και τους Ολυμπιακούς κύκλους.",
        "funFacts": [
            "Η πολυπλοκότητα των διαφορικών γραναζιών του δεν εμφανίστηκε ξανά στην ιστορία μέχρι την ευρωπαϊκή ωρολογοποιία του 14ου αιώνα.",
            "Ανακαλύφθηκε το 1901 από Συμιακούς σφουγγαράδες σε ναυάγιο κοντά στα Αντικύθηρα."
        ],
        "source": "https://en.wikipedia.org/wiki/Antikythera_mechanism",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "archaeology", "ancient_greece", "technology"]
    },
    {
        "id": "wtf_facts_hard_279",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος αρχαιολογικός χώρος στην Τουρκία χρονολογείται γύρω στο 9500 π.Χ. και περιλαμβάνει τους αρχαιότερους γνωστούς μεγαλιθικούς ναούς της ανθρωπότητας;",
        "answers": ["Çatalhöyük", "Göbekli Tepe", "Nevalı Çori", "Jericho"],
        "correctAnswerIndex": 1,
        "explanation": "Το Γκεμπεκλί Τεπέ (Göbekli Tepe) κατασκευάστηκε από κυνηγούς-συλλέκτες πριν από την ανακάλυψη της κεραμικής και της γεωργίας, ανατρέποντας τις θεωρίες για την εξέλιξη των πρώτων οργανωμένων κοινωνιών.",
        "funFacts": [
            "Οι πελώριοι πυλώνες σε σχήμα Τ ζυγίζουν έως και 20 τόνους ο καθένας και είναι σκαλισμένοι με ανάγλυφα ζώων.",
            "Οι ίδιοι οι κατασκευαστές του έθαψαν σκόπιμα τους κύκλους των λίθων κάτω από χώμα πριν εγκαταλείψουν την περιοχή."
        ],
        "source": "https://en.wikipedia.org/wiki/G%C3%B6bekli_Tepe",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "archaeology", "prehistory"]
    },
    {
        "id": "wtf_facts_hard_280",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο σύστημα γραφής του Νησιού του Πάσχα παραμένει μη αποκρυπτογραφημένο και ήταν γραμμένο με τη μέθοδο του αντίστροφου βουστροφηδόν;",
        "answers": ["Rongorongo", "Linear A", "Phaistos script", "Epi-Olmec"],
        "correctAnswerIndex": 0,
        "explanation": "Το Ρονγκορόνγκο (Rongorongo) είναι σύστημα γλυφών χαραγμένο σε ξύλινες πινακίδες στο Νησί του Πάσχα. Για να το διαβάσει κανείς, πρέπει να περιστρέφει την πινακίδα κατά 180 μοίρες στο τέλος κάθε γραμμής.",
        "funFacts": [
            "Μόνο περίπου 26 αυθεντικές ξύλινες πινακίδες διασώζονται σήμερα παγκοσμίως σε μουσεία.",
            "Αν αποδειχθεί ότι αποτελεί πλήρες σύστημα γραφής, είναι μία από τις ελάχιστες εντελώς ανεξάρτητες επινοήσεις γραφής στην ανθρώπινη ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Rongorongo",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "linguistics", "archaeology"]
    },
    {
        "id": "wtf_facts_hard_281",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο διάσημο εικονογραφημένο χειρόγραφο του 15ου αιώνα είναι γραμμένο σε άγνωστη γραφή και περιέχει σχέδια ανύπαρκτων φυτών και αστρονομικών διαγραμμάτων;",
        "answers": ["Codex Seraphinianus", "Codex Gigas", "Χειρόγραφο Voynich", "Book of Kells"],
        "correctAnswerIndex": 2,
        "explanation": "Το Χειρόγραφο Βόινιτς (Voynich manuscript), που χρονολογείται με άνθρακα-14 στις αρχές του 15ου αιώνα, έχει αντισταθεί σε κάθε προσπάθεια αποκρυπτογράφησης από κορυφαίους κρυπταναλυτές του κόσμου.",
        "funFacts": [
            "Ακόμη και ο William Friedman, ο κορυφαίος Αμερικανός κρυπταναλυτής του Β' Παγκοσμίου Πολέμου, απέτυχε να αποκρυπτογραφήσει έστω μία πρόταση.",
            "Τα κείμενα ακολουθούν στατιστικούς κανόνες φυσικής γλώσσας (όπως ο νόμος του Zipf), υποδεικνύοντας ότι δεν πρόκειται για τυχαία σύμβολα."
        ],
        "source": "https://en.wikipedia.org/wiki/Voynich_manuscript",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "cryptography", "manuscripts"]
    },
    {
        "id": "wtf_facts_hard_282",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο αρχαίο τεχνούργημα από την Κρήτη περιέχει ιερογλυφικά σύμβολα που τυπώθηκαν στον νωπό πηλό με σφραγίδες, θυμίζοντας πρώιμη τυπογραφία;",
        "answers": ["Ο Δίσκος της Φαιστού", "Ο Πέλεκυς του Αρκαλοχωρίου", "Η Πινακίδα του Δισπηλιού", "Το Ρυτό των Μυκηνών"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Δίσκος της Φαιστού (2η χιλιετία π.Χ.) περιλαμβάνει 241 σύμβολα σε σπειροειδή διάταξη, τα οποία αποτυπώθηκαν με προκατασκευασμένες ιερογλυφικές σφραγίδες, χιλιετίες πριν από τον Γουτεμβέργιο.",
        "funFacts": [
            "Κανένα άλλο κείμενο με την ίδια γραφή δεν έχει βρεθεί, γεγονός που καθιστά την αποκρυπτογράφησή του πρακτικά αδύνατη.",
            "Φυλάσσεται στο Αρχαιολογικό Μουσείο Ηρακλείου."
        ],
        "source": "https://en.wikipedia.org/wiki/Phaistos_Disc",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "archaeology", "ancient_greece"]
    },
    {
        "id": "wtf_facts_hard_283",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος Άγγλος αρχιτέκτονας και ερασιτέχνης γλωσσολόγος αποκρυπτογράφησε τη Γραμμική Β το 1952 αποδεικνύοντας ότι ήταν πρώιμη ελληνική γλώσσα;",
        "answers": ["Arthur Evans", "Michael Ventris", "Jean-François Champollion", "Heinrich Schliemann"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Μάικλ Βέντρις (Michael Ventris), με τη βοήθεια του κλασικού φιλολόγου John Chadwick, απέδειξε ότι τα σύμβολα της Γραμμικής Β απέδιδαν μυκηναϊκά ελληνικά και όχι κάποια άγνωστη μινωική γλώσσα.",
        "funFacts": [
            "Ο Sir Arthur Evans, που ανέσκαψε την Κνωσό, πίστευε ακράδαντα μέχρι τον θάνατό του ότι η γλώσσα δεν είχε καμία σχέση με τα ελληνικά.",
            "Ο Βέντρις δεν ήταν επαγγελματίας αρχαιολόγος, αλλά αρχιτέκτονας με πάθος για τις γλώσσες και την κρυπτογραφία."
        ],
        "source": "https://en.wikipedia.org/wiki/Michael_Ventris",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "linguistics", "ancient_greece"]
    },
    {
        "id": "wtf_facts_hard_284",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια μικροσκοπική ουδέτερη επικράτεια μεταξύ Βελγίου και Πρωσίας υπήρξε από το 1816 έως το 1920 και επιχείρησε να γίνει το πρώτο εσπεραντόφωνο κράτος;",
        "answers": ["Ουδέτερο Μορεσνέτ (Neutral Moresnet)", "Ελεύθερη Πόλη του Ντάντσιχ", "Σάαρλαντ", "Κοντομίνιο των Νέων Εβρίδων"],
        "correctAnswerIndex": 0,
        "explanation": "Το Ουδέτερο Μορεσνέτ (Neutral Moresnet) δημιουργήθηκε λόγω διαφωνίας για ένα ορυχείο ψευδαργύρου. Το 1908 προτάθηκε να μετατραπεί στο πρώτο ανεξάρτητο κράτος με επίσημη γλώσσα την Εσπεράντο, υπό το όνομα 'Amikejo' (Τόπος Φιλίας).",
        "funFacts": [
            "Είχε έκταση μόλις 3,5 τετραγωνικά χιλιόμετρα και διοικούνταν από κοινού από έναν Πρώσο και έναν Βέλγο επίτροπο.",
            "Ενσωματώθηκε οριστικά στο Βέλγιο με τη Συνθήκη των Βερσαλλιών μετά τον Α' Παγκόσμιο Πόλεμο."
        ],
        "source": "https://en.wikipedia.org/wiki/Neutral_Moresnet",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "history", "microstates"]
    },
    {
        "id": "wtf_facts_hard_285",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια ιταλική δημοκρατία δημιουργήθηκε κατά λάθος το 1440 λόγω σφάλματος στην οριοθέτηση συνόρων από τον Πάπα Ευγένιο Δ' και τη Φλωρεντία;",
        "answers": ["Δημοκρατία της Κοσπάια (Republic of Cospaia)", "Δημοκρατία του Σαν Μαρίνο", "Δημοκρατία της Νόλι", "Δημοκρατία της Ραγούσας"],
        "correctAnswerIndex": 0,
        "explanation": "Η Δημοκρατία της Κοσπάια (Republic of Cospaia) προέκυψε όταν μια συνθήκη παρέλειψε μια στενή λωρίδα γης 300 μέτρων. Οι κάτοικοι κήρυξαν ανεξαρτησία, την οποία διατήρησαν για σχεδόν 400 χρόνια χωρίς φόρους, στρατό ή νόμους.",
        "funFacts": [
            "Το σύνθημά τους ήταν 'Perpetua et firma libertas' (Αιώνια και σταθερή ελευθερία).",
            "Έγινε ένα από τα πρώτα κέντρα καλλιέργειας καπνού στην Ιταλία, καθώς δεν υπόκειτο στα παπικά μονοπώλια."
        ],
        "source": "https://en.wikipedia.org/wiki/Republic_of_Cospaia",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "history", "italy"]
    },
    {
        "id": "wtf_facts_hard_286",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο βακτήριο κατέχει το ρεκόρ Guinness ως η πιο ανθεκτική μορφή ζωής στην ιονίζουσα ακτινοβολία, αντέχοντας έως και 15.000 Gray;",
        "answers": ["Deinococcus radiodurans", "Bacillus subtilis", "Thermus aquaticus", "Pseudomonas aeruginosa"],
        "correctAnswerIndex": 0,
        "explanation": "Το Deinococcus radiodurans, συχνά αποκαλούμενο 'Conan the Bacterium', μπορεί να επιβιώσει σε δόσεις ακτινοβολίας χιλιάδες φορές υψηλότερες από τη θανατηφόρα δόση για τον άνθρωπο (5 Gray) αναδομώντας το κατακερματισμένο DNA του.",
        "funFacts": [
            "Διαθέτει πολλαπλά αντίγραφα του γονιδιώματός του και εξαιρετικά αποδοτικά ένζυμα επιδιόρθωσης διπλών σπασιμάτων DNA μέσα σε λίγες ώρες.",
            "Ανακαλύφθηκε για πρώτη φορά το 1956 σε κονσέρβες κρέατος που είχαν υποστεί αποστείρωση με ακτίνες γάμμα και παρ' όλα αυτά αλλοιώθηκαν."
        ],
        "source": "https://en.wikipedia.org/wiki/Deinococcus_radiodurans",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biology", "microbiology"]
    },
    {
        "id": "wtf_facts_hard_287",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο αρχαιοβακτήριο κατέχει το ρεκόρ επιβίωσης και πολλαπλασιασμού στην υψηλότερη θερμοκρασία, αναπτυσσόμενο στους 122 °C υπό πίεση;",
        "answers": ["Methanopyrus kandleri strain 116", "Pyrolobus fumarii", "Geogemma barossii", "Sulfolobus solfataricus"],
        "correctAnswerIndex": 0,
        "explanation": "Το στέλεχος 116 του Methanopyrus kandleri, που απομονώθηκε από υδροθερμικές καμινάδες στον Κόλπο της Καλιφόρνιας, μπορεί να πολλαπλασιαστεί στους 122 °C υπό συνθήκες υψηλής υδροστατικής πίεσης.",
        "funFacts": [
            "Σε κανονική ατμοσφαιρική πίεση το νερό βράζει στους 100 °C, αλλά στον πυθμένα του ωκεανού παραμένει υγρό σε πολύ υψηλότερες θερμοκρασίες.",
            "Χρησιμοποιεί υδρογόνο και διοξείδιο του άνθρακα για να παράγει μεθάνιο ως πηγή ενέργειας."
        ],
        "source": "https://en.wikipedia.org/wiki/Methanopyrus",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biology", "extremophiles"]
    },
    {
        "id": "wtf_facts_hard_288",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο θαλάσσιο βακτήριο θεωρείται ο πολυπληθέστερος οργανισμός στον πλανήτη Γη, αριθμώντας περίπου 2×10^28 μεμονωμένα κύτταρα;",
        "answers": ["Pelagibacter ubique (SAR11)", "Prochlorococcus marinus", "Synechococcus", "Vibrio fischeri"],
        "correctAnswerIndex": 0,
        "explanation": "Το Pelagibacter ubique (μέλος του κλάδου SAR11) αποτελεί έως και το 25% όλων των μικροβιακών κυττάρων στους ωκεανούς. Έχει ένα από τα μικρότερα και πιο εξορθολογισμένα γονιδιώματα ελεύθερα διαβιούντων οργανισμών.",
        "funFacts": [
            "Το γονιδίωμά του δεν περιέχει περιττό 'άχρηστο' DNA (junk DNA), βελτιστοποιώντας το ενεργειακό κόστος αναπαραγωγής.",
            "Αν συγκεντρώνονταν όλα τα κύτταρα Pelagibacter του πλανήτη, η συνολική βιομάζα τους θα ξεπερνούσε εκείνη όλων των ψαριών στους ωκεανούς."
        ],
        "source": "https://en.wikipedia.org/wiki/Pelagibacter_ubique",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "microbiology", "marine_biology"]
    },
    {
        "id": "wtf_facts_hard_289",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο παράξενο απολίθωμα της Καμβρίου περιόδου ανακατασκευάστηκε αρχικά ανάποδα, με τα αγκάθια του να θεωρούνται πόδια και το κεφάλι ουρά;",
        "answers": ["Hallucigenia", "Anomalocaris", "Opabinia", "Wiwaxia"],
        "correctAnswerIndex": 0,
        "explanation": "Η Hallucigenia, που ανακαλύφθηκε στα σχιστολιθικά πετρώματα Burgess Shale, ανακατασκευάστηκε λανθασμένα από τον Simon Conway Morris το 1977. Χρειάστηκαν δεκαετίες για να συνειδητοποιήσουν οι παλαιοντολόγοι ότι τα 'πόδια' ήταν αμυντικά αγκάθια της ράχης.",
        "funFacts": [
            "Ονομάστηκε έτσι λόγω της ονειρικής, 'παραισθησιογόνου' και αλλόκοτης εμφάνισής της.",
            "Μόλις το 2015 οι επιστήμονες κατάφεραν τελικά να ταυτοποιήσουν με βεβαιότητα ποιο άκρο ήταν το κεφάλι, εντοπίζοντας μάτια και δόντια με ηλεκτρονικό μικροσκόπιο."
        ],
        "source": "https://en.wikipedia.org/wiki/Hallucigenia",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "paleontology", "fossils"]
    },
    {
        "id": "wtf_facts_hard_290",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο μυστηριώδες απολίθωμα του Ιλινόις (Tullimonstrum gregarium) προβλημάτισε τους επιστήμονες επί μισό αιώνα σχετικά με το αν ήταν σπόνδυλος ή ασπόνδυλο;",
        "answers": ["Τέρας του Tully", "Ψάρι Tiktaalik", "Προτότυπο Burgess", "Κονόδοντας"],
        "correctAnswerIndex": 0,
        "explanation": "Το Τέρας του Tully (Tullimonstrum) είχε μάτια τοποθετημένα σε πλευρικούς μίσχους και μια μακριά προβοσκίδα με σαγόνι γεμάτο δόντια. Ακόμα και σήμερα η ακριβής ταξινόμησή του παραμένει αντικείμενο έντονης επιστημονικής διαμάχης.",
        "funFacts": [
            "Ανακαλύφθηκε το 1955 από τον ερασιτέχνη συλλέκτη Francis Tully στα ορυχεία άνθρακα του Mazon Creek.",
            "Το 1989 ανακηρύχθηκε επίσημο κρατικό απολίθωμα της πολιτείας του Ιλινόις."
        ],
        "source": "https://en.wikipedia.org/wiki/Tullimonstrum",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "paleontology", "fossils"]
    },
    {
        "id": "wtf_facts_hard_291",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο σπάνιο χημικό στοιχείο της ομάδας του λευκόχρυσου βρέθηκε σε αφθονία στο όριο K-Pg, αποτελώντας την πρώτη ένδειξη πρόσκρουσης αστεροειδούς που εξαφάνισε τους δεινοσαύρους;",
        "answers": ["Όσμιο", "Ιρίδιο", "Ρήνιο", "Ρόδιο"],
        "correctAnswerIndex": 1,
        "explanation": "Ο νομπελίστας φυσικός Luis Alvarez και ο γιος του Walter ανακάλυψαν μια παγκόσμια 'ανωμαλία ιριδίου' στο γεωλογικό στρώμα πριν από 66 εκατομμύρια χρόνια, στοιχείο που είναι εξαιρετικά σπάνιο στον γήινο φλοιό αλλά άφθονο σε μετεωρίτες.",
        "funFacts": [
            "Το ιρίδιο βυθίστηκε στον πυρήνα της Γης κατά τον σχηματισμό της, οπότε η επιφανειακή του παρουσία υποδηλώνει εξωγήινη πηγή.",
            "Η ανακάλυψη αυτή οδήγησε αργότερα στον εντοπισμό του κρατήρα Chicxulub στη χερσόνησο Γιουκατάν."
        ],
        "source": "https://en.wikipedia.org/wiki/Cretaceous%E2%80%93Paleogene_extinction_event#Iridium_anomaly",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "geology", "dinosaurs", "extinction"]
    },
    {
        "id": "wtf_facts_hard_292",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είδος μέδουσας θεωρείται βιολογικά αθάνατο καθώς μπορεί να επιστρέψει στο στάδιο του πολύποδα μετά την ενηλικίωση;",
        "answers": ["Turritopsis dohrnii", "Chironex fleckeri", "Aurelia aurita", "Cyanea capillata"],
        "correctAnswerIndex": 0,
        "explanation": "Η Turritopsis dohrnii μπορεί, όταν αντιμετωπίζει σωματική βλάβη ή πείνα, να υποστεί κυτταρική διαδιαφοροποίηση (transdifferentiation) και να μετατραπεί ξανά σε νεαρό πολύποδα, αποφεύγοντας το γήρας.",
        "funFacts": [
            "Αυτή η διαδικασία μπορεί θεωρητικά να επαναλαμβάνεται επ' άπειρον, καθιστώντας την βιολογικά αθάνατη.",
            "Παρά την ικανότητα αυτή, οι περισσότερες καταλήγουν να τρώγονται από θηρευτές ή να υποκύπτουν σε ασθένειες."
        ],
        "source": "https://en.wikipedia.org/wiki/Turritopsis_dohrnii",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biology", "marine_life"]
    },
    {
        "id": "wtf_facts_hard_293",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο θαλάσσιο σαλιγκάρι (Elysia chlorotica) μπορεί να φωτοσυνθέτει ενσωματώνοντας χλωροπλάστες από τα φύκια που καταναλώνει στα δικά του κύτταρα;",
        "answers": ["Κλεπτοπλαστικό θαλάσσιο γυμνοβράγχιο", "Κώνος ο γεωγράφος", "Απλεσία η καλιφορνική", "Γλαύκος ο ατλαντικός"],
        "correctAnswerIndex": 0,
        "explanation": "Η Elysia chlorotica εμφανίζει το φαινόμενο της κλεπτοπλαστικής (kleptoplasty), διατηρώντας λειτουργικούς τους χλωροπλάστες του φύκους Vaucheria litorea στο πεπτικό της σύστημα για μήνες, ζώντας μόνο με ηλιακό φως.",
        "funFacts": [
            "Έχει ενσωματώσει ορισμένα γονίδια του φύκους στο δικό της πυρηνικό DNA μέσω οριζόντιας μεταφοράς γονιδίων για να συντηρεί τους χλωροπλάστες.",
            "Το σώμα της έχει λαμπερό πράσινο χρώμα και σχήμα που μοιάζει εκπληκτικά με φύλλο δέντρου."
        ],
        "source": "https://en.wikipedia.org/wiki/Elysia_chlorotica",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biology", "photosynthesis"]
    },
    {
        "id": "wtf_facts_hard_294",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος είναι ο παλαιότερος γνωστός μεμονωμένος κλωνικός οργανισμός στον κόσμο, ένα δάσος από λεύκες στη Γιούτα με κοινό ριζικό σύστημα;",
        "answers": ["Pando", "Methuselah", "Prometheus", "Old Tjikko"],
        "correctAnswerIndex": 0,
        "explanation": "Το Pando (ή The Trembling Giant) είναι μια αποικία λεύκας (Populus tremuloides) που αποτελείται από πάνω από 40.000 γενετικά πανομοιότυπους κορμούς που συνδέονται με ένα ενιαίο υπόγειο ριζικό σύστημα ηλικίας χιλιάδων ετών.",
        "funFacts": [
            "Ζυγίζει περίπου 6.000 τόνους, αποτελώντας έναν από τους βαρύτερους γνωστούς οργανισμούς στον πλανήτη.",
            "Εκτιμάται ότι έχει ηλικία τουλάχιστον 14.000 ετών, αν και ορισμένες εκτιμήσεις ανεβάζουν την ηλικία του σε εκατοντάδες χιλιάδες χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Pando_(tree)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "botany", "nature"]
    },
    {
        "id": "wtf_facts_hard_295",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο αρχαίο πεύκο (Pinus longaeva) στα Λευκά Όρη της Καλιφόρνιας θεωρείται το γηραιότερο μη κλωνικό δέντρο στον κόσμο, με ηλικία άνω των 4.850 ετών;",
        "answers": ["Μαθουσάλας (Methuselah)", "Προμηθέας (Prometheus)", "Υπερίων (Hyperion)", "Στρατηγός Σέρμαν (General Sherman)"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μαθουσάλας (Methuselah) φύτρωσε γύρω στο 2832 π.Χ., πριν ακόμη ολοκληρωθεί η κατασκευή της Μεγάλης Πυραμίδας της Γκίζας, και παραμένει ζωντανός σε υψόμετρο άνω των 3.000 μέτρων.",
        "funFacts": [
            "Η ακριβής τοποθεσία του δέντρου κρατείται μυστική από τη Δασική Υπηρεσία των ΗΠΑ για να προστατευτεί από βανδαλισμούς.",
            "Ένα άλλο παλαιότερο δέντρο, ο Προμηθέας, κόπηκε κατά λάθος από έναν γεωγράφο ερευνητή το 1964 για τη μέτρηση των δακτυλίων του."
        ],
        "source": "https://en.wikipedia.org/wiki/Methuselah_(tree)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "botany", "trees"]
    },
    {
        "id": "wtf_facts_hard_296",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είδος μύκητα στο Όρεγκον καλύπτει έκταση σχεδόν 9 τετραγωνικών χιλιομέτρων, αποτελώντας τον μεγαλύτερο γνωστό οργανισμό σε έκταση στη Γη;",
        "answers": ["Armillaria ostoyae", "Mycena luxaeterna", "Calvatia gigantea", "Psilocybe semilanceata"],
        "correctAnswerIndex": 0,
        "explanation": "Ο μύκητας Armillaria ostoyae (γνωστός ως 'Humongous Fungus') στο Εθνικό Δάσος Malheur του Όρεγκον εξαπλώνεται υπογείως μέσω μυκηλίων καλύπτοντας 9,65 τετρ. χιλιόμετρα και έχει ηλικία τουλάχιστον 2.400 ετών.",
        "funFacts": [
            "Ανακαλύφθηκε όταν οι δασολόγοι ερεύνησαν γιατί τεράστιες εκτάσεις πεύκων πέθαιναν μυστηριωδώς από σήψη των ριζών.",
            "Το μεγαλύτερο μέρος του οργανισμού είναι αόρατο κάτω από το έδαφος, εκτός από τα μανιτάρια που φυτρώνουν στη βάση των δέντρων το φθινόπωρο."
        ],
        "source": "https://en.wikipedia.org/wiki/Armillaria_ostoyae",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "mycology", "biology"]
    },
    {
        "id": "wtf_facts_hard_297",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια πρωτεΐνη έχει το μακρύτερο χημικό όνομα στην αγγλική γλώσσα, το οποίο αποτελείται από 189.819 γράμματα και απαιτεί πάνω από 3 ώρες για να προφερθεί;",
        "answers": ["Τιτίνη (Titin)", "Κολλαγόνο", "Μυοσφαιρίνη", "Αιμοσφαιρίνη"],
        "correctAnswerIndex": 0,
        "explanation": "Η τιτίνη (titin ή connectin) είναι η μεγαλύτερη γνωστή πρωτεΐνη στο ανθρώπινο σώμα, υπεύθυνη για την παθητική ελαστικότητα των μυών, και η πλήρης χημική IUPAC ονομασία της περιέχει 189.819 γράμματα.",
        "funFacts": [
            "Αποτελείται από περισσότερα από 34.000 αμινοξέα σε μία ενιαία πεπτιδική αλυσίδα.",
            "Τα λεξικά δεν περιλαμβάνουν την πλήρη ονομασία της επειδή θεωρείται χημικός τύπος και όχι τυπική λεξικογραφική λέξη."
        ],
        "source": "https://en.wikipedia.org/wiki/Titin",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biochemistry", "linguistics"]
    },
    {
        "id": "wtf_facts_hard_298",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο βιολογικό φαινόμενο παρατηρείται όταν οι κορυφές ορισμένων δέντρων του ίδιου είδους αποφεύγουν να αγγίζουν η μία την άλλη, δημιουργώντας φωτεινά κανάλια στον θόλο του δάσους;",
        "answers": ["Συστολή της κόμης (Crown shyness)", "Φωτοτροπισμός", "Αλληλοπάθεια", "Αποκοπή φυλλώματος"],
        "correctAnswerIndex": 0,
        "explanation": "Η συστολή της κόμης (crown shyness) είναι το φαινόμενο όπου τα ψηλά δέντρα διατηρούν σαφώς καθορισμένα κενά μεταξύ των φυλλωμάτων τους, σχηματίζοντας μοτίβα που μοιάζουν με ρωγμές ή ποτάμια στον ουρανό.",
        "funFacts": [
            "Πιστεύεται ότι βοηθά στην αποφυγή μετάδοσης επιβλαβών εντόμων και προστατεύει τα ευαίσθητα κλαδιά από το σπάσιμο κατά τους ισχυρούς ανέμους.",
            "Επιτρέπει επίσης στο φως του ήλιου να φτάσει στα χαμηλότερα φυτά του υποορόφου του δάσους."
        ],
        "source": "https://en.wikipedia.org/wiki/Crown_shyness",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "botany", "nature"]
    },
    {
        "id": "wtf_facts_hard_299",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο ένζυμο χρησιμοποιούν οι πυγολαμπίδες για να παράγουν σχεδόν 100% ψυχρό φως χωρίς απώλεια ενέργειας σε θερμότητα;",
        "answers": ["Λουσιφεράση (Luciferase)", "Καταλάση", "Πυροφωσφατάση", "Αμυλάση"],
        "correctAnswerIndex": 0,
        "explanation": "Η λουσιφεράση καταλύει την οξείδωση της λουσιφερίνης παρουσία ATP και οξυγόνου. Η αντίδραση αυτή έχει σχεδόν 100% κβαντική απόδοση, που σημαίνει ότι σχεδόν όλη η ενέργεια μετατρέπεται σε φως και ελάχιστη σε θερμότητα.",
        "funFacts": [
            "Σε σύγκριση, ένας παραδοσιακός λαμπτήρας πυρακτώσεως εκπέμπει μόλις το 10% της ενέργειάς του ως ορατό φως και το 90% ως θερμότητα.",
            "Τα γονίδια της λουσιφεράσης χρησιμοποιούνται ευρύτατα στη γενετική μηχανική ως γονίδια-αναφορείς (reporter genes)."
        ],
        "source": "https://en.wikipedia.org/wiki/Luciferase",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "biochemistry", "bioluminescence"]
    },
    {
        "id": "wtf_facts_hard_300",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο υποθετικό ουράνιο σώμα αποτελείται αποκλειστικά από σκοτεινή ύλη ή συγκεντρώσεις βαρυτονίων χωρίς να περιέχει κανονική βαρυονική ύλη;",
        "answers": ["Σκοτεινός αστέρας (Dark star)", "Μαύρη τρύπα", "Κουάζαρ", "Πάλσαρ"],
        "correctAnswerIndex": 0,
        "explanation": "Οι σκοτεινοί αστέρες (dark stars) είναι θεωρητικά πρώιμα ουράνια σώματα που ίσως υπήρξαν στο πρώιμο σύμπαν, τροφοδοτούμενα από την εξουδετέρωση σωματιδίων σκοτεινής ύλης παρά από πυρηνική σύντηξη.",
        "funFacts": [
            "Αν και ονομάζονται 'σκοτεινοί', θα εξέπεμπαν έντονο ορατό φως και υπέρυθρη ακτινοβολία.",
            "Θα μπορούσαν να έχουν διάμετρο από 4 έως και 2.000 αστρονομικές μονάδες (AU), όντας τεράστιοι σε μέγεθος αλλά με χαμηλή πυκνότητα."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_star_(dark_matter)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astrophysics", "cosmology"]
    },
    {
        "id": "wtf_facts_hard_301",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το μέγιστο θεωρητικό όριο μάζας για έναν μη περιστρεφόμενο αστέρα νετρονίων πριν καταρρεύσει σε μαύρη τρύπα;",
        "answers": ["Όριο Tolman-Oppenheimer-Volkoff (TOV)", "Όριο Chandrasekhar", "Όριο Eddington", "Όριο Roche"],
        "correctAnswerIndex": 0,
        "explanation": "Το όριο Tolman-Oppenheimer-Volkoff (TOV) υπολογίζει τη μέγιστη μάζα ενός αστέρα νετρονίων σε περίπου 2,17 ηλιακές μάζες. Πάνω από αυτό το όριο, η πίεση εκφυλισμού νετρονίων δεν μπορεί να αντισταθεί στη βαρύτητα.",
        "funFacts": [
            "Διατυπώθηκε αρχικά το 1939 από τους Richard Tolman, J. Robert Oppenheimer και George Volkoff.",
            "Αντίστοιχα, το όριο Chandrasekhar (1,4 ηλιακές μάζες) ισχύει για τους λευκούς νάνους."
        ],
        "source": "https://en.wikipedia.org/wiki/Tolman%E2%80%93Oppenheimer%E2%80%93Volkoff_limit",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astrophysics", "neutron_stars"]
    },
    {
        "id": "wtf_facts_hard_302",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο υποθετικό σωματίδιο προτάθηκε για να λύσει το πρόβλημα ισχυρής CP-συμμετρίας στην κβαντική χρωμοδυναμική και αποτελεί κορυφαίο υποψήφιο για τη σκοτεινή ύλη;",
        "answers": ["Αξιόνιο (Axion)", "Ταχυόνιο", "Γκραβιτόνιο", "Γκλουίνο"],
        "correctAnswerIndex": 0,
        "explanation": "Το αξιόνιο είναι υποθετικό μποζόνιο με εξαιρετικά μικρή μάζα και μηδενικό φορτίο, το οποίο προτάθηκε από τους Peccei και Quinn το 1977 και πήρε το όνομά του από μια γνωστή μάρκα απορρυπαντικού.",
        "funFacts": [
            "Ο νομπελίστας φυσικός Frank Wilczek επέλεξε το όνομα από το απορρυπαντικό 'Axion' επειδή το σωματίδιο 'καθάριζε' ένα πρόβλημα της φυσικής.",
            "Ειδικά πειράματα όπως το ADMX προσπαθούν να ανιχνεύσουν αξιόνια μετατρέποντάς τα σε φωτόνια μικροκυμάτων μέσα σε ισχυρά μαγνητικά πεδία."
        ],
        "source": "https://en.wikipedia.org/wiki/Axion",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "particle_physics", "dark_matter"]
    },
    {
        "id": "wtf_facts_hard_303",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το μεγαλύτερο γνωστό κενό (void) στο παρατηρήσιμο σύμπαν, με διάμετρο περίπου 330 εκατομμύρια έτη φωτός και σχεδόν παντελή έλλειψη γαλαξιών;",
        "answers": ["Το Κενό του Βοώτη (Boötes void)", "Το Τοπικό Κενό", "Το Κενό του Ηριδανού", "Το Κενό του Ταύρου"],
        "correctAnswerIndex": 0,
        "explanation": "Το Κενό του Βοώτη (Boötes void ή Μεγάλο Τίποτα) είναι μια τεράστια σφαιρική περιοχή του διαστήματος που περιέχει μόνο περίπου 60 γαλαξίες, ενώ σε έναν κανονικό όγκο τέτοιου μεγέθους θα αναμένονταν περίπου 10.000.",
        "funFacts": [
            "Αν ο Γαλαξίας μας βρισκόταν στο κέντρο του Κενού του Βοώτη, η ανθρωπότητα δεν θα γνώριζε την ύπαρξη άλλων γαλαξιών μέχρι τη δεκαετία του 1960.",
            "Ανακαλύφθηκε το 1981 από τον αστρονόμο Robert Kirshner και τους συνεργάτες του."
        ],
        "source": "https://en.wikipedia.org/wiki/Bo%C3%B6tes_void",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astronomy", "cosmology"]
    },
    {
        "id": "wtf_facts_hard_304",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος είναι ο ταχύτερα περιστρεφόμενος γνωστός πάλσαρ, με ταχύτητα περιστροφής 716 στροφές το δευτερόλεπτο;",
        "answers": ["PSR J1748-2446ad", "Crab Pulsar", "Vela Pulsar", "PSR B1919+21"],
        "correctAnswerIndex": 0,
        "explanation": "Ο πάλσαρ PSR J1748-2446ad, που βρίσκεται στο σφαιρωτό σμήνος Terzan 5, περιστρέφεται 716 φορές κάθε δευτερόλεπτο, που σημαίνει ότι ο ισημερινός του κινείται με περίπου το 24% της ταχύτητας του φωτός.",
        "funFacts": [
            "Ανακαλύφθηκε το 2004 από τον Jason W.T. Hessels και την ομάδα του μέσω του τηλεσκοπίου Green Bank.",
            "Η επιφανειακή του βαρύτητα είναι τόσο ισχυρή που ένα αντικείμενο που πέφτει στην επιφάνειά του θα αποκτούσε ταχύτητα εκατομμυρίων χιλιομέτρων την ώρα."
        ],
        "source": "https://en.wikipedia.org/wiki/PSR_J1748%E2%80%932446ad",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astronomy", "pulsars"]
    },
    {
        "id": "wtf_facts_hard_305",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο αέριο σε υπερκρίσιμη κατάσταση πιστεύεται ότι σχηματίζει τεράστιους θερμούς ωκεανούς στο βαθύ εσωτερικό του Ουρανού και του Ποσειδώνα;",
        "answers": ["Μείγμα νερού, αμμωνίας και μεθανίου", "Καθαρό υδρογόνο", "Υπερκρίσιμο ήλιο", "Διοξείδιο του θείου"],
        "correctAnswerIndex": 0,
        "explanation": "Στο εσωτερικό των παγωμένων γιγάντων επικρατούν ακραίες πιέσεις και θερμοκρασίες χιλιάδων βαθμών, μετατρέποντας το νερό, την αμμωνία και το μεθάνιο σε έναν υπερκρίσιμο, ιοντικό 'υπερθερμασμένο πολτό' με εξαιρετική ηλεκτρική αγωγιμότητα.",
        "funFacts": [
            "Σε ακόμα μεγαλύτερα βάθη, οι πιέσεις διασπούν το μεθάνιο σχηματίζοντας κρυστάλλους διαμαντιών που 'βρέχουν' προς τον πυρήνα των πλανητών.",
            "Αυτός ο ηλεκτρικά αγώγιμος ρευστός μανδύας είναι υπεύθυνος για τα εξαιρετικά ασύμμετρα και κεκλιμένα μαγνητικά πεδία των δύο πλανητών."
        ],
        "source": "https://en.wikipedia.org/wiki/Neptune#Internal_structure",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astronomy", "planetary_science"]
    },
    {
        "id": "wtf_facts_hard_306",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το μοναδικό γνωστό αστέρι που έχει καταγραφεί να περιβάλλεται από έναν ακανόνιστο δακτύλιο που προκαλεί ανεξήγητες αυξομειώσεις φωτεινότητας έως και 22%;",
        "answers": ["Αστέρας της Tabby (KIC 8462852)", "Εγγύτατος Κενταύρου", "Μπετελγκέζ", "Αστέρας του Barnard"],
        "correctAnswerIndex": 0,
        "explanation": "Ο αστέρας KIC 8462852 (γνωστός ως Αστέρας της Tabby ή Boyajian's Star) παρουσιάζει ακανόνιστες βυθίσεις φωτεινότητας που αρχικά πυροδότησαν υποθέσεις ακόμα και για εξωγήινη 'μεγακατασκευή Dyson', αν και πιθανότερη αιτία είναι σκόνη από διαλυμένους κομήτες.",
        "funFacts": [
            "Πήρε το όνομά του από την αστρονόμο Tabetha S. Boyajian που ηγήθηκε της μελέτης του φαινομένου το 2015.",
            "Επειδή το κόκκινο φως μπλοκάρεται λιγότερο από το μπλε κατά τις βυθίσεις, επιβεβαιώθηκε ότι το υλικό που το κρύβει αποτελείται από λεπτά σωματίδια σκόνης."
        ],
        "source": "https://en.wikipedia.org/wiki/KIC_8462852",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "astronomy", "stars"]
    },
    {
        "id": "wtf_facts_hard_307",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια μυστηριώδης επιτάχυνση παρατηρήθηκε στις διαστημικές συσκευές Pioneer 10 και 11 καθώς απομακρύνονταν από το ηλιακό σύστημα, πριν εξηγηθεί τελικά από τη θερμική ακτινοβολία;",
        "answers": ["Ανωμαλία Pioneer (Pioneer anomaly)", "Φαινόμενο Yarkovsky", "Ανωμαλία Flyby", "Φαινόμενο Poynting-Robertson"],
        "correctAnswerIndex": 0,
        "explanation": "Η ανωμαλία Pioneer ήταν μια μικρή, ανεξήγητη επιβράδυνση προς την κατεύθυνση του Ήλιου. Το 2012 αποδείχθηκε ότι προκαλούνταν από την ασύμμετρη εκπομπή θερμότητας από τις θερμοηλεκτρικές γεννήτριες ραδιοϊσοτόπων (RTG) του σκάφους.",
        "funFacts": [
            "Για δεκαετίες ορισμένοι φυσικοί υπέθεταν ότι το φαινόμενο απαιτούσε τροποποίηση των νόμων της βαρύτητας (όπως η θεωρία MOND).",
            "Η επιτάχυνση ήταν εξαιρετικά μικρή, περίπου 8,74 × 10^-10 m/s^2, αλλά μετρήσιμη χάρη στην ακρίβεια των σημάτων τηλεμετρίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Pioneer_anomaly",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "space_exploration", "physics"]
    },
    {
        "id": "wtf_facts_hard_308",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το αρχαιότερο γνωστό επιβεβαιωμένο υλικό γήινης προέλευσης, ένας μικροσκοπικός κρύσταλλος ζιρκονίου ηλικίας 4,4 δισεκατομμυρίων ετών;",
        "answers": ["Ζιρκόνιο των Jack Hills", "Χαλαζίας Isua", "Γνάισιος Acasta", "Βασάλτης Pilbara"],
        "correctAnswerIndex": 0,
        "explanation": "Στους λόφους Jack Hills της Δυτικής Αυστραλίας ανακαλύφθηκαν κρύσταλλοι ζιρκονίου που χρονολογήθηκαν στα 4,404 δισεκατομμύρια έτη, μόλις 160 εκατομμύρια χρόνια μετά τον σχηματισμό της Γης.",
        "funFacts": [
            "Η ισοτοπική ανάλυση οξυγόνου στους κρυστάλλους υποδηλώνει ότι υπήρχε ήδη υγρό νερό και πιθανώς ωκεανοί στην επιφάνεια της Γης εκείνη την εποχή.",
            "Τα ζιρκόνια είναι εξαιρετικά ανθεκτικά και μπορούν να επιβιώσουν από πολλαπλούς κύκλους διάβρωσης και μεταμόρφωσης πετρωμάτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Jack_Hills",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "geology", "earth_history"]
    },
    {
        "id": "wtf_facts_hard_309",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο γεωλογικό φαινόμενο στον πυθμένα της Μαύρης Θάλασσας δημιουργεί υποθαλάσσιο 'ποταμό' με κοίτη, καταρράκτες και όχθες από αλμυρό νερό;",
        "answers": ["Υποθαλάσσιος ποταμός της Μαύρης Θάλασσας", "Ρεύμα του Κόλπου", "Αλοκλινές ρεύμα", "Τουρβιδιτικό ρεύμα"],
        "correctAnswerIndex": 0,
        "explanation": "Μέσω του Βοσπόρου, εξαιρετικά πυκνό και αλμυρό νερό από τη Μεσόγειο ρέει στον πυθμένα της λιγότερο αλμυρής Μαύρης Θάλασσας, σχηματίζοντας έναν ενεργό υποθαλάσσιο ποταμό βάθους έως 35 μέτρων.",
        "funFacts": [
            "Αν βρισκόταν στη στεριά, θα ήταν ο έκτος μεγαλύτερος ποταμός στον κόσμο ως προς τον όγκο ροής νερού.",
            "Διαθέτει δικές του όχθες, κοίτη και υποθαλάσσιους καταρράκτες που έχουν σκαφτεί στον βυθό."
        ],
        "source": "https://en.wikipedia.org/wiki/Black_Sea_undersea_river",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "oceanography", "geography"]
    },
    {
        "id": "wtf_facts_hard_310",
        "categoryId": "wtf_facts",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το μοναδικό γνωστό μέρος στη Γη όπου το μανδύα πέτρωμα (περιδοτίτης) εκτίθεται απευθείας στον πυθμένα του ωκεανού και αντιδρά με το νερό παράγοντας υδρογόνο και μεθάνιο;",
        "answers": ["Υδροθερμικό πεδίο Lost City", "Τάφρος των Μαριανών", "Ρήγμα του Αγίου Ανδρέα", "Σημείο Νέμο"],
        "correctAnswerIndex": 0,
        "explanation": "Το υδροθερμικό πεδίο Lost City στη Μεσοατλαντική Ράχη χαρακτηρίζεται από λευκές καμινάδες ανθρακικού ασβεστίου ύψους έως 60 μέτρων, όπου η διαδικασία σερπεντινίωσης παράγει αλκαλικά υγρά πλούσια σε μεθάνιο και υδρογόνο.",
        "funFacts": [
            "Σε αντίθεση με τις κοινές 'μαύρες καμινάδες' (black smokers), το Lost City δεν τροφοδοτείται από ηφαιστειακό μάγμα αλλά από χημική αντίδραση του θαλασσινού νερού με τον μανδύα.",
            "Θεωρείται από τους αστροβιολόγους ως το κορυφαίο γήινο ανάλογο για τις συνθήκες κάτω από τους πάγους του δορυφόρου του Κρόνου, Εγκέλαδου."
        ],
        "source": "https://en.wikipedia.org/wiki/Lost_City_Hydrothermal_Field",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wtf_facts", "oceanography", "astrobiology"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(questions)} questions for wtf_facts_hard batch 2 (261-310).")
    validate_and_append("wtf_facts", "hard", 5, questions)

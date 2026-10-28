# -*- coding: utf-8 -*-
"""Generator for pop_culture_medium questions 211-310 (100 questions)."""
import os
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

def make_q(qid, text, correct, distractors, explanation, fun_facts, source, tags, diff=3):
    idx = int(qid.split('_')[-1]) % 4
    answers = list(distractors)
    answers.insert(idx, correct)
    return {
        "id": qid,
        "categoryId": "pop_culture",
        "difficulty": diff,
        "locale": "el-GR",
        "text": text,
        "answers": answers,
        "correctAnswerIndex": idx,
        "explanation": explanation,
        "funFacts": fun_facts,
        "source": source,
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": tags
    }

questions = [
    # 211
    make_q(
        "pop_culture_med_211",
        "Σε ποια γερμανική κούκλα ενηλίκων, βασισμένη σε χαρακτήρα κόμικ της εφημερίδας Bild, βασίστηκε ο αρχικός σχεδιασμός της Barbie;",
        "Bild Lilli",
        ["Gretchen", "Fräulein Heidi", "Lorelei"],
        "Η Ruth Handler ανακάλυψε την κούκλα Bild Lilli κατά τη διάρκεια ταξιδιού της στην Ελβετία το 1956 και αγόρασε τρεις για να σχεδιάσει τη Barbie.",
        [
            "Η Bild Lilli πρωτοεμφανίστηκε ως χαρακτήρας κόμικ στριπ για ενήλικες στη γερμανική ταμπλόιντ εφημερίδα Bild Zeitung.",
            "Η Mattel αγόρασε αργότερα τα πνευματικά δικαιώματα της Lilli το 1964 για να τερματίσει τις νομικές διαμάχες."
        ],
        "https://en.wikipedia.org/wiki/Bild_Lilli_doll",
        ["barbie", "bild_lilli", "mattel", "toys"]
    ),
    # 212
    make_q(
        "pop_culture_med_212",
        "Πώς ονομάζεται η εξειδικευμένη σειρά της LEGO με γρανάζια, μοτέρ, άξονες και πνευματικά μέρη για πιο σύνθετες κατασκευές;",
        "LEGO Technic",
        ["LEGO Creator", "LEGO Architecture", "LEGO Mindstorms"],
        "Η σειρά LEGO Technic εισήχθη το 1977 (αρχικά ως 'Technical Sets') για να επιτρέψει τη δημιουργία λειτουργικών μηχανικών μοντέλων.",
        [
            "Εισήγαγε εντελώς νέα είδη τουβλακίων με οπές και συνδέσμους αντί για τις κλασικές προεξοχές (studs).",
            "Η LEGO Technic συνεργάζεται συχνά με κατασκευαστές υπεραυτοκινήτων όπως οι Ferrari, Porsche, Bugatti και Lamborghini."
        ],
        "https://en.wikipedia.org/wiki/Lego_Technic",
        ["lego", "lego_technic", "toys", "engineering"]
    ),
    # 213
    make_q(
        "pop_culture_med_213",
        "Ποιο είναι το όνομα της συζύγου του αρχηγού Μαζεστίξ στα κόμικς του Αστερίξ, η οποία κρατάει συχνά πλάστη κουζίνας;",
        "Μιμίνα (Bonnemine)",
        ["Ιελοσουμπμαρίνα", "Φραμπάλα", "Πανοραμίνα"],
        "Η Μιμίνα (Bonnemine στα γαλλικά, Impedimenta στα αγγλικά) είναι η αρχηγίνα του χωριού, συχνά απογοητευμένη από τις πολιτικές φιλοδοξίες του συζύγου της.",
        [
            "Είναι περήφανη για την αστική της καταγωγή από τη Λουτέτια (Παρίσι) και τον επιτυχημένο αδελφό της Ομεοπαθίξ.",
            "Στο τεύχος 'Η Διχόνοια', οι Ρωμαίοι εκμεταλλεύονται τη ζήλια και τις φιλοδοξίες των γυναικών του χωριού για να σπείρουν έριδες."
        ],
        "https://en.wikipedia.org/wiki/List_of_Asterix_characters#Impedimenta",
        ["asterix", "bonnemine", "comics"]
    ),
    # 214
    make_q(
        "pop_culture_med_214",
        "Ποιο είναι το όνομα του νεκροθάφτη που εμφανίζεται τακτικά στα κόμικς του Λούκυ Λουκ συνοδευόμενος από ένα κοράκι;",
        "Ματίας Μπόουν (Mathias Bone)",
        ["Έλιοτ Μπελτ", "Πατ Πόκερ", "Μπάφαλο Μπιλ"],
        "Ο νεκροθάφτης Mathias Bone ανυπομονεί πάντα για μονομαχίες και μετράει τους περαστικούς με τη μεζούρα του για να ετοιμάσει φέρετρα.",
        [
            "Το πιστό του κατοικίδιο είναι ένα κοράκι που κάθεται πάντα στον ώμο του ή πάνω σε ταφόπλακες.",
            "Αποτελεί μία από τις πιο αναγνωρίσιμες μαύρες κωμικές πινελιές που πρόσθεσαν οι Morris και Goscinny στη σειρά."
        ],
        "https://en.wikipedia.org/wiki/Lucky_Luke",
        ["lucky_luke", "undertaker", "comics", "morris"]
    ),
    # 215
    make_q(
        "pop_culture_med_215",
        "Ποιος εκκεντρικός, βαρήκοος επιστήμονας εφευρέτης είναι στενός φίλος του Τεντέν και σχεδίασε το υποβρύχιο-καρχαρία;",
        "Καθηγητής Τουρνεσόλ (Professor Calculus)",
        ["Καθηγητής Φίλιππος", "Δρ. Μίλερ", "Καθηγητής Αλαμπίκ"],
        "Ο Καθηγητής Τρύφων Τουρνεσόλ (Tryphon Tournesol στα γαλλικά, Cuthbert Calculus στα αγγλικά) χρησιμοποιεί συχνά ένα εκκρεμές για να βρίσκει αντικείμενα.",
        [
            "Ο Hergé βάσισε την εμφάνιση και τη συμπεριφορά του Τουρνεσόλ στον πραγματικό Ελβετό φυσικό και εξερευνητή Auguste Piccard.",
            "Είναι ο κατασκευαστής του εμβληματικού κόκκινου-λευκού πυραύλου που ταξιδεύει στη Σελήνη στο τεύχος 'Αποστολή στη Σελήνη' (1953)."
        ],
        "https://en.wikipedia.org/wiki/Professor_Calculus",
        ["tintin", "professor_calculus", "herge", "comics"]
    ),
    # 216
    make_q(
        "pop_culture_med_216",
        "Ποια εκκεντρική Ιταλίδα ντίβα της όπερας τραγουδάει διαρκώς την 'Άρια των Κοσμημάτων' και εκνευρίζει τον Καπετάνιο Χάντοκ στον Τεντέν;",
        "Μπιάνκα Κασταφιόρε (Bianca Castafiore)",
        ["Μαρία Κάλλας", "Τζίλντα Ρασέλι", "Αντζελίνα Φαρινέλι"],
        "Η Bianca Castafiore, γνωστή ως 'Το Αηδόνι του Μιλάνου', δεν θυμάται ποτέ σωστά το όνομα του Καπετάνιου Χάντοκ, αποκαλώντας τον 'Μπάρτοκ' ή 'Χάμποκ'.",
        [
            "Είναι ο μόνος σημαντικός γυναικείος χαρακτήρας που εμφανίζεται τακτικά στο σχεδόν εξ ολοκλήρου ανδροκρατούμενο σύμπαν του Τεντέν.",
            "Το τεύχος 'Τα Κοσμήματα της Κασταφιόρε' (1963) είναι μια κωμωδία παρεξηγήσεων που εκτυλίσσεται εξ ολοκλήρου μέσα στον πύργο του Μάρλινσπαϊκ."
        ],
        "https://en.wikipedia.org/wiki/Bianca_Castafiore",
        ["tintin", "bianca_castafiore", "comics", "herge"]
    ),
    # 217
    make_q(
        "pop_culture_med_217",
        "Ποιος Αμερικανός σκιτσογράφος δημιούργησε το αριστουργηματικό κόμικ στριπ 'Calvin and Hobbes' (1985-1995);",
        "Bill Watterson",
        ["Charles M. Schulz", "Jim Davis", "Gary Larson"],
        "Ο Bill Watterson αρνήθηκε κατηγορηματικά να εμπορευματοποιήσει τους χαρακτήρες του με παιχνίδια και μπλουζάκια, διαφυλάσσοντας την καλλιτεχνική ακεραιότητα του έργου.",
        [
            "Τα ονόματα των δύο ηρώων προέρχονται από τον θεολόγο John Calvin και τον φιλόσοφο Thomas Hobbes.",
            "Στα μάτια όλων των άλλων ο Hobbes είναι ένα λούτρινο τίγρης, αλλά για τον 6χρονο Calvin είναι ένας ζωντανός, σοφός φίλος."
        ],
        "https://en.wikipedia.org/wiki/Bill_Watterson",
        ["calvin_and_hobbes", "bill_watterson", "comics"]
    ),
    # 218
    make_q(
        "pop_culture_med_218",
        "Ποιο φανταστικό παιχνίδι επινόησαν ο Calvin και ο Hobbes στο οποίο οι κανόνες αλλάζουν διαρκώς και δεν παίζεται ποτέ με τον ίδιο τρόπο;",
        "Calvinball",
        ["Tigerball", "Hobbesball", "Chaosball"],
        "Το Calvinball έχει έναν μοναδικό απαράβατο κανόνα: δεν μπορεί να παιχτεί ποτέ με τους ίδιους κανόνες δύο φορές.",
        [
            "Οι παίκτες φορούν πάντα μάσκες και επινοούν κανόνες, σκορ και ζώνες στο γήπεδο επιτόπου κατά τη διάρκεια του παιχνιδιού.",
            "Ο όρος 'Calvinball' χρησιμοποιείται σήμερα στην πολιτική και τη νομική για καταστάσεις όπου κάποιος αλλάζει τους κανόνες κατά το δοκούν."
        ],
        "https://en.wikipedia.org/wiki/Calvin_and_Hobbes#Calvinball",
        ["calvin_and_hobbes", "calvinball", "comics"]
    ),
    # 219
    make_q(
        "pop_culture_med_219",
        "Ποιος αθάνατος ηγέτης της Λίγκας των Δολοφόνων αναγεννάται στις Πηγές του Λαζάρου (Lazarus Pits) στα κόμικς του Batman;",
        "Ra's al Ghul",
        ["Vandal Savage", "Bane", "Deathstroke"],
        "Ο Ra's al Ghul ('Το Κεφάλι του Δαίμονα' στα αραβικά) μάχεται για μια ριζοσπαστική περιβαλλοντική ισορροπία μέσω της εξόντωσης του μεγαλύτερου μέρους της ανθρωπότητας.",
        [
            "Η κόρη του, Talia al Ghul, είναι η μητέρα του Damian Wayne, γιου του Batman και πέμπτου Robin.",
            "Στην ταινία 'Batman Begins' (2005) του Christopher Nolan, τον Ra's al Ghul υποδύθηκε ο Liam Neeson."
        ],
        "https://en.wikipedia.org/wiki/Ra%27s_al_Ghul",
        ["batman", "ras_al_ghul", "dc_comics", "villains"]
    ),
    # 220
    make_q(
        "pop_culture_med_220",
        "Ποιο αντικείμενο χρησιμοποιεί ο Harvey Dent (Two-Face) για να αποφασίσει τη μοίρα των θυμάτων του στα κόμικς της DC;",
        "Ένα παραμορφωμένο ασημένιο νόμισμα",
        ["Ένα ζευγάρι ζάρια", "Μια τράπουλα ταρώ", "Μια κλεψύδρα"],
        "Ο Two-Face στρίβει ένα δολάριο με δύο όψεις (η μία χαραγμένη και καμένη) για να αποφασίσει αν θα χαρίσει τη ζωή ή θα εκτελέσει το θύμα του.",
        [
            "Πριν παραμορφωθεί από οξύ στο δικαστήριο από τον μαφιόζο Sal Maroni, ήταν ο έντιμος εισαγγελέας της Gotham City.",
            "Ο Aaron Eckhart τον υποδύθηκε στην ταινία 'The Dark Knight' (2008) και ο Tommy Lee Jones στο 'Batman Forever' (1995)."
        ],
        "https://en.wikipedia.org/wiki/Two-Face",
        ["two_face", "batman", "dc_comics", "harvey_dent"]
    ),
    # 221
    make_q(
        "pop_culture_med_221",
        "Ποιος πρώην καθηγητής ψυχολογίας χρησιμοποιεί μια ειδική τοξίνη φόβου ως ο κακοποιός Scarecrow στον Batman;",
        "Dr. Jonathan Crane",
        ["Dr. Hugo Strange", "Dr. Kirk Langstrom", "Dr. Thomas Elliot"],
        "Ο Dr. Jonathan Crane χρησιμοποιεί τη μάσκα του Σκιάχτρου και ψυχοτρόπα αέρια για να προκαλεί τους βαθύτερους φοβικούς εφιάλτες στα θύματά του.",
        [
            "Στην τριλογία του Christopher Nolan, τον Scarecrow υποδύθηκε ο Cillian Murphy, εμφανιζόμενος και στις τρεις ταινίες.",
            "Ο Scarecrow εμφανίστηκε για πρώτη φορά στο World's Finest Comics #3 το 1941."
        ],
        "https://en.wikipedia.org/wiki/Scarecrow_(DC_Comics)",
        ["scarecrow", "batman", "dc_comics", "jonathan_crane"]
    ),
    # 222
    make_q(
        "pop_culture_med_222",
        "Ποιο ήταν το όνομα του πρώτου Robin, ο οποίος αργότερα ανεξαρτητοποιήθηκε από τον Batman και υιοθέτησε το όνομα Nightwing;",
        "Dick Grayson",
        ["Jason Todd", "Tim Drake", "Damian Wayne"],
        "Ο Dick Grayson ήταν ακροβάτης τσίρκου στους 'Flying Graysons' πριν οι γονείς του δολοφονηθούν και τον υιοθετήσει ο Bruce Wayne.",
        [
            "Ως Nightwing, ο Grayson εγκαταστάθηκε στη γειτονική πόλη Blüdhaven και ηγήθηκε της ομάδας Teen Titans.",
            "Σε αρκετές περιόδους των κόμικς, όταν ο Bruce Wayne απουσίαζε, ο Dick Grayson ανέλαβε ο ίδιος τον ρόλο του Batman."
        ],
        "https://en.wikipedia.org/wiki/Dick_Grayson",
        ["nightwing", "dick_grayson", "batman", "robin", "dc_comics"]
    ),
    # 223
    make_q(
        "pop_culture_med_223",
        "Ποιος Robin δολοφονήθηκε άγρια από τον Joker με λοστό το 1988 μετά από τηλεφωνική ψηφοφορία των αναγνωστών και επέστρεψε ως Red Hood;",
        "Jason Todd",
        ["Dick Grayson", "Tim Drake", "Stephanie Brown"],
        "Στην ιστορία 'A Death in the Family', η DC οργάνωσε τηλεφωνική ψηφοφορία όπου οι αναγνώστες αποφάσισαν με οριακή πλειοψηφία (5.343 έναντι 5.271) τον θάνατο του Jason Todd.",
        [
            "Χρόνια αργότερα ο Todd αναστήθηκε μέσω των Lazarus Pits και επέστρεψε ως ο αμείλικτος ένοπλος αντιήρωας Red Hood.",
            "Ο θάνατός του αποτέλεσε το μεγαλύτερο τραύμα στην καριέρα του Batman μέχρι την επιστροφή του."
        ],
        "https://en.wikipedia.org/wiki/Jason_Todd",
        ["jason_todd", "red_hood", "batman", "dc_comics"]
    ),
    # 224
    make_q(
        "pop_culture_med_224",
        "Ποιο είναι το επίσημο εβραϊκό όνομα γέννησης του Magneto πριν υιοθετήσει το ψευδώνυμο Erik Lehnsherr στα κόμικς της Marvel;",
        "Max Eisenhardt",
        ["Jakob Eisenberg", "David Haller", "Nathaniel Essex"],
        "Το πραγματικό όνομα του Magneto αποκαλύφθηκε πλήρως στη σειρά 'X-Men: Magneto Testament' (2008), καταγράφοντας τα παιδικά του χρόνια στο Άουσβιτς.",
        [
            "Κατά τη διάρκεια του Β' Παγκοσμίου Πολέμου υπήρξε μέλος των Sonderkommando στο στρατόπεδο εξόντωσης του Άουσβιτς.",
            "Μετά τον πόλεμο υιοθέτησε την ταυτότητα του Erik Lehnsherr για να κρυφτεί από τις διώξεις."
        ],
        "https://en.wikipedia.org/wiki/Magneto_(character)",
        ["magneto", "marvel", "xmen", "max_eisenhardt"]
    ),
    # 225
    make_q(
        "pop_culture_med_225",
        "Ποιος ανθρωπολόγος επιστήμονας σχεδίασε τα γιγάντια ρομπότ Sentinels για να κυνηγήσουν και να εξολοθρεύσουν τους μεταλλαγμένους στα X-Men;",
        "Bolivar Trask",
        ["Miles Warren", "Arnim Zola", "Justin Hammer"],
        "Ο Dr. Bolivar Trask πίστευε ότι η άνοδος του Homo superior θα οδηγούσε στον αφανισμό της ανθρωπότητας, δημιουργώντας τα Sentinels.",
        [
            "Στην ταινία 'X-Men: Days of Future Past' (2014), τον Bolivar Trask υποδύθηκε ο Peter Dinklage.",
            "Ειρωνικά, ο γιος του Trask, Larry, αποδείχθηκε αργότερα ότι ήταν και ο ίδιος μεταλλαγμένος με δυνάμεις πρόβλεψης του μέλλοντος."
        ],
        "https://en.wikipedia.org/wiki/Bolivar_Trask",
        ["bolivar_trask", "sentinels", "xmen", "marvel"]
    ),
    # 226
    make_q(
        "pop_culture_med_226",
        "Πώς ονομάζεται το πανίσχυρο τσεκούρι μάχης που σφυρηλάτησε ο Thor στο Nidavellir στην ταινία 'Avengers: Infinity War';",
        "Stormbreaker",
        ["Mjolnir", "Jarnbjorn", "Gungnir"],
        "Το Stormbreaker σχεδιάστηκε ως το ισχυρότερο όπλο στην ιστορία του Asgard, ικανό να συγκρατεί τις δυνάμεις του Bifrost.",
        [
            "Η λαβή του Stormbreaker δημιουργήθηκε από το ίδιο το χέρι του Groot, που κόπηκε εθελοντικά για να ενώσει τις δύο μεταλλικές λεπίδες.",
            "Στα κλασικά κόμικς της Marvel, το Stormbreaker δόθηκε αρχικά από τον Odin στον εξωγήινο πολεμιστή Beta Ray Bill."
        ],
        "https://en.wikipedia.org/wiki/Stormbreaker",
        ["thor", "stormbreaker", "marvel", "avengers"]
    ),
    # 227
    make_q(
        "pop_culture_med_227",
        "Ποιο φανταστικό ευρωπαϊκό κράτος κυβερνά με σιδηρά πυγμή ο Victor von Doom (Doctor Doom) στα κόμικς της Marvel;",
        "Λατβέρια (Latveria)",
        ["Σοκόβια", "Συμκαρία", "Βλαστοβία"],
        "Η Latveria είναι ένα απομονωμένο κράτος στα Βαλκάνια που συνδυάζει μεσαιωνική αισθητική με υπερσύγχρονη ρομποτική τεχνολογία Doombots.",
        [
            "Παρότι ο Doom είναι αδίστακτος δικτάτορας, ο λαός της Latveria απολαμβάνει μηδενική εγκληματικότητα, δωρεάν υγεία και παιδεία.",
            "Η πρωτεύουσα της Latveria ονομάζεται Doomstadt."
        ],
        "https://en.wikipedia.org/wiki/Latveria",
        ["doctor_doom", "latveria", "marvel", "fantastic_four"]
    ),
    # 228
    make_q(
        "pop_culture_med_228",
        "Ποιο είναι το πραγματικό όνομα του Silver Surfer, του αστρικού κήρυκα που θυσίασε την ελευθερία του για να σώσει τον πλανήτη Zenn-La;",
        "Norrin Radd",
        ["Adam Warlock", "Richard Rider", "Wendell Vaughn"],
        "Ο Norrin Radd συμφώνησε να υπηρετήσει τον κοσμικό καταβροχθιστή κόσμων Galactus ως κήρυκας για να σώσει την αγαπημένη του Shalla-Bal και την πατρίδα του.",
        [
            "Ο Galactus τού χάρισε το Power Cosmic, μετατρέποντας το σώμα του σε άφθαρτη ασημένια ουσία και δίνοντάς του μια διαστρική σανίδα.",
            "Ο Silver Surfer πρωτοεμφανίστηκε στο Fantastic Four #48 το 1966, σχεδιασμένος από τον Jack Kirby."
        ],
        "https://en.wikipedia.org/wiki/Silver_Surfer",
        ["silver_surfer", "norrin_radd", "marvel", "fantastic_four"]
    ),
    # 229
    make_q(
        "pop_culture_med_229",
        "Ποιο είναι το πραγματικό ονοματεπώνυμο του πανίσχυρου άρχοντα του οργανωμένου εγκλήματος Kingpin στα κόμικς της Marvel;",
        "Wilson Fisk",
        ["Hammerhead", "Silvio Manfredi", "Lonnie Lincoln"],
        "Ο Wilson Fisk ελέγχει το υπόβαθρο της Νέας Υόρκης κρυμμένος πίσω από την πρόσοψη ενός ευυπόληπτου επιχειρηματία και φιλάνθρωπου.",
        [
            "Είναι ο κύριος αντίπαλος του Daredevil και του Spider-Man, διαθέτοντας τεράστια σωματική δύναμη από καθαρό μυϊκό ιστό.",
            "Στη σειρά Daredevil του Netflix και στο MCU, τον Fisk υποδύθηκε συγκλονιστικά ο Vincent D'Onofrio."
        ],
        "https://en.wikipedia.org/wiki/Kingpin_(character)",
        ["kingpin", "wilson_fisk", "daredevil", "marvel"]
    ),
    # 230
    make_q(
        "pop_culture_med_230",
        "Ποιος κλώνος του Peter Parker έγινε γνωστός ως Scarlet Spider φορώντας κόκκινη στολή με μπλε αμάνικο φούτερ;",
        "Ben Reilly",
        ["Kaine Parker", "Miles Morales", "Miguel O'Hara"],
        "Ο Ben Reilly δημιουργήθηκε από τον Jackal (Miles Warren) και πήρε το όνομά του από τον θείο Ben και το πατρικό επώνυμο της θείας May (Reilly).",
        [
            "Πρωταγωνίστησε στο περίφημο και πολυσυζητημένο 'Clone Saga' της δεκαετίας του 1990.",
            "Για ένα διάστημα στη δεκαετία του '90, ο Ben Reilly είχε αναλάβει τον επίσημο ρόλο του Spider-Man στα βασικά κόμικς."
        ],
        "https://en.wikipedia.org/wiki/Ben_Reilly",
        ["spiderman", "scarlet_spider", "ben_reilly", "marvel"]
    ),
    # 231
    make_q(
        "pop_culture_med_231",
        "Ποιο τραγούδι της 13χρονης Rebecca Black έγινε viral το 2011 συγκεντρώνοντας εκατομμύρια dislikes και τον τίτλο 'το χειρότερο τραγούδι όλων των εποχών';",
        "Friday",
        ["Saturday", "Thanksgiving", "My Jeans"],
        "Το τραγούδι 'Friday' παρήχθη από την εταιρεία Ark Music Factory και οι απλοϊκοί στίχοι του για τις ημέρες της εβδομάδας έγιναν παγκόσμιο meme.",
        [
            "Παρά τον χλευασμό, το βίντεο ξεπέρασε τις 160 εκατομμύρια προβολές και μπήκε στο Billboard Hot 100.",
            "Η ίδια η Black αργότερα αγκάλιασε το τραγούδι και κυκλοφόρησε ένα επετειακό remix για τα 10 χρόνια το 2021."
        ],
        "https://en.wikipedia.org/wiki/Friday_(Rebecca_Black_song)",
        ["rebecca_black", "friday", "viral", "youtube", "memes"]
    ),
    # 232
    make_q(
        "pop_culture_med_232",
        "Ποιο ήταν το πραγματικό μικρό όνομα του πρωταγωνιστή του διάσημου meme 'Bad Luck Brian' με το καρό γιλέκο και τα σιδεράκια;",
        "Kyle (Kyle Craven)",
        ["Brian", "Kevin", "Justin"],
        "Ο πρωταγωνιστής της φωτογραφίας της σχολικής επετηρίδας ονομάζεται στην πραγματικότητα Kyle Craven και όχι Brian.",
        [
            "Η φωτογραφία αναρτήθηκε στο Reddit το 2012 από τον φίλο του Ian Davies με τη λεζάντα 'Δίνει εξετάσεις οδήγησης... παίρνει κλήση για οδήγηση υπό την επήρεια'.",
            "Ο Craven είχε φορέσει σκόπιμα το καρό γιλέκο και είχε πάρει αυτή την περίεργη έκφραση για να πειράξει τον διευθυντή του σχολείου."
        ],
        "https://en.wikipedia.org/wiki/Bad_Luck_Brian",
        ["bad_luck_brian", "memes", "reddit", "viral"]
    ),
    # 233
    make_q(
        "pop_culture_med_233",
        "Σε ποια χώρα τραβήχτηκε το 2015 η διάσημη φωτογραφία αρχείου (stock photo) που έγινε το viral meme 'Distracted Boyfriend';",
        "Ισπανία",
        ["Ιταλία", "ΗΠΑ", "Γαλλία"],
        "Η φωτογραφία τραβήχτηκε στη Χιρόνα της Ισπανίας από τον φωτογράφο Antonio Guillem, ο οποίος συνεργαζόταν τακτικά με τα ίδια τρία μοντέλα.",
        [
            "Ο επίσημος τίτλος της φωτογραφίας στις βιβλιοθήκες stock εικόνων ήταν 'Disloyal man walking with his girlfriend and looking amazed at another seductive girl'.",
            "Κέρδισε το βραβείο 'Meme of the Year' στα 10α ετήσια Shorty Awards το 2018."
        ],
        "https://en.wikipedia.org/wiki/Distracted_boyfriend",
        ["distracted_boyfriend", "stock_photo", "memes", "viral"]
    ),
    # 234
    make_q(
        "pop_culture_med_234",
        "Ποιος Ούγγρος συνταξιούχος ηλεκτρολόγος μηχανικός έγινε παγκόσμιο meme ως 'Hide the Pain Harold' λόγω του αμήχανου χαμόγελού του;",
        "András Arató",
        ["László Kovács", "Zoltán Gera", "Béla Tarr"],
        "Ο András Arató φωτογραφήθηκε για επαγγελματικές stock φωτογραφίες και το βλέμμα του, που έμοιαζε να συγκρατεί κρυφό πόνο, έγινε viral.",
        [
            "Αρχικά ένιωσε άβολα με τη διασημότητα, αλλά αργότερα αποδέχτηκε τον ρόλο του δίνοντας ακόμη και ομιλία TEDx για την εμπειρία του.",
            "Έχει πρωταγωνιστήσει σε διαφημιστικές καμπάνιες για διεθνείς κολοσσούς όπως η Coca-Cola και η Manchester City."
        ],
        "https://en.wikipedia.org/wiki/Andr%C3%A1s_Arat%C3%B3",
        ["hide_the_pain_harold", "andras_arato", "memes", "viral"]
    ),
    # 235
    make_q(
        "pop_culture_med_235",
        "Ποιος Βιετναμέζος προγραμματιστής δημιούργησε το εξαιρετικά εθιστικό mobile game Flappy Bird και το απέσυρε ξαφνικά το 2014;",
        "Dong Nguyen",
        ["Hideo Kojima", "Shigeru Miyamoto", "Satoshi Tajiri"],
        "Ο Dong Nguyen απέσυρε το Flappy Bird από τα App Store και Google Play επειδή ένιωσε ένοχος για τον ακραίο εθισμό που προκαλούσε στους παίκτες.",
        [
            "Την περίοδο της απόσυρσης, το παιχνίδι απέφερε στον δημιουργό περίπου 50.000 δολάρια την ημέρα από διαφημίσεις.",
            "Κινητά τηλέφωνα που είχαν ήδη εγκατεστημένο το παιχνίδι πωλούνταν στο eBay για χιλιάδες δολάρια μετά την κατάργησή του."
        ],
        "https://en.wikipedia.org/wiki/Flappy_Bird",
        ["flappy_bird", "dong_nguyen", "mobile_games", "viral"]
    ),
    # 236
    make_q(
        "pop_culture_med_236",
        "Ποιο απλό καθημερινό αντικείμενο κατέρριψε το παγκόσμιο ρεκόρ των περισσότερων likes στο Instagram τον Ιανουάριο του 2019;",
        "Ένα αυγό (World Record Egg)",
        ["Μια μπανάνα", "Ένα φλιτζάνι καφέ", "Μια φέτα πίτσα"],
        "Ο λογαριασμός @world_record_egg ανάρτησε τη φωτογραφία ενός απλού αυγού κότας με μοναδικό στόχο να ξεπεράσει το ρεκόρ των 18 εκατομμυρίων likes της Kylie Jenner.",
        [
            "Η ανάρτηση συγκέντρωσε τελικά πάνω από 50 εκατομμύρια likes μέσα σε λίγες ημέρες.",
            "Αργότερα αποκαλύφθηκε ότι η καμπάνια σχεδιάστηκε από τον διαφημιστή Chris Godfrey για την ευαισθητοποίηση σχετικά με την ψυχική υγεία."
        ],
        "https://en.wikipedia.org/wiki/World_record_egg",
        ["world_record_egg", "instagram", "viral", "social_media"]
    ),
    # 237
    make_q(
        "pop_culture_med_237",
        "Ποιο εμβληματικό πράσινο φόρεμα της Jennifer Lopez στα Grammy του 2000 οδήγησε άμεσα στην εφεύρεση του Google Images;",
        "Το πράσινο φόρεμα Versace (Green Versace Dress)",
        ["Το λευκό φόρεμα Dior", "Το κόκκινο φόρεμα Valentino", "Το μαύρο φόρεμα Gucci"],
        "Η ζήτηση για φωτογραφίες του αποκαλυπτικού πράσινου φορέματος της J.Lo με τροπικά μοτίβα ήταν τόσο σαρωτική που ώθησε τη Google να δημιουργήσει την αναζήτηση εικόνων.",
        [
            "Ο πρώην CEO της Google, Eric Schmidt, επιβεβαίωσε επίσημα ότι το φόρεμα αποτέλεσε τη γενεσιουργό αιτία για το Google Image Search.",
            "Η Jennifer Lopez φόρεσε μια ανανεωμένη έκδοση του ίδιου φορέματος στην επίδειξη μόδας του Versace στο Μιλάνο το 2019."
        ],
        "https://en.wikipedia.org/wiki/Green_Versace_dress_of_Jennifer_Lopez",
        ["jennifer_lopez", "versace", "google_images", "fashion"]
    ),
    # 238
    make_q(
        "pop_culture_med_238",
        "Ποιος ιδιοφυής Βρετανός σχεδιαστής μόδας ήταν διάσημος για τις σκοτεινές, θεατρικές επιδείξεις και τα μαντήλια με νεκροκεφαλές;",
        "Alexander McQueen (Lee McQueen)",
        ["John Galliano", "Vivienne Westwood", "Stella McCartney"],
        "Ο Lee Alexander McQueen υπήρξε καλλιτεχνικός διευθυντής του Givenchy (1996-2001) πριν επικεντρωθεί στον δικό του ομώνυμο πρωτοποριακό οίκο.",
        [
            "Στην επίδειξη Άνοιξη/Καλοκαίρι 1999, ρομποτικοί βραχίονες ψέκασαν με μπογιά σε πραγματικό χρόνο το λευκό φόρεμα του μοντέλου Shalom Harlow.",
            "Σχεδίασε τα διάσημα παπούτσια 'Armadillo' με τα οποία εμφανίστηκε η Lady Gaga στο βίντεο κλιπ του 'Bad Romance'."
        ],
        "https://en.wikipedia.org/wiki/Alexander_McQueen",
        ["alexander_mcqueen", "fashion", "haute_couture", "british"]
    ),
    # 239
    make_q(
        "pop_culture_med_239",
        "Ποιος Γερμανός σχεδιαστής με τη χαρακτηριστική άσπρη αλογοουρά, τα μαύρα γυαλιά και τα γάντια ηγήθηκε του οίκου Chanel για 36 χρόνια;",
        "Karl Lagerfeld",
        ["Jean-Paul Gaultier", "Christian Lacroix", "Hubert de Givenchy"],
        "Ο Karl Lagerfeld ανέλαβε τον οίκο Chanel το 1983 και αναζωογόνησε πλήρως τη μάρκα, σχεδιάζοντας ταυτόχρονα και για τον ιταλικό οίκο Fendi.",
        [
            "Η γάτα του, μια ράτσας Βιρμανίας με το όνομα Choupette, έγινε διάσημη σε όλο τον κόσμο και κληρονόμησε μέρος της περιουσίας του.",
            "Ήταν γνωστός για τα εντυπωσιακά θεματικά σκηνικά στο Grand Palais του Παρισιού, μετατρέποντάς το σε σούπερ μάρκετ, διαστημοδρόμιο ή παραλία."
        ],
        "https://en.wikipedia.org/wiki/Karl_Lagerfeld",
        ["karl_lagerfeld", "chanel", "fendi", "fashion"]
    ),
    # 240
    make_q(
        "pop_culture_med_240",
        "Ποιος ιταλικός οίκος πολυτελείας είναι διάσημος για την τεχνική πλεξίματος δέρματος 'Intrecciato' χωρίς εμφανή λογότυπα;",
        "Bottega Veneta",
        ["Salvatore Ferragamo", "Tod's", "Loro Piana"],
        "Η Bottega Veneta ιδρύθηκε στη Βιτσέντζα το 1966 και υιοθέτησε το περίφημο σλόγκαν: 'Όταν τα αρχικά σου είναι αρκετά' ('When your own initials are enough').",
        [
            "Η τεχνική intrecciato αναπτύχθηκε επειδή οι ραπτομηχανές της περιοχής ήταν φτιαγμένες για ρούχα και όχι για παχύ δέρμα, απαιτώντας λεπτό πλεγμένο δέρμα.",
            "Υπό τη δημιουργική διεύθυνση του Daniel Lee (2018-2021), η μάρκα γνώρισε τεράστια αναγέννηση με την τσάντα 'The Pouch' και τα παπούτσια 'Lido'."
        ],
        "https://en.wikipedia.org/wiki/Bottega_Veneta",
        ["bottega_veneta", "fashion", "intrecciato", "luxury"]
    ),
    # 241
    make_q(
        "pop_culture_med_241",
        "Ποιος Γάλλος σχεδιαστής σόκαρε την παγκόσμια μόδα το 1966 παρουσιάζοντας το 'Le Smoking', το πρώτο γυναικείο σμόκιν;",
        "Yves Saint Laurent",
        ["Christian Dior", "Pierre Cardin", "André Courrèges"],
        "Ο Yves Saint Laurent έφερε επανάσταση επιτρέποντας στις γυναίκες να φορούν ανδρικά κοστούμια σε επίσημες βραδινές εξόδους.",
        [
            "Αρχικά ορισμένα εστιατόρια και ξενοδοχεία αρνούνταν την είσοδο σε γυναίκες που φορούσαν το 'Le Smoking' θεωρώντας το ακατάλληλο.",
            "Η ιστορική ασπρόμαυρη φωτογραφία του Helmut Newton στο Παρίσι το 1975 εδραίωσε το κοστούμι ως διαχρονικό σύμβολο ανδρόγυνης κομψότητας."
        ],
        "https://en.wikipedia.org/wiki/Le_Smoking",
        ["yves_saint_laurent", "le_smoking", "fashion", "paris"]
    ),
    # 242
    make_q(
        "pop_culture_med_242",
        "Ποιο ιστορικό λευκό δερμάτινο παπούτσι τένις της Adidas με πράσινη φτέρνα πήρε το όνομά του από έναν Αμερικανό πρωταθλητή του Wimbledon;",
        "Stan Smith",
        ["Rod Laver", "Arthur Ashe", "Björn Borg"],
        "Το παπούτσι κυκλοφόρησε αρχικά το 1965 ως 'Robert Haillet' πριν μετονομαστεί το 1978 προς τιμήν του Νο 1 τενίστα στον κόσμο Stan Smith.",
        [
            "Το παπούτσι Stan Smith έχει πουλήσει πάνω από 50 εκατομμύρια ζευγάρια, αποτελώντας ένα από τα πιο επιτυχημένα sneakers όλων των εποχών.",
            "Ο ίδιος ο Stan Smith έχει αστειευτεί ότι πολλοί νέοι σήμερα νομίζουν πως είναι απλώς ένα παπούτσι και όχι πραγματικό πρόσωπο."
        ],
        "https://en.wikipedia.org/wiki/Adidas_Stan_Smith",
        ["adidas", "stan_smith", "sneakers", "tennis"]
    ),
    # 243
    make_q(
        "pop_culture_med_243",
        "Ποιος πρωτοποριακός βελγικός οίκος μόδας σχεδίασε τις εμβληματικές μπότες Tabi με τον χωρισμένο αντίχειρα το 1988;",
        "Maison Margiela (Martin Margiela)",
        ["Dries Van Noten", "Ann Demeulemeester", "Raf Simons"],
        "Ο Martin Margiela εμπνεύστηκε τις μπότες Tabi από τις παραδοσιακές ιαπωνικές κάλτσες του 15ου αιώνα που χωρίζουν το μεγάλο δάχτυλο.",
        [
            "Στην πρώτη του επίδειξη το 1988, τα μοντέλα πάτησαν σε κόκκινη μπογιά αφήνοντας ίχνη σαν οπλές σε λευκό ύφασμα.",
            "Ο Martin Margiela υπήρξε διάσημος για την απόλυτη ανωνυμία του, αρνούμενος να φωτογραφηθεί ή να δώσει συνεντεύξεις πρόσωπο με πρόσωπο."
        ],
        "https://en.wikipedia.org/wiki/Maison_Margiela",
        ["margiela", "tabi_boots", "fashion", "belgium"]
    ),
    # 244
    make_q(
        "pop_culture_med_244",
        "Ποιες κούκλες της δεκαετίας του 1980 με μάλλινα μαλλιά και 'πιστοποιητικά υιοθεσίας' προκάλεσαν μαζικές μάχες στα καταστήματα παιχνιδιών;",
        "Cabbage Patch Kids",
        ["Rainbow Brite", "Strawberry Shortcake", "Care Bears"],
        "Οι κούκλες Cabbage Patch Kids δημιουργήθηκαν από τον Xavier Roberts και κάθε κούκλα ήταν μοναδική, προκαλώντας καταναλωτική υστερία τα Χριστούγεννα του 1983.",
        [
            "Οι γονείς σχημάτιζαν ουρές για ώρες και συνεπλάκησαν σωματικά στα καταστήματα στις ΗΠΑ, φαινόμενο γνωστό ως 'Cabbage Patch Riots'.",
            "Κάθε κούκλα ερχόταν με δικό της όνομα, ημερομηνία γέννησης και υπογραφή του Roberts στο πίσω μέρος."
        ],
        "https://en.wikipedia.org/wiki/Cabbage_Patch_Kids",
        ["cabbage_patch_kids", "toys", "80s", "fads"]
    ),
    # 245
    make_q(
        "pop_culture_med_245",
        "Ποια λούτρινα ζωάκια της εταιρείας Ty γεμισμένα με πλαστικούς κόκκους προκάλεσαν μια τεράστια κερδοσκοπική φούσκα τη δεκαετία του 1990;",
        "Beanie Babies",
        ["Webkinz", "Squishmallows", "Pillow Pets"],
        "Ο Ty Warner λάνσαρε τα Beanie Babies το 1993 και απέσυρε σκόπιμα συγκεκριμένα σχέδια, ωθώντας συλλέκτες να πληρώνουν χιλιάδες δολάρια θεωρώντας τα 'επένδυση'.",
        [
            "Τα ζωάκια είχαν χαρακτηριστική κόκκινη καρδούλα-ετικέτα με ένα μικρό ποίημα και ημερομηνία γέννησης.",
            "Η κερδοσκοπική μανία κατέρρευσε απότομα γύρω στο 1999, αφήνοντας πολλούς συλλέκτες με χιλιάδες σχεδόν άχρηστα λούτρινα."
        ],
        "https://en.wikipedia.org/wiki/Beanie_Babies",
        ["beanie_babies", "ty_warner", "toys", "90s", "bubble"]
    ),
    # 246
    make_q(
        "pop_culture_med_246",
        "Σε ποιο πολυβραβευμένο επιτραπέζιο παιχνίδι του Alan R. Moon οι παίκτες συλλέγουν κάρτες τρένων για να ενώσουν πόλεις με σιδηροδρομικές γραμμές;",
        "Ticket to Ride",
        ["TransAmerica", "Railway Rivals", "Steam"],
        "Στο Ticket to Ride, οι παίκτες συνδέουν πόλεις σε έναν χάρτη (π.χ. Βόρειας Αμερικής ή Ευρώπης) συμπληρώνοντας μυστικά εισιτήρια διαδρομών.",
        [
            "Κέρδισε το κορυφαίο βραβείο Spiel des Jahres (Παιχνίδι της Χρονιάς στη Γερμανία) το 2004.",
            "Έχει πουλήσει πάνω από 15 εκατομμύρια αντίτυπα παγκοσμίως και διαθέτει δεκάδες επεκτάσεις με χάρτες διαφόρων χωρών."
        ],
        "https://en.wikipedia.org/wiki/Ticket_to_Ride_(board_game)",
        ["ticket_to_ride", "board_games", "trains"]
    ),
    # 247
    make_q(
        "pop_culture_med_247",
        "Ποιο από τα παρακάτω ΔΕΝ ήταν ένα από τα αρχικά 6 όπλα του κλασικού επιτραπέζιου παιχνιδιού Cluedo;",
        "Δηλητήριο (Poison)",
        ["Κηροπήγιο (Candlestick)", "Μαχαίρι (Dagger)", "Γαλλικό κλειδί (Wrench)"],
        "Τα 6 αρχικά επίσημα όπλα του Cluedo είναι: Κηροπήγιο, Μαχαίρι, Σιδεροσωλήνας, Περίστροφο, Σχοινί και Γαλλικό κλειδί. Το δηλητήριο προστέθηκε μόνο σε μεταγενέστερες ειδικές εκδόσεις.",
        [
            "Στον αρχικό σχεδιασμό του Anthony Pratt υπήρχαν 10 όπλα, ανάμεσά τους τσεκούρι και βόμβα, αλλά μειώθηκαν στα 6 για λόγους ισορροπίας.",
            "Στο αμερικανικό Clue, το 'Dagger' μετονομάστηκε σε 'Knife' και το 'Lead Piping' σε 'Lead Pipe'."
        ],
        "https://en.wikipedia.org/wiki/Cluedo",
        ["cluedo", "board_games", "mystery"]
    ),
    # 248
    make_q(
        "pop_culture_med_248",
        "Ποιο διάσημο γερμανικό επιτραπέζιο παιχνίδι πλακιδίων του Klaus-Jürgen Wrede πήρε το όνομά του από μια μεσαιωνική οχυρωμένη πόλη της Γαλλίας;",
        "Carcassonne",
        ["Avignon", "Mont Saint-Michel", "Colmar"],
        "Στο Carcassonne, οι παίκτες τραβούν πλακίδια και χτίζουν συλλογικά έναν μεσαιωνικό χάρτη με δρόμους, πόλεις, μοναστήρια και λιβάδια τοποθετώντας 'meeples'.",
        [
            "Κέρδισε το περίβλεπτο βραβείο Spiel des Jahres το 2001.",
            "Ο όρος 'meeple' (σύντμηση του 'my people' για τα ξύλινα ανθρωπάκια) γεννήθηκε κατά τη διάρκεια μιας παρτίδας Carcassonne το 2000."
        ],
        "https://en.wikipedia.org/wiki/Carcassonne_(board_game)",
        ["carcassonne", "board_games", "meeples", "spiel_des_jahres"]
    ),
    # 249
    make_q(
        "pop_culture_med_249",
        "Ποιο διάσημο παιχνίδι στρατηγικής με μινιατούρες της Games Workshop διαδραματίζεται στη σκοτεινή 41η χιλιετία;",
        "Warhammer 40,000",
        ["BattleTech", "Warmachine", "Infinity"],
        "Το Warhammer 40k εισήγαγε τη διάσημη φράση: 'Στο ζοφερό σκοτάδι του μακρινού μέλλοντος, υπάρχει μόνο πόλεμος' ('In the grim darkness of the far future, there is only war').",
        [
            "Οι Space Marines (Adeptus Astartes) είναι οι γενετικά ενισχυμένοι υπερστρατιώτες που προστατεύουν το ανθρώπινο Imperium.",
            "Ο όρος 'grimdark' στην επιστημονική φαντασία προήλθε απευθείας από το σλόγκαν του Warhammer 40k."
        ],
        "https://en.wikipedia.org/wiki/Warhammer_40,000",
        ["warhammer_40k", "miniatures", "tabletop", "games_workshop"]
    ),
    # 250
    make_q(
        "pop_culture_med_250",
        "Σε ποιον πλανήτη διαδραματίζονται οι περιπέτειες του He-Man και των 'Κυρίαρχων του Σύμπαντος' (Masters of the Universe);",
        "Eternia",
        ["Thundera", "Cybertron", "Third Earth"],
        "Ο He-Man (πρίγκιπας Adam) προστατεύει τον πλανήτη Eternia και τα μυστικά του κάστρου Grayskull από τον διαβολικό Skeletor.",
        [
            "Για να μεταμορφωθεί, ο Adam σηκώνει το Power Sword και φωνάζει: 'By the power of Grayskull... I HAVE THE POWER!'.",
            "Η Mattel δημιούργησε τη σειρά παιχνιδιών το 1982 αφού απέρριψε τα δικαιώματα για τα παιχνίδια του Star Wars."
        ],
        "https://en.wikipedia.org/wiki/Masters_of_the_Universe",
        ["he_man", "eternia", "mattel", "80s", "animation"]
    ),
    # 251
    make_q(
        "pop_culture_med_251",
        "Ποια είναι η χαρακτηριστική ενεργειακή επίθεση του Goku στο Dragon Ball, την οποία διδάχθηκε από τον Master Roshi;",
        "Kamehameha",
        ["Final Flash", "Spirit Bomb", "Special Beam Cannon"],
        "Το Kamehameha απαιτεί τη συγκέντρωση της ενέργειας ki στα χέρια πριν από την εκτόξευσή της σε μια πανίσχυρη γαλάζια ακτίνα.",
        [
            "Ο δημιουργός Akira Toriyama εμπνεύστηκε το όνομα από τον ιστορικό βασιλιά Kamehameha I της Χαβάης μετά από πρόταση της συζύγου του.",
            "Ο Master Roshi χρειάστηκε 50 χρόνια για να επινοήσει την τεχνική, ενώ ο Goku την αντέγραψε επιτυχώς με την πρώτη προσπάθεια."
        ],
        "https://en.wikipedia.org/wiki/Dragon_Ball",
        ["dragon_ball", "goku", "kamehameha", "anime", "manga"]
    ),
    # 252
    make_q(
        "pop_culture_med_252",
        "Ποιο είναι το πραγματικό όνομα του θηρίου με τις εννέα ουρές (Nine-Tails) που είναι σφραγισμένο μέσα στον Naruto Uzumaki;",
        "Kurama",
        ["Shukaku", "Gyuki", "Matatabi"],
        "Ο Kurama είναι μια γιγάντια αλεπού από συμπυκνωμένο τσάκρα, που αρχικά μισούσε τους ανθρώπους πριν γίνει ισόβιος σύμμαχος του Naruto.",
        [
            "Ο δημιουργός Masashi Kishimoto ονόμασε το πλάσμα από το ιστορικό όρος Kurama στην Ιαπωνία.",
            "Η σφράγιση του Kurama μέσα στον νεογέννητο Naruto κόστισε τη ζωή των γονιών του, Minato Namikaze και Kushina Uzumaki."
        ],
        "https://en.wikipedia.org/wiki/Naruto",
        ["naruto", "kurama", "nine_tails", "anime"]
    ),
    # 253
    make_q(
        "pop_culture_med_253",
        "Στο δημοφιλές anime και manga 'Death Note', τι υπερφυσικό πλάσμα είναι ο Ryuk που λατρεύει να τρώει μήλα;",
        "Shinigami (Θεός του Θανάτου)",
        ["Yokai", "Akuma", "Oni"],
        "Ο Ryuk είναι ένας Shinigami που από καθαρή ανία ρίχνει το υπερφυσικό τετράδιο Death Note στον ανθρώπινο κόσμο, όπου το βρίσκει ο Light Yagami.",
        [
            "Ο Ryuk αναπτύσσει εθισμό στα ανθρώπινα μήλα, δηλώνοντας ότι για τους Shinigami είναι σαν το αλκοόλ ή το τσιγάρο.",
            "Ο κανόνας του τετραδίου ορίζει: 'Ο άνθρωπος του οποίου το όνομα γράφεται σε αυτό το σημειωματάριο θα πεθάνει'."
        ],
        "https://en.wikipedia.org/wiki/Death_Note",
        ["death_note", "ryuk", "shinigami", "anime"]
    ),
    # 254
    make_q(
        "pop_culture_med_254",
        "Ποιο είναι το πραγματικό ιαπωνικό όνομα της μαθήτριας Usagi Tsukino όταν δεν πολεμά ως η υπερηρωίδα Sailor Moon;",
        "Usagi Tsukino",
        ["Ami Mizuno", "Rei Hino", "Makoto Kino"],
        "Η Usagi Tsukino είναι μια ανέμελη μαθήτρια που ανακαλύπτει ότι είναι η μετενσάρκωση της Πριγκίπισσας Serenity του Φεγγαριού.",
        [
            "Το όνομα 'Tsukino Usagi' αποτελεί ιαπωνικό λογοπαίγνιο με τη φράση 'tsuki no usagi', που σημαίνει 'ο λαγός του φεγγαριού'.",
            "Η σειρά της Naoko Takeuchi καθόρισε παγκοσμίως το είδος των 'magical girls' (mahou shoujo)."
        ],
        "https://en.wikipedia.org/wiki/Sailor_Moon_(character)",
        ["sailor_moon", "usagi_tsukino", "anime", "manga"]
    ),
    # 255
    make_q(
        "pop_culture_med_255",
        "Πώς ονομάζεται ο στρατιωτικός κλάδος στο 'Attack on Titan' που αναλαμβάνει τις επικίνδυνες αποστολές έξω από τα τείχη;",
        "Σώμα Εξερεύνησης (Survey Corps / Scout Regiment)",
        ["Στρατιωτική Αστυνομία", "Φρουρά των Τειχών", "Βασιλική Φρουρά"],
        "Το Σώμα Εξερεύνησης φέρει ως έμβλημα τα 'Φτερά της Ελευθερίας' (Wings of Freedom) και μάχεται για την ανακάλυψη της αλήθειας για τους Τιτάνες.",
        [
            "Χρησιμοποιούν τον Εξοπλισμό Πανκατευθυντικής Κινητικότητας (ODM gear) για να ελίσσονται στον αέρα και να χτυπούν τους Τιτάνες στον αυχένα.",
            "Ο Captain Levi Ackerman του Σώματος Εξερεύνησης θεωρείται 'ο ισχυρότερος στρατιώτης της ανθρωπότητας'."
        ],
        "https://en.wikipedia.org/wiki/Attack_on_Titan",
        ["attack_on_titan", "survey_corps", "anime", "manga"]
    ),
    # 256
    make_q(
        "pop_culture_med_256",
        "Ποια αριστουργηματική ταινία του Hayao Miyazaki και του Studio Ghibli κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2003;",
        "Spirited Away (Ταξίδι στη Χώρα των Θαυμάτων)",
        ["Princess Mononoke", "Howl's Moving Castle", "My Neighbor Totoro"],
        "Το 'Spirited Away' (Sen to Chihiro no Kamikakushi) αφηγείται την ιστορία της 10χρονης Chihiro που παγιδεύεται σε έναν κόσμο πνευμάτων.",
        [
            "Παραμένει η μοναδική χειροποίητη μη-αγγλόφωνη ταινία anime που έχει κερδίσει το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων.",
            "Υπήρξε η πιο επιτυχημένη εισπρακτικά ταινία στην ιστορία του ιαπωνικού κινηματογράφου για 19 ολόκληρα χρόνια."
        ],
        "https://en.wikipedia.org/wiki/Spirited_Away",
        ["spirited_away", "hayao_miyazaki", "studio_ghibli", "anime", "oscars"]
    ),
    # 257
    make_q(
        "pop_culture_med_257",
        "Ποιο μυθικό Φρούτο του Διαβόλου έφαγε ο Monkey D. Luffy στο 'One Piece' αποκτώντας ένα σώμα με ιδιότητες απόλυτου καουτσούκ;",
        "Gomu Gomu no Mi",
        ["Mera Mera no Mi", "Ope Ope no Mi", "Hito Hito no Mi"],
        "Το φρούτο έδωσε στον Luffy την ικανότητα να τεντώνει το σώμα του σαν λάστιχο και να είναι απρόσβλητος σε ηλεκτρισμό και αμβλείες κρούσεις.",
        [
            "Αργότερα στην ιστορία αποκαλύπτεται ότι το πραγματικό όνομα του φρούτου είναι το μυθικό Zoan 'Hito Hito no Mi, Model: Nika'.",
            "Το 'One Piece' του Eiichiro Oda κατέχει το ρεκόρ Γκίνες για τα περισσότερα αντίτυπα που έχουν εκδοθεί για την ίδια σειρά κόμικ από έναν συγγραφέα (πάνω από 500 εκατομμύρια)."
        ],
        "https://en.wikipedia.org/wiki/One_Piece",
        ["one_piece", "luffy", "devil_fruit", "anime", "manga"]
    ),
    # 258
    make_q(
        "pop_culture_med_258",
        "Ποιος χαρισματικός κυνηγός επικηρυγμένων και πρώην μέλος του συνδικάτου Red Dragon είναι ο πρωταγωνιστής του anime 'Cowboy Bebop';",
        "Spike Spiegel",
        ["Jet Black", "Vicious", "Faye Valentine"],
        "Ο Spike Spiegel είναι ένας ικανότατος πιλότος και σκοπευτής που εξασκεί τη φιλοσοφία πολεμικών τεχνών Jeet Kune Do του Bruce Lee.",
        [
            "Το διαστημόπλοιο της ομάδας ονομάζεται Bebop και το πιστό σκυλί ράτσας Corgi ονομάζεται Ein.",
            "Η σειρά του Shinichirō Watanabe (1998) θεωρείται ένα από τα κορυφαία anime όλων των εποχών χάρη στην εξαιρετική τζαζ μουσική της Yoko Kanno."
        ],
        "https://en.wikipedia.org/wiki/Spike_Spiegel",
        ["cowboy_bebop", "spike_spiegel", "anime"]
    ),
    # 259
    make_q(
        "pop_culture_med_259",
        "Ποιο θεωρητικά αδύναμο και άχρηστο ψάρι Pokémon εξελίσσεται στο πανίσχυρο και τρομακτικό θαλάσσιο δράκο Gyarados;",
        "Magikarp",
        ["Goldeen", "Feebas", "Remoraid"],
        "Το Magikarp γνωρίζει μόνο την επίθεση 'Splash' που δεν προκαλεί καμία ζημιά, αλλά στο επίπεδο 20 μεταμορφώνεται στον πανίσχυρο Gyarados.",
        [
            "Η εξέλιξη βασίζεται σε έναν αρχαίο κινεζικό μύθο σύμφωνα με τον οποίο ένας κυπρίνος που πηδάει πάνω από την Πύλη του Δράκου μεταμορφώνεται σε ουράνιο δράκο.",
            "Το Magikarp έχει γίνει ένα από τα πιο αναγνωρίσιμα memes στον κόσμο των βιντεοπαιχνιδιών."
        ],
        "https://en.wikipedia.org/wiki/Magikarp",
        ["pokemon", "magikarp", "gyarados", "nintendo"]
    ),
    # 260
    make_q(
        "pop_culture_med_260",
        "Ποιος εσωστρεφής 14χρονος έφηβος πιλοτάρει το βιομηχανικό γιγάντιο ρομπότ EVA-01 στο ψυχολογικό anime 'Neon Genesis Evangelion';",
        "Shinji Ikari",
        ["Kaworu Nagisa", "Asuka Langley", "Toji Suzuhara"],
        "Ο Shinji Ikari εξαναγκάζεται από τον απόμακρο πατέρα του Gendo Ikari να πολεμήσει τα εξωγήινα όντα γνωστά ως 'Άγγελοι' για να σώσει το Τόκιο-3.",
        [
            "Η φράση 'Get in the robot, Shinji' έγινε ένα από τα πιο διάσημα pop culture memes του διαδικτύου.",
            "Η σειρά του Hideaki Anno (1995) εξερεύνησε βαθιά θέματα κατάθλιψης, υπαρξισμού και ψυχανάλυσης."
        ],
        "https://en.wikipedia.org/wiki/Shinji_Ikari",
        ["evangelion", "shinji_ikari", "anime", "hideaki_anno"]
    ),
    # 261
    make_q(
        "pop_culture_med_261",
        "Ποιος Γάλλος σχεδιαστής υψηλής ραπτικής δημιούργησε τον περίφημο κωνικό κορσέ (cone bra) της Madonna για την περιοδεία Blond Ambition (1990);",
        "Jean-Paul Gaultier",
        ["Thierry Mugler", "Claude Montana", "Christian Lacroix"],
        "Ο Jean-Paul Gaultier σχεδίασε τον εμβληματικό ροζ σατέν κωνικό κορσέ, μετατρέποντας τα εσώρουχα σε δήλωση γυναικείας δύναμης και σεξουαλικότητας.",
        [
            "Ο Gaultier είχε πειραματιστεί με κωνικά σχήματα σε αρκουδάκια όταν ήταν παιδί πριν τα παρουσιάσει στην πασαρέλα τη δεκαετία του '80.",
            "Η εμφάνιση της Madonna θεωρείται μία από τις πιο επιδραστικές στιγμές στην ιστορία της μόδας και της ποπ μουσικής."
        ],
        "https://en.wikipedia.org/wiki/Jean-Paul_Gaultier",
        ["madonna", "jean_paul_gaultier", "cone_bra", "fashion"]
    ),
    # 262
    make_q(
        "pop_culture_med_262",
        "Ποιο ήταν το όνομα της φιλανθρωπικής συναυλίας του George Harrison το 1971 που θεωρείται η πρώτη μεγάλη ροκ συναυλία αλληλεγγύης;",
        "The Concert for Bangladesh",
        ["Live Aid", "Farm Aid", "Live 8"],
        "Ο George Harrison και ο Ravi Shankar οργάνωσαν δύο συναυλίες στο Madison Square Garden για να βοηθήσουν τους πρόσφυγες του Μπανγκλαντές.",
        [
            "Στη συναυλία συμμετείχαν θρύλοι όπως ο Bob Dylan, ο Eric Clapton και ο Ringo Starr.",
            "Αποτέλεσε το ιστορικό πρότυπο για μεταγενέστερες μεγαλειώδεις συναυλίες όπως το Live Aid του Bob Geldof το 1985."
        ],
        "https://en.wikipedia.org/wiki/The_Concert_for_Bangladesh",
        ["george_harrison", "bangladesh", "rock_music", "charity"]
    ),
    # 263
    make_q(
        "pop_culture_med_263",
        "Ποιο ήταν το πραγματικό όνομα γέννησης του θρυλικού τραγουδιστή των Queen, Freddie Mercury, που γεννήθηκε στη Ζανζιβάρη;",
        "Farrokh Bulsara",
        ["David Jones", "Reginald Dwight", "Declan McManus"],
        "Ο Farrokh Bulsara μεγάλωσε στην Ινδία και τη Ζανζιβάρη πριν μετακομίσει στην Αγγλία και υιοθετήσει το καλλιτεχνικό ψευδώνυμο Freddie Mercury.",
        [
            "Επέλεξε το επώνυμο Mercury εμπνευσμένος από έναν στίχο του τραγουδιού 'My Fairy King' ('Mother Mercury, look what they've done to me').",
            "Η οικογένειά του ανήκε στη θρησκευτική κοινότητα των Πάρσι (Ζωροάστρες)."
        ],
        "https://en.wikipedia.org/wiki/Freddie_Mercury",
        ["freddie_mercury", "queen", "rock_music", "celebrities"]
    ),
    # 264
    make_q(
        "pop_culture_med_264",
        "Ποιες δύο ποπ σταρ αντάλλαξαν ένα πολυσυζητημένο φιλί στο στόμα με τη Madonna στα MTV Video Music Awards του 2003;",
        "Britney Spears και Christina Aguilera",
        ["Beyoncé και Rihanna", "Katy Perry και Lady Gaga", "P!nk και Shakira"],
        "Η εμφάνιση ξεκίνησε με τις Britney Spears και Christina Aguilera ντυμένες νύφες να τραγουδούν το 'Like a Virgin' πριν η Madonna τις φιλήσει διαδοχικά.",
        [
            "Η αντίδραση του πρώην συντρόφου της Britney, Justin Timberlake, στο κοινό καταγράφηκε σε ζωντανή μετάδοση και έγινε viral.",
            "Η σκηνή θεωρείται μία από τις πιο πολυσυζητημένες στιγμές στην ιστορία της τηλεοπτικής ποπ κουλτούρας."
        ],
        "https://en.wikipedia.org/wiki/2003_MTV_Video_Music_Awards",
        ["madonna", "britney_spears", "christina_aguilera", "mtv_vma"]
    ),
    # 265
    make_q(
        "pop_culture_med_265",
        "Ποιο διάσημο ζευγάρι διασημοτήτων των αρχών των 2000s επινόησε για πρώτη φορά τα συνδυαστικά παρατσούκλια των media όπως 'Bennifer';",
        "Ben Affleck και Jennifer Lopez",
        ["Brad Pitt και Jennifer Aniston", "Tom Cruise και Katie Holmes", "David και Victoria Beckham"],
        "Το όνομα 'Bennifer' καθιέρωσε τη μόδα των μέσων ενημέρωσης να ενώνουν τα μικρά ονόματα διάσημων ζευγαριών (όπως αργότερα 'Brangelina').",
        [
            "Γνωρίστηκαν στα γυρίσματα της ταινίας 'Gigli' το 2002 και ο Affleck πρωταγωνίστησε στο βίντεο κλιπ 'Jenny from the Block'.",
            "Αφού χώρισαν το 2004, επανασυνδέθηκαν σχεδόν δύο δεκαετίες αργότερα και παντρεύτηκαν το 2022."
        ],
        "https://en.wikipedia.org/wiki/Bennifer",
        ["bennifer", "ben_affleck", "jennifer_lopez", "celebrities"]
    ),
    # 266
    make_q(
        "pop_culture_med_266",
        "Ποιος σκηνοθέτης του Χόλιγουντ ανέλαβε τη σκηνοθεσία του ιστορικού 14λεπτου μουσικού βίντεο 'Thriller' του Michael Jackson το 1983;",
        "John Landis",
        ["Martin Scorsese", "Steven Spielberg", "David Fincher"],
        "Ο Michael Jackson επέλεξε τον John Landis αφού εντυπωσιάστηκε από την ταινία τρόμου του 'An American Werewolf in London' (1981).",
        [
            "Το 'Thriller' ήταν το πρώτο μουσικό βίντεο που εντάχθηκε στο National Film Registry της Βιβλιοθήκης του Κογκρέσου των ΗΠΑ.",
            "Η κόκκινη δερμάτινη ζακέτα που φορούσε ο Jackson στο βίντεο πουλήθηκε σε δημοπρασία το 2011 για 1,8 εκατομμύρια δολάρια."
        ],
        "https://en.wikipedia.org/wiki/Michael_Jackson%27s_Thriller_(music_video)",
        ["thriller", "michael_jackson", "john_landis", "music_video"]
    ),
    # 267
    make_q(
        "pop_culture_med_267",
        "Ποια δημιουργική διευθύντρια του οίκου Alexander McQueen σχεδίασε το ιστορικό νυφικό φόρεμα της Kate Middleton το 2011;",
        "Sarah Burton",
        ["Stella McCartney", "Phoebe Philo", "Clare Waight Keller"],
        "Η Sarah Burton δημιούργησε ένα νυφικό από δαντέλα και σατέν εμπνευσμένο από τη βικτωριανή παράδοση, το οποίο αντιγράφηκε από σχεδιαστές σε όλο τον κόσμο.",
        [
            "Η δαντέλα του νυφικού κατασκευάστηκε στο χέρι από τη Βασιλική Σχολή Κεντήματος (Royal School of Needlework).",
            "Η Burton ανέλαβε τη δημιουργική διεύθυνση του οίκου μετά τον θάνατο του ίδιου του Alexander McQueen το 2010."
        ],
        "https://en.wikipedia.org/wiki/Wedding_dress_of_Kate_Middleton",
        ["kate_middleton", "sarah_burton", "alexander_mcqueen", "fashion"]
    ),
    # 268
    make_q(
        "pop_culture_med_268",
        "Ποιος θρυλικός κιθαρίστας ισοφάρισε το ρεκόρ του Michael Jackson κερδίζοντας 8 βραβεία Grammy σε μία μόνο βραδιά το 2000 με το άλμπουμ 'Supernatural';",
        "Carlos Santana",
        ["Eric Clapton", "Stevie Ray Vaughan", "B.B. King"],
        "Ο Carlos Santana κυριάρχησε στα βραβεία Grammy του 2000 χάρη σε παγκόσμιες επιτυχίες όπως το 'Smooth' (με τον Rob Thomas) και το 'Maria Maria'.",
        [
            "Το 'Supernatural' σηματοδότησε μια από τις πιο θεαματικές επιστροφές στην ιστορία της ροκ, πουλώντας πάνω από 30 εκατομμύρια αντίτυπα.",
            "Το τραγούδι 'Smooth' παρέμεινε 12 εβδομάδες στο νούμερο 1 του Billboard Hot 100."
        ],
        "https://en.wikipedia.org/wiki/Supernatural_(Santana_album)",
        ["carlos_santana", "supernatural", "grammys", "rock_music"]
    ),
    # 269
    make_q(
        "pop_culture_med_269",
        "Ποια τραγουδίστρια έγινε η πρώτη γυναίκα που κέρδισε το κορυφαίο βραβείο Grammy για το Άλμπουμ της Χρονιάς τρεις φορές (με τα Fearless, 1989 και Folklore);",
        "Taylor Swift",
        ["Adele", "Beyoncé", "Barbra Streisand"],
        "Η Taylor Swift πέτυχε αυτό το ιστορικό ορόσημο το 2021 και αργότερα το 2024 έγινε η μοναδική καλλιτέχνιδα στην ιστορία με τέσσερις νίκες στη συγκεκριμένη κατηγορία (με το Midnights).",
        [
            "Πριν από αυτήν, μόνο οι Frank Sinatra, Stevie Wonder και Paul Simon είχαν κερδίσει τρεις φορές το Άλμπουμ της Χρονιάς.",
            "Κέρδισε για πρώτη φορά το βραβείο σε ηλικία μόλις 20 ετών με το άλμπουμ 'Fearless'."
        ],
        "https://en.wikipedia.org/wiki/Taylor_Swift",
        ["taylor_swift", "grammys", "album_of_the_year", "pop_music"]
    ),
    # 270
    make_q(
        "pop_culture_med_270",
        "Ποιο Βρετανικό supermodel ανακαλύφθηκε στο αεροδρόμιο JFK στα 14 της και καθιέρωσε το στυλ 'heroin chic' τη δεκαετία του 1990;",
        "Kate Moss",
        ["Naomi Campbell", "Linda Evangelista", "Cindy Crawford"],
        "Η Kate Moss αποτέλεσε το αντίπαλο δέος των αθλητικών και λαμπερών supermodels των late 80s με την εύθραυστη και φυσική της εμφάνιση.",
        [
            "Οι διαφημιστικές της καμπάνιες για το άρωμα 'Obsession' του Calvin Klein το 1993 έγραψαν ιστορία.",
            "Έχει εμφανιστεί στο εξώφυλλο της βρετανικής Vogue περισσότερες από 40 φορές."
        ],
        "https://en.wikipedia.org/wiki/Kate_Moss",
        ["kate_moss", "supermodels", "calvin_klein", "fashion", "90s"]
    ),
    # 271
    make_q(
        "pop_culture_med_271",
        "Πώς ονομάζεται το αρχαίο σπαθί του Elendil που ξανασφυρηλατήθηκε από τα κομμάτια του για τον Aragorn στον 'Άρχοντα των Δαχτυλιδιών';",
        "Andúril (Η Φλόγα της Δύσης)",
        ["Narsil", "Glamdring", "Sting"],
        "Το Narsil ήταν το σπαθί που έκοψε το Δαχτυλίδι από το χέρι του Sauron πριν σπάσει, και ξανασφυρηλατήθηκε στο Rivendell ως Andúril.",
        [
            "Στα ξωτικά (Sindarin), το όνομα Andúril σημαίνει 'Φλόγα της Δύσης'.",
            "Η λεπίδα του σπαθιού φέρει μαγικές επιγραφές που λάμπουν στο σκοτάδι όταν πλησιάζουν εχθροί."
        ],
        "https://en.wikipedia.org/wiki/Narsil",
        ["lord_of_the_rings", "anduril", "aragorn", "tolkien"]
    ),
    # 272
    make_q(
        "pop_culture_med_272",
        "Ποιο είναι το επίσημο όνομα του είδους στο οποίο ανήκει ο Master Yoda στο σύμπαν του Star Wars;",
        "Παραμένει άγνωστο (Unknown species)",
        ["Whill", "Lannik", "Trandoshan"],
        "Ο George Lucas αποφάσισε σκόπιμα να μην αποκαλύψει ποτέ το όνομα του είδους ή τον γενέθλιο πλανήτη του Yoda για να διατηρήσει το μυστήριο.",
        [
            "Ο χαρακτήρας του Grogu ('Baby Yoda') στη σειρά 'The Mandalorian' ανήκει στο ίδιο σπάνιο είδος με μακρά διάρκεια ζωής.",
            "Το μόνο άλλο μέλος του είδους που έχει εμφανιστεί στις ταινίες είναι η θηλυκή Yaddle στο 'The Phantom Menace'."
        ],
        "https://en.wikipedia.org/wiki/Yoda",
        ["star_wars", "yoda", "grogu", "sci_fi"]
    ),
    # 273
    make_q(
        "pop_culture_med_273",
        "Από ποιο μαγικό πλάσμα προέρχονται τα δύο δίδυμα φτερά που αποτελούν τους πυρήνες των ραβδιών του Harry Potter και του Lord Voldemort;",
        "Από τον φοίνικα Fawkes",
        ["Από έναν ιππόγρυπα", "Από έναν ουγγρικό κερκόκερο", "Από ένα θεστράλ"],
        "Ο κατασκευαστής ραβδιών Ollivander αποκαλύπτει ότι ο φοίνικας του Dumbledore, Fawkes, έδωσε μόνο δύο φτερά στην ιστορία, συνδέοντας άρρηκτα τα δύο ραβδιά.",
        [
            "Αυτή η σύνδεση προκαλεί το φαινόμενο 'Priori Incantatem' όταν τα δύο ραβδιά συγκρούονται απευθείας στο τέλος του 'Κυπέλλου της Φωτιάς'.",
            "Το ξύλο του ραβδιού του Harry είναι από πουρνάρι (holly), ενώ του Voldemort από ίταμο (yew)."
        ],
        "https://en.wikipedia.org/wiki/Magic_in_Harry_Potter#Wands",
        ["harry_potter", "wands", "fawkes", "voldemort"]
    ),
    # 274
    make_q(
        "pop_culture_med_274",
        "Ποιο ήταν το πατρογονικό δίκοπο σπαθί από βαλυριανό ατσάλι του Οίκου Stark που κρατούσε ο Ned Stark στην αρχή του 'Game of Thrones';",
        "Ice (Πάγος)",
        ["Longclaw", "Widow's Wail", "Oathkeeper"],
        "Το Ice ήταν ένα τεράστιο προγονικό σπαθί δύο χεριών που χρησιμοποιούνταν για εκτελέσεις και επίσημες τελετές στο Winterfell.",
        [
            "Μετά την εκτέλεση του Ned Stark, ο Tywin Lannister έλιωσε το σπαθί για να φτιάξει δύο νέα: το Oathkeeper και το Widow's Wail.",
            "Το Oathkeeper δόθηκε τελικά από τον Jaime Lannister στην Brienne του Tarth."
        ],
        "https://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_weapons#Ice",
        ["game_of_thrones", "ice", "house_stark", "valyrian_steel"]
    ),
    # 275
    make_q(
        "pop_culture_med_275",
        "Στην ταινία 'The Matrix' (1999), ποιο χρώμα χαπιού επιλέγει ο Neo από τον Morpheus για να μάθει τη σκληρή αλήθεια της πραγματικότητας;",
        "Κόκκινο",
        ["Μπλε", "Πράσινο", "Κίτρινο"],
        "Ο Morpheus εξηγεί: 'Παίρνεις το μπλε χάπι, η ιστορία τελειώνει. Παίρνεις το κόκκινο χάπι, μένεις στη Χώρα των Θαυμάτων και σου δείχνω πόσο βαθιά πάει η λαγουδότρυπα'.",
        [
            "Ο όρος 'red pill' εισήλθε έκτοτε στην παγκόσμια ποπ κουλτούρα και την πολιτική φιλοσοφία ως έννοια αφύπνισης στην πραγματικότητα.",
            "Οι σκηνοθέτιδες αδελφές Wachowski έχουν επιβεβαιώσει ότι το Matrix λειτουργεί και ως βαθιά αλληγορία για τη διεμφυλική μετάβαση."
        ],
        "https://en.wikipedia.org/wiki/Red_pill_and_blue_pill",
        ["the_matrix", "red_pill", "morpheus", "cinema"]
    ),
    # 276
    make_q(
        "pop_culture_med_276",
        "Ποιο είναι το παρατσούκλι του Geralt of Rivia που συνδέεται με τη σχολή μαγείας των Witcher στο Kaer Morhen και τα λευκά του μαλλιά;",
        "White Wolf (Λευκός Λύκος / Gwynbleidd)",
        ["Black Dog", "Iron Bull", "Grey Ghost"],
        "Ο Geralt ανήκει στη Σχολή του Λύκου (School of the Wolf) και τα μαλλιά του έχασαν όλη τη χρωστική τους ουσία κατά τη διάρκεια των σκληρών μεταλλάξεων.",
        [
            "Στη γλώσσα των Ξωτικών (Elder Speech), ονομάζεται 'Gwynbleidd'.",
            "Φέρει επίσης το τρομακτικό παρατσούκλι 'Ο Χασάπης του Blaviken' μετά από ένα αιματηρό περιστατικό στην ομώνυμη πόλη."
        ],
        "https://en.wikipedia.org/wiki/Geralt_of_Rivia",
        ["the_witcher", "geralt", "white_wolf", "fantasy"]
    ),
    # 277
    make_q(
        "pop_culture_med_277",
        "Ποια επιτυχημένη μίνι σειρά του Netflix με την Anya Taylor-Joy ως Beth Harmon εκτόξευσε τις παγκόσμιες πωλήσεις σκακιέρας το 2020;",
        "The Queen's Gambit (Το Γκαμπί της Βασίλισσας)",
        ["The Crown", "Unorthodox", "Maid"],
        "Η σειρά βασίστηκε στο ομώνυμο μυθιστόρημα του Walter Tevis από το 1983 και παρακολουθεί την άνοδο ενός ορφανού κοριτσιού-θαύματος στην κορυφή του παγκόσμιου σκακιού.",
        [
            "Ο θρυλικός παγκόσμιος πρωταθλητής Garry Kasparov υπήρξε ειδικός σύμβουλος για την απόλυτη πιστότητα των σκακιστικών παρτίδων στη σειρά.",
            "Τις πρώτες εβδομάδες προβολής, οι εγγραφές στο Chess.com και οι πωλήσεις σκακιστικών σετ αυξήθηκαν κατά εκατοντάδες τοις εκατό παγκοσμίως."
        ],
        "https://en.wikipedia.org/wiki/The_Queen%27s_Gambit_(miniseries)",
        ["the_queens_gambit", "chess", "netflix", "anya_taylor_joy"]
    ),
    # 278
    make_q(
        "pop_culture_med_278",
        "Ποιο είναι το πραγματικό όνομα γέννησης της Eleven στη σειρά 'Stranger Things' πριν καταλήξει στο εργαστήριο του Hawkins;",
        "Jane Ives",
        ["Sara Hopper", "Maxine Mayfield", "Nancy Wheeler"],
        "Η μητέρα της, Terry Ives, συμμετείχε στο κυβερνητικό πρόγραμμα MKUltra κατά τη διάρκεια της εγκυμοσύνης της και της έδωσε το όνομα Jane πριν της την αρπάξουν.",
        [
            "Αργότερα, ο σερίφης Jim Hopper την υιοθετεί νόμιμα με το όνομα Jane Hopper.",
            "Τον ρόλο της Eleven ενσάρκωσε η Millie Bobby Brown, εκτοξεύοντας την καριέρα της σε παγκόσμιο επίπεδο σε ηλικία μόλις 12 ετών."
        ],
        "https://en.wikipedia.org/wiki/Eleven_(Stranger_Things)",
        ["stranger_things", "eleven", "jane_ives", "netflix"]
    ),
    # 279
    make_q(
        "pop_culture_med_279",
        "Ποιος διάσημος ηθοποιός ενσάρκωσε τον μεγαλοφυή χημικό Walter White που μετατρέπεται στον αδίστακτο Heisenberg στο 'Breaking Bad';",
        "Bryan Cranston",
        ["Aaron Paul", "Bob Odenkirk", "Giancarlo Esposito"],
        "Ο Bryan Cranston κέρδισε τέσσερα βραβεία Emmy Α' Ανδρικού Ρόλου για την ασύλληπτη μεταμόρφωση ενός φιλήσυχου καθηγητή σε βαρόνο ναρκωτικών.",
        [
            "Πριν το Breaking Bad, ο Cranston ήταν κυρίως γνωστός για τον κωμικό ρόλο του παιδιάστικου πατέρα Hal στη σειρά 'Malcolm in the Middle'.",
            "Ο δημιουργός Vince Gilligan περιέγραψε τη σειρά ως τη διαδικασία μετατροπής του 'Mr. Chips σε Scarface'."
        ],
        "https://en.wikipedia.org/wiki/Walter_White_(Breaking_Bad)",
        ["breaking_bad", "bryan_cranston", "heisenberg", "tv_series"]
    ),
    # 280
    make_q(
        "pop_culture_med_280",
        "Ποιο χαρακτηριστικό μπλε παρατσούκλι είχε η σχεδόν χημικά τέλεια μεθαμφεταμίνη (99,1% καθαρότητας) που παρασκεύαζε ο Heisenberg στο 'Breaking Bad';",
        "Blue Sky",
        ["Crystal Magic", "Blue Diamond", "Azure Pure"],
        "Η χαρακτηριστική μπλε απόχρωση της 'Blue Sky' προέκυπτε από τη χρήση μεθυλαμίνης στη συνταγή P2P, γινόμενη το εμπορικό σήμα υπεροχής του Heisenberg στην αγορά.",
        [
            "Στην πραγματικότητα, η καθαρή μεθαμφεταμίνη είναι εντελώς διάφανη ή λευκή, και η παραγωγή χρησιμοποίησε μπλε καραμέλα (rock candy) στα γυρίσματα.",
            "Πραγματικοί έμποροι ναρκωτικών άρχισαν να προσθέτουν μπλε χρωστικές στις ουσίες τους για να μιμηθούν τη δημοφιλία της σειράς."
        ],
        "https://en.wikipedia.org/wiki/Breaking_Bad",
        ["breaking_bad", "blue_sky", "heisenberg"]
    ),
    # 281
    make_q(
        "pop_culture_med_281",
        "Ποιο από τα τέσσερα ρωμαϊκά στρατόπεδα που περικυκλώνουν το γαλατικό χωριό του Αστερίξ έχει το όνομα ενός γαλλικού γλυκού με ρούμι;",
        "Μπαμπαόρουμ (Babaorum)",
        ["Πετιμπονούμ", "Λαουντανούμ", "Ακουάριουμ"],
        "Τα τέσσερα ρωμαϊκά οχυρά γύρω από το χωριό είναι: Petibonum, Aquarium, Laudanum και Babaorum (από το γλυκό baba au rhum).",
        [
            "Οι Ρωμαίοι λεγεωνάριοι που υπηρετούν σε αυτά τα στρατόπεδα τρέμουν τις εξόδους στο δάσος μήπως πέσουν πάνω στον Αστερίξ και τον Οβελίξ.",
            "Τα ονόματα σχεδόν όλων των Ρωμαίων στα κόμικς τελειώνουν σε '-us' και αποτελούν έξυπνα γαλλικά λογοπαίγνια (π.χ. Caius Bonus)."
        ],
        "https://en.wikipedia.org/wiki/Asterix",
        ["asterix", "babaorum", "comics", "goscinny"]
    ),
    # 282
    make_q(
        "pop_culture_med_282",
        "Ποια ιστορική τηλεγραφική εταιρεία προστατεύει ο Λούκυ Λουκ στο ομώνυμο άλμπουμ καθώς ενώνει την ανατολική με τη δυτική ακτή των ΗΠΑ;",
        "Western Union",
        ["Pony Express", "Wells Fargo", "Union Pacific"],
        "Στο άλμπουμ 'Το Σύρμα που Τραγουδάει' (Le Fil qui chante, 1977), ο Λούκυ Λουκ συνοδεύει τους εργάτες της Western Union στην τοποθέτηση του διηπειρωτικού τηλεγράφου.",
        [
            "Το 'σύρμα που τραγουδάει' ήταν το όνομα που έδιναν οι αυτόχθονες Αμερικανοί στα τηλεγραφικά καλώδια λόγω του ήχου του ανέμου ανάμεσά τους.",
            "Η ολοκλήρωση του τηλεγράφου το 1861 σήμανε το τέλος της σύντομης εποχής του Pony Express."
        ],
        "https://en.wikipedia.org/wiki/Le_Fil_qui_chante",
        ["lucky_luke", "western_union", "telegraph", "comics"]
    ),
    # 283
    make_q(
        "pop_culture_med_283",
        "Ποιο θρυλικό γαλλοβελγικό περιοδικό κόμικς κυκλοφόρησε για πρώτη φορά το 1946 με σλόγκαν 'Η εφημερίδα για νέους από 7 έως 77 ετών';",
        "Le Journal de Tintin",
        ["Spirou", "Pilote", "A Suivre"],
        "Το περιοδικό Tintin ιδρύθηκε από τον εκδότη Raymond Leblanc και τον Hergé και φιλοξένησε σειρές όπως Blake and Mortimer, Alix και Michel Vaillant.",
        [
            "Η περίφημη φράση 'από 7 έως 77 ετών' καθιέρωσε την ιδέα ότι τα κόμικς απευθύνονται εξίσου σε ενήλικες και παιδιά.",
            "Υπήρξε ο μεγάλος ιστορικός αντίπαλος του περιοδικού 'Spirou' στον ανταγωνισμό της γαλλοβελγικής σχολής."
        ],
        "https://en.wikipedia.org/wiki/Tintin_(magazine)",
        ["tintin", "comics", "belgium", "herge"]
    ),
    # 284
    make_q(
        "pop_culture_med_284",
        "Ποια Ελληνίδα πολεμίστρια νίντζα και δολοφόνος είναι ο μεγάλος έρωτας και συχνή αντίπαλος του Daredevil στα κόμικς της Marvel;",
        "Elektra Natchios",
        ["Echo", "Karen Page", "Lady Bullseye"],
        "Η Elektra Natchios, κόρη Έλληνα πρέσβη, εκπαιδεύτηκε στις πολεμικές τέχνες από την οργάνωση The Hand και χειρίζεται δίδυμα μαχαίρια sai.",
        [
            "Δημιουργήθηκε από τον Frank Miller στο Daredevil #168 το 1981, εμπνευσμένος από την αρχαία ελληνική τραγωδία της Ηλέκτρας.",
            "Η ιστορική σκηνή του θανάτου της από τον Bullseye με τα δικά της sai παραμένει ένα από τα πιο αναγνωρίσιμα καρέ στην ιστορία της Marvel."
        ],
        "https://en.wikipedia.org/wiki/Elektra_(character)",
        ["elektra", "daredevil", "marvel", "frank_miller"]
    ),
    # 285
    make_q(
        "pop_culture_med_285",
        "Ποιο είναι το πραγματικό κρυπτονιανό όνομα της Supergirl, ξαδέλφης του Superman από την Argo City;",
        "Kara Zor-El",
        ["Lara Lor-Van", "Faora Hu-Ul", "Alura In-Ze"],
        "Η Kara Zor-El στάλθηκε στη Γη για να προστατεύσει το μωρό ξάδελφό της Kal-El, αλλά το σκάφος της εκτράπηκε και έφτασε αφού εκείνος είχε ήδη μεγαλώσει.",
        [
            "Πρωτοεμφανίστηκε στο Action Comics #252 το 1959, δημιουργημένη από τον Otto Binder και τον Al Plastino.",
            "Στη Γη χρησιμοποιεί τη μυστική ταυτότητα Linda Lee Danvers."
        ],
        "https://en.wikipedia.org/wiki/Supergirl_(Kara_Zor-El)",
        ["supergirl", "kara_zor_el", "superman", "dc_comics"]
    ),
    # 286
    make_q(
        "pop_culture_med_286",
        "Ποιος νεαρός έφηβος μεταμορφώνεται στον υπερήρωα Shazam κάθε φορά που φωνάζει το όνομα του αρχαίου μάγου;",
        "Billy Batson",
        ["Freddy Freeman", "Eugene Choi", "Pedro Peña"],
        "Ο ορφανός Billy Batson επιλέχθηκε από τον μάγο Shazam ως πρωταθλητής της ανθρωπότητας λόγω της αγνής του καρδιάς.",
        [
            "Το ακρωνύμιο S.H.A.Z.A.M. αντιστοιχεί στις δυνάμεις των: Σολομώντα, Ηρακλή, Άτλαντα, Δία (Zeus), Αχιλλέα και Ερμή (Mercury).",
            "Αρχικά ο χαρακτήρας ονομαζόταν 'Captain Marvel' όταν εκδιδόταν από τη Fawcett Comics τη δεκαετία του 1940."
        ],
        "https://en.wikipedia.org/wiki/Captain_Marvel_(DC_Comics)",
        ["shazam", "billy_batson", "dc_comics", "superheroes"]
    ),
    # 287
    make_q(
        "pop_culture_med_287",
        "Ποιο σύστημα τεχνητής νοημοσύνης δημιούργησε ο Tony Stark για να διαχειρίζεται τις στολές του πριν αυτό ενσωματωθεί στο σώμα του Vision;",
        "J.A.R.V.I.S.",
        ["F.R.I.D.A.Y.", "E.D.I.T.H.", "K.A.R.E.N."],
        "Το J.A.R.V.I.S. (Just A Rather Very Intelligent System) πήρε το όνομά του ως φόρος τιμής στον παλιό μπάτλερ του πατέρα του, Edwin Jarvis.",
        [
            "Τη φωνή του J.A.R.V.I.S. χάρισε ο Βρετανός ηθοποιός Paul Bettany, ο οποίος στη συνέχεια υποδύθηκε σωματικά τον Vision.",
            "Μετά την απώλεια του Jarvis, ο Stark υιοθέτησε τη γυναικεία φωνή τεχνητής νοημοσύνης F.R.I.D.A.Y."
        ],
        "https://en.wikipedia.org/wiki/J.A.R.V.I.S.",
        ["iron_man", "jarvis", "marvel", "mcu"]
    ),
    # 288
    make_q(
        "pop_culture_med_288",
        "Ποια μοχθηρή οργάνωση της Marvel έχει ως σύνθημα 'Κόψε ένα κεφάλι, δύο άλλα θα πάρουν τη θέση του' και έμβλημα ένα χταπόδι-κρανίο;",
        "HYDRA",
        ["A.I.M.", "The Hand", "Leviathan"],
        "Η HYDRA είναι μια αρχαία συνωμοτική οργάνωση που κατά τον Β' Παγκόσμιο Πόλεμο ηγήθηκε από τον Red Skull και διείσδυσε κρυφά στη S.H.I.E.L.D.",
        [
            "Η αποκάλυψη ότι η HYDRA λειτουργούσε κρυφά μέσα στη S.H.I.E.L.D. αποτέλεσε την κεντρική ανατροπή στην ταινία 'Captain America: The Winter Soldier' (2014).",
            "Στα κόμικς του 2017 ('Secret Empire'), ο Captain America προκάλεσε σοκ στους αναγνώστες λέγοντας τη φράση 'Hail Hydra'."
        ],
        "https://en.wikipedia.org/wiki/Hydra_(comics)",
        ["hydra", "marvel", "captain_america", "supervillains"]
    ),
    # 289
    make_q(
        "pop_culture_med_289",
        "Ποια είναι η ιδιοφυής νεαρή πριγκίπισσα της Wakanda που σχεδιάζει τις στολές και την τεχνολογία του Black Panther;",
        "Shuri",
        ["Nakia", "Okoye", "Ramonda"],
        "Η Shuri είναι η μικρότερη αδελφή του βασιλιά T'Challa, επικεφαλής του Ομίλου Επιστημών της Wakanda και εφευρέτρια των γαντιών δόνησης.",
        [
            "Στο MCU τη χαρακτήρα ενσαρκώνει η Letitia Wright.",
            "Στην ταινία 'Black Panther: Wakanda Forever' (2022), η Shuri αναλαμβάνει η ίδια τον μανδύα του Black Panther μετά τον θάνατο του αδελφού της."
        ],
        "https://en.wikipedia.org/wiki/Shuri_(character)",
        ["shuri", "black_panther", "wakanda", "marvel"]
    ),
    # 290
    make_q(
        "pop_culture_med_290",
        "Ποιο μυθικό βασίλειο των νεκρών κυβερνά η θεά του θανάτου Hela στη μυθολογία και τα κόμικς του Thor;",
        "Hel (Χελ)",
        ["Muspelheim", "Alfheim", "Vanaheim"],
        "Το Hel είναι ο παγωμένος υπόκοσμος της σκανδιναβικής μυθολογίας όπου καταλήγουν όσοι δεν πεθαίνουν ένδοξα στη μάχη.",
        [
            "Στην ταινία 'Thor: Ragnarok' (2017), την Hela υποδύθηκε η βραβευμένη με Όσκαρ Cate Blanchett ως πρωτότοκη κόρη του Odin.",
            "Η Hela αντλεί τη δύναμή της απευθείας από το Asgard, γινόμενη ισχυρότερη όσο παραμένει εκεί."
        ],
        "https://en.wikipedia.org/wiki/Hela_(character)",
        ["hela", "thor", "asgard", "marvel"]
    ),
    # 291
    make_q(
        "pop_culture_med_291",
        "Ποιο νορβηγικό κωμικό ντουέτο κυκλοφόρησε το viral τραγούδι 'The Fox (What Does the Fox Say?)' το 2013;",
        "Ylvis",
        ["Kol collective", "Madcon", "Datarock"],
        "Τα αδέλφια Bård και Vegard Ylvisåker δημιούργησαν το τραγούδι ως παρωδία για την τηλεοπτική τους εκπομπή, αλλά έγινε παγκόσμιο mega-hit.",
        [
            "Το βίντεο ξεπέρασε το 1 δισεκατομμύριο προβολές στο YouTube και έφτασε στο top 10 του Billboard Hot 100.",
            "Οι παράξενοι ήχοι της αλεπούς στο ρεφρέν, όπως 'Ring-ding-ding-ding-dingeringeding!', επαναλαμβάνονταν σε όλο τον κόσμο."
        ],
        "https://en.wikipedia.org/wiki/The_Fox_(What_Does_the_Fox_Say%3F)",
        ["ylvis", "the_fox", "viral", "youtube"]
    ),
    # 292
    make_q(
        "pop_culture_med_292",
        "Ποιο μπαχαρικό προσπαθούσαν να καταπιούν σε κουταλιά χωρίς νερό οι χρήστες στο επικίνδυνο viral challenge των αρχών των 2010s;",
        "Κανέλα (Cinnamon Challenge)",
        ["Μοσχοκάρυδο", "Πιπέρι καγιέν", "Κουρκουμά"],
        "Το Cinnamon Challenge έγινε viral στο YouTube με ανθρώπους να βήχουν σύννεφα σκόνης, προκαλώντας προειδοποιήσεις από γιατρούς για κίνδυνο πνευμονικής βλάβης.",
        [
            "Η κανέλα περιέχει κυτταρίνη που δεν διαλύεται εύκολα, καλύπτοντας τον λαιμό και προκαλώντας έντονο πνιγμό και σπασμούς.",
            "Διασημότητες και αθλητές δοκίμασαν το challenge σε εκπομπές πριν οι πλατφόρμες αρχίσουν να κατεβάζουν τέτοια βίντεο."
        ],
        "https://en.wikipedia.org/wiki/Cinnamon_challenge",
        ["cinnamon_challenge", "viral", "youtube", "challenges"]
    ),
    # 293
    make_q(
        "pop_culture_med_293",
        "Ποιο οικιακό προϊόν καθαρισμού έγινε αντικείμενο ενός παράλογου και επικίνδυνου viral trend το 2018 προκαλώντας ιατρικές απαγορεύσεις;",
        "Κάψουλες πλυντηρίου Tide Pods",
        ["Χλωρίνη", "Ταμπλέτες πλυντηρίου πιάτων", "Μαλακτικό ρούχων"],
        "Το 'Tide Pod Challenge' ξεκίνησε από διαδικτυακά αστεία για την ομοιότητα των καψουλών με καραμέλες πριν εξελιχθεί σε επικίνδυνο trend κατάποσης από εφήβους.",
        [
            "Η κατασκευάστρια εταιρεία Procter & Gamble άλλαξε τη συσκευασία κάνοντάς την αδιαφανή και επιστράτευσε αθλητές για καμπάνιες αποτροπής.",
            "Οι πλατφόρμες κοινωνικής δικτύωσης απέσυραν μαζικά όλα τα σχετικά βίντεο για λόγους δημόσιας υγείας."
        ],
        "https://en.wikipedia.org/wiki/Consumption_of_Tide_Pods",
        ["tide_pod_challenge", "viral", "internet_memes"]
    ),
    # 294
    make_q(
        "pop_culture_med_294",
        "Ποιος γορίλας του ζωολογικού κήπου του Σινσινάτι πυροβολήθηκε θανάσιμα το 2016 μετά την πτώση ενός παιδιού στο κλουβί του, γινόμενος παγκόσμιο meme;",
        "Harambe",
        ["Bokito", "Koko", "Jambo"],
        "Ο θάνατος του 17χρονου γορίλα Harambe προκάλεσε παγκόσμια κατακραυγή και μετατράπηκε σε ένα από τα πιο διαδεδομένα και σουρεαλιστικά memes της χρονιάς.",
        [
            "Το όνομα Harambe αναφερόταν διαρκώς σε αθλητικές εκδηλώσεις, διαδικτυακές ψηφοφορίες και τραγούδια rap.",
            "Ο ζωολογικός κήπος του Σινσινάτι αναγκάστηκε να κλείσει προσωρινά τους λογαριασμούς του στα social media λόγω του καταιγισμού μηνυμάτων."
        ],
        "https://en.wikipedia.org/wiki/Killing_of_Harambe",
        ["harambe", "memes", "viral", "internet_history"]
    ),
    # 295
    make_q(
        "pop_culture_med_295",
        "Ποια viral καμπάνια-ντοκιμαντέρ του 2012 από την Invisible Children συγκέντρωσε πάνω από 100 εκατομμύρια προβολές σε 6 ημέρες στοχεύοντας έναν πολέμαρχο της Ουγκάντα;",
        "Kony 2012",
        ["Free Tibet", "Blood Diamond", "Save Darfur"],
        "Το βίντεο του Jason Russell στόχευε να κάνει διάσημο τον Joseph Kony, αρχηγό του Lord's Resistance Army, ώστε να συλληφθεί μέχρι το τέλος του 2012.",
        [
            "Έγινε το ταχύτερα αναπτυσσόμενο viral βίντεο στην ιστορία του YouTube έως τότε.",
            "Παρά τη μαζική απήχηση, δέχθηκε έντονη κριτική για απλοποίηση της γεωπολιτικής κατάστασης και κακή διαχείριση των κονδυλίων."
        ],
        "https://en.wikipedia.org/wiki/Kony_2012",
        ["kony_2012", "viral", "youtube", "documentary"]
    ),
    # 296
    make_q(
        "pop_culture_med_296",
        "Ποιο μουσικό και χορευτικό είδος της Νότιας Αφρικής έγινε παγκόσμιο viral trend στο TikTok με χαρακτηριστικές χορογραφίες;",
        "Amapiano",
        ["Afrobeats", "Kwaito", "Highlife"],
        "Το Amapiano γεννήθηκε στα μέσα της δεκαετίας του 2010 στη Νότια Αφρική συνδυάζοντας deep house, jazz και πιανιστικές μελωδίες.",
        [
            "Χορευτικές κινήσεις όπως το 'Bacardi dance' και το shuffling σε κομμάτια amapiano κατέκλυσαν το TikTok.",
            "Η λέξη 'amapiano' είναι στη γλώσσα Ζουλού και σημαίνει κυριολεκτικά 'τα πιάνα'."
        ],
        "https://en.wikipedia.org/wiki/Amapiano",
        ["amapiano", "dance", "tiktok", "south_africa", "music"]
    ),
    # 297
    make_q(
        "pop_culture_med_297",
        "Ποιος Γάλλος σχεδιαστής αναδιαμόρφωσε ριζικά την ανδρική μόδα τη δεκαετία του 2000 στο Dior Homme εισάγοντας τις εξαιρετικά στενές γραμμές (skinny silhouette);",
        "Hedi Slimane",
        ["Raf Simons", "Kim Jones", "Kris Van Assche"],
        "Ο Hedi Slimane εισήγαγε στενά σακάκια, χαμηλοκάβαλα στενά τζιν και ροκ αισθητική, επηρεάζοντας τόσο πολύ τη μόδα που ακόμα και ο Karl Lagerfeld έχασε 40 κιλά για να χωρέσει στα ρούχα του.",
        [
            "Αργότερα ανέλαβε τον οίκο Saint Laurent αφαιρώντας το 'Yves' από το όνομα του ready-to-wear brand.",
            "Το 2018 ανέλαβε την καλλιτεχνική διεύθυνση του γαλλικού οίκου Celine."
        ],
        "https://en.wikipedia.org/wiki/Hedi_Slimane",
        ["hedi_slimane", "dior_homme", "celine", "fashion"]
    ),
    # 298
    make_q(
        "pop_culture_med_298",
        "Σε ποια χώρα ιδρύθηκε ο ιστορικός οίκος μόδας Balenciaga το 1919 από τον Cristóbal Balenciaga πριν μεταφερθεί στο Παρίσι;",
        "Ισπανία",
        ["Ιταλία", "Γαλλία", "Πορτογαλία"],
        "Ο Cristóbal Balenciaga άνοιξε την πρώτη του μπουτίκ στο Σαν Σεμπαστιάν της Ισπανίας πριν μετακομίσει στο Παρίσι λόγω του Ισπανικού Εμφυλίου Πολέμου.",
        [
            "Ο Christian Dior αποκαλούσε τον Balenciaga 'ο δάσκαλος όλων μας'.",
            "Υπό τη σύγχρονη καθοδήγηση του Demna Gvasalia, ο οίκος έγινε πρωτοπόρος σε ανατρεπτικά και viral σχέδια όπως τα chunky sneakers Triple S."
        ],
        "https://en.wikipedia.org/wiki/Balenciaga",
        ["balenciaga", "fashion", "spain", "haute_couture"]
    ),
    # 299
    make_q(
        "pop_culture_med_299",
        "Ποιο εμβληματικό μοντέλο τσάντας του Louis Vuitton δημιουργήθηκε το 1930 με το αρχικό όνομα 'Express' και έγινε αγαπημένο της Audrey Hepburn;",
        "Speedy",
        ["Neverfull", "Keepall", "Alma"],
        "Η τσάντα Speedy σχεδιάστηκε ως μια μικρότερη καθημερινή εκδοχή του ταξιδιωτικού σάκου Keepall για να ανταποκριθεί στις γρήγορες μετακινήσεις της εποχής.",
        [
            "Η Audrey Hepburn ζήτησε προσωπικά από τη Louis Vuitton να φτιάξει μια μικρότερη έκδοση (Speedy 25) ειδικά για εκείνη το 1965.",
            "Κατασκευάζεται από τον χαρακτηριστικό επικαλυμμένο καμβά Monogram με φυσικές δερμάτινες λαβές Vachetta."
        ],
        "https://en.wikipedia.org/wiki/Louis_Vuitton#Speedy",
        ["louis_vuitton", "speedy", "fashion", "luxury", "audrey_hepburn"]
    ),
    # 300
    make_q(
        "pop_culture_med_300",
        "Ποια Βρετανίδα ηθοποιός έγινε παγκόσμιο θέμα συζήτησης το 1994 φορώντας το μαύρο φόρεμα Versace με τις τεράστιες χρυσές παραμάνες στην πρεμιέρα του 'Four Weddings and a Funeral';",
        "Elizabeth Hurley",
        ["Hugh Grant", "Emma Thompson", "Helena Bonham Carter"],
        "Η Elizabeth Hurley συνόδευσε τον τότε σύντροφό της Hugh Grant φορώντας το τολμηρό φόρεμα, μια στιγμή που εκτόξευσε την καριέρα της μέσα σε ένα μόνο βράδυ.",
        [
            "Το φόρεμα έγινε γνωστό στα μέσα απλώς ως 'That Dress' και θεωρείται μία από τις πιο αναγνωρίσιμες εμφανίσεις στο κόκκινο χαλί στην ιστορία.",
            "Ο Gianni Versace δήλωσε ότι εμπνεύστηκε τις παραμάνες από το πανκ κίνημα συνδυασμένο με την αρχαιοελληνική ενδυμασία."
        ],
        "https://en.wikipedia.org/wiki/Black_Versace_dress_of_Elizabeth_Hurley",
        ["elizabeth_hurley", "versace", "safety_pin_dress", "fashion"]
    ),
    # 301
    make_q(
        "pop_culture_med_301",
        "Σε ποιο ιστορικό νησάκι της Κρήτης που λειτούργησε ως λεπροκομείο εκτυλίσσεται η πολυβραβευμένη δραματική σειρά του Mega 'Το Νησί' (2010);",
        "Σπιναλόγκα",
        ["Χρυσή", "Γαύδος", "Κουφονήσι"],
        "Η σειρά βασίστηκε στο διεθνές best seller μυθιστόρημα της Victoria Hislop και αφηγείται τις συγκλονιστικές ζωές των κατοίκων της Σπιναλόγκας από το 1903 έως το 1957.",
        [
            "Υπήρξε μία από τις πιο ακριβές ελληνικές τηλεοπτικές παραγωγές όλων των εποχών, με κόστος άνω των 4 εκατομμυρίων ευρώ.",
            "Σημείωσε τεράστια επιτυχία με τηλεθέαση που ξεπέρασε το 60% και προβλήθηκε σε πολλές ξένες χώρες."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9D%CE%B7%CF%83%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
        ["to_nisi", "spinalonga", "mega", "greek_tv"]
    ),
    # 302
    make_q(
        "pop_culture_med_302",
        "Στην κωμική σειρά 'Σαββατογεννημένες' (2003-2004), πόσες γυναίκες μοιράζονταν εν αγνοία τους το κερδοφόρο λαχείο με τον Σάββα Τζόγιο;",
        "Τρεις",
        ["Δύο", "Τέσσερις", "Πέντε"],
        "Ο Σάββας (Σάκης Μπουλάς) είχε συμπληρώσει το ίδιο λαχείο με την πρώην σύζυγο Μπία (Ελένη Ράντου), την εν διαστάσει Καίτη (Ρένια Λουιζίδου) και την ερωμένη Σούλα (Βασιλική Ανδρίτσου).",
        [
            "Μετά από ατύχημα που του προκαλεί αμνησία, οι τρεις γυναίκες αναγκάζονται να συνεργαστούν για να εντοπίσουν τον κερδοφόρο λαχνό.",
            "Η σειρά αποτέλεσε το εξαιρετικά επιτυχημένο συγγραφικό ντεμπούτο του Γιώργου Καπουτζίδη στην τηλεόραση."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%B2%CE%B2%CE%B1%CF%84%CE%BF%CE%B3%CE%B5%CE%BD%CE%BD%CE%B7%CE%BC%CE%AD%CE%BD%CE%B5%CF%82",
        ["savvatogennimenes", "kapoutzidis", "mega", "greek_tv"]
    ),
    # 303
    make_q(
        "pop_culture_med_303",
        "Ποιο ήταν το όνομα του χαρακτήρα που υποδυόταν ο Γιώργος Καπουτζίδης στη σειρά 'Σαββατογεννημένες';",
        "Χοσέ Μανουέλ Μαρτίνεθ",
        ["Φώτης Βουρνάς", "Σπύρος Δελόγλου", "Μίλτος"],
        "Ο Χοσέ ήταν ένας πολυλογάς και καλόκαρδος πολιτικός πρόσφυγας που δούλευε ως βοηθός στο κατάστημα της Μπίας Ντούλου.",
        [
            "Η χαρακτηριστική προφορά του και η ατάκα 'Κυρία Μπία!' έγιναν άμεσα σήμα κατατεθέν της σειράς.",
            "Η ερμηνεία του Καπουτζίδη ως Χοσέ τον καθιέρωσε στο ελληνικό τηλεοπτικό κοινό τόσο ως σεναριογράφο όσο και ως κωμικό ηθοποιό."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%B2%CE%B2%CE%B1%CF%84%CE%BF%CE%B3%CE%B5%CE%BD%CE%BD%CE%B7%CE%BC%CE%AD%CE%BD%CE%B5%CF%82",
        ["savvatogennimenes", "jose", "kapoutzidis", "greek_tv"]
    ),
    # 304
    make_q(
        "pop_culture_med_304",
        "Στη μαύρη κωμωδία 'Εγκλήματα' (ΑΝΤ1, 1998-2000), ποιος ήταν ο ιδιοκτήτης κρεοπωλείου που απατούσε τη γυναίκα του με τη Φλώρα;",
        "Αλέκος Παπαδήμας (Κώστας Κόκλας)",
        ["Μιχαήλ", "Παύλος", "Τάσος"],
        "Ο Αλέκος ήταν παντρεμένος με τη σατανική Σωσώ (Υρώ Μανέ) και διατηρούσε παράνομο δεσμό με την παντρεμένη Φλώρα (Υρώ Λούπη).",
        [
            "Η σειρά του Λευτέρη Παπαπέτρου θεωρείται μία από τις πιο τολμηρές και ανατρεπτικές μαύρες κωμωδίες της ελληνικής τηλεόρασης.",
            "Η Σωσώ Παπαδήμα κατέστρωνε διαρκώς μακάβρια σχέδια δολοφονίας για τον Αλέκο και τη Φλώρα, ακούγοντας κλασική όπερα."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
        ["eglimata", "soso", "ant1", "greek_tv", "comedy"]
    ),
    # 305
    make_q(
        "pop_culture_med_305",
        "Ποια ηθοποιός ενσάρκωσε την αδίστακτη αλλά απολαυστική Σωσώ Παπαδήμα στα 'Εγκλήματα';",
        "Υρώ Μανέ",
        ["Μαρία Καβογιάννη", "Καίτη Κωνσταντίνου", "Υρώ Λούπη"],
        "Η Υρώ Μανέ δημιούργησε έναν από τους πιο εμβληματικούς ρόλους 'κακιάς' στην ελληνική τηλεόραση, με κατάμαυρο χιούμορ και ψυχρότητα.",
        [
            "Η Σωσώ δεν δίσταζε να δηλητηριάσει γλυκά, να σαμποτάρει αυτοκίνητα και να προσλάβει εκτελεστές για να ξεφορτωθεί τον σύζυγό της.",
            "Η σκηνή όπου ετοιμάζει τα δηλητηριασμένα κουραμπιεδάκια για τα Χριστούγεννα παραμένει κλασική."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
        ["eglimata", "yro_mane", "soso", "greek_tv"]
    ),
    # 306
    make_q(
        "pop_culture_med_306",
        "Ποια θρυλική σατιρική εκπομπή της Θεσσαλονίκης με τους Αντώνη Κανάκη και Σωτήρη Καλυβάτση ξεκίνησε στο Mega το 1997;",
        "Α.Μ.Α.Ν.",
        ["Comfuzio", "Ράδιο Αρβύλα", "Όχι τα Νέα του ΑΝΤ1"],
        "Το Α.Μ.Α.Ν. καθιέρωσε ένα μοναδικό είδος τηλεοπτικής σάτιρας με γρήγορα σκετς, παρωδίες διαφημίσεων και αυτοσχεδιαστικό χιούμορ.",
        [
            "Η ομάδα είχε ξεκινήσει νωρίτερα στη νεανική εκπομπή 'Comfuzio' στην ΕΤ3.",
            "Μετά τη μεταγραφή στον ΑΝΤ1, η εκπομπή μετονομάστηκε σε 'Α.Μ.Α.Ν. Τα Καθάρματα'."
        ],
        "https://el.wikipedia.org/wiki/%CE%91.%CE%9C.%CE%91.%CE%9D.",
        ["aman", "kanakis", "kalyvatsis", "greek_tv", "satire"]
    ),
    # 307
    make_q(
        "pop_culture_med_307",
        "Προς τιμήν ποιου εκλιπόντος συνεργάτη και φίλου τους έδωσαν οι δημιουργοί το όνομα 'Α.Μ.Α.Ν.' (Αντώνη Μας Άφησες Νωρίς);",
        "Αντώνης Παραράς",
        ["Αντώνης Βαρδής", "Αντώνης Καλογιάννης", "Αντώνης Τρικαμηνάς"],
        "Ο Αντώνης Παραράς ήταν μέλος της αρχικής παρέας του Comfuzio και έφυγε πρόωρα από τη ζωή από λευχαιμία το 1997 σε ηλικία μόλις 29 ετών.",
        [
            "Οι Αντώνης Κανάκης και Σωτήρης Καλυβάτσης αφιέρωσαν την εκπομπή στη μνήμη του μετατρέποντας το επιφώνημα 'αμάν' σε συγκινητικό ακρωνύμιο.",
            "Ο Παραράς ήταν ένας από τους πιο ταλαντούχους και αγαπητούς νέους παρουσιαστές της εποχής του."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%8E%CE%BD%CE%B7%CF%82_%CE%A0%CE%B1%CF%81%CE%B1%CF%81%CE%AC%CF%82",
        ["antonis_pararas", "aman", "greek_tv", "tribute"]
    ),
    # 308
    make_q(
        "pop_culture_med_308",
        "Ποιος αυστηρός και συντηρητικός δήμαρχος στο 'Καφέ της Χαράς' είχε θέσει ως στόχο να διώξει την πρωτευουσιάνα Χαρά Χάσκα;",
        "Περίανδρος Πώποτας (Χάρης Ρώμας)",
        ["Φατσέας", "Τάσος", "Πολυμενέας"],
        "Ο Περίανδρος Πώποτας διοικούσε το Κολοκοτρωνίτσι με αυταρχικότητα και εμμονή στην παράδοση, συγκρουόμενος σφοδρά με τη μοντέρνα Χαρά (Ρένια Λουιζίδου).",
        [
            "Η σειρά των Χάρη Ρώμα και Άννας Χατζησοφιά προβλήθηκε στον ΑΝΤ1 από το 2003 έως το 2006 (και επανήλθε το 2019-2021).",
            "Ο γιος του, Μανωλάκης, και η κόρη της Χαράς, Βάλια, ανέπτυξαν μια παιδική αγάπη που γεφύρωσε τους δύο κόσμους."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
        ["kafe_tis_charas", "popotas", "haris_romas", "ant1", "greek_tv"]
    ),
    # 309
    make_q(
        "pop_culture_med_309",
        "Πώς ονομαζόταν το φανταστικό ορεινό αρκαδικό χωριό όπου διαδραματίζεται η ιστορία στο 'Καφέ της Χαράς';",
        "Κολοκοτρωνίτσι",
        ["Αραχωβίτσα", "Πλατανόρεμα", "Καστανίτσα"],
        "Τα εξωτερικά γυρίσματα του χωριού Κολοκοτρωνίτσι πραγματοποιήθηκαν κυρίως στον γραφικό ιστορικό οικισμό της Καρυάς Αργολίδας.",
        [
            "Το χωριό χαρακτηριζόταν από την πλήρη απομόνωσή του από τον μοντέρνο τρόπο ζωής μέχρι την άφιξη της Χαράς και το άνοιγμα του καφέ.",
            "Η επιτυχία της σειράς μετέτρεψε την Καρυά σε δημοφιλή τουριστικό προορισμό για τους θαυμαστές της σειράς."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
        ["kafe_tis_charas", "kolokotronitsi", "greek_tv"]
    ),
    # 310
    make_q(
        "pop_culture_med_310",
        "Ποιο ήταν το περίφημο επίσημο σύνθημα του δημάρχου Περίανδρου Πώποτα για τους κατοίκους του Κολοκοτρωνιτσίου;",
        "Τάξις και Ηθική",
        ["Πίστη και Πατρίδα", "Παράδοση και Έθιμα", "Καθαριότητα και Τάξη"],
        "Ο Πώποτας επαναλάμβανε συνεχώς το δόγμα 'Τάξις και Ηθική', επιβάλλοντας πρόστιμα και τιμωρίες σε όποιον χωριανό παραβίαζε τα χρηστά ήθη.",
        [
            "Ο χαρακτήρας του Ευάγγελου Φατσέα (Γεράσιμος Σκιαδαρέσης) με τα ανύπαρκτα ελληνικά του ('φατσεϊκά') έγινε επίσης τεράστιο φαινόμενο.",
            "Η λέξη 'φατσεϊκά' χρησιμοποιείται έκτοτε στη νεοελληνική αργκό για να περιγράψει ξεκαρδιστικά σολοικισμούς και λάθη στη γλώσσα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
        ["kafe_tis_charas", "taxis_kai_ithiki", "popotas", "greek_tv"]
    ),
]

if __name__ == "__main__":
    validate_and_append("pop_culture", "medium", 3, questions)

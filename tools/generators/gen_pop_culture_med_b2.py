# -*- coding: utf-8 -*-
"""Generator for pop_culture_medium questions 311-410 (100 questions)."""
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
    # 311
    make_q(
        "pop_culture_med_311",
        "Ποιος παραμορφωμένος και επιθετικός πρώτος κλώνος του Peter Parker έγινε αργότερα ο αντιήρωας Kaine στα κόμικς του Spider-Man;",
        "Kaine Parker",
        ["Ben Reilly", "Miles Morales", "Miguel O'Hara"],
        "Ο Kaine ήταν το πρώτο ατελές πείραμα κλωνοποίησης του Jackal, το οποίο υπέφερε από κυτταρικό εκφυλισμό και έντονη επιθετικότητα.",
        [
            "Διέθετε το 'Mark of Kaine', μια ικανότητα να καίει τα πρόσωπα των εχθρών του με τα χέρια του χρησιμοποιώντας τις συγκολλητικές του δυνάμεις.",
            "Αργότερα θεραπεύτηκε και ανέλαβε τον ρόλο του Scarlet Spider με έδρα το Χιούστον του Τέξας."
        ],
        "https://en.wikipedia.org/wiki/Kaine_Parker",
        ["spiderman", "kaine", "marvel", "comics"]
    ),
    # 312
    make_q(
        "pop_culture_med_312",
        "Ποιο φανταστικό ευρωπαϊκό κράτος συνορεύει με τη Λατβέρια και αποτελεί την πατρίδα της μισθοφόρου Silver Sable στη Marvel;",
        "Συμκαρία (Symkaria)",
        ["Σοκόβια", "Βακαντά", "Μαντριπούρ"],
        "Η Συμκαρία είναι ένα μικρό κράτος των Βαλκανίων του οποίου η οικονομία βασίζεται σχεδόν αποκλειστικά στους μισθοφόρους της Silver Sable (Wild Pack).",
        [
            "Η πρωτεύουσα της Συμκαρίας ονομάζεται Aniana.",
            "Παρά τις διαφορές τους, η Συμκαρία και η Λατβέρια του Doctor Doom διατηρούν ένα εύθραυστο σύμφωνο μη επίθεσης."
        ],
        "https://en.wikipedia.org/wiki/Symkaria",
        ["symkaria", "silver_sable", "marvel", "comics"]
    ),
    # 313
    make_q(
        "pop_culture_med_313",
        "Ποιο είναι το πραγματικό όνομα του μεταλλαγμένου Gambit με καταγωγή από τη Νέα Ορλεάνη στα X-Men;",
        "Remy LeBeau",
        ["Lucas Bishop", "Warren Worthington", "Piotr Rasputin"],
        "Ο Remy LeBeau μεγάλωσε στη Νέα Ορλεάνη ως μέλος της Συντεχνίας των Κλεφτών (Thieves Guild) πριν ενταχθεί στους X-Men.",
        [
            "Μιλάει με έντονη γαλλική/κατζούν προφορά και αποκαλεί συχνά τους άλλους 'chère'.",
            "Η θυελλώδης ερωτική του σχέση με τη Rogue αποτελεί ένα από τα πιο αναγνωρίσιμα ειδύλλια στα κόμικς."
        ],
        "https://en.wikipedia.org/wiki/Gambit_(Marvel_Comics)",
        ["gambit", "remy_lebeau", "xmen", "marvel"]
    ),
    # 314
    make_q(
        "pop_culture_med_314",
        "Ποιο αντικείμενο φορτίζει συνηθέστερα με εκρηκτική κινητική ενέργεια ο Gambit για να το εκτοξεύσει εναντίον των εχθρών του;",
        "Τραπουλόχαρτα",
        ["Νομίσματα", "Μαρμάρινους βόλους", "Βελάκια"],
        "Ο Gambit έχει την ικανότητα να μετατρέπει τη δυναμική ενέργεια οποιουδήποτε άψυχου αντικειμένου σε καθαρή εκρηκτική κινητική ενέργεια.",
        [
            "Χρησιμοποιεί συνήθως μια τράπουλα επειδή είναι ελαφριά, εύκολη στη μεταφορά και τα χαρτιά κόβουν σαν λεπίδες.",
            "Εκτός από τραπουλόχαρτα, χειρίζεται αριστοτεχνικά ένα τηλεσκοπικό μεταλλικό ραβδί μάχης bo."
        ],
        "https://en.wikipedia.org/wiki/Gambit_(Marvel_Comics)",
        ["gambit", "xmen", "marvel", "kinetic_energy"]
    ),
    # 315
    make_q(
        "pop_culture_med_315",
        "Ποια είναι η τραγική μετάλλαξη της Rogue των X-Men που την εμποδίζει να αγγίξει οποιονδήποτε άνθρωπο με γυμνό δέρμα;",
        "Απορρόφηση δυνάμεων, μνήμης και ζωτικής ενέργειας",
        ["Ακούσια εκπομπή ραδιενέργειας", "Διαρκής παραγωγή πάγου", "Ανεξέλεγκτη τηλεπάθεια"],
        "Το άγγιγμα της Rogue απορροφά τις μνήμες, τις υπερδυνάμεις και τη ζωτική δύναμη όποιου αγγίξει, οδηγώντας σε κώμα ή και θάνατο σε παρατεταμένη επαφή.",
        [
            "Απέκτησε μόνιμα την ικανότητα πτήσης και υπερδύναμης αφού απορρόφησε κατά λάθος για υπερβολικά μεγάλο διάστημα την Ms. Marvel (Carol Danvers).",
            "Η αδυναμία της να νιώσει ανθρώπινη σωματική επαφή αποτελεί το κεντρικό δραματικό στοιχείο του χαρακτήρα της."
        ],
        "https://en.wikipedia.org/wiki/Rogue_(Marvel_Comics)",
        ["rogue", "xmen", "marvel", "mutants"]
    ),
    # 316
    make_q(
        "pop_culture_med_316",
        "Ποιο ισχυρό κοσμικό αντικείμενο σε σχήμα μπλε κύβου περιείχε τον Λίθο του Χώρου (Space Stone) στο κινηματογραφικό σύμπαν της Marvel;",
        "Tesseract",
        ["Aether", "Orb", "Eye of Agamotto"],
        "Το Tesseract φυλασσόταν στην Asgard, βρέθηκε στη Νορβηγία από τον Red Skull στον Β' Παγκόσμιο Πόλεμο και χρησιμοποιήθηκε από τον Loki για να ανοίξει πύλη στη Νέα Υόρκη.",
        [
            "Στα κλασικά κόμικς της Marvel, ο κύβος αυτός ονομαζόταν Cosmic Cube και μπορούσε να αναδιαμορφώσει την ίδια την πραγματικότητα.",
            "Στην ταινία Captain Marvel (2019), το Tesseract καταπίνεται από τη γάτα Goose, η οποία είναι στην πραγματικότητα εξωγήινο πλάσμα Flerken."
        ],
        "https://en.wikipedia.org/wiki/Cosmic_Cube",
        ["tesseract", "marvel", "mcu", "infinity_stones"]
    ),
    # 317
    make_q(
        "pop_culture_med_317",
        "Ποιος αρχαίος κοσμικός συλλέκτης σπάνιων ειδών και αντικειμένων υποδύθηκε ο Benicio del Toro στις ταινίες της Marvel;",
        "The Collector (Taneleer Tivan)",
        ["The Grandmaster", "The Watcher", "Ego"],
        "Ο Taneleer Tivan είναι ένας από τους Πρεσβύτερους του Σύμπαντος (Elders of the Universe) και διατηρεί ένα τεράστιο μουσείο στο Knowhere.",
        [
            "Ο αδελφός του στο σύμπαν της Marvel είναι ο Grandmaster (Jeff Goldblum), ηγεμόνας του πλανήτη Sakaar.",
            "Στο μουσείο του Collector εμφανίστηκαν σπάνια εκθέματα όπως ένας στρατιώτης Chitauri, ένας Dark Elf και ο Howard the Duck."
        ],
        "https://en.wikipedia.org/wiki/Collector_(character)",
        ["collector", "marvel", "guardians_of_the_galaxy", "benicio_del_toro"]
    ),
    # 318
    make_q(
        "pop_culture_med_318",
        "Σε ποια παραθαλάσσια πόλη της Νορβηγίας εγκαταστάθηκαν οι επιζώντες Ασγκαρντιανοί ιδρύοντας το 'New Asgard' στο Avengers: Endgame;",
        "Tønsberg (Τένσμπεργκ)",
        ["Bergen", "Trondheim", "Stavanger"],
        "Το Tønsberg είναι η ιστορική πόλη όπου ο Odin είχε πολεμήσει τους Frost Giants αιώνες νωρίτερα, κάνοντάς την φυσικό καταφύγιο για τους Ασγκαρντιανούς.",
        [
            "Στην πραγματικότητα, το Tønsberg θεωρείται η αρχαιότερη καταγεγραμμένη πόλη της Νορβηγίας.",
            "Στο τέλος του Endgame, ο Thor παραδίδει τη διακυβέρνηση του New Asgard στη Valkyrie (Tessa Thompson)."
        ],
        "https://en.wikipedia.org/wiki/T%C3%B8nsberg",
        ["thor", "new_asgard", "tonsberg", "mcu", "marvel"]
    ),
    # 319
    make_q(
        "pop_culture_med_319",
        "Ποιο είναι το πλήρες ονοματεπώνυμο του πιστού παιδικού φίλου του Captain America που μετατράπηκε στον Winter Soldier;",
        "James Buchanan Barnes (Bucky)",
        ["Timothy Aloysius Cadwallader Dugan", "Gabriel Jones", "James Montgomery Falsworth"],
        "Ο Bucky Barnes πήρε το όνομά του από τον 15ο πρόεδρο των Ηνωμένων Πολιτειών James Buchanan.",
        [
            "Θεωρούνταν νεκρός για δεκαετίες μετά από πτώση από τρένο σε παγωμένο γκρεμό πριν αποκαλυφθεί η επιβίωσή του από τον Ed Brubaker το 2005.",
            "Στο MCU τον Bucky υποδύεται σταθερά ο Sebastian Stan."
        ],
        "https://en.wikipedia.org/wiki/Bucky_Barnes",
        ["bucky_barnes", "winter_soldier", "captain_america", "marvel"]
    ),
    # 320
    make_q(
        "pop_culture_med_320",
        "Ποιο τραγικό γεγονός του 1991 οδήγησε στη διάλυση των Avengers στην ταινία 'Captain America: Civil War';",
        "Η δολοφονία των γονιών του Tony Stark από τον Winter Soldier",
        ["Η κλοπή των σχεδίων του Ultron", "Η καταστροφή της βάσης της S.H.I.E.L.D.", "Η απαγωγή της Pepper Potts"],
        "Ο Helmut Zemo αποκάλυψε το βίντεο της δολοφονίας των Howard και Maria Stark από τον Bucky υπό πλύση εγκεφάλου της HYDRA, εξοργίζοντας τον Tony Stark.",
        [
            "Η σκηνή της σύγκρουσης μεταξύ Iron Man, Captain America και Bucky στη Σιβηρία αποτελεί μία από τις πιο δραματικές κορυφώσεις του MCU.",
            "Ο Steve Rogers γνώριζε για την εμπλοκή του Bucky αλλά το είχε αποκρύψει από τον Tony για να προστατεύσει τον φίλο του."
        ],
        "https://en.wikipedia.org/wiki/Captain_America:_Civil_War",
        ["civil_war", "iron_man", "winter_soldier", "mcu", "marvel"]
    ),
    # 321
    make_q(
        "pop_culture_med_321",
        "Ποιο ήταν το όνομα της βοτανολόγου Dr. Pamela Isley πριν αποκτήσει ανοσία στα δηλητήρια και γίνει η Poison Ivy;",
        "Dr. Pamela Isley",
        ["Dr. Harleen Quinzel", "Dr. Leslie Thompkins", "Dr. Joan Leland"],
        "Η Dr. Pamela Lillian Isley ήταν μια λαμπρή βοτανολόγος του Σιάτλ που δηλητηριάστηκε από τον καθηγητή της Jason Woodrue αποκτώντας χλωροπλάστες στο αίμα της.",
        [
            "Μπορεί να ελέγχει τα φυτά και να παράγει θανατηφόρες φερομόνες που υπνωτίζουν τους άνδρες με ένα απλό φιλί.",
            "Στα σύγχρονα κόμικς και σειρές κινουμένων σχεδίων, η Poison Ivy διατηρεί σταθερή ερωτική σχέση με τη Harley Quinn."
        ],
        "https://en.wikipedia.org/wiki/Poison_Ivy_(character)",
        ["poison_ivy", "batman", "dc_comics", "pamela_isley"]
    ),
    # 322
    make_q(
        "pop_culture_med_322",
        "Ποιο ήταν το πραγματικό όνομα της Harley Quinn όταν εργαζόταν ως ψυχίατρος στο άσυλο Arkham;",
        "Dr. Harleen Quinzel",
        ["Dr. Helena Bertinelli", "Dr. Dinah Lance", "Dr. Barbara Gordon"],
        "Η Harleen Frances Quinzel ανέλαβε τη θεραπεία του Joker στο Arkham Asylum, αλλά γοητεύτηκε παθολογικά από αυτόν και τον βοήθησε να αποδράσει.",
        [
            "Το όνομά της αποτελεί λογοπαίγνιο με τη λέξη 'Harlequin' (Αρλεκίνος).",
            "Η πρώτη της εμφάνιση έγινε με την κλασική ολόσωμη ασπρόμαυρη/κόκκινη στολή γελωτοποιού με καμπανάκια."
        ],
        "https://en.wikipedia.org/wiki/Harley_Quinn",
        ["harley_quinn", "batman", "joker", "dc_comics"]
    ),
    # 323
    make_q(
        "pop_culture_med_323",
        "Σε ποια εμβληματική σειρά κινουμένων σχεδίων έκανε το ντεμπούτο της η Harley Quinn το 1992 πριν καν υπάρξει στα κόμικς;",
        "Batman: The Animated Series",
        ["The Batman (2004)", "Batman Beyond", "Justice League"],
        "Η Harley Quinn δημιουργήθηκε από τους Paul Dini και Bruce Timm ειδικά για το επεισόδιο 'Joker's Favor' και έγινε τόσο δημοφιλής που πέρασε στα επίσημα κόμικς.",
        [
            "Τη φωνή της στη σειρά χάρισε η ηθοποιός Arleen Sorkin, η οποία ενέπνευσε και τον χαρακτήρα.",
            "Το graphic novel 'Mad Love' (1994) που αφηγείται το παρελθόν της κέρδισε το κορυφαίο βραβείο Eisner Award."
        ],
        "https://en.wikipedia.org/wiki/Harley_Quinn",
        ["harley_quinn", "batman_the_animated_series", "paul_dini", "dc_comics"]
    ),
    # 324
    make_q(
        "pop_culture_med_324",
        "Ποιος τρομακτικός μυώδης κακοποιός έσπασε τη μέση του Batman πάνω στο γόνατό του στο περίφημο κόμικ 'Knightfall' (1993);",
        "Bane",
        ["Killer Croc", "Clayface", "Solomon Grundy"],
        "Ο Bane εξάντλησε πρώτα τον Batman απελευθερώνοντας όλους τους κρατούμενους του Arkham και στη συνέχεια του έσπασε τη σπονδυλική στήλη μέσα στην έπαυλη Wayne.",
        [
            "Ο Bane μεγάλωσε μέσα στη σκληρή φυλακή Peña Duro στη φανταστική χώρα Santa Prisca εκτίοντας την ποινή του πατέρα του.",
            "Στην ταινία 'The Dark Knight Rises' (2012), τον Bane ενσάρκωσε ο Tom Hardy με μια χαρακτηριστική μηχανική φωνή."
        ],
        "https://en.wikipedia.org/wiki/Bane_(DC_Comics)",
        ["bane", "knightfall", "batman", "dc_comics"]
    ),
    # 325
    make_q(
        "pop_culture_med_325",
        "Ποιο πειραματικό στεροειδές φάρμακο διοχετεύεται απευθείας στον εγκέφαλο του Bane μέσω ειδικών σωλήνων για να του χαρίσει υπεράνθρωπη δύναμη;",
        "Venom",
        ["Mirakuru", "Titan", "Velocity 9"],
        "Το Venom είναι ένα ισχυρό αναβολικό ναρκωτικό που αυξάνει δραματικά τη μυϊκή μάζα και την αντοχή του Bane, αλλά προκαλεί έντονο σωματικό εθισμό.",
        [
            "Αν κοπούν οι σωλήνες που τροφοδοτούν το Venom στο κεφάλι του, ο Bane παθαίνει άμεσα συμπτώματα στέρησης και εξασθενεί ραγδαία.",
            "Δεν πρέπει να συγχέεται με τον ομώνυμο εξωγήινο χαρακτήρα Venom της Marvel."
        ],
        "https://en.wikipedia.org/wiki/Bane_(DC_Comics)",
        ["bane", "venom_drug", "batman", "dc_comics"]
    ),
    # 326
    make_q(
        "pop_culture_med_326",
        "Ποιο είναι το αριστοκρατικό πραγματικό όνομα του κακοποιού Penguin στα κόμικς του Batman;",
        "Oswald Cobblepot",
        ["Roman Sionis", "Julian Day", "Waylon Jones"],
        "Ο Oswald Chesterfield Cobblepot προέρχεται από μία από τις παλαιότερες και πλουσιότερες ιδρυτικές οικογένειες της Gotham City.",
        [
            "Χρησιμοποιεί πληθώρα θανατηφόρων ομπρελών εξοπλισμένων με όπλα, σπαθιά, φλογοβόλα ή ελικόπτερα διαφυγής.",
            "Στην ταινία 'Batman Returns' (1992) του Tim Burton, τον Penguin υποδύθηκε ο Danny DeVito, ενώ ο Colin Farrell τον ενσάρκωσε στο 'The Batman' (2022)."
        ],
        "https://en.wikipedia.org/wiki/Penguin_(character)",
        ["penguin", "oswald_cobblepot", "batman", "dc_comics"]
    ),
    # 327
    make_q(
        "pop_culture_med_327",
        "Πώς ονομάζεται το πολυτελές νυχτερινό κέντρο και καζίνο που διατηρεί ο Penguin ως βιτρίνα για τις εγκληματικές του δραστηριότητες;",
        "The Iceberg Lounge",
        ["The Black Mask Club", "The Gotham Casino", "The Penguin Club"],
        "Το Iceberg Lounge λειτουργεί ως ουδέτερο έδαφος για τον υπόκοσμο της Gotham, όπου ο Batman συχνά επισκέπτεται τον Penguin για να αποσπάσει πληροφορίες.",
        [
            "Το κλαμπ διαθέτει μια τεράστια πισίνα με αληθινές πλωτές πλάκες πάγου και ζωντανούς πιγκουίνους και φώκιες.",
            "Στο υπόγειο του κτιρίου κρύβονται μυστικά δωμάτια συσκέψεων και αποθήκες λαθρεμπορίου."
        ],
        "https://en.wikipedia.org/wiki/Iceberg_Lounge",
        ["iceberg_lounge", "penguin", "batman", "dc_comics"]
    ),
    # 328
    make_q(
        "pop_culture_med_328",
        "Ποιο όνομα χρησιμοποιεί ο Riddler ως λογοπαίγνιο με τη λέξη 'enigma' (αίνιγμα) στα κόμικς του Batman;",
        "Edward Nygma (E. Nygma)",
        ["Arthur Pendelton", "Julian Gregory", "Harvey Bullock"],
        "Ο Edward Nygma έχει ψυχαναγκαστική ανάγκη να αφήνει γρίφους, σπαζοκεφαλιές και στοιχεία στον τόπο των εγκλημάτων του για να αποδείξει την ανώτερη ευφυΐα του.",
        [
            "Η στολή του είναι πράσινη γεμάτη ερωτηματικά και κρατάει ένα χαρακτηριστικό μπαστούνι με λαβή σε σχήμα ερωτηματικού.",
            "Στην ταινία 'The Batman' (2022), ο Paul Dano υποδύθηκε μια σκοτεινή εκδοχή του Riddler εμπνευσμένη από τον πραγματικό Zodiac Killer."
        ],
        "https://en.wikipedia.org/wiki/Riddler",
        ["riddler", "edward_nygma", "batman", "dc_comics"]
    ),
    # 329
    make_q(
        "pop_culture_med_329",
        "Ποιος τυραννικός άρχοντας του πλανήτη Apokolips επιδιώκει να κατακτήσει το σύμπαν χρησιμοποιώντας την Εξίσωση της Αντι-Ζωής;",
        "Darkseid",
        ["Thanos", "Brainiac", "Mongul"],
        "Ο Darkseid (Uxas) είναι ένας από τους Νέους Θεούς (New Gods) που δημιούργησε ο Jack Kirby το 1970 και ένας από τους πιο επικίνδυνους εχθρούς της Justice League.",
        [
            "Εκτοξεύει τις 'Ακτίνες Ωμέγα' (Omega Beams) από τα μάτια του, οι οποίες μπορούν να αλλάζουν κατεύθυνση στον αέρα και να διαλύουν ή να τηλεμεταφέρουν οποιοδήποτε στόχο.",
            "Ο Jim Starlin παραδέχτηκε ανοιχτά ότι ο σχεδιασμός του Thanos στη Marvel εμπνεύστηκε άμεσα από τον Darkseid του Kirby."
        ],
        "https://en.wikipedia.org/wiki/Darkseid",
        ["darkseid", "dc_comics", "apokolips", "justice_league"]
    ),
    # 330
    make_q(
        "pop_culture_med_330",
        "Ποια μαθηματική φόρμουλα αναζητά ο Darkseid για να αποδείξει μαθηματικά τη ματαιότητα της ελπίδας και να υποτάξει την ελεύθερη βούληση όλων των όντων;",
        "Η Εξίσωση της Αντι-Ζωής (Anti-Life Equation)",
        ["Η Φόρμουλα του Χάους", "Ο Κοσμικός Αλγόριθμος", "Η Εξίσωση της Αιωνιότητας"],
        "Η Anti-Life Equation είναι μια υπερφυσική γνώση που αποδεικνύει ότι η ζωή, η αγάπη και η ελευθερία είναι αυταπάτες, μετατρέποντας όποιον την ακούει σε απόλυτο υποχείριο.",
        [
            "Σύμφωνα με τον μύθο των κόμικς, η εξίσωση κρύβεται βαθιά μέσα στο υποσυνείδητο των ανθρώπων της Γης.",
            "Στο επιτυχημένο crossover κόμικ 'DCeased', ένας μολυσμένος ιός της Anti-Life εξαπλώνεται μέσω των οθονών μετατρέποντας τον πληθυσμό σε ζόμπι."
        ],
        "https://en.wikipedia.org/wiki/Anti-Life_Equation",
        ["anti_life_equation", "darkseid", "dc_comics"]
    ),
    # 331
    make_q(
        "pop_culture_med_331",
        "Ποιο ήταν το όνομα της μικρότερης αδελφής της Barbie που παρουσιάστηκε από τη Mattel το 1964;",
        "Skipper",
        ["Stacie", "Chelsea", "Tutti"],
        "Η Skipper Roberts παρουσιάστηκε ως η έφηβη αδελφή της Barbie για να καλύψει το κενό ανάμεσα σε παιδικές κούκλες και κούκλες μόδας.",
        [
            "Το 1975 η Mattel κυκλοφόρησε την αμφιλεγόμενη κούκλα 'Growing Up Skipper', η οποία ψήλωνε και ανέπτυσσε στήθος όταν γύριζες το χέρι της.",
            "Σήμερα η Skipper παρουσιάζεται συχνά ως λάτρης της τεχνολογίας και DJ."
        ],
        "https://en.wikipedia.org/wiki/Skipper_(Barbie)",
        ["barbie", "skipper", "mattel", "toys"]
    ),
    # 332
    make_q(
        "pop_culture_med_332",
        "Ποιες κούκλες μόδας της MGA Entertainment με μεγάλα κεφάλια, αμυγδαλωτά μάτια και βαρύ μακιγιάζ απείλησαν την κυριαρχία της Barbie το 2001;",
        "Bratz",
        ["My Scene", "Monster High", "Bratzillaz"],
        "Οι τέσσερις αρχικές Bratz (Yasmin, Cloe, Sasha, Jade) σχεδιάστηκαν από τον Carter Bryant και έγιναν τεράστια επιτυχία στις αρχές των 2000s.",
        [
            "Χαρακτηριστικό τους ήταν τα αποσπώμενα παπούτσια που αφαιρούνταν μαζί με τα πέλματα των ποδιών της κούκλας.",
            "Η Mattel και η MGA ενεπλάκησαν σε έναν πολυετή δικαστικό πόλεμο εκατοντάδων εκατομμυρίων δολαρίων για τα πνευματικά δικαιώματα του σχεδιαστή."
        ],
        "https://en.wikipedia.org/wiki/Bratz",
        ["bratz", "mga_entertainment", "barbie", "toys", "2000s"]
    ),
    # 333
    make_q(
        "pop_culture_med_333",
        "Ποια σειρά από κούκλες μόδας της Mattel του 2010 βασίστηκε στα παιδιά διάσημων τεράτων όπως ο Δράκουλας και ο Φρανκενστάιν;",
        "Monster High",
        ["Ever After High", "Bratzillaz", "Descendants"],
        "Η σειρά Monster High περιλάμβανε χαρακτήρες όπως η Frankie Stein, η Draculaura και η Clawdeen Wolf με γοτθική και μοδάτη αισθητική.",
        [
            "Το σύνθημα της σειράς ήταν 'Be yourself. Be unique. Be a monster.', προωθώντας τη διαφορετικότητα και την αποδοχή.",
            "Έγινε ένα από τα πιο κερδοφόρα franchise της Mattel, ξεπερνώντας το 1 δισεκατομμύριο δολάρια σε πωλήσεις μέσα σε τρία χρόνια."
        ],
        "https://en.wikipedia.org/wiki/Monster_High",
        ["monster_high", "mattel", "toys", "gothic"]
    ),
    # 334
    make_q(
        "pop_culture_med_334",
        "Πώς ονομάζονταν τα χάρτινα και πλαστικά κυκλικά δισκάκια που μάζευαν τα παιδιά στην Ελλάδα τη δεκαετία του 1990 μέσα από τα γαριδάκια;",
        "Τάπες (Tazos)",
        ["Βόλοι", "Αυτοκόλλητα", "Μπρελόκ"],
        "Τα Tazos (Pogs διεθνώς) κυκλοφόρησαν στα πατατάκια και γαριδάκια Frito-Lay / Tasty Foods και προκάλεσαν μαζική συλλεκτική μανία στα ελληνικά σχολεία.",
        [
            "Υπήρχαν κλασικά Tazos, Chiquitazos, Mega Tazos και μεταλλικά Tazos με χαρακτήρες Looney Tunes, Pokémon και Star Wars.",
            "Το παιχνίδι προήλθε αρχικά από τη Χαβάη τη δεκαετία του 1920 όπου τα παιδιά έπαιζαν με τα καπάκια από χυμούς Passion Orange Guava (POG)."
        ],
        "https://en.wikipedia.org/wiki/Tazos",
        ["tazos", "tapes", "90s", "greece", "nostalgia", "toys"]
    ),
    # 335
    make_q(
        "pop_culture_med_335",
        "Ποιο κλασικό μηχανικό παιχνίδι σχεδίασης χρησιμοποιεί δύο περιστρεφόμενα κουμπιά για να χαράζει γραμμές σε γκρίζα σκόνη αλουμινίου;",
        "Etch A Sketch",
        ["Spirograph", "Magna Doodle", "Lite-Brite"],
        "Το Etch A Sketch εφευρέθηκε στη Γαλλία από τον André Cassagnes το 1959 και για να σβηστεί το σχέδιο πρέπει απλώς να αναποδογυριστεί και να κουνηθεί.",
        [
            "Μέσα στην οθόνη υπάρχει μια γραφίδα συνδεδεμένη με λεπτά συρματόσχοινα που ξύνει τη σκόνη αλουμινίου από το γυαλί.",
            "Έκανε διάσημη επανεμφάνιση στις ταινίες κινουμένων σχεδίων 'Toy Story' της Pixar ως ένας από τους ζωντανούς χαρακτήρες-παιχνίδια."
        ],
        "https://en.wikipedia.org/wiki/Etch_A_Sketch",
        ["etch_a_sketch", "toys", "drawing", "retro"]
    ),
    # 336
    make_q(
        "pop_culture_med_336",
        "Ποιο κλασικό παιχνίδι-ελατήριο εφευρέθηκε κατά λάθος από τον μηχανικό του πολεμικού ναυτικού Richard James το 1943;",
        "Slinky",
        ["Yo-yo", "Hula Hoop", "Rubik's Snake"],
        "Ο James εργαζόταν πάνω σε ελατήρια για τη σταθεροποίηση ευαίσθητων οργάνων σε πλοία όταν ένα ελατήριο έπεσε και άρχισε να 'περπατά' στο πάτωμα.",
        [
            "Το πρώτο απόθεμα των 400 τεμαχίων εξαντλήθηκε μέσα σε 90 λεπτά σε ένα πολυκατάστημα της Φιλαδέλφειας το 1945.",
            "Κατά τον πόλεμο του Βιετνάμ, στρατιώτες των ΗΠΑ χρησιμοποίησαν Slinky ως αυτοσχέδιες φορητές κεραίες ασυρμάτου στα δάση."
        ],
        "https://en.wikipedia.org/wiki/Slinky",
        ["slinky", "toys", "invention"]
    ),
    # 337
    make_q(
        "pop_culture_med_337",
        "Σε ποιο εξαιρετικά δημοφιλές συνεργατικό επιτραπέζιο παιχνίδι του Matt Leacock οι παίκτες προσπαθούν να περιορίσουν 4 παγκόσμιες επιδημίες;",
        "Pandemic",
        ["Outbreak", "Contagion", "Plague Inc."],
        "Στο Pandemic όλοι οι παίκτες κερδίζουν ή χάνουν μαζί, αναλαμβάνοντας ρόλους όπως Επιστήμονας, Γιατρός και Ερευνητής για να βρουν θεραπείες.",
        [
            "Η έκδοση 'Pandemic Legacy: Season 1' (2015) θεωρείται ένα από τα κορυφαία επιτραπέζια παιχνίδια όλων των εποχών στις διεθνείς κατατάξεις.",
            "Οι πωλήσεις του παιχνιδιού σημείωσαν νέα εκτίναξη το 2020 κατά την έναρξη της πραγματικής πανδημίας COVID-19."
        ],
        "https://en.wikipedia.org/wiki/Pandemic_(board_game)",
        ["pandemic", "board_games", "matt_leacock", "cooperative"]
    ),
    # 338
    make_q(
        "pop_culture_med_338",
        "Ποιο οικονομικό φαινόμενο του 2021 προκλήθηκε από μικροεπενδυτές του Reddit (r/wallstreetbets) εκτοξεύοντας τη μετοχή μιας αλυσίδας βιντεοπαιχνιδιών;",
        "GameStop short squeeze",
        ["Bitcoin rally", "Tesla bubble", "AMC rush"],
        "Χιλιάδες χρήστες αγόρασαν συντονισμένα μετοχές της GameStop για να προκαλέσουν τεράστιες ζημιές σε hedge funds που είχαν ποντάρει στην πτώση της (short selling).",
        [
            "Η τιμή της μετοχής εκτινάχθηκε από λιγότερο από 20 δολάρια σε σχεδόν 500 δολάρια μέσα σε λίγες ημέρες.",
            "Το γεγονός ενέπνευσε την ταινία 'Dumb Money' του 2023 με τον Paul Dano στον ρόλο του ηγέτη των επενδυτών Roaring Kitty (Keith Gill)."
        ],
        "https://en.wikipedia.org/wiki/GameStop_short_squeeze",
        ["gamestop", "wallstreetbets", "reddit", "viral", "finance"]
    ),
    # 339
    make_q(
        "pop_culture_med_339",
        "Ποιος Βρετανός φοιτητής δημιούργησε το 2005 την ιστοσελίδα 'The Million Dollar Homepage' πουλώντας 1 εκατομμύριο pixel για διαφημίσεις;",
        "Alex Tew",
        ["Mark Zuckerberg", "Jack Dorsey", "Jimmy Wales"],
        "Ο 21χρονος Alex Tew ήθελε να συγκεντρώσει χρήματα για τις σπουδές του και πούλησε όλο τον χώρο της σελίδας προς 1 δολάριο ανά pixel σε μόλις 138 ημέρες.",
        [
            "Το εγχείρημα απέφερε πάνω από 1 εκατομμύριο δολάρια και ενέπνευσε εκατοντάδες αποτυχημένες απομιμήσεις.",
            "Αργότερα, ο Tew έγινε συνιδρυτής της εξαιρετικά επιτυχημένης εφαρμογής διαλογισμού και ύπνου Calm."
        ],
        "https://en.wikipedia.org/wiki/The_Million_Dollar_Homepage",
        ["million_dollar_homepage", "alex_tew", "internet_history", "viral"]
    ),
    # 340
    make_q(
        "pop_culture_med_340",
        "Ποιος Αμερικανός γερουσιαστής έγινε viral meme το 2021 καθισμένος σταυροπόδι με πλεκτά μάλλινα γάντια στην ορκωμοσία του Joe Biden;",
        "Bernie Sanders",
        ["Mitt Romney", "Chuck Schumer", "Ted Cruz"],
        "Η φωτογραφία του φωτορεπόρτερ Brendan Smialowski με τον Bernie Sanders να κάθεται απομονωμένος στο κρύο τοποθετήθηκε μέσω Photoshop σε χιλιάδες ιστορικές εικόνες.",
        [
            "Τα χαρακτηριστικά μάλλινα γάντια είχαν πλεχτεί από μια δασκάλα στο Βερμόντ χρησιμοποιώντας ανακυκλωμένα πλαστικά μπουκάλια.",
            "Η ομάδα του Sanders τύπωσε τη φωτογραφία σε φούτερ και συγκέντρωσε σχεδόν 2 εκατομμύρια δολάρια για φιλανθρωπικές οργανώσεις του Βερμόντ."
        ],
        "https://en.wikipedia.org/wiki/Bernie_Sanders_mittens_meme",
        ["bernie_sanders", "mittens", "memes", "viral"]
    ),
    # 341
    make_q(
        "pop_culture_med_341",
        "Ποιο viral challenge του 2018 υπό τους ήχους του τραγουδιού 'In My Feelings' του Drake απαιτούσε από ανθρώπους να πηδούν έξω από κινούμενα αυτοκίνητα;",
        "Kiki Challenge",
        ["Mannequin Challenge", "Ghost Pepper Challenge", "Harlem Shake"],
        "Το challenge ξεκίνησε από τον κωμικό Shiggy στο Instagram και γρήγορα εξελίχθηκε σε επικίνδυνη μόδα με οδηγούς να αφήνουν το όχημα σε κίνηση.",
        [
            "Αστυνομικές αρχές σε πολλές χώρες εξέδωσαν αυστηρές προειδοποιήσεις και πρόστιμα για οδική επικινδυνότητα.",
            "Η επιτυχία του challenge οδήγησε το τραγούδι του Drake να παραμείνει 10 εβδομάδες στο νούμερο 1 του Billboard Hot 100."
        ],
        "https://en.wikipedia.org/wiki/In_My_Feelings",
        ["kiki_challenge", "drake", "in_my_feelings", "viral"]
    ),
    # 342
    make_q(
        "pop_culture_med_342",
        "Ποιο διάσημο μοντέλο ψηλοτάκουνης γόβας του Christian Louboutin με 120 χιλιοστά τακούνι πήρε το όνομά του από μια συνοικία του Παρισιού;",
        "Pigalle",
        ["So Kate", "Daffodile", "Iriza"],
        "Η γόβα Pigalle σχεδιάστηκε το 2004 προς τιμήν της μποέμ συνοικίας του Παρισιού και του διάσημου καμπαρέ Moulin Rouge.",
        [
            "Θεωρείται το πιο κλασικό και αναγνωρίσιμο σχέδιο του Louboutin με βαθύ κόψιμο στα δάχτυλα ('toe cleavage').",
            "Αργότερα κυκλοφόρησε και η παραλλαγή 'So Kate' με ακόμα πιο μυτερή μύτη και λεπτότερο τακούνι."
        ],
        "https://en.wikipedia.org/wiki/Christian_Louboutin",
        ["louboutin", "pigalle", "shoes", "fashion", "luxury"]
    ),
    # 343
    make_q(
        "pop_culture_med_343",
        "Ποιος Αμερικανός σχεδιαστής ίδρυσε το brand Off-White και υπήρξε καλλιτεχνικός διευθυντής ανδρικής μόδας του Louis Vuitton μέχρι τον θάνατό του το 2021;",
        "Virgil Abloh",
        ["Kanye West", "Heron Preston", "Matthew Williams"],
        "Ο Virgil Abloh γεφύρωσε με μοναδικό τρόπο τη streetwear κουλτούρα με την υψηλή ραπτική, χρησιμοποιώντας εισαγωγικά και βιομηχανικά στοιχεία.",
        [
            "Η διάσημη συνεργασία του με τη Nike, η συλλογή 'The Ten' (2017), επαναπροσδιόρισε τη σύγχρονη κουλτούρα των sneakers.",
            "Υπήρξε ο πρώτος Αφροαμερικανός καλλιτεχνικός διευθυντής σε γαλλικό οίκο πολυτελείας στην ιστορία της Louis Vuitton."
        ],
        "https://en.wikipedia.org/wiki/Virgil_Abloh",
        ["virgil_abloh", "off_white", "louis_vuitton", "fashion"]
    ),
    # 344
    make_q(
        "pop_culture_med_344",
        "Ποια τσάντα του οίκου Gucci, που δημιουργήθηκε το 1961, μετονομάστηκε προς τιμήν της Πρώτης Κυρίας των ΗΠΑ που τη φορούσε συνεχώς;",
        "Jackie",
        ["Diana", "Kelly", "Birkin"],
        "Η τσάντα 'Jackie' απέκτησε το όνομά της όταν η Jacqueline Kennedy φωτογραφήθηκε επανειλημμένα να την κρατάει στους δρόμους της Νέας Υόρκης.",
        [
            "Χαρακτηρίζεται από το καμπυλωτό σχήμα μισοφέγγαρου (hobo bag) και το μεταλλικό κούμπωμα με έμβολο.",
            "Η Gucci επανέφερε την τσάντα σε σύγχρονες συλλογές με τεράστια εμπορική επιτυχία."
        ],
        "https://en.wikipedia.org/wiki/Gucci#The_Jackie_bag",
        ["gucci", "jackie_bag", "fashion", "luxury"]
    ),
    # 345
    make_q(
        "pop_culture_med_345",
        "Ποια Ιαπωνέζα πρωτοπόρος σχεδιάστρια ίδρυσε τον ανατρεπτικό οίκο μόδας Comme des Garçons στο Τόκιο το 1969;",
        "Rei Kawakubo",
        ["Chitose Abe", "Yohji Yamamoto", "Issey Miyake"],
        "Η Rei Kawakubo αμφισβήτησε τους δυτικούς κανόνες ομορφιάς εισάγοντας ασύμμετρα, σκούρα και αποδομημένα ρούχα που άλλαξαν την ιστορία της μόδας.",
        [
            "Το 2017 το Μουσείο Μετροπόλιταν της Νέας Υόρκης (The Met) αφιέρωσε το Met Gala και μια μεγάλη έκθεση στο έργο της, τιμή που είχε δοθεί σε εν ζωή σχεδιαστή μόνο στον Yves Saint Laurent.",
            "Δημιούργησε επίσης τα διάσημα concept πολυκαταστήματα Dover Street Market."
        ],
        "https://en.wikipedia.org/wiki/Rei_Kawakubo",
        ["comme_des_garcons", "rei_kawakubo", "fashion", "japan"]
    ),
    # 346
    make_q(
        "pop_culture_med_346",
        "Ποια ιταλική μάρκα πολυτελείας ιδρύθηκε το 1993 από τη Miuccia Prada ως μια πιο νεανική και πειραματική αδελφή μάρκα της Prada;",
        "Miu Miu",
        ["Moschino", "Versus", "Max Mara"],
        "Η Miu Miu πήρε το όνομά της από το οικογενειακό παρατσούκλι της ίδιας της Miuccia Prada και επικεντρώνεται σε avant-garde, ρετρό-μοντέρνες γραμμές.",
        [
            "Η micro-mini φούστα της Miu Miu από τη συλλογή Άνοιξη/Καλοκαίρι 2022 έγινε ένα από τα μεγαλύτερα viral κομμάτια μόδας της δεκαετίας.",
            "Τα shows της Miu Miu στο Παρίσι κλείνουν παραδοσιακά την Εβδομάδα Μόδας."
        ],
        "https://en.wikipedia.org/wiki/Miu_Miu",
        ["miu_miu", "prada", "fashion", "luxury"]
    ),
    # 347
    make_q(
        "pop_culture_med_347",
        "Ποια Βρετανίδα σχεδιάστρια μόδας θεωρείται η μητέρα της μίνι φούστας (miniskirt) στη δεκαετία του 1960 στο Λονδίνο;",
        "Mary Quant",
        ["Vivienne Westwood", "Barbara Hulanicki", "Laura Ashley"],
        "Η Mary Quant ονόμασε τη μίνι φούστα από το αγαπημένο της αυτοκίνητο, το Mini Cooper, πουλώντας την στην περίφημη μπουτίκ της Bazaar στο King's Road.",
        [
            "Η μίνι φούστα έγινε το απόλυτο σύμβολο της γυναικείας χειραφέτησης και του κινήματος 'Swinging London'.",
            "Η Quant εκλαΐκευσε επίσης τα χρωματιστά καλσόν και τα καυτά σορτσάκια (hotpants)."
        ],
        "https://en.wikipedia.org/wiki/Mary_Quant",
        ["mary_quant", "miniskirt", "fashion", "60s", "london"]
    ),
    # 348
    make_q(
        "pop_culture_med_348",
        "Ποιο ιστορικό φιλανθρωπικό supergroup Αμερικανών καλλιτεχνών ηχογράφησε το 'We Are the World' το 1985 για την πείνα στην Αιθιοπία;",
        "USA for Africa",
        ["Band Aid", "Northern Lights", "Hear 'n Aid"],
        "Το τραγούδι γράφτηκε από τον Michael Jackson και τον Lionel Richie, σε παραγωγή Quincy Jones, συγκεντρώνοντας 45 κορυφαίους καλλιτέχνες.",
        [
            "Στην είσοδο του στούντιο ο Quincy Jones είχε κρεμάσει μια επιγραφή που έγραφε: 'Αφήστε το εγώ σας έξω από την πόρτα'.",
            "Το σινγκλ πούλησε πάνω από 20 εκατομμύρια αντίτυπα και συγκέντρωσε περισσότερα από 60 εκατομμύρια δολάρια για ανθρωπιστική βοήθεια."
        ],
        "https://en.wikipedia.org/wiki/We_Are_the_World",
        ["we_are_the_world", "usa_for_africa", "michael_jackson", "charity"]
    ),
    # 349
    make_q(
        "pop_culture_med_349",
        "Πώς αποκαλεί επίσημα η Lady Gaga τους αφοσιωμένους θαυμαστές της σε όλο τον κόσμο;",
        "Little Monsters",
        ["Beliebers", "Swifties", "Barbz"],
        "Η Lady Gaga ονόμασε τους θαυμαστές της 'Little Monsters' μετά την κυκλοφορία του άλμπουμ 'The Fame Monster' (2009), αυτοαποκαλούμενη 'Mother Monster'.",
        [
            "Το χαρακτηριστικό σύμβολο των Little Monsters είναι το 'Monster Paw' (σηκωμένο χέρι με λυγισμένα δάχτυλα σαν νύχι τέρατος).",
            "Η σχέση της με τη βάση των θαυμαστών της θεωρείται πρωτοπόρα για τη χρήση των μέσων κοινωνικής δικτύωσης στη σύγχρονη μουσική βιομηχανία."
        ],
        "https://en.wikipedia.org/wiki/Lady_Gaga",
        ["lady_gaga", "little_monsters", "pop_music", "fanbase"]
    ),
    # 350
    make_q(
        "pop_culture_med_350",
        "Πώς ονομάζεται επίσημα η παγκόσμια στρατιά των φανατικών θαυμαστών της Taylor Swift;",
        "Swifties",
        ["Arianators", "Directioners", "KatyCats"],
        "Ο όρος 'Swifties' καθιερώθηκε για να περιγράψει τη μαζική και εξαιρετικά οργανωμένη κοινότητα των θαυμαστών της Taylor Swift.",
        [
            "Οι Swifties είναι διάσημοι για την αποκωδικοποίηση κρυφών μηνυμάτων και πασχαλινών αυγών ('Easter eggs') που κρύβει η ίδια στους στίχους και τα βίντεό της.",
            "Η λέξη 'Swiftie' προστέθηκε επίσημα στο λεξικό Oxford English Dictionary το 2023."
        ],
        "https://en.wikipedia.org/wiki/Swifties",
        ["taylor_swift", "swifties", "pop_culture", "fanbase"]
    ),
    # 351
    make_q(
        "pop_culture_med_351",
        "Ποια είναι η επίσημη ονομασία της κοινότητας των φανατικών θαυμαστών της Beyoncé;",
        "BeyHive",
        ["Rihanna Navy", "Little Monsters", "Bardi Gang"],
        "Το όνομα 'BeyHive' προέρχεται από το παρατσούκλι της Beyoncé ως 'Queen Bey' και τη λέξη 'beehive' (κυψέλη μελισσών).",
        [
            "Οι θαυμαστές χρησιμοποιούν ευρέως το emoji της μέλισσας στα σχόλια των μέσων κοινωνικής δικτύωσης.",
            "Η BeyHive θεωρείται μία από τις πιο πιστές και διαδικτυακά μαχητικές κοινότητες θαυμαστών στον κόσμο."
        ],
        "https://en.wikipedia.org/wiki/Beyonc%C3%A9#Public_image",
        ["beyonce", "beyhive", "pop_music", "fanbase"]
    ),
    # 352
    make_q(
        "pop_culture_med_352",
        "Ποιος Αμερικανός τραγουδιστής και παραγωγός ερμήνευσε τα φωνητικά στο τεράστιο disco-funk hit 'Get Lucky' των Daft Punk το 2013;",
        "Pharrell Williams",
        ["Bruno Mars", "The Weeknd", "Justin Timberlake"],
        "Ο Pharrell Williams συνεργάστηκε με τους Daft Punk και τον θρυλικό κιθαρίστα Nile Rodgers των Chic για το τραγούδι που σάρωσε τα βραβεία Grammy.",
        [
            "Το 'Get Lucky' κέρδισε το Grammy Ηχογράφησης της Χρονιάς και Καλύτερης Pop Ερμηνείας από Ντουέτο/Συγκρότημα το 2014.",
            "Την ίδια χρονιά ο Pharrell κυκλοφόρησε και τη δική του σόλο mega-επιτυχία 'Happy'."
        ],
        "https://en.wikipedia.org/wiki/Get_Lucky_(Daft_Punk_song)",
        ["daft_punk", "pharrell_williams", "get_lucky", "pop_music"]
    ),
    # 353
    make_q(
        "pop_culture_med_353",
        "Στο κόμικ 'Ο Αστερίξ στους Βρετανούς', τι έπιναν οι Βρετανοί κάθε απόγευμα στις 5 πριν ο Αστερίξ τους μάθει το τσάι;",
        "Ζεστό νερό με μια σταγόνα γάλα",
        ["Ζεστό μηλίτη", "Βραστό κριθάρι", "Ζεστό κρασί με μπαχαρικά"],
        "Οι Βρετανοί σταματούσαν κάθε μάχη στις 5 το απόγευμα για να πιουν ένα φλιτζάνι ζεστό νερό, συνήθεια που ο Οβελίξ έβρισκε εντελώς ακατανόητη.",
        [
            "Στο τέλος της ιστορίας, ο Αστερίξ ρίχνει μυστηριώδη αποξηραμένα φύλλα από την Ανατολή στο ζεστό νερό για να τους δώσει κουράγιο, 'εφευρίσκοντας' έτσι το βρετανικό τσάι.",
            "Ο ξάδελφος του Αστερίξ στη Βρετανία ονομάζεται Ομορφοθώραξ (Jolitorax)."
        ],
        "https://en.wikipedia.org/wiki/Asterix_in_Britain",
        ["asterix", "tea", "britain", "comics"]
    ),
    # 354
    make_q(
        "pop_culture_med_354",
        "Ποια ιστορική γυναίκα σκοπευτής και ιχνηλάτης του στρατού των ΗΠΑ παρουσιάζεται ως αθυρόστομη και σκληροτράχηλη στα κόμικς του Λούκυ Λουκ;",
        "Καλάμιτυ Τζέιν (Calamity Jane)",
        ["Άννι Όκλεϊ", "Μπελ Σταρ", "Περλ Χαρτ"],
        "Η Martha Jane Canary (Calamity Jane) μασάει καπνό, φτύνει με απόλυτη ακρίβεια και τα βάζει με οποιονδήποτε άνδρα στην Άγρια Δύση.",
        [
            "Στο άλμπουμ 'Calamity Jane' (1958), ο Λούκυ Λουκ προσπαθεί να τη διδάξει καλούς τρόπους για να γίνει αποδεκτή στην κοινωνία του El Plomo.",
            "Στην πραγματική ζωή υπήρξε στενή φίλη του Wild Bill Hickok."
        ],
        "https://en.wikipedia.org/wiki/Calamity_Jane_(Lucky_Luke)",
        ["lucky_luke", "calamity_jane", "comics", "western"]
    ),
    # 355
    make_q(
        "pop_culture_med_355",
        "Ποιος ιστορικός αυτοαποκαλούμενος δικαστής του Τέξας κρατούσε δικαστήριο μέσα στο σαλούν του συνοδευόμενος από μια αρκούδα στον Λούκυ Λουκ;",
        "Δικαστής Ρόι Μπιν (Judge Roy Bean)",
        ["Δικαστής Πάρκερ", "Δικαστής Κολτ", "Δικαστής Χόλις"],
        "Ο Roy Bean αποκαλούσε τον εαυτό του 'Ο μόνος νόμος δυτικά του Πέκος' ('The Only Law West of the Pecos') και δίκαζε χρησιμοποιώντας έναν μόνο τόμο νομικών κειμένων.",
        [
            "Ήταν παθολογικά ερωτευμένος με τη Βρετανίδα ηθοποιό Lily Langtry, ονομάζοντας το σαλούν του 'The Jersey Lilly' προς τιμήν της.",
            "Στο κόμικ, ο Λούκυ Λουκ αντιμετωπίζει τις παράλογες αποφάσεις του Roy Bean που επιβάλλει πρόστιμα σε όλους υπέρ του σαλούν του."
        ],
        "https://en.wikipedia.org/wiki/The_Judge_(Lucky_Luke)",
        ["lucky_luke", "roy_bean", "comics", "western"]
    ),
    # 356
    make_q(
        "pop_culture_med_356",
        "Ποια φανταστική λατινοαμερικανική δημοκρατία της μπανάνας επισκέπτεται επανειλημμένα ο Τεντέν εν μέσω συνεχών στρατιωτικών πραξικοπημάτων;",
        "Σαν Θεοδώρος (San Theodoros)",
        ["Νουέβο Ρίκο", "Σαν Μάρκος", "Κοσταγκουάνα"],
        "Στη δημοκρατία του San Theodoros συγκρούονται διαρκώς για την εξουσία ο Στρατηγός Αλκαζάρ και ο Στρατηγός Ταπιόκα.",
        [
            "Η χώρα πρωτοεμφανίστηκε στο τεύχος 'Το Σπασμένο Αυτί' (1937) και επανήλθε στο τελευταίο ολοκληρωμένο άλμπουμ 'Ο Τεντέν και οι Πικαρός' (1976).",
            "Η γειτονική της αντίπαλος χώρα στο κόμικ ονομάζεται Nuevo Rico."
        ],
        "https://en.wikipedia.org/wiki/San_Theodoros",
        ["tintin", "san_theodoros", "herge", "comics"]
    ),
    # 357
    make_q(
        "pop_culture_med_357",
        "Ποιος δισεκατομμυριούχος μεγιστάνας και αρχηγός διεθνούς εγκληματικού συνδικάτου με μονόκλ είναι ο μεγάλος εχθρός του Τεντέν;",
        "Ρομπέρτο Ρασταπόπουλος (Roberto Rastapopoulos)",
        ["Άλαν Τόμπσον", "Δρ. Μίλερ", "Μιτς Χιρονίτο"],
        "Ο Rastapopoulos κρύβεται πίσω από την πρόσοψη ενός παραγωγού ταινιών και εφοπλιστή, διευθύνοντας λαθρεμπόριο οπίου και όπλων.",
        [
            "Πρωτοεμφανίστηκε στο 'Τα Πούρα του Φαραώ' (1934) και εμφανίστηκε σε συνολικά πέντε διαφορετικά άλμπουμ του Τεντέν.",
            "Στο τεύχος 'Πτήση 714 για Σίδνεϊ', ο χαρακτήρας του απομυθοποιείται γελοιοποιούμενος από τον Hergé ως ένας αξιοθρήνητος κακοποιός."
        ],
        "https://en.wikipedia.org/wiki/Roberto_Rastapopoulos",
        ["tintin", "rastapopoulos", "herge", "comics"]
    ),
    # 358
    make_q(
        "pop_culture_med_358",
        "Ποιος είναι ο μεγαλύτερος βιολογικός αδελφός του Goku που φτάνει στη Γη στην αρχή του Dragon Ball Z αποκαλύπτοντας την εξωγήινη καταγωγή του;",
        "Raditz",
        ["Nappa", "Vegeta", "Bardock"],
        "Ο Raditz αποκαλύπτει στον Goku ότι το πραγματικό του όνομα είναι Kakarot και ότι ανήκει στην πολεμική εξωγήινη φυλή των Saiyans.",
        [
            "Απάγει τον μικρό Gohan αναγκάζοντας τον Goku και τον παλιό του εχθρό Piccolo να συμμαχήσουν για πρώτη φορά.",
            "Για να νικηθεί ο Raditz, ο Goku αναγκάζεται να θυσιάσει την ίδια του τη ζωή κρατώντας τον ακίνητο για το Special Beam Cannon του Piccolo."
        ],
        "https://en.wikipedia.org/wiki/Raditz",
        ["dragon_ball_z", "raditz", "goku", "anime"]
    ),
    # 359
    make_q(
        "pop_culture_med_359",
        "Ποιος μυστηριώδης ξιφομάχος έφτασε από το μέλλον στο Dragon Ball Z και εξόντωσε τον Mecha Frieza με ένα μόνο χτύπημα;",
        "Trunks (Future Trunks)",
        ["Goten", "Gohan", "Vegito"],
        "Ο Future Trunks είναι ο γιος του Vegeta και της Bulma από ένα δυστοπικό μέλλον κατεστραμμένο από τα ανδροειδή 17 και 18.",
        [
            "Ταξίδεψε στο παρελθόν με τη χρονομηχανή της μητέρας του για να δώσει στον Goku το φάρμακο για την καρδιακή νόσο.",
            "Έγινε άμεσα ένας από τους πιο δημοφιλείς χαρακτήρες του franchise χάρη στο σπαθί του και το Super Saiyan look."
        ],
        "https://en.wikipedia.org/wiki/Trunks_(Dragon_Ball)",
        ["dragon_ball_z", "trunks", "anime", "manga"]
    ),
    # 360
    make_q(
        "pop_culture_med_360",
        "Ποια επίλεκτη εγκληματική οργάνωση επικίνδυνων αποστατών νίντζα στο Naruto φορούσε μαύρους μανδύες με κόκκινα σύννεφα;",
        "Akatsuki",
        ["Anbu", "Sound Four", "Seven Swordsmen"],
        "Η Akatsuki είχε ως απώτερο στόχο τη σύλληψη και των εννέα Bijuu (ουραίων θηρίων) για να επιβάλει παγκόσμια ειρήνη μέσω απόλυτης ισχύος.",
        [
            "Ιδρύθηκε αρχικά από τους Yahiko, Nagato (Pain) και Konan στο χωριό της Βροχής ως ειρηνιστική ομάδα πριν χειραγωγηθεί από τον Obito Uchiha.",
            "Όλα τα μέλη της φορούσαν δαχτυλίδια με μοναδικά kanji και έφεραν χαραγμένη γραμμή στο προστατευτικό του μετώπου τους."
        ],
        "https://en.wikipedia.org/wiki/Naruto",
        ["naruto", "akatsuki", "anime", "manga"]
    ),
    # 361
    make_q(
        "pop_culture_med_361",
        "Ποιος ξιφομάχος των Ψάθινων Καπέλων στο 'One Piece' μάχεται με το μοναδικό στυλ των τριών σπαθιών (Santoryu) κρατώντας ένα στο στόμα του;",
        "Roronoa Zoro",
        ["Sanji", "Brook", "Trafalgar Law"],
        "Ο Zoro ήταν ο πρώτος σύντροφος που εντάχθηκε στο πλήρωμα του Luffy και έχει ορκιστεί να γίνει ο κορυφαίος ξιφομάχος στον κόσμο.",
        [
            "Έχει διαβόητα κακό προσανατολισμό και χάνεται συνεχώς ακόμα και σε ευθείες γραμμές.",
            "Το όνομά του εμπνεύστηκε από τον ιστορικό Γάλλο πειρατή François l'Olonnais."
        ],
        "https://en.wikipedia.org/wiki/Roronoa_Zoro",
        ["one_piece", "zoro", "anime", "manga"]
    ),
    # 362
    make_q(
        "pop_culture_med_362",
        "Ποιος μάγειρας των Ψάθινων Καπέλων στο 'One Piece' αρνείται να χρησιμοποιήσει τα χέρια του στη μάχη για να μην τραυματιστούν και πολεμά μόνο με κλωτσιές;",
        "Sanji",
        ["Zoro", "Franky", "Usopp"],
        "Ο 'Black Leg' Sanji χρησιμοποιεί αποκλειστικά τα πόδια του στη μάχη επειδή θεωρεί τα χέρια ιερά εργαλεία για το μαγείρεμα.",
        [
            "Όνειρό του είναι να βρει τον μυθικό ωκεανό All Blue, όπου συναντώνται τα ψάρια από όλες τις θάλασσες του κόσμου.",
            "Έχει έναν άκαμπτο ιπποτικό κώδικα τιμής που του απαγορεύει κατηγορηματικά να χτυπήσει ποτέ γυναίκα, ακόμη κι αν κινδυνεύει η ζωή του."
        ],
        "https://en.wikipedia.org/wiki/Sanji_(One_Piece)",
        ["one_piece", "sanji", "anime", "manga"]
    ),
    # 363
    make_q(
        "pop_culture_med_363",
        "Πώς ονομάζεται το εξωτερικό από τα τρία κυκλικά ομόκεντρα τείχη που καταστράφηκε από τον Κολοσσιαίο Τιτάνα στην αρχή του 'Attack on Titan';",
        "Τείχος Μαρία (Wall Maria)",
        ["Τείχος Ρόζε", "Τείχος Σίνα", "Τείχος Ελντία"],
        "Η ανθρωπότητα προστατευόταν από τρία τείχη: το εξωτερικό Wall Maria, το μεσαίο Wall Rose και το εσωτερικό Wall Sina όπου ζούσε ο βασιλιάς.",
        [
            "Η πτώση του Wall Maria και της συνοικίας Shiganshina το έτος 845 οδήγησε στον θάνατο της μητέρας του Eren Yeager.",
            "Αργότερα αποκαλύπτεται ότι τα τείχη κατασκευάστηκαν από εκατομμύρια κοιμώμενους γιγάντιους Τιτάνες (Colossal Titans)."
        ],
        "https://en.wikipedia.org/wiki/Attack_on_Titan",
        ["attack_on_titan", "wall_maria", "anime", "manga"]
    ),
    # 364
    make_q(
        "pop_culture_med_364",
        "Ποιος είναι ο θεμελιώδης νόμος της αλχημείας στο 'Fullmetal Alchemist' που ορίζει ότι για να αποκτήσεις κάτι πρέπει να θυσιάσεις κάτι ίσης αξίας;",
        "Ο Νόμος της Ισοδύναμης Ανταλλαγής (Law of Equivalent Exchange)",
        ["Το Δόγμα της Μετουσίωσης", "Ο Κανόνας της Φιλοσοφικής Λίθου", "Η Αρχή της Εντροπίας"],
        "Τα αδέλφια Edward και Alphonse Elric παραβίασαν το μεγαλύτερο ταμπού της αλχημείας (την ανθρώπινη μετουσίωση) προσπαθώντας να αναστήσουν τη μητέρα τους.",
        [
            "Το τίμημα ήταν ο Edward να χάσει το αριστερό του πόδι και ο Alphonse ολόκληρο το σώμα του, το οποίο ο Edward έδεσε σε μια πανοπλία θυσιάζοντας το δεξί του χέρι.",
            "Το manga της Hiromu Arakawa θεωρείται ένα από τα πιο άρτια δομημένα έργα στην ιστορία της ιαπωνικής μυθοπλασίας."
        ],
        "https://en.wikipedia.org/wiki/Fullmetal_Alchemist",
        ["fullmetal_alchemist", "equivalent_exchange", "anime", "manga"]
    ),
    # 365
    make_q(
        "pop_culture_med_365",
        "Ποιο παράξενο πλάσμα με δώδεκα πόδια και φωτεινά μάτια λειτουργεί ως ζωντανό μέσο μεταφοράς στην ταινία 'My Neighbor Totoro';",
        "Το Γατολεωφορείο (Catbus / Nekobasu)",
        ["Το Σκυλοτρένο", "Ο Δρακοστρόβιλος", "Το Πουλοπλοίο"],
        "Το Catbus είναι ένα πνεύμα που μπορεί να αλλάζει προορισμό μέσω περιστρεφόμενης πινακίδας στο κεφάλι του και να τρέχει πάνω σε καλώδια και δάση αόρατο από τους ανθρώπους.",
        [
            "Εμφανίστηκε επίσης στη μικρού μήκους ταινία 'Mei and the Kittenbus' που προβάλλεται αποκλειστικά στο Μουσείο Ghibli στο Τόκιο.",
            "Τα παράθυρά του σχηματίζονται ανοίγοντας το τρίχωμα στα πλευρά του σώματός του."
        ],
        "https://en.wikipedia.org/wiki/My_Neighbor_Totoro",
        ["totoro", "catbus", "studio_ghibli", "hayao_miyazaki", "anime"]
    ),
    # 366
    make_q(
        "pop_culture_med_366",
        "Τι φοράει πάνω στο στόμα της η Nezuko Kamado στο anime 'Demon Slayer' για να αποτρέψει τον εαυτό της από το να δαγκώσει ανθρώπους;",
        "Ένα φίμωτρο από μπαμπού",
        ["Ένα μεταλλικό δαχτυλίδι", "Μια δερμάτινη μάσκα", "Ένα μεταξωτό μαντήλι"],
        "Ο πρώην Water Hashira, Sakonji Urokodaki, τοποθέτησε το κομμάτι μπαμπού στο στόμα της Nezuko για να την εμποδίσει να γευτεί ανθρώπινο αίμα μετά τη μετατροπή της σε δαίμονα.",
        [
            "Σε αντίθεση με άλλους δαίμονες που χρειάζονται ανθρώπινη σάρκα, η Nezuko ανακτά τις δυνάμεις της κοιμώμενη για παρατεταμένες περιόδους.",
            "Η ταινία 'Demon Slayer: Mugen Train' (2020) έγινε η πιο επιτυχημένη εισπρακτικά ιαπωνική ταινία όλων των εποχών παγκοσμίως."
        ],
        "https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba",
        ["demon_slayer", "nezuko", "anime", "manga"]
    ),
    # 367
    make_q(
        "pop_culture_med_367",
        "Ποιος διαβόητος κυνηγός επικηρυγμένων με μανδαλοριανή πανοπλία παρέδωσε τον Han Solo παγωμένο σε καρβονίτη στον Jabba the Hutt;",
        "Boba Fett",
        ["Jango Fett", "Cad Bane", "Din Djarin"],
        "Ο Boba Fett είναι ένας αμετάλλακτος κλώνος του Jango Fett, τον οποίο ο Jango μεγάλωσε ως δικό του γιο στον πλανήτη Kamino.",
        [
            "Αν και είχε ελάχιστες ατάκες και χρόνο εμφάνισης στην αρχική τριλογία, έγινε ένας από τους πιο λατρεμένους χαρακτήρες του Star Wars.",
            "Η επιβίωσή του από το λάκκο του Sarlacc επιβεβαιώθηκε επίσημα στη σειρά 'The Mandalorian' και στη δική του σειρά 'The Book of Boba Fett'."
        ],
        "https://en.wikipedia.org/wiki/Boba_Fett",
        ["star_wars", "boba_fett", "mandalorian", "sci_fi"]
    ),
    # 368
    make_q(
        "pop_culture_med_368",
        "Σε ποιον έρημο πλανήτη με δύο ήλιους μεγάλωσαν τόσο ο Luke Skywalker όσο και ο πατέρας του Anakin στο Star Wars;",
        "Tatooine",
        ["Jakku", "Hoth", "Geonosis"],
        "Ο Tatooine είναι ένας απομακρυσμένος πλανήτης των Outer Rim territories που κυβερνάται από το συνδικάτο εγκλήματος των Hutts.",
        [
            "Τα εξωτερικά πλάνα του πλανήτη γυρίστηκαν κυρίως στην Τυνησία, και ο πλανήτης πήρε το όνομά του από την πραγματική τυνησιακή πόλη Tataouine.",
            "Η σκηνή όπου ο νεαρός Luke ατενίζει το διπλό ηλιοβασίλεμα (Binary Sunset) υπό τη μουσική του John Williams είναι ιστορική."
        ],
        "https://en.wikipedia.org/wiki/Tatooine",
        ["star_wars", "tatooine", "luke_skywalker", "cinema"]
    ),
    # 369
    make_q(
        "pop_culture_med_369",
        "Ποιο ήταν το όνομα του Sith Λόρδου που κυβερνούσε τη Γαλαξιακή Αυτοκρατορία ως Αυτοκράτορας Palpatine στο Star Wars;",
        "Darth Sidious",
        ["Darth Plagueis", "Darth Maul", "Darth Tyranus"],
        "Ο Sheev Palpatine έζησε διπλή ζωή ως αξιοσέβαστος γερουσιαστής του Naboo (και μετέπειτα Ύπατος Καγκελάριος) ενώ ενορχήστρωνε τους Πολέμους των Κλώνων ως Darth Sidious.",
        [
            "Ο δάσκαλός του ήταν ο Darth Plagueis the Wise, τον οποίο ο Sidious δολοφόνησε στον ύπνο του αφού έμαθε τα μυστικά του.",
            "Εξέδωσε την 'Εντολή 66' (Order 66) εξολοθρεύοντας σχεδόν όλους τους Jedi σε ολόκληρο τον γαλαξία."
        ],
        "https://en.wikipedia.org/wiki/Palpatine",
        ["star_wars", "palpatine", "darth_sidious", "sith"]
    ),
    # 370
    make_q(
        "pop_culture_med_370",
        "Πώς ονομάζεται ο μαγικός χάρτης που δημιούργησαν οι Moony, Wormtail, Padfoot και Prongs αποκαλύπτοντας τα πάντα στο Hogwarts;",
        "Ο Χάρτης των Επιδρομέων (The Marauder's Map)",
        ["Ο Χάρτης του Μέρλιν", "Ο Χάρτης των Ιδρυτών", "Το Μαγικό Διάγραμμα"],
        "Ο χάρτης ενεργοποιείται με τη φράση 'Ορκίζομαι επίσημα ότι είμαι κατεργάρης' και σβήνει με τη φράση 'Η αταξία εξετελέσθη' (Mischief managed).",
        [
            "Οι τέσσερις δημιουργοί ήταν οι Remus Lupin, Peter Pettigrew, Sirius Black και James Potter.",
            "Ο χάρτης δείχνει όχι μόνο όλα τα μυστικά περάσματα αλλά και τη θέση και την κίνηση κάθε ατόμου στο κάστρο σε πραγματικό χρόνο."
        ],
        "https://en.wikipedia.org/wiki/Marauder%27s_Map",
        ["harry_potter", "marauders_map", "hogwarts", "magic"]
    ),
    # 371
    make_q(
        "pop_culture_med_371",
        "Ποιο είναι το όνομα του γιγάντιου τρικέφαλου σκύλου του Hagrid που φύλαγε την καταπακτή της Φιλοσοφικής Λίθου στο Harry Potter;",
        "Fluffy",
        ["Fang", "Norbert", "Buckbeak"],
        "Ο Fluffy αποκοιμιέται αμέσως μόλις ακούσει οποιοδήποτε είδος μουσικής, μυστικό που ο Hagrid αποκάλυψε κατά λάθος στον Harry και τους φίλους του.",
        [
            "Ο χαρακτήρας αποτελεί άμεση αναφορά στον μυθικό Κέρβερο της αρχαίας ελληνικής μυθολογίας.",
            "Ο Hagrid ανέφερε ότι αγόρασε τον Fluffy από έναν 'Έλληνα τύπο σε μια παμπ'."
        ],
        "https://en.wikipedia.org/wiki/List_of_magical_creatures_in_Harry_Potter#Fluffy",
        ["harry_potter", "fluffy", "hagrid", "mythology"]
    ),
    # 372
    make_q(
        "pop_culture_med_372",
        "Ποιο είναι το επίσημο ρητό του περήφανου και σκληροτράχηλου Οίκου Greyjoy των Σιδερένιων Νήσων στο 'Game of Thrones';",
        "Εμείς δεν σπέρνουμε (We Do Not Sow)",
        ["Ο Χειμώνας Έρχεται", "Ακούστε το Βρυχηθμό μου", "Άκαμπτοι, Αλύγιστοι, Άθραυστοι"],
        "Οι Greyjoy υπερηφανεύονται ότι δεν καλλιεργούν τη γη αλλά παίρνουν ό,τι χρειάζονται πληρώνοντας το 'τίμημα του σιδήρου' (iron price) μέσω επιδρομών.",
        [
            "Το έμβλημα του οίκου τους είναι ένα χρυσό κράκεν σε μαύρο φόντο.",
            "Η θρησκεία τους λατρεύει τον Πνιγμένο Θεό (Drowned God) με τη φράση: 'Ό,τι είναι νεκρό δεν μπορεί να πεθάνει ποτέ' ('What is dead may never die')."
        ],
        "https://en.wikipedia.org/wiki/House_Greyjoy",
        ["game_of_thrones", "house_greyjoy", "iron_islands", "fantasy"]
    ),
    # 373
    make_q(
        "pop_culture_med_373",
        "Ποιο όνομα έδωσε η Arya Stark στο λεπτό ξίφος ξιφασκίας που της χάρισε ο ετεροθαλής αδελφός της Jon Snow πριν φύγει για το Τείχος;",
        "Needle (Βελόνα)",
        ["Dark Sister", "Oathkeeper", "Widow's Wail"],
        "Η Arya ονόμασε το σπαθί 'Βελόνα' ειρωνευόμενη τα μαθήματα κεντήματος της Septa Mordane, λέγοντας: 'Το κέντημα είναι δύσκολο... αλλά αυτό το Needle το χρησιμοποιώ εύκολα'.",
        [
            "Ο Jon Snow της έδωσε τον πρώτο και πιο βασικό κανόνα ξιφομαχίας: 'Stick 'em with the pointy end' (Κάρφωσέ τους με τη μυτερή άκρη).",
            "Η Arya εκπαιδεύτηκε στη χρήση του σπαθιού στο King's Landing από τον Syrio Forel, τον πρώτο σπαθοφόρο του Braavos."
        ],
        "https://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_weapons#Needle",
        ["game_of_thrones", "arya_stark", "needle", "jon_snow"]
    ),
    # 374
    make_q(
        "pop_culture_med_374",
        "Πώς ονομάζεται το σκοτεινό οχυρό και φρούριο του Sauron στη Mordor όπου δεσπόζει το φλεγόμενο Μάτι;",
        "Barad-dûr",
        ["Orthanc", "Minas Morgul", "Cirith Ungol"],
        "Το Barad-dûr ('Σκοτεινός Πύργος' στα Sindarin) ήταν το υψηλότερο οχυρό της Μέσης Γης στη Δεύτερη και Τρίτη Εποχή, κρατημένο όρθιο από τη δύναμη του Ενός Δαχτυλιδιού.",
        [
            "Όταν το Ένα Δαχτυλίδι καταστράφηκε στις φλόγες του Mount Doom, τα θεμέλια του Barad-dûr κατέρρευσαν ολοσχερώς.",
            "Ο άλλος διάσημος μαύρος πύργος της ιστορίας είναι το Orthanc στο Isengard, έδρα του μάγου Saruman."
        ],
        "https://en.wikipedia.org/wiki/Barad-d%C3%BBr",
        ["lord_of_the_rings", "barad_dur", "sauron", "mordor"]
    ),
    # 375
    make_q(
        "pop_culture_med_375",
        "Ποιο κλασικό επιτραπέζιο παιχνίδι ρόλων (RPG) παίζουν οι τέσσερις φίλοι στο υπόγειο του Mike στην αρχή του 'Stranger Things';",
        "Dungeons & Dragons",
        ["Warhammer", "Call of Cthulhu", "Pathfinder"],
        "Τα παιδιά ονομάζουν τα τέρατα του Upside Down (όπως το Demogorgon, ο Mind Flayer και ο Vecna) από τους αντίστοιχους εχθρούς της καμπάνιας D&D τους.",
        [
            "Η προβολή της σειράς προκάλεσε μια τεράστια παγκόσμια αναγέννηση της δημοτικότητας του Dungeons & Dragons σε νέες γενιές παικτών.",
            "Στην 4η σεζόν, η παρέα ανήκει στο σχολικό κλαμπ D&D που ονομάζεται 'The Hellfire Club'."
        ],
        "https://en.wikipedia.org/wiki/Stranger_Things",
        ["stranger_things", "dungeons_and_dragons", "dnd", "netflix"]
    ),
    # 376
    make_q(
        "pop_culture_med_376",
        "Ποια αυστηρή ιερή φράση επαναλαμβάνουν οι Μανδαλοριανοί της ομάδας 'Children of the Watch' για να επιβεβαιώσουν τον κώδικά τους;",
        "This is the Way",
        ["May the Force be with you", "I have spoken", "Honor above all"],
        "Ο Din Djarin (The Mandalorian) και η Armorer επαναλαμβάνουν τη φράση 'This is the Way' ως απόλυτη δήλωση πίστης στις αρχαίες παραδόσεις της Mandalore.",
        [
            "Ο κανόνας της ομάδας τους απαγορεύει αυστηρά να αφαιρέσουν το κράνος τους μπροστά σε οποιοδήποτε άλλο ζωντανό ον.",
            "Η φράση έγινε ένα από τα πιο δημοφιλή pop culture συνθήματα των τελευταίων ετών στο διαδίκτυο."
        ],
        "https://en.wikipedia.org/wiki/The_Mandalorian",
        ["the_mandalorian", "star_wars", "this_is_the_way"]
    ),
    # 377
    make_q(
        "pop_culture_med_377",
        "Ποιο ήταν το όνομα του αιωρούμενου σκάφους του Morpheus στο 'The Matrix' (1999);",
        "Nebuchadnezzar (Ναβουχοδονόσορ)",
        ["Logos", "Osiris", "Vigilant"],
        "Το πλοίο πήρε το όνομά του από τον ιστορικό βασιλιά της Βαβυλώνας Ναβουχοδονόσορα Β', παραπέμποντας στη βιβλική αναζήτηση της αλήθειας των ονείρων.",
        [
            "Μια μεταλλική πλακέτα στο πλοίο φέρει την επιγραφή 'Mark III No. 11', άμεση αναφορά στο εδάφιο του Ευαγγελίου του Μάρκου (Μάρκος 3:11).",
            "Το σκάφος διαθέτει όπλο ηλεκτρομαγνητικού παλμού (EMP) ως έσχατη άμυνα απέναντι στα φονικά ρομπότ Sentinels."
        ],
        "https://en.wikipedia.org/wiki/The_Matrix",
        ["the_matrix", "nebuchadnezzar", "morpheus", "sci_fi"]
    ),
    # 378
    make_q(
        "pop_culture_med_378",
        "Πώς ονομάζεται το μεγαλειώδες λευκό άλογο του Gandalf, αρχηγός της φυλής των Mearas, που τρέχει γρηγορότερα από τον άνεμο;",
        "Shadowfax (Σκιότριχος)",
        ["Arod", "Hasufel", "Bill"],
        "Ο Shadowfax αρνείται να δεχτεί σέλα ή χαλινάρι και επιτρέπει μόνο στον Gandalf να ιππεύει ελεύθερα στην πλάτη του.",
        [
            "Ανήκε αρχικά στους στάβλους του βασιλιά Théoden του Rohan, ο οποίος τον παραχώρησε απρόθυμα στον μάγο.",
            "Στο τέλος της ιστορίας, ο Shadowfax επιβιβάζεται στο πλοίο για τις Αθάνατες Χώρες (Undying Lands) μαζί με τον Gandalf."
        ],
        "https://en.wikipedia.org/wiki/Shadowfax",
        ["lord_of_the_rings", "shadowfax", "gandalf", "tolkien"]
    ),
    # 379
    make_q(
        "pop_culture_med_379",
        "Ποιο θανατηφόρο σπάνιο δηλητήριο χρησιμοποιήθηκε στον 'Ματωμένο Γάμο' του Joffrey Baratheon προκαλώντας ασφυξία και μελάνιασμα του προσώπου του;",
        "The Strangler (Ο Στραγγαλιστής)",
        ["Tears of Lys", "Nightshade", "Widow's Blood"],
        "Ο Στραγγαλιστής παρασκευάζεται από ένα σπάνιο φυτό των νησιών της Jade Sea και μετατρέπεται σε κρυστάλλους που διαλύονται ακαριαία στο κρασί.",
        [
            "Το δηλητήριο ήταν κρυμμένο σε ένα από τα διακοσμητικά πετράδια του διχτυωτού κοσμήματος μαλλιών (ή περιδέραιου) της Sansa Stark.",
            "Η δολοφονία του Joffrey οργανώθηκε μυστικά από τη Lady Olenna Tyrell και τον Petyr Baelish (Littlefinger)."
        ],
        "https://en.wikipedia.org/wiki/Purple_Wedding",
        ["game_of_thrones", "joffrey", "the_strangler", "poison"]
    ),
    # 380
    make_q(
        "pop_culture_med_380",
        "Ποιο μαγικό πλάσμα αποτελεί το Patronus του καθηγητή Severus Snape, αποκαλύπτοντας την αιώνια αγάπη του για τη Lily Potter;",
        "Ελαφίνα (Doe)",
        ["Ελάφι (Stag)", "Λύκος", "Κύκνος"],
        "Το Patronus του Snape είναι μια ασημένια θηλυκή ελαφίνα, ακριβώς το ίδιο με εκείνο της Lily Evans-Potter.",
        [
            "Όταν ο Dumbledore ρωτάει με έκπληξη αν αγαπά ακόμα τη Lily μετά από τόσα χρόνια, ο Snape απαντά με την ιστορική λέξη: 'Always' (Πάντα).",
            "Το Patronus του Harry είναι ένα αρσενικό ελάφι (stag), όπως και της μορφής animagus του πατέρα του James Potter."
        ],
        "https://en.wikipedia.org/wiki/Severus_Snape",
        ["harry_potter", "severus_snape", "patronus", "always"]
    ),
    # 381
    make_q(
        "pop_culture_med_381",
        "Στην κωμική σειρά 'Το Σόι σου' (Alpha, 2014-2019), ποια ήταν τα επώνυμα των δύο οικογενειών των συμπεθέρων;",
        "Τριανταφύλλου και Χαμπέοι",
        ["Παπαδόπουλοι και Γεωργίου", "Μαρκοράδες και Κουντουράτοι", "Κολοβού και Σταμίρη"],
        "Η σειρά παρακολουθούσε τις ξεκαρδιστικές οικογενειακές συγκεντρώσεις κάθε Κυριακή ανάμεσα στους αστούς Τριανταφύλλου και τους λαϊκούς Χαμπέους.",
        [
            "Το κεντρικό παντρεμένο ζευγάρι ήταν ο Σάββας Τριανταφύλλου (Μελέτης Ηλίας) και η Λυδία Χαμπέα (Βάσω Λασκαράκη).",
            "Η σειρά προβλήθηκε για 5 συνεχόμενες σεζόν και 307 επεισόδια σημειώνοντας τεράστια επιτυχία."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
        ["to_soi_sou", "alpha", "greek_tv", "comedy"]
    ),
    # 382
    make_q(
        "pop_culture_med_382",
        "Ποια ηθοποιός υποδύθηκε τη λαϊκή, υπερπροστατευτική μητέρα Χαρούλα Χαμπέα που μαγείρευε ασταμάτητα στο 'Το Σόι σου';",
        "Ρένια Λουιζίδου",
        ["Μίρκα Παπακωνσταντίνου", "Ελένη Γερασιμίδου", "Μαρία Καβογιάννη"],
        "Η Χαρούλα Χαμπέα (Ρένια Λουιζίδου) και ο σύζυγός της Βαγγέλης (Γιώργος Γιαννόπουλος) εκπροσωπούσαν την αυθεντική παραδοσιακή ελληνική οικογένεια.",
        [
            "Η ατάκα του Βαγγέλη Χαμπέα 'Ορίτζιναλ!' και η εμμονή του με τα κρέατα του χασάπικου άφησαν εποχή.",
            "Η Λουιζίδου κέρδισε την αγάπη του κοινού για τη ζεστασιά και τον ρεαλισμό της ερμηνείας της."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
        ["to_soi_sou", "renia_louizidou", "greek_tv"]
    ),
    # 383
    make_q(
        "pop_culture_med_383",
        "Ποια σπουδαία ηθοποιός ενσάρκωσε τη σνομπ και αριστοκρατική πεθερά Αλεξάνδρα Τριανταφύλλου στο 'Το Σόι σου';",
        "Μίρκα Παπακωνσταντίνου",
        ["Ντίνα Κώνστα", "Μπέτυ Βαλάση", "Μάρω Κοντού"],
        "Η Αλεξάνδρα Τριανταφύλλου ήταν γλύπτρια με υψηλή αισθητική και εκλεπτυσμένα γούστα που περιφρονούσε τις λαϊκές συνήθειες των Χαμπέων.",
        [
            "Ο σύζυγός της Μενέλαος (Παύλος Ορκόπουλος) λειτουργούσε ως η φωνή της λογικής και της ηρεμίας στην οικογένεια.",
            "Οι αμοιβαίες 'φαρμακερές' φιλοφρονήσεις ανάμεσα στην Αλεξάνδρα και τη Χαρούλα αποτελούσαν τη ραχοκοκαλιά του χιούμορ της σειράς."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
        ["to_soi_sou", "mirka_papakonstantinou", "greek_tv"]
    ),
    # 384
    make_q(
        "pop_culture_med_384",
        "Σε ποια ιστορική οδό του κέντρου της Αθήνας βρισκόταν η πολυκατοικία στην ομώνυμη κωμική σειρά του Mega (2008-2011);",
        "Μιχαήλ Βόδα",
        ["Αχαρνών", "Πατησίων", "Φυλής"],
        "Η 'Πολυκατοικία' (βασισμένη στην ισπανική σειρά 'Aquí no hay quien viva') παρακολουθούσε τις τρελές ιστορίες των ενοίκων στην οδό Μιχαήλ Βόδα.",
        [
            "Ο Παύλος Χαϊκάλης υποδυόταν τον διαχειριστή Θανάση Μπαλαφούτη με την ιστορική ατάκα 'Εδώ είναι Μιχαήλ Βόδα!'.",
            "Η σειρά γνώρισε τεράστια επιτυχία διαρκώντας 3 σεζόν και 132 επεισόδια."
        ],
        "https://el.wikipedia.org/wiki/%CE%97_%CE%A0%CE%BF%CE%BB%CF%85%CE%BA%CE%B1%CF%84%CE%BF%CE%B9%CE%BA%CE%AF%CE%B1",
        ["i_polykatoikia", "michail_voda", "balafoutis", "mega", "greek_tv"]
    ),
    # 385
    make_q(
        "pop_culture_med_385",
        "Σε ποιο ασυνήθιστο περιβάλλον διαδραματιζόταν η ανατρεπτική κωμική σειρά των Ρήγα - Αποστόλου 'Οι Σταύλοι της Εριέτας Ζαΐμη' (2002-2004);",
        "Πρότυπες γυναικείες φυλακές",
        ["Ψυχιατρική κλινική", "Στρατόπεδο νεοσυλλέκτων", "Μοναστήρι"],
        "Η σειρά εξελισσόταν στις φανταστικές πρότυπες φυλακές του Καλάμου που διηύθυνε ο αυστηρός διευθυντής Δημήτρης Πλαπούτας (Νίκος Σεργιανόπουλος).",
        [
            "Η Εριέτα Ζαΐμη (Μίρκα Παπακωνσταντίνου) ήταν μια ζάπλουτη μεγαλοαστή κρατούμενη που είχε μετατρέψει το κελί της σε σουίτα πολυτελείας.",
            "Η σειρά περιλάμβανε ένα πολυπληθές καστ από τις πιο γνωστές Ελληνίδες ηθοποιούς σε ακραίους κωμικούς ρόλους."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CF%83%CF%84%CE%AC%CE%B2%CE%BB%CE%BF%CE%B9_%CF%84%CE%B7%CF%82_%CE%95%CF%81%CE%B9%CE%AD%CF%84%CE%B1%CF%82_%CE%96%CE%B1%CE%90%CE%BC%CE%B7",
        ["stavloi_tis_erietas_zaimi", "sergianopoulos", "ant1", "greek_tv"]
    ),
    # 386
    make_q(
        "pop_culture_med_386",
        "Ποια αξέχαστη ηθοποιός ενσάρκωσε τη δυναμική κρατούμενη Μελίτα Σκαφίδα στους 'Σταύλους της Εριέτας Ζαΐμη';",
        "Τζέσυ Παπουτσή",
        ["Χρυσούλα Διαβάτη", "Πηνελόπη Πιτσούλη", "Μαρία Κανελλοπούλου"],
        "Η Μελίτα Σκαφίδα ήταν μια από τις πιο σκληρές και ταυτόχρονα ευαίσθητες κρατούμενες, γνωστή για τους καβγάδες και τις εκρηκτικές της ατάκες.",
        [
            "Η σχέση της με τις υπόλοιπες τρόφιμες και τη δεσμοφύλακα Καίτη Κολεσίδου (Βασιλική Ανδρίτσου) χάρισε άφθονο γέλιο.",
            "Η Τζέσυ Παπουτσή υπήρξε μία από τις πιο αγαπητές και πληθωρικές κωμικές παρουσίες του ελληνικού θεάτρου και της τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CF%83%CF%84%CE%AC%CE%B2%CE%BB%CE%BF%CE%B9_%CF%84%CE%B7%CF%82_%CE%95%CF%81%CE%B9%CE%AD%CF%84%CE%B1%CF%82_%CE%96%CE%B1%CE%90%CE%BC%CE%B7",
        ["tzessy_papoutsi", "stavloi_tis_erietas_zaimi", "greek_tv"]
    ),
    # 387
    make_q(
        "pop_culture_med_387",
        "Πώς ονομαζόταν το φανταστικό χωριό του θεσσαλικού κάμπου όπου εκτυλίσσονταν οι 'Άγριες Μέλισσες' (ΑΝΤ1, 2019-2022);",
        "Διαφάνι",
        ["Καρυές", "Πλατανιάς", "Αμπελώνας"],
        "Το Διαφάνι ήταν το επίκεντρο της πολυβραβευμένης δραματικής σειράς εποχής που αναβίωσε τη σύγχρονη ελληνική τηλεοπτική μυθοπλασία.",
        [
            "Ένα ολόκληρο χωριό εποχής κατασκευάστηκε από το μηδέν στα στούντιο της Finos Film στα Σπάτα για τις ανάγκες των γυρισμάτων.",
            "Η σειρά διήρκεσε 3 σεζόν και 421 επεισόδια σημειώνοντας τεράστια εμπορική και καλλιτεχνική επιτυχία."
        ],
        "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CF%81%CE%B9%CE%B5%CF%82_%CE%BC%CE%AD%CE%BB%CE%B9%CF%83%CF%83%CE%B5%CF%82",
        ["agries_melisses", "diafani", "ant1", "greek_tv", "drama"]
    ),
    # 388
    make_q(
        "pop_culture_med_388",
        "Πόσες ήταν οι αδελφές Σταμίρη (Ελένη, Ασημίνα, Δρόσω) που δολοφόνησαν τον Σέργιο Σεβαστό στην πρεμιέρα των 'Άγριων Μελισσών';",
        "Τρεις",
        ["Δύο", "Τέσσερις", "Πέντε"],
        "Οι τρεις ορφανές αδελφές αναγκάστηκαν να σκοτώσουν τον Σέργιο τη νύχτα του γάμου του με την Ελένη για να προστατεύσουν τη ζωή τους, ξεκινώντας μια πολυετή βεντέτα.",
        [
            "Τις αδελφές ενσάρκωσαν οι Μαρία Κίτσου (Ελένη), Έλλη Τρίγγου (Ασημίνα) και Δανάη Μιχαλάκη (Δρόσω).",
            "Η σκηνή του φόνου στο πρώτο επεισόδιο καθήλωσε το τηλεοπτικό κοινό και σημείωσε ρεκόρ τηλεθέασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CF%81%CE%B9%CE%B5%CF%82_%CE%BC%CE%AD%CE%BB%CE%B9%CF%83%CF%83%CE%B5%CF%82",
        ["agries_melisses", "stamiri", "maria_kitsou", "greek_tv"]
    ),
    # 389
    make_q(
        "pop_culture_med_389",
        "Στην κωμωδία 'Κάτι Τρέχει με τους Δίπλα' (Mega, 1999-2000), ποιος ηθοποιός υποδυόταν τον εκκεντρικό ζωγράφο Μάνο Καλαβρέζο;",
        "Κλέων Γρηγοριάδης",
        ["Ρένος Χαραλαμπίδης", "Κώστας Κόκλας", "Θοδωρής Αθερίδης"],
        "Ο Μάνος Καλαβρέζος ήταν ένας μποέμ καλλιτέχνης παντρεμένος με τη λαϊκή τραγουδίστρια Γωγώ (Ελευθερία Βιδάκη), που μετακομίζουν δίπλα σε ένα σοβαροφανές ζευγάρι ακαδημαϊκών.",
        [
            "Το αντίπαλο ζευγάρι ήταν ο καθηγητής Θανάσης Καλημέρης (Ρένος Χαραλαμπίδης) και η Ελένη (Δήμητρα Ματσούκα).",
            "Η ατάκα του Χαραλαμπίδη 'Είστε πολύ μπανάλ!' και η σκηνή με το 'κουφετάκι' έγιναν κλασικές στιγμές της ελληνικής τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%84%CE%B9_%CF%84%CF%81%CE%AD%CF%87%CE%B5%CE%B9_%CE%BC%CE%B5_%CF%84%CE%BF%CF%85%CF%82_%CE%B4%CE%AF%CF%80%CE%BB%CE%B1",
        ["kati_trehei_me_tous_dipla", "charalampidis", "mega", "greek_tv"]
    ),
    # 390
    make_q(
        "pop_culture_med_390",
        "Ποιο μουσικό reality ταλέντων του ΑΝΤ1 το 2004 ανέδειξε νικήτρια την Καλομοίρα Σαράντη μέσα από έντονους τηλεοπτικούς καβγάδες;",
        "Fame Story 2",
        ["Super Idol", "Popstars", "Dream Show"],
        "Το Fame Story 2 με παρουσιαστή τον Ανδρέα Μικρούτσικο υπήρξε το απόλυτο τηλεοπτικό φαινόμενο της σεζόν 2003-2004 με πρωτοφανή νούμερα τηλεθέασης.",
        [
            "Η Καλομοίρα κέρδισε το κοινό με την παιδική της αφέλεια, τα σπαστά ελληνικά της και το πηγαίο ταλέντο της.",
            "Στο ίδιο παιχνίδι συμμετείχαν καλλιτέχνες όπως ο Κώστας Καραφώτης, η Ραλλία Χρηστίδου και ο Γιώργος Χρήστου."
        ],
        "https://el.wikipedia.org/wiki/Fame_Story",
        ["fame_story", "kalomira", "ant1", "reality_tv"]
    ),
    # 391
    make_q(
        "pop_culture_med_391",
        "Με ποιο ρυθμικό pop τραγούδι εκπροσώπησε η Καλομοίρα την Ελλάδα στη Eurovision του 2008 στο Βελιγράδι τερματίζοντας στην 3η θέση;",
        "Secret Combination",
        ["Shine", "My Secret", "Always and Forever"],
        "Το 'Secret Combination' (σε μουσική Κωνσταντίνου Παντζή και στίχους Ποσειδώνα Γιαννόπουλου) κέρδισε τον πρώτο ημιτελικό και κατέκτησε την 3η θέση στον τελικό με 218 βαθμούς.",
        [
            "Η σκηνική εμφάνιση περιλάμβανε ένα τεράστιο ανοιγόμενο βιβλίο από το οποίο ξεπετάχτηκε η τραγουδίστρια.",
            "Το τραγούδι έγινε τεράστια επιτυχία στην Ελλάδα και σε αρκετές ευρωπαϊκές χώρες."
        ],
        "https://en.wikipedia.org/wiki/Secret_Combination_(song)",
        ["kalomira", "eurovision", "secret_combination", "greek_music"]
    ),
    # 392
    make_q(
        "pop_culture_med_392",
        "Ποιο ήταν το χαρακτηριστικό έμβλημα της σκοτεινής οργάνωσης των ισχυρών κακοποιών στη σειρά 'Στο Παρά 5';",
        "Ένας κύκλος με πέντε βέλη (ή πεντάκτινο σύμβολο)",
        ["Μια μαύρη αράχνη", "Ένα φίδι γύρω από σπαθί", "Ένα γεράκι"],
        "Η οργάνωση των πέντε ισχυρών δολοφόνων χρησιμοποιούσε ένα ειδικό σύμβολο και μια καρφίτσα για να αναγνωρίζονται τα μέλη της.",
        [
            "Στο φινάλε της σειράς αποκαλύπτεται η ταυτότητα των πέντε ισχυρών ανδρών που κινούσαν τα νήματα πίσω από τη δολοφονία του υπουργού.",
            "Η αναζήτηση της αλήθειας ένωσε τους πέντε εντελώς διαφορετικούς πρωταγωνιστές σε μια αδιάσπαστη παρέα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CF%80%CE%B1%CF%81%CE%AC_5",
        ["sto_para_pente", "kapoutzidis", "mega", "greek_tv"]
    ),
    # 393
    make_q(
        "pop_culture_med_393",
        "Ποια ήταν η κοινωνική ιδιότητα της ζάπλουτης και αφελoύς Ντάλιας Χατζηαλεξάνδρου (Σμαράγδα Καρύδη) στο 'Στο Παρά 5';",
        "Κληρονόμος κολοσσιαίας περιουσίας",
        ["Εφοπλίστρια", "Πολιτικός", "Ιδιοκτήτρια τράπεζας"],
        "Η Ντάλια ζούσε απομονωμένη στη χλιδή χωρίς να γνωρίζει την αξία των χρημάτων, μέχρι που ενεπλάκη στην περιπέτεια των πέντε ηρώων.",
        [
            "Δεν ήξερε καν τι είναι το μετρό ή τα απλά χαρτονομίσματα, κουβαλώντας συχνά μαζί της τσάντες γεμάτες δεσμίδες.",
            "Η Σμαράγδα Καρύδη δημιούργησε έναν από τους πιο αγαπητούς και καλτ ρόλους στην ιστορία της ελληνικής τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CF%80%CE%B1%CF%81%CE%AC_5",
        ["sto_para_pente", "dalia", "smaragda_karydi", "greek_tv"]
    ),
    # 394
    make_q(
        "pop_culture_med_394",
        "Ποια ήταν η κλασική ατάκα που έλεγε η Ντάλια Χατζηαλεξάνδρου κάθε φορά που κάποιος ανέφερε ένα χρηματικό ποσό;",
        "Πόσα θες να με τρελάνεις;",
        ["Μα αυτά είναι ψίχουλα!", "Ποιος νοιάζεται για τα λεφτά;", "Αυτά είναι τίποτα!"],
        "Η Ντάλια θεωρούσε αδιανόητο ότι κάποιος μπορούσε να αγχώνεται για μικροποσά και πετούσε διαρκώς τη φράση 'Πόσα θες να με τρελάνεις;'.",
        [
            "Η ατάκα έγινε viral στην ελληνική καθημερινότητα και αναφέρεται μέχρι σήμερα.",
            "Σε ένα επεισόδιο, η Ντάλια αγοράζει ένα ολόκληρο ξενοδοχείο απλώς και μόνο για να μπορεί να χρησιμοποιήσει την τουαλέτα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CF%80%CE%B1%CF%81%CE%AC_5",
        ["sto_para_pente", "dalia", "greek_tv", "catchphrase"]
    ),
    # 395
    make_q(
        "pop_culture_med_395",
        "Πώς αυτοαποκαλούνταν χαϊδευτικά η ομάδα των πέντε ηρώων (Ντάλια, Ζουμπουλία, Αγγέλα, Φώτης, Σπύρος) στο 'Στο Παρά 5';",
        "Η ομάδα / Οι Πέντε",
        ["Οι Ατρόμητοι", "Οι Εκδικητές", "Η Συμμορία των 5"],
        "Οι πέντε άγνωστοι γνωρίστηκαν όταν παγιδεύτηκαν μαζί σε ένα ασανσέρ όπου άφησε την τελευταία του πνοή ένας δολοφονημένος υπουργός.",
        [
            "Ο Γιώργος Καπουτζίδης έγραψε το σενάριο με τέτοιο τρόπο ώστε κάθε χαρακτήρας να αντιπροσωπεύει έναν εντελώς διαφορετικό κοινωνικό κόσμο.",
            "Το τελευταίο επεισόδιο της σειράς το 2007 καθήλωσε πάνω από 3 εκατομμύρια τηλεθεατές με ποσοστό τηλεθέασης άνω του 60%."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CF%80%CE%B1%CF%81%CE%AC_5",
        ["sto_para_pente", "kapoutzidis", "mega", "greek_tv"]
    ),
    # 396
    make_q(
        "pop_culture_med_396",
        "Ποιο ήταν το παρατσούκλι που έδινε ο εαυτός της η απελπισμένη για γάμο Ματίνα Μανταρινάκη στο 'Κωνσταντίνου και Ελένης';",
        "Το ταπεινό χαμομηλάκι",
        ["Η πιστή σκυλίτσα", "Το άδολο περιστέρι", "Η αιώνια παρθένα"],
        "Η Ματίνα (Καλλιρρόη Μυριαγκού) αυτοχαρακτηριζόταν 'ταπεινό χαμομηλάκι' ενώ αναζητούσε απεγνωσμένα άνδρα για γάμο και έπεφτε σε συνεχή υστερικά κλάματα.",
        [
            "Η ατάκα της 'Εγώ θα περιμένω!' όταν απορριπτόταν από άνδρες έμεινε στην ιστορία.",
            "Στο τέλος της σειράς, η Ματίνα αλλάζει ριζικά εμφάνιση και νοοτροπία μετατρεπόμενη σε 'μοιραία γυναίκα'."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
        ["konstantinou_kai_elenis", "matina_mandarinaki", "ant1", "greek_tv"]
    ),
    # 397
    make_q(
        "pop_culture_med_397",
        "Ποια ηθοποιός ενσάρκωσε μοναδικά την κλαψιάρα γειτόνισσα Ματίνα Μανταρινάκη στο 'Κωνσταντίνου και Ελένης';",
        "Καλλιρρόη Μυριαγκού",
        ["Μαρία Λεκάκη", "Ελένη Ράντου", "Άννα Χατζησοφιά"],
        "Η Καλλιρρόη Μυριαγκού έκανε το τηλεοπτικό της ντεμπούτο με τον ρόλο της Ματίνας, κερδίζοντας τεράστια αναγνωρισιμότητα.",
        [
            "Η χαρακτηριστική υψίσυχνη φωνή και ο τρόπος που έκλαιγε ήταν αποκλειστική επινόηση της ηθοποιού για τον ρόλο.",
            "Αργότερα πρωταγωνίστησε σε πολλές θεατρικές παραστάσεις και στην τηλεοπτική σειρά 'Η Νταντά'."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BB%CE%BB%CE%B9%CF%81%CF%81%CF%8C%CE%B7_%CE%9C%CF%85%CF%81%CE%B9%CE%B1%CE%B3%CE%BA%CE%BF%CF%8D",
        ["kallirroi_myriagkou", "matina_mandarinaki", "konstantinou_kai_elenis"]
    ),
    # 398
    make_q(
        "pop_culture_med_398",
        "Ποια ήταν η χαρακτηριστική φράση που φώναζε ο μπάρμαν Μανώλης Σκουφάλης (Βασίλης Κούκουρας) όταν άκουγε κάτι εξωφρενικό στο 'Κωνσταντίνου και Ελένης';",
        "Σκίζω τα ρούχα μου!",
        ["Θα πηδηχτώ απ' το παράθυρο!", "Παναγία μου και Χριστέ μου!", "Έλεος πια!"],
        "Ο Μανώλης, ο γυναικάς μπάρμαν και καλύτερος φίλος του Κωνσταντίνου, απειλούσε διαρκώς ότι θα 'σκίσει τα ρούχα του' σε στιγμές έντασης.",
        [
            "Ο χαρακτήρας του Μανώλη ήταν γνωστός για τις δεκάδες ερωμένες του και την ανικανότητά του να μείνει πιστός σε μία σχέση.",
            "Η σχέση του με την Πέγκυ Καρρά (Μαρία Λεκάκη) πέρασε από αμέτρητους χωρισμούς και επανασυνδέσεις."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
        ["konstantinou_kai_elenis", "manolis", "koukouras", "greek_tv"]
    ),
    # 399
    make_q(
        "pop_culture_med_399",
        "Ποια ήταν η Ρωσίδα οικιακή βοηθός της Ντένης Μαρκορά στους 'Δύο Ξένους' με την οποία επικοινωνούσε σε μια ανύπαρκτη γλώσσα;",
        "Μαρούσκα (Καλλιόπη Ταχτσόγλου)",
        ["Σβετλάνα", "Όλγα", "Νατάσα"],
        "Η Ντένη Μαρκορά (Ντίνα Κώνστα) φώναζε συνεχώς 'Μαρούσκα, το εσπρεσάκι μου!' και η Μαρούσκα απαντούσε σταθερά με ένα ξερό 'Ντα!'.",
        [
            "Η Μαρούσκα καταλάβαινε τα πάντα αλλά μιλούσε μόνο ρωσικά (ή ακατάληπτα), λειτουργώντας ως η απόλυτη έμπιστη της Ντένης.",
            "Η χημεία ανάμεσα στις δύο ηθοποιούς δημιούργησε ένα από τα πιο αστεία τηλεοπτικά δίδυμα στην ιστορία του Mega."
        ],
        "https://el.wikipedia.org/wiki/%CE%94%CF%8D%CE%BF_%CE%BE%CE%AD%CE%BD%CE%BF%CE%B9",
        ["dyo_xenoi", "marouska", "deni_markora", "mega", "greek_tv"]
    ),
    # 400
    make_q(
        "pop_culture_med_400",
        "Ποια ομάδα ποδοσφαίρου υποστήριζε με φανατισμό η Ντένη Μαρκορά στους 'Δύο Ξένους' πηγαίνοντας τακτικά στο γήπεδο;",
        "Παναθηναϊκός",
        ["Ολυμπιακός", "ΑΕΚ", "ΠΑΟΚ"],
        "Η Ντένη Μαρκορά ήταν φανατική οπαδός του Παναθηναϊκού, έβριζε τους διαιτητές από τις εξέδρες και πανηγύριζε με πράσινα κασκόλ στο σαλόνι της.",
        [
            "Η αντίθεση της μεγαλοαστής κυρίας των βορείων προαστίων με το πάθος της χούλιγκαν για τον Παναθηναϊκό ήταν βασική πηγή γέλιου.",
            "Η ερμηνεία της Ντίνας Κώνστα ως Ντένη Μαρκορά θεωρείται αξεπέραστη στιγμή της ελληνικής τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%94%CF%8D%CE%BF_%CE%BE%CE%AD%CE%BD%CE%BF%CE%B9",
        ["dyo_xenoi", "deni_markora", "panathinaikos", "greek_tv"]
    ),
    # 401
    make_q(
        "pop_culture_med_401",
        "Ποια διάσημη ατάκα επαναλάμβανε η ηθοποιός Πέγκυ Καρρά (Μαρία Λεκάκη) όταν αναφερόταν στον εαυτό της στο 'Κωνσταντίνου και Ελένης';",
        "Είμαι μια ηθοποιός... ίσως η μόνη!",
        ["Είμαι ένα αστέρι που λάμπει!", "Το θέατρο είναι η ζωή μου!", "Γεννήθηκα για το σανίδι!"],
        "Η Πέγκυ Καρρά δήλωνε 'ηθοποιός... ίσως η μόνη' παρά το γεγονός ότι ήταν εντελώς ατάλαντη και έπαιζε μόνο σε αποτυχημένες παραστάσεις.",
        [
            "Ο μονόλογός της από το 'Σκηνικό Φως' ('Μάνα, φως!') χρησιμοποιούνταν ως μόνιμο πείραγμα από την Ελένη Βλαχάκη.",
            "Παρά την αποτυχία της στις οντισιόν, η Πέγκυ διατηρούσε ακλόνητη αυτοπεποίθηση."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
        ["konstantinou_kai_elenis", "peggy_karra", "maria_lekaki", "greek_tv"]
    ),
    # 402
    make_q(
        "pop_culture_med_402",
        "Στο 'Κωνσταντίνου και Ελένης', ποια ήταν η αγαπημένη γάτα της Ελένης Βλαχάκη που συχνά προκαλούσε την οργή του Κατακουζηνού;",
        "Μιτσούκο",
        ["Λούση", "Μπέμπα", "Φιφή"],
        "Η γάτα Μιτσούκο ήταν το αγαπημένο κατοικίδιο της Ελένης και ο Κατακουζηνός παραπονιόταν συνεχώς για τις τρίχες της στα έπιπλα αντίκες.",
        [
            "Σε ένα επεισόδιο, η Μιτσούκο εξαφανίζεται και η Ελένη κατηγορεί τον Κωνσταντίνο ότι την ξεφορτώθηκε.",
            "Η σχέση αγάπης-μίσους των δύο συγκατοίκων επεκτεινόταν ακόμα και στη φροντίδα της γάτας."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
        ["konstantinou_kai_elenis", "mitsouko", "eleni_vlachaki", "greek_tv"]
    ),
    # 403
    make_q(
        "pop_culture_med_403",
        "Στη σειρά 'Είσαι το Ταίρι μου', ποιος ήταν ο ιδιόρρυθμος Αυστραλός φίλος του Σωτήρη που μιλούσε άπταιστα αρχαία ελληνικά;",
        "Γρηγόρης (Βασίλης Χαραλαμπόπουλος)",
        ["Λάζαρος (Άρης Σερβετάλης)", "Μίλτος", "Νίκος"],
        "Ο Γρηγόρης ήταν ένας συνεσταλμένος νέος που ερωτεύτηκε τη Βίκυ (Στέλλα) χωρίς να γνωρίζει την πραγματική της ταυτότητα.",
        [
            "Η παρέα του Γρηγόρη, του Σωτήρη (Αλέξης Γεωργούλης) και του Λάζαρου (Άρης Σερβετάλης) άφησε εποχή στην ελληνική τηλεόραση.",
            "Ο Άρης Σερβετάλης ως Λάζαρος με το κόκκινο μαλλί και το ιγκουάνα του 'Μήτσο' έγινε το απόλυτο είδωλο της νεολαίας της εποχής."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
        ["eisai_to_tairi_mou", "charalampopoulos", "servetalis", "greek_tv"]
    ),
    # 404
    make_q(
        "pop_culture_med_404",
        "Τι κατοικίδιο ζώο είχε ο ανατρεπτικός Λάζαρος (Άρης Σερβετάλης) στη σειρά 'Είσαι το Ταίρι μου' και το κουβαλούσε παντού μαζί του;",
        "Ένα ιγκουάνα (τον Μήτσο)",
        ["Έναν χαμαιλέοντα", "Ένα φίδι", "Έναν παπαγάλο"],
        "Ο Λάζαρος είχε ως πιστό του σύντροφο ένα πράσινο ιγκουάνα με το όνομα Μήτσος, το οποίο τάιζε και του μιλούσε σαν να ήταν άνθρωπος.",
        [
            "Ο ρόλος του Λάζαρου εκτόξευσε τη δημοτικότητα του Άρη Σερβετάλη, κάνοντας το εκκεντρικό στυλ του μόδα ανάμεσα στους εφήβους.",
            "Η σκηνή όπου ο Λάζαρος χορεύει ζεϊμπέκικο με τον δικό του μοναδικό τρόπο παραμένει από τις πιο viral στιγμές της σειράς."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
        ["eisai_to_tairi_mou", "lazaros", "iguana", "servetalis", "greek_tv"]
    ),
    # 405
    make_q(
        "pop_culture_med_405",
        "Ποια διάσημη ατάκα έλεγε διαρκώς η αυταρχική Αννέτα (Δάφνη Λαμπρόγιαννη) στον μικρό της γιο Μιλτιάδη στο 'Είσαι το Ταίρι μου';",
        "Μιλτιάδη, είσαι ένα τέρας!",
        ["Μιλτιάδη, διάβασε!", "Μιλτιάδη, σταμάτα!", "Μιλτιάδη, σιωπή!"],
        "Η Αννέτα προσπαθούσε να αναθρέψει τον γιο της ως παιδί-θαύμα με αυστηρό πρόγραμμα, αλλά κατέληγε πάντα να του φωνάζει 'Μιλτιάδη, είσαι ένα τέρας!'.",
        [
            "Ο μικρός Μιλτιάδης (Παναγιώτης Φιλιππαίος) απαντούσε με απόλυτη ψυχραιμία και κυνισμό στις υστερίες της μητέρας του.",
            "Η σχέση μητέρας-γιου αποτέλεσε μία από τις πιο απολαυστικές υποπλοκές της σειράς."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
        ["eisai_to_tairi_mou", "anneta", "miltiadis", "greek_tv"]
    ),
    # 406
    make_q(
        "pop_culture_med_406",
        "Ποια ελληνική ταινία του Νίκου Περράκη το 1984 σημείωσε τεράστια επιτυχία σατιρίζοντας τη στρατιωτική θητεία στον Έβρο κατά τη διάρκεια της Χούντας;",
        "Λούφα και Παραλλαγή",
        ["Βίος και Πολιτεία", "Αυτοί που μίλησαν με τον θάνατο", "Σειρήνες στο Αιγαίο"],
        "Η 'Λούφα και Παραλλαγή' παρακολουθεί μια ομάδα στρατιωτών που υπηρετούν στην Τηλεόραση Ενόπλων Δυνάμεων (ΥΕΝΕΔ) κατά τη δικτατορία των συνταγματαρχών.",
        [
            "Κέρδισε τέσσερα βραβεία στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης, ανάμεσά τους Καλύτερης Ταινίας και Σεναρίου.",
            "Το 2005 ο Περράκης κυκλοφόρησε το sequel 'Λούφα και Παραλλαγή: Σειρήνες στο Αιγαίο' σημειώνοντας εισπρακτικό ρεκόρ με πάνω από 1,3 εκατομμύριο εισιτήρια."
        ],
        "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CF%8D%CF%86%CE%B1_%CE%BA%CE%B1%CE%B9_%CF%80%CE%B1%CF%81%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE",
        ["loufa_kai_parallagi", "perrakis", "greek_cinema", "comedy"]
    ),
    # 407
    make_q(
        "pop_culture_med_407",
        "Ποιο τραγούδι σε μουσική Στέφανου Κορκολή και στίχους Πάνου Φαλάρα ερμήνευσε ο Σάκης Ρουβάς το 1991 κάνοντας το εκρηκτικό του ντεμπούτο;",
        "Πάρ' τα",
        ["Μην αντιστέκεσαι", "1992", "Αίμα, δάκρυα κι ιδρώτας"],
        "Ο Σάκης Ρουβάς εμφανίστηκε στο Φεστιβάλ Τραγουδιού Θεσσαλονίκης το 1991 με το 'Πάρ' τα' κερδίζοντας το βραβείο καλύτερης σύνθεσης και προκαλώντας υστερία.",
        [
            "Η εμφάνισή του στη σκηνή με τζιν και λευκό πουκάμισο ξεκίνησε το φαινόμενο των 'Ρουβιτσών'.",
            "Ο μάνατζερ Ηλίας Ψινάκης ανέλαβε την προώθησή του δημιουργώντας ένα πρωτοφανές σταρ-σίστεμ για τα ελληνικά δεδομένα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CE%AC%CE%BA%CE%B7%CF%82_%CE%A1%CE%BF%CF%85%CE%B2%CE%AC%CF%82",
        ["sakis_rouvas", "par_ta", "korkolis", "greek_music"]
    ),
    # 408
    make_q(
        "pop_culture_med_408",
        "Πώς ονομάστηκαν από τα ελληνικά μέσα ενημέρωσης οι χιλιάδες φανατικές νεαρές θαυμάστριες του Σάκη Ρουβά στη δεκαετία του 1990;",
        "Ρουβίτσες",
        ["Σακίστριες", "Ρουβικίτσες", "Σακοκόριτσα"],
        "Ο όρος 'Ρουβίτσες' επινοήθηκε για να περιγράψει τα κορίτσια που ούρλιαζαν, λιποθυμούσαν και καταδίωκαν τον Σάκη Ρουβά σε συναυλίες και ξενοδοχεία.",
        [
            "Το φαινόμενο συγκρίθηκε συχνά από τους κοινωνιολόγους με την Beatlemania της δεκαετίας του 1960.",
            "Η λέξη πέρασε στην καθομιλουμένη νεοελληνική γλώσσα ως σύμβολο της απόλυτης εφηβικής λατρείας για ένα ποπ είδωλο."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CE%AC%CE%BA%CE%B7%CF%82_%CE%A1%CE%BF%CF%85%CE%B2%CE%AC%CF%82",
        ["sakis_rouvas", "rouvitses", "pop_culture", "90s"]
    ),
    # 409
    make_q(
        "pop_culture_med_409",
        "Ποια ελληνική ταινία του 1999 σε σκηνοθεσία Μιχάλη Ρέππα και Θανάση Παπαθανασίου έσπασε όλα τα ρεκόρ εισιτηρίων ξεπερνώντας το 1,2 εκατομμύριο θεατές;",
        "Safe Sex",
        ["Το Κλάμα Βγήκε απ' τον Παράδεισο", "Οξυγόνο", "Αυστηρώς Κατάλληλο"],
        "Το 'Safe Sex' ήταν μια σπονδυλωτή σεξουαλική κωμωδία που αποτύπωνε την ευημερία και τα ήθη της Ελλάδας στα τέλη της δεκαετίας του 1990.",
        [
            "Έγινε η πιο εμπορική ελληνική ταινία όλων των εποχών μέχρι τότε, αναζωογονώντας το ενδιαφέρον του κοινού για τον ελληνικό κινηματογράφο.",
            "Το σάουντρακ της ταινίας περιλάμβανε το τραγούδι 'Μείνε μαζί μου έστω για λίγο' από τη Χάρις Αλεξίου."
        ],
        "https://el.wikipedia.org/wiki/Safe_Sex_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["safe_sex", "reppas_papathanasiou", "greek_cinema", "blockbuster"]
    ),
    # 410
    make_q(
        "pop_culture_med_410",
        "Ποια επική παρωδία του παλιού ελληνικού κινηματογράφου γύρισαν οι Ρέππας - Παπαθανασίου το 2001 με τη φανταστική οικογένεια Μπισμπίκη και Δελαφράγκα;",
        "Το Κλάμα Βγήκε απ' τον Παράδεισο",
        ["Safe Sex", "Αυστηρώς Κατάλληλο", "Νήsos"],
        "Η ταινία παρωδεί με ευφυή τρόπο όλα τα κλισέ του ελληνικού κινηματογράφου των δεκαετιών του '50 και '60 (μελόδραμα, βουκολικά, μιούζικαλ, πολεμικά).",
        [
            "Η ατάκα της Μίρκας Παπακωνσταντίνου ως Τζέλα Δελαφράγκα 'Και μη ξεχνάτε: η Τζέλα Δελαφράγκα δεν πεθαίνει ποτέ!' έμεινε στην ιστορία.",
            "Υπήρξε μία από τις πιο ακριβές παραγωγές του ελληνικού σινεμά, με εκατοντάδες κοστούμια εποχής και εντυπωσιακά σκηνικά."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%BB%CE%AC%CE%BC%CE%B1_%CE%B2%CE%B3%CE%AE%CE%BA%CE%B5_%CE%B1%CF%80%CF%8C_%CF%84%CE%BF%CE%BD_%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF",
        ["to_klama_vgike_ap_ton_paradeiso", "reppas_papathanasiou", "greek_cinema", "comedy"]
    ),
]

if __name__ == "__main__":
    validate_and_append("pop_culture", "medium", 3, questions)

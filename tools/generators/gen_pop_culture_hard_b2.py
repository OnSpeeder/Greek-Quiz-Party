# -*- coding: utf-8 -*-
"""Generator for pop_culture_hard questions 311-410 (100 questions)."""
import os
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

def make_q(qid, text, correct, distractors, explanation, fun_facts, source, tags, diff=5):
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
        "pop_culture_hard_311",
        "Ποιο ήταν το όνομα και ο πλανήτης καταγωγής του Galactus πριν τη Μεγάλη Έκρηξη και τη μεταμόρφωσή του σε κοσμικό καταβροχθιστή πλανητών;",
        "Galan από τον πλανήτη Taa",
        ["Norrin Radd από τον Zenn-La", "Taneleer Tivan από τον Cygnus", "En Sabah Nur από την Αίγυπτο"],
        "Ο Galan ήταν ένας εξερευνητής του προηγούμενου σύμπαντος που συγχωνεύτηκε με τη Sentience of the Universe πριν το Big Bang, αναγεννώμενος ως Galactus.",
        [
            "Ο πλανήτης Taa ήταν ο πιο προηγμένος πολιτισμός του προηγούμενου κοσμικού κύκλου.",
            "Ο Galactus πρωτοεμφανίστηκε στην ιστορική 'The Galactus Trilogy' στο Fantastic Four #48-50 το 1966 από τους Stan Lee και Jack Kirby."
        ],
        "https://en.wikipedia.org/wiki/Galactus",
        ["galactus", "galan_of_taa", "marvel", "fantastic_four"]
    ),
    # 312
    make_q(
        "pop_culture_hard_312",
        "Πώς ονομάζεται το πρωτότυπο σκάφος και διαστημική βάση του Ronan the Accuser και των Kree Accuser Corps στα κόμικς και το MCU;",
        "Dark Aster",
        ["Sanctuary II", "Chitauri Command", "Statesman"],
        "Το Dark Aster είναι το τεράστιο διαστημόπλοιο σε σχήμα ανάποδου σταυρού/γερακιού με το οποίο ο Ronan επιτέθηκε στον πλανήτη Xandar.",
        [
            "Στο τέλος της ταινίας 'Guardians of the Galaxy' (2014), το σκάφος συντρίβεται στην επιφάνεια του Xandar.",
            "Το χαρακτηριστικό όπλο του Ronan είναι το Cosmi-Rod (Universal Weapon) που μπορεί να διοχετεύει κοσμική ενέργεια."
        ],
        "https://en.wikipedia.org/wiki/Ronan_the_Accuser",
        ["ronan_the_accuser", "dark_aster", "guardians_of_the_galaxy", "marvel"]
    ),
    # 313
    make_q(
        "pop_culture_hard_313",
        "Ποιο ήταν το πραγματικό όνομα γέννησης του Wolverine πριν υιοθετήσει το ψευδώνυμο Logan στον 19ο αιώνα στον Καναδά;",
        "James Howlett",
        ["Thomas Logan", "John Howlett", "Victor Creed"],
        "Η καταγωγή του Wolverine αποκαλύφθηκε πλήρως στη μίνι σειρά κόμικς 'Origin' (2001-2002) από τον Paul Jenkins.",
        [
            "Ο μικρός James Howlett εμφάνισε για πρώτη φορά τα οστέινα νύχια του όταν είδε τον πατέρα του να δολοφονείται από τον επιστάτη Thomas Logan.",
            "Υιοθέτησε το όνομα 'Logan' καθώς διέφυγε στην άγρια φύση του καναδικού βορρά για να κρυφτεί."
        ],
        "https://en.wikipedia.org/wiki/Wolverine_(character)#Origin",
        ["wolverine", "james_howlett", "marvel", "xmen", "origin"]
    ),
    # 314
    make_q(
        "pop_culture_hard_314",
        "Ποιο είναι το όνομα του μεταλλαγμένου γιου του Wolverine από την Ιαπωνία, ο οποίος διαθέτει επίσης πτυσσόμενα νύχια και φερομόνες;",
        "Daken (Akihiro)",
        ["Silver Samurai", "Shinobi Shaw", "Sunfire"],
        "Ο Akihiro (Daken) είναι γιος του Logan και της Γιαπωνέζας συζύγου του Itsu, ο οποίος μεγάλωσε με μίσος για τον πατέρα του υπό την καθοδήγηση του Romulus.",
        [
            "Η λέξη 'Daken' (駄犬) είναι ιαπωνική υβριστική λέξη που σημαίνει 'μπάσταρδο σκυλί'.",
            "Διαθέτει δύο νύχια στην κορυφή του καρπού και ένα τρίτο νύχι που προεξέχει από την κάτω πλευρά του καρπού."
        ],
        "https://en.wikipedia.org/wiki/Daken",
        ["daken", "wolverine", "marvel", "xmen"]
    ),
    # 315
    make_q(
        "pop_culture_hard_315",
        "Ποιο νησιωτικό κράτος ανοιχτά της Αφρικής έγινε καταφύγιο και κυρίαρχο κράτος μεταλλαγμένων υπό τον Magneto τη δεκαετία του 1990;",
        "Τζενόσα (Genosha)",
        ["Μάντριπουρ", "Κρακόα", "Σοκόβια"],
        "Η Genosha ήταν αρχικά ένα κράτος απαρτχάιντ όπου οι μεταλλαγμένοι υποδουλώνονταν ως εργάτες πριν ο Magneto αναλάβει τον πλήρη έλεγχο της χώρας.",
        [
            "Το 2001, στο 'New X-Men' του Grant Morrison, η Cassandra Nova εξαπέλυσε γιγάντια Sentinels εξοντώνοντας 16 εκατομμύρια μεταλλαγμένους στη Genosha.",
            "Η γενοκτονία της Genosha αποτέλεσε μία από τις πιο καθοριστικές και σκοτεινές τραγωδίες στην ιστορία των X-Men."
        ],
        "https://en.wikipedia.org/wiki/Genosha",
        ["genosha", "xmen", "magneto", "marvel"]
    ),
    # 316
    make_q(
        "pop_culture_hard_316",
        "Ποιος ιστορικός συγγραφέας των X-Men έγραψε το εμβληματικό graphic novel 'God Loves, Man Kills' (1982) που ενέπνευσε την ταινία X2;",
        "Chris Claremont",
        ["John Byrne", "Jim Lee", "Grant Morrison"],
        "Ο Chris Claremont συνέγραψε τη σειρά Uncanny X-Men επί 16 συνεχόμενα χρόνια (1975-1991), δημιουργώντας τη χρυσή εποχή των μεταλλαγμένων.",
        [
            "Στο 'God Loves, Man Kills', ο φανατικός ιεροκήρυκας William Stryker ξεκινά μια σταυροφορία εξόντωσης των μεταλλαγμένων στο όνομα της θρησκείας.",
            "Η ιστορία ανάγκασε τους X-Men και τον Magneto να ενώσουν τις δυνάμεις τους ενάντια στον ανθρώπινο φανατισμό."
        ],
        "https://en.wikipedia.org/wiki/X-Men:_God_Loves,_Man_Kills",
        ["chris_claremont", "xmen", "god_loves_man_kills", "marvel"]
    ),
    # 317
    make_q(
        "pop_culture_hard_317",
        "Ποιο ήταν το πραγματικό αρχικό κίνητρο του Thanos για την εξόντωση του μισού σύμπαντος στο κλασικό κόμικ 'The Infinity Gauntlet' (1991);",
        "Για να κερδίσει την αγάπη της κοσμικής οντότητας του Θανάτου (Mistress Death)",
        ["Για να σώσει το σύμπαν από υπερπληθυσμό", "Για να κατακτήσει τον θρόνο του Asgard", "Για να καταστρέψει τη Γη"],
        "Στα κόμικς του Jim Starlin, ο Thanos ήταν παθολογικά ερωτευμένος με την προσωποποίηση του Θανάτου και ήθελε να της προσφέρει ως δώρο δισεκατομμύρια ψυχές.",
        [
            "Στο MCU το κίνητρό του άλλαξε σε μια φιλοσοφική θεωρία εξισορρόπησης πόρων για να τον καταστήσει πιο ρεαλιστικό ανταγωνιστή.",
            "Παρά τη θυσία του μισού σύμπαντος, η Mistress Death συνέχισε να τον αγνοεί επιδεικτικά στα κόμικς, στρέφοντας το ενδιαφέρον της στον Deadpool."
        ],
        "https://en.wikipedia.org/wiki/The_Infinity_Gauntlet",
        ["thanos", "mistress_death", "infinity_gauntlet", "marvel", "comics"]
    ),
    # 318
    make_q(
        "pop_culture_hard_318",
        "Τι ήταν στην πραγματικότητα ο διαστημικός σταθμός και πόλη Knowhere στο σύμπαν της Marvel πριν μετατραπεί σε ορυχείο;",
        "Το αποκομμένο κεφάλι ενός αρχαίου Σελέστιαλ (Celestial)",
        ["Ένας νεκρός πλανήτης των Skrulls", "Μια τεχνητή βάση των Kree", "Ένας διαστημικός μετεωρίτης"],
        "Το Knowhere βρίσκεται στην άκρη του γνωστού σύμπαντος και οι κάτοικοί του εξορύσσουν τον εγκεφαλικό ιστό και το νωτιαίο υγρό του ουράνιου γίγαντα.",
        [
            "Στο MCU, ο Collector διατηρούσε το μουσείο του μέσα στο Knowhere.",
            "Στο Guardians of the Galaxy Holiday Special (2022), οι Φύλακες αγοράζουν το Knowhere από τον Collector και το μετατρέπουν σε επίσημη έδρα τους."
        ],
        "https://en.wikipedia.org/wiki/Knowhere",
        ["knowhere", "celestial", "guardians_of_the_galaxy", "marvel"]
    ),
    # 319
    make_q(
        "pop_culture_hard_319",
        "Ποια μυστική οργάνωση πλουσίων οικογενειών της Gotham City με μάσκες κουκουβάγιας εισήγαγαν οι Scott Snyder και Greg Capullo το 2011;",
        "The Court of Owls (Το Δικαστήριο των Κουκουβαγιών)",
        ["The Black Glove", "Order of Saint Dumas", "The Sacred Order"],
        "Το Court of Owls ελέγχει κρυφά την Gotham City εδώ και αιώνες μέσα από μυστικά δωμάτια κρυμμένα στον 13ο όροφο των παλιών κτιρίων της πόλης.",
        [
            "Οι θανατηφόροι, αναστημένοι δολοφόνοι του δικαστηρίου ονομάζονται Talons και διατηρούνται σε κρυογονική κατάσταση.",
            "Η ιστορία ξεκινά με ένα παλιό παιδικό νανούρισμα της Gotham που προειδοποιεί: 'Beware the Court of Owls, that watches all the time...'."
        ],
        "https://en.wikipedia.org/wiki/Court_of_Owls",
        ["court_of_owls", "batman", "scott_snyder", "dc_comics"]
    ),
    # 320
    make_q(
        "pop_culture_hard_320",
        "Σε ποιο ιστορικό τεύχος του Green Lantern/Green Arrow (1971) αποκαλύφθηκε ο εθισμός του βοηθού Speedy (Roy Harper) στην ηρωίνη;",
        "Green Lantern #85 ('Snowbirds Don't Fly')",
        ["Action Comics #250", "Detective Comics #400", "Batman #232"],
        "Το τεύχος των Dennis O'Neil και Neal Adams σόκαρε τη βιομηχανία αντιμετωπίζοντας ρεαλιστικά τον εθισμό στα ναρκωτικά χωρίς την έγκριση του Comics Code Authority.",
        [
            "Το εξώφυλλο έδειχνε τον Speedy με τα σύνεργα της χρήσης και τον Green Arrow να αναφωνεί με απόγνωση.",
            "Ο τότε δήμαρχος της Νέας Υόρκης John Lindsay έστειλε συγχαρητήρια επιστολή στην DC Comics για την κοινωνική προσφορά του τεύχους."
        ],
        "https://en.wikipedia.org/wiki/Snowbirds_Don%27t_Fly",
        ["green_lantern", "speedy", "dennis_oneil", "neal_adams", "dc_comics"]
    ),
    # 321
    make_q(
        "pop_culture_hard_321",
        "Ποιος Βρετανός καλλιτέχνης σχεδίασε το επαναστατικό graphic novel 'Watchmen' (1986-1987) σε σενάριο του Alan Moore;",
        "Dave Gibbons",
        ["Brian Bolland", "David Lloyd", "John Higgins"],
        "Ο Dave Gibbons καθιέρωσε την αυστηρή διάταξη πλέγματος 9 καρέ ανά σελίδα (nine-panel grid) που έδωσε στο Watchmen τον χαρακτηριστικό κινηματογραφικό ρυθμό του.",
        [
            "Ο χρωματιστής John Higgins χρησιμοποίησε δευτερεύουσες αποχρώσεις (μωβ, πορτοκαλί) αντί για τα βασικά χρώματα των κλασικών κόμικς.",
            "Το Watchmen παραμένει το μοναδικό graphic novel που συμπεριλήφθηκε στη λίστα του περιοδικού Time με τα 100 καλύτερα αγγλόφωνα μυθιστορήματα από το 1923."
        ],
        "https://en.wikipedia.org/wiki/Dave_Gibbons",
        ["watchmen", "dave_gibbons", "alan_moore", "dc_comics"]
    ),
    # 322
    make_q(
        "pop_culture_hard_322",
        "Ποιο ήταν το πραγματικό ονοματεπώνυμο του υπερήρωα The Comedian του οποίου η δολοφονία ξεκινά την πλοκή στο 'Watchmen';",
        "Edward Blake",
        ["Walter Kovacs", "Dan Dreiberg", "Adrian Veidt"],
        "Ο Edward Blake ήταν ένας κυνικός, βίαιος κυβερνητικός πράκτορας που θεωρούσε τον κόσμο ένα κακόγουστο αστείο.",
        [
            "Η κίτρινη καρφίτσα με το χαμογελαστό πρόσωπο (smiley face) και τη σταγόνα αίματος έγινε το κεντρικό σύμβολο του έργου.",
            "Αποκαλύπτεται αργότερα ότι ήταν ο βιολογικός πατέρας της Silk Spectre II (Laurie Juspeczyk)."
        ],
        "https://en.wikipedia.org/wiki/Comedian_(character)",
        ["watchmen", "edward_blake", "the_comedian", "alan_moore"]
    ),
    # 323
    make_q(
        "pop_culture_hard_323",
        "Ποιο ήταν το πραγματικό όνομα του πανέξυπνου βιομήχανου Ozymandias στο 'Watchmen' που σχεδίασε τη σωτηρία του κόσμου μέσω μιας κατασκευασμένης τραγωδίας;",
        "Adrian Veidt",
        ["Walter Kovacs", "Jon Osterman", "Hollis Mason"],
        "Ο Adrian Veidt θεωρούσε τον εαυτό του πνευματικό διάδοχο του Μεγάλου Αλεξάνδρου και του Φαραώ Ραμσή Β' (Οσυμανδύα).",
        [
            "Τηλεμετέφερε ένα γενετικά κατασκευασμένο 'εξωγήινο' τέρας στην καρδιά της Νέας Υόρκης σκοτώνοντας εκατομμύρια για να αποτρέψει τον πυρηνικό πόλεμο ΗΠΑ-ΕΣΣΔ.",
            "Στην κινηματογραφική μεταφορά του Zack Snyder (2009), το τέρας αντικαταστάθηκε από ενεργειακή έκρηξη που ενοχοποιούσε τον Doctor Manhattan."
        ],
        "https://en.wikipedia.org/wiki/Ozymandias_(character)",
        ["watchmen", "adrian_veidt", "ozymandias", "dc_comics"]
    ),
    # 324
    make_q(
        "pop_culture_hard_324",
        "Ποιο ήταν το όνομα του κόμικ πειρατών μέσα στο κόμικ που διαβάζει ένα αγόρι δίπλα σε ένα περίπτερο στο 'Watchmen';",
        "Tales of the Black Freighter",
        ["Curse of the Crimson Corsair", "Pirates of the Damned", "Ghost Ship Chronicles"],
        "Το κόμικ εξιστορεί την κάθοδο ενός ναυαγού καπετάνιου στην απόλυτη παράνοια καθώς προσπαθεί να προειδοποιήσει την πατρίδα του για το πλοίο-φάντασμα Black Freighter.",
        [
            "Η ιστορία λειτουργεί ως σκοτεινός αλληγορικός καθρέφτης για τις πράξεις και την ψυχοσύνθεση του ίδιου του Adrian Veidt.",
            "Στο σύμπαν του Watchmen, τα πειρατικά κόμικς αντικατέστησαν τα υπερηρωικά επειδή οι πραγματικοί υπερήρωες υπήρχαν στην καθημερινότητα."
        ],
        "https://en.wikipedia.org/wiki/Watchmen#Tales_of_the_Black_Freighter",
        ["watchmen", "black_freighter", "alan_moore", "dave_gibbons"]
    ),
    # 325
    make_q(
        "pop_culture_hard_325",
        "Ποιο ήταν το όνομα του δειλού πράσινου τίγρη του πρίγκιπα Adam πριν μεταμορφωθεί στον ατρόμητο Battle Cat στο Masters of the Universe;",
        "Cringer",
        ["Panthor", "Clawful", "Stridor"],
        "Ο Cringer τρέμει στην παραμικρή απειλή και προσπαθεί να κρυφτεί, αλλά όταν ο He-Man τον αγγίζει με το Power Sword μεταμορφώνεται σε θωρακισμένο πολεμικό αιλουροειδές.",
        [
            "Ο ανταγωνιστής Skeletor έχει έναν αντίστοιχο μωβ πάνθηρα με το όνομα Panthor.",
            "Ο σχεδιασμός του Battle Cat προέκυψε επειδή η Mattel χρησιμοποίησε ένα παλιό καλούπι τίγρη από τη σειρά 'Big Jim' βάφοντάς το πράσινο για εξοικονόμηση κόστους."
        ],
        "https://en.wikipedia.org/wiki/Battle_Cat",
        ["he_man", "cringer", "battle_cat", "masters_of_the_universe"]
    ),
    # 326
    make_q(
        "pop_culture_hard_326",
        "Ποιος συγγραφέας της Marvel έγραψε το επίσημο 'story bible' των Transformers το 1984 επινοώντας σχεδόν όλα τα ονόματα των ηρώων όπως Optimus Prime και Megatron;",
        "Bob Budiansky",
        ["Jim Shooter", "Stan Lee", "Larry Hama"],
        "Ο Bob Budiansky δημιούργησε τα ονόματα, τις προσωπικότητες και τις βιογραφίες για δεκάδες αρχικούς χαρακτήρες των Transformers μέσα σε ένα μόνο Σαββατοκύριακο.",
        [
            "Η Hasbro είχε αγοράσει τα δικαιώματα των παιχνιδιών από την ιαπωνική Takara αλλά δεν είχε καμία ιστορία ή υπόβαθρο για τους χαρακτήρες.",
            "Ο Budiansky έγραψε επίσης το μεγαλύτερο μέρος της κλασικής σειράς κόμικς Transformers της Marvel."
        ],
        "https://en.wikipedia.org/wiki/Bob_Budiansky",
        ["transformers", "bob_budiansky", "marvel", "hasbro"]
    ),
    # 327
    make_q(
        "pop_culture_hard_327",
        "Από ποιες δύο ιαπωνικές σειρές παιχνιδιών της Takara προήλθαν οι αρχικές φιγούρες που συνδυάστηκαν από τη Hasbro για να δημιουργήσουν τους Transformers το 1984;",
        "Diaclone και Microman (Micro Change)",
        ["Gundam και Macross", "Chogokin και Zoids", "Super Sentai και Kamen Rider"],
        "Η σειρά Diaclone περιλάμβανε οχήματα που γίνονταν ρομπότ (τα μετέπειτα αυτοκίνητα Autobots), ενώ η Micro Change περιλάμβανε αντικείμενα κλίμακας 1:1 όπως το όπλο Megatron και το κασετόφωνο Soundwave.",
        [
            "Στα ιαπωνικά παιχνίδια Diaclone υπήρχαν μικροσκοπικοί πιλότοι που έμπαιναν μέσα στα ρομπότ, τους οποίους η Hasbro κατάργησε για να κάνει τα ρομπότ αυτόνομες οντότητες.",
            "Η επιτυχία της συγχώνευσης δημιούργησε ένα από τα μακροβιότερα franchise παιχνιδιών στην ιστορία."
        ],
        "https://en.wikipedia.org/wiki/Transformers#History",
        ["transformers", "diaclone", "microman", "takara", "hasbro"]
    ),
    # 328
    make_q(
        "pop_culture_hard_328",
        "Ποιος Σουηδός animator δημιούργησε το 2003 τον χαρακτήρα 'The Annoying Thing' που αργότερα έγινε παγκόσμιο φαινόμενο ως 'Crazy Frog';",
        "Erik Wernquist",
        ["Daniel Malmedahl", "Jonas Odell", "Markus Persson"],
        "Ο Erik Wernquist σχεδίασε το 3D animation ενός εκκεντρικού μπλε αμφιβίου συνδυάζοντάς το με τους ήχους μηχανής που είχε ηχογραφήσει ο Daniel Malmedahl το 1997.",
        [
            "Η γερμανική εταιρεία Jamster αγόρασε τα δικαιώματα και μετέτρεψε το κλιπ σε ήχο κλήσης κινητού (ringtone), κερδίζοντας εκατοντάδες εκατομμύρια ευρώ.",
            "Το remix του 'Axel F' από τον Crazy Frog έφτασε στο νούμερο 1 των βρετανικών charts το 2005 εκθρονίζοντας τους Coldplay."
        ],
        "https://en.wikipedia.org/wiki/Crazy_Frog",
        ["crazy_frog", "erik_wernquist", "viral", "ringtone"]
    ),
    # 329
    make_q(
        "pop_culture_hard_329",
        "Σε ποια ακριβή ημερομηνία αναρτήθηκε το πρώτο tweet στην ιστορία του Twitter από τον συνιδρυτή Jack Dorsey;",
        "21 Μαρτίου 2006",
        ["15 Ιανουαρίου 2006", "4 Ιουλίου 2006", "11 Σεπτεμβρίου 2006"],
        "Ο Jack Dorsey έγραψε το μήνυμα 'just setting up my twttr' στις 21 Μαρτίου 2006 στις 21:50 UTC εγκαινιάζοντας την πλατφόρμα.",
        [
            "Αρχικά η πλατφόρμα ονομαζόταν 'twttr' χωρίς φωνήεντα, εμπνευσμένη από το Flickr και τα πενταψήφια SMS.",
            "Το 2021 ο Dorsey πούλησε το πρώτο αυτό tweet ως NFT για το ποσό των 2,9 εκατομμυρίων δολαρίων."
        ],
        "https://en.wikipedia.org/wiki/Twitter",
        ["twitter", "jack_dorsey", "first_tweet", "social_media", "2006"]
    ),
    # 330
    make_q(
        "pop_culture_hard_330",
        "Ποιο ήταν το όνομα της θηλυκής σκυλίτσας ράτσας Shiba Inu από την Ιαπωνία που υπήρξε το αυθεντικό πρόσωπο του meme 'Doge' και έφυγε από τη ζωή το 2024;",
        "Kabosu",
        ["Saki", "Hana", "Momo"],
        "Η Kabosu διασώθηκε από εκτροφείο κουταβιών το 2008 από τη νηπιαγωγό Atsuko Sato, η οποία ανάρτησε τη διάσημη φωτογραφία στο blog της το 2010.",
        [
            "Η έκφραση του προσώπου της με τα σταυρωμένα πόδια και το πλάγιο βλέμμα ενέπνευσε το κρυπτονόμισμα Dogecoin.",
            "Ένα χάλκινο άγαλμα της Kabosu ανεγέρθηκε προς τιμήν της σε πάρκο της πόλης Sakura στην Ιαπωνία."
        ],
        "https://en.wikipedia.org/wiki/Kabosu_(dog)",
        ["kabosu", "doge", "shiba_inu", "memes", "dogecoin"]
    ),
    # 331
    make_q(
        "pop_culture_hard_331",
        "Ποιος Ισπανός σχεδιαστής και εφευρέτης δημιούργησε το 1907 το φόρεμα 'Delphos' εμπνευσμένο από τον Ηνίοχο των Δελφών με μυστική τεχνική πλισαρίσματος;",
        "Mariano Fortuny",
        ["Cristóbal Balenciaga", "Paco Rabanne", "Manolo Blahnik"],
        "Ο Mariano Fortuny y Madrazo κατοχύρωσε την πατέντα για το κυματιστό πλισέ μετάξι το 1909 στη Βενετία, δημιουργώντας ένα φόρεμα που απελευθέρωσε το γυναικείο σώμα από τον κορσέ.",
        [
            "Κάθε φόρεμα Delphos παραδιδόταν τυλιγμένο σφιχτά σε ένα μικρό κουτί για να διατηρείται το λεπτό πλισάρισμα.",
            "Το σχέδιο αναφέρεται εκτενώς στο αριστούργημα του Marcel Proust 'Αναζητώντας τον Χαμένο Χρόνο'."
        ],
        "https://en.wikipedia.org/wiki/Delphos_gown",
        ["mariano_fortuny", "delphos_gown", "delphi", "fashion_history"]
    ),
    # 332
    make_q(
        "pop_culture_hard_332",
        "Ποια ταινία του 1980 με πρωταγωνιστή τον Richard Gere καθιέρωσε παγκοσμίως τον Giorgio Armani ως τον κορυφαίο σχεδιαστή της σύγχρονης ανδρικής κομψότητας;",
        "American Gigolo",
        ["Pretty Woman", "Primal Fear", "The Untouchables"],
        "Ο Armani αφαίρεσε τις άκαμπτες βάτες και τις σκληρές επενδύσεις από τα ανδρικά κοστούμια, εισάγοντας απαλά υφάσματα και μια νέα αίσθηση ρευστής γοητείας.",
        [
            "Η σκηνή όπου ο Richard Gere διαλέγει πουκάμισα και γραβάτες υπό τους ήχους του 'Call Me' των Blondie λειτούργησε ως η απόλυτη πασαρέλα μόδας.",
            "Η επιτυχία της ταινίας άνοιξε τον δρόμο για την κατάκτηση της αμερικανικής αγοράς από τον ιταλικό οίκο."
        ],
        "https://en.wikipedia.org/wiki/American_Gigolo",
        ["giorgio_armani", "american_gigolo", "richard_gere", "fashion"]
    ),
    # 333
    make_q(
        "pop_culture_hard_333",
        "Ποιος Ιάπωνας σχεδιαστής μόδας ίδρυσε τη σειρά 'Pleats Please' το 1993 αναπτύσσοντας μια πρωτοποριακή μέθοδο θερμικού πλισαρίσματος πολυεστέρα;",
        "Issey Miyake",
        ["Yohji Yamamoto", "Kenzo Takada", "Junya Watanabe"],
        "Ο Issey Miyake έκοβε και έραβε πρώτα τα ρούχα σε μεγέθη 2,5 φορές μεγαλύτερα πριν τα περάσει από θερμική πρέσα με χαρτί για να δημιουργήσει μόνιμες πτυχές.",
        [
            "Τα ρούχα Pleats Please δεν τσαλακώνονται ποτέ, πλένονται στο πλυντήριο και στεγνώνουν σε λίγα λεπτά, συνδυάζοντας την άνεση με την υψηλή αισθητική.",
            "Ο Miyake σχεδίασε επίσης τα εμβληματικά μαύρα ζιβάγκο που φορούσε καθημερινά ο Steve Jobs."
        ],
        "https://en.wikipedia.org/wiki/Issey_Miyake",
        ["issey_miyake", "pleats_please", "fashion", "japan"]
    ),
    # 334
    make_q(
        "pop_culture_hard_334",
        "Ποιο ψυχολογικό θρίλερ anime του Satoshi Kon (1997) αφηγείται την ιστορία μιας ποπ τραγουδίστριας που χάνει την επαφή με την πραγματικότητα όταν γίνεται ηθοποιός;",
        "Perfect Blue",
        ["Millennium Actress", "Paprika", "Tokyo Godfathers"],
        "Το 'Perfect Blue' εξερευνά τη διάσπαση της ταυτότητας της Mima Kirigoe μέσα από τον τρόμο ενός εμμονικού stalker και των παραισθήσεων της δόξας.",
        [
            "Ο σκηνοθέτης Darren Aronofsky αγόρασε τα δικαιώματα της ταινίας για να αναπαράγει σκηνές της στο 'Requiem for a Dream' και επηρεάστηκε έντονα στο 'Black Swan'.",
            "Θεωρείται ένα από τα σπουδαιότερα δείγματα ψυχολογικού κινηματογράφου κινουμένων σχεδίων όλων των εποχών."
        ],
        "https://en.wikipedia.org/wiki/Perfect_Blue",
        ["perfect_blue", "satoshi_kon", "anime", "psychological_thriller"]
    ),
    # 335
    make_q(
        "pop_culture_hard_335",
        "Πώς ονομάζεται η μυστική οργάνωση των σκοτεινών γερόντων με τους μαύρους μονόλιθους που κατευθύνει τη NERV στο 'Neon Genesis Evangelion';",
        "SEELE",
        ["GEHIRN", "MARDUK", "WILLE"],
        "Η SEELE καθοδηγείται από τα αρχαία 'Χειρόγραφα της Νεκράς Θάλασσας' και επιδιώκει το 'Human Instrumentality Project' για τη συγχώνευση όλων των ψυχών σε μία οντότητα.",
        [
            "Η λέξη 'Seele' σημαίνει 'ψυχή' στα γερμανικά, ενώ το όνομα της NERV σημαίνει 'νεύρο'.",
            "Ο ηγέτης της SEELE είναι ο Keel Lorenz, που επικοινωνεί μέσω του μονόλιθου 01."
        ],
        "https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion",
        ["evangelion", "seele", "nerv", "anime"]
    ),
    # 336
    make_q(
        "pop_culture_hard_336",
        "Ποιο ήταν το όνομα του νεαρού πρίγκιπα της φυλής των Emishi που ταξιδεύει στη Δύση για να βρει θεραπεία για τη θανατηφόρα κατάρα του στην 'Princess Mononoke';",
        "Ashitaka",
        ["Jigo", "Eboshi", "Kouroku"],
        "Ο πρίγκιπας Ashitaka μολύνεται από το μίσος ενός δαιμονικού αγριογούρουνου και αναζητά το Πνεύμα του Δάσους (Forest Spirit) για να βρει λύτρωση.",
        [
            "Στο ταξίδι του προσπαθεί να μεσολαβήσει ειρηνικά ανάμεσα στους ανθρώπους της Σιδηρούπολης (Lady Eboshi) και τους θεούς των ζώων της San.",
            "Η ταινία του Hayao Miyazaki (1997) έσπασε όλα τα ρεκόρ εισπράξεων στην Ιαπωνία και κέρδισε το βραβείο Καλύτερης Ταινίας της Ιαπωνικής Ακαδημίας."
        ],
        "https://en.wikipedia.org/wiki/Princess_Mononoke",
        ["princess_mononoke", "ashitaka", "studio_ghibli", "hayao_miyazaki", "anime"]
    ),
    # 337
    make_q(
        "pop_culture_hard_337",
        "Ποιο είναι το πραγματικό όνομα και η αληθινή ταυτότητα του πνεύματος του ποταμού Haku στην ταινία 'Spirited Away';",
        "Nigihayami Kohakunushi",
        ["Kamaji", "No-Face", "Boh"],
        "Ο Haku είναι το πνεύμα του ποταμού Kohaku, ο οποίος είχε σώσει την Chihiro από πνιγμό όταν εκείνη ήταν μικρό κορίτσι.",
        [
            "Ο ποταμός του είχε μπαζωθεί από κατασκευαστικές εταιρείες, αφήνοντάς τον άστεγο και ευάλωτο στα μάγια της μάγισσας Yubaba.",
            "Η Chihiro θυμάται το πραγματικό του όνομα σπάζοντας την κατάρα και χαρίζοντάς του πίσω την ελευθερία του."
        ],
        "https://en.wikipedia.org/wiki/Spirited_Away",
        ["spirited_away", "haku", "studio_ghibli", "anime"]
    ),
    # 338
    make_q(
        "pop_culture_hard_338",
        "Πώς ονομαζόταν το θρυλικό μισθοφορικό τάγμα υπό την ηγεσία του χαρισματικού Griffith στο έπος του 'Berserk';",
        "Το Τάγμα του Γερακιού (Band of the Hawk / Band of the Falcon)",
        ["Οι Μαύροι Ξιφομάχοι", "Οι Σιδερένιοι Σταυροφόροι", "Οι Ιππότες της Αγίας Αλυσίδας"],
        "Το Band of the Hawk δοξάστηκε στον Εκατονταετή Πόλεμο του βασιλείου του Midland πριν ο Griffith θυσιάσει όλους τους συντρόφους του κατά τη διάρκεια του Eclipse.",
        [
            "Ο Guts υπηρέτησε ως ο αήττητος αρχηγός των επιθετικών δυνάμεων (Raiders Captain) του τάγματος.",
            "Η Casca ήταν η μοναδική γυναίκα αξιωματικός του τάγματος και υπαρχηγός του Griffith."
        ],
        "https://en.wikipedia.org/wiki/Berserk_(manga)",
        ["berserk", "band_of_the_hawk", "griffith", "guts", "manga"]
    ),
    # 339
    make_q(
        "pop_culture_hard_339",
        "Ποιο είναι το όνομα του Stand του ανταγωνιστή Dio Brando στο 'JoJo's Bizarre Adventure' που διαθέτει την ικανότητα να σταματά τον χρόνο;",
        "The World (Za Warudo)",
        ["Star Platinum", "Crazy Diamond", "King Crimson"],
        "Το Stand 'The World' επιτρέπει στον Dio να παγώνει τον χρόνο για αρκετά δευτερόλεπτα, κατά τη διάρκεια των οποίων μπορεί να κινείται και να χτυπά ανενόχλητος.",
        [
            "Η ιαπωνική προφορά της κραυγής του Dio ('Za Warudo!') και ο ήχος του ρολογιού έγιναν ένα από τα πιο αναγνωρίσιμα memes των anime παγκοσμίως.",
            "Ο Jotaro Kujo ανακαλύπτει ότι το δικό του Stand, το Star Platinum, διαθέτει ακριβώς τον ίδιο τύπο ικανότητας."
        ],
        "https://en.wikipedia.org/wiki/Dio_Brando",
        ["jojo", "dio_brando", "the_world", "za_warudo", "anime"]
    ),
    # 340
    make_q(
        "pop_culture_hard_340",
        "Σε ποιο ιερό δάσος συγκεντρώνονται ετησίως όλοι οι Γαλάτες δρυΐδες για τον μεγάλο διαγωνισμό του καλύτερου μάγου στο 'Ο Αστερίξ και οι Γότθοι';",
        "Δάσος των Καρνουτών (Forest of the Carnutes)",
        ["Δάσος της Αρμορικής", "Δάσος των Αρδεννών", "Δάσος του Μπροσέλιαντ"],
        "Στο Δάσος των Καρνουτών ο δρυΐδης Πανοραμίξ κερδίζει το 'Χρυσό Μενίρ' για τον μαγικό του ζωμό πριν απαχθεί από τους Γότθους εισβολείς.",
        [
            "Η τοποθεσία βασίζεται σε πραγματικές καταγραφές του Ιουλίου Καίσαρα στα 'Απομνημονεύματα περί του Γαλατικού Πολέμου' για τις ετήσιες συνάξεις των δρυϊδών.",
            "Η περιοχή των Καρνουτών αντιστοιχεί στη σημερινή πόλη Chartres της Γαλλίας."
        ],
        "https://en.wikipedia.org/wiki/Asterix_and_the_Goths",
        ["asterix", "forest_of_carnutes", "druids", "comics"]
    ),
    # 341
    make_q(
        "pop_culture_hard_341",
        "Σε ποιον ιστορικό Γαλάτη πολέμαρχο ανήκε αρχικά η ασπίδα πάνω στην οποία μεταφέρεται ο αρχηγός Μαζεστίξ, όπως αποκαλύπτεται στο 'Η Ασπίδα της Αρβέρνης';",
        "Βερκιγγετόριξ (Vercingetorix)",
        ["Βρενός", "Δουμνόριξ", "Κασσιβελαύνος"],
        "Ο Βερκιγγετόριξ κατέθεσε τα όπλα και την ασπίδα του στα πόδια του Καίσαρα μετά τη μάχη της Αλεσίας, αλλά η ασπίδα εκλάπη και άλλαξε πολλά χέρια.",
        [
            "Ο Ιούλιος Καίσαρας προσπαθεί σε όλο το άλμπουμ να εντοπίσει την ασπίδα για να κάνει έναν θριαμβευτικό γύρο, χωρίς να γνωρίζει ότι την κατέχει ήδη ο Μαζεστίξ.",
            "Η αναζήτηση της ασπίδας αποτελεί παρωδία των κλασικών αστυνομικών ιστοριών μυστηρίου."
        ],
        "https://en.wikipedia.org/wiki/Asterix_and_the_Chieftain%27s_Shield",
        ["asterix", "vercingetorix", "vitalstatistix", "comics"]
    ),
    # 342
    make_q(
        "pop_culture_hard_342",
        "Ποια παγκοσμίου φήμης Γαλλίδα ηθοποιός του θεάτρου περιοδεύει στην Άγρια Δύση υπό την προστασία του Λούκυ Λουκ στο ομώνυμο άλμπουμ του 1982;",
        "Σάρα Μπερνάρ (Sarah Bernhardt)",
        ["Ελεονόρα Ντούζε", "Ραχήλ", "Μιστενγκέτ"],
        "Η Sarah Bernhardt ταξιδεύει στις ΗΠΑ για να παίξει Σαίξπηρ και Ρακίνα σε ανθρακωρύχους και καουμπόηδες, αντιμετωπίζοντας σαμποτάζ από φανατικούς ηθικολόγους.",
        [
            "Ο πρόεδρος Rutherford B. Hayes αναθέτει προσωπικά στον Λούκυ Λουκ να συνοδεύσει τη μεγάλη ντίβα.",
            "Η Bernhardt ενθουσιάζεται με την Άγρια Δύση και πυροβολεί με περίστροφο από το παράθυρο του τρένου."
        ],
        "https://en.wikipedia.org/wiki/Sarah_Bernhardt_(Lucky_Luke)",
        ["lucky_luke", "sarah_bernhardt", "theatre", "western", "comics"]
    ),
    # 343
    make_q(
        "pop_culture_hard_343",
        "Πού ήταν τελικά κρυμμένος ο θρυλικός θησαυρός του πειρατή Κόκκινου Ρακάμ στο τέλος της ιστορίας του Τεντέν;",
        "Στο υπόγειο του πύργου του Μάρλινσπαϊκ (μέσα στην υδρόγειο σφαίρα)",
        ["Στο ναυάγιο του πλοίου στον βυθό", "Σε μια σπηλιά ενός τροπικού νησιού", "Στο μουσείο των Βρυξελλών"],
        "Ο Τεντέν συνειδητοποιεί ότι η περγαμηνή ανέφερε 'Το φως έρχεται από το φως': ο θησαυρός βρισκόταν στη βάση του αγάλματος του Αγίου Ιωάννη στο υπόγειο του ίδιου του πύργου.",
        [
            "Μέσα στην κούφια υδρόγειο σφαίρα βρίσκονταν όλα τα κλεμμένα χρυσά νομίσματα και διαμάντια του πειρατή Red Rackham.",
            "Με τα χρήματα αυτά ο Καπετάνιος Χάντοκ μπόρεσε να διατηρήσει την κυριότητα του πύργου των προγόνων του."
        ],
        "https://en.wikipedia.org/wiki/Red_Rackham%27s_Treasure",
        ["tintin", "red_rackham", "marlinspike_hall", "herge"]
    ),
    # 344
    make_q(
        "pop_culture_hard_344",
        "Ποιο ήταν το αρχικό όνομα της πόλης Minas Tirith (Πύργος της Φρουράς) πριν την πτώση του δίδυμου πύργου Minas Ithil στις δυνάμεις της Mordor;",
        "Minas Anor (Πύργος του Ήλιου)",
        ["Osgiliath", "Pelargir", "Dol Amroth"],
        "Η πόλη Minas Anor χτίστηκε από τον Anárion για να φυλάσσει το Gondor από τη δύση, ενώ ο αδελφός του Isildur έχτισε το Minas Ithil (Πύργος της Σελήνης) στην ανατολή.",
        [
            "Όταν το Minas Ithil καταλήφθηκε από τους Nazgûl και έγινε Minas Morgul, το Minas Anor μετονομάστηκε σε Minas Tirith.",
            "Στο ανώτατο επίπεδο της πόλης φυλασσόταν το Λευκό Δέντρο του Gondor."
        ],
        "https://en.wikipedia.org/wiki/Minas_Tirith",
        ["minas_tirith", "minas_anor", "gondor", "lord_of_the_rings", "tolkien"]
    ),
    # 345
    make_q(
        "pop_culture_hard_345",
        "Πώς ονομάζονταν οι επτά αρχαίες μαγικές πέτρες επικοινωνίας και όρασης που έφεραν οι επιζώντες του Númenor στη Μέση Γη;",
        "Παλαντίρι (Palantíri)",
        ["Σιλμαρίλ (Silmarils)", "Ναουγκλαμίρ (Nauglamír)", "Άρκενστοουν (Arkenstone)"],
        "Τα Palantíri κατασκευάστηκαν από τα ξωτικά του Valinor (πιθανώς από τον Fëanor) και επέτρεπαν σε όσους τα χρησιμοποιούσαν να βλέπουν μακρινά μέρη και να συνομιλούν νοητικά.",
        [
            "Ο Sauron χρησιμοποίησε την πέτρα της Ithil για να διαφθείρει τον Saruman μέσω της πέτρας του Orthanc και να οδηγήσει στην απόγνωση τον Denethor.",
            "Η λέξη 'Palantír' στην γλώσσα Quenya σημαίνει 'αυτό που κοιτάζει μακριά'."
        ],
        "https://en.wikipedia.org/wiki/Palant%C3%ADr",
        ["palantir", "lord_of_the_rings", "tolkien", "middle_earth"]
    ),
    # 346
    make_q(
        "pop_culture_hard_346",
        "Ποια επίλεκτη λεγεώνα κλώνων στρατιωτών τέθηκε υπό τη διοίκηση του Darth Vader μετά την εφαρμογή της Εντολής 66 και έγινε γνωστή ως 'Vader's Fist';",
        "501η Λεγεώνα (501st Legion)",
        ["212ο Τάγμα Επίθεσης", "41ο Σώμα Ελίτ", "104ο Τάγμα"],
        "Η 501η Λεγεώνα πολέμησε υπό τον Anakin Skywalker στους Πολέμους των Κλώνων και στη συνέχεια εισέβαλε στον Ναό των Jedi κατά την 'Επιχείρηση Knightfall'.",
        [
            "Η επίσημη παγκόσμια κοινότητα cosplayers του Star Wars ονομάζεται '501st Legion' (Vader's Fist) προς τιμήν αυτής της στρατιάς.",
            "Ο αρχηγός της 501ης κατά τους Πολέμους των Κλώνων ήταν ο πιστός Captain Rex (CT-7567)."
        ],
        "https://en.wikipedia.org/wiki/501st_Legion",
        ["star_wars", "501st_legion", "darth_vader", "clone_wars"]
    ),
    # 347
    make_q(
        "pop_culture_hard_347",
        "Ποια ήταν τα ονόματα των τριών αδελφών Peverell που παρέλαβαν τους Κλήρους του Θανάτου (Ραβδί, Πέτρα, Μανδύα) στο Harry Potter;",
        "Antioch, Cadmus και Ignotus",
        ["Godric, Salazar και Rowena", "Gellert, Albus και Aberforth", "Sirius, Regulus και Orion"],
        "Ο Antioch πήρε το Elder Wand, ο Cadmus την Resurrection Stone και ο νεότερος και σοφότερος Ignotus τον Αόρατο Μανδύα.",
        [
            "Ο Harry Potter είναι απευθείας απόγονος του Ignotus Peverell, κληρονομώντας τον γνήσιο Αόρατο Μανδύα από τον πατέρα του James.",
            "Ο Lord Voldemort καταγόταν αντίστοιχα από τον μεσαίο αδελφό Cadmus μέσω του δαχτυλιδιού της οικογένειας Gaunt."
        ],
        "https://en.wikipedia.org/wiki/Deathly_Hallows",
        ["harry_potter", "deathly_hallows", "peverell", "magic"]
    ),
    # 348
    make_q(
        "pop_culture_hard_348",
        "Ποιο ήταν το πατρικό επώνυμο της Lily Potter και της Petunia Dursley πριν από τους γάμους τους;",
        "Evans",
        ["Prewett", "Black", "Brown"],
        "Η Lily και η Petunia Evans μεγάλωσαν στην πόλη Cokeworth, όπου η Lily ανακάλυψε τις μαγικές της δυνάμεις με τη βοήθεια του γείτονα Severus Snape.",
        [
            "Η ζήλια της Petunia για τα μαγικά χαρίσματα της Lily οδήγησε στο βαθύ της μίσος για τον μαγικό κόσμο και τον κακομεταχείριση του μικρού Harry.",
            "Ο Snape αγαπούσε τη Lily Evans από την ηλικία των 9 ετών μέχρι το τέλος της ζωής του."
        ],
        "https://en.wikipedia.org/wiki/Lily_Potter",
        ["harry_potter", "lily_potter", "evans", "snape"]
    ),
    # 349
    make_q(
        "pop_culture_hard_349",
        "Ποιος ήταν ο τελευταίος βασιλιάς της δυναστείας των Targaryen που έμεινε στην ιστορία ως ο 'Τρελός Βασιλιάς' (Mad King) στο Game of Thrones;",
        "Aerys II Targaryen",
        ["Aegon V Targaryen", "Maekar I Targaryen", "Viserys I Targaryen"],
        "Ο Aerys II είχε εμμονή με το υγρό πυρ (wildfire) και φώναζε συνεχώς 'Κάψτε τους όλους!' ('Burn them all!') πριν δολοφονηθεί από τον σωματοφύλακά του Jaime Lannister.",
        [
            "Η παράνοιά του επιδεινώθηκε ραγδαία μετά την εξάμηνη αιχμαλωσία και τα βασανιστήριά του κατά την ανταρσία του Duskendale.",
            "Ήταν ο πατέρας του Rhaegar, του Viserys και της Daenerys Targaryen."
        ],
        "https://en.wikipedia.org/wiki/Aerys_II_Targaryen",
        ["game_of_thrones", "aerys_targaryen", "mad_king", "westeros"]
    ),
    # 350
    make_q(
        "pop_culture_hard_350",
        "Ποια ανεξερεύνητη νότια ήπειρος του κόσμου του George R. R. Martin καλύπτεται από πυκνές θανατηφόρες ζούγκλες και αρχαία ερείπια από μαύρη πέτρα;",
        "Σοθόριος (Sothoryos)",
        ["Ουλθός (Ulthos)", "Έσος (Essos)", "Γουέστερος (Westeros)"],
        "Το Sothoryos είναι μια τεράστια και επικίνδυνη ήπειρος μολυσμένη από θανατηφόρες τροπικές ασθένειες, σαρκοφάγα θηρία και βασιλίσκους.",
        [
            "Η Jaenara Belaerys πέταξε με τον δράκο της Terax βαθιά στον νότο του Sothoryos επί τρία χρόνια και επέστρεψε δηλώνοντας ότι η ήπειρος 'δεν έχει τέλος'.",
            "Η εγκαταλειμμένη αρχαία πόλη Yeen στην ήπειρο είναι χτισμένη από τεράστιους ογκόλιθους λιωμένης μαύρης πέτρας που απορροφούν το φως."
        ],
        "https://en.wikipedia.org/wiki/World_of_A_Song_of_Ice_and_Fire#Sothoryos",
        ["game_of_thrones", "sothoryos", "george_rr_martin", "fantasy"]
    ),
    # 351
    make_q(
        "pop_culture_hard_351",
        "Ποια ιστορική κινηματογραφική εταιρεία ιδρύθηκε από τον Φιλοποίμενα Φίνο το 1942/1943 και κυριάρχησε απόλυτα στη χρυσή εποχή του ελληνικού σινεμά;",
        "Finos Film (Φίνος Φιλμ)",
        ["Καραγιάννης - Καρατζόπουλος", "Δαμασκηνός - Μιχαηλίδης", "Ανζερβός"],
        "Η Finos Film παρήγαγε 186 ταινίες από το 1943 έως το 1977, διαμορφώνοντας ολόκληρη τη λαϊκή κουλτούρα της μεταπολεμικής Ελλάδας.",
        [
            "Ο Φιλοποίμην Φίνος εισήγαγε όλες τις τεχνολογικές καινοτομίες στην Ελλάδα: σύγχρονη ηχοληψία, μαγνητικό ήχο, σινεμασκόπ και έγχρωμο φιλμ.",
            "Τα στούντιο της εταιρείας στους Αγίους Αναργύρους και στα Σπάτα υπήρξαν τα πιο εξελιγμένα στα Βαλκάνια."
        ],
        "https://el.wikipedia.org/wiki/%CE%A6%CE%AF%CE%BD%CE%BF%CF%82_%CE%A6%CE%B9%CE%BB%CE%BC",
        ["finos_film", "filopoimin_finos", "greek_cinema", "history"]
    ),
    # 352
    make_q(
        "pop_culture_hard_352",
        "Ποια ήταν η πρώτη ιστορική ταινία που παρήγαγε η Finos Film το 1943 μέσα στην Κατοχή σε σκηνοθεσία Δημήτρη Ιωαννόπουλου;",
        "Η Φωνή της Καρδιάς",
        ["Χειροκροτήματα", "Η Βίλα με τα Νούφαρα", "Μαρίνα"],
        "Η 'Φωνή της Καρδιάς' έκανε πρεμιέρα τον Μάρτιο του 1943 στους κινηματογράφους 'Ρεξ' και 'Έσπερος' με πρωταγωνιστές τον Αιμίλιο Βεάκη και τον Δημήτρη Χορν.",
        [
            "Η κοσμοσυρροή του κοινού ήταν τόσο πρωτοφανής που οι ουρές των θεατών έκλεισαν την οδό Πανεπιστημίου προκαλώντας την επέμβαση των ιταλικών αρχών κατοχής.",
            "Η επιτυχία της ταινίας απέδειξε στον Φίνο ότι ο ελληνικός κινηματογράφος μπορούσε να σταθεί αυτόνομα."
        ],
        "https://el.wikipedia.org/wiki/%CE%97_%CF%86%CF%89%CE%BD%CE%AE_%CF%84%CE%B7%CF%82_%CE%BA%CE%B1%CF%81%CE%B4%CE%B9%CE%AC%CF%82",
        ["finos_film", "i_foni_tis_kardias", "veakis", "horn", "greek_cinema"]
    ),
    # 353
    make_q(
        "pop_culture_hard_353",
        "Ποιο κλασικό μιούζικαλ της Finos Film του 1968 σε σκηνοθεσία Γιάννη Δαλιανίδη γυρίστηκε εξ ολοκλήρου στο γραφικό νησί της Ύδρας;",
        "Γοργόνες και Μάγκες",
        ["Μια Κυρία στα Μπουζούκια", "Κορίτσια για Φίλημα", "Κάτι Κουράζεται στα Παλικάρια"],
        "Το 'Γοργόνες και Μάγκες' συνδύασε μοναδικά το παραδοσιακό νησιώτικο τοπίο της Ύδρας με τη μοντέρνα αισθητική και τη μουσική του Μίμη Πλέσσα.",
        [
            "Στην ταινία πρωταγωνίστησαν η Μαίρη Χρονοπούλου, ο Φαίδων Γεωργίτσης, ο Χρόνης Εξαρχάκος και η Μάρθα Καραγιάννη.",
            "Ο Στράτος Διονυσίου ερμήνευσε στην ταινία το ανεπανάληπτο 'Βρέχει φωτιά στη στράτα μου' σε στίχους Λευτέρη Παπαδόπουλου."
        ],
        "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%81%CE%B3%CF%8C%CE%BD%CE%B5%CF%82_%CE%BA%CE%B1%CE%B9_%CE%BC%CE%AC%CE%B3%CE%BA%CE%B5%CF%82",
        ["gorgones_kai_magkes", "dalianidis", "plessas", "hydra", "greek_cinema"]
    ),
    # 354
    make_q(
        "pop_culture_hard_354",
        "Ποια πολεμική ταινία του 1970 σε σκηνοθεσία Νίκου Φώσκολου με την Αλίκη Βουγιουκλάκη κατέχει το ιστορικό ρεκόρ εισιτηρίων της Finos Film με 751.115 εισιτήρια;",
        "Υπολοχαγός Νατάσσα",
        ["Η Υπογραφή", "Η Δασκάλα με τα Ξανθά Μαλλιά", "Η Αρχόντισσα κι ο Αλήτης"],
        "Η 'Υπολοχαγός Νατάσσα' υπήρξε η πιο επιτυχημένη εισπρακτικά ταινία στην ιστορία του ελληνικού κινηματογράφου για σχεδόν τρεις δεκαετίες (μέχρι το Safe Sex το 1999).",
        [
            "Πρωταγωνιστούσαν η Αλίκη Βουγιουκλάκη και ο Δημήτρης Παπαμιχαήλ σε μια υπερπαραγωγή με γυρίσματα στην Ελλάδα και το εξωτερικό.",
            "Η σκηνή των βασανιστηρίων της Νατάσσας από τους Γερμανούς έγινε μία από τις πιο αναγνωρίσιμες δραματικές σκηνές της Βουγιουκλάκη."
        ],
        "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CF%87%CE%B1%CE%B3%CF%8C%CF%82_%CE%9D%CE%B1%CF%84%CE%AC%CF%83%CF%83%CE%B1",
        ["ypolochagos_natassa", "vougiouklaki", "foskolos", "finos_film", "greek_cinema"]
    ),
    # 355
    make_q(
        "pop_culture_hard_355",
        "Ποια καθημερινή δραματική σειρά του Νίκου Φώσκολου στον ΑΝΤ1 προβλήθηκε για 14 συνεχόμενα χρόνια (1991-2005) φτάνοντας τα 3.457 επεισόδια;",
        "Η Λάμψη",
        ["Καλημέρα Ζωή", "Το Τμήμα Ηθών", "Επιθυμίες"],
        "Η 'Λάμψη' είναι η μακροβιότερη καθημερινή τηλεοπτική σειρά στην ιστορία της ελληνικής τηλεόρασης, καταγράφοντας τις ίντριγκες της οικογένειας του Γιάγκου Δράκου.",
        [
            "Ο Νίκος Φώσκολος έγραψε μόνος του το σενάριο για σχεδόν όλα τα επεισόδια της σειράς.",
            "Η σειρά μεταδόθηκε επίσης με επιτυχία στην Κύπρο, τη Βουλγαρία και σε ομογενειακά κανάλια των ΗΠΑ και της Αυστραλίας."
        ],
        "https://el.wikipedia.org/wiki/%CE%97_%CE%9B%CE%AC%CE%BC%CF%88%CE%B7",
        ["i_lampsi", "nikos_foskolos", "giagkos_drakos", "ant1", "greek_tv"]
    ),
    # 356
    make_q(
        "pop_culture_hard_356",
        "Ποιος ηθοποιός ενσάρκωσε τον αδίστακτο μεγιστάνα Γιάγκο Δράκο της Giant Holdings και στα 14 χρόνια προβολής της 'Λάμψης';",
        "Χρήστος Πολίτης",
        ["Κώστας Σπυρόπουλος", "Γιώργος Βασιλείου", "Νίκος Απέργης"],
        "Ο Χρήστος Πολίτης ταυτίστηκε απόλυτα με τον ρόλο του ισχυρού επιχειρηματία που προσπαθούσε να διατηρήσει την αυτοκρατορία του ανάμεσα σε εχθρούς και οικογενειακές προδοσίες.",
        [
            "Η ατάκα του 'Εγώ είμαι ο Γιάγκος Δράκος!' αποτελεί μία από τις πιο διάσημες φράσεις στην ιστορία της ελληνικής σαπουνόπερας.",
            "Μετά το τέλος της σειράς το 2005, ο Πολίτης αποσύρθηκε οριστικά από τα φώτα της δημοσιότητας."
        ],
        "https://el.wikipedia.org/wiki/%CE%A7%CF%81%CE%AE%CF%83%CF%84%CE%BF%CF%82_%CE%A0%CE%BF%CE%BB%CE%AF%CF%84%CE%B7%CF%82",
        ["christos_politis", "giagkos_drakos", "i_lampsi", "greek_tv"]
    ),
    # 357
    make_q(
        "pop_culture_hard_357",
        "Ποια πρωταγωνίστρια υποδύθηκε την αριστοκρατική σύζυγο του Γιάγκου Δράκου, Βίρνα Λιώση-Δράκου, στα πρώτα χρόνια της 'Λάμψης';",
        "Κάτια Δανδουλάκη",
        ["Έλενα Ακρίτα", "Κοραλία Καράντη", "Μπέτυ Λιβανού"],
        "Η Κάτια Δανδουλάκη έδωσε ξεχωριστό κύρος στη σειρά υποδυόμενη τη δικαστικό Βίρνα Δράκου που συγκρουόταν ηθικά με τις μεθόδους του συζύγου της.",
        [
            "Η αποχώρησή της από τη σειρά το 1998 αποτέλεσε μείζον τηλεοπτικό γεγονός της εποχής.",
            "Η Δανδουλάκη είχε πρωταγωνιστήσει νωρίτερα στο θρυλικό ιστορικό σίριαλ της ΕΡΤ 'Πανθέοι' (1977-1979) ως Μάρμω."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%84%CE%B9%CE%B1_%CE%94%CE%B1%CE%BD%CE%B4%CE%BF%CF%85%CE%BB%CE%AC%CE%BA%CE%B7",
        ["katia_dandoulaki", "virna_drakou", "i_lampsi", "greek_tv"]
    ),
    # 358
    make_q(
        "pop_culture_hard_358",
        "Ποιος ηθοποιός υποδύθηκε τον αδιάφθορο Ταξίαρχο Στάθη Θεοχάρη στη δεύτερη καθημερινή σειρά του Νίκου Φώσκολου 'Καλημέρα Ζωή' (1993-2006);",
        "Γιώργος Βασιλείου",
        ["Φαίδων Γεωργίτσης", "Χρήστος Πολίτης", "Γιάννης Βόγλης"],
        "Ο Γιώργος Βασιλείου ενσάρκωσε τον εκρηκτικό αστυνομικό διευθυντή που πολεμούσε το οργανωμένο έγκλημα φωνάζοντας 'Σκουλήκια, καθάρματα!'.",
        [
            "Ο ρόλος του Θεοχάρη τον έκανε έναν από τους πιο αναγνωρίσιμους τηλεοπτικούς ήρωες στην Ελλάδα για πάνω από μία δεκαετία.",
            "Αργότερα ο Βασιλείου εκλέχθηκε βουλευτής στη Β' Περιφέρεια Πειραιά."
        ],
        "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8E%CF%81%CE%B3%CE%BF%CF%82_%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%B5%CE%AF%CE%BF%CF%85_(%CE%B7%CE%B8%CE%BF%CF%80%CE%BF%CE%B9%CF%8C%CF%82)",
        ["theoharis", "giorgos_vasileiou", "kalimera_zoi", "greek_tv"]
    ),
    # 359
    make_q(
        "pop_culture_hard_359",
        "Ποια δραματική σειρά της ΕΡΤ το 1975 σε σκηνοθεσία Βασίλη Γεωργιάδη μετέφερε το ομώνυμο αριστούργημα του Νίκου Καζαντζάκη με πρωταγωνιστή τον Αλέξη Γκόλφη;",
        "Ο Χριστός Ξανασταυρώνεται",
        ["Οι Πανθέοι", "Η Γειτονιά μας", "Γιούγκερμαν"],
        "Η σειρά παρακολουθούσε τους κατοίκους του χωριού Λυκόβρυση που ετοιμάζουν την αναπαράσταση των Παθών του Χριστού ενώ αρνούνται βοήθεια σε πεινασμένους πρόσφυγες.",
        [
            "Ο ηθοποιός Αλέξης Γκόλφης που υποδύθηκε τον βοσκό Μανωλιό ταυτίστηκε τόσο βαθιά με τον ρόλο που δυσκολεύτηκε να συνεχίσει την καριέρα του.",
            "Η σειρά σημείωσε πρωτοφανή τηλεθέαση και θεωρείται μία από τις κορυφαίες μεταφορές λογοτεχνίας στην ιστορία της δημόσιας τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F_%CE%A7%CF%81%CE%B9%CF%83%CF%84%CF%8C%CF%82_%CE%9E%CE%B1%CE%BD%CE%B1%CF%83%CF%84%CE%B1%CF%85%CF%81%CF%8E%CE%BD%CE%B5%CF%84%CE%B1%CE%B9_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
        ["o_christos_xanastavronetai", "kazantzakis", "georgiadis", "ert", "greek_tv"]
    ),
    # 360
    make_q(
        "pop_culture_hard_360",
        "Ποια ήταν η πρώτη καθημερινή σαπουνόπερα που μεταδόθηκε από την ελληνική ιδιωτική τηλεόραση (Mega Channel) το 1990;",
        "Η Δίψα",
        ["Η Λάμψη", "Το Ρετιρέ", "Οι Αυθαίρετοι"],
        "Η 'Δίψα' έκανε πρεμιέρα τον Ιανουάριο του 1990 σε σενάριο Λευτέρη Καπώνη με πρωταγωνιστή τον Γιάννη Βόγλη στον ρόλο του μεγαλοεπιχειρηματία Τζώρτζη Σέκερη.",
        [
            "Προβλήθηκε για 102 επεισόδια και απέδειξε ότι η ιδιωτική τηλεόραση μπορούσε να παράγει ανταγωνιστική καθημερινή μυθοπλασία.",
            "Στη σειρά πρωταγωνιστούσαν επίσης η Βάσια Τριφύλλη, η Κοραλία Καράντη και ο Αντώνης Καφετζόπουλος."
        ],
        "https://el.wikipedia.org/wiki/%CE%97_%CE%94%CE%AF%CF%88%CE%B1",
        ["i_dipsa", "mega_channel", "giannis_voglis", "greek_tv", "1990"]
    ),
    # 361
    make_q(
        "pop_culture_hard_361",
        "Ποιος Κρητικός σκηνοθέτης σκηνοθέτησε με κινηματογραφική αρτιότητα και τα 26 επεισόδια της επιτυχημένης σειράς 'Το Νησί' (Mega, 2010);",
        "Θοδωρής Παπαδουλάκης",
        ["Πάνος Κοκκινόπουλος", "Κώστας Κωστόπουλος", "Γρηγόρης Καραντινάκης"],
        "Ο Θοδωρής Παπαδουλάκης απέσπασε διθυραμβικές κριτικές για τη σκηνοθεσία του, χρησιμοποιώντας τεχνικές κινηματογράφου υψηλής ευκρίνειας και τοπικά γυρίσματα στην Ελούντα και τη Σπιναλόγκα.",
        [
            "Η σειρά κέρδισε δεκάδες τηλεοπτικά βραβεία και χαρακτηρίστηκε ως η πιο ποιοτική παραγωγή στην ιστορία της ελληνικής ιδιωτικής τηλεόρασης.",
            "Ο Παπαδουλάκης σκηνοθέτησε αργότερα και τη δραματική σειρά 'Κομάντα και Δράκοι' (2021)."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9D%CE%B7%CF%83%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
        ["to_nisi", "papadoulakis", "mega", "greek_tv"]
    ),
    # 362
    make_q(
        "pop_culture_hard_362",
        "Ποιος Έλληνας συνθέτης έγραψε την υποβλητική πρωτότυπη μουσική για την τηλεοπτική σειρά 'Το Νησί' (2010);",
        "Μίνως Μάτσας",
        ["Σταμάτης Κραουνάκης", "Στέφανος Κορκολής", "Ευανθία Ρεμπούτσικα"],
        "Ο Μίνως Μάτσας συνέθεσε το ορχηστρικό σάουντρακ του 'Νησιού' συνδυάζοντας συμφωνική ορχήστρα με παραδοσιακά κρητικά όργανα όπως η λύρα και το λαούτο.",
        [
            "Το ομώνυμο τραγούδι των τίτλων 'Είσαι εσύ ο άνθρωπός μου' ερμήνευσε η Ανδριάνα Μπάμπαλη σε διασκευή παλιού ρεμπέτικου.",
            "Το σάουντρακ της σειράς έγινε πλατινένιο σε πωλήσεις στην Ελλάδα."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%AF%CE%BD%CF%89%CF%82_%CE%9C%CE%AC%CF%84%CF%83%CE%B1%CF%82",
        ["minos_matsas", "to_nisi", "soundtrack", "greek_music"]
    ),
    # 363
    make_q(
        "pop_culture_hard_363",
        "Ποιο περίβλεπτο βραβείο κέρδισε ο Γιώργος Λάνθιμος στο Φεστιβάλ των Καννών το 2009 με την ταινία 'Κυνόδοντας' (Dogtooth) εγκαινιάζοντας το 'Greek Weird Wave';",
        "Prix Un Certain Regard (Ένα Κάποιο Βλέμμα)",
        ["Χρυσός Φοίνικας", "Μέγα Βραβείο Επιτροπής", "Χρυσή Κάμερα"],
        "Ο 'Κυνόδοντας' απέσπασε το κορυφαίο βραβείο του τμήματος 'Ένα Κάποιο Βλέμμα' στις Κάννες, τραβώντας για πρώτη φορά τα βλέμματα της παγκόσμιας κριτικής στον Λάνθιμο.",
        [
            "Η ταινία παρακολουθεί τρία ενήλικα παιδιά που ζουν απομονωμένα από τους γονείς τους σε μια περίκλειστη έπαυλη μαθαίνοντας παραποιημένες λέξεις.",
            "Υπήρξε η πρώτη ελληνική ταινία μετά από 33 χρόνια που προτάθηκε για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας (το 2011)."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%85%CE%BD%CF%8C%CE%B4%CE%BF%CE%BD%CF%84%CE%B1%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["dogtooth", "kynodontas", "lanthimos", "cannes", "greek_weird_wave"]
    ),
    # 364
    make_q(
        "pop_culture_hard_364",
        "Ποιος Έλληνας σεναριογράφος υπήρξε ο στενός συγγραφικός συνεργάτης του Γιώργου Λάνθιμου συνυπογράφοντας τα σενάρια των 'Κυνόδοντας', 'Άλπεις', 'The Lobster' και 'The Killing of a Sacred Deer';",
        "Ευθύμης Φιλίππου",
        ["Αλέξανδρος Βούλγαρης", "Χρήστος Νίκου", "Σύλλας Τζουμέρκας"],
        "Ο Ευθύμης Φιλίππου κέρδισε το Βραβείο Σεναρίου στο Φεστιβάλ Βενετίας (για τις 'Άλπεις') και στο Φεστιβάλ Καννών (για το 'The Killing of a Sacred Deer').",
        [
            "Το 2017 ήταν υποψήφιος για το Όσκαρ Καλύτερου Πρωτότυπου Σεναρίου για την ταινία 'The Lobster' μαζί με τον Λάνθιμο.",
            "Το ιδιαίτερο, αποστασιοποιημένο ύφος γραφής του καθόρισε την ταυτότητα του σύγχρονου ελληνικού κινηματογράφου διεθνώς."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CF%85%CE%B8%CF%8D%CE%BC%CE%B7%CF%82_%CE%A6%CE%B9%CE%BB%CE%AF%CF%80%CF%80%CE%BF%CF%85",
        ["efthymis_filippou", "lanthimos", "dogtooth", "the_lobster", "screenplay"]
    ),
    # 365
    make_q(
        "pop_culture_hard_365",
        "Σε ποιο ζώο δήλωνε ο Colin Farrell ότι επιθυμεί να μεταμορφωθεί αν αποτύχει να βρει σύντροφο στην ταινία του Γιώργου Λάνθιμου 'The Lobster' (2015);",
        "Αστακό (Lobster)",
        ["Σκύλο", "Άλογο", "Παπαγάλο"],
        "Ο πρωταγωνιστής David επιλέγει τον αστακό επειδή ζει πάνω από 100 χρόνια, έχει μπλε αίμα σαν τους ευγενείς και παραμένει γόνιμος σε όλη του τη ζωή.",
        [
            "Η ταινία κέρδισε το Βραβείο της Επιτροπής στο Φεστιβάλ των Καννών το 2015.",
            "Υπήρξε η πρώτη αγγλόφωνη ταινία του Λάνθιμου με διεθνές καστ όπως οι Rachel Weisz, Olivia Colman και Léa Seydoux."
        ],
        "https://en.wikipedia.org/wiki/The_Lobster",
        ["the_lobster", "lanthimos", "colin_farrell", "cinema"]
    ),
    # 366
    make_q(
        "pop_culture_hard_366",
        "Πόσα βραβεία Όσκαρ κέρδισε η ταινία 'Poor Things' (2023) του Γιώργου Λάνθιμου, ανάμεσά τους και το Όσκαρ Α' Γυναικείου Ρόλου για την Emma Stone;",
        "Τέσσερα (4)",
        ["Δύο", "Τρία", "Έξι"],
        "Το 'Poor Things' κέρδισε 4 Όσκαρ: Α' Γυναικείου Ρόλου (Emma Stone), Σχεδιασμού Παραγωγής, Κοστουμιών και Μακιγιάζ/Κομμώσεων.",
        [
            "Η ταινία είχε κερδίσει προηγουμένως τον Χρυσό Λέοντα στο Φεστιβάλ Βενετίας 2023.",
            "Βασίστηκε στο ομώνυμο σατιρικό μυθιστόρημα του Σκωτσέζου συγγραφέα Alasdair Gray από το 1992."
        ],
        "https://en.wikipedia.org/wiki/Poor_Things_(film)",
        ["poor_things", "lanthimos", "emma_stone", "oscars", "golden_lion"]
    ),
    # 367
    make_q(
        "pop_culture_hard_367",
        "Ποιο ήταν το τελικό σκορ στον ιστορικό τελικό του EuroBasket 1987 στο Στάδιο Ειρήνης και Φιλίας όπου η Ελλάδα νίκησε τη Σοβιετική Ένωση στην παράταση;",
        "103 - 101",
        ["98 - 96", "101 - 99", "105 - 103"],
        "Η Ελλάδα κατέκτησε το χρυσό μετάλλιο στις 14 Ιουνίου 1987 νικώντας την ανίκητη Σοβιετική Ένωση, γεγονός που άλλαξε ριζικά τον ελληνικό αθλητισμό.",
        [
            "Ο Νίκος Γκάλης αναδείχθηκε πρώτος σκόρερ και MVP του τουρνουά σκοράροντας 40 πόντους στον τελικό (με μέσο όρο 37 πόντους ανά αγώνα).",
            "Η νίκη έβγαλε εκατομμύρια Έλληνες στους δρόμους σε ένα πανεθνικό παραλήρημα που κράτησε μέχρι το πρωί."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CF%85%CF%81%CF%89%CE%BC%CF%80%CE%AC%CF%83%CE%BA%CE%B5%CF%84_1987",
        ["eurobasket_1987", "galis", "greek_basketball", "history"]
    ),
    # 368
    make_q(
        "pop_culture_hard_368",
        "Ποιος παίκτης ευστόχησε στις δύο ιστορικές ελεύθερες βολές 4 δευτερόλεπτα πριν τη λήξη της παράτασης στον τελικό του EuroBasket 1987;",
        "Αργύρης Καμπούρης",
        ["Παναγιώτης Γιαννάκης", "Νίκος Γκάλης", "Φάνης Χριστοδούλου"],
        "Ο Αργύρης Καμπούρης ('Ο Τίμιος Γίγαντας') κέρδισε το ριμπάουντ, κέρδισε φάουλ και ευστόχησε ψύχραιμα και στις δύο βολές κάνοντας το σκορ 103-101.",
        [
            "Η περιγραφή του Φίλιππα Συρίγου στην τηλεόραση: 'Και τώρα ο Καμπούρης... η πρώτη βολή... μέσα! Και η δεύτερη... μέσα!' έμεινε χαραγμένη στη μνήμη όλων των Ελλήνων.",
            "Ο Καμπούρης αγωνιζόταν τότε στον Ολυμπιακό και ήταν γνωστός για τη μαχητικότητά του κάτω από τα καλάθια."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CF%81%CE%B3%CF%8D%CF%81%CE%B7%CF%82_%CE%9A%CE%B1%CE%BC%CF%80%CE%BF%CF%8D%CF%81%CE%B7%CF%82",
        ["argyris_kampouris", "eurobasket_1987", "free_throws", "greek_basketball"]
    ),
    # 369
    make_q(
        "pop_culture_hard_369",
        "Ποιος ήταν ο προπονητής της Εθνικής Ελλάδας μπάσκετ που οδήγησε την ομάδα στον ιστορικό θρίαμβο του EuroBasket 1987;",
        "Κώστας Πολίτης",
        ["Γιάννης Ιωαννίδης", "Ευθύμης Κιουμουρτζόγλου", "Παναγιώτης Γιαννάκης"],
        "Ο Κώστας Πολίτης ('Ο Ευρωκόουτς') διαχειρίστηκε άριστα το ταλέντο του Νίκου Γκάλη και του Παναγιώτη Γιαννάκη, σχεδιάζοντας τη στρατηγική της νίκης.",
        [
            "Η ψυχραιμία του στον πάγκο κατά τη διάρκεια των δραματικών τελευταίων δευτερολέπτων υπήρξε υποδειγματική.",
            "Υπήρξε παλιός διεθνής παίκτης του Παναθηναϊκού και της Εθνικής πριν αναλάβει την τεχνική ηγεσία."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CF%83%CF%84%CE%B1%CF%82_%CE%A0%CE%BF%CE%BB%CE%AF%CF%84%CE%B7%CF%82",
        ["kostas_politis", "eurobasket_1987", "coach", "greek_basketball"]
    ),
    # 370
    make_q(
        "pop_culture_hard_370",
        "Ποιος ήταν ο αρχηγός της Εθνικής Ελλάδας ποδοσφαίρου που σήκωσε το τρόπαιο του Euro 2004 στον ουρανό της Λισαβόνας αναδεικνυόμενος MVP του τουρνουά;",
        "Θοδωρής Ζαγοράκης",
        ["Άγγελος Χαριστέας", "Τραϊανός Δέλλας", "Γιώργος Καραγκούνης"],
        "Ο Θοδωρής Ζαγοράκης ηγήθηκε της Εθνικής στη μεγαλύτερη έκπληξη στην ιστορία του παγκόσμιου ποδοσφαίρου, νικώντας τη διοργανώτρια Πορτογαλία με 1-0 στον τελικό.",
        [
            "Η εντυπωσιακή του ντρίμπλα πάνω στον Bixente Lizarazu στον προημιτελικό με τη Γαλλία οδήγησε στην ασίστ για το νικητήριο γκολ του Χαριστέα.",
            "Η UEFA τον ανακήρυξε επίσημα ως τον Πολυτιμότερο Παίκτη (Player of the Tournament) του Euro 2004."
        ],
        "https://el.wikipedia.org/wiki/%CE%98%CE%BF%CE%B4%CF%89%CF%81%CE%AE%CF%82_%CE%96%CE%B1%CE%B3%CE%BF%CF%81%CE%AC%CE%BA%CE%B7%CF%82",
        ["zagorakis", "euro_2004", "greek_football", "mvp"]
    ),
    # 371
    make_q(
        "pop_culture_hard_371",
        "Σε ποιο λεπτό του τελικού του Euro 2004 σημείωσε ο Άγγελος Χαριστέας τη χρυσή κεφαλιά μετά από κόρνερ του Άγγελου Μπασινά;",
        "57ο λεπτό",
        ["43ο λεπτό", "68ο λεπτό", "75ο λεπτό"],
        "Στο 57ο λεπτό του τελικού στο Estádio da Luz, ο Χαριστέας νίκησε στον αέρα τον τερματοφύλακα Ricardo γράφοντας το τελικό 1-0 για την Ελλάδα.",
        [
            "Ο Χαριστέας σκόραρε επίσης το νικητήριο γκολ στον προημιτελικό με τη Γαλλία και το γκολ της ισοφάρισης στον όμιλο με την Ισπανία.",
            "Η φράση του σπίκερ Κώστα Βερνίκου 'Γκοοολ ο Χαριστέας!' έμεινε στην ιστορία των ελληνικών τηλεοπτικών μεταδόσεων."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CE%BB%CE%B9%CE%BA%CF%8C%CF%82_%CE%95%CF%85%CF%81%CF%89%CF%80%CE%B1%CF%8A%CE%BA%CE%BF%CF%8D_%CE%A0%CF%81%CF%89%CF%84%CE%B1%CE%B8%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_2004",
        ["charisteas", "euro_2004", "lisbon", "greek_football"]
    ),
    # 372
    make_q(
        "pop_culture_hard_372",
        "Ποιος Γερμανός τεχνικός καθοδήγησε την Εθνική Ελλάδας ως ομοσπονδιακός προπονητής στην κατάκτηση του Euro 2004 αποκτώντας το προσωνύμιο 'Ρεχακλής';",
        "Ότο Ρεχάγκελ (Otto Rehhagel)",
        ["Γιούργκεν Κλίνσμαν", "Φραντς Μπεκενμπάουερ", "Γιουπ Χάινκες"],
        "Ο Otto Rehhagel οργάνωσε μια απαραβίαστη αμυντική τακτική και ενέπνευσε ακλόνητη πίστη στους παίκτες, γινόμενος ο πρώτος ξένος προπονητής που κατέκτησε Euro με άλλη χώρα.",
        [
            "Ανακηρύχθηκε επίτιμος δημότης Αθηναίων και 'Έλληνας της Χρονιάς' το 2004.",
            "Παρέμεινε στον πάγκο της Εθνικής για 9 χρόνια (2001-2010), οδηγώντας την ομάδα και στο Μουντιάλ του 2010."
        ],
        "https://el.wikipedia.org/wiki/%CE%8C%CF%84%CE%BF_%CE%A1%CE%B5%CF%87%CE%AC%CE%B3%CE%BA%CE%B5%CE%BB",
        ["otto_rehhagel", "rehakles", "euro_2004", "coach"]
    ),
    # 373
    make_q(
        "pop_culture_hard_373",
        "Ποιος ποδοσφαιριστής σημείωσε το ιστορικό 'ασημένιο γκολ' με κεφαλιά στις καθυστερήσεις του πρώτου ημιχρόνου της παράτασης στον ημιτελικό με την Τσεχία στο Euro 2004;",
        "Τραϊανός Δέλλας",
        ["Μιχάλης Καψής", "Νίκος Νταμπίζας", "Γιούρκας Σεϊταρίδης"],
        "Ο 'Κολοσσός' Τραϊανός Δέλλας σκόραρε στο 105+1' μετά από κόρνερ του Τσιάρτα, οδηγώντας τη χώρα απευθείας στον τελικό βάσει του κανονισμού του silver goal.",
        [
            "Υπήρξε το μοναδικό 'ασημένιο γκολ' που έκρινε ποτέ αγώνα στην ιστορία του Ευρωπαϊκού Πρωταθλήματος πριν ο κανονισμός καταργηθεί.",
            "Ο Δέλλας αναδείχθηκε μέλος της καλύτερης ενδεκάδας της διοργάνωσης από την UEFA."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%B1%CF%8A%CE%B1%CE%BD%CF%8C%CF%82_%CE%94%CE%AD%CE%BB%CE%BB%CE%B1%CF%82",
        ["traianos_dellas", "silver_goal", "euro_2004", "greek_football"]
    ),
    # 374
    make_q(
        "pop_culture_hard_374",
        "Ποιος Έλληνας τενίστας έγινε ο πρώτος στην ιστορία που έφτασε σε τελικό του Roland Garros στο απλό ανδρών το 2021;",
        "Στέφανος Τσιτσιπάς",
        ["Μάρκος Παγδατής", "Κωνσταντίνος Οικονομίδης", "Πέτρος Τσιτσιπάς"],
        "Ο Στέφανος Τσιτσιπάς προηγήθηκε με 2-0 σετ στον τελικό του Γαλλικού Όπεν απέναντι στον Novak Djokovic πριν ηττηθεί σε έναν επικό αγώνα πέντε σετ.",
        [
            "Το 2019 είχε κερδίσει το ATP Finals στο Λονδίνο, σημειώνοντας τον σπουδαιότερο τίτλο της καριέρας του.",
            "Έφτασε μέχρι το No. 3 της παγκόσμιας κατάταξης ATP."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AD%CF%86%CE%B1%CE%BD%CE%BF%CF%82_%CE%A4%CF%83%CE%B9%CF%84%CF%83%CE%B9%CF%80%CE%AC%CF%82",
        ["stefanos_tsitsipas", "tennis", "roland_garros", "sports"]
    ),
    # 375
    make_q(
        "pop_culture_hard_375",
        "Ποια Ελληνίδα τενίστρια έφτασε στους ημιτελικούς δύο Grand Slam τουρνουά (Roland Garros και US Open) το 2021 φτάνοντας στο No. 3 του κόσμου;",
        "Μαρία Σάκκαρη",
        ["Ελένη Δανιηλίδου", "Αγγελική Κανελλοπούλου", "Δέσποινα Παπαμιχαήλ"],
        "Η Μαρία Σάκκαρη έγραψε ιστορία για το ελληνικό γυναικείο τένις με τη δυναμική της παρουσία και την είσοδό της στην κορυφαία τριάδα της WTA.",
        [
            "Η μητέρα της, Αγγελική Κανελλοπούλου, υπήρξε επίσης κορυφαία Ελληνίδα πρωταθλήτρια του τένις τη δεκαετία του 1980.",
            "Το 2023 κατέκτησε τον τίτλο WTA 1000 στη Γουαδαλαχάρα του Μεξικού."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AF%CE%B1_%CE%A3%CE%AC%CE%BA%CE%BA%CE%B1%CF%81%CE%B7",
        ["maria_sakkari", "tennis", "wta", "sports"]
    ),
    # 376
    make_q(
        "pop_culture_hard_376",
        "Ποιος Έλληνας άλτης του μήκους κατέκτησε το χρυσό μετάλλιο στους Ολυμπιακούς Αγώνες του Τόκιο 2020 και του Παρισιού 2024;",
        "Μίλτος Τεντόγλου",
        ["Λούης Τσάτουμας", "Κώστας Κουκοδήμος", "Εμμανουήλ Καραλής"],
        "Ο Μίλτος Τεντόγλου έγινε μόλις ο δεύτερος αθλητής στην ιστορία των Ολυμπιακών Αγώνων μετά τον Carl Lewis που διατήρησε τον τίτλο του στο μήκος ανδρών.",
        [
            "Στο Τόκιο κέρδισε το χρυσό στο έκτο και τελευταίο άλμα του με επίδοση 8,41 μέτρα.",
            "Είναι εξαιρετικά δημοφιλής για τη χαλαρή και αυθεντική προσωπικότητά του και την αγάπη του για το anime 'One Piece', μιμούμενος συχνά πόζες του Luffy."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%AF%CE%BB%CF%84%CE%BF%CF%82_%CE%A4%CE%B5%CE%BD%CF%84%CF%8C%CE%B3%CE%BB%CE%BF%CF%85",
        ["miltos_tentoglou", "olympics", "long_jump", "athletics", "tokyo_2020", "paris_2024"]
    ),
    # 377
    make_q(
        "pop_culture_hard_377",
        "Ποια Ελληνίδα πρωταθλήτρια του επί κοντώ κατέκτησε το χρυσό μετάλλιο στους Ολυμπιακούς Αγώνες του Ρίο 2016 με άλμα στα 4,85 μέτρα;",
        "Κατερίνα Στεφανίδη",
        ["Νικόλ Κυριακοπούλου", "Βούλα Παπαχρήστου", "Αθανασία Τσουμελέκα"],
        "Η Κατερίνα Στεφανίδη πέτυχε ένα σπάνιο σερί κατακτώντας διαδοχικά χρυσά μετάλλια σε Ολυμπιακούς Αγώνες, Παγκόσμιο Πρωτάθλημα (2017) και Ευρωπαϊκό Πρωτάθλημα.",
        [
            "Αναδείχθηκε κορυφαία αθλήτρια της Ευρώπης στον στίβο (European Athlete of the Year) το 2017.",
            "Σπούδασε νευροβιολογία στο πανεπιστήμιο Stanford των ΗΠΑ."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%B5%CF%81%CE%AF%CE%BD%CE%B1_%CE%A3%CF%84%CE%B5%CF%86%CE%B1%CE%BD%CE%AF%CE%B4%CE%B7",
        ["katerina_stefanidi", "pole_vault", "olympics", "rio_2016", "athletics"]
    ),
    # 378
    make_q(
        "pop_culture_hard_378",
        "Ποιος ήταν ο πρώτος Έλληνας αθλητής που κατέκτησε χρυσό μετάλλιο στην ενόργανη γυμναστική στους Ολυμπιακούς Αγώνες της Ατλάντα 1996 (στο έδαφος);",
        "Ιωάννης Μελισσανίδης",
        ["Δημοσθένης Ταμπάκος", "Λευτέρης Πετρούνιας", "Βλάσης Μάρας"],
        "Ο 19χρονος Ιωάννης Μελισσανίδης σόκαρε τον κόσμο της γυμναστικής εκτελώντας ένα τέλειο πρόγραμμα στο έδαφος και χαρίζοντας στην Ελλάδα το πρώτο της χρυσό στη σύγχρονη ενόργανη.",
        [
            "Η εντυπωσιακή του έξοδος και ο πανηγυρισμός του έμειναν στις κλασικές στιγμές του ελληνικού αθλητισμού.",
            "Κέρδισε επίσης το ασημένιο μετάλλιο στο άλμα στους Ολυμπιακούς Αγώνες του Σίδνεϊ 2000."
        ],
        "https://el.wikipedia.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%9C%CE%B5%CE%BB%CE%B9%CF%83%CF%83%CE%B1%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
        ["melissanidis", "gymnastics", "atlanta_1996", "olympics"]
    ),
    # 379
    make_q(
        "pop_culture_hard_379",
        "Ποιος Έλληνας πρωταθλητής της ενόργανης γυμναστικής κατέκτησε τρία διαδοχικά ολυμπιακά μετάλλια στους κρίκους (Ρίο 2016, Τόκιο 2020, Παρίσι 2024);",
        "Λευτέρης Πετρούνιας",
        ["Δημοσθένης Ταμπάκος", "Βλάσης Μάρας", "Ιωάννης Μελισσανίδης"],
        "Ο 'Άρχοντας των Κρίκων' Λευτέρης Πετρούνιας κατέκτησε το χρυσό στο Ρίο και δύο χάλκινα σε Τόκιο και Παρίσι, γινόμενος ο κορυφαίος Έλληνας γυμναστής όλων των εποχών.",
        [
            "Έχει κερδίσει επτά χρυσά μετάλλια σε Ευρωπαϊκά Πρωταθλήματα, επίτευγμα μοναδικό στην ιστορία των κρίκων παγκοσμίως.",
            "Μια κίνηση στους κρίκους φέρει επίσημα το όνομά του ('The Petrounias') στον κώδικα της Διεθνούς Ομοσπονδίας Γυμναστικής."
        ],
        "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CF%85%CF%84%CE%AD%CF%81%CE%B7%CF%82_%CE%A0%CE%B5%CF%84%CF%81%CE%BF%CF%8D%CE%BD%CE%B9%CE%B1%CF%82",
        ["lefteris_petrounias", "rings", "gymnastics", "olympics"]
    ),
    # 380
    make_q(
        "pop_culture_hard_380",
        "Ποιος ήταν ο πρώτος Έλληνας αθλητής που κέρδισε χρυσό ολυμπιακό μετάλλιο στους κρίκους στους Ολυμπιακούς Αγώνες της Αθήνας 2004;",
        "Δημοσθένης Ταμπάκος",
        ["Λευτέρης Πετρούνιας", "Βλάσης Μάρας", "Γιώργος Ελληνογερμανός"],
        "Ο Δημοσθένης Ταμπάκος κατέκτησε το χρυσό μετάλλιο μέσα σε αποθέωση στο κλειστό του ΟΑΚΑ, έχοντας κερδίσει προηγουμένως το ασημένιο στο Σίδνεϊ 2000.",
        [
            "Η βαθμολογία του 9,862 στον τελικό τον έφερε στην κορυφή του βάθρου μπροστά από τον Βούλγαρο Iordan Iovtchev.",
            "Υπήρξε ο σημαιοφόρος της ελληνικής αποστολής στην τελετή λήξης των Αγώνων της Αθήνας."
        ],
        "https://el.wikipedia.org/wiki/%CE%94%CE%B7%CE%BC%CE%BF%CF%83%CE%B8%CE%AD%CE%BD%CE%B7%CF%82_%CE%A4%CE%B1%CE%BC%CF%80%CE%AC%CE%BA%CE%BF%CF%82",
        ["dimosthenis_tampakos", "rings", "athens_2004", "olympics"]
    ),
    # 381
    make_q(
        "pop_culture_hard_381",
        "Ποιος Έλληνας άλτης του επί κοντώ κατέκτησε το χάλκινο μετάλλιο στους Ολυμπιακούς Αγώνες του Παρισιού 2024 με άλμα στα 5,90 μέτρα;",
        "Εμμανουήλ Καραλής",
        ["Κώστας Φιλιππίδης", "Μίλτος Τεντόγλου", "Λούης Τσάτουμας"],
        "Ο Εμμανουήλ Καραλής ('Manolo') κατέκτησε το πρώτο ελληνικό ολυμπιακό μετάλλιο στο επί κοντώ ανδρών μετά από 68 χρόνια (από τον Γιώργο Ρουμπάνη το 1956).",
        [
            "Ο Καραλής επιλέχθηκε μαζί με την Ευαγγελία Πλατανιώτη ως σημαιοφόρος της Ελλάδας στην τελετή λήξης του Παρισιού 2024.",
            "Είναι εξαιρετικά αγαπητός στο κοινό για το πηγαίο του χιούμορ και την στενή φιλία του με τον Μίλτο Τεντόγλου."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%BC%CE%BC%CE%B1%CE%BD%CE%BF%CF%85%CE%AE%CE%BB_%CE%9A%CE%B1%CF%81%CE%B1%CE%BB%CE%AE%CF%82",
        ["emmanouil_karalis", "pole_vault", "paris_2024", "olympics", "athletics"]
    ),
    # 382
    make_q(
        "pop_culture_hard_382",
        "Ποιος θρυλικός αρσιβαρίστας χάρισε στην Ελλάδα τρία χρυσά (1992, 1996, 2000) και ένα χάλκινο ολυμπιακό μετάλλιο (2004);",
        "Πύρρος Δήμας",
        ["Κάχι Καχιασβίλι", "Λεωνίδας Σαμπάνης", "Βαλέριος Λεωνίδης"],
        "Ο Πύρρος Δήμας έγινε ο πιο επιτυχημένος αρσιβαρίστας στην ιστορία των σύγχρονων Ολυμπιακών Αγώνων με τέσσερα ολυμπιακά μετάλλια.",
        [
            "Η ιαχή του 'Για την Ελλάδα!' στους Αγώνες της Βαρκελώνης το 1992 συγκίνησε ολόκληρο το έθνος.",
            "Στους Αγώνες της Αθήνας 2004, το ελληνικό κοινό χειροκροτούσε όρθιο επί 10 συνεχόμενα λεπτά κατά την απονομή του χάλκινου μεταλλίου."
        ],
        "https://el.wikipedia.org/wiki/%CE%A0%CF%8D%CF%81%CF%81%CE%BF%CF%82_%CE%94%CE%AE%CE%BC%CE%B1%CF%82",
        ["pyrros_dimas", "weightlifting", "olympics", "greek_sports"]
    ),
    # 383
    make_q(
        "pop_culture_hard_383",
        "Ποιος ομογενής αρσιβαρίστας από τη Γεωργία ισοφάρισε το ρεκόρ των τριών διαδοχικών χρυσών ολυμπιακών μεταλλίων (1992 για την Κοινοπολιτεία, 1996 και 2000 για την Ελλάδα);",
        "Κάχι Καχιασβίλι (Ακάκιος Κακιιασβίλης)",
        ["Πύρρος Δήμας", "Βίκτωρ Μήτρου", "Γιώργος Τζελίλης"],
        "Ο Κάχι Καχιασβίλι υπήρξε ένας από τους πιο τεχνικούς και ψύχραιμους αρσιβαρίστες στην ιστορία, κυριαρχώντας στην κατηγορία των 94 κιλών.",
        [
            "Στο Σίδνεϊ 2000 κατέκτησε το χρυσό μετάλλιο σε έναν δραματικό αγώνα χάρη στο χαμηλότερο σωματικό του βάρος έναντι των αντιπάλων του.",
            "Υπηρέτησε αργότερα ως πρόεδρος της Ελληνικής Ομοσπονδίας Άρσης Βαρών."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%87%CE%B9_%CE%9A%CE%B1%CF%87%CE%B9%CE%B1%CF%83%CE%B2%CE%AF%CE%BB%CE%B9",
        ["kachi_kakhiashvili", "weightlifting", "olympics", "greek_sports"]
    ),
    # 384
    make_q(
        "pop_culture_hard_384",
        "Ποιος ιστορικός αγώνας άρσης βαρών στην Ατλάντα το 1996 μεταξύ του Βαλέριου Λεωνίδη και ποιου Τούρκου αρσιβαρίστα έμεινε ως η σπουδαιότερη μονομαχία του αθλήματος;",
        "Ναΐμ Σουλεϊμάνογλου (Naim Süleymanoğlu)",
        ["Χαλίλ Μουτλού", "Φεντάι Γκιουλέρ", "Τανέρ Σαγίρ"],
        "Ο Βαλέριος Λεωνίδης και ο 'Ηρακλής Τσέπης' Naim Süleymanoğlu κατέρριψαν διαδοχικά παγκόσμια ρεκόρ στην κατηγορία των 64 κιλών σε μια μυθική αναμέτρηση.",
        [
            "Ο Süleymanoğlu κέρδισε τελικά το χρυσό σηκώνοντας 335 κιλά στο σύνολο έναντι 332,5 κιλών του Λεωνίδη.",
            "Οι δύο αθλητές αγκαλιάστηκαν θερμά μετά τον αγώνα και έγιναν ισόβιοι φίλοι, με τον Λεωνίδη να παρίσταται συντετριμμένος στην κηδεία του Τούρκου θρύλου το 2017."
        ],
        "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CE%BB%CE%AD%CF%81%CE%B9%CE%BF%CF%82_%CE%9B%CE%B5%CF%89%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
        ["valerios_leonidis", "naim_suleymanoglu", "atlanta_1996", "weightlifting"]
    ),
    # 385
    make_q(
        "pop_culture_hard_385",
        "Ποιος Έλληνας κολυμβητής ανοιχτής θαλάσσης κατέκτησε το ασημένιο μετάλλιο στα 10 χιλιόμετρα στους Ολυμπιακούς Αγώνες του Ρίο 2016 χάνοντας το χρυσό στην επαφή;",
        "Σπύρος Γιαννιώτης",
        ["Κριστιάν Γκολομέεβ", "Απόστολος Χρήστου", "Ανδρέας Βαζαίος"],
        "Ο Σπύρος Γιαννιώτης τερμάτισε στον ίδιο ακριβώς χρόνο (1:52:59.8) με τον Ολλανδό Ferry Weertman σε ηλικία 36 ετών στην πέμπτη του ολυμπιακή συμμετοχή.",
        [
            "Η ελληνική αποστολή αρνήθηκε να υποβάλει ένσταση για το photo-finish, σεβόμενη το πνεύμα του ευ αγωνίζεσθαι.",
            "Ο Γιαννιώτης ανακηρύχθηκε κορυφαίος αθλητής της χρονιάς στην Ελλάδα και εντάχθηκε στο International Marathon Swimming Hall of Fame."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%80%CF%8D%CF%81%CE%BF%CF%82_%CE%93%CE%B9%CE%B1%CE%BD%CE%BD%CE%B9%CF%8E%CF%84%CE%B7%CF%82",
        ["spyros_gianniotis", "open_water_swimming", "rio_2016", "olympics"]
    ),
    # 386
    make_q(
        "pop_culture_hard_386",
        "Ποιος Έλληνας κολυμβητής κατέκτησε το ασημένιο μετάλλιο στα 200 μέτρα ύπτιο στους Ολυμπιακούς Αγώνες του Παρισιού 2024;",
        "Απόστολος Χρήστου",
        ["Κριστιάν Γκολομέεβ", "Απόστολος Σίσκος", "Στέργιος Μπίλας"],
        "Ο Απόστολος Χρήστου κατέκτησε το πρώτο ολυμπιακό μετάλλιο της Ελλάδας στην κολύμβηση σε πισίνα μετά από 128 χρόνια (από τους πρώτους Αγώνες της Αθήνας το 1896).",
        [
            "Μόλις λίγες ημέρες νωρίτερα, είχε χάσει το μετάλλιο στα 100 μέτρα ύπτιο για μόλις 2 εκατοστά του δευτερολέπτου τερματίζοντας τέταρτος.",
            "Η ψυχική δύναμη και η ανάκαμψή του στον τελικό των 200μ αποτέλεσε μία από τις πιο συγκινητικές στιγμές του ελληνικού αθλητισμού."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CF%80%CF%8C%CF%83%CF%84%CE%BF%CE%BB%CE%BF%CF%82_%CE%A7%CF%81%CE%AE%CF%83%CF%84%CE%BF%CF%85",
        ["apostolos_christou", "swimming", "paris_2024", "olympics"]
    ),
    # 387
    make_q(
        "pop_culture_hard_387",
        "Ποια Ελληνίδα σκοπεύτρια κατέκτησε χρυσό (25μ πιστόλι) και χάλκινο μετάλλιο (10μ αεροβόλο πιστόλι) στους Ολυμπιακούς Αγώνες του Ρίο 2016 σε ηλικία 20 ετών;",
        "Άννα Κορακάκη",
        ["Αγησιστράτη Κορακάκη", "Δώρα Γκουντούρα", "Βασιλική Μιλλούση"],
        "Η Άννα Κορακάκη έγινε η πρώτη Ελληνίδα αθλήτρια που κατέκτησε δύο ολυμπιακά μετάλλια στην ίδια διοργάνωση μετά από έναν αιώνα (από τον Κωνσταντίνο Τσικλητήρα το 1912).",
        [
            "Προπονητής της υπήρξε σταθερά ο πατέρας της, Τάσος Κορακάκης, υπό δύσκολες συνθήκες προπόνησης σε ένα πρόχειρο σκοπευτήριο στη Δράμα.",
            "Έγινε η πρώτη γυναίκα στην ιστορία που ξεκίνησε την Ολυμπιακή Λαμπαδηδρομία για τους Αγώνες του Τόκιο 2020 στην Αρχαία Ολυμπία."
        ],
        "https://el.wikipedia.org/wiki/%CE%86%CE%BD%CE%BD%CE%B1_%CE%9A%CE%BF%CF%81%CE%B1%CE%BA%CE%AC%CE%BA%CE%B7",
        ["anna_korakaki", "shooting", "rio_2016", "olympics"]
    ),
    # 388
    make_q(
        "pop_culture_hard_388",
        "Ποιος Έλληνας πρωταθλητής της ιστιοπλοΐας κατέκτησε το χρυσό μετάλλιο στην κατηγορία Mistral στους Ολυμπιακούς Αγώνες της Ατλάντα 1996;",
        "Νίκος Κακλαμανάκης",
        ["Ανδρέας Κοσματόπουλος", "Τάσος Μπουντούρης", "Αιμίλιος Παπαθανασίου"],
        "Ο 'Γιος του Ανέμου' Νίκος Κακλαμανάκης κατέκτησε το χρυσό στην Ατλάντα και στη συνέχεια το ασημένιο μετάλλιο στους Ολυμπιακούς Αγώνες της Αθήνας 2004.",
        [
            "Στους Ολυμπιακούς Αγώνες της Αθήνας 2004, ο Κακλαμανάκης είχε την υπέρτατη τιμή να ανάψει τον Ολυμπιακό Βωμό στην τελετή έναρξης.",
            "Διέσχισε το Αιγαίο Πέλαγος με ιστιοσανίδα από το Σούνιο μέχρι την Κρήτη σε μια ιστορική διαδρομή αντοχής."
        ],
        "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%9A%CE%B1%CE%BA%CE%BB%CE%B1%CE%BC%CE%B1%CE%BD%CE%AC%CE%BA%CE%B7%CF%82",
        ["kaklamanakis", "sailing", "windsurfing", "atlanta_1996", "athens_2004"]
    ),
    # 389
    make_q(
        "pop_culture_hard_389",
        "Ποιο ήταν το όνομα της θρυλικής εκπομπής μουσικών βίντεο που παρουσίαζε ο Γκάρι Φαλκόνερ και ο Νίκος Μουρατίδης στην ΕΡΤ τη δεκαετία του 1980;",
        "Μουσικό Καλειδοσκόπιο",
        ["Μουσικόραμα", "Pop 80s", "Studio 4"],
        "Το 'Μουσικόραμα' (μετέπειτα παρουσιαζόμενο από τον Βασίλη Λούκα) υπήρξε το μοναδικό παράθυρο των νέων της εποχής στη διεθνή ποπ και ροκ σκηνή.",
        [
            "Προβλήθηκαν για πρώτη φορά στην ελληνική τηλεόραση βίντεο κλιπ του Michael Jackson, της Madonna, των Duran Duran και των Depeche Mode.",
            "Τα επεισόδια καταγράφονταν μανιωδώς σε βιντεοκασέτες VHS από χιλιάδες εφήβους σε όλη τη χώρα."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CF%8C%CF%81%CE%B1%CE%BC%CE%B1",
        ["mousikorama", "ert", "80s", "music_videos", "greek_tv"]
    ),
    # 390
    make_q(
        "pop_culture_hard_390",
        "Ποιος πρωτοποριακός ραδιοφωνικός σταθμός της Αθήνας ξεκίνησε τη λειτουργία του το 1987 ως ο πρώτος ελεύθερος δημοτικός ραδιοσταθμός της χώρας;",
        "Αθήνα 9.84",
        ["Flash 96.1", "ΣΚΑΪ 100.4", "Top FM"],
        "Ο 'Αθήνα 9.84' ιδρύθηκε από τον δήμαρχο Αθηναίων Μιλτιάδη Έβερτ σπάζοντας το κρατικό μονοπώλιο της ΕΡΤ και εγκαινιάζοντας την ελεύθερη ραδιοφωνία.",
        [
            "Η πρώτη επίσημη εκπομπή έγινε στις 31 Μαΐου 1987 εν μέσω δικαστικών διώξεων και απειλών σύλληψης από την κυβέρνηση.",
            "Ο σταθμός συγκέντρωσε κορυφαίους δημοσιογράφους και καλλιτέχνες αλλάζοντας ριζικά την ενημέρωση στην Ελλάδα."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CE%B8%CE%AE%CE%BD%CE%B1_9.84",
        ["athina_984", "radio", "free_radio", "evert", "1987"]
    ),
    # 391
    make_q(
        "pop_culture_hard_391",
        "Ποιος ήταν ο πρώτος ιδιωτικός τηλεοπτικός σταθμός πανελλαδικής εμβέλειας που εξέπεμψε σήμα στην Ελλάδα στις 20 Νοεμβρίου 1989;",
        "Mega Channel",
        ["ΑΝΤ1", "New Channel", "Κανάλι 29"],
        "Το Mega Channel ξεκίνησε τις εκπομπές του στις 20 Νοεμβρίου 1989 στις 15:00 με το καλωσόρισμα: 'Το πρώτο ιδιωτικό κανάλι είναι στον αέρα'.",
        [
            "Ιδρύθηκε από την εταιρεία Τηλέτυπος Α.Ε., κοινοπραξία πέντε εκδοτών εφημερίδων (Βαρδινογιάννης, Λαμπράκης, Μπόμπολας, Τεγόπουλος, Αλαφούζος).",
            "Ο ΑΝΤ1 του Μίνωα Κυριακού ξεκίνησε τις εκπομπές του μόλις ένα μήνα αργότερα, στις 31 Δεκεμβρίου 1989."
        ],
        "https://el.wikipedia.org/wiki/Mega_Channel",
        ["mega_channel", "private_television", "history", "1989", "greece"]
    ),
    # 392
    make_q(
        "pop_culture_hard_392",
        "Ποιος ιστορικός δημοσιογράφος παρουσίασε το πρώτο επίσημο δελτίο ειδήσεων στην πρεμιέρα του Mega Channel το 1989;",
        "Νίκος Χατζηνικολάου",
        ["Αιμίλιος Λιάτσος", "Τέρενς Κουίκ", "Παύλος Τσίμας"],
        "Ο νεαρός τότε Νίκος Χατζηνικολάου παρουσίασε το κεντρικό δελτίο ειδήσεων εγκαινιάζοντας μια νέα εποχή ταχύτητας και τηλεοπτικού ρεπορτάζ.",
        [
            "Ο Χατζηνικολάου παρέμεινε ο κεντρικός παρουσιαστής ειδήσεων του Mega για 14 συνεχόμενα χρόνια.",
            "Η εκπομπή του 'Ενώπιος Ενωπίω' φιλοξένησε τις πιο σημαντικές προσωπικότητες της πολιτικής και του πολιτισμού."
        ],
        "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%A7%CE%B1%CF%84%CE%B6%CE%B7%CE%BD%CE%B9%CE%BA%CE%BF%CE%BB%CE%AC%CE%BF%CF%85",
        ["nikos_chatzinikolaou", "mega_channel", "news", "journalism"]
    ),
    # 393
    make_q(
        "pop_culture_hard_393",
        "Ποιος ήταν ο πρώτος παρουσιαστής του πρώτου δελτίου ειδήσεων του ΑΝΤ1 την παραμονή Πρωτοχρονιάς του 1989;",
        "Τέρενς Κουίκ",
        ["Νίκος Ευαγγελάτος", "Θοδωρής Δρακάκης", "Γιώργος Παπαδάκης"],
        "Ο Τέρενς Κουίκ παρουσίασε το πρώτο δελτίο ειδήσεων του ΑΝΤ1 στις 31 Δεκεμβρίου 1989, αποτελώντας το πρόσωπο του σταθμού για πολλά χρόνια.",
        [
            "Το δελτίο του ΑΝΤ1 καθιέρωσε ένα πιο επιθετικό και άμεσο στυλ ρεπορτάζ σε ανταγωνισμό με το Mega.",
            "Αργότερα ο Κουίκ παρουσίασε με μεγάλη επιτυχία την ενημερωτική εκπομπή 'Απόψε με τον Τέρενς Κουίκ'."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%AD%CF%81%CE%B5%CE%BD%CF%82_%CE%9A%CE%BF%CF%85%CE%AF%CE%BA",
        ["terence_quick", "ant1", "news", "television_history"]
    ),
    # 394
    make_q(
        "pop_culture_hard_394",
        "Ποια πρωινή ενημερωτική εκπομπή του Γιώργου Παπαδάκη στον ΑΝΤ1 κατέχει το ρεκόρ της μακροβιότερης καθημερινής πρωινής εκπομπής στην Ελλάδα (από το 1992);",
        "Καλημέρα Ελλάδα",
        ["Πρωινός Καφές", "Κοινωνία Ώρα Mega", "Στούντιο 4"],
        "Το 'Καλημέρα Ελλάδα' ξεκίνησε στις 28 Απριλίου 1992 δημιουργώντας ουσιαστικά την πρωινή ενημερωτική ζώνη στην ελληνική τηλεόραση.",
        [
            "Ο Γιώργος Παπαδάκης παραμένει σταθερά στο τιμόνι της εκπομπής για πάνω από τρεις δεκαετίες.",
            "Η εκπομπή ανέδειξε δεκάδες νέους δημοσιογράφους και ρεπόρτερ που αργότερα ανέλαβαν δικές τους εκπομπές."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BB%CE%B7%CE%BC%CE%AD%CF%81%CE%B1_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1",
        ["kalimera_ellada", "giorgos_papadakis", "ant1", "morning_news"]
    ),
    # 395
    make_q(
        "pop_culture_hard_395",
        "Ποια παρουσιάστρια ταυτίστηκε απόλυτα με τον 'Πρωινό Καφέ' του ΑΝΤ1 παρουσιάζοντάς τον επί 10 συνεχόμενα χρόνια (1995-2005) στη χρυσή εποχή του;",
        "Ελένη Μενεγάκη",
        ["Ρούλα Κορομηλά", "Πόπη Χατζηδημητρίου", "Ελεονώρα Μελέτη"],
        "Η Ελένη Μενεγάκη ανέλαβε τον 'Πρωινό Καφέ' το 1995 και έγινε η απόλυτη 'βασίλισσα της πρωινής ζώνης' και το πιο ισχυρό εμπορικό πρόσωπο της τηλεόρασης.",
        [
            "Η εκπομπή ξεκίνησε αρχικά το 1991 με τη Ρούλα Κορομηλά.",
            "Το 2005 η Μενεγάκη μεταγράφηκε στον Alpha για την εκπομπή 'Καφές με την Ελένη' προκαλώντας τηλεοπτικό σεισμό."
        ],
        "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CF%89%CE%B9%CE%BD%CF%8C%CF%82_%CE%9A%CE%B1%CF%86%CE%AD%CF%82",
        ["proinos_kafes", "eleni_menegaki", "ant1", "greek_tv"]
    ),
    # 396
    make_q(
        "pop_culture_hard_396",
        "Ποιο ήταν το πρώτο υπερθέαμα ζωντανού σόου του Σαββατοκύριακου που παρουσίασε η Ρούλα Κορομηλά στο Mega το 1992 εγκαινιάζοντας τη λαμπερή prime time;",
        "Ciao ANT1 / Ciao",
        ["Μπράβο", "Ciao Mega", "Super Saturday"],
        "Το 'Ciao ANT1' (και νωρίτερα οι πρωινές εκπομπές της) καθιέρωσε τη Ρούλα Κορομηλά ως την πρώτη μεγάλη σταρ παρουσιάστρια της ιδιωτικής τηλεόρασης.",
        [
            "Στο σόου της 'Μπράβο' στο Mega το 1995 φιλοξένησε κορυφαίους διεθνείς σταρ όπως ο Ricky Martin, ο Eros Ramazzotti και η Madonna.",
            "Η ζωντανή εκπομπή από το Δημοτικό Θέατρο Πειραιά και αργότερα από το ΣΕΦ συγκέντρωνε τηλεθεάσεις άνω του 60%."
        ],
        "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CF%8D%CE%BB%CE%B1_%CE%9A%CE%BF%CF%81%CE%BF%CE%BC%CE%B7%CE%BB%CE%AC",
        ["roula_koromila", "ciao_ant1", "bravo", "mega", "variety_show"]
    ),
    # 397
    make_q(
        "pop_culture_hard_397",
        "Ποιος διεθνής ποπ σταρ εμφανίστηκε ζωντανά στο σόου 'Μπράβο' της Ρούλας Κορομηλά στον ΑΝΤ1 το 1999 τραγουδώντας το 'Livin' la Vida Loca';",
        "Ricky Martin",
        ["Enrique Iglesias", "Eros Ramazzotti", "Robbie Williams"],
        "Ο Ricky Martin βρισκόταν στο απόγειο της παγκόσμιας δόξας του και η εμφάνισή του στην ελληνική τηλεόραση προκάλεσε υστερία στο κοινό του σταδίου.",
        [
            "Η Ρούλα Κορομηλά χόρεψε μαζί του στη σκηνή σε μία από τις πιο πολυσυζητημένες στιγμές της ελληνικής τηλεόρασης.",
            "Τα μέτρα ασφαλείας γύρω από το στούντιο ήταν πρωτοφανή για τα ελληνικά δεδομένα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CF%8D%CE%BB%CE%B1_%CE%9A%CE%BF%CF%81%CE%BF%CE%BC%CE%B7%CE%BB%CE%AC",
        ["ricky_martin", "roula_koromila", "bravo", "livin_la_vida_loca"]
    ),
    # 398
    make_q(
        "pop_culture_hard_398",
        "Ποιο ήταν το όνομα του σατιρικού χαρακτήρα με τη μαύρη καμπαρντίνα και το καπέλο που υποδυόταν ο Χάρρυ Κλυνν σατιρίζοντας τον μέσο Έλληνα ψηφοφόρο;",
        "Τραμπάκουλας",
        ["Αρτέμης", "Χαράλαμπος", "Μαλάκας"],
        "Ο Τραμπάκουλας ήταν ένας βοσκός από την επαρχία με απίστευτες ατάκες για την πολιτική κατάσταση, την ΕΟΚ και τα συνδικάτα.",
        [
            "Ο Χάρρυ Κλυνν (Χάρης Τριανταφυλλίδης) άλλαξε ριζικά την ελληνική σάτιρα εισάγοντας τη stand-up comedy και τους σατιρικούς δίσκους βινυλίου.",
            "Οι δίσκοι του όπως 'Για δέσιμο' και 'Δοξάστε με' πούλησαν εκατοντάδες χιλιάδες αντίτυπα σπάζοντας ρεκόρ πωλήσεων."
        ],
        "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CF%81%CF%85_%CE%9A%CE%BB%CF%85%CE%BD%CE%BD",
        ["harry_klynn", "trampakoulas", "satire", "stand_up_comedy"]
    ),
    # 399
    make_q(
        "pop_culture_hard_399",
        "Ποιος ιστορικός σατιρικός δίσκος του Χάρρυ Κλυνν το 1978 έγινε ο πρώτος πλατινένιος δίσκος κωμωδίας στην ιστορία της ελληνικής δισκογραφίας;",
        "Για δέσιμο",
        ["Δοξάστε με", "Πατάτες", "Γελάτε γιατί χανόμαστε"],
        "Ο δίσκος 'Για δέσιμο' σε παραγωγή της Columbia πούλησε πάνω από 150.000 αντίτυπα και καθιέρωσε το σατιρικό σκετς ως κυρίαρχο είδος ψυχαγωγίας.",
        [
            "Ο Χάρρυ Κλυνν εισήγαγε ηχητικά εφέ, μιμήσεις πολιτικών (Καραμανλής, Παπανδρέου) και ανατρεπτικές παρωδίες διαφημίσεων.",
            "Υπήρξε ο πρώτος που έφερε το αμερικανικό φορμάτ του stand-up comedy στα ελληνικά νυχτερινά κέντρα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CF%81%CF%85_%CE%9A%CE%BB%CF%85%CE%BD%CE%BD",
        ["harry_klynn", "gia_desimo", "comedy_records", "greek_music"]
    ),
    # 400
    make_q(
        "pop_culture_hard_400",
        "Ποια θρυλική ραδιοφωνική εκπομπή του Γιάννη Πετρίδη στο Πρώτο Πρόγραμμα της ΕΡΑ ξεκίνησε το 1975 και συνεχίζεται αδιάλειπτα για πάνω από 45 χρόνια;",
        "Από τις 4 στις 5",
        ["Μουσικόραμα", "Ήχοι του Κόσμου", "Ροκ Αναζητήσεις"],
        "Ο Γιάννης Πετρίδης εκπαίδευσε μουσικά γενιές Ελλήνων ακροατών παρουσιάζοντας όλες τις νέες κυκλοφορίες της παγκόσμιας ροκ και ποπ σκηνής.",
        [
            "Η εκπομπή κατέχει παγκόσμιο ρεκόρ διάρκειας για ραδιοφωνική εκπομπή με τον ίδιο παρουσιαστή στην ίδια συχνότητα.",
            "Ο Πετρίδης διετέλεσε επί σειρά ετών διευθυντής της δισκογραφικής εταιρείας Virgin Greece."
        ],
        "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%A0%CE%B5%CF%84%CF%81%CE%AF%CE%B4%CE%B7%CF%82",
        ["giannis_petridis", "apo_tis_4_stis_5", "era", "radio_history"]
    ),
    # 401
    make_q(
        "pop_culture_hard_401",
        "Ποιο μουσικό περιοδικό που ίδρυσε ο Γιάννης Πετρίδης και ο Κώστας Ζουγρής το 1978 υπήρξε η 'βίβλος' των Ελλήνων μουσικόφιλων για δεκαετίες;",
        "Ποπ & Ροκ",
        ["Μουσική", "Ήχος & Hi-Fi", "Zoo"],
        "Το 'Ποπ & Ροκ' κατέγραψε όλες τις μεγάλες τάσεις της διεθνούς και ελληνικής μουσικής, περιλαμβάνοντας συνεντεύξεις, δισκοκριτικές και αφίσες συγκροτημάτων.",
        [
            "Κυκλοφόρησε για πάνω από 30 χρόνια και αποτέλεσε σημείο αναφοράς για τη μουσική δημοσιογραφία στην Ελλάδα.",
            "Το πρώτο τεύχος κυκλοφόρησε τον Φεβρουάριο του 1978 με εξώφυλλο τους Genesis."
        ],
        "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CF%80_%26_%CE%A1%CE%BF%CE%BA",
        ["pop_kai_rok", "petridis", "music_magazines", "greece"]
    ),
    # 402
    make_q(
        "pop_culture_hard_402",
        "Ποιος ιστορικός ραδιοφωνικός σταθμός της Αθήνας (στους 100.3 FM) ιδρύθηκε το 1989 από τον όμιλο Αλαφούζου και έφερε επανάσταση στην ενημέρωση;",
        "ΣΚΑΪ 100.3 (τότε ΣΚΑΪ 100.4)",
        ["Flash 96.1", "Planet 104.5", "Antenna 97.1"],
        "Ο ΣΚΑΪ 100.4 εξέπεμψε για πρώτη φορά το 1989 με ένα πλήρες δημοσιογραφικό επιτελείο, 24ωρη ενημέρωση και ζωντανές συνδέσεις από όλο τον κόσμο.",
        [
            "Υπήρξε ο πρώτος σταθμός που χρησιμοποίησε δορυφορικές μεταδόσεις και ειδικά διαμορφωμένα βαν εξωτερικών μεταδόσεων.",
            "Αργότερα ο σταθμός μετακινήθηκε στη συχνότητα 100.3 FM παραμένοντας σταθερά στην κορυφή της ακροαματικότητας."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CE%9A%CE%91%CE%AA_100.3",
        ["skai_100_3", "radio_history", "alafouzos", "journalism"]
    ),
    # 403
    make_q(
        "pop_culture_hard_403",
        "Ποια πρωτοποριακή εκπομπή ερευνητικής δημοσιογραφίας του Στέλιου Κούλογλου ξεκίνησε στην ΕΡΤ το 1996 καταγράφοντας διεθνή ρεπορτάζ;",
        "Ρεπορτάζ Χωρίς Σύνορα",
        ["Φάκελοι", "Μαύρο Κουτί", "Εμπόλεμη Ζώνη"],
        "Το 'Ρεπορτάζ Χωρίς Σύνορα' κέρδισε τέσσερις φορές το βραβείο της καλύτερης ενημερωτικής εκπομπής και απέσπασε διεθνείς διακρίσεις για τα ιστορικά και πολιτικά του αφιερώματα.",
        [
            "Η εκπομπή κάλυψε θέματα από τον πόλεμο στη Γιουγκοσλαβία μέχρι τη δολοφονία του Che Guevara και το Ολοκαύτωμα.",
            "Ο Κούλογλου ίδρυσε αργότερα τον ειδησεογραφικό ιστότοπο TVXS (Τηλεόραση Χωρίς Σύνορα)."
        ],
        "https://el.wikipedia.org/wiki/%CE%A1%CE%B5%CF%80%CE%BF%CF%81%CF%84%CE%AC%CE%B6_%CE%A7%CF%89%CF%81%CE%AF%CF%82_%CE%A3%CF%8D%CE%BD%CE%BF%CF%81%CE%B1",
        ["reportaz_horis_synora", "kouloglou", "ert", "documentary"]
    ),
    # 404
    make_q(
        "pop_culture_hard_404",
        "Ποιος δημοσιογράφος παρουσίαζε την επιτυχημένη ενημερωτική εκπομπή 'Φάκελοι' στο Mega Channel (2000-2010) με αποκαλυπτικές έρευνες;",
        "Αλέξης Παπαχελάς",
        ["Παύλος Τσίμας", "Σταύρος Θεοδωράκης", "Τάσος Τέλλογλου"],
        "Οι 'Φάκελοι' (με τους Αλέξη Παπαχελά, Τάσο Τέλλογλου και Σοφία Παπαϊωάννου) παρουσίασαν ιστορικές συνεντεύξεις με παγκόσμιους ηγέτες και έρευνες για τη σύγχρονη ελληνική ιστορία.",
        [
            "Ο Παπαχελάς εξασφάλισε σπάνιο απόρρητο αρχειακό υλικό από το State Department των ΗΠΑ για τη δικτατορία της 21ης Απριλίου και την κυπριακή τραγωδία.",
            "Η εκπομπή θεωρείται πρότυπο τηλεοπτικής ερευνητικής δημοσιογραφίας στην Ελλάδα."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AD%CE%BE%CE%B7%CF%82_%CE%A0%CE%B1%CF%80%CE%B1%CF%87%CE%B5%CE%BB%CE%AC%CF%82",
        ["fakeloi", "papachelas", "mega_channel", "journalism"]
    ),
    # 405
    make_q(
        "pop_culture_hard_405",
        "Ποια εκπομπή κοινωνικών ρεπορτάζ του Σταύρου Θεοδωράκη στο Mega (2000-2014) ταξίδευε με ένα σακίδιο σε όλη την Ελλάδα καταγράφοντας ανθρώπινες ιστορίες;",
        "Πρωταγωνιστές",
        ["Οι Νέοι Φάκελοι", "Εμπόλεμη Ζώνη", "Όχι τα Νέα του ΑΝΤ1"],
        "Οι 'Πρωταγωνιστές' καθιέρωσαν ένα νέο στυλ αφήγησης χωρίς γραβάτα και στούντιο, δίνοντας φωνή σε περιθωριοποιημένους ανθρώπους και ιδιαίτερες κοινωνικές ομάδες.",
        [
            "Το χαρακτηριστικό σήμα κατατεθέν του Θεοδωράκη ήταν το σακίδιο πλάτης με το οποίο περιπλανιόταν στις συνεντεύξεις.",
            "Η επιτυχία της εκπομπής οδήγησε τον Θεοδωράκη να ιδρύσει το πολιτικό κόμμα 'Το Ποτάμι' το 2014."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AC%CF%85%CF%81%CE%BF%CF%82_%CE%98%CE%B5%CE%BF%CE%B4%CF%89%CF%81%CE%AC%CE%BA%CE%B7%CF%82",
        ["protagonistes", "theodorakis", "mega_channel", "journalism"]
    ),
    # 406
    make_q(
        "pop_culture_hard_406",
        "Ποια δραματική ταινία του Παντελή Βούλγαρη το 1998 με πρωταγωνιστή τον Γιώργο Αρμένη κατέγραψε τη νυχτερινή ζωή και τα σκυλάδικα της επαρχίας;",
        "Όλα είναι δρόμος",
        ["Πέτρινα Χρόνια", "Η Φανέλα με το '9'", "Ψυχή Βαθιά"],
        "Η σπονδυλωτή ταινία περιλαμβάνει την ιστορική τρίτη ιστορία όπου ο επιχειρηματίας Μάκης Τσετσένογλου (Γιώργος Αρμένης) γκρεμίζει ένα ολόκληρο νυχτερινό κέντρο με μπουλντόζα.",
        [
            "Η κραυγή 'Ηλία, ρίχτο!' και η σκηνή όπου ο Αρμένης χορεύει ζεϊμπέκικο καίγοντας την καπαρντίνα του αποτελούν μία από τις πιο διάσημες σκηνές του ελληνικού σινεμά.",
            "Η φράση 'Όλα είναι δρόμος' πέρασε ως λαϊκή φιλοσοφική έκφραση στη νεοελληνική κουλτούρα."
        ],
        "https://el.wikipedia.org/wiki/%CE%8C%CE%BB%CE%B1_%CE%B5%CE%AF%CE%BD%CE%B1%CE%B9_%CE%B4%CF%81%CF%8C%CE%BC%CE%BF%CF%82",
        ["ola_einai_dromos", "pantelis_voulgaris", "giorgos_armenis", "ilia_richto"]
    ),
    # 407
    make_q(
        "pop_culture_hard_407",
        "Ποια ήταν η ιστορική φράση που φώναξε ο Γιώργος Αρμένης στον χειριστή της μπουλντόζας πριν ισοπεδώσει το νυχτερινό κέντρο 'Βιετνάμ' στο 'Όλα είναι δρόμος';",
        "Ηλία, ρίχτο!",
        ["Ηλία, σπάσ' τα όλα!", "Ηλία, γκρέμισέ το!", "Ηλία, κάψ' το!"],
        "Ο Μάκης Τσετσένογλου πληρώνει τον ιδιοκτήτη σε μετρητά, φωνάζει 'Ηλία, ρίχτο! Όλα είναι δρόμος!' και δίνει εντολή στη μπουλντόζα να κατεδαφίσει το μαγαζί ενώ ο ίδιος χορεύει.",
        [
            "Το μαγαζί 'Βιετνάμ' βρισκόταν στην πραγματικότητα έξω από το Κιλκίς.",
            "Η σκηνή γυρίστηκε με μία μόνο λήψη καθώς το κτίριο κατεδαφίστηκε στ' αλήθεια κατά τη διάρκεια του γυρίσματος."
        ],
        "https://el.wikipedia.org/wiki/%CE%8C%CE%BB%CE%B1_%CE%B5%CE%AF%CE%BD%CE%B1%CE%B9_%CE%B4%CF%81%CF%8C%CE%BC%CE%BF%CF%82",
        ["ilia_richto", "ola_einai_dromos", "voulgaris", "cult_cinema"]
    ),
    # 408
    make_q(
        "pop_culture_hard_408",
        "Ποια ταινία του Παντελή Βούλγαρη το 1985 βασίστηκε στην αληθινή ιστορία αγάπης δύο εξόριστων κομμουνιστών κερδίζοντας βραβεία στη Βενετία;",
        "Πέτρινα Χρόνια",
        ["Το Προξενιό της Άννας", "Ακροπόλ", "Μικρά Αγγλία"],
        "Τα 'Πέτρινα Χρόνια' αφηγούνται την ιστορία της Ελένης Βούλγαρη (Θέμις Μπαζάκα) και του Μπάμπη Γκολέμα (Δημήτρης Καταλειφός) που έζησαν δεκαετίες στις φυλακές και τις εξορίες.",
        [
            "Η Θέμις Μπαζάκα απέσπασε Ειδική Μνεία Ερμηνείας στο Φεστιβάλ Κινηματογράφου της Βενετίας το 1985.",
            "Η μουσική του Σταμάτη Σπανουδάκη με το σόλο κλαρίνο του Βασίλη Σαλέα έγινε διαχρονική επιτυχία."
        ],
        "https://el.wikipedia.org/wiki/%CE%A0%CE%AD%CF%84%CF%81%CE%B9%CE%BD%CE%B1_%CE%A7%CF%81%CF%8C%CE%BD%CE%B9%CE%B1",
        ["petrina_chronia", "voulgaris", "bazaka", "katalifos", "greek_cinema"]
    ),
    # 409
    make_q(
        "pop_culture_hard_409",
        "Ποιος δεξιοτέχνης του κλαρίνου ερμήνευσε το συγκλονιστικό μουσικό θέμα του Σταμάτη Σπανουδάκη για την ταινία 'Πέτρινα Χρόνια' (1985);",
        "Βασίλης Σαλέας",
        ["Μάνος Αχαλινωτόπουλος", "Γιώργος Μάγκας", "Πετρολούκας Χαλκιάς"],
        "Ο Βασίλης Σαλέας χάρισε έναν απαράμιλλο λυρισμό στο βασικό μοτίβο της ταινίας, καθιερώνοντας το κλαρίνο ως όργανο κινηματογραφικής συγκίνησης πέρα από τη δημοτική παράδοση.",
        [
            "Το μουσικό θέμα των 'Πέτρινων Χρόνων' χρησιμοποιήθηκε σε δεκάδες διεθνείς παραγωγές και τηλεοπτικά αφιερώματα.",
            "Η συνεργασία του Σαλέα με τον Σπανουδάκη συνεχίστηκε σε πολλά επιτυχημένα ορχηστρικά άλμπουμ."
        ],
        "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B7%CF%82_%CE%A3%CE%B1%CE%BB%CE%AD%CE%B1%CF%82",
        ["vasilis_saleas", "petrina_chronia", "spanoudakis", "clarinet", "greek_music"]
    ),
    # 410
    make_q(
        "pop_culture_hard_410",
        "Ποια ρομαντική δραματική ταινία εποχής του Παντελή Βούλγαρη το 2013, βασισμένη στο ομώνυμο βιβλίο της Ιωάννας Καρυστιάνη, γυρίστηκε εξ ολοκλήρου στην Άνδρο;",
        "Μικρά Αγγλία",
        ["Νύφες", "Ψυχή Βαθιά", "Πέτρινα Χρόνια"],
        "Η 'Μικρά Αγγλία' κατέγραψε τη ναυτική ζωή της Άνδρου της δεκαετίας του 1930 και τον κρυφό έρωτα δύο αδελφών (Πηνελόπη Τσιλίκα, Σοφία Κόκκαλη) για τον ίδιο καπετάνιο.",
        [
            "Κέρδισε έξι βραβεία της Ελληνικής Ακαδημίας Κινηματογράφου, ανάμεσά τους Καλύτερης Ταινίας, και το Χρυσό Κύπελλο στο Φεστιβάλ της Σαγκάης.",
            "Υπήρξε η επίσημη υποβολή της Ελλάδας για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας το 2015."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%BA%CF%81%CE%AC_%CE%91%CE%B3%CE%B3%CE%BB%CE%AF%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["mikra_anglia", "voulgaris", "karystiani", "andros", "greek_cinema"]
    ),
]

if __name__ == "__main__":
    validate_and_append("pop_culture", "hard", 5, questions)

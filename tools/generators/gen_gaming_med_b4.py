# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_med_361",
        "text": "Στη σειρά 'Resident Evil', τι σημαίνουν τα αρχικά της επίλεκτης αστυνομικής ομάδας S.T.A.R.S. του Raccoon City Police Department;",
        "correct": "Special Tactics And Rescue Service",
        "distractors": [
            "Special Taskforce Against Rogue Soldiers",
            "Scientific Team And Research Security",
            "Special Trauma And Rescue Squad"
        ],
        "explanation": "Η ομάδα S.T.A.R.S. ιδρύθηκε το 1996 στη Raccoon City και χωριζόταν στις μονάδες Alpha Team (με αρχηγό τον Albert Wesker) και Bravo Team (με αρχηγό τον Enrico Marini).",
        "funFacts": [
            "Ο Wesker ήταν στην πραγματικότητα διπλός πράκτορας της Umbrella Corporation και οδήγησε επίτηδες τα μέλη της S.T.A.R.S. στην έπαυλη για να δοκιμάσει τα βιολογικά όπλα.",
            "Η Jill Valentine και ο Chris Redfield ίδρυσαν αργότερα τη διεθνή οργάνωση B.S.A.A. για την καταπολέμηση της βιοτρομοκρατίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil",
        "tags": ["gaming", "resident_evil", "capcom", "lore"]
    },
    {
        "id": "gaming_med_362",
        "text": "Στο 'Resident Evil 4' (2005), ποιο αρχαίο παρασιτικό πλάσμα χρησιμοποιεί η αίρεση Los Illuminados για να ελέγχει τους ντόπιους χωρικούς (Ganados);",
        "correct": "Las Plagas",
        "distractors": ["T-Virus", "G-Virus", "Uroboros"],
        "explanation": "Τα παράσιτα Las Plagas δεν μετατρέπουν τους ανθρώπους σε άμυαλα ζόμπι, αλλά διατηρούν τη νοημοσύνη και την ικανότητά τους να χρησιμοποιούν εργαλεία και όπλα υπό τον απόλυτο έλεγχο του Osmund Saddler.",
        "funFacts": [
            "Όταν ο παίκτης πυροβολεί το κεφάλι ενός μολυσμένου εχθρού, ένα τεράστιο παράσιτο με λεπίδες ή πλοκάμια μπορεί να ξεπηδήσει από τον λαιμό του.",
            "Η χρήση των Las Plagas σήμανε την απομάκρυνση της σειράς από τα παραδοσιακά ζόμπι της Umbrella σε πιο γρήγορο action gameplay."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_4",
        "tags": ["gaming", "resident_evil", "capcom", "las_plagas"]
    },
    {
        "id": "gaming_med_363",
        "text": "Στο 'Metal Gear Solid 4: Guns of the Patriots' (2008), ποιο νανοτεχνολογικό σύστημα ελέγχει τα συναισθήματα, τα όπλα και τις πράξεις όλων των στρατιωτών παγκοσμίως;",
        "correct": "SOP System (Sons of the Patriots)",
        "distractors": ["FOXHOUND Network", "The Patriots Core", "Arsenal Gear AI"],
        "explanation": "Το σύστημα SOP συνδέεται με τα νανορομπότ στο αίμα των στρατιωτών και τα όπλα τους, αποτρέποντας τη χρήση τους από μη εγκεκριμένους χρήστες και ρυθμίζοντας τον φόβο και τον πόνο.",
        "funFacts": [
            "Ο Liquid Ocelot χακάρει το σύστημα SOP καταφέρνοντας να απενεργοποιήσει τα όπλα των στρατών και να προκαλέσει μαζικές ψυχολογικές κρίσεις στους στρατιώτες.",
            "Ο Solid Snake πάσχει από επιταχυνόμενη γήρανση (Old Snake) επειδή δημιουργήθηκε ως γενετικός κλώνος του Big Boss με προκαθορισμένη ημερομηνία λήξης."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_4:_Guns_of_the_Patriots",
        "tags": ["gaming", "metal_gear", "hideo_kojima", "playstation3", "lore"]
    },
    {
        "id": "gaming_med_364",
        "text": "Στο 'The Last of Us' (2013), ποια είναι η τραγική απώλεια που βιώνει ο Joel Miller στην εισαγωγή του παιχνιδιού κατά την πρώτη ημέρα του ξεσπάσματος της πανδημίας;",
        "correct": "Η 12χρονη κόρη του Sarah δολοφονείται από έναν στρατιώτη",
        "distractors": ["Η σύζυγός του μεταλλάσσεται σε Clicker", "Ο αδελφός του Tommy χάνεται στην πόλη", "Ο καλύτερός του φίλος αυτοκτονεί"],
        "explanation": "Ένας στρατιώτης λαμβάνει εντολή να πυροβολήσει τον Joel και τη Sarah για λόγους καραντίνας, τραυματίζοντας θανάσιμα το κορίτσι στα χέρια του πατέρα της.",
        "funFacts": [
            "Το σπασμένο ρολόι χειρός που φοράει ο Joel σε όλη την περιπέτεια ήταν το δώρο γενεθλίων που του είχε κάνει η Sarah εκείνο το πρωί.",
            "Η σχέση του Joel με την Ellie εξελίσσεται σταδιακά σε πατρική σχέση, καθώς η Ellie γεμίζει το συναισθηματικό κενό της χαμένης του κόρης."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Last_of_Us",
        "tags": ["gaming", "the_last_of_us", "naughty_dog", "story", "joel"]
    },
    {
        "id": "gaming_med_365",
        "text": "Στο 'The Last of Us Part II' (2020), ποιο είναι το κίνητρο που οδηγεί την Abby Anderson στην αναζήτηση και εκδίκηση εναντίον του Joel;",
        "correct": "Ο Joel σκότωσε τον πατέρα της, τον χειρουργό των Fireflies στο νοσοκομείο",
        "distractors": [
            "Ο Joel έκλεψε τις προμήθειες της κοινότητάς της",
            "Ο Joel κατέστρεψε το καταφύγιό της στο Σιάτλ",
            "Ο Joel είχε προδώσει τη στρατιωτική της μονάδα"
        ],
        "explanation": "Ο πατέρας της Abby, Jerry Anderson, ήταν ο επικεφαλής χειρουργός που επρόκειτο να χειρουργήσει την Ellie για να βρει το εμβόλιο πριν τον σκοτώσει ο Joel για να τη σώσει.",
        "funFacts": [
            "Το παιχνίδι χωρίζει την αφήγησή του στα δύο, αναγκάζοντας τον παίκτη να παίξει για περίπου 15 ώρες ως η Abby για να κατανοήσει την οπτική της γωνία.",
            "Το The Last of Us Part II κέρδισε πάνω από 320 βραβεία Game of the Year, σημειώνοντας ιστορικό ρεκόρ στη βιομηχανία."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Last_of_Us_Part_II",
        "tags": ["gaming", "the_last_of_us", "naughty_dog", "abby", "story"]
    },
    {
        "id": "gaming_med_366",
        "text": "Στο 'Uncharted 2: Among Thieves' (2009), ποια μυθική χαμένη πόλη στα Ιμαλάια αναζητά ο Nathan Drake ακολουθώντας τα ίχνη του Marco Polo;",
        "correct": "Shambhala (Σαμπάλα)",
        "distractors": ["El Dorado", "Iram of the Pillars", "Libertalia"],
        "explanation": "Στη Shambhala κρύβεται η περίφημη Πέτρα Cintamani, η οποία αποδεικνύεται ότι δεν είναι ζαφείρι αλλά απολιθωμένο κεχριμπάρι από το Δέντρο της Ζωής.",
        "funFacts": [
            "Η εμβληματική εισαγωγική σκηνή ξεκινά με τον Drake τραυματισμένο μέσα σε ένα βαγόνι τρένου που κρέμεται στο χείλος ενός παγωμένου γκρεμού.",
            "Το παιχνίδι κέρδισε πάνω από 200 βραβεία Game of the Year και θεωρείται από πολλούς ως η κορυφαία στιγμή της σειράς Uncharted."
        ],
        "source": "https://en.wikipedia.org/wiki/Uncharted_2:_Among_Thieves",
        "tags": ["gaming", "uncharted", "naughty_dog", "playstation", "nathan_drake"]
    },
    {
        "id": "gaming_med_367",
        "text": "Στο 'Uncharted 4: A Thief's End' (2016), ποια θρυλική πειρατική αποικία στη Μαδαγασκάρη αναζητούν ο Nathan και ο αδελφός του Sam Drake;",
        "correct": "Libertalia (Λιμπερτάλια)",
        "distractors": ["Port Royal", "Tortuga", "New Providence"],
        "explanation": "Η Libertalia ιδρύθηκε τον 17ο αιώνα από τον διαβόητο πειρατή Henry Avery και άλλους καπετάνιους ως μια ουτοπία όπου όλοι οι πειρατές μοιράζονταν ισότιμα τα πλούτη τους.",
        "funFacts": [
            "Ο Sam Drake (με τη φωνή του Troy Baker) επιστρέφει στη ζωή του Nathan αφού θεωρούνταν νεκρός για 15 χρόνια σε φυλακή του Παναμά.",
            "Το παιχνίδι ολοκλήρωσε οριστικά την ιστορία του Nathan Drake με έναν συγκινητικό επίλογο όπου βλέπουμε την έφηβη κόρη του, Cassie."
        ],
        "source": "https://en.wikipedia.org/wiki/Uncharted_4:_A_Thief%27s_End",
        "tags": ["gaming", "uncharted", "naughty_dog", "playstation", "henry_avery"]
    },
    {
        "id": "gaming_med_368",
        "text": "Στο 'God of War' (2018), ποιο γιγάντιο μυθικό πλάσμα γεμίζει τη λίμνη των Εννέα (Lake of Nine) και μιλάει μια αρχαία ξεχασμένη γλώσσα;",
        "correct": "Jörmungandr (Το Φίδι του Κόσμου)",
        "distractors": ["Níðhögg", "Fenrir", "Surtr"],
        "explanation": "Το Midgard Serpent (Jörmungandr) είναι τόσο τεράστιο που τυλίγει ολόκληρη τη γη, και είναι φιλικό προς τον Kratos και τον Atreus επειδή αναγνωρίζει το αίμα των Γιγάντων.",
        "funFacts": [
            "Ο Atreus είναι ο μόνος που καταφέρνει σταδιακά να μάθει και να μιλήσει την αρχαία διάλεκτο του Jörmungandr.",
            "Σύμφωνα με τη μυθολογία, στη μάχη του Ragnarök το χτύπημα του Thor είναι τόσο δυνατό ώστε στέλνει το φίδι πίσω στον χρόνο πριν καν γεννηθεί."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_(2018_video_game)",
        "tags": ["gaming", "god_of_war", "playstation", "mythology", "jormungandr"]
    },
    {
        "id": "gaming_med_369",
        "text": "Ποια είναι η ταυτότητα της μητέρας της πρωταγωνίστριας Aloy και δημιουργού του συστήματος GAIA στο 'Horizon Zero Dawn' (2017);",
        "correct": "Dr. Elisabet Sobeck",
        "distractors": ["Dr. Farzenah", "Ted Faro", "Sylens"],
        "explanation": "Η Aloy ανακαλύπτει ότι δεν γεννήθηκε φυσιολογικά, αλλά είναι ένας γενετικός κλώνος της Dr. Elisabet Sobeck που δημιουργήθηκε από την GAIA για να σώσει το σύστημα terraforming.",
        "funFacts": [
            "Ο Ted Faro ήταν ο δισεκατομμυριούχος επιχειρηματίας του οποίου τα αυτόνομα ρομπότ κατανάλωσαν όλη τη βιομάζα της Γης (Faro Plague), αναγκάζοντας τη Sobeck να σχεδιάσει το Zero Dawn.",
            "Η Aloy χρησιμοποιεί μια μικρή τριγωνική συσκευή επαυξημένης πραγματικότητας στον κρόταφο που ονομάζεται Focus."
        ],
        "source": "https://en.wikipedia.org/wiki/Horizon_Zero_Dawn",
        "tags": ["gaming", "horizon_zero_dawn", "guerrilla_games", "aloy", "lore"]
    },
    {
        "id": "gaming_med_370",
        "text": "Στο 'Ghost of Tsushima' (2020), ποιος σαμουράι εγκαταλείπει τον αυστηρό κώδικα τιμής του για να σώσει το νησί του από τη μογγολική εισβολή;",
        "correct": "Jin Sakai",
        "distractors": ["Lord Shimura", "Khotun Khan", "Sensei Ishikawa"],
        "explanation": "Ο Jin Sakai συνειδητοποιεί ότι οι παραδοσιακές τακτικές των σαμουράι οδηγούν σε βέβαιο θάνατο ενάντια στους Μογγόλους και υιοθετεί τακτικές τρόμου, δηλητηρίων και δολοφονιών ως 'The Ghost'.",
        "funFacts": [
            "Το παιχνίδι διαθέτει ειδική επιλογή εικόνας 'Kurosawa Mode' που αποδίδει τα γραφικά σε ασπρόμαυρο με κόκκους φιλμ προς τιμήν του Akira Kurosawa.",
            "Ο άνεμος (Guiding Wind) λειτουργεί ως ο φυσικός δείκτης πορείας για τον παίκτη, αντικαθιστώντας τους τεχνητούς δείκτες στην οθόνη."
        ],
        "source": "https://en.wikipedia.org/wiki/Ghost_of_Tsushima",
        "tags": ["gaming", "ghost_of_tsushima", "sucker_punch", "jin_sakai", "playstation"]
    },
    {
        "id": "gaming_med_371",
        "text": "Στο 'Marvel's Spider-Man' (2018) της Insomniac Games, ποιος θανατηφόρος βιολογικός ιός απελευθερώνεται στη Νέα Υόρκη από τον Doctor Octopus;",
        "correct": "Devil's Breath (Ανάσα του Διαβόλου / GR-27)",
        "distractors": ["Chimera Virus", "Green Goblin Serum", "Symbiote Strain"],
        "explanation": "Ο ιός Devil's Breath αναπτύχθηκε μυστικά από τον Norman Osborn και την Oscorp ως υποτιθέμενη θεραπεία για γενετικές ασθένειες, αλλά μετατρέπεται σε βιολογικό υπερόπλο.",
        "funFacts": [
            "Ο Peter Parker έρχεται αντιμέτωπος με το απόλυτο ηθικό δίλημμα στο τέλος: να χρησιμοποιήσει το μοναδικό αντίδοτο για να σώσει τη θεία May ή για να παραχθεί μαζικό εμβόλιο για ολόκληρη την πόλη.",
            "Η Insomniac Games σχεδίασε ένα από τα πιο απολαυστικά συστήματα αιώρησης με ιστούς (web swinging) που έχουν δημιουργηθεί ποτέ."
        ],
        "source": "https://en.wikipedia.org/wiki/Spider-Man_(2018_video_game)",
        "tags": ["gaming", "spider_man", "insomniac_games", "playstation", "marvel"]
    },
    {
        "id": "gaming_med_372",
        "text": "Ποιος είναι ο αγγελιοφόρος με ποδήλατο που αποκτά ηλεκτρικές υπερδυνάμεις μετά από μια τεράστια έκρηξη στο 'inFamous' (2009) της Sucker Punch;",
        "correct": "Cole MacGrath",
        "distractors": ["Delsin Rowe", "Zeke Dunbar", "Kessler"],
        "explanation": "Ο Cole MacGrath επιβιώνει από την έκρηξη της συσκευής Ray Sphere στην Empire City και αποκτά την ικανότητα να απορροφά και να εκτοξεύει ηλεκτρισμό.",
        "funFacts": [
            "Το σύστημα ηθικής του παιχνιδιού αλλάζει το χρώμα των αστραπών του Cole: μπλε για τις καλές πράξεις (Hero) και κόκκινες για τις κακές (Infamous).",
            "Στο τέλος του παιχνιδιού αποκαλύπτεται ότι ο κύριος κακός Kessler είναι στην πραγματικότητα ο ίδιος ο Cole από ένα δυστοπικό μέλλον."
        ],
        "source": "https://en.wikipedia.org/wiki/Infamous_(video_game)",
        "tags": ["gaming", "infamous", "sucker_punch", "playstation", "cole_macgrath"]
    },
    {
        "id": "gaming_med_373",
        "text": "Ποιο αρχαίο οικογενειακό βιβλίο κλεφτών προσπαθεί να ανακτήσει ο Sly Cooper στη σειρά platformers 'Sly Cooper' της Sucker Punch;",
        "correct": "Thievius Raccoonus",
        "distractors": ["The Master Thief Tome", "Cooper Family Codex", "The Shadow Ledger"],
        "explanation": "Το Thievius Raccoonus περιέχει όλες τις μυστικές κινήσεις και τεχνικές που ανέπτυξαν οι πρόγονοι του Sly σε διάφορες ιστορικές εποχές.",
        "funFacts": [
            "Η συμμορία του Sly αποτελείται από τον ίδιο (διαρρήκτης), τον Bentley (τη χελώνα-εγκέφαλο των επιχειρήσεων) και τον Murray (τον ιπποπόταμο-οδηγό και δύναμη).",
            "Η επιθεωρήτρια της Interpol Carmelita Fox καταδιώκει διαρκώς τον Sly, αναπτύσσοντας ένα αμοιβαίο ρομαντικό φλερτ."
        ],
        "source": "https://en.wikipedia.org/wiki/Sly_Cooper",
        "tags": ["gaming", "sly_cooper", "sucker_punch", "playstation", "platformer"]
    },
    {
        "id": "gaming_med_374",
        "text": "Στο 'Jak and Daxter: The Precursor Legacy' (2001), σε ποιο παράξενο υβρίδιο ζώου (Ottsel) μεταμορφώνεται ο Daxter όταν πέφτει μέσα σε ένα καζάνι με Dark Eco;",
        "correct": "Σε Ότσελ (μισή ενυδρίδα, μισή νυφίτσα)",
        "distractors": ["Σε ρακούν", "Σε κουνάβι", "Σε λεμούριο"],
        "explanation": "Ο Daxter πέφτει κατά λάθος σε μια λίμνη Dark Eco στο Misty Island και μεταμορφώνεται σε ένα μικρό πορτοκαλί Ottsel (Otter + Weasel) με ασταμάτητη φλυαρία.",
        "funFacts": [
            "Στο Jak II (2003), η Naughty Dog άλλαξε δραστικά το ύφος της σειράς μεταφέροντας τους ήρωες στη σκοτεινή δυστοπική πόλη Haven City με πυροβόλα όπλα και οχήματα.",
            "Στο Jak 3 αποκαλύπτεται ότι οι αρχαίοι μυθικοί Precursors ήταν όλοι Ottsels όπως ο Daxter."
        ],
        "source": "https://en.wikipedia.org/wiki/Jak_and_Daxter:_The_Precursor_Legacy",
        "tags": ["gaming", "jak_and_daxter", "naughty_dog", "playstation", "daxter"]
    },
    {
        "id": "gaming_med_375",
        "text": "Στη σειρά 'Ratchet & Clank' της Insomniac Games, σε ποια σπάνια εξωγήινη φυλή με μυτερά αυτιά και ουρά ανήκει ο Ratchet;",
        "correct": "Lombax",
        "distractors": ["Markazian", "Blarg", "Thug-4-Less"],
        "explanation": "Ο Ratchet πιστεύει ότι είναι ο τελευταίος επιζών Lombax στον γαλαξία, μέχρι να συναντήσει τη Rivet από μια παράλληλη διάσταση στο 'Rift Apart' (2021).",
        "funFacts": [
            "Το πιο διάσημο, πανάκριβο υπερόπλο σε όλα σχεδόν τα παιχνίδια Ratchet & Clank είναι το R.Y.N.O. (Rip Ya a New One).",
            "Ο Clank είναι ένα μικρό ρομπότ ελαττωματικής παραγωγής που διαθέτει την ψυχή ενός Zoni."
        ],
        "source": "https://en.wikipedia.org/wiki/Ratchet_%26_Clank",
        "tags": ["gaming", "ratchet_and_clank", "insomniac_games", "playstation", "lombax"]
    },
    {
        "id": "gaming_med_376",
        "text": "Ποιος είναι ο πρωταγωνιστής της σειράς 'Max Payne' (Remedy Entertainment), ένας κυνικός πρώην αστυνομικός της Νέας Υόρκης που βυθίζεται στο πένθος;",
        "correct": "Max Payne",
        "distractors": ["Alan Wake", "Jack Joyce", "Alex Casey"],
        "explanation": "Ο Max Payne χάνει τη γυναίκα και το μωρό του από τοξικομανείς υπό την επήρεια του συνθετικού ναρκωτικού Valkyr, ξεκινώντας μια ανελέητη πορεία εκδίκησης.",
        "funFacts": [
            "Το πρόσωπο του Max Payne στο αρχικό παιχνίδι του 2001 ανήκε στον ίδιο τον σεναριογράφο και δημιουργό της Remedy, Sam Lake.",
            "Το παιχνίδι εισήγαγε τον πρωτοποριακό μηχανισμό 'Bullet Time' που επέτρεπε στους παίκτες να πυροβολούν πέφτοντας σε αργή κίνηση εμπνευσμένοι από το Matrix."
        ],
        "source": "https://en.wikipedia.org/wiki/Max_Payne_(character)",
        "tags": ["gaming", "max_payne", "remedy", "sam_lake", "bullet_time"]
    },
    {
        "id": "gaming_med_377",
        "text": "Στο ατμοσφαιρικό ψυχολογικό θρίλερ 'Alan Wake' (2010) της Remedy, ποιο είναι το βασικό μέσο που χρησιμοποιεί ο Alan για να διαλύσει την ασπίδα των εχθρών Taken;",
        "correct": "Το φως ενός φακού (Flashlight)",
        "distractors": ["Αγιασμό", "Μαγικά σύμβολα", "Υπερηχητικά κύματα"],
        "explanation": "Οι εχθροί προστατεύονται από ένα πέπλο σκοταδιού· ο Alan πρέπει να εστιάσει τη δέσμη του φακού του πάνω τους για να τους κάψει την ασπίδα πριν μπορέσει να τους πυροβολήσει.",
        "funFacts": [
            "Ο Alan Wake είναι ένας επιτυχημένος συγγραφέας μυθιστορημάτων μυστηρίου που παθαίνει συγγραφικό μπλοκάρισμα και ταξιδεύει στη φανταστική πόλη Bright Falls της Ουάσινγκτον.",
            "Οι σελίδες χειρογράφου που βρίσκει ο παίκτης περιγράφουν γεγονότα που πρόκειται να συμβούν λίγα λεπτά αργότερα."
        ],
        "source": "https://en.wikipedia.org/wiki/Alan_Wake",
        "tags": ["gaming", "alan_wake", "remedy", "horror", "action"]
    },
    {
        "id": "gaming_med_378",
        "text": "Στο παιχνίδι 'Control' (2019) της Remedy, ποιο είναι το παράξενο μεταβαλλόμενο κτίριο της Νέας Υόρκης που στεγάζει το Federal Bureau of Control (FBC);",
        "correct": "The Oldest House (Ο Αρχαιότερος Οίκος)",
        "distractors": ["The Dark Place", "The Black Rock Foundry", "The Panopticon"],
        "explanation": "Το Oldest House είναι ένας βρουταλιστικός ουρανοξύστης που είναι πολύ μεγαλύτερος στο εσωτερικό του απ' ό,τι απ' έξω και αποτελεί ένα 'Place of Power' που δεν εντοπίζεται από τους κοινούς ανθρώπους.",
        "funFacts": [
            "Η πρωταγωνίστρια Jesse Faden χρησιμοποιεί το παραφυσικό όπλο Service Weapon, το οποίο μπορεί να αλλάζει μορφή (περίστροφο, καραμπίνα, πολυβόλο).",
            "Το Control και το Alan Wake συνδέονται επίσημα στο κοινό σύμπαν 'Remedy Connected Universe'."
        ],
        "source": "https://en.wikipedia.org/wiki/Control_(video_game)",
        "tags": ["gaming", "control", "remedy", "jesse_faden", "action"]
    },
    {
        "id": "gaming_med_379",
        "text": "Στο 'Prey' (2017) της Arkane Studios, ποια εξωγήινη φυλή που αλλάζει μορφή και μεταμορφώνεται σε καθημερινά αντικείμενα (κούπες, καρέκλες) τρομοκρατεί τον διαστημικό σταθμό Talos I;",
        "correct": "Typhon (Mimics)",
        "distractors": ["Necromorphs", "Combine", "Xenomorphs"],
        "explanation": "Τα Mimics είναι σκοτεινά εξωγήινα πλάσματα που μπορούν να πάρουν τη μορφή οποιουδήποτε αντικειμένου στο περιβάλλον, στήνοντας αιφνιδιαστικές φονικές παγίδες στον Morgan Yu.",
        "funFacts": [
            "Το καινοτόμο όπλο GLOO Cannon επιτρέπει στον παίκτη να παγώνει εχθρούς αλλά και να δημιουργεί σκάλες και ράμπες στον τοίχο για να φτάνει ψηλά σημεία.",
            "Ο παίκτης μπορεί να εγκαταστήσει εξωγήινες δυνάμεις Neuromods, αποκτώντας ο ίδιος την ικανότητα να μεταμορφώνεται σε αντικείμενα."
        ],
        "source": "https://en.wikipedia.org/wiki/Prey_(2017_video_game)",
        "tags": ["gaming", "prey", "arkane", "bethesda", "immersive_sim"]
    },
    {
        "id": "gaming_med_380",
        "text": "Στο 'Deathloop' (2021) της Arkane Studios, ποιον πρέπει να εξοντώσει ο Colt Vahn σε μία μόνο ημέρα στο νησί Blackreef για να σπάσει τον χρονικό βρόχο;",
        "correct": "Και τους 8 Visionaries (Οραματιστές)",
        "distractors": ["Μόνο την αντίπαλό του Julianna Blake", "Τον ηγέτη της στρατιωτικής φρουράς", "Τον αρχικό επιστήμονα του πρότζεκτ"],
        "explanation": "Ο Colt πρέπει να σχεδιάσει την τέλεια σειρά δολοφονιών και για τους 8 Visionaries στις 4 χρονικές περιόδους της ημέρας, καθώς αν επιζήσει έστω κι ένας, ο βρόχος επανεκκινεί τα μεσάνυχτα.",
        "funFacts": [
            "Η αντίπαλός του Julianna Blake μπορεί να ελεγχθεί από άλλον παίκτη online μέσω ενός ασύμμετρου multiplayer συστήματος εισβολής (invasion).",
            "Το παιχνίδι μοιράζεται το ίδιο ιστορικό σύμπαν με τη σειρά Dishonored της Arkane Studios στο μακρινό μέλλον."
        ],
        "source": "https://en.wikipedia.org/wiki/Deathloop",
        "tags": ["gaming", "deathloop", "arkane", "bethesda", "fps"]
    },
    {
        "id": "gaming_med_381",
        "text": "Στο 'Wolfenstein: The New Order' (2014), ποιος σκληροτράχηλος Αμερικανός στρατιώτης ξυπνά από κώμα το 1960 σε έναν κόσμο όπου οι Ναζί κέρδισαν τον Β' Παγκόσμιο Πόλεμο;",
        "correct": "William 'B.J.' Blazkowicz",
        "distractors": ["Fergus Reid", "Probst Wyatt", "Deathshead"],
        "explanation": "Ο B.J. Blazkowicz συνέρχεται σε ένα πολωνικό άσυλο και εντάσσεται στην αντίσταση του Kreisau Circle για να πολεμήσει το ναζιστικό καθεστώς του General Deathshead.",
        "funFacts": [
            "Το παιχνίδι επιτρέπει στον παίκτη να κρατάει δύο αυτόματα τουφέκια ή καραμπίνες ταυτόχρονα (dual-wielding) για εκρηκτική δράση.",
            "Σύμφωνα με το παλιό lore της id Software, ο Blazkowicz είναι ο μακρινός πρόγονος του Commander Keen και του Doom Slayer."
        ],
        "source": "https://en.wikipedia.org/wiki/Wolfenstein:_The_New_Order",
        "tags": ["gaming", "wolfenstein", "machinegames", "bethesda", "fps"]
    },
    {
        "id": "gaming_med_382",
        "text": "Ποιο είναι το όνομα του κυβερνο-αναβαθμισμένου διευθυντή της UAC με το μεταλλικό ρομποτικό σώμα στο 'Doom' (2016);",
        "correct": "Dr. Samuel Hayden",
        "distractors": ["Olivia Pierce", "Betruger", "Pierce Rossi"],
        "explanation": "Ο Dr. Hayden μετέφερε τον εγκέφαλό του σε ένα τεράστιο ανδροειδές σώμα ύψους 3 μέτρων μετά από καρκίνο και εκμεταλλεύεται την ενέργεια Argent από την Κόλαση για τη Γη.",
        "funFacts": [
            "Στο Doom Eternal αποκαλύπτεται ότι ο Hayden ήταν στην πραγματικότητα ο Seraphim (Samur Maykr) που είχε χαρίσει υπεράνθρωπες δυνάμεις στον Doom Slayer.",
            "Τη χαρακτηριστική βαθιά ρομποτική φωνή του Hayden δάνεισε ο ηθοποιός Darin De Paul."
        ],
        "source": "https://en.wikipedia.org/wiki/Doom_(2016_video_game)",
        "tags": ["gaming", "doom", "id_software", "samuel_hayden", "fps"]
    },
    {
        "id": "gaming_med_383",
        "text": "Ποια διάσημη ιαχή του εκφωνητή ακούγεται στο 'Unreal Tournament' όταν ένας παίκτης πετυχαίνει πέντε διαδοχικές εξοντώσεις χωρίς να πεθάνει;",
        "correct": "M-M-M-Monster Kill!",
        "distractors": ["Double Kill!", "Godlike!", "Rampage!"],
        "explanation": "Η κλιμάκωση των ανακοινώσεων (Double Kill -> Multi Kill -> Ultra Kill -> Monster Kill -> Ludicrous Kill / Holy Shit!) έγινε θρύλος στα arena shooters.",
        "funFacts": [
            "Τα ηχητικά δείγματα του εκφωνητή του Unreal Tournament χρησιμοποιήθηκαν αργότερα στο αυθεντικό mod του DotA στο Warcraft III και σε αμέτρητα άλλα games.",
            "Η φράση 'Headshot!' με τη βαριά αντρική φωνή έγινε παγκόσμιο πολιτισμικό σύμβολο του PC gaming."
        ],
        "source": "https://en.wikipedia.org/wiki/Unreal_Tournament",
        "tags": ["gaming", "unreal_tournament", "epic_games", "fps", "retro"]
    },
    {
        "id": "gaming_med_384",
        "text": "Στο κλασικό stealth 'Thief: The Dark Project' (1998) της Looking Glass Studios, ποιος είναι ο κυνικός δεξιοτέχνης κλέφτης που χρησιμοποιεί βέλη νερού για να σβήνει δάδες;",
        "correct": "Garrett",
        "distractors": ["Corvo", "Aragami", "Rikimaru"],
        "explanation": "Ο Garrett εκπαιδεύτηκε από το μυστικό τάγμα των Keepers και ειδικεύεται στο να κινείται στις σκιές αποφεύγοντας θορυβώδεις επιφάνειες (μάρμαρα, μέταλλα) με βέλη βρύων (moss arrows).",
        "funFacts": [
            "Το Thief ήταν το πρώτο παιχνίδι που εφάρμοσε ρεαλιστική διάδοση ήχου: οι φρουροί άκουγαν τα βήματα του παίκτη ανάλογα με το υλικό του πατώματος.",
            "Το ρόπαλο (Blackjack) χρησιμοποιούνταν για να αναισθητοποιεί φρουρούς αθόρυβα από πίσω χωρίς να τους σκοτώνει."
        ],
        "source": "https://en.wikipedia.org/wiki/Thief:_The_Dark_Project",
        "tags": ["gaming", "thief", "looking_glass", "stealth", "classics"]
    },
    {
        "id": "gaming_med_385",
        "text": "Στη σειρά RPG 'Baldur's Gate' (1 & 2) της BioWare, ποια σκοτεινή θεϊκή κληρονομιά κουβαλάει ο πρωταγωνιστής στο αίμα του;",
        "correct": "Είναι Bhaalspawn (παιδί του Bhaal, του Άρχοντα της Δολοφονίας)",
        "distractors": [
            "Είναι απόγονος της Mystra, θεάς της μαγείας",
            "Είναι φορέας της ψυχής του Cyric",
            "Είναι avatar του Helm"
        ],
        "explanation": "Ο Bhaal προέβλεψε τον θάνατό του κατά την Εποχή των Αναταραχών (Time of Troubles) και άφησε πίσω του πολυάριθμους θνητούς απογόνους (Bhaalspawn) για να μπορέσει να αναστηθεί μέσω του αίματός τους.",
        "funFacts": [
            "Ο θετός πατέρας του ήρωα που τον μεγάλωσε στη βιβλιοθήκη του Candlekeep ήταν ο σοφός μάγος Gorion.",
            "Στο Baldur's Gate II: Shadows of Amn, ο κακός Jon Irenicus (με τη φωνή του David Warner) βασανίζει τον παίκτη για να του κλέψει τη θεϊκή σπίθα."
        ],
        "source": "https://en.wikipedia.org/wiki/Baldur%27s_Gate",
        "tags": ["gaming", "baldurs_gate", "bioware", "dnd", "rpg"]
    },
    {
        "id": "gaming_med_386",
        "text": "Στο ιστορικό RPG 'Baldur's Gate 3' (2023) της Larian Studios, ποιο παρασιτικό πλάσμα έχει τοποθετηθεί πίσω από το μάτι των πρωταγωνιστών;",
        "correct": "Ένα παρασιτικό σκουλήκι (Tadpole) των Mind Flayers (Illithids)",
        "distractors": ["Ένας κρύσταλλος Netherese", "Ένα έντομο του Bhaal", "Μια προνύμφη δαίμονα"],
        "explanation": "Το tadpole απειλεί να μεταμορφώσει τον φορέα του σε Mind Flayer μέσω της διαδικασίας ceramorphosis, αλλά η μυστηριώδης προστασία του Astral Prism αναστέλλει τη μεταμόρφωση.",
        "funFacts": [
            "Το Baldur's Gate 3 σάρωσε όλα τα μεγάλα βραβεία Game of the Year (TGA, BAFTA, D.I.C.E., Golden Joysticks, GDC), σημειώνοντας ένα άνευ προηγουμένου grand slam.",
            "Ο παίκτης μπορεί να αγκαλιάσει τις δυνάμεις του παρασίτου καταναλώνοντας περισσότερα tadpoles για να ξεκλειδώσει ισχυρές Illithid δεξιότητες."
        ],
        "source": "https://en.wikipedia.org/wiki/Baldur%27s_Gate_3",
        "tags": ["gaming", "baldurs_gate_3", "larian_studios", "dnd", "goty"]
    },
    {
        "id": "gaming_med_387",
        "text": "Στο αριστούργημα της Black Isle 'Planescape: Torment' (1999), πού ξυπνάει ο αθάνατος πρωταγωνιστής 'The Nameless One' στην αρχή της ιστορίας;",
        "correct": "Πάνω σε μια μεταλλική πλάκα στο Νεκροτομείο της πόλης Sigil",
        "distractors": ["Σε ένα κελί του Carceri", "Στον πυθμένα της Αστρικής Θάλασσας", "Στην ταβέρνα Smoldering Corpse"],
        "explanation": "Ο Nameless One ξυπνά καλυμμένος με ουλές και τατουάζ χωρίς μνήμη, συνοδευόμενος από τον Morte, ένα ιπτάμενο κρανίο με σαρκαστικό χιούμορ.",
        "funFacts": [
            "Το κεντρικό φιλοσοφικό ερώτημα που θέτει το παιχνίδι είναι: 'What can change the nature of a man?' (Τι μπορεί να αλλάξει τη φύση ενός ανθρώπου;).",
            "Το σενάριο του παιχνιδιού από τον Chris Avellone περιέχει πάνω από 800.000 λέξεις, ξεπερνώντας σε μέγεθος το 'Πόλεμος και Ειρήνη'."
        ],
        "source": "https://en.wikipedia.org/wiki/Planescape:_Torment",
        "tags": ["gaming", "planescape_torment", "black_isle", "rpg", "chris_avellone"]
    },
    {
        "id": "gaming_med_388",
        "text": "Ποιο είναι το μυθικό τεχνούργημα terraforming που αναζητά ο 'Chosen One' στο 'Fallout 2' (1998) για να σώσει το πεινασμένο χωριό του Arroyo;",
        "correct": "G.E.C.K. (Garden of Eden Creation Kit)",
        "distractors": ["Water Chip", "Platinum Chip", "Purification Core"],
        "explanation": "Το G.E.C.K. περιέχει τεχνολογία αποκατάστασης εδάφους, καθαρισμού ακτινοβολίας και συμπιεσμένους σπόρους για τη δημιουργία εύφορων κοινοτήτων μετά τον πόλεμο.",
        "funFacts": [
            "Ο κύριος εχθρός στο Fallout 2 είναι το Enclave, τα απομεινάρια της παλιάς αμερικανικής κυβέρνησης υπό τον πρόεδρο Dick Richardson.",
            "Το τελικό αφεντικό Frank Horrigan είναι ένας γιγάντιος μεταλλαγμένος στρατιώτης με εξωσκελετική πανοπλία Power Armor συνδεδεμένη απευθείας στο σώμα του."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout_2",
        "tags": ["gaming", "fallout", "black_isle", "interplay", "rpg"]
    },
    {
        "id": "gaming_med_389",
        "text": "Ποια είναι η τεράστια ανατροπή (plot twist) σχετικά με την ταυτότητα του πρωταγωνιστή στο 'Star Wars: Knights of the Old Republic' (2003) της BioWare;",
        "correct": "Ο ίδιος ο παίκτης αποκαλύπτεται ότι είναι ο πρώην Σκοτεινός Άρχοντας Darth Revan",
        "distractors": [
            "Ο παίκτης είναι ένας κλώνος του Αυτοκράτορα",
            "Ο Bastila Shan είναι η μητέρα του παίκτη",
            "Ο Malak είναι ο χαμένος αδελφός του παίκτη"
        ],
        "explanation": "Το Συμβούλιο των Jedi έσβησε τις αναμνήσεις του ηττημένου Darth Revan και του εμφύτευσε μια νέα ταυτότητα με την ελπίδα να τον στρέψει στο Φως.",
        "funFacts": [
            "Το ρομπότ δολοφόνος HK-47 αναφέρεται υποτιμητικά σε όλους τους ανθρώπους και οργανικούς χαρακτήρες ως 'meatbags' (σακούλες κρέατος).",
            "Η αποκάλυψη του Revan θεωρείται μία από τις πιο καλοστημένες ανατροπές στην ιστορία των RPGs."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars:_Knights_of_the_Old_Republic",
        "tags": ["gaming", "kotor", "bioware", "star_wars", "revan"]
    },
    {
        "id": "gaming_med_390",
        "text": "Στο 'Star Wars Knights of the Old Republic II: The Sith Lords' (2004) της Obsidian, ποια τυφλή δασκάλα Jedi ασκεί δριμεία κριτική στη φύση της ίδιας της Δύναμης (The Force);",
        "correct": "Kreia (Darth Traya)",
        "distractors": ["Atris", "Visas Marr", "Darth Sion"],
        "explanation": "Η Kreia απεχθάνεται τη Δύναμη επειδή πιστεύει ότι έχει δική της συνείδηση και χειραγωγεί τη μοίρα των όντων σε αιώνιους κύκλους πολέμου, επιδιώκοντας να την καταστρέψει.",
        "funFacts": [
            "Ο σεναριογράφος Chris Avellone έγραψε την Kreia για να αμφισβητήσει τον απόλυτο δυϊσμό Καλού-Κακού (Jedi εναντίον Sith) του παραδοσιακού Star Wars.",
            "Ο πρωταγωνιστής είναι ο/η Jedi Exile, το μοναδικό άτομο που απέκοψε οικειοθελώς τη σύνδεσή του με τη Δύναμη μετά τη μάχη του Malachor V."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars_Knights_of_the_Old_Republic_II:_The_Sith_Lords",
        "tags": ["gaming", "kotor", "obsidian", "star_wars", "kreia"]
    },
    {
        "id": "gaming_med_391",
        "text": "Στην τελική αποστολή 'The Suicide Mission' του 'Mass Effect 2' (2010), τι μπορεί να συμβεί αν ο παίκτης δεν αναβαθμίσει το Normandy και κάνει λάθος επιλογές ειδικών;",
        "correct": "Μπορεί να πεθάνει ολόκληρη η ομάδα, συμπεριλαμβανομένου και του ίδιου του Shepard",
        "distractors": [
            "Το πλοίο ανατινάζεται αυτόματα πριν περάσει το Omega-4 Relay",
            "Ο παίκτης αναγκάζεται να συμμαχήσει με τους Collectors",
            "Οι Reapers φτάνουν αμέσως στη Γη"
        ],
        "explanation": "Αν ο Shepard δεν έχει κερδίσει την πίστη (loyalty) του πληρώματος και αναθέσει λάθος ρόλους (ειδικός αεραγωγών, βιοτικό πεδίο, αρχηγός ομάδας), τα μέλη της ομάδας εξοντώνονται ένα προς ένα.",
        "funFacts": [
            "Αν πεθάνει ο ίδιος ο Shepard στο τέλος, ο Joker είναι ο μόνος επιζών και το save file δεν μπορεί να εισαχθεί στο Mass Effect 3.",
            "Η αποστολή Suicide Mission συνοδεύεται από το επικό ορχηστρικό θέμα 'Suicide Mission' των Jack Wall και Sam Hulick."
        ],
        "source": "https://en.wikipedia.org/wiki/Mass_Effect_2",
        "tags": ["gaming", "mass_effect", "bioware", "shepard", "suicide_mission"]
    },
    {
        "id": "gaming_med_392",
        "text": "Στο 'Cyberpunk 2077' (2020), ποιος ροκ σταρ και αντιστασιακός τρομοκράτης (με τη μορφή και φωνή του Keanu Reeves) είναι παγιδευμένος στο βιοτσίπ Relic μέσα στο κεφάλι του V;",
        "correct": "Johnny Silverhand (Robert John Linder)",
        "distractors": ["Kerry Eurodyne", "Alt Cunningham", "Morgan Blackhand"],
        "explanation": "Ο Johnny Silverhand ήταν ο κιθαρίστας του συγκροτήματος Samurai που ανατίναξε τον πύργο Arasaka Tower με πυρηνική βόμβα το 2023 και η ψηφιακή του συνείδηση (en粋) απειλεί να καταλάβει το σώμα του V.",
        "funFacts": [
            "Ο Keanu Reeves ηχογράφησε δεκάδες ώρες διαλόγων και έκανε εκτεταμένο motion capture, μένοντας τόσο ενθουσιασμένος με τον ρόλο που ζήτησε να διπλασιαστεί ο χρόνος παρουσίας του χαρακτήρα.",
            "Το διάσημο τραγούδι των Samurai 'Chippin' In' ηχογραφήθηκε στην πραγματικότητα από το σουηδικό πανκ συγκρότημα Refused."
        ],
        "source": "https://en.wikipedia.org/wiki/Johnny_Silverhand",
        "tags": ["gaming", "cyberpunk_2077", "cd_projekt_red", "johnny_silverhand"]
    },
    {
        "id": "gaming_med_393",
        "text": "Ποια πανίσχυρη ιαπωνική πολυεθνική megacorporation κυριαρχεί στην Night City και αποτελεί τον κύριο ανταγωνιστή στο 'Cyberpunk 2077';",
        "correct": "Arasaka Corporation",
        "distractors": ["Militech", "Kang Tao", "Biotechnica"],
        "explanation": "Η Arasaka διοικείται από τον υπεραιωνόβιο πατριάρχη Saburo Arasaka και ειδικεύεται στην ασφάλεια, τα όπλα και την τεχνολογία ψηφιοποίησης ανθρώπινων ψυχών (Soulkiller).",
        "funFacts": [
            "Ο κύριος αμερικανικός αντίπαλος της Arasaka στον τομέα των στρατιωτικών εξοπλισμών είναι η εταιρεία Militech.",
            "Ο Saburo Arasaka ήταν 158 ετών κατά τα γεγονότα του παιχνιδιού και επιδίωκε την αιώνια ψηφιακή αθανασία."
        ],
        "source": "https://en.wikipedia.org/wiki/Cyberpunk_2077",
        "tags": ["gaming", "cyberpunk_2077", "cd_projekt_red", "arasaka", "lore"]
    },
    {
        "id": "gaming_med_394",
        "text": "Στο 'Elden Ring', ποια ημισέληνος μάγισσα οργάνωσε τη 'Νύχτα των Μαύρων Μαχαιριών' κλέβοντας τον Ρούνο του Θανάτου για να απαλλαγεί από το σώμα της;",
        "correct": "Ranni the Witch",
        "distractors": ["Rennala", "Malenia", "Marika"],
        "explanation": "Η Ranni συνωμότησε με τις Black Knife Assassins για να δολοφονήσει τον Godwyn the Golden, απελευθερώνοντας την ψυχή της από το σώμα της και κατοικώντας μέσα σε μια τετραχέρικη πορσελάνινη κούκλα.",
        "funFacts": [
            "Το questline της Ranni οδηγεί σε ένα από τα πιο δημοφιλή τέλη του παιχνιδιού, την 'Εποχή των Αστεριών' (Age of the Stars).",
            "Οι πιστοί της ακόλουθοι περιλαμβάνουν τον πολεμιστή-λύκο Blaidd, τον γίγαντα σιδερά Iji και τον μάγο Seluvis."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "tags": ["gaming", "elden_ring", "fromsoftware", "ranni", "lore"]
    },
    {
        "id": "gaming_med_395",
        "text": "Ποιο είναι το όνομα του κυνηγού και πρωταγωνιστή στο 'The Witcher 2: Assassins of Kings' (2011) που δολοφονεί τον βασιλιά Foltest ενοχοποιώντας τον Geralt;",
        "correct": "Letho of Gulet",
        "distractors": ["Serrit", "Auckes", "Iorveth"],
        "explanation": "Ο Letho είναι ένας ογκώδης Witcher από τη Σχολή της Οχιάς (School of the Viper) που συμμαχεί με την Αυτοκρατορία της Nilfgaard για να δολοφονήσει τους μονάρχες των Βορείων Βασιλείων.",
        "funFacts": [
            "Αν ο Geralt επιλέξει να χαρίσει τη ζωή στον Letho στο τέλος του The Witcher 2, μπορεί να τον συναντήσει ξανά και να τον στρατολογήσει για τη μάχη του Kaer Morhen στο The Witcher 3.",
            "Το The Witcher 2 προσέφερε μια ριζοσπαστική διακλάδωση: ολόκληρο το δεύτερο κεφάλαιο ήταν εντελώς διαφορετικό ανάλογα με το αν ο παίκτης ακολουθούσε τον Iorveth ή τον Vernon Roche."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Witcher_2:_Assassins_of_Kings",
        "tags": ["gaming", "the_witcher", "cd_projekt_red", "letho", "rpg"]
    },
    {
        "id": "gaming_med_396",
        "text": "Στο 'Dragon Age II' (2011), σε ποια παραθαλάσσια πόλη των Free Marches καταφεύγει ο Hawke ως πρόσφυγας και αναδεικνύεται σε Πρωταθλητή (Champion);",
        "correct": "Kirkwall",
        "distractors": ["Denerim", "Val Royeaux", "Antiva City"],
        "explanation": "Η ιστορία διαδραματίζεται επί μία δεκαετία μέσα στην πόλη Kirkwall, όπου οι εντάσεις μεταξύ των Αποστατών Μάγων και των Ναϊτών κορυφώνονται με την έκρηξη του ναού από τον Anders.",
        "funFacts": [
            "Ολόκληρη η ιστορία του Hawke εξιστορείται από τον νάνο αφηγητή Varric Tethras υπό ανάκριση από την Ιεροεξετάστρια Cassandra Pentaghast.",
            "Η αγαπημένη βαλλίστρα του Varric έχει το όνομα 'Bianca'."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon_Age_II",
        "tags": ["gaming", "dragon_age", "bioware", "hawke", "rpg"]
    },
    {
        "id": "gaming_med_397",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο 'Grand Theft Auto: Vice City Stories' (2006) στο PSP, ο οποίος είναι αδελφός του Lance Vance;",
        "correct": "Victor 'Vic' Vance",
        "distractors": ["Pete Vance", "Ricardo Diaz", "Phil Cassidy"],
        "explanation": "Ο Vic Vance είναι ένας δεκανέας του αμερικανικού στρατού στη βάση Fort Baxter που μπλέκει με το εμπόριο ναρκωτικών για να πληρώσει τα ιατρικά έξοδα του άρρωστου αδελφού του Pete.",
        "funFacts": [
            "Ο Vic Vance είναι ο χαρακτήρας που δολοφονείται στην πρώτη κιόλας σκηνή ανταλλαγής ναρκωτικών στην αρχή του αυθεντικού GTA: Vice City (2002).",
            "Το παιχνίδι περιλάμβανε μια αποστολή όπου ο παίκτης έπρεπε να προστατεύσει τον διάσημο τραγουδιστή Phil Collins στη συναυλία του."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City_Stories",
        "tags": ["gaming", "gta", "rockstar", "psp", "vice_city"]
    },
    {
        "id": "gaming_med_398",
        "text": "Στο 'Grand Theft Auto: Chinatown Wars' (2009) στο Nintendo DS και PSP, ποιος νεαρός γιος δολοφονημένου αρχηγού της Triad φτάνει στη Liberty City;",
        "correct": "Huang Lee",
        "distractors": ["Wu Zi Mu", "Hsin Jaoming", "Chan Jaoming"],
        "explanation": "Ο Huang Lee ταξιδεύει στη Liberty City για να παραδώσει το αρχαίο οικογενειακό σπαθί Yu Jian στον θείο του Kenny, αλλά πέφτει σε ενέδρα και το σπαθί κλέβεται.",
        "funFacts": [
            "Το παιχνίδι αξιοποίησε πλήρως την οθόνη αφής του Nintendo DS για μίνι παιχνίδια όπως το άναμμα της μίζας αυτοκινήτων με καλώδια (hotwiring), η συναρμολόγηση βομβών και το εμπόριο ναρκωτικών.",
            "Παρά την ισομετρική κάμερα από ψηλά, αποτελεί ένα από τα πιο υψηλά βαθμολογημένα παιχνίδια στην ιστορία του Nintendo DS (93/100 στο Metacritic)."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto:_Chinatown_Wars",
        "tags": ["gaming", "gta", "rockstar", "nintendo_ds", "handheld"]
    },
    {
        "id": "gaming_med_399",
        "text": "Στο 'Red Dead Redemption: Undead Nightmare' (2010), ποιο μυθικό πλάσμα της αποκάλυψης μπορεί να δαμάσει ο John Marston ανάμεσα στα τέσσερα Άλογα της Αποκάλυψης;",
        "correct": "Πόλεμος (War), Λιμός (Famine), Θάνατος (Death) και Λοιμός (Pestilence)",
        "distractors": [
            "Κέρβερος, Ύδρα, Χίμαιρα και Μινώταυρος",
            "Πήγασος, Μονόκερος, Γρύπας και Ιππόγρυπας",
            "Σκύλλα, Χάρυβδη, Σφίγγα και Μέδουσα"
        ],
        "explanation": "Το standalone expansion μετέτρεψε ολόκληρο τον χάρτη σε ζόμπι αποκάλυψη, όπου ο παίκτης μπορεί να βρει και να ιππεύσει τα Τέσσερα Άλογα της Αποκάλυψης, καθώς και έναν Μονόκερο.",
        "funFacts": [
            "Το άλογο του Πολέμου (War) βάζει φωτιά σε όποιο ζόμπι αγγίξει καθώς καλπάζει.",
            "Το Undead Nightmare θεωρείται ευρέως ως ένα από τα σπουδαιότερα video game DLCs όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/Red_Dead_Redemption:_Undead_Nightmare",
        "tags": ["gaming", "red_dead_redemption", "rockstar", "undead_nightmare", "zombies"]
    },
    {
        "id": "gaming_med_400",
        "text": "Ποιος είναι ο μικρός πλεκτός πάνινος ήρωας της Media Molecule που πρωταγωνιστεί στη σειρά δημιουργικών platformers 'LittleBigPlanet' στο PlayStation;",
        "correct": "Sackboy",
        "distractors": ["Astro Bot", "Knack", "Tearaway"],
        "explanation": "Ο Sackboy έγινε ανεπίσημη μασκότ της Sony στο PS3, ενσαρκώνοντας το μότο 'Play, Create, Share' με εκατομμύρια πίστες φτιαγμένες από τους ίδιους τους παίκτες.",
        "funFacts": [
            "Οι παίκτες δημιούργησαν πάνω από 10 εκατομμύρια μοναδικά επίπεδα στα παιχνίδια LittleBigPlanet.",
            "Στο PS5 ο ήρωας απέκτησε το δικό του αυτόνομο 3D platformer, το 'Sackboy: A Big Adventure' (2020)."
        ],
        "source": "https://en.wikipedia.org/wiki/LittleBigPlanet",
        "tags": ["gaming", "littlebigplanet", "media_molecule", "playstation", "sackboy"]
    },
    {
        "id": "gaming_med_401",
        "text": "Στο 'Quantum Break' (2016) της Remedy Entertainment, ποιος πρωταγωνιστής αποκτά την ικανότητα να παγώνει και να στρεβλώνει τον χρόνο μετά από ένα πείραμα;",
        "correct": "Jack Joyce",
        "distractors": ["Paul Serene", "William Joyce", "Martin Hatch"],
        "explanation": "Ο Jack Joyce (ενσαρκωμένος από τον ηθοποιό Shawn Ashmore) μάχεται ενάντια στον παλιό του φίλο Paul Serene και την εταιρεία Monarch Solutions για να αποτρέψει το Τέλος του Χρόνου.",
        "funFacts": [
            "Το παιχνίδι συνδύαζε gameplay δράσης με πραγματικά επεισόδια τηλεοπτικής σειράς ζωντανής δράσης (live-action) μεταξύ των κεφαλαίων.",
            "Τον ρόλο του κακού Paul Serene υποδύθηκε ο διάσημος ηθοποιός Aidan Gillen (Littlefinger από το Game of Thrones)."
        ],
        "source": "https://en.wikipedia.org/wiki/Quantum_Break",
        "tags": ["gaming", "quantum_break", "remedy", "xbox", "action"]
    },
    {
        "id": "gaming_med_402",
        "text": "Στο πρώτο 'Silent Hill' (1999) στο PlayStation, ποια είναι η επτάχρονη υιοθετημένη κόρη που αναζητά απεγνωσμένα ο συγγραφέας Harry Mason;",
        "correct": "Cheryl Mason",
        "distractors": ["Heather Mason", "Alessa Gillespie", "Laura"],
        "explanation": "Ο Harry τρακάρει με το αυτοκίνητό του στα περίχωρα του Silent Hill και όταν συνέρχεται διαπιστώνει ότι η Cheryl έχει εξαφανιστεί μέσα στην πυκνή ομίχλη.",
        "funFacts": [
            "Η Cheryl αποκαλύπτεται ότι είναι η μετενσάρκωση του αγνού μισού της ψυχής της βασανισμένης Alessa Gillespie.",
            "Στο Silent Hill 3 (2003), η Cheryl έχει μεγαλώσει υπό το νέο όνομα Heather Mason και πρωταγωνιστεί στην επιστροφή στην εφιαλτική πόλη."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_(video_game)",
        "tags": ["gaming", "silent_hill", "konami", "survival_horror", "cheryl"]
    },
    {
        "id": "gaming_med_403",
        "text": "Στο 'Silent Hill 2' (2001), ποια τραγική χαρακτήρας λέει στον James τη συγκλονιστική φράση 'For me, it's always like this' καθώς ανεβαίνει μια φλεγόμενη σκάλα;",
        "correct": "Angela Orosco",
        "distractors": ["Maria", "Laura", "Mary Shepherd-Sunderland"],
        "explanation": "Η Angela βλέπει τον κόσμο του Silent Hill ως μια μόνιμη, αφόρητη κόλαση από φλόγες, αντανακλώντας το φρικτό τραύμα της χρόνιας κακοποίησης από τον πατέρα της.",
        "funFacts": [
            "Το τέρας Abstract Daddy (Doorman) που αντιμετωπίζει ο James είναι η εκδήλωση του πατέρα της Angela και του κρεβατιού των βασανιστηρίων της.",
            "Η σκηνή της φλεγόμενης σκάλας θεωρείται από τις πιο βαθιές και ανατριχιαστικές αποτυπώσεις ψυχολογικού πόνου στα βιντεοπαιχνίδια."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_2",
        "tags": ["gaming", "silent_hill", "konami", "psychological_horror"]
    },
    {
        "id": "gaming_med_404",
        "text": "Στο 'Metal Gear Solid V: The Phantom Pain' (2015), ποια σοκαριστική αλήθεια αποκαλύπτεται για την πραγματική ταυτότητα του Venom Snake (Punished Snake);",
        "correct": "Είναι ο στρατιωτικός γιατρός του Big Boss που υποβλήθηκε σε πλαστική χειρουργική και ύπνωση",
        "distractors": [
            "Είναι ένας ρομποτικός κυβερνο-κλώνος",
            "Είναι ο πραγματικός Naked Snake χωρίς καμία αλλαγή",
            "Είναι ο Kazuhira Miller με μεταμφίεση"
        ],
        "explanation": "Ο Venom Snake είναι ο επικεφαλής γιατρός του ελικοπτέρου από το Ground Zeroes, ο οποίος μεταμορφώθηκε σε 'σσωσία' (phantom) του Big Boss για να λειτουργήσει ως δόλωμα για τον κόσμο.",
        "funFacts": [
            "Ο Venom Snake είναι ο τελικός αρχηγός του αυθεντικού 8-bit παιχνιδιού Metal Gear (1987) στο MSX2 που σκοτώνει ο Solid Snake.",
            "Τη φωνή του Venom Snake δάνεισε ο διάσημος ηθοποιός Kiefer Sutherland."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_V:_The_Phantom_Pain",
        "tags": ["gaming", "metal_gear", "hideo_kojima", "venom_snake", "plot_twist"]
    },
    {
        "id": "gaming_med_405",
        "text": "Στο 'God of War Ragnarök' (2022), ποιος θεός αποκαλύπτεται ότι έχει πάρει τη μορφή του αιχμάλωτου θεού Tyr παρακολουθώντας τις κινήσεις του Kratos;",
        "correct": "Ο Odin (Όντιν)",
        "distractors": ["Ο Heimdall", "Ο Thor", "Ο Freyr"],
        "explanation": "Ο Πατέρας των Πάντων Odin είχε φυλακίσει τον πραγματικό Tyr και είχε πάρει τη μορφή του μέσα στο σπίτι του Sindri, κατασκοπεύοντας τους ήρωες και σκοτώνοντας τελικά τον νάνο Brok.",
        "funFacts": [
            "Η δολοφονία του Brok από τον ψεύτικο Tyr οδηγεί τον Sindri σε βαθιά θλίψη και οργή, απομακρύνοντάς τον από τον Kratos και τον Atreus.",
            "Τον Odin ενσάρκωσε με μια εξαιρετική, καθημερινή ερμηνεία ο ηθοποιός Richard Schiff."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_Ragnar%C3%B6k",
        "tags": ["gaming", "god_of_war", "playstation", "odin", "story"]
    },
    {
        "id": "gaming_med_406",
        "text": "Στο 'Horizon Zero Dawn', ποιο κακόβουλο δευτερεύον πρόγραμμα (sub-function) της GAIA αποκτά συνείδηση και προσπαθεί να αφανίσει ξανά τη ζωή στη Γη;",
        "correct": "HADES",
        "distractors": ["HEPHAESTUS", "APOLLO", "MINERVA"],
        "explanation": "Το HADES σχεδιάστηκε αρχικά ως πρωτόκολλο επανεκκίνησης σε περίπτωση αποτυχίας του terraforming, αλλά ένα μυστηριώδες σήμα το καθιστά αυτόνομη καταστροφική τεχνητή νοημοσύνη.",
        "funFacts": [
            "Το HADES εκμεταλλεύεται τη λατρεία της φυλής Shadow Carja (The Eclipse) για να ξυπνήσει τα αρχαία ρομπότ εξόντωσης Corruptors και Deathbringers.",
            "Ο Sylens (με τη φωνή του αείμνηστου Lance Reddick) βοήθησε αρχικά το HADES για να αποκτήσει χαμένη τεχνολογική γνώση."
        ],
        "source": "https://en.wikipedia.org/wiki/Horizon_Zero_Dawn",
        "tags": ["gaming", "horizon_zero_dawn", "guerrilla_games", "hades", "lore"]
    },
    {
        "id": "gaming_med_407",
        "text": "Ποιο είναι το όνομα του πολυτελούς μαύρου αυτοκινήτου με το οποίο ταξιδεύει ο πρίγκιπας Noctis και η παρέα του στο 'Final Fantasy XV' (2016);",
        "correct": "Regalia",
        "distractors": ["Highwind", "Ragnarok", "Invincible"],
        "explanation": "Το Regalia ανήκε στον βασιλιά Regis και αποτελεί το σύμβολο του δεσμού πατέρα-γιου και της φιλίας των τεσσάρων νεαρών ανδρών στο οδικό τους ταξίδι.",
        "funFacts": [
            "Αργότερα στο παιχνίδι, οι παίκτες μπορούν να αναβαθμίσουν το Regalia στο μοντέλο Regalia Type-F που μπορεί κυριολεκτικά να πετάξει σαν αεροπλάνο.",
            "Η μηχανικός που συντηρεί και τροποποιεί το αυτοκίνητο στο συνεργείο Hammerhead ονομάζεται Cindy Aurum."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_XV",
        "tags": ["gaming", "final_fantasy", "square_enix", "noctis", "regalia"]
    },
    {
        "id": "gaming_med_408",
        "text": "Ποιο όπλο ακριβείας με ακτίνα στο 'Quake III Arena' (1999) έγινε το απόλυτο εργαλείο επιδεξιότητας των επαγγελματιών παικτών στα esports;",
        "correct": "Railgun",
        "distractors": ["Rocket Launcher", "Lightning Gun", "Plasma Gun"],
        "explanation": "Το Railgun εκτοξεύει ένα υπερηχητικό βλήμα που αφήνει μια ευθεία φωτεινή γραμμή καπνού και προκαλεί τεράστια στιγμιαία ζημιά χωρίς χρόνο πτήσης (hitscan).",
        "funFacts": [
            "Η ιαχή 'Impressive!' ακούγεται όταν ένας παίκτης πετυχαίνει δύο διαδοχικές εύστοχες βολές με το Railgun σε σύντομο χρονικό διάστημα.",
            "Το Quake III Arena εγκατέλειψε εντελώς την παραδοσιακή εκστρατεία μονού παίκτη, εστιάζοντας αποκλειστικά σε γρήγορες αρένες multiplayer."
        ],
        "source": "https://en.wikipedia.org/wiki/Quake_III_Arena",
        "tags": ["gaming", "quake", "id_software", "railgun", "esports"]
    },
    {
        "id": "gaming_med_409",
        "text": "Στο 'Deus Ex: Human Revolution' (2011), ποιος είναι ο επικεφαλής ασφαλείας της Sarif Industries που σώζεται από βέβαιο θάνατο μέσω εκτεταμένων κυβερνο-προσθετικών;",
        "correct": "Adam Jensen",
        "distractors": ["David Sarif", "JC Denton", "Jaron Namir"],
        "explanation": "Ο Adam Jensen επιβιώνει από επίθεση τρομοκρατών στα εργαστήρια της Sarif Industries στο Ντιτρόιτ, αποκτώντας μηχανικά άκρα, νανολεπίδες στα χέρια και το σύστημα Icarus Landing.",
        "funFacts": [
            "Η φράση του Adam Jensen 'I never asked for this' (Ποτέ δεν το ζήτησα αυτό) έγινε ένα από τα πιο διάσημα gaming memes.",
            "Το παιχνίδι χαρακτηρίζεται από μια εντυπωσιακή χρωματική παλέτα μαύρου και χρυσού, εμπνευσμένη από την ευρωπαϊκή Αναγέννηση."
        ],
        "source": "https://en.wikipedia.org/wiki/Deus_Ex:_Human_Revolution",
        "tags": ["gaming", "deus_ex", "eidos_montreal", "square_enix", "adam_jensen"]
    },
    {
        "id": "gaming_med_410",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο 'Divinity: Original Sin II' (2017) της Larian Studios, ενός σκελετωμένου αθάνατου μελετητή που φοράει μάσκα μεταμόρφωσης;",
        "correct": "Fane",
        "distractors": ["Ifan Ben-Mezd", "Lohse", "The Red Prince"],
        "explanation": "Ο Fane είναι ο μοναδικός επιζών του αρχαίου πολιτισμού των Eternals και χρησιμοποιεί τη μάσκα Mask of the Shapeshifter για να παίρνει τη μορφή άλλων φυλών ώστε να μην τρομοκρατεί τους ανθρώπους.",
        "funFacts": [
            "Ως απέθαντος σκελετός, ο Fane θεραπεύεται από δηλητήριο και δέχεται ζημιά από κανονικά ξόρκια και φίλτρα θεραπείας.",
            "Ο Fane γράφτηκε από τον Chris Avellone σε στενή συνεργασία με την ομάδα σεναρίου της Larian Studios."
        ],
        "source": "https://en.wikipedia.org/wiki/Divinity:_Original_Sin_II",
        "tags": ["gaming", "divinity", "larian_studios", "fane", "rpg"]
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
    print(f"Loaded {len(questions)} questions for gaming_medium batch 4.")
    validate_and_append("gaming", "medium", 3, questions)

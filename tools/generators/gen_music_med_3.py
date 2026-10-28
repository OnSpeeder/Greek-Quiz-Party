# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# 50 music medium questions: music_med_111 to music_med_160
QUESTIONS = [
    {
        "id": "music_med_111",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα alternative rock κυκλοφόρησε το άλμπουμ 'Parachutes' το 2000 με το παγκόσμιο hit 'Yellow';",
        "answers": ["Coldplay", "Keane", "Travis", "Snow Patrol"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Coldplay με επικεφαλής τον Κρις Μάρτιν ξεκίνησαν τη διεθνή τους πορεία με το 'Parachutes', κερδίζοντας το βραβείο Grammy Καλύτερου Alternative Μουσικού Άλμπουμ το 2002.",
        "funFacts": [
            "Το διάσημο βίντεο κλιπ του 'Yellow' γυρίστηκε στην παραλία Studland του Dorset σε ένα μόνο συνεχές πλάνο (one-take) με τον Κρις Μάρτιν να περπατά στη βροχή.",
            "Οι Coldplay είναι ένα από τα πιο επιτυχημένα συναυλιακά συγκροτήματα στον κόσμο, με την περιοδεία τους 'Music of the Spheres' να ξεπερνά το 1 δισεκατομμύριο δολάρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Coldplay",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "coldplay"]
    },
    {
        "id": "music_med_112",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Ιταλού τενόρου που γεννήθηκε με συγγενές γλαύκωμα, τυφλώθηκε στα 12 του και τραγούδησε το 'Con te partirò';",
        "answers": ["Λουτσιάνο Παβαρότι", "Αντρέα Μποτσέλι", "Πλάθιντο Ντομίνγκο", "Βιτόριο Γκριγκόλο"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Αντρέα Μποτσέλι (Andrea Bocelli) είναι ο πιο επιτυχημένος καλλιτέχνης κλασικής crossover μουσικής όλων των εποχών, με πωλήσεις άνω των 90 εκατομμυρίων δίσκων.",
        "funFacts": [
            "Το ντουέτο του με τη Σάρα Μπράιτμαν 'Time to Say Goodbye' (αγγλική εκδοχή του Con te partirò) πούλησε πάνω από 12 εκατομμύρια αντίτυπα παγκοσμίως.",
            "Ο Μποτσέλι έχει σπουδάσει νομικά στο Πανεπιστήμιο της Πίζας και εργάστηκε για έναν χρόνο ως δικηγόρος πριν αφοσιωθεί στη μουσική."
        ],
        "source": "https://en.wikipedia.org/wiki/Andrea_Bocelli",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "crossover", "bocelli"]
    },
    {
        "id": "music_med_113",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο θρυλικό progressive rock συγκρότημα από τον Καναδά αποτελούνταν από τους Τζέντι Λι, Άλεξ Λάιφσον και Νιλ Πιρτ;",
        "answers": ["Triumph", "The Guess Who", "Rush", "April Wine"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Rush ιδρύθηκαν στο Τορόντο το 1968 και αναγνωρίζονται για την εξαιρετική μουσική τους δεξιοτεχνία, τις περίπλοκες συνθέσεις και τα φιλοσοφικά θέματα των στίχων τους.",
        "funFacts": [
            "Ο ντράμερ Νιλ Πιρτ (Neil Peart) θεωρείται ευρέως ένας από τους σπουδαιότερους ντράμερ στην ιστορία της ροκ, χρησιμοποιώντας γιγάντια περιστρεφόμενα drum kits 360 μοιρών.",
            "Το άλμπουμ τους 'Moving Pictures' (1981) περιλαμβάνει τον κλασικό ύμνο 'Tom Sawyer'."
        ],
        "source": "https://en.wikipedia.org/wiki/Rush_(band)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "progressive_rock", "rush"]
    },
    {
        "id": "music_med_114",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Έλληνα συνθέτη ηλεκτρονικής μουσικής που κέρδισε το Όσκαρ Πρωτότυπης Μουσικής για το 'Chariots of Fire' (1981);",
        "answers": ["Ιάννης Ξενάκης", "Μάνος Χατζιδάκις", "Μίκης Θεοδωράκης", "Βαγγέλης Παπαθανασίου (Vangelis)"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Βαγγέλης Παπαθανασίου (Vangelis) πρωτοπόρησε στη χρήση συνθεσάιζερ στον κινηματογράφο, συνθέτοντας επίσης τη θρυλική μουσική για το 'Blade Runner' και το '1492: Conquest of Paradise'.",
        "funFacts": [
            "Ο Vangelis ξεκίνησε τη διεθνή του καριέρα στα τέλη των 60s με το ελληνικό progressive rock συγκρότημα Aphrodite's Child μαζί με τον Ντέμη Ρούσσο.",
            "Η NASA χρησιμοποίησε το έργο του 'Mythodea' ως την επίσημη μουσική της αποστολής 2001 Mars Odyssey."
        ],
        "source": "https://en.wikipedia.org/wiki/Vangelis",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soundtracks", "vangelis"]
    },
    {
        "id": "music_med_115",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είδος jazz μουσικής που αναπτύχθηκε τη δεκαετία του 1940 χαρακτηρίζεται από γρήγορα τέμπη, περίπλοκες αρμονίες και βιρτουόζικο αυτοσχεδιασμό;",
        "answers": ["Bebop", "Dixieland", "Smooth jazz", "Cool jazz"],
        "correctAnswerIndex": 0,
        "explanation": "Το Bebop (ή bop) δημιουργήθηκε από πρωτοπόρους όπως ο Τσάρλι Πάρκερ (σαξόφωνο), ο Ντίζι Γκιλέσπι (τρομπέτα) και ο Θελόνιους Μονκ (πιάνο), μετατρέποντας την τζαζ από χορευτική μουσική σε τέχνη για ακρόαση.",
        "funFacts": [
            "Το όνομα 'bebop' ήταν ονοματοποιία που μιμούνταν τους ρυθμικούς συγκοπτόμενους ήχους των αυτοσχεδιασμών.",
            "Οι μουσικοί του bebop φορούσαν συχνά μπερέδες, γυαλιά με κοκάλινο σκελετό και μουσάκια, διαμορφώνοντας τη μόδα της beat γενιάς."
        ],
        "source": "https://en.wikipedia.org/wiki/Bebop",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "bebop"]
    },
    {
        "id": "music_med_116",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό glam rock συγκρότημα με τραγουδιστή τον Marc Bolan κυκλοφόρησε τα hits 'Get It On' και 'Children of the Revolution';",
        "answers": ["Roxy Music", "T. Rex", "Mott the Hoople", "Slade"],
        "correctAnswerIndex": 1,
        "explanation": "Οι T. Rex αποτέλεσαν την αιχμή του δόρατος του βρετανικού glam rock κινήματος στις αρχές της δεκαετίας του 1970, προκαλώντας την επονομαζόμενη 'T. Rextasy'.",
        "funFacts": [
            "Ο Μαρκ Μπόλαν θεωρείται ένας από τους πρώτους καλλιτέχνες που έβαλαν γκλίτερ στα μάγουλά τους στην τηλεόραση (στο Top of the Pops το 1971), ξεκινώντας τη μόδα του glam.",
            "Ο Μπόλαν σκοτώθηκε τραγικά σε αυτοκινητιστικό δυστύχημα το 1977 σε ηλικία μόλις 29 ετών."
        ],
        "source": "https://en.wikipedia.org/wiki/T._Rex_(band)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "glam_rock"]
    },
    {
        "id": "music_med_117",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των The Clash του 1979 που συνδύασε πανκ, ρέγκε, σκα και ροκαμπίλι;",
        "answers": ["Give 'Em Enough Rope", "Sandinista!", "London Calling", "Combat Rock"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'London Calling' των The Clash κατατάσσεται σταθερά ανάμεσα στα σπουδαιότερα ροκ άλμπουμ όλων των εποχών από κριτικούς και μουσικά περιοδικά.",
        "funFacts": [
            "Η εμβληματική φωτογραφία του εξωφύλλου με τον μπασίστα Πολ Σίμονον να συντρίβει το μπάσο του στη σκηνή τραβήχτηκε από την Πένι Σμιθ στο Palladium της Νέας Υόρκης.",
            "Η γραμματοσειρά και τα χρώματα του τίτλου στο εξώφυλλο σχεδιάστηκαν ως άμεσος φόρος τιμής στο ντεμπούτο άλμπουμ του Έλβις Πρίσλεϊ του 1956."
        ],
        "source": "https://en.wikipedia.org/wiki/London_Calling",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "punk", "the_clash"]
    },
    {
        "id": "music_med_118",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο όργανο της οικογένειας των χάλκινων πνευστών δεν χρησιμοποιεί βαλβίδες ή έμβολα, αλλά έναν συρόμενο μηχανισμό (slide) για να αλλάζει νότες;",
        "answers": ["Η τρομπέτα", "Το γαλλικό κόρνο", "Η τούμπα", "Το τρομπόνι"],
        "correctAnswerIndex": 3,
        "explanation": "Το τρομπόνι (trombone) χρησιμοποιεί έναν συρόμενο τηλεσκοπικό σωλήνα με 7 βασικές θέσεις για να μεταβάλλει το μήκος της στήλης αέρα και το τονικό ύψος.",
        "funFacts": [
            "Το τρομπόνι ονομαζόταν παλαιότερα στα αγγλικά 'sackbut' κατά την Αναγέννηση και το Μπαρόκ.",
            "Χάρη στον συρόμενο σωλήνα του, το τρομπόνι μπορεί να εκτελέσει απόλυτα ομαλό glissando (συνεχές γλίστρημα μεταξύ νοτών)."
        ],
        "source": "https://en.wikipedia.org/wiki/Trombone",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "instruments", "brass"]
    },
    {
        "id": "music_med_119",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος συνθέτης και αρχιμουσικός έγραψε τη μουσική για το μιούζικαλ 'West Side Story' το 1957;",
        "answers": ["Λέοναρντ Μπερνστάιν", "Τζορτζ Γκέρσουιν", "Άαρον Κόπλαντ", "Κόουλ Πόρτερ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Λέοναρντ Μπερνστάιν (Leonard Bernstein) συνέθεσε το πρωτοποριακό soundtrack του West Side Story, συνδυάζοντας συμφωνική μουσική, τζαζ και λάτιν ρυθμούς με στίχους του Στίβεν Σόντχαϊμ.",
        "funFacts": [
            "Ο Μπερνστάιν υπήρξε ο πρώτος Αμερικανός μαέστρος που ανέλαβε τη διεύθυνση της διάσημης Φιλαρμονικής της Νέας Υόρκης.",
            "Το West Side Story αποτελεί σύγχρονη μεταφορά της τραγωδίας 'Ρωμαίος και Ιουλιέτα' του Σαίξπηρ στο Μανχάταν των 50s."
        ],
        "source": "https://en.wikipedia.org/wiki/West_Side_Story",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "musicals", "bernstein"]
    },
    {
        "id": "music_med_120",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα grunge από το Σιάτλ με τραγουδιστή τον Κρις Κορνέλ κυκλοφόρησε το άλμπουμ 'Superunknown' (1994) με το hit 'Black Hole Sun';",
        "answers": ["Nirvana", "Soundgarden", "Alice in Chains", "Mudhoney"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Soundgarden ήταν από τους πρώτους που υπέγραψαν στην ανεξάρτητη εταιρεία Sub Pop και το 'Superunknown' έφτασε στο νούμερο 1 του Billboard 200.",
        "funFacts": [
            "Ο Κρις Κορνέλ είχε εκπληκτικό φωνητικό εύρος σχεδόν τεσσάρων οκτάβων και ήταν γνωστός για τις δυναμικές του κραυγές.",
            "Το surreal βίντεο κλιπ του 'Black Hole Sun' με τα παραμορφωμένα χαμόγελα κέρδισε το βραβείο MTV Video Music Award για το Καλύτερο Metal/Hard Rock Βίντεο το 1994."
        ],
        "source": "https://en.wikipedia.org/wiki/Superunknown",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "grunge", "soundgarden"]
    },
    {
        "id": "music_med_121",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη τραγουδίστρια της jazz και των blues ηχογράφησε το 'Feeling Good' και το τραγούδι πολιτικών δικαιωμάτων 'Mississippi Goddam';",
        "answers": ["Έλλα Φιτζέραλντ", "Μπίλι Χόλιντεϊ", "Νίνα Σιμόν", "Έτα Τζέιμς"],
        "correctAnswerIndex": 2,
        "explanation": "Η Νίνα Σιμόν (Nina Simone, πραγματικό όνομα Γιούνις Κάθλιν Γουέιμον) ήταν κλασικά εκπαιδευμένη πιανίστρια και μία από τις πιο επιδραστικές φωνές του κινήματος πολιτικών δικαιωμάτων.",
        "funFacts": [
            "Απορρίφθηκε από το Curtis Institute of Music στη Φιλαδέλφεια λόγω φυλετικών διακρίσεων, γεγονός που την οδήγησε να παίζει σε νυχτερινά κλαμπ για να ζήσει.",
            "Το 2003, λίγες μέρες πριν από τον θάνατό της, το Curtis Institute της απένειμε τιμητικό δίπλωμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Nina_Simone",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "civil_rights", "nina_simone"]
    },
    {
        "id": "music_med_122",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των Metallica του 1991 (γνωστού ως 'The Black Album') που περιλαμβάνει το 'Enter Sandman';",
        "answers": ["Master of Puppets", "...And Justice for All", "Ride the Lightning", "Metallica"],
        "correctAnswerIndex": 3,
        "explanation": "Το πέμπτο άλμπουμ των Metallica, με επίσημο τίτλο απλώς 'Metallica' και ολόμαυρο εξώφυλλο με ένα αμυδρό φίδι, έχει πουλήσει πάνω από 30 εκατομμύρια αντίτυπα παγκοσμίως.",
        "funFacts": [
            "Το άλμπουμ σηματοδότησε τη στροφή του συγκροτήματος σε πιο αργούς, βαριούς ρυθμούς υπό την καθοδήγηση του παραγωγού Μπομπ Ροκ.",
            "Είναι το άλμπουμ με τις μεγαλύτερες πωλήσεις στην εποχή του συστήματος SoundScan στις ΗΠΑ από το 1991."
        ],
        "source": "https://en.wikipedia.org/wiki/Metallica_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "metallica"]
    },
    {
        "id": "music_med_123",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο κλασικό μουσικό έργο του Μορίς Ραβέλ που παρουσιάστηκε το 1928 βασίζεται σε ένα επίμονο ostinato ρυθμό ταμπούρου και ένα τεράστιο crescendo 15 λεπτών;",
        "answers": ["Μπολερό (Boléro)", "Παβάνα", "Δάφνις και Χλόη", "Η Βαλς"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'Boléro' του Ραβέλ επαναλαμβάνει συνεχώς το ίδιο μελωδικό θέμα με διαφορετικά όργανα της ορχήστρας, χτίζοντας μια καθηλωτική κλιμάκωση έντασης.",
        "funFacts": [
            "Ο ίδιος ο Ραβέλ θεωρούσε το έργο ένα απλό ορχηστρικό πείραμα χωρίς ουσιαστικό μουσικό βάθος και εξεπλάγη από την τεράστια παγκόσμια δημοτικότητά του.",
            "Ο ντράμερ του ταμπούρου παίζει το ίδιο ρυθμικό μοτίβο δύο μέτρων ακριβώς 169 φορές χωρίς καμία διακοπή."
        ],
        "source": "https://en.wikipedia.org/wiki/Bol%C3%A9ro",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "ravel"]
    },
    {
        "id": "music_med_124",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός τραγουδιστής και πιανίστας της soul και R&B ήταν γνωστός ως 'The Genius' και τραγούδησε τα 'Georgia on My Mind' και 'Hit the Road Jack';",
        "answers": ["Στίβι Γουόντερ", "Ρέι Τσαρλς", "Μάρβιν Γκέι", "Ότις Ρέντινγκ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Ρέι Τσαρλς (Ray Charles) τυφλώθηκε σε ηλικία 7 ετών και πρωτοπόρησε στη συγχώνευση του gospel, των blues και της jazz, δημιουργώντας το είδος της soul μουσικής τη δεκαετία του '50.",
        "funFacts": [
            "Το 'Georgia on My Mind' ανακηρύχθηκε επίσημα ως ο κρατικός ύμνος της πολιτείας της Τζόρτζια το 1979.",
            "Κέρδισε συνολικά 17 βραβεία Grammy κατά τη διάρκεια της καριέρας του, καθώς και Grammy Lifetime Achievement Award."
        ],
        "source": "https://en.wikipedia.org/wiki/Ray_Charles",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soul", "ray_charles"]
    },
    {
        "id": "music_med_125",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό synth-pop και new wave συγκρότημα από το Μπάσιλντον κυκλοφόρησε το θρυλικό άλμπουμ 'Violator' (1990) με τα hits 'Personal Jesus' και 'Enjoy the Silence';",
        "answers": ["Pet Shop Boys", "New Order", "Depeche Mode", "Erasure"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Depeche Mode (με κύριο συνθέτη τον Μάρτιν Γκορ και τραγουδιστή τον Ντέιβ Γκάχαν) καθόρισαν τον σκοτεινό ηλεκτρονικό ήχο των 80s και 90s.",
        "funFacts": [
            "Το 'Personal Jesus' ήταν εμπνευσμένο από το βιβλίο της Πρισίλα Πρίσλεϊ 'Elvis and Me', όπου περιέγραφε πώς ο Έλβις ήταν ένας προσωπικός θεός για εκείνη.",
            "Το τραγούδι διασκευάστηκε αργότερα με τεράστια επιτυχία τόσο από τον Τζόνι Κας όσο και από τον Μέριλιν Μάνσον."
        ],
        "source": "https://en.wikipedia.org/wiki/Depeche_Mode",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "electronic", "depeche_mode"]
    },
    {
        "id": "music_med_126",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου ελληνικού μουσικού ρεύματος που άνθισε στις αρχές του 20ού αιώνα στα λιμάνια του Πειραιά και της Σμύρνης και συνδέθηκε με τους 'μάγκες';",
        "answers": ["Δημοτικό τραγούδι", "Καντάδα", "Ελαφρό τραγούδι", "Ρεμπέτικο"],
        "correctAnswerIndex": 3,
        "explanation": "Το ρεμπέτικο είναι το αστικό λαϊκό τραγούδι των κατώτερων κοινωνικών στρωμάτων, αναγνωρισμένο από την UNESCO ως Άυλη Πολιτιστική Κληρονομιά της Ανθρωπότητας.",
        "funFacts": [
            "Ο Μάρκος Βαμβακάρης θεωρείται ο 'πατριάρχης' του ρεμπέτικου τραγουδιού με αριστουργήματα όπως η 'Φραγκοσυριανή'.",
            "Την περίοδο της δικτατορίας του Μεταξά το 1936, το ρεμπέτικο υπέστη αυστηρή λογοκρισία και απαγορεύτηκαν οι αναφορές σε ναρκωτικά και τεκέδες."
        ],
        "source": "https://en.wikipedia.org/wiki/Rebetiko",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "rebetiko"]
    },
    {
        "id": "music_med_127",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αυστριακός συνθέτης έγραψε τον πασίγνωστο κύκλο τραγουδιών 'Χειμωνιάτικο Ταξίδι' (Winterreise) και την 'Ημιτελή Συμφωνία';",
        "answers": ["Φραντς Σούμπερτ", "Γιόζεφ Χάιντν", "Άντον Μπρούκνερ", "Γκούσταβ Μάλερ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Φραντς Σούμπερτ (Franz Schubert) συνέθεσε πάνω από 600 ρομαντικά τραγούδια (Lieder) στη σύντομη ζωή του, πεθαίνοντας σε ηλικία μόλις 31 ετών.",
        "funFacts": [
            "Η 8η Συμφωνία του σε Σι ελάσσονα ονομάστηκε 'Ημιτελής' επειδή αποτελείται από δύο μόνο ολοκληρωμένα μέρη αντί για τα συνηθισμένα τέσσερα.",
            "Οι μουσικές βραδιές όπου φίλοι συγκεντρώνονταν σε σπίτια για να ακούσουν τα έργα του ονομάζονταν 'Schubertiades'."
        ],
        "source": "https://en.wikipedia.org/wiki/Franz_Schubert",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "schubert"]
    },
    {
        "id": "music_med_128",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο thrash metal συγκρότημα από το Λος Άντζελες με αρχηγό τον Dave Mustaine κυκλοφόρησε το άλμπουμ 'Rust in Peace' το 1990;",
        "answers": ["Slayer", "Megadeth", "Anthrax", "Testament"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Ντέιβ Μαστέιν ίδρυσε τους Megadeth το 1983 μετά την απόλυσή του από τους Metallica, δημιουργώντας ένα από τα 'Big Four' συγκροτήματα του thrash metal.",
        "funFacts": [
            "Το 'Rust in Peace' θεωρείται από πολλούς μουσικούς ως το κορυφαίο τεχνικό thrash metal άλμπουμ όλων των εποχών, με τα κιθαριστικά σόλο του Μάρτι Φρίντμαν.",
            "Η μασκότ του συγκροτήματος ονομάζεται Vic Rattlehead και συμβολίζει τη λογοκρισία (κλειστό στόμα, καλυμμένα μάτια και αυτιά)."
        ],
        "source": "https://en.wikipedia.org/wiki/Megadeth",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "megadeth"]
    },
    {
        "id": "music_med_129",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο blues τραγούδι του Robert Johnson του 1936 συνδέθηκε με τον μύθο ότι πούλησε την ψυχή του στον διάβολο σε ένα σταυροδρόμι;",
        "answers": ["Sweet Home Chicago", "Hellhound on My Trail", "Cross Road Blues", "Love in Vain"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Cross Road Blues' του Ρόμπερτ Τζόνσον ενέπνευσε τον θρύλο του σταυροδρομιού στο Μισισιπή και διασκευάστηκε ιστορικά από τους Cream και τον Έρικ Κλάπτον το 1968.",
        "funFacts": [
            "Ο Τζόνσον ηχογράφησε μόλις 29 τραγούδια στη ζωή του σε δύο συνεδρίες το 1936 και 1937, αλλά επηρέασε βαθιά σχεδόν όλους τους κορυφαίους κιθαρίστες της ροκ.",
            "Πέθανε μυστηριωδώς σε ηλικία 27 ετών (θεωρούμενος το πρώτο μέλος του τραγικού '27 Club')."
        ],
        "source": "https://en.wikipedia.org/wiki/Cross_Road_Blues",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "blues", "robert_johnson"]
    },
    {
        "id": "music_med_130",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Ιταλού κατασκευαστή εγχόρδων από την Κρεμόνα του οποίου τα βιολιά πωλούνται σήμερα για εκατομμύρια ευρώ σε δημοπρασίες;",
        "answers": ["Νικολό Αμάτι", "Αντρέα Γκουαρνέρι", "Γκασπάρο ντα Σαλό", "Αντόνιο Στραντιβάρι"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Αντόνιο Στραντιβάρι (Antonio Stradivari, 1644-1737) κατασκεύασε μερικά από τα πιο περιζήτητα και πολύτιμα βιολιά, βιόλες και τσέλα στην ανθρώπινη ιστορία (γνωστά ως Στραντιβάριους).",
        "funFacts": [
            "Σώζονται σήμερα περίπου 650 αυθεντικά όργανα κατασκευασμένα από τον Στραντιβάρι.",
            "Το βιολί 'Lady Blunt' του 1721 πουλήθηκε σε δημοπρασία το 2011 για το ποσό ρεκόρ των 15,9 εκατομμυρίων δολαρίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Antonio_Stradivari",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "instruments", "stradivarius"]
    },
    {
        "id": "music_med_131",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα indie rock κυκλοφόρησε το άλμπουμ 'Whatever People Say I Am, That's What I'm Not' (2006) με επικεφαλής τον Alex Turner;",
        "answers": ["Arctic Monkeys", "The Kooks", "Franz Ferdinand", "Kasabian"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Arctic Monkeys από το Σέφιλντ έγιναν διάσημοι μέσω του MySpace και το ντεμπούτο τους έγινε το ταχύτερα πωλούμενο ντεμπούτο άλμπουμ συγκροτήματος στην ιστορία των βρετανικών charts.",
        "funFacts": [
            "Ο τίτλος του άλμπουμ προέρχεται από μια ατάκα του Άλαν Σίλιτοου στο βιβλίο 'Σάββατο Βράδυ, Κυριακή Πρωί'.",
            "Το 2013 κυκλοφόρησαν το άλμπουμ 'AM' που περιλαμβάνει την παγκόσμια επιτυχία 'Do I Wanna Know?'."
        ],
        "source": "https://en.wikipedia.org/wiki/Arctic_Monkeys",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "indie", "arctic_monkeys"]
    },
    {
        "id": "music_med_132",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός τραγουδιστής της soul και R&B κυκλοφόρησε το 1971 το ιστορικό κοινωνικό άλμπουμ 'What's Going On';",
        "answers": ["Στίβι Γουόντερ", "Μάρβιν Γκέι", "Αλ Γκριν", "Κέρτις Μέιφιλντ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Μάρβιν Γκέι (Marvin Gaye) έγραψε το 'What's Going On' για τη Motown, αγγίζοντας θέματα όπως ο πόλεμος του Βιετνάμ, η φτώχεια και η περιβαλλοντική καταστροφή.",
        "funFacts": [
            "Ο ιδρυτής της Motown Μπέρι Γκόρντι αρνούνταν αρχικά να κυκλοφορήσει το single, χαρακτηρίζοντάς το 'το χειρότερο τραγούδι που άκουσε ποτέ'.",
            "Το περιοδικό Rolling Stone το 2020 κατέταξε το 'What's Going On' στο νούμερο 1 της λίστας με τα 500 σπουδαιότερα άλμπουμ όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/What%27s_Going_On_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soul", "marvin_gaye"]
    },
    {
        "id": "music_med_133",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο παραδοσιακό σκωτσέζικο τραγούδι σε ποίηση του Ρόμπερτ Μπερνς τραγουδιέται παραδοσιακά σε όλο τον αγγλόφωνο κόσμο τα μεσάνυχτα της Πρωτοχρονιάς;",
        "answers": ["Loch Lomond", "Danny Boy", "Auld Lang Syne", "Scots Wha Hae"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Auld Lang Syne' (που μεταφράζεται ελεύθερα ως 'για τις παλιές καλές μέρες') είναι το παγκόσμιο παραδοσιακό τραγούδι αποχαιρετισμού του παλιού έτους.",
        "funFacts": [
            "Ο Ρόμπερτ Μπερνς κατέγραψε τους στίχους το 1788 από έναν ηλικιωμένο άνδρα στην ύπαιθρο της Σκωτίας.",
            "Η παράδοση του τραγουδιού την Παραμονή Πρωτοχρονιάς διαδόθηκε διεθνώς από τον Καναδό μαέστρο Γκι Λομπάρντο και την ορχήστρα του στη Νέα Υόρκη από το 1929."
        ],
        "source": "https://en.wikipedia.org/wiki/Auld_Lang_Syne",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "tradition", "folk"]
    },
    {
        "id": "music_med_134",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό hard rock συγκρότημα κυκλοφόρησε το 1970 το άλμπουμ 'Paranoid' με το ομώνυμο τραγούδι και το 'Iron Man';",
        "answers": ["Led Zeppelin", "Deep Purple", "Uriah Heep", "Black Sabbath"],
        "correctAnswerIndex": 3,
        "explanation": "Οι Black Sabbath κυκλοφόρησαν το 'Paranoid' το φθινόπωρο του 1970, κατακτώντας την κορυφή των βρετανικών charts και θεμελιώνοντας τη metal σκηνή.",
        "funFacts": [
            "Ο αρχικός τίτλος του άλμπουμ ήταν 'War Pigs', αλλά η δισκογραφική εταιρεία τον άλλαξε φοβούμενη αντιδράσεις λόγω του πολέμου του Βιετνάμ.",
            "Το εξώφυλλο απεικονίζει έναν άνδρα με σπαθί και κράνος που βγαίνει από πίσω από ένα δέντρο, παραμένοντας ένα από τα πιο αλλόκοτα εξώφυλλα του είδους."
        ],
        "source": "https://en.wikipedia.org/wiki/Paranoid_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "black_sabbath"]
    },
    {
        "id": "music_med_135",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της όπερας έγραψε τις αριστουργηματικές συνθέσεις 'Μποέμ' (La Bohème), 'Τόσκα' και 'Μαντάμα Μπατερφλάι';",
        "answers": ["Τζάκομο Πουτσίνι", "Τζουζέπε Βέρντι", "Γκαετάνο Ντονιτσέτι", "Βιντσέντζο Μπελίνι"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Τζάκομο Πουτσίνι (Giacomo Puccini) υπήρξε ο κορυφαίος εκπρόσωπος του ιταλικού βερισμού (verismo) στην όπερα, χαρίζοντας συγκινησιακά φορτισμένες μελωδίες.",
        "funFacts": [
            "Η πρεμιέρα της 'Μαντάμα Μπατερφλάι' στη Σκάλα του Μιλάνου το 1904 συνοδεύτηκε από σφυρίγματα και αποδοκιμασίες πριν αναθεωρηθεί και γίνει παγκόσμιος θρίαμβος.",
            "Η τελευταία του όπερα, η 'Τουραντότ', έμεινε ημιτελής λόγω του θανάτου του το 1924 και ολοκληρώθηκε από τον Φράνκο Αλφάνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Giacomo_Puccini",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "opera", "puccini"]
    },
    {
        "id": "music_med_136",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου hip hop συγκροτήματος από το Staten Island της Νέας Υόρκης που περιλαμβάνει τους RZA, GZA, Method Man και Raekwon;",
        "answers": ["A Tribe Called Quest", "Wu-Tang Clan", "Public Enemy", "N.W.A"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Wu-Tang Clan έφεραν επανάσταση στο hip hop το 1993 με το ντεμπούτο τους 'Enter the Wu-Tang (36 Chambers)', εμπνευσμένοι από ανατολικές πολεμικές τέχνες και ταινίες kung-fu.",
        "funFacts": [
            "Το συγκρότημα κυκλοφόρησε το 2015 ένα και μοναδικό αντίτυπο του άλμπουμ 'Once Upon a Time in Shaolin', το οποίο πουλήθηκε σε δημοπρασία για 2 εκατομμύρια δολάρια.",
            "Όλα τα μέλη του συγκροτήματος διατήρησαν συμβόλαια που τους επέτρεπαν να κυκλοφορούν σόλο άλμπουμ σε διαφορετικές δισκογραφικές εταιρείες."
        ],
        "source": "https://en.wikipedia.org/wiki/Wu-Tang_Clan",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "wu_tang"]
    },
    {
        "id": "music_med_137",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό folk rock συγκρότημα με επικεφαλής τον Marcus Mumford κυκλοφόρησε τα smash hits 'Little Lion Man' και 'The Cave';",
        "answers": ["The Lumineers", "Fleet Foxes", "Mumford & Sons", "Of Monsters and Men"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Mumford & Sons αναβίωσαν τη folk rock σκηνή στα τέλη των 2000s με τη χρήση μπάντζο, ακουστικής κιθάρας και δυναμικών ρυθμικών crescendo.",
        "funFacts": [
            "Το δεύτερο άλμπουμ τους 'Babel' (2012) κέρδισε το βραβείο Grammy για το Άλμπουμ της Χρονιάς.",
            "Τα μέλη του συγκροτήματος δεν έχουν καμία συγγένεια μεταξύ τους, παρά τη λέξη 'Sons' στο όνομά τους."
        ],
        "source": "https://en.wikipedia.org/wiki/Mumford_%26_Sons",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "folk", "mumford_and_sons"]
    },
    {
        "id": "music_med_138",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο έγχορδο μουσικό όργανο της ινδικής κλασικής μουσικής έκανε παγκοσμίως διάσημο ο Ραβί Σανκάρ, επηρεάζοντας και τον Τζορτζ Χάρισον των Beatles;",
        "answers": ["Το σάροντ", "Το ταμπούρα", "Το σαντούρι", "Το σιτάρ"],
        "correctAnswerIndex": 3,
        "explanation": "Το σιτάρ (sitar) είναι ένα παραδοσιακό ινδικό έγχορδο όργανο με κινητά τάστα, συμπαθητικές χορδές και αντηχείο από αποξηραμένη κολοκύθα.",
        "funFacts": [
            "Ο Τζορτζ Χάρισον έμαθε σιτάρ απευθείας από τον Ραβί Σανκάρ και το χρησιμοποίησε για πρώτη φορά στο τραγούδι 'Norwegian Wood (This Bird Has Flown)' το 1965.",
            "Το σιτάρ διαθέτει συνήθως 18 έως 21 χορδές, εκ των οποίων οι περισσότερες δονούνται συμπαθητικά χωρίς να αγγίζονται άμεσα."
        ],
        "source": "https://en.wikipedia.org/wiki/Sitar",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "world_music", "instruments", "sitar"]
    },
    {
        "id": "music_med_139",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Γερμανού συνθέτη του μπαρόκ που συνέθεσε το ορατόριο 'Μεσσίας' (Messiah) με το πασίγνωστο 'Αλληλούια';",
        "answers": ["Γκέοργκ Φρίντριχ Χαίντελ", "Γιόχαν Σεμπάστιαν Μπαχ", "Γκέοργκ Φίλιπ Τέλεμαν", "Χάινριχ Συτς"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Χαίντελ (George Frideric Handel) συνέθεσε τον 'Μεσσία' στο Λονδίνο το 1741 μέσα σε μόλις 24 ημέρες εντατικής έμπνευσης.",
        "funFacts": [
            "Η παράδοση κατά την οποία το κοινό στέκεται όρθιο κατά τη διάρκεια του χορωδιακού 'Hallelujah' ξεκίνησε όταν ο βασιλιάς Γεώργιος Β' της Αγγλίας σηκώθηκε συγκινημένος στην παράσταση.",
            "Παρόλο που γεννήθηκε στη Γερμανία, ο Χαίντελ πέρασε το μεγαλύτερο μέρος της ζωής του στην Αγγλία και τάφηκε στο Αβαείο του Ουέστμινστερ."
        ],
        "source": "https://en.wikipedia.org/wiki/Messiah_(Handel)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "baroque", "handel"]
    },
    {
        "id": "music_med_140",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του εμβληματικού άλμπουμ των U2 του 1987 που περιλαμβάνει τα κομμάτια 'With or Without You' και 'Where the Streets Have No Name';",
        "answers": ["War", "The Joshua Tree", "Achtung Baby", "The Unforgettable Fire"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'The Joshua Tree' των U2 σε παραγωγή Μπράιαν Ίνο και Ντάνιελ Λανουά εκτόξευσε το ιρλανδικό συγκρότημα σε παγκόσμιο φαινόμενο, κερδίζοντας το Grammy Άλμπουμ της Χρονιάς.",
        "funFacts": [
            "Το άλμπουμ πήρε το όνομά του από το χαρακτηριστικό δέντρο της ερήμου Mojave (Yucca brevifolia) στην Καλιφόρνια.",
            "Το δέντρο όπου φωτογραφήθηκε το συγκρότημα για το εξώφυλλο έπεσε από φυσικά αίτια το 2000, αλλά οι φαν εξακολουθούν να επισκέπτονται το σημείο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Joshua_Tree",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "u2"]
    },
    {
        "id": "music_med_141",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη Ελληνίδα υψίφωνος (σοπράνο) αποκλήθηκε 'La Divina' και θεωρείται η σπουδαιότερη ερμηνεύτρια όπερας του 20ού αιώνα;",
        "answers": ["Ρένα Βλαχοπούλου", "Αγνή Μπάλτσα", "Μαρία Κάλλας", "Έλενα Σουλιώτη"],
        "correctAnswerIndex": 2,
        "explanation": "Η Μαρία Κάλλας (Maria Callas, πραγματικό όνομα Σοφία Καικιλία Καλογεροπούλου) αναβίωσε το ιταλικό bel canto με τη δραματική ένταση της φωνής και της υποκριτικής της.",
        "funFacts": [
            "Γεννήθηκε στη Νέα Υόρκη από Έλληνες μετανάστες και σπούδασε στο Εθνικό Ωδείο της Αθήνας υπό την Ελβίρα ντε Ιδάλγο.",
            "Η θυελλώδης προσωπική της σχέση με τον Έλληνα μεγιστάνα Αριστοτέλη Ωνάση απασχόλησε έντονα τον παγκόσμιο Τύπο."
        ],
        "source": "https://en.wikipedia.org/wiki/Maria_Callas",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "opera", "maria_callas"]
    },
    {
        "id": "music_med_142",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο ήταν το θρυλικό live aid φιλανθρωπικό κοντσέρτο που διοργάνωσε ο Μπομπ Γκέλντοφ στις 13 Ιουλίου 1985 ταυτόχρονα στο Λονδίνο και τη Φιλαδέλφεια;",
        "answers": ["Live 8", "Farm Aid", "The Concert for Bangladesh", "Live Aid"],
        "correctAnswerIndex": 3,
        "explanation": "Το Live Aid συγκέντρωσε χρήματα για την καταπολέμηση του λιμού στην Αιθιοπία και μεταδόθηκε ζωντανά σε περίπου 1,9 δισεκατομμύρια τηλεθεατές σε 150 χώρες.",
        "funFacts": [
            "Η 21λεπτη εμφάνιση των Queen στο στάδιο Wembley θεωρείται ευρέως από τους κριτικούς ως η καλύτερη ζωντανή ροκ συναυλία στην ιστορία.",
            "Ο Φιλ Κόλινς έπαιξε στο Λονδίνο, πήρε το υπερηχητικό Concorde για τις ΗΠΑ και έπαιξε την ίδια ημέρα και στη Φιλαδέλφεια."
        ],
        "source": "https://en.wikipedia.org/wiki/Live_Aid",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "history", "concerts", "live_aid"]
    },
    {
        "id": "music_med_143",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού jazz σαξοφωνίστα που κυκλοφόρησε το πνευματικό αριστούργημα 'A Love Supreme' το 1965;",
        "answers": ["Τζον Κολτρέιν", "Τσάρλι Πάρκερ", "Σόνι Ρόλινς", "Ορνέτ Κόουλμαν"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Τζον Κολτρέιν (John Coltrane) ηχογράφησε το τετραμερές 'A Love Supreme' ως ευχαριστήριο ύμνο προς τον Θεό μετά την απεξάρτησή του από τα ναρκωτικά.",
        "funFacts": [
            "Το 'A Love Supreme' ηχογραφήθηκε σε μία μόνο συνεδρία στις 9 Δεκεμβρίου 1964 στο Van Gelder Studio στο Νιου Τζέρσεϊ.",
            "Στο Σαν Φρανσίσκο υπάρχει η Αφρικανική Ορθόδοξη Εκκλησία του Αγίου Τζον Κολτρέιν, η οποία τον τιμά επίσημα ως άγιο."
        ],
        "source": "https://en.wikipedia.org/wiki/A_Love_Supreme",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "john_coltrane"]
    },
    {
        "id": "music_med_144",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό glam/hard rock συγκρότημα από το Σέφιλντ κυκλοφόρησε το κολοσσιαίο άλμπουμ 'Hysteria' (1987) με ντράμερ τον Ρικ Άλεν που έπαιζε με ένα χέρι;",
        "answers": ["Iron Maiden", "Def Leppard", "Whitesnake", "Judas Priest"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Def Leppard πούλησαν πάνω από 20 εκατομμύρια αντίτυπα του 'Hysteria', αφού ο ντράμερ τους Ρικ Άλεν έχασε το αριστερό του χέρι σε αυτοκινητιστικό δυστύχημα και έμαθε να παίζει με ειδικά ηλεκτρονικά πεντάλ ποδιού.",
        "funFacts": [
            "Το άλμπουμ παρήγαγε επτά singles στο Billboard Hot 100, συμπεριλαμβανομένου του νούμερο 1 hit 'Pour Some Sugar on Me'.",
            "Η ηχογράφηση του άλμπουμ διήρκεσε πάνω από τρία χρόνια και ήταν μία από τις πιο ακριβές παραγωγές στην ιστορία της ροκ."
        ],
        "source": "https://en.wikipedia.org/wiki/Hysteria_(Def_Leppard_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "def_leppard"]
    },
    {
        "id": "music_med_145",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο παραδοσιακό μουσικό όργανο των Αβοριγίνων της Αυστραλίας κατασκευάζεται από κούφιο κορμό ευκαλύπτου που έχουν σκάψει οι τερμίτες;",
        "answers": ["Το ντιτζεριντού (didgeridoo)", "Το μπούμερανγκ", "Το ταμπούρ", "Το κουλούταρ"],
        "correctAnswerIndex": 0,
        "explanation": "Το ντιτζεριντού είναι ένα από τα αρχαιότερα πνευστά όργανα στον πλανήτη, που παίζεται με την τεχνική της κυκλικής αναπνοής παράγοντας έναν βαθύ, υπόκωφο βόμβο.",
        "funFacts": [
            "Η τεχνική της κυκλικής αναπνοής επιτρέπει στον μουσικό να διατηρεί έναν συνεχή ήχο για δεκάδες λεπτά εισπνέοντας από τη μύτη ενώ ταυτόχρονα σπρώχνει αέρα με τα μάγουλα.",
            "Οι σύγχρονες ιατρικές μελέτες έχουν δείξει ότι το παίξιμο του ντιτζεριντού μειώνει σημαντικά την υπνική άπνοια ενδυναμώνοντας τους μύες του λαιμού."
        ],
        "source": "https://en.wikipedia.org/wiki/Didgeridoo",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "world_music", "instruments", "australia"]
    },
    {
        "id": "music_med_146",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της ρομαντικής όπερας έγραψε τις αριστουργηματικές όπερες 'Ριγκολέτο', 'Οθέλλος' και 'Ναμπούκο';",
        "answers": ["Τζοακίνο Ροσίνι", "Τζουζέπε Βέρντι", "Τζάκομο Πουτσίνι", "Γκαετάνο Ντονιτσέτι"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Τζουζέπε Βέρντι (Giuseppe Verdi) υπήρξε η δεσπόζουσα μορφή της ιταλικής όπερας του 19ου αιώνα και σύμβολο του κινήματος της ιταλικής ενοποίησης (Risorgimento).",
        "funFacts": [
            "Το χορωδιακό 'Va, pensiero' (Το χορωδιακό των Εβραίων σκλάβων) από τον Ναμπούκο έγινε ο ανεπίσημος ύμνος του ιταλικού πατριωτισμού.",
            "Το όνομα 'VERDI' χρησιμοποιούνταν ως μυστικό σύνθημα για τον μελλοντικό βασιλιά της ενωμένης Ιταλίας: Vittorio Emanuele Re D'Italia."
        ],
        "source": "https://en.wikipedia.org/wiki/Giuseppe_Verdi",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "opera", "verdi"]
    },
    {
        "id": "music_med_147",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου τραγουδιστή των The Doors που έγινε σύμβολο της αντικουλτούρας με το παρατσούκλι 'The Lizard King';",
        "answers": ["Ρέι Μάνζαρεκ", "Ρόμπι Κρίγκερ", "Τζιμ Μόρισον", "Τζον Ντένσμορ"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Τζιμ Μόρισον (Jim Morrison) υπήρξε χαρισματικός ποιητής και frontman των The Doors, γνωστός για τη βαθιά βαρύτονη φωνή του και τις απρόβλεπτες εμφανίσεις του.",
        "funFacts": [
            "Ο Μόρισον πέθανε στο Παρίσι στις 3 Ιουλίου 1971 σε ηλικία 27 ετών και ο τάφος του στο κοιμητήριο Père Lachaise αποτελεί έναν από τους πιο δημοφιλείς τόπους προσκυνήματος.",
            "Στον τάφο του υπάρχει χαραγμένη η αρχαιοελληνική επιγραφή 'ΚΑΤΑ ΤΟΝ ΔΑΙΜΟΝΑ ΕΑΥΤΟΥ'."
        ],
        "source": "https://en.wikipedia.org/wiki/Jim_Morrison",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "the_doors"]
    },
    {
        "id": "music_med_148",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου αμερικανικού μουσικού τηλεοπτικού προγράμματος της δεκαετίας του '70 που παρουσίαζε μαύρη μουσική (soul, funk, disco) με χορευτές στη γραμμή;",
        "answers": ["American Bandstand", "Top of the Pops", "Soul Train", "The Midnight Special"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Soul Train' δημιουργήθηκε και παρουσιάστηκε από τον Ντον Κορνίλιους από το 1971, αναδεικνύοντας τη μαύρη μουσική, τη μόδα και τον χορό στην αμερικανική τηλεόραση.",
        "funFacts": [
            "Η περίφημη γραμμή χορού 'Soul Train Line' όπου οι χορευτές περνούσαν ανά ζεύγη χορεύοντας στο κέντρο έγινε παγκόσμιο πολιτιστικό φαινόμενο.",
            "Η χαρακτηριστική ευχή αποχαιρετισμού του Ντον Κορνίλιους στο τέλος κάθε επεισοδίου ήταν '...and you can bet your last money, it's all gonna be a stone gas, honey! Peace, love and soul!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Soul_Train",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "tv", "soul", "funk"]
    },
    {
        "id": "music_med_149",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο κρουστό όργανο της συμφωνικής ορχήστρας αποτελείται από μεγάλους χάλκινους λέβητες καλυμμένους με μεμβράνη και κουρδίζεται με ποδοπλήκτρο (πεντάλ) σε συγκεκριμένες νότες;",
        "answers": ["Τα τύμπανα (τιμπάνι / timpani)", "Η γκρανκάσα", "Το ταμπούρο", "Το ταμ-ταμ (γκονγκ)"],
        "correctAnswerIndex": 0,
        "explanation": "Τα τιμπάνι (timpani ή κλασικά τύμπανα) είναι τα μόνα τύμπανα της ορχήστρας που παράγουν συγκεκριμένο τονικό ύψος (pitch) και κουρδίζονται με ακρίβεια.",
        "funFacts": [
            "Ο τυμπανιστής (τιμπανίστας) χρησιμοποιεί διαφορετικές μπαγκέτες με κεφαλές από τσόχα, ξύλο ή δέρμα για να αλλάζει τη σκληρότητα του ήχου.",
            "Τα τιμπάνι εισήχθησαν στην ευρωπαϊκή στρατιωτική και ορχηστρική μουσική από τη Μέση Ανατολή κατά την περίοδο των Σταυροφοριών."
        ],
        "source": "https://en.wikipedia.org/wiki/Timpani",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "instruments", "percussion"]
    },
    {
        "id": "music_med_150",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου rap άλμπουμ του Dr. Dre του 1992 που εισήγαγε το υποείδος G-Funk και ανέδειξε τον Snoop Dogg;",
        "answers": ["The Chronic", "Doggystyle", "Straight Outta Compton", "2001"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'The Chronic' του Dr. Dre καθόρισε τον ήχο της West Coast rap συνδυάζοντας funk samples των Parliament-Funkadelic, μελωδικά synthesizers και χαλαρά beats.",
        "funFacts": [
            "Ο τίτλος του άλμπουμ ήταν παρατσούκλι για μια ισχυρή ποικιλία κάνναβης στο Λος Άντζελες.",
            "Το 'The Chronic' συμπεριλήφθηκε στο Εθνικό Μητρώο Ηχογραφήσεων της Βιβλιοθήκης του Κογκρέσου των ΗΠΑ ως πολιτιστικό μνημείο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Chronic",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "dr_dre"]
    },
    {
        "id": "music_med_151",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το διάσημο ρέγκε και ska συγκρότημα από το Μπέρμιγχαμ που πήρε το όνομά του από το επίσημο έντυπο επιδόματος ανεργίας της βρετανικής κυβέρνησης;",
        "answers": ["The Specials", "UB40", "Madness", "The Selecter"],
        "correctAnswerIndex": 1,
        "explanation": "Οι UB40 σχηματίστηκαν το 1978 από νέους μουσικούς που ήταν άνεργοι και πήραν το όνομά τους από το έντυπο ανεργίας 'Unemployment Benefit, Form 40'.",
        "funFacts": [
            "Έχουν πουλήσει πάνω από 70 εκατομμύρια δίσκους παγκοσμίως με παγκόσμια νούμερο 1 hits όπως το 'Red Red Wine' και το 'Can't Help Falling in Love'.",
            "Η κάρτα ανεργίας UB40 απεικονιζόταν στο εξώφυλλο του πρώτου τους άλμπουμ, 'Signing Off' (1980)."
        ],
        "source": "https://en.wikipedia.org/wiki/UB40",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "reggae", "ub40"]
    },
    {
        "id": "music_med_152",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Φινλανδού συνθέτη της ύστερης ρομαντικής εποχής που έγραψε το πατριωτικό συμφωνικό ποίημα 'Finlandia';",
        "answers": ["Έντβαρντ Γκριγκ", "Γιαν Σιμπέλιους", "Καρλ Νίλσεν", "Έινιβαλ Σάλινεν"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Γιαν Σιμπέλιους (Jean Sibelius) υπήρξε ο εθνικός συνθέτης της Φινλανδίας, του οποίου η μουσική έπαιξε καθοριστικό ρόλο στη σφυρηλάτηση της φινλανδικής εθνικής ταυτότητας κατά της ρωσικής κυριαρχίας.",
        "funFacts": [
            "Το 'Finlandia' απαγορεύτηκε από τη ρωσική τσαρική λογοκρισία και οι ορχήστρες το παρουσίαζαν με παραπλανητικούς τίτλους όπως 'Χαρούμενα Αισθήματα στην Αυγή της Φινλανδικής Άνοιξης'.",
            "Ο Σιμπέλιους απεικονιζόταν στο χαρτονόμισμα των 100 φινλανδικών μάρκων πριν την εισαγωγή του ευρώ."
        ],
        "source": "https://en.wikipedia.org/wiki/Jean_Sibelius",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "sibelius"]
    },
    {
        "id": "music_med_153",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου progressive rock άλμπουμ των Pink Floyd του 1979 που αφηγείται την ιστορία ενός απομονωμένου ροκ σταρ ονόματι Pink;",
        "answers": ["Animals", "Wish You Were Here", "The Wall", "The Final Cut"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'The Wall' σε σύλληψη του Ρότζερ Γουότερς εξερευνά τη μοναξιά, το τραύμα του πολέμου και την αποξένωση, δημιουργώντας ένα από τα πιο εμβληματικά concept albums στην ιστορία.",
        "funFacts": [
            "Το single 'Another Brick in the Wall, Part 2' με τη διάσημη παιδική χορωδία έγινε το μοναδικό νούμερο 1 single των Pink Floyd στο Billboard Hot 100 των ΗΠΑ.",
            "Στις συναυλίες της περιοδείας, ένα γιγάντιο τείχος από χαρτονένια τούβλα χτιζόταν σταδιακά κατά τη διάρκεια του σόου ανάμεσα στο συγκρότημα και το κοινό."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Wall",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "pink_floyd"]
    },
    {
        "id": "music_med_154",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είδος παραδοσιακής μουσικής και χορού της νότιας Ισπανίας (Ανδαλουσία) περιλαμβάνει cante (τραγούδι), toque (κιθάρα), baile (χορό) και palmas (παλαμάκια);",
        "answers": ["Το τάγκο", "Το μπολερό", "Το φλαμένκο", "Η σάλσα"],
        "correctAnswerIndex": 2,
        "explanation": "Το φλαμένκο (flamenco) αναπτύχθηκε από τη συνάντηση των πολιτισμών των Ρομά, των Μαυριτανών, των Εβραίων και των Ανδαλουσιανών και είναι αναγνωρισμένο από την UNESCO.",
        "funFacts": [
            "Ο βαθύς συναισθηματικός εκστατικός δεσμός μεταξύ ερμηνευτή και κοινού στο φλαμένκο ονομάζεται 'duende'.",
            "Η κιθάρα του φλαμένκο διαφέρει από την κλασική κιθάρα: είναι ελαφρύτερη, κατασκευασμένη από κυπαρίσσι και παράγει πιο οξύ, κρουστό ήχο."
        ],
        "source": "https://en.wikipedia.org/wiki/Flamenco",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "world_music", "flamenco", "spain"]
    },
    {
        "id": "music_med_155",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Βραζιλιάνου συνθέτη που συνδύασε τη σάμπα με τη δυτική τζαζ δημιουργώντας την Bossa Nova με το τραγούδι 'The Girl from Ipanema';",
        "answers": ["Αντόνιο Κάρλος Ζομπίμ", "Καετάνο Βελόσο", "Ζιλμπέρτο Ζιλ", "Σέρτζιο Μέντες"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Αντόνιο Κάρλος Ζομπίμ (Tom Jobim) μαζί με τον Ζοάο Ζιλμπέρτο και τον Βινίσιους ντε Μοράες δημιούργησαν την Bossa Nova στα τέλη της δεκαετίας του 1950 στο Ρίο ντε Τζανέιρο.",
        "funFacts": [
            "Το 'The Girl from Ipanema' (Garota de Ipanema) είναι το δεύτερο πιο πολυηχογραφημένο ποπ τραγούδι στην ιστορία μετά το 'Yesterday' των Beatles.",
            "Το διεθνές αεροδρόμιο του Ρίο ντε Τζανέιρο (Galeão) ονομάστηκε επίσημα προς τιμήν του Tom Jobim το 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Ant%C3%B4nio_Carlos_Jobim",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "bossa_nova", "brazil", "jazz"]
    },
    {
        "id": "music_med_156",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο hard rock συγκρότημα από το Λος Άντζελες κυκλοφόρησε το 1987 το πιο επιτυχημένο ντεμπούτο άλμπουμ στην ιστορία των ΗΠΑ, το 'Appetite for Destruction';",
        "answers": ["Guns N' Roses", "Mötley Crüe", "Poison", "Van Halen"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Guns N' Roses με τον Axl Rose και τον Slash πούλησαν πάνω από 30 εκατομμύρια αντίτυπα του 'Appetite for Destruction', που περιλαμβάνει τα 'Sweet Child o' Mine' και 'Welcome to the Jungle'.",
        "funFacts": [
            "Το χαρακτηριστικό εισαγωγικό riff του 'Sweet Child o' Mine' ξεκίνησε από τον Slash ως μια απλή άσκηση προθέρμανσης δακτύλων που ο ίδιος αρχικά δεν έπαιρνε στα σοβαρά.",
            "Το αρχικό εξώφυλλο του άλμπουμ απαγορεύτηκε από τα περισσότερα δισκοπωλεία και αντικαταστάθηκε από τον κλασικό κέλτικο σταυρό με τα κρανία των πέντε μελών."
        ],
        "source": "https://en.wikipedia.org/wiki/Appetite_for_Destruction",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "guns_n_roses"]
    },
    {
        "id": "music_med_157",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος συνθέτης της όπερας από την Αυστρία έγραψε τα αριστουργήματα 'Οι Γάμοι του Φίγκαρο', 'Ντον Τζοβάνι' και 'Ο Μαγικός Αυλός';",
        "answers": ["Βόλφγκανγκ Αμαντέους Μότσαρτ", "Γιόζεφ Χάιντν", "Κρίστοφ Βίλιμπαλντ Γκλουκ", "Λούντβιχ βαν Μπετόβεν"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Βόλφγκανγκ Αμαντέους Μότσαρτ (Wolfgang Amadeus Mozart, 1756-1791) συνέθεσε πάνω από 600 έργα σε σχεδόν κάθε μουσικό είδος της εποχής του.",
        "funFacts": [
            "Ο Μότσαρτ ξεκίνησε να συνθέτει μουσική σε ηλικία μόλις 5 ετών και έγραψε την πρώτη του συμφωνία σε ηλικία 8 ετών.",
            "Το τελευταίο του έργο, το συγκλονιστικό 'Ρέκβιεμ' σε Ρε ελάσσονα (K. 626), έμεινε ημιτελές λόγω του πρόωρου θανάτου του σε ηλικία 35 ετών και ολοκληρώθηκε από τον μαθητή του Φραντς Ξάβερ Ζύσμαϊερ."
        ],
        "source": "https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "mozart"]
    },
    {
        "id": "music_med_158",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο progressive rock συγκρότημα από την Αγγλία κυκλοφόρησε το 1971 το άλμπουμ 'Fragile' με το κορυφαίο κομμάτι 'Roundabout';",
        "answers": ["Genesis", "Yes", "King Crimson", "ELP"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Yes, με τραγουδιστή τον Τζον Άντερσον, μπασίστα τον Κρις Σκουάιρ και πληκτρά τον Ρικ Γουέικμαν, καθιέρωσαν τις πολυφωνικές αρμονίες και την τεχνική αρτιότητα του progressive rock.",
        "funFacts": [
            "Τα φανταστικά, απόκοσμα εξώφυλλα των άλμπουμ των Yes σχεδιάστηκαν από τον διάσημο Άγγλο καλλιτέχνη Ρότζερ Ντιν.",
            "Το 'Roundabout' γνώρισε μια απρόσμενη τεράστια viral αναβίωση τη δεκαετία του 2010 ως το διάσημο 'To Be Continued...' meme στο διαδίκτυο, προερχόμενο από το anime JoJo's Bizarre Adventure."
        ],
        "source": "https://en.wikipedia.org/wiki/Fragile_(Yes_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "progressive_rock", "yes"]
    },
    {
        "id": "music_med_159",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου hip hop παραγωγού και ράπερ από την Ατλάντα που ίδρυσε την Goodie Mob και τους Outkast ως μέρος του Dungeon Family κολλεκτίβου;",
        "answers": ["Organized Noize", "Timberland", "Swizz Beatz", "Metro Boomin"],
        "correctAnswerIndex": 0,
        "explanation": "Η ομάδα παραγωγής Organized Noize (Sleepy Brown, Rico Wade, Ray Murray) δημιούργησε τον χαρακτηριστικό ήχο του Southern hip hop για τους Outkast και TLC.",
        "funFacts": [
            "Ηχογραφούσαν στο υπόγειο του σπιτιού της μητέρας του Rico Wade, το οποίο ονόμαζαν 'The Dungeon' (Το Μπουντρούμι).",
            "Παρήγαγαν επίσης το παγκόσμιο hit 'Waterfalls' των TLC το 1994."
        ],
        "source": "https://en.wikipedia.org/wiki/Organized_Noize",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "production"]
    },
    {
        "id": "music_med_160",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας συνθέτης βραβεύτηκε με το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 1961 για 'Τα Παιδιά του Πειραιά' από την ταινία 'Ποτέ την Κυριακή';",
        "answers": ["Μίκης Θεοδωράκης", "Μάνος Χατζιδάκις", "Σταύρος Ξαρχάκος", "Μάνος Λοΐζος"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Μάνος Χατζιδάκις κέρδισε το Όσκαρ για το τραγούδι που ερμήνευσε η Μελίνα Μερκούρη στην ταινία του Ζιλ Ντασέν, όντας ο πρώτος Έλληνας συνθέτης που τιμήθηκε με το αγαλματίδιο.",
        "funFacts": [
            "Ο Χατζιδάκις δεν παρέστη στην τελετή των Όσκαρ στο Λος Άντζελες και αρχικά δεν εκτιμούσε ιδιαίτερα τη μαζική εμπορική επιτυχία του τραγουδιού.",
            "Το Όσκαρ του εκλάπη κάποια στιγμή και η Ακαδημία του έστειλε αντικαταστάτη μετά από χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Manos_Hatzidakis",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "hadjidakis", "oscars"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(QUESTIONS)} questions for music_medium.")
    validate_and_append("music", "medium", 3, QUESTIONS)

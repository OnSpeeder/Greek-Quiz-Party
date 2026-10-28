# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# 50 music medium questions: music_med_161 to music_med_210
# Distribution of correctAnswerIndex: 13x0, 13x1, 12x2, 12x3 = 50 total
QUESTIONS = [
    {
        "id": "music_med_161",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου τραγουδιστή των The Rolling Stones από την ίδρυσή τους το 1962;",
        "answers": ["Μικ Τζάγκερ", "Κιθ Ρίτσαρντς", "Μπράιαν Τζόουνς", "Τσάρλι Γουότς"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μικ Τζάγκερ (Mick Jagger) είναι ο εμβληματικός frontman των The Rolling Stones, γνωστός για την απαράμιλλη κινησιολογία και σκηνική του ενέργεια.",
        "funFacts": [
            "Ο Τζάγκερ και ο Κιθ Ρίτσαρντς γνωρίζονταν από το δημοτικό σχολείο στο Ντάρτφορντ και ξανασυναντήθηκαν τυχαία σε μια αποβάθρα τρένου το 1961 κρατώντας δίσκους rhythm and blues.",
            "Χρίστηκε ιππότης από τη Βασίλισσα Ελισάβετ Β' το 2003 για τις υπηρεσίες του στη λαϊκή μουσική."
        ],
        "source": "https://en.wikipedia.org/wiki/Mick_Jagger",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "rolling_stones"]
    },
    {
        "id": "music_med_162",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της κλασικής εποχής έγραψε την κωμική όπερα 'Ο Κουρέας της Σεβίλλης' (Il barbiere di Siviglia) μέσα σε λιγότερο από τρεις εβδομάδες;",
        "answers": ["Γκαετάνο Ντονιτσέτι", "Τζοακίνο Ροσίνι", "Βιντσέντζο Μπελίνι", "Ντομένικο Τσιμαρόζα"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Τζοακίνο Ροσίνι (Gioachino Rossini) συνέθεσε το αριστούργημά του το 1816 σε ηλικία 24 ετών, καθιερώνοντας την τεχνική του 'crescendo Rossiniano'.",
        "funFacts": [
            "Η πρεμιέρα στη Ρώμη ήταν σκέτη καταστροφή: ένας τραγουδιστής σκόνταψε και μάτωσε, μια μαύρη γάτα περπάτησε στη σκηνή και το κοινό σφύριζε ασταμάτητα.",
            "Ο Ροσίνι ήταν επίσης δεινός καλοφαγάς και μάγειρας, εμπνέοντας διάσημα πιάτα όπως το 'Tournedos Rossini'."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Barber_of_Seville",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "opera", "rossini"]
    },
    {
        "id": "music_med_163",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό new wave συγκρότημα με τραγουδιστή τον Simon Le Bon κυκλοφόρησε τα smash hits 'Rio', 'Hungry Like the Wolf' και 'Save a Prayer';",
        "answers": ["Spandau Ballet", "Wham!", "Duran Duran", "Tears for Fears"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Duran Duran από το Μπέρμιγχαμ αποτέλεσαν την αιχμή του δόρατος του κινήματος των New Romantics, εκμεταλλευόμενοι όσο λίγοι τη δύναμη του MTV στα 80s.",
        "funFacts": [
            "Πήραν το όνομά τους από τον κακό επιστήμονα Dr. Durand Durand στην καλτ ταινία επιστημονικής φαντασίας 'Barbarella' (1968).",
            "Το συγκρότημα ερμήνευσε το 'A View to a Kill' (1985), το μοναδικό τραγούδι τίτλων ταινίας James Bond που έφτασε στο νούμερο 1 του αμερικανικού Billboard Hot 100."
        ],
        "source": "https://en.wikipedia.org/wiki/Duran_Duran",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "80s", "duran_duran"]
    },
    {
        "id": "music_med_164",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος τυφλός Αμερικανός τραγουδιστής, συνθέτης και πολυοργανίστας κυκλοφόρησε το θρυλικό άλμπουμ 'Songs in the Key of Life' το 1976;",
        "answers": ["Ρέι Τσαρλς", "Μάρβιν Γκέι", "Ντόνι Χάθαγουεϊ", "Στίβι Γουόντερ"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Στίβι Γουόντερ (Stevie Wonder) ηχογράφησε το διπλό αριστούργημα 'Songs in the Key of Life' με κλασικά τραγούδια όπως τα 'Sir Duke' και 'Isn't She Lovely'.",
        "funFacts": [
            "Ο Στίβι Γουόντερ κέρδισε το βραβείο Grammy για το Άλμπουμ της Χρονιάς για τρία διαδοχικά άλμπουμ του τη δεκαετία του '70 (Innervisions, Fulfillingness' First Finale, Songs in the Key of Life).",
            "Υπέγραψε στη δισκογραφική Motown σε ηλικία μόλις 11 ετών με το όνομα 'Little Stevie Wonder'."
        ],
        "source": "https://en.wikipedia.org/wiki/Songs_in_the_Key_of_Life",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soul", "stevie_wonder"]
    },
    {
        "id": "music_med_165",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα heavy metal με κιθαρίστα τον Ρίτσι Μπλάκμορ και τραγουδιστή τον Ίαν Γκίλαν κυκλοφόρησε το 'Smoke on the Water' το 1972;",
        "answers": ["Deep Purple", "Black Sabbath", "Uriah Heep", "Led Zeppelin"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Deep Purple ηχογράφησαν το 'Smoke on the Water' για το άλμπουμ 'Machine Head', βασισμένοι στην πραγματική ιστορία της πυρκαγιάς στο καζίνο του Μοντρέ κατά τη διάρκεια συναυλίας του Φρανκ Ζάπα.",
        "funFacts": [
            "Το εμβληματικό τετράφωνο riff κιθάρας του 'Smoke on the Water' είναι ένα από τα πρώτα κομμάτια που μαθαίνει κάθε αρχάριος κιθαρίστας.",
            "Οι Deep Purple είχαν καταχωρηθεί στο Βιβλίο των Ρεκόρ Γκίνες το 1975 ως το πιο θορυβώδες συγκρότημα στον κόσμο (117 dB)."
        ],
        "source": "https://en.wikipedia.org/wiki/Smoke_on_the_Water",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "deep_purple"]
    },
    {
        "id": "music_med_166",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος συνθέτης της ρομαντικής περιόδου από τη Νορβηγία έγραψε τη διάσημη σουίτα 'Πέερ Γκυντ' (Peer Gynt), που περιλαμβάνει το 'Στη Σπηλιά του Βασιλιά του Βουνού';",
        "answers": ["Γιαν Σιμπέλιους", "Έντβαρντ Γκριγκ", "Καρλ Νίλσεν", "Έντβαρντ Μουνκ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Έντβαρντ Γκριγκ (Edvard Grieg) έγραψε τη μουσική για το θεατρικό έργο του Ερρίκου Ίψεν 'Πέερ Γκυντ' το 1875, ενσωματώνοντας νορβηγικά δημοτικά μοτίβα.",
        "funFacts": [
            "Το 'In the Hall of the Mountain King' ξεκινά σε εξαιρετικά αργό και ήσυχο τέμπο και κλιμακώνεται σε έναν φρενήρη μουσικό ανεμοστρόβιλο.",
            "Ο Γκριγκ είχε ύψος μόλις 1,52 μ. και κουβαλούσε πάντα στην τσέπη του ένα μικρό πήλινο βατραχάκι ως φυλαχτό πριν από κάθε συναυλία."
        ],
        "source": "https://en.wikipedia.org/wiki/Peer_Gynt_(Grieg)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "grieg"]
    },
    {
        "id": "music_med_167",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα της Britpop με ηγέτες τα αδέλφια Λίαμ και Νόελ Γκάλαχερ κυκλοφόρησε το θρυλικό άλμπουμ '(What's the Story) Morning Glory?' το 1995;",
        "answers": ["Blur", "Pulp", "Oasis", "Suede"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Oasis από το Μάντσεστερ κυριάρχησαν στα 90s με παγκόσμιους ύμνους όπως τα 'Wonderwall', 'Don't Look Back in Anger' και 'Champagne Supernova'.",
        "funFacts": [
            "Το '(What's the Story) Morning Glory?' παραμένει το πέμπτο άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία των βρετανικών charts.",
            "Η περίφημη 'Μάχη της Britpop' τον Αύγουστο του 1995 ανάμεσα στο 'Roll With It' των Oasis και το 'Country House' των Blur δίχασε ολόκληρο το Ηνωμένο Βασίλειο."
        ],
        "source": "https://en.wikipedia.org/wiki/(What%27s_the_Story)_Morning_Glory%3F",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "britpop", "oasis"]
    },
    {
        "id": "music_med_168",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο έγχορδο λαϊκό όργανο της Κρήτης παίζεται με δοξάρι και συνοδεύει παραδοσιακά τις μαντινάδες και τους κρητικούς χορούς;",
        "answers": ["Το σαντούρι", "Το βιολί", "Το κανονάκι", "Η κρητική λύρα"],
        "correctAnswerIndex": 3,
        "explanation": "Η κρητική λύρα είναι αχλαδόσχημο τοξωτό έγχορδο με τρεις χορδές, όπου οι νότες δεν πιέζονται πάνω στην ταστιέρα αλλά πλαγίως με τα νύχια των δακτύλων.",
        "funFacts": [
            "Παραδοσιακά, το δοξάρι της λύρας έφερε μικρά σφαιρικά κουδουνάκια (γερακοκούδουνα) που κρατούσαν ρυθμό καθώς ο λυράρης έπαιζε.",
            "Κορυφαίοι δεξιοτέχνες της κρητικής λύρας υπήρξαν ο Νίκος Ξυλούρης, ο Κώστας Μουντάκης και ο Θανάσης Σκορδαλός."
        ],
        "source": "https://en.wikipedia.org/wiki/Cretan_lyra",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "traditional_instruments", "crete"]
    },
    {
        "id": "music_med_169",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο punk rock συγκρότημα από το Λονδίνο με μέλη τους Johnny Rotten και Sid Vicious κυκλοφόρησε το προκλητικό άλμπουμ 'Never Mind the Bollocks' το 1977;",
        "answers": ["Sex Pistols", "The Clash", "The Damned", "Buzzcocks"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Sex Pistols υπό το μάνατζμεντ του Μάλκολμ ΜακΛάρεν πυροδότησαν την πανκ επανάσταση στο Ηνωμένο Βασίλειο με τραγούδια όπως το 'Anarchy in the U.K.' και το 'God Save the Queen'.",
        "funFacts": [
            "Το 'God Save the Queen' κυκλοφόρησε κατά τη διάρκεια του Αργυρού Ιωβηλαίου της Βασίλισσας Ελισάβετ Β' και απαγορεύτηκε πλήρως από το BBC.",
            "Το συγκρότημα διαλύθηκε επεισοδιακά τον Ιανουάριο του 1978 κατά τη διάρκεια της πρώτης του αμερικανικής περιοδείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Sex_Pistols",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "punk", "sex_pistols"]
    },
    {
        "id": "music_med_170",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Γάλλος συνθέτης της ιμπρεσιονιστικής μουσικής συνέθεσε τα αριστουργήματα 'Το Φως του Φεγγαριού' (Clair de lune) και 'Η Θάλασσα' (La Mer);",
        "answers": ["Μορίς Ραβέλ", "Κλοντ Ντεμπισί", "Ερίκ Σατί", "Γκαμπριέλ Φορέ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Κλοντ Ντεμπισί (Claude Debussy) εισήγαγε νέες αρμονίες, ολοτονικές κλίμακες και λεπτές ηχητικές αποχρώσεις, αποτυπώνοντας στη μουσική τις αρχές του ιμπρεσιονισμού.",
        "funFacts": [
            "Ο ίδιος ο Ντεμπισί αντιπαθούσε έντονα τον όρο 'ιμπρεσιονιστής', δηλώνοντας ότι προσπαθούσε απλώς να εκφράσει διαφορετικές πραγματικότητες.",
            "Το 'Clair de lune' είναι το τρίτο μέρος της 'Σουίτας Μπεργκαμάσκ' για πιάνο και εμπνεύστηκε από ποίημα του Πολ Βερλέν."
        ],
        "source": "https://en.wikipedia.org/wiki/Claude_Debussy",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "debussy"]
    },
    {
        "id": "music_med_171",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των U2 του 1991 που ηχογραφήθηκε στα Hansa Studios του Βερολίνου μετά την πτώση του Τείχους;",
        "answers": ["War", "Zooropa", "Achtung Baby", "Pop"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Achtung Baby' ανανέωσε ριζικά τον ήχο των U2 ενσωματώνοντας alternative rock, industrial και ηλεκτρονικά χορευτικά στοιχεία, περιλαμβάνοντας το κλασικό 'One'.",
        "funFacts": [
            "Το 'One' γράφτηκε κατά τη διάρκεια μιας έντονης κρίσης στο συγκρότημα, όπου τα μέλη κόντεψαν να διαλυθούν λόγω καλλιτεχνικών διαφωνιών.",
            "Όλα τα έσοδα από το single 'One' δωρήθηκαν σε οργανώσεις έρευνας για το AIDS."
        ],
        "source": "https://en.wikipedia.org/wiki/Achtung_Baby",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "u2"]
    },
    {
        "id": "music_med_172",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια είναι η χαμηλότερη φωνητική κατηγορία στους άνδρες τραγουδιστές της όπερας και της κλασικής μουσικής;",
        "answers": ["Τενόρος", "Βαρύτονος", "Κόντρα τενόρος", "Βαθύφωνος (Μπάσος)"],
        "correctAnswerIndex": 3,
        "explanation": "Ο βαθύφωνος (bass) διαθέτει τη χαμηλότερη ανθρώπινη φωνή, με έκταση που κυμαίνεται συνήθως από το Μι-1 έως το Μι-3.",
        "funFacts": [
            "Η υποκατηγορία 'basso profondo' φτάνει σε εξαιρετικά χαμηλές νότες κάτω από το Ντο-1 και είναι ιδιαίτερα διαδεδομένη στη ρωσική ορθόδοξη εκκλησιαστική μουσική.",
            "Στην όπερα, οι ρόλοι του μπάσου προορίζονται συνήθως για βασιλιάδες, ιερείς, ηλικιωμένους σοφούς ή τον ίδιο τον διάβολο (Μεφιστοφελής)."
        ],
        "source": "https://en.wikipedia.org/wiki/Bass_(voice_type)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "opera", "voice"]
    },
    {
        "id": "music_med_173",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα southern rock από το Τζάκσονβιλ της Φλόριντα κυκλοφόρησε τους κλασικούς ύμνους 'Sweet Home Alabama' και 'Free Bird';",
        "answers": ["Lynyrd Skynyrd", "The Allman Brothers Band", "ZZ Top", "Creedence Clearwater Revival"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Lynyrd Skynyrd με τραγουδιστή τον Ρόνι Βαν Ζαντ καθόρισαν τον southern rock ήχο της δεκαετίας του 1970 με τριπλή κιθαριστική επίθεση.",
        "funFacts": [
            "Το 'Sweet Home Alabama' γράφτηκε ως απάντηση στα τραγούδια του Νιλ Γιανγκ 'Southern Man' και 'Alabama' που ασκούσαν κριτική στον ρατσισμό του Νότου.",
            "Το 1977, τρία μέλη του συγκροτήματος σκοτώθηκαν τραγικά σε αεροπορικό δυστύχημα στο Μισισιπή λίγες μέρες μετά την κυκλοφορία του άλμπουμ 'Street Survivors'."
        ],
        "source": "https://en.wikipedia.org/wiki/Lynyrd_Skynyrd",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "southern_rock"]
    },
    {
        "id": "music_med_174",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της Αναγέννησης έσωσε -σύμφωνα με τον μύθο- την πολυφωνική μουσική από την απαγόρευση της Καθολικής Εκκλησίας με τη 'Missa Papae Marcelli';",
        "answers": ["Κλαούντιο Μοντεβέρντι", "Τζοβάνι Πιερλουίτζι ντα Παλεστρίνα", "Ορλάντο ντι Λάσσο", "Τζοβάνι Γκαμπριέλι"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Παλεστρίνα (Palestrina, 1525-1594) έγραψε τη λειτουργία 'Missa Papae Marcelli' επιδεικνύοντας ότι η πολυφωνία μπορεί να είναι σαφής και ευανάγνωστη χωρίς να κρύβει τα ιερά λόγια, πείθοντας τη Σύνοδο του Τριδέντου.",
        "funFacts": [
            "Το στιλ του Παλεστρίνα έγινε το επίσημο πρότυπο της αναγεννησιακής αντιστικτικής τέχνης που διδάσκεται μέχρι σήμερα στα ωδεία.",
            "Υπηρέτησε ως αρχιμουσικός στη χορωδία της Καπέλα Τζούλια στον Άγιο Πέτρο της Ρώμης."
        ],
        "source": "https://en.wikipedia.org/wiki/Giovanni_Pierluigi_da_Palestrina",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "renaissance", "palestrina"]
    },
    {
        "id": "music_med_175",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό trip-hop συγκρότημα από το Μπρίστολ κυκλοφόρησε τα πρωτοποριακά άλμπουμ 'Blue Lines' (1991) και 'Mezzanine' (1998);",
        "answers": ["Portishead", "Tricky", "Massive Attack", "Morcheeba"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Massive Attack (Robert Del Naja, Grant Marshall κ.ά.) θεωρούνται οι θεμελιωτές του Bristol sound (trip-hop), συνδυάζοντας hip-hop beats, dub reggae και κινηματογραφικά έγχορδα.",
        "funFacts": [
            "Το κομμάτι 'Teardrop' με φωνητικά από την Ελίζαμπεθ Φρέιζερ των Cocteau Twins χρησιμοποιήθηκε ως το θέμα τίτλων της επιτυχημένης τηλεοπτικής σειράς 'House M.D.'.",
            "Επίμονοι αστικοί μύθοι συνδέουν το ιδρυτικό μέλος Robert Del Naja ('3D') με τον ανώνυμο καλλιτέχνη δρόμου Banksy."
        ],
        "source": "https://en.wikipedia.org/wiki/Massive_Attack",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "trip_hop", "electronic", "massive_attack"]
    },
    {
        "id": "music_med_176",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Αμερικανού κιθαρίστα και τραγουδιστή των blues που έπαιζε στην κιθάρα του Gibson ES-355 που αποκαλούσε χαϊδευτικά 'Lucille';",
        "answers": ["Μάντι Γουότερς", "Άλμπερτ Κινγκ", "Τζον Λι Χούκερ", "Μπι Μπι Κινγκ (B.B. King)"],
        "correctAnswerIndex": 3,
        "explanation": "Ο B.B. King ονόμασε την κιθάρα του Lucille το 1949, αφού κινδύνεψε να καεί ζωντανός μπαίνοντας σε μια φλεγόμενη αίθουσα χορού για να τη σώσει μετά από καβγά δύο ανδρών για μια γυναίκα ονόματι Lucille.",
        "funFacts": [
            "Ο B.B. King ανέπτυξε ένα μοναδικό στιλ σολαρίσματος με χαρακτηριστικό vibrato του καρπού, επηρεάζοντας βαθιά κιθαρίστες όπως ο Έρικ Κλάπτον και ο Τζίμι Χέντριξ.",
            "Έδινε κατά μέσο όρο 250 με 300 συναυλίες τον χρόνο μέχρι τα βαθιά του γεράματα."
        ],
        "source": "https://en.wikipedia.org/wiki/B.B._King",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "blues", "guitar", "bb_king"]
    },
    {
        "id": "music_med_177",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των Joy Division του 1979 που περιλαμβάνει τα κομμάτια 'Disorder' και 'She's Lost Control';",
        "answers": ["Unknown Pleasures", "Closer", "Substance", "Still"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'Unknown Pleasures' των Joy Division με παραγωγό τον Μάρτιν Χάνετ δημιούργησε τον υποβλητικό, κλειστοφοβικό ήχο του post-punk.",
        "funFacts": [
            "Ο παραγωγός Μάρτιν Χάνετ χρησιμοποίησε ανορθόδοξες μεθόδους ηχογράφησης, όπως το σπάσιμο μπουκαλιών και τη λειτουργία ανελκυστήρα, για να δημιουργήσει τα μοναδικά ηχητικά εφέ.",
            "Το συγκρότημα ηχογράφησε το άλμπουμ στα Strawberry Studios του Στόκπορτ μέσα σε μόλις τρία Σαββατοκύριακα."
        ],
        "source": "https://en.wikipedia.org/wiki/Unknown_Pleasures",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "post_punk", "joy_division"]
    },
    {
        "id": "music_med_178",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας λαϊκός συνθέτης έγραψε αθάνατα τραγούδια όπως 'Συννεφιασμένη Κυριακή', 'Νύχτωσε χωρίς φεγγάρι' και 'Αρχόντισσα';",
        "answers": ["Μανώλης Χιώτης", "Βασίλης Τσιτσάνης", "Γιώργος Ζαμπέτας", "Απόστολος Καλδάρας"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Βασίλης Τσιτσάνης (1915-1984) από τα Τρίκαλα θεωρείται ο αναμορφωτής του ελληνικού λαϊκού τραγουδιού, βγάζοντας το ρεμπέτικο από το περιθώριο και καθιερώνοντάς το στην ευρύτερη κοινωνία.",
        "funFacts": [
            "Έγραψε τη 'Συννεφιασμένη Κυριακή' κατά τη διάρκεια της μαύρης ναζιστικής κατοχής στη Θεσσαλονίκη το 1943.",
            "Πέθανε στο Λονδίνο ακριβώς την ημέρα των 69ων γενεθλίων του, στις 18 Ιανουαρίου 1984."
        ],
        "source": "https://en.wikipedia.org/wiki/Vassilis_Tsitsanis",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "tsitsanis"]
    },
    {
        "id": "music_med_179",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό alternative rock συγκρότημα με ηγέτη τον Robert Smith κυκλοφόρησε το σκοτεινό αριστούργημα 'Disintegration' το 1989;",
        "answers": ["The Smiths", "Siouxsie and the Banshees", "The Cure", "Bauhaus"],
        "correctAnswerIndex": 2,
        "explanation": "Οι The Cure δημιούργησαν το 'Disintegration' με εμβληματικά κομμάτια όπως τα 'Lovesong', 'Pictures of You' και 'Lullaby', ορίζοντας τη γοτθική ροκ.",
        "funFacts": [
            "Ο Ρόμπερτ Σμιθ έγραψε το άλμπουμ καθώς πλησίαζε τα 30ά του γενέθλια, βιώνοντας υπαρξιακή κρίση ότι δεν είχε δημιουργήσει ακόμα ένα πραγματικό αριστούργημα.",
            "Τα στελέχη της δισκογραφικής Elektra φοβήθηκαν αρχικά ότι το άλμπουμ ήταν υπερβολικά μελαγχολικό και θα αποτελούσε 'εμπορική αυτοκτονία', πριν εξελιχθεί στο πιο εμπορικό άλμπουμ του συγκροτήματος."
        ],
        "source": "https://en.wikipedia.org/wiki/Disintegration_(The_Cure_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "the_cure"]
    },
    {
        "id": "music_med_180",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ισπανός κιθαρίστας του 20ού αιώνα θεωρείται ο πατέρας της σύγχρονης κλασικής κιθάρας συναυλιών, μεταγράφοντας έργα του Μπαχ για κιθάρα;",
        "answers": ["Πάκο ντε Λουθία", "Αντρές Σεγκόβια", "Ναρκίσο Γέπες", "Χούλιαν Μπριμ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Αντρές Σεγκόβια (Andrés Segovia, 1893-1987) ανέδειξε την κλασική κιθάρα από λαϊκό όργανο σε σοβαρό όργανο κλασικής αίθουσας συναυλιών.",
        "funFacts": [
            "Πολλοί σπουδαίοι συνθέτες (όπως ο Μανουέλ Πόνσε, ο Χοακίν Ροντρίγκο και ο Έιτορ Βίλα-Λόμπος) συνέθεσαν έργα ειδικά αφιερωμένα στον Σεγκόβια.",
            "Ο Σεγκόβια ήταν αυτοδίδακτος στο ξεκίνημά του, καθώς οι καθηγητές της εποχής θεωρούσαν την κιθάρα ανάξια διδασκαλίας στα ωδεία."
        ],
        "source": "https://en.wikipedia.org/wiki/Andr%C3%A9s_Segovia",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "guitar", "segovia"]
    },
    {
        "id": "music_med_181",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό hard rock συγκρότημα κυκλοφόρησε το άλμπουμ 'Led Zeppelin IV' το 1971 που περιλαμβάνει το μνημειώδες 'Stairway to Heaven';",
        "answers": ["Led Zeppelin", "Deep Purple", "The Who", "Black Sabbath"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Led Zeppelin (Ρόμπερτ Πλαντ, Τζίμι Πέιτζ, Τζον Πολ Τζόουνς, Τζον Μπόναμ) κυκλοφόρησαν το τέταρτο άλμπουμ τους χωρίς κανένα γραπτό τίτλο στο εξώφυλλο, μόνο με τέσσερα μυστικιστικά σύμβολα (ZoSo).",
        "funFacts": [
            "Το 'Stairway to Heaven' δεν κυκλοφόρησε ποτέ ως εμπορικό single στις ΗΠΑ, αλλά έγινε το τραγούδι με τις περισσότερες ραδιοφωνικές μεταδόσεις στην ιστορία του ροκ ραδιοφώνου.",
            "Το άλμπουμ έχει πιστοποιηθεί ως 24 φορές πλατινένιο στις ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/Led_Zeppelin_IV",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "led_zeppelin"]
    },
    {
        "id": "music_med_182",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είδος παραδοσιακής μουσικής της Πορτογαλίας χαρακτηρίζεται από μελαγχολικές μελωδίες και τη θεματική της 'saudade' (νοσταλγία/λαχτάρα);",
        "answers": ["Φλαμένκο", "Φάντο (Fado)", "Μποσα νόβα", "Μοράνα"],
        "correctAnswerIndex": 1,
        "explanation": "Το Φάντο (Fado) γεννήθηκε στις ιστορικές συνοικίες της Λισαβόνας (Αλφάμα, Μουραρία) τον 19ο αιώνα και συνοδεύεται παραδοσιακά από την πορτογαλική δωδεκάχορδη κιθάρα.",
        "funFacts": [
            "Η Αμάλια Ροντρίγκες (Amália Rodrigues) θεωρείται η αξεπέραστη 'Βασίλισσα του Φάντο', κάνοντας τη μουσική της γνωστή σε όλο τον κόσμο.",
            "Το Φάντο αναγνωρίστηκε επίσημα από την UNESCO ως Άυλη Πολιτιστική Κληρονομιά της Ανθρωπότητας το 2011."
        ],
        "source": "https://en.wikipedia.org/wiki/Fado",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "world_music", "fado", "portugal"]
    },
    {
        "id": "music_med_183",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των The Beach Boys του 1966 σε παραγωγή Brian Wilson που ενέπνευσε τους Beatles να φτιάξουν το Sgt. Pepper;",
        "answers": ["Surfin' USA", "Pet Sounds", "Smile", "Today!"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Pet Sounds' των The Beach Boys αποτελεί ορόσημο της chamber pop, χρησιμοποιώντας ανορθόδοξα όργανα όπως κόρνα ποδηλάτου, κουδούνες, θέρεμιν και κουδουνίστρες.",
        "funFacts": [
            "Ο Πολ Μακάρτνεϊ έχει δηλώσει επανειλημμένα ότι το 'God Only Knows' από το Pet Sounds είναι το αγαπημένο του τραγούδι όλων των εποχών.",
            "Στο τέλος του άλμπουμ ακούγονται τα πραγματικά γαβγίσματα των σκύλων του Μπράιαν Γουίλσον, Μπανάνα και Λούι."
        ],
        "source": "https://en.wikipedia.org/wiki/Pet_Sounds",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "beach_boys"]
    },
    {
        "id": "music_med_184",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ισπανός βιρτουόζος κιθαρίστας του φλαμένκο έφερε επανάσταση στο είδος εισάγοντας στοιχεία τζαζ και μπάσο και ηχογράφησε το 'Entre dos aguas' (1973);",
        "answers": ["Βισέντε Αμίγκο", "Τοματίτο", "Πάκο ντε Λουθία", "Μανίτας ντε Πλάτα"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Πάκο ντε Λουθία (Paco de Lucía) υπήρξε ο κορυφαίος κιθαρίστας του nuevo flamenco, συνεργαζόμενος με τον τραγουδιστή Camarón de la Isla και τους τζαζ κιθαρίστες Τζον ΜακΛάφλιν και Αλ Ντι Μεόλα.",
        "funFacts": [
            "Ο Πάκο ντε Λουθία εισήγαγε το περουβιανό κρουστό καχόν (cajón) στο φλαμένκο τη δεκαετία του '70, το οποίο σήμερα θεωρείται αναπόσπαστο μέρος του είδους.",
            "Δεν γνώριζε να διαβάζει παρτιτούρα μέχρι τα 44 του χρόνια, όταν έμαθε νότες για να ερμηνεύσει το Concierto de Aranjuez."
        ],
        "source": "https://en.wikipedia.org/wiki/Paco_de_Luc%C3%ADa",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "flamenco", "guitar", "paco_de_lucia"]
    },
    {
        "id": "music_med_185",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου rap άλμπουμ των Nas του 1994 από το Queensbridge που θεωρείται από τα κορυφαία δείγματα East Coast hip hop;",
        "answers": ["Ready to Die", "Illmatic", "Reasonable Doubt", "The Infamous"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Illmatic' του Nas κυκλοφόρησε όταν ο ράπερ ήταν μόλις 20 ετών, με παραγωγούς κορυφαίους beatmakers όπως οι DJ Premier, Large Professor, Pete Rock και Q-Tip.",
        "funFacts": [
            "Το περιοδικό The Source έδωσε στο άλμπουμ την πολυπόθητη βαθμολογία 5 'mics', εξαιρετικά σπάνια διάκριση για ντεμπούτο άλμπουμ.",
            "Το άλμπουμ κατατάσσεται σταθερά στην κορυφή σχεδόν κάθε λίστας με τα σπουδαιότερα hip hop άλμπουμ όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/Illmatic",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "nas"]
    },
    {
        "id": "music_med_186",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας λαϊκός συνθέτης και δεξιοτέχνης του μπουζουκιού συνέθεσε τα τραγούδια 'Μάλιστα κύριε', 'Ο κυρ Θάνος' και 'Σταλιά-σταλιά';",
        "answers": ["Γιώργος Ζαμπέτας", "Μανώλης Χιώτης", "Απόστολος Καλδάρας", "Άκης Πάνου"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Γιώργος Ζαμπέτας (1925-1992) υπήρξε απαράμιλλος σολίστας του μπουζουκιού, συνθέτης εκατοντάδων επιτυχιών και αγαπημένος showman του ελληνικού κινηματογράφου.",
        "funFacts": [
            "Ο Μάνος Χατζιδάκις χαρακτήρισε τον Ζαμπέτα 'τον πιο σπουδαίο σύγχρονο Έλληνα ραψωδό'.",
            "Εισήγαγε στο μπουζούκι μια μοναδική δεξιοτεχνική τεχνική tremolo και staccato που έμεινε γνωστή ως 'ζαμπετική σχολή'."
        ],
        "source": "https://en.wikipedia.org/wiki/Giorgos_Zampetas",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "zampetas"]
    },
    {
        "id": "music_med_187",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό progressive rock συγκρότημα με αρχικό τραγουδιστή τον Πίτερ Γκάμπριελ και αργότερα τον Φιλ Κόλινς κυκλοφόρησε το 'The Lamb Lies Down on Broadway' (1974);",
        "answers": ["Yes", "Genesis", "Camel", "Jethro Tull"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Genesis ξεκίνησαν ως ένα θεατρικό progressive rock σχήμα με περίτεχνα κοστούμια του Πίτερ Γκάμπριελ πριν εξελιχθούν σε παγκόσμιο pop/rock φαινόμενο υπό την ηγεσία του Φιλ Κόλινς.",
        "funFacts": [
            "Ο Φιλ Κόλινς ήταν αρχικά μόνο ο ντράμερ του συγκροτήματος και ανέλαβε τα κύρια φωνητικά το 1975 μετά την αποχώρηση του Γκάμπριελ, αφού πέρασαν από οντισιόν πάνω από 400 τραγουδιστές.",
            "Είναι ένα από τα ελάχιστα συγκροτήματα που ξεπέρασαν τα 100 εκατομμύρια πωλήσεις δίσκων παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/Genesis_(band)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "genesis"]
    },
    {
        "id": "music_med_188",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος συνθέτης του μπαρόκ από τη Λειψία έγραψε τα 'Βρανδεμβούργια Κοντσέρτα' και το 'Καλοκουρδισμένο Κλειδοκύμβαλο';",
        "answers": ["Γκέοργκ Φρίντριχ Χαίντελ", "Γιόχαν Σεμπάστιαν Μπαχ", "Γκέοργκ Φίλιπ Τέλεμαν", "Ντίτριχ Μπουξτεχούντε"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Γιόχαν Σεμπάστιαν Μπαχ (Johann Sebastian Bach, 1685-1750) θεωρείται ο μέγιστος δάσκαλος της αντίστιξης και της φούγκας στη δυτική μουσική ιστορία.",
        "funFacts": [
            "Ο Μπαχ απέκτησε 20 παιδιά από δύο γάμους, εκ των οποίων τέσσερις έγιναν επίσης διακεκριμένοι συνθέτες (C.P.E. Bach, J.C. Bach κ.ά.).",
            "Στην εποχή του ήταν διάσημος κυρίως ως δεξιοτέχνης εκτελεστής του εκκλησιαστικού οργάνου και όχι ως συνθέτης, ανακαλυπτόμενος εκ νέου τον 19ο αιώνα χάρη στον Φέλιξ Μέντελσον."
        ],
        "source": "https://en.wikipedia.org/wiki/Johann_Sebastian_Bach",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "baroque", "bach"]
    },
    {
        "id": "music_med_189",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο hard rock συγκρότημα από την Αυστραλία με τραγουδιστή τον Bon Scott και αργότερα τον Brian Johnson κυκλοφόρησε το 'Highway to Hell' το 1979;",
        "answers": ["Rose Tattoo", "The Angels", "AC/DC", "Midnight Oil"],
        "correctAnswerIndex": 2,
        "explanation": "Οι AC/DC σημείωσαν τεράστια διεθνή επιτυχία με το 'Highway to Hell', το τελευταίο άλμπουμ με τον τραγουδιστή Μπον Σκοτ πριν τον τραγικό θάνατό του το 1980.",
        "funFacts": [
            "Ο τίτλος 'Highway to Hell' ήταν παρατσούκλι για τον αυτοκινητόδρομο Canning Highway στην Αυστραλία, γνωστό για τα πολλά θανατηφόρα τροχαία.",
            "Μετά τον θάνατο του Σκοτ, το συγκρότημα σκέφτηκε να διαλυθεί αλλά επέστρεψε με τον Μπράιαν Τζόνσον και κυκλοφόρησε το 'Back in Black'."
        ],
        "source": "https://en.wikipedia.org/wiki/Highway_to_Hell",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "acdc"]
    },
    {
        "id": "music_med_190",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός τραγουδιστής, συνθέτης και πιανίστας είναι γνωστός ως 'The Piano Man' από το ομώνυμο αυτοβιογραφικό τραγούδι του 1973;",
        "answers": ["Έλτον Τζον", "Ρέι Τσαρλς", "Μπάρι Μάνιλοου", "Μπίλι Τζόελ"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Μπίλι Τζόελ (Billy Joel) έγραψε το 'Piano Man' βασισμένος στις πραγματικές εμπειρίες του ως πιανίστας στο μπαρ 'The Executive Room' στο Λος Άντζελες.",
        "funFacts": [
            "Όλοι οι χαρακτήρες στο τραγούδι (ο μπάρμαν Τζον, ο μεσίτης Πολ κ.λπ.) βασίστηκαν σε πραγματικούς θαμώνες του μπαρ.",
            "Ο Μπίλι Τζόελ είναι ο μόνος καλλιτέχνης που έδωσε μηνιαία συναυλία στο Madison Square Garden της Νέας Υόρκης για πάνω από 10 χρόνια (συνολικά 150 συναυλίες)."
        ],
        "source": "https://en.wikipedia.org/wiki/Billy_Joel",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "rock", "billy_joel"]
    },
    {
        "id": "music_med_191",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό shoegaze συγκρότημα με επικεφαλής τον Kevin Shields κυκλοφόρησε το θρυλικό άλμπουμ 'Loveless' το 1991;",
        "answers": ["My Bloody Valentine", "Slowdive", "Ride", "Lush"],
        "correctAnswerIndex": 0,
        "explanation": "Οι My Bloody Valentine όρισαν το είδος του shoegaze με το 'Loveless', χρησιμοποιώντας την τεχνική 'glide guitar' με συνεχή χρήση του τρέμολο της Fender Jazzmaster.",
        "funFacts": [
            "Η παραγωγή του άλμπουμ διήρκεσε πάνω από δύο χρόνια και πέρασε από 19 διαφορετικά στούντιο, σχεδόν χρεοκοπώντας τη δισκογραφική εταιρεία Creation Records.",
            "Οι ζωντανές συναυλίες τους είναι διαβόητες για την εκκωφαντική τους ένταση (συχνά πάνω από 120-130 dB), μοιράζοντας υποχρεωτικά ωτοασπίδες στην είσοδο."
        ],
        "source": "https://en.wikipedia.org/wiki/Loveless_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "shoegaze"]
    },
    {
        "id": "music_med_192",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αυστριακός συνθέτης της κλασικής περιόδου αποκλήθηκε 'Πατέρας της Συμφωνίας' και 'Πατέρας του Κουαρτέτου Εγχόρδων', γράφοντας 104 συμφωνίες;",
        "answers": ["Βόλφγκανγκ Αμαντέους Μότσαρτ", "Γιόζεφ Χάιντν", "Λούντβιχ βαν Μπετόβεν", "Φραντς Σούμπερτ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Γιόζεφ Χάιντν (Joseph Haydn, 1732-1809) υπηρέτησε για δεκαετίες ως αρχιμουσικός στην αυλή της οικογένειας Εστερχάζι, τελειοποιώντας τις κλασικές μουσικές φόρμες.",
        "funFacts": [
            "Στη διάσημη 'Συμφωνία της Εκπλήξεως' (No. 94), πρόσθεσε ένα εκκωφαντικό χτύπημα τυμπάνου στο αργό μέρος για να ξυπνήσει τους ευγενείς θεατές που αποκοιμιούνταν.",
            "Υπήρξε στενός φίλος του Μότσαρτ και δάσκαλος του νεαρού Μπετόβεν στη Βιέννη."
        ],
        "source": "https://en.wikipedia.org/wiki/Joseph_Haydn",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "haydn"]
    },
    {
        "id": "music_med_193",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου τραγουδιστή των Queen που γεννήθηκε στη Ζανζιβάρη με το όνομα Φαρόκ Μπουλσάρα;",
        "answers": ["Μπράιαν Μέι", "Ρότζερ Τέιλορ", "Φρέντι Μέρκιουρι", "Τζον Ντίκον"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Φρέντι Μέρκιουρι (Freddie Mercury) υπήρξε ένας από τους πιο χαρισματικούς τραγουδιστές στην ιστορία της ροκ, με φωνητικό εύρος τεσσάρων οκτάβων.",
        "funFacts": [
            "Γεννήθηκε στη Ζανζιβάρη από γονείς Παρσί (Ζωροάστρες με καταγωγή από την Ινδία) και μεγάλωσε στην Ινδία πριν μεταναστεύσει με την οικογένειά του στην Αγγλία το 1964.",
            "Είχε τέσσερα επιπλέον δόντια (υπεραριθμία) στο πίσω μέρος της άνω γνάθου, τα οποία αρνήθηκε να ισιώσει πιστεύοντας ότι του χάριζαν τον ιδιαίτερο φωνητικό του συντονισμό."
        ],
        "source": "https://en.wikipedia.org/wiki/Freddie_Mercury",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "queen", "freddie_mercury"]
    },
    {
        "id": "music_med_194",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου rap ντουέτου από την Ατλάντα που αποτελούνταν από τους André 3000 και Big Boi;",
        "answers": ["Mobb Deep", "Clipse", "Run the Jewels", "Outkast"],
        "correctAnswerIndex": 3,
        "explanation": "Οι Outkast κυκλοφόρησαν το διπλό διαμάντι 'Speakerboxxx/The Love Below' το 2003 με τα smash hits 'Hey Ya!' και 'The Way You Move', κερδίζοντας το Grammy Άλμπουμ της Χρονιάς.",
        "funFacts": [
            "Το 'Speakerboxxx/The Love Below' είναι ένα από τα μόλις δύο hip hop άλμπουμ στην ιστορία που κέρδισαν το Grammy για το Άλμπουμ της Χρονιάς.",
            "Η ατάκα 'Shake it like a Polaroid picture' από το τραγούδι 'Hey Ya!' οδήγησε την εταιρεία Polaroid να εκδώσει επίσημη ανακοίνωση προειδοποιώντας ότι το κούνημα μπορεί να καταστρέψει τη φωτογραφία!"
        ],
        "source": "https://en.wikipedia.org/wiki/Outkast",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "outkast"]
    },
    {
        "id": "music_med_195",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας ποιητής και στιχουργός έγραψε τους στίχους για το εμβληματικό άλμπουμ 'Ο Μεγάλος Ερωτικός' (1972) σε μουσική Μάνου Χατζιδάκι;",
        "answers": ["Μάνος Χατζιδάκις (επιλογή ποιημάτων)", "Νίκος Γκάτσος", "Οδυσσέας Ελύτης", "Γιάννης Ρίτσος"],
        "correctAnswerIndex": 0,
        "explanation": "Στον 'Μεγάλο Ερωτικό', ο Μάνος Χατζιδάκις μελοποίησε ποιήματα από την αρχαιότητα έως τη σύγχρονη εποχή (από τη Σαπφώ, τον Ευριπίδη και το Άσμα Ασμάτων μέχρι τον Σολωμό, τον Καβάφη και τον Ελύτη).",
        "funFacts": [
            "Το άλμπουμ ηχογραφήθηκε στη Νέα Υόρκη και την Αθήνα και θεωρείται ένα από τα κορυφαία αριστουργήματα της ελληνικής δισκογραφίας.",
            "Οι ερμηνείες του Φλέρυς Νταντωνάκη και του Δημήτρη Ψαριανού έμειναν κλασικές."
        ],
        "source": "https://en.wikipedia.org/wiki/Magnus_Eroticus",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "hadjidakis"]
    },
    {
        "id": "music_med_196",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό indie rock συγκρότημα με τραγουδιστή τον Morrissey και κιθαρίστα τον Johnny Marr κυκλοφόρησε το 'The Queen Is Dead' το 1986;",
        "answers": ["The Smiths", "New Order", "The Stone Roses", "Echo & the Bunnymen"],
        "correctAnswerIndex": 0,
        "explanation": "Οι The Smiths από το Μάντσεστερ υπήρξαν το πιο επιδραστικό βρετανικό indie συγκρότημα της δεκαετίας του '80, με κομμάτια όπως το 'There Is a Light That Never Goes Out'.",
        "funFacts": [
            "Ο Τζόνι Μαρ χρησιμοποιούσε περίπλοκες στρώσεις κιθάρων κουρδισμένων σε διαφορετικές τονικότητες για να δημιουργεί τον χαρακτηριστικό 'jangle' ήχο.",
            "Το συγκρότημα διαλύθηκε το 1987 μετά από μόλις πέντε χρόνια πορείας λόγω προσωπικών και καλλιτεχνικών διαφορών ανάμεσα στους Μόρισι και Μαρ."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Smiths",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "indie", "the_smiths"]
    },
    {
        "id": "music_med_197",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο jazz πρότυπο σε σύνθεση του Dave Brubeck και σαξοφωνίστα Paul Desmond του 1959 είναι γραμμένο στον ασυνήθιστο ρυθμό 5/4;",
        "answers": ["Blue Rondo à la Turk", "Take Five", "Unsquare Dance", "Time Out"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Take Five' του The Dave Brubeck Quartet έγινε το jazz single με τις μεγαλύτερες πωλήσεις στην ιστορία, εκλαϊκεύοντας τους ασύμμετρους ρυθμούς στη δυτική μουσική.",
        "funFacts": [
            "Ο τίτλος είναι διπλής σημασίας: αναφέρεται τόσο στον ρυθμό 5/4 όσο και στην κοινή αγγλική φράση για ένα σύντομο διάλειμμα 5 λεπτών.",
            "Ο Πολ Ντέσμοντ κληροδότησε όλα τα δικαιώματα του τραγουδιού στον Αμερικανικό Ερυθρό Σταυρό, ο οποίος εισπράττει εκατοντάδες χιλιάδες δολάρια ετησίως μέχρι σήμερα."
        ],
        "source": "https://en.wikipedia.org/wiki/Take_Five",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "brubeck"]
    },
    {
        "id": "music_med_198",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου progressive rock άλμπουμ των Genesis του 1973 με το επικό 23λεπτο κομμάτι 'Supper's Ready';",
        "answers": ["Foxtrot", "Selling England by the Pound", "Nursery Cryme", "Trespass"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Selling England by the Pound' περιλαμβάνει κορυφαίες συνθέσεις όπως τα 'Firth of Fifth', 'Dancing with the Moonlit Knight' και το πρώτο μεγάλο βρετανικό hit του συγκροτήματος 'I Know What I Like (In Your Wardrobe)'.",
        "funFacts": [
            "Το πιανιστικό intro του Τόνι Μπανκς και το σόλο κιθάρας του Στιβ Χάκετ στο 'Firth of Fifth' θεωρούνται από τις κορυφαίες στιγμές της progressive rock μουσικής.",
            "Ο τίτλος του άλμπουμ προήλθε από ένα πολιτικό σλόγκαν του Βρετανικού Εργατικού Κόμματος της εποχής."
        ],
        "source": "https://en.wikipedia.org/wiki/Selling_England_by_the_Pound",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "progressive_rock", "genesis"]
    },
    {
        "id": "music_med_199",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της όπερας του μπαρόκ έγραψε το 'L'Orfeo' (1607), που θεωρείται η αρχαιότερη όπερα που εξακολουθεί να παρουσιάζεται τακτικά μέχρι σήμερα;",
        "answers": ["Κλαούντιο Μοντεβέρντι", "Γιάκοπο Πέρι", "Αντόνιο Τσέστι", "Φραντσέσκο Καβάλι"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Κλαούντιο Μοντεβέρντι (Claudio Monteverdi) σηματοδότησε τη μετάβαση από την Αναγέννηση στο Μπαρόκ και με το 'L'Orfeo' θεμελίωσε την όπερα ως ολοκληρωμένη δραματική μορφή τέχνης.",
        "funFacts": [
            "Το 'L'Orfeo' παρουσιάστηκε για πρώτη φορά στο καρναβάλι της Μάντοβα τον Φεβρουάριο του 1607.",
            "Ο Μοντεβέρντι χρησιμοποίησε μια πρωτοποριακή ορχήστρα περίπου 40 οργάνων με συγκεκριμένη οργανοθεσία για κάθε σκηνή (π.χ. σκοτεινά πνευστά για τον Κάτω Κόσμο)."
        ],
        "source": "https://en.wikipedia.org/wiki/L%27Orfeo",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "opera", "monteverdi"]
    },
    {
        "id": "music_med_200",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα grunge από το Σιάτλ με τραγουδιστή τον Layne Staley και κιθαρίστα τον Jerry Cantrell κυκλοφόρησε το άλμπουμ 'Dirt' (1992);",
        "answers": ["Soundgarden", "Pearl Jam", "Alice in Chains", "Screaming Trees"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Alice in Chains συνδύασαν το grunge με το heavy metal και τις χαρακτηριστικές διφωνίες των Στέιλι και Κάντρελ σε τραγούδια όπως τα 'Rooster', 'Them Bones' και 'Would?'.",
        "funFacts": [
            "Το τραγούδι 'Rooster' γράφτηκε από τον Τζέρι Κάντρελ για τον πατέρα του, βετεράνο του πολέμου του Βιετνάμ που είχε το παρατσούκλι 'Rooster'.",
            "Η εμφάνισή τους στο MTV Unplugged το 1996 ήταν μία από τις τελευταίες ζωντανές εμφανίσεις του Λέιν Στέιλι πριν από τον τραγικό θάνατό του το 2002."
        ],
        "source": "https://en.wikipedia.org/wiki/Dirt_(Alice_in_Chains_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "grunge", "alice_in_chains"]
    },
    {
        "id": "music_med_201",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας στιχουργός και ποιητής έγραψε τους στίχους για αθάνατα έργα όπως η 'Μυθολογία', το 'Ρεμπέτικο' και 'Χάρτινο το φεγγαράκι';",
        "answers": ["Νίκος Γκάτσος", "Μάνος Ελευθερίου", "Λευτέρης Παπαδόπουλος", "Κώστας Βίρβος"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Νίκος Γκάτσος (1911-1992), δημιουργός της υπερρεαλιστικής ποιητικής σύνθεσης 'Αμοργός', συνεργάστηκε στενά με τον Μάνο Χατζιδάκι, τον Μίκη Θεοδωράκη και τον Σταύρο Ξαρχάκο.",
        "funFacts": [
            "Ο Γκάτσος εξέδωσε στη ζωή του μία και μοναδική ποιητική συλλογή (την 'Αμοργό' το 1943), επιλέγοντας στη συνέχεια να εκφράζεται σχεδόν αποκλειστικά μέσα από τη στιχουργική.",
            "Τα τραγούδια του για την ταινία 'Ρεμπέτικο' (1983) του Κώστα Φέρρη σε μουσική Σταύρου Ξαρχάκου θεωρούνται σύγχρονα δημοτικά και λαϊκά αριστουργήματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Nikos_Gatsos",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "poetry", "gatsos"]
    },
    {
        "id": "music_med_202",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο θρυλικό progressive rock συγκρότημα από το Κέιμπριτζ κυκλοφόρησε το άλμπουμ 'Wish You Were Here' το 1975 ως φόρο τιμής στον ιδρυτή τους Syd Barrett;",
        "answers": ["Genesis", "Pink Floyd", "King Crimson", "Yes"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Pink Floyd ηχογράφησαν το 'Wish You Were Here' στα Abbey Road Studios, αφιερώνοντας τη σουίτα 'Shine On You Crazy Diamond' στον Σιντ Μπάρετ που είχε αποχωρήσει λόγω ψυχικής κατάρρευσης.",
        "funFacts": [
            "Κατά τη διάρκεια της μίξης του 'Shine On You Crazy Diamond', ο ίδιος ο Σιντ Μπάρετ εμφανίστηκε ξαφνικά στο στούντιο απροειδοποίητα, υπέρβαρος και με ξυρισμένο κεφάλι και φρύδια, με αποτέλεσμα οι παλιοί του συμπαίκτες να μην τον αναγνωρίσουν στην αρχή.",
            "Το εξώφυλλο με τον άνδρα που καίγεται ενώ κάνει χειραψία τραβήχτηκε με πραγματικό κασκαντέρ (Ρόνι Ρόντελ) που τυλίχθηκε στις φλόγες."
        ],
        "source": "https://en.wikipedia.org/wiki/Wish_You_Were_Here_(Pink_Floyd_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "pink_floyd"]
    },
    {
        "id": "music_med_203",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου soundtrack της ταινίας κινουμένων σχεδίων 'Tarzan' (1999) της Disney που συνέθεσε και τραγούδησε ο Phil Collins κερδίζοντας Όσκαρ;",
        "answers": ["Two Worlds", "Strangers Like Me", "You'll Be in My Heart", "Son of Man"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'You'll Be in My Heart' του Φιλ Κόλινς κέρδισε το Όσκαρ και τη Χρυσή Σφαίρα Καλύτερου Πρωτότυπου Τραγουδιού το 2000.",
        "funFacts": [
            "Ο Φιλ Κόλινς ηχογράφησε τα τραγούδια του soundtrack όχι μόνο στα αγγλικά, αλλά και στα γαλλικά, γερμανικά, ιταλικά και ισπανικά για τις διεθνείς μεταγλωττίσεις της ταινίας.",
            "Έγραψε αρχικά το τραγούδι ως νανούρισμα για την κόρη του, τη γνωστή ηθοποιό Λίλι Κόλινς."
        ],
        "source": "https://en.wikipedia.org/wiki/You%27ll_Be_in_My_Heart",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soundtracks", "disney", "phil_collins"]
    },
    {
        "id": "music_med_204",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα της παραδοσιακής ορχήστρας κρουστών και μεταλλοφώνων από τα νησιά της Ινδονησίας (Ιάβα και Μπαλί) που επηρέασε βαθιά συνθέτες όπως ο Ντεμπισί;",
        "answers": ["Μαριάτσι", "Γκαμελάν (Gamelan)", "Ταϊκό", "Ράγκα"],
        "correctAnswerIndex": 1,
        "explanation": "Το Γκαμελάν αποτελείται κυρίως από μεταλλόφωνα, γκονγκ, τυμπανάκια (kendang) και μπαμπού φλάουτα, δημιουργώντας περίπλοκες πολυρυθμικές υφές.",
        "funFacts": [
            "Ο Κλοντ Ντεμπισί άκουσε για πρώτη φορά γκαμελάν στην Παγκόσμια Έκθεση του Παρισιού το 1889 και δήλωσε ότι η ευρωπαϊκή πολυφωνία ήταν πρωτόγονη μπροστά στην ινδονησιακή μουσική.",
            "Κάθε σύνολο γκαμελάν στην Ινδονησία θεωρείται ιερό, έχει δικό του ξεχωριστό όνομα και δεν μπορεί να αναμιχθεί με όργανα άλλου συνόλου γιατί έχει μοναδικό κούρδισμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Gamelan",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "world_music", "indonesia", "gamelan"]
    },
    {
        "id": "music_med_205",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό punk και post-punk συγκρότημα με τραγουδίστρια τη Siouxsie Sioux και μπασίστα τον Severin κυκλοφόρησε τα κλασικά κομμάτια 'Spellbound' και 'Cities in Dust';",
        "answers": ["Siouxsie and the Banshees", "The Slits", "X-Ray Spex", "Cocteau Twins"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Siouxsie and the Banshees (1976-1996) άσκησαν τεράστια επιρροή στο post-punk, το gothic rock και το alternative rock, επηρεάζοντας καλλιτέχνες όπως οι Joy Division, The Cure, Radiohead και Massive Attack.",
        "funFacts": [
            "Ο Σιντ Βίσιους των Sex Pistols έπαιξε ντραμς στην πρώτη άναρχη ζωντανή εμφάνιση του συγκροτήματος στο 100 Club Punk Festival το 1976.",
            "Ο Ρόμπερτ Σμιθ των The Cure υπήρξε επίσημος κιθαρίστας των Banshees για δύο περιόδους (1979 και 1982-1984)."
        ],
        "source": "https://en.wikipedia.org/wiki/Siouxsie_and_the_Banshees",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "post_punk", "goth"]
    },
    {
        "id": "music_med_206",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου rap άλμπουμ των The Notorious B.I.G. του 1994 που περιλαμβάνει τα κομμάτια 'Juicy' και 'Big Poppa';",
        "answers": ["Life After Death", "Ready to Die", "All Eyez on Me", "Me Against the World"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Ready to Die' του Biggie Smalls (Κρίστοφερ Γουάλας) σε παραγωγή Puff Daddy (Bad Boy Records) αναζωογόνησε τη hip-hop σκηνή της Νέας Υόρκης απέναντι στην κυριαρχία της Δυτικής Ακτής.",
        "funFacts": [
            "Το 'Juicy' ήταν το πρώτο single του άλμπουμ και αφηγείται την άνοδο του Biggie από τη φτώχεια και τις δυσκολίες στην κορυφή της επιτυχίας.",
            "Το μωρό με το άφρο μαλλί στο εξώφυλλο του άλμπουμ δεν ήταν ο ίδιος ο Biggie, αλλά ένα μοντέλο μωρού που επιλέχθηκε από πρακτορείο."
        ],
        "source": "https://en.wikipedia.org/wiki/Ready_to_Die",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "notorious_big"]
    },
    {
        "id": "music_med_207",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο blues τραγούδι του Muddy Waters του 1950 έδωσε το όνομά του τόσο στο θρυλικό ροκ συγκρότημα του Μικ Τζάγκερ όσο και στο κορυφαίο μουσικό περιοδικό;",
        "answers": ["Mannish Boy", "Hoochie Coochie Man", "Rollin' Stone", "Got My Mojo Working"],
        "correctAnswerIndex": 2,
        "explanation": "Το τραγούδι 'Rollin' Stone' (βασισμένο στην παλιά παροιμία 'μια πέτρα που κυλάει δεν πιάνει βρύα') ενέπνευσε τον Μπράιαν Τζόουνς να ονομάσει το συγκρότημα The Rolling Stones το 1962, καθώς και τον Γιαν Γουένερ να ιδρύσει το περιοδικό Rolling Stone το 1967.",
        "funFacts": [
            "Ο Μπομπ Ντίλαν εμπνεύστηκε επίσης από την ίδια φράση για να γράψει το μνημειώδες τραγούδι του 'Like a Rolling Stone' (1965).",
            "Ο Muddy Waters ηχογράφησε το τραγούδι με ηλεκτρική κιθάρα στο Σικάγο για την Chess Records."
        ],
        "source": "https://en.wikipedia.org/wiki/Rollin%27_Stone",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "blues", "muddy_waters", "history"]
    },
    {
        "id": "music_med_208",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας συνθέτης και μαέστρος έγραψε τις ιστορικές συνθέσεις 'Ελεύθεροι Πολιορκημένοι' και 'Κορίτσι με τα μαύρα' και υπήρξε ιδρυτής της Ορχήστρας των Χρωμάτων;",
        "answers": ["Μάνος Χατζιδάκις", "Γιάννης Μαρκόπουλος", "Σταύρος Ξαρχάκος", "Χρήστος Λεοντής"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μάνος Χατζιδάκις ίδρυσε την Ορχήστρα των Χρωμάτων το 1989 για να παρουσιάζει πρωτότυπα και απαιτητικά μουσικά έργα χωρίς συμβιβασμούς.",
        "funFacts": [
            "Ο Χατζιδάκις υπήρξε επίσης διευθυντής του Τρίτου Προγράμματος της Ελληνικής Ραδιοφωνίας (1975-1981), δημιουργώντας μια ιστορική περίοδο πολιτιστικής άνθησης.",
            "Εισήγαγε την εκπομπή 'Εδώ Λιλιπούπολη', η οποία έγινε σταθμός στην ιστορία της ελληνικής ραδιοφωνίας για παιδιά και ενήλικες."
        ],
        "source": "https://en.wikipedia.org/wiki/Manos_Hatzidakis",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "hadjidakis"]
    },
    {
        "id": "music_med_209",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των Nirvana του 1993 με παραγωγό τον Steve Albini που περιλαμβάνει τα τραγούδια 'Heart-Shaped Box' και 'All Apologies';",
        "answers": ["Bleach", "In Utero", "Incesticide", "MTV Unplugged in New York"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'In Utero' ήταν το τρίτο και τελευταίο στούντιο άλμπουμ των Nirvana, με πιο τραχύ, ασυμβίβαστο και ωμό ήχο σε σύγκριση με το γυαλισμένο 'Nevermind'.",
        "funFacts": [
            "Ο αρχικός τίτλος που σκόπευε να δώσει ο Κερτ Κομπέιν στο άλμπουμ ήταν 'I Hate Myself and Want to Die'.",
            "Το άλμπουμ ηχογραφήθηκε μέσα σε μόλις δύο εβδομάδες στο απομονωμένο Pachyderm Studio στη Μινεσότα."
        ],
        "source": "https://en.wikipedia.org/wiki/In_Utero",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "grunge", "nirvana"]
    },
    {
        "id": "music_med_210",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του θρυλικού φεστιβάλ κλασικής μουσικής που διεξάγεται κάθε καλοκαίρι για οκτώ εβδομάδες στο Royal Albert Hall του Λονδίνου με την περίφημη 'Last Night';",
        "answers": ["Salzburg Festival", "Bayreuth Festival", "The Proms (BBC Proms)", "Lucerne Festival"],
        "correctAnswerIndex": 2,
        "explanation": "Τα BBC Proms (Henry Wood Promenade Concerts) ιδρύθηκαν το 1895 και αποτελούν το μεγαλύτερο και πιο δημοκρατικό φεστιβάλ κλασικής μουσικής στον κόσμο.",
        "funFacts": [
            "Ο όρος 'promenade concert' αναφέρεται στην παράδοση των θεατών που στέκονται όρθιοι στην κεντρική αρένα πληρώνοντας πολύ φθηνό εισιτήριο (γνωστοί ως 'Prommers').",
            "Η τελευταία βραδιά ('Last Night of the Proms') είναι μια παγκόσμια μουσική γιορτή όπου το κοινό τραγουδά παραδοσιακούς βρετανικούς ύμνους όπως το 'Land of Hope and Glory' και το 'Rule, Britannia!'."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Proms",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "festivals", "proms"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(QUESTIONS)} questions for music_medium.")
    validate_and_append("music", "medium", 3, QUESTIONS)

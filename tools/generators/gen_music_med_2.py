# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# 50 music medium questions: music_med_061 to music_med_110
QUESTIONS = [
    {
        "id": "music_med_061",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο θρυλικό άλμπουμ των Pink Floyd που κυκλοφόρησε το 1973 περιλαμβάνει τα κομμάτια 'Money' και 'Time';",
        "answers": ["The Dark Side of the Moon", "The Wall", "Wish You Were Here", "Animals"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'The Dark Side of the Moon' των Pink Floyd έμεινε στα αμερικανικά charts του Billboard για πάνω από 900 εβδομάδες (πάνω από 14 χρόνια).",
        "funFacts": [
            "Το εξώφυλλο με το πρίσμα που διαθλά το λευκό φως σχεδιάστηκε από τη διάσημη γραφιστική ομάδα Hipgnosis.",
            "Τα ηχητικά εφέ κερμάτων και ταμειακής μηχανής στο τραγούδι 'Money' ηχογραφήθηκαν από τον Ρότζερ Γουότερς με πραγματικά νομίσματα σε μπολ."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Dark_Side_of_the_Moon",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "pink_floyd"]
    },
    {
        "id": "music_med_062",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης της περιόδου του μπαρόκ συνέθεσε το διάσημο σύνολο κοντσέρτων για βιολί 'Οι Τέσσερις Εποχές';",
        "answers": ["Κλαούντιο Μοντεβέρντι", "Αντόνιο Βιβάλντι", "Τζοακίνο Ροσίνι", "Τζοβάνι Μπατίστα Περγκολέζι"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Αντόνιο Βιβάλντι συνέθεσε τις 'Τέσσερις Εποχές' (Le quattro stagioni) γύρω στο 1720, συνοδεύοντάς τες από περιγραφικά σονέτα.",
        "funFacts": [
            "Ο Βιβάλντι ήταν χειροτονημένος καθολικός ιερέας και ήταν γνωστός ως 'Il Prete Rosso' (Ο Κόκκινος Παπάς) λόγω των κόκκινων μαλλιών του.",
            "Οι Τέσσερις Εποχές είναι ένα από τα πρώτα και πιο χαρακτηριστικά δείγματα προγραμματικής μουσικής στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Four_Seasons_(Vivaldi)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "baroque"]
    },
    {
        "id": "music_med_063",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό ροκ συγκρότημα κυκλοφόρησε τον εμβληματικό ύμνο 'Bohemian Rhapsody' το 1975;",
        "answers": ["The Rolling Stones", "Led Zeppelin", "Queen", "The Who"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Queen και ο Φρέντι Μέρκιουρι δημιούργησαν το 'Bohemian Rhapsody' για το άλμπουμ 'A Night at the Opera', συνδυάζοντας μπαλάντα, οπερατικά μέρη και hard rock.",
        "funFacts": [
            "Η οπερατική ενότητα του τραγουδιού απαίτησε πάνω από 180 ξεχωριστά overdubs φωνητικών σε αναλογική ταινία 24 καναλιών.",
            "Η δισκογραφική εταιρεία EMI θεωρούσε αρχικά ότι τα 5 λεπτά και 55 δευτερόλεπτα ήταν απαγορευτικά μεγάλη διάρκεια για ραδιοφωνικό single."
        ],
        "source": "https://en.wikipedia.org/wiki/Bohemian_Rhapsody",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "queen"]
    },
    {
        "id": "music_med_064",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη jazz τραγουδίστρια ήταν γνωστή με το προσωνύμιο 'Lady Day' και συγκλόνισε με την ερμηνεία της στο τραγούδι 'Strange Fruit';",
        "answers": ["Έλλα Φιτζέραλντ", "Σάρα Βον", "Νίνα Σιμόν", "Μπίλι Χόλιντεϊ"],
        "correctAnswerIndex": 3,
        "explanation": "Η Μπίλι Χόλιντεϊ (Billie Holiday) ηχογράφησε το 'Strange Fruit' το 1939, ένα τραγούδι διαμαρτυρίας κατά του ρατσιστικού λιντσαρίσματος των μαύρων στον αμερικανικό Νότο.",
        "funFacts": [
            "Το προσωνύμιο 'Lady Day' της το έδωσε ο στενός της φίλος και θρυλικός σαξοφωνίστας Λέστερ Γιανγκ.",
            "Το περιοδικό Time ανακήρυξε το 'Strange Fruit' ως το 'Τραγούδι του Αιώνα' το 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Billie_Holiday",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "billie_holiday"]
    },
    {
        "id": "music_med_065",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο μουσικό όργανο έχει 88 πλήκτρα (52 λευκά και 36 μαύρα) στην κλασική του διάταξη;",
        "answers": ["Το πιάνο", "Το εκκλησιαστικό όργανο", "Το τσέμπαλο", "Το ακορντεόν"],
        "correctAnswerIndex": 0,
        "explanation": "Το σύγχρονο ακουστικό πιάνο έχει 88 πλήκτρα, καλύπτοντας περισσότερες από 7 οκτάβες (από το Λα-2 έως το Ντο-7).",
        "funFacts": [
            "Το πιάνο εφευρέθηκε στην Ιταλία γύρω στο 1700 από τον Μπαρτολομέο Κριστοφόρι και ονομαζόταν αρχικά 'gravicembalo col piano e forte' (τσέμπαλο με απαλό και δυνατό ήχο).",
            "Η εταιρεία Bösendorfer κατασκευάζει ένα ειδικό μοντέλο πιάνου με 97 πλήκτρα (Imperial 290) με πρόσθετα μπάσα πλήκτρα."
        ],
        "source": "https://en.wikipedia.org/wiki/Piano",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "instruments", "piano"]
    },
    {
        "id": "music_med_066",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του πρωτοπόρου μουσικού της reggae που τραγούδησε τα 'No Woman, No Cry' και 'Redemption Song';",
        "answers": ["Πίτερ Τος", "Μπομπ Μάρλεϊ", "Τζίμι Κλιφ", "Μπάνι Γουέιλερ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Μπομπ Μάρλεϊ (Bob Marley) υπήρξε ο κορυφαίος πρεσβευτής της τζαμαϊκανής ρέγκε μουσικής και του κινήματος των Ρασταφάρι σε όλο τον κόσμο.",
        "funFacts": [
            "Το άλμπουμ αναδρομής 'Legend' (1984) των Bob Marley and the Wailers είναι το πιο εμπορικό άλμπουμ ρέγκε όλων των εποχών, με πάνω από 28 εκατομμύρια πωλήσεις.",
            "Του απονεμήθηκε το Μετάλλιο Ειρήνης του Τρίτου Κόσμου από τα Ηνωμένα Έθνη το 1978."
        ],
        "source": "https://en.wikipedia.org/wiki/Bob_Marley",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "reggae", "bob_marley"]
    },
    {
        "id": "music_med_067",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος διάσημος συνθέτης έγραψε την 9η Συμφωνία που περιλαμβάνει την 'Ωδή στη Χαρά' ενώ ήταν σχεδόν εντελώς κωφός;",
        "answers": ["Βόλφγκανγκ Αμαντέους Μότσαρτ", "Φραντς Σούμπερτ", "Λούντβιχ βαν Μπετόβεν", "Γιοχάνες Μπραμς"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Μπετόβεν ολοκλήρωσε την 9η Συμφωνία το 1824 όντας σχεδόν πλήρως κωφός, μελοποιώντας το ποίημα του Φρίντριχ Σίλερ 'Ωδή στη Χαρά'.",
        "funFacts": [
            "Στην πρεμιέρα στη Βιέννη, η υψίφωνος Καρολίνε Ούνγκερ χρειάστηκε να στρέψει τον Μπετόβεν προς το κοινό για να δει το κοινό να χειροκροτεί όρθιο.",
            "Η 'Ωδή στη Χαρά' υιοθετήθηκε το 1972 ως ο επίσημος ύμνος της Ευρωπαϊκής Ένωσης."
        ],
        "source": "https://en.wikipedia.org/wiki/Symphony_No._9_(Beethoven)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "beethoven"]
    },
    {
        "id": "music_med_068",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη Σουηδέζα ποπ τετράδα κέρδισε τη Eurovision το 1974 με το τραγούδι 'Waterloo';",
        "answers": ["Roxette", "Ace of Base", "The Cardigans", "ABBA"],
        "correctAnswerIndex": 3,
        "explanation": "Οι ABBA (Agnetha, Björn, Benny, Anni-Frid) κέρδισαν τον Διαγωνισμό Τραγουδιού της Eurovision στο Μπράιτον, ξεκινώντας μια μυθική παγκόσμια καριέρα.",
        "funFacts": [
            "Το όνομα ABBA είναι ακρωνύμιο των πρώτων γραμμάτων των ονομάτων των τεσσάρων μελών του συγκροτήματος.",
            "Το μιούζικαλ 'Mamma Mia!', βασισμένο στα τραγούδια τους, έχει παιχτεί σε περισσότερες από 50 χώρες από πάνω από 65 εκατομμύρια θεατές."
        ],
        "source": "https://en.wikipedia.org/wiki/ABBA",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "abba", "eurovision"]
    },
    {
        "id": "music_med_069",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος τρομπετίστας της jazz κυκλοφόρησε το 1959 το ιστορικό άλμπουμ 'Kind of Blue';",
        "answers": ["Μάιλς Ντέιβις", "Ντίζι Γκιλέσπι", "Λούις Άρμστρονγκ", "Τσετ Μπέικερ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μάιλς Ντέιβις (Miles Davis) δημιούργησε το 'Kind of Blue' με μια εξαμελή σύνθεση που περιλάμβανε τον Τζον Κολτρέιν και τον Μπιλ Έβανς, καθιερώνοντας τη modal jazz.",
        "funFacts": [
            "Το 'Kind of Blue' θεωρείται από πολλούς κριτικούς ως το σπουδαιότερο και πιο επιδραστικό jazz άλμπουμ όλων των εποχών.",
            "Οι ηχογραφήσεις πραγματοποιήθηκαν σε μόλις δύο συνεδρίες χωρίς σχεδόν καθόλου πρόβες, βασισμένες σε απλά προσχέδια κλιμάκων που μοίρασε ο Ντέιβις."
        ],
        "source": "https://en.wikipedia.org/wiki/Kind_of_Blue",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "miles_davis"]
    },
    {
        "id": "music_med_070",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα hard rock από την Αυστραλία έγινε παγκόσμιος θρύλος με κιθαρίστα τον Άνγκους Γιανγκ με σχολική στολή;",
        "answers": ["INXS", "AC/DC", "Airbourne", "Midnight Oil"],
        "correctAnswerIndex": 1,
        "explanation": "Οι AC/DC ιδρύθηκαν στο Σίδνεϊ το 1973 από τα αδέλφια Μάλκολμ και Άνγκους Γιανγκ, κυκλοφορώντας κλασικά άλμπουμ όπως το 'Back in Black'.",
        "funFacts": [
            "Το άλμπουμ 'Back in Black' (1980) είναι το δεύτερο άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία της μουσικής (μετά το Thriller), με πάνω από 50 εκατομμύρια αντίτυπα.",
            "Η αδελφή του Άνγκους, η Μάργκαρετ, ήταν εκείνη που πρότεινε να φοράει τη σχολική του στολή επί σκηνής."
        ],
        "source": "https://en.wikipedia.org/wiki/AC/DC",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "acdc"]
    },
    {
        "id": "music_med_071",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο έγχορδο όργανο με δοξάρι παίζεται ανάμεσα στα πόδια του καθιστού μουσικού και έχει βαθύτερο ήχο από τη βιόλα αλλά υψηλότερο από το κοντραμπάσο;",
        "answers": ["Το βιολί", "Η κιθάρα", "Το βιολοντσέλο (τσέλο)", "Το λαούτο"],
        "correctAnswerIndex": 2,
        "explanation": "Το βιολοντσέλο είναι το βαθύφωνο μέλος της οικογένειας των εγχόρδων, κουρδισμένο στις νότες Ντο-Σολ-Ρε-Λα σε διαστήματα πέμπτης.",
        "funFacts": [
            "Ο Γιόχαν Σεμπάστιαν Μπαχ συνέθεσε τις περίφημες Έξι Σουίτες για Τσέλο, που αποτελούν ακρογωνιαίο λίθο του ρεπερτορίου του οργάνου.",
            "Μέχρι τα μέσα του 20ού αιώνα, οι τσελίστες κρατούσαν το όργανο μόνο με τις γάμπες τους, πριν διαδοθεί η ρυθμιζόμενη μεταλλική ακίδα εδάφους (endpin)."
        ],
        "source": "https://en.wikipedia.org/wiki/Cello",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "instruments", "classical"]
    },
    {
        "id": "music_med_072",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια Αμερικανίδα τραγουδίστρια της soul και R&B αποκλήθηκε 'Η Βασίλισσα της Soul' (Queen of Soul) και τραγούδησε το 'Respect';",
        "answers": ["Τίνα Τέρνερ", "Νταϊάνα Ρος", "Γουίτνεϊ Χιούστον", "Αρίθα Φράνκλιν"],
        "correctAnswerIndex": 3,
        "explanation": "Η Αρίθα Φράνκλιν (Aretha Franklin) ηχογράφησε το 'Respect' του Ότις Ρέντινγκ το 1967, μετατρέποντάς το σε διαχρονικό ύμνο για τα πολιτικά δικαιώματα και τον φεμινισμό.",
        "funFacts": [
            "Η Αρίθα Φράνκλιν ήταν η πρώτη γυναίκα καλλιτέχνιδα που εισήχθη στο Rock and Roll Hall of Fame το 1987.",
            "Τραγούδησε στην ορκωμοσία τριών Αμερικανών προέδρων: του Τζίμι Κάρτερ, του Μπιλ Κλίντον και του Μπαράκ Ομπάμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Aretha_Franklin",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soul", "aretha_franklin"]
    },
    {
        "id": "music_med_073",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα heavy metal από το Μπέρμιγχαμ με κιθαρίστα τον Τόνι Αϊόμι θεωρείται ο ιδρυτικός πυλώνας του heavy metal ήχου;",
        "answers": ["Black Sabbath", "Judas Priest", "Iron Maiden", "Deep Purple"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Black Sabbath με τραγουδιστή τον Όζι Όσμπορν κυκλοφόρησαν το ομώνυμο ντεμπούτο άλμπουμ τους την Παρασκευή και 13 Φεβρουαρίου 1970, ορίζοντας το heavy metal.",
        "funFacts": [
            "Ο κιθαρίστας Τόνι Αϊόμι έχασε τις άκρες δύο δαχτύλων του σε βιομηχανικό ατύχημα και κατασκεύασε πλαστικές προθέσεις, ξεκουρδίζοντας την κιθάρα για ευκολότερο παίξιμο και δημιουργώντας τον σκοτεινό, βαρύ ήχο του metal.",
            "Το τραγούδι 'Paranoid' γράφτηκε σε μόλις 20 λεπτά στο στούντιο επειδή το συγκρότημα χρειαζόταν ένα επιπλέον κομμάτι διάρκειας 3 λεπτών για το άλμπουμ."
        ],
        "source": "https://en.wikipedia.org/wiki/Black_Sabbath",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "black_sabbath"]
    },
    {
        "id": "music_med_074",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου μουσικού φεστιβάλ που πραγματοποιήθηκε τον Αύγουστο του 1969 στη Νέα Υόρκη συγκεντρώνοντας 400.000 άτομα;",
        "answers": ["Glastonbury", "Woodstock", "Monterey Pop", "Altamont"],
        "correctAnswerIndex": 1,
        "explanation": "Το Φεστιβάλ του Γούντστοκ (Woodstock Music & Art Fair) αποτέλεσε το αποκορύφωμα της κουλτούρας των χίπις και της αντικουλτούρας της δεκαετίας του 1960.",
        "funFacts": [
            "Παρά το όνομά του, το φεστιβάλ δεν πραγματοποιήθηκε στο Γούντστοκ αλλά στη φάρμα γαλακτοπαραγωγής του Μαξ Γιασγκούρ στο Μπέθελ της Νέας Υόρκης.",
            "Η εμφάνιση του Τζίμι Χέντριξ με την ηλεκτρική παραμόρφωση του αμερικανικού εθνικού ύμνου 'The Star-Spangled Banner' έμεινε στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Woodstock",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "history", "woodstock"]
    },
    {
        "id": "music_med_075",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Πολωνός συνθέτης και βιρτουόζος του πιάνου της ρομαντικής περιόδου έγραψε σχεδόν αποκλειστικά για σόλο πιάνο (νοκτούρνες, μαζούρκες, πολωνέζες);",
        "answers": ["Φραντς Λιστ", "Ρόμπερτ Σούμαν", "Φρεντερίκ Σοπέν", "Φέλιξ Μέντελσον"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Φρεντερίκ Σοπέν (Frédéric Chopin) έζησε μεγάλο μέρος της ζωής του στο Παρίσι και θεωρείται ένας από τους πιο ποιητικούς συνθέτες πιάνου όλων των εποχών.",
        "funFacts": [
            "Σύμφωνα με την τελευταία του επιθυμία, η καρδιά του μεταφέρθηκε στην πατρίδα του τη Βαρσοβία και φυλάσσεται σε πυλώνα της εκκλησίας του Τιμίου Σταυρού.",
            "Είχε μια πολυετή ταραχώδη σχέση με τη διάσημη Γαλλίδα συγγραφέα Γεωργία Σάνδη (George Sand)."
        ],
        "source": "https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "chopin"]
    },
    {
        "id": "music_med_076",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη τραγουδίστρια της ποπ κυκλοφόρησε το άλμπουμ 'Like a Virgin' το 1984 και έγινε γνωστή ως 'Η Βασίλισσα της Ποπ';",
        "answers": ["Σίντι Λόπερ", "Κάιλι Μινόγκ", "Μαράια Κάρεϊ", "Μαντόνα"],
        "correctAnswerIndex": 3,
        "explanation": "Η Μαντόνα (Madonna Louise Ciccone) κυριάρχησε στην παγκόσμια ποπ σκηνή με συνεχείς επανεφευρέσεις της εικόνας και του ήχου της.",
        "funFacts": [
            "Το βιβλίο των Ρεκόρ Γκίνες αναγνωρίζει τη Μαντόνα ως τη γυναίκα καλλιτέχνιδα με τις μεγαλύτερες πωλήσεις δίσκων στην ιστορία (πάνω από 300 εκατομμύρια).",
            "Η εμβληματική εμφάνισή της στα πρώτα βραβεία MTV Video Music Awards το 1984 με νυφικό και ζώνη 'Boy Toy' προκάλεσε τεράστιο σκάνδαλο στην εποχή της."
        ],
        "source": "https://en.wikipedia.org/wiki/Madonna",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "madonna"]
    },
    {
        "id": "music_med_077",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Αμερικανού κιθαρίστα που έπαιζε αριστερόχειρα μια ανάποδα χορδισμένη Fender Stratocaster και έπαιξε στο Woodstock;",
        "answers": ["Τζίμι Χέντριξ", "Έρικ Κλάπτον", "Τζεφ Μπεκ", "Στίβι Ρέι Βον"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Τζίμι Χέντριξ (Jimi Hendrix) έφερε επανάσταση στην ηλεκτρική κιθάρα με τη χρήση feedback, distortion και wah-wah πεντάλ.",
        "funFacts": [
            "Ο Χέντριξ ήταν αριστερόχειρας, αλλά ο πατέρας του προσπάθησε να τον αναγκάσει να παίζει με το δεξί θεωρώντας το αριστερό χέρι σημάδι του διαβόλου.",
            "Στο Φεστιβάλ του Monterey Pop το 1967, ο Χέντριξ έβαλε φωτιά στην κιθάρα του στο τέλος του τραγουδιού 'Wild Thing'."
        ],
        "source": "https://en.wikipedia.org/wiki/Jimi_Hendrix",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "guitar", "hendrix"]
    },
    {
        "id": "music_med_078",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο γερμανικό συγκρότημα ηλεκτρονικής μουσικής από το Ντίσελντορφ θεωρείται ο θεμέλιος λίθος του synth-pop με το άλμπουμ 'Autobahn' (1974);",
        "answers": ["Tangerine Dream", "Kraftwerk", "Can", "Neu!"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Kraftwerk, ιδρυμένοι από τους Ραλφ Χίτερ και Φλόριαν Σνάιντερ, πρωτοπόρησαν στην αποκλειστική χρήση συνθεσάιζερ, drum machines και vocoders.",
        "funFacts": [
            "Οι Kraftwerk επηρέασαν σχεδόν κάθε σύγχρονο είδος ηλεκτρονικής μουσικής, από το synth-pop και το techno μέχρι το early hip-hop (όπως το 'Planet Rock' του Afrika Bambaataa).",
            "Στις ζωντανές εμφανίσεις τους συχνά αντικαθιστούσαν τους εαυτούς τους στη σκηνή με μηχανικά ρομπότ ανδρείκελα."
        ],
        "source": "https://en.wikipedia.org/wiki/Kraftwerk",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "electronic", "kraftwerk"]
    },
    {
        "id": "music_med_079",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου Ιρλανδού τραγουδιστή των U2, γνωστού για την ακτιβιστική του δράση;",
        "answers": ["The Edge", "Άνταμ Κλέιτον", "Μπόνο", "Λάρι Μάλεν"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Μπόνο (Bono, πραγματικό όνομα Πολ Ντέιβιντ Χιούσον) είναι ο κεντρικός τραγουδιστής των U2 από την ίδρυσή τους στο Δουβλίνο το 1976.",
        "funFacts": [
            "Το καλλιτεχνικό ψευδώνυμο 'Bono Vox' προήλθε από ένα κατάστημα ακουστικών βαρηκοΐας στο Δουβλίνο (Bonavox, που σημαίνει 'καλή φωνή' στα λατινικά).",
            "Φοράει σχεδόν πάντα φιμέ γυαλιά ηλίου δημοσίως όχι για στυλ αλλά επειδή πάσχει από χρόνιο γλαύκωμα που κάνει τα μάτια του εξαιρετικά ευαίσθητα στο φως."
        ],
        "source": "https://en.wikipedia.org/wiki/Bono",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "u2"]
    },
    {
        "id": "music_med_080",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το παλαιότερο είδος έντεχνης πολυφωνικής μουσικής που αναπτύχθηκε στη δυτική Ευρώπη τον Μεσαίωνα και τραγουδιόταν a cappella στα λατινικά;",
        "answers": ["Το μαδριγάλι", "Το μοτέτο", "Το γρηγοριανό μέλος", "Η καντάτα"],
        "correctAnswerIndex": 2,
        "explanation": "Το γρηγοριανό μέλος (Gregorian chant) είναι μονοφωνική, a cappella εκκλησιαστική μουσική της Ρωμαιοκαθολικής Εκκλησίας που κωδικοποιήθηκε επί Πάπα Γρηγορίου Α'.",
        "funFacts": [
            "Το γρηγοριανό μέλος οδήγησε στην εφεύρεση της σύγχρονης μουσικής σημειογραφίας (παρτιτούρα με πεντάγραμμο) από τον Γκουίντο ντ' Αρέτσο τον 11ο αιώνα.",
            "Τα ονόματα των νοτών (Ντο, Ρε, Μι, Φα, Σολ, Λα) προήλθαν από τα αρχικά των στίχων ενός λατινικού ύμνου στον Άγιο Ιωάννη τον Βαπτιστή (Ut queant laxis)."
        ],
        "source": "https://en.wikipedia.org/wiki/Gregorian_chant",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "medieval"]
    },
    {
        "id": "music_med_081",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα heavy metal με μασκότ τον ζόμπι 'Eddie' κυκλοφόρησε το άλμπουμ 'The Number of the Beast' το 1982;",
        "answers": ["Iron Maiden", "Saxon", "Motorhead", "Def Leppard"],
        "correctAnswerIndex": 0,
        "explanation": "Οι Iron Maiden με τραγουδιστή τον Μπρους Ντίκινσον και μπασίστα τον Στιβ Χάρις κυκλοφόρησαν το 'The Number of the Beast', εκτοξεύοντας το New Wave of British Heavy Metal (NWOBHM).",
        "funFacts": [
            "Ο Μπρους Ντίκινσον είναι επίσης επαγγελματίας πιλότος επιβατικών αεροσκαφών και πιλοτάριζε ο ίδιος το ειδικά διαμορφωμένο Boeing 747 του συγκροτήματος, το 'Ed Force One'.",
            "Η μασκότ Eddie εμφανίζεται σε όλα τα εξώφυλλα άλμπουμ και στις ζωντανές συναυλίες τους σε γιγάντια animatronic μορφή."
        ],
        "source": "https://en.wikipedia.org/wiki/Iron_Maiden",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "iron_maiden"]
    },
    {
        "id": "music_med_082",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη όπερα του Ζορζ Μπιζέ διαδραματίζεται στη Σεβίλλη και ακολουθεί τη σαγηνευτική τσιγγάνα Carmen;",
        "answers": ["Τραβιάτα", "Κάρμεν", "Τόσκα", "Αΐντα"],
        "correctAnswerIndex": 1,
        "explanation": "Η 'Κάρμεν' (Carmen) του Μπιζέ έκανε πρεμιέρα στο Παρίσι το 1875 και περιλαμβάνει πασίγνωστες άριες όπως η 'Habanera' και το 'Chanson du Toréador'.",
        "funFacts": [
            "Στην πρεμιέρα της, η όπερα θεωρήθηκε σκανδαλώδης και καταδικάστηκε από τους κριτικούς για την 'ανήθικη' συμπεριφορά της ηρωίδας.",
            "Ο Μπιζέ πέθανε ξαφνικά μόλις τρεις μήνες μετά την πρεμιέρα, χωρίς να προλάβει να δει την τεράστια παγκόσμια αποδοχή του έργου του."
        ],
        "source": "https://en.wikipedia.org/wiki/Carmen",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "opera", "classical"]
    },
    {
        "id": "music_med_083",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο progressive rock συγκρότημα κυκλοφόρησε το 1969 το μνημειώδες άλμπουμ 'In the Court of the Crimson King';",
        "answers": ["Yes", "Genesis", "King Crimson", "Jethro Tull"],
        "correctAnswerIndex": 2,
        "explanation": "Οι King Crimson του κιθαρίστα Ρόμπερτ Φριπ όρισαν το progressive rock συνδυάζοντας ροκ με τζαζ, κλασική μουσική και πειραματικό mellotron.",
        "funFacts": [
            "Ο Πιτ Τάουνσεντ των The Who χαρακτήρισε το άλμπουμ 'απόκοσμο αριστούργημα'.",
            "Το εισαγωγικό κομμάτι '21st Century Schizoid Man' έχει σαμπλαριστεί από πολλούς σύγχρονους καλλιτέχνες, συμπεριλαμβανομένου του Κάνιε Γουέστ στο τραγούδι 'Power'."
        ],
        "source": "https://en.wikipedia.org/wiki/In_the_Court_of_the_Crimson_King",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "progressive_rock"]
    },
    {
        "id": "music_med_084",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο παραδοσιακό ελληνικό μουσικό όργανο έχει τρεις ή τέσσερις διπλές χορδές και αποτελεί τη βάση του ρεμπέτικου και λαϊκού τραγουδιού;",
        "answers": ["Ο μπαγλαμάς", "Το ούτι", "Το κανονάκι", "Το μπουζούκι"],
        "correctAnswerIndex": 3,
        "explanation": "Το μπουζούκι κατάγεται από την αρχαιοελληνική πανδούρα και εξελίχθηκε στον βασικό πρωταγωνιστή της ελληνικής αστικής λαϊκής μουσικής.",
        "funFacts": [
            "Ο Μανώλης Χιώτης πρόσθεσε την τέταρτη διπλή χορδή (τετράχορδο μπουζούκι) και άλλαξε το κούρδισμα σε Ρε-Λα-Φα-Ντο τη δεκαετία του '50, επιτρέποντας ταχύτατα κιθαριστικά σόλο.",
            "Το τρίχορδο μπουζούκι (κουρδισμένο Ρε-Λα-Ρε) παραμένει η παραδοσιακή επιλογή για το κλασικό ρεμπέτικο."
        ],
        "source": "https://en.wikipedia.org/wiki/Bouzouki",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "instruments"]
    },
    {
        "id": "music_med_085",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός τραγουδοποιός κέρδισε το Νόμπελ Λογοτεχνίας το 2016 για τη δημιουργία νέων ποιητικών εκφράσεων στο πλαίσιο της μεγάλης αμερικανικής μουσικής παράδοσης;",
        "answers": ["Μπομπ Ντίλαν", "Μπρους Σπρίνγκστιν", "Λέοναρντ Κοέν", "Πολ Σάιμον"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μπομπ Ντίλαν (Bob Dylan) έγινε ο πρώτος μουσικός στην ιστορία που τιμήθηκε με το Βραβείο Νόμπελ Λογοτεχνίας.",
        "funFacts": [
            "Ο Ντίλαν χρειάστηκε αρκετές εβδομάδες για να αναγνωρίσει δημόσια το βραβείο και δεν παρέστη στην επίσημη τελετή απονομής στη Στοκχόλμη.",
            "Τα ιστορικά του τραγούδια 'Blowin' in the Wind' και 'The Times They Are a-Changin'' έγιναν ύμνοι του κινήματος για τα πολιτικά δικαιώματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Bob_Dylan",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "folk", "nobel"]
    },
    {
        "id": "music_med_086",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο άλμπουμ των The Beatles που κυκλοφόρησε το 1967 θεωρείται από τα πρώτα ολοκληρωμένα concept albums στην ιστορία της ροκ;",
        "answers": ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band", "Revolver", "The White Album"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Sgt. Pepper's Lonely Hearts Club Band' παρουσίασε τα 'Σκαθάρια' ως μια φανταστική μπάντα εποχής Εδουάρδου, φέρνοντας επανάσταση στην παραγωγή και το artwork.",
        "funFacts": [
            "Το πολύχρωμο εξώφυλλο περιλαμβάνει κολάζ με χαρτονένια ομοιώματα δεκάδων ιστορικών προσωπικοτήτων, από τον Όσκαρ Ουάιλντ μέχρι τον Μάρλον Μπράντο.",
            "Ήταν το πρώτο ροκ άλμπουμ που κέρδισε το βραβείο Grammy για το Άλμπουμ της Χρονιάς (1968)."
        ],
        "source": "https://en.wikipedia.org/wiki/Sgt._Pepper%27s_Lonely_Hearts_Club_Band",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "beatles"]
    },
    {
        "id": "music_med_087",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια είναι η ταχύτερη ένδειξη ρυθμού (tempo) στη δυτική κλασική μουσική μεταξύ των παρακάτω;",
        "answers": ["Andante", "Adagio", "Presto", "Moderato"],
        "correctAnswerIndex": 2,
        "explanation": "Το Presto υποδηλώνει πολύ γρήγορο τέμπο (συνήθως 168-200 χτύπους ανά λεπτό), ενώ τα Adagio (αργά), Andante (σε ρυθμό βαδίσματος) και Moderato (μέτρια) είναι σαφώς πιο αργά.",
        "funFacts": [
            "Ακόμα πιο γρήγορο από το Presto είναι το Prestissimo (πάνω από 200 bpm).",
            "Οι ιταλικοί όροι καθιερώθηκαν στην ευρωπαϊκή μουσική κατά τη διάρκεια της Αναγέννησης και του Μπαρόκ."
        ],
        "source": "https://en.wikipedia.org/wiki/Tempo",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "theory", "tempo"]
    },
    {
        "id": "music_med_088",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα grunge από το Σιάτλ κυκλοφόρησε το κολοσσιαίο ντεμπούτο άλμπουμ 'Ten' το 1991 με τραγουδιστή τον Έντι Βέντερ;",
        "answers": ["Soundgarden", "Alice in Chains", "Stone Temple Pilots", "Pearl Jam"],
        "correctAnswerIndex": 3,
        "explanation": "Οι Pearl Jam κυκλοφόρησαν το 'Ten' με τεράστια επιτυχία, περιλαμβάνοντας κλασικά κομμάτια όπως τα 'Alive', 'Even Flow' και 'Jeremy'.",
        "funFacts": [
            "Το όνομα του άλμπουμ 'Ten' ήταν φόρος τιμής στον αριθμό φανέλας του μπασκετμπολίστα Μούκι Μπλέιλοκ, από τον οποίο ονομαζόταν αρχικά το συγκρότημα.",
            "Το 'Ten' έχει πιστοποιηθεί ως 13 φορές πλατινένιο στις ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/Ten_(Pearl_Jam_album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "grunge", "pearl_jam"]
    },
    {
        "id": "music_med_089",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ισπανός τενόρος, μέλος των περίφημων 'Τριών Τενόρων' μαζί με τους Πλάθιντο Ντομίνγκο και Χοσέ Καρέρας, ήταν ο Λουτσιάνο Παβαρότι;",
        "answers": ["Λουτσιάνο Παβαρότι", "Αντρέα Μποτσέλι", "Ενρίκο Καρούζο", "Χουάν Ντιέγκο Φλόρες"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Ιταλός Λουτσιάνο Παβαρότι (Luciano Pavarotti) υπήρξε ένας από τους πιο επιτυχημένους και αναγνωρίσιμους τενόρους στην ιστορία της όπερας, διάσημος για το άπιαστο ψηλό Ντο του.",
        "funFacts": [
            "Η συναυλία των Τριών Τενόρων στη Ρώμη το 1990 για το Παγκόσμιο Κύπελλο Ποδοσφαίρου έγινε το πιο επιτυχημένο εμπορικά κλασικό άλμπουμ όλων των εποχών.",
            "Η ερμηνεία του στο 'Nessun dorma' από την όπερα Turandot του Πουτσίνι ταυτίστηκε απόλυτα με το όνομά του."
        ],
        "source": "https://en.wikipedia.org/wiki/Luciano_Pavarotti",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "opera", "pavarotti"]
    },
    {
        "id": "music_med_090",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο ηλεκτρονικό ντουέτο από τη Γαλλία με στολές και κράνη ρομπότ κυκλοφόρησε τα smash hits 'Around the World' και 'Get Lucky';",
        "answers": ["Justice", "Daft Punk", "Air", "Cassius"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Daft Punk (Γκι-Μανουέλ ντε Ομέμ-Κριστό και Τομά Μπανγκαλτέρ) υπήρξαν οι κορυφαίοι πρωτοπόροι του French House κινήματος από τη δεκαετία του '90 έως τη διάλυσή τους το 2021.",
        "funFacts": [
            "Υιοθέτησαν τα χαρακτηριστικά κράνη ρομπότ το 2001 για να διατηρήσουν την ανωνυμία τους και να προστατεύσουν την προσωπική τους ζωή.",
            "Το άλμπουμ τους 'Random Access Memories' (2013) κέρδισε πέντε βραβεία Grammy, συμπεριλαμβανομένου του Άλμπουμ της Χρονιάς."
        ],
        "source": "https://en.wikipedia.org/wiki/Daft_Punk",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "electronic", "daft_punk"]
    },
    {
        "id": "music_med_091",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Πόσες χορδές έχει μια τυπική κλασική κιθάρα;",
        "answers": ["4", "5", "6", "8"],
        "correctAnswerIndex": 2,
        "explanation": "Η κλασική κιθάρα έχει 6 χορδές, κουρδισμένες από τη χαμηλότερη στην υψηλότερη στις νότες Μι-Λα-Ρε-Σολ-Σι-Μι (E-A-D-G-B-E).",
        "funFacts": [
            "Οι σύγχρονες κλασικές κιθάρες χρησιμοποιούν νάιλον χορδές για τις υψηλές νότες, σε αντίθεση με το παρελθόν όπου κατασκευάζονταν από έντερα ζώων (gut strings).",
            "Ο Ισπανός Αντόνιο ντε Τόρες Χουράδο θεωρείται ο 'πατέρας' της σύγχρονης κλασικής κιθάρας, καθιερώνοντας το μέγεθος και τις αναλογίες της τον 19ο αιώνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Classical_guitar",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "instruments", "guitar"]
    },
    {
        "id": "music_med_092",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο punk rock συγκρότημα από τη Νέα Υόρκη, με μέλη που υιοθέτησαν όλοι το ίδιο επίθετο (Joey, Johnny, Dee Dee), θεωρείται το πρώτο αληθινό punk συγκρότημα;",
        "answers": ["The Clash", "Sex Pistols", "The Damned", "Ramones"],
        "correctAnswerIndex": 3,
        "explanation": "Οι Ramones σχηματίστηκαν στο Queens της Νέας Υόρκης το 1974, παίζοντας σύντομα, αστραπιαία τραγούδια με τρία ακκόρντα.",
        "funFacts": [
            "Κανένα από τα μέλη των Ramones δεν είχε βιολογική συγγένεια μεταξύ τους.",
            "Το ψευδώνυμο Ramone εμπνεύστηκε από τον Πολ Μακάρτνεϊ, ο οποίος χρησιμοποιούσε το ψευδώνυμο 'Paul Ramon' όταν έκανε check-in σε ξενοδοχεία για να μην τον αναγνωρίζουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Ramones",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "punk", "ramones"]
    },
    {
        "id": "music_med_093",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ρώσος συνθέτης δημιούργησε τα αθάνατα μπαλέτα 'Η Λίμνη των Κύκνων', 'Ο Καρυοθραύστης' και 'Η Ωραία Κοιμωμένη';",
        "answers": ["Πιότρ Ιλίτς Τσαϊκόφσκι", "Σεργκέι Ραχμάνινοφ", "Ιγκόρ Στραβίνσκι", "Σεργκέι Προκόφιεφ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Πιότρ Ιλίτς Τσαϊκόφσκι υπήρξε ο κορυφαίος συνθέτης της ρωσικής ρομαντικής εποχής, χαρίζοντας μερικά από τα πιο δημοφιλή έργα κλασικής μουσικής.",
        "funFacts": [
            "Στην 'Εισαγωγή 1812', ο Τσαϊκόφσκι συμπεριέλαβε στην παρτιτούρα πραγματικούς πυροβολισμούς κανονιών.",
            "Η πρεμιέρα της 'Λίμνης των Κύκνων' στη Μόσχα το 1877 ήταν αρχικά αποτυχία λόγω κακής χορογραφίας, πριν αναγνωριστεί αργότερα ως απόλυτο αριστούργημα."
        ],
        "source": "https://en.wikipedia.org/wiki/Pyotr_Ilyich_Tchaikovsky",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "ballet", "tchaikovsky"]
    },
    {
        "id": "music_med_094",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός μουσικός και παραγωγός συνίδρυσε την Def Jam Recordings και βοήθησε στη διαμόρφωση του ήχου καλλιτεχνών όπως οι Beastie Boys, Run-DMC, Public Enemy και Slayer;",
        "answers": ["Dr. Dre", "Ρικ Ρούμπιν", "Κουίνσι Τζόουνς", "Τζίμι Άιοβιν"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Ρικ Ρούμπιν (Rick Rubin) ξεκίνησε την Def Jam από το δωμάτιο της φοιτητικής του εστίας στο NYU και εξελίχθηκε σε έναν από τους πιο επιδραστικούς παραγωγούς στην ιστορία της μουσικής.",
        "funFacts": [
            "Ο Ρούμπιν αναβίωσε την καριέρα του Τζόνι Κας τη δεκαετία του '90 με τη σειρά ακουστικών ηχογραφήσεων 'American Recordings'.",
            "Είναι γνωστός για τη μινιμαλιστική του προσέγγιση ('απογύμνωση' του ήχου) και το ότι παράγει άλμπουμ χωρίς να παίζει ο ίδιος κάποιο όργανο στο στούντιο."
        ],
        "source": "https://en.wikipedia.org/wiki/Rick_Rubin",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "production", "producers"]
    },
    {
        "id": "music_med_095",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου μουσικού φεστιβάλ heavy metal που διεξάγεται κάθε καλοκαίρι σε ένα μικρό χωριό στη βόρεια Γερμανία;",
        "answers": ["Hellfest", "Download Festival", "Wacken Open Air", "Graspop"],
        "correctAnswerIndex": 2,
        "explanation": "Το Wacken Open Air (W:O:A) ξεκίνησε το 1990 ως ένα μικρό τοπικό φεστιβάλ με 800 θεατές και εξελίχθηκε στο μεγαλύτερο heavy metal φεστιβάλ του κόσμου με πάνω από 85.000 επισκέπτες.",
        "funFacts": [
            "Το φεστιβάλ κατασκεύασε έναν ειδικό υπόγειο αγωγό μπύρας μήκους 7 χιλιομέτρων για να τροφοδοτεί τα μπαρ χωρίς να καταστρέφεται το έδαφος από βαριά φορτηγά.",
            "Τα εισιτήρια του φεστιβάλ εξαντλούνται τακτικά μέσα σε λίγες ώρες, σχεδόν έναν χρόνο πριν από τη διεξαγωγή του."
        ],
        "source": "https://en.wikipedia.org/wiki/Wacken_Open_Air",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "festivals"]
    },
    {
        "id": "music_med_096",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του ελληνικού πνευστού παραδοσιακού οργάνου από δέρμα κατσίκας, αντίστοιχου της σκωτσέζικης γκάιντας;",
        "answers": ["Η τσαμπούνα", "Το κλαρίνο", "Ο ζουρνάς", "Το νέι"],
        "correctAnswerIndex": 0,
        "explanation": "Η τσαμπούνα είναι παραδοσιακός άσκαυλος των νησιών του Αιγαίου, κατασκευασμένος από ολόκληρο δέρμα κατσικιού και διπλό καλαμένιο σωλήνα με τρύπες.",
        "funFacts": [
            "Σε αντίθεση με τη βορειοελλαδίτικη γκάιντα, η αιγαιοπελαγίτικη τσαμπούνα δεν έχει μακρύ ισοκράτη (μπουρί), παράγοντας πολυφωνικό ήχο από τις δύο παράλληλες καλαμένιες πίπιλες.",
            "Είναι ένα από τα αρχαιότερα πνευστά όργανα που παίζονται αδιάλειπτα στον ελλαδικό χώρο από την αρχαιότητα."
        ],
        "source": "https://en.wikipedia.org/wiki/Tsampouna",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "traditional_instruments"]
    },
    {
        "id": "music_med_097",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο θρυλικό progressive metal συγκρότημα από τις ΗΠΑ κυκλοφόρησε το άλμπουμ 'Images and Words' (1992) με το κομμάτι 'Pull Me Under';",
        "answers": ["Queensrÿche", "Dream Theater", "Fates Warning", "Symphony X"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Dream Theater, ιδρυμένοι από φοιτητές του Berklee College of Music (Πετρούτσι, Πορτνόι, Μιούνγκ), έγιναν οι κορυφαίοι εκπρόσωποι του τεχνικού progressive metal.",
        "funFacts": [
            "Το 'Pull Me Under' έγινε αναπάντεχο ραδιοφωνικό και MTV hit, παρά το γεγονός ότι διαρκεί πάνω από 8 λεπτά.",
            "Το τέλος του τραγουδιού κόβεται απότομα σε πλήρη σιωπή, ως φόρος τιμής στο 'I Want You (She's So Heavy)' των Beatles."
        ],
        "source": "https://en.wikipedia.org/wiki/Images_and_Words",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "metal", "dream_theater"]
    },
    {
        "id": "music_med_098",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Βρετανός τραγουδοποιός και πιανίστας συνέθεσε το soundtrack της ταινίας 'The Lion King' (Ο Βασιλιάς των Λιονταριών) της Disney μαζί με τον Τιμ Ράις;",
        "answers": ["Φιλ Κόλινς", "Μπίλι Τζόελ", "Έλτον Τζον", "Πολ Μακάρτνεϊ"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Έλτον Τζον συνέθεσε κλασικά τραγούδια όπως τα 'Can You Feel the Love Tonight' και 'Circle of Life', κερδίζοντας το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 1995.",
        "funFacts": [
            "Το 'Can You Feel the Love Tonight' κόντεψε να κοπεί από την ταινία, αλλά ο Έλτον Τζον επέμεινε να παραμείνει αφού είδε ένα πρώτο cut.",
            "Το single του Έλτον Τζον 'Candle in the Wind 1997' (αφιερωμένο στην Πριγκίπισσα Νταϊάνα) είναι το δεύτερο single με τις μεγαλύτερες πωλήσεις στην ιστορία της μουσικής."
        ],
        "source": "https://en.wikipedia.org/wiki/Elton_John",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "pop", "disney", "elton_john"]
    },
    {
        "id": "music_med_099",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο ξύλινο πνευστό όργανο με διπλή γλωττίδα δίνει παραδοσιακά τον τόνο κουρδίσματος (νότα Λα) σε ολόκληρη τη συμφωνική ορχήστρα;",
        "answers": ["Το φλάουτο", "Το κλαρινέτο", "Το φαγκότο", "Το όμποε"],
        "correctAnswerIndex": 3,
        "explanation": "Το όμποε έχει έντονο, διαπεραστικό ήχο πλούσιο σε αρμονικές και σταθερό κούρδισμα, γι' αυτό ο πρώτος ομποΐστας δίνει παραδοσιακά το Λα (A440) για το κούρδισμα της ορχήστρας.",
        "funFacts": [
            "Οι γλωττίδες του όμποε κατασκευάζονται στο χέρι από ειδικό καλάμι (Arundo donax) και είναι εξαιρετικά ευαίσθητες στην υγρασία και τη θερμοκρασία.",
            "Το όνομα όμποε προέρχεται από το γαλλικό 'hautbois', που σημαίνει κυριολεκτικά 'υψηλό ξύλο'."
        ],
        "source": "https://en.wikipedia.org/wiki/Oboe",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "instruments", "orchestra"]
    },
    {
        "id": "music_med_100",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας συνθέτης έγραψε τη μουσική για την ταινία 'Ζορμπάς' (Zorba the Greek, 1964) καθιερώνοντας το συρτάκι παγκοσμίως;",
        "answers": ["Μάνος Χατζιδάκις", "Μίκης Θεοδωράκης", "Σταύρος Ξαρχάκος", "Γιάννης Μαρκόπουλος"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Μίκης Θεοδωράκης συνέθεσε το διάσημο θέμα του Ζορμπά, βασισμένο σε παραδοσιακούς χασάπικους ρυθμούς, κάνοντας τη μουσική του σύμβολο της Ελλάδας σε όλο τον πλανήτη.",
        "funFacts": [
            "Ο χορός συρτάκι δημιουργήθηκε ειδικά για την ταινία ώστε να διευκολυνθεί ο ηθοποιός Άντονι Κουίν, ο οποίος είχε σπάσει το πόδι του και δεν μπορούσε να χοροπηδάει.",
            "Ο Θεοδωράκης συνέθεσε επίσης ιστορικούς κύκλους τραγουδιών βασισμένους στην ποίηση των Ρίτσου, Σεφέρη, Ελύτη και Λόρκα."
        ],
        "source": "https://en.wikipedia.org/wiki/Mikis_Theodorakis",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "greek_music", "theodorakis"]
    },
    {
        "id": "music_med_101",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό post-punk συγκρότημα από το Μάντσεστερ με τραγουδιστή τον Ίαν Κέρτις μετονομάστηκε σε New Order μετά τον θάνατό του το 1980;",
        "answers": ["The Smiths", "Joy Division", "The Cure", "Echo & the Bunnymen"],
        "correctAnswerIndex": 1,
        "explanation": "Οι Joy Division κυκλοφόρησαν τα σκοτεινά αριστουργήματα 'Unknown Pleasures' και 'Closer' πριν διαλυθούν και αναγεννηθούν ως New Order.",
        "funFacts": [
            "Το εξώφυλλο του 'Unknown Pleasures' απεικονίζει τα ραδιοσήματα από το πρώτο ανακαλυφθέν πάλσαρ (CP 1919) και αποτελεί ένα από τα πιο διάσημα εξώφυλλα στην ιστορία της ροκ.",
            "Το κομμάτι των New Order 'Blue Monday' (1983) έγινε το πιο εμπορικό maxi-single 12 ιντσών όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/Joy_Division",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "post_punk"]
    },
    {
        "id": "music_med_102",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Ιταλός συνθέτης κινηματογραφικής μουσικής έγραψε τα θρυλικά scores για τα σπαγγέτι γουέστερν του Σέρτζιο Λεόνε, όπως 'Ο Καλός, ο Κακός και ο Άσχημος';",
        "answers": ["Νίνο Ρότα", "Ένιο Μορικόνε", "Νικόλα Πιοβάνι", "Τζόρτζιο Μόροντερ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Ένιο Μορικόνε (Ennio Morricone) συνέθεσε πάνω από 400 κινηματογραφικά scores, χρησιμοποιώντας σφυρίγματα, πυροβολισμούς, άρπες στόματος και ηλεκτρικές κιθάρες.",
        "funFacts": [
            "Ο Μορικόνε και ο Σέρτζιο Λεόνε ήταν συμμαθητές στο δημοτικό σχολείο στη Ρώμη πριν συνεργαστούν δεκαετίες αργότερα στον κινηματογράφο.",
            "Κέρδισε το Όσκαρ Καλύτερης Πρωτότυπης Μουσικής σε ηλικία 87 ετών για την ταινία 'The Hateful Eight' του Κουέντιν Ταραντίνο (2015)."
        ],
        "source": "https://en.wikipedia.org/wiki/Ennio_Morricone",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "soundtracks", "morricone"]
    },
    {
        "id": "music_med_103",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου άλμπουμ των Fleetwood Mac του 1977 που γράφτηκε εν μέσω χωρισμών όλων των μελών του συγκροτήματος;",
        "answers": ["Tusk", "Mirage", "Rumours", "Tango in the Night"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Rumours' των Fleetwood Mac πούλησε πάνω από 40 εκατομμύρια αντίτυπα παγκοσμίως και περιλαμβάνει hits όπως τα 'Go Your Own Way' και 'Dreams'.",
        "funFacts": [
            "Κατά τη διάρκεια των ηχογραφήσεων, ο Τζον και η Κριστίν ΜακΒί έπαιρναν διαζύγιο, ο Λίντσεϊ Μπάκιγχαμ και η Στίβι Νικς χώριζαν, και ο Μικ Φλίτγουντ χώριζε με τη σύζυγό του.",
            "Το τραγούδι 'Dreams' έγινε ξανά viral hit στο TikTok το 2020 χάρη σε ένα βίντεο ενός άνδρα πάνω σε σκέιτμπορντ που έπινε χυμό κράνμπερι."
        ],
        "source": "https://en.wikipedia.org/wiki/Rumours_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "fleetwood_mac"]
    },
    {
        "id": "music_med_104",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο έγχορδο όργανο με 47 χορδές και 7 πεντάλ ποδιού παίζεται με τα δάχτυλα και έχει τριγωνικό πλαίσιο;",
        "answers": ["Το σαντούρι", "Το κανονάκι", "Η άρπα", "Η λύρα"],
        "correctAnswerIndex": 2,
        "explanation": "Η ορχηστρική άρπα με πεντάλ (concert harp) διαθέτει 47 χορδές και 7 ποδοπλήκτρα που αλλάζουν το κούρδισμα των χορδών κατά ένα ημιτόνιο.",
        "funFacts": [
            "Οι αρπίστες χρησιμοποιούν μόνο τα τέσσερα δάχτυλα κάθε χεριού (αντίχειρα, δείκτη, μέσο και παράμεσο), καθώς το μικρό δαχτυλάκι θεωρείται πολύ αδύναμο.",
            "Η άρπα είναι το επίσημο εθνικό σύμβολο της Ιρλανδίας και εμφανίζεται στο έμβλημα της μπύρας Guinness."
        ],
        "source": "https://en.wikipedia.org/wiki/Harp",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "instruments", "harp"]
    },
    {
        "id": "music_med_105",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο ήταν το πρώτο μουσικό βίντεο κλιπ που μεταδόθηκε ποτέ από το τηλεοπτικό κανάλι MTV κατά την έναρξη λειτουργίας του την 1η Αυγούστου 1981;",
        "answers": ["Video Killed the Radio Star", "Billie Jean", "Take on Me", "Money for Nothing"],
        "correctAnswerIndex": 0,
        "explanation": "Το τραγούδι 'Video Killed the Radio Star' των The Buggles ήταν το απόλυτα προφητικό πρώτο βίντεο κλιπ που έπαιξε στην ιστορία του MTV.",
        "funFacts": [
            "Το δεύτερο βίντεο κλιπ που προβλήθηκε αμέσως μετά ήταν το 'You Better Run' της Πατ Μπέναταρ.",
            "Ο Χανς Ζίμερ, διάσημος συνθέτης ταινιών σήμερα, εμφανίζεται ως νεαρός πληκτράς στο βίντεο κλιπ των Buggles."
        ],
        "source": "https://en.wikipedia.org/wiki/Video_Killed_the_Radio_Star",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "history", "mtv"]
    },
    {
        "id": "music_med_106",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος βιολονίστας της κλασικής εποχής συνέθεσε τα 24 Καπρίτσια και φημολογούνταν από τους συγχρόνους του ότι είχε πουλήσει την ψυχή του στον διάβολο;",
        "answers": ["Νικολό Παγκανίνι", "Τζουζέπε Ταρτίνι", "Πάμπλο ντε Σαρασάτε", "Φριτς Κράισλερ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Νικολό Παγκανίνι (Niccolò Paganini) διέθετε απίστευτη δεξιοτεχνία στο βιολί και εξαιρετικά εύκαμπτα δάχτυλα (πιθανώς λόγω του συνδρόμου Marfan).",
        "funFacts": [
            "Το αγαπημένο του βιολί ήταν ένα Guarneri del Gesù του 1743, το οποίο ονόμαζε 'Il Cannone' (Το Κανόνι) λόγω του πανίσχυρου ήχου του.",
            "Εισήγαγε πρωτοποριακές τεχνικές στο βιολί, όπως το pizzicato με το αριστερό χέρι και τα διπλά αρμονικά."
        ],
        "source": "https://en.wikipedia.org/wiki/Niccol%C3%B2_Paganini",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "classical", "violin", "paganini"]
    },
    {
        "id": "music_med_107",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο άλμπουμ των Radiohead του 1997 περιλαμβάνει τα κομμάτια 'Paranoid Android' και 'Karma Police';",
        "answers": ["The Bends", "OK Computer", "Kid A", "In Rainbows"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'OK Computer' των Radiohead με παραγωγό τον Νάιτζελ Γκόντριτς θεωρείται ένα από τα σπουδαιότερα άλμπουμ της δεκαετίας του '90, αποτυπώνοντας την τεχνολογική αποξένωση.",
        "funFacts": [
            "Ο τίτλος προήλθε από μια φράση στο ραδιοφωνικό έργο 'Γυρίστε το Γαλαξία με Ώτοστοπ' του Ντάγκλας Άνταμς.",
            "Το κομμάτι 'Fitter Happier' απαγγέλλεται εξ ολοκλήρου από τη συνθετική φωνή του προγράμματος SimpleText των υπολογιστών Apple Macintosh."
        ],
        "source": "https://en.wikipedia.org/wiki/OK_Computer",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "rock", "radiohead"]
    },
    {
        "id": "music_med_108",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός τραγουδιστής της country και rockabilly αποκλήθηκε 'The Man in Black' και τραγούδησε τα 'Ring of Fire' και 'I Walk the Line';",
        "answers": ["Γουίλι Νέλσον", "Τζόνι Κας", "Γουέιλον Τζένινγκς", "Κένι Ρότζερς"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Τζόνι Κας (Johnny Cash) έμεινε στην ιστορία για τη βαθιά μπάσα φωνή του, τα μαύρα ρούχα του και τις θρυλικές ζωντανές συναυλίες του μέσα σε φυλακές όπως το Folsom και το San Quentin.",
        "funFacts": [
            "Φορούσε αποκλειστικά μαύρα ρούχα επί σκηνής ως ένδειξη αλληλεγγύης προς τους φτωχούς, τους καταπιεσμένους και τους φυλακισμένους.",
            "Η διασκευή του στο τραγούδι 'Hurt' των Nine Inch Nails το 2002 θεωρείται μία από τις πιο συγκινητικές ερμηνείες στην ιστορία της μουσικής."
        ],
        "source": "https://en.wikipedia.org/wiki/Johnny_Cash",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "country", "johnny_cash"]
    },
    {
        "id": "music_med_109",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη jazz τραγουδίστρια αποκλήθηκε 'Η Πρώτη Κυρία του Τραγουδιού' (First Lady of Song) και ήταν ανυπέρβλητη στο scat singing;",
        "answers": ["Μπίλι Χόλιντεϊ", "Σάρα Βον", "Έλλα Φιτζέραλντ", "Κάρμεν ΜακΡέι"],
        "correctAnswerIndex": 2,
        "explanation": "Η Έλλα Φιτζέραλντ (Ella Fitzgerald) είχε καθαρότατη φωνή τριών οκτάβων, αλάνθαστο συγχρονισμό και κέρδισε 14 βραβεία Grammy στη λαμπρή καριέρα της.",
        "funFacts": [
            "Η σειρά ηχογραφήσεών της 'Great American Songbook' για τη δισκογραφική Verve αποτελεί το οριστικό αρχείο των κλασικών αμερικανικών προτύπων.",
            "Ξεκίνησε την καριέρα της κερδίζοντας την ερασιτεχνική βραδιά στο θρυλικό θέατρο Apollo του Χάρλεμ το 1934 σε ηλικία 17 ετών."
        ],
        "source": "https://en.wikipedia.org/wiki/Ella_Fitzgerald",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "jazz", "ella_fitzgerald"]
    },
    {
        "id": "music_med_110",
        "categoryId": "music",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου μουσικού ρεύματος που γεννήθηκε στο Μπρονξ της Νέας Υόρκης τη δεκαετία του 1970 και βασίζεται στα τέσσερα στοιχεία: DJing, MCing, B-boying και Graffiti;",
        "answers": ["R&B", "Funk", "Soul", "Hip Hop"],
        "correctAnswerIndex": 3,
        "explanation": "Το Hip Hop γεννήθηκε επίσημα στις 11 Αυγούστου 1973 σε ένα πάρτι στην οδό Sedgwick Avenue 1520 στο Μπρονξ από τον DJ Kool Herc.",
        "funFacts": [
            "Ο DJ Kool Herc απομόνωσε τα ρυθμικά 'breaks' των funk δίσκων χρησιμοποιώντας δύο πικάπ, γεννώντας τη βάση της hip hop παραγωγής.",
            "Το 'Rapper's Delight' των Sugarhill Gang (1979) ήταν το πρώτο rap single που μπήκε στο top 40 των charts των ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/Hip_hop_music",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["music", "hip_hop", "history"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(QUESTIONS)} questions for music_medium.")
    validate_and_append("music", "medium", 3, QUESTIONS)

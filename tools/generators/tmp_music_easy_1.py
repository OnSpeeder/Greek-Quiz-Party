import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
    {
        "id": "music_easy_011",
        "text": "Ποια εμβληματική Ελληνοαμερικανίδα υψίφωνος (σοπράνο) έμεινε στην ιστορία της παγκόσμιας όπερας με τον τίτλο «La Divina» (Η Θεϊκή);",
        "answers": [
            "Μαρία Κάλλας",
            "Ρενάτα Τεμπάλντι",
            "Μονσερά Καμπαγιέ",
            "Τζόαν Σάδερλαντ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Μαρία Κάλλας υπήρξε η σπουδαιότερη υψίφωνος του 20ού αιώνα, ανανεώνοντας ριζικά την τέχνη της όπερας με τις υποκριτικές και φωνητικές της ερμηνείες.",
        "funFacts": [
            "Γεννήθηκε στη Νέα Υόρκη από Έλληνες μετανάστες και το πραγματικό της όνομα ήταν Σοφία Καικιλία Άννα Μαρία Καλογεροπούλου.",
            "Οι εμφανίσεις της στη Σκάλα του Μιλάνου και στη Βασιλική Όπερα του Λονδίνου θεωρούνται μέχρι σήμερα ανυπέρβλητες ιστορικά."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AF%CE%B1_%CE%9A%CE%AC%CE%BB%CE%BB%CE%B1%CF%82",
        "locale": "el-GR",
        "tags": ["callas", "opera", "classical", "greece"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_012",
        "text": "Ποιο σουηδικό ποπ συγκρότημα κέρδισε τον Διαγωνισμό της Eurovision το 1974 με το τραγούδι «Waterloo» και εξελίχθηκε σε παγκόσμιο φαινόμενο;",
        "answers": [
            "Roxette",
            "ABBA",
            "Ace of Base",
            "A-ha"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι ABBA δημιουργήθηκαν στη Στοκχόλμη το 1972 από τους Agnetha Fältskog, Björn Ulvaeus, Benny Andersson και Anni-Frid Lyngstad.",
        "funFacts": [
            "Το όνομα του συγκροτήματος σχηματίστηκε από τα αρχικά γράμματα των μικρών ονομάτων των τεσσάρων μελών του.",
            "Η μουσική τους ενέπνευσε το παγκοσμίως επιτυχημένο μιούζικαλ και κινηματογραφική ταινία 'Mamma Mia!'."
        ],
        "source": "https://el.wikipedia.org/wiki/ABBA",
        "locale": "el-GR",
        "tags": ["abba", "pop", "eurovision", "sweden"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_013",
        "text": "Πόσα πλήκτρα (λευκά και μαύρα) διαθέτει κατά κανόνα ένα σύγχρονο τυπικό πιάνο;",
        "answers": [
            "76",
            "84",
            "88",
            "96"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ένα κανονικό πληκτρολόγιο πιάνου έχει ακριβώς 88 πλήκτρα, τα οποία καλύπτουν έκταση επτά οκτάβων συν μια μικρή τρίτη.",
        "funFacts": [
            "Από τα 88 πλήκτρα, τα 52 είναι λευκά (φυσικοί φθόγγοι) και τα 36 είναι μαύρα (αλλοιώσεις/ημιτόνια).",
            "Το πιάνο εφευρέθηκε στην Ιταλία γύρω στο 1700 από τον κατασκευαστή μουσικών οργάνων Μπαρτολομέο Κριστοφόρι."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CE%AC%CE%BD%CE%BF",
        "locale": "el-GR",
        "tags": ["piano", "instruments", "music-theory"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_014",
        "text": "Ποιος Τζαμαϊκανός καλλιτέχνης υπήρξε ο κορυφαίος εκπρόσωπος και πρεσβευτής της ρέγκε μουσικής παγκοσμίως;",
        "answers": [
            "Πίτερ Τος",
            "Τζίμι Κλιφ",
            "Σάγκι",
            "Μπομπ Μάρλεϊ"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Bob Marley έκανε τη ρέγκε και το κίνημα των Ρασταφάρι γνωστά σε ολόκληρο τον πλανήτη με τους The Wailers.",
        "funFacts": [
            "Το άλμπουμ 'Exodus' του 1977 ψηφίστηκε από το περιοδικό Time ως το κορυφαίο μουσικό άλμπουμ του 20ού αιώνα.",
            "Η συλλογή τραγουδιών του 'Legend' (1984) παραμένει το ρέγκε άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CE%BC%CF%80_%CE%9C%CE%AC%CF%81%CE%BB%CE%B5%CF%8A",
        "locale": "el-GR",
        "tags": ["bob-marley", "reggae", "jamaica"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_015",
        "text": "Ποια τραγουδίστρια χάρισε στην Ελλάδα την πρώτη της νίκη στον Διαγωνισμό Τραγουδιού της Eurovision το 2005 με το «My Number One»;",
        "answers": [
            "Έλενα Παπαρίζου",
            "Καλομοίρα",
            "Άννα Βίσση",
            "Ελένη Φουρέιρα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Έλενα Παπαρίζου κατέκτησε την πρώτη θέση για την Ελλάδα στον 50ό διαγωνισμό της Eurovision στο Κίεβο το 2005.",
        "funFacts": [
            "Είχε εκπροσωπήσει ξανά την Ελλάδα το 2001 στην Κοπεγχάγη ως μέλος του συγκροτήματος Antique, κατακτώντας την 3η θέση με το 'Die for You'.",
            "Το 'My Number One' ήταν σε σύνθεση του Χρήστου Δάντη και στίχους της Ναταλίας Γερμανού και του Χρήστου Δάντη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BB%CE%B5%CE%BD%CE%B1_%CE%A0%CE%B1%CF%80%CE%B1%CF%81%CE%AF%CE%B6%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["eurovision", "paparizou", "greek-music", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_016",
        "text": "Ποιος Αυστριακός συνθέτης υπήρξε παιδί-θαύμα της κλασικής εποχής και έγραψε έργα όπως «Μικρή Νυχτερινή Μουσική» και «Ο Μαγικός Αυλός»;",
        "answers": [
            "Φραντς Γιόζεφ Χάυντν",
            "Βόλφγκανγκ Αμαντέους Μότσαρτ",
            "Γιόχαν Στράους",
            "Ρίχαρντ Βάγκνερ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Mozart συνέθεσε περισσότερα από 600 έργα κατά τη διάρκεια της σύντομης ζωής του, πεθαίνοντας σε ηλικία μόλις 35 ετών.",
        "funFacts": [
            "Άρχισε να συνθέτει μουσική στην ηλικία των 5 ετών και έπαιζε άπταιστα πληκτροφόρο και βιολί μπροστά σε βασιλείς της Ευρώπης.",
            "Το τελευταίο του έργο, το επιβλητικό Ρέκβιεμ (Requiem), έμεινε ημιτελές λόγω του αιφνίδιου θανάτου του το 1791."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CF%8C%CE%BB%CF%86%CE%B3%CE%BA%CE%B1%CE%BD%CE%B3%CE%BA_%CE%91%CE%BC%CE%B1%CE%BD%CF%84%CE%AD%CE%BF%CF%85%CF%82_%CE%9C%CF%8C%CF%84%CF%83%CE%B1%CF%81%CF%84",
        "locale": "el-GR",
        "tags": ["mozart", "classical", "salzburg", "opera"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_017",
        "text": "Ποιο θρυλικό βρετανικό ροκ συγκρότημα έχει ως παγκοσμίως αναγνωρίσιμο έμβλημα μια κόκκινη γλώσσα που προεξέχει από τα χείλη;",
        "answers": [
            "Led Zeppelin",
            "AC/DC",
            "The Rolling Stones",
            "Aerosmith"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το διάσημο λογότυπο σχεδιάστηκε το 1970 από τον John Pasche και πρωτοεμφανίστηκε στο άλμπουμ 'Sticky Fingers' (1971).",
        "funFacts": [
            "Το συγκρότημα δημιουργήθηκε στο Λονδίνο το 1962 με επικεφαλής τους Mick Jagger και Keith Richards.",
            "Το τραγούδι τους '(I Can\\'t Get No) Satisfaction' του 1965 αποτέλεσε την πρώτη τους νούμερο ένα επιτυχία στις ΗΠΑ."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Rolling_Stones",
        "locale": "el-GR",
        "tags": ["rolling-stones", "rock", "bands"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_018",
        "text": "Ποιος παγκοσμίου φήμης Έλληνας συνθέτης κέρδισε το Όσκαρ Πρωτότυπης Μουσικής για το soundtrack της ταινίας «Οι Δρόμοι της Φωτιάς» (Chariots of Fire);",
        "answers": [
            "Σταύρος Ξαρχάκος",
            "Γιάννης Μαρκόπουλος",
            "Μίκης Θεοδωράκης",
            "Βαγγέλης Παπαθανασίου"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Βαγγέλης Παπαθανασίου (Vangelis) πρωτοπόρησε στην ηλεκτρονική και κινηματογραφική μουσική, κερδίζοντας το Όσκαρ το 1982.",
        "funFacts": [
            "Συνέθεσε επίσης το εμβληματικό soundtrack για τη θρυλική ταινία επιστημονικής φαντασίας 'Blade Runner' (1982) του Ρίντλεϊ Σκοτ.",
            "Η NASA και η ESA χρησιμοποίησαν συνθέσεις του σε διαστημικές αποστολές, όπως το έργο 'Μυθωδία' για την αποστολή στον Άρη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CE%B3%CE%B3%CE%AD%CE%BB%CE%B7%CF%82_%CE%A0%CE%B1%CF%80%CE%B1%CE%B8%CE%B1%CE%BD%CE%B1%CF%83%CE%AF%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["vangelis", "soundtracks", "oscars", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_019",
        "text": "Ποια Αμερικανίδα τραγουδίστρια και ποπ σταρ αποκλήθηκε διεθνώς «Η Βασίλισσα της Ποπ» με επιτυχίες όπως «Like a Virgin» και «Vogue»;",
        "answers": [
            "Μαντόνα",
            "Σίντι Λόπερ",
            "Μαράια Κάρεϊ",
            "Σερ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Madonna είναι η γυναίκα καλλιτέχνιδα με τις μεγαλύτερες πωλήσεις δίσκων όλων των εποχών, ξεπερνώντας τα 300 εκατομμύρια.",
        "funFacts": [
            "Το 1996 πρωταγωνίστησε στον κινηματογράφο ως Εβίτα Περόν στην ταινία 'Evita', κερδίζοντας Χρυσή Σφαίρα Καλύτερης Ηθοποιού.",
            "Το Βιβλίο των Ρεκόρ Γκίνες την αναγνωρίζει επισήμως ως την πιο επιτυχημένη γυναίκα καλλιτέχνιδα στην ιστορία της μουσικής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%84%CF%8C%CE%BD%CE%B1_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%85%CE%B4%CE%AF%CF%83%CF%84%CF%81%CE%B9%CE%B1)",
        "locale": "el-GR",
        "tags": ["madonna", "pop", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_020",
        "text": "Ποιος Ιταλός συνθέτης της περιόδου του μπαρόκ συνέθεσε το παγκοσμίου φήμης σύνολο τεσσάρων κοντσέρτων για βιολί «Οι Τέσσερις Εποχές»;",
        "answers": [
            "Τζοακίνο Ροσσίνι",
            "Αντόνιο Βιβάλντι",
            "Τζουζέπε Βέρντι",
            "Τζάκομο Πουτσίνι"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Antonio Vivaldi συνέθεσε τις 'Τέσσερις Εποχές' γύρω στο 1720, αποτυπώνοντας μουσικά τους ήχους της φύσης κάθε εποχής.",
        "funFacts": [
            "Ήταν χειροτονημένος καθολικός ιερέας και έφερε το παρατσούκλι 'Il Prete Rosso' (Ο Κόκκινος Παπάς) εξαιτίας των κόκκινων μαλλιών του.",
            "Εργάστηκε για πολλά χρόνια ως δάσκαλος μουσικής στο ορφανοτροφείο Ospedale della Pietà στη Βενετία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%8C%CE%BD%CE%B9%CE%BF_%CE%92%CE%B9%CE%B2%CE%AC%CE%BB%CE%BD%CF%84%CE%B9",
        "locale": "el-GR",
        "tags": ["vivaldi", "classical", "baroque", "violin"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_021",
        "text": "Ποιο παραδοσιακό τοξωτό μουσικό όργανο με απιοειδές (αχλαδόσχημο) σώμα αποτελεί το κατεξοχήν μουσικό σύμβολο της Κρήτης;",
        "answers": [
            "Ποντιακή λύρα",
            "Βιολί",
            "Κρητική λύρα",
            "Κανονάκι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η κρητική λύρα είναι τρίχορδο τοξωτό όργανο που συνοδεύει παραδοσιακά τους κρητικούς χορούς και τις μαντινάδες.",
        "funFacts": [
            "Σε αντίθεση με το βιολί, οι χορδές της λύρας δεν πιέζονται πάνω στην ταστιέρα με το νύχι, αλλά ακουμπούν στο πλάι από τα νύχια των δακτύλων.",
            "Συνήθως παίζεται σε μουσικό ζευγάρι με το κρητικό λαούτο, το οποίο κρατά τον ρυθμό και την αρμονική βάση."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%81%CE%B7%CF%84%CE%B9%CE%BA%CE%AE_%CE%BB%CF%8D%CF%81%CE%B1",
        "locale": "el-GR",
        "tags": ["instruments", "crete", "folk-music", "tradition"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_022",
        "text": "Ποιος θρυλικός Αμερικανός τρομπετίστας και τραγουδιστής της τζαζ έμεινε στην ιστορία για τη χαρακτηριστική βραχνή φωνή του και το «What a Wonderful World»;",
        "answers": [
            "Μάιλς Ντέιβις",
            "Τζον Κολτρέιν",
            "Ντιουκ Έλινγκτον",
            "Λούις Άρμστρονγκ"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Louis Armstrong, γνωστός και ως Satchmo, υπήρξε η πιο επιδραστική μορφή στη διαμόρφωση της τζαζ ως σολιστικής τέχνης.",
        "funFacts": [
            "Γεννήθηκε στη Νέα Ορλεάνη της Λουιζιάνα, την κοιτίδα της παραδοσιακής τζαζ μουσικής.",
            "Καθιέρωσε το 'scat singing', δηλαδή το φωνητικό τραγούδι χωρίς λέξεις με αυτοσχέδιες συλλαβές."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CF%8D%CE%B9%CF%82_%CE%86%CF%81%CE%BC%CF%83%CF%84%CF%81%CE%BF%CE%BD%CE%B3%CE%BA",
        "locale": "el-GR",
        "tags": ["jazz", "armstrong", "brass"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_023",
        "text": "Ποιος κορυφαίος συνθέτης του ρεμπέτικου και λαϊκού τραγουδιού έγραψε τη διαχρονική «Συννεφιασμένη Κυριακή» κατά τη διάρκεια της Κατοχής;",
        "answers": [
            "Βασίλης Τσιτσάνης",
            "Μάρκος Βαμβακάρης",
            "Απόστολος Καλδάρας",
            "Γιάννης Παπαϊωάννου"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Βασίλης Τσιτσάνης θεωρείται ο αναμορφωτής του ελληνικού λαϊκού τραγουδιού, γεφυρώνοντας το παλιό ρεμπέτικο με τη σύγχρονη λαϊκή μουσική.",
        "funFacts": [
            "Γεννήθηκε στα Τρίκαλα το 1915 και έγραψε τη 'Συννεφιασμένη Κυριακή' στη Θεσσαλονίκη την περίοδο της γερμανικής κατοχής.",
            "Έφυγε από τη ζωή την ημέρα των γενεθλίων του, στις 18 Ιανουαρίου 1984, στο Λονδίνο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B7%CF%82_%CE%A4%CF%83%CE%B9%CF%84%CF%83%CE%AC%CE%BD%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["tsitsanis", "rebetiko", "laiko", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_024",
        "text": "Ποιο σύμβολο σχεδιάζεται στην αρχή του μουσικού πενταγράμμου και ορίζει τη θέση της νότας Σολ στη δεύτερη γραμμή;",
        "answers": [
            "Κλειδί του Φα",
            "Κλειδί του Σολ",
            "Κλειδί του Ντο",
            "Δίεση"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το κλειδί του Σολ (G-clef) χρησιμοποιείται για όργανα με υψηλό τονικό ύψος, όπως το βιολί, το φλάουτο και το δεξί χέρι του πιάνου.",
        "funFacts": [
            "Η χαρακτηριστική καμπύλη του σχεδιάζεται γύρω από τη δεύτερη γραμμή του πενταγράμμου, δίνοντάς της το όνομα Σολ.",
            "Εξελίχθηκε ιστορικά από το καλλιγραφικό λατινικό γράμμα G, το οποίο υποδηλώνει τη νότα Σολ στο δυτικό σύστημα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%B5%CE%B9%CE%B4%CE%AF_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "locale": "el-GR",
        "tags": ["music-theory", "notation", "education"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_025",
        "text": "Ποιο συγκρότημα grunge ροκ από το Σιάτλ, με ηγέτη τον Kurt Cobain, κυκλοφόρησε το επαναστατικό άλμπουμ «Nevermind» το 1991;",
        "answers": [
            "Pearl Jam",
            "Soundgarden",
            "Nirvana",
            "Alice in Chains"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Nirvana άλλαξαν την πορεία της ροκ μουσικής στις αρχές των 90s, με το 'Smells Like Teen Spirit' να αποτελεί ύμνο της Generation X.",
        "funFacts": [
            "Το εξώφυλλο του 'Nevermind' απεικονίζει ένα μωρό να κολυμπά κάτω από το νερό προς ένα χαρτονόμισμα του ενός δολαρίου.",
            "Ο ντράμερ του συγκροτήματος, Dave Grohl, ίδρυσε αργότερα τους άκρως επιτυχημένους Foo Fighters."
        ],
        "source": "https://el.wikipedia.org/wiki/Nirvana",
        "locale": "el-GR",
        "tags": ["nirvana", "grunge", "rock", "cobain"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_026",
        "text": "Ποια σπουδαία Αμερικανίδα τραγουδίστρια ερμήνευσε τη θρυλική διασκευή του «I Will Always Love You» για το soundtrack της ταινίας «Ο Σωματοφύλακας»;",
        "answers": [
            "Σελίν Ντιόν",
            "Μαράια Κάρεϊ",
            "Αρίθα Φράνκλιν",
            "Γουίτνεϊ Χιούστον"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Whitney Houston πρωταγωνίστησε στην ταινία 'The Bodyguard' (1992) δίπλα στον Kevin Costner, σημειώνοντας τεράστια επιτυχία.",
        "funFacts": [
            "Το 'I Will Always Love You' είχε γραφτεί και πρωτοκυκλοφορήσει από τη διάσημη σταρ της κάντρι Dolly Parton το 1974.",
            "Το soundtrack της ταινίας πούλησε πάνω από 45 εκατομμύρια αντίτυπα και παραμένει το εμπορικότερο soundtrack όλων των εποχών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%85%CE%AF%CF%84%CE%BD%CE%B5%CF%8A_%CE%A7%CE%B9%CE%BF%CF%8D%CF%83%CF%84%CE%BF%CE%BD",
        "locale": "el-GR",
        "tags": ["whitney-houston", "pop", "soundtracks", "ballad"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_027",
        "text": "Ποιο βρετανικό progressive rock συγκρότημα δημιούργησε τα αριστουργηματικά θεματικά άλμπουμ «The Dark Side of the Moon» και «The Wall»;",
        "answers": [
            "Pink Floyd",
            "Genesis",
            "Yes",
            "King Crimson"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Pink Floyd ξεχώρισαν για την πρωτοποριακή χρήση ηχητικών εφέ, τους φιλοσοφικούς στίχους και τα περίτεχνα οπτικά εφέ στις συναυλίες τους.",
        "funFacts": [
            "Το άλμπουμ 'The Dark Side of the Moon' (1973) παρέμεινε στα αμερικανικά charts του Billboard για περισσότερες από 900 εβδομάδες (πάνω από 17 χρόνια).",
            "Το χαρακτηριστικό πρίσμα που διαθλά το λευκό φως σε ουράνιο τόξο στο εξώφυλλο του άλμπουμ σχεδιάστηκε από την ομάδα Hipgnosis."
        ],
        "source": "https://el.wikipedia.org/wiki/Pink_Floyd",
        "locale": "el-GR",
        "tags": ["pink-floyd", "rock", "progressive-rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_028",
        "text": "Από πόσες οριζόντιες παράλληλες γραμμές αποτελείται ένα τυπικό μουσικό πεντάγραμμο;",
        "answers": [
            "4",
            "5",
            "6",
            "7"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το πεντάγραμμο αποτελείται από 5 οριζόντιες παράλληλες γραμμές και 4 ίσα διαστήματα ανάμεσά τους, όπου σημειώνονται οι μουσικοί φθόγγοι.",
        "funFacts": [
            "Η αρίθμηση των γραμμών και των διαστημάτων στο πεντάγραμμο γίνεται πάντα από κάτω προς τα πάνω.",
            "Η εισαγωγή των γραμμών για τη μουσική σημειογραφία αποδίδεται στον Ιταλό μοναχό και θεωρητικό Γκουίντο ντ' Αρέτσο τον 11ο αιώνα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CE%BD%CF%84%CE%AC%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%BF",
        "locale": "el-GR",
        "tags": ["music-theory", "notation", "education"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_029",
        "text": "Ποιος μεγάλος Ρώσος συνθέτης της ρομαντικής περιόδου συνέθεσε τη μουσική για τα κλασικά μπαλέτα «Η Λίμνη των Κύκνων» και «Ο Καρυοθραύστης»;",
        "answers": [
            "Σεργκέι Ραχμάνινοφ",
            "Ιγκόρ Στραβίνσκι",
            "Πιοτρ Ίλιτς Τσαϊκόφσκι",
            "Νικολάι Ρίμσκι-Κόρσακοφ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Pyotr Ilyich Tchaikovsky υπήρξε ο πρώτος Ρώσος συνθέτης που απέκτησε διαρκή διεθνή απήχηση με τις συμφωνίες, τα κοντσέρτα και τα μπαλέτα του.",
        "funFacts": [
            "Στην περίφημη 'Εισαγωγή 1812' που συνέθεσε, η παρτιτούρα περιλαμβάνει πραγματικούς κανονιοβολισμούς κατά την κορύφωση του έργου.",
            "Το μπαλέτο 'Ο Καρυοθραύστης' αποτελεί την πιο πολυπαιγμένη χριστουγεννιάτικη παράσταση κλασικού χορού σε όλο τον κόσμο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CE%BF%CF%84%CF%81_%CE%88%CE%BB%CE%B9%CF%84%CF%83_%CE%A4%CF%83%CE%B1%CF%8A%CE%BA%CF%8C%CF%86%CF%83%CE%BA%CE%B9",
        "locale": "el-GR",
        "tags": ["tchaikovsky", "ballet", "classical", "russia"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_030",
        "text": "Ποιος σπουδαίος Έλληνας ερμηνευτής τραγούδησε το καθηλωτικό ζεϊμπέκικο «Ρόζα» σε σύνθεση του Θάνου Μικρούτσικου και στίχους του Άλκη Αλκαίου;",
        "answers": [
            "Στέλιος Καζαντζίδης",
            "Στράτος Διονυσίου",
            "Γιώργος Νταλάρας",
            "Δημήτρης Μητροπάνος"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Δημήτρης Μητροπάνος σφράγισε με τη δωρική φωνή του το τραγούδι 'Ρόζα' στον δίσκο 'Στου αιώνα την παράγκα' το 1996.",
        "funFacts": [
            "Το τραγούδι είχε γραφτεί σχεδόν είκοσι χρόνια νωρίτερα, αλλά περίμενε στο συρτάρι του συνθέτη μέχρι να βρεθεί η κατάλληλη στιγμή και φωνή.",
            "Ο Μητροπάνος ξεκίνησε την καριέρα του στη δεκαετία του 1960 έχοντας στο πλευρό του τον Γρηγόρη Μπιθικώτση και τον Γιώργο Ζαμπέτα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B7%CE%BC%CE%AE%CF%84%CF%81%CE%B7%CF%82_%CE%9C%CE%B7%CF%84%CF%81%CE%BF%CF%80%CE%AC%CE%BD%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["mitropanos", "laiko", "zeibekiko", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_031",
        "text": "Ποιο πνευστό μουσικό όργανο κατασκευασμένο από ορείχαλκο, αλλά κατατασσόμενο στα ξύλινα πνευστά λόγω επιστομίου, εφηύρε ο Adolphe Sax το 1840;",
        "answers": [
            "Σαξόφωνο",
            "Τρομπέτα",
            "Τρομπόνι",
            "Τούμπα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το σαξόφωνο εφευρέθηκε από τον Βέλγο οργανοποιό Adolphe Sax και έγινε το κατεξοχήν σολιστικό όργανο της σύγχρονης τζαζ.",
        "funFacts": [
            "Αν και είναι φτιαγμένο από μέταλλο, κατατάσσεται στα ξύλινα πνευστά επειδή ο ήχος παράγεται από παλλόμενη ξύλινη γλωττίδα (καλάμι).",
            "Υπάρχει σε διάφορα μεγέθη, με τα πιο διαδεδομένα να είναι το άλτο, το τενόρο, το σοπράνο και το βαρύτονο σαξόφωνο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%BE%CF%8C%CF%86%CF%89%CE%BD%CE%BF",
        "locale": "el-GR",
        "tags": ["saxophone", "instruments", "jazz", "brass"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_032",
        "text": "Ποιος Καναδός ποπ τραγουδιστής ανακαλύφθηκε από βίντεο στο YouTube και γνώρισε παγκόσμια υστερία σε εφηβική ηλικία με το σινγκλ «Baby»;",
        "answers": [
            "Σον Μέντες",
            "Τζάστιν Μπίμπερ",
            "Ντρέικ",
            "The Weeknd"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Justin Bieber υπέγραψε δισκογραφικό συμβόλαιο το 2008 αφού ανακαλύφθηκε από τον μάνατζερ Scooter Braun μέσω βίντεο στο YouTube.",
        "funFacts": [
            "Το βιντεοκλίπ του τραγουδιού 'Baby' (2010) υπήρξε για πολλά χρόνια το βίντεο με τις περισσότερες προβολές και dislikes στην ιστορία του YouTube.",
            "Έγινε ο νεότερος σόλο καλλιτέχνης στην ιστορία με 7 άλμπουμ στο νούμερο ένα του αμερικανικού Billboard 200, καταρρίπτοντας το ρεκόρ του Elvis Presley."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AC%CF%83%CF%84%CE%B9%CE%BD_%CE%9C%CF%80%CE%AF%CE%BC%CF%80%CE%B5%CF%81",
        "locale": "el-GR",
        "tags": ["bieber", "pop", "artists"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_033",
        "text": "Ποιος κορυφαίος Αμερικανός ράπερ πρωταγωνίστησε στην αυτοβιογραφική ταινία «8 Mile» και κέρδισε Όσκαρ Τραγουδιού για το «Lose Yourself»;",
        "answers": [
            "Snoop Dogg",
            "Jay-Z",
            "Eminem",
            "50 Cent"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Marshall Mathers, γνωστός επαγγελματικά ως Eminem, είναι ένας από τους πιο επιτυχημένους σε πωλήσεις καλλιτέχνες όλων των εποχών.",
        "funFacts": [
            "Το 'Lose Yourself' (2002) ήταν το πρώτο χιπ χοπ τραγούδι στην ιστορία που κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού.",
            "Δεν παρέστη στην 75η τελετή απονομής των Όσκαρ για να παραλάβει το βραβείο, καθώς κοιμόταν στο σπίτι του με την κόρη του."
        ],
        "source": "https://el.wikipedia.org/wiki/Eminem",
        "locale": "el-GR",
        "tags": ["eminem", "hip-hop", "rap", "oscars"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_034",
        "text": "Ποια διάσημη Ελληνίδα τραγουδίστρια με τεράστια διεθνή καριέρα έχει ως χαρακτηριστικό γνώρισμα της εμφάνισής της τα μαύρα κοκάλινα γυαλιά;",
        "answers": [
            "Μαρινέλλα",
            "Χάρις Αλεξίου",
            "Βίκυ Λέανδρος",
            "Νάνα Μούσχουρη"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Νάνα Μούσχουρη έχει πουλήσει περισσότερους από 300 εκατομμύρια δίσκους παγκοσμίως τραγουδώντας σε δεκάδες διαφορετικές γλώσσες.",
        "funFacts": [
            "Υπήρξε πρέσβειρα καλής θελήσεως της UNICEF και εκλέχθηκε ευρωβουλευτής το 1994.",
            "Το τραγούδι της 'Weiße Rosen aus Athen' (Λευκά ρόδα από την Αθήνα) πούλησε πάνω από 1,5 εκατομμύριο αντίτυπα μόνο στη Γερμανία μέσα σε έξι μήνες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AC%CE%BD%CE%B1_%CE%9C%CE%BF%CF%8D%CF%83%CF%87%CE%BF%CF%85%CF%81%CE%B7",
        "locale": "el-GR",
        "tags": ["mouskouri", "greek-music", "international", "singers"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_035",
        "text": "Ποιο γαλλικό ντουέτο ηλεκτρονικής μουσικής εμφανιζόταν πάντοτε δημόσια με ρομποτικές μάσκες και σημείωσε παγκόσμια επιτυχία με το «Get Lucky»;",
        "answers": [
            "Daft Punk",
            "Justice",
            "Air",
            "The Chemical Brothers"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Guy-Manuel de Homem-Christo και Thomas Bangalter σχημάτισαν τους Daft Punk στο Παρίσι το 1993, καθορίζοντας τη σύγχρονη house σκηνή.",
        "funFacts": [
            "Το άλμπουμ τους 'Random Access Memories' (2013) απέσπασε πέντε βραβεία Grammy, ανάμεσα στα οποία και το Άλμπουμ της Χρονιάς.",
            "Ανακοίνωσαν τη διάλυσή τους το 2021 μέσα από ένα αινιγματικό βίντεο διάρκειας 8 λεπτών με τίτλο 'Epilogue'."
        ],
        "source": "https://el.wikipedia.org/wiki/Daft_Punk",
        "locale": "el-GR",
        "tags": ["daft-punk", "electronic", "french-house"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_036",
        "text": "Ποιος Πολωνός συνθέτης και βιρτουόζος πιανίστας της ρομαντικής εποχής συνέθεσε αμέτρητα νυχτερινά (nocturnes), μαζούρκες και βαλς για πιάνο;",
        "answers": [
            "Φραντς Λιστ",
            "Φρεντερίκ Σοπέν",
            "Ρόμπερτ Σούμαν",
            "Γιοχάνες Μπραμς"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Frédéric Chopin αφιέρωσε σχεδόν το σύνολο του συνθετικού του έργου στο σόλο πιάνο, αναδεικνύοντας τη λυρική και τεχνική του εκφραστικότητα.",
        "funFacts": [
            "Πέρασε μεγάλο μέρος της ζωής του στο Παρίσι και διατηρούσε σχέση με τη διάσημη Γαλλίδα συγγραφέα Γεωργία Σάνδη (George Sand).",
            "Παρότι πέθανε και ετάφη στο Παρίσι, σύμφωνα με την τελευταία του επιθυμία η καρδιά του μεταφέρθηκε και φυλάσσεται στη Βαρσοβία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%81%CE%B5%CE%BD%CF%84%CE%B5%CF%81%CE%AF%CE%BA_%CE%A3%CE%BF%CF%80%CE%AD%CE%BD",
        "locale": "el-GR",
        "tags": ["chopin", "classical", "piano", "romanticism"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_037",
        "text": "Ποιο αυστραλιανό hard rock συγκρότημα, με τον κιθαρίστα Angus Young να φορά στολή μαθητή, κυκλοφόρησε τον ύμνο «Highway to Hell»;",
        "answers": [
            "Guns N' Roses",
            "Iron Maiden",
            "AC/DC",
            "Black Sabbath"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι AC/DC ιδρύθηκαν στο Σίδνεϊ το 1973 από τα αδέλφια Malcolm και Angus Young και έγιναν πρωτοπόροι του hard rock ήχου.",
        "funFacts": [
            "Το άλμπουμ τους 'Back in Black' (1980) είναι το ροκ άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία (πάνω από 50 εκατομμύρια αντίτυπα).",
            "Το όνομά τους προέρχεται από τη συντομογραφία 'Alternate Current / Direct Current' (εναλλασσόμενο/συνεχές ρεύμα), την οποία είδαν σε ραπτομηχανή της αδερφής τους."
        ],
        "source": "https://el.wikipedia.org/wiki/AC/DC",
        "locale": "el-GR",
        "tags": ["acdc", "hard-rock", "australia", "bands"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_038",
        "text": "Ποιος σπουδαίος Έλληνας τραγουδιστής αποκλήθηκε «Η φωνή του λαού» και εξέφρασε όσο κανείς άλλος τον πόνο της ξενιτιάς και της εργατιάς;",
        "answers": [
            "Μανώλης Αγγελόπουλος",
            "Πάνος Γαβαλάς",
            "Γρηγόρης Μπιθικώτσης",
            "Στέλιος Καζαντζίδης"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Στέλιος Καζαντζίδης αποτέλεσε τη σπουδαιότερη ανδρική φωνή του ελληνικού λαϊκού τραγουδιού του δεύτερου μισού του 20ού αιώνα.",
        "funFacts": [
            "Τραγούδησε κορυφαίες επιτυχίες όπως 'Υπάρχω', 'Δυο πόρτες έχει η ζωή' και 'Το ψωμί της ξενιτιάς'.",
            "Παρά τη λαοθάλασσα των θαυμαστών του, αποφάσισε να σταματήσει οριστικά τις ζωντανές εμφανίσεις σε νυχτερινά κέντρα ήδη από το 1965."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AD%CE%BB%CE%B9%CE%BF%CF%82_%CE%9A%CE%B1%CE%B6%CE%B1%CE%BD%CF%84%CE%B6%CE%AF%CE%B4%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["kazantzidis", "laiko", "greek-music", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_039",
        "text": "Ποια διάσημη Καναδέζα τραγουδίστρια ερμήνευσε το βραβευμένο με Όσκαρ τραγούδι «My Heart Will Go On» για την ταινία «Τιτανικός»;",
        "answers": [
            "Σελίν Ντιόν",
            "Σανάια Τουέιν",
            "Αβρίλ Λαβίν",
            "Αλάνις Μορισέτ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Céline Dion κατέκτησε την κορυφή των charts παγκοσμίως με το εμβληματικό τραγούδι της επικής ταινίας του James Cameron το 1997.",
        "funFacts": [
            "Αρχικά δεν ήθελε καθόλου να ηχογραφήσει το τραγούδι, αλλά πείστηκε από τον σύζυγο και μάνατζέρ της René Angélil να κάνει ένα δοκιμαστικό demo.",
            "Το 'My Heart Will Go On' πούλησε πάνω από 18 εκατομμύρια αντίτυπα και κέρδισε τέσσερα βραβεία Grammy εκτός από το Όσκαρ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B5%CE%BB%CE%AF%CE%BD_%CE%9D%CF%84%CE%B9%CF%8C%CE%BD",
        "locale": "el-GR",
        "tags": ["celine-dion", "soundtracks", "titanic", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_040",
        "text": "Πόσες χορδές έχει ένα κανονικό ακουστικό βιολί της κλασικής ορχήστρας;",
        "answers": [
            "3",
            "4",
            "5",
            "6"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το βιολί διαθέτει 4 χορδές κουρδισμένες σε πέμπτες: Σολ, Ρε, Λα, Μι (G, D, A, E).",
        "funFacts": [
            "Το δοξάρι του βιολιού περιέχει περίπου 150 έως 200 τρίχες που προέρχονται παραδοσιακά από ουρά αλόγου.",
            "Τα ιστορικά βιολιά που κατασκεύασε ο Αντόνιο Στραντιβάρι (Stradivarius) τον 17ο και 18ο αιώνα πωλούνται σήμερα για δεκάδες εκατομμύρια ευρώ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%BF%CE%BB%CE%AF",
        "locale": "el-GR",
        "tags": ["violin", "instruments", "classical", "strings"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_041",
        "text": "Ποιος Αμερικανός τραγουδοποιός και ροκ μουσικός είναι παγκοσμίως γνωστός με το προσωνύμιο «The Boss» (Το Αφεντικό);",
        "answers": [
            "Μπίλι Τζόελ",
            "Τομ Πέτι",
            "Μπρους Σπρίνγκστιν",
            "Τζον Μέλενκαμπ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Bruce Springsteen και η θρυλική E Street Band καθόρισαν το αμερικανικό heartland rock με άλμπουμ όπως 'Born to Run' και 'Born in the U.S.A.'.",
        "funFacts": [
            "Το άλμπουμ 'Born in the U.S.A.' (1984) έβγαλε επτά κορυφαία top-10 σινγκλ στα αμερικανικά charts, ισοφαρίζοντας το ρεκόρ του Michael Jackson.",
            "Οι συναυλίες του είναι διάσημες για την τρομερή τους διάρκεια, ξεπερνώντας συχνά τις 3,5 έως 4 ώρες συνεχούς παιξίματος."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%81%CE%BF%CF%85%CF%82_%CE%A3%CF%80%CF%81%CE%AF%CE%BD%CE%B3%CE%BA%CF%83%CF%84%CE%B9%CE%BD",
        "locale": "el-GR",
        "tags": ["springsteen", "rock", "the-boss", "usa"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_042",
        "text": "Ποιο αμερικανικό heavy metal συγκρότημα κυκλοφόρησε το πασίγνωστο ομώνυμο άλμπουμ («The Black Album») το 1991 με το τραγούδι «Enter Sandman»;",
        "answers": [
            "Megadeth",
            "Slayer",
            "Judas Priest",
            "Metallica"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Metallica ιδρύθηκαν στο Λος Άντζελες το 1981 από τον James Hetfield και τον Lars Ulrich και αποτελούν το πιο επιτυχημένο metal συγκρότημα στην ιστορία.",
        "funFacts": [
            "Το 'Black Album' έχει πουλήσει πάνω από 30 εκατομμύρια αντίτυπα παγκοσμίως, όντας το πιο επιτυχημένο metal άλμπουμ της σύγχρονης εποχής.",
            "Το 2013 έγιναν το πρώτο μουσικό συγκρότημα στην ιστορία που έπαιξε ζωντανή συναυλία και στις επτά ηπείρους της Γης μέσα σε ένα μόνο έτος, παίζοντας ακόμα και στην Ανταρκτική."
        ],
        "source": "https://el.wikipedia.org/wiki/Metallica",
        "locale": "el-GR",
        "tags": ["metallica", "metal", "heavy-metal", "rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_043",
        "text": "Ποια Αμερικανίδα τραγουδίστρια έγινε το μεγαλύτερο εφηβικό είδωλο της ποπ στα τέλη της δεκαετίας του 1990 με το τραγούδι «...Baby One More Time»;",
        "answers": [
            "Μπρίτνεϊ Σπίαρς",
            "Κριστίνα Αγκιλέρα",
            "Τζέσικα Σίμπσον",
            "Πινκ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Britney Spears έφερε επανάσταση στην εφηβική ποπ μουσική (teen pop) στα τέλη των 90s και στις αρχές των 2000s.",
        "funFacts": [
            "Ήταν μόλις 17 ετών όταν το ντεμπούτο άλμπουμ της έφτασε στην κορυφή των charts και έγινε διαμαντένιο στις ΗΠΑ.",
            "Το τραγούδι της 'Toxic' (2003) της χάρισε το πρώτο της βραβείο Grammy στην κατηγορία Best Dance Recording."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%81%CE%AF%CF%84%CE%BD%CE%B5%CF%8A_%CE%A3%CF%80%CE%AF%CE%B1%CF%81%CF%82",
        "locale": "el-GR",
        "tags": ["britney-spears", "pop", "90s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_044",
        "text": "Ποιος διάσημος Ιταλός τενόρος καθήλωσε τα πλήθη παγκοσμίως ως μέλος των «Τριών Τενόρων» και με την ανεπανάληπτη ερμηνεία του στο «Nessun dorma»;",
        "answers": [
            "Πλάθιντο Ντομίνγκο",
            "Λουτσιάνο Παβαρότι",
            "Χοσέ Καρέρας",
            "Αντρέα Μποτσέλι"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Luciano Pavarotti υπήρξε ένας από τους διασημότερους τενόρους όλων των εποχών, φέρνοντας την όπερα κοντά στο ευρύ λαϊκό κοινό.",
        "funFacts": [
            "Η συναυλία των 'Τριών Τενόρων' στη Ρώμη το 1990 με τους Domingo και Carreras κατέχει το ρεκόρ του εμπορικότερου άλμπουμ κλασικής μουσικής.",
            "Η τελευταία του δημόσια εμφάνιση έγινε στην τελετή έναρξης των Χειμερινών Ολυμπιακών Αγώνων του 2006 στο Τορίνο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CF%85%CF%84%CF%83%CE%B9%CE%AC%CE%BD%CE%BF_%CE%A0%CE%B1%CE%B2%CE%B1%CF%81%CF%8C%CF%84%CE%B9",
        "locale": "el-GR",
        "tags": ["pavarotti", "opera", "tenor", "classical"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_045",
        "text": "Ποιο ιρλανδικό ροκ συγκρότημα με ηγέτη τον τραγουδιστή Bono κυκλοφόρησε το κορυφαίο άλμπουμ «The Joshua Tree» (1987) με επιτυχίες όπως το «With or Without You»;",
        "answers": [
            "The Cranberries",
            "R.E.M.",
            "U2",
            "Oasis"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι U2 σχηματίστηκαν στο Δουβλίνο το 1976 και εξελίχθηκαν σε ένα από τα πιο επιτυχημένα και πολιτικοποιημένα ροκ γκρουπ στην ιστορία.",
        "funFacts": [
            "Έχουν κερδίσει συνολικά 22 βραβεία Grammy, περισσότερα από οποιοδήποτε άλλο ροκ συγκρότημα στην ιστορία του θεσμού.",
            "Η περιοδεία τους '360° Tour' (2009-2011) υπήρξε για πολλά χρόνια η πιο επικερδής συναυλιακή περιοδεία όλων των εποχών."
        ],
        "source": "https://el.wikipedia.org/wiki/U2",
        "locale": "el-GR",
        "tags": ["u2", "bono", "rock", "ireland"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_046",
        "text": "Ποια Αμερικανίδα σούπερ σταρ ξεκίνησε από το συγκρότημα Destiny's Child και έγινε η καλλιτέχνιδα με τα περισσότερα βραβεία Grammy στην ιστορία;",
        "answers": [
            "Ριάννα",
            "Αλίσια Κις",
            "Νίκι Μινάζ",
            "Μπιγιονσέ"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Beyoncé Knowles-Carter κατέχει το απόλυτο ρεκόρ των περισσότερων βραβείων Grammy στην ιστορία της μουσικής, ξεπερνώντας τα 32 τρόπαια.",
        "funFacts": [
            "Το 2008 κυκλοφόρησε το κομμάτι 'Single Ladies (Put a Ring on It)', του οποίου η χορογραφία έγινε ένα από τα πρώτα viral βίντεο στο διαδίκτυο.",
            "Είναι παντρεμένη με τον διάσημο ράπερ και μεγιστάνα της μουσικής βιομηχανίας Jay-Z από το 2008."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B9%CE%B3%CE%B9%CE%BF%CE%BD%CF%83%CE%AD",
        "locale": "el-GR",
        "tags": ["beyonce", "grammy", "pop", "rnb"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_047",
        "text": "Ποιος Γερμανός συνθέτης και οργανίστας θεωρείται ο μέγιστος εκπρόσωπος του μπαρόκ και έγραψε τα «Βρανδεμβούργια Κοντσέρτα»;",
        "answers": [
            "Γιόχαν Σεμπάστιαν Μπαχ",
            "Γκέοργκ Φρίντριχ Χαίντελ",
            "Γκέοργκ Φίλιπ Τέλεμαν",
            "Χάινριχ Συτς"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο J. S. Bach θεωρείται ακρογωνιαίος λίθος της δυτικής κλασικής μουσικής για την αρμονία και την πολυφωνική αντίστιξη των έργων του.",
        "funFacts": [
            "Πέρασε μεγάλο μέρος της καριέρας του ως κάντορας στην εκκλησία του Αγίου Θωμά στη Λειψία.",
            "Έκανε είκοσι παιδιά συνολικά από δύο γάμους, και αρκετοί από τους γιους του έγιναν επίσης διακεκριμένοι συνθέτες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CF%87%CE%B1%CE%BD_%CE%A3%CE%B5%CE%BC%CF%80%CE%AC%CF%83%CF%84%CE%B9%CE%B1%CE%BD_%CE%9C%CF%80%CE%B1%CF%87",
        "locale": "el-GR",
        "tags": ["bach", "baroque", "classical", "germany"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_048",
        "text": "Ποια Κολομβιανή τραγουδίστρια ερμήνευσε τον επίσημο ύμνο του Παγκοσμίου Κυπέλλου Ποδοσφαίρου 2010 «Waka Waka (This Time for Africa)»;",
        "answers": [
            "Τζένιφερ Λόπεζ",
            "Σακίρα",
            "Καμίλα Καμπέγιο",
            "Ροζαλία"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Shakira είναι η πιο επιτυχημένη Λατινοαμερικανίδα τραγουδίστρια όλων των εποχών, με επιτυχίες όπως 'Whenever, Wherever' και 'Hips Don\\'t Lie'.",
        "funFacts": [
            "Το βιντεοκλίπ του 'Waka Waka' ξεπέρασε τα 3 δισεκατομμύρια προβολές στο YouTube.",
            "Στα γυρίσματα του συγκεκριμένου βιντεοκλίπ γνώρισε τον Ισπανό ποδοσφαιριστή Ζεράρ Πικέ, με τον οποίο απέκτησε δύο παιδιά."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%BA%CE%AF%CF%81%CE%B1",
        "locale": "el-GR",
        "tags": ["shakira", "latin", "pop", "world-cup"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_049",
        "text": "Ποια σπουδαία Ελληνίδα ερμηνεύτρια και τραγουδοποιός, γνωστή χαϊδευτικά ως «Χαρούλα», τραγούδησε επιτυχίες όπως «Όλα σε θυμίζουν» και «Το τανγκό της Νεφέλης»;",
        "answers": [
            "Δήμητρα Γαλάνη",
            "Ελευθερία Αρβανιτάκη",
            "Χάρις Αλεξίου",
            "Άλκηστις Πρωτοψάλτη"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Χάρις Αλεξίου αποτελεί μία από τις πιο αγαπημένες και εμπορικά επιτυχημένες γυναικείες φωνές στην ιστορία της ελληνικής μουσικής.",
        "funFacts": [
            "Πρωτοεμφανίστηκε στη δισκογραφία τη δεκαετία του 1970 συμμετέχοντας στον ιστορικό δίσκο 'Μικρά Ασία' του Απόστολου Καλδάρα.",
            "Το 2020 ανακοίνωσε ότι σταματά τις ζωντανές μουσικές εμφανίσεις λόγω προβλημάτων στη φωνή της και στράφηκε με μεγάλη επιτυχία στο θέατρο και την τηλεόραση ('Maestro')."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CE%B9%CF%82_%CE%91%CE%BB%CE%B5%CE%BE%CE%AF%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["alexiou", "greek-music", "entechno", "singers"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_050",
        "text": "Ποιος τυφλός Αμερικανός τραγουδιστής, πιανίστας και συνθέτης της Motown κέρδισε 25 βραβεία Grammy και κυκλοφόρησε το «I Just Called to Say I Love You»;",
        "answers": [
            "Ρέι Τσαρλς",
            "Μάρβιν Γκέι",
            "Αλ Γκριν",
            "Στίβι Γουόντερ"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Stevie Wonder υπήρξε μουσικό παιδί-θαύμα και εξελίχθηκε σε έναν από τους πιο πολυτάλαντους καλλιτέχνες της σόουλ και ποπ μουσικής.",
        "funFacts": [
            "Έχασε την όρασή του λίγο μετά τη γέννησή του λόγω υπερβολικού οξυγόνου στη θερμοκοιτίδα.",
            "Το τραγούδι 'I Just Called to Say I Love You' (1984) για την ταινία 'The Woman in Red' του χάρισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AF%CE%B2%CE%B9_%CE%93%CE%BF%CF%85%CF%8C%CE%BD%CF%84%CE%B5%CF%81",
        "locale": "el-GR",
        "tags": ["stevie-wonder", "soul", "motown", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_051",
        "text": "Ποιος Βρετανός πιανίστας και συνθέτης έγραψε το «Rocket Man» και ερμήνευσε το «Candle in the Wind 1997» στη μνήμη της πριγκίπισσας Νταϊάνα;",
        "answers": [
            "Έλτον Τζον",
            "Ροντ Στιούαρτ",
            "Φιλ Κόλινς",
            "Τζορτζ Μάικλ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Sir Elton John είναι ένας από τους πιο επιτυχημένους μουσικούς στην ιστορία, έχοντας πουλήσει περισσότερους από 300 εκατομμύρια δίσκους.",
        "funFacts": [
            "Η έκδοση του 'Candle in the Wind' το 1997 έγινε το σινγκλ με τις ταχύτερες πωλήσεις στην ιστορία, ξεπερνώντας τα 33 εκατομμύρια αντίτυπα.",
            "Έγραψε τη μουσική για την εξαιρετικά επιτυχημένη ταινία κινουμένων σχεδίων 'Ο Βασιλιάς των Λιονταριών' (The Lion King) της Disney το 1994."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BB%CF%84%CE%BF%CE%BD_%CE%A4%CE%B6%CE%BF%CE%BD",
        "locale": "el-GR",
        "tags": ["elton-john", "pop", "piano", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_052",
        "text": "Ποιο βρετανικό συγκρότημα της Britpop με ηγέτες τα αδέλφια Noel και Liam Gallagher κυκλοφόρησε τον διαχρονικό ύμνο «Wonderwall» το 1995;",
        "answers": [
            "Blur",
            "Oasis",
            "Pulp",
            "The Verve"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Oasis σχηματίστηκαν στο Μάντσεστερ το 1991 και έγιναν το κορυφαίο συγκρότημα του κινήματος της britpop τη δεκαετία του 1990.",
        "funFacts": [
            "Το δεύτερο άλμπουμ τους '(What\\'s the Story) Morning Glory?' (1995) παραμένει ένα από τα πιο εμπορικά άλμπουμ όλων των εποχών στο Ηνωμένο Βασίλειο.",
            "Οι συνεχείς δημόσιες διαμάχες μεταξύ των δύο αδελφών οδήγησαν στη διάλυσή τους το 2009, πριν ανακοινώσουν την επανένωσή τους το 2024."
        ],
        "source": "https://el.wikipedia.org/wiki/Oasis",
        "locale": "el-GR",
        "tags": ["oasis", "britpop", "rock", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_053",
        "text": "Ποιος διάσημος Αυστριακός συνθέτης έμεινε στην ιστορία με το προσωνύμιο «Ο Βασιλιάς των Βαλς» συνθέτοντας τον «Γαλάζιο Δούναβη»;",
        "answers": [
            "Φραντς Σούμπερτ",
            "Γκούσταβ Μάλερ",
            "Γιόχαν Στράους ο νεότερος",
            "Άντον Μπρούκνερ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Johann Strauss II συνέθεσε πάνω από 500 έργα χορευτικής μουσικής, κυρίως βαλς και πόλκες, κάνοντας το βιεννέζικο βαλς παγκόσμια μόδα.",
        "funFacts": [
            "Ο 'Γαλάζιος Δούναβης' (An der schönen blauen Donau) γράφτηκε το 1866 και θεωρείται ο ανεπίσημος εθνικός ύμνος της Αυστρίας.",
            "Ο πατέρας του, επίσης Γιόχαν Στράους, ήταν διάσημος συνθέτης και είχε γράψει το περίφημο εμβατήριο 'Radetzky March'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CF%87%CE%B1%CE%BD_%CE%A3%CF%84%CF%81%CE%AC%CE%BF%CF%85%CF%82_(%CE%B3%CE%B9%CE%BF%CF%82)",
        "locale": "el-GR",
        "tags": ["strauss", "waltz", "classical", "vienna"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_054",
        "text": "Ποια εκκεντρική Αμερικανίδα τραγουδίστρια της ποπ έγινε διάσημη με το «Poker Face» και κέρδισε Όσκαρ Τραγουδιού για το ντουέτο «Shallow»;",
        "answers": [
            "Κέιτι Πέρι",
            "Μάιλι Σάιρους",
            "Κέσα",
            "Lady Gaga"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Stefani Joanne Angelina Germanotta, γνωστή ως Lady Gaga, πρωτοστάτησε στην ηλεκτροπόπ μουσική και απέσπασε διθυραμβικές κριτικές στην υποκριτική.",
        "funFacts": [
            "Το ψευδώνυμό της είναι εμπνευσμένο από το διάσημο τραγούδι των Queen 'Radio Ga Ga'.",
            "Πρωταγωνίστησε στην ταινία 'Ένα Αστέρι Γεννιέται' (A Star Is Born, 2018) δίπλα στον Μπράντλεϊ Κούπερ, κερδίζοντας το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού."
        ],
        "source": "https://el.wikipedia.org/wiki/Lady_Gaga",
        "locale": "el-GR",
        "tags": ["lady-gaga", "pop", "oscars", "artists"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_055",
        "text": "Ποιος σπουδαίος Κρητικός τραγουδιστής και λυράρης αποκλήθηκε «Αρχάγγελος της Κρήτης» και σημάδεψε με τη φωνή του τα γεγονότα του Πολυτεχνείου;",
        "answers": [
            "Νίκος Ξυλούρης",
            "Ψαραντώνης",
            "Κώστας Μουντάκης",
            "Θανάσης Σκορδαλός"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Νίκος Ξυλούρης συνδύασε μοναδικά την κρητική παραδοσιακή μουσική με το έντεχνο τραγούδι και τη μελοποιημένη ποίηση.",
        "funFacts": [
            "Γεννήθηκε στα Ανώγεια Μυλοποτάμου το 1936 και σε ηλικία μόλις 12 ετών απέκτησε την πρώτη του λύρα.",
            "Η παρουσία του μέσα στο Πολυτεχνείο το 1973 τραγουδώντας το ριζίτικο 'Πότε θα κάμει ξαστεριά' έμεινε ανεξίτηλη στην ελληνική ιστορία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%9E%CF%85%CE%BB%CE%BF%CF%8D%CF%81%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["xylouris", "crete", "folk-music", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_056",
        "text": "Ποια σύγχρονη Αμερικανίδα τραγουδίστρια έγραψε ιστορία στη μουσική βιομηχανία με την περιοδεία-φαινόμενο «The Eras Tour»;",
        "answers": [
            "Αριάνα Γκράντε",
            "Τέιλορ Σουίφτ",
            "Μπίλι Άιλις",
            "Σελένα Γκόμεζ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Taylor Swift είναι η πρώτη καλλιτέχνιδα που έχει κερδίσει τέσσερις φορές το βραβείο Grammy για το Άλμπουμ της Χρονιάς.",
        "funFacts": [
            "Η περιοδεία 'The Eras Tour' έγινε η πρώτη συναυλιακή περιοδεία στην ιστορία που ξεπέρασε το 1 δισεκατομμύριο δολάρια σε εισπράξεις.",
            "Ξεκίνησε την καριέρα της από τη μουσική κάντρι στο Νάσβιλ σε ηλικία 14 ετών, πριν μεταπηδήσει με τεράστια επιτυχία στην ποπ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AD%CE%B9%CE%BB%CE%BF%CF%81_%CE%A3%CE%BF%CF%85%CE%AF%CF%86%CF%84",
        "locale": "el-GR",
        "tags": ["taylor-swift", "pop", "eras-tour", "charts"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_057",
        "text": "Ποιο όργανο της συμφωνικής ορχήστρας ανήκει στην οικογένεια των ξύλινων πνευστών και παίζεται κρατώντας το οριζόντια προς τα δεξιά;",
        "answers": [
            "Όμποε",
            "Κλαρινέτο",
            "Φλάουτο",
            "Φαγκότο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το πλάγιο φλάουτο είναι πνευστό μουσικό όργανο όπου ο ήχος παράγεται από τη ροή του αέρα που προσκρούει στο χείλος της οπής φυσήματος.",
        "funFacts": [
            "Παρότι στα σύγχρονα όργανα κατασκευάζεται συνήθως από μέταλλο (ασήμι, νικέλιο ή χρυσό), κατατάσσεται παραδοσιακά στα ξύλινα πνευστά.",
            "Παλαιολιθικά φλάουτα κατασκευασμένα από οστά πτηνών και μαμούθ αποτελούν τα αρχαιότερα γνωστά μουσικά όργανα που ανακάλυψε η αρχαιολογία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%BB%CE%AC%CE%BF%CF%85%CF%84%CE%BF",
        "locale": "el-GR",
        "tags": ["flute", "woodwinds", "instruments", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_058",
        "text": "Ποιος Αμερικανός τραγουδοποιός και θρύλος της φολκ μουσικής τιμήθηκε το 2016 με το Νόμπελ Λογοτεχνίας;",
        "answers": [
            "Λέοναρντ Κοέν",
            "Πολ Σάιμον",
            "Νιλ Γιανγκ",
            "Μπομπ Ντίλαν"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Bob Dylan έγινε ο πρώτος μουσικός στην ιστορία που βραβεύτηκε με Νόμπελ Λογοτεχνίας για τους ποιητικούς του στίχους.",
        "funFacts": [
            "Τραγούδια του όπως το 'Blowin\\' in the Wind' και το 'The Times They Are a-Changin\\'' έγιναν ύμνοι του κινήματος για τα πολιτικά δικαιώματα.",
            "Το πραγματικό του όνομα είναι Robert Allen Zimmerman και γεννήθηκε στη Μινεσότα το 1941."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CE%BC%CF%80_%CE%9D%CF%84%CE%AF%CE%BB%CE%B1%CE%BD",
        "locale": "el-GR",
        "tags": ["bob-dylan", "folk", "nobel", "poetry"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_059",
        "text": "Ποιο βρετανικό συγκρότημα εναλλακτικής ροκ με τραγουδιστή τον Chris Martin κυκλοφόρησε παγκόσμιες επιτυχίες όπως «Yellow», «Fix You» και «Viva la Vida»;",
        "answers": [
            "Coldplay",
            "Muse",
            "Radiohead",
            "Snow Patrol"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Coldplay δημιουργήθηκαν στο Λονδίνο το 1996 και αποτελούν ένα από τα πιο εμπορικά επιτυχημένα μουσικά συγκροτήματα του 21ου αιώνα.",
        "funFacts": [
            "Όλα τα μέλη του συγκροτήματος γνωρίστηκαν κατά τη διάρκεια των φοιτητικών τους χρόνων στο University College London (UCL).",
            "Οι συναυλίες τους είναι γνωστές για τα φωτιζόμενα διαδραστικά βραχιόλια (Xylobands) που φορούν όλοι οι θεατές, δημιουργώντας ένα εντυπωσιακό φωτεινό σόου."
        ],
        "source": "https://el.wikipedia.org/wiki/Coldplay",
        "locale": "el-GR",
        "tags": ["coldplay", "rock", "alternative", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_060",
        "text": "Ποιος θρυλικός Αμερικανός τραγουδιστής, γνωστός και ως «Ol' Blue Eyes», σημάδεψε την ιστορία της φωνητικής τζαζ με το «My Way» και το «Fly Me to the Moon»;",
        "answers": [
            "Ντιν Μάρτιν",
            "Φρανκ Σινάτρα",
            "Τόνι Μπένετ",
            "Νατ Κινγκ Κόουλ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Frank Sinatra υπήρξε μία από τις πιο δημοφιλείς και επιδραστικές προσωπικότητες του 20ού αιώνα στη μουσική και τον κινηματογράφο.",
        "funFacts": [
            "Εκτός από τη μουσική, κέρδισε Όσκαρ Β' Ανδρικού Ρόλου το 1954 για την ερμηνεία του στην ταινία 'Όσο υπάρχουν άνθρωποι' (From Here to Eternity).",
            "Ήταν ο ηγέτης της περίφημης παρέας καλλιτεχνών του Χόλιγουντ και του Λας Βέγκας που έγινε γνωστή ως 'Rat Pack'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%81%CE%B1%CE%BD%CE%BA_%CE%A3%CE%B9%CE%BD%CE%AC%CF%84%CF%81%CE%B1",
        "locale": "el-GR",
        "tags": ["sinatra", "jazz", "swing", "vocal"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(questions)} questions to append.")
    validate_and_append('music', 'easy', 1, questions)

import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
    {
        "id": "music_easy_111",
        "text": "Ποια κορυφαία Αμερικανίδα τραγουδίστρια έμεινε στην ιστορία ως «Η Βασίλισσα της Σόουλ» (Queen of Soul) με τον διαχρονικό ύμνο «Respect»;",
        "answers": [
            "Αρίθα Φράνκλιν",
            "Νταϊάνα Ρος",
            "Νίνα Σιμόν",
            "Έτα Τζέιμς"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Aretha Franklin υπήρξε μία από τις πιο αναγνωρίσιμες φωνές του 20ού αιώνα και η πρώτη γυναίκα που εντάχθηκε στο Rock and Roll Hall of Fame (1987).",
        "funFacts": [
            "Τραγούδησε στην τελετή ορκωμοσίας τριών Αμερικανών προέδρων: του Jimmy Carter, του Bill Clinton και του Barack Obama.",
            "Κέρδισε συνολικά 18 βραβεία Grammy κατά τη διάρκεια της πολυετούς μουσικής της διαδρομής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CF%81%CE%AF%CE%B8%CE%B1_%CE%A6%CF%81%CE%AC%CE%BD%CE%BA%CE%BB%CE%B9%CE%BD",
        "locale": "el-GR",
        "tags": ["aretha-franklin", "soul", "legends", "rnb"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_112",
        "text": "Ποιος μεγάλος Έλληνας συνθέτης του λαϊκού τραγουδιού υπέγραψε τον ιστορικό δίσκο «Μικρά Ασία» (1972) και το κλασικό «Νύχτωσε χωρίς φεγγάρι»;",
        "answers": [
            "Γιώργος Ζαμπέτας",
            "Απόστολος Καλδάρας",
            "Άκης Πάνου",
            "Χρήστος Νικολόπουλος"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Απόστολος Καλδάρας υπήρξε από τους σπουδαιότερους λαϊκούς δημιουργούς, γράφοντας αξέχαστες μελωδίες για τον Καζαντζίδη, τον Μπιθικώτση, τον Νταλάρα και την Αλεξίου.",
        "funFacts": [
            "Ο δίσκος 'Μικρά Ασία' σε στίχους Πυθαγόρα κυκλοφόρησε για τα 50 χρόνια από τη Μικρασιατική Καταστροφή και αποτέλεσε τον πρώτο επίσημα χρυσό δίσκο στην ελληνική δισκογραφία.",
            "Το τραγούδι 'Νύχτωσε χωρίς φεγγάρι' γράφτηκε το 1947 και είχε απαγορευτεί αρχικά από τη λογοκρισία λόγω των υπαινιγμών του για τον Εμφύλιο Πόλεμο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CF%8C%CF%83%CF%84%CE%BF%CE%BB%CE%BF%CF%82_%CE%9A%CE%B1%CE%BB%CE%B4%CE%AC%CF%81%CE%B1%CF%82",
        "locale": "el-GR",
        "tags": ["kaldaras", "laiko", "greek-music", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_113",
        "text": "Ποιο μικρό πνευστό μουσικό όργανο τσέπης παίζεται τοποθετώντας τα χείλη πάνω σε οπές και εισπνέοντας ή εκπνέοντας αέρα (γνωστό και ως φυσαρμόνικα);",
        "answers": [
            "Φλογέρα",
            "Μελόντικα",
            "Φυσαρμόνικα",
            "Όκαρινα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η φυσαρμόνικα είναι αερόφωνο όργανο με ελεύθερες μεταλλικές γλωττίδες που συνδέθηκε άρρηκτα με τα αμερικανικά μπλουζ και τη φολκ μουσική.",
        "funFacts": [
            "Καλλιτέχνες όπως ο Bob Dylan και ο Neil Young τη στερέωναν σε ειδική βάση στον λαιμό τους για να μπορούν να παίζουν ταυτόχρονα κιθάρα.",
            "Ήταν το πρώτο μουσικό όργανο που παίχτηκε ποτέ στο διάστημα, όταν ο αστροναύτης Walter Schirra έπαιξε το 'Jingle Bells' στην αποστολή Gemini 6A το 1965."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%85%CF%83%CE%B1%CF%81%CE%BC%CF%8C%CE%BD%CE%B9%CE%BA%CE%B1",
        "locale": "el-GR",
        "tags": ["harmonica", "instruments", "blues", "folk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_114",
        "text": "Ποια επική ροκ μπαλάντα των Guns N' Roses με εκτενές σόλο πιάνου από τον Axl Rose και ιστορικό σόλο κιθάρας από τον Slash στην έρημο διαρκεί σχεδόν 9 λεπτά;",
        "answers": [
            "Don't Cry",
            "Patience",
            "Civil War",
            "November Rain"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'November Rain' συμπεριλήφθηκε στο άλμπουμ 'Use Your Illusion I' (1991) και αποτελεί ένα από τα πιο διάσημα ροκ τραγούδια όλων των εποχών.",
        "funFacts": [
            "Παραμένει το μεγαλύτερο σε διάρκεια τραγούδι στην ιστορία που κατάφερε να μπει στο top-10 του αμερικανικού Billboard Hot 100.",
            "Το κόστος παραγωγής του κινηματογραφικού του βιντεοκλίπ ξεπέρασε το 1,5 εκατομμύριο δολάρια, ποσό εξωπραγματικό για την εποχή του."
        ],
        "source": "https://el.wikipedia.org/wiki/November_Rain",
        "locale": "el-GR",
        "tags": ["guns-n-roses", "rock", "ballad", "slash"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_115",
        "text": "Ποιος αγαπημένος Έλληνας συνθέτης έγραψε αριστουργηματικά τραγούδια όπως «Το ακορντεόν», «Ο δρόμος» και «Τσε Γκεβάρα», φεύγοντας πρόωρα από τη ζωή το 1982;",
        "answers": [
            "Μάνος Λοΐζος",
            "Θάνος Μικρούτσικος",
            "Δήμος Μούτσης",
            "Λουκιανός Κηλαηδόνης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Μάνος Λοΐζος υπήρξε από τους πιο ευαίσθητους και μελωδικούς συνθέτες του πολιτικού και κοινωνικού τραγουδιού στην Ελλάδα.",
        "funFacts": [
            "Γεννήθηκε στην Αλεξάνδρεια της Αιγύπτου από Κύπριους γονείς πριν εγκατασταθεί στην Αθήνα για σπουδές.",
            "Η φράση 'Δεν θα περάσει ο φασισμός' από 'Το ακορντεόν' έγινε διαχρονικό σύνθημα σε μαθητικές και εργατικές πορείες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%BD%CE%BF%CF%82_%CE%9B%CE%BF%CE%90%CE%B6%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["loizos", "greek-music", "entechno", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_116",
        "text": "Ποιο παγκόσμιο λάτιν-ποπ χιτ της Shakira με τη συμμετοχή του Wyclef Jean κατέκτησε την πρώτη θέση σε πάνω από 50 χώρες το 2006;",
        "answers": [
            "Whenever, Wherever",
            "Hips Don't Lie",
            "La Tortura",
            "She Wolf"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Hips Don't Lie' συνδύασε ρυθμούς ρεγκετόν και κολομβιανής κούμπια, αποτελώντας ένα από τα εμπορικότερα σινγκλ του 21ου αιώνα.",
        "funFacts": [
            "Έγινε το πρώτο νούμερο ένα σινγκλ της Shakira στο αμερικανικό Billboard Hot 100.",
            "Ο τίτλος προήλθε από μια συνήθεια της Shakira στο στούντιο να καταλαβαίνει αν ένας ρυθμός λειτουργεί από το αν την παρακινεί αυθόρμητα να κουνήσει τους γοφούς της."
        ],
        "source": "https://el.wikipedia.org/wiki/Hips_Don%27t_Lie",
        "locale": "el-GR",
        "tags": ["shakira", "latin", "pop", "hits"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_117",
        "text": "Ποιο κρουστό μουσικό όργανο αποτελείται από ξύλινες πλάκες διαφορετικού μεγέθους διατεταγμένες σαν πλήκτρα πιάνου και παίζεται χτυπώντας τες με ειδικές μπαγκέτες;",
        "answers": [
            "Μαρίμπα",
            "Μεταλλόφωνο",
            "Ξυλόφωνο",
            "Τσελέστα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το ξυλόφωνο παράγει έναν ξηρό, σύντομο και διαπεραστικό ήχο όταν οι ξύλινες ράβδοι (συνήθως από παλίσανδρο) χτυπιούνται με σκληρές μπαγκέτες.",
        "funFacts": [
            "Η λέξη προέρχεται απευθείας από τις ελληνικές λέξεις 'ξύλον' και 'φωνή'.",
            "Χρησιμοποιείται συχνά στην ορχηστρική μουσική για να απεικονίσει ανατριχιαστικούς ή παιχνιδιάρικους ήχους, όπως ο χορός των σκελετών στο έργο 'Danse Macabre' του Saint-Saëns."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9E%CF%85%CE%BB%CF%8C%CF%86%CF%89%CE%BD%CE%BF",
        "locale": "el-GR",
        "tags": ["xylophone", "instruments", "percussion", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_118",
        "text": "Ποια ρομαντική μπαλάντα του Elton John από την ταινία της Disney «Ο Βασιλιάς των Λιονταριών» (1994) κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού;",
        "answers": [
            "Circle of Life",
            "Hakuna Matata",
            "Your Song",
            "Can You Feel the Love Tonight"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το τραγούδι συντέθηκε από τον Elton John σε στίχους του Tim Rice και αποτέλεσε τεράστια εμπορική επιτυχία παγκοσμίως.",
        "funFacts": [
            "Αρχικά η Disney σχεδίαζε να τραγουδηθεί αποκλειστικά από τους χαρακτήρες Τιμόν και Πούμπα σε κωμικό τόνο, αλλά ο Elton John επέμεινε να παραμείνει σοβαρό ερωτικό θέμα.",
            "Κέρδισε τόσο το Όσκαρ όσο και το βραβείο Grammy Καλύτερης Ανδρικής Ποπ Φωνητικής Ερμηνείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Can_You_Feel_the_Love_Tonight",
        "locale": "el-GR",
        "tags": ["elton-john", "disney", "lion-king", "oscars"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_119",
        "text": "Ποια δυναμική Ελληνίδα ερμηνεύτρια, γεννημένη στην Αλεξάνδρεια, απογείωσε τη συνεργασία της με τον Σταμάτη Κραουνάκη και τη Λίνα Νικολακοπούλου σε δίσκους όπως «Κυκλοφορώ κι οπλοφορώ»;",
        "answers": [
            "Άλκηστις Πρωτοψάλτη",
            "Δήμητρα Γαλάνη",
            "Ελευθερία Αρβανιτάκη",
            "Τάνια Τσανακλίδου"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Άλκηστις Πρωτοψάλτη (Άλκηστις Σεβαστή Αττικιουζέλ) ξεχωρίζει για τη σκηνική της ενέργεια και τη μοναδική εκφραστική της δύναμη.",
        "funFacts": [
            "Στα νεανικά της χρόνια ασχολήθηκε με τον αθλητισμό και υπήρξε διακεκριμένη αθλήτρια στον στίβο (100μ. και 200μ.).",
            "Τον Απρίλιο του 2020, εν μέσω της πανδημίας, πραγματοποίησε μια συγκινητική συναυλία πάνω σε κινούμενη ανοιχτή πλατφόρμα φορτηγού στους δρόμους της Αθήνας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%BA%CE%B7%CF%83%CF%84%CE%B9%CF%82_%CE%A0%CF%81%CF%89%CF%84%CE%BF%CF%88%CE%AC%CE%BB%CF%84%CE%B7",
        "locale": "el-GR",
        "tags": ["protopsalti", "greek-music", "entechno", "singers"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_120",
        "text": "Ποιο παγκόσμιο χριστουγεννιάτικο ποπ τραγούδι κυκλοφόρησαν οι Wham! το 1984, γραμμένο εξ ολοκλήρου από τον George Michael στο παιδικό του δωμάτιο;",
        "answers": [
            "Careless Whisper",
            "Last Christmas",
            "Wake Me Up Before You Go-Go",
            "Club Tropicana"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Last Christmas' αποτελεί ένα από τα πιο πολυακουσμένα τραγούδια κάθε εορταστική περίοδο σε ολόκληρο τον πλανήτη.",
        "funFacts": [
            "Όλα τα έσοδα του σινγκλ από την αρχική του κυκλοφορία δωρήθηκαν για την καταπολέμηση του λιμού στην Αιθιοπία.",
            "Χρειάστηκαν 36 ολόκληρα χρόνια για να κατακτήσει τελικά την πρώτη θέση στα βρετανικά charts, φτάνοντας στο #1 την Πρωτοχρονιά του 2021."
        ],
        "source": "https://el.wikipedia.org/wiki/Last_Christmas",
        "locale": "el-GR",
        "tags": ["wham", "george-michael", "christmas", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_121",
        "text": "Ποιο είναι το μεγαλύτερο σε μέγεθος και με τον χαμηλότερο (βαρύτερο) ήχο όργανο της οικογένειας των εγχόρδων με δοξάρι στη συμφωνική ορχήστρα;",
        "answers": [
            "Βιολοντσέλο",
            "Βιόλα",
            "Κοντραμπάσο",
            "Βιολί"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το κοντραμπάσο έχει ύψος περίπου 1,80 έως 2 μέτρα και ο μουσικός παίζει συνήθως όρθιος ή καθισμένος σε ψηλό σκαμπό.",
        "funFacts": [
            "Στην τζαζ μουσική παίζεται σχεδόν αποκλειστικά με τσίμπημα των χορδών με τα δάχτυλα (pizzicato) αποτελώντας τη βάση του ρυθμού.",
            "Σε αντίθεση με τα υπόλοιπα όργανα της ορχήστρας (βιολί, βιόλα, τσέλο) που κουρδίζονται σε πέμπτες, το κοντραμπάσο κουρδίζεται παραδοσιακά σε τέταρτες (Μι-Λα-Ρε-Σολ)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CE%BD%CF%84%CF%81%CE%B1%CE%BC%CF%80%CE%AC%CF%83%CE%BF",
        "locale": "el-GR",
        "tags": ["double-bass", "instruments", "orchestra", "strings"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_122",
        "text": "Ποιο δημοφιλές αμερικανικό hard rock συγκρότημα από το Νιου Τζέρσεϊ απογείωσε την καριέρα του τη δεκαετία του '80 με τον ύμνο «Livin' on a Prayer»;",
        "answers": [
            "Aerosmith",
            "Def Leppard",
            "Van Halen",
            "Bon Jovi"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Bon Jovi, με ηγέτη τον τραγουδιστή Jon Bon Jovi, σημείωσαν τεράστια επιτυχία με το άλμπουμ 'Slippery When Wet' (1986).",
        "funFacts": [
            "Ο κιθαρίστας Richie Sambora χρησιμοποίησε ένα εφέ talkbox στην εισαγωγή του 'Livin\\' on a Prayer' για να δώσει τον χαρακτηριστικό 'wah-wah' ήχο.",
            "Το συγκρότημα έχει δώσει περισσότερες από 2.700 συναυλίες σε πάνω από 50 χώρες για περισσότερους από 35 εκατομμύρια θεατές."
        ],
        "source": "https://el.wikipedia.org/wiki/Bon_Jovi",
        "locale": "el-GR",
        "tags": ["bon-jovi", "rock", "hard-rock", "80s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_123",
        "text": "Ποιος σπουδαίος Έλληνας συνθέτης και δεξιοτέχνης πιανίστας υπέγραψε τον θρυλικό δίσκο «Ο Δρόμος» (1969) σε στίχους Λευτέρη Παπαδόπουλου;",
        "answers": [
            "Μίμης Πλέσσας",
            "Γιώργος Χατζηνάσιος",
            "Κώστας Χατζής",
            "Γιάννης Σπανός"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Μίμης Πλέσσας υπήρξε πολυγραφότατος δημιουργός με τεράστια παρακαταθήκη στον ελληνικό κινηματογράφο και τη σύγχρονη μουσική.",
        "funFacts": [
            "Εκτός από κορυφαίος μουσικός, κατείχε διδακτορικό δίπλωμα στη Χημεία από το Πανεπιστήμιο Αθηνών.",
            "'Ο Δρόμος' παραμένει ο πιο επιτυχημένος εμπορικά δίσκος στην ιστορία της ελληνικής δισκογραφίας, ξεπερνώντας τα 2 εκατομμύρια αντίτυπα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AF%CE%BC%CE%B7%CF%82_%CE%A0%CE%BB%CE%AD%CF%83%CF%83%CE%B1%CF%82",
        "locale": "el-GR",
        "tags": ["plessas", "greek-music", "soundtracks", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_124",
        "text": "Ποιος τυφλός Αμερικανός πιανίστας και τραγουδιστής αποκλήθηκε «Η Ιδιοφυΐα» (The Genius) συνδυάζοντας μπλουζ, γκόσπελ και τζαζ σε κομμάτια όπως «Hit the Road Jack» και «Georgia on My Mind»;",
        "answers": [
            "Μπιλ Γουίδερς",
            "Ρέι Τσαρλς",
            "Τσακ Μπέρι",
            "Ότις Ρέντινγκ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Ray Charles υπήρξε ο πρωτεργάτης της soul μουσικής στη δεκαετία του 1950, ενσωματώνοντας το πάθος της εκκλησιαστικής γκόσπελ στο R&B.",
        "funFacts": [
            "Έχασε την όρασή του σε ηλικία περίπου επτά ετών, πιθανότατα εξαιτίας γλαυκώματος, αλλά έμαθε να διαβάζει και να συνθέτει μουσική σε γραφή Braille.",
            "Η ερμηνεία του στο 'Georgia on My Mind' καθιερώθηκε επίσημα ως ο κρατικός ύμνος της πολιτείας της Τζόρτζια το 1979."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AD%CE%B9_%CE%A4%CF%83%CE%AC%CF%81%CE%BB%CF%82",
        "locale": "el-GR",
        "tags": ["ray-charles", "soul", "blues", "piano"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_125",
        "text": "Ποιο μικρό τετράχορδο έγχορδο όργανο, που μοιάζει με μινιατούρα κιθάρας, συνδέεται άρρηκτα με τη μουσική παράδοση της Χαβάης;",
        "answers": [
            "Μπάντζο",
            "Μαντολίνο",
            "Γιουκαλίλι",
            "Καβακίνιο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το γιουκαλίλι αναπτύχθηκε στη Χαβάη τον 19ο αιώνα ως τοπική προσαρμογή πορτογαλικών εγχόρδων που έφεραν μετανάστες εργάτες.",
        "funFacts": [
            "Η λέξη 'ukulele' στη γλώσσα της Χαβάης μεταφράζεται κατά προσέγγιση ως 'ψύλλος που χοροπηδά' (jumping flea), περιγράφοντας τη γρήγορη κίνηση των δακτύλων στην ταστιέρα.",
            "Ο Χαβανέζος μουσικός Israel Kamakawiwoʻole γνώρισε παγκόσμια δόξα παίζοντας γιουκαλίλι στο ποτ-πουρί 'Somewhere Over the Rainbow / What a Wonderful World'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%BF%CF%85%CE%BA%CE%B1%CE%BB%CE%AF%CE%BB%CE%B9",
        "locale": "el-GR",
        "tags": ["ukulele", "instruments", "hawaii", "strings"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_126",
        "text": "Ποιο εμβληματικό τραγούδι της Madonna του 1989 συνδύασε ποπ μουσική με εκκλησιαστική χορωδία γκόσπελ και προκάλεσε έντονες αντιδράσεις από το Βατικανό για το βιντεοκλίπ του;",
        "answers": [
            "Papa Don't Preach",
            "Material Girl",
            "La Isla Bonita",
            "Like a Prayer"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Like a Prayer' θεωρείται ένα από τα κορυφαία τραγούδια στην καριέρα της Madonna, επαινεμένο από τους κριτικούς για την παραγωγή και τα φωνητικά του.",
        "funFacts": [
            "Το βιντεοκλίπ απεικόνιζε καιόμενους σταυρούς και θρησκευτικά σύμβολα, οδηγώντας την εταιρεία Pepsi να ακυρώσει μια τεράστια χορηγική διαφημιστική καμπάνια μαζί της.",
            "Στα φωνητικά του ρεφρέν συμμετείχε η περίφημη χορωδία Andraé Crouch Gospel Choir."
        ],
        "source": "https://el.wikipedia.org/wiki/Like_a_Prayer_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["madonna", "pop", "gospel", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_127",
        "text": "Ποια διεθνής Ελληνίδα ηθοποιός και υπουργός Πολιτισμού τραγούδησε τα βραβευμένα με Όσκαρ «Παιδιά του Πειραιά» στην ταινία «Ποτέ την Κυριακή» (1960);",
        "answers": [
            "Μελίνα Μερκούρη",
            "Ειρήνη Παππά",
            "Αλίκη Βουγιουκλάκη",
            "Τζένη Καρέζη"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Μελίνα Μερκούρη υπήρξε παγκόσμιο σύμβολο του ελληνικού πολιτισμού, ενώ ως υπουργός Πολιτισμού ξεκίνησε τη διεθνή εκστρατεία για την επιστροφή των Γλυπτών του Παρθενώνα.",
        "funFacts": [
            "Για τον ρόλο της Ίλιας στο 'Ποτέ την Κυριακή' απέσπασε το Βραβείο Καλύτερης Ηθοποιού στο Φεστιβάλ των Καννών και προτάθηκε για Όσκαρ Α' Γυναικείου Ρόλου.",
            "Ήταν η εμπνεύστρια του θεσμού της 'Πολιτιστικής Πρωτεύουσας της Ευρώπης', που εγκαινιάστηκε στην Αθήνα το 1985."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CE%BB%CE%AF%CE%BD%CE%B1_%CE%9C%CE%B5%CF%81%CE%BA%CE%BF%CF%8D%CF%81%CE%B7",
        "locale": "el-GR",
        "tags": ["merkouri", "chatzidakis", "greek-music", "cinema"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_128",
        "text": "Ποιο βρετανικό ροκ συγκρότημα με τραγουδιστή και μπασίστα τον Sting κυκλοφόρησε τον διαχρονικό ύμνο «Every Breath You Take» το 1983;",
        "answers": [
            "Dire Straits",
            "The Police",
            "The Clash",
            "Duran Duran"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι The Police συνδύασαν post-punk, new wave και reggae rock, αποτελώντας ένα από τα πιο επιτυχημένα γκρουπ των αρχών της δεκαετίας του 1980.",
        "funFacts": [
            "Το 'Every Breath You Take' έγινε το τραγούδι με τις περισσότερες ραδιοφωνικές μεταδόσεις στην ιστορία του ραδιοφώνου των ΗΠΑ σύμφωνα με τον οργανισμό BMI.",
            "Παρά τον συχνά ερωτικό τρόπο με τον οποίο εκλαμβάνεται, ο Sting έχει δηλώσει ότι οι στίχοι μιλούν για ζήλια, εμμονή και παρακολούθηση μετά από έναν χωρισμό."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Police",
        "locale": "el-GR",
        "tags": ["the-police", "sting", "rock", "80s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_129",
        "text": "Ποιο απλό ξύλινο ή πλαστικό πνευστό όργανο με ράμφος (επιστόμιο) και οπές για τα δάχτυλα διδάσκεται παραδοσιακά στα σχολεία για την εκμάθηση της μουσικής;",
        "answers": [
            "Σαξόφωνο",
            "Τρομπέτα",
            "Μπλοκφλάουτο",
            "Όμποε"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το μπλοκφλάουτο (ή ευθύ φλάουτο με ράμφος) είναι ένα από τα πιο προσιτά όργανα για τη βασική μουσική εκπαίδευση των παιδιών.",
        "funFacts": [
            "Ήταν εξαιρετικά δημοφιλές κατά την περίοδο της Αναγέννησης και του Μπαρόκ πριν παραγκωνιστεί προσωρινά από το πλάγιο φλάουτο στις κλασικές ορχήστρες.",
            "Σε αντίθεση με το πλάγιο φλάουτο, ο ήχος παράγεται φυσώντας απευθείας σε ένα στενό κανάλι (windway) χωρίς να απαιτείται ειδική τοποθέτηση χειλιών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%BB%CE%AC%CE%BF%CF%85%CF%84%CE%BF_%CE%BC%CE%B5_%CF%81%CE%AC%CE%BC%CF%86%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["recorder", "instruments", "woodwinds", "education"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_130",
        "text": "Ποιο θρυλικό hard rock τραγούδι των Deep Purple περιέχει το πιο αναγνωρίσιμο κιθαριστικό riff στην ιστορία και εμπνεύστηκε από μια φωτιά στο καζίνο του Μοντρέ;",
        "answers": [
            "Highway Star",
            "Child in Time",
            "Burn",
            "Smoke on the Water"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Smoke on the Water' κυκλοφόρησε στο άλμπουμ 'Machine Head' (1972) και το διάσημο ριφ τεσσάρων συγχορδιών παίχτηκε από τον κιθαρίστα Ritchie Blackmore.",
        "funFacts": [
            "Οι στίχοι αφηγούνται αληθινά γεγονότα: το καζίνο του Μοντρέ στην Ελβετία κάηκε ολοσχερώς όταν κάποιος θεατής εκτόξευσε φωτοβολίδα κατά τη διάρκεια συναυλίας του Frank Zappa.",
            "Ο τίτλος περιγράφει τον καπνό της πυρκαγιάς που απλώθηκε πάνω από τα νερά της λίμνης της Γενεύης."
        ],
        "source": "https://el.wikipedia.org/wiki/Smoke_on_the_Water",
        "locale": "el-GR",
        "tags": ["deep-purple", "rock", "hard-rock", "guitar-riff"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_131",
        "text": "Ποιος κορυφαίος Έλληνας συνθέτης μελοποίησε με ανεπανάληπτο τρόπο τα ποιήματα του Νίκου Καββαδία στον ιστορικό δίσκο «Ο Σταυρός του Νότου» (1979);",
        "answers": [
            "Θάνος Μικρούτσικος",
            "Μάνος Λοΐζος",
            "Χρήστος Λεοντής",
            "Διονύσης Τσακνής"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Θάνος Μικρούτσικος υπήρξε ριζοσπαστικός συνθέτης, διατελώντας επίσης υπουργός Πολιτισμού της Ελλάδας.",
        "funFacts": [
            "Ο δίσκος 'Ο Σταυρός του Νότου' αντιμετωπίστηκε αρχικά με επιφύλαξη από ορισμένους κριτικούς, αλλά εξελίχθηκε σε έναν από τους πιο αγαπημένους δίσκους όλων των εποχών στην Ελλάδα.",
            "Συνέθεσε επίσης εμβληματικά τραγούδια όπως 'Η Ρόζα' και το 'Ένα Μαχαίρι'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%98%CE%AC%CE%BD%CE%BF%CF%82_%CE%9C%CE%B9%CE%BA%CF%81%CE%BF%CF%8D%CF%84%CF%83%CE%B9%CE%BA%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["mikroutsikos", "kavvadias", "greek-music", "poetry"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_132",
        "text": "Ποιος Αμερικανός ποπ τραγουδιστής ξεκίνησε ως βασικός τραγουδιστής του boyband *NSYNC και έκανε τεράστια σόλο καριέρα με επιτυχίες όπως «Cry Me a River» και «Can't Stop the Feeling!»;",
        "answers": [
            "Ρόμπι Γουίλιαμς",
            "Τζάστιν Τίμπερλεϊκ",
            "Νικ Κάρτερ",
            "Άσερ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Justin Timberlake καθιερώθηκε ως ένας από τους πιο επιδραστικούς ποπ ερμηνευτές και χορευτές των 2000s, κερδίζοντας 10 βραβεία Grammy.",
        "funFacts": [
            "Το τραγούδι του 'Can't Stop the Feeling!' από την ταινία κινουμένων σχεδίων 'Trolls' ήταν το σινγκλ με τις υψηλότερες πωλήσεις στις ΗΠΑ για το 2016.",
            "Έχει διαγράψει αξιόλογη πορεία και ως ηθοποιός σε κινηματογραφικές ταινίες, όπως το 'The Social Network' (2010)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AC%CF%83%CF%84%CE%B9%CE%BD_%CE%A4%CE%AF%CE%BC%CF%80%CE%B5%CF%81%CE%BB%CE%B5%CF%8A%CE%BA",
        "locale": "el-GR",
        "tags": ["timberlake", "pop", "nsync", "grammy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_133",
        "text": "Ποιο μικρό έγχορδο μουσικό όργανο με οβάλ κυρτό ηχείο και τέσσερα ζεύγη διπλών μεταλλικών χορδών αποτελεί χαρακτηριστικό όργανο των επτανησιακών καντάδων;",
        "answers": [
            "Κιθάρα",
            "Λαούτο",
            "Μαντολίνο",
            "Ταμπουράς"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το μαντολίνο παίζεται με πένα και χαρακτηρίζεται από τη γρήγορη παλμική τεχνική εκτέλεσης (τρέμολο) στις διπλές χορδές του.",
        "funFacts": [
            "Είναι κουρδισμένο ακριβώς όπως το βιολί (Σολ-Ρε-Λα-Μι), αλλά παίζεται αποκλειστικά με πένα αντί για δοξάρι.",
            "Στα Επτάνησα αποτελούσε τη βάση για τις παραδοσιακές 'μαντολινάτες', ορχηστρικά σύνολα που συνόδευαν τις τοπικές καντάδες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%84%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF",
        "locale": "el-GR",
        "tags": ["mandolin", "instruments", "heptanese", "tradition"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_134",
        "text": "Ποιο εμβληματικό τραγούδι των Queen αποτελείται σχεδόν αποκλειστικά από ρυθμικά χτυπήματα ποδιών στο πάτωμα και παλαμάκια (stomp-stomp-clap) πριν το τελικό σόλο κιθάρας;",
        "answers": [
            "Radio Ga Ga",
            "Another One Bites the Dust",
            "Under Pressure",
            "We Will Rock You"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'We Will Rock You' γράφτηκε από τον κιθαρίστα Brian May το 1977 και έχει γίνει ο απόλυτος αθλητικός ύμνος στα στάδια ολόκληρου του πλανήτη.",
        "funFacts": [
            "Ο ήχος των ποδιών και των χειροκροτημάτων δημιουργήθηκε από τα μέλη του συγκροτήματος που χτυπούσαν σε παλιές ξύλινες σανίδες στο στούντιο και πολλαπλασιάστηκε με ειδικά ηχητικά εφέ.",
            "Στο single κυκλοφόρησε μαζί με το εξίσου μυθικό τραγούδι 'We Are the Champions'."
        ],
        "source": "https://el.wikipedia.org/wiki/We_Will_Rock_You",
        "locale": "el-GR",
        "tags": ["queen", "rock", "stadium-anthem", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_135",
        "text": "Ποιος μεγάλος λαϊκός βάρδος με τη βαθιά, αυθεντική φωνή ερμήνευσε κλασικά λαϊκά τραγούδια όπως «Βρέχει φωτιά στη στράτα μου» και «Ο παλιατζής»;",
        "answers": [
            "Στράτος Διονυσίου",
            "Στέλιος Καζαντζίδης",
            "Μιχάλης Μενιδιάτης",
            "Μανώλης Αγγελόπουλος"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Στράτος Διονυσίου υπήρξε μία από τις πιο γνήσιες και επιβλητικές φωνές του ελληνικού λαϊκού τραγουδιού από τα τέλη του 1960 έως το 1990.",
        "funFacts": [
            "Το 'Βρέχει φωτιά στη στράτα μου' σε μουσική Μίμη Πλέσσα και στίχους Λευτέρη Παπαδόπουλου γράφτηκε για την ταινία 'Ορατότης μηδέν' (1970) με τον Νίκο Κούρκουλο.",
            "Οι γιοι του, Άγγελος, Στέλιος και Διαμαντής Διονυσίου, ακολούθησαν επίσης επαγγελματική καριέρα στο λαϊκό τραγούδι."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CF%81%CE%AC%CF%84%CE%BF%CF%82_%CE%94%CE%B9%CE%BF%CE%BD%CF%85%CF%83%CE%AF%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["dionysiou", "laiko", "greek-music", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_136",
        "text": "Ποιο γερμανικό ροκ συγκρότημα κυκλοφόρησε τη διάσημη μπαλάντα με το χαρακτηριστικό σφύριγμα «Wind of Change», που συνδέθηκε ιστορικά με την πτώση του Τείχους του Βερολίνου;",
        "answers": [
            "Rammstein",
            "Scorpions",
            "Helloween",
            "Accept"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Scorpions κυκλοφόρησαν το 'Wind of Change' το 1990 και αποτέλεσε τον παγκόσμιο ύμνο για το τέλος του Ψυχρού Πολέμου.",
        "funFacts": [
            "Το τραγούδι εμπνεύστηκε ο τραγουδιστής Klaus Meine κατά την επίσκεψη του συγκροτήματος στη Μόσχα το 1989 για το Moscow Music Peace Festival.",
            "Αποτελεί ένα από τα πιο εμπορικά σινγκλ όλων των εποχών, με πωλήσεις άνω των 14 εκατομμυρίων αντιτύπων παγκοσμίως."
        ],
        "source": "https://el.wikipedia.org/wiki/Scorpions",
        "locale": "el-GR",
        "tags": ["scorpions", "rock", "wind-of-change", "ballad"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_137",
        "text": "Ποιο ηλεκτρονικό μουσικό όργανο παράγει και επεξεργάζεται ηλεκτρικά ηχητικά σήματα για να δημιουργήσει ήχους που μιμούνται φυσικά όργανα ή εντελώς νέες ηχητικές συχνότητες;",
        "answers": [
            "Ηλεκτρικό πιάνο",
            "Αρμόνιο",
            "Συνθεσάιζερ",
            "Τσελέστα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το συνθεσάιζερ (synthesizer) έφερε επανάσταση στη σύγχρονη μουσική, γεννώντας νέα είδη όπως η synth-pop, η ηλεκτρονική και η χορευτική μουσική.",
        "funFacts": [
            "Το αναλογικό συνθεσάιζερ Minimoog, που κυκλοφόρησε το 1970 από τον Robert Moog, ήταν το πρώτο ευρέως προσβάσιμο και φορητό synth για συναυλίες.",
            "Έλληνες συνθέτες όπως ο Vangelis υπήρξαν πρωτοπόροι παγκοσμίως στην εκτεταμένη αξιοποίηση των συνθεσάιζερ σε κινηματογραφικές συνθέσεις."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%BD%CE%B8%CE%B5%CF%83%CE%AC%CE%B9%CE%B6%CE%B5%CF%81",
        "locale": "el-GR",
        "tags": ["synthesizer", "electronic", "instruments", "music-tech"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_138",
        "text": "Ποια Βρετανίδα σταρ της ποπ με καταγωγή από το Κοσσυφοπέδιο κυριάρχησε στα παγκόσμια charts με το nu-disco άλμπουμ «Future Nostalgia» και επιτυχίες όπως το «Levitating»;",
        "answers": [
            "Ρίτα Όρα",
            "Μπέμπε Ρέτζα",
            "Καμίλα Καμπέγιο",
            "Ντούα Λίπα"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Dua Lipa έχει αναδειχθεί σε μία από τις κορυφαίες φιγούρες της σύγχρονης ποπ μουσικής, κερδίζοντας πολλαπλά βραβεία Grammy και Brit Awards.",
        "funFacts": [
            "Το άλμπουμ 'Future Nostalgia' κυκλοφόρησε τον Μάρτιο του 2020 στην αρχή της παγκόσμιας καραντίνας και έγινε το soundtrack της χρονιάς για εκατομμύρια ακροατές.",
            "Τραγούδησε επίσης τη μεγάλη επιτυχία 'Dance the Night' για το soundtrack της ταινίας υπερπαραγωγής 'Barbie' (2023)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%BF%CF%8D%CE%B1_%CE%9B%CE%AF%CF%80%CE%B1",
        "locale": "el-GR",
        "tags": ["dua-lipa", "pop", "disco", "charts"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_139",
        "text": "Ποιος μεγάλος Κρητικός συνθέτης εισήγαγε το κίνημα «Επιστροφή στις ρίζες» συνδυάζοντας συμφωνικά όργανα με παραδοσιακά ελληνικά όργανα σε έργα όπως το «Χρονικό» και η «Θητεία»;",
        "answers": [
            "Γιάννης Μαρκόπουλος",
            "Χρήστος Λεοντής",
            "Σταύρος Ξαρχάκος",
            "Ηλίας Ανδριόπουλος"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Γιάννης Μαρκόπουλος συνέδεσε άρρηκτα τη μουσική του με τους αγώνες για δημοκρατία, συνεργαζόμενος με ερμηνευτές όπως ο Νίκος Ξυλούρης και ο Λάκης Χαλκιάς.",
        "funFacts": [
            "Στα έργα του χρησιμοποίησε για πρώτη φορά ταυτόχρονα τη λύρα, το σαντούρι και το λαούτο πλάι σε συμφωνικά έγχορδα και τρομπέτες.",
            "Συνέθεσε το περίφημο θέμα για τη βρετανική τηλεοπτική σειρά 'Who Pays the Ferryman?' (1977), το οποίο έγινε διεθνές hit στα βρετανικά charts."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%9C%CE%B1%CF%81%CE%BA%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["markopoulos", "greek-music", "tradition", "crete"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_140",
        "text": "Ποιο θρυλικό hard rock συγκρότημα από τη Βοστώνη με τραγουδιστή τον Steven Tyler ερμήνευσε το βραβευμένο σινγκλ «I Don't Want to Miss a Thing» για την ταινία «Αρμαγεδδών»;",
        "answers": [
            "Kiss",
            "Aerosmith",
            "Van Halen",
            "Def Leppard"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Aerosmith, γνωστοί και ως 'The Bad Boys from Boston', αποτελούν το αμερικανικό hard rock συγκρότημα με τις περισσότερες πωλήσεις δίσκων στην ιστορία.",
        "funFacts": [
            "Το 'I Don't Want to Miss a Thing' (1998) ήταν το πρώτο και μοναδικό τραγούδι στην 28χρονη τότε πορεία του συγκροτήματος που κατέκτησε το νούμερο 1 του Billboard Hot 100.",
            "Στην ταινία 'Αρμαγεδδών' πρωταγωνιστούσε η κόρη του Steven Tyler, η διάσημη ηθοποιός Liv Tyler."
        ],
        "source": "https://el.wikipedia.org/wiki/Aerosmith",
        "locale": "el-GR",
        "tags": ["aerosmith", "hard-rock", "soundtracks", "steven-tyler"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_141",
        "text": "Ποιο απλό μεταλλικό κρουστό όργανο έχει σχήμα ανοιχτού γεωμετρικού τριγώνου και χρησιμοποιείται παραδοσιακά στην Ελλάδα από τα παιδιά για τα κάλαντα των Χριστουγέννων;",
        "answers": [
            "Κουδούνι",
            "Ντέφι",
            "Τρίγωνο",
            "Μεταλλόφωνο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το τρίγωνο είναι ιδιόφωνο όργανο από ατσάλινο κυλινδρικό ράβδο, που παράγει έναν διαυγή, ψηλό μεταλλικό ήχο όταν χτυπιέται με ατσάλινη ράβδο.",
        "funFacts": [
            "Μία από τις γωνίες του τριγώνου παραμένει πάντα ανοιχτή για να επιτρέπει στο μέταλλο να ταλαντώνεται ελεύθερα και να παράγει αρμονικές συχνότητες.",
            "Στη συμφωνική ορχήστρα εισήχθη ευρέως τον 18ο αιώνα για να προσδώσει τη λεγόμενη 'τουρκική' ή στρατιωτική χροιά σε έργα όπως η 9η Συμφωνία του Beethoven."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%AF%CE%B3%CF%89%CE%BD%CE%BF_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CF%8C_%CF%8C%CF%81%CE%B3%CE%B1%CE%BD%CE%BF)",
        "locale": "el-GR",
        "tags": ["triangle", "instruments", "percussion", "tradition"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_142",
        "text": "Ποιο πασίγνωστο τραγούδι των ABBA, που κυκλοφόρησε το 1976, θεωρείται ένας από τους κορυφαίους ποπ-ντίσκο ύμνους όλων των εποχών με τον στίχο «Young and sweet, only seventeen»;",
        "answers": [
            "Mamma Mia",
            "Waterloo",
            "Gimme! Gimme! Gimme!",
            "Dancing Queen"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Dancing Queen' αποτέλεσε την πιο επιτυχημένη εμπορικά δημιουργία των ABBA, φτάνοντας στην κορυφή των charts σε περισσότερες από 15 χώρες.",
        "funFacts": [
            "Το συγκρότημα πρωτοπαρουσίασε το τραγούδι ζωντανά σε ειδική τηλεοπτική εκδήλωση προς τιμήν του γάμου του βασιλιά Carl XVI Gustaf της Σουηδίας το 1976.",
            "Ήταν το μοναδικό τραγούδι των ABBA που κατάφερε ποτέ να φτάσει στο νούμερο 1 του αμερικανικού Billboard Hot 100."
        ],
        "source": "https://el.wikipedia.org/wiki/Dancing_Queen",
        "locale": "el-GR",
        "tags": ["abba", "pop", "disco", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_143",
        "text": "Ποια καταξιωμένη Ελληνίδα ερμηνεύτρια ξεκίνησε από την Οπισθοδρομική Κομπανία και καθήλωσε το κοινό με επιτυχίες όπως «Δυνατά», τραγουδώντας και στην τελετή λήξης των Ολυμπιακών Αγώνων της Αθήνας το 2004;",
        "answers": [
            "Ελευθερία Αρβανιτάκη",
            "Ελένη Τσαλιγοπούλου",
            "Μελίνα Κανά",
            "Γιώτα Νέγκα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Ελευθερία Αρβανιτάκη συνδύασε μοναδικά το παραδοσιακό δημοτικό τραγούδι με το σύγχρονο έντεχνο και την έθνικ μουσική.",
        "funFacts": [
            "Το τραγούδι 'Δυνατά' είναι διασκευή του κομματιού 'Ara Batur' του Αρμένιου συνθέτη Ara Dinkjian.",
            "Έχει εμφανιστεί σε κορυφαίες διεθνείς αίθουσες συναυλιών, όπως το Carnegie Hall της Νέας Υόρκης και το Barbican Center του Λονδίνου."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BB%CE%B5%CF%85%CE%B8%CE%B5%CF%81%CE%AF%CE%B1_%CE%91%CF%81%CE%B2%CE%B1%CE%BD%CE%B9%CF%84%CE%AC%CE%BA%CE%B7",
        "locale": "el-GR",
        "tags": ["arvanitaki", "greek-music", "entechno", "world-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_144",
        "text": "Ποιος θρυλικός Αμερικανός τραγουδιστής της κάντρι και του ροκ έγινε παγκοσμίως γνωστός ως «The Man in Black» και έδωσε ιστορικές συναυλίες μέσα στις φυλακές Folsom και San Quentin;",
        "answers": [
            "Γουίλι Νέλσον",
            "Τζόνι Κας",
            "Κένι Ρότζερς",
            "Γουάιλον Τζένινγκς"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Johnny Cash υπήρξε μία από τις πιο επιδραστικές μορφές της αμερικανικής μουσικής, με χαρακτηριστική βαθιά μπάσα φωνή και τραγούδια όπως 'I Walk the Line' και 'Ring of Fire'.",
        "funFacts": [
            "Φορούσε αποκλειστικά μαύρα ρούχα στις δημόσιες εμφανίσεις του ως ένδειξη συμπαράστασης στους φτωχούς, τους καταπιεσμένους και τους φυλακισμένους.",
            "Το 2002 η συγκλονιστική διασκευή του στο τραγούδι 'Hurt' των Nine Inch Nails απέσπασε διθυραμβικές κριτικές λίγο πριν από τον θάνατό του."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CF%8C%CE%BD%CE%B9_%CE%9A%CE%B1%CF%82",
        "locale": "el-GR",
        "tags": ["johnny-cash", "country", "rock", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_145",
        "text": "Ποια μεγάλα ημισφαιρικά τύμπανα με χάλκινο σώμα και ποδοκίνητο πεντάλ για τη ρύθμιση συγκεκριμένου τονικού ύψους αποτελούν βασικό στοιχείο των κρουστών της συμφωνικής ορχήστρας;",
        "answers": [
            "Ταμπούρα",
            "Μπότες",
            "Τυμπάνια",
            "Κονγκάς"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Τα τυμπάνια (timpani ή kettledrums) είναι τα μοναδικά κρουστά τύμπανα της κλασικής ορχήστρας που κουρδίζονται σε απόλυτα συγκεκριμένες νότες.",
        "funFacts": [
            "Ο εκτελεστής αλλάζει το τονικό ύψος πιέζοντας ένα ποδοκίνητο πεντάλ που τεντώνει ή χαλαρώνει τη μεμβράνη.",
            "Συνήθως χρησιμοποιείται ένα σετ από τέσσερα διαφορετικού μεγέθους τυμπάνια τοποθετημένα σε ημικύκλιο γύρω από τον μουσικό."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%85%CE%BC%CF%80%CE%AC%CE%BD%CE%B9%CE%B1",
        "locale": "el-GR",
        "tags": ["timpani", "instruments", "percussion", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_146",
        "text": "Ποιο ιστορικό βρετανικό πανκ ροκ συγκρότημα κυκλοφόρησε το επαναστατικό άλμπουμ «London Calling» (1979) με επιρροές από ρέγκε, σκα και rockabilly;",
        "answers": [
            "Sex Pistols",
            "The Ramones",
            "The Jam",
            "The Clash"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι The Clash, με ηγέτη τον Joe Strummer, ξεχώρισαν για την πολιτική τους στράτευση και τον πειραματισμό με διάφορα μουσικά στυλ πέρα από το παραδοσιακό πανκ.",
        "funFacts": [
            "Το εξώφυλλο του 'London Calling' με τον μπασίστα Paul Simonon να σπάει το μπάσο του στη σκηνή θεωρείται μια από τις πιο εμβληματικές ροκ φωτογραφίες όλων των εποχών.",
            "Το περιοδικό Rolling Stone ανακήρυξε το 'London Calling' ως το κορυφαίο άλμπουμ της δεκαετίας του 1980 (αν και κυκλοφόρησε στο Ηνωμένο Βασίλειο τον Δεκέμβριο του 1979)."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Clash",
        "locale": "el-GR",
        "tags": ["the-clash", "punk", "rock", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_147",
        "text": "Ποιος αυτοδίδακτος Έλληνας τραγουδοποιός ξεκίνησε αναρτώντας ερασιτεχνικά βίντεο με την κιθάρα του στο YouTube και έγινε λαϊκό φαινόμενο με το τραγούδι «Δεν ταιριάζετε σου λέω»;",
        "answers": [
            "Παντελής Παντελίδης",
            "Νίκος Οικονομόπουλος",
            "Κωνσταντίνος Αργυρός",
            "Πέτρος Ιακωβίδης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Παντελής Παντελίδης γνώρισε πρωτοφανή λαϊκή αποδοχή μέσα σε ελάχιστο χρονικό διάστημα, πριν χάσει τραγικά τη ζωή του σε τροχαίο δυστύχημα το 2016.",
        "funFacts": [
            "Υπηρέτησε ως υπαξιωματικός στο Πολεμικό Ναυτικό για σχεδόν μία δεκαετία πριν παραιτηθεί για να αφοσιωθεί επαγγελματικά στη μουσική.",
            "Όλα τα τραγούδια που ερμήνευσε ήταν σε δικούς του στίχους και μουσική, ενώ έγραψε επιτυχίες και για πολλούς άλλους γνωστούς καλλιτέχνες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%BD%CF%84%CE%B5%CE%BB%CE%AE%CF%82_%CE%A0%CE%B1%CE%BD%CF%84%CE%B5%CE%BB%CE%AF%CE%B4%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["pantelidis", "laiko", "greek-music", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_148",
        "text": "Ποια Αμερικανίδα τραγουδίστρια με φωνητική έκταση πέντε οκτάβων και χαρακτηριστικό σφύριγμα (whistle register) ερμήνευσε το απόλυτο εορταστικό χιτ «All I Want for Christmas Is You»;",
        "answers": [
            "Σελίν Ντιόν",
            "Μαράια Κάρεϊ",
            "Γουίτνεϊ Χιούστον",
            "Κριστίνα Αγκιλέρα"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Mariah Carey είναι μία από τις πιο επιτυχείς εμπορικά καλλιτέχνιδες στην ιστορία, με 19 τραγούδια της να έχουν κατακτήσει το νούμερο 1 του αμερικανικού Billboard Hot 100.",
        "funFacts": [
            "Το 'All I Want for Christmas Is You' (1994) αποφέρει ετησίως εκατομμύρια δολάρια σε δικαιώματα και επανέρχεται στο #1 των παγκόσμιων charts κάθε Δεκέμβριο.",
            "Κατέχει το ρεκόρ των περισσότερων εβδομάδων στην πρώτη θέση των αμερικανικών charts από οποιονδήποτε σόλο καλλιτέχνη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AC%CE%B9%CE%B1_%CE%9A%CE%AC%CF%81%CE%B5%CF%8A",
        "locale": "el-GR",
        "tags": ["mariah-carey", "pop", "christmas", "whistle-register"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_149",
        "text": "Ποιο μεγάλο κυκλικό μεταλλικό κρουστό όργανο με καταγωγή από την Ανατολική και Νοτιοανατολική Ασία παράγει έναν βαθύ, αντηχητικό ήχο όταν χτυπιέται με μεγάλη μαλακή μπαγκέτα;",
        "answers": [
            "Πιατίνι",
            "Ταμπούρο",
            "Γκονγκ",
            "Κουδούνα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το γκονγκ χρησιμοποιείται παραδοσιακά σε τελετές στην Ασία, καθώς και σε ορχηστρικά κρεσέντο στη δυτική συμφωνική μουσική και τον κινηματογράφο.",
        "funFacts": [
            "Τα παραδοσιακά γκονγκ σφυρηλατούνται χειροποίητα από κράμα χαλκού και κασσίτερου (μπρούντζος).",
            "Στο εισαγωγικό λογότυπο της ιστορικής κινηματογραφικής εταιρείας Rank Organisation εμφανιζόταν ένας μυώδης άνδρας που χτυπούσε ένα γιγάντιο γκονγκ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%BF%CE%BD%CE%B3%CE%BA",
        "locale": "el-GR",
        "tags": ["gong", "instruments", "percussion", "asia"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_150",
        "text": "Ποιο πασίγνωστο τραγούδι των Oasis, γραμμένο και τραγουδισμένο από τον Noel Gallagher, περιέχει τον περίφημο στίχο «So Sally can wait» και έγινε ύμνος αλληλεγγύης για την πόλη του Μάντσεστερ;",
        "answers": [
            "Wonderwall",
            "Champagne Supernova",
            "Live Forever",
            "Don't Look Back in Anger"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Don't Look Back in Anger' κυκλοφόρησε το 1995 στο άλμπουμ '(What\\'s the Story) Morning Glory?' και αποτέλεσε το δεύτερο νούμερο 1 σινγκλ του συγκροτήματος στο Ηνωμένο Βασίλειο.",
        "funFacts": [
            "Το εισαγωγικό πιάνο του κομματιού αποτελεί άμεσο φόρο τιμής στο τραγούδι 'Imagine' του John Lennon.",
            "Μετά την τρομοκρατική επίθεση στο Manchester Arena το 2017, το τραγούδι τραγουδήθηκε αυθόρμητα από τα πλήθη και έγινε το σύμβολο ενότητας και δύναμης της πόλης."
        ],
        "source": "https://el.wikipedia.org/wiki/Don%27t_Look_Back_in_Anger",
        "locale": "el-GR",
        "tags": ["oasis", "britpop", "noel-gallagher", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_151",
        "text": "Ποιος πρωτοποριακός Έλληνας τραγουδοποιός και συνθέτης διοργάνωσε το θρυλικό «Πάρτι στη Βουλιαγμένη» το καλοκαίρι του 1983, μαζεύοντας πάνω από 70.000 θεατές στην πλαζ;",
        "answers": [
            "Λουκιανός Κηλαηδόνης",
            "Διονύσης Σαββόπουλος",
            "Κώστας Τουρνάς",
            "Βασίλης Παπακωνσταντίνου"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Λουκιανός Κηλαηδόνης έφερε έναν εντελώς νέο, ανάλαφρο και νοσταλγικό αέρα στο ελληνικό τραγούδι, επηρεασμένος από το αμερικανικό σουίνγκ, το μπλουζ και το ροκ εν ρολ.",
        "funFacts": [
            "Το 'Πάρτι στη Βουλιαγμένη' θεωρείται το ελληνικό 'Γούντστοκ' και ήταν η πρώτη μεγάλη συναυλία σε φυσικό υπαίθριο χώρο στην Ελλάδα, με τη σκηνή στημένη πάνω σε πλωτή σχεδία μέσα στη θάλασσα.",
            "Είχε σπουδάσει αρχιτεκτονική στο Εθνικό Μετσόβιο Πολυτεχνείο πριν αφοσιωθεί αποκλειστικά στη μουσική."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CF%85%CE%BA%CE%B9%CE%B1%CE%BD%CF%8C%CF%82_%CE%9A%CE%B7%CE%BB%CE%B1%CE%B7%CE%B4%CF%8C%CE%BD%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["kilaidonis", "greek-music", "swing", "events"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_152",
        "text": "Ποιο κορυφαίο βρετανικό heavy metal συγκρότημα, με τραγουδιστή τον Bruce Dickinson και μασκότ το τέρας Eddie, κυκλοφόρησε το κλασικό άλμπουμ «The Number of the Beast» (1982);",
        "answers": [
            "Judas Priest",
            "Iron Maiden",
            "Black Sabbath",
            "Motorhead"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Iron Maiden ιδρύθηκαν στο Λονδίνο το 1975 από τον μπασίστα Steve Harris και υπήρξαν οι ηγέτες του New Wave of British Heavy Metal.",
        "funFacts": [
            "Ο τραγουδιστής Bruce Dickinson είναι επαγγελματίας πιλότος πολιτικών αεροσκαφών και πιλοτάριζε ο ίδιος το ειδικά διαμορφωμένο Boeing 747 του γκρουπ ('Ed Force One') στις παγκόσμιες περιοδείες τους.",
            "Η ανατριχιαστική εισαγωγή στο τραγούδι 'The Number of the Beast' διαβάζεται από τον Βρετανό ηθοποιό Barry Clayton και παραθέτει αποσπάσματα από την Αποκάλυψη του Ιωάννη."
        ],
        "source": "https://el.wikipedia.org/wiki/Iron_Maiden",
        "locale": "el-GR",
        "tags": ["iron-maiden", "metal", "heavy-metal", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_153",
        "text": "Ποιο ξύλινο πνευστό όργανο με διπλή γλωττίδα δίνει παραδοσιακά τον πρώτο φθόγγο (νότα Λα στα 440 Hz) για να κουρδίσουν όλα τα όργανα της συμφωνικής ορχήστρας;",
        "answers": [
            "Φλάουτο",
            "Κλαρινέτο",
            "Όμποε",
            "Φαγκότο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το όμποε επιλέγεται για το κούρδισμα της ορχήστρας επειδή ο καθαρός, διαπεραστικός του ήχος ξεχωρίζει εύκολα ανάμεσα σε όλα τα υπόλοιπα όργανα.",
        "funFacts": [
            "Η λέξη προέρχεται από το γαλλικό 'hautbois', που σημαίνει κυριολεκτικά 'ψηλό ξύλο' (λόγω του υψηλού του τόνου).",
            "Το διπλό καλάμι (γλωττίδα) του όμποε κατασκευάζεται συνήθως με εξαιρετική ακρίβεια στο χέρι από τους ίδιους τους μουσικούς."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%8C%CE%BC%CF%80%CE%BF%CE%B5",
        "locale": "el-GR",
        "tags": ["oboe", "instruments", "woodwinds", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_154",
        "text": "Ποιο εκρηκτικό ηλεκτροπόπ τραγούδι της Lady Gaga του 2009 ξεκινά με τη διάσημη συλλαβική εισαγωγή «Rah-rah-ah-ah-ah, roma-roma-ma» και απέσπασε δύο βραβεία Grammy;",
        "answers": [
            "Poker Face",
            "Just Dance",
            "Born This Way",
            "Bad Romance"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Bad Romance' κυκλοφόρησε ως το βασικό σινγκλ του άλμπουμ 'The Fame Monster' και έγινε ένα από τα πιο αναγνωρίσιμα ποπ τραγούδια του 21ου αιώνα.",
        "funFacts": [
            "Το φουτουριστικό βιντεοκλίπ του τραγουδιού ήταν το πρώτο βίντεο στην ιστορία του YouTube που ξεπέρασε τις 200 εκατομμύρια προβολές.",
            "Στο βιντεοκλίπ η Lady Gaga φόρεσε τα περίφημα παπούτσια 'Armadillo' ύψους 30 εκατοστών του σχεδιαστή Alexander McQueen."
        ],
        "source": "https://el.wikipedia.org/wiki/Bad_Romance",
        "locale": "el-GR",
        "tags": ["lady-gaga", "pop", "grammy", "hits"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_155",
        "text": "Ποιος επιδραστικός τραγουδοποιός από τη Θεσσαλονίκη εγκαινίασε μια νέα εποχή στο ελληνικό τραγούδι με δίσκους όπως «Το φορτηγό», «Το περιβόλι του τρελού» και «Μπάλλος»;",
        "answers": [
            "Διονύσης Σαββόπουλος",
            "Λουκιανός Κηλαηδόνης",
            "Βασίλης Παπακωνσταντίνου",
            "Νικόλας Άσιμος"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Διονύσης Σαββόπουλος (γνωστός και ως Νιόνιος) συνδύασε μοναδικά την αμερικανική φολκ του Bob Dylan με την ελληνική δημοτική και λαϊκή παράδοση.",
        "funFacts": [
            "Το 1983 παρουσίασε τη θρυλική τηλεοπτική εκπομπή 'Ζήτω το ελληνικό τραγούδι' στην ΕΡΤ, δίνοντας βήμα σε δεκάδες νέους και καθιερωμένους καλλιτέχνες.",
            "Το τραγούδι του 'Ας κρατήσουν οι χοροί' αποτελεί έναν από τους πιο πολυτραγουδισμένους ύμνους συλλογικής χαράς στην Ελλάδα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%BF%CE%BD%CF%8D%CF%83%CE%B7%CF%82_%CE%A3%CE%B1%CE%B2%CE%B2%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["savvopoulos", "greek-music", "entechno", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_156",
        "text": "Ποιο παγκόσμιο χιτ των Coldplay βασίζεται σε ένα επιβλητικό μοτίβο εγχόρδων και αφηγείται την πτώση ενός βασιλιά, παίρνοντας τον τίτλο του από πίνακα της Frida Kahlo;",
        "answers": [
            "Yellow",
            "Viva la Vida",
            "Clocks",
            "The Scientist"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Viva la Vida' κυκλοφόρησε το 2008 και χάρισε στους Coldplay το πρώτο τους νούμερο 1 σινγκλ τόσο στα βρετανικά όσο και στα αμερικανικά charts.",
        "funFacts": [
            "Ο τίτλος στα ισπανικά σημαίνει 'Ζήτω η Ζωή' και είναι εμπνευσμένος από τον τελευταίο πίνακα με καρπούζια που ζωγράφισε η Μεξικανή ζωγράφος Frida Kahlo.",
            "Το εξώφυλλο του άλμπουμ 'Viva la Vida or Death and All His Friends' απεικονίζει τον διάσημο ιστορικό πίνακα του Eugène Delacroix 'Η Ελευθερία οδηγεί τον Λαό'."
        ],
        "source": "https://el.wikipedia.org/wiki/Viva_la_Vida",
        "locale": "el-GR",
        "tags": ["coldplay", "alternative", "rock", "charts"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_157",
        "text": "Ποιο έγχορδο μουσικό όργανο διαθέτει κυκλικό σώμα με τεντωμένη μεμβράνη σαν ταμπούρο και συνδέεται κατεξοχήν με την αμερικανική bluegrass και country μουσική;",
        "answers": [
            "Γιουκαλίλι",
            "Μαντολίνο",
            "Μπάντζο",
            "Σιτάρ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το μπάντζο αναπτύχθηκε στις ΗΠΑ από Αφρικανούς σκλάβους που προσάρμοσαν παραδοσιακά αφρικανικά έγχορδα όργανα, παράγοντας έναν έντονο μεταλλικό κρουστό ήχο.",
        "funFacts": [
            "Το κλασικό πεντάχορδο μπάντζο έχει μια ιδιαιτερότητα: η πέμπτη χορδή είναι πιο κοντή από τις άλλες και ξεκινά από κλειδί στο μέσο του μπράτσου.",
            "Ο Earl Scruggs τελειοποίησε το 1945 την τεχνική παιξίματος με τρία δάχτυλα (Scruggs style), η οποία καθόρισε τον ήχο της bluegrass μουσικής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%AC%CE%BD%CF%84%CE%B6%CE%BF",
        "locale": "el-GR",
        "tags": ["banjo", "instruments", "country", "bluegrass"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_158",
        "text": "Ποιο κλασικό ροκ κομμάτι των Rolling Stones του 1966 ξεχώρισε για το εξωτικό ινδικό σιτάρ που έπαιξε ο Brian Jones και τον στίχο «I see a red door and I want it painted black»;",
        "answers": [
            "Satisfaction",
            "Angie",
            "Jumpin' Jack Flash",
            "Paint It Black"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Paint It Black' κυκλοφόρησε το 1966 σε σύνθεση των Mick Jagger και Keith Richards και κατέκτησε την κορυφή των charts σε ΗΠΑ και Ηνωμένο Βασίλειο.",
        "funFacts": [
            "Ήταν το πρώτο τραγούδι με σιτάρ που έφτασε στο νούμερο ένα των charts στις Ηνωμένες Πολιτείες.",
            "Χρησιμοποιήθηκε εκτενώς ως μουσικό θέμα στους τίτλους τέλους της ταινίας 'Full Metal Jacket' (1987) του Stanley Kubrick."
        ],
        "source": "https://el.wikipedia.org/wiki/Paint_It_Black",
        "locale": "el-GR",
        "tags": ["rolling-stones", "rock", "60s", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_159",
        "text": "Ποιος εξαιρετικά δημοφιλής Έλληνας λαϊκός τραγουδιστής κυριάρχησε απόλυτα στις πωλήσεις δίσκων τη δεκαετία του '90 με τεράστιες επιτυχίες όπως «Ο αετός» και «Σώμα μου»;",
        "answers": [
            "Νότης Σφακιανάκης",
            "Σταμάτης Γονίδης",
            "Βασίλης Καρράς",
            "Πασχάλης Τερζής"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Νότης Σφακιανάκης υπήρξε ένας από τους εμπορικότερους τραγουδιστές στην ιστορία της ελληνικής δισκογραφίας, με συνεχόμενους πολυπλατινένιους δίσκους.",
        "funFacts": [
            "Μεγάλωσε στην Κω και ξεκίνησε την επαγγελματική του πορεία ως DJ πριν ασχοληθεί ενεργά με το τραγούδι.",
            "Το τραγούδι 'Ο αετός' (1995) έγινε ένα από τα πιο αναγνωρίσιμα και πολυτραγουδισμένα ζεϊμπέκικα της σύγχρονης λαϊκής μουσικής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%8C%CF%84%CE%B7%CF%82_%CE%A3%CF%86%CE%B1%CE%BA%CE%B9%CE%B1%CE%BD%CE%AC%CE%BA%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["sfakianakis", "laiko", "greek-music", "zeibekiko"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_160",
        "text": "Ποιο εικονικό (virtual) βρετανικό συγκρότημα δημιούργησαν ο μουσικός Damon Albarn και ο σκιτσογράφος Jamie Hewlett, αποτελούμενο από τέσσερις σχεδιασμένους χαρακτήρες (2-D, Murdoc, Noodle, Russel);",
        "answers": [
            "Daft Punk",
            "Gorillaz",
            "The Prodigy",
            "Massive Attack"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι Gorillaz σημείωσαν παγκόσμια επιτυχία αναμειγνύοντας εναλλακτικό ροκ, χιπ χοπ και ηλεκτρονική μουσική σε τραγούδια όπως 'Clint Eastwood' και 'Feel Good Inc.'.",
        "funFacts": [
            "Το Βιβλίο των Ρεκόρ Γκίνες αναγνωρίζει επισήμως τους Gorillaz ως το 'Πιο Επιτυχημένο Εικονικό Συγκρότημα' στον κόσμο.",
            "Στις ζωντανές τους συναυλίες οι πραγματικοί μουσικοί παίζουν συχνά πίσω από γιγαντοοθόνες όπου προβάλλονται κινούμενα σχέδια των χαρακτήρων."
        ],
        "source": "https://el.wikipedia.org/wiki/Gorillaz",
        "locale": "el-GR",
        "tags": ["gorillaz", "virtual-band", "alternative", "uk"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(questions)} questions to append.")
    validate_and_append('music', 'easy', 1, questions)

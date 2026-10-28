import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
    {
        "id": "music_easy_161",
        "text": "Ποιος αγαπημένος Έλληνας ροκ ερμηνευτής, αποκαλούμενος και «αιώνιος έφηβος», τραγούδησε ιστορικά κομμάτια όπως «Ελλάς», «Ο μαύρος γάτος» και «Πριν το τέλος»;",
        "answers": [
            "Βασίλης Παπακωνσταντίνου",
            "Παύλος Σιδηρόπουλος",
            "Δημήτρης Πουλικάκος",
            "Λαυρέντης Μαχαιρίτσας"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Βασίλης Παπακωνσταντίνου αποτελεί τη μεγαλύτερη μορφή του ελληνικού ροκ τραγουδιού για περισσότερες από πέντε δεκαετίες, γεμίζοντας σταθερά στάδια.",
        "funFacts": [
            "Τον Ιούνιο του 2023 γιόρτασε τα 50 του χρόνια στη δισκογραφία με μια ιστορική συναυλία στο Καλλιμάρμαρο Παναθηναϊκό Στάδιο μπροστά σε 50.000 θεατές.",
            "Ξεκίνησε τη σταδιοδρομία του τραγουδώντας πολιτικά τραγούδια του Μίκη Θεοδωράκη και του Μάνου Λοΐζου κατά τη μεταπολίτευση."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B7%CF%82_%CE%A0%CE%B1%CF%80%CE%B1%CE%BA%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["papakonstantinou", "rock", "greek-rock", "legends"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_162",
        "text": "Ποιο χορευτικό funk-rock τραγούδι των Queen βασίστηκε στη χαρακτηριστική γραμμή μπάσου του John Deacon και έγινε το πιο εμπορικό σινγκλ του συγκροτήματος παγκοσμίως;",
        "answers": [
            "Under Pressure",
            "Another One Bites the Dust",
            "Radio Ga Ga",
            "I Want to Break Free"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Another One Bites the Dust' (1980) κατέκτησε την πρώτη θέση στο αμερικανικό Billboard Hot 100 και πούλησε πάνω από 7 εκατομμύρια αντίτυπα.",
        "funFacts": [
            "Ο Michael Jackson ήταν εκείνος που παρότρυνε τον Freddie Mercury να κυκλοφορήσει το κομμάτι ως σινγκλ μετά από συναυλία των Queen στο Λος Άντζελες.",
            "Η χαρακτηριστική γραμμή του μπάσου εμπνεύστηκε άμεσα από το κομμάτι 'Good Times' του συγκροτήματος Chic."
        ],
        "source": "https://el.wikipedia.org/wiki/Another_One_Bites_the_Dust",
        "locale": "el-GR",
        "tags": ["queen", "funk-rock", "bass-line", "hits"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_163",
        "text": "Ποιο ξύλινο κρουστό όργανο αποτελείται από δύο κοίλα κοχύλια δεμένα με σπάγκο που εφαρμόζουν στα δάχτυλα και συνδέεται στενά με τον ισπανικό χορό φλαμένκο;",
        "answers": [
            "Μαράκες",
            "Κρόταλα",
            "Καστανιέτες",
            "Ντέφι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι καστανιέτες παράγουν έναν κοφτό κροταλιστό ήχο και χρησιμοποιούνται για να τονίζουν τον ρυθμό στους παραδοσιακούς ισπανικούς και ανδαλουσιανούς χορούς.",
        "funFacts": [
            "Το όνομά τους προέρχεται από την ισπανική λέξη 'castaña' (κάστανο) λόγω του σχήματος και του σκούρου ξύλου καστανιάς από το οποίο παραδοσιακά κατασκευάζονταν.",
            "Στο φλαμένκο, η καστανιέτα στο δεξί χέρι είναι ελαφρώς ψηλότερη σε τόνο (hembra) και παίζει τα γρήγορα περάσματα, ενώ του αριστερού (macho) κρατά τον βασικό παλμό."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%83%CF%84%CE%B1%CE%BD%CE%B9%CE%AD%CF%84%CE%B5%CF%82",
        "locale": "el-GR",
        "tags": ["castanets", "instruments", "flamenco", "spain"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_164",
        "text": "Ποια συγκινητική μπαλάντα της Adele με συνοδεία μόνο πιάνου έφτασε στην κορυφή των charts παγκοσμίως το 2011 με τον στίχο «Never mind, I'll find someone like you»;",
        "answers": [
            "Rolling in the Deep",
            "Set Fire to the Rain",
            "Hello",
            "Someone Like You"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Someone Like You' υπήρξε το πρώτο νούμερο 1 σινγκλ της Adele στο Ηνωμένο Βασίλειο, κερδίζοντας το βραβείο Grammy Καλύτερης Ποπ Σόλο Ερμηνείας.",
        "funFacts": [
            "Η ζωντανή της ερμηνεία στα βραβεία BRIT Awards το 2011 καθήλωσε το κοινό και εκτόξευσε τις πωλήσεις του άλμπουμ '21' σε πρωτοφανή επίπεδα.",
            "Το ασπρόμαυρο βιντεοκλίπ του τραγουδιού γυρίστηκε νωρίς το πρωί στους άδειους δρόμους του Παρισιού κατά μήκος του ποταμού Σηκουάνα."
        ],
        "source": "https://el.wikipedia.org/wiki/Someone_like_You_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9,_%CE%91%CE%BD%CF%84%CE%AD%CE%BB)",
        "locale": "el-GR",
        "tags": ["adele", "pop", "ballad", "piano"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_165",
        "text": "Ποια δημοφιλής Ελληνίδα τραγουδίστρια με τα χαρακτηριστικά γαλάζια μάτια εκπροσώπησε την Ελλάδα στη Eurovision το 1993 με το «Ελλάδα, χώρα του φωτός» και σάρωσε στα 90s με δίσκους του Φοίβου;",
        "answers": [
            "Καίτη Γαρμπή",
            "Δέσποινα Βανδή",
            "Έλλη Κοκκίνου",
            "Ευρυδίκη"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Καίτη Γαρμπή υπήρξε μία από τις πιο επιτυχημένες και λαοφιλείς τραγουδίστριες της δεκαετίας του 1990 με άλμπουμ όπως 'Αρχίζω πόλεμο' και 'Ευαισθησίες'.",
        "funFacts": [
            "Η εμφάνισή της στη Eurovision του 1993 με το περίφημο γαλάζιο φόρεμα της Σήλιας Κριθαριώτη έμεινε στην ιστορία του διαγωνισμού για το εντυπωσιακό μονοπλάνο του σκηνοθέτη.",
            "Είναι παντρεμένη με τον τραγουδιστή Διονύση Σχοινά από το 1997, μετά από μια πολυσυζητημένη πρόταση γάμου σε ζωντανή τηλεοπτική εκπομπή."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%AF%CF%84%CE%B7_%CE%93%CE%B1%CF%81%CE%BC%CF%80%CE%AE",
        "locale": "el-GR",
        "tags": ["garbi", "pop", "greek-music", "eurovision"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_166",
        "text": "Ποια θρυλική ακουστική μπαλάντα των Beatles με ερμηνεία του Paul McCartney και κουαρτέτο εγχόρδων κατέχει το ρεκόρ του τραγουδιού με τις περισσότερες διασκευές στην ιστορία;",
        "answers": [
            "Hey Jude",
            "Yesterday",
            "Let It Be",
            "Help!"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Yesterday' κυκλοφόρησε το 1965 και έχει καταγραφεί στο Βιβλίο των Ρεκόρ Γκίνες με περισσότερες από 2.200 επίσημες ηχογραφημένες διασκευές.",
        "funFacts": [
            "Η μελωδία ήρθε στον Paul McCartney στον ύπνο του σε όνειρο, και αρχικά χρησιμοποιούσε ως προσωρινούς στίχους τις λέξεις 'Scrambled eggs, oh my baby how I love your legs'.",
            "Ήταν το πρώτο τραγούδι των Beatles όπου έπαιξε μόνο ένα μέλος του συγκροτήματος χωρίς τους υπόλοιπους τρεις."
        ],
        "source": "https://el.wikipedia.org/wiki/Yesterday_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["beatles", "mccartney", "acoustic", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_167",
        "text": "Ποιο είναι το μεγαλύτερο και με τον χαμηλότερο (βαρύτερο) ήχο όργανο στην κατηγορία των ξύλινων πνευστών της συμφωνικής ορχήστρας, διαθέτοντας διπλή γλωττίδα;",
        "answers": [
            "Κλαρινέτο",
            "Όμποε",
            "Φαγκότο",
            "Κόρνο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το φαγκότο έχει έναν βαθύ, ζεστό και συχνά κωμικό ή επιβλητικό ήχο, αποτελώντας τη ραχοκοκαλιά των μπάσων στα ξύλινα πνευστά.",
        "funFacts": [
            "Εάν ξεδιπλωθεί ο εσωτερικός ξύλινος σωλήνας του φαγκότου, το συνολικό του μήκος φτάνει σχεδόν τα 2,5 μέτρα.",
            "Στο μουσικό παραμύθι 'Ο Πέτρος και ο Λύκος' του Prokofiev, το φαγκότο ενσαρκώνει με το βαρύ ηχόχρωμά του τον αυστηρό παππού."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B1%CE%B3%CE%BA%CF%8C%CF%84%CE%BF",
        "locale": "el-GR",
        "tags": ["bassoon", "instruments", "woodwinds", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_168",
        "text": "Ποια ρομαντική ακουστική μπαλάντα του Ed Sheeran από το άλμπουμ «÷» (Divide) έγινε ένας από τους πιο δημοφιλείς γαμήλιους χορούς παγκοσμίως;",
        "answers": [
            "Shape of You",
            "Thinking Out Loud",
            "Photograph",
            "Perfect"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Perfect' κυκλοφόρησε το 2017 και κατέκτησε την πρώτη θέση στα charts δεκάδων χωρών, συμπεριλαμβανομένου του Billboard Hot 100.",
        "funFacts": [
            "Ο Ed Sheeran ηχογράφησε ειδικές εκδοχές του τραγουδιού σε ντουέτο με την Beyoncé και με τον διάσημο Ιταλό τενόρο Andrea Bocelli (τιτλοφορούμενο 'Perfect Symphony').",
            "Το τραγούδι γράφτηκε για την τότε σύντροφό του και μετέπειτα σύζυγό του, Cherry Seaborn, την οποία γνώριζε από τα σχολικά του χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Perfect_(Ed_Sheeran_song)",
        "locale": "el-GR",
        "tags": ["ed-sheeran", "pop", "ballad", "wedding"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_169",
        "text": "Ποια σπουδαία Ελληνίδα ερμηνεύτρια του ελαφρού τραγουδιού με τη βελούδινη φωνή ερμήνευσε κλασικές επιτυχίες όπως «Αγόρι μου» και «Αν είναι η αγάπη αμαρτία»;",
        "answers": [
            "Τζένη Βάνου",
            "Ρένα Βλαχοπούλου",
            "Μαίρη Λίντα",
            "Ζωζώ Σαπουντζάκη"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Τζένη Βάνου (Ευγενία Βραχνού) υπήρξε η κατεξοχήν φωνή του ελληνικού ερωτικού και ελαφρού τραγουδιού στις δεκαετίες του 1960 και 1970.",
        "funFacts": [
            "Ο σπουδαίος συνθέτης Μίμης Πλέσσας υπήρξε ο μέντοράς της, ανακαλύπτοντάς την και γράφοντας για εκείνη μερικές από τις μεγαλύτερες επιτυχίες της.",
            "Βραβεύτηκε επανειλημμένα στο ιστορικό Φεστιβάλ Ελαφρού Τραγουδιού Θεσσαλονίκης."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CE%BD%CE%B7_%CE%92%CE%AC%CE%BD%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["vanou", "elafro-tragoudi", "greek-music", "plessas"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_170",
        "text": "Ποιο ανεβαστικό τραγούδι του Bob Marley and the Wailers, που κυκλοφόρησε το 1980 στο τελευταίο άλμπουμ του «Uprising», συνδύασε ρέγκε με στοιχεία ντίσκο;",
        "answers": [
            "Jamming",
            "Could You Be Loved",
            "Buffalo Soldier",
            "Is This Love"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Could You Be Loved' γνώρισε τεράστια διεθνή επιτυχία στα κλαμπ και στα charts, αποτελώντας ένα από τα πιο χορευτικά κομμάτια του Marley.",
        "funFacts": [
            "Το τραγούδι γράφτηκε σε ένα αεροπλάνο το 1979 ενώ το συγκρότημα ταξίδευε κατά τη διάρκεια περιοδείας.",
            "Στο τραγούδι ακούγεται το βραζιλιάνικο παραδοσιακό κρουστό όργανο cuíca, δίνοντας μια μοναδική λάτιν πινελιά."
        ],
        "source": "https://el.wikipedia.org/wiki/Could_You_Be_Loved",
        "locale": "el-GR",
        "tags": ["bob-marley", "reggae", "disco", "hits"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_171",
        "text": "Ποιο παραδοσιακό ινδικό έγχορδο όργανο με μεγάλο ηχείο από αποξηραμένη κολοκύθα διαδόθηκε στη δυτική ροκ από τον George Harrison των Beatles και τον Ravi Shankar;",
        "answers": [
            "Σαρόντ",
            "Ταμπούρα",
            "Σιτάρ",
            "Ούτι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το σιτάρ είναι το πιο γνωστό όργανο της ινδικής κλασικής μουσικής, έχοντας συμπαθητικές χορδές που δονούνται και παράγουν έναν εξωτικό αντηχητικό ήχο.",
        "funFacts": [
            "Ο George Harrison άρχισε να μαθαίνει σιτάρ το 1965 και το χρησιμοποίησε για πρώτη φορά στο τραγούδι των Beatles 'Norwegian Wood (This Bird Has Flown)'.",
            "Διαθέτει μετακινούμενα καμπύλα μεταλλικά τάστα και έως και 21 χορδές, εκ των οποίων οι περισσότερες δονούνται συμπαθητικά χωρίς να αγγίζονται."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B9%CF%84%CE%AC%CF%81",
        "locale": "el-GR",
        "tags": ["sitar", "instruments", "india", "beatles"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_172",
        "text": "Ποιο διάσημο dance-pop τραγούδι της Britney Spears από το άλμπουμ «In the Zone» (2003) περιείχε ένα χαρακτηριστικό ριφ εγχόρδων από ινδικό σάουντρακ και κέρδισε βραβείο Grammy;",
        "answers": [
            "Oops!... I Did It Again",
            "I'm a Slave 4 U",
            "Gimme More",
            "Toxic"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Toxic' θεωρείται ένα από τα κορυφαία ποπ κομμάτια της δεκαετίας του 2000, χαρίζοντας στην Britney Spears το μοναδικό της βραβείο Grammy.",
        "funFacts": [
            "Το διάσημο βιντεοκλίπ σε σκηνοθεσία Joseph Kahn παρουσίαζε την τραγουδίστρια ως μυστική πράκτορα και αεροσυνοδό.",
            "Το βασικό sample των βιολιών προέρχεται από το κομμάτι 'Tere Mere Beech Mein' της ινδικής ταινίας του Bollywood 'Ek Duuje Ke Liye' (1981)."
        ],
        "source": "https://el.wikipedia.org/wiki/Toxic_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["britney-spears", "pop", "dance", "grammy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_173",
        "text": "Ποιος αγαπημένος λαϊκός τραγουδιστής από τη Θεσσαλονίκη με τη χαρακτηριστική βαριά βραχνή φωνή αποθεώθηκε με επιτυχίες όπως «Δεν πάω πουθενά» και «Άσ' την να λέει»;",
        "answers": [
            "Βασίλης Καρράς",
            "Πασχάλης Τερζής",
            "Ζαφείρης Μελάς",
            "Μάκης Χριστοδουλόπουλος"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Βασίλης Καρράς (Βασίλης Κεσογλίδης) υπήρξε ένας από τους πιο αγαπητούς λαϊκούς καλλιτέχνες, με τεράστιο και πιστό κοινό σε όλη την Ελλάδα.",
        "funFacts": [
            "Το 2017 μπήκε στο Βιβλίο των Ρεκόρ Γκίνες όταν γέμισε το στάδιο Arena Armeec στη Σόφια της Βουλγαρίας με 17.000 θεατές (και άλλες 4.000 απ' έξω), όντας ο πρώτος Ευρωπαίος καλλιτέχνης που το κατάφερε.",
            "Πριν ξεκινήσει την καριέρα του στη νυχτερινή Θεσσαλονίκη, εργαζόταν ως μηχανικός αυτοκινήτων."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B7%CF%82_%CE%9A%CE%B1%CF%81%CF%81%CE%AC%CF%82",
        "locale": "el-GR",
        "tags": ["karras", "laiko", "greek-music", "thessaloniki"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_174",
        "text": "Ποια διάσημη ακουστική μπαλάντα των Rolling Stones κυκλοφόρησε το 1973 στο άλμπουμ «Goats Head Soup» και έγινε τεράστια επιτυχία με τον στίχο «Angie, Angie, when will those clouds all disappear?»;",
        "answers": [
            "Wild Horses",
            "Angie",
            "Ruby Tuesday",
            "As Tears Go By"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Angie' γράφτηκε κυρίως από τον κιθαρίστα Keith Richards και έφτασε στην κορυφή του Billboard Hot 100 στις ΗΠΑ.",
        "funFacts": [
            "Υπήρξαν πολλές φήμες ότι το τραγούδι γράφτηκε για την τότε σύζυγο του David Bowie, Angela, αλλά ο Keith Richards διευκρίνισε ότι ήταν εμπνευσμένο από τη νεογέννητη κόρη του Dandelion Angela.",
            "Το χαρακτηριστικό πιάνο στο τραγούδι παίχτηκε από τον Nicky Hopkins, έναν από τους πιο περιζήτητους session πιανίστες της ροκ ιστορίας."
        ],
        "source": "https://el.wikipedia.org/wiki/Angie_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["rolling-stones", "rock", "ballad", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_175",
        "text": "Ποια κυκλικά μεταλλικά κρουστά όργανα από κράμα ορείχαλκου ή μπρούντζου παίζονται είτε συγκρουόμενα μεταξύ τους σε ζεύγος είτε χτυπώμενα με μπαγκέτα πάνω σε βάση;",
        "answers": [
            "Τρίγωνα",
            "Ταμπούρα",
            "Πιατίνια",
            "Καμπάνες"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Τα πιατίνια (κύμβαλα) παράγουν έναν εκρηκτικό, διαπεραστικό ήχο και χρησιμοποιούνται τόσο στις συμφωνικές ορχήστρες όσο και στα σύγχρονα ντραμς (crash, ride, splash).",
        "funFacts": [
            "Η ιστορική εταιρεία κατασκευής πιατινιών Zildjian ιδρύθηκε στην Κωνσταντινούπολη το 1623 από τον Αρμένιο αλχημιστή Avedis Zildjian και λειτουργεί αδιάλειπτα μέχρι σήμερα.",
            "Η λέξη 'Zildjian' στην αρμενική/τουρκική σημαίνει κυριολεκτικά 'γιος του κατασκευαστή κυμβάλων' (zil = κύμβαλο)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CE%B1%CF%84%CE%AF%CE%BD%CE%B9%CE%B1",
        "locale": "el-GR",
        "tags": ["cymbals", "instruments", "percussion", "drums"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_176",
        "text": "Ποιο σαρωτικό ποπ τραγούδι της Taylor Swift από το άλμπουμ «1989» αποτέλεσε έναν ύμνο αδιαφορίας απέναντι στην αρνητική κριτική και έφτασε κατευθείαν στο #1 του Billboard;",
        "answers": [
            "Blank Space",
            "Bad Blood",
            "Anti-Hero",
            "Shake It Off"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Shake It Off' σηματοδότησε την πλήρη μετάβαση της Taylor Swift από την country μουσική στην mainstream pop σκηνή το 2014.",
        "funFacts": [
            "Το βιντεοκλίπ του τραγουδιού περιλάμβανε επαγγελματίες χορευτές διαφόρων ειδών (μπαλέτο, hip hop, cheerleader), με τη Swift να προσπαθεί χιουμοριστικά να ακολουθήσει τα βήματά τους.",
            "Είναι ένα από τα ελάχιστα βιντεοκλίπ στην ιστορία του YouTube που έχουν ξεπεράσει τα 3 δισεκατομμύρια προβολές."
        ],
        "source": "https://el.wikipedia.org/wiki/Shake_It_Off",
        "locale": "el-GR",
        "tags": ["taylor-swift", "pop", "charts", "dance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_177",
        "text": "Ποιος καταξιωμένος Έλληνας ερμηνευτής από τη Χαλκιδική ερμήνευσε διαχρονικά τραγούδια κορυφαίων συνθετών, όπως «Ποτέ» και «Ο Γιάννης ο φονιάς»;",
        "answers": [
            "Μανώλης Μητσιάς",
            "Γιώργος Νταλάρας",
            "Δημήτρης Μητροπάνος",
            "Χαράλαμπος Γαργανουράκης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Μανώλης Μητσιάς πρωτοεμφανίστηκε στα τέλη της δεκαετίας του 1960 και διακρίνεται για τη σταθερή, ευγενική και καθαρή ερμηνεία του.",
        "funFacts": [
            "Το τραγούδι του 'Στην Ελευσίνα μια φορά' σε μουσική Δήμου Μούτση αποτέλεσε το διαβατήριό του για την πανελλήνια αναγνώριση το 1969.",
            "Έχει ερμηνεύσει σε πρώτη εκτέλεση έργα των σημαντικότερων Ελλήνων συνθετών, ανάμεσα στους οποίους οι Μάνος Χατζιδάκις, Μίκης Θεοδωράκης, Λουκιανός Κηλαηδόνης και Σταμάτης Κραουνάκης."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%8E%CE%BB%CE%B7%CF%82_%CE%9C%CE%B7%CF%84%CF%83%CE%B9%CE%AC%CF%82",
        "locale": "el-GR",
        "tags": ["mitsias", "greek-music", "entechno", "laiko"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_178",
        "text": "Ποιο κορυφαίο χορευτικό κομμάτι του Michael Jackson από το άλμπουμ «Thriller» περιέχει μια από τις πιο διάσημες μπασογραμμές στην ποπ και συνοδεύτηκε από το πρώτο «moonwalk»;",
        "answers": [
            "Beat It",
            "Billie Jean",
            "Smooth Criminal",
            "Wanna Be Startin' Somethin'"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Billie Jean' κυκλοφόρησε το 1983 σε παραγωγή του Quincy Jones και αποτέλεσε το τραγούδι που καθιέρωσε τον Michael Jackson ως παγκόσμιο φαινόμενο.",
        "funFacts": [
            "Ο παραγωγός Quincy Jones δεν ήθελε αρχικά να συμπεριλάβει το τραγούδι στο άλμπουμ επειδή δεν του άρεσε η εισαγωγή του μπάσου, αλλά ο Jackson επέμεινε λέγοντας ότι τον έκανε να θέλει να χορέψει.",
            "Ήταν το πρώτο βιντεοκλίπ μαύρου καλλιτέχνη που παίχτηκε σε συνεχή βαριά περιστροφή (heavy rotation) από το τηλεοπτικό κανάλι MTV, σπάζοντας τα τότε φυλετικά εμπόδια."
        ],
        "source": "https://el.wikipedia.org/wiki/Billie_Jean",
        "locale": "el-GR",
        "tags": ["michael-jackson", "billie-jean", "moonwalk", "pop"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_179",
        "text": "Ποιο παραδοσιακό έγχορδο μουσικό όργανο με μεγάλο αχλαδόσχημο σώμα και τέσσερα ζεύγη χορδών συνοδεύει παραδοσιακά τη λύρα ή το βιολί στα νησιά και την Κρήτη;",
        "answers": [
            "Μπουζούκι",
            "Κιθάρα",
            "Λαούτο",
            "Κανονάκι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το λαούτο κρατά τον ρυθμό και την αρμονία στις παραδοσιακές ορχήστρες, ενώ στην Κρήτη οι δεξιοτέχνες παίζουν και εντυπωσιακά σόλο περάσματα.",
        "funFacts": [
            "Παίζεται με ένα μακρύ φτερό αρπακτικού πτηνού (ή σύγχρονη πλαστική πένα) που χτυπά με δύναμη τις διπλές χορδές.",
            "Ιστορικά κατάγεται από το αραβικό ούτι (al-ud), το οποίο εισήχθη στην Ευρώπη κατά τον Μεσαίωνα και εξελίχθηκε στο δυτικό λαούτο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B1%CE%BF%CF%8D%CF%84%CE%BF",
        "locale": "el-GR",
        "tags": ["laouto", "instruments", "crete", "folk-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_180",
        "text": "Ποια μελαγχολική μπαλάντα της Billie Eilish από την ταινία «Barbie» (2023) κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού και το Grammy Τραγουδιού της Χρονιάς;",
        "answers": [
            "Bad Guy",
            "Ocean Eyes",
            "Happier Than Ever",
            "What Was I Made For?"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το τραγούδι γράφτηκε από την Billie Eilish και τον αδελφό της Finneas O'Connell ειδικά για την ταινία Barbie της Greta Gerwig.",
        "funFacts": [
            "Η νίκη της Billie Eilish στα Όσκαρ το 2024 την κατέστησε το νεότερο άτομο στην ιστορία του κινηματογράφου με δύο Όσκαρ (σε ηλικία 22 ετών).",
            "Το επίσημο βιντεοκλίπ σκηνοθετήθηκε από την ίδια και την απεικονίζει να τακτοποιεί ρούχα κούκλας Barbie σε μέγεθος μινιατούρας."
        ],
        "source": "https://en.wikipedia.org/wiki/What_Was_I_Made_For%3F",
        "locale": "el-GR",
        "tags": ["billie-eilish", "barbie", "oscars", "ballad"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_181",
        "text": "Ποιος σπουδαίος Έλληνας κιθαρίστας και τραγουδοποιός ρομά καταγωγής σφράγισε το κοινωνικό τραγούδι με την κιθάρα του και τη βραχνή φωνή του σε κομμάτια όπως «Η αγάπη όλα τα υπομένει»;",
        "answers": [
            "Κώστας Χατζής",
            "Γιώργος Μαργαρίτης",
            "Μανώλης Αγγελόπουλος",
            "Βασίλης Παϊτέρης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Κώστας Χατζής εισήγαγε το στυλ του σύγχρονου τροβαδούρου στην Ελλάδα, ερμηνεύοντας μπαλάντες με έντονα μηνύματα κατά του ρατσισμού και της κοινωνικής αδικίας.",
        "funFacts": [
            "Το 1976 κυκλοφόρησε μαζί με τη Μαρινέλλα τον τριπλό δίσκο 'Ρεσιτάλ', ο οποίος πούλησε εκατοντάδες χιλιάδες αντίτυπα και έγραψε ιστορία.",
            "Τραγούδησε στο κτίριο των Ηνωμένων Εθνών στη Νέα Υόρκη, αποσπώντας τιμητική διάκριση για το έργο του υπέρ των ανθρωπίνων δικαιωμάτων."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CF%83%CF%84%CE%B1%CF%82_%CE%A7%CE%B1%CF%84%CE%B6%CE%AE%CF%82",
        "locale": "el-GR",
        "tags": ["chatzis", "guitar", "greek-music", "ballads"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_182",
        "text": "Ποια τεράστια επιτυχία των ABBA του 1975 με το χαρακτηριστικό εισαγωγικό μοτίβο μαρίμπας έδωσε αργότερα το όνομά της στο επιτυχημένο μιούζικαλ και στις ταινίες;",
        "answers": [
            "Fernando",
            "Mamma Mia",
            "Waterloo",
            "SOS"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Mamma Mia' αποτέλεσε το τραγούδι που επιβεβαίωσε ότι οι ABBA δεν ήταν απλώς ένα εφήμερο συγκρότημα μιας επιτυχίας της Eurovision.",
        "funFacts": [
            "Η ιταλική έκφραση 'Mamma Mia' σημαίνει 'Μητέρα μου!' και χρησιμοποιείται συχνά στην καθομιλουμένη για να δηλώσει έκπληξη ή απόγνωση.",
            "Το μιούζικαλ 'Mamma Mia!' που βασίστηκε στα τραγούδια του συγκροτήματος έκανε πρεμιέρα στο Λονδίνο το 1999 και το έχουν παρακολουθήσει πάνω από 65 εκατομμύρια θεατές παγκοσμίως."
        ],
        "source": "https://el.wikipedia.org/wiki/Mamma_Mia_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["abba", "pop", "musical", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_183",
        "text": "Ποιο χάλκινο πνευστό μουσικό όργανο έχει κυκλικό περιελιγμένο σωλήνα με φαρδιά καμπάνα και παίζεται τοποθετώντας το δεξί χέρι του μουσικού μέσα στην καμπάνα;",
        "answers": [
            "Σάλπιγγα",
            "Κορνέτα",
            "Γαλλικό κόρνο",
            "Ευφώνιο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το γαλλικό κόρνο διαθέτει έναν ζεστό, ευγενικό και πλούσιο ήχο που γεφυρώνει ιδανικά τα ξύλινα με τα χάλκινα πνευστά της συμφωνικής ορχήστρας.",
        "funFacts": [
            "Εάν ξετυλιχθεί ο σωλήνας ενός σύγχρονου διπλού κόρνου, το συνολικό του μήκος ξεπερνά τα 5 μέτρα.",
            "Η τοποθέτηση του δεξιού χεριού μέσα στην καμπάνα ξεκίνησε ιστορικά ως τρόπος αλλαγής του τονικού ύψους πριν από την εφεύρεση των περιστροφικών βαλβίδων."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CF%81%CE%BD%CE%BF",
        "locale": "el-GR",
        "tags": ["french-horn", "brass", "instruments", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_184",
        "text": "Ποιο επαναστατικό grunge ροκ κομμάτι των Nirvana του 1991 ξεκινά με το διάσημο riff κιθάρας του Kurt Cobain και ανακηρύχθηκε από τα μέσα ενημέρωσης ως «ύμνος της γενιάς X»;",
        "answers": [
            "Come as You Are",
            "In Bloom",
            "Lithium",
            "Smells Like Teen Spirit"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Smells Like Teen Spirit' ανέτρεψε την κυριαρχία του hair metal και της pop στα αμερικανικά charts, εκτοξεύοντας το alternative rock στο παγκόσμιο προσκήνιο.",
        "funFacts": [
            "Ο τίτλος προήλθε όταν μια φίλη του Cobain έγραψε με σπρέι στον τοίχο του σπιτιού του 'Kurt smells like Teen Spirit' (το Teen Spirit ήταν μάρκα αποσμητικού που φορούσε η τότε κοπέλα του).",
            "Το εκρηκτικό βιντεοκλίπ εκτυλίσσεται σε ένα σχολικό γυμναστήριο με αναρχικές μαζορέτες και εξέγερση των μαθητών."
        ],
        "source": "https://el.wikipedia.org/wiki/Smells_Like_Teen_Spirit",
        "locale": "el-GR",
        "tags": ["nirvana", "grunge", "rock", "generation-x"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_185",
        "text": "Ποια δημοφιλής Ελληνίδα τραγουδίστρια σημείωσε τεράστια επιτυχία στη σύγχρονη λαϊκή δισκογραφία των 2000s με επιτυχίες όπως «Δυστυχώς», «Ματώνω» και «Είμαι καλά»;",
        "answers": [
            "Πέγκυ Ζήνα",
            "Νατάσα Θεοδωρίδου",
            "Έλλη Κοκκίνου",
            "Αγγελική Ηλιάδη"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Πέγκυ Ζήνα καθιερώθηκε ως μία από τις πιο αναγνωρίσιμες γυναικείες φωνές της νυχτερινής Αθήνας με συνεχόμενους πλατινένιους δίσκους.",
        "funFacts": [
            "Είναι κόρη της γνωστής τραγουδίστριας Στέλλας Χρυσικοπούλου.",
            "Το άλμπουμ της 'Ματώνω' (2004) απέσπασε διπλά πλατινένια διάκριση και περιείχε μερικές από τις μεγαλύτερες ραδιοφωνικές επιτυχίες της δεκαετίας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AD%CE%B3%CE%BA%CF%85_%CE%96%CE%AE%CE%BD%CE%B1",
        "locale": "el-GR",
        "tags": ["peggy-zina", "laiko", "greek-music", "2000s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_186",
        "text": "Ποια τρυφερή μπαλάντα του Elton John με στίχους του Bernie Taupin κυκλοφόρησε το 1970 και περιέχει τον περίφημο στίχο «How wonderful life is while you're in the world»;",
        "answers": [
            "Tiny Dancer",
            "Your Song",
            "Rocket Man",
            "Goodbye Yellow Brick Road"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Your Song' ήταν η πρώτη μεγάλη παγκόσμια επιτυχία του Elton John και παραμένει ένα από τα πιο αγαπημένα ερωτικά τραγούδια όλων των εποχών.",
        "funFacts": [
            "Ο στιχουργός Bernie Taupin έγραψε τους στίχους στο τραπέζι της κουζίνας της μητέρας του Elton John ενώ έτρωγε πρωινό, όντας μόλις 17 ετών.",
            "Ο John Lennon είχε δηλώσει τότε ότι ήταν το πρώτο πραγματικά σπουδαίο καινούργιο πράγμα στη μουσική μετά τη διάλυση των Beatles."
        ],
        "source": "https://el.wikipedia.org/wiki/Your_Song",
        "locale": "el-GR",
        "tags": ["elton-john", "pop", "ballad", "piano"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_187",
        "text": "Ποιο ζευγάρι ρυθμικών κρουστών οργάνων με λαβή περιέχει στο εσωτερικό του αποξηραμένους σπόρους ή χάντρες και παίζεται ανακινώντας τα ρυθμικά με τα χέρια;",
        "answers": [
            "Καστανιέτες",
            "Ντέφι",
            "Μαράκες",
            "Κουδούνες"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι μαράκες αποτελούν βασικό ρυθμικό στοιχείο στη μουσική λάτιν, τη σάλσα, το τσα-τσα-τσα και τη ρούμπα.",
        "funFacts": [
            "Κατάγονται από τους αυτόχθονες πληθυσμούς της Καραϊβικής (ιδίως τους Ταΐνο), οι οποίοι τις κατασκεύαζαν παραδοσιακά από αποξηραμένες κολοκύθες γεμισμένες με βότσαλα.",
            "Στις σύγχρονες παραγωγές κατασκευάζονται συχνά από ξύλο, δέρμα ή ανθεκτικό πλαστικό για να αντέχουν στην έντονη σκηνική χρήση."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AC%CE%BA%CE%B5%CF%82",
        "locale": "el-GR",
        "tags": ["maracas", "instruments", "percussion", "latin"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_188",
        "text": "Ποιο ιστορικό άλμπουμ των AC/DC του 1980 κυκλοφόρησε με κατάμαυρο εξώφυλλο ως φόρος τιμής στον εκλιπόντα τραγουδιστή Bon Scott και αποτέλεσε το ντεμπούτο του Brian Johnson;",
        "answers": [
            "Highway to Hell",
            "The Razors Edge",
            "Let There Be Rock",
            "Back in Black"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το άλμπουμ 'Back in Black' είναι το δεύτερο άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία της παγκόσμιας μουσικής μετά το 'Thriller' του Michael Jackson.",
        "funFacts": [
            "Η εισαγωγική καμπάνα στο ομώνυμο τραγούδι 'Hells Bells' ζύγιζε έναν τόνο και κατασκευάστηκε ειδικά για το συγκρότημα στο Loughborough της Αγγλίας.",
            "Έχει πουλήσει περισσότερα από 50 εκατομμύρια αντίτυπα παγκοσμίως."
        ],
        "source": "https://el.wikipedia.org/wiki/Back_in_Black",
        "locale": "el-GR",
        "tags": ["acdc", "hard-rock", "back-in-black", "rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_189",
        "text": "Ποιος Έλληνας λαϊκός τραγουδιστής και συνθέτης από την Κύθνο σημείωσε τεράστια εμπορική επιτυχία τη δεκαετία του '90 με τραγούδια όπως «Όλα σ' αγαπάνε» και «Μια ματιά σου μόνο φτάνει»;",
        "answers": [
            "Σταμάτης Γονίδης",
            "Λευτέρης Πανταζής",
            "Άγγελος Διονυσίου",
            "Βασίλης Τερλέγκας"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Σταμάτης Γονίδης διακρίνεται για το ιδιαίτερο φωνητικό του στυλ με έντονα γυρίσματα και έχει γράψει δεκάδες επιτυχίες τόσο για τον ίδιο όσο και για άλλους καλλιτέχνες.",
        "funFacts": [
            "Πριν ασχοληθεί επαγγελματικά με το τραγούδι, ταξίδευε επί σειρά ετών ως ναυτικός στα καράβια.",
            "Έχει συγγράψει και εκδώσει βιβλία φιλοσοφικού και πνευματικού περιεχομένου."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B1%CE%BC%CE%AC%CF%84%CE%B7%CF%82_%CE%93%CE%BF%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["gonidis", "laiko", "greek-music", "kythnos"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_190",
        "text": "Ποιο πολιτικό τραγούδι των U2 από το άλμπουμ «War» (1983) ξεκινά με τον χαρακτηριστικό στρατιωτικό ρυθμό στα ντραμς από τον Larry Mullen Jr. και αναφέρεται στα γεγονότα του Ντέρι στη Βόρεια Ιρλανδία;",
        "answers": [
            "Pride (In the Name of Love)",
            "Sunday Bloody Sunday",
            "New Year's Day",
            "Bad"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Sunday Bloody Sunday' αποτελεί ένα από τα πιο δυναμικά τραγούδια διαμαρτυρίας των U2 κατά των συγκρούσεων στη Βόρεια Ιρλανδία.",
        "funFacts": [
            "Ο Bono εισήγαγε το τραγούδι στις ζωντανές συναυλίες λέγοντας ρητά στο κοινό: 'This song is not a rebel song, this song is Sunday Bloody Sunday'.",
            "Η περίφημη ζωντανή εκτέλεση στο άλμπουμ 'Under a Blood Red Sky' (1983) με τον Bono να ανεμίζει μια λευκή σημαία έγινε το οπτικό σύμβολο του συγκροτήματος."
        ],
        "source": "https://el.wikipedia.org/wiki/Sunday_Bloody_Sunday",
        "locale": "el-GR",
        "tags": ["u2", "rock", "protest-song", "ireland"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_191",
        "text": "Ποιο έγχορδο όργανο με δοξάρι είναι ελαφρώς μεγαλύτερο από το βιολί, είναι κουρδισμένο μια πέμπτη χαμηλότερα (Ντο-Σολ-Ρε-Λα) και διαβάζει παρτιτούρα στο κλειδί της άλτο;",
        "answers": [
            "Βιολί",
            "Βιολοντσέλο",
            "Βιόλα",
            "Κοντραμπάσο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η βιόλα καλύπτει τη μεσαία φωνή στην οικογένεια των εγχόρδων, προσφέροντας έναν πιο σκοτεινό, μεστό και ζεστό τόνο σε σχέση με το βιολί.",
        "funFacts": [
            "Ο Wolfgang Amadeus Mozart και ο Johann Sebastian Bach προτιμούσαν συχνά να παίζουν βιόλα όταν συμμετείχαν σε σύνολα μουσικής δωματίου.",
            "Είναι το μοναδικό σύγχρονο όργανο της ορχήστρας που χρησιμοποιεί κατά κύριο λόγο το κλειδί του Ντο (άλτο κλειδί) για τη σημειογραφία του."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CF%8C%CE%BB%CE%B1",
        "locale": "el-GR",
        "tags": ["viola", "instruments", "classical", "strings"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_192",
        "text": "Ποιο σινγκλ της Lady Gaga από το ντεμπούτο άλμπουμ της «The Fame» (2008) κατέκτησε την πρώτη θέση σε πάνω από 20 χώρες με τον στίχο «Can't read my, can't read my, no he can't read my poker face»;",
        "answers": [
            "Just Dance",
            "Paparazzi",
            "Alejandro",
            "Poker Face"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Poker Face' ήταν το σινγκλ με τις μεγαλύτερες πωλήσεις παγκοσμίως για το έτος 2009, ξεπερνώντας τα 9,8 εκατομμύρια αντίτυπα εκείνη τη χρονιά.",
        "funFacts": [
            "Το τραγούδι πιστοποιήθηκε ως Διαμαντένιο από την Ένωση Δισκογραφικών Εταιρειών των ΗΠΑ (RIAA) για πωλήσεις άνω των 10 εκατομμυρίων αντιτύπων.",
            "Η μελωδική γραμμή του ρεφρέν περιλαμβάνει ένα ηχητικό sample από το ντίσκο τραγούδι 'Ma Baker' (1977) των Boney M."
        ],
        "source": "https://el.wikipedia.org/wiki/Poker_Face",
        "locale": "el-GR",
        "tags": ["lady-gaga", "pop", "dance-pop", "hits"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_193",
        "text": "Ποιος κορυφαίος σύγχρονος λαϊκός τραγουδιστής από την Πυλαία Θεσσαλονίκης αγαπήθηκε για τη στιβαρή φωνή του σε επιτυχίες όπως «Άστατος», «Ο δικός μου ο δρόμος» και «Φαντάσου»;",
        "answers": [
            "Πασχάλης Τερζής",
            "Βασίλης Καρράς",
            "Ζαφείρης Μελάς",
            "Σταμάτης Γονίδης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Πασχάλης Τερζής θεωρείται ένας από τους σπουδαιότερους κλασικούς λαϊκούς ερμηνευτές της γενιάς του, με δεκάδες πλατινένιους δίσκους.",
        "funFacts": [
            "Ξεκίνησε να τραγουδά επαγγελματικά στη Θεσσαλονίκη στις αρχές της δεκαετίας του 1970, αλλά η πανελλήνια αναγνώριση ήρθε αργότερα, στη δεκαετία του 1990.",
            "Η κόρη του, Γιάννα Τερζή, ακολούθησε επίσης καριέρα στο τραγούδι και εκπροσώπησε την Ελλάδα στη Eurovision το 2018 με το 'Όνειρό μου'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CF%83%CF%87%CE%AC%CE%BB%CE%B7%CF%82_%CE%A4%CE%B5%CF%81%CE%B6%CE%AE%CF%82",
        "locale": "el-GR",
        "tags": ["terzis", "laiko", "greek-music", "thessaloniki"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_194",
        "text": "Ποιο μεγαλειώδες τραγούδι του Frank Sinatra του 1980 έγινε ο ανεπίσημος ύμνος της Νέας Υόρκης με τον θρυλικό στίχο «If I can make it there, I'll make it anywhere»;",
        "answers": [
            "My Way",
            "Theme from New York, New York",
            "Strangers in the Night",
            "Fly Me to the Moon"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Theme from New York, New York' γράφτηκε από τους John Kander και Fred Ebb για την ομώνυμη ταινία του Martin Scorsese (1977), αλλά απογειώθηκε παγκοσμίως από τη φωνή του Sinatra.",
        "funFacts": [
            "Το τραγούδι παίζεται παραδοσιακά από τα μεγάφωνα του σταδίου Yankee Stadium στο τέλος κάθε εντός έδρας αγώνα της ομάδας μπέιζμπολ New York Yankees.",
            "Στην ταινία του Scorsese το τραγούδι είχε ερμηνευτεί αρχικά από τη Liza Minnelli."
        ],
        "source": "https://el.wikipedia.org/wiki/Theme_from_New_York,_New_York",
        "locale": "el-GR",
        "tags": ["sinatra", "jazz", "swing", "new-york"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_195",
        "text": "Ποιο είναι το μεγαλύτερο σε διαστάσεις και με τον βαθύτερο (χαμηλότερο) ήχο όργανο στην οικογένεια των χάλκινων πνευστών της συμφωνικής ορχήστρας;",
        "answers": [
            "Τρομπόνι",
            "Κόρνο",
            "Τούμπα",
            "Ευφώνιο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η τούμπα παρέχει τη μπάσα αρμονική βάση στα χάλκινα πνευστά της συμφωνικής ορχήστρας και στις στρατιωτικές μπάντες.",
        "funFacts": [
            "Εφευρέθηκε στη Γερμανία το 1835 από τους Wilhelm Wieprecht και Johann Gottfried Moritz ως αντικαταστάτης του οφικλείδιου.",
            "Μια παραλλαγή της σχεδιασμένη ειδικά για παρελάσεις, ώστε να φοριέται γύρω από το σώμα του μουσικού, ονομάζεται σουζάφωνο (sousaphone)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF%CF%8D%CE%BC%CF%80%CE%B1",
        "locale": "el-GR",
        "tags": ["tuba", "brass", "instruments", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_196",
        "text": "Ποια εμβληματική πιανιστική μπαλάντα των Coldplay από το άλμπουμ «A Rush of Blood to the Head» (2002) συνδέθηκε με ένα διάσημο βιντεοκλίπ που εκτυλίσσεται εξ ολοκλήρου αντίστροφα;",
        "answers": [
            "Fix You",
            "Yellow",
            "Clocks",
            "The Scientist"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'The Scientist' γράφτηκε από τον Chris Martin και αποτελεί ένα από τα πιο αναγνωρίσιμα και συναισθηματικά τραγούδια του συγκροτήματος.",
        "funFacts": [
            "Για τις ανάγκες του βιντεοκλίπ, ο Chris Martin έπρεπε να μάθει να τραγουδά ολόκληρο το τραγούδι ανάποδα (φωνητικά), ώστε όταν το βίντεο προβληθεί αντίστροφα τα χείλη του να συγχρονίζονται με τη μουσική.",
            "Το βιντεοκλίπ κέρδισε τρία βραβεία στα MTV Video Music Awards το 2003."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Scientist",
        "locale": "el-GR",
        "tags": ["coldplay", "alternative-rock", "piano", "ballad"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_197",
        "text": "Ποια καταξιωμένη Ελληνίδα ερμηνεύτρια και συνθέτρια ξεκίνησε σε εφηβική ηλικία με τον Μίκη Θεοδωράκη και τον Μάνο Χατζιδάκι και ερμήνευσε διαχρονικά κομμάτια όπως «Δύο μέρες μόνο»;",
        "answers": [
            "Δήμητρα Γαλάνη",
            "Τάνια Τσανακλίδου",
            "Ελένη Βιτάλη",
            "Βίκυ Μοσχολιού"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Δήμητρα Γαλάνη έχει διαγράψει μια εντυπωσιακή πορεία άνω των 50 ετών στο ελληνικό τραγούδι, τόσο ως μοναδική φωνή όσο και ως συνθέτρια.",
        "funFacts": [
            "Την ανακάλυψε ο συνθέτης Δήμος Μούτσης όταν εκείνη ήταν μόλις 16 ετών και της εμπιστεύτηκε τραγούδια στον ιστορικό δίσκο 'Ένα χαμόγελο' (1969).",
            "Έχει γράψει μουσική για πολλές κινηματογραφικές ταινίες και τηλεοπτικές σειρές, αποσπώντας κρατικά βραβεία μουσικής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AE%CE%BC%CE%B7%CF%84%CF%81%CE%B1_%CE%93%CE%B1%CE%BB%CE%AC%CE%BD%CE%B7",
        "locale": "el-GR",
        "tags": ["galani", "greek-music", "entechno", "singers"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_198",
        "text": "Ποιο διάσημο ροκ τραγούδι των Fleetwood Mac γράφτηκε από τον Lindsey Buckingham ως απάντηση στον επώδυνο χωρισμό του με τη Stevie Nicks κατά τη διάρκεια των ηχογραφήσεων του άλμπουμ «Rumours»;",
        "answers": [
            "Dreams",
            "Go Your Own Way",
            "The Chain",
            "Don't Stop"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Go Your Own Way' (1976) ήταν το πρώτο σινγκλ από το ιστορικό άλμπουμ 'Rumours' και έγινε τεράστια επιτυχία σε ΗΠΑ και Βρετανία.",
        "funFacts": [
            "Η Stevie Nicks διαφωνούσε έντονα με τον στίχο 'Packing up, shacking up's all you wanna do' και ζητούσε να αφαιρεθεί, αλλά ο Buckingham αρνήθηκε.",
            "Το περιοδικό Rolling Stone το κατέταξε ανάμεσα στα 500 σπουδαιότερα τραγούδια όλων των εποχών."
        ],
        "source": "https://el.wikipedia.org/wiki/Go_Your_Own_Way",
        "locale": "el-GR",
        "tags": ["fleetwood-mac", "rock", "rumours", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_199",
        "text": "Ποιο ορχηστρικό κρουστό όργανο αποτελείται από κρεμαστούς κατακόρυφους μεταλλικούς σωλήνες κουρδισμένους σε συγκεκριμένες νότες και παίζεται χτυπώντας τους με ειδικό ξύλινο ή δερμάτινο σφυρί;",
        "answers": [
            "Ξυλόφωνο",
            "Τρίγωνο",
            "Σωληνωτές καμπάνες",
            "Γκονγκ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Οι σωληνωτές καμπάνες (tubular bells ή chimes) σχεδιάστηκαν για να αναπαράγουν τον επιβλητικό ήχο των εκκλησιαστικών καμπανών μέσα στην αίθουσα συναυλιών.",
        "funFacts": [
            "Το πρωτοποριακό ορχηστρικό άλμπουμ 'Tubular Bells' (1973) του Mike Oldfield ήταν ο πρώτος δίσκος που κυκλοφόρησε η δισκογραφική εταιρεία Virgin Records του Richard Branson.",
            "Το εισαγωγικό θέμα του 'Tubular Bells' έγινε παγκοσμίως διάσημο ως το βασικό μουσικό θέμα της κλασικής ταινίας τρόμου 'Ο Εξορκιστής' (The Exorcist)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%89%CE%BB%CE%B7%CE%BD%CF%89%CF%84%CE%AD%CF%82_%CE%BA%CE%B1%CE%BC%CF%80%CE%AC%CE%BD%CE%B5%CF%82",
        "locale": "el-GR",
        "tags": ["tubular-bells", "instruments", "percussion", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_200",
        "text": "Ποιο παγκόσμιο τραγούδι διαμαρτυρίας των Pink Floyd από το άλμπουμ «The Wall» (1979) περιέχει τον ιστορικό στίχο «We don't need no education» με τη συνοδεία παιδικής χορωδίας;",
        "answers": [
            "Comfortably Numb",
            "Money",
            "Wish You Were Here",
            "Another Brick in the Wall, Part 2"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Another Brick in the Wall, Part 2' ήταν το μοναδικό νούμερο 1 σινγκλ των Pink Floyd τόσο στο Ηνωμένο Βασίλειο όσο και στις ΗΠΑ.",
        "funFacts": [
            "Η παιδική χορωδία αποτελούνταν από 23 μαθητές του σχολείου Islington Green School του Λονδίνου, οι οποίοι ηχογραφήθηκαν μυστικά από τον παραγωγό χωρίς ειδική άδεια.",
            "Το τραγούδι απαγορεύτηκε από το καθεστώς του απαρτχάιντ στη Νότια Αφρική το 1980 όταν μαύροι μαθητές το υιοθέτησαν ως ύμνο διαμαρτυρίας κατά των φυλετικών διακρίσεων στα σχολεία."
        ],
        "source": "https://el.wikipedia.org/wiki/Another_Brick_in_the_Wall",
        "locale": "el-GR",
        "tags": ["pink-floyd", "the-wall", "progressive-rock", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_201",
        "text": "Ποιος διακεκριμένος Έλληνας συνθέτης και πιανίστας συνέθεσε το «Μάθημα Σολφέζ» για τη Eurovision του 1977 και έγραψε εμβληματικά soundtracks για τον ελληνικό κινηματογράφο και την τηλεόραση;",
        "answers": [
            "Γιώργος Χατζηνάσιος",
            "Γιάννης Σπανός",
            "Μίμης Πλέσσας",
            "Κώστας Χατζής"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Γιώργος Χατζηνάσιος υπήρξε πρωτοπόρος στην ανάμειξη κλασικής τεχνικής με το σύγχρονο ελληνικό τραγούδι και τη μουσική επένδυση σειρών.",
        "funFacts": [
            "Το 'Μάθημα Σολφέζ' σε στίχους Σέβης Τηλιακού ερμηνεύτηκε από τους Πασχάλη, Μπέσσυ Αργυράκη, Ρόμπερτ Ουίλιαμς και Μαριάννα Τόλη, κατακτώντας την 5η θέση στη Eurovision του 1977.",
            "Ξεκίνησε ως παιδί-θαύμα στο πιάνο από τη Θεσσαλονίκη και σε ηλικία 14 ετών έπαιζε ήδη επαγγελματικά σε ορχήστρες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8E%CF%81%CE%B3%CE%BF%CF%82_%CE%A7%CE%B1%CF%84%CE%B6%CE%B7%CE%BD%CE%AC%CF%83%CE%B9%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["chatzinasios", "greek-music", "eurovision", "soundtracks"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_202",
        "text": "Ποια διάσημη power ballad των Metallica από το «Black Album» (1991) ξεκινά με ένα χαρακτηριστικό άρπισμα ανοιχτών χορδών στην κιθάρα από τον James Hetfield;",
        "answers": [
            "Fade to Black",
            "Nothing Else Matters",
            "One",
            "The Unforgiven"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Nothing Else Matters' γράφτηκε από τον Hetfield ενώ μιλούσε στο τηλέφωνο με την κοπέλα του και έπαιζε τις τέσσερις ανοιχτές χορδές της κιθάρας με το ένα χέρι.",
        "funFacts": [
            "Αρχικά ο James Hetfield δεν σκόπευε να κυκλοφορήσει το τραγούδι θεωρώντας το πολύ προσωπικό και μη-metal, αλλά ο ντράμερ Lars Ulrich τον έπεισε να το συμπεριλάβουν στον δίσκο.",
            "Την ενορχήστρωση των συμφωνικών εγχόρδων στο τραγούδι έκανε ο διάσημος συνθέτης κινηματογραφικής μουσικής Michael Kamen."
        ],
        "source": "https://el.wikipedia.org/wiki/Nothing_Else_Matters",
        "locale": "el-GR",
        "tags": ["metallica", "metal", "ballad", "guitar"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_203",
        "text": "Ποιο βασικό τύμπανο του σετ ντραμς διαθέτει μια σειρά από μεταλλικά σύρματα (χορδιέρα) τεντωμένα στην κάτω μεμβράνη του, προσφέροντας έναν κοφτό και τραγανό ήχο;",
        "answers": [
            "Μπότα",
            "Τομ-τομ",
            "Ταμπούρο",
            "Τυμπάνιο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το ταμπούρο (snare drum) είναι το πιο κεντρικό τύμπανο στο σετ ντραμς και παίζεται με μπαγκέτες, δίνοντας το χαρακτηριστικό 'backbeat' στον δεύτερο και τέταρτο χρόνο.",
        "funFacts": [
            "Εξελίχθηκε ιστορικά από τα στρατιωτικά τύμπανα του Μεσαίωνα (tabor) που χρησιμοποιούνταν για τον συντονισμό των βημάτων των στρατιωτών.",
            "Ο εκτελεστής μπορεί να απενεργοποιήσει τη μεταλλική χορδιέρα με έναν μικρό μοχλό στο πλάι, μετατρέποντας τον ήχο του σε βαθύ τομ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CE%BC%CF%80%CE%BF%CF%8D%CF%81%CE%BF",
        "locale": "el-GR",
        "tags": ["snare-drum", "instruments", "drums", "percussion"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_204",
        "text": "Ποια εκρηκτική χορευτική ποπ επιτυχία της Whitney Houston από το 1987 κατέκτησε την πρώτη θέση σε πάνω από 15 χώρες και της χάρισε βραβείο Grammy;",
        "answers": [
            "How Will I Know",
            "Greatest Love of All",
            "I Have Nothing",
            "I Wanna Dance with Somebody (Who Loves Me)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'I Wanna Dance with Somebody' αποτέλεσε ένα από τα πιο αναγνωρίσιμα dance-pop κομμάτια της δεκαετίας του 1980.",
        "funFacts": [
            "Το τραγούδι έφτασε στο νούμερο 1 τόσο στο Billboard Hot 100 των ΗΠΑ όσο και στο Official Singles Chart του Ηνωμένου Βασιλείου.",
            "Το 2022 η ομώνυμη βιογραφική ταινία για τη ζωή της Whitney Houston πήρε τον τίτλο της από αυτό το θρυλικό τραγούδι."
        ],
        "source": "https://el.wikipedia.org/wiki/I_Wanna_Dance_with_Somebody_(Who_Loves_Me)",
        "locale": "el-GR",
        "tags": ["whitney-houston", "pop", "dance-pop", "80s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_205",
        "text": "Ποιος σύγχρονος Έλληνας λαϊκός τραγουδιστής κέρδισε το μουσικό τηλεοπτικό σόου «Dream Show» το 2007 και κυριάρχησε στα charts με επιτυχίες όπως «Εννοείται» και «Βάλτο τέρμα»;",
        "answers": [
            "Νίκος Οικονομόπουλος",
            "Κωνσταντίνος Αργυρός",
            "Νίκος Βέρτης",
            "Πέτρος Ιακωβίδης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Ο Νίκος Οικονομόπουλος καθιερώθηκε ως ένας από τους κορυφαίους σύγχρονους λαϊκούς ερμηνευτές με πολυάριθμες πολυπλατινένιες κυκλοφορίες.",
        "funFacts": [
            "Γεννήθηκε στην Πάτρα και ξεκίνησε να τραγουδά σε νυχτερινά κέντρα της Πελοποννήσου πριν από τη συμμετοχή του στο talent show.",
            "Διακρίνεται για την προσήλωσή του στο γνήσιο λαϊκό τραγούδι και τη βαθιά του θρησκευτική πίστη, την οποία εκφράζει ανοιχτά σε συνεντεύξεις του."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%9F%CE%B9%CE%BA%CE%BF%CE%BD%CE%BF%CE%BC%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["oikonomopoulos", "laiko", "greek-music", "charts"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_206",
        "text": "Ποιο εκρηκτικό hard rock τραγούδι των Guns N' Roses άνοιγε το άλμπουμ «Appetite for Destruction» (1987) με τη χαρακτηριστική κραυγή του Axl Rose «You know where you are? You're in the jungle, baby!»;",
        "answers": [
            "Paradise City",
            "Welcome to the Jungle",
            "Nightrain",
            "Mr. Brownstone"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Welcome to the Jungle' έγραψε ιστορία στο MTV και καθιέρωσε τους Guns N' Roses ως τη νέα δύναμη της παγκόσμιας hard rock σκηνής.",
        "funFacts": [
            "Οι στίχοι εμπνεύστηκαν από ένα πραγματικό περιστατικό όταν ένας άγνωστος άνδρας φώναξε αυτή τη φράση στον Axl Rose όταν εκείνος έφτασε για πρώτη φορά ως νεαρός στο Λος Άντζελες.",
            "Το κανάλι MTV αρχικά αρνούνταν να παίξει το βιντεοκλίπ, αλλά μετά από πιέσεις το πρόβαλε μία φορά στις 4 τα ξημερώματα της Κυριακής, προκαλώντας κατακλυσμό τηλεφωνημάτων από ενθουσιασμένους τηλεθεατές."
        ],
        "source": "https://el.wikipedia.org/wiki/Welcome_to_the_Jungle",
        "locale": "el-GR",
        "tags": ["guns-n-roses", "hard-rock", "axl-rose", "slash"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_207",
        "text": "Ποιο παραδοσιακό έγχορδο κρουστό μουσικό όργανο με τραπεζοειδές ξύλινο σχήμα και δεκάδες χορδές παίζεται χτυπώντας τες με δύο λεπτά ξύλινα ραβδάκια (μπαγκέτες/μπαγκετάκια);",
        "answers": [
            "Κανονάκι",
            "Τσέμπαλο",
            "Σαντούρι",
            "Ψαλτήρι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το σαντούρι αποτελεί βασικό όργανο της παραδοσιακής μουσικής του Αιγαίου, της Μικράς Ασίας και της Σμύρνης.",
        "funFacts": [
            "Η διάσημη Ελληνίδα σολίστ Αριστείδης Μόσχος και αργότερα η Αρετή Κετιμέ ανέδειξαν το σαντούρι στο σύγχρονο ελληνικό κοινό.",
            "Το όνομά του προέρχεται από την περσική λέξη 'santur', που σημαίνει 'εκατό χορδές'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%BD%CF%84%CE%BF%CF%8D%CF%81%CE%B9",
        "locale": "el-GR",
        "tags": ["santouri", "instruments", "traditional", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_208",
        "text": "Ποια γλυκιά ποπ μπαλάντα του Bruno Mars αποτέλεσε το ντεμπούτο σόλο σινγκλ του το 2010 και κατέκτησε την πρώτη θέση στο Billboard Hot 100 κερδίζοντας βραβείο Grammy;",
        "answers": [
            "Grenade",
            "Locked Out of Heaven",
            "When I Was Your Man",
            "Just the Way You Are"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Just the Way You Are' εκτόξευσε τη σόλο καριέρα του Bruno Mars, πουλώντας πάνω από 12 εκατομμύρια αντίτυπα παγκοσμίως.",
        "funFacts": [
            "Το τραγούδι γράφτηκε με πρόθεση να αποτελέσει έναν απλό, άμεσο και διαχρονικό ύμνο θαυμασμού προς μια γυναίκα, εμπνευσμένο από κλασικές μπαλάντες όπως το 'Wonderful Tonight' του Eric Clapton.",
            "Το βιντεοκλίπ χρησιμοποίησε μια πρωτότυπη τεχνική σχεδιασμού εικόνων με την ξετυλιγμένη μαγνητική ταινία μιας παλιάς κασέτας ήχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Just_the_Way_You_Are_(Bruno_Mars_song)",
        "locale": "el-GR",
        "tags": ["bruno-mars", "pop", "ballad", "grammy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_209",
        "text": "Ποια σπουδαία Ελληνίδα λαϊκή τραγουδίστρια με τη χαρακτηριστική δωρική και βαθιά φωνή καθιερώθηκε ερμηνεύοντας σε πρώτη εκτέλεση το «Χάθηκε το φεγγάρι» του Σταύρου Ξαρχάκου;",
        "answers": [
            "Βίκυ Μοσχολιού",
            "Πόλυ Πάνου",
            "Μαίρη Λίντα",
            "Δούκισσα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Η Βίκυ Μοσχολιού υπήρξε μία από τις μεγαλύτερες φωνές της ελληνικής μουσικής, ερμηνεύοντας κορυφαία τραγούδια των Ζαμπέτα, Ξαρχάκου, Σπανού και Καλδάρα.",
        "funFacts": [
            "Το 'Χάθηκε το φεγγάρι' τραγουδήθηκε στην ταινία 'Λόλα' (1964) με τον Νίκο Κούρκουλο και την Τζένη Καρέζη, εκτοξεύοντας την καριέρα της εν μία νυκτί.",
            "Υπήρξε η πρώτη λαϊκή τραγουδίστρια που εγκατέλειψε τα μεγάλα νυχτερινά μαγαζιά για να τραγουδήσει στις μπουάτ της Πλάκας, φέρνοντας το λαϊκό τραγούδι πιο κοντά στη νεολαία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%AF%CE%BA%CF%85_%CE%9C%CE%BF%CF%83%CF%87%CE%BF%CE%BB%CE%B9%CE%BF%CF%8D",
        "locale": "el-GR",
        "tags": ["moscholiou", "laiko", "greek-music", "xarchakos"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_easy_210",
        "text": "Ποια δραματική μπαλάντα του Phil Collins από την ομώνυμη ταινία του 1984 έφτασε στο νούμερο ένα του Billboard Hot 100 και προτάθηκε για Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού;",
        "answers": [
            "One More Night",
            "Against All Odds (Take a Look at Me Now)",
            "Another Day in Paradise",
            "A Groovy Kind of Love"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 1,
        "explanation": "Το 'Against All Odds' γράφτηκε από τον Phil Collins κατά τη διάρκεια του διαζυγίου του από την πρώτη του σύζυγο και αποτελεί μία από τις πιο διάσημες ερωτικές μπαλάντες των 80s.",
        "funFacts": [
            "Ήταν το πρώτο από τα επτά συνολικά νούμερο 1 σινγκλ που πέτυχε ο Phil Collins στο αμερικανικό Billboard Hot 100 ως σόλο καλλιτέχνης.",
            "Το 1999 η Mariah Carey ηχογράφησε μια εξαιρετικά επιτυχημένη διασκευή του τραγουδιού, η οποία έφτασε επίσης στο #1 των βρετανικών charts σε ντουέτο με τους Westlife."
        ],
        "source": "https://el.wikipedia.org/wiki/Against_All_Odds_(Take_a_Look_at_Me_Now)",
        "locale": "el-GR",
        "tags": ["phil-collins", "pop", "ballad", "soundtracks"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(questions)} questions to append.")
    validate_and_append('music', 'easy', 1, questions)

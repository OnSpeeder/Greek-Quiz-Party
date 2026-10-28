# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# 50 pop culture medium questions: pop_culture_med_161 to pop_culture_med_210
QUESTIONS = [
    {
        "id": "pop_culture_med_161",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο sitcom του CBS ακολουθεί τη ζωή μιας παρέας επιστημόνων και της γειτόνισσάς τους Penny;",
        "answers": ["The Big Bang Theory", "How I Met Your Mother", "Modern Family", "Brooklyn Nine-Nine"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'The Big Bang Theory' των Τσακ Λόρι και Μπιλ Πράντι προβλήθηκε για 12 σεζόν (2007-2019) και εξελίχθηκε στην πιο δημοφιλή τηλεοπτική κωμωδία των ΗΠΑ.",
        "funFacts": [
            "Ο Τζιμ Πάρσονς κέρδισε τέσσερα βραβεία Emmy για τον ρόλο του εκκεντρικού φυσικού Σέλντον Κούπερ.",
            "Ένα είδος μέλισσας (Euglossa bazinga) πήρε το όνομά του από τη διάσημη ατάκα 'Bazinga!' του Σέλντον."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Big_Bang_Theory",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "sitcom"]
    },
    {
        "id": "pop_culture_med_162",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος πρωταγωνίστησε ως ο αρχιτέκτονας Ted Mosby στη σειρά 'How I Met Your Mother';",
        "answers": ["Νιλ Πάτρικ Χάρις", "Τζος Ράντνορ", "Τζέισον Σίγκελ", "Πολ Ραντ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Τζος Ράντνορ (Josh Radnor) υποδύθηκε τον Τεντ Μόσμπι, ο οποίος αφηγείται στα παιδιά του πώς γνώρισε τη μητέρα τους.",
        "funFacts": [
            "Τη φωνή του μεσήλικα αφηγητή Τεντ στο μέλλον δάνειζε ο γνωστός ηθοποιός Μπομπ Σάγκετ.",
            "Όλες οι σκηνές με τα δύο παιδιά στον καναπέ γυρίστηκαν κατά τη διάρκεια της πρώτης σεζόν ώστε να μην μεγαλώσουν οι έφηβοι ηθοποιοί."
        ],
        "source": "https://en.wikipedia.org/wiki/How_I_Met_Your_Mother",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "himym"]
    },
    {
        "id": "pop_culture_med_163",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια είναι η ταυτότητα του μυστηριώδους ήρωα με το ψευδώνυμο 'Spiderman' της Marvel Comics;",
        "answers": ["Μπρους Γουέιν", "Κλαρκ Κεντ", "Πίτερ Πάρκερ", "Ματ Μέρντοκ"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Πίτερ Πάρκερ είναι ο αρχικός Spider-Man, δημιουργημένος από τους Σταν Λι και Στιβ Ντίτκο το 1962 (Amazing Fantasy #15).",
        "funFacts": [
            "Ο εκδότης Μάρτιν Γκούντμαν πίστευε αρχικά ότι ο Spider-Man θα αποτύγχανε επειδή 'ο κόσμος σιχαίνεται τις αράχνες'.",
            "Η εμβληματική φράση 'Με τη μεγάλη δύναμη έρχεται και μεγάλη ευθύνη' εμφανίστηκε αρχικά στο κείμενο του αφηγητή και αργότερα αποδόθηκε στον θείο Μπεν."
        ],
        "source": "https://en.wikipedia.org/wiki/Spider-Man",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "spiderman"]
    },
    {
        "id": "pop_culture_med_164",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος είναι ο διάσημος πειρατής καπετάνιος που υποδύθηκε ο Τζόνι Ντεπ στη σειρά ταινιών 'Οι Πειρατές της Καραϊβικής';",
        "answers": ["Κάπταιν Χουκ", "Έκτορ Μπαρμπόσα", "Ντέιβι Τζόουνς", "Τζακ Σπάροου"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Τζόνι Ντεπ ενσάρκωσε τον εκκεντρικό Captain Jack Sparrow, κερδίζοντας υποψηφιότητα για Όσκαρ Α' Ανδρικού Ρόλου για την πρώτη ταινία το 2003.",
        "funFacts": [
            "Ο Ντεπ βάσισε τη συμπεριφορά και τον τρόπο ομιλίας του Τζακ Σπάροου στον κιθαρίστα των Rolling Stones, Κιθ Ρίτσαρντς.",
            "Τα στελέχη της Disney φοβήθηκαν αρχικά ότι ο Ντεπ 'κατέστρεφε την ταινία' με την ιδιόρρυθμη ερμηνεία του, πριν η ταινία γίνει παγκόσμιος θρίαμβος."
        ],
        "source": "https://en.wikipedia.org/wiki/Jack_Sparrow",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "pirates"]
    },
    {
        "id": "pop_culture_med_165",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη τραγουδίστρια έγινε γνωστή ως μέλος των Destiny's Child πριν ακολουθήσει μια κολοσσιαία σόλο καριέρα;",
        "answers": ["Μπιγιονσέ", "Ριάνα", "Αλίσια Κις", "Σακίρα"],
        "correctAnswerIndex": 0,
        "explanation": "Η Μπιγιονσέ (Beyoncé Knowles) ηγήθηκε του R&B συγκροτήματος Destiny's Child προτού κυκλοφορήσει το ντεμπούτο σόλο άλμπουμ της 'Dangerously in Love' το 2003.",
        "funFacts": [
            "Η Μπιγιονσέ είναι η καλλιτέχνιδα με τα περισσότερα βραβεία Grammy στην ιστορία της μουσικής (πάνω από 32 βραβεία).",
            "Το 2024 έγινε η πρώτη μαύρη γυναίκα που έφτασε στο νούμερο 1 του Billboard Hot Country Songs με το τραγούδι 'Texas Hold 'Em'."
        ],
        "source": "https://en.wikipedia.org/wiki/Beyonc%C3%A9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "beyonce"]
    },
    {
        "id": "pop_culture_med_166",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ταινία τρόμου του 1996 σε σκηνοθεσία Γουές Κρέιβεν αναβίωσε το είδος του slasher με τη μάσκα Ghostface;",
        "answers": ["I Know What You Did Last Summer", "Scream", "The Ring", "Final Destination"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Scream' του Γουές Κρέιβεν και του σεναριογράφου Κέβιν Γουίλιαμσον σατίρισε και ανανέωσε τα κλισέ των ταινιών τρόμου με αυτοαναφορικό χιούμορ.",
        "funFacts": [
            "Η μάσκα του Ghostface ανακαλύφθηκε τυχαία από την παραγωγό Μαριάν Μανταλένα σε ένα εγκαταλελειμμένο σπίτι κατά τη διάρκεια αναζήτησης τοποθεσιών.",
            "Η διάσημη εναρκτήρια σκηνή με την Ντρου Μπάριμορ στο τηλέφωνο αποτελεί φόρο τιμής στο 'Psycho' του Χίτσκοκ."
        ],
        "source": "https://en.wikipedia.org/wiki/Scream_(1996_film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "horror", "scream"]
    },
    {
        "id": "pop_culture_med_167",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του γιγάντιου πράσινου τέρατος που δημιουργείται όταν ο επιστήμονας Μπρους Μπάνερ εξοργίζεται;",
        "answers": ["Thing", "Colossus", "Hulk", "Juggernaut"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Incredible Hulk δημιουργήθηκε από τον Σταν Λι και τον Τζακ Κίρμπι το 1962 μετά από ατύχημα με ακτίνες γάμμα.",
        "funFacts": [
            "Στο πρώτο κιόλας τεύχος, ο Hulk ήταν γκρίζος και όχι πράσινος, αλλά το χρώμα άλλαξε σε πράσινο λόγω προβλημάτων εκτύπωσης.",
            "Ο Σταν Λι δήλωσε ότι εμπνεύστηκε τον χαρακτήρα από τον συνδυασμό του Φρανκενστάιν και του Δρ. Τζέκιλ και κυρίου Χάιντ."
        ],
        "source": "https://en.wikipedia.org/wiki/Hulk",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "comics"]
    },
    {
        "id": "pop_culture_med_168",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος διάσημος μάγος είναι ο πιστός μέντορας του Χάρι Πότερ και διευθυντής του Χόγκουαρτς;",
        "answers": ["Σέβερους Σνέιπ", "Σίριους Μπλακ", "Ρέμους Λούπιν", "Άλμπους Ντάμπλντορ"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Άλμπους Πέρσιβαλ Γούλφρικ Μπράιαν Ντάμπλντορ θεωρείται ο ισχυρότερος μάγος της σύγχρονης εποχής στο σύμπαν της Τζ. Κ. Ρόουλινγκ.",
        "funFacts": [
            "Η λέξη 'dumbledore' είναι παλιά αγγλική λέξη της διαλέκτου του Ντέβον που σημαίνει 'βομβίνος' (μεγάλη αγριομέλισσα).",
            "Στις ταινίες τον ρόλο υποδύθηκε αρχικά ο Ρίτσαρντ Χάρις και μετά τον θάνατό του ο Μάικλ Γκάμπον."
        ],
        "source": "https://en.wikipedia.org/wiki/Albus_Dumbledore",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "harry_potter", "fantasy"]
    },
    {
        "id": "pop_culture_med_169",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό boy band της δεκαετίας του 2010 αποτελούνταν από τους Χάρι Στάιλς, Ζέιν Μάλικ, Λίαμ Πέιν, Λούι Τόμλινσον και Νάιαλ Χόραν;",
        "answers": ["One Direction", "The Wanted", "JLS", "Backstreet Boys"],
        "correctAnswerIndex": 0,
        "explanation": "Οι One Direction δημιουργήθηκαν το 2010 στο βρετανικό The X Factor υπό την καθοδήγηση του Σάιμον Κάουελ και κατέκτησαν παγκόσμια υστερία.",
        "funFacts": [
            "Κανένα από τα μέλη δεν πέρασε αρχικά στην κατηγορία 'Boys' ως σόλο τραγουδιστής στο X Factor πριν ενωθούν σε συγκρότημα.",
            "Έγιναν το πρώτο βρετανικό συγκρότημα στην ιστορία που είδε τα τέσσερα πρώτα άλμπουμ του να κάνουν ντεμπούτο στο νούμερο 1 των ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/One_Direction",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "one_direction"]
    },
    {
        "id": "pop_culture_med_170",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη πλατφόρμα σύντομων βίντεο ανήκει στην κινεζική εταιρεία ByteDance;",
        "answers": ["Instagram", "TikTok", "Snapchat", "Vine"],
        "correctAnswerIndex": 1,
        "explanation": "Το TikTok (γνωστό ως Douyin στην Κίνα) κυκλοφόρησε διεθνώς το 2017 μετά τη συγχώνευση με το Musical.ly και έγινε η πιο κατεβασμένη εφαρμογή στον κόσμο.",
        "funFacts": [
            "Ο αλγόριθμος συστάσεων της σελίδας 'For You' του TikTok θεωρείται ένας από τους πιο εξελιγμένους και εθιστικούς στον κόσμο των social media.",
            "Το τραγούδι 'Old Town Road' του Lil Nas X εκτοξεύτηκε στο νούμερο 1 χάρη στη viral επιτυχία του στο TikTok."
        ],
        "source": "https://en.wikipedia.org/wiki/TikTok",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tech", "social_media"]
    },
    {
        "id": "pop_culture_med_171",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός υποδύθηκε τον Τζακ Ντόσον στην ταινία 'Τιτανικός' (Titanic) του 1997;",
        "answers": ["Μπραντ Πιτ", "Ματ Ντέιμον", "Λεονάρντο Ντι Κάπριο", "Τομ Κρουζ"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Λεονάρντο Ντι Κάπριο πρωταγωνίστησε δίπλα στην Κέιτ Γουίνσλετ στο έπος του Τζέιμς Κάμερον, που κέρδισε 11 βραβεία Όσκαρ.",
        "funFacts": [
            "Τα σκίτσα στο μπλοκ του Τζακ στην ταινία, συμπεριλαμβανομένου του περίφημου πορτρέτου της Ρόουζ, τα σχεδίασε ο ίδιος ο σκηνοθέτης Τζέιμς Κάμερον.",
            "Η παγκόσμια επιτυχία της ταινίας δημιούργησε τη λεγόμενη 'Leo-Mania' στα τέλη των 90s."
        ],
        "source": "https://en.wikipedia.org/wiki/Titanic_(1997_film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "titanic"]
    },
    {
        "id": "pop_culture_med_172",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ποπ σταρ από τα Μπαρμπάντος κυκλοφόρησε τα smash hits 'Umbrella', 'Diamonds' και ίδρυσε την εταιρεία καλλυντικών Fenty Beauty;",
        "answers": ["Μπιγιονσέ", "Νίκι Μινάζ", "Κάρντι Μπι", "Ριάνα"],
        "correctAnswerIndex": 3,
        "explanation": "Η Ριάνα (Rihanna) έχει πουλήσει πάνω από 250 εκατομμύρια δίσκους και αναγνωρίστηκε ως εθνική ηρωίδα των Μπαρμπάντος το 2021.",
        "funFacts": [
            "Η Fenty Beauty έφερε επανάσταση στη βιομηχανία καλλυντικών λανσάροντας από την αρχή 40 διαφορετικές αποχρώσεις foundation.",
            "Το τραγούδι 'Umbrella' γράφτηκε αρχικά για την Μπρίτνεϊ Σπίαρς, η οποία όμως το απέρριψε."
        ],
        "source": "https://en.wikipedia.org/wiki/Rihanna",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "fashion"]
    },
    {
        "id": "pop_culture_med_173",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του κεντρικού πρωταγωνιστή στη σειρά manga και anime 'Dragon Ball' του Ακίρα Τοριγιάμα;",
        "answers": ["Σον Γκόκου", "Βεγκέτα", "Ναρούτο", "Λούφι"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Σον Γκόκου (Son Goku) είναι ένας πολεμιστής Σάγιαν που στάλθηκε στη Γη ως μωρό και εκπαιδεύτηκε στις πολεμικές τέχνες.",
        "funFacts": [
            "Ο Τοριγιάμα εμπνεύστηκε τον Γκόκου από τον Sun Wukong (Βασιλιά Πίθηκο) του κλασικού κινεζικού μυθιστορήματος 'Ταξίδι στη Δύση'.",
            "Η χαρακτηριστική επίθεση 'Kamehameha' πήρε το όνομά της από τον πρώτο βασιλιά της Χαβάης, Καμεχαμέχα Α'."
        ],
        "source": "https://en.wikipedia.org/wiki/Goku",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "anime", "dragon_ball"]
    },
    {
        "id": "pop_culture_med_174",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος Αμερικανός κωμικός υποδύθηκε τον Ace Ventura, τον Stanley Ipkiss στο 'The Mask' και τον Lloyd στο 'Dumb and Dumber' το 1994;",
        "answers": ["Άνταμ Σάντλερ", "Τζιμ Κάρεϊ", "Μάικ Μάγιερς", "Μπεν Στίλερ"],
        "correctAnswerIndex": 1,
        "explanation": "Το 1994 υπήρξε ιστορικό έτος για τον Τζιμ Κάρεϊ, καθώς κυκλοφόρησε τρεις διαδοχικές τεράστιες εισπρακτικές επιτυχίες μέσα σε μία χρονιά.",
        "funFacts": [
            "Ο Κάρεϊ έγινε ο πρώτος ηθοποιός στην ιστορία που έλαβε αμοιβή 20 εκατομμυρίων δολαρίων για μία μόνο ταινία ('The Cable Guy' το 1996).",
            "Η απίστευτη εκφραστικότητα του προσώπου του του χάρισε το προσωνύμιο 'Rubber Face' (λαστιχένιο πρόσωπο)."
        ],
        "source": "https://en.wikipedia.org/wiki/Jim_Carrey",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "comedy"]
    },
    {
        "id": "pop_culture_med_175",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα της φανταστικής πόλης όπου ζει η οικογένεια Σίμπσον στην ομώνυμη μακροβιότερη σειρά κινουμένων σχεδίων;",
        "answers": ["Κουαχόγκ", "Σάουθ Παρκ", "Σπρίνγκφιλντ", "Σέλμπιβιλ"],
        "correctAnswerIndex": 2,
        "explanation": "Οι Simpsons ζουν στο Springfield, μια πόλη που επιλέχθηκε επίτηδες από τον Ματ Γκρέινινγκ επειδή είναι ένα από τα πιο κοινά ονόματα πόλεων στις ΗΠΑ.",
        "funFacts": [
            "Ο Γκρέινινγκ επιβεβαίωσε το 2012 ότι εμπνεύστηκε το όνομα συγκεκριμένα από το Σπρίνγκφιλντ του Όρεγκον.",
            "Οι Σίμπσονς έχουν προβλέψει με αξιοσημείωτη ακρίβεια πολλά μελλοντικά γεγονότα, όπως την εκλογή Τραμπ και την εξαγορά της Fox από τη Disney."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Simpsons",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "simpsons"]
    },
    {
        "id": "pop_culture_med_176",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο superhero δίδυμο της Marvel αποτελείται από έναν ρακούν ονόματι Rocket και ένα ανθρωπόμορφο δέντρο;",
        "answers": ["Groot", "Drax", "Gamora", "Mantis"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Groot είναι ένα νοήμον πλάσμα που μοιάζει με δέντρο και σύντροφος του Rocket Raccoon στους 'Guardians of the Galaxy' (Φύλακες του Γαλαξία).",
        "funFacts": [
            "Τη χαρακτηριστική φωνή του Groot δανείζει ο Βιν Ντίζελ, ηχογραφώντας την ατάκα 'I am Groot' σε δεκάδες διαφορετικές γλώσσες.",
            "Ο Groot πρωτοεμφανίστηκε στα κόμικς το 1960 ως εξωγήινος εισβολέας που ήθελε να αιχμαλωτίσει ανθρώπους για πειράματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Groot",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "guardians_of_the_galaxy"]
    },
    {
        "id": "pop_culture_med_177",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια είναι η επίσημη ονομασία του επιτραπέζιου παιχνιδιού λέξεων που εφηύρε ο Άλφρεντ Μοσέρ Μπατς το 1938;",
        "answers": ["Boggle", "Scrabble", "Taboo", "Trivial Pursuit"],
        "correctAnswerIndex": 1,
        "explanation": "Το Scrabble είναι το πιο διάσημο παιχνίδι σταυρόλεξου στον κόσμο, διαθέσιμο σε 121 χώρες και περισσότερες από 30 γλώσσες.",
        "funFacts": [
            "Ο Μπατς υπολόγισε τη βαθμολογία κάθε γράμματος μελετώντας τη συχνότητα εμφάνισης των γραμμάτων στην πρώτη σελίδα των The New York Times.",
            "Το γράμμα Q και το γράμμα Z είναι τα πιο ακριβά γράμματα στην αγγλική έκδοση, αξίζοντας 10 πόντους το καθένα."
        ],
        "source": "https://en.wikipedia.org/wiki/Scrabble",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "board_games", "scrabble"]
    },
    {
        "id": "pop_culture_med_178",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά ταινιών επιστημονικής φαντασίας σκηνοθέτησε ο Τζορτζ Μίλερ, με πρωταγωνιστές τον Mel Gibson και αργότερα τον Tom Hardy;",
        "answers": ["Dune", "Escape from New York", "Mad Max", "Waterworld"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Mad Max' ξεκίνησε το 1979 στην Αυστραλία και το 'Mad Max: Fury Road' (2015) κέρδισε έξι βραβεία Όσκαρ.",
        "funFacts": [
            "Το πρώτο Mad Max γυρίστηκε με εξαιρετικά χαμηλό προϋπολογισμό και κατείχε για χρόνια το ρεκόρ Γκίνες για την πιο κερδοφόρα ταινία σε σχέση κόστους-εισπράξεων.",
            "Στο Fury Road, πάνω από το 80% των εφέ και των συγκρούσεων οχημάτων πραγματοποιήθηκαν με πραγματικά οχήματα στην έρημο της Ναμίμπια."
        ],
        "source": "https://en.wikipedia.org/wiki/Mad_Max",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "mad_max"]
    },
    {
        "id": "pop_culture_med_179",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια αμερικανική οικογένεια έγινε παγκόσμιο φαινόμενο των reality media με τη σειρά 'Keeping Up with the Kardashians';",
        "answers": ["Οικογένεια Χίλτον", "Οικογένεια Όσμπορν", "Οικογένεια Σμιθ", "Οικογένεια Καρντάσιαν-Τζένερ"],
        "correctAnswerIndex": 3,
        "explanation": "Η οικογένεια Kardashian-Jenner με επικεφαλής την Κρις Τζένερ και τις κόρες της Κιμ, Κόρτνεϊ, Κλόι, Κένταλ και Κάιλι δημιούργησαν μια αυτοκρατορία lifestyle.",
        "funFacts": [
            "Η σειρά προβλήθηκε για 20 σεζόν στο κανάλι E! από το 2007 έως το 2021, πριν μεταφερθεί στο Hulu.",
            "Η Κάιλι Τζένερ έγινε μία από τις νεότερες δισεκατομμυριούχους χάρη στην εταιρεία καλλυντικών Kylie Cosmetics."
        ],
        "source": "https://en.wikipedia.org/wiki/Keeping_Up_with_the_Kardashians",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "reality", "kardashians"]
    },
    {
        "id": "pop_culture_med_180",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του μαγικού δαχτυλιδιού που βρίσκει ο Μπίλμπο Μπάγκινς στο 'Χόμπιτ';",
        "answers": ["Το Ένα Δαχτυλίδι", "Το Δαχτυλίδι της Φωτιάς", "Το Δαχτυλίδι του Αέρα", "Το Δαχτυλίδι του Νερού"],
        "correctAnswerIndex": 0,
        "explanation": "Το Ένα Δαχτυλίδι (The One Ring) κατασκευάστηκε από τον Σάουρον στο Βουνό του Χαμού για να κυβερνά όλα τα υπόλοιπα Δαχτυλίδια της Δύναμης.",
        "funFacts": [
            "Η διάσημη επιγραφή του δαχτυλιδιού είναι γραμμένη στη Μαύρη Γλώσσα του Μόρντορ με χαρακτήρες Τένγκβαρ.",
            "Στο βιβλίο 'Το Χόμπιτ', ο Τόλκιν παρουσίασε αρχικά το δαχτυλίδι απλώς ως ένα μαγικό αντικείμενο αορατότητας, προτού αναπτύξει τη σκοτεινή του μυθολογία στον Άρχοντα των Δαχτυλιδιών."
        ],
        "source": "https://en.wikipedia.org/wiki/One_Ring",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "fantasy", "tolkien"]
    },
    {
        "id": "pop_culture_med_181",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον θρυλικό αρχαιοπώλη και τυχοδιώκτη Indiana Jones σε πέντε ταινίες από το 1981 έως το 2023;",
        "answers": ["Σον Κόνερι", "Χάρισον Φορντ", "Μάικλ Ντάγκλας", "Κερτ Ράσελ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Χάρισον Φορντ υποδύθηκε τον Ιντιάνα Τζόουνς ξεκινώντας με τους 'Κυνηγούς της Χαμένης Κιβωτού' (Raiders of the Lost Ark) σε σκηνοθεσία Στίβεν Σπίλμπεργκ.",
        "funFacts": [
            "Ο Τζορτζ Λούκας ονόμασε τον χαρακτήρα 'Indiana' από τον αγαπημένο του σκύλο ράτσας Alaskan Malamute.",
            "Ο Τομ Σέλεκ ήταν η αρχική επιλογή για τον ρόλο, αλλά αναγκάστηκε να αρνηθεί λόγω του συμβολαίου του για τη σειρά Magnum, P.I."
        ],
        "source": "https://en.wikipedia.org/wiki/Indiana_Jones",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "indiana_jones"]
    },
    {
        "id": "pop_culture_med_182",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του κακού αυτοκράτορα των Sith και κυρίαρχου της Γαλαξιακής Αυτοκρατορίας στο Star Wars;",
        "answers": ["Κόμης Ντούκου", "Νταρθ Μολ", "Πάλπατιν", "Κάιλο Ρεν"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Αυτοκράτορας Πάλπατιν (γνωστός και ως Darth Sidious) ενορχήστρωσε την πτώση της Δημοκρατίας και τη διάλυση των Jedi.",
        "funFacts": [
            "Τον ρόλο του Πάλπατιν ενσάρκωσε μοναδικά ο Σκωτσέζος ηθοποιός Ίαν ΜακΝτίαρμιντ σε όλες τις τριλογίες του Star Wars.",
            "Η περίφημη εντολή του για την εξόντωση των Jedi είναι το 'Order 66'."
        ],
        "source": "https://en.wikipedia.org/wiki/Palpatine",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "star_wars", "cinema"]
    },
    {
        "id": "pop_culture_med_183",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο παιχνίδι προσομοίωσης ζωής δημιουργήθηκε από τον Will Wright και την εταιρεία Maxis το 2000;",
        "answers": ["SimCity", "Animal Crossing", "Second Life", "The Sims"],
        "correctAnswerIndex": 3,
        "explanation": "Το 'The Sims' επέτρεψε στους παίκτες να δημιουργήσουν και να ελέγξουν ψηφιακούς ανθρώπους, εξελισσόμενο σε ένα από τα πιο επιτυχημένα franchises ηλεκτρονικών παιχνιδιών στην ιστορία.",
        "funFacts": [
            "Οι χαρακτήρες του παιχνιδιού μιλούν μια τεχνητή γλώσσα χωρίς νόημα που ονομάζεται 'Simlish'.",
            "Ο Ράιτ εμπνεύστηκε το παιχνίδι αφού έχασε το σπίτι και όλα τα υπάρχοντά του στη μεγάλη πυρκαγιά του Όουκλαντ το 1991."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Sims",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "sims"]
    },
    {
        "id": "pop_culture_med_184",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο animated franchise της DreamWorks ακολουθεί έναν πράσινο δράκο-κυνηγό ονόματι Toothless (Φαφούτης) και τον νεαρό Hiccup;",
        "answers": ["How to Train Your Dragon", "Shrek", "Madagascar", "The Croods"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'How to Train Your Dragon' (Πώς να Εκπαιδεύσετε τον Δράκο σας) βασίστηκε στη σειρά βιβλίων της Κρεσίντα Κάουελ και αγαπήθηκε παγκοσμίως.",
        "funFacts": [
            "Ο Toothless ανήκει στο σπάνιο και επικίνδυνο είδος δράκων 'Night Fury' (Οργή της Νύχτας).",
            "Οι κινήσεις και η συμπεριφορά του Toothless σχεδιάστηκαν με βάση πραγματικές γάτες, σκύλους και άλογα."
        ],
        "source": "https://en.wikipedia.org/wiki/How_to_Train_Your_Dragon_(film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "dragons"]
    },
    {
        "id": "pop_culture_med_185",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά παιχνιδιών περιλαμβάνει τους Assassin's Creed και αναπτύσσεται κυρίως από τη γαλλική εταιρεία;",
        "answers": ["Electronic Arts", "Ubisoft", "Square Enix", "Capcom"],
        "correctAnswerIndex": 1,
        "explanation": "Η Ubisoft κυκλοφόρησε το πρώτο 'Assassin's Creed' το 2007, δημιουργώντας ένα από τα πιο κερδοφόρα franchises ιστορικής δράσης και περιπέτειας.",
        "funFacts": [
            "Το παιχνίδι γεννήθηκε αρχικά ως spinoff του Prince of Persia με τίτλο 'Prince of Persia: Assassins'.",
            "Η συσκευή εικονικής πραγματικότητας που επιτρέπει την αναβίωση των γενετικών αναμνήσεων των προγόνων ονομάζεται 'Animus'."
        ],
        "source": "https://en.wikipedia.org/wiki/Assassin%27s_Creed",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "assassins_creed"]
    },
    {
        "id": "pop_culture_med_186",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου κακού μάγου με τη μορφή πνεύματος που προσπαθεί να κατακτήσει τον κόσμο στο Legend of Zelda;",
        "answers": ["Vaati", "Ghirahim", "Ganon", "Skull Kid"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Ganon (ή Ganondorf στην ανθρώπινη μορφή Gerudo) είναι ο αιώνιος ανταγωνιστής της σειράς Zelda και κάτοχος του Triforce of Power.",
        "funFacts": [
            "Στο πρωτότυπο παιχνίδι του 1986 για το NES, το όνομά του γράφτηκε κατά λάθος ως 'Gannon' με δύο 'n'.",
            "Στο The Legend of Zelda: Ocarina of Time (1998), αποκαλύφθηκε για πρώτη φορά η καταγωγή του ως ο μόνος άνδρας που γεννιέται στη φυλή Gerudo κάθε 100 χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Ganon",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "zelda"]
    },
    {
        "id": "pop_culture_med_187",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά βιβλίων και ταινιών της Στέφανι Μέγιερ παρουσιάζει τον έρωτα μεταξύ της Μπέλα Σουάν και του βρικόλακα Έντουαρντ Κάλεν;",
        "answers": ["The Vampire Diaries", "True Blood", "Buffy the Vampire Slayer", "Twilight"],
        "correctAnswerIndex": 3,
        "explanation": "Το 'Twilight' (Λυκόφως) ξεκίνησε το 2005 ως μυθιστόρημα και μεταφέρθηκε στον κινηματογράφο με πρωταγωνιστές τους Κρίστεν Στιούαρτ και Ρόμπερτ Πάτινσον.",
        "funFacts": [
            "Η Μέγιερ δήλωσε ότι η ιδέα για το Twilight της ήρθε κυριολεκτικά μέσα σε ένα όνειρο στις 2 Ιουνίου 2003.",
            "Η σειρά προκάλεσε την παγκόσμια διαμάχη των θαυμαστών ανάμεσα στην 'Team Edward' και την 'Team Jacob'."
        ],
        "source": "https://en.wikipedia.org/wiki/Twilight_(novel_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "twilight"]
    },
    {
        "id": "pop_culture_med_188",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος είναι ο διάσημος μυστικός πράκτορας με αριθμό μητρώου 007 που δημιούργησε ο Ίαν Φλέμινγκ το 1953;",
        "answers": ["Τζέιμς Μποντ", "Τζορτζ Σμάιλι", "Τζακ Ράιαν", "Χάρι Πάλμερ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο James Bond πρωτοεμφανίστηκε στο μυθιστόρημα 'Casino Royale' του Ίαν Φλέμινγκ το 1953.",
        "funFacts": [
            "Ο Φλέμινγκ επέλεξε το όνομα James Bond επειδή ήθελε ένα 'συνηθισμένο, βαρετό όνομα' και το πήρε από έναν διάσημο Αμερικανό ορνιθολόγο.",
            "Το '00' στον αριθμό πράκτορα της MI6 υποδηλώνει την 'άδεια να σκοτώνει' (licence to kill)."
        ],
        "source": "https://en.wikipedia.org/wiki/James_Bond",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "literature", "james_bond"]
    },
    {
        "id": "pop_culture_med_189",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο animation στούντιο της Ιαπωνίας ίδρυσαν οι Χαγιάο Μιγιαζάκι και Ισάο Τακαχάτα το 1985;",
        "answers": ["Toei Animation", "Studio Ghibli", "Madhouse", "Kyoto Animation"],
        "correctAnswerIndex": 1,
        "explanation": "Το Studio Ghibli δημιούργησε μερικά από τα πιο αναγνωρισμένα αριστουργήματα του παγκόσμιου animation, όπως τα 'Spirited Away', 'My Neighbor Totoro' και 'Princess Mononoke'.",
        "funFacts": [
            "Το Spirited Away κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2003, παραμένοντας η μόνη μη αγγλόφωνη ταινία που το έχει καταφέρει.",
            "Το όνομα 'Ghibli' προέρχεται από την αραβική λέξη για τον καυτό άνεμο της Σαχάρας και ήταν ιταλικό πολεμικό αεροσκάφος."
        ],
        "source": "https://en.wikipedia.org/wiki/Studio_Ghibli",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "anime", "ghibli"]
    },
    {
        "id": "pop_culture_med_190",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο μουσικό talent show δημιούργησε ο Σάιμον Κάουελ στο Ηνωμένο Βασίλειο το 2004;",
        "answers": ["Pop Idol", "The Voice", "The X Factor", "America's Got Talent"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'The X Factor' αντικατέστησε το Pop Idol και ανέδειξε παγκόσμια μουσικά φαινόμενα όπως οι One Direction, η Leona Lewis και οι Little Mix.",
        "funFacts": [
            "Ο όρος 'X Factor' αναφέρεται στην ανεξήγητη ποιότητα που κάνει κάποιον γεννημένο star.",
            "Το franchise μεταφέρθηκε σε περισσότερες από 50 χώρες σε όλο τον κόσμο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_X_Factor_(British_TV_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "music", "talent_shows"]
    },
    {
        "id": "pop_culture_med_191",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον εμβληματικό ρόλο του John Wick στην ομώνυμη σειρά ταινιών δράσης;",
        "answers": ["Τομ Κρουζ", "Κρίστιαν Μπέιλ", "Τζέισον Στέιθαμ", "Κιάνου Ριβς"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Κιάνου Ριβς πρωταγωνιστεί ως ο ασταμάτητος πρώην εκτελεστής John Wick, σε σκηνοθεσία Τσαντ Σταχέλσκι από το 2014.",
        "funFacts": [
            "Ο Ριβς εκτέλεσε πάνω από το 90% των επικίνδυνων σκηνών και των πυροβολισμών μόνος του, εκπαιδευόμενος στο Judo, Jiu-Jitsu και 3-Gun shooting.",
            "Η αφορμή για το μακελειό στην πρώτη ταινία ήταν η δολοφονία του κουταβιού του, που του είχε χαρίσει η εκλιπούσα σύζυγός του."
        ],
        "source": "https://en.wikipedia.org/wiki/John_Wick",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "action", "john_wick"]
    },
    {
        "id": "pop_culture_med_192",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του φανταστικού πλανήτη στον οποίο κατοικούν οι Na'vi στην ταινία 'Avatar';",
        "answers": ["Πανδώρα", "Αρράκις", "Κρύπτον", "Κοροσάντ"],
        "correctAnswerIndex": 0,
        "explanation": "Η Πανδώρα (Pandora) είναι ένας κατοικήσιμος εξωγήινος δορυφόρος που περιφέρεται γύρω από τον αέριο γίγαντα Polyphemus στο σύστημα του Alpha Centauri.",
        "funFacts": [
            "Η ατμόσφαιρα της Πανδώρας είναι τοξική για τους ανθρώπους, απαιτώντας τη χρήση ειδικών μασκών εξωτερικού χώρου (exopacks).",
            "Το πολύτιμο υπεραγώγιμο ορυκτό που εξορύσσουν οι άνθρωποι στην Πανδώρα ονομάζεται 'Unobtainium'."
        ],
        "source": "https://en.wikipedia.org/wiki/Pandora_(Avatar)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "avatar", "sci_fi"]
    },
    {
        "id": "pop_culture_med_193",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη τραγουδίστρια έγινε γνωστή στην εφηβεία της με το hit 'Ocean Eyes' και το άλμπουμ 'When We All Fall Asleep, Where Do We Go;';",
        "answers": ["Ολίβια Ροντρίγκο", "Μπίλι Άιλις", "Λόρντε", "Ντούα Λίπα"],
        "correctAnswerIndex": 1,
        "explanation": "Η Μπίλι Άιλις (Billie Eilish) έγραψε ιστορία το 2020 όταν κέρδισε και τα τέσσερα κύρια βραβεία Grammy (Καλύτερος Νέος Καλλιτέχνης, Δίσκος, Τραγούδι και Άλμπουμ της Χρονιάς) σε μία μόνο τελετή.",
        "funFacts": [
            "Έγραψε και ηχογράφησε τα περισσότερα από τα πρώτα της τραγούδια στο υπνοδωμάτιο του σπιτιού της μαζί με τον αδελφό της, Finneas O'Connell.",
            "Κέρδισε δύο Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού σε ηλικία μόλις 22 ετών (για το 'No Time to Die' και το 'What Was I Made For?')."
        ],
        "source": "https://en.wikipedia.org/wiki/Billie_Eilish",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "billie_eilish"]
    },
    {
        "id": "pop_culture_med_194",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου υπερήρωα της Marvel που τυφλώθηκε σε μικρή ηλικία αλλά απέκτησε υπεράνθρωπες αισθήσεις ραντάρ;",
        "answers": ["Iron Fist", "Moon Knight", "Daredevil", "Punisher"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Ματ Μέρντοκ είναι ο Daredevil (Ο Άνθρωπος Χωρίς Φόβο), δικηγόρος την ημέρα και τιμωρός του εγκλήματος τη νύχτα στη συνοικία Hell's Kitchen.",
        "funFacts": [
            "Ο Daredevil δημιουργήθηκε από τον Σταν Λι και τον Μπιλ Έβερετ το 1964.",
            "Η εμβληματική αναγέννηση του χαρακτήρα έγινε τη δεκαετία του '80 από τον σεναριογράφο και σκιτσογράφο Φρανκ Μίλερ."
        ],
        "source": "https://en.wikipedia.org/wiki/Daredevil_(Marvel_Comics_character)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "superheroes", "daredevil"]
    },
    {
        "id": "pop_culture_med_195",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ποπ σταρ εμφανίστηκε στο ημίχρονο του Super Bowl το 2023 αποκαλύπτοντας τη δεύτερη εγκυμοσύνη της;",
        "answers": ["Κέιτι Πέρι", "Lady Gaga", "Μπιγιονσέ", "Ριάνα"],
        "correctAnswerIndex": 3,
        "explanation": "Η Ριάνα επέστρεψε στη ζωντανή σκηνή στο Super Bowl LVII τον Φεβρουάριο του 2023, σε μια παράσταση πάνω σε αιωρούμενες πλατφόρμες.",
        "funFacts": [
            "Το σόου της ήταν το πιο δημοφιλές halftime show στην ιστορία του Super Bowl, ξεπερνώντας τα 121 εκατομμύρια τηλεθεατές.",
            "Δεν είχε κανέναν καλεσμένο καλλιτέχνη στη σκηνή, στηριζόμενη αποκλειστικά στη δική της παρουσία και δεκάδες χορευτές στα λευκά."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Bowl_LVII_halftime_show",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "super_bowl", "rihanna"]
    },
    {
        "id": "pop_culture_med_196",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου καφέ-εστιατορίου όπου δουλεύει ο Μπομπ Σφουγγαράκης;",
        "answers": ["Ο Τραγανός Κάβουρας", "Ο Κουβάς του Δολώματος", "Το Στέκι του Ναυτίλου", "Το Μυστικό Κοχύλι"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μπομπ Σφουγγαράκης εργάζεται ως ψήστης στον Τραγανό Κάβουρα (Krusty Krab), που ανήκει στον φιλάργυρο Ευγένιο Καβούρη.",
        "funFacts": [
            "Το κτίριο του Τραγανού Κάβουρα έχει το σχήμα μιας παραδοσιακής παγίδας για αστακούς.",
            "Η μυστική συνταγή του Καβουροπάτι (Krabby Patty) αποτελεί το κεντρικό μυστικό που προσπαθεί διαρκώς να κλέψει ο Πλαγκτόν."
        ],
        "source": "https://en.wikipedia.org/wiki/Krusty_Krab",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "spongebob"]
    },
    {
        "id": "pop_culture_med_197",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά μυστηρίου του Netflix ακολουθεί την κόρη της οικογένειας Addams στο σχολείο Nevermore Academy;",
        "answers": ["Chilling Adventures of Sabrina", "Wednesday", "Locke & Key", "Riverdale"],
        "correctAnswerIndex": 1,
        "explanation": "Η σειρά 'Wednesday' με πρωταγωνίστρια την Τζένα Ορτέγκα και σκηνοθέτη τον Τιμ Μπάρτον έγινε μία από τις πιο δημοφιλείς αγγλόφωνες σειρές του Netflix.",
        "funFacts": [
            "Ο χορός της Wednesday στο τραγούδι 'Goo Goo Muck' των The Cramps έγινε παγκόσμιο viral trend στο TikTok με το τραγούδι 'Bloody Mary' της Lady Gaga.",
            "Η Τζένα Ορτέγκα χορογράφησε μόνη της τη σκηνή του χορού εμπνευσμένη από βίντεο γοτθικών κλαμπ της δεκαετίας του '80."
        ],
        "source": "https://en.wikipedia.org/wiki/Wednesday_(TV_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "netflix", "wednesday"]
    },
    {
        "id": "pop_culture_med_198",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστικού χαρακτήρα που υποδύεται ο Κίλιαν Μέρφι στην ιστορική δραματική σειρά 'Peaky Blinders';",
        "answers": ["Άρθουρ Σέλμπι", "Τζον Σέλμπι", "Τόμας Σέλμπι", "Μάικλ Γκρέι"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Τόμας Σέλμπι είναι ο πανέξυπνος, ψυχρός και φιλόδοξος ηγέτης της συμμορίας Peaky Blinders στο Μπέρμιγχαμ μετά τον Α' Παγκόσμιο Πόλεμο.",
        "funFacts": [
            "Το όνομα Peaky Blinders προήλθε από τον αστικό μύθο ότι η συμμορία έραβε ξυραφάκια στο γείσο των τραγιάσκων της.",
            "Ο Κίλιαν Μέρφι κάπνισε πάνω από 3.000 τσιγάρα από βότανα (χωρίς καπνό και νικοτίνη) κατά τη διάρκεια των γυρισμάτων των σεζόν."
        ],
        "source": "https://en.wikipedia.org/wiki/Tommy_Shelby",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "peaky_blinders"]
    },
    {
        "id": "pop_culture_med_199",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο superhero team της DC Comics αποτελείται από τους Superman, Batman, Wonder Woman, Flash και Aquaman;",
        "answers": ["Teen Titans", "Suicide Squad", "The Watchmen", "Justice League"],
        "correctAnswerIndex": 3,
        "explanation": "Η Justice League of America (Λίγκα της Δικαιοσύνης) πρωτοεμφανίστηκε στο The Brave and the Bold #28 το 1960.",
        "funFacts": [
            "Η επιτυχία της Justice League ώθησε τον εκδότη της Marvel Μάρτιν Γκούντμαν να ζητήσει από τον Σταν Λι τη δημιουργία μιας δικής τους ομάδας, οδηγώντας στη γέννηση των Fantastic Four.",
            "Η έδρα της ομάδας είναι συχνά ο Watchtower (Παρατηρητήριο) σε τροχιά γύρω από τη Γη."
        ],
        "source": "https://en.wikipedia.org/wiki/Justice_League",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "dc", "superheroes", "justice_league"]
    },
    {
        "id": "pop_culture_med_200",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη κούκλα μόδας κυκλοφόρησε για πρώτη φορά από την εταιρεία Mattel στις 9 Μαρτίου 1959;",
        "answers": ["Μπάρμπι", "Μπρατζ", "Σίντι", "Πόλι Πόκετ"],
        "correctAnswerIndex": 0,
        "explanation": "Η Ρουθ Χάντλερ δημιούργησε την Μπάρμπι (Barbie, πλήρες όνομα Barbara Millicent Roberts), εμπνευσμένη από τη γερμανική κούκλα Bild Lilli.",
        "funFacts": [
            "Η πρώτη κούκλα Barbie φορούσε ένα ασπρόμαυρο ριγέ μαγιό και είχε τα μαλλιά της πιασμένα σε αλογοουρά.",
            "Η Ρουθ Χάντλερ ονόμασε την Barbie από την κόρη της Μπάρμπαρα και τον Ken από τον γιο της Κένεθ."
        ],
        "source": "https://en.wikipedia.org/wiki/Barbie",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "toys", "barbie"]
    },
    {
        "id": "pop_culture_med_201",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο franchise ταινιών επιστημονικής φαντασίας σκηνοθέτησε ο Στίβεν Σπίλμπεργκ το 1993, βασισμένο στο μυθιστόρημα του Μάικλ Κράιτον;",
        "answers": ["E.T.", "Jurassic Park", "Close Encounters of the Third Kind", "Minority Report"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Jurassic Park' έφερε επανάσταση στα ειδικά εφέ συνδυάζοντας ψηφιακά γραφικά υπολογιστή (CGI) από την ILM και animatronics του Σταν Γουίνστον.",
        "funFacts": [
            "Ο βρυχηθμός του T-Rex στην ταινία δημιουργήθηκε από τον σχεδιαστή ήχου Γκάρι Ράιντστρομ συνδυάζοντας ήχους από μωρό ελέφαντα, τίγρη και αλιγάτορα.",
            "Παρά τη διάρκειά της (127 λεπτά), η ταινία περιέχει μόλις 15 λεπτά πραγματικών πλάνων με δεινοσαύρους."
        ],
        "source": "https://en.wikipedia.org/wiki/Jurassic_Park_(film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "jurassic_park"]
    },
    {
        "id": "pop_culture_med_202",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου οίκου μόδας που ίδρυσε ο Ιταλός σχεδιαστής Τζιάνι Βερσάτσε το 1978;",
        "answers": ["Armani", "Gucci", "Versace", "Prada"],
        "correctAnswerIndex": 2,
        "explanation": "Ο οίκος Versace ιδρύθηκε στο Μιλάνο και έγινε παγκοσμίως γνωστός για τα τολμηρά χρώματα, τα λαμπερά prints και το λογότυπο με το κεφάλι της Μέδουσας.",
        "funFacts": [
            "Ο Τζιάνι επέλεξε το κεφάλι της Μέδουσας επειδή έκανε τους ανθρώπους να την ερωτεύονται κεραυνοβόλα και να μην μπορούν να ξεφύγουν.",
            "Μετά τη δολοφονία του Τζιάνι το 1997, η αδελφή του Ντονατέλα Βερσάτσε ανέλαβε την καλλιτεχνική ηγεσία του οίκου."
        ],
        "source": "https://en.wikipedia.org/wiki/Versace",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "fashion", "versace"]
    },
    {
        "id": "pop_culture_med_203",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του κακού cyborg δολοφόνου που έστειλε η Skynet πίσω στον χρόνο στην ταινία του Τζέιμς Κάμερον το 1984;",
        "answers": ["RoboCop", "Replicant", "Cylon", "Terminator"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Άρνολντ Σβαρτσενέγκερ ενσάρκωσε τον Cyberdyne Systems Model 101 (T-800) στην κλασική ταινία 'The Terminator'.",
        "funFacts": [
            "Ο Σβαρτσενέγκερ λέει μόλις 74 λέξεις σε ολόκληρη την πρώτη ταινία του 1984.",
            "Η ατάκα 'I'll be back' (Θα επιστρέψω) ψηφίστηκε ως μία από τις πιο διάσημες ατάκες στην ιστορία του σινεμά."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Terminator",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "terminator", "sci_fi"]
    },
    {
        "id": "pop_culture_med_204",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο τραγούδι της Adele κυκλοφόρησε το 2015 και έσπασε το ρεκόρ των ταχύτερων 1 δισεκατομμυρίου προβολών στο YouTube σε μόλις 87 ημέρες;",
        "answers": ["Hello", "Rolling in the Deep", "Someone Like You", "Easy on Me"],
        "correctAnswerIndex": 0,
        "explanation": "Το 'Hello' ήταν το πρώτο single από το τρίτο στούντιο άλμπουμ της Adele, '25', καταρρίπτοντας ρεκόρ πωλήσεων και streaming παγκοσμίως.",
        "funFacts": [
            "Το μουσικό βίντεο σε σκηνοθεσία Ξαβιέ Ντολάν γυρίστηκε σε αναλογία 4:3 και έγινε το πρώτο μουσικό κλιπ που χρησιμοποίησε κάμερες IMAX.",
            "Το άλμπουμ '25' πούλησε πάνω από 3,38 εκατομμύρια αντίτυπα μόνο στις ΗΠΑ μέσα στην πρώτη εβδομάδα κυκλοφορίας του."
        ],
        "source": "https://en.wikipedia.org/wiki/Hello_(Adele_song)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "adele"]
    },
    {
        "id": "pop_culture_med_205",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστικού χαρακτήρα και αρχηγού της συμμορίας στο βιντεοπαιχνίδι 'Red Dead Redemption 2' της Rockstar Games;",
        "answers": ["Τζον Μάρστον", "Άρθουρ Μόργκαν", "Ντατς βαν ντερ Λίντε", "Μίκα Μπελ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Άρθουρ Μόργκαν είναι ο τραγικός πρωταγωνιστής του 'Red Dead Redemption 2' (2018), ευρέως αναγνωρισμένος ως ένας από τους πιο καλογραμμένους χαρακτήρες στην ιστορία του gaming.",
        "funFacts": [
            "Ο ηθοποιός Ρότζερ Κλαρκ πέρασε πάνω από πέντε χρόνια κάνοντας performance capture και ηχογραφήσεις για τον ρόλο του Άρθουρ.",
            "Το παιχνίδι σημείωσε το δεύτερο μεγαλύτερο εμπορικό άνοιγμα στην ιστορία της ψυχαγωγίας, με 725 εκατομμύρια δολάρια μέσα σε τρεις μόλις ημέρες."
        ],
        "source": "https://en.wikipedia.org/wiki/Red_Dead_Redemption_2",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "rockstar"]
    },
    {
        "id": "pop_culture_med_206",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη κωμική σειρά του BBC και του NBC παρουσιάζει την καθημερινότητα των εργαζομένων στην εταιρεία χαρτιού Dunder Mifflin;",
        "answers": ["Parks and Recreation", "Community", "The Office", "Arrested Development"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'The Office' δημιουργήθηκε από τους Ρίκι Τζερβέις και Στίβεν Μέρτσαντ στο Ηνωμένο Βασίλειο και διασκευάστηκε με τεράστια επιτυχία στις ΗΠΑ με πρωταγωνιστή τον Στιβ Καρέλ (Μάικλ Σκοτ).",
        "funFacts": [
            "Η αμερικανική εκδοχή γυρίστηκε σε στυλ ψευδοντοκιμαντέρ (mockumentary) χωρίς ζωντανό κοινό ή κονσερβοποιημένα γέλια.",
            "Η ατάκα 'That's what she said' έγινε ένα από τα πιο αναγνωρίσιμα catchphrases της σύγχρονης τηλεόρασης."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Office_(American_TV_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "the_office"]
    },
    {
        "id": "pop_culture_med_207",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος σχεδιαστής κόμικς δημιούργησε τον χαρακτήρα του Hellboy για την Dark Horse Comics το 1993;",
        "answers": ["Μάικ Μινιόλα", "Τοντ ΜακΦάρλαν", "Φρανκ Μίλερ", "Άλαν Μουρ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μάικ Μινιόλα (Mike Mignola) δημιούργησε τον Hellboy, έναν δαίμονα που κλήθηκε στη Γη από ναζί αποκρυφιστές αλλά μεγάλωσε για να πολεμά το παραφυσικό κακό.",
        "funFacts": [
            "Ο Hellboy μεταφέρθηκε στον κινηματογράφο το 2004 σε σκηνοθεσία Γκιγιέρμο ντελ Τόρο με πρωταγωνιστή τον Ρον Πέρλμαν.",
            "Το δεξί του χέρι είναι φτιαγμένο από άφθαρτη πέτρα και ονομάζεται 'Το Δεξί Χέρι του Χαμού' (Right Hand of Doom)."
        ],
        "source": "https://en.wikipedia.org/wiki/Hellboy",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics", "hellboy"]
    },
    {
        "id": "pop_culture_med_208",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ποπ τραγουδίστρια έγινε γνωστή με το τραγούδι 'Genie in a Bottle' το 1999 και υπήρξε βασική 'αντίπαλος' της Britney Spears στα τέλη των 90s;",
        "answers": ["Τζέσικα Σίμπσον", "Κριστίνα Αγκιλέρα", "Μάντι Μουρ", "Πινκ"],
        "correctAnswerIndex": 1,
        "explanation": "Η Κριστίνα Αγκιλέρα (Christina Aguilera) αναδείχθηκε μέσα από το The Mickey Mouse Club και κέρδισε το Grammy Καλύτερου Νέου Καλλιτέχνη το 2000.",
        "funFacts": [
            "Η Αγκιλέρα είναι γνωστή για το τεράστιο φωνητικό της εύρος τεσσάρων οκτάβων και την τεχνική belting.",
            "Το 2002 επαναπροσδιόρισε την εικόνα της με το άλμπουμ 'Stripped' και την περσόνα 'Xtina'."
        ],
        "source": "https://en.wikipedia.org/wiki/Christina_Aguilera",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "90s"]
    },
    {
        "id": "pop_culture_med_209",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου anime και manga όπου έφηβοι μάχονται εναντίον γιγάντιων ανθρωποφάγων όντων μέσα από τρία πελώρια κυκλικά τείχη;",
        "answers": ["Death Note", "Tokyo Ghoul", "Attack on Titan", "Fullmetal Alchemist"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Attack on Titan' (Shingeki no Kyojin) του Χατζίμε Ισαγιάμα ξεκίνησε το 2009 και έγινε μία από τις πιο αναγνωρισμένες σειρές anime παγκοσμίως.",
        "funFacts": [
            "Τα τρία ομόκεντρα τείχη που προστατεύουν την ανθρωπότητα ονομάζονται Wall Maria, Wall Rose και Wall Sheena.",
            "Ο ειδικός εξοπλισμός των στρατιωτών για να μάχονται στον αέρα ονομάζεται 'Omni-Directional Mobility Gear' (ODM Gear)."
        ],
        "source": "https://en.wikipedia.org/wiki/Attack_on_Titan",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "anime", "attack_on_titan"]
    },
    {
        "id": "pop_culture_med_210",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος διάσημος ηθοποιός ενσάρκωσε τον ρόλο του μαφιόζου Tony Soprano στην πρωτοποριακή δραματική σειρά 'The Sopranos' του HBO;",
        "answers": ["Τζο Πέσι", "Αλ Πατσίνο", "Ρόμπερτ Ντε Νίρο", "Τζέιμς Γκαντολφίνι"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Τζέιμς Γκαντολφίνι (James Gandolfini) κέρδισε τρία βραβεία Emmy και μία Χρυσή Σφαίρα για την ανεπανάληπτη ερμηνεία του ως ο αρχηγός της μαφίας του Νιου Τζέρσεϊ που επισκέπτεται ψυχίατρο.",
        "funFacts": [
            "Το 'The Sopranos' (1999-2007) θεωρείται από πολλούς κριτικούς ως η σειρά που εγκαινίασε τη 'Χρυσή Εποχή της Τηλεόρασης'.",
            "Το αινιγματικό φινάλε της σειράς, με το απότομο κόψιμο στο μαύρο υπό τους ήχους του τραγουδιού 'Don't Stop Believin'' των Journey, προκάλεσε έντονες συζητήσεις που συνεχίζονται μέχρι σήμερα."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Sopranos",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "sopranos", "hbo"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(QUESTIONS)} questions for pop_culture_medium.")
    validate_and_append("pop_culture", "medium", 3, QUESTIONS)

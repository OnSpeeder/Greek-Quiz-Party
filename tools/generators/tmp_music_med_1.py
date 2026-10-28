import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
    {
        "id": "music_med_011",
        "text": "Ποιο από τα παρακάτω ξύλινα πνευστά μουσικά όργανα της συμφωνικής ορχήστρας χρησιμοποιεί διπλή γλωττίδα (καλάμι) για την παραγωγή του ήχου του;",
        "answers": [
            "Όμποε",
            "Κλαρινέτο",
            "Σαξόφωνο",
            "Πλάγιο φλάουτο"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το όμποε και το φαγκότο ανήκουν στα όργανα με διπλή γλωττίδα, σε αντίθεση με το κλαρινέτο και το σαξόφωνο που διαθέτουν μονή γλωττίδα.",
        "funFacts": [
            "Οι δύο λεπτές λωρίδες καλαμιού της διπλής γλωττίδας δονούνται η μία πάνω στην άλλη όταν ο μουσικός φυσά ανάμεσά τους.",
            "Λόγω της μεγάλης αντίστασης του αέρα στη διπλή γλωττίδα, το παίξιμο του όμποε απαιτεί ιδιαίτερο έλεγχο της αναπνοής και των μυών του προσώπου."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%8C%CE%BC%CF%80%CE%BF%CE%B5",
        "locale": "el-GR",
        "tags": ["oboe", "instruments", "woodwinds", "orchestra"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_012",
        "text": "Ποιο υπήρξε το τελευταίο άλμπουμ που ηχογράφησαν μαζί στο στούντιο οι The Beatles το 1969, με το διάσημο εξώφυλλο στη διάβαση πεζών;",
        "answers": [
            "Let It Be",
            "Abbey Road",
            "White Album",
            "Revolver"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Αν και το 'Let It Be' κυκλοφόρησε τελευταίο το 1970, το 'Abbey Road' (1969) ήταν το τελευταίο άλμπουμ που ηχογράφησαν από κοινού τα τέσσερα μέλη των Beatles.",
        "funFacts": [
            "Η διάβαση πεζών έξω από τα Abbey Road Studios στο Λονδίνο έχει κηρυχθεί διατηρητέο μνημείο εθνικής πολιτιστικής κληρονομιάς.",
            "Η δεύτερη πλευρά του δίσκου περιλαμβάνει ένα μνημειώδες ποτ-πουρί 16 λεπτών από μικρότερα ημιτελή τραγούδια ενωμένα σε ενιαία σουίτα."
        ],
        "source": "https://el.wikipedia.org/wiki/Abbey_Road_(%CE%AC%CE%BB%CE%BC%CF%80%CE%BF%CF%85%CE%BC)",
        "locale": "el-GR",
        "tags": ["beatles", "abbey-road", "rock", "albums"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_013",
        "text": "Ποιος κορυφαίος Έλληνας ποιητής και στιχουργός, συγγραφέας της «Αμοργού», συνεργάστηκε στενά με τον Μάνο Χατζιδάκι γράφοντας στίχους για τραγούδια όπως ο «Κεμάλ» και το «Χάρτινο το φεγγαράκι»;",
        "answers": [
            "Οδυσσέας Ελύτης",
            "Γιάννης Ρίτσος",
            "Νίκος Γκάτσος",
            "Μανόλης Αναγνωστάκης"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Νίκος Γκάτσος συνέδεσε την υψηλή υπερρεαλιστική ποίηση με το ελληνικό τραγούδι, αποτελώντας τον βασικό στιχουργικό συνοδοιπόρο του Μάνου Χατζιδάκι.",
        "funFacts": [
            "Η μοναδική ποιητική συλλογή που εξέδωσε ήταν η 'Αμοργός' το 1943, η οποία θεωρείται ορόσημο του ελληνικού υπερρεαλισμού.",
            "Έγραψε επίσης τους στίχους για το θρυλικό soundtrack του Σταύρου Ξαρχάκου στην ταινία 'Ρεμπέτικο' (1983)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%93%CE%BA%CE%AC%CF%84%CF%83%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["gatsos", "poetry", "chatzidakis", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_014",
        "text": "Σε ποια πόλη της πολιτείας της Νέας Υόρκης πραγματοποιήθηκε τελικά το ιστορικό φεστιβάλ του Woodstock τον Αύγουστο του 1969, στη φάρμα του Max Yasgur;",
        "answers": [
            "Γούντστοκ",
            "Όλμπανι",
            "Ιθάκη",
            "Μπέθελ"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Παρότι το φεστιβάλ πήρε το όνομά του από την πόλη του Γούντστοκ, οι τοπικές αντιδράσεις ανάγκασαν τους διοργανωτές να το μεταφέρουν στη γαλακτοκομική φάρμα στο Μπέθελ.",
        "funFacts": [
            "Υπολογίζεται ότι περισσότεροι από 400.000 νέοι κατέκλυσαν τον χώρο, δημιουργώντας μία από τις μεγαλύτερες ειρηνικές συγκεντρώσεις στην ιστορία.",
            "Η εμφάνιση του Jimi Hendrix το πρωί της τελευταίας ημέρας με την παραμορφωμένη εκτέλεση του αμερικανικού εθνικού ύμνου στην ηλεκτρική κιθάρα έμεινε στην ιστορία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B5%CF%83%CF%84%CE%B9%CE%B2%CE%AC%CE%BB_%CF%84%CE%BF%CF%85_%CE%93%CE%BF%CF%8D%CE%BD%CF%84%CF%83%CF%84%CE%BF%CE%BA",
        "locale": "el-GR",
        "tags": ["woodstock", "festivals", "rock", "counterculture"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_015",
        "text": "Ποιο ιστορικό στούντιο ηχογραφήσεων στο Μέμφις του Τενεσί ίδρυσε ο Sam Phillips το 1950, ανακαλύπτοντας θρύλους όπως ο Elvis Presley, ο Johnny Cash και ο Jerry Lee Lewis;",
        "answers": [
            "Sun Studio",
            "Stax Records",
            "Motown Records",
            "Chess Records"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το Sun Studio θεωρείται το λίκνο του ροκ εν ρολ, όπου ηχογραφήθηκε το 'Rocket 88' (1951) και οι πρώτες ιστορικές επιτυχίες του Elvis.",
        "funFacts": [
            "Στις 4 Δεκεμβρίου 1956, μια αυθόρμητη συνάντηση και κοινή τζαμ ηχογράφηση των Presley, Cash, Perkins και Lewis έμεινε στην ιστορία ως το 'Million Dollar Quartet'.",
            "Το στούντιο λειτουργεί σήμερα ως ιστορικό μουσείο και τουριστικό αξιοθέατο, παραμένοντας παράλληλα ενεργό στούντιο ηχογράφησης το βράδυ."
        ],
        "source": "https://el.wikipedia.org/wiki/Sun_Records",
        "locale": "el-GR",
        "tags": ["sun-studio", "rock-and-roll", "elvis", "memphis"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_016",
        "text": "Σε ποια ιαπωνική πόλη διαδραματίζεται η υπόθεση της διάσημης τραγικής όπερας «Μαντάμα Μπατερφλάι» (1904) του Giacomo Puccini;",
        "answers": [
            "Τόκιο",
            "Ναγκασάκι",
            "Κιότο",
            "Οσάκα"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η όπερα αφηγείται την τραγική ιστορία της νεαρής γκέισας Τσο-Τσο-Σαν στο λιμάνι του Ναγκασάκι γύρω στα 1900.",
        "funFacts": [
            "Στην πρεμιέρα της στη Σκάλα του Μιλάνου το 1904 η όπερα αποδοκιμάστηκε άγρια από το κοινό, αναγκάζοντας τον Puccini να την αποσύρει και να την αναθεωρήσει ριζικά.",
            "Η υπόθεση της όπερας αποτέλεσε τη βασική πηγή έμπνευσης για το παγκοσμίως επιτυχημένο σύγχρονο μιούζικαλ 'Miss Saigon'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%84%CE%AC%CE%BC%CE%B1_%CE%9C%CF%80%CE%B1%CF%84%CE%B5%CF%81%CF%86%CE%BB%CE%AC%CE%B9",
        "locale": "el-GR",
        "tags": ["puccini", "opera", "japan", "classical"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_017",
        "text": "Ποιο μνημειώδες άλμπουμ των Led Zeppelin του 1971 περιλαμβάνει το «Stairway to Heaven» και κυκλοφόρησε χωρίς κανένα όνομα συγκροτήματος στο εξώφυλλο, παρά μόνο με τέσσερα σύμβολα;",
        "answers": [
            "Led Zeppelin II",
            "Physical Graffiti",
            "Led Zeppelin IV",
            "Houses of the Holy"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το άτιτλο τέταρτο άλμπουμ (ευρέως γνωστό ως 'Led Zeppelin IV' ή 'Four Symbols') έχει πουλήσει πάνω από 37 εκατομμύρια αντίτυπα παγκοσμίως.",
        "funFacts": [
            "Κάθε ένα από τα τέσσερα μέλη του συγκροτήματος επέλεξε ένα μυστικιστικό σύμβολο για να τον αντιπροσωπεύει, με πιο διάσημο το σύμβολο 'Zoso' του Jimmy Page.",
            "Ο κιθαρίστας Jimmy Page ηχογράφησε το περίφημο σόλο του 'Stairway to Heaven' χρησιμοποιώντας μια κιθάρα Fender Telecaster που του είχε χαρίσει ο Jeff Beck."
        ],
        "source": "https://el.wikipedia.org/wiki/Led_Zeppelin_IV",
        "locale": "el-GR",
        "tags": ["led-zeppelin", "hard-rock", "70s", "albums"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_018",
        "text": "Ποιος πρωτοποριακός Έλληνας συνθέτης και αρχιτέκτονας εισήγαγε τη στοχαστική μουσική και μαθηματικά μοντέλα στη σύνθεση, σχεδιάζοντας παράλληλα το περίπτερο Philips στην Expo '58 με τον Le Corbusier;",
        "answers": [
            "Μίκης Θεοδωράκης",
            "Νίκος Σκαλκώτας",
            "Δημήτρης Μητρόπουλος",
            "Ιάννης Ξενάκης"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Ιάννης Ξενάκης υπήρξε ηγετική μορφή της παγκόσμιας μεταπολεμικής μουσικής πρωτοπορίας, συνδέοντας τη θεωρία πιθανοτήτων και την αρχιτεκτονική με τον ήχο.",
        "funFacts": [
            "Τραυματίστηκε σοβαρά στο πρόσωπο κατά τα Δεκεμβριανά στην Αθήνα το 1944 από όλμο, χάνοντας το αριστερό του μάτι.",
            "Ανέπτυξε το σύστημα UPIC, ένα πρωτοποριακό υπολογιστικό εργαλείο που επέτρεπε τη σύνθεση μουσικής μέσω γραφικού σχεδιασμού καμπυλών σε ειδικό πίνακα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%99%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%9E%CE%B5%CE%BD%CE%AC%CE%BA%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["xenakis", "avant-garde", "architecture", "modern-classical"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_019",
        "text": "Σε ποια αμερικανική πόλη ιδρύθηκε το 1959 από τον Berry Gordy Jr. η θρυλική δισκογραφική εταιρεία Motown Records («Hitsville U.S.A.»);",
        "answers": [
            "Ντιτρόιτ",
            "Σικάγο",
            "Νέα Υόρκη",
            "Φιλαδέλφεια"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η Motown πήρε το όνομά της από το προσωνύμιο του Ντιτρόιτ ('Motor Town') και καθιέρωσε ένα μοναδικό ποπ-σόουλ ήχο που έσπασε τα φυλετικά σύνορα.",
        "funFacts": [
            "Το αρχηγείο της εταιρείας σε ένα διώροφο σπίτι στη λεωφόρο West Grand Blvd στο Ντιτρόιτ είχε μια φωτεινή επιγραφή που έγραφε 'Hitsville U.S.A.'.",
            "Από τη Motown ξεκίνησαν τεράστια ονόματα όπως οι The Jackson 5, ο Stevie Wonder, η Diana Ross & The Supremes και ο Marvin Gaye."
        ],
        "source": "https://el.wikipedia.org/wiki/Motown",
        "locale": "el-GR",
        "tags": ["motown", "detroit", "soul", "music-history"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_020",
        "text": "Ποιος Γάλλος συνθέτης υπήρξε ο κορυφαίος εκπρόσωπος του μουσικού ιμπρεσιονισμού, γράφοντας αριστουργήματα όπως το «Φως του Φεγγαριού» (Clair de Lune) και «Η Θάλασσα» (La Mer);",
        "answers": [
            "Μορίς Ραβέλ",
            "Κλοντ Ντεμπυσί",
            "Ερίκ Σατί",
            "Γκαμπριέλ Φορέ"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Claude Debussy ανανέωσε ριζικά την αρμονία και τα ηχοχρώματα, απομακρυνόμενος από τους παραδοσιακούς τονικούς κανόνες του γερμανικού ρομαντισμού.",
        "funFacts": [
            "Παρότι οι κριτικοί τον κατέταξαν ως τον θεμελιωτή του 'ιμπρεσιονισμού' στη μουσική, ο ίδιος αντιπαθούσε έντονα αυτόν τον όρο για το έργο του.",
            "Το 'Πρελούδιο στο απομεσήμερο ενός φαύνου' (1894) θεωρείται από πολλούς μουσικολόγους ως η αφετηρία της σύγχρονης μοντέρνας μουσικής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%BF%CE%BD%CF%84_%CE%9D%CF%84%CE%B5%CE%BC%CF%80%CF%85%CF%83%CE%AF",
        "locale": "el-GR",
        "tags": ["debussy", "impressionism", "classical", "france"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_021",
        "text": "Ποιο συμφωνικό μουσικό σύνολο ίδρυσε ο Μάνος Χατζιδάκις στην Αθήνα το 1989 με σκοπό την παρουσίαση πρωτότυπων έργων μακριά από τη συμβατική ορχηστρική ρουτίνα;",
        "answers": [
            "Καμεράτα",
            "Κρατική Ορχήστρα Αθηνών",
            "Ορχήστρα των Χρωμάτων",
            "Εθνική Συμφωνική Ορχήστρα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η Ορχήστρα των Χρωμάτων παρουσίασε υπό τη διεύθυνση του Χατζιδάκι απαιτητικά προγράμματα κλασικής, σύγχρονης και ελληνικής μουσικής υψηλής αισθητικής.",
        "funFacts": [
            "Ο Χατζιδάκις χρηματοδότησε προσωπικά τη δημιουργία της ορχήστρας στα πρώτα της βήματα, επιλέγοντας ο ίδιος τους μουσικούς μετά από αυστηρές ακροάσεις.",
            "Η πρώτη συναυλία της δόθηκε στο θέατρο Παλλάς τον Νοέμβριο του 1989 με έργα Ελλήνων και ξένων δημιουργών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9F%CF%81%CF%87%CE%AE%CF%83%CF%84%CF%81%CE%B1_%CF%84%CF%89%CE%BD_%CE%A7%CF%81%CF%89%CE%BC%CE%AC%CF%84%CF%89%CE%BD",
        "locale": "el-GR",
        "tags": ["chatzidakis", "orchestra", "classical", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_022",
        "text": "Ποια διάσημη ροκ όπερα κυκλοφόρησε το βρετανικό συγκρότημα The Who το 1969, αφηγούμενη την ιστορία ενός κωφάλαλου και τυφλού αγοριού που γίνεται πρωταθλητής στο φλίπερ;",
        "answers": [
            "Quadrophenia",
            "The Wall",
            "Ziggy Stardust",
            "Tommy"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Tommy' συντέθηκε κυρίως από τον Pete Townshend και υπήρξε η πρώτη ολοκληρωμένη ροκ δουλειά που χαρακτηρίστηκε επισήμως ως 'ροκ όπερα'.",
        "funFacts": [
            "Το τραγούδι 'Pinball Wizard' από το άλμπουμ έγινε τεράστια επιτυχία και ερμηνεύτηκε αργότερα από τον Elton John στην κινηματογραφική μεταφορά του 1975.",
            "Το άλμπουμ εντάχθηκε στο Grammy Hall of Fame για την ιστορική και καλλιτεχνική του αξία."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Who",
        "locale": "el-GR",
        "tags": ["the-who", "rock-opera", "tommy", "60s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_023",
        "text": "Σε ποιο ιστορικό αμερικανικό φεστιβάλ του 1967 ο αριστερόχειρας κιθαρίστας Jimi Hendrix έβαλε φωτιά στην κιθάρα του στο τέλος του τραγουδιού «Wild Thing»;",
        "answers": [
            "Monterey Pop Festival",
            "Woodstock",
            "Isle of Wight Festival",
            "Altamont Speedway"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το Monterey International Pop Festival τον Ιούνιο του 1967 στην Καλιφόρνια αποτέλεσε την εκρηκτική εμφάνιση που καθιέρωσε τον Hendrix στις ΗΠΑ.",
        "funFacts": [
            "Μετά το άναμμα της φωτιάς με υγρό αναπτήρα, έσπασε την κιθάρα του Fender Stratocaster στη σκηνή και πέταξε τα κομμάτια στο έκπληκτο κοινό.",
            "Έπαιζε ανάποδα μια κανονική δεξιόχειρη Stratocaster αλλάζοντας απλώς τη σειρά των χορδών, γεγονός που του έδινε μοναδικό ηχόχρωμα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AF%CE%BC%CE%B9_%CE%A7%CE%AD%CE%BD%CF%84%CF%81%CE%B9%CE%BE",
        "locale": "el-GR",
        "tags": ["jimi-hendrix", "guitar", "monterey", "rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_024",
        "text": "Ποιο μνημειώδες λαϊκό ορατόριο συνέθεσε ο Μίκης Θεοδωράκης το 1964, βασισμένο στο ομώνυμο ποιητικό έργο του βραβευμένου με Νόμπελ Οδυσσέα Ελύτη;",
        "answers": [
            "Επιτάφιος",
            "Το Άξιον Εστί",
            "Πνευματικό Εμβατήριο",
            "Ρωμιοσύνη"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Άξιον Εστί' συνδύασε τη βυζαντινή εκκλησιαστική υμνολογία, τη συμφωνική ορχήστρα και το λαϊκό τραγούδι με σολίστα τον Γρηγόρη Μπιθικώτση.",
        "funFacts": [
            "Χωρίζεται σε τρία μέρη: 'Η Γένεσις', 'Τα Πάθη' και 'Το Δοξαστικόν', περιλαμβάνοντας ύμνους όπως 'Της δικαιοσύνης ήλιε νοητέ' και 'Ένα το χελιδόνι'.",
            "Στην πρώτη ηχογράφηση τον ρόλο του ψάλτη ερμήνευσε ο βαρύτονος Θεόδωρος Δημήτριεφ και του αναγνώστη ο ηθοποιός Μάνος Κατράκης."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%86%CE%BE%CE%B9%CE%BF%CE%BD_%CE%95%CF%83%CF%84%CE%AF_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "locale": "el-GR",
        "tags": ["theodorakis", "elytis", "axion-esti", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_025",
        "text": "Ποιο πρωτοποριακό ηλεκτρονικό μουσικό όργανο, που εφευρέθηκε το 1920, παίζεται χωρίς καμία απολύτως φυσική επαφή, ελέγχοντας τον ήχο με την κίνηση των χεριών κοντά σε δύο κεραίες;",
        "answers": [
            "Συνθεσάιζερ",
            "Οντ Μαρτενό",
            "Θέρεμιν",
            "Μελλοτρόν"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το θέρεμιν (theremin) εφευρέθηκε από τον Ρώσο φυσικό Léon Theremin και ελέγχει τη συχνότητα και την ένταση του ήχου μέσω ηλεκτρομαγνητικών πεδίων.",
        "funFacts": [
            "Χρησιμοποιήθηκε εκτενώς σε κλασικές ταινίες επιστημονικής φαντασίας και θρίλερ του Χόλιγουντ της δεκαετίας του 1950 για να δημιουργήσει ανατριχιαστικούς απόκοσμους ήχους.",
            "Ο Brian Wilson των Beach Boys χρησιμοποίησε μια παραλλαγή του οργάνου (electro-theremin) στο περίφημο κομμάτι 'Good Vibrations' (1966)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%98%CE%AD%CF%81%CE%B5%CE%BC%CE%B9%CE%BD",
        "locale": "el-GR",
        "tags": ["theremin", "electronic-instruments", "music-tech", "sci-fi"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_026",
        "text": "Ποια ιστορική διπλή φιλανθρωπική συναυλία διοργάνωσαν οι Bob Geldof και Midge Ure τον Ιούλιο του 1985 ταυτόχρονα στο Λονδίνο και τη Φιλαδέλφεια για την καταπολέμηση του λιμού στην Αιθιοπία;",
        "answers": [
            "Farm Aid",
            "Concert for Bangladesh",
            "Woodstock '94",
            "Live Aid"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το Live Aid παρακολούθησαν ζωντανά μέσω τηλεόρασης περίπου 1,9 δισεκατομμύρια άνθρωποι σε 150 χώρες, αποτελώντας τη μεγαλύτερη δορυφορική μετάδοση της εποχής.",
        "funFacts": [
            "Η 20λεπτη εμφάνιση των Queen στο στάδιο Wembley ψηφίστηκε από κριτικούς και κοινό ως η κορυφαία ζωντανή ροκ συναυλία όλων των εποχών.",
            "Ο Phil Collins έπαιξε στο Wembley, πήρε αμέσως το υπερηχητικό αεροσκάφος Concorde για τις ΗΠΑ και έπαιξε την ίδια ημέρα και στο στάδιο JFK της Φιλαδέλφειας."
        ],
        "source": "https://el.wikipedia.org/wiki/Live_Aid",
        "locale": "el-GR",
        "tags": ["live-aid", "charity", "queen", "rock-history"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_027",
        "text": "Πώς ονομάζονται οι παραδοσιακές λαϊκές τροπικές κλίμακες (όπως Ραστ, Χιτζάζ, Ουσάκ και Νιαβέντ) που αποτελούν τη μελωδική βάση του ρεμπέτικου και του ελληνικού λαϊκού τραγουδιού;",
        "answers": [
            "Δρόμοι",
            "Μακάμια",
            "Ηχογραφήσεις",
            "Συγκερασμοί"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Οι λαϊκοί «δρόμοι» αποτελούν προσαρμογή των ανατολικών μακάμ στο δυτικό συγκερασμένο σύστημα του μπουζουκιού και της κιθάρας.",
        "funFacts": [
            "Κάθε δρόμος έχει συγκεκριμένες έλξεις, κύριες δεσπόζουσες νότες και χαρακτηριστικά ακούσματα που εκφράζουν διαφορετικά συναισθήματα (πένθος, χαρά, νοσταλγία).",
            "Ο δρόμος Χιτζάζ είναι από τους πιο διαδεδομένους στο ρεμπέτικο, με χαρακτηριστικό διάστημα τριημιτονίου ανάμεσα στη δεύτερη και την τρίτη βαθμίδα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B1%CF%8A%CE%BA%CE%BF%CE%AF_%CE%B4%CF%81%CF%8C%CE%BC%CE%BF%CE%B9",
        "locale": "el-GR",
        "tags": ["dromoi", "rebetiko", "music-theory", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_028",
        "text": "Σε ποιο ιστορικό μουσικό φεστιβάλ το 1965 ο Bob Dylan προκάλεσε την οργή των φολκ πουριτανών παίζοντας για πρώτη φορά με ηλεκτρική κιθάρα και ροκ μπάντα;",
        "answers": [
            "Woodstock",
            "Newport Folk Festival",
            "Monterey Pop Festival",
            "Isle of Wight"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η 'ηλεκτρική στροφή' του Dylan στο Newport Folk Festival δίχασε βαθιά το κοινό της φολκ αλλά άνοιξε τον δρόμο για τη γέννηση του folk-rock.",
        "funFacts": [
            "Κάποιοι θεατές τον γιούχαραν τόσο έντονα που ο θρυλικός τραγουδιστής της φολκ Pete Seeger φέρεται να απείλησε να κόψει τα καλώδια του ήχου με τσεκούρι.",
            "Η ηλεκτρική κιθάρα Fender Stratocaster Sunburst που έπαιξε ο Dylan σε εκείνη τη συναυλία πουλήθηκε σε δημοπρασία το 2013 για σχεδόν 1 εκατομμύριο δολάρια."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CE%BC%CF%80_%CE%9D%CF%84%CE%AF%CE%BB%CE%B1%CE%BD",
        "locale": "el-GR",
        "tags": ["bob-dylan", "newport", "folk-rock", "electric"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_029",
        "text": "Ποιος μεγάλος Ιταλός συνθέτης της όπερας συνδέθηκε άρρηκτα με το κίνημα της ιταλικής ενοποίησης (Risorgimento) με έργα όπως «Ναμπούκο», «Ριγκολέτο» και «Τραβιάτα»;",
        "answers": [
            "Τζοακίνο Ροσσίνι",
            "Τζάκομο Πουτσίνι",
            "Τζουζέπε Βέρντι",
            "Βιντσέντζο Μπελίνι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το όνομα του Giuseppe Verdi χρησιμοποιούνταν ως πατριωτικό σύνθημα ('Viva V.E.R.D.I.' = Vittorio Emanuele Re D'Italia) για την ανεξαρτησία της Ιταλίας.",
        "funFacts": [
            "Το χορωδιακό 'Va, pensiero' (Το τραγούδι των Εβραίων σκλάβων) από τον 'Ναμπούκο' έγινε ο ανεπίσημος εθνικός ύμνος των Ιταλών πατριωτών.",
            "Στην κηδεία του στο Μιλάνο το 1901 συγκεντρώθηκαν πάνω από 300.000 άνθρωποι, στη μεγαλύτερη δημόσια συγκέντρωση που είχε δει ποτέ η πόλη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%85%CE%B6%CE%AD%CF%80%CE%B5_%CE%92%CE%AD%CF%81%CE%BD%CF%84%CE%B9",
        "locale": "el-GR",
        "tags": ["verdi", "opera", "italy", "classical"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_030",
        "text": "Ποιο βρετανικό post-punk συγκρότημα από το Μάντσεστερ, με τραγουδιστή τον Ian Curtis, κυκλοφόρησε τον θρυλικό ύμνο «Love Will Tear Us Apart» πριν μετονομαστεί σε New Order;",
        "answers": [
            "The Cure",
            "The Smiths",
            "Echo & the Bunnymen",
            "Joy Division"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Οι Joy Division καθόρισαν τον σκοτεινό post-punk ήχο με τα άλμπουμ 'Unknown Pleasures' (1979) και 'Closer' (1980), πριν την τραγική αυτοκτονία του Curtis.",
        "funFacts": [
            "Το εμβληματικό εξώφυλλο του 'Unknown Pleasures' απεικονίζει τα ραδιοκύματα από το πρώτο πάλσαρ που ανακαλύφθηκε ποτέ (CP 1919).",
            "Μετά τον θάνατο του Curtis, τα εναπομείναντα μέλη σχημάτισαν τους New Order, πρωτοπορώντας στη synth-pop με το 'Blue Monday'."
        ],
        "source": "https://el.wikipedia.org/wiki/Joy_Division",
        "locale": "el-GR",
        "tags": ["joy-division", "post-punk", "manchester", "new-order"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_031",
        "text": "Ποιος σπουδαίος Έλληνας συνθέτης υπέγραψε τη μουσική για τον εμβληματικό δίσκο «Οδός Αριστοτέλους» (1974) σε στίχους Λευτέρη Παπαδόπουλου, με τη φωνή της Χάρις Αλεξίου και του Γιάννη Πάριου;",
        "answers": [
            "Γιάννης Σπανός",
            "Μίμης Πλέσσας",
            "Γιώργος Χατζηνάσιος",
            "Απόστολος Καλδάρας"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Γιάννης Σπανός δημιούργησε με την 'Οδό Αριστοτέλους' έναν από τους πιο κλασικούς δίσκους της ελληνικής μουσικής, καθιερώνοντας οριστικά τη Χάρις Αλεξίου.",
        "funFacts": [
            "Ο τίτλος του δίσκου και του ομώνυμου τραγουδιού είναι εμπνευσμένος από τον δρόμο στην πλατεία Βικτωρίας όπου μεγάλωσε ο στιχουργός Λευτέρης Παπαδόπουλος.",
            "Ο Γιάννης Σπανός είχε διαγράψει σπουδαία καριέρα στο Παρίσι παίζοντας πιάνο στις μπουάτ δίπλα σε αστέρες όπως η Brigitte Bardot και η Juliette Gréco."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%A3%CF%80%CE%B1%CE%BD%CF%8C%CF%82",
        "locale": "el-GR",
        "tags": ["spanos", "alexiou", "papadopoulos", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_032",
        "text": "Ποιος ιδιοφυής Βρετανός κιθαρίστας των μπλουζ ίδρυσε τους Fleetwood Mac το 1967, πριν αποχωρήσει λόγω σοβαρών προβλημάτων ψυχικής υγείας;",
        "answers": [
            "Eric Clapton",
            "Peter Green",
            "Mick Taylor",
            "Jeff Beck"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Peter Green υπήρξε ένας από τους σπουδαιότερους κιθαρίστες του βρετανικού blues boom, συνθέτοντας κλασικά κομμάτια όπως το 'Black Magic Woman' και το 'Albatross'.",
        "funFacts": [
            "Ο θρυλικός B.B. King είχε δηλώσει για τον Peter Green ότι ήταν ο μόνος κιθαρίστας που τον έκανε να ιδρώνει όταν τον άκουγε να παίζει.",
            "Το instrumental κομμάτι του 'Albatross' (1968) αποτέλεσε τη βασική έμπνευση των Beatles για το τραγούδι 'Sun King' στο άλμπουμ Abbey Road."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AF%CF%84%CE%B5%CF%81_%CE%93%CE%BA%CF%81%CE%B9%CE%BD",
        "locale": "el-GR",
        "tags": ["peter-green", "fleetwood-mac", "blues", "guitar"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_033",
        "text": "Ποιο πληκτροφόρο μουσικό όργανο, πρόδρομος του πιάνου, κυριάρχησε στην Αναγέννηση και το Μπαρόκ, παράγοντας ήχο με νύξιμο (τσίμπημα) των χορδών από πτερύγια αντί για κρούση με σφυράκια;",
        "answers": [
            "Κλαβίχορδο",
            "Εκκλησιαστικό όργανο",
            "Τσέμπαλο",
            "Σπινέτο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το τσέμπαλο (harpsichord) δεν έχει τη δυνατότητα δυναμικής διαβάθμισης (πιάνο/φόρτε) ανάλογα με την πίεση των δακτύλων, γι' αυτό αντικαταστάθηκε σταδιακά από το πιάνο.",
        "funFacts": [
            "Συχνά διέθετε δύο σειρές πληκτρολογίων (manuals) για να επιτρέπει την εναλλαγή διαφορετικών ηχοχρωμάτων και εντάσεων.",
            "Ο Johann Sebastian Bach έγραψε το μνημειώδες έργο 'Το Καλοσυγκερασμένο Κλειδοκύμβαλο' για να αναδείξει τις δυνατότητες κουρδίσματος στα πληκτροφόρα της εποχής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%83%CE%AD%CE%BC%CF%80%CE%B1%CE%BB%CE%BF",
        "locale": "el-GR",
        "tags": ["harpsichord", "instruments", "baroque", "keyboard"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_034",
        "text": "Ποια διάσημη σειρά τριών άλμπουμ ηχογράφησε ο David Bowie στα τέλη της δεκαετίας του 1970 σε συνεργασία με τον Brian Eno στη γερμανική πρωτεύουσα («Berlin Trilogy»);",
        "answers": [
            "Station to Station, Heroes, Scary Monsters",
            "Ziggy Stardust, Aladdin Sane, Diamond Dogs",
            "Young Americans, Low, Lodger",
            "Low, Heroes, Lodger"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η 'Τριλογία του Βερολίνου' περιλαμβάνει τα άλμπουμ 'Low' (1977), 'Heroes' (1977) και 'Lodger' (1979), σηματοδοτώντας μια ριζοσπαστική στροφή στον ηλεκτρονικό ambient ήχο.",
        "funFacts": [
            "Τα Hansa Studios όπου ηχογραφήθηκε το 'Heroes' βρίσκονταν σε απόσταση μόλις 500 μέτρων από το Τείχος του Βερολίνου.",
            "Στο τραγούδι 'Heroes', ο κιθαρίστας Robert Fripp των King Crimson πέταξε από τη Νέα Υόρκη στο Βερολίνο και ηχογράφησε τα εκπληκτικά κιθαριστικά του μέρη μέσα σε μία μόνο μέρα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%AD%CE%B9%CE%B2%CE%B9%CE%BD%CF%84_%CE%9C%CF%80%CF%8C%CE%BF%CF%85%CE%B9",
        "locale": "el-GR",
        "tags": ["bowie", "berlin-trilogy", "brian-eno", "electronic-rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_035",
        "text": "Ποια κορυφαία Ελληνίδα στιχουργός υπέγραψε τους ανατρεπτικούς στίχους σε ιστορικούς δίσκους του Σταμάτη Κραουνάκη, όπως «Κυκλοφορώ κι οπλοφορώ» και «Μαμά γερνάω»;",
        "answers": [
            "Λίνα Νικολακοπούλου",
            "Ευτυχία Παπαγιαννοπούλου",
            "Μαριανίνα Κριεζή",
            "Αφροδίτη Μάνου"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η Λίνα Νικολακοπούλου ανανέωσε ριζικά τον ελληνικό ποιητικό στίχο από τη δεκαετία του 1980, εισάγοντας σύγχρονες αστικές εικόνες και τολμηρή γλώσσα.",
        "funFacts": [
            "Γνωρίστηκε με τον Σταμάτη Κραουνάκη στα φοιτητικά τους χρόνια στο Πάντειο Πανεπιστήμιο όπου σπούδαζαν πολιτικές επιστήμες.",
            "Έγραψε τους επίσημους στίχους για τα τραγούδια των τελετών έναρξης και λήξης των Ολυμπιακών Αγώνων της Αθήνας το 2004 σε μουσική Trevor Horn."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AF%CE%BD%CE%B1_%CE%9D%CE%B9%CE%BA%CE%BF%CE%BB%CE%B1%CE%BA%CE%BF%CF%80%CE%BF%CF%8D%CE%BB%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["nikolakopoulou", "kraounakis", "lyrics", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_036",
        "text": "Ποιο αριστουργηματικό άλμπουμ των Beach Boys του 1966, σε παραγωγή και σύνθεση του Brian Wilson, αποτέλεσε την κύρια πηγή έμπνευσης των Beatles για το «Sgt. Pepper»;",
        "answers": [
            "Surfin' USA",
            "Pet Sounds",
            "Smile",
            "Wild Honey"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Pet Sounds' αναγνωρίζεται ως ένα από τα πιο επιδραστικά άλμπουμ στην ιστορία της ποπ, με πρωτοποριακή χρήση ορχηστρικών οργάνων και περίπλοκων φωνητικών αρμονιών.",
        "funFacts": [
            "Ο Paul McCartney έχει δηλώσει επανειλημμένα ότι το 'God Only Knows' από αυτό το άλμπουμ είναι το αγαπημένο του τραγούδι όλων των εποχών.",
            "Για τις ανάγκες των ηχογραφήσεων ο Brian Wilson χρησιμοποίησε ασυνήθιστα όργανα και ήχους, όπως κουδούνια ποδηλάτου, σφυρίχτρες σκύλων και άδεια δοχεία νερού."
        ],
        "source": "https://el.wikipedia.org/wiki/Pet_Sounds",
        "locale": "el-GR",
        "tags": ["beach-boys", "brian-wilson", "pet-sounds", "classics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_037",
        "text": "Ποιος θρυλικός Ιταλός κατασκευαστής εγχόρδων από την Κρεμόνα δημιούργησε στα τέλη του 17ου και αρχές του 18ου αιώνα τα διασημότερα και ακριβότερα βιολιά και τσέλα στην ιστορία;",
        "answers": [
            "Αντρέα Αμάτι",
            "Τζουζέπε Γκουαρνέρι",
            "Αντόνιο Στραντιβάρι",
            "Νικολό Παγκανίνι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Antonio Stradivari (Stradivarius) κατασκεύασε περίπου 1.100 όργανα, εκ των οποίων σώζονται περίπου 650, φημισμένα για την απαράμιλλη ακουστική τους διαύγεια.",
        "funFacts": [
            "Τα βιολιά της λεγόμενης 'Χρυσής Περιόδου' του (1700-1725) πωλούνται σήμερα σε διεθνείς δημοπρασίες για ποσά που ξεπερνούν τα 15 εκατομμύρια ευρώ.",
            "Παρά τις δεκαετίες επιστημονικών ερευνών με ακτίνες Χ και χημικές αναλύσεις, το ακριβές 'μυστικό' του βερνικιού και της επεξεργασίας του ξύλου παραμένει αντικείμενο συζήτησης."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%8C%CE%BD%CE%B9%CE%BF_%CE%A3%CF%84%CF%81%CE%B1%CE%BD%CF%84%CE%B9%CE%B2%CE%AC%CF%81%CE%B9",
        "locale": "el-GR",
        "tags": ["stradivarius", "violin", "cremona", "instruments"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_038",
        "text": "Ποιο ιστορικό τραγούδι συνεργασίας ηχογράφησαν από κοινού οι Queen και ο David Bowie το 1981 στο Μοντρέ της Ελβετίας, με μια από τις πιο γνωστές γραμμές μπάσου στη ροκ;",
        "answers": [
            "Radio Ga Ga",
            "Heroes",
            "Somebody to Love",
            "Under Pressure"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Under Pressure' γεννήθηκε από μια αυθόρμητη jam session στα Mountain Studios και κατέκτησε την κορυφή των βρετανικών charts.",
        "funFacts": [
            "Η διάσημη εισαγωγική γραμμή μπάσου του John Deacon χρησιμοποιήθηκε αργότερα ως sample από τον ράπερ Vanilla Ice στην τεράστια επιτυχία του 1990 'Ice Ice Baby'.",
            "Οι Queen και ο David Bowie δεν ερμήνευσαν ποτέ το τραγούδι μαζί ζωντανά επί σκηνής όσο ζούσε ο Freddie Mercury."
        ],
        "source": "https://el.wikipedia.org/wiki/Under_Pressure",
        "locale": "el-GR",
        "tags": ["queen", "david-bowie", "under-pressure", "collab"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_039",
        "text": "Ποιος μεγάλος συνθέτης και μπουζουξής του λαϊκού τραγουδιού αποκλήθηκε «ο δάσκαλος» και έγραψε ιστορικά τραγούδια όπως «Το δικό σου το μαράζι» και «Ο ναύτης»;",
        "answers": [
            "Γιώργος Μητσάκης",
            "Απόστολος Χατζηχρήστος",
            "Μπάμπης Μπακάλης",
            "Θεόδωρος Δερβενιώτης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Γιώργος Μητσάκης υπήρξε από τους σπουδαιότερους λαϊκούς δημιουργούς, γράφοντας τόσο τη μουσική όσο και τους στίχους σε εκατοντάδες κλασικά τραγούδια.",
        "funFacts": [
            "Γεννήθηκε στην Κωνσταντινούπολη το 1921 και εγκαταστάθηκε στην Ελλάδα μετά από περιπλανήσεις στην Καβάλα και τη Θεσσαλονίκη.",
            "Του αποδόθηκε το προσωνύμιο 'δάσκαλος' λόγω της βαθιάς του γνώσης στο μπουζούκι και του σεβασμού που ενέπνεε σε όλους τους νεότερους μουσικούς."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8E%CF%81%CE%B3%CE%BF%CF%82_%CE%9C%CE%B7%CF%84%CF%83%CE%AC%CE%BA%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["mitsakis", "rebetiko", "laiko", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_040",
        "text": "Ποιος διάσημος καλλιτέχνης της pop art σχεδίασε το εξώφυλλο με την κίτρινη μπανάνα-αυτοκόλλητο για το ιστορικό ντεμπούτο άλμπουμ των The Velvet Underground & Nico (1967);",
        "answers": [
            "Roy Lichtenstein",
            "Andy Warhol",
            "Keith Haring",
            "Jean-Michel Basquiat"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Andy Warhol υπήρξε ο μάνατζερ και παραγωγός του συγκροτήματος, εντάσσοντας τη Γερμανίδα τραγουδίστρια Nico στο πλευρό του Lou Reed.",
        "funFacts": [
            "Στην αρχική έκδοση του δίσκου, το αυτοκόλλητο της μπανάνας μπορούσε να ξεκολλήσει αποκαλύπτοντας από κάτω μια σάρκα σε χρώμα ροζ.",
            "Ο μουσικός Brian Eno είχε πει τη διάσημη φράση ότι το άλμπουμ πούλησε αρχικά μόνο 30.000 αντίτυπα, αλλά όποιος το αγόρασε έφτιαξε δικό του συγκρότημα."
        ],
        "source": "https://el.wikipedia.org/wiki/The_Velvet_Underground_%26_Nico",
        "locale": "el-GR",
        "tags": ["velvet-underground", "andy-warhol", "lou-reed", "art-rock"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_041",
        "text": "Ποιο είναι το χαρακτηριστικό μουσικό μέτρο (ρυθμική αγωγή) που καθορίζει τον παραδοσιακό ελληνικό αντικριστό χορό ζεϊμπέκικο;",
        "answers": [
            "7/8",
            "2/4",
            "9/8",
            "5/8"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το ζεϊμπέκικο βασίζεται σε εννιάσημο ρυθμό (9/8 ή 9/4), ο οποίος υποδιαιρείται εσωτερικά σε 2+2+2+3 ή 4+5 χρόνους.",
        "funFacts": [
            "Πήρε το όνομά του από τους Ζεϊμπέκηδες, ελληνόφωνους ή τουρκόφωνους αντάρτες και πολεμιστές της Μικράς Ασίας.",
            "Θεωρείται κατεξοχήν μοναχικός και εσωτερικός ανδρικός αυτοσχεδιαστικός χορός, που δεν επιδέχεται σταθερά προκαθορισμένα βήματα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B5%CF%8A%CE%BC%CF%80%CE%AD%CE%BA%CE%B9%CE%BA%CE%BF",
        "locale": "el-GR",
        "tags": ["zeibekiko", "time-signature", "rhythm", "folk-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_042",
        "text": "Ποιος κιθαρίστας των Beatles κυκλοφόρησε το 1970 το μνημειώδες τριπλό σόλο άλμπουμ «All Things Must Pass», που περιείχε την επιτυχία «My Sweet Lord»;",
        "answers": [
            "John Lennon",
            "Paul McCartney",
            "Ringo Starr",
            "George Harrison"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο George Harrison συγκέντρωσε στο 'All Things Must Pass' δεκάδες τραγούδια που είχε γράψει τα προηγούμενα χρόνια αλλά δεν χωρούσαν στα άλμπουμ των Beatles.",
        "funFacts": [
            "Ήταν το πρώτο τριπλό άλμπουμ στην ιστορία της ροκ μουσικής από έναν μόνο καλλιτέχνη και σημείωσε τεράστια εμπορική επιτυχία.",
            "Το 'My Sweet Lord' έγινε το πρώτο νούμερο ένα σόλο σινγκλ από πρώην μέλος των Beatles σε Βρετανία και Αμερική."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CF%81%CF%84%CE%B6_%CE%A7%CE%AC%CF%81%CE%B9%CF%83%CE%BF%CE%BD",
        "locale": "el-GR",
        "tags": ["harrison", "beatles", "solo", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_043",
        "text": "Ποια κορυφαία Ελληνίδα κοντράλτο ερμηνεύτρια χαρακτηρίστηκε διεθνώς ως η «ιέρεια» του Μίκη Θεοδωράκη, ερμηνεύοντας τα μεγαλύτερα πολιτικά και ποιητικά του έργα σε όλο τον κόσμο;",
        "answers": [
            "Μαρία Φαραντούρη",
            "Μαρίζα Κωχ",
            "Νένα Βενετσάνου",
            "Φλέρυ Νταντωνάκη"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η Μαρία Φαραντούρη διαθέτει μια επιβλητική βαθιά φωνή που συνδέθηκε άρρηκτα με τον αγώνα κατά της Δικτατορίας των Συνταγματαρχών.",
        "funFacts": [
            "Ο Μίκης Θεοδωράκης την άκουσε για πρώτη φορά σε ηλικία μόλις 16 ετών και της είπε ότι γεννήθηκε για να τραγουδάει τα έργα του.",
            "Ο διεθνής Τύπος και προσωπικότητες όπως ο François Mitterrand την είχαν αποκαλέσει 'τη φωνή της Ελλάδας'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AF%CE%B1_%CE%A6%CE%B1%CF%81%CE%B1%CE%BD%CF%84%CE%BF%CF%8D%CF%81%CE%B7",
        "locale": "el-GR",
        "tags": ["farantouri", "theodorakis", "greek-music", "contralto"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_044",
        "text": "Ποιο συγκρότημα εναλλακτικής ροκ από την Οξφόρδη κυκλοφόρησε το προφητικό άλμπουμ «OK Computer» το 1997, εξερευνώντας θέματα τεχνολογικής αποξένωσης και καπιταλισμού;",
        "answers": [
            "Oasis",
            "Radiohead",
            "Blur",
            "Muse"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Οι Radiohead με ηγέτη τον Thom Yorke δημιούργησαν ένα από τα πιο αναγνωρισμένα άλμπουμ της δεκαετίας του 1990, με κομμάτια όπως το 'Paranoid Android' και το 'Karma Police'.",
        "funFacts": [
            "Ηχογραφήθηκε κυρίως σε ένα ιστορικό παλιό αρχοντικό του 15ου αιώνα στο Somerset χωρίς παραδοσιακές εγκαταστάσεις στούντιο.",
            "Το 2014 η Βιβλιοθήκη του Κογκρέσου των ΗΠΑ επέλεξε το 'OK Computer' για διατήρηση στο Εθνικό Μητρώο Ηχογραφήσεων ως πολιτιστικά σημαντικό έργο."
        ],
        "source": "https://el.wikipedia.org/wiki/OK_Computer",
        "locale": "el-GR",
        "tags": ["radiohead", "ok-computer", "alternative-rock", "90s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_045",
        "text": "Ποιος θρυλικός Ινδός δεξιοτέχνης του σιτάρ δίδαξε τον George Harrison, έπαιξε στο Woodstock και υπήρξε πατέρας της τραγουδίστριας Norah Jones;",
        "answers": [
            "Ζακίρ Χουσεΐν",
            "Αλί Ακμπάρ Χαν",
            "Ραβί Σανκάρ",
            "Χαριπρασάντ Τσαουρασία"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Ravi Shankar υπήρξε ο κορυφαίος πρεσβευτής της ινδικής κλασικής μουσικής στη Δύση και κέρδισε πέντε βραβεία Grammy.",
        "funFacts": [
            "Μαζί με τον George Harrison διοργάνωσε το ιστορικό 'Concert for Bangladesh' στη Νέα Υόρκη το 1971, την πρώτη μεγάλη φιλανθρωπική ροκ συναυλία στην ιστορία.",
            "Η κόρη του Norah Jones κατέκτησε πέντε βραβεία Grammy το 2003 με το ντεμπούτο άλμπουμ της 'Come Away with Me'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B1%CE%B2%CE%AF_%CE%A3%CE%B1%CE%BD%CE%BA%CE%AC%CF%81",
        "locale": "el-GR",
        "tags": ["ravi-shankar", "sitar", "india", "world-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_046",
        "text": "Από ποια ιστορική ραδιοφωνική φράση του BBC World Service κατά τη διάρκεια του Β' Παγκοσμίου Πολέμου εμπνεύστηκαν οι The Clash τον τίτλο του άλμπουμ «London Calling» (1979);",
        "answers": [
            "Good morning Britain",
            "Radio Free Europe",
            "London Bridge is down",
            "This is London calling"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η φράση 'This is London calling' χρησιμοποιούνταν ως εισαγωγή στις ραδιοφωνικές εκπομπές του BBC προς την κατεχόμενη από τους Ναζί Ευρώπη.",
        "funFacts": [
            "Το τραγούδι αναφέρεται σε φόβους για πυρηνική καταστροφή, αστυνομική βία και πιθανή πλημμύρα του ποταμού Τάμεση στο Λονδίνο.",
            "Η γραμματοσειρά και ο σχεδιασμός του εξωφύλλου του δίσκου ήταν άμεσος φόρος τιμής στο πρώτο ομώνυμο άλμπουμ του Elvis Presley του 1956."
        ],
        "source": "https://el.wikipedia.org/wiki/London_Calling_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
        "locale": "el-GR",
        "tags": ["the-clash", "london-calling", "punk", "history"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_047",
        "text": "Ποιο όνομα έφερε το πρωτοποριακό συγκρότημα που συνόδευε τον Διονύση Σαββόπουλο στις αρχές της δεκαετίας του 1970, ηχογραφώντας μαζί του τον ιστορικό «Μπάλλο»;",
        "answers": [
            "Μπουρμπούλια",
            "Σπυριδούλα",
            "Τερμίτες",
            "Φατμέ"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Τα 'Μπουρμπούλια' συνδύασαν progressive rock με παραδοσιακή ελληνική δημοτική μουσική και παραμορφωμένες κιθάρες.",
        "funFacts": [
            "Στο συγκρότημα συμμετείχε ως τραγουδιστής για ένα διάστημα ο μετέπειτα μεγάλος τραγουδοποιός Νίκος Παπάζογλου.",
            "Μετά τη διάλυσή τους, ορισμένα μέλη των Μπουρμπουλιών συνεργάστηκαν με τον Παύλο Σιδηρόπουλο δημιουργώντας τα 'Δάμων και Φιντίας'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%BF%CE%BD%CF%8D%CF%83%CE%B7%CF%82_%CE%A3%CE%B1%CE%B2%CE%B2%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
        "locale": "el-GR",
        "tags": ["savvopoulos", "bourboulia", "greek-rock", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_048",
        "text": "Ποιος Αυστριακός ρομαντικός συνθέτης έγραψε περισσότερα από 600 κλασικά γερμανικά τραγούδια (Lieder), ανάμεσά τους τον «Βασιλιά των Ξωτικών» (Erlkönig) και τον κύκλο «Χειμωνιάτικο Ταξίδι»;",
        "answers": [
            "Ρόμπερτ Σούμαν",
            "Φραντς Σούμπερτ",
            "Γιοχάνες Μπραμς",
            "Φέλιξ Μέντελσον"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Franz Schubert υπήρξε ο αδιαμφισβήτητος μάστορας του γερμανικού λιντ (Lied), συνδυάζοντας την ποίηση με εκφραστική συνοδεία πιάνου.",
        "funFacts": [
            "Πέθανε σε ηλικία μόλις 31 ετών, έχοντας προλάβει να συνθέσει εννέα συμφωνίες, λειτουργίες και αμέτρητα έργα μουσικής δωματίου.",
            "Η 8η Συμφωνία του σε Σι ελάσσονα έμεινε στην ιστορία με το προσωνύμιο 'Ημιτελής' επειδή αποτελείται από μόνο δύο ολοκληρωμένα μέρη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%81%CE%B1%CE%BD%CF%84%CF%82_%CE%A3%CE%BF%CF%8D%CE%BC%CF%80%CE%B5%CF%81%CF%84",
        "locale": "el-GR",
        "tags": ["schubert", "classical", "lied", "romanticism"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_049",
        "text": "Ποια είναι η βασική δομική εξέλιξη του ρυθμού στον χορό συρτάκι που συνέθεσε ο Μίκης Θεοδωράκης για τον «Αλέξη Ζορμπά»;",
        "answers": [
            "Γρήγορος 7/8 που γίνεται αργός 2/4",
            "Σταθερός 9/8 ζεϊμπέκικος",
            "Αργός 4/4 χασάπικος που επιταχύνει σε γρήγορο 2/4 χασαποσέρβικο",
            "Αργός καλαματιανός που καταλήγει σε βαλς"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το συρτάκι ξεκινά αργόσυρτα με βήματα παραδοσιακού χασάπικου σε μέτρο 4/4 και σταδιακά επιταχύνει δραματικά σε ρυθμό γρήγορου χασαποσέρβικου σε μέτρο 2/4.",
        "funFacts": [
            "Ο χορός δεν υπήρχε ως αυθεντικός παραδοσιακός λαϊκός χορός, αλλά χορογραφήθηκε από τον Γιώργο Προβιά ειδικά για την ταινία του Μιχάλη Κακογιάννη το 1964.",
            "Ο ηθοποιός Anthony Quinn είχε σπάσει το πόδι του λίγο πριν από τα γυρίσματα, γεγονός που οδήγησε στα συρτά, αργά εισαγωγικά βήματα επειδή δεν μπορούσε να πηδήξει."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CF%81%CF%84%CE%AC%CE%BA%CE%B9",
        "locale": "el-GR",
        "tags": ["sirtaki", "theodorakis", "zorba", "dance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_050",
        "text": "Ποιο ήταν το ντεμπούτο άλμπουμ των Daft Punk το 1997, ηχογραφημένο στο υπνοδωμάτιο του Thomas Bangalter, που περιλάμβανε επιτυχίες όπως «Da Funk» και «Around the World»;",
        "answers": [
            "Discovery",
            "Human After All",
            "Random Access Memories",
            "Homework"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Homework' θεωρείται σταθμός της γαλλικής house μουσικής (French touch), συνδυάζοντας techno, funk, disco και electro ήχους.",
        "funFacts": [
            "Το διάσημο βιντεοκλίπ του 'Around the World' σκηνοθετήθηκε από τον Michel Gondry, με κάθε ομάδα χορευτών (μούμιες, σκελετοί, ρομπότ) να αναπαριστά οπτικά ένα διαφορετικό μουσικό όργανο.",
            "Την εποχή εκείνη τα μέλη των Daft Punk δεν φορούσαν ακόμη τα διάσημα κράνη ρομπότ, αλλά εμφανίζονταν φορώντας απλές αποκριάτικες μάσκες."
        ],
        "source": "https://el.wikipedia.org/wiki/Daft_Punk",
        "locale": "el-GR",
        "tags": ["daft-punk", "french-touch", "electronic", "90s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_051",
        "text": "Ποιο ιστορικό άλμπουμ του Μάνου Χατζιδάκι ηχογραφήθηκε στη Νέα Υόρκη το 1970 με αγγλικούς στίχους σε συνεργασία με το ροκ συγκρότημα New York Rock & Roll Ensemble;",
        "answers": [
            "Reflections",
            "Sweet Movie",
            "Gioconda's Smile",
            "Magnus Eroticus"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'Reflections' αποτέλεσε μια τολμηρή συνάντηση της μελωδικής ευαισθησίας του Χατζιδάκι με το αμερικανικό progressive και baroque rock.",
        "funFacts": [
            "Το 1993 το άλμπουμ διασκευάστηκε στα ελληνικά από το συγκρότημα Raining Pleasure, γνωρίζοντας τεράστια επιτυχία στη νεότερη γενιά.",
            "Περιλαμβάνει κλασικά θέματα όπως το 'Kemal' και το 'Noble Dame' (Το τραγούδι της καλής παρέας)."
        ],
        "source": "https://el.wikipedia.org/wiki/Reflections_(%CE%AC%CE%BB%CE%BC%CF%80%CE%BF%CF%85%CE%BC_%CF%84%CE%BF%CF%85_%CE%9C%CE%AC%CE%BD%CE%BF%CF%85_%CE%A7%CE%B1%CF%84%CE%B6%CE%B9%CE%B4%CE%AC%CE%BA%CE%B9)",
        "locale": "el-GR",
        "tags": ["chatzidakis", "reflections", "rock", "new-york"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_052",
        "text": "Ποιο πνευματικό τζαζ αριστούργημα ηχογράφησε ο σαξοφωνίστας John Coltrane το 1964 σε μία και μοναδική ημέρα στο στούντιο του Rudy Van Gelder;",
        "answers": [
            "Giant Steps",
            "A Love Supreme",
            "Blue Train",
            "My Favorite Things"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το 'A Love Supreme' αποτελείται από μια τετραμερή σουίτα και θεωρείται από τις κορυφαίες και βαθύτερες στιγμές στην ιστορία της τζαζ.",
        "funFacts": [
            "Τα τέσσερα μέρη της σουίτας είναι: 'Acknowledgement', 'Resolution', 'Pursuance' και 'Psalm'.",
            "Στο πρώτο μέρος, ο Coltrane ψέλνει με τη φωνή του το βασικό μοτίβο τεσσάρων φθόγγων 'A Love Supreme' σχεδόν είκοσι φορές."
        ],
        "source": "https://el.wikipedia.org/wiki/A_Love_Supreme",
        "locale": "el-GR",
        "tags": ["coltrane", "jazz", "saxophone", "spiritual-jazz"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_053",
        "text": "Ποιο μουσικό κίνημα γεννήθηκε στα τέλη της δεκαετίας του 1950 στο Ρίο ντε Τζανέιρο της Βραζιλίας από τους João Gilberto και Antônio Carlos Jobim, παντρεύοντας τη σάμπα με την τζαζ;",
        "answers": [
            "Τάνγκο",
            "Σάλσα",
            "Μπόσα Νόβα",
            "Κούμπια"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Η Μπόσα Νόβα (Bossa Nova, 'νέο κύμα/στυλ') χαρακτηρίζεται από απαλά ψιθυριστά φωνητικά, εκλεπτυσμένες συγχορδίες κιθάρας και χαλαρό ρυθμό.",
        "funFacts": [
            "Το τραγούδι 'The Girl from Ipanema' (Garota de Ipanema) έγινε παγκόσμιο φαινόμενο και αποτελεί ένα από τα πιο πολυηχογραφημένα ποπ τραγούδια στην ιστορία.",
            "Το ιστορικό άλμπουμ 'Getz/Gilberto' (1964) απέσπασε το βραβείο Grammy για το Άλμπουμ της Χρονιάς, κάτι πρωτοφανές για λάτιν τζαζ παραγωγή."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%8C%CF%83%CE%B1_%CE%BD%CF%8C%CE%B2%CE%B1",
        "locale": "el-GR",
        "tags": ["bossa-nova", "brazil", "jazz", "latin"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_054",
        "text": "Ποιος μπασίστας των Black Sabbath υπήρξε ο βασικός στιχουργός του συγκροτήματος, γράφοντας τους σκοτεινούς στίχους για κλασικά κομμάτια όπως «War Pigs», «Iron Man» και «Paranoid»;",
        "answers": [
            "Tony Iommi",
            "Bill Ward",
            "Ozzy Osbourne",
            "Geezer Butler"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Geezer Butler άντλησε έμπνευση από τον αποκρυφισμό, τη θεολογία, την επιστημονική φαντασία και τον πόλεμο του Βιετνάμ για τους στίχους των Black Sabbath.",
        "funFacts": [
            "Ήταν ένας από τους πρώτους μπασίστες στη heavy metal που χρησιμοποίησε πεντάλ εφέ wah-wah στο μπάσο, όπως στην εισαγωγή του 'N.I.B.'.",
            "Το πραγματικό του όνομα είναι Terence Michael Joseph Butler και απέκτησε το προσωνύμιο 'Geezer' στο σχολείο επειδή αποκαλούσε έτσι όλους τους φίλους του."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%AF%CE%B6%CE%B5%CF%81_%CE%9C%CF%80%CE%AC%CF%84%CE%BB%CE%B5%CF%81",
        "locale": "el-GR",
        "tags": ["black-sabbath", "geezer-butler", "metal", "lyrics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_055",
        "text": "Ποιος αγαπημένος τραγουδοποιός από τη Θεσσαλονίκη καθιέρωσε το χαρακτηριστικό κόκκινο μαντήλι στον λαιμό και υπέγραψε διαχρονικά τραγούδια όπως ο «Αύγουστος» και το «Χαράτσι»;",
        "answers": [
            "Νίκος Παπάζογλου",
            "Σωκράτης Μάλαμας",
            "Θανάσης Παπακωνσταντίνου",
            "Ορφέας Περίδης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Νίκος Παπάζογλου δημιούργησε μια ολόκληρη σχολή στο ελληνικό τραγούδι, παντρεύοντας το ηλεκτρικό ροκ με το γνήσιο λαϊκό και παραδοσιακό άκουσμα.",
        "funFacts": [
            "Ίδρυσε το ιστορικό στούντιο 'Αγροτικόν' στην Τούμπα Θεσσαλονίκης, όπου ηχογραφήθηκαν μερικοί από τους πιο καθοριστικούς δίσκους της ελληνικής εναλλακτικής και λαϊκής σκηνής.",
            "Το κόκκινο μαντήλι στον λαιμό ξεκίνησε να το φοράει αρχικά για να προστατεύει τις φωνητικές του χορδές από τον ιδρώτα και τον αέρα στις συναυλίες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%A0%CE%B1%CF%80%CE%AC%CE%B6%CE%BF%CE%B3%CE%BB%CE%BF%CF%85",
        "locale": "el-GR",
        "tags": ["papazoglou", "thessaloniki", "greek-music", "rock-laiko"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_056",
        "text": "Ποιο πρωτοποριακό μπαλέτο του Igor Stravinsky προκάλεσε πρωτοφανή ταραχή και συμπλοκές ανάμεσα στους θεατές κατά την πρεμιέρα του στο Παρίσι το 1913;",
        "answers": [
            "Το Πουλί της Φωτιάς",
            "Η Ιεροτελεστία της Άνοιξης",
            "Πετρούσκα",
            "Απόλλων Μουσηγέτης"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "'Η Ιεροτελεστία της Άνοιξης' (Le Sacre du Printemps) σόκαρε το κοινό με τους ασύμμετρους βίαιους ρυθμούς, τις παραφωνίες και τη γήινη παγανιστική χορογραφία του Vaslav Nijinsky.",
        "funFacts": [
            "Οι αποδοκιμασίες και οι καυγάδες μεταξύ των συντηρητικών θεατών και της πρωτοπορίας ήταν τόσο δυνατοί που οι χορευτές στη σκηνή δεν άκουγαν την ορχήστρα.",
            "Το έργο θεωρείται σήμερα ένα από τα σημαντικότερα μουσικά αριστουργήματα του 20ού αιώνα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%99%CE%B5%CF%81%CE%BF%CF%84%CE%B5%CE%BB%CE%B5%CF%83%CF%84%CE%AF%CE%B1_%CF%84%CE%B7%CF%82_%CE%86%CE%BD%CE%BF%CE%B9%CE%BE%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["stravinsky", "ballet", "modern-classical", "paris"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_057",
        "text": "Ποιο πανάρχαιο πνευστό μουσικό όργανο, κατασκευασμένο παραδοσιακά από κορμούς ευκαλύπτου κουφωμένους από τερμίτες, αναπτύχθηκε από τους αυτόχθονες Αβορίγινες της Αυστραλίας;",
        "answers": [
            "Σακουχάτσι",
            "Πανδούρα",
            "Ντιντζεριντού",
            "Νέι"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Το ντιντζεριντού (didgeridoo) παράγει έναν βαθύ βόμβο με πλούσιες αρμονικές και παίζεται με την τεχνική της κυκλικής αναπνοής.",
        "funFacts": [
            "Η κυκλική αναπνοή επιτρέπει στον εκτελεστή να εισπνέει από τη μύτη ενώ ταυτόχρονα εξωθεί αέρα από τα μάγουλα στο στόμιο, διατηρώντας έναν αδιάκοπο ήχο για δεκάδες λεπτά.",
            "Αρχαιολογικές ενδείξεις και βραχογραφίες υποδηλώνουν ότι το όργανο χρησιμοποιείται σε τελετές εδώ και τουλάχιστον 1.500 χρόνια."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%B9%CE%BD%CF%84%CE%B6%CE%B5%CF%81%CE%B9%CE%BD%CF%84%CE%BF%CF%8D",
        "locale": "el-GR",
        "tags": ["didgeridoo", "aboriginal", "instruments", "australia"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_058",
        "text": "Ποιο αμερικανικό jazz-rock συγκρότημα, με ιδρυτές τους τελειομανείς μουσικούς Walter Becker και Donald Fagen, κυκλοφόρησε το θρυλικό για την ηχητική του πιστότητα άλμπουμ «Aja» (1977);",
        "answers": [
            "Chicago",
            "Toto",
            "Doobie Brothers",
            "Steely Dan"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Οι Steely Dan ήταν διάσημοι για την εμμονή τους στην ηχητική τελειότητα στο στούντιο, προσλαμβάνοντας δεκάδες κορυφαίους session μουσικούς για κάθε κομμάτι.",
        "funFacts": [
            "Το άλμπουμ 'Aja' χρησιμοποιείται μέχρι σήμερα από ηχολήπτες και λάτρεις του hi-fi ως σημείο αναφοράς για τη δοκιμή της ποιότητας ηχοσυστημάτων.",
            "Το σόλο σαξόφωνο στο ομώνυμο τραγούδι 'Aja' παίχτηκε από τον θρυλικό τζαζίστα Wayne Shorter."
        ],
        "source": "https://el.wikipedia.org/wiki/Steely_Dan",
        "locale": "el-GR",
        "tags": ["steely-dan", "jazz-rock", "audiophile", "70s"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_059",
        "text": "Ποιος σπουδαίος Έλληνας συνθέτης και πιανίστας υπήρξε ο πρωτεργάτης του «Νέου Κύματος» στη δεκαετία του 1960 μελοποιώντας ποιητές στις περίφημες «Ανθολογίες» του;",
        "answers": [
            "Γιάννης Σπανός",
            "Λίνος Κόκοτος",
            "Νότης Μαυρουδής",
            "Κώστας Χατζής"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Γιάννης Σπανός έφερε το στυλ του γαλλικού chanson στις μπουάτ της Πλάκας, διαμορφώνοντας τον λιτό και ευαίσθητο ήχο του Νέου Κύματος.",
        "funFacts": [
            "Στις τρεις ιστορικές 'Ανθολογίες' του μελοποίησε σπουδαίους ποιητές όπως ο Κώστας Καρυωτάκης, ο Μιλτιάδης Μαλακάσης και ο Ζαχαρίας Παπαντωνίου.",
            "Τραγούδια του όπως 'Μια αγάπη για το καλοκαίρι' και 'Άσπρα καράβια' σημάδεψαν ανεξίτηλα μια ολόκληρη γενιά."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%A3%CF%80%CE%B1%CE%BD%CF%8C%CF%82",
        "locale": "el-GR",
        "tags": ["spanos", "neo-kyma", "anthologies", "greek-music"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "music_med_060",
        "text": "Ποιος χαρισματικός ποιητής και τραγουδιστής των The Doors, γνωστός και ως «Lizard King», έφυγε μυστηριωδώς από τη ζωή στο Παρίσι το 1971 σε ηλικία 27 ετών;",
        "answers": [
            "Kurt Cobain",
            "Jim Morrison",
            "Jimi Hendrix",
            "Janis Joplin"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "music",
        "difficulty": 3,
        "explanation": "Ο Jim Morrison υπήρξε μία από τις πιο εμβληματικές και επαναστατικές φιγούρες της ψυχεδελικής ροκ των 1960s.",
        "funFacts": [
            "Ο τάφος του στο ιστορικό νεκροταφείο Père Lachaise στο Παρίσι αποτελεί έναν από τους πιο επισκέψιμους τάφους στον κόσμο.",
            "Πάνω στην ταφόπλακά του υπάρχει η αρχαιοελληνική επιγραφή «ΚΑΤΑ ΤΟΝ ΔΑΙΜΟΝΑ ΕΑΥΤΟΥ».",
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%B9%CE%BC_%CE%9C%CF%8C%CF%81%CE%B9%CF%83%CE%BF%CE%BD",
        "locale": "el-GR",
        "tags": ["doors", "jim-morrison", "psychedelic-rock", "27-club"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(questions)} questions to append.")
    validate_and_append('music', 'medium', 3, questions)

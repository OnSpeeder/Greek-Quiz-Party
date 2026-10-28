# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_easy_061",
    "text": "Ποιον αδίστακτο εκδικητή εκτελεστή υποδύεται ο Κιάνου Ριβς στην ομώνυμη σειρά ταινιών δράσης που ξεκίνησε το 2014;",
    "answers": ["Τζον Γουίκ", "Τζέισον Μπορν", "Τζακ Ρίτσερ", "Ίθαν Χαντ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Keanu Reeves πρωταγωνιστεί ως John Wick, ένας θρυλικός πρώην πληρωμένος δολοφόνος που επιστρέφει στον υπόκοσμο για εκδίκηση.",
    "funFacts": [
      "Ο Ριβς εκτέλεσε μόνος του σχεδόν το 90% των επικίνδυνων σκηνών μάχης και οδήγησης στην πρώτη ταινία.",
      "Το franchise έγινε διάσημο για το στυλ μάχης 'gun-fu', που συνδυάζει πολεμικές τέχνες τζούντο και ζίου-ζίτσου με πιστολίδι εξ επαφής."
    ],
    "source": "https://el.wikipedia.org/wiki/John_Wick",
    "locale": "el-GR",
    "tags": ["john-wick", "keanu-reeves", "action", "hollywood"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_062",
    "text": "Ποιο είναι το όνομα του κοκκινομάλλη καλύτερου φίλου του Χάρι Πότερ από την οικογένεια των Ουέσλι;",
    "answers": ["Νέβιλ", "Ρον", "Ντράκο", "Σέιμους"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ρον Ουέσλι (Ron Weasley) είναι ο αχώριστος φίλος του Χάρι Πότερ και της Ερμιόνης Γκρέιντζερ σε όλες τις περιπέτειες της σειράς.",
    "funFacts": [
      "Τον ρόλο του Ρον στις οκτώ κινηματογραφικές ταινίες υποδύθηκε ο Βρετανός ηθοποιός Ρούπερτ Γκριντ.",
      "Ο Ρον έχει παθολογική φοβία με τις αράχνες (αραχνοφοβία), στοιχείο που εμπνεύστηκε η ίδια η συγγραφέας Τζ. Κ. Ρόουλινγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CE%BD_%CE%9F%CF%85%CE%AD%CF%83%CE%BB%CE%B9",
    "locale": "el-GR",
    "tags": ["harry-potter", "ron-weasley", "hogwarts", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_063",
    "text": "Ποια σπουδαία ηθοποιός ενσάρκωσε την εκκεντρική μητέρα «Παστελλίνα» στην κλασική κωμωδία «Μια τρελή, τρελή οικογένεια» (1965);",
    "answers": ["Ρένα Βλαχοπούλου", "Γεωργία Βασιλειάδου", "Μαίρη Αρώνη", "Σαπφώ Νοταρά"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Μαίρη Αρώνη έδωσε ένα ανεπανάληπτο ρεσιτάλ ως η ανέμελη, αριστοκράτισσα μητέρα που αναφωνούσε 'Μικρούλα μου!' και χόρευε μανιωδώς.",
    "funFacts": [
      "Η ταινία της Φίνος Φιλμ ήταν βασισμένη στο θεατρικό έργο των Νίκου Τσιφόρου και Πολύβιου Βασιλειάδη.",
      "Παρά τη μεγάλη της καριέρα στο θέατρο, αυτή ήταν μία από τις ελάχιστες κινηματογραφικές εμφανίσεις της Μαίρης Αρώνη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CF%84%CF%81%CE%B5%CE%BB%CE%AE,_%CF%84%CF%81%CE%B5%CE%BB%CE%AE_%CE%BF%CE%B9%CE%BA%CE%BF%CE%B3%CE%AD%CE%BD%CE%B5%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "mary-aroni", "comedy", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_064",
    "text": "Στην πρώτη ταινία των «Πειρατών της Καραϊβικής» (2003), ποια κατάρα μετέτρεπε το πλήρωμα του Μπαρμπόσα σε ζωντανούς σκελετούς;",
    "answers": ["Η κατάρα της Μέδουσας", "Το ξόρκι του Ποσειδώνα", "Το δηλητήριο του Κράκεν", "Ο καταραμένος χρυσός των Αζτέκων"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Οι πειρατές έκλεψαν τα 882 χρυσά νομίσματα του Ερνάν Κορτές από το σεντούκι των Αζτέκων, με αποτέλεσμα να γίνουν καταραμένοι απέθαντοι.",
    "funFacts": [
      "Κάτω από το φως του φεγγαριού αποκαλυπτόταν η πραγματική τους μορφή ως σκελετοί.",
      "Η πρώτη ταινία 'Η Κατάρα του Μαύρου Μαργαριταριού' βασίστηκε σε θεματικό τρενάκι των πάρκων της Disneyland."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%A0%CE%B5%CE%B9%CF%81%CE%B1%CF%84%CE%AD%CF%82_%CF%84%CE%B7%CF%82_%CE%9A%CE%B1%CF%81%CE%B1%CF%8A%CE%B2%CE%B9%CE%BA%CE%AE%CF%82:_%CE%97_%CE%9A%CE%B1%CF%84%CE%AC%CF%81%CE%B1_%CF%84%CE%BF%CF%85_%CE%9C%CE%B1%CF%8D%CF%81%CE%BF%CF%85_%CE%9C%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%B9%CF%84%CE%B1%CF%81%CE%B9%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["pirates", "disney", "fantasy", "jack-sparrow"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_065",
    "text": "Σε ποια φανταστική φυλή μικρόσωμων πλασμάτων ανήκει ο Φρόντο Μπάγκινς στον «Άρχοντα των Δαχτυλιδιών»;",
    "answers": ["Χόμπιτ", "Ξωτικά", "Νάνοι", "Ορκ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Frodo Baggins είναι ένα Χόμπιτ (Hobbit) από το Σάιρ (Shire), γνωστό για το μικρό ανάστημα και τα τριχωτά πόδια των εκπροσώπων της φυλής του.",
    "funFacts": [
      "Τα Χόμπιτ αγαπούν την καλή ζωή, το φαγητό και απολαμβάνουν παραδοσιακά επτά γεύματα την ημέρα.",
      "Τον Φρόντο υποδύθηκε στην κινηματογραφική τριλογία του Πίτερ Τζάκσον ο Αμερικανός ηθοποιός Ελάιτζα Γουντ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CF%8C%CE%BC%CF%80%CE%B9%CF%84",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "hobbit", "frodo", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_066",
    "text": "Ποια παράνομη ουσία με το χαρακτηριστικό μπλε χρώμα παρασκευάζει ο Γουόλτερ Γουάιτ στη σειρά «Breaking Bad»;",
    "answers": ["Ηρωίνη", "Μεθαμφεταμίνη", "Κοκαΐνη", "Μορφίνη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Walter White χρησιμοποιεί τις γνώσεις του στη χημεία για να παράγει εξαιρετικά καθαρή μπλε κρυσταλλική μεθαμφεταμίνη (Blue Sky).",
    "funFacts": [
      "Στα γυρίσματα της σειράς χρησιμοποιήθηκαν θρυμματισμένα μπλε ζαχαρωτά καραμέλας (rock candy) αντί για πραγματικά ναρκωτικά.",
      "Η σειρά απέσπασε 16 βραβεία Primetime Emmy και θεωρείται από τις κορυφαίες δραματικές παραγωγές στην ιστορία της τηλεόρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/Breaking_Bad",
    "locale": "el-GR",
    "tags": ["breaking-bad", "walter-white", "tv-series", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_067",
    "text": "Ποιος αγαπημένος ηθοποιός πρωταγωνίστησε ως ο επαγγελματίας ψεύτης Θεόδωρος Πάρλας στην κωμωδία «Ζητείται ψεύτης» (1961);",
    "answers": ["Λάμπρος Κωνσταντάρας", "Κώστας Χατζηχρήστος", "Ντίνος Ηλιόπουλος", "Μίμης Φωτόπουλος"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ντίνος Ηλιόπουλος ενσάρκωσε τον 'Ψευτοθόδωρο', που προσλαμβάνεται από έναν βουλευτή για να λέει πειστικά ψέματα στους ψηφοφόρους του.",
    "funFacts": [
      "Η ταινία της Φίνος Φιλμ βασίστηκε στο θεατρικό έργο του Δημήτρη Ψαθά.",
      "Ο Ντίνος Ηλιόπουλος ξεχώριζε για την αέρινη κίνησή του, τους ευγενικούς τρόπους και τις χορευτικές του ικανότητες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B7%CF%84%CE%B5%CE%AF%CF%84%CE%B1%CE%B9_%CF%88%CE%B5%CF%8D%CF%84%CE%B7%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1961)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dinos-iliopoulos", "comedy", "psathas"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_068",
    "text": "Ποιο μαγικό όπλο κραδαίνει ο Σκανδιναβός θεός Θορ στις ταινίες του κινηματογραφικού σύμπαντος της Marvel;",
    "answers": ["Ένα δόρυ φωτιάς", "Ένα χρυσό τόξο", "Ένα μαγικό σπαθί", "Το σφυρί Μγιόλνιρ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Thor κρατά το πανίσχυρο σφυρί Mjolnir, το οποίο μπορεί να σηκώσει μόνο όποιος αποδειχθεί 'άξιος' (worthy).",
    "funFacts": [
      "Στον κινηματογράφο τον Θορ υποδύεται ο Αυστραλός ηθοποιός Κρις Χέμσγουορθ.",
      "Σύμφωνα με τον μύθο της Marvel, το Μγιόλνιρ σφυρηλατήθηκε στην καρδιά ενός ετοιμοθάνατου άστρου από τους νάνους του Νινταβελίρ."
    ],
    "source": "https://el.wikipedia.org/wiki/Thor_(Marvel_Comics)",
    "locale": "el-GR",
    "tags": ["marvel", "thor", "superheroes", "avengers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_069",
    "text": "Στην ιστορική κωμική σειρά «Οι Απαράδεκτοι» (Mega, 1991–1993), ποιοι δύο ηθοποιοί υποδύονταν το παντρεμένο ζευγάρι;",
    "answers": ["Ο Σπύρος Παπαδόπουλος και η Δήμητρα Παπαδοπούλου", "Ο Γιάννης Μπέζος and η Ρένια Λουιζίδου", "Ο Βλάσσης Μπονάτσος and η Δήμητρα Παπαδοπούλου", "Ο Σπύρος Παπαδόπουλος and η Ρένια Λουιζίδου"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Σπύρος και η Δήμητρα ήταν το κεντρικό παντρεμένο ζευγάρι της πολυκατοικίας στην οδό Αδάμαντος στον Λυκαβηττό.",
    "funFacts": [
      "Το ευρηματικό σενάριο της σειράς έγραψε η ίδια η Δήμητρα Παπαδοπούλου.",
      "Η σειρά θεωρείται ορόσημο της ιδιωτικής ελληνικής τηλεόρασης και ανέδειξε κορυφαίες ατάκες όπως 'Τι έγινε, ρε παιδιά;'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "aparadektoi", "mega-channel", "sitcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_070",
    "text": "Ποιο είναι το όνομα της κοκκινομάλλας πριγκίπισσας γοργόνας στην κλασική ταινία της Disney «Η Μικρή Γοργόνα» (1989);",
    "answers": ["Μπελ", "Άριελ", "Τιάνα", "Γιασμίν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Άριελ (Ariel) είναι η νεαρή κόρη του βασιλιά Τρίτωνα που ονειρεύεται να γνωρίσει τον κόσμο των ανθρώπων στη στεριά.",
    "funFacts": [
      "Η επιτυχία της 'Μικρής Γοργόνας' εγκαινίασε τη χρυσή περίοδο γνωστή ως 'Αναγέννηση της Disney' (Disney Renaissance).",
      "Η ταινία κέρδισε δύο Όσκαρ: Καλύτερης Πρωτότυπης Μουσικής και Καλύτερου Τραγουδιού για το 'Under the Sea'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%9C%CE%B9%CE%BA%CF%81%CE%AE_%CE%93%CE%BF%CF%81%CE%B3%CF%8C%CE%BD%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1989)",
    "locale": "el-GR",
    "tags": ["disney", "the-little-mermaid", "animation", "ariel"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_071",
    "text": "Ποιος πράσινος και σοφός δάσκαλος των Τζεντάι μιλά με ανεστραμμένη σύνταξη προτάσεων στον κόσμο του «Star Wars»;",
    "answers": ["Όμπι-Ουάν Κενόμπι", "Μέις Γουίντου", "Γιόντα", "Κουάι-Γκον Τζιν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Yoda είναι ο αιωνόβιος Μέγας Δάσκαλος του Τάγματος των Τζεντάι που εκπαίδευσε γενιές ιπποτών, ανάμεσά τους και τον Λουκ Σκαϊγουόκερ.",
    "funFacts": [
      "Στην αρχική τριλογία, ο Γιόντα ήταν μια μαριονέτα που χειριζόταν και δάνειζε τη φωνή του ο διάσημος μαριονετίστας Frank Oz.",
      "Έζησε περίπου 900 χρόνια πριν πεθάνει γαλήνια στο απομονωμένο έλος του πλανήτη Ντάγκομπα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CE%BD%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["star-wars", "yoda", "jedi", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_072",
    "text": "Ποιος αγαπημένος κωμικός έμεινε στην ιστορία ως ο ζηλιάρης σύζυγος που έψαχνε «Τα κίτρινα γάντια» (1960);",
    "answers": ["Βασίλης Αυλωνίτης", "Κώστας Βουτσάς", "Διονύσης Παπαγιαννόπουλος", "Νίκος Σταυρίδης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Νίκος Σταυρίδης υποδύθηκε τον παθολογικά ζηλιάρη Ορέστη Καλλιγαρίδη που υποπτεύεται τη γυναίκα του για ένα ζευγάρι κίτρινα γάντια.",
    "funFacts": [
      "Στην ίδια ταινία εκτυλίσσεται ο ιστορικός διάλογος με τον Γκιωνάκη για την 'πορτοκαλάδα από πορτοκάλια'.",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο και αποτελεί μία από τις δημοφιλέστερες κωμωδίες της Φίνος Φιλμ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%BA%CE%AF%CF%84%CF%81%CE%B9%CE%BD%CE%B1_%CE%B3%CE%AC%CE%BD%CF%84%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "nikos-stavridis", "comedy", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_073",
    "text": "Σε ποιο άθλημα ανακάλυψε ότι έχει εκπληκτικό φυσικό ταλέντο ο Φόρεστ Γκαμπ όσο ανάρρωνε στο στρατιωτικό νοσοκομείο;",
    "answers": ["Επιτραπέζια αντισφαίριση (Πινγκ-πονγκ)", "Μπέιζμπολ", "Μπάσκετ", "Γκολφ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Forrest Gump έμαθε πινγκ-πονγκ κρατώντας πάντα το μάτι του στο μπαλάκι, φτάνοντας μέχρι την εθνική ομάδα των ΗΠΑ που επισκέφθηκε την Κίνα.",
    "funFacts": [
      "Στα γυρίσματα της ταινίας το μπαλάκι του πινγκ-πονγκ δεν υπήρχε στην πραγματικότητα, αλλά προστέθηκε ψηφιακά με ειδικά εφέ.",
      "Η σκηνή αποτελεί αναφορά στην πραγματική 'διπλωματία του πινγκ-πονγκ' ανάμεσα στις ΗΠΑ και την Κίνα τη δεκαετία του 1970."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%8C%CF%81%CE%B5%CF%83%CF%84_%CE%93%CE%BA%CE%B1%CE%BC%CF%80",
    "locale": "el-GR",
    "tags": ["forrest-gump", "tom-hanks", "cinema", "sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_074",
    "text": "Ποιο είναι το επώνυμο της ισχυρής οικογένειας μαφιόζων στην τριλογία του «Νονού» (The Godfather);",
    "answers": ["Σοπράνο", "Κορλεόνε", "Μπαρζίνι", "Σκαρφέις"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η ιστορία περιστρέφεται γύρω από την οικογένεια Corleone υπό την ηγεσία του Don Vito και αργότερα του γιου του, Michael Corleone.",
    "funFacts": [
      "Το όνομα Κορλεόνε προέρχεται από την πραγματική κωμόπολη Corleone στη Σικελία.",
      "Η πρώτη ταινία (1972) απέσπασε τρία βραβεία Όσκαρ: Καλύτερης Ταινίας, Α' Ανδρικού Ρόλου (Μάρλον Μπράντο) και Διασκευασμένου Σεναρίου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9D%CE%BF%CE%BD%CF%8C%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["the-godfather", "corleone", "mafia", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_075",
    "text": "Σε ποιο φανταστικό χωριό της Αρκαδίας διαδραματίζεται η δημοφιλής σειρά του ΑΝΤ1 «Το Καφέ της Χαράς»;",
    "answers": ["Αράχοβα", "Πλάτανος", "Κολοκοτρωνίτσι", "Καστανιά"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Κολοκοτρωνίτσι είναι το συντηρητικό χωριό όπου δήμαρχος ήταν ο αυστηρός Περίανδρος Πώποτας (Χάρης Ρώμας).",
    "funFacts": [
      "Τα εξωτερικά γυρίσματα του χωριού πραγματοποιήθηκαν κυρίως στην Καρυά Αργολίδας.",
      "Το σύνθημα του Περίανδρου Πώποτα που έγινε σλόγκαν ήταν 'Τάξις και Ηθική'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9A%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-kafe-tis-charas", "ant1", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_076",
    "text": "Ποιος σταρ του Χόλιγουντ υποδύθηκε τον φτωχό ζωγράφο Τζακ Ντόσον στην ταινία «Τιτανικός» (1997);",
    "answers": ["Μπραντ Πιτ", "Τομ Κρουζ", "Ματ Ντέιμον", "Λεονάρντο Ντι Κάπριο"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Leonardo DiCaprio έγινε παγκόσμιο είδωλο υποδυόμενος τον Jack Dawson, που κερδίζει ένα εισιτήριο τρίτης θέσης στα χαρτιά και ερωτεύεται τη Rose.",
    "funFacts": [
      "Ο ίδιος ο σκηνοθέτης Τζέιμς Κάμερον σχεδίασε όλα τα σκίτσα στο μπλοκ του Τζακ, συμπεριλαμβανομένου του διάσημου πορτρέτου της Ρόουζ.",
      "Ο ρόλος αυτός εκτόξευσε τη λεγόμενη 'Leo-mania' σε όλο τον πλανήτη στα τέλη των 90s."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9%CF%84%CE%B1%CE%BD%CE%B9%CE%BA%CF%8C%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1997)",
    "locale": "el-GR",
    "tags": ["titanic", "leonardo-dicaprio", "romance", "blockbuster"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_077",
    "text": "Σε ποια ακριβώς ώρα έσπαγαν τα μάγια της νεραϊδονονάς για τη Σταχτοπούτα στην κλασική ταινία της Disney;",
    "answers": ["Στις 12 τα μεσάνυχτα", "Στις 6 το πρωί", "Στο ηλιοβασίλεμα", "Στις 3 τα ξημερώματα"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η νονά προειδοποίησε τη Σταχτοπούτα πως στο τελευταίο χτύπημα των μεσανυχτών η άμαξα θα ξαναγινόταν κολοκύθα και τα ρούχα της κουρέλια.",
    "funFacts": [
      "Φεύγοντας βιαστικά από το παλάτι τα μεσάνυχτα, έχασε το ένα από τα γυάλινα γοβάκια της στα σκαλιά.",
      "Η ταινία της Disney κυκλοφόρησε το 1950 και έσωσε το στούντιο από σοβαρά οικονομικά προβλήματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B1%CF%87%CF%84%CE%BF%CF%80%CE%BF%CF%8D%CF%84%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1950)",
    "locale": "el-GR",
    "tags": ["disney", "cinderella", "animation", "fairy-tale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_078",
    "text": "Ποιος υπήρξε ο πρώτος ηθοποιός που υποδύθηκε τον Τζέιμς Μποντ στην επίσημη κινηματογραφική σειρά ταινιών;",
    "answers": ["Ρότζερ Μουρ", "Σον Κόνερι", "Πιρς Μπρόσναν", "Ντάνιελ Κρεγκ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Σκωτσέζος ηθοποιός Sean Connery πρωταγωνίστησε στην πρώτη ταινία 'Dr. No' (1962) και σε άλλες έξι ταινίες ως πράκτορας 007.",
    "funFacts": [
      "Ο συγγραφέας Ίαν Φλέμινγκ αρχικά αμφέβαλλε για τον Κόνερι, αλλά εντυπωσιάστηκε τόσο από την ερμηνεία του που πρόσθεσε σκωτσέζικη καταγωγή στον Μποντ.",
      "Ο Σον Κόνερι κέρδισε αργότερα Όσκαρ Β' Ανδρικού Ρόλου για την ταινία 'Οι Αδιάφθοροι' (1987)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%BF%CE%BD_%CE%9A%CF%8C%CE%BD%CE%B5%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["james-bond", "sean-connery", "007", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_079",
    "text": "Στην κλασική κωμωδία «Της κακομοίρας» (1963), τι είδους κατάστημα διατηρεί ο κυρ-Παντελής όπου εργάζεται ο Ζήκος;",
    "answers": ["Φαρμακείο", "Κουρείο", "Μπακάλικο (παντοπωλείο)", "Καφενείο"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ζήκος (Κώστας Χατζηχρήστος) είναι ο επαρχιώτης υπάλληλος του μπακάλικου που μοιράζει παραγγελίες και μπλέκει σε κωμικές καταστάσεις.",
    "funFacts": [
      "Η ταινία έμεινε ευρύτερα γνωστή στο κοινό με τον ανεπίσημο τίτλο 'Ο Μπακαλόγατος'.",
      "Οι περισσότερες από τις ξεκαρδιστικές ατάκες του Ζήκου προέκυψαν από επί τόπου αυτοσχεδιασμό του Χατζηχρήστου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%BA%CE%B1%CE%BA%CE%BF%CE%BC%CE%BF%CE%AF%CF%81%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "chatzichristos", "comedy", "bakalogatos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_080",
    "text": "Ποιο είναι το όνομα του προγονικού κάστρου της οικογένειας Σταρκ στον παγωμένο Βορρά στο «Game of Thrones»;",
    "answers": ["Κινγκς Λάντινγκ", "Κάστερλι Ροκ", "Έιρι", "Γουίντερφελ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Winterfell είναι η αρχαία έδρα του Οίκου των Σταρκ και η πρωτεύουσα του Βορρά στα Επτά Βασίλεια.",
    "funFacts": [
      "Το μότο του Οίκου Σταρκ είναι η διάσημη προειδοποίηση 'Winter Is Coming' ('Ο χειμώνας έρχεται').",
      "Πολλές από τις σκηνές του Γουίντερφελ στην πρώτη σεζόν γυρίστηκαν στο Κάστρο Γουόρντ στη Βόρεια Ιρλανδία."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_of_Thrones",
    "locale": "el-GR",
    "tags": ["game-of-thrones", "winterfell", "stark", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_081",
    "text": "Ποιο ζώο είναι ο πολυλογάς και αστείος καλύτερος φίλος του Σρεκ στις ταινίες κινουμένων σχεδίων;",
    "answers": ["Ο Γάιδαρος", "Ο Σκύλος", "Το Άλογο", "Η Κατσίκα"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Donkey (Γάιδαρος) είναι ο πιστός και ασταμάτητος στην ομιλία σύντροφος του Σρεκ, που παντρεύεται μάλιστα μια δράκαινα.",
    "funFacts": [
      "Στην αγγλική εκδοχή τη φωνή του Γαϊδάρου χάρισε ο διάσημος κωμικός Έντι Μέρφι.",
      "Στην ελληνική μεταγλώττιση ο ηθοποιός Λυκούργος Μαρκούδης απέδωσε εξαιρετικά τον χαρακτήρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%81%CE%B5%CE%BA",
    "locale": "el-GR",
    "tags": ["shrek", "donkey", "animation", "dreamworks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_082",
    "text": "Ποια μοχθηρή και ψυχρή σύζυγο με τάσεις δολοφονίας υποδύθηκε η Υρώ Μανέ στη μαύρη κωμωδία «Εγκλήματα» (ΑΝΤ1);",
    "answers": ["Κορίνα", "Σωσώ Παπαδήμα", "Πέγκυ", "Μάχη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Σωσώ Παπαδήμα είναι ένας από τους πιο καλτ τηλεοπτικούς χαρακτήρες, διάσημη για τα δολοφονικά σχέδια εναντίον του άντρα της Αλέκου.",
    "funFacts": [
      "Η σειρά προβλήθηκε τις σεζόν 1998–2000 γνωρίζοντας τεράστια επιτυχία για το πρωτοποριακό μαύρο χιούμορ της.",
      "Η σκηνή όπου σχεδιάζει δηλητηριάσεις ακούγοντας κλασική μουσική παραμένει viral μέχρι σήμερα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "egklimata", "ant1", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_083",
    "text": "Ποιος ηθοποιός έγραψε το σενάριο και πρωταγωνίστησε ως ο θρυλικός πυγμάχος Ρόκι Μπαλμπόα (Rocky, 1976);",
    "answers": ["Άρνολντ Σβαρτσενέγκερ", "Μπρους Γουίλις", "Σιλβέστερ Σταλόνε", "Τσακ Νόρις"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Sylvester Stallone έγραψε το σενάριο σε μόλις τρεισήμισι ημέρες και αρνήθηκε να το πουλήσει αν δεν έπαιζε ο ίδιος τον πρωταγωνιστικό ρόλο.",
    "funFacts": [
      "Η ταινία κέρδισε τρία βραβεία Όσκαρ, συμπεριλαμβανομένου αυτού για την Καλύτερη Ταινία της χρονιάς.",
      "Τα 72 σκαλοπάτια του Μουσείου Τέχνης της Φιλαδέλφειας όπου προπονείται ο Ρόκι αποκαλούνται πλέον παγκοσμίως 'Rocky Steps'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%8C%CE%BA%CF%85:_%CE%A1%CF%8C%CE%BA%CE%B9_%CE%9C%CF%80%CE%B1%CE%BB%CE%BC%CF%80%CF%8C%CE%B1",
    "locale": "el-GR",
    "tags": ["rocky", "stallone", "sports", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_084",
    "text": "Σε ποια θέση αγωνίζεται ο Χάρι Πότερ στην ομάδα Κουίντιτς του κοιτώνα Γκρίφιντορ;",
    "answers": ["Κυνηγός", "Φύλακας", "Ροπαλοφόρος", "Αναζητητής"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Harry Potter είναι ο Αναζητητής (Seeker), με βασική αποστολή να εντοπίσει και να πιάσει τη μικρή Χρυσή Μπάλα (Golden Snitch).",
    "funFacts": [
      "Έγινε ο νεότερος Αναζητητής σε ομάδα κοιτώνα στο Χόγκουαρτς εδώ και έναν αιώνα, ξεκινώντας από το πρώτο του κιόλας έτος.",
      "Το πιάσιμο της Χρυσής Μπάλας χαρίζει 150 πόντους στην ομάδα και τερματίζει αυτόματα τον αγώνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CF%85%CE%AF%CE%BD%CF%84%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["harry-potter", "quidditch", "hogwarts", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_085",
    "text": "Ποια λαμπερή ηθοποιός υπήρξε μούσα της Φίνος Φιλμ σε ταινίες όπως «Ο κατήφορος», «Νόμος 4000» και «Στεφανία»;",
    "answers": ["Ζωή Λάσκαρη", "Έλενα Ναθαναήλ", "Μπέτυ Λιβανού", "Νόρα Βαλσάμη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ζωή Λάσκαρη (πρώην Σταρ Ελλάς 1959) καθιερώθηκε ως μία από τις μεγαλύτερες σταρ του ελληνικού κινηματογράφου μετά τον 'Κατήφορο' (1961).",
    "funFacts": [
      "Το πραγματικό της επώνυμο ήταν Κουρούκλη, αλλά ο Φιλοποίμην Φίνος επέλεξε το καλλιτεχνικό 'Λάσκαρη' για να μη συγχέεται με την εξαδέλφη της τραγουδίστρια.",
      "Υπήρξε η μοναδική Ελληνίδα ηθοποιός που δεν εμφανίστηκε ποτέ σε τηλεοπτική διαφήμιση στη ζωή της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CF%89%CE%AE_%CE%9B%CE%AC%CF%83%CE%BA%CE%B1%CF%81%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-cinema", "zoe-laskari", "finos-film", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_086",
    "text": "Ποιο χαρακτηριστικό εξάρτημα κουβαλούν στην πλάτη τους οι «Ghostbusters» για να αιχμαλωτίζουν φαντάσματα;",
    "answers": ["Εξαγνιστή νερού", "Πακέτο πρωτονίων (Proton Pack)", "Ανιχνευτή μαγνητισμού", "Κάτοπτρο ακτίνων λέιζερ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Proton Pack είναι ένας φορητός επιταχυντής σωματιδίων που εκτοξεύει δέσμη πρωτονίων για να παγιδεύει αρνητικά φορτισμένα φαντάσματα.",
    "funFacts": [
      "Ο βασικός κανόνας ασφαλείας των Ghostbusters ήταν να μην διασταυρώνουν ποτέ τις φωτεινές δέσμες τους ('Don't cross the streams!').",
      "Η ταινία του 1984 σημείωσε τεράστια εισπρακτική επιτυχία και το ομότιτλο τραγούδι του Ray Parker Jr. έγινε παγκόσμιο χιτ."
    ],
    "source": "https://el.wikipedia.org/wiki/Ghostbusters",
    "locale": "el-GR",
    "tags": ["ghostbusters", "80s", "sci-fi", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_087",
    "text": "Ποιο είναι το όνομα του δολοπλόκου θείου του Σίμπα που σφετερίζεται τον θρόνο στον «Βασιλιά των Λιονταριών»;",
    "answers": ["Μουφάσα", "Ζαζού", "Σκαρ", "Ραφίκι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Scar είναι ο ζηλόφθονος αδελφός του βασιλιά Μουφάσα που οργανώνει τη δολοφονία του για να αναλάβει την εξουσία στο Pride Rock.",
    "funFacts": [
      "Στην πρωτότυπη αγγλική εκδοχή τη φωνή του Σκαρ δάνεισε ο Βρετανός ηθοποιός Τζέρεμι Άιρονς.",
      "Το χαρακτηριστικό του όνομα οφείλεται στην ουλή (scar) που διατρέχει το αριστερό του μάτι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%B9%CE%AC%CF%82_%CF%84%CF%89%CE%BD_%CE%9B%CE%B9%CE%BF%CE%BD%CF%84%CE%B1%CF%81%CE%B9%CF%8E%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1994)",
    "locale": "el-GR",
    "tags": ["disney", "lion-king", "scar", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_088",
    "text": "Σε ποια ιστορική νησίδα της Κρήτης διαδραματίζεται η πολυβραβευμένη δραματική σειρά του Mega «Το Νησί» (2010);",
    "answers": ["Χρυσή", "Γαύδος", "Κουφονήσι", "Σπιναλόγκα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά βασίστηκε στο ομότιτλο βιβλίο της Βικτόρια Χίσλοπ και αφηγείται τη ζωή των χανσενικών (λεπρών) στη Σπιναλόγκα.",
    "funFacts": [
      "Υπήρξε μία από τις ακριβότερες τηλεοπτικές παραγωγές στην ιστορία της ελληνικής τηλεόρασης με κόστος σχεδόν 4 εκατομμύρια ευρώ.",
      "Τα γυρίσματα πραγματοποιήθηκαν εξ ολοκλήρου στην Κρήτη (Πλάκα, Ελούντα και πάνω στη Σπιναλόγκα)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9D%CE%B7%CF%83%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-nisi", "mega-channel", "spinalonga"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_089",
    "text": "Σε ποια σκοτεινή φανταστική αμερικανική μεγαλούπολη δρα ο υπερήρωας Μπάτμαν;",
    "answers": ["Γκόθαμ Σίτι (Gotham City)", "Μετρόπολις", "Σταρ Σίτι", "Σέντραλ Σίτι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Gotham City είναι η πόλη που προστατεύει ο Μπάτμαν, γνωστή για την υψηλή εγκληματικότητα και τη γοτθική αρχιτεκτονική της.",
    "funFacts": [
      "Το όνομα 'Gotham' ήταν ιστορικό παρατσούκλι της Νέας Υόρκης ήδη από τον 19ο αιώνα.",
      "Το ψυχιατρικό άσυλο όπου φυλάσσονται οι επικίνδυνοι κακοποιοί της πόλης ονομάζεται Arkham Asylum."
    ],
    "source": "https://el.wikipedia.org/wiki/Batman",
    "locale": "el-GR",
    "tags": ["batman", "gotham", "dc-comics", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_090",
    "text": "Ποιος κορυφαίος κωμικός πρωταγωνίστησε στις κλασικές ταινίες «Ο θησαυρός του μακαρίτη» και «Η καφετζού» δίπλα στη Γεωργία Βασιλειάδου;",
    "answers": ["Ντίνος Ηλιόπουλος", "Βασίλης Αυλωνίτης", "Μίμης Φωτόπουλος", "Κώστας Χατζηχρήστος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Βασίλης Αυλωνίτης και η Γεωργία Βασιλειάδου αποτέλεσαν ένα από τα πιο ακαταμάχητα και επιτυχημένα κωμικά δίδυμα του ελληνικού σινεμά.",
    "funFacts": [
      "Ο Αυλωνίτης ξεκίνησε την καριέρα του από την επιθεώρηση και το θέατρο σκιών πριν κατακτήσει τη μεγάλη οθόνη.",
      "Υπήρξε αυτοδίδακτος ηθοποιός με μοναδική φυσική εκφραστικότητα και χάρισμα στις γκριμάτσες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B7%CF%82_%CE%91%CF%85%CE%BB%CF%89%CE%BD%CE%AF%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "vasilis-avlonitis", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_091",
    "text": "Τι σημαίνει η διάσημη φράση «Hakuna Matata» από τη γλώσσα Σουαχίλι που τραγουδούν ο Τιμόν και ο Πούμπα;",
    "answers": ["Καλημέρα φίλε μου", "Εμπρός για κυνήγι", "Καμία έγνοια (κανένα πρόβλημα)", "Το λιοντάρι κοιμάται"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η φράση 'Hakuna Matata' προέρχεται από τα Σουαχίλι της Ανατολικής Αφρικής και μεταφράζεται κυριολεκτικά ως 'δεν υπάρχουν προβλήματα/έγνοιες'.",
    "funFacts": [
      "Το τραγούδι συνέθεσε ο Έλτον Τζον σε στίχους του Τιμ Ράις και ήταν υποψήφιο για Όσκαρ Καλύτερου Τραγουδιού.",
      "Στην ελληνική μεταγλώττιση ο Τιμόν και ο Πούμπα ερμηνεύτηκαν αξέχαστα από τον Ζανό Ντάνιας και τον Τάσο Κωστή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%B9%CE%AC%CF%82_%CF%84%CF%89%CE%BD_%CE%9B%CE%B9%CE%BF%CE%BD%CF%84%CE%B1%CF%81%CE%B9%CF%8E%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1994)",
    "locale": "el-GR",
    "tags": ["disney", "lion-king", "hakuna-matata", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_092",
    "text": "Στη σειρά «Friends», ποιο περίπλοκο επάγγελμα ασκούσε ο Τσάντλερ Μπινγκ που κανένας φίλος του δεν μπορούσε να θυμηθεί;",
    "answers": ["Παλαιοντολόγος", "Σεφ σε εστιατόριο", "Ηθοποιός σαπουνόπερας", "Ανάλυση και επεξεργασία δεδομένων"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Chandler Bing εργαζόταν στη 'στατιστική ανάλυση και αναδιαμόρφωση δεδομένων' (statistical analysis and data reconfiguration).",
    "funFacts": [
      "Στο περίφημο κουίζ για το διαμέρισμα, η Μόνικα και η Ρέιτσελ έχασαν γιατί είπαν λανθασμένα ότι είναι 'transponster'.",
      "Τον Τσάντλερ υποδύθηκε ο αγαπημένος ηθοποιός Μάθιου Πέρι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%A6%CE%B9%CE%BB%CE%B1%CF%81%CE%AC%CE%BA%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["friends", "chandler-bing", "sitcom", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_093",
    "text": "Ποια γοητευτική πρωταγωνίστρια τραγούδησε και χόρεψε το «Του αγοριού απέναντι» και το «Καμαρούλα μια σταλιά» στις ταινίες του Γιάννη Δαλιανίδη;",
    "answers": ["Μαίρη Χρονοπούλου", "Ζωή Λάσκαρη", "Μάρθα Καραγιάννη", "Μπέτυ Αρβανίτη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Μαίρη Χρονοπούλου σφράγισε τα ελληνικά μιούζικαλ με την αρχοντική παρουσία της σε ταινίες όπως 'Μια κυρία στα μπουζούκια' και 'Γοργόνες και μάγκες'.",
    "funFacts": [
      "Το τραγούδι 'Του αγοριού απέναντι' σε μουσική Μίμη Πλέσσα και στίχους Λευτέρη Παπαδόπουλου έγινε διαχρονικό σουξέ.",
      "Κέρδισε βραβείο Α' Γυναικείου Ρόλου στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης το 1987 για την ταινία 'Τα παιδιά της χελιδόνας'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%AF%CF%81%CE%B7_%CE%A7%CF%81%CE%BF%CE%BD%CE%BF%CF%80%CE%BF%CF%8D%CE%BB%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["greek-cinema", "mary-chronopoulou", "musical", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_094",
    "text": "Από ποιο άφθαρτο φανταστικό μέταλλο της Γουακάντα είναι κατασκευασμένη η ασπίδα του Captain America;",
    "answers": ["Αδαμάντιο", "Βιμπράνιο (Vibranium)", "Κρυπτονίτης", "Μιθρίλιο"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Vibranium είναι ένα σπάνιο εξωγήινο μέταλλο που απορροφά τους κραδασμούς και την κινητική ενέργεια, κάνοντας την ασπίδα άθραυστη.",
    "funFacts": [
      "Την ασπίδα κατασκεύασε ο Χάουαρντ Σταρκ, πατέρας του Τόνι Σταρκ (Iron Man), κατά τον Β' Παγκόσμιο Πόλεμο.",
      "Το ίδιο μέταλλο αποτελεί την πηγή της τεχνολογικής υπεροχής του βασιλείου της Γουακάντα και της στολής του Black Panther."
    ],
    "source": "https://el.wikipedia.org/wiki/Captain_America",
    "locale": "el-GR",
    "tags": ["marvel", "captain-america", "superheroes", "vibranium"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_095",
    "text": "Στη νεανική σειρά του Mega «Singles», ποια ιδιόρρυθμη ηρωίδα υποδύθηκε η Μαρία Σολωμού αναλύοντας θεωρίες για τη ζωή;",
    "answers": ["Λίλα", "Μάρω", "Ράνια Κουκουμάφκα", "Περιστέρα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ράνια Κουκουμάφκα ήταν η αντικομφορμίστρια κεντρική ηρωίδα που μοιραζόταν με τους τηλεθεατές τις 'θεωρίες ζωής' και τους κανόνες της.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 3 σεζόν (2005–2008) σε σενάριο του Γιώργου Φειδά και σκηνοθεσία του Στέφανου Μπλάτσου.",
      "Χαρακτηριστικό στοιχείο της σειράς ήταν τα γραφικά κείμενα και οι σημειώσεις που εμφανίζονταν στην οθόνη."
    ],
    "source": "https://el.wikipedia.org/wiki/Singles_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "singles", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_096",
    "text": "Στην ταινία «Εξολοθρευτής 2: Μέρα Κρίσης» (1991), από τι υλικό αποτελείται το προηγμένο φονικό ρομπότ T-1000;",
    "answers": ["Από τιτάνιο", "Από ανθρακονήματα", "Από γραφένιο", "Από υγρό μέταλλο"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο T-1000 (Ρόμπερτ Πάτρικ) αποτελείται από 'μιμητικό πολυμεταλλικό κράμα' (υγρό μέταλλο), επιτρέποντάς του να αλλάζει μορφή και να αναγεννάται.",
    "funFacts": [
      "Τα ψηφιακά εφέ της ταινίας από την Industrial Light & Magic θεωρούνται ορόσημο στην ιστορία του κινηματογράφου CGI.",
      "Η ταινία κέρδισε 4 βραβεία Όσκαρ σε τεχνικές κατηγορίες, συμπεριλαμβανομένων των Οπτικών Εφέ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%95%CE%BE%CE%BF%CE%BB%CE%BF%CE%B8%CF%81%CE%B5%CF%85%CF%84%CE%AE%CF%82_2:_%CE%9C%CE%AD%CF%81%CE%B1_%CE%9A%CF%81%CE%AF%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["terminator", "sci-fi", "schwarzenegger", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_097",
    "text": "Στην κωμωδία «Η Αλίκη στο ναυτικό» (1961), τι είδους πολεμικό πλοίο είναι ο «Αετός» όπου τρυπώνει κρυφά η Αλίκη;",
    "answers": ["Αντιτορπιλικό", "Υποβρύχιο", "Αεροπλανοφόρο", "Ναρκαλιευτικό"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Αλίκη μεταμφιέζεται σε ναύτη και μπαίνει κρυφά στο ιστορικό αντιτορπιλικό 'Αετός' για να ακολουθήσει τον αγαπημένο της δόκιμο (Δημήτρη Παπαμιχαήλ).",
    "funFacts": [
      "Υπήρξε η πρώτη έγχρωμη ταινία της Φίνος Φιλμ, γυρισμένη σε σύστημα Agfacolor.",
      "Η ταινία εκπροσώπησε ανεπίσημα την Ελλάδα στο Φεστιβάλ των Καννών το 1961."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%91%CE%BB%CE%AF%CE%BA%CE%B7_%CF%83%CF%84%CE%BF_%CE%BD%CE%B1%CF%85%CF%84%CE%B9%CE%BA%CF%8C",
    "locale": "el-GR",
    "tags": ["greek-cinema", "aliki-vougiouklaki", "finos-film", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_098",
    "text": "Πώς ονομάζεται η σκοτεινή παράλληλη διάσταση όπου κατοικεί το Demogorgon στη σειρά «Stranger Things»;",
    "answers": ["Η Σκοτεινή Ζώνη", "Ο Ανάποδος Κόσμος (The Upside Down)", "Η Άβυσσος", "Ο Κάτω Κόσμος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το 'The Upside Down' είναι ένα σκοτεινό, παγωμένο και παρακμάζον αντίγραφο του ανθρώπινου κόσμου, γεμάτο τέρατα και τοξικά σπόρια.",
    "funFacts": [
      "Η πύλη για τη διάσταση αυτή άνοιξε κατά λάθος στο Εθνικό Εργαστήριο του Χόκινς κατά τη διάρκεια πειραμάτων τηλεπάθειας.",
      "Η σειρά των αδελφών Duffer αποτέλεσε μία από τις μεγαλύτερες επιτυχίες στην ιστορία του Netflix."
    ],
    "source": "https://el.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger-things", "upside-down", "netflix", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_099",
    "text": "Ποιο είναι το όνομα του ηφαιστείου στη Μόρντορ όπου πρέπει να καταστραφεί το Ένα Δαχτυλίδι στον «Άρχοντα των Δαχτυλιδιών»;",
    "answers": ["Όρος Έβερεστ", "Μαύρο Βουνό", "Βουνό του Χαμού (Mount Doom)", "Μοναχικό Βουνό"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Mount Doom (Οροντρούιν) είναι το ηφαίστειο στη γη της Μόρντορ όπου ο Σάουρον σφυρηλάτησε το Ένα Δαχτυλίδι και το μόνο μέρος όπου μπορεί να λιώσει.",
    "funFacts": [
      "Για τις σκηνές του Βουνού του Χαμού στις ταινίες χρησιμοποιήθηκε το ενεργό ηφαίστειο Mount Ngauruhoe στη Νέα Ζηλανδία.",
      "Η τριλογία κέρδισε συνολικά 17 βραβεία Όσκαρ από 30 υποψηφιότητες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%86%CF%81%CF%87%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CF%89%CE%BD_%CE%94%CE%B1%CF%87%CF%84%CF%85%CE%BB%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "mount-doom", "fantasy", "mordor"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_100",
    "text": "Στην κωμική σειρά «Σαββατογεννημένες» (Mega, 2003–2004), ποιο αναπάντεχο γεγονός ενώνει τις τρεις πρώην συζύγους του Σάββα;",
    "answers": ["Μια κληρονομιά αρχοντικού", "Ένα αεροπορικό δυστύχημα", "Ένα τηλεπαιχνίδι γνώσεων", "Το κέρδος του Τζόκερ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Σάββας κερδίζει 7,5 εκατομμύρια ευρώ στο Τζόκερ, αλλά παθαίνει αμνησία μετά από τροχαίο και οι τρεις πρώην σύζυγοι ψάχνουν το δελτίο.",
    "funFacts": [
      "Υπήρξε η πρώτη τηλεοπτική σειρά που έγραψε ο Γιώργος Καπουτζίδης, πριν γνωρίσει τεράστια επιτυχία με το 'Στο Παρά 5'.",
      "Τις τρεις συζύγους υποδύθηκαν η Ελένη Ράντου (Μπία), η Κατιάνα Μπαλανίκα (Καίτη) και η Ράνια Σχίζα (Σούλα)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%B2%CE%B2%CE%B1%CF%84%CE%BF%CE%B3%CE%B5%CE%BD%CE%BD%CE%B7%CE%BC%CE%AD%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "savvatogennimenes", "kapoutzidis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_101",
    "text": "Ποια παλαιοβοτανολόγος, την οποία υποδύεται η Λόρα Ντερν, πρωταγωνιστεί στην ταινία «Jurassic Park» (1993);",
    "answers": ["Έλι Σάτλερ", "Λούσι Πέβενσι", "Κλερ Ντίρινγκ", "Σάρα Χάρντινγκ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Dr. Ellie Sattler είναι η θαρραλέα παλαιοβοτανολόγος που επισκέπτεται το πάρκο μαζί με τον παλαιοντολόγο Dr. Alan Grant.",
    "funFacts": [
      "Η Λόρα Ντερν επανέλαβε τον ρόλο της στην ταινία 'Jurassic World: Dominion' το 2022.",
      "Η διάσημη σκηνή όπου φροντίζει έναν άρρωστο Τρικεράτοπα ήταν από τις πρώτες με πρακτικά animatronics που γυρίστηκαν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%85%CF%81%CE%AC%CF%83%CE%B9%CE%BA_%CE%A0%CE%B1%CF%81%CE%BA_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["jurassic-park", "spielberg", "dinosaurs", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_102",
    "text": "Στην κωμωδία «Της κακομοίρας», ποιος ηλικιωμένος μπακάλης θέλει να παντρευτεί τη νεαρή Φιφίκα παρά τη διαφορά ηλικίας;",
    "answers": ["Κυρ-Μανώλης", "Κυρ-Παντελής", "Κυρ-Στέλιος", "Κυρ-Θανάσης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο κυρ-Παντελής (Κώστας Δούκας) είναι ο ιδιοκτήτης του μπακάλικου που θέλει με προξενιό τη νεαρή Φιφίκα, ξεσηκώνοντας τα πειράγματα του Ζήκου.",
    "funFacts": [
      "Ο Κώστας Δούκας και ο Κώστας Χατζηχρήστος είχαν εξαιρετική χημεία και συνεργάστηκαν σε πολλές ακόμη κωμωδίες.",
      "Η ατάκα του Ζήκου 'Μα εσύ δεν είσαι άντρας, εσύ είσαι αρχαίο μνημείο!' προκάλεσε άφθονο γέλιο στις αίθουσες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%BA%CE%B1%CE%BA%CE%BF%CE%BC%CE%BF%CE%AF%CF%81%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "bakalogatos", "chatzichristos", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_103",
    "text": "Σε ποια εφημερίδα πουλά φωτογραφίες του Spider-Man ο Πίτερ Πάρκερ στον απαιτητικό εκδότη Τζ. Τζόνα Τζέιμσον;",
    "answers": ["Daily Planet", "Gotham Gazette", "The Daily Bugle", "New York Times"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Daily Bugle είναι η νεοϋορκέζικη εφημερίδα ταμπλόιντ που διευθύνει ο J. Jonah Jameson, ο οποίος μονίμως δυσφημεί τον Spider-Man.",
    "funFacts": [
      "Ο ηθοποιός J. K. Simmons απέσπασε διθυραμβικές κριτικές ενσαρκώνοντας τον Jameson στην τριλογία του Sam Raimi.",
      "Η αντίπαλη εφημερίδα στον κόσμο των κόμικς της DC όπου εργάζεται ο Clark Kent (Superman) είναι η Daily Planet."
    ],
    "source": "https://el.wikipedia.org/wiki/Spider-Man",
    "locale": "el-GR",
    "tags": ["spider-man", "marvel", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_104",
    "text": "Ποιο είναι το όνομα του μικροσκοπικού κόκκινου κινεζικού δράκου που συνοδεύει τη Μουλάν στην ταινία της Disney;",
    "answers": ["Κρίκι", "Χαν", "Σαν Γιου", "Μούσου (Mushu)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Mushu είναι ο έκπτωτος φύλακας-δράκος της οικογένειας Φα που προσπαθεί να βοηθήσει τη Μουλάν να δοξαστεί ώστε να ξανακερδίσει τη θέση του.",
    "funFacts": [
      "Στην αμερικανική εκδοχή τη φωνή του Μούσου δάνεισε ο Έντι Μέρφι.",
      "Στην ελληνική μεταγλώττιση ο Πέτρος Φιλιππίδης χάρισε τη φωνή του στον δημοφιλή δράκο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CF%85%CE%BB%CE%AC%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1998)",
    "locale": "el-GR",
    "tags": ["disney", "mulan", "animation", "mushu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_105",
    "text": "Ποιο θρυλικό ζευγάρι του ελληνικού κινηματογράφου παντρεύτηκε το 1965 και συμπρωταγωνίστησε σε ταινίες όπως «Το ξύλο βγήκε από τον παράδεισο»;",
    "answers": ["Ο Δημήτρης Παπαμιχαήλ και η Αλίκη Βουγιουκλάκη", "Ο Αλέκος Αλεξανδράκης and η Τζένη Καρέζη", "Ο Κώστας Καζάκος and η Τζένη Καρέζη", "Ο Ανδρέας Μπάρκουλης and η Μαίρη Χρονοπούλου"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Αλίκη Βουγιουκλάκη και ο Δημήτρης Παπαμιχαήλ υπήρξαν το διασημότερο καλλιτεχνικό ζευγάρι στην ιστορία του ελληνικού θεάτρου και κινηματογράφου.",
    "funFacts": [
      "Ο γάμος τους στους Δελφούς στις 18 Ιανουαρίου 1965 προκάλεσε κοσμοσυρροή και πρωτοφανές ενδιαφέρον από τον Τύπο.",
      "Γύρισαν μαζί δεκάδες ταινίες που έσπασαν τα ταμεία, ανάμεσά τους 'Η Αρχόντισσα κι ο Αλήτης' και 'Υπολοχαγός Νατάσσα'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AF%CE%BA%CE%B7_%CE%92%CE%BF%CF%85%CE%B3%CE%B9%CE%BF%CF%85%CE%BA%CE%BB%CE%AC%CE%BA%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-cinema", "papamichail", "vougiouklaki", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_106",
    "text": "Ποιο ιερό βιβλικό κειμήλιο αναζητά ο Ιντιάνα Τζόουνς στην πρώτη ταινία «Οι Κυνηγοί της Χαμένης Κιβωτού» (1981);",
    "answers": ["Το Άγιο Δισκοπότηρο", "Την Κιβωτό της Διαθήκης", "Το Χρυσόμαλλο Δέρας", "Τη Λόγχη του Πεπρωμένου"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Indiana Jones προσπαθεί να εντοπίσει την Κιβωτό της Διαθήκης (Ark of the Covenant) πριν πέσει στα χέρια των ναζιστικών δυνάμεων.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Στίβεν Σπίλμπεργκ σε ιστορία του Τζορτζ Λούκας και κέρδισε τέσσερα βραβεία Όσκαρ.",
      "Στην τρίτη ταινία της σειράς (1989), ο Ιντιάνα αναζητά ένα άλλο ιερό κειμήλιο, το Άγιο Δισκοπότηρο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%9A%CF%85%CE%BD%CE%B7%CE%B3%CE%BF%CE%AF_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CE%BC%CE%AD%CE%BD%CE%B7%CF%82_%CE%9A%CE%B9%CE%B2%CF%89%CF%84%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["indiana-jones", "spielberg", "adventure", "archaeology"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_107",
    "text": "Ποια είναι τα ονόματα των τριών αδελφών Σταμίρη στη δημοφιλή δραματική σειρά εποχής «Άγριες Μέλισσες» (ΑΝΤ1);",
    "answers": ["Μυρσίνη, Πηνελόπη και Θεοδοσία", "Βιολέτα, Ουρανία και Παγώνα", "Ελένη, Ασημίνα και Δρόσω", "Ανέτ, Ζωρζέτ και Σοφούλα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ελένη (Μαρία Κίτσου), η Ασημίνα (Έλλη Τρίγγου) και η Δρόσω (Δανάη Μιχαλάκη) είναι οι τρεις ορφανές αδελφές στο χωριό Διαφάνι.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 3 σεζόν (2019–2022) και αναβίωσε πανηγυρικά την ελληνική μυθοπλασία εποχής στην τηλεόραση.",
      "Το εντυπωσιακό σκηνικό του χωριού Διαφάνι χτίστηκε εξ ολοκλήρου από την αρχή στα στούντιο στα Σπάτα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CF%81%CE%B9%CE%B5%CF%82_%CE%9C%CE%AD%CE%BB%CE%B9%CF%83%CF%83%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "agries-melisses", "ant1", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_108",
    "text": "Ποιο είναι το όνομα του διαστημόπλοιου hovercraft στο οποίο κυβερνήτης είναι ο Μορφέας στην ταινία «The Matrix» (1999);",
    "answers": ["Μιλένιουμ Φάλκον", "Εντερπράιζ", "Νοστρόμο", "Ναβουχοδονόσορ (Nebuchadnezzar)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Nebuchadnezzar είναι το σκάφος της ανθρώπινης αντίστασης που κινείται στους υπονόμους της κατεστραμμένης Γης κάτω από τη μύτη των Μηχανών.",
    "funFacts": [
      "Το όνομα του σκάφους παραπέμπει στον βασιλιά Ναβουχοδονόσορα Β' της Βαβυλώνας, γνωστό από βιβλικά όνειρα που ζητούσε να του ερμηνεύσουν.",
      "Μια μεταλλική πλάκα στο εσωτερικό του σκάφους γράφει 'Mark III No. 11', υπονοώντας εδάφιο του Ευαγγελίου του Μάρκου."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Matrix",
    "locale": "el-GR",
    "tags": ["the-matrix", "sci-fi", "morpheus", "cyberpunk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_109",
    "text": "Ποιος αγαπημένος ηθοποιός είπε την αξέχαστη ατάκα «Έχω και κότερο, πάμε μια βόλτα;» στην ταινία «Κορίτσια για φίλημα» (1965);",
    "answers": ["Κώστας Βουτσάς", "Γιάννης Βογιατζής", "Ανδρέας Ντούζος", "Φαίδων Γεωργίτσης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Κώστας Βουτσάς υποδύθηκε τον Κώστα Καλιακούδα, χαρίζοντας μία από τις πιο διάσημες ατάκες στην ιστορία του ελληνικού κινηματογράφου.",
    "funFacts": [
      "Η ταινία της Φίνος Φιλμ γυρίστηκε στη Ρόδο και την Ύδρα και ήταν το πρώτο ελληνικό μιούζικαλ με στερεοφωνικό ήχο.",
      "Ο Βουτσάς διακρίθηκε για τη σωματική κωμωδία και τη μοναδική του ενέργεια που τον καθιέρωσε ως έναν από τους μεγαλύτερους κωμικούς της Ελλάδας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CF%81%CE%AF%CF%84%CF%83%CE%B9%CE%B1_%CE%B3%CE%B9%CE%B1_%CF%86%CE%AF%CE%BB%CE%B7%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "kostas-voutsas", "comedy", "dalianidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_110",
    "text": "Στην ταινία «Ο Ναυαγός» (Cast Away, 2000), τι μάρκα ήταν η μπάλα βόλεϊ που ο Τομ Χανκς ονόμασε και έκανε φίλο του;",
    "answers": ["Spalding", "Wilson", "Molten", "Mikasa"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Chuck Noland (Τομ Χανκς) ξεβράζεται σε ένα ερημονήσι με μια μπάλα βόλεϊ Wilson, πάνω στην οποία σχεδιάζει ένα πρόσωπο με το ίδιο του το αίμα.",
    "funFacts": [
      "Ο 'Wilson' κέρδισε τιμητικό βραβείο Broadcast Film Critics Association για το Καλύτερο Άψυχο Αντικείμενο.",
      "Μία από τις αυθεντικές μπάλες που χρησιμοποιήθηκαν στα γυρίσματα πουλήθηκε σε δημοπρασία το 2021 για περισσότερα από 300.000 δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9D%CE%B1%CF%85%CE%B1%CE%B3%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["cast-away", "tom-hanks", "wilson", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'easy', 1, questions)

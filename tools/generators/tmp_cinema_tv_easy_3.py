# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_easy_111",
    "text": "Ποιος σοφός μάγος καθοδηγεί τη Συντροφιά του Δαχτυλιδιού φορώντας γκρίζο και αργότερα λευκό μανδύα;",
    "answers": ["Γκάνταλφ", "Σάρουμαν", "Ράνταγκαστ", "Σάουρον"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Gandalf (Γκάνταλφ ο Γκρίζος και μετέπειτα Γκάνταλφ ο Λευκός) είναι ο μάγος που εμπνέει και οδηγεί την αντίσταση κατά του Σάουρον.",
    "funFacts": [
      "Τον εμβληματικό μάγο υποδύθηκε στην κινηματογραφική τριλογία ο σπουδαίος Βρετανός ηθοποιός Ίαν ΜακΚέλεν.",
      "Η διάσημη φράση του 'You shall not pass!' ('Δεν θα περάσεις!') προς τον Μπάλρογκ στα Ορυχεία της Μόρια έγινε θρυλική."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%AC%CE%BD%CF%84%CE%B1%CE%BB%CF%86",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "gandalf", "fantasy", "tolkien"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_112",
    "text": "Ποιος διακεκριμένος ηθοποιός είπε τη θρυλική ατάκα «Στάσου, μύγδαλα!» στην ταινία «Κορίτσια στον ήλιο» (1968);",
    "answers": ["Νίκος Κούρκουλος", "Γιάννης Βόγλης", "Φαίδων Γεωργίτσης", "Αλέκος Αλεξανδράκης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Γιάννης Βόγλης υποδύθηκε έναν βοσκό που προσπαθεί να προσφέρει αμύγδαλα σε μια Αγγλίδα τουρίστρια (Αν Λόμπεργκ).",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Βασίλη Γεωργιάδη και ήταν υποψήφια για Χρυσή Σφαίρα Καλύτερης Ξενόγλωσσης Ταινίας το 1969.",
      "Η μουσική επένδυση του Σταύρου Ξαρχάκου απέσπασε ειδικό βραβείο στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CF%81%CE%AF%CF%84%CF%83%CE%B9%CE%B1_%CF%83%CF%84%CE%BF%CE%BD_%CE%AE%CE%BB%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "giannis-voglis", "classics", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_113",
    "text": "Σε ποιο πράσινο πανίσχυρο τέρας μεταμορφώνεται ο επιστήμονας Μπρους Μπάνερ όταν εξοργίζεται στο σύμπαν της Marvel;",
    "answers": ["Iron Man", "Γουλβερίν", "Χαλκ (Hulk)", "Θορ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Dr. Bruce Banner εκτέθηκε σε ακτίνες γάμμα, με αποτέλεσμα να μεταμορφώνεται στον ασταμάτητο πράσινο γίγαντα Incredible Hulk όταν θυμώνει.",
    "funFacts": [
      "Στην πρώτη του εμφάνιση στα κόμικς το 1962, ο Χαλκ ήταν γκρι, αλλά άλλαξε σε πράσινο λόγω προβλημάτων εκτύπωσης.",
      "Στις ταινίες των Avengers τον ήρωα υποδύεται ο Μαρκ Ράφαλο."
    ],
    "source": "https://el.wikipedia.org/wiki/Hulk",
    "locale": "el-GR",
    "tags": ["marvel", "hulk", "superheroes", "avengers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_114",
    "text": "Από ποια μυστική αποβάθρα του σταθμού Κινγκς Κρος αναχωρεί το τρένο Χόγκουαρτς Εξπρές για τη σχολή μαγείας;",
    "answers": ["Πλατφόρμα 7 ½", "Πλατφόρμα 8 ¼", "Πλατφόρμα 10", "Πλατφόρμα 9 ¾"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Πλατφόρμα 9 ¾ (Platform 9 ¾) βρίσκεται ανάμεσα στις πλατφόρμες 9 και 10, και οι μαθητές περνούν διασχίζοντας έναν φαινομενικά συμπαγή τοίχο.",
    "funFacts": [
      "Στον πραγματικό σιδηροδρομικό σταθμό King's Cross του Λονδίνου έχει στηθεί μόνιμο σημείο φωτογράφισης με ένα καρότσι αποσκευών μισοχωμένο στον τοίχο.",
      "Το τρένο αναχωρεί πιστά κάθε χρόνο την 1η Σεπτεμβρίου στις 11 ακριβώς το πρωί."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CE%B9_%CE%A0%CF%8C%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["harry-potter", "platform-9-3-4", "hogwarts", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_115",
    "text": "Ποια αγαπημένη ηθοποιός πρωταγωνίστησε ως η νευρική και εργασιομανής Κατερίνα στην επιτυχημένη σειρά «Το Ρετιρέ» (Mega, 1990–1992);",
    "answers": ["Κατερίνα Γιουλάκη", "Έλντα Πανοπούλου", "Βίκυ Βανίτα", "Τζόυς Ευείδη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Κατερίνα Γιουλάκη ενσάρκωσε την Κατερίνα Σοφιανού, προϊσταμένη στην εταιρεία Cosmos Ε.Π.Ε., που προσπαθούσε να επιβιώσει ανάμεσα στα οικογενειακά και επαγγελματικά βάσανα.",
    "funFacts": [
      "Η σειρά γράφτηκε και σκηνοθετήθηκε από τον Γιάννη Δαλιανίδη και αποτέλεσε ένα από τα πρώτα μεγάλα χιτ του Mega Channel.",
      "Προβλήθηκε σε 84 επεισόδια και επαναπροβάλλεται σχεδόν κάθε καλοκαίρι για τρεις δεκαετίες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%A1%CE%B5%CF%84%CE%B9%CF%81%CE%AD",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-retire", "mega-channel", "dalianidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_116",
    "text": "Τι είδους ζώο είναι ο Ρεμί, ο ταλαντούχος επίδοξος σεφ στην ταινία της Pixar «Ο Ρατατούης» (Ratatouille, 2007);",
    "answers": ["Σκαντζόχοιρος", "Αρουραίος", "Σκίουρος", "Ρακούν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Remy είναι ένας νεαρός αρουραίος με εξαιρετικά ανεπτυγμένη όσφρηση και γεύση, που ονειρεύεται να γίνει κορυφαίος σεφ στο Παρίσι.",
    "funFacts": [
      "Η ταινία κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2008.",
      "Ο Ρεμί μαγειρεύει κατευθύνοντας τον αδέξιο νεαρό Λινγκουίνι τραβώντας του απαλά τα μαλλιά κάτω από το καπέλο του μάγειρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%A1%CE%B1%CF%84%CE%B1%CF%84%CE%BF%CF%8D%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["pixar", "ratatouille", "animation", "disney"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_117",
    "text": "Στην κωμωδία «Ο Παπατρέχας» (1966), ποιο επάγγελμα ασκεί ο Θανάσης Βέγγος τρέχοντας ασταμάτητα στην πολυκατοικία;",
    "answers": ["Ταχυδρόμος", "Ηλεκτρολόγος", "Θυρωρός", "Υδραυλικός"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Θανάσης Βέγγος υποδύεται τον θυρωρό Πολύδωρο Λαγό, που τρέχει συνεχώς για να εξυπηρετήσει τους ενοίκους και να παντρέψει τις έξι αδελφές του.",
    "funFacts": [
      "Η ταινία θεωρείται η επιτομή της εξαντλητικής σωματικής κωμωδίας του Βέγγου, καταγράφοντας ρεκόρ σε σκηνές τρεξίματος σε σκάλες.",
      "Το σενάριο υπέγραψε ο Γιώργος Λαζαρίδης και η σκηνοθεσία ήταν του Ερρίκου Θαλασσινού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%A0%CE%B1%CF%80%CE%B1%CF%84%CF%81%CE%AD%CF%87%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "thanasis-veggos", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_118",
    "text": "Ποιος κατασκεύασε το χρυσό ανδροειδές πρωτοκόλλου C-3PO όταν ήταν ακόμα μικρό αγόρι στον πλανήτη Τατουίν;",
    "answers": ["Ο Λουκ Σκαϊγουόκερ", "Ο Χαν Σόλο", "Ο Όμπι-Ουάν Κενόμπι", "Ο Άνακιν Σκαϊγουόκερ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Anakin Skywalker συναρμολόγησε τον C-3PO από παλιοσίδερα για να βοηθά τη μητέρα του Shmi στις δουλειές του σπιτιού.",
    "funFacts": [
      "Τον C-3PO ενσάρκωσε μέσα στη μεταλλική στολή ο ηθοποιός Anthony Daniels σε όλες τις βασικές ταινίες της σειράς.",
      "Ο C-3PO ισχυρίζεται ότι γνωρίζει άπταιστα περισσότερες από έξι εκατομμύρια μορφές επικοινωνίας στο σύμπαν."
    ],
    "source": "https://el.wikipedia.org/wiki/C-3PO",
    "locale": "el-GR",
    "tags": ["star-wars", "c-3po", "anakin", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_119",
    "text": "Ποιος κομψός ζεν πρεμιέ του ελληνικού κινηματογράφου πρωταγωνίστησε ως ο γοητευτικός υποδιευθυντής στην ταινία «Δεσποινίς Διευθυντής» (1964);",
    "answers": ["Αλέκος Αλεξανδράκης", "Δημήτρης Παπαμιχαήλ", "Ανδρέας Μπάρκουλης", "Νίκος Κούρκουλος"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Αλέκος Αλεξανδράκης υποδύθηκε τον Αλέκο Σαμιωτάκη, τον υπάλληλο που γοητεύει τη νέα και αυστηρή διευθύντριά του (Τζένη Καρέζη).",
    "funFacts": [
      "Ο Αλεξανδράκης υπήρξε ένας από τους πιο ταλαντούχους και ευγενείς πρωταγωνιστές του ελληνικού θεάτρου και σινεμά.",
      "Η ταινία έκοψε πάνω από 402.000 εισιτήρια κατά την πρώτη της προβολή, σημειώνοντας τεράστια εμπορική επιτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B5%CF%83%CF%80%CE%BF%CE%B9%CE%BD%CE%AF%CF%82_%CE%B4%CE%B9%CE%B5%CF%85%CE%B8%CF%85%CE%BD%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "alexandrakis", "karezi", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_120",
    "text": "Ποιος μυστηριώδης ηγέτης της αντίστασης προσφέρει στον Νίο την επιλογή ανάμεσα στο μπλε και το κόκκινο χάπι στο «The Matrix»;",
    "answers": ["Ο Σάιφερ", "Ο Μορφέας", "Ο Πράκτορας Σμιθ", "Ο Τανκ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Morpheus (τον οποίο υποδύεται ο Laurence Fishburne) προσφέρει στον Neo τη δυνατότητα να μάθει τη σκληρή αλήθεια για την πραγματικότητα.",
    "funFacts": [
      "Το κόκκινο χάπι συμβολίζει την αφύπνιση στην αληθινή πραγματικότητα, ενώ το μπλε την επιστροφή στην άνετη άγνοια της ψευδαίσθησης.",
      "Η ταινία των αδελφών Wachowski κέρδισε και τα τέσσερα Όσκαρ για τα οποία προτάθηκε το 2000."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Matrix",
    "locale": "el-GR",
    "tags": ["the-matrix", "morpheus", "sci-fi", "neo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_121",
    "text": "Ποιος πρωταγωνιστής υποδύθηκε τον πατέρα τριών αγοριών Διονύση Μαυροτσούκαλο στην κωμική σειρά «Ευτυχισμένοι Μαζί» (Mega);",
    "answers": ["Παύλος Χαϊκάλης", "Σάκης Μπουλάς", "Γιάννης Μπέζος", "Πέτρος Φιλιππίδης"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Γιάννης Μπέζος ενσάρκωσε τον ταβερνιάρη Διονύση που ξαναπαντρεύεται την παλιά του αγάπη Ελένη (Κατερίνα Λέχου), ενώνοντας δύο εντελώς διαφορετικές οικογένειες.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 2 σεζόν (2007–2009) γνωρίζοντας τεράστια τηλεθέαση που άγγιζε το 50%.",
      "Βασίστηκε στην ισπανική επιτυχημένη σειρά 'Los Serrano'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CF%84%CF%85%CF%87%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF%CE%B9_%CE%9C%CE%B1%CE%B6%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "eftyxismenoi-mazi", "giannis-bezos", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_122",
    "text": "Ποιο είναι το όνομα της παιδικής φίλης και μετέπειτα συντρόφου του Σίμπα στον «Βασιλιά των Λιονταριών»;",
    "answers": ["Σαράμπι", "Κιάρα", "Σενζί", "Νάλα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Nala είναι η πιστή παιδική φίλη του Σίμπα που τον βρίσκει στην εξορία και τον πείθει να επιστρέψει για να διεκδικήσει το βασίλειό του.",
    "funFacts": [
      "Στο live-action ριμέικ του 2019, τη φωνή της Νάλα δάνεισε η παγκόσμια σούπερ σταρ της ποπ Beyoncé.",
      "Η σκηνή της επανένωσής τους συνοδεύεται από το βραβευμένο με Όσκαρ ερωτικό τραγούδι 'Can You Feel the Love Tonight'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%B9%CE%AC%CF%82_%CF%84%CF%89%CE%BD_%CE%9B%CE%B9%CE%BF%CE%BD%CF%84%CE%B1%CF%81%CE%B9%CF%8E%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1994)",
    "locale": "el-GR",
    "tags": ["disney", "the-lion-king", "nala", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_123",
    "text": "Ποιος σταρ του Χόλιγουντ υποδύθηκε τον ριψοκίνδυνο πιλότο μαχητικών αεροσκαφών Μάβερικ στην ταινία «Top Gun» (1986);",
    "answers": ["Τομ Κρουζ", "Βαλ Κίλμερ", "Τσάρλι Σιν", "Κέβιν Μπέικον"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Tom Cruise πρωταγωνίστησε ως ο νεαρός αεροπόρος του αμερικανικού ναυτικού Pete 'Maverick' Mitchell στη σχολή πιλότων μαχητικών.",
    "funFacts": [
      "Η ταινία προκάλεσε θεαματική αύξηση στις αιτήσεις κατάταξης στο Ναυτικό των ΗΠΑ μετά την προβολή της.",
      "Η συνέχεια 'Top Gun: Maverick' (2022) ξεπέρασε τα 1,4 δισεκατομμύρια δολάρια στο παγκόσμιο box office."
    ],
    "source": "https://el.wikipedia.org/wiki/Top_Gun",
    "locale": "el-GR",
    "tags": ["top-gun", "tom-cruise", "action", "aviation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_124",
    "text": "Σε ποιο κυκλαδίτικο νησί γυρίστηκε η βραβευμένη ταινία της Φίνος Φιλμ «Μανταλένα» (1960) με την Αλίκη Βουγιουκλάκη;",
    "answers": ["Μύκονος", "Αντίπαρος", "Σαντορίνη", "Νάξος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η 'Μανταλένα' γυρίστηκε εξ ολοκλήρου στην Αντίπαρο, προβάλλοντας τα αυθεντικά τοπία και τη ζωή των νησιωτών της δεκαετίας του 1960.",
    "funFacts": [
      "Η Αλίκη Βουγιουκλάκη κέρδισε το Βραβείο Α' Γυναικείου Ρόλου στην 1η Εβδομάδα Ελληνικού Κινηματογράφου στη Θεσσαλονίκη το 1960.",
      "Η ταινία εκπροσώπησε την Ελλάδα στο διαγωνιστικό τμήμα του Φεστιβάλ των Καννών το 1961."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%84%CE%B1%CE%BB%CE%AD%CE%BD%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "madalena", "antiparos", "vougiouklaki"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_125",
    "text": "Ποιο είναι το όνομα του μεγαλύτερου και πιο επιθετικού μαύρου δράκου της Ντενέρις Ταργκάριεν στο «Game of Thrones»;",
    "answers": ["Ρέγκαλ", "Βισέριον", "Ντρόγκον", "Βάγκαρ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Drogon είναι ο μαύρος δράκος με κόκκινες λεπτομέρειες που η Daenerys ονόμασε προς τιμήν του εκλιπόντος συζύγου της, Khal Drogo.",
    "funFacts": [
      "Ο Ντρόγκον ήταν ο προσωπικός δράκος τον οποίο ίππευε η ίδια η Daenerys Targaryen στις μάχες.",
      "Στην τελευταία σεζόν έλιωσε με την καυτή ανάσα του τον Σιδερένιο Θρόνο πριν πετάξει μακριά."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_of_Thrones",
    "locale": "el-GR",
    "tags": ["game-of-thrones", "drogon", "daenerys", "dragons"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_126",
    "text": "Στη σειρά «Κωνσταντίνου και Ελένης», ποιο επάγγελμα προσπαθούσε μάταια να ασκήσει η Πέγκυ Καρρά (Ελένη Ράντου);",
    "answers": ["Δημοσιογράφος", "Τραγουδίστρια", "Μοντέλο", "Ηθοποιός"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Πέγκυ Καρρά δήλωνε 'ηθοποιός' παρότι έπαιζε μόνο μικρούς ρόλους ως κομπάρσος, επαναλαμβάνοντας συνεχώς μονολόγους από το θεατρικό 'Αντιγόνη'.",
    "funFacts": [
      "Ο μόνιμος σύντροφός της στη σειρά ήταν ο οινοχόος Μάνθος Φουστάνος (Βασίλης Κούκουρας).",
      "Το σκυλάκι της Πέγκυς στη σειρά ονομαζόταν 'Τζοβάνα'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "konstantinou-kai-elenis", "comedy", "peggy-karra"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_127",
    "text": "Ποια μαγική νταντά προσγειώνεται με την ιπτάμενη ομπρέλα της στην κλασική μουσική ταινία της Disney (1964);",
    "answers": ["Μαίρη Πόπινς", "Νανί ΜακΦί", "Ματίλντα", "Έμμα Τόμσον"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Mary Poppins (Τζούλι Άντριους) φτάνει με τον ανατολικό άνεμο για να φροντίσει τα παιδιά της οικογένειας Μπανκς στο Λονδίνο.",
    "funFacts": [
      "Η ταινία προτάθηκε για 13 βραβεία Όσκαρ και κέρδισε 5, ανάμεσά τους το Όσκαρ Α' Γυναικείου Ρόλου για την Τζούλι Άντριους.",
      "Συνδύασε με πρωτοποριακό τρόπο ζωντανούς ηθοποιούς με κινούμενα σχέδια στη σκηνή του πικνίκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%AF%CF%81%CE%B7_%CE%A0%CF%8C%CF%80%CE%B9%CE%BD%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["disney", "mary-poppins", "musical", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_128",
    "text": "Στην ταινία «Η Αρχόντισσα κι ο Αλήτης» (1968), ποιο ανδρικό όνομα χρησιμοποιεί η Αλίκη Βουγιουκλάκη όταν ντύνεται αγόρι;",
    "answers": ["Μήτσος", "Πίπης", "Φώτης", "Νίκος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η πλούσια Ρένα το σκάει από το σπίτι της για να γλιτώσει από έναν ανεπιθύμητο γάμο, κουρεύεται και παριστάνει το αγόρι με το όνομα 'Πίπης'.",
    "funFacts": [
      "Υπήρξε η πιο εμπορική ταινία της σεζόν 1968–1969 κόβοντας 750.380 εισιτήρια στην πρώτη της προβολή.",
      "Το χαρακτηριστικό τραγούδι 'Στον ήλιο του μεσημεριού' έγινε μία από τις πιο γνωστές επιτυχίες της ταινίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B1%CF%81%CF%87%CF%8C%CE%BD%CF%84%CE%B9%CF%83%CF%83%CE%B1_%CE%BA%CE%B9_%CE%BF_%CE%B1%CE%BB%CE%AE%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "aliki-vougiouklaki", "pipis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_129",
    "text": "Ποιο μυθικό γιγάντιο θαλάσσιο τέρας ελέγχει ο Ντέιβι Τζόουνς στους «Πειρατές της Καραϊβικής» για να βυθίζει πλοία;",
    "answers": ["Λεβιάθαν", "Μεγαλόδοντας", "Κράκεν", "Σκύλλα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Kraken είναι το τερατώδες κεφαλόποδο πλάσμα των ωκεανών που υπακούει στις εντολές του καπετάνιου του 'Ιπτάμενου Ολλανδού'.",
    "funFacts": [
      "Στη δεύτερη ταινία ('Το Σεντούκι του Νεκρού'), το Κράκεν καταστρέφει το 'Μαύρο Μαργαριτάρι' και παρασύρει τον Τζακ Σπάροου στον βυθό.",
      "Η ταινία κέρδισε το Όσκαρ Καλύτερων Οπτικών Εφέ το 2007 για την ψηφιακή δημιουργία του τέρατος και του πληρώματος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%A0%CE%B5%CE%B9%CF%81%CE%B1%CF%84%CE%AD%CF%82_%CF%84%CE%B7%CF%82_%CE%9A%CE%B1%CF%81%CE%B1%CF%8A%CE%B2%CE%B9%CE%BA%CE%AE%CF%82:_%CE%A4%CE%BF_%CE%A3%CE%B5%CE%BD%CF%84%CE%BF%CF%8D%CE%BA%CE%B9_%CF%84%CE%BF%CF%85_%CE%9D%CE%B5%CE%BA%CF%81%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["pirates-of-the-caribbean", "kraken", "disney", "monsters"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_130",
    "text": "Στην κωμωδία «Ο φίλος μου ο Λευτεράκης» (1963), ποιος ηθοποιός υποδύεται τον σύζυγο που εφευρίσκει έναν ανύπαρκτο φίλο για άλλοθι;",
    "answers": ["Κώστας Βουτσάς", "Γιώργος Πάντζας", "Γιάννης Γκιωνάκης", "Ντίνος Ηλιόπουλος"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ντίνος Ηλιόπουλος παίζει τον Θόδωρο Καρατουμπούρα, που χρησιμοποιεί έναν φανταστικό φίλο ονόματι 'Λευτεράκη' για να καλύπτει τις εξωσυζυγικές του αταξίες.",
    "funFacts": [
      "Τον υποτιθέμενο 'Λευτεράκη' που εμφανίζεται ξαφνικά ζωντανός υποδύθηκε απολαυστικά ο Κώστας Βουτσάς.",
      "Η ταινία σκηνοθετήθηκε από τον Αλέκο Σακελλάριο και θεωρείται από τις πιο καλογραμμένες κωμωδίες παρεξηγήσεων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CF%86%CE%AF%CE%BB%CE%BF%CF%82_%CE%BC%CE%BF%CF%85_%CE%BF_%CE%9B%CE%B5%CF%85%CF%84%CE%B5%CF%81%CE%AC%CE%BA%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dinos-iliopoulos", "voutsas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_131",
    "text": "Σε ποια διάσημη διεύθυνση του Λονδίνου κατοικεί ο ιδιωτικός ντετέκτιβ Σέρλοκ Χολμς;",
    "answers": ["221B Baker Street", "10 Downing Street", "4 Privet Drive", "742 Evergreen Terrace"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η διεύθυνση 221B Baker Street είναι η θρυλική κατοικία και γραφείο του Sherlock Holmes και του Dr. Watson στις ιστορίες του Arthur Conan Doyle.",
    "funFacts": [
      "Στην πραγματική Baker Street του Λονδίνου λειτουργεί σήμερα επίσημο Μουσείο Σέρλοκ Χολμς.",
      "Όταν γράφτηκαν οι ιστορίες, οι αριθμοί στην Baker Street δεν έφταναν ως το 221, καθώς ο δρόμος ήταν μικρότερος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%AD%CF%81%CE%BB%CE%BF%CE%BA_%CE%A7%CE%BF%CE%BB%CE%BC%CF%82",
    "locale": "el-GR",
    "tags": ["sherlock-holmes", "london", "detective", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_132",
    "text": "Στην κωμική σειρά «Είσαι το ταίρι μου», ποιος χαρακτήρας ήταν ο καλοκάγαθος Ελληνοαυστραλός φίλος που ερωτεύτηκε τη Στέλλα;",
    "answers": ["Ο Σωτήρης", "Ο Γρηγόρης", "Ο Παναγιώτης", "Ο Λυκούργος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Βασίλης Χαραλαμπόπουλος υποδύθηκε τον Γρηγόρη, τον αφελή και ευαίσθητο φίλο από τη Μελβούρνη που προσπαθούσε να καταλάβει τι συμβαίνει.",
    "funFacts": [
      "Ο ρόλος αυτός χάρισε τεράστια αναγνωρισιμότητα στον Βασίλη Χαραλαμπόπουλο.",
      "Η σειρά θεωρείται μία από τις πιο ευρηματικές κωμωδίες στην ιστορία του Mega Channel."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["greek-tv", "eisai-to-tairi-mou", "charalampopoulos", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_133",
    "text": "Ποιο δηλητηριασμένο φρούτο προσφέρει η Κακιά Βασίλισσα στη Χιονάτη στην κλασική ταινία κινουμένων σχεδίων (1937);",
    "answers": ["Ένα ρόδι", "Ένα σύκο", "Ένα κόκκινο μήλο", "Ένα αχλάδι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η μεταμφιεσμένη σε γριά μάγισσα Βασίλισσα ξεγελά τη Χιονάτη και της δίνει να δαγκώσει ένα δηλητηριασμένο μήλο που προκαλεί ύπνο παρόμοιο με θάνατο.",
    "funFacts": [
      "Η ταινία 'Η Χιονάτη και οι Επτά Νάνοι' ήταν η πρώτη μεγάλου μήκους έγχρωμη ταινία κινουμένων σχεδίων στην παγκόσμια ιστορία.",
      "Ο Γουόλτ Ντίσνεϊ βραβεύτηκε με ένα κανονικό Όσκαρ και επτά μικροσκοπικά αγαλματίδια για το καλλιτεχνικό του επίτευγμα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A7%CE%B9%CE%BF%CE%BD%CE%AC%CF%84%CE%B7_%CE%BA%CE%B1%CE%B9_%CE%BF%CE%B9_%CE%B5%CF%80%CF%84%CE%AC_%CE%BD%CE%AC%CE%BD%CE%BF%CE%B9_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1937)",
    "locale": "el-GR",
    "tags": ["disney", "snow-white", "animation", "fairy-tale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_134",
    "text": "Ποιος κορυφαίος ηθοποιός υποδύθηκε τον μισογύνη καθηγητή Λεωνίδα Πετρόχειλο στην ταινία «Ο στρίγγλος που έγινε αρνάκι» (1967);",
    "answers": ["Διονύσης Παπαγιαννόπουλος", "Κώστας Χατζηχρήστος", "Μίμης Φωτόπουλος", "Λάμπρος Κωνσταντάρας"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Λάμπρος Κωνσταντάρας πρωταγωνιστεί ως αυστηρός χήρος διευθυντής σχολής με τρεις ατίθασους γιους, που αλλάζει εντελώς χαρακτήρα όταν γνωρίζει τη Μαίρη (Μάρω Κοντού).",
    "funFacts": [
      "Η ταινία περιλαμβάνει τη γνωστή ατάκα 'Μπούρδας! Ένας είναι ο Μπούρδας!' που αναφωνούσε ο πρωταγωνιστής.",
      "Βασίστηκε στο θεατρικό έργο των Αλέκου Σακελλάριου και Χρήστου Γιαννακόπουλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CF%83%CF%84%CF%81%CE%AF%CE%B3%CE%B3%CE%BB%CE%BF%CF%82_%CF%80%CE%BF%CF%85_%CE%AD%CE%B3%CE%B9%CE%BD%CE%B5_%CE%B1%CF%81%CE%BD%CE%AC%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-cinema", "konstantaras", "maro-kontou", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_135",
    "text": "Πώς ονομάζεται το θρυλικό διαστημόπλοιο του Χαν Σόλο και του Τσουμπάκα στο «Star Wars»;",
    "answers": ["Μιλένιουμ Φάλκον (Millennium Falcon)", "Έντερπραϊζ", "Ντισκάβερι", "Αστρικός Καταστροφέας"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Millennium Falcon είναι ένα τροποποιημένο ελαφρύ φορτηγό σκάφος YT-1300, διάσημο για την ταχύτητα και τις παράτολμες πτήσεις του.",
    "funFacts": [
      "Σύμφωνα με τον Χαν Σόλο, είναι το σκάφος που έκανε τη διαδρομή Kessel Run σε λιγότερο από 12 παρσέκ.",
      "Ο Τζορτζ Λούκας εμπνεύστηκε το αρχικό σχήμα του σκάφους παρατηρώντας ένα χάμπουργκερ με μια ελιά καρφωμένη στο πλάι."
    ],
    "source": "https://el.wikipedia.org/wiki/Star_Wars",
    "locale": "el-GR",
    "tags": ["star-wars", "millennium-falcon", "han-solo", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_136",
    "text": "Στη σειρά «Δύο Ξένοι» (Mega, 1997–1999), ποια ήταν η ιδιότητα και το επάγγελμα του Κωνσταντίνου Μαρκορά (Νίκος Σεργιανόπουλος);",
    "answers": ["Δικηγόρος", "Σκηνοθέτης θεάτρου και καθηγητής υποκριτικής", "Παρουσιαστής ειδήσεων", "Γιατρός χειρουργός"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Κωνσταντίνος Μαρκοράς ήταν ένας καλλιεργημένος σκηνοθέτης και καθηγητής δραματικής σχολής που ερωτεύτηκε την ξανθιά παρουσιάστρια Μαρίνα Κουντουράτου (Εβελίνα Παπούλια).",
    "funFacts": [
      "Η σειρά των Αλέξανδρου Ρήγα και Δημήτρη Αποστόλου σημείωσε ρεκόρ τηλεθέασης στα τέλη της δεκαετίας του 1990.",
      "Ο χαρακτήρας της Ντένης Μαρκορά, μητέρας του Κωνσταντίνου, ερμηνεύτηκε ανεπανάληπτα από τη Ντίνα Κώνστα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CF%8D%CE%BF_%CE%9E%CE%AD%CE%BD%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "dyo-xenoi", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_137",
    "text": "Ποια διάσημη μάρκα αθλητικών παπουτσιών χάρισε η Τζένη στον Φόρεστ Γκαμπ, με τα οποία έτρεξε σε ολόκληρη την Αμερική;",
    "answers": ["Adidas", "Puma", "Nike", "Converse"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Jenny του έκανε δώρο ένα ζευγάρι λευκά Nike Cortez με κόκκινο swoosh, με τα οποία ο Φόρεστ ξεκίνησε το τριετές τρέξιμό του από ακτή σε ακτή.",
    "funFacts": [
      "Το μοντέλο Nike Cortez γνώρισε τεράστια αύξηση πωλήσεων μετά την κυκλοφορία της ταινίας το 1994.",
      "Η ατάκα 'Run, Forrest, run!' αποτελεί μία από τις δημοφιλέστερες στην ιστορία του κινηματογράφου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%8C%CF%81%CE%B5%CF%83%CF%84_%CE%93%CE%BA%CE%B1%CE%BC%CF%80",
    "locale": "el-GR",
    "tags": ["forrest-gump", "nike", "tom-hanks", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_138",
    "text": "Στην κλασική ταινία «Λατέρνα, φτώχεια και φιλότιμο» (1955), ποιο παραδοσιακό μουσικό όργανο κουβαλούν στον δρόμο ο Αυλωνίτης και ο Φωτόπουλος;",
    "answers": ["Ακορντεόν", "Μπουζούκι", "Βιολί", "Λατέρνα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Παυλάρας και ο Πετράκης είναι δύο φτωχοί αλλά φιλότιμοι λατερνατζήδες που περιπλανώνται στα χωριά παίζοντας τη λατέρνα τους.",
    "funFacts": [
      "Υπήρξε η πρώτη ταινία στην ιστορία του ελληνικού κινηματογράφου που απέκτησε σίκουελ, το 'Λατέρνα, φτώχεια και γαρύφαλλο' (1957).",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο σε παραγωγή της Φίνος Φιλμ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B1%CF%84%CE%AD%CF%81%CE%BD%CE%B1,_%CF%86%CF%84%CF%8e%CF%87%CE%B5%CE%B9%CE%B1_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "laterna", "avlonitis", "fotopoulos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_139",
    "text": "Στην εμβληματική σκηνή του «Jurassic Park» (1993), ποιο υγρό μέσα σε ένα ποτήρι κάνει κυματισμούς από τα βήματα του T-Rex;",
    "answers": ["Νερό", "Καφές", "Γάλα", "Αναψυκτικό"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Οι ομόκεντροι κυματισμοί στην επιφάνεια του νερού σε ένα πλαστικό ποτήρι στο ταμπλό του τζιπ προειδοποιούν για την άφιξη του Τυραννόσαυρου Ρεξ.",
    "funFacts": [
      "Ο Σπίλμπεργκ εμπνεύστηκε το εφέ βλέποντας τον καθρέφτη του αυτοκινήτου του να δονείται από τη δυνατή μουσική.",
      "Για να επιτύχουν τον κυματισμό στα γυρίσματα, τοποθέτησαν μια χορδή κιθάρας κάτω από το ταμπλό και την τράβηξαν ρυθμικά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%85%CF%81%CE%AC%CF%83%CE%B9%CE%BA_%CE%A0%CE%B1%CF%81%CE%BA_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["jurassic-park", "t-rex", "spielberg", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_140",
    "text": "Στη μαύρη κωμωδία του ΑΝΤ1 «Εγκλήματα», ποιο ήταν το επάγγελμα του Αλέκου Παπαδήμα (Κώστας Κόκλας);",
    "answers": ["Οδοντίατρος", "Κρεοπώλης", "Φαρμακοποιός", "Υδραυλικός"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Αλέκος διατηρούσε συνοικιακό κρεοπωλείο και διατηρούσε παράνομο δεσμό με τη Φλώρα (Υρώ Μανέ/Βασιλική Ανδρίτσου), εξοργίζοντας τη σύζυγό του Σωσώ.",
    "funFacts": [
      "Το χασάπικο του Αλέκου αποτέλεσε το βασικό σκηνικό πολλών ξεκαρδιστικών επεισοδίων της σειράς.",
      "Η σειρά προβλήθηκε για δύο σεζόν σημειώνοντας τεράστια επιτυχία στο νεανικό κυρίως κοινό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "egklimata", "ant1", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_141",
    "text": "Ποιο ξωτικό με απαράμιλλη τοξοβολία εκπροσωπεί τη φυλή του στη Συντροφιά του Δαχτυλιδιού;",
    "answers": ["Έλροντ", "Θράντουιλ", "Λέγκολας", "Κέλεμπορν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Legolas Greenleaf είναι ο πρίγκιπας του Μέρκγουντ που εντυπωσιάζει με την ταχύτητα και τις ακροβατικές του ικανότητες στο τόξο.",
    "funFacts": [
      "Τον ρόλο του Λέγκολας ενσάρκωσε ο Βρετανός ηθοποιός Ορλάντο Μπλουμ, ρόλος που τον έκανε παγκόσμιο αστέρα.",
      "Η ανταγωνιστική αλλά βαθιά φιλία του με τον νάνο Γκίμλι αποτελεί ένα από τα πιο αγαπημένα στοιχεία της ιστορίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AD%CE%B3%CE%BA%CE%BF%CE%BB%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "legolas", "orlando-bloom", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_142",
    "text": "Ποιος γοητευτικός ηθοποιός υποδύθηκε τον υποψήφιο βουλευτή Νίκο Μαντά στην κωμωδία «Τζένη Τζένη» (1966);",
    "answers": ["Λάμπρος Κωνσταντάρας", "Δημήτρης Παπαμιχαήλ", "Γιάννης Φέρτης", "Ανδρέας Μπάρκουλης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ανδρέας Μπάρκουλης υποδύθηκε τον ανιψιό του εφοπλιστή Κασσανδρή που κάνει λευκό γάμο με την Τζένη Σκούταρη (Τζένη Καρέζη) για να εκλεγεί βουλευτής.",
    "funFacts": [
      "Η ταινία γυρίστηκε στο πανέμορφο νησί των Σπετσών, προβάλλοντας τα γραφικά σοκάκια και το λιμάνι.",
      "Η φράση της εποχής 'Κορίτσια, ο Μπάρκουλης!' αποτυπώνει την τεράστια απήχηση που είχε ο ηθοποιός στο γυναικείο κοινό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CE%BD%CE%B7_%CE%A4%CE%B6%CE%AD%CE%BD%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-cinema", "barkoulis", "karezi", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_143",
    "text": "Τι συμβαίνει στη μύτη της ξύλινης μαριονέτας Πινόκιο κάθε φορά που λέει ψέματα στην ταινία της Disney (1940);",
    "answers": ["Μεγαλώνει σε μήκος", "Αλλάζει χρώμα σε κόκκινο", "Βγάζει καπνό", "Μικραίνει και εξαφανίζεται"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Κάθε φορά που ο Pinocchio λέει ψέματα, η μύτη του μακραίνει εντυπωσιακά, ενώ βγάζει ακόμη και φύλλα και κλαδιά.",
    "funFacts": [
      "Η ταινία κέρδισε δύο βραβεία Όσκαρ: Καλύτερης Πρωτότυπης Μουσικής και Καλύτερου Τραγουδιού για το 'When You Wish Upon a Star'.",
      "Ο πιστός οδηγός συνείδησης του Πινόκιο στην ταινία είναι ο Τζίμινι Κρίκετ (Jiminy Cricket)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CE%BD%CF%8C%CE%BA%CE%B9%CE%BF_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1940)",
    "locale": "el-GR",
    "tags": ["disney", "pinocchio", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_144",
    "text": "Στη δημοφιλή σειρά κινουμένων σχεδίων «Scooby-Doo», σε ποια φυλή σκύλων ανήκει ο αξιαγάπητος Σκούμπι;",
    "answers": ["Γερμανικός Ποιμενικός", "Μεγάλος Δανός (Μολοσσός)", "Γκόλντεν Ριτρίβερ", "Μπιγκλ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Scooby-Doo είναι ένας μεγαλόσωμος Μεγάλος Δανός (Great Dane) που λατρεύει το φαγητό και τα σνακ (Scooby Snacks) και τρομάζει εύκολα με τα φαντάσματα.",
    "funFacts": [
      "Ο σχεδιαστής Iwao Takamoto συμβουλεύτηκε έναν εκτροφέα Μεγάλων Δανών και σχεδίασε τον Σκούμπι με τα ακριβώς αντίθετα χαρακτηριστικά από τα πρότυπα της ράτσας.",
      "Το όνομα 'Scooby-Doo' εμπνεύστηκε από τα φωνητικά του Frank Sinatra στο τέλος του τραγουδιού 'Strangers in the Night'."
    ],
    "source": "https://el.wikipedia.org/wiki/Scooby-Doo",
    "locale": "el-GR",
    "tags": ["scooby-doo", "animation", "cartoons", "dogs"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_145",
    "text": "Στην ταινία «Επιστροφή στο Μέλλον II» (1989), ποιο αντικείμενο χρησιμοποιεί ο Μάρτι ΜακΦλάι για να αιωρείται στον αέρα;",
    "answers": ["Ιπτάμενες μπότες", "Μαγικό χαλί", "Ιπτάμενο σκέιτμπορντ (Hoverboard)", "Μίνι τζετ-πακ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Marty McFly δανείζεται ένα φουτουριστικό Hoverboard της Mattel που αιωρείται πάνω από το έδαφος χρησιμοποιώντας μαγνητική απώθηση.",
    "funFacts": [
      "Το hoverboard δεν λειτουργούσε πάνω από το νερό εκτός αν ο αναβάτης είχε κινητήρια δύναμη.",
      "Μετά την πρεμιέρα της ταινίας δημιουργήθηκε αστικός μύθος ότι τα hoverboards υπήρχαν στ' αλήθεια αλλά δεν κυκλοφόρησαν για λόγους ασφαλείας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%83%CF%84%CF%81%CE%BF%CF%86%CE%AE_%CF%83%CF%84%CE%BF_%CE%9C%CE%AD%CE%BB%CE%BB%CE%BF%CE%BD_2",
    "locale": "el-GR",
    "tags": ["back-to-the-future", "hoverboard", "marty-mcfly", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_146",
    "text": "Στην κωμωδία «Υπάρχει και φιλότιμο», ποια χειρονομία αγανάκτησης δέχεται επανειλημμένα ο υπουργός Μαυρογιαλούρος στο πρόσωπο;",
    "answers": ["Σφαλιάρα", "Γροθιά", "Τσίμπημα", "Μούτζα (φάσκελο)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Οι εξαπατημένοι χωρικοί μουντζώνουν επανειλημμένα τον υπουργό, ο οποίος αργότερα αναφωνεί απορημένος τη φράση 'Φάσκελο εσείς; Φάσκελο κι εγώ!' συνειδητοποιώντας την πραγματικότητα.",
    "funFacts": [
      "Η ταινία αποτελεί διαχρονική σάτιρα των πελατειακών σχέσεων και της διαφθοράς στην πολιτική ζωή.",
      "Ο Λάμπρος Κωνσταντάρας έδωσε μία από τις κορυφαίες ερμηνείες της καριέρας του ως Ανδρέας Μαυρογιαλούρος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%AC%CF%81%CF%87%CE%B5%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "konstantaras", "satire", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_147",
    "text": "Ποιο επιτραπέζιο παιχνίδι ρόλων (RPG) παίζουν τα παιδιά στο υπόγειο του Μάικ στη σειρά «Stranger Things»;",
    "answers": ["Dungeons & Dragons", "Warhammer", "Call of Cthulhu", "Magic: The Gathering"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η παρέα παίζει με πάθος Dungeons & Dragons (D&D), δανειζόμενη ονόματα τεράτων από το παιχνίδι (όπως Demogorgon και Mind Flayer) για τις απειλές που αντιμετωπίζουν.",
    "funFacts": [
      "Η τεράστια επιτυχία της σειράς οδήγησε σε παγκόσμια αναβίωση του ενδιαφέροντος για το Dungeons & Dragons.",
      "Το πρώτο επεισόδιο της σειράς ξεκινά με μια δεκάωρη παρτίδα D&D στην οποία ο Γουίλ αντιμετωπίζει τον Demogorgon."
    ],
    "source": "https://el.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger-things", "dnd", "netflix", "games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_148",
    "text": "Στη σειρά «Πενήντα Πενήντα» (Mega, 2005–2011), ποια ήταν τα ονόματα των τριών αχώριστων πενηντάρηδων φίλων;",
    "answers": ["Γιάννης, Πέτρος και Γιώργος", "Νικηφόρος, Μίμης και Παύλος", "Σπύρος, Βλάσσης και Κώστας", "Αλέκος, Μάκης και Σάββας"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Νικηφόρος (Πέτρος Φιλιππίδης), ο Μίμης (Παύλος Χαϊκάλης) και ο Παύλος (Σάκης Μπουλάς) ήταν το τρίο των φίλων που αντιμετώπιζαν την κρίση μέσης ηλικίας.",
    "funFacts": [
      "Το χαρακτηριστικό τσιπουράδικο στο οποίο συναντιόνταν ήταν το κέντρο των συζητήσεων και των σχεδίων τους.",
      "Το τραγούδι των τίτλων ερμήνευσε ο Λαυρέντης Μαχαιρίτσας."
    ],
    "source": "https://el.wikipedia.org/wiki/50-50_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "50-50", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_149",
    "text": "Ποιο είναι το όνομα της αγαπημένης θείας που μεγάλωσε τον Πίτερ Πάρκερ μετά τον θάνατο των γονιών του;",
    "answers": ["Θεία Σάρα", "Θεία Κλερ", "Θεία Μέι (May)", "Θεία Έμμα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Aunt May (Μέι Πάρκερ) είναι η στοργική θεία που μεγάλωσε τον Πίτερ μαζί με τον σύζυγό της θείο Μπεν στο Κουίνς της Νέας Υόρκης.",
    "funFacts": [
      "Στον κινηματογράφο τη θεία Μέι έχουν υποδυθεί η Ρόζμαρι Χάρις, η Σάλι Φιλντ και η Μαρίζα Τομέι.",
      "Ο τραγικός θάνατος του θείου Μπεν από έναν κλέφτη ήταν αυτός που ενέπνευσε τον Πίτερ να πολεμήσει το έγκλημα."
    ],
    "source": "https://el.wikipedia.org/wiki/Spider-Man",
    "locale": "el-GR",
    "tags": ["spider-man", "aunt-may", "marvel", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_150",
    "text": "Ποιος αγαπημένος κωμικός υποδύθηκε τον αφασικό σερβιτόρο Μπρίλη στην κλασική σκηνή με την «πορτοκαλάδα από πορτοκάλια»;",
    "answers": ["Κώστας Βουτσάς", "Νίκος Ρίζος", "Χρόνης Εξαρχάκος", "Γιάννης Γκιωνάκης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Στην ταινία 'Τα κίτρινα γάντια' (1960), ο Γιάννης Γκιωνάκης χάρισε έναν από τους πιο ξεκαρδιστικούς διαλόγους του ελληνικού σινεμά απέναντι στον Νίκο Σταυρίδη.",
    "funFacts": [
      "Ο διάλογος 'Πορτοκαλάδα θέτε; Από πορτοκάλια;' ήταν εμπνευσμένος από πραγματικό περιστατικό σε καφενείο στην Κόρινθο.",
      "Ο Γκιωνάκης αυτοσχεδίασε πολλές από τις ιδιόρρυθμες εκφράσεις του ρόλου του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%BA%CE%AF%CF%84%CF%81%CE%B9%CE%BD%CE%B1_%CE%B3%CE%AC%CE%BD%CF%84%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "gionakis", "stavridis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_151",
    "text": "Ποιο είναι το πιο διάσημο τραγούδι που τραγουδά η Φοίβη Μπουφέ με την κιθάρα της στη σειρά «Friends»;",
    "answers": ["Smelly Cat (Βρωμόγατος)", "Shiny Shoes", "Little Black Curly Hair", "Sticky Shoes"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το τραγούδι 'Smelly Cat' έγινε το σήμα κατατεθέν της Phoebe Buffay (Lisa Kudrow) και μία από τις πιο αναγνωρίσιμες μελωδίες της σειράς.",
    "funFacts": [
      "Σε ειδικό επεισόδιο της σειράς γυρίστηκε μάλιστα ένα υποτιθέμενο επίσημο βιντεοκλίπ για το τραγούδι.",
      "Η Λίζα Κούντροου το τραγούδησε ζωντανά σε συναυλίες μαζί με την Τέιλορ Σουίφτ και τη Lady Gaga."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%A6%CE%B9%CE%BB%CE%B1%CF%81%CE%AC%CE%BA%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["friends", "phoebe-buffay", "smelly-cat", "sitcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_152",
    "text": "Στην κωμική σειρά «Οι Στάβλοι της Εριέτας Ζαΐμη» (ΑΝΤ1, 2002–2004), σε ποιον ασυνήθιστο χώρο εκτυλίσσεται η υπόθεση;",
    "answers": ["Σε ένα ψυχιατρικό νοσοκομείο", "Σε πρότυπες γυναικείες φυλακές", "Σε ένα πολυτελές καζίνο", "Σε μια στρατιωτική βάση"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά των Αλέξανδρου Ρήγα και Δημήτρη Αποστόλου διαδραματίζεται στις πρότυπες σωφρονιστικές φυλακές γυναικών στον Κάλαμο.",
    "funFacts": [
      "Ο διευθυντής των φυλακών Ιάσων Παπαληγούρας (Νίκος Σεργιανόπουλος) ερωτεύεται παράφορα την κρατούμενη Εριέτα Ζαΐμη (Φαίη Κοκκινοπούλου).",
      "Η σειρά ξεχώρισε για το εκκεντρικό μαύρο χιούμορ και τους ακραίους χαρακτήρες των κρατουμένων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%A3%CF%84%CE%AC%CE%B2%CE%BB%CE%BF%CE%B9_%CF%84%CE%B7%CF%82_%CE%95%CF%81%CE%B9%CE%AD%CF%84%CE%B1%CF%82_%CE%96%CE%B1%CE%90%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-tv", "stavloi-tis-erietas-zaimi", "ant1", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_153",
    "text": "Ποιο είναι το όνομα της κλασικής ξύλινης κούκλας καουμπόι που είναι το αγαπημένο παιχνίδι του Άντι στο «Toy Story»;",
    "answers": ["Μπαζ", "Σλίνκι", "Γούντι (Woody)", "Ρεξ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Sheriff Woody Pride είναι ο καλόκαρδος καουμπόι και φυσικός ηγέτης των παιχνιδιών στο δωμάτιο του Άντι.",
    "funFacts": [
      "Στην αγγλική πρωτότυπη εκδοχή τη φωνή του Γούντι δανείζει ο διάσημος ηθοποιός Τομ Χανκς.",
      "Στην ελληνική μεταγλώττιση ο ηθοποιός Άλκης Κούρκουλος χάρισε τη φωνή του στον Γούντι."
    ],
    "source": "https://el.wikipedia.org/wiki/Toy_Story",
    "locale": "el-GR",
    "tags": ["pixar", "toy-story", "woody", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_154",
    "text": "Ποιο είναι το όνομα του χαριτωμένου χιονάνθρωπου που λατρεύει τις θερμές αγκαλιές και το καλοκαίρι στο «Frozen»;",
    "answers": ["Σβεν", "Κριστόφ", "Χανς", "Όλαφ (Olaf)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Olaf είναι ο μαγικός χιονάνθρωπος που δημιούργησε η Έλσα με τις δυνάμεις της, γνωστός για την αφέλεια και την αγάπη του για το καλοκαίρι.",
    "funFacts": [
      "Στην πρωτότυπη αγγλική εκδοχή τη φωνή του Όλαφ δάνεισε ο ηθοποιός Josh Gad.",
      "Στην ελληνική μεταγλώττιση ο Πάνος Μουζουράκης ερμήνευσε απολαυστικά τον αγαπημένο χαρακτήρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A8%CF%85%CF%87%CF%81%CE%AC_%CE%BA%CE%B9_%CE%91%CE%BD%CE%AC%CF%80%CE%BF%CE%B4%CE%B1",
    "locale": "el-GR",
    "tags": ["disney", "frozen", "olaf", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_155",
    "text": "Ποιο αντικείμενο στρίβει στον αέρα ο Χάρβεϊ Ντεντ («Διπρόσωπος») για να αποφασίσει τη μοίρα των θυμάτων του στο «The Dark Knight»;",
    "answers": ["Ένα νόμισμα", "Ένα ζάρι", "Μια κάρτα ταρώ", "Ένα πιστόλι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Two-Face (Aaron Eckhart) χρησιμοποιεί ένα ασημένιο δολάριο με δύο όψεις, η μία εκ των οποίων κάηκε και παραμορφώθηκε κατά την έκρηξη.",
    "funFacts": [
      "Πριν από το ατύχημά του χρησιμοποιούσε ένα νόμισμα με δύο ίδιες πλευρές κεφαλής, λέγοντας ότι 'φτιάχνει ο ίδιος την τύχη του'.",
      "Η ταινία θεωρείται από τους κριτικούς μία από τις σπουδαιότερες ταινίες υπερηρώων όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%A3%CE%BA%CE%BF%CF%84%CE%B5%CE%B9%CE%BD%CF%8C%CF%82_%CE%99%CF%80%CF%80%CF%8C%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["batman", "the-dark-knight", "two-face", "dc-comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_156",
    "text": "Στη σειρά «Άκρως Οικογενειακόν» (ΑΝΤ1), ποιο επάγγελμα ασκούσε ο αυστηρός αλλά τρυφερός πατέρας Αλέξανδρος Θεοτοκάτος;",
    "answers": ["Γιατρός", "Δικηγόρος", "Καθηγητής Πανεπιστημίου", "Αρχιτέκτονας"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Αλέξανδρος Θεοτοκάτος (Γιάννης Μπέζος) ήταν ένας πολυάσχολος δικηγόρος που προσπαθούσε να ισορροπήσει την καριέρα του με τα προβλήματα των τεσσάρων παιδιών του.",
    "funFacts": [
      "Η σειρά προβλήθηκε τις σεζόν 2001–2003 στον ΑΝΤ1 σημειώνοντας μεγάλη τηλεθέαση.",
      "Τη σύζυγό του Μαργαρίτα υποδύθηκε η Ναταλία Τσαλίκη, πραγματική σύζυγος του Γιάννη Μπέζου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BA%CF%81%CF%89%CF%82_%CE%9F%CE%B9%CE%BA%CE%BF%CE%B3%CE%B5%CE%BD%CE%B5%CE%B9%CE%B1%CE%BA%CF%8C%CE%BD",
    "locale": "el-GR",
    "tags": ["greek-tv", "akros-oikogeneiakon", "ant1", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_157",
    "text": "Στην ταινία κινουμένων σχεδίων «Μπαμπούλας Α.Ε.» (Monsters, Inc.), ποια είναι η πηγή ενέργειας που τροφοδοτεί την πόλη Μπαμπουλόπολη;",
    "answers": ["Ηλιακή ενέργεια", "Πυρηνική ενέργεια", "Οι παιδικές κραυγές φόβου", "Μαγικοί κρύσταλλοι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Τα τέρατα μπαίνουν στα δωμάτια των παιδιών τη νύχτα μέσω μαγικών πορτών για να συλλέξουν τις κραυγές τους, οι οποίες μετατρέπονται σε ηλεκτρική ενέργεια.",
    "funFacts": [
      "Στο τέλος της ταινίας ανακαλύπτουν ότι το παιδικό γέλιο παράγει δέκα φορές περισσότερη ενέργεια από τον φόβο.",
      "Η ταινία της Pixar απέσπασε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού για το 'If I Didn't Have You'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B1%CE%BC%CF%80%CE%BF%CF%8D%CE%BB%CE%B1%CF%82_%CE%91.%CE%95.",
    "locale": "el-GR",
    "tags": ["pixar", "monsters-inc", "animation", "disney"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_158",
    "text": "Στη μουσική κωμωδία «Η κόρη μου η σοσιαλίστρια» (1966), ποια πρωταγωνίστρια υποδύεται τη Λίζα που συγκρούεται με τον εργοστασιάρχη πατέρα της;",
    "answers": ["Τζένη Καρέζη", "Μάρω Κοντού", "Ζωή Λάσκαρη", "Αλίκη Βουγιουκλάκη"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Αλίκη Βουγιουκλάκη υποδύεται τη μοναχοκόρη ενός αυταρχικού εργοστασιάρχη (Λάμπρου Κωνσταντάρα), η οποία επιστρέφει από το Λονδίνο με προοδευτικές ιδέες.",
    "funFacts": [
      "Στην ταινία ακούγεται το πασίγνωστο τραγούδι του Γιώργου Ζαμπέτα 'Σήκω χόρεψε συρτάκι'.",
      "Υπήρξε η πιο εμπορική ταινία της σεζόν 1966–1967, κόβοντας 659.671 εισιτήρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%BA%CF%8C%CF%81%CE%B7_%CE%BC%CE%BF%CF%85_%CE%B7_%CF%83%CE%BF%CF%83%CE%B9%CE%B1%CE%BB%CE%AF%CF%83%CF%84%CF%81%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "aliki-vougiouklaki", "zampetas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_159",
    "text": "Ποιος είναι ο τριχωτός εξωγήινος Γούκι (Wookiee), συγκυβερνήτης και πιστός φίλος του Χαν Σόλο στο «Star Wars»;",
    "answers": ["Τσουμπάκα (Chewbacca)", "Τζάμπα ο Χατ", "Μπόμπα Φετ", "Γκρίντο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Chewbacca είναι ο πανύψηλος και πανίσχυρος πολεμιστής Wookiee από τον πλανήτη Kashyyyk, που επικοινωνεί με χαρακτηριστικούς λαρυγγισμούς.",
    "funFacts": [
      "Τον Τσουμπάκα ενσάρκωσε στην αρχική τριλογία ο πανύψηλος Βρετανός ηθοποιός Peter Mayhew, ύψους 2,18 μέτρων.",
      "Ο Τζορτζ Λούκας εμπνεύστηκε τον χαρακτήρα από τον αγαπημένο του σκύλο ράτσας Alaskan Malamute, που καθόταν πάντα στη θέση του συνοδηγού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%83%CE%BF%CF%85%CE%BC%CF%80%CE%AC%CE%BA%CE%B1",
    "locale": "el-GR",
    "tags": ["star-wars", "chewbacca", "wookiee", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_160",
    "text": "Στη σειρά «Στο Παρά 5», ποιο ήταν το όνομα της αξιαγάπητης κουφής γιαγιάς που ήταν αχώριστη φίλη με τη γιαγιά Σοφία;",
    "answers": ["Μαρίκα", "Θεοπούλα", "Ευδοξία", "Αντιγόνη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Θεοπούλα (Έφη Παπαθεοδώρου) και η γιαγιά Σοφία (Ειρήνη Κουμαριανού) αποτέλεσαν ένα από τα πιο ξεκαρδιστικά και αγαπημένα δίδυμα της ελληνικής τηλεόρασης.",
    "funFacts": [
      "Η διάσημη ατάκα της Θεοπούλας 'Κόβεται το σεξ;' συζητιέται μέχρι σήμερα ως κορυφαία τηλεοπτική στιγμή.",
      "Οι δύο ηθοποιοί συνδέονταν με πραγματική βαθιά φιλία εκτός πλατό για δεκαετίες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["greek-tv", "sto-para-5", "theopoula", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'easy', 1, questions)

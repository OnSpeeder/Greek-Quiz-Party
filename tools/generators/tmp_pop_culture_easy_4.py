# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_easy_161",
    "text": "Ποιο είδος ζώου είναι ο Μπαλού που μαθαίνει στον Μόγλη τα 'απολύτως απαραίτητα' στο 'Βιβλίο της Ζούγκλας';",
    "answers": [
      "Αρκούδα",
      "Πάνθηρας",
      "Τίγρης",
      "Λύκος"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μπαλού είναι μια καλόκαρδη και νωχελική αρκούδα που τραγουδά το πασίγνωστο τραγούδι 'The Bare Necessities'.",
    "funFacts": [
      "Η ταινία της Disney (1967) ήταν η τελευταία παραγωγή κινουμένων σχεδίων που επέβλεψε προσωπικά ο ίδιος ο Walt Disney πριν τον θάνατό του.",
      "Ο πάνθηρας που προστατεύει επίσης τον Μόγλη και τον καθοδηγεί με σοβαρότητα ονομάζεται Μπαγκίρα."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Jungle_Book_(1967_film)",
    "locale": "el-GR",
    "tags": ["the_jungle_book", "disney", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_162",
    "text": "Ποιος πρωταγωνίστησε στην ταινία 'The Truman Show' (1998) ως ο άνδρας που ανακαλύπτει ότι όλη η ζωή του είναι τηλεοπτικό ριάλιτι;",
    "answers": [
      "Ρόμπιν Ουίλιαμς",
      "Τζιμ Κάρεϊ",
      "Τομ Χανκς",
      "Μπιλ Μάρεϊ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Jim Carrey έδωσε μια συγκλονιστική δραματική και κωμική ερμηνεία ως Truman Burbank, κερδίζοντας Χρυσή Σφαίρα.",
    "funFacts": [
      "Η χαρακτηριστική αποχαιρετιστήρια ατάκα του Truman είναι: 'Good afternoon, good evening, and good night!'.",
      "Η ψυχιατρική κοινότητα αναγνώρισε αργότερα μια πραγματική παραληρητική διαταραχή που ονομάστηκε 'The Truman Show delusion'."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Truman_Show",
    "locale": "el-GR",
    "tags": ["the_truman_show", "jim_carrey", "cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_163",
    "text": "Ποια διάσημη Καναδή τραγουδίστρια ερμήνευσε το οσκαρικό τραγούδι 'My Heart Will Go On' για την ταινία 'Τιτανικός';",
    "answers": [
      "Γουίτνεϊ Χιούστον",
      "Μαράια Κάρεϊ",
      "Σελίν Ντιόν",
      "Σανάια Τουέιν"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Celine Dion ερμήνευσε το 'My Heart Will Go On', το οποίο έγινε το πιο επιτυχημένο single στην καριέρα της και κέρδισε Όσκαρ και Grammy.",
    "funFacts": [
      "Η Celine Dion αρχικά δεν ήθελε να ηχογραφήσει το τραγούδι, αλλά πείστηκε από τον σύζυγό της να κάνει μια πρόχειρη δοκιμαστική ηχογράφηση (demo), η οποία τελικά χρησιμοποιήθηκε στην ταινία.",
      "Το τραγούδι πούλησε πάνω από 18 εκατομμύρια αντίτυπα παγκοσμίως και βρέθηκε στο νούμερο 1 σε περισσότερες από είκοσι χώρες."
    ],
    "source": "https://en.wikipedia.org/wiki/My_Heart_Will_Go_On",
    "locale": "el-GR",
    "tags": ["celine_dion", "titanic", "music", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_164",
    "text": "Ποια πρωταγωνίστρια τραγούδησε το αξέχαστο 'Του αγοριού απέναντι' στο μιούζικαλ 'Γοργόνες και Μάγκες' (1968);",
    "answers": [
      "Ζωή Λάσκαρη",
      "Μάρθα Καραγιάννη",
      "Νόρα Βαλσάμη",
      "Μαίρη Χρονοπούλου"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Μαίρη Χρονοπούλου τραγούδησε το ιστορικό κομμάτι των Μίμη Πλέσσα και Λευτέρη Παπαδόπουλου ντυμένη στα μαύρα στο νησιώτικο ταβερνάκι.",
    "funFacts": [
      "Η ταινία γυρίστηκε σχεδόν εξ ολοκλήρου στο γραφικό νησί της Ύδρας.",
      "Στην ίδια ταινία ο Γιάννης Πουλόπουλος ερμήνευσε μοναδικά το τραγούδι 'Καμαρούλα μια σταλιά'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%81%CE%B3%CF%8C%CE%BD%CE%B5%CF%82_%CE%BA%CE%B1%CE%B9_%CE%BC%CE%AC%CE%B3%CE%BA%CE%B5%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "chronopoulou", "plessas", "musicals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_165",
    "text": "Ποιος θρυλικός δημιουργός των κόμικς της Marvel έκανε χαρακτηριστικές σύντομες εμφανίσεις (cameos) στις περισσότερες ταινίες του MCU;",
    "answers": [
      "Σταν Λι",
      "Τζακ Κίρμπι",
      "Στιβ Ντίτκο",
      "Μπομπ Κέιν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Stan Lee (1922-2018), συνδημιουργός ηρώων όπως ο Spider-Man, οι Avengers και οι X-Men, έκανε cameo σε δεκάδες ταινίες της Marvel.",
    "funFacts": [
      "Η αγαπημένη του φράση-σλόγκαν με την οποία υπέγραφε τις στήλες του στα κόμικς ήταν το λατινογενές 'Excelsior!'.",
      "Το τελευταίο του κινηματογραφικό cameo προβλήθηκε μετά θάνατον στην ταινία 'Avengers: Endgame' (2019)."
    ],
    "source": "https://en.wikipedia.org/wiki/Stan_Lee",
    "locale": "el-GR",
    "tags": ["marvel", "stan_lee", "comics", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_166",
    "text": "Ποιο είδος ζώου είναι ο Alex, ο βασικός πρωταγωνιστής της ταινίας κινουμένων σχεδίων 'Μαδαγασκάρη' (2005);",
    "answers": [
      "Ζέβρα",
      "Λιοντάρι",
      "Καμηλοπάρδαλη",
      "Ιπποπόταμος"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Alex είναι το καλομαθημένο λιοντάρι και αδιαμφισβήτητος 'Βασιλιάς της Νέας Υόρκης' στον ζωολογικό κήπο του Central Park.",
    "funFacts": [
      "Τη φωνή του Alex στην αμερικανική εκδοχή έδωσε ο Ben Stiller, ενώ στην ελληνική μεταγλώττιση ο Σπύρος Ζουπάνος.",
      "Ο λεμούριος Βασιλιάς Τζούλιαν έκλεψε την παράσταση τραγουδώντας το ξεσηκωτικό 'I Like to Move It'."
    ],
    "source": "https://en.wikipedia.org/wiki/Madagascar_(2005_film)",
    "locale": "el-GR",
    "tags": ["madagascar", "dreamworks", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_167",
    "text": "Σε ποιο πολυτελές ξενοδοχείο της σειράς του Mega 'Το Κόκκινο Δωμάτιο' εκτυλίσσονταν οι ιστορίες των ενοίκων;",
    "answers": [
      "Grand Hotel Athina",
      "Hotel Poseidon",
      "Conte Del Mare",
      "Palace Resort"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το ξενοδοχείο Conte Del Mare φιλοξενούσε την περίφημη κοκκινόχρωμη σουίτα όπου εκτυλίσσονταν οι αυτοτελείς κωμικές και δραματικές ιστορίες.",
    "funFacts": [
      "Η Βασιλική Ανδρίτσου υποδύθηκε τη δυναμική ρεσεψιονίστ Μάρω και ο Αλέξανδρος Ρήγας τον μπάρμαν Μίλτο.",
      "Η σειρά προβλήθηκε για 3 σεζόν (2005-2008) και φιλοξένησε δεκάδες διάσημους Έλληνες ηθοποιούς ως guest stars."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%BF_%CE%B4%CF%89%CE%BC%CE%AC%CF%84%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["to_kokkino_domatio", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_168",
    "text": "Ποιο ρόλο ευφυούς αλλά κανίβαλου ψυχιάτρου ενσάρκωσε ο Anthony Hopkins στην ταινία 'Η Σιωπή των Αμνών' (1991);",
    "answers": [
      "Norman Bates",
      "Jack Torrance",
      "Patrick Bateman",
      "Dr. Hannibal Lecter"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Anthony Hopkins κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου για την ερμηνεία του ως Hannibal Lecter παρόλο που εμφανίστηκε στην οθόνη για λιγότερο από 25 λεπτά.",
    "funFacts": [
      "Η ταινία είναι μία από τις μόλις τρεις στην ιστορία των Όσκαρ που κέρδισαν και τα πέντε μεγάλα βραβεία (Ταινίας, Σκηνοθεσίας, Α' Ανδρικού, Α' Γυναικείου, Σεναρίου).",
      "Την πράκτορα του FBI Clarice Starling υποδύθηκε η Jodie Foster, κερδίζοντας επίσης το Όσκαρ Α' Γυναικείου Ρόλου."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Silence_of_the_Lambs_(film)",
    "locale": "el-GR",
    "tags": ["silence_of_the_lambs", "hannibal_lecter", "cinema", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_169",
    "text": "Ποιο πράσινο περιστρεφόμενο σύμβολο αιωρείται πάνω από το κεφάλι των χαρακτήρων στο παιχνίδι προσομοίωσης ζωής 'The Sims';",
    "answers": [
      "Plumbob (πράσινος κρύσταλλος)",
      "Χρυσό αστέρι",
      "Κόκκινη καρδιά",
      "Μπλε κύβος"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Plumbob είναι ένας πράσινος ρομβοειδής κρύσταλλος που δείχνει ποιος Sim είναι ενεργός και αντικατοπτρίζει τη διάθεσή του.",
    "funFacts": [
      "Η ακαταλαβίστικη γλώσσα που μιλούν όλοι οι χαρακτήρες στα παιχνίδια της σειράς ονομάζεται 'Simlish'.",
      "Το The Sims δημιουργήθηκε από τον Will Wright και αποτέλεσε ένα από τα πιο επιτυχημένα franchises ηλεκτρονικών παιχνιδιών όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Sims",
    "locale": "el-GR",
    "tags": ["the_sims", "ea", "gaming", "maxis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_170",
    "text": "Σε ποιον πλανήτη εκτυλίσσεται το μουσικό βίντεο της Britney Spears για το τραγούδι 'Oops!... I Did It Again' (2000);",
    "answers": [
      "Στη Σελήνη",
      "Στον Άρη",
      "Στην Αφροδίτη",
      "Στον Δία"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στο βίντεο κλιπ, ένας αστροναύτης προσεδαφίζεται στον κόκκινο πλανήτη Άρη και συναντά την Britney Spears με κόκκινη ολόσωμη στολή από λατέξ.",
    "funFacts": [
      "Το βίντεο περιλαμβάνει διάλογο όπου ο αστροναύτης χαρίζει στην Britney το περιδέραιο 'Heart of the Ocean' από τον Τιτανικό.",
      "Το άλμπουμ πούλησε πάνω από 1,3 εκατομμύριο αντίτυπα στην πρώτη εβδομάδα κυκλοφορίας του στις ΗΠΑ, σημειώνοντας ρεκόρ για γυναίκα καλλιτέχνιδα."
    ],
    "source": "https://en.wikipedia.org/wiki/Oops!..._I_Did_It_Again_(song)",
    "locale": "el-GR",
    "tags": ["britney_spears", "music", "pop", "2000s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_171",
    "text": "Ποιος διάσημος ηθοποιός δάνεισε τη φωνή του στον ημίθεο Μάουι στην ταινία κινουμένων σχεδίων 'Μοάνα' (Moana, 2016);",
    "answers": [
      "Βιν Ντίζελ",
      "Τζέισον Μομόα",
      "Ντουέιν Τζόνσον (The Rock)",
      "Κρις Πρατ"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Dwayne 'The Rock' Johnson χάρισε τη φωνή του στον πολυνησιακό ημίθεο Maui και τραγούδησε το κομμάτι 'You're Welcome'.",
    "funFacts": [
      "Ο σχεδιασμός και τα κινούμενα τατουάζ στο σώμα του Maui ήταν εμπνευσμένα από την πολυνησιακή κληρονομιά του ίδιου του Dwayne Johnson.",
      "Η ταινία ήταν υποψήφια για δύο βραβεία Όσκαρ, συμπεριλαμβανομένου αυτού για το τραγούδι 'How Far I'll Go' του Lin-Manuel Miranda."
    ],
    "source": "https://en.wikipedia.org/wiki/Moana_(2016_film)",
    "locale": "el-GR",
    "tags": ["moana", "disney", "animation", "dwayne_johnson"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_172",
    "text": "Ποιος ανορθόδοξος δικηγόρος από το 'Breaking Bad' απέκτησε τη δική του εξαιρετικά επιτυχημένη σειρά prequel;",
    "answers": [
      "Hank Schrader",
      "Mike Ehrmantraut",
      "Gustavo Fring",
      "Saul Goodman"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Bob Odenkirk πρωταγωνίστησε ως ο δικηγόρος Saul Goodman (πραγματικό όνομα Jimmy McGill) στη σειρά 'Better Call Saul'.",
    "funFacts": [
      "Το ψευδώνυμο 'Saul Goodman' προήλθε από την παράφραση της φράσης '[It]'s all good, man!'.",
      "Η σειρά 'Better Call Saul' διήρκεσε 6 σεζόν και απέσπασε συνολικά 53 υποψηφιότητες για βραβεία Emmy."
    ],
    "source": "https://en.wikipedia.org/wiki/Better_Call_Saul",
    "locale": "el-GR",
    "tags": ["better_call_saul", "breaking_bad", "tv", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_173",
    "text": "Ποιος σπουδαίος ηθοποιός ενσάρκωσε τον 'Ψευτοθόδωρο' στην κλασική κωμωδία 'Ζητείται Ψεύτης' (1961);",
    "answers": [
      "Ντίνος Ηλιόπουλος",
      "Κώστας Βουτσάς",
      "Διονύσης Παπαγιαννόπουλος",
      "Μίμης Φωτόπουλος"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ντίνος Ηλιόπουλος υποδύθηκε τον Θεόδωρο Πάρλα, έναν ασυναγώνιστο ψεύτη που προσλαμβάνεται από έναν βουλευτή για να κατευνάζει τους ψηφοφόρους του.",
    "funFacts": [
      "Τον ρόλο του βουλευτή Θεόφιλου Φερέκη ενσάρκωσε απολαυστικά ο Παντελής Ζερβός.",
      "Η ταινία βασίστηκε στο ομώνυμο θεατρικό έργο του Δημήτρη Ψαθά και αποτελεί διαχρονική σάτιρα της πολιτικής ζωής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B7%CF%84%CE%B5%CE%AF%CF%84%CE%B1%CE%B9_%CF%88%CE%B5%CF%8D%CF%84%CE%B7%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1961)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "iliopoulos", "psathas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_174",
    "text": "Ποια διάσημη ηθοποιός ενσάρκωσε τη Natasha Romanoff (Black Widow) στο Κινηματογραφικό Σύμπαν της Marvel (MCU);",
    "answers": [
      "Έμιλι Μπλαντ",
      "Σκάρλετ Τζοχάνσον",
      "Νάταλι Πόρτμαν",
      "Σαρλίζ Θερόν"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Scarlett Johansson πρωτοεμφανίστηκε ως Black Widow στο 'Iron Man 2' (2010) και παρέμεινε βασικό στέλεχος των Avengers για πάνω από μία δεκαετία.",
    "funFacts": [
      "Η Scarlett Johansson έκανε μόνη της πολλές από τις δύσκολες σκηνές μάχης και ακροβατικών του ρόλου.",
      "Η ηρωίδα θυσιάστηκε στον πλανήτη Vormir στο 'Avengers: Endgame' (2019) ώστε η ομάδα να αποκτήσει την Πέτρα της Ψυχής."
    ],
    "source": "https://en.wikipedia.org/wiki/Natasha_Romanoff_(Marvel_Cinematic_Universe)",
    "locale": "el-GR",
    "tags": ["marvel", "black_widow", "mcu", "scarlett_johansson"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_175",
    "text": "Ποια παραδοσιακή μεξικανική γιορτή αποτελεί το σκηνικό της ταινίας κινουμένων σχεδίων 'Coco' (2017) της Pixar;",
    "answers": [
      "Cinco de Mayo",
      "Fiesta de la Candelaria",
      "Día de los Muertos (Ημέρα των Νεκρών)",
      "Las Posadas"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η υπόθεση του 'Coco' διαδραματίζεται κατά την Ημέρα των Νεκρών (Día de los Muertos), όταν οι ψυχές επιστρέφουν στον κόσμο των ζωντανών.",
    "funFacts": [
      "Το συγκινητικό τραγούδι 'Remember Me' κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 2018.",
      "Το 'Coco' έγινε η ταινία με τα υψηλότερα εισιτήρια στην ιστορία του μεξικανικού κινηματογράφου."
    ],
    "source": "https://en.wikipedia.org/wiki/Coco_(2017_film)",
    "locale": "el-GR",
    "tags": ["coco", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_176",
    "text": "Ποιο μουσικό είδος καθιέρωσε σε όλο τον κόσμο ο θρυλικός Τζαμαϊκανός τραγουδοποιός Bob Marley;",
    "answers": [
      "Σάλσα",
      "Καλυψώ",
      "Μποσάνοβα",
      "Ρέγκε (Reggae)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Bob Marley υπήρξε ο κορυφαίος πρεσβευτής της ρέγκε μουσικής διεθνώς με τραγούδια όπως τα 'No Woman, No Cry' και 'One Love'.",
    "funFacts": [
      "Το άλμπουμ αναδρομής 'Legend' (1984) παραμένει το ρέγκε άλμπουμ με τις μεγαλύτερες πωλήσεις όλων των εποχών, έχοντας πουλήσει άνω των 25 εκατομμυρίων αντιτύπων.",
      "Το 1978, ο Marley ένωσε συμβολικά τα χέρια των δύο αντίπαλων πολιτικών αρχηγών της Τζαμάικα πάνω στη σκηνή κατά τη συναυλία 'One Love Peace'."
    ],
    "source": "https://en.wikipedia.org/wiki/Bob_Marley",
    "locale": "el-GR",
    "tags": ["bob_marley", "reggae", "music", "jamaica"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_177",
    "text": "Ποια διάσημη ατάκα φωνάζει ο Jack Nicholson σπάζοντας την πόρτα με τσεκούρι στην ταινία 'Η Λάμψη' (The Shining, 1980);",
    "answers": [
      "Here's Johnny!",
      "I'm back!",
      "Surprise!",
      "Knock knock!"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η φράση 'Here's Johnny!' ήταν ένας αυτοσχεδιασμός του Nicholson εμπνευσμένος από την εισαγωγή του 'The Tonight Show Starring Johnny Carson'.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Stanley Kubrick και βασίστηκε στο ομώνυμο βιβλίο τρόμου του Stephen King.",
      "Για τη σκηνή όπου σπάει την πόρτα του μπάνιου, ο Jack Nicholson χρειάστηκε να καταστρέψει περίπου 60 πόρτες μέχρι να μείνει ικανοποιημένος ο σκηνοθέτης."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Shining_(film)",
    "locale": "el-GR",
    "tags": ["the_shining", "jack_nicholson", "kubrick", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_178",
    "text": "Ποια ατάκα επαναλάμβανε συνεχώς η Δήμητρα στον Θοδωρή στη δημοφιλή σειρά του Mega 'Σ' αγαπώ - Μ' αγαπάς';",
    "answers": [
      "Πότε θα πάμε διακοπές;",
      "Εγώ πότε θα γίνω μάνα;",
      "Πότε θα παντρευτούμε επιτέλους;",
      "Γιατί δεν με προσέχεις;"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Εγώ πότε θα γίνω μάνα;' έγινε μία από τις πιο αναγνωρίσιμες και χιουμοριστικές τηλεοπτικές ατάκες των αρχών της δεκαετίας του 2000.",
    "funFacts": [
      "Η σειρά παρουσίαζε τη ζωή του ζευγαριού μέσα από σταθερή κάμερα χωρίς να φαίνονται ποτέ τρίτα πρόσωπα στην οθόνη.",
      "Βασίστηκε στο επιτυχημένο γαλλόφωνο καναδικό φορμάτ 'Un gars, une fille' και προβλήθηκε τις σεζόν 2000-2002."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%27_%CE%B1%CE%B3%CE%B1%CF%80%CF%8E_-_%CE%9C%27_%CE%B1%CE%B3%CE%B1%CF%80%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["s_agapo_m_agapas", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_179",
    "text": "Ποιο είδος ζώου είναι ο κλασικός αντίπαλος της Nintendo Donkey Kong που πετάει βαρέλια;",
    "answers": [
      "Χιμπατζής",
      "Ουρακοτάγκος",
      "Γορίλας",
      "Μπαμπουίνος"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Donkey Kong είναι ένας γιγάντιος γορίλας με κόκκινη γραβάτα που πρωτοεμφανίστηκε στα arcades το 1981.",
    "funFacts": [
      "Ο Shigeru Miyamoto επέλεξε τη λέξη 'Donkey' πιστεύοντας λανθασμένα ότι σήμαινε 'πεισματάρης' στα αγγλικά.",
      "Το παιχνίδι Donkey Kong αποτέλεσε το ντεμπούτο τόσο του ομώνυμου γορίλα όσο και του Mario."
    ],
    "source": "https://en.wikipedia.org/wiki/Donkey_Kong",
    "locale": "el-GR",
    "tags": ["donkey_kong", "nintendo", "gaming", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_180",
    "text": "Σε ποια ευρωπαϊκή πρωτεύουσα μετακομίζει η νεαρή Αμερικανίδα Emily Cooper στην επιτυχημένη σειρά του Netflix 'Emily in Paris';",
    "answers": [
      "Στη Ρώμη",
      "Στη Μαδρίτη",
      "Στο Λονδίνο",
      "Στο Παρίσι"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Emily (Lily Collins) μετακομίζει στο Παρίσι για να προσφέρει μια αμερικανική οπτική στη γαλλική εταιρεία μάρκετινγκ Savoir.",
    "funFacts": [
      "Η σειρά δημιουργήθηκε από τον Darren Star, τον δημιουργό του 'Sex and the City'.",
      "Η σειρά προκάλεσε έντονες συζητήσεις στη Γαλλία για τα στερεότυπα που παρουσιάζει σχετικά με τη ζωή στο Παρίσι, αλλά γνώρισε τεράστια παγκόσμια θεαματικότητα."
    ],
    "source": "https://en.wikipedia.org/wiki/Emily_in_Paris",
    "locale": "el-GR",
    "tags": ["emily_in_paris", "netflix", "tv", "paris"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_181",
    "text": "Ποιο είναι το όνομα του μικρού κόκκινου δράκου που συντροφεύει και προστατεύει τη Μουλάν στην ομώνυμη ταινία της Disney;",
    "answers": [
      "Μούσου (Mushu)",
      "Κρίκι",
      "Σαν Γιου",
      "Χαν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μούσου είναι ένας μικρόσωμος κηδεμόνας-δράκος που στέλνεται από τους προγόνους για να βοηθήσει τη Μουλάν στον πόλεμο.",
    "funFacts": [
      "Στην αμερικανική εκδοχή τη φωνή του Mushu έκανε ο Eddie Murphy, ενώ στην ελληνική ο Πέτρος Φιλιππίδης.",
      "Η ταινία βασίστηκε στον αρχαίο κινεζικό θρύλο της πολεμίστριας Χουά Μουλάν."
    ],
    "source": "https://en.wikipedia.org/wiki/Mulan_(1998_film)",
    "locale": "el-GR",
    "tags": ["mulan", "disney", "animation", "mushu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_182",
    "text": "Πώς ονομάζεται το θρυλικό πειρατικό πλοίο με τα μαύρα πανιά του Jack Sparrow στους 'Πειρατές της Καραϊβικής';",
    "answers": [
      "Flying Dutchman",
      "Μαύρο Μαργαριτάρι (Black Pearl)",
      "Queen Anne's Revenge",
      "Silent Mary"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Black Pearl είναι το ταχύτερο πλοίο της Καραϊβικής και το μεγάλο πάθος του καπετάνιου Jack Sparrow.",
    "funFacts": [
      "Πριν βαφτεί μαύρο και μετονομαστεί σε Black Pearl, το πλοίο ονομαζόταν 'Wicked Wench'.",
      "Στην πρώτη ταινία, το πλήρωμα του πλοίου τελούσε υπό την επίδραση της κατάρας του χρυσού των Αζτέκων μεταμορφωνόμενο σε σκελετούς στο σεληνόφως."
    ],
    "source": "https://en.wikipedia.org/wiki/Black_Pearl",
    "locale": "el-GR",
    "tags": ["pirates_of_the_caribbean", "black_pearl", "cinema", "disney"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_183",
    "text": "Ποια Βρετανοαλβανίδα τραγουδίστρια κυριάρχησε στην παγκόσμια ποπ σκηνή με το άλμπουμ 'Future Nostalgia' και την επιτυχία 'Levitating';",
    "answers": [
      "Rita Ora",
      "Bebe Rexha",
      "Dua Lipa",
      "Charli XCX"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Dua Lipa κατέκτησε τον πλανήτη το 2020 με το disco-pop άλμπουμ της 'Future Nostalgia' κερδίζοντας βραβείο Grammy.",
    "funFacts": [
      "Το τραγούδι της 'Levitating' ήταν το single με τη μεγαλύτερη παραμονή και τις περισσότερες αναπαραγωγές στο αμερικανικό Billboard Hot 100 για το έτος 2021.",
      "Η Dua Lipa έκανε το ντεμπούτο της ως ηθοποιός στην ταινία 'Barbie' (2023) ερμηνεύοντας επίσης το τραγούδι 'Dance the Night'."
    ],
    "source": "https://en.wikipedia.org/wiki/Dua_Lipa",
    "locale": "el-GR",
    "tags": ["dua_lipa", "music", "pop", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_184",
    "text": "Ποιο παρατσούκλι μητέρας ενσάρκωσε μοναδικά η Μαίρη Αρώνη στην κλασική κωμωδία 'Μια τρελή, τρελή οικογένεια' (1965);",
    "answers": [
      "Μαντάμ Σουσού",
      "Κυρία Ντορεμί",
      "Μπέμπα",
      "Πάστα Φλώρα"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Μαίρη Αρώνη υποδύθηκε την αφηρημένη και εκκεντρική μητέρα 'Πάστα Φλώρα' σε μια από τις πιο εμβληματικές ερμηνείες του ελληνικού σινεμά.",
    "funFacts": [
      "Η ταινία γυρίστηκε σε συμπαραγωγή της Φίνος Φιλμ στη Βενετία και στην Αθήνα.",
      "Στην ταινία πρωταγωνίστησαν επίσης η Τζένη Καρέζη, ο Αλέκος Αλεξανδράκης και ο Διονύσης Παπαγιαννόπουλος (Στέλιος)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CF%84%CF%81%CE%B5%CE%BB%CE%AE,_%CF%84%CF%81%CE%B5%CE%BB%CE%AE_%CE%BF%CE%B9%CE%BA%CE%BF%CE%B3%CE%AD%CE%BD%CE%B5%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["greek_cinema", "aroni", "karezi", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_185",
    "text": "Ποια ηθοποιός ενσάρκωσε την Carol Danvers στην ταινία της Marvel 'Captain Marvel' (2019);",
    "answers": [
      "Μπρι Λάρσον",
      "Τζένιφερ Λόρενς",
      "Έμμα Στόουν",
      "Σίρσα Ρόναν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η βραβευμένη με Όσκαρ Brie Larson υποδύθηκε την πιλότο Carol Danvers που αποκτά κοσμικές υπερδυνάμεις και γίνεται η Captain Marvel.",
    "funFacts": [
      "Το Captain Marvel ήταν η πρώτη ταινία του MCU με πρωταγωνίστρια γυναίκα υπερηρωίδα σε σόλο τίτλο.",
      "Η ταινία ξεπέρασε το 1,1 δισεκατομμύριο δολάρια στο παγκόσμιο box office."
    ],
    "source": "https://en.wikipedia.org/wiki/Captain_Marvel_(film)",
    "locale": "el-GR",
    "tags": ["captain_marvel", "marvel", "mcu", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_186",
    "text": "Ποιος είναι ο αριθμός του αγωνιστικού αυτοκινήτου Κεραυνός Μακουίν (Lightning McQueen) στην ταινία 'Cars' (2006);",
    "answers": [
      "51",
      "95",
      "86",
      "43"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Lightning McQueen αγωνίζεται με τον αριθμό 95, προς τιμήν του έτους 1995 στο οποίο κυκλοφόρησε η πρώτη ταινία της Pixar, το 'Toy Story'.",
    "funFacts": [
      "Η πόλη όπου καταλήγει κατά λάθος ο Lightning McQueen στον ιστορικό Route 66 ονομάζεται Radiator Springs.",
      "Τη φωνή του McQueen στην αυθεντική ταινία κάνει ο Owen Wilson, ενώ στην ελληνική μεταγλώττιση ο Σάκης Ρουβάς."
    ],
    "source": "https://en.wikipedia.org/wiki/Cars_(film)",
    "locale": "el-GR",
    "tags": ["cars", "pixar", "animation", "lightning_mcqueen"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_187",
    "text": "Ποιο πυρηνικό ατύχημα του 1986 αποτέλεσε το θέμα της καθηλωτικής μίνι σειράς του HBO που καθήλωσε το παγκόσμιο κοινό το 2019;",
    "answers": [
      "Φουκουσίμα",
      "Three Mile Island",
      "Τσερνόμπιλ",
      "Κυστίμ"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η μίνι σειρά 'Chernobyl' του Craig Mazin εξιστόρησε τα δραματικά γεγονότα της έκρηξης του αντιδραστήρα 4 στον πυρηνικό σταθμό του Τσερνόμπιλ στη Σοβιετική Ουκρανία.",
    "funFacts": [
      "Η σειρά κέρδισε 10 βραβεία Emmy και έγινε μία από τις σειρές με την υψηλότερη βαθμολογία όλων των εποχών στο IMDb (9.4/10).",
      "Η διάσημη ατάκα '3.6 roentgen, not great, not terrible' έγινε παγκόσμιο meme."
    ],
    "source": "https://en.wikipedia.org/wiki/Chernobyl_(miniseries)",
    "locale": "el-GR",
    "tags": ["chernobyl", "hbo", "tv", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_188",
    "text": "Ποιο ιστορικό άλμπουμ των Pink Floyd έχει στο εξώφυλλό του ένα γυάλινο πρίσμα που διαθλά μια δέσμη φωτός σε ουράνιο τόξο;",
    "answers": [
      "The Wall",
      "Wish You Were Here",
      "Animals",
      "The Dark Side of the Moon"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'The Dark Side of the Moon' (1973) των Pink Floyd είναι ένα από τα πιο αναγνωρίσιμα και επιτυχημένα ροκ άλμπουμ όλων των εποχών.",
    "funFacts": [
      "Το άλμπουμ παρέμεινε στο Billboard 200 chart για το ασύλληπτο ρεκόρ των 950 και πλέον εβδομάδων (πάνω από 18 χρόνια συνολικά).",
      "Το διάσημο εξώφυλλο σχεδιάστηκε από τη γραφιστική κολεκτίβα Hipgnosis και τον Storm Thorgerson."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Dark_Side_of_the_Moon",
    "locale": "el-GR",
    "tags": ["pink_floyd", "rock", "music", "70s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_189",
    "text": "Σε ποιο φανταστικό τροπικό νησί κοντά στην Κόστα Ρίκα δημιουργήθηκε το αρχικό 'Jurassic Park';",
    "answers": [
      "Ίσλα Νούμπλαρ (Isla Nublar)",
      "Ίσλα Σόρνα",
      "Αμίτι Άιλαντ",
      "Σκοπελίτι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Isla Nublar ('Νησί των Σύννεφων') είναι το νησί όπου ο John Hammond ίδρυσε το αρχικό θεματικό πάρκο δεινοσαύρων.",
    "funFacts": [
      "Το κοντινό νησί Isla Sorna (Site B) ήταν ο χώρος όπου οι δεινόσαυροι εκτρέφονταν εργοστασιακά πριν μεταφερθούν στο πάρκο.",
      "Τα περισσότερα γυρίσματα της ταινίας πραγματοποιήθηκαν στην πραγματικότητα στα νησιά Kauai και Oahu της Χαβάης."
    ],
    "source": "https://en.wikipedia.org/wiki/Jurassic_Park_(film)",
    "locale": "el-GR",
    "tags": ["jurassic_park", "cinema", "dinosaurs", "spielberg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_190",
    "text": "Ποιος ηθοποιός υποδύθηκε τον αυστηρό και ιδιόρρυθμο διαχειριστή Θανάση Μπαλαφούτη στη σειρά του Mega 'Η Πολυκατοικία';",
    "answers": [
      "Γιάννης Μπέζος",
      "Παύλος Χαϊκάλης",
      "Κώστας Κόκλας",
      "Χάρης Ρώμας"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Παύλος Χαϊκάλης ενσάρκωσε τον παθιασμένο με τα κοινόχρηστα διαχειριστή Θανάση Μπαλαφούτη στην επιτυχημένη σειρά του Mega.",
    "funFacts": [
      "Η σειρά βασίστηκε στην εξαιρετικά δημοφιλή ισπανική κωμωδία 'Aquí no hay quien viva'.",
      "Προβλήθηκε για τρεις τηλεοπτικές σεζόν (2008-2011) σημειώνοντας πολύ υψηλή τηλεθέαση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A0%CE%BF%CE%BB%CF%85%CE%BA%CE%B1%CF%84%CE%BF%CE%B9%CE%BA%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["i_polykatoikia", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_191",
    "text": "Ποια μοχθηρή φαρμακευτική εταιρεία ευθύνεται για τον ιό T-Virus και τα ζόμπι στη σειρά βιντεοπαιχνιδιών 'Resident Evil';",
    "answers": [
      "Aperture Science",
      "Vault-Tec",
      "Umbrella Corporation",
      "Shinra Company"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Umbrella Corporation δημιούργησε βιολογικά όπλα και τον μεταλλαξιογόνο ιό T-Virus στο υπόγειο εργαστήριο Hive κάτω από τη Raccoon City.",
    "funFacts": [
      "Στην Ιαπωνία, το franchise του παιχνιδιού είναι γνωστό με τον αρχικό τίτλο 'Biohazard'.",
      "Το Resident Evil θεωρείται ο θεμελιωτής του είδους παιχνιδιών επιβίωσης τρόμου (survival horror)."
    ],
    "source": "https://en.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident_evil", "capcom", "gaming", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_192",
    "text": "Ποιος διάσημος Βρετανός μουσικός έγραψε και ερμήνευσε το οσκαρικό σάουντρακ της animated ταινίας 'Tarzan' (1999) της Disney;",
    "answers": [
      "Στινγκ",
      "Έλτον Τζον",
      "Πολ Μακάρτνεϊ",
      "Φιλ Κόλινς"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Phil Collins συνέθεσε και τραγούδησε τα κομμάτια της ταινίας, κερδίζοντας Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού για το 'You'll Be in My Heart'.",
    "funFacts": [
      "Ο Phil Collins ηχογράφησε τα τραγούδια του σάουντρακ ο ίδιος σε πέντε γλώσσες (αγγλικά, ισπανικά, γαλλικά, ιταλικά και γερμανικά).",
      "Το άλμπουμ του σάουντρακ πούλησε πάνω από 2 εκατομμύρια αντίτυπα μόνο στις ΗΠΑ."
    ],
    "source": "https://en.wikipedia.org/wiki/Tarzan_(1999_film)",
    "locale": "el-GR",
    "tags": ["tarzan", "disney", "phil_collins", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_193",
    "text": "Από ποια θρυλική παγίδα τρέχει να γλιτώσει ο Indiana Jones στην αρχή της ταινίας 'Οι Κυνηγοί της Χαμένης Κιβωτού' (1981);",
    "answers": [
      "Από έναν γιγάντιο κυλιόμενο βράχο",
      "Από έναν λάκκο με φίδια",
      "Από έναν καταρράκτη λάβας",
      "Από βέλη με δηλητήριο"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Αφού αρπάζει το χρυσό είδωλο, ο Indiana Jones ενεργοποιεί την παγίδα και καταδιώκεται από έναν τεράστιο σφαιρικό βράχο.",
    "funFacts": [
      "Ο τεχνητός βράχος ήταν κατασκευασμένος από υαλοβάμβακα και είχε διάμετρο άνω των δύο μέτρων.",
      "Η σκηνή αυτή έχει παρωδηθεί και αντιγραφεί σε αμέτρητες ταινίες, κινούμενα σχέδια και βιντεοπαιχνίδια."
    ],
    "source": "https://en.wikipedia.org/wiki/Raiders_of_the_Lost_Ark",
    "locale": "el-GR",
    "tags": ["indiana_jones", "cinema", "spielberg", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_194",
    "text": "Ποιο πολυβραβευμένο άλμπουμ του 2006 εκτόξευσε την Amy Winehouse στην παγκόσμια δόξα με επιτυχίες όπως το 'Rehab';",
    "answers": [
      "Frank",
      "Back to Black",
      "Lioness",
      "Back to Life"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το άλμπουμ 'Back to Black' κέρδισε πέντε βραβεία Grammy σε μία μόνο βραδιά και καθιέρωσε την Amy Winehouse ως κορυφαία soul φωνή.",
    "funFacts": [
      "Το χαρακτηριστικό στυλ της με τα έντονα eyeliners και το χτένισμα 'beehive' έγινε μόδα και σήμα κατατεθέν της εποχής.",
      "Το 'Back to Black' έγινε ένα από τα βρετανικά άλμπουμ με τις μεγαλύτερες πωλήσεις στον 21ο αιώνα."
    ],
    "source": "https://en.wikipedia.org/wiki/Back_to_Black",
    "locale": "el-GR",
    "tags": ["amy_winehouse", "music", "soul", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_195",
    "text": "Ποιον ρόλο πρακτικής μαμής υποδύθηκε η Γεωργία Βασιλειάδου στην κλασική κωμωδία 'Η κυρά μας η μαμή' (1958);",
    "answers": [
      "Καλλιόπη",
      "Ευτυχία",
      "Κυρά-Μαρία",
      "Ασημίνα"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Γεωργία Βασιλειάδου έπαιξε την κυρά-Μαρία, τη μαμή του χωριού Λεσκοβίτσι που συγκρούεται με τον νέο επιστήμονα γιατρό (Ορέστης Μακρής).",
    "funFacts": [
      "Η σκηνή με το ξεμάτιασμα της μαμής με το λάδι και το νερό είναι μία από τις πιο κλασικές της ελληνικής κωμωδίας.",
      "Τη σκηνοθεσία και το σενάριο υπέγραψε ο Αλέκος Σακελλάριος για τη Φίνος Φιλμ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%BA%CF%85%CF%81%CE%AC_%CE%BC%CE%B1%CF%82_%CE%B7_%CE%BC%CE%B1%CE%BC%CE%AE",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vasileiadou", "makris", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_196",
    "text": "Ποιο είναι το ιδιαίτερο χαρακτηριστικό του αντιήρωα Deadpool (Ryan Reynolds) που τον κάνει να επικοινωνεί κατευθείαν με το κοινό;",
    "answers": [
      "Έχει τηλεπαθητικές δυνάμεις",
      "Μιλάει όλες τις γλώσσες του κόσμου",
      "Χρησιμοποιεί μαγικό καθρέφτη",
      "Σπάει τον τέταρτο τοίχο (Fourth Wall)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Deadpool γνωρίζει ότι είναι φανταστικός χαρακτήρας κόμικ και ταινίας και 'σπάει τον τέταρτο τοίχο' σχολιάζοντας τα γεγονότα απευθείας στους θεατές.",
    "funFacts": [
      "Η ταινία 'Deadpool & Wolverine' (2024) έγινε η πιο κερδοφόρα ταινία με σήμανση καταλληλότητας R-rated στην ιστορία του κινηματογράφου.",
      "Το αγαπημένο φαγητό που αναφέρει διαρκώς ο Deadpool είναι τα chimichangas."
    ],
    "source": "https://en.wikipedia.org/wiki/Deadpool_(film)",
    "locale": "el-GR",
    "tags": ["deadpool", "marvel", "ryan_reynolds", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_197",
    "text": "Ποιος Ιάπωνας δημιουργός σκηνοθέτησε το αριστούργημα κινουμένων σχεδίων 'Ταξίδι στη Χώρα των Θαυμάτων' (Spirited Away, 2001);",
    "answers": [
      "Χαγιάο Μιγιαζάκι",
      "Ισάο Τακαχάτα",
      "Μακότο Σινκάι",
      "Σατόσι Κον"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Hayao Miyazaki του Studio Ghibli δημιούργησε την ιστορία της μικρής Chihiro στον μαγικό κόσμο των πνευμάτων.",
    "funFacts": [
      "Το Spirited Away παραμένει η μοναδική μη αγγλόφωνη ταινία σχεδιασμένη στο χέρι που κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων.",
      "Υπήρξε για σχεδόν 19 χρόνια η πιο εμπορική ταινία στην ιστορία του ιαπωνικού box office."
    ],
    "source": "https://en.wikipedia.org/wiki/Spirited_Away",
    "locale": "el-GR",
    "tags": ["spirited_away", "miyazaki", "studio_ghibli", "anime"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_198",
    "text": "Ποιος είναι ο εγκέφαλος πίσω από τις παράτολμες ληστείες στην ισπανική σειρά 'La Casa de Papel';",
    "answers": [
      "Ο Μπερλίν",
      "Ο Καθηγητής (El Profesor)",
      "Ο Παλέρμο",
      "Ο Ντένβερ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Sergio Marquina, γνωστός ως 'El Profesor' (Άλβαρο Μόρτε), σχεδιάζει κάθε λεπτομέρεια των ληστειών προβλέποντας κάθε κίνηση της αστυνομίας.",
    "funFacts": [
      "Η χαρακτηριστική κίνηση του Καθηγητή να διορθώνει τα γυαλιά του στη μύτη με τον δείκτη ήταν προσωπική επιλογή του ηθοποιού Álvaro Morte.",
      "Η σειρά απέκτησε εκατομμύρια φανατικούς οπαδούς παγκοσμίως όταν εντάχθηκε στον κατάλογο του Netflix."
    ],
    "source": "https://en.wikipedia.org/wiki/Professor_(Money_Heist)",
    "locale": "el-GR",
    "tags": ["la_casa_de_papel", "el_profesor", "netflix", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_199",
    "text": "Ποιο ιστορικό ροκ συγκρότημα κυκλοφόρησε το θρυλικό άλμπουμ 'Rumours' (1977) με επιτυχίες όπως το 'Dreams' και το 'Go Your Own Way';",
    "answers": [
      "The Eagles",
      "Fleetwood Mac",
      "Blondie",
      "Heart"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι Fleetwood Mac (Stevie Nicks, Lindsey Buckingham, Christine McVie, John McVie, Mick Fleetwood) δημιούργησαν ένα από τα πιο επιτυχημένα άλμπουμ όλων των εποχών.",
    "funFacts": [
      "Το άλμπουμ γράφτηκε εν μέσω έντονων προσωπικών χωρισμών ανάμεσα σε όλα τα μέλη του συγκροτήματος, κάτι που αποτυπώθηκε στους στίχους.",
      "Το 'Rumours' έχει πουλήσει πάνω από 40 εκατομμύρια αντίτυπα παγκοσμίως."
    ],
    "source": "https://en.wikipedia.org/wiki/Rumours_(album)",
    "locale": "el-GR",
    "tags": ["fleetwood_mac", "rumours", "rock", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_200",
    "text": "Τι χρώμα έχουν οι χαρακτήρες ψηφιακού κώδικα που πέφτουν σαν βροχή στην οθόνη στην τριλογία 'The Matrix';",
    "answers": [
      "Μπλε",
      "Κόκκινο",
      "Κίτρινο",
      "Πράσινο"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο πράσινος ψηφιακός κώδικας (digital rain) σε μαύρο φόντο αποτελεί το απόλυτο οπτικό σύμβολο του Matrix.",
    "funFacts": [
      "Ο σχεδιαστής του εφέ Simon Whiteley αποκάλυψε ότι τα σύμβολα του κώδικα ήταν στην πραγματικότητα γιαπωνέζικοι χαρακτήρες kana από βιβλία μαγειρικής σούσι της συζύγου του.",
      "Το εφέ αναπαριστά τη δραστηριότητα του εικονικού περιβάλλοντος προσομοίωσης του Matrix."
    ],
    "source": "https://en.wikipedia.org/wiki/Matrix_digital_rain",
    "locale": "el-GR",
    "tags": ["the_matrix", "cinema", "sci_fi", "effects"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_201",
    "text": "Ποια είναι η ατρόμητη Βρετανίδα αρχαιολόγος και πρωταγωνίστρια της σειράς βιντεοπαιχνιδιών 'Tomb Raider';",
    "answers": [
      "Lara Croft",
      "Jill Valentine",
      "Elena Fisher",
      "Claire Redfield"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Lara Croft είναι η διάσημη αρχαιολόγος και τυχοδιώκτρια που εξερευνά αρχαίους τάφους και ερείπια οπλισμένη με τα δίδυμα πιστόλια της.",
    "funFacts": [
      "Η Lara Croft μπήκε στο Βιβλίο των Ρεκόρ Γκίνες ως η πιο επιτυχημένη ηρωίδα στην ιστορία των βιντεοπαιχνιδιών.",
      "Στον κινηματογράφο την υποδύθηκε για πρώτη φορά η Angelina Jolie το 2001."
    ],
    "source": "https://en.wikipedia.org/wiki/Lara_Croft",
    "locale": "el-GR",
    "tags": ["tomb_raider", "lara_croft", "gaming", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_202",
    "text": "Ανάμεσα σε ποιες δύο οικογένειες μαίνεται η βεντέτα στην καθηλωτική κρητική σειρά 'Σασμός' του Alpha;",
    "answers": [
      "Σεβαστών και Σταμίρη",
      "Σταματάκηδων και Βρουλάκηδων",
      "Τριαντάφυλλων και Χαμπέων",
      "Φουρτουνάκηδων και Βροντάκηδων"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η δραματική σειρά 'Σασμός' βασίστηκε στο μυθιστόρημα του Σπύρου Πετρουλάκη και εστιάζει στη μακρόχρονη βεντέτα των οικογενειών Σταματάκη και Βρουλάκη.",
    "funFacts": [
      "Η κρητική λέξη 'σασμός' σημαίνει τη συμφιλίωση και το σιάξιμο (συμφιλίωση των οικογενειών για να σταματήσει μια βεντέτα).",
      "Η σειρά προβλήθηκε για τρεις σεζόν στον Alpha γνωρίζοντας τεράστια επιτυχία και υψηλή τηλεθέαση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CF%83%CE%BC%CF%8C%CF%82_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["sasmos", "greek_tv", "drama", "alpha"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_203",
    "text": "Ως ποιο ζώο απεικονίζεται ο Ρομπέν των Δασών στην ομώνυμη κλασική ταινία της Disney (1973);",
    "answers": [
      "Λύκος",
      "Αρκούδα",
      "Κόκκινη αλεπού",
      "Λιοντάρι"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στην κλασική animated εκδοχή της Disney, ο Robin Hood είναι μια πονηρή αλλά ευγενική κόκκινη αλεπού που κλέβει από τους πλούσιους για να δώσει στους φτωχούς.",
    "funFacts": [
      "Ο κακός Πρίγκιπας Ιωάννης (Prince John) σχεδιάστηκε ως ένα ανώριμο λιοντάρι χωρίς χαίτη που πιπιλάει τον αντίχειρά του.",
      "Η ταινία επαναχρησιμοποίησε ακριβή animation πλάνα χορού από παλαιότερες ταινίες της Disney όπως το 'The Jungle Book' και 'The Aristocats'."
    ],
    "source": "https://en.wikipedia.org/wiki/Robin_Hood_(1973_film)",
    "locale": "el-GR",
    "tags": ["robin_hood", "disney", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_204",
    "text": "Ποιο θαλάσσιο πλάσμα τρομοκρατεί τους λουόμενους στο νησί Amity στην ταινία 'Τα Σαγόνια του Καρχαρία' (Jaws, 1975);",
    "answers": [
      "Γιγάντιο καλαμάρι",
      "Όρκα (φάλαινα δολοφόνος)",
      "Σφυροκέφαλος καρχαρίας",
      "Μεγάλος λευκός καρχαρίας"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο σκηνοθέτης Steven Spielberg δημιούργησε το πρώτο καλοκαιρινό blockbuster με θέμα έναν γιγάντιο μεγάλο λευκό καρχαρία.",
    "funFacts": [
      "Η ατάκα 'You're gonna need a bigger boat' ήταν αυτοσχεδιασμός του ηθοποιού Roy Scheider.",
      "Το μηχανικό ρομπότ καρχαρία στα γυρίσματα χάλαγε τόσο συχνά που ο Spielberg αναγκάστηκε να υποδηλώνει την παρουσία του με μουσική και επιπλέοντα βαρέλια, κάνοντας την ταινία ακόμα πιο τρομακτική."
    ],
    "source": "https://en.wikipedia.org/wiki/Jaws_(film)",
    "locale": "el-GR",
    "tags": ["jaws", "cinema", "spielberg", "sharks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_205",
    "text": "Με ποιο εφηβικό single του 2010 εκτοξεύτηκε στην παγκόσμια μουσική κορυφή ο Justin Bieber;",
    "answers": [
      "Baby",
      "Sorry",
      "Boyfriend",
      "What Do You Mean?"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι 'Baby' με τη συμμετοχή του Ludacris έκανε τον Καναδό Justin Bieber παγκόσμιο φαινόμενο της ποπ σε ηλικία μόλις 16 ετών.",
    "funFacts": [
      "Ο Justin Bieber ανακαλύφθηκε το 2008 από τον μάνατζερ Scooter Braun μέσα από ερασιτεχνικά βίντεο διασκευών που ανέβαζε η μητέρα του στο YouTube.",
      "Το βίντεο του 'Baby' υπήρξε για χρόνια το βίντεο με τις περισσότερες θεάσεις στην ιστορία του YouTube."
    ],
    "source": "https://en.wikipedia.org/wiki/Baby_(Justin_Bieber_song)",
    "locale": "el-GR",
    "tags": ["justin_bieber", "music", "pop", "youtube"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_206",
    "text": "Σε ποιο ελληνικό νησί εκτυλίσσεται η κλασική κωμωδία 'Το Δόλωμα' (1964) με την Αλίκη Βουγιουκλάκη;",
    "answers": [
      "Στην Κέρκυρα",
      "Στη Ρόδο",
      "Στην Κρήτη",
      "Στη Μύκονο"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η συμμορία των χαρτοκλεφτών με επικεφαλής τον Αλέκο Αλεξανδράκη και τον Ντίνο Ηλιόπουλο χρησιμοποιεί την Καίτη (Αλίκη Βουγιουκλάκη) ως 'δόλωμα' στα πολυτελή ξενοδοχεία της Ρόδου.",
    "funFacts": [
      "Στην ταινία η Αλίκη Βουγιουκλάκη τραγουδά το διαχρονικό 'Άστο το χεράκι σου' σε μουσική Μάνου Χατζιδάκι.",
      "Η ταινία αποτέλεσε τεράστια τουριστική διαφήμιση για το νησί των Ιπποτών τη δεκαετία του 1960."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%B4%CF%8C%CE%BB%CF%89%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vougiouklaki", "rhodes", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_207",
    "text": "Ποιο είναι το επίσημο όνομα του αξιολάτρευτου πράσινου πλάσματος που οι θεατές αποκαλούσαν αρχικά 'Baby Yoda' στη σειρά 'The Mandalorian';",
    "answers": [
      "Yaddle",
      "Din Djarin",
      "Grogu (Γκρόγκου)",
      "Ezra"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το πραγματικό όνομα του μυστηριώδους παιδιού αποκαλύφθηκε στη δεύτερη σεζόν της σειράς ότι είναι Grogu.",
    "funFacts": [
      "Το Grogu χειρίζεται ως φυσική animatronic μαριονέτα στα γυρίσματα που κόστισε περίπου 5 εκατομμύρια δολάρια.",
      "Η διάσημη ατάκα των Μανταλοριανών στη σειρά είναι το 'This is the Way' (Αυτός είναι ο Δρόμος)."
    ],
    "source": "https://en.wikipedia.org/wiki/Grogu",
    "locale": "el-GR",
    "tags": ["the_mandalorian", "star_wars", "grogu", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_208",
    "text": "Ποιο μαγικό αξίωμα κατέχει ο Stephen Strange στο Κινηματογραφικό Σύμπαν της Marvel;",
    "answers": [
      "Master of Illusions",
      "Grand Enchanter",
      "Lord of the Mystic Arts",
      "Sorcerer Supreme (Υπέρτατος Μάγος)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο πρώην νευροχειρουργός Stephen Strange (Benedict Cumberbatch) εκπαιδεύεται στο Kamar-Taj και γίνεται ο Sorcerer Supreme.",
    "funFacts": [
      "Ο Doctor Strange φορά τον Μανδύα της Αιώρησης (Cloak of Levitation), ο οποίος διαθέτει δική του συνείδηση και προσωπικότητα.",
      "Το φυλαχτό του, το 'Μάτι του Αγκαμότο', περιείχε αρχικά την Πέτρα του Χρόνου (Time Stone)."
    ],
    "source": "https://en.wikipedia.org/wiki/Doctor_Strange_(2016_film)",
    "locale": "el-GR",
    "tags": ["doctor_strange", "marvel", "mcu", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_209",
    "text": "Ποιο συναίσθημα ηγείται των υπολοίπων στο κέντρο ελέγχου του μυαλού της Riley στην ταινία 'Τα Μυαλά που Πονάνε' (Inside Out, 2015);",
    "answers": [
      "Η Χαρά (Joy)",
      "Η Λύπη (Sadness)",
      "Ο Θυμός (Anger)",
      "Ο Φόβος (Fear)"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Χαρά (Joy) είναι το πρώτο και βασικό συναίσθημα που καθοδηγεί τη μικρή Riley πριν μάθει να αποδέχεται και την αξία της Λύπης.",
    "funFacts": [
      "Κάθε συναίσθημα σχεδιάστηκε με βάση ένα συγκεκριμένο σχήμα: η Χαρά μοιάζει με αστέρι, η Λύπη με δάκρυ και ο Θυμός με συμπαγές τούβλο.",
      "Η ταινία κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2016."
    ],
    "source": "https://en.wikipedia.org/wiki/Inside_Out_(2015_film)",
    "locale": "el-GR",
    "tags": ["inside_out", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_210",
    "text": "Ποιο κλασικό rock 'n' roll τραγούδι παίζει στην κιθάρα ο Marty McFly στον σχολικό χορό του 1955 στο 'Back to the Future';",
    "answers": [
      "Rock Around the Clock",
      "Johnny B. Goode",
      "Jailhouse Rock",
      "Hound Dog"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Marty McFly (Michael J. Fox) παίζει στην κιθάρα το 'Johnny B. Goode' του Chuck Berry τρία χρόνια πριν αυτό γραφτεί στην πραγματικότητα.",
    "funFacts": [
      "Στη σκηνή, ο μουσικός Marvin Berry τηλεφωνεί στον ξάδελφό του Chuck Berry λέγοντάς του: 'Chuck! It's Marvin. Your cousin, Marvin Berry. You know that new sound you're looking for? Well, listen to this!'.",
      "Η ταινία του Robert Zemeckis έγινε η πιο επιτυχημένη εισπρακτικά ταινία του 1985 παγκοσμίως."
    ],
    "source": "https://en.wikipedia.org/wiki/Back_to_the_Future",
    "locale": "el-GR",
    "tags": ["back_to_the_future", "cinema", "rock_and_roll", "michael_j_fox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'easy', 1, questions)

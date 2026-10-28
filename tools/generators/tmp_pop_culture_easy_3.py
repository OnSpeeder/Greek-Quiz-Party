# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_easy_111",
    "text": "Από ποιο άφθαρτο φανταστικό μέταλλο είναι κατασκευασμένα τα νύχια και ο σκελετός του Wolverine στα X-Men;",
    "answers": [
      "Αδαμάντιο (Adamantium)",
      "Βιβράνιο (Vibranium)",
      "Κρυπτονίτης",
      "Μιθρίλ"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Wolverine (Logan) απέκτησε σκελετό και πτυσσόμενα νύχια ενισχυμένα με αδαμάντιο κατά τη διάρκεια του μυστικού πειράματος Weapon X.",
    "funFacts": [
      "Τον Wolverine υποδύθηκε για πάνω από δύο δεκαετίες στον κινηματογράφο ο Αυστραλός ηθοποιός Hugh Jackman.",
      "Το αδαμάντιο στα κόμικς της Marvel θεωρείται σχεδόν εντελώς άφθαρτο μετά τη στερεοποίησή του."
    ],
    "source": "https://en.wikipedia.org/wiki/Wolverine_(character)",
    "locale": "el-GR",
    "tags": ["x_men", "marvel", "wolverine", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_112",
    "text": "Τι συμβαίνει στη μύτη του Πινόκιο στην κλασική ταινία της Disney (1940) κάθε φορά που λέει ψέματα;",
    "answers": [
      "Αλλάζει χρώμα σε μπλε",
      "Μακραίνει",
      "Βγάζει καπνό",
      "Εξαφανίζεται"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η μύτη της ξύλινης μαριονέτας του Τζεπέτο μεγαλώνει ανεξέλεγκτα κάθε φορά που προσπαθεί να πει ψέματα στη Γαλάζια Νεράιδα.",
    "funFacts": [
      "Η φράση 'μεγαλώνει η μύτη σου' έχει γίνει παγκόσμια έκφραση που υποδηλώνει ότι κάποιος λέει ψέματα.",
      "Η ταινία βασίστηκε στο κλασικό ιταλικό παραμύθι του Κάρλο Κολόντι 'Οι περιπέτειες του Πινόκιο' (1883)."
    ],
    "source": "https://en.wikipedia.org/wiki/Pinocchio_(1940_film)",
    "locale": "el-GR",
    "tags": ["pinocchio", "disney", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_113",
    "text": "Ποια διάσημη δικαιολογία επαναλάμβανε συνεχώς ο Ross Geller για τον χωρισμό του με τη Rachel στη σειρά 'Τα Φιλαράκια';",
    "answers": [
      "Ήταν απλώς ένα ατύχημα",
      "Δεν το εννοούσα ποτέ",
      "We were on a break! (Είχαμε κάνει διάλειμμα!)",
      "Μου το ζήτησε η Μόνικα"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'We were on a break!' έγινε μία από τις πιο αναγνωρίσιμες και αστείες φράσεις στην ιστορία της τηλεόρασης, διχάζοντας τους θαυμαστές της σειράς.",
    "funFacts": [
      "Η διαμάχη για το αν ο Ross και η Rachel ήταν πράγματι 'on a break' συνεχίστηκε ως αστείο μέχρι και το τελευταίο επεισόδιο της σειράς.",
      "Η σχέση του Ross και της Rachel κράτησε σε αγωνία τους τηλεθεατές για 10 ολόκληρες σεζόν."
    ],
    "source": "https://en.wikipedia.org/wiki/Friends",
    "locale": "el-GR",
    "tags": ["friends", "tv", "sitcom", "quotes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_114",
    "text": "Ποια σπουδαία κωμικός πρωταγωνίστησε στην κλασική ταινία 'Μια Ελληνίδα στο χαρέμι' (1971) υποδυόμενη τη μέντιουμ 'Ρένα';",
    "answers": [
      "Γεωργία Βασιλειάδου",
      "Μαίρη Αρώνη",
      "Σαπφώ Νοταρά",
      "Ρένα Βλαχοπούλου"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Ρένα Βλαχοπούλου χάρισε ανεπανάληπτες κωμικές σκηνές ως ψευτο-μέντιουμ που καταλήγει κατά λάθος στο χαρέμι ενός εμίρη.",
    "funFacts": [
      "Η σκηνή όπου η Ρένα Βλαχοπούλου λιποθυμά στο μικρό αεροπλάνο φωνάζοντας 'Βαγγέλη!' παραμένει μία από τις πιο γνωστές της ελληνικής κωμωδίας.",
      "Η ταινία γυρίστηκε από τη Φίνος Φιλμ σε σκηνοθεσία Γιάννη Δαλιανίδη με εξωτερικά γυρίσματα και στα Χανιά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CE%95%CE%BB%CE%BB%CE%B7%CE%BD%CE%AF%CE%B4%CE%B1_%CF%83%CF%84%CE%BF_%CF%87%CE%B1%CF%81%CE%AD%CE%BC%CE%B9",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vlachopoulou", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_115",
    "text": "Ποια ποπ σταρ της δεκαετίας του 1990 έγινε παγκόσμιο είδωλο με το ντεμπούτο single '...Baby One More Time' (1998);",
    "answers": [
      "Britney Spears",
      "Christina Aguilera",
      "Jessica Simpson",
      "Mandy Moore"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Britney Spears κατέκτησε την κορυφή των charts παγκοσμίως στα 16 της χρόνια με το τραγούδι '...Baby One More Time'.",
    "funFacts": [
      "Το μουσικό βίντεο κλιπ με τη στολή μαθήτριας γυρίστηκε στο ίδιο σχολείο όπου είχε γυριστεί η ταινία 'Grease'.",
      "Το single πούλησε πάνω από 10 εκατομμύρια αντίτυπα και είναι ένα από τα πιο επιτυχημένα ντεμπούτα όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/...Baby_One_More_Time_(song)",
    "locale": "el-GR",
    "tags": ["britney_spears", "music", "pop", "90s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_116",
    "text": "Τι χρώμα φωτόσπαθο κατασκεύασε και κρατά ο Luke Skywalker στην ταινία 'Η Επιστροφή των Τζεντάι' (Return of the Jedi);",
    "answers": [
      "Μπλε",
      "Πράσινο",
      "Κόκκινο",
      "Μοβ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Αφού έχασε το μπλε φωτόσπαθο του πατέρα του στο Cloud City, ο Luke κατασκεύασε ένα νέο φωτόσπαθο με πράσινη λεπίδα.",
    "funFacts": [
      "Το χρώμα άλλαξε σε πράσινο κατά τα γυρίσματα επειδή το μπλε φωτόσπαθο δεν ξεχώριζε καλά απέναντι στον καταγάλανο ουρανό της ερήμου.",
      "Το μοναδικό μοβ φωτόσπαθο στην αρχική εξαλογία άνηκε στον Mace Windu κατόπιν προσωπικού αιτήματος του Samuel L. Jackson."
    ],
    "source": "https://en.wikipedia.org/wiki/Lightsaber",
    "locale": "el-GR",
    "tags": ["star_wars", "luke_skywalker", "cinema", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_117",
    "text": "Ποιος είναι ο απαράβατος κανόνας της εκκεντρικής σχεδιάστριας στολών Edna Mode στην ταινία 'Οι Απίθανοι' (The Incredibles);",
    "answers": [
      "Ποτέ μαύρο χρώμα",
      "Ποτέ εφαρμοστές μάσκες",
      "Όχι κάπες! (No capes!)",
      "Ποτέ βαριά υφάσματα"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Edna Mode αρνείται κατηγορηματικά να προσθέσει κάπες στις στολές υπερηρώων, υπενθυμίζοντας θανατηφόρα ατυχήματα του παρελθόντος.",
    "funFacts": [
      "Τη φωνή της Edna Mode στην πρωτότυπη ταινία έκανε ο ίδιος ο σκηνοθέτης της ταινίας Brad Bird.",
      "Η ταινία The Incredibles της Pixar κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2005."
    ],
    "source": "https://en.wikipedia.org/wiki/Edna_Mode",
    "locale": "el-GR",
    "tags": ["the_incredibles", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_118",
    "text": "Ποια είναι η πιο διάσημη ειδική επίθεση ενέργειας των πολεμιστών Ryu και Ken στη σειρά βιντεοπαιχνιδιών 'Street Fighter';",
    "answers": [
      "Shoryuken",
      "Sonic Boom",
      "Tiger Uppercut",
      "Hadouken"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Hadouken (Κύμα Γροθιάς) είναι η χαρακτηριστική μπλε ενεργειακή σφαίρα που εκτοξεύουν οι Ryu και Ken από τις παλάμες τους.",
    "funFacts": [
      "Η φράση 'Hadouken' αποτελεί μία από τις πιο αναγνωρίσιμες ηχητικές ατάκες στην ιστορία των ηλεκτρονικών παιχνιδιών.",
      "Το Street Fighter II (1991) καθόρισε και διαμόρφωσε ολόκληρο το σύγχρονο είδος των competitive fighting games."
    ],
    "source": "https://en.wikipedia.org/wiki/Hadouken",
    "locale": "el-GR",
    "tags": ["street_fighter", "capcom", "gaming", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_119",
    "text": "Ποια αδίστακτη αλλά κωμική δολοφόνο υποδύθηκε η Καίτη Κωνσταντίνου στη μαύρη κωμωδία του ΑΝΤ1 'Εγκλήματα';",
    "answers": [
      "Σωσώ Παπαδήμα",
      "Κορίνα Μητροπούλου",
      "Φλώρα Καρασούμπα",
      "Πέπη"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Σωσώ Παπαδήμα έγινε ένας από τους πιο λατρεμένους καλτ χαρακτήρες της ελληνικής τηλεόρασης, καταστρώνοντας συνεχώς δολοφονικά σχέδια κατά του συζύγου της Αλέκου.",
    "funFacts": [
      "Η ατάκα της 'Αλέκο, ο σολομός!' και οι δηλητηριώδεις της ατάκες έγιναν viral στην ελληνική ποπ κουλτούρα.",
      "Το σενάριο της σειράς έγραψε ο Λευτέρης Παπαπέτρου, γνωρίζοντας τεράστια επιτυχία τις σεζόν 1998-2000."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["eglimata", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_120",
    "text": "Τι αντικείμενο ήταν ο 'Wilson', ο μοναδικός σιωπηλός φίλος του Tom Hanks στην ταινία 'Ο Ναυαγός' (Cast Away);",
    "answers": [
      "Μια ξύλινη σανίδα",
      "Μια μπάλα βόλεϊ",
      "Μια καρύδα με πρόσωπο",
      "Ένα ρολόι τσέπης"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Chuck Noland (Tom Hanks) σχεδίασε ένα πρόσωπο με το ματωμένο του αποτύπωμα πάνω σε μια μπάλα βόλεϊ της εταιρείας Wilson και της μιλούσε για να μη χάσει τα λογικά του.",
    "funFacts": [
      "Η αυθεντική μπάλα βόλεϊ που χρησιμοποιήθηκε στην ταινία πωλήθηκε σε δημοπρασία έναντι άνω των 300.000 δολαρίων.",
      "Ο Tom Hanks έχασε περίπου 25 κιλά και άφησε πυκνά μαλλιά και γένια κατά τη διάρκεια ενός διαλείμματος των γυρισμάτων για να δείχνει πειστικός ναυαγός."
    ],
    "source": "https://en.wikipedia.org/wiki/Cast_Away",
    "locale": "el-GR",
    "tags": ["cast_away", "tom_hanks", "cinema", "hollywood"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_121",
    "text": "Ποιο συγκινητικό τραγούδι επανεκτέλεσε ο Elton John στην κηδεία της πριγκίπισσας Νταϊάνα το 1997;",
    "answers": [
      "Your Song",
      "Rocket Man",
      "Candle in the Wind 1997",
      "Tiny Dancer"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Candle in the Wind 1997' (Goodbye England's Rose) γράφτηκε προς τιμήν της εκλιπούσας φίλης του πριγκίπισσας Νταϊάνα.",
    "funFacts": [
      "Το single έγινε το δεύτερο σε πωλήσεις single όλων των εποχών παγκοσμίως (μετά το 'White Christmas' του Bing Crosby), ξεπερνώντας τα 33 εκατομμύρια αντίτυπα.",
      "Όλα τα κέρδη από τις πωλήσεις του τραγουδιού διατέθηκαν στο φιλανθρωπικό ίδρυμα της πριγκίπισσας Diana."
    ],
    "source": "https://en.wikipedia.org/wiki/Candle_in_the_Wind_1997",
    "locale": "el-GR",
    "tags": ["elton_john", "princess_diana", "music", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_122",
    "text": "Πώς ονομάζεται ο πιστός μπάτλερ και πατρική φιγούρα του Bruce Wayne στην έπαυλη του Batman;",
    "answers": [
      "Jim Gordon",
      "Lucius Fox",
      "Harvey Dent",
      "Alfred Pennyworth"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Alfred Pennyworth φροντίζει τον Bruce Wayne, επουλώνει τα τραύματά του και διαχειρίζεται τα μυστικά της Batcave.",
    "funFacts": [
      "Πριν γίνει μπάτλερ της οικογένειας Wayne, ο Alfred στα περισσότερα κόμικς υπηρέτησε ως πράκτορας των βρετανικών μυστικών υπηρεσιών (MI6).",
      "Στον κινηματογράφο τον έχουν υποδυθεί σπουδαίοι ηθοποιοί όπως ο Michael Caine, ο Michael Gough και ο Andy Serkis."
    ],
    "source": "https://en.wikipedia.org/wiki/Alfred_Pennyworth",
    "locale": "el-GR",
    "tags": ["batman", "dc_comics", "alfred", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_123",
    "text": "Ποιος είναι ο μεγαλύτερος και πιο πιστός δράκος της Daenerys Targaryen στη σειρά 'Game of Thrones';",
    "answers": [
      "Drogon",
      "Rhaegal",
      "Viserion",
      "Balerion"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Drogon πήρε το όνομά του από τον εκλιπόντα σύζυγο της Daenerys, Khal Drogo, και διακρίνεται για τα μαύρα και κόκκινα λέπια του.",
    "funFacts": [
      "Η λέξη 'Dracarys' στην υψηλή βαλυριανή γλώσσα ήταν η εντολή που έδινε η Daenerys στους δράκους της για να εκτοξεύσουν φωτιά.",
      "Στο φινάλε της σειράς, ο Drogon λιώνει τον Σιδερένιο Θρόνο με την καυτή ανάσα του πριν απομακρυνθεί πετώντας."
    ],
    "source": "https://en.wikipedia.org/wiki/Daenerys_Targaryen",
    "locale": "el-GR",
    "tags": ["game_of_thrones", "drogon", "dragons", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_124",
    "text": "Ποιο είδος ζώου είναι ο Po που προορίζεται να γίνει ο 'Δράκος Πολεμιστής' στην ταινία 'Kung Fu Panda';",
    "answers": [
      "Κόκκινη πάντα",
      "Γιγάντια πάντα",
      "Τίγρης",
      "Λεοπάρδαλη του χιονιού"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Po είναι μια αδέξια, λαίμαργη γιγάντια πάντα που εργάζεται στο εστιατόριο νουντλς του θετού πατέρα του πριν επιλεγεί για το Κουνγκ Φου.",
    "funFacts": [
      "Τη φωνή του Po στην αμερικανική εκδοχή δάνεισε απολαυστικά ο Jack Black.",
      "Η ταινία της DreamWorks (2008) σημείωσε τεράστια επιτυχία και απέσπασε υποψηφιότητα για Όσκαρ."
    ],
    "source": "https://en.wikipedia.org/wiki/Kung_Fu_Panda",
    "locale": "el-GR",
    "tags": ["kung_fu_panda", "dreamworks", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_125",
    "text": "Ποιοι ήταν οι δύο βασικοί ερωτευμένοι πρωταγωνιστές της κλασικής κωμικής σειράς του Mega 'Ντόλτσε Βίτα';",
    "answers": [
      "Μαρίνα και Κωνσταντίνος",
      "Στέλλα και Σωτήρης",
      "Χριστίνα Μαρκάτου και Αντώνης Καλούδης",
      "Ελένη και Κωνσταντίνος"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Άννα Παναγιωτοπούλου (Χριστίνα) και ο Θανάσης Ευθυμιάδης (Αντώνης) ενσάρκωσαν το παράνομο ζευγάρι που γνωρίστηκε στην Περούτζια της Ιταλίας.",
    "funFacts": [
      "Ο χαρακτήρας της οικιακής βοηθού 'Ασπασίας' που υποδύθηκε η Μαρία Καβογιάννη άφησε εποχή με τις ξεκαρδιστικές της σκηνές.",
      "Η σειρά των Αλέξανδρου Ρήγα και Λευτέρη Παπαπέτρου προβλήθηκε τις σεζόν 1995-1997 σημειώνοντας τεράστια νούμερα τηλεθέασης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CF%8C%CE%BB%CF%84%CF%83%CE%B5_%CE%92%CE%AF%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["dolce_vita", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_126",
    "text": "Ποιος είναι ο διάσημος μυστικός πράκτορας της IMF που υποδύεται ο Tom Cruise στη σειρά ταινιών 'Επικίνδυνη Αποστολή' (Mission: Impossible);",
    "answers": [
      "Jason Bourne",
      "Jack Reacher",
      "James Bond",
      "Ethan Hunt"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ethan Hunt είναι ο κορυφαίος πράκτορας της Impossible Missions Force (IMF) που αναλαμβάνει τις πιο επικίνδυνες αποστολές.",
    "funFacts": [
      "Ο Tom Cruise είναι παγκοσμίως διάσημος επειδή εκτελεί μόνος του τα περισσότερα επικίνδυνα ακροβατικά, όπως το κρέμασμα από το Burj Khalifa και από αεροπλάνο εν πτήσει.",
      "Το διάσημο μουσικό θέμα της σειράς γράφτηκε αρχικά από τον Lalo Schifrin σε ασυνήθιστο ρυθμό 5/4."
    ],
    "source": "https://en.wikipedia.org/wiki/Ethan_Hunt",
    "locale": "el-GR",
    "tags": ["mission_impossible", "tom_cruise", "cinema", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_127",
    "text": "Ποιο τραγούδι της Billie Eilish έγινε παγκόσμιο φαινόμενο το 2019 με τη χαρακτηριστική ψιθυριστή ατάκα 'I'm the bad guy, duh';",
    "answers": [
      "Bad Guy",
      "Ocean Eyes",
      "Happier Than Ever",
      "Bury a Friend"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Bad Guy' εκτόξευσε την Billie Eilish στην κορυφή του Billboard Hot 100 και κέρδισε τα βραβεία Grammy Τραγουδιού και Ηχογράφησης της Χρονιάς.",
    "funFacts": [
      "Η Billie Eilish έγραψε και ηχογράφησε το μεγαλύτερο μέρος του πρώτου της άλμπουμ στο υπνοδωμάτιο του σπιτιού της μαζί με τον αδελφό της Finneas.",
      "Έγινε η νεότερη καλλιτέχνιδα στην ιστορία που κέρδισε και τις τέσσερις κύριες γενικές κατηγορίες των βραβείων Grammy σε μία μόνο χρονιά."
    ],
    "source": "https://en.wikipedia.org/wiki/Bad_Guy_(Billie_Eilish_song)",
    "locale": "el-GR",
    "tags": ["billie_eilish", "music", "pop", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_128",
    "text": "Πώς ονομάζεται το πολύχρωμο φορτηγάκι με το οποίο ταξιδεύει η παρέα του Scooby-Doo λύνοντας μυστήρια;",
    "answers": [
      "Ghost Hunter",
      "The Mystery Machine",
      "Spooky Van",
      "Monster Mobile"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'The Mystery Machine' με τα ψυχεδελικά πράσινα και τιρκουάζ χρώματα και τα πορτοκαλί λουλούδια μεταφέρει τον Scooby, τον Shaggy, τον Fred, τη Daphne και τη Velma.",
    "funFacts": [
      "Η αγαπημένη λιχουδιά που πείθει τον Scooby και τον Shaggy να μπούν σε στοιχειωμένα μέρη είναι τα περίφημα 'Scooby Snacks'.",
      "Η σειρά κινουμένων σχεδίων Scooby-Doo ξεκίνησε από τα στούντιο Hanna-Barbera το 1969."
    ],
    "source": "https://en.wikipedia.org/wiki/Scooby-Doo",
    "locale": "el-GR",
    "tags": ["scooby_doo", "animation", "hanna_barbera", "mystery"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_129",
    "text": "Ποιες δύο αντίπαλες παρατάξεις συγκρούονται στον φανταστικό κόσμο του Azeroth στο παιχνίδι 'World of Warcraft';",
    "answers": [
      "Αυτοκρατορία και Επαναστάτες",
      "Τζεντάι και Σιθ",
      "Συμμαχία (Alliance) και Ορδή (Horde)",
      "Τάμπλιερ και Ασασίνοι"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το MMORPG της Blizzard χωρίζει τους παίκτες σε δύο ιστορικές αντίπαλες παρατάξεις: την Alliance (άνθρωποι, νάνοι, ξωτικά κ.ά.) και την Horde (ορκ, απέθαντοι, ταύροι κ.ά.).",
    "funFacts": [
      "Η κραυγή 'For the Alliance!' και 'For the Horde!' αποτελεί σύμβολο ταυτότητας για εκατομμύρια gamers παγκοσμίως.",
      "Το World of Warcraft κατείχε το Ρεκόρ Γκίνες για το πιο δημοφιλές MMORPG με πάνω από 12 εκατομμύρια συνδρομητές στην ακμή του."
    ],
    "source": "https://en.wikipedia.org/wiki/World_of_Warcraft",
    "locale": "el-GR",
    "tags": ["world_of_warcraft", "blizzard", "gaming", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_130",
    "text": "Ποιοι δύο ηθοποιοί πρωταγωνίστησαν ως μαθήτρια και καθηγητής στην κλασική κωμωδία 'Το ξύλο βγήκε από τον παράδεισο' (1959);",
    "answers": [
      "Τζένη Καρέζη και Ανδρέας Μπάρκουλης",
      "Μάρω Κοντού και Γιώργος Κωνσταντίνου",
      "Ζωή Λάσκαρη και Φαίδων Γεωργίτσης",
      "Αλίκη Βουγιουκλάκη και Δημήτρης Παπαμιχαήλ"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Αλίκη Βουγιουκλάκη (Λίζα Παπασταύρου) και ο Δημήτρης Παπαμιχαήλ (καθηγητής Πάνος Φλωράς) δημιούργησαν ένα από τα πιο αγαπημένα κινηματογραφικά ζευγάρια.",
    "funFacts": [
      "Στην ταινία ακούστηκαν ιστορικά τραγούδια του Μάνου Χατζιδάκι, όπως το 'Έχω ένα μυστικό' και το 'Γκρίζο γατί'.",
      "Η ταινία έκοψε πάνω από 200.000 εισιτήρια στην πρώτη της προβολή στην Αθήνα, εδραιώνοντας τη Βουγιουκλάκη ως 'εθνική σταρ'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BE%CF%8D%CE%BB%CE%BF_%CE%B2%CE%B3%CE%AE%CE%BA%CE%B5_%CE%B1%CF%80%CF%8C_%CF%84%CE%BF%CE%BD_%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vougiouklaki", "papamichael", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_131",
    "text": "Ποια διάσημη φιλοσοφική ατάκα λέει ο Dr. Ian Malcolm (Jeff Goldblum) στην ταινία 'Jurassic Park';",
    "answers": [
      "Life finds a way (Η ζωή βρίσκει τρόπο)",
      "Greed is good",
      "Winter is coming",
      "There is no spoon"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Dr. Malcolm προειδοποιεί ότι η φύση δεν μπορεί να περιοριστεί από ανθρώπινους φραγμούς, λέγοντας 'Life finds a way'.",
    "funFacts": [
      "Η φράση αυτή έγινε μία από τις πιο αναγνωρίσιμες ατάκες στην ιστορία του κινηματογράφου και επαναλήφθηκε σε μεταγενέστερες ταινίες της σειράς.",
      "Ο Jeff Goldblum βασίστηκε στη θεωρία του χάους για να υποδυθεί τον εκκεντρικό μαθηματικό χαρακτήρα."
    ],
    "source": "https://en.wikipedia.org/wiki/Jurassic_Park_(film)",
    "locale": "el-GR",
    "tags": ["jurassic_park", "cinema", "quotes", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_132",
    "text": "Τι κάνει ο Bart Simpson στη χαρακτηριστική εισαγωγική σκηνή των επεισοδίων της σειράς 'The Simpsons';",
    "answers": [
      "Κάνει άλματα με το skateboard",
      "Γράφει τιμωρία στον σχολικό μαυροπίνακα",
      "Τρώει ντόνατς κρυφά",
      "Παίζει σαξόφωνο"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Σε κάθε επεισόδιο, ο Bart γράφει επανειλημμένα μια διαφορετική αστεία φράση τιμωρίας στον πίνακα του σχολείου του Springfield.",
    "funFacts": [
      "Η εισαγωγική σεκάνς περιλαμβάνει επίσης το 'gag του καναπέ' (couch gag), το οποίο αλλάζει σχεδόν σε κάθε επεισόδιο.",
      "Τη φωνή του δεκάχρονου Bart κάνει από την αρχή της σειράς η γυναίκα ηθοποιός Nancy Cartwright."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Simpsons",
    "locale": "el-GR",
    "tags": ["the_simpsons", "animation", "tv", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_133",
    "text": "Ποιο βρετανικό γυναικείο συγκρότημα εκτόξευσε το σύνθημα 'Girl Power' στη δεκαετία του 1990 με το τραγούδι 'Wannabe';",
    "answers": [
      "Destiny's Child",
      "All Saints",
      "Spice Girls",
      "TLC"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι Spice Girls (Victoria, Geri, Mel B, Mel C, Emma) έγιναν το πιο επιτυχημένο γυναικείο ποπ συγκρότημα στην ιστορία της μουσικής.",
    "funFacts": [
      "Το ντεμπούτο single τους 'Wannabe' (1996) έφτασε στο νούμερο 1 σε περισσότερες από 30 χώρες παγκοσμίως.",
      "Το διάσημο φόρεμα με τη βρετανική σημαία (Union Jack) που φόρεσε η Geri Halliwell στα Brit Awards του 1997 πωλήθηκε σε δημοπρασία για πάνω από 40.000 λίρες."
    ],
    "source": "https://en.wikipedia.org/wiki/Spice_Girls",
    "locale": "el-GR",
    "tags": ["spice_girls", "music", "pop", "90s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_134",
    "text": "Ποια υπερδύναμη διαθέτει ο σούπερ ήρωας The Flash (Barry Allen) των κόμικς της DC;",
    "answers": [
      "Τηλεπάθεια",
      "Αορατότητα",
      "Υπεράνθρωπη δύναμη",
      "Υπεράνθρωπη ταχύτητα"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Barry Allen αντλεί δύναμη από το Speed Force και μπορεί να τρέχει με ταχύτητες ταχύτερες από το φως, ταξιδεύοντας ακόμη και στον χρόνο.",
    "funFacts": [
      "Ο Flash απέκτησε τις δυνάμεις του όταν χτυπήθηκε από κεραυνό στο εγκληματολογικό του εργαστήριο και περιλούστηκε με χημικά.",
      "Το έμβλημα στο κόκκινο κοστούμι του είναι ένας χρυσός κεραυνός μέσα σε λευκό κύκλο."
    ],
    "source": "https://en.wikipedia.org/wiki/Flash_(Barry_Allen)",
    "locale": "el-GR",
    "tags": ["flash", "dc_comics", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_135",
    "text": "Ποιο είναι το αγαπημένο φαγητό των κίτρινων Minions στην ταινία 'Εγώ, ο Απαισιότατος' (Despicable Me);",
    "answers": [
      "Μπανάνες",
      "Μήλα",
      "Παγωτά",
      "Πίτσες"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Τα Minions έχουν πάθος με τις μπανάνες και φωνάζουν με ενθουσιασμό 'Banana!' κάθε φορά που βλέπουν μία.",
    "funFacts": [
      "Η διάλεκτος των Minions (Minionese) είναι ένα μείγμα λέξεων από αγγλικά, ισπανικά, γαλλικά, ιταλικά, ιαπωνικά και άλλες γλώσσες.",
      "Τις φωνές των Minions ηχογράφησε ο ίδιος ο συν-σκηνοθέτης της ταινίας Pierre Coffin."
    ],
    "source": "https://en.wikipedia.org/wiki/Minions_(characters)",
    "locale": "el-GR",
    "tags": ["minions", "despicable_me", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_136",
    "text": "Σε τι είδους ίδρυμα διαδραματίζεται η σατιρική σειρά των Ρήγα - Αποστόλου 'Οι Στάβλοι της Εριέτας Ζαΐμη';",
    "answers": [
      "Σε ψυχιατρική κλινική",
      "Σε γυναικείες φυλακές",
      "Σε στρατόπεδο νεοσυλλέκτων",
      "Σε οικοτροφείο θηλέων"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η σειρά εκτυλίσσεται στις πρότυπες γυναικείες φυλακές Καλάμου που ίδρυσε η εκκεντρική Εριέτα Ζαΐμη.",
    "funFacts": [
      "Τη διευθύντρια των φυλακών Μελίνα Νατσίκου υποδύθηκε η Μίρκα Παπακωνσταντίνου και τον έγκλειστο αρχιτέκτονα Παύλο Κοντογιαννόπουλο ο Νίκος Σεργιανόπουλος.",
      "Η σειρά προβλήθηκε στον ΑΝΤ1 τις σεζόν 2002-2004 με εξαιρετικά υψηλή τηλεθέαση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CF%83%CF%84%CE%AC%CE%B2%CE%BB%CE%BF%CE%B9_%CF%84%CE%B7%CF%82_%CE%95%CF%81%CE%B9%CE%AD%CF%84%CE%B1%CF%82_%CE%96%CE%B1%CE%90%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["oi_stavloi_tis_erietas_zaimi", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_137",
    "text": "Ποια ανατριχιαστική ερώτηση επαναλαμβάνει ο Joker (Heath Ledger) στην ταινία 'Ο Σκοτεινός Ιππότης' (The Dark Knight, 2008);",
    "answers": [
      "Do you want to know a secret?",
      "Who are you waiting for?",
      "Why so serious?",
      "Are you afraid of the dark?"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Why so serious?' αποτελεί την πιο εμβληματική ατάκα του Joker καθώς διηγείται διαφορετικές ψεύτικες ιστορίες για τις ουλές στο πρόσωπό του.",
    "funFacts": [
      "Ο Heath Ledger βραβεύτηκε μετά θάνατον με το Όσκαρ Β' Ανδρικού Ρόλου για την ασύλληπτη ερμηνεία του.",
      "Για να προετοιμαστεί για τον ρόλο, ο Ledger κλείστηκε μόνος του σε ένα δωμάτιο ξενοδοχείου για έξι εβδομάδες κρατώντας ένα προσωπικό ημερολόγιο του Joker."
    ],
    "source": "https://en.wikipedia.org/wiki/Joker_(The_Dark_Knight)",
    "locale": "el-GR",
    "tags": ["the_dark_knight", "joker", "heath_ledger", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_138",
    "text": "Ποιο μοτίβο τίτλων χρησιμοποίησε ο Βρετανός τραγουδοποιός Ed Sheeran για τα πρώτα του επιτυχημένα άλμπουμ;",
    "answers": [
      "Χρώματα",
      "Ονόματα πόλεων",
      "Ζώδια",
      "Μαθηματικά σύμβολα (+, x, ÷, =)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ed Sheeran ονόμασε τα άλμπουμ του με βάση μαθηματικά σύμβολα: '+' (Plus), 'x' (Multiply), '÷' (Divide) και '=' (Equals).",
    "funFacts": [
      "Το τραγούδι του 'Shape of You' έγινε ένα από τα τραγούδια με τα περισσότερα streams στην ιστορία του Spotify, ξεπερνώντας τα 3 δισεκατομμύρια.",
      "Ο Ed Sheeran ξεκίνησε την καριέρα του παίζοντας μουσική σε δρόμους και μικρές παμπ του Λονδίνου."
    ],
    "source": "https://en.wikipedia.org/wiki/Ed_Sheeran",
    "locale": "el-GR",
    "tags": ["ed_sheeran", "music", "pop", "spotify"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_139",
    "text": "Πώς ονομάζονται οι κρυφοί σαμποτέρ που προσπαθούν να εξοντώσουν το πλήρωμα στο διαδικτυακό παιχνίδι 'Among Us';",
    "answers": [
      "Impostors (Απατεώνες)",
      "Hackers",
      "Zombies",
      "Ghosts"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στο Among Us, οι Impostors παριστάνουν τα μέλη του πληρώματος (Crewmates) σαμποτάροντας το διαστημόπλοιο και εξοντώνοντας τους υπόλοιπους παίκτες.",
    "funFacts": [
      "Ο όρος 'sus' (συντομογραφία του suspicious) έγινε viral διαδικτυακό meme παγκοσμίως εξαιτίας του παιχνιδιού.",
      "Το Among Us κυκλοφόρησε αρχικά το 2018 χωρίς μεγάλη ανταπόκριση, αλλά γνώρισε εκρηκτική παγκόσμια άνοδο το 2020 μέσω streamers στο Twitch και YouTube."
    ],
    "source": "https://en.wikipedia.org/wiki/Among_Us",
    "locale": "el-GR",
    "tags": ["among_us", "gaming", "innersloth", "memes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_140",
    "text": "Τι αντικείμενο χάνει η Σταχτοπούτα (Cinderella) στα σκαλιά του παλατιού όταν χτυπούν τα μεσάνυχτα;",
    "answers": [
      "Ένα χρυσό δαχτυλίδι",
      "Ένα γυάλινο γοβάκι",
      "Μια μεταξωτή κορδέλα",
      "Ένα μαγικό γάντι"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Σταχτοπούτα φεύγει βιαστικά από τον χορό πριν διαλυθούν τα μάγια και αφήνει πίσω της το ένα γυάλινο γοβάκι, με το οποίο ο πρίγκιπας την αναζητά.",
    "funFacts": [
      "Η animated ταινία της Disney κυκλοφόρησε το 1950 και έσωσε το στούντιο της Disney από σοβαρά οικονομικά προβλήματα μετά τον Β' Παγκόσμιο Πόλεμο.",
      "Η σκηνή όπου τα κουρέλια της Σταχτοπούτας μεταμορφώνονται σε αστραφτερή τουαλέτα θεωρούνταν από τον ίδιο τον Walt Disney ως η αγαπημένη του σκηνή animation."
    ],
    "source": "https://en.wikipedia.org/wiki/Cinderella_(1950_film)",
    "locale": "el-GR",
    "tags": ["cinderella", "disney", "animation", "fairy_tale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_141",
    "text": "Ποιος ηθοποιός ενσάρκωσε τον 'κοντό' στην κλασική κωμωδία 'Ο Κλέαρχος, η Μαρίνα και ο κοντός' (1961);",
    "answers": [
      "Κώστας Χατζηχρήστος",
      "Γιάννης Γκιωνάκης",
      "Νίκος Ρίζος",
      "Βασίλης Αυλωνίτης"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Νίκος Ρίζος υποδύθηκε τον Μάχο, τον 'κοντό' γαμπρό του Κλέαρχου (Βασίλης Αυλωνίτης) και της Μαρίνας (Γεωργία Βασιλειάδου).",
    "funFacts": [
      "Η ταινία βασίστηκε στο ομώνυμο θεατρικό έργο των Νίκου Τσιφόρου και Πολύβιου Βασιλειάδη.",
      "Ο Νίκος Ρίζος υπήρξε ένας από τους πιο δημοφιλείς και αγαπητούς καρατερίστες της χρυσής εποχής του ελληνικού κινηματογράφου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9A%CE%BB%CE%AD%CE%B1%CF%81%CF%87%CE%BF%CF%82,_%CE%B7_%CE%9C%CE%B1%CF%81%CE%AF%CE%BD%CE%B1_%CE%BA%CE%B1%CE%B9_%CE%BF_%CE%BA%CE%BF%CE%BD%CF%84%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["greek_cinema", "comedy", "rizos", "avlonitis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_142",
    "text": "Ποιο είναι το αγαπημένο σνακ της Eleven στην πρώτη σεζόν της σειράς 'Stranger Things';",
    "answers": [
      "Ποπ κορν",
      "Σοκολάτες KitKat",
      "Πατατάκια Pringles",
      "Βάφλες Eggo"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Eleven λατρεύει τις κατεψυγμένες βάφλες Eggo, τις οποίες τρώει συνεχώς αφού δραπετεύει από το εργαστήριο του Hawkins.",
    "funFacts": [
      "Οι πωλήσεις της μάρκας Eggo στις ΗΠΑ σημείωσαν κατακόρυφη άνοδο μετά την προβολή της πρώτης σεζόν της σειράς.",
      "Ο χαρακτήρας του Chief Jim Hopper άφηνε βάφλες Eggo σε ένα ξύλινο κουτί στο δάσος για να ταΐσει κρυφά την Eleven."
    ],
    "source": "https://en.wikipedia.org/wiki/Eleven_(Stranger_Things)",
    "locale": "el-GR",
    "tags": ["stranger_things", "eleven", "netflix", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_143",
    "text": "Ποιο θρυλικό ροκ συγκρότημα έχει ως παγκοσμίως αναγνωρίσιμο σήμα μια κατακόκκινη γλώσσα που προεξέχει από τα χείλη;",
    "answers": [
      "The Rolling Stones",
      "Aerosmith",
      "KISS",
      "Led Zeppelin"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το εμβληματικό λογότυπο 'Tongue and Lips' των Rolling Stones σχεδιάστηκε από τον John Pasche το 1970 και πρωτοεμφανίστηκε στο άλμπουμ 'Sticky Fingers'.",
    "funFacts": [
      "Το σχέδιο εμπνεύστηκε άμεσα από τα μεγάλα και εκφραστικά χείλη του frontman του συγκροτήματος, Mick Jagger.",
      "Θεωρείται ευρέως το πιο διάσημο και εμπορικό ροκ λογότυπο στην ιστορία της μουσικής."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Rolling_Stones",
    "locale": "el-GR",
    "tags": ["rolling_stones", "mick_jagger", "rock", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_144",
    "text": "Ποιος ηθοποιός κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου υποδυόμενος τον στρατηγό Μάξιμο στην ταινία 'Ο Μονομάχος' (Gladiator, 2000);",
    "answers": [
      "Μελ Γκίμπσον",
      "Ράσελ Κρόου",
      "Χοακίν Φίνιξ",
      "Κρίστιαν Μπέιλ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Russell Crowe πρωταγωνίστησε ως ο Ρωμαίος στρατηγός Maximus Decimus Meridius που καταλήγει μονομάχος στο Κολοσσαίο.",
    "funFacts": [
      "Η ατάκα του 'Are you not entertained?' προς το πλήθος του Κολοσσαίου παραμένει ένα από τα πιο διάσημα κινηματογραφικά στιγμιότυπα.",
      "Η ταινία σε σκηνοθεσία Ridley Scott κέρδισε συνολικά 5 βραβεία Όσκαρ, συμπεριλαμβανομένου αυτού της Καλύτερης Ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Gladiator_(2000_film)",
    "locale": "el-GR",
    "tags": ["gladiator", "russell_crowe", "cinema", "ridley_scott"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_145",
    "text": "Ποιο είναι το πραγματικό όνομα του επιστήμονα που μεταμορφώνεται στον απίθανο Hulk όταν εξοργίζεται;",
    "answers": [
      "Peter Parker",
      "Steve Rogers",
      "Dr. Bruce Banner",
      "Tony Stark"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο πυρηνικός φυσικός Dr. Bruce Banner εκτέθηκε σε ακτίνες γάμμα, με αποτέλεσμα να μεταμορφώνεται στον πανίσχυρο πράσινο Hulk όταν ανεβαίνουν οι σφυγμοί του.",
    "funFacts": [
      "Στα πρώτα κόμικς του 1962, ο Hulk ήταν αρχικά γκρι, αλλά το χρώμα άλλαξε σε πράσινο επειδή τα τυπογραφεία δεν μπορούσαν να διατηρήσουν σταθερό τον γκρι τόνο.",
      "Η κλασική προειδοποιητική ατάκα του Bruce Banner είναι: 'Don't make me angry. You wouldn't like me when I'm angry.'"
    ],
    "source": "https://en.wikipedia.org/wiki/Hulk",
    "locale": "el-GR",
    "tags": ["hulk", "bruce_banner", "marvel", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_146",
    "text": "Ποιοι τρεις κολλητοί φίλοι πρωταγωνιστούν στην κωμική σειρά του Mega '50-50' (Πενήντα-Πενήντα);",
    "answers": [
      "Σπύρος, Βλάσσης, Γιάννης",
      "Σάββας, Μενέλαος, Βαγγέλης",
      "Κωνσταντίνος, Μάνθος, Νικόλας",
      "Νικηφόρος, Μίμης, Παύλος"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι Πέτρος Φιλιππίδης (Νικηφόρος), Παύλος Χαϊκάλης (Μίμης) και Σάκης Μπουλάς (Παύλος) ενσάρκωσαν την αχώριστη αντροπαρέα των πενηντάρηδων φίλων.",
    "funFacts": [
      "Το τσιπουράδικο όπου συγκεντρώνονταν οι τρεις ήρωες για να συζητήσουν τα προβλήματά τους ήταν το βασικό σημείο αναφοράς της σειράς.",
      "Η σειρά γνώρισε τεράστια επιτυχία και οδήγησε επίσης σε μία τηλεταινία και θεατρική παράσταση."
    ],
    "source": "https://el.wikipedia.org/wiki/50-50_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["50_50", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_147",
    "text": "Πώς καταφέρνει ο ηλικιωμένος Carl Fredricksen να απογειώσει το σπίτι του στην ταινία 'Up' (Ψηλά στον Ουρανό, 2009);",
    "answers": [
      "Με χιλιάδες μπαλόνια ηλίου",
      "Με έναν τεράστιο πύραυλο",
      "Με έλικες ελικοπτέρου",
      "Με μαγική σκόνη"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Carl δένει χιλιάδες πολύχρωμα μπαλόνια γεμάτα ήλιο στην καμινάδα του σπιτιού του για να πετάξει μέχρι τους Καταρράκτες του Παραδείσου.",
    "funFacts": [
      "Τα πρώτα 10 λεπτά της ταινίας που εξιστορούν τη ζωή και την αγάπη του Carl και της Ellie θεωρούνται αριστούργημα της κινηματογραφικής αφήγησης.",
      "Το Up ήταν η δεύτερη ταινία κινουμένων σχεδίων στην ιστορία (μετά την Πεντάμορφη και το Τέρας) που προτάθηκε για Όσκαρ Καλύτερης Ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Up_(2009_film)",
    "locale": "el-GR",
    "tags": ["up", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_148",
    "text": "Ποιο τραγούδι του συγκροτήματος Nirvana από το άλμπουμ 'Nevermind' (1991) έγινε ο απόλυτος ύμνος του grunge κινήματος;",
    "answers": [
      "Come as You Are",
      "Smells Like Teen Spirit",
      "Lithium",
      "Heart-Shaped Box"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Smells Like Teen Spirit' εκτόξευσε τους Nirvana και τον Kurt Cobain στην κορυφή του μουσικού κόσμου, αλλάζοντας το ροκ τοπίο της δεκαετίας του 1990.",
    "funFacts": [
      "Ο τίτλος προήλθε όταν μια φίλη του Kurt Cobain έγραψε στον τοίχο του 'Kurt smells like Teen Spirit' (το Teen Spirit ήταν μάρκα αποσμητικού).",
      "Το άλμπουμ 'Nevermind' εκθρόνισε το 'Dangerous' του Michael Jackson από την κορυφή των charts στις αρχές του 1992."
    ],
    "source": "https://en.wikipedia.org/wiki/Smells_Like_Teen_Spirit",
    "locale": "el-GR",
    "tags": ["nirvana", "kurt_cobain", "grunge", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_149",
    "text": "Ποιο είναι το αρχικό Pokémon τύπου Φωτιάς (Fire starter) που μπορεί να επιλέξει ο παίκτης στην πρώτη γενιά (Kanto);",
    "answers": [
      "Squirtle",
      "Bulbasaur",
      "Charmander",
      "Pikachu"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Charmander είναι μια πορτοκαλί σαύρα με μια φλόγα στην άκρη της ουράς του που εξελίσσεται στον Charmeleon και τελικά στον Charizard.",
    "funFacts": [
      "Αν η φλόγα στην άκρη της ουράς του Charmander σβήσει εντελώς, το Pokémon υποτίθεται ότι χάνει τη ζωή του.",
      "Ο Charizard παραμένει σταθερά ένα από τα πιο δημοφιλή και αναγνωρίσιμα πλάσματα σε ολόκληρο το franchise των Pokémon."
    ],
    "source": "https://en.wikipedia.org/wiki/Charmander",
    "locale": "el-GR",
    "tags": ["pokemon", "charmander", "gaming", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_150",
    "text": "Σε ποια φυλή της Μέσης Γης ανήκει ο Legolas στην τριλογία 'Ο Άρχοντας των Δαχτυλιδιών';",
    "answers": [
      "Στους Χόμπιτ",
      "Στους Ανθρώπους",
      "Στους Νάνους",
      "Στα Ξωτικά (Elves)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Legolas Greenleaf (Orlando Bloom) είναι πρίγκιπας των Ξωτικών του Woodland Realm και διακρίνεται για την αξεπέραστη τοξοβολία του.",
    "funFacts": [
      "Η αντιπαλότητα και σταδιακή βαθιά φιλία ανάμεσα στο ξωτικό Legolas και τον νάνο Gimli αποτελεί ένα από τα ομορφότερα στοιχεία της ιστορίας.",
      "Ο ρόλος του Legolas έκανε τον Orlando Bloom παγκόσμιο σταρ σχεδόν αμέσως μετά την αποφοίτησή του από τη δραματική σχολή."
    ],
    "source": "https://en.wikipedia.org/wiki/Legolas",
    "locale": "el-GR",
    "tags": ["lord_of_the_rings", "legolas", "tolkien", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_151",
    "text": "Ποιο δηλητηριασμένο φρούτο προσφέρει η Κακιά Βασίλισσα στη Χιονάτη στην κλασική ταινία της Disney (1937);",
    "answers": [
      "Ένα κόκκινο μήλο",
      "Ένα ζουμερό αχλάδι",
      "Ένα ροδάκινο",
      "Ένα πορτοκάλι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η μεταμφιεσμένη σε γριά μάγισσα Κακιά Βασίλισσα ξεγελά τη Χιονάτη προσφέροντάς της ένα δηλητηριασμένο κόκκινο μήλο που τη βυθίζει σε λήθαργο.",
    "funFacts": [
      "Η 'Χιονάτη και οι Επτά Νάνοι' ήταν η πρώτη μεγάλου μήκους έγχρωμη ταινία κινουμένων σχεδίων στην ιστορία του κινηματογράφου.",
      "Στην τελετή των Όσκαρ του 1939, η Ακαδημία απένειμε στον Walt Disney ένα κανονικό Όσκαρ και επτά μικρά αγαλματίδια."
    ],
    "source": "https://en.wikipedia.org/wiki/Snow_White_and_the_Seven_Dwarfs_(1937_film)",
    "locale": "el-GR",
    "tags": ["snow_white", "disney", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_152",
    "text": "Ποιο διάσημο παρατσούκλι πολιτικού απέκτησε ο Λάμπρος Κωνσταντάρας στην κλασική κωμωδία 'Υπάρχει και φιλότιμο' (1965);",
    "answers": [
      "Δερβέναγας",
      "Μαυρογιαλούρος",
      "Φον Δημητράκης",
      "Γκόρτσος"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Λάμπρος Κωνσταντάρας υποδύθηκε τον υπουργό Ανδρέα Μαυρογιαλούρο, του οποίου το όνομα έγινε έκτοτε συνώνυμο των πολιτικών που υπόσχονται ανέφικτα πράγματα.",
    "funFacts": [
      "Η ατάκα 'Φάγαμε, φάγαμε, φάγαμε!' που λέει ο υπουργός όταν ανακαλύπτει τις καταχρήσεις των συνεργατών του έμεινε στην ιστορία του ελληνικού κινηματογράφου.",
      "Η ταινία βασίστηκε σε θεατρικό έργο των Χρήστου Γιαννακόπουλου και Αλέκου Σακελλάριου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%AC%CF%81%CF%87%CE%B5%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["greek_cinema", "konstantaras", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_153",
    "text": "Πώς αποκαλούν συνήθως τους απέθαντους (ζόμπι) οι επιζώντες στη δημοφιλή μεταποκαλυπτική σειρά 'The Walking Dead';",
    "answers": [
      "Runners",
      "Clickers",
      "Walkers",
      "Infected"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στο The Walking Dead, η λέξη 'zombie' δεν χρησιμοποιείται σχεδόν ποτέ· οι χαρακτήρες τους ονομάζουν 'Walkers' (περιπατητές).",
    "funFacts": [
      "Ο δημιουργός των κόμικς Robert Kirkman επέλεξε σκόπιμα να μην υπάρχει η λέξη 'zombie' στον κόσμο της σειράς, ώστε οι χαρακτήρες να μην έχουν προηγούμενη γνώση από ταινίες τρόμου.",
      "Ο Andrew Lincoln πρωταγωνίστησε για εννέα σεζόν ως ο αστυνομικός Rick Grimes, ηγέτης των επιζώντων."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Walking_Dead_(TV_series)",
    "locale": "el-GR",
    "tags": ["the_walking_dead", "tv", "horror", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_154",
    "text": "Ποιο νοτιοκορεάτικο τραγούδι του Psy έγινε το πρώτο βίντεο στην ιστορία του YouTube που ξεπέρασε το 1 δισεκατομμύριο προβολές το 2012;",
    "answers": [
      "Dynamite",
      "Gentleman",
      "Ddu-Du Ddu-Du",
      "Gangnam Style"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Gangnam Style' και ο χαρακτηριστικός 'χορός ιππασίας' του Psy κατέκλυσαν τον πλανήτη το 2012 σπάζοντας κάθε προηγούμενο ρεκόρ θεάσεων.",
    "funFacts": [
      "Το βίντεο είχε τόσες πολλές προβολές που ανάγκασε τους μηχανικούς του YouTube να αναβαθμίσουν τον μετρητή προβολών από ακέραιο 32-bit σε 64-bit.",
      "Ο τίτλος αναφέρεται στην πολυτελή συνοικία Gangnam της Σεούλ και στον επιδεικτικό τρόπο ζωής των κατοίκων της."
    ],
    "source": "https://en.wikipedia.org/wiki/Gangnam_Style",
    "locale": "el-GR",
    "tags": ["gangnam_style", "psy", "k_pop", "youtube"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_155",
    "text": "Ποιος υπερήρωας της DC Comics είναι ο νόμιμος βασιλιάς της υποθαλάσσιας Ατλαντίδας;",
    "answers": [
      "Aquaman",
      "Namor",
      "Ocean Master",
      "Black Manta"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Arthur Curry είναι ο Aquaman, γιος μιας βασίλισσας της Ατλαντίδας και ενός φαροφύλακα, με την ικανότητα να επικοινωνεί τηλεπαθητικά με τη θαλάσσια ζωή.",
    "funFacts": [
      "Στο DC Extended Universe, τον Aquaman ενσάρκωσε ο ηθοποιός Jason Momoa, δίνοντας στον χαρακτήρα μια πιο δυναμική και άγρια εικόνα.",
      "Η ταινία Aquaman (2018) έγινε η πιο κερδοφόρα ταινία βασισμένη σε χαρακτήρα της DC Comics, με εισπράξεις άνω του 1,1 δισεκατομμυρίου δολαρίων."
    ],
    "source": "https://en.wikipedia.org/wiki/Aquaman",
    "locale": "el-GR",
    "tags": ["aquaman", "dc_comics", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_156",
    "text": "Τι προσπαθεί απεγνωσμένα να θάψει και να προστατεύσει ο προϊστορικός σκίουρος Scrat στις ταινίες 'Η Εποχή των Παγετώνων' (Ice Age);",
    "answers": [
      "Ένα καρύδι",
      "Ένα βελανίδι",
      "Ένα κουκουνάρι",
      "Ένα κόκαλο"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Scrat κυνηγά ασταμάτητα ένα βελανίδι, προκαλώντας κατά λάθος τεκτονικούς σεισμούς, χιονοστιβάδες και τη διάσπαση των ηπείρων.",
    "funFacts": [
      "Οι περιπέτειες του Scrat σχεδιάστηκαν αρχικά ως σύντομα κωμικά ιντερλούδια ανάμεσα στις βασικές σκηνές της ταινίας.",
      "Το όνομα Scrat είναι συνδυασμός των αγγλικών λέξεων 'squirrel' (σκίουρος) και 'rat' (αρουραίος)."
    ],
    "source": "https://en.wikipedia.org/wiki/Scrat",
    "locale": "el-GR",
    "tags": ["ice_age", "scrat", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_157",
    "text": "Ποιο ήταν το όνομα της εκκεντρικής και αυταρχικής γιαγιάς της σειράς 'Δέκα Λεπτά Κήρυγμα' που υποδύθηκε η Κάρμεν Ρουγγέρη;",
    "answers": [
      "Ζουμπουλία",
      "Ελισάβετ",
      "Κικίτσα",
      "Αμαλία"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Κάρμεν Ρουγγέρη ενσάρκωσε τη γιαγιά Κικίτσα, που προσπαθούσε συνεχώς να επιβάλει την τάξη στον έφηβο εγγονό της Λεωνίδα (Δημήτρης Κουρούμπαλης).",
    "funFacts": [
      "Η σειρά προβλήθηκε στο Mega Channel από το 2000 έως το 2004 σημειώνοντας τεράστια επιτυχία στο νεανικό κοινό.",
      "Τον χωρισμένο πατέρα του Λεωνίδα υποδύθηκε ο Σάκης Μπουλάς και τη μητέρα του η Αριέττα Μουτούση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BA%CE%B1_%CE%BB%CE%B5%CF%80%CF%84%CE%AC_%CE%BA%CE%AE%CF%81%CF%85%CE%B3%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["deka_lepta_kirygma", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_158",
    "text": "Ποιο είναι το χαρακτηριστικό παρατσούκλι πιλότου (call sign) του Tom Cruise στην ταινία 'Top Gun' (1986);",
    "answers": [
      "Goose",
      "Iceman",
      "Viper",
      "Maverick"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Tom Cruise υποδύεται τον ριψοκίνδυνο υποπλοίαρχο Pete Mitchell, γνωστό με το κωδικό όνομα 'Maverick'.",
    "funFacts": [
      "Η συνέχεια της ταινίας, 'Top Gun: Maverick' (2022), ξεπέρασε το 1,4 δισεκατομμύριο δολάρια σε εισπράξεις παγκοσμίως.",
      "Το τραγούδι 'Take My Breath Away' του συγκροτήματος Berlin από την πρώτη ταινία κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού."
    ],
    "source": "https://en.wikipedia.org/wiki/Pete_%22Maverick%22_Mitchell",
    "locale": "el-GR",
    "tags": ["top_gun", "tom_cruise", "maverick", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_159",
    "text": "Ποιο είναι το πραγματικό όνομα του θρυλικού ράπερ Eminem;",
    "answers": [
      "Marshall Mathers",
      "Curtis Jackson",
      "Calvin Broadus",
      "Shawn Carter"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Eminem γεννήθηκε ως Marshall Bruce Mathers III και δημιούργησε επίσης το διάσημο alter ego 'Slim Shady'.",
    "funFacts": [
      "Το τραγούδι του 'Lose Yourself' από την αυτοβιογραφική ταινία '8 Mile' (2002) έγινε το πρώτο hip-hop τραγούδι στην ιστορία που κέρδισε Όσκαρ.",
      "Το καλλιτεχνικό όνομα 'Eminem' προήλθε από την προφορά των αρχικών του ονόματός του (M&M)."
    ],
    "source": "https://en.wikipedia.org/wiki/Eminem",
    "locale": "el-GR",
    "tags": ["eminem", "rap", "music", "hip_hop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_160",
    "text": "Ποια διάσημη εταιρεία βιντεοπαιχνιδιών δημιούργησε τη σειρά 'Grand Theft Auto' (GTA);",
    "answers": [
      "Ubisoft",
      "Rockstar Games",
      "Electronic Arts",
      "Activision"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Rockstar Games είναι η δημιουργός της εξαιρετικά επιτυχημένης σειράς ανοιχτού κόσμου Grand Theft Auto.",
    "funFacts": [
      "Το Grand Theft Auto V (2013) απέφερε πάνω από 800 εκατομμύρια δολάρια στις πρώτες 24 ώρες κυκλοφορίας του, σπάζοντας κάθε ρεκόρ στον τομέα της ψυχαγωγίας.",
      "Το GTA V έχει ξεπεράσει τα 190 εκατομμύρια αντίτυπα σε πωλήσεις παγκοσμίως."
    ],
    "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto",
    "locale": "el-GR",
    "tags": ["gta", "rockstar_games", "gaming", "video_games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'easy', 1, questions)

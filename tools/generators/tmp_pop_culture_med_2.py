# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_med_061",
    "text": "Τι περιέχει ο μυστηριώδης χαρτοφύλακας που εκπέμπει πορτοκαλί λάμψη στην ταινία 'Pulp Fiction' (1994);",
    "answers": [
      "Δεν αποκαλύπτεται ποτέ στην ταινία",
      "Ράβδους καθαρού χρυσού",
      "Ένα διαμαντένιο περιδέραιο",
      "Εμπιστευτικά έγγραφα της μαφίας"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Quentin Tarantino επέλεξε σκόπιμα να μην αποκαλύψει ποτέ το περιεχόμενο του χαρτοφύλακα, λειτουργώντας ως κλασικό 'MacGuffin'.",
    "funFacts": [
      "Η θεωρία των φαν ότι ο χαρτοφύλακας περιείχε την ψυχή του Marsellus Wallace διαψεύστηκε επίσημα από τον ίδιο τον Tarantino.",
      "Για τη σκηνή όπου ανοίγει ο χαρτοφύλακας τοποθετήθηκε στο εσωτερικό του ένας μικρός πορτοκαλί λαμπτήρας με μπαταρία."
    ],
    "source": "https://en.wikipedia.org/wiki/Pulp_Fiction",
    "locale": "el-GR",
    "tags": ["pulp_fiction", "tarantino", "cinema", "macguffin"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_062",
    "text": "Από ποιο φυτό εξήγαγε τη θανατηφόρα τοξίνη ρισίνη (ricin) ο Walter White στη σειρά 'Breaking Bad';",
    "answers": [
      "Από την μπελαντόνα (Άτροπος η ευθαλεία)",
      "Από τους σπόρους της ρετσινολαδιάς (κίκινος)",
      "Από το ακόνιτο (λυκοκτόνο)",
      "Από τη δακτυλίτιδα"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Walter White παρασκευάζει ρισίνη από σπόρους του φυτού Ricinus communis (ρετσινολαδιά) για να εξοντώσει αθόρυβα τους εχθρούς του.",
    "funFacts": [
      "Το πακέτο τσιγάρων με το κρυμμένο φιαλίδιο ρισίνης αποτέλεσε κεντρικό στοιχείο αγωνίας για αρκετές σεζόν της σειράς.",
      "Η ρισίνη είναι εξαιρετικά ισχυρό δηλητήριο που δεν ανιχνεύεται εύκολα σε τυπικές τοξικολογικές εξετάσεις."
    ],
    "source": "https://en.wikipedia.org/wiki/Breaking_Bad",
    "locale": "el-GR",
    "tags": ["breaking_bad", "walter_white", "tv", "chemistry"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_063",
    "text": "Ποιος ροκ θρύλος δημιούργησε το εξωγήινο alter ego 'Ziggy Stardust' στο κλασικό concept άλμπουμ του 1972;",
    "answers": [
      "Μικ Τζάγκερ",
      "Φρέντι Μέρκιουρι",
      "Ντέιβιντ Μπόουι",
      "Έλτον Τζον"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο David Bowie ενσάρκωσε τον Ziggy Stardust, έναν ανδρόγυνο εξωγήινο ροκ σταρ που στάλθηκε στη Γη για να σώσει την ανθρωπότητα.",
    "funFacts": [
      "Το άλμπουμ 'The Rise and Fall of Ziggy Stardust and the Spiders from Mars' καθιέρωσε το glam rock παγκοσμίως.",
      "Ο Bowie 'σκότωσε' επίσημα τον χαρακτήρα του Ziggy πάνω στη σκηνή στο Hammersmith Odeon του Λονδίνου το 1973."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Rise_and_Fall_of_Ziggy_Stardust_and_the_Spiders_from_Mars",
    "locale": "el-GR",
    "tags": ["david_bowie", "ziggy_stardust", "glam_rock", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_064",
    "text": "Τι επιχείρηση κληρονομούν από κοινού τέσσερις μακρινοί συγγενείς στην κλασική κωμωδία 'Οι Κληρονόμοι' (1964);",
    "answers": [
      "Ένα ξενοδοχείο στη Ρόδο",
      "Ένα παραδοσιακό τσιπουράδικο",
      "Ένα εργοστάσιο ζυμαρικών",
      "Έναν οίκο μόδας και ραπτικής"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στην ταινία των Τσιφόρου - Βασιλειάδη, οι τέσσερις κληρονόμοι (Κώστας Χατζηχρήστος, Κώστας Βουτσάς, Μάρθα Καραγιάννη, Χλόη Λιάσκου) κληρονομούν έναν οίκο υψηλής ραπτικής.",
    "funFacts": [
      "Η ταινία σε σκηνοθεσία Γιάννη Δαλιανίδη έκοψε σχεδόν 250.000 εισιτήρια στην πρώτη της προβολή.",
      "Τον ρόλο του αυστηρού διευθυντή του οίκου μόδας υποδύθηκε ο Ντίνος Ηλιόπουλος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%BA%CE%BB%CE%B7%CF%81%CE%BF%CE%BD%CF%8C%CE%BC%CE%BF%CE%B9_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1964)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "chatzichristos", "voutzas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_065",
    "text": "Πώς ονομάζεται η τεχνητή νοημοσύνη της στολής του Peter Parker στην ταινία 'Spider-Man: Homecoming' (2017);",
    "answers": [
      "Karen",
      "Friday",
      "Edith",
      "Veronica"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Peter Parker ονομάζει την ευγενική AI φωνή της νέας του Stark στολής 'Karen'.",
    "funFacts": [
      "Τη φωνή της Karen έκανε η βραβευμένη με Όσκαρ ηθοποιός Jennifer Connelly.",
      "Στην πραγματική ζωή, η Jennifer Connelly είναι παντρεμένη με τον Paul Bettany, ο οποίος δάνειζε τη φωνή του στον J.A.R.V.I.S. και ενσάρκωσε τον Vision!"
    ],
    "source": "https://en.wikipedia.org/wiki/Spider-Man:_Homecoming",
    "locale": "el-GR",
    "tags": ["spider_man", "marvel", "mcu", "ai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_066",
    "text": "Ποιο όνομα δίνει ο μικρός Russell στο γιγάντιο πολύχρωμο πουλί που συναντούν στη Νότια Αμερική στην ταινία 'Up' (2009);",
    "answers": [
      "Dug",
      "Kevin",
      "Charlie",
      "Pip"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Russell ονομάζει το σπάνιο πουλί 'Kevin', για να ανακαλύψει αργότερα ότι είναι θηλυκό όταν συναντά τα μικρά της.",
    "funFacts": [
      "Το πουλί Kevin βασίστηκε στον εντυπωσιακό σχεδιασμό του πραγματικού πτηνού Himalayan monal (εθνικό πουλί του Νεπάλ).",
      "Ο κακός εξερευνητής Charles Muntz πέρασε δεκαετίες κυνηγώντας τον Kevin για να αποκαταστήσει τη φήμη του."
    ],
    "source": "https://en.wikipedia.org/wiki/Up_(2009_film)",
    "locale": "el-GR",
    "tags": ["up", "pixar", "animation", "kevin"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_067",
    "text": "Ποιο ήταν το επάγγελμα του χαρακτήρα του Γιάννη Μπέζου στη θρυλική κωμική σειρά 'Οι Απαράδεκτοι';",
    "answers": [
      "Ηθοποιός",
      "Αρχιτέκτονας",
      "Σχεδιαστής μόδας",
      "Δημοσιογράφος"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Γιάννης εργαζόταν ως σχεδιαστής μόδας και διακοσμητής, ζώντας στο απέναντι διαμέρισμα από τον Σπύρο και τη Δήμητρα.",
    "funFacts": [
      "Ο χαρακτήρας του Γιάννη ήταν ο πρώτος ανοιχτά ομοφυλόφιλος βασικός πρωταγωνιστής στην ελληνική prime time τηλεόραση, αντιμετωπιζόμενος με τρυφερότητα και φυσικότητα.",
      "Η σειρά προβλήθηκε στο Mega Channel από το 1991 έως το 1993 σημειώνοντας ανεπανάληπτη επιτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["oi_aparadektoi", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_068",
    "text": "Ποιο προσωπικό μικρό αντικείμενο χρησιμοποιεί ως 'τότεμ' ο Dom Cobb (Leonardo DiCaprio) στην ταινία 'Inception' (2010);",
    "answers": [
      "Ένα ζάρι με λάθος βάρος",
      "Ένα πιόνι σκακιού",
      "Ένα παλιό κέρμα",
      "Μια μεταλλική σβούρα"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Cobb περιστρέφει τη σβούρα: αν σταματήσει και πέσει βρίσκεται στην πραγματικότητα, ενώ αν συνεχίσει να περιστρέφεται αέναα βρίσκεται σε όνειρο.",
    "funFacts": [
      "Το τελικό πλάνο της ταινίας όπου η σβούρα τρεμοπαίζει αλλά η οθόνη μαυρίζει πριν φανεί αν πέφτει αποτελεί ένα από τα πιο διάσημα ανοιχτά τέλη του σινεμά.",
      "Το τότεμ ανήκε αρχικά στην εκλιπούσα σύζυγό του Mal (Marion Cotillard)."
    ],
    "source": "https://en.wikipedia.org/wiki/Inception",
    "locale": "el-GR",
    "tags": ["inception", "christopher_nolan", "cinema", "totem"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_069",
    "text": "Ποια τέσσερα μέλη αποτελούσαν το σουηδικό συγκρότημα των ABBA που θριάμβευσε στη Eurovision του 1974;",
    "answers": [
      "Agnetha, Björn, Benny, Anni-Frid",
      "Astrid, Birgit, Bo, Annika",
      "Anna, Bengt, Bertil, Alva",
      "Agnes, Bjarne, Boris, Astrid"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το όνομα ABBA σχηματίστηκε ως ακρωνύμιο από τα αρχικά των ονομάτων των τεσσάρων μελών: Agnetha Fältskog, Björn Ulvaeus, Benny Andersson και Anni-Frid Lyngstad.",
    "funFacts": [
      "Πριν επιλεγεί το όνομα ABBA, τα μέλη έπρεπε να πάρουν επίσημη άδεια από μια γνωστή σουηδική εταιρεία κονσερβοποίησης ψαριών με την ίδια επωνυμία.",
      "Το συγκρότημα αποτελούνταν αρχικά από δύο παντρεμένα ζευγάρια, τα οποία χώρισαν κατά τη διάρκεια της ακμής της καριέρας τους."
    ],
    "source": "https://en.wikipedia.org/wiki/ABBA",
    "locale": "el-GR",
    "tags": ["abba", "music", "pop", "eurovision"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_070",
    "text": "Πώς ονομάζεται η αρχαία γλώσσα των δράκων στην οποία διατυπώνονται οι πολεμικές κραυγές (Thu'um) στο παιχνίδι 'Skyrim';",
    "answers": [
      "Daedric",
      "Dovahzul",
      "Altmeris",
      "Falmer"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Dovahzul είναι η πλήρως ανεπτυγμένη γλώσσα των δράκων που δημιούργησε η Bethesda με δικό της ρουνικό αλφάβητο σφηνοειδούς γραφής.",
    "funFacts": [
      "Η διάσημη κραυγή 'Fus Ro Dah' μεταφράζεται στα ελληνικά ως 'Δύναμη, Ισορροπία, Ώθηση' (Force, Balance, Push).",
      "Οι χαρακτήρες του αλφαβήτου σχεδιάστηκαν έτσι ώστε να μοιάζουν με σημάδια που θα μπορούσε να χαράξει ένα νύχι δράκου πάνω σε πέτρα."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "locale": "el-GR",
    "tags": ["skyrim", "bethesda", "gaming", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_071",
    "text": "Ποιο ήταν το αρχικό επάγγελμα και ονοματεπώνυμο της Harley Quinn πριν συναντήσει τον Joker στο Arkham Asylum;",
    "answers": [
      "Δικηγόρος Selina Kyle",
      "Βιοχημικός Pamela Isley",
      "Ψυχίατρος Harleen Quinzel",
      "Αστυνομικός Renee Montoya"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Dr. Harleen Frances Quinzel ήταν ψυχίατρος στο άσυλο του Arkham που ανέλαβε τη θεραπεία του Joker, αλλά κατέληξε να τον ερωτευτεί παράφορα.",
    "funFacts": [
      "Η Harley Quinn δεν δημιουργήθηκε στα κόμικς, αλλά έκανε το ντεμπούτο της στην τηλεοπτική σειρά κινουμένων σχεδίων 'Batman: The Animated Series' το 1992.",
      "Δημιουργοί της ήταν οι Paul Dini και Bruce Timm, οι οποίοι εμπνεύστηκαν τον χαρακτήρα από την ηθοποιό Arleen Sorkin."
    ],
    "source": "https://en.wikipedia.org/wiki/Harley_Quinn",
    "locale": "el-GR",
    "tags": ["harley_quinn", "batman", "dc_comics", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_072",
    "text": "Ποιο ασυνήθιστο αντικείμενο κλέβει ο Ted Mosby από ένα εστιατόριο για να εντυπωσιάσει τη Robin στη σειρά 'How I Met Your Mother';",
    "answers": [
      "Μια κίτρινη ομπρέλα",
      "Ένα vintage ρολόι τοίχου",
      "Έναν πίνακα αφηρημένης τέχνης",
      "Ένα μπλε γαλλικό κόρνο (Blue French Horn)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το μπλε γαλλικό κόρνο έγινε το απόλυτο σύμβολο της ρομαντικής εμμονής του Ted για τη Robin σε ολόκληρη τη σειρά.",
    "funFacts": [
      "Στο τέλος των γυρισμάτων της σειράς, η παραγωγή χάρισε το αυθεντικό μπλε κόρνο στον πρωταγωνιστή Josh Radnor.",
      "Η σειρά προβλήθηκε για 9 σεζόν (2005-2014) στο αμερικανικό δίκτυο CBS."
    ],
    "source": "https://en.wikipedia.org/wiki/How_I_Met_Your_Mother",
    "locale": "el-GR",
    "tags": ["how_i_met_your_mother", "sitcom", "tv", "romance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_073",
    "text": "Ποιο είδος νυχτοπεταλούδας τοποθετούσε στα θύματά του ο κατά συρροή δολοφόνος Buffalo Bill στη 'Σιωπή των Αμνών';",
    "answers": [
      "Νυχτοπεταλούδα του θανάτου (Acherontia atropos)",
      "Πεταλούδα Μονάρχης",
      "Σφίγγα της λεύκας",
      "Σελήνη του μεταξιού"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Acherontia atropos φέρει στο θώρακά της ένα φυσικό σχέδιο που μοιάζει εντυπωσιακά με ανθρώπινο κρανίο.",
    "funFacts": [
      "Το διάσημο εξώφυλλο και η αφίσα της ταινίας δείχνουν τη νυχτοπεταλούδα πάνω στο στόμα της Jodie Foster, όπου το σχέδιο κρανίου αποτελείται από γυμνά γυναικεία σώματα βασισμένα σε φωτογραφία του Salvador Dalí.",
      "Η μεταμόρφωση της κάμπιας σε πεταλούδα συμβόλιζε για τον δολοφόνο την επιθυμία του να μεταμορφωθεί σε γυναίκα."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Silence_of_the_Lambs_(film)",
    "locale": "el-GR",
    "tags": ["silence_of_the_lambs", "cinema", "thriller", "details"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_074",
    "text": "Ποιος πρωταγωνίστησε ως ο Αλέκος Κουρούζιλος στην κλασική κωμωδία 'Ο ατσίδας' (1961) λανσάροντας τη φράση 'Στρίβειν διά του αρραβώνος';",
    "answers": [
      "Κώστας Χατζηχρήστος",
      "Ντίνος Ηλιόπουλος",
      "Μίμης Φωτόπουλος",
      "Γιάννης Γκιωνάκης"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Ντίνος Ηλιόπουλος υποδύθηκε τον δαιμόνιο Αλέκο που αρραβωνιαζόταν διαδοχικά για να κερδίζει χρόνο και χρήματα χωρίς ποτέ να παντρεύεται.",
    "funFacts": [
      "Η φράση 'Στρίβειν διά του αρραβώνος' πέρασε έκτοτε στη νεοελληνική γλώσσα ως παροιμιώδης έκφραση υπεκφυγής.",
      "Η ταινία γυρίστηκε από τη Φίνος Φιλμ σε σκηνοθεσία Γιάννη Δαλιανίδη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%B1%CF%84%CF%83%CE%AF%CE%B4%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek_cinema", "iliopoulos", "comedy", "dalianidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_075",
    "text": "Ποιος ήταν ο χαρισματικός τραγουδιστής των Soundgarden και των Audioslave που έγραψε το θρυλικό κομμάτι 'Black Hole Sun';",
    "answers": [
      "Έντι Βέντερ",
      "Λέιν Στέιλι",
      "Κρις Κορνέλ",
      "Σκοτ Γουέιλαντ"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Chris Cornell (1964-2017) υπήρξε πρωτεργάτης της grunge σκηνής του Σιάτλ, διαθέτοντας σπάνιο φωνητικό εύρος σχεδόν τεσσάρων οκτάβων.",
    "funFacts": [
      "Ο Chris Cornell ερμήνευσε επίσης το τραγούδι τίτλων 'You Know My Name' για την ταινία James Bond 'Casino Royale' (2006).",
      "Το 'Black Hole Sun' γράφτηκε από τον Cornell σε μόλις δεκαπέντε λεπτά ενώ οδηγούσε προς το σπίτι του."
    ],
    "source": "https://en.wikipedia.org/wiki/Chris_Cornell",
    "locale": "el-GR",
    "tags": ["chris_cornell", "soundgarden", "grunge", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_076",
    "text": "Πώς ονομάζεται ο εκκεντρικός εφευρέτης πατέρας της Belle στην κλασική ταινία 'Η Πεντάμορφη και το Τέρας' (1991);",
    "answers": [
      "Γκαστόν",
      "Λεφού",
      "Λουμιέρ",
      "Μορίς (Maurice)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Maurice είναι ο καλόκαρδος εφευρέτης που χάνεται στο σκοτεινό δάσος και αιχμαλωτίζεται πρώτος στο κάστρο του Τέρατος.",
    "funFacts": [
      "Η αυτόματη μηχανή κοπής ξύλων του Maurice ήταν η εφεύρεση που πήγαινε να παρουσιάσει στην έκθεση όταν χάθηκε στον δρόμο.",
      "Στο live-action ριμέικ του 2017, τον ρόλο του Maurice υποδύθηκε ο βραβευμένος με Όσκαρ Kevin Kline."
    ],
    "source": "https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film)",
    "locale": "el-GR",
    "tags": ["beauty_and_the_beast", "disney", "animation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_077",
    "text": "Σε ποια διαφημιστική εταιρεία της Madison Avenue ξεκινά ως επικεφαλής δημιουργικού ο Don Draper στη σειρά 'Mad Men';",
    "answers": [
      "Sterling Cooper",
      "McCann Erickson",
      "BBDO Worldwide",
      "Ogilvy & Mather"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Don Draper (Jon Hamm) είναι ο ιδιοφυής αλλά μυστηριώδης creative director της φανταστικής εταιρείας Sterling Cooper στη Νέα Υόρκη της δεκαετίας του 1960.",
    "funFacts": [
      "Η σειρά κέρδισε το Βραβείο Emmy Καλύτερης Δραματικής Σειράς για τέσσερις συνεχόμενες χρονιές (2008-2011).",
      "Το πραγματικό όνομα του Don Draper αποκαλύπτεται ότι ήταν Dick Whitman, έχοντας κλέψει την ταυτότητα του νεκρού διοικητή του στον πόλεμο της Κορέας."
    ],
    "source": "https://en.wikipedia.org/wiki/Mad_Men",
    "locale": "el-GR",
    "tags": ["mad_men", "don_draper", "tv", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_078",
    "text": "Ποιο ήταν το επίσημο όνομα της πριγκίπισσας Peach στις αμερικανικές εκδόσεις των παιχνιδιών Mario μέχρι τα μέσα της δεκαετίας του '90;",
    "answers": [
      "Princess Daisy",
      "Princess Toadstool",
      "Princess Pauline",
      "Princess Rosalina"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στη Δύση ονομαζόταν αρχικά Princess Toadstool μέχρι το 'Super Mario 64' (1996), όπου καθιερώθηκε παγκοσμίως το ιαπωνικό της όνομα Peach.",
    "funFacts": [
      "Στην επιστολή της στην εισαγωγή του Super Mario 64 υπογράφει ως 'Princess Toadstool, Peach'.",
      "Το ροζ φόρεμα και τα ξανθά μαλλιά της αποτελούν το πιο αναγνωρίσιμο στυλ γυναικείας ηρωίδας της Nintendo."
    ],
    "source": "https://en.wikipedia.org/wiki/Princess_Peach",
    "locale": "el-GR",
    "tags": ["super_mario", "princess_peach", "nintendo", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_079",
    "text": "Ποια σχολή σπούδαζε ο Σπύρος Δελόγλου (Γιώργος Καπουτζίδης) όταν γνώρισε τους υπόλοιπους τέσσερις στη σειρά 'Στο Παρά 5';",
    "answers": [
      "Ιατρική",
      "Νομική",
      "Μαθηματικό",
      "Πληροφορική"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Σπύρος ήταν αιώνιος φοιτητής του Μαθηματικού τμήματος που ζούσε με τη γιαγιά του Σοφία και έλυνε γρίφους με τη λογική του σκέψη.",
    "funFacts": [
      "Η σχέση του Σπύρου με τη γιαγιά του (Ειρήνη Κουμαριανού) και τη συμπεθέρα Θεοπούλα (Έφη Παπαθεοδώρου) χάρισε μερικές από τις πιο ξεκαρδιστικές στιγμές της σειράς.",
      "Ο Γιώργος Καπουτζίδης εμπνεύστηκε μεγάλο μέρος των διαλόγων από προσωπικά του βιώματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["sto_para_pente", "greek_tv", "comedy", "kapoutzidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_080",
    "text": "Σε ποιον παγωμένο πλανήτη βρισκόταν η μυστική βάση 'Echo Base' των Επαναστατών στο 'The Empire Strikes Back' (1980);",
    "answers": [
      "Tatooine",
      "Endor",
      "Dagobah",
      "Hoth (Χοθ)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο πλανήτης Hoth είναι ένας αφιλόξενος κόσμος καλυμμένος από πάγο και χιόνι, όπου οι Επαναστάτες αντιμετώπισαν τα γιγάντια AT-AT walkers της Αυτοκρατορίας.",
    "funFacts": [
      "Τα γυρίσματα των εξωτερικών σκηνών του Hoth πραγματοποιήθηκαν στο χωριό Finse της Νορβηγίας κατά τη διάρκεια μιας σφοδρής χιονοθύελλας.",
      "Για να επιβιώσει στο πολικό ψύχος του πλανήτη, ο Han Solo έβαλε τον τραυματισμένο Luke μέσα στην κοιλιά ενός νεκρού Tauntaun."
    ],
    "source": "https://en.wikipedia.org/wiki/Hoth",
    "locale": "el-GR",
    "tags": ["star_wars", "hoth", "cinema", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_081",
    "text": "Ποιο ήταν το ακρωνύμιο της πρώτης τεχνητής νοημοσύνης που κατασκεύασε ο Tony Stark για να διαχειρίζεται τα συστήματά του;",
    "answers": [
      "J.A.R.V.I.S.",
      "F.R.I.D.A.Y.",
      "E.D.I.T.H.",
      "H.O.M.E.R."
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το J.A.R.V.I.S. σημαίνει 'Just A Rather Very Intelligent System' και πήρε το όνομά του προς τιμήν του παλιού μπάτλερ του πατέρα του, Edwin Jarvis.",
    "funFacts": [
      "Τη φωνή του J.A.R.V.I.S. δάνεισε ο Βρετανός ηθοποιός Paul Bettany πριν ενσαρκώσει με σάρκα και οστά τον Vision.",
      "Ο J.A.R.V.I.S. συγχωνεύτηκε τελικά με το Mind Stone και το συνθετικό σώμα vibranium για να γεννηθεί ο Vision στην ταινία 'Avengers: Age of Ultron'."
    ],
    "source": "https://en.wikipedia.org/wiki/J.A.R.V.I.S.",
    "locale": "el-GR",
    "tags": ["iron_man", "jarvis", "marvel", "mcu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_082",
    "text": "Ποια ημιαυτοβιογραφική ταινία του 2002 παρουσίασε τα πρώτα βήματα του Eminem στις ραπ μονομαχίες του Ντιτρόιτ;",
    "answers": [
      "Get Rich or Die Tryin'",
      "8 Mile",
      "Straight Outta Compton",
      "Notorious"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στην ταινία '8 Mile' ο Eminem υποδύθηκε τον Jimmy 'B-Rabbit' Smith Jr., έναν λευκό εργάτη εργοστασίου που παλεύει να κερδίσει τον σεβασμό στη σκηνή του underground hip hop.",
    "funFacts": [
      "Ο τίτλος '8 Mile' αναφέρεται στην οδό 8 Mile Road που χωρίζει τη μητροπολιτική πόλη του Ντιτρόιτ από τα βόρεια προάστια.",
      "Το τραγούδι 'Lose Yourself' που έγραψε για την ταινία κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού."
    ],
    "source": "https://en.wikipedia.org/wiki/8_Mile_(film)",
    "locale": "el-GR",
    "tags": ["8_mile", "eminem", "hip_hop", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_083",
    "text": "Ποιο ήταν το όνομα του δόκιμου αξιωματικού που υποδύθηκε ο Δημήτρης Παπαμιχαήλ στην ταινία 'Η Αλίκη στο ναυτικό' (1961);",
    "answers": [
      "Πάνος Φλωράς",
      "Αλέκος Κορτέσης",
      "Κώστας Δεληπέτρου",
      "Δημήτρης Νικολάου"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Δημήτρης Παπαμιχαήλ ενσάρκωσε τον δόκιμο του Βασιλικού Ναυτικού Κώστα Δεληπέτρου, τον οποίο ερωτεύεται η Αλίκη και τρυπώνει κρυφά στο πολεμικό πλοίο.",
    "funFacts": [
      "Η ταινία υπήρξε η πρώτη έγχρωμη παραγωγή της Φίνος Φιλμ και εκπροσώπησε ανεπίσημα την Ελλάδα στο Φεστιβάλ των Καννών.",
      "Τα γυρίσματα έγιναν με την άδεια του Γενικού Επιτελείου Ναυτικού πάνω στο ιστορικό καταδρομικό 'Έλλη'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%91%CE%BB%CE%AF%CE%BA%CE%B7_%CF%83%CF%84%CE%BF_%CE%BD%CE%B1%CF%85%CF%84%CE%B9%CE%BA%CF%8C",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vougiouklaki", "papamichael", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_084",
    "text": "Πώς ονομαζόταν το αρχαίο σπαθί του βασιλιά Elendil που έσπασε στη μάχη και ανασφυρηλατήθηκε αργότερα ως Andúril;",
    "answers": [
      "Glamdring",
      "Sting",
      "Orcrist",
      "Narsil (Νάρσιλ)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το Narsil έσπασε όταν ο Elendil έπεσε νεκρός, και με τη σπασμένη λαβή του ο Isildur έκοψε το Ένα Δαχτυλίδι από το χέρι του Sauron.",
    "funFacts": [
      "Τα θραύσματα του Narsil φυλάσσονταν στο Rivendell για χιλιάδες χρόνια μέχρι να ανασφυρηλατηθούν από τα ξωτικά για τον Aragorn.",
      "Το νέο όνομα Andúril σημαίνει στα σίνταριν 'Φλόγα της Δύσης'."
    ],
    "source": "https://en.wikipedia.org/wiki/Narsil",
    "locale": "el-GR",
    "tags": ["lord_of_the_rings", "narsil", "aragorn", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_085",
    "text": "Ποιος είναι ο περιβόητος αόρατος φίλος του Cosmo Kramer στη σειρά 'Seinfeld' του οποίου τις απίθανες ιστορίες διηγείται συνεχώς;",
    "answers": [
      "Bob Sacamano",
      "Art Vandelay",
      "Newman",
      "Lloyd Braun"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Bob Sacamano αναφέρεται συχνά από τον Kramer ως πηγή τρελών ιστοριών και παράξενων συμβουλών, αλλά δεν εμφανίζεται ποτέ στην οθόνη.",
    "funFacts": [
      "Ο χαρακτήρας πήρε το όνομά του από έναν πραγματικό φίλο του συνδημιουργού της σειράς Larry David.",
      "Το Seinfeld προβλήθηκε για 9 σεζόν (1989-1998) και θεωρείται ευρέως μία από τις σπουδαιότερες κωμικές σειρές όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/Seinfeld",
    "locale": "el-GR",
    "tags": ["seinfeld", "kramer", "sitcom", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_086",
    "text": "Ποιο είναι το υπερηρωικό όνομα και η δύναμη της μητέρας Helen Parr στην ταινία 'Οι Απίθανοι' (The Incredibles);",
    "answers": [
      "Invisible Woman (Αορατότητα)",
      "Elastigirl (Ακραία ελαστικότητα σώματος)",
      "Speedstar (Υπερταχύτητα)",
      "Stormy (Έλεγχος καιρού)"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Helen Parr είναι η Elastigirl, ικανή να τεντώνει, να λυγίζει και να μεταμορφώνει το σώμα της σε οποιοδήποτε σχήμα.",
    "funFacts": [
      "Στη δεύτερη ταινία ('Incredibles 2', 2018), η Elastigirl είναι η κεντρική πρωταγωνίστρια που επιλέγεται για την επιστροφή των υπερηρώων στη νομιμότητα.",
      "Τη φωνή της στην αυθεντική ταινία κάνει η ηθοποιός Holly Hunter."
    ],
    "source": "https://en.wikipedia.org/wiki/Elastigirl",
    "locale": "el-GR",
    "tags": ["the_incredibles", "elastigirl", "pixar", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_087",
    "text": "Ποιος κορυφαίος σκηνοθέτης του Χόλιγουντ σκηνοθέτησε το 18λεπτο βίντεο κλιπ του Michael Jackson για το τραγούδι 'Bad' (1987);",
    "answers": [
      "Στίβεν Σπίλμπεργκ",
      "Τζορτζ Λούκας",
      "Μάρτιν Σκορσέζε",
      "Φράνσις Φορντ Κόπολα"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Martin Scorsese σκηνοθέτησε το ασπρόμαυρο και έγχρωμο βίντεο κλιπ σε έναν σταθμό του μετρό του Μπρούκλιν.",
    "funFacts": [
      "Το βίντεο αποτέλεσε το κινηματογραφικό ντεμπούτο του ηθοποιού Wesley Snipes, ο οποίος υποδύθηκε τον αντίπαλο του Michael Jackson.",
      "Το άλμπουμ 'Bad' ήταν το πρώτο στην ιστορία που απέφερε πέντε συνεχόμενα νούμερο 1 singles στο Billboard Hot 100."
    ],
    "source": "https://en.wikipedia.org/wiki/Bad_(song)",
    "locale": "el-GR",
    "tags": ["michael_jackson", "martin_scorsese", "music_video", "80s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_088",
    "text": "Ποιο ήταν το επάγγελμα του Αλέκου Παπαδήμα (Κώστας Κόκλας) στην κλασική μαύρη κωμωδία 'Εγκλήματα';",
    "answers": [
      "Φαρμακοποιός",
      "Μανάβης",
      "Νεκροθάφτης",
      "Κρεοπώλης (χασάπης)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Αλέκος διατηρούσε κρεοπωλείο, το οποίο ήταν το βασικό σημείο όπου εκτυλίσσονταν οι απιστίες του με τη Φλώρα (Υρώ Μανέ).",
    "funFacts": [
      "Το χασάπικο του Αλέκου αποτέλεσε το επίκεντρο πολλών δολοφονικών παγίδων που του έστηνε η σύζυγός του Σωσώ.",
      "Η σειρά των Παπαπέτρου - Κωνσταντινίδη έσπασε τα ταμπού της εποχής γνωρίζοντας πρωτοφανή καλτ δημοτικότητα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["eglimata", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_089",
    "text": "Ποιο είναι το χαρακτηριστικό χειροκίνητο όπλο μάχης σώμα με σώμα του θεωρητικού φυσικού Gordon Freeman στη σειρά 'Half-Life';",
    "answers": [
      "Ένας κόκκινος λοστός (Crowbar)",
      "Μια βαριοπούλα",
      "Ένας πυροσβεστικός πέλεκυς",
      "Μια σιδερένια αλυσίδα"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο λοστός του Gordon Freeman έγινε το απόλυτο εμβληματικό σύμβολο ολόκληρης της σειράς παιχνιδιών Half-Life της Valve.",
    "funFacts": [
      "Ο Gordon Freeman είναι διάσημος ως ένας εντελώς 'σιωπηλός πρωταγωνιστής' που δεν αρθρώνει ούτε μία λέξη σε όλα τα παιχνίδια της σειράς.",
      "Το Half-Life (1998) άλλαξε για πάντα τα first-person shooters ενσωματώνοντας κινηματογραφική αφήγηση χωρίς διακοπή της ροής του παιχνιδιού."
    ],
    "source": "https://en.wikipedia.org/wiki/Gordon_Freeman",
    "locale": "el-GR",
    "tags": ["half_life", "valve", "gaming", "gordon_freeman"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_090",
    "text": "Ποιος θρυλικός Ιάπωνας οπλουργός στην Οκινάουα κατασκευάζει το σπαθί κατάνα της 'Νύφης' στην ταινία 'Kill Bill: Vol. 1' (2003);",
    "answers": [
      "Go-Go Yubari",
      "Hattori Hanzō (Χατόρι Χάνζο)",
      "Pai Mei",
      "Johnny Mo"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Hattori Hanzō (τον οποίο υποδύθηκε ο Sonny Chiba) είχε ορκιστεί να μην ξαναφτιάξει ποτέ φονικό όπλο, αλλά παραβιάζει τον όρκο του μόλις μαθαίνει ότι στόχος είναι ο Bill.",
    "funFacts": [
      "Ο Quentin Tarantino επέλεξε τον Sonny Chiba προς τιμήν των κλασικών ιαπωνικών ταινιών πολεμικών τεχνών και σαμουράι της δεκαετίας του 1970 στις οποίες πρωταγωνιστούσε.",
      "Η διάσημη ατάκα του Hanzō είναι ότι αν συναντούσε τον Θεό στον δρόμο του, το σπαθί αυτό θα μπορούσε να κόψει ακόμη κι Εκείνον."
    ],
    "source": "https://en.wikipedia.org/wiki/Kill_Bill:_Volume_1",
    "locale": "el-GR",
    "tags": ["kill_bill", "tarantino", "cinema", "hattori_hanzo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_091",
    "text": "Ποιος πανίσχυρος τηλεπαθητικός μεταλλαγμένος ίδρυσε τη Σχολή για Χαρισματικά Παιδιά και την ομάδα των X-Men στα κόμικς της Marvel;",
    "answers": [
      "Magneto (Erik Lehnsherr)",
      "Apocalypse (En Sabah Nur)",
      "Professor X (Charles Xavier)",
      "Cable (Nathan Summers)"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο καθηγητής Charles Xavier οραματίστηκε την ειρηνική συνύπαρξη ανθρώπων και μεταλλαγμένων, εκπαιδεύοντας τους X-Men στην έπαυλή του στη Νέα Υόρκη.",
    "funFacts": [
      "Στον κινηματογράφο τον Professor X ενσάρκωσαν ανεπανάληπτα ο Sir Patrick Stewart και ο James McAvoy.",
      "Η διαμάχη του Charles Xavier με τον Magneto θεωρείται συχνά παραλληλισμός με τις διαφορετικές προσεγγίσεις των Martin Luther King Jr. και Malcolm X για τα πολιτικά δικαιώματα."
    ],
    "source": "https://en.wikipedia.org/wiki/Professor_X",
    "locale": "el-GR",
    "tags": ["x_men", "professor_x", "marvel", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_092",
    "text": "Πώς ονομάζεται το στριπτιτζάδικο στο Νιου Τζέρσεϊ που λειτουργεί ως βασικό αρχηγείο της μαφίας του Tony Soprano στη σειρά 'The Sopranos';",
    "answers": [
      "Satriale's",
      "The Velvet Lounge",
      "Crazy Horse",
      "Bada Bing!"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το Bada Bing! (ή απλώς 'The Bing') ήταν το κλαμπ ιδιοκτησίας του Silvio Dante όπου η μαφία συγκεντρωνόταν για να σχεδιάσει τις δραστηριότητές της.",
    "funFacts": [
      "Τα γυρίσματα έγιναν σε ένα πραγματικό εν ενεργεία στριπ κλαμπ με το όνομα Satin Dolls στον αυτοκινητόδρομο Route 17 του Νιου Τζέρσεϊ.",
      "Η σειρά του David Chase θεωρείται ο προπομπός της σύγχρονης 'Χρυσής Εποχής της Τηλεόρασης'."
    ],
    "source": "https://en.wikipedia.org/wiki/Bada_Bing!",
    "locale": "el-GR",
    "tags": ["the_sopranos", "hbo", "tv", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_093",
    "text": "Ποιος πρωταγωνίστησε ως ο Αντώνης Κοκοβίκος δίπλα στη Μάρω Κοντού στην κλασική κωμωδία 'Η δε γυνή να φοβήται τον άνδρα' (1965);",
    "answers": [
      "Γιώργος Κωνσταντίνου",
      "Λάμπρος Κωνσταντάρας",
      "Δημήτρης Παπαμιχαήλ",
      "Αλέκος Αλεξανδράκης"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Γιώργος Κωνσταντίνου υποδύθηκε τον αυταρχικό δημόσιο υπάλληλο Αντώνη Κοκοβίκο, που συζούσε επί χρόνια ανύπαντρος με την υπομονετική Ελενίτσα.",
    "funFacts": [
      "Η ταινία σε σκηνοθεσία Γιώργου Τζαβέλλα κέρδισε το Βραβείο Σκηνοθεσίας στο Διεθνές Φεστιβάλ Κινηματογράφου του Σικάγο το 1965.",
      "Το ιστορικό νεοκλασικό σπίτι των Κοκοβίκων στην Πλάκα (οδός Τριπόδων) διασώζεται μέχρι σήμερα ως τουριστικό σημείο ενδιαφέροντος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B4%CE%B5_%CE%B3%CF%85%CE%BD%CE%AE_%CE%BD%CE%B1_%CF%86%CE%BF%CE%B2%CE%AE%CF%84%CE%B1%CE%B9_%CF%84%CE%BF%CE%BD_%CE%AC%CE%BD%CE%B4%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["greek_cinema", "konstantinou", "kontou", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_094",
    "text": "Ποια ποπ σταρ κυκλοφόρησε το 2011 τον φεμινιστικό χορευτικό ύμνο 'Run the World (Girls)' με ηλεκτρονικά αφρικανικά beats;",
    "answers": [
      "Rihanna",
      "Beyoncé",
      "Lady Gaga",
      "Shakira"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Beyoncé κυκλοφόρησε το 'Run the World (Girls)' ως το βασικό single του τέταρτου προσωπικού της άλμπουμ '4'.",
    "funFacts": [
      "Το τραγούδι βασίζεται σε sample από το διάσημο club κομμάτι 'Pon de Floor' των Major Lazer.",
      "Για το βίντεο κλιπ, η Beyoncé προσέλαβε και χόρεψε μαζί με τους Tofo Tofo, μια ομάδα χορευτών από τη Μοζαμβίκη που είχε ανακαλύψει στο YouTube."
    ],
    "source": "https://en.wikipedia.org/wiki/Run_the_World_(Girls)",
    "locale": "el-GR",
    "tags": ["beyonce", "music", "pop", "dance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_095",
    "text": "Ποιο είναι το όνομα του πιστού ταράνδου που συντροφεύει τον Κρίστοφ στην ταινία 'Frozen' (2013);",
    "answers": [
      "Όλαφ",
      "Χανς",
      "Σβεν (Sven)",
      "Μπούλντα"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Sven είναι ο αχώριστος τάρανδος του Kristoff, που συμπεριφέρεται περισσότερο σαν πιστός σκύλος παρά σαν άγριος τάρανδος.",
    "funFacts": [
      "Για να σχεδιάσουν ρεαλιστικά τις κινήσεις του ταράνδου, οι σχεδιαστές της Disney έφεραν έναν ζωντανό τάρανδο μέσα στα στούντιο κινουμένων σχεδίων.",
      "Ο Kristoff μιλάει συχνά εκ μέρους του Sven κάνοντας μια αστεία μπάσα φωνή."
    ],
    "source": "https://en.wikipedia.org/wiki/Frozen_(2013_film)",
    "locale": "el-GR",
    "tags": ["frozen", "disney", "animation", "sven"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_096",
    "text": "Ποιο μέλος του πληρώματος του Nebuchadnezzar προδίδει τον Μορφέα στους Πράκτορες για μια ψεύτικη πλούσια ζωή στο 'The Matrix';",
    "answers": [
      "Mouse",
      "Tank",
      "Dozer",
      "Cypher"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Cypher (Joe Pantoliano) συναντά κρυφά τον Agent Smith σε ένα πολυτελές εικονικό εστιατόριο προφέροντας τη φράση 'Ignorance is bliss'.",
    "funFacts": [
      "Η σκηνή όπου ο Cypher τρώει μια ζουμερή ζεστή μπριζόλα γνωρίζοντας ότι είναι ψευδαίσθηση αποτελεί διάσημο φιλοσοφικό παράδειγμα της 'μηχανής εμπειριών' του Robert Nozick.",
      "Το πραγματικό του όνομα στον πραγματικό κόσμο ήταν Reagan."
    ],
    "source": "https://en.wikipedia.org/wiki/Cypher_(The_Matrix)",
    "locale": "el-GR",
    "tags": ["the_matrix", "cypher", "cinema", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_097",
    "text": "Ποιες τρεις μοναδικές διαστημικές φυλές πολεμούν για την κυριαρχία στο στρατηγικό παιχνίδι 'StarCraft' της Blizzard;",
    "answers": [
      "Terran, Zerg, Protoss",
      "Humans, Orcs, Elves",
      "Empire, Rebels, Mandalorians",
      "Covenant, Flood, UNSC"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το StarCraft (1998) εισήγαγε τρεις απόλυτα ασύμμετρες αλλά τέλεια ισορροπημένες φυλές: τους ανθρώπους Terran, τα βιολογικά έντομα Zerg και τους υπερεξελιγμένους ψιονικούς Protoss.",
    "funFacts": [
      "Το παιχνίδι έγινε εθνικό άθλημα στη Νότια Κορέα, δημιουργώντας την πρώτη επαγγελματική σκηνή esports με τηλεοπτικά κανάλια και γεμάτα στάδια.",
      "Η φράση 'Zerg rush' καταχωρήθηκε επίσημα στο αγγλικό λεξικό ως όρος για τη μαζική συντριπτική επίθεση."
    ],
    "source": "https://en.wikipedia.org/wiki/StarCraft",
    "locale": "el-GR",
    "tags": ["starcraft", "blizzard", "gaming", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_098",
    "text": "Ποιο ήταν το επάγγελμα του πατριάρχη Βαγγέλη Χαμπέα (Γιώργος Γιαννόπουλος) στην κωμική σειρά 'Το Σόι σου';",
    "answers": [
      "Φαρμακοποιός",
      "Χονδρέμπορος κρεάτων (κρεοπώλης)",
      "Ιδιοκτήτης ταξί",
      "Εργολάβος οικοδομών"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Βαγγέλης Χαμπέας διατηρούσε μεγάλο κρεοπωλείο και υπερηφανευόταν διαρκώς για τα ποιοτικά κρέατά του στα κυριακάτικα οικογενειακά τραπέζια.",
    "funFacts": [
      "Οι ατάκες του 'Το παιδί μου!' και οι συνεχείς κόντρες του με τον συμπεθέρα Μενέλαο Τριαντάφυλλο (γιατρό) ήταν ο βασικός κωμικός πυρήνας της σειράς.",
      "Η σειρά προβλήθηκε για 5 σεζόν (2014-2019) στον Alpha."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["to_soi_sou", "greek_tv", "comedy", "alpha"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_099",
    "text": "Ποιο εμβληματικό σύνθημα αναγράφεται στην αφίσα με τον ιπτάμενο δίσκο στο υπόγειο γραφείο του Fox Mulder στα 'The X-Files';",
    "answers": [
      "The Truth Is Out There",
      "Trust No One",
      "I Want to Believe",
      "Deny Everything"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η αφίσα 'I Want to Believe' με τη θολή φωτογραφία UFO στον τοίχο του πράκτορα Mulder έγινε ένα από τα πιο αναγνωρίσιμα σύμβολα στην ιστορία της τηλεόρασης.",
    "funFacts": [
      "Ο δημιουργός της σειράς Chris Carter επέλεξε προσωπικά τη φωτογραφία του UFO, η οποία προερχόταν από τον Ελβετό φωτογράφο Billy Meier.",
      "Η αφίσα κάηκε και αντικαταστάθηκε αρκετές φορές στη διάρκεια των έντεκα σεζόν της σειράς."
    ],
    "source": "https://en.wikipedia.org/wiki/The_X-Files",
    "locale": "el-GR",
    "tags": ["the_x_files", "fox_mulder", "sci_fi", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_100",
    "text": "Ποιο ιστορικό βρετανικό hard rock συγκρότημα κυκλοφόρησε το 1971 το μνημειώδες τραγούδι 'Stairway to Heaven';",
    "answers": [
      "Deep Purple",
      "Black Sabbath",
      "The Who",
      "Led Zeppelin"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι Led Zeppelin (Robert Plant, Jimmy Page, John Paul Jones, John Bonham) συμπεριέλαβαν το 'Stairway to Heaven' στο τέταρτο άλμπουμ τους, Led Zeppelin IV.",
    "funFacts": [
      "Το κιθαριστικό σόλο του Jimmy Page στο τέλος του κομματιού ψηφίζεται σταθερά από μουσικά περιοδικά ως το σπουδαιότερο σόλο στην ιστορία της ροκ.",
      "Το τραγούδι δεν κυκλοφόρησε ποτέ ως εμπορικό single στις ΗΠΑ, αλλά έγινε το κομμάτι με τις περισσότερες ραδιοφωνικές μεταδόσεις στα αμερικανικά FM της δεκαετίας του '70."
    ],
    "source": "https://en.wikipedia.org/wiki/Stairway_to_Heaven",
    "locale": "el-GR",
    "tags": ["led_zeppelin", "rock", "music", "70s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_101",
    "text": "Ποιος αγαπημένος ηθοποιός κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου για την ερμηνεία του ως ψυχολόγος Sean Maguire στο 'Ο Ξεχωριστός Γουίλ Χάντινγκ' (1997);",
    "answers": [
      "Ρόμπιν Ουίλιαμς",
      "Μπεν Άφλεκ",
      "Ματ Ντέιμον",
      "Στέλαν Σκάρσγκορντ"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Robin Williams κέρδισε το μοναδικό Όσκαρ της καριέρας του για τη συγκλονιστική δραματική του ερμηνεία απέναντι στον Matt Damon.",
    "funFacts": [
      "Η διάσημη συγκινητική σκηνή όπου μιλάει για τη σύζυγό του που έκλανε στον ύπνο της ήταν εντελώς αυτοσχέδια από τον Robin Williams, κάνοντας το συνεργείο να τρέμει από τα γέλια.",
      "Το σενάριο της ταινίας έγραψαν οι τότε νεαροί άγνωστοι ηθοποιοί Matt Damon και Ben Affleck, κερδίζοντας επίσης το Όσκαρ Πρωτότυπου Σεναρίου."
    ],
    "source": "https://en.wikipedia.org/wiki/Good_Will_Hunting",
    "locale": "el-GR",
    "tags": ["good_will_hunting", "robin_williams", "cinema", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_102",
    "text": "Από ποιον κατεστραμμένο εξωγήινο πλανήτη κατάγεται η Kara Zor-El, γνωστή ως η υπερηρωίδα Supergirl;",
    "answers": [
      "Daxam",
      "Κρύπτων (Krypton)",
      "Colu",
      "Thanagar"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Supergirl είναι πρώτη ξαδέλφη του Kal-El (Superman) από την πόλη Argo City του πλανήτη Κρύπτωνα.",
    "funFacts": [
      "Το σκάφος της εκτοξεύτηκε την ίδια στιγμή με του Superman, αλλά παγιδεύτηκε σε μετέωρο χρόνο στο Phantom Zone, με αποτέλεσμα να φτάσει στη Γη χρόνια αργότερα ως έφηβη.",
      "Η Supergirl πρωτοεμφανίστηκε στο τεύχος Action Comics #252 το 1959."
    ],
    "source": "https://en.wikipedia.org/wiki/Supergirl",
    "locale": "el-GR",
    "tags": ["supergirl", "superman", "dc_comics", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_103",
    "text": "Ποιος σπουδαίος ηθοποιός ενσάρκωσε τον αυστηρό γυμνασιάρχη πατέρα στην κοινωνική δραματική ταινία 'Νόμος 4000' (1962);",
    "answers": [
      "Μάνος Κατράκης",
      "Δημήτρης Χορν",
      "Βασίλης Διαμαντόπουλος",
      "Παντελής Ζερβός"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Βασίλης Διαμαντόπουλος υποδύθηκε τον αυστηρό καθηγητή που εφαρμόζει σκληρά τον νόμο περί τεντιμποϊσμού, μέχρι που ανακαλύπτει τα μυστικά της δικής του κόρης.",
    "funFacts": [
      "Η ταινία του Γιάννη Δαλιανίδη βασίστηκε στον πραγματικό αναγκαστικό νόμο 4000/1958 που επέβαλε δημόσιο διασυρμό (κούρεμα με την ψιλή και διαπόμπευση) στους νεαρούς 'τεντιμπόηδες'.",
      "Η ταινία έκοψε πάνω από 118.000 εισιτήρια στην πρώτη της προβολή και προκάλεσε έντονες κοινωνικές συζητήσεις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%8C%CE%BC%CE%BF%CF%82_4000_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "diamantopoulos", "dalianidis", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_104",
    "text": "Πώς ονομάζεται ο αγαπημένος λούτρινος πιγκουίνος του Joey Tribbiani στη σειρά 'Τα Φιλαράκια' (Friends);",
    "answers": [
      "Flipper",
      "Pingu",
      "Waddles",
      "Hugsy"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Hugsy ('the bedtime pal') είναι ο λούτρινος πιγκουίνος του Joey με γυαλιά και μάλλινο σκούφο, τον οποίο αρνείται να αποχωριστεί.",
    "funFacts": [
      "Σε ένα επεισόδιο, ο Joey προσπαθεί απεγνωσμένα να πάρει πίσω τον Hugsy από τη μικρή κόρη της Rachel, Emma.",
      "Ο Matt LeBlanc κράτησε τον αυθεντικό Hugsy μετά το τέλος των γυρισμάτων της σειράς."
    ],
    "source": "https://en.wikipedia.org/wiki/Joey_Tribbiani",
    "locale": "el-GR",
    "tags": ["friends", "joey_tribbiani", "hugsy", "sitcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_105",
    "text": "Ποιος Ισπανός σταρ δάνεισε την ακαταμάχητη φωνή του στον Γατούλη Σπιρουνάτο (Puss in Boots) στην ταινία 'Shrek 2' (2004);",
    "answers": [
      "Αντόνιο Μπαντέρας",
      "Χαβιέ Μπαρδέμ",
      "Πέδρο Αλμοδόβαρ",
      "Μπενίσιο ντελ Τόρο"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Antonio Banderas υποδύθηκε τον χαρακτήρα παρωδώντας τον δικό του θρυλικό ρόλο ως Ζορό (Zorro).",
    "funFacts": [
      "Ο Banderas ηχογράφησε τη φωνή του Puss in Boots στα αγγλικά, ισπανικά και ιταλικά για τη διεθνή διανομή της ταινίας.",
      "Το χαρακτηριστικό βλέμμα με τα τεράστια συγκινητικά μάτια που κάνει ο γάτος έγινε ένα από τα πιο διάσημα memes του διαδικτύου."
    ],
    "source": "https://en.wikipedia.org/wiki/Puss_in_Boots_(Shrek)",
    "locale": "el-GR",
    "tags": ["shrek", "puss_in_boots", "antonio_banderas", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_106",
    "text": "Ποιο είδος πραγματικού παρασιτικού μύκητα ενέπνευσε τη μόλυνση των ανθρώπων στο βιντεοπαιχνίδι 'The Last of Us';",
    "answers": [
      "Aspergillus",
      "Cordyceps (Κόρντισεπς)",
      "Candida",
      "Penicillium"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο μύκητας Ophiocordyceps unilateralis μολύνει στην πραγματικότητα έντομα (μυρμήγκια ζόμπι), ελέγχοντας το νευρικό τους σύστημα.",
    "funFacts": [
      "Ο δημιουργός Neil Druckmann εμπνεύστηκε την ιστορία αφού παρακολούθησε ένα ντοκιμαντέρ του BBC Planet Earth με μολυσμένα μυρμήγκια.",
      "Η τηλεοπτική μεταφορά του παιχνιδιού από το HBO με τον Pedro Pascal και την Bella Ramsey γνώρισε σαρωτική επιτυχία κερδίζοντας 8 βραβεία Emmy."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Last_of_Us",
    "locale": "el-GR",
    "tags": ["the_last_of_us", "naughty_dog", "gaming", "cordyceps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_107",
    "text": "Ποιο ήταν το πρώτο single της Adele από το άλμπουμ '19' (2008) που της χάρισε το πρώτο της βραβείο Grammy;",
    "answers": [
      "Hometown Glory",
      "Make You Feel My Love",
      "Chasing Pavements",
      "Cold Shoulder"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'Chasing Pavements' αποτέλεσε το διεθνές breakthrough της Adele, κερδίζοντας το βραβείο Grammy Καλύτερης Γυναικείας Pop Φωνητικής Ερμηνείας το 2009.",
    "funFacts": [
      "Η Adele έγραψε το τραγούδι μετά από έναν καβγά σε ένα κλαμπ του Λονδίνου στις έξι το πρωί, τρέχοντας μόνη της στον δρόμο.",
      "Το μουσικό βίντεο κλιπ σκηνοθετήθηκε από τον Matthew Cullen και περιλάμβανε μια χορογραφία ανθρώπων ξαπλωμένων στην άσφαλτο."
    ],
    "source": "https://en.wikipedia.org/wiki/Chasing_Pavements",
    "locale": "el-GR",
    "tags": ["adele", "music", "pop", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_108",
    "text": "Ποιο ήταν το παρατσούκλι του εκκεντρικού κολλητού φίλου του Λεωνίδα (Χάρης Βορκάς) στη σειρά 'Δέκα Λεπτά Κήρυγμα';",
    "answers": [
      "Μπίλης",
      "Φώτης",
      "Νικόλας",
      "Τέλης"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Τέλης (Τελεσίφορος) ήταν ο αχώριστος φίλος του Λεωνίδα, γνωστός για το ιδιαίτερο ντύσιμό του και τις απίθανες ιδέες του.",
    "funFacts": [
      "Η σειρά του Κώστα Κιμούλη προβλήθηκε με τεράστια επιτυχία στο Mega από το 2000 έως το 2004.",
      "Ο χαρακτήρας του Τέλη αγαπήθηκε ιδιαίτερα από τους τηλεθεατές για τις διαρκείς ατάκες και την κωμική του αφέλεια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BA%CE%B1_%CE%BB%CE%B5%CF%80%CF%84%CE%AC_%CE%BA%CE%AE%CF%81%CF%85%CE%B3%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["deka_lepta_kirygma", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_109",
    "text": "Ποιος εκκεντρικός Σκωτσέζος ηθοποιός και σκηνοθέτης ενσάρκωσε τον δισεκατομμυριούχο ιδρυτή John Hammond στο 'Jurassic Park' (1993);",
    "answers": [
      "Ρίτσαρντ Ατένμπορο (Richard Attenborough)",
      "Σον Κόνερι",
      "Μάικλ Κέιν",
      "Άντονι Χόπκινς"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Richard Attenborough (βραβευμένος με Όσκαρ σκηνοθέτης του 'Gandhi') υποδύθηκε τον οραματιστή δημιουργό του πάρκου που επαναλάμβανε διαρκώς 'Spared no expense!'.",
    "funFacts": [
      "Ο Steven Spielberg παρακάλεσε τον Attenborough να επιστρέψει στην υποκριτική μετά από 14 χρόνια αποχής ειδικά για τον ρόλο του Hammond.",
      "Ο Richard Attenborough ήταν ο μεγαλύτερος αδελφός του διάσημου φυσιοδίφη και παρουσιαστή ντοκιμαντέρ Sir David Attenborough."
    ],
    "source": "https://en.wikipedia.org/wiki/Richard_Attenborough",
    "locale": "el-GR",
    "tags": ["jurassic_park", "attenborough", "cinema", "spielberg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_110",
    "text": "Ποιο ιστορικό σπαθί από βαλυριανό ατσάλι κρατά ο πρίγκιπας Daemon Targaryen στη σειρά 'House of the Dragon';",
    "answers": [
      "Blackfyre",
      "Dark Sister (Σκοτεινή Αδελφή)",
      "Heartsbane",
      "Lady Forlorn"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το Dark Sister είναι ένα από τα δύο προγονικά σπαθιά από βαλυριανό ατσάλι του οίκου Targaryen, φτιαγμένο αρχικά για τη βασίλισσα Visenya.",
    "funFacts": [
      "Το σπαθί είναι λεπτότερο και ελαφρύτερο από το Blackfyre, σχεδιασμένο ειδικά για να εξυπηρετεί γρήγορες κινήσεις σε μονομαχία.",
      "Τον ρόλο του απρόβλεπτου πρίγκιπα Daemon Targaryen υποδύεται ο Matt Smith."
    ],
    "source": "https://en.wikipedia.org/wiki/House_of_the_Dragon",
    "locale": "el-GR",
    "tags": ["house_of_the_dragon", "daemon_targaryen", "valyrian_steel", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'medium', 3, questions)

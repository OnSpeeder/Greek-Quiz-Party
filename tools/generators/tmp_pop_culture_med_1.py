# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_med_011",
    "text": "Ποια βραβευμένη με Όσκαρ ηθοποιός υποδύθηκε τη μοχθηρή Hela, Θεά του Θανάτου, στην ταινία 'Thor: Ragnarok' (2017);",
    "answers": [
      "Κέιτ Μπλάνσετ",
      "Τίλντα Σουίντον",
      "Νικόλ Κίντμαν",
      "Σαρλίζ Θερόν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Cate Blanchett ενσάρκωσε την πρωτότοκη κόρη του Όντιν και πανίσχυρη Θεά του Θανάτου, Hela, που κατέστρεψε το Mjolnir.",
    "funFacts": [
      "Η Cate Blanchett δήλωσε ότι δέχτηκε τον ρόλο κυρίως επειδή τα παιδιά της ήταν φανατικοί θαυμαστές των κόμικς της Marvel.",
      "Για τις σκηνές μάχης, η ηθοποιός προπονήθηκε στην παραδοσιακή βραζιλιάνικη πολεμική τέχνη Capoeira."
    ],
    "source": "https://en.wikipedia.org/wiki/Thor:_Ragnarok",
    "locale": "el-GR",
    "tags": ["thor", "marvel", "mcu", "cate_blanchett"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_012",
    "text": "Ποια αλυσίδα εστιατορίων γρήγορου φαγητού με τηγανητό κοτόπουλο χρησιμοποιούσε ως βιτρίνα ο Gus Fring στο 'Breaking Bad';",
    "answers": [
      "Cluckin' Bell",
      "Los Pollos Hermanos",
      "El Pollo Loco",
      "Twisters"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'Los Pollos Hermanos' (Τα Αδέλφια Κοτόπουλα) ήταν η δημοφιλής αλυσίδα φαστ φουντ που κάλυπτε το δίκτυο διακίνησης μεθαμφεταμίνης του Fring.",
    "funFacts": [
      "Το πραγματικό εστιατόριο στο Albuquerque όπου γυρίστηκαν οι σκηνές ανήκει στην τοπική αλυσίδα Twisters και αποτελεί δημοφιλές τουριστικό αξιοθέατο.",
      "Το όνομα Los Pollos Hermanos αναφερόταν στον Gus Fring και στον αδικοχαμένο συνεργάτη και φίλο του Max Arciniega."
    ],
    "source": "https://en.wikipedia.org/wiki/Los_Pollos_Hermanos",
    "locale": "el-GR",
    "tags": ["breaking_bad", "gus_fring", "tv", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_013",
    "text": "Ποιος ποιητής και τραγουδιστής ήταν ο εμβληματικός frontman του ροκ συγκροτήματος The Doors μέχρι τον πρόωρο θάνατό του το 1971;",
    "answers": [
      "Ρέι Μάνζαρεκ",
      "Ρόμπερτ Πλαντ",
      "Τζιμ Μόρισον",
      "Τζάνις Τζόπλιν"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Jim Morrison (1943-1971), γνωστός και ως 'The Lizard King', ήταν ο χαρισματικός τραγουδιστής και στιχουργός των Doors.",
    "funFacts": [
      "Ο Jim Morrison απεβίωσε στο Παρίσι σε ηλικία μόλις 27 ετών, εντασσόμενος στο περίφημο άτυπο 'Club 27'.",
      "Ο τάφος του στο κοιμητήριο Père Lachaise στο Παρίσι παραμένει ένα από τα πιο επισκέψιμα σημεία της γαλλικής πρωτεύουσας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%B9%CE%BC_%CE%9C%CF%8C%CF%81%CE%B9%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["the_doors", "jim_morrison", "rock", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_014",
    "text": "Ποιος νεαρός γόης του ελληνικού σινεμά υποδύθηκε τον βιολονίστα Άλκη στην κωμωδία 'Μια τρελή... τρελή σαραντάρα' (1970);",
    "answers": [
      "Αλέκος Αλεξανδράκης",
      "Φαίδων Γεωργίτσης",
      "Κώστας Πρέκας",
      "Ανδρέας Μπάρκουλης"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Ανδρέας Μπάρκουλης έπαιξε τον γοητευτικό νεαρό μουσικό Άλκη που ερωτεύεται την ώριμη χήρα Τζένη Πετρομιχάλη (Ρένα Βλαχοπούλου).",
    "funFacts": [
      "Η ταινία σε σκηνοθεσία Γιάννη Δαλιανίδη βασίστηκε στο ομώνυμο θεατρικό έργο των Αλέκου Σακελλάριου και Χρήστου Γιαννακόπουλου.",
      "Η ατάκα 'Κορίτσια, ο Μπάρκουλης!' είχε γίνει τότε σλόγκαν στην Αθήνα λόγω της τεράστιας δημοτικότητας του ηθοποιού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CF%84%CF%81%CE%B5%CE%BB%CE%AE..._%CF%84%CF%81%CE%B5%CE%BB%CE%AE_%CF%83%CE%B1%CF%81%CE%B1%CE%BD%CF%84%CE%AC%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["greek_cinema", "barkoulis", "vlachopoulou", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_015",
    "text": "Ποιο είναι το πραγματικό μικρό όνομα της μικρής ανθρώπινης ηρωίδας 'Μπου' (Boo) στην ταινία 'Μπαμπούλας Α.Ε.' (Monsters, Inc.);",
    "answers": [
      "Mary (Μαίρη)",
      "Lily (Λίλη)",
      "Emma (Έμμα)",
      "Chloe (Χλόη)"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το πραγματικό όνομα της Boo αποκαλύπτεται φευγαλέα σε μία από τις ζωγραφιές της στο δωμάτιό της, όπου υπογράφει ως 'Mary'.",
    "funFacts": [
      "Η μικρή πήρε το όνομά της από τη Mary Gibbs, τη μικρή κόρη ενός εκ των σχεδιαστών της Pixar, η οποία έκανε τη φωνή του χαρακτήρα.",
      "Επειδή η Mary Gibbs ήταν μόλις νήπιο κατά τις ηχογραφήσεις, η ομάδα ήχου την ακολουθούσε στο στούντιο καταγράφοντας τις αυθόρμητες κουβέντες και τα γέλια της."
    ],
    "source": "https://en.wikipedia.org/wiki/Monsters,_Inc.",
    "locale": "el-GR",
    "tags": ["monsters_inc", "pixar", "animation", "trivia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_016",
    "text": "Σε ποιο μυθιστόρημα του συγγραφέα επιστημονικής φαντασίας Philip K. Dick βασίστηκε η κλασική ταινία 'Blade Runner' (1982);",
    "answers": [
      "Ubik",
      "Do Androids Dream of Electric Sheep?",
      "A Scanner Darkly",
      "The Man in the High Castle"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το αριστούργημα του Ridley Scott βασίστηκε στο βιβλίο 'Do Androids Dream of Electric Sheep?' (Ηλεκτρικό Πρόβατο) του 1968.",
    "funFacts": [
      "Ο Philip K. Dick πρόλαβε να δει αποσπάσματα των ειδικών εφέ της ταινίας πριν πεθάνει το 1982 και δήλωσε ενθουσιασμένος με την οπτική απόδοση του κόσμου του.",
      "Ο όρος 'Replicants' (Ανδροειδή) επινοήθηκε ειδικά για το σενάριο της ταινίας από τον σεναριογράφο David Peoples."
    ],
    "source": "https://en.wikipedia.org/wiki/Blade_Runner",
    "locale": "el-GR",
    "tags": ["blade_runner", "ridley_scott", "sci_fi", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_017",
    "text": "Ποιο ασυνήθιστο μεσαίο όνομα αποκαλύπτεται ότι έχει ο Chandler Bing στη σειρά 'Τα Φιλαράκια' (Friends);",
    "answers": [
      "Francis",
      "Eustace",
      "Muriel",
      "Eugene"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στην 7η σεζόν αποκαλύπτεται ότι το αρχικό 'M' στο Chandler M. Bing αντιστοιχεί στο όνομα 'Muriel', ένα παραδοσιακά γυναικείο όνομα που ήταν οικογενειακό κειμήλιο.",
    "funFacts": [
      "Ο Chandler κράτησε το μεσαίο του όνομα μυστικό για χρόνια μέχρι που ο Ross το αποκάλυψε κατά λάθος στην παρέα.",
      "Τον εκκεντρικό πατέρα του Chandler υποδύθηκε η σπουδαία ηθοποιός Kathleen Turner."
    ],
    "source": "https://en.wikipedia.org/wiki/Chandler_Bing",
    "locale": "el-GR",
    "tags": ["friends", "chandler_bing", "sitcom", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_018",
    "text": "Πώς ονομαζόταν το μπαρ στο οποίο εργάζονταν ως σερβιτόρες η Ελένη Βλαχάκη και η Πέγκυ Καρρά στη σειρά 'Κωνσταντίνου και Ελένης';",
    "answers": [
      "Το Στέκι",
      "Η Βαρέλα",
      "Το Κουτούκι",
      "Το Μαύρο Πρόβατο"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Ελένη και η Πέγκυ δούλευαν στο μπαρ 'Το Μαύρο Πρόβατο' με ιδιοκτήτη τον Νικόλα Βαρθακούρη (Βασίλης Χαραλαμπόπουλος).",
    "funFacts": [
      "Ο μπάρμαν Νικόλας ήταν ο κολλητός φίλος της Ελένης και είχε το παρατσούκλι 'οινοχόος'.",
      "Στο ίδιο μπαρ σύχναζαν όλοι οι πρωταγωνιστές, αποτελώντας ένα από τα βασικά σκηνικά της σειράς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["konstantinou_kai_elenis", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_019",
    "text": "Ποιο πρωτοποριακό ηλεκτρονικό ποπ άλμπουμ του 1998 χάρισε στη Madonna τέσσερα βραβεία Grammy σε παραγωγή του William Orbit;",
    "answers": [
      "Ray of Light",
      "Music",
      "Bedtime Stories",
      "Confessions on a Dance Floor"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'Ray of Light' σηματοδότησε μια νέα δημιουργική εποχή για τη Madonna, ενσωματώνοντας ambient, techno και trip-hop στοιχεία.",
    "funFacts": [
      "Το ομώνυμο τραγούδι 'Ray of Light' βασίστηκε στη μελωδία του κομματιού 'Sepheryn' του Curtiss Maldoon από το 1971.",
      "Η φωνή της Madonna παρουσίασε εντυπωσιακή βελτίωση στο άλμπουμ χάρη στα εντατικά μαθήματα φωνητικής που είχε κάνει για την ταινία 'Evita'."
    ],
    "source": "https://en.wikipedia.org/wiki/Ray_of_Light",
    "locale": "el-GR",
    "tags": ["madonna", "ray_of_light", "music", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_020",
    "text": "Ποιος Γάλλος ηθοποιός ενσάρκωσε το αλαζονικό αρχαίο πρόγραμμα 'Merovingian' στην ταινία 'The Matrix Reloaded' (2003);",
    "answers": [
      "Βενσάν Κασέλ",
      "Λαμπέρ Γουίλσον",
      "Ζαν Ρενό",
      "Ματιέ Κασοβίτς"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Lambert Wilson υποδύθηκε τον Merovingian (Γάλλο), έναν παλιό κώδικα του Matrix με πάθος για τη γαλλική γλώσσα, τα κρασιά και την αιτιότητα (causality).",
    "funFacts": [
      "Τη σύζυγό του Περσεφόνη στην ταινία υποδύθηκε η Ιταλίδα σταρ Monica Bellucci.",
      "Ο Merovingian έχει μια αξέχαστη σκηνή όπου εξηγεί φιλοσοφικά γιατί θεωρεί τη γαλλική γλώσσα την καλύτερη στον κόσμο για να βρίζει κανείς."
    ],
    "source": "https://en.wikipedia.org/wiki/Merovingian_(The_Matrix)",
    "locale": "el-GR",
    "tags": ["the_matrix", "merovingian", "cinema", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_021",
    "text": "Ποιο σκοτεινό παρατσούκλι απέκτησε ο Geralt of Rivia στη σειρά 'The Witcher' μετά τη σφαγή της συμμορίας της Renfri;",
    "answers": [
      "The White Wolf",
      "The Kingslayer",
      "The Butcher of Blaviken (Ο Χασάπης του Μπλάβικεν)",
      "The Bane of Monsters"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Geralt αναγκάστηκε να εξοντώσει τη συμμορία της Renfri στην αγορά του Blaviken για να σώσει την πόλη, αλλά οι κάτοικοι τον θεώρησαν αδίστακτο σφαγέα.",
    "funFacts": [
      "Το προσωνύμιο αυτό ακολουθεί τον Geralt σε όλα τα βιβλία του Andrzej Sapkowski και στα βιντεοπαιχνίδια της CD Projekt Red.",
      "Η χορογραφία της μονομαχίας στο Blaviken στο πρώτο επεισόδιο της σειράς του Netflix απέσπασε διθυραμβικά σχόλια για τον ρεαλισμό της."
    ],
    "source": "https://en.wikipedia.org/wiki/Geralt_of_Rivia",
    "locale": "el-GR",
    "tags": ["the_witcher", "geralt", "gaming", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_022",
    "text": "Ποιο είναι το πραγματικό όνομα και alter ego της Catwoman στα κόμικς και τις ταινίες του Batman;",
    "answers": [
      "Pamela Isley",
      "Harleen Quinzel",
      "Talia al Ghul",
      "Selina Kyle"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Selina Kyle είναι η ικανότατη διαρρήκτρια και κατά καιρούς σύμμαχος ή ερωτική σύντροφος του Batman.",
    "funFacts": [
      "Στον κινηματογράφο τη Selina Kyle έχουν υποδυθεί κορυφαίες ηθοποιοί όπως η Michelle Pfeiffer (1992), η Anne Hathaway (2012) και η Zoë Kravitz (2022).",
      "Η Catwoman πρωτοεμφανίστηκε στο ιστορικό τεύχος Batman #1 το 1940 με το απλό όνομα 'The Cat'."
    ],
    "source": "https://en.wikipedia.org/wiki/Catwoman",
    "locale": "el-GR",
    "tags": ["catwoman", "batman", "dc_comics", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_023",
    "text": "Ποιος ήταν ο αριθμός παίκτη του Seong Gi-hun, του κεντρικού πρωταγωνιστή στη σειρά 'Squid Game';",
    "answers": [
      "Παίκτης 456",
      "Παίκτης 001",
      "Παίκτης 218",
      "Παίκτης 067"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Seong Gi-hun ήταν ο τελευταίος διαγωνιζόμενος που μπήκε στο παιχνίδι, φορώντας τον αριθμό 456 στην πράσινη φόρμα του.",
    "funFacts": [
      "Ο ηθοποιός Lee Jung-jae κέρδισε το Βραβείο Emmy Α' Ανδρικού Ρόλου σε Δραματική Σειρά, γράφοντας ιστορία ως ο πρώτος Ασιάτης ηθοποιός που το κατακτά για μη αγγλόφωνο ρόλο.",
      "Το συνολικό χρηματικό έπαθλο του παιχνιδιού ήταν 45,6 δισεκατομμύρια κορεατικά γουόν (100 εκατομμύρια για κάθε έναν από τους 456 παίκτες)."
    ],
    "source": "https://en.wikipedia.org/wiki/Seong_Gi-hun",
    "locale": "el-GR",
    "tags": ["squid_game", "netflix", "lee_jung_jae", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_024",
    "text": "Ποιος σπουδαίος σκηνοθέτης υπέγραψε τα μεγαλύτερα κινηματογραφικά μιούζικαλ της Φίνος Φιλμ, όπως 'Μερικοί το προτιμούν κρύο' και 'Γοργόνες και Μάγκες';",
    "answers": [
      "Αλέκος Σακελλάριος",
      "Γιάννης Δαλιανίδης",
      "Ντίνος Δημόπουλος",
      "Βασίλης Γεωργιάδης"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Γιάννης Δαλιανίδης υπήρξε ο απόλυτος πρωτοπόρος και αναμορφωτής του ελληνικού μιούζικαλ, καθιερώνοντας αστέρια όπως η Ζωή Λάσκαρη και η Μάρθα Καραγιάννη.",
    "funFacts": [
      "Ο Δαλιανίδης εισήγαγε το αμερικανικό μοντέλο κινηματογράφησης μιούζικαλ προσαρμοσμένο στην ελληνική πραγματικότητα και μουσική.",
      "Δημιούργησε επίσης μερικές από τις πιο επιτυχημένες σειρές της ελληνικής τηλεόρασης, όπως 'Το Λούνα Παρκ' και 'Τα Λιονταράκια του κυρ-Ηλία'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%94%CE%B1%CE%BB%CE%B9%CE%B1%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek_cinema", "dalianidis", "musicals", "finos_film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_025",
    "text": "Ποιο ήταν το ιστορικό ντεμπούτο σόλο άλμπουμ του Snoop Dogg το 1993, σε παραγωγή του Dr. Dre;",
    "answers": [
      "The Chronic",
      "All Eyez on Me",
      "Doggystyle",
      "Tha Doggfather"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'Doggystyle' έκανε ντεμπούτο κατευθείαν στο νούμερο 1 του Billboard 200 πουλώντας πάνω από 800.000 αντίτυπα την πρώτη εβδομάδα.",
    "funFacts": [
      "Το άλμπουμ περιλάμβανε κλασικά χιπ-χοπ κομμάτια όπως τα 'Gin and Juice' και 'Who Am I? (What's My Name?)'.",
      "Καθιέρωσε τον ήχο West Coast G-funk ως κυρίαρχο μουσικό ρεύμα της δεκαετίας του 1990."
    ],
    "source": "https://en.wikipedia.org/wiki/Doggystyle",
    "locale": "el-GR",
    "tags": ["snoop_dogg", "hip_hop", "dr_dre", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_026",
    "text": "Τι εργαλείο χρησιμοποίησε ο Andy Dufresne για να σκάψει τη σήραγγα διαφυγής του στην ταινία 'Τελευταία Έξοδος: Ρίτα Χέιγουορθ' (1994);",
    "answers": [
      "Ένα μεταλλικό κουτάλι",
      "Ένα μαχαίρι κουζίνας",
      "Μια λίμα νυχιών",
      "Ένα μικρό γεωλογικό σφυρί (Rock hammer)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Andy έκρυψε ένα μικρό σφυρί εξόρυξης ορυκτών μέσα στη Βίβλο του και χρειάστηκε 19 χρόνια για να σκάψει τον τοίχο του κελιού του.",
    "funFacts": [
      "Η ταινία παραμένει σταθερά στο νούμερο 1 των 250 καλύτερων ταινιών όλων των εποχών στο IMDb με πάνω από 2,8 εκατομμύρια ψήφους.",
      "Το σενάριο βασίστηκε στη νουβέλα του Stephen King 'Rita Hayworth and Shawshank Redemption'."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Shawshank_Redemption",
    "locale": "el-GR",
    "tags": ["shawshank_redemption", "cinema", "tim_robbins", "stephen_king"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_027",
    "text": "Ποιος βραβευμένος Βρετανός ηθοποιός δάνεισε την επιβλητική του φωνή στον κακό Σκαρ στην ταινία 'Ο Βασιλιάς των Λιονταριών' (1994);",
    "answers": [
      "Τζέρεμι Άιρονς",
      "Άλαν Ρίκμαν",
      "Πάτρικ Στιούαρτ",
      "Ίαν ΜακΚέλεν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Jeremy Irons έδωσε μια ανυπέρβλητη θεατρική ερμηνεία στον Scar, ερμηνεύοντας επίσης το τραγούδι 'Be Prepared'.",
    "funFacts": [
      "Οι σχεδιαστές της Disney ενσωμάτωσαν εκφράσεις του προσώπου του Jeremy Irons στον σχεδιασμό του λιονταριού Scar.",
      "Κατά την ηχογράφηση του 'Be Prepared', ο Irons έχασε τη φωνή του και το τελευταίο κουπλέ ολοκληρώθηκε από τον ηθοποιό Jim Cummings."
    ],
    "source": "https://en.wikipedia.org/wiki/Scar_(The_Lion_King)",
    "locale": "el-GR",
    "tags": ["the_lion_king", "jeremy_irons", "disney", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_028",
    "text": "Πώς ονομάζεται το λεπτό σπαθί braavosi στυλ που χάρισε ο Jon Snow στην Arya Stark στο 'Game of Thrones';",
    "answers": [
      "Ice",
      "Needle (Βελόνα)",
      "Oathkeeper",
      "Widow's Wail"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Jon Snow έδωσε στην Arya το λεπτό ξίφος λέγοντάς της τον πρώτο της βασικό κανόνα μάχης: 'Stick 'em with the pointy end'.",
    "funFacts": [
      "Η Arya ονόμασε το σπαθί 'Needle' ως ειρωνική αναφορά στις ώρες που περνούσε μισώντας το κέντημα με βελόνες στο Winterfell.",
      "Η ηθοποιός Maisie Williams έμαθε να ξιφομαχεί με το αριστερό χέρι επειδή η Arya στα βιβλία ήταν αριστερόχειρας."
    ],
    "source": "https://en.wikipedia.org/wiki/Arya_Stark",
    "locale": "el-GR",
    "tags": ["game_of_thrones", "arya_stark", "fantasy", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_029",
    "text": "Ποιο ήταν το επάγγελμα της δυναμικής Αγγέλας Ιωακειμίδου (Αγγελική Λάμπρη) στη σειρά 'Στο Παρά 5';",
    "answers": [
      "Δημοσιογράφος",
      "Αστυνομικός",
      "Κασκαντέρ",
      "Δικηγόρος"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Αγγέλα εργαζόταν ως κασκαντέρ σε ταινίες και σειρές δράσης, εκτελώντας επικίνδυνες πτώσεις, συγκρούσεις και άλματα.",
    "funFacts": [
      "Οι ικανότητες της Αγγέλας στις πολεμικές τέχνες και στην οδήγηση έσωσαν την παρέα των πέντε ηρώων σε πολλές κρίσιμες στιγμές.",
      "Το χιούμορ και ο τσαμπουκάς του χαρακτήρα της την έκαναν μία από τις πιο αγαπημένες ηρωίδες της σειράς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["sto_para_pente", "greek_tv", "comedy", "kapoutzidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_030",
    "text": "Ποιο προϊόν παρασκευάζουν και πωλούν ο Tyler Durden και ο αφηγητής στην ταινία 'Fight Club' (1999);",
    "answers": [
      "Χειροποίητα κεριά",
      "Αρώματα",
      "Βιολογικό κρασί",
      "Σαπούνι πολυτελείας"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι πρωταγωνιστές κλέβουν ανθρώπινο λίπος από κλινικές λιποαναρρόφησης για να φτιάξουν ακριβό σαπούνι που πωλούν σε πολυκαταστήματα.",
    "funFacts": [
      "Η διάσημη αφίσα της ταινίας απεικονίζει ένα ροζ σαπούνι με χαραγμένο το λογότυπο Fight Club.",
      "Ο σκηνοθέτης David Fincher αποκάλυψε ότι ένα φλιτζάνι καφέ Starbucks κρύβεται σχεδόν σε κάθε σκηνή της ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Fight_Club",
    "locale": "el-GR",
    "tags": ["fight_club", "david_fincher", "brad_pitt", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_031",
    "text": "Ποιο πρωτοποριακό alternative rock συγκρότημα κυκλοφόρησε το εμβληματικό άλμπουμ 'OK Computer' το 1997;",
    "answers": [
      "Radiohead",
      "Oasis",
      "Blur",
      "The Verve"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι Radiohead δημιούργησαν ένα από τα σημαντικότερα ροκ άλμπουμ της δεκαετίας του 1990 με τραγούδια όπως τα 'Paranoid Android' και 'Karma Police'.",
    "funFacts": [
      "Το άλμπουμ προέβλεψε θέματα όπως η ψηφιακή αποξένωση, η υπερκατανάλωση και η κυριαρχία της τεχνολογίας στον σύγχρονο άνθρωπο.",
      "Εισήχθη στο Εθνικό Μητρώο Ηχογραφήσεων της Βιβλιοθήκης του Κογκρέσου των ΗΠΑ ως έργο πολιτιστικής σημασίας."
    ],
    "source": "https://en.wikipedia.org/wiki/OK_Computer",
    "locale": "el-GR",
    "tags": ["radiohead", "ok_computer", "rock", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_032",
    "text": "Ποιο μυστηριώδες alter ego υιοθετεί η πριγκίπισσα Zelda στο βιντεοπαιχνίδι 'The Legend of Zelda: Ocarina of Time';",
    "answers": [
      "Midna",
      "Sheik (Σέικ)",
      "Impa",
      "Tetra"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Zelda μεταμφιέζεται στον πολεμιστή Sheik της αρχαίας φυλής Sheikah για να κρυφτεί από τον Ganondorf και να καθοδηγήσει τον Link.",
    "funFacts": [
      "Η αποκάλυψη της πραγματικής ταυτότητας του Sheik προς το τέλος του παιχνιδιού θεωρείται μία από τις κορυφαίες ανατροπές στην ιστορία του gaming.",
      "Ο Sheik έγινε εξαιρετικά δημοφιλής χαρακτήρας και εντάχθηκε ως αυτόνομος μαχητής στη σειρά παιχνιδιών Super Smash Bros."
    ],
    "source": "https://en.wikipedia.org/wiki/Princess_Zelda",
    "locale": "el-GR",
    "tags": ["zelda", "sheik", "nintendo", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_033",
    "text": "Ποιο αποκαλύφθηκε ότι είναι το πραγματικό όνομα γέννησης του Wolverine στα κόμικς της Marvel;",
    "answers": [
      "Logan Howlett",
      "Victor Creed",
      "James Howlett",
      "Thomas Logan"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στη σειρά κόμικς 'Origin' (2001) αποκαλύφθηκε ότι ο Wolverine γεννήθηκε ως James Howlett στον Καναδά στα τέλη του 19ου αιώνα.",
    "funFacts": [
      "Για δεκαετίες το παρελθόν και το όνομα του Wolverine παρέμεναν ένα από τα μεγαλύτερα ανεξιχνίαστα μυστήρια των κόμικς.",
      "Το όνομα 'Logan' ήταν το ψευδώνυμο που υιοθέτησε αφού αναγκάστηκε να εγκαταλείψει το πατρικό του κτήμα."
    ],
    "source": "https://en.wikipedia.org/wiki/Wolverine_(character)",
    "locale": "el-GR",
    "tags": ["wolverine", "marvel", "x_men", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_034",
    "text": "Ποιος αγαπημένος κωμικός υποδύθηκε τον βουλευτή Δημοσθένη Καλοχαιρέτα στην ταινία 'Στουρνάρα 288' (1959);",
    "answers": [
      "Διονύσης Παπαγιαννόπουλος",
      "Ορέστης Μακρής",
      "Γιάννης Γκιωνάκης",
      "Νίκος Σταυρίδης"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Νίκος Σταυρίδης έδωσε μια ανεπανάληπτη ερμηνεία ως ο υποψήφιος βουλευτής που μοιράζει υποσχέσεις με το διάσημο επιφώνημα 'Χαιρέτα μου τον πλάτανο!'.",
    "funFacts": [
      "Η ταινία σε σκηνοθεσία Ντίνου Δημόπουλου κατέγραψε τη ζωή των ενοίκων μιας αθηναϊκής πολυκατοικίας στην οδό Στουρνάρα.",
      "Η ατάκα του Καλοχαιρέτα για τα 'έργα που θα γίνουν' αποτελεί κλασική σάτιρα της ελληνικής προεκλογικής δημαγωγίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF%CF%85%CF%81%CE%BD%CE%AC%CF%81%CE%B1_288",
    "locale": "el-GR",
    "tags": ["greek_cinema", "stavridis", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_035",
    "text": "Σε ποιο πεδίο της θεωρητικής φυσικής ειδικεύεται ο Sheldon Cooper στη σειρά 'The Big Bang Theory';",
    "answers": [
      "Θεωρία των Χορδών (String Theory)",
      "Κβαντική Οπτική",
      "Αστροφυσική Σωματιδίων",
      "Πυρηνική Σύντηξη"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Sheldon αφιερώνει το μεγαλύτερο μέρος της έρευνάς του στη Θεωρία των Χορδών προσπαθώντας να ενοποιήσει τη βαρύτητα με την κβαντομηχανική.",
    "funFacts": [
      "Στον τελευταίο κύκλο της σειράς, ο Sheldon και η σύζυγός του Amy κερδίζουν το Βραβείο Νόμπελ Φυσικής για τη θεωρία της υπερασυμμετρίας (Super-Asymmetry).",
      "Ο πραγματικός καθηγητής φυσικής David Saltzberg του UCLA εργαζόταν ως επιστημονικός σύμβουλος της σειράς γράφοντας όλες τις εξισώσεις στους πίνακες."
    ],
    "source": "https://en.wikipedia.org/wiki/Sheldon_Cooper",
    "locale": "el-GR",
    "tags": ["the_big_bang_theory", "sheldon_cooper", "tv", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_036",
    "text": "Ποιο είναι το αγαπημένο κοκτέιλ του χαρακτήρα 'The Dude' (Jeff Bridges) στην καλτ ταινία 'The Big Lebowski' (1998);",
    "answers": [
      "Old Fashioned",
      "White Russian",
      "Manhattan",
      "Whiskey Sour"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο 'The Dude' καταναλώνει συνεχώς White Russian (βότκα, λικέρ καφέ Kahlúa και κρέμα γάλακτος) σε όλη τη διάρκεια της ταινίας.",
    "funFacts": [
      "Στη διάρκεια της ταινίας, ο Dude πίνει συνολικά εννέα κοκτέιλ White Russian.",
      "Η ταινία των αδελφών Coen ενέπνευσε τη δημιουργία μιας πραγματικής φιλοσοφικής θρησκείας/κινήματος με την ονομασία 'Dudeism'."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Big_Lebowski",
    "locale": "el-GR",
    "tags": ["the_big_lebowski", "cinema", "coen_brothers", "cocktails"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_037",
    "text": "Σε ποια πόλη διεξήχθη ο Διαγωνισμός Τραγουδιού της Eurovision το 2005, όπου νίκησε η Ελλάδα με την Έλενα Παπαρίζου;",
    "answers": [
      "Στο Ελσίνκι",
      "Στη Στοκχόλμη",
      "Στο Κίεβο",
      "Στην Κωνσταντινούπολη"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο 50ός Διαγωνισμός Τραγουδιού της Eurovision φιλοξενήθηκε στο Palace of Sports στο Κίεβο της Ουκρανίας μετά τη νίκη της Ruslana το 2004.",
    "funFacts": [
      "Η Ελλάδα συγκέντρωσε 230 βαθμούς λαμβάνοντας το απόλυτο '12άρι' από δέκα διαφορετικές χώρες.",
      "Το τραγούδι 'My Number One' γράφτηκε από τον Χρήστο Δάντη και τη Ναταλία Γερμανού."
    ],
    "source": "https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2005",
    "locale": "el-GR",
    "tags": ["eurovision", "paparizou", "music", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_038",
    "text": "Ποιο ζώο-θεότητα μεγάλωσε την ανθρώπινη πολεμίστρια San στην ταινία 'Πριγκίπισσα Μονονόκε' (Princess Mononoke, 1997);",
    "answers": [
      "Ένα αγριογούρουνο",
      "Ένα ελάφι",
      "Μια αρκούδα",
      "Μια γιγάντια λύκαινα (Moro)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η San μεγάλωσε από τη θεά λύκαινα Moro και θεωρεί τον εαυτό της λύκο, πολεμώντας ενάντια στους ανθρώπους που καταστρέφουν το δάσος.",
    "funFacts": [
      "Η ταινία του Hayao Miyazaki υπήρξε η πρώτη ταινία κινουμένων σχεδίων που κέρδισε το Βραβείο Καλύτερης Ταινίας στα Ιαπωνικά Βραβεία Όσκαρ (Japan Academy Film Prize).",
      "Για τη διανομή στις ΗΠΑ, ο παραγωγός Harvey Weinstein ήθελε να κόψει σκηνές, αλλά ο Miyazaki του έστειλε ένα αυθεντικό σπαθί σαμουράι με το μήνυμα 'No cuts'."
    ],
    "source": "https://en.wikipedia.org/wiki/Princess_Mononoke",
    "locale": "el-GR",
    "tags": ["princess_mononoke", "miyazaki", "anime", "studio_ghibli"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_039",
    "text": "Από ποια πόλη της Αυστραλίας ταξίδεψαν για την Ελλάδα η Στέλλα και η Βίκυ στη σειρά 'Είσαι το Ταίρι μου';",
    "answers": [
      "Από τη Μελβούρνη",
      "Από το Σίδνεϊ",
      "Από το Μπρίσμπεϊν",
      "Από το Περθ"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι δύο Ελληνοαυστραλές γνωρίστηκαν και ξεκίνησαν το ταξίδι τους από τη Μελβούρνη, όπου ζει μεγάλη ελληνική παροικία.",
    "funFacts": [
      "Τα πρώτα επεισόδια της σειράς περιλάμβαναν πραγματικά γυρίσματα σε γνωστές τοποθεσίες της Μελβούρνης.",
      "Η σκηνή στο αεροπλάνο όπου η Βίκυ πείθει τη Στέλλα να ανταλλάξουν ταυτότητες έθεσε την πλοκή για ολόκληρη τη σειρά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%AC%CE%B9%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["eisai_to_tairi_mou", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_040",
    "text": "Πώς ονομάζεται η υπερμεγέθης μαύρη τρύπα γύρω από την οποία περιστρέφονται οι νέοι πλανήτες στην ταινία 'Interstellar' (2014);",
    "answers": [
      "Κυρίαρχος (Overlord)",
      "Γαργάντουας (Gargantua)",
      "Σινγκουλάριτι (Singularity)",
      "Λεβιάθαν (Leviathan)"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η μαύρη τρύπα Gargantua σχεδιάστηκε με βάση πραγματικές επιστημονικές εξισώσεις γενικής σχετικότητας από τον νομπελίστα φυσικό Kip Thorne.",
    "funFacts": [
      "Η υπολογιστική προσομοίωση του Gargantua από την εταιρεία οπτικών εφέ Double Negative οδήγησε σε νέες επιστημονικές δημοσιεύσεις για τη συμπεριφορά του φωτός κοντά σε μαύρες τρύπες.",
      "Στον πλανήτη του Miller που βρίσκεται κοντά στη μαύρη τρύπα, μία ώρα ισοδυναμεί με επτά γήινα χρόνια λόγω της βαρυτικής διαστολής του χρόνου."
    ],
    "source": "https://en.wikipedia.org/wiki/Interstellar_(film)",
    "locale": "el-GR",
    "tags": ["interstellar", "christopher_nolan", "sci_fi", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_041",
    "text": "Ποιο ιστορικό βιντεοπαιχνίδι πλατφόρμας συνόδευσε την κυκλοφορία του Nintendo 64 το 1996, επαναπροσδιορίζοντας τα 3D γραφικά;",
    "answers": [
      "Banjo-Kazooie",
      "Crash Bandicoot",
      "Super Mario 64",
      "Spyro the Dragon"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'Super Mario 64' έθεσε τα θεμέλια για τον έλεγχο κάμερας σε τρισδιάστατο χώρο και τον χειρισμό μέσω αναλογικού μοχλού.",
    "funFacts": [
      "Ο παίκτης συνέλεγε Power Stars μέσα από μαγικούς πίνακες ζωγραφικής στο κάστρο της πριγκίπισσας Peach.",
      "Θεωρείται ευρέως από τους κριτικούς ως ένα από τα πιο επιδραστικά βιντεοπαιχνίδια όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/Super_Mario_64",
    "locale": "el-GR",
    "tags": ["super_mario_64", "nintendo", "gaming", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_042",
    "text": "Πώς ονομάζεται ο πανίσχυρος μιντιακός κολοσσός της οικογένειας Roy στη βραβευμένη δραματική σειρά 'Succession';",
    "answers": [
      "Pierce Media",
      "Ewing Oil",
      "Initech Global",
      "Waystar RoyCo"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Waystar RoyCo είναι ο πολυεθνικός όμιλος μέσων ενημέρωσης, ψυχαγωγίας και κρουαζιέρας που ίδρυσε ο πατριάρχης Logan Roy (Brian Cox).",
    "funFacts": [
      "Η σειρά κέρδισε συνολικά 19 βραβεία Primetime Emmy, σαρώνοντας τις κατηγορίες καλύτερης δραματικής σειράς και ερμηνειών.",
      "Η οικογένεια Roy θεωρείται ότι είναι εμπνευσμένη εν μέρει από την πραγματική οικογένεια του μεγιστάνα των μέσων ενημέρωσης Rupert Murdoch."
    ],
    "source": "https://en.wikipedia.org/wiki/Succession_(TV_series)",
    "locale": "el-GR",
    "tags": ["succession", "hbo", "tv", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_043",
    "text": "Ποιο ήταν το πρώτο μεγάλο breakthrough single της Katy Perry το 2008 που την εκτόξευσε στην κορυφή του Billboard Hot 100;",
    "answers": [
      "I Kissed a Girl",
      "Hot n Cold",
      "Teenage Dream",
      "California Gurls"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το 'I Kissed a Girl' από το άλμπουμ 'One of the Boys' έφτασε στο νούμερο 1 σε σχεδόν είκοσι χώρες και καθιέρωσε την Katy Perry.",
    "funFacts": [
      "Η Katy Perry ξεκίνησε την καριέρα της τραγουδώντας χριστιανική γκόσπελ μουσική με το πραγματικό της όνομα, Katy Hudson.",
      "Το τραγούδι προκάλεσε έντονες αντιδράσεις από συντηρητικές οργανώσεις αλλά έγινε τεράστια εμπορική επιτυχία."
    ],
    "source": "https://en.wikipedia.org/wiki/I_Kissed_a_Girl",
    "locale": "el-GR",
    "tags": ["katy_perry", "music", "pop", "billboard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_044",
    "text": "Ποιος σκηνοθέτης υπέγραψε το ιστορικό κοινωνικό δράμα 'Τα κόκκινα φανάρια' (1963), που έφτασε μέχρι την τελική πεντάδα των Όσκαρ;",
    "answers": [
      "Μιχάλης Κακογιάννης",
      "Βασίλης Γεωργιάδης",
      "Γιάννης Δαλιανίδης",
      "Αλέκος Σακελλάριος"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Βασίλης Γεωργιάδης σκηνοθέτησε 'Τα κόκκινα φανάρια', που προτάθηκαν για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας στην 36η απονομή (1964).",
    "funFacts": [
      "Η ταινία περιέγραψε τις ζωές των γυναικών στην Τρούμπα του Πειραιά λίγο πριν το οριστικό κλείσιμο των οίκων ανοχής.",
      "Ο Βασίλης Γεωργιάδης προτάθηκε ξανά για Όσκαρ δύο χρόνια αργότερα με την ταινία 'Το χώμα βάφτηκε κόκκινο' (1965)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%B1_%CF%86%CE%B1%CE%BD%CE%AC%CF%81%CE%B9%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "georgiadis", "oscars", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_045",
    "text": "Ποιο ήταν το δημόσιο αξίωμα του Harvey Dent στην Gotham City πριν παραμορφωθεί και μετατραπεί στον κακό Two-Face;",
    "answers": [
      "Αρχηγός της Αστυνομίας",
      "Δήμαρχος",
      "Επαρχιακός Εισαγγελέας (District Attorney)",
      "Επικεφαλής Δικαστής"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Harvey Dent ήταν ο αδιάφθορος εισαγγελέας της πόλης, γνωστός ως ο 'Λευκός Ιππότης' του Gotham, πριν καεί η μισή πλευρά του προσώπου του από οξύ.",
    "funFacts": [
      "Ο Two-Face παίρνει όλες τις κρίσιμες αποφάσεις για τη ζωή των θυμάτων του ρίχνοντας ένα δίπτυχο νόμισμα με τη μία πλευρά χαραγμένη.",
      "Στην ταινία 'Ο Σκοτεινός Ιππότης' (2008) τον Harvey Dent υποδύθηκε ο Aaron Eckhart."
    ],
    "source": "https://en.wikipedia.org/wiki/Two-Face",
    "locale": "el-GR",
    "tags": ["batman", "two_face", "dc_comics", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_046",
    "text": "Ποια πρόταση πληκτρολογεί εμμονικά ο Jack Torrance σε εκατοντάδες σελίδες στην ταινία 'Η Λάμψη' (The Shining);",
    "answers": [
      "Redrum Redrum Redrum",
      "Here is Jack coming for you",
      "Murder at the Overlook Hotel",
      "All work and no play makes Jack a dull boy"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η σύζυγός του Wendy ανακαλύπτει έντρομη ότι το υποτιθέμενο μυθιστόρημα του Jack αποτελείται μόνο από την επανάληψη αυτής της μίας πρότασης.",
    "funFacts": [
      "Για τις εκδόσεις της ταινίας σε άλλες χώρες, ο Stanley Kubrick γύρισε εναλλακτικά πλάνα δακτυλογραφημένων σελίδων στις αντίστοιχες γλώσσες (π.χ. στα ιταλικά, γερμανικά, ισπανικά).",
      "Η γραμματέας του Kubrick πέρασε μήνες δακτυλογραφώντας πράγματι εκατοντάδες σελίδες με τη συγκεκριμένη φράση."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Shining_(film)",
    "locale": "el-GR",
    "tags": ["the_shining", "kubrick", "cinema", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_047",
    "text": "Πώς ονομάζεται ο αυστηρός και επίφοβος κριτικός γαστρονομίας στην ταινία 'Ρατατούης' (Ratatouille, 2007);",
    "answers": [
      "Άντον Ίγκο (Anton Ego)",
      "Ωγκύστ Γκουστό",
      "Σκίνερ",
      "Αλφρέντο Λινγκουίνι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Anton Ego είναι ο σκληρός κριτικός εστιατορίων που μαλακώνει συναισθηματικά όταν δοκιμάζει το ρατατούι του Ρεμί, θυμούμενος τη μητέρα του.",
    "funFacts": [
      "Τη φωνή του Anton Ego στην αμερικανική εκδοχή έκανε ο σπουδαίος ηθοποιός Peter O'Toole.",
      "Το γραφείο του Anton Ego σχεδιάστηκε επίτηδες με σχήμα που θυμίζει φέρετρο για να τονίσει τη θανατηφόρα κριτική του ματιά."
    ],
    "source": "https://en.wikipedia.org/wiki/Ratatouille_(film)",
    "locale": "el-GR",
    "tags": ["ratatouille", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_048",
    "text": "Σε ποιον συνάδελφό του στην εταιρεία Dunder Mifflin έστηνε συνεχώς περίτεχνες φάρσες ο Jim Halpert στη σειρά 'The Office';",
    "answers": [
      "Στον Ryan Howard",
      "Στον Dwight Schrute",
      "Στον Andy Bernard",
      "Στον Kevin Malone"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι φάρσες του Jim (John Krasinski) στον Dwight (Rainn Wilson) – όπως το να βάλει το συρραπτικό του μέσα σε ζελέ – έγιναν σήμα κατατεθέν της σειράς.",
    "funFacts": [
      "Η φάρσα με το συρραπτικό μέσα σε ζελέ ήταν άμεσος φόρος τιμής στο πρώτο επεισόδιο του αρχικού βρετανικού The Office.",
      "Παρά τις αδιάκοπες κόντρες των χαρακτήρων τους, οι ηθοποιοί John Krasinski και Rainn Wilson είναι στενοί φίλοι στην πραγματικότητα."
    ],
    "source": "https://en.wikipedia.org/wiki/Dwight_Schrute",
    "locale": "el-GR",
    "tags": ["the_office", "jim_halpert", "dwight_schrute", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_049",
    "text": "Ποιος θρυλικός κιθαρίστας έπαιξε το ιστορικό κιθαριστικό σόλο στο τραγούδι 'Beat It' του Michael Jackson το 1982;",
    "answers": [
      "Slash",
      "Eric Clapton",
      "Eddie Van Halen",
      "Brian May"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Eddie Van Halen ηχογράφησε το εκρηκτικό σόλο δωρεάν ως χάρη στον παραγωγό Quincy Jones μέσα σε μόλις μισή ώρα.",
    "funFacts": [
      "Κατά τη διάρκεια της ηχογράφησης του σόλο, η ένταση του ενισχυτή ήταν τόσο υψηλή που ένα από τα ηχεία στο στούντιο πήρε κυριολεκτικά φωτιά.",
      "Ο Van Halen δεν ζήτησε καμία αμοιβή ούτε πνευματικά δικαιώματα για τη συμμετοχή του στο τραγούδι."
    ],
    "source": "https://en.wikipedia.org/wiki/Beat_It",
    "locale": "el-GR",
    "tags": ["michael_jackson", "van_halen", "beat_it", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_050",
    "text": "Ποια αρχαία τραγωδία επιχειρούσε να ανεβάσει ο θεατρικός σκηνοθέτης Κωνσταντίνος Μαρκοράς με τη Μαρίνα Κουντουράτου στη σειρά 'Δύο Ξένοι';",
    "answers": [
      "Μήδεια",
      "Ηλέκτρα",
      "Οιδίπους Τύραννος",
      "Αντιγόνη"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Μαρκοράς προσπαθούσε απεγνωσμένα να διδάξει στην ξανθιά τηλεπαρουσιάστρια τον ρόλο της Αντιγόνης του Σοφοκλή, οδηγώντας σε απολαυστικές κωμικές συγκρούσεις.",
    "funFacts": [
      "Η σκηνή της πρόβας με την ατάκα 'Έρως ανίκατε μάχαν' είναι μία από τις πιο αναγνωρίσιμες της σειράς.",
      "Η σειρά των Ρήγα - Αποστόλου προβλήθηκε στο Mega τις σεζόν 1997-1999 και αποτελεί ορόσημο της ελληνικής τηλεόρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CF%85%CE%BF_%CE%9E%CE%AD%CE%BD%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["dyo_xenoi", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_051",
    "text": "Ποιο ιστορικό debate πυροδότησε η σκηνή στην καντίνα του Mos Eisley ανάμεσα στον Han Solo και τον Greedo στο 'Star Wars' (1977);",
    "answers": [
      "Ποιος πυροβόλησε πρώτος (Who shot first?)",
      "Πόσα χρήματα χρωστούσε ο Solo",
      "Αν το blaster ήταν νόμιμο",
      "Αν ο Greedo ήταν πράκτορας"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Στην αρχική ταινία του 1977 ο Han Solo πυροβολεί πρώτος εν ψυχρώ κάτω από το τραπέζι, αλλά στις επανεκδόσεις ο George Lucas άλλαξε τη σκηνή ώστε να πυροβολεί πρώτος ο Greedo.",
    "funFacts": [
      "Το σλόγκαν 'Han Shot First' εμφανίστηκε σε μπλουζάκια και έγινε ένα από τα πιο διάσημα συνθήματα διαμαρτυρίας των φαν της σειράς.",
      "Ο ηθοποιός Harrison Ford, ερωτηθείς σε συνέντευξη για το ποιος πυροβόλησε πρώτος, απάντησε αφοπλιστικά: 'Δεν με νοιάζει'."
    ],
    "source": "https://en.wikipedia.org/wiki/Han_shot_first",
    "locale": "el-GR",
    "tags": ["star_wars", "han_solo", "cinema", "trivia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_052",
    "text": "Ποιο πάνθεο θεοτήτων κατασφάζει ο Kratos στην αρχική τριλογία της σειράς βιντεοπαιχνιδιών 'God of War';",
    "answers": [
      "Το Νορβηγικό",
      "Το Ελληνικό (Δωδεκάθεο)",
      "Το Αιγυπτιακό",
      "Το Κελτικό"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Σπαρτιάτης Kratos αναζητά εκδίκηση από τον θεό Άρη και στη συνέχεια εξολοθρεύει ολόκληρο το πάνθεο του Ολύμπου, συμπεριλαμβανομένου του πατέρα του, Δία.",
    "funFacts": [
      "Μετά την καταστροφή του ελληνικού κόσμου στο God of War III (2010), η σειρά μετακόμισε στη σκανδιναβική μυθολογία με το God of War του 2018.",
      "Τον Kratos στα πρώτα παιχνίδια δάνεισε τη φωνή του ο Terrence C. Carson, ενώ στη σκανδιναβική εποχή ο Christopher Judge."
    ],
    "source": "https://en.wikipedia.org/wiki/God_of_War_(franchise)",
    "locale": "el-GR",
    "tags": ["god_of_war", "kratos", "gaming", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_053",
    "text": "Πώς ονομάζεται το μυστικό κυβερνητικό εργαστήριο όπου μεγάλωσε και εκπαιδεύτηκε η Eleven στη σειρά 'Stranger Things';",
    "answers": [
      "Los Alamos Laboratory",
      "Oak Ridge Facility",
      "Hawkins National Laboratory",
      "Pine Gap Research"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Το Εθνικό Εργαστήριο του Hawkins ανήκει στο Υπουργείο Ενέργειας των ΗΠΑ και πραγματοποιούσε μυστικά πειράματα τηλεπάθειας υπό τον Dr. Martin Brenner.",
    "funFacts": [
      "Το εργαστήριο της σειράς είναι εμπνευσμένο από το πραγματικό διαβόητο μυστικό πρόγραμμα της CIA με την ονομασία Project MKUltra.",
      "Το εξωτερικό κτίριο του εργαστηρίου στα γυρίσματα ήταν ένα παλιό ψυχιατρικό άσυλο στην πανεπιστημιούπολη Briarcliff του Πανεπιστημίου Emory στην Ατλάντα."
    ],
    "source": "https://en.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger_things", "eleven", "netflix", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_054",
    "text": "Ποια σπουδαία κυρία του ελληνικού θεάτρου υποδύθηκε την Άννα που προσποιείται την τρελή στην κωμωδία 'Η γυναίκα μου τρελάθηκε' (1966);",
    "answers": [
      "Ρένα Βλαχοπούλου",
      "Γεωργία Βασιλειάδου",
      "Τζένη Καρέζη",
      "Μαίρη Αρώνη"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Μαίρη Αρώνη υποδύθηκε απολαυστικά την Άννα, η οποία κάνει την τρελή για να παρακολουθήσει τις απιστίες του συζύγου της (Λάμπρος Κωνσταντάρας).",
    "funFacts": [
      "Η σκηνή όπου η Αρώνη τραγουδάει και χορεύει φορώντας εκκεντρικά ρούχα για να πείσει τους πάντες ότι τρελάθηκε θεωρείται υπόδειγμα κωμικής ερμηνείας.",
      "Η ταινία γυρίστηκε από τη Φίνος Φιλμ σε σκηνοθεσία Δημήτρη Νικολαΐδη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B3%CF%85%CE%BD%CE%B1%CE%AF%CE%BA%CE%B1_%CE%BC%CE%BF%CF%85_%CF%84%CF%81%CE%B5%CE%BB%CE%AC%CE%B8%CE%B7%CE%BA%CE%B5",
    "locale": "el-GR",
    "tags": ["greek_cinema", "aroni", "konstantaras", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_055",
    "text": "Ποιο βρετανικό synthpop συγκρότημα κυκλοφόρησε το 1983 το κομμάτι 'Blue Monday', το πιο επιτυχημένο 12ιντσο single όλων των εποχών;",
    "answers": [
      "New Order",
      "Depeche Mode",
      "Pet Shop Boys",
      "The Human League"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Οι New Order (που σχηματίστηκαν από τα εναπομείναντα μέλη των Joy Division μετά τον θάνατο του Ian Curtis) δημιούργησαν τον απόλυτο ύμνο της ηλεκτρονικής χορευτικής μουσικής.",
    "funFacts": [
      "Το εξώφυλλο του 12ιντσου δίσκου σχεδιάστηκε από τον Peter Saville σαν πραγματική δισκέτα υπολογιστή (floppy disk) 5¼ ιντσών.",
      "Επειδή το περίτεχνο εξώφυλλο είχε τόσο υψηλό κόστος παραγωγής, η εταιρεία Factory Records έχανε χρήματα για κάθε αντίτυπο που πουλούσε!"
    ],
    "source": "https://en.wikipedia.org/wiki/Blue_Monday_(New_Order_song)",
    "locale": "el-GR",
    "tags": ["new_order", "synthpop", "music", "80s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_056",
    "text": "Ποια λεπτομέρεια προδίδει τον Βρετανό κατάσκοπο Archie Hicox στην ταβέρνα στην ταινία του Quentin Tarantino 'Άδωξοι Μπάσταρδη' (2009);",
    "answers": [
      "Η αγγλική προφορά του",
      "Ο τρόπος που παραγγέλνει τρία ποτήρια με τα δάχτυλα",
      "Το ξένο νόμισμα που πληρώνει",
      "Το στυλό με τα βρετανικά διακριτικά"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Hicox ζητάει τρία ποτήρια σηκώνοντας τον δείκτη, τον μέσο και τον παράμεσο (βρετανική συνήθεια), αντί για τον αντίχειρα, τον δείκτη και τον μέσο όπως κάνουν οι Γερμανοί.",
    "funFacts": [
      "Τον ύποπτο αξιωματικό των SS Dieter Hellstrom στην περίφημη σκηνή υποδύθηκε ο August Diehl.",
      "Ο Christoph Waltz κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου για την ερμηνεία του ως ο πολυμαθής και αδίστακτος συνταγματάρχης Hans Landa."
    ],
    "source": "https://en.wikipedia.org/wiki/Inglourious_Basterds",
    "locale": "el-GR",
    "tags": ["inglourious_basterds", "tarantino", "cinema", "details"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_057",
    "text": "Ποια ηρωίδα θυσιάζεται από τον πατέρα της Thanos στον πλανήτη Vormir στο 'Avengers: Infinity War' (2018);",
    "answers": [
      "Nebula",
      "Mantise",
      "Gamora",
      "Black Widow"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Thanos πετάει τη θετή του κόρη Gamora (Zoe Saldaña) στον γκρεμό του Vormir, καθώς η Πέτρα της Ψυχής απαιτούσε τη θυσία αυτού που αγαπούσε περισσότερο.",
    "funFacts": [
      "Η ηθοποιός Zoe Saldaña πέρασε πάνω από τρεις ώρες καθημερινά στο μακιγιάζ για να αποκτήσει το χαρακτηριστικό πράσινο δέρμα της Gamora.",
      "Η σκηνή του θανάτου της ήταν μία από τις πιο καλά φυλαγμένες εκπλήξεις του κινηματογραφικού σύμπαντος της Marvel."
    ],
    "source": "https://en.wikipedia.org/wiki/Gamora_(Marvel_Cinematic_Universe)",
    "locale": "el-GR",
    "tags": ["avengers", "gamora", "marvel", "infinity_war"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_058",
    "text": "Πώς ονομάζεται ο σαρκαστικός και οξύθυμος παπαγάλος-συνεργάτης του κακού Jafar στην κλασική ταινία 'Aladdin' (1992);",
    "answers": [
      "Ζάζου",
      "Ντιάμπλο",
      "Αμπού",
      "Ιάγκο (Iago)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Ο Iago είναι ο κόκκινος παπαγάλος του Jafar που σχεδιάζει συνεχώς μηχανορραφίες για την ανατροπή του Σουλτάνου του Agrabah.",
    "funFacts": [
      "Τη φωνή του Iago στην αυθεντική αγγλική έκδοση έδωσε ο κωμικός Gilbert Gottfried με τη χαρακτηριστική τσιριχτή φωνή του.",
      "Το όνομα Iago είναι αναφορά στον διάσημο δόλιο προδότη από το σαιξπηρικό έργο 'Οθέλλος'."
    ],
    "source": "https://en.wikipedia.org/wiki/Jafar_(Disney)#Iago",
    "locale": "el-GR",
    "tags": ["aladdin", "disney", "animation", "iago"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_059",
    "text": "Ποιο μάθημα δίδασκε στο σχολείο η αυστηρή καθηγήτρια Σούλα Σακελλαρίου (Κάτια Δανδουλάκη) στη σειρά 'Σαββατογεννημένες';",
    "answers": [
      "Αρχαία Ελληνικά / Φιλολογία",
      "Μαθηματικά",
      "Βιολογία",
      "Ιστορία Τέχνης"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Σούλα Σακελλαρίου ήταν αυστηρή φιλόλογος σε λύκειο, διαρκώς εκνευρισμένη με τους ανορθόγραφους και απείθαρχους μαθητές της.",
    "funFacts": [
      "Η σκηνή όπου διορθώνει με κόκκινο στιλό και παθαίνει νευρική κρίση με τα μαργαριτάρια των μαθητών ήταν από τις πιο αστείες της σειράς.",
      "Τον τεμπέλη μαθητή 'Χοσέ' υποδύθηκε ο ίδιος ο σεναριογράφος της σειράς, Γιώργος Καπουτζίδης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%B2%CE%B2%CE%B1%CF%84%CE%BF%CE%B3%CE%B5%CE%BD%CE%BD%CE%B7%CE%BC%CE%AD%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["savvatogennimenes", "greek_tv", "comedy", "dandoulaki"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_med_060",
    "text": "Πώς ονομάζεται η γιγάντια θηλυκή δράκαινα που ιππεύει ο πρίγκιπας Aemond Targaryen στη σειρά 'House of the Dragon';",
    "answers": [
      "Syrax",
      "Vhagar (Βάγκαρ)",
      "Caraxes",
      "Meleys"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 3,
    "explanation": "Η Vhagar ήταν ο παλαιότερος και μεγαλύτερος εν ζωή δράκος στο Westeros, έχοντας πολεμήσει αρχικά στην κατάκτηση του Aegon I Targaryen.",
    "funFacts": [
      "Στη σειρά, το μέγεθος της Vhagar είναι τόσο κολοσσιαίο που το άνοιγμα των φτερών της ξεπερνά τα 150 μέτρα, καλύπτοντας ολόκληρες πόλεις με τη σκιά της.",
      "Πριν τη διεκδικήσει ο Aemond, αναβάτες της Vhagar υπήρξαν η βασίλισσα Visenya, ο πρίγκιπας Baelon και η λαίδη Laena Velaryon."
    ],
    "source": "https://en.wikipedia.org/wiki/House_of_the_Dragon",
    "locale": "el-GR",
    "tags": ["house_of_the_dragon", "game_of_thrones", "dragons", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'medium', 3, questions)

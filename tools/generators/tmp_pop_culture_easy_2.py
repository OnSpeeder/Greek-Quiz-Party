# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_easy_061",
    "text": "Ποιο είναι το όνομα του μικρού μοναχικού ρομπότ συμπίεσης σκουπιδιών στην ομώνυμη ταινία της Pixar (2008);",
    "answers": [
      "WALL-E",
      "R2-D2",
      "Baymax",
      "Bender"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο WALL-E (Waste Allocation Load Lifter: Earth-Class) είναι το μοναχικό ρομπότ που καθαρίζει την εγκαταλελειμμένη Γη.",
    "funFacts": [
      "Σχεδόν όλη η πρώτη μισή ώρα της ταινίας δεν περιέχει καθόλου διαλόγους, παρά μόνο φυσικούς ήχους και εκφράσεις του ρομπότ.",
      "Η ταινία κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2009."
    ],
    "source": "https://en.wikipedia.org/wiki/WALL-E",
    "locale": "el-GR",
    "tags": ["wall_e", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_062",
    "text": "Ποια είναι η αγαπημένη ατάκα του ιδιόρρυθμου φυσικού Sheldon Cooper στη σειρά 'The Big Bang Theory' όταν κάνει φάρσα;",
    "answers": [
      "Eureka!",
      "Bazinga!",
      "D'oh!",
      "Bingo!"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Sheldon Cooper (Jim Parsons) χρησιμοποιεί τη λέξη 'Bazinga!' κάθε φορά που κάνει ένα αστείο ή μια πετυχημένη φάρσα.",
    "funFacts": [
      "Η λέξη 'Bazinga' ενέπνευσε τους επιστήμονες να ονομάσουν ένα νεοανακαλυφθέν είδος μέλισσας Euglossa bazinga.",
      "Ο Jim Parsons κέρδισε τέσσερα βραβεία Primetime Emmy Α' Ανδρικού Ρόλου για την ερμηνεία του ως Sheldon."
    ],
    "source": "https://en.wikipedia.org/wiki/Sheldon_Cooper",
    "locale": "el-GR",
    "tags": ["the_big_bang_theory", "tv", "sitcom", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_063",
    "text": "Ποια Βρετανίδα τραγουδίστρια σημείωσε παγκόσμια επιτυχία με τα άλμπουμ '19', '21' και '25';",
    "answers": [
      "Dua Lipa",
      "Amy Winehouse",
      "Adele",
      "Ellie Goulding"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Adele έδωσε στα πρώτα της άλμπουμ ως τίτλους τις ηλικίες στις οποίες έγραψε τα αντίστοιχα τραγούδια.",
    "funFacts": [
      "Το τραγούδι της 'Skyfall' για την ομώνυμη ταινία James Bond κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 2013.",
      "Το άλμπουμ '21' παρέμεινε στην κορυφή του βρετανικού chart για 23 εβδομάδες, σημειώνοντας ρεκόρ για σόλο καλλιτέχνη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%AD%CE%BB",
    "locale": "el-GR",
    "tags": ["adele", "music", "pop", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_064",
    "text": "Στην κλασική ελληνική κωμωδία 'Η θεία από το Σικάγο' (1957), τι αντικείμενα πετούσε η Γεωργία Βασιλειάδου από το μπαλκόνι για να βρει γαμπρούς για τις ανιψιές της;",
    "answers": [
      "Κουβάδες νερό",
      "Μαντήλια",
      "Πιάτα",
      "Πήλινα κανάτια (κιούπια)"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η θεία Καλλιόπη (Γεωργία Βασιλειάδου) πετούσε επίτηδες πήλινα κανάτια στον δρόμο για να προκαλέσει γνωριμίες με περαστικούς νέους.",
    "funFacts": [
      "Η ταινία σε σκηνοθεσία Αλέκου Σακελλάριου ήταν η μεγαλύτερη εισπρακτική επιτυχία της σεζόν 1957-1958 στην Ελλάδα.",
      "Τον αυστηρό πατέρα και απόστρατο στρατιωτικό Χαρίλαο υποδύθηκε ο σπουδαίος Ορέστης Μακρής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B8%CE%B5%CE%AF%CE%B1_%CE%B1%CF%80%CF%8C_%CF%84%CE%BF_%CE%A3%CE%B9%CE%BA%CE%AC%CE%B3%CE%BF",
    "locale": "el-GR",
    "tags": ["greek_cinema", "comedy", "vasileiadou", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_065",
    "text": "Ποιο ραδιενεργό ορυκτό από τον πλανήτη καταγωγής του αποτελεί τη μεγαλύτερη αδυναμία του Superman;",
    "answers": [
      "Κρυπτονίτης",
      "Αδαμάντιο",
      "Βιβράνιο",
      "Μιθρίλ"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο πράσινος κρυπτονίτης (Kryptonite) αποδυναμώνει πλήρως τον Superman και μπορεί να αποβεί θανατηφόρος για εκείνον.",
    "funFacts": [
      "Ο κρυπτονίτης δεν επινοήθηκε στα πρώτα κόμικς, αλλά εισήχθη αρχικά στη ραδιοφωνική σειρά του Superman το 1943.",
      "Εκτός από τον πράσινο κρυπτονίτη, στα κόμικς υπάρχουν και άλλες παραλλαγές (κόκκινος, χρυσός, μαύρος) με διαφορετικές επιδράσεις."
    ],
    "source": "https://en.wikipedia.org/wiki/Kryptonite",
    "locale": "el-GR",
    "tags": ["superman", "dc_comics", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_066",
    "text": "Πώς ονομάζεται ο θηλυκός βελοσιράπτορας με τη μπλε ρίγα που εκπαίδευσε ο Owen Grady στην ταινία 'Jurassic World';",
    "answers": [
      "Delta",
      "Blue",
      "Charlie",
      "Echo"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Blue είναι η αρχηγός της ομάδας ράπτορα (raptor squad) και διακρίνεται για τη νοημοσύνη και τη συναισθηματική της σύνδεση με τον Owen Grady.",
    "funFacts": [
      "Το DNA της Blue περιείχε γονίδια από τη σαύρα monitor με μαύρο λαιμό, που της χάρισε το ιδιαίτερο σχέδιο μπλε χρωματισμού.",
      "Η ταινία Jurassic World (2015) ξεπέρασε το 1,6 δισεκατομμύριο δολάρια σε εισπράξεις παγκοσμίως."
    ],
    "source": "https://en.wikipedia.org/wiki/Jurassic_World",
    "locale": "el-GR",
    "tags": ["jurassic_world", "cinema", "dinosaurs", "blue"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_067",
    "text": "Σε ποιο στοιχειακό τύπο ανήκει το διάσημο Pokémon Pikachu;",
    "answers": [
      "Φωτιά",
      "Νερό",
      "Ηλεκτρισμός",
      "Χορτάρι"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Pikachu είναι Pokémon τύπου Ηλεκτρισμού (Electric type) και χρησιμοποιεί επιθέσεις όπως το Thunderbolt.",
    "funFacts": [
      "Το όνομα Pikachu είναι σύνθεση των ιαπωνικών λέξεων 'pika' (ηχομιμητική λέξη για τη λάμψη σπίθας) και 'chu' (ο ήχος που κάνει το ποντίκι).",
      "Η εξέλιξη του Pikachu είναι ο Raichu, στην οποία μεταμορφώνεται με τη βοήθεια μιας Thunder Stone."
    ],
    "source": "https://en.wikipedia.org/wiki/Pikachu",
    "locale": "el-GR",
    "tags": ["pokemon", "pikachu", "nintendo", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_068",
    "text": "Ποιος θρυλικός κωμικός ηθοποιός δάνεισε την αξέχαστη φωνή του στο Τζίνι (Genie) στην ταινία κινουμένων σχεδίων 'Aladdin' (1992);",
    "answers": [
      "Τζιμ Κάρεϊ",
      "Έντι Μέρφι",
      "Μπίλι Κρίσταλ",
      "Ρόμπιν Ουίλιαμς"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Robin Williams έδωσε μια ανεπανάληπτη ερμηνεία αυτοσχεδιάζοντας μεγάλο μέρος των διαλόγων και των μιμήσεων του Τζίνι.",
    "funFacts": [
      "Ο σκηνοθέτης και οι σχεδιαστές εμπνεύστηκαν τον χαρακτήρα ειδικά για τον Robin Williams, δημιουργώντας δοκιμαστικά σκίτσα πάνω σε ηχογραφήσεις stand-up του.",
      "Το τραγούδι 'Friend Like Me' που ερμήνευσε ο Williams προτάθηκε για Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού."
    ],
    "source": "https://en.wikipedia.org/wiki/Genie_(Disney)",
    "locale": "el-GR",
    "tags": ["aladdin", "disney", "animation", "robin_williams"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_069",
    "text": "Ποιες δύο οικογένειες συγκεντρώνονται κάθε Κυριακή για μεσημεριανό φαγητό στην κωμική σειρά του Alpha 'Το Σόι σου';",
    "answers": [
      "Οι οικογένειες Τριανταφύλλου και Χαμπέα",
      "Οι οικογένειες Παπαδοπούλου και Γεωργίου",
      "Οι οικογένειες Κωνσταντίνου και Ελένης",
      "Οι οικογένειες Μαυρογιαλούρου και Φωτόπουλου"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η σειρά παρακολουθεί τις ξεκαρδιστικές οικογενειακές συγκρούσεις των γονέων της Αντωνίας και του Σάββα, δηλαδή των οικογενειών Χαμπέα και Τριανταφύλλου.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 5 συνεχόμενες σεζόν στον Alpha γνωρίζοντας τεράστια επιτυχία και υψηλή τηλεθέαση.",
      "Τους πατριάρχες των δύο οικογενειών ενσάρκωσαν απολαυστικά ο Γιώργος Γιαννόπουλος (Βαγγέλης Χαμπέας) και ο Παύλος Ορκόπουλος (Μενέλαος Τριαντάφυλλος)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["to_soi_sou", "greek_tv", "comedy", "alpha"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_070",
    "text": "Μέσω ποιου παιχνιδιού κέρδισε ο Μπίλμπο Μπάγκινς το Ένα Δαχτυλίδι από το Γκόλουμ στο βιβλίο 'Το Χόμπιτ';",
    "answers": [
      "Μονομαχία με σπαθιά",
      "Παιχνίδι με αινίγματα",
      "Σκάκι",
      "Αγώνα δρόμου"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μπίλμπο και το Γκόλουμ έπαιξαν ένα παιχνίδι αινιγμάτων στα σκοτεινά σπήλαια των Ομιχλωδών Βουνών.",
    "funFacts": [
      "Το τελικό 'αίνιγμα' του Μπίλμπο που νίκησε το Γκόλουμ ήταν απλώς η ερώτηση: 'Τι έχω στην τσέπη μου;'.",
      "Το βιβλίο 'Το Χόμπιτ' του Τζ. Ρ. Ρ. Τόλκιν εκδόθηκε για πρώτη φορά το 1937 και αρχικά γράφτηκε ως παιδικό παραμύθι."
    ],
    "source": "https://en.wikipedia.org/wiki/Riddles_in_the_Dark",
    "locale": "el-GR",
    "tags": ["the_hobbit", "tolkien", "books", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_071",
    "text": "Με ποιον στίχο ξεκινά το ιστορικό ροκ τραγούδι 'Bohemian Rhapsody' των Queen;",
    "answers": [
      "Mama, just killed a man",
      "Scaramouche, Scaramouche",
      "Is this the real life? Is this just fantasy?",
      "Too late, my time has come"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι ξεκινά με την ακαπέλα αρμονία: 'Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality.'",
    "funFacts": [
      "Η δισκογραφική εταιρεία αρχικά αρνήθηκε να κυκλοφορήσει το τραγούδι ως single επειδή θεωρούσε τα 6 λεπτά διάρκειάς του απαγορευτικά για το ραδιόφωνο.",
      "Το βίντεο κλιπ του τραγουδιού θεωρείται από πολλούς ιστορικούς το πρώτο σύγχρονο προωθητικό μουσικό βίντεο."
    ],
    "source": "https://en.wikipedia.org/wiki/Bohemian_Rhapsody",
    "locale": "el-GR",
    "tags": ["queen", "bohemian_rhapsody", "music", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_072",
    "text": "Τι χρώμα στολές φορούν οι μυστηριώδεις ένοπλοι φρουροί με τις μάσκες γεωμετρικών σχημάτων στη σειρά 'Squid Game';",
    "answers": [
      "Κίτρινες",
      "Μπλε",
      "Μαύρες",
      "Ροζ / Φούξια"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι διαγωνιζόμενοι φορούν πράσινες αθλητικές φόρμες με αριθμούς, ενώ οι φρουροί φορούν ροζ-φούξια ολόσωμες στολές με μάσκες.",
    "funFacts": [
      "Τα γεωμετρικά σχήματα στις μάσκες δηλώνουν ιεραρχία: ο κύκλος για τους εργάτες, το τρίγωνο για τους στρατιώτες και το τετράγωνο για τους διευθυντές.",
      "Η σειρά 'Squid Game' έγινε η πιο επιτυχημένη σειρά στην ιστορία του Netflix ξεπερνώντας το 1,6 δισεκατομμύριο ώρες παρακολούθησης στον πρώτο μήνα."
    ],
    "source": "https://en.wikipedia.org/wiki/Squid_Game",
    "locale": "el-GR",
    "tags": ["squid_game", "netflix", "tv", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_073",
    "text": "Με τι παρομοιάζει τη ζωή η μητέρα του Forrest Gump στη διάσημη ατάκα της ομώνυμης ταινίας;",
    "answers": [
      "Με ένα κουτί σοκολατάκια",
      "Με ένα ποτάμι που κυλάει",
      "Με ένα βιβλίο χωρίς τέλος",
      "Με μια παρτίδα σκάκι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η διάσημη ατάκα είναι: 'Life is like a box of chocolates. You never know what you're gonna get.'",
    "funFacts": [
      "Ο Τομ Χανκς κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου για την ερμηνεία του, μόλις έναν χρόνο μετά τη νίκη του για το 'Philadelphia'.",
      "Το φτερό που αιωρείται στην αρχή και στο τέλος της ταινίας συμβολίζει την τυχαιότητα και την ελαφρότητα της ανθρώπινης μοίρας."
    ],
    "source": "https://en.wikipedia.org/wiki/Forrest_Gump",
    "locale": "el-GR",
    "tags": ["forrest_gump", "cinema", "tom_hanks", "quotes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_074",
    "text": "Σε τι είδους σπίτι κατοικεί ο Μπομπ Σφουγγαράκης (SpongeBob SquarePants) στον βυθό του Μπικίνι;",
    "answers": [
      "Σε ένα κοχύλι",
      "Σε έναν ανανά",
      "Σε ένα ναυάγιο πλοίου",
      "Σε μια τσαγιέρα"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μπομπ Σφουγγαράκης ζει σε έναν διώροφο ανανά στο 124 Conch Street στο Βυθό του Μπικίνι (Bikini Bottom).",
    "funFacts": [
      "Ο δημιουργός της σειράς Stephen Hillenburg ήταν θαλάσσιος βιολόγος πριν ασχοληθεί επαγγελματικά με τα κινούμενα σχέδια.",
      "Το κατοικίδιο του Μπομπ είναι το σαλιγκάρι Γκάρι, το οποίο νιαουρίζει σαν γάτα."
    ],
    "source": "https://en.wikipedia.org/wiki/SpongeBob_SquarePants_(character)",
    "locale": "el-GR",
    "tags": ["spongebob", "animation", "nickelodeon", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_075",
    "text": "Ποιο παγκόσμιο hit single του 2007 καθιέρωσε τη Rihanna στην κορυφή της ποπ μουσικής με τη συμμετοχή του Jay-Z;",
    "answers": [
      "Diamonds",
      "Disturbia",
      "Umbrella",
      "Only Girl (In the World)"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι 'Umbrella' από το άλμπουμ 'Good Girl Gone Bad' έγινε παγκόσμια επιτυχία κερδίζοντας βραβείο Grammy.",
    "funFacts": [
      "Το τραγούδι προοριζόταν αρχικά για την Britney Spears, αλλά η δισκογραφική της το απέρριψε πριν φτάσει στη Rihanna.",
      "Στη Μεγάλη Βρετανία, το 'Umbrella' παρέμεινε στο νούμερο 1 για 10 συνεχόμενες εβδομάδες εν μέσω σπάνιων συνεχών βροχοπτώσεων στη χώρα."
    ],
    "source": "https://en.wikipedia.org/wiki/Umbrella_(song)",
    "locale": "el-GR",
    "tags": ["rihanna", "music", "pop", "grammy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_076",
    "text": "Ποιος αγαπημένος ηθοποιός ενσάρκωσε τον 'Σάββα' που κέρδισε το τζόκερ στην κωμική σειρά 'Σαββατογεννημένες';",
    "answers": [
      "Αντώνης Καφετζόπουλος",
      "Γιάννης Μπέζος",
      "Ιεροκλής Μιχαηλίδης",
      "Σάκης Μπουλάς"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Σάκης Μπουλάς έπαιξε τον Σάββα Κατσίκη, τον διπλοπαντρεμένο και τραυματία με αμνησία που κέρδισε 7,5 εκατομμύρια ευρώ.",
    "funFacts": [
      "Οι 'Σαββατογεννημένες' ήταν η πρώτη τηλεοπτική σειρά που έγραψε ο Γιώργος Καπουτζίδης για το Mega Channel (σεζόν 2003-2004).",
      "Ο ρόλος του οξύθυμου μαθητή 'Χοσέ' υποδύθηκε από τον ίδιο τον Γιώργο Καπουτζίδη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%B2%CE%B2%CE%B1%CF%84%CE%BF%CE%B3%CE%B5%CE%BD%CE%BD%CE%B7%CE%BC%CE%AD%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["savvatogennimenes", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_077",
    "text": "Ποια συσκευή χρησιμοποιούν οι μυστικοί πράκτορες στην ταινία 'Men in Black' για να σβήνουν τις μνήμες των πολιτών;",
    "answers": [
      "Neuralyzer (Νευραναστολέας)",
      "Memory Flasher",
      "Brain Eraser",
      "Amnesia Pen"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Neuralyzer είναι μια κυλινδρική μεταλλική συσκευή που εκπέμπει μια έντονη λάμψη φωτός απομονώνοντας και σβήνοντας αναμνήσεις.",
    "funFacts": [
      "Οι πράκτορες φορούν ειδικά μαύρα γυαλιά Ray-Ban για να προστατεύουν τα δικά τους μάτια από τη λάμψη της συσκευής.",
      "Η ταινία Men in Black (1997) με τους Will Smith και Tommy Lee Jones ήταν βασισμένη σε ομώνυμη σειρά κόμικς της Malibu Comics."
    ],
    "source": "https://en.wikipedia.org/wiki/Men_in_Black_(1997_film)",
    "locale": "el-GR",
    "tags": ["men_in_black", "cinema", "sci_fi", "will_smith"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_078",
    "text": "Ποιος ηθοποιός πρωταγωνιστεί ως ο αρχηγός συμμορίας Thomas Shelby στη βρετανική σειρά 'Peaky Blinders';",
    "answers": [
      "Τομ Χάρντι",
      "Κίλιαν Μέρφι",
      "Πολ Άντερσον",
      "Άντριου Σκοτ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ιρλανδός ηθοποιός Cillian Murphy υποδύθηκε τον Thomas Shelby, αρχηγό της εγκληματικής οργάνωσης Peaky Blinders στο Μπέρμιγχαμ.",
    "funFacts": [
      "Το όνομα της συμμορίας Peaky Blinders προήλθε από τη συνήθειά τους να ράβουν ξυραφάκια στο γείσο από τα τραγιάσκα τους.",
      "Ο Cillian Murphy έπρεπε να καπνίζει χιλιάδες ψεύτικα τσιγάρα από βότανα κατά τη διάρκεια των γυρισμάτων των έξι σεζόν."
    ],
    "source": "https://en.wikipedia.org/wiki/Peaky_Blinders_(TV_series)",
    "locale": "el-GR",
    "tags": ["peaky_blinders", "tv", "drama", "cillian_murphy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_079",
    "text": "Από ποιο σπάνιο φανταστικό μέταλλο της Marvel είναι κατασκευασμένη η ασπίδα του Captain America;",
    "answers": [
      "Αδαμάντιο",
      "Κρυπτονίτη",
      "Βιβράνιο (Vibranium)",
      "Ουρού"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η ασπίδα του Captain America είναι φτιαγμένη από Vibranium, ένα μέταλλο ικανό να απορροφά πλήρως κάθε κραδασμό και κινητική ενέργεια.",
    "funFacts": [
      "Στο Marvel Cinematic Universe, το Vibranium προέρχεται αποκλειστικά από τον μετεωρίτη που έπεσε στο αφρικανικό έθνος της Wakanda.",
      "Την πρώτη αυθεντική ασπίδα του Captain America σχεδίασε και κατασκεύασε ο Howard Stark κατά τον Β' Παγκόσμιο Πόλεμο."
    ],
    "source": "https://en.wikipedia.org/wiki/Captain_America%27s_shield",
    "locale": "el-GR",
    "tags": ["captain_america", "marvel", "superheroes", "vibranium"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_080",
    "text": "Σε ποια χώρα επινοήθηκε και προγραμματίστηκε το θρυλικό βιντεοπαιχνίδι παζλ 'Tetris' το 1984;",
    "answers": [
      "Στην Ιαπωνία",
      "Στις ΗΠΑ",
      "Στη Γερμανία",
      "Στη Σοβιετική Ένωση"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Tetris δημιουργήθηκε από τον Σοβιετικό μηχανικό λογισμικού Alexey Pajitnov στην Ακαδημία Επιστημών της ΕΣΣΔ στη Μόσχα.",
    "funFacts": [
      "Το όνομα 'Tetris' προήλθε από τη σύνθεση της ελληνικής λέξης 'τέτρα' (καθώς όλα τα κομμάτια έχουν 4 τετράγωνα) και του τένις.",
      "Το παιχνίδι έγινε παγκόσμιο φαινόμενο όταν κυκλοφόρησε μαζί με την κονσόλα χειρός Game Boy της Nintendo το 1989."
    ],
    "source": "https://en.wikipedia.org/wiki/Tetris",
    "locale": "el-GR",
    "tags": ["tetris", "gaming", "retro", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_081",
    "text": "Τι παραχωρεί η γοργόνα Άριελ στη μάγισσα Ούρσουλα για να αποκτήσει ανθρώπινα πόδια στη 'Μικρή Γοργόνα' (1989);",
    "answers": [
      "Τη φωνή της",
      "Τα μαλλιά της",
      "Το μαγικό της περιδέραιο",
      "Την ουρά των αδελφών της"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Άριελ συμφωνεί να δώσει την πανέμορφη φωνή της στην Ούρσουλα με αντάλλαγμα ένα ξόρκι που θα της χαρίσει ανθρώπινα πόδια για 3 ημέρες.",
    "funFacts": [
      "Η επιτυχία της 'Μικρής Γοργόνας' το 1989 σηματοδότησε την έναρξη της χρυσής περιόδου της Disney γνωστής ως 'Αναγέννηση της Disney' (Disney Renaissance).",
      "Η ταινία βασίστηκε στο κλασικό παραμύθι του Χανς Κρίστιαν Άντερσεν, αλλά με πολύ πιο ευτυχισμένο τέλος."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Little_Mermaid_(1989_film)",
    "locale": "el-GR",
    "tags": ["the_little_mermaid", "disney", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_082",
    "text": "Ποιον αξέχαστο ρόλο μπακαλόγατου υποδύθηκε ο Κώστας Χατζηχρήστος στην κωμωδία 'Της Κακομοίρας' (1963);",
    "answers": [
      "Κυρ-Παντελή",
      "Ζήκο",
      "Μανώλη",
      "Θανάση"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Κώστας Χατζηχρήστος ενσάρκωσε τον ανεπανάληπτο Ζήκο, τον επαρχιώτη βοηθό παντοπωλείου που σχολίαζε τα πάντα με ασταμάτητη φλυαρία.",
    "funFacts": [
      "Οι περισσότερες ατάκες του Ζήκου ήταν εμπνευσμένοι αυτοσχεδιασμοί του ίδιου του Χατζηχρήστου πάνω στα γυρίσματα.",
      "Η ταινία προβλήθηκε έγχρωμη δεκαετίες αργότερα χάρη σε ψηφιακό επιχρωματισμό, γνωρίζοντας νέα τεράστια επιτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%BA%CE%B1%CE%BA%CE%BF%CE%BC%CE%BF%CE%AF%CF%81%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek_cinema", "comedy", "chatzichristos", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_083",
    "text": "Σε ποιο τραγούδι παρουσίασε για πρώτη φορά ο Michael Jackson την εμβληματική χορευτική κίνηση 'Moonwalk' το 1983;",
    "answers": [
      "Thriller",
      "Beat It",
      "Billie Jean",
      "Bad"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Michael Jackson έκανε για πρώτη φορά το Moonwalk ζωντανά στη σκηνή κατά την εκτέλεση του 'Billie Jean' στην τηλεοπτική εκπομπή Motown 25.",
    "funFacts": [
      "Η εκπομπή Motown 25 μεταδόθηκε στις 16 Μαΐου 1983 και την παρακολούθησαν σχεδόν 50 εκατομμύρια τηλεθεατές στις ΗΠΑ.",
      "Ο ίδιος ο Michael Jackson δήλωσε ότι εμπνεύστηκε και έμαθε βασικά στοιχεία της κίνησης από παιδιά χορευτές του δρόμου στο Λος Άντζελες."
    ],
    "source": "https://en.wikipedia.org/wiki/Moonwalk_(dance)",
    "locale": "el-GR",
    "tags": ["michael_jackson", "moonwalk", "billie_jean", "dance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_084",
    "text": "Πώς ονομάζεται το πολυμήχανο αγόρι που μένει μόνο στο σπίτι και αντιμετωπίζει δύο αδέξιους ληστές στην ταινία 'Home Alone';",
    "answers": [
      "Τόμι",
      "Μάικλ",
      "Ντένις",
      "Κέβιν ΜακΚάλιστερ"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Kevin McCallister (Macaulay Culkin) στήνει ξεκαρδιστικές παγίδες για να προστατεύσει το σπίτι του από τους ληστές Χάρι και Μαρβ.",
    "funFacts": [
      "Το 'Home Alone' (1990) παρέμεινε η κωμωδία με τις υψηλότερες εισπράξεις όλων των εποχών στις ΗΠΑ για σχεδόν 27 χρόνια.",
      "Η ταινία γυρίστηκε σχεδόν εξ ολοκλήρου σε πραγματικό σπίτι στο προάστιο Winnetka του Ιλινόις."
    ],
    "source": "https://en.wikipedia.org/wiki/Home_Alone",
    "locale": "el-GR",
    "tags": ["home_alone", "cinema", "christmas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_085",
    "text": "Ποιος Βρετανός ηθοποιός ενσάρκωσε τον σύγχρονο Σέρλοκ Χολμς στην επιτυχημένη σειρά 'Sherlock' του BBC;",
    "answers": [
      "Μπένεντικτ Κάμπερμπατς",
      "Μάρτιν Φρίμαν",
      "Τομ Χίντλστον",
      "Έντι Ρεντμέιν"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Benedict Cumberbatch πρωταγωνίστησε ως Sherlock Holmes δίπλα στον Martin Freeman ως Dr. John Watson.",
    "funFacts": [
      "Η σειρά μετέφερε τις κλασικές ιστορίες του Sir Arthur Conan Doyle στο σύγχρονο Λονδίνο του 21ου αιώνα με τη χρήση smartphones και διαδικτύου.",
      "Ο ρόλος αυτός εκτόξευσε την παγκόσμια καριέρα του Benedict Cumberbatch ανοίγοντάς του την πόρτα για το Χόλιγουντ."
    ],
    "source": "https://en.wikipedia.org/wiki/Sherlock_(TV_series)",
    "locale": "el-GR",
    "tags": ["sherlock", "bbc", "tv", "cumberbatch"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_086",
    "text": "Τι χρώμα και χαρακτηριστικό σχήμα έχει το τέρας Μάικ Βαζόφσκι στην ταινία 'Μπαμπούλας Α.Ε.' (Monsters, Inc.);",
    "answers": [
      "Μπλε με κέρατα",
      "Πράσινο σφαιρικό με ένα μεγάλο μάτι",
      "Μοβ με πολλά πόδια",
      "Κόκκινο με φτερά"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Mike Wazowski είναι ένα μικρόσωμο, πράσινο σφαιρικό τέρας με ένα μοναδικό γιγάντιο μάτι και λεπτά άκρα.",
    "funFacts": [
      "Τη φωνή του Mike Wazowski στην αυθεντική ταινία δάνεισε ο κωμικός Billy Crystal.",
      "Στον κόσμο των τεράτων, η ενέργεια της πόλης Monstropolis παραγόταν από τις κραυγές τρόμου των ανθρώπινων παιδιών."
    ],
    "source": "https://en.wikipedia.org/wiki/Monsters,_Inc.",
    "locale": "el-GR",
    "tags": ["monsters_inc", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_087",
    "text": "Ποιο επίσημο τραγούδι ερμήνευσε η Shakira για το Παγκόσμιο Κύπελλο Ποδοσφαίρου 2010 στη Νότια Αφρική;",
    "answers": [
      "La La La",
      "Hips Don't Lie",
      "Waka Waka (This Time for Africa)",
      "Dare (La La La)"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι 'Waka Waka (This Time for Africa)' έγινε ένα από τα πιο αναγνωρίσιμα αθλητικά και ποπ τραγούδια στον κόσμο.",
    "funFacts": [
      "Το ρεφρέν βασίστηκε στο παραδοσιακό καμερουνέζικο τραγούδι στρατιωτών 'Zangaléwa' του συγκροτήματος Golden Sounds.",
      "Το μουσικό βίντεο του τραγουδιού ήταν ένα από τα πρώτα στην ιστορία του YouTube που ξεπέρασαν το 1 δισεκατομμύριο προβολές."
    ],
    "source": "https://en.wikipedia.org/wiki/Waka_Waka_(This_Time_for_Africa)",
    "locale": "el-GR",
    "tags": ["shakira", "world_cup", "music", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_088",
    "text": "Σε ποιο φανταστικό θεσσαλικό χωριό διαδραματίστηκε η υπόθεση της δραματικής σειράς εποχής 'Άγριες Μέλισσες';",
    "answers": [
      "Στο Καστανόφυτο",
      "Στη Βαλανιδιά",
      "Στον Αμπελώνα",
      "Στο Διαφάνι"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η ζωή των τριών αδελφών Σταμίρη και της ισχυρής οικογένειας Σεβαστού εκτυλίχθηκε στο θεσσαλικό χωριό Διαφάνι.",
    "funFacts": [
      "Για τις ανάγκες της σειράς κατασκευάστηκε εξ ολοκλήρου ένα τεράστιο υπαίθριο σκηνικό χωριού στα στούντιο στα Σπάτα.",
      "Η σειρά προβλήθηκε για 3 σεζόν στον ΑΝΤ1 και θεωρείται υπεύθυνη για την αναβίωση της ελληνικής μυθοπλασίας στην τηλεόραση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CF%81%CE%B9%CE%B5%CF%82_%CE%9C%CE%AD%CE%BB%CE%B9%CF%83%CF%83%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["agries_melisses", "greek_tv", "drama", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_089",
    "text": "Από ποια Περιοχή (District) κατάγεται η Katniss Everdeen στην τριλογία 'The Hunger Games' (Αγώνες Πείνας);",
    "answers": [
      "Από την Περιοχή 12",
      "Από την Περιοχή 1",
      "Από την Περιοχή 4",
      "Από την Περιοχή 7"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Katniss Everdeen κατάγεται από τη φτωχή Περιοχή 12 (District 12) που ειδικεύεται στην εξόρυξη γαιάνθρακα.",
    "funFacts": [
      "Το σύμβολο της επανάστασης που υιοθετεί η Katniss είναι η Κοτσυφόκισσα (Mockingjay).",
      "Η Jennifer Lawrence έγινε η πιο ακριβοπληρωμένη ηρωίδα δράσης στην ιστορία του κινηματογράφου μετά την επιτυχία της ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Katniss_Everdeen",
    "locale": "el-GR",
    "tags": ["hunger_games", "cinema", "jennifer_lawrence", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_090",
    "text": "Ποιο είναι το όνομα του βασικού πρωταγωνιστή με τον πράσινο χιτώνα στη σειρά βιντεοπαιχνιδιών 'The Legend of Zelda';",
    "answers": [
      "Zelda",
      "Link",
      "Ganon",
      "Navi"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο πρωταγωνιστής που ελέγχει ο παίκτης ονομάζεται Link, ενώ η Zelda είναι η πριγκίπισσα του βασιλείου της Hyrule.",
    "funFacts": [
      "Πολλοί περιστασιακοί παίκτες μπερδεύουν το όνομα του πρωταγωνιστή θεωρώντας λανθασμένα ότι ονομάζεται Zelda λόγω του τίτλου.",
      "Ο δημιουργός Shigeru Miyamoto εμπνεύστηκε το όνομα της πριγκίπισσας Zelda από τη Zelda Fitzgerald, σύζυγο του F. Scott Fitzgerald."
    ],
    "source": "https://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)",
    "locale": "el-GR",
    "tags": ["zelda", "link", "nintendo", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_091",
    "text": "Πώς ονομάζεται το μαγικό σφυρί του Thor που μπορεί να σηκώσει μόνο όποιος είναι 'άξιος';",
    "answers": [
      "Stormbreaker",
      "Gungnir",
      "Mjolnir (Μγιόλνιρ)",
      "Aegis"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Mjolnir σφυρηλατήθηκε στην καρδιά ενός ετοιμοθάνατου άστρου και μόνο όποιος είναι ηθικά άξιος μπορεί να το σηκώσει.",
    "funFacts": [
      "Στην ταινία 'Avengers: Endgame', ο Captain America αποδεικνύεται άξιος και σηκώνει το Mjolnir σε μια από τις πιο διάσημες σκηνές του MCU.",
      "Στη σκανδιναβική μυθολογία, το Mjolnir κατασκευάστηκε από τους νάνους αδελφούς Sindri και Brokkr."
    ],
    "source": "https://en.wikipedia.org/wiki/Mj%C3%B6lnir_(Marvel_Cinematic_Universe)",
    "locale": "el-GR",
    "tags": ["thor", "marvel", "superheroes", "mjolnir"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_092",
    "text": "Ποια είναι η αγαπημένη ενδυματολογική συμβουλή του Barney Stinson στη σειρά 'How I Met Your Mother';",
    "answers": [
      "Stay Casual!",
      "Dress to Impress!",
      "Always be Cool!",
      "Suit Up!"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Barney Stinson (Neil Patrick Harris) είναι παθιασμένος με τα κοστούμια και παροτρύνει συνεχώς τους φίλους του λέγοντας 'Suit Up!'.",
    "funFacts": [
      "Ο Barney διαθέτει ακόμα και μεταξωτές πιτζάμες κομμένες στο σχήμα κοστουμιού (suitjamas) για τον ύπνο.",
      "Το άλλο διάσημο μότο του Barney είναι το 'Legen... wait for it... dary!'."
    ],
    "source": "https://en.wikipedia.org/wiki/Barney_Stinson",
    "locale": "el-GR",
    "tags": ["how_i_met_your_mother", "tv", "sitcom", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_093",
    "text": "Ποια εμβληματική φράση λέει ο εξωγήινος E.T. στην κλασική ταινία του Steven Spielberg (1982);",
    "answers": [
      "E.T. phone home",
      "E.T. go home",
      "E.T. love Elliott",
      "E.T. fly moon"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η φράση 'E.T. phone home' αποτελεί μία από τις διασημότερες κινηματογραφικές ατάκες στην ιστορία του σινεμά.",
    "funFacts": [
      "Η διάσημη σκηνή με το ποδήλατο του Elliott να πετάει μπροστά από την πανσέληνο έγινε το επίσημο λογότυπο της εταιρείας Amblin Entertainment.",
      "Η ταινία ξεπέρασε τον 'Πόλεμο των Άστρων' και έγινε η πιο κερδοφόρα ταινία όλων των εποχών μέχρι τότε."
    ],
    "source": "https://en.wikipedia.org/wiki/E.T._the_Extra-Terrestrial",
    "locale": "el-GR",
    "tags": ["et", "cinema", "spielberg", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_094",
    "text": "Σε ποια θέση τερμάτισε η Καλομοίρα εκπροσωπώντας την Ελλάδα στη Eurovision του 2008 με το 'Secret Combination';",
    "answers": [
      "1η θέση",
      "3η θέση",
      "5η θέση",
      "2η θέση"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Καλομοίρα κατέκτησε την εξαιρετική 3η θέση στον τελικό του Βελιγραδίου το 2008, συγκεντρώνοντας 218 βαθμούς.",
    "funFacts": [
      "Η Ελλάδα κέρδισε τον πρώτο ημιτελικό εκείνης της χρονιάς με την Καλομοίρα να τερματίζει στην κορυφή πριν τον τελικό.",
      "Το τραγούδι έγινε τεράστια ραδιοφωνική επιτυχία σε όλη την Ευρώπη και αγαπήθηκε ιδιαίτερα από τους eurofans."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%BC%CE%BC%CE%B5%CF%84%CE%BF%CF%87%CE%AE_%CF%84%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1%CF%82_%CF%83%CF%84%CE%B7_%CE%93%CE%B9%CE%BF%CF%85%CF%81%CE%BF%CE%B2%CE%AF%CE%B6%CE%B9%CE%BF%CE%BD_2008",
    "locale": "el-GR",
    "tags": ["eurovision", "greece", "kalomira", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_095",
    "text": "Ποιο ζώο είναι ο Ρεμί που ονειρεύεται να γίνει διάσημος σεφ στο Παρίσι στην ταινία 'Ratatouille' (2007);",
    "answers": [
      "Σκύλος",
      "Γάτα",
      "Αρουραίος",
      "Κουνέλι"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ρεμί είναι ένας προικισμένος αρουραίος με εξαιρετικά ανεπτυγμένη όσφρηση και γεύση που μαγειρεύει κρυμμένος κάτω από το καπέλο του Λινγκουίνι.",
    "funFacts": [
      "Για να σχεδιάσουν ρεαλιστικά τα φαγητά, οι συντελεστές της Pixar παρακολούθησαν μαθήματα γαλλικής γαστρονομίας με κορυφαίους σεφ.",
      "Η ταινία κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2008."
    ],
    "source": "https://en.wikipedia.org/wiki/Ratatouille_(film)",
    "locale": "el-GR",
    "tags": ["ratatouille", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_096",
    "text": "Ποιο funk τραγούδι του Mark Ronson με τη φωνή του Bruno Mars κυριάρχησε στα παγκόσμια charts το 2014-2015;",
    "answers": [
      "24K Magic",
      "Locked Out of Heaven",
      "Treasure",
      "Uptown Funk"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Uptown Funk' παρέμεινε στο νούμερο 1 του Billboard Hot 100 για 14 συνεχόμενες εβδομάδες και κέρδισε δύο βραβεία Grammy.",
    "funFacts": [
      "Το μουσικό βίντεο κλιπ του Uptown Funk ξεπέρασε τα 5 δισεκατομμύρια προβολές στο YouTube, όντας ένα από τα πιο προβεβλημένα όλων των εποχών.",
      "Το τραγούδι είναι εμπνευσμένο από τον ήχο Minneapolis funk της δεκαετίας του 1980."
    ],
    "source": "https://en.wikipedia.org/wiki/Uptown_Funk",
    "locale": "el-GR",
    "tags": ["bruno_mars", "mark_ronson", "music", "funk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_097",
    "text": "Ποια ερώτηση θέτει το διάσημο θεματικό τραγούδι της ταινίας 'Ghostbusters' (1984);",
    "answers": [
      "Who you gonna call?",
      "Where you gonna hide?",
      "What you gonna do?",
      "Why you gonna run?"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι του Ray Parker Jr. ρωτάει 'Who you gonna call?' με την κλασική απάντηση να είναι 'Ghostbusters!'.",
    "funFacts": [
      "Το όχημα των Ghostbusters είναι μια τροποποιημένη Cadillac Miller-Meteor ασθενοφόρο του 1959 με το όνομα Ecto-1.",
      "Το τραγούδι προτάθηκε για Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 1985."
    ],
    "source": "https://en.wikipedia.org/wiki/Ghostbusters_(song)",
    "locale": "el-GR",
    "tags": ["ghostbusters", "cinema", "music", "80s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_098",
    "text": "Ποιο τηλεοπτικό φορμάτ χρησιμοποιεί η επιτυχημένη κωμική σειρά 'Modern Family';",
    "answers": [
      "Κλασικό sitcom με ζωντανό κοινό",
      "Ψευδοντοκιμαντέρ (Mockumentary)",
      "Μιούζικαλ",
      "Κινούμενα σχέδια"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η σειρά χρησιμοποιεί το στυλ του mockumentary, όπου οι χαρακτήρες μιλούν συχνά κατευθείαν στην κάμερα σαν να δίνουν συνέντευξη.",
    "funFacts": [
      "Η σειρά κέρδισε το Βραβείο Emmy Καλύτερης Κωμικής Σειράς για πέντε συνεχόμενα χρόνια (2010-2014).",
      "Ο χαρακτήρας της Gloria Delgado-Pritchett ανέδειξε την Κολομβιανή ηθοποιό Sofía Vergara σε μία από τις πιο ακριβοπληρωμένες τηλεοπτικές σταρ."
    ],
    "source": "https://en.wikipedia.org/wiki/Modern_Family",
    "locale": "el-GR",
    "tags": ["modern_family", "tv", "comedy", "sitcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_099",
    "text": "Ποια είναι η επίσημη βασιλική και εθνική χαιρετιστήρια κραυγή στο αφρικανικό βασίλειο της Wakanda στο 'Black Panther';",
    "answers": [
      "Wakanda United!",
      "Long Live Wakanda!",
      "Wakanda Forever!",
      "Glory to Wakanda!"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Wakanda Forever' συνοδεύεται από τη χαρακτηριστική κίνηση με τα χέρια σταυρωμένα στο στήθος.",
    "funFacts": [
      "Ο πρωταγωνιστής Chadwick Boseman έδωσε μια συγκλονιστική ερμηνεία πριν τον πρόωρο θάνατό του το 2020.",
      "Το Black Panther (2018) έγινε η πρώτη ταινία με υπερήρωες στην ιστορία που προτάθηκε για Όσκαρ Καλύτερης Ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Black_Panther_(film)",
    "locale": "el-GR",
    "tags": ["black_panther", "marvel", "mcu", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_100",
    "text": "Σε ποιο νησί εκτυλίσσεται η κλασική ελληνική ταινία 'Μανταλένα' (1960) με πρωταγωνίστρια την Αλίκη Βουγιουκλάκη;",
    "answers": [
      "Στην Ύδρα",
      "Στη Σαντορίνη",
      "Στη Μύκονο",
      "Στην Αντίπαρο"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η 'Μανταλένα' γυρίστηκε εξ ολοκλήρου στο κυκλαδίτικο νησί της Αντιπάρου, αναδεικνύοντας τις ομορφιές του.",
    "funFacts": [
      "Η ταινία εκπροσώπησε την Ελλάδα στο Φεστιβάλ Κινηματογράφου των Καννών το 1961.",
      "Η Αλίκη Βουγιουκλάκη κέρδισε το Βραβείο Α' Γυναικείου Ρόλου στην 1η Εβδομάδα Ελληνικού Κινηματογράφου στη Θεσσαλονίκη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BD%CF%84%CE%B1%CE%BB%CE%AD%CE%BD%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek_cinema", "vougiouklaki", "classics", "antiparos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_101",
    "text": "Ποιο είναι το είδος του ζώου και το σήμα κατατεθέν της μασκότ Sonic της εταιρείας Sega;",
    "answers": [
      "Μπλε σκαντζόχοιρος",
      "Κόκκινη αλεπού",
      "Πράσινος δεινόσαυρος",
      "Κίτρινος σκίουρος"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Sonic the Hedgehog είναι ένας υπερηχητικός μπλε σκαντζόχοιρος που τρέχει με ασύλληπτη ταχύτητα μαζεύοντας χρυσά δαχτυλίδια.",
    "funFacts": [
      "Ο Sonic δημιουργήθηκε από τη Sega για να ανταγωνιστεί άμεσα τον Mario της Nintendo στις αρχές της δεκαετίας του 1990.",
      "Τα παπούτσια του Sonic εμπνεύστηκαν από τις μπότες του Michael Jackson στο άλμπουμ 'Bad' και το χρώμα του Άγιου Βασίλη."
    ],
    "source": "https://en.wikipedia.org/wiki/Sonic_the_Hedgehog",
    "locale": "el-GR",
    "tags": ["sonic", "sega", "gaming", "video_games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_102",
    "text": "Ποιος είναι ο frontman και τραγουδιστής του παγκοσμίου φήμης βρετανικού συγκροτήματος Coldplay;",
    "answers": [
      "Thom Yorke",
      "Chris Martin",
      "Matt Bellamy",
      "Alex Turner"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Chris Martin ίδρυσε τους Coldplay στο Λονδίνο το 1996 μαζί με τον Jonny Buckland, τον Guy Berryman και τον Will Champion.",
    "funFacts": [
      "Η παγκόσμια περιοδεία τους 'Music of the Spheres World Tour' περιλάμβανε και δύο sold-out συναυλίες στο ΟΑΚΑ στην Αθήνα το καλοκαίρι του 2024.",
      "Οι Coldplay χρησιμοποιούν κινητικά δάπεδα και στατικά ποδήλατα στις συναυλίες τους ώστε το κοινό να παράγει μέρος της απαιτούμενης ηλεκτρικής ενέργειας."
    ],
    "source": "https://en.wikipedia.org/wiki/Chris_Martin",
    "locale": "el-GR",
    "tags": ["coldplay", "chris_martin", "music", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_103",
    "text": "Ποιοι δύο ηθοποιοί χορεύουν το διάσημο τουίστ στο εστιατόριο Jack Rabbit Slim's στην ταινία 'Pulp Fiction' (1994);",
    "answers": [
      "Μπρους Γουίλις και Ούμα Θέρμαν",
      "Σάμιουελ Τζάκσον και Τζον Τραβόλτα",
      "Τζον Τραβόλτα και Ούμα Θέρμαν",
      "Χάρβεϊ Καϊτέλ και Ούμα Θέρμαν"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Vincent Vega (John Travolta) και η Mia Wallace (Uma Thurman) χορεύουν το 'You Never Can Tell' του Chuck Berry κερδίζοντας το τρόπαιο.",
    "funFacts": [
      "Ο Quentin Tarantino εμπνεύστηκε τη χορογραφία από τη γαλλική ταινία του Jean-Luc Godard 'Bande à part' (1964).",
      "Η ταινία κέρδισε τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών και το Όσκαρ Καλύτερου Πρωτότυπου Σεναρίου."
    ],
    "source": "https://en.wikipedia.org/wiki/Pulp_Fiction",
    "locale": "el-GR",
    "tags": ["pulp_fiction", "tarantino", "cinema", "travolta"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_104",
    "text": "Τι μορφή έχει εξωτερικά το σκάφος TARDIS του Time Lord στη βρετανική σειρά επιστημονικής φαντασίας 'Doctor Who';",
    "answers": [
      "Κόκκινου λεωφορείου",
      "Τηλεφωνικού θαλάμου της Νέας Υόρκης",
      "Ασημένιου δίσκου",
      "Μπλε βρετανικού αστυνομικού θαλάμου"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το TARDIS έχει τη μορφή ενός βρετανικού αστυνομικού τηλεφωνικού θαλάμου της δεκαετίας του 1960 και είναι πολύ μεγαλύτερο εσωτερικά ('bigger on the inside').",
    "funFacts": [
      "Το ακρωνύμιο TARDIS σημαίνει 'Time And Relative Dimension In Space'.",
      "Το Doctor Who είναι η μακροβιότερη τηλεοπτική σειρά επιστημονικής φαντασίας στον κόσμο, έχοντας ξεκινήσει το 1963."
    ],
    "source": "https://en.wikipedia.org/wiki/TARDIS",
    "locale": "el-GR",
    "tags": ["doctor_who", "bbc", "sci_fi", "tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_105",
    "text": "Ποιο μαγεμένο αντικείμενο μετρά τον χρόνο που απομένει στον Πρίγκιπα για να σπάσει την κατάρα στην 'Πεντάμορφη και το Τέρας';",
    "answers": [
      "Ένα μαγεμένο τριαντάφυλλο",
      "Μια μαγική κλεψύδρα",
      "Ένα χρυσό ρολόι",
      "Ένας σπασμένος καθρέφτης"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Τέρας πρέπει να αγαπήσει και να αγαπηθεί πριν πέσει και το τελευταίο πέταλο του μαγεμένου τριαντάφυλλου την ημέρα των 21ων γενεθλίων του.",
    "funFacts": [
      "Η 'Πεντάμορφη και το Τέρας' (1991) ήταν η πρώτη ταινία κινουμένων σχεδίων στην ιστορία που προτάθηκε για Όσκαρ Καλύτερης Ταινίας.",
      "Το τραγούδι των τίτλων ερμήνευσαν ντουέτο η Celine Dion και ο Peabo Bryson, κερδίζοντας βραβείο Όσκαρ."
    ],
    "source": "https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film)",
    "locale": "el-GR",
    "tags": ["beauty_and_the_beast", "disney", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_106",
    "text": "Ποιοι τέσσερις ηθοποιοί αποτελούσαν την αρχική παρέα της θρυλικής κωμικής σειράς του Mega 'Οι Απαράδεκτοι';",
    "answers": [
      "Χάρης Ρώμας, Ελένη Ράντου, Βασίλης Χαραλαμπόπουλος, Γιάννης Μπέζος",
      "Σπύρος Παπαδόπουλος, Δήμητρα Παπαδοπούλου, Γιάννης Μπέζος, Βλάσσης Μπονάτσος",
      "Κώστας Κόκλας, Καίτη Κωνσταντίνου, Υρώ Μανέ, Χρήστος Χατζηπαναγιώτης",
      "Αντώνης Καφετζόπουλος, Βλαδίμηρος Κυριακίδης, Ρένια Λουιζίδου, Σάκης Μπουλάς"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι Σπύρος Παπαδόπουλος, Δήμητρα Παπαδοπούλου, Γιάννης Μπέζος και Βλάσσης Μπονάτσος έγραψαν τηλεοπτική ιστορία ως οι ένοικοι της οδού Αδάμαντος 4 στην πλατεία Λυκαβηττού.",
    "funFacts": [
      "Το σενάριο της σειράς έγραψε η ίδια η Δήμητρα Παπαδοπούλου, εισάγοντας έναν μοντέρνο και ανατρεπτικό τηλεοπτικό λόγο.",
      "Η σειρά υπήρξε πρωτοποριακή για την ελληνική τηλεόραση, προβάλλοντας τον πρώτο ανοιχτά ομοφυλόφιλο βασικό χαρακτήρα (Γιάννης Μπέζος)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["oi_aparadektoi", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_107",
    "text": "Ποιο είναι το μυστικό όπλο της Wonder Woman που αναγκάζει όποιον τυλίγει να λέει πάντα την απόλυτη αλήθεια;",
    "answers": [
      "Το Σπαθί της Αθηνάς",
      "Η Χρυσή Ασπίδα",
      "Το Λάσο της Αλήθειας",
      "Η Τιάρα της Θεμίσκυρας"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Λάσο της Αλήθειας (Lasso of Truth) σφυρηλατήθηκε από τη ζώνη της Εστίας και είναι άθραυστο, εξαναγκάζοντας οποιονδήποτε αιχμάλωτο σε απόλυτη ειλικρίνεια.",
    "funFacts": [
      "Ο δημιουργός της Wonder Woman, William Moulton Marston, ήταν ψυχολόγος που συνέβαλε καθοριστικά στην εφεύρεση του πρώτου σύγχρονου ανιχνευτή ψεύδους (πολύγραφου).",
      "Στη σύγχρονη κινηματογραφική μεταφορά, την Αμαζόνα πριγκίπισσα Ντιάνα υποδύθηκε η Gal Gadot."
    ],
    "source": "https://en.wikipedia.org/wiki/Lasso_of_Truth",
    "locale": "el-GR",
    "tags": ["wonder_woman", "dc_comics", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_108",
    "text": "Ποιο εργαλείο χρησιμοποιεί ο παίκτης στο mobile παιχνίδι 'Angry Birds' για να εκτοξεύει τα πουλιά στα γουρούνια;",
    "answers": [
      "Κανόνι",
      "Καταπέλτη",
      "Τόξο",
      "Σφεντόνα"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο παίκτης ρυθμίζει τη γωνία και τη δύναμη μιας γιγάντιας σφεντόνας (slingshot) για να γκρεμίσει τις κατασκευές των πράσινων γουρουνιών.",
    "funFacts": [
      "Το παιχνίδι δημιουργήθηκε από τη φινλανδική εταιρεία Rovio Entertainment και ξεπέρασε τα 5 δισεκατομμύρια downloads σε όλες τις πλατφόρμες.",
      "Τα πράσινα γουρούνια σχεδιάστηκαν πράσινα επειδή κατά την περίοδο ανάπτυξης του παιχνιδιού (2009) υπήρχε η επιδημία της γρίπης των χοίρων (H1N1)."
    ],
    "source": "https://en.wikipedia.org/wiki/Angry_Birds",
    "locale": "el-GR",
    "tags": ["angry_birds", "gaming", "mobile", "rovio"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_109",
    "text": "Ποιο τραγούδι της Katy Perry έγινε παγκόσμιος ενθαρρυντικός ύμνος αυτοπεποίθησης με στίχους όπως 'Cause baby, you're a firework';",
    "answers": [
      "Firework",
      "Roar",
      "California Gurls",
      "Dark Horse"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Firework' από το άλμπουμ 'Teenage Dream' (2010) έγινε ένα από τα πιο αναγνωρίσιμα και εμπορικά επιτυχημένα τραγούδια της Katy Perry.",
    "funFacts": [
      "Το άλμπουμ 'Teenage Dream' ισοφάρισε το ιστορικό ρεκόρ του Michael Jackson ('Bad') με 5 νούμερο 1 singles από το ίδιο άλμπουμ στο Billboard Hot 100.",
      "Η Katy Perry έχει ερμηνεύσει το Firework σε ιστορικές περιστάσεις, όπως στην τελετή ορκωμοσίας του προέδρου των ΗΠΑ το 2021."
    ],
    "source": "https://en.wikipedia.org/wiki/Firework_(song)",
    "locale": "el-GR",
    "tags": ["katy_perry", "music", "pop", "firework"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_110",
    "text": "Ποια εμβληματική ατάκα λέει ο Arnold Schwarzenegger στην πρώτη ταινία 'Ο Εξολοθρευτής' (The Terminator, 1984) πριν αποχωρήσει από το αστυνομικό τμήμα;",
    "answers": [
      "Hasta la vista, baby",
      "I'll be back",
      "Get to the chopper",
      "Come with me if you want to live"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η φράση 'I'll be back' αποτελεί ίσως την πιο αναγνωρίσιμη ατάκα δράσης στην ιστορία του κινηματογράφου.",
    "funFacts": [
      "Ο Σβαρτσενέγκερ αρχικά προσπάθησε να πείσει τον σκηνοθέτη Τζέιμς Κάμερον να αλλάξει την ατάκα σε 'I will be back' γιατί δυσκολευόταν να προφέρει το 'I'll'.",
      "Το Αμερικανικό Ινστιτούτο Κινηματογράφου (AFI) κατέταξε την ατάκα στο νούμερο 37 των σπουδαιότερων κινηματογραφικών φράσεων όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/I%27ll_be_back",
    "locale": "el-GR",
    "tags": ["terminator", "cinema", "schwarzenegger", "quotes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'easy', 1, questions)

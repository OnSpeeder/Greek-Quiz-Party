# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_easy_111",
    "text": "Ποιο ιστορικό arcade παιχνίδι της Taito (1978) έβαλε τους παίκτες να εξολοθρεύουν σειρές εξωγήινων που κατεβαίνουν αργά στην οθόνη;",
    "answers": ["Space Invaders", "Galaga", "Asteroids", "Defender"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Space Invaders σχεδιάστηκε από τον Tomohiro Nishikado και ήταν ένα από τα πρώτα παγκόσμια blockbusters στην ιστορία των ηλεκτρονικών παιχνιδιών.",
    "funFacts": [
      "Ο αστικός μύθος υποστηρίζει ότι το παιχνίδι προκάλεσε προσωρινή έλλειψη κερμάτων των 100 γεν στην Ιαπωνία λόγω της τεράστιας δημοτικότητάς του.",
      "Η μουσική του επιταχύνει σταδιακά καθώς λιγοστεύουν οι εξωγήινοι, δημιουργώντας πρωτοποριακή ένταση και αγωνία για την εποχή."
    ],
    "source": "https://el.wikipedia.org/wiki/Space_Invaders",
    "locale": "el-GR",
    "tags": ["space-invaders", "taito", "arcade", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_112",
    "text": "Ποια θρυλική 8-bit κονσόλα της Nintendo (γνωστή στην Ιαπωνία ως Famicom) αναζωογόνησε τη διεθνή βιομηχανία βιντεοπαιχνιδιών τη δεκαετία του '80;",
    "answers": ["Atari 2600", "NES (Nintendo Entertainment System)", "Sega Master System", "Commodore 64"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το NES κυκλοφόρησε στη Βόρεια Αμερική το 1985 και έσωσε την αγορά των οικιακών βιντεοπαιχνιδιών μετά το μεγάλο κραχ του 1983.",
    "funFacts": [
      "Για να πείσει τα καταστήματα να το τοποθετήσουν στα ράφια τους μετά την κρίση, η Nintendo το διαφήμισε ως σύστημα ψυχαγωγίας μαζί με ένα ρομποτικό παιχνίδι, το R.O.B.",
      "Συνοδεύτηκε από το αυστηρό πρότυπο ποιότητας 'Nintendo Seal of Quality' για να εγγυάται ότι τα παιχνίδια δεν ήταν πρόχειρα κατασκευασμένα."
    ],
    "source": "https://el.wikipedia.org/wiki/Nintendo_Entertainment_System",
    "locale": "el-GR",
    "tags": ["nes", "nintendo", "famicom", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_113",
    "text": "Ποιο επικό action RPG ανοιχτού κόσμου της FromSoftware (2022) αναπτύχθηκε σε συνεργασία με τον συγγραφέα του «Game of Thrones», George R. R. Martin;",
    "answers": ["Bloodborne", "Dark Souls III", "Elden Ring", "Sekiro"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Elden Ring σκηνοθετήθηκε από τον Hidetaka Miyazaki, ενώ ο George R. R. Martin συνέγραψε τη μυθολογία και την κοσμογονία των Lands Between.",
    "funFacts": [
      "Κέρδισε τον τίτλο του Game of the Year στα The Game Awards 2022 και πούλησε πάνω από 25 εκατομμύρια αντίτυπα παγκοσμίως.",
      "Ο πιστός κερασφόρος επιβήτορας του παίκτη, ο Torrent, επιτρέπει γρήγορη μετακίνηση και διπλά άλματα στον απέραντο χάρτη."
    ],
    "source": "https://el.wikipedia.org/wiki/Elden_Ring",
    "locale": "el-GR",
    "tags": ["elden-ring", "fromsoftware", "action-rpg", "george-martin"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_114",
    "text": "Ποιος πρώην μαφιόζος με το γαλάζιο χαβανέζικο πουκάμισο είναι ο κεντρικός πρωταγωνιστής στο «Grand Theft Auto: Vice City» (2002);",
    "answers": ["Niko Bellic", "Claude", "Carl Johnson", "Tommy Vercetti"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Tommy Vercetti ταξιδεύει στη Vice City (εμπνευσμένη από το Μαϊάμι της δεκαετίας του 1980) μετά την αποφυλάκισή του και χτίζει τη δική του εγκληματική αυτοκρατορία.",
    "funFacts": [
      "Τη φωνή του Tommy Vercetti δάνεισε ο διάσημος ηθοποιός Ray Liotta, πρωταγωνιστής της ταινίας 'Goodfellas'.",
      "Η αισθητική και η πλοκή του παιχνιδιού άντλησαν έντονη έμπνευση από την ταινία 'Ο Σημαδεμένος' (Scarface) και την τηλεοπτική σειρά 'Miami Vice'."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City",
    "locale": "el-GR",
    "tags": ["gta", "vice-city", "tommy-vercetti", "rockstar-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_115",
    "text": "Ποιος βασιλιάς των θεών του Ολύμπου και πατέρας του Κράτου αποτελεί τον τελικό αντίπαλο στο «God of War III»;",
    "answers": ["Δίας", "Ποσειδώνας", "Άδης", "Ήλιος"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Δίας είναι ο ανώτατος άρχοντας των Ολύμπιων θεών και ο απόλυτος εχθρός του Κράτου στο αποκορύφωμα της ελληνικής τριλογίας God of War.",
    "funFacts": [
      "Στο God of War II αποκαλύπτεται ότι ο Δίας είναι ο πραγματικός βιολογικός πατέρας του Κράτου.",
      "Η τελική αναμέτρηση του God of War III συνδυάζει μάχες πρώτου και τρίτου προσώπου πάνω στην καρδιά της Γαίας."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_III",
    "locale": "el-GR",
    "tags": ["god-of-war", "kratos", "zeus", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_116",
    "text": "Τι καταναλώνει κατά εκατοντάδες ο Pac-Man καθώς διασχίζει τους διαδρόμους του κλασικού λαβύρινθου;",
    "answers": ["Νομίσματα", "Μικρές τελείες (Pac-Dots)", "Διαμάντια", "Μπισκότα"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Pac-Man πρέπει να καταναλώσει και τις 240 μικρές τελείες (Pac-Dots) και τα 4 μεγάλα χάπια δύναμης για να ολοκληρώσει κάθε πίστα.",
    "funFacts": [
      "Κάθε μικρή τελεία προσφέρει 10 πόντους, ενώ τα μεγάλα χάπια (Power Pellets) προσφέρουν 50 πόντους.",
      "Το χαρακτηριστικό ηχητικό εφέ του Pac-Man καθώς τρώει τις τελείες ('γουάκα-γουάκα') είναι ένα από τα πιο αναγνωρίσιμα ηχητικά σήματα στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/Pac-Man",
    "locale": "el-GR",
    "tags": ["pac-man", "namco", "arcade", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_117",
    "text": "Ποια κόκκινη έχιδνα (echidna) και πιστός φύλακας του Master Emerald ξεκίνησε ως αντίπαλος και έγινε σύμμαχος του Sonic;",
    "answers": ["Tails", "Shadow", "Knuckles (Νακλς)", "Silver"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Knuckles the Echidna πρωτοεμφανίστηκε στο Sonic the Hedgehog 3 (1994) και διαθέτει πανίσχυρες γροθιές και ικανότητα αναρρίχησης σε τοίχους.",
    "funFacts": [
      "Ζει στο ιπτάμενο νησί Angel Island και είναι ο τελευταίος επιζών της αρχαίας φυλής των εχιδνών.",
      "Στην ταινία 'Sonic the Hedgehog 2' (2022), τη φωνή του Knuckles δάνεισε ο διάσημος ηθοποιός Idris Elba."
    ],
    "source": "https://en.wikipedia.org/wiki/Knuckles_the_Echidna",
    "locale": "el-GR",
    "tags": ["sonic", "knuckles", "sega", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_118",
    "text": "Ποια διεφθαρμένη πολυεθνική φαρμακευτική εταιρεία με το ασπροκόκκινο λογότυπο ευθύνεται για τα βιολογικά όπλα στο «Resident Evil»;",
    "answers": ["Aperture Science", "Vault-Tec", "Abstergo Industries", "Umbrella Corporation"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Umbrella Corporation παρουσιαζόταν εξωτερικά ως κολοσσός φαρμάκων και καλλυντικών, ενώ στα υπόγεια εργαστήριά της κατασκεύαζε ιούς και βιολογικά τέρατα.",
    "funFacts": [
      "Το σύνθημα της εταιρείας ήταν 'Our business is life itself' ('Η δουλειά μας είναι η ίδια η ζωή').",
      "Ιδρύθηκε τη δεκαετία του 1960 από τους Oswell E. Spencer, Edward Ashford και James Marcus μετά την ανακάλυψη του ιού Progenitor στην Αφρική."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident-evil", "umbrella", "capcom", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_119",
    "text": "Ποια νεαρή κοπέλα με τα σταχτιά μαλλιά και το Αρχαίο Αίμα είναι η θετή κόρη του Geralt of Rivia στο «The Witcher 3: Wild Hunt»;",
    "answers": ["Σίρι (Ciri)", "Γένεφερ (Yennefer)", "Τρις (Triss)", "Κίρα (Keira)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Cirilla Fiona Elen Riannon (Ciri) διαθέτει την ικανότητα να τηλεμεταφέρεται ανάμεσα στον χώρο και τον χρόνο και καταδιώκεται από την Άγρια Κυνηγεσία (Wild Hunt).",
    "funFacts": [
      "Η Ciri συνδέεται με τον Geralt μέσω του 'Νόμου της Έκπληξης' (Law of Surprise), ενός αρχαίου εθίμου του κόσμου του Witcher.",
      "Στο παιχνίδι, ο παίκτης αναλαμβάνει τον έλεγχο της Ciri σε ειδικές αναδρομικές αποστολές μάχης."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
    "locale": "el-GR",
    "tags": ["witcher", "ciri", "geralt", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_120",
    "text": "Ποιος είναι ο βασικός ενεργειακός πόρος που αυξάνεται κατά ένα σε κάθε γύρο και χρησιμοποιείται για να παιχτούν κάρτες στο «Hearthstone»;",
    "answers": ["Χρυσός", "Μάνα (Mana)", "Ενέργεια (Energy)", "Σθένος (Stamina)"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι παίκτες ξεκινούν με 1 κρύσταλλο Mana στον πρώτο γύρο και κερδίζουν έναν επιπλέον σε κάθε επόμενο γύρο, μέχρι το μέγιστο όριο των 10 κρυστάλλων.",
    "funFacts": [
      "Ο παίκτης που παίζει δεύτερος λαμβάνει μια ειδική δωρεάν κάρτα ('The Coin') που του χαρίζει 1 επιπλέον προσωρινό κρύσταλλο Mana για να εξισορροπηθεί το μειονέκτημα σειράς.",
      "Ορισμένες κάρτες διαθέτουν την ιδιότητα 'Overload', η οποία κλειδώνει συγκεκριμένο αριθμό κρυστάλλων Mana στον επόμενο γύρο."
    ],
    "source": "https://el.wikipedia.org/wiki/Hearthstone",
    "locale": "el-GR",
    "tags": ["hearthstone", "blizzard", "mana", "card-game"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_121",
    "text": "Ποιος μικρός ευκίνητος χιμπατζής με κόκκινο καπέλο είναι ο καλύτερος φίλος και βοηθός του Donkey Kong;",
    "answers": ["Funky Kong", "Cranky Kong", "Diddy Kong", "Dixie Kong"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Diddy Kong δημιουργήθηκε από τη βρετανική εταιρεία Rare για το Donkey Kong Country (1994) και χρησιμοποιεί jetpacks από βαρέλια και πιστόλια φυστικιών.",
    "funFacts": [
      "Πρωταγωνίστησε στο δικό του εξαιρετικά επιτυχημένο παιχνίδι αγώνων, το Diddy Kong Racing (1997) στο Nintendo 64.",
      "Αρχικά η Rare σχεδίαζε να εκσυγχρονίσει τον Donkey Kong Jr., αλλά η Nintendo ζήτησε να δημιουργηθεί ένας εντελώς νέος χαρακτήρας, γεννώντας τον Diddy."
    ],
    "source": "https://en.wikipedia.org/wiki/Diddy_Kong",
    "locale": "el-GR",
    "tags": ["diddy-kong", "donkey-kong", "nintendo", "rare"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_122",
    "text": "Ποιο εμβληματικό τετράποδο πράσινο πλάσμα στο Minecraft πλησιάζει αθόρυβα τους παίκτες και εκρήγνυται με ένα χαρακτηριστικό σφύριγμα;",
    "answers": ["Zombie", "Skeleton", "Enderman", "Creeper"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Creeper είναι το πιο διάσημο εχθρικό πλάσμα του Minecraft, γνωστό για την ξαφνική αυτοκαταστροφική του έκρηξη που γκρεμίζει κτίσματα.",
    "funFacts": [
      "Ο δημιουργός Markus 'Notch' Persson δημιούργησε τον Creeper κατά λάθος, όταν μπέρδεψε το ύψος με το μήκος κατά τον προγραμματισμό του μοντέλου ενός γουρουνιού.",
      "Το πρόσωπο του Creeper ενσωματώθηκε επίσημα στο λογότυπο του τίτλου του Minecraft, αντικαθιστώντας το γράμμα 'A'."
    ],
    "source": "https://el.wikipedia.org/wiki/Minecraft",
    "locale": "el-GR",
    "tags": ["minecraft", "creeper", "mojang", "sandbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_123",
    "text": "Σε ποιο ισχυρότερο ηλεκτρικό Pokémon εξελίσσεται ο Pikachu όταν εκτεθεί σε μια Πέτρα του Κεραυνού (Thunder Stone);",
    "answers": ["Ράιτσου (Raichu)", "Πίτσου (Pichu)", "Ηλέκτραμπας (Electabuzz)", "Τζόλτεον (Jolteon)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Raichu είναι η τελική εξέλιξη του Pikachu, με μακρύτερη ουρά σε σχήμα κεραυνού και μεγαλύτερη αποθήκευση ηλεκτρικού φορτίου.",
    "funFacts": [
      "Στη σειρά anime, ο Pikachu του Ash αρνήθηκε να αγγίξει την Thunder Stone, θέλοντας να νικήσει τον Raichu του αρχηγού γυμναστηρίου υποστηρίζοντας την αρχική του μορφή.",
      "Στην περιοχή Alola, ο Raichu αποκτά διπλό τύπο (Ηλεκτρικό/Ψυχικό) και αιωρείται πάνω στην πλατιά ουρά του σαν να κάνει σερφ."
    ],
    "source": "https://el.wikipedia.org/wiki/Pikachu",
    "locale": "el-GR",
    "tags": ["pokemon", "raichu", "pikachu", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_124",
    "text": "Ποιο είναι το όνομα της σιωπηλής ηρωίδας με την πορτοκαλί φόρμα δοκιμών που ελέγχουν οι παίκτες στη σειρά παιχνιδιών «Portal»;",
    "answers": ["Alyx Vance", "Chell", "Faith Connors", "Jill Valentine"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Chell είναι το ανθρώπινο υποκείμενο δοκιμών που χρησιμοποιεί τη συσκευή πυλών για να δραπετεύσει από τα εργαστήρια της Aperture Science.",
    "funFacts": [
      "Φοράει ειδικές προηγμένες μπότες στα πόδια της (Long Fall Boots), οι οποίες απορροφούν πλήρως τους κραδασμούς από πτώσεις οποιουδήποτε ύψους.",
      "Το πρόσωπο και η εμφάνιση της Chell βασίστηκαν στο πραγματικό μοντέλο και ηθοποιό Alésia Glidewell."
    ],
    "source": "https://en.wikipedia.org/wiki/Chell_(Portal)",
    "locale": "el-GR",
    "tags": ["portal", "chell", "valve", "puzzle"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_125",
    "text": "Τι είδους πλάσμα είναι ο Bowser, ο αιώνιος αντίπαλος του Mario που κυβερνά τους Koopas και εκπνέει φωτιά;",
    "answers": ["Γιγάντιος βάτραχος", "Δράκος της λάβας", "Γιγάντια χελώνα με αγκάθια (Koopa)", "Κροκόδειλος"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Bowser (γνωστός στην Ιαπωνία ως King Koopa) είναι μια τερατώδης ανθρωπόμορφη χελώνα με αιχμηρό καβούκι και κέρατα.",
    "funFacts": [
      "Ο Shigeru Miyamoto αρχικά εμπνεύστηκε τη μορφή του Bowser από τον King Ox στην κλασική κινεζική ιστορία 'Ταξίδι στη Δύση'.",
      "Στην ταινία κινουμένων σχεδίων 'The Super Mario Bros. Movie' (2023), τη φωνή του Bowser δάνεισε ο Jack Black, ερμηνεύοντας το viral τραγούδι 'Peaches'."
    ],
    "source": "https://el.wikipedia.org/wiki/Bowser",
    "locale": "el-GR",
    "tags": ["bowser", "mario", "nintendo", "koopa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_126",
    "text": "Ποια είναι η πασίγνωστη ιαχή που φωνάζει ο Scorpion όταν εκτοξεύει το δόρυ του για να τραβήξει τον αντίπαλο στο «Mortal Kombat»;",
    "answers": ["Finish Him!", "Fatality!", "Come to Me!", "Get over here!"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Scorpion πετάει το δόρυ με το σκοινί από την παλάμη του φωνάζοντας 'Get over here!' (ή εναλλακτικά 'Come here!') για να ζαλίσει τον αντίπαλο.",
    "funFacts": [
      "Τη φωνή για την ατάκα αυτή δάνεισε ο ίδιος ο συνδημιουργός του Mortal Kombat, Ed Boon, σε όλα τα κλασικά παιχνίδια και ταινίες.",
      "Ο Scorpion είναι στην πραγματικότητα ένα αναστημένο πνεύμα εκδίκησης (specter) που ονομαζόταν Hanzo Hasashi πριν δολοφονηθεί η οικογένειά του."
    ],
    "source": "https://el.wikipedia.org/wiki/Mortal_Kombat",
    "locale": "el-GR",
    "tags": ["mortal-kombat", "scorpion", "fighting", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_127",
    "text": "Ποιο τεράστιο και εμβληματικό σπαθί κρατάει ο Cloud Strife στο θρυλικό JRPG «Final Fantasy VII»;",
    "answers": ["Buster Sword", "Gunblade", "Masamune", "Master Sword"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Buster Sword είναι ένα γιγάντιο πλατύ σπαθί που κληροδότησε στον Cloud ο επιστήθιος φίλος του Zack Fair.",
    "funFacts": [
      "Το σπαθί έχει μήκος περίπου 1,8 μέτρα και διαθέτει δύο χαρακτηριστικές οπές στη βάση της λεπίδας για την τοποθέτηση μαγικών κρυστάλλων (Materia).",
      "Ο αρχικός κάτοχος του σπαθιού ήταν ο στρατιώτης Angeal Hewley, ο οποίος το μεταβίβασε στον Zack Fair πριν φτάσει στον Cloud."
    ],
    "source": "https://en.wikipedia.org/wiki/Cloud_Strife",
    "locale": "el-GR",
    "tags": ["final-fantasy", "cloud-strife", "square-enix", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_128",
    "text": "Ποιο πρωτοποριακό όπλο χειρισμού φυσικής στο «Half-Life 2» επιτρέπει στον Gordon Freeman να σηκώνει και να εκτοξεύει βαριά αντικείμενα;",
    "answers": ["Portal Gun", "Gravity Gun", "Physics Cannon", "Plasma Rifle"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Gravity Gun (επισήμως Zero-Point Energy Field Manipulator) επέτρεψε στους παίκτες να εκμεταλλευτούν πλήρως τη ρεαλιστική μηχανή φυσικής Havok.",
    "funFacts": [
      "Οι παίκτες μπορούσαν να χρησιμοποιήσουν ακόμη και λεπίδες πριονιού ή καλοριφέρ ως φονικά αυτοσχέδια βλήματα εναντίον των εχθρών.",
      "Προς το τέλος του παιχνιδιού, το όπλο υπερφορτίζεται με σκοτεινή ενέργεια, επιτρέποντας στον παίκτη να σηκώνει απευθείας τους ίδιους τους στρατιώτες Combine."
    ],
    "source": "https://el.wikipedia.org/wiki/Half-Life_2",
    "locale": "el-GR",
    "tags": ["half-life", "gravity-gun", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_129",
    "text": "Ποιες είναι οι δύο μεγάλες αντίπαλες παρατάξεις που συγκρούονται διαρκώς στον κόσμο του «World of Warcraft»;",
    "answers": ["Οι Ασπόνδυλοι και οι Άγιοι", "Οι Ναΐτες και οι Ασσασίνοι", "Η Συμμαχία και η Ορδή (Alliance & Horde)", "Οι Σπαρτιάτες και οι Αθηναίοι"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Συμμαχία (Alliance με ηγέτες τους Ανθρώπους) και η Ορδή (Horde με ηγέτες τα Ορκ) αποτελούν τους δύο βασικούς πυλώνες του σύμπαντος του Warcraft.",
    "funFacts": [
      "Η περίφημη πολεμική ιαχή 'For the Horde!' ('Για την Ορδή!') έχει γίνει παγκόσμιο σύνθημα των εκατομμυρίων παικτών της παράταξης.",
      "Για πάνω από 15 χρόνια, παίκτες αντίπαλων παρατάξεων δεν μπορούσαν καν να συνομιλήσουν στο παιχνίδι ή να δημιουργήσουν κοινές ομάδες για dungeons."
    ],
    "source": "https://el.wikipedia.org/wiki/World_of_Warcraft",
    "locale": "el-GR",
    "tags": ["world-of-warcraft", "alliance", "horde", "blizzard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_130",
    "text": "Τι είδους μικρό πλάσμα είναι ο πιστός φίλος Sparx που ακολουθεί τον Spyro the Dragon και δείχνει την κατάσταση της υγείας του;",
    "answers": ["Πυγολαμπίδα", "Μέλισσα", "Πεταλούδα", "Λιβελούλα (Dragonfly)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Sparx είναι μια κίτρινη λιβελούλα που προστατεύει τον Spyro. Όταν ο Spyro δέχεται χτυπήματα, ο Sparx αλλάζει χρώμα από χρυσό σε μπλε, πράσινο και τελικά εξαφανίζεται.",
    "funFacts": [
      "Ο Sparx ανακτά την υγεία του και προστατεύει ξανά τον Spyro όταν τρώει πεταλούδες που εμφανίζονται από μικρά ζώα στις πίστες.",
      "Βοηθά επίσης τον παίκτη ρουφώντας αυτόματα τους πολύτιμους λίθους που βρίσκονται διάσπαρτοι στο έδαφος."
    ],
    "source": "https://el.wikipedia.org/wiki/Spyro",
    "locale": "el-GR",
    "tags": ["spyro", "sparx", "insomniac-games", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_131",
    "text": "Ποια διάσημη 16-bit κονσόλα της Sega κυκλοφόρησε το 1988 και αποτέλεσε τον κυριότερο ανταγωνιστή του Super Nintendo;",
    "answers": ["Sega Mega Drive (Genesis)", "Sega Saturn", "Sega Dreamcast", "Sega Master System"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Mega Drive (που ονομάστηκε Sega Genesis στη Βόρεια Αμερική) καθιέρωσε τη Sega χάρη στην ταχύτητα του επεξεργαστή Motorola 68000 και τα παιχνίδια Sonic.",
    "funFacts": [
      "Η διάσημη διαφημιστική καμπάνια στις ΗΠΑ είχε το επιθετικό σλόγκαν: 'Genesis does what Nintendon't'.",
      "Είναι η πιο επιτυχημένη κονσόλα στην ιστορία της Sega, με πωλήσεις που ξεπέρασαν τα 30 εκατομμύρια μονάδες παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/Sega_Mega_Drive",
    "locale": "el-GR",
    "tags": ["sega", "mega-drive", "genesis", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_132",
    "text": "Ποιο πανίσχυρο ουδέτερο τέρας ζει στον ποταμό του Summoner's Rift στο «League of Legends» και δίνει τεράστιο buff στην ομάδα που θα το εξοντώσει;",
    "answers": ["Dragon", "Baron Nashor", "Rift Herald", "Blue Sentinel"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Baron Nashor είναι το ισχυρότερο ουδέτερο τέρας στο Summoner's Rift, και η εξόντωσή του χαρίζει στην ομάδα αυξημένη δύναμη και ενισχυμένα minions.",
    "funFacts": [
      "Το όνομα 'Nashor' είναι αναγραμματισμός του ονόματος 'Roshan', του αντίστοιχου μυθικού τέρατος από το Dota.",
      "Εμφανίζεται στον χάρτη ακριβώς στο 20ό λεπτό του αγώνα, αντικαθιστώντας το Rift Herald."
    ],
    "source": "https://el.wikipedia.org/wiki/League_of_Legends",
    "locale": "el-GR",
    "tags": ["league-of-legends", "baron-nashor", "moba", "riot-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_133",
    "text": "Ποια Κινέζα αξιωματικός της Interpol με τα αστραπιαία λακτίσματα θεωρείται η ιστορική «πρώτη κυρία» των fighting games στο «Street Fighter»;",
    "answers": ["Cammy", "Juri", "Chun-Li", "Sakura"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Chun-Li πρωτοεμφανίστηκε στο Street Fighter II (1991) και ήταν η πρώτη playable γυναίκα μαχήτρια σε mainstream fighting game.",
    "funFacts": [
      "Η διάσημη ειδική της επίθεση ονομάζεται 'Hyakuretsukyaku' (Lightning Legs), κατά την οποία εκτελεί δεκάδες αστραπιαίες κλωτσιές σε ελάχιστα δευτερόλεπτα.",
      "Το κίνητρό της στις μάχες είναι να εκδικηθεί τον αρχηγό της Shadaloo, M. Bison, για τον θάνατο του πατέρα της."
    ],
    "source": "https://el.wikipedia.org/wiki/Chun-Li",
    "locale": "el-GR",
    "tags": ["street-fighter", "chun-li", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_134",
    "text": "Σε ποια πρωτοποριακή κονσόλα της Nintendo κυκλοφόρησε το «Super Mario 64» το 1996, θέτοντας τα θεμέλια για τα τρισδιάστατα παιχνίδια;",
    "answers": ["Super Nintendo", "Nintendo GameCube", "Virtual Boy", "Nintendo 64"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Nintendo 64 εισήγαγε τον αναλογικό μοχλό (thumbstick) στο χειριστήριο, ο οποίος επέτρεψε τον ομαλό έλεγχο κίνησης του Mario σε 360 μοίρες.",
    "funFacts": [
      "Το Super Mario 64 όρισε τον τρόπο λειτουργίας της κινούμενης τρισδιάστατης κάμερας τρίτου προσώπου για όλη τη μετέπειτα βιομηχανία.",
      "Ο Mario μπορούσε για πρώτη φορά να εκτελεί τριπλά άλματα, τούμπες προς τα πίσω και άλματα από τοίχο σε τοίχο (wall jumps)."
    ],
    "source": "https://el.wikipedia.org/wiki/Super_Mario_64",
    "locale": "el-GR",
    "tags": ["mario-64", "nintendo-64", "nintendo", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_135",
    "text": "Ποιος απρόβλεπτος, εκρηκτικός και βίαιος πρώην στρατιωτικός πιλότος είναι ένας από τους τρεις πρωταγωνιστές του «Grand Theft Auto V»;",
    "answers": ["Trevor Philips", "Michael De Santa", "Franklin Clinton", "Lester Crest"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Trevor Philips ζει σε ένα τροχόσπιτο στην έρημο του Sandy Shores και διατηρεί τη δική του επιχείρηση διακίνησης όπλων ('Trevor Philips Enterprises').",
    "funFacts": [
      "Τη φωνή και το motion capture του Trevor ανέλαβε ο Καναδός ηθοποιός Steven Ogg, ο οποίος έδωσε μια αξιομνημόνευτη ερμηνεία.",
      "Η ειδική ικανότητα του Trevor στο παιχνίδι είναι η 'Κατάσταση Μανίας' (Rage Mode), η οποία διπλασιάζει τη ζημιά που προκαλεί και μειώνει σχεδόν στο μηδέν τη ζημιά που δέχεται."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto_V",
    "locale": "el-GR",
    "tags": ["gta-v", "trevor", "rockstar-games", "open-world"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_136",
    "text": "Ποιοι είναι οι τεράστιοι γενετικά μεταλλαγμένοι φρουροί με βαριές καταδυτικές στολές και τρυπάνια που προστατεύουν τις Little Sisters στο «BioShock»;",
    "answers": ["Splicers", "Big Daddies", "Handymen", "Songbirds"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι Big Daddies είναι βαριά οπλισμένοι σωματοφύλακες συνδεδεμένοι ψυχολογικά με τις Little Sisters, τις οποίες προστατεύουν μέχρι θανάτου.",
    "funFacts": [
      "Οι Little Sisters τους αποκαλούν χαϊδευτικά 'Mr. Bubbles' εξαιτίας του ήχου των φυσαλίδων από το σκάφανδρο της στολής τους.",
      "Η μορφή του Big Daddy με το τεράστιο τρυπάνι στο χέρι έγινε το κυρίαρχο αναγνωρίσιμο σύμβολο στο εξώφυλλο και την προώθηση του BioShock."
    ],
    "source": "https://el.wikipedia.org/wiki/BioShock",
    "locale": "el-GR",
    "tags": ["bioshock", "big-daddy", "rapture", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_137",
    "text": "Ποια ευφυής τεχνητή νοημοσύνη με μπλε ολογραφική γυναικεία μορφή συνοδεύει και καθοδηγεί τον Master Chief στη σειρά «Halo»;",
    "answers": ["GLaDOS", "SHODAN", "Cortana", "The Weapon"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Cortana δημιουργήθηκε από κλωνοποιημένο εγκεφαλικό ιστό της Dr. Catherine Halsey και αποτελεί τον στενότερο σύντροφο του Master Chief.",
    "funFacts": [
      "Η Microsoft ονόμασε την πραγματική ψηφιακή φωνητική βοηθό των Windows 'Cortana' απευθείας προς τιμήν της ηρωίδας του Halo.",
      "Τη φωνή της Cortana χάρισε η ηθοποιός Jen Taylor, τόσο στα βιντεοπαιχνίδια όσο και στην ψηφιακή βοηθό της Microsoft."
    ],
    "source": "https://en.wikipedia.org/wiki/Cortana_(Halo)",
    "locale": "el-GR",
    "tags": ["halo", "cortana", "master-chief", "xbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_138",
    "text": "Τι είδους γενετικά τροποποιημένο ζώο είναι ο ιδιοφυής επιστήμονας Winston στο hero shooter «Overwatch»;",
    "answers": ["Χιμπατζής", "Αρκούδα", "Πάντα", "Γορίλας"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Winston είναι ένας εξαιρετικά ευφυής γορίλας που μεγάλωσε στη σεληνιακή αποικία Horizon Lunar Colony και πολεμά με κανόνι ηλεκτρικών εκκενώσεων (Tesla Cannon).",
    "funFacts": [
      "Πήρε το όνομά του προς τιμήν του ανθρώπου μέντορά του στη Σελήνη, του επιστήμονα Dr. Harold Winston.",
      "Έχει τεράστια αδυναμία στο φυστικοβούτυρο (peanut butter), το οποίο αναζητά διαρκώς στα επίσημα animated shorts του παιχνιδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/Overwatch",
    "locale": "el-GR",
    "tags": ["overwatch", "winston", "blizzard", "hero-shooter"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_139",
    "text": "Ποιο χαρακτηριστικό πράσινο διαμάντι αιωρείται πάνω από το κεφάλι του ενεργού χαρακτήρα στη σειρά «The Sims»;",
    "answers": ["Plumbob", "SimDiamond", "MoodGem", "LifeCrystal"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Plumbob είναι το πράσινο οκτάεδρο διαμάντι που δείχνει ποιος Sim ελέγχεται εκείνη τη στιγμή, ενώ αλλάζει χρώμα ανάλογα με τη διάθεσή του.",
    "funFacts": [
      "Ο όρος 'plumbob' προέρχεται από το πραγματικό οικοδομικό εργαλείο νήμα της στάθμης (βαρίδι), που χρησιμοποιείται για την εύρεση της κατακόρυφης ευθείας.",
      "Όταν οι ανάγκες του Sim βρίσκονται σε κρίσιμο σημείο, το Plumbob γίνεται σκούρο κόκκινο."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Sims",
    "locale": "el-GR",
    "tags": ["the-sims", "plumbob", "ea", "simulation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_140",
    "text": "Ποιο παράξενο όχημα μεταφέρει τους 100 παίκτες ψηλά πάνω από το νησί στην αρχή κάθε αγώνα στο «Fortnite»;",
    "answers": ["Στρατιωτικό αεροπλάνο", "Ιπτάμενο σχολικό λεωφορείο (Battle Bus)", "Διαστημική κάψουλα", "Ελικόπτερο"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Battle Bus είναι ένα μπλε αμερικανικό σχολικό λεωφορείο συνδεδεμένο με ένα τεράστιο αερόστατο θερμού αέρα, από το οποίο πηδούν οι παίκτες με ανεμόπτερα.",
    "funFacts": [
      "Οι παίκτες έχουν τη δυνατότητα να πατήσουν ένα κουμπί για να ευχαριστήσουν τον οδηγό του λεωφορείου ('Thank the bus driver') πριν πηδήξουν.",
      "Σε διάφορες εορταστικές περιόδους και συνεργασίες, το Battle Bus αλλάζει εμφάνιση και μουσική (π.χ. θεματικό για το Halloween ή τη Marvel)."
    ],
    "source": "https://el.wikipedia.org/wiki/Fortnite",
    "locale": "el-GR",
    "tags": ["fortnite", "battle-bus", "epic-games", "battle-royale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_141",
    "text": "Σε ποιο σημείο του σώματος είναι προσαρμοσμένη η χαρακτηριστική κρυφή λεπίδα (hidden blade) των Ασσασίνων στο «Assassin's Creed»;",
    "answers": ["Στη σόλα της μπότας", "Στη ζώνη της μέσης", "Στον καρπό / πήχη του χεριού", "Στον ώμο"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η κρυφή λεπίδα εκτείνεται με έναν μηχανισμό ελατηρίου από τον καρπό κάτω από το μανίκι, επιτρέποντας αστραπιαίες και αθόρυβες δολοφονίες.",
    "funFacts": [
      "Στα πρώιμα χρόνια της Αδελφότητας (όπως στην εποχή του Altaïr), οι Ασσασίνοι ακρωτηρίαζαν τον παράμεσο δάχτυλο ώστε να μπορεί να εκτείνεται η λεπίδα χωρίς εμπόδιο.",
      "Ο Λεονάρντο ντα Βίντσι τροποποίησε τον μηχανισμό στο Assassin's Creed II ώστε ο Ezio να μπορεί να χρησιμοποιεί τη λεπίδα χωρίς να χρειάζεται να κόψει το δάχτυλό του."
    ],
    "source": "https://el.wikipedia.org/wiki/Assassin%27s_Creed",
    "locale": "el-GR",
    "tags": ["assassins-creed", "hidden-blade", "ubisoft", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_142",
    "text": "Ποιος πρώην παράνομος της συμμορίας Van der Linde με τις χαρακτηριστικές ουλές στο πρόσωπο είναι ο πρωταγωνιστής του πρώτου «Red Dead Redemption» (2010);",
    "answers": ["Arthur Morgan", "Dutch van der Linde", "Bill Williamson", "John Marston"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο John Marston αναγκάζεται από κυβερνητικούς πράκτορες που κρατούν όμηρο την οικογένειά του να κυνηγήσει και να εξοντώσει τα παλιά μέλη της συμμορίας του.",
    "funFacts": [
      "Τη φωνή και το motion capture του John Marston χάρισε ο Rob Wiethoff, ο οποίος επιλέχθηκε ανάμεσα σε εκατοντάδες ηθοποιούς για τη φυσική τραχιά φωνή του.",
      "Στο Red Dead Redemption 2, ο παίκτης μαθαίνει πώς ο Marston απέκτησε τις διάσημες ουλές στο πρόσωπό του μετά από επίθεση λύκων στα χιονισμένα βουνά."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "john-marston", "rockstar-games", "western"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_143",
    "text": "Ποιο μαγικό φιαλίδιο με χρυσαφένιο υγρό πίνουν οι παίκτες για να αποκαταστήσουν την υγεία τους στη σειρά «Dark Souls»;",
    "answers": ["Estus Flask", "Crimson Tear", "Blood Vial", "Elixir of Life"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Estus Flask γεμίζει ξανά αυτόματα κάθε φορά που ο παίκτης αναπαύεται σε μια Πυρά (Bonfire) και αποτελεί το βασικότερο μέσο επιβίωσης.",
    "funFacts": [
      "Η λατινική λέξη 'aestus' σχετίζεται με τη θερμότητα και τη φωτιά, παραπέμποντας στη σύνδεση του φιαλιδίου με τις φλόγες των bonfires.",
      "Οι παίκτες μπορούν να αυξήσουν τη χωρητικότητα και τη δύναμη επούλωσης του φιαλιδίου προσφέροντας Estus Shards και Sublime Bone Dust."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "estus-flask", "fromsoftware", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_144",
    "text": "Ποιος είναι ο πιστός αδελφός του Cuphead με το μπλε χρώμα και τη μεγάλη μύτη, ο οποίος ελέγχεται από τον δεύτερο παίκτη στο «Cuphead»;",
    "answers": ["Teacup", "Mugman", "Chalice", "Bowlboy"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Mugman είναι ο αδελφός του Cuphead, διακρινόμενος για το μπλε παντελονάκι, τη μεγαλύτερη γαλάζια μύτη και το πιο προσεκτικό του ταμπεραμέντο.",
    "funFacts": [
      "Ενώ ο Cuphead είναι παρορμητικός και οδήγησε τα δύο αδέλφια στη συμφωνία με τον Διάβολο, ο Mugman προσπαθούσε εξαρχής να τον αποτρέψει.",
      "Στη σειρά κινουμένων σχεδίων 'The Cuphead Show!' στο Netflix, ο Mugman αποτελεί ισότιμο συμπρωταγωνιστή με εξαιρετικά κωμικές σκηνές."
    ],
    "source": "https://el.wikipedia.org/wiki/Cuphead",
    "locale": "el-GR",
    "tags": ["cuphead", "mugman", "indie", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_145",
    "text": "Ποιο μικρό γαλάζιο χελωνάκι νερού είναι το τρίτο κλασικό αρχικό Pokémon της πρώτης γενιάς στην περιοχή Kanto;",
    "answers": ["Τότοπαϊλ (Totodile)", "Μάντκιπ (Mudkip)", "Σκουίρτλ (Squirtle)", "Πίπλαπ (Piplup)"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Squirtle είναι το αρχικό Pokémon τύπου νερού του Kanto, το οποίο εξελίσσεται στον Wartortle και τελικά στον πανίσχυρο Blastoise με τα κανόνια νερού.",
    "funFacts": [
      "Στο anime, μια συμμορία από εγκαταλελειμμένους Squirtle με μαύρα μυτερά γυαλιά ηλίου ονομαζόταν 'Squirtle Squad'.",
      "Το όνομά του αποτελεί συνδυασμό των αγγλικών λέξεων 'squirt' (εκτοξεύω νερό) και 'turtle' (χελώνα)."
    ],
    "source": "https://el.wikipedia.org/wiki/Squirtle",
    "locale": "el-GR",
    "tags": ["pokemon", "squirtle", "nintendo", "kanto"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_146",
    "text": "Ποιος κοντός τρελός επιστήμονας με κίτρινο δέρμα και ένα μεγάλο γράμμα «N» χαραγμένο στο μέτωπο είναι ο αρχι-εχθρός του Crash Bandicoot;",
    "answers": ["Dr. N. Tropy", "Dr. N. Brio", "Dr. N. Gin", "Dr. Neo Cortex"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Dr. Neo Cortex είναι ο σατανικός γενετιστής που δημιούργησε κατά λάθος τον Crash Bandicoot με την ακτίνα Evolvo-Ray, προτού ο Crash επαναστατήσει εναντίον του.",
    "funFacts": [
      "Τη χαρακτηριστική φωνή του Cortex στη σειρά παιχνιδιών δάνεισε για πολλά χρόνια ο ηθοποιός Clancy Brown.",
      "Το όνομά του είναι ένα λογοπαίγνιο με τον νεοφλοιό του ανθρώπινου εγκεφάλου (neocortex)."
    ],
    "source": "https://en.wikipedia.org/wiki/Doctor_Neo_Cortex",
    "locale": "el-GR",
    "tags": ["crash-bandicoot", "cortex", "naughty-dog", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_147",
    "text": "Ποιο είναι το επίσημο νόμισμα που χρησιμοποιούν οι παίκτες για αγορές, συναλλαγές και αποπληρωμή δανείων στη σειρά «Animal Crossing»;",
    "answers": ["Bells", "Pokédollars", "Rupees", "Gils"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Bells αποτελούν το νόμισμα του Animal Crossing, το οποίο οι παίκτες κερδίζουν πουλώντας ψάρια, έντομα, φρούτα και απολιθώματα.",
    "funFacts": [
      "Οι παίκτες μπορούν να φυτέψουν ένα σακίδιο με Bells σε μια λαμπερή τρύπα στο χώμα για να φυτρώσει ένα μαγικό 'δέντρο χρημάτων' (Money Tree).",
      "Το μεγαλύτερο μέρος των Bells πηγαίνει συνήθως στην αποπληρωμή των διαδοχικών στεγαστικών δανείων του Tom Nook για την επέκταση του σπιτιού."
    ],
    "source": "https://el.wikipedia.org/wiki/Animal_Crossing",
    "locale": "el-GR",
    "tags": ["animal-crossing", "bells", "nintendo", "simulation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_148",
    "text": "Ποιος σοφός γέροντας του τάγματος των Horadrim υποδέχεται τους ήρωες στη σειρά «Diablo» με την ατάκα «Stay awhile and listen!»;",
    "answers": ["Tyrael", "Deckard Cain", "Marius", "Wirt"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Deckard Cain είναι ο τελευταίος επιζών των Horadrim, ο οποίος προσφέρει γνώσεις μυθολογίας και ταυτοποιεί δωρεάν τα μαγικά αντικείμενα των παικτών.",
    "funFacts": [
      "Πήρε το όνομά του από ένα πραγματικό παιδί, τον Deckard Cain Elder, του οποίου ο πατέρας κέρδισε διαγωνισμό ονοματοδοσίας της Blizzard το 1996.",
      "Η φράση του 'Stay awhile and listen!' ('Κάτσε για λίγο και άκου!') έγινε ένα από τα πιο αναγνωρίσιμα ακουστικά σήματα της Blizzard."
    ],
    "source": "https://en.wikipedia.org/wiki/Deckard_Cain",
    "locale": "el-GR",
    "tags": ["diablo", "deckard-cain", "blizzard", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_149",
    "text": "Ποιος μυστηριώδης άνδρας με κοστούμι και χαρτοφύλακα παρακολουθεί από μακριά τον Gordon Freeman σε όλη τη σειρά «Half-Life»;",
    "answers": ["Barney Calhoun", "Eli Vance", "G-Man", "Dr. Breen"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο G-Man είναι μια αινιγματική οντότητα με υπερφυσικές δυνάμεις χειραγώγησης του χρόνου και του χώρου, που ενεργεί εκ μέρους άγνωστων 'εργοδοτών'.",
    "funFacts": [
      "Μιλάει με μια παράξενη, διακοπτόμενη και ανατριχιαστική χροιά φωνής, την οποία ερμηνεύει ο ηθοποιός Michael Shapiro.",
      "Στο τέλος του πρώτου Half-Life (1998), ο G-Man θέτει τον Gordon Freeman σε κατάσταση στασιμότητας για σχεδόν είκοσι χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/Half-Life",
    "locale": "el-GR",
    "tags": ["half-life", "g-man", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_150",
    "text": "Ποιο είναι το όνομα της προηγμένης διαστημικής φρεγάτας stealth που κυβερνά ο Commander Shepard στη σειρά «Mass Effect»;",
    "answers": ["Pillar of Autumn", "Hyperion", "Ebon Hawk", "SSV Normandy"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το SSV Normandy (και αργότερα Normandy SR-2) είναι ένα πρωτοποριακό σκάφος κοινής ανθρώπινης και τουριανής τεχνολογίας με συστήματα απόκρυψης εκπομπών θερμότητας.",
    "funFacts": [
      "Πήρε το όνομά του προς τιμήν της ιστορικής απόβασης στη Νορμανδία κατά τον Β΄ Παγκόσμιο Πόλεμο.",
      "Ο πιλότος του διαστημοπλοίου, ο Jeff 'Joker' Moreau, πάσχει από ατελή οστεογένεση (νόσο των γυάλινων οστών) αλλά θεωρείται ο καλύτερος πιλότος του στόλου."
    ],
    "source": "https://el.wikipedia.org/wiki/Mass_Effect_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["mass-effect", "normandy", "bioware", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_151",
    "text": "Ποια χαριτωμένα μικρά σφαιρικά πνεύματα του δάσους σε σχήμα μήλου βοηθούν τον παίκτη να επισκευάσει το Κοινοτικό Κέντρο στο «Stardew Valley»;",
    "answers": ["Junimos", "Koroks", "Moogles", "Lumas"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Junimos είναι μαγικά πλάσματα που ζουν στο εγκαταλελειμμένο Κοινοτικό Κέντρο (Community Center) και ανταμείβουν τον παίκτη όταν ολοκληρώνει δέσμες υλικών (bundles).",
    "funFacts": [
      "Εάν ο παίκτης χτίσει μια καλύβα Junimo Hut στη φάρμα του, τα μικρά πλάσματα θα μαζεύουν αυτόματα τις ώριμες σοδειές καθημερινά.",
      "Μιλούν μια μυστηριώδη γλώσσα συμβόλων την οποία ο παίκτης κατανοεί μόνο αφού πιει το μαγικό φίλτρο του Μάγου του δάσους."
    ],
    "source": "https://el.wikipedia.org/wiki/Stardew_Valley",
    "locale": "el-GR",
    "tags": ["stardew-valley", "junimos", "indie", "farming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_152",
    "text": "Ποιος πανίσχυρος θεός της αστραπής με το σφυρί Mjölnir συγκρούεται με τον Κράτο στο «God of War Ragnarök» (2022);",
    "answers": ["Όντιν", "Θορ (Thor)", "Χέιμνταλ", "Τυρ"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Thor είναι ο πρωτότοκος γιος του Όντιν και ο πιο επικίνδυνος πολεμιστής του Asgard, αναζητώντας εκδίκηση από τον Κράτο για τον θάνατο των γιων του.",
    "funFacts": [
      "Η εμφάνιση του Thor στο παιχνίδι σχεδιάστηκε πιστά στη σκανδιναβική μυθολογία, παρουσιάζοντάς τον ως μεγαλόσωμο, κοκκινομάλλη και μυώδη πολεμιστή.",
      "Τη φωνή και το motion capture του Thor ανέλαβε ο Αμερικανός ηθοποιός Ryan Hurst, γνωστός από τη σειρά 'Sons of Anarchy'."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_Ragnar%C3%B6k",
    "locale": "el-GR",
    "tags": ["god-of-war", "thor", "kratos", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_153",
    "text": "Ποιο είναι το πιο αναγνωρίσιμο και δημοφιλές αγωνιστικό αυτοκίνητο στο «Rocket League», που προτιμάται σταθερά από επαγγελματίες παίκτες;",
    "answers": ["Dominus", "Breakout", "Octane", "Fennec"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Octane είναι το προεπιλεγμένο αυτοκίνητο του παιχνιδιού και παραμένει το πιο αγαπητό όχημα χάρη στο ισορροπημένο hitbox και την ευελιξία του.",
    "funFacts": [
      "Το Octane πρωτοεμφανίστηκε στον πρόγονο του τίτλου, το 'Supersonic Acrobatic Rocket-Powered Battle-Cars' το 2008.",
      "Υπάρχει ακόμα και ως πραγματικό τηλεκατευθυνόμενο όχημα αλλά και ως ειδικό crossover αντικείμενο στο Fortnite."
    ],
    "source": "https://el.wikipedia.org/wiki/Rocket_League",
    "locale": "el-GR",
    "tags": ["rocket-league", "octane", "esports", "cars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_154",
    "text": "Σε ποιο ιστορικό παιχνίδι της σειράς Call of Duty (2008 από την Treyarch) εισήχθη για πρώτη φορά το δημοφιλές mode επιβίωσης «Zombies»;",
    "answers": ["Call of Duty 4: Modern Warfare", "Call of Duty: Black Ops", "Call of Duty 2", "Call of Duty: World at War"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το αρχικό 'Nacht der Untoten' εμφανίστηκε ως μυστικό bonus minigame μετά τους τίτλους τέλους του Call of Duty: World at War.",
    "funFacts": [
      "Το mode δημιουργήθηκε στον ελεύθερο χρόνο των προγραμματιστών της Treyarch για πλάκα, χωρίς επίσημη έγκριση από τη διοίκηση της εταιρείας.",
      "Η τεράστια επιτυχία του οδήγησε στο να γίνει αναπόσπαστο κομμάτι σχεδόν κάθε επόμενου τίτλου Call of Duty της Treyarch."
    ],
    "source": "https://el.wikipedia.org/wiki/Call_of_Duty:_World_at_War",
    "locale": "el-GR",
    "tags": ["call-of-duty", "zombies", "treyarch", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_155",
    "text": "Ποια είναι η πιο διάσημη τρισύλλαβη δρακο-ιαχή (Dragon Shout) του Dragonborn στο «Skyrim» που εκτοξεύει τους εχθρούς μακριά;",
    "answers": ["Fus Ro Dah", "Yol Toor Shul", "Wuld Nah Kest", "Lok Vah Koor"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η κραυγή 'Fus Ro Dah' (Unrelenting Force / Αμείλικτη Δύναμη) αποτελείται από τις λέξεις της δρακογλώσσας για τη Δύναμη, την Ισορροπία και την Ώθηση.",
    "funFacts": [
      "Η κραυγή αυτή έγινε ένα από τα πιο διάσημα internet memes της δεκαετίας του 2010, με εκατοντάδες βίντεο παρωδίας.",
      "Η πλήρης γλώσσα των δρακόμορφων (Dovahzul) σχεδιάστηκε από τη Bethesda με ειδικό ρούνικο αλφάβητο εμπνευσμένο από τη σφηνοειδή γραφή."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "locale": "el-GR",
    "tags": ["skyrim", "fus-ro-dah", "bethesda", "elder-scrolls"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_156",
    "text": "Ποια δυναμική δημοσιογράφος συνοδεύει τον Nathan Drake στις αποστολές του και αργότερα γίνεται σύζυγός του στη σειρά «Uncharted»;",
    "answers": ["Chloe Frazer", "Elena Fisher", "Nadine Ross", "Marissa Chase"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Elena Fisher πρωτοεμφανίζεται στο Uncharted: Drake's Fortune (2007) ως τηλεοπτική ρεπόρτερ που χρηματοδοτεί την αποστολή του Drake.",
    "funFacts": [
      "Τη φωνή και το motion capture της Elena ανέλαβε η ηθοποιός Emily Rose σε όλα τα κεφάλαια της σειράς.",
      "Στο Uncharted 4: A Thief's End (2016), ο Nathan και η Elena ζουν μαζί και έχουν αποκτήσει μια κόρη, την Cassie."
    ],
    "source": "https://en.wikipedia.org/wiki/Elena_Fisher",
    "locale": "el-GR",
    "tags": ["uncharted", "elena-fisher", "naughty-dog", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_157",
    "text": "Ποιος θρυλικός βρικόλακας άρχοντας του σκότους ανασταίνεται περιοδικά και αποτελεί τον τελικό αντίπαλο στη σειρά «Castlevania»;",
    "answers": ["Lord Carmilla", "Death (Χάρος)", "Κόμης Δράκουλας (Dracula)", "Alucard"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Dracula (παλαιότερα γνωστός ως Mathias Cronqvist) ανασταίνεται συνήθως κάθε 100 χρόνια για να επιβάλει το σκότος στην ανθρωπότητα.",
    "funFacts": [
      "Ο ίδιος ο γιος του, ο μισός-βρικόλακας Alucard (το όνομα Dracula γραμμένο ανάποδα), επαναστατεί εναντίον του πατέρα του για να προστατεύσει τους ανθρώπους.",
      "Το κάστρο του Δράκουλα (Castlevania) είναι ένα ζωντανό πλάσμα του χάους που αλλάζει διαρκώς εσωτερική διαρρύθμιση σε κάθε αναγέννηση."
    ],
    "source": "https://el.wikipedia.org/wiki/Castlevania",
    "locale": "el-GR",
    "tags": ["castlevania", "dracula", "konami", "vampires"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_158",
    "text": "Ποιο φαινομενικά αστείο καθημερινό αντικείμενο συσκευασίας χρησιμοποιεί ο Solid Snake ως το απόλυτο καμουφλάζ απόκρυψης στο «Metal Gear Solid»;",
    "answers": ["Κουβάς σκουπιδιών", "Βαρέλι πετρελαίου", "Ψεύτικος θάμνος", "Χαρτόκουτο (Cardboard Box)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το απλό χαρτόκουτο είναι ένα από τα πιο διάσημα χαρακτηριστικά της σειράς stealth του Hideo Kojima, επιτρέποντας στον Snake να μετακινείται απαρατήρητος.",
    "funFacts": [
      "Ο Snake περιγράφει συχνά στο ασύρματο codec το χαρτόκουτο με βαθύ φιλοσοφικό θαυμασμό ως το 'τέλειο καταφύγιο γαλήνης και ασφάλειας'.",
      "Στο Metal Gear Solid V, οι παίκτες μπορούν να κολλήσουν αφίσες στο κουτί ή να γλιστρήσουν με αυτό σαν έλκηθρο στις πλαγιές."
    ],
    "source": "https://el.wikipedia.org/wiki/Metal_Gear_Solid",
    "locale": "el-GR",
    "tags": ["metal-gear", "solid-snake", "cardboard-box", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_159",
    "text": "Ποια κλάση στο «Team Fortress 2» διαθέτει συσκευή αορατότητας, μεταμφιέζεται σε εχθρούς και εξοντώνει άμεσα με μαχαιριά στην πλάτη (backstab);",
    "answers": ["Spy", "Sniper", "Scout", "Demoman"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Spy είναι ο Γάλλος μυστικός πράκτορας του Team Fortress 2, ικανός να σαμποτάρει τα κτίσματα του Engineer με ηλεκτρονικούς σαμποτέρ (Sapppers).",
    "funFacts": [
      "Η διάσημη ταινία κινουμένων σχεδίων της Valve 'Meet the Spy' έχει ξεπεράσει τα 45 εκατομμύρια προβολές στο YouTube.",
      "Το ρολόι 'Dead Ringer' του Spy του επιτρέπει να σκηνοθετεί τον θάνατό του αφήνοντας πίσω ένα ψεύτικο πτώμα, ενώ γίνεται προσωρινά αόρατος."
    ],
    "source": "https://el.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "spy", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_160",
    "text": "Ποια είναι η προσωπική ηλεκτρονική συσκευή καρπού που φορά ο παίκτης στη σειρά «Fallout» για να διαχειρίζεται τα στατιστικά και τον χάρτη;",
    "answers": ["Game Boy", "Pip-Boy", "GizmoWatch", "VaultWatch"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Pip-Boy (Personal Information Processor) κατασκευάστηκε από τη Vault-Tec και αποτελεί το πλήρες in-game μενού διαχείρισης εξοπλισμού και υγείας.",
    "funFacts": [
      "Στην ειδική συλλεκτική έκδοση του Fallout 4 περιλαμβανόταν ένα πραγματικό αντίγραφο Pip-Boy στο οποίο ο παίκτης μπορούσε να τοποθετήσει το smartphone του.",
      "Διαθέτει επίσης ενσωματωμένο μετρητή ραδιενέργειας Geiger και δέκτη ραδιοφωνικών σταθμών της ερημιάς."
    ],
    "source": "https://en.wikipedia.org/wiki/Pip-Boy",
    "locale": "el-GR",
    "tags": ["fallout", "pip-boy", "bethesda", "post-apocalyptic"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'easy', 1, questions)

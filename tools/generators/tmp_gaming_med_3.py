# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_med_111",
    "text": "Πόσες ημέρες έχει στη διάθεσή του ο Link για να σώσει τον κόσμο της Termina πριν συντριβεί η Σελήνη στο «The Legend of Zelda: Majora's Mask» (2000);",
    "answers": ["Τρεις ημέρες (72 ώρες)", "Επτά ημέρες", "Μία ημέρα (24 ώρες)", "Πέντε ημέρες"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Link χρησιμοποιεί την Οκαρίνα του Χρόνου και το 'Song of Time' για να επαναφέρει τον κύκλο των 72 ωρών ξανά και ξανά στην αρχή της πρώτης ημέρας.",
    "funFacts": [
      "Το παιχνίδι ολοκληρώθηκε σε μόλις έναν χρόνο ανάπτυξης επειδή ο Eiji Aonuma δέχτηκε την πρόκληση του Shigeru Miyamoto επαναχρησιμοποιώντας τη μηχανή και τα μοντέλα του Ocarina of Time.",
      "Το Majora's Mask διαθέτει 24 διαφορετικές μάσκες, καθεμία από τις οποίες προσφέρει ειδικές δυνάμεις ή μεταμορφώνει τον Link σε Deku, Goron ή Zora."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Legend_of_Zelda:_Majora%27s_Mask",
    "locale": "el-GR",
    "tags": ["zelda", "majoras-mask", "nintendo-64", "eiji-aonuma"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_112",
    "text": "Ποιος ιδιοφυής επιστήμονας Salarian βοήθησε στην τροποποίηση του Genophage και τραγουδά αποσπάσματα από οπερέτες στο «Mass Effect 2»;",
    "answers": ["Captain Kirrahe", "Mordin Solus", "Padok Wiks", "Jondum Bau"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Dr. Mordin Solus είναι πρώην πράκτορας των ειδικών δυνάμεων STG και διακρίνεται για τον αστραπιαίο τρόπο ομιλίας του και το φιλοσοφικό του δίλημμα γύρω από τη στείρωση των Krogan.",
    "funFacts": [
      "Η διάσημη σκηνή όπου τραγουδά μια τροποποιημένη εκδοχή του 'Major-General's Song' των Gilbert και Sullivan αποτελεί μία από τις πιο αγαπημένες στιγμές της σειράς.",
      "Η θυσία του στο Mass Effect 3 συνοδεύεται από την ιστορική ατάκα του: 'Had to be me. Someone else might have gotten it wrong'."
    ],
    "source": "https://en.wikipedia.org/wiki/Mordin_Solus",
    "locale": "el-GR",
    "tags": ["mass-effect", "mordin-solus", "salarian", "bioware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_113",
    "text": "Ποιος τραγικός βασιλιάς του Drangleic εξαπατήθηκε από τη βασίλισσα Nashandra και κατέληξε περιπλανώμενο κούφιο πλάσμα (Hollow) στο «Dark Souls II»;",
    "answers": ["King Allant", "Lord Gwyn", "King Vendrick", "Oceiros"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Vendrick πολέμησε τους Γίγαντες υπό την καθοδήγηση της Nashandra, αλλά όταν συνειδητοποίησε ότι ήταν κομμάτι του Manus, κλειδώθηκε στην Undead Crypt για να προστατεύσει το βασίλειο.",
    "funFacts": [
      "Όταν ο παίκτης φτάνει στον Vendrick στην Undead Crypt, τον βρίσκει να περπατά άσκοπα σε κύκλους γυμνός, σέρνοντας το τεράστιο σπαθί του χωρίς να επιτίθεται.",
      "Η άμυνά του μειώνεται δραστικά μόνο εάν ο παίκτης συγκεντρώσει τις πέντε Ψυχές των Γιγάντων (Giant Souls) στο inventory του."
    ],
    "source": "https://en.wikipedia.org/wiki/Dark_Souls_II",
    "locale": "el-GR",
    "tags": ["dark-souls-2", "vendrick", "fromsoftware", "soulslike"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_114",
    "text": "Ποιος οξύθυμος βαρόνος ναρκωτικών της Vice City ζούσε στην πολυτελή έπαυλη Starfish Island προτού ανατραπεί από τον Tommy Vercetti;",
    "answers": ["Sonny Forelli", "Lance Vance", "Colonel Cortez", "Ricardo Diaz"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Ricardo Diaz ήταν ο πιο ισχυρός έμπορος ναρκωτικών στη Vice City. Μετά τη δολοφονία του, η έπαυλή του γίνεται το αρχηγείο της αυτοκρατορίας του Vercetti (Vercetti Estate).",
    "funFacts": [
      "Η έπαυλη του Diaz σχεδιάστηκε με άμεση έμπνευση από την έπαυλη του Tony Montana στην ταινία 'Scarface' του 1983.",
      "Ο Diaz είναι διάσημος για τις εκρήξεις οργής του, πυροβολώντας βιντεοκασέτες και περιστέρια όταν εκνευριζόταν."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City",
    "locale": "el-GR",
    "tags": ["gta", "vice-city", "ricardo-diaz", "rockstar-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_115",
    "text": "Ποιος γενετικά στοχευμένος τεχνητός ιός σχεδιάστηκε για να προκαλεί καρδιακή ανακοπή σε συγκεκριμένα άτομα βάσει DNA στο «Metal Gear Solid»;",
    "answers": ["FOXDIE", "T-Virus", "Cordyceps", "Phazon"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο ιός FOXDIE εγχύθηκε κρυφά στον Solid Snake από την Dr. Naomi Hunter, λειτουργώντας ως βιολογικό όπλο για την εξόντωση των ανταρτών του Shadow Moses.",
    "funFacts": [
      "Ο ιός ενεργοποιείται αναγνωρίζοντας συγκεκριμένες αλληλουχίες DNA και προκαλεί άμεση καρδιακή προσβολή μέσα σε λίγα λεπτά.",
      "Ο Liquid Snake πεθαίνει ξαφνικά από τον FOXDIE στο φινάλε του παιχνιδιού, ακριβώς τη στιγμή που ήταν έτοιμος να σκοτώσει τον Snake."
    ],
    "source": "https://el.wikipedia.org/wiki/Metal_Gear_Solid",
    "locale": "el-GR",
    "tags": ["metal-gear", "foxdie", "solid-snake", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_116",
    "text": "Ποιο επικίνδυνο αντικείμενο βρίσκεται στο κέντρο της πόλης Megaton στο «Fallout 3», το οποίο ο παίκτης μπορεί είτε να εξουδετερώσει είτε να πυροδοτήσει;",
    "answers": ["Ένας πυρηνικός αντιδραστήρας", "Μια ενεργή ατομική βόμβα που δεν εξερράγη", "Μια δεξαμενή ραδιενεργών αποβλήτων", "Ένα στρατιωτικό τανκ"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η πόλη Megaton χτίστηκε γύρω από μια αμερικανική ατομική βόμβα που έπεσε αλλά δεν έσκασε κατά τον Μεγάλο Πόλεμο, λατρευόμενη από την αίρεση Children of Atom.",
    "funFacts": [
      "Ο μυστηριώδης Mr. Burke προσφέρει στον παίκτη 1.000 καπάκια και μια σουίτα στο Tenpenny Tower εάν επιλέξει να ανατινάξει την πόλη.",
      "Η πυροδότηση της βόμβας αποτελεί μία από τις πιο θεαματικές και ηθικά ακραίες επιλογές στην ιστορία των παιχνιδιών της Bethesda."
    ],
    "source": "https://el.wikipedia.org/wiki/Fallout_3",
    "locale": "el-GR",
    "tags": ["fallout-3", "megaton", "bethesda", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_117",
    "text": "Ποιος αδελφός του Diablo, γνωστός ως ο Άρχοντας της Καταστροφής, πολιορκεί το ιερό βουνό Mount Arreat στο «Diablo II: Lord of Destruction» (2001);",
    "answers": ["Mephisto", "Belial", "Baal", "Azmodan"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Baal είναι ένας από τους τρεις Μεγάλους Δαίμονες (Prime Evils) που εκστρατεύει για να διαφθείρει τον Worldstone στα βάθη του Mount Arreat.",
    "funFacts": [
      "Η εισαγωγική κινηματογραφική σκηνή όπου ο Baal εκμηδενίζει τον βάρβαρο πρεσβευτή στις πύλες του Arreat θεωρείται ορόσημο animation της Blizzard.",
      "Μετά τη νίκη του παίκτη, ο αρχάγγελος Tyrael αναγκάζεται να καταστρέψει τον μολυσμένο Worldstone, αλλάζοντας για πάντα τη μοίρα του Sanctuary."
    ],
    "source": "https://en.wikipedia.org/wiki/Diablo_II:_Lord_of_Destruction",
    "locale": "el-GR",
    "tags": ["diablo-2", "baal", "blizzard", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_118",
    "text": "Ποιος είναι ο κεντρικός πρωταγωνιστής στο «BioShock 2», όντας ένα πρωτότυπο Big Daddy της σειράς Alpha Series;",
    "answers": ["Booker DeWitt", "Jack", "Frank Fontaine", "Subject Delta"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Subject Delta ήταν το πρώτο επιτυχημένο Big Daddy που συνδέθηκε ψυχολογικά με μία μόνο Little Sister, την Eleanor Lamb, και ξυπνά 10 χρόνια μετά για να τη βρει.",
    "funFacts": [
      "Σε αντίθεση με τα μεταγενέστερα Big Daddies τύπου Bouncer, ο Delta διατηρεί ελεύθερη βούληση και μπορεί να χρησιμοποιεί πλασμίδια και συμβατικά όπλα ταυτόχρονα.",
      "Εάν απομακρυνθεί πολύ από την Eleanor για μεγάλο διάστημα, το νευρικό του σύστημα παθαίνει κώμα και η καρδιά του σταματά να χτυπά."
    ],
    "source": "https://en.wikipedia.org/wiki/BioShock_2",
    "locale": "el-GR",
    "tags": ["bioshock-2", "subject-delta", "big-daddy", "rapture"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_119",
    "text": "Ποια είναι η αρραβωνιαστικιά του Isaac Clarke που υπηρετούσε ως ανώτερη ιατρική αξιωματικός στο USG Ishimura στο «Dead Space»;",
    "answers": ["Nicole Brennan", "Kendra Daniels", "Ellie Langford", "Lexine Murdoch"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Isaac Clarke προσφέρεται εθελοντικά για την αποστολή επισκευής του Ishimura αποκλειστικά για να βρει και να σώσει τη Nicole.",
    "funFacts": [
      "Η Nicole είχε αυτοκτονήσει πριν καν φτάσει το σκάφος του Isaac, και οι εμφανίσεις της σε όλο το παιχνίδι ήταν παραισθήσεις που δημιουργούσε ο εξωγήινος Marker.",
      "Στο remake του 2023, η Nicole απέκτησε πολύ βαθύτερο ρόλο με πλήρεις προαιρετικές δευτερεύουσες αποστολές που αποκαλύπτουν τις τελευταίες της ώρες."
    ],
    "source": "https://el.wikipedia.org/wiki/Dead_Space_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["dead-space", "nicole-brennan", "isaac-clarke", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_120",
    "text": "Ποια είναι τα τρία βασικά λειτουργικά κτίσματα που μπορεί να κατασκευάσει και να αναβαθμίσει ο Engineer στο «Team Fortress 2»;",
    "answers": ["Radar, Barrier, Turret", "Sentry Gun, Dispenser, Teleporter", "Minefield, Medikit, Generator", "Shield, Jammer, Cannon"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Dell Conagher (Engineer) κατασκευάζει αυτόματα πολυβόλα (Sentry Guns), συσκευές ανεφοδιασμού ζωής/πυρομαχικών (Dispensers) και τηλεμεταφορείς (Teleporters).",
    "funFacts": [
      "Ο Engineer κατάγεται από το Bee Cave του Τέξας και διαθέτει 11 διδακτορικά διπλώματα σε διάφορους τομείς της μηχανικής.",
      "Χτυπώντας τα κτίσματά του με το κλειδί (Wrench), ο Engineer μπορεί να επισκευάσει ζημιές και να τα αναβαθμίσει έως το Επίπεδο 3."
    ],
    "source": "https://el.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "engineer", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_121",
    "text": "Ποιο ευτραφές Special Infected στο «Left 4 Dead» κάνει εμετό πράσινη χολή πάνω στους επιζώντες, τυφλώνοντάς τους και προσελκύοντας μαζικά ορδές ζόμπι;",
    "answers": ["Spitter", "Charger", "Boomer", "Smoker"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Boomer εκρήγνυται όταν πυροβοληθεί, καλύπτοντας όσους βρίσκονται κοντά με ελκυστική χολή που εξαγριώνει τα κοινά ζόμπι.",
    "funFacts": [
      "Οι παίκτες πρέπει να τον απωθούν με το κοντάκι του όπλου (shove) προτού τον πυροβολήσουν, ώστε να μην λερωθούν από την έκρηξη.",
      "Υπάρχει και θηλυκή παραλλαγή (Boomette) που εισήχθη στο Left 4 Dead 2."
    ],
    "source": "https://el.wikipedia.org/wiki/Left_4_Dead",
    "locale": "el-GR",
    "tags": ["left-4-dead", "boomer", "valve", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_122",
    "text": "Ποια Ελβετίδα γιατρός και υποστηρικτικός ήρωας στο «Overwatch» φωνάζει τη διάσημη ατάκα «Heroes never die!» κατά την ανάσταση των συμμάχων της;",
    "answers": ["Moira", "Ana", "Brigitte", "Mercy (Dr. Angela Ziegler)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Dr. Angela Ziegler (Mercy) είναι επικεφαλής ιατρικών ερευνών της Overwatch και χρησιμοποιεί τη ράβδο Caduceus Staff για θεραπεία και ενίσχυση ζημιάς.",
    "funFacts": [
      "Στην αρχική έκδοση του Overwatch το 2016, η απόλυτη ικανότητά της 'Resurrect' μπορούσε να αναστήσει ολόκληρη την ομάδα πέντε παικτών ταυτόχρονα.",
      "Η στολή Valkyrie που φοράει της επιτρέπει να γλιστράει απαλά στον αέρα και να πετάει απευθείας προς τους τραυματισμένους συμπαίκτες της."
    ],
    "source": "https://el.wikipedia.org/wiki/Overwatch",
    "locale": "el-GR",
    "tags": ["overwatch", "mercy", "blizzard", "hero-shooter"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_123",
    "text": "Ποιο μυθικό αρχαίο Pokémon αποτέλεσε το γενετικό πρότυπο από το οποίο κλωνοποιήθηκε εργαστηριακά ο πανίσχυρος Mewtwo στο νησί Cinnabar;",
    "answers": ["Mew", "Ditto", "Arceus", "Celebi"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Mewtwo δημιουργήθηκε από επιστήμονες που τροποποίησαν το DNA του Mew με στόχο να κατασκευάσουν το απόλυτο μαχητικό Pokémon.",
    "funFacts": [
      "Στο αρχικό Pokémon Red/Blue, ο Mew ήταν ένα κρυφό Pokémon που πρόσθεσε μυστικά ο προγραμματιστής Shigeki Morimoto μόλις δύο εβδομάδες πριν την κυκλοφορία.",
      "Τα ημερολόγια μέσα στην καμένη έπαυλη του Cinnabar Island καταγράφουν ότι ο Mew 'γέννησε' τον Mewtwo στις 6 Φεβρουαρίου."
    ],
    "source": "https://el.wikipedia.org/wiki/Mewtwo",
    "locale": "el-GR",
    "tags": ["pokemon", "mewtwo", "mew", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_124",
    "text": "Ποια παρανοϊκή οικογένεια κανιβάλων αιχμαλωτίζει τον Ethan Winters στην εγκαταλελειμμένη έπαυλη της Λουιζιάνας στο «Resident Evil 7: Biohazard»;",
    "answers": ["Η οικογένεια Salazar", "Η οικογένεια Baker", "Η οικογένεια Beneviento", "Η οικογένεια Ashford"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Jack, η Marguerite και ο Lucas Baker είχαν μολυνθεί από το βιολογικό όπλο Eveline, αποκτώντας υπεράνθρωπες αναπλαστικές δυνάμεις και κανιβαλιστικές τάσεις.",
    "funFacts": [
      "Η διάσημη σκηνή όπου ο Jack Baker σπάει τον τοίχο με βαριοπούλα φωνάζοντας 'Welcome to the family, son!' έγινε το σήμα κατατεθέν του παιχνιδιού.",
      "Το Resident Evil 7 επανέφερε τη σειρά στις καθαρές ρίζες τρόμου επιβίωσης, υιοθετώντας για πρώτη φορά στην κύρια σειρά κάμερα πρώτου προσώπου."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil_7:_Biohazard",
    "locale": "el-GR",
    "tags": ["resident-evil-7", "baker-family", "capcom", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_125",
    "text": "Σε ποιο εξωτικό τροπικό νησί της Καραϊβικής ναυαγούν προσωρινά ο Arthur Morgan και τα μέλη της συμμορίας στο «Red Dead Redemption 2»;",
    "answers": ["Tahiti", "Cuba", "Guarma", "Saint Denis"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Στο Κεφάλαιο 5, μετά την καταστροφική ληστεία τράπεζας στο Saint Denis, οι επιζώντες ναυαγούν στο νησί Guarma και εμπλέκονται σε μια τοπική επανάσταση σκλάβων.",
    "funFacts": [
      "Το Guarma είναι η μοναδική περιοχή στο παιχνίδι όπου ο παίκτης δεν μπορεί να επιστρέψει ελεύθερα μετά την ολοκλήρωση των αποστολών του κεφαλαίου.",
      "Φιλοξενεί μοναδικά είδη τροπικών πτηνών και φιδιών που είναι απαραίτητα για την πλήρη συμπλήρωση του εγκυκλοπαιδικού Compendium."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "guarma", "rockstar-games", "western"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_126",
    "text": "Ποιο γιγάντιο σκουριασμένο όπλο σέρνει αργά στο πάτωμα ο Pyramid Head στις ανατριχιαστικές εμφανίσεις του στο «Silent Hill 2»;",
    "answers": ["Ένα τεράστιο σφυρί", "Μια αλυσοπρίονο", "Μια βαριά λόγχη", "Το Μεγάλο Μαχαίρι (Great Knife)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Great Knife είναι ένα υπερμεγέθες μαχαίρι εκτέλεσης τόσο βαρύ που ο Pyramid Head αναγκάζεται να το σέρνει με τα δύο χέρια, παράγοντας ανατριχιαστικό μεταλλικό ήχο.",
    "funFacts": [
      "Ο James Sunderland μπορεί να βρει και να εξοπλιστεί ο ίδιος με το Great Knife στο Labyrinth, αλλά είναι τόσο βαρύ που επιβραδύνει υπερβολικά το περπάτημά του.",
      "Ο σχεδιαστής Masahiro Ito δήλωσε ότι εμπνεύστηκε τη μορφή του Pyramid Head από τους εκτελεστές της μεσαιωνικής πόλης που φορούσαν τριγωνικές κουκούλες."
    ],
    "source": "https://el.wikipedia.org/wiki/Silent_Hill_2",
    "locale": "el-GR",
    "tags": ["silent-hill-2", "pyramid-head", "great-knife", "konami"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_127",
    "text": "Ποιος ευγενής ιππότης του Μεσαίωνα μεταμορφώθηκε σε ανθρωπόμορφο βάτραχο από μια κατάρα του σκοτεινού μάγου Magus στο «Chrono Trigger»;",
    "answers": ["Glenn (Frog)", "Cyrus", "Robo", "Kino"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Glenn ήταν ο σкваϊρος του θρυλικού ιππότη Cyrus. Μετά τον θάνατο του μέντορά του, καταράστηκε να ζει ως βάτραχος κρατώντας το θρυλικό σπαθί Masamune.",
    "funFacts": [
      "Στην αγγλική μετάφραση του SNES από τον Ted Woolsey, ο Frog μιλάει με ψευδο-σεξπηρική αγγλική διάλεκτο ('Thou', 'Thee'), κάτι που δεν υπήρχε στο ιαπωνικό κείμενο.",
      "Μπορεί να κόψει ένα ολόκληρο βουνό στα δύο με το σπαθί Masamune για να ανοίξει το πέρασμα προς το κάστρο του Magus."
    ],
    "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
    "locale": "el-GR",
    "tags": ["chrono-trigger", "frog", "glenn", "square"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_128",
    "text": "Σε ποια ιερή αρχαία τοποθεσία δολοφονείται τραγικά η Aerith Gainsborough από το σπαθί του Sephiroth στο κλασικό «Final Fantasy VII» (1997);",
    "answers": ["Στη Midgar", "Στην Ξεχασμένη Πόλη (Forgotten Capital)", "Στο Nibelheim", "Στο Cosmo Canyon"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Aerith προσευχόταν στον βωμό της Forgotten Capital για να επικαλεστεί το Holy (το αντίδοτο στο Meteor) όταν ο Sephiroth έπεσε από ψηλά καρφώνοντάς την με το σπαθί του.",
    "funFacts": [
      "Η σκηνή όπου ο Cloud αφήνει το σώμα της Aerith να βυθιστεί στα γαλήνια νερά της λίμνης θεωρείται η πιο συγκινητική στιγμή στην ιστορία των JRPGs.",
      "Η απώλεια της Aerith ήταν μόνιμη στο παιχνίδι, καταρρίπτοντας δεκάδες αστικούς μύθους της εποχής για μυστικούς τρόπους ανάστασής της."
    ],
    "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VII",
    "locale": "el-GR",
    "tags": ["final-fantasy", "aerith", "sephiroth", "square-enix"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_129",
    "text": "Πώς ονομάζεται το ειδικό τόξο που κληρονόμησε ο Ατρέας από τη μητέρα του Faye και αναβαθμίζεται με μαγικά βέλη στο «God of War»;",
    "answers": ["Leviathan Bow", "Apollo's Bow", "Talon Bow", "Yggdrasil Bow"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Talon Bow κατασκευάστηκε από ξύλο γιού (yew wood) από τη Faye και εμπλουτίζεται κατά τη διάρκεια του ταξιδιού με βέλη φωτός (Light) και ηλεκτρισμού (Shock).",
    "funFacts": [
      "Ο παίκτης μπορεί να δώσει εντολή στον Ατρέα να πυροβολήσει στόχους ανά πάσα στιγμή πατώντας το κουμπί Τετράγωνο (Square), χωρίς να διακόπτεται η μάχη του Κράτου.",
      "Τα βέλη του Ατρέα είναι απαραίτητα για την επίλυση γρίφων στον κόσμο, διαλύοντας κόκκινους κρυστάλλους και ενεργοποιώντας μπλε γέφυρες φωτός."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "atreus", "talon-bow", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_130",
    "text": "Ποιος διάσημος Βρετανός κωμικός και ηθοποιός χάρισε τη χαρακτηριστική φωνή του στον φλύαρο πυρήνα Wheatley στο «Portal 2»;",
    "answers": ["Ricky Gervais", "Hugh Laurie", "Simon Pegg", "Stephen Merchant"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Stephen Merchant αυτοσχεδίασε πολλές από τις αστείες ατάκες του Wheatley, ενός πυρήνα τεχνητής νοημοσύνης σχεδιασμένου ειδικά από τους επιστήμονες ως 'ο μεγαλύτερος βλάκας του κόσμου'.",
    "funFacts": [
      "Ο Wheatley σχεδιάστηκε για να παράγει συνεχώς κακές ιδέες ώστε να αποδυναμώνει τη νοημοσύνη της GLaDOS.",
      "Η ερμηνεία του Merchant απέσπασε διθυραμβικές κριτικές και κέρδισε το βραβείο Best Performance by a Human Male στα Spike Video Game Awards 2011."
    ],
    "source": "https://en.wikipedia.org/wiki/Wheatley_(Portal)",
    "locale": "el-GR",
    "tags": ["portal-2", "wheatley", "stephen-merchant", "valve"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_131",
    "text": "Πώς ονομάζεται η ψυχική κατάρρευση και βίαιη μανία που παθαίνουν οι άνθρωποι στο «Cyberpunk 2077» από την υπερβολική προσθήκη κυβερνοεμφυτευμάτων;",
    "answers": ["Cyberpsychosis", "Brain Dance", "Netrunning Shock", "Relic Overload"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Cyberpsychosis εμφανίζεται όταν η ανθρώπινη ψυχοσύνθεση αποξενώνεται από το ίδιο της το σώμα λόγω των μηχανικών τροποποιήσεων, οδηγώντας σε δολοφονικές εκρήξεις.",
    "funFacts": [
      "Η επίλεκτη αστυνομική δύναμη 'MaxTac' (Psycho Squad) αναλαμβάνει την άμεση και αμείλικτη εξουδετέρωση των cyberpsychos στους δρόμους της Night City.",
      "Το φαινόμενο της Cyberpsychosis εξερευνάται βαθιά στην πολυβραβευμένη σειρά anime 'Cyberpunk: Edgerunners' μέσω του πρωταγωνιστή David Martinez."
    ],
    "source": "https://el.wikipedia.org/wiki/Cyberpunk_2077",
    "locale": "el-GR",
    "tags": ["cyberpunk-2077", "cyberpsychosis", "cd-projekt-red", "lore"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_132",
    "text": "Ποια τεράστια τρίποδα βιομηχανικά τέρατα των Combine περιπολούν στους δρόμους της City 17 και εκτοξεύουν φονικές δέσμες στρέβλωσης στο «Half-Life 2»;",
    "answers": ["Hunters", "Striders", "Gunships", "Dropships"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Striders είναι συνθετικές πολεμικές μηχανές (Synths) ύψους άνω των 15 μέτρων που κινούνται με τρία αρθρωτά μακριά πόδια και καταστρέφονται μόνο με ρουκέτες RPG.",
    "funFacts": [
      "Στην επική μάχη στους δρόμους της City 17, οι Striders μπορούν να ισοπεδώσουν ολόκληρα κτίρια και να εξοντώσουν στρατιώτες της αντίστασης με τα πόδια τους σαν καρφιά.",
      "Στο Half-Life 2: Episode Two, ο παίκτης χρησιμοποιεί τις αυτοσχέδιες κολλώδεις βόμβες του Dr. Magnusson ('Magnusson Devices') για να ανατινάξει τους Striders."
    ],
    "source": "https://el.wikipedia.org/wiki/Half-Life_2",
    "locale": "el-GR",
    "tags": ["half-life", "striders", "combine", "valve"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_133",
    "text": "Πώς ονομάζεται η μεταλλαγμένη Sarah Kerrigan αφού αιχμαλωτίστηκε και ενσωματώθηκε στο σμήνος των Zerg ως η απόλυτη ηγέτιδά τους στο «StarCraft»;",
    "answers": ["The Broodmother", "The Overmind", "The Queen of Blades", "The Infested Empress"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Kerrigan προδόθηκε από τον Arcturus Mengsk στον πλανήτη Tarsonis, αλλά αντί να εκτελεστεί, μεταλλάχθηκε από τον Overmind στην πανίσχυρη 'Βασίλισσα των Λεπίδων'.",
    "funFacts": [
      "Τα μαλλιά της μετατράπηκαν σε αγκαθωτά πλοκάμια και στην πλάτη της φύτρωσαν τεράστια οστέινα φτερά σε σχήμα λεπίδων.",
      "Αποτελεί μία από τις πιο διάσημες γυναικείες αντι-ηρωίδες στην ιστορία των βιντεοπαιχνιδιών, ελέγχοντας δισεκατομμύρια πλάσματα Zerg μέσω τηλεπαθητικής σύνδεσης."
    ],
    "source": "https://el.wikipedia.org/wiki/StarCraft",
    "locale": "el-GR",
    "tags": ["starcraft", "kerrigan", "queen-of-blades", "blizzard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_134",
    "text": "Ποια δυναμική προστάτιδα του Hallownest με το κόκκινο ένδυμα κρατάει βελόνα με μεταξωτή κλωστή και πρωταγωνιστεί στο αναμενόμενο «Hollow Knight: Silksong»;",
    "answers": ["Cloth", "Monomon", "White Lady", "Hornet"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Hornet είναι η πριγκίπισσα-προστάτιδα των ερειπίων, καρπός της συμφωνίας του Pale King με την Herrah the Beast, δοκιμάζοντας τη δύναμη του ιππότη σε δύο αναμετρήσεις.",
    "funFacts": [
      "Σε αντίθεση με τον σιωπηλό Knight, η Hornet μιλάει κανονικά και εκφωνεί τη διάσημη πολεμική ιαχή 'Shaw!' κατά τη διάρκεια των επιθέσεών της.",
      "Το 'Silksong' ξεκίνησε αρχικά ως απλό πρόσθετο περιεχόμενο (DLC) αλλά επεκτάθηκε σε πλήρες αυτόνομο σίκουελ στο βασίλειο του Pharloom."
    ],
    "source": "https://en.wikipedia.org/wiki/Hollow_Knight:_Silksong",
    "locale": "el-GR",
    "tags": ["hollow-knight", "hornet", "silksong", "team-cherry"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_135",
    "text": "Ποιος ογκώδης μεταλλαγμένος Witcher της Σχολής της Οχιάς δολοφονεί τον βασιλιά Foltest στο «The Witcher 2: Assassins of Kings» (2011);",
    "answers": ["Letho of Gulet", "Vesemir", "Lambert", "Eskel"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Letho παγιδεύει τον Geralt ώστε να κατηγορηθεί άδικα για τη δολοφονία του βασιλιά, δρώντας υπό τις μυστικές διαταγές της αυτοκρατορίας του Nilfgaard.",
    "funFacts": [
      "Ο Letho είχε σώσει στο παρελθόν τη ζωή της Yennefer, γεγονός που περιπλέκει έντονα τη σχέση του με τον Geralt.",
      "Στο The Witcher 3, εάν ο παίκτης έχει αφήσει τον Letho ζωντανό, μπορεί να τον στρατολογήσει για να πολεμήσει στην άμυνα του Kaer Morhen."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_2:_Assassins_of_Kings",
    "locale": "el-GR",
    "tags": ["witcher", "letho", "cd-projekt-red", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_136",
    "text": "Ποιος μυθικός ημίθεος στρατηγός στο «Elden Ring» συγκρατεί τη μοίρα των αστεριών με βαρυτική μαγεία και ιππεύει ένα μικρό άλογο ονόματι Leonard;",
    "answers": ["Godrick the Grafted", "Starscourge Radahn", "Rykard", "Morgott"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο General Radahn έμαθε τη μαγεία της βαρύτητας ειδικά για να μπορεί να ιππεύει το αγαπημένο του άλογο χωρίς να το συνθλίβει με το γιγάντιο βάρος του.",
    "funFacts": [
      "Η μάχη εναντίον του διεξάγεται ως ένα επικό 'Φεστιβάλ Πολέμου' (Radahn Festival), όπου ο παίκτης μπορεί να καλέσει ταυτόχρονα δεκάδες NPCs στη μάχη.",
      "Κατά τη δεύτερη φάση της μάχης, ο Radahn εκτοξεύεται στην στρατόσφαιρα και πέφτει πίσω στη γη σαν φλεγόμενος μετεωρίτης."
    ],
    "source": "https://el.wikipedia.org/wiki/Elden_Ring",
    "locale": "el-GR",
    "tags": ["elden-ring", "radahn", "fromsoftware", "bosses"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_137",
    "text": "Ποιος ιπτάμενος διαστημικός δράκος και πιστός διοικητής των Space Pirates είναι ο αιώνιος ορκισμένος εχθρός της Samus Aran στη σειρά «Metroid»;",
    "answers": ["Kraid", "Phantoon", "Ridley", "Draygon"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Ridley δολοφόνησε τους γονείς της Samus στην αποικία K-2L όταν εκείνη ήταν παιδί, ξεκινώντας μια διαγαλαξιακή βεντέτα που διαρκεί δεκαετίες.",
    "funFacts": [
      "Πήρε το όνομά του προς τιμήν του σκηνοθέτη Ridley Scott, δημιουργού της κλασικής ταινίας επιστημονικής φαντασίας 'Alien'.",
      "Επανεμφανίζεται σε πολλαπλές κυβερνητικές μορφές, όπως ο Meta Ridley και ο Mecha Ridley, επιστρέφοντας πάντα από τον θάνατο."
    ],
    "source": "https://en.wikipedia.org/wiki/Ridley_(Metroid)",
    "locale": "el-GR",
    "tags": ["metroid", "ridley", "nintendo", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_138",
    "text": "Με ποια πρωτοποριακή τεχνολογία είναι γενετικά και κυτταρικά εξοπλισμένος ο πράκτορας JC Denton στο πρωτότυπο «Deus Ex» (2000);",
    "answers": ["Μηχανικά προσθετικά μέλη", "Κυβερνητικά καλώδια", "Βιολογικούς κλώνους", "Νανοτεχνολογία (Nano-augmentations)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο JC Denton και ο αδελφός του Paul ήταν οι πρώτοι πράκτορες της UNATCO που τροποποιήθηκαν με νανοτεχνολογία σε μικροσκοπικό μοριακό επίπεδο.",
    "funFacts": [
      "Σε αντίθεση με τους παλαιότερους μηχανικούς πράκτορες Gunther Hermann και Anna Navarre, ο Denton διατηρεί εντελώς φυσική ανθρώπινη εμφάνιση.",
      "Τα νανο-εμφυτεύματα απαιτούν βιο-ηλεκτρική ενέργεια από μπαταρίες για να τροφοδοτήσουν ικανότητες όπως η αορατότητα και η υπεράνθρωπη δύναμη."
    ],
    "source": "https://en.wikipedia.org/wiki/Deus_Ex_(video_game)",
    "locale": "el-GR",
    "tags": ["deus-ex", "jc-denton", "nanotechnology", "cyberpunk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_139",
    "text": "Ποιο είναι το επίσημο πλήρες επώνυμο του Ken, του πλούσιου Αμερικανού αντιπάλου και αδελφικού φίλου του Ryu στη σειρά «Street Fighter»;",
    "answers": ["Ken Masters", "Ken Bogard", "Ken Howard", "Ken Vance"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Ken Masters είναι ο κληρονόμος του πανίσχυρου αμερικανικού ομίλου Masters Foundation, συνδυάζοντας την πολυτελή ζωή με την αγάπη για τις πολεμικές τέχνες.",
    "funFacts": [
      "Ενώ ο Ryu εστιάζει στην ισχύ του Hadoken, ο Ken ειδικεύεται στο Shoryuken, προσθέτοντας φλόγες στη γροθιά του (Flaming Shoryuken).",
      "Είναι παντρεμένος με την Eliza και έχουν έναν γιο που ονομάζεται Mel."
    ],
    "source": "https://en.wikipedia.org/wiki/Ken_Masters",
    "locale": "el-GR",
    "tags": ["street-fighter", "ken-masters", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_140",
    "text": "Ποια χαμένη πόλη στην αφιλόξενη έρημο Rub' al Khali αναζητά ο Nathan Drake στο «Uncharted 3: Drake's Deception» (2011);",
    "answers": ["Ελ Ντοράντο", "Iram of the Pillars (Ατλαντίδα των Άμμων)", "Shambhala", "Shangri-La"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Drake ακολουθεί τα ίχνη του προγόνου του Sir Francis Drake και του Lawrence της Αραβίας για να βρει τη χαμένη πόλη Iram of the Pillars.",
    "funFacts": [
      "Η πόλη καταστράφηκε όταν ο βασιλιάς Σολομών έκλεισε έναν ορειχάλκινο αμφορέα με παγιδευμένα κακά πνεύματα (Djinn) στα βάθη της πηγής της.",
      "Η σκηνή όπου ο Nathan Drake πέφτει από ένα φλεγόμενο φορτηγό αεροπλάνο με αλεξίπτωτο στην καρδιά της ερήμου είναι μία από τις πιο διάσημες σκηνές δράσης."
    ],
    "source": "https://el.wikipedia.org/wiki/Uncharted_3:_Drake%27s_Deception",
    "locale": "el-GR",
    "tags": ["uncharted-3", "iram-of-the-pillars", "naughty-dog", "nathan-drake"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_141",
    "text": "Ποια ήταν η κατάρα που επέβαλε ο Δράκουλας στον Simon Belmont στο τέλος του αρχικού παιχνιδιού, οδηγώντας στην πλοκή του «Castlevania II: Simon's Quest»;",
    "answers": ["Τον τύφλωσε μόνιμα", "Τον φυλάκισε στον χρόνο", "Μια θανατηφόρα κατάρα αργής αποσύνθεσης", "Τον μετέτρεψε σε λυκάνθρωπο"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Simon Belmont αναγκάζεται να ταξιδέψει σε όλη την Τρανσυλβανία για να βρει και να κάψει τα πέντε διασκορπισμένα μέλη του σώματος του Δράκουλα ώστε να λύσει την κατάρα.",
    "funFacts": [
      "Το παιχνίδι εισήγαγε τον πρωτοποριακό κύκλο ημέρας και νύχτας, με την ιστορική προειδοποίηση στην οθόνη: 'What a horrible night to have a curse'.",
      "Είχε τρία διαφορετικά φινάλε ανάλογα με τον αριθμό των ημερών που χρειάστηκε ο παίκτης για να ολοκληρώσει την αποστολή."
    ],
    "source": "https://en.wikipedia.org/wiki/Castlevania_II:_Simon%27s_Quest",
    "locale": "el-GR",
    "tags": ["castlevania", "simons-quest", "konami", "nes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_142",
    "text": "Από ποιον θρυλικό βασιλιά της Σπάρτης κατάγονται οι πρωταγωνιστές Αλέξιος και Κασσάνδρα στο «Assassin's Creed Odyssey» (2018);",
    "answers": ["Αγησίλαος Β΄", "Κλεομένης Α΄", "Παυσανίας", "Λεωνίδας Α΄"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο πρωταγωνιστής κρατά ως κύριο όπλο και κειμήλιο της Πρώτης Φυλής (Isu) το σπασμένο 'Δόρυ του Λεωνίδα', το οποίο κληρονόμησε από τον παππού του.",
    "funFacts": [
      "Το εισαγωγικό επίπεδο του παιχνιδιού αναπαριστά την ιστορική μάχη των Θερμοπυλών (480 π.Χ.), όπου ο παίκτης ελέγχει απευθείας τον βασιλιά Λεωνίδα.",
      "Η Κασσάνδρα θεωρείται ο επίσημος canon κεντρικός χαρακτήρας του παιχνιδιού σύμφωνα με το επίσημο βιβλίο της Ubisoft."
    ],
    "source": "https://el.wikipedia.org/wiki/Assassin%27s_Creed_Odyssey",
    "locale": "el-GR",
    "tags": ["assassins-creed", "odyssey", "leonidas", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_143",
    "text": "Ποιος βασανισμένος ιερέας και κυνηγός της Healing Church αποτελεί το πρώτο υποχρεωτικό αφεντικό μέσα στην πόλη Yharnam στο «Bloodborne»;",
    "answers": ["Father Gascoigne", "Cleric Beast", "Vicar Amelia", "Gehrman"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Father Gascoigne έχει υποκύψει στη μανία του αίματος και κατά τη διάρκεια της μάχης μεταμορφώνεται σε ένα γιγάντιο λυκάνθρωπο θηρίο.",
    "funFacts": [
      "Ο παίκτης μπορεί να χρησιμοποιήσει ένα μικρό μουσικό κουτί (Tiny Music Box) που του δίνει η μικρή κόρη του Gascoigne για να τον ζαλίσει προσωρινά με αναμνήσεις της οικογένειάς του.",
      "Η φράση του 'Beasts all over the shop... You'll be one of them, sooner or later' είναι από τις πιο αναγνωρίσιμες ατάκες του παιχνιδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/Bloodborne",
    "locale": "el-GR",
    "tags": ["bloodborne", "father-gascoigne", "fromsoftware", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_144",
    "text": "Ποιο πανίσχυρο διαστημόπλοιο που θεωρούνταν η ναυαρχίδα του Saren αποκαλύπτεται ότι είναι ένα ζωντανό sentient Reaper στο πρώτο «Mass Effect»;",
    "answers": ["Harbinger", "Sovereign (Nazara)", "Leviathan", "Collector Base"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Sovereign χειραγωγεί τον Saren μέσω κατήχησης (indoctrination) και προσπαθεί να ανοίξει το ρελέ της Ακρόπολης για να ξεκινήσει η γενοκτονία των Reapers.",
    "funFacts": [
      "Η ανατριχιαστική συνομιλία του Sovereign με τον Shepard στον πλανήτη Virmire περιέχει τη διάσημη φράση: 'Rudimentary creatures of blood and flesh, you touch my mind, fumbling in ignorance'.",
      "Το πραγματικό του όνομα ανάμεσα στους Reapers είναι 'Nazara'."
    ],
    "source": "https://el.wikipedia.org/wiki/Mass_Effect_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["mass-effect", "sovereign", "reapers", "bioware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_145",
    "text": "Ποια μαύρη δράκαινα, κόρη του Deathwing, είχε διεισδύσει στη βασιλική αυλή του Stormwind υποδυόμενη την ευγενή Katrana Prestor στο «World of Warcraft»;",
    "answers": ["Alexstrasza", "Ysera", "Onyxia", "Sindragosa"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Onyxia χειραγωγούσε τον ανήλικο πρίγκιπα Anduin Wrynn και αποδυνάμωνε τη Συμμαχία, προτού αποκαλυφθεί η συνωμοσία της από τον Marshal Windsor.",
    "funFacts": [
      "Η επιδρομή (raid) 'Onyxia's Lair' γέννησε το ιστορικό viral ηχητικό meme του 2006 'More Dots, 50 DKP Minus!'.",
      "Η τακτική της επίθεση με βαθιά ανάσα φωτιάς ('Onyxia wipes the raid with Deep Breath') ήταν ο φόβος και ο τρόμος των παικτών."
    ],
    "source": "https://en.wikipedia.org/wiki/World_of_Warcraft",
    "locale": "el-GR",
    "tags": ["world-of-warcraft", "onyxia", "blizzard", "mmorpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_146",
    "text": "Ποιος διάσημος ηθοποιός του Χόλιγουντ δάνεισε τη φωνή του στον James, τον πατέρα του Lone Wanderer, στο «Fallout 3» (2008);",
    "answers": ["Ron Perlman", "Patrick Stewart", "Sean Bean", "Liam Neeson"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Liam Neeson ενσάρκωσε τον James, τον επικεφαλής επιστήμονα του Project Purity που εγκαταλείπει το Vault 101 για να προσφέρει καθαρό νερό στην Capital Wasteland.",
    "funFacts": [
      "Ο Ron Perlman, από την άλλη πλευρά, εκφωνεί τη διαχρονική εισαγωγική φράση κάθε παιχνιδιού Fallout: 'War. War never changes.'.",
      "Το πρόσωπο του πατέρα James προσαρμόζεται αυτόματα στον κώδικα του παιχνιδιού ώστε να μοιάζει με τα χαρακτηριστικά που επέλεξε ο παίκτης για τον ήρωά του."
    ],
    "source": "https://el.wikipedia.org/wiki/Fallout_3",
    "locale": "el-GR",
    "tags": ["fallout-3", "liam-neeson", "bethesda", "voice-acting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_147",
    "text": "Ποια αρχέγονη θεά της νύχτας λειτουργεί ως στοργική μητρική φιγούρα και σύμβουλος για τον Ζαγρέα στο παλάτι του Κάτω Κόσμου στο «Hades»;",
    "answers": ["Νύχτα (Nyx)", "Περσεφόνη", "Μέγαιρα", "Εκάτη"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Νύχτα μεγάλωσε τον Ζαγρέα σαν δικό της γιο και τον βοηθά κρυφά στην απόδρασή του, χαρίζοντάς του τον μαγικό Καθρέφτη της Νύχτας (Mirror of Night).",
    "funFacts": [
      "Είναι η μητέρα πολλών άλλων θεοτήτων στον Κάτω Κόσμο, συμπεριλαμβανομένου του Θανάτου (Thanatos) και του Ύπνου (Hypnos).",
      "Η Νύχτα χρησιμοποιεί τις δυνάμεις της για να ανοίξει επικοινωνία ανάμεσα στον Ζαγρέα και τους Ολύμπιους θεούς."
    ],
    "source": "https://el.wikipedia.org/wiki/Hades_(%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%AF%CE%B4%CE%B9)",
    "locale": "el-GR",
    "tags": ["hades", "nyx", "supergiant-games", "greek-mythology"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_148",
    "text": "Ποιο μυστικό υπόγειο τοπίο με γιγάντια πέτρινα δέντρα και μια απέραντη σκοτεινή θάλασσα βρίσκεται κάτω από το Great Hollow στο αρχικό «Dark Souls»;",
    "answers": ["Lost Izalith", "Ash Lake", "Tomb of the Giants", "Valley of Drakes"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Ash Lake είναι μια απόκοσμη, γαλήνια παραλία που κρύβεται πίσω από δύο ψεύτικους τοίχους (illusory walls), αποκαλύπτοντας τα αρχαία δέντρα που στηρίζουν τον κόσμο.",
    "funFacts": [
      "Στο τέρμα του Ash Lake ζει ο Everlasting Dragon, ένας επιζών δράκος της αρχέγονης εποχής που επιτρέπει στον παίκτη να μπει στο Covenant 'Path of the Dragon'.",
      "Η απόλυτη σιωπή και η ξαφνική έναρξη της επιβλητικής χορωδιακής μουσικής κάνουν την ανακάλυψη του Ash Lake μία από τις πιο μυστηριακές στιγμές του παιχνιδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "ash-lake", "fromsoftware", "secret-areas"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_149",
    "text": "Ποιος ναρκισσιστής και ψυχοπαθής διευθύνων σύμβουλος της Hyperion Corporation είναι ο κεντρικός αντίπαλος στο «Borderlands 2» (2012);",
    "answers": ["General Knoxx", "Captain Flynt", "Handsome Jack", "Professor Nakayama"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Handsome Jack αυτοανακηρύσσεται δικτάτορας της Pandora, θεωρώντας τον εαυτό του 'ήρωα' και αποκαλώντας τους Vault Hunters τρομοκράτες.",
    "funFacts": [
      "Φοράει μια πλαστική μάσκα προσώπου στερεωμένη με μεταλλικά κλιπς για να κρύβει τις ουλές και το σημάδι του Vault στο πρόσωπό του.",
      "Αγόρασε ένα άλογο φτιαγμένο από συμπαγή διαμάντια μόνο και μόνο για να χλευάσει τον παίκτη, ονομάζοντάς το 'Butt Stallion'."
    ],
    "source": "https://en.wikipedia.org/wiki/Handsome_Jack",
    "locale": "el-GR",
    "tags": ["borderlands-2", "handsome-jack", "gearbox", "villains"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_150",
    "text": "Ποιος ήταν ο τελευταίος επιζών ιδρυτής της Umbrella Corporation που δολοφονείται από τον Albert Wesker στην ευρωπαϊκή του έπαυλη στο «Resident Evil 5»;",
    "answers": ["Edward Ashford", "James Marcus", "William Birkin", "Oswell E. Spencer"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Lord Oswell E. Spencer αποκάλυψε στον Wesker ότι ήταν μέρος του μυστικού πειράματος 'Project W' για τη δημιουργία μιας νέας φυλής υπερανθρώπων, πριν ο Wesker τον εκτελέσει.",
    "funFacts": [
      "Ο Spencer χρηματοδότησε την κατασκευή της διάσημης έπαυλης Spencer Mansion στα βουνά Arklay από τον αρχιτέκτονα George Trevor.",
      "Η δολοφονία του Spencer λαμβάνει χώρα στο DLC 'Lost in Nightmares', όπου οι παίκτες ελέγχουν τον Chris Redfield και την Jill Valentine."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident-evil", "spencer", "albert-wesker", "capcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_151",
    "text": "Ποια συσκευή εξοπλισμού επιτρέπει στον Isaac Clarke να επιβραδύνει δραματικά την κίνηση των εχθρών και των περιστρεφόμενων μηχανισμών στο «Dead Space»;",
    "answers": ["Stasis Module", "Kinesis Module", "Gravity Boots", "Shock Wave"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Stasis εκτοξεύει μια μπλε ενεργειακή δέσμη που παγώνει προσωρινά την ταχύτητα οποιουδήποτε κινούμενου αντικειμένου ή Necromorph.",
    "funFacts": [
      "Η ενέργεια του Stasis απεικονίζεται ως ένα ημικυκλικό μπλε μετρητή πάνω στη στολή RIG στην πλάτη του Isaac.",
      "Είναι απαραίτητο τόσο για την επιβίωση ενάντια σε ταχύτατους εχθρούς (όπως οι Twitchers) όσο και για το πέρασμα μέσα από ελαττωματικές πόρτες και ανεμιστήρες."
    ],
    "source": "https://el.wikipedia.org/wiki/Dead_Space_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["dead-space", "stasis", "isaac-clarke", "visceral-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_152",
    "text": "Ποιος πρώην σύντροφος του Solid Snake επανεμφανίζεται στο «Metal Gear Solid» ως κυβερνητικός νίντζα με εξωσκελετό και σπαθί υψηλής συχνότητας;",
    "answers": ["Revolver Ocelot", "Gray Fox (Frank Jaeger)", "Vulcan Raven", "Decoy Octopus"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Gray Fox ήταν ο κορυφαίος πράκτορας της FOXHOUND που ακρωτηριάστηκε και μετατράπηκε πειραματικά σε Cyborg Ninja, ζητώντας μια τελευταία έντιμη μονομαχία με τον Snake.",
    "funFacts": [
      "Η διάσημη φράση του στη μονομαχία σώμα με σώμα είναι: 'Only a fool trusts his life to a weapon!'.",
      "Θυσιάζει τη ζωή του συνθλιβόμενος κάτω από το πόδι του γιγάντιου ρομπότ Metal Gear REX για να καταστρέψει το ραντάρ του και να σώσει τον Snake."
    ],
    "source": "https://en.wikipedia.org/wiki/Gray_Fox_(Metal_Gear)",
    "locale": "el-GR",
    "tags": ["metal-gear", "gray-fox", "cyborg-ninja", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_153",
    "text": "Ποιο είναι το μόνιμο μυστήριο γύρω από την κλάση του Pyro στο «Team Fortress 2» που δεν έχει αποκαλυφθεί ποτέ από τη Valve;",
    "answers": ["Το πραγματικό του όπλο", "Η χώρα καταγωγής του", "Η πραγματική του ταυτότητα και το φύλο του", "Η ηλικία του"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Pyro φοράει μια αεροστεγή στολή με μάσκα αερίων που αλλοιώνει τη φωνή του σε ακατάληπτους ήχους, αφήνοντας την ταυτότητα και το φύλο του εντελώς άγνωστα.",
    "funFacts": [
      "Στην επίσημη ταινία 'Meet the Pyro', αποκαλύπτεται ότι ο Pyro πάσχει από παραισθήσεις ('Pyroland'), βλέποντας έναν παραμυθένιο κόσμο με ουράνια τόξα και μωρά ενώ καίει ζωντανούς τους αντιπάλους του.",
      "Οι παίκτες μπορούν να εξοπλιστούν με τα γυαλιά 'Pyrovision Goggles' για να βλέπουν τον χάρτη όπως ακριβώς τον αντιλαμβάνεται ο Pyro."
    ],
    "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "pyro", "valve", "mystery"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_154",
    "text": "Πώς ονομάζεται το ιπτάμενο σκάφος ταξιδιού στον χρόνο που κατασκευάστηκε από τον γκουρού Belthasar στο «Chrono Trigger»;",
    "answers": ["Blackbird", "Silbird", "Invincible", "Epoch (Wings of Time)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Epoch επιτρέπει στην ομάδα του Crono να ταξιδεύει άμεσα ανάμεσα στις ιστορικές εποχές (από την προϊστορία έως το μακρινό μέλλον) χωρίς να χρησιμοποιεί χρονικές πύλες.",
    "funFacts": [
      "Αργότερα στο παιχνίδι αναβαθμίζεται με φτερά από τον Dalton, αποκτώντας τη δυνατότητα πτήσης σε οποιοδήποτε σημείο του χάρτη.",
      "Ο παίκτης μπορεί να επιλέξει να συντρίψει το Epoch απευθείας πάνω στο τελικό τέρας Lavos για να παρακάμψει την πρώτη φάση της τελικής μάχης."
    ],
    "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
    "locale": "el-GR",
    "tags": ["chrono-trigger", "epoch", "square", "time-travel"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_155",
    "text": "Ποιος αρχαίος συνετός δράκος ζει στην απομονωμένη κορυφή του Throat of the World και ηγείται των μοναχών Greybeards στο «Skyrim»;",
    "answers": ["Paarthurnax", "Alduin", "Odahviing", "Durnehviir"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Paarthurnax ήταν ο υπαρχηγός του Alduin, αλλά επαναστάτησε εναντίον του και δίδαξε στους ανθρώπους πώς να χρησιμοποιούν τις δρακο-ιαχές (Thu'um) για να ελευθερωθούν.",
    "funFacts": [
      "Τη φωνή του Paarthurnax χάρισε ο Charles Martinet, ο διάσημος ηθοποιός που ήταν η επίσημη φωνή του Mario για δεκαετίες.",
      "Η διάσημη φιλοσοφική του ερώτηση στον παίκτη είναι: 'What is better: to be born good, or to overcome your evil nature through great effort?'."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "locale": "el-GR",
    "tags": ["skyrim", "paarthurnax", "dragon", "bethesda"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_156",
    "text": "Ποιος παρανοϊκός αυλικός μάγος και γελωτοποιός καταστρέφει την ισορροπία του πλανήτη και γίνεται θεός στο «Final Fantasy VI» (1994);",
    "answers": ["Golbez", "Kefka Palazzo", "Exdeath", "Kuja"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Kefka είναι ένας από τους πιο μοχθηρούς κακούς στην ιστορία των RPGs, δηλητηριάζοντας το νερό του Doma και καταστρέφοντας τον κόσμο στα μισά του παιχνιδιού.",
    "funFacts": [
      "Το χαρακτηριστικό, ανατριχιαστικό 16-bit γέλιο του Kefka ήταν ένα πρωτοποριακό ηχητικό δείγμα που απομνημονεύθηκε από κάθε παίκτη του SNES.",
      "Η τελική μάχη εναντίον του συνοδεύεται από το τετραμερές συμφωνικό αριστούργημα 'Dancing Mad' του Nobuo Uematsu διάρκειας άνω των 17 λεπτών."
    ],
    "source": "https://en.wikipedia.org/wiki/Kefka_Palazzo",
    "locale": "el-GR",
    "tags": ["final-fantasy-6", "kefka", "square", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_157",
    "text": "Ποιος θεός του Ολύμπου σφυρηλάτησε τις Λεπίδες του Χάους στα βάθη του Κάτω Κόσμου και τις χάρισε στον Κράτο στο αρχικό «God of War»;",
    "answers": ["Ήφαιστος", "Άδης", "Άρης (Ares)", "Ερμής"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Άρης έσωσε τον Κράτο από τον θάνατο στη μάχη ενάντια στους βαρβάρους, απαιτώντας σε αντάλλαγμα την απόλυτη αιώνια υποταγή του.",
    "funFacts": [
      "Οι αλυσίδες των λεπίδων κάηκαν και συγκολλήθηκαν μόνιμα στους καρπούς του Κράτου ως σύμβολο της δουλείας του στον Θεό του Πολέμου.",
      "Αφού ο Κράτος σκότωσε τον Άρη με το Κουτί της Πανδώρας, ανέβηκε ο ίδιος στον θρόνο του Ολύμπου ως ο νέος Θεός του Πολέμου."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(σειρά)",
    "locale": "el-GR",
    "tags": ["god-of-war", "ares", "blades-of-chaos", "kratos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_158",
    "text": "Ποιος γιγάντιος προϊστορικός καρχαρίας μπορεί να επιτεθεί αιφνιδιαστικά στα πλοία των παικτών στο «Sea of Thieves» εκτός από τον Κράκεν;",
    "answers": ["Leviathan", "Jaws", "Moby Dick", "Megalodon (Μεγαλόδοντας)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Megalodon εμφανίζεται ξαφνικά με απειλητική μουσική τρομπέτας και επιτίθεται δαγκώνοντας το κύτος του πλοίου, απαιτώντας κανονιοβολισμούς για να ηττηθεί.",
    "funFacts": [
      "Υπάρχουν πέντε διαφορετικά είδη Megalodon, με σπανιότερο όλων τον μυθικό λευκό καρχαρία 'The Shrouded Ghost'.",
      "Εισήχθη για πρώτη φορά στο πρώτο μεγάλο update του παιχνιδιού, 'The Hungering Deep', το καλοκαίρι του 2018."
    ],
    "source": "https://en.wikipedia.org/wiki/Sea_of_Thieves",
    "locale": "el-GR",
    "tags": ["sea-of-thieves", "megalodon", "rare", "pirates"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_159",
    "text": "Ποιος διάσημος ποιητής, τραγουδοποιός και γυναικοκατακτητής είναι ο στενότερος και πιο πιστός φίλος του Geralt of Rivia στη σειρά «The Witcher»;",
    "answers": ["Δανδελέων (Dandelion / Jaskier)", "Zoltan Chivay", "Vernon Roche", "Sigismund Dijkstra"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Dandelion (γνωστός ως Jaskier στο πολωνικό πρωτότυπο) καταγράφει τις περιπέτειες του Geralt σε τραγούδια και μπαλάντες, κάνοντάς τον διάσημο σε όλη την ήπειρο.",
    "funFacts": [
      "Ο Dandelion λειτουργεί ως ο αφηγητής όλων των εισαγωγικών και καταληκτικών σκηνών στο The Witcher 3.",
      "Στην τηλεοπτική σειρά του Netflix, ο χαρακτήρας έγινε παγκόσμιο viral φαινόμενο χάρη στο τραγούδι 'Toss a Coin to Your Witcher'."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC_%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["witcher", "dandelion", "jaskier", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_160",
    "text": "Ποια ευκίνητα, τρομακτικά θηλυκά πλάσματα με καταδυτικές στολές και σύριγγες κυνηγούν τον Subject Delta στο «BioShock 2»;",
    "answers": ["Splicers", "Big Sisters", "Sirens", "Gatherers"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Big Sisters είναι παλιές Little Sisters που μεγάλωσαν, ανέπτυξαν υπερφυσικές τηλεκινητικές δυνάμεις και εξοπλίστηκαν με ελαφριές στολές κατάδυσης.",
    "funFacts": [
      "Επιτίθενται στον παίκτη κάθε φορά που εκείνος ολοκληρώνει τη διάσωση ή τη συγκομιδή όλων των Little Sisters σε μια περιοχή, με μια ανατριχιαστική κραυγή να προειδοποιεί για την άφιξή τους.",
      "Είναι πολύ πιο γρήγορες και ευκίνητες από τα βαριά Big Daddies, σκαρφαλώνοντας σε τοίχους και εξαπολύοντας φωτιά και τηλεκίνηση."
    ],
    "source": "https://en.wikipedia.org/wiki/BioShock_2",
    "locale": "el-GR",
    "tags": ["bioshock-2", "big-sisters", "rapture", "irrational-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'medium', 3, questions)

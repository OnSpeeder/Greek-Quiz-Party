# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_easy_161",
    "text": "Ποια είναι η επίσημη φανταστική γλώσσα που μιλούν οι χαρακτήρες στη σειρά εξομοίωσης ζωής «The Sims»;",
    "answers": ["Simlish", "Esperanto", "Hylian", "Dothraki"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Simlish είναι μια τεχνητή γλώσσα αυτοσχεδιασμού που δημιουργήθηκε για να εκφράζει συναισθήματα χωρίς να απαιτείται μετάφραση σε διάφορες γλώσσες.",
    "funFacts": [
      "Διάσημοι καλλιτέχνες όπως η Katy Perry, οι My Chemical Romance και οι Depeche Mode έχουν ηχογραφήσει ειδικές εκδόσεις των τραγουδιών τους στα Simlish για το παιχνίδι.",
      "Η διάσημη λέξη χαιρετισμού στη Simlish είναι 'Sul Sul'."
    ],
    "source": "https://en.wikipedia.org/wiki/Simlish",
    "locale": "el-GR",
    "tags": ["the-sims", "simlish", "ea", "simulation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_162",
    "text": "Ποια μεγάλα κίτρινα πτηνά που μοιάζουν με στρουθοκαμήλους χρησιμεύουν ως υποζύγια και μασκότ στη σειρά «Final Fantasy»;",
    "answers": ["Moogles", "Chocobo (Τσόκομπο)", "Cactuars", "Tonberries"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Chocobo πρωτοεμφανίστηκαν στο Final Fantasy II (1988) και χρησιμοποιούνται για γρήγορες μετακινήσεις χωρίς τυχαίες μάχες.",
    "funFacts": [
      "Το χαρακτηριστικό μουσικό θέμα των Chocobo που συνέθεσε ο Nobuo Uematsu εμφανίζεται σε σχεδόν κάθε τίτλο της σειράς με διαφορετική ενορχήστρωση.",
      "Στο Final Fantasy VII, οι παίκτες μπορούν να εκτρέφουν και να διασταυρώνουν Chocobo διαφορετικών χρωμάτων για να αποκτήσουν το θρυλικό χρυσό Chocobo."
    ],
    "source": "https://en.wikipedia.org/wiki/Chocobo",
    "locale": "el-GR",
    "tags": ["final-fantasy", "chocobo", "square-enix", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_163",
    "text": "Ποιο κλασικό power-up επιτρέπει στον Mario να αλλάζει στολή και να εκτοξεύει πύρινες μπάλες εναντίον των εχθρών του;",
    "answers": ["Super Mushroom", "Super Leaf", "Fire Flower (Λουλούδι Φωτιάς)", "Ice Flower"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Fire Flower μεταμορφώνει τον Mario σε Fire Mario, αλλάζοντας τη στολή του σε λευκή μπλούζα με κόκκινη φόρμα και δίνοντάς του τη δυνατότητα εκτόξευσης φωτιάς.",
    "funFacts": [
      "Πρωτοεμφανίστηκε στο ιστορικό Super Mario Bros. (1985) για το NES.",
      "Είναι το μοναδικό επιθετικό power-up που εμφανίζεται σταθερά σχεδόν σε κάθε κύριο παιχνίδι Mario για πάνω από τέσσερις δεκαετίες."
    ],
    "source": "https://el.wikipedia.org/wiki/Super_Mario",
    "locale": "el-GR",
    "tags": ["mario", "fire-flower", "nintendo", "power-up"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_164",
    "text": "Ποιο είναι το προεπιλεγμένο όνομα του βασικού ανδρικού χαρακτήρα με το γαλάζιο μπλουζάκι στο «Minecraft»;",
    "answers": ["Alex", "Notch", "Herobrine", "Steve (Στιβ)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Steve είναι η αρχική προεπιλεγμένη εμφάνιση (skin) παίκτη στο Minecraft, σχεδιασμένος από τον Markus Persson.",
    "funFacts": [
      "Ο Notch του έδωσε αρχικά το όνομα 'Steve' ως αστείο, αλλά η κοινότητα το υιοθέτησε τόσο έντονα που έγινε επίσημο.",
      "Το 2014 προστέθηκε και η προεπιλεγμένη γυναικεία μορφή 'Alex', με πορτοκαλί μαλλιά και πράσινη μπλούζα."
    ],
    "source": "https://el.wikipedia.org/wiki/Minecraft",
    "locale": "el-GR",
    "tags": ["minecraft", "steve", "mojang", "sandbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_165",
    "text": "Ποια είναι η διάσημη σύζυγος του Pac-Man με τον κόκκινο φιόγκο στο κεφάλι και το κραγιόν που απέκτησε δικό της arcade παιχνίδι το 1982;",
    "answers": ["Ms. Pac-Man", "Lady Pac", "Pac-Girl", "Pac-Mom"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Ms. Pac-Man κυκλοφόρησε το 1982 από τη Midway και έγινε ένα από τα πιο επιτυχημένα αμερικανικά arcade παιχνίδια όλων των εποχών.",
    "funFacts": [
      "Το παιχνίδι ξεκίνησε ως ένα μη εξουσιοδοτημένο τροποποιημένο mod του Pac-Man με το όνομα 'Crazy Otto' πριν εξαγοραστεί επίσημα από τη Midway.",
      "Εισήγαγε τέσσερις διαφορετικούς λαβύρινθους με ποικίλα χρώματα και τυχαίες κινήσεις για τα φαντάσματα."
    ],
    "source": "https://en.wikipedia.org/wiki/Ms._Pac-Man",
    "locale": "el-GR",
    "tags": ["pac-man", "ms-pac-man", "arcade", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_166",
    "text": "Πόσα είναι τα θρυλικά Σμαράγδια του Χάους (Chaos Emeralds) που πρέπει να συγκεντρώσει ο Sonic the Hedgehog για να ξεκλειδώσει την απόλυτη δύναμή του;",
    "answers": ["Πέντε (5)", "Επτά (7)", "Έξι (6)", "Οκτώ (8)"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Στα κλασικά παιχνίδια Sonic υπάρχουν ακριβώς 7 Σμαράγδια του Χάους, τα οποία επιτρέπουν στον Sonic να μεταμορφωθεί σε Super Sonic.",
    "funFacts": [
      "Στο πρώτο παιχνίδι Sonic the Hedgehog (1991) για το Mega Drive υπήρχαν μόνο 6 σμαράγδια, με το έβδομο να προστίθεται στο Sonic 2.",
      "Τα σμαράγδια περιέχουν απεριόριστη μυστικιστική ενέργεια που μπορεί να τροφοδοτήσει τόσο θαύματα όσο και υπερόπλα μαζικής καταστροφής."
    ],
    "source": "https://el.wikipedia.org/wiki/Sonic_the_Hedgehog",
    "locale": "el-GR",
    "tags": ["sonic", "chaos-emeralds", "sega", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_167",
    "text": "Πώς ονομάζεται το εμβληματικό άλμα εμπιστοσύνης από ψηλά κτίρια μέσα σε κάρα με άχυρα στη σειρά «Assassin's Creed»;",
    "answers": ["Eagle Dive", "Swan Dive", "Leap of Faith (Άλμα Πίστης)", "Shadow Jump"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Leap of Faith είναι το σήμα κατατεθέν των Ασσασίνων, κατά το οποίο πηδούν από τεράστια ύψη συνοδευόμενοι από την κραυγή ενός αετού.",
    "funFacts": [
      "Εκτελείται συνήθως αμέσως μετά τον συγχρονισμό ενός ψηλού σημείου παρατήρησης (Viewpoint) στον χάρτη.",
      "Στα γυρίσματα της ταινίας Assassin's Creed (2016), ο κασκαντέρ Damien Walters πραγματοποίησε ένα πραγματικό ελεύθερο άλμα 38 μέτρων χωρίς καλώδια."
    ],
    "source": "https://el.wikipedia.org/wiki/Assassin%27s_Creed",
    "locale": "el-GR",
    "tags": ["assassins-creed", "leap-of-faith", "ubisoft", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_168",
    "text": "Ποιο χρώμα θεραπευτικού βοτάνου χρησιμοποιούν οι παίκτες για να ανακτήσουν τη χαμένη υγεία τους στη σειρά «Resident Evil»;",
    "answers": ["Μπλε βότανο", "Κίτρινο βότανο", "Μοβ βότανο", "Πράσινο βότανο (Green Herb)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το πράσινο βότανο (Green Herb) θεραπεύει τα τραύματα του παίκτη και μπορεί να συνδυαστεί με κόκκινο βότανο για πλήρη αποκατάσταση της υγείας.",
    "funFacts": [
      "Το μπλε βότανο (Blue Herb) χρησιμεύει για τη θεραπεία από το δηλητήριο των εχθρών.",
      "Ο συνδυασμός βοτάνων γίνεται μέσα στο σύστημα απογραφής (inventory) και τα μετατρέπει σε φαρμακευτική σκόνη ή δισκία."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident-evil", "green-herb", "capcom", "survival-horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_169",
    "text": "Από ποια ιστορική αρχαία ελληνική πόλη-κράτος κατάγεται ο Κράτος πριν γίνει ο νέος Θεός του Πολέμου;",
    "answers": ["Σπάρτη", "Αθήνα", "Κόρινθος", "Θήβα"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Κράτος ήταν στρατηγός του σπαρτιατικού στρατού, γνωστός ως 'Φάντασμα της Σπάρτης' (Ghost of Sparta) μετά τη σφαγή της οικογένειάς του.",
    "funFacts": [
      "Το λευκό χρώμα στο δέρμα του Κράτου οφείλεται στις στάχτες της συζύγου και της κόρης του, οι οποίες κόλλησαν μόνιμα στο σώμα του ως αιώνια κατάρα.",
      "Η κόκκινη λωρίδα-τατουάζ στο σώμα του έγινε προς τιμήν του αδελφού του, Δημοσθένη (Deimos), ο οποίος είχε γεννηθεί με παρόμοιο σημάδι."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(σειρά)",
    "locale": "el-GR",
    "tags": ["god-of-war", "kratos", "sparta", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_170",
    "text": "Ποιο είναι το πιο αναγνωρίσιμο τετράτροχο στρατιωτικό όχημα αναγνώρισης με περιστρεφόμενο πολυβόλο στη σειρά «Halo»;",
    "answers": ["Scorpion Tank", "Warthog (M12 FAV)", "Ghost", "Banshee"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Warthog είναι το ελαφρύ όχημα παντός εδάφους των δυνάμεων UNSC, σχεδιασμένο για έναν οδηγό, έναν συνοδηγό και έναν πολυβολητή.",
    "funFacts": [
      "Διαθέτει σύστημα διεύθυνσης και στους τέσσερις τροχούς (four-wheel steering), προσφέροντας εξαιρετική ευελιξία σε ανώμαλο έδαφος.",
      "Στην παρωδιακή διαδικτυακή σειρά 'Red vs. Blue', οι στρατιώτες διαφωνούν κωμικά αν το όχημα μοιάζει με φακόχοιρο (warthog) ή με πούμα."
    ],
    "source": "https://en.wikipedia.org/wiki/Warthog_(Halo)",
    "locale": "el-GR",
    "tags": ["halo", "warthog", "master-chief", "xbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_171",
    "text": "Πώς απεικονίζεται στην οθόνη το επίπεδο καταδίωξης του παίκτη από τις αστυνομικές αρχές στη σειρά «Grand Theft Auto»;",
    "answers": ["Με σφαίρες", "Με σειρήνες περιπολικού", "Με αστέρια (Stars)", "Με χειροπέδες"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το 'Wanted Level' μετριέται με αστέρια (από 1 έως 5 ή 6 αστέρια ανάλογα με τον τίτλο), καθορίζοντας την επιθετικότητα και τις δυνάμεις της αστυνομίας.",
    "funFacts": [
      "Στο μέγιστο επίπεδο αστέρων, ο στρατός και οι ειδικές δυνάμεις (SWAT/NOOSE) επεμβαίνουν με τανκς και στρατιωτικά ελικόπτερα.",
      "Στα πρώτα παιχνίδια GTA υπήρχαν 6 αστέρια καταδίωξης, αλλά στο GTA V το όριο μειώθηκε σε 5 αστέρια."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto",
    "locale": "el-GR",
    "tags": ["gta", "wanted-level", "rockstar-games", "open-world"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_172",
    "text": "Πώς ονομάζεται η κλασική σφαιρική συσκευή με κόκκινο καπάκι και λευκή βάση που χρησιμοποιείται για τη σύλληψη των Pokémon;",
    "answers": ["Great Ball", "Ultra Ball", "Master Ball", "Poké Ball"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Poké Ball είναι το βασικό εργαλείο κάθε εκπαιδευτή, συρρικνώνοντας και αποθηκεύοντας τα πλάσματα Pokémon με ασφάλεια.",
    "funFacts": [
      "Η πιο σπάνια και ισχυρή μπάλα είναι η Master Ball, η οποία έχει 100% πιθανότητα επιτυχίας και δεν αποτυγχάνει ποτέ.",
      "Σύμφωνα με τη μυθολογία των παιχνιδιών, οι αρχαίοι εκπαιδευτές κατασκεύαζαν χειροποίητες μπάλες από τους καρπούς των δέντρων Apricorn."
    ],
    "source": "https://el.wikipedia.org/wiki/Pok%C3%A9mon",
    "locale": "el-GR",
    "tags": ["pokemon", "poke-ball", "nintendo", "kanto"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_173",
    "text": "Πώς ονομάζονται οι διάσημες θεαματικές και βίαιες κινήσεις αποτελειώματος στο τέλος κάθε αγώνα στη σειρά «Mortal Kombat»;",
    "answers": ["Fatalities", "Ultra Combos", "Critical Arts", "Destruction Moves"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Fatalities είναι ειδικές ακολουθίες κουμπιών που εκτελούνται μετά την εντολή 'Finish Him!', χαρίζοντας στον νικητή μια μοναδική σκηνή εξόντωσης.",
    "funFacts": [
      "Σε επόμενα παιχνίδια εισήχθησαν και χιουμοριστικές παραλλαγές, όπως τα 'Babalities' (που μετατρέπουν τον αντίπαλο σε μωρό) και τα 'Friendships'.",
      "Η ανακάλυψη των συνδυασμών Fatality στα arcades της δεκαετίας του '90 διαδιδόταν από στόμα σε στόμα και μέσω περιοδικών σαν μυστικός κώδικας."
    ],
    "source": "https://el.wikipedia.org/wiki/Mortal_Kombat",
    "locale": "el-GR",
    "tags": ["mortal-kombat", "fatality", "fighting", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_174",
    "text": "Ποιο ήταν το κλασικό χαρακτηριστικό ζευγάρι πυροβόλων όπλων που κρατούσε η Lara Croft στις αρχικές περιπέτειες του «Tomb Raider»;",
    "answers": ["Δίδυμες καραμπίνες", "Δίδυμα πιστόλια 9mm (Dual Pistols)", "Τόξο και βέλη", "Δίδυμα περίστροφα"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα διπλά ημιαυτόματα πιστόλια Browning Hi-Power με τις θήκες στους μηρούς αποτέλεσαν το απόλυτο οπτικό σήμα κατατεθέν της Lara Croft.",
    "funFacts": [
      "Στα κλασικά παιχνίδια, τα δίδυμα πιστόλια είχαν άπειρα πυρομαχικά, επιτρέποντας στους παίκτες να πυροβολούν ασταμάτητα κάνοντας ακροβατικά άλματα.",
      "Στο reboot του 2013, η Lara Croft απέκτησε ως κύριο όπλο το ορειβατικό τόξο, αντανακλώντας έναν πιο ρεαλιστικό τόνο επιβίωσης."
    ],
    "source": "https://el.wikipedia.org/wiki/Tomb_Raider",
    "locale": "el-GR",
    "tags": ["tomb-raider", "lara-croft", "weapons", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_175",
    "text": "Ποιο είναι το όνομα της πιστής καφέ φοράδας που ιππεύει ο Link στο «The Legend of Zelda: Ocarina of Time»;",
    "answers": ["Zelda", "Midna", "Έπονα (Epona)", "Saria"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Epona είναι το άλογο του Link, το οποίο μεγαλώνει στο Lon Lon Ranch και καλείται από τον ήρωα παίζοντας το 'Epona's Song' στην οκαρίνα.",
    "funFacts": [
      "Πήρε το όνομά της από την Έπονα, την αρχαία κελτική θεότητα των αλόγων και της γονιμότητας.",
      "Η ίππευση της Epona επέτρεψε στους παίκτες να διασχίζουν γρήγορα την τεράστια πεδιάδα του Hyrule και να πηδούν φράχτες."
    ],
    "source": "https://en.wikipedia.org/wiki/Epona_(The_Legend_of_Zelda)",
    "locale": "el-GR",
    "tags": ["zelda", "epona", "link", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_176",
    "text": "Ποια μικρά αμφίβια πλάσματα που μοιάζουν με ψάρια βγάζουν τον χαρακτηριστικό γαργαριστό ήχο «Rwlrwlrwlrwl» στο «World of Warcraft»;",
    "answers": ["Gnolls", "Kobolds", "Troggs", "Murlocs"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι Murlocs είναι επιθετικά αμφίβια ανθρωποειδή που ζουν στις ακτές του Azeroth και επιτίθενται πάντα μαζικά σε ομάδες.",
    "funFacts": [
      "Ο χαρακτηριστικός τους ήχος δημιουργήθηκε από τον ηχολήπτη της Blizzard που έκανε γαργάρες με γιαούρτι μπροστά στο μικρόφωνο.",
      "Έχουν γίνει επίσημη μασκότ της Blizzard, εμπνέοντας λούτρινα παιχνίδια, κατοικίδια και το τραγούδι 'I Am Murloc' της εσωτερικής μπάντας L70ETC."
    ],
    "source": "https://en.wikipedia.org/wiki/Murloc",
    "locale": "el-GR",
    "tags": ["warcraft", "murloc", "blizzard", "mmorpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_177",
    "text": "Τι είδους ενέργεια εκτοξεύουν από τις παλάμες τους οι Ryu και Ken όταν φωνάζουν «Hadoken» στο «Street Fighter»;",
    "answers": ["Μια συμπυκνωμένη σφαίρα πνευματικής ενέργειας (Ki blast)", "Μια βολίδα πάγου", "Μια δέσμη λέιζερ", "Ένα ηλεκτρικό βέλος"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Hadoken (Κυματική Γροθιά Κίνησης) συγκεντρώνει την πνευματική ενέργεια (chi/ki) του μαχητή ανάμεσα στις παλάμες του και την εκτοξεύει προς τα εμπρός.",
    "funFacts": [
      "Είναι η πιο αναγνωρίσιμη ειδική κίνηση στην ιστορία των fighting games, εκτελούμενη με τον συνδυασμό: Κάτω, Κάτω-Μπροστά, Μπροστά + Γροθιά.",
      "Σε διάφορα παιχνίδια της Capcom, ακόμα και ο Mega Man μπορεί να αποκτήσει το Hadoken ως κρυφό μυστικό όπλο."
    ],
    "source": "https://en.wikipedia.org/wiki/Hadoken",
    "locale": "el-GR",
    "tags": ["street-fighter", "hadoken", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_178",
    "text": "Τι είδους ζώο είναι ο χαλαρός μουσικός K.K. Slider που εμφανίζεται με την ακουστική του κιθάρα στη σειρά «Animal Crossing»;",
    "answers": ["Γάτα", "Σκύλος (Jack Russell)", "Αρκούδα", "Κουνέλι"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο K.K. Slider (Totakeke στην Ιαπωνία) είναι ένας λευκός σκύλος μουσικός που ταξιδεύει και χαρίζει δίσκους με τη μουσική του στους παίκτες.",
    "funFacts": [
      "Βασίζεται στον πραγματικό συνθέτη της Nintendo Kazumi Totaka, ο οποίος έγραψε τη μουσική για το Animal Crossing και χάρισε το όνομά του στον ήρωα.",
      "Υπάρχουν δεκάδες διαφορετικά τραγούδια του K.K. Slider που οι παίκτες μπορούν να αναπαράγουν στα ραδιόφωνα των σπιτιών τους."
    ],
    "source": "https://en.wikipedia.org/wiki/K.K._Slider",
    "locale": "el-GR",
    "tags": ["animal-crossing", "kk-slider", "nintendo", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_179",
    "text": "Ποια μικρά τετράποδα εξωγήινα παράσιτα πηδούν στα κεφάλια των ανθρώπων και τους μετατρέπουν σε ζόμπι στη σειρά «Half-Life»;",
    "answers": ["Facehuggers", "Vortigaunts", "Headcrabs", "Snarks"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Headcrabs προέρχονται από τη συνοριακή διάσταση Xen και προσκολλώνται στο κρανίο των θυμάτων τους, αναλαμβάνοντας τον έλεγχο του νευρικού τους συστήματος.",
    "funFacts": [
      "Ο επιστήμονας Dr. Isaac Kleiner στο Half-Life 2 έχει εξημερώσει ένα ακίνδυνο αποπτερωμένο Headcrab ως κατοικίδιο, ονόματι 'Lamarr'.",
      "Εκτός από τα κοινά Headcrabs, υπάρχουν παραλλαγές Fast Headcrabs και Poison Headcrabs με μαύρο χρώμα και νευροτοξίνες."
    ],
    "source": "https://en.wikipedia.org/wiki/Headcrab",
    "locale": "el-GR",
    "tags": ["half-life", "headcrab", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_180",
    "text": "Ποιος πιστός μεταλλικός κύβος με μια ροζ καρδιά στη μέση συνοδεύει την Chell στο Chamber 17 του «Portal»;",
    "answers": ["Weighted Storage Cube", "Energy Sphere", "Edgeless Safety Cube", "Weighted Companion Cube"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Weighted Companion Cube βοηθά την Chell να λύσει τους γρίφους του επιπέδου, πριν η GLaDOS την αναγκάσει να τον ρίξει σε έναν αποτεφρωτήρα.",
    "funFacts": [
      "Η υποχρεωτική αποτέφρωση του Companion Cube αποτελεί μία από τις πιο συναισθηματικά φορτισμένες και κωμικές στιγμές στο gaming.",
      "Η GLaDOS ισχυρίζεται σαρκαστικά στα μεγάφωνα ότι ο κύβος 'δεν μπορεί να μιλήσει' και ότι τυχόν ψίθυροι είναι προϊόν παραισθήσεων του παίκτη."
    ],
    "source": "https://en.wikipedia.org/wiki/Portal_(video_game)",
    "locale": "el-GR",
    "tags": ["portal", "companion-cube", "valve", "glados"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_181",
    "text": "Ποια πρώην επαγγελματίας παίκτρια esports από τη Νότια Κορέα πιλοτάρει ένα ροζ πολεμικό ρομπότ (mech) στο «Overwatch»;",
    "answers": ["D.Va (Hana Song)", "Mei", "Pharah", "Widowmaker"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Hana Song (γνωστή ως D.Va) επιστρατεύτηκε από τον στρατό της Νότιας Κορέας (MEKA) για να χειριστεί πολεμικά ρομπότ χάρη στα αστραπιαία της ανακλαστικά.",
    "funFacts": [
      "Η απόλυτη ικανότητά της (Self-Destruct) της επιτρέπει να υπερφορτώσει τον αντιδραστήρα του mech της φωνάζοντας 'Nerf this!' και προκαλώντας τεράστια έκρηξη.",
      "Εάν το ρομπότ της καταστραφεί, η D.Va εκτοξεύεται αυτόματα έξω και συνεχίζει να μάχεται με πιστόλι λέιζερ μέχρι να καλέσει νέο mech."
    ],
    "source": "https://el.wikipedia.org/wiki/Overwatch",
    "locale": "el-GR",
    "tags": ["overwatch", "dva", "blizzard", "hero-shooter"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_182",
    "text": "Ποιο μικροσκοπικό γούνινο πλάσμα Yordle φυτεύει αόρατα δηλητηριώδη μανιτάρια στους διαδρόμους του «League of Legends»;",
    "answers": ["Gnar", "Teemo", "Kennen", "Ziggs"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Teemo (The Swift Scout) χρησιμοποιεί φυσοκάλαμο με δηλητηριώδη βέλη και παγιδεύει τον χάρτη με εκρηκτικά μανιτάρια που επιβραδύνουν τους εχθρούς.",
    "funFacts": [
      "Είναι ένας από τους πιο αμφιλεγόμενους χαρακτήρες στην ιστορία του παιχνιδιού, αγαπητός για τη χαριτωμένη του εμφάνιση αλλά μισητός στους αντιπάλους για τα ενοχλητικά του μανιτάρια.",
      "Η παθητική του ικανότητα του επιτρέπει να γίνεται εντελώς αόρατος εάν παραμείνει ακίνητος για λίγα δευτερόλεπτα."
    ],
    "source": "https://el.wikipedia.org/wiki/League_of_Legends",
    "locale": "el-GR",
    "tags": ["league-of-legends", "teemo", "riot-games", "moba"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_183",
    "text": "Ποιο λαμπερό αντικείμενο χαρίζει στον Mario προσωρινή απόλυτη ατρωσία και αυξημένη ταχύτητα ενώ αλλάζει συνεχώς χρώματα;",
    "answers": ["Super Mushroom", "Fire Flower", "Super Star (Starman)", "Power Moon"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Super Star κάνει τον Mario ανίκητο απέναντι σε κάθε εχθρικό άγγιγμα, εξουδετερώνοντας τους αντιπάλους με ένα απλό πέρασμα.",
    "funFacts": [
      "Όταν ο Mario αποκτά το αστέρι, παίζει μια ταχύτατη χαρακτηριστική μουσική που σηματοδοτεί τη σύντομη διάρκεια της ατρωσίας του.",
      "Παρά την απόλυτη ατρωσία απέναντι στους εχθρούς, ο Mario εξακολουθεί να χάνει ζωή εάν πέσει σε γκρεμό ή σε λάβα."
    ],
    "source": "https://el.wikipedia.org/wiki/Super_Mario",
    "locale": "el-GR",
    "tags": ["mario", "super-star", "nintendo", "power-up"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_184",
    "text": "Πώς ονομάζεται η ικανότητα αργής κίνησης (slow-motion) που επιτρέπει στον παίκτη να σημαδεύει πολλαπλούς στόχους στο «Red Dead Redemption»;",
    "answers": ["Bullet Time", "Eagle Vision", "Focus Mode", "Dead Eye"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Dead Eye επιβραδύνει τον χρόνο, επιτρέποντας στον Arthur Morgan και τον John Marston να μαρκάρουν στόχους με ακρίβεια και να πυροβολούν αστραπιαία.",
    "funFacts": [
      "Ο μηχανισμός Dead Eye αντλεί άμεση έμπνευση από τις κλασικές ταινίες σπαγγέτι γουέστερν του Sergio Leone.",
      "Σε υψηλότερα επίπεδα, το Dead Eye αποκαλύπτει τα κρίσιμα ζωτικά σημεία των ανθρώπων και των ζώων (όπως η καρδιά και ο εγκέφαλος) με κόκκινο χρώμα."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "dead-eye", "rockstar-games", "western"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_185",
    "text": "Πώς αποκαλείται στη δρακογλώσσα ο θρυλικός ήρωας που γεννήθηκε με σώμα θνητού αλλά ψυχή δράκου στο «Skyrim»;",
    "answers": ["Dovahkiin", "Alduin", "Paarthurnax", "Ysgramor"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Dovahkiin (Dragonborn / Δρακογέννητος) είναι ο προφητευμένος ήρωας που μπορεί να απορροφά τις ψυχές των δράκων και να χρησιμοποιεί τη φωνή τους (Thu'um).",
    "funFacts": [
      "Η διάσημη χορωδιακή μουσική του τίτλου 'Dragonborn Theme' ηχογραφήθηκε από χορωδία τριάντα ανδρών που τραγουδούσαν στη φανταστική γλώσσα των δράκων.",
      "Η λέξη Dovahkiin αναλύεται σε 'Dovah' (δράκος) και 'Kiin' (γεννημένος/παιδί)."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "locale": "el-GR",
    "tags": ["skyrim", "dovahkiin", "dragonborn", "bethesda"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_186",
    "text": "Ποιο μέλος του σώματος του επαναστάτη Johnny Silverhand στο «Cyberpunk 2077» είναι κατασκευασμένο από λαμπερό μέταλλο, χαρίζοντάς του το παρατσούκλι του;",
    "answers": ["Το δεξί του πόδι", "Το αριστερό του χέρι (κυβερνο-βραχίονας)", "Το σαγόνι του", "Το δεξί του μάτι"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Johnny Silverhand απέκτησε το ασημένιο κυβερνητικό χέρι μετά τον ακρωτηριασμό του κατά τη διάρκεια των πολέμων των εταιρειών.",
    "funFacts": [
      "Είναι ο τραγουδιστής και κιθαρίστας του θρυλικού ροκ συγκροτήματος 'Samurai'.",
      "Τον ρόλο του υποδύεται ο Keanu Reeves, ο οποίος ηχογράφησε δεκάδες ώρες διαλόγων για την εικονική περσόνα του Johnny μέσα στο μυαλό του πρωταγωνιστή V."
    ],
    "source": "https://el.wikipedia.org/wiki/Cyberpunk_2077",
    "locale": "el-GR",
    "tags": ["cyberpunk-2077", "johnny-silverhand", "keanu-reeves", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_187",
    "text": "Ποια ζουμερά τροπικά φρούτα που μοιάζουν με μήλα συλλέγει κατά εκατοντάδες ο Crash Bandicoot στις πίστες του;",
    "answers": ["Μπανάνες", "Καρύδες", "Φρούτα Γούμπα (Wumpa Fruit)", "Μάνγκο"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Wumpa Fruit είναι τα πορτοκαλοκόκκινα φρούτα που τρώει ο Crash. Κάθε φορά που μαζεύει 100 φρούτα, κερδίζει αυτόματα μία επιπλέον ζωή.",
    "funFacts": [
      "Σε διάφορα παιχνίδια της σειράς, ο Crash χρησιμοποιεί ένα μπαζούκα που εκτοξεύει φρούτα Wumpa εναντίον των εχθρών του.",
      "Παρόλο που μοιάζουν με μήλα ή μάνγκο, οι δημιουργοί δήλωσαν ότι έχουν γεύση παρόμοια με ροδάκινο και μήλο μαζί."
    ],
    "source": "https://el.wikipedia.org/wiki/Crash_Bandicoot",
    "locale": "el-GR",
    "tags": ["crash-bandicoot", "wumpa-fruit", "naughty-dog", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_188",
    "text": "Ποιο είναι το χαρακτηριστικό όπλο παγίδευσης που τοποθετεί στο έδαφος ο Trapper, ο πρώτος δολοφόνος του «Dead by Daylight»;",
    "answers": ["Νάρκες ξηράς", "Συρματοπλέγματα", "Λάκκους με καρφιά", "Παγίδες για αρκούδες (Bear Traps)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Evan MacMillan (The Trapper) τοποθετεί μεγάλες ατσάλινες παγίδες για αρκούδες στο γρασίδι, ακινητοποιώντας και τραυματίζοντας τους επιζώντες.",
    "funFacts": [
      "Ο Trapper ήταν ο πρώτος δολοφόνος που σχεδιάστηκε για το παιχνίδι και αποτελεί το πρόσωπο του εξωφύλλου του Dead by Daylight.",
      "Εάν ο Trapper δεν προσέξει, μπορεί κατά λάθος να πατήσει ο ίδιος πάνω σε μια δική του παγίδα και να ακινητοποιηθεί για λίγα δευτερόλεπτα."
    ],
    "source": "https://en.wikipedia.org/wiki/Dead_by_Daylight",
    "locale": "el-GR",
    "tags": ["dead-by-daylight", "trapper", "horror", "multiplayer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_189",
    "text": "Ποιος ευδιάθετος πολεμιστής του ήλιου προτρέπει τους παίκτες στο «Dark Souls» να υμνούν το φως με τη διάσημη πόζα «Praise the Sun!»;",
    "answers": ["Solaire of Astora", "Siekmeyer of Catarina", "Andre of Astora", "Lautrec of Carim"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Solaire of Astora είναι μέλος της διαθήκης Warriors of Sunlight και βοηθά τον παίκτη ως σύμμαχος σε πολλές δύσκολες μάχες με αφεντικά.",
    "funFacts": [
      "Η χαρακτηριστική του πόζα με τα χέρια υψωμένα σε σχήμα V προς τον ουρανό έγινε το πιο αγαπητό meme στην κοινότητα των παιχνιδιών FromSoftware.",
      "Αναζητά με εμμονή τον 'δικό του ήλιο' μέσα στον σκοτεινό και απελπισμένο κόσμο του Lordran."
    ],
    "source": "https://en.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "solaire", "fromsoftware", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_190",
    "text": "Σε ποια εξωγήινη φυλή με εξωσκελετό και αυστηρή στρατιωτική ιεραρχία ανήκει ο πιστός σύντροφος του Shepard, Garrus Vakarian, στο «Mass Effect»;",
    "answers": ["Asari", "Turian (Τούριαν)", "Krogan", "Salarian"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Garrus είναι ένας Turian πρώην αξιωματικός της C-Sec στην Ακρόπολη (Citadel), ο οποίος εξελίσσεται στον πιο πιστό φίλο του Commander Shepard.",
    "funFacts": [
      "Στο Mass Effect 2, ο Garrus δρα ως μασκοφόρος εκδικητής στον σταθμό Omega με το ψευδώνυμο 'Archangel'.",
      "Η αγαπημένη του ασχολία πάνω στο Normandy είναι να 'καλιμπράρει' (calibrating) τα πυροβόλα κανόνια του σκάφους."
    ],
    "source": "https://en.wikipedia.org/wiki/Garrus_Vakarian",
    "locale": "el-GR",
    "tags": ["mass-effect", "garrus", "turian", "bioware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_191",
    "text": "Σε ποια σκοτεινή φιγούρα χρωστούν τις ψυχές τους ο Cuphead και ο Mugman αφού έχασαν τα πάντα στα ζάρια στο καζίνο;",
    "answers": ["Στον King Dice", "Στον Captain Brineybeard", "Στον Διάβολο (The Devil)", "Στον Cagney Carnation"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Cuphead τζόγαρε τις ψυχές τους στο Devil's Casino και αναγκάστηκε να δεχτεί τη συμφωνία να εισπράξει τα συμβόλαια ψυχών άλλων οφειλετών για να σωθούν.",
    "funFacts": [
      "Ο Διάβολος λειτουργεί ως το τελικό αφεντικό (final boss) του παιχνιδιού, έχοντας ως δεξί του χέρι τον King Dice.",
      "Ο σχεδιασμός του είναι εμπνευσμένος από τους διαβόλους των κλασικών κινουμένων σχεδίων των Fleischer Studios και της Disney της δεκαετίας του 1930."
    ],
    "source": "https://el.wikipedia.org/wiki/Cuphead",
    "locale": "el-GR",
    "tags": ["cuphead", "the-devil", "studio-mdhr", "indie"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_192",
    "text": "Τι πρέπει να αρπάξει πρώτος ένας παίκτης στον τελικό γύρο του «Fall Guys» για να κερδίσει την αναμέτρηση;",
    "answers": ["Ένα χρυσό τρόπαιο", "Ένα χρυσό αυγό", "Ένα μαγικό δαχτυλίδι", "Το Στέμμα (Crown)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Στις τελικές πίστες όπως το Fall Mountain, οι φιναλίστ διαγωνίζονται σε μια κούρσα εμποδίων για να πηδήξουν και να αρπάξουν το αιωρούμενο χρυσό Στέμμα.",
    "funFacts": [
      "Τα στέμματα που κερδίζουν οι παίκτες χρησιμοποιούνται ως ειδικό νόμισμα (Crown Rank) για το ξεκλείδωμα σπάνιων εμφανίσεων.",
      "Πολλοί νέοι παίκτες κάνουν το λάθος να πέσουν με άλμα πάνω στο στέμμα χωρίς να πατήσουν το κουμπί αρπαγής, χάνοντας τη νίκη."
    ],
    "source": "https://el.wikipedia.org/wiki/Fall_Guys",
    "locale": "el-GR",
    "tags": ["fall-guys", "crown", "mediatonic", "battle-royale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_193",
    "text": "Ποια αγαπημένη τροφή κλέβει ο μοχθηρός κροκόδειλος King K. Rool από την αποθήκη του Donkey Kong;",
    "answers": ["Μπανάνες", "Καρύδες", "Φιστίκια", "Ανανάδες"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο King K. Rool και ο στρατός του από Kremlings κλέβουν την τεράστια συλλογή από μπανάνες (Banana Hoard) του Donkey Kong, ξεκινώντας την περιπέτεια.",
    "funFacts": [
      "Η συλλογή 100 μπανανών στις πίστες του Donkey Kong Country ανταμείβει τον παίκτη με μία επιπλέον ζωή (Extra Life).",
      "Ο Donkey Kong διαθέτει ειδικές χρυσές μπανάνες στο τρισδιάστατο Donkey Kong 64, οι οποίες απαιτούν την επίλυση γρίφων για να συλλεχθούν."
    ],
    "source": "https://el.wikipedia.org/wiki/Donkey_Kong",
    "locale": "el-GR",
    "tags": ["donkey-kong", "bananas", "nintendo", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_194",
    "text": "Πώς ονομάζεται το επίσημο ψηφιακό νόμισμα του «Fortnite» που χρησιμοποιείται για την αγορά εμφανίσεων (skins) και του Battle Pass;",
    "answers": ["Fortbucks", "V-Bucks", "Epic Coins", "Battle Points"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα V-Bucks (Vindertech Bucks) είναι το εσωτερικό νόμισμα του Fortnite, με το οποίο οι παίκτες αποκτούν αισθητικά αντικείμενα και χορούς (emotes).",
    "funFacts": [
      "Το όνομα 'V-Bucks' προέρχεται από την εταιρεία Vindertech στο αρχικό PvE mode του παιχνιδιού, 'Fortnite: Save the World'.",
      "Τα αντικείμενα που αγοράζονται με V-Bucks είναι καθαρά κοσμητικά και δεν προσφέρουν κανένα ανταγωνιστικό πλεονέκτημα στις μάχες."
    ],
    "source": "https://el.wikipedia.org/wiki/Fortnite",
    "locale": "el-GR",
    "tags": ["fortnite", "v-bucks", "epic-games", "battle-royale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_195",
    "text": "Τι πίνουν οι πειρατές από τα κύπελλά τους στα πανδοχεία του «Sea of Thieves» που τους κάνει να παραπατούν και να ξερνούν κωμικά;",
    "answers": ["Ρούμι", "Κρασί των ναυτικών", "Γκρογκ (Grog)", "Μπύρα τζίντζερ"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Grog είναι το παραδοσιακό ποτό των πειρατών στο Sea of Thieves. Όταν ο παίκτης πιει πάνω από ένα ποτήρι, η οθόνη θολώνει και ο χαρακτήρας χάνει την ισορροπία του.",
    "funFacts": [
      "Οι παίκτες μπορούν να μαζέψουν τον εμετό τους σε έναν κουβά και να τον πετάξουν σε εχθρούς για να τους τυφλώσουν προσωρινά.",
      "Το σεντούκι 'Chest of a Thousand Grogs' κάνει όποιον το κουβαλά να παραπατά συνεχώς σαν να είναι βαριά μεθυσμένος."
    ],
    "source": "https://en.wikipedia.org/wiki/Sea_of_Thieves",
    "locale": "el-GR",
    "tags": ["sea-of-thieves", "grog", "rare", "pirates"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_196",
    "text": "Ποιος μουστακαλής βετεράνος κυνηγός θησαυρών με το πούρο είναι ο μέντορας και πιστός φίλος του Nathan Drake στη σειρά «Uncharted»;",
    "answers": ["Harry Flynn", "Rafe Adler", "Gabriel Roman", "Victor 'Sully' Sullivan"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Victor Sullivan (Sully) γνώρισε τον Drake όταν ήταν ακόμη έφηβος κλέφτης στην Κολομβία και έγινε ο προστάτης, συνεργάτης και πατρική του φιγούρα.",
    "funFacts": [
      "Ο Sully διαθέτει ένα χαρακτηριστικό κίτρινο αμφίβιο αεροσκάφος Grumman Goose, το οποίο καταστρέφεται σχεδόν σε κάθε περιπέτεια.",
      "Στην κινηματογραφική ταινία Uncharted (2022), τον ρόλο του Victor Sullivan υποδύθηκε ο Mark Wahlberg."
    ],
    "source": "https://en.wikipedia.org/wiki/Victor_Sullivan",
    "locale": "el-GR",
    "tags": ["uncharted", "sully", "naughty-dog", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_197",
    "text": "Ποιο είναι το βασικό παραδοσιακό όπλο κοντινής μάχης που κρατά ο σιωπηλός ιππότης στο indie αριστούργημα «Hollow Knight»;",
    "answers": ["Καρφί (Nail)", "Βελόνι (Needle)", "Σπαθί", "Δόρυ"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Nail είναι το παραδοσιακό σπαθί των εντόμων στο Hallownest, το οποίο ο παίκτης μπορεί να αναβαθμίσει στον σιδηρουργό Nailsmith.",
    "funFacts": [
      "Ο παίκτης μπορεί να χτυπήσει προς τα κάτω με το Nail πάνω σε εχθρούς ή αγκάθια (μηχανισμός 'pogo') για να αναπηδά στον αέρα.",
      "Η ηρωίδα Hornet κρατά ένα διαφορετικό όπλο που ονομάζεται 'Needle' (Βελόνι) και συνδέεται με μεταξωτή κλωστή."
    ],
    "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
    "locale": "el-GR",
    "tags": ["hollow-knight", "nail", "indie", "metroidvania"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_198",
    "text": "Πόσα δευτερόλεπτα χρειάζονται κανονικά για να εκραγεί το εκρηκτικό C4 αφού τοποθετηθεί σε έναν αγώνα ανταγωνιστικού «Counter-Strike»;",
    "answers": ["30 δευτερόλεπτα", "40 δευτερόλεπτα", "50 δευτερόλεπτα", "60 δευτερόλεπτα"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο χρονοδιακόπτης της βόμβας C4 στο ανταγωνιστικό Counter-Strike είναι ρυθμισμένος ακριβώς στα 40 δευτερόλεπτα, δίνοντας περιθώριο στους Αντιτρομοκράτες να την εξουδετερώσουν.",
    "funFacts": [
      "Η απλή εξουδετέρωση της βόμβας διαρκεί 10 δευτερόλεπτα, αλλά εάν ο παίκτης διαθέτει κιτ απενεργοποίησης (Defuse Kit) ο χρόνος μειώνεται σε μόλις 5 δευτερόλεπτα.",
      "Ο ήχος των μπιπ του C4 επιταχύνει διαρκώς όσο πλησιάζει η στιγμή της έκρηξης, δημιουργώντας τεράστια ψυχολογική πίεση στους παίκτες."
    ],
    "source": "https://el.wikipedia.org/wiki/Counter-Strike",
    "locale": "el-GR",
    "tags": ["counter-strike", "c4", "valve", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_199",
    "text": "Ποιο τρομακτικό μολυσμένο πλάσμα κλαίει στο σκοτάδι και εξαπολύει φονική επίθεση αν ενοχληθεί από φακούς στο «Left 4 Dead»;",
    "answers": ["Hunter", "Smoker", "Witch (Μάγισσα)", "Boomer"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Witch είναι ένα εξαιρετικά επικίνδυνο Special Infected που κάθεται στο πάτωμα κλαίγοντας, αλλά εάν τρομάξει από φως ή πυρά επιτίθεται αστραπιαία ρίχνοντας τον παίκτη με ένα χτύπημα.",
    "funFacts": [
      "Οι παίκτες συμβουλεύονται να σβήνουν τους φακούς τους και να περνούν σκυφτοί από δίπλα της για να μην την 'εξοργίσουν' (startle).",
      "Έμπειροι παίκτες χρησιμοποιούν την τεχνική 'crashing', εξοντώνοντας τη Witch με έναν άμεσο πυροβολισμό καραμπίνας εξ επαφής στο κεφάλι."
    ],
    "source": "https://el.wikipedia.org/wiki/Left_4_Dead",
    "locale": "el-GR",
    "tags": ["left-4-dead", "witch", "valve", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_200",
    "text": "Πώς ονομάζεται το ταυτόχρονο καθάρισμα τεσσάρων οριζόντιων γραμμών με ένα και μόνο μακρόστενο τουβλάκι τεσσάρων τετραγώνων στο «Tetris»;",
    "answers": ["Strike", "Combo", "Quadra", "Tetris"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το να πετύχει ο παίκτης 'Tetris' (καθαρίζοντας 4 γραμμές ταυτόχρονα με το μακρύ κυανό κομμάτι I-tetromino) προσφέρει τους περισσότερους πόντους στο παιχνίδι.",
    "funFacts": [
      "Στο σύγχρονο αγωνιστικό Tetris, η τεχνική των διαδοχικών Tetris ('Back-to-Back Tetris') αποτελεί την κορυφαία στρατηγική επίθεσης.",
      "Το 2024, ο 13χρονος Willis Gibson (Blue Scuti) έγινε ο πρώτος άνθρωπος στην ιστορία που 'τερμάτισε' το αρχικό NES Tetris προκαλώντας crash στο παιχνίδι στο επίπεδο 157."
    ],
    "source": "https://el.wikipedia.org/wiki/Tetris",
    "locale": "el-GR",
    "tags": ["tetris", "puzzle", "retro-gaming", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_201",
    "text": "Ποιο είναι το χαρακτηριστικό χρώμα των παπουτσιών που φοράει πάντα ο Sonic the Hedgehog;",
    "answers": ["Κόκκινα παπούτσια με λευκή λωρίδα", "Μπλε αθλητικά παπούτσια", "Κίτρινα μποτάκια", "Καθαρά λευκά sneakers"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Sonic φοράει τα εμβληματικά κόκκινα αθλητικά παπούτσια με τη λευκή λωρίδα και τη χρυσή αγκράφα, εμπνευσμένα από τις μπότες του Michael Jackson.",
    "funFacts": [
      "Ο σχεδιαστής Naoto Ohshima εμπνεύστηκε το κόκκινο χρώμα των παπουτσιών από το εξώφυλλο του άλμπουμ 'Bad' του Michael Jackson και τη στολή του Άγιου Βασίλη.",
      "Στο παιχνίδι Sonic Adventure 2, ο Sonic αποκτά τα ειδικά παπούτσια 'Soap Shoes' που του επιτρέπουν να γλιστράει πάνω σε σιδηροδρομικές ράγες (rail grinding)."
    ],
    "source": "https://el.wikipedia.org/wiki/Sonic_the_Hedgehog",
    "locale": "el-GR",
    "tags": ["sonic", "sega", "shoes", "mascot"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_202",
    "text": "Ποιο τρομακτικό πρώιμο αφεντικό στο αρχικό «Diablo» (1997) κατατρομοκρατούσε τους παίκτες φωνάζοντας «Ah, fresh meat!»;",
    "answers": ["The Skeleton King", "The Butcher (Ο Χασάπης)", "Lazarus", "Diablo"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Butcher είναι ένας γιγάντιος αιμοδιψής δαίμονας με μπαλτά κρεοπώλη που περιμένει σε ένα δωμάτιο γεμάτο ακρωτηριασμένα πτώματα στο δεύτερο επίπεδο των κατακομβών.",
    "funFacts": [
      "Η ατάκα του 'Ah, fresh meat!' ('Αχ, φρέσκο κρέας!') έγινε μία από τις πιο διάσημες φράσεις στην ιστορία της Blizzard.",
      "Επανεμφανίζεται ως τρομακτικό τυχαίο boss στο Diablo III και Diablo IV, εισβάλλοντας απροειδοποίητα στα dungeons των παικτών."
    ],
    "source": "https://en.wikipedia.org/wiki/Diablo_(video_game)",
    "locale": "el-GR",
    "tags": ["diablo", "the-butcher", "blizzard", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_203",
    "text": "Ποια εφιαλτική, καυτή διάσταση γεμάτη λάβα και φωτιά μπορούν να επισκεφθούν οι παίκτες στο «Minecraft» μέσω πύλης οψιδιανού;",
    "answers": ["The End", "The Aether", "Nether (Το Κάτω)", "The Deep Dark"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Nether είναι μια υπόγεια διάσταση εμπνευσμένη από την κόλαση, όπου οι παίκτες ταξιδεύουν για να βρουν Blazes, Ghasts και Nether Fortress.",
    "funFacts": [
      "Εάν ένας παίκτης προσπαθήσει να κοιμηθεί σε ένα κρεβάτι μέσα στο Nether, το κρεβάτι εκρήγνυται με τεράστια ισχύ καταστρέφοντας τα πάντα γύρω του.",
      "Κάθε βήμα που κάνει ο παίκτης στο Nether ισοδυναμεί με οκτώ μπλοκ στον κανονικό επάνω κόσμο (Overworld), χρησιμεύοντας για γρήγορα ταξίδια."
    ],
    "source": "https://el.wikipedia.org/wiki/Minecraft",
    "locale": "el-GR",
    "tags": ["minecraft", "nether", "mojang", "sandbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_204",
    "text": "Τι συλλέγει κατά χιλιάδες ο Spyro the Dragon στα επίπεδα για να ανοίξει νέους κόσμους και να πετύχει 100% ολοκλήρωση;",
    "answers": ["Χρυσά δαχτυλίδια", "Μαγικά φίλτρα", "Αυγά δεινοσαύρων", "Πολύτιμους λίθους (Gems)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι πολύτιμοι λίθοι (διαμάντια διαφόρων χρωμάτων και αξιών από 1 έως 25 πόντους) βρίσκονται κρυμμένοι σε σεντούκια και εχθρούς.",
    "funFacts": [
      "Ο άπληστος αρκούδος Moneybags απαιτεί συχνά μεγάλες ποσότητες gems από τον Spyro για να του ανοίξει γέφυρες ή να του μάθει νέες κινήσεις.",
      "Η λιβελούλα Sparx βοηθά τον Spyro μαζεύοντας αυτόματα τους λίθους από μακριά."
    ],
    "source": "https://el.wikipedia.org/wiki/Spyro",
    "locale": "el-GR",
    "tags": ["spyro", "gems", "insomniac-games", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_205",
    "text": "Πόσα Εμβλήματα Γυμναστηρίων (Gym Badges) πρέπει να κερδίσει ένας εκπαιδευτής Pokémon στην περιοχή Kanto για να συμμετάσχει στο Pokémon League;",
    "answers": ["Οκτώ (8)", "Έξι (6)", "Δέκα (10)", "Δώδεκα (12)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Στα κλασικά παιχνίδια Pokémon, ο εκπαιδευτής πρέπει να νικήσει και τους 8 αρχηγούς γυμναστηρίων για να αποκτήσει πρόσβαση στο Indigo Plateau και τους Elite Four.",
    "funFacts": [
      "Ο τελευταίος αρχηγός γυμναστηρίου στο Kanto (στην πόλη Viridian) αποκαλύπτεται ότι είναι ο Giovanni, ο επικεφαλής της εγκληματικής οργάνωσης Team Rocket.",
      "Κάθε έμβλημα επιτρέπει στον παίκτη να χρησιμοποιεί ειδικές κινήσεις έξω από τη μάχη (όπως Cut, Surf και Fly) και εξασφαλίζει την υπακοή δυνατότερων Pokémon."
    ],
    "source": "https://el.wikipedia.org/wiki/Pok%C3%A9mon",
    "locale": "el-GR",
    "tags": ["pokemon", "gym-badges", "kanto", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_206",
    "text": "Πόσα συνεχόμενα kills χωρίς θάνατο (killstreak) απαιτούνταν για την κλήση του Tactical Nuke στο «Call of Duty: Modern Warfare 2» (2009);",
    "answers": ["15 kills", "25 kills", "30 kills", "50 kills"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η επίτευξη 25 συνεχόμενων kills επέτρεπε στον παίκτη να καλέσει μια πυρηνική βόμβα που τερμάτιζε ακαριαία τον αγώνα χαρίζοντας αυτόματη νίκη στην ομάδα του.",
    "funFacts": [
      "Όταν καλείται το Tactical Nuke, μια αντίστροφη μέτρηση 10 δευτερολέπτων με σειρήνες συναγερμού ακούγεται σε όλο τον χάρτη.",
      "Είναι το πιο διάσημο και συζητημένο killstreak στην ιστορία του Call of Duty multiplayer."
    ],
    "source": "https://el.wikipedia.org/wiki/Call_of_Duty:_Modern_Warfare_2",
    "locale": "el-GR",
    "tags": ["call-of-duty", "modern-warfare", "nuke", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_207",
    "text": "Σε ποια επίλεκτη ειδική ομάδα διάσωσης και τακτικών της αστυνομίας της Raccoon City ανήκουν η Jill Valentine και ο Chris Redfield στο «Resident Evil»;",
    "answers": ["B.S.A.A.", "D.S.O.", "S.T.A.R.S.", "F.B.I."],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η ομάδα S.T.A.R.S. (Special Tactics and Rescue Service) στάλθηκε στα βουνά Arklay για να ερευνήσει μυστηριώδεις κανιβαλιστικές δολοφονίες, ανακαλύπτοντας την έπαυλη Spencer.",
    "funFacts": [
      "Ο αρχηγός της ομάδας Alpha των S.T.A.R.S., Albert Wesker, αποκαλύφθηκε ότι ήταν διπλός πράκτορας που δούλευε μυστικά για την Umbrella Corporation.",
      "Η Jill Valentine ήταν η ειδική στην εξουδετέρωση εκρηκτικών και στο ξεκλείδωμα κλειδαριών (lockpicking) της ομάδας."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident-evil", "stars", "jill-valentine", "capcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_208",
    "text": "Ποιοι δύο κλασικοί χαρακτήρες κινουμένων σχεδίων της Disney συνοδεύουν τον Sora ως μάγος της αυλής και αρχηγός της φρουράς στο «Kingdom Hearts»;",
    "answers": ["Ο Μίκυ Μάους και ο Πλούτο", "Ο Τιμόν και ο Πούμπα", "Ο Γούντι και ο Μπαζ", "Ο Ντόναλντ Ντακ και ο Γκούφι"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Donald Duck (ως μάγος της αυλής) και ο Goofy (ως αρχηγός των βασιλικών ιπποτών με ασπίδα) αναζητούν τον εξαφανισμένο Βασιλιά Μίκυ και συμμαχούν με τον Sora.",
    "funFacts": [
      "Σε κάθε κόσμο της Disney που επισκέπτονται (όπως ο κόσμος του Βασιλιά των Λιονταριών ή της Μικρής Γοργόνας), ο Donald χρησιμοποιεί μαγεία για να αλλάξει τη μορφή τους ώστε να ταιριάζουν με το περιβάλλον.",
      "Οι παίκτες συχνά αστειεύονται ότι ο Donald Duck δεν τους θεραπεύει ποτέ έγκαιρα στις δύσκολες μάχες με τα bosses."
    ],
    "source": "https://el.wikipedia.org/wiki/Kingdom_Hearts",
    "locale": "el-GR",
    "tags": ["kingdom-hearts", "disney", "donald-duck", "goofy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_209",
    "text": "Ποιο θρυλικό μυθολογικό όπλο ενέπνευσε τον καινοτόμο μηχανισμό ανάκλησης του τσεκουριού Leviathan πίσω στο χέρι του Κράτου στο «God of War» (2018);",
    "answers": ["Το σφυρί Mjölnir του Thor", "Η τρίαινα του Ποσειδώνα", "Το τόξο του Απόλλωνα", "Το σπαθί Excalibur"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο μηχανισμός εκτόξευσης και άμεσης επιστροφής του Leviathan Axe στο χέρι του Κράτου σχεδιάστηκε με έμπνευση από το σφυρί Mjölnir της σκανδιναβικής μυθολογίας.",
    "funFacts": [
      "Ο σκηνοθέτης Cory Barlog δήλωσε ότι η ομάδα ανάπτυξης πέρασε μήνες τελειοποιώντας το 'βάρος' και την ακουστική αίσθηση της στιγμής που το τσεκούρι προσγειώνεται ξανά στην παλάμη του Κράτου.",
      "Το τσεκούρι κατασκευάστηκε αρχικά από τους νάνους Brok και Sindri για τη γιγάντισσα Faye, τη μητέρα του Atreus."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "leviathan-axe", "kratos", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_210",
    "text": "Ποιο χαρακτηριστικό χειριστήριο με έναν μαύρο μοχλό και ένα μοναδικό κόκκινο κουμπί καθιέρωσε την κλασική κονσόλα Atari 2600;",
    "answers": ["D-Pad", "CX40 Joystick", "Trackball", "Light Gun"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το joystick CX40 της Atari έγινε το παγκόσμιο σύμβολο του χειριστηρίου βιντεοπαιχνιδιών για τη γενιά των τελών της δεκαετίας του 1970 και των αρχών του 1980.",
    "funFacts": [
      "Το απλό του σύστημα με μοχλό 8 κατευθύνσεων και ένα κουμπί πυρός ήταν τόσο δημοφιλές που μπορούσε να συνδεθεί απευθείας και στους οικιακούς υπολογιστές Commodore 64.",
      "Το πρωτότυπο σχέδιο κατοχυρώθηκε με δίπλωμα ευρεσιτεχνίας από τον James C. Asher το 1978."
    ],
    "source": "https://en.wikipedia.org/wiki/Atari_CX40_joystick",
    "locale": "el-GR",
    "tags": ["atari", "joystick", "atari-2600", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'easy', 1, questions)

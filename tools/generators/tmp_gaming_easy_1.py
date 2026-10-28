# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_easy_011",
    "text": "Ποιο κίτρινο ηλεκτρικό πλάσμα αποτελεί την πιο διάσημη μασκότ και το κεντρικό σύμβολο του franchise Pokémon;",
    "answers": ["Πίκατσου (Pikachu)", "Τσάρμαντερ (Charmander)", "Σκουίρτλ (Squirtle)", "Μπούλμπασαρ (Bulbasaur)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Πίκατσου είναι Pokémon ηλεκτρικού τύπου, σχεδιασμένος από την Atsuko Nishida και τον Ken Sugimori, και έγινε η παγκόσμια μασκότ της σειράς.",
    "funFacts": [
      "Το όνομά του προέρχεται από τον συνδυασμό των ιαπωνικών λέξεων 'pika' (λάμψη ηλεκτρισμού) και 'chu' (ήχος ποντικιού).",
      "Αρχικά, η μασκότ της σειράς προοριζόταν να είναι η Clefairy, αλλά ο Pikachu επιλέχθηκε τελικά ως πιο ελκυστικός και για τα δύο φύλα."
    ],
    "source": "https://el.wikipedia.org/wiki/Pikachu",
    "locale": "el-GR",
    "tags": ["pokemon", "pikachu", "nintendo", "anime"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_012",
    "text": "Ποιο ιστορικό μαζικό διαδικτυακό παιχνίδι ρόλων (MMORPG) κυκλοφόρησε η Blizzard το 2004 και διαδραματίζεται στον κόσμο του Azeroth;",
    "answers": ["The Elder Scrolls Online", "World of Warcraft", "Guild Wars", "Final Fantasy XIV"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το World of Warcraft (WoW) είναι το πιο εμβληματικό MMORPG στην ιστορία, φτάνοντας στο αποκορύφωμά του πάνω από 12 εκατομμύρια ενεργούς συνδρομητές.",
    "funFacts": [
      "Το περιστατικό του Corrupted Blood (2005), όπου μια εικονική επιδημία εξαπλώθηκε τυχαία στο παιχνίδι, μελετήθηκε από επιδημιολόγους για την κατανόηση πραγματικών πανδημιών.",
      "Το παιχνίδι κατέχει Ρεκόρ Γκίνες ως το πιο δημοφιλές MMORPG βάσει συνδρομητών παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/World_of_Warcraft",
    "locale": "el-GR",
    "tags": ["warcraft", "blizzard", "mmorpg", "pc-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_013",
    "text": "Σε ποια δημοφιλή σειρά παιχνιδιών δράσης ανοιχτού κόσμου της Rockstar Games οι παίκτες εξερευνούν πόλεις όπως η Los Santos και η Vice City;",
    "answers": ["Mafia", "Saints Row", "Grand Theft Auto", "Watch Dogs"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η σειρά Grand Theft Auto (GTA) ξεκίνησε το 1997 και είναι μία από τις πιο κερδοφόρες σειρές ψυχαγωγίας όλων των εποχών.",
    "funFacts": [
      "Το Grand Theft Auto V απέφερε πάνω από 800 εκατομμύρια δολάρια στις πρώτες 24 ώρες κυκλοφορίας του το 2013, σπάζοντας κάθε ρεκόρ πωλήσεων.",
      "Η πόλη Los Santos βασίζεται εξ ολοκλήρου στο Λος Άντζελες, ενώ η Vice City είναι εμπνευσμένη από το Μαϊάμι."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto",
    "locale": "el-GR",
    "tags": ["gta", "rockstar-games", "open-world", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_014",
    "text": "Ποιος υπερ-στρατιώτης Spartan με χαρακτηριστική πράσινη πανοπλία και χρυσό γείσο είναι ο κεντρικός πρωταγωνιστής της σειράς Halo;",
    "answers": ["Marcus Fenix", "Commander Shepard", "Doom Slayer", "Master Chief"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Master Chief (John-117) είναι ο κυριότερος ήρωας της σειράς Halo και η άτυπη μασκότ της πλατφόρμας Xbox της Microsoft.",
    "funFacts": [
      "Η φωνή του Master Chief ανήκει στον Αμερικανό ηθοποιό Steve Downes, ο οποίος εργαζόταν ως ραδιοφωνικός παραγωγός στο Σικάγο.",
      "Το πρώτο Halo: Combat Evolved (2001) ήταν ο τίτλος λανσαρίσματος που καθιέρωσε το αρχικό Xbox στην παγκόσμια αγορά."
    ],
    "source": "https://en.wikipedia.org/wiki/Master_Chief_(Halo)",
    "locale": "el-GR",
    "tags": ["halo", "master-chief", "xbox", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_015",
    "text": "Ποια υβριδική κονσόλα της Nintendo, που κυκλοφόρησε το 2017, λειτουργεί τόσο ως φορητή όσο και συνδεδεμένη στην τηλεόραση;",
    "answers": ["Nintendo Switch", "Nintendo Wii U", "Nintendo 3DS", "GameCube"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Nintendo Switch διαθέτει αποσπώμενα χειριστήρια Joy-Con και βάση σύνδεσης (dock) για απρόσκοπτη εναλλαγή μεταξύ τηλεόρασης και φορητής χρήσης.",
    "funFacts": [
      "Τα μικρά πλαστικά cartridges του Nintendo Switch είναι επικαλυμμένα με μια μη τοξική αλλά εξαιρετικά πικρή ουσία για να αποτρέπεται η κατάποσή τους από παιδιά.",
      "Είναι μία από τις πιο επιτυχημένες κονσόλες όλων των εποχών, έχοντας πουλήσει πάνω από 140 εκατομμύρια μονάδες παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/Nintendo_Switch",
    "locale": "el-GR",
    "tags": ["nintendo", "switch", "consoles", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_016",
    "text": "Σε ποιο εξαιρετικά δημοφιλές παιχνίδι για κινητά (2009) της φινλανδικής Rovio οι παίκτες εκτοξεύουν πουλιά με σφεντόνα για να εξοντώσουν πράσινα γουρούνια;",
    "answers": ["Cut the Rope", "Angry Birds", "Flappy Bird", "Fruit Ninja"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Angry Birds δημιουργήθηκε από τη Rovio Entertainment και έγινε ένα από τα μεγαλύτερα franchise παιχνιδιών για smartphone παγκοσμίως.",
    "funFacts": [
      "Η ιδέα για τα πράσινα γουρούνια προέκυψε από την επιδημία της γρίπης των χοίρων που απασχολούσε την επικαιρότητα το 2009.",
      "Η τεράστια επιτυχία του παιχνιδιού οδήγησε στη δημιουργία θεματικών πάρκων και επιτυχημένων ταινιών κινουμένων σχεδίων."
    ],
    "source": "https://el.wikipedia.org/wiki/Angry_Birds",
    "locale": "el-GR",
    "tags": ["angry-birds", "mobile", "casual", "rovio"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_017",
    "text": "Σε ποιο viral multiplayer παιχνίδι του 2018 οι παίκτες εκτελούν εργασίες σε διαστημόπλοιο προσπαθώντας να αποκαλύψουν τον μυστικό «απατεώνα» (impostor);",
    "answers": ["Fall Guys", "Rust", "Among Us", "Phasmophobia"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Among Us αναπτύχθηκε από την ανεξάρτητη ομάδα Innersloth και γνώρισε παγκόσμια εκτόξευση δημοτικότητας το 2020 μέσω streamers στο Twitch και YouTube.",
    "funFacts": [
      "Το παιχνίδι αναπτύχθηκε αρχικά από μόλις τρία άτομα και είχε ελάχιστους παίκτες στα δύο πρώτα χρόνια κυκλοφορίας του.",
      "Ο όρος 'sus' (συντομογραφία του suspicious) έγινε παγκόσμιο διαδικτυακό meme εξαιτίας των συζητήσεων ψηφοφορίας στο Among Us."
    ],
    "source": "https://el.wikipedia.org/wiki/Among_Us",
    "locale": "el-GR",
    "tags": ["among-us", "multiplayer", "indie", "social-deduction"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_018",
    "text": "Ποιο κορυφαίο free-to-play παιχνίδι μάχης αρένας (MOBA) κυκλοφόρησε η Riot Games το 2009 και κυριαρχεί στα παγκόσμια esports;",
    "answers": ["Dota 2", "Heroes of the Storm", "Smite", "League of Legends"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το League of Legends (LoL) φέρνει αντιμέτωπες δύο ομάδες πέντε παικτών με στόχο την καταστροφή του αντίπαλου Nexus.",
    "funFacts": [
      "Ο τελικός του παγκοσμίου πρωταθλήματος (Worlds) προσελκύει σταθερά πάνω από 100 εκατομμύρια θεατές παγκοσμίως.",
      "Ενέπνευσε την εξαιρετικά επιτυχημένη σειρά κινουμένων σχεδίων 'Arcane' στο Netflix, η οποία κέρδισε τέσσερα βραβεία Emmy."
    ],
    "source": "https://el.wikipedia.org/wiki/League_of_Legends",
    "locale": "el-GR",
    "tags": ["league-of-legends", "riot-games", "moba", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_019",
    "text": "Ποια πορτοκαλί δίγουρη αλεπού με ικανότητα πτήσης είναι ο πιστός φίλος και βοηθός του Sonic the Hedgehog;",
    "answers": ["Τέιλς (Tails)", "Νακλς (Knuckles)", "Σάντοου (Shadow)", "Έιμι Ρόουζ (Amy Rose)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Miles 'Tails' Prower πρωτοεμφανίστηκε στο Sonic the Hedgehog 2 (1992) και χρησιμοποιεί τις δύο ουρές του σαν έλικα για να πετάει.",
    "funFacts": [
      "Το πλήρες όνομά του, Miles Prower, είναι ένα ηχητικό λογοπαίγνιο με την αγγλική φράση 'miles per hour' (μίλια ανά ώρα).",
      "Εκτός από την πτήση, ο Tails είναι ιδιοφυής μηχανικός και κατασκευάζει διάφορα οχήματα και αεροσκάφη για την ομάδα του Sonic."
    ],
    "source": "https://en.wikipedia.org/wiki/Tails_(character)",
    "locale": "el-GR",
    "tags": ["sonic", "tails", "sega", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_020",
    "text": "Ποια εξαιρετικά επιτυχημένη σειρά προσομοίωσης ζωής της Maxis και της Electronic Arts επιτρέπει στους παίκτες να δημιουργούν εικονικούς χαρακτήρες και σπίτια;",
    "answers": ["SimCity", "The Sims", "Spore", "Second Life"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το The Sims σχεδιάστηκε από τον Will Wright και κυκλοφόρησε το 2000, αποτελώντας ένα από τα μεγαλύτερα franchise προσομοίωσης όλων των εποχών.",
    "funFacts": [
      "Οι χαρακτήρες του παιχνιδιού μιλούν μια φανταστική γλώσσα που ονομάζεται 'Simlish', η οποία δημιουργήθηκε για να μην απαιτείται μετάφραση σε κάθε χώρα.",
      "Ο Will Wright εμπνεύστηκε τη δημιουργία του παιχνιδιού αφού έχασε το σπίτι και τα υπάρχοντά του στην καταστροφική πυρκαγιά του Όουκλαντ το 1991."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Sims",
    "locale": "el-GR",
    "tags": ["the-sims", "ea", "simulation", "pc-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_021",
    "text": "Ποια εμβληματική φορητή κονσόλα 8-bit με μονόχρωμη οθόνη κυκλοφόρησε η Nintendo το 1989 και έγινε σύμβολο της δεκαετίας του '90;",
    "answers": ["Sega Game Gear", "Atari Lynx", "Game Boy", "Neo Geo Pocket"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Game Boy σχεδιάστηκε από τον Gunpei Yokoi και σημείωσε τεράστια επιτυχία, πουλώντας μαζί με το Game Boy Color σχεδόν 119 εκατομμύρια μονάδες.",
    "funFacts": [
      "Ένα Game Boy συνόδευσε τους κοσμοναύτες στον διαστημικό σταθμό Mir το 1993, περνώντας πάνω από 14 μήνες σε τροχιά γύρω από τη Γη.",
      "Ένα Game Boy επέζησε από βομβαρδισμό στρατώνα κατά τον Πόλεμο του Κόλπου και συνέχισε να λειτουργεί κανονικά."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_Boy",
    "locale": "el-GR",
    "tags": ["game-boy", "nintendo", "retro-gaming", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_022",
    "text": "Ποιος γιγάντιος γορίλας της Nintendo ρίχνει βαρέλια και έκανε το ντεμπούτο του στο ομώνυμο κλασικό arcade παιχνίδι του 1981;",
    "answers": ["King K. Rool", "Bowser", "Diddy Kong", "Donkey Kong"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Donkey Kong δημιουργήθηκε από τον Shigeru Miyamoto και ήταν ο πρώτος μεγάλος αντίπαλος του Jumpman (ο οποίος αργότερα ονομάστηκε Mario).",
    "funFacts": [
      "Το όνομα 'Donkey' επιλέχθηκε από τον Miyamoto επειδή πίστευε ότι η λέξη σήμαινε 'πεισματάρης' ή 'ανόητος' στα αγγλικά.",
      "Στη σειρά Donkey Kong Country (1994) για το SNES, η Rare επαναπροσδιόρισε τον χαρακτήρα με πρωτοποριακά προσχεδιασμένα 3D γραφικά."
    ],
    "source": "https://el.wikipedia.org/wiki/Donkey_Kong",
    "locale": "el-GR",
    "tags": ["donkey-kong", "nintendo", "arcade", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_023",
    "text": "Ποιο διάσημο τακτικό first-person shooter της Valve φέρνει αντιμέτωπες ομάδες Τρομοκρατών και Αντιτρομοκρατών σε χάρτες όπως το de_dust2;",
    "answers": ["Counter-Strike", "Rainbow Six Siege", "Valorant", "Team Fortress 2"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Counter-Strike ξεκίνησε το 1999 ως mod του Half-Life από τους Minh Le και Jess Cliffe, προτού εξαγοραστεί από τη Valve και εξελιχθεί σε κορυφαίο esport.",
    "funFacts": [
      "Ο χάρτης Dust II (de_dust2), σχεδιασμένος από τον David Johnston, είναι ο πιο αναγνωρίσιμος και πολυπαιγμένος χάρτης στην ιστορία των multiplayer shooters.",
      "Τα επίσημα παγκόσμια τουρνουά 'Majors' του Counter-Strike προσφέρουν χρηματικά έπαθλα που ξεπερνούν το 1 εκατομμύριο δολάρια ανά διοργάνωση."
    ],
    "source": "https://el.wikipedia.org/wiki/Counter-Strike",
    "locale": "el-GR",
    "tags": ["counter-strike", "valve", "fps", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_024",
    "text": "Ποια ιστορική σειρά fighting games της Capcom καθιέρωσε το είδος με το Street Fighter II (1991) και πρωταγωνιστές τους Ryu και Ken;",
    "answers": ["Tekken", "Street Fighter", "Mortal Kombat", "Soulcalibur"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Street Fighter II εισήγαγε το σύστημα των combos, τις ειδικές κινήσεις με συνδυασμούς μοχλού και πολλαπλούς επιλέξιμους μαχητές από διάφορες χώρες.",
    "funFacts": [
      "Η διάσημη κίνηση 'Hadoken' είναι εμπνευσμένη από το κανόνι κυμάτων του κλασικού anime 'Space Battleship Yamato'.",
      "Το σύστημα των combos ανακαλύφθηκε τυχαία ως bug κατά την ανάπτυξη του Street Fighter II, αλλά οι προγραμματιστές αποφάσισαν να το αφήσουν στο τελικό παιχνίδι."
    ],
    "source": "https://el.wikipedia.org/wiki/Street_Fighter",
    "locale": "el-GR",
    "tags": ["street-fighter", "capcom", "fighting", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_025",
    "text": "Ποιο εθιστικό casual παιχνίδι παζλ της King βασίζεται στην αντιστοίχιση τριών ή περισσότερων όμοιων χρωματιστών καραμελών;",
    "answers": ["Fruit Ninja", "Subway Surfers", "Candy Crush Saga", "Temple Run"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Candy Crush Saga κυκλοφόρησε το 2012 για το Facebook και τα κινητά τηλέφωνα, ξεπερνώντας τα 3 δισεκατομμύρια downloads παγκοσμίως.",
    "funFacts": [
      "Η εταιρεία King εξαγοράστηκε από την Activision Blizzard το 2016 για το αστρονομικό ποσό των 5,9 δισεκατομμυρίων δολαρίων.",
      "Το παιχνίδι διαθέτει πλέον πάνω από 15.000 διαφορετικά επίπεδα που ανανεώνονται συνεχώς με νέες δοκιμασίες."
    ],
    "source": "https://en.wikipedia.org/wiki/Candy_Crush_Saga",
    "locale": "el-GR",
    "tags": ["candy-crush", "mobile", "puzzle", "casual"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_026",
    "text": "Ποιος τεχνητός ιός ευθύνεται για τη μόλυνση των ζωντανών νεκρών στη σειρά παιχνιδιών τρόμου «Resident Evil» της Capcom;",
    "answers": ["G-Virus", "Las Plagas", "Cordyceps", "T-Virus"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο T-Virus (Tyrant Virus) αναπτύχθηκε κρυφά από την Umbrella Corporation ως βιολογικό όπλο, οδηγώντας στην καταστροφή της πόλης Raccoon City.",
    "funFacts": [
      "Στην Ιαπωνία, η σειρά Resident Evil είναι γνωστή με τον τίτλο 'Biohazard'.",
      "Το αρχικό παιχνίδι του 1996 στο PlayStation καθιέρωσε τον όρο 'survival horror' στην ορολογία της βιομηχανίας."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil",
    "locale": "el-GR",
    "tags": ["resident-evil", "capcom", "horror", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_027",
    "text": "Ποιος αμερικανικός κολοσσός λογισμικού κυκλοφόρησε την πρώτη οικιακή κονσόλα Xbox στη Βόρεια Αμερική το 2001;",
    "answers": ["Microsoft", "Apple", "IBM", "Intel"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Microsoft εισήλθε στην αγορά των κονσολών βιντεοπαιχνιδιών το 2001 με το πρώτο Xbox, ανταγωνιζόμενη τη Sony και τη Nintendo.",
    "funFacts": [
      "Το αρχικό Xbox ήταν η πρώτη οικιακή κονσόλα με ενσωματωμένο σκληρό δίσκο (hard drive), καταργώντας την ανάγκη για κάρτες μνήμης σε πολλά παιχνίδια.",
      "Το όνομά του προήλθε από τη συντόμευση του αρχικού εσωτερικού σχεδίου της Microsoft που ονομαζόταν 'DirectX Box'."
    ],
    "source": "https://el.wikipedia.org/wiki/Xbox_(%CE%BA%CE%BF%CE%BD%CF%83%CF%8C%CE%BB%CE%B1)",
    "locale": "el-GR",
    "tags": ["xbox", "microsoft", "consoles", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_028",
    "text": "Ποια πασίγνωστη στρατιωτική σειρά first-person shooter της Activision περιλαμβάνει υπο-σειρές όπως το Modern Warfare και το Black Ops;",
    "answers": ["Battlefield", "Call of Duty", "Medal of Honor", "Killzone"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Call of Duty ξεκίνησε το 2003 εστιάζοντας στον Β΄ Παγκόσμιο Πόλεμο και αποτελεί ένα από τα εμπορικότερα franchise στην ιστορία του gaming.",
    "funFacts": [
      "Το Call of Duty 4: Modern Warfare (2007) άλλαξε ριζικά το τοπίο των multiplayer shooters με το σύστημα των killstreaks και custom classes.",
      "Η σειρά έχει πουλήσει πάνω από 400 εκατομμύρια αντίτυπα παγκοσμίως από την πρώτη της εμφάνιση."
    ],
    "source": "https://el.wikipedia.org/wiki/Call_of_Duty",
    "locale": "el-GR",
    "tags": ["call-of-duty", "activision", "fps", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_029",
    "text": "Ποια διασκεδαστική σειρά αγώνων ταχύτητας της Nintendo επιτρέπει στους παίκτες να εκτοξεύουν κόκκινα και μπλε καβούκια εναντίον των αντιπάλων;",
    "answers": ["F-Zero", "Crash Team Racing", "Mario Kart", "Sonic & Sega All-Stars Racing"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Mario Kart ξεκίνησε το 1992 στο Super Nintendo (Super Mario Kart) και παραμένει η κορυφαία σειρά arcade αγώνων με κάρτ.",
    "funFacts": [
      "Το περίφημο 'μπλε καβούκι' (Spiny Shell) εισήχθη στο Mario Kart 64 για να στοχεύει αποκλειστικά τον πρωτοπόρο του αγώνα.",
      "Το Mario Kart 8 Deluxe στο Nintendo Switch έχει ξεπεράσει τα 60 εκατομμύρια πωλήσεις, όντας το εμπορικότερο παιχνίδι της κονσόλας."
    ],
    "source": "https://el.wikipedia.org/wiki/Mario_Kart",
    "locale": "el-GR",
    "tags": ["mario-kart", "nintendo", "racing", "party-game"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_030",
    "text": "Ποιο πορτοκαλί μαρσιποφόρο πρωταγωνιστεί στην ομώνυμη κλασική σειρά platformer του PlayStation που δημιούργησε η Naughty Dog;",
    "answers": ["Spyro the Dragon", "Jak", "Sly Cooper", "Crash Bandicoot"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Crash Bandicoot δημιουργήθηκε από τους Andy Gavin και Jason Rubin στη Naughty Dog το 1996 και έγινε ανεπίσημη μασκότ του αρχικού PlayStation.",
    "funFacts": [
      "Το πραγματικό ζώο 'bandicoot' είναι ένα μικρό νυκτόβιο μαρσιποφόρο που ζει κυρίως στην Αυστραλία.",
      "Κατά τη διάρκεια των αρχικών δοκιμών, η ομάδα αποκαλούσε προσωρινά τον ήρωα με το ψευδώνυμο 'Willy the Wombat'."
    ],
    "source": "https://el.wikipedia.org/wiki/Crash_Bandicoot",
    "locale": "el-GR",
    "tags": ["crash-bandicoot", "naughty-dog", "playstation", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_031",
    "text": "Ποιο ομαδικό hero shooter πρώτου προσώπου της Blizzard Entertainment (2016) διαθέτει χαρακτήρες όπως η Tracer, ο Winston και ο Reinhardt;",
    "answers": ["Overwatch", "Paladins", "Valorant", "Apex Legends"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Overwatch κέρδισε το βραβείο Game of the Year στα The Game Awards 2016 για τον καινοτόμο συνδυασμό διαφορετικών κλάσεων ηρώων και ομαδικής τακτικής.",
    "funFacts": [
      "Πολλά βασικά στοιχεία και ιδέες του Overwatch προήλθαν από το 'Project Titan', ένα τεράστιο MMO που η Blizzard ακύρωσε μετά από χρόνια ανάπτυξης.",
      "Η Tracer, η Βρετανίδα πιλότος με ικανότητες χρονικού άλματος, έγινε η επίσημη μασκότ στο εξώφυλλο του παιχνιδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/Overwatch",
    "locale": "el-GR",
    "tags": ["overwatch", "blizzard", "fps", "hero-shooter"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_032",
    "text": "Ποια σαρκαστική τεχνητή νοημοσύνη υποβάλλει την Chell σε δοκιμασίες με όπλο πυλών στα εργαστήρια Aperture Science στο παιχνίδι Portal;",
    "answers": ["SHODAN", "GLaDOS", "Cortana", "HAL 9000"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η GLaDOS (Genetic Lifeform and Disk Operating System) είναι η εμβληματική AI ανταγωνίστρια της σειράς Portal της Valve, γνωστή για τις μαύρες χιουμοριστικές της ατάκες.",
    "funFacts": [
      "Η ψευδής υπόσχεση της GLaDOS ότι στο τέλος των δοκιμασιών περιμένει 'κέικ' γέννησε τη διάσημη διαδικτυακή φράση 'The cake is a lie'.",
      "Η φωνή της ανήκει στην ηθοποιό Ellen McLain, η οποία ερμηνεύει και το διάσημο τραγούδι των τίτλων τέλους 'Still Alive'."
    ],
    "source": "https://en.wikipedia.org/wiki/GLaDOS",
    "locale": "el-GR",
    "tags": ["portal", "valve", "glados", "puzzle"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_033",
    "text": "Ποιο Pokémon λαμβάνει ως αρχικό σύντροφο ο Ash Ketchum στο ξεκίνημα των περιπετειών του στην ομώνυμη τηλεοπτική σειρά anime;",
    "answers": ["Τσάρμαντερ", "Σκουίρτλ", "Πίκατσου", "Μπούλμπασαρ"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Ash Ketchum έφτασε αργοπορημένος στο εργαστήριο του Καθηγητή Oak, με αποτέλεσμα όλα τα κλασικά αρχικά Pokémon να έχουν μοιραστεί και να του απομείνει ο απείθαρχος Πίκατσου.",
    "funFacts": [
      "Στην ιαπωνική έκδοση, ο πρωταγωνιστής ονομάζεται Satoshi, προς τιμήν του Satoshi Tajiri, του δημιουργού του franchise Pokémon.",
      "Ο Πίκατσου του Ash αρνείται να μπει μέσα σε Poké Ball και ταξιδεύει μόνιμα στον ώμο του φίλου του."
    ],
    "source": "https://el.wikipedia.org/wiki/Pok%C3%A9mon_(τηλεοπτική_σειρά)",
    "locale": "el-GR",
    "tags": ["pokemon", "anime", "pikachu", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_034",
    "text": "Ποιο ιστορικό όνομα έφερε η σειρά ποδοσφαιρικών βιντεοπαιχνιδιών της Electronic Arts από το 1993 έως το 2023, πριν μετονομαστεί σε «EA Sports FC»;",
    "answers": ["Pro Evolution Soccer", "Sensible Soccer", "Club Football", "FIFA"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η σειρά έφερε το όνομα FIFA για τρεις δεκαετίες, μέχρι τη λήξη της συμφωνίας εμπορικής χρήσης του ονόματος με την παγκόσμια ποδοσφαιρική ομοσπονδία το 2023.",
    "funFacts": [
      "Το πρώτο παιχνίδι της σειράς κυκλοφόρησε τα Χριστούγεννα του 1993 με τον τίτλο 'FIFA International Soccer' στην κονσόλα Sega Mega Drive.",
      "Μετά τη λήξη της συνεργασίας, η EA συνέχισε κανονικά τη σειρά με τη νέα επωνυμία 'EA Sports FC 24'."
    ],
    "source": "https://el.wikipedia.org/wiki/FIFA_(σειρά_βιντεοπαιχνιδιών)",
    "locale": "el-GR",
    "tags": ["fifa", "ea-sports", "football", "sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_035",
    "text": "Ποια διάσημη φράση αναφωνεί ο αφηγητής στο τέλος κάθε νικηφόρου γύρου στο Mortal Kombat, προτρέποντας τον παίκτη να αποτελειώσει τον αντίπαλο;",
    "answers": ["Finish Him!", "Game Over!", "Fatality Now!", "Knockout!"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η φράση 'Finish Him!' καλεί τον νικητή να εκτελέσει μια θεαματική και αιματηρή κίνηση εξόντωσης γνωστή ως 'Fatality'.",
    "funFacts": [
      "Η γραφική βία του αρχικού Mortal Kombat (1992) προκάλεσε ακροάσεις στο αμερικανικό Κογκρέσο και οδήγησε στη δημιουργία του συστήματος αξιολόγησης ηλικιών ESRB.",
      "Ο συνδημιουργός του παιχνιδιού Ed Boon δάνεισε τη δική του φωνή για την εμβληματική ατάκα του Scorpion 'Get over here!'."
    ],
    "source": "https://el.wikipedia.org/wiki/Mortal_Kombat",
    "locale": "el-GR",
    "tags": ["mortal-kombat", "fighting", "arcade", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_036",
    "text": "Ποιο είναι το όνομα του επιθετικού κόκκινου φαντάσματος που καταδιώκει διαρκώς τον Pac-Man στον κλασικό λαβύρινθο;",
    "answers": ["Pinky", "Blinky", "Inky", "Clyde"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Blinky είναι το κόκκινο φάντασμα που ακολουθεί επίμονα τον Pac-Man και αυξάνει την ταχύτητά του όσο λιγοστεύουν οι τελείες στον λαβύρινθο.",
    "funFacts": [
      "Στην ιαπωνική έκδοση, το παρατσούκλι του Blinky είναι 'Akabei', που σημαίνει 'κόκκινος τύπος'.",
      "Όταν ο Pac-Man καταναλώνει ένα μεγάλο χάπι δύναμης (Power Pellet), όλα τα φαντάσματα γίνονται σκούρα μπλε και ευάλωτα για λίγα δευτερόλεπτα."
    ],
    "source": "https://en.wikipedia.org/wiki/Ghosts_(Pac-Man)",
    "locale": "el-GR",
    "tags": ["pac-man", "blinky", "arcade", "namco"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_037",
    "text": "Ποιο ψηφιακό κατάστημα και πλατφόρμα κοινότητας της Valve Corporation αποτελεί τη δημοφιλέστερη υπηρεσία διανομής παιχνιδιών για PC;",
    "answers": ["Epic Games Store", "GOG.com", "Steam", "Origin"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Steam ξεκίνησε το 2003 ως μέσο αυτόματης παροχής ενημερώσεων για τα παιχνίδια της Valve και εξελίχθηκε στη μεγαλύτερη πλατφόρμα ψηφιακών πωλήσεων για υπολογιστές.",
    "funFacts": [
      "Όταν κυκλοφόρησε για πρώτη φορά, αντιμετωπίστηκε με δυσπιστία επειδή απαιτούσε συνεχή σύνδεση στο διαδίκτυο για το Counter-Strike.",
      "Σήμερα η πλατφόρμα καταγράφει τακτικά πάνω από 35 εκατομμύρια ταυτόχρονα συνδεδεμένους χρήστες παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/Steam",
    "locale": "el-GR",
    "tags": ["steam", "valve", "pc-gaming", "digital-distribution"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_038",
    "text": "Σε ποια φουτουριστική μητρόπολη της Καλιφόρνιας διαδραματίζεται το δυστοπικό RPG δράσης «Cyberpunk 2077» της CD Projekt Red;",
    "answers": ["Raccoon City", "Vice City", "Gotham City", "Night City"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Night City είναι μια υπερσύγχρονη αλλά επικίνδυνη φουτουριστική μεγαλούπολη, ελεγχόμενη από πανίσχυρες πολυεθνικές εταιρείες και συμμορίες.",
    "funFacts": [
      "Ο ηθοποιός Keanu Reeves δάνεισε τη φωνή, την εμφάνιση και το motion capture στον εμβληματικό χαρακτήρα Johnny Silverhand.",
      "Η βραβευμένη σειρά anime 'Cyberpunk: Edgerunners' στο Netflix διαδραματίζεται στην ίδια πόλη και ανανέωσε κατακόρυφα το ενδιαφέρον για το παιχνίδι."
    ],
    "source": "https://el.wikipedia.org/wiki/Cyberpunk_2077",
    "locale": "el-GR",
    "tags": ["cyberpunk-2077", "cd-projekt-red", "rpg", "night-city"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_039",
    "text": "Ποια είναι τα χαρακτηριστικά διπλά μαχαίρια δεμένα με αλυσίδες στους καρπούς του Κράτου στα κλασικά παιχνίδια God of War;",
    "answers": ["Λεπίδες του Χάους (Blades of Chaos)", "Τσεκούρι του Λεβιάθαν (Leviathan Axe)", "Δόρυ του Άρη (Spear of Ares)", "Σπαθί του Ολύμπου (Blade of Olympus)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι Λεπίδες του Χάους δόθηκαν στον Κράτο από τον ίδιο τον θεό Άρη, σφυρηλατημένες στα βάθη του Κάτω Κόσμου και δεμένες αιώνια στους καρπούς του.",
    "funFacts": [
      "Στα νεότερα παιχνίδια στη σκανδιναβική μυθολογία (God of War 2018), ο Κράτος χρησιμοποιεί αρχικά το μαγικό Τσεκούρι του Λεβιάθαν.",
      "Η φωνή του Κράτου στα αρχικά παιχνίδια ανήκε στον Terrence C. Carson, ενώ στα σκανδιναβικά κεφάλαια τον ενσαρκώνει ο Christopher Judge."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(σειρά)",
    "locale": "el-GR",
    "tags": ["god-of-war", "kratos", "playstation", "sony"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_040",
    "text": "Ποιο επαναστατικό χαρακτηριστικό διέθετε το χειριστήριο Wii Remote της κονσόλας Nintendo Wii (2006) που μαγνήτισε το ευρύ κοινό;",
    "answers": ["Οθόνη αφής στο κέντρο", "Ανίχνευση φυσικής κίνησης στον χώρο", "Ενσωματωμένο πληκτρολόγιο", "Μαγνητική φόρτιση χωρίς μπαταρίες"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Wii Remote χρησιμοποιούσε επιταχυνσιόμετρα και οπτικό αισθητήρα υπερύθρων για να μεταφράζει τις πραγματικές κινήσεις του χεριού σε ενέργειες στο παιχνίδι.",
    "funFacts": [
      "Το Wii Sports, που περιλαμβανόταν στο πακέτο της κονσόλας, έγινε ένα από τα εμπορικότερα παιχνίδια όλων των εποχών με πάνω από 82 εκατομμύρια αντίτυπα.",
      "Λόγω παικτών που εκτόξευαν κατά λάθος το χειριστήριο στις τηλεοράσεις τους παίζοντας μπόουλινγκ ή τένις, η Nintendo πρόσφερε δωρεάν προστατευτικές θήκες σιλικόνης."
    ],
    "source": "https://el.wikipedia.org/wiki/Wii",
    "locale": "el-GR",
    "tags": ["wii", "nintendo", "hardware", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_041",
    "text": "Ποιο είναι το θεμελιώδες σημείο ανάπαυσης, αναπλήρωσης υγείας και επαναφοράς των εχθρών στη σειρά παιχνιδιών Dark Souls;",
    "answers": ["Το Ιερό (Shrine)", "Το Κελλί (Cell)", "Η Πυρά (Bonfire)", "Ο Βωμός (Altar)"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Bonfire (Πυρά με ένα σπαθί καρφωμένο στη στάχτη) αποτελεί το βασικό checkpoint όπου οι παίκτες ανεβάζουν επίπεδο και ξαποσταίνουν.",
    "funFacts": [
      "Κάθε φορά που ο παίκτης αναπαύεται σε ένα Bonfire, όλοι οι εχθροί του κόσμου ανασταίνονται, εκτός από τα μεγάλα bosses.",
      "Η επιγραφή 'YOU DIED' με κόκκινα γράμματα στην οθόνη θανάτου έχει γίνει το απόλυτο σήμα κατατεθέν της σειράς."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "fromsoftware", "action-rpg", "bonfire"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_042",
    "text": "Ποιο χαλαρωτικό παιχνίδι προσομοίωσης νησιωτικής ζωής της Nintendo σημείωσε παγκόσμια φρενίτιδα την άνοιξη του 2020 με τον υπότιτλο New Horizons;",
    "answers": ["Harvest Moon", "Stardew Valley", "MySims", "Animal Crossing"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Animal Crossing: New Horizons κυκλοφόρησε τον Μάρτιο του 2020 στο Nintendo Switch και έγινε παγκόσμιο φαινόμενο κοινωνικοποίησης κατά τη διάρκεια των lockdowns.",
    "funFacts": [
      "Ο χαρακτήρας Tom Nook, ένα ιαπωνικό ρακούν (tanuki), λειτουργεί ως ο επιχειρηματίας που παρέχει στους παίκτες το πρώτο στεγαστικό δάνειο για το σπίτι τους.",
      "Το παιχνίδι λειτουργεί σε πραγματικό χρόνο, συντονισμένο με το εσωτερικό ρολόι της κονσόλας και τις πραγματικές εποχές του έτους."
    ],
    "source": "https://el.wikipedia.org/wiki/Animal_Crossing",
    "locale": "el-GR",
    "tags": ["animal-crossing", "nintendo", "simulation", "switch"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_043",
    "text": "Ποια εξαιρετικά δημοφιλής online πλατφόρμα επιτρέπει στους χρήστες να δημιουργούν δικά τους τρισδιάστατα παιχνίδια με τη γλώσσα προγραμματισμού Lua;",
    "answers": ["Roblox", "Habbo Hotel", "Club Penguin", "Second Life"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Roblox ιδρύθηκε από τους David Baszucki και Erik Cassel το 2006 και επιτρέπει σε νέους δημιουργούς να σχεδιάζουν και να κυκλοφορούν τα δικά τους παιχνίδια.",
    "funFacts": [
      "Το εικονικό νόμισμα της πλατφόρμας ονομάζεται 'Robux' και μπορεί να εξαργυρωθεί σε πραγματικά χρήματα από επιλέξιμους δημιουργούς.",
      "Ο χαρακτηριστικός ήχος θανάτου 'Oof' των χαρακτήρων προερχόταν αρχικά από το βιντεοπαιχνίδι Messiah του 2000."
    ],
    "source": "https://el.wikipedia.org/wiki/Roblox",
    "locale": "el-GR",
    "tags": ["roblox", "metaverse", "multiplayer", "lua"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_044",
    "text": "Τι συλλέγει κατά μήκος των διαδρομών ο Sonic the Hedgehog για να προστατεύεται από ζημιά και να μην χάνει ζωές;",
    "answers": ["Χρυσά νομίσματα", "Χρυσά δαχτυλίδια", "Μπλε διαμάντια", "Κόκκινα μανιτάρια"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα χρυσά δαχτυλίδια (Rings) προστατεύουν τον Sonic. Αν δεχθεί χτύπημα έχοντας έστω κι ένα δαχτυλίδι, αυτά διασκορπίζονται χωρίς ο ήρωας να χάσει ζωή.",
    "funFacts": [
      "Εάν ο Sonic συλλέξει 100 δαχτυλίδια σε μια πίστα, κερδίζει αυτόματα μία επιπλέον ζωή.",
      "Η συγκέντρωση και των επτά σμαραγδιών του χάους σε συνδυασμό με 50 δαχτυλίδια του επιτρέπει να μεταμορφωθεί στον πανίσχυρο Super Sonic."
    ],
    "source": "https://el.wikipedia.org/wiki/Sonic_the_Hedgehog",
    "locale": "el-GR",
    "tags": ["sonic", "sega", "rings", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_045",
    "text": "Ποια ομάδα ανάπτυξης (δημιουργός και της σειράς Titanfall) σχεδίασε το επιτυχημένο battle royale πρώτου προσώπου «Apex Legends»;",
    "answers": ["Infinity Ward", "Treyarch", "Respawn Entertainment", "Bungie"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Respawn Entertainment κυκλοφόρησε το Apex Legends το 2019 ως ξαφνική κυκλοφορία χωρίς προηγούμενη διαφημιστική εκστρατεία.",
    "funFacts": [
      "Το Apex Legends διαδραματίζεται στο ίδιο επιστημονικής φαντασίας σύμπαν με τη σειρά Titanfall.",
      "Εισήγαγε το σύστημα 'Ping', έναν καινοτόμο μηχανισμό συνεννόησης χωρίς φωνή που υιοθετήθηκε στη συνέχεια από σχεδόν όλα τα shooters."
    ],
    "source": "https://en.wikipedia.org/wiki/Apex_Legends",
    "locale": "el-GR",
    "tags": ["apex-legends", "respawn", "battle-royale", "ea"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_046",
    "text": "Ποια είναι η ιδιότητα και το επάγγελμα του Geralt of Rivia στον φανταστικό κόσμο της σειράς παιχνιδιών «The Witcher»;",
    "answers": ["Βασιλικός ιππότης", "Σκοτεινός μάγος", "Αρχηγός κλεφτών", "Μεταλλαγμένος κυνηγός τεράτων"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Γκέραλτ είναι ένας Witcher (Γητευτής), ένας γενετικά μεταλλαγμένος επαγγελματίας που εξολοθρεύει τέρατα έναντι αμοιβής.",
    "funFacts": [
      "Τα παιχνίδια βασίζονται στη διάσημη σειρά βιβλίων φαντασίας του Πολωνού συγγραφέα Andrzej Sapkowski.",
      "Ο Γκέραλτ φέρει πάντα δύο σπαθιά στην πλάτη του: ένα από ατσάλι για ανθρώπους και θηρία, και ένα από ασήμι ειδικά για υπερφυσικά πλάσματα."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC_%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["witcher", "geralt", "cd-projekt-red", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_047",
    "text": "Ποια ιαπωνική εταιρεία βιντεοπαιχνιδιών είναι ο δημιουργός των θρυλικών σειρών ρόλων Final Fantasy, Dragon Quest και Kingdom Hearts;",
    "answers": ["Square Enix", "Konami", "Bandai Namco", "Capcom"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Square Enix προέκυψε το 2003 από τη συγχώνευση των δύο ιστορικών ιαπωνικών κολοσσών JRPG, της Square και της Enix.",
    "funFacts": [
      "Το πρώτο Final Fantasy (1987) ονομάστηκε έτσι επειδή ο Hironobu Sakaguchi πίστευε ότι θα ήταν το τελευταίο του παιχνίδι πριν αποχωρήσει από τη βιομηχανία.",
      "Η σειρά Kingdom Hearts αποτελεί επίσημη συνεργασία μεταξύ της Square Enix και των κινουμένων σχεδίων της Disney."
    ],
    "source": "https://el.wikipedia.org/wiki/Square_Enix",
    "locale": "el-GR",
    "tags": ["square-enix", "final-fantasy", "jrpg", "japan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_048",
    "text": "Σε ποια ιστορική περίοδο και γεωγραφικό περιβάλλον διαδραματίζονται οι περιπέτειες της επικής σειράς «Red Dead Redemption»;",
    "answers": ["Στη μεσαιωνική Αγγλία", "Στην αμερικανική Άγρια Δύση", "Στη ναπολεόντεια Γαλλία", "Στην αρχαία Ρώμη"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η σειρά Red Dead Redemption της Rockstar Games εξερευνά τη δύση της εποχής των καουμπόηδων και των παρανόμων στα τέλη του 19ου και αρχές του 20ού αιώνα.",
    "funFacts": [
      "Το Red Dead Redemption 2 (2018) χρειάστηκε πάνω από οκτώ χρόνια ανάπτυξης για να ολοκληρωθεί.",
      "Ο πρωταγωνιστής Arthur Morgan θεωρείται ευρέως ένας από τους πιο καλογραμμένους χαρακτήρες στην ιστορία των βιντεοπαιχνιδιών."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "rockstar-games", "western", "open-world"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_049",
    "text": "Ποιο είναι το όνομα του χαμογελαστού ξανθού αγοριού με το μπλε-κίτρινο κολάν που λειτουργεί ως η αναγνωρίσιμη μασκότ της σειράς Fallout;",
    "answers": ["Pip-Boy", "Nuka-Man", "Vault Boy", "Radioactive Kid"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Vault Boy είναι η επίσημη μασκότ της Vault-Tec Corporation στη μετα-αποκαλυπτική σειρά Fallout, εικονογραφώντας τα στατιστικά και τα perks.",
    "funFacts": [
      "Συγχέεται συχνά με το Pip-Boy, το οποίο είναι η ηλεκτρονική συσκευή καρπού που φορά ο πρωταγωνιστής.",
      "Η κλασική πόζα του με τον ανασηκωμένο αντίχειρα συνδέεται με τον παλιό εμπειρικό κανόνα μέτρησης του μεγέθους ενός πυρηνικού μανιταριού."
    ],
    "source": "https://en.wikipedia.org/wiki/Vault_Boy",
    "locale": "el-GR",
    "tags": ["fallout", "vault-boy", "bethesda", "post-apocalyptic"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_050",
    "text": "Σε ποιο πρωτότυπο αθλητικό παιχνίδι της Psyonix οι παίκτες οδηγούν πυραυλοκίνητα αυτοκίνητα για να σκοράρουν γκολ με μια τεράστια μπάλα;",
    "answers": ["TrackMania", "Twisted Metal", "Destruction Derby", "Rocket League"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Rocket League κυκλοφόρησε το 2015 και συνδυάζει τους κανόνες του ποδοσφαίρου με ακροβατικά άλματα και ώθηση πυραύλων οχημάτων.",
    "funFacts": [
      "Αποτελεί συνέχεια ενός προηγούμενου τίτλου του 2008 με το τεράστιο όνομα 'Supersonic Acrobatic Rocket-Powered Battle-Cars'.",
      "Η εταιρεία Psyonix εξαγοράστηκε από την Epic Games το 2019, και το παιχνίδι έγινε εντελώς δωρεάν (free-to-play) το 2020."
    ],
    "source": "https://el.wikipedia.org/wiki/Rocket_League",
    "locale": "el-GR",
    "tags": ["rocket-league", "sports", "cars", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_051",
    "text": "Ποιος γοητευτικός κυνηγός θησαυρών και λάτρης της αρχαιολογίας είναι ο βασικός πρωταγωνιστής της σειράς περιπετειών «Uncharted»;",
    "answers": ["Νέιθαν Ντρέικ (Nathan Drake)", "Σαμ Φίσερ (Sam Fisher)", "Τζόελ Μίλερ (Joel Miller)", "Άρθουρ Μόργκαν (Arthur Morgan)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Nathan Drake πρωταγωνιστεί σε τέσσερις κύριους τίτλους Uncharted στο PlayStation, αναζητώντας χαμένες μυθικές πόλεις όπως το El Dorado.",
    "funFacts": [
      "Ο Drake ισχυρίζεται ότι είναι απόγονος του διάσημου Άγγλου εξερευνητή και κουρσάρου Sir Francis Drake.",
      "Στην κινηματογραφική μεταφορά του Uncharted (2022), τον ρόλο του νεαρού Nathan Drake υποδύθηκε ο Tom Holland."
    ],
    "source": "https://el.wikipedia.org/wiki/Uncharted",
    "locale": "el-GR",
    "tags": ["uncharted", "nathan-drake", "naughty-dog", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_052",
    "text": "Ποιο σφαιρικό ροζ πλασματάκι της Nintendo έχει την ικανότητα να εισπνέει εχθρούς και να αντιγράφει τις δυνάμεις τους;",
    "answers": ["Γιόσι (Yoshi)", "Κίρμπι (Kirby)", "Τζίγκλιπαφ (Jigglypuff)", "Τόαντ (Toad)"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Kirby δημιουργήθηκε από τον Masahiro Sakurai για το Game Boy (Kirby's Dream Land, 1992) και ζει στον πλανήτη Popstar.",
    "funFacts": [
      "Πήρε το όνομά του προς τιμήν του John Kirby Jr., του δικηγόρου που υπερασπίστηκε επιτυχώς τη Nintendo στη δικαστική διαμάχη για το Donkey Kong.",
      "Στην πρώτη του εμφάνιση στο Game Boy ήταν λευκός λόγω της μονόχρωμης οθόνης, και ο Shigeru Miyamoto αρχικά τον προτιμούσε κίτρινο."
    ],
    "source": "https://el.wikipedia.org/wiki/Kirby",
    "locale": "el-GR",
    "tags": ["kirby", "nintendo", "platformer", "sakurai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_053",
    "text": "Ποιο είναι το χαρακτηριστικό εργαλείο και όπλο κοντινής μάχης του θεωρητικού φυσικού Gordon Freeman στη σειρά «Half-Life»;",
    "answers": ["Σφυρί", "Τσεκούρι", "Λοστός", "Μαχαίρι μάχης"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο κόκκινος λοστός (crowbar) είναι το πρώτο όπλο που αποκτά ο Gordon Freeman μετά το καταστροφικό πείραμα στις εγκαταστάσεις Black Mesa.",
    "funFacts": [
      "Ο Gordon Freeman είναι ένας από τους πιο διάσημους 'σιωπηλούς πρωταγωνιστές', καθώς δεν μιλάει ποτέ σε κανένα παιχνίδι της σειράς.",
      "Το αρχικό Half-Life (1998) έφερε επανάσταση στα FPS επειδή απέφυγε τα cutscenes, διατηρώντας τον παίκτη διαρκώς σε πρώτο πρόσωπο."
    ],
    "source": "https://el.wikipedia.org/wiki/Half-Life",
    "locale": "el-GR",
    "tags": ["half-life", "valve", "gordon-freeman", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_054",
    "text": "Ποιο μοναδικό ανατομικό γνώρισμα χαρακτηρίζει τον ήρωα πλατφόρμας Rayman της Ubisoft;",
    "answers": ["Έχει μόνο ένα μάτι", "Έχει φτερά νυχτερίδας", "Έχει μεταλλικό σώμα", "Δεν έχει καθόλου χέρια και πόδια"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Rayman δεν έχει λαιμό, μπράτσα ή γάμπες: τα χέρια, τα πόδια και το κεφάλι του αιωρούνται ελεύθερα γύρω από το σώμα του.",
    "funFacts": [
      "Ο σχεδιαστής Michel Ancel αφαίρεσε τα άκρα του Rayman για τεχνικούς λόγους, ώστε να γίνει απλούστερο το animation στις κονσόλες της δεκαετίας του '90.",
      "Τα μαλλιά του λειτουργούν σαν έλικας, επιτρέποντάς του να αιωρείται στον αέρα μετά από άλματα."
    ],
    "source": "https://el.wikipedia.org/wiki/Rayman",
    "locale": "el-GR",
    "tags": ["rayman", "ubisoft", "platformer", "michel-ancel"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_055",
    "text": "Ποια διάσημη σειρά fighting crossover της Nintendo φέρνει σε αναμετρήσεις χαρακτήρες όπως οι Mario, Link, Pikachu και Kirby;",
    "answers": ["Super Smash Bros.", "Mario Party", "Nintendo All-Stars", "Brawlhalla"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Super Smash Bros. δημιουργήθηκε από τον Masahiro Sakurai και διαφέρει από τα παραδοσιακά fighting games, καθώς στόχος είναι η εκτόξευση του αντιπάλου εκτός ορίων.",
    "funFacts": [
      "Το Super Smash Bros. Ultimate στο Nintendo Switch περιλαμβάνει πάνω από 80 playable χαρακτήρες από δεκάδες διαφορετικές σειρές.",
      "Αρχικά ξεκίνησε ως πειραματικό πρωτότυπο με το όνομα 'Dragon King: The Fighting Game', πριν ενσωματώσει τις μασκότ της Nintendo."
    ],
    "source": "https://el.wikipedia.org/wiki/Super_Smash_Bros.",
    "locale": "el-GR",
    "tags": ["super-smash-bros", "nintendo", "fighting", "sakurai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_056",
    "text": "Ποιο είναι το όνομα του μικρού θαρραλέου μοβ δράκου που πρωταγωνιστεί στην ομώνυμη κλασική σειρά 3D platformer του PlayStation;",
    "answers": ["Σπάρκο (Sparko)", "Σπύρο (Spyro)", "Ντράκο (Draco)", "Ίγκνιτους (Ignitus)"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Spyro the Dragon δημιουργήθηκε από την Insomniac Games το 1998 και συνοδεύεται πάντα από τη μικρή πιστή λιβελούλα Sparx.",
    "funFacts": [
      "Αρχικά προοριζόταν να είναι πράσινος, αλλά επιλέχθηκε το μοβ χρώμα για να ξεχωρίζει εύκολα από το πράσινο γρασίδι των επιπέδων.",
      "Το soundtrack των τριών πρώτων παιχνιδιών γράφτηκε από τον Stewart Copeland, τον θρυλικό ντράμερ του συγκροτήματος The Police."
    ],
    "source": "https://el.wikipedia.org/wiki/Spyro",
    "locale": "el-GR",
    "tags": ["spyro", "insomniac-games", "playstation", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_057",
    "text": "Ποια κινεζική εταιρεία ανέπτυξε το εξαιρετικά δημοφιλές δωρεάν action RPG ανοιχτού κόσμου «Genshin Impact» που κυκλοφόρησε το 2020;",
    "answers": ["Tencent", "NetEase", "miHoYo (HoYoverse)", "Game Science"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η miHoYo (που δραστηριοποιείται διεθνώς με την επωνυμία HoYoverse) κυκλοφόρησε το Genshin Impact, σημειώνοντας τεράστια παγκόσμια εμπορική επιτυχία.",
    "funFacts": [
      "Ο φανταστικός κόσμος του παιχνιδιού (Teyvat) αποτελείται από επτά έθνη, καθένα από τα οποία αντλεί έμπνευση από πραγματικούς πολιτισμούς της Γης.",
      "Το κόστος ανάπτυξης των 100 εκατομμυρίων δολαρίων αποσβέστηκε μέσα σε μόλις δύο εβδομάδες από την κυκλοφορία του."
    ],
    "source": "https://el.wikipedia.org/wiki/Genshin_Impact",
    "locale": "el-GR",
    "tags": ["genshin-impact", "hoyoverse", "mihoyo", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_058",
    "text": "Πόσοι παίκτες συνεργάζονται ως ομάδα επιζώντων ενάντια σε ορδές μολυσμένων στο κλασικό zombie shooter «Left 4 Dead» της Valve;",
    "answers": ["Δύο (2)", "Τρεις (3)", "Έξι (6)", "Τέσσερις (4)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Left 4 Dead βασίζεται στη στενή συνεργασία τεσσάρων επιζώντων που πρέπει να αλληλοβοηθούνται για να φτάσουν στα ασφαλή δωμάτια (safe rooms).",
    "funFacts": [
      "Το παιχνίδι εισήγαγε τον 'AI Director', ένα σύστημα τεχνητής νοημοσύνης που ρυθμίζει δυναμικά τη δυσκολία και τον ρυθμό εμφάνισης των ζόμπι.",
      "Ο αριθμός 4 στον τίτλο αποτελεί λογοπαίγνιο με την αγγλική φράση 'Left for dead'."
    ],
    "source": "https://el.wikipedia.org/wiki/Left_4_Dead",
    "locale": "el-GR",
    "tags": ["left-4-dead", "valve", "co-op", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_059",
    "text": "Ποια επιτυχημένη σειρά μουσικών παιχνιδιών της Ubisoft καλεί τους παίκτες να μιμούνται χορογραφίες γνωστών ποπ τραγουδιών μπροστά στην οθόνη;",
    "answers": ["Just Dance", "Dance Dance Revolution", "Guitar Hero", "SingStar"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Just Dance κυκλοφόρησε για πρώτη φορά το 2009 στο Nintendo Wii και εξελίχθηκε σε ετήσιο παγκόσμιο franchise χορευτικών παιχνιδιών.",
    "funFacts": [
      "Το όνομα του παιχνιδιού προέρχεται από το ομώνυμο διάσημο τραγούδι της Lady Gaga.",
      "Το Just Dance 2020 ήταν το τελευταίο επίσημο παιχνίδι που κυκλοφόρησε παγκοσμίως για την κονσόλα Nintendo Wii, 14 χρόνια μετά το λανσάρισμά της."
    ],
    "source": "https://el.wikipedia.org/wiki/Just_Dance",
    "locale": "el-GR",
    "tags": ["just-dance", "ubisoft", "music", "dance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_060",
    "text": "Ποιο ψηφιακό παιχνίδι στρατηγικής με κάρτες (CCG) της Blizzard Entertainment βασίζεται στους ήρωες και τους μύθους του World of Warcraft;",
    "answers": ["Magic: The Gathering Arena", "Hearthstone", "Gwent", "Legends of Runeterra"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Hearthstone (αρχικά Heroes of Warcraft) κυκλοφόρησε το 2014 και έφερε τα ψηφιακά παιχνίδια συλλεκτικών καρτών σε ένα ευρύτατο παγκόσμιο κοινό.",
    "funFacts": [
      "Το παιχνίδι ξεκίνησε ως πειραματικό project μιας μικρής εσωτερικής ομάδας της Blizzard με την ονομασία 'Team 5'.",
      "Η υπόθεση εκτυλίσσεται εικονικά μέσα σε μια ζεστή πανδοχείο του Azeroth, όπου οι παίκτες μαζεύονται γύρω από το τζάκι για να παίξουν κάρτες."
    ],
    "source": "https://el.wikipedia.org/wiki/Hearthstone",
    "locale": "el-GR",
    "tags": ["hearthstone", "blizzard", "card-game", "warcraft"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'easy', 1, questions)

# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_easy_061",
    "text": "Ποιο επαναστατικό FPS της id Software (1993) έβαλε τους παίκτες στον ρόλο ενός διαστημικού πεζοναύτη που μάχεται δαίμονες στον Άρη;",
    "answers": ["Doom", "Quake", "Unreal Tournament", "Wolfenstein 3D"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Doom κυκλοφόρησε το 1993 από την id Software και καθιέρωσε τα first-person shooters, εκλαϊκεύοντας τα 3D γραφικά και τα δικτυακά deathmatches.",
    "funFacts": [
      "Λόγω του ανοιχτού πηγαίου κώδικα, το Doom έχει μεταφερθεί σε αμέτρητες απρόσμενες συσκευές, όπως επιστημονικά κομπιουτεράκια, ψηφιακά τεστ εγκυμοσύνης και εκτυπωτές.",
      "Ο πρωταγωνιστής είναι ευρύτερα γνωστός στην κοινότητα των παικτών ως 'Doomguy' ή αργότερα 'Doom Slayer'."
    ],
    "source": "https://el.wikipedia.org/wiki/Doom",
    "locale": "el-GR",
    "tags": ["doom", "id-software", "fps", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_062",
    "text": "Ποιο είναι το θρυλικό ιερό σπαθί που κρατάει ο Link στα περισσότερα παιχνίδια της σειράς «The Legend of Zelda»;",
    "answers": ["Buster Sword", "Master Sword", "Soul Edge", "Keyblade"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Master Sword (γνωστό και ως Blade of Evil's Bane) είναι το ιερό σπαθί που σφυρηλατήθηκε από τη θεά Hylia για να αποκρούει το κακό.",
    "funFacts": [
      "Στο κλασικό A Link to the Past (1991), ο Link πρέπει πρώτα να συγκεντρώσει τρία μενταγιόν για να αποδείξει την αξία του και να τραβήξει το σπαθί από το βάθρο του.",
      "Στο Breath of the Wild, το Master Sword είναι το μοναδικό όπλο στο παιχνίδι που δεν σπάει μόνιμα, αλλά απλώς εξαντλείται προσωρινά η ενέργειά του."
    ],
    "source": "https://en.wikipedia.org/wiki/Master_Sword",
    "locale": "el-GR",
    "tags": ["zelda", "link", "master-sword", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_063",
    "text": "Ποιος είναι ο ψηλότερος δίδυμος αδελφός του Mario με το πράσινο καπέλο και την πράσινη μπλούζα;",
    "answers": ["Wario", "Waluigi", "Luigi (Λουίτζι)", "Toad"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Luigi δημιουργήθηκε από τον Shigeru Miyamoto και πρωτοεμφανίστηκε στο Mario Bros. (1983) ως ο δεύτερος παίκτης (Player 2).",
    "funFacts": [
      "Το όνομά του προέρχεται από το ιαπωνικό λογοπαίγνιο 'ruiji', που σημαίνει 'παρόμοιος' ή 'ίδιος'.",
      "Πρωταγωνιστεί στη δική του επιτυχημένη σειρά παιχνιδιών 'Luigi's Mansion', όπου κυνηγά φαντάσματα με μια ειδική ηλεκτρική σκούπα."
    ],
    "source": "https://el.wikipedia.org/wiki/Luigi",
    "locale": "el-GR",
    "tags": ["luigi", "mario", "nintendo", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_064",
    "text": "Ποιο είναι το όνομα του γιου του Κράτου που τον συνοδεύει και μάχεται στο πλευρό του στο «God of War» (2018);",
    "answers": ["Βάλντουρ (Baldur)", "Μίμιρ (Mimir)", "Θορ (Thor)", "Ατρέας (Atreus)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Atreus είναι ο γιος του Κράτου και της Faye, ο οποίος χρησιμοποιεί τόξο και μαθαίνει σταδιακά για τη θεϊκή καταγωγή του.",
    "funFacts": [
      "Στο φινάλε του παιχνιδιού αποκαλύπτεται ότι το όνομα που του είχαν δώσει οι γίγαντες Γιότουν ήταν Λόκι (Loki).",
      "Τη φωνή και το motion capture του Atreus ανέλαβε ο Αμερικανός ηθοποιός Sunny Suljic."
    ],
    "source": "https://en.wikipedia.org/wiki/Atreus_(God_of_War)",
    "locale": "el-GR",
    "tags": ["god-of-war", "atreus", "kratos", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_065",
    "text": "Ποιο πέμπτο αριθμημένο παιχνίδι της σειράς The Elder Scrolls κυκλοφόρησε το 2011 και έγινε ένα από τα διασημότερα RPG ανοιχτού κόσμου;",
    "answers": ["Skyrim", "Morrowind", "Oblivion", "Daggerfall"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το The Elder Scrolls V: Skyrim της Bethesda Game Studios διαδραματίζεται στην παγωμένη επαρχία Skyrim και παρακολουθεί τον Dragonborn (Dovahkiin).",
    "funFacts": [
      "Η φράση 'I used to be an adventurer like you, then I took an arrow in the knee' που λένε οι φρουροί του παιχνιδιού έγινε ένα από τα πιο διάσημα gaming memes.",
      "Το παιχνίδι κυκλοφόρησε στη χαρακτηριστική ημερομηνία 11/11/11."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim",
    "locale": "el-GR",
    "tags": ["skyrim", "elder-scrolls", "bethesda", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_066",
    "text": "Ποιο αναγνωρισμένο μετα-αποκαλυπτικό παιχνίδι δράσης της Naughty Dog (2013) αφηγείται το ταξίδι επιβίωσης του Joel και της νεαρής Ellie;",
    "answers": ["Days Gone", "The Last of Us", "Left 4 Dead", "State of Decay"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το The Last of Us παρουσιάζει έναν κόσμο ρημαγμένο από μια μεταλλαγμένη παρασιτική λοίμωξη του μύκητα Cordyceps.",
    "funFacts": [
      "Η τηλεοπτική μεταφορά του παιχνιδιού από το HBO με πρωταγωνιστές τον Pedro Pascal και την Bella Ramsey σημείωσε τεράστια επιτυχία και κέρδισε Emmy.",
      "Ο παρασιτικός μύκητας Cordyceps υπάρχει στην πραγματικότητα στη φύση, αλλά προσβάλλει μόνο έντομα, όπως τα μυρμήγκια."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Last_of_Us",
    "locale": "el-GR",
    "tags": ["the-last-of-us", "naughty-dog", "playstation", "action-adventure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_067",
    "text": "Ποιος πρωτάρης αστυνομικός πρωτοεμφανίστηκε στο Resident Evil 2 και αργότερα πρωταγωνίστησε ως ειδικός πράκτορας στο Resident Evil 4;",
    "answers": ["Chris Redfield", "Albert Wesker", "Leon S. Kennedy", "Barry Burton"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Leon S. Kennedy έφτασε στη Raccoon City ακριβώς την ημέρα της κατάρρευσής της και αργότερα ταξίδεψε στην αγροτική Ισπανία για να σώσει την κόρη του Προέδρου.",
    "funFacts": [
      "Το Resident Evil 4 (2005) καθιέρωσε την κάμερα πάνω από τον ώμο (over-the-shoulder), επηρεάζοντας ολόκληρη τη μετέπειτα βιομηχανία των παιχνιδιών τρίτου προσώπου.",
      "Στο Resident Evil 2, η πρώτη ημέρα του Leon στο αστυνομικό τμήμα συνέπεσε τραγικά με το ξέσπασμα του ιού."
    ],
    "source": "https://en.wikipedia.org/wiki/Leon_S._Kennedy",
    "locale": "el-GR",
    "tags": ["resident-evil", "leon-kennedy", "capcom", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_068",
    "text": "Σε ποιο πολύχρωμο party battle royale παιχνίδι (2020) δεκάδες ανθρωπάκια σε σχήμα φασολιού διαγωνίζονται σε αστείες πίστες με εμπόδια;",
    "answers": ["Human: Fall Flat", "Gang Beasts", "Stumble Guys", "Fall Guys"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Fall Guys: Ultimate Knockout αναπτύχθηκε από τη Mediatonic και είναι εμπνευσμένο από τηλεοπτικά παιχνίδια όπως το Κάστρο του Τακέσι.",
    "funFacts": [
      "Το παιχνίδι κατέχει Ρεκόρ Γκίνες ως το παιχνίδι με τις περισσότερες λήψεις όλων των εποχών στην ιστορία της υπηρεσίας PlayStation Plus.",
      "Οι χαρακτήρες σχεδιάστηκαν σκόπιμα αδέξιοι ώστε να συγκρούονται και να παραπατούν κωμικά μεταξύ τους."
    ],
    "source": "https://el.wikipedia.org/wiki/Fall_Guys",
    "locale": "el-GR",
    "tags": ["fall-guys", "party-game", "battle-royale", "casual"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_069",
    "text": "Ποιο σκοτεινό action RPG της Blizzard Entertainment διαδραματίζεται στον κόσμο του Sanctuary και επικεντρώνεται στη μάχη ενάντια στον Άρχοντα του Τρόμου;",
    "answers": ["Diablo", "Torchlight", "Path of Exile", "Grim Dawn"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Diablo κυκλοφόρησε το 1997 και όρισε το είδος του action RPG και του loot-based παιχνιδιού με τυχαία παραγόμενα μπουντρούμια.",
    "funFacts": [
      "Ο μυστικός κρυφός κόσμος των αγελάδων ('Secret Cow Level') στο Diablo II ξεκίνησε ως αστικός μύθος παικτών πριν υλοποιηθεί επίσημα από τη Blizzard.",
      "Η μουσική της πόλης Tristram με την ακουστική κιθάρα, σε σύνθεση Matt Uelmen, είναι ένα από τα πιο αναγνωρίσιμα κομμάτια στο gaming."
    ],
    "source": "https://el.wikipedia.org/wiki/Diablo_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["diablo", "blizzard", "action-rpg", "dark-fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_070",
    "text": "Ποιο κλασικό αντικείμενο στη σειρά Mario Kart προσφέρει στιγμιαία επιτάχυνση (boost) στο όχημα του παίκτη όταν χρησιμοποιηθεί;",
    "answers": ["Μπανάνα", "Μανιτάρι (Mushroom)", "Πράσινο καβούκι", "Νομισματοθήκη"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Super Mushroom δίνει μια σύντομη ώθηση ταχύτητας, επιτρέποντας στους οδηγούς να περάσουν μέσα από γρασίδι ή άμμο χωρίς να επιβραδύνουν.",
    "funFacts": [
      "Το χρυσό μανιτάρι (Golden Dash Mushroom) επιτρέπει πολλαπλές συνεχόμενες επιταχύνσεις για περιορισμένο χρονικό διάστημα.",
      "Στο αρχικό Super Mario Kart (1992) στο SNES, το μανιτάρι ήταν το βασικότερο εργαλείο για την εκτέλεση σύντομων παρακαμπτήριων (shortcuts)."
    ],
    "source": "https://el.wikipedia.org/wiki/Mario_Kart",
    "locale": "el-GR",
    "tags": ["mario-kart", "mario", "nintendo", "racing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_071",
    "text": "Ποια οικιακή κονσόλα της Nintendo (2001) είχε χαρακτηριστικό κυβικό σχήμα με ενσωματωμένο χερούλι και χρησιμοποιούσε mini-DVD δίσκους;",
    "answers": ["Nintendo 64", "Sega Dreamcast", "Nintendo GameCube", "Nintendo Wii U"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το GameCube ήταν η έκτη γενιά οικιακών συστημάτων της Nintendo και εισήγαγε το εξαιρετικά δημοφιλές εργονομικό χειριστήριο GameCube controller.",
    "funFacts": [
      "Τα mini-DVD των 8 εκατοστών είχαν χωρητικότητα 1,5 GB και επιλέχθηκαν κυρίως για την αποτροπή της πειρατείας λογισμικού.",
      "Ο επεξεργαστής του GameCube είχε την κωδική ονομασία 'Gekko' και αναπτύχθηκε σε συνεργασία με την IBM."
    ],
    "source": "https://el.wikipedia.org/wiki/GameCube",
    "locale": "el-GR",
    "tags": ["gamecube", "nintendo", "hardware", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_072",
    "text": "Σε ποιο διάσημο endless runner παιχνίδι για κινητά ο ήρωας τρέχει στις γραμμές του τρένου αποφεύγοντας εμπόδια και τον φύλακα με τον σκύλο του;",
    "answers": ["Sonic Dash", "Jetpack Joyride", "Flappy Bird", "Subway Surfers"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Subway Surfers δημιουργήθηκε από τις δανέζικες εταιρείες Kiloo και SYBO Games το 2012 και έγινε ένα από τα πιο κατεβασμένα παιχνίδια όλων των εποχών.",
    "funFacts": [
      "Έγινε το πρώτο παιχνίδι στην ιστορία του Google Play Store που ξεπέρασε το 1 δισεκατομμύριο λήψεις.",
      "Κάθε μήνα το παιχνίδι ανανεώνεται με την περιοδεία 'World Tour', μεταφέροντας τη δράση σε διαφορετικές διάσημες πόλεις του πλανήτη."
    ],
    "source": "https://el.wikipedia.org/wiki/Subway_Surfers",
    "locale": "el-GR",
    "tags": ["subway-surfers", "mobile", "casual", "endless-runner"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_073",
    "text": "Ποιος γοητευτικός ευγενής από τη Φλωρεντία της Αναγέννησης είναι ο πρωταγωνιστής της τριλογίας Assassin's Creed II, Brotherhood και Revelations;",
    "answers": ["Έτσιο Αουντιτόρε (Ezio Auditore)", "Αλταΐρ Ιμπν-Λα'Αχάντ", "Κόνορ Κένγουεϊ", "Έντουαρντ Κένγουεϊ"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Ezio Auditore da Firenze γίνεται Ασσασίνος για να εκδικηθεί την προδοσία και την εκτέλεση του πατέρα και των αδελφών του.",
    "funFacts": [
      "Στα παιχνίδια του Ezio, ο διάσημος εφευρέτης και καλλιτέχνης Λεονάρντο ντα Βίντσι λειτουργεί ως στενός φίλος και του κατασκευάζει όπλα και πτητικές μηχανές.",
      "Ο Ezio παραμένει ο μοναδικός πρωταγωνιστής της σειράς Assassin's Creed του οποίου η ζωή παρουσιάστηκε από τη γέννηση μέχρι τα γηρατειά του."
    ],
    "source": "https://en.wikipedia.org/wiki/Ezio_Auditore_da_Firenze",
    "locale": "el-GR",
    "tags": ["assassins-creed", "ezio", "ubisoft", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_074",
    "text": "Ποιο δημοφιλές δωρεάν multiplayer FPS της Valve διαθέτει καρτουνίστικο στυλ και εννέα μοναδικές κλάσεις χαρακτήρων όπως οι Heavy, Spy και Medic;",
    "answers": ["Dirty Bomb", "Team Fortress 2", "Paladins", "Left 4 Dead 2"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Team Fortress 2 κυκλοφόρησε το 2007 ως μέρος της συλλογής The Orange Box και καθιέρωσε το είδος του class-based multiplayer shooter.",
    "funFacts": [
      "Το παιχνίδι έγινε διάσημο για την οικονομία εικονικών αντικειμένων και καπέλων (hats), τα οποία οι παίκτες ανταλλάσσουν μέσω της πλατφόρμας Steam.",
      "Χρειάστηκε εννέα ολόκληρα χρόνια ανάπτυξης, καθώς ξεκίνησε ως ρεαλιστικό στρατιωτικό shooter πριν υιοθετήσει το καρτουνίστικο ύφος."
    ],
    "source": "https://el.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "valve", "fps", "pc-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_075",
    "text": "Ποια επιτυχημένη σειρά μουσικών παιχνιδιών της δεκαετίας του 2000 παιζόταν με ειδικό πλαστικό χειριστήριο σε σχήμα ηλεκτρικής κιθάρας;",
    "answers": ["Rocksmith", "DJ Hero", "Guitar Hero", "Band Hero"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Guitar Hero κυκλοφόρησε το 2005 από τη Harmonix και την RedOctane, επιτρέποντας στους παίκτες να παίζουν κλασικά ροκ σόλο πατώντας χρωματιστά πλήκτρα.",
    "funFacts": [
      "Το Guitar Hero III: Legends of Rock (2007) ήταν το πρώτο μεμονωμένο βιντεοπαιχνίδι στην ιστορία που ξεπέρασε το 1 δισεκατομμύριο δολάρια σε λιανικές πωλήσεις.",
      "Στο παιχνίδι εμφανίζονται ως ψηφιακοί αντίπαλοι θρύλοι της κιθάρας όπως ο Slash των Guns N' Roses και ο Tom Morello των Rage Against the Machine."
    ],
    "source": "https://el.wikipedia.org/wiki/Guitar_Hero",
    "locale": "el-GR",
    "tags": ["guitar-hero", "music", "rhythm", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_076",
    "text": "Ποιο είναι το όνομα του μπλε ανδροειδούς της Capcom με το ενσωματωμένο κανόνι στο χέρι, που πρωτοεμφανίστηκε στο NES το 1987;",
    "answers": ["Astro Boy", "Zero", "Proto Man", "Mega Man (Rockman)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Mega Man (γνωστός ως Rockman στην Ιαπωνία) δημιουργήθηκε από τον Dr. Light για να πολεμήσει τα μοχθηρά ρομπότ του Dr. Wily.",
    "funFacts": [
      "Το χαρακτηριστικό του γνώρισμα είναι ότι απορροφά και χρησιμοποιεί τα ειδικά όπλα των Robot Masters που νικά σε κάθε πίστα.",
      "Επιλέχθηκε το μπλε χρώμα επειδή η κονσόλα NES είχε τη μεγαλύτερη παλέτα διαφορετικών αποχρώσεων του μπλε."
    ],
    "source": "https://el.wikipedia.org/wiki/Mega_Man",
    "locale": "el-GR",
    "tags": ["mega-man", "capcom", "platformer", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_077",
    "text": "Σε ποια μυστηριώδη υποβρύχια Art Deco πόλη διαδραματίζεται το αριστουργηματικό παιχνίδι τρόμου και μυστηρίου «BioShock» (2007);",
    "answers": ["Rapture", "Columbia", "Atlantis", "Dunwall"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Rapture χτίστηκε στα βάθη του Ατλαντικού από τον οραματιστή επιχειρηματία Andrew Ryan ως καταφύγιο για την ελεύθερη επιστήμη και τέχνη.",
    "funFacts": [
      "Η πόλη καταστράφηκε από την εξάρτηση των κατοίκων της από το ADAM, μια γενετική ουσία που χαρίζει υπερφυσικές δυνάμεις.",
      "Η εμβληματική φράση χειραγώγησης 'Would you kindly' θεωρείται μία από τις μεγαλύτερες σεναριακές ανατροπές στην ιστορία των βιντεοπαιχνιδιών."
    ],
    "source": "https://el.wikipedia.org/wiki/BioShock",
    "locale": "el-GR",
    "tags": ["bioshock", "rapture", "fps", "story-rich"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_078",
    "text": "Ποια είναι η πριγκίπισσα με το ροζ φόρεμα που κυβερνά το Mushroom Kingdom και πέφτει συχνά θύμα απαγωγής από τον Bowser;",
    "answers": ["Πριγκίπισσα Daisy", "Πριγκίπισσα Peach (Πιτς)", "Rosalina", "Pauline"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Princess Peach είναι η κυριότερη γυναικεία φιγούρα στον κόσμο του Super Mario και ο λόγος για τις περισσότερες αποστολές διάσωσης του Mario.",
    "funFacts": [
      "Στα πρώτα δυτικά παιχνίδια (όπως στο αρχικό Super Mario Bros.), το όνομά της είχε αποδοθεί ως 'Princess Toadstool'.",
      "Πρωταγωνιστεί σε δικά της αυτόνομα παιχνίδια, όπως το Super Princess Peach (2005) και το Princess Peach: Showtime! (2024)."
    ],
    "source": "https://el.wikipedia.org/wiki/Πριγκίπισσα_Peach",
    "locale": "el-GR",
    "tags": ["princess-peach", "mario", "nintendo", "mushroom-kingdom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_079",
    "text": "Ποιο κλασικό παιχνίδι προσομοίωσης και στρατηγικής (1989) του Will Wright τοποθετεί τον παίκτη στον ρόλο του δημάρχου μιας αναπτυσσόμενης πόλης;",
    "answers": ["Cities: Skylines", "Civilization", "SimCity", "Tropico"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το SimCity έθεσε τις βάσεις για τα παιχνίδια οικοδόμησης πόλεων, απαιτώντας από τον παίκτη να σχεδιάζει δρόμους, ζώνες κατοικίας και παροχές ενέργειας.",
    "funFacts": [
      "Ο Will Wright εμπνεύστηκε το SimCity ενώ δημιουργούσε επίπεδα για ένα παιχνίδι με ελικόπτερα και διαπίστωσε ότι διασκέδαζε περισσότερο σχεδιάζοντας τους χάρτες.",
      "Οι παίκτες μπορούσαν ανά πάσα στιγμή να δοκιμάσουν την αντοχή της πόλης τους εξαπολύοντας καταστροφές όπως σεισμούς ή επιθέσεις τεράτων."
    ],
    "source": "https://el.wikipedia.org/wiki/SimCity",
    "locale": "el-GR",
    "tags": ["simcity", "maxis", "simulation", "city-builder"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_080",
    "text": "Τι συλλέγουν οι παίκτες νικώντας εχθρούς στη σειρά Dark Souls, το οποίο χρησιμεύει τόσο ως νόμισμα όσο και ως πόντοι εμπειρίας;",
    "answers": ["Χρυσό", "Ρούνους", "Σφαίρες αίματος", "Ψυχές (Souls)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Οι Ψυχές (Souls) είναι το απόλυτο μέσο συναλλαγής και αναβάθμισης χαρακτήρα. Εάν ο παίκτης πεθάνει, οι ψυχές παραμένουν στο σημείο θανάτου και χάνονται οριστικά με δεύτερο θάνατο.",
    "funFacts": [
      "Ο μηχανισμός απώλειας και ανάκτησης ψυχών καθιέρωσε ένα εντελώς νέο υπο-είδος παιχνιδιών που ονομάζεται 'Soulslike'.",
      "Ο δημιουργός Hidetaka Miyazaki δήλωσε ότι η υψηλή δυσκολία στοχεύει στο να δώσει στους παίκτες ένα αυθεντικό αίσθημα ικανοποίησης όταν ξεπερνούν τα εμπόδια."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "souls", "fromsoftware", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_081",
    "text": "Σε ποια μυστική ερευνητική εγκατάσταση στο Νέο Μεξικό εργαζόταν ο Gordon Freeman όταν συνέβη το καταστροφικό πείραμα στο αρχικό Half-Life;",
    "answers": ["Black Mesa", "Aperture Science", "Umbrella Facility", "Vault 101"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Black Mesa Research Facility είναι το υπόγειο συγκρότημα εργαστηρίων όπου ένα πείραμα τηλεμεταφοράς προκαλεί ρήξη και εισβολή εξωγήινων πλασμάτων.",
    "funFacts": [
      "Η Aperture Science (από τη σειρά Portal) παρουσιάζεται στο ίδιο σύμπαν ως η άσπονδη εμπορική ανταγωνίστρια της Black Mesa για κυβερνητικά κονδύλια.",
      "Μια ομάδα φίλων του παιχνιδιού δημιούργησε ένα πλήρες remake του αρχικού Half-Life με σύγχρονα γραφικά, το οποίο κυκλοφόρησε επίσημα με τον τίτλο 'Black Mesa'."
    ],
    "source": "https://en.wikipedia.org/wiki/Black_Mesa_Research_Facility",
    "locale": "el-GR",
    "tags": ["half-life", "black-mesa", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_082",
    "text": "Ποια είναι η διάσημη αντιαεροπορική κίνηση άλματος με ανοδική γροθιά που εκτελούν ο Ryu και ο Ken στη σειρά Street Fighter;",
    "answers": ["Hadoken", "Shoryuken (Dragon Punch)", "Tatsumaki Senpukyaku", "Flash Kick"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Shoryuken (που σημαίνει 'Γροθιά του Ανερχόμενου Δράκου') είναι η εμβληματική αντιαεροπορική επίθεση με άλμα των μαχητών του Ansatsuken.",
    "funFacts": [
      "Ένα λάθος στη μετάφραση της ατάκας νίκης του Ryu στο Street Fighter II οδήγησε στη δημιουργία του μυθικού ανύπαρκτου χαρακτήρα 'Sheng Long'.",
      "Η κίνηση εκτελείται με τον κλασικό συνδυασμό μοχλού: Μπροστά, Κάτω, Κάτω-Μπροστά + Γροθιά."
    ],
    "source": "https://en.wikipedia.org/wiki/Shoryuken",
    "locale": "el-GR",
    "tags": ["street-fighter", "shoryuken", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_083",
    "text": "Ποιο είναι το επίσημο όνομα του εξελιγμένου χειριστηρίου του PlayStation 5, γνωστό για την απτική ανάδραση και τις δυναμικές σκανδάλες;",
    "answers": ["DualShock 4", "Sixaxis", "DualSense", "PlayStation Move"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το DualSense αντικατέστησε τη σειρά DualShock, προσφέροντας εξελιγμένους ενεργοποιητές απτικής ανάδρασης (haptics) και σκανδάλες με αντίσταση (adaptive triggers).",
    "funFacts": [
      "Η επιφάνεια της λαβής του χειριστηρίου καλύπτεται από περίπου 40.000 μικροσκοπικά ανάγλυφα γεωμετρικά σύμβολα του PlayStation (τρίγωνο, κύκλος, χι, τετράγωνο).",
      "Διαθέτει επίσης ενσωματωμένο μικρόφωνο και ηχείο για άμεση συνομιλία χωρίς ακουστικά."
    ],
    "source": "https://el.wikipedia.org/wiki/PlayStation_5",
    "locale": "el-GR",
    "tags": ["playstation-5", "dualsense", "sony", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_084",
    "text": "Ποιο απλό επιτραπέζιο παιχνίδι ηλεκτρονικού τένις δύο διαστάσεων κυκλοφόρησε η Atari το 1972, ξεκινώντας τη βιομηχανία του gaming;",
    "answers": ["Space Invaders", "Asteroids", "Breakout", "Pong"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Pong σχεδιάστηκε από τον Allan Alcorn υπό την καθοδήγηση του Nolan Bushnell στην Atari και υπήρξε το πρώτο εμπορικά επιτυχημένο arcade παιχνίδι στον κόσμο.",
    "funFacts": [
      "Το πρώτο πρωτότυπο μηχάνημα arcade εγκαταστάθηκε σε μια τοπική παμπ στην Καλιφόρνια και χάλασε επειδή γέμισε ασφυκτικά με κέρματα.",
      "Η επιτυχία του Pong οδήγησε στην κυκλοφορία της οικιακής έκδοσης 'Home Pong' το 1975 μέσω των καταστημάτων Sears."
    ],
    "source": "https://el.wikipedia.org/wiki/Pong",
    "locale": "el-GR",
    "tags": ["pong", "atari", "retro-gaming", "arcade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_085",
    "text": "Ποιο εξαιρετικά απαιτητικό indie παιχνίδι δράσης (2017) διακρίθηκε για τα χειροποίητα γραφικά του στο στυλ των κινουμένων σχεδίων του 1930;",
    "answers": ["Cuphead", "Hollow Knight", "Celeste", "Ori and the Blind Forest"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Cuphead δημιουργήθηκε από το Studio MDHR με παραδοσιακή τεχνική σχεδιασμού στο χέρι καρέ-καρέ σε χαρτί.",
    "funFacts": [
      "Οι δημιουργοί υποθήκευσαν τα σπίτια τους για να χρηματοδοτήσουν την ολοκλήρωση του παιχνιδιού σύμφωνα με το αρχικό τους καλλιτεχνικό όραμα.",
      "Το παιχνίδι μεταφέρθηκε σε επιτυχημένη σειρά κινουμένων σχεδίων στο Netflix με τίτλο 'The Cuphead Show!'."
    ],
    "source": "https://el.wikipedia.org/wiki/Cuphead",
    "locale": "el-GR",
    "tags": ["cuphead", "indie", "platformer", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_086",
    "text": "Ποιος εμβληματικός νίντζα της φυλής Lin Kuei στη σειρά Mortal Kombat έχει την ικανότητα να παγώνει τους αντιπάλους του με κρυσταλλικό πάγο;",
    "answers": ["Scorpion", "Sub-Zero", "Reptile", "Noob Saibot"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Sub-Zero (Kuai Liang / Bi-Han) είναι ο κυριότερος αντίπαλος του Scorpion και διαθέτει κρυοκινητικές δυνάμεις ελέγχου του πάγου.",
    "funFacts": [
      "Ο αρχικός Sub-Zero (Bi-Han) σκοτώνεται στο πρώτο τουρνουά και ανασταίνεται στον Κάτω Κόσμο ως ο σκοτεινός νίντζα Noob Saibot.",
      "Η διάσημη κίνηση εξόντωσής του (Spine Rip Fatality), όπου ξεριζώνει το κρανίο και τη σπονδυλική στήλη του αντιπάλου, ήταν από τις πιο πολυσυζητημένες της δεκαετίας του '90."
    ],
    "source": "https://en.wikipedia.org/wiki/Sub-Zero_(Mortal_Kombat)",
    "locale": "el-GR",
    "tags": ["mortal-kombat", "sub-zero", "fighting", "ninjas"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_087",
    "text": "Ποια θρυλική οικογένεια κυνηγών βρικολάκων πολεμά τις σκοτεινές δυνάμεις του Κόμη Δράκουλα με το ιερό μαστίγιο στη σειρά «Castlevania»;",
    "answers": ["Βαν Χέλσινγκ", "Τζοεστάρ", "Μπέλμοντ (Belmont)", "Ρέντφιλντ"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η οικογένεια Belmont (με εκπροσώπους όπως ο Simon, ο Richter και ο Trevor Belmont) κρατά το ιερό μαστίγιο 'Vampire Killer'.",
    "funFacts": [
      "Το Castlevania: Symphony of the Night (1997) συνδύασε εξερεύνηση και στοιχεία RPG, γεννώντας τον όρο 'Metroidvania'.",
      "Η εξαιρετικά δημοφιλής σειρά anime Castlevania στο Netflix βασίζεται κυρίως στα γεγονότα του Castlevania III: Dracula's Curse."
    ],
    "source": "https://el.wikipedia.org/wiki/Castlevania",
    "locale": "el-GR",
    "tags": ["castlevania", "konami", "vampires", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_088",
    "text": "Ποιος θρυλικός πράκτορας μυστικών αποστολών και ειδικός στο stealth πρωταγωνιστεί στη σειρά «Metal Gear Solid» του Hideo Kojima;",
    "answers": ["Sam Fisher", "Agent 47", "Gabriel Logan", "Solid Snake"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Solid Snake (David) είναι ο επίλεκτος στρατιώτης της μονάδας FOXHOUND που αναλαμβάνει να εξουδετερώσει πυρηνικά εξοπλισμένα διποδικά τανκς (Metal Gear).",
    "funFacts": [
      "Η εμφάνιση του Snake βασίστηκε εν μέρει στον χαρακτήρα Snake Plissken που υποδύθηκε ο Kurt Russell στην ταινία 'Απόδραση από τη Νέα Υόρκη'.",
      "Ένα από τα πιο διάσημα κωμικά εργαλεία καμουφλάζ του Snake στις αποστολές του είναι ένα απλό χαρτόκουτο (cardboard box)."
    ],
    "source": "https://el.wikipedia.org/wiki/Solid_Snake",
    "locale": "el-GR",
    "tags": ["metal-gear", "solid-snake", "stealth", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_089",
    "text": "Ποιος ευτραφής τρελός επιστήμονας με το μεγάλο μουστάκι είναι ο αιώνιος ορκισμένος εχθρός του Sonic the Hedgehog;",
    "answers": ["Dr. Eggman (Dr. Robotnik)", "Dr. Wily", "Dr. Neo Cortex", "Bowser"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Dr. Ivo Robotnik (γνωστός και ως Eggman) σχεδιάζει διαρκώς να μετατρέψει τα ζώα σε ρομπότ και να κατακτήσει τον κόσμο.",
    "funFacts": [
      "Στην Ιαπωνία ήταν πάντα γνωστός ως Dr. Eggman λόγω του αυγοειδούς σχήματος του σώματός του, ενώ στη Δύση είχε αρχικά ονομαστεί Dr. Ivo Robotnik.",
      "Στις κινηματογραφικές ταινίες του Sonic, τον Dr. Robotnik υποδύεται ο διάσημος κωμικός Jim Carrey."
    ],
    "source": "https://el.wikipedia.org/wiki/Dr._Eggman",
    "locale": "el-GR",
    "tags": ["sonic", "eggman", "sega", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_090",
    "text": "Σε ποιο υπόγειο, μυστηριώδες και ερειπωμένο βασίλειο εντόμων διαδραματίζεται το βραβευμένο indie Metroidvania «Hollow Knight»;",
    "answers": ["Deepnest", "Hallownest", "Hallowfall", "Dirtmouth"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Hallownest είναι ένα τεράστιο υπόγειο βασίλειο που καταστράφηκε από μια μυστηριώδη μόλυνση (The Infection) και κατοικείται από έντομα.",
    "funFacts": [
      "Το Hollow Knight αναπτύχθηκε από μια μικρή ανεξάρτητη ομάδα μόλις τριών ατόμων στην Αδελαΐδα της Αυστραλίας (Team Cherry).",
      "Η ανάπτυξη του παιχνιδιού χρηματοδοτήθηκε αρχικά μέσω μιας εκστρατείας στο Kickstarter το 2014, συγκεντρώνοντας περίπου 57.000 δολάρια Αυστραλίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
    "locale": "el-GR",
    "tags": ["hollow-knight", "metroidvania", "indie", "hallownest"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_091",
    "text": "Ποιο Pokémon φωτιάς τύπου σαύρας με μια αναμμένη φλόγα στην άκρη της ουράς του είναι ένα από τα τρία αρχικά της πρώτης γενιάς (Kanto);",
    "answers": ["Σίντακουιλ (Cyndaquil)", "Τόρτσιτς (Torchic)", "Τσάρμαντερ (Charmander)", "Τσίμτσαρ (Chimchar)"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Charmander είναι το βασικό Pokémon φωτιάς της πρώτης γενιάς, το οποίο εξελίσσεται στον Charmeleon και τελικά στον πανίσχυρο Charizard.",
    "funFacts": [
      "Εάν η φλόγα στην ουρά του Charmander σβήσει εντελώς, το Pokémon κινδυνεύει να χάσει τη ζωή του.",
      "Η κάρτα πρώτης έκδοσης του Charizard (Base Set 1st Edition) από το αρχικό παιχνίδι καρτών έχει πουληθεί σε δημοπρασίες για πάνω από 300.000 δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/Charmander",
    "locale": "el-GR",
    "tags": ["pokemon", "charmander", "nintendo", "kanto"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_092",
    "text": "Ποιος κυβερνήτης του διαστημοπλοίου Normandy είναι ο κεντρικός πρωταγωνιστής της αρχικής τριλογίας επιστημονικής φαντασίας «Mass Effect»;",
    "answers": ["Captain Price", "Isaac Clarke", "Gordon Freeman", "Commander Shepard"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο/Η Commander Shepard (του οποίου το φύλο και την εμφάνιση επιλέγει ελεύθερα ο παίκτης) ηγείται του αγώνα ενάντια στην απειλή των Reapers.",
    "funFacts": [
      "Το όνομα Shepard δόθηκε προς τιμήν του Alan Shepard, του πρώτου Αμερικανού αστροναύτη που ταξίδεψε στο διάστημα το 1961.",
      "Οι επιλογές και οι αποφάσεις του παίκτη μεταφέρονταν απευθείας από το ένα παιχνίδι στο επόμενο μέσω των αποθηκευμένων αρχείων (save files)."
    ],
    "source": "https://el.wikipedia.org/wiki/Mass_Effect_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["mass-effect", "bioware", "sci-fi", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_093",
    "text": "Ποιο χαρακτηριστικό μαγικό όπλο σε σχήμα μεγάλου κλειδιού κρατά ο νεαρός Sora στη σειρά παιχνιδιών «Kingdom Hearts»;",
    "answers": ["Keyblade", "Gunblade", "Master Sword", "Buster Sword"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Keyblade (Κλειδοσπάθι) είναι το μυστηριώδες όπλο που επιλέγει τον φορέα του και έχει τη δύναμη να κλειδώνει και να ξεκλειδώνει πύλες ανάμεσα στους κόσμους.",
    "funFacts": [
      "Το πρώτο Keyblade που αποκτά ο Sora ονομάζεται 'Kingdom Key' και φέρει ως μπρελόκ τη σιλουέτα του κεφαλιού του Mickey Mouse.",
      "Αρχικά, η Disney επιθυμούσε ο πρωταγωνιστής να είναι ο Donald Duck, ενώ η Square προτιμούσε τον Mickey, πριν συμφωνήσουν στη δημιουργία ενός εντελώς νέου ήρωα (Sora)."
    ],
    "source": "https://en.wikipedia.org/wiki/Kingdom_Hearts",
    "locale": "el-GR",
    "tags": ["kingdom-hearts", "square-enix", "disney", "keyblade"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_094",
    "text": "Σε ποια βασική δραστηριότητα επικεντρώνεται το δημοφιλές χαλαρωτικό indie παιχνίδι «Stardew Valley» του Eric Barone;",
    "answers": ["Διαστημικές μάχες", "Καλλιέργεια φάρμας και αγροτική ζωή", "Αγώνες ταχύτητας με αυτοκίνητα", "Κατασκευή θεματικών πάρκων"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Στο Stardew Valley, ο παίκτης κληρονομεί το παλιό αγρόκτημα του παππού του και αναλαμβάνει να καλλιεργήσει τη γη, να εκθρέψει ζώα και να κοινωνικοποιηθεί.",
    "funFacts": [
      "Ο Eric Barone (γνωστός ως ConcernedApe) ανέπτυξε μόνος του ολόκληρο το παιχνίδι σε διάστημα 4,5 ετών, γράφοντας τον κώδικα, σχεδιάζοντας τα pixel art και συνθέτοντας τη μουσική.",
      "Το παιχνίδι άντλησε άμεση έμπνευση από την κλασική ιαπωνική σειρά αγροτικής προσομοίωσης Harvest Moon."
    ],
    "source": "https://el.wikipedia.org/wiki/Stardew_Valley",
    "locale": "el-GR",
    "tags": ["stardew-valley", "farming", "indie", "simulation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_095",
    "text": "Ποια αρχαία μαγική ξύλινη μάσκα πνεύματος με πολύχρωμα φτερά προστατεύει τον Crash Bandicoot από τους κινδύνους;",
    "answers": ["Uka Uka", "Ouka Ouka", "Aku Aku", "Tikimon"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Aku Aku είναι το πνεύμα ενός αρχαίου μάγου γιατρού που καθοδηγεί και προστατεύει τον Crash και την Coco απέναντι στα σχέδια του Dr. Cortex.",
    "funFacts": [
      "Εάν ο παίκτης συγκεντρώσει τρεις μάσκες Aku Aku στη σειρά, ο Crash αποκτά προσωρινή απόλυτη ατρωσία και αυξημένη ταχύτητα.",
      "Ο αδελφός του Aku Aku είναι ο μοχθηρός Uka Uka, ο οποίος συμμαχεί με τον Dr. Neo Cortex."
    ],
    "source": "https://en.wikipedia.org/wiki/Crash_Bandicoot_(character)",
    "locale": "el-GR",
    "tags": ["crash-bandicoot", "aku-aku", "playstation", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_096",
    "text": "Πόσες πύλες (portals) διαφορετικού χρώματος (μία μπλε και μία πορτοκαλί) μπορεί να ανοίξει ταυτόχρονα το όπλο πυλών στο «Portal»;",
    "answers": ["Τέσσερις (4)", "Τρεις (3)", "Μία (1)", "Δύο (2)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Aperture Science Handheld Portal Device ανοίγει ακριβώς δύο πύλες: ό,τι μπαίνει από τη μία πύλη εξέρχεται ακαριαία από την άλλη διατηρώντας την ορμή του.",
    "funFacts": [
      "Ο θεμελιώδης κανόνας της φυσικής των πυλών συνοψίζεται στη φράση του παιχνιδιού: 'Speedy thing goes in, speedy thing comes out'.",
      "Η αρχική ιδέα του μηχανισμού πυλών προήλθε από το φοιτητικό project 'Narbacular Drop' του πανεπιστημίου DigiPen, του οποίου οι δημιουργοί προσλήφθηκαν άμεσα από τη Valve."
    ],
    "source": "https://el.wikipedia.org/wiki/Portal_(%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%AF%CE%B4%CE%B9)",
    "locale": "el-GR",
    "tags": ["portal", "valve", "puzzle", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_097",
    "text": "Ποιο εξαιρετικά δημοφιλές 2D sandbox παιχνίδι εξόρυξης, κατασκευών και επιβίωσης κυκλοφόρησε η Re-Logic το 2011;",
    "answers": ["Terraria", "Starbound", "Spelunky", "Don't Starve"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Terraria συνδυάζει κλασική δράση 2D platformer με εξόρυξη υλικών, κατασκευή όπλων και εξοπλισμού, και μάχες ενάντια σε γιγάντια bosses.",
    "funFacts": [
      "Έχει πουλήσει πάνω από 58 εκατομμύρια αντίτυπα παγκοσμίως, όντας ένα από τα εμπορικότερα ανεξάρτητα παιχνίδια στην ιστορία.",
      "Παρόλο που χαρακτηρίστηκε αρχικά από ορισμένους ως '2D Minecraft', διαθέτει πολύ μεγαλύτερη έμφαση στη μάχη, την ποικιλία εξοπλισμού και τα RPG στοιχεία."
    ],
    "source": "https://el.wikipedia.org/wiki/Terraria",
    "locale": "el-GR",
    "tags": ["terraria", "sandbox", "indie", "2d"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_098",
    "text": "Ποιο είναι το ιερό χρυσό κειμήλιο τριών τριγώνων που αντιπροσωπεύει τη Δύναμη, τη Σοφία και το Θάρρος στο σύμπαν της Zelda;",
    "answers": ["Ring of Power", "Triforce (Τρίφορς)", "Ocarina of Time", "Hylian Crest"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Triforce αφέθηκε στον κόσμο της Hyrule από τις τρεις χρυσές θεές (Din, Nayru και Farore) και εκπληρώνει τις επιθυμίες όποιου το αγγίξει.",
    "funFacts": [
      "Κάθε κομμάτι συνδέεται με έναν χαρακτήρα: η Δύναμη με τον Ganon, η Σοφία με την πριγκίπισσα Zelda και το Θάρρος με τον Link.",
      "Το σύμβολο του Triforce βασίζεται στο ιστορικό οικόσημο (mon) της ιαπωνικής φατρίας Hojo."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Legend_of_Zelda",
    "locale": "el-GR",
    "tags": ["zelda", "triforce", "nintendo", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_099",
    "text": "Ποιος επαναστάτης πρίγκιπας και γιος του θεού Άδη είναι ο κεντρικός πρωταγωνιστής του βραβευμένου roguelike παιχνιδιού «Hades»;",
    "answers": ["Θησέας", "Αχιλλέας", "Ζαγρέας (Zagreus)", "Χάροντας"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Ζαγρέας προσπαθεί να αποδράσει από το βασίλειο των νεκρών για να βρει τη βιολογική του μητέρα Περσεφόνη, δεχόμενος ευλογίες από τους Ολύμπιους θεούς.",
    "funFacts": [
      "Το Hades ήταν το πρώτο βιντεοπαιχνίδι στην ιστορία που τιμήθηκε ποτέ με το κορυφαίο λογοτεχνικό βραβείο επιστημονικής φαντασίας Hugo Award (2021).",
      "Ο Ζαγρέας είναι μια υπαρκτή αλλά λιγότερο γνωστή θεότητα της αρχαίας ελληνικής μυθολογίας και του Ορφισμού."
    ],
    "source": "https://el.wikipedia.org/wiki/Hades_(%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%AF%CE%B4%CE%B9)",
    "locale": "el-GR",
    "tags": ["hades", "supergiant-games", "roguelike", "greek-mythology"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_100",
    "text": "Ποιος είναι ο αξιομνημόνευτος πρωταγωνιστής που επιστρέφει στη γειτονιά του στο Los Santos στο θρυλικό «GTA: San Andreas» (2004);",
    "answers": ["Tommy Vercetti", "Niko Bellic", "Franklin Clinton", "Carl 'CJ' Johnson"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Carl 'CJ' Johnson επιστρέφει στο Los Santos μετά τη δολοφονία της μητέρας του και αναλαμβάνει να επαναφέρει τη συμμορία Grove Street Families στην κορυφή.",
    "funFacts": [
      "Τη φωνή του CJ δάνεισε ο Αμερικανός ράπερ Young Maylay, ο οποίος ήταν ξάδερφος ενός παραγωγού της Rockstar Games.",
      "Η ατάκα του CJ 'Ah shit, here we go again' στην εισαγωγική σκηνή έγινε ένα από τα πιο διάσημα memes στην ιστορία του ίντερνετ."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas",
    "locale": "el-GR",
    "tags": ["gta", "san-andreas", "cj", "rockstar-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_101",
    "text": "Σε ποιο δημοφιλές ασύμμετρο multiplayer παιχνίδι τρόμου τέσσερις επιζώντες επισκευάζουν γεννήτριες για να ξεφύγουν από έναν δολοφόνο;",
    "answers": ["Dead by Daylight", "Friday the 13th", "Texas Chain Saw Massacre", "Outlast Trials"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Dead by Daylight (Behaviour Interactive) φέρνει αντιμέτωπους τέσσερις ανυπεράσπιστους επιζώντες εναντίον ενός πανίσχυρου δολοφόνου πρώτου προσώπου.",
    "funFacts": [
      "Φιλοξενεί διάσημους εμβληματικούς δολοφόνους από ταινίες τρόμου, όπως ο Michael Myers, ο Freddy Krueger, ο Ghostface και ο Leatherface.",
      "Οι επιζώντες πρέπει να επισκευάσουν πέντε γεννήτριες σε όλο τον χάρτη για να τροφοδοτήσουν με ρεύμα τις πύλες εξόδου."
    ],
    "source": "https://en.wikipedia.org/wiki/Dead_by_Daylight",
    "locale": "el-GR",
    "tags": ["dead-by-daylight", "horror", "multiplayer", "asymmetrical"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_102",
    "text": "Σε ποιο multiplayer παιχνίδι περιπέτειας της Rare οι παίκτες γίνονται πειρατές, επανδρώνουν ιστιοφόρα πλοία και αναζητούν θαμμένους θησαυρούς;",
    "answers": ["Skull and Bones", "Sea of Thieves", "Blackwake", "Assassin's Creed IV"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Sea of Thieves κυκλοφόρησε το 2018 και επιτρέπει σε πληρώματα φίλων να πλοηγούνται, να χειρίζονται τα πανιά και τα κανόνια, και να πολεμούν θαλάσσια τέρατα.",
    "funFacts": [
      "Ο μυθικός γιγάντιος Κράκεν μπορεί να επιτεθεί αιφνιδιαστικά σε οποιοδήποτε πλοίο, μαυρίζοντας το νερό και τυλίγοντας τα πλοκάμια του γύρω από το κατάστρωμα.",
      "Περιλαμβάνει επίσημες θεματικές ιστορίες συνεργασίας με τους 'Πειρατές της Καραϊβικής' και τη σειρά Monkey Island."
    ],
    "source": "https://en.wikipedia.org/wiki/Sea_of_Thieves",
    "locale": "el-GR",
    "tags": ["sea-of-thieves", "rare", "pirates", "multiplayer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_103",
    "text": "Ποιο φρούτο αποτελεί το πρώτο και πιο αναγνωρίσιμο bonus αντικείμενο που εμφανίζεται στο κέντρο του λαβύρινθου στο κλασικό Pac-Man;",
    "answers": ["Φράουλα", "Πορτοκάλι", "Κεράσια (Cherries)", "Μήλο"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Τα Κεράσια εμφανίζονται στο πρώτο επίπεδο του Pac-Man ακριβώς κάτω από το κελί των φαντασμάτων και προσφέρουν 100 επιπλέον πόντους.",
    "funFacts": [
      "Στα επόμενα επίπεδα εμφανίζονται διαδοχικά φράουλες (300 πόντοι), πορτοκάλια (500 πόντοι), μήλα, πεπόνια, καθώς και κλειδιά που δίνουν 5.000 πόντους.",
      "Το μέγιστο δυνατό σκορ στο αρχικό arcade Pac-Man είναι 3.333.360 πόντοι, γνωστό ως 'τέλειο παιχνίδι' (perfect game)."
    ],
    "source": "https://el.wikipedia.org/wiki/Pac-Man",
    "locale": "el-GR",
    "tags": ["pac-man", "arcade", "retro-gaming", "namco"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_104",
    "text": "Ποιο είναι το όνομα του εκκεντρικού, υπερκινητικού και ασταμάτητα ομιλητικού κίτρινου μονορόδιου ρομπότ στη σειρά «Borderlands»;",
    "answers": ["Dethklok", "Bumblebee", "R2-D2", "Claptrap"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Claptrap (μοντέλο CL4P-TP) είναι η ανεπίσημη μασκότ της σειράς Borderlands της Gearbox Software, γνωστός για την κωμική του ανασφάλεια και τις γκάφες του.",
    "funFacts": [
      "Η μεγαλύτερη γνωστή αδυναμία και απόλυτος φόβος του Claptrap στα παιχνίδια είναι... οι σκάλες, καθώς κινείται πάνω σε έναν μόνο τροχό.",
      "Στην κινηματογραφική ταινία Borderlands (2024), τη φωνή του Claptrap δάνεισε ο Jack Black."
    ],
    "source": "https://en.wikipedia.org/wiki/Claptrap",
    "locale": "el-GR",
    "tags": ["borderlands", "claptrap", "gearbox", "looter-shooter"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_105",
    "text": "Στους κανόνες ποιου παγκοσμίως διάσημου επιτραπέζιου παιχνιδιού ρόλων (TTRPG) βασίζεται εξ ολοκλήρου το «Baldur's Gate 3»;",
    "answers": ["Dungeons & Dragons (D&D)", "Pathfinder", "Warhammer 40,000", "Call of Cthulhu"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Baldur's Gate 3 της Larian Studios βασίζεται πιστά στους κανόνες της 5ης έκδοσης του Dungeons & Dragons και διαδραματίζεται στον κόσμο των Forgotten Realms.",
    "funFacts": [
      "Κέρδισε το βραβείο Game of the Year στα The Game Awards 2023 και σάρωσε σχεδόν κάθε μεγάλη διάκριση στη βιομηχανία.",
      "Όλοι οι διάλογοι και οι κινήσεις των χαρακτήρων ηχογραφήθηκαν και αποδόθηκαν με motion capture από επαγγελματίες ηθοποιούς, δημιουργώντας πάνω από 170 ώρες cutscenes."
    ],
    "source": "https://el.wikipedia.org/wiki/Baldur%27s_Gate_3",
    "locale": "el-GR",
    "tags": ["baldurs-gate-3", "dnd", "larian-studios", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_106",
    "text": "Τι είδους φιλικό προϊστορικό πλάσμα είναι ο Yoshi, ο οποίος εμφανίστηκε στο Super Mario World και μεταφέρει τον Mario στην πλάτη του;",
    "answers": ["Δράκος", "Δεινόσαυρος", "Σαύρα", "Χελώνα"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Yoshi είναι ένα είδος ανθρωπόμορφου δεινοσαύρου (Yoshi species) που ζει στο Dinosaur Land και χρησιμοποιεί τη μακριά κολλώδη γλώσσα του για να καταπίνει εχθρούς.",
    "funFacts": [
      "Ο Shigeru Miyamoto ήθελε ο Mario να ιππεύει έναν δεινόσαυρο ήδη από το πρώτο Super Mario Bros., αλλά οι τεχνικοί περιορισμοί του NES δεν το επέτρεπαν μέχρι το SNES.",
      "Όταν ο Yoshi καταπίνει εχθρούς, μπορεί να τους μετατρέψει στιγμιαία σε αυγά με βούλες και να τα εκτοξεύσει ως όπλα."
    ],
    "source": "https://el.wikipedia.org/wiki/Yoshi",
    "locale": "el-GR",
    "tags": ["yoshi", "mario", "nintendo", "platformer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_107",
    "text": "Ποια εκκεντρική πρωταθλήτρια με μακριές μπλε κοτσίδες και εμμονή με τα εκρηκτικά πρωταγωνιστεί στο League of Legends και στη σειρά «Arcane»;",
    "answers": ["Vi", "Caitlyn", "Jinx", "Lux"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Η Jinx (The Loose Cannon) κατάγεται από την υπόγεια πόλη Zaun και σπέρνει το χάος με το οπλοστάσιό της, που περιλαμβάνει το πολυβόλο 'Pow-Pow' και τον εκτοξευτή 'Fishbones'.",
    "funFacts": [
      "Η Jinx είναι η μικρότερη αδελφή της Vi (Violet), μια τραγική σχέση που αναλύεται σε βάθος στην πολυβραβευμένη σειρά κινουμένων σχεδίων 'Arcane'.",
      "Ήταν η πρώτη πρωταθλήτρια στην ιστορία του League of Legends που απέκτησε το δικό της επίσημο μουσικό βίντεο κινουμένων σχεδίων ('Get Jinxed') το 2013."
    ],
    "source": "https://en.wikipedia.org/wiki/Jinx_(League_of_Legends)",
    "locale": "el-GR",
    "tags": ["jinx", "league-of-legends", "arcane", "riot-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_108",
    "text": "Ποιες τρεις μοναδικές και ασύμμετρα ισορροπημένες παρατάξεις συγκρούονται στο ιστορικό RTS «StarCraft» της Blizzard;",
    "answers": ["Ορκ, Άνθρωποι, Ξωτικά", "Συμμαχία, Ορδή, Απέθαντοι", "GDI, Nod, Scrin", "Terran, Zerg, Protoss"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το StarCraft (1998) καθιέρωσε την απόλυτη ισορροπία τριών εντελώς διαφορετικών φατριών: των ανθρώπων Terran, των εντομοειδών Zerg και των υπερεξελιγμένων Protoss.",
    "funFacts": [
      "Στη Νότια Κορέα, το StarCraft εξελίχθηκε σε εθνικό άθλημα με ειδικά τηλεοπτικά κανάλια 24ωρης μετάδοσης αγώνων και επαγγελματίες παίκτες που λατρεύονταν ως διασημότητες.",
      "Η τακτική αιφνιδιαστικής μαζικής επίθεσης με φθηνές μονάδες Zergling γέννησε τον παγκόσμιο όρο 'Zerg rush'."
    ],
    "source": "https://el.wikipedia.org/wiki/StarCraft",
    "locale": "el-GR",
    "tags": ["starcraft", "blizzard", "rts", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_109",
    "text": "Ποιο τερατώδες βιολογικό όπλο της Umbrella καταδιώκει ασταμάτητα την Jill Valentine στο «Resident Evil 3: Nemesis»;",
    "answers": ["Nemesis", "Mr. X (Tyrant T-103)", "Licker", "William Birkin"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Ο Nemesis είναι ένας εξελιγμένος Τύραννος σχεδιασμένος με ένα μόνο σκοπό: την εξόντωση όλων των εναπομεινάντων μελών της ομάδας S.T.A.R.S.",
    "funFacts": [
      "Η μόνη λέξη που προφέρει με ανατριχιαστική βαριά φωνή κατά τη διάρκεια των επιθέσεών του είναι: 'S.T.A.R.S....'.",
      "Είναι εξοπλισμένος με εκτοξευτή ρουκετών και μπορεί να τρέχει πιο γρήγορα από τον χαρακτήρα του παίκτη, σπάζοντας πόρτες και τοίχους."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil_3:_Nemesis",
    "locale": "el-GR",
    "tags": ["resident-evil", "nemesis", "capcom", "survival-horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_easy_110",
    "text": "Ποιο στοιχείο της φύσης ελέγχει και εκπέμπει το μαγικό τσεκούρι Leviathan του Κράτου στα νεότερα παιχνίδια God of War;",
    "answers": ["Φωτιά", "Πάγος / Παγετός", "Κεραυνός", "Δηλητήριο"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 1,
    "explanation": "Το Leviathan Axe είναι εμποτισμένο με τη δύναμη του πάγου, επιτρέποντας στον Κράτο να παγώνει μηχανισμούς και εχθρούς όταν το εκτοξεύει.",
    "funFacts": [
      "Το τσεκούρι κατασκευάστηκε από τα αδέλφια νάνους Brok και Sindri, τους ίδιους σιδηρουργούς που είχαν σφυρηλατήσει και το σφυρί Mjölnir του Thor.",
      "Ο Κράτος μπορεί να ανακαλέσει το τσεκούρι πίσω στο χέρι του από οποιαδήποτε απόσταση, με μηχανισμό εμπνευσμένο από το σφυρί του Thor."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "kratos", "leviathan-axe", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'easy', 1, questions)

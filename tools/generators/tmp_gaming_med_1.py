# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_med_011",
    "text": "Ποια διαγαλαξιακή κυνηγός επικηρυγμένων με τη στολή Power Suit είναι η πρωταγωνίστρια της ιστορικής σειράς «Metroid» της Nintendo;",
    "answers": ["Σάμους Αράν (Samus Aran)", "Τζιλ Βάλενταϊν", "Λάρα Κροφτ", "Τζοάνα Νταρκ"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Samus Aran πρωτοεμφανίστηκε στο Metroid (1986) για το NES και ήταν μία από τις πρώτες γυναίκες πρωταγωνίστριες στην ιστορία των βιντεοπαιχνιδιών.",
    "funFacts": [
      "Στο τέλος του αρχικού Metroid, εάν ο παίκτης ολοκλήρωνε γρήγορα το παιχνίδι, η Samus έβγαζε το κράνος της αποκαλύπτοντας προς έκπληξη όλων ότι ήταν γυναίκα.",
      "Το επώνυμό της 'Aran' επιλέχθηκε από τον συνδημιουργό Hiroji Kiyotake επειδή εμπνεύστηκε από το πραγματικό όνομα του θρυλικού ποδοσφαιριστή Πελέ (Edson Arantes do Nascimento)."
    ],
    "source": "https://el.wikipedia.org/wiki/Metroid",
    "locale": "el-GR",
    "tags": ["metroid", "samus-aran", "nintendo", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_012",
    "text": "Ποια φυλή πετρωδών πλασμάτων που τρέφονται με βράχους και κυλούν σαν μπάλες ζει στο Death Mountain στο σύμπαν της Zelda;",
    "answers": ["Zora", "Goron (Γκόρον)", "Gerudo", "Rito"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Gorons είναι μια φιλήσυχη και δυνατή φυλή ανθρωπόμορφων πλασμάτων που κατοικούν σε ηφαιστειακές περιοχές και είναι αδελφικοί φίλοι του Link.",
    "funFacts": [
      "Στο Ocarina of Time (1998), ο ηγέτης των Goron, Darunia, ονομάζει τον γιο του 'Link' προς τιμήν του ήρωα.",
      "Παρά το τεράστιο βάρος τους και τη διατροφή τους με πέτρες, οι Gorons είναι εξαιρετικοί μουσικοί και λατρεύουν τους χορούς."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Legend_of_Zelda",
    "locale": "el-GR",
    "tags": ["zelda", "goron", "nintendo", "ocarina-of-time"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_013",
    "text": "Ποιος διακεκριμένος δημιουργός και επικεφαλής της Irrational Games σχεδίασε το System Shock 2 και το αρχικό «BioShock»;",
    "answers": ["Cliff Bleszinski", "Todd Howard", "Ken Levine", "Warren Spector"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Ken Levine υπήρξε ο βασικός σεναριογράφος και σκηνοθέτης των BioShock και BioShock Infinite, συνδυάζοντας φιλοσοφικά ερωτήματα με ατμοσφαιρικό gameplay.",
    "funFacts": [
      "Για τη συγγραφή του BioShock μελέτησε εις βάθος τα βιβλία και τη φιλοσοφία του αντικειμενισμού της Ayn Rand.",
      "Η διάσημη φράση 'Would you kindly' σχεδιάστηκε για να ασκήσει κριτική στην τυφλή υπακοή των παικτών στις οδηγίες των βιντεοπαιχνιδιών."
    ],
    "source": "https://en.wikipedia.org/wiki/Ken_Levine_(game_developer)",
    "locale": "el-GR",
    "tags": ["bioshock", "ken-levine", "irrational-games", "directors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_014",
    "text": "Ποιο ιστορικό JRPG του 1995 στο SNES δημιουργήθηκε από την «Ομάδα των Ονείρων» (Sakaguchi, Yuji Horii και Akira Toriyama);",
    "answers": ["Secret of Mana", "EarthBound", "Final Fantasy VI", "Chrono Trigger"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Chrono Trigger της Square θεωρείται ένα από τα σπουδαιότερα παιχνίδια ρόλων όλων των εποχών, εισάγοντας ταξίδια στον χρόνο και πολλαπλά τέλη.",
    "funFacts": [
      "Ο δημιουργός του Dragon Ball, Akira Toriyama, ανέλαβε εξ ολοκλήρου τον σχεδιασμό των χαρακτήρων και των τεράτων του παιχνιδιού.",
      "Διέθετε πάνω από 13 διαφορετικά φινάλε ανάλογα με τη χρονική περίοδο και τον τρόπο που ο παίκτης αντιμετώπιζε το τελικό αφεντικό Lavos."
    ],
    "source": "https://el.wikipedia.org/wiki/Chrono_Trigger",
    "locale": "el-GR",
    "tags": ["chrono-trigger", "square", "snes", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_015",
    "text": "Ποιο ήταν το πρώτο επίσημο πακέτο επέκτασης (expansion) που κυκλοφόρησε για το «World of Warcraft» το 2007;",
    "answers": ["The Burning Crusade", "Wrath of the Lich King", "Cataclysm", "Mists of Pandaria"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το World of Warcraft: The Burning Crusade άνοιξε τη Σκοτεινή Πύλη (Dark Portal) προς τον κατεστραμμένο κόσμο του Outland και αύξησε το level cap στο 70.",
    "funFacts": [
      "Εισήγαγε για πρώτη φορά τα ιπτάμενα υποζύγια (flying mounts) και δύο νέες playable φυλές: τα Blood Elves και τους Draenei.",
      "Πούλησε σχεδόν 2,4 εκατομμύρια αντίτυπα μέσα στις πρώτες 24 ώρες κυκλοφορίας του, σπάζοντας το ρεκόρ ταχύτερων πωλήσεων παιχνιδιού για PC της εποχής."
    ],
    "source": "https://el.wikipedia.org/wiki/World_of_Warcraft:_The_Burning_Crusade",
    "locale": "el-GR",
    "tags": ["warcraft", "burning-crusade", "blizzard", "mmorpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_016",
    "text": "Ποια θρυλική εσωτερική ομάδα ανάπτυξης της Konami δημιούργησε τα τέσσερα πρώτα κλασικά παιχνίδια ψυχολογικού τρόμου «Silent Hill»;",
    "answers": ["Capcom Production Studio 4", "Team Silent", "Climax Studios", "Tango Gameworks"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Team Silent ήταν υπεύθυνη για τα Silent Hill 1 έως 4, καθιερώνοντας τον ψυχολογικό τρόμο, την ομίχλη και την απόκοσμη μουσική του Akira Yamaoka.",
    "funFacts": [
      "Η πυκνή ομίχλη στην πόλη σχεδιάστηκε αρχικά για τεχνικούς λόγους, ώστε να κρύβει την περιορισμένη απόσταση σχεδίασης γραφικών του PlayStation 1.",
      "Ο εμβληματικός τέρας Pyramid Head (Τριγωνοκέφαλος) σχεδιάστηκε από τον καλλιτέχνη Masahiro Ito ως εκδήλωση των ενοχών του James Sunderland στο Silent Hill 2."
    ],
    "source": "https://el.wikipedia.org/wiki/Silent_Hill",
    "locale": "el-GR",
    "tags": ["silent-hill", "team-silent", "konami", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_017",
    "text": "Ποια αμερικανική εταιρεία ανάπτυξης (θυγατρική της Sony) δημιούργησε τις σειρές Crash Bandicoot, Jak and Daxter, Uncharted και The Last of Us;",
    "answers": ["Insomniac Games", "Sucker Punch", "Naughty Dog", "Guerrilla Games"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Naughty Dog ιδρύθηκε το 1984 από τους Andy Gavin και Jason Rubin (αρχικά ως JAM Software) και εξελίχθηκε σε κορυφαίο στούντιο του PlayStation.",
    "funFacts": [
      "Το αρχικό λογότυπο της εταιρείας απεικόνιζε ένα σκυλάκι με γυαλιά ηλίου που φορούσε κόκκινο καπέλο.",
      "Η Naughty Dog ανέπτυξε τη δική της γλώσσα προγραμματισμού, την GOAL (Game Oriented Assembly Lisp), για τα παιχνίδια Jak and Daxter στο PS2."
    ],
    "source": "https://el.wikipedia.org/wiki/Naughty_Dog",
    "locale": "el-GR",
    "tags": ["naughty-dog", "playstation", "sony", "studios"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_018",
    "text": "Ποιος θρυλικός πρώην SOLDIER με το μακρύ σπαθί Masamune και τα ασημένια μαλλιά είναι ο κεντρικός αντίπαλος στο «Final Fantasy VII»;",
    "answers": ["Kefka Palazzo", "Genesis Rhapsodos", "Seymour Guado", "Σέφιροθ (Sephiroth)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Sephiroth ανακαλύπτει ότι δημιουργήθηκε από κύτταρα της εξωγήινης οντότητας Jenova και αποφασίζει να καταστρέψει τον πλανήτη καλώντας έναν τεράστιο μετεωρίτη (Meteor).",
    "funFacts": [
      "Η επική συμφωνική μουσική μάχης του, το 'One-Winged Angel', περιέχει στίχους στα λατινικά βασισμένους στη μεσαιωνική συλλογή Carmina Burana.",
      "Το σπαθί του Masamune έχει μήκος πάνω από 2 μέτρα, ξεπερνώντας κατά πολύ το ίδιο το ύψος του χαρακτήρα."
    ],
    "source": "https://en.wikipedia.org/wiki/Sephiroth_(Final_Fantasy)",
    "locale": "el-GR",
    "tags": ["final-fantasy", "sephiroth", "square-enix", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_019",
    "text": "Ποια εταιρεία ανάπτυξης δημιούργησε και εξελίσσει τη διάσημη μηχανή γραφικών Unreal Engine, η οποία χρησιμοποιείται ευρύτατα και στον κινηματογράφο;",
    "answers": ["Epic Games", "Crytek", "Unity Technologies", "id Software"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Epic Games, υπό την καθοδήγηση του Tim Sweeney, κυκλοφόρησε την πρώτη Unreal Engine το 1998 μαζί με το ομώνυμο FPS 'Unreal'.",
    "funFacts": [
      "Η τεχνολογία Unreal Engine χρησιμοποιήθηκε για την παραγωγή οπτικών εφέ σε πραγματικό χρόνο στην τηλεοπτική σειρά 'The Mandalorian' της Disney.",
      "Η έκδοση Unreal Engine 5 εισήγαγε τις τεχνολογίες Nanite (μικροπολυγωνική γεωμετρία) και Lumen (δυναμικός παγκόσμιος φωτισμός)."
    ],
    "source": "https://el.wikipedia.org/wiki/Unreal_Engine",
    "locale": "el-GR",
    "tags": ["unreal-engine", "epic-games", "technology", "game-engines"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_020",
    "text": "Σε ποια σκοτεινή γοτθική και βικτοριανή πόλη εμπνευσμένη από τον κοσμικό τρόμο του Lovecraft διαδραματίζεται το «Bloodborne»;",
    "answers": ["Boletaria", "Yharnam (Γιάρναμ)", "Lothric", "Drangleic"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Yharnam είναι γνωστή για τη θαυματουργή θεραπεία αίματος της Healing Church, η οποία όμως προκάλεσε μια τερατώδη επιδημία μεταμόρφωσης των κατοίκων σε θηρία.",
    "funFacts": [
      "Το Bloodborne αντικατέστησε τα βαριά αμυντικά μπλοκαρίσματα με ασπίδα με ένα επιθετικό σύστημα ανάκτησης υγείας (Rally system) αμέσως μετά τα χτυπήματα.",
      "Η αρχιτεκτονική της πόλης άντλησε άμεση έμπνευση από ιστορικά κτίρια της Πράγας και της Ρουμανίας."
    ],
    "source": "https://el.wikipedia.org/wiki/Bloodborne",
    "locale": "el-GR",
    "tags": ["bloodborne", "yharnam", "fromsoftware", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_021",
    "text": "Από ποιον τεχνολογικό κολοσσό αποχώρησαν οι Gabe Newell και Mike Harrington το 1996 για να ιδρύσουν τη Valve Corporation;",
    "answers": ["Apple", "IBM", "Microsoft", "Electronic Arts"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Gabe Newell εργάστηκε για 13 χρόνια στη Microsoft συμβάλλοντας στις πρώτες εκδόσεις των Windows, προτού χρηματοδοτήσει τη δημιουργία της Valve.",
    "funFacts": [
      "Ο Newell αυτοχαρακτηρίστηκε 'παραγωγός των τριών πρώτων εκδόσεων των Windows' πριν αποφασίσει να ασχοληθεί με τα παιχνίδια επηρεασμένος από το Doom.",
      "Η Valve χρηματοδοτήθηκε αρχικά εξ ολοκλήρου από τα προσωπικά κεφάλαια που κέρδισαν οι δύο ιδρυτές από τα stock options της Microsoft."
    ],
    "source": "https://el.wikipedia.org/wiki/Valve_Corporation",
    "locale": "el-GR",
    "tags": ["valve", "gabe-newell", "microsoft", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_022",
    "text": "Ποιος μυστηριώδης μασκοφόρος χαρακτήρας με το μοβ παλτό υποδέχεται τον Leon στο «Resident Evil 4» με την ατάκα «What're ya buyin'?»;",
    "answers": ["The Duke", "Leon", "Luis Sera", "Ο Έμπορος (The Merchant)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Merchant περιμένει σε φωτισμένα με μπλε πυρσούς σημεία, πουλώντας όπλα, αναβαθμίσεις και αγοράζοντας πολύτιμους θησαυρούς.",
    "funFacts": [
      "Παρόλο που τα μάτια του φωσφορίζουν δείχνοντας ότι έχει μολυνθεί από το παράσιτο Las Plagas, παραμένει εντελώς φιλικός και νηφάλιος απέναντι στον Leon.",
      "Η βαριά φωνή και οι φράσεις του ('What're ya buyin'?', 'Heh heh heh, thank you!') έγιναν από τα πιο δημοφιλή ηχητικά αποσπάσματα στο gaming."
    ],
    "source": "https://en.wikipedia.org/wiki/Resident_Evil_4",
    "locale": "el-GR",
    "tags": ["resident-evil-4", "the-merchant", "capcom", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_023",
    "text": "Ποια ιαπωνική εταιρεία ανάπτυξης και έκδοσης υπογράφει τις εξαιρετικά επιτυχημένες σειρές JRPG «Persona» και «Shin Megami Tensei»;",
    "answers": ["Atlus", "Square Enix", "Bandai Namco", "Nippon Ichi"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Atlus (θυγατρική της Sega) δημιούργησε το σύμπαν του Shin Megami Tensei και το spin-off franchise Persona, συνδυάζοντας μαθητική ζωή και μάχες με δαίμονες.",
    "funFacts": [
      "Το Persona 5 (2016) σημείωσε παγκόσμια επιτυχία με πάνω από 7 εκατομμύρια πωλήσεις, διακρινόμενο για το έντονο κόκκινο στιλιζαρισμένο acid jazz UI του.",
      "Η επίσημη μασκότ της Atlus είναι ο χιονάνθρωπος-δαίμονας Jack Frost, ο οποίος τελειώνει τις φράσεις του με το επιφώνημα 'Hee-Ho!'."
    ],
    "source": "https://el.wikipedia.org/wiki/Atlus",
    "locale": "el-GR",
    "tags": ["atlus", "persona", "shin-megami-tensei", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_024",
    "text": "Τι σημαίνουν τα αρχικά του ονόματος της μοχθηρής τεχνητής νοημοσύνης GLaDOS στη σειρά παιχνιδιών «Portal»;",
    "answers": ["General Laser and Defense Operating System", "Genetic Lifeform and Disk Operating System", "Global Logic and Digital Orbital System", "Geographic Land and Domain Operation Server"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το GLaDOS σημαίνει 'Genetic Lifeform and Disk Operating System', αντανακλώντας το γεγονός ότι ενσωματώνει την ανθρώπινη συνείδηση της Caroline.",
    "funFacts": [
      "Η GLaDOS σχεδιάστηκε οπτικά ως μια ρομποτική φιγούρα που κρέμεται ανάποδα από την οροφή, θυμίζοντας μια δεμένη γυναίκα.",
      "Στο Portal 2, η GLaDOS μετατρέπεται προσωρινά σε μπαταρία πατάτας ('PotatOS') από τον ανίκανο Wheatley."
    ],
    "source": "https://en.wikipedia.org/wiki/GLaDOS",
    "locale": "el-GR",
    "tags": ["portal", "glados", "valve", "acronyms"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_025",
    "text": "Πόσοι γιγάντιοι κολοσσοί (Colossi) πρέπει να εντοπιστούν και να εξοντωθούν από τον Wander στο αριστούργημα «Shadow of the Colossus» (2005);",
    "answers": ["Οκτώ (8)", "Δώδεκα (12)", "Δεκαέξι (16)", "Είκοσι (20)"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Wander πρέπει να εξοντώσει και τους 16 κολοσσούς στην Απαγορευμένη Χώρα για να επαναφέρει στη ζωή τη νεκρή αγαπημένη του Mono.",
    "funFacts": [
      "Κάθε κολοσσός λειτουργεί ουσιαστικά ως ένα αυτόνομο περιβαλλοντικό παζλ πλατφόρμας, όπου ο παίκτης πρέπει να σκαρφαλώσει στο τρίχωμά του για να βρει τα αδύναμα σημεία.",
      "Το παιχνίδι σχεδιάστηκε από τον Fumito Ueda και την Team Ico, αποτελώντας ορόσημο για την αναγνώριση των βιντεοπαιχνιδιών ως μορφή υψηλής τέχνης."
    ],
    "source": "https://el.wikipedia.org/wiki/Shadow_of_the_Colossus",
    "locale": "el-GR",
    "tags": ["shadow-of-the-colossus", "team-ico", "playstation", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_026",
    "text": "Σε ποια φουτουριστική μητρόπολη ξεκινά η πρώτη αποστολή του ιστορικού cyberpunk RPG «Deus Ex» (2000) στο κατεστραμμένο Άγαλμα της Ελευθερίας;",
    "answers": ["Σικάγο", "Σιάτλ", "Λονδίνο", "Νέα Υόρκη"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο πράκτορας JC Denton ξεκινά την έρευνά του στο Liberty Island της Νέας Υόρκης για την ανάκτηση κλεμμένων εμβολίων κατά του θανατηφόρου ιού Gray Death.",
    "funFacts": [
      "Λόγω περιορισμών μνήμης, οι σχεδιαστές δεν συμπεριέλαβαν τους Δίδυμους Πύργους στον ορίζοντα της Νέας Υόρκης, δικαιολογώντας το στο σενάριο ως αποτέλεσμα τρομοκρατικής επίθεσης — ένα χρόνο πριν τα πραγματικά γεγονότα της 11ης Σεπτεμβρίου 2001.",
      "Το παιχνίδι έδινε απόλυτη ελευθερία στον παίκτη να ολοκληρώσει τις αποστολές με μάχη, stealth, χακάρισμα υπολογιστών ή κοινωνική διπλωματία."
    ],
    "source": "https://en.wikipedia.org/wiki/Deus_Ex_(video_game)",
    "locale": "el-GR",
    "tags": ["deus-ex", "cyberpunk", "ion-storm", "pc-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_027",
    "text": "Ποια φιλο-ανθρώπινη μυστική οργάνωση διευθύνει ο αινιγματικός Illusive Man στην τριλογία επιστημονικής φαντασίας «Mass Effect»;",
    "answers": ["Cerberus (Κέρβερος)", "Spectre", "Alliance", "Shadow Broker"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Cerberus είναι μια παραστρατιωτική οργάνωση που θεωρείται τρομοκρατική από την Ακρόπολη, η οποία ξοδεύει δισεκατομμύρια για να αναστήσει τον Shepard στο 'Lazarus Project'.",
    "funFacts": [
      "Τη φωνή του Illusive Man χάρισε ο διάσημος ηθοποιός Martin Sheen (πρωταγωνιστής του 'Apocalypse Now' και του 'The West Wing').",
      "Το σύμβολο της Cerberus είναι ένα κεφάλι τρικέφαλου σκύλου σχηματισμένο από γεωμετρικές γραμμές."
    ],
    "source": "https://el.wikipedia.org/wiki/Mass_Effect_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["mass-effect", "cerberus", "bioware", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_028",
    "text": "Ποιος σκοτεινός πολεμιστής που κατέχεται από το Satsui no Hado έκανε το ντεμπούτο του ως μυστικό κρυφό αφεντικό στο «Super Street Fighter II Turbo»;",
    "answers": ["M. Bison", "Akuma (Gouki)", "Sagat", "Vega"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Akuma εμφανίζεται ξαφνικά εξουδετερώνοντας τον M. Bison με την κίνηση 'Raging Demon' (Shun Goku Satsu) αν ο παίκτης φτάσει στον τελικό χωρίς να χάσει γύρο.",
    "funFacts": [
      "Στην Ιαπωνία είναι γνωστός με το όνομα 'Gouki', που σημαίνει 'Μεγάλος Δαίμονας'.",
      "Στην πλάτη της στολής του λάμπει το ιαπωνικό ιδεόγραμμα 'Ten' (天), που συμβολίζει τον ουρανό ή την υπεράνθρωπη δύναμη."
    ],
    "source": "https://en.wikipedia.org/wiki/Akuma_(Street_Fighter)",
    "locale": "el-GR",
    "tags": ["street-fighter", "akuma", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_029",
    "text": "Σε ποιο τεράστιο ηφαιστειογενές νησί της επαρχίας Morrowind διαδραματίζεται το κλασικό RPG «The Elder Scrolls III» (2002);",
    "answers": ["Cyrodiil", "High Rock", "Vvardenfell", "Hammerfell"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το νησί Vvardenfell κυριαρχείται στο κέντρο του από το γιγάντιο ηφαίστειο Red Mountain και αποτελεί την πατρίδα των Σκοτεινών Ξωτικών (Dunmer).",
    "funFacts": [
      "Το Morrowind ήταν ο τίτλος που έσωσε οικονομικά την Bethesda Game Studios από τη χρεοκοπία, σημειώνοντας τεράστια επιτυχία σε PC και στο αρχικό Xbox.",
      "Σε αντίθεση με τα νεότερα παιχνίδια της σειράς, το Morrowind δεν είχε αυτόματη πυξίδα με δείκτες αποστολών αλλά απαιτούσε διάβασμα οδηγιών στο ημερολόγιο."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Elder_Scrolls_III:_Morrowind",
    "locale": "el-GR",
    "tags": ["morrowind", "elder-scrolls", "bethesda", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_030",
    "text": "Ποιο ιστορικό FPS της Rare για το Nintendo 64 (1997) απέδειξε για πρώτη φορά ότι τα shooters πρώτου προσώπου μπορούν να διαπρέψουν σε κονσόλες;",
    "answers": ["Perfect Dark", "Turok: Dinosaur Hunter", "Quake II", "GoldenEye 007"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το GoldenEye 007 καθιέρωσε το split-screen multiplayer τεσσάρων παικτών και εισήγαγε αποστολές με στόχους κατασκοπείας αντί για απλή εξόντωση εχθρών.",
    "funFacts": [
      "Το διάσημο multiplayer mode του παιχνιδιού προστέθηκε από έναν μόνο προγραμματιστή τον τελευταίο μήνα της ανάπτυξης χωρίς επίσημη έγκριση.",
      "Η επιλογή του χαρακτήρα Oddjob θεωρούνταν 'παράνομη' μεταξύ των φίλων, επειδή το χαμηλό του ανάστημα τον έκανε εξαιρετικά δύσκολο στόχο."
    ],
    "source": "https://el.wikipedia.org/wiki/GoldenEye_007_(%CE%B2%CE%B9%CE%BD%CF%84%CE%B5%CE%BF%CF%80%CE%B1%CE%B9%CF%87%CE%BD%CE%AF%CE%B4%CE%B9_1997)",
    "locale": "el-GR",
    "tags": ["goldeneye-007", "rare", "nintendo-64", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_031",
    "text": "Ποιος χαρισματικός αλλά σταδιακά παρανοϊκός αρχηγός ηγείται της συμμορίας παρανόμων στο «Red Dead Redemption 2»;",
    "answers": ["Dutch van der Linde", "Micah Bell", "Hosea Matthews", "Bill Williamson"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Dutch van der Linde υπόσχεται διαρκώς στη συμμορία 'ένα τελευταίο μεγάλο κόλπο' πριν αποσυρθούν στην Ταϊτή, αλλά η φιλοσοφία του καταρρέει.",
    "funFacts": [
      "Η φράση του 'I have a plan!' ('Έχω ένα σχέδιο!') έγινε ένα από τα πιο διάσημα memes στην ιστορία της Rockstar Games.",
      "Τη φωνή και την ερμηνεία motion capture του Dutch χάρισε ο ηθοποιός Benjamin Byron Davis."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "dutch", "rockstar-games", "western"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_032",
    "text": "Πώς ονομάζεται το γιγάντιο διαστημόπλοιο εξόρυξης πλανητών (Planet Cracker) όπου διαδραματίζεται ο εφιάλτης του αρχικού «Dead Space» (2008);",
    "answers": ["SSV Normandy", "USG Ishimura", "UNSC Pillar of Autumn", "Sovereign"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο μηχανικός Isaac Clarke αποστέλλεται στο USG Ishimura για επισκευές, ανακαλύπτοντας ότι όλο το πλήρωμα σφαγιάστηκε και μεταλλάχθηκε σε Necromorphs.",
    "funFacts": [
      "Το όνομα Ishimura δόθηκε προς τιμήν του διάσημου Ιάπωνα συγγραφέα επιστημονικής φαντασίας Shinichi Hoshi (και του ηθοποιού Ken Ishimura).",
      "Το Dead Space κατάργησε το παραδοσιακό HUD οθόνης: η υγεία του παίκτη φαίνεται στη ραχοκοκαλιά της στολής του και τα πυρομαχικά ως ολόγραμμα πάνω στο όπλο."
    ],
    "source": "https://el.wikipedia.org/wiki/Dead_Space_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["dead-space", "ishimura", "visceral-games", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_033",
    "text": "Ποιο ανεξάρτητο στούντιο με έδρα το Σαν Φρανσίσκο δημιούργησε τα αναγνωρισμένα παιχνίδια «Bastion», «Transistor», «Pyre» και «Hades»;",
    "answers": ["Housemarque", "Team Cherry", "Supergiant Games", "Motion Twin"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Supergiant Games ιδρύθηκε το 2009 από τους Amir Rao και Gavin Simon και διακρίνεται για τις αφηγήσεις του Logan Cunningham και τη μουσική του Darren Korb.",
    "funFacts": [
      "Ο ηθοποιός Logan Cunningham έχει δανείσει τη φωνή του σε χαρακτήρες σε κάθε ανεξαιρέτως παιχνίδι του στούντιο (όπως ο Αφηγητής στο Bastion και ο Άδης στο Hades).",
      "Ο συνθέτης Darren Korb και η τραγουδίστρια Ashley Barrett ηχογραφούν όλα τα τραγούδια των παιχνιδιών στο ίδιο προσωπικό οικιακό στούντιο από το 2011."
    ],
    "source": "https://en.wikipedia.org/wiki/Supergiant_Games",
    "locale": "el-GR",
    "tags": ["supergiant-games", "hades", "bastion", "indie"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_034",
    "text": "Ποιο κορυφαίο στούντιο ανάπτυξης RPG δημιούργησε το αριστουργηματικό «Star Wars: Knights of the Old Republic» (KOTOR) το 2003;",
    "answers": ["Obsidian Entertainment", "Bethesda Game Studios", "Black Isle Studios", "BioWare"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η καναδική BioWare τοποθέτησε το KOTOR 4.000 χρόνια πριν από τη Γαλαξιακή Αυτοκρατορία, παρουσιάζοντας μια από τις σπουδαιότερες σεναριακές ανατροπές στην ιστορία.",
    "funFacts": [
      "Η αποκάλυψη ότι ο παίκτης είναι στην πραγματικότητα ο ίδιος ο αμνησιακός Sith Lord Revan θεωρείται κορυφαία ανατροπή στην ιστορία των παιχνιδιών.",
      "Το παιχνίδι εισήγαγε τον σαδιστή αλλά εξαιρετικά αστείο δολοφόνο ανδροειδές HK-47, ο οποίος αποκαλεί υποτιμητικά όλους τους ανθρώπους 'meatbags'."
    ],
    "source": "https://el.wikipedia.org/wiki/Star_Wars:_Knights_of_the_Old_Republic",
    "locale": "el-GR",
    "tags": ["star-wars", "kotor", "bioware", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_035",
    "text": "Ποιος επίδοξος πειρατής είναι ο αδέξιος πρωταγωνιστής της κλασικής σειράς περιπετειών «The Secret of Monkey Island» του Ron Gilbert;",
    "answers": ["Guybrush Threepwood", "Manny Calavera", "LeChuck", "Stan S. Stanman"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Guybrush Threepwood ξεκινά στο νησί Mêlée Island δηλώνοντας με σιγουριά 'My name is Guybrush Threepwood, and I want to be a pirate!'.",
    "funFacts": [
      "Οι ξιφομαχίες στο παιχνίδι δεν κερδίζονται με σπαθιά αλλά με έξυπνες προσβολές και ετοιμόλογες απαντήσεις (Insult Sword Fighting).",
      "Ο Guybrush μπορεί να κρατήσει την αναπνοή του κάτω από το νερό για ακριβώς δέκα ολόκληρα λεπτά."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Secret_of_Monkey_Island",
    "locale": "el-GR",
    "tags": ["monkey-island", "lucasarts", "adventure", "retro-gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_036",
    "text": "Πώς ονομάζεται το πιο καταστροφικό ενεργειακό υπερόπλο του Doom που εξαϋλώνει ολόκληρες οθόνες δαιμόνων με μία τεράστια πράσινη βολή πλάσματος;",
    "answers": ["Unmaker", "BFG 9000", "Super Shotgun", "Plasma Gun"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το BFG 9000 (Big Fucking Gun) πρωτοεμφανίστηκε στο αρχικό Doom (1993) και αποτελεί το απόλυτο όπλο μαζικής καταστροφής της id Software.",
    "funFacts": [
      "Στην κινηματογραφική ταινία Doom (2005) με τον Dwayne 'The Rock' Johnson, το όνομα του όπλου λογοκρίθηκε χιουμοριστικά ως 'Bio Force Gun'.",
      "Η τεχνική λειτουργία του αρχικού BFG στον κώδικα του παιχνιδιού υπολόγιζε ζημιά σε όλους τους εχθρούς που βρίσκονταν στο οπτικό πεδίο του παίκτη κατά την πρόσκρουση της σφαίρας."
    ],
    "source": "https://en.wikipedia.org/wiki/BFG_(weapon)",
    "locale": "el-GR",
    "tags": ["doom", "bfg-9000", "id-software", "weapons"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_037",
    "text": "Ποιο είναι το όνομα του αρχαίου βασιλείου των θεών όπου διαδραματίζονται τα γεγονότα του πρώτου «Dark Souls»;",
    "answers": ["Drangleic", "Lothric", "Lordran", "The Lands Between"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Lordran είναι η γη των αρχαίων Αρχόντων (Lords), όπου ο παίκτης ως 'Chosen Undead' ταξιδεύει για να ανανεώσει την Πρώτη Φλόγα (First Flame).",
    "funFacts": [
      "Ο σχεδιασμός του κόσμου του Lordran είναι διάσημος για την κατακόρυφη συνδεσιμότητά του (interconnectivity), με συντομεύσεις που ενώνουν φαινομενικά άσχετες περιοχές.",
      "Η λαμπερή μητρόπολη των θεών στο Lordran ονομάζεται Anor Londo και φυλάσσεται από το διαβόητο δίδυμο Ornstein και Smough."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "lordran", "fromsoftware", "soulslike"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_038",
    "text": "Με ποιον ευρηματικό τρόπο μπορούσε ο παίκτης να εξουδετερώσει την τηλεπαθητική ανάγνωση κινήσεων του Psycho Mantis στο αρχικό «Metal Gear Solid»;",
    "answers": ["Κάνοντας παύση στο μενού", "Πυροβολώντας τα αγάλματα", "Χρησιμοποιώντας χειροβομβίδα κρότου", "Συνδέοντας το χειριστήριο στη δεύτερη θύρα (Port 2)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Συνδέοντας το χειριστήριο στη θύρα Controller 2 του PlayStation, ο Psycho Mantis δεν μπορούσε πλέον να 'διαβάσει το μυαλό' του Snake και να αποφύγει τις επιθέσεις.",
    "funFacts": [
      "Πριν από τη μάχη, ο Psycho Mantis σχολίαζε άλλα παιχνίδια της Konami (όπως το Castlevania) διαβάζοντας τα αρχεία της Memory Card του παίκτη.",
      "Ζητούσε επίσης από τον παίκτη να αφήσει το χειριστήριο στο πάτωμα για να το κινήσει με 'τηλεπάθεια' ενεργοποιώντας τη δόνηση DualShock."
    ],
    "source": "https://el.wikipedia.org/wiki/Metal_Gear_Solid",
    "locale": "el-GR",
    "tags": ["metal-gear", "psycho-mantis", "kojima", "ps1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_039",
    "text": "Ποιος θρυλικός σχεδιαστής έδωσε το όνομά του στη διάσημη σειρά παιχνιδιών στρατηγικής turn-based «Civilization»;",
    "answers": ["Sid Meier", "Peter Molyneux", "Chris Sawyer", "Will Wright"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Sid Meier συνίδρυσε τη MicroProse και την Firaxis Games, δημιουργώντας το Sid Meier's Civilization το 1991.",
    "funFacts": [
      "Το παιχνίδι καθιέρωσε το παγκόσμιο σύνδρομο 'One more turn' ('Ακόμα έναν γύρο'), κρατώντας τους παίκτες ξάγρυπνους μέχρι το πρωί.",
      "Στο αρχικό παιχνίδι, ένα bug υπερχείλισης ακεραίου (integer overflow) έκανε τον Μαχάτμα Γκάντι απρόσμενα τον πιο επιθετικό ηγέτη με εμμονή στα πυρηνικά όπλα."
    ],
    "source": "https://el.wikipedia.org/wiki/Civilization",
    "locale": "el-GR",
    "tags": ["civilization", "sid-meier", "strategy", "4x"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_040",
    "text": "Ποια δύο αδέλφια νάνοι σιδηρουργοί κατασκεύασαν το τσεκούρι Leviathan και το σφυρί Mjölnir στη σκανδιναβική εποχή του «God of War»;",
    "answers": ["Magni & Modi", "Brok και Sindri", "Baldur & Heimdall", "Freyr & Freya"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Brok (με το μπλε δέρμα) και ο Sindri (που έχει μικροβιοφοβία) είναι οι διάσημοι σιδηρουργοί Χουλντρα που αναβαθμίζουν τα όπλα του Κράτου και του Ατρέα.",
    "funFacts": [
      "Το μπλε χρώμα του Brok οφείλεται σε δηλητηρίαση από επαφή με ασήμι, καθώς δούλευε χωρίς προστατευτικά γάντια.",
      "Η συναισθηματική κατάληξη της ιστορίας των δύο αδελφών αποτελεί κεντρικό πυρήνα της πλοκής στο God of War Ragnarök."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "brok", "sindri", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_041",
    "text": "Σε ποια παραδοσιακή μεξικανική γιορτή και μυθολογία βασίζεται το καλλιτεχνικό σύμπαν του graphic adventure «Grim Fandango» (1998);",
    "answers": ["Καρναβάλι της Βενετίας", "Mardi Gras", "Ημέρα των Νεκρών (Día de los Muertos)", "Halloween"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το αριστούργημα του Tim Schafer για τη LucasArts συνδυάζει τη μεξικανική λαογραφία των calaca σκελετών με κλασικό κινηματογραφικό φιλμ νουάρ.",
    "funFacts": [
      "Ο πρωταγωνιστής Manny Calavera εργάζεται ως ταξιδιωτικός πράκτορας ψυχών στο Υπουργείο Θανάτου (Department of Death).",
      "Ήταν το πρώτο παιχνίδι περιπέτειας της LucasArts που χρησιμοποίησε τρισδιάστατα γραφικά χαρακτήρων αντί για δισδιάστατα sprites."
    ],
    "source": "https://el.wikipedia.org/wiki/Grim_Fandango",
    "locale": "el-GR",
    "tags": ["grim-fandango", "tim-schafer", "lucasarts", "adventure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_042",
    "text": "Πώς ονομάζεται η συσκευή εικονικής πραγματικότητας που επιτρέπει την αναβίωση των γενετικών αναμνήσεων των προγόνων στο «Assassin's Creed»;",
    "answers": ["Helix", "Chronos", "Eden Device", "Animus"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Animus αναπτύχθηκε από την εταιρεία Abstergo Industries (τη σύγχρονη βιτρίνα των Ναϊτών) για να εντοπίσει τα πανίσχυρα Μήλα της Εδέμ.",
    "funFacts": [
      "Ο Desmond Miles χρησιμοποιεί το Animus για να ζήσει τις ζωές των προγόνων του Altaïr, Ezio και Connor.",
      "Η παρατεταμένη χρήση του Animus προκαλεί το 'Bleeding Effect', όπου οι ικανότητες και οι παραισθήσεις του προγόνου περνούν στη σύγχρονη συνείδηση του υποκειμένου."
    ],
    "source": "https://el.wikipedia.org/wiki/Assassin%27s_Creed",
    "locale": "el-GR",
    "tags": ["assassins-creed", "animus", "ubisoft", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_043",
    "text": "Ποιοι είναι οι δύο επιστήθιοι παιδικοί φίλοι του Sora από τα Destiny Islands που αναζητά σε όλη τη σειρά «Kingdom Hearts»;",
    "answers": ["Riku και Kairi", "Roxas και Axel", "Terra και Aqua", "Hayner και Olette"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Riku (που πέφτει προσωρινά στο σκοτάδι) και η Kairi (μια από τις επτά Πριγκίπισσες της Καρδιάς) αποτελούν το βασικό κίνητρο του Sora στο ταξίδι του.",
    "funFacts": [
      "Τα ονόματα των τριών παιδιών στα ιαπωνικά συμβολίζουν τα στοιχεία της φύσης: Sora σημαίνει Ουρανός, Riku σημαίνει Γη και Kairi σημαίνει Θάλασσα.",
      "Ο Riku προοριζόταν αρχικά να είναι ο αρχικός φορέας του Keyblade, πριν το όπλο επιλέξει τελικά τον Sora."
    ],
    "source": "https://en.wikipedia.org/wiki/Kingdom_Hearts",
    "locale": "el-GR",
    "tags": ["kingdom-hearts", "riku", "kairi", "square-enix"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_044",
    "text": "Ποιο στούντιο RPG (στελεχωμένο από δημιουργούς των αρχικών Fallout) ανέπτυξε το εξαιρετικά αγαπημένο «Fallout: New Vegas» (2010);",
    "answers": ["BioWare", "Obsidian Entertainment", "inXile Entertainment", "Bethesda Game Studios"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Obsidian Entertainment ανέλαβε την ανάπτυξη του New Vegas για λογαριασμό της Bethesda, επιστρέφοντας στη δυτική ακτή των ΗΠΑ και την έρημο Mojave.",
    "funFacts": [
      "Ο πρωταγωνιστής είναι ο 'Courier 6', ο οποίος πυροβολείται στο κεφάλι και θάβεται ζωντανός στην εισαγωγική σκηνή από τον Benny.",
      "Το παιχνίδι ολοκληρώθηκε σε μόλις 18 μήνες ανάπτυξης και έχασε για έναν μόλις βαθμό στο Metacritic (84 αντί για 85) το ειδικό οικονομικό μπόνους της Bethesda."
    ],
    "source": "https://el.wikipedia.org/wiki/Fallout:_New_Vegas",
    "locale": "el-GR",
    "tags": ["fallout-new-vegas", "obsidian", "rpg", "post-apocalyptic"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_045",
    "text": "Ποιος μισός-βρικόλακας γιος του Κόμη Δράκουλα ξυπνά από τον αιώνιο ύπνο του και πρωταγωνιστεί στο «Castlevania: Symphony of the Night»;",
    "answers": ["Simon Belmont", "Richter Belmont", "Alucard (Άλουκαρντ)", "Trevor Belmont"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Alucard (Adrian Fahrenheit Ţepeş) είναι καρπός του έρωτα του Δράκουλα με τη θνητή Lisa και μάχεται για να σταματήσει την καταστροφή των ανθρώπων.",
    "funFacts": [
      "Το όνομά του 'Alucard' είναι ο αναγραμματισμός του ονόματος 'Dracula' γραμμένου ανάποδα.",
      "Στο παιχνίδι, αφού ο παίκτης φτάσει στο φαινομενικό τέλος του κάστρου, ξεκλειδώνει μια ολόκληρη δεύτερη ανεστραμμένη εκδοχή του κάστρου (Inverted Castle) που κρέμεται ανάποδα στον ουρανό."
    ],
    "source": "https://el.wikipedia.org/wiki/Castlevania:_Symphony_of_the_Night",
    "locale": "el-GR",
    "tags": ["castlevania", "alucard", "konami", "metroidvania"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_046",
    "text": "Ποιος εξόριστος διοικητής των Covenant Elite ενώνει τις δυνάμεις του με τον Master Chief στα «Halo 2» και «Halo 3»;",
    "answers": ["Tartarus", "Atriox", "Ripa 'Moramee", "The Arbiter (Thel 'Vadam)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Thel 'Vadam αναλαμβάνει τον τίτλο του Arbiter μετά την καταστροφή του πρώτου Halo δακτυλίου, ανακαλύπτοντας την προδοσία των Προφητών.",
    "funFacts": [
      "Στο Halo 2, οι παίκτες ελέγχουν εναλλάξ τον Master Chief και τον Arbiter, βλέποντας τον διαγαλαξιακό πόλεμο και από τις δύο πλευρές.",
      "Τη φωνή του Arbiter χάρισε ο σπουδαίος ηθοποιός Keith David."
    ],
    "source": "https://en.wikipedia.org/wiki/Arbiter_(Halo)",
    "locale": "el-GR",
    "tags": ["halo", "arbiter", "bungie", "xbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_047",
    "text": "Ποια από τις αρχικές τέσσερις playable κλάσεις του πρώτου «Borderlands» εκπροσωπείται από τη Lilith, η οποία διαθέτει υπερφυσικές δυνάμεις Phasewalk;",
    "answers": ["Siren (Σειρήνα)", "Soldier", "Hunter", "Berserker"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Σειρήνες (Sirens) είναι μυστηριώδεις γυναίκες με εξωγήινα τατουάζ και κοσμικές δυνάμεις, με μόνο έξι από αυτές να μπορούν να υπάρχουν ταυτόχρονα στο σύμπαν.",
    "funFacts": [
      "Η ικανότητα Phasewalk της Lilith της επιτρέπει να εξαφανίζεται σε μια παράλληλη διάσταση, κινούμενη με τεράστια ταχύτητα χωρίς να δέχεται ζημιά.",
      "Στα επόμενα παιχνίδια, η Lilith γίνεται η ηγέτιδα των Crimson Raiders στον πλανήτη Pandora."
    ],
    "source": "https://en.wikipedia.org/wiki/Borderlands_(video_game)",
    "locale": "el-GR",
    "tags": ["borderlands", "lilith", "siren", "gearbox"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_048",
    "text": "Ποιος διάσημος μουσικός και επικεφαλής των Nine Inch Nails συνέθεσε το σκοτεινό βιομηχανικό soundtrack και τα εφέ του αρχικού «Quake» (1996);",
    "answers": ["Mick Gordon", "Trent Reznor", "Frank Klepacki", "Kelly Bailey"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Trent Reznor ήταν τεράστιος θαυμαστής της id Software και δέχτηκε να γράψει όλη τη μουσική και τα ηχητικά εφέ του Quake δωρεάν.",
    "funFacts": [
      "Προς τιμήν του, τα κουτιά πυρομαχικών για το πολυβόλο Nailgun στο παιχνίδι φέρουν χαραγμένο το επίσημο λογότυπο των 'NIN' (Nine Inch Nails).",
      "Ο Reznor κέρδισε αργότερα δύο βραβεία Όσκαρ για τη μουσική του σε ταινίες του Χόλιγουντ όπως το 'The Social Network' και το 'Soul'."
    ],
    "source": "https://en.wikipedia.org/wiki/Quake_(video_game)",
    "locale": "el-GR",
    "tags": ["quake", "trent-reznor", "id-software", "soundtrack"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_049",
    "text": "Ποιος Ιάπωνας δημιουργός εμπνεύστηκε τη σύλληψη των Pokémon από το παιδικό του χόμπι της συλλογής εντόμων στα δάση;",
    "answers": ["Shigeru Miyamoto", "Ken Sugimori", "Satoshi Tajiri", "Junichi Masuda"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Satoshi Tajiri ίδρυσε την Game Freak και ανέπτυξε τα Pokémon Red and Green για το Game Boy, θέλοντας να προσφέρει στα παιδιά των πόλεων τη χαρά της ανακάλυψης πλασμάτων.",
    "funFacts": [
      "Ο πρωταγωνιστής του anime, Satoshi (γνωστός στη Δύση ως Ash Ketchum), πήρε το όνομά του απευθείας από τον Tajiri.",
      "Χρειάστηκαν πάνω από έξι χρόνια σκληρής ανάπτυξης μέχρι να κυκλοφορήσει το πρώτο παιχνίδι το 1996, οδηγώντας την Game Freak σχεδόν στα όρια της χρεοκοπίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CF%84%CF%8C%CF%83%CE%B9_%CE%A4%CE%B1%CF%84%CE%B6%CE%AF%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["pokemon", "satoshi-tajiri", "game-freak", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_050",
    "text": "Ποιο είναι το όνομα του λευκού περιστεριού που έχει ως αγαπημένο κατοικίδιο ο Medic στο «Team Fortress 2»;",
    "answers": ["Aristotle", "Plato", "Socrates", "Archimedes (Αρχιμήδης)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Archimedes είναι το λευκό περιστέρι του Medic που πρωτοεμφανίστηκε στην επίσημη ταινία κινουμένων σχεδίων 'Meet the Medic', φωλιάζοντας μέσα στα ανοιχτά στήθη των ασθενών.",
    "funFacts": [
      "Υπάρχει ως επίσημο κοσμητικό αντικείμενο στο Steam, το οποίο στέκεται ματωμένο πάνω στον ώμο του Medic κατά τη διάρκεια του αγώνα.",
      "Στο παιχνίδι, όταν ένας Heavy εκραγεί από επίθεση Scout, υπάρχει μια μικρή πιθανότητα (1 στις 100) να πετάξει έξω από το πτώμα του ένα περιστέρι."
    ],
    "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "medic", "archimedes", "valve"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_051",
    "text": "Ποιο ήταν το ασυνήθιστο φυσικό χαρακτηριστικό της Lady Dimitrescu που προκάλεσε παγκόσμιο φαινόμενο στο διαδίκτυο πριν την κυκλοφορία του «Resident Evil Village»;",
    "answers": ["Περίπου 2,9 μέτρα ύψος (9 πόδια και 6 ίντσες)", "Περίπου 2,1 μέτρα ύψος", "Περίπου 3,8 μέτρα ύψος", "Περίπου 1,9 μέτρα ύψος"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο καλλιτεχνικός διευθυντής Tomonori Takano επιβεβαίωσε επίσημα ότι το ύψος της Lady Dimitrescu (μαζί με το καπέλο και τα τακούνια της) φτάνει τα 2,9 μέτρα.",
    "funFacts": [
      "Ο σχεδιασμός της βασίστηκε σε ιστορικές φιγούρες όπως η ματωμένη κόμισσα Ελισάβετ Μπάθορι και ο ιαπωνικός αστικός μύθος Hasshaku-sama.",
      "Η ηθοποιός Maggie Robertson που ενσάρκωσε τη Lady Dimitrescu κέρδισε το βραβείο Best Performance στα The Game Awards 2021."
    ],
    "source": "https://el.wikipedia.org/wiki/Resident_Evil_Village",
    "locale": "el-GR",
    "tags": ["resident-evil-village", "lady-dimitrescu", "capcom", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_052",
    "text": "Ποιος σκοτεινός ξωτικός βασιλιάς των Aen Elle ηγείται της τρομερής Άγριας Κυνηγεσίας (Wild Hunt) στο «The Witcher 3»;",
    "answers": ["Avallac'h", "Eredin Bréacc Glas", "Imlerith", "Caranthir"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Eredin Bréacc Glas καταδιώκει αμείλικτα τη Ciri μέσα στις διαστάσεις για να εκμεταλλευτεί το Αρχαίο Αίμα της και να σώσει τον λαό του από το White Frost.",
    "funFacts": [
      "Φοράει μια τρομακτική πανοπλία με μεταλλικό κρανίο που κάνει τους ανθρώπους να νομίζουν ότι η Άγρια Κυνηγεσία είναι στρατός φαντασμάτων.",
      "Στα βιβλία του Andrzej Sapkowski, ο Eredin δηλητηριάζει τον προηγούμενο βασιλιά των Aen Elle για να καταλάβει τον θρόνο."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
    "locale": "el-GR",
    "tags": ["witcher", "eredin", "wild-hunt", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_053",
    "text": "Σε ποια πραγματική απαγορευμένη περιοχή πυρηνικής καταστροφής διαδραματίζεται η ουκρανική σειρά επιβίωσης «S.T.A.L.K.E.R.»;",
    "answers": ["Στο κοσμοδρόμιο του Μπαϊκονούρ", "Στα ορυχεία των Ουραλίων", "Στη Ζώνη Αποκλεισμού του Τσερνόμπιλ", "Στη χερσόνησο Καμτσάτκα"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το S.T.A.L.K.E.R. της GSC Game World διαδραματίζεται στη 'Ζώνη' (The Zone) γύρω από τον πυρηνικό σταθμό του Τσερνόμπιλ, γεμάτη ραδιενέργεια, μεταλλάξεις και ανωμαλίες.",
    "funFacts": [
      "Η ομάδα ανάπτυξης ταξίδεψε προσωπικά πολλές φορές στην πραγματική εγκαταλελειμμένη πόλη του Πρίπιατ για να αποτυπώσει πιστά τα κτίρια και την ατμόσφαιρα.",
      "Άντλησε έμπνευση από το φιλοσοφικό βιβλίο επιστημονικής φαντασίας 'Πικνίκ δίπλα στον δρόμο' των αδελφών Στρουγκάτσκι και την ταινία 'Stalker' του Αντρέι Ταρκόφσκι."
    ],
    "source": "https://en.wikipedia.org/wiki/S.T.A.L.K.E.R.",
    "locale": "el-GR",
    "tags": ["stalker", "chernobyl", "gsc-game-world", "survival-fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_054",
    "text": "Ποιο είναι το πιο ογκώδες και ανθεκτικό Special Infected που εκσφενδονίζει τσιμεντένιους βράχους και αυτοκίνητα στους επιζώντες στο «Left 4 Dead»;",
    "answers": ["Charger", "Jockey", "Spitter", "Tank"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Tank είναι ένα γιγάντιο μυώδες τέρας με τεράστια ποσότητα υγείας, η εμφάνιση του οποίου συνοδεύεται πάντα από ειδικό καταιγιστικό μουσικό θέμα.",
    "funFacts": [
      "Η καλύτερη ομαδική στρατηγική εναντίον του Tank είναι να πυρποληθεί με βόμβα μολότοφ, καθώς η φωτιά του προκαλεί συνεχή ζημιά μέχρι να πέσει.",
      "Στο ανταγωνιστικό Versus mode, ο έλεγχος του Tank ανατίθεται τυχαία σε έναν παίκτη της ομάδας των μολυσμένων με ειδικό μετρητή απογοήτευσης (frustration meter)."
    ],
    "source": "https://el.wikipedia.org/wiki/Left_4_Dead",
    "locale": "el-GR",
    "tags": ["left-4-dead", "tank", "valve", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_055",
    "text": "Ποιο ανεξάρτητο καλλιτεχνικό στούντιο με έδρα την Εσθονία δημιούργησε το αριστουργηματικό και πολυβραβευμένο RPG «Disco Elysium» (2019);",
    "answers": ["ZA/UM", "Larian Studios", "Spiders", "InXile"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η κολεκτίβα καλλιτεχνών και συγγραφέων ZA/UM, υπό τον μυθιστοριογράφο Robert Kurvitz, δημιούργησε τον ντετέκτιβ Harry Du Bois και την παρακμάζουσα πόλη Revachol.",
    "funFacts": [
      "Το Disco Elysium δεν περιέχει καθόλου παραδοσιακό σύστημα μάχης: όλες οι αναμετρήσεις και οι πράξεις επιλύονται μέσω διαλόγων και ρίψεων ζαριών βασισμένων σε 24 δεξιότητες.",
      "Στην ομιλία αποδοχής του βραβείου στα The Game Awards 2019, οι δημιουργοί ευχαρίστησαν δημόσια τους Karl Marx και Friedrich Engels για τις πολιτικές τους ιδέες."
    ],
    "source": "https://en.wikipedia.org/wiki/Disco_Elysium",
    "locale": "el-GR",
    "tags": ["disco-elysium", "zaum", "indie", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_056",
    "text": "Πώς ονομάζεται το καταραμένο ρουνοσπάθι που κατέκλεψε την ψυχή του πρίγκιπα Arthas Menethil, μετατρέποντάς τον στον Lich King στο «Warcraft»;",
    "answers": ["Shadowmourne", "Frostmourne (Παγερή Θλίψη)", "Ashbringer", "Gorehowl"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Frostmourne σφυρηλατήθηκε από τη Burning Legion και παγίδευε τις ψυχές όσων σκότωνε, καθιστώντας τον κάτοχό του πιόνι του Lich King.",
    "funFacts": [
      "Στο τέλος του expansion 'Wrath of the Lich King', ο Highlord Tirion Fordring σπάει το Frostmourne στα δύο με το ιερό σπαθί Ashbringer, απελευθερώνοντας χιλιάδες βασανισμένες ψυχές.",
      "Η επιγραφή στο βάθρο του σπαθιού προειδοποιούσε: 'Όποιος πάρει αυτή τη λεπίδα θα ασκήσει δύναμη αιώνια. Όπως η λεπίδα σχίζει τη σάρκα, έτσι και η δύναμη σημαδεύει το πνεύμα'."
    ],
    "source": "https://el.wikipedia.org/wiki/World_of_Warcraft:_Wrath_of_the_Lich_King",
    "locale": "el-GR",
    "tags": ["warcraft", "frostmourne", "arthas", "blizzard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_057",
    "text": "Ποιος επικεφαλής προγραμματιστής της Sonic Team δημιούργησε τον πρωτοποριακό αλγόριθμο κύλισης καμπύλων επιφανειών για το «Sonic the Hedgehog» (1991);",
    "answers": ["Naoto Ohshima", "Hirokazu Yasuhara", "Yuji Naka", "Tom Kalinske"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Yuji Naka κατάφερε να εκμεταλλευτεί στο έπακρο τον επεξεργαστή του Mega Drive, επιτρέποντας στον Sonic να διασχίζει περιστροφές 360 μοιρών (loops) με ιλιγγιώδη ταχύτητα.",
    "funFacts": [
      "Πριν από το Sonic, ο Naka είχε προγραμματίσει το ιστορικό Phantasy Star για το Master System.",
      "Η ομάδα της Nintendo πίστευε αρχικά ότι μια τόσο γρήγορη κίνηση ήταν αδύνατη σε 16-bit επεξεργαστή χωρίς ειδικό τσιπ επιτάχυνσης."
    ],
    "source": "https://en.wikipedia.org/wiki/Yuji_Naka",
    "locale": "el-GR",
    "tags": ["sonic", "yuji-naka", "sega", "developers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_058",
    "text": "Ποια δυστοπική ανατολικοευρωπαϊκή μητρόπολη αποτελεί το κεντρικό σκηνικό της κυριαρχίας των Combine στο «Half-Life 2»;",
    "answers": ["Rapture", "Dunwall", "Columbia", "City 17"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η City 17 κυριαρχείται στο κέντρο της από την πανύψηλη Ακρόπολη (Citadel), ένα γιγάντιο μεταλλικό φρούριο των εξωγήινων Combine.",
    "funFacts": [
      "Ο καλλιτεχνικός διευθυντής Viktor Antonov σχεδίασε την City 17 βασισμένος στην πατρίδα του τη Σόφια της Βουλγαρίας, συνδυάζοντας κλασική ευρωπαϊκή αρχιτεκτονική με σοβιετικό μπρουταλισμό.",
      "Η διάσημη εισαγωγή του παιχνιδιού ξεκινά στον σιδηροδρομικό σταθμό της City 17, με τον Dr. Breen να απευθύνει προπαγανδιστικά μηνύματα από γιγαντοοθόνες."
    ],
    "source": "https://el.wikipedia.org/wiki/Half-Life_2",
    "locale": "el-GR",
    "tags": ["half-life", "city-17", "valve", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_059",
    "text": "Ποια αρχαία φωτεινή θεότητα των ονείρων σε μορφή γιγάντιας νυχτοπεταλούδας είναι η πραγματική πηγή της μόλυνσης στο «Hollow Knight»;",
    "answers": ["The Radiance (Η Ακτινοβολία)", "The Pale King", "The White Lady", "Grimm"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Radiance σφραγίστηκε μέσα στο μυαλό του Hollow Knight, αλλά η ξεχασμένη της οργή ξέσπασε στον κόσμο του Hallownest με τη μορφή πορτοκαλί μόλυνσης των ονείρων.",
    "funFacts": [
      "Για να πολεμήσει τη Radiance, ο παίκτης πρέπει να αποκτήσει το Awoken Dream Nail και να μπει μέσα στο μυαλό του τελικού αφεντικού.",
      "Η υπέρτατη εκδοχή της στο DLC 'Godmaster', η 'Absolute Radiance', θεωρείται μία από τις πιο δύσκολες προκλήσεις σε ολόκληρο το σύγχρονο gaming."
    ],
    "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
    "locale": "el-GR",
    "tags": ["hollow-knight", "the-radiance", "team-cherry", "indie"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_060",
    "text": "Ποιος Αμερικανός σχεδιαστής δημιούργησε το αρχικό επιτραπέζιο RPG «Cyberpunk 2020» (1990) στο οποίο βασίστηκε το «Cyberpunk 2077»;",
    "answers": ["William Gibson", "Mike Pondsmith", "Bruce Sterling", "Richard Garriott"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Mike Pondsmith ίδρυσε την R. Talsorian Games και δημιούργησε τον κόσμο του Cyberpunk, συνεργαζόμενος στενά με τη CD Projekt Red ως σύμβουλος.",
    "funFacts": [
      "Ο ίδιος ο Pondsmith δάνεισε τη φωνή του στον ραδιοφωνικό παραγωγό Maximum Mike του σταθμού Morro Rock Radio μέσα στο Cyberpunk 2077.",
      "Εμπνεύστηκε το σύστημα μάχης και τον ρυθμό του παιχνιδιού από την ταινία 'Blade Runner' του Ridley Scott και τα μυθιστορήματα του Walter Jon Williams."
    ],
    "source": "https://en.wikipedia.org/wiki/Mike_Pondsmith",
    "locale": "el-GR",
    "tags": ["cyberpunk-2077", "mike-pondsmith", "rpg", "tabletop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'medium', 3, questions)

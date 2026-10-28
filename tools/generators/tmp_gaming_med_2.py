# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "gaming_med_061",
    "text": "Ποιος εκκεντρικός ιδρυτής και διευθύνων σύμβουλος της Aperture Science εκφωνεί ηχογραφημένα μηνύματα για τα λεμόνια στο «Portal 2»;",
    "answers": ["Cave Johnson", "Wallace Breen", "Wheatley", "Dr. Isaac Kleiner"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Cave Johnson ίδρυσε την Aperture Fixtures (που μετεξελίχθηκε σε Aperture Science) και είναι διάσημος για τον οργισμένο μονόλογό του: 'Όταν η ζωή σου δίνει λεμόνια, μην φτιάξεις λεμονάδα, κάψε το σπίτι της ζωής με λεμόνια!'.",
    "funFacts": [
      "Τη φωνή του Cave Johnson χάρισε ο βραβευμένος με Όσκαρ ηθοποιός J.K. Simmons.",
      "Η εταιρεία ξεκίνησε τη δεκαετία του 1940 κατασκευάζοντας κουρτίνες μπάνιου προτού στραφεί στα πειράματα τηλεμεταφοράς και πυλών."
    ],
    "source": "https://en.wikipedia.org/wiki/Portal_2",
    "locale": "el-GR",
    "tags": ["portal-2", "cave-johnson", "valve", "jk-simmons"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_062",
    "text": "Ποιο βιομηχανικό εργαλείο εξόρυξης χρησιμοποιεί ο Isaac Clarke ως το πιο αποτελεσματικό όπλο ακρωτηριασμού των Necromorphs στο «Dead Space»;",
    "answers": ["Pulse Rifle", "Plasma Cutter", "Line Gun", "Flamethrower"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το 211-V Plasma Cutter επιτρέπει στον παίκτη να αλλάζει τη φορά των τριών δεσμών λέιζερ από οριζόντια σε κάθετη για ακριβή αποκοπή των άκρων των τεράτων.",
    "funFacts": [
      "Το κεντρικό μήνυμα επιβίωσης γραμμένο με αίμα στους τοίχους του USG Ishimura είναι: 'Cut off their limbs' ('Κόψτε τα άκρα τους').",
      "Υπάρχει ειδικό τρόπαιο/επίτευγμα ('One Gun') για τους παίκτες που ολοκληρώνουν ολόκληρο το παιχνίδι χρησιμοποιώντας αποκλειστικά και μόνο το Plasma Cutter."
    ],
    "source": "https://el.wikipedia.org/wiki/Dead_Space_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["dead-space", "plasma-cutter", "isaac-clarke", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_063",
    "text": "Ποιος γιγάντιος λύκος κρατάει ένα τεράστιο σπαθί στο στόμα του και φυλάει τον τάφο του ιππότη Artorias στο αρχικό «Dark Souls»;",
    "answers": ["Gwyn", "Gravelord Nito", "Great Grey Wolf Sif", "Seath the Scaleless"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Sif ήταν ο πιστός σύντροφος του Artorias the Abysswalker και προστατεύει το δαχτυλίδι Covenant of Artorias ώστε κανείς άλλος να μην χαθεί στην Άβυσσο.",
    "funFacts": [
      "Εάν ο παίκτης σώσει τον Sif στο DLC 'Artorias of the Abyss' πριν αντιμετωπίσει το αφεντικό στο κυρίως παιχνίδι, εμφανίζεται ένα συγκινητικό εναλλακτικό cutscene όπου ο λύκος αναγνωρίζει τη μυρωδιά του παίκτη.",
      "Όταν η υγεία του Sif πέσει πολύ χαμηλά, αρχίζει να κουτσαίνει και δυσκολεύεται να κουνήσει το βαρύ σπαθί, προκαλώντας έντονη συναισθηματική φόρτιση στους παίκτες."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "sif", "artorias", "fromsoftware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_064",
    "text": "Σε ποιο ιστορικό κτίριο στεγαζόταν αρχικά το αστυνομικό τμήμα (R.P.D.) της Raccoon City πριν μετατραπεί σε αστυνομικό σταθμό στο «Resident Evil 2»;",
    "answers": ["Σε παλιό δημαρχείο", "Σε εγκαταλελειμμένο νοσοκομείο", "Σε έπαυλη ευγενών", "Σε μουσείο τέχνης (Art museum)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το κτίριο του R.P.D. ήταν πρώην μουσείο τέχνης που αγοράστηκε από την πόλη το 1969, γεγονός που εξηγεί τα περίτεχνα αγάλματα, τους μυστικούς μηχανισμούς και τα περίεργα κλειδιά.",
    "funFacts": [
      "Ο διεφθαρμένος αρχηγός της αστυνομίας Brian Irons ήταν μανιώδης συλλέκτης έργων τέχνης και ταριχευμένων ζώων.",
      "Η διάταξη του αστυνομικού τμήματος στο remake του 2019 αναδημιουργήθηκε με φωτορεαλιστική πιστότητα χάρη στη μηχανή RE Engine της Capcom."
    ],
    "source": "https://en.wikipedia.org/wiki/Resident_Evil_2",
    "locale": "el-GR",
    "tags": ["resident-evil-2", "rpd", "capcom", "survival-horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_065",
    "text": "Ποιο μαγικό σημείο (Witcher Sign) χρησιμοποιεί ο Geralt of Rivia για να δημιουργήσει μια προστατευτική ενεργειακή ασπίδα γύρω από το σώμα του;",
    "answers": ["Quen", "Igni", "Aard", "Axii"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Quen απορροφά την επόμενη εχθρική επίθεση χωρίς να δεχτεί ζημιά ο Geralt, ενώ στην αναβαθμισμένη του μορφή λειτουργεί ως ενεργός θόλος που αποκαθιστά υγεία.",
    "funFacts": [
      "Τα υπόλοιπα βασικά σημεία είναι το Igni (φωτιά), το Aard (τηλεκινητική ριπή), το Axii (νοητικός έλεγχος) και το Yrden (μαγική παγίδα επιβράδυνσης).",
      "Τα Σημεία (Signs) είναι απλές μορφές μαγείας που εκτελούνται με μονοκόμματες χειρονομίες, σχεδιασμένες για άμεση χρήση εν ώρα ξιφομαχίας."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
    "locale": "el-GR",
    "tags": ["witcher", "quen", "geralt", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_066",
    "text": "Ποιο ρομποτικό σακίδιο πλάτης με αντλία νερού βοηθά τον Mario να καθαρίσει τη μαγική μπογιά στο «Super Mario Sunshine» (2002);",
    "answers": ["Poltergust 3000", "F.L.U.D.D.", "AquaPack", "HydroJet"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το F.L.U.D.D. (Flash Liquidizer Ultra Dousing Device) κατασκευάστηκε από τον Professor E. Gadd και διαθέτει πολλαπλά ακροφύσια (Hover, Rocket, Turbo).",
    "funFacts": [
      "Το F.L.U.D.D. έχει τεχνητή νοημοσύνη και μιλάει στον Mario με συνθετική φωνή στα αγγλικά.",
      "Ο Mario κατηγορείται άδικα ότι βανδάλισε το τροπικό νησί Isle Delfino από έναν σωσία του, τον Shadow Mario (ο οποίος αποκαλύπτεται ως ο Bowser Jr.)."
    ],
    "source": "https://en.wikipedia.org/wiki/Super_Mario_Sunshine",
    "locale": "el-GR",
    "tags": ["mario-sunshine", "fludd", "gamecube", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_067",
    "text": "Ποιες τρεις εξωγήινες φυλές αποτελούσαν αρχικά το Συμβούλιο της Ακρόπολης (Citadel Council) στο πρώτο «Mass Effect»;",
    "answers": ["Krogan, Quarian, Batarian", "Turian, Geth, Vorcha", "Asari, Salarian, Turian", "Prothean, Volus, Elcor"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Asari (διπλωματία), οι Salarian (πληροφορίες/επιστήμη) και οι Turian (στρατιωτική ισχύς) διοικούσαν τον γαλαξία πριν η ανθρωπότητα κερδίσει μια θέση στο Συμβούλιο.",
    "funFacts": [
      "Οι Asari ήταν η πρώτη φυλή που ανακάλυψε την Ακρόπολη μετά την εξαφάνιση των Protheans και πρότεινε τη συγκρότηση του πολυφυλετικού Συμβουλίου.",
      "Οι Krogan βοήθησαν στη νίκη κατά των Rachni αλλά αποκλείστηκαν από το Συμβούλιο και υποτάχθηκαν στον βιολογικό περιορισμό γεννήσεων Genophage."
    ],
    "source": "https://el.wikipedia.org/wiki/Mass_Effect_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["mass-effect", "citadel-council", "bioware", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_068",
    "text": "Πώς ονομάζεται η αιωρούμενη νεοκλασική πόλη στα σύννεφα όπου διαδραματίζεται το «BioShock Infinite» (2013);",
    "answers": ["Rapture", "Olympus", "Sky City", "Columbia"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Columbia χτίστηκε από την αμερικανική κυβέρνηση ως ιπτάμενο τεχνολογικό θαύμα, πριν αποσχιστεί υπό τον θρησκευτικό φανατισμό του προφήτη Zachary Comstock.",
    "funFacts": [
      "Η πόλη παραμένει στον αέρα χάρη σε γιγάντια αερόστατα και την κβαντική τεχνολογία αιώρησης που ανακάλυψε η επιστήμονας Rosalind Lutece.",
      "Ο πρωταγωνιστής Booker DeWitt στέλνεται στην Columbia με την εντολή: 'Bring us the girl, and wipe away the debt' ('Φέρε μας το κορίτσι και σβήσε το χρέος')."
    ],
    "source": "https://el.wikipedia.org/wiki/BioShock_Infinite",
    "locale": "el-GR",
    "tags": ["bioshock-infinite", "columbia", "irrational-games", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_069",
    "text": "Ποια μεγάλη βιομηχανική πόλη του νότου στο «Red Dead Redemption 2» είναι εμπνευσμένη από την πραγματική Νέα Ορλεάνη;",
    "answers": ["Saint Denis", "Blackwater", "Valentine", "Rhodes"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η πόλη Saint Denis στην πολιτεία Lemoyne αποτυπώνει τη γαλλική αποικιακή αρχιτεκτονική, τα τραμ, την έντονη εκβιομηχάνιση και τους βάλτους της Νέας Ορλεάνης.",
    "funFacts": [
      "Κατά τη διάρκεια της ανάπτυξης, η πόλη ονομαζόταν προσωρινά 'New Bordeaux' πριν μετονομαστεί σε Saint Denis.",
      "Η άφιξη της συμμορίας του Dutch στο Saint Denis σηματοδοτεί τη σύγκρουση του παλιού κόσμου των παρανόμων με τον σύγχρονο αστικό πολιτισμό."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "locale": "el-GR",
    "tags": ["red-dead-redemption", "saint-denis", "rockstar-games", "open-world"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_070",
    "text": "Ποιος πανίσχυρος δαίμονας του «Doom» διαθέτει μηχανικό πόδι και εκτοξευτή ρουκετών προσαρμοσμένο στο αριστερό του χέρι;",
    "answers": ["Baron of Hell", "Cyberdemon", "Mancubus", "Arch-Vile"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Cyberdemon είναι ο αρχηγός των δυνάμεων της κόλασης στο Tower of Babel στο αρχικό Doom (1993), συνδυάζοντας σάρκα δαίμονα και κυβερνητική τεχνολογία.",
    "funFacts": [
      "Ο επίσημος οδηγός στρατηγικής του παιχνιδιού περιείχε τη θρυλική συμβουλή για την εξόντωσή του: 'To defeat the Cyberdemon, shoot at it until it dies'.",
      "Επανεμφανίζεται σε σχεδόν κάθε τίτλο της σειράς, συμπεριλαμβανομένων των Doom II, Doom 3 και Doom (2016)."
    ],
    "source": "https://en.wikipedia.org/wiki/Doom_(1993_video_game)",
    "locale": "el-GR",
    "tags": ["doom", "cyberdemon", "id-software", "fps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_071",
    "text": "Ποιο είναι το όνομα του παίκτη που έγινε παγκόσμιο viral meme το 2005 όταν όρμησε στο Upper Blackrock Spire στο «World of Warcraft» φωνάζοντας το όνομά του;",
    "answers": ["Athene", "Swifty", "Leeroy Jenkins", "Kungen"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Leeroy Jenkins (Ben Schulz) αγνόησε το προσεκτικό πλάνο της ομάδας του Paladin και όρμησε στο Rookery φωνάζοντας 'Leeeeeroy Jenkins!', οδηγώντας όλους στον θάνατο.",
    "funFacts": [
      "Το βίντεο έγινε ένα από τα πιο διάσημα viral βίντεο στην ιστορία του ίντερνετ και αναφέρθηκε σε σειρές όπως το South Park, το Jeopardy! και το How I Met Your Mother.",
      "Η Blizzard τον τίμησε ενσωματώνοντάς τον ως επίσημο τίτλο παίκτη ('Jenkins'), επίτευγμα (achievement) και κάρτα στο Hearthstone."
    ],
    "source": "https://el.wikipedia.org/wiki/Leeroy_Jenkins",
    "locale": "el-GR",
    "tags": ["world-of-warcraft", "leeroy-jenkins", "memes", "blizzard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_072",
    "text": "Ποιος βασανισμένος άνδρας ταξιδεύει στην ομιχλώδη πόλη στο «Silent Hill 2» (2001) αφού έλαβε ένα γράμμα από τη νεκρή σύζυγό του Mary;",
    "answers": ["Harry Mason", "Henry Townshend", "Travis Grady", "James Sunderland"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο James Sunderland αναζητά την αλήθεια για τον θάνατο της συζύγου του, αντιμετωπίζοντας τα τέρατα που γεννά το ίδιο του το υποσυνείδητο και οι τύψεις του.",
    "funFacts": [
      "Το Silent Hill 2 θεωρείται ευρέως ένα από τα κορυφαία ψυχολογικά δράματα τρόμου στην ιστορία των βιντεοπαιχνιδιών.",
      "Το παιχνίδι διαθέτει πολλαπλά τέλη που καθορίζονται όχι από επιλογές διαλόγων αλλά από ανεπαίσθητες συμπεριφορές του παίκτη κατά το gameplay."
    ],
    "source": "https://el.wikipedia.org/wiki/Silent_Hill_2",
    "locale": "el-GR",
    "tags": ["silent-hill-2", "james-sunderland", "konami", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_073",
    "text": "Ποια είναι η πανίσχυρη Βασίλισσα των Βαλκυριών που αποτελεί το πιο απαιτητικό προαιρετικό αφεντικό στο «God of War» (2018);",
    "answers": ["Σίγκρουν (Sigrún)", "Γκούντρουν (Gudrun)", "Φρέγια (Freya)", "Όλρουν (Olrun)"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Sigrún απελευθερώνεται αφού ο Κράτος νικήσει τις υπόλοιπες οκτώ Βαλκυρίες, συνδυάζοντας όλες τις επιθέσεις και τις κινήσεις των προηγούμενων μαχών.",
    "funFacts": [
      "Η Sigrún ανέλαβε τη θέση της Βασίλισσας μετά την κατάρα που επέβαλε ο Όντιν στην αρχική Βασίλισσα, τη θεά Φρέγια.",
      "Η νίκη εναντίον της απαιτεί άψογο συγχρονισμό parry, αποφυγών και αναγνώριση των κραυγών της ('Valhalla!')."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "sigrun", "valkyrie", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_074",
    "text": "Ποιο είναι το πραγματικό μικρό όνομα του Big Boss (Naked Snake) στη σειρά «Metal Gear» του Hideo Kojima;",
    "answers": ["David", "John (Jack)", "George", "Eli"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Naked Snake αποκαλείται Jack από τη μέντορά του The Boss και συστήνεται ως John στον Major Zero κατά την επιχείρηση Virtuous Mission στο Metal Gear Solid 3.",
    "funFacts": [
      "Αντίθετα, ο κλώνος του Solid Snake έχει το πραγματικό όνομα David, εμπνευσμένο από τον Dave Bowman στην ταινία '2001: Η Οδύσσεια του Διαστήματος'.",
      "Ο Big Boss ίδρυσε τους στρατούς χωρίς σύνορα 'Militaires Sans Frontières' (MSF) και το κράτος Outer Heaven."
    ],
    "source": "https://en.wikipedia.org/wiki/Big_Boss_(Metal_Gear)",
    "locale": "el-GR",
    "tags": ["metal-gear", "big-boss", "naked-snake", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_075",
    "text": "Ποια μυστηριώδης υπερφυσική οντότητα του Void χαρίζει το μαγικό του σημάδι και δυνάμεις στον Corvo Attano στο «Dishonored»;",
    "answers": ["The Lord Regent", "Daud", "The Outsider", "Anton Sokolov"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Outsider είναι μια αρχαία θεότητα που εμφανίζεται στα όνειρα επιλεγμένων ανθρώπων, παρατηρώντας με περιέργεια πώς θα χρησιμοποιήσουν τις δυνάμεις τους.",
    "funFacts": [
      "Χαρίζει στον Corvo ικανότητες όπως η τηλεμεταφορά (Blink), η κατοχή σωμάτων ζώων και ανθρώπων (Possession) και το πάγωμα του χρόνου (Bend Time).",
      "Το Dishonored επιτρέπει στον παίκτη να ολοκληρώσει ολόκληρη την ιστορία χωρίς να σκοτώσει ούτε έναν άνθρωπο (Ghost / Clean Hands)."
    ],
    "source": "https://en.wikipedia.org/wiki/Dishonored",
    "locale": "el-GR",
    "tags": ["dishonored", "the-outsider", "arkane-studios", "stealth"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_076",
    "text": "Ποιο είναι το επίσημο λατινικό σύνθημα και πολεμικός χαιρετισμός των μελών της Αδελφότητας του Ατσαλιού στο «Fallout 4»;",
    "answers": ["Semper Fidelis", "Carpe Diem", "Veni Vidi Vici", "Ad Victoriam"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το 'Ad Victoriam' (που σημαίνει στα λατινικά 'Προς τη Νίκη') καθιερώθηκε υπό την ηγεσία του Elder Arthur Maxson ως ο επίσημος χαιρετισμός των Paladins.",
    "funFacts": [
      "Η Αδελφότητα του Ατσαλιού φτάνει στη Βοστώνη πάνω στο επιβλητικό ιπτάμενο αερόπλοιο Prydwen.",
      "Η κύρια αποστολή τους είναι η διαφύλαξη και η κατάσχεση της προηγμένης προπολεμικής τεχνολογίας ώστε να μην ξανακαταστραφεί η ανθρωπότητα."
    ],
    "source": "https://el.wikipedia.org/wiki/Fallout_4",
    "locale": "el-GR",
    "tags": ["fallout-4", "brotherhood-of-steel", "ad-victoriam", "bethesda"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_077",
    "text": "Ποια πανίσχυρη ιαπωνική πολυεθνική megacorporation κυριαρχεί στη Night City υπό την ηγεσία του Saburo στο «Cyberpunk 2077»;",
    "answers": ["Arasaka", "Militech", "Kang Tao", "Biotechnica"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Arasaka Corporation εξειδικεύεται στην εταιρική ασφάλεια, τις τραπεζικές υπηρεσίες και την κατασκευή όπλων, όντας η πιο επίφοβη δύναμη στον πλανήτη.",
    "funFacts": [
      "Ο πατριάρχης της εταιρείας Saburo Arasaka είναι 158 ετών κατά τα γεγονότα του παιχνιδιού, επιβιώνοντας χάρη σε προηγμένες κυβερνοθεραπείες.",
      "Η Arasaka ανέπτυξε το πρόγραμμα 'Secure Your Soul' και το τσιπ Relic που αποθηκεύει ψηφιακά την ανθρώπινη συνείδηση."
    ],
    "source": "https://el.wikipedia.org/wiki/Cyberpunk_2077",
    "locale": "el-GR",
    "tags": ["cyberpunk-2077", "arasaka", "cd-projekt-red", "rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_078",
    "text": "Ποιο ισχυρό μηχανοκίνητο εργαλείο προστέθηκε ως όπλο κοντινής μάχης στο «Left 4 Dead 2», εξολοθρεύοντας ορδές ζόμπι σε δευτερόλεπτα αλλά με περιορισμένα καύσιμα;",
    "answers": ["Χορτοκοπτικό", "Αλυσοπρίονο (Chainsaw)", "Τρυπάνι εδάφους", "Κυκλικό πριόνι"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Chainsaw προκαλεί 1.000 πόντους ζημιάς ανά δευτερόλεπτο και διαθέτει καύσιμα για 20 δευτερόλεπτα συνεχούς λειτουργίας, αλλά ο θόρυβός του προσελκύει επιπλέον ζόμπι.",
    "funFacts": [
      "Είναι ένα από τα ελάχιστα όπλα που μπορούν να εξοντώσουν έναν Witch ή έναν Tank σε ελάχιστα δευτερόλεπτα συνεχούς επαφής.",
      "Όταν εξαντληθούν τα καύσιμά του, ο χαρακτήρας πετάει αυτόματα το αλυσοπρίονο και γυρίζει στο πιστόλι του."
    ],
    "source": "https://el.wikipedia.org/wiki/Left_4_Dead_2",
    "locale": "el-GR",
    "tags": ["left-4-dead-2", "chainsaw", "valve", "zombies"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_079",
    "text": "Ποιος φιλικός περιπλανώμενος με ένα όστρακο στο κεφάλι συναντά τον ιππότη σε διάφορα σημεία του Hallownest και τον βοηθά στη μάχη με το Uumuu στο «Hollow Knight»;",
    "answers": ["Zote the Mighty", "Cloth", "Quirrel", "Tiso"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Quirrel ήταν ο πρώην μαθητής της Monomon the Teacher και επέστρεψε στο Hallownest για να εκπληρώσει το καθήκον του να σπάσει τη σφραγίδα της δασκάλας του.",
    "funFacts": [
      "Το όπλο του είναι ένα καμπυλωτό καρφί και το όστρακο που φοράει στο κεφάλι είναι στην πραγματικότητα η μάσκα της Monomon.",
      "Μετά την ολοκλήρωση της αποστολής του, συναντάται για τελευταία φορά στη λίμνη Blue Lake, απολαμβάνοντας τη γαλήνη του νερού."
    ],
    "source": "https://en.wikipedia.org/wiki/Hollow_Knight",
    "locale": "el-GR",
    "tags": ["hollow-knight", "quirrel", "team-cherry", "indie"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_080",
    "text": "Ποιος υπερ-μυώδης Αυστραλός που κυνηγά κροκόδειλους και δεν φοράει ποτέ πουκάμισο είναι ο πρόεδρος της εταιρείας Mann Co. στο σύμπαν του «Team Fortress 2»;",
    "answers": ["Redmond Mann", "Blutarch Mann", "Gray Mann", "Saxton Hale"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Saxton Hale είναι ο εκκεντρικός επικεφαλής της Mann Co., της εταιρείας που προμηθεύει όπλα και καπέλα και στις δύο αντίπαλες ομάδες μισθοφόρων (RED και BLU).",
    "funFacts": [
      "Το στήθος του έχει τρίχες διαμορφωμένες στο ακριβές γεωγραφικό σχήμα της Αυστραλίας.",
      "Το 2023, η Valve τον πρόσθεσε ως επίσημο playable boss σε ειδικό game mode του Team Fortress 2 ('VS Saxton Hale')."
    ],
    "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "saxton-hale", "valve", "lore"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_081",
    "text": "Πώς ονομάζονται οι τυφλοί μολυσμένοι στο «The Last of Us» των οποίων το κεφάλι έχει σχιστεί από τον μύκητα και εντοπίζουν θηράματα αποκλειστικά με ηχοεντοπισμό;",
    "answers": ["Clickers", "Runners", "Stalkers", "Bloaters"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Clickers βρίσκονται στο τρίτο στάδιο μόλυνσης του Cordyceps, παράγοντας ανατριχιαστικούς ήχους κλικ για να εντοπίσουν τις κινήσεις του Joel και της Ellie στον χώρο.",
    "funFacts": [
      "Εάν ένας Clicker πιάσει τον παίκτη, προκαλεί άμεσο θάνατο (instant kill) εκτός εάν ο παίκτης διαθέτει μαχαίρι (Shiv) για άμυνα.",
      "Οι ανατριχιαστικοί ήχοι κλικ των Clickers δημιουργήθηκαν από τους ηθοποιούς φωνής Misty Lee και Phillip Kovats χρησιμοποιώντας μόνο τον λαιμό τους."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Last_of_Us",
    "locale": "el-GR",
    "tags": ["the-last-of-us", "clickers", "naughty-dog", "cordyceps"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_082",
    "text": "Ποιος Αμερικανός στρατιωτικός με το χαρακτηριστικό ψηλό ξανθό κούρεμα έγινε διάσημος στο «Street Fighter» για το μουσικό θέμα που «ταιριάζει με τα πάντα»;",
    "answers": ["Nash", "Guile", "Cody", "Luke"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Major Guile της αμερικανικής πολεμικής αεροπορίας μάχεται για να εκδικηθεί τον θάνατο του φίλου του Charlie Nash από τον M. Bison.",
    "funFacts": [
      "Το viral meme 'Guile's Theme Goes with Everything' ξεκίνησε όταν χρήστες διαπίστωσαν ότι το γρήγορο τέμπο του κομματιού ταίριαζε με οποιαδήποτε κινηματογραφική σκηνή δράσης.",
      "Οι δύο χαρακτηριστικές του κινήσεις είναι το Sonic Boom και το Flash Kick (Somersault Kick)."
    ],
    "source": "https://en.wikipedia.org/wiki/Guile_(Street_Fighter)",
    "locale": "el-GR",
    "tags": ["street-fighter", "guile", "capcom", "fighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_083",
    "text": "Σε ποιο φανταστικό υποβρύχιο ομαδικό άθλημα με μπάλα διαπρέπει ο πρωταγωνιστής Tidus στο ιστορικό JRPG «Final Fantasy X» (2001);",
    "answers": ["Sphere Grid", "Chocobo Racing", "Blitzball (Μπλίτζμπολ)", "Triple Triad"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Blitzball είναι ένα άθλημα που παίζεται μέσα σε μια τεράστια αιωρούμενη σφαίρα νερού, όπου δύο ομάδες των έξι παικτών κολυμπούν και σουτάρουν.",
    "funFacts": [
      "Ο Tidus ήταν ο σταρ παίκτης της ομάδας 'Zanarkand Abes' πριν μεταφερθεί μυστηριωδώς στον κόσμο της Spira.",
      "Η διάσημη ειδική τεχνική σουτ του πατέρα του Tidus ονομάζεται 'Jecht Shot'."
    ],
    "source": "https://el.wikipedia.org/wiki/Final_Fantasy_X",
    "locale": "el-GR",
    "tags": ["final-fantasy", "tidus", "blitzball", "square-enix"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_084",
    "text": "Ποιο είναι το όνομα του χαρισματικού πρώην σερίφη των Terran που ηγείται των επαναστατών Raiders εναντίον της Dominion στο «StarCraft»;",
    "answers": ["Arcturus Mengsk", "Tychus Findlay", "Gabriel Tosh", "Jim Raynor"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Jim Raynor ξεκινά ως σερίφης στον πλανήτη Mar Sara και εξελίσσεται στον κεντρικό ανθρώπινο ήρωα του StarCraft, ερωτευμένος με τη Sarah Kerrigan.",
    "funFacts": [
      "Το θρυλικό διαστημόπλοιο-ναυαρχίδα των επαναστατών του Raynor ονομάζεται Hyperion.",
      "Στο StarCraft II: Wings of Liberty (2010), η ιστορία επικεντρώνεται στην προσπάθεια του Raynor να επαναφέρει την ανθρώπινη μορφή της Kerrigan από τη μόλυνση των Zerg."
    ],
    "source": "https://el.wikipedia.org/wiki/StarCraft",
    "locale": "el-GR",
    "tags": ["starcraft", "jim-raynor", "blizzard", "rts"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_085",
    "text": "Ποια ανίκητη ξιφομάχος των Lands Between στο «Elden Ring» προειδοποιεί τον παίκτη με τη φράση «I am Malenia, Blade of Miquella, and I have never known defeat»;",
    "answers": ["Malenia", "Ranni the Witch", "Queen Marika", "Rellana"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Malenia είναι ένα από τα πιο διαβόητα δύσκολα bosses στην ιστορία των Soulslike παιχνιδιών, θεραπεύοντας τον εαυτό της με κάθε χτύπημα που καταφέρει στον παίκτη.",
    "funFacts": [
      "Η χαρακτηριστική της αλληλουχία επιθέσεων 'Waterfowl Dance' είναι εξαιρετικά δύσκολο να αποφευχθεί και έγινε εφιάλτης για εκατομμύρια παίκτες.",
      "Ένας θρυλικός παίκτης της κοινότητας με το όνομα 'Let Me Solo Her' έγινε παγκόσμιο φαινόμενο βοηθώντας πάνω από 1.000 παίκτες να νικήσουν τη Malenia φορώντας μόνο ένα πιθάρι στο κεφάλι."
    ],
    "source": "https://el.wikipedia.org/wiki/Elden_Ring",
    "locale": "el-GR",
    "tags": ["elden-ring", "malenia", "fromsoftware", "bosses"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_086",
    "text": "Ποια μυθική χαμένη πόλη των Ιμαλαΐων και το Δέντρο της Ζωής αναζητά ο Nathan Drake στο «Uncharted 2: Among Thieves» (2009);",
    "answers": ["Ελ Ντοράντο", "Shambhala (Σαμπάλα)", "Ατλαντίδα των Άμμων", "Libertalia"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Drake ακολουθεί τα ίχνη του χαμένου στόλου του Μάρκο Πόλο για να βρει τη μυθική Shambhala και τον πολύτιμο λίθο Cintamani Stone.",
    "funFacts": [
      "Η πόλη φυλάσσεται από τους πανύψηλους Guardians, άγριους υπεράνθρωπους πολεμιστές με μπλε δέρμα που έχουν πιει από το ρετσίνι του Δέντρου της Ζωής.",
      "Το Uncharted 2 απέσπασε πάνω από 200 βραβεία Game of the Year και θεωρείται από πολλούς το αποκορύφωμα της σειράς."
    ],
    "source": "https://el.wikipedia.org/wiki/Uncharted_2:_Among_Thieves",
    "locale": "el-GR",
    "tags": ["uncharted-2", "shambhala", "naughty-dog", "nathan-drake"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_087",
    "text": "Από τι υλικό ήταν φτιαγμένο το αρχικό μαστίγιο της οικογένειας Belmont πριν ευλογηθεί με την αυτοθυσία της Sara Trantoul για να γίνει το Vampire Killer;",
    "answers": ["Από καθαρό ασήμι", "Από τρίχες μονόκερου", "Αλχημικό δερμάτινο μαστίγιο (Leather Whip)", "Από σιδερένια αλυσίδα"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Στο Castlevania: Lament of Innocence (2003), ο Leon Belmont χρησιμοποιεί το 'Whip of Alchemy', το οποίο μετατρέπεται στο ιερό Vampire Killer μετά από ειδική τελετή.",
    "funFacts": [
      "Το Vampire Killer μπορεί να ασκηθεί με πλήρη ισχύ μόνο από τους γνήσιους απογόνους της αιματολογικής γραμμής των Belmont.",
      "Εάν κάποιος άλλος πολεμιστής χρησιμοποιήσει το μαστίγιο (όπως ο John Morris στο Bloodlines), το όπλο απορροφά σταδιακά τη ζωτική του ενέργεια."
    ],
    "source": "https://el.wikipedia.org/wiki/Castlevania",
    "locale": "el-GR",
    "tags": ["castlevania", "vampire-killer", "belmont", "konami"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_088",
    "text": "Πώς ονομάζεται το πειρατικό ιστιοφόρο μπρίκι (brig) που κυβερνά ο Edward Kenway στην Καραϊβική στο «Assassin's Creed IV: Black Flag»;",
    "answers": ["Queen Anne's Revenge", "Aquila", "Black Pearl", "Jackdaw"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Jackdaw (που πήρε το όνομά του από το ομώνυμο πουλί κάργια) είναι το πλοίο του Edward Kenway, το οποίο οι παίκτες αναβαθμίζουν με κανόνια, όλμους και ενισχυμένο σκελετό.",
    "funFacts": [
      "Ο Edward Kenway τοποθέτησε ως πρώτο αξιωματικό του πλοίου τον Adéwalé, έναν πρώην σκλάβο που δραπέτευσε και έγινε Ασσασίνος.",
      "Οι παίκτες μπορούσαν να συλλέγουν παρτιτούρες σε πόλεις για να μαθαίνουν οι ναύτες νέα αυθεντικά ιστορικά ναυτικά τραγούδια (sea shanties)."
    ],
    "source": "https://el.wikipedia.org/wiki/Assassin%27s_Creed_IV:_Black_Flag",
    "locale": "el-GR",
    "tags": ["assassins-creed", "black-flag", "jackdaw", "ubisoft"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_089",
    "text": "Ποιο διακοσμητικό αντικείμενο κήπου έπρεπε να κουβαλήσουν οι παίκτες σε όλο το παιχνίδι μέχρι τον πύραυλο για το επίτευγμα «Little Rocket Man» στο «Half-Life 2: Episode Two»;",
    "answers": ["Ένας πήλινος νάνος κήπου (Gnome Chompski)", "Ένα πλαστικό ροζ φλαμίνγκο", "Μια γλάστρα με λουλούδια", "Ένα ρολόι τοίχου"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο νάνος Gnome Chompski έπρεπε να τοποθετηθεί στο αυτοκίνητο και να μεταφερθεί προσεκτικά μέσα από μάχες για να τοποθετηθεί τελικά στον πύραυλο του White Forest.",
    "funFacts": [
      "Το επίτευγμα έγινε τόσο δημοφιλές που ο Gabe Newell έστειλε έναν πραγματικό μεταλλικό νάνο Chompski από τιτάνιο στο διάστημα το 2020 με πύραυλο της Rocket Lab για φιλανθρωπικό σκοπό.",
      "Ο νάνος επανεμφανίστηκε αργότερα και στο παιχνίδι εικονικής πραγματικότητας Half-Life: Alyx (2020)."
    ],
    "source": "https://en.wikipedia.org/wiki/Half-Life_2:_Episode_Two",
    "locale": "el-GR",
    "tags": ["half-life", "gnome-chompski", "valve", "achievements"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_090",
    "text": "Από ποια γεωγραφική περιοχή της Ευρώπης μετανάστευσε ο βετεράνος πολέμου Niko Bellic στη Liberty City στο «Grand Theft Auto IV» (2008);",
    "answers": ["Από τη Σκανδιναβία", "Από τα Βαλκάνια / Ανατολική Ευρώπη", "Από την Ιβηρική Χερσόνησο", "Από τη Σικελία"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Niko Bellic πολέμησε στους γιουγκοσλαβικούς πολέμους και ταξίδεψε στην Αμερική μετά από πρόσκληση του ξαδέλφου του Roman, αναζητώντας τον άνθρωπο που πρόδωσε τη μονάδα του.",
    "funFacts": [
      "Ο Roman καλεί συνεχώς τον Niko στο κινητό τηλέφωνο με την ιστορική ατάκα: 'Hey Niko, it's your cousin! Let's go bowling!'.",
      "Η ερμηνεία του ηθοποιού Michael Hollick ως Niko Bellic απέσπασε διθυραμβικές κριτικές για τον ρεαλισμό και τη μελαγχολία της."
    ],
    "source": "https://el.wikipedia.org/wiki/Grand_Theft_Auto_IV",
    "locale": "el-GR",
    "tags": ["gta-iv", "niko-bellic", "rockstar-games", "liberty-city"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_091",
    "text": "Ποιο είναι το τελικό μοβ Pokémon τύπου Φαντάσματος/Δηλητηρίου της πρώτης γενιάς που εξελίσσεται από τον Haunter μέσω ανταλλαγής (trade);",
    "answers": ["Gastly", "Misdreavus", "Gengar (Γκένγκαρ)", "Dusclops"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Gengar είναι ένα από τα πιο αναγνωρίσιμα Pokémon πρώτης γενιάς, διακρινόμενος για το πονηρό του χαμόγελο και τα κόκκινα μάτια του.",
    "funFacts": [
      "Υπάρχει μια διάσημη θεωρία των φίλων της σειράς ότι ο Gengar είναι στην πραγματικότητα η στοιχειωμένη σκιά του Clefable, λόγω της πανομοιότυπης σιλουέτας τους.",
      "Ο Gengar ήταν ένα από τα δύο πρώτα Pokémon που εμφανίστηκαν ποτέ στην ιστορία, στην εισαγωγική μάχη του αρχικού Pokémon Red στο Game Boy ενάντια στον Nidorino."
    ],
    "source": "https://el.wikipedia.org/wiki/Gengar",
    "locale": "el-GR",
    "tags": ["pokemon", "gengar", "nintendo", "kanto"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_092",
    "text": "Πώς ονομάζεται η χρυσαφένια μητρόπολη των θεών όπου ο παίκτης αντιμετωπίζει το διαβόητο δίδυμο Ornstein και Smough στο «Dark Souls»;",
    "answers": ["New Londo Ruins", "Lost Izalith", "The Catacombs", "Anor Londo"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Anor Londo είναι η λαμπερή πόλη του Lord Gwyn, η οποία όμως αποκαλύπτεται ότι είναι μια οφθαλμαπάτη συντηρούμενη από τη μαγεία του Gwyndolin.",
    "funFacts": [
      "Εάν ο παίκτης πυροβολήσει την τεράστια ψευδαίσθηση της πριγκίπισσας Gwynevere, ολόκληρος ο λαμπερός ουρανός του Anor Londo σκοτεινιάζει σε βαθιά νύχτα.",
      "Οι τοξότες Silver Knights πάνω στα στενά γείσα της πόλης (Anor Londo Archers) θεωρούνται από τα πιο εξοργιστικά σημεία για νέους παίκτες."
    ],
    "source": "https://el.wikipedia.org/wiki/Dark_Souls",
    "locale": "el-GR",
    "tags": ["dark-souls", "anor-londo", "fromsoftware", "soulslike"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_093",
    "text": "Από ποιο παράξενο θαλάσσιο πλάσμα του βυθού ανακαλύφθηκε η μεταλλαξιογόνος ουσία ADAM που κατέστρεψε την πόλη Rapture στο «BioShock»;",
    "answers": ["Από ένα σπάνιο είδος θαλάσσιου γυμνοσάλιαγκα (Sea slug)", "Από μια φωτεινή μέδουσα", "Από δηλητηριώδη κοράλλια", "Από ένα προϊστορικό καλαμάρι"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η επιστήμονας Brigid Tenenbaum παρατήρησε ότι ένας τραυματισμένος εργάτης γιατρεύτηκε ακαριαία μετά από δάγκωμα ενός θαλάσσιου γυμνοσάλιαγκα, ανακαλύπτοντας το ADAM.",
    "funFacts": [
      "Επειδή οι γυμνοσάλιαγκες παρήγαγαν ελάχιστες ποσότητες ADAM, η Dr. Tenenbaum άρχισε να τους εμφυτεύει στα στομάχια μικρών ορφανών κοριτσιών (Little Sisters).",
      "Η συνεχής χρήση πλασμιδίων ADAM προκαλεί έντονο σωματικό και ψυχικό εθισμό, μετατρέποντας τους πολίτες στους παρανοϊκούς Splicers."
    ],
    "source": "https://el.wikipedia.org/wiki/BioShock",
    "locale": "el-GR",
    "tags": ["bioshock", "adam", "rapture", "irrational-games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_094",
    "text": "Σε ποια εξωγήινη νομαδική φυλή ανήκει η Tali'Zorah στο «Mass Effect», τα μέλη της οποίας ζουν στον Στόλο Μετανάστευσης και φορούν περιβαλλοντικές στολές;",
    "answers": ["Drell", "Quarian (Κουάριαν)", "Volus", "Asari"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Quarians εκδιώχθηκαν από τον πλανήτη τους Rannoch από τα ρομπότ Geth που είχαν δημιουργήσει οι ίδιοι, ζώντας για αιώνες πάνω σε διαστημόπλοια με αδύναμο ανοσοποιητικό σύστημα.",
    "funFacts": [
      "Κάθε νεαρός Quarian πρέπει να ολοκληρώσει το 'Pilgrimage' (Προσκύνημα), φέρνοντας πίσω στον στόλο ένα πολύτιμο τεχνολογικό δώρο για να γίνει πλήρες μέλος.",
      "Το πρόσωπο της Tali καλύπτεται από μια ημιδιαφανή μοβ μάσκα, εξάπτοντας την περιέργεια των παικτών για τρία συνεχόμενα παιχνίδια."
    ],
    "source": "https://en.wikipedia.org/wiki/Tali%27Zorah",
    "locale": "el-GR",
    "tags": ["mass-effect", "tali", "quarian", "bioware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_095",
    "text": "Ποιος σκοτεινός μάγος του Μεσαίωνα στο «Chrono Trigger» ξεκινά ως κεντρικός αντίπαλος και μπορεί αργότερα να στρατολογηθεί ως playable μέλος της ομάδας;",
    "answers": ["Lavos", "Ozzie", "Magus (Janus)", "Dalton"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Magus αποκαλύπτεται ότι είναι ο πρίγκιπας Janus από το αρχαίο βασίλειο Zeal (12.000 π.Χ.), ο οποίος προσπαθούσε να εκδικηθεί το τέρας Lavos για την καταστροφή της οικογένειάς του.",
    "funFacts": [
      "Ο παίκτης έχει την επιλογή είτε να μονομαχήσει και να σκοτώσει τον Magus στο North Cape είτε να τον δεχτεί στην ομάδα του ως πανίσχυρο σύμμαχο.",
      "Το μουσικό θέμα μάχης του Magus είναι ένα από τα πιο αναγνωρισμένα και δημοφιλή κομμάτια του συνθέτη Yasunori Mitsuda."
    ],
    "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
    "locale": "el-GR",
    "tags": ["chrono-trigger", "magus", "square", "jrpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_096",
    "text": "Ποιο είναι το εμβληματικό ιπτάμενο τέρας (Wyvern) με τα κόκκινα λέπια που αποκαλείται 'Βασιλιάς των Ουρανών' στη σειρά «Monster Hunter» της Capcom;",
    "answers": ["Tigrex", "Nargacuga", "Zinogre", "Rathalos"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Rathalos εμφανίστηκε στο πρώτο Monster Hunter (2004) και αποτελεί την επίσημη μασκότ της σειράς, επιτιθέμενος με πύρινες ανάσες και δηλητηριώδη νύχια.",
    "funFacts": [
      "Το θηλυκό αντίστοιχό του ονομάζεται Rathian, είναι πράσινη και προτιμά να μάχεται στο έδαφος χρησιμοποιώντας την αγκαθωτή ουρά της.",
      "Ο Rathalos έχει εμφανιστεί ως ειδικό crossover boss σε άλλα διάσημα παιχνίδια, όπως το Super Smash Bros. Ultimate και το Final Fantasy XIV."
    ],
    "source": "https://en.wikipedia.org/wiki/Monster_Hunter",
    "locale": "el-GR",
    "tags": ["monster-hunter", "rathalos", "capcom", "action-rpg"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_097",
    "text": "Ποια ξύλινη κούκλα σε φυσικό ανθρώπινο μέγεθος ζωντανεύει και βοηθά τον κυνηγό να αναβαθμίσει τα στατιστικά του στο «Bloodborne»;",
    "answers": ["The Plain Doll", "Lady Maria", "Eileen the Crow", "Annalise"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Plain Doll βρίσκεται στο Hunter's Dream και αποκτά ζωή μόνο όταν ο παίκτης συγκεντρώσει τουλάχιστον έναν πόντο διορατικότητας (Insight).",
    "funFacts": [
      "Κατασκευάστηκε από τον πρώτο κυνηγό Gehrman κατ' εικόνα και ομοίωση της μαθήτριάς του Lady Maria of the Astral Clocktower.",
      "Εάν ο παίκτης κάνει χειρονομίες (emotes) μπροστά στην Κούκλα, εκείνη αντιδρά υποκλινόμενη ή χειροκροτώντας χαριτωμένα."
    ],
    "source": "https://el.wikipedia.org/wiki/Bloodborne",
    "locale": "el-GR",
    "tags": ["bloodborne", "plain-doll", "fromsoftware", "playstation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_098",
    "text": "Ποια θρυλική γυναίκα στρατιώτης και μέντορας του Naked Snake θεωρείται η 'Μητέρα των Ειδικών Δυνάμεων' στο «Metal Gear Solid 3: Snake Eater»;",
    "answers": ["EVA", "The Boss (Voyevoda)", "Sniper Wolf", "Quiet"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η The Boss ηγήθηκε της μονάδας Cobra Unit στον Β΄ Παγκόσμιο Πόλεμο και θυσίασε τη ζωή και την υστεροφημία της για χάρη της πατρίδας της.",
    "funFacts": [
      "Η τελική μονομαχία ανάμεσα στον Snake και την The Boss διεξάγεται μέσα σε ένα απέραντο λιβάδι με λευκά κρίνα, τα οποία βάφονται κόκκινα από αίμα.",
      "Ο Snake αναγκάζεται να πατήσει ο ίδιος το κουμπί για να πυροβολήσει τη μέντορά του, κερδίζοντας τον τίτλο του 'Big Boss'."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Boss_(Metal_Gear)",
    "locale": "el-GR",
    "tags": ["metal-gear", "the-boss", "snake-eater", "kojima"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_099",
    "text": "Ποιος λοχαγός του αμερικανικού στρατού ίδρυσε την Αδελφότητα του Ατσαλιού (Brotherhood of Steel) στην Καλιφόρνια αμέσως μετά τον Μεγάλο Πόλεμο στο «Fallout»;",
    "answers": ["Arthur Maxson", "John Henry Eden", "Roger Maxson", "Robert House"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο λοχαγός Roger Maxson αποστάτησε από τον αμερικανικό στρατό όταν ανακάλυψε τα απάνθρωπα πειράματα με τον ιό FEV στη βάση Mariposa, ιδρύοντας την Αδελφότητα.",
    "funFacts": [
      "Οδήγησε τους επιζώντες στρατιώτες και τις οικογένειές τους μέσα από τη ραδιενεργή ερημιά στο καταφύγιο Lost Hills, σε ένα ιστορικό γεγονός γνωστό ως 'Η Έξοδος'.",
      "Όλοι οι μετέπειτα ηγέτες της Αδελφότητας (συμπεριλαμβανομένου του Arthur Maxson στο Fallout 4) είναι απόγονοι της δυναστείας των Maxson."
    ],
    "source": "https://en.wikipedia.org/wiki/Brotherhood_of_Steel",
    "locale": "el-GR",
    "tags": ["fallout", "roger-maxson", "brotherhood-of-steel", "lore"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_100",
    "text": "Κάτω από ποιο ιστορικό κτίριο της πόλης Tristram βρίσκονται οι κατακόμβες που οδηγούν στον Άρχοντα του Τρόμου στο αρχικό «Diablo» (1997);",
    "answers": ["Κάτω από το Δημαρχείο", "Κάτω από το πανδοχείο Tavern", "Κάτω από το νεκροταφείο", "Κάτω από τον Καθεδρικό Ναό (Tristram Cathedral)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο ερειπωμένος καθεδρικός ναός του Tristram κρύβει κάτω από τα θεμέλιά του 16 επίπεδα μπουντρουμιών που καταλήγουν στην ίδια την Κόλαση.",
    "funFacts": [
      "Ο αρχιεπίσκοπος Lazarus ξεγέλασε τον βασιλιά Leoric και απήγαγε τον νεαρό πρίγκιπα Albrecht για να τον κάνει ξενιστή του Diablo στα βάθη του ναού.",
      "Στο τέλος του παιχνιδιού, ο ήρωας καρφώνει τη μαγική ψυχόπετρα (Soulstone) του Diablo στο ίδιο του το μέτωπο προσπαθώντας μάταια να τον φυλακίσει."
    ],
    "source": "https://el.wikipedia.org/wiki/Diablo_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["diablo", "tristram", "cathedral", "blizzard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_101",
    "text": "Ποια τερατώδης βιομηχανική υπερ-νοημοσύνη σε γυάλινη γυάλα είναι το τελικό αφεντικό στον πλανήτη Zebes στο «Super Metroid» (1994);",
    "answers": ["Mother Brain", "Ridley", "Kraid", "Krang"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Mother Brain κατασκευάστηκε αρχικά από τους Chozo αλλά συμμάχησε με τους Space Pirates για να αναπαράγει τα Metroids ως βιολογικά όπλα.",
    "funFacts": [
      "Στην τελική μάχη, το μωρό Metroid (Baby Metroid) θυσιάζει τη ζωή του προστατεύοντας τη Samus και της χαρίζει το πανίσχυρο Hyper Beam.",
      "Η Mother Brain εμφανίζεται επίσης ως επαναλαμβανόμενος κεντρικός κακός στη σειρά κινουμένων σχεδίων 'Captain N: The Game Master'."
    ],
    "source": "https://en.wikipedia.org/wiki/Mother_Brain",
    "locale": "el-GR",
    "tags": ["metroid", "mother-brain", "snes", "nintendo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_102",
    "text": "Ποια εκκεντρικά δίδυμα αδέλφια της δυναστείας Ashford διοικούν τη βάση στο νησί Rockfort στο «Resident Evil - Code: Veronica»;",
    "answers": ["Albert & Alex Wesker", "Alfred και Alexia Ashford", "William & Annette Birkin", "James & Mary Sunderland"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Alfred Ashford πάσχει από διαταραχή ταυτότητας υποδυόμενος την αδελφή του Alexia, η οποία βρισκόταν σε κρυογενικό ύπνο για 15 χρόνια για να συγχωνευτεί με τον ιό T-Veronica.",
    "funFacts": [
      "Η Alexia Ashford δημιούργησε τον ιό T-Veronica συνδυάζοντας τον ιό Progenitor με γονίδια αρχαίων μυρμηγκιών σε ηλικία μόλις 12 ετών.",
      "Το παιχνίδι ήταν ο πρώτος τίτλος της βασικής σειράς Resident Evil που χρησιμοποίησε εξ ολοκλήρου πραγματικά τρισδιάστατα περιβάλλοντα (στο Sega Dreamcast)."
    ],
    "source": "https://en.wikipedia.org/wiki/Resident_Evil_%E2%80%93_Code:_Veronica",
    "locale": "el-GR",
    "tags": ["resident-evil", "code-veronica", "ashford", "capcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_103",
    "text": "Ποια είναι η πασίγνωστη κυνική ατάκα του κυβερνητικά ενισχυμένου Adam Jensen στο cyberpunk RPG «Deus Ex: Human Revolution» (2011);",
    "answers": ["«Stay awhile and listen»", "«War never changes»", "«I never asked for this»", "«Wake up, Samurai»"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Adam Jensen αναγκάζεται να δεχτεί εκτεταμένες μηχανικές επεμβάσεις στο σώμα του μετά από μια δολοφονική επίθεση, σχολιάζοντας κυνικά: 'I never asked for this'.",
    "funFacts": [
      "Η ατάκα αυτή έγινε άμεσα viral meme σε ολόκληρη την gaming κοινότητα, χρησιμοποιούμενη σε χιλιάδες παρωδίες.",
      "Τη χαρακτηριστική βαθιά και βραχνή φωνή του Adam Jensen χάρισε ο Καναδός ηθοποιός Elias Toufexis."
    ],
    "source": "https://en.wikipedia.org/wiki/Deus_Ex:_Human_Revolution",
    "locale": "el-GR",
    "tags": ["deus-ex", "adam-jensen", "square-enix", "cyberpunk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_104",
    "text": "Ποιος Νοτιοκορεάτης παίκτης (Lee Sang-hyeok) θεωρείται ο σπουδαιότερος όλων των εποχών στο League of Legends με το παρατσούκλι 'The Unkillable Demon King';",
    "answers": ["Caps", "ShowMaker", "Ruler", "Faker"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Faker αγωνίζεται ως mid laner για την ομάδα T1 (πρώην SK Telecom T1) και είναι ο μοναδικός παίκτης στην ιστορία που έχει κατακτήσει τέσσερα παγκόσμια πρωταθλήματα Worlds.",
    "funFacts": [
      "Το 2024 έγινε το πρώτο μέλος που εισήχθη στο νεοσύστατο Hall of Legends του League of Legends από τη Riot Games.",
      "Η διάσημη φράση 'Look at the cleanse, look at the moves, Faker what was that?!' από τον εκφωνητή DoA το 2013 είναι το πιο εμβληματικό shoutcast στην ιστορία των esports."
    ],
    "source": "https://en.wikipedia.org/wiki/Faker_(video_game_player)",
    "locale": "el-GR",
    "tags": ["league-of-legends", "faker", "esports", "t1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_105",
    "text": "Πώς ονομάζεται το ορεινό οχυρό της Σχολής του Λύκου όπου εκπαιδεύτηκε ο Geralt of Rivia και διαδραματίζεται η εισαγωγή του «The Witcher 3»;",
    "answers": ["Kaer Morhen", "Vizima", "Oxenfurt", "Novigrad"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Kaer Morhen (από την αρχαία γλώσσα: 'Caer a'Muirehen', δηλαδή 'Οχυρό της Παλιάς Θάλασσας') είναι το απομονωμένο καταφύγιο των Witchers στα βουνά του Kaedwen.",
    "funFacts": [
      "Εδώ υποβάλλονταν οι νεαροί υποψήφιοι στην επίπονη και επικίνδυνη 'Δοκιμασία των Χορτών' (Trial of the Grasses), στην οποία επιβίωνε μόλις 3 στα 10 παιδιά.",
      "Στο The Witcher 3, το οχυρό δέχεται πολιορκία από τον στρατό της Άγριας Κυνηγεσίας σε μία από τις πιο κρίσιμες μάχες της ιστορίας."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
    "locale": "el-GR",
    "tags": ["witcher", "kaer-morhen", "geralt", "cd-projekt-red"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_106",
    "text": "Ποιο μυθικό μεταλλικό στοιχείο χαρίζει στους Αυστραλούς υπεράνθρωπη δύναμη, μουστάκια και ευφυΐα στο σύμπαν του «Team Fortress 2»;",
    "answers": ["Adamantium", "Australium", "Vibranium", "Unobtainium"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το Australium είναι ένα σπάνιο χρυσαφένιο μέταλλο που μεταμορφώνει όποιον εκτεθεί σε αυτό σε ιδιοφυΐα με τεράστια σωματική δύναμη, κάνοντας την Αυστραλία υπερδύναμη.",
    "funFacts": [
      "Στο παιχνίδι, τα όπλα 'Australium' είναι εξαιρετικά σπάνιες χρυσές παραλλαγές που αποκτώνται από το mode Mann vs. Machine και έχουν τεράστια εμπορική αξία στο Steam Marketplace.",
      "Η διαμάχη για τα τελευταία αποθέματα Australium αποτελεί το βασικό κίνητρο πίσω από τον πόλεμο των αδελφών Mann στα επίσημα κόμικς της Valve."
    ],
    "source": "https://en.wikipedia.org/wiki/Team_Fortress_2",
    "locale": "el-GR",
    "tags": ["team-fortress-2", "australium", "valve", "lore"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_107",
    "text": "Ποιο ήταν το ιστορικό παγκόσμιο διαφημιστικό σλόγκαν της Microsoft για την κυκλοφορία του «Halo 3» στο Xbox 360 το 2007;",
    "answers": ["«Believe in Heroes»", "«Jump In»", "«Finish the Fight»", "«Fight for the Future»"],
    "correctAnswerIndex": 2,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Το σλόγκαν 'Finish the Fight' υποσχέθηκε στους παίκτες την οριστική κορύφωση και το φινάλε του πολέμου ανάμεσα στην ανθρωπότητα, τους Covenant και το Flood.",
    "funFacts": [
      "Το Halo 3 απέφερε 170 εκατομμύρια δολάρια μέσα στις πρώτες 24 ώρες κυκλοφορίας του στις ΗΠΑ, ξεπερνώντας κάθε προηγούμενο ρεκόρ της βιομηχανίας ψυχαγωγίας.",
      "Η διάσημη διαφημιστική καμπάνια 'Believe' παρουσίασε ένα τεράστιο, απίστευτα λεπτομερές διοράμα μάχης με μινιατούρες στρατιωτών."
    ],
    "source": "https://el.wikipedia.org/wiki/Halo_3",
    "locale": "el-GR",
    "tags": ["halo-3", "master-chief", "bungie", "xbox-360"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_108",
    "text": "Ποιος μυστηριώδης εξωγήινος διπλός ελικοειδής μονόλιθος εκπέμπει σήματα που προκαλούν παράνοια και δημιουργούν τα Necromorphs στο «Dead Space»;",
    "answers": ["The Monolith", "The Obelisk", "The Relic", "The Marker (Ο Δείκτης)"],
    "correctAnswerIndex": 3,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Ο Black Marker (και οι τεχνητοί Red Markers) αναμεταδίδουν ένα ηλεκτρομαγνητικό σήμα που αναδιοργανώνει τον νεκρό βιολογικό ιστό σε τερατώδη πλάσματα.",
    "funFacts": [
      "Η θρησκευτική αίρεση της 'Εκκλησίας της Ενωτισμού' (Unitology) λατρεύει τους Markers ως θεϊκά εργαλεία για τη μεταθανάτια ένωση όλης της ανθρωπότητας (Convergence).",
      "Εάν πάρετε το πρώτο γράμμα από κάθε ένα από τα 12 κεφάλαια του αρχικού Dead Space, σχηματίζεται η κρυφή φράση-ανατροπή: 'N-I-C-O-L-E-I-S-D-E-A-D'."
    ],
    "source": "https://el.wikipedia.org/wiki/Dead_Space_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["dead-space", "the-marker", "visceral-games", "lore"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_109",
    "text": "Πώς ονομάζονται τα τρομακτικά ψυχικά πλάσματα με πλοκάμια χταποδιού στο πρόσωπο που εμφυτεύουν προνύμφες στα κεφάλια των θυμάτων τους στο «Baldur's Gate 3»;",
    "answers": ["Illithids (Mind Flayers)", "Beholders", "Githyanki", "Drow"],
    "correctAnswerIndex": 0,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Οι Mind Flayers (Illithids) είναι αρχαία όντα που τρέφονται με ανθρώπινους εγκεφάλους και αναπαράγονται μέσω της 'κεραμορφοποίησης' (ceremorphosis), μετατρέποντας τον ξενιστή σε όμοιό τους.",
    "funFacts": [
      "Ο πρωταγωνιστής και οι σύντροφοί του στο Baldur's Gate 3 ξεκινούν την περιπέτεια μολυσμένοι με προνύμφες Mind Flayer, αλλά προστατεύονται μυστηριωδώς από την άμεση μεταμόρφωση.",
      "Οι Githyanki, υπό την ηγεσία της βασίλισσας Vlaakith, έχουν ορκιστεί αιώνιο πόλεμο για την εξόντωση κάθε Mind Flayer στο πολυσύμπαν."
    ],
    "source": "https://el.wikipedia.org/wiki/Baldur%27s_Gate_3",
    "locale": "el-GR",
    "tags": ["baldurs-gate-3", "mind-flayers", "illithid", "larian-studios"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "gaming_med_110",
    "text": "Ποιο ήταν το πραγματικό όνομα και η μυθική καταγωγή της συζύγου του Κράτου και μητέρας του Ατρέα στο «God of War» (2018);",
    "answers": ["Angrboda", "Laufey the Just (Γιγάντισσα Γιότουν)", "Skadi", "Sif"],
    "correctAnswerIndex": 1,
    "categoryId": "gaming",
    "difficulty": 3,
    "explanation": "Η Faye ήταν στην πραγματικότητα η Laufey, η τελευταία φύλακας των Γιγάντων στο Jötunheim, η οποία είχε προβλέψει ολόκληρο το ταξίδι του Κράτου και του Ατρέα μέσα από προφητείες στους τοίχους.",
    "funFacts": [
      "Ο Κράτος αγνοούσε εντελώς την πραγματική της ταυτότητα καθ' όλη τη διάρκεια του γάμου τους, γνωρίζοντάς την απλώς ως μια εξαιρετικά ικανή θνητή τοξότρια.",
      "Το τσεκούρι Leviathan ανήκε αρχικά στη Faye, η οποία το εμπιστεύτηκε στον Κράτο πριν πεθάνει ζητώντας να σκορπίσουν τις στάχτες της στην ψηλότερη κορυφή."
    ],
    "source": "https://el.wikipedia.org/wiki/God_of_War_(2018)",
    "locale": "el-GR",
    "tags": ["god-of-war", "faye", "kratos", "atreus"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('gaming', 'medium', 3, questions)

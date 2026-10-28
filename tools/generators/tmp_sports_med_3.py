# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "sports_med_111",
    "text": "Σε ποια χρονιά κατέκτησε η Ισπανία το πρώτο Παγκόσμιο Κύπελλο Ποδοσφαίρου της ιστορίας της στα γήπεδα της Νότιας Αφρικής;",
    "answers": ["Το 2010", "Το 2006", "Το 2008", "Το 2012"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Ισπανία κατέκτησε το Μουντιάλ του 2010 νικώντας στον τελικό του Γιοχάνεσμπουργκ την Ολλανδία με 1-0 στην παράταση.",
    "funFacts": [
      "Ολοκλήρωσε έναν ιστορικό κύκλο κατακτήσεων κερδίζοντας διαδοχικά το Euro 2008, το Μουντιάλ 2010 και το Euro 2012.",
      "Ο Ίκερ Κασίγιας αναδείχθηκε κορυφαίος τερματοφύλακας της διοργάνωσης δεχόμενος μόλις δύο γκολ σε όλο το τουρνουά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%B3%CE%BA%CF%8C%CF%83%CE%BC%CE%B9%CE%BF_%CE%9A%CF%8D%CF%80%CE%B5%CE%BB%CE%BB%CE%BF_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_2010",
    "locale": "el-GR",
    "tags": ["spain-2010", "world-cup", "football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_112",
    "text": "Ποιος θρυλικός πλέι μέικερ των Utah Jazz κατέχει τα απόλυτα ρεκόρ όλων των εποχών στο NBA σε ασίστ (15.806) και κλεψίματα (3.265);",
    "answers": ["Μάτζικ Τζόνσον", "Τζον Στόκτον", "Στιβ Νας", "Τζέισον Κιντ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο John Stockton αγωνίστηκε 19 σεζόν στους Jazz συνθέτοντας με τον Karl Malone το πιο διάσημο δίδυμο pick-and-roll στην ιστορία του μπάσκετ.",
    "funFacts": [
      "Το ρεκόρ των 15.806 ασίστ θεωρείται ένα από τα πιο ασφαλή ρεκόρ στον αμερικανικό επαγγελματικό αθλητισμό, απέχοντας πάνω από 3.000 ασίστ από τον δεύτερο.",
      "Έχασε μόλις 22 αγώνες σε όλη την 19ετή καριέρα του, αγωνιζόμενος και στα 82 παιχνίδια της κανονικής περιόδου σε 17 διαφορετικές σεζόν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%A3%CF%84%CF%8C%CE%BA%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["john-stockton", "nba-records", "assists", "steals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_113",
    "text": "Ποιος Αιθίοπας δρομέας αντοχής κατέκτησε δύο συνεχόμενα χρυσά ολυμπιακά στα 10.000μ (1996, 2000) και κατέρριψε 27 παγκόσμια ρεκόρ στην καριέρα του;",
    "answers": ["Κενενίσα Μπεκέλε", "Ελιούντ Κιπτσόγκε", "Χαϊλέ Γκεμπρεσελασιέ", "Αμπέμπε Μπικίλα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Haile Gebrselassie κυριάρχησε στις μεγάλες αποστάσεις στις πίστες και αργότερα στους μαραθωνίους, σπάζοντας επανειλημμένα τα παγκόσμια ρεκόρ.",
    "funFacts": [
      "Ως παιδί έτρεχε καθημερινά 10 χιλιόμετρα για να πάει στο σχολείο κρατώντας τα βιβλία του, κάτι που επηρέασε μόνιμα τη χαρακτηριστική κλίση του αριστερού του χεριού.",
      "Έγινε ο πρώτος άνθρωπος που έτρεξε τον Μαραθώνιο σε χρόνο κάτω από 2 ώρες και 4 λεπτά (Βερολίνο, 2008)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B1%CF%8A%CE%BB%CE%AD_%CE%93%CE%BA%CE%B5%CE%BC%CF%80%CF%81%CE%B5%CF%83%CE%B5%CE%BB%CE%B1%CF%83%CE%B9%CE%AD",
    "locale": "el-GR",
    "tags": ["gebrselassie", "athletics", "distance-running", "marathon"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_114",
    "text": "Ποιος εκκεντρικός Ρουμάνος τενίστας ('Nasty') κατέκτησε το Roland Garros το 1973 και υπήρξε ο πρώτος επίσημος Νο. 1 στην ιστορία της κατάταξης ATP;",
    "answers": ["Ιόν Τσιριάκ", "Γκιγιέρμο Βίλας", "Αντριάνο Πανάτα", "Ίλιε Ναστάσε"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ilie Năstase ήταν ο πρώτος παίκτης που ανέβηκε στην κορυφή όταν δημιουργήθηκε η ηλεκτρονική παγκόσμια κατάταξη ATP τον Αύγουστο του 1973.",
    "funFacts": [
      "Ήταν εξίσου διάσημος για το απαράμιλλο ταλέντο του όσο και για τα θεατρικά ξεσπάσματα και τις διαμαρτυρίες του προς τους διαιτητές.",
      "Κέρδισε πάνω από 100 επαγγελματικούς τίτλους σε μονό και διπλό κατά τη διάρκεια της καριέρας του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%8A%CE%BB%CE%B9%CE%B5_%CE%9D%CE%B1%CF%83%CF%84%CE%AC%CF%83%CE%B5",
    "locale": "el-GR",
    "tags": ["nastase", "atp-rankings", "tennis-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_115",
    "text": "Με ποια ομάδα κατέκτησε ο Μίχαελ Σουμάχερ τα δύο πρώτα παγκόσμια πρωταθλήματα Formula 1 της καριέρας του το 1994 και το 1995;",
    "answers": ["Benetton", "Jordan", "Ferrari", "Mercedes"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Schumacher κατέκτησε τους δύο πρώτους του τίτλους με την Benetton-Ford και Benetton-Renault υπό την τεχνική ηγεσία του Ross Brawn.",
    "funFacts": [
      "Ο τίτλος του 1994 κρίθηκε στον τελευταίο αγώνα στην Αδελαΐδα της Αυστραλίας μετά από αμφιλεγόμενη σύγκρουση με τον Damon Hill.",
      "Το 1996 μετακόμισε στη Ferrari, η οποία δεν είχε κερδίσει πρωτάθλημα οδηγών από το 1979."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%AD%CE%BD%CE%B5%CF%84%CE%BF%CE%BD_%CE%A6%CF%8C%CF%81%CE%BC%CE%BF%CF%85%CE%BB%CE%B1_1",
    "locale": "el-GR",
    "tags": ["schumacher", "benetton", "f1-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_116",
    "text": "Ποια ιταλική ομάδα δημιούργησε τη θρυλική 'Grande Inter' τη δεκαετία του '60 κατακτώντας δύο διαδοχικά Κύπελλα Πρωταθλητριών υπό τον Ελένιο Ερέρα;",
    "answers": ["Μίλαν", "Ίντερ", "Γιουβέντους", "Ρόμα"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Inter Milan κυριάρχησε στην Ευρώπη το 1964 (νικώντας τη Ρεάλ 3-1) και το 1965 (νικώντας την Μπενφίκα 1-0) τελειοποιώντας το σύστημα 'κατενάτσιο' (catenaccio).",
    "funFacts": [
      "Ηγέτης της άμυνας εκείνης της ομάδας ήταν ο θρυλικός αριστερός μπακ Τζατσίντο Φακέτι, ένας από τους πρώτους επιθετικογενείς ακραίους αμυντικούς.",
      "Ο Helenio Herrera εφάρμοσε πρωτοποριακές μεθόδους ψυχολογικής προετοιμασίας και αυστηρής διατροφής στους ποδοσφαιριστές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%9A_%CE%84%CE%99%CE%BD%CF%84%CE%B5%CF%81_%CE%9C%CE%B9%CE%BB%CE%AC%CE%BD%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["inter", "catenaccio", "champions-league-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_117",
    "text": "Σε ποιους Ολυμπιακούς Αγώνες κατέκτησε ο Μάικλ Φελπς 8 χρυσά μετάλλια καταρρίπτοντας το ιστορικό ρεκόρ του Μαρκ Σπιτς;",
    "answers": ["Στην Αθήνα το 2004", "Στο Λονδίνο το 2012", "Στο Πεκίνο το 2008", "Στο Ρίο το 2016"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο Πεκίνο το 2008, ο Phelps κέρδισε 8 χρυσά μετάλλια σε 8 αγωνίσματα σημειώνοντας 7 παγκόσμια και 1 ολυμπιακό ρεκόρ.",
    "funFacts": [
      "Στα 100μ πεταλούδα νίκησε τον Σέρβο Μίλοραντ Τσάβιτς με διαφορά μόλις ενός εκατοστού του δευτερολέπτου (0,01 δευτ.).",
      "Στη σκυταλοδρομία 4x100μ ελεύθερο, η εκπληκτική τελευταία διαδρομή του Jason Lezak έσωσε το χρυσό μετάλλιο προσπερνώντας τη Γαλλία στα τελευταία μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%B9%CE%BA%CE%BB_%CE%A6%CE%B5%CE%BB%CF%80%CF%82",
    "locale": "el-GR",
    "tags": ["phelps-beijing", "beijing-2008", "swimming-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_118",
    "text": "Σε ποια ιταλική πόλη κατέκτησε ο Παναθηναϊκός την EuroLeague το 2002 νικώντας στον τελικό την πανίσχυρη οικοδέσποινα Κίντερ Μπολόνια;",
    "answers": ["Στο Μιλάνο", "Στη Ρώμη", "Στο Τρεβίζο", "Στην Μπολόνια"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο Final Four του PalaMalaguti στην Μπολόνια, ο Παναθηναϊκός επικράτησε της Κίντερ του Μανού Τζινόμπιλι και του Έτορε Μεσίνα με 89-83.",
    "funFacts": [
      "Ο Ντέγιαν Μποντιρόγκα πραγματοποίησε ηγετική εμφάνιση με 21 πόντους και αναδείχθηκε MVP του Final Four.",
      "Ο Λάζαρος Παπαδόπουλος έκανε το παιχνίδι της ζωής του απέναντι στους ψηλούς της ιταλικής ομάδας σημειώνοντας 12 πόντους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%BD%CE%B1%CE%B8%CE%B7%CE%BD%CE%B1%CF%8A%CE%BA%CF%8C%CF%82_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["panathinaikos-2002", "bologna-2002", "euroleague"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_119",
    "text": "Ποιο αγώνισμα του αλπικού σκι χαρακτηρίζεται από τις πιο στενά τοποθετημένες πόρτες (πόλους) απαιτώντας τις ταχύτερες εναλλαγές στροφών;",
    "answers": ["Σλάλομ (Slalom)", "Ελεύθερη κατάβαση (Downhill)", "Γιγαντιαίο σλάλομ", "Super-G"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το σλάλομ είναι το πιο τεχνικό αγώνισμα του σκι, με τις πόρτες να απέχουν μόλις 6 έως 13 μέτρα μεταξύ τους.",
    "funFacts": [
      "Οι χιονοδρόμοι φορούν ειδικές ενισχυμένες επικαλαμίδες και προστατευτικά χεριών για να χτυπούν τους εύκαμπτους πόλους κατευθείαν (τεχνική cross-blocking).",
      "Ο τελικός χρόνος προκύπτει από το άθροισμα δύο διαφορετικών καταβάσεων στην ίδια πλαγιά την ίδια ημέρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CF%80%CE%B9%CE%BA%CF%8C_%CF%83%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["slalom", "alpine-skiing", "winter-sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_120",
    "text": "Σε ποια χρονιά έλαβε χώρα ο ιστορικός αγώνας πυγμαχίας 'Rumble in the Jungle' στην Κινσάσα του Ζαΐρ ανάμεσα στον Μοχάμεντ Άλι και τον Τζορτζ Φόρμαν;",
    "answers": ["Το 1971", "Το 1974", "Το 1976", "Το 1978"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 30 Οκτωβρίου 1974, ο Ali εφάρμοσε την τακτική 'rope-a-dope' εξαντλώντας τον Foreman και βγάζοντάς τον νοκ-άουτ στον 8ο γύρο.",
    "funFacts": [
      "Ο αγώνας διοργανώθηκε από τον εκκεντρικό προαγωγό Don King με χρηματοδότηση του δικτάτορα του Ζαΐρ Μομπούτου Σέσε Σέκο.",
      "Πριν από τον αγώνα διοργανώθηκε ένα τεράστιο τριήμερο μουσικό φεστιβάλ με τη συμμετοχή του James Brown και του B.B. King."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CF%87%CE%AC%CE%BC%CE%B5%CE%BD%CF%84_%CE%86%CE%BB%CE%B9",
    "locale": "el-GR",
    "tags": ["rumble-in-the-jungle", "ali-foreman", "boxing-1974"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_121",
    "text": "Ποιος Βρετανός νευρολόγος και αθλητής έγινε το 1954 ο πρώτος άνθρωπος στην ιστορία που έτρεξε το ένα μίλι σε λιγότερο από 4 λεπτά;",
    "answers": ["Σεμπάστιαν Κόου", "Στιβ Οβέτ", "Ρότζερ Μπάνιστερ", "Κρις Τσάταγουεϊ"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 6 Μαΐου 1954 στην Οξφόρδη, ο Roger Bannister κάλυψε το ένα μίλι σε 3 λεπτά και 59,4 δευτερόλεπτα καταρρίπτοντας ένα όριο που θεωρούνταν σωματικά αδύνατο.",
    "funFacts": [
      "Το ιστορικό του ρεκόρ κράτησε μόλις 46 ημέρες, καθώς ο Αυστραλός John Landy το κατέρριψε στο Τούρκου με 3:57.9.",
      "Ο Bannister συνδύασε την προπόνησή του με πλήρεις σπουδές ιατρικής στο νοσοκομείο St Mary's του Λονδίνου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%8C%CF%84%CE%B6%CE%B5%CF%81_%CE%9C%CF%80%CE%AC%CE%BD%CE%B9%CF%83%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["bannister", "four-minute-mile", "athletics-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_122",
    "text": "Σε ποιους Ολυμπιακούς Αγώνες εντάχθηκε για πρώτη φορά επίσημα η πετοσφαίριση (βόλεϊ) στο ολυμπιακό πρόγραμμα;",
    "answers": ["Στη Ρώμη το 1960", "Στο Ελσίνκι το 1952", "Στη Μελβούρνη το 1956", "Στο Τόκιο το 1964"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το βόλεϊ έκανε το ολυμπιακό του ντεμπούτο στους Αγώνες του Τόκιο το 1964 τόσο στους άνδρες (χρυσό η Σοβιετική Ένωση) όσο και στις γυναίκες (χρυσό η Ιαπωνία).",
    "funFacts": [
      "Η ιαπωνική ομάδα γυναικών αποκλήθηκε 'Οι Μάγισσες της Ανατολής' (Oriental Witches) χάρη στην ασύλληπτη προπόνηση και αμυντική τους αυτοθυσία.",
      "Το μπιτς βόλεϊ εντάχθηκε ως επίσημο άθλημα πολύ αργότερα, στους Ολυμπιακούς της Ατλάντα το 1996."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CF%83%CF%84%CE%BF%CF%85%CF%82_%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CF%8D%CF%82_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CF%8D%CF%82_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["volleyball-olympics", "tokyo-1964", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_123",
    "text": "Ποιος Ιταλός ποδηλάτης αποκλήθηκε 'Il Campionissimo' (Ο Πρωταθλητής των Πρωταθλητών) κερδίζοντας 5 Γύρους Ιταλίας και 2 Γύρους Γαλλίας στις δεκαετίες του '40 και '50;",
    "answers": ["Φαούστο Κόπι (Fausto Coppi)", "Τζίνο Μπάρταλι", "Φελίτσε Τζιμόντι", "Βιντσέντζο Νίμπαλι"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Fausto Coppi υπήρξε εθνικός ήρωας στην Ιταλία και ο πρώτος ποδηλάτης στην ιστορία που πέτυχε το νταμπλ Giro-Tour την ίδια χρονιά (1949 και 1952).",
    "funFacts": [
      "Η αντιπαλότητά του με τον ευσεβή καθολικό Gino Bartali δίχασε την Ιταλία σε δύο πολιτικά και κοινωνικά στρατόπεδα.",
      "Πέθανε τραγικά το 1960 σε ηλικία μόλις 40 ετών από ελονοσία που κόλλησε σε ταξίδι στην Άνω Βόλτα (Μπουρκίνα Φάσο)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B1%CE%BF%CF%8D%CF%83%CF%84%CE%BF_%CE%9A%CF%8C%CF%80%CE%B9",
    "locale": "el-GR",
    "tags": ["fausto-coppi", "giro-d-italia", "cycling-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_124",
    "text": "Ποια χώρα κατέκτησε το Παγκόσμιο Κύπελλο Ποδοσφαίρου του 1978 ως οικοδέσποινα, με πρώτο σκόρερ και πρωταγωνιστή τον Μάριο Κέμπες;",
    "answers": ["Βραζιλία", "Αργεντινή", "Ολλανδία", "Δυτική Γερμανία"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Αργεντινή του Σέζαρ Λουίς Μενότι νίκησε την Ολλανδία στον τελικό του Μπουένος Άιρες με 3-1 στην παράταση, κατακτώντας το πρώτο Μουντιάλ της ιστορίας της.",
    "funFacts": [
      "Ο Mario Kempes σημείωσε δύο γκολ στον τελικό του Estadio Monumental και κέρδισε το Χρυσό Παπούτσι της διοργάνωσης με 6 γκολ.",
      "Ο αγωνιστικός χώρος γέμισε με εκατομμύρια κομφετί (papelitos) που πέταξαν οι Αργεντινοί οπαδοί δημιουργώντας μια ανεπανάληπτη εικόνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%B3%CE%BA%CF%8C%CF%83%CE%BC%CE%B9%CE%BF_%CE%9A%CF%8D%CF%80%CE%B5%CE%BB%CE%BB%CE%BF_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_1978",
    "locale": "el-GR",
    "tags": ["argentina-1978", "mario-kempes", "world-cup"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_125",
    "text": "Ποιος πάουερ φόργουορντ/σέντερ των Σαν Αντόνιο Σπερς αποκλήθηκε 'The Big Fundamental' και κατέκτησε 5 πρωταθλήματα NBA υπό τις οδηγίες του Γκρεγκ Πόποβιτς;",
    "answers": ["Ντέιβιντ Ρόμπινσον", "Κέβιν Γκαρνέτ", "Τιμ Ντάνκαν (Tim Duncan)", "Ντιρκ Νοβίτσκι"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Tim Duncan θεωρείται από πολλούς ως ο σπουδαιότερος πάουερ φόργουορντ στην ιστορία του NBA, διακρινόμενος για την αλάνθαστη τεχνική και την ηρεμία του.",
    "funFacts": [
      "Ξεκίνησε την αθλητική του καριέρα ως πολλά υποσχόμενος κολυμβητής στις Παρθένες Νήσους, αλλά στράφηκε στο μπάσκετ όταν ο τυφώνας Hugo κατέστρεψε τη μοναδική ολυμπιακή πισίνα του νησιού του.",
      "Κέρδισε πρωταθλήματα NBA σε τρεις διαφορετικές δεκαετίες (1999, 2003, 2005, 2007, 2014)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9%CE%BC_%CE%9D%CF%84%CE%AC%CE%BD%CE%BA%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["tim-duncan", "spurs", "nba-legends"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_126",
    "text": "Ποια θρυλική τενίστρια τσεχοσλοβακικής καταγωγής κατέκτησε 18 τίτλους Grand Slam στο μονό και το απόλυτο ρεκόρ των 9 τίτλων στο Wimbledon;",
    "answers": ["Κρις Έβερτ", "Μπίλι Τζιν Κινγκ", "Μόνικα Σέλες", "Μαρτίνα Ναβρατίλοβα"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Martina Navratilova υπήρξε η απόλυτη κυρίαρχος του γυναικείου τένις, κερδίζοντας συνολικά 59 τίτλους Grand Slam (18 μονό, 31 διπλό, 10 μεικτό).",
    "funFacts": [
      "Αυτομόλησε στις Ηνωμένες Πολιτείες το 1975 σε ηλικία 18 ετών κατά τη διάρκεια του US Open.",
      "Η αντιπαλότητά της με την Chris Evert διήρκεσε 16 χρόνια και περιλάμβανε 80 επίσημους αγώνες (43-37 υπέρ της Navratilova)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CF%84%CE%AF%CE%BD%CE%B1_%CE%9D%CE%B1%CE%B2%CF%81%CE%B1%CF%84%CE%AF%CE%BB%CE%BF%CE%B2%CE%B1",
    "locale": "el-GR",
    "tags": ["navratilova", "wimbledon-records", "tennis-legends"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_127",
    "text": "Σε ποιο αγώνισμα του στίβου κατέκτησε η Μιρέλα Μανιάνι δύο χρυσά μετάλλια σε Παγκόσμια Πρωταθλήματα (Σεβίλλη 1999, Παρίσι 2003);",
    "answers": ["Στον ακοντισμό", "Στη δισκοβολία", "Στη σφαιροβολία", "Στο άλμα εις τριπλούν"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Μιρέλα Μανιάνι υπήρξε κορυφαία ακοντίστρια παγκοσμίως, χαρίζοντας στην Ελλάδα επίσης το ασημένιο ολυμπιακό μετάλλιο στο Σίδνεϊ (2000) και το χάλκινο στην Αθήνα (2004).",
    "funFacts": [
      "Στη Σεβίλλη το 1999 σημείωσε παγκόσμιο ρεκόρ με βολή στα 67,09 μέτρα με το νέο μοντέλο ακοντίου.",
      "Το ατομικό της ρεκόρ των 67,51 μέτρων (από το 2000) παραμένει πανελλήνιο ρεκόρ στον ακοντισμό γυναικών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CF%81%CE%AD%CE%BB%CE%B1_%CE%9C%CE%B1%CE%BD%CE%B9%CE%AC%CE%BD%CE%B9",
    "locale": "el-GR",
    "tags": ["maniani", "javelin", "world-champion", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_128",
    "text": "Σε ποια χώρα της Νότιας Αμερικής βρίσκεται η διάσημη πίστα Ιντερλάγκος (Autódromo José Carlos Pace), όπου κρίθηκαν συγκλονιστικά πρωταθλήματα F1;",
    "answers": ["Στην Αργεντινή", "Στη Βραζιλία", "Στο Μεξικό", "Στη Χιλή"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η πίστα του Interlagos βρίσκεται στο Σάο Πάολο της Βραζιλίας και είναι γνωστή για την αριστερόστροφη φορά της και τις δραματικές αλλαγές καιρού.",
    "funFacts": [
      "Εκεί εξασφάλισε ο Lewis Hamilton το πρώτο του παγκόσμιο πρωτάθλημα το 2008 προσπερνώντας τον Timo Glock στην τελευταία στροφή του τελευταίου γύρου.",
      "Η πίστα μετονομάστηκε προς τιμήν του Βραζιλιάνου πιλότου της F1 José Carlos Pace που σκοτώθηκε σε αεροπορικό δυστύχημα το 1977."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BF%CF%85%CF%84%CE%BF_%CE%BD%CF%84%CF%81%CF%8C%CE%BC%CE%BF_%CE%96%CE%BF%CE%B6%CE%AD_%CE%9A%CE%AC%CF%81%CE%BB%CE%BF%CF%82_%CE%A0%CE%AC%CF%83%CE%B5",
    "locale": "el-GR",
    "tags": ["interlagos", "brazil-gp", "formula-1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_129",
    "text": "Πόσα λεπτά διαρκεί η προσωρινή ποινή αποβολής ενός παίκτη όταν του υποδειχθεί 'δίλεπτος αποκλεισμός' στο χάντμπολ;",
    "answers": ["5 λεπτά", "1 λεπτό", "2 λεπτά", "3 λεπτά"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η δίλεπτη αποβολή (2-minute suspension) υποχρεώνει τον παίκτη να καθίσει στον πάγκο για ακριβώς 2 λεπτά και η ομάδα αγωνίζεται με παίκτη λιγότερο.",
    "funFacts": [
      "Ο διαιτητής υποδεικνύει την ποινή υψώνοντας δύο δάχτυλα στον αέρα.",
      "Εάν ο ίδιος παίκτης δεχθεί τρεις δίλεπτες αποβολές στον ίδιο αγώνα, αποβάλλεται οριστικά με κόκκινη κάρτα (disqualification)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CF%81%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["handball-rules", "suspension", "two-minutes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_130",
    "text": "Ποιος θρυλικός Πορτογάλος επιθετικός ('Μαύρος Πάνθηρας') αναδείχθηκε πρώτος σκόρερ του Παγκοσμίου Κυπέλλου του 1966 στην Αγγλία με 9 γκολ;",
    "answers": ["Λουίς Φίγκο", "Κριστιάνο Ρονάλντο", "Πάουλο Φούτρε", "Εουσέμπιο (Eusébio)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Eusébio da Silva Ferreira οδήγησε την Πορτογαλία στην 3η θέση του Μουντιάλ 1966 και τη Μπενφίκα σε αναρίθμητους τίτλους κερδίζοντας τη Χρυσή Μπάλα το 1965.",
    "funFacts": [
      "Στον προημιτελικό του 1966 εναντίον της Βόρειας Κορέας, πέτυχε 4 γκολ ανατρέποντας το εις βάρος της Πορτογαλίας 0-3 σε νίκη με 5-3.",
      "Έξω από το Estádio da Luz της Μπενφίκα στη Λισαβόνα δεσπόζει ένα επιβλητικό μπρούντζινο άγαλμά του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BF%CF%85%CF%83%CE%AD%CE%B2%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["eusebio", "world-cup-1966", "portugal-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_131",
    "text": "Σε ποια χρονιά και σε ποια ασιατική πόλη κατέκτησε η Εθνική Ελλάδας υδατοσφαίρισης γυναικών το χρυσό μετάλλιο στο Παγκόσμιο Πρωτάθλημα Υγρού Στίβου;",
    "answers": ["Το 2011 στη Σαγκάη", "Το 2008 στο Πεκίνο", "Το 2015 στο Καζάν", "Το 2019 στην Γκουανγκτζού"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 29 Ιουλίου 2011 στη Σαγκάη, η Εθνική Ελλάδας πόλο γυναικών υπό τον Γιώργο Μορφέση κατέκτησε τον παγκόσμιο τίτλο νικώντας στον τελικό την Κίνα με 9-8.",
    "funFacts": [
      "Αποτελεί τον μοναδικό παγκόσμιο τίτλο σε επίπεδο ανδρών ή γυναικών στην ιστορία των ελληνικών ομαδικών ολυμπιακών αθλημάτων.",
      "Η Αλεξάνδρα Ασημάκη αναδείχθηκε κορυφαία πολίστρια στον κόσμο για το 2011 από τη FINA."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1%CF%82_(%CF%85%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B3%CF%85%CE%BD%CE%B1%CE%B9%CE%BA%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["greek-womens-waterpolo", "shanghai-2011", "world-champions"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_132",
    "text": "Ποιος Γερμανός σούπερ σταρ αγωνίστηκε και τις 21 σεζόν της καριέρας του στο NBA αποκλειστικά στους Dallas Mavericks κατακτώντας το πρωτάθλημα το 2011;",
    "answers": ["Ντέτλεφ Σρεμπφ", "Ντιρκ Νοβίτσκι", "Ντένις Σρέντερ", "Κρίστιαν Βελπ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Dirk Nowitzki έφερε επανάσταση στη θέση του πάουερ φόργουορντ με το φονικό του σουτ τριών πόντων και το χαρακτηριστικό 'one-legged fadeaway'.",
    "funFacts": [
      "Το 2007 έγινε ο πρώτος Ευρωπαίος παίκτης που κέρδισε το βραβείο MVP της κανονικής περιόδου του NBA.",
      "Είναι ο 6ος σκόρερ όλων των εποχών στην ιστορία του NBA με 31.560 πόντους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%B9%CF%81%CE%BA_%CE%9D%CE%BF%CE%B2%CE%AF%CF%84%CF%83%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["nowitzki", "dallas-mavericks", "nba-legends"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_133",
    "text": "Ποιος Αμερικανός υπεραθλητής ισοφάρισε το θρυλικό επίτευγμα του Τζέσε Όουενς κερδίζοντας 4 χρυσά μετάλλια (100μ, 200μ, 4x100μ, μήκος) στους Ολυμπιακούς του 1984;",
    "answers": ["Μάικλ Τζόνσον", "Μορίς Γκριν", "Καρλ Λιούις", "Τάισον Γκέι"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Carl Lewis κέρδισε 4 χρυσά στο Λος Άντζελες το 1984 και συνολικά 9 χρυσά ολυμπιακά μετάλλια στην καριέρα του (1984–1996).",
    "funFacts": [
      "Κέρδισε το χρυσό μετάλλιο στο άλμα εις μήκος σε 4 συνεχόμενες Ολυμπιάδες (1984, 1988, 1992, 1996), επίτευγμα που μοιράζεται μόνο με τους Al Oerter και Michael Phelps.",
      "Ανακηρύχθηκε 'Αθλητής του Αιώνα' από τη Διεθνή Ολυμπιακή Επιτροπή το 1999."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%81%CE%BB_%CE%9B%CE%B9%CE%BF%CF%8D%CE%B9%CF%82",
    "locale": "el-GR",
    "tags": ["carl-lewis", "los-angeles-1984", "olympic-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_134",
    "text": "Ποια ιαπωνική πόλη φιλοξένησε τους Χειμερινούς Ολυμπιακούς Αγώνες του 1998, όπου εντάχθηκε για πρώτη φορά το σνόουμπορντ και οι επαγγελματίες του NHL στο χόκεϊ;",
    "answers": ["Το Σαπόρο", "Το Τόκιο", "Η Οσάκα", "Το Ναγκάνο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Nagano διοργάνωσε τους 18ους Χειμερινούς Ολυμπιακούς Αγώνες το 1998, στους οποίους η Τσεχία με τον τερματοφύλακα Dominik Hašek κέρδισε το ιστορικό χρυσό στο χόκεϊ ανδρών.",
    "funFacts": [
      "Συμμετείχαν για πρώτη φορά περισσότεροι από 2.000 αθλητές σε Χειμερινή Ολυμπιάδα.",
      "Το κέρλινγκ επέστρεψε ως επίσημο άθλημα για πρώτη φορά μετά το 1924."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CE%BC%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1998",
    "locale": "el-GR",
    "tags": ["nagano-1998", "winter-olympics", "japan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_135",
    "text": "Ποιο ιστορικό αμερικανικό περιοδικό πυγμαχίας ιδρύθηκε το 1922 και αποκαλείται παγκοσμίως 'Η Βίβλος της Πυγμαχίας' (The Bible of Boxing);",
    "answers": ["The Ring", "Sports Illustrated", "KO Magazine", "Boxing News"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το περιοδικό 'The Ring' απονέμει τις δικές του αναγνωρισμένες ζώνες παγκόσμιου πρωταθλητή (The Ring championship belt) στον αδιαφιλονίκητο γραμμικό πρωταθλητή κάθε κατηγορίας.",
    "funFacts": [
      "Ιδρύθηκε από τον Nat Fleischer και διατηρεί τις πιο σεβαστές ανεξάρτητες κατατάξεις πυγμάχων pound-for-pound στον κόσμο.",
      "Απονέμει επίσης τα ετήσια βραβεία για τον 'Πυγμάχο της Χρονιάς' και τον 'Αγώνα της Χρονιάς'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%85%CE%B3%CE%BC%CE%B1%CF%87%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["the-ring", "boxing-magazine", "media"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_136",
    "text": "Ποια αγγλική επαρχιακή ομάδα κατέκτησε δύο συνεχόμενα Κύπελλα Πρωταθλητριών Ευρώπης (1979, 1980) υπό την καθοδήγηση του χαρισματικού Μπράιαν Κλαφ;",
    "answers": ["Άστον Βίλα", "Νότιγχαμ Φόρεστ", "Λιντς Γιουνάιτεντ", "Ντέρμπι Κάουντι"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Nottingham Forest πέτυχε ένα μοναδικό κατόρθωμα: ανέβηκε από τη Β' κατηγορία, κέρδισε το αγγλικό πρωτάθλημα και κατόπιν κατέκτησε δύο διαδοχικά ευρωπαϊκά τρόπαια (1979 στο Μόναχο και 1980 στη Μαδρίτη).",
    "funFacts": [
      "Είναι ο μοναδικός σύλλογος στην ιστορία του ευρωπαϊκού ποδοσφαίρου που έχει κατακτήσει περισσότερα Κύπελλα Πρωταθλητριών (2) από ό,τι εγχώρια πρωταθλήματα (1).",
      "Ο Brian Clough και ο βοηθός του Peter Taylor έμειναν στην ιστορία ως ένα από τα σπουδαιότερα προπονητικά δίδυμα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%8C%CF%84%CE%B9%CE%BD%CE%B3%CF%87%CE%B1%CE%BC_%CE%A6%CF%8C%CF%81%CE%B5%CF%83%CF%84",
    "locale": "el-GR",
    "tags": ["nottingham-forest", "brian-clough", "champions-league-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_137",
    "text": "Ποιος Ελβετός τενίστας ('Stan the Man') κατέκτησε 3 τουρνουά Grand Slam (Australian Open 2014, Roland Garros 2015, US Open 2016) στην εποχή του Big Three;",
    "answers": ["Ρότζερ Φέντερερ", "Ντόμινικ Τιμ", "Σταν Βαβρίνκα (Stan Wawrinka)", "Μαρίν Τσίλιτς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Stan Wawrinka νίκησε εν ενεργεία Νο. 1 παίκτες σε όλους τους τελικούς Grand Slam που κέρδισε (τον Nadal το 2014 και τον Djokovic το 2015 και 2016).",
    "funFacts": [
      "Είναι διάσημος για το εκρηκτικό μονοχέρι backhand του, που θεωρείται από πολλούς ως το πιο δυνατό στην ιστορία του αθλήματος.",
      "Κέρδισε επίσης το χρυσό ολυμπιακό μετάλλιο στο διπλό ανδρών στο Πεκίνο το 2008 με συμπαίκτη τον Roger Federer."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B1%CE%BD_%CE%92%CE%B1%CE%B2%CF%81%CE%AF%CE%BD%CE%BA%CE%B1",
    "locale": "el-GR",
    "tags": ["wawrinka", "grand-slam", "tennis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_138",
    "text": "Τι ιδιαίτερο σύμβολο νίκης απονέμεται στον πρωταθλητή του φημισμένου τουρνουά γκολφ Masters στην Augusta National της Τζόρτζια;",
    "answers": ["Ένα χρυσό ρολόι", "Ένα ασημένιο μπαστούνι", "Μια δερμάτινη ζώνη", "Το Πράσινο Σακάκι (Green Jacket)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Green Jacket απονέμεται από το 1949 στον νικητή του Masters και αποτελεί το πιο αναγνωρίσιμο έπαθλο στον κόσμο του γκολφ.",
    "funFacts": [
      "Παραδοσιακά, ο νικητής της προηγούμενης χρονιάς βοηθά τον νέο πρωταθλητή να φορέσει το πράσινο σακάκι στην τελετή απονομής.",
      "Ο πρωταθλητής επιτρέπεται να πάρει το σακάκι στο σπίτι του για έναν μόνο χρόνο, μετά τον οποίο παραμένει φυλαγμένο στο clubhouse της Augusta."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%BF%CE%BB%CF%86",
    "locale": "el-GR",
    "tags": ["masters", "green-jacket", "augusta", "golf"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_139",
    "text": "Σε ποια ελβετική πόλη κατέκτησε ο ΠΑΟΚ το Κύπελλο Κυπελλούχων Ευρώπης στο μπάσκετ το 1991 νικώντας τη Σαραγόσα με 76-72;",
    "answers": ["Στη Γενεύη", "Στη Ζυρίχη", "Στη Λωζάνη", "Στη Βέρνη"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 26 Μαρτίου 1991 στο Patinoire des Vernets της Γενεύης, ο ΠΑΟΚ του Ντράγκαν Σάκοτα κατέκτησε το πρώτο ευρωπαϊκό τρόπαιο της ιστορίας του.",
    "funFacts": [
      "Πρωταγωνιστές σε εκείνον τον τελικό ήταν ο Μπάνε Πρέλεβιτς (31 πόντοι) και ο Κεν Μπάρλοου (20 πόντοι).",
      "Χιλιάδες οπαδοί του ΠΑΟΚ ταξίδεψαν οδικώς και αεροπορικώς στην Ελβετία μετατρέποντας το γήπεδο σε 'Αλεξάνδρειο'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%91%CE%9F%CE%9A_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["paok-1991", "geneva", "cup-winners-cup", "greek-basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_140",
    "text": "Ποιος Γερμανός πιλότος κατέκτησε τέσσερα συνεχόμενα παγκόσμια πρωταθλήματα Formula 1 με τη Red Bull Racing από το 2010 έως το 2013;",
    "answers": ["Νίκο Ρόσμπεργκ", "Σεμπάστιαν Φέτελ", "Μίχαελ Σουμάχερ", "Νικ Χάιντφελντ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Sebastian Vettel έγινε ο νεότερος παγκόσμιος πρωταθλητής στην ιστορία της Formula 1 το 2010 σε ηλικία 23 ετών και 134 ημερών.",
    "funFacts": [
      "Το 2013 πέτυχε το απίστευτο ρεκόρ των 9 συνεχόμενων νικών σε Grand Prix σε μία σεζόν.",
      "Συνολικά σημείωσε 53 νίκες σε Grand Prix στην καριέρα του, όντας τέταρτος στη λίστα όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B5%CE%BC%CF%80%CE%AC%CF%83%CF%84%CE%B9%CE%B1%CE%BD_%CE%A6%CE%AD%CF%84%CE%B5%CE%BB",
    "locale": "el-GR",
    "tags": ["vettel", "red-bull", "formula-1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_141",
    "text": "Ποιο διάσημο στάδιο στο Μιλάνο αποτελεί κοινή έδρα της Μίλαν και της Ίντερ και φέρει επίσης το όνομα του Τζουζέπε Μεάτσα;",
    "answers": ["Ολίμπικο", "Ντέλε Άλπι", "Σαν Σίρο", "Αρτέμιο Φράνκι"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Stadio Giuseppe Meazza (ευρέως γνωστό ως San Siro) εγκαινιάστηκε το 1926 και έχει φιλοξενήσει 4 τελικούς Κυπέλλου Πρωταθλητριών / Champions League.",
    "funFacts": [
      "Όταν αγωνίζεται η Ίντερ συνηθίζεται να αποκαλείται 'Τζουζέπε Μεάτσα', προς τιμήν του θρύλου της ομάδας, ενώ οι οπαδοί της Μίλαν προτιμούν το παραδοσιακό 'Σαν Σίρο'.",
      "Έχει χωρητικότητα άνω των 75.000 θεατών και διακρίνεται για τους χαρακτηριστικούς κυλινδρικούς πύργους στις γωνίες του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AC%CE%B4%CE%B9%CE%BF_%CE%A4%CE%B6%CE%BF%CF%85%CE%B6%CE%AD%CF%80%CE%B5_%CE%9C%CE%B5%CE%AC%CF%84%CF%83%CE%B1",
    "locale": "el-GR",
    "tags": ["san-siro", "milan", "inter", "stadiums"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_142",
    "text": "Σε ποια χρονιά και σε ποια πόλη σημείωσε ο Γιουσέιν Μπολτ τα ασύλληπτα παγκόσμια ρεκόρ στα 100μ (9,58) και στα 200μ (19,19);",
    "answers": ["Το 2008 στο Πεκίνο", "Το 2012 στο Λονδίνο", "Το 2011 στο Ντέγκου", "Το 2009 στο Βερολίνο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο Παγκόσμιο Πρωτάθλημα Στίβου του Βερολίνου το 2009, ο Usain Bolt βελτίωσε τα δικά του προηγούμενα ρεκόρ από το Πεκίνο με επιδόσεις που παραμένουν ακατάρριπτες.",
    "funFacts": [
      "Στον τελικό των 100 μέτρων κατέγραψε μέση ταχύτητα 37,58 χλμ/ώρα και μέγιστη ταχύτητα 44,72 χλμ/ώρα μεταξύ του 60ού και 80ού μέτρου.",
      "Η διαφορά των 0,11 δευτερολέπτων με την οποία κατέρριψε το ρεκόρ των 100μ ήταν η μεγαλύτερη βελτίωση ρεκόρ από την εισαγωγή της ηλεκτρονικής χρονομέτρησης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%BF%CF%85%CF%83%CE%AD%CE%B9%CE%BD_%CE%9C%CF%80%CE%BF%CE%BB%CF%84",
    "locale": "el-GR",
    "tags": ["usain-bolt", "berlin-2009", "world-records", "100m"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_143",
    "text": "Πώς ονομάζεται ο ιστορικός ετήσιος κωπηλατικός αγώνας στον ποταμό Τάμεση ανάμεσα στα πανεπιστήμια της Οξφόρδης και του Κέιμπριτζ που ξεκίνησε το 1829;",
    "answers": ["The Boat Race", "Henley Regatta", "Thames Cup", "Head of the River"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το The Boat Race διεξάγεται σε διαδρομή 6,8 χιλιομέτρων (4,2 μιλίων) στον Τάμεση ανάμεσα στο Πάτνεϊ και το Μορτλέικ στο δυτικό Λονδίνο.",
    "funFacts": [
      "Τα πληρώματα των δύο πανεπιστημίων διακρίνονται από τις αποχρώσεις του μπλε: σκούρο μπλε για την Οξφόρδη και γαλάζιο (light blue) για το Κέιμπριτζ.",
      "Πάνω από 250.000 θεατές παρακολουθούν παραδοσιακά τον αγώνα ζωντανά από τις όχθες του ποταμού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CF%80%CE%B7%CE%BB%CE%B1%CF%83%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["the-boat-race", "oxford-cambridge", "rowing-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_144",
    "text": "Ποια ομάδα κατέκτησε διαδοχικά πρωταθλήματα NBA το 1994 και το 1995 υπό τις οδηγίες του Ρούντι Τομγιάνοβιτς με τη διάσημη φράση 'Don't ever underestimate the heart of a champion';",
    "answers": ["Σικάγο Μπουλς", "Χιούστον Ρόκετς", "Σαν Αντόνιο Σπερς", "Σιάτλ Σουπερσόνικς"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Οι Houston Rockets του Hakeem Olajuwon (και αργότερα του Clyde Drexler) εκμεταλλεύτηκαν την προσωρινή απόσυρση του Michael Jordan κερδίζοντας δύο τίτλους.",
    "funFacts": [
      "Το 1995 έγιναν η ομάδα με τη χαμηλότερη θέση στην κανονική περίοδο (6η θέση στη Δύση) που κατέκτησε ποτέ το πρωτάθλημα NBA.",
      "Στους Τελικούς του 1995 σκούπισαν τους Ορλάντο Μάτζικ του νεαρού Shaquille O'Neal με 4-0."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B9%CE%BF%CF%8D%CF%83%CF%84%CE%BF%CE%BD_%CE%A1%CF%8C%CE%BA%CE%B5%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["houston-rockets", "nba-champions", "olajuwon"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_145",
    "text": "Ποια ασιατική χώρα έχει κυριαρχήσει απόλυτα στην επιτραπέζια αντισφαίριση (πινγκ πονγκ) κερδίζοντας πάνω από το 90% όλων των χρυσών ολυμπιακών μεταλλίων από το 1988;",
    "answers": ["Ιαπωνία", "Νότια Κορέα", "Κίνα", "Σιγκαπούρη"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Κίνα αποτελεί την απόλυτη υπερδύναμη του πινγκ πονγκ έχοντας κερδίσει 32 από τα 37 χρυσά ολυμπιακά μετάλλια που έχουν δοθεί συνολικά μέχρι το 2024.",
    "funFacts": [
      "Το πινγκ πονγκ θεωρείται το εθνικό άθλημα της Κίνας και έπαιξε καθοριστικό ρόλο στη διπλωματία κατά τον Ψυχρό Πόλεμο ('Ping-Pong Diplomacy' το 1971).",
      "Ο Κινέζος Ma Long θεωρείται ο κορυφαίος παίκτης όλων των εποχών με 6 χρυσά ολυμπιακά μετάλλια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%84%CF%81%CE%B1%CF%80%CE%AD%CE%B6%CE%B9%CE%B1_%CE%B1%CE%BD%CF%84%CE%B9%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CF%83%CF%84%CE%BF%CF%85%CF%82_%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CF%8D%CF%82_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CF%8D%CF%82_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["china-table-tennis", "olympics", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_146",
    "text": "Ποιος Νοτιοκορεάτης επιθετικός πέτυχε το περίφημο 'Χρυσό Γκολ' στον δραματικό αγώνα των 16 του Μουντιάλ 2002 αποκλείοντας την Ιταλία;",
    "answers": ["Παρκ Τζι-σονγκ", "Σον Χιουνγκ-μιν", "Τσα Μπουμ-κουν", "Αν Γιουνγκ-χουάν (Ahn Jung-hwan)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ahn Jung-hwan σκόραρε με κεφαλιά στο 117' της παράτασης γράφοντας το τελικό 2-1 υπέρ της συνδιοργανώτριας Νότιας Κορέας.",
    "funFacts": [
      "Μετά το γκολ, ο πρόεδρος της ιταλικής Περούτζια όπου αγωνιζόταν ο Ahn ακύρωσε οργισμένος το συμβόλαιό του δηλώνοντας ότι 'δεν θα πληρώνει κάποιον που κατέστρεψε το ιταλικό ποδόσφαιρο'.",
      "Η Νότια Κορέα υπό τον Γκους Χίντινκ έφτασε μέχρι τα ημιτελικά εκείνης της διοργάνωσης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%B3%CE%BA%CF%8C%CF%83%CE%BC%CE%B9%CE%BF_%CE%9A%CF%8D%CF%80%CE%B5%CE%BB%CE%BB%CE%BF_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_2002",
    "locale": "el-GR",
    "tags": ["ahn-jung-hwan", "world-cup-2002", "golden-goal"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_147",
    "text": "Ποια είναι η μεγαλύτερη σε απόσταση κολυμβητική διαδρομή που διεξάγεται εντός πισίνας στο πρόγραμμα των Ολυμπιακών Αγώνων;",
    "answers": ["1.500 μέτρα ελεύθερο", "800 μέτρα ελεύθερο", "1.000 μέτρα ελεύθερο", "2.000 μέτρα ελεύθερο"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Τα 1.500 μέτρα ελεύθερο (30 μήκη πισίνας των 50 μέτρων) αποτελούν το κατεξοχήν αγώνισμα αντοχής στην πισίνα για άνδρες και γυναίκες.",
    "funFacts": [
      "Ο Αυστραλός Grant Hackett κυριάρχησε στα 1.500μ μένοντας αήττητος σε μεγάλες διοργανώσεις για σχεδόν μία δεκαετία.",
      "Το μεγαλύτερο ολυμπιακό αγώνισμα γενικά είναι ο μαραθώνιος κολύμβησης ανοιχτής θάλασσας (10 χιλιόμετρα)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CE%BB%CF%8D%CE%BC%CE%B2%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["1500m-freestyle", "swimming", "endurance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_148",
    "text": "Ποια Ελληνίδα αθλήτρια κατέκτησε το χρυσό ολυμπιακό μετάλλιο στα 400 μέτρα με εμπόδια στους Ολυμπιακούς Αγώνες της Αθήνας το 2004 σημειώνοντας ολυμπιακό ρεκόρ στα ημιτελικά;",
    "answers": ["Πηγή Δεβετζή", "Φανή Χαλκιά", "Χριστίνα Χαντζή", "Βούλα Πατουλίδου"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Φανή Χαλκιά συγκλόνισε το Ολυμπιακό Στάδιο της Αθήνας κερδίζοντας τον τελικό των 400μ με εμπόδια με 52,82 δευτερόλεπτα, έχοντας πετύχει ολυμπιακό ρεκόρ (52,77) στον ημιτελικό.",
    "funFacts": [
      "Πριν από το 2004 είχε αποσυρθεί προσωρινά από τον στίβο και εργαζόταν ως δημοσιογράφος πριν επιστρέψει με προπονητή τον Γιώργο Παναγιωτόπουλο.",
      "Ήταν το μοναδικό χρυσό μετάλλιο της Ελλάδας στον στίβο στους Αγώνες της Αθήνας το 2004."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B1%CE%BD%CE%AE_%CE%A7%CE%B1%CE%BB%CE%BA%CE%B9%CE%AC",
    "locale": "el-GR",
    "tags": ["fani-chalkia", "athens-2004", "400m-hurdles", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_149",
    "text": "Σε ποια κατηγορία βάρους αναδείχθηκε ο Μάικ Τάισον ο νεότερος παγκόσμιος πρωταθλητής στην ιστορία της πυγμαχίας σε ηλικία μόλις 20 ετών το 1986;",
    "answers": ["Ελαφρών βαρών", "Ημιβαρέων βαρών", "Βαρέων βαρών (Heavyweight)", "Μέσων βαρών"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 22 Νοεμβρίου 1986, ο Mike Tyson έβγαλε νοκ-άουτ τον Trevor Berbick στον δεύτερο γύρο κερδίζοντας τη ζώνη WBC βαρέων βαρών σε ηλικία 20 ετών και 145 ημερών.",
    "funFacts": [
      "Υπό την καθοδήγηση του θρυλικού προπονητή Cus D'Amato ανέπτυξε το καταστροφικό στυλ 'peek-a-boo'.",
      "Κέρδισε τους πρώτους 19 επαγγελματικούς του αγώνες με νοκ-άουτ, εκ των οποίων οι 12 στον πρώτο γύρο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%B9%CE%BA_%CE%A4%CE%AC%CE%B9%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["mike-tyson", "heavyweight-champion", "boxing-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_150",
    "text": "Ποιος Γάλλος πρωτοπόρος αεροπόρος και ήρωας του Α' Παγκοσμίου Πολέμου έδωσε το όνομά του στο φημισμένο στάδιο και τουρνουά τένις του Παρισιού;",
    "answers": ["Λουί Μπλεριό", "Αντουάν ντε Σαιντ-Εξυπερί", "Ζαν Μερμόζ", "Ρολάν Γκαρός (Roland Garros)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Roland Garros ήταν διάσημος Γάλλος αεροπόρος που πραγματοποίησε την πρώτη πτήση πάνω από τη Μεσόγειο το 1913 και δεν υπήρξε ποτέ επαγγελματίας τενίστας.",
    "funFacts": [
      "Το στάδιο ονομάστηκε προς τιμήν του το 1928 όταν κατασκευάστηκε για να φιλοξενήσει τον τελικό του Davis Cup μετά τη νίκη των Γάλλων 'Τεσσάρων Σωματοφυλάκων'.",
      "Ο Garros καταρρίφθηκε και σκοτώθηκε σε αερομαχία το 1918, μόλις πέντε εβδομάδες πριν από τη λήξη του πολέμου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CE%BB%CE%AC%CE%BD_%CE%93%CE%BA%CE%B1%CF%81%CF%8C%CF%82_(%CE%B1%CE%B5%CF%81%CE%BF%CF%80%CF%8C%CF%81%CE%BF%CF%82)",
    "locale": "el-GR",
    "tags": ["roland-garros-aviator", "tennis-history", "stadiums"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_151",
    "text": "Ποιο είναι το επίσημο ιταλικό προσωνύμιο της Εθνικής Ομάδας Ποδοσφαίρου της Ιταλίας, εμπνευσμένο από το χαρακτηριστικό γαλάζιο χρώμα των εμφανίσεών της;",
    "answers": ["Σκουάντρα Ατζούρα (Squadra Azzurra)", "Ι Ροσονέρι", "Ι Μπιανκονέρι", "Νατσιονάλε Μπλε"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η εθνική Ιταλίας ονομάζεται 'Squadra Azzurra' (Γαλάζια Ομάδα) προς τιμήν του μπλε της Σαβοΐας (Azzurro Savoia), του βασιλικού οίκου που ένωσε την Ιταλία το 1861.",
    "funFacts": [
      "Η Ιταλία έχει κατακτήσει 4 Παγκόσμια Κύπελλα (1934, 1938, 1982, 2006) και 2 Ευρωπαϊκά Πρωταθλήματα (1968, 2020).",
      "Στον πρώτο της επίσημο διεθνή αγώνα το 1910 εναντίον της Γαλλίας, η Ιταλία φόρεσε λευκές φανέλες επειδή δεν είχαν αποφασιστεί ακόμη τα επίσημα χρώματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%99%CF%84%CE%B1%CE%BB%CE%AF%CE%B1%CF%82_(%CF%80%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["squadra-azzurra", "italy-football", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_152",
    "text": "Ποιος εκρηκτικός γκαρντ ('The Answer') οδήγησε τους Philadelphia 76ers στους Τελικούς του NBA το 2001 κερδίζοντας το βραβείο MVP της χρονιάς;",
    "answers": ["Τρέισι ΜακΓκρέιντι", "Άλεν Άιβερσον (Allen Iverson)", "Βινς Κάρτερ", "Ρέι Άλεν"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Allen Iverson, με ύψος μόλις 1,83 μ., κυριάρχησε στο NBA με το crossover του και αναδείχθηκε 4 φορές πρώτος σκόρερ της λίγκας.",
    "funFacts": [
      "Στον 1ο αγώνα των Τελικών του 2001 σημείωσε 48 πόντους υποχρεώνοντας τους ανίκητους μέχρι τότε Lakers των Shaq και Kobe στη μοναδική τους ήττα στα πλέι οφ.",
      "Η διάσημη φάση όπου ευστόχησε και πέρασε επιδεικτικά πάνω από τον Tyronn Lue ('stepover') παραμένει εμβληματική στιγμή του NBA."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%B5%CE%BD_%CE%86%CE%B9%CE%B2%CE%B5%CF%81%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["iverson", "76ers", "nba-mvp-2001"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_153",
    "text": "Σε ποια χώρα διεξήχθη το 2008 το πρώτο νυχτερινό Grand Prix στην ιστορία της Formula 1 υπό το φως τεχνητών προβολέων, όπου συνέβη το σκάνδαλο 'Crashgate';",
    "answers": ["Στο Μπαχρέιν", "Στα Ηνωμένα Αραβικά Εμιράτα (Άμπου Ντάμπι)", "Στη Σιγκαπούρη", "Στη Μαλαισία"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο Grand Prix της Σιγκαπούρης το 2008 στην πίστα Marina Bay, η ομάδα της Renault διέταξε τον Nelson Piquet Jr. να τρακάρει εσκεμμένα για να ευνοήσει τον Fernando Alonso που κέρδισε τον αγώνα.",
    "funFacts": [
      "Το σκάνδαλο αποκαλύφθηκε το 2009 οδηγώντας στον πολυετή αποκλεισμό του επικεφαλής της ομάδας Flavio Briatore από τον μηχανοκίνητο αθλητισμό.",
      "Η πίστα φωτίζεται από περίπου 1.600 ειδικούς προβολείς ισχύος τετραπλάσιας από τους προβολείς ενός τυπικού ποδοσφαιρικού σταδίου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CF%81%CE%B1%CE%BD_%CE%A0%CF%81%CE%B9_%CF%84%CE%B7%CF%82_%CE%A3%CE%B9%CE%B3%CE%BA%CE%B1%CF%80%CE%BF%CF%8D%CF%81%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["singapore-gp", "crashgate", "formula-1-2008"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_154",
    "text": "Σε ποια πόλη διοργανώθηκαν οι Ολυμπιακοί Αγώνες του 1936, όπου ο Αφροαμερικανός Τζέσε Όουενς κατέκτησε 4 χρυσά μετάλλια καταρρίπτοντας τις ναζιστικές θεωρίες περί φυλετικής ανωτερότητας;",
    "answers": ["Στο Μόναχο", "Στη Νυρεμβέργη", "Στη Βιέννη", "Στο Βερολίνο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Jesse Owens κέρδισε τα 100μ, 200μ, 4x100μ και το άλμα εις μήκος στο Ολυμπιακό Στάδιο του Βερολίνου μπροστά στα μάτια του Αδόλφου Χίτλερ.",
    "funFacts": [
      "Στον τελικό του μήκους, ο Γερμανός αντίπαλός του Luz Long τον συμβούλεψε φιλικά πού να πατήσει για να αποφύγει τρίτο άκυρο άλμα στα προκριματικά.",
      "Η ταινία 'Olympia' της Leni Riefenstahl κατέγραψε τους θριάμβους του Owens με πρωτοποριακές κινηματογραφικές τεχνικές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CF%83%CE%B5_%CE%8C%CE%BF%CF%85%CE%B5%CE%BD%CF%82",
    "locale": "el-GR",
    "tags": ["jesse-owens", "berlin-1936", "olympic-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_155",
    "text": "Ποιο είναι το επίσημο ύψος των εμποδίων στο αγώνισμα των 3.000 μέτρων στιπλ (steeplechase) ανδρών στον στίβο;",
    "answers": ["91,4 εκατοστά (0,914 μ.)", "106,7 εκατοστά", "83,8 εκατοστά", "76,2 εκατοστά"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο στιπλ ανδρών τα εμπόδια έχουν ύψος 91,4 εκατοστά (3 πόδια), ενώ στις γυναίκες έχουν ύψος 76,2 εκατοστά.",
    "funFacts": [
      "Σε αντίθεση με τα ελαφριά εμπόδια των αγώνων ταχύτητας, τα εμπόδια του στιπλ είναι βαριά και ακλόνητα δοκάρια στα οποία οι αθλητές επιτρέπεται να πατήσουν πάνω τους.",
      "Το εμπόδιο πριν από τη λίμνη νερού έχει πλάτος 3,66 μέτρα και στηρίζεται σταθερά στο έδαφος."
    ],
    "source": "https://el.wikipedia.org/wiki/3.000_%CE%BC%CE%AD%CF%84%CF%81%CE%B1_%CE%BC%CE%B5_%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AC_%CE%B5%CE%BC%CF%80%CF%8C%CE%B4%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["steeplechase-hurdles", "dimensions", "athletics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_156",
    "text": "Ποιος προπονητής οδήγησε την Πόρτο (2004) και την Ίντερ (2010) στην κατάκτηση του UEFA Champions League;",
    "answers": ["Κάρλο Αντσελότι", "Ζοσέ Μουρίνιο", "Πεπ Γκουαρδιόλα", "Γιουπ Χάινκες"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο José Mourinho είναι ένας από τους ελάχιστους προπονητές στην ιστορία που κατέκτησαν το κορυφαίο ευρωπαϊκό διασυλλογικό τρόπαιο με δύο διαφορετικές ομάδες.",
    "funFacts": [
      "Με την Πόρτο νίκησε τη Μονακό με 3-0 στον τελικό του Γκελζενκίρχεν το 2004.",
      "Με την Ίντερ ολοκλήρωσε το ιστορικό Treble το 2010 νικώντας στον τελικό της Μαδρίτης την Μπάγερν Μονάχου με 2-0 χάρη σε δύο γκολ του Diego Milito."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%BF%CF%83%CE%AD_%CE%9C%CE%BF%CF%85%CF%81%CE%AF%CE%BD%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["mourinho-ucl", "porto-2004", "inter-2010"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_157",
    "text": "Σε ποια πασίγνωστη λεωφόρο του Παρισιού τερματίζει παραδοσιακά το τελευταίο ετάπ του Γύρου της Γαλλίας (Tour de France) από το 1975;",
    "answers": ["Στη Λεωφόρο της Όπερας", "Στη Λεωφόρο Φος", "Στη Λεωφόρο των Ηλυσίων Πεδίων (Champs-Élysées)", "Στη Λεωφόρο Σεν Ζερμέν"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το τελευταίο ετάπ ολοκληρώνεται με πολλαπλούς γύρους στα Ηλύσια Πεδία γύρω από την Αψίδα του Θριάμβου, όπου διεξάγεται το πιο φημισμένο μαζικό σπριντ της ποδηλασίας.",
    "funFacts": [
      "Ο Βρετανός σπρίντερ Mark Cavendish κατέχει το ρεκόρ με 4 διαδοχικές νίκες στα Ηλύσια Πεδία (2009–2012).",
      "Παραδοσιακά, ο πρωτοπόρος της γενικής κατάταξης δεν δέχεται επιθέσεις στο τελευταίο ετάπ και πίνει σαμπάνια εν κινήσει με την ομάδα του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CF%8D%CF%81%CE%BF%CF%82_%CF%84%CE%B7%CF%82_%CE%93%CE%B1%CE%BB%CE%BB%CE%AF%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["champs-elysees", "tour-de-france-finale", "cycling"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_158",
    "text": "Ποιες δύο Ελληνίδες ιστιοπλόοι κατέκτησαν το χρυσό ολυμπιακό μετάλλιο στην κατηγορία 470 στους Ολυμπιακούς Αγώνες της Αθήνας το 2004;",
    "answers": [
      "Βιργινία Κραβαριώτη και Σοφία Παπαδοπούλου",
      "Μαρία Τσουρή και Αγγελική Καραπατάκη",
      "Βούλα Κοζομπόλη και Γιούλη Λαρά",
      "Σοφία Μπεκατώρου και Αιμιλία Τσουλφά"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το δίδυμο Μπεκατώρου - Τσουλφά εξασφάλισε το χρυσό μετάλλιο στον Άγιο Κοσμά πριν καν διεξαχθεί η τελευταία ιστιοδρομία χάρη στη βαθμολογική τους υπεροχή.",
    "funFacts": [
      "Είχαν αναδειχθεί τέσσερις συνεχόμενες χρονιές Παγκόσμιες Πρωταθλήτριες στην κατηγορία 470 (2000, 2001, 2002, 2003).",
      "Η Σοφία Μπεκατώρου κατέκτησε επίσης το χάλκινο μετάλλιο στο Πεκίνο το 2008 στην καλάση Ίνγκλινγκ (Yngling)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%BF%CF%86%CE%AF%CE%B1_%CE%9C%CF%80%CE%B5%CE%BA%CE%B1%CF%84%CF%8E%CF%81%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["bekatorou-tsoulfa", "athens-2004-sailing", "olympics-gold"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_159",
    "text": "Ποια είναι η απαραίτητη διαφορά πόντων που απαιτείται για να κερδίσει μια ομάδα ένα σετ στο βόλεϊ αν το σκορ φτάσει στο 24-24;",
    "answers": ["Τουλάχιστον 2 πόντοι διαφορά", "Μόνο 1 πόντος (ξαφνικός θάνατος)", "Τουλάχιστον 3 πόντοι διαφορά", "Ο πρώτος που θα φτάσει στους 30 πόντους"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο βόλεϊ δεν υπάρχει ανώτατο όριο πόντων στο σετ. Αν το σκορ φτάσει στο 24-24 (ή 14-14 στο τάι-μπρέικ), το σετ συνεχίζεται επ' άπειρον μέχρι μία ομάδα να αποκτήσει προβάδισμα 2 πόντων.",
    "funFacts": [
      "Το μεγαλύτερο σε διάρκεια σετ στην ιστορία του επίσημου επαγγελματικού βόλεϊ έληξε με σκορ 54-52 σε αγώνα του πρωταθλήματος της Νότιας Κορέας το 2013.",
      "Σε διεθνές επίπεδο εθνικών ομάδων, το ρεκόρ κατέχει ένα σετ μεταξύ Καναδά και Αυστραλίας που έληξε 44-42."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["volleyball-rules", "deuce", "scoring"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_160",
    "text": "Ποιος Έλληνας προπονητής έγινε ο πρώτος στην ιστορία της χώρας που κατέκτησε την EuroLeague, οδηγώντας τον Ολυμπιακό στον τίτλο στο Λονδίνο το 2013;",
    "answers": ["Γιάννης Ιωαννίδης", "Γιώργος Μπαρτζώκας", "Παναγιώτης Γιαννάκης", "Δημήτρης Ιτούδης"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Γιώργος Μπαρτζώκας έγραψε ιστορία το 2013 διαδεχόμενος τον Ντούσαν Ίβκοβιτς και καθοδηγώντας τον Ολυμπιακό σε θρίαμβο επί της Ρεάλ Μαδρίτης (100-88) στον τελικό της O2 Arena.",
    "funFacts": [
      "Έχει αναδειχθεί 3 φορές Προπονητής της Χρονιάς στην EuroLeague (Alexander Gomelsky Coach of the Year) το 2013, 2022 και 2023.",
      "Έχει εργαστεί επίσης με επιτυχία στο εξωτερικό στη Λοκομοτίβ Κουμπάν, την Μπαρτσελόνα και τη Χίμκι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8E%CF%81%CE%B3%CE%BF%CF%82_%CE%9C%CF%80%CE%B1%CF%81%CF%84%CE%B6%CF%8E%CE%BA%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["bartzokas", "olympiacos-2013", "euroleague-coaches", "london-2013"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('sports', 'medium', 3, questions)

# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "sports_med_061",
    "text": "Σε ποια χρονιά πέτυχε η Λίβερπουλ τη θρυλική ανατροπή από 0-3 σε 3-3 εναντίον της Μίλαν στην Κωνσταντινούπολη κατακτώντας το Champions League;",
    "answers": ["Το 2005", "Το 2003", "Το 2007", "Το 2001"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 25 Μαΐου 2005, η Λίβερπουλ του Ράφα Μπενίτεθ ισοφάρισε τη Μίλαν σε 3-3 μέσα σε 6 λεπτά στο δεύτερο ημίχρονο και πήρε το τρόπαιο στα πέναλτι.",
    "funFacts": [
      "Ο τερματοφύλακας Γέρζι Ντούντεκ μιμήθηκε τα 'wobbly legs' του Μπρους Γκρόμπελαρ στη διαδικασία των πέναλτι αποκρούοντας το κρίσιμο πέναλτι του Σεβτσένκο.",
      "Το παιχνίδι αυτό θεωρείται ευρέως ως ο πιο δραματικός τελικός στην ιστορία των ευρωπαϊκών κυπέλλων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CE%BB%CE%B9%CE%BA%CF%8C%CF%82_%CE%9F%CE%A5%CE%95%CE%A6%CE%91_%CE%A4%CF%83%CE%AC%CE%BC%CF%80%CE%B9%CE%BF%CE%BD%CF%82_%CE%9B%CE%B9%CE%B3%CE%BA_2005",
    "locale": "el-GR",
    "tags": ["istanbul-2005", "liverpool", "milan", "champions-league"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_062",
    "text": "Ποιος Έλληνας πλέι μέικερ αναδείχθηκε MVP της EuroLeague το 2006 με την ΤΣΣΚΑ Μόσχας και κατέκτησε συνολικά δύο ευρωπαϊκά τρόπαια;",
    "answers": ["Βασίλης Σπανούλης", "Θοδωρής Παπαλουκάς", "Δημήτρης Διαμαντίδης", "Νικ Καλάθης"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Θοδωρής Παπαλουκάς ('Τσάρος') κυριάρχησε στην Ευρώπη με την ΤΣΣΚΑ Μόσχας κατακτώντας την EuroLeague το 2006 και το 2008.",
    "funFacts": [
      "Έγινε ο πρώτος παίκτης στην ιστορία που αγωνίστηκε σε 8 συνεχόμενα Final Four της EuroLeague (2003–2010).",
      "Είναι ο μοναδικός παίκτης που κέρδισε το βραβείο MVP της EuroLeague ερχόμενος μόνιμα από τον πάγκο ως έκτος παίκτης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%BF%CE%B4%CF%89%CF%81%CE%AE%CF%82_%CE%A0%CE%B1%CF%80%CE%B1%CE%BB%CE%BF%CF%85%CE%BA%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["papaloukas", "cska", "euroleague", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_063",
    "text": "Ποιος θρυλικός Φινλανδός δρομέας αντοχής ('Ιπτάμενος Φινλανδός') κατέκτησε συνολικά 9 χρυσά ολυμπιακά μετάλλια στις δεκαετίες του 1920;",
    "answers": ["Χάνες Κολεχμάινεν", "Βίλε Ρίτολα", "Πάαβο Νούρμι", "Λάσε Βίρεν"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Paavo Nurmi υπήρξε ο μεγαλύτερος δρομέας αποστάσεων της εποχής του, κερδίζοντας 9 χρυσά και 3 ασημένια ολυμπιακά μετάλλια (1920, 1924, 1928).",
    "funFacts": [
      "Στους Ολυμπιακούς του Παρισιού το 1924 κέρδισε τα 1.500μ και τα 5.000μ με διαφορά μόλις 55 λεπτών μεταξύ των δύο τελικών.",
      "Έτρεχε πάντα κρατώντας ένα χρονόμετρο στο χέρι για να ρυθμίζει με απόλυτη ακρίβεια τον ρυθμό των διασκελισμών του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AC%CE%B1%CE%B2%CE%BF_%CE%9D%CE%BF%CF%8D%CF%81%CE%BC%CE%B9",
    "locale": "el-GR",
    "tags": ["paavo-nurmi", "flying-finns", "olympics-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_064",
    "text": "Ποιος Σουηδός τενίστας κατέκτησε 11 τίτλους Grand Slam (6 Roland Garros και 5 συνεχόμενα Wimbledon) πριν αποσυρθεί σοκαριστικά σε ηλικία μόλις 26 ετών;",
    "answers": ["Στέφαν Έντμπεργκ", "Ματς Βιλάντερ", "Μάγκνους Νόρμαν", "Μπιόρν Μποργκ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Björn Borg κυριάρχησε στο παγκόσμιο τένις τη δεκαετία του '70 με τη χαρακτηριστική κορδέλα στα μαλλιά και το 'παγωμένο' στυλ παιχνιδιού του (Ice Man).",
    "funFacts": [
      "Κέρδισε 5 συνεχόμενα Wimbledon μεταξύ 1976 και 1980, επίδοση που ισοφάρισε μόνο ο Roger Federer σχεδόν τρεις δεκαετίες αργότερα.",
      "Η επική κόντρα του με τον Αμερικανό Τζον Μάκενρο το 1980 θεωρείται από τις σπουδαιότερες στην ιστορία του αθλητισμού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B9%CF%8C%CF%81%CE%BD_%CE%9C%CF%80%CE%BF%CF%81%CE%B3%CE%BA",
    "locale": "el-GR",
    "tags": ["bjorn-borg", "wimbledon", "tennis-legends"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_065",
    "text": "Σε ποια ευρωπαϊκή χώρα βρίσκεται η ιστορική πίστα του Σπα-Φρανκορσάν (Spa-Francorchamps), διάσημη για τη θρυλική ανηφορική στροφή Eau Rouge;",
    "answers": ["Στο Βέλγιο", "Στην Ολλανδία", "Στη Γαλλία", "Στην Αυστρία"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η πίστα του Σπα βρίσκεται στις Αρδέννες του Βελγίου και είναι η μεγαλύτερη σε μήκος πίστα του σύγχρονου πρωταθλήματος Formula 1 (7,004 χλμ.).",
    "funFacts": [
      "Ο καιρός στο Σπα είναι τόσο απρόβλεπτος που μπορεί να βρέχει καταρρακτωδώς σε ένα τμήμα της πίστας ενώ σε άλλο να έχει απόλυτη ηλιοφάνεια.",
      "Ο Michael Schumacher κατέχει το ρεκόρ με 6 νίκες στο ιστορικό βελγικό σιρκουί."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AF%CF%83%CF%84%CE%B1_%CE%A3%CF%80%CE%B1-%CE%A6%CF%81%CE%B1%CE%BD%CE%BA%CE%BF%CF%81%CF%83%CE%AC%CE%BD",
    "locale": "el-GR",
    "tags": ["spa-francorchamps", "belgium", "formula-1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_066",
    "text": "Ποιος Γάλλος ποδοσφαιρικός θρύλος σημείωσε δύο γκολ με κεφαλιά στον τελικό του Μουντιάλ 1998 χαρίζοντας στη Γαλλία το τρόπαιο με 3-0 εναντίον της Βραζιλίας;",
    "answers": ["Τιερί Ανρί", "Ζινεντίν Ζιντάν", "Ντιντιέ Ντεσάν", "Εμανουέλ Πετί"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Zinedine Zidane ('Zizou') οδήγησε τη Γαλλία στον πρώτο της παγκόσμιο τίτλο στο Stade de France κερδίζοντας την ίδια χρονιά και τη Χρυσή Μπάλα.",
    "funFacts": [
      "Πριν από τον τελικό του 1998 δεν είχε σκοράρει κανένα γκολ σε εκείνο το Μουντιάλ και είχε δεχτεί μάλιστα κόκκινη κάρτα στους ομίλους.",
      "Το 2002 πέτυχε με τη Ρεάλ Μαδρίτης στον τελικό του Champions League ένα από τα πιο διάσημα εναέρια βολέ στην ιστορία του ποδοσφαίρου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B9%CE%BD%CE%B5%CE%BD%CF%84%CE%AF%CE%BD_%CE%96%CE%B9%CE%BD%CF%84%CE%AC%CE%BD",
    "locale": "el-GR",
    "tags": ["zidane", "world-cup-1998", "france-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_067",
    "text": "Ποια Ολλανδή κολυμβήτρια κυριάρχησε στους Ολυμπιακούς Αγώνες του Σίδνεϊ το 2000 κερδίζοντας 3 χρυσά μετάλλια στα σπριντ (50μ ελεύθερο, 100μ ελεύθερο, 100μ πεταλούδα);",
    "answers": ["Φέμκε Χέεμσκερκ", "Ρανόμι Κρομοβιντζότζο", "Ίνγκε ντε Μπρούιν", "Πένι Χέινς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Inge de Bruijn κατέρριψε πολλαπλά παγκόσμια ρεκόρ στο Σίδνεϊ αποτελώντας την κορυφαία σπρίντερ της παγκόσμιας κολύμβησης.",
    "funFacts": [
      "Στην Αθήνα το 2004 υπερασπίστηκε τον τίτλο της στα 50μ ελεύθερο φτάνοντας συνολικά τα 8 ολυμπιακά μετάλλια.",
      "Αναδείχθηκε Κολυμβήτρια της Χρονιάς παγκοσμίως από το περιοδικό Swimming World το 2000 και το 2001."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%8A%CE%BD%CE%B3%CE%BA%CE%B5_%CE%BD%CF%84%CE%B5_%CE%9C%CF%80%CF%81%CE%BF%CF%8D%CE%B9%CE%BD",
    "locale": "el-GR",
    "tags": ["de-bruijn", "swimming", "sydney-2000"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_068",
    "text": "Σε ποιο χειμερινό άθλημα διεξάγεται κάθε χρόνο την περίοδο των εορτών το περίφημο 'Τουρνουά των Τεσσάρων Λόφων' (Vierschanzentournee);",
    "answers": ["Δίαθλο", "Αλπικό σκι", "Σνόουμπορντ", "Άλμα με σκι"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Four Hills Tournament διεξάγεται από το 1953 σε τέσσερις βατήρες άλματος στη Γερμανία (Όμπερστορφ, Γκάρμις) και στην Αυστρία (Ίνσμπρουκ, Μπίσοφσχοφεν).",
    "funFacts": [
      "Ο Γερμανός Σβεν Χαναβάλντ ήταν ο πρώτος αθλητής στην ιστορία που κέρδισε και τους τέσσερις αγώνες στην ίδια σεζόν (2001-02).",
      "Ο νικητής της διοργάνωσης παραλαμβάνει το διάσημο χρυσό αγαλματίδιο του Χρυσού Αετού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%BC%CE%B1_%CE%BC%CE%B5_%CF%83%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["ski-jumping", "four-hills", "winter-sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_069",
    "text": "Σε ποια χρονιά πέτυχε ο Μπάστερ Ντάγκλας τη μεγαλύτερη έκπληξη στην ιστορία της πυγμαχίας βγάζοντας νοκ-άουτ τον ανίκητο Μάικ Τάισον στο Τόκιο;",
    "answers": ["Το 1990", "Το 1988", "Το 1992", "Το 1986"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 11 Φεβρουαρίου 1990 στο Tokyo Dome, ο Buster Douglas (αουτσάιντερ με απόδοση 42 προς 1) έβγαλε νοκ-άουτ τον Mike Tyson στον 10ο γύρο.",
    "funFacts": [
      "Ήταν η πρώτη επαγγελματική ήττα της καριέρας του Tyson μετά από 37 συνεχόμενες νίκες.",
      "Ο Douglas είχε χάσει τη μητέρα του μόλις 23 ημέρες πριν από τον αγώνα και της αφιέρωσε τη συγκλονιστική νίκη του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%B9%CE%BA_%CE%A4%CE%AC%CE%B9%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["mike-tyson", "buster-douglas", "boxing-upset", "tokyo-1990"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_070",
    "text": "Ποιος Σέρβος προπονητής οδήγησε τον Παναθηναϊκό στο πρώτο ευρωπαϊκό πρωτάθλημα μπάσκετ της ιστορίας του στο Final Four του Παρισιού το 1996;",
    "answers": ["Ζέλικο Ομπράντοβιτς", "Μπόζινταρ Μάλκοβιτς", "Ντούσαν Ίβκοβιτς", "Σβέτισλαβ Πέσιτς"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Božidar Maljković οδήγησε τον Παναθηναϊκό στον θρίαμβο του Παρισιού νικώντας στον δραματικό τελικό την Μπαρτσελόνα με 67-66.",
    "funFacts": [
      "Ο τελικός κρίθηκε στο τελευταίο δευτερόλεπτο με το ιστορικό κόψιμο του Στόγιαν Βράνκοβιτς στον Χοσέ Αντόνιο Μοντέρο.",
      "Ο Maljković είχε κατακτήσει νωρίτερα την EuroLeague δύο φορές με τη Γιουγκοπλάστικα Σπλιτ και μία με τη γαλλική Λιμόζ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%BD%CE%B1%CE%B8%CE%B7%CE%BD%CE%B1%CF%8A%CE%BA%CF%8C%CF%82_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["panathinaikos-1996", "maljkovic", "paris-1996", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_071",
    "text": "Ποιος φημισμένος μονοήμερος ποδηλατικός αγώνας στη βόρεια Γαλλία αποκαλείται 'Η Κόλαση του Βορρά' λόγω των επικίνδυνων λιθόστρωτων τομέων του;",
    "answers": ["Γύρος της Φλάνδρας", "Μιλάνο - Σαν Ρέμο", "Παρίσι - Ρουμπέ (Paris-Roubaix)", "Λιέγη - Μπαστόν - Λιέγη"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Paris-Roubaix διεξάγεται από το 1896 και περιλαμβάνει πάνω από 50 χιλιόμετρα τραχιού καλντεριμιού (pavé), καταπονώντας τρομερά αναβάτες και ποδήλατα.",
    "funFacts": [
      "Ο νικητής του αγώνα δεν παραλαμβάνει συνηθισμένο κύπελλο, αλλά ένα αυθεντικό λιθόστρωτο καλντεριμιού στερεωμένο σε βάση.",
      "Ο τερματισμός γίνεται παραδοσιακά μέσα στο ιστορικό ανοιχτό ποδηλατοδρόμιο του Ρουμπέ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CF%81%CE%AF%CF%83%CE%B9-%CE%A1%CE%BF%CF%85%CE%BC%CF%80%CE%AD",
    "locale": "el-GR",
    "tags": ["paris-roubaix", "cycling-monuments", "hell-of-the-north"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_072",
    "text": "Ποιος Νορβηγός επιθετικός ('Super Sub') πέτυχε το ιστορικό γκολ στο 93ο λεπτό χαρίζοντας στη Μάντσεστερ Γιουνάιτεντ το Champions League του 1999 κόντρα στην Μπάγερν;",
    "answers": ["Τέντι Σέριγχαμ", "Ντουάιτ Γιορκ", "Άντι Κόουλ", "Όλε Γκούναρ Σόλσκιερ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ole Gunnar Solskjær μπήκε ως αλλαγή και σκόραρε από κοντά μετά από κόρνερ στις καθυστερήσεις, ολοκληρώνοντας την απόλυτη ανατροπή από 0-1 σε 2-1 στο Camp Nou.",
    "funFacts": [
      "Με εκείνο το γκολ η Manchester United εξασφάλισε το ιστορικό Treble (Premier League, FA Cup, Champions League) της σεζόν 1998-99.",
      "Αργότερα διετέλεσε και πρώτος προπονητής της Μάντσεστερ Γιουνάιτεντ μεταξύ 2018 και 2021."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%8C%CE%BB%CE%B5_%CE%93%CE%BA%CE%BF%CF%8D%CE%BD%CE%B1%CF%81_%CE%A3%CF%8C%CE%BB%CF%83%CE%BA%CE%B9%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["solskjaer", "manchester-united-1999", "champions-league"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_073",
    "text": "Ποιο είναι το επίσημο ελάχιστο βάρος του ανδρικού ακοντίου στους επίσημους αγώνες στίβου;",
    "answers": ["800 γραμμάρια", "600 γραμμάρια", "1.000 γραμμάρια", "700 γραμμάρια"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το ακόντιο ανδρών ζυγίζει επίσημα τουλάχιστον 800 γραμμάρια και έχει μήκος 2,60 έως 2,70 μέτρα.",
    "funFacts": [
      "Στις γυναίκες το αντίστοιχο ακόντιο ζυγίζει τουλάχιστον 600 γραμμάρια και έχει μήκος 2,20 έως 2,30 μέτρα.",
      "Το ακόντιο πρέπει να προσγειωθεί πρώτα με τη μεταλλική του αιχμή για να θεωρηθεί η ρίψη έγκυρη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BA%CE%BF%CE%BD%CF%84%CE%B9%CF%83%CE%BC%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["javelin", "athletics-equipment", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_074",
    "text": "Σε ποια σκανδιναβική χώρα κωδικοποιήθηκαν για πρώτη φορά οι πρώιμοι κανόνες της σύγχρονης χειροσφαίρισης (χάντμπολ) από τον Χόλγκερ Νίλσεν το 1898;",
    "answers": ["Στη Σουηδία", "Στη Δανία", "Στη Νορβηγία", "Στη Φινλανδία"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Δανός δάσκαλος και ολυμπιονίκης Holger Nielsen θέσπισε το παιχνίδι 'haandbold' το 1898 στο Όρντρουπ της Δανίας και δημοσίευσε τους πρώτους επίσημους κανόνες το 1906.",
    "funFacts": [
      "Ο Nielsen υπήρξε επίσης ολυμπιονίκης στην ξιφασκία και στη σκοποβολή στους πρώτους Ολυμπιακούς Αγώνες της Αθήνας το 1896.",
      "Η Δανία αποτελεί παραδοσιακή υπερδύναμη του αθλήματος έχοντας κερδίσει τρία διαδοχικά Παγκόσμια Πρωταθλήματα ανδρών (2019, 2021, 2023)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CF%81%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["handball-history", "denmark", "holger-nielsen"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_075",
    "text": "Ποιος ελληνικός σύλλογος έχει κατακτήσει δύο φορές το Champions League υδατοσφαίρισης ανδρών (το 2002 στη Βουδαπέστη και το 2018 στη Γένοβα);",
    "answers": ["Βουλιαγμένη", "Εθνικός Πειραιώς", "Ολυμπιακός", "Παναθηναϊκός"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ολυμπιακός είναι η μοναδική ελληνική ομάδα που έχει κατακτήσει την κορυφαία ευρωπαϊκή διασυλλογική διοργάνωση στο ανδρικό πόλο.",
    "funFacts": [
      "Το 2002 νίκησε στον τελικό την ουγγρική Χόνβεντ μέσα στη Βουδαπέστη με 9-7, γινόμενος η πρώτη ομάδα που πέτυχε το ευρωπαϊκό Grand Slam στο πόλο.",
      "Το 2018 επικράτησε της πανίσχυρης διοργανώτριας Προ Ρέκο στη Γένοβα με 9-7."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CF%8C%CF%82_%CE%A3.%CE%A6.%CE%A0._(%CF%85%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["olympiacos-waterpolo", "champions-league", "water-polo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_076",
    "text": "Ποιος Αυστριακός πιλότος είναι ο μοναδικός στην ιστορία της Formula 1 που αναδείχθηκε Παγκόσμιος Πρωταθλητής μετά θάνατον (το 1970);",
    "answers": ["Νίκι Λάουντα", "Γκέρχαρντ Μπέργκερ", "Ρόλαντ Ράτσενμπεργκερ", "Γιόχεν Ριντ (Jochen Rindt)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Jochen Rindt σκοτώθηκε στις δοκιμές της Μόντσα τον Σεπτέμβριο του 1970 οδηγώντας για τη Lotus, αλλά η βαθμολογική του διαφορά δεν καλύφθηκε στους εναπομείναντες αγώνες.",
    "funFacts": [
      "Το τρόπαιο του πρωταθλητή απονεμήθηκε στη χήρα του, Νίνα Ριντ, στο τέλος της σεζόν.",
      "Είχε κερδίσει 5 Grand Prix εκείνη τη σεζόν πριν από το μοιραίο ατύχημα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CF%87%CE%B5%CE%BD_%CE%A1%CE%B9%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["jochen-rindt", "formula-1-1970", "motorsport-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_077",
    "text": "Ποιο ήταν το παγκοσμίως διάσημο προσωνύμιο της Εθνικής Ολλανδίας της δεκαετίας του '70 υπό τον Ρίνους Μίχελς και τον Γιόχαν Κρόιφ;",
    "answers": ["Κουρδιστό Πορτοκάλι", "Ιπτάμενοι Ολλανδοί", "Πορτοκαλί Θύελλα", "Ολλανδική Μηχανή"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Ολλανδία του 1974 έμεινε στην ιστορία ως 'Κουρδιστό Πορτοκάλι' (εμπνευσμένο από την ταινία του Κιούμπρικ) χάρη στο επαναστατικό σύστημα του 'Total Football'.",
    "funFacts": [
      "Στο 'Ολοκληρωτικό Ποδόσφαιρο' κάθε παίκτης γηπέδου μπορούσε να αναλάβει τον ρόλο οποιουδήποτε άλλου συμπαίκτη ανάλογα με τη ροή του αγώνα.",
      "Έφτασε σε δύο συνεχόμενους τελικούς Μουντιάλ (1974 και 1978), χάνοντας όμως και τους δύο από τις διοργανώτριες χώρες (Δυτική Γερμανία και Αργεντινή)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%9F%CE%BB%CE%BB%CE%B1%CE%BD%CE%B4%CE%AF%CE%B1%CF%82_(%CF%80%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%BF_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["netherlands-1974", "total-football", "cruyff"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_078",
    "text": "Ποιος Νιγηριανός σέντερ επελέγη στο No. 1 του ιστορικού NBA Draft του 1984 από τους Houston Rockets, μπροστά από τον Μάικλ Τζόρνταν;",
    "answers": ["Τσαρλς Μπάρκλεϊ", "Χακίμ Ολάζουον", "Σαμ Μπόουι", "Τζον Στόκτον"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Hakeem 'The Dream' Olajuwon επιλέχθηκε πρώτος και δικαίωσε απόλυτα την επιλογή οδηγώντας τους Rockets σε δύο συνεχόμενα πρωταθλήματα NBA (1994, 1995).",
    "funFacts": [
      "Έμεινε στην ιστορία για την ανυπέρβλητη κίνηση προσποίησης στη ρακέτα γνωστή ως 'Dream Shake'.",
      "Είναι ο κορυφαίος μπλοκέρ όλων των εποχών στην ιστορία του NBA με 3.830 κοψίματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B1%CE%BA%CE%AF%CE%BC_%CE%9F%CE%BB%CE%AC%CE%B6%CE%BF%CF%85%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["olajuwon", "nba-draft-1984", "rockets"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_079",
    "text": "Ποιος Ελληνοαμερικανός τενίστας κατέκτησε 14 τίτλους Grand Slam και κυριάρχησε στο ανδρικό τένις τη δεκαετία του '90 με το περίφημο serve-and-volley παιχνίδι του;",
    "answers": ["Αντρέ Αγκάσι", "Τζιμ Κούριερ", "Πιτ Σάμπρας", "Μάικλ Τσανγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Pete Sampras ('Pistol Pete') κατέκτησε 7 Wimbledon, 5 US Open και 2 Australian Open, τερματίζοντας στο Νο. 1 της παγκόσμιας κατάταξης για 6 συνεχόμενα έτη (1993–1998).",
    "funFacts": [
      "Ο πατέρας του ήταν ελληνικής καταγωγής και η μητέρα του Ελληνίδα μετανάστρια από τη Σπάρτη.",
      "Έδωσε τον τελευταίο αγώνα της καριέρας του στον τελικό του US Open το 2002 νικώντας τον αιώνιο αντίπαλό του Andre Agassi."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CF%84_%CE%A3%CE%AC%CE%BC%CF%80%CF%81%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["pete-sampras", "tennis-legends", "grand-slam"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_080",
    "text": "Σε ποια νορβηγική πόλη διεξήχθησαν οι Χειμερινοί Ολυμπιακοί Αγώνες του 1994, οι πρώτοι που έγιναν σε διαφορετικό έτος από τους Θερινούς;",
    "answers": ["Στο Όσλο", "Στο Μπέργκεν", "Στο Τρόντχαϊμ", "Στο Λιλεχάμερ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Lillehammer φιλοξένησε τους Αγώνες του 1994, μόλις δύο χρόνια μετά το Albertville 1992, εγκαινιάζοντας την εναλλάξ διεξαγωγή Θερινών και Χειμερινών Αγώνων ανά διετία.",
    "funFacts": [
      "Οι Αγώνες του Λιλεχάμερ θεωρούνται από πολλούς ως οι πιο επιτυχημένοι Χειμερινοί Ολυμπιακοί Αγώνες στην ιστορία χάρη στην αυθεντική ατμόσφαιρα.",
      "Η κούρσα των 1.000 μέτρων ταχείας παγοδρομίας κερδήθηκε από τον Νορβηγό Johann Olav Koss με τρία παγκόσμια ρεκόρ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CE%BC%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1994",
    "locale": "el-GR",
    "tags": ["lillehammer-1994", "winter-olympics", "norway"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_081",
    "text": "Ποιο είναι το επίσημο παγκόσμιο ρεκόρ στον ακοντισμό ανδρών που πέτυχε ο Τσέχος Γιαν Ζελέζνι το 1996 στην Ιένα της Γερμανίας;",
    "answers": ["98,48 μέτρα", "104,80 μέτρα", "95,66 μέτρα", "92,72 μέτρα"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 25 Μαΐου 1996, ο Jan Železný έστειλε το ακόντιο στα 98,48 μέτρα, επίδοση που παραμένει ακατάρριπτο παγκόσμιο ρεκόρ για σχεδόν 30 χρόνια.",
    "funFacts": [
      "Ο Železný κατέχει τις 5 κορυφαίες βολές στην ιστορία του ακοντισμού με το σύγχρονο μοντέλο ακοντίου.",
      "Κέρδισε 3 συνεχόμενα χρυσά ολυμπιακά μετάλλια (1992, 1996, 2000) και ένα ασημένιο (1988)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%B1%CE%BD_%CE%96%CE%B5%CE%BB%CE%AD%CE%B6%CE%BD%CE%B9",
    "locale": "el-GR",
    "tags": ["jan-zelezny", "javelin-record", "athletics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_082",
    "text": "Ποιος Πορτογάλος προπονητής αυτοαποκαλέστηκε 'Special One' στην πρώτη του συνέντευξη τύπου στην Τσέλσι το 2004;",
    "answers": ["Πεπ Γκουαρδιόλα", "Ζοσέ Μουρίνιο", "Φερνάντο Σάντος", "Αντρέ Βίλας-Μπόας"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο José Mourinho δήλωσε το περίφημο 'Please don't call me arrogant, but I'm European champion and I think I'm a special one' έχοντας μόλις κατακτήσει το Champions League με την Πόρτο.",
    "funFacts": [
      "Στην πρώτη του σεζόν στην Premier League (2004-05), η Τσέλσι δέχτηκε μόλις 15 γκολ σε 38 αγώνες, ρεκόρ που παραμένει ακατάρριπτο.",
      "Το 2010 οδήγησε την Ίντερ στο πρώτο ιστορικό Treble ιταλικού συλλόγου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%BF%CF%83%CE%AD_%CE%9C%CE%BF%CF%85%CF%81%CE%AF%CE%BD%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["mourinho", "chelsea", "special-one", "football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_083",
    "text": "Σε ποια ιστορική χρονιά κατέκτησε η ΑΕΚ το Κύπελλο Κυπελλούχων Ευρώπης στο μπάσκετ μπροστά σε 80.000 θεατές στο Καλλιμάρμαρο;",
    "answers": ["Το 1964", "Το 1970", "Το 1968", "Το 1972"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 4 Απριλίου 1968, η ΑΕΚ νίκησε τη Σλάβια Πράγας με 89-82 στο Παναθηναϊκό Στάδιο κατακτώντας τον πρώτο ευρωπαϊκό τίτλο ελληνικού ομαδικού αθλητισμού.",
    "funFacts": [
      "Η προσέλευση των 80.000 θεατών καταγράφηκε στο Βιβλίο των Ρεκόρ Γκίνες ως το παγκόσμιο ρεκόρ θεατών σε αγώνα μπάσκετ.",
      "Η ιστορική ραδιοφωνική μετάδοση του Βασίλη Γεωργίου με τη φράση 'Είναι το κύπελλο της Ελλάδος!' συγκίνησε ολόκληρο το έθνος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%95%CE%9A_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["aek-1968", "kallimarmaro", "greek-basketball", "saporta"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_084",
    "text": "Ποιος Γάλλος κολυμβητής αναδείχθηκε το απόλυτο πρόσωπο των Ολυμπιακών Αγώνων του Παρισιού το 2024 κατακτώντας 4 ατομικά χρυσά μετάλλια;",
    "answers": ["Φλοράν Μανοντού", "Αμορί Λεβό", "Γιανίκ Ανιέλ", "Λεόν Μαρσάν (Léon Marchand)"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Léon Marchand κέρδισε 4 χρυσά μετάλλια (200μ πρόσθιο, 200μ πεταλούδα, 200μ μικτή, 400μ μικτή) καταρρίπτοντας ολυμπιακά ρεκόρ και στα τέσσερα.",
    "funFacts": [
      "Στις 31 Ιουλίου 2024 πέτυχε το μοναδικό επίτευγμα να κερδίσει τα 200μ πεταλούδα και τα 200μ πρόσθιο την ίδια ακριβώς βραδιά μέσα σε διάστημα δύο ωρών.",
      "Προπονείται στις ΗΠΑ υπό τις οδηγίες του Bob Bowman, του πρώην προπονητή του Michael Phelps."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CF%8C%CE%BD_%CE%9C%CE%B1%CF%81%CF%83%CE%AC%CE%BD",
    "locale": "el-GR",
    "tags": ["leon-marchand", "paris-2024", "swimming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_085",
    "text": "Ποια ιστορική ιταλική πίστα της Formula 1 αποκαλείται παραδοσιακά 'Ο Ναός της Ταχύτητας' (Il Tempio della Velocità);",
    "answers": ["Μόντσα (Monza)", "Ίμολα (Imola)", "Μουτζέλο (Mugello)", "Φιοράνο (Fiorano)"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Autodromo Nazionale Monza κοντά στο Μιλάνο κατασκευάστηκε το 1922 και είναι η ταχύτερη πίστα στο πρόγραμμα της F1 με μέσες ταχύτητες γύρου άνω των 260 χλμ/ώρα.",
    "funFacts": [
      "Οι φανατικοί οπαδοί της Ferrari στη Μόντσα ονομάζονται 'Tifosi' και πλημμυρίζουν την ευθεία εκκίνησης μετά από κάθε αγώνα.",
      "Ο ταχύτερος γύρος στην ιστορία της Formula 1 σημειώθηκε στη Μόντσα από τον Lewis Hamilton το 2020 με μέση ταχύτητα 264,362 χλμ/ώρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BF%CF%85%CF%84%CF%8C%CE%BD%CF%84%CF%81%CE%BF%CE%BC%CE%BF_%CE%9D%CE%B1%CF%84%CF%83%CE%B9%CE%BF%CE%BD%CE%AC%CE%BB%CE%B5_%CE%9C%CF%8C%CE%BD%CF%84%CF%83%CE%B1",
    "locale": "el-GR",
    "tags": ["monza", "temple-of-speed", "formula-1", "italy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_086",
    "text": "Πόσα μεγάλα τουρνουά (Major Championships) έχει κατακτήσει στην καριέρα του ο Τάιγκερ Γουντς (Tiger Woods), δεύτερος πίσω από τον Τζακ Νίκλαους;",
    "answers": ["18 majors", "15 majors", "12 majors", "20 majors"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Tiger Woods έχει κερδίσει 15 Majors (μεταξύ των οποίων 5 Masters), απέχοντας τρεις τίτλους από το ιστορικό ρεκόρ των 18 τίτλων του Jack Nicklaus.",
    "funFacts": [
      "Το 2000-2001 πέτυχε το περίφημο 'Tiger Slam', κατέχοντας και τα 4 μεγάλα τουρνουά ταυτόχρονα.",
      "Η επιστροφή του και η κατάκτηση του Masters το 2019, έπειτα από πολλαπλές εγχειρήσεις στη μέση, θεωρείται μια από τις σπουδαιότερες επιστροφές στον αθλητισμό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AC%CE%B9%CE%B3%CE%BA%CE%B5%CF%81_%CE%93%CE%BF%CF%85%CE%BD%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["tiger-woods", "golf-majors", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_087",
    "text": "Πώς ονομάζεται στο βόλεϊ η θεαματική επίθεση όπου ο επιτιθέμενος απογειώνεται πίσω από τη γραμμή των 3 μέτρων για να καρφώσει;",
    "answers": ["Πλασέ", "Μπλοκ-άουτ", "Επίθεση πίσω ζώνης (Pipe)", "Φλοτ σερβίς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η επίθεση από την πίσω ζώνη (pipe attack) επιτρέπει σε παίκτες της πίσω γραμμής να επιτεθούν δυναμικά, αρκεί το πάτημά τους να γίνει πίσω από τη γραμμή επίθεσης των 3 μέτρων.",
    "funFacts": [
      "Ο παίκτης μπορεί να προσγειωθεί μέσα στην μπροστινή ζώνη μετά το χτύπημα, αρκεί το άλμα απογείωσης να μην πάτησε τη γραμμή.",
      "Εισήχθη ευρέως στο διεθνές βόλεϊ τη δεκαετία του '80 από τις ομάδες των ΗΠΑ και της Βραζιλίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["volleyball-tactics", "pipe-attack", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_088",
    "text": "Ποιος Ουκρανός επιθετικός κατέκτησε τη Χρυσή Μπάλα το 2004 αγωνιζόμενος για τη Μίλαν, όντας ένας από τους κορυφαίους σκόρερ της Serie A;",
    "answers": ["Σεργκέι Ρεμπρόφ", "Αντρέι Γιαρμολένκο", "Όλεγκ Μπλαχίν", "Αντρέι Σεβτσένκο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Andriy Shevchenko ('Sheva') κέρδισε το Ballon d'Or το 2004 αφού οδήγησε τη Μίλαν στο ιταλικό πρωτάθλημα, έχοντας κερδίσει και το Champions League το 2003.",
    "funFacts": [
      "Είναι ο δεύτερος σκόρερ όλων των εποχών στην ιστορία της Μίλαν με 175 γκολ, πίσω μόνο από τον Gunnar Nordahl.",
      "Διετέλεσε ομοσπονδιακός προπονητής της Εθνικής Ουκρανίας οδηγώντας την στα προημιτελικά του Euro 2020."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%81%CE%AD%CE%B9_%CE%A3%CE%B5%CE%B2%CF%84%CF%83%CE%AD%CE%BD%CE%BA%CE%BF",
    "locale": "el-GR",
    "tags": ["shevchenko", "ballon-dor-2004", "milan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_089",
    "text": "Σε ποια ιαπωνική πόλη βρίσκεται το Κοντοκάν (Kodokan), το παγκόσμιο αρχηγείο και λίκνο του αθλήματος του τζούντο;",
    "answers": ["Στο Τόκιο", "Στο Κιότο", "Στην Οσάκα", "Στη Χιροσίμα"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το ινστιτούτο Kodokan ιδρύθηκε το 1882 στο Τόκιο από τον Τζίγκορο Κάνο και παραμένει η παγκόσμια πνευματική και τεχνική έδρα του τζούντο.",
    "funFacts": [
      "Ξεκίνησε με μόλις 9 μαθητές σε έναν μικρό βουδιστικό ναό και σήμερα στεγάζεται σε ένα πολυώροφο κτίριο με οκτώ ορόφους dojo.",
      "Το κεντρικό dojo στον 7ο όροφο περιλαμβάνει 420 τατάμι και φιλοξενεί εκατοντάδες ασκούμενους καθημερινά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%8D%CE%BD%CF%84%CE%BF",
    "locale": "el-GR",
    "tags": ["kodokan", "judo", "tokyo", "martial-arts"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_090",
    "text": "Ποια Αμερικανίδα σπρίντερ ('Flo-Jo') σημείωσε το 1988 τα ασύλληπτα παγκόσμια ρεκόρ στα 100μ (10,49 δευτ.) και 200μ (21,34 δευτ.) που διατηρούνται ακόμα;",
    "answers": ["Μάριον Τζόουνς", "Φλόρενς Γκρίφιθ-Τζόινερ", "Έβελιν Άσφορντ", "Γουίλμα Ρούντολφ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Florence Griffith Joyner έγραψε ιστορία το 1988 στη Σεούλ με τις απίστευτες ταχύτητές της και το εκκεντρικό στυλ με τα μακριά βαμμένα νύχια.",
    "funFacts": [
      "Τα δύο παγκόσμια ρεκόρ της παραμένουν ακατάρριπτα για σχεδόν τέσσερις δεκαετίες.",
      "Πέθανε ξαφνικά στον ύπνο της το 1998 σε ηλικία μόλις 38 ετών από επιληπτική κρίση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%BB%CF%8C%CF%81%CE%B5%CE%BD%CF%82_%CE%93%CE%BA%CF%81%CE%AF%CF%86%CE%B9%CE%B8-%CE%A4%CE%B6%CF%8C%CE%B9%CE%BD%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["flo-jo", "sprint-records", "athletics-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_091",
    "text": "Ποιος ιστορικός ισραηλινός σύλλογος καλαθοσφαίρισης έχει κατακτήσει 6 φορές την EuroLeague και αγωνίζεται παραδοσιακά στη Nokia Arena (Yad Eliyahu);",
    "answers": ["Χάποελ Ιερουσαλήμ", "Χάποελ Τελ Αβίβ", "Μακάμπι Τελ Αβίβ", "Ιρόνι Νες Ζιόνα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Maccabi Tel Aviv είναι μία από τις πιο επιτυχημένες ομάδες στην ιστορία της EuroLeague με κατακτήσεις το 1977, 1981, 2001, 2004, 2005 και 2014.",
    "funFacts": [
      "Στον τελικό του 2004 στο Τελ Αβίβ διέλυσε τη Σκίπερ Μπολόνια με 118-74, σημειώνοντας τη μεγαλύτερη διαφορά πόντων σε τελικό EuroLeague.",
      "Το 2014 κατέκτησε τον τίτλο στο Μιλάνο ως το απόλυτο αουτσάιντερ υπό τις οδηγίες του Ντέιβιντ Μπλατ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%BA%CE%AC%CE%BC%CF%80%CE%B9_%CE%A4%CE%B5%CE%BB_%CE%91%CE%B2%CE%AF%CE%B2_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7)",
    "locale": "el-GR",
    "tags": ["maccabi-tel-aviv", "euroleague", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_092",
    "text": "Σε ποια καναδική πόλη διοργανώθηκαν οι Χειμερινοί Ολυμπιακοί Αγώνες του 1988, όπου έκανε το ιστορικό ντεμπούτο της η ομάδα μπόμπσλεϊ της Τζαμάικα;",
    "answers": ["Στο Βανκούβερ", "Στο Μόντρεαλ", "Στο Τορόντο", "Στο Κάλγκαρι"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Calgary φιλοξένησε τους Χειμερινούς Αγώνες του 1988 που ενέπνευσαν την παγκόσμια επιτυχία της κινηματογραφικής ταινίας 'Cool Runnings'.",
    "funFacts": [
      "Στους ίδιους αγώνες αγωνίστηκε και ο Βρετανός Έντι 'Ο Αετός' Έντουαρντς στο άλμα με σκι, κερδίζοντας τη λατρεία του κοινού παρά τις τελευταίες θέσεις.",
      "Ο Φινλανδός Μάτι Νίκανεν κέρδισε και τα τρία χρυσά μετάλλια στο άλμα με σκι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CE%BC%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1988",
    "locale": "el-GR",
    "tags": ["calgary-1988", "bobsleigh", "cool-runnings", "winter-olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_093",
    "text": "Ποιο είναι το επίσημο όνομα του σταδίου Μαρακανά στο Ρίο ντε Τζανέιρο προς τιμήν ενός διάσημου Βραζιλιάνου αθλητικογράφου;",
    "answers": ["Εστάντιο Ζορναλίστα Μάριο Φίλιο", "Εστάντιο Πελέ", "Εστάντιο Γκαρίντσα", "Εστάντιο Ζίκο"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το επίσημο όνομα του Μαρακανά είναι 'Estádio Jornalista Mário Filho', προς τιμήν του δημοσιογράφου που πρωτοστάτησε στην ανέγερσή του για το Μουντιάλ του 1950.",
    "funFacts": [
      "Η περιοχή ονομαζόταν Μαρακανά από ένα είδος παπαγάλου που ζούσε στον κοντινό ποταμό.",
      "Φιλοξένησε δύο τελικούς Παγκοσμίου Κυπέλλου (1950 και 2014) καθώς και την τελετή έναρξης των Ολυμπιακών Αγώνων του 2016."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AC%CE%B4%CE%B9%CE%BF_%CE%9C%CE%B1%CF%81%CE%B1%CE%BA%CE%B1%CE%BD%CE%AC",
    "locale": "el-GR",
    "tags": ["maracana", "stadiums", "brazil-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_094",
    "text": "Ποια Ελβετίδα τενίστρια έγινε το 1997 η νεότερη νικήτρια Grand Slam στην Open Era κερδίζοντας το Australian Open σε ηλικία μόλις 16 ετών και 3 μηνών;",
    "answers": ["Μόνικα Σέλες", "Μαρτίνα Χίνγκις", "Αράντσα Σάντσεθ Βικάριο", "Ζιστίν Ενάν"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Martina Hingis κατέκτησε 3 Grand Slam το 1997 (Australian Open, Wimbledon, US Open) και έγινε η νεότερη Νο. 1 στην ιστορία της WTA.",
    "funFacts": [
      "Πήρε το όνομά της από τη θρυλική Martina Navratilova, καθώς η μητέρα της ήταν επίσης επαγγελματίας προπονήτρια τένις.",
      "Κέρδισε συνολικά 25 τίτλους Grand Slam στην καριέρα της (5 στο μονό, 13 στο διπλό και 7 στο μεικτό διπλό)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CF%84%CE%AF%CE%BD%CE%B1_%CE%A7%CE%AF%CE%BD%CE%B3%CE%BA%CE%B9%CF%82",
    "locale": "el-GR",
    "tags": ["martina-hingis", "tennis-records", "grand-slam"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_095",
    "text": "Ποιος Έλληνας άλτης κατέκτησε το ασημένιο μετάλλιο στο άλμα εις μήκος στο Ευρωπαϊκό Πρωτάθλημα της Βουδαπέστης το 1998 και κατέχει το πανελλήνιο ρεκόρ κλειστού στίβου (8,23 μ.);",
    "answers": ["Μίλτος Τεντόγλου", "Σπύρος Βασδέκης", "Κώστας Κουκοδήμος", "Λούης Τσάτουμας"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Κώστας Κουκοδήμος υπήρξε κορυφαίος Έλληνας άλτης μήκους της δεκαετίας του 1990 με άλμα 8,36 μέτρα στον ανοιχτό στίβο και ολυμπιακή διάκριση (6ος στη Βαρκελώνη 1992).",
    "funFacts": [
      "Κέρδισε επίσης το χάλκινο μετάλλιο στο Ευρωπαϊκό Πρωτάθλημα του Ελσίνκι το 1994.",
      "Μετά την αθλητική του καριέρα εξελέγη βουλευτής και δήμαρχος Κατερίνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CF%83%CF%84%CE%B1%CF%82_%CE%9A%CE%BF%CF%85%CE%BA%CE%BF%CE%B4%CE%AE%CE%BC%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["koukodimos", "long-jump", "greek-athletics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_096",
    "text": "Από ποια χώρα καταγόταν ο θρυλικός Χουάν Μανουέλ Φάντζιο (Juan Manuel Fangio), που κατέκτησε 5 παγκόσμια πρωταθλήματα Formula 1 τη δεκαετία του '50;",
    "answers": ["Βραζιλία", "Ισπανία", "Ιταλία", "Αργεντινή"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Juan Manuel Fangio ('El Chueco') γεννήθηκε στο Μπαλκάρσε της Αργεντινής και κατέκτησε 5 πρωταθλήματα με 4 διαφορετικές ομάδες (Alfa Romeo, Maserati, Mercedes, Ferrari).",
    "funFacts": [
      "Κατέχει το απλησίαστο ρεκόρ του υψηλότερου ποσοστού νικών στην ιστορία της Formula 1, έχοντας κερδίσει το 46,15% των αγώνων στους οποίους εκκίνησε (24 νίκες σε 52 Grand Prix).",
      "Το 1958 απήχθη στην Κούβα από επαναστάτες του Φιντέλ Κάστρο για πολιτικούς λόγους και αφέθηκε ελεύθερος σώος 29 ώρες αργότερα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%BF%CF%85%CE%AC%CE%BD_%CE%9C%CE%B1%CE%BD%CE%BF%CF%85%CE%AD%CE%BB_%CE%A6%CE%AC%CE%BD%CF%84%CE%B6%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["fangio", "formula-1-history", "argentina"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_097",
    "text": "Ποια εθνική ομάδα κατέκτησε το Euro 1992 στη Σουηδία παρότι είχε κληθεί στο τουρνουά μόλις 10 ημέρες πριν από την έναρξη αντικαθιστώντας τη Γιουγκοσλαβία;",
    "answers": ["Δανία", "Σουηδία", "Ολλανδία", "Τσεχοσλοβακία"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Δανία κλήθηκε εκτάκτως λόγω των κυρώσεων του ΟΗΕ στη Γιουγκοσλαβία και πραγματοποίησε ένα αδιανόητο παραμύθι νικώντας τη Γερμανία στον τελικό με 2-0.",
    "funFacts": [
      "Ο τερματοφύλακας Πέτερ Σμάιχελ ήταν ο απόλυτος ήρωας της διοργάνωσης αποκρούοντας πέναλτι του Φαν Μπάστεν στον ημιτελικό.",
      "Ο αστέρας της ομάδας Μίκαελ Λάουντρουπ είχε αρνηθεί να συμμετάσχει στη διοργάνωση λόγω διαφωνίας τακτικής με τον προπονητή Ρίτσαρντ Μέλερ Νίλσεν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CF%81%CF%89%CF%80%CE%B1%CF%8A%CE%BA%CF%8C_%CE%A0%CF%81%CF%89%CF%84%CE%AC%CE%B8%CE%BB%CE%B7%CE%BC%CE%B1_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_1992",
    "locale": "el-GR",
    "tags": ["denmark-1992", "euro-1992", "fairytale-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_098",
    "text": "Ποιος γκαρντ κατέχει το ρεκόρ των περισσότερων βραβείων Καλύτερου Έκτου Παίκτη του NBA (Sixth Man of the Year) με 3 κατακτήσεις ισοβαθμώντας με τον Λου Γουίλιαμς;",
    "answers": ["Μανού Τζινόμπιλι", "Τζαμάλ Κρόφορντ", "Τζέισον Τέρι", "Αντρέ Ιγκουοντάλα"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Jamal Crawford κέρδισε το βραβείο του κορυφαίου έκτου παίκτη 3 φορές (2010 με Hawks, 2014 και 2016 με Clippers).",
    "funFacts": [
      "Μοιράζεται το ρεκόρ των 3 βραβείων με τον Lou Williams.",
      "Είναι ο μοναδικός παίκτης στην ιστορία του NBA που έχει σημειώσει τουλάχιστον 50 πόντους σε αγώνα με τέσσερις διαφορετικές ομάδες (Bulls, Knicks, Warriors, Suns)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%B1%CE%BC%CE%AC%CE%BB_%CE%9A%CF%81%CF%8C%CF%86%CE%BF%CF%81%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["jamal-crawford", "sixth-man", "nba-awards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_099",
    "text": "Ποιος Κουβανός άλτης κατέχει το παγκόσμιο ρεκόρ στο άλμα εις ύψος ανδρών με 2,45 μέτρα από το 1993;",
    "answers": ["Πάτρικ Σιόμπεργκ", "Μουτάζ Εσά Μπαρσίμ", "Χαβιέρ Σοτομαγιόρ", "Μπόγκνταν Μπονταρένκο"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 27 Ιουλίου 1993 στη Σαλαμάνκα της Ισπανίας, ο Javier Sotomayor πέρασε τα 2,45 μέτρα, ένα ρεκόρ που παραμένει ακατάρριπτο για πάνω από 30 χρόνια.",
    "funFacts": [
      "Είναι ο μόνος άνθρωπος στην ιστορία που έχει ξεπεράσει τα 8 πόδια (2,44 μ.) σε ύψος.",
      "Κατέκτησε το χρυσό ολυμπιακό μετάλλιο στους Ολυμπιακούς Αγώνες της Βαρκελώνης το 1992."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B1%CE%B2%CE%B9%CE%AD%CF%81_%CE%A3%CE%BF%CF%84%CE%BF%CE%BC%CE%B1%CE%B3%CE%B9%CF%8C%CF%81",
    "locale": "el-GR",
    "tags": ["sotomayor", "high-jump-record", "cuba-athletics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_100",
    "text": "Ποιος πυγμάχος βαρέων βαρών νίκησε τον Μοχάμεντ Άλι στον περίφημο 'Αγώνα του Αιώνα' (Fight of the Century) στο Madison Square Garden το 1971;",
    "answers": ["Τζορτζ Φόρμαν", "Κεν Νόρτον", "Σόνι Λίστον", "Τζο Φρέιζερ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Joe Frazier ('Smokin' Joe') έριξε στο καναβάτσο τον Ali στον 15ο γύρο με ένα θρυλικό αριστερό κροσέ και κέρδισε με ομόφωνη απόφαση των κριτών.",
    "funFacts": [
      "Ήταν η πρώτη επίσημη ήττα στην επαγγελματική καριέρα του Muhammad Ali.",
      "Οι δύο αθλητές έδωσαν συνολικά τρεις ιστορικές αναμετρήσεις, με αποκορύφωμα το 'Thrilla in Manila' το 1975 όπου επικράτησε ο Ali."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF_%CE%A6%CF%81%CE%AD%CE%B9%CE%B6%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["joe-frazier", "fight-of-the-century", "ali-frazier"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_101",
    "text": "Σε ποια χρονιά κατέκτησε η Άρσεναλ το πρώτο της νταμπλ (Premier League και FA Cup) υπό την καθοδήγηση του Αρσέν Βενγκέρ;",
    "answers": ["Το 1998", "Το 2002", "Το 2004", "Το 1996"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Τη σεζόν 1997-98, στην πρώτη του πλήρη χρονιά στο τιμόνι των 'Κανονιέρηδων', ο Wenger οδήγησε την Arsenal στο νταμπλ με ηγέτες τους Bergkamp, Vieira και Overmars.",
    "funFacts": [
      "Ο Wenger έγινε ο πρώτος μη Βρετανός προπονητής στην ιστορία που κατέκτησε το αγγλικό πρωτάθλημα.",
      "Η Άρσεναλ ανέτρεψε διαφορά 12 βαθμών από τη Μάντσεστερ Γιουνάιτεντ στον δρόμο προς τον τίτλο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CF%81%CF%83%CE%B5%CE%BD_%CE%92%CE%B5%CE%BD%CE%B3%CE%BA%CE%AD%CF%81",
    "locale": "el-GR",
    "tags": ["wenger", "arsenal-1998", "premier-league"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_102",
    "text": "Ποιος Έλληνας αρσιβαρίστας κατέκτησε δύο ασημένια ολυμπιακά μετάλλια στην κατηγορία των 59 κιλών στην Ατλάντα (1996) και των 62 κιλών στο Σίδνεϊ (2000);",
    "answers": ["Βαλέριος Λεωνίδης", "Λεωνίδας Σαμπάνης", "Γιώργος Τζελίλης", "Βίκτωρ Μήτρου"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Λεωνίδας Σαμπάνης υπήρξε βασικό στέλεχος της 'χρυσής ομάδας' του Χρήστου Ιακώβου, ανεβαίνοντας δύο φορές στο ολυμπιακό βάθρο.",
    "funFacts": [
      "Το 1996 στην Ατλάντα άνοιξε τον χορό των μεταλλίων για την ελληνική άρση βαρών κατακτώντας το πρώτο μετάλλιο της αποστολής.",
      "Αναδείχθηκε επίσης δύο φορές Παγκόσμιος Πρωταθλητής (1995 στην Γκουανγκτζόου και 1998 στο Λάχτι)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CF%89%CE%BD%CE%AF%CE%B4%CE%B1%CF%82_%CE%A3%CE%B1%CE%BC%CF%80%CE%AC%CE%BD%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["sampanis", "weightlifting-greece", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_103",
    "text": "Τι μοτίβο έχει η φανέλα που φοράει ο κορυφαίος αναβάτης των βουνών (King of the Mountains) στον Γύρο της Γαλλίας;",
    "answers": ["Ολόλευκη", "Κίτρινη με μαύρες ρίγες", "Λευκή με κόκκινα βούλωμα (πουά)", "Μπλε με κίτρινα αστέρια"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η πουά φανέλα (Maillot à pois rouges) εισήχθη το 1975 με χορηγό τη σοκολατοποιία Poulain, της οποίας τα περιτυλίγματα είχαν χαρακτηριστικές κόκκινες βούλες.",
    "funFacts": [
      "Ο Γάλλος Ρισάρ Βιράνκ κατέχει το απόλυτο ρεκόρ έχοντας κερδίσει την πουά φανέλα 7 φορές.",
      "Βαθμοί για την κατάταξη των βουνών απονέμονται στις κορυφές των κατηγοριοποιημένων αναβάσεων (από 4η κατηγορία έως Hors Catégorie)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CF%8D%CF%81%CE%BF%CF%82_%CF%84%CE%B7%CF%82_%CE%93%CE%B1%CE%BB%CE%BB%CE%AF%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["polka-dot-jersey", "tour-de-france", "climbing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_104",
    "text": "Ποιος Αυστραλός τενίστας έγινε το 2001 ο νεότερος παίκτης στην ιστορία που έφτασε στο Νο. 1 της παγκόσμιας κατάταξης ATP σε ηλικία 20 ετών και 8 μηνών;",
    "answers": ["Πάτρικ Ράφτερ", "Μαρκ Φιλιππούσης", "Νικ Κύργιος", "Λέιτον Χιούιτ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Lleyton Hewitt κέρδισε το US Open το 2001 και το Wimbledon το 2002, διατηρώντας το ρεκόρ του νεότερου No. 1 μέχρι να το καταρρίψει ο Carlos Alcaraz το 2022.",
    "funFacts": [
      "Έμεινε παροιμιώδης για το μαχητικό του πνεύμα και τη χαρακτηριστική ιαχή 'Come on!' με το καπελάκι γυρισμένο ανάποδα.",
      "Οδήγησε την Αυστραλία στην κατάκτηση δύο τίτλων Davis Cup (1999, 2003)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AD%CE%B9%CF%84%CE%BF%CE%BD_%CE%A7%CE%B9%CE%BF%CF%8D%CE%B9%CF%84",
    "locale": "el-GR",
    "tags": ["lleyton-hewitt", "tennis-atp", "youngest-no1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_105",
    "text": "Από ποια απόσταση σε μέτρα εκτελείται το πέναλτι στην υδατοσφαίριση (πόλο);",
    "answers": ["5 μέτρα", "4 μέτρα", "6 μέτρα", "7 μέτρα"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο πόλο το πέναλτι εκτελείται από τη γραμμή των 5 μέτρων απευθείας προς την εστία χωρίς προσποίηση.",
    "funFacts": [
      "Ο εκτελεστής του πέναλτι πρέπει να σουτάρει με μία συνεχή κίνηση απευθείας προς το τέρμα με το σφύριγμα του διαιτητή.",
      "Ο τερματοφύλακας πρέπει να στέκεται πάνω στη γραμμή του τέρματος ανάμεσα στα δοκάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["water-polo-penalty", "rules", "5-meters"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_106",
    "text": "Ποιος προπονητής οδήγησε τους 'Bad Boys' Ντιτρόιτ Πίστονς σε δύο συνεχόμενα πρωταθλήματα NBA το 1989 και το 1990 και αργότερα καθοδήγησε την αυθεντική Dream Team;",
    "answers": ["Πατ Ράιλι", "Τσακ Ντέιλι", "Λένι Γουίλκενς", "Ντον Νέλσον"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Chuck Daly δημιούργησε την περίφημη σκληροτράχηλη ομάδα του Ντιτρόιτ με τους Isiah Thomas, Bill Laimbeer και Dennis Rodman.",
    "funFacts": [
      "Επινόησε τους περίφημους αμυντικούς 'Jordan Rules' για να περιορίσει τον Michael Jordan στα πλέι οφ.",
      "Ως προπονητής της Dream Team το 1992 στη Βαρκελώνη δεν κάλεσε ούτε ένα τάιμ-άουτ σε ολόκληρο το ολυμπιακό τουρνουά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%83%CE%B1%CE%BA_%CE%9D%CF%84%CE%AD%CE%B9%CE%BB%CE%B9",
    "locale": "el-GR",
    "tags": ["chuck-daly", "detroit-pistons", "bad-boys", "dream-team"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_107",
    "text": "Ποιο είναι παραδοσιακά το δέκατο και τελευταίο αγώνισμα στο οποίο διαγωνίζονται οι δεκαθλητές στο τέλος της 2ης ημέρας του δεκάθλου;",
    "answers": ["Ακοντισμός", "Άλμα επί κοντώ", "1.500 μέτρα", "110μ με εμπόδια"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο εξαντλητικός αγώνας των 1.500 μέτρων αποτελεί το τελευταίο αγώνισμα του δεκάθλου, όπου συχνά κρίνονται τα μετάλλια με βάση τη διαφορά χρόνου.",
    "funFacts": [
      "Παραδοσιακά, όλοι οι δεκαθλητές αγκαλιάζονται και κάνουν μαζί τον γύρο του θριάμβου μετά τον τερματισμό των 1.500 μέτρων ως ένδειξη αλληλοσεβασμού.",
      "Ο νικητής του δεκάθλου κερδίζει παραδοσιακά τον άτυπο τίτλο του 'Κορυφαίου Αθλητή του Κόσμου' (World's Greatest Athlete)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BA%CE%B1%CE%B8%CE%BB%CE%BF",
    "locale": "el-GR",
    "tags": ["decathlon", "1500m", "athletics-events"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_108",
    "text": "Ποιος Ιταλός κεντρικός αμυντικός κατέκτησε τη Χρυσή Μπάλα (Ballon d'Or) το 2006 μετά την αρχηγική του εμφάνιση στην κατάκτηση του Μουντιάλ από την Ιταλία;",
    "answers": ["Πάολο Μαλντίνι", "Αλεσάντρο Νέστα", "Τζόρτζιο Κιελίνι", "Φάμπιο Καναβάρο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Fabio Cannavaro είναι ένας από τους ελάχιστους καθαρόαιμους αμυντικούς στην ιστορία του ποδοσφαίρου που τιμήθηκαν με τη Χρυσή Μπάλα.",
    "funFacts": [
      "Με ύψος μόλις 1,76 μ., υπερίσχυε των ψηλότερων επιθετικών χάρη στο εξαιρετικό του timing και την εκρηκτικότητα στα άλματα.",
      "Αποκλήθηκε 'Il Muro di Berlino' (Το Τείχος του Βερολίνου) για τις ανυπέρβλητες εμφανίσεις του στα γήπεδα της Γερμανίας το 2006."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%AC%CE%BC%CF%80%CE%B9%CE%BF_%CE%9A%CE%B1%CE%BD%CE%B1%CE%B2%CE%AC%CF%81%CE%BF",
    "locale": "el-GR",
    "tags": ["cannavaro", "ballon-dor-2006", "italy-world-cup"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_109",
    "text": "Ποια Ουγγαρέζα κολυμβήτρια ('Iron Lady') κατέκτησε 3 χρυσά μετάλλια και ένα ασημένιο στους Ολυμπιακούς Αγώνες του Ρίο το 2016;",
    "answers": ["Κατίνκα Χόσου (Katinka Hosszú)", "Κρίστινα Έγκερσεγκι", "Μπογκλάρκα Κάπας", "Ζουζάνα Γιάκαμπος"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Katinka Hosszú κυριάρχησε στα αγωνίσματα μικτής ατομικής και υπτίου στο Ρίο καταρρίπτοντας μεταξύ άλλων το παγκόσμιο ρεκόρ στα 400μ μικτή κατά 2 δευτερόλεπτα.",
    "funFacts": [
      "Κέρδισε συνολικά 26 χρυσά μετάλλια σε Παγκόσμια Πρωταθλήματα (σε 50άρα και 25άρα πισίνα).",
      "Είναι η πρώτη κολυμβήτρια στην ιστορία που κατείχε ταυτόχρονα τα παγκόσμια ρεκόρ σε όλα τα αγωνίσματα μικτής ατομικής (200μ και 400μ σε μεγάλη και μικρή πισίνα, 100μ σε μικρή πισίνα)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%AF%CE%BD%CE%BA%CE%B1_%CE%A7%CF%8C%CF%83%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["katinka-hosszu", "iron-lady", "swimming", "rio-2016"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_110",
    "text": "Με ποια βρετανική ομάδα κατέκτησε ο Άιρτον Σένα και τα τρία παγκόσμια πρωταθλήματα Formula 1 της καριέρας του (1988, 1990, 1991);",
    "answers": ["Williams", "McLaren", "Lotus", "Benetton"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ayrton Senna μεγαλούργησε με τη θρυλική McLaren-Honda στα ασπροκόκκινα χρώματα, συνθέτοντας με τον Alain Prost ένα από τα πιο εκρηκτικά δίδυμα στην ιστορία του σπορ.",
    "funFacts": [
      "Το 1988 η McLaren-Honda κέρδισε τους 15 από τους 16 αγώνες της σεζόν (8 νίκες ο Senna και 7 ο Prost).",
      "Ο Senna πέτυχε συνολικά 35 νίκες σε Grand Prix αποκλειστικά με τα μονοθέσια της McLaren."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%B9%CF%81%CF%84%CE%BF%CE%BD_%CE%A3%CE%AD%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["senna-mclaren", "formula-1", "mclaren-honda"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('sports', 'medium', 3, questions)

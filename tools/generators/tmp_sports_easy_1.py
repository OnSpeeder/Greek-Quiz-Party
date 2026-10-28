# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "sports_easy_011",
    "text": "Πόσοι καλαθοσφαιριστές από κάθε ομάδα βρίσκονται ταυτόχρονα στο παρκέ κατά τη διάρκεια ενός αγώνα μπάσκετ;",
    "answers": ["5", "6", "4", "7"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Σε κάθε αγώνα καλαθοσφαίρισης, κάθε ομάδα αγωνίζεται με 5 παίκτες ταυτόχρονα στο γήπεδο.",
    "funFacts": [
      "Μια πλήρης ομάδα αποτελείται συνήθως από 12 παίκτες, με τους 7 να κάθονται στον πάγκο ως αναπληρωματικοί.",
      "Οι αλλαγές παικτών στο μπάσκετ είναι απεριόριστες κατά τη διάρκεια των διακοπών του αγώνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["basketball", "rules", "players"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_012",
    "text": "Πώς ονομάζεται το σκορ μηδέν (0) για έναν παίκτη στη βαθμολογία ενός γκέιμ στο τένις;",
    "answers": ["Nil", "Love", "Zero", "Fault"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Στο τένις, το μηδέν προφέρεται παραδοσιακά ως 'Love', πιθανώς από τη γαλλική λέξη 'l'oeuf' (το αυγό) λόγω του σχήματος του μηδενικού.",
    "funFacts": [
      "Η σειρά καταμέτρησης των πόντων σε ένα γκέιμ τένις είναι 15, 30, 40 και γκέιμ.",
      "Όταν το σκορ φτάσει στο 40-40, ονομάζεται 'deuce' (ισοπαλία) και απαιτούνται δύο συνεχόμενοι πόντοι για τη νίκη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B9%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["tennis", "scoring", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_013",
    "text": "Ποια είναι η επίσημη απόσταση του κλασικού αγωνίσματος του Μαραθωνίου δρόμου;",
    "answers": ["40 χιλιόμετρα", "50 χιλιόμετρα", "42,195 χιλιόμετρα", "38,5 χιλιόμετρα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η επίσημη απόσταση του Μαραθωνίου καθορίστηκε στους Ολυμπιακούς Αγώνες του Λονδίνου το 1908 σε 42,195 χιλιόμετρα (26 μίλια και 385 γιάρδες).",
    "funFacts": [
      "Η απόσταση ορίστηκε ώστε ο αγώνας να ξεκινήσει από το Κάστρο του Ουίνδσορ και να τερματίσει ακριβώς μπροστά στο βασιλικό θεωρείο του σταδίου White City.",
      "Ο αγώνας εμπνεύστηκε από τον αρχαίο Έλληνα οπλίτη-αγγελιοφόρο Φειδιππίδη, που έτρεξε από τον Μαραθώνα στην Αθήνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%B1%CE%B8%CF%8E%CE%BD%CE%B9%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["marathon", "athletics", "running"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_014",
    "text": "Ποια εθνική ομάδα έχει κατακτήσει τα περισσότερα Παγκόσμια Κύπελλα Ποδοσφαίρου (Μουντιάλ) στην ιστορία;",
    "answers": ["Γερμανία", "Ιταλία", "Αργεντινή", "Βραζιλία"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η Βραζιλία είναι η πιο επιτυχημένη ομάδα με 5 κατακτήσεις (1958, 1962, 1970, 1994 και 2002).",
    "funFacts": [
      "Η Βραζιλία είναι η μοναδική εθνική ομάδα που έχει συμμετάσχει σε όλα ανεξαιρέτως τα Παγκόσμια Κύπελλα από το 1930.",
      "Ακολουθούν η Γερμανία και η Ιταλία με 4 τρόπαια η καθεμία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%B3%CE%BA%CF%8C%CF%83%CE%BC%CE%B9%CE%BF_%CE%9A%CF%8D%CF%80%CE%B5%CE%BB%CE%BB%CE%BF_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["world-cup", "brazil", "football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_015",
    "text": "Σε ποια χώρα έχει την ιστορική της έδρα η διάσημη ομάδα της Formula 1, Scuderia Ferrari;",
    "answers": ["Στην Ιταλία", "Στη Γαλλία", "Στη Γερμανία", "Στο Ηνωμένο Βασίλειο"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η Scuderia Ferrari εδρεύει στο Μαρανέλο της Ιταλίας και αποτελεί τη μακροβιότερη ομάδα στην ιστορία της Formula 1.",
    "funFacts": [
      "Η Ferrari είναι η μοναδική ομάδα που συμμετέχει ανελλιπώς στο Παγκόσμιο Πρωτάθλημα Formula 1 από την ίδρυσή του το 1950.",
      "Το έμβλημα της ομάδας είναι το περίφημο 'Cavallino Rampante' (όρθιο αλογάκι) σε κίτρινο φόντο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%BA%CE%BF%CF%85%CE%BD%CF%84%CE%B5%CF%81%CE%AF%CE%B1_%CE%A6%CE%B5%CF%81%CF%81%CE%AC%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["formula-1", "ferrari", "motorsport"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_016",
    "text": "Πόσοι παίκτες από κάθε ομάδα αγωνίζονται ταυτόχρονα στο τερέν σε έναν αγώνα πετοσφαίρισης (βόλεϊ);",
    "answers": ["5", "6", "7", "8"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Στο παραδοσιακό βόλεϊ σάλας, κάθε ομάδα αγωνίζεται με 6 παίκτες εντός γηπέδου.",
    "funFacts": [
      "Στο μπιτς βόλεϊ (beach volley) οι ομάδες αποτελούνται από μόλις 2 παίκτες χωρίς δικαίωμα αλλαγών.",
      "Ο παίκτης που φοράει διαφορετική φανέλα και αγωνίζεται αποκλειστικά στην άμυνα ονομάζεται λίμπερο (libero)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["volleyball", "rules", "players"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_017",
    "text": "Πόσοι πολίστες από κάθε ομάδα βρίσκονται μέσα στο νερό κατά τη διάρκεια ενός αγώνα υδατοσφαίρισης (πόλο);",
    "answers": ["5", "6", "7", "8"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Κάθε ομάδα πόλο αγωνίζεται με 7 παίκτες (6 παίκτες πεδιάς και 1 τερματοφύλακα) μέσα στο νερό.",
    "funFacts": [
      "Οι παίκτες του πόλο δεν επιτρέπεται να ακουμπούν στον πυθμένα της πισίνας και μένουν στην επιφάνεια με την τεχνική του 'eggbeater kick'.",
      "Οι τερματοφύλακες φορούν σκουφάκι με τον αριθμό 1 (παραδοσιακά κόκκινου χρώματος)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["water-polo", "rules", "swimming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_018",
    "text": "Ποια ελληνική ομάδα κατέκτησε την κορυφή της Ευρώπης στο Final Four της EuroLeague στο Βερολίνο το 2024;",
    "answers": ["Ολυμπιακός", "ΑΕΚ", "ΠΑΟΚ", "Παναθηναϊκός"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Παναθηναϊκός νίκησε τη Ρεάλ Μαδρίτης στον τελικό του Βερολίνου το 2024 κατακτώντας το 7ο ευρωπαϊκό τρόπαιο της ιστορίας του.",
    "funFacts": [
      "Προπονητής της ομάδας σε αυτόν τον θρίαμβο ήταν ο Τούρκος τεχνικός Εργκίν Αταμάν.",
      "Πολυτιμότερος παίκτης (MVP) του Final Four αναδείχθηκε ο αρχηγός της ομάδας Κώστας Σλούκας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%BD%CE%B1%CE%B8%CE%B7%CE%BD%CE%B1%CF%8A%CE%BA%CF%8C%CF%82_(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["panathinaikos", "euroleague", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_019",
    "text": "Ποια κάρτα δείχνει ο διαιτητής σε έναν ποδοσφαιριστή για να τον αποβάλει άμεσα από τον αγώνα;",
    "answers": ["Κόκκινη κάρτα", "Κίτρινη κάρτα", "Μπλε κάρτα", "Πράσινη κάρτα"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η κόκκινη κάρτα σημαίνει άμεση αποβολή του ποδοσφαιριστή από το παιχνίδι, αφήνοντας την ομάδα του με έναν παίκτη λιγότερο.",
    "funFacts": [
      "Ένας παίκτης αποβάλλεται επίσης εάν δεχθεί δύο κίτρινες κάρτες στον ίδιο αγώνα.",
      "Οι πειθαρχικές κάρτες στο ποδόσφαιρο εισήχθησαν για πρώτη φορά στο Παγκόσμιο Κύπελλο του 1970 στο Μεξικό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%B7_%CE%BA%CE%AC%CF%81%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["football", "rules", "referee"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_020",
    "text": "Τι γεωμετρικό σχήμα έχει ο αγωνιστικός χώρος (ρινγκ) στην επαγγελματική πυγμαχία;",
    "answers": ["Κυκλικό", "Τετράγωνο", "Οκταγωνικό", "Τριγωνικό"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Παρά την ονομασία του ('ring', που σημαίνει δακτύλιος), το ρινγκ της πυγμαχίας είναι τετράγωνο και περιβάλλεται από τέσσερα σχοινιά.",
    "funFacts": [
      "Η ονομασία 'ρινγκ' προέρχεται από την εποχή που οι θεατές σχημάτιζαν κύκλο γύρω από τους μαχητές.",
      "Αντίθετα, στις μεικτές πολεμικές τέχνες (MMA / UFC) ο χώρος μάχης είναι συνήθως οκταγωνικός (Octagon)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%85%CE%B3%CE%BC%CE%B1%CF%87%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["boxing", "ring", "combat-sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_021",
    "text": "Πόσες βάσεις συνολικά πρέπει να πατήσει με τη σειρά ένας δρομέας στο μπέιζμπολ για να σημειώσει πόντο;",
    "answers": ["2 βάσεις", "3 βάσεις", "4 βάσεις", "5 βάσεις"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο επιτιθέμενος πρέπει να διασχίσει την 1η, τη 2η, την 3η βάση και να επιστρέψει στην κύρια βάση (home plate), δηλαδή συνολικά 4 βάσεις.",
    "funFacts": [
      "Όταν ένας παίκτης χτυπήσει τη μπάλα εκτός γηπέδου, κατοχυρώνεται αυτόματα 'home run' και διατρέχει τις 4 βάσεις χωρίς πίεση.",
      "Αν υπάρχουν ήδη συμπαίκτες και στις τρεις βάσεις, ένα home run ονομάζεται 'Grand Slam' και προσφέρει 4 πόντους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%AD%CE%B9%CE%B6%CE%BC%CF%80%CE%BF%CE%BB",
    "locale": "el-GR",
    "tags": ["baseball", "rules", "scoring"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_022",
    "text": "Ποιο στυλ κολύμβησης χαρακτηρίζεται από ταυτόχρονη κίνηση των χεριών πάνω από το νερό και κυματοειδή κλωτσιά δελφινιού;",
    "answers": ["Ύπτιο", "Πρόσθιο", "Ελεύθερο", "Πεταλούδα"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η πεταλούδα (butterfly) θεωρείται το πιο απαιτητικό σωματικά από τα τέσσερα επίσημα ολυμπιακά στυλ κολύμβησης.",
    "funFacts": [
      "Η πεταλούδα αναγνωρίστηκε ως ξεχωριστό ανεξάρτητο στυλ από τη FINA μόλις το 1952, καθώς πριν θεωρούνταν παραλλαγή του προσθίου.",
      "Το ταχύτερο στυλ κολύμβησης παραμένει το ελεύθερο (κρόουλ)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CE%BB%CF%8D%CE%BC%CE%B2%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["swimming", "butterfly", "styles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_023",
    "text": "Πώς ονομάζεται στο γκολφ η ολοκλήρωση μιας τρύπας με ένα χτύπημα λιγότερο από το καθορισμένο par;",
    "answers": ["Birdie", "Eagle", "Bogey", "Albatross"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το 'Birdie' δηλώνει σκορ ενός χτυπήματος κάτω από το par (παράδειγμα: 3 χτυπήματα σε τρύπα par-4).",
    "funFacts": [
      "Δύο χτυπήματα κάτω από το par ονομάζονται 'Eagle', ενώ ένα χτύπημα πάνω από το par λέγεται 'Bogey'.",
      "Ένα τυπικό πλήρες γήπεδο γκολφ αποτελείται από 18 τρύπες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%BF%CE%BB%CF%86",
    "locale": "el-GR",
    "tags": ["golf", "scoring", "terminology"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_024",
    "text": "Πώς ονομάζεται ο δίσκος από σκληρό καουτσούκ που χρησιμοποιείται αντί για μπάλα στο χόκεϊ επί πάγου;",
    "answers": ["Σφαίρα", "Πακ (Puck)", "Μπιλιάρδο", "Πίλος"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Στο χόκεϊ επί πάγου χρησιμοποιείται ένας κυλινδρικός μαύρος δίσκος από βουλκανισμένο καουτσούκ, γνωστός διεθνώς ως puck (πακ).",
    "funFacts": [
      "Πριν από τους αγώνες τα πακ καταψύχονται, ώστε να γλιστρούν ομαλά στον πάγο και να μην αναπηδούν υπερβολικά.",
      "Τα πακ μπορούν να αναπτύξουν ταχύτητες άνω των 160 χιλιομέτρων την ώρα μετά από δυνατό σουτ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CF%8C%CE%BA%CE%B5%CF%8A_%CE%B5%CF%80%CE%AF_%CF%80%CE%AC%CE%B3%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["ice-hockey", "puck", "equipment"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_025",
    "text": "Ποιος Έλληνας γυμναστής αποκαλείται 'Άρχοντας των Κρίκων' και κέρδισε το χρυσό μετάλλιο στους Ολυμπιακούς Αγώνες του Ρίο το 2016;",
    "answers": ["Δημοσθένης Ταμπάκος", "Βλάσης Μάρας", "Λευτέρης Πετρούνιας", "Ιωάννης Μελισσανίδης"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Λευτέρης Πετρούνιας έχει κυριαρχήσει στους κρίκους παγκοσμίως κατακτώντας ολυμπιακά μετάλλια σε τρεις συνεχόμενες διοργανώσεις (2016, 2021, 2024).",
    "funFacts": [
      "Είναι ο μοναδικός αθλητής στην ιστορία των κρίκων που έχει κατακτήσει έξι χρυσά μετάλλια σε Ευρωπαϊκά Πρωταθλήματα.",
      "Έχει δώσει το όνομά του σε επίσημη άσκηση κρίκων εγκεκριμένη από τη Διεθνή Ομοσπονδία Γυμναστικής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CF%85%CF%84%CE%AD%CF%81%CE%B7%CF%82_%CE%A0%CE%B5%CF%84%CF%81%CE%BF%CF%85%CE%BD%CE%B9%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["petrounias", "gymnastics", "olympics", "rings"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_026",
    "text": "Ποιος ποδοσφαιρικός σύλλογος έχει κατακτήσει τα περισσότερα τρόπαια UEFA Champions League (Κύπελλο Πρωταθλητριών);",
    "answers": ["Μπάγερν Μονάχου", "Μίλαν", "Λίβερπουλ", "Ρεάλ Μαδρίτης"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η Ρεάλ Μαδρίτης είναι η αδιαμφισβήτητη βασίλισσα της διοργάνωσης με 15 κατακτήσεις τροπαίων έως το 2024.",
    "funFacts": [
      "Κέρδισε τα πρώτα πέντε συνεχόμενα Κύπελλα Πρωταθλητριών στην ιστορία του θεσμού (1956–1960).",
      "Η δεύτερη πιο επιτυχημένη ομάδα είναι η ιταλική Μίλαν με 7 τίτλους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B5%CE%AC%CE%BB_%CE%9C%CE%B1%CE%B4%CF%81%CE%AF%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["champions-league", "real-madrid", "football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_027",
    "text": "Πόσοι αλληλένδετοι κύκλοι (κρίκοι) απεικονίζονται στη σημαία των Ολυμπιακών Αγώνων;",
    "answers": ["5 κύκλοι", "4 κύκλοι", "6 κύκλοι", "7 κύκλοι"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Οι 5 ολυμπιακοί κύκλοι συμβολίζουν την ένωση των πέντε ηπείρων της Γης μέσα από το αθλητικό ιδεώδες.",
    "funFacts": [
      "Τα πέντε χρώματα (μπλε, κίτρινο, μαύρο, πράσινο, κόκκινο) μαζί με το λευκό φόντο επιλέχθηκαν γιατί τουλάχιστον ένα εξ αυτών υπάρχει στη σημαία κάθε χώρας του κόσμου.",
      "Το ολυμπιακό σύμβολο σχεδιάστηκε το 1913 από τον βαρόνο Πιερ ντε Κουμπερτέν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%B1%CE%B3%CF%8E%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["olympics", "symbol", "rings"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_028",
    "text": "Με ποια ομάδα του NBA αναδείχθηκε πρωταθλητής το 2021 ο Γιάννης Αντετοκούνμπο;",
    "answers": ["Λος Άντζελες Λέικερς", "Μιλγουόκι Μπακς", "Μπόστον Σέλτικς", "Γκόλντεν Στέιτ Ουόριορς"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο 'Greek Freak' οδήγησε τους Milwaukee Bucks στον πρώτο τους τίτλο NBA μετά από 50 χρόνια, κερδίζοντας και το βραβείο MVP των τελικών.",
    "funFacts": [
      "Στον καθοριστικό έκτο αγώνα των τελικών εναντίον των Φοίνιξ Σανς σημείωσε 50 πόντους.",
      "Έχει αναδειχθεί δύο συνεχόμενες χρονιές πολυτιμότερος παίκτης (MVP) της κανονικής περιόδου του NBA (2019, 2020)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%91%CE%BD%CF%84%CE%B5%CF%84%CE%BF%CE%BA%CE%BF%CF%8D%CE%BD%CE%BC%CF%80%CE%BF",
    "locale": "el-GR",
    "tags": ["antetokounmpo", "nba", "bucks", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_029",
    "text": "Ποιο είναι το επίσημο όνομα του αθλήματος που παίζεται με μικρές ρακέτες και ελαφρύ μπαλάκι πάνω σε ειδικό τραπέζι;",
    "answers": ["Μπάντμιντον", "Σκουός", "Επιτραπέζια αντισφαίριση", "Μπόουλινγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η επιτραπέζια αντισφαίριση είναι η επίσημη ονομασία του δημοφιλούς αθλήματος που είναι ευρέως γνωστό ως πινγκ πονγκ.",
    "funFacts": [
      "Έγινε ολυμπιακό άθλημα στους Αγώνες της Σεούλ το 1988.",
      "Το μπαλάκι είναι κούφιο, κατασκευασμένο από πλαστικό (παλαιότερα κυτταρινοειδές) και ζυγίζει μόλις 2,7 γραμμάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%84%CF%81%CE%B1%CF%80%CE%AD%CE%B6%CE%B9%CE%B1_%CE%B1%CE%BD%CF%84%CE%B9%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["table-tennis", "ping-pong", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_030",
    "text": "Από ποια απόσταση σε μέτρα εκτελείται το πέναλτι στο ποδόσφαιρο;",
    "answers": ["9 μέτρα", "13 μέτρα", "15 μέτρα", "11 μέτρα"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το σημείο του πέναλτι απέχει ακριβώς 11 μέτρα (12 γιάρδες) από τη γραμμή τέρματος.",
    "funFacts": [
      "Στην Ελλάδα η λέξη πέναλτι αναφέρεται συχνά στην καθομιλουμένη ως 'η άσπρη βούλα'.",
      "Κατά την εκτέλεση του πέναλτι, όλοι οι άλλοι παίκτες εκτός του εκτελεστή και του τερματοφύλακα πρέπει να βρίσκονται έξω από τη μεγάλη περιοχή και τουλάχιστον 9,15 μέτρα μακριά από τη μπάλα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AD%CE%BD%CE%B1%CE%BB%CF%84%CE%B9_(%CF%80%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%BF)",
    "locale": "el-GR",
    "tags": ["penalty", "football", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_031",
    "text": "Τι χρώμα φανέλα φοράει ο προπορευόμενος αθλητής στη γενική κατάταξη του Γύρου της Γαλλίας (Tour de France);",
    "answers": ["Κίτρινη", "Πράσινη", "Κόκκινη", "Ροζ"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η κίτρινη φανέλα (Maillot Jaune) απονέμεται στον ποδηλάτη με τον ταχύτερο συνολικό χρόνο στον Γύρο της Γαλλίας.",
    "funFacts": [
      "Το κίτρινο χρώμα επιλέχθηκε επειδή η εφημερίδα L'Auto, που δημιούργησε τον αγώνα το 1903, τυπωνόταν σε κίτρινο χαρτί.",
      "Στον Γύρο της Ιταλίας (Giro d'Italia) ο αντίστοιχος πρωτοπόρος φοράει ροζ φανέλα (Maglia Rosa)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CF%8D%CF%81%CE%BF%CF%82_%CF%84%CE%B7%CF%82_%CE%93%CE%B1%CE%BB%CE%BB%CE%AF%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["tour-de-france", "cycling", "jersey"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_032",
    "text": "Πώς ονομάζεται στο τένις ένα σερβίς που καταλήγει άμεσα σε πόντο χωρίς ο αντίπαλος να ακουμπήσει καν τη μπάλα;",
    "answers": ["Σμας", "Άσος (Ace)", "Βολέ", "Λομπ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο άσος (ace) είναι ένα έγκυρο σερβίς το οποίο ο αντίπαλος παίκτης δεν καταφέρνει να αγγίξει με τη ρακέτα του.",
    "funFacts": [
      "Τα σερβίς κορυφαίων επαγγελματιών τενιστών ξεπερνούν συχνά τα 220 έως 240 χιλιόμετρα την ώρα.",
      "Αν το σερβίς ακουμπήσει στο φιλέ και καταλήξει στην έγκυρη περιοχή, ονομάζεται 'let' και επαναλαμβάνεται."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B9%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["tennis", "ace", "serve"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_033",
    "text": "Ποιο χρώμα ζώνης συμβολίζει παραδοσιακά τον υψηλότερο βαθμό επάρκειας (επίπεδο δασκάλου) στις ανατολικές πολεμικές τέχνες (όπως το τζούντο και το καράτε);",
    "answers": ["Άσπρη", "Κίτρινη", "Μαύρη", "Πράσινη"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η μαύρη ζώνη (dan) απονέμεται σε αθλητές που έχουν κατακτήσει τις βασικές τεχνικές και αρχές της τέχνης σε υψηλό επίπεδο.",
    "funFacts": [
      "Το σύστημα των χρωματιστών ζωνών επινοήθηκε στα τέλη του 19ου αιώνα από τον ιδρυτή του τζούντο, Τζίγκορο Κάνο.",
      "Οι αρχάριοι αθλητές ξεκινούν παραδοσιακά με τη λευκή ζώνη, που συμβολίζει την αγνότητα και την έλλειψη προηγούμενης γνώσης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%8D%CE%BD%CF%84%CE%BF",
    "locale": "el-GR",
    "tags": ["martial-arts", "judo", "karate", "belts"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_034",
    "text": "Σε ποιο άθλημα διακρίνεται διεθνώς ο κορυφαίος Έλληνας πρωταθλητής Στέφανος Τσιτσιπάς;",
    "answers": ["Μπάσκετ", "Στίβος", "Κολύμβηση", "Τένις"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Στέφανος Τσιτσιπάς είναι επαγγελματίας τενίστας που έφτασε μέχρι το No. 3 της παγκόσμιας κατάταξης ATP.",
    "funFacts": [
      "Το 2019 κατέκτησε το ATP Finals στο Λονδίνο, σημειώνοντας τη μεγαλύτερη επιτυχία στην ιστορία της ελληνικής αντισφαίρισης.",
      "Έχει φτάσει σε δύο τελικούς Grand Slam στο μονό ανδρών (Roland Garros 2021 και Australian Open 2023)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AD%CF%86%CE%B1%CE%BD%CE%BF%CF%82_%CE%A4%CF%83%CE%B9%CF%84%CF%83%CE%B9%CF%80%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["tsitsipas", "tennis", "atp"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_035",
    "text": "Σε ποιο αγώνισμα του στίβου αναδείχθηκε χρυσός Ολυμπιονίκης στο Τόκιο (2021) και στο Παρίσι (2024) ο Μίλτος Τεντόγλου;",
    "answers": ["Άλμα εις μήκος", "Άλμα επί κοντώ", "Άλμα εις ύψος", "Τριπλούν"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Μιλτιάδης Τεντόγλου αγωνίζεται στο άλμα εις μήκος και είναι ένας από τους κορυφαίους άλτες όλων των εποχών.",
    "funFacts": [
      "Στους Ολυμπιακούς Αγώνες του Τόκιο κατέκτησε το χρυσό μετάλλιο με άλμα στα 8,41 μέτρα στην τελευταία του προσπάθεια.",
      "Κατάγεται από τα Γρεβενά και ξεκίνησε τον αθλητισμό κάνοντας παρκούρ στην εφηβεία του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%BB%CF%84%CE%B9%CE%AC%CE%B4%CE%B7%CF%82_%CE%A4%CE%B5%CE%BD%CF%84%CF%8C%CE%B3%CE%BB%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["tentoglou", "long-jump", "athletics", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_036",
    "text": "Σε ποια χώρα της Ασίας το κρίκετ αποτελεί το μακράν πιο δημοφιλές και λαοφιλές άθλημα;",
    "answers": ["Στην Ιαπωνία", "Στην Ινδία", "Στη Νότια Κορέα", "Στην Κίνα"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Στην Ινδία το κρίκετ έχει στάτους σχεδόν 'θρησκείας', με το εγχώριο πρωτάθλημα IPL να συγκεντρώνει εκατοντάδες εκατομμύρια τηλεθεατές.",
    "funFacts": [
      "Το κρίκετ εισήχθη στην Ινδία από τους Βρετανούς κατά την περίοδο της αποικιοκρατίας.",
      "Το στάδιο Narendra Modi στο Αχμενταμπάντ της Ινδίας είναι το μεγαλύτερο στάδιο κρίκετ στον κόσμο με χωρητικότητα 132.000 θεατών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%81%CE%AF%CE%BA%CE%B5%CF%84",
    "locale": "el-GR",
    "tags": ["cricket", "india", "sports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_037",
    "text": "Τι χρώμα έχει ο κεντρικός κύκλος (διάμετρος μέγιστης βαθμολογίας) στον στόχο της τοξοβολίας;",
    "answers": ["Μαύρο", "Μπλε", "Κίτρινο", "Κόκκινο"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο κεντρικός κύκλος του στόχου στην τοξοβολία είναι κίτρινος (χρυσός) και αποφέρει τους μέγιστους βαθμούς (9 ή 10 πόντους).",
    "funFacts": [
      "Οι δακτύλιοι του στόχου από έξω προς τα μέσα είναι: λευκός, μαύρος, μπλε, κόκκινος και κίτρινος στο κέντρο.",
      "Η τοξοβολία υπήρξε ολυμπιακό άθλημα στις αρχές του 20ού αιώνα και επανήλθε οριστικά στους Αγώνες του Μονάχου το 1972."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF%CE%BE%CE%BF%CE%B2%CE%BF%CE%BB%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["archery", "target", "bullseye"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_038",
    "text": "Ποιος Βρετανός πιλότος μοιράζεται το ιστορικό ρεκόρ των 7 παγκόσμιων πρωταθλημάτων Formula 1 μαζί με τον Μίχαελ Σουμάχερ;",
    "answers": ["Σεμπάστιαν Φέτελ", "Φερνάντο Αλόνσο", "Μαξ Φερστάπεν", "Λιούις Χάμιλτον"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Lewis Hamilton έχει κατακτήσει 7 Παγκόσμια Πρωταθλήματα Οδηγών (1 με τη McLaren και 6 με τη Mercedes).",
    "funFacts": [
      "Κατέχει το απόλυτο ρεκόρ για τις περισσότερες νίκες σε Grand Prix (πάνω από 100) στην ιστορία της Formula 1.",
      "Χρίστηκε ιππότης από τη βρετανική βασιλική οικογένεια στα τέλη του 2021."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B9%CE%BF%CF%8D%CE%B9%CF%82_%CE%A7%CE%AC%CE%BC%CE%B9%CE%BB%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["hamilton", "formula-1", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_039",
    "text": "Πόσοι παίκτες από κάθε ομάδα αγωνίζονται ταυτόχρονα στο γήπεδο σε έναν αγώνα χειροσφαίρισης (χάντμπολ);",
    "answers": ["7", "5", "6", "8"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Κάθε ομάδα χάντμπολ παρατάσσει 7 παίκτες (6 παίκτες γηπέδου και 1 τερματοφύλακα).",
    "funFacts": [
      "Ένας αγώνας χάντμπολ αποτελείται από δύο ημίχρονα διάρκειας 30 λεπτών το καθένα.",
      "Οι παίκτες επιτρέπεται να κάνουν μέχρι 3 βήματα κρατώντας τη μπάλα χωρίς να την αναπηδήσουν στο έδαφος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CF%81%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["handball", "rules", "players"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_040",
    "text": "Ποια είναι η κορυφαία ευρωπαϊκή ποδοσφαιρική διοργάνωση εθνικών ομάδων που διεξάγεται κάθε 4 χρόνια από την UEFA;",
    "answers": ["Copa America", "Euro (Ευρωπαϊκό Πρωτάθλημα)", "Copa Libertadores", "Asian Cup"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το Ευρωπαϊκό Πρωτάθλημα Ποδοσφαίρου (γνωστό ως Euro) συγκεντρώνει τις κορυφαίες εθνικές ομάδες της Ευρώπης κάθε τέσσερα χρόνια.",
    "funFacts": [
      "Η πρώτη διοργάνωση πραγματοποιήθηκε το 1960 στη Γαλλία και κατακτήθηκε από τη Σοβιετική Ένωση.",
      "Η Ισπανία είναι η πολυνίκης του θεσμού έχοντας κατακτήσει 4 φορές το τρόπαιο (1964, 2008, 2012, 2024)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CF%81%CF%89%CF%80%CE%B1%CF%8A%CE%BA%CF%8C_%CE%A0%CF%81%CF%89%CF%84%CE%AC%CE%B8%CE%BB%CE%B7%CE%BC%CE%B1_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["euro", "football", "uefa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_041",
    "text": "Ποιος θρύλος των LA Lakers απεικονίζεται στη διάσημη λευκή σιλουέτα του επίσημου λογότυπου του NBA;",
    "answers": ["Μάικλ Τζόρνταν", "Καρίμ Αμπντούλ-Τζαμπάρ", "Τζέρι Ουέστ", "Μάτζικ Τζόνσον"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η σιλουέτα του Jerry West, σχεδιασμένη το 1969 από τον Alan Siegel, αποτελεί το παγκοσμίως αναγνωρίσιμο σήμα του NBA.",
    "funFacts": [
      "Λόγω αυτής της φιγούρας, ο Jerry West απέκτησε στον αθλητικό κόσμο το προσωνύμιο 'The Logo'.",
      "Είναι ένας από τους ελάχιστους παίκτες που κέρδισε το βραβείο MVP των Τελικών του NBA (1969) παρότι η ομάδα του ηττήθηκε στη σειρά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CF%81%CE%B9_%CE%9F%CF%85%CE%AD%CF%83%CF%84",
    "locale": "el-GR",
    "tags": ["nba", "logo", "jerry-west", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_042",
    "text": "Ποιο χειμερινό ολυμπιακό άθλημα συνδυάζει το σκι αντοχής (cross-country) με τη σκοποβολή με τουφέκι;",
    "answers": ["Κέρλινγκ", "Μπόμπσλεϊ", "Άλμα με σκι", "Δίαθλο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το δίαθλο (biathlon) αποτελεί συνδυασμό σκι αντοχής και βολών σκοποβολής σε συγκεκριμένες στάσεις (πρηνηδόν και ορθίως).",
    "funFacts": [
      "Κάθε άστοχη βολή στη σκοποβολή επιφέρει ποινή ενός γύρου (150 μέτρα) στον ειδικό γύρο ποινής ή προσθήκη ενός λεπτού στον συνολικό χρόνο.",
      "Οι ρίζες του αθλήματος ανάγονται στις στρατιωτικές ασκήσεις περιπολίας των σκανδιναβικών χωρών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AF%CE%B1%CE%B8%CE%BB%CE%BF",
    "locale": "el-GR",
    "tags": ["biathlon", "winter-sports", "skiing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_043",
    "text": "Πώς ονομάζεται στο μπόουλινγκ όταν ένας παίκτης ρίξει και τις 10 κορίνες με την πρώτη του μπαλιά;",
    "answers": ["Strike", "Spare", "Split", "Turkey"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το 'Strike' (συμβολίζεται με ένα 'X') επιτυγχάνεται όταν καταρρίπτονται και οι 10 κορίνες με το πρώτο χτύπημα του πλαισίου (frame).",
    "funFacts": [
      "Αν ο παίκτης ρίξει τις εναπομείνασες κορίνες με τη δεύτερη μπαλιά του, αυτό ονομάζεται 'Spare' (συμβολίζεται με '/').",
      "Τρία συνεχόμενα strikes σε έναν αγώνα μπόουλινγκ αποκαλούνται παραδοσιακά 'Turkey'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%8C%CE%BF%CF%85%CE%BB%CE%B9%CE%BD%CE%B3%CE%BA",
    "locale": "el-GR",
    "tags": ["bowling", "strike", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_044",
    "text": "Τι σχήμα έχει η μπάλα που χρησιμοποιείται στο άθλημα του ράγκμπι;",
    "answers": ["Τέλεια σφαιρικό", "Ωοειδές (ελλειψοειδές)", "Κυβικό", "Πυραμιδοειδές"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η μπάλα του ράγκμπι είναι ωοειδής, γεγονός που διευκολύνει το κράτημα με τα χέρια αλλά προκαλεί απρόβλεπτες αναπηδήσεις στο έδαφος.",
    "funFacts": [
      "Αρχικά οι μπάλες ράγκμπι κατασκευάζονταν από ουροδόχους κύστεις χοίρων καλυμμένες με δέρμα.",
      "Στο ράγκμπι οι πάσες με τα χέρια επιτρέπεται να εκτελούνται μόνο προς τα πίσω ή παράλληλα, ποτέ προς τα εμπρός."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AC%CE%B3%CE%BA%CE%BC%CF%80%CE%B9",
    "locale": "el-GR",
    "tags": ["rugby", "ball", "equipment"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_045",
    "text": "Με ποια ομάδα της Θεσσαλονίκης κατέκτησε 8 πρωταθλήματα Ελλάδας τη δεκαετία του '80 και του '90 ο ανυπέρβλητος Νίκος Γκάλης;",
    "answers": ["ΠΑΟΚ", "Ηρακλής", "Άρης", "Απόλλων Καλαμαριάς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Νίκος Γκάλης μεγαλούργησε με τη φανέλα του Άρη Θεσσαλονίκης δημιουργώντας τη θρυλική ομάδα των τριών Final Four.",
    "funFacts": [
      "Το 1987 οδήγησε την Εθνική Ελλάδας στην ιστορική κατάκτηση του Ευρωμπάσκετ στο Στάδιο Ειρήνης και Φιλίας.",
      "Είναι μέλος του Naismith Memorial Basketball Hall of Fame στις Ηνωμένες Πολιτείες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CF%82_%CE%93%CE%BA%CE%AC%CE%BB%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["galis", "aris", "basketball", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_046",
    "text": "Ποιος είναι ο μοναδικός παίκτης σε μια ομάδα ποδοσφαίρου που επιτρέπεται να αγγίξει τη μπάλα με τα χέρια εντός παιδιάς (στη μεγάλη του περιοχή);",
    "answers": ["Ο κεντρικός αμυντικός", "Ο αρχηγός της ομάδας", "Ο σέντερ φορ", "Ο τερματοφύλακας"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο τερματοφύλακας είναι ο μόνος παίκτης που μπορεί νόμιμα να χρησιμοποιήσει τα χέρια του μέσα στη δική του περιοχή πέναλτι.",
    "funFacts": [
      "Αν συμπαίκτης του τού επιστρέψει εσκεμμένα τη μπάλα με το πόδι, ο τερματοφύλακας δεν επιτρέπεται να την πιάσει με τα χέρια (κανονισμός back-pass).",
      "Ο τερματοφύλακας υποχρεούται να φορά φανέλα με διαφορετικό χρώμα από τους συμπαίκτες του και τον διαιτητή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CF%81%CE%BC%CE%B1%CF%84%CE%BF%CF%86%CF%8D%CE%BB%CE%B1%CE%BA%CE%B1%CF%82_(%CF%80%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%BF)",
    "locale": "el-GR",
    "tags": ["goalkeeper", "football", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_047",
    "text": "Πώς ονομάζεται το αντικείμενο με τα φτερά που χτυπούν οι παίκτες πάνω από το φιλέ στο μπάντμιντον;",
    "answers": ["Φτερωτό (Shuttlecock)", "Μπαλάκι", "Δίσκος", "Πούλια"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Στο μπάντμιντον χρησιμοποιείται το shuttlecock (φτερωτό), το οποίο αποτελείται από κώνο με 16 φτερά χήνας στερεωμένα σε φελλό.",
    "funFacts": [
      "Τα επίσημα φτερωτά κατασκευάζονται κατά προτίμηση αποκλειστικά από φτερά της αριστερής φτερούγας χήνας για τέλεια αεροδυναμική περιστροφή.",
      "Ένα δυνατό χτύπημα στο μπάντμιντον (smash) μπορεί να ξεπεράσει σε αρχική ταχύτητα τα 400 χιλιόμετρα την ώρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B9%CF%80%CF%84%CE%AD%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["badminton", "shuttlecock", "equipment"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_048",
    "text": "Σε ποια πόλη διεξήχθησαν οι Θερινοί Ολυμπιακοί Αγώνες του 2004, επιστρέφοντας στη γενέτειρά τους;",
    "answers": ["Στο Σίδνεϊ", "Στην Αθήνα", "Στο Πεκίνο", "Στο Λονδίνο"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η Αθήνα φιλοξένησε τους 28ους Θερινούς Ολυμπιακούς Αγώνες τον Αύγουστο του 2004 με το σύνθημα 'Καλώς ήρθατε σπίτι'.",
    "funFacts": [
      "Στους Αγώνες της Αθήνας το 2004 συμμετείχαν 10.625 αθλητές από 201 χώρες.",
      "Η τελετή έναρξης που σκηνοθέτησε ο Δημήτρης Παπαϊωάννου απέσπασε διθυραμβικές κριτικές παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_2004",
    "locale": "el-GR",
    "tags": ["athens-2004", "olympics", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_049",
    "text": "Πόσα μέτρα είναι το μήκος ενός πλήρους γύρου στον εσωτερικό διάδρομο ενός τυπικού υπαίθριου ολυμπιακού σταδίου στίβου;",
    "answers": ["200 μέτρα", "300 μέτρα", "400 μέτρα", "500 μέτρα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο εσωτερικός διάδρομος (διάδρομος 1) ενός πρότυπου στίβου έχει επίσημο μήκος ακριβώς 400 μέτρα.",
    "funFacts": [
      "Ένα τυπικό στάδιο στίβου περιλαμβάνει συνήθως 8 ή 9 διαδρόμους (κουλουάρ).",
      "Στον κλειστό στίβο, ο αντίστοιχος κανονικός γύρος έχει μήκος 200 μέτρα με κεκλιμένες στροφές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AF%CE%B2%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["track-and-field", "athletics", "distance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_050",
    "text": "Σε ποιο ομαδικό άθλημα ο τελικός αγώνας για την ανάδειξη του πρωταθλητή στις ΗΠΑ ονομάζεται 'Super Bowl';",
    "answers": ["Μπέιζμπολ", "Μπάσκετ", "Χόκεϊ επί πάγου", "Αμερικανικό ποδόσφαιρο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το Super Bowl είναι ο ετήσιος τελικός αγώνας του πρωταθλήματος NFL (National Football League) στο αμερικανικό ποδόσφαιρο.",
    "funFacts": [
      "Αποτελεί το πιο προβεβλημένο τηλεοπτικό γεγονός στις ΗΠΑ, διάσημο τόσο για τον αγώνα όσο και για το μουσικό Halftime Show.",
      "Οι τηλεοπτικές διαφημίσεις 30 δευτερολέπτων κατά τη διάρκεια του Super Bowl κοστίζουν πάνω από 7 εκατομμύρια δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%BF%CF%8D%CF%80%CE%B5%CF%81_%CE%9C%CF%80%CE%BF%CE%BF%CF%85%CE%BB",
    "locale": "el-GR",
    "tags": ["super-bowl", "nfl", "american-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_051",
    "text": "Πόσα τετράγωνα συνολικά έχει μια κανονική σκακιέρα στο σκάκι;",
    "answers": ["64", "32", "81", "100"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η σκακιέρα αποτελείται από πλέγμα 8x8 τετραγώνων, άρα έχει συνολικά 64 τετράγωνα (32 λευκά και 32 μαύρα).",
    "funFacts": [
      "Κάθε παίκτης ξεκινά την παρτίδα με 16 πιόνια: 8 πιόνια (στρατιώτες), 2 πύργους, 2 ίππους, 2 αξιωματικούς, 1 βασίλισσα και 1 βασιλιά.",
      "Η σκακιέρα τοποθετείται πάντα έτσι ώστε το δεξί γωνιακό τετράγωνο κάθε παίκτη να είναι λευκό ('λευκό στα δεξιά')."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%BA%CE%AC%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["chess", "board", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_052",
    "text": "Ποιος θρυλικός Έλληνας αρσιβαρίστας κατέκτησε τρία χρυσά ολυμπιακά μετάλλια (1992, 1996, 2000) και ένα χάλκινο (2004);",
    "answers": ["Κάχι Καχιασβίλι", "Πύρρος Δήμας", "Βαλέριος Λεωνίδης", "Λεωνίδας Σαμπάνης"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Ο Πύρρος Δήμας είναι ένας από τους σπουδαιότερους αρσιβαρίστες όλων των εποχών και κορυφαίος Έλληνας Ολυμπιονίκης.",
    "funFacts": [
      "Στους Ολυμπιακούς Αγώνες της Βαρκελώνης το 1992 φώναξε το ιστορικό 'Για την Ελλάδα!' σηκώνοντας τα βάρη.",
      "Στην τελετή λήξης της Αθήνας το 2004 αποθεώθηκε όρθιος από δεκάδες χιλιάδες θεατές επί πολλά λεπτά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%8D%CF%81%CF%81%CE%BF%CF%82_%CE%94%CE%AE%CE%BC%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["pyrros-dimas", "weightlifting", "olympics", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_053",
    "text": "Τι σηματοδοτεί η καρό ασπρόμαυρη σημαία που ανεμίζει στον τερματισμό ενός αγώνα Formula 1;",
    "answers": [
      "Είσοδος του αυτοκινήτου ασφαλείας",
      "Επικίνδυνο ατύχημα στην πίστα",
      "Την ολοκλήρωση (τέλος) του αγώνα",
      "Ακύρωση του προπορευόμενου πιλότου"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η καρό σημαία (chequered flag) κυματίζει πάνω από τη γραμμή τερματισμού για να δηλώσει το τέλος του αγώνα.",
    "funFacts": [
      "Ο πρώτος οδηγός που περνά την καρό σημαία αφού συμπληρωθούν όλοι οι προγραμματισμένοι γύροι είναι ο νικητής.",
      "Η κίτρινη σημαία υποδεικνύει κίνδυνο στην πίστα και απαγορεύει τις προσπεράσεις."
    ],
    "source": "https://el.wikipedia.org/wiki/Formula_1",
    "locale": "el-GR",
    "tags": ["formula-1", "flags", "racing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_054",
    "text": "Σε ποιον χώρο διεξάγονται οι επίσημοι αγώνες του αθλήματος της υδατοσφαίρισης (πόλο);",
    "answers": ["Στη θάλασσα", "Σε ποτάμι", "Σε λίμνη", "Σε πισίνα κολυμβητηρίου"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η σύγχρονη υδατοσφαίριση διεξάγεται αποκλειστικά σε ειδικά διαμορφωμένες κολυμβητικές δεξαμενές (πισίνες) ελάχιστου βάθους 1,80-2,00 μέτρων.",
    "funFacts": [
      "Στα τέλη του 19ου αιώνα, όταν πρωτοξεκίνησε το άθλημα στη Μεγάλη Βρετανία, παιζόταν σε ποτάμια και λίμνες.",
      "Οι διαστάσεις του αγωνιστικού χώρου για τους άνδρες είναι 30 μέτρα μήκος και 20 μέτρα πλάτος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["water-polo", "pool", "swimming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_055",
    "text": "Σε ποιο άθλημα διαπρέπει η Ελληνίδα πρωταθλήτρια Μαρία Σάκκαρη φτάνοντας στο Top-3 της παγκόσμιας κατάταξης;",
    "answers": ["Τένις", "Κολύμβηση", "Στίβος", "Ενόργανη γυμναστική"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Η Μαρία Σάκκαρη είναι κορυφαία Ελληνίδα επαγγελματίας αντισφαιρίστρια της WTA.",
    "funFacts": [
      "Έφτασε στα ημιτελικά δύο τουρνουά Grand Slam το 2021 (Roland Garros και US Open).",
      "Η μητέρα της, Αγγελική Κανελλοπούλου, υπήρξε επίσης σπουδαία πρωταθλήτρια του τένις στις δεκαετίες του '70 και '80."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AF%CE%B1_%CE%A3%CE%AC%CE%BA%CE%BA%CE%B1%CF%81%CE%B7",
    "locale": "el-GR",
    "tags": ["sakkari", "tennis", "wta"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_056",
    "text": "Ποια είναι η επίσημη μέγιστη διάρκεια της ανάπαυλας του ημιχρόνου σε έναν κανονικό ποδοσφαιρικό αγώνα;",
    "answers": ["10 λεπτά", "15 λεπτά", "20 λεπτά", "5 λεπτά"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Σύμφωνα με τους κανονισμούς της IFAB/FIFA, το διάλειμμα του ημιχρόνου δεν μπορεί να υπερβαίνει τα 15 λεπτά.",
    "funFacts": [
      "Σε περιπτώσεις ακραίας ζέστης, ο διαιτητής μπορεί επίσης να επιτρέψει σύντομα διαλείμματα δροσισμού (cooling breaks) διάρκειας 1-3 λεπτών.",
      "Αν ο αγώνας οδηγηθεί σε παράταση, το διάλειμμα μεταξύ των δύο ημιχρόνων της παράτασης διαρκεί μόλις 1-5 λεπτά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%BF",
    "locale": "el-GR",
    "tags": ["football", "rules", "halftime"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_057",
    "text": "Σε ποιο ύψος από το έδαφος βρίσκεται το στεφάνι της μπασκέτας σε έναν επίσημο αγώνα καλαθοσφαίρισης;",
    "answers": ["2,85 μέτρα", "3,50 μέτρα", "3,05 μέτρα", "2,60 μέτρα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το επίσημο ύψος της στεφάνης είναι ακριβώς 3,05 μέτρα (ή 10 πόδια στο αγγλοσαξονικό σύστημα).",
    "funFacts": [
      "Το ύψος των 10 ποδιών ορίστηκε το 1891 από τον James Naismith επειδή σε αυτό το ακριβές ύψος βρισκόταν το κιγκλίδωμα του γυμναστηρίου όπου κάρφωσε τα πρώτα καλάθια.",
      "Η διάμετρος του στεφανιού της μπασκέτας είναι ακριβώς 45 εκατοστά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["basketball", "hoop", "height", "rules"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_058",
    "text": "Ποια είναι η ελληνική απόδοση του κλασικού λατινικού ολυμπιακού συνθήματος 'Citius, Altius, Fortius';",
    "answers": [
      "Ειρήνη, Φιλία, Συναδέλφωση",
      "Νους υγιής εν σώματι υγιεί",
      "Πάντοτε ευ αγωνίζεσθαι",
      "Ταχύτερα, Ψηλότερα, Δυνατότερα"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το ιστορικό ολυμπιακό σύνθημα 'Citius, Altius, Fortius' σημαίνει 'Ταχύτερα, Ψηλότερα, Δυνατότερα' (το 2021 προστέθηκε και η λέξη 'Communiter' - 'Μαζί').",
    "funFacts": [
      "Η φράση προτάθηκε από τον Δομινικανό μοναχό Ανρί Ντιντόν και υιοθετήθηκε από τον Πιερ ντε Κουμπερτέν κατά την ίδρυση της ΔΟΕ το 1894.",
      "Το σύνθημα ενθαρρύνει τους αθλητές να ξεπερνούν διαρκώς τα ανθρώπινα όρια με ευγενή άμιλλα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%B1%CE%B3%CF%8E%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["olympics", "motto", "tradition"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_059",
    "text": "Ποιο είναι το μέγιστο δυνατό σκορ που μπορεί να πετύχει ένας παίκτης με 3 βελάκια σε έναν γύρο στα βελάκια (darts);",
    "answers": ["180 πόντοι", "150 πόντοι", "200 πόντοι", "300 πόντοι"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Το μέγιστο σκορ είναι 180 (3 βελάκια στο τριπλό 20, δηλαδή 3 x 60 πόντους).",
    "funFacts": [
      "Το κέντρο του στόχου (bullseye) αποφέρει 50 πόντους, οπότε 3 κεντρικά βελάκια δίνουν 150 πόντους, λιγότερους από το τριπλό 20.",
      "Το ιδανικό παιχνίδι στο κλασικό 501 ονομάζεται 'nine-darter' και απαιτεί τουλάχιστον 9 τέλεια βελάκια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B5%CE%BB%CE%AC%CE%BA%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["darts", "scoring", "180"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_060",
    "text": "Πόσες επαφές (χτυπήματα) κατ' ανώτατο όριο επιτρέπεται να κάνει μια ομάδα στο βόλεϊ πριν στείλει τη μπάλα στο αντίπαλο γήπεδο;",
    "answers": ["2 επαφές", "3 επαφές", "4 επαφές", "5 επαφές"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 1,
    "explanation": "Κάθε ομάδα έχει δικαίωμα για το πολύ τρεις διαδοχικές επαφές (συνήθως: υποδοχή/πάσα, πάσα setter, επίθεση/καρφί).",
    "funFacts": [
      "Η επαφή στο μπλοκ δεν υπολογίζεται στις τρεις επιτρεπόμενες επαφές της ομάδας.",
      "Κανένας παίκτης δεν επιτρέπεται να χτυπήσει τη μπάλα δύο συνεχόμενες φορές μόνος του (εκτός αν η πρώτη επαφή ήταν μπλοκ)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["volleyball", "rules", "touches"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('sports', 'easy', 1, questions)

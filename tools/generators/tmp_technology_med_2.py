# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "tech_med_061",
    "text": "Ποια ιστορική ομάδα οκτώ κορυφαίων επιστημόνων αποχώρησε από το εργαστήριο του Γουίλιαμ Σόκλεϊ το 1957 για να ιδρύσει τη Fairchild Semiconductor;",
    "answers": ["Οι «Προδότες Οκτώ» (Traitorous Eight)", "Η Συμμορία των Τεσσάρων", "Οι Ιδρυτές του Στάνφορντ", "Οι Πρωτοπόροι της Intel"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι 'Traitorous Eight' (μεταξύ των οποίων οι Ρόμπερτ Νόις και Γκόρντον Μουρ) εγκατέλειψαν τον αυταρχικό Σόκλεϊ και έθεσαν τα θεμέλια για την έκρηξη της Silicon Valley.",
    "funFacts": [
      "Ο Σόκλεϊ τους χαρακτήρισε περιφρονητικά 'προδότες', αλλά η κίνησή τους άλλαξε για πάντα την ιστορία της τεχνολογίας.",
      "Από τα μέλη της ομάδας αυτής ιδρύθηκαν αργότερα κολοσσοί όπως η Intel, η AMD και κορυφαία ταμεία επιχειρηματικών συμμετοχών."
    ],
    "source": "https://el.wikipedia.org/wiki/Fairchild_Semiconductor",
    "locale": "el-GR",
    "tags": ["fairchild", "traitorous-eight", "silicon-valley", "semiconductors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_062",
    "text": "Ποιοι δύο Αμερικανοί εφευρέτες επινόησαν ανεξάρτητα το μονολιθικό ολοκληρωμένο κύκλωμα (μικροτσίπ) στα τέλη της δεκαετίας του 1950;",
    "answers": ["Γουίλιαμ Σόκλεϊ και Τζον Μπαρντίν", "Τζακ Κίλμπι και Ρόμπερτ Νόις", "Τόμας Έντισον και Νίκολα Τέσλα", "Τζον φον Νόιμαν και Άλαν Τιούρινγκ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζακ Κίλμπι (Texas Instruments) κατασκεύασε το πρώτο υβριδικό τσιπ από γερμάνιο το 1958, ενώ ο Ρόμπερτ Νόις (Fairchild) επινόησε το πρώτο επίπεδο τσιπ πυριτίου το 1959.",
    "funFacts": [
      "Ο Τζακ Κίλμπι βραβεύτηκε με το Νόμπελ Φυσικής το 2000 για την εφεύρεση του ολοκληρωμένου κυκλώματος (ο Νόις είχε αποβιώσει το 1990).",
      "Η μέθοδος του Νόις με τη χρήση στρωμάτων αλουμινίου για τις εσωτερικές διασυνδέσεις επέτρεψε τη μαζική βιομηχανική παραγωγή μικροτσίπ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CE%BF%CE%BA%CE%BB%CE%B7%CF%81%CF%89%CE%BC%CE%AD%CE%BD%CE%BF_%CE%BA%CF%8D%CE%BA%CE%BB%CF%89%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["integrated-circuit", "kilby", "noyce", "semiconductors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_063",
    "text": "Ποιος Ιταλός φυσικός και ηλεκτρολόγος μηχανικός ηγήθηκε της σχεδίασης του πρώτου εμπορικού μικροεπεξεργαστή μονού τσιπ Intel 4004 το 1971;",
    "answers": ["Ενρίκο Φέρμι", "Γουλιέλμο Μαρκόνι", "Φεντερίκο Φατζίν", "Αλεσάντρο Βόλτα"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Φεντερίκο Φατζίν (Federico Faggin) ανέπτυξε την καινοτόμο τεχνολογία πυλών πυριτίου (MOS silicon gate technology) κάνοντας εφικτή τη σχεδίαση του επεξεργαστή 4004.",
    "funFacts": [
      "Χάραξε τα αρχικά του 'F.F.' στη γωνία του πρώτου σχεδιασμού του τσιπ Intel 4004 ως προσωπική υπογραφή.",
      "Αργότερα ίδρυσε την εταιρεία Zilog και σχεδίασε τον θρυλικό μικροεπεξεργαστή Z80."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B5%CE%BD%CF%84%CE%B5%CF%81%CE%AF%CE%BA%CE%BF_%CE%A6%CE%B1%CF%84%CE%B6%CE%AF%CE%BD",
    "locale": "el-GR",
    "tags": ["faggin", "intel-4004", "microprocessors", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_064",
    "text": "Ποιος εξαιρετικά δημοφιλής 8-bit μικροεπεξεργαστής της δεκαετίας του 1970 και 1980 τροφοδότησε υπολογιστές όπως το ZX Spectrum και το αρχικό Game Boy;",
    "answers": ["Intel 8086", "MOS 6502", "Motorola 6800", "Zilog Z80"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Zilog Z80 κυκλοφόρησε το 1976 ως συμβατή προς τα πίσω αλλά ισχυρότερη και φθηνότερη εναλλακτική του Intel 8080, γνωρίζοντας τεράστια επιτυχία.",
    "funFacts": [
      "Εκτός από το ZX Spectrum, χρησιμοποιήθηκε σε αμέτρητα coin-op ηλεκτρονικά παιχνίδια (arcades), όπως το θρυλικό Pac-Man και το Galaga.",
      "Παραμένει σε παραγωγή για δεκαετίες ως ενσωματωμένος ελεγκτής σε βιομηχανικές συσκευές και αριθμομηχανές γραφημάτων Texas Instruments."
    ],
    "source": "https://el.wikipedia.org/wiki/Zilog_Z80",
    "locale": "el-GR",
    "tags": ["zilog-z80", "microprocessors", "gaming", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_065",
    "text": "Ποιος θρυλικός, εξαιρετικά φθηνός 8-bit επεξεργαστής σχεδιάστηκε από τον Τσακ Πεντλ και τροφοδότησε το Apple II, το NES και το Commodore 64;",
    "answers": ["MOS Technology 6502", "Intel 8088", "Motorola 68000", "ARM1"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο MOS 6502 κυκλοφόρησε το 1975 στην επαναστατικά χαμηλή τιμή των 25 δολαρίων, ενώ οι ανταγωνιστικοί επεξεργαστές της Motorola και της Intel κόστιζαν πάνω από 150 δολάρια.",
    "funFacts": [
      "Ο Στιβ Βόζνιακ επέλεξε τον 6502 για να σχεδιάσει τον Apple I και τον Apple II επειδή ήταν ο μόνος επεξεργαστής που μπορούσε να αντέξει οικονομικά.",
      "Στην ταινία επιστημονικής φαντασίας 'The Terminator' (1984), η οθόνη όρασης του ρομπότ T-800 δείχνει κώδικα συμβολικής γλώσσας (assembly) για τον επεξεργαστή MOS 6502."
    ],
    "source": "https://el.wikipedia.org/wiki/MOS_Technology_6502",
    "locale": "el-GR",
    "tags": ["mos-6502", "microprocessors", "apple-ii", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_066",
    "text": "Ποιος ισχυρός 16/32-bit μικροεπεξεργαστής αποτέλεσε την καρδιά του πρώτου Apple Macintosh, της Amiga 1000 και της κονσόλας Sega Mega Drive;",
    "answers": ["Intel 80286", "Motorola 68000", "Zilog Z8000", "NEC V20"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Motorola 68000 (m68k) κυκλοφόρησε το 1979 και διακρινόταν για την ευρεία αρχιτεκτονική καταχωρητών 32-bit και τον γραμμικό χώρο διευθυνσιοδότησης 16 MB.",
    "funFacts": [
      "Το όνομά του '68000' προήλθε από τον αριθμό των τρανζίστορ που περιείχε στο εσωτερικό του κυκλώματός του (περίπου 68.000).",
      "Κυριάρχησε στους σταθμούς εργασίας (workstations) της Sun Microsystems και στα coin-op ηλεκτρονικά παιχνίδια της Capcom (σύστημα CPS-1 και CPS-2)."
    ],
    "source": "https://el.wikipedia.org/wiki/Motorola_68000",
    "locale": "el-GR",
    "tags": ["motorola-68000", "microprocessors", "macintosh", "amiga"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_067",
    "text": "Ποιος Βρετανός εφευρέτης και επιχειρηματίας δημιούργησε τον εξαιρετικά δημοφιλή οικιακό υπολογιστή ZX Spectrum το 1982 φέρνοντας την πληροφορική στα βρετανικά σπίτια;",
    "answers": ["Άλαν Σούγκαρ", "Κρίστοφερ Κάρι", "Σερ Κλάιβ Σινκλέρ", "Χέρμαν Χάουζερ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Σερ Κλάιβ Σινκλέρ (Sir Clive Sinclair) ίδρυσε τη Sinclair Research και δημιούργησε τα προσιτά ZX80, ZX81 και ZX Spectrum με το χαρακτηριστικό ελαστικό πληκτρολόγιο.",
    "funFacts": [
      "Χρίστηκε ιππότης από τη βασίλισσα Ελισάβετ Β' το 1983 για την πρωτοποριακή συνεισφορά του στη βρετανική βιομηχανία υπολογιστών.",
      "Επινόησε επίσης το πρώτο ηλεκτρικό τρίκυκλο όχημα πόλης, το Sinclair C5 (1985), το οποίο όμως υπήρξε τεράστια εμπορική αποτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%AC%CE%B9%CE%B2_%CE%A3%CE%B9%CE%BD%CE%BA%CE%BB%CE%AD%CF%81",
    "locale": "el-GR",
    "tags": ["sinclair", "zx-spectrum", "history-tech", "inventions"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_068",
    "text": "Ποιος Αμερικανός ηλεκτρολόγος μηχανικός θεωρείται ο «πατέρας των υπερυπολογιστών», ιδρύοντας την Cray Research και σχεδιάζοντας το θρυλικό σύστημα Cray-1;",
    "answers": ["Τζον Ατανάσοφ", "Τζ. Πρέσπερ Έκερτ", "Τζον Μόκλι", "Σέιμουρ Κρέι"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Σέιμουρ Κρέι (Seymour Cray) σχεδίασε τους ταχύτερους υπολογιστές στον κόσμο για δεκαετίες (όπως το CDC 6600 και το Cray-1) καθιερώνοντας τη διανυσματική επεξεργασία.",
    "funFacts": [
      "Το σύστημα Cray-1 (1976) είχε ένα χαρακτηριστικό ημικυκλικό σχήμα σχήματος 'C' με ενσωματωμένο δερμάτινο κάθισμα γύρω από τη βάση του.",
      "Χρησιμοποιούσε πρωτοποριακό σύστημα ψύξης με υγρό φρέον για να απάγει την τεράστια θερμότητα των κυκλωμάτων του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%AD%CE%B9%CE%BC%CE%BF%CF%85%CF%81_%CE%9A%CF%81%CE%AD%CE%B9",
    "locale": "el-GR",
    "tags": ["cray", "supercomputers", "hardware", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_069",
    "text": "Ποιος Βρετανός επιστήμονας υπολογιστών στην IBM θεμελίωσε το σχεσιακό μοντέλο βάσεων δεδομένων με την ιστορική του εργασία το 1970;",
    "answers": ["Έντγκαρ Φ. Κοντ", "Πίτερ Τσεν", "Τζέιμς Μάρτιν", "Μάικλ Στόουνμπρεϊκερ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Έντγκαρ Φ. Κοντ (Edgar F. Codd) πρότεινε το σχεσιακό μοντέλο βάσεων δεδομένων βασισμένο στην άλγεβρα συνόλων και τις μαθηματικές σχέσεις.",
    "funFacts": [
      "Η εργασία του 'A Relational Model of Data for Large Shared Data Banks' αποτέλεσε το θεμέλιο πάνω στο οποίο βασίστηκαν η SQL και όλες οι σύγχρονες σχεσιακές βάσεις δεδομένων (RDBMS).",
      "Βραβεύτηκε με το Βραβείο Turing το 1981 για την ανεκτίμητη συνεισφορά του στη διαχείριση δεδομένων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BD%CF%84%CE%B3%CE%BA%CE%B1%CF%81_%CE%A6._%CE%9A%CE%BF%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["codd", "databases", "relational-model", "computer-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_070",
    "text": "Ποιος δισεκατομμυριούχος επιχειρηματίας συνίδρυσε την εταιρεία Software Development Laboratories το 1977, η οποία μετεξελίχθηκε στον κολοσσό βάσεων δεδομένων Oracle;",
    "answers": ["Μπιλ Γκέιτς", "Λάρι Έλισον", "Στιβ Τζομπς", "Σκοτ ΜακΝίλι"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Λάρι Έλισον (Larry Ellison) μαζί με τους Μπομπ Μάινερ και Εντ Οουτς δημιούργησαν το πρώτο εμπορικό σχεσιακό σύστημα διαχείρισης βάσεων δεδομένων συμβατό με SQL.",
    "funFacts": [
      "Το όνομα 'Oracle' προήλθε από την κωδική ονομασία ενός μυστικού ερευνητικού έργου που είχαν αναλάβει για την αμερικανική μυστική υπηρεσία CIA.",
      "Υπήρξε ένας από τους μακροβιότερους διευθύνοντες συμβούλους στον χώρο της τεχνολογίας, ηγούμενος της Oracle για 37 συνεχή χρόνια (1977-2014)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AC%CF%81%CE%B9_%CE%88%CE%BB%CE%B9%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["oracle", "larry-ellison", "databases", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_071",
    "text": "Ποιον χιουμοριστικό τιμητικό τίτλο έφερε για δεκαετίες ο δημιουργός της Python, Γκίντο βαν Ρόσουμ, ως τελικός διαιτητής αποφάσεων στην κοινότητα;",
    "answers": ["Αρχιερέας του Κώδικα", "Μέγας Διδάσκαλος των Script", "Ισόβιος Καλοπροαίρετος Δικτάτορας (BDFL)", "Πρώτος μεταξύ Ίσων"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο τίτλος BDFL (Benevolent Dictator For Life) απονεμήθηκε στον Van Rossum το 1995, διατηρώντας το προνόμιο να παίρνει την τελική απόφαση για τις προτάσεις εξέλιξης της Python (PEPs).",
    "funFacts": [
      "Παραιτήθηκε από τον ρόλο του BDFL τον Ιούλιο του 2018 μετά από έντονες διαφωνίες στην κοινότητα για την εισαγωγή του τελεστή εκχώρησης ':=' (walrus operator).",
      "Έκτοτε, η διακυβέρνηση της γλώσσας Python ασκείται από ένα δημοκρατικά εκλεγμένο πενταμελές Συμβούλιο Καθοδήγησης (Steering Council)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%AF%CE%BD%CF%84%CE%BF_%CE%B2%CE%B1%CE%BD_%CE%A1%CF%8C%CF%83%CE%BF%CF%85%CE%BC",
    "locale": "el-GR",
    "tags": ["python", "van-rossum", "bdfl", "open-source"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_072",
    "text": "Ποια σύγχρονη γλώσσα προγραμματισμού συστημάτων ξεκίνησε το 2006 από τον Γκρέιντον Χόαρ στα εργαστήρια της Mozilla για ασφαλή διαχείριση μνήμης;",
    "answers": ["Go", "Zig", "D", "Rust"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Rust σχεδιάστηκε για να προσφέρει την ταχύτητα και τον έλεγχο της C/C++ αποτρέποντας όμως σφάλματα μνήμης χάρη στον καινοτόμο μηχανισμό ιδιοκτησίας και δανεισμού (ownership/borrow checker).",
    "funFacts": [
      "Πήρε το όνομά της από έναν μύκητα της σκουριάς (rust fungus), ο οποίος είναι εξαιρετικά ανθεκτικός και επιβιώνει σε ακραίες συνθήκες.",
      "Έχει ψηφιστεί ως η 'πιο αγαπημένη γλώσσα προγραμματισμού' στην ετήσια παγκόσμια έρευνα προγραμματιστών του Stack Overflow για περισσότερα από 7 συνεχή χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/Rust_(%CE%B3%CE%BB%CF%8E%CF%83%CF%83%CE%B1_%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%8D)",
    "locale": "el-GR",
    "tags": ["rust", "programming", "mozilla", "systems-programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_073",
    "text": "Ποιοι τρεις κορυφαίοι μηχανικοί υπολογιστών σχεδίασαν τη γλώσσα προγραμματισμού Go στην Google το 2007 για ταχύτατη κατανεμημένη ανάπτυξη;",
    "answers": ["Ρόμπερτ Γκρίσεμερ, Ρομπ Πάικ και Κεν Τόμπσον", "Μπιάρνε Στρούστρουπ, Ντένις Ρίτσι και Μπράιαν Κέρνιχαν", "Τζέιμς Γκόσλινγκ, Μπιλ Τζόι και Γκάι Στιλ", "Άντερς Χέιλσμπεργκ, Μιγκέλ ντε Ικάζα και Τζον Σκιτ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Go (γνωστή και ως Golang) σχεδιάστηκε για να συνδυάζει την αποτελεσματικότητα μιας μεταγλωττιζόμενης γλώσσας με την ευκολία συγγραφής και την εγγενή υποστήριξη ταυτοχρονισμού (goroutines).",
    "funFacts": [
      "Η επίσημη μασκότ της γλώσσας Go είναι ο Gopher, ένας χαριτωμένος τυφλοπόντικας που σχεδιάστηκε από τη Ρενέ Φρεντς.",
      "Κορυφαία σύγχρονα συστήματα υποδομής υπολογιστικού νέφους, όπως το Docker και το Kubernetes, είναι γραμμένα εξ ολοκλήρου σε Go."
    ],
    "source": "https://el.wikipedia.org/wiki/Go_(%CE%B3%CE%BB%CF%8E%CF%83%CF%83%CE%B1_%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%8D)",
    "locale": "el-GR",
    "tags": ["golang", "google", "programming", "cloud"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_074",
    "text": "Ποιος διακεκριμένος μηχανικός λογισμικού ηγήθηκε της ανάπτυξης της γλώσσας Swift και της υποδομής μεταγλωττιστών LLVM στην Apple;",
    "answers": ["Κρεγκ Φεντερίγκι", "Κρις Λάτνερ", "Τζον ΜακΦάρλαν", "Τζόναθαν Άιβ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Κρις Λάτνερ (Chris Lattner) ξεκίνησε το έργο LLVM το 2000 και στη συνέχεια δημιούργησε τη γλώσσα Swift στην Apple για να αντικαταστήσει την Objective-C.",
    "funFacts": [
      "Η Apple παρουσίασε επίσημα τη Swift στο συνέδριο WWDC το 2014 και την κατέστησε λογισμικό ανοιχτού κώδικα στα τέλη του 2015.",
      "Η υποδομή LLVM του Λάτνερ χρησιμοποιείται σήμερα ως ραχοκοκαλιά μεταγλώττισης για δεκάδες γλώσσες, συμπεριλαμβανομένων των Clang (C/C++), Rust και Julia."
    ],
    "source": "https://el.wikipedia.org/wiki/Swift_(%CE%B3%CE%BB%CF%8E%CF%83%CF%83%CE%B1_%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%8D)",
    "locale": "el-GR",
    "tags": ["swift", "apple", "programming", "compilers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_075",
    "text": "Από ποια ευρωπαϊκή εταιρεία εργαλείων λογισμικού αναπτύχθηκε η γλώσσα Kotlin, η οποία ανακηρύχθηκε επίσημη προτιμώμενη γλώσσα για Android από την Google το 2019;",
    "answers": ["Canonical", "SAP", "JetBrains", "Atlassian"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η JetBrains (δημιουργός του δημοφιλούς περιβάλλοντος IntelliJ IDEA) ξεκίνησε την ανάπτυξη της Kotlin το 2010 ως σύγχρονη γλώσσα πλήρως διαλειτουργική με τη Java.",
    "funFacts": [
      "Πήρε το όνομά της από το ρωσικό νησί Κότλιν (Kotlin Island) στον κόλπο της Φινλανδίας, κοντά στην Αγία Πετρούπολη, όπως ακριβώς η Java πήρε το όνομά της από το ινδονησιακό νησί Ιάβα.",
      "Πάνω από το 80% των κορυφαίων εφαρμογών στο Google Play Store χρησιμοποιούν κώδικα γραμμένο σε Kotlin."
    ],
    "source": "https://el.wikipedia.org/wiki/Kotlin",
    "locale": "el-GR",
    "tags": ["kotlin", "jetbrains", "android", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_076",
    "text": "Ποιος διακεκριμένος μηχανικός λογισμικού της Microsoft, σχεδιαστής των Turbo Pascal και C#, ηγήθηκε της ανάπτυξης της γλώσσας TypeScript;",
    "answers": ["Σκοτ Γκάθρι", "Μαρκ Ρουσίνοβιτς", "Ναθάν Μίρβολντ", "Άντερς Χέιλσμπεργκ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Άντερς Χέιλσμπεργκ (Anders Hejlsberg) σχεδίασε την TypeScript ως αυστηρό συντακτικό υπερσύνολο της JavaScript που προσθέτει προαιρετικό στατικό έλεγχο τύπων.",
    "funFacts": [
      "Η TypeScript μεταγλωττίζεται (transpiles) απευθείας σε καθαρή JavaScript ώστε να εκτελείται σε οποιοδήποτε περιβάλλον ιστού.",
      "Κορυφαία διαδικτυακά πλαίσια όπως το Angular και το Vue 3 είναι γραμμένα εξ ολοκλήρου σε TypeScript."
    ],
    "source": "https://el.wikipedia.org/wiki/TypeScript",
    "locale": "el-GR",
    "tags": ["typescript", "microsoft", "javascript", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_077",
    "text": "Ποιο ιδιόκτητο σύστημα διαχείρισης εκδόσεων χρησιμοποιούσε η κοινότητα του πυρήνα Linux πριν η ανάκληση της δωρεάν άδειάς του οδηγήσει στη δημιουργία του Git το 2005;",
    "answers": ["BitKeeper", "ClearCase", "Perforce", "Visual SourceSafe"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η εταιρεία BitMover παρείχε δωρεάν άδεια χρήσης του BitKeeper στους συντελεστές του Linux, αλλά την ανακάλεσε το 2005 όταν προγραμματιστές προσπάθησαν να κάνουν reverse engineering στο πρωτόκολλό του.",
    "funFacts": [
      "Ο Λίνους Τόρβαλντς αρνήθηκε να υιοθετήσει άλλα υπάρχοντα συστήματα όπως το CVS ή το SVN θεωρώντας τα αργά και αναξιόπιστα, γράφοντας το πρώτο πρωτότυπο του Git μέσα σε λίγες μέρες.",
      "Το πρώτο commit του πυρήνα Linux χρησιμοποιώντας Git πραγματοποιήθηκε με επιτυχία τον Απρίλιο του 2005."
    ],
    "source": "https://el.wikipedia.org/wiki/Git",
    "locale": "el-GR",
    "tags": ["git", "bitkeeper", "torvalds", "version-control"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_078",
    "text": "Ποιο κεντρικό σύστημα ελέγχου εκδόσεων ήταν το κυρίαρχο ανοιχτό πρότυπο στη βιομηχανία λογισμικού τη δεκαετία του 2000 πριν την καθολική επικράτηση του Git;",
    "answers": ["CVS", "Apache Subversion (SVN)", "Mercurial", "Bazaar"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Apache Subversion (SVN) δημιουργήθηκε το 2000 για να διορθώσει τις ατέλειες του παλαιότερου CVS και υπήρξε το κυρίαρχο κεντρικό σύστημα διαχείρισης κώδικα.",
    "funFacts": [
      "Σε αντίθεση με το κατανεμημένο μοντέλο του Git όπου κάθε προγραμματιστής έχει πλήρες τοπικό αντίγραφο του ιστορικού, το SVN βασιζόταν σε έναν κεντρικό ενιαίο διακομιστή.",
      "Χρησιμοποιούσε σειριακούς αριθμούς εκδόσεων (revisions 1, 2, 3...) αντί για κρυπτογραφικούς κατακερματισμούς SHA-1."
    ],
    "source": "https://el.wikipedia.org/wiki/Apache_Subversion",
    "locale": "el-GR",
    "tags": ["svn", "subversion", "version-control", "apache"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_079",
    "text": "Ποιος Αμερικανός προγραμματιστής τυποποίησε και διέδωσε τη μορφή ανταλλαγής δεδομένων JSON (JavaScript Object Notation) στις αρχές της δεκαετίας του 2000;",
    "answers": ["Τιμ Μπέρνερς-Λι", "Μπρένταν Άιχ", "Ντάγκλας Κρόκφορντ", "Τζον Ρέσιγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ντάγκλας Κρόκφορντ (Douglas Crockford) όρισε επίσημα το πρότυπο JSON ως μια ελαφριά, ευανάγνωστη μορφή ανταλλαγής δεδομένων βασισμένη στη σύνταξη αντικειμένων της JavaScript.",
    "funFacts": [
      "Κατοχύρωσε το domain json.org το 2002 για να τεκμηριώσει τη μορφή, η οποία εκτόπισε ταχέως την περίπλοκη μορφή XML από τον παγκόσμιο ιστό.",
      "Συνέγραψε το επιδραστικό βιβλίο 'JavaScript: The Good Parts' (2008), το οποίο επηρέασε βαθιά τον τρόπο συγγραφής σύγχρονου κώδικα JavaScript."
    ],
    "source": "https://el.wikipedia.org/wiki/JSON",
    "locale": "el-GR",
    "tags": ["json", "crockford", "web-standards", "data-formats"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_080",
    "text": "Ποιος επιστήμονας υπολογιστών όρισε το αρχιτεκτονικό στυλ REST (Representational State Transfer) για δικτυακές εφαρμογές στη διδακτορική του διατριβή το 2000;",
    "answers": ["Βιντ Σερφ", "Τιμ Μπέρνερς-Λι", "Ρομπέρ Καγιώ", "Ρόι Φίλντινγκ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ρόι Φίλντινγκ (Roy Fielding) περιέγραψε τις αρχές του REST ως πρότυπο σχεδιασμού κατανεμημένων συστημάτων υπερμέσων, το οποίο καθόρισε τον τρόπο σχεδίασης των Web APIs.",
    "funFacts": [
      "Ο Φίλντινγκ ήταν επίσης ένας από τους κύριους συντάκτες της προδιαγραφής του πρωτοκόλλου HTTP/1.1.",
      "Ένα πραγματικό RESTful API βασίζεται σε αρχιτεκτονική χωρίς κατάσταση (stateless), όπου κάθε αίτημα περιέχει όλες τις απαραίτητες πληροφορίες για την εκτέλεσή του."
    ],
    "source": "https://el.wikipedia.org/wiki/REST",
    "locale": "el-GR",
    "tags": ["rest", "api", "fielding", "web-architecture"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_081",
    "text": "Ποιο πρωτόκολλο επικοινωνίας του διαδικτύου παρέχει πλήρως αμφίδρομη (full-duplex) επικοινωνία σε πραγματικό χρόνο πάνω από μία συνεχή σύνδεση TCP;",
    "answers": ["WebSocket", "HTTP/1.0", "FTP", "SNMP"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το WebSocket (RFC 6455) επιτρέπει σε περιηγητές και διακομιστές να ανταλλάσσουν μηνύματα άμεσα χωρίς το συνεχές κόστος αποστολής νέων κεφαλίδων HTTP.",
    "funFacts": [
      "Ξεκινά ως μια απλή σύνδεση HTTP η οποία στη συνέχεια 'αναβαθμίζεται' (Upgrade handshake) σε πρωτόκολλο WebSocket.",
      "Είναι απαραίτητο για σύγχρονες εφαρμογές άμεσης συνομιλίας (chat), συνεργατικά έγγραφα σε πραγματικό χρόνο και διαδικτυακά multiplayer παιχνίδια."
    ],
    "source": "https://el.wikipedia.org/wiki/WebSocket",
    "locale": "el-GR",
    "tags": ["websocket", "networking", "web-standards", "real-time"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_082",
    "text": "Ποια σύγχρονη γλώσσα υποβολής ερωτημάτων και περιβάλλον εκτέλεσης για APIs αναπτύχθηκε εσωτερικά από το Facebook το 2012 και διατέθηκε ως ανοιχτός κώδικας το 2015;",
    "answers": ["SPARQL", "GraphQL", "OData", "gRPC"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το GraphQL επιτρέπει στους πελάτες (clients) να ζητούν ακριβώς τα δεδομένα που χρειάζονται και τίποτα περισσότερο, αποτρέποντας το over-fetching και under-fetching.",
    "funFacts": [
      "Σε αντίθεση με τα κλασικά REST APIs που απαιτούν πολλαπλά endpoints (URLs), το GraphQL χρησιμοποιεί συνήθως ένα ενιαίο endpoint για όλα τα αιτήματα.",
      "Από το 2018 η διαχείρισή του πέρασε στο ανεξάρτητο ίδρυμα GraphQL Foundation υπό την ομπρέλα του Linux Foundation."
    ],
    "source": "https://el.wikipedia.org/wiki/GraphQL",
    "locale": "el-GR",
    "tags": ["graphql", "facebook", "api", "web-development"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_083",
    "text": "Ποια πρωτοποριακή πλατφόρμα λογισμικού που παρουσιάστηκε το 2013 από τον Σόλομον Χάικς καθιέρωσε τη συσκευασία εφαρμογών σε ελαφριά κοντέινερ (containers);",
    "answers": ["Vagrant", "VirtualBox", "Docker", "OpenVZ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Docker εκμεταλλεύτηκε τα cgroups και namespaces του πυρήνα Linux για να απομονώσει εφαρμογές σε ελαφριά containers χωρίς την ανάγκη βαριών εικονικών μηχανών (VMs).",
    "funFacts": [
      "Η διάσημη φράση 'Μα στον δικό μου υπολογιστή δούλευε!' (It works on my machine) επιλύθηκε σε μεγάλο βαθμό χάρη στην ομοιομορφία που προσφέρουν τα Docker containers.",
      "Η μασκότ του Docker είναι μια μπλε φάλαινα που μεταφέρει ναυτιλιακά εμπορευματοκιβώτια (containers) στην πλάτη της."
    ],
    "source": "https://el.wikipedia.org/wiki/Docker",
    "locale": "el-GR",
    "tags": ["docker", "containers", "devops", "cloud"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_084",
    "text": "Ποιο σύστημα ενορχήστρωσης κοντέινερ ανοιχτού κώδικα σχεδιάστηκε αρχικά από μηχανικούς της Google αντλώντας έμπνευση από το εσωτερικό σύστημα Borg;",
    "answers": ["Mesos", "Nomad", "OpenShift", "Kubernetes"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Kubernetes (γνωστό και ως K8s) αυτοματοποιεί την ανάπτυξη, την κλιμάκωση και τη διαχείριση εφαρμογών σε κοντέινερ σε συστοιχίες διακομιστών.",
    "funFacts": [
      "Το όνομα προέρχεται από την ελληνική λέξη 'κυβερνήτης' (τιμονιέρης πλοίου), γι' αυτό και το επίσημο λογότυπό του είναι το τιμόνι ενός πλοίου με 7 ακτίνες.",
      "Οι 7 ακτίνες του λογοτύπου επιλέχθηκαν ως αναφορά στο αρχικό εσωτερικό έργο της Google που ονομαζόταν 'Project Seven of Nine' (από τον χαρακτήρα των Borg στο Star Trek)."
    ],
    "source": "https://el.wikipedia.org/wiki/Kubernetes",
    "locale": "el-GR",
    "tags": ["kubernetes", "google", "containers", "cloud-computing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_085",
    "text": "Ποιος Γερμανός μηχανικός λογισμικού ίδρυσε το 1993 την ιστορική διανομή Debian Linux, συνθέτοντας το όνομα της τότε φίλης του Debra και το δικό του;",
    "answers": ["Ίαν Μέρντοκ", "Πάτρικ Φόλκερντινγκ", "Μαρκ Σάτλγουερθ", "Ντανιέλ Ρόμπινς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ίαν Μέρντοκ (Ian Murdock) ξεκίνησε το Debian Manifesto το 1993, δημιουργώντας μία από τις πιο σταθερές και επιδραστικές διανομές Linux ανοιχτού κώδικα.",
    "funFacts": [
      "Το όνομα Debian προήλθε από τη συνένωση του ονόματος της τότε κοπέλας του Debra Lynn και του ονόματός του Ian (Deb + Ian).",
      "Όλες οι επίσημες εκδόσεις του Debian παίρνουν παραδοσιακά την κωδική τους ονομασία από χαρακτήρες της ταινίας κινουμένων σχεδίων Toy Story (π.χ. Buzz, Woody, Bullseye, Bookworm)."
    ],
    "source": "https://el.wikipedia.org/wiki/Debian",
    "locale": "el-GR",
    "tags": ["debian", "linux", "open-source", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_086",
    "text": "Ποιος κολοσσός επιχειρηματικού λογισμικού ανοιχτού κώδικα που ιδρύθηκε το 1993 εξαγοράστηκε από την IBM το 2019 έναντι περίπου 34 δισεκατομμυρίων δολαρίων;",
    "answers": ["Novell", "Red Hat", "SUSE", "Canonical"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Red Hat πρωτοπόρησε στο επιχειρηματικό μοντέλο ανοιχτού κώδικα παρέχοντας την εμπορική διανομή Red Hat Enterprise Linux (RHEL) και επαγγελματική τεχνική υποστήριξη.",
    "funFacts": [
      "Η εξαγορά της Red Hat από την IBM αποτέλεσε τη μεγαλύτερη εξαγορά εταιρείας λογισμικού στην ιστορία μέχρι εκείνη τη στιγμή.",
      "Το διάσημο κόκκινο καπέλο της εταιρείας εμπνεύστηκε από το κόκκινο καπέλο λακρός του Πανεπιστημίου Cornell που φορούσε ο συνιδρυτής Μαρκ Ίγουινγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/Red_Hat",
    "locale": "el-GR",
    "tags": ["red-hat", "linux", "ibm", "open-source"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_087",
    "text": "Ποιος Νοτιοαφρικανός επιχειρηματίας και διαστημικός τουρίστας ίδρυσε την εταιρεία Canonical και χρηματοδότησε τη δημοφιλή διανομή Ubuntu Linux το 2004;",
    "answers": ["Έλον Μασκ", "Κιμ Ντότκομ", "Μαρκ Σάτλγουερθ", "Μάικλ Ντελ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μαρκ Σάτλγουερθ (Mark Shuttleworth) δημιούργησε το Ubuntu βασισμένο στο Debian με στόχο ένα φιλικό, δωρεάν λειτουργικό σύστημα για όλους τους χρήστες.",
    "funFacts": [
      "Έγινε ο πρώτος πολίτης ανεξάρτητης αφρικανικής χώρας που ταξίδεψε στο διάστημα, επισκεπτόμενος τον Διεθνή Διαστημικό Σταθμό το 2002.",
      "Η λέξη 'Ubuntu' προέρχεται από αρχαία αφρικανική φιλοσοφία και μεταφράζεται περίπου ως 'ανθρωπιά προς τους άλλους' ή 'είμαι επειδή είμαστε'."
    ],
    "source": "https://el.wikipedia.org/wiki/Ubuntu",
    "locale": "el-GR",
    "tags": ["ubuntu", "canonical", "shuttleworth", "linux"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_088",
    "text": "Έναντι ποιου εκτιμώμενου ποσού εξαγόρασε η Google τη νεοφυή εταιρεία Android Inc. το 2005, σε μια από τις πιο επικερδείς εξαγορές στην ιστορία της τεχνολογίας;",
    "answers": ["1 δισεκατομμύριο δολάρια", "500 εκατομμύρια δολάρια", "165 εκατομμύρια δολάρια", "Περίπου 50 εκατομμύρια δολάρια"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Google αγόρασε το Android τον Ιούλιο του 2005 έναντι περίπου 50 εκατομμυρίων δολαρίων, εντάσσοντας στην ομάδα της τους ιδρυτές Άντι Ρούμπιν και Ριτς Μάινερ.",
    "funFacts": [
      "Αρχικός στόχος της εταιρείας Android Inc. δεν ήταν τα έξυπνα τηλέφωνα, αλλά η δημιουργία ενός προηγμένου λειτουργικού συστήματος για ψηφιακές φωτογραφικές μηχανές.",
      "Όταν η Apple παρουσίασε το πρώτο iPhone το 2007, η ομάδα του Android πέταξε στα σκουπίδια το αρχικό πρωτότυπο που θύμιζε BlackBerry και σχεδίασε ξανά το σύστημα για οθόνες αφής."
    ],
    "source": "https://el.wikipedia.org/wiki/Android_(%CE%BB%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%B9%CE%BA%CF%8C_%CF%83%CF%8D%CF%83%CF%84%CE%B7%CE%BC%CE%B1)",
    "locale": "el-GR",
    "tags": ["android", "google", "acquisitions", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_089",
    "text": "Ποιο λειτουργικό σύστημα κινητών τηλεφώνων ήταν το κυρίαρχο στα smartphones παγκοσμίως τη δεκαετία του 2000, κυρίως μέσω των συσκευών της Nokia;",
    "answers": ["Symbian", "Windows Mobile", "Palm OS", "BlackBerry OS"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Symbian OS ήταν το αδιαφιλονίκητο λειτουργικό σύστημα στα πρώιμα smartphones κατέχοντας πάνω από το 60% της παγκόσμιας αγοράς μέχρι το 2010.",
    "funFacts": [
      "Αναπτύχθηκε από κοινοπραξία κολοσσών της κινητής τηλεφωνίας (Nokia, Ericsson, Motorola και Psion) βασισμένο στο λειτουργικό EPOC32.",
      "Κατέρρευσε ραγδαία μετά την έλευση του iOS και του Android, καθώς η αρχιτεκτονική του δεν ήταν σχεδιασμένη εξαρχής για οθόνες αφής και σύγχρονες εφαρμογές."
    ],
    "source": "https://el.wikipedia.org/wiki/Symbian",
    "locale": "el-GR",
    "tags": ["symbian", "nokia", "smartphones", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_090",
    "text": "Ποια καναδική εταιρεία τεχνολογίας (αρχικά γνωστή ως Research In Motion - RIM) κυριάρχησε στα εταιρικά smartphones τη δεκαετία του 2000 χάρη στο πληκτρολόγιο QWERTY και την κρυπτογραφημένη υπηρεσία BBM;",
    "answers": ["Nortel", "BlackBerry", "Alcatel", "Siemens"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η BlackBerry (RIM), ιδρυμένη από τον Μάικ Λαζαρίδη, ήταν το απόλυτο σύμβολο κύρους για στελέχη επιχειρήσεων και πολιτικούς λόγω του ασφαλούς push email.",
    "funFacts": [
      "Ο πρόεδρος των ΗΠΑ Μπαράκ Ομπάμα έδωσε μάχη με τις μυστικές υπηρεσίες το 2009 για να του επιτραπεί να κρατήσει το προσωπικό του BlackBerry στον Λευκό Οίκο.",
      "Η εταιρεία έχασε τη συντριπτική πλειονότητα των χρηστών της όταν υποτίμησε τη μετάβαση των καταναλωτών στις οθόνες αφής και τις εφαρμογές."
    ],
    "source": "https://el.wikipedia.org/wiki/BlackBerry",
    "locale": "el-GR",
    "tags": ["blackberry", "rim", "smartphones", "mobile-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_091",
    "text": "Ποιο ηγετικό στέλεχος διαδέχθηκε τον Μπιλ Γκέιτς ως διευθύνων σύμβουλος (CEO) της Microsoft το 2000, μένοντας γνωστός για τις εκρηκτικές ομιλίες του με το σύνθημα «Developers! Developers!»;",
    "answers": ["Σάτια Ναντέλα", "Πολ Άλεν", "Στιβ Μπάλμερ", "Μπραντ Σμιθ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Στιβ Μπάλμερ (Steve Ballmer) ηγήθηκε της Microsoft από το 2000 έως το 2014 επιβλέποντας την κυκλοφορία του Xbox και την εκρηκτική αύξηση των εσόδων της εταιρείας.",
    "funFacts": [
      "Το ιστορικό βίντεο όπου χοροπηδάει και φωνάζει ρυθμικά 'Developers, developers, developers!' σε συνέδριο προγραμματιστών έγινε ένα από τα διασημότερα memes στην ιστορία της τεχνολογίας.",
      "Μετά την αποχώρησή του από τη Microsoft, αγόρασε την ομάδα μπάσκετ του NBA Los Angeles Clippers έναντι 2 δισεκατομμυρίων δολαρίων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B9%CE%B2_%CE%9C%CF%80%CE%AC%CE%BB%CE%BC%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["ballmer", "microsoft", "executives", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_092",
    "text": "Ποιο στέλεχος ινδικής καταγωγής ανέλαβε διευθύνων σύμβουλος της Microsoft το 2014, οδηγώντας την εταιρεία σε θεαματική ανάκαμψη με επίκεντρο το υπολογιστικό νέφος Azure;",
    "answers": ["Σουντάρ Πιτσάι", "Αρβίντ Κρίσνα", "Σαντανού Ναραγέν", "Σάτια Ναντέλα"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Σάτια Ναντέλα (Satya Nadella) άλλαξε ριζικά την εταιρική κουλτούρα της Microsoft στρέφοντας το βάρος στις συνδρομητικές υπηρεσίες cloud και το ανοιχτό λογισμικό.",
    "funFacts": [
      "Επινόησε τη στρατηγική 'Cloud First, Mobile First' και αγκάλιασε το Linux δηλώνοντας δημόσια 'Microsoft loves Linux'.",
      "Υπό την ηγεσία του, η χρηματιστηριακή αξία της Microsoft εκτοξεύτηκε από περίπου 300 δισεκατομμύρια δολάρια σε πάνω από 3 τρισεκατομμύρια δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%AC%CF%84%CE%B9%CE%B1_%CE%9D%CE%B1%CE%BD%CF%84%CE%AD%CE%BB%CE%B1",
    "locale": "el-GR",
    "tags": ["nadella", "microsoft", "cloud", "executives"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_093",
    "text": "Ποια εταιρεία υπολογιστών ίδρυσε ο Στιβ Τζομπς το 1985 μετά την απομάκρυνσή του από την Apple, το λειτουργικό σύστημα της οποίας αποτέλεσε τη βάση του σύγχρονου macOS;",
    "answers": ["NeXT", "Be Inc.", "Pixar", "Silicon Graphics"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η NeXT ανέπτυξε τους πρωτοποριακούς σταθμούς εργασίας NeXT Computer και το αντικειμενοστραφές λειτουργικό NeXTSTEP βασισμένο στον πυρήνα Mach και το BSD Unix.",
    "funFacts": [
      "Σε έναν υπολογιστή NeXTcube στο CERN δημιούργησε ο Τιμ Μπέρνερς-Λι τον πρώτο παγκόσμιο διακομιστή και πρόγραμμα περιήγησης ιστού το 1990.",
      "Η Apple εξαγόρασε τη NeXT το 1996 φέρνοντας πίσω τον Στιβ Τζομπς, ενώ το NeXTSTEP μετεξελίχθηκε στα λειτουργικά Mac OS X, iOS και iPadOS."
    ],
    "source": "https://el.wikipedia.org/wiki/NeXT",
    "locale": "el-GR",
    "tags": ["next", "steve-jobs", "operating-systems", "apple-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_094",
    "text": "Ποιος Αμερικανός πρωτοπόρος μηχανικός λογισμικού ίδρυσε την Android Inc. το 2003 έχοντας προηγουμένως εργαστεί στην Apple και συνιδρύσει την Danger;",
    "answers": ["Τόνι Φαντέλ", "Άντι Ρούμπιν", "Σκοτ Φόρσταλ", "Μαρκ Άντρισεν"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Άντι Ρούμπιν (Andy Rubin) δημιούργησε το Android και ηγήθηκε της ανάπτυξής του στην Google ως επικεφαλής του τμήματος κινητών συσκευών μέχρι το 2013.",
    "funFacts": [
      "Το προσωνύμιο 'Android' του είχε δοθεί από συναδέλφους του στην Apple στα τέλη της δεκαετίας του 1980 λόγω της μεγάλης του αγάπης για τα ρομπότ.",
      "Πριν από το Android, είχε δημιουργήσει το Danger Hiptop (γνωστότερο ως T-Mobile Sidekick), το πρώτο δημοφιλές smartphone με διαδικτυακές εφαρμογές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BD%CF%84%CE%B9_%CE%A1%CE%BF%CF%8D%CE%BC%CF%80%CE%B9%CE%BD",
    "locale": "el-GR",
    "tags": ["andy-rubin", "android", "google", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_095",
    "text": "Ποιος μηχανικός της Intel συνέλαβε πρώτος την ιδέα ενός μικροεπεξεργαστή γενικής χρήσης για αριθμομηχανές της Busicom, οδηγώντας στη γέννηση του Intel 4004;",
    "answers": ["Ρόμπερτ Νόις", "Γκόρντον Μουρ", "Μαρσιάν «Τεντ» Χοφ", "Άντι Γκρόουβ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τεντ Χοφ (Ted Hoff) πρότεινε να αντικατασταθούν τα 12 πολύπλοκα ειδικά προσαρμοσμένα τσιπ της Busicom με έναν ενιαίο προγραμματιζόμενο επεξεργαστή γενικής χρήσης.",
    "funFacts": [
      "Η ιδέα του Χοφ θεωρήθηκε ριζοσπαστική επειδή μετέφερε την πολυπλοκότητα από το υλικό (hardware) στο λογισμικό (software).",
      "Εισήχθη στο Εθνικό Hall of Fame Εφευρετών των ΗΠΑ για τη συμβολή του στη σύλληψη του μικροεπεξεργαστή."
    ],
    "source": "https://el.wikipedia.org/wiki/Intel_4004",
    "locale": "el-GR",
    "tags": ["ted-hoff", "intel-4004", "microprocessors", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_096",
    "text": "Ποιο είναι το ελάχιστο προτεινόμενο μέγεθος κλειδιού σε bits για τον ασύμμετρο αλγόριθμο RSA στα σύγχρονα πρότυπα κυβερνοασφάλειας;",
    "answers": ["128 bits", "256 bits", "1024 bits", "2048 bits"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Εθνικό Ινστιτούτο Προτύπων και Τεχνολογίας (NIST) ορίζει τα 2048 bits ως το ελάχιστο αποδεκτό μήκος κλειδιού RSA, καθώς τα κλειδιά 1024 bits θεωρούνται πλέον ανεπαρκώς ασφαλή.",
    "funFacts": [
      "Για μακροπρόθεσμη προστασία δεδομένων μετά το 2030 συνιστάται συχνά κλειδί μήκους 3072 ή 4096 bits.",
      "Σε αντίθεση με τη συμμετρική κρυπτογραφία (όπως το AES) όπου τα 256 bits παρέχουν απόλυτη ασφάλεια, η ασύμμετρη κρυπτογραφία απαιτεί πολύ μεγαλύτερα κλειδιά λόγω των ειδικών μαθηματικών αλγορίθμων παραγοντοποίησης."
    ],
    "source": "https://el.wikipedia.org/wiki/RSA_(%CE%BA%CF%81%CF%85%CF%80%CF%84%CE%BF%CF%83%CF%8D%CF%83%CF%84%CE%B7%CE%BC%CE%B1)",
    "locale": "el-GR",
    "tags": ["rsa", "cryptography", "security", "encryption-keys"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_097",
    "text": "Ποιος βελγικός αλγόριθμος συμμετρικής κρυπτογράφησης επιλέχθηκε από το αμερικανικό NIST το 2001 ως το παγκόσμιο πρότυπο AES;",
    "answers": ["Rijndael", "Twofish", "Serpent", "RC6"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος Rijndael, που σχεδιάστηκε από τους Βέλγους κρυπτογράφους Βίνσεντ Ρέιμεν και Τζόαν Ντάμεν, επιλέχθηκε μετά από ανοιχτό πενταετή διεθνή διαγωνισμό ως το πρότυπο AES.",
    "funFacts": [
      "Το όνομα Rijndael είναι συνδυασμός των επιθέτων των δύο δημιουργών του (Rijmen και Daemen).",
      "Χρησιμοποιεί μπλοκ μεγέθους 128 bits και μήκη κλειδιών 128, 192 ή 256 bits, προστατεύοντας σήμερα τραπεζικές συναλλαγές και κρατικά απόρρητα έγγραφα παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/Advanced_Encryption_Standard",
    "locale": "el-GR",
    "tags": ["aes", "rijndael", "cryptography", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_098",
    "text": "Σε ποια επίσημη οικογένεια κρυπτογραφικών συναρτήσεων κατακερματισμού (hash functions) ανήκει ο αλγόριθμος SHA-256 που χρησιμοποιείται στο δίκτυο του Bitcoin;",
    "answers": ["MD5", "SHA-2", "SHA-1", "CRC32"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο SHA-256 είναι μέλος της οικογένειας προτύπων SHA-2 (Secure Hash Algorithm 2) που σχεδιάστηκε από την Υπηρεσία Εθνικής Ασφαλείας των ΗΠΑ (NSA) και δημοσιεύτηκε το 2001.",
    "funFacts": [
      "Μετατρέπει οποιοδήποτε μέγεθος δεδομένων εισόδου σε μια μοναδική έξοδο σταθερού μήκους 256 bits (64 δεκαεξαδικοί χαρακτήρες).",
      "Στο Bitcoin χρησιμοποιείται στον μηχανισμό απόδειξης εργασίας (Proof of Work) και στη δημιουργία διευθύνσεων πορτοφολιών."
    ],
    "source": "https://el.wikipedia.org/wiki/SHA-2",
    "locale": "el-GR",
    "tags": ["sha-256", "cryptography", "bitcoin", "hashing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_099",
    "text": "Ποια είναι η θεμελιώδης μονάδα κβαντικής πληροφορίας που μπορεί να βρίσκεται σε κβαντική υπέρθεση καταστάσεων 0 και 1 ταυτόχρονα;",
    "answers": ["Bit", "Byte", "Qubit (κβαντικό bit)", "Voxel"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το qubit (quantum bit) αξιοποιεί τις αρχές της κβαντομηχανικής (υπέρθεση και κβαντική διεμπλοκή) επιτρέποντας στους κβαντικούς υπολογιστές να εκτελούν ορισμένους υπολογισμούς εκθετικά ταχύτερα.",
    "funFacts": [
      "Ενώ n κλασικά bits μπορούν να βρίσκονται σε μία μόνο από 2^n πιθανές καταστάσεις ανά πάσα στιγμή, n qubits μπορούν να αναπαραστήσουν ταυτόχρονα και τις 2^n καταστάσεις.",
      "Υλοποιούνται πειραματικά με υπεραγώγιμα κυκλώματα (όπως στην IBM και Google), παγιδευμένα ιόντα ή φωτόνια σε θερμοκρασίες κοντά στο απόλυτο μηδέν (-273,15 °C)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B2%CE%B1%CE%BD%CF%84%CE%B9%CE%BA%CF%8C_bit",
    "locale": "el-GR",
    "tags": ["qubit", "quantum-computing", "physics", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_100",
    "text": "Ποιος κβαντικός αλγόριθμος που προτάθηκε το 1994 αποδεικνύει ότι ένας αρκετά ισχυρός κβαντικός υπολογιστής μπορεί να παραγοντοποιήσει μεγάλους αριθμούς σε πολυωνυμικό χρόνο, απειλώντας τον RSA;",
    "answers": ["Αλγόριθμος του Grover", "Αλγόριθμος του Deutsch-Jozsa", "Αλγόριθμος Simon", "Αλγόριθμος του Shor"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος του Peter Shor επιλύει το πρόβλημα της εύρεσης περιόδου και της παραγοντοποίησης ακεραίων εκθετικά ταχύτερα από οποιονδήποτε γνωστό κλασικό αλγόριθμο.",
    "funFacts": [
      "Η δημοσίευση του αλγορίθμου Shor το 1994 ήταν το βασικό έναυσμα για την έκρηξη των διεθνών ερευνητικών κονδυλίων για την κατασκευή κβαντικών υπολογιστών.",
      "Οδήγησε την παγκόσμια κοινότητα ασφάλειας στην ανάπτυξη της 'Μετα-κβαντικής Κρυπτογραφίας' (Post-Quantum Cryptography) με νέους αλγορίθμους ανθεκτικούς σε κβαντικές επιθέσεις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%BF%CF%81",
    "locale": "el-GR",
    "tags": ["shor-algorithm", "quantum-computing", "cryptography", "algorithms"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_101",
    "text": "Ποιος κρίσιμος μηχανισμός του ελεγκτή ενός δίσκου SSD κατανέμει ομοιόμορφα τις εγγραφές σε όλα τα κελιά flash για να αποτρέψει την πρόωρη φθορά τους;",
    "answers": ["Εξισορρόπηση φθοράς (Wear leveling)", "Υπερχρονισμός", "Ανασυγκρότηση δίσκου (Defrag)", "Διαχωρισμός τομέων"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Τα κελιά μνήμης NAND flash αντέχουν περιορισμένο αριθμό κύκλων εγγραφής/διαγραφής (P/E cycles). Ο αλγόριθμος wear leveling διασφαλίζει ότι όλα τα μπλοκ γράφονται εξίσου συχνά.",
    "funFacts": [
      "Υπάρχει δυναμικό (dynamic) και στατικό (static) wear leveling, με το στατικό να μετακινεί ακόμη και σπάνια μεταβαλλόμενα δεδομένα για να ελευθερώσει λιγότερο φθαρμένα μπλοκ.",
      "Χάρη στο wear leveling, ένας σύγχρονος δίσκος SSD διαρκεί συνήθως πάνω από 5-10 χρόνια κανονικής καθημερινής χρήσης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CF%83%CF%84%CE%B5%CF%81%CE%B5%CE%AC%CF%82_%CE%BA%CE%B1%CF%84%CE%AC%CF%83%CF%84%CE%B1%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["ssd", "wear-leveling", "hardware", "storage"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_102",
    "text": "Ποια εντολή του λειτουργικού συστήματος ενημερώνει έναν δίσκο SSD ποια μπλοκ δεδομένων θεωρούνται διαγραμμένα ώστε να προετοιμαστούν για εκ νέου εγγραφή;",
    "answers": ["FORMAT", "TRIM", "CHKDSK", "FDISK"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η εντολή TRIM αποτρέπει την πτώση της ταχύτητας εγγραφής του SSD επιτρέποντας στον ελεγκτή να εκτελεί διαδικασίες αποκομιδής απορριμμάτων (garbage collection) στο παρασκήνιο.",
    "funFacts": [
      "Επειδή η μνήμη flash δεν μπορεί να επανεγγράψει δεδομένα πάνω σε υφιστάμενα κελιά χωρίς προηγουμένως να διαγράψει ολόκληρο το μπλοκ, το TRIM είναι κρίσιμο για τη διατήρηση των υψηλών ταχυτήτων.",
      "Υποστηρίζεται αυτόματα σε όλα τα σύγχρονα λειτουργικά συστήματα από τα Windows 7, macOS Snow Leopard και Linux πυρήνα 2.6.33."
    ],
    "source": "https://el.wikipedia.org/wiki/Trim_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["trim", "ssd", "operating-systems", "storage"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_103",
    "text": "Ποιο σύγχρονο πρωτόκολλο διεπαφής σχεδιάστηκε ειδικά για ταχύτατους δίσκους SSD συνδεδεμένους απευθείας στον δίαυλο PCI Express αντικαθιστώντας το παλιό SATA;",
    "answers": ["IDE", "SCSI", "NVMe", "AGP"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το NVMe (Non-Volatile Memory Express) σχεδιάστηκε από το μηδέν για μνήμες στερεάς κατάστασης, υποστηρίζοντας έως και 64.000 ουρές εντολών με 64.000 εντολές ανά ουρά.",
    "funFacts": [
      "Σε αντίθεση με το παλιό πρωτόκολλο SATA που περιοριζόταν σε ταχύτητες γύρω στα 550 MB/s, οι δίσκοι NVMe PCIe 4.0 και 5.0 ξεπερνούν τα 7.000 έως 14.000 MB/s.",
      "Μειώνει δραματικά την καθυστέρηση (latency) επικοινωνώντας απευθείας με τους διαύλους του επεξεργαστή χωρίς περιττά ενδιάμεσα επίπεδα ελεγκτών."
    ],
    "source": "https://el.wikipedia.org/wiki/NVM_Express",
    "locale": "el-GR",
    "tags": ["nvme", "ssd", "hardware", "storage"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_104",
    "text": "Πόσους κύκλους ρολογιού ανά δευτερόλεπτο εκτελεί το εσωτερικό ρολόι ενός επεξεργαστή που λειτουργεί σε συχνότητα 3 GHz;",
    "answers": ["3 χιλιάδες", "3 εκατομμύρια", "300 εκατομμύρια", "3 δισεκατομμύρια"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρόθεμα 'Giga-' σημαίνει ένα δισεκατομμύριο (10^9). Συνεπώς, ένας επεξεργαστής στα 3 GHz εκτελεί 3.000.000.000 κύκλους ρολογιού κάθε δευτερόλεπτο.",
    "funFacts": [
      "Σε κάθε κύκλο ρολογιού, τα κυκλώματα του επεξεργαστή μπορούν να προχωρήσουν τα στάδια εκτέλεσης μίας ή περισσότερων εντολών (pipelining).",
      "Το φως στο κενό ταξιδεύει μόλις περίπου 10 εκατοστά κατά τη διάρκεια ενός και μόνο κύκλου ενός επεξεργαστή στα 3 GHz."
    ],
    "source": "https://el.wikipedia.org/wiki/Hertz",
    "locale": "el-GR",
    "tags": ["ghz", "cpu", "clock-speed", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_105",
    "text": "Πώς ονομάζεται η τεχνολογία της Intel που επιτρέπει σε έναν φυσικό πυρήνα επεξεργαστή να λειτουργεί ως δύο λογικοί πυρήνες εκτελώντας δύο σειρές εντολών ταυτόχρονα;",
    "answers": ["Hyper-Threading", "Turbo Boost", "Overclocking", "QuickPath"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Hyper-Threading (υλοποίηση της ταυτόχρονης πολυνημάτωσης - SMT) διπλασιάζει τους εικονικούς πυρήνες αξιοποιώντας αδρανείς υπολογιστικές μονάδες του επεξεργαστή.",
    "funFacts": [
      "Πρωτοεμφανίστηκε στους επεξεργαστές Xeon για διακομιστές και στη συνέχεια στον επιτραπέζιο Pentium 4 'Northwood' το 2002.",
      "Μπορεί να προσφέρει τυπική αύξηση απόδοσης μεταξύ 15% και 30% σε εφαρμογές με καλό παραλληλισμό χωρίς να απαιτεί διπλάσιο φυσικό πυρίτιο."
    ],
    "source": "https://el.wikipedia.org/wiki/Hyper-Threading",
    "locale": "el-GR",
    "tags": ["hyper-threading", "intel", "cpu", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_106",
    "text": "Ποιο επίπεδο κρυφής μνήμης (cache) στην ιεραρχία ενός σύγχρονου επεξεργαστή βρίσκεται πιο κοντά στις μονάδες εκτέλεσης και είναι το ταχύτερο αλλά με τη μικρότερη χωρητικότητα;",
    "answers": ["L3 Cache", "L1 Cache", "L2 Cache", "Κύρια μνήμη RAM"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μνήμη L1 (Level 1) cache είναι ενσωματωμένη απευθείας μέσα σε κάθε πυρήνα, προσφέροντας χρόνο προσπέλασης περίπου 1 νανοδευτερολέπτου (λίγων κύκλων ρολογιού).",
    "funFacts": [
      "Συνήθως χωρίζεται σε δύο διακριτά τμήματα: L1i για εντολές (instruction cache) και L1d για δεδομένα (data cache), με μεγέθη τυπικά από 32 έως 64 KB ανά πυρήνα.",
      "Η ιεραρχία προχωρά στην L2 (μεγαλύτερη αλλά ελαφρώς πιο αργή) και στην L3 (κοινόχρηστη για όλους τους πυρήνες, συνήθως από 16 έως 96 MB)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%81%CF%85%CF%86%CE%AE_%CE%BC%CE%BD%CE%AE%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["cache", "l1-cache", "cpu", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_107",
    "text": "Τι αντιπροσωπεύει η τιμή TDP (Thermal Design Power), μετρούμενη σε Watts, στις τεχνικές προδιαγραφές ενός επεξεργαστή ή κάρτας γραφικών;",
    "answers": ["Την ταχύτητα μεταφοράς δεδομένων στον δίαυλο μνήμης", "Τη συνολική χωρητικότητα των τρανζίστορ του τσιπ", "Τη μέγιστη θερμότητα που παράγει το τσιπ και πρέπει να αποβάλει το σύστημα ψύξης", "Τη μέγιστη τάση λειτουργίας σε Volts"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το TDP (Θερμική Ισχύς Σχεδίασης) καθορίζει τις απαιτήσεις του συστήματος ψύξης για να διατηρείται ο επεξεργαστής εντός ασφαλών ορίων θερμοκρασίας υπό κανονικό φορτίο.",
    "funFacts": [
      "Ενώ σχετίζεται με την κατανάλωση ρεύματος, το TDP δεν ισούται πάντα με τη μέγιστη στιγμιαία ηλεκτρική κατανάλωση, η οποία σε κατάσταση Turbo μπορεί να είναι σημαντικά υψηλότερη.",
      "Οι επεξεργαστές κινητών τηλεφώνων έχουν συνήθως TDP κάτω από 5 Watts, ενώ ισχυροί επεξεργαστές gaming PC μπορούν να ξεπεράσουν τα 150-250 Watts."
    ],
    "source": "https://el.wikipedia.org/wiki/TDP",
    "locale": "el-GR",
    "tags": ["tdp", "hardware", "cooling", "processors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_108",
    "text": "Ποιοι δύο απόφοιτοι του Στάνφορντ ίδρυσαν την εταιρεία τους σε ένα γκαράζ στο Πάλο Άλτο το 1939, γεγονός που θεωρείται η επίσημη ιστορική αφετηρία της Silicon Valley;",
    "answers": ["Στιβ Τζομπς και Στιβ Βόζνιακ", "Μπιλ Γκέιτς και Πολ Άλεν", "Λάρι Πέιτζ και Σεργκέι Μπριν", "Μπιλ Χιούλετ και Ντέιβιντ Πάκαρντ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μπιλ Χιούλετ (Bill Hewlett) και ο Ντέιβιντ Πάκαρντ (David Packard) ίδρυσαν την HP κατασκευάζοντας έναν ταλαντωτή ακουστικών συχνοτήτων (HP 200A).",
    "funFacts": [
      "Αποφάσισαν με στρίψιμο νομίσματος αν η εταιρεία τους θα ονομαζόταν Hewlett-Packard ή Packard-Hewlett.",
      "Ένας από τους πρώτους μεγάλους πελάτες τους ήταν τα στούντιο Walt Disney, που αγόρασαν οκτώ ταλαντωτές για τον έλεγχο των ηχητικών συστημάτων της ταινίας κινουμένων σχεδίων Fantasia (1940)."
    ],
    "source": "https://el.wikipedia.org/wiki/Hewlett-Packard",
    "locale": "el-GR",
    "tags": ["hewlett-packard", "silicon-valley", "founders", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_109",
    "text": "Ποια ιστορική εταιρεία ημιαγωγών που ιδρύθηκε το 1957 θεωρείται η «μητέρα» της Silicon Valley, καθώς πρώην στελέχη της ίδρυσαν την Intel, την AMD και δεκάδες άλλες εταιρείες;",
    "answers": ["Fairchild Semiconductor", "Texas Instruments", "Motorola", "National Semiconductor"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Fairchild Semiconductor υπήρξε το επίκεντρο της επανάστασης των ημιαγωγών, αναπτύσσοντας την επίπεδη διαδικασία (planar process) που επέτρεψε τη μαζική παραγωγή τσιπ.",
    "funFacts": [
      "Οι εταιρείες που δημιουργήθηκαν άμεσα ή έμμεσα από πρώην υπαλλήλους της Fairchild έμειναν γνωστές στον επιχειρηματικό κόσμο ως 'Fairchildren'.",
      "Μέχρι τα μέσα της δεκαετίας του 1980, υπολογίζεται ότι σχεδόν το 70% των εταιρειών τεχνολογίας στη Silicon Valley συνδέονταν με κάποιο τρόπο με αποφοίτους της Fairchild."
    ],
    "source": "https://el.wikipedia.org/wiki/Fairchild_Semiconductor",
    "locale": "el-GR",
    "tags": ["fairchild", "silicon-valley", "semiconductors", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_110",
    "text": "Ποιος χαρισματικός Αμερικανός επιχειρηματίας και πρώην επικεφαλής πωλήσεων της Fairchild Semiconductor ίδρυσε την εταιρεία Advanced Micro Devices (AMD) το 1969;",
    "answers": ["Γκόρντον Μουρ", "Τζέρι Σάντερς", "Ρόμπερτ Νόις", "Τσάρλι Σπορκ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζέρι Σάντερς (Jerry Sanders) ίδρυσε την AMD μαζί με επτά πρώην συναδέλφους του από τη Fairchild, οδηγώντας την εταιρεία ως βασικό ανταγωνιστή της Intel για δεκαετίες.",
    "funFacts": [
      "Έμεινε παροιμιώδης για το εκκεντρικό του στυλ και το επιθετικό του μότο: 'Οι άνθρωποι πρώτα, τα προϊόντα και τα κέρδη θα ακολουθήσουν'.",
      "Εξασφάλισε το 1982 μια κρίσιμη συμφωνία δεύτερης πηγής προμήθειας με την Intel για την παραγωγή επεξεργαστών x86 για τους υπολογιστές της IBM."
    ],
    "source": "https://el.wikipedia.org/wiki/AMD",
    "locale": "el-GR",
    "tags": ["amd", "jerry-sanders", "semiconductors", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'medium', 3, questions)

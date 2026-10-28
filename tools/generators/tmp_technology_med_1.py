# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "tech_med_011",
    "text": "Ποιο ιστορικό ερευνητικό κέντρο της Καλιφόρνια επινόησε τη δεκαετία του 1970 το γραφικό περιβάλλον χρήστη (GUI), το σύγχρονο ποντίκι και το Ethernet;",
    "answers": ["Xerox PARC", "Bell Labs", "MIT Media Lab", "IBM Almaden"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Xerox PARC (Palo Alto Research Center) υπήρξε η γενέτειρα πολλών θεμελιωδών τεχνολογιών των σύγχρονων προσωπικών υπολογιστών.",
    "funFacts": [
      "Ο Στιβ Τζομπς επισκέφθηκε το Xerox PARC το 1979 και εμπνεύστηκε άμεσα για τη δημιουργία των γραφικών περιβαλλόντων του Apple Lisa και Macintosh.",
      "Εκεί αναπτύχθηκε επίσης ο πρώτος πειραματικός εκτυπωτής λέιζερ από τον Γκάρι Στάρκγουεδερ."
    ],
    "source": "https://el.wikipedia.org/wiki/Xerox_PARC",
    "locale": "el-GR",
    "tags": ["xerox-parc", "gui", "history-tech", "research"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_012",
    "text": "Ποιος Αμερικανός επιστήμονας υπολογιστών δημιούργησε τη γλώσσα προγραμματισμού C και συν-ανέπτυξε το λειτουργικό σύστημα Unix στα εργαστήρια Bell;",
    "answers": ["Κεν Τόμπσον", "Ντένις Ρίτσι", "Μπιάρνε Στρούστρουπ", "Μπράιαν Κέρνιχαν"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ντένις Ρίτσι (Dennis Ritchie) ανέπτυξε τη γλώσσα C μεταξύ 1969 και 1973, πάνω στην οποία ξαναγράφτηκε ο πυρήνας του Unix.",
    "funFacts": [
      "Συνέγραψε μαζί με τον Μπράιαν Κέρνιχαν το ιστορικό βιβλίο 'The C Programming Language', γνωστό στην κοινότητα ως 'K&R'.",
      "Τιμήθηκε με το Βραβείο Turing το 1983 από κοινού με τον Κεν Τόμπσον για τη συνεισφορά τους στη θεωρία λειτουργικών συστημάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%AD%CE%BD%CE%B9%CF%82_%CE%A1%CE%AF%CF%84%CF%83%CE%B9",
    "locale": "el-GR",
    "tags": ["dennis-ritchie", "c-language", "unix", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_013",
    "text": "Ποιος Δανός επιστήμονας υπολογιστών ανέπτυξε τη γλώσσα προγραμματισμού C++ το 1979 ως αντικειμενοστραφή επέκταση της γλώσσας C;",
    "answers": ["Νίκλαους Βιρθ", "Άντερς Χέιλσμπεργκ", "Μπιάρνε Στρούστρουπ", "Ράσμους Λέρντορφ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μπιάρνε Στρούστρουπ (Bjarne Stroustrup) δημιούργησε την C++ στα εργαστήρια Bell Labs, αρχικά υπό την ονομασία 'C with Classes'.",
    "funFacts": [
      "Η C++ παραμένει η κυρίαρχη γλώσσα για την ανάπτυξη μηχανών βιντεοπαιχνιδιών (όπως Unreal Engine), λειτουργικών συστημάτων και χρηματοοικονομικών συστημάτων υψηλής συχνότητας.",
      "Το σύμβολο '++' στο όνομα προέρχεται από τον τελεστή αύξησης της γλώσσας C, υποδηλώνοντας την εξέλιξη της αρχικής γλώσσας."
    ],
    "source": "https://el.wikipedia.org/wiki/C%2B%2B",
    "locale": "el-GR",
    "tags": ["cpp", "programming", "stroustrup", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_014",
    "text": "Ποιος Καναδός επιστήμονας υπολογιστών θεωρείται ο κύριος δημιουργός της γλώσσας προγραμματισμού Java στην εταιρεία Sun Microsystems;",
    "answers": ["Τζον Μπάκους", "Γκίντο βαν Ρόσουμ", "Λάρι Γουόλ", "Τζέιμς Γκόσλινγκ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζέιμς Γκόσλινγκ (James Gosling) ηγήθηκε της ομάδας ανάπτυξης της Java στις αρχές της δεκαετίας του 1990 στη Sun Microsystems.",
    "funFacts": [
      "Η γλώσσα ονομαζόταν αρχικά 'Oak' (βελανιδιά), από ένα δέντρο που έβλεπε ο Γκόσλινγκ έξω από το παράθυρο του γραφείου του.",
      "Η διάσημη αρχή σχεδιασμού της Java συνοψίζεται στο σύνθημα: 'Write Once, Run Anywhere' (Γράψε μια φορά, τρέξε παντού) χάρη στην εικονική μηχανή JVM."
    ],
    "source": "https://el.wikipedia.org/wiki/Java",
    "locale": "el-GR",
    "tags": ["java", "gosling", "programming", "sun-microsystems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_015",
    "text": "Ποιοι δύο Αμερικανοί επιστήμονες ανέπτυξαν τη σουίτα πρωτοκόλλων TCP/IP και αναγνωρίζονται ευρέως ως οι «πατέρες του διαδικτύου»;",
    "answers": ["Βιντ Σερφ και Μπομπ Καν", "Τιμ Μπέρνερς-Λι και Ρομπέρ Καγιώ", "Κεν Τόμπσον και Ντένις Ρίτσι", "Στιβ Βόζνιακ και Στιβ Τζομπς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Βιντ Σερφ (Vint Cerf) και ο Μπομπ Καν (Bob Kahn) σχεδίασαν την αρχιτεκτονική TCP/IP το 1973, θέτοντας τα θεμέλια για την ενοποίηση διαφορετικών δικτύων.",
    "funFacts": [
      "Βραβεύτηκαν με το Προεδρικό Μετάλλιο της Ελευθερίας και το Βραβείο Turing το 2004 για το πρωτοποριακό τους έργο στη δικτύωση υπολογιστών.",
      "Ο Βιντ Σερφ εργάζεται από το 2005 στην Google ως 'Chief Internet Evangelist' σχεδιάζοντας ακόμη και διαπλανητικά πρωτόκολλα επικοινωνίας (Interplanetary Internet)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%BD%CF%84_%CE%A3%CE%B5%CF%81%CF%86",
    "locale": "el-GR",
    "tags": ["tcp-ip", "internet", "networking", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_016",
    "text": "Ποιος Αμερικανός μαθηματικός και ηλεκτρολόγος μηχανικός θεμελίωσε τη Θεωρία της Πληροφορίας με την ιστορική εργασία του το 1948;",
    "answers": ["Νόρμπερτ Βίνερ", "Κλοντ Σάνον", "Τζον φον Νόιμαν", "Κουρτ Γκέντελ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Κλοντ Σάνον (Claude Shannon) δημοσίευσε το 1948 τη μελέτη 'A Mathematical Theory of Communication', ορίζοντας την έννοια της πληροφορίας και του δυαδικού ψηφίου (bit).",
    "funFacts": [
      "Στη μεταπτυχιακή του διατριβή το 1937 απέδειξε πρώτος ότι η άλγεβρα Μπουλ μπορεί να εφαρμοστεί σε ηλεκτρικά κυκλώματα με διακόπτες.",
      "Ήταν επίσης γνωστός για τα εκκεντρικά του χόμπι στα εργαστήρια Bell, όπως το να κάνει μονοκύκλιο στους διαδρόμους παίζοντας ταυτόχρονα ζογκλερικά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%BF%CE%BD%CF%84_%CE%A3%CE%AC%CE%BD%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["claude-shannon", "information-theory", "mathematics", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_017",
    "text": "Ποιος κορυφαίος μαθηματικός περιέγραψε το 1945 την υπολογιστική αρχιτεκτονική όπου πρόγραμμα και δεδομένα αποθηκεύονται στην ίδια κοινή μνήμη;",
    "answers": ["Άλαν Τιούρινγκ", "Τσαρλς Μπάμπατζ", "Τζον φον Νόιμαν", "Έντσγκερ Ντάικστρα"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η αρχιτεκτονική Von Neumann (αποθηκευμένου προγράμματος) αποτελεί τη βάση για τη σχεδίαση σχεδόν όλων των σύγχρονων ηλεκτρονικών υπολογιστών γενικής χρήσης.",
    "funFacts": [
      "Περιγράφηκε για πρώτη φορά στην αναφορά 'First Draft of a Report on the EDVAC' τον Ιούνιο του 1945.",
      "Το κύριο θεωρητικό της μειονέκτημα είναι το λεγόμενο 'σημείο συμφόρησης φον Νόιμαν' (Von Neumann bottleneck), καθώς ο δίαυλος μνήμης περιορίζει τον ρυθμό διαμεταγωγής μεταξύ CPU και RAM."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CF%86%CE%BF%CE%BD_%CE%9D%CF%8C%CE%B9%CE%BC%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["von-neumann", "architecture", "hardware", "computer-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_018",
    "text": "Ποιος υπερυπολογιστής της IBM νίκησε το 1997 τον παγκόσμιο πρωταθλητή Γκάρι Κασπάροφ, σε ιστορική στιγμή για την τεχνητή νοημοσύνη;",
    "answers": ["Watson", "HAL 9000", "Deep Thought", "Deep Blue"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο υπερυπολογιστής σκακιού Deep Blue της IBM νίκησε τον Κασπάροφ σε αναμέτρηση έξι παρτίδων με σκορ 3,5 - 2,5 στη Νέα Υόρκη τον Μάιο του 1997.",
    "funFacts": [
      "Ήταν ικανός να υπολογίζει και να αξιολογεί περίπου 200 εκατομμύρια πιθανές σκακιστικές θέσεις ανά δευτερόλεπτο.",
      "Χρησιμοποιούσε συνδυασμό προηγμένου λογισμικού αναζήτησης δέντρου και 480 ειδικά κατασκευασμένων τσιπ υλικού (ASIC) αποκλειστικά για σκάκι."
    ],
    "source": "https://el.wikipedia.org/wiki/Deep_Blue",
    "locale": "el-GR",
    "tags": ["deep-blue", "chess", "ai", "ibm"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_019",
    "text": "Ποιο σύστημα τεχνητής νοημοσύνης της Google DeepMind νίκησε το 2016 τον παγκόσμιο πρωταθλητή Λι Σεντόλ στο εξαιρετικά πολύπλοκο αρχαίο παιχνίδι Go;",
    "answers": ["AlphaGo", "Deep Blue", "Stockfish", "AlphaFold"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το AlphaGo επικράτησε με σκορ 4-1 σε αναμέτρηση στη Σεούλ, επιτυγχάνοντας ένα τεχνολογικό ορόσημο που οι ειδικοί θεωρούσαν ότι απείχε τουλάχιστον μια δεκαετία.",
    "funFacts": [
      "Στην 37η κίνηση της δεύτερης παρτίδας, το AlphaGo πραγματοποίησε μια κίνηση τόσο απροσδόκητη και ιδιοφυή που άφησε άναυδους όλους τους διεθνείς σχολιαστές.",
      "Χρησιμοποίησε συνδυασμό βαθιών συνελικτικών νευρωνικών δικτύων (Deep CNNs) και ενισχυτικής μάθησης (Reinforcement Learning) παίζοντας εκατομμύρια παρτίδες εναντίον του εαυτού του."
    ],
    "source": "https://el.wikipedia.org/wiki/AlphaGo",
    "locale": "el-GR",
    "tags": ["alphago", "ai", "deepmind", "machine-learning"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_020",
    "text": "Σε ποιο έτος κυκλοφόρησε ο πρωτοποριακός υπολογιστής IBM PC (μοντέλο 5150) που καθιέρωσε την αρχιτεκτονική των σύγχρονων προσωπικών υπολογιστών PC;",
    "answers": ["1976", "1981", "1984", "1989"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο IBM Personal Computer κυκλοφόρησε τον Αύγουστο του 1981 με επεξεργαστή Intel 8088 στα 4,77 MHz και λειτουργικό σύστημα PC-DOS από τη Microsoft.",
    "funFacts": [
      "Η IBM επέλεξε ανοιχτή αρχιτεκτονική με εξαρτήματα τρίτων κατασκευαστών, γεγονός που επέτρεψε τη δημιουργία της τεράστιας βιομηχανίας των 'IBM PC συμβατών' κλώνων.",
      "Το περιοδικό TIME ανακήρυξε τον υπολογιστή PC ως 'Πρόσωπο της Χρονιάς' (Machine of the Year) για το 1982."
    ],
    "source": "https://el.wikipedia.org/wiki/IBM_PC",
    "locale": "el-GR",
    "tags": ["ibm-pc", "history-tech", "hardware", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_021",
    "text": "Ποιο μοντέλο οικιακού υπολογιστή που κυκλοφόρησε το 1982 κατέχει το ρεκόρ Γκίνες ως ο προσωπικός υπολογιστής με τις περισσότερες πωλήσεις στην ιστορία;",
    "answers": ["ZX Spectrum", "Apple II", "Commodore 64", "Atari 800"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Commodore 64 (C64) πούλησε εκτιμώμενα μεταξύ 12,5 και 17 εκατομμυρίων μονάδων παγκοσμίως, κυριαρχώντας στην αγορά της δεκαετίας του 1980.",
    "funFacts": [
      "Διέθετε 64 Kilobytes μνήμης RAM και το θρυλικό τσιπ ήχου SID 6581 που παρήγαγε πολυφωνική μουσική ανώτερη από τους περισσότερους υπολογιστές της εποχής.",
      "Πωλούνταν απευθείας σε πολυκαταστήματα και καταστήματα παιχνιδιών αντί αποκλειστικά σε εξειδικευμένα καταστήματα υπολογιστών."
    ],
    "source": "https://el.wikipedia.org/wiki/Commodore_64",
    "locale": "el-GR",
    "tags": ["commodore-64", "gaming", "history-tech", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_022",
    "text": "Ποια ιστορική κατασκευάστρια εταιρεία κυκλοφόρησε το 1985 τον υπολογιστή Amiga 1000, εισάγοντας προηγμένα γραφικά και πραγματικό προληπτικό multitasking;",
    "answers": ["Atari", "Apple", "Sinclair", "Commodore"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Commodore εξαγόρασε την Amiga Corporation και παρουσίασε την Amiga 1000 τον Ιούλιο του 1985 με εξειδικευμένα προσαρμοσμένα τσιπ για γραφικά και ήχο.",
    "funFacts": [
      "Στην επίσημη παρουσίαση στη Νέα Υόρκη, ο διάσημος καλλιτέχνης Άντι Γουόρχολ ζωγράφισε ζωντανά ένα ψηφιακό πορτρέτο της τραγουδίστριας Ντέμπι Χάρι πάνω σε μια Amiga.",
      "Το λειτουργικό της σύστημα (AmigaOS) υποστήριζε πλήρες preemptive multitasking χρόνια πριν καθιερωθεί σε Windows και Mac."
    ],
    "source": "https://el.wikipedia.org/wiki/Amiga",
    "locale": "el-GR",
    "tags": ["amiga", "commodore", "multimedia", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_023",
    "text": "Ποιος Αμερικανός προγραμματιστής και ακτιβιστής ίδρυσε το κίνημα ελεύθερου λογισμικού (Free Software Foundation) και το εγχείρημα GNU το 1983;",
    "answers": ["Ρίτσαρντ Στόλμαν", "Λίνους Τόρβαλντς", "Έρικ Ρέιμοντ", "Μπρους Πέρενς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ρίτσαρντ Στόλμαν (Richard Stallman) ξεκίνησε το GNU Project με στόχο τη δημιουργία ενός πλήρως ελεύθερου λειτουργικού συστήματος συμβατού με το Unix.",
    "funFacts": [
      "Επινόησε τη νομική έννοια του 'Copyleft' και συνέταξε τη γενική άδεια δημόσιας χρήσης GNU General Public License (GPL).",
      "Το όνομα GNU είναι ένα αναδρομικό ακρωνύμιο που σημαίνει: 'GNU's Not Unix' (Το GNU δεν είναι Unix)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AF%CF%84%CF%83%CE%B1%CF%81%CE%BD%CF%84_%CE%A3%CF%84%CF%8C%CE%BB%CE%BC%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["stallman", "gnu", "free-software", "open-source"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_024",
    "text": "Ποιος πρωτοπόρος μηχανικός των Bell Labs σχεδίασε την αρχική έκδοση του Unix, τη γλώσσα προγραμματισμού B και συν-δημιούργησε τη γλώσσα Go στην Google;",
    "answers": ["Τζον Μακάρθι", "Κεν Τόμπσον", "Ντόναλντ Κνουθ", "Έντσγκερ Ντάικστρα"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Κεν Τόμπσον (Ken Thompson) έγραψε την πρώτη έκδοση του Unix το 1969 σε έναν υπολογιστή PDP-7 και αργότερα συνεισέφερε στη δημιουργία της κωδικοποίησης UTF-8.",
    "funFacts": [
      "Έγραψε το πρώτο πρόγραμμα του Unix για να μπορέσει να παίξει το διαστημικό παιχνίδι 'Space Travel' που είχε προγραμματίσει.",
      "Μαζί με τον Ρομπ Πάικ δημιούργησαν στα Bell Labs το πειραματικό κατανεμημένο λειτουργικό σύστημα Plan 9."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B5%CE%BD_%CE%A4%CF%8C%CE%BC%CF%80%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["ken-thompson", "unix", "bell-labs", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_025",
    "text": "Ποιος Αμερικανός προγραμματιστής και επενδυτής συν-δημιούργησε τον ιστορικό φυλλομετρητή NCSA Mosaic και συνίδρυσε την εταιρεία Netscape;",
    "answers": ["Τζιμ Κλαρκ", "Μπιλ Τζόι", "Μαρκ Άντρισεν", "Τιμ Ο'Ράιλι"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μαρκ Άντρισεν (Marc Andreessen) ανέπτυξε το Mosaic στο Πανεπιστήμιο του Ιλινόις και στη συνέχεια ίδρυσε τη Netscape, πυροδοτώντας την έκρηξη του διαδικτύου τη δεκαετία του 1990.",
    "funFacts": [
      "Η αρχική δημόσια εγγραφή (IPO) της Netscape στο χρηματιστήριο το 1995 θεωρείται ιστορικά η αφετηρία της επενδυτικής 'φούσκας Dot-com'.",
      "Είναι συνιδρυτής του κολοσσιαίου ταμείου επιχειρηματικών συμμετοχών Andreessen Horowitz (a16z) στη Silicon Valley."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%BA_%CE%86%CE%BD%CF%84%CF%81%CE%B9%CF%83%CE%B5%CE%BD",
    "locale": "el-GR",
    "tags": ["andreessen", "netscape", "browsers", "internet-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_026",
    "text": "Ποιος Αμερικανός τεχνολόγος επινόησε τη γλώσσα JavaScript το 1995 και συνίδρυσε αργότερα το ίδρυμα Mozilla και τον περιηγητή Brave;",
    "answers": ["Ράσμους Λέρντορφ", "Γκίντο βαν Ρόσουμ", "Ντόναλντ Κνουθ", "Μπρένταν Άιχ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μπρένταν Άιχ (Brendan Eich) ανέπτυξε το αρχικό πρωτότυπο της JavaScript στη Netscape και διετέλεσε για χρόνια επικεφαλής τεχνολογίας (CTO) της Mozilla.",
    "funFacts": [
      "Δημιούργησε την πρώτη λειτουργική έκδοση της JavaScript μέσα σε μόλις 10 ημέρες τον Μάιο του 1995.",
      "Το 2015 ίδρυσε την Brave Software, δημιουργώντας τον ομώνυμο φυλλομετρητή που εστιάζει στην ιδιωτικότητα και το σύστημα αμοιβών Basic Attention Token (BAT)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%81%CE%AD%CE%BD%CF%84%CE%B1%CE%BD_%CE%86%CE%B9%CF%87",
    "locale": "el-GR",
    "tags": ["brendan-eich", "javascript", "mozilla", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_027",
    "text": "Ποιος Δανο-γροιλανδός προγραμματιστής δημιούργησε την πρώτη έκδοση της δημοφιλούς γλώσσας σεναρίων διακομιστή PHP το 1994;",
    "answers": ["Ράσμους Λέρντορφ", "Μπιάρνε Στρούστρουπ", "Άντερς Χέιλσμπεργκ", "Ντέιβιντ Χάινεμαϊερ Χάνσον"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ράσμους Λέρντορφ (Rasmus Lerdorf) έγραψε αρχικά τη γλώσσα σε C για να παρακολουθεί τις επισκέψεις στο προσωπικό του διαδικτυακό βιογραφικό.",
    "funFacts": [
      "Τα αρχικά PHP σήμαιναν αρχικά 'Personal Home Page Tools', πριν υιοθετηθεί το αναδρομικό ακρωνύμιο 'PHP: Hypertext Preprocessor'.",
      "Σήμερα η PHP τροφοδοτεί σχεδόν το 75% όλων των ιστότοπων με γνωστή γλώσσα διακομιστή, χάρη σε πλατφόρμες όπως το WordPress."
    ],
    "source": "https://el.wikipedia.org/wiki/PHP",
    "locale": "el-GR",
    "tags": ["php", "programming", "web-development", "servers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_028",
    "text": "Ποιος Ιάπωνας επιστήμονας υπολογιστών σχεδίασε τη γλώσσα προγραμματισμού Ruby τη δεκαετία του 1990 εστιάζοντας στην παραγωγικότητα και την ευχαρίστηση του προγραμματιστή;",
    "answers": ["Σατόρου Ιβάτα", "Γιουκιχίρο Ματσουμότο", "Χιντέο Κοτζίμα", "Μασαγιόσι Σον"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Γιουκιχίρο Ματσουμότο (γνωστός στην κοινότητα ως 'Matz') κυκλοφόρησε τη Ruby το 1995 συνδυάζοντας στοιχεία από Perl, Smalltalk και Lisp.",
    "funFacts": [
      "Το όνομα 'Ruby' (ρουμπίνι) επιλέχθηκε ως αναφορά στο γενέθλιο πετράδι ενός συναδέλφου του και ως λογοπαίγνιο με το όνομα της γλώσσας Perl (μαργαριτάρι).",
      "Η δημοτικότητα της γλώσσας εκτοξεύτηκε διεθνώς στα μέσα της δεκαετίας του 2000 με την εμφάνιση του διαδικτυακού πλαισίου Ruby on Rails."
    ],
    "source": "https://el.wikipedia.org/wiki/Ruby",
    "locale": "el-GR",
    "tags": ["ruby", "programming", "software", "japan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_029",
    "text": "Ποιος Ελβετός καθηγητής επιστήμης υπολογιστών και νομπελίστας Turing ανέπτυξε τις γλώσσες προγραμματισμού Pascal, Modula-2 και Oberon;",
    "answers": ["Έντσγκερ Ντάικστρα", "Κ.Α.Ρ. Χορ", "Νίκλαους Βιρθ", "Τζον Μπάκους"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Νίκλαους Βιρθ (Niklaus Wirth) σχεδίασε την Pascal το 1970 με στόχο τη διδασκαλία του δομημένου προγραμματισμού και της ορθής μηχανικής λογισμικού.",
    "funFacts": [
      "Διατύπωσε τον 'Νόμο του Βιρθ', σύμφωνα με τον οποίο το λογισμικό επιβραδύνεται ταχύτερα από όσο επιταχύνεται το υλικό (hardware).",
      "Βραβεύτηκε με το Βραβείο Turing το 1984 για την ανάπτυξη μιας σειράς πρωτοποριακών γλωσσών υπολογιστών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BB%CE%B1%CE%BF%CF%85%CF%82_%CE%92%CE%B9%CF%81%CE%B8",
    "locale": "el-GR",
    "tags": ["pascal", "wirth", "programming", "computer-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_030",
    "text": "Ποιος κορυφαίος επιστήμονας υπολογιστών συνέγραψε το μνημειώδες πολύτομο σύγγραμμα «The Art of Computer Programming» και δημιούργησε το τυπογραφικό σύστημα TeX;",
    "answers": ["Άλαν Τιούρινγκ", "Κλοντ Σάνον", "Τζον φον Νόιμαν", "Ντόναλντ Κνουθ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ντόναλντ Κνουθ (Donald Knuth) θεωρείται ο θεμελιωτής της συστηματικής μαθηματικής ανάλυσης αλγορίθμων και τιμήθηκε με το Βραβείο Turing το 1974.",
    "funFacts": [
      "Δημιούργησε το σύστημα στοιχειοθεσίας TeX στα τέλη της δεκαετίας του 1970 επειδή δεν ήταν ικανοποιημένος από την τυπογραφική ποιότητα των μαθηματικών βιβλίων του.",
      "Είναι διάσημος επειδή προσφέρει συμβολικές επιταγές (Knuth reward checks) αξίας 2,56 δολαρίων (ένα 'εξαδικό δολάριο') σε όποιον εντοπίσει τυπογραφικό λάθος στα βιβλία του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CF%8C%CE%BD%CE%B1%CE%BB%CE%BD%CF%84_%CE%9A%CE%BD%CE%BF%CF%85%CE%B8",
    "locale": "el-GR",
    "tags": ["knuth", "algorithms", "tex", "computer-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_031",
    "text": "Ποιος Ολλανδός πρωτοπόρος της πληροφορικής επινόησε τον κλασικό αλγόριθμο εύρεσης της συντομότερης διαδρομής σε έναν γράφο το 1956;",
    "answers": ["Έντσγκερ Ντάικστρα", "Γκίντο βαν Ρόσουμ", "Άντριου Τανενμπάουμ", "Ρόμπερτ Τάρτζαν"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος του Dijkstra λύνει το πρόβλημα εύρεσης της συντομότερης διαδρομής από έναν κόμβο-πηγή προς όλους τους άλλους σε έναν σταθμισμένο γράφο.",
    "funFacts": [
      "Ο Ντάικστρα επινόησε τον διάσημο αλγόριθμο μέσα σε μόλις 20 λεπτά ενώ έπινε καφέ με την αρραβωνιαστικιά του σε μια καφετέρια στο Άμστερνταμ.",
      "Έγραψε επίσης το ιστορικό άρθρο 'Go To Statement Considered Harmful' το 1968, καθιερώνοντας οριστικά τον δομημένο προγραμματισμό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BD%CF%84%CF%83%CF%87%CE%B5%CF%81_%CE%9D%CF%84%CE%AC%CE%B9%CE%BA%CF%83%CF%84%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["dijkstra", "algorithms", "graphs", "computer-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_032",
    "text": "Ποιοι τρεις επιστήμονες του MIT επινόησαν το 1977 τον διάσημο αλγόριθμο ασύμμετρης κρυπτογραφίας δημοσίου κλειδιού RSA;",
    "answers": ["Ντίφι, Χέλμαν και Μερκλ", "Ριβέστ, Σαμίρ και Άντλεμαν", "Σάνον, Τιούρινγκ και Νόιμαν", "Κερνέλ, Τόμσον και Ρίτσι"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ρον Ριβέστ (Ron Rivest), ο Άντι Σαμίρ (Adi Shamir) και ο Λέοναρντ Άντλεμαν (Leonard Adleman) συνδύασαν τα αρχικά των επωνύμων τους για να ονομάσουν τον RSA.",
    "funFacts": [
      "Η μαθηματική ασφάλεια του RSA βασίζεται στην πρακτική υπολογιστική δυσκολία παραγοντοποίησης του γινομένου δύο πολύ μεγάλων πρώτων αριθμών.",
      "Οι τρεις δημιουργοί βραβεύτηκαν από κοινού με το Βραβείο Turing το 2002 για τη θεμελίωση της πρακτικής κρυπτογραφίας δημοσίου κλειδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/RSA_(%CE%BA%CF%81%CF%85%CF%80%CF%84%CE%BF%CF%83%CF%8D%CF%83%CF%84%CE%B7%CE%BC%CE%B1)",
    "locale": "el-GR",
    "tags": ["rsa", "cryptography", "security", "mathematics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_033",
    "text": "Ποιοι δύο κρυπτογράφοι επινόησαν το 1976 το πρώτο πρακτικό πρωτόκολλο ασφαλούς ανταλλαγής κλειδιών πάνω από ένα μη ασφαλές δημόσιο κανάλι επικοινωνίας;",
    "answers": ["Άλαν Τιούρινγκ και Γκόρντον Γουέλτσμαν", "Ρον Ριβέστ και Άντι Σαμίρ", "Γουίτφιλντ Ντίφι και Μάρτιν Χέλμαν", "Κλοντ Σάνον και Ραλφ Χάρτλεϊ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρωτόκολλο ανταλλαγής κλειδιών Diffie-Hellman εισήγαγε για πρώτη φορά την έννοια της κρυπτογραφίας δημοσίου κλειδιού χωρίς προηγούμενη ανταλλαγή μυστικού κωδικού.",
    "funFacts": [
      "Η δημοσίευση της εργασίας τους 'New Directions in Cryptography' το 1976 άλλαξε ριζικά την επιστήμη της ασφάλειας πληροφοριών.",
      "Βραβεύτηκαν με το Βραβείο Turing το 2015 για τη θεμελίωση της κρυπτογραφίας δημοσίου κλειδιού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE_%CE%BA%CE%BB%CE%B5%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD_%CE%9D%CF%84%CE%AF%CF%86%CE%B9-%CE%A7%CE%AD%CE%BB%CE%BC%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["diffie-hellman", "cryptography", "security", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_034",
    "text": "Ποιος Αμερικανός προγραμματιστής και κρυπτογράφος ανέπτυξε το πρόγραμμα κρυπτογράφησης ηλεκτρονικού ταχυδρομείου PGP (Pretty Good Privacy) το 1991;",
    "answers": ["Έντουαρντ Σνόουντεν", "Μπρους Σνάιερ", "Κέβιν Μίτνικ", "Φιλ Ζίμερμαν"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Φιλ Ζίμερμαν (Phil Zimmermann) κυκλοφόρησε το PGP δωρεάν για την προστασία των ανθρωπίνων δικαιωμάτων και του απορρήτου των ψηφιακών επικοινωνιών.",
    "funFacts": [
      "Η κυβέρνηση των ΗΠΑ ξεκίνησε ποινική έρευνα εναντίον του για παράνομη εξαγωγή πολεμικού υλικού όταν το PGP εξαπλώθηκε διεθνώς μέσω διαδικτύου.",
      "Για να παρακάμψει τους περιορισμούς εξαγωγής λογισμικού, ο Ζίμερμαν τύπωσε ολόκληρο τον πηγαίο κώδικα σε βιβλίο, εκμεταλλευόμενος την προστασία της ελευθερίας του λόγου."
    ],
    "source": "https://el.wikipedia.org/wiki/Pretty_Good_Privacy",
    "locale": "el-GR",
    "tags": ["pgp", "cryptography", "privacy", "security"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_035",
    "text": "Ποιο εξαιρετικά εξελιγμένο κακόβουλο σκουλήκι κυβερνοπολέμου ανακαλύφθηκε το 2010 έχοντας σαμποτάρει φυσικά τις συσκευές φυγοκέντρησης ουρανίου στο Ιράν;",
    "answers": ["Stuxnet", "WannaCry", "ILOVEYOU", "Conficker"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Stuxnet στόχευε βιομηχανικά συστήματα ελέγχου SCADA της Siemens και προκάλεσε φυσική καταστροφή στις εγκαταστάσεις εμπλουτισμού της Νατάνζ.",
    "funFacts": [
      "Θεωρείται το πρώτο γνωστό ψηφιακό κυβερνοόπλο που προκάλεσε πραγματική φυσική καταστροφή σε βιομηχανική υποδομή στον φυσικό κόσμο.",
      "Εκμεταλλευόταν ταυτόχρονα τέσσερις άγνωστες μέχρι τότε ευπάθειες μηδενικής ημέρας (Zero-day exploits) στα Windows."
    ],
    "source": "https://el.wikipedia.org/wiki/Stuxnet",
    "locale": "el-GR",
    "tags": ["stuxnet", "cyberwarfare", "malware", "security"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_036",
    "text": "Ποιο ήταν το πρώτο ιστορικό «σκουλήκι» υπολογιστών που εξαπλώθηκε στο διαδίκτυο (ARPANET) τον Νοέμβριο του 1988 παραλύοντας χιλιάδες συστήματα Unix;",
    "answers": ["Melissa", "Morris Worm", "Brain", "Creeper"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Morris Worm γράφτηκε από τον Ρόμπερτ Τάπαν Μόρις, φοιτητή του Πανεπιστημίου Κορνέλ, προκαλώντας μαζική άρνηση εξυπηρέτησης σε περίπου 6.000 υπολογιστές.",
    "funFacts": [
      "Ο Μόρις υποστήριξε ότι στόχος του ήταν να μετρήσει το πραγματικό μέγεθος του τότε διαδικτύου, αλλά ένα σφάλμα στον κώδικα προκαλούσε ανεξέλεγκτο πολλαπλασιασμό.",
      "Έγινε το πρώτο άτομο που καταδικάστηκε βάσει του αμερικανικού νόμου περί απάτης και κατάχρησης υπολογιστών (CFAA) του 1986, ενώ αργότερα έγινε καθηγητής στο MIT."
    ],
    "source": "https://el.wikipedia.org/wiki/Morris_worm",
    "locale": "el-GR",
    "tags": ["morris-worm", "malware", "arpanet", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_037",
    "text": "Ποια σοβαρότατη ευπάθεια ασφαλείας ανακαλύφθηκε το 2014 στη δημοφιλή βιβλιοθήκη OpenSSL, επιτρέποντας την ανάγνωση κρυφών δεδομένων μνήμης διακομιστών;",
    "answers": ["Shellshock", "Dirty COW", "Heartbleed", "Log4Shell"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Heartbleed (CVE-2014-0160) ήταν ένα σφάλμα υπερχείλισης προσωρινής μνήμης (buffer over-read) στην υλοποίηση της επέκτασης Heartbeat του πρωτοκόλλου TLS.",
    "funFacts": [
      "Επέτρεπε σε οποιονδήποτε στο διαδίκτυο να διαβάζει έως και 64 Kilobytes μνήμης του διακομιστή, περιλαμβάνοντας μυστικά κλειδιά κρυπτογράφησης και κωδικούς χρηστών.",
      "Επηρέασε περίπου το 17% όλων των ασφαλών διακομιστών ιστού παγκοσμίως (περίπου μισό εκατομμύριο ιστότοπους)."
    ],
    "source": "https://el.wikipedia.org/wiki/Heartbleed",
    "locale": "el-GR",
    "tags": ["heartbleed", "openssl", "security", "vulnerabilities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_038",
    "text": "Ποιες δύο κρίσιμες ευπάθειες υλικού ανακαλύφθηκαν στις αρχές του 2018 εκμεταλλευόμενες την κερδοσκοπική εκτέλεση (speculative execution) των σύγχρονων επεξεργαστών;",
    "answers": ["Rowhammer και Stuxnet", "Heartbleed και Shellshock", "WannaCry και Petya", "Meltdown και Spectre"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι ευπάθειες Meltdown και Spectre επέτρεπαν σε κακόβουλο λογισμικό να διαβάζει ευαίσθητα δεδομένα από τη μνήμη του πυρήνα του λειτουργικού συστήματος παρακάμπτοντας τους μηχανισμούς απομόνωσης.",
    "funFacts": [
      "Επηρέασαν σχεδόν όλους τους επεξεργαστές Intel, AMD και ARM που είχαν κατασκευαστεί τις τελευταίες δύο δεκαετίες.",
      "Η αντιμετώπισή τους απαιτούσε ενημερώσεις μικροκώδικα (microcode) και λειτουργικών συστημάτων που σε ορισμένες περιπτώσεις μείωσαν την απόδοση των επεξεργαστών."
    ],
    "source": "https://el.wikipedia.org/wiki/Meltdown_(%CE%B5%CF%85%CF%80%CE%AC%CE%B8%CE%B5%CE%B9%CE%B1_%CE%B1%CF%83%CF%86%CE%B1%CE%BB%CE%B5%CE%AF%CE%B1%CF%82)",
    "locale": "el-GR",
    "tags": ["meltdown", "spectre", "hardware", "cpu-security"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_039",
    "text": "Πόσα διακριτά επίπεδα (layers) ορίζει το διεθνές θεωρητικό μοντέλο αναφοράς διασύνδεσης ανοιχτών συστημάτων (OSI Model);",
    "answers": ["7 επίπεδα", "4 επίπεδα", "5 επίπεδα", "10 επίπεδα"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το μοντέλο OSI αποτελείται από 7 επίπεδα: Φυσικό, Σύνδεσης Δεδομένων, Δικτύου, Μεταφοράς, Συνόδου, Παρουσίασης και Εφαρμογής.",
    "funFacts": [
      "Αναπτύχθηκε από τον Διεθνή Οργανισμό Τυποποίησης (ISO) το 1984 για να περιγράψει τη ροή δεδομένων στα τηλεπικοινωνιακά δίκτυα.",
      "Στην πράξη, το διαδίκτυο βασίζεται στο πιο απλοποιημένο μοντέλο TCP/IP, το οποίο περιλαμβάνει συνήθως 4 ή 5 επίπεδα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CF%84%CE%AD%CE%BB%CE%BF_%CE%91%CE%BD%CE%B1%CF%86%CE%BF%CF%81%CE%AC%CF%82_OSI",
    "locale": "el-GR",
    "tags": ["osi-model", "networking", "protocols", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_040",
    "text": "Ποιο πρωτόκολλο του επιπέδου μεταφοράς είναι ασυνδέδετο (connectionless) και προτιμάται για gaming και ζωντανό streaming λόγω ελάχιστης καθυστέρησης;",
    "answers": ["TCP", "UDP", "FTP", "BGP"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το UDP (User Datagram Protocol) αποστέλλει πακέτα χωρίς χειραψία σύνδεσης ή επιβεβαίωση παραλαβής, προσφέροντας μέγιστη ταχύτητα και χαμηλό latency.",
    "funFacts": [
      "Σε αντίθεση με το TCP που ξαναστέλνει χαμένα πακέτα, το UDP απλώς τα αγνοεί, κάτι ιδανικό για ζωντανή φωνή και βίντεο όπου ένα καθυστερημένο πακέτο είναι άχρηστο.",
      "Ο σχεδιασμός του UDP έγινε από τον Ντέιβιντ Ριντ το 1980 και καθορίστηκε στο RFC 768."
    ],
    "source": "https://el.wikipedia.org/wiki/User_Datagram_Protocol",
    "locale": "el-GR",
    "tags": ["udp", "networking", "protocols", "streaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_041",
    "text": "Ποιος είναι ο καθιερωμένος προεπιλεγμένος αριθμός θύρας (port number) για την ασφαλή, κρυπτογραφημένη περιήγηση ιστού μέσω HTTPS;",
    "answers": ["Port 80", "Port 21", "Port 443", "Port 8080"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η θύρα 443 TCP είναι η παγκοσμίως δεσμευμένη θύρα για το ασφαλές πρωτόκολλο επικοινωνίας HTTPS (HTTP over TLS/SSL).",
    "funFacts": [
      "Η μη κρυπτογραφημένη κίνηση απλού HTTP χρησιμοποιεί παραδοσιακά τη θύρα 80.",
      "Η θύρα 443 κατοχυρώθηκε επίσημα για το HTTPS από τον Πολ Σάτον της Netscape το 1994."
    ],
    "source": "https://el.wikipedia.org/wiki/HTTPS",
    "locale": "el-GR",
    "tags": ["https", "networking", "ports", "security"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_042",
    "text": "Ποια κλασική προεπιλεγμένη θύρα TCP χρησιμοποιείται συνήθως από το πρωτόκολλο ασφαλούς απομακρυσμένης διαχείρισης διακομιστών SSH;",
    "answers": ["Port 25", "Port 53", "Port 110", "Port 22"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρωτόκολλο SSH (Secure Shell) ακούει προεπιλεγμένα στη θύρα 22 TCP παρέχοντας κρυπτογραφημένη πρόσβαση στη γραμμή εντολών απομακρυσμένων μηχανημάτων.",
    "funFacts": [
      "Ο δημιουργός του SSH, Τάτου Ύλονεν, ζήτησε και έλαβε τη θύρα 22 από τον οργανισμό IANA επειδή βρισκόταν ανάμεσα στη θύρα 21 (FTP) και 23 (Telnet).",
      "Αντικατέστησε τα παλαιότερα ανασφαλή πρωτόκολλα Telnet και rlogin, τα οποία μετέδιδαν κωδικούς σε απλό μη κρυπτογραφημένο κείμενο."
    ],
    "source": "https://el.wikipedia.org/wiki/Secure_Shell",
    "locale": "el-GR",
    "tags": ["ssh", "networking", "ports", "servers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_043",
    "text": "Ποιος τύπος λογικής πύλης μνήμης flash κυριαρχεί σε όλους τους σύγχρονους δίσκους SSD, κάρτες μνήμης SD και smartphones;",
    "answers": ["NAND flash", "NOR flash", "AND flash", "XOR flash"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μνήμη NAND flash προσφέρει πολύ μεγαλύτερη πυκνότητα αποθήκευσης, ταχύτερη εγγραφή και χαμηλότερο κόστος ανά gigabyte σε σχέση με τη NOR flash.",
    "funFacts": [
      "Εφευρέθηκε από τον Φούτζιο Μασουόκα στην Toshiba το 1989.",
      "Η σύγχρονη τεχνολογία 3D NAND στοιβάζει δεκάδες ή και εκατοντάδες στρώματα κυψελών μνήμης κατακόρυφα για εκτόξευση της χωρητικότητας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BD%CE%AE%CE%BC%CE%B7_flash",
    "locale": "el-GR",
    "tags": ["nand", "flash-memory", "storage", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_044",
    "text": "Ποια διάταξη ανεξάρτητων δίσκων (RAID) χρησιμοποιεί τη μέθοδο του καθρεπτισμού (mirroring) αντιγράφοντας τα ίδια δεδομένα σε δύο δίσκους για ασφάλεια;",
    "answers": ["RAID 0", "RAID 1", "RAID 5", "RAID 10"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το RAID 1 προσφέρει πλήρη πλεονασμό αποθηκεύοντας πανομοιότυπα αντίγραφα δεδομένων σε δύο ξεχωριστούς δίσκους, προστατεύοντας από αστοχία του ενός.",
    "funFacts": [
      "Το κύριο μειονέκτημα του RAID 1 είναι ότι η συνολική αξιοποιήσιμη χωρητικότητα ισούται με τη χωρητικότητα του μικρότερου δίσκου (χάνεται το 50% του συνολικού χώρου).",
      "Αντίθετα, το RAID 0 μοιράζει τα δεδομένα σε λωρίδες (striping) αυξάνοντας την ταχύτητα αλλά χωρίς καμία προστασία από βλάβη."
    ],
    "source": "https://el.wikipedia.org/wiki/RAID",
    "locale": "el-GR",
    "tags": ["raid", "storage", "hardware", "redundancy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_045",
    "text": "Τι ιδιαίτερο χαρακτηρίζει την ειδική μνήμη ECC RAM που χρησιμοποιείται υποχρεωτικά σε διακομιστές και κρίσιμα υπολογιστικά κέντρα;",
    "answers": ["Λειτουργεί χωρίς καθόλου παροχή ρεύματος", "Διαθέτει ενσωματωμένο επεξεργαστή γραφικών", "Εντοπίζει και διορθώνει αυτόματα σφάλματα αλλοίωσης bit", "Είναι υγρόψυκτη"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μνήμη ECC (Error-Correcting Code) περιέχει επιπλέον bits ισοτιμίας που επιτρέπουν τον αυτόματο εντοπισμό και διόρθωση σφαλμάτων μονού bit που προκαλούνται από ηλεκτρομαγνητικές παρεμβολές ή κοσμική ακτινοβολία.",
    "funFacts": [
      "Αποτρέπει καταστροφικά κρασαρίσματα του συστήματος και διαφθορά δεδομένων σε χρηματοπιστωτικά συστήματα και ιατρικούς διακομιστές.",
      "Τα απλά καταναλωτικά PC συνήθως δεν υποστηρίζουν μνήμη ECC για λόγους κόστους."
    ],
    "source": "https://el.wikipedia.org/wiki/ECC_RAM",
    "locale": "el-GR",
    "tags": ["ecc-ram", "memory", "servers", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_046",
    "text": "Ποια βρετανική εταιρεία σχεδιάζει την εξαιρετικά αποδοτική αρχιτεκτονική επεξεργαστών RISC που τροφοδοτεί σχεδόν όλα τα σύγχρονα smartphones;",
    "answers": ["Intel", "Qualcomm", "Nvidia", "Arm"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η εταιρεία Arm Holdings σχεδιάζει τις αρχιτεκτονικές συνόλου εντολών και πυρήνων και παραχωρεί άδειες χρήσης σε κατασκευαστές όπως Apple, Qualcomm και Samsung.",
    "funFacts": [
      "Η εταιρεία ξεκίνησε αρχικά το 1990 ως κοινοπραξία της Acorn Computers, της Apple και της VLSI Technology.",
      "Τα αρχικά ARM σήμαιναν αρχικά 'Acorn RISC Machine' πριν μετονομαστούν σε 'Advanced RISC Machines'."
    ],
    "source": "https://el.wikipedia.org/wiki/Arm_(%CE%B5%CF%84%CE%B1%CE%B9%CF%81%CE%B5%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["arm", "processors", "hardware", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_047",
    "text": "Τι σημαίνει το ακρωνύμιο «RISC» στον σχεδιασμό της αρχιτεκτονικής συνόλου εντολών ενός επεξεργαστή;",
    "answers": ["Reduced Instruction Set Computer", "Random Input System Controller", "Rapid Integrated Silicon Circuit", "Remote Internal Server Connection"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η αρχιτεκτονική RISC (Υπολογιστής Μειωμένου Συνόλου Εντολών) χρησιμοποιεί απλούστερες εντολές που εκτελούνται σε έναν μόνο κύκλο ρολογιού, επιτυγχάνοντας υψηλή ενεργειακή αποδοτικότητα.",
    "funFacts": [
      "Αντιπαραβάλλεται στην αρχιτεκτονική CISC (Complex Instruction Set Computer), της οποίας κύριος εκπρόσωπος είναι οι επεξεργαστές x86 της Intel και AMD.",
      "Η έννοια του RISC αναπτύχθηκε στα πανεπιστήμια Berkeley και Stanford στις αρχές της δεκαετίας του 1980 από τους Ντέιβιντ Πάτερσον και Τζον Χένεσι."
    ],
    "source": "https://el.wikipedia.org/wiki/RISC",
    "locale": "el-GR",
    "tags": ["risc", "processors", "architecture", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_048",
    "text": "Ποιος διεθνής επιστημονικός οργανισμός απονέμει ετησίως το περίφημο Turing Award, το οποίο θεωρείται το αντίστοιχο του Βραβείου Νόμπελ στην πληροφορική;",
    "answers": ["IEEE", "ACM (Association for Computing Machinery)", "ISO", "W3C"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η ACM απονέμει το A.M. Turing Award από το 1966 για εξαιρετικές συνεισφορές διαρκούς τεχνικής σημασίας στην επιστήμη των υπολογιστών.",
    "funFacts": [
      "Το βραβείο συνοδεύεται από χρηματικό έπαθλο 1 εκατομμυρίου δολαρίων, το οποίο χρηματοδοτείται εξ ολοκλήρου από την Google.",
      "Ανάμεσα στους βραβευθέντες περιλαμβάνονται θρύλοι όπως οι Ντάικστρα, Κνουθ, Ρίτσι, Τόμσον, Μπερνερς-Λι και οι πρωτοπόροι του Deep Learning Χίντον, Λεκούν και Μπέντζιο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CF%81%CE%B1%CE%B2%CE%B5%CE%AF%CE%BF_%CE%A4%CE%B9%CE%BF%CF%81%CE%B9%CE%BD%CE%B3%CE%BA",
    "locale": "el-GR",
    "tags": ["turing-award", "acm", "computer-science", "awards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_049",
    "text": "Ποιος μηχανικός υπολογιστών έστειλε το πρώτο ηλεκτρονικό μήνυμα δικτύου (email) στο ARPANET το 1971, καθιερώνοντας το σύμβολο @ στις διευθύνσεις;",
    "answers": ["Βιντ Σερφ", "Τιμ Μπέρνερς-Λι", "Ρέι Τόμλινσον", "Μπομπ Μέτκαλφ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ρέι Τόμλινσον (Ray Tomlinson) στην εταιρεία BBN Technologies ανέπτυξε το πρόγραμμα SNDMSG επιτρέποντας την αποστολή μηνυμάτων μεταξύ διαφορετικών υπολογιστών.",
    "funFacts": [
      "Επέλεξε το σύμβολο @ επειδή ήταν ένα σπάνια χρησιμοποιούμενο πλήκτρο που δήλωνε τη θέση (at) του χρήστη στον διακομιστή.",
      "Το περιεχόμενο του πρώτου δοκιμαστικού μηνύματος ήταν ασήμαντο και πιθανότατα έγραφε 'QWERTYUIOP'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AD%CE%B9_%CE%A4%CF%8C%CE%BC%CE%BB%CE%B9%CE%BD%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["email", "tomlinson", "arpanet", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_050",
    "text": "Ποιος Πολωνοαμερικανός μηχανικός επινόησε ανεξάρτητα την έννοια της «μεταγωγής πακέτων» (packet switching) στα εργαστήρια RAND τη δεκαετία του 1960;",
    "answers": ["Λέοναρντ Κλάινροκ", "Ντόναλντ Ντέιβις", "Τζον φον Νόιμαν", "Πολ Μπάραν"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Πολ Μπάραν (Paul Baran) σχεδίασε ένα κατανεμημένο δίκτυο επικοινωνιών που μπορούσε να επιβιώσει από πυρηνική επίθεση σπάζοντας τα μηνύματα σε ανεξάρτητα πακέτα.",
    "funFacts": [
      "Ταυτόχρονα και ανεξάρτητα στη Βρετανία, ο Ντόναλντ Ντέιβις επινόησε την ίδια τεχνολογία και επινόησε τον όρο 'packet' (πακέτο).",
      "Η παραδοσιακή τηλεφωνική εταιρεία AT&T απέρριψε αρχικά τις ιδέες του Μπάραν ισχυριζόμενη ότι ένα τέτοιο ψηφιακό δίκτυο δεν θα μπορούσε ποτέ να λειτουργήσει."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB_%CE%9C%CF%80%CE%AC%CF%81%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["paul-baran", "packet-switching", "networking", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_051",
    "text": "Ποιος μηχανικός επινόησε το πρότυπο τοπικής δικτύωσης Ethernet στο ερευνητικό κέντρο Xerox PARC το 1973 και ίδρυσε αργότερα την εταιρεία 3Com;",
    "answers": ["Ρόμπερτ Μέτκαλφ", "Ντάγκλας Ένγκελμπαρτ", "Τσακ Θάκερ", "Άλαν Κέι"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ρόμπερτ Μέτκαλφ (Robert Metcalfe) σχεδίασε το Ethernet αντλώντας έμπνευση από το ασύρματο δίκτυο ALOHAnet του Πανεπιστημίου της Χαβάης.",
    "funFacts": [
      "Διατύπωσε τον περίφημο 'Νόμο του Μέτκαλφ', σύμφωνα με τον οποίο η αξία ενός τηλεπικοινωνιακού δικτύου είναι ανάλογη του τετραγώνου του αριθμού των συνδεδεμένων χρηστών (n^2).",
      "Τιμήθηκε με το Βραβείο Turing το 2022 για την εφεύρεση και τυποποίηση του Ethernet."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%8C%CE%BC%CF%80%CE%B5%CF%81%CF%84_%CE%9C%CE%AD%CF%84%CE%BA%CE%B1%CE%BB%CF%86",
    "locale": "el-GR",
    "tags": ["metcalfe", "ethernet", "xerox-parc", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_052",
    "text": "Σε ποιο ιστορικό έτος πραγματοποιήθηκε η θρυλική παρουσίαση «The Mother of All Demos» από τον Ντάγκλας Ένγκελμπαρτ, παρουσιάζοντας το ποντίκι και τα γραφικά παράθυρα;",
    "answers": ["1962", "1968", "1975", "1984"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Στις 9 Δεκεμβρίου 1968 στο Σαν Φρανσίσκο, ο Ντάγκλας Ένγκελμπαρτ παρουσίασε σε μια 90λεπτη ζωντανή επίδειξη το ποντίκι, την επεξεργασία κειμένου, το υπερκείμενο και τις τηλεδιασκέψεις.",
    "funFacts": [
      "Η επίδειξη του συστήματος NLS (oN-Line System) θεωρείται ευρέως η πιο επιδραστική ζωντανή παρουσίαση στην ιστορία της πληροφορικής.",
      "Το σύστημα χρησιμοποιούσε ειδικό πληκτρολόγιο συγχορδιών (keyset) με 5 πλήκτρα για ταχύτατη εισαγωγή εντολών με το ένα χέρι ενώ το άλλο χειριζόταν το ποντίκι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%AC%CE%B3%CE%BA%CE%BB%CE%B1%CF%82_%CE%88%CE%BD%CE%B3%CE%BA%CE%B5%CE%BB%CE%BC%CF%80%CE%B1%CF%81%CF%84",
    "locale": "el-GR",
    "tags": ["mother-of-all-demos", "engelbart", "history-tech", "mouse"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_053",
    "text": "Ποιος Αμερικανός επιστήμονας υπολογιστών δημιούργησε το ιστορικό λειτουργικό σύστημα CP/M για μικροϋπολογιστές βασισμένους στον επεξεργαστή Intel 8080 το 1974;",
    "answers": ["Μπιλ Γκέιτς", "Στιβ Τζομπς", "Γκάρι Κίλνταλ", "Τιμ Πάτερσον"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Γκάρι Κίλνταλ (Gary Kildall) ίδρυσε την Digital Research Inc. και δημιούργησε το CP/M, το κυρίαρχο λειτουργικό σύστημα για μικροϋπολογιστές της δεκαετίας του 1970.",
    "funFacts": [
      "Επινόησε την έννοια του BIOS (Basic Input/Output System) για να διαχωρίσει το υλικό από το λειτουργικό σύστημα.",
      "Η άρνησή του να υπογράψει ένα αυστηρό συμφωνητικό εμπιστευτικότητας με την IBM το 1980 οδήγησε την IBM να στραφεί στη Microsoft για το λειτουργικό του IBM PC."
    ],
    "source": "https://el.wikipedia.org/wiki/CP/M",
    "locale": "el-GR",
    "tags": ["cpm", "kildall", "operating-systems", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_054",
    "text": "Ποιος προγραμματιστής έγραψε το λειτουργικό σύστημα QDOS (Quick and Dirty Operating System) το οποίο αγόρασε η Microsoft το 1981 για να το μετονομάσει σε MS-DOS;",
    "answers": ["Πολ Άλεν", "Στιβ Μπάλμερ", "Γκάρι Κίλνταλ", "Τιμ Πάτερσον"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τιμ Πάτερσον (Tim Paterson) στην εταιρεία Seattle Computer Products έγραψε το QDOS (γνωστό και ως 86-DOS) ως κλώνο του CP/M για τον επεξεργαστή Intel 8086.",
    "funFacts": [
      "Η Microsoft αγόρασε όλα τα δικαιώματα του συστήματος από την εταιρεία του Πάτερσον έναντι μόλις 50.000 δολαρίων τον Ιούλιο του 1981.",
      "Στη συνέχεια, η Microsoft παραχώρησε μη αποκλειστική άδεια χρήσης στην IBM κρατώντας τα δικαιώματα πώλησης σε άλλους κατασκευαστές, δημιουργώντας την αυτοκρατορία της."
    ],
    "source": "https://el.wikipedia.org/wiki/MS-DOS",
    "locale": "el-GR",
    "tags": ["ms-dos", "paterson", "microsoft", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_055",
    "text": "Ποιος επικεφαλής ερευνητής της IBM ανέπτυξε τη Fortran, την πρώτη ευρέως διαδεδομένη γλώσσα προγραμματισμού υψηλού επιπέδου, τη δεκαετία του 1950;",
    "answers": ["Τζον Μπάκους", "Τζον Μακάρθι", "Άλαν Πέρλις", "Μορίς Γουίλκς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζον Μπάκους (John Backus) ηγήθηκε της ομάδας της IBM που δημιούργησε τη Fortran (Formula Translation) για επιστημονικούς και μηχανικούς υπολογισμούς.",
    "funFacts": [
      "Επινόησε επίσης τη μορφή Backus-Naur (BNF), την τυποποιημένη μέθοδο περιγραφής της γραμματικής των γλωσσών προγραμματισμού.",
      "Βραβεύτηκε με το Βραβείο Turing το 1977 για τη θεμελίωση πρακτικών συστημάτων προγραμματισμού υψηλού επιπέδου."
    ],
    "source": "https://el.wikipedia.org/wiki/Fortran",
    "locale": "el-GR",
    "tags": ["fortran", "backus", "programming", "ibm"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_056",
    "text": "Ποια ιστορική γλώσσα προγραμματισμού επινόησε ο Τζον Μακάρθι το 1958, η οποία καθιέρωσε τις συνδεδεμένες λίστες και έγινε η βάση της κλασικής τεχνητής νοημοσύνης;",
    "answers": ["Prolog", "Lisp", "COBOL", "ALGOL"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Lisp (LISt Processor) εισήγαγε πρωτοποριακές έννοιες όπως η αυτόματη διαχείριση μνήμης (garbage collection), οι ανώνυμες συναρτήσεις (lambdas) και οι αναδρομές.",
    "funFacts": [
      "Είναι η δεύτερη παλαιότερη γλώσσα προγραμματισμού υψηλού επιπέδου που εξακολουθεί να χρησιμοποιείται ευρέως σήμερα, μετά τη Fortran.",
      "Ο ίδιος ο Τζον Μακάρθι ήταν ο άνθρωπος που επινόησε και καθιέρωσε τον όρο 'Τεχνητή Νοημοσύνη' το 1956."
    ],
    "source": "https://el.wikipedia.org/wiki/LISP",
    "locale": "el-GR",
    "tags": ["lisp", "john-mccarthy", "ai", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_057",
    "text": "Ποια πρωτοποριακή γλώσσα προγραμματισμού που αναπτύχθηκε στα εργαστήρια Xerox PARC καθιέρωσε πλήρως τον αμιγώς αντικειμενοστραφή προγραμματισμό (OOP);",
    "answers": ["Simula", "Eiffel", "Smalltalk", "APL"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Smalltalk αναπτύχθηκε κυρίως από τον Άλαν Κέι, τον Νταν Ίνγκαλς και την Αντέλ Γκόλντμπεργκ, όπου κυριολεκτικά 'τα πάντα είναι αντικείμενο'.",
    "funFacts": [
      "Εισήγαγε για πρώτη φορά το αρχιτεκτονικό πρότυπο MVC (Model-View-Controller), το οποίο χρησιμοποιείται μέχρι σήμερα σε όλο τον παγκόσμιο ιστό.",
      "Επηρέασε βαθύτατα τη σχεδίαση μεταγενέστερων γλωσσών όπως η Objective-C, η Java, η Python και η Ruby."
    ],
    "source": "https://el.wikipedia.org/wiki/Smalltalk",
    "locale": "el-GR",
    "tags": ["smalltalk", "oop", "xerox-parc", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_058",
    "text": "Ποιος Αμερικανός γλωσσολόγος και προγραμματιστής δημιούργησε τη γλώσσα προγραμματισμού Perl το 1987 ως ισχυρό εργαλείο επεξεργασίας κειμένου;",
    "answers": ["Γκίντο βαν Ρόσουμ", "Γιούκιχιρο Ματσουμότο", "Ράσμους Λέρντορφ", "Λάρι Γουόλ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Λάρι Γουόλ (Larry Wall) σχεδίασε την Perl συνδυάζοντας χαρακτηριστικά από C, sed, awk και κέλυφος sh, η οποία έγινε η ραχοκοκαλιά του πρώιμου διαδικτύου (CGI scripts).",
    "funFacts": [
      "Το διάσημο μότο της κοινότητας της Perl είναι: 'There's more than one way to do it' (TMTOWTDI - Υπάρχουν περισσότεροι από ένας τρόποι να το κάνεις).",
      "Εκτός από την Perl, ο Γουόλ έγραψε επίσης το διάσημο εργαλείο 'patch' των συστημάτων Unix."
    ],
    "source": "https://el.wikipedia.org/wiki/Perl",
    "locale": "el-GR",
    "tags": ["perl", "larry-wall", "programming", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_059",
    "text": "Ποιος Σκωτσέζος φυσικός και μαθηματικός διατύπωσε τις θεμελιώδεις εξισώσεις του κλασικού ηλεκτρομαγνητισμού προβλέποντας θεωρητικά τα ραδιοκύματα το 1865;",
    "answers": ["Τζέιμς Κλερκ Μάξγουελ", "Μάικλ Φαραντέι", "Αντρέ-Μαρί Αμπέρ", "Χάινριχ Χερτς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζέιμς Κλερκ Μάξγουελ (James Clerk Maxwell) ένωσε τον ηλεκτρισμό, τον μαγνητισμό και το φως σε ένα ενιαίο θεωρητικό πλαίσιο μέσω των περίφημων εξισώσεων Μάξγουελ.",
    "funFacts": [
      "Απέδειξε θεωρητικά ότι τα ηλεκτρομαγνητικά κύματα ταξιδεύουν στο κενό με την ταχύτητα του φωτός.",
      "Δημιούργησε επίσης την πρώτη έγχρωμη φωτογραφία στην ιστορία το 1861, χρησιμοποιώντας τρία φίλτρα (κόκκινο, πράσινο, μπλε)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CE%B9%CE%BC%CF%82_%CE%9A%CE%BB%CE%B5%CF%81%CE%BA_%CE%9C%CE%AC%CE%BE%CE%BF%CF%85%CE%B5%CE%BB",
    "locale": "el-GR",
    "tags": ["maxwell", "physics", "electromagnetism", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_060",
    "text": "Ποιος Γερμανός φυσικός απέδειξε πειραματικά για πρώτη φορά την πραγματική ύπαρξη των ηλεκτρομαγνητικών ραδιοκυμάτων το 1887;",
    "answers": ["Βίλχελμ Ρέντγκεν", "Χάινριχ Χερτς", "Μαξ Πλανκ", "Γκούσταβ Κίρχοφ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Χάινριχ Χερτς (Heinrich Hertz) κατασκεύασε τον πρώτο πομπό και δέκτη ραδιοκυμάτων, επιβεβαιώνοντας πανηγυρικά τις θεωρητικές προβλέψεις του Μάξγουελ.",
    "funFacts": [
      "Όταν ρωτήθηκε για τη χρησιμότητα της ανακάλυψής του, ο Χερτς απάντησε: 'Δεν έχει καμία απολύτως χρησιμότητα... είναι απλώς ένα πείραμα που αποδεικνύει ότι ο καθηγητής Μάξγουελ είχε δίκιο'.",
      "Προς τιμήν του, η μονάδα μέτρησης της συχνότητας (κύκλοι ανά δευτερόλεπτο) ονομάστηκε διεθνώς Hertz (Hz) το 1930."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CE%B9%CE%BD%CF%81%CE%B9%CF%87_%CE%A7%CE%B5%CF%81%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["hertz", "physics", "radio", "electromagnetism"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'medium', 3, questions)

# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "technology_easy_161",
    "text": "Ποιος οραματιστής επιστήμονας υπολογιστών συνέλαβε τη δεκαετία του 1960 την ιδέα του «Dynabook», που θεωρείται ο πρόδρομος του σύγχρονου tablet και laptop;",
    "answers": ["Άλαν Κέι", "Μπιλ Γκέιτς", "Στιβ Τζομπς", "Τιμ Μπέρνερς-Λι"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Άλαν Κέι (Alan Kay) περιέγραψε το 1968 το Dynabook ως έναν φορητό, διαδραστικό προσωπικό υπολογιστή με επίπεδη οθόνη σχεδιασμένο κυρίως για εκπαιδευτική χρήση.",
    "funFacts": [
      "Είναι επίσης γνωστός για τη διάσημη ρήση του: 'Ο καλύτερος τρόπος να προβλέψεις το μέλλον είναι να το εφεύρεις'.",
      "Συνέβαλε καθοριστικά στην ανάπτυξη του αντικειμενοστραφούς προγραμματισμού και του γραφικού περιβάλλοντος εργασίας στο εργαστήριο Xerox PARC."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%B1%CE%BD_%CE%9A%CE%AD%CE%B9",
    "locale": "el-GR",
    "tags": ["alan-kay", "dynabook", "pioneers", "tablets"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_162",
    "text": "Ποια πρωτοπόρος Αμερικανίδα μαθηματικός και ναύαρχος ανέπτυξε τον πρώτο μεταγλωττιστή (compiler) στην ιστορία των υπολογιστών;",
    "answers": ["Άντα Λάβλεϊς", "Γκρέις Χόπερ", "Κάθριν Τζόνσον", "Μάργκαρετ Χάμιλτον"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Γκρέις Χόπερ (Grace Hopper) δημιούργησε τον μεταγλωττιστή A-0 το 1952, επιτρέποντας τη συγγραφή προγραμμάτων με αγγλικές λέξεις αντί για γλώσσα μηχανής.",
    "funFacts": [
      "Η πρωτοποριακή εργασία της οδήγησε άμεσα στη δημιουργία της γλώσσας COBOL, μιας από τις πρώτες γλώσσες υψηλού επιπέδου.",
      "Ένα αντιτορπιλικό πλοίο κατευθυνόμενων βλημάτων του Πολεμικού Ναυτικού των ΗΠΑ ονομάστηκε USS Hopper προς τιμήν της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CF%81%CE%AD%CE%B9%CF%82_%CE%A7%CF%8C%CF%80%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["grace-hopper", "compiler", "pioneers", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_163",
    "text": "Ποιο διάσημο κατανεμημένο σύστημα ελέγχου εκδόσεων πηγαίου κώδικα δημιούργησε ο Λίνους Τόρβαλντς το 2005 για τη διαχείριση της ανάπτυξης του Linux;",
    "answers": ["SVN", "Mercurial", "Git", "CVS"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Λίνους Τόρβαλντς ανέπτυξε το Git μέσα σε λίγες εβδομάδες για να επιτρέψει σε χιλιάδες προγραμματιστές σε όλο τον κόσμο να συνεργάζονται ταχύτατα στον πυρήνα του Linux.",
    "funFacts": [
      "Σήμερα το Git είναι το κυρίαρχο εργαλείο διαχείρισης κώδικα παγκοσμίως, χρησιμοποιούμενο από περισσότερο από το 90% των προγραμματιστών.",
      "Η λέξη 'git' είναι βρετανική αργκό που σημαίνει 'δύστροπος' ή 'ενοχλητικός άνθρωπος', όνομα που ο Τόρβαλντς επέλεξε αυτοσαρκαζόμενος."
    ],
    "source": "https://el.wikipedia.org/wiki/Git",
    "locale": "el-GR",
    "tags": ["git", "linus-torvalds", "open-source", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_164",
    "text": "Ποια είναι η μεγαλύτερη διαδικτυακή πλατφόρμα φιλοξενίας έργων κώδικα και συνεργασίας ανοιχτού λογισμικού, την οποία εξαγόρασε η Microsoft το 2018;",
    "answers": ["Bitbucket", "SourceForge", "GitLab", "GitHub"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το GitHub φιλοξενεί αποθετήρια κώδικα βασισμένα στο Git και εξαγοράστηκε από τη Microsoft το 2018 έναντι 7,5 δισεκατομμυρίων δολαρίων.",
    "funFacts": [
      "Η διάσημη επίσημη μασκότ του GitHub είναι η Octocat, ένα πλάσμα με κεφάλι γάτας και πλοκάμια χταποδιού.",
      "Το 2020 το GitHub αποθήκευσε αντίγραφα των σημαντικότερων έργων ανοιχτού κώδικα σε ειδικό θησαυροφυλάκιο μέσα σε ένα παγωμένο ορυχείο στο Σβάλμπαρντ της Αρκτικής για 1.000 χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/GitHub",
    "locale": "el-GR",
    "tags": ["github", "git", "microsoft", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_165",
    "text": "Ποιος κορυφαίος ιστότοπος ερωταπαντήσεων αποτελεί την πιο διάσημη και απαραίτητη καθημερινή διαδικτυακή κοινότητα για προγραμματιστές υπολογιστών;",
    "answers": ["Stack Overflow", "Quora", "Yahoo! Answers", "Reddit"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Stack Overflow ιδρύθηκε το 2008 από τους Τζεφ Άτγουντ και Τζόελ Σπόλσκι και παρέχει λύσεις σε τεχνικά προβλήματα προγραμματισμού μέσω ψηφοφορίας της κοινότητας.",
    "funFacts": [
      "Το όνομα της ιστοσελίδας επιλέχθηκε με ψηφοφορία των αναγνωστών και προέρχεται από το διάσημο σφάλμα υπερχείλισης στοίβας μνήμης (stack overflow).",
      "Περιέχει εκατομμύρια απαντήσεις που καλύπτουν σχεδόν κάθε υπάρχουσα γλώσσα προγραμματισμού και τεχνολογικό πλαίσιο."
    ],
    "source": "https://el.wikipedia.org/wiki/Stack_Overflow",
    "locale": "el-GR",
    "tags": ["stack-overflow", "programming", "developers", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_166",
    "text": "Ποια γλώσσα υπολογιστή χρησιμοποιείται στον παγκόσμιο ιστό για να καθορίσει την οπτική εμφάνιση, τα χρώματα, τις γραμματοσειρές και τη διάταξη (styling) των σελίδων HTML;",
    "answers": ["JavaScript", "CSS (Cascading Style Sheets)", "PHP", "Python"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το CSS (Διαδοχικά Φύλλα Στυλ) διαχωρίζει την οπτική παρουσίαση μιας ιστοσελίδας από τη δομή του περιεχομένου της (HTML).",
    "funFacts": [
      "Προτάθηκε για πρώτη φορά το 1994 από τον Χάακον Βίελιουμ Λι ενώ εργαζόταν με τον Τιμ Μπέρνερς-Λι στο CERN.",
      "Η σύγχρονη έκδοση CSS3 υποστηρίζει ενσωματωμένα κινούμενα σχέδια (animations), διαβαθμίσεις χρωμάτων (gradients) και προσαρμοστική σχεδίαση (Responsive Web Design)."
    ],
    "source": "https://el.wikipedia.org/wiki/CSS",
    "locale": "el-GR",
    "tags": ["css", "web", "design", "html"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_167",
    "text": "Ποια εξαιρετικά δημοφιλής γλώσσα προγραμματισμού δημιουργήθηκε σε μόλις 10 ημέρες το 1995 από τον Μπρένταν Άιχ για τον περιηγητή Netscape;",
    "answers": ["Java", "TypeScript", "JavaScript", "C#"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η JavaScript αναπτύχθηκε για να προσθέσει δυναμική διάδραση στις ιστοσελίδες και σήμερα εκτελείται σχεδόν σε κάθε σύγχρονο πρόγραμμα περιήγησης.",
    "funFacts": [
      "Αρχικά ονομαζόταν 'Mocha' και αργότερα 'LiveScript', πριν μετονομαστεί σε JavaScript για λόγους μάρκετινγκ λόγω της τότε τεράστιας απήχησης της Java.",
      "Παρά την ομοιότητα στο όνομα, η JavaScript και η Java είναι εντελώς διαφορετικές γλώσσες με διαφορετική φιλοσοφία και σχεδιασμό."
    ],
    "source": "https://el.wikipedia.org/wiki/JavaScript",
    "locale": "el-GR",
    "tags": ["javascript", "web", "programming", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_168",
    "text": "Ποια τυποποιημένη γλώσσα χρησιμοποιείται παγκοσμίως για τη διαχείριση, αποθήκευση και ανάκτηση δεδομένων σε σχεσιακές βάσεις δεδομένων;",
    "answers": ["HTML", "XML", "JSON", "SQL"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η SQL (Structured Query Language) είναι η καθιερωμένη γλώσσα υποβολής ερωτημάτων για συστήματα σχεσιακών βάσεων δεδομένων όπως MySQL, PostgreSQL και Oracle.",
    "funFacts": [
      "Αναπτύχθηκε αρχικά στην IBM τη δεκαετία του 1970 από τους Ντόναλντ Τσάμπερλιν και Ρέιμοντ Μπόις.",
      "Βασικές εντολές της όπως SELECT, INSERT, UPDATE και DELETE χρησιμοποιούνται καθημερινά από εκατομμύρια διακομιστές σε όλο τον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/SQL",
    "locale": "el-GR",
    "tags": ["sql", "databases", "programming", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_169",
    "text": "Πόσα bits μήκος έχει μια κλασική διεύθυνση του πρωτοκόλλου διαδικτύου IPv4 (όπως για παράδειγμα η 192.168.1.1);",
    "answers": ["32 bits", "64 bits", "128 bits", "16 bits"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Μια διεύθυνση IPv4 αποτελείται από 32 bits χωρισμένα σε 4 οκτάδες (bytes), που γράφονται παραδοσιακά σε δεκαδική μορφή χωρισμένα με τελείες.",
    "funFacts": [
      "Το μήκος των 32 bits επιτρέπει συνολικά 2^32 (περίπου 4,29 δισεκατομμύρια) πιθανές μοναδικές διευθύνσεις.",
      "Λόγω της εξάντλησης των διευθύνσεων IPv4, αναπτύχθηκε το νεότερο πρωτόκολλο IPv6 με μήκος 128 bits."
    ],
    "source": "https://el.wikipedia.org/wiki/IPv4",
    "locale": "el-GR",
    "tags": ["ipv4", "networking", "internet", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_170",
    "text": "Πόσα Megabits (Mb) απαιτούνται για να σχηματιστεί ένα πλήρες Megabyte (MB) δεδομένων;",
    "answers": ["2 Megabits", "8 Megabits", "10 Megabits", "1.000 Megabits"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Επειδή 1 Byte αποτελείται πάντα από 8 bits, 1 Megabyte (MB) ισούται ακριβώς με 8 Megabits (Mb).",
    "funFacts": [
      "Οι πάροχοι διαδικτύου διαφημίζουν τις ταχύτητες σύνδεσης σε Megabits ανά δευτερόλεπτο (Mbps) και όχι σε Megabytes, κάνοντας το νούμερο να φαίνεται 8 φορές μεγαλύτερο.",
      "Μια οικιακή γραμμή με ταχύτητα 100 Mbps κατεβάζει αρχεία με μέγιστο πραγματικό ρυθμό περίπου 12,5 MB ανά δευτερόλεπτο."
    ],
    "source": "https://el.wikipedia.org/wiki/Megabyte",
    "locale": "el-GR",
    "tags": ["megabyte", "megabit", "networking", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_171",
    "text": "Ποια πρωτοπόρος εταιρεία ημιαγωγών κατασκεύασε τον πρώτο εμπορικό μικροεπεξεργαστή μονού τσιπ στον κόσμο (τον Intel 4004) το 1971;",
    "answers": ["AMD", "IBM", "Intel", "Motorola"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Intel κυκλοφόρησε τον επεξεργαστή 4004 τον Νοέμβριο του 1971, ενσωματώνοντας όλα τα κυκλώματα επεξεργασίας σε ένα ενιαίο τσιπ πυριτίου.",
    "funFacts": [
      "Ο επεξεργαστής σχεδιάστηκε αρχικά για μια ιαπωνική επιτραπέζια αριθμομηχανή (τη Busicom 141-PF).",
      "Περιείχε μόλις 2.300 τρανζίστορ, ενώ οι σύγχρονοι επεξεργαστές ξεπερνούν τα 10 δισεκατομμύρια τρανζίστορ."
    ],
    "source": "https://el.wikipedia.org/wiki/Intel_4004",
    "locale": "el-GR",
    "tags": ["intel", "microprocessors", "hardware", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_172",
    "text": "Ποιος συνιδρυτής της Intel διατύπωσε τον διάσημο εμπειρικό κανόνα ότι ο αριθμός των τρανζίστορ σε ένα μικροτσίπ διπλασιάζεται περίπου κάθε δύο χρόνια;",
    "answers": ["Ρόμπερτ Νόις", "Άντι Γκρόουβ", "Τιμ Κουκ", "Γκόρντον Μουρ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Γκόρντον Μουρ (Gordon Moore) διατύπωσε την παρατήρηση αυτή το 1965, η οποία έμεινε στην ιστορία ως ο «Νόμος του Μουρ» καθοδηγώντας τη βιομηχανία ημιαγωγών για δεκαετίες.",
    "funFacts": [
      "Αρχικά ο Μουρ είχε προβλέψει ετήσιο διπλασιασμό, αλλά το 1975 αναθεώρησε την πρόβλεψη σε διπλασιασμό ανά περίπου δύο έτη.",
      "Ο νόμος του Μουρ δεν είναι φυσικός νόμος, αλλά ένας τεχνολογικός στόχος και πρόβλεψη που εκπληρώθηκε χάρη στη διαρκή σμίκρυνση των ηλεκτρονικών κυκλωμάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%8C%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%9C%CE%BF%CF%85%CF%81",
    "locale": "el-GR",
    "tags": ["moores-law", "intel", "semiconductors", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_173",
    "text": "Ποιο μικροσκοπικό ηλεκτρονικό εξάρτημα ημιαγωγών που εφευρέθηκε στα εργαστήρια Bell το 1947 αντικατέστησε τις ογκώδεις και ευπαθείς λυχνίες κενού;",
    "answers": ["Τρανζίστορ (Transistor)", "Πυκνωτής", "Μετασχηματιστής", "Ηλεκτρονόμος (Relay)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το τρανζίστορ λειτουργεί ως ενισχυτής ή ηλεκτρονικός διακόπτης και θεωρείται από τις σημαντικότερες τεχνολογικές εφευρέσεις του 20ού αιώνα.",
    "funFacts": [
      "Εφευρέθηκε από τους φυσικούς Τζον Μπαρντίν, Γουόλτερ Μπράτεϊν και Γουίλιαμ Σόκλεϊ, οι οποίοι μοιράστηκαν το Νόμπελ Φυσικής το 1956.",
      "Χωρίς το τρανζίστορ θα ήταν αδύνατη η δημιουργία υπολογιστών τσέπης, έξυπνων κινητών τηλεφώνων και του σύγχρονου διαδικτύου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%B1%CE%BD%CE%B6%CE%AF%CF%83%CF%84%CE%BF%CF%81",
    "locale": "el-GR",
    "tags": ["transistor", "electronics", "inventions", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_174",
    "text": "Ποιο χημικό στοιχείο (ημιαγωγός) αποτελεί το βασικό θεμέλιο και υλικό κατασκευής για σχεδόν όλα τα σύγχρονα μικροτσίπ και επεξεργαστές;",
    "answers": ["Χαλκός", "Πυρίτιο (Silicon)", "Σίδηρος", "Ασήμι"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πυρίτιο (χημικό σύμβολο Si) είναι άφθονο στη φύση (βασικό συστατικό της άμμου) και διαθέτει ιδανικές ημιαγωγικές ιδιότητες για ολοκληρωμένα κυκλώματα.",
    "funFacts": [
      "Είναι το δεύτερο πιο άφθονο στοιχείο στον φλοιό της Γης κατά βάρος (περίπου 28%), μετά το οξυγόνο.",
      "Για την κατασκευή τσιπ απαιτείται υπερκάθαρο πυρίτιο ηλεκτρονικής ποιότητας με καθαρότητα 99,9999999%."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%85%CF%81%CE%AF%CF%84%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["silicon", "semiconductors", "chemistry", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_175",
    "text": "Πώς ονομάζεται ο υπερσύγχρονος, εξαιρετικά φιλτραρισμένος χώρος εργοστασίου όπου κατασκευάζονται τα μικροτσίπ ώστε να μην καταστραφούν από κόκκους σκόνης;",
    "answers": ["Θάλαμος αποσυμπίεσης", "Σκοτεινός θάλαμος", "Καθαρό δωμάτιο (Cleanroom)", "Υψικάμινος"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Σε ένα καθαρό δωμάτιο (cleanroom), ο αέρας φιλτράρεται διαρκώς ώστε να περιέχει ελάχιστα έως μηδενικά αιωρούμενα μικροσωματίδια σκόνης.",
    "funFacts": [
      "Ένα απλό σωματίδιο σκόνης είναι εκατοντάδες φορές μεγαλύτερο από τα κυκλώματα ενός σύγχρονου επεξεργαστή και μπορεί να προκαλέσει βραχυκύκλωμα.",
      "Οι εργαζόμενοι φορούν ειδικές ολόσωμες προστατευτικές στολές γνωστές ως 'στολές λαγού' (bunny suits) για να μην αποβάλλουν τρίχες ή νεκρά κύτταρα δέρματος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%B8%CE%B1%CF%81%CF%8C%CF%82_%CF%87%CF%8E%CF%81%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["cleanroom", "manufacturing", "semiconductors", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_176",
    "text": "Πώς ονομάζεται η μικρή φορητή συσκευή αποθήκευσης που συνδέεται άμεσα σε θύρα υπολογιστή και αποκαλείται στην καθομιλουμένη «στικάκι»;",
    "answers": ["Εξωτερικό CD-ROM", "Κάρτα γραφικών", "Δισκέτα", "USB flash drive"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το USB flash drive είναι μια συμπαγής μονάδα μόνιμης αποθήκευσης δεδομένων που χρησιμοποιεί μνήμη flash και ενσωματώνει διεπαφή USB.",
    "funFacts": [
      "Πρωτοεμφανίστηκε εμπορικά στα τέλη του 2000 με χωρητικότητα μόλις 8 Megabytes.",
      "Αντικατέστησε οριστικά τις δισκέτες και τα επανεγγράψιμα CD λόγω της ταχύτητας, της αντοχής και της ευκολίας χρήσης Plug-and-Play."
    ],
    "source": "https://el.wikipedia.org/wiki/USB_flash_drive",
    "locale": "el-GR",
    "tags": ["usb-flash-drive", "storage", "hardware", "gadgets"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_177",
    "text": "Ποια μικροσκοπική αφαιρούμενη κάρτα μνήμης flash χρησιμοποιείται ευρύτατα σε smartphone, action κάμερες και κονσόλες για την επέκταση του αποθηκευτικού χώρου;",
    "answers": ["Κάρτα MicroSD", "CompactFlash", "Memory Stick", "SmartMedia"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η κάρτα MicroSD αναπτύχθηκε από τη SanDisk το 2004 και έχει διαστάσεις μόλις 15 x 11 χιλιοστά, αποτελώντας την πιο διαδεδομένη μικρή κάρτα μνήμης.",
    "funFacts": [
      "Αρχικά ονομαζόταν 'TransFlash' πριν τυποποιηθεί επίσημα από τον οργανισμό SD Association ως microSD.",
      "Παρά το μέγεθος ενός νυχιού, οι σύγχρονες κάρτες MicroSD μπορούν να αποθηκεύσουν έως και 1 ή 2 Terabytes ψηφιακών δεδομένων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%81%CF%84%CE%B1_SD",
    "locale": "el-GR",
    "tags": ["microsd", "storage", "flash-memory", "mobile"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_178",
    "text": "Ποιος όρος περιγράφει την αγορά, πώληση και διακίνηση προϊόντων και υπηρεσιών μέσω ηλεκτρονικών δικτύων και του διαδικτύου;",
    "answers": ["Ηλεκτρονική διακυβέρνηση", "Ηλεκτρονικό εμπόριο (E-commerce)", "Τηλεργασία", "Τηλεϊατρική"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το ηλεκτρονικό εμπόριο (e-commerce) περιλαμβάνει διαδικτυακά καταστήματα (e-shops), ψηφιακές αγορές και ηλεκτρονικές πληρωμές μέσω διαδικτύου.",
    "funFacts": [
      "Η πρώτη ασφαλής διαδικτυακή συναλλαγή με πιστωτική κάρτα θεωρείται ότι έγινε το 1994 για την αγορά ενός μουσικού άλμπουμ του Στινγκ (Ten Summoner's Tales).",
      "Σήμερα οι παγκόσμιες ηλεκτρονικές πωλήσεις λιανικής ξεπερνούν τα 5 τρισεκατομμύρια δολάρια ετησίως."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97%CE%BB%CE%B5%CE%BA%CF%84%CF%81%CE%BF%CE%BD%CE%B9%CE%BA%CF%8C_%CE%B5%CE%BC%CF%80%CF%8C%CF%81%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["ecommerce", "internet", "business", "shopping"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_179",
    "text": "Ποια πρωτοπόρος εταιρεία διαδικτυακών πληρωμών ιδρύθηκε στα τέλη της δεκαετίας του 1990 και είχε μεταξύ των ιδρυτών της τον Έλον Μασκ και τον Πίτερ Τιλ;",
    "answers": ["Stripe", "Revolut", "PayPal", "Square"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το PayPal δημιουργήθηκε από τη συγχώνευση της Confinity και της X.com το 2000 και έγινε η κορυφαία μέθοδος ασφαλών ψηφιακών συναλλαγών στο διαδίκτυο.",
    "funFacts": [
      "Η ομάδα των αρχικών ιδρυτών και στελεχών του PayPal έμεινε γνωστή ως 'PayPal Mafia', καθώς τα μέλη της ίδρυσαν αργότερα κολοσσούς όπως το YouTube, το LinkedIn, το Yelp και την Tesla.",
      "Εξαγοράστηκε από το eBay το 2002 έναντι 1,5 δισεκατομμυρίων δολαρίων, πριν αποσχιστεί ξανά σε ανεξάρτητη εταιρεία το 2015."
    ],
    "source": "https://el.wikipedia.org/wiki/PayPal",
    "locale": "el-GR",
    "tags": ["paypal", "payments", "fintech", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_180",
    "text": "Ποιος ιστότοπος ηλεκτρονικού εμπορίου που ιδρύθηκε το 1995 από τον Πιερ Ομιντιάρ έγινε παγκοσμίως διάσημος για τις διαδικτυακές δημοπρασίες μεταξύ ιδιωτών;",
    "answers": ["Amazon", "Alibaba", "Craigslist", "eBay"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το eBay ξεκίνησε αρχικά με το όνομα 'AuctionWeb' το 1995 και εξελίχθηκε σε μία από τις μεγαλύτερες πλατφόρμες δημοπρασιών και απευθείας πωλήσεων.",
    "funFacts": [
      "Το πρώτο αντικείμενο που πουλήθηκε ποτέ στο eBay ήταν ένας σπασμένος δείκτης λέιζερ έναντι 14,83 δολαρίων από έναν συλλέκτη χαλασμένων λέιζερ.",
      "Το όνομα eBay προήλθε από την εταιρεία Echo Bay Technology Group του ιδρυτή του."
    ],
    "source": "https://el.wikipedia.org/wiki/EBay",
    "locale": "el-GR",
    "tags": ["ebay", "ecommerce", "auctions", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_181",
    "text": "Πώς ονομάζεται η μέθοδος χρηματοδότησης έργων, προϊόντων και ιδεών μέσω συγκέντρωσης μικρών χρηματικών ποσών από μεγάλο αριθμό υποστηρικτών στο διαδίκτυο;",
    "answers": ["Συμμετοχική χρηματοδότηση (Crowdfunding)", "Εταιρικό ομόλογο", "Κεφάλαιο επιχειρηματικών συμμετοχών", "Τραπεζικό δάνειο"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Crowdfunding (όπως στις πλατφόρμες Kickstarter και Indiegogo) επιτρέπει σε δημιουργούς να χρηματοδοτούν τα έργα τους απευθείας από το κοινό χωρίς μεσάζοντες.",
    "funFacts": [
      "Η πλατφόρμα Kickstarter ξεκίνησε το 2009 και έχει βοηθήσει στη συγκέντρωση πάνω από 7 δισεκατομμυρίων δολαρίων για εκατοντάδες χιλιάδες δημιουργικά έργα.",
      "Ένα από τα πιο επιτυχημένα έργα στην ιστορία του crowdfunding ήταν το έξυπνο ρολόι Pebble Time, που συγκέντρωσε πάνω από 20 εκατομμύρια δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%BC%CE%BC%CE%B5%CF%84%CE%BF%CF%87%CE%B9%CE%BA%CE%AE_%CF%87%CF%81%CE%B7%CE%BC%CE%B1%CF%84%CE%BF%CE%B4%CF%8C%CF%84%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["crowdfunding", "kickstarter", "internet", "business"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_182",
    "text": "Ποιο διεθνές πρότυπο κωδικοποίησης χαρακτήρων επιτρέπει στους υπολογιστές να αναπαριστούν και να χειρίζονται με συνέπεια κείμενα από όλες τις γλώσσες του κόσμου και emojis;",
    "answers": ["ASCII", "Unicode", "Morse", "Binary"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Unicode αποδίδει έναν μοναδικό αριθμό (code point) σε κάθε χαρακτήρα, ανεξάρτητα από την πλατφόρμα, τη συσκευή ή τη γλώσσα προγραμματισμού.",
    "funFacts": [
      "Το παλιό πρότυπο ASCII μπορούσε να κωδικοποιήσει μόνο 128 χαρακτήρες, κυρίως του αγγλικού αλφαβήτου.",
      "Η πιο δημοφιλής υλοποίηση του προτύπου στο διαδίκτυο είναι η μορφή κωδικοποίησης UTF-8, η οποία χρησιμοποιείται σε πάνω από το 98% των ιστοσελίδων."
    ],
    "source": "https://el.wikipedia.org/wiki/Unicode",
    "locale": "el-GR",
    "tags": ["unicode", "utf8", "text", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_183",
    "text": "Σε ποια χώρα σχεδιάστηκαν τα πρώτα 176 ψηφιακά εικονίδια emoji το 1999 από τον σχεδιαστή Σιγκετάκα Κουρίτα για κινητά τηλέφωνα;",
    "answers": ["Νότια Κορέα", "Ηνωμένες Πολιτείες Αμερικής", "Ιαπωνία", "Γερμανία"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Σιγκετάκα Κουρίτα δημιούργησε τα πρώτα emoji για την ιαπωνική εταιρεία κινητής τηλεφωνίας NTT DoCoMo και την πλατφόρμα i-mode.",
    "funFacts": [
      "Η λέξη 'emoji' είναι ιαπωνική και προέρχεται από το 'e' (εικόνα) και 'moji' (χαρακτήρας).",
      "Τα αρχικά 176 πρωτότυπα emojis είχαν ανάλυση μόλις 12x12 pixels και εκτίθενται σήμερα ως έργα τέχνης στο Μουσείο Μοντέρνας Τέχνης (MoMA) της Νέας Υόρκης."
    ],
    "source": "https://el.wikipedia.org/wiki/Emoji",
    "locale": "el-GR",
    "tags": ["emoji", "japan", "communication", "design"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_184",
    "text": "Πώς ονομάζεται το ειδικό πρόγραμμα περιήγησης ανοιχτού κώδικα που δρομολογεί την κυκλοφορία μέσω πολλαπλών επιπέδων κρυπτογράφησης («δρομολόγηση κρεμμυδιού») για ανωνυμία;",
    "answers": ["Opera", "Brave", "Chromium", "Tor Browser"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρόγραμμα περιήγησης Tor Browser κρυπτογραφεί τα δεδομένα και τα στέλνει μέσω τριών τυχαίων ενδιάμεσων κόμβων σε όλο τον κόσμο, αποκρύπτοντας την πραγματική διεύθυνση IP του χρήστη.",
    "funFacts": [
      "Τα αρχικά Tor σημαίνουν 'The Onion Router', αναφερόμενα στα πολλαπλά στρώματα κρυπτογράφησης που ξεφλουδίζονται σαν τα στρώματα ενός κρεμμυδιού.",
      "Αναπτύχθηκε αρχικά από το Ερευνητικό Εργαστήριο του Πολεμικού Ναυτικού των ΗΠΑ (NRL) τη δεκαετία του 1990 για την προστασία στρατιωτικών επικοινωνιών."
    ],
    "source": "https://el.wikipedia.org/wiki/Tor_(%CF%80%CF%81%CF%8C%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1)",
    "locale": "el-GR",
    "tags": ["tor", "privacy", "browsers", "anonymity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_185",
    "text": "Τι σημαίνουν τα αρχικά «VPN» για την τεχνολογία που δημιουργεί μια ασφαλή, κρυπτογραφημένη «σήραγγα» επικοινωνίας μέσω του διαδικτύου;",
    "answers": ["Virtual Private Network", "Variable Packet Node", "Verified Public Network", "Virtual Protected Navigation"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το VPN (Εικονικό Ιδιωτικό Δίκτυο) κρυπτογραφεί τη σύνδεση του χρήστη στο διαδίκτυο, προστατεύοντας τα δεδομένα σε δημόσια Wi-Fi και αποκρύπτοντας την πραγματική γεωγραφική θέση.",
    "funFacts": [
      "Χρησιμοποιείται ευρύτατα από επιχειρήσεις για να επιτρέπει σε εργαζομένους να συνδέονται με ασφάλεια στο εσωτερικό δίκτυο της εταιρείας από το σπίτι.",
      "Ένα VPN κατευθύνει όλη την κίνηση μέσω ενός απομακρυσμένου διακομιστή, κάνοντας τις ιστοσελίδες να βλέπουν την IP του διακομιστή αντί του χρήστη."
    ],
    "source": "https://el.wikipedia.org/wiki/VPN",
    "locale": "el-GR",
    "tags": ["vpn", "security", "networking", "privacy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_186",
    "text": "Πώς ονομάζεται το εξειδικευμένο λογισμικό που έχει σχεδιαστεί για να εντοπίζει, να εμποδίζει και να αφαιρεί κακόβουλο λογισμικό από έναν υπολογιστή;",
    "answers": ["Πρόγραμμα περιήγησης", "Πρόγραμμα προστασίας από ιούς (Antivirus)", "Πρόγραμμα επεξεργασίας κειμένου", "Πρόγραμμα αποσυμπίεσης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Τα προγράμματα antivirus σαρώνουν αρχεία και μνήμη συγκρίνοντας δεδομένα με βάσεις ψηφιακών υπογραφών γνωστών ιών και αναλύοντας ύποπτη συμπεριφορά.",
    "funFacts": [
      "Τα σύγχρονα Windows περιλαμβάνουν το ενσωματωμένο δωρεάν πρόγραμμα Microsoft Defender, το οποίο παρέχει προστασία σε πραγματικό χρόνο.",
      "Εκτός από ιούς, τα σύγχρονα προγράμματα ασφαλείας προστατεύουν από ransomware, spyware, trojans και phishing."
    ],
    "source": "https://el.wikipedia.org/wiki/Antivirus",
    "locale": "el-GR",
    "tags": ["antivirus", "security", "cybersecurity", "malware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_187",
    "text": "Πώς ονομάζεται η πρόσθετη επέκταση περιηγητή (browser extension) που εμποδίζει την προβολή διαφημίσεων και ιχνηλατών στις ιστοσελίδες;",
    "answers": ["VPN", "Password manager", "Πρόγραμμα αποκλεισμού διαφημίσεων (Ad blocker)", "Κρυπτογραφητής"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ένας ad blocker φιλτράρει το περιεχόμενο των ιστοσελίδων και εμποδίζει τη φόρτωση διαφημιστικών banners, αναδυόμενων παραθύρων και διαφημίσεων βίντεο.",
    "funFacts": [
      "Εκτός από την αποφυγή ενοχλητικών διαφημίσεων, οι ad blockers επιταχύνουν σημαντικά τη φόρτωση των σελίδων και μειώνουν την κατανάλωση δεδομένων.",
      "Προστατεύουν επίσης τους χρήστες από το λεγόμενο 'malvertising', δηλαδή κακόβουλο λογισμικό που διακινείται μέσω παραπλανητικών διαφημίσεων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CE%BF%CE%BA%CE%BB%CE%B5%CE%B9%CF%83%CE%BC%CF%8C%CF%82_%CE%B4%CE%B9%CE%B1%CF%86%CE%B7%CE%BC%CE%AF%CF%83%CE%B5%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["ad-blocker", "browsers", "privacy", "web"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_188",
    "text": "Πώς ονομάζεται το κακόβουλο λογισμικό κατασκοπείας που καταγράφει κρυφά κάθε πάτημα πλήκτρου του χρήστη με σκοπό την υποκλοπή κωδικών πρόσβασης;",
    "answers": ["Ransomware", "Adware", "Rootkit", "Keylogger"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το keylogger καταγράφει τις πληκτρολογήσεις του χρήστη και τις αποστέλλει κρυφά στον επιτιθέμενο, υποκλέπτοντας κωδικούς, μηνύματα και αριθμούς καρτών.",
    "funFacts": [
      "Μπορεί να υλοποιηθεί είτε ως πρόγραμμα λογισμικού είτε ως μικρή φυσική συσκευή υλικού που παρεμβάλλεται ανάμεσα στο πληκτρολόγιο και τη θύρα USB του υπολογιστή.",
      "Η χρήση εικονικού πληκτρολογίου στην οθόνη (on-screen keyboard) και η ταυτοποίηση δύο παραγόντων (2FA) βοηθούν στην εξουδετέρωση των keyloggers."
    ],
    "source": "https://el.wikipedia.org/wiki/Keylogger",
    "locale": "el-GR",
    "tags": ["keylogger", "spyware", "malware", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_189",
    "text": "Πώς ονομάζεται ένα εκτεταμένο δίκτυο μολυσμένων συσκευών («ζόμπι») που ελέγχονται εξ αποστάσεως για την εκτέλεση κακόβουλων κυβερνοεπιθέσεων;",
    "answers": ["Botnet", "Intranet", "Mainframe", "Cluster"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ένα botnet αποτελείται από χιλιάδες ή εκατομμύρια υπολογιστές και συσκευές IoT που έχουν μολυνθεί και εκτελούν συντονισμένες εντολές από έναν διακομιστή ελέγχου.",
    "funFacts": [
      "Η λέξη είναι σύντμηση των λέξεων 'robot' και 'network'.",
      "Τα botnets χρησιμοποιούνται συνήθως για την αποστολή δισεκατομμυρίων μηνυμάτων spam, την εξόρυξη κρυπτονομισμάτων και τη διεξαγωγή επιθέσεων DDoS."
    ],
    "source": "https://el.wikipedia.org/wiki/Botnet",
    "locale": "el-GR",
    "tags": ["botnet", "security", "cybersecurity", "malware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_190",
    "text": "Τι σημαίνουν τα αρχικά της επίθεσης «DDoS», κατά την οποία πολλαπλοί υπολογιστές κατακλύζουν έναν διακομιστή με αιτήματα για να τον καταστήσουν μη διαθέσιμο;",
    "answers": ["Direct Denial of Software", "Distributed Denial of Service", "Digital Domain of Servers", "Distributed Data of Systems"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η κατανεμημένη επίθεση άρνησης υπηρεσίας (DDoS - Distributed Denial of Service) υπερφορτώνει έναν στόχο με τεράστιο όγκο ψεύτικης κίνησης ώστε να καταρρεύσει.",
    "funFacts": [
      "Σε αντίθεση με μια απλή επίθεση DoS που προέρχεται από μία μόνο πηγή, η DDoS χρησιμοποιεί χιλιάδες διαφορετικές διευθύνσεις IP ταυτόχρονα μέσω botnet.",
      "Μερικές από τις μεγαλύτερες επιθέσεις DDoS στην ιστορία έχουν ξεπεράσει σε ένταση τα 3 Terabits ανά δευτερόλεπτο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%AF%CE%B8%CE%B5%CF%83%CE%B7_%CE%AC%CF%81%CE%BD%CE%B7%CF%83%CE%B7%CF%82_%CE%B5%CE%BE%CF%85%CF%80%CE%B7%CF%81%CE%AD%CF%84%CE%B7%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["ddos", "security", "cybersecurity", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_191",
    "text": "Ποια διάσημη εφαρμογή της Google δημιουργεί μοναδικούς εξαψήφιους κωδικούς μίας χρήσης κάθε 30 δευτερόλεπτα για ασφαλή είσοδο σε λογαριασμούς;",
    "answers": ["Google Drive", "Google Maps", "Google Authenticator", "Google Keep"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Google Authenticator υλοποιεί τον αλγόριθμο TOTP (Time-based One-time Password) παρέχοντας δεύτερο παράγοντα ταυτοποίησης χωρίς να απαιτείται σύνδεση στο διαδίκτυο.",
    "funFacts": [
      "Επειδή παράγει τους κωδικούς τοπικά στη συσκευή με βάση ένα κοινό μυστικό κλειδί και την ώρα, λειτουργεί ακόμα και σε λειτουργία πτήσης.",
      "Είναι πολύ ασφαλέστερο από τους κωδικούς που αποστέλλονται μέσω SMS, οι οποίοι μπορούν να υποκλαπούν μέσω επιθέσεων SIM swapping."
    ],
    "source": "https://el.wikipedia.org/wiki/Google_Authenticator",
    "locale": "el-GR",
    "tags": ["google-authenticator", "2fa", "security", "google"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_192",
    "text": "Ποιο από τα παρακάτω θεωρείται το πιο κρίσιμο στοιχείο για τη δημιουργία ενός πραγματικά ισχυρού κωδικού πρόσβασης (password);",
    "answers": ["Να περιέχει το όνομα ή την ημερομηνία γέννησης του χρήστη", "Να είναι σύντομος ώστε να απομνημονεύεται εύκολα", "Να χρησιμοποιείται ο ίδιος ακριβώς σε όλους τους λογαριασμούς", "Μεγάλο μήκος και συνδυασμός κεφαλαίων, πεζών, αριθμών και συμβόλων"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ένας ισχυρός κωδικός πρόσβασης πρέπει να έχει μήκος τουλάχιστον 12-16 χαρακτήρων και να συνδυάζει διαφορετικούς τύπους χαρακτήρων χωρίς να περιέχει προβλέψιμες λέξεις λεξικού.",
    "funFacts": [
      "Ο πιο συνηθισμένος και εύκολα παραβιάσιμος κωδικός στον κόσμο παραμένει σταθερά κάθε χρόνο το '123456' και το 'password'.",
      "Οι διαχειριστές κωδικών πρόσβασης (password managers) επιτρέπουν τη δημιουργία και ασφαλή αποθήκευση μοναδικών πολύπλοκων κωδικών για κάθε ιστότοπο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%B4%CE%B9%CE%BA%CF%8C%CF%82_%CF%80%CF%81%CF%8C%CF%83%CE%B2%CE%B1%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["passwords", "security", "cybersecurity", "authentication"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_193",
    "text": "Ποια τεχνολογία βιομετρικής ασφάλειας αναγνωρίζει τις μοναδικές ανάγλυφες γραμμές στην επιφάνεια του ανθρώπινου δακτύλου για ξεκλείδωμα συσκευών;",
    "answers": ["Αισθητήρας δακτυλικών αποτυπωμάτων", "Σαρωτής ίριδας", "Αναγνώριση φωνής", "Αισθητήρας θερμοκρασίας"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο αισθητήρας δακτυλικών αποτυπωμάτων (οπτικός, χωρητικός ή υπερηχητικός) σαρώνει και επαληθεύει το μοναδικό μοτίβο του δακτύλου για άμεση ταυτοποίηση.",
    "funFacts": [
      "Η πιθανότητα δύο άνθρωποι να έχουν ακριβώς το ίδιο δακτυλικό αποτύπωμα υπολογίζεται σε λιγότερο από 1 στα 64 δισεκατομμύρια, ακόμα και για πανομοιότυπους διδύμους.",
      "Το πρώτο κινητό τηλέφωνο με ενσωματωμένο αισθητήρα δακτυλικού αποτυπώματος ήταν το Sagem my G-5 το 2000, ενώ η Apple το καθιέρωσε μαζικά με το iPhone 5s (Touch ID) το 2013."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B1%CE%BA%CF%84%CF%85%CE%BB%CE%B9%CE%BA%CF%8C_%CE%B1%CF%80%CE%BF%CF%84%CF%8D%CF%80%CF%89%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["fingerprint", "biometrics", "security", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_194",
    "text": "Ποιο σύστημα τρισδιάστατης αναγνώρισης προσώπου παρουσίασε η Apple στο iPhone X το 2017 προβάλλοντας 30.000 αόρατες υπέρυθρες κουκκίδες στο πρόσωπο;",
    "answers": ["Touch ID", "Face ID", "Iris Scan", "Smart Lock"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το σύστημα Face ID χρησιμοποιεί την κάμερα TrueDepth και έναν προβολέα υπέρυθρων σημείων για να δημιουργήσει έναν λεπτομερή τρισδιάστατο γεωμετρικό χάρτη του προσώπου.",
    "funFacts": [
      "Σύμφωνα με την Apple, η πιθανότητα τυχαίου ξεκλειδώματος από άλλο άτομο με Face ID είναι περίπου 1 στο 1.000.000 (σε σύγκριση με 1 στις 50.000 για το Touch ID).",
      "Χρησιμοποιεί νευρωνικά δίκτυα μηχανικής μάθησης για να αναγνωρίζει τον χρήστη ακόμα κι αν φορέσει γυαλιά, καπέλο ή αλλάξει κούρεμα."
    ],
    "source": "https://el.wikipedia.org/wiki/Face_ID",
    "locale": "el-GR",
    "tags": ["face-id", "apple", "biometrics", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_195",
    "text": "Ποιος όρος περιγράφει το παγκόσμιο δίκτυο καθημερινών φυσικών συσκευών (λάμπες, θερμοστάτες, οικιακές συσκευές) που συνδέονται στο διαδίκτυο και ανταλλάσσουν δεδομένα;",
    "answers": ["Υπολογιστικό πλέγμα", "Διαδίκτυο βαθιάς κατάδυσης (Deep Web)", "Διαδίκτυο των Πραγμάτων (IoT)", "Εικονικό δίκτυο LAN"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Διαδίκτυο των Πραγμάτων (IoT - Internet of Things) επιτρέπει σε οικιακές συσκευές και αισθητήρες να επικοινωνούν μεταξύ τους και να ελέγχονται εξ αποστάσεως.",
    "funFacts": [
      "Ο όρος επινοήθηκε το 1999 από τον Βρετανό πρωτοπόρο της τεχνολογίας Κέβιν Άστον κατά τη διάρκεια παρουσίασης στην Procter & Gamble.",
      "Εκτιμάται ότι σήμερα υπάρχουν περισσότερες από 15 δισεκατομμύρια συνδεδεμένες συσκευές IoT παγκοσμίως, ξεπερνώντας κατά πολύ τον ανθρώπινο πληθυσμό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B1%CE%B4%CE%AF%CE%BA%CF%84%CF%85%CE%BF_%CF%84%CF%89%CE%BD_%CF%80%CF%81%CE%B1%CE%B3%CE%BC%CE%AC%CF%84%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["iot", "smart-home", "internet", "connected-devices"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_196",
    "text": "Πώς ονομάζεται η δημοφιλής εικονική ψηφιακή βοηθός φωνής της Amazon που ενσωματώνεται στα έξυπνα ηχεία Echo;",
    "answers": ["Cortana", "Siri", "Google Assistant", "Alexa"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Alexa είναι η φωνητική βοηθός της Amazon με δυνατότητες αναπαραγωγής μουσικής, ελέγχου έξυπνου σπιτιού, ενημέρωσης καιρού και εκτέλεσης χιλιάδων 'skills'.",
    "funFacts": [
      "Το όνομα Alexa επιλέχθηκε επειδή περιέχει το σύμφωνο 'X', το οποίο αναγνωρίζεται φωνητικά με μεγάλη ακρίβεια από τους αλγορίθμους, καθώς και ως φόρος τιμής στη Βιβλιοθήκη της Αλεξάνδρειας.",
      "Παρουσιάστηκε για πρώτη φορά τον Νοέμβριο του 2014 μαζί με το πρώτο έξυπνο ηχείο Amazon Echo."
    ],
    "source": "https://el.wikipedia.org/wiki/Amazon_Alexa",
    "locale": "el-GR",
    "tags": ["alexa", "amazon", "voice-assistant", "smart-home"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_197",
    "text": "Ποια έξυπνη οικιακή συσκευή επιτρέπει στον χρήστη να αλλάζει φωτεινότητα και χρώματα στο σπίτι μέσω smartphone ή φωνητικών εντολών;",
    "answers": ["Έξυπνη λάμπα (Smart bulb)", "Έξυπνο ψυγείο", "Έξυπνος φούρνος", "Έξυπνος διακόπτης ρολών"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι έξυπνες λάμπες LED συνδέονται μέσω Wi-Fi, Bluetooth ή Zigbee επιτρέποντας αυτοματισμούς, χρονοδιαγράμματα και ρύθμιση εκατομμυρίων χρωμάτων.",
    "funFacts": [
      "Μία από τις πρώτες και πιο επιτυχημένες σειρές έξυπνου φωτισμού είναι η Philips Hue, που πρωτοκυκλοφόρησε το 2012.",
      "Καταναλώνουν έως και 80% λιγότερη ενέργεια σε σχέση με τους παλιούς λαμπτήρες πυρακτώσεως χάρη στην τεχνολογία LED."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%89%CF%84%CE%BF%CE%B4%CE%AF%CE%BF%CE%B4%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["smart-bulb", "smart-home", "led", "lighting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_198",
    "text": "Ποια έξυπνη συσκευή παρεμβάλλεται ανάμεσα στην πρίζα τοίχου και μια συμβατική οικιακή συσκευή, επιτρέποντας τον εξ αποστάσεως έλεγχο και τη μέτρηση κατανάλωσης;",
    "answers": ["Πολύπριζο ασφαλείας", "Έξυπνη πρίζα (Smart plug)", "Μετασχηματιστής", "Σταθεροποιητής τάσης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η έξυπνη πρίζα (smart plug) συνδέεται στο τοπικό Wi-Fi και επιτρέπει την ενεργοποίηση ή απενεργοποίηση οποιασδήποτε συνδεδεμένης συσκευής μέσω εφαρμογής.",
    "funFacts": [
      "Μπορεί να ρυθμιστεί ώστε να κλείνει αυτόματα συσκευές όταν λείπουμε από το σπίτι, συμβάλλοντας στη μείωση του λογαριασμού ρεύματος.",
      "Πολλά μοντέλα παρέχουν ιστορικό καταγραφής της ηλεκτρικής ισχύος και κατανάλωσης σε κιλοβατώρες (kWh)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B5%CF%85%CE%BC%CE%B1%CF%84%CE%BF%CE%BB%CE%AE%CF%80%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["smart-plug", "smart-home", "iot", "gadgets"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_199",
    "text": "Ποια πρωτοποριακή ρομποτική ηλεκτρική σκούπα καθαρισμού δαπέδων κυκλοφόρησε η εταιρεία iRobot το 2002 κάνοντας τα οικιακά ρομπότ εμπορική πραγματικότητα;",
    "answers": ["Aibo", "Asimo", "Roomba", "Roborock"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Roomba της iRobot ήταν το πρώτο ευρέως επιτυχημένο εμπορικό οικιακό ρομπότ καθαρισμού, χρησιμοποιώντας αισθητήρες για αυτόνομη πλοήγηση στον χώρο.",
    "funFacts": [
      "Η εταιρεία iRobot ιδρύθηκε αρχικά το 1990 από ερευνητές ρομποτικής του κορυφαίου πανεπιστημίου MIT.",
      "Τα σύγχρονα μοντέλα ρομποτικών σκουπών χρησιμοποιούν αισθητήρες LIDAR και κάμερες για να δημιουργούν λεπτομερείς κατόψεις των δωματίων."
    ],
    "source": "https://el.wikipedia.org/wiki/Roomba",
    "locale": "el-GR",
    "tags": ["roomba", "robotics", "appliances", "smart-home"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_200",
    "text": "Πώς ονομάζεται ένα όχημα που είναι εξοπλισμένο με αισθητήρες, κάμερες και τεχνητή νοημοσύνη ώστε να κινείται και να πλοηγείται αυτόνομα χωρίς άνθρωπο οδηγό;",
    "answers": ["Υβριδικό όχημα", "Ηλεκτρικό καρτ", "Τηλεκατευθυνόμενο αυτοκίνητο", "Αυτόνομο όχημα (Self-driving car)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Τα αυτόνομα οχήματα (self-driving cars) χρησιμοποιούν συνδυασμό καμερών, ραντάρ, αισθητήρων LIDAR και προηγμένων αλγορίθμων για ασφαλή πλοήγηση στους δρόμους.",
    "funFacts": [
      "Ο διεθνής οργανισμός SAE ορίζει 6 επίπεδα αυτονομίας οδήγησης, από το Επίπεδο 0 (καμία αυτονομία) έως το Επίπεδο 5 (πλήρης αυτονομία υπό οποιεσδήποτε συνθήκες).",
      "Εταιρείες όπως η Waymo λειτουργούν ήδη εμπορικές υπηρεσίες πλήρως αυτόνομων ταξί χωρίς οδηγό (robotaxis) σε επιλεγμένες πόλεις των ΗΠΑ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%85%CF%84%CF%8C%CE%BD%CE%BF%CE%BC%CE%BF_%CF%8C%CF%87%CE%B7%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["autonomous-vehicles", "self-driving", "ai", "transportation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_201",
    "text": "Ποια τεχνολογία οπτικής ανίχνευσης χρησιμοποιεί χιλιάδες παλμούς λέιζερ ανά δευτερόλεπτο για να δημιουργήσει λεπτομερή τρισδιάστατο χάρτη του περιβάλλοντος χώρου;",
    "answers": ["LIDAR", "RADAR", "SONAR", "GPS"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το LIDAR (Light Detection and Ranging) μετρά τον χρόνο που χρειάζεται το ανακλώμενο φως λέιζερ να επιστρέψει στον αισθητήρα, υπολογίζοντας αποστάσεις με ακρίβεια χιλιοστού.",
    "funFacts": [
      "Εκτός από τα αυτόνομα αυτοκίνητα, μικρογραφία αισθητήρα LiDAR ενσωματώνεται στα μοντέλα iPhone Pro της Apple για ταχύτερη εστίαση και εφαρμογές επαυξημένης πραγματικότητας.",
      "Χρησιμοποιήθηκε από την αποστολή Apollo 15 το 1971 για τη λεπτομερή χαρτογράφηση της επιφάνειας της Σελήνης."
    ],
    "source": "https://el.wikipedia.org/wiki/Lidar",
    "locale": "el-GR",
    "tags": ["lidar", "sensors", "lasers", "autonomous-vehicles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_202",
    "text": "Ποιος μικροσκοπικός αισθητήρας στο εσωτερικό των σύγχρονων smartphones ανιχνεύει τον γωνιακό προσανατολισμό και την περιστροφή της συσκευής στον τρισδιάστατο χώρο;",
    "answers": ["Βαρόμετρο", "Γυροσκόπιο", "Θερμόμετρο", "Μαγνητόμετρο"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το γυροσκόπιο (MEMS gyroscope) μετρά τον ρυθμό περιστροφής γύρω από τους τρεις άξονες (pitch, roll, yaw), επιτρέποντας ακριβή έλεγχο σε βιντεοπαιχνίδια και εφαρμογές VR.",
    "funFacts": [
      "Σε συνδυασμό με το επιταχυνσιόμετρο, επιτρέπει στο τηλέφωνο να καταλαβαίνει με ακρίβεια πότε το γυρίζουμε οριζόντια για να προβάλει ένα βίντεο σε πλήρη οθόνη.",
      "Βασίζεται στην τεχνολογία MEMS (Μικρο-Ηλεκτρο-Μηχανικά Συστήματα), όπου μικροσκοπικά κινούμενα εξαρτήματα χαράσσονται απευθείας πάνω σε τσιπ πυριτίου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CF%85%CF%81%CE%BF%CF%83%CE%BA%CF%8C%CF%80%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["gyroscope", "sensors", "hardware", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_203",
    "text": "Ποιος αισθητήρας των smartphones και των fitness trackers μετρά τις γραμμικές δυνάμεις επιτάχυνσης και κίνησης, λειτουργώντας ως βηματόμετρο;",
    "answers": ["Υγρόμετρο", "Αισθητήρας καρδιακών παλμών", "Επιταχυνσιόμετρο (Accelerometer)", "Βαρόμετρο"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το επιταχυνσιόμετρο καταγράφει τις αλλαγές στην ταχύτητα κίνησης της συσκευής και χρησιμοποιείται για την καταμέτρηση βημάτων και την ανίχνευση πτώσεων.",
    "funFacts": [
      "Ανιχνεύει επίσης τη δύναμη της γήινης βαρύτητας, επιτρέποντας στη συσκευή να γνωρίζει προς τα πού είναι το 'κάτω'.",
      "Χρησιμοποιείται στα αυτοκίνητα για την ακαριαία ενεργοποίηση των αερόσακων σε περίπτωση σφοδρής σύγκρουσης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%84%CE%B1%CF%87%CF%85%CE%BD%CF%83%CE%B9%CF%8C%CE%BC%CE%B5%CF%84%CF%81%CE%BF",
    "locale": "el-GR",
    "tags": ["accelerometer", "sensors", "hardware", "wearables"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_204",
    "text": "Ποιος αισθητήρας στο πάνω μέρος ενός smartphone απενεργοποιεί αυτόματα την οθόνη αφής όταν πλησιάζουμε τη συσκευή στο αυτί κατά τη διάρκεια μιας τηλεφωνικής κλήσης;",
    "answers": ["Αισθητήρας υπερύθρων τηλεχειριστηρίου", "Αισθητήρας δακτυλικού αποτυπώματος", "Αισθητήρας Hall", "Αισθητήρας εγγύτητας (Proximity sensor)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο αισθητήρας εγγύτητας ανιχνεύει την παρουσία κοντινών αντικειμένων (όπως το μάγουλο ή το αυτί) για να αποτρέψει τυχαία πατήματα κουμπιών κατά την ομιλία.",
    "funFacts": [
      "Εκτός από την αποτροπή ανεπιθύμητων πατημάτων, η απενεργοποίηση της οθόνης εξοικονομεί σημαντική ενέργεια μπαταρίας κατά τις τηλεφωνικές συνομιλίες.",
      "Λειτουργεί συνήθως εκπέμποντας μια αόρατη δέσμη υπέρυθρου φωτός και μετρώντας την ανάκλασή της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%B9%CF%83%CE%B8%CE%B7%CF%84%CE%AE%CF%81%CE%B1%CF%82_%CE%B5%CE%B3%CE%B3%CF%8D%CF%84%CE%B7%CF%84%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["proximity-sensor", "sensors", "smartphones", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_205",
    "text": "Ποιος αισθητήρας μετρά την ένταση του φωτός στον περιβάλλοντα χώρο ώστε να ρυθμίζει αυτόματα τη φωτεινότητα της οθόνης μιας συσκευής;",
    "answers": ["Αισθητήρας φωτισμού περιβάλλοντος (Ambient light sensor)", "Μαγνητικός αισθητήρας", "Αισθητήρας πίεσης", "Αισθητήρας υπερήχων"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο αισθητήρας φωτισμού περιβάλλοντος αυξάνει τη φωτεινότητα κάτω από έντονο ηλιακό φως για ευκρίνεια και τη μειώνει στο σκοτάδι για ξεκούραστη θέαση.",
    "funFacts": [
      "Η αυτόματη ρύθμιση φωτεινότητας μπορεί να παρατείνει τη διάρκεια ζωής της μπαταρίας ενός smartphone έως και κατά 30%.",
      "Χρησιμοποιεί φωτοδίοδο ευαίσθητη στο ορατό φως παρόμοια με τη λειτουργία της ανθρώπινης όρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%89%CF%84%CE%BF%CE%B4%CE%AF%CE%BF%CE%B4%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["ambient-light-sensor", "sensors", "displays", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_206",
    "text": "Πώς ονομάζεται η λειτουργία ενός κινητού τηλεφώνου που του επιτρέπει να δέχεται και να λειτουργεί ταυτόχρονα με δύο διαφορετικές κάρτες τηλεφωνίας;",
    "answers": ["Single SIM", "Dual SIM", "Multi-touch", "Split screen"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Μια συσκευή Dual SIM επιτρέπει τη διατήρηση δύο ξεχωριστών τηλεφωνικών αριθμών (π.χ. έναν επαγγελματικό και έναν προσωπικό) στην ίδια συσκευή.",
    "funFacts": [
      "Πολλά σύγχρονα τηλέφωνα συνδυάζουν μία φυσική υποδοχή κάρτας nano-SIM με μία ψηφιακή ηλεκτρονική κάρτα eSIM.",
      "Στη λειτουργία 'Dual SIM Standby', και οι δύο γραμμές μπορούν να δέχονται κλήσεις, αλλά όταν η μία είναι σε ενεργή συνομιλία, η άλλη εμφανίζεται προσωρινά μη διαθέσιμη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%81%CF%84%CE%B1_SIM",
    "locale": "el-GR",
    "tags": ["dual-sim", "smartphones", "mobile", "telecommunications"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_207",
    "text": "Πόσα μεμονωμένα pixels περιέχει ακριβώς ένα Megapixel (1 MP) στην ανάλυση μιας ψηφιακής φωτογραφικής μηχανής ή κάμερας κινητού;",
    "answers": ["1.000 pixels", "10.000 pixels", "1.000.000 pixels", "1.000.000.000 pixels"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρόθεμα 'Mega-' σημαίνει ένα εκατομμύριο, συνεπώς μια κάμερα 12 Megapixels συλλαμβάνει εικόνες αποτελούμενες από περίπου 12 εκατομμύρια pixels.",
    "funFacts": [
      "Μια τυπική φωτογραφία ανάλυσης 4000 επί 3000 pixels ισοδυναμεί ακριβώς με 12.000.000 pixels, δηλαδή 12 Megapixels.",
      "Παρότι τα περισσότερα Megapixels προσφέρουν μεγαλύτερη λεπτομέρεια για μεγεθύνσεις, η ποιότητα της εικόνας εξαρτάται εξίσου από το φυσικό μέγεθος του αισθητήρα και την ποιότητα του φακού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B9%CE%BA%CE%BF%CE%BD%CE%BF%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%CE%AF%CE%BF",
    "locale": "el-GR",
    "tags": ["megapixel", "cameras", "photography", "imaging"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_208",
    "text": "Ποιος τύπος ζουμ σε μια φωτογραφική μηχανή μεγεθύνει το θέμα χρησιμοποιώντας πραγματική κίνηση οπτικών γυάλινων φακών χωρίς καμία υποβάθμιση της ποιότητας;",
    "answers": ["Ψηφιακό ζουμ (Digital zoom)", "Υβριδικό ζουμ", "Ηλεκτρονικό ζουμ", "Οπτικό ζουμ (Optical zoom)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το οπτικό ζουμ (optical zoom) μεταβάλλει τη φυσική εστιακή απόσταση των οπτικών στοιχείων του φακού, προσφέροντας γνήσια μεγέθυνση σε πλήρη ανάλυση.",
    "funFacts": [
      "Επειδή τα σύγχρονα λεπτά smartphones δεν έχουν χώρο για κινούμενους φακούς, χρησιμοποιούν ξεχωριστές κάμερες-τηλεφακούς ή σχεδιασμό περισκοπίου για οπτικό ζουμ.",
      "Στον σχεδιασμό περισκοπίου, το φως ανακλάται κατά 90 μοίρες με πρίσμα κατά μήκος του σώματος του τηλεφώνου επιτρέποντας οπτικό ζουμ 5x ή 10x."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%89%CF%84%CE%BF%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CF%8C%CF%82_%CF%86%CE%B1%CE%BA%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["optical-zoom", "cameras", "photography", "optics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_209",
    "text": "Πώς λειτουργεί το απλό ψηφιακό ζουμ (digital zoom) σε μια κάμερα smartphone όταν δεν υπάρχει διαθέσιμος οπτικός τηλεφακός;",
    "answers": ["Περικόπτει ψηφιακά το κεντρικό τμήμα της εικόνας και το μεγεθύνει χάνοντας λεπτομέρεια", "Προσθέτει περισσότερους φακούς μπροστά από τον αισθητήρα", "Αυξάνει αυτόματα τον φωτισμό του φλας", "Αλλάζει τη θερμοκρασία του αισθητήρα"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το ψηφιακό ζουμ δεν μεγεθύνει οπτικά το θέμα, αλλά απλώς αποκόπτει (crop) ψηφιακά ένα κομμάτι του κάδρου και το παρεμβάλλει, με αποτέλεσμα πιξελιασμένη εικόνα.",
    "funFacts": [
      "Τα σύγχρονα κορυφαία smartphones χρησιμοποιούν τεχνητή νοημοσύνη και τεχνικές Super Resolution για να ανακτήσουν χαμένες λεπτομέρειες στο ψηφιακό ζουμ.",
      "Το ψηφιακό ζουμ ισοδυναμεί πρακτικά με το να τραβήξει κανείς μια κανονική φωτογραφία και να την περικόψει αργότερα σε ένα πρόγραμμα επεξεργασίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A8%CE%B7%CF%86%CE%B9%CE%B1%CE%BA%CE%AE_%CF%86%CF%89%CF%84%CE%BF%CE%B3%CF%81%CE%B1%CF%86%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["digital-zoom", "cameras", "smartphones", "photography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_210",
    "text": "Τι προσφέρει το σύστημα οπτικής σταθεροποίησης εικόνας (OIS) στις κάμερες σύγχρονων smartphones και φωτογραφικών μηχανών;",
    "answers": ["Αυξάνει αυτόματα τα Megapixels της κάμερας", "Εξουδετερώνει το τρέμουλο των χεριών μετακινώντας μηχανικά τον φακό ή τον αισθητήρα", "Επιτρέπει τη λήψη υποβρύχιων φωτογραφιών", "Αποθηκεύει τις φωτογραφίες απευθείας στο cloud"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το OIS (Optical Image Stabilization) χρησιμοποιεί μικροσκοπικούς ηλεκτρομαγνητικούς ενεργοποιητές για να αντισταθμίζει σε πραγματικό χρόνο τις μικροκινήσεις των χεριών.",
    "funFacts": [
      "Είναι ιδιαίτερα κρίσιμο για νυχτερινές λήψεις, καθώς επιτρέπει στο κλείστρο να παραμένει ανοιχτό για περισσότερο χρόνο χωρίς να βγαίνει η φωτογραφία θολή (motion blur).",
      "Εξασφαλίζει επίσης εξαιρετικά ομαλή εγγραφή βίντεο κατά το περπάτημα χωρίς να απαιτείται εξωτερικός σταθεροποιητής (gimbal)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B1%CE%B8%CE%B5%CF%81%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_%CE%B5%CE%B9%CE%BA%CF%8C%CE%BD%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["ois", "cameras", "photography", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'easy', 1, questions)

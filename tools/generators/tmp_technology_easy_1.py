# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "technology_easy_011",
    "text": "Σε ποιον ιστορικό βασιλιά της Δανίας οφείλει το όνομά της η ασύρματη τεχνολογία Bluetooth;",
    "answers": ["Χάραλντ ο Κυανόδους", "Κνούτος ο Μέγας", "Έρικ ο Ερυθρός", "Σβεν ο Διχαλογένης"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η τεχνολογία Bluetooth πήρε το όνομά της από τον βασιλιά Χάραλντ «Κυανόδοντα» (Harald Blåtand / Bluetooth) της Δανίας και της Νορβηγίας.",
    "funFacts": [
      "Ο Χάραλντ ο Κυανόδους έμεινε στην ιστορία επειδή ένωσε τις σκανδιναβικές φυλές σε ένα ενιαίο βασίλειο, όπως το Bluetooth ενώνει διάφορες συσκευές επικοινωνίας.",
      "Το διάσημο λογότυπο του Bluetooth είναι ένα κράμα των αρχαίων σκανδιναβικών ρούνων Hagall (ᚼ) και Bjarkan (ᛒ), δηλαδή των αρχικών H.B."
    ],
    "source": "https://el.wikipedia.org/wiki/Bluetooth",
    "locale": "el-GR",
    "tags": ["bluetooth", "wireless", "history", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_012",
    "text": "Τι σημαίνουν τα αρχικά του ευρέως διαδεδομένου προτύπου σύνδεσης περιφερειακών USB;",
    "answers": ["Unified System Bus", "Universal Serial Bus", "Universal Storage Board", "Ultra Speed Binary"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το USB (Universal Serial Bus) καθιερώθηκε το 1996 για να τυποποιήσει τη σύνδεση πληκτρολογίων, ποντικιών, εκτυπωτών και άλλων περιφερειακών σε υπολογιστές.",
    "funFacts": [
      "Πριν από την καθιέρωση του USB, οι υπολογιστές απαιτούσαν ξεχωριστές σειριακές και παράλληλες θύρες για κάθε διαφορετική συσκευή.",
      "Η νεότερη υποδοχή USB Type-C έχει αναστρέψιμο σχεδιασμό, επιτρέποντας τη σύνδεση του καλωδίου από οποιαδήποτε πλευρά."
    ],
    "source": "https://el.wikipedia.org/wiki/USB",
    "locale": "el-GR",
    "tags": ["usb", "hardware", "cables", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_013",
    "text": "Ποιο βασικό εξάρτημα χαρακτηρίζεται συχνά ως ο «εγκέφαλος» ενός ηλεκτρονικού υπολογιστή;",
    "answers": ["Τροφοδοτικό (PSU)", "Σκληρός δίσκος (HDD)", "Κεντρική Μονάδα Επεξεργασίας (CPU)", "Κάρτα ήχου"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η CPU (Central Processing Unit) εκτελεί τις εντολές των προγραμμάτων και επεξεργάζεται τα δεδομένα του συστήματος.",
    "funFacts": [
      "Ο πρώτος εμπορικός μικροεπεξεργαστής μονού τσιπ στον κόσμο ήταν ο Intel 4004, ο οποίος κυκλοφόρησε το 1971.",
      "Οι σύγχρονοι επεξεργαστές περιέχουν δισεκατομμύρια μικροσκοπικά τρανζίστορ χαραγμένα σε μια επιφάνεια πυριτίου λίγων τετραγωνικών χιλιοστών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CE%AE_%CE%BC%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CE%B5%CF%80%CE%B5%CE%BE%CE%B5%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["cpu", "hardware", "processor", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_014",
    "text": "Ποιο είδος μνήμης υπολογιστή χάνει όλα τα αποθηκευμένα δεδομένα του όταν διακοπεί η τροφοδοσία ρεύματος;",
    "answers": ["Σκληρός δίσκος (HDD)", "Μνήμη Flash USB", "Οπτικός δίσκος DVD", "Μνήμη RAM"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η RAM (Random Access Memory) είναι πτητική μνήμη (volatile memory), που σημαίνει ότι απαιτεί συνεχή παροχή ηλεκτρικού ρεύματος για να διατηρεί τα δεδομένα της.",
    "funFacts": [
      "Χρησιμεύει ως χώρος προσωρινής αποθήκευσης δεδομένων και εντολών που χρειάζεται άμεσα ο επεξεργαστής κατά την εκτέλεση εφαρμογών.",
      "Όσο περισσότερη μνήμη RAM διαθέτει ένας υπολογιστής, τόσο περισσότερες εφαρμογές μπορεί να τρέχει ταυτόχρονα χωρίς καθυστερήσεις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BD%CE%AE%CE%BC%CE%B7_%CF%84%CF%85%CF%87%CE%B1%CE%AF%CE%B1%CF%82_%CF%80%CF%81%CE%BF%CF%83%CF%80%CE%AD%CE%BB%CE%B1%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["ram", "memory", "hardware", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_015",
    "text": "Ποιο σύμβολο πληκτρολογίου χρησιμοποιείται υποχρεωτικά για τον διαχωρισμό του ονόματος χρήστη και του παρόχου σε μια διεύθυνση email;",
    "answers": ["@ (παπάκι)", "# (δίεση)", "& (και)", "% (επί τοις εκατό)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το σύμβολο @ επιλέχθηκε το 1971 από τον Ρέι Τόμλινσον για να συνδέει το όνομα του χρήστη με το όνομα του υπολογιστή/διακομιστή στο δίκτυο ARPANET.",
    "funFacts": [
      "Στα ελληνικά το σύμβολο @ αποκαλείται συνήθως 'παπάκι', ενώ στα ιταλικά 'chiocciola' (σαλιγκάρι) και στα γαλλικά 'arobase'.",
      "Ο Ρέι Τόμλινσον έστειλε το πρώτο email μεταξύ δύο υπολογιστών που βρίσκονταν δίπλα ο ένας στον άλλον στο δίκτυο ARPANET."
    ],
    "source": "https://el.wikipedia.org/wiki/@",
    "locale": "el-GR",
    "tags": ["email", "internet", "symbols", "communication"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_016",
    "text": "Ποιος ίδρυσε το Facebook το 2004 κατά τη διάρκεια των σπουδών του στο Πανεπιστήμιο Χάρβαρντ;",
    "answers": ["Έλον Μασκ", "Μαρκ Ζάκερμπεργκ", "Τζεφ Μπέζος", "Τζακ Ντόρσεϊ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Μαρκ Ζάκερμπεργκ μαζί με τους συμφοιτητές του Εντουάρντο Σάβεριν, Άντριου ΜακΚόλουμ, Ντάστιν Μόσκοβιτς και Κρις Χιουζ δημιούργησαν το Facebook τον Φεβρουάριο του 2004.",
    "funFacts": [
      "Αρχικά ονομαζόταν 'Thefacebook' και η πρόσβαση περιοριζόταν αποκλειστικά σε φοιτητές του Χάρβαρντ.",
      "Το 2021 η μητρική εταιρεία του Facebook μετονομάστηκε σε Meta για να αντικατοπτρίζει τη στροφή της προς το metaverse."
    ],
    "source": "https://el.wikipedia.org/wiki/Facebook",
    "locale": "el-GR",
    "tags": ["facebook", "meta", "social-media", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_017",
    "text": "Ποια εταιρεία λογισμικού δημιούργησε το ευρέως διαδεδομένο πρότυπο αρχείων εγγράφων PDF;",
    "answers": ["Microsoft", "Oracle", "Adobe", "Corel"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Adobe Systems ανέπτυξε τη μορφή αρχείων PDF (Portable Document Format) το 1993 με στόχο τη συνεπή προβολή εγγράφων σε οποιαδήποτε συσκευή.",
    "funFacts": [
      "Το κύριο πλεονέκτημα του PDF είναι ότι διατηρεί ακριβώς την ίδια μορφοποίηση, γραμματοσειρές και εικόνες ανεξάρτητα από το λειτουργικό σύστημα ή το υλικό.",
      "Από το 2008 το PDF έχει αναγνωριστεί ως ανοιχτό διεθνές πρότυπο από τον Διεθνή Οργανισμό Τυποποίησης (ISO)."
    ],
    "source": "https://el.wikipedia.org/wiki/PDF",
    "locale": "el-GR",
    "tags": ["pdf", "adobe", "software", "formats"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_018",
    "text": "Ποιο ζώο αποτελεί την επίσημη μασκότ του λειτουργικού συστήματος Linux;",
    "answers": ["Αλεπού", "Χαμαιλέοντας", "Πάντα", "Πιγκουίνος"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο πιγκουίνος Tux είναι η παγκοσμίως αναγνωρίσιμη επίσημη μασκότ του ανοιχτού κώδικα πυρήνα Linux.",
    "funFacts": [
      "Η μασκότ σχεδιάστηκε το 1996 από τον Λάρι Γουίνγκ χρησιμοποιώντας το ελεύθερο πρόγραμμα επεξεργασίας εικόνας GIMP.",
      "Ο δημιουργός του Linux, Λίνους Τόρβαλντς, επέλεξε τον πιγκουίνο επειδή είχε δεχτεί τσίμπημα από έναν μικρό πιγκουίνο κατά την επίσκεψή του σε ζωολογικό κήπο στην Αυστραλία."
    ],
    "source": "https://el.wikipedia.org/wiki/Tux",
    "locale": "el-GR",
    "tags": ["linux", "open-source", "mascot", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_019",
    "text": "Ποια είναι η μεγαλύτερη διαδικτυακή ελεύθερη εγκυκλοπαίδεια στον κόσμο, την οποία μπορεί να επεξεργαστεί οποιοσδήποτε;",
    "answers": ["Βικιπαίδεια (Wikipedia)", "Encarta", "Britannica Online", "Citizendium"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Βικιπαίδεια (Wikipedia) ιδρύθηκε τον Ιανουάριο του 2001 από τον Τζίμι Γουέιλς και τον Λάρι Σάνγκερ.",
    "funFacts": [
      "Το όνομά της προκύπτει από τη σύνθεση της χαβανέζικης λέξης 'wiki' (που σημαίνει γρήγορα) και της ελληνικής 'εγκυκλοπαίδεια'.",
      "Διαθέτει λήμματα σε περισσότερες από 300 διαφορετικές γλώσσες και συντηρείται αποκλειστικά από εθελοντές συντάκτες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%BA%CE%B9%CF%80%CE%B1%CE%AF%CE%B4%CE%B5%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["wikipedia", "internet", "encyclopedia", "web"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_020",
    "text": "Ποιο πρωτοποριακό φορητό player ψηφιακής μουσικής παρουσίασε η Apple το 2001 με το σύνθημα «1.000 τραγούδια στην τσέπη σας»;",
    "answers": ["Walkman", "iPod", "Zune", "Discman"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρώτο iPod κυκλοφόρησε τον Οκτώβριο του 2001 διαθέτοντας σκληρό δίσκο 5 GB και έναν καινοτόμο περιστροφικό τροχό πλοήγησης (scroll wheel).",
    "funFacts": [
      "Η συνδυασμένη επιτυχία του iPod και του iTunes Store άλλαξε ριζικά τον τρόπο με τον οποίο το κοινό αγόραζε και άκουγε μουσική παγκοσμίως.",
      "Η Apple απέσυρε επίσημα το τελευταίο μοντέλο της σειράς (iPod Touch) τον Μάιο του 2022, κλείνοντας έναν κύκλο πάνω από 20 ετών."
    ],
    "source": "https://el.wikipedia.org/wiki/IPod",
    "locale": "el-GR",
    "tags": ["apple", "ipod", "music", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_021",
    "text": "Πόσα bits (δυαδικά ψηφία) απαρτίζουν ακριβώς ένα Byte ψηφιακών δεδομένων;",
    "answers": ["4", "6", "8", "16"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ένα Byte αποτελείται σταθερά από 8 bits, επιτρέποντας 256 διαφορετικούς συνδυασμούς (από 00000000 έως 11111111).",
    "funFacts": [
      "Μια ομάδα 4 bits (το μισό ενός Byte) αποκαλείται επίσημα στην πληροφορική 'nibble'.",
      "Ο όρος 'byte' επινοήθηκε από τον επιστήμονα Βέρνερ Μπούχολτς το 1956 κατά τη διάρκεια σχεδιασμού του υπολογιστή IBM Stretch."
    ],
    "source": "https://el.wikipedia.org/wiki/Byte",
    "locale": "el-GR",
    "tags": ["byte", "bits", "binary", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_022",
    "text": "Ποια γλώσσα σήμανσης αποτελεί το βασικό θεμέλιο για τη δομή και το περιεχόμενο όλων των ιστοσελίδων;",
    "answers": ["SQL", "C++", "Java", "HTML"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η HTML (HyperText Markup Language) χρησιμοποιεί ετικέτες (tags) για να ορίσει κείμενα, εικόνες, συνδέσμους και άλλα στοιχεία σε μια ιστοσελίδα.",
    "funFacts": [
      "Δημιουργήθηκε από τον Τιμ Μπέρνερς-Λι στα τέλη της δεκαετίας του 1980 στο ερευνητικό κέντρο CERN.",
      "Η πιο σύγχρονη έκδοση του προτύπου είναι η HTML5, η οποία ενσωματώνει εγγενή υποστήριξη για αναπαραγωγή βίντεο και ήχου χωρίς εξωτερικά πρόσθετα."
    ],
    "source": "https://el.wikipedia.org/wiki/HTML",
    "locale": "el-GR",
    "tags": ["html", "web", "programming", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_023",
    "text": "Ποιος ερευνητικός οργανισμός τεχνητής νοημοσύνης ανέπτυξε και διέθεσε στο κοινό το ChatGPT το 2022;",
    "answers": ["OpenAI", "DeepMind", "Nvidia", "Baidu"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η εταιρεία OpenAI κυκλοφόρησε το ChatGPT τον Νοέμβριο του 2022, προκαλώντας παγκόσμια επανάσταση στη γενετική τεχνητή νοημοσύνη (Generative AI).",
    "funFacts": [
      "Το ChatGPT απέκτησε περισσότερους από 100 εκατομμύρια ενεργούς χρήστες μέσα σε μόλις δύο μήνες, καθιστώντας το μία από τις ταχύτερα αναπτυσσόμενες εφαρμογές στην ιστορία.",
      "Τα αρχικά GPT σημαίνουν 'Generative Pre-trained Transformer', περιγράφοντας την υποκείμενη αρχιτεκτονική νευρωνικών δικτύων."
    ],
    "source": "https://el.wikipedia.org/wiki/ChatGPT",
    "locale": "el-GR",
    "tags": ["ai", "chatgpt", "openai", "machine-learning"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_024",
    "text": "Τι σημαίνουν τα αρχικά του κώδικα «QR Code» που σαρώνουμε καθημερινά με την κάμερα του κινητού τηλεφώνου;",
    "answers": ["Quantum Reader", "Quick Response", "Quality Radio", "Quick Route"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο κώδικας QR (Quick Response - Γρήγορη Απόκριση) σχεδιάστηκε για να επιτρέπει ταχύτατη ανάγνωση και αποκωδικοποίηση δεδομένων από ψηφιακούς αισθητήρες.",
    "funFacts": [
      "Εφευρέθηκε το 1994 από την ιαπωνική εταιρεία Denso Wave για την παρακολούθηση οχημάτων και εξαρτημάτων στη γραμμή συναρμολόγησης.",
      "Σε αντίθεση με τα κλασικά μονοδιάστατα barcodes, ο κώδικας QR μπορεί να αποθηκεύσει πάνω από 7.000 αριθμητικούς χαρακτήρες σε δισδιάστατη μορφή."
    ],
    "source": "https://el.wikipedia.org/wiki/QR_code",
    "locale": "el-GR",
    "tags": ["qrcode", "mobile", "standards", "barcodes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_025",
    "text": "Ποιοι δύο φοιτητές του Πανεπιστημίου Στάνφορντ ίδρυσαν τη μηχανή αναζήτησης Google το 1998;",
    "answers": ["Μπιλ Γκέιτς και Πολ Άλεν", "Στιβ Τζομπς και Στιβ Βόζνιακ", "Λάρι Πέιτζ και Σεργκέι Μπριν", "Ντέιβιντ Φίλο και Τζέρι Γιανγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Λάρι Πέιτζ και ο Σεργκέι Μπριν δημιούργησαν τη Google ως ερευνητικό πρόγραμμα στο Πανεπιστήμιο Στάνφορντ το 1996 και την ίδρυσαν επίσημα το 1998.",
    "funFacts": [
      "Το αρχικό όνομα της μηχανής αναζήτησης ήταν 'BackRub' επειδή ανέλυε τους συνδέσμους επιστροφής (backlinks) των ιστοσελίδων.",
      "Το όνομα Google προέρχεται από παράφραση της μαθηματικής λέξης 'googol', που αντιπροσωπεύει τον αριθμό 1 ακολουθούμενο από 100 μηδενικά."
    ],
    "source": "https://el.wikipedia.org/wiki/Google",
    "locale": "el-GR",
    "tags": ["google", "founders", "search", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_026",
    "text": "Ποια διάσημη πλατφόρμα κοινής χρήσης φωτογραφιών και βίντεο εξαγοράστηκε από την εταιρεία Facebook το 2012 έναντι περίπου 1 δισ. δολαρίων;",
    "answers": ["Snapchat", "Pinterest", "TikTok", "Instagram"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Instagram ιδρύθηκε το 2010 από τους Κέβιν Σίστρομ και Μάικ Κρίγκερ και εξαγοράστηκε από το Facebook τον Απρίλιο του 2012.",
    "funFacts": [
      "Κατά τη στιγμή της εξαγοράς του από το Facebook, το Instagram είχε μόλις 13 υπαλλήλους και καμία σταθερή πηγή εσόδων.",
      "Η πρώτη φωτογραφία που αναρτήθηκε ποτέ στο Instagram ήταν ένα αδέσποτο σκυλί σε ένα περίπτερο τάκος στο Μεξικό."
    ],
    "source": "https://el.wikipedia.org/wiki/Instagram",
    "locale": "el-GR",
    "tags": ["instagram", "meta", "social-media", "photography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_027",
    "text": "Ποιος τεχνολογικός όρος περιγράφει την αποθήκευση και επεξεργασία δεδομένων μέσω απομακρυσμένων διακομιστών στο διαδίκτυο;",
    "answers": ["Υπολογιστικό νέφος (Cloud computing)", "Εικονική πραγματικότητα (Virtual reality)", "Αλυσίδα συστοιχιών (Blockchain)", "Εξόρυξη δεδομένων (Data mining)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Cloud computing επιτρέπει στους χρήστες να αποθηκεύουν αρχεία και να εκτελούν εφαρμογές σε απομακρυσμένα κέντρα δεδομένων αντί στον τοπικό τους υπολογιστή.",
    "funFacts": [
      "Υπηρεσίες όπως το Google Drive, το iCloud, το Dropbox και το Microsoft OneDrive βασίζονται εξ ολοκλήρου στο cloud.",
      "Οι τρεις μεγαλύτεροι πάροχοι υποδομών cloud παγκοσμίως είναι η Amazon Web Services (AWS), η Microsoft Azure και η Google Cloud."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%B9%CE%BA%CF%8C_%CE%BD%CE%AD%CF%86%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["cloud", "storage", "internet", "infrastructure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_028",
    "text": "Ποια βασική συσκευή κατάδειξης και εισόδου εφευρέθηκε από τον Ντάγκλας Ένγκελμπαρτ τη δεκαετία του 1960 και αρχικά ήταν ξύλινη;",
    "answers": ["Πληκτρολόγιο", "Ποντίκι (Mouse)", "Χειριστήριο (Joystick)", "Οθόνη αφής"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Ντάγκλας Ένγκελμπαρτ παρουσίασε το πρώτο ποντίκι υπολογιστή το 1968, το οποίο διέθετε ξύλινο περίβλημα και δύο μεταλλικούς τροχούς κύλισης.",
    "funFacts": [
      "Ονομάστηκε 'ποντίκι' (mouse) επειδή το καλώδιο που έβγαινε από το πίσω μέρος του θύμιζε την ουρά του μικρού τρωκτικού.",
      "Η θρυλική παρουσίαση του Ένγκελμπαρτ το 1968, όπου παρουσίασε το ποντίκι, τα γραφικά παράθυρα και τους υπερσυνδέσμους, έμεινε στην ιστορία ως «Η Μητέρα Όλων των Επιδείξεων» (The Mother of All Demos)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BD%CF%84%CE%AF%CE%BA%CE%B9_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["mouse", "hardware", "input", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_029",
    "text": "Ποια εξαιρετικά διαδεδομένη γλώσσα προγραμματισμού, που δημιούργησε ο Γκίντο βαν Ρόσουμ, πήρε το όνομά της από τη βρετανική κωμική ομάδα Monty Python;",
    "answers": ["Ruby", "Perl", "Python", "Cobol"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Ολλανδός προγραμματιστής Γκίντο βαν Ρόσουμ δημιούργησε την Python το 1991, εμπνευσμένος από την αγαπημένη του τηλεοπτική σειρά Monty Python's Flying Circus.",
    "funFacts": [
      "Η Python σχεδιάστηκε με κύριο γνώμονα την αναγνωσιμότητα του κώδικα και τη σαφήνεια, χρησιμοποιώντας υποχρεωτική στοίχιση για τα μπλοκ εντολών.",
      "Σήμερα είναι η κυρίαρχη γλώσσα στον τομέα της επιστήμης δεδομένων (Data Science) και της μηχανικής μάθησης."
    ],
    "source": "https://el.wikipedia.org/wiki/Python",
    "locale": "el-GR",
    "tags": ["python", "programming", "languages", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_030",
    "text": "Τι σημαίνουν τα αρχικά «URL» που αποτελούν τη μοναδική διεύθυνση ενός πόρου ή ιστοσελίδας στο διαδίκτυο;",
    "answers": ["Universal Radio Link", "User Routing Line", "United Remote Location", "Uniform Resource Locator"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το URL (Uniform Resource Locator - Ενιαίος Εντοπιστής Πόρων) καθορίζει τη θέση ενός ψηφιακού πόρου στο διαδίκτυο και τον μηχανισμό ανάκτησής του.",
    "funFacts": [
      "Δημιουργήθηκε από τον Τιμ Μπέρνερς-Λι το 1994 ως μέρος του προτύπου ονοματοδοσίας Uniform Resource Identifier (URI).",
      "Μια τυπική δομή URL περιλαμβάνει το πρωτόκολλο (π.χ. https://), το όνομα τομέα (domain name) και τη διαδρομή του αρχείου (path)."
    ],
    "source": "https://el.wikipedia.org/wiki/URL",
    "locale": "el-GR",
    "tags": ["url", "web", "internet", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_031",
    "text": "Ποιο ήταν το αρχικό όριο χαρακτήρων για κάθε μήνυμα στην πλατφόρμα κοινωνικής δικτύωσης Twitter κατά την ίδρυσή της;",
    "answers": ["140 χαρακτήρες", "100 χαρακτήρες", "280 χαρακτήρες", "500 χαρακτήρες"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Twitter τέθηκε σε λειτουργία το 2006 με όριο 140 χαρακτήρων ανά tweet, ώστε τα μηνύματα να χωρούν σε ένα απλό γραπτό μήνυμα κινητού SMS (που είχε όριο 160 χαρακτήρες).",
    "funFacts": [
      "Το όριο των 140 χαρακτήρων διπλασιάστηκε σε 280 χαρακτήρες τον Νοέμβριο του 2017.",
      "Το πρώτο tweet στην ιστορία στάλθηκε από τον συνιδρυτή Τζακ Ντόρσεϊ στις 21 Μαρτίου 2006 και έγραφε: 'just setting up my twttr'."
    ],
    "source": "https://el.wikipedia.org/wiki/Twitter",
    "locale": "el-GR",
    "tags": ["twitter", "social-media", "internet", "communication"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_032",
    "text": "Ποιος τύπος οθόνης αφής χρησιμοποιείται σήμερα σχεδόν σε όλα τα σύγχρονα smartphones, αντιδρώντας στο ηλεκτρικό φορτίο των δακτύλων;",
    "answers": ["Αντιστατική οθόνη (Resistive)", "Χωρητική οθόνη (Capacitive)", "Υπέρυθρη οθόνη (Infrared)", "Ακουστική οθόνη (Surface Acoustic Wave)"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι χωρητικές οθόνες αφής (capacitive touchscreens) ανιχνεύουν την αλλαγή στο ηλεκτρικό πεδίο της επιφάνειας όταν την αγγίζει ένας αγωγός, όπως το ανθρώπινο δάχτυλο.",
    "funFacts": [
      "Σε αντίθεση με τις παλαιότερες αντιστατικές οθόνες που απαιτούσαν πίεση ή γραφίδα, οι χωρητικές οθόνες υποστηρίζουν φυσικό multi-touch (χειρονομίες με πολλαπλά δάχτυλα).",
      "Επειδή βασίζονται στην ηλεκτρική αγωγιμότητα, συνήθως δεν ανταποκρίνονται όταν ο χρήστης φορά κοινά υφασμάτινα γάντια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B8%CF%8C%CE%BD%CE%B7_%CE%B1%CF%86%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["touchscreen", "smartphones", "hardware", "display"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_033",
    "text": "Ποιο είναι το κυριότερο λειτουργικό πλεονέκτημα ενός δίσκου SSD (Solid State Drive) σε σύγκριση με έναν κλασικό σκληρό δίσκο HDD;",
    "answers": ["Διαθέτει μεγαλύτερους μαγνητικούς κυλίνδρους", "Χρησιμοποιεί οπτική κεφαλή λέιζερ", "Πολύ υψηλότερες ταχύτητες ανάγνωσης και εγγραφής", "Απαιτεί συνεχή ψύξη με υγρό"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι δίσκοι SSD χρησιμοποιούν ολοκληρωμένα κυκλώματα μνήμης flash χωρίς κινούμενα μηχανικά μέρη, επιτυγχάνοντας θεαματικά ταχύτερη μεταφορά δεδομένων και μηδενικό χρόνο αναζήτησης.",
    "funFacts": [
      "Επειδή δεν περιέχουν κινητά μέρη, οι δίσκοι SSD είναι εντελώς αθόρυβοι και εξαιρετικά ανθεκτικοί σε κραδασμούς και πτώσεις.",
      "Η κατανάλωση ενέργειας ενός SSD είναι σημαντικά χαμηλότερη, βελτιώνοντας σημαντικά την αυτονομία της μπαταρίας στους φορητούς υπολογιστές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CF%83%CF%84%CE%B5%CF%81%CE%B5%CE%AC%CF%82_%CE%BA%CE%B1%CF%84%CE%AC%CF%83%CF%84%CE%B1%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["ssd", "storage", "hardware", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_034",
    "text": "Ποιο είδος προϊόντων πουλούσε αποκλειστικά το ηλεκτρονικό κατάστημα της Amazon όταν ξεκίνησε τη λειτουργία του το 1994;",
    "answers": ["Ηλεκτρονικούς υπολογιστές", "Ρούχα και παπούτσια", "Παιχνίδια", "Βιβλία"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Τζεφ Μπέζος ίδρυσε την Amazon το 1994 αρχικά ως διαδικτυακό βιβλιοπωλείο, εκμεταλλευόμενος την τεράστια ποικιλία τίτλων που δεν μπορούσαν να φιλοξενήσουν τα φυσικά καταστήματα.",
    "funFacts": [
      "Το αρχικό όνομα που είχε κατοχυρώσει ο Μπέζος για την εταιρεία ήταν 'Cadabra' (από το abracadabra), αλλά το άλλαξε επειδή ακουγόταν σαν 'cadaver' (πτώμα).",
      "Το πρώτο βιβλίο που πωλήθηκε ποτέ στην πλατφόρμα ήταν μια επιστημονική μελέτη για την τεχνητή νοημοσύνη και τη ρευστοδυναμική."
    ],
    "source": "https://el.wikipedia.org/wiki/Amazon",
    "locale": "el-GR",
    "tags": ["amazon", "ecommerce", "internet", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_035",
    "text": "Πώς ονομάζεται η παγκοσμίως πιο διαδεδομένη διάταξη πλήκτρων στα λατινικά πληκτρολόγια γραφομηχανών και υπολογιστών;",
    "answers": ["QWERTY", "DVORAK", "AZERTY", "COLEMAK"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η διάταξη QWERTY πήρε το όνομά της από τα πρώτα έξι γράμματα στην επάνω αριστερή σειρά των πλήκτρων και κατοχυρώθηκε το 1878 από τον Κρίστοφερ Σολς.",
    "funFacts": [
      "Σχεδιάστηκε αρχικά για μηχανικές γραφομηχανές ώστε να αποτρέπει το μπλοκάρισμα των μεταλλικών μοχλών όταν πατιούνταν γρήγορα διαδοχικά σύμφωνα.",
      "Παρότι η διάταξη Dvorak σχεδιάστηκε αργότερα ειδικά για μεγαλύτερη ταχύτητα και εργονομία, το QWERTY παραμένει το αδιαφιλονίκητο πρότυπο λόγω συνήθειας."
    ],
    "source": "https://el.wikipedia.org/wiki/QWERTY",
    "locale": "el-GR",
    "tags": ["qwerty", "keyboard", "hardware", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_036",
    "text": "Ποιο δημοφιλές πρόγραμμα περιήγησης διαδικτύου (web browser) ανέπτυξε η Google και κυκλοφόρησε για πρώτη φορά το 2008;",
    "answers": ["Safari", "Google Chrome", "Mozilla Firefox", "Opera"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Google κυκλοφόρησε το Google Chrome τον Σεπτέμβριο του 2008, το οποίο βασίστηκε στο έργο ανοιχτού κώδικα Chromium.",
    "funFacts": [
      "Για να εξηγήσει στο κοινό πώς λειτουργεί το νέο πρόγραμμα, η Google κυκλοφόρησε ένα ψηφιακό κόμικ 38 σελίδων σχεδιασμένο από τον διάσημο δημιουργό Scott McCloud.",
      "Σήμερα το Chrome αποτελεί το δημοφιλέστερο πρόγραμμα περιήγησης στον κόσμο, διατηρώντας σταθερά μερίδιο αγοράς άνω του 60%."
    ],
    "source": "https://el.wikipedia.org/wiki/Google_Chrome",
    "locale": "el-GR",
    "tags": ["chrome", "google", "browsers", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_037",
    "text": "Ποιο εξάρτημα ενός υπολογιστή είναι ειδικά σχεδιασμένο για την ταχύτατη επεξεργασία γραφικών και τρισδιάστατων εικόνων;",
    "answers": ["Κάρτα δικτύου (NIC)", "Κάρτα ήχου", "Μονάδα Επεξεργασίας Γραφικών (GPU)", "Μονάδα τροφοδοσίας (PSU)"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η GPU (Graphics Processing Unit) διαθέτει χιλιάδες μικρούς πυρήνες σχεδιασμένους για μαζική παράλληλη επεξεργασία υπολογισμών που απαιτούνται στα γραφικά και τα βιντεοπαιχνίδια.",
    "funFacts": [
      "Ο όρος 'GPU' διαδόθηκε ευρέως από την εταιρεία Nvidia το 1999 με την κυκλοφορία της πρωτοποριακής κάρτας GeForce 256.",
      "Εκτός από τα βιντεοπαιχνίδια, οι σύγχρονες GPUs χρησιμοποιούνται εντατικά για την εκπαίδευση μοντέλων τεχνητής νοημοσύνης και την εξόρυξη κρυπτονομισμάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CE%B5%CF%80%CE%B5%CE%BE%CE%B5%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82_%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CF%8E%CE%BD",
    "locale": "el-GR",
    "tags": ["gpu", "hardware", "graphics", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_038",
    "text": "Ποια εταιρεία ξεκίνησε το 1997 αποστέλλοντας ενοικιαζόμενα DVD μέσω ταχυδρομείου πριν εξελιχθεί στον κολοσσό του online streaming σειρών και ταινιών;",
    "answers": ["Hulu", "Blockbuster", "Disney+", "Netflix"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Netflix ιδρύθηκε το 1997 από τους Ριντ Χέιστινγκς και Μαρκ Ράντολφ και εγκαινίασε την επαναστατική υπηρεσία online streaming το 2007.",
    "funFacts": [
      "Το έτος 2000 οι ιδρυτές του Netflix πρότειναν στην αλυσίδα Blockbuster να εξαγοράσει την εταιρεία τους έναντι 50 εκατομμυρίων δολαρίων, αλλά η πρόταση απορρίφθηκε περιπαικτικά.",
      "Η πρώτη πρωτότυπη σειρά παραγωγής του Netflix που γνώρισε τεράστια επιτυχία ήταν το πολιτικό δράμα 'House of Cards' το 2013."
    ],
    "source": "https://el.wikipedia.org/wiki/Netflix",
    "locale": "el-GR",
    "tags": ["netflix", "streaming", "entertainment", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_039",
    "text": "Πώς ονομάζεται το σύστημα ασφαλείας υπολογιστών και δικτύων που φιλτράρει και ελέγχει την εισερχόμενη και εξερχόμενη κυκλοφορία δεδομένων;",
    "answers": ["Τείχος προστασίας (Firewall)", "Πρόγραμμα περιήγησης (Browser)", "Ανιχνευτής θέσης (GPS)", "Μεταγλωττιστής (Compiler)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το τείχος προστασίας (firewall) λειτουργεί ως ψηφιακό φράγμα ανάμεσα σε ένα ασφαλές εσωτερικό δίκτυο και σε μη αξιόπιστα εξωτερικά δίκτυα όπως το διαδίκτυο.",
    "funFacts": [
      "Ο όρος δανείστηκε από την αρχιτεκτονική και την πυροπροστασία, όπου το τείχος πυρασφάλειας εμποδίζει την εξάπλωση πυρκαγιάς ανάμεσα σε κτήρια.",
      "Ένα τείχος προστασίας μπορεί να υλοποιηθεί είτε ως πρόγραμμα λογισμικού είτε ως αυτόνομη φυσική συσκευή υλικού (hardware appliance)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CE%AF%CF%87%CE%BF%CF%82_%CF%80%CF%81%CE%BF%CF%83%CF%84%CE%B1%CF%83%CE%AF%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["firewall", "security", "networking", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_040",
    "text": "Από ποιο σατιρικό σκετς της βρετανικής κωμικής ομάδας Monty Python προήλθε ο όρος «spam» για τα ανεπιθύμητα ηλεκτρονικά μηνύματα;",
    "answers": ["Το σκετς με τον νεκρό παπαγάλο", "Το σκετς με το κονσερβοποιημένο χοιρινό SPAM", "Το σκετς με το Υπουργείο Ανόητων Βηματισμών", "Το σκετς με τον Ισπανικό Ιεροεξεταστή"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στο διάσημο σκετς των Monty Python του 1970, όλοι οι χαρακτήρες επαναλάμβαναν επίμονα και ενοχλητικά τη λέξη 'SPAM' σε κάθε πιάτο του καταλόγου ενός καφενείου.",
    "funFacts": [
      "Το πραγματικό SPAM είναι δημοφιλές κονσερβοποιημένο μαγειρεμένο χοιρινό κρέας που παράγεται από την εταιρεία Hormel Foods από το 1937.",
      "Το πρώτο καταγεγραμμένο μαζικό ανεπιθύμητο εμπορικό email στάλθηκε το 1978 σε περίπου 400 χρήστες του πρώιμου δικτύου ARPANET."
    ],
    "source": "https://el.wikipedia.org/wiki/Spam",
    "locale": "el-GR",
    "tags": ["spam", "email", "internet", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_041",
    "text": "Πόσα Bytes αντιστοιχούν ακριβώς σε ένα παραδοσιακό Kilobyte (KB) σύμφωνα με το δυαδικό σύστημα μονάδων των υπολογιστών;",
    "answers": ["500 Bytes", "1.000 Bytes", "1.024 Bytes", "2.048 Bytes"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στο δυαδικό σύστημα των υπολογιστών (δυνάμεις του 2), ένα Kilobyte ισούται με 2^10 = 1.024 Bytes.",
    "funFacts": [
      "Η διεθνής επιτροπή IEC καθιέρωσε τον όρο 'Kibibyte' (KiB) για τα 1.024 Bytes ώστε να ξεχωρίζει από το δεκαδικό Kilobyte (1.000 Bytes).",
      "Λόγω της διαφοράς μεταξύ δεκαδικού και δυαδικού συστήματος, ένας σκληρός δίσκος 1 Terabyte φαίνεται στα Windows να έχει χωρητικότητα περίπου 931 Gigabytes."
    ],
    "source": "https://el.wikipedia.org/wiki/Kilobyte",
    "locale": "el-GR",
    "tags": ["kilobyte", "bytes", "storage", "units"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_042",
    "text": "Ποια εξαιρετικά δημοφιλής εφαρμογή ανταλλαγής άμεσων μηνυμάτων για smartphone εξαγοράστηκε από την εταιρεία Facebook το 2014 έναντι 19 δισ. δολαρίων;",
    "answers": ["Viber", "Telegram", "Signal", "WhatsApp"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το WhatsApp ιδρύθηκε το 2009 από τους πρώην εργαζομένους της Yahoo Γιαν Κουμ και Μπράιαν Άκτον και εξαγοράστηκε από το Facebook τον Φεβρουάριο του 2014.",
    "funFacts": [
      "Το όνομα WhatsApp προέρχεται από λογοπαίγνιο με την αγγλική έκφραση χαιρετισμού 'What's up?' (Τι νέα;).",
      "Όλα τα μηνύματα και οι κλήσεις στην πλατφόρμα προστατεύονται από άκρο-σε-άκρο κρυπτογράφηση (end-to-end encryption) βάσει του πρωτοκόλλου Signal."
    ],
    "source": "https://el.wikipedia.org/wiki/WhatsApp",
    "locale": "el-GR",
    "tags": ["whatsapp", "meta", "messaging", "mobile"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_043",
    "text": "Ποια σύγχρονη μέθοδος κατασκευής δημιουργεί φυσικά τρισδιάστατα αντικείμενα προσθέτοντας διαδοχικά στρώματα λιωμένου πλαστικού ή άλλου υλικού;",
    "answers": ["Τρισδιάστατη εκτύπωση (3D Printing)", "Υπερηχητική κοπή", "Χύτευση υπό πίεση", "Ηλεκτροστατική βαφή"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η τρισδιάστατη εκτύπωση (προσθετική κατασκευή) κατασκευάζει στερεά αντικείμενα απευθείας από ψηφιακά τρισδιάστατα μοντέλα CAD εναποθέτοντας διαδοχικές στρώσεις υλικού.",
    "funFacts": [
      "Η τεχνολογία κατοχυρώθηκε για πρώτη φορά το 1986 από τον Τσακ Χαλ με την εφεύρεση της στερεολιθογραφίας (SLA).",
      "Σήμερα η 3D εκτύπωση χρησιμοποιείται από την ιατρική για την παραγωγή ορθοπεδικών προθέσεων έως και την αεροδιαστημική για εξαρτήματα πυραύλων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%B9%CF%83%CE%B4%CE%B9%CE%AC%CF%83%CF%84%CE%B1%CF%84%CE%B7_%CE%B5%CE%BA%CF%84%CF%8D%CF%80%CF%89%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["3d-printing", "manufacturing", "hardware", "engineering"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_044",
    "text": "Ποιος κορυφαίος Βρετανός μαθηματικός θεωρείται «πατέρας της θεωρητικής επιστήμης υπολογιστών» και συνέβαλε καθοριστικά στο σπάσιμο του γερμανικού κώδικα Enigma;",
    "answers": ["Τζον φον Νόιμαν", "Άλαν Τιούρινγκ", "Τσαρλς Μπάμπατζ", "Άντα Λάβλεϊς"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Άλαν Τιούρινγκ (Alan Turing) διατύπωσε την έννοια της γενικής υπολογιστικής μηχανής («Μηχανή Τιούρινγκ») και ηγήθηκε της ομάδας αποκρυπτογράφησης στο Bletchley Park κατά τον Β' Παγκόσμιο Πόλεμο.",
    "funFacts": [
      "Επινόησε το περίφημο «Τεστ Τιούρινγκ» (Turing Test) το 1950 για να εξετάσει αν μια μηχανή μπορεί να επιδείξει ευφυή συμπεριφορά ισοδύναμη με την ανθρώπινη.",
      "Το Βραβείο Τιούρινγκ (Turing Award) απονέμεται ετησίως και θεωρείται το αντίστοιχο του Βραβείου Νόμπελ στον χώρο της επιστήμης των υπολογιστών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%B1%CE%BD_%CE%A4%CE%B9%CE%BF%CF%81%CE%B9%CE%BD%CE%B3%CE%BA",
    "locale": "el-GR",
    "tags": ["turing", "computer-science", "history", "cryptography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_045",
    "text": "Ποιο μέσο ενσύρματης μετάδοσης δεδομένων χρησιμοποιεί εξαιρετικά λεπτές ίνες γυαλιού και παλμούς φωτός για να επιτύχει τεράστιες ταχύτητες διαδικτύου;",
    "answers": ["Καλώδιο ομοαξονικό", "Καλώδιο χαλκού συνεστραμμένου ζεύγους", "Οπτικές ίνες (Fiber optics)", "Καλώδιο τροφοδοσίας"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι οπτικές ίνες μεταφέρουν ψηφιακά δεδομένα με τη μορφή φωτεινών κυμάτων μέσω λεπτών ινών καθαρού γυαλιού ή πλαστικού εκμεταλλευόμενες την ολική εσωτερική ανάκλαση.",
    "funFacts": [
      "Σε αντίθεση με τα καλώδια χαλκού, τα σήματα φωτός στις οπτικές ίνες έχουν μηδενική ευαισθησία σε ηλεκτρομαγνητικές παρεμβολές.",
      "Πάνω από το 95% της παγκόσμιας διηπειρωτικής κυκλοφορίας διαδικτύου μεταφέρεται μέσω υποθαλάσσιων καλωδίων οπτικών ινών στους ωκεανούς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CE%AF%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["fiber-optics", "networking", "telecommunications", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_046",
    "text": "Ποια φυσική γλώσσα ήταν η πρώτη στην οποία γράφτηκαν άρθρα κατά τα εγκαίνια της διαδικτυακής εγκυκλοπαίδειας Wikipedia το 2001;",
    "answers": ["Γαλλικά", "Γερμανικά", "Ισπανικά", "Αγγλικά"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Wikipedia ξεκίνησε επίσημα στις 15 Ιανουαρίου 2001 αποκλειστικά στην αγγλική γλώσσα, πριν επεκταθεί λίγους μήνες αργότερα σε δεκάδες άλλες γλώσσες.",
    "funFacts": [
      "Η ελληνική έκδοση της Βικιπαίδειας ξεκίνησε τη λειτουργία της τον Δεκέμβριο του 2002.",
      "Σήμερα η αγγλική Wikipedia περιέχει περισσότερα από 6,8 εκατομμύρια άρθρα, αποτελώντας τη μακράν μεγαλύτερη γλωσσική έκδοση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%BA%CE%B9%CF%80%CE%B1%CE%AF%CE%B4%CE%B5%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["wikipedia", "english", "encyclopedia", "web"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_047",
    "text": "Ποια είναι η επίσημη τεχνική ονομασία για τις ιπτάμενες τηλεκατευθυνόμενες συσκευές που αποκαλούνται ευρέως στην καθημερινότητα «drones»;",
    "answers": ["Μη επανδρωμένα αεροσκάφη (UAV)", "Αυτόνομα ρομποτικά υποβρύχια", "Ηλιακά υπερελαφρά αεροπλάνα", "Διαστημικοί δορυφόροι χαμηλής τροχιάς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Τα drones ονομάζονται επίσημα Μη Επανδρωμένα Αεροσκάφη (UAV - Unmanned Aerial Vehicles) επειδή πετούν χωρίς φυσικό χειριστή στο πιλοτήριο.",
    "funFacts": [
      "Η λέξη 'drone' σημαίνει κυριολεκτικά στα αγγλικά 'κηφήνας' (το αρσενικό της μέλισσας) λόγω του χαρακτηριστικού βουητού των ελίκων κατά την πτήση.",
      "Τα περισσότερα εμπορικά καταναλωτικά drones είναι τετρακόπτερα (quadcopters), χρησιμοποιώντας τέσσερις ανεξάρτητους ρότορες για σταθεροποίηση και πλοήγηση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B7_%CE%B5%CF%80%CE%B1%CE%BD%CE%B4%CF%81%CF%89%CE%BC%CE%AD%CE%BD%CE%BF_%CE%B1%CE%B5%CF%81%CE%BF%CF%83%CE%BA%CE%AC%CF%86%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["drones", "uav", "aviation", "robotics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_048",
    "text": "Ποια ιαπωνική πολυεθνική εταιρεία κυκλοφόρησε την πρώτη ιστορική οικιακή κονσόλα PlayStation το 1994;",
    "answers": ["Nintendo", "Sony", "Sega", "Bandai"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Sony κυκλοφόρησε την πρώτη κονσόλα PlayStation στην Ιαπωνία τον Δεκέμβριο του 1994, εισάγοντας οριστικά τα CD-ROM και τα 3D γραφικά στο ευρύ κοινό.",
    "funFacts": [
      "Το PlayStation γεννήθηκε αρχικά ως κοινό ερευνητικό πρόγραμμα της Sony με τη Nintendo για τη δημιουργία ενός οδηγού CD για το Super Nintendo (SNES).",
      "Έγινε η πρώτη κονσόλα στην ιστορία των βιντεοπαιχνιδιών που ξεπέρασε σε συνολικές πωλήσεις τα 100 εκατομμύρια τεμάχια."
    ],
    "source": "https://el.wikipedia.org/wiki/PlayStation",
    "locale": "el-GR",
    "tags": ["playstation", "sony", "gaming", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_049",
    "text": "Από ποιο αρχαίο σύστημα γραφής προέρχονται τα δύο γράμματα που συνδυάστηκαν για να δημιουργήσουν το λογότυπο του Bluetooth;",
    "answers": ["Αιγυπτιακά ιερογλυφικά", "Φοινικικό αλφάβητο", "Σκανδιναβικοί ρούνοι", "Ελληνική Γραμμική Β"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το λογότυπο του Bluetooth συνδυάζει τους δύο σκανδιναβικούς ρούνους Hagall (ᚼ) και Bjarkan (ᛒ), που αντιπροσωπεύουν τα αρχικά του βασιλιά Χάραλντ Μπλούτουθ (Harald Bluetooth).",
    "funFacts": [
      "Ο μηχανικός Σβεν Ματέισον της Ericsson και ο Τζιμ Κάρνταχ της Intel ήταν υπεύθυνοι για την επιλογή του ονόματος Bluetooth το 1997.",
      "Αρχικά το όνομα Bluetooth προοριζόταν μόνο ως προσωρινή κωδική ονομασία του έργου μέχρι να βρεθεί ένα επίσημο όνομα μάρκετινγκ, αλλά επικράτησε οριστικά."
    ],
    "source": "https://el.wikipedia.org/wiki/Bluetooth",
    "locale": "el-GR",
    "tags": ["bluetooth", "runes", "branding", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_050",
    "text": "Τι σημαίνουν τα αρχικά του βασικού δικτυακού πρωτοκόλλου «HTTP» που χρησιμοποιείται για τη μεταφορά ιστοσελίδων;",
    "answers": ["High Speed Transfer Technology", "Hybrid Terminal Telecom Protocol", "Hosting Text Translating Platform", "HyperText Transfer Protocol"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το HTTP (HyperText Transfer Protocol - Πρωτόκολλο Μεταφοράς Υπερκειμένου) καθορίζει τον τρόπο με τον οποίο διακομιστές και προγράμματα περιήγησης ανταλλάσσουν δεδομένα ιστού.",
    "funFacts": [
      "Η ασφαλής κρυπτογραφημένη παραλλαγή του πρωτοκόλλου ονομάζεται HTTPS, όπου το 'S' σημαίνει 'Secure' και προστατεύει την επικοινωνία με κρυπτογράφηση SSL/TLS.",
      "Σχεδιάστηκε από τον Τιμ Μπέρνερς-Λι το 1989 στο CERN ταυτόχρονα με την επινόηση του Παγκόσμιου Ιστού."
    ],
    "source": "https://el.wikipedia.org/wiki/HTTP",
    "locale": "el-GR",
    "tags": ["http", "web", "networking", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_051",
    "text": "Πώς ονομάζεται η κεντρική πλακέτα κυκλώματος ενός ηλεκτρονικού υπολογιστή πάνω στην οποία συνδέονται ο επεξεργαστής, η μνήμη και όλα τα περιφερειακά;",
    "answers": ["Μητρική πλακέτα (Motherboard)", "Κάρτα γραφικών", "Σκληρός δίσκος", "Τροφοδοτικό"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η μητρική πλακέτα (motherboard ή mainboard) αποτελεί τη ραχοκοκαλιά του υπολογιστή, παρέχοντας διαύλους επικοινωνίας και υποδοχές για όλα τα ζωτικά εξαρτήματα.",
    "funFacts": [
      "Φιλοξενεί το τσιπ BIOS/UEFI, το οποίο περιέχει το πρώτο λογισμικό χαμηλού επιπέδου που εκτελείται κατά την εκκίνηση του υπολογιστή.",
      "Οι μητρικές πλακέτες κατασκευάζονται σε τυποποιημένα μεγέθη (form factors), με πιο διαδεδομένα τα ATX, Micro-ATX και Mini-ITX."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B7%CF%84%CF%81%CE%B9%CE%BA%CE%AE_%CF%80%CE%BB%CE%B1%CE%BA%CE%AD%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["motherboard", "hardware", "computers", "components"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_052",
    "text": "Ποια πρωτοποριακή μορφή ψηφιακής συμπίεσης ήχου έφερε πραγματική επανάσταση στη διανομή και αναπαραγωγή μουσικής τη δεκαετία του 1990;",
    "answers": ["WAV", "MP3", "FLAC", "MIDI"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο μορφότυπος MP3 (MPEG Audio Layer III) επέτρεψε τη δραστική μείωση του μεγέθους ενός αρχείου ήχου κατά περίπου 90% με ανεπαίσθητη απώλεια ποιότητας.",
    "funFacts": [
      "Αναπτύχθηκε κυρίως στη Γερμανία από την ερευνητική ομάδα του Ινστιτούτου Fraunhofer με επικεφαλής τον Καρλχάιντς Μπράντενμπουργκ.",
      "Το τραγούδι 'Tom's Diner' της Σούζαν Βέγκα χρησιμοποιήθηκε ως βασικό μουσικό δείγμα αναφοράς για τη ρύθμιση του αλγορίθμου συμπίεσης του MP3."
    ],
    "source": "https://el.wikipedia.org/wiki/MP3",
    "locale": "el-GR",
    "tags": ["mp3", "audio", "compression", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_053",
    "text": "Πώς ονομάζονται τα μικρά αρχεία δεδομένων που αποθηκεύουν οι ιστότοποι στον περιηγητή μας για να θυμούνται τις προτιμήσεις και τις συνδέσεις μας;",
    "answers": ["Spam", "Trojans", "Cookies", "Firewalls"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Τα HTTP cookies (ή απλώς cookies) είναι μικρά κομμάτια κειμένου που αποστέλλονται από τον διακομιστή και αποθηκεύονται τοπικά στον υπολογιστή του χρήστη.",
    "funFacts": [
      "Εφευρέθηκαν το 1994 από τον Λου Μοντούλι, προγραμματιστή της εταιρείας Netscape Communications, για να αναγνωρίζονται οι χρήστες σε ηλεκτρονικά καταστήματα.",
      "Ο όρος 'cookie' προήλθε από την έννοια των 'magic cookies' στα λειτουργικά συστήματα Unix."
    ],
    "source": "https://el.wikipedia.org/wiki/Cookie_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["cookies", "web", "browsers", "privacy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_054",
    "text": "Ποιος ήταν ο μακροβιότερος ηγέτης και συνιδρυτής της Microsoft, ο οποίος υπήρξε επί δεκαετίες ένας από τους πλουσιότερους ανθρώπους στον κόσμο;",
    "answers": ["Στιβ Τζομπς", "Λάρι Έλισον", "Έλον Μασκ", "Μπιλ Γκέιτς"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Μπιλ Γκέιτς ίδρυσε τη Microsoft το 1975 μαζί με τον Πολ Άλεν και ηγήθηκε της εταιρείας ως διευθύνων σύμβουλος μέχρι το 2000.",
    "funFacts": [
      "Έγραψε το πρώτο του λογισμικό υπολογιστή σε ηλικία μόλις 13 ετών σε έναν υπολογιστή General Electric.",
      "Μαζί με την πρώην σύζυγό του ίδρυσε το Ίδρυμα Bill & Melinda Gates, έναν από τους μεγαλύτερους ιδιωτικούς φιλανθρωπικούς οργανισμούς παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B9%CE%BB_%CE%93%CE%BA%CE%AD%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["bill-gates", "microsoft", "founders", "personalities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_055",
    "text": "Από ποια ευρωπαϊκή χώρα ξεκίνησε η δημοφιλής πλατφόρμα ροής μουσικής (streaming) Spotify το 2006;",
    "answers": ["Σουηδία", "Γερμανία", "Νορβηγία", "Φινλανδία"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Spotify ιδρύθηκε στη Στοκχόλμη της Σουηδίας τον Απρίλιο του 2006 από τους Ντάνιελ Εκ και Μάρτιν Λόρεντζον.",
    "funFacts": [
      "Το όνομα 'Spotify' προήλθε από παρεξήγηση, όταν ο Ντάνιελ Εκ άκουσε λάθος μια πρόταση ονόματος που φώναξε ο Μάρτιν Λόρεντζον από άλλο δωμάτιο.",
      "Η σουηδική υπηρεσία άλλαξε δραστικά τη μουσική βιομηχανία προσφέροντας νόμιμη απεριόριστη μουσική μέσω διαφημίσεων ή μηνιαίας συνδρομής."
    ],
    "source": "https://el.wikipedia.org/wiki/Spotify",
    "locale": "el-GR",
    "tags": ["spotify", "streaming", "music", "sweden"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_056",
    "text": "Ποια δοκιμασία ασφαλείας ζητά από τον χρήστη να διαβάσει παραμορφωμένα γράμματα ή να αναγνωρίσει αντικείμενα για να επιβεβαιώσει ότι δεν είναι αυτοματοποιημένο ρομπότ;",
    "answers": ["Firewall", "CAPTCHA", "Benchmark", "BIOS"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το CAPTCHA είναι ένα αυτοματοποιημένο τεστ που ξεχωρίζει αν ο χρήστης μιας ιστοσελίδας είναι πραγματικός άνθρωπος ή αυτοματοποιημένο κακόβουλο πρόγραμμα (bot).",
    "funFacts": [
      "Τα αρχικά σημαίνουν: 'Completely Automated Public Turing test to tell Computers and Humans Apart' (Πλήρως Αυτοματοποιημένο Δημόσιο Τεστ Τιούρινγκ).",
      "Αναπτύχθηκε γύρω στο 2000 στο Πανεπιστήμιο Carnegie Mellon από τον Λούις φον Αν και την ομάδα του."
    ],
    "source": "https://el.wikipedia.org/wiki/CAPTCHA",
    "locale": "el-GR",
    "tags": ["captcha", "security", "web", "bots"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_057",
    "text": "Ποιο δημοφιλές καλώδιο και πρότυπο σύνδεσης μεταφέρει ταυτόχρονα ψηφιακή εικόνα υψηλής ευκρίνειας και πολυκάναλο ήχο από υπολογιστές σε οθόνες και τηλεοράσεις;",
    "answers": ["VGA", "DVI", "HDMI", "RCA"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρότυπο HDMI (High-Definition Multimedia Interface) σχεδιάστηκε το 2002 για τη μετάδοση ασυμπίεστων ψηφιακών δεδομένων βίντεο και ήχου σε μία ενιαία γραμμή.",
    "funFacts": [
      "Αντικατέστησε τα παλαιότερα αναλογικά πρότυπα όπως τα καλώδια SCART, VGA και RCA (τρίχρωμα βύσματα).",
      "Οι σύγχρονες εκδόσεις όπως το HDMI 2.1 υποστηρίζουν ανάλυση έως 8K και ρυθμό ανανέωσης 120Hz για προηγμένο gaming."
    ],
    "source": "https://el.wikipedia.org/wiki/HDMI",
    "locale": "el-GR",
    "tags": ["hdmi", "cables", "audio-video", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_058",
    "text": "Πώς ονομάζεται η ειδική λειτουργία των σύγχρονων προγραμμάτων περιήγησης κατά την οποία δεν καταγράφεται το ιστορικό και δεν αποθηκεύονται τοπικά cookies;",
    "answers": ["Ασφαλής εκκίνηση (Safe mode)", "Λειτουργία πτήσης (Airplane mode)", "Λειτουργία εξοικονόμησης ενέργειας", "Ανώνυμη περιήγηση (Incognito mode)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η ανώνυμη περιήγηση (γνωστή και ως Incognito ή Private Browsing) διαγράφει το ιστορικό περιήγησης, τα cookies και τα προσωρινά δεδομένα φόρμας μόλις κλείσει το παράθυρο.",
    "funFacts": [
      "Παρότι προστατεύει το απόρρητο από άλλους χρήστες της ίδιας συσκευής, δεν κρύβει τη δραστηριότητα από τον πάροχο διαδικτύου (ISP) ή τον διαχειριστή του δικτύου.",
      "Η πρώτη εταιρεία που ενσωμάτωσε λειτουργία ιδιωτικής περιήγησης σε πρόγραμμα περιήγησης ήταν η Apple στο Safari το 2005."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%B4%CE%B9%CF%89%CF%84%CE%B9%CE%BA%CE%AE_%CF%80%CE%B5%CF%81%CE%B9%CE%AE%CE%B3%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["incognito", "privacy", "browsers", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_059",
    "text": "Ποιος όρος περιγράφει ένα άτομο που χρησιμοποιεί εξειδικευμένες γνώσεις πληροφορικής για να αποκτήσει μη εξουσιοδοτημένη πρόσβαση σε υπολογιστικά συστήματα ή δίκτυα;",
    "answers": ["Χάκερ (Hacker)", "Blogger", "Webmaster", "Gamer"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στη σύγχρονη γλώσσα, ο όρος χάκερ (hacker) αναφέρεται συνήθως σε κάποιον που παραβιάζει συστήματα υπολογιστών και ασφάλειας, αν και αρχικά σήμαινε απλώς έναν ενθουσιώδη και ικανό προγραμματιστή.",
    "funFacts": [
      "Στην κυβερνοασφάλεια διακρίνονται σε 'White Hat' (ηθικοί χάκερς που βρίσκουν κενά για να τα διορθώσουν) και 'Black Hat' (κακόβουλοι εισβολείς).",
      "Ο όρος 'hack' ξεκίνησε τη δεκαετία του 1960 στη λέσχη σιδηροδρόμων του διάσημου αμερικανικού πανεπιστημίου MIT."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CE%BA%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["hacker", "cybersecurity", "computers", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_060",
    "text": "Πώς ονομάζεται η ενσωματωμένη φωνητική ψηφιακή βοηθός τεχνητής νοημοσύνης στις συσκευές της Apple (iPhone, iPad, Mac);",
    "answers": ["Alexa", "Siri", "Cortana", "Bixby"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Siri είναι η εφαρμογή εικονικού βοηθού της Apple που χρησιμοποιεί αναγνώριση φωνής και επεξεργασία φυσικής γλώσσας για να απαντά σε ερωτήσεις και να εκτελεί εντολές.",
    "funFacts": [
      "Παρουσιάστηκε για πρώτη φορά ενσωματωμένη στο iPhone 4S τον Οκτώβριο του 2011.",
      "Η λέξη Siri σημαίνει 'όμορφη γυναίκα που σε οδηγεί στη νίκη' στα παλαιά νορβηγικά."
    ],
    "source": "https://el.wikipedia.org/wiki/Siri",
    "locale": "el-GR",
    "tags": ["siri", "apple", "voice-assistant", "ai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'easy', 1, questions)

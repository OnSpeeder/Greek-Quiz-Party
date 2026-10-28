# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "tech_med_161",
    "text": "Ποια τεχνολογία δυαδικού κώδικα χαμηλού επιπέδου επιτρέπει σε γλώσσες όπως C++, Rust και C# να εκτελούνται μέσα στον περιηγητή ιστού με σχεδόν εγγενή ταχύτητα;",
    "answers": ["WebAssembly (Wasm)", "ActiveX", "Java Applets", "Adobe Flash"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το WebAssembly (Wasm) είναι ένα ανοιχτό διεθνές πρότυπο του W3C που προσφέρει ένα συμπαγές δυαδικό format για εκτέλεση κώδικα υψηλής απόδοσης στον ιστό.",
    "funFacts": [
      "Αναπτύχθηκε με κοινή συνεργασία μηχανικών από τις Mozilla, Google, Microsoft και Apple.",
      "Επιτρέπει σε βαριές εφαρμογές, όπως το Figma, η μηχανή Unreal Engine και το AutoCAD, να εκτελούνται ομαλά μέσα από μια απλή καρτέλα του browser."
    ],
    "source": "https://el.wikipedia.org/wiki/WebAssembly",
    "locale": "el-GR",
    "tags": ["webassembly", "wasm", "web-standards", "performance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_162",
    "text": "Ποια μηχανή εκτέλεσης JavaScript ανοιχτού κώδικα αναπτύχθηκε αρχικά από την Google για το Chrome και χρησιμοποιήθηκε αργότερα για τη δημιουργία του Node.js;",
    "answers": ["SpiderMonkey", "V8", "JavaScriptCore", "Chakra"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μηχανή V8 μεταγλωττίζει απευθείας τη JavaScript σε εγγενή κώδικα μηχανής πριν την εκτέλεσή της, προσφέροντας πρωτοφανείς ταχύτητες εκτέλεσης.",
    "funFacts": [
      "Σχεδιάστηκε από τον Δανό μηχανικό Λαρς Μπακ, ο οποίος είχε προηγουμένως εργαστεί στην εικονική μηχανή HotSpot της Java.",
      "Το όνομα V8 εμπνεύστηκε από τους ισχυρούς οκτακύλινδρους κινητήρες αυτοκινήτων V8."
    ],
    "source": "https://el.wikipedia.org/wiki/V8_(%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE_JavaScript)",
    "locale": "el-GR",
    "tags": ["v8", "javascript", "google-chrome", "compilers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_163",
    "text": "Ποιος Αμερικανός μηχανικός λογισμικού δημιούργησε το περιβάλλον εκτέλεσης Node.js το 2009, φέρνοντας την JavaScript από τον περιηγητή στην πλευρά του διακομιστή;",
    "answers": ["Μπρένταν Άιχ", "Ντάγκλας Κρόκφορντ", "Ράιαν Νταλ", "Τζον Ρέσιγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ράιαν Νταλ (Ryan Dahl) συνδύασε τη μηχανή V8 της Google με έναν ασύγχρονο βρόχο γεγονότων (event loop), δημιουργώντας μια εξαιρετικά γρήγορη πλατφόρμα διακομιστή.",
    "funFacts": [
      "Εμπνεύστηκε τη δημιουργία του Node.js όταν παρατήρησε μια μπάρα προόδου μεταφόρτωσης αρχείων στο Flickr που δεν ήξερε πόσο είχε προχωρήσει η αποστολή επειδή ο διακομιστής μπλόκαρε τις συνδέσεις.",
      "Χρόνια αργότερα, ο Νταλ δημιούργησε το Deno (αναγραμματισμός του Node), ένα νεότερο περιβάλλον εκτέλεσης γραμμένο σε Rust που διορθώνει αρχιτεκτονικά λάθη του Node.js."
    ],
    "source": "https://el.wikipedia.org/wiki/Node.js",
    "locale": "el-GR",
    "tags": ["nodejs", "ryan-dahl", "javascript", "backend"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_164",
    "text": "Ποιος μηχανικός λογισμικού του Facebook δημιούργησε την εξαιρετικά δημοφιλή δηλωτική βιβλιοθήκη διεπαφών χρήστη React (React.js) το 2011;",
    "answers": ["Μαρκ Ζάκερμπεργκ", "Έβαν Γιου", "Μπρετ Βίκτορ", "Τζόρνταν Γουόκ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζόρνταν Γουόκ (Jordan Walke) ανέπτυξε το αρχικό πρωτότυπο του React (εμπνευσμένο από το XHP) για τη ροή ειδήσεων του Facebook και αργότερα για το Instagram.",
    "funFacts": [
      "Το React εισήγαγε την έννοια του Virtual DOM (Εικονικό DOM), συγκρίνοντας διαφορές στη μνήμη πριν κάνει ελάχιστες τροποποιήσεις στην πραγματική ιστοσελίδα.",
      "Διατέθηκε ως λογισμικό ανοιχτού κώδικα στο συνέδριο JSConf US το 2013 και έγινε η πιο διαδεδομένη βιβλιοθήκη frontend στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/React",
    "locale": "el-GR",
    "tags": ["react", "frontend", "javascript", "facebook"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_165",
    "text": "Ποιος πρώην μηχανικός της Google δημιούργησε το ευρέως διαδεδομένο προοδευτικό διαδικτυακό πλαίσιο Vue.js το 2014;",
    "answers": ["Έβαν Γιου", "Μίκο Χέβερι", "Τζόρνταν Γουόκ", "Νταν Αμπράμοφ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Έβαν Γιου (Evan You) δημιούργησε το Vue.js κρατώντας τα καλύτερα στοιχεία από το Angular (όπως τη σύνδεση δεδομένων) σε μια πολύ πιο ελαφριά και προσιτή δομή.",
    "funFacts": [
      "Σε αντίθεση με το React (Facebook) και το Angular (Google), το Vue.js είναι ένα ανεξάρτητο έργο που χρηματοδοτείται αποκλειστικά από χορηγίες της κοινότητας και crowdfunding.",
      "Ο Έβαν Γιου δημιούργησε επίσης το Vite, ένα εξαιρετικά γρήγορο εργαλείο ανάπτυξης frontend βασισμένο σε εγγενή ES modules."
    ],
    "source": "https://el.wikipedia.org/wiki/Vue.js",
    "locale": "el-GR",
    "tags": ["vuejs", "frontend", "javascript", "open-source"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_166",
    "text": "Ποιος Ρώσος μηχανικός λογισμικού συν-δημιούργησε τη διάσημη βιβλιοθήκη διαχείρισης κατάστασης Redux για εφαρμογές JavaScript το 2015;",
    "answers": ["Πάβελ Ντούροφ", "Νταν Αμπράμοφ", "Αντρέι Μπρέσλαβ", "Εβγκένι Κασπέρσκι"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Νταν Αμπράμοφ (Dan Abramov) μαζί με τον Άντριου Κλαρκ δημιούργησαν το Redux για μια παρουσίαση συνεδρίου, βασισμένοι στην αρχιτεκτονική Flux και τη γλώσσα Elm.",
    "funFacts": [
      "Το Redux βασίζεται σε τρεις θεμελιώδεις αρχές: μία μοναδική πηγή αλήθειας (single source of truth), κατάσταση μόνο για ανάγνωση και καθαρές συναρτήσεις reducers.",
      "Εντάχθηκε αμέσως μετά στην ομάδα ανάπτυξης του React στη Meta, γράφοντας εκτενή τεκμηρίωση και εκπαιδευτικά εργαλεία."
    ],
    "source": "https://el.wikipedia.org/wiki/React",
    "locale": "el-GR",
    "tags": ["redux", "abramov", "javascript", "state-management"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_167",
    "text": "Ποιοι δύο μηχανικοί ίδρυσαν αρχικά την εταιρεία Tesla Motors το 2003 πριν ενταχθεί ο Έλον Μασκ ως ο κύριος επενδυτής χρηματοδότησης;",
    "answers": ["Τζ. Μπ. Στρόμπελ και Ίαν Ράιτ", "Πίτερ Τιλ και Μαξ Λέβτσιν", "Μάρτιν Έμπερχαρντ και Μαρκ Τάρπενινγκ", "Μπιλ Χιούλετ και Ντέιβιντ Πάκαρντ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μάρτιν Έμπερχαρντ και ο Μαρκ Τάρπενινγκ ίδρυσαν την Tesla Motors τον Ιούλιο του 2003, ονομάζοντάς την προς τιμήν του εφευρέτη Νίκολα Τέσλα.",
    "funFacts": [
      "Ο Έλον Μασκ ηγήθηκε του πρώτου μεγάλου γύρου χρηματοδότησης (Series A) το 2004 συνεισφέροντας 6,5 εκατομμύρια δολάρια και αναλαμβάνοντας πρόεδρος του διοικητικού συμβουλίου.",
      "Μετά από δικαστικό συμβιβασμό το 2009, αναγνωρίστηκαν επίσημα πέντε άτομα ως συνιδρυτές της Tesla, συμπεριλαμβανομένων των Μασκ, Έμπερχαρντ και Τάρπενινγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/Tesla_(%CE%B5%CF%84%CE%B1%CE%B9%CF%81%CE%B5%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["tesla", "founders", "automotive", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_168",
    "text": "Ποιος πρωτοπόρος μηχανικός διετέλεσε επί 15 χρόνια επικεφαλής τεχνολογίας (CTO) της Tesla, όντας ο κύριος αρχιτέκτονας των συστημάτων μπαταριών και ηλεκτροκίνησης;",
    "answers": ["Φραντς φον Χολτσχάουζεν", "Άντριου Καρπάθι", "Τζιμ Κέλερ", "Τζ. Μπ. Στρόμπελ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζ. Μπ. Στρόμπελ (JB Straubel) ήταν ο τεχνικός εγκέφαλος πίσω από την αρχιτεκτονική μπαταριών των Roadster, Model S, Model X, Model 3 και των Gigafactories.",
    "funFacts": [
      "Αποχώρησε από την Tesla το 2019 για να ιδρύσει τη Redwood Materials, μια κορυφαία εταιρεία ανακύκλωσης μπαταριών λιθίου.",
      "Επανεντάχθηκε στο διοικητικό συμβούλιο της Tesla το 2023 ως ανεξάρτητο μέλος."
    ],
    "source": "https://el.wikipedia.org/wiki/Tesla_(%CE%B5%CF%84%CE%B1%CE%B9%CF%81%CE%B5%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["straubel", "tesla", "batteries", "engineering"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_169",
    "text": "Τι αντικαθιστά τον εύφλεκτο υγρό ηλεκτρολύτη στις πειραματικές μπαταρίες στερεάς κατάστασης (solid-state batteries) για ασφάλεια και μεγαλύτερη πυκνότητα;",
    "answers": ["Στερεό κεραμικό, γυάλινο ή πολυμερικό υλικό", "Πεπιεσμένο αέριο υδρογόνο", "Υγρό υδράργυρο", "Απιονισμένο νερό"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι μπαταρίες στερεάς κατάστασης χρησιμοποιούν στερεό ηλεκτρολύτη, εξαλείφοντας τον κίνδυνο διαρροής ή πυρκαγιάς και επιτρέποντας πολύ ταχύτερη φόρτιση.",
    "funFacts": [
      "Μπορούν να προσφέρουν έως και διπλάσια ενεργειακή πυκνότητα ανά όγκο σε σύγκριση με τις συμβατικές μπαταρίες ιόντων λιθίου.",
      "Η μεγαλύτερη κατασκευαστική πρόκληση παραμένει η αποφυγή σχηματισμού δενδριτών λιθίου (μικροσκοπικών μεταλλικών ινών) που μπορεί να βραχυκυκλώσουν τα ηλεκτρόδια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97%CE%BB%CE%B5%CE%BA%CF%84%CF%81%CE%B9%CE%BA%CF%8C%CF%82_%CF%83%CF%85%CF%83%CF%83%CF%89%CF%81%CE%B5%CF%85%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["solid-state", "batteries", "energy", "materials-science"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_170",
    "text": "Ποιος κορυφαίος επιστήμονας τιμήθηκε με το Νόμπελ Χημείας το 2019 σε ηλικία 97 ετών (ο γηραιότερος νομπελίστας στην ιστορία) για την εφεύρεση της καθόδου της μπαταρίας ιόντων λιθίου;",
    "answers": ["Μ. Στάνλεϊ Γουίτινγχαμ", "Τζον Μπ. Γκούντιναφ", "Ακίρα Γιοσίνο", "Ρίτσαρντ Σμάλεϊ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζον Μπ. Γκούντιναφ (John B. Goodenough) ανέπτυξε το 1980 στο Πανεπιστήμιο της Οξφόρδης την κάθοδο οξειδίου κοβαλτίου-λιθίου (LiCoO2), διπλασιάζοντας την τάση της μπαταρίας στα 4 Volts.",
    "funFacts": [
      "Μοιράστηκε το Νόμπελ Χημείας 2019 με τους Στάνλεϊ Γουίτινγχαμ και Ακίρα Γιοσίνο για την ανάπτυξη της μπαταρίας ιόντων λιθίου που άλλαξε τον σύγχρονο κόσμο.",
      "Συνέχισε την ενεργό επιστημονική του έρευνα πάνω σε νέες μπαταρίες στερεάς κατάστασης μέχρι τα 100 του χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%9C%CF%80._%CE%93%CE%BA%CE%BF%CF%8D%CE%BD%CF%84%CE%B9%CE%BD%CE%B1%CF%86",
    "locale": "el-GR",
    "tags": ["goodenough", "batteries", "nobel", "chemistry"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_171",
    "text": "Ποια σύγχρονη προδιαγραφή φυσικής υποδοχής και μεγέθους καρτών επέκτασης (γνωστή αρχικά ως NGFF) χρησιμοποιείται ευρέως για γρήγορους δίσκους SSD σε μητρικές και λάπτοπ;",
    "answers": ["mSATA", "Mini PCIe", "Υποδοχή M.2", "ExpressCard"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρότυπο M.2 (Next Generation Form Factor) προσφέρει εξαιρετικά μικρό μέγεθος και υποστηρίζει πολλαπλά πρωτόκολλα (PCIe NVMe, SATA, USB).",
    "funFacts": [
      "Τα μεγέθη των καρτών M.2 κωδικοποιούνται με τετραψήφιο αριθμό, όπου το '2280' σημαίνει πλάτος 22 χιλιοστά και μήκος 80 χιλιοστά.",
      "Χρησιμοποιεί διαφορετικές εγκοπές κλειδώματος (keys), με το B key και το M key να καθορίζουν τον αριθμό των υποστηριζόμενων γραμμών PCIe."
    ],
    "source": "https://el.wikipedia.org/wiki/M.2",
    "locale": "el-GR",
    "tags": ["m2", "ssd", "hardware", "motherboards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_172",
    "text": "Πόσες ανεξάρτητες γραμμές διαύλου (lanes) PCIe χρησιμοποιούν παραδοσιακά οι σύγχρονες αυτόνομες κάρτες γραφικών στην πλήρη υποδοχή της μητρικής πλακέτας;",
    "answers": ["x1", "x4", "x8", "x16"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η τυπική υποδοχή κάρτας γραφικών είναι η PCIe x16, η οποία περιλαμβάνει 16 αμφίδρομες σειριακές γραμμές για μέγιστη διαμεταγωγή δεδομένων.",
    "funFacts": [
      "Στο πρότυπο PCIe 4.0, μια υποδοχή x16 προσφέρει θεωρητική ταχύτητα περίπου 32 GB/s, ενώ στο PCIe 5.0 φτάνει τα εντυπωσιακά 64 GB/s.",
      "Κάθε γραμμή PCIe (lane) αποτελείται από δύο διαφορικά ζεύγη καλωδίων: ένα για αποστολή και ένα για λήψη δεδομένων."
    ],
    "source": "https://el.wikipedia.org/wiki/PCI_Express",
    "locale": "el-GR",
    "tags": ["pcie", "gpu", "hardware", "motherboards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_173",
    "text": "Ποιες δύο τεχνολογικές εταιρείες συνεργάστηκαν αρχικά για την ανάπτυξη της διεπαφής διασύνδεσης υψηλής ταχύτητας Thunderbolt (κωδική ονομασία Light Peak);",
    "answers": ["Intel και Apple", "Microsoft και Sony", "IBM και AMD", "HP και Compaq"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Intel ανέπτυξε την υποκείμενη τεχνολογία και η Apple την πρωτοπαρουσίασε εμπορικά στη γραμμή MacBook Pro το 2011.",
    "funFacts": [
      "Αρχικά σχεδιάστηκε για χρήση οπτικών ινών (Light Peak), αλλά τελικά υιοθετήθηκαν χάλκινα καλώδια για μείωση του κόστους και παροχή ταυτόχρονης τροφοδοσίας ρεύματος.",
      "Το πρότυπο Thunderbolt 3 και 4 υιοθέτησε το φυσικό βύσμα USB Type-C, ενσωματώνοντας πρωτόκολλα PCIe και DisplayPort."
    ],
    "source": "https://el.wikipedia.org/wiki/Thunderbolt",
    "locale": "el-GR",
    "tags": ["thunderbolt", "intel", "apple", "cables"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_174",
    "text": "Ποιο πρότυπο σειριακού διαύλου υψηλής ταχύτητας (IEEE 1394) ανέπτυξε η Apple στα τέλη της δεκαετίας του 1980 για ψηφιακές κάμερες και εξωτερικούς δίσκους;",
    "answers": ["Lightning", "FireWire", "SCSI", "ADB"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το FireWire (IEEE 1394) προσέφερε σταθερές ταχύτητες 400 και αργότερα 800 Mbps, όντας ιδανικό για επεξεργασία ψηφιακού βίντεο DV.",
    "funFacts": [
      "Η Sony χρησιμοποίησε το ίδιο πρότυπο στις βιντεοκάμερες και στο PlayStation 2 υπό την εμπορική ονομασία 'i.LINK'.",
      "Σε αντίθεση με το αρχικό USB που απαιτούσε κεντρικό υπολογιστή (host), το FireWire υποστήριζε απευθείας επικοινωνία συσκευής προς συσκευή (peer-to-peer)."
    ],
    "source": "https://el.wikipedia.org/wiki/IEEE_1394",
    "locale": "el-GR",
    "tags": ["firewire", "apple", "ieee-1394", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_175",
    "text": "Ποιο ιστορικό πρότυπο παράλληλης διασύνδεσης (Small Computer System Interface) χρησιμοποιήθηκε ευρέως σε διακομιστές και επαγγελματικά PC τη δεκαετία του 1990;",
    "answers": ["IDE", "ESDI", "SCSI", "ST-506"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρότυπο SCSI (προφέρεται 'σκάζι') επέτρεπε τη σύνδεση πολλαπλών περιφερειακών (σκληροί δίσκοι, σαρωτές, ταινίες) σε σειρά (daisy chain) με τερματισμό.",
    "funFacts": [
      "Κάθε συσκευή στην αλυσίδα SCSI έπρεπε να έχει έναν μοναδικό αριθμό ταυτότητας (SCSI ID) που ρυθμιζόταν συχνά με φυσικούς διακόπτες.",
      "Η σύγχρονη εξέλιξή του σε σειριακή μορφή ονομάζεται SAS (Serial Attached SCSI) και χρησιμοποιείται σε εταιρικούς διακομιστές."
    ],
    "source": "https://el.wikipedia.org/wiki/SCSI",
    "locale": "el-GR",
    "tags": ["scsi", "storage", "hardware", "servers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_176",
    "text": "Ποια είναι η μέγιστη θεωρητική ταχύτητα διαμεταγωγής δεδομένων του διαύλου SATA Revision 3.0 (SATA 6Gb/s);",
    "answers": ["1,5 Gbps (περίπου 150 MB/s)", "3 Gbps (περίπου 300 MB/s)", "10 Gbps (περίπου 1 GB/s)", "6 Gbps (περίπου 600 MB/s)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρότυπο SATA 3.0 λειτουργεί στα 6 Gigabits/s και λόγω της κωδικοποίησης 8b/10b έχει μέγιστο θεωρητικό ρυθμό δεδομένων περίπου 600 Megabytes ανά δευτερόλεπτο.",
    "funFacts": [
      "Αυτό το όριο των 600 MB/s αποτέλεσε το λεγόμενο 'SATA bottleneck' που ανάγκασε τη βιομηχανία να στραφεί στο NVMe και στο PCIe για ταχύτερους SSDs.",
      "Αντικατέστησε το παλιό πρότυπο PATA (Parallel ATA) που χρησιμοποιούσε φαρδιές γκρι ταινίες 40 ή 80 αγωγών."
    ],
    "source": "https://el.wikipedia.org/wiki/Serial_ATA",
    "locale": "el-GR",
    "tags": ["sata", "storage", "hardware", "cables"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_177",
    "text": "Ποιος είναι ο ελάχιστος αριθμός φυσικών δίσκων που απαιτούνται για τη δημιουργία μιας διάταξης RAID 5 με κατανεμημένη ισοτιμία (distributed parity);",
    "answers": ["3 δίσκοι", "2 δίσκοι", "4 δίσκοι", "5 δίσκοι"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το RAID 5 απαιτεί τουλάχιστον 3 δίσκους και κατανέμει τα δεδομένα και τα δεδομένα ισοτιμίας σε όλους τους δίσκους, αντέχοντας την απώλεια ενός δίσκου.",
    "funFacts": [
      "Η διαθέσιμη χωρητικότητα ισούται με (N - 1) φορές τη χωρητικότητα του μικρότερου δίσκου, όπου N είναι ο αριθμός των δίσκων.",
      "Αν καταρρεύσει ένας δίσκος, το σύστημα συνεχίζει να λειτουργεί σε κατάσταση υποβάθμισης (degraded mode) υπολογίζοντας τα χαμένα δεδομένα μέσω πράξεων XOR."
    ],
    "source": "https://el.wikipedia.org/wiki/RAID",
    "locale": "el-GR",
    "tags": ["raid5", "storage", "redundancy", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_178",
    "text": "Ποιος συνδυασμός επιπέδων RAID συνθέτει τη διάταξη RAID 10 (ή RAID 1+0), προσφέροντας ταυτόχρονα υψηλές επιδόσεις και ισχυρή ανοχή σφαλμάτων;",
    "answers": ["RAID 5 και RAID 0", "Μοίρασμα λωρίδων (RAID 0) πάνω από καθρεπτισμένα ζεύγη (RAID 1)", "RAID 1 και RAID 5", "Δύο διατάξεις JBOD"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το RAID 10 δημιουργεί ζεύγη καθρεπτισμού (mirroring - RAID 1) και στη συνέχεια μοιράζει τα δεδομένα σε λωρίδες (striping - RAID 0) πάνω από αυτά, απαιτώντας τουλάχιστον 4 δίσκους.",
    "funFacts": [
      "Προσφέρει πολύ ταχύτερους χρόνους ανοικοδόμησης (rebuild) σε σχέση με το RAID 5/6 επειδή δεν απαιτεί πολύπλοκους υπολογισμούς ισοτιμίας.",
      "Μπορεί να επιβιώσει από την ταυτόχρονη απώλεια πολλαπλών δίσκων, αρκεί να μην καταρρεύσουν και οι δύο δίσκοι του ίδιου καθρεπτισμένου ζεύγους."
    ],
    "source": "https://el.wikipedia.org/wiki/RAID",
    "locale": "el-GR",
    "tags": ["raid10", "storage", "redundancy", "performance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_179",
    "text": "Πώς ονομάζεται μια εξειδικευμένη αυτόνομη συσκευή αποθήκευσης που συνδέεται απευθείας σε τοπικό δίκτυο παρέχοντας κοινή πρόσβαση σε αρχεία (file-level storage);",
    "answers": ["DAS (Direct Attached Storage)", "SAN (Storage Area Network)", "NAS (Network Attached Storage)", "RAM Disk"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το NAS είναι ένας μικρός εξειδικευμένος διακομιστής αρχείων με δικό του λειτουργικό σύστημα (συχνά Linux) που μοιράζει αρχεία μέσω πρωτοκόλλων NFS ή SMB/CIFS.",
    "funFacts": [
      "Εταιρείες όπως η Synology και η QNAP κατασκευάζουν δημοφιλείς οικιακές συσκευές NAS με θήκες για πολλαπλούς δίσκους hot-swap.",
      "Εκτός από αποθήκευση αρχείων, τα σύγχρονα NAS εκτελούν εφαρμογές πολυμέσων (Plex), αυτοματισμούς λήψεων και αυτόματα αντίγραφα ασφαλείας."
    ],
    "source": "https://el.wikipedia.org/wiki/Network_attached_storage",
    "locale": "el-GR",
    "tags": ["nas", "storage", "networking", "servers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_180",
    "text": "Ποιο εξειδικευμένο δίκτυο αποθήκευσης υψηλής ταχύτητας συνδέει διακομιστές με απομακρυσμένες συστοιχίες δίσκων σε επίπεδο μπλοκ (block-level storage);",
    "answers": ["LAN", "WAN", "PAN", "SAN (Storage Area Network)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ένα SAN (Δίκτυο Αποθηκευτικού Χώρου) εμφανίζει τις απομακρυσμένες συστοιχίες αποθήκευσης στον διακομιστή σαν να ήταν τοπικά προσαρτημένοι σκληροί δίσκοι.",
    "funFacts": [
      "Χρησιμοποιεί παραδοσιακά δίκτυα οπτικών ινών Fibre Channel ή πρωτόκολλο iSCSI πάνω από Ethernet.",
      "Είναι το βασικό πρότυπο αποθήκευσης σε μεγάλα εταιρικά data centers και τραπεζικά υπολογιστικά κέντρα."
    ],
    "source": "https://el.wikipedia.org/wiki/Storage_area_network",
    "locale": "el-GR",
    "tags": ["san", "storage", "enterprise", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_181",
    "text": "Ποιο πρωτόκολλο δικτύωσης μεταφέρει εντολές αποθήκευσης SCSI πάνω από παραδοσιακά δίκτυα IP/Ethernet, επιτρέποντας φθηνότερα δίκτυα SAN;",
    "answers": ["iSCSI", "FCoE", "NFS", "SMB"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το iSCSI (Internet Small Computer System Interface) ενσωματώνει εντολές SCSI σε πακέτα TCP/IP, επιτρέποντας τη δημιουργία δικτύων SAN χωρίς ακριβό εξοπλισμό Fibre Channel.",
    "funFacts": [
      "Ορίστηκε από τον οργανισμό IETF το 2003 στο RFC 3720.",
      "Ο υπολογιστής-πελάτης που ζητά πρόσβαση ονομάζεται 'iSCSI Initiator', ενώ η συσκευή αποθήκευσης ονομάζεται 'iSCSI Target'."
    ],
    "source": "https://el.wikipedia.org/wiki/ISCSI",
    "locale": "el-GR",
    "tags": ["iscsi", "storage", "networking", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_182",
    "text": "Ποια τεχνολογία σειριακού δικτύου οπτικών ινών υψηλής ταχύτητας (συνήθως 16, 32 ή 64 Gbps) αποτελεί το κυρίαρχο πρότυπο για εταιρικά δίκτυα SAN;",
    "answers": ["InfiniBand", "Fibre Channel", "FDDI", "Token Ring"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Fibre Channel (FC) σχεδιάστηκε ειδικά για τη μεταφορά δεδομένων αποθήκευσης χωρίς απώλειες πακέτων και με εξαιρετικά χαμηλή υστέρηση.",
    "funFacts": [
      "Χρησιμοποιεί εξειδικευμένους διακόπτες (FC switches) και προσαρμογείς διαύλου κεντρικού υπολογιστή (HBAs - Host Bus Adapters).",
      "Η λέξη 'Fibre' γράφεται παραδοσιακά με τη βρετανική ορθογραφία επειδή υποστηρίζει τόσο οπτικές ίνες όσο και χάλκινα ομοαξονικά καλώδια."
    ],
    "source": "https://el.wikipedia.org/wiki/Fibre_Channel",
    "locale": "el-GR",
    "tags": ["fibre-channel", "san", "storage", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_183",
    "text": "Ποιος κλασικός αλγόριθμος συμπίεσης χωρίς απώλειες που δημοσίευσαν το 1977 οι Αβραάμ Λέμπελ και Γιάκομπ Ζιβ αποτελεί τη βάση των ZIP, GZIP και PNG;",
    "answers": ["Huffman", "Run-Length Encoding", "LZ77", "BWT"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο LZ77 χρησιμοποιεί ένα 'συρόμενο παράθυρο' (sliding window) για να αντικαθιστά επαναλαμβανόμενες ακολουθίες δεδομένων με αναφορές σε προηγούμενες εμφανίσεις τους.",
    "funFacts": [
      "Μαζί με τον διάδοχό του LZ78 και την παραλλαγή LZW (που χρησιμοποιήθηκε στο GIF), οι αλγόριθμοι Lempel-Ziv θεμελίωσαν τη σύγχρονη ψηφιακή συμπίεση.",
      "Ο συνδυασμός του LZ77 με την κωδικοποίηση Huffman δημιούργησε τον εξαιρετικά δημοφιλή αλγόριθμο DEFLATE."
    ],
    "source": "https://el.wikipedia.org/wiki/LZ77_%CE%BA%CE%B1%CE%B9_LZ78",
    "locale": "el-GR",
    "tags": ["lz77", "compression", "algorithms", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_184",
    "text": "Ποια μέθοδος εντροπικής συμπίεσης που ανέπτυξε ο Ντέιβιντ Χάφμαν το 1952 αναθέτει συντομότερους δυαδικούς κωδικούς στα σύμβολα που εμφανίζονται συχνότερα;",
    "answers": ["Αριθμητική κωδικοποίηση", "Κωδικοποίηση Shannon-Fano", "Κωδικοποίηση Golomb", "Κωδικοποίηση Huffman"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος Huffman κατασκευάζει ένα βέλτιστο δυαδικό δέντρο προθεμάτων όπου οι πιο συχνοί χαρακτήρες κωδικοποιούνται με λιγότερα bits.",
    "funFacts": [
      "Ο Χάφμαν επινόησε τον αλγόριθμο ως μεταπτυχιακός φοιτητής στο MIT για μια εργασία εξαμήνου, όταν ο καθηγητής του Ρόμπερτ Φάνο τους έδωσε την επιλογή ανάμεσα σε τελική εξέταση ή επίλυση αυτού του προβλήματος.",
      "Χρησιμοποιείται ευρέως ως το τελικό στάδιο συμπίεσης σε πρότυπα όπως τα JPEG, MP3, ZIP και GZIP."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%B4%CE%B9%CE%BA%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_%CE%A7%CE%AC%CF%86%CE%BC%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["huffman", "compression", "algorithms", "information-theory"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_185",
    "text": "Ποιος μαθηματικός αλγόριθμος που επανεφηύραν οι Κούλι και Τούκι το 1965 επιτρέπει την ταχύτατη μετατροπή ενός ψηφιακού σήματος από το πεδίο του χρόνου στο πεδίο των συχνοτήτων;",
    "answers": ["Ταχύς Μετασχηματισμός Φουριέ (FFT)", "Μετασχηματισμός Laplace", "Μετασχηματισμός Wavelet", "Αλγόριθμος Gauss-Jordan"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο FFT (Fast Fourier Transform) μείωσε την υπολογιστική πολυπλοκότητα του διακριτού μετασχηματισμού Φουριέ από O(N^2) σε O(N log N), κάνοντας εφικτή την ψηφιακή επεξεργασία σημάτων.",
    "funFacts": [
      "Θεωρείται από το περιοδικό Computing in Science & Engineering ως ένας από τους 10 σημαντικότερους αλγορίθμους του 20ού αιώνα.",
      "Είναι απαραίτητος για τη συμπίεση ήχου MP3, την ψηφιακή τηλεφωνία 4G/5G (OFDM), τη μαγνητική τομογραφία (MRI) και τη σεισμολογία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CF%87%CF%8D%CF%82_%CE%BC%CE%B5%CF%84%CE%B1%CF%83%CF%87%CE%B7%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CF%8C%CF%82_%CE%A6%CE%BF%CF%85%CF%81%CE%B9%CE%AD",
    "locale": "el-GR",
    "tags": ["fft", "fourier", "signal-processing", "mathematics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_186",
    "text": "Σύμφωνα με το θεώρημα δειγματοληψίας των Νάικουιστ και Σάνον, ποιος πρέπει να είναι ο ελάχιστος ρυθμός δειγματοληψίας για την πιστή ψηφιοποίηση ενός αναλογικού σήματος χωρίς παραμόρφωση (aliasing);",
    "answers": ["Ίσος με τη μέγιστη συχνότητα", "Τουλάχιστον διπλάσιος από τη μέγιστη συχνότητα του σήματος", "Τετραπλάσιος από τη μέση συχνότητα", "Δέκα φορές μεγαλύτερος"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο ρυθμός Nyquist ορίζει ότι η συχνότητα δειγματοληψίας (fs) πρέπει να είναι αυστηρά μεγαλύτερη από το διπλάσιο της υψηλότερης συχνότητας (fmax) του σήματος (fs > 2*fmax).",
    "funFacts": [
      "Αν η δειγματοληψία γίνει σε χαμηλότερο ρυθμό, εμφανίζεται το φαινόμενο του 'ψευδωνυμισμού' (aliasing), όπου υψηλές συχνότητες παραμορφώνονται και εμφανίζονται ψευδώς ως χαμηλές.",
      "Για να αποτραπεί αυτό, τα συστήματα ήχου χρησιμοποιούν ένα φίλτρο anti-aliasing που κόβει όλες τις συχνότητες πάνω από το όριο Nyquist πριν τη δειγματοληψία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%8E%CF%81%CE%B7%CE%BC%CE%B1_%CE%B4%CE%B5%CE%B9%CE%B3%CE%BC%CE%B1%CF%84%CE%BF%CE%BB%CE%B7%CF%88%CE%AF%CE%B1%CF%82_%CE%9D%CE%AC%CE%B9%CE%BA%CE%BF%CF%85%CE%B9%CF%83%CF%84-%CE%A3%CE%AC%CE%BD%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["nyquist-shannon", "sampling", "audio", "signal-processing"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_187",
    "text": "Γιατί επιλέχθηκε συγκεκριμένα ο ρυθμός δειγματοληψίας των 44,1 kHz για το παγκόσμιο πρότυπο του μουσικού ψηφιακού δίσκου Compact Disc (CD-Audio);",
    "answers": ["Επειδή ήταν η μέγιστη ταχύτητα των επεξεργαστών της εποχής", "Λόγω της χωρητικότητας του λέιζερ", "Επειδή καλύπτει το ανώτατο όριο της ανθρώπινης ακοής (20 kHz) βάσει του θεωρήματος Nyquist", "Από τυχαίο υπολογιστικό λάθος της Sony"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το ανθρώπινο αυτί ακούει συχνότητες έως περίπου 20 kHz. Βάσει του θεωρήματος Nyquist, απαιτούνταν ρυθμός πάνω από 40 kHz, και τα 44,1 kHz ήταν επίσης συμβατά με τα πρότυπα βίντεο PAL και NTSC που χρησιμοποιούνταν για την εγγραφή των master tapes.",
    "funFacts": [
      "Ο ακριβής αριθμός 44.100 προέκυψε από το γινόμενο των πρώτων αριθμών 2^2 * 3^2 * 5^2 * 7^2, διευκολύνοντας τους μαθηματικούς υπολογισμούς.",
      "Επέτρεπε επίσης ένα περιθώριο 2,05 kHz για την ομαλή απόσβεση των αναλογικών φίλτρων αποκοπής (anti-aliasing filters)."
    ],
    "source": "https://el.wikipedia.org/wiki/Compact_Disc",
    "locale": "el-GR",
    "tags": ["cd-audio", "sampling-rate", "nyquist", "acoustics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_188",
    "text": "Πόσα διακριτά επίπεδα κβάντισης πλάτους (δυναμικό εύρος περίπου 96 dB) προσφέρει η ανάλυση βάθους 16-bit ενός απλού μουσικού CD ήχου;",
    "answers": ["256 επίπεδα", "1.024 επίπεδα", "4.096 επίπεδα", "65.536 επίπεδα"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Σε ανάλυση 16-bit, υπάρχουν 2^16 = 65.536 δυνατές ακέραιες τιμές για την περιγραφή του πλάτους του ηχητικού κύματος σε κάθε χρονικό δείγμα.",
    "funFacts": [
      "Κάθε επιπλέον bit βάθους δείγματος προσθέτει περίπου 6 dB στο θεωρητικό δυναμικό εύρος του ήχου (16 bits * 6 dB = 96 dB).",
      "Ο σύγχρονος επαγγελματικός ήχος υψηλής πιστότητας (Hi-Res Audio) χρησιμοποιεί συνήθως ανάλυση 24-bit, προσφέροντας 16.777.216 επίπεδα και δυναμικό εύρος 144 dB."
    ],
    "source": "https://el.wikipedia.org/wiki/Compact_Disc",
    "locale": "el-GR",
    "tags": ["bit-depth", "audio", "cd", "quantization"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_189",
    "text": "Ποιο πρότυπο ψηφιακής επικοινωνίας ηλεκτρονικών μουσικών οργάνων και υπολογιστών καθιερώθηκε το 1983 από τον Ντέιβ Σμιθ και κορυφαίους κατασκευαστές συνθεσάιζερ;",
    "answers": ["MIDI", "Open Sound Control (OSC)", "MP3", "ASIO"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το MIDI (Musical Instrument Digital Interface) δεν μεταφέρει πραγματικό ήχο, αλλά οδηγίες εκτέλεσης (νότες, ένταση, πλήκτρα, ρυθμό) μεταξύ συσκευών.",
    "funFacts": [
      "Ο Ντέιβ Σμιθ (Sequential Circuits) και ο Ίκουταρο Κακεχάσι (Roland) παρουσίασαν την πρώτη σύνδεση MIDI στο συνέδριο NAMM το 1983 συνδέοντας ένα Prophet-600 με ένα Roland Jupiter-6.",
      "Το πρωτόκολλο παρέμεινε ουσιαστικά αμετάβλητο για σχεδόν 40 χρόνια μέχρι την επίσημη εισαγωγή του προτύπου MIDI 2.0 το 2020."
    ],
    "source": "https://el.wikipedia.org/wiki/MIDI",
    "locale": "el-GR",
    "tags": ["midi", "music-technology", "synthesizers", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_190",
    "text": "Ποιο είναι το θεμελιώδες πλεονέκτημα των διανυσματικών γραφικών (Vector graphics, όπως SVG) σε σύγκριση με τα ψηφιογραφικά γραφικά (Raster, όπως JPEG/PNG);",
    "answers": ["Αποθηκεύουν περισσότερα χρώματα ανά pixel", "Μπορούν να μεγεθυνθούν σε οποιαδήποτε κλίμακα χωρίς καμία απώλεια ευκρίνειας", "Είναι ιδανικά για πολύπλοκες φυσικές φωτογραφίες τοπίων", "Δεν απαιτούν επεξεργαστή για την προβολή τους"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Τα διανυσματικά γραφικά ορίζονται μαθηματικά μέσω γεωμετρικών σημείων, γραμμών, καμπυλών Bezier και πολυγώνων, επιτρέποντας απεριόριστη κλιμάκωση χωρίς πίξελ.",
    "funFacts": [
      "Χρησιμοποιούνται υποχρεωτικά για τη σχεδίαση εταιρικών λογοτύπων, εικονιδίων διεπαφής χρήστη και γραμματοσειρών υπολογιστών.",
      "Το πρότυπο SVG (Scalable Vector Graphics) βασίζεται σε μορφή κειμένου XML και υποστηρίζεται εγγενώς από όλους τους σύγχρονους περιηγητές ιστού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B1%CE%BD%CF%85%CF%83%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CE%AC_%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CE%AC",
    "locale": "el-GR",
    "tags": ["vector-graphics", "svg", "design", "computer-graphics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_191",
    "text": "Ποια πρωτοποριακή γλώσσα περιγραφής σελίδας ανέπτυξαν οι Τζον Γουόρνοκ και Τσαρλς Γκέσκε το 1982 στην Adobe, πυροδοτώντας την επανάσταση της επιτραπέζιας τυπογραφίας (DTP);",
    "answers": ["TrueType", "TeX", "PostScript", "PCL"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η PostScript επέτρεψε σε υπολογιστές να στέλνουν εντολές υψηλού επιπέδου σε εκτυπωτές λέιζερ (όπως ο Apple LaserWriter το 1985), αποδίδοντας κείμενα και γραφικά σε τέλεια ανάλυση.",
    "funFacts": [
      "Η PostScript είναι στην πραγματικότητα μια πλήρης γλώσσα προγραμματισμού βασισμένη σε στοίβα (stack-based), όπως η Forth.",
      "Αποτέλεσε τον άμεσο τεχνολογικό πρόγονο του μορφότυπου PDF που δημιούργησε η Adobe το 1993."
    ],
    "source": "https://el.wikipedia.org/wiki/PostScript",
    "locale": "el-GR",
    "tags": ["postscript", "adobe", "printing", "fonts"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_192",
    "text": "Ποιες δύο ανταγωνίστριες εταιρείες συνεργάστηκαν στα μέσα της δεκαετίας του 1990 για την από κοινού ανάπτυξη του προηγμένου προτύπου γραμματοσειρών OpenType;",
    "answers": ["Apple και Google", "IBM και Apple", "Sun Microsystems και Oracle", "Microsoft και Adobe"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Microsoft και η Adobe ένωσαν τις δυνάμεις τους το 1996 συνδυάζοντας την τεχνολογία TrueType με την PostScript Type 1 σε μια ενιαία μορφή γραμματοσειρών OpenType (.otf).",
    "funFacts": [
      "Το OpenType υποστηρίζει έως και 65.536 γλύφους σε μία μόνο γραμματοσειρά και ενσωματώνει προηγμένα τυπογραφικά χαρακτηριστικά όπως συμπλέγματα γραμμάτων (ligatures) και παλαιού τύπου ψηφία.",
      "Βασίζεται πλήρως στην κωδικοποίηση Unicode, επιτρέποντας σε μία γραμματοσειρά να υποστηρίζει πολλαπλά αλφάβητα ταυτόχρονα (λατινικό, ελληνικό, κυριλλικό)."
    ],
    "source": "https://el.wikipedia.org/wiki/OpenType",
    "locale": "el-GR",
    "tags": ["opentype", "fonts", "typography", "adobe-microsoft"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_193",
    "text": "Ποια τεχνική γραφικών υπολογιστή απαλύνει τις τραχιές οδοντωτές άκρες (jaggies) σε γραμμές και πολυγωνικές ακμές αναμειγνύοντας κατάλληλα τα χρώματα των γειτονικών pixels;",
    "answers": ["Εξομάλυνση (Anti-aliasing)", "Ανισότροπο φιλτράρισμα (Anisotropic filtering)", "Χαρτογράφηση υφής (Texture mapping)", "Περικοπή βάθους (Occlusion culling)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Anti-aliasing (όπως MSAA, FXAA, TAA) εξαλείφει τα οπτικά τεχνουργήματα υποδειγματοληψίας υπολογίζοντας ενδιάμεσες αποχρώσεις στα όρια των αντικειμένων.",
    "funFacts": [
      "Στην απόδοση κειμένων σε οθόνες LCD, τεχνολογίες όπως το ClearType της Microsoft χρησιμοποιούν εξομάλυνση υπο-εικονοστοιχείων (subpixel rendering) στα κόκκινα, πράσινα και μπλε στοιχεία.",
      "Το κλασικό MSAA (Multi-Sample Anti-Aliasing) λαμβάνει πολλαπλά δείγματα μόνο στις ακμές των πολυγώνων για εξοικονόμηση επεξεργαστικής ισχύος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BE%CE%BF%CE%BC%CE%AC%CE%BB%CF%85%CE%BD%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["anti-aliasing", "computer-graphics", "rendering", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_194",
    "text": "Ποια προηγμένη τεχνική φωτορεαλιστικής απόδοσης γραφικών προσομοιώνει τη φυσική συμπεριφορά του φωτός παρακολουθώντας την πορεία μεμονωμένων ακτίνων και τις ανακλάσεις τους;",
    "answers": ["Rasterization", "Ιχνηλάτηση ακτίνων (Ray Tracing)", "Tessellation", "Bump mapping"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Ray Tracing παράγει εξαιρετικά ρεαλιστικές σκιές, ανακλάσεις και διαθλάσεις ακολουθώντας την αντίστροφη πορεία των ακτίνων φωτός από την εικονική κάμερα προς τις φωτεινές πηγές.",
    "funFacts": [
      "Προτάθηκε για πρώτη φορά στα γραφικά υπολογιστών από τον Άρθουρ Άπελ το 1968 και επεκτάθηκε από τον Τέρνερ Γουίτεν το 1979.",
      "Ενώ παραδοσιακά χρειαζόταν ώρες για την απόδοση ενός και μόνο καρέ σε ταινίες κινουμένων σχεδίων, οι σύγχρονες GPUs εκτελούν Ray Tracing σε πραγματικό χρόνο στα βιντεοπαιχνίδια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CF%87%CE%BD%CE%B7%CE%BB%CE%AC%CF%84%CE%B7%CF%83%CE%B7_%CE%B1%CE%BA%CF%84%CE%AF%CE%BD%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["ray-tracing", "computer-graphics", "rendering", "gpu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_195",
    "text": "Πώς ονομάζονται τα εξειδικευμένα μικροπρογράμματα που εκτελούνται απευθείας στους παράλληλους πυρήνες της κάρτας γραφικών για τον υπολογισμό επιφανειών, φωτισμού και εφέ;",
    "answers": ["Drivers", "Codecs", "Shaders", "Firmware"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι shaders (όπως Vertex, Pixel/Fragment και Compute shaders) γράφονται σε εξειδικευμένες γλώσσες (GLSL, HLSL) και ελέγχουν κάθε πτυχή της οπτικής απόδοσης στην GPU.",
    "funFacts": [
      "Η εισαγωγή των προγραμματιζόμενων shaders στις αρχές της δεκαετίας του 2000 (με τις κάρτες GeForce 3 και Xbox) τερμάτισε την εποχή του άκαμπτου σταθερού αγωγού γραφικών (fixed-function pipeline).",
      "Εκτός από γραφικά, οι σύγχρονοι compute shaders χρησιμοποιούνται για προσομοιώσεις φυσικής, υπολογισμούς τεχνητής νοημοσύνης και επεξεργασία ήχου."
    ],
    "source": "https://el.wikipedia.org/wiki/Shader",
    "locale": "el-GR",
    "tags": ["shaders", "gpu", "computer-graphics", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_196",
    "text": "Ποια σύγχρονη διεπαφή προγραμματισμού γραφικών χαμηλού επιπέδου (low-overhead API) σχεδιάστηκε από την κοινοπραξία Khronos Group ως ο άμεσος διάδοχος του OpenGL;",
    "answers": ["DirectX 9", "Metal", "Mantle", "Vulkan"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Vulkan προσφέρει άμεσο έλεγχο στο υλικό της GPU και ανώτερη απόδοση πολυνημάτωσης, μειώνοντας δραστικά την επιβάρυνση του επεξεργαστή (CPU overhead).",
    "funFacts": [
      "Βασίστηκε αρχικά σε τεχνολογικές συνεισφορές από το πειραματικό API Mantle της AMD.",
      "Είναι πλήρως ανεξάρτητο πλατφόρμας, τρέχοντας σε Windows, Linux, Android και μέσω του επιπέδου MoltenVK ακόμη και σε macOS/iOS."
    ],
    "source": "https://el.wikipedia.org/wiki/Vulkan",
    "locale": "el-GR",
    "tags": ["vulkan", "opengl", "graphics-api", "khronos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_197",
    "text": "Ποια σουίτα διεπαφών προγραμματισμού πολυμέσων (APIs) κυκλοφόρησε η Microsoft το 1995 για να καταστήσει τα Windows 95 κορυφαία πλατφόρμα ανάπτυξης βιντεοπαιχνιδιών;",
    "answers": ["DirectX", "QuickTime", "OpenGL", "XNA"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το DirectX παρείχε στους δημιουργούς παιχνιδιών άμεση πρόσβαση χαμηλού επιπέδου στο υλικό της κάρτας γραφικών και ήχου, παρακάμπτοντας τους περιορισμούς των Windows.",
    "funFacts": [
      "Αναπτύχθηκε αρχικά με την κωδική ονομασία 'Manhattan Project' από τους μηχανικούς Άλεξ Σεντ Τζον, Κρεγκ Άισλερ και Έρικ Ένγκστρομ.",
      "Περιλαμβάνει επιμέρους συνιστώσες όπως το Direct3D για γραφικά, το DirectSound για ήχο και το DirectInput για χειριστήρια."
    ],
    "source": "https://el.wikipedia.org/wiki/DirectX",
    "locale": "el-GR",
    "tags": ["directx", "microsoft", "gaming", "windows"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_198",
    "text": "Από ποιο τεχνολογικό προϊόν της Microsoft πήρε αρχικά το όνομά της η κονσόλα βιντεοπαιχνιδιών Xbox όταν σχεδιάστηκε ως πρωτότυπο («DirectX Box»);",
    "answers": ["Windows", "DirectX", "Excel", "MS-DOS"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Μια ομάδα τεσσάρων μηχανικών της ομάδας του DirectX (Σέιμους Μπλάκλεϊ, Κέβιν Μπαχούς, Τεντ Χας και Ότο Μπερκς) κατασκεύασε την πρώτη κονσόλα ως 'DirectX Box'.",
    "funFacts": [
      "Το τμήμα μάρκετινγκ της Microsoft μισούσε αρχικά το όνομα Xbox και πρότεινε δεκάδες εναλλακτικές (όπως WEP, FACE και MITH), αλλά το Xbox κέρδισε στις έρευνες καταναλωτών.",
      "Η αρχική κονσόλα Xbox κυκλοφόρησε το 2001 βασισμένη σε επεξεργαστή Intel Pentium III και κάρτα γραφικών Nvidia GeForce 3."
    ],
    "source": "https://el.wikipedia.org/wiki/Xbox",
    "locale": "el-GR",
    "tags": ["xbox", "microsoft", "directx", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_199",
    "text": "Ποιος Αμερικανός προγραμματιστής και επιχειρηματίας ίδρυσε την Epic Games και έγραψε την αρχική μηχανή παιχνιδιών Unreal Engine το 1998;",
    "answers": ["Γκέιμπ Νιούελ", "Τοντ Χάουαρντ", "Τιμ Σουίνι", "Κλιφ Μπλεζίνσκι"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τιμ Σουίνι (Tim Sweeney) έγραψε σχεδόν μόνος του το 90% του κώδικα της πρώτης μηχανής Unreal, η οποία εξελίχθηκε στην κορυφαία εμπορική μηχανή τρισδιάστατων γραφικών παγκοσμίως.",
    "funFacts": [
      "Η Unreal Engine κατέχει το ρεκόρ Γκίνες ως η 'πιο επιτυχημένη μηχανή βιντεοπαιχνιδιών' στον κόσμο.",
      "Εκτός από παιχνίδια όπως το Fortnite, χρησιμοποιείται σήμερα στην παραγωγή ταινιών του Χόλιγουντ (όπως στη σειρά The Mandalorian) για ψηφιακά σκηνικά σε πραγματικό χρόνο."
    ],
    "source": "https://el.wikipedia.org/wiki/Unreal_Engine",
    "locale": "el-GR",
    "tags": ["unreal-engine", "tim-sweeney", "epic-games", "game-development"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_200",
    "text": "Ποιος θρυλικός προγραμματιστής της id Software πρωτοπόρησε στα τρισδιάστατα γραφικά πραγματικού χρόνου αναπτύσσοντας τις ιστορικές μηχανές των Wolfenstein 3D, Doom και Quake;",
    "answers": ["Σιντ Μέγιερ", "Γουίλ Ράιτ", "Πίτερ Μολινέ", "Τζον Κάρμακ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζον Κάρμακ (John Carmack) έφερε επανάσταση στα γραφικά υπολογιστών με αλγορίθμους όπως το adaptive tile refresh, το raycasting, τα δέντρα BSP και το δικτυακό multiplayer.",
    "funFacts": [
      "Αργότερα διετέλεσε επικεφαλής τεχνολογίας (CTO) στην Oculus VR, καθορίζοντας τη σύγχρονη εικονική πραγματικότητα.",
      "Είναι επίσης γνωστός για τη φιλοσοφία του να διαθέτει τον πηγαίο κώδικα των παλαιότερων μηχανών παιχνιδιών του ως ελεύθερο λογισμικό ανοιχτού κώδικα υπό άδεια GPL."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%9A%CE%AC%CF%81%CE%BC%CE%B1%CE%BA",
    "locale": "el-GR",
    "tags": ["john-carmack", "doom", "quake", "graphics-programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_201",
    "text": "Ποια ιεραρχική γεωμετρική δομή δεδομένων αξιοποίησε ο Τζον Κάρμακ στο παιχνίδι Doom για τον ταχύτατο υπολογισμό των ορατών επιφανειών χωρίς περιττή επανάληψη σχεδίασης;",
    "answers": ["Δέντρο BSP (Binary Space Partitioning)", "Octree", "Kd-tree", "Bounding Volume Hierarchy"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το δέντρο BSP διαχωρίζει αναδρομικά τον τρισδιάστατο χώρο με υπερεπίπεδα, επιτρέποντας την ταξινόμηση όλων των πολυγώνων από εμπρός προς τα πίσω σε χρόνο O(N).",
    "funFacts": [
      "Η τεχνική προϋπολόγιζε τη γεωμετρία της πίστας εκ των προτέρων (προ-επεξεργασία), επιτρέποντας στο Doom να τρέχει με εντυπωσιακή ταχύτητα σε απλούς επεξεργαστές Intel 486.",
      "Ανέπτυξε την ιδέα αφού διάβασε ακαδημαϊκές δημοσιεύσεις του 1980 των Μπρους Νέιλορ και Χένρι Φουξ."
    ],
    "source": "https://el.wikipedia.org/wiki/Doom",
    "locale": "el-GR",
    "tags": ["bsp-tree", "doom", "carmack", "algorithms"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_202",
    "text": "Ποιος διάσημος αλγόριθμος ταχύτατου υπολογισμού του 1/sqrt(x) με τον μυστηριώδη αριθμό 0x5f3759df έγινε θρυλικός στον πηγαίο κώδικα του Quake III Arena;",
    "answers": ["Μέθοδος του Newton-Raphson", "Fast Inverse Square Root", "Αλγόριθμος CORDIC", "Παρεμβολή Lagrange"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος εκμεταλλεύεται τον τρόπο αναπαράστασης των αριθμών κινητής υποδιαστολής IEEE 754 κάνοντας έναν ευφυή δυαδικό χειρισμό σε επίπεδο ακεραίου και μία μόνο επανάληψη Newton.",
    "funFacts": [
      "Ήταν έως και 4 φορές ταχύτερος από την κανονική διαίρεση κινητής υποδιαστολής στο υλικό της δεκαετίας του 1990, όντας απαραίτητος για τον υπολογισμό διανυσμάτων φωτισμού.",
      "Η ακριβής αρχική πατρότητα του μυστηριώδους 'μαγικού αριθμού' παρέμενε άγνωστη για χρόνια, πριν αποδοθεί στον Γκρεγκ Γουόλς της Ardent Computer."
    ],
    "source": "https://el.wikipedia.org/wiki/Fast_inverse_square_root",
    "locale": "el-GR",
    "tags": ["fast-inverse-sqrt", "quake", "algorithms", "carmack"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_203",
    "text": "Ποια τεχνική δημιουργίας δυναμικών φωτοσκιάσεων σε πραγματικό χρόνο (stencil shadow volumes) ανακαλύφθηκε ανεξάρτητα από τον Τζον Κάρμακ κατά την ανάπτυξη του Doom 3;",
    "answers": ["Shadow Mapping", "Ray Traced Shadows", "Carmack's Reverse (Z-Fail)", "Ambient Occlusion"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μέθοδος Z-Fail (Carmack's Reverse) έλυσε το χρόνιο πρόβλημα σφάλματος σκίασης όταν η κάμερα του παίκτη εισέρχεται μέσα στον όγκο της σκιάς.",
    "funFacts": [
      "Ο Κάρμακ ανακάλυψε αργότερα ότι η ίδια μαθηματική τεχνική είχε κατοχυρωθεί με πατέντα λίγους μήνες νωρίτερα από την εταιρεία Creative Technology.",
      "Για να αποφύγει δικαστικές διαμάχες, η id Software αναγκάστηκε να υπογράψει συμφωνία με την Creative για την ενσωμάτωση της τεχνολογίας ήχου EAX στο Doom 3."
    ],
    "source": "https://el.wikipedia.org/wiki/Doom_3",
    "locale": "el-GR",
    "tags": ["carmacks-reverse", "doom-3", "graphics", "shadows"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_204",
    "text": "Πώς ονομάζεται το τρισδιάστατο ισοδύναμο του δισδιάστατου pixel, που αντιπροσωπεύει μια μονάδα όγκου σε ένα κανονικό τρισδιάστατο πλέγμα (όπως στα μπλοκ του Minecraft);",
    "answers": ["Texel", "Vertex", "Polygon", "Voxel (Volumetric Pixel)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το voxel (σύντμηση των λέξεων volumetric και pixel) περιέχει πληροφορίες όπως χρώμα, πυκνότητα ή διαφάνεια σε τρισδιάστατο χώρο.",
    "funFacts": [
      "Χρησιμοποιείται ευρέως στην ιατρική απεικόνιση (αξονική τομογραφία CT και μαγνητική τομογραφία MRI) για την αναπαράσταση τρισδιάστατων ανθρώπινων οργάνων.",
      "Παιχνίδια όπως το Minecraft και το Teardown αξιοποιούν voxels για πλήρως καταστρέψιμους και τροποποιήσιμους κόσμους."
    ],
    "source": "https://el.wikipedia.org/wiki/Voxel",
    "locale": "el-GR",
    "tags": ["voxel", "3d-graphics", "minecraft", "medical-imaging"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_205",
    "text": "Ποιος θεμελιώδης αλγόριθμος γραφικών υπολογιστή διατηρεί έναν πίνακα με τις αποστάσεις βάθους κάθε εικονοστοιχείου από την κάμερα για να επιλύει ποια επιφάνεια κρύβει ποια;",
    "answers": ["Z-buffering (Depth buffering)", "Alpha Blending", "Ray Marching", "Rasterization"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο ενταμιευτής Z (Z-buffer) αποθηκεύει την τιμή βάθους Z κάθε pixel, σχεδιάζοντας ένα νέο pixel μόνο αν βρίσκεται πιο κοντά στον παρατηρητή από το ήδη αποθηκευμένο.",
    "funFacts": [
      "Επινόησε την τεχνική ο Έντγουιν Κάτμουλ (συνιδρυτής της Pixar) το 1974 στη διδακτορική του διατριβή στο Πανεπιστήμιο της Γιούτα.",
      "Είναι ενσωματωμένος στο υλικό σχεδόν όλων των σύγχρονων καρτών γραφικών, αποτελώντας τη βάση της τρισδιάστατης απόδοσης."
    ],
    "source": "https://el.wikipedia.org/wiki/Z-buffering",
    "locale": "el-GR",
    "tags": ["z-buffer", "catmull", "computer-graphics", "rendering"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_206",
    "text": "Ποιος ρυθμός ανανέωσης καρέ (FPS - Frames Per Second) θεωρείται το ελάχιστο σύγχρονο πρότυπο για ομαλή απόκριση σε competitive esports βιντεοπαιχνίδια;",
    "answers": ["24 FPS", "60 FPS", "15 FPS", "30 FPS"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Τα 60 καρέ ανά δευτερόλεπτο (60 FPS) προσφέρουν χρόνο ανανέωσης 16,6 χιλιοστών του δευτερολέπτου ανά καρέ, παρέχοντας άμεση απόκριση στις εντολές του παίκτη.",
    "funFacts": [
      "Στον παραδοσιακό κινηματογράφο, το πρότυπο είναι 24 FPS, το οποίο δημιουργεί φυσικό θόλωμα κίνησης (motion blur).",
      "Σε επαγγελματικές gaming οθόνες esports χρησιμοποιούνται ρυθμοί 144 Hz, 240 Hz ή ακόμη και 360-540 Hz για ελαχιστοποίηση της καθυστέρησης εισόδου (input lag)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%85%CE%B8%CE%BC%CF%8C%CF%82_%CE%B1%CE%BD%CE%B1%CE%BD%CE%AD%CF%89%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["fps", "frame-rate", "gaming", "esports"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_207",
    "text": "Ποια τεχνολογία συγχρονίζει τον ρυθμό παραγωγής καρέ της κάρτας γραφικών με τον σταθερό ρυθμό ανανέωσης της οθόνης για να αποτρέψει το οριζόντιο σχίσιμο της εικόνας (screen tearing);",
    "answers": ["G-Sync", "FreeSync", "V-Sync (Vertical Synchronization)", "DLSS"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο κατακόρυφος συγχρονισμός (V-Sync) υποχρεώνει την GPU να περιμένει το διάστημα κάθετης απόσβεσης (vertical blanking interval) της οθόνης πριν στείλει το νέο καρέ.",
    "funFacts": [
      "Το κύριο μειονέκτημα του απλού V-Sync είναι ότι αν η κάρτα δεν προλάβει να ετοιμάσει το καρέ στην ώρα του, το frame rate πέφτει απότομα στο μισό (π.χ. από 60 σε 30 FPS).",
      "Επιπλέον, εισάγει αισθητή καθυστέρηση εισόδου (input lag), γι' αυτό αναπτύχθηκαν οι νεότερες τεχνολογίες μεταβλητού ρυθμού (VRR)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%B1%CE%BA%CF%8C%CF%81%CF%85%CF%86%CE%BF%CF%82_%CF%83%CF%85%CE%B3%CF%87%CF%81%CE%BF%CE%BD%CE%B9%CF%83%CE%BC%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["vsync", "tearing", "gaming", "monitors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_208",
    "text": "Ποια εταιρεία ανέπτυξε το ανοιχτό πρότυπο μεταβλητού ρυθμού ανανέωσης FreeSync, το οποίο βασίζεται στο Adaptive-Sync του DisplayPort χωρίς ιδιόκτητο τσιπ υλικού;",
    "answers": ["Intel", "Nvidia", "Qualcomm", "AMD"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η AMD παρουσίασε το FreeSync το 2014 ως δωρεάν απάντηση ανοιχτού προτύπου απέναντι στην κλειστή τεχνολογία G-Sync της Nvidia.",
    "funFacts": [
      "Προσάρμοσε τον ρυθμό της οθόνης δυναμικά στα καρέ που παράγει η GPU σε πραγματικό χρόνο, εξαλείφοντας το tearing χωρίς το lag του V-Sync.",
      "Η τεχνολογία ενσωματώθηκε επίσημα στις προδιαγραφές του DisplayPort 1.2a και στα πρότυπα HDMI 2.1 VRR."
    ],
    "source": "https://el.wikipedia.org/wiki/FreeSync",
    "locale": "el-GR",
    "tags": ["freesync", "amd", "displays", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_209",
    "text": "Ποια πρωτοποριακή τεχνολογία τεχνητής νοημοσύνης της Nvidia αναβαθμίζει (upscales) εικόνες χαμηλότερης ανάλυσης σε πραγματικό χρόνο χρησιμοποιώντας τους πυρήνες Tensor;",
    "answers": ["DLSS (Deep Learning Super Sampling)", "FSR (FidelityFX Super Resolution)", "XeSS", "SMAA"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το DLSS εκπαιδεύεται σε υπερυπολογιστές της Nvidia με εικόνες εξαιρετικά υψηλής ποιότητας (16K ground truth), επιτρέποντας στην GPU να αποδίδει το παιχνίδι σε χαμηλότερη ανάλυση και να το μεγεθύνει με τεχνητή νοημοσύνη.",
    "funFacts": [
      "Η έκδοση DLSS 3 εισήγαγε τη λειτουργία Frame Generation, όπου νευρωνικά δίκτυα δημιουργούν εξ ολοκλήρου νέα ενδιάμεσα καρέ διπλασιάζοντας το frame rate.",
      "Απαιτεί αποκλειστικά κάρτες γραφικών της σειράς Nvidia GeForce RTX με ενσωματωμένους πυρήνες Tensor."
    ],
    "source": "https://el.wikipedia.org/wiki/Deep_Learning_Super_Sampling",
    "locale": "el-GR",
    "tags": ["dlss", "nvidia", "ai", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_210",
    "text": "Πώς ονομάζονται οι εξειδικευμένες υπολογιστικές μονάδες υλικού που ενσωμάτωσε η Nvidia στις κάρτες αρχιτεκτονικής Turing (σειρά RTX) αποκλειστικά για την επιτάχυνση του Ray Tracing;",
    "answers": ["Tensor Cores", "RT Cores", "CUDA Cores", "Stream Processors"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι πυρήνες RT (Ray Tracing Cores) είναι ειδικά κυκλώματα πυριτίου σχεδιασμένα να επιταχύνουν τους υπολογισμούς δομών BVH (Bounding Volume Hierarchy) και τις τομές ακτίνας-τριγώνου.",
    "funFacts": [
      "Απάλλαξαν τους γενικούς υπολογιστικούς πυρήνες CUDA από τον τεράστιο όγκο υπολογισμού τομών ακτίνων, κάνοντας το φωτορεαλιστικό Ray Tracing εφικτό σε πραγματικό χρόνο.",
      "Η αντίστοιχη μονάδα υλικού στις κάρτες γραφικών RDNA της AMD ονομάζεται Ray Accelerator."
    ],
    "source": "https://el.wikipedia.org/wiki/Nvidia",
    "locale": "el-GR",
    "tags": ["rt-cores", "ray-tracing", "nvidia", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'medium', 3, questions)

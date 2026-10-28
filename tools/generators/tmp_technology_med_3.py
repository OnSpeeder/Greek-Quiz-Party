# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "tech_med_111",
    "text": "Ποιος 16-bit επεξεργαστής που κυκλοφόρησε η Intel το 1978 δημιούργησε την ιστορική οικογένεια αρχιτεκτονικής x86;",
    "answers": ["Intel 8086", "Intel 8080", "Intel 80486", "Intel Pentium"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Intel 8086 ήταν ο πρώτος 16-bit επεξεργαστής της Intel και η αρχιτεκτονική συνόλου εντολών του αποτέλεσε το θεμέλιο της πλατφόρμας PC.",
    "funFacts": [
      "Μια ελαφρώς φθηνότερη παραλλαγή του με εξωτερικό δίαυλο 8-bit, ο Intel 8088, επιλέχθηκε από την IBM για το πρώτο IBM PC το 1981.",
      "Ο όρος 'x86' προέκυψε επειδή οι επόμενοι επεξεργαστές της σειράς είχαν ονόματα που τελείωναν σε '86' (80186, 80286, 80386, 80486)."
    ],
    "source": "https://el.wikipedia.org/wiki/Intel_8086",
    "locale": "el-GR",
    "tags": ["intel-8086", "x86", "microprocessors", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_112",
    "text": "Ποια εταιρεία ανέπτυξε πρώτη την 64-bit επέκταση της αρχιτεκτονικής x86 (AMD64 / x86-64) με τους επεξεργαστές Opteron και Athlon 64 το 2003;",
    "answers": ["Intel", "AMD", "IBM", "Cyrix"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η AMD σχεδίασε την αρχιτεκτονική AMD64 διατηρώντας πλήρη συμβατότητα με τις εφαρμογές 32-bit x86, αναγκάζοντας τελικά την Intel να υιοθετήσει το ίδιο πρότυπο.",
    "funFacts": [
      "Η ανταγωνιστική 64-bit αρχιτεκτονική Itanium (IA-64) της Intel απέτυχε επειδή δεν υποστήριζε εγγενώς παλαιότερο κώδικα x86.",
      "Σήμερα σχεδόν όλοι οι επεξεργαστές προσωπικών υπολογιστών και διακομιστών Intel και AMD βασίζονται στην προδιαγραφή x86-64."
    ],
    "source": "https://el.wikipedia.org/wiki/X86-64",
    "locale": "el-GR",
    "tags": ["amd64", "x86-64", "amd", "microprocessors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_113",
    "text": "Ποιος πρωτοπόρος μηχανικός ίδρυσε την TSMC στην Ταϊβάν το 1987, καθιερώνοντας το επιχειρηματικό μοντέλο του ανεξάρτητου εργοστασίου ημιαγωγών (pure-play foundry);",
    "answers": ["Τέρι Γκου", "Τσενγκ-Τσουνγκ Γουάνγκ", "Μόρις Τσανγκ", "Ρόμπερτ Τσάο"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Μόρις Τσανγκ (Morris Chang) συνειδητοποίησε ότι οι εταιρείες σχεδιασμού τσιπ χρειάζονταν ένα ανεξάρτητο εργοστάσιο παραγωγής που δεν θα ανταγωνιζόταν τα δικά τους προϊόντα.",
    "funFacts": [
      "Η TSMC κατασκευάζει σήμερα πάνω από το 90% των πιο προηγμένων μικροτσίπ στον πλανήτη, τροφοδοτώντας την Apple, την Nvidia, την AMD και την Qualcomm.",
      "Ο Τσανγκ είχε προηγουμένως εργαστεί επί 25 χρόνια στην Texas Instruments, ανεβαίνοντας στη θέση του αντιπροέδρου παγκόσμιων δραστηριοτήτων ημιαγωγών."
    ],
    "source": "https://el.wikipedia.org/wiki/TSMC",
    "locale": "el-GR",
    "tags": ["tsmc", "morris-chang", "semiconductors", "taiwan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_114",
    "text": "Ποια ολλανδική εταιρεία κατέχει παγκόσμιο μονοπώλιο στην κατασκευή των μηχανημάτων ακραίας υπεριώδους λιθογραφίας (EUV) που απαιτούνται για τα πιο σύγχρονα μικροτσίπ;",
    "answers": ["NXP Semiconductors", "Philips", "Tokyo Electron", "ASML"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η ASML, με έδρα το Βελντχόφεν της Ολλανδίας, είναι η μόνη εταιρεία που κατασκευάζει συστήματα λιθογραφίας EUV (Extreme Ultraviolet) για τσιπ κάτω των 7 νανομέτρων.",
    "funFacts": [
      "Κάθε μηχάνημα EUV της ASML κοστίζει πάνω από 200-350 εκατομμύρια δολάρια, έχει μέγεθος λεωφορείου και ζυγίζει περίπου 180 τόνους.",
      "Χρησιμοποιεί λέιζερ CO2 που εξαϋλώνει 50.000 μικροσκοπικές σταγόνες λιωμένου κασσίτερου ανά δευτερόλεπτο για να παραγάγει φως EUV μήκους κύματος μόλις 13,5 nm."
    ],
    "source": "https://el.wikipedia.org/wiki/ASML",
    "locale": "el-GR",
    "tags": ["asml", "lithography", "euv", "semiconductors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_115",
    "text": "Πώς ονομάζεται το επιχειρηματικό μοντέλο εταιρειών τεχνολογίας (όπως Apple, Nvidia και Qualcomm) που σχεδιάζουν μικροτσίπ αλλά αναθέτουν εξ ολοκλήρου την κατασκευή τους σε τρίτα εργοστάσια;",
    "answers": ["Fabless (χωρίς εργοστάσιο)", "Foundry", "IDM (Integrated Device Manufacturer)", "OEM"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Οι εταιρείες fabless επικεντρώνονται στην έρευνα, την αρχιτεκτονική και τον σχεδιασμό κυκλωμάτων, εξοικονομώντας τα δεκάδες δισεκατομμύρια δολάρια που απαιτούνται για την ανέγερση εργοστασίων πυριτίου.",
    "funFacts": [
      "Αντίθετα, εταιρείες όπως η Intel και η Samsung που σχεδιάζουν και κατασκευάζουν τα δικά τους τσιπ σε ιδιόκτητα εργοστάσια ονομάζονται IDM (Integrated Device Manufacturers).",
      "Η ανέγερση ενός και μόνο σύγχρονου εργοστασίου ημιαγωγών (fab) κοστίζει σήμερα πάνω από 15 έως 20 δισεκατομμύρια δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97%CE%BC%CE%B9%CE%B1%CE%B3%CF%89%CE%B3%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["fabless", "semiconductors", "hardware", "business"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_116",
    "text": "Σε ποιο έτος ιδρύθηκε η εταιρεία επεξεργαστών γραφικών Nvidia από τους Τζένσεν Χουάνγκ, Κρις Μαλακόφσκι και Κέρτις Πριμ σε ένα εστιατόριο Denny's στην Καλιφόρνια;",
    "answers": ["1989", "1993", "1999", "2002"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Nvidia ιδρύθηκε τον Απρίλιο του 1993 με όραμα να φέρει τρισδιάστατα γραφικά σε πραγματικό χρόνο στους προσωπικούς υπολογιστές.",
    "funFacts": [
      "Το όνομα Nvidia προήλθε από τη λατινική λέξη 'invidia' που σημαίνει φθόνος (εξ ου και το παραδοσιακό πράσινο χρώμα της εταιρείας).",
      "Το 1999 κυκλοφόρησε την GeForce 256, ορίζοντας για πρώτη φορά στην αγορά τον όρο GPU (Graphics Processing Unit)."
    ],
    "source": "https://el.wikipedia.org/wiki/Nvidia",
    "locale": "el-GR",
    "tags": ["nvidia", "jensen-huang", "gpu", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_117",
    "text": "Ποια αρχιτεκτονική και πλατφόρμα παράλληλου προγραμματισμού παρουσίασε η Nvidia το 2006, επιτρέποντας τη χρήση των GPUs για επιστημονικούς υπολογισμούς γενικού σκοπού;",
    "answers": ["OpenCL", "DirectX", "CUDA", "Vulkan"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το CUDA (Compute Unified Device Architecture) επέτρεψε στους προγραμματιστές να εκμεταλλευτούν τους χιλιάδες πυρήνες της κάρτας γραφικών για βαριές αριθμητικές προσομοιώσεις και τεχνητή νοημοσύνη.",
    "funFacts": [
      "Η επένδυση δισεκατομμυρίων της Nvidia στο CUDA θεωρήθηκε τότε οικονομικά ριψοκίνδυνη, αλλά αποτέλεσε το θεμέλιο της σημερινής παγκόσμιας κυριαρχίας της στην τεχνητή νοημοσύνη.",
      "Σχεδόν όλα τα σύγχρονα πλαίσια βαθιάς μάθησης (όπως PyTorch και TensorFlow) βασίζονται στην επιτάχυνση βιβλιοθηκών CUDA."
    ],
    "source": "https://el.wikipedia.org/wiki/CUDA",
    "locale": "el-GR",
    "tags": ["cuda", "nvidia", "gpu", "ai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_118",
    "text": "Ποιος Βρετανοκαναδός επιστήμονας, γνωστός ως «νονός της τεχνητής νοημοσύνης», τιμήθηκε με το Νόμπελ Φυσικής το 2024 για τις θεμελιώδεις ανακαλύψεις του στα τεχνητά νευρωνικά δίκτυα;",
    "answers": ["Ντέμης Χασάμπης", "Γιαν ΛεΚούν", "Γιόσουα Μπέντζιο", "Τζέφρι Χίντον"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τζέφρι Χίντον (Geoffrey Hinton) μοιράστηκε το Νόμπελ Φυσικής 2024 με τον Τζον Χόπφιλντ για την ανάπτυξη μεθόδων μηχανικής μάθησης βασισμένων σε φυσικά μοντέλα.",
    "funFacts": [
      "Το 2012, η ομάδα του Χίντον στο Πανεπιστήμιο του Τορόντο δημιούργησε το νευρωνικό δίκτυο AlexNet, το οποίο πυροδότησε τη σύγχρονη επανάσταση της βαθιάς μάθησης (Deep Learning).",
      "Παραιτήθηκε από την Google το 2023 για να μπορεί να μιλά ελεύθερα για τους υπαρξιακούς κινδύνους που μπορεί να εγκυμονεί η ανεξέλεγκτη ανάπτυξη της τεχνητής νοημοσύνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CF%86%CF%81%CE%B9_%CE%A7%CE%AF%CE%BD%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["geoffrey-hinton", "nobel", "ai", "deep-learning"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_119",
    "text": "Ποιος Γάλλος πρωτοπόρος της τεχνητής νοημοσύνης ανέπτυξε τα συνελικτικά νευρωνικά δίκτυα (CNNs) και το σύστημα LeNet για την οπτική αναγνώριση χειρόγραφων χαρακτήρων;",
    "answers": ["Γιαν ΛεΚούν", "Τζέφρι Χίντον", "Γιόσουα Μπέντζιο", "Άντριου Ενγκ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Γιαν ΛεΚούν (Yann LeCun) ανέπτυξε στα εργαστήρια Bell Labs το σύστημα LeNet-5 το 1998, το οποίο χρησιμοποιήθηκε από τράπεζες των ΗΠΑ για την ανάγνωση τραπεζικών επιταγών.",
    "funFacts": [
      "Είναι επικεφαλής επιστήμονας τεχνητής νοημοσύνης στη Meta (Chief AI Scientist) και καθηγητής στο Πανεπιστήμιο της Νέας Υόρκης (NYU).",
      "Μοιράστηκε το Βραβείο Turing το 2018 μαζί με τους Τζέφρι Χίντον και Γιόσουα Μπέντζιο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%B1%CE%BD_%CE%9B%CE%B5%CE%9A%CE%BF%CF%8D%CE%BD",
    "locale": "el-GR",
    "tags": ["lecun", "ai", "cnn", "computer-vision"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_120",
    "text": "Σε ποιο έτος δημοσίευσαν ερευνητές της Google την ιστορική επιστημονική μελέτη «Attention Is All You Need», η οποία εισήγαγε την αρχιτεκτονική Transformer;",
    "answers": ["2014", "2017", "2019", "2021"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μελέτη 'Attention Is All You Need' παρουσιάστηκε τον Ιούνιο του 2017 στο συνέδριο NeurIPS, καταργώντας τα αναδρομικά δίκτυα (RNNs) χάρη στον μηχανισμό αυτό-προσοχής (self-attention).",
    "funFacts": [
      "Η αρχιτεκτονική Transformer αποτελεί τη βάση όλων των σύγχρονων μεγάλων γλωσσικών μοντέλων, όπως το GPT-4, το BERT, το Gemini και το Claude.",
      "Και οι οκτώ κύριοι συγγραφείς της ιστορικής μελέτης της Google αποχώρησαν αργότερα για να ιδρύσουν δικές τους κορυφαίες εταιρείες AI (όπως Cohere, Character.ai και Essential AI)."
    ],
    "source": "https://el.wikipedia.org/wiki/Transformer_(%CE%BC%CE%BF%CE%BD%CF%84%CE%AD%CE%BB%CE%BF_%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%BC%CE%AC%CE%B8%CE%B7%CF%83%CE%B7%CF%82)",
    "locale": "el-GR",
    "tags": ["transformer", "ai", "google", "deep-learning"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_121",
    "text": "Πώς ονομαζόταν η ηλεκτρομηχανική συσκευή που σχεδίασε ο Άλαν Τιούρινγκ στο Bletchley Park για την ταχύτατη αποκρυπτογράφηση των μηνυμάτων της γερμανικής μηχανής Enigma;",
    "answers": ["Colossus", "Enigma Plus", "Bombe", "Ultra"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μηχανή Bombe εξέταζε αυτόματα χιλιάδες πιθανές θέσεις των στροφέων (rotors) της Enigma, μειώνοντας δραστικά τον χρόνο εντοπισμού των ημερήσιων ρυθμίσεων.",
    "funFacts": [
      "Βασίστηκε και εξέλιξε μια προγενέστερη ιδέα των Πολωνών μαθηματικών Μάριαν Ρεγιέφσκι, Γέζι Ροζίτσκι και Χένρικ Ζιγκάλσκι που ονομαζόταν 'Bomba'.",
      "Περισσότερες από 200 συσκευές Bombe κατασκευάστηκαν και λειτούργησαν στη Βρετανία κατά τη διάρκεια του Β' Παγκοσμίου Πολέμου, επανδρωμένες κυρίως από γυναίκες του Wrens."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%B1%CE%BD_%CE%A4%CE%B9%CE%BF%CF%81%CE%B9%CE%BD%CE%B3%CE%BA",
    "locale": "el-GR",
    "tags": ["bombe", "turing", "enigma", "cryptography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_122",
    "text": "Ποιος Βρετανός μηχανικός τηλεπικοινωνιών σχεδίασε τον υπολογιστή Colossus το 1943, τον πρώτο προγραμματιζόμενο ηλεκτρονικό υπολογιστή με λυχνίες στον κόσμο;",
    "answers": ["Άλαν Τιούρινγκ", "Μορίς Γουίλκς", "Τσαρλς Μπάμπατζ", "Τόμι Φλάουερς"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Τόμι Φλάουερς (Tommy Flowers) σχεδίασε τον Colossus στο Post Office Research Station για το σπάσιμο των ανώτατων γερμανικών τηλετυπικών κρυπτογραφημάτων Lorenz SZ40/42.",
    "funFacts": [
      "Ο Colossus χρησιμοποιούσε περίπου 1.600 έως 2.400 θερμιονικές ηλεκτρονικές λυχνίες, διαβάζοντας διάτρητη χαρτοταινία με ταχύτητα 5.000 χαρακτήρων ανά δευτερόλεπτο.",
      "Η ύπαρξη του Colossus κρατήθηκε απόλυτο κρατικό μυστικό για πάνω από τρεις δεκαετίες, με αποτέλεσμα ο Φλάουερς να μην λάβει τη δημόσια αναγνώριση που του άξιζε όσο ζούσε."
    ],
    "source": "https://el.wikipedia.org/wiki/Colossus_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE%CF%82)",
    "locale": "el-GR",
    "tags": ["colossus", "tommy-flowers", "cryptography", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_123",
    "text": "Ποιος Γερμανός πολιτικός μηχανικός και εφευρέτης κατασκεύασε τον Z3 το 1941, τον πρώτο λειτουργικό πλήρως αυτόματο προγραμματιζόμενο ψηφιακό υπολογιστή στον κόσμο;",
    "answers": ["Κόνραντ Τσούζε", "Βέρνερ φον Μπράουν", "Χάινριχ Χερτς", "Καρλ Φερντινάντ Μπράουν"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Κόνραντ Τσούζε (Konrad Zuse) κατασκεύασε τον Z3 στο Βερολίνο χρησιμοποιώντας 2.600 ηλεκτρομηχανικούς ηλεκτρονόμους (ρελέ) και δυαδική αριθμητική κινητής υποδιαστολής.",
    "funFacts": [
      "Το 1998 αποδείχθηκε μαθηματικά ότι ο υπολογιστής Z3 ήταν πλήρης κατά Turing (Turing-complete).",
      "Επινόησε επίσης το 1945 την Plankalkül, την πρώτη θεωρητική γλώσσα προγραμματισμού υψηλού επιπέδου στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CE%BD%CF%81%CE%B1%CE%BD%CF%84_%CE%A4%CF%83%CE%BF%CF%8D%CE%B6%CE%B5",
    "locale": "el-GR",
    "tags": ["zuse", "z3", "history-tech", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_124",
    "text": "Ποιος Αμερικανός φυσικός και πρωτοπόρος των υπολογιστών ηγήθηκε της κατασκευής του ηλεκτρομηχανικού υπολογιστή Harvard Mark I (IBM ASCC) το 1944;",
    "answers": ["Τζον φον Νόιμαν", "Χάουαρντ Έικεν", "Τζ. Πρέσπερ Έκερτ", "Νόρμπερτ Βίνερ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Χάουαρντ Έικεν (Howard Aiken) σχεδίασε τον Harvard Mark I σε συνεργασία με μηχανικούς της IBM, δημιουργώντας μια γιγαντιαία ηλεκτρομηχανική αριθμομηχανή μήκους 16 μέτρων.",
    "funFacts": [
      "Η Γκρέις Χόπερ ήταν μία από τους πρώτους προγραμματιστές του Mark I και έγραψε το πρώτο εγχειρίδιο χρήσης του μηχανήματος.",
      "Χρησιμοποιήθηκε εκτενώς από το Πολεμικό Ναυτικό των ΗΠΑ κατά τον Β' Παγκόσμιο Πόλεμο και για υπολογισμούς του Σχεδίου Μανχάταν."
    ],
    "source": "https://el.wikipedia.org/wiki/Harvard_Mark_I",
    "locale": "el-GR",
    "tags": ["mark-i", "howard-aiken", "harvard", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_125",
    "text": "Ποιοι δύο εφευρέτες κατασκεύασαν τον υπολογιστή Atanasoff-Berry (ABC) μεταξύ 1939 και 1942, ο οποίος εισήγαγε τη χρήση πυκνωτών ως δυναμική μνήμη RAM;",
    "answers": ["Τζ. Πρέσπερ Έκερτ και Τζον Μόκλι", "Άλαν Τιούρινγκ και Τόμι Φλάουερς", "Τζον Ατανάσοφ και Κλίφορντ Μπέρι", "Κόνραντ Τσούζε και Χέλμουτ Σράγιερ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο καθηγητής Τζον Ατανάσοφ (βουλγαρικής καταγωγής) και ο φοιτητής του Κλίφορντ Μπέρι κατασκεύασαν τον πρώτο ηλεκτρονικό ψηφιακό υπολογιστή ειδικού σκοπού στο Iowa State College.",
    "funFacts": [
      "Το 1973, μια ιστορική απόφαση ομοσπονδιακού δικαστηρίου των ΗΠΑ ακύρωσε την πατέντα του ENIAC, αναγνωρίζοντας τον Ατανάσοφ ως τον αρχικό εφευρέτη του ηλεκτρονικού ψηφιακού υπολογιστή.",
      "Χρησιμοποιούσε περιστρεφόμενο τύμπανο με πυκνωτές που ανανεώνονταν περιοδικά, εισάγοντας τη θεμελιώδη αρχή λειτουργίας της σύγχρονης μνήμης DRAM."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE%CF%82_%CE%91%CF%84%CE%B1%CE%BD%CE%AC%CF%83%CE%BF%CF%86-%CE%9C%CF%80%CE%AD%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["atanasoff", "abc-computer", "history-tech", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_126",
    "text": "Ποιος ήταν ο πρώτος εμπορικά παραγόμενος ψηφιακός υπολογιστής στις ΗΠΑ, ο οποίος έγινε παγκοσμίως διάσημος όταν προέβλεψε την εκλογική νίκη του Αϊζενχάουερ το 1952;",
    "answers": ["ENIAC", "IBM 701", "EDVAC", "UNIVAC I"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο UNIVAC I (Universal Automatic Computer I) σχεδιάστηκε από τους Τζ. Πρέσπερ Έκερτ και Τζον Μόκλι και παραδόθηκε αρχικά στο Γραφείο Απογραφής των ΗΠΑ το 1951.",
    "funFacts": [
      "Στις προεδρικές εκλογές του 1952 για το δίκτυο CBS, ο UNIVAC προέβλεψε συντριπτική νίκη του Αϊζενχάουερ με βάση μόλις το 7% των ψήφων, αλλά οι υπεύθυνοι δίστασαν αρχικά να μεταδώσουν το αποτέλεσμα επειδή οι δημοσκοπήσεις έδειχναν αμφίρροπη μάχη.",
      "Χρησιμοποιούσε μαγνητικές μεταλλικές ταινίες πλάτους μισής ίντσας αντί για διάτρητες κάρτες, επιτυγχάνοντας ταχύτατη ανάγνωση δεδομένων."
    ],
    "source": "https://el.wikipedia.org/wiki/UNIVAC_I",
    "locale": "el-GR",
    "tags": ["univac", "history-tech", "computers", "eckert-mauchly"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_127",
    "text": "Ποια πρωτοπόρος επιστήμονας υπολογιστών ηγήθηκε της ομάδας του MIT που ανέπτυξε το λογισμικό πτήσης για τις επανδρωμένες αποστολές Apollo στη Σελήνη;",
    "answers": ["Μάργκαρετ Χάμιλτον", "Γκρέις Χόπερ", "Κάθριν Τζόνσον", "Άντα Λάβλεϊς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η Μάργκαρετ Χάμιλτον (Margaret Hamilton) ήταν διευθύντρια του τμήματος μηχανικής λογισμικού του MIT Instrumentation Laboratory για το διαστημικό πρόγραμμα Apollo.",
    "funFacts": [
      "Επινόησε τον ίδιο τον όρο 'Software Engineering' (Μηχανική Λογισμικού) για να αποδώσει στο λογισμικό τον σεβασμό και την επιστημονική αυστηρότητα άλλων κλάδων μηχανικής.",
      "Μια διάσημη ιστορική φωτογραφία του 1969 τη δείχνει να στέκεται δίπλα σε μια στοίβα εκτυπωμένου πηγαίου κώδικα του Apollo Guidance Computer ψηλότερη από την ίδια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CF%81%CE%B3%CE%BA%CE%B1%CF%81%CE%B5%CF%84_%CE%A7%CE%AC%CE%BC%CE%B9%CE%BB%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["margaret-hamilton", "apollo", "nasa", "software-engineering"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_128",
    "text": "Τι είδους ανθεκτική χειροποίητη μνήμη ROM χρησιμοποιούσε ο υπολογιστής πλοήγησης Apollo Guidance Computer (AGC) στο διαστημόπλοιο Apollo 11;",
    "answers": ["Μαγνητική ταινία", "Μνήμη πυρήνων με σύρματα (Core rope memory)", "Οπτικό δίσκο", "Λυχνίες υδραργύρου"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η μνήμη Core rope memory κατασκευαζόταν με το χέρι πλέκοντας χάλκινα καλώδια μέσα από ή γύρω από μαγνητικούς φεριτικούς δακτυλίους (πυρήνες), αντιπροσωπεύοντας 1 ή 0.",
    "funFacts": [
      "Η μέθοδος κατασκευής απαιτούσε εξαιρετική ακρίβεια και ανατέθηκε σε έμπειρες εργάτριες κλωστοϋφαντουργίας, γι' αυτό και το λογισμικό ονομαζόταν χαριτολογώντας 'LOL memory' (Little Old Lady memory).",
      "Ήταν σχεδόν άφθαρτη και δεν μπορούσε να αλλοιωθεί από ηλεκτρικές διακοπές ή κοσμική ακτινοβολία κατά τη διάρκεια της αποστολής στη Σελήνη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE%CF%82_%CE%BA%CE%B1%CE%B8%CE%BF%CE%B4%CE%AE%CE%B3%CE%B7%CF%83%CE%B7%CF%82_%CE%86%CF%80%CE%BF%CE%BB%CE%BB%CE%BF",
    "locale": "el-GR",
    "tags": ["apollo-computer", "core-rope-memory", "nasa", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_129",
    "text": "Ποιο ήταν το φιλόδοξο εθνικό έργο της Σοβιετικής Ένωσης τη δεκαετία του 1960 υπό τον Βίκτορ Γκλουσκόφ για τη διασύνδεση των κρατικών υπολογιστών σε ένα ενιαίο δίκτυο;",
    "answers": ["InterNiet", "Sputnik-Net", "OGAS", "Glavlit"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το OGAS (Πανεθνικό Αυτοματοποιημένο Σύστημα) σχεδιάστηκε για τον κεντρικό ψηφιακό σχεδιασμό και διαχείριση της σοβιετικής οικονομίας, αλλά εγκαταλείφθηκε λόγω γραφειοκρατικών ανταγωνισμών.",
    "funFacts": [
      "Προέβλεπε ένα ιεραρχικό δίκτυο χιλιάδων υπολογιστικών κέντρων συνδεδεμένων σε πραγματικό χρόνο δεκαετίες πριν από το εμπορικό διαδίκτυο.",
      "Το σοβιετικό Υπουργείο Οικονομικών πολέμησε το έργο επειδή φοβόταν ότι θα έχανε τον έλεγχο των κονδυλίων υπέρ των μηχανικών πληροφορικής."
    ],
    "source": "https://el.wikipedia.org/wiki/OGAS",
    "locale": "el-GR",
    "tags": ["ogas", "soviet-union", "networking", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_130",
    "text": "Ποιο πρωτοποριακό εθνικό δίκτυο ηλεκτρονικών τερματικών λειτούργησε με τεράστια επιτυχία στη Γαλλία από το 1982 έως το 2012 προσφέροντας online κρατήσεις εισιτηρίων, τηλεφωνικούς καταλόγους και μηνύματα;",
    "answers": ["Ceefax", "Prestel", "Teletel", "Minitel"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Minitel διανεμήθηκε δωρεάν από τη γαλλική PTT σε εκατομμύρια νοικοκυριά αντί για έντυπους τηλεφωνικούς καταλόγους, δημιουργώντας το πρώτο μαζικό δίκτυο ηλεκτρονικού εμπορίου στον κόσμο.",
    "funFacts": [
      "Στην ακμή του εξυπηρετούσε πάνω από 25 εκατομμύρια χρήστες στη Γαλλία με σχεδόν 26.000 διαφορετικές διαθέσιμες ψηφιακές υπηρεσίες.",
      "Η τεράστια επιτυχία του Minitel καθυστέρησε αρχικά την υιοθέτηση του Παγκόσμιου Ιστού (World Wide Web) στη Γαλλία κατά τη δεκαετία του 1990."
    ],
    "source": "https://el.wikipedia.org/wiki/Minitel",
    "locale": "el-GR",
    "tags": ["minitel", "france", "telecommunications", "history-tech"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_131",
    "text": "Ποιο εργαλείο που αναπτύχθηκε το 1990 από τον Άλαν Έμτατζ στο Πανεπιστήμιο ΜακΓκιλ θεωρείται ιστορικά η πρώτη μηχανή αναζήτησης στο διαδίκτυο;",
    "answers": ["Archie", "Veronica", "Gopher", "Yahoo!"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Archie δημιουργήθηκε για να ευρετηριάζει αυτόματα τα περιεχόμενα ανώνυμων διακομιστών αρχείων FTP επιτρέποντας στους χρήστες να εντοπίζουν αρχεία στο πρώιμο διαδίκτυο.",
    "funFacts": [
      "Το όνομα προήλθε από τη λέξη 'archive' παραλείποντας το γράμμα 'v'.",
      "Ενέπνευσε τη δημιουργία μεταγενέστερων εργαλείων με ονόματα χαρακτήρων κόμικ, όπως το Veronica και το Jughead για το πρωτόκολλο Gopher."
    ],
    "source": "https://el.wikipedia.org/wiki/Archie_(%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE_%CE%B1%CE%BD%CE%B1%CE%B6%CE%AE%CF%84%CE%B7%CF%83%CE%B7%CF%82)",
    "locale": "el-GR",
    "tags": ["archie", "search-engines", "internet-history", "ftp"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_132",
    "text": "Από πού πήρε το όνομά του ο θεμελιώδης αλγόριθμος κατάταξης ιστοσελίδων «PageRank» της μηχανής αναζήτησης Google;",
    "answers": ["Από τον αριθμό των ιστοσελίδων (web pages)", "Από τον συνιδρυτή της Google, Λάρι Πέιτζ", "Από την εταιρεία σελιδοποίησης Page Corp", "Από την αγγλική έννοια της τηλεειδοποίησης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο αλγόριθμος PageRank πήρε το όνομά του από τον Λάρι Πέιτζ (Larry Page), ο οποίος τον κατοχύρωσε το 1998 στο Πανεπιστήμιο Στάνφορντ.",
    "funFacts": [
      "Αντιμετωπίζει τους υπερσυνδέσμους (links) προς μια σελίδα σαν θετικές ψήφους εμπιστοσύνης, σταθμίζοντας την αξία κάθε ψήφου με βάση τη σημασία της σελίδας που παραπέμπει.",
      "Το Πανεπιστήμιο Στάνφορντ έλαβε μετοχές της Google σε αντάλλαγμα για την παραχώρηση της πατέντας του PageRank, τις οποίες πούλησε αργότερα για πάνω από 330 εκατομμύρια δολάρια."
    ],
    "source": "https://el.wikipedia.org/wiki/PageRank",
    "locale": "el-GR",
    "tags": ["pagerank", "google", "larry-page", "algorithms"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_133",
    "text": "Πόσες διακριτές λογικές ομάδες διακομιστών ρίζας (root name servers, ονομασμένες από a.root-servers.net έως m.root-servers.net) υπάρχουν στην κορυφή του ιεραρχικού δέντρου του DNS;",
    "answers": ["7", "10", "13", "26"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Υπάρχουν ακριβώς 13 λογικές διευθύνσεις διακομιστών ρίζας DNS (από το Α έως το Μ) λόγω του ορίου μεγέθους 512 bytes σε απλά πακέτα DNS πάνω από UDP.",
    "funFacts": [
      "Παρότι οι λογικές διευθύνσεις είναι 13, στην πραγματικότητα υπάρχουν πάνω από 1.500 φυσικοί διακομιστές διασκορπισμένοι σε όλο τον κόσμο χάρη στην τεχνολογία Anycast.",
      "Διαχειρίζονται από διάφορους ανεξάρτητους οργανισμούς, όπως το ICANN, το Πανεπιστήμιο της Νότιας Καλιφόρνιας (ISI), ο αμερικανικός στρατός και η NASA."
    ],
    "source": "https://el.wikipedia.org/wiki/DNS",
    "locale": "el-GR",
    "tags": ["dns", "root-servers", "networking", "internet-infrastructure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_134",
    "text": "Ποιο κρίσιμο πρωτόκολλο εξωτερικής πύλης (Exterior Gateway Protocol) αποτελεί το «ταχυδρομείο» του διαδικτύου, ανταλλάσσοντας διαδρομές ανάμεσα σε Αυτόνομα Συστήματα (AS);",
    "answers": ["OSPF", "RIP", "IS-IS", "BGP (Border Gateway Protocol)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το BGP είναι το θεμελιώδες πρωτόκολλο δρομολόγησης που ενώνει τους μεγάλους παρόχους διαδικτύου (ISPs) και επιτρέπει στα δεδομένα να ταξιδεύουν παγκοσμίως.",
    "funFacts": [
      "Σφάλματα ρυθμίσεων στο BGP (BGP misconfigurations) έχουν προκαλέσει ιστορικά τις μεγαλύτερες παγκόσμιες διακοπές υπηρεσιών διαδικτύου, όπως το πολύωρο μπλακάουτ του Facebook και του Instagram το 2021.",
      "Σχεδιάστηκε αρχικά το 1989 από τους Κερκ Λάουγκιντ και Γιακόβ Ρέκτερ πάνω σε τρεις χαρτοπετσέτες κατά τη διάρκεια συνεδρίου του IETF."
    ],
    "source": "https://el.wikipedia.org/wiki/Border_Gateway_Protocol",
    "locale": "el-GR",
    "tags": ["bgp", "networking", "routing", "internet-infrastructure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_135",
    "text": "Ποιο κλασικό εργαλείο διάγνωσης δικτύου εκμεταλλεύεται το πεδίο TTL (Time to Live) των πακέτων IP για να καταγράψει διαδοχικά όλους τους ενδιάμεσους δρομολογητές;",
    "answers": ["Traceroute", "Ping", "Netstat", "Nslookup"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Traceroute στέλνει πακέτα με σταδιακά αυξανόμενο TTL (1, 2, 3...) αναγκάζοντας κάθε ενδιάμεσο δρομολογητή να επιστρέψει μήνυμα ICMP Time Exceeded.",
    "funFacts": [
      "Γράφτηκε αρχικά το 1988 από τον Βαν Τζέικομπσον για να εντοπίζει σημεία συμφόρησης και προβλήματα δρομολόγησης στο διαδίκτυο.",
      "Στα συστήματα Unix/Linux καλείται ως 'traceroute', ενώ στα Windows η εντολή στη γραμμή εντολών είναι 'tracert'."
    ],
    "source": "https://el.wikipedia.org/wiki/Traceroute",
    "locale": "el-GR",
    "tags": ["traceroute", "networking", "diagnostics", "icmp"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_136",
    "text": "Ποια τεχνολογία δικτύωσης επιτρέπει σε δεκάδες συσκευές ενός οικιακού δικτύου να μοιράζονται μία μόνο δημόσια διεύθυνση IPv4 τροποποιώντας τις θύρες στα πακέτα;",
    "answers": ["DHCP", "NAT / NAPT (Network Address Translation)", "DNS", "VLAN"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το NAT μεταφράζει τις ιδιωτικές μη δρομολογήσιμες διευθύνσεις (όπως 192.168.x.x) σε μία ενιαία δημόσια διεύθυνση IP του παρόχου, παρατείνοντας τη ζωή του IPv4 για δεκαετίες.",
    "funFacts": [
      "Ορίστηκε αρχικά στο RFC 1631 το 1994 ως προσωρινή λύση έκτακτης ανάγκης μέχρι να υιοθετηθεί το IPv6.",
      "Παρέχει επίσης ένα βασικό επίπεδο ασφάλειας, καθώς αποτρέπει την απευθείας εξωτερική σύνδεση αγνώστων προς τις εσωτερικές συσκευές του σπιτιού."
    ],
    "source": "https://el.wikipedia.org/wiki/NAT",
    "locale": "el-GR",
    "tags": ["nat", "networking", "ip-addresses", "routers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_137",
    "text": "Τι δηλώνει η ένδειξη /24 στη σημειογραφία CIDR στο τέλος μιας διεύθυνσης δικτύου (όπως 192.168.1.0/24);",
    "answers": ["Ότι το δίκτυο έχει 24 διαθέσιμους διακομιστές", "Ότι η ταχύτητα είναι 24 Mbps", "Ότι τα πρώτα 24 bits είναι δεσμευμένα για τη μάσκα δικτύου (255.255.255.0)", "Ότι το δίκτυο λειτουργεί σε συχνότητα 2,4 GHz"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Στη σημειογραφία CIDR (Classless Inter-Domain Routing), ο αριθμός μετά την κάθετο δείχνει πόσα bits ανήκουν στο πρόθεμα δικτύου, αφήνοντας 8 bits (256 διευθύνσεις) για τις συσκευές.",
    "funFacts": [
      "Από τις 256 διευθύνσεις ενός δικτύου /24, δύο δεν μπορούν να αποδοθούν σε συσκευές: η πρώτη (.0) που ορίζει το ίδιο το δίκτυο και η τελευταία (.255) που είναι η διεύθυνση εκπομπής (broadcast).",
      "Το CIDR εισήχθη το 1993 αντικαθιστώντας το παλιό άκαμπτο σύστημα των κλάσεων δικτύου (Class A, B, C)."
    ],
    "source": "https://el.wikipedia.org/wiki/CIDR",
    "locale": "el-GR",
    "tags": ["cidr", "networking", "ip-address", "subnets"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_138",
    "text": "Ποια ειδική διεύθυνση IPv4 προορίζεται αποκλειστικά για την αναδρομολόγηση της κυκλοφορίας πίσω στην ίδια την τοπική συσκευή (loopback / localhost);",
    "answers": ["192.168.1.1", "10.0.0.1", "255.255.255.255", "127.0.0.1"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ολόκληρο το μπλοκ 127.0.0.0/8 είναι δεσμευμένο για δοκιμές loopback, με τη διεύθυνση 127.0.0.1 να αντιστοιχεί παραδοσιακά στο όνομα συστήματος 'localhost'.",
    "funFacts": [
      "Τα πακέτα που αποστέλλονται στη διεύθυνση 127.0.0.1 δεν φτάνουν ποτέ στην κάρτα δικτύου αλλά αναστρέφονται αμέσως μέσα στον πυρήνα του συστήματος.",
      "Η διάσημη φράση των προγραμματιστών 'There's no place like 127.0.0.1' αποτελεί λογοπαίγνιο με το 'There's no place like home'."
    ],
    "source": "https://el.wikipedia.org/wiki/Localhost",
    "locale": "el-GR",
    "tags": ["localhost", "loopback", "networking", "ip"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_139",
    "text": "Πόσα bits μήκος έχει μια παγκόσμια μοναδική φυσική διεύθυνση υλικού MAC (Media Access Control) μιας κάρτας δικτύου;",
    "answers": ["48 bits", "32 bits", "64 bits", "128 bits"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Μια διεύθυνση MAC (επίπεδο 2 του μοντέλου OSI) αποτελείται από 48 bits (6 bytes) και αναπαρίσταται συνήθως με 12 δεκαεξαδικά ψηφία (π.χ. 00:1A:2B:3C:4D:5E).",
    "funFacts": [
      "Τα πρώτα 24 bits αποτελούν το αναγνωριστικό OUI (Organizationally Unique Identifier) που ταυτοποιεί τον κατασκευαστή του υλικού.",
      "Τα σύγχρονα smartphone χρησιμοποιούν τυχαίες διευθύνσεις MAC (MAC randomization) όταν αναζητούν δίκτυα Wi-Fi για να αποτρέψουν την ιχνηλάτηση της φυσικής θέσης του χρήστη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B5%CF%8D%CE%B8%CF%85%CE%BD%CF%83%CE%B7_MAC",
    "locale": "el-GR",
    "tags": ["mac-address", "networking", "hardware", "ethernet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_140",
    "text": "Ποιο είναι το τυπικό μέγιστο μέγεθος μονάδας μετάδοσης (MTU) σε bytes για ένα κλασικό πλαίσιο δεδομένων Ethernet στο διαδίκτυο;",
    "answers": ["512 bytes", "1.500 bytes", "4.096 bytes", "9.000 bytes"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το πρότυπο Ethernet ορίζει μέγιστο ωφέλιμο φορτίο (MTU) 1.500 bytes. Πακέτα μεγαλύτερα από το MTU πρέπει να κατακερματιστούν (fragmentation).",
    "funFacts": [
      "Σε ειδικά τοπικά δίκτυα υψηλής ταχύτητας υποστηρίζονται τα λεγόμενα 'Jumbo frames' με MTU έως 9.000 bytes για μείωση του φόρτου του επεξεργαστή.",
      "Το πρωτόκολλο IPv6 απαγορεύει στους ενδιάμεσους δρομολογητές να κατακερματίζουν πακέτα, απαιτώντας ο κατακερματισμός να γίνεται αποκλειστικά από τον αποστολέα."
    ],
    "source": "https://el.wikipedia.org/wiki/Maximum_transmission_unit",
    "locale": "el-GR",
    "tags": ["mtu", "networking", "ethernet", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_141",
    "text": "Ποιο σύγχρονο κρυπτογραφικό πρωτόκολλο επικοινωνίας αντικατέστησε οριστικά το παλαιότερο και επισφαλές πρότυπο SSL (Secure Sockets Layer);",
    "answers": ["SSH", "IPsec", "TLS (Transport Layer Security)", "PGP"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το TLS είναι ο άμεσος διάδοχος του SSL, με το TLS 1.0 να τυποποιείται το 1999 και τις σύγχρονες εκδόσεις TLS 1.2 και TLS 1.3 να προστατεύουν όλη την κίνηση HTTPS.",
    "funFacts": [
      "Παρόλο που το SSL θεωρείται επίσημα απαρχαιωμένο και ανασφαλές από το 2015, ο όρος 'πιστοποιητικό SSL' χρησιμοποιείται ακόμα ευρέως από συνήθεια.",
      "Το νεότερο TLS 1.3 μείωσε τη διαδικασία χειραψίας (handshake) σε μόλις ένα round-trip (1-RTT), επιταχύνοντας σημαντικά τη φόρτωση των ασφαλών σελίδων."
    ],
    "source": "https://el.wikipedia.org/wiki/Transport_Layer_Security",
    "locale": "el-GR",
    "tags": ["tls", "ssl", "cryptography", "security"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_142",
    "text": "Πώς ονομάζεται ένας αξιόπιστος τρίτος φορέας που εκδίδει και υπογράφει ψηφιακά πιστοποιητικά για την επαλήθευση της ταυτότητας ιστοτόπων στο διαδίκτυο;",
    "answers": ["Πάροχος διαδικτύου (ISP)", "Διαχειριστής τομέα (DNS Registrar)", "Τείχος προστασίας", "Αρχή Πιστοποίησης (Certificate Authority - CA)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Μια Αρχή Πιστοποίησης (CA) ελέγχει την κυριότητα ενός domain name και εκδίδει το ψηφιακό πιστοποιητικό που εμπιστεύονται οι περιηγητές ιστού.",
    "funFacts": [
      "Ο μη κερδοσκοπικός οργανισμός Let's Encrypt ξεκίνησε το 2015 παρέχοντας δωρεάν αυτοματοποιημένα πιστοποιητικά, εκτοξεύοντας τη χρήση του HTTPS παγκοσμίως πάνω από το 90%.",
      "Τα λειτουργικά συστήματα και οι browsers διατηρούν έναν προεγκατεστημένο κατάλογο 'έμπιστων ριζικών πιστοποιητικών' (Root CAs)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%81%CF%87%CE%AE_%CE%A0%CE%B9%CF%83%CF%84%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["certificate-authority", "tls", "security", "https"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_143",
    "text": "Ποιο σύστημα κανόνων, τεχνολογιών και διαδικασιών διαχειρίζεται τη δημιουργία, διανομή και ανάκληση ψηφιακών πιστοποιητικών δημόσιου κλειδιού;",
    "answers": ["Υποδομή Δημοσίου Κλειδιού (PKI)", "Σύστημα Ανίχνευσης Εισβολών (IDS)", "Εικονικό Ιδιωτικό Δίκτυο (VPN)", "Ενιαία Σύνδεση (SSO)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η PKI (Public Key Infrastructure) διασφαλίζει ότι ένα δημόσιο κλειδί ανήκει πραγματικά στην οντότητα που ισχυρίζεται, αποτρέποντας επιθέσεις πλαστοπροσωπίας.",
    "funFacts": [
      "Το πρότυπο X.509 αποτελεί τη διεθνή προδιαγραφή μορφοποίησης των ψηφιακών πιστοποιητικών δημόσιου κλειδιού.",
      "Περιλαμβάνει μηχανισμούς ανάκλησης πιστοποιητικών, όπως τις λίστες CRL και το πρωτόκολλο OCSP σε πραγματικό χρόνο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%B4%CE%BF%CE%BC%CE%AE_%CE%B4%CE%B7%CE%BC%CF%8C%CF%83%CE%B9%CE%BF%CF%85_%CE%BA%CE%BB%CE%B5%CE%B9%CE%B4%CE%B9%CE%BF%CF%83",
    "locale": "el-GR",
    "tags": ["pki", "cryptography", "security", "certificates"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_144",
    "text": "Τι ορίζεται ως «ευπάθεια μηδενικής ημέρας» (Zero-day vulnerability) στον τομέα της κυβερνοασφάλειας;",
    "answers": ["Ένας ιός που καταστρέφει το σύστημα σε 24 ώρες", "Μια ευπάθεια ασφαλείας άγνωστη στον κατασκευαστή για την οποία δεν υπάρχει διαθέσιμη διόρθωση", "Ένα σφάλμα που συμβαίνει κατά την πρώτη ημέρα του έτους", "Ένας κωδικός που λήγει τα μεσάνυχτα"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ονομάζεται 'Zero-day' επειδή ο προγραμματιστής ή η εταιρεία έχει 'μηδέν ημέρες' για να τη διορθώσει, καθώς έχει ήδη εντοπιστεί ή αξιοποιηθεί από επιτιθέμενους.",
    "funFacts": [
      "Στη μαύρη και γκρίζα αγορά κυβερνοασφάλειας, άγνωστες ευπάθειες zero-day για λειτουργικά όπως το iOS και τα Windows πωλούνται για εκατομμύρια δολάρια.",
      "Οι εταιρείες λογισμικού οργανώνουν προγράμματα αμοιβών (Bug Bounty Programs) πληρώνοντας ηθικούς ερευνητές για να τους αποκαλύπτουν τέτοιες ευπάθειες πριν τις εκμεταλλευτούν κακόβουλοι χάκερς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%AF%CE%B8%CE%B5%CF%83%CE%B7_%CE%BC%CE%B7%CE%B4%CE%B5%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%B7%CE%BC%CE%AD%CF%81%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["zero-day", "security", "vulnerabilities", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_145",
    "text": "Πώς ονομάζεται ένα σκόπιμα ευάλωτο υπολογιστικό σύστημα-δόλωμα που τοποθετείται σε ένα δίκτυο για να παραπλανήσει και να καταγράψει τις μεθόδους των εισβολέων;",
    "answers": ["Sandbox", "Firewall", "Honeypot (δοχείο μελιού)", "Proxy"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το honeypot μιμείται πραγματικούς στόχους (όπως βάσεις δεδομένων ή διακομιστές) επιτρέποντας στους ειδικούς ασφαλείας να παρακολουθούν τις τεχνικές των χάκερς χωρίς κίνδυνο για τα πραγματικά δεδομένα.",
    "funFacts": [
      "Ένα δίκτυο πολλαπλών διασυνδεδεμένων honeypots ονομάζεται 'honeynet'.",
      "Επειδή το honeypot δεν έχει καμία νόμιμη παραγωγική λειτουργία, οποιαδήποτε απόπειρα σύνδεσης σε αυτό θεωρείται αυτομάτως ύποπτη ή κακόβουλη."
    ],
    "source": "https://el.wikipedia.org/wiki/Honeypot",
    "locale": "el-GR",
    "tags": ["honeypot", "security", "cybersecurity", "monitoring"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_146",
    "text": "Ποιος τύπος κυβερνοεπίθεσης περιγράφει την κατάσταση όπου ένας εισβολέας παρεμβάλλεται κρυφά ανάμεσα σε δύο συνομιλητές υποκλέπτοντας ή παραποιώντας τα μηνύματά τους;",
    "answers": ["DDoS", "Phishing", "Ransomware", "Επίθεση Ενδιάμεσου (Man-in-the-Middle)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Στην επίθεση Man-in-the-Middle (MitM), τα δύο μέρη πιστεύουν ότι επικοινωνούν απευθείας μεταξύ τους, ενώ στην πραγματικότητα όλη η κίνηση διέρχεται και ελέγχεται από τον επιτιθέμενο.",
    "funFacts": [
      "Μια συνηθισμένη μορφή επίθεσης MitM συμβαίνει σε δημόσια μη κρυπτογραφημένα δίκτυα Wi-Fi καφετεριών ή αεροδρομίων.",
      "Η κρυπτογράφηση άκρο-σε-άκρο (End-to-End Encryption) και ο έλεγχος ταυτότητας ψηφιακών πιστοποιητικών σχεδιάστηκαν ειδικά για να αποτρέπουν επιθέσεις MitM."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%AF%CE%B8%CE%B5%CF%83%CE%B7_%CE%B5%CE%BD%CE%B4%CE%B9%CE%AC%CE%BC%CE%B5%CF%83%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["mitm", "cybersecurity", "attacks", "networking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_147",
    "text": "Ποια κλασική τεχνική επίθεσης σε διαδικτυακές εφαρμογές εκμεταλλεύεται την κακή επικύρωση εισόδου για να εκτελέσει αυθαίρετες εντολές στη σχεσιακή βάση δεδομένων;",
    "answers": ["Έγχυση SQL (SQL Injection)", "Cross-Site Scripting", "Buffer Overflow", "Denial of Service"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το SQL Injection (SQLi) συμβαίνει όταν δεδομένα χρήστη (π.χ. σε μια φόρμα σύνδεσης) ερμηνεύονται ως εντολές SQL, επιτρέποντας την ανάγνωση ή διαγραφή ολόκληρης της βάσης δεδομένων.",
    "funFacts": [
      "Αποτελεί μία από τις παλαιότερες και πιο επικίνδυνες ευπάθειες ιστού, παραμένοντας σταθερά στην κορυφή του καταλόγου OWASP Top 10.",
      "Η χρήση παραμετροποιημένων ερωτημάτων (Prepared Statements) αποτρέπει πλήρως τις επιθέσεις SQL injection διαχωρίζοντας τα δεδομένα από τις εντολές."
    ],
    "source": "https://el.wikipedia.org/wiki/SQL_injection",
    "locale": "el-GR",
    "tags": ["sql-injection", "security", "databases", "owasp"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_148",
    "text": "Ποια διαδεδομένη ευπάθεια διαδικτυακών εφαρμογών επιτρέπει σε εισβολείς να εισάγουν κακόβουλα σενάρια JavaScript που εκτελούνται στον περιηγητή ανυποψίαστων χρηστών;",
    "answers": ["SQL Injection", "Cross-Site Scripting (XSS)", "Directory Traversal", "CSRF"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Στις επιθέσεις XSS, ο ιστότοπος εμφανίζει μη ελεγμένα δεδομένα εισόδου άλλων χρηστών, επιτρέποντας την εκτέλεση κακόβουλης JavaScript για υποκλοπή cookies και συνδέσεων.",
    "funFacts": [
      "Διακρίνεται σε Stored XSS (όταν ο κακόβουλος κώδικας αποθηκεύεται μόνιμα στη βάση, π.χ. σε σχόλιο) και Reflected XSS (όταν ανακλάται απευθείας από αίτημα).",
      "Η σωστή κωδικοποίηση εξόδου HTML (HTML entity encoding) και οι πολιτικές ασφάλειας περιεχομένου (CSP) προστατεύουν από επιθέσεις XSS."
    ],
    "source": "https://el.wikipedia.org/wiki/Cross-site_scripting",
    "locale": "el-GR",
    "tags": ["xss", "web-security", "javascript", "owasp"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_149",
    "text": "Ποιο κρίσιμο σφάλμα διαχείρισης μνήμης σε γλώσσες όπως η C/C++ συμβαίνει όταν ένα πρόγραμμα γράφει δεδομένα πέρα από τα όρια ενός πίνακα μνήμης;",
    "answers": ["Null Pointer Dereference", "Memory Leak", "Υπερχείλιση προσωρινής μνήμης (Buffer Overflow)", "Race Condition"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το buffer overflow μπορεί να αλλοιώσει παρακείμενες διευθύνσεις μνήμης και τη διεύθυνση επιστροφής της στοίβας (return address), επιτρέποντας την εκτέλεση αυθαίρετου κώδικα.",
    "funFacts": [
      "Το ιστορικό άρθρο 'Smashing The Stack For Fun And Profit' του Aleph One στο περιοδικό Phrack το 1996 καθιέρωσε τις τεχνικές εκμετάλλευσης buffer overflow.",
      "Σύγχρονα λειτουργικά συστήματα χρησιμοποιούν προστασίες όπως ASLR (τυχαιοποίηση διευθύνσεων μνήμης) και Stack Canaries για να αποτρέψουν τέτοιες επιθέσεις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%B5%CF%81%CF%87%CE%B5%CE%AF%CE%BB%CE%B9%CF%83%CE%B7_%CE%B5%CE%BD%CF%84%CE%B1%CE%BC%CE%B9%CE%B5%CF%85%CF%84%CE%AE",
    "locale": "el-GR",
    "tags": ["buffer-overflow", "security", "memory", "c-language"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_150",
    "text": "Ποιος όρος περιγράφει την τεχνική ασφαλείας κατά την οποία μια εφαρμογή εκτελείται μέσα σε ένα αυστηρά απομονωμένο περιβάλλον με περιορισμένη πρόσβαση στο σύστημα αρχείων;",
    "answers": ["Virtualization", "Emulation", "Containerization", "Sandboxing (Αμμοδοχείο)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το sandboxing περιορίζει τα δικαιώματα μιας διεργασίας (π.χ. μιας καρτέλας περιηγητή ή μιας εφαρμογής κινητού) ώστε ακόμα κι αν παραβιαστεί, να μην μπορεί να βλάψει το υπόλοιπο λειτουργικό σύστημα.",
    "funFacts": [
      "Κάθε εφαρμογή στο iOS και στο Android εκτελείται υποχρεωτικά μέσα στο δικό της ξεχωριστό sandbox.",
      "Τα σύγχρονα προγράμματα περιήγησης (όπως το Chrome) εκτελούν κάθε ιστοσελίδα και πρόσθετο σε ξεχωριστή απομονωμένη διεργασία sandbox."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BC%CE%BC%CE%BF%CE%B4%CE%BF%CF%87%CE%B5%CE%AF%CE%BF_(%CE%B1%CF%83%CF%86%CE%AC%CE%BB%CE%B5%CE%B9%CE%B1_%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["sandboxing", "security", "operating-systems", "isolation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_151",
    "text": "Πώς ονομάζεται ο προνομιούχος χώρος διευθύνσεων μνήμης όπου εκτελείται ο πυρήνας ενός λειτουργικού συστήματος με πλήρη, ανεμπόδιστη πρόσβαση στο φυσικό υλικό;",
    "answers": ["Χώρος πυρήνα (Kernel space)", "Χώρος χρήστη (User space)", "Εικονικός χώρος", "Προσωρινός χώρος"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο διαχωρισμός σε Kernel space και User space προστατεύει το λειτουργικό σύστημα, καθώς οι κοινές εφαρμογές χρηστών δεν μπορούν να τροποποιήσουν απευθείας ευαίσθητες δομές του πυρήνα.",
    "funFacts": [
      "Όταν μια εφαρμογή χρειάζεται να διαβάσει ένα αρχείο ή να στείλει δεδομένα στο δίκτυο, πραγματοποιεί μια 'κλήση συστήματος' (system call) περνώντας προσωρινά τον έλεγχο στον πυρήνα.",
      "Σφάλμα σε κώδικα που εκτελείται στον χώρο του πυρήνα προκαλεί κατάρρευση ολόκληρου του λειτουργικού συστήματος (Kernel Panic στο Linux/Mac ή Blue Screen στα Windows)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%85%CF%81%CE%AE%CE%BD%CE%B1%CF%82_(%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%AE)",
    "locale": "el-GR",
    "tags": ["kernel-space", "operating-systems", "memory", "architecture"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_152",
    "text": "Ποια αρχιτεκτονική πυρήνα λειτουργικού συστήματος εκτελεί σχεδόν όλες τις βασικές υπηρεσίες (οδηγούς, σύστημα αρχείων, διαχείριση μνήμης) στον ενιαίο χώρο του πυρήνα (όπως το Linux);",
    "answers": ["Μικροπυρήνας (Microkernel)", "Μονολιθικός πυρήνας (Monolithic kernel)", "Εξωπυρήνας (Exokernel)", "Υβριδικός πυρήνας"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο μονολιθικός πυρήνας εκτελεί όλες τις διεργασίες του λειτουργικού συστήματος στον ίδιο χώρο διευθύνσεων, επιτυγχάνοντας μέγιστη ταχύτητα επικοινωνίας χωρίς το κόστος εναλλαγής περιβάλλοντος.",
    "funFacts": [
      "Το 1992 ξέσπασε η περίφημη δημόσια διαμάχη Tanenbaum-Torvalds, όπου ο καθηγητής Άντριου Τανενμπάουμ υποστήριξε ότι το Linux ήταν απαρχαιωμένο επειδή χρησιμοποίησε μονολιθικό πυρήνα αντί για μικροπυρήνα.",
      "Παρά την κριτική, οι μονολιθικοί πυρήνες παραμένουν οι ταχύτεροι και πιο διαδεδομένοι στην πράξη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%BF%CE%BB%CE%B9%CE%B8%CE%B9%CE%BA%CF%8C%CF%82_%CF%80%CF%85%CF%81%CE%AE%CE%BD%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["monolithic-kernel", "linux", "operating-systems", "architecture"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_153",
    "text": "Σε ποιον ιστορικό μικροπυρήνα (microkernel) που αναπτύχθηκε στο Πανεπιστήμιο Carnegie Mellon βασίζεται ο υβριδικός πυρήνας XNU των λειτουργικών συστημάτων της Apple (macOS, iOS);",
    "answers": ["L4", "QNX", "Mach", "Minix"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο πυρήνας Mach αναπτύχθηκε από τον Ρικ Ρασίντ και τους συνεργάτες του στο CMU τη δεκαετία του 1980 και ενσωματώθηκε στο σύστημα NeXTSTEP και στη συνέχεια στο macOS.",
    "funFacts": [
      "Ο πυρήνας της Apple ονομάζεται XNU, ένα αναδρομικό ακρωνύμιο που σημαίνει 'X is Not Unix'.",
      "Συνδυάζει την αρχιτεκτονική μηνυμάτων του Mach με υποσυστήματα του FreeBSD και το περιβάλλον οδηγών I/O Kit σε έναν ενιαίο υβριδικό σχεδιασμό."
    ],
    "source": "https://el.wikipedia.org/wiki/Mach_(%CF%80%CF%85%CF%81%CE%AE%CE%BD%CE%B1%CF%82)",
    "locale": "el-GR",
    "tags": ["mach", "apple", "macos", "kernels"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_154",
    "text": "Ποιος βασικός μηχανισμός των λειτουργικών συστημάτων επεκτείνει τη διαθέσιμη μνήμη RAM αποθηκεύοντας προσωρινά αδρανή μπλοκ δεδομένων στον σκληρό δίσκο;",
    "answers": ["Κατακερματισμός", "Συντονισμός διαύλου", "Υπερχρονισμός", "Εικονική μνήμη (Virtual memory)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Η εικονική μνήμη χρησιμοποιεί τη μονάδα διαχείρισης μνήμης (MMU) του επεξεργαστή για να αντιστοιχίζει εικονικές διευθύνσεις σε φυσική RAM ή σε ειδικό χώρο εναλλαγής στον δίσκο (swap space / pagefile).",
    "funFacts": [
      "Επιτρέπει σε προγράμματα να εκτελούνται ακόμα κι αν απαιτούν περισσότερη μνήμη από τη φυσικά εγκατεστημένη RAM του υπολογιστή.",
      "Η έννοια της εικονικής μνήμης με σελιδοποίηση επινοήθηκε αρχικά για τον βρετανικό υπερυπολογιστή Atlas στο Πανεπιστήμιο του Μάντσεστερ γύρω στο 1959."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B9%CE%BA%CE%BF%CE%BD%CE%B9%CE%BA%CE%AE_%CE%BC%CE%BD%CE%AE%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["virtual-memory", "paging", "operating-systems", "memory"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_155",
    "text": "Τι συμβαίνει όταν μια διεργασία προσπαθεί να διαβάσει μια σελίδα εικονικής μνήμης που δεν βρίσκεται φορτωμένη στη φυσική RAM αλλά έχει αποθηκευτεί στον δίσκο;",
    "answers": ["Σφάλμα σελίδας (Page fault)", "Διακοπή πυρήνα (Kernel Panic)", "Υπερχείλιση στοίβας (Stack overflow)", "Αδιέξοδο (Deadlock)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Page fault είναι μια φυσιολογική εξαίρεση υλικού που ειδοποιεί το λειτουργικό σύστημα να φέρει την απαιτούμενη σελίδα από τον δίσκο πίσω στη μνήμη RAM.",
    "funFacts": [
      "Αν η RAM είναι εντελώς γεμάτη και το σύστημα ξοδεύει όλο τον χρόνο του μεταφέροντας συνεχώς σελίδες μεταξύ RAM και δίσκου, η κατάσταση αυτή ονομάζεται 'thrashing'.",
      "Η εισαγωγή γρήγορων δίσκων SSD μείωσε δραστικά την καθυστέρηση που προκαλούν τα page faults σε σύγκριση με τους παλιούς μηχανικούς δίσκους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%86%CE%AC%CE%BB%CE%BC%CE%B1_%CF%83%CE%B5%CE%BB%CE%AF%CE%B4%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["page-fault", "virtual-memory", "operating-systems", "mmu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_156",
    "text": "Πώς ονομάζεται η παθολογική κατάσταση στα πολυνηματικά συστήματα όπου δύο ή περισσότερες διεργασίες μπλοκάρουν επ' αόριστον περιμένοντας πόρους που κατέχει η άλλη;",
    "answers": ["Αγώνας δρόμου (Race condition)", "Αδιέξοδο (Deadlock)", "Διαρροή μνήμης (Memory leak)", "Λιμοκτονία (Starvation)"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το αδιέξοδο (deadlock) συμβαίνει όταν πληρούνται ταυτόχρονα οι τέσσερις συνθήκες του Coffman: αμοιβαίος αποκλεισμός, κράτηση και αναμονή, μη ανάκληση και κυκλική αναμονή.",
    "funFacts": [
      "Ο Έντσγκερ Ντάικστρα περιέγραψε το πρόβλημα αυτό με τη διάσημη αλληγορία του 'Προβλήματος των Φιλοσόφων που Δειπνούν' (Dining Philosophers Problem).",
      "Τα λειτουργικά συστήματα χρησιμοποιούν αλγορίθμους όπως ο Αλγόριθμος του Τραπεζίτη (Banker's Algorithm) για να αποτρέπουν καταστάσεις αδιεξόδου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%B4%CE%B9%CE%AD%CE%BE%CE%BF%CE%B4%CE%BF_(%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%AE)",
    "locale": "el-GR",
    "tags": ["deadlock", "concurrency", "operating-systems", "algorithms"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_157",
    "text": "Ποιος πρωτοπόρος της επιστήμης υπολογιστών επινόησε την έννοια του «σηματοφόρου» (semaphore) το 1965 για τον έλεγχο πρόσβασης σε κοινόχρηστους πόρους;",
    "answers": ["Άλαν Τιούρινγκ", "Κ.Α.Ρ. Χορ", "Έντσγκερ Ντάικστρα", "Ντόναλντ Κνουθ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο Ντάικστρα εισήγαγε τον σηματοφόρο με τις δύο ατομικές λειτουργίες P (wait) και V (signal), από τις ολλανδικές λέξεις 'proberen' (δοκιμή) και 'verhogen' (αύξηση).",
    "funFacts": [
      "Ένας δυαδικός σηματοφόρος (με τιμές μόνο 0 και 1) λειτουργεί ως κλείδωμα αμοιβαίου αποκλεισμού (mutex - mutual exclusion).",
      "Εμπνεύστηκε την ονομασία από τους μηχανικούς σηματοφόρους των σιδηροδρόμων που ελέγχουν αν ένα τμήμα γραμμής είναι ελεύθερο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B7%CE%BC%CE%B1%CF%84%CE%BF%CF%86%CF%8C%CF%81%CE%BF%CF%82_(%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%AE)",
    "locale": "el-GR",
    "tags": ["semaphore", "dijkstra", "concurrency", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_158",
    "text": "Ποιος μηχανισμός αυτόματης απελευθέρωσης αχρησιμοποίητης δυναμικής μνήμης επινοήθηκε από τον Τζον Μακάρθι το 1959 για τη γλώσσα Lisp;",
    "answers": ["Χειροκίνητη απελευθέρωση (free/malloc)", "Έλεγχος δανεισμού (Borrow checker)", "Ανασυγκρότηση σωρού", "Αποκομιδή απορριμμάτων (Garbage Collection)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Το Garbage Collection (GC) απαλλάσσει τον προγραμματιστή από τη χειροκίνητη διαχείριση μνήμης, εντοπίζοντας και απελευθερώνοντας αυτόματα αντικείμενα που δεν χρησιμοποιούνται πλέον.",
    "funFacts": [
      "Ο αρχικός αλγόριθμος που επινόησε ο Μακάρθι ονομαζόταν 'Mark-and-Sweep' (Σημείωση και Σκούπισμα).",
      "Γλώσσες όπως η Java, η Python, η C# και η Go βασίζονται εξ ολοκλήρου σε εξελιγμένους αποκομιδείς απορριμμάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CE%BF%CE%BA%CE%BF%CE%BC%CE%B9%CE%B4%CE%AE_%CE%B1%CF%80%CE%BF%CF%81%CF%81%CE%B9%CE%BC%CE%BC%CE%AC%CF%84%CF%89%CE%BD_(%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%AE)",
    "locale": "el-GR",
    "tags": ["garbage-collection", "mccarthy", "memory", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_159",
    "text": "Ποιος τύπος μεταγλωττιστή μετατρέπει δυναμικά ενδιάμεσο κώδικα (bytecode) σε εγγενή κώδικα μηχανής ακριβώς κατά τη στιγμή της εκτέλεσης του προγράμματος;",
    "answers": ["Μεταγλωττιστής JIT (Just-In-Time)", "Προ-μεταγλωττιστής AOT (Ahead-Of-Time)", "Διερμηνέας (Interpreter)", "Διασυνδέτης (Linker)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο JIT μεταγλωττιστής συνδυάζει τη φορητότητα ενός διερμηνέα με την ταχύτητα μιας μεταγλωττισμένης γλώσσας, εντοπίζοντας συχνά εκτελούμενα τμήματα κώδικα ('hot spots') και μεταγλωττίζοντάς τα σε γλώσσα μηχανής.",
    "funFacts": [
      "Χρησιμοποιείται εκτεταμένα στην εικονική μηχανή HotSpot της Java, στην πλατφόρμα .NET (CLR) και στις μηχανές JavaScript (όπως η V8 του Chrome).",
      "Η πρώτη καταγεγραμμένη χρήση τεχνικής JIT αποδίδεται στον Τζον ΜακΚάρθι για τη γλώσσα LISP το 1960."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CF%84%CE%B1%CE%B3%CE%BB%CF%89%CF%84%CF%84%CE%B9%CF%83%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["jit", "compilers", "virtual-machine", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "tech_med_160",
    "text": "Πώς ονομάζεται η ενδιάμεση δυαδική αναπαράσταση εντολών που παράγει ο μεταγλωττιστής της Java (.class) ή της Python (.pyc) για εκτέλεση από μια εικονική μηχανή;",
    "answers": ["Machine code", "Bytecode", "Source code", "Assembly"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 3,
    "explanation": "Ο bytecode είναι ένα σύνολο εντολών βελτιστοποιημένο για αποδοτική εκτέλεση από έναν διερμηνέα λογισμικού ή εικονική μηχανή (όπως η JVM), ανεξάρτητα από το υλικό της συσκευής.",
    "funFacts": [
      "Ονομάζεται 'bytecode' επειδή κάθε κωδικός εντολής (opcode) έχει παραδοσιακά μήκος ενός byte (επιτρέποντας έως 256 διαφορετικές εντολές).",
      "Επιτρέπει στο ίδιο μεταγλωττισμένο αρχείο να εκτελείται χωρίς καμία αλλαγή σε Windows, Linux, macOS ή κινητά τηλέφωνα."
    ],
    "source": "https://el.wikipedia.org/wiki/Bytecode",
    "locale": "el-GR",
    "tags": ["bytecode", "jvm", "compilers", "virtual-machines"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'medium', 3, questions)

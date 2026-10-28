# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_med_061",
    "text": "Ποιος Γάλλος σκηνοθέτης υπέγραψε την ποιητική ρομαντική κομεντί «Αμελί» (Le Fabuleux Destin d'Amélie Poulain, 2001);",
    "answers": ["Ζαν-Πιερ Ζενέ", "Λικ Μπεσόν", "Φρανσουά Οζόν", "Ματιέ Κασοβίτς"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jean-Pierre Jeunet σκηνοθέτησε την 'Αμελί' με πρωταγωνίστρια την Audrey Tautou, αποσπώντας 5 υποψηφιότητες για Όσκαρ και 4 βραβεία Σεζάρ.",
    "funFacts": [
      "Η διάσημη μουσική της ταινίας συντέθηκε από τον Γιαν Τιερσέν (Yann Tiersen) χρησιμοποιώντας κυρίως ακορντεόν και πιάνο.",
      "Το καφέ 'Café des 2 Moulins' στη Μονμάρτρη όπου εργαζόταν η Αμελί έγινε πραγματικό τουριστικό αξιοθέατο του Παρισιού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BC%CE%B5%CE%BB%CE%AF",
    "locale": "el-GR",
    "tags": ["amelie", "jeunet", "french-cinema", "romance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_062",
    "text": "Ποιος κορυφαίος Αμερικανός ηθοποιός πρωταγωνίστησε στο «Βλέμμα του Οδυσσέα» (1995) του Θόδωρου Αγγελόπουλου;",
    "answers": ["Αλ Πατσίνο", "Χάρβεϊ Καϊτέλ", "Γουίλεμ Νταφόε", "Ρόμπερτ Ντε Νίρο"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Harvey Keitel υποδύθηκε έναν Ελληνοαμερικανό σκηνοθέτη που περιπλανιέται στα εμπόλεμα Βαλκάνια αναζητώντας τις τρεις χαμένες μπομπίνες των αδελφών Μανάκια.",
    "funFacts": [
      "Η ταινία απέσπασε το Μεγάλο Βραβείο της Κριτικής Επιτροπής (Grand Prix) στο Φεστιβάλ των Καννών το 1995.",
      "Στην ταινία πραγματοποίησε μία από τις τελευταίες κινηματογραφικές του εμφανίσεις ο σπουδαίος Σουηδός ηθοποιός Έρλαντ Γιόσεφσον."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%92%CE%BB%CE%AD%CE%BC%CE%BC%CE%B1_%CF%84%CE%BF%CF%85_%CE%9F%CE%B4%CF%85%CF%83%CF%83%CE%AD%CE%B1",
    "locale": "el-GR",
    "tags": ["angelopoulos", "harvey-keitel", "cannes", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_063",
    "text": "Ποιο είναι το αγαπημένο αλκοολούχο κοκτέιλ του «Dude» (Τζεφ Μπρίτζες) στην καλτ κωμωδία «Ο Μεγάλος Λεμπόφσκι» (1998);",
    "answers": ["Μανχάταν", "Μαρτίνι", "White Russian (Λευκός Ρώσος)", "Μαργαρίτα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jeffrey 'The Dude' Lebowski πίνει συνεχώς White Russian, ένα κοκτέιλ φτιαγμένο από βότκα, λικέρ καφέ και κρέμα γάλακτος.",
    "funFacts": [
      "Ο Dude καταναλώνει συνολικά εννέα White Russians κατά τη διάρκεια της ταινίας των αδελφών Κοέν.",
      "Η ταινία ενέπνευσε μια πραγματική φιλοσοφική κοινότητα και τρόπο ζωής γνωστό ως 'Dudeism'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9C%CE%B5%CE%B3%CE%AC%CE%BB%CE%BF%CF%82_%CE%9B%CE%B5%CE%BC%CF%80%CF%8C%CF%86%CF%83%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["the-big-lebowski", "coen-brothers", "jeff-bridges", "cult-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_064",
    "text": "Ποιο ήταν το πραγματικό όνομα γέννησης του δικηγόρου Σολ Γκούντμαν στη σειρά «Better Call Saul»;",
    "answers": ["Τσακ ΜακΓκιλ", "Χάουαρντ Χάμλιν", "Κιμ Γουέξλερ", "Τζίμι ΜακΓκιλ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο James Morgan 'Jimmy' McGill (Bob Odenkirk) υιοθέτησε το ψευδώνυμο Saul Goodman από το λογοπαίγνιο '[it]'s all good, man!'.",
    "funFacts": [
      "Η σειρά απέσπασε 53 υποψηφιότητες για βραβεία Primetime Emmy κατά τη διάρκεια των έξι σεζόν της.",
      "Η ερμηνεία της Rhea Seehorn ως Kim Wexler επαινέθηκε από τους κριτικούς ως μία από τις κορυφαίες στην ιστορία της τηλεόρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/Better_Call_Saul",
    "locale": "el-GR",
    "tags": ["better-call-saul", "breaking-bad", "amc", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_065",
    "text": "Στο δικαστικό δράμα «Κοινωνία ώρα μηδέν» (1966), ποιος πρωταγωνιστής υποδύθηκε τον αποπεμφθέντα αξιωματικό Άγγελο Μουρούζη;",
    "answers": ["Νίκος Κούρκουλος", "Μάνος Κατράκης", "Γιάννης Βόγλης", "Φαίδων Γεωργίτσης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Νίκος Κούρκουλος ενσάρκωσε έναν πρώην πιλότο που αναλαμβάνει να διερευνήσει τα αίτια ενός μυστηριώδους αεροπορικού δυστυχήματος.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Ντίνο Δημόπουλο σε σενάριο του Νίκου Φώσκολου για τη Φίνος Φιλμ.",
      "Σημείωσε τεράστια εμπορική επιτυχία, κόβοντας περισσότερα από 596.000 εισιτήρια κατά την πρώτη της προβολή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CE%B9%CE%BD%CF%89%CE%BD%CE%AF%CE%B1_%CF%8E%CF%81%CE%B1_%CE%BC%CE%B7%CE%B4%CE%AD%CE%BD",
    "locale": "el-GR",
    "tags": ["greek-cinema", "kourkoulos", "foskolos", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_066",
    "text": "Ποιος Τσεχοαμερικανός σκηνοθέτης κέρδισε το Όσκαρ Σκηνοθεσίας για τη «Φωλιά του Κούκου» (1975) και το «Αμαντέους» (1984);",
    "answers": ["Ίρι Μένζελ", "Μίλος Φόρμαν", "Ρομάν Πολάνσκι", "Γιαν Σβανκμάγιερ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Miloš Forman υπήρξε ηγετική μορφή του Νέου Κύματος του τσεχοσλοβακικού κινηματογράφου πριν κατακτήσει το Χόλιγουντ με δύο οσκαρικά αριστουργήματα.",
    "funFacts": [
      "Η 'Φωλιά του Κούκου' ήταν μόλις η δεύτερη ταινία στην ιστορία που απέσπασε και τα πέντε βασικά Όσκαρ (Ταινίας, Σκηνοθεσίας, Α' Ανδρικού, Α' Γυναικείου, Σεναρίου).",
      "Ο Τζακ Νίκολσον κέρδισε το πρώτο του Όσκαρ Α' Ανδρικού Ρόλου για την ερμηνεία του ως Randle McMurphy."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AF%CE%BB%CE%BF%CF%82_%CE%A6%CF%8C%CF%81%CE%BC%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["milos-forman", "one-flew-over-the-cuckoos-nest", "oscars", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_067",
    "text": "Στη δραματική σειρά εποχής «Το Κόκκινο Ποτάμι» (Open TV, 2019) του Μανούσου Μανουσάκη, ποιο ιστορικό γεγονός εξιστορείται;",
    "answers": ["Η Μικρασιατική Καταστροφή", "Η Εθνική Αντίσταση", "Η Γενοκτονία των Ελλήνων του Πόντου", "Ο Εμφύλιος Πόλεμος"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η σειρά βασίστηκε στο ομότιτλο ιστορικό μυθιστόρημα του Χάρη Τσιρκινίδη και αποτύπωσε τα τραγικά γεγονότα των διωγμών και της Γενοκτονίας του Ποντιακού Ελληνισμού.",
    "funFacts": [
      "Υπήρξε μία από τις μεγαλύτερες παραγωγές της ελληνικής τηλεόρασης με γυρίσματα σε περισσότερες από 15 πόλεις σε Ελλάδα, Ρωσία και Γαλλία.",
      "Το ομώνυμο τραγούδι των τίτλων ερμήνευσε η Ελεωνόρα Ζουγανέλη σε μουσική Χρήστου Παπαδόπουλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9A%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%BF_%CE%A0%CE%BF%CF%84%CE%AC%CE%BC%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-kokkino-potami", "manousakis", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_068",
    "text": "Ποια είναι η διάσημη σοκαριστική αποκάλυψη για τον παιδοψυχίατρο Μάλκολμ Κρόου (Μπρους Γουίλις) στην «Έκτη Αίσθηση» (1999);",
    "answers": ["Ήταν ο δολοφόνος του παιδιού", "Ήταν φανταστικός χαρακτήρας", "Είχε χάσει τη μνήμη του", "Ήταν νεκρός καθ' όλη τη διάρκεια"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Στο φινάλε της ταινίας του M. Night Shyamalan αποκαλύπτεται ότι ο Malcolm Crowe σκοτώθηκε στην αρχή της ταινίας και ήταν ένα από τα φαντάσματα που έβλεπε ο μικρός Cole.",
    "funFacts": [
      "Η ατάκα του μικρού Χέιλι Τζόελ Όσμεντ 'I see dead people' («Βλέπω νεκρούς ανθρώπους») ψηφίστηκε στις κορυφαίες του παγκόσμιου σινεμά.",
      "Η ταινία προτάθηκε για 6 βραβεία Όσκαρ και έγινε η δεύτερη πιο εμπορική ταινία του 1999 παγκοσμίως."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%88%CE%BA%CF%84%CE%B7_%CE%91%CE%AF%CF%83%CE%B8%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["sixth-sense", "bruce-willis", "shyamalan", "plot-twist"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_069",
    "text": "Ποια ιστορική μορφή της ελληνικής Αριστεράς ενσάρκωσε ο Φοίβος Γκικόπουλος στην ταινία «Ο άνθρωπος με το γαρύφαλλο» (1980);",
    "answers": ["Νίκο Μπελογιάννη", "Νίκο Πλουμπίδη", "Άρη Βελουχιώτη", "Γρηγόρη Λαμπράκη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η ιστορική ταινία του Νίκου Τζίμα κατέγραψε τη δράση, τη δίκη και την εκτέλεση του στελέχους του ΚΚΕ Νίκου Μπελογιάννη το 1952.",
    "funFacts": [
      "Η ταινία έκοψε περισσότερα από 2.000.000 εισιτήρια σε όλη την Ελλάδα, σημειώνοντας ένα από τα μεγαλύτερα ρεκόρ προσέλευσης.",
      "Το προσωνύμιο 'Ο άνθρωπος με το γαρύφαλλο' εμπνεύστηκε από το διάσημο σκίτσο που φιλοτέχνησε ο Πάμπλο Πικάσο στη διάρκεια της δίκης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%AC%CE%BD%CE%B8%CF%81%CF%89%CF%80%CE%BF%CF%82_%CE%BC%CE%B5_%CF%84%CE%BF_%CE%B3%CE%B1%CF%81%CF%8D%CF%86%CE%B1%CE%BB%CE%BB%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "beloyannis", "tzimas", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_070",
    "text": "Ποιος Γαλλοκαναδός σκηνοθέτης ανέλαβε και υλοποίησε το πολυαναμενόμενο σίκουελ επιστημονικής φαντασίας «Blade Runner 2049» (2017);",
    "answers": ["Ζαν-Μαρκ Βαλέ", "Ντενί Βιλνέβ", "Ξαβιέ Ντολάν", "Ντέιβιντ Φίντσερ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Denis Villeneuve σκηνοθέτησε το 'Blade Runner 2049' με πρωταγωνιστές τον Ryan Gosling και τον Harrison Ford, αποσπώντας διθυραμβικές κριτικές.",
    "funFacts": [
      "Ο κορυφαίος διευθυντής φωτογραφίας Roger Deakins κέρδισε το πρώτο του Όσκαρ Καλύτερης Φωτογραφίας μετά από 14 άκαρπες υποψηφιότητες.",
      "Η ταινία κέρδισε επίσης το Όσκαρ Καλύτερων Οπτικών Εφέ."
    ],
    "source": "https://el.wikipedia.org/wiki/Blade_Runner_2049",
    "locale": "el-GR",
    "tags": ["blade-runner-2049", "denis-villeneuve", "sci-fi", "harrison-ford"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_071",
    "text": "Στη μαύρη κωμωδία «Μαύρα Μεσάνυχτα» (Mega, 2008), τι είδους κατάστημα κληρονομεί αναπάντεχα ο ήσυχος βιοπαλαιστής Θράσος Κουτρουμπάς;",
    "answers": ["Πρακτορείο στοιχημάτων", "Χαρτοπαικτική λέσχη", "Νυχτερινό κέντρο (σκυλάδικο)", "Στούντιο ηχογραφήσεων"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Θράσος (Στέλιος Μάινας) κληρονομεί από τον μαφιόζο αδελφό του Αποστόλη το νυχτερινό κέντρο 'Kollasi' και μπλέκει στον υπόκοσμο της νύχτας.",
    "funFacts": [
      "Η σειρά σκηνοθετήθηκε από τον Πάνο Κοκκινόπουλο σε σενάριο Βασίλη Ρίσβα και Δήμητρας Σακαλή.",
      "Το τραγούδι των τίτλων 'Μαύρα Μεσάνυχτα' σε ερμηνεία της Μαρίας Ιακώβου και των Onirama έγινε τεράστια ραδιοφωνική επιτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%8D%CF%81%CE%B1_%CE%9C%CE%B5%CF%83%CE%AC%CE%BD%CF%85%CF%87%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-tv", "mavra-mesanychta", "kokkinopoulos", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_072",
    "text": "Στο αστυνομικό θρίλερ «Συνήθεις Ύποπτοι» (1995), ποιος ανάπηρος μικροαπατεώνας αποκαλύπτεται ότι ήταν ο διαβόητος Κάιζερ Σόζε;",
    "answers": ["Ντιν Κίτον", "Μάικλ ΜακΜάνους", "Φρεντ Φένστερ", "Ρότζερ «Βέρμπαλ» Κιντ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Kevin Spacey υποδύεται τον Verbal Kint, έναν φαινομενικά αδύναμο απατεώνα που στο φινάλε ισιώνει το πόδι του και αποκαλύπτεται ως ο πανίσχυρος μαφιόζος Keyser Söze.",
    "funFacts": [
      "Ο Kevin Spacey κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου και ο Christopher McQuarrie το Όσκαρ Πρωτότυπου Σεναρίου.",
      "Η διάσημη ατάκα της ταινίας είναι: 'Το σπουδαιότερο κόλπο του Διαβόλου ήταν να πείσει τον κόσμο ότι δεν υπάρχει'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%BD%CE%AE%CE%B8%CE%B5%CE%B9%CF%82_%CE%8E%CF%80%CE%BF%CF%80%CF%84%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["usual-suspects", "keyser-soze", "kevin-spacey", "plot-twist"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_073",
    "text": "Σε ποια ιστορική κακόφημη συνοικία του Πειραιά διαδραματίζεται το υποψήφιο για Όσκαρ δράμα «Τα κόκκινα φανάρια» (1963);",
    "answers": ["Στην Τρούμπα", "Στην Καστέλλα", "Στη Δραπετσώνα", "Στο Πασαλιμάνι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η ταινία του Βασίλη Γεωργιάδη καταγράφει τη ζωή και τα δράματα των ιερόδουλων στο 'σπίτι' της μαντάμ Παρί στην κακόφημη συνοικία της Τρούμπας.",
    "funFacts": [
      "Η ταινία υπήρξε υποψήφια για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας το 1964 και συμμετείχε στο διαγωνιστικό τμήμα των Καννών.",
      "Πρωταγωνίστησαν σπουδαίες ηθοποιοί όπως η Τζένη Καρέζη, η Μαίρη Χρονοπούλου και η Δέσπω Διαμαντίδου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%B1_%CF%86%CE%B1%CE%BD%CE%AC%CF%81%CE%B9%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "troumba", "karezis", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_074",
    "text": "Ποια νεαρή ηθοποιός υποδύθηκε τη δαιμονισμένη δωδεκάχρονη Ρίγκαν ΜακΝίλ στην ταινία τρόμου «Ο Εξορκιστής» (The Exorcist, 1973);",
    "answers": ["Τζόντι Φόστερ", "Λίντα Μπλερ", "Μπρουκ Σιλντς", "Ντρου Μπάριμορ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Linda Blair κέρδισε Χρυσή Σφαίρα και υποψηφιότητα για Όσκαρ Β' Γυναικείου Ρόλου σε ηλικία μόλις 14 ετών για την ανατριχιαστική ερμηνεία της.",
    "funFacts": [
      "Η βαριά φωνή του δαίμονα Pazuzu ανήκε στην ηθοποιό Mercedes McCambridge, η οποία κατάπινε ωμά αυγά και κάπνιζε μανιωδώς για να πετύχει τη βραχνάδα.",
      "Υπήρξε η πρώτη ταινία τρόμου στην ιστορία που προτάθηκε ποτέ για Όσκαρ Καλύτερης Ταινίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%95%CE%BE%CE%BF%CF%81%CE%BA%CE%B9%CF%83%CF%84%CE%AE%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["the-exorcist", "linda-blair", "horror", "friedkin"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_075",
    "text": "Στη δραματική σειρά «Άγριες Μέλισσες» (ΑΝΤ1), ποιο ήταν το όνομα του σκληρού και αδίστακτου γαιοκτήμονα της οικογένειας Σεβαστού;",
    "answers": ["Μιλτιάδης Σεβαστός", "Κωνσταντής Σεβαστός", "Δούκας Σεβαστός", "Νικηφόρος Σεβαστός"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Δούκας Σεβαστός (Λεωνίδας Κακούρης) ήταν ο ισχυρός και αδίστακτος άρχοντας του χωριού Διαφάνι που βρισκόταν σε διαρκή πόλεμο με τις αδελφές Σταμίρη.",
    "funFacts": [
      "Η ερμηνεία του Λεωνίδα Κακούρη απέσπασε διθυραμβικές κριτικές και τον κατέστησε έναν από τους πιο εμβληματικούς τηλεοπτικούς 'κακούς'.",
      "Η σειρά προβλήθηκε για τρεις συνεχόμενες σεζόν συγκεντρώνοντας φανατικό κοινό σε κάθε επεισόδιο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CF%81%CE%B9%CE%B5%CF%82_%CE%9C%CE%AD%CE%BB%CE%B9%CF%83%CF%83%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["agries-melisses", "ant1", "doukas-sevastos", "greek-tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_076",
    "text": "Ποια Αυστραλή ηθοποιός εκτόξευσε τη διεθνή της καριέρα με τον διπλό ρόλο στο ψυχολογικό θρίλερ «Οδός Μαλχόλαντ» (Mulholland Drive, 2001);",
    "answers": ["Νικόλ Κίντμαν", "Κέιτ Μπλάνσετ", "Τόνι Κολέτ", "Ναόμι Γουότς"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Naomi Watts έδωσε μια συγκλονιστική ερμηνεία ως η αισιόδοξη ηθοποιός Betty Elms και η απελπισμένη Diane Selwyn στο σουρεαλιστικό νεο-νουάρ του David Lynch.",
    "funFacts": [
      "Ο Ντέιβιντ Λιντς κέρδισε το Βραβείο Σκηνοθεσίας στο Φεστιβάλ των Καννών για την ταινία.",
      "Σε ψηφοφορία του BBC Culture το 2016 ανάμεσα σε 177 κριτικούς παγκοσμίως, το 'Mulholland Drive' ψηφίστηκε ως η καλύτερη ταινία του 21ου αιώνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B4%CF%8C%CF%82_%CE%9C%CE%B1%CE%BB%CF%87%CF%8C%CE%BB%CE%B1%CE%BD%CF%84_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["mulholland-drive", "naomi-watts", "david-lynch", "neo-noir"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_077",
    "text": "Ποια διεθνώς αναγνωρισμένη Ελληνίδα συνθέτρια υπέγραψε την υποβλητική μουσική για τις περισσότερες ταινίες του Θόδωρου Αγγελόπουλου;",
    "answers": ["Ελένη Καραΐνδρου", "Ευανθία Ρεμπούτσικα", "Σοφία Καμαγιάννη", "Καλλιόπη Τσουπάκη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Ελένη Καραΐνδρου συνέθεσε ιστορικά scores για ταινίες όπως 'Τοπίο στην ομίχλη', 'Το μετέωρο βήμα του πελαργού' και 'Μια αιωνιότητα και μια μέρα'.",
    "funFacts": [
      "Η μουσική της κυκλοφόρησε παγκοσμίως από τη διάσημη γερμανική δισκογραφική εταιρεία ECM, αποσπώντας διεθνή βραβεία.",
      "Ο ίδιος ο Αγγελόπουλος συνήθιζε να γράφει τα σενάριά του ακούγοντας τα πρώτα μουσικά θέματα της Καραΐνδρου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BB%CE%AD%CE%BD%CE%B7_%CE%9A%CE%B1%CF%81%CE%B1%CE%90%CE%BD%CE%B4%CF%81%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["karaindrou", "angelopoulos", "soundtrack", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_078",
    "text": "Ποιος Μεξικανός σκηνοθέτης πέτυχε το ιστορικό επίτευγμα να κερδίσει δύο συνεχόμενα Όσκαρ Σκηνοθεσίας για το «Birdman» (2014) και το «The Revenant» (2015);",
    "answers": ["Αλφόνσο Κουαρόν", "Αλεχάντρο Γκονσάλες Ινιάριτου", "Γκιγιέρμο ντελ Τόρο", "Κάρλος Ρεϊγάδας"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Alejandro González Iñárritu έγινε μόλις ο τρίτος σκηνοθέτης στην ιστορία που κέρδισε διαδοχικά Όσκαρ Σκηνοθεσίας, μετά τους Τζον Φορντ και Τζόζεφ Μάνκιεβιτς.",
    "funFacts": [
      "Το 'Birdman' γυρίστηκε και μονταρίστηκε με τέτοιο τρόπο ώστε να δίνει την εντύπωση ενός ενιαίου, αδιάκοπου μονοπλάνου δύο ωρών.",
      "Με το 'The Revenant', ο Λεονάρντο Ντι Κάπριο κέρδισε επιτέλους το πρώτο του Όσκαρ Α' Ανδρικού Ρόλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B5%CF%87%CE%AC%CE%BD%CF%84%CF%81%CE%BF_%CE%93%CE%BA%CE%BF%CE%BD%CF%83%CE%AC%CE%BB%CE%B5%CF%82_%CE%99%CE%BD%CE%B9%CE%AC%CF%81%CE%B9%CF%84%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["inarritu", "birdman", "the-revenant", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_079",
    "text": "Στη δημοφιλή σειρά «Το Δις Εξαμαρτείν» (Mega, 1993–1996), σε τι είδους εργασιακό περιβάλλον εξελίσσεται το ερωτικό τρίγωνο;",
    "answers": ["Σε μια εφημερίδα μεγάλης κυκλοφορίας", "Σε μια διαφημιστική εταιρεία", "Στον τηλεοπτικό σταθμό Media 7", "Σε έναν ραδιοφωνικό σταθμό"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Άννα Ραγιά (Νένα Μεντή) είναι διευθύντρια ειδήσεων στο ιδιωτικό κανάλι Media 7 και διατηρεί παράλληλη σχέση με τον διευθυντή προγράμματος και έναν δημοσιογράφο.",
    "funFacts": [
      "Η σειρά γράφτηκε από τους Μιχάλη Ρέππα και Θανάση Παπαθανασίου, αποτελώντας υπόδειγμα έξυπνης αστικής κωμωδίας.",
      "Στη σειρά πρωταγωνίστησαν επίσης ο Χάρης Ρώμας, ο Αλέξανδρος Αντωνόπουλος και η Ντίνα Κώνστα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%B4%CE%B9%CF%82_%CE%B5%CE%BE%CE%B1%CE%BC%CE%B1%CF%81%CF%84%CE%B5%CE%AF%CE%BD",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-dis-examartein", "mega-channel", "reppas-papathanasiou"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_080",
    "text": "Ποιου κλασικού συνθέτη η 9η Συμφωνία αποτελεί τη μεγάλη μουσική εμμονή του παραβατικού Άλεξ στο «Κουρδιστό Πορτοκάλι» (1971);",
    "answers": ["Βόλφγκανγκ Αμαντέους Μότσαρτ", "Γιόχαν Σεμπάστιαν Μπαχ", "Φραντς Σούμπερτ", "Λούντβιχ βαν Μπετόβεν"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Alex DeLarge (Malcolm McDowell) αποκαλεί με πάθος τον συνθέτη 'Ludwig Van', και η μουσική της 9ης Συμφωνίας χρησιμοποιείται στην τεχνική αποστροφής Ludovico.",
    "funFacts": [
      "Η ταινία του Στάνλεϊ Κιούμπρικ βασίστηκε στο ομώνυμο δυστοπικό μυθιστόρημα του Άντονι Μπέρτζες.",
      "Ο Κιούμπρικ απέσυρε ο ίδιος την ταινία από τους βρετανικούς κινηματογράφους μετά από απειλές κατά της οικογένειάς του και μιμητικές πράξεις βίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9A%CE%BF%CF%85%CF%81%CE%B4%CE%B9%CF%83%CF%84%CF%8C_%CE%A0%CE%BF%CF%81%CF%84%CE%BF%CE%BA%CE%AC%CE%BB%CE%B9_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["clockwork-orange", "kubrick", "beethoven", "dystopia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_081",
    "text": "Στην κωμωδία δρόμου «Βαλκανιζατέρ» (1997) του Σωτήρη Γκορίτσα, με ποια παράνομη δραστηριότητα προσπαθούν να πλουτίσουν δύο φίλοι από την Κοζάνη;",
    "answers": ["Μαύρη αγορά συναλλάγματος", "Λαθρεμπόριο τσιγάρων", "Πώληση κλεμμένων αυτοκινήτων", "Εισαγωγή παράνομων καυσίμων"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Φώτης και ο Σταύρος (Στέλιος Μάινας και Γεράσιμος Σκιαδαρέσης) ταξιδεύουν σε Βουλγαρία και Ρουμανία για να εκμεταλλευτούν τις διαφορές στις ισοτιμίες δολαρίου.",
    "funFacts": [
      "Η ταινία βασίστηκε στο αυτοβιογραφικό βιβλίο του Σάκη Τώτλη 'Το συνάλλαγμα'.",
      "Αποτέλεσε μία από τις πιο χαρακτηριστικές και επιτυχημένες ελληνικές ταινίες της δεκαετίας του 1990."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CE%BB%CE%BA%CE%B1%CE%BD%CE%B9%CE%B6%CE%B1%CF%84%CE%AD%CF%81",
    "locale": "el-GR",
    "tags": ["greek-cinema", "balkanizater", "goritsas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_082",
    "text": "Ποιος διακεκριμένος σεναριογράφος δημιούργησε την ανθολογική τηλεοπτική σειρά «Fargo» (FX) βασισμένος στον κόσμο των αδελφών Κοέν;",
    "answers": ["Νικ Πιτσολάτο", "Νόα Χόλεϊ", "Ντέιμον Λίντελοφ", "Κρεγκ Μέιζιν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Noah Hawley ανέπτυξε τη σειρά 'Fargo' το 2014, διατηρώντας το ιδιόρρυθμο μαύρο χιούμορ, την παγωμένη ατμόσφαιρα και τις εκκεντρικές φιγούρες της ταινίας.",
    "funFacts": [
      "Η σειρά απέσπασε 6 βραβεία Emmy και 3 Χρυσές Σφαίρες, γνωρίζοντας τεράστια αποδοχή από κριτικούς και κοινό.",
      "Κάθε σεζόν αφηγείται μια ανεξάρτητη ιστορία εγκλήματος με διαφορετικό καστ πρωταγωνιστών σε διαφορετική χρονική περίοδο."
    ],
    "source": "https://el.wikipedia.org/wiki/Fargo_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["fargo-series", "noah-hawley", "anthology", "crime"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_083",
    "text": "Στο αριστούργημα «Μια αιωνιότητα και μια μέρα» (1998), ποιου εθνικού ποιητή τα χαμένα ποιήματα προσπαθεί να αγοράσει ο ετοιμοθάνατος συγγραφέας;",
    "answers": ["Κωστή Παλαμά", "Ανδρέα Κάλβου", "Διονύσιου Σολωμού", "Κ. Π. Καβάφη"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο συγγραφέας Αλέξανδρος (Μπρούνο Γκαντς) ερευνά τη ζωή του Διονύσιου Σολωμού, ο οποίος αγόραζε λέξεις από τους απλούς ανθρώπους για να γράψει τους 'Ελεύθερους Πολιορκημένους'.",
    "funFacts": [
      "Η ταινία χάρισε στον Θόδωρο Αγγελόπουλο τον Χρυσό Φοίνικα στο Φεστιβάλ των Καννών με ομόφωνη απόφαση της επιτροπής υπό την προεδρία του Μάρτιν Σκορσέζε.",
      "Τον ρόλο του ποιητή Διονύσιου Σολωμού στην ταινία υποδύθηκε ο ηθοποιός Φαμπρίτσιο Μπεντιβόλιο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CE%B1%CE%B9%CF%89%CE%BD%CE%B9%CF%8C%CF%84%CE%B7%CF%84%CE%B1_%CE%BA%CE%B1%CE%B9_%CE%BC%CE%B9%CE%B1_%CE%BC%CE%AD%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["angelopoulos", "solomos", "palme-dor", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_084",
    "text": "Ποιος σπουδαίος δημιουργός σκηνοθέτησε το ιστορικό έπος «Θα χυθεί αίμα» (There Will Be Blood, 2007);",
    "answers": ["Ντέιβιντ Φίντσερ", "Κουέντιν Ταραντίνο", "Κρίστοφερ Νόλαν", "Πολ Τόμας Άντερσον"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Paul Thomas Anderson σκηνοθέτησε την ταινία, βασισμένος ελεύθερα στο μυθιστόρημα 'Oil!' του Upton Sinclair.",
    "funFacts": [
      "Ο Ντάνιελ Ντέι-Λιούις κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου για την ανεπανάληπτη ερμηνεία του ως ο αδίστακτος πετρελαιοπαραγωγός Daniel Plainview.",
      "Η ατάκα του Plainview 'I drink your milkshake!' ('Πίνω το μιλκσέικ σου!') έγινε μία από τις πιο διάσημες της σύγχρονης κινηματογραφικής ιστορίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B1_%CF%87%CF%85%CE%B8%CE%B5%CE%AF_%CE%B1%CE%AF%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["paul-thomas-anderson", "there-will-be-blood", "daniel-day-lewis", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_085",
    "text": "Ποιος σκηνοθέτης υπήρξε ο δημιουργός και η ψυχή των εμβληματικών αστυνομικών σειρών «Κόκκινος Κύκλος» και «10η Εντολή»;",
    "answers": ["Πάνος Κοκκινόπουλος", "Μανούσος Μανουσάκης", "Σωτήρης Τσαφούλιας", "Κώστας Κουτσομύτης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Πάνος Κοκκινόπουλος καθιέρωσε το σκοτεινό ψυχολογικό θρίλερ στην ελληνική τηλεόραση, εμπνεόμενος από πραγματικά εγκλήματα που συγκλόνισαν την κοινή γνώμη.",
    "funFacts": [
      "Οι σειρές του ξεχώρισαν για την κινηματογραφική αισθητική, το γρήγορο μοντάζ και τις εξαιρετικές επιλογές ανεξάρτητης ροκ μουσικής.",
      "Σχεδόν όλοι οι κορυφαίοι Έλληνες ηθοποιοί πέρασαν ως πρωταγωνιστές από τα αυτοτελή επεισόδια των σειρών του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AC%CE%BD%CE%BF%CF%82_%CE%9A%CE%BF%CE%BA%CE%BA%CE%B9%CE%BD%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["kokkinopoulos", "dekati-entoli", "greek-tv", "thriller"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_086",
    "text": "Ποια μυθική ηθοποιός κέρδισε το Όσκαρ Α' Γυναικείου Ρόλου στον πρώτο της μεγάλο χολιγουντιανό ρόλο στις «Διακοπές στη Ρώμη» (1953);",
    "answers": ["Γκρέις Κέλι", "Όντρεϊ Χέπμπορν", "Ελίζαμπεθ Τέιλορ", "Ίνγκριντ Μπέργκμαν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Audrey Hepburn μάγεψε κοινό και κριτικούς ως η πριγκίπισσα Άννα που το σκάει από τα καθήκοντά της για να γνωρίσει τη Ρώμη μαζί με τον Γκρέγκορι Πεκ.",
    "funFacts": [
      "Ο Γκρέγκορι Πεκ απαίτησε από το στούντιο να μπει το όνομα της Χέπμπορν πάνω από τον τίτλο μαζί με το δικό του, προβλέποντας ότι θα κέρδιζε Όσκαρ.",
      "Η σκηνή στο 'Στόμα της Αλήθειας' (Bocca della Verità) όπου ο Πεκ κρύβει το χέρι του στο μανίκι ήταν αυθόρμητη φάρσα που τρόμαξε αληθινά την ηθοποιό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B1%CE%BA%CE%BF%CF%80%CE%AD%CF%82_%CF%83%CF%84%CE%B7_%CE%A1%CF%8E%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["audrey-hepburn", "roman-holiday", "oscars", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_087",
    "text": "Ποιος σκηνοθέτης υπέγραψε την τεράστια εμπορική και καλλιτεχνική επιτυχία «Πολίτικη Κουζίνα» (2003);",
    "answers": ["Περικλής Χούρσογλου", "Σωτήρης Γκορίτσας", "Τάσος Μπουλμέτης", "Νίκος Παναγιωτόπουλος"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Τάσος Μπουλμέτης σκηνοθέτησε την 'Πολίτικη Κουζίνα', βασισμένος σε βιώματα και αναμνήσεις από τις απελάσεις των Ελλήνων της Κωνσταντινούπολης το 1964.",
    "funFacts": [
      "Η ταινία έκοψε περισσότερα από 1.500.000 εισιτήρια στην Ελλάδα, σημειώνοντας το απόλυτο ρεκόρ εισιτηρίων της σύγχρονης εποχής.",
      "Η νοσταλγική μουσική επένδυση της Ευανθίας Ρεμπούτσικα γνώρισε τεράστια εμπορική επιτυχία και απέσπασε διεθνή βραβεία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB%CE%AF%CF%84%CE%B9%CE%BA%CE%B7_%CE%9A%CE%BF%CF%85%CE%B6%CE%AF%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["politiki-kouzina", "boulmetis", "remboutsika", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_088",
    "text": "Ποιος Δανός σκηνοθέτης κέρδισε το Βραβείο Σκηνοθεσίας στις Κάννες για το νεο-νουάρ θρίλερ «Drive» (2011) με τον Ράιαν Γκόσλινγκ;",
    "answers": ["Λαρς φον Τρίερ", "Τόμας Βίντερμπεργκ", "Σουζάνε Μπίερ", "Νίκολας Βίντινγκ Ρεφν"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Nicolas Winding Refn δημιούργησε ένα κομψό, βίαιο και υπνωτιστικό θρίλερ με έντονη synthwave μουσική και 80s αισθητική.",
    "funFacts": [
      "Ο Ράιαν Γκόσλινγκ επέλεξε ο ίδιος τον Ρεφν για τη σκηνοθεσία και βοήθησε στην επισκευή του αυτοκινήτου Chevy Malibu του 1973 που οδηγεί στην ταινία.",
      "Το χαρακτηριστικό λευκό σατέν μπουφάν με τον χρυσό κεντητό σκορπιό στην πλάτη έγινε άμεσα αντικείμενο λατρείας."
    ],
    "source": "https://el.wikipedia.org/wiki/Drive_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1_2011)",
    "locale": "el-GR",
    "tags": ["drive", "refn", "ryan-gosling", "neo-noir"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_089",
    "text": "Ποιος υπήρξε ο κορυφαίος συγγραφέας αστυνομικής λογοτεχνίας του οποίου το μυθιστόρημα μεταφέρθηκε στο σινεμά ως «Έγκλημα στα παρασκήνια» (1960);",
    "answers": ["Γιάννης Μαρής", "Πέτρος Μάρκαρης", "Βασίλης Βασιλικός", "Μένης Κουμανταρέας"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Γιάννης Μαρής υπήρξε ο 'πατέρας του ελληνικού αστυνομικού μυθιστορήματος', δημιουργός του διάσημου αστυνόμου Μπέκα.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Ντίνο Κατσουρίδη και κέρδισε δύο βραβεία στην 1η Εβδομάδα Ελληνικού Κινηματογράφου Θεσσαλονίκης.",
      "Τον αστυνόμο Μπέκα υποδύθηκε στην ταινία ο ηθοποιός Τίτος Βανδής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%B3%CE%BA%CE%BB%CE%B7%CE%BC%CE%B1_%CF%83%CF%84%CE%B1_%CF%80%CE%B1%CF%81%CE%B1%CF%83%CE%BA%CE%AE%CE%BD%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["giannis-maris", "katsouridis", "crime", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_090",
    "text": "Ποιος Ταϊβανέζος δημιουργός κέρδισε δύο φορές το Όσκαρ Σκηνοθεσίας για το «Το μυστικό του Brokeback Mountain» και τη «Ζωή του Πι»;",
    "answers": ["Έντουαρντ Γιανγκ", "Ανγκ Λι", "Χόου Χσιάο-Χσιεν", "Γουόνγκ Καρ-γουάι"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Ang Lee έγραψε ιστορία ως ο πρώτος Ασιάτης σκηνοθέτης που κέρδισε το Όσκαρ Καλύτερης Σκηνοθεσίας.",
    "funFacts": [
      "Έχει κερδίσει επίσης δύο φορές τον Χρυσό Λέοντα στη Βενετία και δύο φορές τη Χρυσή Άρκτο στο Βερολίνο.",
      "Η ταινία του 'Τίγρης και Δράκος' (2000) απέσπασε 4 Όσκαρ και παραμένει η πιο εμπορική ξενόγλωσση ταινία στην ιστορία των ΗΠΑ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CE%B3%CE%BA_%CE%9B%CE%B9",
    "locale": "el-GR",
    "tags": ["ang-lee", "brokeback-mountain", "life-of-pi", "directors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_091",
    "text": "Στη σειρά «Το Νησί», ποιος ήταν ο αφοσιωμένος γιατρός που εγκαταστάθηκε στη Σπιναλόγκα για να δοκιμάσει τη νέα θεραπεία με σουλφόνες;",
    "answers": ["Δρ. Νίκος Βανδουλάκης", "Δρ. Αντώνης Αγγελόπουλος", "Δρ. Χρήστος Κυρίτσης", "Δρ. Γιώργος Πετράκης"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο γιατρός Χρήστος Κυρίτσης (Αλέξανδρος Λογοθέτης) ρισκάρει τη ζωή του πηγαίνοντας στο νησί για να χορηγήσει τα πρώτα αποτελεσματικά φάρμακα κατά της λέπρας.",
    "funFacts": [
      "Ο Αλέξανδρος Λογοθέτης απέσπασε διθυραμβικές κριτικές για την ευαισθησία και την ακρίβεια της ερμηνείας του.",
      "Η ανακάλυψη των σουλφονών τη δεκαετία του 1950 οδήγησε πράγματι στο οριστικό κλείσιμο του λεπροκομείου της Σπιναλόγκας το 1957."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9D%CE%B7%CF%83%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-nisi", "spinalonga", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_092",
    "text": "Ποιος σπουδαίος δημιουργός του γαλλικού ποιητικού ρεαλισμού σκηνοθέτησε την αντιπολεμική «Μεγάλη Χίμαιρα» (La Grande Illusion, 1937);",
    "answers": ["Μαρσέλ Καρνέ", "Ζαν Βιγκό", "Ζακ Τατί", "Ζαν Ρενουάρ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jean Renoir (γιος του ζωγράφου Πιερ-Ογκίστ Ρενουάρ) σκηνοθέτησε αυτό το οικουμενικό ανθρωπιστικό αριστούργημα με πρωταγωνιστή τον Ζαν Γκαμπέν.",
    "funFacts": [
      "Υπήρξε η πρώτη ξενόγλωσση ταινία στην ιστορία που προτάθηκε για Όσκαρ Καλύτερης Ταινίας (1939).",
      "Ο Όρσον Γουέλς δήλωσε κάποτε ότι η 'Μεγάλη Χίμαιρα' ήταν μία από τις δύο ταινίες που θα έπαιρνε μαζί του στην κιβωτό των απογόνων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%9C%CE%B5%CE%B3%CE%AC%CE%BB%CE%B7_%CE%A7%CE%AF%CE%BC%CE%B1%CE%B9%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["jean-renoir", "la-grande-illusion", "french-cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_093",
    "text": "Ποιος σεναριογράφος συνυπέγραψε με τον Γιώργο Λάνθιμο τα αναγνωρισμένα σενάρια των ταινιών «Κυνόδοντας», «Άλπεις» και «Ο Αστακός»;",
    "answers": ["Ευθύμης Φιλίππου", "Αλέξανδρος Βούλγαρης", "Χρήστος Νίκου", "Σύλλας Τζουμέρκας"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Ευθύμης Φιλίππου υπήρξε ο στενότερος δημιουργικός συνεργάτης του Λάνθιμου, συνδιαμορφώνοντας το χαρακτηριστικό ύφος του Greek Weird Wave.",
    "funFacts": [
      "Το δίδυμο Λάνθιμου-Φιλίππου κέρδισε το Βραβείο Σεναρίου στο Φεστιβάλ Καννών για τον 'Θάνατο του Ιερού Ελαφιού' και υποψηφιότητα για Όσκαρ για τον 'Αστακό'.",
      "Ο Φιλίππου είναι επίσης διακεκριμένος θεατρικός συγγραφέας και λογοτέχνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CE%B8%CF%8D%CE%BC%CE%B7%CF%82_%CE%A6%CE%B9%CE%BB%CE%AF%CF%80%CF%80%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["lanthimos", "efthimis-filippou", "dogtooth", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_094",
    "text": "Ποιος Ιταλός σκηνοθέτης υπέγραψε το ιστορικό πολιτικό ντοκυμαντέρ μυθοπλασίας «Η Μάχη του Αλγερίου» (The Battle of Algiers, 1966);",
    "answers": ["Φραντσέσκο Ρόσι", "Τζίλο Ποντεκόρβο", "Πιερ Πάολο Παζολίνι", "Έλιο Πέτρι"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Gillo Pontecorvo δημιούργησε ένα ρηξικέλευθο αριστούργημα για τον αγώνα του Εθνικού Απελευθερωτικού Μετώπου της Αλγερίας κατά των Γάλλων αποικιοκρατών.",
    "funFacts": [
      "Η ταινία κέρδισε τον Χρυσό Λέοντα στο Φεστιβάλ Βενετίας και απέσπασε 3 υποψηφιότητες για Όσκαρ.",
      "Χρησιμοποιήθηκε ιστορικά ως εκπαιδευτικό υλικό τόσο από αντάρτικες οργανώσεις όσο και από στρατιωτικές υπηρεσίες αντι-ανταρτοπόλεμου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%9C%CE%AC%CF%87%CE%B7_%CF%84%CE%BF%CF%85_%CE%91%CE%BB%CE%B3%CE%B5%CF%81%CE%AF%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["battle-of-algiers", "pontecorvo", "political-cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_095",
    "text": "Στη δημοφιλή σειρά «Ντόλτσε Βίτα» (Mega, 1995–1997), ποιος ήταν ο νεαρός σύντροφος της κόρης με τον οποίο ερωτεύτηκε η Χριστίνα Μαρκάτου;",
    "answers": ["Μανώλης", "Λουκάς", "Αντώνης Καλούδης", "Στέφανος"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η εργοστασιάρχης Χριστίνα Μαρκάτου (Άννα Παναγιωτοπούλου) ερωτεύτηκε στην Περούτζια τον φοιτητή Αντώνη Καλούδη (Θανάσης Ευθυμιάδης), που αποδείχτηκε αρραβωνιαστικός της κόρης της.",
    "funFacts": [
      "Η σειρά των Αλέξανδρου Ρήγα και Λευτέρη Παπαπέτρου σημείωσε τεράστια επιτυχία με τηλεθέαση που ξεπερνούσε το 40%.",
      "Αξέχαστοι έμειναν οι χαρακτήρες της γιαγιάς Όλγας (Μαρία Φωκά) και της γραμματέως Σάσας (Κατιάνα Μπαλανίκα)."
    ],
    "source": "https://el.wikipedia.org/wiki/Dolce_Vita",
    "locale": "el-GR",
    "tags": ["greek-tv", "dolce-vita", "panagiotopoulou", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_096",
    "text": "Στο κορεατικό νεο-νουάρ θρίλερ «Oldboy» (2003) του Παρκ Τσαν-γουκ, για πόσα ολόκληρα χρόνια κρατείται μυστηριωδώς φυλακισμένος ο Ο Ντε-σου;",
    "answers": ["5 χρόνια", "10 χρόνια", "12 χρόνια", "15 χρόνια"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Oh Dae-su (Choi Min-sik) απάγεται και κρατείται έγκλειστος σε ένα απομονωμένο δωμάτιο για 15 χρόνια χωρίς να γνωρίζει τον λόγο ή τον βασανιστή του.",
    "funFacts": [
      "Η περίφημη σκηνή μάχης στον διάδρομο γυρίστηκε σε ένα ενιαίο μονοπλάνο διάρκειας τριών λεπτών χωρίς ψηφιακά κοψίματα.",
      "Η ταινία κέρδισε το Μεγάλο Βραβείο της Επιτροπής (Grand Prix) στις Κάννες το 2004 με πρόεδρο τον Κουέντιν Ταραντίνο."
    ],
    "source": "https://el.wikipedia.org/wiki/Oldboy_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_2003)",
    "locale": "el-GR",
    "tags": ["oldboy", "park-chan-wook", "korean-cinema", "thriller"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_097",
    "text": "Σε ποια προσφυγική συνοικία της Αθήνας τοποθέτησε ο Νίκος Κούνδουρος τη νεορεαλιστική πρώτη του ταινία «Μαγική πόλη» (1954);",
    "answers": ["Στη Δραπετσώνα", "Στην Καισαριανή", "Στη Νέα Κοκκινιά", "Στον Ταύρο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η 'Μαγική πόλη' γυρίστηκε στη φτωχική παραγκούπολη της Δραπετσώνας, εισάγοντας τις αρχές του ιταλικού νεορεαλισμού στον ελληνικό κινηματογράφο.",
    "funFacts": [
      "Η ταινία συμμετείχε στο διαγωνιστικό τμήμα του Φεστιβάλ Κινηματογράφου της Βενετίας το 1954.",
      "Το σενάριο έγραψε η συγγραφέας Μαργαρίτα Λυμπεράκη και τη μουσική συνέθεσε ο Μάνος Χατζιδάκις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%B3%CE%B9%CE%BA%CE%AE_%CF%80%CF%8C%CE%BB%CE%B9%CF%82",
    "locale": "el-GR",
    "tags": ["koundouros", "magiki-poli", "neorealism", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_098",
    "text": "Ποιο μακάβριο ανθρώπινο μέλος βρίσκει ο νεαρός Τζέφρι σε ένα λιβάδι, ξεκινώντας το μυστήριο στο «Μπλε Βελούδο» (Blue Velvet, 1986);",
    "answers": ["Ένα δάχτυλο", "Ένα κομμένο αυτί", "Ένα μάτι", "Μια παλάμη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jeffrey Beaumont (Kyle MacLachlan) βρίσκει ένα κομμένο ανθρώπινο αυτί σκεπασμένο με μυρμήγκια, το οποίο τον οδηγεί στον σκοτεινό υπόκοσμο της πόλης.",
    "funFacts": [
      "Ο Ντέιβιντ Λιντς κέρδισε υποψηφιότητα για Όσκαρ Σκηνοθεσίας για τη δεξιοτεχνική ανατομία της σκοτεινής πλευράς των αμερικανικών προαστίων.",
      "Ο Ντένις Χόπερ έδωσε μία από τις πιο τρομακτικές ερμηνείες του ως ο ψυχοπαθής κακοποιός Frank Booth."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BB%CE%B5_%CE%92%CE%B5%CE%BB%CE%BF%CF%8D%CE%B4%CE%BF_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["blue-velvet", "david-lynch", "neo-noir", "mystery"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_099",
    "text": "Στη σειρά «Το Καφέ της Χαράς», ποιο ήταν το όνομα του μοναχογιού του αυστηρού δημάρχου Περίανδρου Πώποτα;",
    "answers": ["Μπίλης", "Νικόλας", "Μανωλάκης", "Διονύσης"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Μανωλάκης (Πάρης Σκαρτσολιάς) ήταν ο συνεσταλμένος γιος του Πώποτα που ανέπτυξε μια τρυφερή παιδική φιλία και αγάπη με τη μικρή Βάλια.",
    "funFacts": [
      "Η σειρά επανήλθε με νέους κύκλους 15 χρόνια αργότερα (2019–2021) δείχνοντας τους δύο παιδικούς ήρωες πλέον ενήλικες.",
      "Το τραγούδι της σειράς τραγουδούσαν τα ίδια τα παιδιά σε διάφορα επεισόδια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9A%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["to-kafe-tis-charas", "ant1", "popotas", "greek-tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_100",
    "text": "Ποιος σπουδαίος ηθοποιός υποδύθηκε τον χαρισματικό ηγέτη αίρεσης Λάνκαστερ Ντοντ στην ταινία «The Master» (2012);",
    "answers": ["Ντάνιελ Ντέι-Λιούις", "Κέβιν Σπέισι", "Κρίστοφερ Γουόκεν", "Φίλιπ Σέιμουρ Χόφμαν"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Philip Seymour Hoffman απέσπασε υποψηφιότητα για Όσκαρ Β' Ανδρικού Ρόλου για την ερμηνεία του ως ο ηγέτης του πνευματικού κινήματος 'The Cause'.",
    "funFacts": [
      "Και οι τρεις πρωταγωνιστές της ταινίας (Χόφμαν, Χοακίν Φίνιξ και Έιμι Άνταμς) προτάθηκαν για Όσκαρ υποκριτικής.",
      "Η ταινία του Πολ Τόμας Άντερσον κέρδισε το Αργυρό Λιοντάρι Σκηνοθεσίας και το βραβείο ανδρικής ερμηνείας εξ ημισείας στο Φεστιβάλ Βενετίας."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Master_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_2012)",
    "locale": "el-GR",
    "tags": ["the-master", "philip-seymour-hoffman", "paul-thomas-anderson", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_101",
    "text": "Στο αριστούργημα «Ο θίασος» (1975) του Θόδωρου Αγγελόπουλου, ποιο θεατρικό ειδύλλιο του 19ου αιώνα προσπαθεί να ανεβάσει ο περιοδεύων θίασος;",
    "answers": ["«Γκόλφω»", "«Η Ερωφίλη»", "«Η αγαπητική του βοσκού»", "«Η Μαρία Πενταγιώτισσα»"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο περιπλανώμενος θίασος επιχειρεί αδιάκοπα να παίξει το βουκολικό δράμα 'Γκόλφω' του Σπυρίδωνος Περεσιάδη, το οποίο διακόπτεται διαρκώς από τα ιστορικά γεγονότα (1939–1952).",
    "funFacts": [
      "Η ταινία απέσπασε το Βραβείο FIPRESCI στο Φεστιβάλ των Καννών και θεωρείται από τις σημαντικότερες δημιουργίες του παγκόσμιου κινηματογράφου.",
      "Αποτελείται από μόλις περίπου 80 εκτενή και εξαιρετικά χορογραφημένα μονοπλάνα σε διάρκεια σχεδόν 4 ωρών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%98%CE%AF%CE%B1%CF%83%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["angelopoulos", "o-thiasos", "golfo", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_102",
    "text": "Σε ποιες επικίνδυνες φαβέλες της Βραζιλίας εκτυλίσσεται το ωμό αστυνομικό δράμα «Η Πόλη του Θεού» (City of God, 2002);",
    "answers": ["Του Σάο Πάολο", "Του Ρίο ντε Τζανέιρο", "Της Μπραζίλια", "Του Σαλβαδόρ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η ταινία των Fernando Meirelles και Kátia Lund καταγράφει την άνοδο του οργανωμένου εγκλήματος στις φαβέλες Cidade de Deus του Ρίο ντε Τζανέιρο.",
    "funFacts": [
      "Η ταινία προτάθηκε για 4 βραβεία Όσκαρ (Σκηνοθεσίας, Διασκευασμένου Σεναρίου, Φωτογραφίας, Μοντάζ).",
      "Οι περισσότεροι ηθοποιοί δεν ήταν επαγγελματίες αλλά πραγματικοί κάτοικοι των φαβελών του Ρίο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A0%CF%8C%CE%BB%CE%B7_%CF%84%CE%BF%CF%85_%CE%98%CE%B5%CE%BF%CF%8D_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["city-of-god", "brazilian-cinema", "crime", "meirelles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_103",
    "text": "Σε ποιο ειδυλλιακό νησί του Ιονίου εκτυλίσσεται η δραματική σειρά «Maestro» (2022) του Χριστόφορου Παπακαλιάτη;",
    "answers": ["Στην Κέρκυρα", "Στη Λευκάδα", "Στους Παξούς", "Στην Ιθάκη"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η σειρά διαδραματίζεται στους Παξούς, όπου ένας μουσικός ταξιδεύει κατά τη διάρκεια της πανδημίας για να διοργανώσει ένα φεστιβάλ μουσικής.",
    "funFacts": [
      "Έγραψε ιστορία καθώς έγινε η πρώτη ελληνική τηλεοπτική σειρά που εντάχθηκε στην παγκόσμια πλατφόρμα του Netflix.",
      "Στη σειρά πρωταγωνιστούν σπουδαίοι ηθοποιοί όπως η Μαρία Καβογιάννη, η Χάρις Αλεξίου και ο Φάνης Μουρατίδης."
    ],
    "source": "https://el.wikipedia.org/wiki/Maestro_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["maestro", "papakaliatis", "netflix", "greek-tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_104",
    "text": "Ποιος κορυφαίος Σουηδός σκηνοθέτης υπέγραψε το ψυχολογικό αριστούργημα «Περσόνα» (Persona, 1966);",
    "answers": ["Βίκτορ Σιόστρομ", "Γιαν Τρόελ", "Ρόι Άντερσον", "Ίνγκμαρ Μπέργκμαν"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Ingmar Bergman εξερεύνησε την ταυτότητα, τη σιωπή και τη γυναικεία ψυχολογία μέσα από τη σχέση μιας ηθοποιού που έπαψε να μιλάει (Liv Ullmann) και της νοσοκόμας της (Bibi Andersson).",
    "funFacts": [
      "Η διάσημη σκηνή όπου τα πρόσωπα των δύο πρωταγωνιστριών συγχωνεύονται σε ένα θεωρείται από τις πιο επιδραστικές εικόνες του μοντέρνου σινεμά.",
      "Η ταινία γυρίστηκε στο απομονωμένο σουηδικό νησί Fårö στη Βαλτική Θάλασσα, όπου κατοικούσε ο ίδιος ο Μπέργκμαν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%81%CF%83%CF%8C%CE%BD%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["bergman", "persona", "swedish-cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_105",
    "text": "Ποια αδέλφια θεατράνθρωποι έγραψαν και σκηνοθέτησαν τη σπονδυλωτή σάτιρα της Κατοχής «Το κανόνι και τ' αηδόνι» (1968);",
    "answers": ["Ο Ιάκωβος και ο Γιώργος Καμπανέλλης", "Ο Χρήστος and ο Γιώργος Γιαννακόπουλος", "Ο Αλέκος and ο Κώστας Σακελλάριος", "Ο Νίκος and ο Πολύβιος Βασιλειάδης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Ιάκωβος Καμπανέλλης και ο αδελφός του Γιώργος δημιούργησαν τρεις αυτόνομες σουρεαλιστικές ιστορίες με κοινό άξονα τη συμπεριφορά των κατακτητών απέναντι στους Έλληνες.",
    "funFacts": [
      "Η ταινία διακρίθηκε στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης το 1968 αποσπώντας το Βραβείο Σεναρίου.",
      "Η μουσική επένδυση γράφτηκε από τον Νίκο Μαμαγκάκη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%B1%CE%BD%CF%8C%CE%BD%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%84%27_%CE%B1%CE%B7%CE%B4%CF%8C%CE%BD%CE%B9",
    "locale": "el-GR",
    "tags": ["kambanellis", "greek-cinema", "satire", "occupation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_106",
    "text": "Ποιο επιτραπέζιο παιχνίδι στρατηγικής παίζει ο ιππότης Αντώνιος Μπλοκ ενάντια στον Χάρο στην «Έβδομη Σφραγίδα» (1957);",
    "answers": ["Τάβλι", "Σκάκι", "Ντάμα", "Ζάρια"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Στο αριστούργημα του Ίνγκμαρ Μπέργκμαν, ο σταυροφόρος ιππότης (Max von Sydow) προκαλεί τον Θάνατο σε παρτίδα σκακιού για να κερδίσει χρόνο και απαντήσεις για την ύπαρξη του Θεού.",
    "funFacts": [
      "Η εικόνα του ιππότη να παίζει σκάκι στην ανεμοδαρμένη παραλία με τον μαυροντυμένο Θάνατο είναι μία από τις πιο αναγνωρίσιμες αλληγορίες της έβδομης τέχνης.",
      "Η ταινία κέρδισε το Ειδικό Βραβείο της Επιτροπής στο Φεστιβάλ των Καννών το 1957."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%88%CE%B2%CE%B4%CE%BF%CE%BC%CE%B7_%CE%A3%CF%86%CF%81%CE%B1%CE%B3%CE%AF%CE%B4%CE%B1",
    "locale": "el-GR",
    "tags": ["seventh-seal", "bergman", "chess", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_107",
    "text": "Στη δραματική σειρά «Αναστασία» (Mega, 1993) του Γιώργου Κυρίτση, ποιο τολμηρό ερωτικό θέμα προκάλεσε έντονες συζητήσεις στην κοινωνία;",
    "answers": ["Ο έρωτας δύο ανθρώπων με μεγάλη διαφορά πλούτου", "Ο έρωτας μιας μοναχής με έναν γιατρό", "Η ταυτόχρονη σχέση μιας γυναίκας με πατέρα και γιο", "Ο κρυφός έρωτας δύο πολιτικών αντιπάλων"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η νεαρή Αναστασία (Μυρτώ Αλικάκη) ερωτεύεται κεραυνοβόλα τόσο τον ώριμο επιχειρηματία Παύλο (Μηνά Χατζησάββα) όσο και τον γιο του Αλέξανδρο (Άλκη Κούρκουλο).",
    "funFacts": [
      "Η σειρά κατέγραψε ρεκόρ τηλεθέασης που άγγιζε το 70% στο καθηλωτικό της φινάλε.",
      "Το ομώνυμο τραγούδι των τίτλων σε μουσική Δημήτρη Παπαδημητρίου και ερμηνεία Ελευθερίας Αρβανιτάκη έγινε κλασικό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CE%B1%CF%83%CF%84%CE%B1%CF%83%CE%AF%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "anastasia", "arvanitaki", "mega-channel"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_108",
    "text": "Ποιος σκηνοθέτης υπέγραψε το κυνικό νουάρ «Η Λεωφόρος της Δύσεως» (Sunset Boulevard, 1950) για τη ματαιοδοξία του Χόλιγουντ;",
    "answers": ["Όρσον Γουέλς", "Άλφρεντ Χίτσκοκ", "Τζον Χιούστον", "Μπίλι Γουάιλντερ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Billy Wilder σκηνοθέτησε αυτό το αριστούργημα με πρωταγωνίστρια την πραγματική σταρ του βωβού σινεμά Gloria Swanson ως την ξεχασμένη ντίβα Norma Desmond.",
    "funFacts": [
      "Η ταινία ξεκινά με τον ίδιο τον νεκρό πρωταγωνιστή (William Holden) να αφηγείται την ιστορία του ενώ επιπλέει σε μια πισίνα.",
      "Η ατάκα 'All right, Mr. DeMille, I'm ready for my close-up' ψηφίστηκε στις πιο εμβληματικές όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%9B%CE%B5%CF%89%CF%86%CF%8C%CF%81%CE%BF%CF%82_%CF%84%CE%B7%CF%82_%CE%94%CF%8D%CF%83%CE%B5%CF%89%CF%82",
    "locale": "el-GR",
    "tags": ["billy-wilder", "sunset-boulevard", "film-noir", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_109",
    "text": "Ποιος Γερμανός διευθυντής φωτογραφίας κέρδισε το Όσκαρ Ασπρόμαυρης Φωτογραφίας για τον «Αλέξη Ζορμπά» (1964) στην Κρήτη;",
    "answers": ["Γουόλτερ Λάσαλι (Walter Lassally)", "Σβεν Νίκβιστ", "Τόνινο Ντέλι Κόλι", "Ραούλ Κουτάρ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Walter Lassally υπέγραψε την απαράμιλλη ασπρόμαυρη φωτογραφία στον 'Αλέξη Ζορμπά', την 'Ηλέκτρα' και το 'Κορίτσι με τα μαύρα' του Μιχάλη Κακογιάννη.",
    "funFacts": [
      "Ο Λάσαλι αγάπησε τόσο πολύ την Κρήτη κατά τα γυρίσματα που εγκαταστάθηκε μόνιμα στον Σταυρό Χανίων μέχρι τον θάνατό του το 2017.",
      "Δώρισε το αυθεντικό του αγαλματίδιο Όσκαρ σε παραθαλάσσια ταβέρνα στον Σταυρό Χανίων όπου γυρίστηκε ο χορός του Ζορμπά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%85%CF%8C%CE%BB%CF%84%CE%B5%CF%81_%CE%9B%CE%AC%CF%83%CE%B1%CE%BB%CE%B9",
    "locale": "el-GR",
    "tags": ["walter-lassally", "zorba", "cinematography", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_110",
    "text": "Ποιο αφηγηματικό εύρημα εισήγαγε ο Ακίρα Κουροσάβα στο «Ρασομόν» (1950), δίνοντας το όνομά του σε ψυχολογικό και νομικό φαινόμενο;",
    "answers": ["Η χρήση αναδρομών στο μέλλον", "Το ίδιο γεγονός αφηγημένο από αντικρουόμενες οπτικές γωνίες", "Η ταυτόχρονη δράση σε χωρισμένη οθόνη", "Η αποκάλυψη ότι ο αφηγητής είναι ο ένοχος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Το 'Rashomon effect' περιγράφει πώς ένα έγκλημα παρουσιάζεται από τέσσερις διαφορετικούς μάρτυρες, καθένας εκ των οποίων δίνει μια εντελώς διαφορετική και υποκειμενική εκδοχή.",
    "funFacts": [
      "Η ταινία κέρδισε τον Χρυσό Λέοντα στο Φεστιβάλ Βενετίας και Τιμητικό Όσκαρ, ανοίγοντας τις πόρτες της Δύσης για το ιαπωνικό σινεμά.",
      "Ο Κουροσάβα χρησιμοποίησε καθρέφτες για να αντανακλούν το φυσικό φως του ήλιου στα πρόσωπα των ηθοποιών μέσα στο πυκνό δάσος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B1%CF%83%CE%BF%CE%BC%CF%8C%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["kurosawa", "rashomon", "japanese-cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'medium', 3, questions)

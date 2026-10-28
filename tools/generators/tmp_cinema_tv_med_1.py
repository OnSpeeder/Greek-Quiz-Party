# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_med_011",
    "text": "Ποιος κορυφαίος σκηνοθέτης υπέγραψε το ψυχολογικό νεο-νουάρ αριστούργημα «Ο Ταξιτζής» (Taxi Driver, 1976);",
    "answers": ["Μάρτιν Σκορσέζε", "Μπράιαν Ντε Πάλμα", "Φράνσις Φορντ Κόπολα", "Γουίλιαμ Φρίντκιν"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Martin Scorsese σκηνοθέτησε τον 'Ταξιτζή' σε σενάριο του Paul Schrader, κερδίζοντας τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών το 1976.",
    "funFacts": [
      "Ο Ρόμπερτ Ντε Νίρο δούλεψε πραγματικά ως οδηγός ταξί στη Νέα Υόρκη για 12 ώρες την ημέρα ώστε να προετοιμαστεί για τον ρόλο του Travis Bickle.",
      "Η διάσημη σκηνή στον καθρέφτη με την ατάκα 'You talkin' to me?' ήταν πλήρης αυτοσχεδιασμός του Ντε Νίρο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%A4%CE%B1%CE%BE%CE%B9%CF%84%CE%B6%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["scorsese", "de-niro", "taxi-driver", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_012",
    "text": "Ποιο εμβληματικό τραγούδι του Μάνου Χατζιδάκι από την ταινία «Ποτέ την Κυριακή» (1960) κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού;",
    "answers": ["«Ο κυρ-Αντώνης»", "«Τα παιδιά του Πειραιά»", "«Χάρτινο το φεγγαράκι»", "«Η κυρά»"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Το τραγούδι 'Τα παιδιά του Πειραιά' σε ερμηνεία της Μελίνας Μερκούρη χάρισε στον Μάνο Χατζιδάκι το πρώτο Όσκαρ για ελληνικό τραγούδι.",
    "funFacts": [
      "Ο Μάνος Χατζιδάκις δεν παρευρέθηκε στην τελετή απονομής και για χρόνια κρατούσε αποστασιοποιημένη στάση απέναντι στην τεράστια εμπορική επιτυχία του τραγουδιού.",
      "Η ταινία σκηνοθετήθηκε από τον Ζυλ Ντασσέν και χάρισε στη Μελίνα Μερκούρη το Βραβείο Γυναικείας Ερμηνείας στις Κάννες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%A0%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC_%CF%84%CE%BF%CF%85_%CE%A0%CE%B5%CE%B9%CF%81%CE%B1%CE%B9%CE%AC_(%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9)",
    "locale": "el-GR",
    "tags": ["hadjidakis", "never-on-sunday", "oscars", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_013",
    "text": "Στην καλτ ταινία «Fight Club» (1999), ποιος είναι ο πρώτος και απαράβατος κανόνας της μυστικής λέσχης;",
    "answers": ["«Ποτέ δεν εγκαταλείπεις τη μάχη»", "«Μόνο δύο άτομα σε κάθε αγώνα»", "«Δεν μιλάς ποτέ για το Fight Club»", "«Κανένας δεν φορά παπούτσια»"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο πρώτος (αλλά και ο δεύτερος) κανόνας που θεσπίζει ο Tyler Durden είναι: 'The first rule of Fight Club is: you do not talk about Fight Club'.",
    "funFacts": [
      "Η ταινία του Ντέιβιντ Φίντσερ βασίστηκε στο ομότιτλο βιβλίο του Τσακ Πόλανικ.",
      "Ο Μπραντ Πιτ και ο Έντουαρντ Νόρτον έκαναν μαθήματα πυγμαχίας, ταεκβοντό και παρασκευής σαπουνιού για τις ανάγκες των ρόλων τους."
    ],
    "source": "https://el.wikipedia.org/wiki/Fight_Club",
    "locale": "el-GR",
    "tags": ["fight-club", "fincher", "brad-pitt", "cult-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_014",
    "text": "Ποιος σεναριογράφος και παραγωγός δημιούργησε την εμβληματική δραματική σειρά του HBO «The Sopranos» (1999–2007);",
    "answers": ["Τέρενς Γουίντερ", "Μάθιου Γουάινερ", "Βινς Γκίλιγκαν", "Ντέιβιντ Τσέις"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο David Chase δημιούργησε το 'The Sopranos', βασίζοντας πολλές από τις δυναμικές της μαφιόζικης οικογένειας στη δική του σχέση με τη μητέρα του.",
    "funFacts": [
      "Η σειρά απέσπασε 21 βραβεία Emmy και θεωρείται από τους κριτικούς η απαρχή της 'Χρυσής Εποχής της Τηλεόρασης'.",
      "Ο Τζέιμς Γκαντολφίνι κέρδισε τρία βραβεία Emmy Α' Ανδρικού Ρόλου για την καθηλωτική ερμηνεία του ως Τόνι Σοπράνο."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Sopranos",
    "locale": "el-GR",
    "tags": ["the-sopranos", "hbo", "david-chase", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_015",
    "text": "Ποια κλασική νουβέλα του Τζόζεφ Κόνραντ αποτέλεσε τη βασική λογοτεχνική έμπνευση για το πολεμικό έπος «Αποκάλυψη Τώρα» (1979);",
    "answers": ["«Η καρδιά του σκότους»", "«Λόρδος Τζιμ»", "«Νοστρόμο»", "«Ο μυστικός πράκτορας»"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Φράνσις Φορντ Κόπολα μετέφερε την πλοκή του 'Heart of Darkness' από τον ποταμό Κονγκό της αποικιοκρατικής Αφρικής στον πόλεμο του Βιετνάμ.",
    "funFacts": [
      "Τα γυρίσματα στις Φιλιππίνες ήταν εξαιρετικά επεισοδιακά, διήρκεσαν 238 ημέρες και παραλίγο να καταστρέψουν οικονομικά και σωματικά τον Κόπολα.",
      "Η ταινία κέρδισε τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών το 1979 ενώ βρισκόταν ακόμη σε ημιτελή μορφή (work in progress)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CE%BF%CE%BA%CE%AC%CE%BB%CF%85%CF%88%CE%B7,_%CE%A4%CF%8E%CF%81%CE%B1!",
    "locale": "el-GR",
    "tags": ["apocalypse-now", "coppola", "conrad", "war-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_016",
    "text": "Ποιος Έλληνας σκηνοθέτης υπέγραψε το πολιτικό θρίλερ «Ζ» (1969), κερδίζοντας το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας;",
    "answers": ["Μιχάλης Κακογιάννης", "Κώστας Γαβράς", "Νίκος Κούνδουρος", "Παντελής Βούλγαρης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Costa-Gavras σκηνοθέτησε το 'Ζ', βασισμένο στο ομώνυμο βιβλίο του Βασίλη Βασιλικού για τη δολοφονία του βουλευτή Γρηγόρη Λαμπράκη.",
    "funFacts": [
      "Το 'Ζ' υπήρξε η πρώτη ταινία στην ιστορία των Όσκαρ που προτάθηκε ταυτόχρονα για Καλύτερη Ξενόγλωσση Ταινία και Καλύτερη Ταινία γενικής κατηγορίας.",
      "Η δυναμική μουσική επένδυση της ταινίας γράφτηκε από τον Μίκη Θεοδωράκη, ο οποίος τότε βρισκόταν υπό κατ' οίκον περιορισμό από τη χούντα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["costa-gavras", "z-movie", "oscars", "political-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_017",
    "text": "Ποιος Ιάπωνας δεξιοτέχνης του Studio Ghibli σκηνοθέτησε το αριστούργημα κινουμένων σχεδίων «Ταξίδι στη Χώρα των Θαυμάτων» (Spirited Away, 2001);",
    "answers": ["Ισάο Τακαχάτα", "Μακότο Σινκάι", "Χαγιάο Μιγιαζάκι", "Σατόσι Κον"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Hayao Miyazaki δημιούργησε το 'Spirited Away', το οποίο κέρδισε τη Χρυσή Άρκτο στο Βερολίνο και το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων.",
    "funFacts": [
      "Παραμένει η μοναδική παραδοσιακά σχεδιασμένη στο χέρι και μη αγγλόφωνη ταινία anime που κέρδισε ποτέ το σχετικό Όσκαρ.",
      "Κατείχε για 19 χρόνια το ρεκόρ της πιο κερδοφόρας κινηματογραφικής ταινίας στην ιστορία του ιαπωνικού box office."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CE%BE%CE%AF%CE%B4%CE%B9_%CF%83%CF%84%CE%B7_%CE%A7%CF%8E%CF%81%CE%B1_%CF%84%CF%89%CE%BD_%CE%98%CE%B1%CF%85%CE%BC%CE%AC%CF%84%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["miyazaki", "ghibli", "spirited-away", "anime"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_018",
    "text": "Ποιος Αυστραλός σκηνοθέτης υπέγραψε την προφητική σάτιρα «The Truman Show» (1998) με πρωταγωνιστή τον Τζιμ Κάρεϊ;",
    "answers": ["Τζορτζ Μίλερ", "Μπαζ Λούρμαν", "Μπρους Μπέρεσφορντ", "Πίτερ Γουίαρ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Peter Weir σκηνοθέτησε το 'The Truman Show', προβλέποντας με μοναδική ακρίβεια την έκρηξη των τηλεριάλιτι και της μαζικής επιτήρησης.",
    "funFacts": [
      "Ο Τζιμ Κάρεϊ κέρδισε Χρυσή Σφαίρα Α' Ανδρικού Ρόλου για την πρώτη του μεγάλη στροφή σε δραματικό ρόλο.",
      "Η ταινία ενέπνευσε μια πραγματική ψυχιατρική διαταραχή που ονομάστηκε 'The Truman Show delusion'."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Truman_Show",
    "locale": "el-GR",
    "tags": ["truman-show", "peter-weir", "jim-carrey", "satire"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_019",
    "text": "Ποια σπουδαία τραγωδός ενσάρκωσε την «Ηλέκτρα» στην ομώνυμη υποψήφια για Όσκαρ κινηματογραφική ταινία του Μιχάλη Κακογιάννη (1962);",
    "answers": ["Ειρήνη Παπά", "Μελίνα Μερκούρη", "Αλέκα Κατσέλη", "Έλλη Λαμπέτη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Ειρήνη Παπά έδωσε μια συγκλονιστική ερμηνεία στην τραγωδία του Ευριπίδη, εδραιώνοντας τη διεθνή της φήμη ως κορυφαία τραγωδός.",
    "funFacts": [
      "Η ταινία κέρδισε δύο ειδικά βραβεία στο Φεστιβάλ των Καννών και ήταν υποψήφια για Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας το 1963.",
      "Η λιτή και αυστηρή φωτογραφία του Walter Lassally ανέδειξε με μοναδικό τρόπο τα άγονα τοπία της ελληνικής υπαίθρου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97%CE%BB%CE%AD%CE%BA%CF%84%CF%81%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1962)",
    "locale": "el-GR",
    "tags": ["irene-papas", "cacoyannis", "tragedy", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_020",
    "text": "Στην ταινία επιστημονικής φαντασίας «Inception» (2010), ποιο προσωπικό αντικείμενο (totem) περιστρέφει ο Κομπ για να ελέγξει αν ονειρεύεται;",
    "answers": ["Ένα ζάρι", "Μια μεταλλική σβούρα", "Ένα νόμισμα", "Ένα πιόνι σκακιού"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Dom Cobb (Leonardo DiCaprio) χρησιμοποιεί μια μικρή μεταλλική σβούρα· αν συνεχίσει να γυρίζει ασταμάτητα, γνωρίζει ότι βρίσκεται ακόμα μέσα σε όνειρο.",
    "funFacts": [
      "Το διφορούμενο φινάλε όπου η σβούρα ταλαντεύεται ελαφρώς πριν πέσει το μαύρο στην οθόνη προκάλεσε αμέτρητες συζητήσεις ανάμεσα στους θεατές.",
      "Η ταινία του Κρίστοφερ Νόλαν κέρδισε 4 βραβεία Όσκαρ σε τεχνικές κατηγορίες (Φωτογραφία, Ήχος, Μοντάζ Ήχου, Οπτικά Εφέ)."
    ],
    "source": "https://el.wikipedia.org/wiki/Inception",
    "locale": "el-GR",
    "tags": ["inception", "nolan", "totem", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_021",
    "text": "Σε ποια αμερικανική πόλη εκτυλίσσεται η ρεαλιστική αστυνομική και κοινωνική σειρά του HBO «The Wire» (2002–2008);",
    "answers": ["Φιλαδέλφεια", "Βοστώνη", "Βαλτιμόρη", "Ντιτρόιτ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Το 'The Wire' δημιουργήθηκε από τον πρώην δημοσιογράφο David Simon και διαδραματίζεται στη Βαλτιμόρη του Μέριλαντ, εξετάζοντας τους θεσμούς της πόλης.",
    "funFacts": [
      "Κάθε μία από τις πέντε σεζόν εστιάζει σε διαφορετικό τομέα της πόλης: ναρκωτικά, λιμάνι, πολιτική, σχολεία και εφημερίδες.",
      "Παρότι δεν έκανε ποτέ υψηλή τηλεθέαση ούτε κέρδισε σημαντικά Emmy, κατατάσσεται σταθερά στις σπουδαιότερες σειρές όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Wire",
    "locale": "el-GR",
    "tags": ["the-wire", "hbo", "baltimore", "crime-drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_022",
    "text": "Ποιος κορυφαίος ηθοποιός ενσάρκωσε τον αφελή υπαλληλάκο Θωμά Ματσούκα στο εξπρεσιονιστικό αριστούργημα «Ο δράκος» (1956);",
    "answers": ["Μίμης Φωτόπουλος", "Βασίλης Διαμαντόπουλος", "Μάνος Κατράκης", "Ντίνος Ηλιόπουλος"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Ντίνος Ηλιόπουλος παρέδωσε μια ανεπανάληπτη δραματική ερμηνεία υπό τη σκηνοθεσία του Νίκου Κούνδουρου, υποδυόμενος έναν άνδρα που μοιάζει με έναν καταζητούμενο κακοποιό.",
    "funFacts": [
      "Η ταινία θεωρείται από την Πανελλήνια Ένωση Κριτικών Κινηματογράφου (ΠΕΚΚ) ως η κορυφαία ελληνική ταινία όλων των εποχών.",
      "Το σενάριο συνυπέγραψε ο σπουδαίος θεατρικός συγγραφέας Ιάκωβος Καμπανέλλης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%94%CF%81%CE%AC%CE%BA%CE%BF%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "koundouros", "o-drakos", "iliopoulos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_023",
    "text": "Ποιο είναι το όνομα της πορτοκαλί γάτας που κρατά συντροφιά στην Έλεν Ρίπλεϊ στο διαστημόπλοιο Nostromo στην ταινία «Alien» (1979);",
    "answers": ["Τζόουνσι (Jonesy)", "Μίλο", "Όλιβερ", "Φίγκαρο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jonesy είναι η γάτα του πληρώματος και μαζί με τη Ripley (Sigourney Weaver) είναι οι μοναδικοί επιζώντες από την επίθεση του Ξενομόρφου στο Nostromo.",
    "funFacts": [
      "Τέσσερις διαφορετικές εκπαιδευμένες γάτες χρησιμοποιήθηκαν στα γυρίσματα της ταινίας του Ρίντλεϊ Σκοτ.",
      "Η ταινία κέρδισε το Όσκαρ Καλύτερων Οπτικών Εφέ για τον εφιαλτικό σχεδιασμό του εξωγήινου από τον Ελβετό καλλιτέχνη H.R. Giger."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%B9%CE%B5%CE%BD:_%CE%9F_%CE%95%CF%80%CE%B9%CE%B2%CE%AC%CF%84%CE%B7%CF%82_%CF%84%CE%BF%CF%85_%CE%94%CE%B9%CE%B1%CF%83%CF%84%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["alien", "ripley", "ridley-scott", "sci-fi-horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_024",
    "text": "Ποιο διάσημο αδελφικό σκηνοθετικό δίδυμο δημιούργησε το παγωμένο αστυνομικό θρίλερ «Fargo» (1996);",
    "answers": ["Αδελφοί Γουατσόφσκι", "Αδελφοί Κοέν (Τζόελ και Ίθαν)", "Αδελφοί Ρούσο", "Αδελφοί Νταρντέν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Οι Joel και Ethan Coen έγραψαν και σκηνοθέτησαν το 'Fargo', κερδίζοντας το Όσκαρ Πρωτότυπου Σεναρίου.",
    "funFacts": [
      "Η Φράνσις ΜακΝτόρμαντ κέρδισε το Όσκαρ Α' Γυναικείου Ρόλου υποδυόμενη την έγκυο αστυνομικό διευθύντρια Marge Gunderson.",
      "Παρότι η ταινία ξεκινά με την ψευδή δήλωση 'Αυτή είναι μια αληθινή ιστορία', τα γεγονότα ήταν σχεδόν εξ ολοκλήρου προϊόν μυθοπλασίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%AC%CF%81%CE%B3%CE%BA%CE%BF_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["fargo", "coen-brothers", "crime", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_025",
    "text": "Ποιο εμβληματικό οργανικό ζεϊμπέκικο του Μάνου Λοΐζου γράφτηκε για την ταινία «Ευδοκία» (1971) του Αλέξη Δαμιανού;",
    "answers": ["«Το ζεϊμπέκικο του Πειραιά»", "«Το ζεϊμπέκικο της ξενιτιάς»", "«Το ζεϊμπέκικο της Ευδοκίας»", "«Ο χορός του λοχαγού»"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Το 'Ζεϊμπέκικο της Ευδοκίας' αποτελεί ένα από τα πιο αναγνωρίσιμα και συγκλονιστικά οργανικά κομμάτια στην ιστορία της ελληνικής μουσικής.",
    "funFacts": [
      "Στην αυθεντική ηχογράφηση, το σόλο μπουζούκι έπαιξε ο δεξιοτέχνης μουσικός Θανάσης Πολυκανδριώτης.",
      "Η ταινία θεωρείται σταθμός του Νέου Ελληνικού Κινηματογράφου για τον ωμό ρεαλισμό και την ποιητική της δύναμη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CE%B4%CE%BF%CE%BA%CE%AF%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["evdokia", "loizos", "zeibekiko", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_026",
    "text": "Ποιος ηθοποιός κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου υποδυόμενος τον οξύθυμο γκάνγκστερ Τόμι ΝτεΒίτο στα «Καλά Παιδιά» (Goodfellas, 1990);",
    "answers": ["Ρόμπερτ Ντε Νίρο", "Ρέι Λιότα", "Πολ Σορβίνο", "Τζο Πέσι"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Joe Pesci απέσπασε το Όσκαρ για την εκρηκτική ερμηνεία του στην ταινία του Μάρτιν Σκορσέζε, παραδίδοντας και τον διάσημο αυτοσχεδιασμό 'Funny how?'.",
    "funFacts": [
      "Ο ευχαριστήριος λόγος του στην απονομή των Όσκαρ ήταν από τους συντομότερους στην ιστορία: 'Ήταν τιμή μου. Ευχαριστώ', και αποχώρησε.",
      "Η ταινία βασίστηκε στο βιβλίο 'Wiseguy' του ερευνητή δημοσιογράφου Nicholas Pileggi."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%9A%CE%B1%CE%BB%CE%AC_%CE%A0%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC",
    "locale": "el-GR",
    "tags": ["goodfellas", "joe-pesci", "scorsese", "mafia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_027",
    "text": "Ποιος Ιταλός σκηνοθέτης υπέγραψε το νοσταλγικό αριστούργημα «Σινεμά ο Παράδεισος» (Nuovo Cinema Paradiso, 1988);",
    "answers": ["Τζουζέπε Τορνατόρε", "Μπερνάρντο Μπερτολούτσι", "Ρομπέρτο Μπενίνι", "Πάολο Σορεντίνο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Giuseppe Tornatore σκηνοθέτησε την ταινία, κερδίζοντας το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας και το Μέγα Ειδικό Βραβείο στις Κάννες.",
    "funFacts": [
      "Η συγκινητική μουσική επένδυση συντέθηκε από τον θρυλικό Ένιο Μορικόνε σε συνεργασία με τον γιο του Αντρέα.",
      "Η τελική σκηνή με το μοντάζ των λογοκριμένων φιλιών θεωρείται μία από τις πιο συγκινητικές ερωτικές επιστολές προς την έβδομη τέχνη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B9%CE%BD%CE%B5%CE%BC%CE%AC_%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["cinema-paradiso", "tornatore", "morricone", "italian-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_028",
    "text": "Ποιος σκηνοθέτης γύρισε το δραματικό αριστούργημα «Το κορίτσι με τα μαύρα» (1956) στο νησί της Ύδρας με την Έλλη Λαμπέτη;",
    "answers": ["Γιώργος Τζαβέλλας", "Μιχάλης Κακογιάννης", "Ντίνος Δημόπουλος", "Γιάννης Δαλιανίδης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Μιχάλης Κακογιάννης σκηνοθέτησε την ταινία σε δικό του σενάριο, κερδίζοντας τη Χρυσή Σφαίρα Καλύτερης Ξενόγλωσσης Ταινίας το 1957.",
    "funFacts": [
      "Η ταινία ανέδειξε διεθνώς την ομορφιά της Ύδρας, μετατρέποντας το νησί σε πόλο έλξης καλλιτεχνών από όλο τον κόσμο.",
      "Συμπρωταγωνιστής της Έλλης Λαμπέτη ήταν ο Δημήτρης Χορν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%BF%CF%81%CE%AF%CF%84%CF%83%CE%B9_%CE%BC%CE%B5_%CF%84%CE%B1_%CE%BC%CE%AC%CF%85%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["cacoyannis", "lambeti", "hydra", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_029",
    "text": "Από ποια νευρολογική πάθηση υποφέρει ο ήρωας Λέοναρντ Σέλμπι στο ανατρεπτικό θρίλερ «Memento» (2000) του Κρίστοφερ Νόλαν;",
    "answers": ["Οπισθοδρομική αμνησία", "Ναρκοληψία", "Προσθογράμ Card (προσθόδρομη αμνησία)", "Προσωπαγνωσία"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Leonard (Guy Pearce) έχει χάσει την ικανότητα να δημιουργεί νέες αναμνήσεις μετά από ένα χτύπημα στο κεφάλι και χρησιμοποιεί τατουάζ και φωτογραφίες Polaroid για να ερευνήσει τη δολοφονία της γυναίκας του.",
    "funFacts": [
      "Η ταινία αφηγείται τα γεγονότα με δύο παράλληλες γραμμές: οι έγχρωμες σκηνές κινούνται αντίστροφα στον χρόνο και οι ασπρόμαυρες προς τα εμπρός.",
      "Το σενάριο βασίστηκε στο διήγημα 'Memento Mori' του αδελφού του σκηνοθέτη, Τζόναθαν Νόλαν."
    ],
    "source": "https://el.wikipedia.org/wiki/Memento_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["memento", "nolan", "thriller", "indie-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_030",
    "text": "Στη βραβευμένη σειρά εποχής «Mad Men», ποια διαφημιστική εταιρεία της Μάντισον Άβενιου αποτελεί το βασικό εργασιακό περιβάλλον;",
    "answers": ["BBDO", "Ogilvy & Mather", "McCann Erickson", "Sterling Cooper"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Sterling Cooper είναι η φανταστική διαφημιστική εταιρεία της Νέας Υόρκης της δεκαετίας του 1960 όπου διευθυντής δημιουργικού είναι ο Don Draper (Jon Hamm).",
    "funFacts": [
      "Η σειρά του Matthew Weiner κέρδισε τέσσερα συνεχόμενα βραβεία Emmy Καλύτερης Δραματικής Σειράς (2008–2011).",
      "Επαινέθηκε ιδιαίτερα από ιστορικούς για την απαράμιλλη ακρίβεια στην απεικόνιση των κοστουμιών, των επίπλων και της κοινωνικής ατμόσφαιρας των 60s."
    ],
    "source": "https://el.wikipedia.org/wiki/Mad_Men",
    "locale": "el-GR",
    "tags": ["mad-men", "don-draper", "sterling-cooper", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_031",
    "text": "Ποιο ιστορικό αριστούργημα του Φεντερίκο Φελίνι (1960) με πρωταγωνιστή τον Μαρτσέλο Μαστρογιάννι κατέγραψε τη νυχτερινή ζωή της Ρώμης;",
    "answers": ["Γλυκιά ζωή (La Dolce Vita)", "8½", "Λα Στράντα", "Νύχτες της Καμπίρια"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Το 'La Dolce Vita' κέρδισε τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών και καθιέρωσε τον όρο 'paparazzo' για τους φωτογράφους διασημοτήτων.",
    "funFacts": [
      "Η σκηνή όπου η Ανίτα Έκμπεργκ μπαίνει στο συντριβάνι της Φοντάνα ντι Τρέβι μέσα στη νύχτα είναι μία από τις πιο εμβληματικές στην ιστορία του κινηματογράφου.",
      "Το Βατικανό καταδίκασε επίσημα την ταινία ως ανήθικη κατά την πρώτη κυκλοφορία της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BB%CF%85%CE%BA%CE%B9%CE%AC_%CE%B6%CF%89%CE%AE_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["fellini", "la-dolce-vita", "italian-cinema", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_032",
    "text": "Ποιος κορυφαίος σκηνοθέτης υπέγραψε το δικαστικό δράμα «Οι 12 ένορκοι» (12 Angry Men, 1957) με πρωταγωνιστή τον Χένρι Φόντα;",
    "answers": ["Ελία Καζάν", "Σίντνεϊ Λουμέτ", "Μπίλι Γουάιλντερ", "Φρεντ Τσίνεμαν"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Sidney Lumet έκανε το εντυπωσιακό σκηνοθετικό του ντεμπούτο στον κινηματογράφο με τους '12 Ενόρκους', γυρίζοντας σχεδόν ολόκληρη την ταινία μέσα σε ένα δωμάτιο συσκέψεων.",
    "funFacts": [
      "Ο Λουμέτ χρησιμοποίησε σταδιακά μεγαλύτερους φακούς εστιακής απόστασης για να προκαλέσει ένα αυξανόμενο αίσθημα κλειστοφοβίας καθώς η ένταση κλιμακωνόταν.",
      "Η ταινία κατέχει βαθμολογία 100% στο Rotten Tomatoes και κατατάσσεται σταθερά στην πρώτη δεκάδα του IMDb Top 250."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_12_%CE%AD%CE%BD%CE%BF%CF%81%CE%BA%CE%BF%CE%B9_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1957)",
    "locale": "el-GR",
    "tags": ["12-angry-men", "sidney-lumet", "courtroom-drama", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_033",
    "text": "Στην πολυβραβευμένη δραματική σειρά του HBO «Succession», ποιος είναι ο κολοσσιαίος όμιλος μέσων ενημέρωσης της οικογένειας Ρόι;",
    "answers": ["Ewing Oil", "InGen", "Waystar Royco", "Delos Destinations"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Waystar Royco είναι ένας διεθνής όμιλος μέσων ενημέρωσης, κρουαζιέρας και ψυχαγωγίας που ίδρυσε ο πατριάρχης Logan Roy (Brian Cox).",
    "funFacts": [
      "Η σειρά απέσπασε 19 βραβεία Primetime Emmy, κερδίζοντας τρεις φορές το Emmy Καλύτερης Δραματικής Σειράς.",
      "Ο δημιουργός Jesse Armstrong εμπνεύστηκε στοιχεία της δυναστείας από πραγματικές οικογένειες μεγιστάνων όπως οι Murdochs και οι Redstones."
    ],
    "source": "https://el.wikipedia.org/wiki/Succession",
    "locale": "el-GR",
    "tags": ["succession", "hbo", "waystar-royco", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_034",
    "text": "Ποιος σπουδαίος δημιουργός σκηνοθέτησε και αφηγήθηκε την πρώτη σπονδυλωτή ταινία του ελληνικού σινεμά «Η κάλπικη λίρα» (1955);",
    "answers": ["Αλέκος Σακελλάριος", "Νίκος Κούνδουρος", "Γιάννης Δαλιανίδης", "Γιώργος Τζαβέλλας"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Γιώργος Τζαβέλλας έγραψε και σκηνοθέτησε αυτό το αριστούργημα, παρακολουθώντας την πορεία μιας κίβδηλης χρυσής λίρας μέσα από τέσσερις διαφορετικές ιστορίες.",
    "funFacts": [
      "Στην ταινία πρωταγωνιστεί η αφρόκρεμα του ελληνικού θεάτρου: Βασίλης Λογοθετίδης, Ίλια Λιβυκού, Μίμης Φωτόπουλος, Έλλη Λαμπέτη και Δημήτρης Χορν.",
      "Συγκαταλέγεται στις κορυφαίες ταινίες του ελληνικού κινηματογράφου και γνώρισε μεγάλη επιτυχία σε φεστιβάλ του εξωτερικού."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%BA%CE%AC%CE%BB%CF%80%CE%B9%CE%BA%CE%B7_%CE%BB%CE%AF%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "tzavellas", "i-kalpiki-lira", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_035",
    "text": "Ποιος σκηνοθέτης με απαράμιλλη οπτική συμμετρία και παστέλ χρωματικές παλέτες υπέγραψε το «Ξενοδοχείο Grand Budapest» (2014);",
    "answers": ["Γουές Άντερσον", "Τιμ Μπάρτον", "Τέρι Γκίλιαμ", "Σπάικ Τζόνζι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Wes Anderson σκηνοθέτησε το 'The Grand Budapest Hotel', κερδίζοντας τέσσερα βραβεία Όσκαρ και τη Χρυσή Σφαίρα Καλύτερης Κωμωδίας.",
    "funFacts": [
      "Η ταινία γυρίστηκε σε τρία διαφορετικά aspect ratios (1.37:1, 1.85:1, 2.35:1) για να αντιστοιχούν στις τρεις διαφορετικές χρονικές περιόδους της ιστορίας.",
      "Ο πρωταγωνιστής Ρέιφ Φάινς έδωσε μία από τις πιο αναγνωρισμένες ερμηνείες του ως ο εκκεντρικός θυρωρός Monsieur Gustave H."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9E%CE%B5%CE%BD%CE%BF%CE%B4%CE%BF%CF%87%CE%B5%CE%AF%CE%BF_Grand_Budapest",
    "locale": "el-GR",
    "tags": ["wes-anderson", "grand-budapest-hotel", "indie", "cinematography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_036",
    "text": "Στη σειρά μυστηρίου «Έτερος Εγώ», ποια είναι η ειδικότητα του εκκεντρικού πρωταγωνιστή Δημήτρη Λαΐνη (Πυγμαλίων Δαδακαρίδης);",
    "answers": ["Ιατροδικαστής", "Καθηγητής Εγκληματολογίας", "Εισαγγελέας εφετών", "Ψυχίατρος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Δημήτρης Λαΐνης είναι καθηγητής εγκληματολογίας με σύνδρομο Asperger, ο οποίος βοηθά την αστυνομία στην επίλυση σύνθετων υποθέσεων serial killers.",
    "funFacts": [
      "Η σειρά δημιουργήθηκε από τον Σωτήρη Τσαφούλια μετά την ομώνυμη επιτυχημένη κινηματογραφική ταινία του 2016.",
      "Αποτέλεσε την πρώτη ελληνική παραγωγή επιπέδου streaming που απέκτησε φανατικό κοινό σε Cosmote TV και διαδίκτυο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CF%84%CE%B5%CF%81%CE%BF%CF%82_%CE%95%CE%B3%CF%8E_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-tv", "eteros-ego", "crime-mystery", "tsafoulias"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_037",
    "text": "Στην ταινία «Καμιά Πατρίδα για τους Μελλοθάνατους» (2007), ποιο ασυνήθιστο όπλο κρατά ο αδίστακτος εκτελεστής Άντον Σιγκούρ (Χαβιέ Μπαρδέμ);",
    "answers": ["Φλογοβόλο", "Τόξο με δηλητήριο", "Πιστόλι πεπιεσμένου αέρα για βοοειδή", "Ακτινικό πριόνι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Anton Chigurh χρησιμοποιεί ένα όπλο σφαγής βοοειδών με πεπιεσμένο αέρα (captive bolt pistol) για να εξολοθρεύει τα θύματά του και να παραβιάζει κλειδαριές.",
    "funFacts": [
      "Ο Javier Bardem κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου, γινόμενος ο πρώτος Ισπανός ηθοποιός που απέσπασε ποτέ Όσκαρ υποκριτικής.",
      "Η ταινία των αδελφών Κοέν κέρδισε συνολικά 4 βραβεία Όσκαρ, συμπεριλαμβανομένου αυτού της Καλύτερης Ταινίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BC%CE%B9%CE%AC_%CE%A0%CE%B1%CF%84%CF%81%CE%AF%CE%B4%CE%B1_%CE%B3%CE%B9%CE%B1_%CF%84%CE%BF%CF%85%CF%82_%CE%9C%CE%B5%CE%BB%CE%BB%CE%BF%CE%B8%CE%AC%CE%BD%CE%B1%CF%84%CE%BF%CF%85%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["no-country-for-old-men", "bardem", "coen-brothers", "thriller"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_038",
    "text": "Ποιος σουρεαλιστής σκηνοθέτης δημιούργησε μαζί με τον Μαρκ Φροστ την πρωτοποριακή σειρά μυστηρίου «Twin Peaks» (1990–1991);",
    "answers": ["Ντέιβιντ Κρόνενμπεργκ", "Τζον Κάρπεντερ", "Όλιβερ Στόουν", "Ντέιβιντ Λιντς"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο David Lynch συνδύασε σαπουνόπερα, υπερφυσικό τρόμο και αστυνομική έρευνα γύρω από το ερώτημα 'Ποιος σκότωσε τη Λόρα Πάλμερ;'.",
    "funFacts": [
      "Η ατμοσφαιρική μουσική του Angelo Badalamenti απέσπασε βραβείο Grammy και έγινε ένα από τα πιο αναγνωρίσιμα soundtracks.",
      "Ο πράκτορας του FBI Dale Cooper (Kyle MacLachlan) είχε εμμονή με τον ζεστό μαύρο καφέ και την κερασόπιτα."
    ],
    "source": "https://el.wikipedia.org/wiki/Twin_Peaks",
    "locale": "el-GR",
    "tags": ["twin-peaks", "david-lynch", "mystery", "cult-tv"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_039",
    "text": "Ποιος κορυφαίος συνθέτης έγραψε τη μουσική και τα τραγούδια για τη βραβευμένη ταινία «Ρεμπέτικο» (1983) του Κώστα Φέρρη;",
    "answers": ["Σταύρος Ξαρχάκος", "Μάνος Χατζιδάκις", "Μίκης Θεοδωράκης", "Διονύσης Σαββόπουλος"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Σταύρος Ξαρχάκος συνέθεσε σε στίχους του Νίκου Γκάτσου αριστουργήματα όπως 'Το δίχτυ' και 'Μάνα μου Ελλάς' για την ταινία.",
    "funFacts": [
      "Η ταινία κέρδισε την Αργυρή Άρκτο στο Φεστιβάλ Κινηματογράφου του Βερολίνου το 1984.",
      "Η υπόθεση είναι ελεύθερα βασισμένη στη μυθιστορηματική ζωή της θρυλικής ρεμπέτισσας Μαρίκας Νίνου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B5%CE%BC%CF%80%CE%AD%CF%84%CE%B9%CE%BA%CE%BF_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["rebetiko", "xarchakos", "ferris", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_040",
    "text": "Ποιο μουσικό όργανο παίζει με μανία μέχρι εξαντλήσεως ο νεαρός Άντριου Νίμαν στην οσκαρική ταινία «Whiplash» (2014);",
    "answers": ["Σαξόφωνο", "Τύμπανα (ντραμς)", "Τρομπέτα", "Κοντραμπάσο"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Andrew Neiman (Miles Teller) φιλοδοξεί να γίνει ένας από τους κορυφαίους τζαζ ντράμερ, υπομένοντας την ψυχολογική κακοποίηση του μαέστρου Terence Fletcher (J.K. Simmons).",
    "funFacts": [
      "Ο J.K. Simmons κέρδισε το Όσκαρ Β' Ανδρικού Ρόλου για την καθηλωτική ερμηνεία του τυραννικού μαέστρου.",
      "Ο ηθοποιός Miles Teller έπαιζε πράγματι ντραμς από τα 15 του χρόνια και εκτέλεσε το μεγαλύτερο μέρος των σόλο στην ταινία."
    ],
    "source": "https://el.wikipedia.org/wiki/Whiplash_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_2014)",
    "locale": "el-GR",
    "tags": ["whiplash", "jazz", "chazelle", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_041",
    "text": "Στη σειρά μυστηρίου «Lost», ποιος ήταν ο αριθμός της μοιραίας πτήσης της Oceanic Airlines που συνετρίβη στο νησί;",
    "answers": ["Πτήση 777", "Πτήση 404", "Πτήση 815", "Πτήση 216"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η πτήση Oceanic 815 εκτελούσε το δρομολόγιο από το Σίδνεϊ προς το Λος Άντζελες πριν διαλυθεί στον αέρα πάνω από ένα αχαρτογράφητο νησί στον Ειρηνικό.",
    "funFacts": [
      "Ο μυστηριώδης συνδυασμός αριθμών της σειράς ήταν 4, 8, 15, 16, 23, 42, με το 8 και το 15 να σχηματίζουν τον αριθμό της πτήσης.",
      "Το πιλοτικό επεισόδιο του J.J. Abrams ήταν εκείνη την εποχή το πιο ακριβό στην ιστορία της τηλεόρασης με κόστος άνω των 12 εκατομμυρίων δολαρίων."
    ],
    "source": "https://el.wikipedia.org/wiki/Lost",
    "locale": "el-GR",
    "tags": ["lost", "oceanic-815", "mystery", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_042",
    "text": "Ποιος ιδιοσυγκρασιακός σκηνοθέτης υπέγραψε την καλτ κωμωδία δρόμου «Ας περιμένουν οι γυναίκες» (1998) με τον Γιάννη Ζουγανέλη;",
    "answers": ["Νίκος Παναγιωτόπουλος", "Κωνσταντίνος Γιάνναρης", "Νίκος Νικολαΐδης", "Σταύρος Τσιώλης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Σταύρος Τσιώλης δημιούργησε μία από τις πιο αναγνωρίσιμες καλτ κωμωδίες του σύγχρονου ελληνικού σινεμά, καταγράφοντας το ταξίδι τριών μπατζανάκηδων προς τη Θάσο.",
    "funFacts": [
      "Οι ατάκες της ταινίας, όπως 'Ψήφισε η μάνα μου Νέα Δημοκρατία;', έγιναν διαχρονικά memes και συνθήματα στα μέσα κοινωνικής δικτύωσης.",
      "Στην ταινία πρωταγωνίστησαν ο Γιάννης Ζουγανέλης, ο Αργύρης Μπακιρτζής και ο Σάκης Μπουλάς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%82_%CF%80%CE%B5%CF%81%CE%B9%CE%BC%CE%AD%CE%BD%CE%BF%CF%85%CE%BD_%CE%BF%CE%B9_%CE%B3%CF%85%CE%BD%CE%B1%CE%AF%CE%BA%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "tsaiolis", "zouganelis", "cult-comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_043",
    "text": "Ποιο είναι το επάγγελμα του καθηλωμένου σε αναπηρικό καροτσάκι πρωταγωνιστή στην ταινία «Σιωπηλός Μάρτυς» (Rear Window, 1954);",
    "answers": ["Φωτορεπόρτερ", "Ιδιωτικός ντετέκτιβ", "Αρχιτέκτονας", "Συγγραφέας αστυνομικών βιβλίων"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο L.B. Jefferies (James Stewart) είναι επαγγελματίας φωτορεπόρτερ που έσπασε το πόδι του και σκοτώνει την ώρα του παρατηρώντας τους γείτονές του με τηλεφακό.",
    "funFacts": [
      "Ολόκληρη η ταινία του Άλφρεντ Χίτσκοκ γυρίστηκε σε ένα γιγάντιο ενιαίο σκηνικό στα στούντιο της Paramount, που αναπαριστούσε 31 διαμερίσματα.",
      "Συμπρωταγωνίστρια ήταν η πανέμορφη Γκρέις Κέλι στον ρόλο της κοσμικής συντρόφου του Lisa Fremont."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B9%CF%89%CF%80%CE%B7%CE%BB%CF%8C%CF%82_%CE%9C%CE%AC%CF%81%CF%84%CF%85%CF%82",
    "locale": "el-GR",
    "tags": ["hitchcock", "rear-window", "james-stewart", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_044",
    "text": "Ποιο μουσικό είδος και η ιστορία του βρίσκονται στον πυρήνα της ιστορικής τηλεοπτικής σειράς της ΕΡΤ «Το Μινόρε της Αυγής» (1983–1984);",
    "answers": ["Το ελαφρό τραγούδι", "Το ρεμπέτικο τραγούδι", "Η επτανησιακή καντάδα", "Το δημοτικό τραγούδι"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η σειρά σε σκηνοθεσία Φώτη Μεσθεναίου κατέγραψε τη γέννηση και την ακμή της ρεμπέτικης κομπανίας του Πειραιά στον Μεσοπόλεμο.",
    "funFacts": [
      "Η επιτυχία της σειράς προκάλεσε τεράστια αναβίωση του ενδιαφέροντος της νεολαίας για το ρεμπέτικο και λαϊκό τραγούδι τη δεκαετία του '80.",
      "Στη σειρά πρωταγωνίστησαν ο Αντώνης Καφετζόπουλος, ο Δημήτρης Καταλειφός και ο Τίμος Περλέγκας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BC%CE%B9%CE%BD%CF%8C%CF%81%CE%B5_%CF%84%CE%B7%CF%82_%CE%B1%CF%85%CE%B3%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-minore-tis-avgis", "ert", "rebetiko"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_045",
    "text": "Ποιος Μεξικανός σκηνοθέτης υπέγραψε το σκοτεινό παραμύθι «Ο Λαβύρινθος του Πάνα» (El laberinto del fauno, 2006);",
    "answers": ["Αλεχάντρο Γκονσάλες Ινιάριτου", "Αλφόνσο Κουαρόν", "Γκιγιέρμο ντελ Τόρο", "Ρόμπερτ Ροντρίγκεζ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Guillermo del Toro συνδύασε τη σκληρή πραγματικότητα της μετεμφυλιακής Ισπανίας του Φράνκο με έναν μαγικό, απόκοσμο υπόγειο κόσμο.",
    "funFacts": [
      "Η ταινία απέσπασε διθυραμβικές κριτικές και κέρδισε τρία βραβεία Όσκαρ (Φωτογραφία, Καλλιτεχνική Διεύθυνση, Μακιγιάζ).",
      "Ο ηθοποιός Doug Jones ενσάρκωσε με ειδικά προσθετικά τόσο τον επιβλητικό Πάνα όσο και το ανατριχιαστικό τέρας Pale Man."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9B%CE%B1%CE%B2%CF%8D%CF%81%CE%B9%CE%BD%CE%B8%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A0%CE%AC%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["pans-labyrinth", "del-toro", "dark-fantasy", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_046",
    "text": "Ποιον σπουδαίο ιστορικό εφευρέτη υποδύθηκε ο ροκ σταρ Ντέιβιντ Μπόουι στην ταινία «The Prestige» (2006);",
    "answers": ["Τόμας Έντισον", "Αλεξάντερ Γκράχαμ Μπελ", "Γουλιέλμο Μαρκόνι", "Νίκολα Τέσλα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο David Bowie έκανε μια αξιομνημόνευτη εμφάνιση ως ο εκκεντρικός εφευρέτης Nikola Tesla, που κατασκευάζει μια παράδοξη συσκευή τηλεμεταφοράς.",
    "funFacts": [
      "Ο σκηνοθέτης Κρίστοφερ Νόλαν δήλωσε ότι ο Μπόουι ήταν η μοναδική του επιλογή για τον ρόλο και ταξίδεψε προσωπικά στη Νέα Υόρκη για να τον πείσει.",
      "Η ταινία αφηγείται τη μοιραία αντιπαλότητα δύο ταχυδακτυλουργών του 19ου αιώνα (Hugh Jackman και Christian Bale)."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Prestige_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["the-prestige", "david-bowie", "tesla", "nolan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_047",
    "text": "Ποια κορυφαία θεατρική ηθοποιός έκανε το κινηματογραφικό της ντεμπούτο στην ταινία «Κυριακάτικο ξύπνημα» (1954) του Μιχάλη Κακογιάννη;",
    "answers": ["Έλλη Λαμπέτη", "Μαίρη Αρώνη", "Άννα Συνοδινού", "Αλέκα Παΐζη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Έλλη Λαμπέτη πρωταγωνίστησε ως η νεαρή Μίνα που χάνει ένα λαχείο στην πλαζ, σε μια ανάλαφρη ρομαντική κωμωδία που έλαβε μέρος στο Φεστιβάλ των Καννών.",
    "funFacts": [
      "Η ταινία σηματοδότησε την πρώτη σκηνοθετική απόπειρα του Μιχάλη Κακογιάννη στον ελληνικό κινηματογράφο.",
      "Η χημεία της Λαμπέτη με τον Δημήτρη Χορν και τον Γιώργο Παππά υπήρξε υποδειγματική."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%85%CF%81%CE%B9%CE%B1%CE%BA%CE%AC%CF%84%CE%B9%CE%BA%CE%BF_%CE%BE%CF%8D%CF%80%CE%BD%CE%B7%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "lambeti", "cacoyannis", "horn"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_048",
    "text": "Ποιο θρησκευτικό μοτίβο συνδέει τις φρικιαστικές δολοφονίες στο σκοτεινό ψυχολογικό θρίλερ «Seven» (1995) του Ντέιβιντ Φίντσερ;",
    "answers": ["Οι Δέκα Εντολές", "Τα Επτά Θανάσιμα Αμαρτήματα", "Οι Επτά Πληγές του Φαραώ", "Οι Τέσσερις Καβαλάρηδες της Αποκάλυψης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο serial killer John Doe (Kevin Spacey) εκτελεί μια σειρά από τελετουργικούς φόνους εμπνευσμένους από τα επτά θανάσιμα αμαρτήματα.",
    "funFacts": [
      "Η σοκαριστική τελική σκηνή στην έρημο με το μυστηριώδες κουτί ('What's in the box?') θεωρείται από τις πιο έντονες στην ιστορία του κινηματογράφου.",
      "Ο Μπραντ Πιτ επέβαλε στο στούντιο να μην αλλαχθεί το σκοτεινό τέλος, απειλώντας ότι θα αποχωρούσε από το έργο."
    ],
    "source": "https://el.wikipedia.org/wiki/Seven_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["seven", "fincher", "brad-pitt", "thriller"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_049",
    "text": "Ποια Βρετανίδα δημιουργός και ηθοποιός έγραψε και πρωταγωνίστησε στην πολυβραβευμένη κωμική σειρά «Fleabag» (BBC/Amazon);",
    "answers": ["Μικαέλα Κόελ", "Σάρον Χόργκαν", "Φίμπι Γουόλερ-Μπριτζ", "Ολίβια Κόλμαν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Phoebe Waller-Bridge έγραψε και πρωταγωνίστησε στο 'Fleabag', κερδίζοντας 6 βραβεία Primetime Emmy για τη δεύτερη σεζόν της σειράς.",
    "funFacts": [
      "Η σειρά ξεκίνησε αρχικά ως σόλο θεατρικός μονόλογος της Waller-Bridge στο Φεστιβάλ Fringe του Εδιμβούργου το 2013.",
      "Χαρακτηριστικό γνώρισμα της σειράς είναι το διαρκές σπάσιμο του 'τέταρτου τοίχου', καθώς η ηρωίδα κοιτάζει και μιλά απευθείας στην κάμερα."
    ],
    "source": "https://el.wikipedia.org/wiki/Fleabag",
    "locale": "el-GR",
    "tags": ["fleabag", "waller-bridge", "comedy", "emmy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_050",
    "text": "Ποιος κορυφαίος μουσικοσυνθέτης υπέγραψε το διάσημο «Συρτάκι του Ζορμπά» για την ταινία «Αλέξης Ζορμπάς» (1964);",
    "answers": ["Μάνος Χατζιδάκις", "Σταύρος Ξαρχάκος", "Γιάννης Μαρκόπουλος", "Μίκης Θεοδωράκης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Μίκης Θεοδωράκης συνέθεσε το παγκοσμίως διάσημο συρτάκι, το οποίο ταυτίστηκε διεθνώς με την Ελλάδα και τον χορό του Άντονι Κουίν.",
    "funFacts": [
      "Η ταινία του Μιχάλη Κακογιάννη κέρδισε τρία βραβεία Όσκαρ: Β' Γυναικείου Ρόλου (Lila Kedrova), Φωτογραφίας και Καλλιτεχνικής Διεύθυνσης.",
      "Ο χορός του Ζορμπά δημιουργήθηκε σταδιακά στα γυρίσματα επειδή ο Άντονι Κουίν είχε τραυματίσει το πόδι του και δεν μπορούσε να κάνει γρήγορα πηδήματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AD%CE%BE%CE%B7%CF%82_%CE%96%CE%BF%CF%81%CE%BC%CF%80%CE%AC%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["zorba-the-greek", "theodorakis", "cacoyannis", "greek-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_051",
    "text": "Ποιος θρύλος του παγκόσμιου κινηματογράφου σκηνοθέτησε και πρωταγωνίστησε στην αντιπολεμική σάτιρα «Ο Μεγάλος Δικτάτωρ» (1940);",
    "answers": ["Τσάρλι Τσάπλιν", "Μπάστερ Κίτον", "Όρσον Γουέλς", "Χάρολντ Λόιντ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Charlie Chaplin σατίρισε ανοιχτά τον Αδόλφο Χίτλερ και τον φασισμό, υποδυόμενος τόσο τον δικτάτορα Αντενόιντ Χίνκελ όσο και έναν φτωχό Εβραίο κουρέα.",
    "funFacts": [
      "Υπήρξε η πρώτη ταινία με πλήρη διάλογο και συγχρονισμένο ήχο στην καριέρα του Τσάπλιν.",
      "Ο τελικός συγκινητικός λόγος του κουρέα υπέρ της ειρήνης και της ελευθερίας παραμένει μία από τις πιο εμπνευσμένες στιγμές της έβδομης τέχνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9C%CE%B5%CE%B3%CE%AC%CE%BB%CE%BF%CF%82_%CE%94%CE%B9%CE%BA%CF%84%CE%AC%CF%84%CF%89%CF%81",
    "locale": "el-GR",
    "tags": ["chaplin", "the-great-dictator", "classics", "satire"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_052",
    "text": "Στη σειρά εποχής «Το 10» (Alpha, 2007) σε σκηνοθεσία Πηγής Δημητρακοπούλου, ποιου μεγάλου συγγραφέα το έργο διασκευάστηκε;",
    "answers": ["Στρατή Μυριβήλη", "Μ. Καραγάτση", "Ηλία Βενέζη", "Άγγελου Τερζάκη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η σειρά βασίστηκε στο ημιτελές μυθιστόρημα του Μ. Καραγάτση 'Το 10', που καταγράφει τη ζωή των ενοίκων μιας πολυκατοικίας στον Πειραιά.",
    "funFacts": [
      "Η σειρά απέσπασε διθυραμβικές κριτικές και κέρδισε πολυάριθμα βραβεία στα τηλεοπτικά 'Πρόσωπα 2008'.",
      "Την εξαιρετική πρωτότυπη μουσική επένδυση της σειράς συνέθεσε η Ελένη Καραΐνδρου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_10_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-deka", "karagatsis", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_053",
    "text": "Στην ταινία «Reservoir Dogs» (1992) του Κουέντιν Ταραντίνο, ποιο χρώμα-ψευδώνυμο αποδόθηκε στον χαρακτήρα του Στιβ Μπουσέμι;",
    "answers": ["Κύριος Λευκός", "Κύριος Πορτοκαλί", "Κύριος Ροζ (Mr. Pink)", "Κύριος Ξανθός"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Steve Buscemi υποδύθηκε τον Mr. Pink, ο οποίος διαμαρτυρόταν έντονα στον αρχηγό Joe Cabot γιατί δεν ήθελε να έχει αυτό το κωδικό όνομα.",
    "funFacts": [
      "Ο χαρακτήρας του Mr. Pink είναι διάσημος για τον εναρκτήριο μονόλογό του στο εστιατόριο όπου αρνείται να αφήσει φιλοδώρημα στις σερβιτόρες.",
      "Η ταινία γυρίστηκε με εξαιρετικά χαμηλό προϋπολογισμό 1,2 εκατομμυρίων δολαρίων και εκτόξευσε την καριέρα του Ταραντίνο."
    ],
    "source": "https://el.wikipedia.org/wiki/Reservoir_Dogs",
    "locale": "el-GR",
    "tags": ["reservoir-dogs", "tarantino", "steve-buscemi", "cult-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_054",
    "text": "Ποιος σπουδαίος Έλληνας σκηνοθέτης έκανε το ντεμπούτο του μεγάλου μήκους με την ταινία «Το προξενιό της Άννας» (1972);",
    "answers": ["Θόδωρος Αγγελόπουλος", "Κώστας Φέρρης", "Αλέξης Δαμιανός", "Παντελής Βούλγαρης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Παντελής Βούλγαρης σκηνοθέτησε 'Το προξενιό της Άννας' σε παραγωγή Ντίνου Κατσουρίδη, κερδίζοντας το Βραβείο Καλύτερης Ταινίας στο Φεστιβάλ Θεσσαλονίκης.",
    "funFacts": [
      "Η πρωταγωνίστρια Άννα Βαγενά απέσπασε το Βραβείο Α' Γυναικείου Ρόλου για την καθηλωτική της ερμηνεία ως υπηρέτρια.",
      "Η ταινία βραβεύτηκε επίσης στο Φεστιβάλ του Βερολίνου το 1973."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%80%CF%81%CE%BF%CE%BE%CE%B5%CE%BD%CE%B9%CF%8C_%CF%84%CE%B7%CF%82_%CE%86%CE%BD%CE%BD%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["voulgaris", "greek-cinema", "classics", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_055",
    "text": "Ποιο είναι το όνομα του αυτόνομου υπολογιστή τεχνητής νοημοσύνης στο «2001: Η Οδύσσεια του Διαστήματος» (1968);",
    "answers": ["HAL 9000", "Skynet", "GORT", "Mother"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο HAL 9000 είναι ο υπερυπολογιστής με το κόκκινο μάτι που ελέγχει το σκάφος Discovery One και σταδιακά στρέφεται κατά του ανθρώπινου πληρώματος.",
    "funFacts": [
      "Τα γράμματα H-A-L είναι κατά μία θέση προγενέστερα στο λατινικό αλφάβητο από τα γράμματα I-B-M, αν και ο συγγραφέας Arthur C. Clarke ισχυρίστηκε ότι ήταν σύμπτωση.",
      "Η σκηνή όπου ο αστροναύτης Dave Bowman αποσυνδέει σταδιακά τα κυκλώματα του HAL καθώς εκείνος τραγουδά το 'Daisy Bell' είναι κλασική."
    ],
    "source": "https://el.wikipedia.org/wiki/2001:_%CE%97_%CE%9F%CE%B4%CF%8D%CF%83%CF%83%CE%B5%CE%B9%CE%B1_%CF%84%CE%BF%CF%85_%CE%94%CE%B9%CE%B1%CF%83%CF%84%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["kubrick", "hal-9000", "sci-fi", "space-odyssey"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_056",
    "text": "Ποιος πρωτοπόρος σκηνοθέτης υπέγραψε την καλτ ταινία «Γλυκιά συμμορία» (1983) του σύγχρονου ελληνικού κινηματογράφου;",
    "answers": ["Κώστας Φέρρης", "Νίκος Νικολαΐδης", "Σταύρος Τορνές", "Γιώργος Πανουσόπουλος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Νίκος Νικολαΐδης έγραψε και σκηνοθέτησε τη 'Γλυκιά συμμορία', το δεύτερο μέρος της άτυπης τριλογίας του για τα 'χρόνια της χολέρας'.",
    "funFacts": [
      "Η ταινία απέσπασε 8 κρατικά βραβεία ποιότητας στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης το 1983.",
      "Αποτέλεσε σημείο αναφοράς για τη νεανική underground κουλτούρα της δεκαετίας του 1980 στην Ελλάδα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BB%CF%85%CE%BA%CE%B9%CE%AC_%CF%83%CF%85%CE%BC%CE%BC%CE%BF%CF%81%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["nikolaidis", "glykia-symmoria", "greek-cinema", "cult"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_057",
    "text": "Ποιος Βρετανός ηθοποιός ενσάρκωσε τον επιστήμονα Βαλέρι Λεγκάσοφ στη δραματική μίνι σειρά του HBO «Chernobyl» (2019);",
    "answers": ["Στέλαν Σκάρσγκαρντ", "Πολ Ρίτερ", "Τζάρεντ Χάρις", "Μαρκ Λιούις Τζόουνς"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Jared Harris πρωταγωνίστησε ως ο Σοβιετικός χημικός Valery Legasov που ηγήθηκε της επιστημονικής επιτροπής αντιμετώπισης του πυρηνικού δυστυχήματος.",
    "funFacts": [
      "Η σειρά απέσπασε 10 βραβεία Primetime Emmy και γνώρισε εξαιρετική κριτική αποδοχή παγκοσμίως.",
      "Η εισαγωγική ατάκα του Λεγκάσοφ 'What is the cost of lies?' ('Ποιο είναι το κόστος των ψεμάτων;') συνοψίζει το φιλοσοφικό νόημα της σειράς."
    ],
    "source": "https://el.wikipedia.org/wiki/Chernobyl_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["chernobyl", "jared-harris", "hbo", "drama"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_058",
    "text": "Στη θρυλική σειρά της ΕΡΤ «Ο Χριστός Ξανασταυρώνεται» (1975), ποιου σπουδαίου Κρητικού συγγραφέα το έργο μεταφέρθηκε στη μικρή οθόνη;",
    "answers": ["Παντελή Πρεβελάκη", "Μενέλαου Λουντέμη", "Κώστα Βάρναλη", "Νίκου Καζαντζάκη"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η σειρά σε σκηνοθεσία Βασίλη Γεωργιάδη βασίστηκε στο ομώνυμο αριστούργημα του Νίκου Καζαντζάκη και καθήλωσε το πανελλήνιο.",
    "funFacts": [
      "Τον ρόλο του Μανωλιού υποδύθηκε ο Αλέξης Γκόλφης, η ζωή του οποίου είχε αργότερα τραγική κατάληξη.",
      "Υπήρξε μία από τις μεγαλύτερες τηλεοπτικές επιτυχίες της δεκαετίας του 1970 με απήχηση σε όλη την Ελλάδα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%A7%CF%81%CE%B9%CF%83%CF%84%CF%8C%CF%82_%CE%BE%CE%B1%CE%BD%CE%B1%CF%83%CF%84%CE%B1%CF%85%CF%81%CF%8E%CE%BD%CE%B5%CF%84%CE%B1%CE%B9_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["kazantzakis", "greek-tv", "ert", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_059",
    "text": "Στην ταινία «Η Αιώνια Λιακάδα ενός Καθαρού Μυαλού» (2004), ποια ιατρική υπηρεσία παρέχει η μυστηριώδης εταιρεία Lacuna Inc.;",
    "answers": ["Διαγραφή ανεπιθύμητων αναμνήσεων", "Εμφύτευση ψεύτικων ονείρων", "Πρόβλεψη μελλοντικών σχέσεων", "Αναστροφή βιολογικής ηλικίας"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Η Lacuna Inc. προσφέρει μια τεχνική διαγραφής συγκεκριμένων προσώπων από τη μνήμη, την οποία επιλέγουν ο Τζόελ (Τζιμ Κάρεϊ) και η Κλημεντίνη (Κέιτ Γουίνσλετ).",
    "funFacts": [
      "Ο σεναριογράφος Τσάρλι Κάουφμαν και ο σκηνοθέτης Μισέλ Γκοντρί κέρδισαν το Όσκαρ Πρωτότυπου Σεναρίου το 2005.",
      "Ο τίτλος της ταινίας προέρχεται από στίχο του ποιήματος του Αλεξάντερ Πόουπ 'Eloisa to Abelard'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%91%CE%B9%CF%8E%CE%BD%CE%B9%CE%B1_%CE%9B%CE%B9%CE%B1%CE%BA%CE%AC%CE%B4%CE%B1_%CE%B5%CE%BD%CF%8C%CF%82_%CE%9A%CE%B1%CE%B8%CE%B1%CF%81%CE%BF%CF%8D_%CE%9C%CF%85%CE%B1%CE%BB%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["eternal-sunshine", "jim-carrey", "kaufman", "romance-sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_med_060",
    "text": "Στην κλασική ταινία «Αλίμονο στους νέους» (1961), ποιος ηθοποιός υποδύεται τον ηλικιωμένο Ανδρέα που κάνει συμφωνία με τον Διάβολο;",
    "answers": ["Αλέκος Αλεξανδράκης", "Δημήτρης Χορν", "Λάμπρος Κωνσταντάρας", "Βασίλης Αυλωνίτης"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 3,
    "explanation": "Ο Δημήτρης Χορν υποδύεται έναν πλούσιο ηλικιωμένο που δέχεται να γίνει φτωχός νέος με αντάλλαγμα τα νιάτα του, σε μια παραλλαγή του μύθου του Φάουστ.",
    "funFacts": [
      "Στην ταινία ο Χορν ερμηνεύει το πασίγνωστο τραγούδι του Μάνου Χατζιδάκι 'Πες μου μια λέξη' μαζί με τη Μάρω Κοντού.",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο και αποτελεί μία από τις πιο κομψές ταινίες του ελληνικού κινηματογράφου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AF%CE%BC%CE%BF%CE%BD%CE%BF_%CF%83%CF%84%CE%BF%CF%85%CF%82_%CE%BD%CE%AD%CE%BF%CF%85%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dimitris-horn", "maro-kontou", "hadjidakis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'medium', 3, questions)

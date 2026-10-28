# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_easy_011",
    "text": "Ποια είναι η δίδυμη αδελφή του Λουκ Σκαϊγουόκερ στον κόσμο του «Star Wars»;",
    "answers": ["Πριγκίπισσα Λέια", "Πάντμε Αμιντάλα", "Ρέι", "Ασόκα Τάνο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Πριγκίπισσα Λέια Οργκάνα (Princess Leia) αποκαλύπτεται στο 'Η Επιστροφή των Τζεντάι' ότι είναι η δίδυμη αδελφή του Λουκ Σκαϊγουόκερ.",
    "funFacts": [
      "Τον ρόλο της Λέια ενσάρκωσε η αξέχαστη ηθοποιός Κάρι Φίσερ (Carrie Fisher).",
      "Το διάσημο χτένισμά της με τους δύο στρογγυλούς κότσους στα πλαϊνά του κεφαλιού έγινε παγκόσμιο σύμβολο της ποπ κουλτούρας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CE%B9%CE%B3%CE%BA%CE%AF%CF%80%CE%B9%CF%83%CF%83%CE%B1_%CE%9B%CE%AD%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["star-wars", "sci-fi", "cinema", "characters"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_012",
    "text": "Ποιο εμβληματικό όχημα μετατράπηκε σε χρονομηχανή στην τριλογία ταινιών «Επιστροφή στο Μέλλον»;",
    "answers": ["Ford Mustang", "DeLorean DMC-12", "Chevrolet Corvette", "Volkswagen Beetle"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο εκκεντρικός επιστήμονας Ντοκ Μπράουν κατασκεύασε τη μηχανή του χρόνου χρησιμοποιώντας ένα τροποποιημένο σπορ αυτοκίνητο DeLorean DMC-12.",
    "funFacts": [
      "Το αυτοκίνητο έπρεπε να αναπτύξει ταχύτητα 88 μιλίων την ώρα (περίπου 142 χλμ/ώρα) για να ενεργοποιηθεί το ταξίδι στον χρόνο.",
      "Στο αρχικό προσχέδιο του σεναρίου, η χρονομηχανή ήταν σχεδιασμένη ως ένα παλιό ψυγείο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%83%CF%84%CF%81%CE%BF%CF%86%CE%AE_%CF%83%CF%84%CE%BF_%CE%9C%CE%AD%CE%BB%CE%BB%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["back-to-the-future", "sci-fi", "80s", "vehicles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_013",
    "text": "Ποια προϊστορικά πλάσματα κλωνοποιήθηκαν και δημιούργησαν το ομώνυμο θεματικό πάρκο στο «Jurassic Park» (1993);",
    "answers": ["Μαμούθ", "Μυθικά τέρατα", "Δεινόσαυροι", "Εξωγήινα όντα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Στο 'Jurassic Park' του Στίβεν Σπίλμπεργκ, επιστήμονες κλωνοποιούν δεινοσαύρους από DNA διατηρημένο σε κεχριμπάρι για ένα τουριστικό πάρκο.",
    "funFacts": [
      "Η ταινία βασίστηκε στο ομότιτλο μυθιστόρημα επιστημονικής φαντασίας του Μάικλ Κράιτον.",
      "Κέρδισε τρία βραβεία Όσκαρ για τα πρωτοποριακά οπτικά εφέ και τον ήχο της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%85%CF%81%CE%AC%CF%83%CE%B9%CE%BA_%CE%A0%CE%B1%CF%81%CE%BA_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["jurassic-park", "spielberg", "dinosaurs", "blockbuster"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_014",
    "text": "Σε ποιον κοιτώνα (οίκο) της σχολής Χόγκουαρτς ανήκουν ο Χάρι Πότερ, ο Ρον και η Ερμιόνη;",
    "answers": ["Σλίθεριν", "Ρέιβενκλο", "Χάφλπαφ", "Γκρίφιντορ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο κοιτώνας Γκρίφιντορ (Gryffindor) έχει σύμβολο το λιοντάρι, χρώματα το κόκκινο και το χρυσό, και τιμά τη γενναιότητα και το θάρρος.",
    "funFacts": [
      "Το Καπέλο της Επιλογής σκεφτόταν αρχικά να στείλει τον Χάρι στον οίκο Σλίθεριν, αλλά σεβάστηκε την επιθυμία του ίδιου του Χάρι.",
      "Ιδρυτής του κοιτώνα ήταν ο Γκόντρικ Γκρίφιντορ, από τον οποίο πήρε το όνομά του και το θρυλικό σπαθί του οίκου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CE%B9_%CE%A0%CF%8C%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["harry-potter", "fantasy", "hogwarts", "gryffindor"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_015",
    "text": "Σε ποια πόλη των Ηνωμένων Πολιτειών διαδραματίζεται η πολυαγαπημένη κωμική σειρά «Τα Φιλαράκια» (Friends);",
    "answers": ["Νέα Υόρκη", "Λος Άντζελες", "Σικάγο", "Βοστώνη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά 'Friends' ακολουθεί τη ζωή μιας παρέας έξι φίλων που ζουν και συχνάζουν στο Μανχάταν της Νέας Υόρκης.",
    "funFacts": [
      "Παρότι η πλοκή εκτυλίσσεται στη Νέα Υόρκη, σχεδόν όλα τα γυρίσματα πραγματοποιήθηκαν σε στούντιο της Warner Bros. στην Καλιφόρνια.",
      "Η αγαπημένη καφετέρια της παρέας όπου περνούσαν τις ώρες τους ονομαζόταν 'Central Perk'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%A6%CE%B9%CE%BB%CE%B1%CF%81%CE%AC%CE%BA%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["friends", "sitcom", "tv-series", "new-york"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_016",
    "text": "Ποια θρυλική Ελληνίδα ηθοποιός χαρακτηρίστηκε και έμεινε στην ιστορία ως η «εθνική σταρ» της Ελλάδας;",
    "answers": ["Τζένη Καρέζη", "Αλίκη Βουγιουκλάκη", "Μαίρη Χρονοπούλου", "Ζωή Λάσκαρη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Αλίκη Βουγιουκλάκη υπήρξε η δημοφιλέστερη πρωταγωνίστρια του ελληνικού θεάτρου και κινηματογράφου με τεράστια εμπορική επιτυχία.",
    "funFacts": [
      "Η ταινία της 'Υπολοχαγός Νατάσσα' (1970) κατείχε για δεκαετίες το απόλυτο ρεκόρ εισιτηρίων στον ελληνικό κινηματογράφο.",
      "Συμπρωταγωνίστησε σε πολλές ταινίες-σταθμούς με τον σύζυγό της Δημήτρη Παπαμιχαήλ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AF%CE%BA%CE%B7_%CE%92%CE%BF%CF%85%CE%B3%CE%B9%CE%BF%CF%85%CE%BA%CE%BB%CE%AC%CE%BA%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-cinema", "aliki-vougiouklaki", "classic-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_017",
    "text": "Ποιος διάσημος Αμερικανός σκηνοθέτης υπέγραψε την καλτ ταινία «Pulp Fiction» το 1994;",
    "answers": ["Ντέιβιντ Φίντσερ", "Μάρτιν Σκορσέζε", "Κουέντιν Ταραντίνο", "Γούντι Άλεν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Quentin Tarantino έγραψε και σκηνοθέτησε το 'Pulp Fiction', κερδίζοντας τον Χρυσό Φοίνικα στις Κάννες και το Όσκαρ Πρωτότυπου Σεναρίου.",
    "funFacts": [
      "Η ταινία αναζωογόνησε θεαματικά την καριέρα του Τζον Τραβόλτα, ο οποίος ήταν υποψήφιος για Όσκαρ Α' Ανδρικού Ρόλου.",
      "Ο διάσημος χορός του Τραβόλτα με την Ούμα Θέρμαν στο Jack Rabbit Slim's αποτελεί αναφορά στον ευρωπαϊκό κινηματογράφο."
    ],
    "source": "https://el.wikipedia.org/wiki/Pulp_Fiction",
    "locale": "el-GR",
    "tags": ["pulp-fiction", "tarantino", "90s", "cult-cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_018",
    "text": "Στην ταινία κινουμένων σχεδίων «Toy Story» (1995), τι είδους παιχνίδι είναι ο Μπαζ Λαϊτγίαρ (Buzz Lightyear);",
    "answers": ["Καουμπόι", "Δεινόσαυρος", "Στρατιωτάκι", "Αστροναύτης"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Buzz Lightyear είναι ένας υπερσύγχρονος αστροναύτης/διαστημικός φρουρός (Space Ranger) που αρχικά πιστεύει πως είναι αληθινός.",
    "funFacts": [
      "Το 'Toy Story' της Pixar ήταν η πρώτη ταινία μεγάλου μήκους στην ιστορία που δημιουργήθηκε εξ ολοκλήρου σε υπολογιστή (CGI).",
      "Η διάσημη φράση του Μπαζ είναι 'Στο άπειρο κι ακόμα παραπέρα!' ('To infinity and beyond!')."
    ],
    "source": "https://el.wikipedia.org/wiki/Toy_Story",
    "locale": "el-GR",
    "tags": ["pixar", "toy-story", "animation", "buzz-lightyear"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_019",
    "text": "Ποιος κορυφαίος ηθοποιός ενσάρκωσε τον ριψοκίνδυνο αρχαιολόγο Ιντιάνα Τζόουνς στη μεγάλη οθόνη;",
    "answers": ["Χάρισον Φορντ", "Μάικλ Ντάγκλας", "Σιλβέστερ Σταλόνε", "Κλιντ Ίστγουντ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Harrison Ford πρωταγωνίστησε ως Dr. Henry 'Indiana' Jones σε πέντε ταινίες της σειράς ξεκινώντας από το 1981.",
    "funFacts": [
      "Ο Τομ Σέλεκ ήταν η αρχική επιλογή για τον ρόλο, αλλά δεν μπόρεσε να δεχτεί λόγω του τηλεοπτικού του συμβολαίου για το 'Magnum, P.I.'.",
      "Το χαρακτηριστικό του καπέλο (fedora) και το δερμάτινο μαστίγιο έγιναν άμεσα αναγνωρίσιμα σύμβολα της έβδομης τέχνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%BD%CF%84%CE%B9%CE%AC%CE%BD%CE%B1_%CE%A4%CE%B6%CF%8C%CE%BF%CF%85%CE%BD%CF%82",
    "locale": "el-GR",
    "tags": ["indiana-jones", "harrison-ford", "adventure", "hollywood"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_020",
    "text": "Ποια πριγκίπισσα της Disney έχει μαγικές δυνάμεις πάγου και τραγουδά το παγκόσμιο χιτ «Let It Go» στο «Frozen»;",
    "answers": ["Άννα", "Έλσα", "Ραπουνζέλ", "Μοάνα"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η βασίλισσα Έλσα (Elsa) γεννήθηκε με τη μαγική ικανότητα να δημιουργεί και να ελέγχει τον πάγο και το χιόνι.",
    "funFacts": [
      "Η ταινία 'Ψυχρά κι Ανάποδα' (Frozen, 2013) κέρδισε δύο βραβεία Όσκαρ: Καλύτερης Ταινίας Κινουμένων Σχεδίων και Καλύτερου Τραγουδιού.",
      "Η πλοκή της ταινίας είναι ελεύθερα εμπνευσμένη από το παραμύθι 'Η Βασίλισσα του Χιονιού' του Χανς Κρίστιαν Άντερσεν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A8%CF%85%CF%87%CF%81%CE%AC_%CE%BA%CE%B9_%CE%91%CE%BD%CE%AC%CF%80%CE%BF%CE%B4%CE%B1",
    "locale": "el-GR",
    "tags": ["disney", "frozen", "animation", "elsa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_021",
    "text": "Ποιο είναι το πραγματικό όνομα και η μυστική ταυτότητα του Spider-Man;",
    "answers": ["Μπρους Γουέιν", "Κλαρκ Κεντ", "Πίτερ Πάρκερ", "Μπρους Μπάνερ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Peter Parker είναι ο νεαρός μαθητής και φωτογράφος που αποκτά υπερδυνάμεις μετά από τσίμπημα ραδιενεργού αράχνης.",
    "funFacts": [
      "Η αρχή που καθορίζει τη ζωή του ήρωα είναι: 'Με τη μεγάλη δύναμη έρχεται και μεγάλη ευθύνη'.",
      "Στον κινηματογράφο τον έχουν υποδυθεί τρεις διαφορετικοί ηθοποιοί: ο Τόμπι Μαγκουάιρ, ο Άντριου Γκάρφιλντ και ο Τομ Χόλαντ."
    ],
    "source": "https://el.wikipedia.org/wiki/Spider-Man",
    "locale": "el-GR",
    "tags": ["spider-man", "marvel", "superheroes", "comics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_022",
    "text": "Στην ελληνική κωμική σειρά «Κωνσταντίνου και Ελένης», ποιο ήταν το επάγγελμα του Κωνσταντίνου Κατακουζηνού;",
    "answers": ["Δικηγόρος", "Γιατρός", "Αρχιτέκτονας", "Καθηγητής Βυζαντινολογίας"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Κωνσταντίνος Κατακουζηνός (Χάρης Ρώμας) ήταν επίκουρος καθηγητής Βυζαντινολογίας που έγραφε το σύγγραμμα 'Το Αποχετευτικό Σύστημα στο Βυζάντιο'.",
    "funFacts": [
      "Η σειρά προβλήθηκε στον ΑΝΤ1 τις σεζόν 1998–2000 και προβάλλεται σε αδιάκοπες καθημερινές επαναλήψεις για πάνω από δύο δεκαετίες.",
      "Το σενάριο συνυπέγραψαν ο Χάρης Ρώμας και η Άννα Χατζησοφιά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%BD%CF%83%CF%84%CE%B1%CE%BD%CF%84%CE%AF%CE%BD%CE%BF%CF%85_%CE%BA%CE%B1%CE%B9_%CE%95%CE%BB%CE%AD%CE%BD%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "comedy", "ant1", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_023",
    "text": "Ποιος ηθοποιός κέρδισε μεταθανάτιο Όσκαρ για την ανεπανάληπτη ερμηνεία του ως Τζόκερ στην ταινία «Ο Σκοτεινός Ιππότης» (2008);",
    "answers": ["Χιθ Λέτζερ", "Χοακίν Φίνιξ", "Τζακ Νίκολσον", "Τζάρεντ Λέτο"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Heath Ledger βραβεύτηκε με το Όσκαρ Β' Ανδρικού Ρόλου για την ερμηνεία του ως Joker στο 'The Dark Knight' του Κρίστοφερ Νόλαν.",
    "funFacts": [
      "Απεβίωσε τραγικά σε ηλικία μόλις 28 ετών λίγους μήνες πριν από την πρεμιέρα της ταινίας.",
      "Ήταν μόλις ο δεύτερος ηθοποιός στην ιστορία του κινηματογράφου που έλαβε Όσκαρ μετά θάνατον, μετά τον Πίτερ Φιντς το 1977."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B9%CE%B8_%CE%9B%CE%AD%CF%84%CE%B6%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["batman", "joker", "heath-ledger", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_024",
    "text": "Τι είδους πλάσμα είναι ο πράσινος και καλόκαρδος ήρωας «Σρεκ» (Shrek) στην ομώνυμη ταινία κινουμένων σχεδίων;",
    "answers": ["Ξωτικό", "Ογκρ (γίγαντας)", "Κένταυρος", "Καλικάντζαρος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Shrek είναι ένας πράσινος ογκρ (ogre) που ζει απομονωμένος σε έναν βάλτο πριν αναγκαστεί να σώσει την πριγκίπισσα Φιόνα.",
    "funFacts": [
      "Η ταινία 'Shrek' της DreamWorks (2001) κέρδισε το πρώτο στην ιστορία Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων.",
      "Τη φωνή του Σρεκ στην αγγλική εκδοχή χάρισε ο διάσημος κωμικός Μάικ Μάγιερς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%81%CE%B5%CE%BA",
    "locale": "el-GR",
    "tags": ["shrek", "dreamworks", "animation", "ogre"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_025",
    "text": "Ποιο είναι το όνομα του κοριτσιού με τις τηλεκινητικές ικανότητες στη δημοφιλή σειρά «Stranger Things»;",
    "answers": ["Μαξ", "Νάνσι", "Έντεκα (Eleven)", "Ρόμπιν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Eleven (την οποία υποδύεται η Μίλι Μπόμπι Μπράουν) διαθέτει ισχυρές τηλεκινητικές και τηλεπαθητικές δυνάμεις.",
    "funFacts": [
      "Ένα από τα αγαπημένα της φαγητά στη σειρά είναι οι κατεψυγμένες βάφλες Eggo.",
      "Η σειρά αποτελεί φόρο τιμής στην ποπ κουλτούρα και τον κινηματογράφο επιστημονικής φαντασίας της δεκαετίας του 1980."
    ],
    "source": "https://el.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger-things", "netflix", "sci-fi", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_026",
    "text": "Ποιος αγαπημένος κωμικός του ελληνικού σινεμά έμεινε στην ιστορία για το ασταμάτητο τρέξιμό του και την ατάκα «Καλέ μου άνθρωπε»;",
    "answers": ["Κώστας Βουτσάς", "Νίκος Σταυρίδης", "Λάμπρος Κωνσταντάρας", "Θανάσης Βέγγος"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Θανάσης Βέγγος υπήρξε ένας από τους σπουδαιότερους και πιο αγαπητούς Έλληνες ηθοποιούς, γνωστός ως 'ο άνθρωπος που έτρεχε πάντα'.",
    "funFacts": [
      "Το 1971 απέσπασε το Βραβείο Α' Ανδρικού Ρόλου στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης για την ταινία 'Τι έκανες στον πόλεμο, Θανάση;'.",
      "Ίδρυσε τη δική του εταιρεία παραγωγής, τη 'ΘΒ Ταινίες Γέλιου', γυρίζοντας ιστορικές κωμωδίες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B1%CE%BD%CE%AC%CF%83%CE%B7%CF%82_%CE%92%CE%AD%CE%B3%CE%B3%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "thanasis-veggos", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_027",
    "text": "Ποιος θρυλικός ηθοποιός υποδύθηκε τον Ρικ Μπλέιν στην κλασική ρομαντική ταινία «Καζαμπλάνκα» (1942);",
    "answers": ["Χάμφρεϊ Μπόγκαρτ", "Κλαρκ Γκέιμπλ", "Κάρι Γκραντ", "Τζέιμς Στιούαρτ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Humphrey Bogart πρωταγωνίστησε ως ο κυνικός αλλά ευγενής ιδιοκτήτης του Rick's Café Américain απέναντι στην Ίνγκριντ Μπέργκμαν.",
    "funFacts": [
      "Η ταινία κέρδισε τρία βραβεία Όσκαρ, ανάμεσά τους και το Όσκαρ Καλύτερης Ταινίας.",
      "Η διάσημη ατάκα 'Play it again, Sam' δεν ειπώθηκε ποτέ επακριβώς έτσι στην ταινία, αποτελώντας ένα από τα πιο γνωστά misquotes."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%B6%CE%B1%CE%BC%CF%80%CE%BB%CE%AC%CE%BD%CE%BA%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["casablanca", "humphrey-bogart", "classics", "romance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_028",
    "text": "Από ποια χώρα προέρχεται η δραματική σειρά-φαινόμενο «Το Παιχνίδι του Καλαμαριού» (Squid Game);",
    "answers": ["Ιαπωνία", "Νότια Κορέα", "Κίνα", "Ταϊλάνδη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το 'Squid Game' δημιουργήθηκε στη Νότια Κορέα από τον Hwang Dong-hyuk και έγινε η πιο επιτυχημένη σε τηλεθέαση σειρά στην ιστορία του Netflix.",
    "funFacts": [
      "Έγινε η πρώτη μη αγγλόφωνη σειρά που κέρδισε κορυφαία αμερικανικά βραβεία Primetime Emmy, συμπεριλαμβανομένου Α' Ανδρικού Ρόλου.",
      "Τα παιχνίδια θανάτου της σειράς βασίζονται σε πραγματικά παραδοσιακά παιδικά παιχνίδια της Κορέας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%A0%CE%B1%CE%B9%CF%87%CE%BD%CE%AF%CE%B4%CE%B9_%CF%84%CE%BF%CF%85_%CE%9A%CE%B1%CE%BB%CE%B1%CE%BC%CE%B1%CF%81%CE%B9%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["squid-game", "south-korea", "netflix", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_029",
    "text": "Τι είδος ψαριού είναι ο Νέμο στη διάσημη ταινία κινουμένων σχεδίων «Ψάχνοντας τον Νέμο» (2003);",
    "answers": ["Χρυσόψαρο", "Ξιφίας", "Ψάρι κλόουν", "Μπλε τανγκ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Νέμο και ο πατέρας του Μάρλιν ανήκουν στο είδος των ψαριών κλόουν (clownfish / αμφιπρίων) που ζουν προστατευμένα ανάμεσα σε θαλάσσιες ανεμώνες.",
    "funFacts": [
      "Η ταινία της Pixar κέρδισε το Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2004.",
      "Η φίλη τους η Ντόρι, που έχει απώλεια πρόσφατης μνήμης, είναι ψάρι του είδους μπλε τανγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A8%CE%AC%CF%87%CE%BD%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CE%BF%CE%BD_%CE%9D%CE%AD%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["pixar", "finding-nemo", "animation", "disney"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_030",
    "text": "Ποιον ανατριχιαστικό κανίβαλο ψυχίατρο υποδύθηκε ο Άντονι Χόπκινς στην ταινία «Η Σιωπή των Αμνών» (1991);",
    "answers": ["Νόρμαν Μπέιτς", "Φρέντι Κρούγκερ", "Τζέισον Βόρχις", "Χάνιμπαλ Λέκτερ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Dr. Hannibal Lecter είναι ο ευφυής και επικίνδυνος ψυχίατρος που βοηθά την πράκτορα Clarice Starling να συλλάβει έναν άλλο κατά συρροή δολοφόνο.",
    "funFacts": [
      "Ο Χόπκινς κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου εμφανιζόμενος στην οθόνη για μόλις περίπου 16 λεπτά συνολικού χρόνου.",
      "Η ταινία κέρδισε και τα 5 βασικά βραβεία Όσκαρ (Ταινίας, Σκηνοθεσίας, Α' Ανδρικού, Α' Γυναικείου, Σεναρίου)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A3%CE%B9%CF%89%CF%80%CE%AE_%CF%84%CF%89%CE%BD_%CE%91%CE%BC%CE%BD%CF%8E%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["anthony-hopkins", "hannibal-lecter", "thriller", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_031",
    "text": "Σε ποια κλασική ελληνική κωμωδία ο Λάμπρος Κωνσταντάρας υποδύεται τον υπουργό Ανδρέα Μαυρογιαλούρο;",
    "answers": ["Υπάρχει και φιλότιμο", "Ο στρίγγλος που έγινε αρνάκι", "Ο φαντασμένος", "Η βίλα των οργίων"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Στο 'Υπάρχει και φιλότιμο' (1965) του Αλέκου Σακελλάριου, ο υπουργός ανακαλύπτει τις απάτες των συνεργατών του μετά από τροχαίο ατύχημα σε χωριό.",
    "funFacts": [
      "Ο όρος 'Μαυρογιαλούρος' καθιερώθηκε στην ελληνική πολιτική γλώσσα ως συνώνυμο του ανειλικρινούς πολιτικού που μοιράζει ψεύτικες υποσχέσεις.",
      "Η ταινία βασίστηκε στο θεατρικό έργο 'Ανώμαλη προσγείωση' των Σακελλάριου και Γιαννακόπουλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%AC%CF%81%CF%87%CE%B5%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "konstantaras", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_032",
    "text": "Ποιο θαλάσσιο πλάσμα σκορπά τον τρόμο στους λουόμενους στην ταινία «Τα Σαγόνια του Καρχαρία» (Jaws);",
    "answers": ["Γιγάντιο καλαμάρι", "Μεγάλος λευκός καρχαρίας", "Φονική όρκα", "Θαλάσσιος ίππος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η ταινία του Στίβεν Σπίλμπεργκ (1975) εστιάζει στις επιθέσεις ενός τεράστιου λευκού καρχαρία στις ακτές του τουριστικού νησιού Άμιτι.",
    "funFacts": [
      "Θεωρείται το πρώτο πραγματικό καλοκαιρινό blockbuster στην ιστορία του παγκόσμιου κινηματογράφου.",
      "Το διάσημο απειλητικό μουσικό θέμα δύο νοτών συνέθεσε ο κορυφαίος συνθέτης Τζον Γουίλιαμς, κερδίζοντας Όσκαρ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%A3%CE%B1%CE%B3%CF%8C%CE%BD%CE%B9%CE%B1_%CF%84%CE%BF%CF%85_%CE%9A%CE%B1%CF%81%CF%87%CE%B1%CF%81%CE%AF%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["jaws", "spielberg", "blockbuster", "sharks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_033",
    "text": "Σε ποια βρετανική πόλη δραστηριοποιείται η συμμορία της οικογένειας Σέλμπι στη σειρά «Peaky Blinders»;",
    "answers": ["Λονδίνο", "Λίβερπουλ", "Μπέρμιγχαμ", "Μάντσεστερ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά ακολουθεί την εγκληματική οργάνωση Peaky Blinders με αρχηγό τον Τόμι Σέλμπι (Κίλιαν Μέρφι) στο Μπέρμιγχαμ μετά τον Α' Παγκόσμιο Πόλεμο.",
    "funFacts": [
      "Το όνομα της συμμορίας προήλθε από τις λεπίδες ξυραφιού που υποτίθεται ότι έραβαν στα γείσα των τραγιάσκων τους.",
      "Η σειρά προβλήθηκε από το BBC από το 2013 έως το 2022 γνωρίζοντας παγκόσμια απήχηση."
    ],
    "source": "https://el.wikipedia.org/wiki/Peaky_Blinders",
    "locale": "el-GR",
    "tags": ["peaky-blinders", "bbc", "crime", "birmingham"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_034",
    "text": "Ποιος μυώδης σταρ του Χόλιγουντ είπε την ιστορική ατάκα «I'll be back» στην ταινία «Ο Εξολοθρευτής» (1984);",
    "answers": ["Σιλβέστερ Σταλόνε", "Μπρους Γουίλις", "Ζαν-Κλοντ Βαν Νταμ", "Άρνολντ Σβαρτσενέγκερ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Arnold Schwarzenegger υποδύθηκε το αδίστακτο ανδροειδές δολοφόνο T-800 στην ταινία επιστημονικής φαντασίας του Τζέιμς Κάμερον.",
    "funFacts": [
      "Η φράση 'I'll be back' ψηφίστηκε ως μία από τις πιο αναγνωρίσιμες ατάκες στην ιστορία του παγκόσμιου κινηματογράφου.",
      "Στην αρχική του εκδοχή ο Σβαρτσενέγκερ προοριζόταν για τον ρόλο του ανθρώπινου ήρωα Κάιλ Ρις."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%95%CE%BE%CE%BF%CE%BB%CE%BF%CE%B8%CF%81%CE%B5%CF%85%CF%84%CE%AE%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["terminator", "schwarzenegger", "sci-fi", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_035",
    "text": "Ποιος σπουδαίος ηθοποιός υποδύθηκε τον αυστηρό γυμνασιάρχη Παναγιώτη Φλωρά στην ταινία «Το ξύλο βγήκε από τον παράδεισο»;",
    "answers": ["Ορέστης Μακρής", "Διονύσης Παπαγιαννόπουλος", "Βασίλης Αυλωνίτης", "Παντελής Ζερβός"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Ορέστης Μακρής ενσάρκωσε τον αυστηρό γυμνασιάρχη Φλωρά που φώναζε στους μαθητές και καθηγητές τη θρυλική ατάκα 'Κουραμπιέδες!'.",
    "funFacts": [
      "Η ταινία προβλήθηκε τη σεζόν 1959–1960 και έκοψε πάνω από 239.000 εισιτήρια στις αίθουσες πρώτης προβολής.",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο, ο οποίος έγραψε και τους στίχους για τα τραγούδια του Μάνου Χατζιδάκι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BE%CF%8D%CE%BB%CE%BF_%CE%B2%CE%B3%CE%AE%CE%BA%CE%B5_%CE%B1%CF%80%CF%8C_%CF%84%CE%BF%CE%BD_%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "orestis-makris", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_036",
    "text": "Ποιο είναι το όνομα του σκανδαλιάρη γιου του Χόμερ και της Μαρτζ στη σειρά «The Simpsons»;",
    "answers": ["Μίλχαους", "Μπαρτ", "Ραλφ", "Νέλσον"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Bart Simpson είναι ο δεκάχρονος πρωτότοκος γιος της οικογένειας Simpsons, γνωστός για τις φάρσες και το σκέιτμπορντ του.",
    "funFacts": [
      "Το όνομά του 'Bart' είναι αναγραμματισμός της αγγλικής λέξης 'brat' (κακομαθημένο παιδί).",
      "Τη φωνή του Μπαρτ στην αμερικανική εκδοχή δανείζει από το ξεκίνημα της σειράς μια γυναίκα, η ηθοποιός Nancy Cartwright."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Simpsons",
    "locale": "el-GR",
    "tags": ["the-simpsons", "animation", "bart-simpson", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_037",
    "text": "Ποιος πρωταγωνιστής υποδύθηκε τον Ρωμαίο στρατηγό Μάξιμο στην οσκαρική ταινία «Ο Μονομάχος» (Gladiator, 2000);",
    "answers": ["Μελ Γκίμπσον", "Χοακίν Φίνιξ", "Ράσελ Κρόου", "Τζεράρντ Μπάτλερ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Russell Crowe υποδύθηκε τον στρατηγό Maximus Decimus Meridius, κερδίζοντας το Όσκαρ Α' Ανδρικού Ρόλου.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Ρίντλεϊ Σκοτ και απέσπασε συνολικά 5 βραβεία Όσκαρ, συμπεριλαμβανομένου Καλύτερης Ταινίας.",
      "Η περίφημη αρένα του Κολοσσαίου ανακατασκευάστηκε εν μέρει στη Μάλτα και συμπληρώθηκε με ψηφιακά εφέ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9C%CE%BF%CE%BD%CE%BF%CE%BC%CE%AC%CF%87%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["gladiator", "russell-crowe", "ridley-scott", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_038",
    "text": "Στην ταινία κινουμένων σχεδίων «Αλαντίν» (1992), ποιο μαγικό πλάσμα βγαίνει από το λυχνάρι για να εκπληρώσει τρεις ευχές;",
    "answers": ["Ένας δράκος", "Ένα ξωτικό", "Ένας μάγος", "Το Τζίνι"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Τζίνι (Genie) είναι το πανίσχυρο μπλε πλάσμα που ήταν παγιδευμένο στο μαγικό λυχνάρι για 10.000 χρόνια.",
    "funFacts": [
      "Στην αμερικανική εκδοχή, ο Ρόμπιν Ουίλιαμς έδωσε ρεσιτάλ αυτοσχεδιασμού χαρίζοντας τη φωνή του στον ρόλο.",
      "Στην ελληνική μεταγλώττιση, το Τζίνι ερμήνευσε απολαυστικά ο Ζανό Ντάνιας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B1%CE%BD%CF%84%CE%AF%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1992)",
    "locale": "el-GR",
    "tags": ["disney", "aladdin", "animation", "genie"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_039",
    "text": "Στην ελληνική σειρά «Είσαι το ταίρι μου», ποιες δύο γυναίκες ανταλλάσσουν ταυτότητες στην πτήση από την Αυστραλία;",
    "answers": ["Η Στέλλα και η Βίκυ", "Η Αννέτα και η Ράνια", "Η Τούλα και η Σούλα", "Η Λίτσα και η Μαίρη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Στέλλα (Βίκυ Σταυροπούλου) και η Βίκυ (Κατερίνα Λέχου) συμφωνούν να αλλάξουν ρόλους ώστε η καθεμία να δοκιμάσει τη ζωή που ονειρευόταν.",
    "funFacts": [
      "Η σειρά του Mega προβλήθηκε τη σεζόν 2001–2002 σε σενάριο του Λευτέρη Παπαπέτρου και γνώρισε σαρωτική τηλεθέαση.",
      "Ο ρόλος του Σωτήρη (Αλέξης Γεωργούλης) εκτόξευσε τη δημοφιλία του ηθοποιού σε πανελλήνιο επίπεδο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["greek-tv", "eisai-to-tairi-mou", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_040",
    "text": "Ποιο είναι το χαρακτηριστικό φωτεινό όπλο των ιπποτών Τζεντάι στο σύμπαν του «Star Wars»;",
    "answers": ["Ακτινοπίστολο", "Φωτόσπαθο", "Βαλλίστρα πλάσματος", "Ενεργειακό δόρυ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το φωτόσπαθο (lightsaber) είναι το παραδοσιακό όπλο των Jedi και των Sith, τροφοδοτούμενο από κρύσταλλο Kyber.",
    "funFacts": [
      "Ο χαρακτηριστικός βόμβος του φωτόσπαθου δημιουργήθηκε από τον ηχολήπτη Ben Burtt αναμιγνύοντας τον ήχο παλιών προβολέων κινηματογράφου και τηλεόρασης.",
      "Τα φωτόσπαθα των Τζεντάι έχουν συνήθως μπλε ή πράσινο χρώμα, ενώ των Σιθ είναι παραδοσιακά κόκκινα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%89%CF%84%CF%8C%CF%83%CF%80%CE%B1%CE%B8%CE%BF",
    "locale": "el-GR",
    "tags": ["star-wars", "lightsaber", "jedi", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_041",
    "text": "Στη σειρά «Η Τέλεια Ληστεία» (La Casa de Papel), ποιο όνομα πρωτεύουσας επέλεξε ως ψευδώνυμο η βασική αφηγήτρια;",
    "answers": ["Ναϊρόμπι", "Λισαβόνα", "Τόκιο", "Μπερλίν"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Silene Oliveira, την οποία υποδύεται η Ούρσουλα Κορμπερό, επιλέγει το όνομα 'Τόκιο' (Tokyo) και είναι η αφηγήτρια της σειράς.",
    "funFacts": [
      "Όλα τα μέλη της συμμορίας του Καθηγητή χρησιμοποιούν ονόματα παγκόσμιων πόλεων για να μην αποκαλύπτουν την πραγματική τους ταυτότητα.",
      "Η σειρά εκτόξευσε σε παγκόσμιο επίπεδο το ιταλικό αντιστασιακό τραγούδι 'Bella Ciao'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A4%CE%AD%CE%BB%CE%B5%CE%B9%CE%B1_%CE%9B%CE%B7%CF%83%CF%84%CE%B5%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["la-casa-de-papel", "netflix", "tokyo", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_042",
    "text": "Ποια διάσημη Ελληνίδα ηθοποιός με τα μαγευτικά μάτια πρωταγωνίστησε στις κωμωδίες «Το κοροϊδάκι της δεσποινίδος» και «Δεσποινίς Διευθυντής»;",
    "answers": ["Έλλη Λαμπέτη", "Μάρθα Καραγιάννη", "Μάρω Κοντού", "Τζένη Καρέζη"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Τζένη Καρέζη υπήρξε μία από τις μεγαλύτερες σταρ του ελληνικού θεάτρου και σινεμά, διάσημη για το ταλέντο και τα εκφραστικά της μάτια.",
    "funFacts": [
      "Στο 'Δεσποινίς Διευθυντής' (1964) είπε την αξέχαστη ατάκα 'Γυρίσατε;... Ε, τότε λοιπόν, να αλλάξω;'.",
      "Ήταν παντρεμένη με τον ηθοποιό Κώστα Καζάκο, με τον οποίο ανέβασε ιστορικές παραστάσεις όπως 'Το μεγάλο μας τσίρκο'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%AD%CE%BD%CE%B7_%CE%9A%CE%B1%CF%81%CE%AD%CE%B6%CE%B7",
    "locale": "el-GR",
    "tags": ["greek-cinema", "jenny-karezi", "comedy", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_043",
    "text": "Ποιος κορυφαίος ηθοποιός ενσάρκωσε τον ψυχωτικό συγγραφέα Τζακ Τόρανς στην ταινία τρόμου «Η Λάμψη» (The Shining, 1980);",
    "answers": ["Τζακ Νίκολσον", "Ρόμπερτ Ντε Νίρο", "Αλ Πατσίνο", "Τζιν Χάκμαν"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Jack Nicholson παρέδωσε μια ανεπανάληπτη ερμηνεία στο ψυχολογικό θρίλερ του Στάνλεϊ Κιούμπρικ, βασισμένο στο βιβλίο του Στίβεν Κινγκ.",
    "funFacts": [
      "Η σκηνή όπου σπάει την πόρτα με το τσεκούρι φωνάζοντας 'Here's Johnny!' χρειάστηκε τρεις ημέρες και δεκάδες πόρτες για να ολοκληρωθεί.",
      "Το ξενοδοχείο όπου εκτυλίσσεται η ιστορία ονομάζεται Overlook Hotel."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%9B%CE%AC%CE%BC%CF%88%CE%B7_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["the-shining", "jack-nicholson", "kubrick", "horror"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_044",
    "text": "Ποιος Ιρλανδός ηθοποιός κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου το 2024 υποδυόμενος τον Ρόμπερτ Οπενχάιμερ;",
    "answers": ["Κόλιν Φάρελ", "Κίλιαν Μέρφι", "Πολ Μέσκαλ", "Μπρένταν Γκλίσον"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Cillian Murphy πρωταγωνίστησε στην ταινία 'Oppenheimer' του Κρίστοφερ Νόλαν ενσαρκώνοντας τον 'πατέρα της ατομικής βόμβας'.",
    "funFacts": [
      "Έγινε ο πρώτος ιρλανδικής καταγωγής ηθοποιός γεννημένος στην Ιρλανδία που κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου.",
      "Η ταινία απέσπασε συνολικά 7 βραβεία Όσκαρ, ανάμεσά τους Καλύτερης Ταινίας και Σκηνοθεσίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AF%CE%BB%CE%B9%CE%B1%CE%BD_%CE%9C%CE%AD%CF%81%CF%86%CE%B9",
    "locale": "el-GR",
    "tags": ["oppenheimer", "cillian-murphy", "oscars", "nolan"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_045",
    "text": "Στην κωμική σειρά «The Big Bang Theory», ποια επιστήμη υπηρετούν και μελετούν ο Σέλντον και ο Λέοναρντ;",
    "answers": ["Βιολογία", "Γεωλογία", "Φυσική", "Αρχαιολογία"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Sheldon Cooper είναι θεωρητικός φυσικός και ο Leonard Hofstadter είναι πειραματικός φυσικός στο πανεπιστήμιο Caltech.",
    "funFacts": [
      "Η σειρά είχε ως επιστημονικό σύμβουλο τον καθηγητή David Saltzberg, ο οποίος έλεγχε και έγραφε όλες τις εξισώσεις στους πίνακες.",
      "Η σειρά διήρκεσε 12 σεζόν (2007–2019) συμπληρώνοντας 279 επεισόδια."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Big_Bang_Theory",
    "locale": "el-GR",
    "tags": ["the-big-bang-theory", "sitcom", "physics", "tv-series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_046",
    "text": "Ποιος σπουδαίος ηθοποιός υποδύθηκε τον «Αντωνάκη» δίπλα στη Μάρω Κοντού στην κλασική ταινία «Η δε γυνή να φοβήται τον άνδρα» (1965);",
    "answers": ["Ντίνος Ηλιόπουλος", "Κώστας Χατζηχρήστος", "Δημήτρης Παπαμιχαήλ", "Γιώργος Κωνσταντίνου"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Γιώργος Κωνσταντίνου ενσάρκωσε τον Αντώνη Κοκοβίκο, έναν αυταρχικό δημόσιο υπάλληλο απέναντι στην υπομονετική Ελενίτσα.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Γιώργο Τζαβέλλα και κέρδισε το βραβείο σκηνοθεσίας στο Φεστιβάλ του Σικάγου το 1965.",
      "Το ιστορικό νεοκλασικό σπίτι των Κοκοβίκων βρίσκεται στην Πλάκα (οδός Τριπόδων 32) και διατηρείται μέχρι σήμερα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B4%CE%B5_%CE%B3%CF%85%CE%BD%CE%AE_%CE%BD%CE%B1_%CF%86%CE%BF%CE%B2%CE%AE%CF%84%CE%B1%CE%B9_%CF%84%CE%BF%CE%BD_%CE%AC%CE%BD%CE%B4%CF%81%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "giorgos-konstantinou", "classics", "tzavellas"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_047",
    "text": "Από ποιον μακρινό πλανήτη κατάγεται ο υπερήρωας Σούπερμαν (Superman);",
    "answers": ["Κρύπτων", "Βάλκαν", "Άρης", "Άσγκαρντ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Superman γεννήθηκε στον πλανήτη Κρύπτωνα (Krypton) με το όνομα Καλ-Ελ, πριν καταστραφεί ο πλανήτης και σταλεί μωρό στη Γη.",
    "funFacts": [
      "Η μοναδική φυσική ουσία που μπορεί να του στερήσει τις δυνάμεις και να τον τραυματίσει είναι ο ραδιενεργός κρυπτονίτης.",
      "Στην ταινία-ορόσημο του 1978 τον Superman υποδύθηκε ο Κρίστοφερ Ριβ."
    ],
    "source": "https://el.wikipedia.org/wiki/Superman",
    "locale": "el-GR",
    "tags": ["superman", "dc-comics", "superheroes", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_048",
    "text": "Ποιος νεαρός ηθοποιός έγινε παγκόσμιος σούπερ σταρ υποδυόμενος τον Κέβιν ΜακΚάλιστερ στην ταινία «Μόνος στο Σπίτι» (1990);",
    "answers": ["Ντάνιελ Ράντκλιφ", "Μακόλεϊ Κάλκιν", "Ελάιτζα Γουντ", "Χέιλι Τζόελ Όσμεντ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Macaulay Culkin πρωταγωνίστησε ως ο οκτάχρονος Κέβιν που μένει κατά λάθος μόνος του στο σπίτι τα Χριστούγεννα και αντιμετωπίζει δύο αδέξιους διαρρήκτες.",
    "funFacts": [
      "Η ταινία γνώρισε τεράστια εμπορική επιτυχία, συγκεντρώνοντας σχεδόν 476 εκατομμύρια δολάρια παγκοσμίως.",
      "Η σκηνή όπου βάζει λοσιόν μετά το ξύρισμα και ουρλιάζει κρατώντας τα μάγουλά του ήταν εν μέρει αυτοσχεδιασμός του Κάλκιν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%8C%CE%BD%CE%BF%CF%82_%CF%83%CF%84%CE%BF_%CE%A3%CF%80%CE%AF%CF%84%CE%B9",
    "locale": "el-GR",
    "tags": ["home-alone", "macaulay-culkin", "christmas", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_049",
    "text": "Στη θρυλική κωμική σειρά του Mega «Στο Παρά 5», πόσα άτομα αποτελούν τη βασική ομάδα που ερευνά το έγκλημα;",
    "answers": ["Τρία", "Τέσσερα", "Πέντε", "Έξι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Οι πέντε εντελώς διαφορετικοί χαρακτήρες (Ντάλια, Ζουμπουλία, Αγγέλα, Φώτης, Σπύρος) εγκλωβίζονται σε ένα ασανσέρ και ξεκινούν κοινή έρευνα.",
    "funFacts": [
      "Η σειρά δημιουργήθηκε από τον Γιώργο Καπουτζίδη και κατέγραψε τηλεθέαση ρεκόρ που ξεπέρασε το 60% στο φινάλε της.",
      "Προβλήθηκε για δύο σεζόν (2005–2007) και θεωρείται μία από τις πιο επιτυχημένες ελληνικές σειρές όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["greek-tv", "sto-para-5", "kapoutzidis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_050",
    "text": "Στην ταινία επιστημονικής φαντασίας «Men in Black» (1997), τι χρώμα κουστούμια φορούν οι πράκτορες που επιτηρούν τους εξωγήινους;",
    "answers": ["Μπλε", "Γκρι", "Άσπρα", "Μαύρα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Οι πράκτορες της μυστικής οργάνωσης Men in Black φορούν αυστηρά μαύρα κοστούμια, λευκά πουκάμισα και μαύρα γυαλιά ηλίου.",
    "funFacts": [
      "Χρησιμοποιούν μια ειδική συσκευή που εκπέμπει φλας, το 'Neuralyzer', για να σβήνουν τις μνήμες των πολιτών που είδαν εξωγήινους.",
      "Στην ταινία πρωταγωνίστησαν ο Γουίλ Σμιθ (Agent J) και ο Τόμι Λι Τζόουνς (Agent K)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%86%CE%BD%CE%B4%CF%81%CE%B5%CF%82_%CE%BC%CE%B5_%CF%84%CE%B1_%CE%9C%CE%B1%CF%8D%CF%81%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["men-in-black", "sci-fi", "will-smith", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_051",
    "text": "Ποια είναι η πραγματική μυστική ταυτότητα του υπερήρωα Μπάτμαν (Batman);",
    "answers": ["Μπρους Γουέιν", "Πίτερ Πάρκερ", "Κλαρκ Κεντ", "Τόνι Σταρκ"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Bruce Wayne είναι ο δισεκατομμυριούχος βιομήχανος της Gotham City που μάχεται το έγκλημα ως Batman μετά τη δολοφονία των γονιών του.",
    "funFacts": [
      "Ο Μπάτμαν είναι ένας από τους ελάχιστους διάσημους υπερήρωες που δεν διαθέτει υπερφυσικές δυνάμεις, αλλά βασίζεται στην ευφυΐα, την τεχνολογία και τις πολεμικές τέχνες.",
      "Το αρχηγείο του βρίσκεται στην περίφημη Batcave, κάτω από την έπαυλη Wayne Manor."
    ],
    "source": "https://el.wikipedia.org/wiki/Batman",
    "locale": "el-GR",
    "tags": ["batman", "dc-comics", "superheroes", "bruce-wayne"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_052",
    "text": "Ποια σπουδαία κωμική ηθοποιός ενσάρκωσε την εκκεντρική θεία Καλλιόπη στην ταινία «Η θεία από το Σικάγο» (1957);",
    "answers": ["Ρένα Βλαχοπούλου", "Γεωργία Βασιλειάδου", "Σαπφώ Νοταρά", "Μαίρη Αρώνη"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Γεωργία Βασιλειάδου υποδύθηκε τη χειραφετημένη θεία από την Αμερική που αναστατώνει το αυστηρό σπίτι του αδελφού της (Ορέστη Μακρή).",
    "funFacts": [
      "Η ταινία σημείωσε τεράστια εισπρακτική επιτυχία για την εποχή της, κόβοντας 142.459 εισιτήρια στην πρώτη της προβολή.",
      "Η σκηνή όπου πετά κανάτια από το μπαλκόνι για να προσελκύσει γαμπρούς για τις ανιψιές της έμεινε κλασική."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B8%CE%B5%CE%AF%CE%B1_%CE%B1%CF%80%CF%8C_%CF%84%CE%BF_%CE%A3%CE%B9%CE%BA%CE%AC%CE%B3%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "georgia-vasileiadou", "comedy", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_053",
    "text": "Τι χρώμα είχαν τα μαγικά γοβάκια της Ντόροθι στην κλασική ταινία «Ο Μάγος του Οζ» (1939);",
    "answers": ["Χρυσά", "Ασημένια", "Κόκκινα (ρουμπινί)", "Πράσινα (σμαραγδένια)"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Τα ρουμπινί γοβάκια (Ruby Slippers) της Ντόροθι (Τζούντι Γκάρλαντ) την έστειλαν πίσω στο σπίτι της χτυπώντας τα τακούνια της τρεις φορές.",
    "funFacts": [
      "Στο αρχικό βιβλίο του L. Frank Baum τα γοβάκια ήταν ασημένια, αλλά άλλαξαν σε ρουμπινί για να εντυπωσιάσουν στην έγχρωμη τεχνολογία Technicolor.",
      "Ένα από τα αυθεντικά ζευγάρια παπουτσιών που χρησιμοποιήθηκαν στα γυρίσματα εκτίθεται στο Εθνικό Μουσείο Αμερικανικής Ιστορίας Smithsonian."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9C%CE%AC%CE%B3%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%9F%CE%B6_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1939)",
    "locale": "el-GR",
    "tags": ["wizard-of-oz", "judy-garland", "classics", "technicolor"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_054",
    "text": "Ποια διάσημη φράση επαναλαμβάνει ο αξιαγάπητος εξωγήινος στην ταινία «Ε.Τ. ο Εξωγήινος» (1982) προσπαθώντας να επικοινωνήσει με τον πλανήτη του;",
    "answers": ["«Ε.Τ. θέλω σπίτι»", "«Ε.Τ. πάρε με»", "«Ε.Τ. ζητά βοήθεια»", "«Ε.Τ. τηλέφωνο σπίτι»"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η φράση 'E.T. phone home' («E.T. τηλέφωνο σπίτι») είναι μία από τις πιο αναγνωρίσιμες και συγκινητικές ατάκες στην ιστορία του κινηματογράφου.",
    "funFacts": [
      "Η ταινία του Στίβεν Σπίλμπεργκ ξεπέρασε τον 'Πόλεμο των Άστρων' και έγινε η πιο κερδοφόρα ταινία όλων των εποχών μέχρι τότε.",
      "Κέρδισε 4 βραβεία Όσκαρ, συμπεριλαμβανομένου αυτού για την πρωτότυπη μουσική επένδυση του Τζον Γουίλιαμς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95.%CE%A4._%CE%BF_%CE%95%CE%BE%CF%89%CE%B3%CE%AE%CE%B9%CE%BD%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["et", "spielberg", "sci-fi", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_055",
    "text": "Ποια διάσημη Ελληνίδα κωμικός πρωταγωνίστησε στην ταινία «Μια Ελληνίδα στο χαρέμι» (1971) υποδυόμενη ένα ψεύτικο μέντιουμ στην έρημο;",
    "answers": ["Ρένα Βλαχοπούλου", "Μάρθα Καραγιάννη", "Μαίρη Χρονοπούλου", "Κατερίνα Γιουλάκη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ρένα Βλαχοπούλου χάρισε ανεπανάληπτες σκηνές γέλιου παριστάνοντας το μέντιουμ που διψάει και φωνάζει 'Τράβα μαλλί!'.",
    "funFacts": [
      "Οι σκηνές της ερήμου γυρίστηκαν στην πραγματικότητα στους αμμόλοφους της Ελαφονήσου και σε παραλίες της Αττικής.",
      "Η ταινία σκηνοθετήθηκε από τον Γιάννη Δαλιανίδη και σημείωσε τεράστια εμπορική επιτυχία με 455.385 εισιτήρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CE%95%CE%BB%CE%BB%CE%B7%CE%BD%CE%AF%CE%B4%CE%B1_%CF%83%CF%84%CE%BF_%CF%87%CE%B1%CF%81%CE%AD%CE%BC%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-cinema", "rena-vlachopoulou", "comedy", "dalianidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_056",
    "text": "Στην ταινία «Η Πεντάμορφη και το Τέρας» (1991), ποιο μαγικό αντικείμενο χάνει τα πέταλά του μετρώντας τον χρόνο της κατάρας;",
    "answers": ["Ένα μαγικό ρολόι", "Ένα μαγικό τριαντάφυλλο", "Ένας μαγικός καθρέφτης", "Ένα μαγικό βιβλίο"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το μαγεμένο τριαντάφυλλο θα άνθιζε μέχρι τα 21α γενέθλια του πρίγκιπα· αν δεν μάθαινε να αγαπά και να αγαπιέται πριν πέσει και το τελευταίο πέταλο, θα έμενε Τέρας για πάντα.",
    "funFacts": [
      "Υπήρξε η πρώτη ταινία κινουμένων σχεδίων στην ιστορία των Όσκαρ που προτάθηκε για Όσκαρ Καλύτερης Ταινίας.",
      "Κέρδισε δύο βραβεία Όσκαρ για την πρωτότυπη μουσική και το ομότιτλο τραγούδι του Άλαν Μένκεν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A0%CE%B5%CE%BD%CF%84%CE%AC%CE%BC%CE%BF%CF%81%CF%86%CE%B7_%CE%BA%CE%B1%CE%B9_%CF%84%CE%BF_%CE%A4%CE%AD%CF%81%CE%B1%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1991)",
    "locale": "el-GR",
    "tags": ["disney", "beauty-and-the-beast", "animation", "fairy-tale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_057",
    "text": "Σε ποια επιτυχημένη κωμική σειρά (mockumentary) παρακολουθούμε τις ζωές των οικογενειών Πρίτσετ, Ντάνφι και Τάκερ;",
    "answers": ["The Office", "Parks and Recreation", "Modern Family", "Brooklyn Nine-Nine"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το 'Modern Family' (2009–2020) παρουσιάζει σε στυλ ψευδοντοκιμαντέρ τις ξεκαρδιστικές σχέσεις μιας διευρυμένης σύγχρονης οικογένειας στο Λος Άντζελες.",
    "funFacts": [
      "Κέρδισε 5 συνεχόμενα βραβεία Emmy Καλύτερης Κωμικής Σειράς (2010–2014), ισοφαρίζοντας το ιστορικό ρεκόρ του 'Frasier'.",
      "Συνολικά απέσπασε 22 βραβεία Primetime Emmy κατά τη διάρκεια των 11 σεζόν της."
    ],
    "source": "https://el.wikipedia.org/wiki/Modern_Family",
    "locale": "el-GR",
    "tags": ["modern-family", "sitcom", "tv-series", "emmy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_058",
    "text": "Στη δημοφιλή ελληνική οικογενειακή σειρά «Το Σόι σου», ποια είναι τα επώνυμα των δύο συμπέθερων οικογενειών;",
    "answers": ["Παπαδοπούλου και Γεωργίου", "Κωνσταντίνου και Αντωνίου", "Δημητρίου και Νικολάου", "Τριανταφύλλου και Χαμπέα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά του Alpha εστιάζει στα κυριακάτικα οικογενειακά τραπέζια ανάμεσα στη λαϊκή οικογένεια Χαμπέα και την αστική οικογένεια Τριανταφύλλου.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 5 συνεχόμενες σεζόν (2014–2019) γνωρίζοντας τεράστια επιτυχία και υψηλή τηλεθέαση.",
      "Τους γονείς Χαμπέα υποδύθηκαν η Μίρκα Παπακωνσταντίνου και ο Γιώργος Γιαννόπουλος, ενώ τους γονείς Τριανταφύλλου η Ρένια Λουιζίδου και ο Παύλος Ορκόπουλος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%A3%CF%8C%CE%B9_%CF%83%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["greek-tv", "to-soi-sou", "alpha-tv", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_059",
    "text": "Ποιος διάσημος ηθοποιός του Χόλιγουντ πρωταγωνιστεί ως ο μυστικός πράκτορας Ίθαν Χαντ στη σειρά ταινιών «Επικίνδυνη Αποστολή» (Mission: Impossible);",
    "answers": ["Τομ Κρουζ", "Μπραντ Πιτ", "Κιάνου Ριβς", "Ματ Ντέιμον"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Tom Cruise πρωταγωνιστεί ως Ethan Hunt από το 1996, εκτελώντας ο ίδιος τα περισσότερα εξαιρετικά επικίνδυνα ακροβατικά των ταινιών.",
    "funFacts": [
      "Για τις ανάγκες των ταινιών έχει πηδήξει από αεροπλάνα σε ύψος 25.000 ποδιών (HALO jump) και έχει κρεμαστεί από το ψηλότερο κτίριο του κόσμου, το Μπουρτζ Χαλίφα.",
      "Το διάσημο μουσικό θέμα της σειράς συνέθεσε αρχικά ο Lalo Schifrin για την κλασική τηλεοπτική σειρά της δεκαετίας του 1960."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CE%BA%CE%AF%CE%BD%CE%B4%CF%85%CE%BD%CE%B7_%CE%91%CF%80%CE%BF%CF%83%CF%84%CE%BF%CE%BB%CE%AE_(%CF%83%CE%B5%CE%B9%CF%81%CE%AC_%CF%84%CE%B1%CE%B9%CE%BD%CE%B9%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["mission-impossible", "tom-cruise", "action", "spy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_060",
    "text": "Σε ποιο διάσημο μιούζικαλ του Γιάννη Δαλιανίδη (1964) ακούγεται το τραγούδι «Έχω στενάχωρη καρδιά» και διαδραματίζεται εν μέρει στη Ρόδο;",
    "answers": ["Μερικοί το προτιμούν κρύο", "Κάτι να καίει", "Κορίτσια για φίλημα", "Οι θαλασσιές οι χάντρες"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το 'Κάτι να καίει' (1964) της Φίνος Φιλμ ήταν το πρώτο ελληνικό μιούζικαλ γυρισμένο σε σύστημα Σινεμασκόπ με πρωταγωνιστές τους Βουτσά, Βλαχοπούλου και Καραγιάννη.",
    "funFacts": [
      "Υπήρξε η εμπορικότερη ταινία της σεζόν 1963–1964, κόβοντας περισσότερα από 660.000 εισιτήρια.",
      "Η μουσική και τα τραγούδια της ταινίας γράφτηκαν από τον σπουδαίο συνθέτη Μίμη Πλέσσα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%84%CE%B9_%CE%BD%CE%B1_%CE%BA%CE%B1%CE%AF%CE%B5%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dalianidis", "musical", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'easy', 1, questions)

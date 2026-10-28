# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "cinema_tv_easy_161",
    "text": "Ποια συγκλονιστική συγγενική σχέση αποκαλύπτει ο Νταρθ Βέιντερ στον Λουκ Σκαϊγουόκερ στην ταινία «Η Αυτοκρατορία Αντεπιτίθεται» (1980);",
    "answers": ["Ότι είναι ο πατέρας του", "Ότι είναι ο αδελφός του", "Ότι είναι ο θείος του", "Ότι είναι ο παππούς του"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η ατάκα 'No, I am your father' («Όχι, εγώ είμαι ο πατέρας σου») αποτελεί τη διασημότερη σεναριακή ανατροπή στην ιστορία του κινηματογράφου.",
    "funFacts": [
      "Στο αρχικό σενάριο η ατάκα κρατήθηκε απόλυτο μυστικό και μόνο ο Τζορτζ Λούκας, ο σκηνοθέτης και ο Μαρκ Χάμιλ γνώριζαν την αλήθεια πριν τα γυρίσματα.",
      "Συχνά αναφέρεται λανθασμένα ως 'Luke, I am your father', αποτελώντας ένα από τα πιο γνωστά misquotes της ποπ κουλτούρας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%B1%CF%81%CE%B8_%CE%92%CE%AD%CE%B9%CE%BD%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["star-wars", "darth-vader", "luke-skywalker", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_162",
    "text": "Τι είδους ζώο είναι ο ανέμελος Μπαλού, ο πιστός φίλος του Μόγλη στην ταινία της Disney «Το Βιβλίο της Ζούγκλας» (1967);",
    "answers": ["Πάνθηρας", "Αρκούδα", "Τίγρης", "Λύκος"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Baloo είναι μια καλόκαρδη και νωχελική αρκούδα που διδάσκει στον Μόγλη να απολαμβάνει τις απλές χαρές της ζωής με το τραγούδι 'The Bare Necessities'.",
    "funFacts": [
      "Υπήρξε η τελευταία ταινία κινουμένων σχεδίων στην οποία επέβλεψε προσωπικά την παραγωγή ο ίδιος ο Γουόλτ Ντίσνεϊ πριν πεθάνει.",
      "Βασίστηκε στην ομώνυμη συλλογή διηγημάτων του Βρετανού συγγραφέα Ράντγιαρντ Κίπλινγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%92%CE%B9%CE%B2%CE%BB%CE%AF%CE%BF_%CF%84%CE%B7%CF%82_%CE%96%CE%BF%CF%8D%CE%B3%CE%BA%CE%BB%CE%B1%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1967)",
    "locale": "el-GR",
    "tags": ["disney", "the-jungle-book", "baloo", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_163",
    "text": "Στη σειρά «Στο Παρά 5», ποια εκκεντρική πάμπλουτη κληρονόμος ενσάρκωσε η Σμαράγδα Καρύδη;",
    "answers": ["Ζουμπουλία Αμπατζίδου", "Αγγέλα Ιωακειμίδου", "Ντάλια Χατζηαλεξάνδρου", "Αμαλία Αντωνοπούλου"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ντάλια Χατζηαλεξάνδρου ήταν η απομονωμένη από την κοινωνία δισεκατομμυριούχος που δεν ήξερε την αξία των χρημάτων ούτε πώς μοιάζουν τα απλά καθημερινά πράγματα.",
    "funFacts": [
      "Η διάσημη ατάκα της 'Πόσο κάνει αυτό; Ένα εκατομμύριο;' έμεινε κλασική στην ελληνική τηλεόραση.",
      "Η σειρά απέσπασε πολυάριθμα βραβεία και έκανε ρεκόρ τηλεθέασης τις σεζόν 2005–2007."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["greek-tv", "sto-para-5", "dalia", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_164",
    "text": "Ποιο είναι το φανταστικό και τεχνολογικά υπερεξελιγμένο αφρικανικό βασίλειο στο οποίο βασιλεύει ο Black Panther;",
    "answers": ["Ζαμούντα", "Γένοβα", "Σοκόβια", "Γουακάντα (Wakanda)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Wakanda είναι η απομονωμένη αφρικανική χώρα που κρύβει την τεράστια τεχνολογική της πρόοδο πίσω από ένα ολογραφικό πέπλο ζούγκλας.",
    "funFacts": [
      "Ο χαιρετισμός 'Wakanda Forever' με τους βραχίονες σταυρωμένους στο στήθος έγινε παγκόσμιο πολιτιστικό φαινόμενο.",
      "Η ταινία 'Black Panther' (2018) υπήρξε η πρώτη ταινία με υπερήρωες που προτάθηκε για Όσκαρ Καλύτερης Ταινίας."
    ],
    "source": "https://el.wikipedia.org/wiki/Black_Panther_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["marvel", "black-panther", "wakanda", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_165",
    "text": "Ποιος κορυφαίος σκηνοθέτης υπέγραψε τα μεγαλύτερα μιούζικαλ της Φίνος Φιλμ, όπως «Μερικοί το προτιμούν κρύο» και «Κορίτσια για φίλημα»;",
    "answers": ["Γιάννης Δαλιανίδης", "Αλέκος Σακελλάριος", "Ντίνος Δημόπουλος", "Γιώργος Τζαβέλλας"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Γιάννης Δαλιανίδης υπήρξε ο κατεξοχήν δημιουργός του ελληνικού κινηματογραφικού μιούζικαλ, αλλά και σπουδαίων κοινωνικών δραμάτων όπως 'Ο κατήφορος'.",
    "funFacts": [
      "Καθιέρωσε στη μεγάλη οθόνη μεγάλα ονόματα όπως η Ζωή Λάσκαρη, ο Κώστας Βουτσάς και η Μάρθα Καραγιάννη.",
      "Αργότερα δημιούργησε μερικές από τις πιο επιτυχημένες σειρές της ελληνικής τηλεόρασης, όπως 'Το Ρετιρέ' και 'Οι Μικρομεσαίοι'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%94%CE%B1%CE%BB%CE%B9%CE%B1%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dalianidis", "musical", "directors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_166",
    "text": "Ποιο είναι το όνομα του αξιαγάπητου μπλε ψαριού με απώλεια πρόσφατης μνήμης στην ταινία «Ψάχνοντας τον Νέμο» (2003);",
    "answers": ["Πεταλούδα", "Ντόρι (Dory)", "Μπλου", "Σάμι"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Dory είναι ένα μπλε ψάρι (blue tang) που υποφέρει από απώλεια βραχυπρόθεσμης μνήμης και βοηθά τον Μάρλιν να διασχίσει τον ωκεανό.",
    "funFacts": [
      "Στην αγγλική πρωτότυπη εκδοχή τη φωνή της Ντόρι χάρισε η διάσημη παρουσιάστρια Έλεν ΝτιΤζένερις.",
      "Η τεράστια επιτυχία του χαρακτήρα οδήγησε στη δική της αυτόνομη ταινία 'Ψάχνοντας την Ντόρι' (Finding Dory) το 2016."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A8%CE%AC%CF%87%CE%BD%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CE%BF%CE%BD_%CE%9D%CE%AD%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["pixar", "finding-nemo", "dory", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_167",
    "text": "Στη σειρά «Στο Παρά 5», ποια πρωταγωνίστρια από τις Σέρρες μιλούσε με βαριά βορειοελλαδίτικη προφορά και μαγείρευε συνεχώς;",
    "answers": ["Ντάλια", "Αγγέλα", "Ζουμπουλία", "Αμαλία"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ζουμπουλία Αμπατζίδου (Ελισάβετ Κωνσταντινίδου) ήταν η παραδοσιακή γυναίκα από τις Σέρρες που προκάλεσε αμέτρητες σκηνές γέλιου με τις εκφράσεις της.",
    "funFacts": [
      "Η σχέση αγάπης και μίσους ανάμεσα στη Ζουμπουλία και τη συμπεθέρα της Μαριάνθη αποτέλεσε βασικό κωμικό στοιχείο της σειράς.",
      "Η χαρακτηριστική ατάκα της 'Πού πας, μωρή;' έμεινε αξέχαστη στο τηλεοπτικό κοινό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["greek-tv", "sto-para-5", "zoumpoulia", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_168",
    "text": "Ποιο είναι το όνομα του γιγάντιου φιδιού του Λόρδου Βόλντεμορτ που λειτουργούσε και ως Πεμπτουσιωτής του στον «Χάρι Πότερ»;",
    "answers": ["Βασιλίσκος", "Άραγκογκ", "Φλάφι", "Ναγκίνι (Nagini)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Nagini είναι το τεράστιο δηλητηριώδες ερπετό που υπακούει τυφλά στον Βόλντεμορτ και επικοινωνεί μαζί του στη γλώσσα των φιδιών (Parseltongue).",
    "funFacts": [
      "Στην τελική Μάχη του Χόγκουαρτς, ο Νέβιλ Λονγκμπότομ αποκεφαλίζει τη Ναγκίνι με το σπαθί του Γκρίφιντορ.",
      "Στις ταινίες 'Φανταστικά Ζώα' αποκαλύπτεται ότι η Ναγκίνι ήταν αρχικά μια γυναίκα με κατάρα αίματος (Maledictus) που μετατράπηκε μόνιμα σε φίδι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CE%B9_%CE%A0%CF%8C%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["harry-potter", "voldemort", "nagini", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_169",
    "text": "Στη δραματική ταινία «Το χώμα βάφτηκε κόκκινο» (1966), σε ποια γεωγραφική περιοχή της Ελλάδας μαίνεται η σύγκρουση κολλήγων και τσιφλικάδων;",
    "answers": ["Στον Θεσσαλικό κάμπο", "Στην πεδιάδα των Σερρών", "Στην πεδιάδα της Άρτας", "Στο οροπέδιο Λασιθίου"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η ταινία του Βασίλη Γεωργιάδη εκτυλίσσεται στη Θεσσαλία το 1907, εξιστορώντας τους αγώνες των ακτημόνων αγροτών για τη γη.",
    "funFacts": [
      "Η ταινία υπήρξε υποψήφια για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας το 1966.",
      "Πρωταγωνίστησαν σπουδαίοι ηθοποιοί όπως ο Νίκος Κούρκουλος, ο Γιάννης Βόγλης και ο Μάνος Κατράκης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%87%CF%8E%CE%BC%CE%B1_%CE%B2%CE%AC%CF%86%CF%84%CE%B7%CE%BA%CE%B5_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "kourkoulos", "oscars", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_170",
    "text": "Ποιο πελώριο παγωμένο οχύρωμα προστατεύει τα Επτά Βασίλεια από τις απειλές του ακραίου Βορρά στο «Game of Thrones»;",
    "answers": ["Το Σιδερένιο Φρούριο", "Το Τείχος (The Wall)", "Η Παγωμένη Πύλη", "Το Μαύρο Κάστρο"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Τείχος είναι μια κολοσσιαία κατασκευή από συμπαγή πάγο μήκους 480 χιλιομέτρων και ύψους άνω των 200 μέτρων που επανδρώνεται από τη Νυχτερινή Φρουρά.",
    "funFacts": [
      "Ο Τζορτζ Ρ. Ρ. Μάρτιν εμπνεύστηκε το Τείχος από μια επίσκεψή του στο πραγματικό Τείχος του Αδριανού στη βόρεια Αγγλία.",
      "Στην έβδομη σεζόν της σειράς, ο Night King καταστρέφει ένα μέρος του Τείχους χρησιμοποιώντας τον αναστημένο δράκο Viserion."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_of_Thrones",
    "locale": "el-GR",
    "tags": ["game-of-thrones", "the-wall", "fantasy", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_171",
    "text": "Στην κωμική σειρά «Λατρεμένοι μου γείτονες» (Mega), ποια είναι τα επώνυμα των δύο οικογενειών που συγκρούονται;",
    "answers": ["Παπαδοπούλου και Γεωργίου", "Κωνσταντίνου και Αντωνίου", "Μουστάκα και Παπαπαύλου", "Τριανταφύλλου και Χαμπέα"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η λαϊκή οικογένεια του μανάβη Μπάμπη Μουστάκα μετακομίζει στα βόρεια προάστια δίπλα στην καθώς πρέπει αστική οικογένεια του οδοντιάτρου Παπαπαύλου.",
    "funFacts": [
      "Η σειρά προβλήθηκε τις σεζόν 2007–2009 σημειώνοντας υψηλά ποσοστά τηλεθέασης.",
      "Βασίστηκε στην επιτυχημένη ισπανική σειρά 'Mis adorables vecinos'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B1%CF%84%CF%81%CE%B5%CE%BC%CE%AD%CE%BD%CE%BF%CE%B9_%CE%BC%CE%BF%CF%85_%CE%B3%CE%B5%CE%AF%CF%84%CE%BF%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["greek-tv", "latremenoi-mou-geitones", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_172",
    "text": "Ποιο είναι το αγαπημένο αλκοολούχο ποτό του καπετάνιου Τζακ Σπάροου στις ταινίες «Οι Πειρατές της Καραϊβικής»;",
    "answers": ["Ουίσκι", "Μπίρα", "Κονιάκ", "Ρούμι"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το ρούμι (rum) είναι η μεγάλη αδυναμία του Jack Sparrow, ο οποίος αναφωνεί απελπισμένος στη δεύτερη ταινία: 'Why is the rum gone?' ('Γιατί τελείωσε το ρούμι;').",
    "funFacts": [
      "Η διάσημη ατάκα για το ρούμι ήταν ένας από τους πολλούς αυτοσχεδιασμούς του Τζόνι Ντεπ κατά τα γυρίσματα.",
      "Το ρούμι ήταν ιστορικά το κατεξοχήν ποτό των πειρατών και των ναυτικών στην περιοχή της Καραϊβικής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CF%8C%CE%BD%CE%B9_%CE%9D%CF%84%CE%B5%CF%80",
    "locale": "el-GR",
    "tags": ["pirates-of-the-caribbean", "jack-sparrow", "disney", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_173",
    "text": "Στη ρομαντική κωμωδία «Γάμος αλά ελληνικά» (1964), ποια αγαπημένη ηθοποιός πρωταγωνίστησε ως η νεαρή νύφη Μίνα;",
    "answers": ["Ξένια Καλογεροπούλου", "Μάρθα Καραγιάννη", "Μπέτυ Αρβανίτη", "Ζωή Λάσκαρη"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ξένια Καλογεροπούλου πρωταγωνίστησε ως η Μίνα, κερδίζοντας το Βραβείο Α' Γυναικείου Ρόλου στο Φεστιβάλ Κινηματογράφου Θεσσαλονίκης το 1964.",
    "funFacts": [
      "Συμπρωταγωνίστησε με τον Γιώργο Πάντζα υπό τη σκηνοθεσία του Βασίλη Γεωργιάδη.",
      "Η ταινία προβλήθηκε με επιτυχία και στο εξωτερικό, αποσπώντας θετικές κριτικές για τη φρεσκάδα της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%AC%CE%BC%CE%BF%CF%82_%CE%B1%CE%BB%CE%AC_%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AC_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["greek-cinema", "kalogeropoulou", "comedy", "romance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_174",
    "text": "Σε ποια ανθεκτική και πολεμοχαρή φυλή ανήκει ο Γκίμλι στον «Άρχοντα των Δαχτυλιδιών»;",
    "answers": ["Ξωτικά", "Νάνοι", "Άνθρωποι", "Ορκ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Gimli, γιος του Glóin, είναι ο εκπρόσωπος των Νάνων (Dwarves) στη Συντροφιά του Δαχτυλιδιού, οπλισμένος με βαριά τσεκούρια.",
    "funFacts": [
      "Τον Γκίμλι υποδύθηκε ο Ουαλός ηθοποιός Τζον Ρις-Ντέιβις, ο οποίος στην πραγματικότητα ήταν ο ψηλότερος από όλους τους ηθοποιούς της Συντροφιάς (1,85 μ.).",
      "Η φιλία του με το ξωτικό Λέγκολας γεφύρωσε το πανάρχαιο μίσος ανάμεσα στις δύο φυλές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%86%CF%81%CF%87%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CF%89%CE%BD_%CE%94%CE%B1%CF%87%CF%84%CF%85%CE%BB%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "gimli", "dwarf", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_175",
    "text": "Στη σειρά «Η Πολυκατοικία» (Mega), ποιον ρόλο είχε ο καταπιεστικός και περίεργος Θανάσης Μπαλαφούτης (Παύλος Χαϊκάλης);",
    "answers": ["Θυρωρός και υδραυλικός", "Πρόεδρος δικαστηρίου", "Διαχειριστής της πολυκατοικίας", "Αστυνομικός της γειτονιάς"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Θανάσης Μπαλαφούτης ήταν ο αυταρχικός διαχειριστής που παρακολουθούσε συνεχώς τους ενοίκους και συγκέντρωνε με το ζόρι τα κοινόχρηστα.",
    "funFacts": [
      "Η σειρά προβλήθηκε για 3 σεζόν (2008–2011) γνωρίζοντας μεγάλη εμπορική επιτυχία.",
      "Βασίστηκε στην ισπανική τηλεοπτική επιτυχία 'Aquí no hay quien viva'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%A0%CE%BF%CE%BB%CF%85%CE%BA%CE%B1%CF%84%CE%BF%CE%B9%CE%BA%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-tv", "i-polykatoikia", "chaikalis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_176",
    "text": "Ποιος υπερκακός, πατέρας του Χάρι Όσμπορν, πετάει με ανεμόπτερο και πετά εκρηκτικές κολοκύθες στον Spider-Man;",
    "answers": ["Doctor Octopus", "Venom", "Sandman", "Πράσινος Καλικάντζαρος (Green Goblin)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Norman Osborn μετατρέπεται στον Green Goblin μετά τη χρήση ενός πειραματικού ορού ενίσχυσης της δύναμης που τον οδηγεί στην παράνοια.",
    "funFacts": [
      "Στην ταινία 'Spider-Man' του 2002 τον ρόλο ενσάρκωσε μοναδικά ο Γουίλεμ Νταφόε.",
      "Ο Νταφόε επανέλαβε τον θρυλικό του ρόλο είκοσι χρόνια αργότερα στο 'Spider-Man: No Way Home' (2021)."
    ],
    "source": "https://el.wikipedia.org/wiki/Spider-Man",
    "locale": "el-GR",
    "tags": ["spider-man", "green-goblin", "marvel", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_177",
    "text": "Σε ποια μουσική ταινία του 1966 η Αλίκη Βουγιουκλάκη και ο Δημήτρης Παπαμιχαήλ τραγουδούν τις μεγάλες επιτυχίες του Σταύρου Ξαρχάκου;",
    "answers": ["Διπλοπενιές", "Η κόρη μου η σοσιαλίστρια", "Αχ! Αυτή η γυναίκα μου", "Το πιο λαμπρό αστέρι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Στις 'Διπλοπενιές' (1966) ακούστηκαν διαχρονικά τραγούδια όπως 'Μάτια βουρκωμένα' και 'Στου Όθωνα τα χρόνια' σε μουσική Σταύρου Ξαρχάκου.",
    "funFacts": [
      "Η ταινία προβλήθηκε στο Φεστιβάλ των Καννών με τον διεθνή τίτλο 'Dancing the Sirtaki'.",
      "Έκοψε περισσότερα από 463.000 εισιτήρια κατά την πρώτη της προβολή στους κινηματογράφους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CF%80%CE%BB%CE%BF%CF%80%CE%B5%CE%BD%CE%B9%CE%AD%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "diplopenies", "xarchakos", "vougiouklaki"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_178",
    "text": "Στη σειρά κινουμένων σχεδίων «The Simpsons», ποιο είναι το όνομα της ταβέρνας όπου συχνάζει ο Χόμερ για να πίνει μπίρα Duff;",
    "answers": ["Η ταβέρνα του Τζο", "Η ταβέρνα του Μο (Moe's Tavern)", "Το στέκι του Μπαρνς", "Το καφέ του Κράστι"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Moe's Tavern ανήκει στον δύστροπο αλλά καλόκαρδο μπάρμαν Moe Szyslak και είναι το αγαπημένο στέκι του Homer Simpson και των φίλων του.",
    "funFacts": [
      "Ο Μπαρτ Σίμπσον κάνει συχνά τηλεφωνικές φάρσες στον Μο ζητώντας πελάτες με αστεία ονόματα με διπλό νόημα.",
      "Πραγματικό αντίγραφο του Moe's Tavern λειτουργεί στα θεματικά πάρκα της Universal Studios."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Simpsons",
    "locale": "el-GR",
    "tags": ["the-simpsons", "moes-tavern", "homer-simpson", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_179",
    "text": "Στη μαύρη κωμωδία «Τι ψυχή θα παραδώσεις μωρή;» (Mega, 2000), πόσες γυναίκες ενώνουν τις δυνάμεις τους για να εκδικηθούν τον κακοποιητή τους;",
    "answers": ["Δύο", "Τρεις", "Τέσσερις", "Έξι"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Τέσσερις εντελώς διαφορετικές γυναίκες (Αλέκα, Ντομινίκ, Πόπη και Φωφώ) που μεγάλωσαν στο ίδιο ορφανοτροφείο αποφασίζουν να σκοτώσουν τον διευθυντή που τις κακοποιούσε.",
    "funFacts": [
      "Η σειρά των Αλέξανδρου Ρήγα και Δημήτρη Αποστόλου σταμάτησε απότομα μετά από μόλις 7 επεισόδια λόγω έντονων παρασκηνιακών διαφωνιών.",
      "Παρά τη σύντομη διάρκειά της, απέκτησε φανατικό κοινό και θεωρείται μία από τις πιο καλτ σειρές στην ιστορία της ελληνικής τηλεόρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9_%CF%88%CF%85%CF%87%CE%AE_%CE%B8%CE%B1_%CF%80%CE%B1%CF%81%CE%B1%CE%B4%CF%8E%CF%83%CE%B5%CE%B9%CF%82_%CE%BC%CF%89%CF%81%CE%AE%3B",
    "locale": "el-GR",
    "tags": ["greek-tv", "ti-psychi-tha-paradoseis-mori", "mega-channel", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_180",
    "text": "Στην ταινία «Jurassic Park», ποιο προϊστορικό έντομο παγιδευμένο σε κεχριμπάρι περιείχε το αίμα δεινοσαύρου για την κλωνοποίηση;",
    "answers": ["Μέλισσα", "Λιβελούλα", "Σκαθάρι", "Κουνούπι"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ένα προϊστορικό κουνούπι είχε τσιμπήσει δεινόσαυρους και στη συνέχεια παγιδεύτηκε σε ρετσίνι δέντρου που έγινε κεχριμπάρι, διατηρώντας το DNA τους ανέπαφο.",
    "funFacts": [
      "Το μπαστούνι του ιδρυτή του πάρκου, Τζον Χάμοντ, είχε στην κορυφή του ένα κομμάτι κεχριμπάρι με ένα παγιδευμένο κουνούπι.",
      "Στην πραγματικότητα, το DNA αποδομείται πολύ ταχύτερα από όσο απαιτείται για να επιβιώσει 65 εκατομμύρια χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CF%85%CF%81%CE%AC%CF%83%CE%B9%CE%BA_%CE%A0%CE%B1%CF%81%CE%BA_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["jurassic-park", "dinosaurs", "amber", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_181",
    "text": "Ποιος κορυφαίος ηθοποιός πρωταγωνίστησε ως ο ταμίας τραπέζης Κλέων στην κλασική κωμωδία «Μια ζωή την έχουμε» (1958);",
    "answers": ["Δημήτρης Χορν", "Αλέκος Αλεξανδράκης", "Ντίνος Ηλιόπουλος", "Μάνος Κατράκης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Δημήτρης Χορν υποδύθηκε έναν φτωχό υπάλληλο που βρίσκει έλλειμμα στα βιβλία της τράπεζας και αποφασίζει να καταχραστεί τα χρήματα για να ζήσει πλουσιοπάροχα.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Γιώργο Τζαβέλλα και απέκτησε διαχρονική αξία για τις φιλοσοφικές της προεκτάσεις γύρω από την ευτυχία.",
      "Η συμπρωταγωνίστρια του Χορν ήταν η διάσημη Ιταλίδα ηθοποιός Υβόν Σανσόν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%B1_%CE%B6%CF%89%CE%AE_%CF%84%CE%B7%CE%BD_%CE%AD%CF%87%CE%BF%CF%85%CE%BC%CE%B5",
    "locale": "el-GR",
    "tags": ["greek-cinema", "dimitris-horn", "tzavellas", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_182",
    "text": "Ποιο μυθικό φτερωτό άλογο είναι ο πιστός σύντροφος του Ηρακλή στην ταινία κινουμένων σχεδίων της Disney (1997);",
    "answers": ["Βουκεφάλας", "Πήγασος", "Κένταυρος", "Χείρων"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Pegasus είναι το φτερωτό άλογο φτιαγμένο από σύννεφα που χάρισε ο Δίας στον γιο του Ηρακλή όταν γεννήθηκε.",
    "funFacts": [
      "Στην ελληνική μυθολογία ο Πήγασος συνδέεται κυρίως με τον ήρωα Βελλερεφόντη, αλλά η Disney τον συνέδεσε με τον Ηρακλή.",
      "Η ταινία διακρίθηκε για τη μουσική της που συνδύασε ελληνικούς μύθους με παραδοσιακή γκόσπελ μουσική."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97%CF%81%CE%B1%CE%BA%CE%BB%CE%AE%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1997)",
    "locale": "el-GR",
    "tags": ["disney", "hercules", "pegasus", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_183",
    "text": "Ποιος δημοφιλής σατιρικός δημιουργός εμπνεύστηκε και υποδύθηκε σχεδόν όλους τους χαρακτήρες στη σατιρική σειρά «Δέκα Μικροί Μήτσοι»;",
    "answers": ["Χάρρυ Κλυνν", "Γιώργος Μητσικώστας", "Λάκης Λαζόπουλος", "Γιάννης Ζουγανέλης"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Λάκης Λαζόπουλος δημιούργησε και ενσάρκωσε 20 διαφορετικούς ρόλους (όπως η χήρα Μήτση, ο γύφτος, ο αστυνόμος) σατιρίζοντας την ελληνική κοινωνία.",
    "funFacts": [
      "Η σειρά προβλήθηκε από το Mega μεταξύ 1992 και 2003 γνωρίζοντας πρωτοφανή επιτυχία και τηλεθέαση που ξεπερνούσε το 50%.",
      "Στη σειρά συμμετείχαν ως καλεσμένοι κορυφαίοι Έλληνες καλλιτέχνες, ανάμεσά τους και η Αλίκη Βουγιουκλάκη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BA%CE%B1_%CE%9C%CE%B9%CE%BA%CF%81%CE%BF%CE%AF_%CE%9C%CE%AE%CF%84%CF%83%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "deka-mikroi-mitsoi", "lazopoulos", "satire"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_184",
    "text": "Ποιο είναι το όνομα της τελευταίας ανθρώπινης πόλης στα έγκατα της Γης στην τριλογία ταινιών «The Matrix»;",
    "answers": ["Ατλαντίδα", "Ματρίξ", "Βαβυλώνα", "Σιών (Zion)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Zion είναι η υπόγεια πόλη κοντά στον θερμό πυρήνα της Γης, όπου επιβιώνουν οι ελεύθεροι άνθρωποι που έχουν αποσυνδεθεί από το Matrix.",
    "funFacts": [
      "Το όνομα Zion είναι άμεση βιβλική αναφορά στη γη της επαγγελίας και της σωτηρίας.",
      "Στην τρίτη ταινία ('The Matrix Revolutions'), η άμυνα της Σιών απέναντι στις στρατιές των Sentinels αποτελεί την κορύφωση της πλοκής."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Matrix",
    "locale": "el-GR",
    "tags": ["the-matrix", "zion", "sci-fi", "cyberpunk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_185",
    "text": "Στην κωμωδία «Ο Κλέαρχος, η Μαρίνα και ο κοντός» (1961), ποια ηθοποιός υποδύθηκε τη ζηλιάρα σύζυγο Μαρίνα που παρακολουθεί τον άντρα της;",
    "answers": ["Γεωργία Βασιλειάδου", "Ρένα Βλαχοπούλου", "Μαίρη Αρώνη", "Σαπφώ Νοταρά"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Γεωργία Βασιλειάδου υποδύθηκε τη Μαρίνα που υποψιάζεται τον άντρα της Κλέαρχο (Βασίλη Αυλωνίτη) και βάζει τον γαμπρό της (Νίκο Ρίζο) να τον παρακολουθήσει στα Καμένα Βούρλα.",
    "funFacts": [
      "Ο Νίκος Ρίζος ως 'κοντός' χάρισε αξέχαστες σκηνές κωμωδίας απέναντι στον Αυλωνίτη και τη Βασιλειάδου.",
      "Η ταινία της Φίνος Φιλμ ήταν βασισμένη στο θεατρικό έργο των Νίκου Τσιφόρου και Πολύβιου Βασιλειάδη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9A%CE%BB%CE%AD%CE%B1%CF%81%CF%87%CE%BF%CF%82,_%CE%B7_%CE%9C%CE%B1%CF%81%CE%AF%CE%BD%CE%B1_%CE%BA%CE%B1%CE%B9_%CE%BF_%CE%BA%CE%BF%CE%BD%CF%84%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "vasileiadou", "avlonitis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_186",
    "text": "Σε ποια φανταστική μικρή πόλη της πολιτείας Ιντιάνα διαδραματίζονται τα μυστήρια της σειράς «Stranger Things»;",
    "answers": ["Σπρίνγκφιλντ", "Χόκινς (Hawkins)", "Ρίβερντεϊλ", "Σάνιγκεϊλ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η πόλη Hawkins είναι το επίκεντρο των παραφυσικών φαινομένων λόγω των μυστικών κυβερνητικών πειραμάτων στο Εθνικό Εργαστήριο Hawkins.",
    "funFacts": [
      "Παρότι η υπόθεση τοποθετείται στην Ιντιάνα, τα γυρίσματα πραγματοποιήθηκαν κυρίως στην πολιτεία της Τζόρτζια των ΗΠΑ.",
      "Η σειρά των αδελφών Duffer έκανε πρεμιέρα το 2016 και έγινε παγκόσμιο φαινόμενο της σύγχρονης τηλεόρασης."
    ],
    "source": "https://el.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger-things", "hawkins", "netflix", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_187",
    "text": "Ποιο είναι το κεντρικό θέμα της μακροβιότερης ελληνικής κωμικής σειράς του Alpha «Μην αρχίζεις τη μουρμούρα»;",
    "answers": ["Η ζωή σε ένα δικηγορικό γραφείο", "Οι περιπέτειες ενοίκων σε ένα ξενοδοχείο", "Η καθημερινή ζωή και τα πειράγματα ζευγαριών διαφορετικών ηλικιών", "Η λειτουργία μιας οικογενειακής ταβέρνας"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η σειρά παρουσιάζει με χιουμοριστικό τρόπο την καθημερινότητα, τους καβγάδες και την αγάπη διαφορετικών ζευγαριών διαφόρων ηλικιακών ομάδων στην Ελλάδα.",
    "funFacts": [
      "Ξεκίνησε να προβάλλεται το 2013 και ξεπέρασε τις 11 σεζόν και τα 900 επεισόδια.",
      "Ένα από τα πιο αγαπημένα ζευγάρια υπήρξε ο Μηνάς (Αντώνης Αντωνίου) και η Βούλα (Ελένη Κοκκίδου)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B7%CE%BD_%CE%B1%CF%81%CF%87%CE%AF%CE%B6%CE%B5%CE%B9%CF%82_%CF%84%CE%B7_%CE%BC%CE%BF%CF%85%CF%81%CE%BC%CE%BF%CF%8D%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-tv", "mourmoura", "alpha-tv", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_188",
    "text": "Τι χρώμα έχει ο Λίθος του Χρόνου (Time Stone) που φυλάσσει ο Doctor Strange στο Μάτι του Αγκαμότο;",
    "answers": ["Μπλε", "Κόκκινο", "Μωβ", "Πράσινο"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Time Stone έχει φωτεινό σμαραγδένιο πράσινο χρώμα και επιτρέπει στον κάτοχό του να χειραγωγεί τη ροή του χρόνου προς το παρελθόν ή το μέλλον.",
    "funFacts": [
      "Είναι ένας από τους έξι Λίθους της Αιωνιότητας (Infinity Stones) που προσπαθεί να συγκεντρώσει ο Thanos στο 'Avengers: Infinity War'.",
      "Τον Doctor Strange υποδύεται στο MCU ο Βρετανός ηθοποιός Μπένεντικτ Κάμπερμπατς."
    ],
    "source": "https://el.wikipedia.org/wiki/Doctor_Strange_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["marvel", "doctor-strange", "infinity-stones", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_189",
    "text": "Στην κωμωδία «Υπάρχει και φιλότιμο», ποιο είναι το όνομα του επαρχιακού χωριού όπου τρακάρει ο υπουργός Μαυρογιαλούρος;",
    "answers": ["Πλατανίτσα", "Αγριλόκαμπος", "Κολοκοτρωνίτσι", "Καστανιά"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το αυτοκίνητο του υπουργού συγκρούεται έξω από το χωριό Πλατανίτσα, αναγκάζοντάς τον να φιλοξενηθεί incognito στο σπίτι ενός απλού χωρικού.",
    "funFacts": [
      "Εκεί έρχεται αντιμέτωπος με τις πραγματικές ελλείψεις και τα παράπονα των κατοίκων για τα έργα που υποσχέθηκε αλλά δεν έγιναν ποτέ.",
      "Η ταινία προβλήθηκε το 1965 και έκοψε 451.000 εισιτήρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%AC%CF%81%CF%87%CE%B5%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
    "locale": "el-GR",
    "tags": ["greek-cinema", "konstantaras", "platanitsa", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_190",
    "text": "Τι τύπος οχήματος είναι ο Κεραυνός Μακουίν (Lightning McQueen) στην ταινία της Pixar «Αυτοκίνητα» (Cars, 2006);",
    "answers": ["Πυροσβεστικό όχημα", "Αγωνιστικό αυτοκίνητο", "Φορτηγό ρυμούλκησης", "Αστυνομικό περιπολικό"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Lightning McQueen είναι ένα κόκκινο, φιλόδοξο αγωνιστικό αυτοκίνητο του κυπέλλου Piston Cup με τον αριθμό 95 στις πόρτες του.",
    "funFacts": [
      "Ο αριθμός 95 επιλέχθηκε προς τιμήν του 1995, έτους κυκλοφορίας της πρώτης ταινίας της Pixar, του 'Toy Story'.",
      "Στην ελληνική μεταγλώττιση τη φωνή του Μακουίν δάνεισε ο γνωστός τραγουδιστής Σάκης Ρουβάς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%85%CF%84%CE%BF%CE%BA%CE%AF%CE%BD%CE%B7%CF%84%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["pixar", "cars", "lightning-mcqueen", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_191",
    "text": "Στη σειρά «Εγκλήματα», ποια αφελή και εκκεντρική πρώην ιερόδουλη υποδύθηκε απολαυστικά η Μαρία Καβογιάννη;",
    "answers": ["Φλώρα", "Σωσώ", "Κορίνα Μητροπούλου", "Μάχη"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Κορίνα Μητροπούλου ήταν μια καλόκαρδη αλλά ανίδεη πρώην ιερόδουλη που προσπαθούσε να μπει στην υψηλή κοινωνία και να βρει αληθινή αγάπη.",
    "funFacts": [
      "Ο ρόλος της Κορίνας θεωρείται μία από τις σπουδαιότερες κωμικές ερμηνείες στην ιστορία της ιδιωτικής τηλεόρασης στην Ελλάδα.",
      "Η Μαρία Καβογιάννη κέρδισε τεράστια αναγνώριση και αγάπη από το κοινό μέσα από αυτή τη σειρά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B3%CE%BA%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["greek-tv", "egklimata", "kavogianni", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_192",
    "text": "Ποιος είναι ο πιστός Βρετανός μπάτλερ και πατρική φιγούρα του Μπρους Γουέιν στην έπαυλη των Γουέιν;",
    "answers": ["Επίτροπος Γκόρντον", "Λούσιους Φοξ", "Χάρβεϊ Ντεντ", "Άλφρεντ Πένιγουορθ"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Alfred Pennyworth είναι ο έμπιστος μπάτλερ, πρώην στρατιωτικός και γιατρός που φροντίζει τον Μπάτμαν και περιποιείται τα τραύματά του.",
    "funFacts": [
      "Στην τριλογία του Κρίστοφερ Νόλαν τον Άλφρεντ υποδύθηκε με μοναδικό κύρος ο Μάικλ Κέιν.",
      "Είναι ένας από τους ελάχιστους ανθρώπους στον κόσμο που γνωρίζουν την πραγματική μυστική ταυτότητα του Batman."
    ],
    "source": "https://el.wikipedia.org/wiki/Batman",
    "locale": "el-GR",
    "tags": ["batman", "alfred-pennyworth", "dc-comics", "superheroes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_193",
    "text": "Στην κωμωδία «Πολυτεχνίτης κι ερημοσπίτης» (1963), σε ποιο επάγγελμα ο Θανάσης Βέγγος σαπουνίζει και ξυρίζει πελάτες με καταστροφικά αποτελέσματα;",
    "answers": ["Κουρέας", "Σερβιτόρος", "Διαιτητής", "Φωτογράφος"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Θανάσης Μπιρμπίλης δοκιμάζει διάφορα επαγγέλματα, ανάμεσά τους και βοηθός κουρέα, καταλήγοντας να γεμίσει σαπουνάδες τα πρόσωπα των πελατών.",
    "funFacts": [
      "Η ταινία περιλαμβάνει πέντε διαφορετικά σκετς επαγγελμάτων (σερβιτόρος, κουρέας, διαιτητής, φαρμακοποιός, αστυνομικός).",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο και αποτελεί μία από τις πιο διασκεδαστικές κωμωδίες του ελληνικού σινεμά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB%CF%85%CF%84%CE%B5%CF%87%CE%BD%CE%AF%CF%84%CE%B7%CF%82_%CE%BA%CE%B9_%CE%B5%CF%81%CE%B7%CE%BC%CE%BF%CF%83%CF%80%CE%AF%CF%84%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "thanasis-veggos", "comedy", "sakellarios"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_194",
    "text": "Ποιου γνωστού παραμυθένιου ήρωα η μύτη μακραίνει όταν ανακρίνεται από τον Λόρδο Φάρκουαντ στην ταινία «Shrek» (2001);",
    "answers": ["Του Τζακ", "Του Πινόκιο", "Του Πίτερ Παν", "Του Μπισκοτάκου"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Pinocchio προσπαθεί να πει ψέματα για το πού κρύβεται ο Σρεκ, αλλά η μύτη του αρχίζει να μακραίνει προδίδοντάς τον αμέσως.",
    "funFacts": [
      "Ο Πινόκιο είναι ένας από τους πολλούς κλασικούς παραμυθένιους χαρακτήρες που εξορίστηκαν στον βάλτο του Σρεκ.",
      "Η ταινία της DreamWorks σατίρισε ανοιχτά τα παραδοσιακά κλισέ των ταινιών της Disney."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%81%CE%B5%CE%BA",
    "locale": "el-GR",
    "tags": ["shrek", "pinocchio", "dreamworks", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_195",
    "text": "Στη θρυλική σειρά «Οι Απαράδεκτοι», ποια χαρακτηριστική έκφραση ενθουσιασμού επαναλάμβανε συνεχώς ο Βλάσσης Μπονάτσος;",
    "answers": ["«Έλα ρε φίλε!»", "«Πω πω ζημιά!»", "«Τρομερό! Φοβερό!»", "«Άστο πάνω μου!»"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Βλάσσης Μπονάτσος έμεινε στην τηλεοπτική ιστορία για το πηγαίο κέφι του και τις ατάκες 'Τρομερό!' και 'Φοβερό!' που έλεγε με πάθος.",
    "funFacts": [
      "Ο Βλάσσης υποδυόταν έναν ανέμελο και καλοκάγαθο θεατρίνο που συγκατοικούσε με τον Γιάννη Μπέζο.",
      "Η σειρά των Απαράδεκτων θεωρείται από πολλούς η κορυφαία ελληνική κωμική σειρά όλων των εποχών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%91%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%BA%CF%84%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "aparadektoi", "bonatsos", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_196",
    "text": "Τι πλάσμα είναι ο Μπακμπίκ (Buckbeak) στον «Χάρι Πότερ», με σώμα αλόγου και κεφάλι και φτερά αετού;",
    "answers": ["Κένταυρος", "Γρύπας", "Σφίγγα", "Ιππόγρυπας (Hippogriff)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Buckbeak είναι ένας υπερήφανος Ιππόγρυπας που διδάσκει ο Χάγκριντ στους μαθητές στο μάθημα Φροντίδας Μαγικών Πλασμάτων.",
    "funFacts": [
      "Για να πλησιάσει κανείς έναν Ιππόγρυπα με ασφάλεια, πρέπει πρώτα να υποκλιθεί και να περιμένει να του ανταποδώσει την υπόκλιση.",
      "Στην ταινία 'Ο Αιχμάλωτος του Αζκαμπάν', ο Χάρι και η Ερμιόνη σώζουν τον Μπακμπίκ χρησιμοποιώντας τη Χρονομηχανή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AC%CF%81%CE%B9_%CE%A0%CF%8C%CF%84%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["harry-potter", "buckbeak", "hippogriff", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_197",
    "text": "Στην κωμωδία «Η θεία μου η χίπισσα» (1970), σε ποιον διάσημο προορισμό χίπηδων στην Κρήτη ταξιδεύει η Ρένα Βλαχοπούλου;",
    "answers": ["Στα Μάταλα", "Στο Βάι", "Στη Φαλάσαρνα", "Στο Ελαφονήσι"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ρένα πηγαίνει στα περίφημα Μάταλα της Κρήτης και ντύνεται χίπισσα με πολύχρωμα ρούχα για να εντοπίσει την ανιψιά της.",
    "funFacts": [
      "Τα Μάταλα ήταν πραγματικό παγκόσμιο κέντρο συγκέντρωσης χίπηδων στις φυσικές σπηλιές των βράχων τη δεκαετία του 1960 και 1970.",
      "Η ταινία της Φίνος Φιλμ σημείωσε μεγάλη εισπρακτική επιτυχία με 481.598 εισιτήρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%B8%CE%B5%CE%AF%CE%B1_%CE%BC%CE%BF%CF%85_%CE%B7_%CF%87%CE%AF%CF%80%CE%B9%CF%83%CF%83%CE%B1",
    "locale": "el-GR",
    "tags": ["greek-cinema", "rena-vlachopoulou", "matala", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_198",
    "text": "Ποια είναι η μητέρα του μελλοντικού ηγέτη της ανθρώπινης αντίστασης Τζον Κόνορ στην ταινία «Ο Εξολοθρευτής»;",
    "answers": ["Έλεν Ρίπλεϊ", "Σάρα Κόνορ", "Λόρι Στρόουντ", "Κλάρις Στάρλινγκ"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Sarah Connor (Linda Hamilton) είναι ο πρωταρχικός στόχος του T-800 ώστε να αποτραπεί η γέννηση του γιου της John Connor.",
    "funFacts": [
      "Η μεταμόρφωσή της από ανυποψίαστη σερβιτόρα στην πρώτη ταινία σε σκληροτράχηλη πολεμίστρια στη δεύτερη θεωρείται εμβληματική.",
      "Η Λίντα Χάμιλτον προπονήθηκε εντατικά με πρώην εκπαιδευτή των ισραηλινών ειδικών δυνάμεων για τον ρόλο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%95%CE%BE%CE%BF%CE%BB%CE%BF%CE%B8%CF%81%CE%B5%CF%85%CF%84%CE%AE%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["terminator", "sarah-connor", "sci-fi", "action"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_199",
    "text": "Στη σειρά «Δύο Ξένοι», ποια ποδοσφαιρική ομάδα υποστήριζε με παθολογικό πάθος η εκκεντρική Ντένη Μαρκορά;",
    "answers": ["Ολυμπιακό", "ΑΕΚ", "Παναθηναϊκό", "ΠΑΟΚ"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ντένη Μαρκορά (Ντίνα Κώνστα) ήταν φανατική οπαδός του Παναθηναϊκού, πήγαινε στο γήπεδο της Λεωφόρου και τραγουδούσε συνθήματα.",
    "funFacts": [
      "Οι τηλεφωνικοί διάλογοι ανάμεσα στη Ντένη και τη Μαρούσκα αποτελούν μερικές από τις πιο ξεκαρδιστικές στιγμές της σειράς.",
      "Η ερμηνεία της Ντίνας Κώνστα θεωρείται κορυφαία στην ιστορία των ελληνικών κωμικών σειρών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CF%8D%CE%BF_%CE%9E%CE%AD%CE%BD%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["greek-tv", "dyo-xenoi", "deni-markora", "panathinaikos"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_200",
    "text": "Από ποια οικογένεια άγριων ζώων της ζούγκλας υιοθετείται και μεγαλώνει ο Ταρζάν στην ταινία της Disney (1999);",
    "answers": ["Λεοπαρδάλεις", "Ελέφαντες", "Λιοντάρια", "Γορίλες"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η θηλυκή γορίλας Κάλα (Kala) βρίσκει το ορφανό μωρό στην καλύβα των νεκρών γονιών του και το μεγαλώνει ως δικό της παιδί.",
    "funFacts": [
      "Το τραγούδι 'You'll Be in My Heart' του Φιλ Κόλινς για την ταινία κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού.",
      "Ο Φιλ Κόλινς ηχογράφησε τα τραγούδια της ταινίας όχι μόνο στα αγγλικά, αλλά και στα γαλλικά, γερμανικά, ιταλικά και ισπανικά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CF%81%CE%B6%CE%AC%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1999)",
    "locale": "el-GR",
    "tags": ["disney", "tarzan", "animation", "phil-collins"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_201",
    "text": "Ποιος αγαπημένος ηθοποιός υποδύθηκε τον φτωχό νέο που παριστάνει τον Άραβα πρίγκιπα στην κωμωδία «Ο ξυπόλητος πρίγκηψ» (1966);",
    "answers": ["Κώστας Βουτσάς", "Δημήτρης Παπαμιχαήλ", "Γιώργος Πάντζας", "Αλέκος Αλεξανδράκης"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Κώστας Βουτσάς ενσάρκωσε τον Κώστα που ντύνεται Άραβας εμίρης σε πολυτελές ξενοδοχείο της Ρόδου για να βοηθήσει την αγαπημένη του.",
    "funFacts": [
      "Η ταινία σκηνοθετήθηκε από τον Γιάννη Δαλιανίδη και γυρίστηκε στο ξενοδοχείο 'Miramare' στη Ρόδο.",
      "Έκοψε 615.483 εισιτήρια κατά την πρώτη της κινηματογραφική σεζόν, γνωρίζοντας τεράστια επιτυχία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%BE%CF%85%CF%80%CF%8C%CE%BB%CE%B7%CF%84%CE%BF%CF%82_%CF%80%CF%81%CE%AF%CE%B3%CE%BA%CE%B7%CF%88",
    "locale": "el-GR",
    "tags": ["greek-cinema", "kostas-voutsas", "dalianidis", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_202",
    "text": "Ποια είναι η ανεπίσημη αλλά πασίγνωστη παροιμιώδης φράση της οικογένειας Λάνιστερ στο «Game of Thrones»;",
    "answers": ["«Η φωτιά και το αίμα νικούν»", "«Ένας Λάνιστερ πληρώνει πάντα τα χρέη του»", "«Ο χειμώνας δεν μας τρομάζει»", "«Η ισχύς είναι δικαίωμα»"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η φράση 'A Lannister always pays his debts' («Ένας Λάνιστερ πληρώνει πάντα τα χρέη του») χρησιμοποιείται τόσο ως υπόσχεση ανταμοιβής όσο και ως απειλή εκδίκησης.",
    "funFacts": [
      "Το επίσημο μότο του Οίκου των Λάνιστερ είναι στην πραγματικότητα το 'Hear Me Roar!' ('Άκουσε τη Βοή μου!').",
      "Το οικόσημό τους απεικονίζει ένα χρυσό λιοντάρι σε βαθύ κόκκινο φόντο."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_of_Thrones",
    "locale": "el-GR",
    "tags": ["game-of-thrones", "lannister", "hbo", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_203",
    "text": "Σε ποια μακρινή χώρα ξεκινά η υπόθεση της σειράς «Είσαι το ταίρι μου», πριν οι ηρωίδες επιβιβαστούν στο αεροπλάνο για Ελλάδα;",
    "answers": ["Στον Καναδά", "Στις Ηνωμένες Πολιτείες", "Στην Αυστραλία", "Στη Νότια Αφρική"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Στέλλα και η Βίκυ γνωρίζονται στη Μελβούρνη της Αυστραλίας, όπου αποφασίζουν να αλλάξουν ταυτότητες κατά την πτήση επιστροφής στην Ελλάδα.",
    "funFacts": [
      "Τα πρώτα επεισόδια γυρίστηκαν όντως σε φυσικές τοποθεσίες στη Μελβούρνη.",
      "Η σειρά προβλήθηκε τη σεζόν 2001–2002 από το Mega και θεωρείται μία από τις πιο καλογραμμένες ελληνικές σειρές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%B1%CE%AF%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["greek-tv", "eisai-to-tairi-mou", "australia", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_204",
    "text": "Σε ποια αμερικανική πολιτεία βρισκόταν η φανταστική πόλη Γκρίνμποου όπου μεγάλωσε ο Φόρεστ Γκαμπ;",
    "answers": ["Τέξας", "Φλόριντα", "Τζόρτζια", "Αλαμπάμα"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Forrest Gump μεγάλωσε στο Greenbow της Alabama, όπου φοίτησε αργότερα και στο Πανεπιστήμιο της Αλαμπάμα παίζοντας αμερικανικό ποδόσφαιρο.",
    "funFacts": [
      "Η ταινία απέσπασε 6 βραβεία Όσκαρ το 1995, ανάμεσά τους Καλύτερης Ταινίας και Σκηνοθεσίας (Robert Zemeckis).",
      "Παρότι η πόλη Greenbow είναι φανταστική, τα γυρίσματα πραγματοποιήθηκαν κυρίως στη Νότια Καρολίνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%8C%CF%81%CE%B5%CF%83%CF%84_%CE%93%CE%BA%CE%B1%CE%BC%CF%80",
    "locale": "el-GR",
    "tags": ["forrest-gump", "alabama", "tom-hanks", "oscars"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_205",
    "text": "Ποιος σπουδαίος Έλληνας συνθέτης υπέγραψε τη μουσική και τα τραγούδια σε ιστορικά μιούζικαλ όπως «Κάτι να καίει» και «Γοργόνες και μάγκες»;",
    "answers": ["Μίμης Πλέσσας", "Μάνος Χατζιδάκις", "Μίκης Θεοδωράκης", "Σταύρος Ξαρχάκος"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Μίμης Πλέσσας συνέθεσε μερικές από τις μεγαλύτερες επιτυχίες του ελληνικού σινεμά, συνεργαζόμενος στενά με τον Γιάννη Δαλιανίδη στη Φίνος Φιλμ.",
    "funFacts": [
      "Έγραψε τη μουσική για περισσότερες από 100 κινηματογραφικές ταινίες και τιμήθηκε με πολυάριθμα διεθνή βραβεία.",
      "Εκτός από εξαιρετικός συνθέτης και πιανίστας, κατείχε διδακτορικό δίπλωμα στη Χημεία από το Πανεπιστήμιο Κορνέλ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AF%CE%BC%CE%B7%CF%82_%CE%A0%CE%BB%CE%AD%CF%83%CF%83%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["greek-cinema", "mimis-plessas", "music", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_206",
    "text": "Ποιος είναι ο διαβόητος κυνηγός κεφαλών που φορά πανοπλία των Μανταλοριανών και αιχμαλωτίζει τον Χαν Σόλο στο «Star Wars»;",
    "answers": ["Ντιν Τζάριν", "Μπόμπα Φετ (Boba Fett)", "Τζάνγκο Φετ", "Γκριφ Κάργκα"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Boba Fett είναι ο αμίλητος και επικίνδυνος μισθοφόρος που εντοπίζει το Millennium Falcon για λογαριασμό της Αυτοκρατορίας και του Τζάμπα.",
    "funFacts": [
      "Παρότι είχε μόλις τέσσερα λεπτά εμφάνισης στην αρχική τριλογία, απέκτησε τεράστια βάση φανατικών θαυμαστών.",
      "Η δημοφιλία του οδήγησε στη δημιουργία της δικής του σειράς 'The Book of Boba Fett' στο Disney+."
    ],
    "source": "https://el.wikipedia.org/wiki/Star_Wars",
    "locale": "el-GR",
    "tags": ["star-wars", "boba-fett", "mandalorian", "sci-fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_207",
    "text": "Στη σειρά «Στο Παρά 5», ποια ήταν η κοινωνική και οικονομική κατάσταση της Ντάλιας Χατζηαλεξάνδρου;",
    "answers": ["Άνεργη ηθοποιός", "Δικηγόρος εταιρείας", "Πάμπλουτη κληρονόμος τεράστιας περιουσίας", "Δημοσιογράφος καναλιού"],
    "correctAnswerIndex": 2,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Η Ντάλια ήταν η πλουσιότερη γυναίκα στην Ελλάδα, κληρονόμος μιας αμύθητης περιουσίας και δεκάδων επιχειρήσεων που διοικούσε χωρίς να έχει επαφή με τον έξω κόσμο.",
    "funFacts": [
      "Ζούσε κλεισμένη σε μια τεράστια έπαυλη περιτριγυρισμένη από σωματοφύλακες μέχρι να γνωρίσει τους άλλους τέσσερις της παρέας.",
      "Χαρακτηριστική ήταν η αδυναμία της να κατανοήσει μικρά χρηματικά ποσά, νομίζοντας ότι όλα κοστίζουν εκατομμύρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["greek-tv", "sto-para-5", "dalia", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_208",
    "text": "Ποιο είναι το όνομα του βασιλικού σπαθιού του Άραγκορν στον «Άρχοντα των Δαχτυλιδιών», που επανασυγκολλήθηκε από τα θραύσματα του Νάρσιλ;",
    "answers": ["Στινγκ", "Γκλάμντρινγκ", "Γκράμντριλ", "Άντουριλ (Andúril)"],
    "correctAnswerIndex": 3,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Το Andúril ('Φλόγα της Δύσης') είναι το θρυλικό σπαθί των βασιλιάδων της Γκόντορ, με το οποίο ο Άραγκορν διεκδικεί τον θρόνο του.",
    "funFacts": [
      "Τα ξωτικά του Σχιστού Λαγκαδιού (Rivendell) σφυρηλάτησαν ξανά το σπαθί χαράσσοντας μαγικά ρούνικα σύμβολα πάνω στη λεπίδα του.",
      "Με αυτό το σπαθί ο Άραγκορν καλεί τον Στρατό των Νεκρών να εκπληρώσει τον όρκο του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CF%81%CE%B1%CE%B3%CE%BA%CE%BF%CF%81%CE%BD",
    "locale": "el-GR",
    "tags": ["lord-of-the-rings", "aragorn", "anduril", "fantasy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_209",
    "text": "Στην κωμωδία «Η Αλίκη στο ναυτικό» (1961), ποιος πρωταγωνιστής υποδύθηκε τον δόκιμο αξιωματικό Κώστα που ερωτεύεται η Αλίκη;",
    "answers": ["Δημήτρης Παπαμιχαήλ", "Αλέκος Αλεξανδράκης", "Ανδρέας Μπάρκουλης", "Κώστας Βουτσάς"],
    "correctAnswerIndex": 0,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Δημήτρης Παπαμιχαήλ υποδύθηκε τον δόκιμο Κώστα Δέγλερη, ο οποίος γνωρίζει την Αλίκη στον Πόρο και αργότερα την κρύβει στο πολεμικό πλοίο.",
    "funFacts": [
      "Η ταινία περιλαμβάνει τη σκηνή παρέλασης της Σχολής Ναυτικών Δοκίμων στον Πειραιά.",
      "Σκηνοθετήθηκε από τον Αλέκο Σακελλάριο και απέσπασε τεράστια εμπορική επιτυχία με πάνω από 213.000 εισιτήρια στην Αθήνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%97_%CE%91%CE%BB%CE%AF%CE%BA%CE%B7_%CF%83%CF%84%CE%BF_%CE%BD%CE%B1%CF%85%CF%84%CE%B9%CE%BA%CF%8C",
    "locale": "el-GR",
    "tags": ["greek-cinema", "papamichail", "aliki-vougiouklaki", "finos-film"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "cinema_tv_easy_210",
    "text": "Τι είδους μικρό ζώο είναι ο Τιμόν, ο αστείος και υπερκινητικός κολλητός του Πούμπα στον «Βασιλιά των Λιονταριών»;",
    "answers": ["Λεμούριος", "Μίρκατ (σουρικάτα)", "Σκίουρος", "Ασβός"],
    "correctAnswerIndex": 1,
    "categoryId": "cinema_tv",
    "difficulty": 1,
    "explanation": "Ο Timon είναι ένα μίρκατ (meerkat / σουρικάτα) που ζει στην αφρικανική σαβάνα και τρέφεται με ζουμερά σκουλήκια και έντομα.",
    "funFacts": [
      "Στην αγγλική εκδοχή τη φωνή του Τιμόν δάνεισε ο θεατρικός και κινηματογραφικός ηθοποιός Nathan Lane.",
      "Το δίδυμο Τιμόν και Πούμπα αγαπήθηκε τόσο πολύ που απέκτησε τη δική του τηλεοπτική σειρά κινουμένων σχεδίων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%B9%CE%AC%CF%82_%CF%84%CF%89%CE%BD_%CE%9B%CE%B9%CE%BF%CE%BD%CF%84%CE%B1%CF%81%CE%B9%CF%8E%CE%BD_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1994)",
    "locale": "el-GR",
    "tags": ["disney", "the-lion-king", "timon", "animation"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('cinema_tv', 'easy', 1, questions)

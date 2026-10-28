# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "technology_easy_111",
    "text": "Ποιος εφευρέτης κατοχύρωσε το πρώτο λειτουργικό δίπλωμα ευρεσιτεχνίας για το ηλεκτρικό τηλέφωνο το 1876;",
    "answers": ["Αλεξάντερ Γκράχαμ Μπελ", "Τόμας Έντισον", "Νίκολα Τέσλα", "Γουλιέλμο Μαρκόνι"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Αλεξάντερ Γκράχαμ Μπελ κατοχύρωσε το δίπλωμα ευρεσιτεχνίας για το τηλέφωνο στις ΗΠΑ τον Μάρτιο του 1876.",
    "funFacts": [
      "Οι πρώτες καταγεγραμμένες λέξεις που μεταδόθηκαν μέσω τηλεφώνου ήταν: 'Κύριε Γουάτσον, ελάτε εδώ, σας χρειάζομαι'.",
      "Ο Μπελ αρνήθηκε να έχει τηλέφωνο στο γραφείο μελέτης του επειδή θεωρούσε ότι διέκοπτε την επιστημονική του συγκέντρωση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B5%CE%BE%CE%AC%CE%BD%CF%84%CE%B5%CF%81_%CE%93%CE%BA%CF%81%CE%AC%CF%87%CE%B1%CE%BC_%CE%9C%CF%80%CE%B5%CE%BB",
    "locale": "el-GR",
    "tags": ["bell", "telephone", "inventions", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_112",
    "text": "Ποιος Αμερικανός εφευρέτης ίδρυσε την General Electric και επινόησε τον φωνόγραφο και τον πρακτικό ηλεκτρικό λαμπτήρα πυρακτώσεως;",
    "answers": ["Χένρι Φορντ", "Τόμας Έντισον", "Τζορτζ Γουέστινγκχαους", "Τζ. Π. Μόργκαν"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Τόμας Έντισον κατέγραψε 1.093 αμερικανικά διπλώματα ευρεσιτεχνίας και δημιούργησε το πρώτο βιομηχανικό ερευνητικό εργαστήριο στο Μένλο Παρκ.",
    "funFacts": [
      "Ο πρώτος πρακτικός λαμπτήρας του το 1879 χρησιμοποιούσε νήμα από απανθρακωμένο μπαμπού που μπορούσε να φωτίζει για πάνω από 1.200 ώρες.",
      "Ο φωνόγραφος, που κατέγραφε και αναπαρήγαγε ήχο σε κυλίνδρους κασσίτερου, ήταν η αγαπημένη του προσωπική εφεύρεση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%8C%CE%BC%CE%B1%CF%82_%CE%88%CE%BD%CF%84%CE%B9%CF%83%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["edison", "inventions", "electricity", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_113",
    "text": "Ποιος Ιταλός εφευρέτης και νομπελίστας θεωρείται ο «πατέρας της ασύρματης τηλεγραφίας» και του ραδιοφώνου;",
    "answers": ["Αλεσάντρο Βόλτα", "Ενρίκο Φέρμι", "Γουλιέλμο Μαρκόνι", "Γαλιλαίος Γαλιλέι"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Γουλιέλμο Μαρκόνι πέτυχε την πρώτη ασύρματη ραδιοφωνική μετάδοση πάνω από τον Ατλαντικό Ωκεανό τον Δεκέμβριο του 1901.",
    "funFacts": [
      "Βραβεύτηκε με το Νόμπελ Φυσικής το 1909 από κοινού με τον Καρλ Φέρντιναντ Μπράουν για τη συμβολή τους στην ασύρματη τηλεγραφία.",
      "Η ασύρματη συσκευή τηλεγράφου του Μαρκόνι πάνω στον Τιτανικό το 1912 βοήθησε να σωθούν πάνω από 700 επιζώντες του ναυαγίου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%85%CE%BB%CE%B9%CE%AD%CE%BB%CE%BC%CE%BF_%CE%9C%CE%B1%CF%81%CE%BA%CF%8C%CE%BD%CE%B9",
    "locale": "el-GR",
    "tags": ["marconi", "radio", "telecommunications", "inventions"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_114",
    "text": "Ποιος ιδιοφυής Σέρβος μηχανικός και εφευρέτης ανέπτυξε το σύστημα εναλλασσόμενου ρεύματος (AC) και τον επαγωγικό ηλεκτροκινητήρα;",
    "answers": ["Μάικλ Φαραντέι", "Τζέιμς Βατ", "Τόμας Έντισον", "Νίκολα Τέσλα"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Νίκολα Τέσλα κατοχύρωσε θεμελιώδη διπλώματα ευρεσιτεχνίας για την παραγωγή και διανομή πολυφασικού εναλλασσόμενου ρεύματος.",
    "funFacts": [
      "Η περίφημη διαμάχη του με τον Τόμας Έντισον για την επικράτηση του εναλλασσόμενου έναντι του συνεχούς ρεύματος έμεινε στην ιστορία ως ο 'Πόλεμος των Ρευμάτων'.",
      "Η μονάδα μέτρησης της πυκνότητας μαγνητικής ροής στο Διεθνές Σύστημα Μονάδων (SI) ονομάστηκε Tesla (T) προς τιμήν του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%BF%CE%BB%CE%B1_%CE%A4%CE%AD%CF%83%CE%BB%CE%B1",
    "locale": "el-GR",
    "tags": ["tesla", "electricity", "inventions", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_115",
    "text": "Ποιος εφευρέτης δημιούργησε το σύστημα κωδικοποίησης χαρακτήρων με τελείες και παύλες για τις ανάγκες του ηλεκτρικού τηλέγραφου;",
    "answers": ["Σάμιουελ Μορς", "Τζον Αμπρόουζ Φλέμινγκ", "Γουίλιαμ Σόκλεϊ", "Αλεξάντερ Ποπόφ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Σάμιουελ Μορς (Samuel Morse) ανέπτυξε τον Κώδικα Μορς τη δεκαετία του 1830, επιτρέποντας τη στιγμιαία μετάδοση μηνυμάτων μέσω καλωδίων.",
    "funFacts": [
      "Το πρώτο επίσημο τηλεγράφημα που στάλθηκε από την Ουάσινγκτον στη Βαλτιμόρη το 1844 περιείχε τη φράση: 'What hath God wrought' (Τι δημιούργησε ο Θεός).",
      "Το διεθνές σήμα κινδύνου SOS στον κώδικα Μορς αποτελείται από τρεις τελείες, τρεις παύλες και τρεις τελείες (... --- ...)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%AC%CE%BC%CE%B9%CE%BF%CF%85%CE%B5%CE%BB_%CE%9C%CE%BF%CF%81%CF%82",
    "locale": "el-GR",
    "tags": ["morse", "morse-code", "telegraph", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_116",
    "text": "Ποιος Βρετανός μαθηματικός του 19ου αιώνα θεωρείται «πατέρας του μηχανικού υπολογιστή» σχεδιάζοντας τη Διαφορική και την Αναλυτική Μηχανή;",
    "answers": ["Άλαν Τιούρινγκ", "Τσαρλς Μπάμπατζ", "Τζον φον Νόιμαν", "Τζορτζ Μπουλ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Τσαρλς Μπάμπατζ (Charles Babbage) σχεδίασε την Αναλυτική Μηχανή, την πρώτη μηχανική διάταξη που περιείχε όλα τα θεμελιώδη στοιχεία ενός σύγχρονου υπολογιστή.",
    "funFacts": [
      "Η Αναλυτική Μηχανή του χρησιμοποιούσε διάτρητες κάρτες για την εισαγωγή προγραμμάτων και δεδομένων, εμπνευσμένη από τον αργαλειό του Ζακάρ.",
      "Παρόλο που δεν ολοκληρώθηκε πλήρως όσο ζούσε λόγω έλλειψης ακριβών μηχανικών εξαρτημάτων, το Μουσείο Επιστημών του Λονδίνου κατασκεύασε ένα λειτουργικό μοντέλο της το 1991."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%83%CE%B1%CF%81%CE%BB%CF%82_%CE%9C%CF%80%CE%AC%CE%BC%CF%80%CE%B1%CF%84%CE%B6",
    "locale": "el-GR",
    "tags": ["babbage", "computers", "history", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_117",
    "text": "Ποιος Γερμανός εφευρέτης εισήγαγε την τυπογραφία με κινητά μεταλλικά στοιχεία στην Ευρώπη γύρω στο 1440 αλλάζοντας τη διάδοση της γνώσης;",
    "answers": ["Μαρτίνος Λούθηρος", "Άλμπρεχτ Ντύρερ", "Ιωάννης Γουτεμβέργιος", "Γιοχάνες Κέπλερ"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Ιωάννης Γουτεμβέργιος (Johannes Gutenberg) επινόησε ένα ανθεκτικό κράμα μολύβδου-κασσίτερου για κινητά τυπογραφικά στοιχεία και μια ειδική ελαιώδη τυπογραφική μελάνη.",
    "funFacts": [
      "Το διασημότερο έργο του ήταν η «Βίβλος του Γουτεμβέργιου», που τυπώθηκε γύρω στο 1455 σε περίπου 180 αντίτυπα.",
      "Η εφεύρεση της τυπογραφίας θεωρείται από πολλούς ιστορικούς το σημαντικότερο τεχνολογικό γεγονός της δεύτερης χιλιετίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%93%CE%BF%CF%85%CF%84%CE%B5%CE%BC%CE%B2%CE%AD%CF%81%CE%B3%CE%B9%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["gutenberg", "printing", "inventions", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_118",
    "text": "Ποιος Σκωτσέζος μηχανικός παρουσίασε την πρώτη λειτουργική ηλεκτρομηχανική τηλεόραση στον κόσμο τη δεκαετία του 1920;",
    "answers": ["Τζέιμς Κλερκ Μάξγουελ", "Τζέιμς Βατ", "Αλεξάντερ Φλέμινγκ", "Τζον Λόγκι Μπερντ"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Τζον Λόγκι Μπερντ (John Logie Baird) παρουσίασε δημόσια στο Λονδίνο το 1926 την πρώτη επιτυχημένη μετάδοση κινούμενης εικόνας μέσω ηλεκτρομηχανικού συστήματος.",
    "funFacts": [
      "Για να κατασκευάσει την πρώτη πειραματική του συσκευή χρησιμοποίησε ένα κουτί καπέλων, βελόνες πλεξίματος, φακούς ποδηλάτου και κερί σφράγισης.",
      "Πραγματοποίησε επίσης την πρώτη υπερατλαντική τηλεοπτική μετάδοση μεταξύ Λονδίνου και Νέας Υόρκης το 1928."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%9B%CF%8C%CE%B3%CE%BA%CE%B9_%CE%9C%CF%80%CE%B5%CF%81%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["baird", "television", "inventions", "broadcasting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_119",
    "text": "Ποιοι δύο αδελφοί πραγματοποίησαν την πρώτη ελεγχόμενη πτήση με μηχανοκίνητο αεροπλάνο το 1903 στο Κίτι Χοκ της Βόρειας Καρολίνας;",
    "answers": ["Αδελφοί Ράιτ", "Αδελφοί Μονγκολφιέ", "Αδελφοί Λυμιέρ", "Αδελφοί Ντάσλερ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Όρβιλ και ο Γουίλμπουρ Ράιτ πέτυχαν την πρώτη επιτυχημένη πτήση με το διπλάνο 'Wright Flyer' στις 17 Δεκεμβρίου 1903.",
    "funFacts": [
      "Η ιστορική πρώτη πτήση του Όρβιλ Ράιτ διήρκεσε μόλις 12 δευτερόλεπτα και κάλυψε απόσταση περίπου 36,5 μέτρων.",
      "Πριν ασχοληθούν με την αεροπορία, οι αδελφοί Ράιτ διατηρούσαν επιτυχημένο κατάστημα κατασκευής και επισκευής ποδηλάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%B4%CE%B5%CE%BB%CF%86%CE%BF%CE%AF_%CE%A1%CE%AC%CE%B9%CF%84",
    "locale": "el-GR",
    "tags": ["wright-brothers", "aviation", "inventions", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_120",
    "text": "Ποιος βιομήχανος αυτοκινήτων τελειοποίησε την κινούμενη γραμμή συναρμολόγησης, κάνοντας τα αυτοκίνητα προσιτά στη μάζα με το μοντέλο Ford Model T;",
    "answers": ["Έντσο Φεράρι", "Χένρι Φορντ", "Καρλ Μπεντς", "Φέρντιναντ Πόρσε"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Χένρι Φορντ εισήγαγε την κινούμενη αλυσίδα παραγωγής στο εργοστάσιο Highland Park το 1913 μειώνοντας δραστικά τον χρόνο και το κόστος κατασκευής.",
    "funFacts": [
      "Χάρη στη γραμμή παραγωγής, ο χρόνος κατασκευής ενός Ford Model T μειώθηκε από 12 ώρες σε μόλις 93 λεπτά.",
      "Διπλασίασε τον ημερήσιο μισθό των εργατών του στα 5 δολάρια την ημέρα ώστε να μπορούν και οι ίδιοι να αγοράσουν τα αυτοκίνητα που κατασκεύαζαν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%AD%CE%BD%CF%81%CE%B9_%CE%A6%CE%BF%CF%81%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["henry-ford", "automotive", "manufacturing", "industry"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_121",
    "text": "Ποιες δύο εταιρείες ηλεκτρονικών κολοσσοί συνεργάστηκαν στα τέλη της δεκαετίας του 1970 για να αναπτύξουν το πρότυπο του ψηφιακού οπτικού δίσκου CD;",
    "answers": ["Apple και IBM", "Panasonic και Toshiba", "Philips και Sony", "Microsoft και Intel"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η ολλανδική Philips και η ιαπωνική Sony ένωσαν τις δυνάμεις τους το 1979 για να καθιερώσουν το παγκόσμιο πρότυπο Compact Disc (CD-DA).",
    "funFacts": [
      "Η διάμετρος του CD (12 εκατοστά) και η μέγιστη χωρητικότητα των 74 λεπτών μουσικής ορίστηκαν ώστε να χωρά ολόκληρη η 9η Συμφωνία του Μπετόβεν.",
      "Το πρώτο εμπορικό μουσικό CD που κυκλοφόρησε στην αγορά το 1982 ήταν το άλμπουμ '52nd Street' του Μπίλι Τζόελ."
    ],
    "source": "https://el.wikipedia.org/wiki/Compact_Disc",
    "locale": "el-GR",
    "tags": ["cd", "philips", "sony", "audio", "storage"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_122",
    "text": "Ποια είναι η τυπική χωρητικότητα αποθήκευσης ενός απλού οπτικού δίσκου DVD μονής όψης και μονής στρώσης;",
    "answers": ["700 MB", "1,44 MB", "25 GB", "4,7 GB"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ένας τυπικός δίσκος DVD (DVD-5) μονής στρώσης έχει χωρητικότητα 4,7 Gigabytes, επιτρέποντας την εγγραφή ταινιών σε ποιότητα SD.",
    "funFacts": [
      "Τα αρχικά DVD αρχικά σήμαιναν 'Digital Video Disc', αλλά αργότερα επικράτησε η ονομασία 'Digital Versatile Disc' λόγω της πολλαπλής χρήσης του για δεδομένα.",
      "Η χωρητικότητα ενός DVD είναι σχεδόν 7 φορές μεγαλύτερη από εκείνη ενός απλού CD (700 MB)."
    ],
    "source": "https://el.wikipedia.org/wiki/DVD",
    "locale": "el-GR",
    "tags": ["dvd", "optical-disc", "storage", "video"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_123",
    "text": "Τι χρώματος λέιζερ χρησιμοποιούν οι συσκευές ανάγνωσης δίσκων Blu-ray Disc για την εγγραφή και ανάγνωση δεδομένων υψηλής πυκνότητας;",
    "answers": ["Μπλε - ιώδες λέιζερ", "Κόκκινο λέιζερ", "Πράσινο λέιζερ", "Κίτρινο λέιζερ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Blu-ray Disc πήρε το όνομά του από το μπλε-ιώδες λέιζερ (μήκους κύματος 405 nm), το οποίο έχει μικρότερο μήκος κύματος από το κόκκινο λέιζερ των DVD (650 nm).",
    "funFacts": [
      "Το μικρότερο μήκος κύματος του μπλε λέιζερ επιτρέπει την εστίαση σε πολύ μικρότερα σημεία, εκτοξεύοντας τη χωρητικότητα στα 25 GB ανά στρώση.",
      "Το γράμμα 'e' παραλείφθηκε σκόπιμα από τη λέξη 'Blue' (Blu-ray) ώστε το όνομα να μπορεί να κατοχυρωθεί νόμιμα ως εμπορικό σήμα."
    ],
    "source": "https://el.wikipedia.org/wiki/Blu-ray_Disc",
    "locale": "el-GR",
    "tags": ["bluray", "optical-disc", "lasers", "storage"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_124",
    "text": "Ποια χώρα ανέπτυξε αρχικά και διαχειρίζεται το παγκόσμιο δορυφορικό σύστημα εντοπισμού θέσης GPS;",
    "answers": ["Ηνωμένο Βασίλειο", "Ηνωμένες Πολιτείες Αμερικής", "Ρωσία", "Κίνα"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το σύστημα GPS (NAVSTAR GPS) αναπτύχθηκε από το Υπουργείο Άμυνας των ΗΠΑ τη δεκαετία του 1970 και τέθηκε σε πλήρη λειτουργία το 1995.",
    "funFacts": [
      "Ο πρόεδρος Ρόναλντ Ρήγκαν εξέδωσε οδηγία το 1983 για τη δωρεάν διάθεση του συστήματος στην πολιτική αεροπορία και το ευρύ κοινό μετά την κατάρριψη της πτήσης KAL 007.",
      "Οι δορυφόροι GPS ενσωματώνουν ατομικά ρολόγια καισίου και ρουβιδίου με εξαιρετική ακρίβεια νανοδευτερολέπτου."
    ],
    "source": "https://el.wikipedia.org/wiki/GPS",
    "locale": "el-GR",
    "tags": ["gps", "usa", "navigation", "satellites"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_125",
    "text": "Πώς ονομάζεται το ευρωπαϊκό δορυφορικό σύστημα πλοήγησης που αναπτύχθηκε από την Ευρωπαϊκή Ένωση ως ανεξάρτητο αντίστοιχο του GPS;",
    "answers": ["Copernicus", "Sputnik", "Galileo", "Hubble"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το σύστημα Galileo είναι το πολιτικό δορυφορικό σύστημα πλοήγησης της Ευρωπαϊκής Ένωσης, παρέχοντας εξαιρετικά υψηλή ακρίβεια θέσης.",
    "funFacts": [
      "Πήρε το όνομά του από τον διάσημο Ιταλό αστρονόμο και φυσικό Γαλιλαίο Γαλιλέι.",
      "Σε αντίθεση με το αμερικανικό GPS και το ρωσικό GLONASS, το ευρωπαϊκό Galileo δημιουργήθηκε και διοικείται από πολιτική και όχι στρατιωτική αρχή."
    ],
    "source": "https://el.wikipedia.org/wiki/Galileo_(%CE%B4%CE%BF%CF%81%CF%85%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CF%8C_%CF%83%CF%8D%CF%83%CF%84%CE%B7%CE%BC%CE%B1_%CF%80%CE%BB%CE%BF%CE%AE%CE%B3%CE%B7%CF%83%CE%B7%CF%82)",
    "locale": "el-GR",
    "tags": ["galileo", "navigation", "satellites", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_126",
    "text": "Ποια χώρα δημιούργησε και συντηρεί το παγκόσμιο δορυφορικό σύστημα πλοήγησης GLONASS;",
    "answers": ["Ιαπωνία", "Γαλλία", "Ινδία", "Ρωσία"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το GLONASS ξεκίνησε να αναπτύσσεται από τη Σοβιετική Ένωση το 1976 και ολοκληρώθηκε υπό τη διαχείριση της Ρωσικής Ομοσπονδίας.",
    "funFacts": [
      "Τα αρχικά GLONASS σημαίνουν 'Globalnaya Navigatsionnaya Sputnikovaya Sistema' (Παγκόσμιο Δορυφορικό Σύστημα Πλοήγησης).",
      "Τα περισσότερα σύγχρονα smartphones συνδυάζουν σήματα από GPS, Galileo και GLONASS ταυτόχρονα για ταχύτερο κλείδωμα θέσης."
    ],
    "source": "https://el.wikipedia.org/wiki/GLONASS",
    "locale": "el-GR",
    "tags": ["glonass", "russia", "navigation", "satellites"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_127",
    "text": "Ποια μορφή αρχείων εικόνας, που πρωτοεμφανίστηκε το 1987, έγινε εξαιρετικά δημοφιλής στο διαδίκτυο για σύντομες κινούμενες λούπες εικόνων;",
    "answers": ["GIF", "BMP", "TIFF", "RAW"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το GIF (Graphics Interchange Format) υποστηρίζει έως 256 χρώματα και επιτρέπει την αναπαραγωγή διαδοχικών καρέ σε επαναλαμβανόμενο κύκλο (loop).",
    "funFacts": [
      "Δημιουργήθηκε από τον επιστήμονα Στιβ Γουίλχαϊτ στην εταιρεία CompuServe τον Ιούνιο του 1987.",
      "Υπάρχει μακροχρόνια χιουμοριστική διαφωνία για την προφορά του ονόματος, με τον δημιουργό του να δηλώνει ότι προφέρεται 'τζιφ' (Jif)."
    ],
    "source": "https://el.wikipedia.org/wiki/GIF",
    "locale": "el-GR",
    "tags": ["gif", "images", "formats", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_128",
    "text": "Ποια συμπιεσμένη μορφή αρχείων εικόνας είναι η πλέον διαδεδομένη παγκοσμίως για ψηφιακές φωτογραφίες σε κάμερες και διαδίκτυο;",
    "answers": ["SVG", "JPEG", "PSD", "ICO"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρότυπο JPEG (Joint Photographic Experts Group) χρησιμοποιεί αλγόριθμο απωλεστικής συμπίεσης ειδικά βελτιστοποιημένο για ρεαλιστικές φωτογραφίες.",
    "funFacts": [
      "Καθιερώθηκε επίσημα το 1992 και υποστηρίζει βάθος χρώματος 24-bit (16,7 εκατομμύρια διαφορετικά χρώματα).",
      "Επιτρέπει τη μείωση του μεγέθους ενός φωτογραφικού αρχείου έως και κατά 90% χωρίς εμφανή υποβάθμιση για το ανθρώπινο μάτι."
    ],
    "source": "https://el.wikipedia.org/wiki/JPEG",
    "locale": "el-GR",
    "tags": ["jpeg", "photography", "images", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_129",
    "text": "Ποιο κύριο πλεονέκτημα προσφέρει η μορφή εικόνας PNG έναντι του κλασικού JPEG για γραφικά ιστοσελίδων και λογότυπα;",
    "answers": ["Μικρότερο μέγεθος για βίντεο", "Υποστήριξη κινούμενου ήχου", "Υποστήριξη διαφανούς φόντου (transparency)", "Δυνατότητα εκτύπωσης 3D"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το PNG (Portable Network Graphics) υποστηρίζει κανάλι άλφα (alpha channel), επιτρέποντας διαβαθμισμένη διαφάνεια στο φόντο των γραφικών.",
    "funFacts": [
      "Δημιουργήθηκε το 1995 ως δωρεάν εναλλακτική λύση ανοιχτού κώδικα απέναντι στο GIF, το οποίο τότε προστατευόταν από πατέντες συμπίεσης.",
      "Χρησιμοποιεί μη απωλεστική συμπίεση (lossless), διατηρώντας ακέραιη την αρχική ποιότητα της εικόνας κατά την αποθήκευση."
    ],
    "source": "https://el.wikipedia.org/wiki/PNG",
    "locale": "el-GR",
    "tags": ["png", "images", "formats", "design"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_130",
    "text": "Πώς ονομάζεται η δημοφιλής μορφή αρχειοθέτησης που συμπιέζει ένα ή περισσότερα αρχεία σε ένα ενιαίο αρχείο με κατάληξη .zip;",
    "answers": ["EXE", "ISO", "PDF", "ZIP"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο μορφότυπος ZIP συμπιέζει δεδομένα χωρίς απώλειες και ομαδοποιεί πολλά αρχεία και φακέλους σε ένα ενιαίο πακέτο.",
    "funFacts": [
      "Δημιουργήθηκε το 1989 από τον Αμερικανό προγραμματιστή Φιλ Κατς για το πρόγραμμα PKZIP.",
      "Όλα τα σύγχρονα λειτουργικά συστήματα (Windows, macOS, Linux) έχουν ενσωματωμένη εγγενή υποστήριξη για άνοιγμα και δημιουργία αρχείων ZIP χωρίς εξωτερικά εργαλεία."
    ],
    "source": "https://el.wikipedia.org/wiki/ZIP_(%CE%BC%CE%BF%CF%81%CF%86%CE%AE_%CE%B1%CF%81%CF%87%CE%B5%CE%AF%CE%BF%CF%85)",
    "locale": "el-GR",
    "tags": ["zip", "compression", "files", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_131",
    "text": "Πώς ονομάζεται το αποκλειστικό λειτουργικό σύστημα που τροφοδοτεί όλα τα κινητά τηλέφωνα iPhone της Apple;",
    "answers": ["iOS", "Android", "Symbian", "Windows Mobile"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το iOS είναι το ιδιόκτητο λειτουργικό σύστημα κινητών συσκευών της Apple, που παρουσιάστηκε για πρώτη φορά το 2007 μαζί με το πρώτο iPhone.",
    "funFacts": [
      "Αρχικά ονομαζόταν απλώς 'iPhone OS' πριν μετονομαστεί επίσημα σε iOS το 2010.",
      "Βασίζεται στον πυρήνα Darwin και μοιράζεται πολλά κοινά αρχιτεκτονικά στοιχεία με το λειτουργικό σύστημα macOS των υπολογιστών Mac."
    ],
    "source": "https://el.wikipedia.org/wiki/IOS",
    "locale": "el-GR",
    "tags": ["ios", "apple", "smartphones", "operating-systems"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_132",
    "text": "Ποια κατηγορία φορητών συσκευών αφής καθιέρωσε μαζικά στην παγκόσμια αγορά η Apple το 2010 με την παρουσίαση του iPad;",
    "answers": ["Smartwatch", "Tablet (Ταμπλέτα)", "Netbook", "E-reader"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Στιβ Τζομπς παρουσίασε το iPad τον Ιανουάριο του 2010, γεφυρώνοντας το κενό μεταξύ smartphone και φορητού υπολογιστή.",
    "funFacts": [
      "Η Apple πούλησε πάνω από 300.000 iPad την πρώτη κιόλας ημέρα κυκλοφορίας του στα καταστήματα.",
      "Αν και η ιδέα του tablet υπήρχε από χρόνια, το iPad ήταν το πρώτο που πέτυχε μαζική εμπορική επιτυχία χάρη στη βελτιστοποιημένη οθόνη αφής πολλαπλών σημείων."
    ],
    "source": "https://el.wikipedia.org/wiki/IPad",
    "locale": "el-GR",
    "tags": ["ipad", "apple", "tablets", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_133",
    "text": "Πώς ονομάζεται μια σύγχρονη οικιακή τηλεόραση που διαθέτει ενσωματωμένη σύνδεση στο διαδίκτυο και δυνατότητα εκτέλεσης εφαρμογών;",
    "answers": ["CRT TV", "Αναλογική TV", "Smart TV", "Plasma TV"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Μια Smart TV (έξυπνη τηλεόραση) ενσωματώνει λειτουργικό σύστημα και επεξεργαστή επιτρέποντας την προβολή online streaming περιεχομένου, περιήγηση στον ιστό και εγκατάσταση εφαρμογών.",
    "funFacts": [
      "Τα περισσότερα μοντέλα χρησιμοποιούν εξειδικευμένα λειτουργικά συστήματα όπως Google TV/Android TV, webOS (LG) ή Tizen (Samsung).",
      "Επιτρέπουν τη λειτουργία 'Screen Mirroring' (όπως Miracast ή AirPlay) για την ασύρματη προβολή της οθόνης του κινητού στην τηλεόραση."
    ],
    "source": "https://el.wikipedia.org/wiki/Smart_TV",
    "locale": "el-GR",
    "tags": ["smart-tv", "television", "streaming", "appliances"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_134",
    "text": "Ποια πρωτοπόρος αμερικανική εταιρεία βιντεοπαιχνιδιών ιδρύθηκε το 1972 από τον Νόλαν Μπούσνελ και δημιούργησε το ιστορικό παιχνίδι Pong;",
    "answers": ["Nintendo", "Sega", "Activision", "Atari"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Atari έπαιξε καθοριστικό ρόλο στη δημιουργία της βιομηχανίας ηλεκτρονικών παιχνιδιών με την κυκλοφορία του Pong και της κονσόλας Atari 2600.",
    "funFacts": [
      "Ο συνιδρυτής της Apple Στιβ Τζομπς και ο Στιβ Βόζνιακ εργάστηκαν στην Atari στις αρχές της δεκαετίας του 1970 σχεδιάζοντας το παιχνίδι Breakout.",
      "Το όνομα 'Atari' προέρχεται από έναν όρο του παραδοσιακού ιαπωνικού επιτραπέζιου παιχνιδιού Go, παρόμοιο με το 'ρουά' στο σκάκι."
    ],
    "source": "https://el.wikipedia.org/wiki/Atari",
    "locale": "el-GR",
    "tags": ["atari", "gaming", "pong", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_135",
    "text": "Ποιος θρυλικός Ιάπωνας σχεδιαστής βιντεοπαιχνιδιών της Nintendo δημιούργησε εμβληματικούς χαρακτήρες όπως ο Mario, ο Donkey Kong και ο Link;",
    "answers": ["Σιγκέρου Μιγιαμότο", "Χιντέο Κοτζίμα", "Σατόρου Ιβάτα", "Μασαχίρο Σακουράι"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Σιγκέρου Μιγιαμότο (Shigeru Miyamoto) θεωρείται ευρέως ο πιο επιδραστικός δημιουργός στην ιστορία των ηλεκτρονικών παιχνιδιών.",
    "funFacts": [
      "Αρχικά είχε προσληφθεί στη Nintendo ως καλλιτέχνης σχεδιασμού παιχνιδιών και όχι ως προγραμματιστής.",
      "Ο χαρακτήρας Mario ονομαζόταν αρχικά 'Jumpman' στο πρώτο παιχνίδι Donkey Kong του 1981."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B9%CE%B3%CE%BA%CE%AD%CF%81%CE%BF%CF%85_%CE%9C%CE%B9%CE%B3%CE%B9%CE%B1%CE%BC%CF%8C%CF%84%CE%BF",
    "locale": "el-GR",
    "tags": ["miyamoto", "nintendo", "mario", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_136",
    "text": "Ποια φορητή κονσόλα βιντεοπαιχνιδιών με ασπρόμαυρη οθόνη υγρών κρυστάλλων κυκλοφόρησε η Nintendo το 1989 και σημείωσε σαρωτική επιτυχία;",
    "answers": ["Game Gear", "Game Boy", "PSP", "Atari Lynx"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Game Boy σχεδιάστηκε από τον Γκούνπεϊ Γιοκόι και την ομάδα Nintendo R&D1 και πούλησε πάνω από 118 εκατομμύρια τεμάχια παγκοσμίως (μαζί με το Game Boy Color).",
    "funFacts": [
      "Η τεράστια επιτυχία του οφειλόταν σε μεγάλο βαθμό στη συμπερίληψη του παιχνιδιού Tetris στην αρχική συσκευασία.",
      "Διακρινόταν για την εξαιρετική ανθεκτικότητά του και τη μεγάλη αυτονομία λειτουργίας με 4 απλές μπαταρίες AA."
    ],
    "source": "https://el.wikipedia.org/wiki/Game_Boy",
    "locale": "el-GR",
    "tags": ["game-boy", "nintendo", "gaming", "consoles"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_137",
    "text": "Σε ποια χώρα εφευρέθηκε το θρυλικό βιντεοπαιχνίδι παζλ Tetris από τον προγραμματιστή Αλεξέι Παζίτνοφ το 1984;",
    "answers": ["Ιαπωνία", "Ηνωμένες Πολιτείες Αμερικής", "Σοβιετική Ένωση", "Γερμανία"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Αλεξέι Παζίτνοφ δημιούργησε το Tetris ενώ εργαζόταν στην Ακαδημία Επιστημών της Σοβιετικής Ένωσης στη Μόσχα σε έναν υπολογιστή Elektronika 60.",
    "funFacts": [
      "Το όνομα 'Tetris' προέρχεται από τον συνδυασμό της ελληνικής λέξης 'τέτρα' (καθώς όλα τα κομμάτια αποτελούνται από 4 τετράγωνα) και του τένις.",
      "Το διάσημο μουσικό θέμα του παιχνιδιού (Theme A) βασίζεται στο παραδοσιακό ρωσικό λαϊκό τραγούδι 'Korobeiniki'."
    ],
    "source": "https://el.wikipedia.org/wiki/Tetris",
    "locale": "el-GR",
    "tags": ["tetris", "gaming", "ussr", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_138",
    "text": "Σε ποιον κύριο σκοπό επικεντρώνεται η πλατφόρμα κοινωνικής δικτύωσης LinkedIn, η οποία ανήκει στη Microsoft;",
    "answers": ["Κοινή χρήση φωτογραφιών φαγητού", "Ζωντανές μεταδόσεις βιντεοπαιχνιδιών", "Αγοραπωλησίες μεταχειρισμένων ειδών", "Επαγγελματική δικτύωση και αναζήτηση εργασίας"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το LinkedIn ιδρύθηκε το 2002 από τον Ριντ Χόφμαν και επιτρέπει σε επαγγελματίες και επιχειρήσεις να συνδέονται και να δημοσιεύουν βιογραφικά και θέσεις εργασίας.",
    "funFacts": [
      "Η Microsoft εξαγόρασε το LinkedIn τον Δεκέμβριο του 2016 έναντι περίπου 26,2 δισεκατομμυρίων δολαρίων.",
      "Αριθμεί σήμερα πάνω από 900 εκατομμύρια εγγεγραμμένα μέλη από περισσότερες από 200 χώρες."
    ],
    "source": "https://el.wikipedia.org/wiki/LinkedIn",
    "locale": "el-GR",
    "tags": ["linkedin", "social-media", "careers", "microsoft"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_139",
    "text": "Ποιο διάσημο σύνθημα χρησιμοποιεί η διαδικτυακή πλατφόρμα συζητήσεων Reddit για να χαρακτηρίσει τον εαυτό της;",
    "answers": ["Η πρώτη σελίδα του διαδικτύου (The front page of the internet)", "Συνδέοντας τους ανθρώπους", "Σκεφτείτε διαφορετικά", "Ο κόσμος στα χέρια σας"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Reddit ιδρύθηκε το 2005 από τους Στιβ Χάφμαν και Αλέξις Οχανιάν και αυτοπροσδιορίζεται ως 'The front page of the internet'.",
    "funFacts": [
      "Το περιεχόμενο οργανώνεται σε θεματικές κοινότητες που ονομάζονται 'subreddits', με πρόθεμα r/ (π.χ. r/science).",
      "Η μασκότ του ιστότοπου είναι ένα ανθρωπόμορφο εξωγήινο ον με μία κεραία που ονομάζεται Snoo."
    ],
    "source": "https://el.wikipedia.org/wiki/Reddit",
    "locale": "el-GR",
    "tags": ["reddit", "social-media", "internet", "communities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_140",
    "text": "Ποιος Ρώσος επιχειρηματίας ίδρυσε τη δημοφιλή εφαρμογή κρυπτογραφημένων μηνυμάτων Telegram το 2013;",
    "answers": ["Γιούρι Μίλνερ", "Πάβελ Ντούροφ", "Εβγκένι Κασπέρσκι", "Όλεγκ Τινκόφ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Πάβελ Ντούροφ μαζί με τον αδελφό του Νικολάι δημιούργησαν το Telegram, έχοντας προηγουμένως ιδρύσει το μεγαλύτερο ρωσικό κοινωνικό δίκτυο VK.",
    "funFacts": [
      "Ο αδελφός του, Νικολάι Ντούροφ, ανέπτυξε το εξειδικευμένο πρωτόκολλο κρυπτογράφησης MTProto πάνω στο οποίο βασίζεται η εφαρμογή.",
      "Το Telegram παρέχει δημόσια κανάλια (channels) και ομάδες που μπορούν να φιλοξενήσουν έως και 200.000 μέλη."
    ],
    "source": "https://el.wikipedia.org/wiki/Telegram",
    "locale": "el-GR",
    "tags": ["telegram", "messaging", "privacy", "founders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_141",
    "text": "Πώς ονομάζεται η διαδικασία αρχικής σύνδεσης και αμοιβαίας αναγνώρισης ανάμεσα σε δύο συσκευές Bluetooth (π.χ. κινητό και ακουστικά);",
    "answers": ["Μόλυνση", "Επανεκκίνηση", "Σύζευξη (Pairing)", "Αποσυμπίεση"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η σύζευξη (pairing) καταχωρίζει ένα ασφαλές κλειδί κρυπτογράφησης ανάμεσα στις δύο συσκευές ώστε να συνδέονται αυτόματα στο μέλλον.",
    "funFacts": [
      "Κατά τη διαδικασία σύζευξης, η μία συσκευή πρέπει να βρίσκεται σε 'λειτουργία εντοπισμού' (discovery mode) για να εκπέμπει το όνομά της.",
      "Πολλές σύγχρονες συσκευές υποστηρίζουν σύζευξη με ένα απλό άγγιγμα μέσω NFC ή αυτόματη αναγνώριση Fast Pair."
    ],
    "source": "https://el.wikipedia.org/wiki/Bluetooth",
    "locale": "el-GR",
    "tags": ["bluetooth", "pairing", "wireless", "devices"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_142",
    "text": "Τι απενεργοποιεί άμεσα η ενεργοποίηση της «λειτουργίας πτήσης» (Airplane mode) σε ένα σύγχρονο smartphone;",
    "answers": ["Την οθόνη και τα ηχεία", "Την κάμερα και το μικρόφωνο", "Τον αισθητήρα δακτυλικού αποτυπώματος", "Όλους τους πομπούς ασύρματης επικοινωνίας (κινητή, Wi-Fi, Bluetooth)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η λειτουργία πτήσης διακόπτει όλες τις ασύρματες εκπομπές ραδιοσυχνοτήτων της συσκευής για την αποφυγή παρεμβολών στα όργανα ναυσιπλοΐας του αεροσκάφους.",
    "funFacts": [
      "Επειδή διακόπτει τη διαρκή αναζήτηση σημάτων κινητής τηλεφωνίας, βοηθά επίσης σημαντικά στην ταχύτερη φόρτιση και εξοικονόμηση της μπαταρίας.",
      "Στις περισσότερες συσκευές, ο χρήστης μπορεί να επανενεργοποιήσει χειροκίνητα το Wi-Fi ή το Bluetooth ακόμη και με τη λειτουργία πτήσης ενεργή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1_%CF%80%CF%84%CE%AE%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["airplane-mode", "smartphones", "wireless", "settings"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_143",
    "text": "Πώς ονομάζεται η λειτουργία κατά την οποία ένα smartphone μοιράζεται τη σύνδεση δεδομένων κινητής τηλεφωνίας λειτουργώντας ως ασύρματο Wi-Fi;",
    "answers": ["Προσωπικό σημείο πρόσβασης (Mobile Hotspot)", "Κρυφή περιήγηση", "Cloud backup", "Απομακρυσμένη επιφάνεια"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Mobile Hotspot (ή Tethering) μετατρέπει το τηλέφωνο σε φορητό ασύρματο ρούτερ επιτρέποντας σε λάπτοπ και τάμπλετ να συνδεθούν στο ίντερνετ.",
    "funFacts": [
      "Η σύνδεση hotspot καταναλώνει σημαντική ενέργεια μπαταρίας και μπορεί να αυξήσει τη θερμοκρασία του smartphone.",
      "Εκτός από Wi-Fi, ο διαμοιρασμός δεδομένων μπορεί να πραγματοποιηθεί επίσης μέσω καλωδίου USB ή Bluetooth."
    ],
    "source": "https://el.wikipedia.org/wiki/Tethering",
    "locale": "el-GR",
    "tags": ["hotspot", "tethering", "wifi", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_144",
    "text": "Πώς ονομάζεται η φορητή επαναφορτιζόμενη εξωτερική μπαταρία που χρησιμοποιείται για την τροφοδοσία κινητών τηλεφώνων μακριά από πρίζες;",
    "answers": ["Inverter", "Power bank", "Τροφοδοτικό UPS", "Σταθεροποιητής τάσης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το power bank περιέχει επαναφορτιζόμενα στοιχεία ιόντων λιθίου και θύρες USB, επιτρέποντας την εν κινήσει φόρτιση φορητών ηλεκτρονικών συσκευών.",
    "funFacts": [
      "Η χωρητικότητά τους μετριέται σε μιλιαμπερώρια (mAh), με τα πιο συνήθη οικιακά μοντέλα να κυμαίνονται από 5.000 έως 20.000 mAh.",
      "Οι διεθνείς κανονισμοί αεροπορικών πτήσεων απαγορεύουν τα μεγάλα power banks στις παραδοτέες αποσκευές και επιτρέπουν μόνο μικρά στη χειραποσκευή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%BF%CF%81%CE%B7%CF%84%CF%8C%CF%82_%CF%86%CE%BF%CF%81%CF%84%CE%B9%CF%83%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["power-bank", "batteries", "gadgets", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_145",
    "text": "Ποιο ανοιχτό διεθνές πρότυπο επαγωγικής ασύρματης φόρτισης χρησιμοποιείται σήμερα σχεδόν σε όλα τα σύγχρονα smartphones;",
    "answers": ["MagSafe", "Quick Charge", "Qi", "Dash Charge"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρότυπο Qi (προφέρεται 'τσι') αναπτύχθηκε από το Wireless Power Consortium (WPC) και επιτρέπει τη μεταφορά ενέργειας μέσω ηλεκτρομαγνητικής επαγωγής.",
    "funFacts": [
      "Το όνομα 'Qi' προέρχεται από την κινεζική φιλοσοφική έννοια της ζωτικής ενέργειας ή ροής.",
      "Η φόρτιση επιτυγχάνεται όταν το πηνίο της βάσης φόρτισης ευθυγραμμιστεί με το αντίστοιχο εσωτερικό πηνίο στο πίσω μέρος του τηλεφώνου."
    ],
    "source": "https://el.wikipedia.org/wiki/Qi_(%CF%80%CF%81%CF%8C%CF%84%CF%85%CF%80%CE%BF)",
    "locale": "el-GR",
    "tags": ["qi", "wireless-charging", "standards", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_146",
    "text": "Σε ποια μονάδα μέτρησης εκφράζεται ο ρυθμός ανανέωσης μιας οθόνης (πόσες φορές ανά δευτερόλεπτο ανανεώνεται η προβαλλόμενη εικόνα);",
    "answers": ["Watt (W)", "Volt (V)", "Decibel (dB)", "Hertz (Hz)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο ρυθμός ανανέωσης (refresh rate) μετριέται σε Hertz (Hz). Μια οθόνη 60 Hz ανανεώνει την εικόνα 60 φορές το δευτερόλεπτο, ενώ μια gaming οθόνη 120 Hz ή 144 Hz προσφέρει πολύ ομαλότερη κίνηση.",
    "funFacts": [
      "Πολλά σύγχρονα smartphones διαθέτουν οθόνες 120 Hz με τεχνολογία μεταβλητού ρυθμού (LTPO), που πέφτει έως και το 1 Hz για εξοικονόμηση μπαταρίας.",
      "Η μονάδα Hertz πήρε το όνομά της από τον Γερμανό φυσικό Χάινριχ Χερτς, ο οποίος απέδειξε πρώτος την ύπαρξη των ηλεκτρομαγνητικών κυμάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%85%CE%B8%CE%BC%CF%8C%CF%82_%CE%B1%CE%BD%CE%B1%CE%BD%CE%AD%CF%89%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["refresh-rate", "displays", "hertz", "monitors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_147",
    "text": "Ποιο είναι το κυριότερο οπτικό πλεονέκτημα των οθονών τεχνολογίας OLED σε σύγκριση με τις κλασικές οθόνες LCD;",
    "answers": ["Απόλυτο μαύρο χρώμα επειδή τα pixel σβήνουν εντελώς", "Μεγαλύτερο βάρος και πάχος", "Ανάγκη για ισχυρό οπίσθιο φωτισμό", "Χαμηλότερη αντίθεση"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στις οθόνες OLED (Organic Light Emitting Diode), κάθε εικονοστοιχείο παράγει το δικό του φως αυτόνομα, επιτρέποντας τέλειο μαύρο και άπειρη αντίθεση όταν σβήνει.",
    "funFacts": [
      "Επειδή δεν απαιτούν ξεχωριστή πλάκα οπίσθιου φωτισμού (backlight), οι οθόνες OLED μπορούν να κατασκευαστούν εξαιρετικά λεπτές, εύκαμπτες ή ακόμα και αναδιπλούμενες.",
      "Σε σκοτεινό θέμα (Dark Mode), οι οθόνες OLED καταναλώνουν σημαντικά λιγότερη ενέργεια μπαταρίας στα smartphones."
    ],
    "source": "https://el.wikipedia.org/wiki/OLED",
    "locale": "el-GR",
    "tags": ["oled", "displays", "hardware", "screens"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_148",
    "text": "Ποια αναλογία διαστάσεων οθόνης (aspect ratio) αποτελεί το παγκόσμιο πρότυπο για τις σύγχρονες τηλεοράσεις υψηλής ευκρίνειας και τα βίντεο ευρείας οθόνης;",
    "answers": ["4:3", "16:9", "1:1", "21:9"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η αναλογία 16:9 (widescreen) καθιερώθηκε ως το διεθνές πρότυπο για ψηφιακή τηλεόραση υψηλής ευκρίνειας (HDTV, Full HD, 4K UHD).",
    "funFacts": [
      "Αντικατέστησε την παλαιότερη σχεδόν τετράγωνη αναλογία 4:3 των αναλογικών τηλεοράσεων καθοδικού σωλήνα (CRT).",
      "Επιλέχθηκε ως ιδανικός συμβιβασμός ανάμεσα στις παλιές τηλεοπτικές εκπομπές 4:3 και τις πολύ φαρδιές κινηματογραφικές ταινίες 2,35:1."
    ],
    "source": "https://el.wikipedia.org/wiki/16:9",
    "locale": "el-GR",
    "tags": ["aspect-ratio", "displays", "video", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_149",
    "text": "Τι είδους αισθητήρα χρησιμοποιούν τα σύγχρονα οπτικά ποντίκια υπολογιστή για να παρακολουθούν την κίνηση πάνω σε μια επιφάνεια;",
    "answers": ["Μαγνητική πυξίδα", "Μηχανική λαστιχένια μπίλια", "Μικροσκοπική ψηφιακή κάμερα με LED ή λέιζερ", "Αισθητήρα υπερήχων"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Τα οπτικά ποντίκια φωτίζουν την επιφάνεια με LED ή λέιζερ και λαμβάνουν χιλιάδες μικροσκοπικές διαδοχικές φωτογραφίες το δευτερόλεπτο συγκρίνοντας τις μικροδιαφορές για τον υπολογισμό της κίνησης.",
    "funFacts": [
      "Αντικατέστησαν οριστικά τα παλιά μηχανικά ποντίκια με μπίλια, τα οποία μάζευαν σκόνη και απαιτούσαν συχνό εσωτερικό καθάρισμα.",
      "Τα σύγχρονα ποντίκια λέιζερ μπορούν να λειτουργήσουν αποτελεσματικά ακόμη και πάνω σε γυαλιστερές επιφάνειες ή διαφανές γυαλί."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BD%CF%84%CE%AF%CE%BA%CE%B9_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["mouse", "hardware", "input", "peripherals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_150",
    "text": "Πώς ονομάζεται η ενσωματωμένη ευαίσθητη στην αφή επιφάνεια κατάδειξης που αντικαθιστά το ποντίκι στους φορητούς υπολογιστές (laptops);",
    "answers": ["Joystick", "Οθόνη αφής", "Trackball", "Επιφάνεια αφής (Touchpad / Trackpad)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το touchpad (ή trackpad) ανιχνεύει την κίνηση των δακτύλων του χρήστη και υποστηρίζει χειρονομίες πολλαπλής αφής (gestures) για κύλιση και ζουμ.",
    "funFacts": [
      "Ο πρώτος φορητός υπολογιστής μαζικής παραγωγής που ενσωμάτωσε touchpad ήταν ο Apple PowerBook 500 το 1994.",
      "Τα σύγχρονα trackpads χρησιμοποιούν συχνά απτική ανάδραση (haptic feedback) με ηλεκτρομαγνήτες αντί για μηχανικό διακόπτη κλικ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B9%CE%BD%CE%B1%CE%BA%CE%AF%CE%B4%CE%B1_%CE%B1%CF%86%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["touchpad", "trackpad", "laptops", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_151",
    "text": "Πώς ονομάζεται η ψηφιακή βιντεοκάμερα που συνδέεται σε έναν υπολογιστή για τηλεδιασκέψεις και ζωντανή μετάδοση βίντεο στο διαδίκτυο;",
    "answers": ["Διαδικτυακή κάμερα (Webcam)", "Προβολέας (Projector)", "Σαρωτής (Scanner)", "Κάρτα καταγραφής τηλεόρασης"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η κάμερα web (webcam) τροφοδοτεί ή μεταδίδει την εικόνα της σε πραγματικό χρόνο μέσω υπολογιστή σε ένα δίκτυο υπολογιστών.",
    "funFacts": [
      "Η πρώτη webcam στην ιστορία τέθηκε σε λειτουργία το 1991 στο Πανεπιστήμιο του Κέιμπριτζ για να παρακολουθεί αν η καφετιέρα του εργαστηρίου ήταν γεμάτη.",
      "Η περίφημη καφετιέρα του Κέιμπριτζ συνδέθηκε στο διαδίκτυο το 1993 και συγκέντρωσε εκατομμύρια επισκέπτες πριν κλείσει οριστικά το 2001."
    ],
    "source": "https://el.wikipedia.org/wiki/Webcam",
    "locale": "el-GR",
    "tags": ["webcam", "hardware", "video", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_152",
    "text": "Ποια βασική λειτουργία ενός μικροφώνου αποκόπτει προσωρινά τη μετάδοση της φωνής μας προς τους υπόλοιπους συμμετέχοντες σε μια κλήση;",
    "answers": ["Ενίσχυση (Boost)", "Σίγαση (Mute)", "Ηχώ (Echo)", "Εξισορρόπηση (EQ)"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η λειτουργία σίγασης (mute) απενεργοποιεί προσωρινά την είσοδο του ήχου από το μικρόφωνο για να αποτρέψει τη μετάδοση ανεπιθύμητων περιβαλλοντικών θορύβων.",
    "funFacts": [
      "Η φράση 'You're on mute' (Είσαι στο mute) ανακηρύχθηκε μία από τις πιο συχνά ειπωμένες φράσεις παγκοσμίως κατά τις τηλεδιασκέψεις της πανδημίας.",
      "Πολλά σύγχρονα ακουστικά διαθέτουν φυσικό διακόπτη ή σιγάζουν αυτόματα όταν ο βραχίονας του μικροφώνου σηκωθεί προς τα πάνω."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%BA%CF%81%CF%8C%CF%86%CF%89%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["audio", "microphone", "conferencing", "settings"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_153",
    "text": "Ποια είναι η ονομαστική ταχύτητα μεταφοράς δεδομένων ενός τυπικού ενσύρματου δικτύου προτύπου Gigabit Ethernet;",
    "answers": ["10 Mbps", "100 Mbps", "1.000 Mbps (1 Gbps)", "10.000 Mbps"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το πρότυπο Gigabit Ethernet (IEEE 802.3ab) παρέχει ταχύτητα μετάδοσης 1 Gigabit ανά δευτερόλεπτο (1.000 Megabits/s) μέσω καλωδίων συνεστραμμένου ζεύγους Cat 5e ή Cat 6.",
    "funFacts": [
      "Είναι 10 φορές ταχύτερο από το προηγούμενο πρότυπο Fast Ethernet (100 Mbps) και 100 φορές ταχύτερο από το αρχικό Ethernet (10 Mbps).",
      "Σε ταχύτητα 1 Gbps, ένα αρχείο βίντεο μεγέθους 1 Gigabyte μπορεί θεωρητικά να μεταφερθεί μέσα σε περίπου 8 δευτερόλεπτα."
    ],
    "source": "https://el.wikipedia.org/wiki/Gigabit_Ethernet",
    "locale": "el-GR",
    "tags": ["ethernet", "networking", "gigabit", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_154",
    "text": "Ποιος όρος περιγράφει τη μέγιστη χωρητικότητα μετάδοσης ψηφιακών δεδομένων ενός δικτύου σε συγκεκριμένο χρονικό διάστημα;",
    "answers": ["Χρόνος απόκρισης", "Αντίσταση", "Διαμοιρασμός", "Εύρος ζώνης (Bandwidth)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το εύρος ζώνης (bandwidth) αντιπροσωπεύει τον όγκο πληροφορίας που μπορεί να μεταφερθεί ανά μονάδα χρόνου και μετριέται σε bits ανά δευτερόλεπτο (bps, Mbps, Gbps).",
    "funFacts": [
      "Μια συνηθισμένη αναλογία για την κατανόηση του bandwidth είναι ένας σωλήνας νερού: όσο πιο φαρδύς ο σωλήνας, τόσο περισσότερο νερό μπορεί να περάσει ταυτόχρονα.",
      "Το μεγαλύτερο bandwidth δεν σημαίνει απαραίτητα ταχύτερη απόκριση (ping), αλλά δυνατότητα μεταφοράς μεγαλύτερου όγκου ταυτόχρονα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%8D%CF%81%CE%BF%CF%82_%CE%B6%CF%8E%CE%BD%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["bandwidth", "networking", "telecommunications", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_155",
    "text": "Ποιος όρος περιγράφει τη διαδικασία και την ταχύτητα μεταφοράς αρχείων και δεδομένων από έναν απομακρυσμένο διακομιστή προς την τοπική συσκευή του χρήστη;",
    "answers": ["Λήψη (Download)", "Μεταφόρτωση (Upload)", "Ανασυγκρότηση (Defrag)", "Κρυπτογράφηση"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η λήψη (downloading) λαμβάνει δεδομένα από το διαδίκτυο και τα αποθηκεύει τοπικά στη συσκευή του χρήστη για προβολή ή χρήση.",
    "funFacts": [
      "Στις περισσότερες οικιακές συνδέσεις ADSL και VDSL, η ταχύτητα download είναι σημαντικά μεγαλύτερη από την ταχύτητα upload (ασύμμετρη σύνδεση).",
      "Όταν παρακολουθούμε ένα βίντεο στο διαδίκτυο, τα δεδομένα 'κατεβαίνουν' προσωρινά στη μνήμη cache της συσκευής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AE%CF%88%CE%B7_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["download", "internet", "networking", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_156",
    "text": "Ποιος όρος περιγράφει τη διαδικασία αποστολής αρχείων ή δεδομένων από την τοπική συσκευή του χρήστη προς έναν απομακρυσμένο διακομιστή στο διαδίκτυο;",
    "answers": ["Λήψη (Download)", "Μεταφόρτωση (Upload)", "Μορφοποίηση (Format)", "Εκκαθάριση (Purge)"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η μεταφόρτωση (uploading) στέλνει δεδομένα (όπως μια φωτογραφία, ένα email ή ένα βίντεο) από τον τοπικό υπολογιστή προς έναν διαδικτυακό διακομιστή.",
    "funFacts": [
      "Οι συμμετρικές συνδέσεις οπτικών ινών (FTTH) προσφέρουν την ίδια ακριβώς ταχύτητα για upload και download.",
      "Η ανάρτηση ενός βίντεο στο YouTube ή μιας φωτογραφίας στο Instagram αποτελεί κλασικό παράδειγμα upload."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CF%84%CE%B1%CF%86%CF%8C%CF%81%CF%84%CF%89%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["upload", "internet", "networking", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_157",
    "text": "Πώς ονομάζεται η χρονική καθυστέρηση που χρειάζεται ένα πακέτο δεδομένων για να μεταβεί από τη συσκευή στον διακομιστή και πίσω, μετρούμενη σε χιλιοστά του δευτερολέπτου (ms);",
    "answers": ["Bandwidth", "Baud rate", "Χρόνος καθυστέρησης (Latency / Ping)", "Bitrate"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το latency (ή ping) εκφράζει την ταχύτητα απόκρισης ενός δικτύου και είναι κρίσιμος παράγοντας για το διαδικτυακό gaming και τις βιντεοκλήσεις.",
    "funFacts": [
      "Η εντολή 'ping' πήρε το όνομά της από τον ήχο που κάνει το σόναρ των υποβρυχίων όταν εντοπίζει ένα αντικείμενο στον βυθό.",
      "Στο online gaming, ένα ping κάτω από 30 ms θεωρείται εξαιρετικό, ενώ πάνω από 150 ms δημιουργεί αισθητό lag (καθυστέρηση)."
    ],
    "source": "https://el.wikipedia.org/wiki/Ping",
    "locale": "el-GR",
    "tags": ["ping", "latency", "networking", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_158",
    "text": "Ποια τεχνολογική εταιρεία εξαγόρασε το σύστημα reCAPTCHA το 2009 και το χρησιμοποίησε για την ψηφιοποίηση αρχείων βιβλίων και αριθμών οδών στους χάρτες της;",
    "answers": ["Apple", "Microsoft", "Yahoo!", "Google"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Google εξαγόρασε το reCAPTCHA από το Πανεπιστήμιο Carnegie Mellon εκμεταλλευόμενη τις ανθρώπινες απαντήσεις για να αποκωδικοποιεί δυσανάγνωστες λέξεις σε παλιά σαρωμένα βιβλία.",
    "funFacts": [
      "Εκατομμύρια χρήστες βοηθούσαν καθημερινά εν αγνοία τους στην ψηφιοποίηση του αρχείου των New York Times λύνοντας CAPTCHAs.",
      "Η νεότερη έκδοση Invisible reCAPTCHA (v3) αναλύει τη φυσική συμπεριφορά του χρήστη χωρίς να απαιτεί καθόλου την επίλυση παζλ."
    ],
    "source": "https://el.wikipedia.org/wiki/ReCAPTCHA",
    "locale": "el-GR",
    "tags": ["recaptcha", "google", "security", "ai"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_159",
    "text": "Ποια εφαρμογή τηλεδιασκέψεων, που ιδρύθηκε από τον Έρικ Γιουάν, γνώρισε εκρηκτική παγκόσμια διάδοση για τηλεργασία και τηλεκπαίδευση το 2020;",
    "answers": ["Zoom", "Skype", "FaceTime", "Google Meet"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Zoom Video Communications ιδρύθηκε το 2011 και έγινε η κυρίαρχη πλατφόρμα βιντεοκλήσεων κατά τη διάρκεια της πανδημίας COVID-19.",
    "funFacts": [
      "Οι καθημερινοί συμμετέχοντες σε συναντήσεις Zoom εκτοξεύθηκαν από 10 εκατομμύρια τον Δεκέμβριο του 2019 σε πάνω από 300 εκατομμύρια τον Απρίλιο του 2020.",
      "Ο όρος 'Zoom fatigue' (κόπωση από το Zoom) επινοήθηκε από επιστήμονες για να περιγράψει την ψυχική εξάντληση από τις συνεχείς βιντεοδιασκέψεις."
    ],
    "source": "https://el.wikipedia.org/wiki/Zoom_Video_Communications",
    "locale": "el-GR",
    "tags": ["zoom", "video-call", "software", "communication"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_160",
    "text": "Ποια πλατφόρμα ομαδικής επικοινωνίας, τηλεδιασκέψεων και συνεργασίας ανέπτυξε η Microsoft ως βασικό ανταγωνιστή του Slack;",
    "answers": ["Yammer", "Microsoft Teams", "Skype for Business", "Windows Live Messenger"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Microsoft Teams κυκλοφόρησε το 2017 ενσωματώνοντας συνομιλίες, τηλεδιασκέψεις και άμεση συνεργασία σε έγγραφα του Microsoft 365.",
    "funFacts": [
      "Αντικατέστησε οριστικά το Skype for Business ως η κύρια επαγγελματική πλατφόρμα επικοινωνίας της Microsoft.",
      "Είναι στενά ενσωματωμένο στα Windows 11 και διαθέτει περισσότερους από 300 εκατομμύρια μηνιαίους ενεργούς χρήστες."
    ],
    "source": "https://el.wikipedia.org/wiki/Microsoft_Teams",
    "locale": "el-GR",
    "tags": ["teams", "microsoft", "collaboration", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'easy', 1, questions)

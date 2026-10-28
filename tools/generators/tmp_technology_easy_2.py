# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "technology_easy_061",
    "text": "Ποια Βρετανίδα μαθηματικός του 19ου αιώνα θεωρείται ιστορικά η πρώτη προγραμματίστρια υπολογιστών στον κόσμο;",
    "answers": ["Άντα Λάβλεϊς", "Μαρί Κιουρί", "Φλόρενς Νάιτινγκεϊλ", "Ρόζαλιντ Φράνκλιν"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Άντα Λάβλεϊς (Ada Lovelace) έγραψε το 1843 τον πρώτο αλγόριθμο που προοριζόταν για εκτέλεση από την Αναλυτική Μηχανή του Τσαρλς Μπάμπατζ.",
    "funFacts": [
      "Ήταν η μοναδική νόμιμη κόρη του διάσημου ρομαντικού ποιητή Λόρδου Βύρωνα.",
      "Προς τιμήν της, το αμερικανικό Υπουργείο Άμυνας ονόμασε 'Ada' μια υψηλού επιπέδου γλώσσα προγραμματισμού το 1980."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BD%CF%84%CE%B1_%CE%9B%CE%AC%CE%B2%CE%BB%CE%B5%CF%8A%CF%82",
    "locale": "el-GR",
    "tags": ["ada-lovelace", "history", "pioneers", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_062",
    "text": "Ποιος συνιδρυτής της Apple ήταν παγκοσμίως γνωστός για τις ομιλίες παρουσίασης νέων προϊόντων φορώντας μαύρο ζιβάγκο και τζιν;",
    "answers": ["Μπιλ Γκέιτς", "Στιβ Τζομπς", "Στιβ Βόζνιακ", "Τιμ Κουκ"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Στιβ Τζομπς (Steve Jobs) καθιέρωσε τις εμβληματικές παρουσιάσεις 'Keynotes' της Apple με το χαρακτηριστικό του ντύσιμο και τη διάσημη ατάκα 'One more thing...'.",
    "funFacts": [
      "Τα μαύρα ζιβάγκο που φορούσε σχεδιάστηκαν αποκλειστικά για εκείνον από τον διάσημο Ιάπωνα σχεδιαστή μόδας Ίσεϊ Μιγιάκε.",
      "Εκτός από την Apple, υπήρξε βασικός επενδυτής και επικεφαλής του πρωτοποριακού στούντιο κινουμένων σχεδίων Pixar."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B9%CE%B2_%CE%A4%CE%B6%CE%BF%CE%BC%CF%80%CF%82",
    "locale": "el-GR",
    "tags": ["steve-jobs", "apple", "founders", "personalities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_063",
    "text": "Ποιο δημοφιλές πρόγραμμα επεξεργασίας υπολογιστικών φύλλων (spreadsheets) αποτελεί μέρος της σουίτας Microsoft Office;",
    "answers": ["Microsoft PowerPoint", "Microsoft Access", "Microsoft Excel", "Microsoft Publisher"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Microsoft Excel κυκλοφόρησε για πρώτη φορά το 1985 και αποτελεί το πιο διαδεδομένο λογισμικό για ανάλυση αριθμητικών δεδομένων, πίνακες και γραφήματα.",
    "funFacts": [
      "Η πρώτη έκδοση του Microsoft Excel κυκλοφόρησε αρχικά για υπολογιστές Apple Macintosh το 1985, πριν διατεθεί για Windows το 1987.",
      "Ένα φύλλο εργασίας στο σύγχρονο Excel υποστηρίζει έως 1.048.576 γραμμές και 16.384 στήλες."
    ],
    "source": "https://el.wikipedia.org/wiki/Microsoft_Excel",
    "locale": "el-GR",
    "tags": ["excel", "microsoft", "software", "office"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_064",
    "text": "Πώς ονομάζεται το κακόβουλο λογισμικό που μεταμφιέζεται σε χρήσιμο πρόγραμμα για να παραπλανήσει τον χρήστη, δανειζόμενο το όνομά του από την αρχαία ελληνική ιστορία;",
    "answers": ["Spyware", "Ransomware", "Worm", "Δούρειος Ίππος (Trojan horse)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Δούρειος Ίππος (Trojan horse) φαίνεται ως αθώο ή χρήσιμο αρχείο, αλλά μόλις εκτελεστεί επιτρέπει σε εισβολείς να αποκτήσουν έλεγχο του συστήματος.",
    "funFacts": [
      "Σε αντίθεση με τους ιούς υπολογιστών (viruses) και τα σκουλήκια (worms), τα Trojans δεν πολλαπλασιάζονται από μόνα τους μολύνοντας άλλα αρχεία.",
      "Το όνομα εμπνεύστηκε από τον ξύλινο ίππο που χρησιμοποίησαν οι αρχαίοι Έλληνες για να εισχωρήσουν μυστικά στην Τροία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%BF%CF%8D%CF%81%CE%B5%CE%B9%CE%BF%CF%82_%CE%87%CF%80%CF%80%CE%BF%CF%82_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
    "locale": "el-GR",
    "tags": ["trojan", "malware", "cybersecurity", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_065",
    "text": "Ποια εφαρμογή σύντομων βίντεο, που ανήκει στην εταιρεία ByteDance, σημείωσε τεράστια παγκόσμια διάδοση ιδίως στη νεολαία μετά το 2018;",
    "answers": ["TikTok", "Snapchat", "Vine", "Tumblr"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το TikTok ξεκίνησε διεθνώς το 2017 μετά τη συγχώνευση με την εφαρμογή Musical.ly, προσφέροντας σύντομα κατακόρυφα βίντεο με μουσική υπόκρουση.",
    "funFacts": [
      "Στην εγχώρια αγορά της Κίνας η εφαρμογή κυκλοφορεί με διαφορετική έκδοση και ονομασία ως 'Douyin'.",
      "Έγινε η πρώτη εφαρμογή μη αμερικανικής προέλευσης που ξεπέρασε τα 3 δισεκατομμύρια παγκόσμιες λήψεις."
    ],
    "source": "https://el.wikipedia.org/wiki/TikTok",
    "locale": "el-GR",
    "tags": ["tiktok", "social-media", "video", "mobile"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_066",
    "text": "Τι σημαίνουν τα αρχικά «IP» στη φράση «διεύθυνση IP» που ταυτοποιεί μοναδικά μια συνδεδεμένη συσκευή στο δίκτυο;",
    "answers": ["Internal Program", "Internet Protocol", "Integrated Pathway", "Information Packet"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το IP (Internet Protocol - Πρωτόκολλο Διαδικτύου) είναι το σύνολο κανόνων που διαχειρίζεται τη δρομολόγηση και διευθυνσιοδότηση πακέτων δεδομένων στο διαδίκτυο.",
    "funFacts": [
      "Το κλασικό πρωτόκολλο IPv4 χρησιμοποιεί 32-bit διευθύνσεις παρέχοντας περίπου 4,3 δισεκατομμύρια διευθύνσεις.",
      "Το νεότερο IPv6 χρησιμοποιεί 128 bits, προσφέροντας πρακτικά ανεξάντλητο αριθμό διευθύνσεων (περίπου 340 undecillion)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B5%CF%8D%CE%B8%CF%85%CE%BD%CF%83%CE%B7_IP",
    "locale": "el-GR",
    "tags": ["ip", "networking", "internet", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_067",
    "text": "Πόσα Megabytes (MB) περιέχει ακριβώς ένα Gigabyte (GB) σύμφωνα με το δυαδικό σύστημα μέτρησης της πληροφορικής;",
    "answers": ["100 MB", "512 MB", "1.024 MB", "2.048 MB"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στο δυαδικό σύστημα που χρησιμοποιούν τα λειτουργικά συστήματα, 1 Gigabyte (Gibibyte) ισούται ακριβώς με 1.024 Megabytes.",
    "funFacts": [
      "Οι κατασκευαστές σκληρών δίσκων χρησιμοποιούν συνήθως το δεκαδικό σύστημα όπου 1 GB = 1.000 MB, γεγονός που δημιουργεί διαφορά στην αναγραφόμενη χωρητικότητα.",
      "Ένα Gigabyte είναι αρκετό για την αποθήκευση περίπου 250 τραγουδιών MP3 υψηλής ποιότητας."
    ],
    "source": "https://el.wikipedia.org/wiki/Gigabyte",
    "locale": "el-GR",
    "tags": ["gigabyte", "storage", "units", "data"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_068",
    "text": "Ποια μέθοδος ηλεκτρονικής εξαπάτησης προσποιείται έμπιστες τράπεζες ή υπηρεσίες για να υποκλέψει μυστικούς κωδικούς και στοιχεία πιστωτικών καρτών;",
    "answers": ["DDoS", "Trojan", "Adware", "Ψάρεμα (Phishing)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το ηλεκτρονικό «ψάρεμα» (Phishing) χρησιμοποιεί παραπλανητικά μηνύματα ηλεκτρονικού ταχυδρομείου ή πλαστές ιστοσελίδες για να αποσπάσει ευαίσθητα δεδομένα χρηστών.",
    "funFacts": [
      "Ο όρος είναι λογοπαίγνιο με την αγγλική λέξη 'fishing' (ψάρεμα), αντικαθιστώντας το 'f' με 'ph' όπως συνήθιζαν παλιοί χάκερς (phreaks).",
      "Περισσότερο από το 90% των επιτυχημένων κυβερνοεπιθέσεων σε επιχειρήσεις ξεκινούν από παραπλανητικό email τύπου phishing."
    ],
    "source": "https://el.wikipedia.org/wiki/Phishing",
    "locale": "el-GR",
    "tags": ["phishing", "security", "scams", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_069",
    "text": "Ποιος Βρετανός επιστήμονας υπολογιστών επινόησε τον Παγκόσμιο Ιστό (World Wide Web) το 1989 στο εργαστήριο CERN;",
    "answers": ["Τιμ Μπέρνερς-Λι", "Βιντ Σερφ", "Μαρκ Άντρισεν", "Μαρκ Ζάκερμπεργκ"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Σερ Τιμ Μπέρνερς-Λι (Tim Berners-Lee) συνέλαβε την ιδέα του ιστού για την εύκολη διαμοίραση πληροφοριών ανάμεσα σε ερευνητές επιστήμονες.",
    "funFacts": [
      "Αρνήθηκε να κατοχυρώσει με δίπλωμα ευρεσιτεχνίας την εφεύρεσή του, χαρίζοντας τον Παγκόσμιο Ιστό ελεύθερα σε ολόκληρη την ανθρωπότητα.",
      "Χρίστηκε ιππότης από τη βασίλισσα Ελισάβετ Β' το 2004 για την ανεκτίμητη προσφορά του στην παγκόσμια τεχνολογική ανάπτυξη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9%CE%BC_%CE%9C%CF%80%CE%AD%CF%81%CE%BD%CE%B5%CF%81%CF%82_%CE%9B%CE%B9",
    "locale": "el-GR",
    "tags": ["tim-berners-lee", "web", "internet", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_070",
    "text": "Πώς ονομάζεται το μικρότερο ανεξάρτητο σημείο ή στοιχείο που συνθέτει μια ψηφιακή εικόνα στην οθόνη μιας συσκευής;",
    "answers": ["Byte", "Pixel", "Voxel", "Bit"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το εικονοστοιχείο (pixel) είναι η βασική δομική μονάδα μιας ψηφιακής εικόνας, ικανό να εμφανίσει ένα συγκεκριμένο χρώμα και φωτεινότητα.",
    "funFacts": [
      "Ο όρος 'pixel' προέρχεται από τη συντόμευση των αγγλικών λέξεων 'picture element' (στοιχείο εικόνας).",
      "Ένα εκατομμύριο pixels ισοδυναμούν με ένα Megapixel (MP), μονάδα που χρησιμοποιείται για τη μέτρηση ανάλυσης ψηφιακών καμερών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B9%CE%BA%CE%BF%CE%BD%CE%BF%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%CE%AF%CE%BF",
    "locale": "el-GR",
    "tags": ["pixel", "displays", "graphics", "imaging"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_071",
    "text": "Ποιο είναι το συνηθέστερο μέγιστο εύρος εμβέλειας για τις τυπικές συσκευές Bluetooth (Class 2), όπως ασύρματα ακουστικά και ηχεία;",
    "answers": ["Περίπου 1 μέτρο", "Περίπου 50 μέτρα", "Περίπου 10 μέτρα", "Περίπου 500 μέτρα"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι περισσότερες καταναλωτικές συσκευές Bluetooth ανήκουν στην Κατηγορία 2 (Class 2), η οποία έχει ονομαστική εμβέλεια περίπου 10 μέτρων σε ανοιχτό χώρο.",
    "funFacts": [
      "Φυσικά εμπόδια, όπως τοίχοι από μπετόν ή μεταλλικές επιφάνειες, μπορούν να μειώσουν την πραγματική εμβέλεια σύνδεσης.",
      "Υπάρχουν συσκευές Bluetooth Class 1 βιομηχανικής χρήσης που μπορούν να φτάσουν σε απόσταση έως και 100 μέτρων."
    ],
    "source": "https://el.wikipedia.org/wiki/Bluetooth",
    "locale": "el-GR",
    "tags": ["bluetooth", "wireless", "specifications", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_072",
    "text": "Ποιος Φινλανδός μηχανικός λογισμικού δημιούργησε τον αρχικό πυρήνα του λειτουργικού συστήματος Linux το 1991;",
    "answers": ["Ρίτσαρντ Στόλμαν", "Μπιάρνε Στρούστρουπ", "Κεν Τόμπσον", "Λίνους Τόρβαλντς"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Λίνους Τόρβαλντς (Linus Torvalds) ανακοίνωσε τη δημιουργία του Linux τον Αύγουστο του 1991 ως χόμπι, ενώ ήταν φοιτητής στο Πανεπιστήμιο του Ελσίνκι.",
    "funFacts": [
      "Εκτός από το Linux, ο Τόρβαλντς δημιούργησε επίσης το Git, το πιο δημοφιλές σύστημα ελέγχου εκδόσεων κώδικα στον κόσμο.",
      "Το μήνυμά του στο Usenet το 1991 ξεκινούσε ταπεινά με τη φράση: 'Κάνω ένα (δωρεάν) λειτουργικό σύστημα (απλώς ένα χόμπι, δεν θα είναι μεγάλο και επαγγελματικό)'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%AF%CE%BD%CE%BF%CF%85%CF%82_%CE%A4%CF%8C%CF%81%CE%B2%CE%B1%CE%BB%CE%BD%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["linus-torvalds", "linux", "open-source", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_073",
    "text": "Ποιο είναι το πιο διαδεδομένο πρόγραμμα επεξεργασίας κειμένου στον κόσμο, βασικό μέλος του πακέτου εφαρμογών Microsoft Office;",
    "answers": ["Microsoft Word", "Notepad++", "Adobe InDesign", "LibreOffice Writer"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Microsoft Word κυκλοφόρησε για πρώτη φορά το 1983 υπό το όνομα 'Multi-Tool Word' και αποτελεί το παγκόσμιο πρότυπο για συγγραφή και μορφοποίηση εγγράφων.",
    "funFacts": [
      "Ήταν ένα από τα πρώτα προγράμματα που εφάρμοσαν την αρχή WYSIWYG ('What You See Is What You Get'), όπου η οθόνη δείχνει ακριβώς πώς θα τυπωθεί το έγγραφο.",
      "Η προεπιλεγμένη μορφή αρχείων του (.docx) καθιερώθηκε το 2007 και βασίζεται σε συμπιεσμένη δομή αρχείων XML."
    ],
    "source": "https://el.wikipedia.org/wiki/Microsoft_Word",
    "locale": "el-GR",
    "tags": ["word", "microsoft", "software", "office"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_074",
    "text": "Ποια συσκευή δικτύου αναλαμβάνει να δρομολογεί την κυκλοφορία δεδομένων ανάμεσα στο οικιακό τοπικό δίκτυο και το διαδίκτυο;",
    "answers": ["Εκτυπωτής", "Δρομολογητής (Router)", "Κάρτα ήχου", "Τροφοδοτικό"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο δρομολογητής (router) εξετάζει τις διευθύνσεις προορισμού των πακέτων δικτύου και επιλέγει την καλύτερη διαδρομή για τη μεταφορά τους.",
    "funFacts": [
      "Οι περισσότεροι σύγχρονοι οικιακοί δρομολογητές συνδυάζουν σε μία συσκευή μόντεμ, ασύρματο σημείο πρόσβασης Wi-Fi, μεταγωγέα switch και τείχος προστασίας.",
      "Χρησιμοποιούν τεχνολογία NAT (Network Address Translation) ώστε πολλές συσκευές να μοιράζονται μία μόνο δημόσια διεύθυνση IP."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CF%81%CE%BF%CE%BC%CE%BF%CE%BB%CE%BF%CE%B3%CE%B7%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["router", "networking", "hardware", "internet"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_075",
    "text": "Ποιο πραγματικό έντομο που παγιδεύτηκε σε έναν υπολογιστή το 1947 ενέπνευσε την καθιέρωση του όρου «bug» για τα σφάλματα προγραμμάτων;",
    "answers": ["Μυρμήγκι", "Κουνούπι", "Σκόρος (πεταλούδα νύχτας)", "Σκαθάρι"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Στις 9 Σεπτεμβρίου 1947, η ομάδα της πρωτοπόρου Γκρέις Χόπερ εντόπισε έναν νεκρό σκόρο παγιδευμένο στο ρελέ 70 του υπολογιστή Harvard Mark II.",
    "funFacts": [
      "Ο σκόρος αφαιρέθηκε προσεκτικά και κολλήθηκε με ταινία στο ημερολόγιο καταγραφής του εργαστηρίου με τη σημείωση: 'Πρώτη πραγματική περίπτωση εντοπισμού εντόμου (bug)'.",
      "Το ιστορικό αυτό ημερολόγιο φυλάσσεται σήμερα στο Εθνικό Μουσείο Αμερικανικής Ιστορίας Smithsonian."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%86%CE%AC%CE%BB%CE%BC%CE%B1_%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CE%BC%CE%B9%CE%BA%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["bug", "grace-hopper", "history", "software"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_076",
    "text": "Ποιο ιστορικό μέσο μαγνητικής αποθήκευσης απεικονίζεται μέχρι σήμερα ως το παγκόσμιο εικονίδιο «Αποθήκευση» (Save) σε πολλά προγράμματα υπολογιστή;",
    "answers": ["Κασέτα ήχου", "Διάτρητη κάρτα", "Οπτικός δίσκος CD", "Δισκέτα (Floppy disk)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η δισκέτα 3,5 ιντσών ήταν το κυρίαρχο φορητό μέσο αποθήκευσης τις δεκαετίες του 1980 και 1990 και καθιερώθηκε ως σύμβολο αποθήκευσης αρχείων.",
    "funFacts": [
      "Μια τυπική δισκέτα 3,5 ιντσών υψηλής πυκνότητας (HD) είχε χωρητικότητα μόλις 1,44 Megabytes.",
      "Η πρώτη εμπορική δισκέτα αναπτύχθηκε από την IBM το 1971 και είχε διάμετρο 8 ίντσες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CF%83%CE%BA%CE%AD%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["floppy-disk", "storage", "history", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_077",
    "text": "Τι σημαίνουν τα αρχικά της δημοφιλούς μορφής ψηφιακών εγγράφων «PDF»;",
    "answers": ["Portable Document Format", "Public Digital File", "Printed Data Folder", "Program Data Function"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το PDF (Portable Document Format - Φορητή Μορφή Εγγράφου) σχεδιάστηκε για την ανεξάρτητη προβολή εγγράφων χωρίς να αλλοιώνεται η γραμματοσειρά ή η διάταξη.",
    "funFacts": [
      "Το έργο ξεκίνησε από τον συνιδρυτή της Adobe, Τζον Γουόρνοκ, με την κωδική ονομασία 'The Camelot Project' το 1991.",
      "Εκτός από κείμενο και εικόνες, ένα σύγχρονο αρχείο PDF μπορεί να περιέχει διαδραστικές φόρμες, ψηφιακές υπογραφές και ενσωματωμένα βίντεο."
    ],
    "source": "https://el.wikipedia.org/wiki/PDF",
    "locale": "el-GR",
    "tags": ["pdf", "adobe", "formats", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_078",
    "text": "Πώς ονομάζεται το βασικό λογισμικό που διαχειρίζεται το υλικό μιας συσκευής και επιτρέπει στους χρήστες να εκτελούν άλλες εφαρμογές;",
    "answers": ["Πρόγραμμα προστασίας από ιούς", "Λειτουργικό σύστημα (Operating System)", "Πρόγραμμα περιήγησης", "Βάση δεδομένων"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το λειτουργικό σύστημα (OS) είναι το θεμελιώδες λογισμικό που γεφυρώνει το υλικό (hardware) με τις εφαρμογές χρήστη, ελέγχοντας τη μνήμη και τους επεξεργαστές.",
    "funFacts": [
      "Τα Windows, το macOS, το Linux, το Android και το iOS είναι τα πιο ευρέως χρησιμοποιούμενα λειτουργικά συστήματα στον πλανήτη.",
      "Το πρώτο λειτουργικό σύστημα στην ιστορία δημιουργήθηκε το 1956 από την General Motors για τον υπολογιστή IBM 704."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%B9%CE%BA%CF%8C_%CF%83%CF%8D%CF%83%CF%84%CE%B7%CE%BC%CE%B1",
    "locale": "el-GR",
    "tags": ["operating-systems", "software", "computers", "architecture"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_079",
    "text": "Ποιο κλασικό πρότυπο ενσύρματης σύνδεσης τοπικών δικτύων (LAN) χρησιμοποιεί συνήθως καλώδια με βύσματα RJ-45;",
    "answers": ["Bluetooth", "FireWire", "Ethernet", "Thunderbolt"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Ethernet είναι η κυρίαρχη τεχνολογία ενσύρματης δικτύωσης για τη σύνδεση υπολογιστών σε τοπικό δίκτυο (LAN), παρέχοντας υψηλή ταχύτητα και σταθερότητα.",
    "funFacts": [
      "Αναπτύχθηκε το 1973 από τον Ρόμπερτ Μέτκαλφ και τους συνεργάτες του στο ιστορικό ερευνητικό κέντρο Xerox PARC.",
      "Το όνομα εμπνεύστηκε από τον 'αιθέρα' (luminiferous aether), μια υποθετική ουσία που οι φυσικοί του 19ου αιώνα πίστευαν ότι μετέφερε το φως."
    ],
    "source": "https://el.wikipedia.org/wiki/Ethernet",
    "locale": "el-GR",
    "tags": ["ethernet", "networking", "cables", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_080",
    "text": "Πώς ονομάζεται το κακόβουλο πρόγραμμα που προσκολλάται σε άλλα αρχεία και αντιγράφει τον εαυτό του με σκοπό να εξαπλωθεί σε άλλες συσκευές;",
    "answers": ["Επεξεργαστής κειμένου", "Οδηγός συσκευής (Driver)", "Πυρήνας συστήματος", "Ιός υπολογιστή (Computer virus)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο ιός υπολογιστή (computer virus) εισάγει τον κώδικά του μέσα σε άλλα νόμιμα προγράμματα και εξαπλώνεται όταν αυτά εκτελούνται.",
    "funFacts": [
      "Ο πρώτος ιός για προσωπικούς υπολογιστές PC ονομαζόταν 'Brain' και γράφτηκε το 1986 στο Πακιστάν από δύο αδέλφια.",
      "Ο όρος 'ιός' υιοθετήθηκε λόγω της αναλογίας με τους βιολογικούς ιούς, οι οποίοι εισβάλλουν σε ζωντανά κύτταρα για να αναπαραχθούν."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CF%8C%CF%82_%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE",
    "locale": "el-GR",
    "tags": ["virus", "malware", "security", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_081",
    "text": "Ποιος όρος περιγράφει τη συνεχή μετάδοση και αναπαραγωγή ήχου ή βίντεο μέσω διαδικτύου χωρίς να απαιτείται η προηγούμενη λήψη ολόκληρου του αρχείου;",
    "answers": ["Ροή δεδομένων (Streaming)", "Μεταγλώττιση (Compiling)", "Αποσυμπίεση (Unzipping)", "Υπερχρονισμός (Overclocking)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το streaming επιτρέπει στον χρήστη να παρακολουθεί περιεχόμενο πολυμέσων σχεδόν ακαριαία, καθώς τα δεδομένα λαμβάνονται και αναπαράγονται ταυτόχρονα.",
    "funFacts": [
      "Η τεχνολογία streaming ευθύνεται σήμερα για περισσότερο από το 60% της συνολικής παγκόσμιας κυκλοφορίας δεδομένων στο διαδίκτυο.",
      "Υπηρεσίες όπως το Spotify, το YouTube, το Netflix και το Twitch αποτελούν χαρακτηριστικά παραδείγματα πλατφορμών streaming."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CE%AE_%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["streaming", "media", "internet", "video"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_082",
    "text": "Τι σημαίνουν τα αρχικά των παραδοσιακών σύντομων γραπτών μηνυμάτων «SMS» στα κινητά τηλέφωνα;",
    "answers": ["Simple Mobile System", "Short Message Service", "Standard Mobile Signal", "Secure Messaging Software"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το SMS (Short Message Service - Υπηρεσία Σύντομων Μηνυμάτων) επιτρέπει την ανταλλαγή κειμένων έως 160 χαρακτήρων μεταξύ κινητών τηλεφώνων.",
    "funFacts": [
      "Το πρώτο SMS στην ιστορία στάλθηκε στις 3 Δεκεμβρίου 1992 από τον Νιλ Πάπγουορθ και έγραφε απλώς: 'Merry Christmas' (Καλά Χριστούγεννα).",
      "Το ανώτατο όριο των 160 χαρακτήρων ορίστηκε από τον μηχανικό Φρίντχελμ Χίλεμπραντ, ο οποίος μέτρησε τους μέσους χαρακτήρες σε τυπικές καρτ ποστάλ."
    ],
    "source": "https://el.wikipedia.org/wiki/SMS",
    "locale": "el-GR",
    "tags": ["sms", "telecommunications", "mobile", "standards"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_083",
    "text": "Ποια ανάλυση οθόνης (Ultra HD) διαθέτει περίπου 4.000 οριζόντια εικονοστοιχεία (συνήθως 3840 x 2160 pixels);",
    "answers": ["Full HD (1080p)", "720p", "4K", "VGA"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η ανάλυση 4K (Ultra High Definition) προσφέρει τέσσερις φορές περισσότερα pixels σε σχέση με την κλασική ανάλυση Full HD (1080p).",
    "funFacts": [
      "Στον οικιακό κινηματογράφο και τις τηλεοράσεις, η ανάλυση 4K αντιστοιχεί συγκεκριμένα σε 3840 επί 2160 pixels (περίπου 8,3 Megapixels).",
      "Στον επαγγελματικό ψηφιακό κινηματογράφο (DCI 4K), η ανάλυση ορίζεται ελαφρώς πλατύτερη, στα 4096 επί 2160 pixels."
    ],
    "source": "https://el.wikipedia.org/wiki/4K",
    "locale": "el-GR",
    "tags": ["4k", "displays", "resolution", "video"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_084",
    "text": "Πώς ονομάζεται η ταχύτατη ενδιάμεση μνήμη που αποθηκεύει προσωρινά συχνά χρησιμοποιούμενα δεδομένα για άμεση επανάκτηση;",
    "answers": ["Σκληρός δίσκος", "Μαγνητική ταινία", "Οπτικός δίσκος", "Κρυφή μνήμη (Cache)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η μνήμη cache αποθηκεύει αντίγραφα δεδομένων ώστε μελλοντικά αιτήματα για τα δεδομένα αυτά να εξυπηρετούνται πολύ ταχύτερα.",
    "funFacts": [
      "Υπάρχει σε επίπεδο επεξεργαστή (L1, L2, L3 cache) αλλά και στους περιηγητές ιστού για την ταχύτερη φόρτωση εικόνων και σελίδων.",
      "Η λέξη 'cache' προέρχεται από το γαλλικό ρήμα 'cacher', που σημαίνει 'κρύβω'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%81%CF%85%CF%86%CE%AE_%CE%BC%CE%BD%CE%AE%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["cache", "memory", "hardware", "performance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_085",
    "text": "Ποια μέθοδος ασφαλείας απαιτεί από τον χρήστη να παρέχει δύο ανεξάρτητα αποδεικτικά ταυτότητας για να αποκτήσει πρόσβαση σε έναν λογαριασμό;",
    "answers": ["Ταυτοποίηση δύο παραγόντων (2FA)", "Ενιαία σύνδεση (SSO)", "Ανώνυμη περιήγηση", "Κρυπτογράφηση δίσκου"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το 2FA (Two-Factor Authentication) συνδυάζει συνήθως κάτι που ξέρεις (κωδικός) με κάτι που κατέχεις (smartphone ή κωδικός SMS), αυξάνοντας δραστικά την ασφάλεια.",
    "funFacts": [
      "Η ενεργοποίηση του 2FA αποτρέπει πάνω από το 99% των μαζικών αυτοματοποιημένων επιθέσεων υποκλοπής λογαριασμών.",
      "Οι εφαρμογές παραγωγής κωδικών (όπως το Google Authenticator) βασίζονται στον αλγόριθμο TOTP (Time-based One-time Password)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BB%CE%B5%CE%B3%CF%87%CE%BF%CF%82_%CF%84%CE%B1%CF%85%CF%84%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82_%CF%80%CE%BF%CE%BB%CE%BB%CE%B1%CF%80%CE%BB%CF%8E%CE%BD_%CF%80%CE%B1%CF%81%CE%B1%CE%B3%CF%8C%CE%BD%CF%84%CF%89%CE%BD",
    "locale": "el-GR",
    "tags": ["2fa", "security", "authentication", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_086",
    "text": "Ποιο βασικό εξάρτημα ΔΕΝ περιέχει ένας σύγχρονος δίσκος SSD σε σύγκριση με έναν παραδοσιακό σκληρό δίσκο HDD;",
    "answers": ["Ηλεκτρονικά τσιπ μνήμης", "Περιστρεφόμενους μηχανικούς δίσκους", "Πλακέτα ελεγκτή", "Θύρα σύνδεσης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι δίσκοι SSD δεν διαθέτουν κινούμενα μηχανικά μέρη ούτε μαγνητικές πλάκες, αποθηκεύοντας όλα τα δεδομένα σε ημιαγωγούς μνήμης flash.",
    "funFacts": [
      "Η απουσία κινούμενων μερών κάνει τους SSD σχεδόν απρόσβλητους σε κραδασμούς που θα κατέστρεφαν έναν συμβατικό σκληρό δίσκο.",
      "Η τεχνολογία μνήμης που χρησιμοποιούν ονομάζεται NAND flash και διατηρεί τα δεδομένα ακόμη και χωρίς ηλεκτρικό ρεύμα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CF%83%CF%84%CE%B5%CF%81%CE%B5%CE%AC%CF%82_%CE%BA%CE%B1%CF%84%CE%AC%CF%83%CF%84%CE%B1%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["ssd", "storage", "hardware", "flash-memory"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_087",
    "text": "Ποια ιστορική σειρά υπολογιστών παρουσίασε η Apple το 1984 με μια διάσημη τηλεοπτική διαφήμιση εμπνευσμένη από το βιβλίο «1984» του Όργουελ;",
    "answers": ["Apple I", "Apple II", "Macintosh", "iMac"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο πρώτος Apple Macintosh κυκλοφόρησε τον Ιανουάριο του 1984 καθιερώνοντας το γραφικό περιβάλλον εργασίας και το ποντίκι στο ευρύ καταναλωτικό κοινό.",
    "funFacts": [
      "Η θρυλική διαφήμιση σκηνοθετήθηκε από τον Ρίντλεϊ Σκοτ και προβλήθηκε κατά τη διάρκεια του τελικού του Super Bowl XVIII.",
      "Το όνομα 'Macintosh' προήλθε από την αγαπημένη ποικιλία μήλων McIntosh του επικεφαλής του έργου Τζεφ Ράσκιν."
    ],
    "source": "https://el.wikipedia.org/wiki/Macintosh",
    "locale": "el-GR",
    "tags": ["macintosh", "apple", "history", "computers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_088",
    "text": "Ποια ασύρματη τεχνολογία πολύ μικρής εμβέλειας επιτρέπει τις ανέπαφες πληρωμές μέσω κινητού τηλεφώνου ή τραπεζικής κάρτας;",
    "answers": ["Wi-Fi", "GPS", "Infrared", "NFC (Near Field Communication)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το NFC (Near Field Communication) λειτουργεί σε απόσταση λίγων εκατοστών, επιτρέποντας ασφαλή ανταλλαγή δεδομένων για ανέπαφες πληρωμές και ταυτοποίηση.",
    "funFacts": [
      "Βασίζεται στην τεχνολογία RFID (ραδιοσυχνική αναγνώριση) και λειτουργεί στη συχνότητα των 13,56 MHz.",
      "Η πολύ μικρή εμβέλεια (κάτω από 4 εκατοστά) αποτελεί χαρακτηριστικό ασφαλείας για να αποτρέπονται ανεπιθύμητες υποκλοπές."
    ],
    "source": "https://el.wikipedia.org/wiki/NFC",
    "locale": "el-GR",
    "tags": ["nfc", "wireless", "payments", "smartphones"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_089",
    "text": "Πώς ονομάζεται το λογισμικό του οποίου ο πηγαίος κώδικας διατίθεται ελεύθερα στο κοινό για μελέτη, τροποποίηση και διανομή;",
    "answers": ["Λογισμικό ανοιχτού κώδικα (Open Source)", "Εμπορικό λογισμικό (Proprietary)", "Υποκλοπικό λογισμικό (Spyware)", "Δοκιμαστικό λογισμικό (Shareware)"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το λογισμικό ανοιχτού κώδικα (Open Source Software) επιτρέπει σε οποιονδήποτε προγραμματιστή να δει τον κώδικα, να τον βελτιώσει και να συνεισφέρει στην κοινότητα.",
    "funFacts": [
      "Το λειτουργικό σύστημα Linux, ο φυλλομετρητής Firefox και ο διακομιστής Apache αποτελούν κορυφαία παραδείγματα λογισμικού ανοιχτού κώδικα.",
      "Ο όρος 'Open Source' καθιερώθηκε επίσημα το 1998 στην Καλιφόρνια με την ίδρυση της Open Source Initiative (OSI)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CE%B3%CE%B9%CF%83%CE%BC%CE%B9%CE%BA%CF%8C_%CE%B1%CE%BD%CE%BF%CE%B9%CE%BA%CF%84%CE%BF%CF%8D_%CE%BA%CF%8E%CE%B4%CE%B9%CE%BA%CE%B1",
    "locale": "el-GR",
    "tags": ["open-source", "software", "licensing", "programming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_090",
    "text": "Σε ποια αμερικανική πολιτεία βρίσκεται η περίφημη περιοχή «Silicon Valley», παγκόσμιο επίκεντρο εταιρειών τεχνολογίας;",
    "answers": ["Νέα Υόρκη", "Καλιφόρνια", "Τέξας", "Φλόριντα"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Silicon Valley (Κοιλάδα του Πυριτίου) βρίσκεται στη Βόρεια Καλιφόρνια, στην περιοχή του κόλπου του Σαν Φρανσίσκο, φιλοξενώντας κολοσσούς όπως η Apple, η Google και η Meta.",
    "funFacts": [
      "Ονομάστηκε έτσι λόγω του μεγάλου αριθμού κατασκευαστών ολοκληρωμένων κυκλωμάτων και τσιπ που χρησιμοποιούσαν πυρίτιο (silicon) ως ημιαγωγό.",
      "Ο όρος χρησιμοποιήθηκε για πρώτη φορά στον τύπο το 1971 από τον δημοσιογράφο Ντον Χόφλερ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%AF%CE%BB%CE%B9%CE%BA%CE%BF%CE%BD_%CE%92%CE%AC%CE%BB%CE%B5%CF%8A",
    "locale": "el-GR",
    "tags": ["silicon-valley", "california", "geography", "tech-industry"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_091",
    "text": "Πώς ονομάζεται το κακόβουλο λογισμικό που κλειδώνει τα αρχεία του υπολογιστή και ζητά χρηματικά λύτρα για την αποκρυπτογράφησή τους;",
    "answers": ["Adware", "Spyware", "Λογισμικό λύτρων (Ransomware)", "Freeware"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Ransomware χρησιμοποιεί ισχυρή κρυπτογράφηση για να καταστήσει απρόσιτα τα δεδομένα του θύματος, απαιτώντας πληρωμή (συνήθως σε Bitcoin) για το κλειδί επαναφοράς.",
    "funFacts": [
      "Μία από τις πιο καταστροφικές επιθέσεις ransomware στην ιστορία ήταν το 'WannaCry' το 2017, που μόλυνε πάνω από 200.000 υπολογιστές σε 150 χώρες.",
      "Οι ειδικοί κυβερνοασφάλειας συνιστούν πάντα τη διατήρηση τακτικών αντιγράφων ασφαλείας (backups) σε εξωτερικούς αποσυνδεδεμένους δίσκους."
    ],
    "source": "https://el.wikipedia.org/wiki/Ransomware",
    "locale": "el-GR",
    "tags": ["ransomware", "security", "malware", "cybersecurity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_092",
    "text": "Ποια μικρή πλαστική κάρτα με ενσωματωμένο μικροτσίπ τοποθετείται στο smartphone για τη σύνδεση και ταυτοποίηση στο δίκτυο κινητής τηλεφωνίας;",
    "answers": ["Κάρτα SD", "Κάρτα PCI", "Κάρτα γραφικών", "Κάρτα SIM"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η κάρτα SIM (Subscriber Identity Module) αποθηκεύει τον μοναδικό αριθμό ταυτότητας του συνδρομητή και το κλειδί πιστοποίησης στο δίκτυο.",
    "funFacts": [
      "Οι κάρτες SIM ξεκίνησαν το 1991 με μέγεθος πιστωτικής κάρτας, πριν συρρικνωθούν διαδοχικά σε Mini, Micro και Nano SIM.",
      "Σήμερα αντικαθίστανται σταδιακά από την τεχνολογία eSIM, ένα ψηφιακό τσιπ μόνιμα ενσωματωμένο στη μητρική πλακέτα του τηλεφώνου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%81%CF%84%CE%B1_SIM",
    "locale": "el-GR",
    "tags": ["sim", "mobile", "smartphones", "telecommunications"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_093",
    "text": "Ποιος θεωρείται ο πρώτος μεγάλης κλίμακας προγραμματιζόμενος ηλεκτρονικός ψηφιακός υπολογιστής γενικής χρήσης, που ολοκληρώθηκε στις ΗΠΑ το 1945;",
    "answers": ["ENIAC", "UNIVAC", "Colossus", "IBM PC"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο ENIAC (Electronic Numerical Integrator and Computer) κατασκευάστηκε στο Πανεπιστήμιο της Πενσυλβάνια και χρησιμοποιούσε χιλιάδες ηλεκτρονικές λυχνίες.",
    "funFacts": [
      "Ζύγιζε περισσότερους από 27 τόνους και καταλάμβανε χώρο περίπου 167 τετραγωνικών μέτρων.",
      "Σχεδιάστηκε αρχικά από τον στρατό των ΗΠΑ για τον ταχύ υπολογισμό πινάκων βολής πυροβολικού κατά τον Β' Παγκόσμιο Πόλεμο."
    ],
    "source": "https://el.wikipedia.org/wiki/ENIAC",
    "locale": "el-GR",
    "tags": ["eniac", "history", "computers", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_094",
    "text": "Ποιο εξάρτημα του υπολογιστή μετατρέπει το εναλλασσόμενο ηλεκτρικό ρεύμα (AC) της οικιακής πρίζας σε συνεχές ρεύμα (DC) χαμηλής τάσης;",
    "answers": ["Επεξεργαστής (CPU)", "Τροφοδοτικό (PSU)", "Μητρική πλακέτα", "Μονάδα ψύξης"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το τροφοδοτικό (Power Supply Unit - PSU) διανέμει την κατάλληλη ηλεκτρική ισχύ και τάση σε όλα τα εξαρτήματα του ηλεκτρονικού υπολογιστή.",
    "funFacts": [
      "Η ενεργειακή αποδοτικότητα των σύγχρονων τροφοδοτικών πιστοποιείται με το πρότυπο 80 PLUS (Bronze, Silver, Gold, Platinum, Titanium).",
      "Τα σύγχρονα τροφοδοτικά περιλαμβάνουν μηχανισμούς προστασίας από υπερτάσεις, βραχυκυκλώματα και υπερθέρμανση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%BF%CF%85%CE%BF%CE%B4%CE%BF%CF%84%CE%B9%CE%BA%CF%8C_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE%CF%82)",
    "locale": "el-GR",
    "tags": ["psu", "hardware", "power", "components"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_095",
    "text": "Ποιος είναι ο ελάχιστος αριθμός δορυφόρων GPS που πρέπει να λαμβάνει μια συσκευή για να υπολογίσει ακριβή τρισδιάστατη θέση και υψόμετρο;",
    "answers": ["1 δορυφόρος", "2 δορυφόροι", "4 δορυφόροι", "12 δορυφόροι"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Για τον ακριβή προσδιορισμό του γεωγραφικού πλάτους, μήκους, υψομέτρου και της χρονικής απόκλισης απαιτείται σήμα από τουλάχιστον 4 δορυφόρους GPS.",
    "funFacts": [
      "Η μέθοδος υπολογισμού της θέσης βασίζεται στη μαθηματική αρχή του τριπλευρισμού (trilateration).",
      "Ο πλήρης αστερισμός του GPS αποτελείται από τουλάχιστον 24 ενεργούς δορυφόρους που περιστρέφονται γύρω από τη Γη σε ύψος περίπου 20.200 χιλιομέτρων."
    ],
    "source": "https://el.wikipedia.org/wiki/GPS",
    "locale": "el-GR",
    "tags": ["gps", "navigation", "satellites", "physics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_096",
    "text": "Ποια υπηρεσία του διαδικτύου λειτουργεί σαν τηλεφωνικός κατάλογος, μεταφράζοντας ονόματα ιστοσελίδων σε αριθμητικές διευθύνσεις IP;",
    "answers": ["FTP", "DHCP", "SMTP", "DNS (Domain Name System)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το DNS (Σύστημα Ονομάτων Τομέα) μετατρέπει τις εύκολες στην απομνημόνευση διευθύνσεις (όπως el.wikipedia.org) στις αντίστοιχες αριθμητικές διευθύνσεις IP.",
    "funFacts": [
      "Εφευρέθηκε το 1983 από τον Πολ Μοκαπετρίς, επιτρέποντας στο διαδίκτυο να επεκταθεί χωρίς οι χρήστες να χρειάζεται να θυμούνται αριθμούς IP.",
      "Χωρίς το DNS, θα έπρεπε να πληκτρολογούμε πολύπλοκες σειρές αριθμών στον περιηγητή για να επισκεφθούμε οποιονδήποτε ιστότοπο."
    ],
    "source": "https://el.wikipedia.org/wiki/DNS",
    "locale": "el-GR",
    "tags": ["dns", "networking", "internet", "protocols"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_097",
    "text": "Ποιος όρος περιγράφει τις έξυπνες ηλεκτρονικές συσκευές που φοριούνται στο ανθρώπινο σώμα, όπως τα smartwatches και τα fitness trackers;",
    "answers": ["Φορετή τεχνολογία (Wearables)", "Υπερυπολογιστές", "Mainframes", "Διακομιστές"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Οι φορετές συσκευές (wearables) ενσωματώνουν αισθητήρες και μικροεπεξεργαστές για να καταγράφουν βιομετρικά δεδομένα και να παρέχουν ειδοποιήσεις.",
    "funFacts": [
      "Πολλά σύγχρονα smartwatches μπορούν να εκτελούν ηλεκτροκαρδιογράφημα (ΗΚΓ) και να ανιχνεύουν αυτόματα πτώσεις του χρήστη.",
      "Ένα από τα πρώτα ιστορικά wearables ήταν ένας μικροσκοπικός υπολογιστής κρυμμένος σε παπούτσι που κατασκεύασαν το 1961 μαθηματικοί για να προβλέπουν τη ρουλέτα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%BF%CF%81%CE%B5%CF%84%CF%8C%CF%82_%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["wearables", "smartwatch", "gadgets", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_098",
    "text": "Σε ποια ζώνη ραδιοσυχνοτήτων λειτουργεί κυρίως η ασύρματη επικοινωνία Bluetooth αλλά και τα περισσότερα οικιακά δίκτυα Wi-Fi;",
    "answers": ["100 kHz", "2,4 GHz", "50 MHz", "60 GHz"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το Bluetooth και τα κλασικά δίκτυα Wi-Fi λειτουργούν στη διεθνώς ελεύθερη ζώνη συχνοτήτων ISM στα 2,4 GHz (2.400 - 2.483,5 MHz).",
    "funFacts": [
      "Στην ίδια ακριβώς συχνότητα (2,4 GHz) λειτουργούν και οι οικιακοί φούρνοι μικροκυμάτων, γι' αυτό κακώς μονωμένοι φούρνοι μπορεί να προκαλέσουν παρεμβολές στο Wi-Fi.",
      "Για να αποφύγει τις παρεμβολές, το Bluetooth χρησιμοποιεί τεχνολογία αναπήδησης συχνότητας (frequency hopping) αλλάζοντας κανάλι έως και 1.600 φορές το δευτερόλεπτο."
    ],
    "source": "https://el.wikipedia.org/wiki/Bluetooth",
    "locale": "el-GR",
    "tags": ["bluetooth", "wifi", "frequencies", "wireless"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_099",
    "text": "Τι σημαίνουν τα αρχικά «AI» στην επιστήμη των υπολογιστών και την τεχνολογία;",
    "answers": ["Automated Internet", "Advanced Integration", "Artificial Intelligence (Τεχνητή Νοημοσύνη)", "Analog Information"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το AI (Artificial Intelligence - Τεχνητή Νοημοσύνη) αναφέρεται στην ικανότητα υπολογιστικών συστημάτων να εκτελούν εργασίες που απαιτούν ανθρώπινη νοημοσύνη.",
    "funFacts": [
      "Ο όρος καθιερώθηκε επίσημα το καλοκαίρι του 1956 στο ιστορικό συνέδριο του Κολλεγίου Ντάρτμουθ από τον Τζον Μακάρθι.",
      "Σήμερα η τεχνητή νοημοσύνη περιλαμβάνει τομείς όπως η μηχανική μάθηση, τα νευρωνικά δίκτυα, η μηχανική όραση και η επεξεργασία φυσικής γλώσσας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CF%87%CE%BD%CE%B7%CF%84%CE%AE_%CE%BD%CE%BF%CE%B7%CE%BC%CE%BF%CF%83%CF%8D%CE%BD%CE%B7",
    "locale": "el-GR",
    "tags": ["ai", "computer-science", "machine-learning", "definitions"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_100",
    "text": "Πώς ονομάζεται η διαδικασία ρύθμισης ενός επεξεργαστή ώστε να λειτουργεί σε υψηλότερη συχνότητα ρολογιού από την επίσημη εργοστασιακή;",
    "answers": ["Αποσφαλμάτωση (Debugging)", "Κρυπτογράφηση (Encryption)", "Εικονικοποίηση (Virtualization)", "Υπερχρονισμός (Overclocking)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το overclocking αυξάνει την ταχύτητα εκτέλεσης εντολών ενός επεξεργαστή ή κάρτας γραφικών, αλλά παράγει περισσότερη θερμότητα και απαιτεί ισχυρότερη ψύξη.",
    "funFacts": [
      "Οι λάτρεις του ακραίου overclocking χρησιμοποιούν συχνά υγρό άζωτο για να ψύξουν επεξεργαστές σε θερμοκρασίες κάτω από -190 βαθμούς Κελσίου.",
      "Το υπερβολικό overclocking χωρίς κατάλληλη ψύξη μπορεί να προκαλέσει αστάθεια στο σύστημα (μπλε οθόνες) ή μόνιμη βλάβη στο υλικό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%B5%CF%81%CF%87%CF%81%CE%BF%CE%BD%CE%B9%CF%83%CE%BC%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["overclocking", "hardware", "cpu", "performance"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_101",
    "text": "Ποιος γνωστός επιχειρηματίας είναι ο διευθύνων σύμβουλος της εταιρείας ηλεκτρικών αυτοκινήτων Tesla και ιδρυτής της διαστημικής SpaceX;",
    "answers": ["Έλον Μασκ", "Τζεφ Μπέζος", "Μαρκ Ζάκερμπεργκ", "Μπιλ Γκέιτς"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Έλον Μασκ (Elon Musk) ηγείται της Tesla, ίδρυσε τη διαστημική εταιρεία SpaceX το 2002 και εξαγόρασε την πλατφόρμα Twitter (νυν X) το 2022.",
    "funFacts": [
      "Συνίδρυσε την εταιρεία X.com το 1999, η οποία στη συνέχεια συγχωνεύτηκε και μετεξελίχθηκε στη διάσημη πύλη πληρωμών PayPal.",
      "Το 2018 εκτόξευσε στο διάστημα το προσωπικό του αυτοκίνητο Tesla Roadster ως φορτίο δοκιμής στον πρώτο πύραυλο Falcon Heavy."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BB%CE%BF%CE%BD_%CE%9C%CE%B1%CF%83%CE%BA",
    "locale": "el-GR",
    "tags": ["elon-musk", "tesla", "spacex", "entrepreneurs"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_102",
    "text": "Πώς ονομάζεται το βασικό υλικολογισμικό (firmware) αποθηκευμένο στη μητρική πλακέτα που αρχικοποιεί το υλικό κατά το άνοιγμα του υπολογιστή;",
    "answers": ["Κερνέλ (Kernel)", "BIOS / UEFI", "Οδηγός (Driver)", "Πρωτόκολλο (Protocol)"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το BIOS (Basic Input/Output System) και ο σύγχρονος διάδοχός του UEFI είναι το πρώτο λογισμικό που εκτελείται για να ελέγξει το υλικό και να εκκινήσει το λειτουργικό σύστημα.",
    "funFacts": [
      "Η διαδικασία αυτοελέγχου που εκτελεί κατά το άνοιγμα του υπολογιστή ονομάζεται POST (Power-On Self-Test).",
      "Το νεότερο πρότυπο UEFI αντικατέστησε το παραδοσιακό BIOS προσφέροντας ταχύτερη εκκίνηση, υποστήριξη για ποντίκι και ασφαλή εκκίνηση (Secure Boot)."
    ],
    "source": "https://el.wikipedia.org/wiki/BIOS",
    "locale": "el-GR",
    "tags": ["bios", "uefi", "firmware", "motherboard"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_103",
    "text": "Ποια είναι η πιο διαδεδομένη συντόμευση πληκτρολογίου στα λειτουργικά συστήματα Windows για την αντιγραφή (Copy) επιλεγμένου κειμένου ή αρχείου;",
    "answers": ["Ctrl + V", "Ctrl + X", "Ctrl + C", "Ctrl + Z"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η συντόμευση πληκτρολογίου Ctrl + C (ή Command + C στο macOS) αντιγράφει το επιλεγμένο περιεχόμενο στο πρόχειρο (clipboard).",
    "funFacts": [
      "Η εντολή αποκοπής/αντιγραφής/επικόλλησης (Cut/Copy/Paste) επινοήθηκε από τον επιστήμονα Λάρι Τέσλερ στα εργαστήρια της Xerox PARC τη δεκαετία του 1970.",
      "Το γράμμα 'C' επιλέχθηκε προφανώς ως το αρχικό γράμμα της αγγλικής λέξης 'Copy'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CE%BF%CE%BA%CE%BF%CF%80%CE%AE,_%CE%B1%CE%BD%CF%84%CE%B9%CE%B3%CF%81%CE%B1%CF%86%CE%AE,_%CE%B5%CF%80%CE%B9%CE%BA%CF%8C%CE%BB%CE%BB%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["shortcuts", "keyboard", "windows", "productivity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_104",
    "text": "Ποια είναι η καθιερωμένη συντόμευση πληκτρολογίου στα Windows για την επικόλληση (Paste) του περιεχομένου από το πρόχειρο;",
    "answers": ["Ctrl + P", "Ctrl + S", "Ctrl + A", "Ctrl + V"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η συντόμευση Ctrl + V (ή Command + V στο macOS) επικολλά τα δεδομένα που βρίσκονται αποθηκευμένα στο πρόχειρο στο επιλεγμένο σημείο.",
    "funFacts": [
      "Το 'V' επιλέχθηκε επειδή βρίσκεται ακριβώς δίπλα στα πλήκτρα 'X' (αποκοπή) και 'C' (αντιγραφή) στα πληκτρολόγια QWERTY.",
      "Η συντόμευση Ctrl + P χρησιμοποιείται διεθνώς για την εκτύπωση (Print) ενός εγγράφου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CE%BF%CE%BA%CE%BF%CF%80%CE%AE,_%CE%B1%CE%BD%CF%84%CE%B9%CE%B3%CF%81%CE%B1%CF%86%CE%AE,_%CE%B5%CF%80%CE%B9%CE%BA%CF%8C%CE%BB%CE%BB%CE%B7%CF%83%CE%B7",
    "locale": "el-GR",
    "tags": ["shortcuts", "keyboard", "windows", "productivity"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_105",
    "text": "Ποια τεχνολογία χρησιμοποιεί ειδικές μάσκες ή κράνη με οθόνες για να μεταφέρει τον χρήστη σε έναν εξ ολοκλήρου ψηφιακό τεχνητό κόσμο 360 μοιρών;",
    "answers": ["Εικονική Πραγματικότητα (VR)", "Επαυξημένη Πραγματικότητα (AR)", "Ολογραφία", "Στερεοσκοπική Φωτογραφία"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Εικονική Πραγματικότητα (Virtual Reality - VR) απομονώνει τον χρήστη από το φυσικό περιβάλλον και δημιουργεί την ψευδαίσθηση πλήρους φυσικής παρουσίας σε έναν ψηφιακό κόσμο.",
    "funFacts": [
      "Ο όρος 'Virtual Reality' διαδόθηκε ευρέως στα τέλη της δεκαετίας του 1980 από τον πρωτοπόρο Τζάρον Λάνιερ.",
      "Οι σύγχρονες συσκευές VR χρησιμοποιούν αισθητήρες 6 DoF (έξι βαθμών ελευθερίας), καταγράφοντας τόσο την περιστροφή όσο και τη μετακίνηση του κεφαλιού στον χώρο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B9%CE%BA%CE%BF%CE%BD%CE%B9%CE%BA%CE%AE_%CF%80%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["vr", "virtual-reality", "gaming", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_106",
    "text": "Ποια τεχνολογία επικαλύπτει ψηφιακά στοιχεία και πληροφορίες πάνω στον πραγματικό κόσμο μέσω κάμερας (όπως στο παιχνίδι Pokémon GO);",
    "answers": ["Εικονική Πραγματικότητα (VR)", "Επαυξημένη Πραγματικότητα (AR)", "Υπολογιστικό Νέφος", "Τηλεδιάσκεψη"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η Επαυξημένη Πραγματικότητα (Augmented Reality - AR) συνδυάζει τον πραγματικό φυσικό κόσμο με ψηφιακές εικόνες και δεδομένα σε πραγματικό χρόνο.",
    "funFacts": [
      "Το παγκόσμιο φαινόμενο Pokémon GO το 2016 έφερε την τεχνολογία AR στα χέρια εκατοντάδων εκατομμυρίων κατόχων smartphones.",
      "Εκτός από τα παιχνίδια, η τεχνολογία AR χρησιμοποιείται ευρύτατα στην ιατρική χειρουργική, την αρχιτεκτονική και τη ναυσιπλοΐα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B1%CF%85%CE%BE%CE%B7%CE%BC%CE%AD%CE%BD%CE%B7_%CF%80%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["ar", "augmented-reality", "mobile", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_107",
    "text": "Πώς ονομάζεται η διαδικασία επανεκκίνησης ενός υπολογιστή ή συστήματος που καθαρίζει τη μνήμη RAM και φορτώνει ξανά το λειτουργικό σύστημα;",
    "answers": ["Ανασυγκρότηση (Defrag)", "Διαμόρφωση (Format)", "Επανεκκίνηση (Reboot / Restart)", "Αρχειοθέτηση (Zip)"],
    "correctAnswerIndex": 2,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Η επανεκκίνηση (reboot) τερματίζει όλες τις τρέχουσες διεργασίες και φορτώνει εκ νέου το σύστημα, λύνοντας πολλά προσωρινά σφάλματα λογισμικού.",
    "funFacts": [
      "Ο όρος 'boot' προέρχεται από την παλιά αγγλική έκφραση 'to pull oneself up by one's bootstraps' (να σηκωθεί κανείς τραβώντας τα κορδόνια των μποτών του).",
      "Στα Windows, ο ιστορικός συνδυασμός Ctrl + Alt + Delete επινοήθηκε από τον μηχανικό Ντέιβιντ Μπράντλεϊ της IBM για γρήγορη επανεκκίνηση χωρίς κλείσιμο του ρεύματος."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BA%CE%BA%CE%AF%CE%BD%CE%B7%CF%83%CE%B7_%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE",
    "locale": "el-GR",
    "tags": ["reboot", "computers", "operating-systems", "troubleshooting"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_108",
    "text": "Πώς ονομάζεται ένας κεντρικός υπολογιστής που παρέχει δεδομένα, αρχεία, ιστοσελίδες ή άλλες υπηρεσίες σε υπολογιστές-πελάτες (clients) μέσω δικτύου;",
    "answers": ["Router", "Μόντεμ", "Πληκτρολόγιο", "Διακομιστής (Server)"],
    "correctAnswerIndex": 3,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο διακομιστής (server) είναι ένα υπολογιστικό σύστημα σχεδιασμένο να εξυπηρετεί αιτήματα πολλών χρηστών και συσκευών συνεχώς χωρίς διακοπή.",
    "funFacts": [
      "Οι μεγάλοι διακομιστές του διαδικτύου στεγάζονται σε τεράστια εξειδικευμένα κέντρα δεδομένων (data centers) με προηγμένα συστήματα κλιματισμού και αδιάλειπτης τροφοδοσίας.",
      "Ο πρώτος διακομιστής ιστού (web server) στον κόσμο ήταν ένας υπολογιστής NeXTcube που χρησιμοποίησε ο Τιμ Μπέρνερς-Λι στο CERN το 1990."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B1%CE%BA%CE%BF%CE%BC%CE%B9%CF%83%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["server", "networking", "internet", "hardware"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_109",
    "text": "Ποιο ψηφιακό πρότυπο σύνδεσης οθόνης αναπτύχθηκε από την κοινοπραξία VESA και χρησιμοποιείται ευρύτατα σε κάρτες γραφικών υπολογιστών δίπλα στο HDMI;",
    "answers": ["DisplayPort", "SCART", "Composite Video", "S-Video"],
    "correctAnswerIndex": 0,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Το DisplayPort είναι ένα ψηφιακό πρότυπο διεπαφής που σχεδιάστηκε κυρίως για τη σύνδεση υπολογιστών με σύγχρονες οθόνες υψηλής ανάλυσης και υψηλού ρυθμού ανανέωσης.",
    "funFacts": [
      "Υποστηρίζει τεχνολογία πολλαπλών οθονών (Multi-Stream Transport) επιτρέποντας τη σύνδεση πολλών οθονών σε σειρά από μία μόνο θύρα.",
      "Σε αντίθεση με το HDMI, το DisplayPort είναι πρότυπο χωρίς καταβολή δικαιωμάτων εκμετάλλευσης (royalty-free) για τους κατασκευαστές."
    ],
    "source": "https://el.wikipedia.org/wiki/DisplayPort",
    "locale": "el-GR",
    "tags": ["displayport", "hardware", "monitors", "video"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "technology_easy_110",
    "text": "Ποιος ταλαντούχος ηλεκτρονικός μηχανικός και συνιδρυτής της Apple σχεδίασε μόνος του τα κυκλώματα των υπολογιστών Apple I και Apple II;",
    "answers": ["Τιμ Κουκ", "Στιβ Βόζνιακ", "Μπιλ Γκέιτς", "Πολ Άλεν"],
    "correctAnswerIndex": 1,
    "categoryId": "technology",
    "difficulty": 1,
    "explanation": "Ο Στιβ Βόζνιακ (Steve Wozniak, γνωστός και ως 'Woz') σχεδίασε ιδιοφυώς από το μηδέν το υλικό και το λογισμικό του Apple I και του θρυλικού Apple II.",
    "funFacts": [
      "Ο Apple II έγινε ένας από τους πιο επιτυχημένους εμπορικά μαζικούς προσωπικούς υπολογιστές της δεκαετίας του 1970 και 1980.",
      "Για να συγκεντρώσουν το αρχικό κεφάλαιο ίδρυσης της Apple το 1976, ο Βόζνιακ πούλησε τον επιστημονικό του υπολογιστή HP-65 και ο Στιβ Τζομπς το φορτηγάκι του Volkswagen."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B9%CE%B2_%CE%92%CF%8C%CE%B6%CE%BD%CE%B9%CE%B1%CE%BA",
    "locale": "el-GR",
    "tags": ["steve-wozniak", "apple", "hardware", "pioneers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    print(f"Total questions to append: {len(questions)}")
    validate_and_append('technology', 'easy', 1, questions)

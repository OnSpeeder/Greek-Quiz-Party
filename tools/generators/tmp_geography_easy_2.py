# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "geography_easy_061",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Κούβας;",
    "answers": ["Αβάνα", "Σαντιάγο ντε Κούμπα", "Καμαγουέι", "Ολγκίν"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Αβάνα είναι η πρωτεύουσα, η μεγαλύτερη πόλη και το κύριο εμπορικό λιμάνι της Κούβας.",
    "funFacts": [
      "Η Παλιά Αβάνα (Habana Vieja) έχει ανακηρυχθεί Μνημείο Παγκόσμιας Κληρονομιάς της UNESCO χάρη στην πλούσια αποικιακή αρχιτεκτονική της.",
      "Η πόλη ιδρύθηκε από τους Ισπανούς κατακτητές το 1519."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%B2%CE%AC%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["cuba", "havana", "capitals", "caribbean"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_062",
    "text": "Σε ποια χώρα βρίσκεται το διάσημο προϊστορικό μεγαλιθικό μνημείο Στόουνχεντζ;",
    "answers": ["Ιρλανδία", "Ηνωμένο Βασίλειο", "Γαλλία", "Γερμανία"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Στόουνχεντζ βρίσκεται στην κομητεία του Ουίλτσιρ στη νοτιοδυτική Αγγλία του Ηνωμένου Βασιλείου.",
    "funFacts": [
      "Χρονολογείται μεταξύ 3000 π.Χ. και 2000 π.Χ. και οι ογκόλιθοί του ευθυγραμμίζονται με το θερινό και χειμερινό ηλιοστάσιο.",
      "Ορισμένοι από τους λίθους του (οι 'μπλε λίθοι') μεταφέρθηκαν από απόσταση άνω των 200 χιλιομέτρων από την Ουαλία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CF%8C%CE%BF%CF%85%CE%BD%CF%87%CE%B5%CE%BD%CF%84%CE%B6",
    "locale": "el-GR",
    "tags": ["stonehenge", "uk", "landmarks", "monuments"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_063",
    "text": "Ποιος είναι ο τρίτος μεγαλύτερος σε έκταση ωκεανός της Γης;",
    "answers": ["Ατλαντικός Ωκεανός", "Αρκτικός Ωκεανός", "Ινδικός Ωκεανός", "Νότιος Ωκεανός"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Ινδικός Ωκεανός καλύπτει περίπου το 20% της συνολικής υδάτινης επιφάνειας του πλανήτη.",
    "funFacts": [
      "Βρέχει την Ασία στα βόρεια, την Αφρική στα δυτικά, την Αυστραλία στα ανατολικά και τον Νότιο Ωκεανό στα νότια.",
      "Είναι ο θερμότερος ωκεανός στον κόσμο, γεγονός που περιορίζει τη συγκέντρωση φυτοπλαγκτού στα τροπικά του νερά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%BD%CE%B4%CE%B9%CE%BA%CF%8C%CF%82_%CF%89%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["indian-ocean", "oceans", "earth"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_064",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ουγγαρίας;",
    "answers": ["Ντέμπρετσεν", "Σέγκεντ", "Μίσκολτ", "Βουδαπέστη"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βουδαπέστη δημιουργήθηκε το 1873 από την ένωση των ιστορικών πόλεων Βούδα, Πέστη και Όβουντα εκατέρωθεν του Δούναβη.",
    "funFacts": [
      "Φημίζεται ως η 'Πόλη των Ιαματικών Λουτρών' χάρη στις περισσότερες από 100 φυσικές θερμές πηγές της.",
      "Το κτίριο του Ουγγρικού Κοινοβουλίου στις όχθες του Δούναβη είναι ένα από τα μεγαλύτερα κοινοβουλευτικά κτίρια στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%BF%CF%85%CE%B4%CE%B1%CF%80%CE%AD%CF%83%CF%84%CE%B7",
    "locale": "el-GR",
    "tags": ["hungary", "budapest", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_065",
    "text": "Ποιο είναι το ψηλότερο ενεργό ηφαίστειο στην ευρωπαϊκή ήπειρο;",
    "answers": ["Αίτνα", "Βεζούβιος", "Στρόμπολι", "Σαντορίνη"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Αίτνα στην ανατολική ακτή της Σικελίας ξεπερνά σε υψόμετρο τα 3.300 μέτρα.",
    "funFacts": [
      "Βρίσκεται σε σχεδόν συνεχή κατάσταση ηφαιστειακής δραστηριότητας εδώ και χιλιάδες χρόνια.",
      "Παρά τις συχνές εκρήξεις, οι πλαγιές της καλλιεργούνται εντατικά λόγω του εξαιρετικά εύφορου ηφαιστειακού εδάφους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%AF%CF%84%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["etna", "volcanoes", "italy", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_066",
    "text": "Ποια χώρα της Νότιας Αμερικής έχει χαρακτηριστικό στενόμακρο σχήμα κατά μήκος των ακτών του Ειρηνικού;",
    "answers": ["Αργεντινή", "Χιλή", "Περού", "Βολιβία"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Χιλή εκτείνεται σε μήκος άνω των 4.200 χιλιομέτρων από βορρά προς νότο, ενώ το μέσο πλάτος της είναι μόλις 177 χιλιόμετρα.",
    "funFacts": [
      "Είναι η μακρύτερη και στενότερη χώρα στον κόσμο.",
      "Λόγω του τεράστιου γεωγραφικού της μήκους περιλαμβάνει από την υπεράνυδρη έρημο Ατακάμα μέχρι τους παγετώνες της Παταγονίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B9%CE%BB%CE%AE",
    "locale": "el-GR",
    "tags": ["chile", "south-america", "geography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_067",
    "text": "Ποια είναι η πρωτεύουσα της Τσεχίας;",
    "answers": ["Μπρνο", "Οστράβα", "Πράγα", "Πίλζεν"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Πράγα είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Τσεχίας, χτισμένη στις όχθες του ποταμού Μολδάβα (Vltava).",
    "funFacts": [
      "Αποκαλείται συχνά 'Η Χρυσή Πόλη' ή 'Η Πόλη των Εκατό Πύργων' λόγω των αναρίθμητων ιστορικών καμπαναριών της.",
      "Το Αστρονομικό Ρολόι της Πράγας, που εγκαταστάθηκε το 1410, είναι το παλαιότερο ακόμα λειτουργικό αστρονομικό ρολόι στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CE%AC%CE%B3%CE%B1",
    "locale": "el-GR",
    "tags": ["czechia", "prague", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_068",
    "text": "Σε ποια χώρα βρίσκεται το κολοσσιαίο άγαλμα του Χριστού Λυτρωτή στο Ρίο ντε Τζανέιρο;",
    "answers": ["Αργεντινή", "Χιλή", "Κολομβία", "Βραζιλία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το άγαλμα του Χριστού Λυτρωτή δεσπόζει στην κορυφή του λόφου Κορκοβάντο στο Ρίο ντε Τζανέιρο της Βραζιλίας.",
    "funFacts": [
      "Έχει ύψος 30 μέτρα (χωρίς το βάθρο 8 μέτρων) και το άνοιγμα των χεριών του φτάνει τα 28 μέτρα.",
      "Το 2007 ψηφίστηκε ως ένα από τα Νέα Επτά Θαύματα του Κόσμου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CF%81%CE%B9%CF%83%CF%84%CF%8C%CF%82_%CE%9B%CF%85%CF%84%CF%81%CF%89%CF%84%CE%AE%CF%82",
    "locale": "el-GR",
    "tags": ["brazil", "rio", "monuments", "landmarks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_069",
    "text": "Ποια ευρωπαϊκή χώρα είναι διεθνώς φημισμένη για τα εντυπωσιακά παράκτια φιόρδ της;",
    "answers": ["Νορβηγία", "Σουηδία", "Φινλανδία", "Δανία"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η ακτογραμμή της Νορβηγίας διαθέτει πάνω από 1.000 καταγεγραμμένα φιόρδ που λαξεύτηκαν από παγετώνες κατά την Εποχή των Παγετώνων.",
    "funFacts": [
      "Το φιόρδ Σόγκνεφιορντ είναι το μεγαλύτερο και βαθύτερο φιόρδ της Νορβηγίας, με μήκος 205 χιλιόμετρα.",
      "Αν συνυπολογιστούν όλες οι εσοχές των φιόρδ και των νησιών, η ακτογραμμή της Νορβηγίας ξεπερνά τα 100.000 χιλιόμετρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%BF%CF%81%CE%B2%CE%B7%CE%B3%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["norway", "fjords", "geography", "scandinavia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_070",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ινδίας;",
    "answers": ["Βομβάη", "Νέο Δελχί", "Καλκούτα", "Μπανγκαλόρ"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Νέο Δελχί αποτελεί την επίσημη έδρα της κυβέρνησης και την ομοσπονδιακή πρωτεύουσα της Δημοκρατίας της Ινδίας.",
    "funFacts": [
      "Σχεδιάστηκε στις αρχές του 20ού αιώνα από τους Βρετανούς αρχιτέκτονες Έντουιν Λάτυενς και Χέρμπερτ Μπέικερ.",
      "Αποτελεί τμήμα της ευρύτερης μητροπολιτικής περιοχής του Δελχί, μιας από τις πολυπληθέστερες στον πλανήτη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AD%CE%BF_%CE%94%CE%B5%CE%BB%CF%87%CE%AF",
    "locale": "el-GR",
    "tags": ["india", "new-delhi", "capitals", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_071",
    "text": "Ποια χώρα αποκαλείται συχνά «Το Εξάγωνο» (L'Hexagone) λόγω του γεωγραφικού της περιγράμματος;",
    "answers": ["Γερμανία", "Ισπανία", "Γαλλία", "Βέλγιο"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το σχήμα της ηπειρωτικής Γαλλίας προσεγγίζει ένα κανονικό εξάγωνο, όρος που χρησιμοποιείται ευρύτατα στη γαλλική γλώσσα.",
    "funFacts": [
      "Τρεις από τις έξι πλευρές του εξαγώνου βρέχονται από θάλασσα και οι άλλες τρεις οριοθετούνται από χερσαία σύνορα.",
      "Η Γαλλία είναι η μεγαλύτερη σε έκταση χώρα της Ευρωπαϊκής Ένωσης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B1%CE%BB%CE%BB%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["france", "hexagone", "europe", "geography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_072",
    "text": "Ποιος ποταμός διασχίζει την πόλη του Παρισιού χωρίζοντάς την στην «Αριστερή» και «Δεξιά Όχθη»;",
    "answers": ["Λίγηρας", "Ροδανός", "Γαρούνας", "Σηκουάνας"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Σηκουάνας έχει μήκος περίπου 777 χιλιόμετρα και ρέει μέσα από την καρδιά του Παρισιού πριν εκβάλει στη Μάγχη.",
    "funFacts": [
      "Στο μέσο του Σηκουάνα στο Παρίσι βρίσκεται το νησάκι Ιλ ντε λα Σιτέ, όπου δεσπόζει η Παναγία των Παρισίων.",
      "Οι ιστορικές όχθες του Σηκουάνα στο Παρίσι αποτελούν Μνημείο Παγκόσμιας Κληρονομιάς της UNESCO από το 1991."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B7%CE%BA%CE%BF%CF%85%CE%AC%CE%BD%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["seine", "paris", "rivers", "france"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_073",
    "text": "Ποια πόλη είναι η ιστορική πρωτεύουσα της Σκωτίας;",
    "answers": ["Εδιμβούργο", "Γλασκώβη", "Αμπερντίν", "Νταντί"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Εδιμβούργο αναγνωρίζεται ως πρωτεύουσα της Σκωτίας τουλάχιστον από τον 15ο αιώνα και φιλοξενεί το Σκωτσέζικο Κοινοβούλιο.",
    "funFacts": [
      "Το επιβλητικό Κάστρο του Εδιμβούργου δεσπόζει στην κορυφή ενός αρχαίου σβησμένου ηφαιστειακού βράχου.",
      "Υπήρξε η πρώτη πόλη στον κόσμο που απέκτησε οργανωμένη δημοτική πυροσβεστική υπηρεσία το 1824."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B4%CE%B9%CE%BC%CE%B2%CE%BF%CF%8D%CF%81%CE%B3%CE%BF",
    "locale": "el-GR",
    "tags": ["scotland", "edinburgh", "capitals", "uk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_074",
    "text": "Ποιο είναι το μεγαλύτερο νησιωτικό κράτος της Αφρικής στον Ινδικό Ωκεανό, διάσημο για τους λεμούριούς του;",
    "answers": ["Σρι Λάνκα", "Μαδαγασκάρη", "Μαυρίκιος", "Σεϋχέλλες"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μαδαγασκάρη είναι το τέταρτο μεγαλύτερο νησί στον κόσμο και αποκόπηκε από την ινδική υποήπειρο πριν από περίπου 88 εκατομμύρια χρόνια.",
    "funFacts": [
      "Πάνω από το 90% της χλωρίδας και της πανίδας της Μαδαγασκάρης δεν υπάρχει πουθενά αλλού στη Γη.",
      "Είναι παγκοσμίως γνωστή για τα εντυπωσιακά αιωνόβια δέντρα μπαομπάμπ και τη διάσημη 'Λεωφόρο των Μπαομπάμπ'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%B4%CE%B1%CE%B3%CE%B1%CF%83%CE%BA%CE%AC%CF%81%CE%B7",
    "locale": "el-GR",
    "tags": ["madagascar", "islands", "africa", "indian-ocean"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_075",
    "text": "Ποια είναι η πρωτεύουσα της Κυπριακής Δημοκρατίας;",
    "answers": ["Λεμεσός", "Λάρνακα", "Λευκωσία", "Πάφος"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Λευκωσία βρίσκεται στο κέντρο του νησιού της Κύπρου, στην πεδιάδα της Μεσαορίας.",
    "funFacts": [
      "Είναι η μοναδική διαιρεμένη πρωτεύουσα στον κόσμο, διαχωρισμένη από την Πράσινη Γραμμή του ΟΗΕ από το 1974.",
      "Περιβάλλεται από επιβλητικά ενετικά τείχη σε σχήμα άστρου με έντεκα προμαχώνες, χτισμένα τον 16ο αιώνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B5%CF%85%CE%BA%CF%89%CF%83%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["cyprus", "nicosia", "capitals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_076",
    "text": "Σε ποια χώρα της Μέσης Ανατολής βρίσκεται η αρχαία πόλη της Πέτρας, λαξευμένη στους ροδόχρωμους βράχους;",
    "answers": ["Αίγυπτος", "Ισραήλ", "Συρία", "Ιορδανία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Πέτρα ήταν η ιστορική πρωτεύουσα του βασιλείου των Ναβαταίων και βρίσκεται στη νοτιοδυτική Ιορδανία.",
    "funFacts": [
      "Αποκαλείται συχνά 'Η Ροδόχρωμη Πόλη' λόγω του φυσικού χρώματος των ψαμμιτικών πετρωμάτων στα οποία λαξεύτηκε.",
      "Η πρόσβαση στην πόλη γίνεται μέσα από ένα εντυπωσιακό στενό φαράγγι μήκους άνω του ενός χιλιομέτρου, το Σικ (Siq)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%AD%CF%84%CF%81%CE%B1_(%CE%99%CE%BF%CF%81%CE%B4%CE%B1%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["petra", "jordan", "landmarks", "monuments"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_077",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Σερβίας;",
    "answers": ["Βελιγράδι", "Νόβι Σαντ", "Νις", "Κραγκούγιεβατς"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Βελιγράδι είναι χτισμένο στη συμβολή των ποταμών Σάβου και Δούναβη και αποτελεί την πρωτεύουσα της Σερβίας.",
    "funFacts": [
      "Το όνομά του σημαίνει κυριολεκτικά 'Λευκή Πόλη'.",
      "Είναι μία από τις παλαιότερες συνεχώς κατοικημένες πόλεις της Ευρώπης, με ίχνη οικισμών της νεολιθικής περιόδου Βίντσα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B5%CE%BB%CE%B9%CE%B3%CF%81%CE%AC%CE%B4%CE%B9",
    "locale": "el-GR",
    "tags": ["serbia", "belgrade", "capitals", "balkans"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_078",
    "text": "Ποια οροσειρά αποτελεί το φυσικό σύνορο μεταξύ Γαλλίας και Ισπανίας;",
    "answers": ["Άλπεις", "Πυρηναία", "Απέννινα", "Καρπάθια"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Τα Πυρηναία εκτείνονται σε μήκος περίπου 430 χιλιομέτρων από τον Ατλαντικό Ωκεανό μέχρι τη Μεσόγειο Θάλασσα.",
    "funFacts": [
      "Μέσα στην οροσειρά των Πυρηναίων βρίσκεται φωλιασμένο το ανεξάρτητο πριγκιπάτο της Ανδόρρας.",
      "Η ψηλότερη κορυφή τους είναι το Ανέτο (Aneto), με υψόμετρο 3.404 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%85%CF%81%CE%B7%CE%BD%CE%B1%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["pyrenees", "mountains", "france", "spain", "borders"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_079",
    "text": "Ποιο νησιωτικό κράτος της Καραϊβικής έχει πρωτεύουσα το Κίνγκστον;",
    "answers": ["Κούβα", "Μπαχάμες", "Τζαμάικα", "Αϊτή"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Τζαμάικα είναι νησί των Μεγάλων Αντιλλών στην Καραϊβική με πρωτεύουσα το Κίνγκστον.",
    "funFacts": [
      "Είναι η γενέτειρα της μουσικής ρέγκε και του παγκόσμιου θρύλου Μπομπ Μάρλεϊ.",
      "Το όνομα Τζαμάικα προέρχεται από την αυτόχθονη λέξη των Ταΐνο 'Xaymaca', που σημαίνει 'γη του ξύλου και του νερού'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%B1%CE%BC%CE%AC%CE%B9%CE%BA%CE%B1",
    "locale": "el-GR",
    "tags": ["jamaica", "caribbean", "islands", "capitals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_080",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ρουμανίας;",
    "answers": ["Κλουζ-Ναπόκα", "Τιμισοάρα", "Ιάσιο", "Βουκουρέστι"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Βουκουρέστι είναι η πρωτεύουσα και το μεγαλύτερο οικονομικό κέντρο της Ρουμανίας.",
    "funFacts": [
      "Στις αρχές του 20ού αιώνα ήταν γνωστό ως 'Το Μικρό Παρίσι της Ανατολής' χάρη στην κομψή αρχιτεκτονική του.",
      "Στο Βουκουρέστι βρίσκεται το Παλάτι του Κοινοβουλίου, το δεύτερο μεγαλύτερο διοικητικό κτίριο στον κόσμο μετά το Πεντάγωνο των ΗΠΑ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%BF%CF%85%CE%BA%CE%BF%CF%85%CF%81%CE%AD%CF%83%CF%84%CE%B9",
    "locale": "el-GR",
    "tags": ["romania", "bucharest", "capitals", "balkans"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_081",
    "text": "Ποιος διάσημος ποταμός των ΗΠΑ εκβάλλει στον Κόλπο του Μεξικού κοντά στη Νέα Ορλεάνη;",
    "answers": ["Μισισιπής", "Κολοράντο", "Χάντσον", "Ρίο Γκράντε"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο ποταμός Μισισιπής διασχίζει το κεντρικό τμήμα των Ηνωμένων Πολιτειών και είναι ένας από τους μεγαλύτερους υδάτινους δρόμους της Βόρειας Αμερικής.",
    "funFacts": [
      "Η λεκάνη απορροής του Μισισιπή καλύπτει περίπου το 40% της επικράτειας των ηπειρωτικών ΗΠΑ.",
      "Το όνομά του προέρχεται από τη γλώσσα των ιθαγενών Οτζίμπουε (misi-ziibi), που σημαίνει 'Μεγάλος Ποταμός'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CF%83%CE%B9%CF%83%CE%B9%CF%80%CE%AE%CF%82_(%CF%80%CE%BF%CF%84%CE%B1%CE%BC%CF%8C%CF%82)",
    "locale": "el-GR",
    "tags": ["mississippi", "rivers", "usa", "north-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_082",
    "text": "Ποια είναι η πρωτεύουσα της Κροατίας;",
    "answers": ["Σπλιτ", "Ζάγκρεμπ", "Ντουμπρόβνικ", "Ριέκα"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ζάγκρεμπ βρίσκεται στις όχθες του ποταμού Σάβου και στις πλαγιές του όρους Μεντβέντνιτσα, αποτελώντας την πρωτεύουσα της Κροατίας.",
    "funFacts": [
      "Η πόλη χωρίζεται στην Άνω Πόλη (Gornji Grad), με ιστορικά μεσαιωνικά κτίρια, και την Κάτω Πόλη (Donji Grad).",
      "Στο Ζάγκρεμπ λειτουργεί το ιδιόρρυθμο και διεθνώς βραβευμένο 'Μουσείο Ραγισμένων Σχέσεων'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%AC%CE%B3%CE%BA%CF%81%CE%B5%CE%BC%CF%80",
    "locale": "el-GR",
    "tags": ["croatia", "zagreb", "capitals", "balkans"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_083",
    "text": "Ποια ευρωπαϊκή χώρα είναι παραδοσιακά γνωστή για τους ανεμόμυλους και τις καλλιέργειες τουλίπας;",
    "answers": ["Βέλγιο", "Δανία", "Ολλανδία", "Λουξεμβούργο"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ολλανδία είναι ο μεγαλύτερος εξαγωγέας τουλιπών στον κόσμο και διαθέτει εκατοντάδες ιστορικούς ανεμόμυλους.",
    "funFacts": [
      "Τον 17ο αιώνα στην Ολλανδία ξέσπασε η περίφημη 'Τουλιπομανία', η πρώτη καταγεγραμμένη κερδοσκοπική οικονομική φούσκα στην ιστορία.",
      "Περίπου το ένα τέταρτο της χώρας βρίσκεται κάτω από το επίπεδο της θάλασσας, προστατευμένο από ένα σύστημα αναχωμάτων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CE%BB%CE%B1%CE%BD%CE%B4%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["netherlands", "culture", "geography", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_084",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Βουλγαρίας;",
    "answers": ["Φιλιππούπολη", "Βάρνα", "Μπουργκάς", "Σόφια"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Σόφια βρίσκεται στους πρόποδες του όρους Βίτοσα και είναι η πρωτεύουσα και η πολυπληθέστερη πόλη της Βουλγαρίας.",
    "funFacts": [
      "Το σύνθημα της πόλης είναι 'Μεγαλώνει, αλλά δεν γερνά' (Raste, no ne staree).",
      "Ο καθεδρικός ναός του Αλεξάνδρου Νιέφσκι στη Σόφια είναι ένας από τους μεγαλύτερους ορθόδοξους ναούς στα Βαλκάνια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%8C%CF%86%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["bulgaria", "sofia", "capitals", "balkans"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_085",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Αλβανίας;",
    "answers": ["Τίρανα", "Δυρράχιο", "Αυλώνας", "Σκόδρα"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Τα Τίρανα ανακηρύχθηκαν πρωτεύουσα της Αλβανίας το 1920 και αποτελούν το διοικητικό και πολιτιστικό κέντρο της χώρας.",
    "funFacts": [
      "Στο κέντρο της πόλης δεσπόζει η τεράστια πλατεία Σκεντέρμπεη με το ομώνυμο άγαλμα του εθνικού ήρωα Γεωργίου Καστριώτη.",
      "Στα Τίρανα πολλά κτίρια της κομμουνιστικής εποχής βάφτηκαν με έντονα φωτεινά χρώματα για να αλλάξει η όψη της πόλης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AF%CF%81%CE%B1%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["albania", "tirana", "capitals", "balkans"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_086",
    "text": "Ποιο είναι το μεγαλύτερο σε έκταση νησί της Καραϊβικής Θάλασσας;",
    "answers": ["Ισπανιόλα", "Κούβα", "Τζαμάικα", "Πουέρτο Ρίκο"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Κούβα καλύπτει πάνω από 100.000 τετραγωνικά χιλιόμετρα και είναι μακράν το μεγαλύτερο νησί στην Καραϊβική.",
    "funFacts": [
      "Το σχήμα του νησιού της Κούβας μοιάζει με κροκόδειλο, γι' αυτό και συχνά αποκαλείται μεταφορικά έτσι από τους ντόπιους.",
      "Διαθέτει πάνω από 200 προστατευόμενες φυσικές περιοχές και πλούσια βιοποικιλότητα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CF%8D%CE%B2%CE%B1",
    "locale": "el-GR",
    "tags": ["cuba", "caribbean", "islands", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_087",
    "text": "Ποια πόλη είναι η επίσημη πρωτεύουσα της Βραζιλίας;",
    "answers": ["Ρίο ντε Τζανέιρο", "Σάο Πάολο", "Μπραζίλια", "Σαλβαδόρ"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μπραζίλια εγκαινιάστηκε ως νέα πρωτεύουσα της χώρας το 1960, αντικαθιστώντας το Ρίο ντε Τζανέιρο.",
    "funFacts": [
      "Είναι μια σχεδιασμένη πόλη, της οποίας το πολεοδομικό σχέδιο (Plano Piloto) έχει το χαρακτηριστικό σχήμα αεροπλάνου.",
      "Τα δημόσια κτίριά της σχεδιάστηκαν από τον διάσημο Βραζιλιάνο αρχιτέκτονα Όσκαρ Νίεμαγιερ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%81%CE%B1%CE%B6%CE%AF%CE%BB%CE%B9%CE%B1",
    "locale": "el-GR",
    "tags": ["brazil", "brasilia", "capitals", "south-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_088",
    "text": "Ποια θάλασσα βρίσκεται βόρεια της Τουρκίας και νότια της Ουκρανίας;",
    "answers": ["Βαλτική Θάλασσα", "Ερυθρά Θάλασσα", "Κασπία Θάλασσα", "Μαύρη Θάλασσα"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μαύρη Θάλασσα (Εύξεινος Πόντος) είναι εσωτερική θάλασσα που συνδέεται με τη Μεσόγειο μέσω του Βοσπόρου και των Δαρδανελλίων.",
    "funFacts": [
      "Στα αρχαία χρόνια οι Έλληνες την ονόμαζαν αρχικά 'Άξενο Πόντο' και αργότερα ευφημιστικά 'Εύξεινο Πόντο'.",
      "Τα βαθύτερα νερά της (κάτω από τα 150-200 μέτρα) είναι ανοξικά, με αποτέλεσμα αρχαία ναυάγια να διατηρούνται σε άριστη κατάσταση."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%8F%CF%81%CE%B7_%CE%98%CE%AC%CE%BB%CE%B1%CF%83%CF%83%CE%B1",
    "locale": "el-GR",
    "tags": ["black-sea", "seas", "europe", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_089",
    "text": "Ποια πόλη είναι η πρωτεύουσα του Μεξικού;",
    "answers": ["Πόλη του Μεξικού", "Γουαδαλαχάρα", "Μοντερέι", "Κανκούν"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Πόλη του Μεξικού (Ciudad de México) είναι η πρωτεύουσα και η μεγαλύτερη μητρόπολη της Βόρειας Αμερικής σε πληθυσμό.",
    "funFacts": [
      "Είναι χτισμένη πάνω στην αποξηραμένη λίμνη Τεξκόκο, σε μέσο υψόμετρο 2.240 μέτρων πάνω από την επιφάνεια της θάλασσας.",
      "Εξαιτίας του μαλακού εδάφους της αρχαίας λίμνης, ορισμένα τμήματα της πόλης βυθίζονται μερικά εκατοστά κάθε χρόνο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%8C%CE%BB%CE%B7_%CF%84%CE%BF%CF%85_%CE%9C%CE%B5%CE%BE%CE%B9%CE%BA%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["mexico", "mexico-city", "capitals", "north-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_090",
    "text": "Ποιο ευρωπαϊκό κράτος αποτελείται κυρίως από δύο γλωσσικές κοινότητες, τους Φλαμανδούς και τους Βαλλώνους;",
    "answers": ["Ελβετία", "Βέλγιο", "Ολλανδία", "Αυστρία"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Βέλγιο χωρίζεται στη Φλάνδρα στα βόρεια (όπου ομιλείται η ολλανδική) και στη Βαλλωνία στα νότια (όπου ομιλείται η γαλλική).",
    "funFacts": [
      "Επισήμως το Βέλγιο αναγνωρίζει τρεις εθνικές γλώσσες: ολλανδικά, γαλλικά και γερμανικά.",
      "Η πρωτεύουσά του, οι Βρυξέλλες, αποτελεί επισήμως δίγλωσση περιφέρεια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%AD%CE%BB%CE%B3%CE%B9%CE%BF",
    "locale": "el-GR",
    "tags": ["belgium", "europe", "politics", "languages"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_091",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ουκρανίας;",
    "answers": ["Χάρκοβο", "Οδησσός", "Κίεβο", "Λβιβ"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Κίεβο είναι η πρωτεύουσα και η πολυπληθέστερη πόλη της Ουκρανίας, χτισμένη στις όχθες του ποταμού Δνείπερου.",
    "funFacts": [
      "Είναι μία από τις αρχαιότερες πόλεις της Ανατολικής Ευρώπης, ιστορικό κέντρο των Ρως του Κιέβου από τον 9ο αιώνα.",
      "Ο σταθμός μετρό Αρσεναλνάγια στο Κίεβο είναι ένας από τους βαθύτερους υπόγειους σταθμούς στον κόσμο, σε βάθος 105,5 μέτρων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AF%CE%B5%CE%B2%CE%BF",
    "locale": "el-GR",
    "tags": ["ukraine", "kyiv", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_092",
    "text": "Στα σύνορα ποιας χώρας με τις Ηνωμένες Πολιτείες βρίσκονται οι φημισμένοι Καταρράκτες του Νιαγάρα;",
    "answers": ["Μεξικό", "Βραζιλία", "Αυστραλία", "Καναδάς"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Οι Καταρράκτες του Νιαγάρα βρίσκονται στον ομώνυμο ποταμό στα σύνορα της επαρχίας Οντάριο του Καναδά και της πολιτείας της Νέας Υόρκης.",
    "funFacts": [
      "Αποτελούνται από τρεις διαφορετικούς καταρράκτες: τους Καταρράκτες του Πετάλου, τους Αμερικανικούς και του Νυφικού Πέπλου.",
      "Περίπου το 90% του όγκου του νερού ρέει πάνω από τους καναδικούς Καταρράκτες του Πετάλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%B1%CF%81%CF%81%CE%AC%CE%BA%CF%84%CE%B5%CF%82_%CF%84%CE%BF%CF%85_%CE%9D%CE%B9%CE%B1%CE%B3%CE%AC%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["niagara", "waterfalls", "canada", "usa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_093",
    "text": "Ποια παραθαλάσσια πόλη της Μεσογείου είναι η πρωτεύουσα του Λιβάνου;",
    "answers": ["Βηρυτός", "Τρίπολη", "Σιδώνα", "Βύβλος"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βηρυτός βρίσκεται σε χερσόνησο στην ανατολική ακτή της Μεσογείου και είναι η πρωτεύουσα του Λιβάνου.",
    "funFacts": [
      "Κατοικείται συνεχώς εδώ και πάνω από 5.000 χρόνια, με τις πρώτες αναφορές σε αυτή να χρονολογούνται στην αρχαία Αίγυπτο.",
      "Στην ακμή της κατά τον 20ό αιώνα αποκαλούνταν συχνά 'Παρίσι της Μέσης Ανατολής' λόγω της κοσμοπολίτικης ατμόσφαιράς της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B7%CF%81%CF%85%CF%84%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["lebanon", "beirut", "capitals", "mediterranean"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_094",
    "text": "Ποιο διάσημο ιταλικό ηφαίστειο κατέστρεψε την αρχαία ρωμαϊκή πόλη της Πομπηίας το 79 μ.Χ.;",
    "answers": ["Αίτνα", "Βεζούβιος", "Στρόμπολι", "Βουλκάνο"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Βεζούβιος δεσπόζει στον Κόλπο της Νάπολης και είναι ένα από τα πιο γνωστά ενεργά ηφαίστεια στον κόσμο.",
    "funFacts": [
      "Η έκρηξη του 79 μ.Χ. έθαψε την Πομπηία και το Ηράκλειο κάτω από παχύ στρώμα τέφρας, διατηρώντας τα σχεδόν άθικτα.",
      "Είναι το μοναδικό ηφαίστειο στην ηπειρωτική Ευρώπη που έχει εκραγεί τα τελευταία εκατό χρόνια (το 1944)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B5%CE%B6%CE%BF%CF%8D%CE%B2%CE%B9%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["vesuvius", "volcanoes", "italy", "pompeii"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_095",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Σλοβακίας;",
    "answers": ["Κόσιτσε", "Ζίλινα", "Μπρατισλάβα", "Πρέσοβ"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μπρατισλάβα βρίσκεται στις όχθες του ποταμού Δούναβη και αποτελεί την πρωτεύουσα της Σλοβακίας.",
    "funFacts": [
      "Είναι η μοναδική εθνική πρωτεύουσα στον κόσμο που συνορεύει άμεσα με δύο ανεξάρτητα κράτη: την Αυστρία και την Ουγγαρία.",
      "Απέχει μόλις περίπου 60 χιλιόμετρα από τη Βιέννη, αποτελώντας ένα από τα πιο κοντινά ζεύγη ευρωπαϊκών πρωτευουσών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%81%CE%B1%CF%84%CE%B9%CF%83%CE%BB%CE%AC%CE%B2%CE%B1",
    "locale": "el-GR",
    "tags": ["slovakia", "bratislava", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_096",
    "text": "Ποια χώρα της Νοτιοανατολικής Ασίας ήταν παλαιότερα γνωστή στη Δύση με το όνομα Σιάμ;",
    "answers": ["Βιετνάμ", "Καμπότζη", "Μαλαισία", "Ταϊλάνδη"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η χώρα μετονομάστηκε επίσημα από Σιάμ σε Ταϊλάνδη το 1939, που σημαίνει 'Γη των Ελεύθερων'.",
    "funFacts": [
      "Είναι η μόνη χώρα στη Νοτιοανατολική Ασία που δεν αποικίστηκε ποτέ από ευρωπαϊκή δύναμη.",
      "Η πρωτεύουσά της είναι η Μπανγκόκ, της οποίας το επίσημο τελετουργικό ταϊλανδέζικο όνομα είναι το μακρύτερο τοπωνύμιο στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CF%8A%CE%BB%CE%AC%CE%BD%CE%B4%CE%B7",
    "locale": "el-GR",
    "tags": ["thailand", "siam", "asia", "geography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_097",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Τυνησίας;",
    "answers": ["Τύνιδα", "Σφαξ", "Σους", "Μπιζέρτα"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Τύνιδα βρίσκεται στη βορειοανατολική ακτή της Τυνησίας, κοντά στα ερείπια της αρχαίας Καρχηδόνας.",
    "funFacts": [
      "Στα περίχωρα της πόλης σώζονται τα αρχαιολογικά κατάλοιπα της ιστορικής Καρχηδόνας, Μνημείο Παγκόσμιας Κληρονομιάς της UNESCO.",
      "Η μεσαιωνική Μεδίνα της Τύνιδας περιλαμβάνει πάνω από 700 ιστορικά μνημεία, παλάτια και τζαμιά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%8D%CE%BD%CE%B9%CE%B4%CE%B1",
    "locale": "el-GR",
    "tags": ["tunisia", "tunis", "capitals", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_098",
    "text": "Ποιος ιστορικός ποταμός διασχίζει την πόλη του Λονδίνου;",
    "answers": ["Σηκουάνας", "Τάμεσης", "Τίβερης", "Δούναβης"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Τάμεσης έχει μήκος περίπου 346 χιλιόμετρα και είναι ο μεγαλύτερος ποταμός που βρίσκεται εξ ολοκλήρου στην Αγγλία.",
    "funFacts": [
      "Πάνω από 200 γέφυρες και πάνω από 20 σήραγγες διασχίζουν τον Τάμεση κατά μήκος της διαδρομής του.",
      "Κατά τον 'Μικρό Παγετώνα' (16ος-19ος αι.), ο Τάμεσης πάγωνε τόσο που διοργανώνονταν πάνω του τα περίφημα παγοπανηγύρια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AC%CE%BC%CE%B5%CF%83%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["thames", "rivers", "london", "uk"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_099",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ιορδανίας;",
    "answers": ["Άκαμπα", "Ζάρκα", "Αμμάν", "Ίρμπιντ"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Αμμάν είναι η πρωτεύουσα και η μεγαλύτερη πόλη του Χασεμιτικού Βασιλείου της Ιορδανίας.",
    "funFacts": [
      "Στην αρχαιότητα ήταν γνωστή ως Φιλαδέλφεια, ονομασμένη προς τιμήν του φαραώ Πτολεμαίου Β΄ του Φιλάδελφου.",
      "Αρχικά χτίστηκε πάνω σε επτά λόφους, αλλά σήμερα εκτείνεται σε περισσότερους από είκοσι λόφους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BC%CE%BC%CE%AC%CE%BD",
    "locale": "el-GR",
    "tags": ["jordan", "amman", "capitals", "middle-east"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_100",
    "text": "Ποια χώρα του πλανήτη κατέχει τον μεγαλύτερο πληθυσμό στον κόσμο, ξεπερνώντας το 1,4 δισεκατομμύριο κατοίκους;",
    "answers": ["Ηνωμένες Πολιτείες", "Ινδονησία", "Πακιστάν", "Ινδία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Σύμφωνα με εκτιμήσεις του ΟΗΕ το 2023, η Ινδία ξεπέρασε την Κίνα και έγινε η πολυπληθέστερη χώρα στον κόσμο.",
    "funFacts": [
      "Περίπου ένας στους έξι ανθρώπους στον πλανήτη ζει στην επικράτεια της Ινδίας.",
      "Η χώρα διαθέτει 22 επίσημα αναγνωρισμένες γλώσσες στο Σύνταγμά της, με τα χίντι και τα αγγλικά να χρησιμοποιούνται ευρέως."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%BD%CE%B4%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["india", "population", "records", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_101",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Χιλής;",
    "answers": ["Σαντιάγο", "Βαλπαραΐσο", "Κονσεπσιόν", "Αντοφαγάστα"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Σαντιάγο (Santiago de Chile) βρίσκεται σε μια κοιλάδα περιβαλλόμενη από τις επιβλητικές κορυφές των Άνδεων.",
    "funFacts": [
      "Ιδρύθηκε το 1541 από τον Ισπανό κονκισταδόρ Πέδρο δε Βαλδίβια με το όνομα Santiago de la Nueva Extremadura.",
      "Στο Σαντιάγο βρίσκεται ο ουρανοξύστης Gran Torre Santiago, ένα από τα ψηλότερα κτίρια στη Νότια Αμερική με ύψος 300 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%BD%CF%84%CE%B9%CE%AC%CE%B3%CE%BF",
    "locale": "el-GR",
    "tags": ["chile", "santiago", "capitals", "south-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_102",
    "text": "Ποια διάσημη ιταλική πόλη είναι χτισμένη πάνω σε λιμνοθάλασσα με κανάλια αντί για δρόμους;",
    "answers": ["Φλωρεντία", "Βενετία", "Γένοβα", "Νάπολη"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βενετία είναι χτισμένη πάνω σε 118 μικρά νησιά που χωρίζονται από κανάλια και συνδέονται με πάνω από 400 γέφυρες.",
    "funFacts": [
      "Το Μεγάλο Κανάλι (Canal Grande) είναι η κύρια υδάτινη αρτηρία της πόλης και έχει μήκος σχεδόν 4 χιλιόμετρα.",
      "Στη Βενετία δεν κυκλοφορούν αυτοκίνητα· όλες οι μετακινήσεις γίνονται με τα πόδια ή με πλωτά μέσα όπως γόνδολες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B5%CE%BD%CE%B5%CF%84%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["venice", "italy", "canals", "cities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_103",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Κολομβίας;",
    "answers": ["Μεδεγίν", "Κάλι", "Μπογκοτά", "Μπαρρανκίγια"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μπογκοτά βρίσκεται σε οροπέδιο των Άνδεων σε μέσο υψόμετρο 2.640 μέτρων, αποτελώντας την πρωτεύουσα της Κολομβίας.",
    "funFacts": [
      "Είναι η τρίτη ψηλότερη πρωτεύουσα της Νότιας Αμερικής σε υψόμετρο, μετά το Κίτο και τη Λα Πας.",
      "Στην Μπογκοτά λειτουργεί το διάσημο 'Μουσείο Χρυσού', που φιλοξενεί τη μεγαλύτερη συλλογή προκολομβιανών χρυσών τεχνουργημάτων στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CE%B3%CE%BA%CE%BF%CF%84%CE%AC",
    "locale": "el-GR",
    "tags": ["colombia", "bogota", "capitals", "south-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_104",
    "text": "Ποια χώρα της Μέσης Ανατολής έχει πρωτεύουσα την Τεχεράνη;",
    "answers": ["Ιράκ", "Συρία", "Αφγανιστάν", "Ιράν"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ιράν (ιστορικά γνωστό ως Περσία) έχει ως πρωτεύουσα και μεγαλύτερη πόλη την Τεχεράνη στους πρόποδες της οροσειράς Αλμπόρζ.",
    "funFacts": [
      "Η Τεχεράνη έγινε πρωτεύουσα του Ιράν το 1786 υπό τη δυναστεία των Κατζάρων.",
      "Το Ιράν συνορεύει με την Κασπία Θάλασσα στα βόρεια και με τον Περσικό Κόλπο στα νότια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CF%81%CE%AC%CE%BD",
    "locale": "el-GR",
    "tags": ["iran", "tehran", "capitals", "middle-east"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_105",
    "text": "Ποια είναι η επίσημη πρωτεύουσα του Βασιλείου του Μαρόκου;",
    "answers": ["Ραμπάτ", "Καζαμπλάνκα", "Μαρακές", "Φες"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ραμπάτ στις ακτές του Ατλαντικού είναι η πρωτεύουσα του Μαρόκου, αν και η Καζαμπλάνκα είναι η πολυπληθέστερη πόλη.",
    "funFacts": [
      "Στο Ραμπάτ δεσπόζει ο Πύργος του Χασάν, ένας ημιτελής μιναρές του 12ου αιώνα που προοριζόταν να γίνει ο μεγαλύτερος στον ισλαμικό κόσμο.",
      "Η ιστορική πόλη του Ραμπάτ έχει ενταχθεί στα Μνημεία Παγκόσμιας Κληρονομιάς της UNESCO από το 2012."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%B1%CE%BC%CF%80%CE%AC%CF%84",
    "locale": "el-GR",
    "tags": ["morocco", "rabat", "capitals", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_106",
    "text": "Ποια είναι η μακρύτερη ηπειρωτική οροσειρά στον κόσμο, διασχίζοντας επτά χώρες της Νότιας Αμερικής;",
    "answers": ["Βραχώδη Όρη", "Άνδεις", "Άλπεις", "Ιμαλάια"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Οι Άνδεις εκτείνονται σε μήκος περίπου 7.000 χιλιομέτρων κατά μήκος της δυτικής ακτής της Νότιας Αμερικής.",
    "funFacts": [
      "Η ψηλότερη κορυφή τους είναι το Ακονκάγκουα στην Αργεντινή, με υψόμετρο 6.961 μέτρα, η ψηλότερη κορυφή εκτός Ασίας.",
      "Διασχίζουν τη Βενεζουέλα, την Κολομβία, τον Ισημερινό, το Περού, τη Βολιβία, τη Χιλή και την Αργεντινή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BD%CE%B4%CE%B5%CE%B9%CF%82",
    "locale": "el-GR",
    "tags": ["andes", "mountains", "south-america", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_107",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Σλοβενίας;",
    "answers": ["Μάριμπορ", "Τσέλιε", "Λιουμπλιάνα", "Κράνι"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Λιουμπλιάνα είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Σλοβενίας, χτισμένη στον ποταμό Λιουμπλιάνιτσα.",
    "funFacts": [
      "Το σύμβολο της πόλης είναι ο Δράκος, ο οποίος απεικονίζεται στο οικόσημό της και στη διάσημη 'Γέφυρα του Δράκου'.",
      "Το 2016 η Λιουμπλιάνα ανακηρύχθηκε 'Πράσινη Πρωτεύουσα της Ευρώπης' λόγω της εκτεταμένης πεζοδρόμησης του κέντρου της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B9%CE%BF%CF%85%CE%BC%CF%80%CE%BB%CE%B9%CE%AC%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["slovenia", "ljubljana", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_108",
    "text": "Ποια αφρικανική χώρα έχει πρωτεύουσα το Ναϊρόμπι;",
    "answers": ["Τανζανία", "Ουγκάντα", "Αιθιοπία", "Κένυα"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ναϊρόμπι είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Κένυας στην Ανατολική Αφρική.",
    "funFacts": [
      "Το όνομά του προέρχεται από τη φράση των Μασάι 'Enkare Nyrobi', που σημαίνει 'τόπος δροσερού νερού'.",
      "Είναι η μοναδική πρωτεύουσα στον κόσμο που διαθέτει εθνικό πάρκο άγριας ζωής σε απόσταση μόλις 7 χιλιομέτρων από το κέντρο της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%B1%CF%8A%CF%81%CF%8C%CE%BC%CF%80%CE%B9",
    "locale": "el-GR",
    "tags": ["kenya", "nairobi", "capitals", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_109",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Εσθονίας;",
    "answers": ["Τάλιν", "Τάρτου", "Νάρβα", "Πάρνου"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Τάλιν βρίσκεται στις ακτές του Κόλπου της Φινλανδίας και αποτελεί την πρωτεύουσα της Εσθονίας.",
    "funFacts": [
      "Η μεσαιωνική Παλιά Πόλη του Τάλιν είναι μία από τις καλύτερα διατηρημένες οχυρωμένες πόλεις της Ευρώπης και ανήκει στην UNESCO.",
      "Απέχει μόλις 80 χιλιόμετρα θαλάσσιας διαδρομής από το Ελσίνκι της Φινλανδίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AC%CE%BB%CE%B9%CE%BD",
    "locale": "el-GR",
    "tags": ["estonia", "tallinn", "capitals", "baltics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_110",
    "text": "Ποιο είναι το μεγαλύτερο σε έκταση κράτος της Αφρικής;",
    "answers": ["Σουδάν", "Αλγερία", "Λιβύη", "Λαϊκή Δημοκρατία του Κονγκό"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Αλγερία καλύπτει έκταση σχεδόν 2,38 εκατομμυρίων τετραγωνικών χιλιομέτρων, αποτελώντας τη μεγαλύτερη χώρα της αφρικανικής ηπείρου.",
    "funFacts": [
      "Έγινε η μεγαλύτερη χώρα της Αφρικής το 2011, μετά τη διάσπαση του Σουδάν και του Νότιου Σουδάν.",
      "Περισσότερο από το 80% της συνολικής έκτασης της Αλγερίας καλύπτεται από την έρημο Σαχάρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CE%B5%CF%81%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["algeria", "africa", "records", "size"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('geography', 'easy', 1, questions)

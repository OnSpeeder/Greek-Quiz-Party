# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "geography_easy_011",
    "text": "Ποια είναι η πρωτεύουσα της Ιταλίας;",
    "answers": ["Ρώμη", "Μιλάνο", "Νάπολη", "Φλωρεντία"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ρώμη είναι η πρωτεύουσα και η πολυπληθέστερη πόλη της Ιταλίας, με ιστορία που ξεπερνά τα 2.500 χρόνια.",
    "funFacts": [
      "Αποκαλείται συχνά 'Αιώνια Πόλη' (La Città Eterna) λόγω της μακραίωνης ιστορίας της.",
      "Μέσα στα όρια της πόλης της Ρώμης βρίσκεται το Βατικανό, το μικρότερο ανεξάρτητο κράτος στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%8E%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["italy", "capitals", "europe", "cities"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_012",
    "text": "Σε ποια ήπειρο βρίσκεται η Αίγυπτος;",
    "answers": ["Ασία", "Αφρική", "Ευρώπη", "Νότια Αμερική"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Αίγυπτος βρίσκεται στη Βορειοανατολική Αφρική, αν και η χερσόνησος του Σινά εκτείνεται γεωγραφικά στην Ασία.",
    "funFacts": [
      "Ο ποταμός Νείλος διασχίζει ολόκληρη τη χώρα και αποτελεί την κύρια πηγή γλυκού νερού για τον πληθυσμό της.",
      "Η Αίγυπτος φιλοξενεί ένα από τα Επτά Θαύματα του Αρχαίου Κόσμου που διασώζεται μέχρι σήμερα, τη Μεγάλη Πυραμίδα της Γκίζας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%AF%CE%B3%CF%85%CF%80%CF%84%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["egypt", "africa", "continents"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_013",
    "text": "Ποια χώρα έχει τον μεγαλύτερο πληθυσμό στη Νότια Αμερική;",
    "answers": ["Αργεντινή", "Κολομβία", "Βραζιλία", "Περού"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βραζιλία έχει πληθυσμό που ξεπερνά τα 210 εκατομμύρια κατοίκους, αποτελώντας την πολυπληθέστερη χώρα της Νότιας Αμερικής.",
    "funFacts": [
      "Είναι η μοναδική πορτογαλόφωνη χώρα στην αμερικανική ήπειρο.",
      "Συνορεύει σχεδόν με όλες τις χώρες της Νότιας Αμερικής, εκτός από τη Χιλή και τον Ισημερινό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CF%81%CE%B1%CE%B6%CE%B9%CE%BB%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["brazil", "south-america", "population"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_014",
    "text": "Ποιο είναι το μεγαλύτερο σε έκταση νησί της Μεσογείου Θάλασσας;",
    "answers": ["Κρήτη", "Κύπρος", "Σαρδηνία", "Σικελία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Σικελία καλύπτει έκταση περίπου 25.711 τετραγωνικών χιλιομέτρων και είναι το μεγαλύτερο νησί της Μεσογείου.",
    "funFacts": [
      "Στη Σικελία δεσπόζει η Αίτνα, το ψηλότερο ενεργό ηφαίστειο στην Ευρώπη.",
      "Χωρίζεται από την ηπειρωτική Ιταλία μέσω του Στενού της Μεσσήνης, πλάτους μόλις 3 χιλιομέτρων στο στενότερο σημείο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B9%CE%BA%CE%B5%CE%BB%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["mediterranean", "islands", "sicily", "italy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_015",
    "text": "Ποια είναι η πρωτεύουσα της Γερμανίας;",
    "answers": ["Βερολίνο", "Μόναχο", "Αμβούργο", "Φρανκφούρτη"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Βερολίνο είναι η πρωτεύουσα και η πολυπληθέστερη πόλη της Γερμανίας, καθώς και ομόσπονδο κρατίδιο.",
    "funFacts": [
      "Η πόλη διαθέτει περισσότερες γέφυρες από τη Βενετία, με τον αριθμό τους να υπολογίζεται σε περίπου 1.700.",
      "Κατά τη διάρκεια του Ψυχρού Πολέμου ήταν χωρισμένη στα δύο από το περίφημο Τείχος του Βερολίνου, το οποίο έπεσε το 1989."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["germany", "berlin", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_016",
    "text": "Σε ποιον ωκεανό βρίσκονται τα νησιά της Χαβάης;",
    "answers": ["Ατλαντικός Ωκεανός", "Ειρηνικός Ωκεανός", "Ινδικός Ωκεανός", "Αρκτικός Ωκεανός"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το σύμπλεγμα των νησιών της Χαβάης βρίσκεται στο κέντρο του βόρειου Ειρηνικού Ωκεανού και αποτελεί πολιτεία των ΗΠΑ.",
    "funFacts": [
      "Η Χαβάη είναι η νοτιότερη και η μόνη νησιωτική πολιτεία των Ηνωμένων Πολιτειών.",
      "Το ηφαίστειο Μάουνα Κέα, μετρούμενο από την υποθαλάσσια βάση του μέχρι την κορυφή, ξεπερνά σε ύψος τα 10.000 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B1%CE%B2%CE%AC%CE%B7",
    "locale": "el-GR",
    "tags": ["hawaii", "oceans", "pacific", "usa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_017",
    "text": "Ποια ασιατική χώρα αποκαλείται παραδοσιακά «Χώρα του Ανατέλλοντος Ηλίου»;",
    "answers": ["Κίνα", "Νότια Κορέα", "Ιαπωνία", "Ταϊλάνδη"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το όνομα της Ιαπωνίας στα ιαπωνικά (Nippon ή Nihon) σημαίνει κυριολεκτικά 'πηγή του ήλιου' ή 'ανατολή'.",
    "funFacts": [
      "Η ιαπωνική σημαία (Hinomaru) απεικονίζει έναν κόκκινο ηλιακό δίσκο σε λευκό φόντο.",
      "Η χώρα αποτελείται από περισσότερα από 6.800 νησιά κατά μήκος της ανατολικής ακτής της Ασίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%B1%CF%80%CF%89%CE%BD%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["japan", "asia", "nicknames"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_018",
    "text": "Ποια είναι η πρωτεύουσα του Ηνωμένου Βασιλείου;",
    "answers": ["Εδιμβούργο", "Μάντσεστερ", "Μπέρμιγχαμ", "Λονδίνο"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Λονδίνο είναι η πρωτεύουσα του Ηνωμένου Βασιλείου και της Αγγλίας, χτισμένο στις όχθες του ποταμού Τάμεση.",
    "funFacts": [
      "Το μετρό του Λονδίνου (The Tube), που άνοιξε το 1863, είναι το παλαιότερο υπόγειο δίκτυο σιδηροδρόμων στον κόσμο.",
      "Μέσα από το προάστιο του Γκρήνουιτς στο Λονδίνο διέρχεται ο Πρώτος Μεσημβρινός (γεωγραφικό μήκος 0°)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CE%BD%CE%B4%CE%AF%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["uk", "london", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_019",
    "text": "Ποια τεχνητή διώρυγα συνδέει τη Μεσόγειο Θάλασσα με την Ερυθρά Θάλασσα;",
    "answers": ["Διώρυγα του Σουέζ", "Διώρυγα του Παναμά", "Διώρυγα της Κορίνθου", "Διώρυγα του Κιέλου"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Διώρυγα του Σουέζ στην Αίγυπτο εγκαινιάστηκε το 1869 και επιτρέπει τη συντόμευση της θαλάσσιας διαδρομής μεταξύ Ευρώπης και Ασίας.",
    "funFacts": [
      "Έχει μήκος περίπου 193 χιλιόμετρα και δεν διαθέτει υδατοφράκτες, καθώς οι δύο θάλασσες βρίσκονται στο ίδιο επίπεδο.",
      "Υπολογίζεται ότι περίπου το 12% του παγκόσμιου εμπορίου διέρχεται από τη συγκεκριμένη θαλάσσια οδό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CF%8E%CF%81%CF%85%CE%B3%CE%B1_%CF%84%CE%BF%CF%85_%CE%A3%CE%BF%CF%85%CE%AD%CE%B6",
    "locale": "el-GR",
    "tags": ["suez", "canals", "egypt", "mediterranean"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_020",
    "text": "Ποια είναι η πρωτεύουσα της Ισπανίας;",
    "answers": ["Βαρκελώνη", "Μαδρίτη", "Σεβίλλη", "Βαλένθια"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μαδρίτη βρίσκεται στο κέντρο της Ιβηρικής Χερσονήσου και αποτελεί την πρωτεύουσα και μεγαλύτερη πόλη της Ισπανίας.",
    "funFacts": [
      "Είναι η δεύτερη ψηλότερη πρωτεύουσα της Ευρωπαϊκής Ένωσης σε υψόμετρο (περίπου 667 μέτρα πάνω από τη θάλασσα).",
      "Στην κεντρική πλατεία Puerta del Sol βρίσκεται το 'Χιλιόμετρο Μηδέν' (Kilómetro Cero), σημείο αφετηρίας των ισπανικών εθνικών οδών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%B4%CF%81%CE%AF%CF%84%CE%B7",
    "locale": "el-GR",
    "tags": ["spain", "madrid", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_021",
    "text": "Ποιο είναι το μεγαλύτερο κοραλλιογενές οικοσύστημα στον κόσμο;",
    "answers": ["Κόλπος του Μεξικού", "Ερυθρά Θάλασσα", "Μεγάλος Κοραλλιογενής Ύφαλος", "Καραϊβική Θάλασσα"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Μεγάλος Κοραλλιογενής Ύφαλος εκτείνεται σε μήκος άνω των 2.300 χιλιομέτρων στα ανοιχτά του Κουίνσλαντ στην Αυστραλία.",
    "funFacts": [
      "Είναι το μεγαλύτερο ενιαίο ζωντανό οικοσύστημα στη Γη και είναι ορατό ακόμη και από το διάστημα.",
      "Αποτελείται από περισσότερους από 2.900 μεμονωμένους υφάλους και σχεδόν 900 νησιά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CE%B3%CE%AC%CE%BB%CE%BF%CF%82_%CE%9A%CE%BF%CF%81%CE%B1%CE%BB%CE%BB%CE%B9%CE%BF%CE%B3%CE%B5%CE%BD%CE%AE%CF%82_%CE%8E%CF%86%CE%B1%CE%BB%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["australia", "coral-reef", "oceans", "nature"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_022",
    "text": "Σε ποια ήπειρο βρίσκεται η χώρα του Περού;",
    "answers": ["Ασία", "Αφρική", "Βόρεια Αμερική", "Νότια Αμερική"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Περού βρίσκεται στο δυτικό τμήμα της Νότιας Αμερικής, κατά μήκος των ακτών του Ειρηνικού Ωκεανού.",
    "funFacts": [
      "Στο Περού βρίσκεται η περίφημη ακρόπολη των Ίνκας, το Μάτσου Πίτσου.",
      "Στα σύνορα Περού και Βολιβίας βρίσκεται η λίμνη Τιτικάκα, η υψηλότερη πλωτή λίμνη στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CF%81%CE%BF%CF%8D",
    "locale": "el-GR",
    "tags": ["peru", "south-america", "continents"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_023",
    "text": "Ποια είναι η πρωτεύουσα των Ηνωμένων Πολιτειών Αμερικής;",
    "answers": ["Ουάσινγκτον", "Νέα Υόρκη", "Λος Άντζελες", "Σικάγο"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ουάσινγκτον (Washington, D.C.) είναι η ομοσπονδιακή πρωτεύουσα των ΗΠΑ και δεν ανήκει σε καμία πολιτεία.",
    "funFacts": [
      "Ονομάστηκε προς τιμήν του Τζορτζ Ουάσινγκτον, του πρώτου προέδρου των Ηνωμένων Πολιτειών.",
      "Το ακρωνύμιο D.C. σημαίνει 'District of Columbia' (Περιφέρεια της Κολούμπια)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CF%85%CE%AC%CF%83%CE%B9%CE%BD%CE%B3%CE%BA%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["usa", "washington", "capitals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_024",
    "text": "Ποια μεγάλη θάλασσα βρέχει τις βόρειες ακτές της Αφρικής και τις νότιες ακτές της Ευρώπης;",
    "answers": ["Μαύρη Θάλασσα", "Μεσόγειος Θάλασσα", "Βαλτική Θάλασσα", "Ερυθρά Θάλασσα"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μεσόγειος Θάλασσα είναι σχεδόν κλειστή θάλασσα που συνδέεται με τον Ατλαντικό μέσω του Πορθμού του Γιβραλτάρ.",
    "funFacts": [
      "Το όνομά της προέρχεται από το 'μέσος' και 'γη', δηλαδή η θάλασσα που βρίσκεται στη μέση των γνωστών ηπείρων του αρχαίου κόσμου.",
      "Οι Ρωμαίοι την αποκαλούσαν 'Mare Nostrum', που σημαίνει 'Η Θάλασσά Μας'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CF%83%CF%8C%CE%B3%CE%B5%CE%B9%CE%BF%CF%82_%CE%98%CE%AC%CE%BB%CE%B1%CF%83%CF%83%CE%B1",
    "locale": "el-GR",
    "tags": ["mediterranean", "seas", "europe", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_025",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ρωσίας;",
    "answers": ["Αγία Πετρούπολη", "Νοβοσιμπίρσκ", "Μόσχα", "Καζάν"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Μόσχα είναι η πρωτεύουσα της Ρωσίας και το σημαντικότερο πολιτικό, οικονομικό και πολιτιστικό κέντρο της χώρας.",
    "funFacts": [
      "Στο κέντρο της Μόσχας βρίσκεται το Κρεμλίνο, ένα ιστορικό οχυρό συγκρότημα και έδρα του Προέδρου της Ρωσίας.",
      "Το μετρό της Μόσχας είναι παγκοσμίως διάσημο για την αρχιτεκτονική πολλών σταθμών του, που μοιάζουν με υπόγεια παλάτια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%8C%CF%83%CF%87%CE%B1",
    "locale": "el-GR",
    "tags": ["russia", "moscow", "capitals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_026",
    "text": "Σε ποια χώρα βρίσκεται το περίφημο μαυσωλείο Ταζ Μαχάλ;",
    "answers": ["Πακιστάν", "Μπανγκλαντές", "Νεπάλ", "Ινδία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ταζ Μαχάλ βρίσκεται στην πόλη Άγκρα της βόρειας Ινδίας, στις όχθες του ποταμού Γιαμούνα.",
    "funFacts": [
      "Χτίστηκε μεταξύ 1632 και 1653 από τον Μογγόλο αυτοκράτορα Σαχ Τζαχάν στη μνήμη της αγαπημένης του συζύγου Μουμτάζ Μαχάλ.",
      "Είναι κατασκευασμένο από λευκό μάρμαρο που αλλάζει αποχρώσεις ανάλογα με το φως του ήλιου και της σελήνης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CE%B6_%CE%9C%CE%B1%CF%87%CE%AC%CE%BB",
    "locale": "el-GR",
    "tags": ["india", "taj-mahal", "monuments", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_027",
    "text": "Ποια είναι η πρωτεύουσα της Κίνας;",
    "answers": ["Πεκίνο", "Σαγκάη", "Καντόνα", "Χονγκ Κονγκ"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Πεκίνο (Beijing) είναι η πρωτεύουσα της Λαϊκής Δημοκρατίας της Κίνας και μία από τις αρχαιότερες πόλεις του κόσμου.",
    "funFacts": [
      "Στην καρδιά του Πεκίνου βρίσκεται η Απαγορευμένη Πόλη, το μεγαλύτερο παλάτι στον κόσμο με σχεδόν 1.000 κτίρια.",
      "Το Πεκίνο είναι η πρώτη πόλη στην ιστορία που φιλοξένησε τόσο Θερινούς (2008) όσο και Χειμερινούς (2022) Ολυμπιακούς Αγώνες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B5%CE%BA%CE%AF%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["china", "beijing", "capitals", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_028",
    "text": "Ποια ήπειρος βρίσκεται γύρω από τον Νότιο Πόλο της Γης;",
    "answers": ["Αρκτική", "Ανταρκτική", "Ωκεανία", "Γροιλανδία"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ανταρκτική είναι η νοτιότερη ήπειρος της Γης και περιέχει τον γεωγραφικό Νότιο Πόλο.",
    "funFacts": [
      "Είναι η πιο ψυχρή, ξηρή και ανεμώδης ήπειρος στον πλανήτη, καλυμμένη κατά 98% από πάγο.",
      "Δεν έχει μόνιμο ανθρώπινο πληθυσμό, αλλά μόνο επιστημονικούς ερευνητές σε επανδρωμένους σταθμούς."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B1%CF%81%CE%BA%CF%84%CE%B9%CE%BA%CE%AE",
    "locale": "el-GR",
    "tags": ["antarctica", "continents", "polar", "south-pole"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_029",
    "text": "Ποιος είναι ο μακρύτερος ποταμός στην Ευρώπη;",
    "answers": ["Δούναβης", "Ρήνος", "Βόλγας", "Σηκουάνας"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Βόλγας στη Ρωσία έχει μήκος περίπου 3.530 χιλιόμετρα και εκβάλλει στην Κασπία Θάλασσα.",
    "funFacts": [
      "Έντεκα από τις είκοσι μεγαλύτερες πόλεις της Ρωσίας είναι χτισμένες στις όχθες του Βόλγα.",
      "Στη ρωσική λαογραφία αποκαλείται χαϊδευτικά 'Μητέρα Βόλγας' (Matushka Volga)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CF%8C%CE%BB%CE%B3%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["volga", "rivers", "europe", "russia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_030",
    "text": "Ποια είναι η πρωτεύουσα της Αιγύπτου;",
    "answers": ["Αλεξάνδρεια", "Γκίζα", "Λούξορ", "Κάιρο"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Κάιρο είναι η πρωτεύουσα της Αιγύπτου και η μεγαλύτερη μητροπολιτική περιοχή στον αραβικό κόσμο.",
    "funFacts": [
      "Στα αραβικά ονομάζεται Al-Qahirah, που σημαίνει 'Ο Νικητής' ή 'Ο Κατακτητής'.",
      "Αποκαλείται επίσης 'Πόλη των Χιλίων Μιναρέδων' λόγω της πληθώρας των ιστορικών τζαμιών της."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CE%B9%CF%81%CE%BF",
    "locale": "el-GR",
    "tags": ["cairo", "egypt", "capitals", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_031",
    "text": "Ποια χώρα συνορεύει βόρεια με τις Ηνωμένες Πολιτείες Αμερικής;",
    "answers": ["Καναδάς", "Μεξικό", "Κούβα", "Γροιλανδία"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Καναδάς βρίσκεται βόρεια των ηπειρωτικών ΗΠΑ, με τα σύνορά τους να αποτελούν τα μακρύτερα χερσαία σύνορα στον κόσμο.",
    "funFacts": [
      "Τα σύνορα ΗΠΑ-Καναδά έχουν μήκος 8.891 χιλιόμετρα και είναι τα μεγαλύτερα μη στρατιωτικοποιημένα σύνορα στη Γη.",
      "Ο Καναδάς έχει δύο επίσημες γλώσσες σε ομοσπονδιακό επίπεδο: τα αγγλικά και τα γαλλικά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CE%BD%CE%B1%CE%B4%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["canada", "usa", "borders", "north-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_032",
    "text": "Ποια είναι η πρωτεύουσα της Πορτογαλίας;",
    "answers": ["Πόρτο", "Λισαβόνα", "Μπράγκα", "Κοΐμπρα"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Λισαβόνα είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Πορτογαλίας, χτισμένη στις εκβολές του ποταμού Τάγου.",
    "funFacts": [
      "Είναι μία από τις παλαιότερες πόλεις της δυτικής Ευρώπης, προγενέστερη από το Λονδίνο, το Παρίσι και τη Ρώμη.",
      "Το 1755 επλήγη από έναν ιστορικό σεισμό και τσουνάμι, αλλά ανοικοδομήθηκε υποδειγματικά από τον Μαρκήσιο του Πομπάλ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B9%CF%83%CE%B1%CE%B2%CF%8C%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["portugal", "lisbon", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_033",
    "text": "Ποια ευρωπαϊκή χώρα έχει πρωτεύουσα το Δουβλίνο;",
    "answers": ["Σκωτία", "Ουαλία", "Ιρλανδία", "Ισλανδία"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Δουβλίνο είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Δημοκρατίας της Ιρλανδίας, στην ανατολική ακτή του νησιού.",
    "funFacts": [
      "Η Ιρλανδία είναι γνωστή διεθνώς ως το 'Σμαραγδένιο Νησί' λόγω του καταπράσινου φυσικού τοπίου της.",
      "Το όνομα Δουβλίνο προέρχεται από την ιρλανδική φράση 'Dubh Linn', που σημαίνει 'μαύρη λίμνη'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%BF%CF%85%CE%B2%CE%BB%CE%AF%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["ireland", "dublin", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_034",
    "text": "Ποια είναι η μεγαλύτερη ήπειρος της Γης τόσο σε έκταση όσο και σε πληθυσμό;",
    "answers": ["Αφρική", "Βόρεια Αμερική", "Ευρώπη", "Ασία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ασία καλύπτει περίπου το 30% της χερσαίας επιφάνειας της Γης και φιλοξενεί περίπου το 60% του παγκόσμιου πληθυσμού.",
    "funFacts": [
      "Στην Ασία βρίσκονται τόσο το ψηλότερο σημείο της Γης (Έβερεστ) όσο και το χαμηλότερο σημείο ξηράς (Νεκρά Θάλασσα).",
      "Φιλοξενεί τις δύο χώρες με τον μεγαλύτερο πληθυσμό στον κόσμο, την Ινδία και την Κίνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%83%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["asia", "continents", "records", "world"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_035",
    "text": "Ποια είναι η πρωτεύουσα της Αυστρίας;",
    "answers": ["Βιέννη", "Σάλτσμπουργκ", "Ίνσμπρουκ", "Γκρατς"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βιέννη είναι η πρωτεύουσα της Αυστρίας, χτισμένη στις όχθες του ποταμού Δούναβη.",
    "funFacts": [
      "Είναι διεθνώς γνωστή ως η 'Πόλη της Μουσικής' χάρη στην κληρονομιά συνθετών όπως ο Μότσαρτ και ο Μπετόβεν.",
      "Φιλοξενεί την έδρα διεθνών οργανισμών, όπως ο ΟΠΕΚ και ο Διεθνής Οργανισμός Ατομικής Ενέργειας (IAEA)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%AD%CE%BD%CE%BD%CE%B7",
    "locale": "el-GR",
    "tags": ["vienna", "austria", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_036",
    "text": "Σε ποια χώρα βρίσκονται οι περίφημες Πυραμίδες της Γκίζας;",
    "answers": ["Ιορδανία", "Αίγυπτος", "Σουδάν", "Μαρόκο"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το σύμπλεγμα των πυραμίδων της Γκίζας και η Μεγάλη Σφίγγα βρίσκονται στα περίχωρα του Καΐρου στην Αίγυπτο.",
    "funFacts": [
      "Η Μεγάλη Πυραμίδα του Χέοπα ήταν το ψηλότερο ανθρώπινο κτίσμα στον κόσμο για πάνω από 3.800 χρόνια.",
      "Αποτελεί το παλαιότερο από τα Επτά Θαύματα του Αρχαίου Κόσμου και το μοναδικό που σώζεται μέχρι σήμερα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%B5%CE%BA%CF%81%CF%8C%CF%80%CE%BF%CE%BB%CE%B7_%CF%84%CE%B7%CF%82_%CE%93%CE%BA%CE%AF%CE%B6%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["egypt", "pyramids", "giza", "landmarks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_037",
    "text": "Ποια πόλη είναι η επίσημη πρωτεύουσα της Τουρκίας;",
    "answers": ["Κωνσταντινούπολη", "Σμύρνη", "Άγκυρα", "Προύσα"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Άγκυρα ανακηρύχθηκε πρωτεύουσα της Τουρκικής Δημοκρατίας το 1923 από τον Μουσταφά Κεμάλ Ατατούρκ.",
    "funFacts": [
      "Αν και η Κωνσταντινούπολη είναι η πολυπληθέστερη πόλη, η Άγκυρα αποτελεί το διοικητικό και πολιτικό κέντρο της χώρας.",
      "Στην Άγκυρα βρίσκεται το Ανίτκαμπιρ, το επιβλητικό μαυσωλείο του Μουσταφά Κεμάλ Ατατούρκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%B3%CE%BA%CF%85%CF%81%CE%B1",
    "locale": "el-GR",
    "tags": ["turkey", "ankara", "capitals"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_038",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Ισλανδίας;",
    "answers": ["Ακουρέιρι", "Κέφλαβικ", "Κόπαβογκουρ", "Ρέικιαβικ"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ρέικιαβικ είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Ισλανδίας, καθώς και η βορειότερη πρωτεύουσα κυρίαρχου κράτους στον κόσμο.",
    "funFacts": [
      "Το όνομά του στα ισλανδικά σημαίνει 'Όρμος των Καπνών', από τις γεωθερμικές αναθυμιάσεις των θερμών πηγών.",
      "Σχεδόν όλη η θέρμανση και η ηλεκτρική ενέργεια της πόλης παράγονται από ανανεώσιμη γεωθερμική ενέργεια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AD%CE%B9%CE%BA%CE%B9%CE%B1%CE%B2%CE%B9%CE%BA",
    "locale": "el-GR",
    "tags": ["iceland", "reykjavik", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_039",
    "text": "Ποια διώρυγα συνδέει τον Ατλαντικό με τον Ειρηνικό Ωκεανό στην Κεντρική Αμερική;",
    "answers": ["Διώρυγα του Παναμά", "Διώρυγα του Σουέζ", "Διώρυγα της Κορίνθου", "Διώρυγα του Κιέλου"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Διώρυγα του Παναμά τέμνει τον ισθμό του Παναμά επιτρέποντας στα πλοία να περνούν μεταξύ των δύο μεγάλων ωκεανών.",
    "funFacts": [
      "Εγκαινιάστηκε επίσημα το 1914 και γλίτωσε τα πλοία από τον επικίνδυνο γύρο του Ακρωτηρίου Χορν στη Νότια Αμερική.",
      "Χρησιμοποιεί δεξαμενές ανύψωσης που ανεβάζουν τα πλοία σε ύψος 26 μέτρων πάνω από την επιφάνεια της θάλασσας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CF%8E%CF%81%CF%85%CE%B3%CE%B1_%CF%84%CE%BF%CF%85_%CE%A0%CE%B1%CE%BD%CE%B1%CE%BC%CE%AC",
    "locale": "el-GR",
    "tags": ["panama", "canals", "oceans", "central-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_040",
    "text": "Ποια είναι η επίσημη συνταγματική πρωτεύουσα της Ολλανδίας;",
    "answers": ["Ρότερνταμ", "Άμστερνταμ", "Χάγη", "Ουτρέχτη"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Άμστερνταμ είναι η επίσημη πρωτεύουσα της Ολλανδίας, αν και η έδρα της κυβέρνησης και του κοινοβουλίου βρίσκεται στη Χάγη.",
    "funFacts": [
      "Είναι διάσημο για τα 165 κανάλια του, τα οποία έχουν συνολικό μήκος άνω των 100 χιλιομέτρων.",
      "Υπολογίζεται ότι στην πόλη υπάρχουν περισσότερα ποδήλατα από ό,τι μόνιμοι κάτοικοι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BC%CF%83%CF%84%CE%B5%CF%81%CE%BD%CF%84%CE%B1%CE%BC",
    "locale": "el-GR",
    "tags": ["netherlands", "amsterdam", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_041",
    "text": "Σε ποια ευρωπαϊκή οροσειρά βρίσκεται η κορυφή Μον Μπλαν (Mont Blanc);",
    "answers": ["Πυρηναία", "Καρπάθια", "Άλπεις", "Απέννινα"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Μον Μπλαν (Λευκό Όρος) βρίσκεται στις Άλπεις, στα σύνορα μεταξύ Γαλλίας και Ιταλίας, με υψόμετρο 4.808 μέτρα.",
    "funFacts": [
      "Είναι η ψηλότερη κορυφή των Άλπεων και της Δυτικής Ευρώπης.",
      "Η πρώτη επιτυχής ανάβαση στην κορυφή του έγινε το 1786, γεγονός που σηματοδότησε τη γέννηση της σύγχρονης ορειβασίας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD_%CE%9C%CF%80%CE%BB%CE%B1%CE%BD",
    "locale": "el-GR",
    "tags": ["alps", "mont-blanc", "mountains", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_042",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Αργεντινής;",
    "answers": ["Κόρδοβα", "Ροσάριο", "Μεντόσα", "Μπουένος Άιρες"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Μπουένος Άιρες είναι η πρωτεύουσα και το μεγαλύτερο λιμάνι της Αργεντινής, στις όχθες του Ρίο ντε λα Πλάτα.",
    "funFacts": [
      "Το όνομά του στα ισπανικά σημαίνει 'Καλοί Άνεμοι' ή 'Δροσεροί Άνεμοι'.",
      "Η λεωφόρος 9 de Julio στο Μπουένος Άιρες θεωρείται μία από τις φαρδύτερες λεωφόρους στον κόσμο με πλάτος έως 140 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CF%85%CE%AD%CE%BD%CE%BF%CF%82_%CE%86%CE%B9%CF%81%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["argentina", "buenos-aires", "capitals", "south-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_043",
    "text": "Ποιο κράτος της Βόρειας Αμερικής βρίσκεται ακριβώς νότια των Ηνωμένων Πολιτειών;",
    "answers": ["Μεξικό", "Γουατεμάλα", "Κούβα", "Μπελίζ"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Μεξικό συνορεύει στα βόρεια με τις Ηνωμένες Πολιτείες Αμερικής κατά μήκος των ποταμών Ρίο Γκράντε και Κολοράντο.",
    "funFacts": [
      "Τα σύνορα ΗΠΑ και Μεξικού είναι από τα πιο πολυσύχναστα χερσαία περάσματα παγκοσμίως.",
      "Η Πόλη του Μεξικού είναι χτισμένη πάνω στα ερείπια της Τενοτστιτλάν, της αρχαίας πρωτεύουσας των Αζτέκων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B5%CE%BE%CE%B9%CE%BA%CF%8C",
    "locale": "el-GR",
    "tags": ["mexico", "usa", "borders", "north-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_044",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Σουηδίας;",
    "answers": ["Γκέτεμποργκ", "Στοκχόλμη", "Μάλμε", "Ουψάλα"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Στοκχόλμη είναι η πρωτεύουσα της Σουηδίας, χτισμένη πάνω σε αρχιπέλαγος 14 νησιών στη λίμνη Μέλαρεν και τη Βαλτική.",
    "funFacts": [
      "Στο Δημαρχείο της Στοκχόλμης πραγματοποιείται κάθε χρόνο το επίσημο συμπόσιο των βραβείων Νόμπελ.",
      "Λόγω των πολλών υδάτινων οδών της, αποκαλείται συχνά 'Βενετία του Βορρά'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF%CE%BA%CF%87%CF%8C%CE%BB%CE%BC%CE%B7",
    "locale": "el-GR",
    "tags": ["sweden", "stockholm", "capitals", "scandinavia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_045",
    "text": "Ποιο νησιωτικό κράτος της Ασίας αποτελείται κυρίως από τα τέσσερα νησιά Χονσού, Χοκάιντο, Κιούσου και Σικόκου;",
    "answers": ["Φιλιππίνες", "Ινδονησία", "Ιαπωνία", "Ταϊβάν"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Αυτά τα τέσσερα κύρια νησιά συγκεντρώνουν τη συντριπτική πλειονότητα του εδάφους και του πληθυσμού της Ιαπωνίας.",
    "funFacts": [
      "Το νησί Χονσού είναι το μεγαλύτερο από τα τέσσερα και φιλοξενεί τόσο το Τόκιο όσο και το επιβλητικό όρος Φούτζι.",
      "Το Χοκάιντο στα βόρεια είναι γνωστό για το ψυχρό κλίμα και τα φημισμένα χιονοδρομικά του κέντρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%99%CE%B1%CF%80%CF%89%CE%BD%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["japan", "islands", "asia", "geography"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_046",
    "text": "Ποια είναι η πρωτεύουσα της Νορβηγίας;",
    "answers": ["Μπέργκεν", "Τρόντχαϊμ", "Σταβάνγκερ", "Όσλο"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Όσλο βρίσκεται στην κορυφή του ομώνυμου φιόρδ και είναι η πρωτεύουσα της Νορβηγίας.",
    "funFacts": [
      "Μέχρι το 1925 η πόλη ονομαζόταν Χριστιανία (Christiania), προς τιμήν του βασιλιά Χριστιανού Δ΄.",
      "Στο Όσλο απονέμεται κάθε χρόνο το Νόμπελ Ειρήνης, σε αντίθεση με τα υπόλοιπα βραβεία Νόμπελ που δίνονται στη Στοκχόλμη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%8C%CF%83%CE%BB%CE%BF",
    "locale": "el-GR",
    "tags": ["norway", "oslo", "capitals", "scandinavia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_047",
    "text": "Ποιος ωκεανός χωρίζει την αμερικανική ήπειρο από την Ευρώπη και την Αφρική;",
    "answers": ["Ατλαντικός Ωκεανός", "Ειρηνικός Ωκεανός", "Ινδικός Ωκεανός", "Αρκτικός Ωκεανός"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Ατλαντικός Ωκεανός είναι ο δεύτερος μεγαλύτερος ωκεανός της Γης, εκτεινόμενος από την Αρκτική μέχρι την Ανταρκτική.",
    "funFacts": [
      "Το όνομά του προέρχεται από τον Τιτάνα Άτλαντα της ελληνικής μυθολογίας.",
      "Στον βυθό του εκτείνεται η Μεσοατλαντική Ράχη, η μεγαλύτερη υποθαλάσσια οροσειρά στον κόσμο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%84%CE%BB%CE%B1%CE%BD%CF%84%CE%B9%CE%BA%CF%8C%CF%82_%CE%A9%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82",
    "locale": "el-GR",
    "tags": ["atlantic", "oceans", "earth"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_048",
    "text": "Ποια πόλη είναι η πρωτεύουσα του Καναδά;",
    "answers": ["Τορόντο", "Οττάβα", "Μόντρεαλ", "Βανκούβερ"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Οττάβα στην επαρχία του Οντάριο επελέγη το 1857 από τη Βασίλισσα Βικτώρια ως η ομοσπονδιακή πρωτεύουσα του Καναδά.",
    "funFacts": [
      "Αν και το Τορόντο είναι η πολυπληθέστερη πόλη, η Οττάβα επιλέχθηκε ως συμβιβασμός μεταξύ αγγλόφωνων και γαλλόφωνων.",
      "Το κανάλι Rideau που διασχίζει την πόλη παγώνει τον χειμώνα και μετατρέπεται σε τεράστιο φυσικό παγοδρόμιο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CF%84%CF%84%CE%AC%CE%B2%CE%B1",
    "locale": "el-GR",
    "tags": ["canada", "ottawa", "capitals", "north-america"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_049",
    "text": "Σε ποια χώρα βρίσκεται το περίφημο καμπαναριό γνωστό ως «Κεκλιμένος Πύργος της Πίζας»;",
    "answers": ["Γαλλία", "Ισπανία", "Ιταλία", "Ελλάδα"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Πύργος της Πίζας είναι το ανεξάρτητο καμπαναριό του καθεδρικού ναού της πόλης Πίζα στην Τοσκάνη της Ιταλίας.",
    "funFacts": [
      "Άρχισε να γέρνει ήδη κατά τη διάρκεια της κατασκευής του τον 12ο αιώνα, λόγω του μαλακού εδάφους θεμελίωσης.",
      "Χρειάστηκαν σχεδόν δύο αιώνες για να ολοκληρωθεί η ανέγερσή του λόγω διαδοχικών πολεμικών συγκρούσεων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%8D%CF%81%CE%B3%CE%BF%CF%82_%CF%84%CE%B7%CF%82_%CE%A0%CE%AF%CE%B6%CE%B1%CF%82",
    "locale": "el-GR",
    "tags": ["italy", "pisa", "landmarks", "monuments"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_050",
    "text": "Ποια πόλη είναι η πρωτεύουσα του Βελγίου;",
    "answers": ["Αμβέρσα", "Γάνδη", "Μπρυζ", "Βρυξέλλες"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Οι Βρυξέλλες είναι η πρωτεύουσα του Βελγίου και de facto πρωτεύουσα της Ευρωπαϊκής Ένωσης.",
    "funFacts": [
      "Στις Βρυξέλλες βρίσκονται τα κεντρικά γραφεία της Ευρωπαϊκής Επιτροπής, του Συμβουλίου της ΕΕ και του ΝΑΤΟ.",
      "Ένα από τα πιο διάσημα σύμβολα της πόλης είναι το Manneken Pis, ένα μικρό μπρούτζινο άγαλμα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CF%81%CF%85%CE%BE%CE%AD%CE%BB%CE%BB%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["belgium", "brussels", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_051",
    "text": "Ποια είναι η μικρότερη ήπειρος του πλανήτη σε χερσαία έκταση;",
    "answers": ["Ωκεανία", "Ευρώπη", "Ανταρκτική", "Νότια Αμερική"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Ωκεανία (μαζί με την Αυστραλία) είναι η μικρότερη σε έκταση ήπειρος στον κόσμο.",
    "funFacts": [
      "Περιλαμβάνει την Αυστραλία, τη Νέα Ζηλανδία και χιλιάδες νησιά διασκορπισμένα στον Ειρηνικό Ωκεανό.",
      "Η Αυστραλία είναι η μόνη χώρα στον κόσμο που εκτείνεται σε ολόκληρη ηπειρωτική μάζα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A9%CE%BA%CE%B5%CE%B1%CE%BD%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["oceania", "continents", "australia", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_052",
    "text": "Ποια πόλη λειτουργεί ως ομοσπονδιακή πρωτεύουσα (έδρα της κυβέρνησης) της Ελβετίας;",
    "answers": ["Ζυρίχη", "Βέρνη", "Γενεύη", "Βασιλεία"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βέρνη είναι η de facto πρωτεύουσα της Ελβετίας (Bundesstadt), καθώς φιλοξενεί το Κοινοβούλιο και την κυβέρνηση.",
    "funFacts": [
      "Η Ελβετία συνταγματικά δεν έχει επίσημη πρωτεύουσα, αλλά η Βέρνη ορίστηκε 'ομοσπονδιακή πόλη' το 1848.",
      "Το ιστορικό κέντρο της Βέρνης έχει ανακηρυχθεί Μνημείο Παγκόσμιας Κληρονομιάς της UNESCO."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%AD%CF%81%CE%BD%CE%B7",
    "locale": "el-GR",
    "tags": ["switzerland", "bern", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_053",
    "text": "Ποιος ευρωπαϊκός ποταμός διασχίζει τέσσερις εθνικές πρωτεύουσες (Βιέννη, Μπρατισλάβα, Βουδαπέστη, Βελιγράδι);",
    "answers": ["Ρήνος", "Έλβας", "Δούναβης", "Σηκουάνας"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Δούναβης είναι ο δεύτερος μακρύτερος ποταμός της Ευρώπης και διασχίζει ή οριοθετεί 10 διαφορετικές χώρες.",
    "funFacts": [
      "Πηγάζει από τον Μέλανα Δρυμό στη Γερμανία και εκβάλλει στη Μαύρη Θάλασσα.",
      "Είναι ο μοναδικός μεγάλος ευρωπαϊκός ποταμός που ρέει από τα δυτικά προς τα ανατολικά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CE%BF%CF%85%CE%BD%CE%B1%CE%B2%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["danube", "rivers", "europe", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_054",
    "text": "Ποια είναι η πρωτεύουσα της Πολωνίας;",
    "answers": ["Κρακοβία", "Γκντανσκ", "Βρότσλαβ", "Βαρσοβία"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Βαρσοβία είναι η πρωτεύουσα και η μεγαλύτερη πόλη της Πολωνίας, χτισμένη στον ποταμό Βιστούλα.",
    "funFacts": [
      "Η ιστορική Παλιά Πόλη της Βαρσοβίας ισοπεδώθηκε στον Β΄ Παγκόσμιο Πόλεμο και ανακατασκευάστηκε με εντυπωσιακή ακρίβεια.",
      "Εκεί γεννήθηκε η διάσημη φυσικός και χημικός Μαρία Κιουρί, η πρώτη γυναίκα που τιμήθηκε με βραβείο Νόμπελ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CF%81%CF%83%CE%BF%CE%B2%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["poland", "warsaw", "capitals", "europe"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_055",
    "text": "Σε ποια χώρα βρίσκεται το εντυπωσιακό και παγκοσμίως διάσημο φαράγγι Γκραν Κάνιον;",
    "answers": ["Ηνωμένες Πολιτείες", "Καναδάς", "Αυστραλία", "Μεξικό"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Γκραν Κάνιον βρίσκεται στην πολιτεία της Αριζόνα στις ΗΠΑ και σμιλεύτηκε από τον ποταμό Κολοράντο.",
    "funFacts": [
      "Έχει μήκος περίπου 446 χιλιόμετρα και σε ορισμένα σημεία φτάνει σε βάθος άνω των 1.800 μέτρων.",
      "Τα πετρώματα στα βαθύτερα στρώματά του έχουν ηλικία σχεδόν δύο δισεκατομμυρίων ετών."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CF%81%CE%B1%CE%BD_%CE%9A%CE%AC%CE%BD%CE%B9%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["grand-canyon", "canyons", "usa", "landmarks"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_056",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Δανίας;",
    "answers": ["Όρχους", "Κοπεγχάγη", "Όντενσε", "Άλμποργκ"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Κοπεγχάγη εκτείνεται στα νησιά Σέλαιν και Άμαγκερ και αποτελεί την πρωτεύουσα της Δανίας.",
    "funFacts": [
      "Στο λιμάνι της πόλης βρίσκεται το διάσημο χάλκινο άγαλμα της 'Μικρής Γοργόνας' από το παραμύθι του Χανς Κρίστιαν Άντερσεν.",
      "Συνδέεται με τη σουηδική πόλη Μάλμε μέσω της εντυπωσιακής γέφυρας Έρεσουντ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CF%80%CE%B5%CE%B3%CF%87%CE%AC%CE%B3%CE%B7",
    "locale": "el-GR",
    "tags": ["denmark", "copenhagen", "capitals", "scandinavia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_057",
    "text": "Ποιο είναι το δεύτερο μεγαλύτερο σε έκταση νησί της Μεσογείου μετά τη Σικελία;",
    "answers": ["Κύπρος", "Κρήτη", "Σαρδηνία", "Κορσική"],
    "correctAnswerIndex": 2,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Σαρδηνία είναι αυτόνομη περιφέρεια της Ιταλίας και καλύπτει πάνω από 24.000 τετραγωνικά χιλιόμετρα.",
    "funFacts": [
      "Είναι γνωστή για τα 'νουράγκι', μυστηριώδεις μεγαλιθικούς πύργους της Εποχής του Χαλκού.",
      "Αποτελεί μία από τις αναγνωρισμένες 'Μπλε Ζώνες' του πλανήτη με υψηλό ποσοστό υπεραιωνόβιων κατοίκων."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CF%81%CE%B4%CE%B7%CE%BD%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["sardinia", "mediterranean", "islands", "italy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_058",
    "text": "Ποια είναι η πρωτεύουσα της Φινλανδίας;",
    "answers": ["Τάμπερε", "Τούρκου", "Έσποο", "Ελσίνκι"],
    "correctAnswerIndex": 3,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Το Ελσίνκι βρίσκεται στις νότιες ακτές της Φινλανδίας, στον Κόλπο της Φινλανδίας στη Βαλτική Θάλασσα.",
    "funFacts": [
      "Είναι η βορειότερη πρωτεύουσα κράτους-μέλους της Ευρωπαϊκής Ένωσης.",
      "Η Φινλανδία διαθέτει σχεδόν 188.000 λίμνες στην επικράτειά της, παίρνοντας τον τίτλο της 'Χώρας των Χιλίων Λιμνών'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BB%CF%83%CE%AF%CE%BD%CE%BA%CE%B9",
    "locale": "el-GR",
    "tags": ["finland", "helsinki", "capitals", "scandinavia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_059",
    "text": "Ποιο διάσημο στενό συνδέει τη Μαύρη Θάλασσα με τη Θάλασσα του Μαρμαρά στην Κωνσταντινούπολη;",
    "answers": ["Βόσπορος", "Δαρδανέλλια", "Στενό της Μεσσήνης", "Πορθμός του Γιβραλτάρ"],
    "correctAnswerIndex": 0,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Ο Βόσπορος είναι φυσικός πορθμός διεθνούς σημασίας που χωρίζει την ευρωπαϊκή από την ασιατική πλευρά της Κωνσταντινούπολης.",
    "funFacts": [
      "Θεωρείται το στενότερο θαλάσσιο πέρασμα διεθνούς ναυσιπλοΐας, με ελάχιστο πλάτος μόλις περίπου 700 μέτρα.",
      "Σύμφωνα με την ελληνική μυθολογία, πήρε το όνομά του από το πέρασμα της Ιούς μεταμορφωμένης σε δάμαλη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CF%8C%CF%83%CF%80%CE%BF%CF%81%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["bosphorus", "straits", "istanbul", "turkey"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "geography_easy_060",
    "text": "Ποια πόλη είναι η πρωτεύουσα της Νότιας Κορέας;",
    "answers": ["Μπουσάν", "Σεούλ", "Ίντσον", "Ντέγκου"],
    "correctAnswerIndex": 1,
    "categoryId": "geography",
    "difficulty": 1,
    "explanation": "Η Σεούλ είναι η πρωτεύουσα και η μεγαλύτερη μητρόπολη της Δημοκρατίας της Κορέας (Νότια Κορέα).",
    "funFacts": [
      "Η μητροπολιτική περιοχή της Σεούλ συγκεντρώνει σχεδόν το ήμισυ του συνολικού πληθυσμού της Νότιας Κορέας.",
      "Διασχίζεται από τον ποταμό Χαν και περιβάλλεται από ορεινούς όγκους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B5%CE%BF%CF%8D%CE%BB",
    "locale": "el-GR",
    "tags": ["south-korea", "seoul", "capitals", "asia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('geography', 'easy', 1, questions)

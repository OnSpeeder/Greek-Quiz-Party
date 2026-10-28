# -*- coding: utf-8 -*-
import sys
import os

# Add repo root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "sports_med_011",
    "text": "Σε ποια χρονιά διεξήχθη στη Γαλλία το πρώτο Ευρωπαϊκό Πρωτάθλημα Ποδοσφαίρου (Euro), το οποίο κατέκτησε η Σοβιετική Ένωση;",
    "answers": ["Το 1960", "Το 1956", "Το 1964", "Το 1952"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το πρώτο Ευρωπαϊκό Πρωτάθλημα Εθνών πραγματοποιήθηκε το 1960 με την ΕΣΣΔ να νικά τη Γιουγκοσλαβία με 2-1 στην παράταση στον τελικό του Παρισιού.",
    "funFacts": [
      "Η ιδέα για το τουρνουά ανήκε στον Ανρί Ντελονέ, γενικό γραμματέα της UEFA, προς τιμήν του οποίου ονομάστηκε το τρόπαιο.",
      "Στην τελική φάση της πρώτης διοργάνωσης συμμετείχαν μόλις τέσσερις εθνικές ομάδες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%85%CF%81%CF%89%CF%80%CE%B1%CF%8A%CE%BA%CF%8C_%CE%A0%CF%81%CF%89%CF%84%CE%AC%CE%B8%CE%BB%CE%B7%CE%BC%CE%B1_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_1960",
    "locale": "el-GR",
    "tags": ["euro-1960", "football-history", "uefa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_012",
    "text": "Ποιος θρυλικός σέντερ κατέχει το αξεπέραστο ρεκόρ των 100 πόντων σε έναν μόνο αγώνα NBA, το οποίο πέτυχε το 1962;",
    "answers": ["Καρίμ Αμπντούλ-Τζαμπάρ", "Ουίλτ Τσάμπερλεϊν", "Μπιλ Ράσελ", "Έλτζιν Μπέιλορ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 2 Μαρτίου 1962, ο Wilt Chamberlain των Philadelphia Warriors σημείωσε 100 πόντους εναντίον των New York Knicks στο Χέρσεϊ της Πενσυλβάνια.",
    "funFacts": [
      "Ο αγώνας δεν μεταδόθηκε τηλεοπτικά και η ιστορική φωτογραφία του Chamberlain να κρατά ένα χαρτί με το νούμερο '100' τραβήχτηκε στα αποδυτήρια.",
      "Εκείνη τη σεζόν (1961-62) είχε μέσο όρο 50,4 πόντους και 25,7 ριμπάουντ ανά αγώνα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BF%CF%85%CE%AF%CE%BB%CF%84_%CE%A4%CF%83%CE%AC%CE%BC%CF%80%CE%B5%CF%81%CE%BB%CE%B5%CF%8A%CE%BD",
    "locale": "el-GR",
    "tags": ["wilt-chamberlain", "nba-records", "100-points"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_013",
    "text": "Ποιος Τσεχοσλοβάκος δρομέας ('Τσεχική Ατμομηχανή') κέρδισε χρυσό στα 5.000μ, 10.000μ και στον Μαραθώνιο στους Ολυμπιακούς του 1952;",
    "answers": ["Πάαβο Νούρμι", "Χάνες Κολεχμάινεν", "Εμίλ Ζάτοπεκ", "Λάσε Βίρεν"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Emil Zátopek πέτυχε το μοναδικό στην ιστορία τριπλό ολυμπιακό χρυσό αντοχής στους Ολυμπιακούς Αγώνες του Ελσίνκι το 1952.",
    "funFacts": [
      "Δεν είχε τρέξει ποτέ ξανά στη ζωή του Μαραθώνιο πριν από εκείνη την ολυμπιακή κούρσα στο Ελσίνκι.",
      "Η σύζυγός του, Ντάνα Ζατοπκοβα, κέρδισε το χρυσό μετάλλιο στον ακοντισμό την ίδια ακριβώς ημέρα που ο Ζάτοπεκ κέρδισε τα 5.000 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BC%CE%AF%CE%BB_%CE%96%CE%AC%CF%84%CE%BF%CF%80%CE%B5%CE%BA",
    "locale": "el-GR",
    "tags": ["zatopek", "helsinki-1952", "distance-running", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_014",
    "text": "Ποιος Γερμανός τενίστας έγινε το 1985 ο νεότερος νικητής στην ιστορία του απλού ανδρών στο Wimbledon σε ηλικία μόλις 17 ετών;",
    "answers": ["Μίχαελ Στιχ", "Τόμι Χάας", "Αλεξάντερ Ζβέρεφ", "Μπόρις Μπέκερ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Boris Becker κατέκτησε το Wimbledon το 1985 σε ηλικία 17 ετών και 227 ημερών όντας μάλιστα εκτός ταμπλό seeded παικτών.",
    "funFacts": [
      "Έγινε ο πρώτος μη διαβαθμισμένος (unseeded) παίκτης και ο πρώτος Γερμανός που κατέκτησε το ιστορικό λονδρέζικο τουρνουά.",
      "Έμεινε γνωστός για τις εντυπωσιακές βουτιές του στο γρασίδι για να αποκρούσει μπάλες στο φιλέ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%8C%CF%81%CE%B9%CF%82_%CE%9C%CF%80%CE%AD%CE%BA%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["boris-becker", "wimbledon-1985", "tennis-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_easy_015_dup_avoid",
    "id": "sports_med_015",
    "text": "Ποιος πιλότος κατέχει το απόλυτο ρεκόρ των περισσότερων pole positions στην ιστορία της Formula 1 ξεπερνώντας τις 100;",
    "answers": ["Λιούις Χάμιλτον", "Μίχαελ Σουμάχερ", "Άιρτον Σένα", "Σεμπάστιαν Φέτελ"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Lewis Hamilton είναι ο μοναδικός οδηγός στην ιστορία της Formula 1 που έχει ξεπεράσει τις 100 pole positions σε κατατακτήριες δοκιμές.",
    "funFacts": [
      "Σημείωσε την 100ή του pole position στο Ισπανικό Grand Prix της Βαρκελώνης το 2021.",
      "Ακολουθεί στη σχετική λίστα ο Michael Schumacher με 68 και ο Ayrton Senna με 65 pole positions."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%B9%CE%BF%CF%8D%CE%B9%CF%82_%CE%A7%CE%AC%CE%BC%CE%B9%CE%BB%CF%84%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["hamilton", "formula-1", "pole-positions"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_016",
    "text": "Ποιος Σενεγαλέζος επιθετικός πέτυχε το ταχύτερο χατ-τρικ στην ιστορία της Premier League σε μόλις 2 λεπτά και 56 δευτερόλεπτα το 2015;",
    "answers": ["Μοχάμεντ Σαλάχ", "Σαντιό Μανέ", "Ντιντιέ Ντρογκμπά", "Πιερ-Εμερίκ Ομπαμεγιάνγκ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Sadio Mané, αγωνιζόμενος για τη Σαουθάμπτον εναντίον της Άστον Βίλα τον Μάιο του 2015, πέτυχε 3 γκολ σε χρόνο ρεκόρ 176 δευτερολέπτων.",
    "funFacts": [
      "Κατέρριψε το ρεκόρ του Robbie Fowler από το 1994 (4 λεπτά και 33 δευτερόλεπτα για τη Λίβερπουλ κατά της Άρσεναλ).",
      "Αργότερα μεταγράφηκε στη Λίβερπουλ όπου κατέκτησε το Champions League (2019) και την Premier League (2020)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CE%B1%CE%BD%CF%84%CE%B9%CF%8C_%CE%9C%CE%B1%CE%BD%CE%AD",
    "locale": "el-GR",
    "tags": ["mane", "premier-league", "hat-trick", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_017",
    "text": "Ποιος Αυστραλός κολυμβητής ('Thorpedo') κατέκτησε 5 χρυσά ολυμπιακά μετάλλια και κυριάρχησε στα αγωνίσματα ελευθέρου στα τέλη του '90 και αρχές του 2000;",
    "answers": ["Γκραντ Χάκετ", "Μάικλ Κλιμ", "Ίαν Θορπ", "Μακ Χόρτον"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Ian Thorpe υπήρξε το μεγαλύτερο αθλητικό είδωλο της Αυστραλίας κερδίζοντας 3 χρυσά στο Σίδνεϊ το 2000 και 2 χρυσά στην Αθήνα το 2004.",
    "funFacts": [
      "Σε ηλικία μόλις 15 ετών έγινε ο νεότερος παγκόσμιος πρωταθλητής στην ιστορία της κολύμβησης (Περθ, 1998 στα 400μ ελεύθερο).",
      "Είχε χαρακτηριστικά τεράστιο μέγεθος πελμάτων (νούμερο υποδημάτων 52), που λειτουργούσαν σχεδόν σαν φυσικά βατραχοπέδιλα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%8A%CE%B1%CE%BD_%CE%98%CE%BF%CF%81%CF%80",
    "locale": "el-GR",
    "tags": ["ian-thorpe", "swimming", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_018",
    "text": "Σε ποια ευρωπαϊκή πόλη κατέκτησε ο Ολυμπιακός το πρώτο του τρόπαιο EuroLeague στο Final Four του 1997 με προπονητή τον Ντούσαν Ίβκοβιτς;",
    "answers": ["Στο Παρίσι", "Στο Τελ Αβίβ", "Στη Σαραγόσα", "Στη Ρώμη"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στο Final Four της Ρώμης τον Απρίλιο του 1997, ο Ολυμπιακός επικράτησε της Μπαρτσελόνα στον τελικό με 73-58.",
    "funFacts": [
      "Ο Αμερικανός σούπερ σταρ Ντέιβιντ Ρίβερς πραγματοποίησε μαγική εμφάνιση σημειώνοντας 26 πόντους και αναδείχθηκε MVP του Final Four.",
      "Εκείνη τη χρονιά ο Ολυμπιακός πέτυχε το Triple Crown κατακτώντας Πρωτάθλημα, Κύπελλο Ελλάδας και EuroLeague."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CF%8C%CF%82_%CE%A3.%CE%A6.%CE%A0._(%CE%BA%CE%B1%CE%BB%CE%B1%CE%B8%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["olympiacos-1997", "euroleague", "rome-1997", "basketball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_019",
    "text": "Σε ποια χρονιά και σε ποια γαλλική πόλη διεξήχθησαν οι πρώτοι ιστορικοί Χειμερινοί Ολυμπιακοί Αγώνες;",
    "answers": ["Το 1924 στο Σαμονί", "Το 1928 στο Σεντ Μόριτζ", "Το 1932 στο Λέικ Πλάσιντ", "Το 1920 στην Αμβέρσα"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Οι πρώτοι Χειμερινοί Ολυμπιακοί Αγώνες πραγματοποιήθηκαν στο Σαμονί (Chamonix) στους πρόποδες του Λευκού Όρους το 1924.",
    "funFacts": [
      "Αρχικά ονομάστηκαν 'Διεθνής Εβδομάδα Χειμερινών Αθλημάτων' και αναγνωρίστηκαν αναδρομικά ως η 1η Χειμερινή Ολυμπιάδα από τη ΔΟΕ το 1925.",
      "Συμμετείχαν 258 αθλητές από 16 χώρες σε 16 αγωνίσματα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A7%CE%B5%CE%B9%CE%BC%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1924",
    "locale": "el-GR",
    "tags": ["chamonix-1924", "winter-olympics", "history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_020",
    "text": "Ποιος Ιταλός προπονητής οδήγησε τη Λέστερ Σίτι στο ανεπανάληπτο θαύμα της κατάκτησης της Premier League τη σεζόν 2015-16;",
    "answers": ["Κάρλο Αντσελότι", "Κλαούντιο Ρανιέρι", "Αντόνιο Κόντε", "Ρομπέρτο Μαντσίνι"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Claudio Ranieri οδήγησε τη Λέστερ σε ένα από τα μεγαλύτερα αθλητικά κατορθώματα όλων των εποχών, με τις στοιχηματικές εταιρείες να δίνουν αρχικά πιθανότητα 5.000 προς 1.",
    "funFacts": [
      "Ο Ranieri είχε απολυθεί λίγους μήνες νωρίτερα από την Εθνική Ελλάδας μετά την ήττα από τα Νησιά Φερόε.",
      "Βραβεύτηκε ως ο κορυφαίος προπονητής στον κόσμο για το 2016 από τη FIFA (The Best FIFA Men's Coach)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%B1%CE%BF%CF%8D%CE%BD%CF%84%CE%B9%CE%BF_%CE%A1%CE%B1%CE%BD%CE%B9%CE%AD%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["ranieri", "leicester", "premier-league-2016"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_021",
    "text": "Σε ποιο ύψος έφτασε το ιστορικό παγκόσμιο ρεκόρ στο άλμα εις ύψος γυναικών η Ουκρανή Γιαροσλάβα Μάχουτσικ το 2024 καταρρίπτοντας το ρεκόρ της Κοσταντίνοβα;",
    "answers": ["2,08 μέτρα", "2,12 μέτρα", "2,10 μέτρα", "2,06 μέτρα"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 7 Ιουλίου 2024 στο Παρίσι, η Yaroslava Mahuchikh υπερέβη τα 2,10 μέτρα καταρρίπτοντας το ρεκόρ των 2,09 μ. της Stefka Kostadinova που κρατούσε από το 1987.",
    "funFacts": [
      "Το προηγούμενο ρεκόρ της Βουλγάρας Κοσταντίνοβα είχε παραμείνει ακατάρριπτο για 37 ολόκληρα χρόνια.",
      "Λίγες εβδομάδες αργότερα, η Μάχουτσικ κατέκτησε και το χρυσό ολυμπιακό μετάλλιο στους Αγώνες του Παρισιού 2024."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%BC%CE%B1_%CE%B5%CE%B9%CF%82_%CF%8D%CF%88%CE%BF%CF%82",
    "locale": "el-GR",
    "tags": ["high-jump", "mahuchikh", "world-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_022",
    "text": "Ποιος θρυλικός Αμερικανός πυγμάχος βαρέων βαρών αποσύρθηκε το 1956 παραμένοντας αήττητος με το τέλειο ρεκόρ 49-0 (43 νοκ-άουτ);",
    "answers": ["Τζο Λούις", "Σόνι Λίστον", "Τζακ Ντέμπσεϊ", "Ρόκι Μαρτσιάνο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Rocky Marciano είναι ο μοναδικός παγκόσμιος πρωταθλητής βαρέων βαρών που ολοκλήρωσε την καριέρα του χωρίς ούτε μία ήττα ή ισοπαλία.",
    "funFacts": [
      "Το ρεκόρ του των 49-0 έμεινε ασυναγώνιστο μέχρι το 2017, όταν ο Floyd Mayweather Jr. έφτασε το 50-0 στην κατηγορία ημιβαρέων/μέσων βαρών.",
      "Έχασε τραγικά τη ζωή του σε αεροπορικό δυστύχημα το 1969, μία ημέρα πριν από τα 46α γενέθλιά του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CF%8C%CE%BA%CE%B9_%CE%9C%CE%B1%CF%81%CF%84%CF%83%CE%B9%CE%AC%CE%BD%CE%BF",
    "locale": "el-GR",
    "tags": ["marciano", "boxing", "undefeated"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_023",
    "text": "Ποιος Ιταλός φόργουορντ/σέντερ έγινε το 2006 ο πρώτος Ευρωπαίος παίκτης που επιλέχθηκε στο No. 1 του NBA Draft (από τους Toronto Raptors);",
    "answers": ["Αντρέα Μπαρνιάνι", "Ντανίλο Γκαλινάρι", "Μάρκο Μπελινέλι", "Πάου Γκασόλ"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Andrea Bargnani επιλέχθηκε στην κορυφή του Draft το 2006 από τους Τορόντο Ράπτορς, γράφοντας ιστορία για το ευρωπαϊκό μπάσκετ.",
    "funFacts": [
      "Πριν από αυτόν, ο Dirk Nowitzki και ο Pau Gasol είχαν επιλεγεί ψηλά αλλά όχι στο No. 1.",
      "Αγωνίστηκε 10 σεζόν στο NBA σημειώνοντας κατά μέσο όρο 14,3 πόντους ανά παιχνίδι."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%81%CE%AD%CE%B1_%CE%9C%CF%80%CE%B1%CF%81%CE%BD%CE%B9%CE%AC%CE%BD%CE%B9",
    "locale": "el-GR",
    "tags": ["bargnani", "nba-draft", "raptors"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_024",
    "text": "Ποια χώρα έγινε η πρώτη αφρικανική και αραβική εθνική ομάδα στην ιστορία που έφτασε στα ημιτελικά του Παγκοσμίου Κυπέλλου (Κατάρ 2022);",
    "answers": ["Σενεγάλη", "Μαρόκο", "Καμερούν", "Γκάνα"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Μαρόκο του Ουαλίντ Ρεγκραγκί απέκλεισε την Ισπανία και την Πορτογαλία φτάνοντας στους '4' του Μουντιάλ 2022.",
    "funFacts": [
      "Μέχρι τα ημιτελικά δεν είχε δεχτεί κανένα γκολ από αντίπαλο παίκτη, με το μοναδικό γκολ παθητικό να είναι ένα αυτογκόλ κόντρα στον Καναδά.",
      "Τερμάτισε στην 4η θέση της διοργάνωσης μετά τον μικρό τελικό με την Κροατία."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%9C%CE%B1%CF%81%CF%8C%CE%BA%CE%BF%CF%85_(%CF%80%CE%BF%CE%B4%CF%8C%CF%83%CF%86%CE%B1%CE%B9%CF%81%CE%BF_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["morocco-2022", "world-cup", "africa"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_025",
    "text": "Ποιος Αυστραλός θρύλος του τένις είναι ο μόνος παίκτης στην ιστορία που πέτυχε το Calendar Grand Slam (και τα 4 major την ίδια χρονιά) δύο φορές (1962, 1969);",
    "answers": ["Κεν Ρόσγουολ", "Τζον Νιούκομπ", "Ροντ Λέιβερ", "Λέιτον Χιούιτ"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Rod Laver πέτυχε το απίστευτο επίτευγμα μία φορά ως ερασιτέχνης (1962) και μία στην επαγγελματική Open Era (1969).",
    "funFacts": [
      "Προς τιμήν του, το κεντρικό γήπεδο του Australian Open στη Μελβούρνη ονομάστηκε Rod Laver Arena το 2000.",
      "Είναι επίσης ο εμπνευστής του ετήσιου τουρνουά Laver Cup ανάμεσα στην Team Europe και την Team World."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%BF%CE%BD%CF%84_%CE%9B%CE%AD%CE%B9%CE%B2%CE%B5%CF%81",
    "locale": "el-GR",
    "tags": ["rod-laver", "grand-slam", "tennis-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_026",
    "text": "Ποιος Βέλγος ποδηλάτης αποκλήθηκε 'Ο Κανίβαλος' (The Cannibal) επειδή κέρδισε 5 Γύρους Γαλλίας, 5 Γύρους Ιταλίας και πάνω από 500 αγώνες;",
    "answers": ["Μπερνάρ Ινό", "Ζακ Ανκετίλ", "Φαούστο Κόπι", "Έντι Μερξ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Eddy Merckx θεωρείται ο κορυφαίος ποδηλάτης όλων των εποχών, κυριαρχώντας απόλυτα στις δεκαετίες του 1960 και 1970.",
    "funFacts": [
      "Κέρδισε και τα πέντε 'Μνημεία' της ποδηλασίας (Monuments) τουλάχιστον δύο φορές το καθένα (συνολικά 19 νίκες σε Μνημεία).",
      "Το παρατσούκλι 'Κανίβαλος' του δόθηκε από την κόρη ενός συναθλητή του, επειδή ήθελε να κερδίζει σε κάθε αγώνα χωρίς να αφήνει τίποτα στους αντιπάλους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BD%CF%84%CE%B9_%CE%9C%CE%B5%CF%81%CE%BE",
    "locale": "el-GR",
    "tags": ["merckx", "cycling", "tour-de-france"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_027",
    "text": "Ποιος Έλληνας σπρίντερ κατέκτησε το χρυσό ολυμπιακό μετάλλιο στα 200 μέτρα στους Ολυμπιακούς Αγώνες του Σίδνεϊ το 2000;",
    "answers": ["Κώστας Κεντέρης", "Άγγελος Παυλακάκης", "Περικλής Ιακωβάκης", "Λυκούργος Τσάκωνας"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Κώστας Κεντέρης κέρδισε τα 200μ στο Σίδνεϊ με χρόνο 20,09 από τον 5ο διάδρομο, χαρίζοντας στην Ελλάδα ένα ανεπανάληπτο χρυσό μετάλλιο.",
    "funFacts": [
      "Έγινε ο πρώτος μη Αμερικανός αθλητής που κέρδισε τα 200μ σε Ολυμπιάδα μετά το 1980.",
      "Στη συνέχεια κατέκτησε το χρυσό στο Παγκόσμιο Πρωτάθλημα του Έντμοντον (2001) και στο Ευρωπαϊκό του Μονάχου (2002), κάνοντας το σπάνιο 'triple crown' στα 200μ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CF%83%CF%84%CE%B1%CF%82_%CE%9A%CE%B5%CE%BD%CF%84%CE%AD%CF%81%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["kenteris", "sydney-2000", "200m", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_028",
    "text": "Σε ποια ιταλική ομάδα μεταγράφηκε ο Ντιέγκο Μαραντόνα το 1984 από την Μπαρτσελόνα, οδηγώντας την στα μόνα δύο πρωταθλήματα της ιστορίας της εκείνη την εποχή;",
    "answers": ["Γιουβέντους", "Νάπολι", "Μίλαν", "Ίντερ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Maradona λατρεύτηκε σαν θεός στη Νάπολι, κατακτώντας τα Scudetti του 1987 και του 1990, καθώς και το Κύπελλο UEFA το 1989.",
    "funFacts": [
      "Περισσότεροι από 75.000 οπαδοί κατέκλυσαν το γήπεδο Σαν Πάολο μόνο για την επίσημη παρουσίασή του στις 5 Ιουλίου 1984.",
      "Μετά τον θάνατό του το 2020, το στάδιο της Νάπολι μετονομάστηκε επίσημα σε 'Stadio Diego Armando Maradona'."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CE%B9%CE%AD%CE%B3%CE%BA%CE%BF_%CE%9C%CE%B1%CF%81%CE%B1%CE%BD%CF%84%CF%8C%CE%BD%CE%B1",
    "locale": "el-GR",
    "tags": ["maradona", "napoli", "serie-a"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_029",
    "text": "Με ποια ομάδα κατέκτησε ο Ισπανός πιλότος Φερνάντο Αλόνσο τα δύο συνεχόμενα παγκόσμια πρωταθλήματα Formula 1 το 2005 και το 2006;",
    "answers": ["Ferrari", "McLaren", "Renault", "Williams"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Fernando Alonso έβαλε τέλος στην πενταετή κυριαρχία του Schumacher κατακτώντας τους τίτλους του 2005 και 2006 με την ομάδα της Renault υπό τον Φλάβιο Μπριατόρε.",
    "funFacts": [
      "Το 2005 έγινε ο νεότερος παγκόσμιος πρωταθλητής στην ιστορία της Formula 1 μέχρι τότε (σε ηλικία 24 ετών).",
      "Είναι ο μόνος Ισπανός πιλότος που έχει κατακτήσει τον παγκόσμιο τίτλο στη Formula 1."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%B5%CF%81%CE%BD%CE%AC%CE%BD%CF%84%CE%BF_%CE%91%CE%BB%CF%8C%CE%BD%CF%83%CE%BF",
    "locale": "el-GR",
    "tags": ["alonso", "renault", "formula-1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_030",
    "text": "Ποια ομάδα επέλεξε τον Κόμπι Μπράιαντ στο No. 13 του NBA Draft το 1996 πριν τον ανταλλάξει άμεσα στους Λος Άντζελες Λέικερς;",
    "answers": ["Νιου Τζέρσεϊ Νετς", "Μινεσότα Τίμπεργουλβς", "Γκόλντεν Στέιτ Ουόριορς", "Σάρλοτ Χόρνετς"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Οι Charlotte Hornets επέλεξαν τον 17χρονο Kobe Bryant απευθείας από το λύκειο και τον αντάλλαξαν στους Lakers για τον σέντερ Vlade Divac.",
    "funFacts": [
      "Η συμφωνία είχε κανονιστεί πριν από το draft από τον διορατικό γενικό διευθυντή των Lakers, Jerry West.",
      "Ο Kobe πέρασε και τα 20 χρόνια της επαγγελματικής του καριέρας αποκλειστικά στους Lakers, κερδίζοντας 5 πρωταθλήματα NBA."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CE%BC%CF%80%CE%B9_%CE%9C%CF%80%CF%81%CE%AC%CE%B9%CE%B1%CE%BD%CF%84",
    "locale": "el-GR",
    "tags": ["kobe-bryant", "nba-draft-1996", "lakers"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_031",
    "text": "Σε ποιους Ολυμπιακούς Αγώνες επετράπη για πρώτη φορά η συμμετοχή γυναικών αθλητριών;",
    "answers": ["Το 1900 στο Παρίσι", "Το 1896 στην Αθήνα", "Το 1908 στο Λονδίνο", "Το 1924 στο Παρίσι"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στους 2ους Ολυμπιακούς Αγώνες στο Παρίσι το 1900 συμμετείχαν 22 γυναίκες σε αθλήματα όπως το τένις, το γκολφ και η ιστιοπλοΐα.",
    "funFacts": [
      "Η Βρετανίδα τενίστρια Σάρλοτ Κούπερ έγινε η πρώτη γυναίκα ολυμπιονίκης στην ιστορία κερδίζοντας το απλό γυναικών.",
      "Ο βαρόνος Πιερ ντε Κουμπερτέν αρχικά αντιτίθεται σθεναρά στη συμμετοχή των γυναικών στους Αγώνες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1900",
    "locale": "el-GR",
    "tags": ["paris-1900", "women-in-sports", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_032",
    "text": "Πώς ονομαζόταν το αρχικό χρυσό τρόπαιο του Παγκοσμίου Κυπέλλου Ποδοσφαίρου, το οποίο δόθηκε οριστικά στη Βραζιλία το 1970;",
    "answers": ["Κύπελλο Εθνών", "Τρόπαιο Ζιλ Ριμέ (Jules Rimet)", "Χρυσή Νίκη", "Κύπελλο FIFA"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το τρόπαιο ονομάστηκε προς τιμήν του προέδρου της FIFA Ζιλ Ριμέ. Σύμφωνα με τον κανονισμό, η πρώτη χώρα που θα συμπλήρωνε 3 κατακτήσεις (Βραζιλία, 1970) θα το κρατούσε για πάντα.",
    "funFacts": [
      "Απεικόνιζε τη Νίκη, την αρχαιοελληνική θεά της νίκης, να κρατά ένα οκταγωνικό κύπελλο.",
      "Το πρωτότυπο τρόπαιο κλάπηκε στο Ρίο ντε Τζανέιρο το 1983 και πιστεύεται ότι έλιωσε από τους δράστες για τον χρυσό του."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CF%8C%CF%80%CE%B1%CE%B9%CE%BF_%CE%A0%CE%B1%CE%B3%CE%BA%CE%BF%CF%83%CE%BC%CE%AF%CE%BF%CF%85_%CE%9A%CF%85%CF%80%CE%AD%CE%BB%CE%BB%CE%BF%CF%85_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["jules-rimet", "world-cup", "trophy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_033",
    "text": "Ποιος Αμερικανός κολυμβητής κέρδισε 7 χρυσά μετάλλια καταρρίπτοντας παγκόσμιο ρεκόρ και στα 7 αγωνίσματα στους Ολυμπιακούς του Μονάχου το 1972;",
    "answers": ["Ματ Μπιόντι", "Τζόνι Βαϊσμίλερ", "Μαρκ Σπιτς", "Μάικλ Φελπς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Mark Spitz σημείωσε ένα από τα μεγαλύτερα επιτεύγματα στον αθλητισμό κερδίζοντας 7 χρυσά με 7 παγκόσμια ρεκόρ σε μία διοργάνωση.",
    "funFacts": [
      "Το ρεκόρ του διατηρήθηκε για 36 ολόκληρα χρόνια, μέχρι να το καταρρίψει ο Michael Phelps με 8 χρυσά στο Πεκίνο το 2008.",
      "Ήταν διάσημος για το χαρακτηριστικό του μουστάκι, σε μια εποχή που όλοι οι κολυμβητές ξύριζαν κάθε τρίχα για μείωση της τριβής."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%BA_%CE%A3%CF%80%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["mark-spitz", "munich-1972", "swimming-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_034",
    "text": "Ποιος Έλληνας μπασκετμπολίστας του Ηρακλή Θεσσαλονίκης κατέχει το απόλυτο ρεκόρ πόντων σε έναν αγώνα ελληνικού πρωταθλήματος (110 πόντοι το 1972);",
    "answers": ["Νίκος Γκάλης", "Παναγιώτης Γιαννάκης", "Βασίλης Γκούμας", "Αριστείδης Μούμογλου"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 13 Ιουλίου 1972, ο Αριστείδης Μούμογλου σημείωσε 110 πόντους στη νίκη του Ηρακλή επί του ΒΑΟ με 170-94, σε εποχή μάλιστα χωρίς τρίποντο.",
    "funFacts": [
      "Είναι η πέμπτη υψηλότερη επίδοση πόντων σε έναν αγώνα μπάσκετ παγκοσμίως σε εθνικά πρωταθλήματα πρώτης κατηγορίας.",
      "Στη δεύτερη θέση στην Ελλάδα βρίσκεται ο Παναγιώτης Γιαννάκης με 73 πόντους για τον Ιωνικό Νικαίας το 1981."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CF%81%CE%B9%CF%83%CF%84%CE%B5%CE%AF%CE%B4%CE%B7%CF%82_%CE%9C%CE%BF%CF%8D%CE%BC%CE%BF%CE%B3%CE%BB%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["moumoglou", "greek-basketball", "records", "110-points"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_035",
    "text": "Σε ποια χρονιά και σε ποιους Ολυμπιακούς Αγώνες πέτυχε ο Μπομπ Μπίμον το εξωπραγματικό άλμα εις μήκος στα 8,90 μέτρα;",
    "answers": ["Το 1968 στην Πόλη του Μεξικού", "Το 1972 στο Μόναχο", "Το 1964 στο Τόκιο", "Το 1976 στο Μόντρεαλ"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Bob Beamon ξεπέρασε το προηγούμενο παγκόσμιο ρεκόρ κατά 55 ολόκληρα εκατοστά, πραγματοποιώντας ένα άλμα που χαρακτηρίστηκε ως 'άλμα στον 21ο αιώνα'.",
    "funFacts": [
      "Το οπτικό σύστημα μέτρησης του σταδίου δεν επαρκούσε για τόσο μεγάλο άλμα και οι κριτές αναγκάστηκαν να φέρουν χειροκίνητη μεταλλική μεζούρα.",
      "Το ολυμπιακό ρεκόρ του Beamon παραμένει ακατάρριπτο μέχρι σήμερα, όντας το μακροβιότερο ολυμπιακό ρεκόρ στον στίβο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%BF%CE%BC%CF%80_%CE%9C%CF%80%CE%AF%CE%BC%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["bob-beamon", "mexico-1968", "long-jump", "world-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_036",
    "text": "Ποια εθνική ομάδα ανδρών κυριάρχησε στο παγκόσμιο βόλεϊ κερδίζοντας 3 συνεχόμενα Παγκόσμια Πρωταθλήματα (2002, 2006, 2010);",
    "answers": ["Ιταλία", "Βραζιλία", "Ρωσία", "Πολωνία"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Βραζιλία υπό την καθοδήγηση του προπονητή Μπερνάρντο Ρεζέντε (Μπερναρντίνιο) και αστέρες όπως ο Giba δημιούργησε μια από τις σπουδαιότερες δυναστείες στην ιστορία του βόλεϊ.",
    "funFacts": [
      "Την ίδια περίοδο κατέκτησε επίσης το χρυσό ολυμπιακό μετάλλιο στην Αθήνα το 2004 και δύο ασημένια (2008, 2012).",
      "Κέρδισε συνολικά 9 τίτλους FIVB World League μεταξύ 2001 και 2010."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%92%CF%81%CE%B1%CE%B6%CE%B9%CE%BB%CE%AF%CE%B1%CF%82_(%CF%80%CE%B5%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["brazil-volleyball", "world-championship", "volleyball"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_037",
    "text": "Ποιος Γάλλος ποδοσφαιριστής κατέχει το αξεπέραστο ρεκόρ των περισσότερων γκολ σε μία μόνο τελική φάση Παγκοσμίου Κυπέλλου (13 γκολ το 1958);",
    "answers": ["Μισέλ Πλατινί", "Κιλιάν Εμπαπέ", "Ζυστ Φονταίν", "Ραϊμόν Κοπά"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Just Fontaine σημείωσε 13 γκολ σε μόλις 6 αγώνες στο Παγκόσμιο Κύπελλο της Σουηδίας το 1958, οδηγώντας τη Γαλλία στην 3η θέση.",
    "funFacts": [
      "Πέτυχε 4 γκολ στον μικρό τελικό εναντίον της Δυτικής Γερμανίας (6-3).",
      "Αγωνίστηκε σε όλο το τουρνουά φορώντας δανεικά ποδοσφαιρικά παπούτσια από τον συμπαίκτη του Stéphane Bruey, καθώς τα δικά του είχαν καταστραφεί."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CF%85%CF%83%CF%84_%CE%A6%CE%BF%CE%BD%CF%84%CE%B1%CE%AF%CE%BD",
    "locale": "el-GR",
    "tags": ["just-fontaine", "world-cup-1958", "goal-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_038",
    "text": "Ποιος Αυστριακός 3 φορές παγκόσμιος πρωταθλητής της Formula 1 επέστρεψε στους αγώνες μόλις 42 ημέρες μετά το φρικτό ατύχημά του στο Nürburgring το 1976;",
    "answers": ["Γιοχεν Ριντ", "Γκέρχαρντ Μπέργκερ", "Χέλμουτ Μάρκο", "Νίκι Λάουντα"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Niki Lauda υπέστη σοβαρότατα εγκαύματα και εισέπνευσε τοξικούς καπνούς, αλλά επέστρεψε ηρωικά στο Grand Prix της Μόντσα την ίδια χρονιά.",
    "funFacts": [
      "Η επική αντιπαλότητά του με τον Βρετανό James Hunt το 1976 αποτυπώθηκε στη διάσημη κινηματογραφική ταινία 'Rush' του 2013.",
      "Κέρδισε παγκόσμια πρωταθλήματα τόσο με τη Ferrari (1975, 1977) όσο και με τη McLaren (1984)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CE%AF%CE%BA%CE%B9_%CE%9B%CE%AC%CE%BF%CF%85%CE%BD%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["niki-lauda", "formula-1", "ferrari", "motorsport"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_039",
    "text": "Ποια ομάδα του NBA κατέχει το ιστορικό ρεκόρ των 8 συνεχόμενων κατακτήσεων πρωταθλήματος (1959–1966);",
    "answers": ["Μπόστον Σέλτικς", "Λος Άντζελες Λέικερς", "Σικάγο Μπουλς", "Γκόλντεν Στέιτ Ουόριορς"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Υπό την καθοδήγηση του προπονητή Red Auerbach και με ηγέτη τον Bill Russell, οι Boston Celtics δημιούργησαν τη μακροβιότερη δυναστεία στον επαγγελματικό αθλητισμό των ΗΠΑ.",
    "funFacts": [
      "Συνολικά εκείνη η ομάδα κατέκτησε 11 πρωταθλήματα NBA σε 13 σεζόν (1957–1969).",
      "Στους τελικούς του 1962 και του 1966 κέρδισαν τους Lakers στον 7ο και καθοριστικό αγώνα με διαφορά μόλις 3 και 2 πόντων αντίστοιχα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CF%8C%CF%83%CF%84%CE%BF%CE%BD_%CE%A3%CE%AD%CE%BB%CF%84%CE%B9%CE%BA%CF%82",
    "locale": "el-GR",
    "tags": ["celtics", "nba-dynasty", "bill-russell"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_040",
    "text": "Ποιος Κροάτης τενίστας έγινε το 2001 ο πρώτος παίκτης στην ιστορία που κέρδισε το Wimbledon μπαίνοντας στο τουρνουά με κάρτα ελευθέρας (wildcard);",
    "answers": ["Μάριν Τσίλιτς", "Γκόραν Ιβανίσεβιτς", "Ιβάν Λιούμπισιτς", "Μάριο Άντσιτς"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Goran Ivanišević, έχοντας χάσει τρεις προηγούμενους τελικούς Wimbledon και όντας στο Νο. 125 της κατάταξης, πέτυχε έναν από τους πιο συναισθηματικούς θριάμβους στο τένις.",
    "funFacts": [
      "Ο τελικός της Δευτέρας (People's Monday) εναντίον του Pat Rafter παρακολουθήθηκε από ένα εκστασιασμένο πλήθος 10.000 οπαδών που περίμεναν όλη νύχτα.",
      "Σημείωσε 213 άσους σε όλο το τουρνουά του 2001, επίδοση που παραμένει ρεκόρ όλων των εποχών για μία διοργάνωση Wimbledon."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CF%8C%CF%81%CE%B1%CE%BD_%CE%99%CE%B2%CE%B1%CE%BD%CE%AF%CF%83%CE%B5%CE%B2%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["ivanisevic", "wimbledon-2001", "tennis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_041",
    "text": "Σε ποια κατηγορία βάρους στην άρση βαρών συγκλόνισε ο Βαλέριος Λεωνίδης στη συγκλονιστική μονομαχία με τον Ναΐμ Σουλεϊμάνογλου στην Ατλάντα το 1996;",
    "answers": ["59 κιλά", "70 κιλά", "64 κιλά", "54 κιλά"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στην κατηγορία των 64 κιλών, ο Λεωνίδης κατέκτησε το ασημένιο ολυμπιακό μετάλλιο σηκώνοντας 332,5 κιλά στο σύνολο, σε μια από τις σπουδαιότερες αναμετρήσεις στην ιστορία του αθλήματος.",
    "funFacts": [
      "Και οι δύο αθλητές κατέρριψαν διαδοχικά παγκόσμια ρεκόρ κατά τη διάρκεια του τελικού της Ατλάντα.",
      "Όταν ο Σουλεϊμάνογλου πέθανε πρόωρα το 2017, ο Λεωνίδης ταξίδεψε στην Κωνσταντινούπολη και φίλησε συγκινημένος το φέρετρο του μεγάλου του αντιπάλου και φίλου."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B1%CE%BB%CE%AD%CF%81%CE%B9%CE%BF%CF%82_%CE%9B%CE%B5%CF%89%CE%BD%CE%AF%CE%B4%CE%B7%CF%82",
    "locale": "el-GR",
    "tags": ["leonidis", "weightlifting", "atlanta-1996", "greece"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_042",
    "text": "Σε ποιο ιστορικό στάδιο του Λονδίνου διεξήχθη ο τελικός του Παγκοσμίου Κυπέλλου του 1966, όπου η Αγγλία νίκησε τη Δυτική Γερμανία με 4-2;",
    "answers": ["Ολντ Τράφορντ", "Στάμφορντ Μπριτζ", "Χάιμπουρι", "Στάδιο Γουέμπλεϊ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το στάδιο Wembley φιλοξένησε τον τελικό του 1966 με τους διάσημους δίδυμους πύργους του (Twin Towers) μπροστά σε 96.924 θεατές.",
    "funFacts": [
      "Ο Τζεφ Χερστ έγινε ο πρώτος παίκτης στην ιστορία που σημείωσε χατ-τρικ σε τελικό Παγκοσμίου Κυπέλλου.",
      "Το τρίτο γκολ της Αγγλίας ('Wembley goal') παραμένει η πιο πολυσυζητημένη φάση στην ιστορία του ποδοσφαίρου για το αν η μπάλα πέρασε ολόκληρη τη γραμμή."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B5%CE%BB%CE%B9%CE%BA%CF%8C%CF%82_%CE%A0%CE%B1%CE%B3%CE%BA%CE%BF%CF%83%CE%BC%CE%AF%CE%BF%CF%85_%CE%9A%CF%85%CF%80%CE%AD%CE%BB%CE%BB%CE%BF%CF%85_%CE%A0%CE%BF%CE%B4%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%BF%CF%85_1966",
    "locale": "el-GR",
    "tags": ["wembley-1966", "world-cup", "england-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_043",
    "text": "Ποιο είναι το επίσημο βάρος της σφύρας (μαζί με το καλώδιο και τη λαβή) στη σφυροβολία ανδρών στους Ολυμπιακούς Αγώνες;",
    "answers": ["7,26 κιλά", "8,00 κιλά", "6,50 κιλά", "5,00 κιλά"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το βάρος της σφύρας ανδρών είναι ακριβώς 7,26 κιλά (16 λίβρες), το ίδιο ακριβώς βάρος με τη σφαίρα στη σφαιροβολία ανδρών.",
    "funFacts": [
      "Στη σφυροβολία γυναικών το αντίστοιχο βάρος είναι ακριβώς 4 κιλά.",
      "Το παγκόσμιο ρεκόρ ανδρών κατέχει ο Σοβιετικός Γιούρι Σεντίχ από το 1986 με την τρομερή βολή στα 86,74 μέτρα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%86%CF%85%CF%81%CE%BF%CE%B2%CE%BF%CE%BB%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["hammer-throw", "athletics", "field-events"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_044",
    "text": "Ποια εθνική ομάδα ανδρών κατέχει το ρεκόρ των περισσότερων κατακτήσεων στο Παγκόσμιο Πρωτάθλημα Χειροσφαίρισης (Χάντμπολ) με 6 τίτλους;",
    "answers": ["Σουηδία", "Γαλλία", "Γερμανία", "Δανία"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Γαλλία (γνωστή διαδοχικά ως 'Les Barjots', 'Les Costauds' και 'Les Experts') κατέκτησε τον παγκόσμιο τίτλο το 1995, 2001, 2009, 2011, 2015 και 2017.",
    "funFacts": [
      "Ο εμβληματικός της παίκτης Νικολά Καραμπατίτς αναδείχθηκε 3 φορές κορυφαίος παίκτης του κόσμου από την IHF.",
      "Η Γαλλία έγινε η πρώτη ομάδα χάντμπολ που κατείχε ταυτόχρονα τον τίτλο της Ολυμπιονίκη, της Παγκόσμιας Πρωταθλήτριας και της Πρωταθλήτριας Ευρώπης."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%B1%CE%B3%CE%BA%CF%8C%CF%83%CE%BC%CE%B9%CE%BF_%CE%A0%CF%81%CF%89%CF%84%CE%AC%CE%B8%CE%BB%CE%B7%CE%BC%CE%B1_%CE%A7%CE%B5%CE%B9%CF%81%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7%CF%82_%CE%91%CE%BD%CE%B4%CF%81%CF%8E%CE%BD",
    "locale": "el-GR",
    "tags": ["handball", "france-handball", "records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_045",
    "text": "Ποια χώρα κατέχει το ιστορικό ρεκόρ των περισσότερων χρυσών ολυμπιακών μεταλλίων στην υδατοσφαίριση ανδρών (συνολικά 9 χρυσά);",
    "answers": ["Ιταλία", "Σερβία", "Ουγγαρία", "Κροατία"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Ουγγαρία είναι η απόλυτη παραδοσιακή υπερδύναμη του πόλο, κερδίζοντας μεταξύ άλλων τρία συνεχόμενα χρυσά το 2000, 2004 και 2008.",
    "funFacts": [
      "Ο ημιτελικός των Ολυμπιακών Αγώνων της Μελβούρνης το 1956 μεταξύ Ουγγαρίας και ΕΣΣΔ έμεινε στην ιστορία ως ο 'Αγώνας στο Αίμα' (Blood in the Water match).",
      "Ο Ούγγρος Dezső Gyarmati κέρδισε μετάλλια σε πέντε διαδοχικές Ολυμπιάδες μεταξύ 1948 και 1964."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A5%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CF%83%CF%84%CE%BF%CF%85%CF%82_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CF%8D%CF%82_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82",
    "locale": "el-GR",
    "tags": ["hungary-waterpolo", "water-polo", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_046",
    "text": "Ποιος θρύλος του NBA κατέκτησε 11 δαχτυλίδια πρωταθλητή με τους Σέλτικς και το βραβείο MVP των Τελικών του NBA φέρει σήμερα το όνομά του;",
    "answers": ["Καρίμ Αμπντούλ-Τζαμπάρ", "Ουίλτ Τσάμπερλεϊν", "Τζέρι Ουέστ", "Μπιλ Ράσελ"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Bill Russell είναι ο πιο επιτυχημένος παίκτης στην ιστορία των ομαδικών σπορ της Βόρειας Αμερικής με 11 τίτλους σε 13 σεζόν.",
    "funFacts": [
      "Στους δύο τελευταίους τίτλους του (1968, 1969) εκτελούσε ταυτόχρονα και χρέη πρώτου προπονητή (παίκτης-προπονητής), όντας ο πρώτος μαύρος προπονητής στο NBA.",
      "Μετά τον θάνατό του το 2022, το NBA απέσυρε τη φανέλα με το νούμερο 6 από όλες ανεξαιρέτως τις ομάδες της λίγκας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B9%CE%BB_%CE%A1%CE%AC%CF%83%CE%B5%CE%BB",
    "locale": "el-GR",
    "tags": ["bill-russell", "celtics", "nba-history"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_047",
    "text": "Ποια χώρα κατέκτησε το Κόπα Αμέρικα δύο διαδοχικές φορές, το 2021 (στο Μαρακανά) και το 2024 (στις ΗΠΑ);",
    "answers": ["Αργεντινή", "Βραζιλία", "Ουρουγουάη", "Χιλή"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Αργεντινή υπό τον Λιονέλ Σκαλόνι και με αρχηγό τον Λιονέλ Μέσι κυριάρχησε απόλυτα κατακτώντας δύο διαδοχικά Copa América και το Παγκόσμιο Κύπελλο 2022.",
    "funFacts": [
      "Με τον τίτλο του 2024 έφτασε τις 16 κατακτήσεις Copa América, ξεπερνώντας την Ουρουγουάη (15) και γινόμενη η πολυνίκης του θεσμού.",
      "Η νίκη του 2021 επί της Βραζιλίας (1-0 με γκολ του Ντι Μαρία) ήταν ο πρώτος μεγάλος διεθνής τίτλος του Μέσι με την ανδρική ομάδα."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CF%80%CE%B1_%CE%91%CE%BC%CE%AD%CF%81%CE%B9%CE%BA%CE%B1",
    "locale": "el-GR",
    "tags": ["copa-america", "argentina", "messi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_048",
    "text": "Ποιος είναι ο μοναδικός οδηγός στην ιστορία του μηχανοκίνητου αθλητισμού που έχει κατακτήσει το 'Triple Crown' (Grand Prix Μονακό, Indy 500, 24 Ώρες Λε Μαν);",
    "answers": ["Φερνάντο Αλόνσο", "Γκράχαμ Χιλ", "Μάριο Αντρέτι", "Χουάν Μανουέλ Φάντζιο"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Βρετανός Graham Hill είναι ο μόνος οδηγός που κέρδισε το GP Μονακό (5 φορές), το Indianapolis 500 (1966) και τις 24 Ώρες του Le Mans (1972).",
    "funFacts": [
      "Υπήρξε δύο φορές παγκόσμιος πρωταθλητής της Formula 1 (1962, 1968).",
      "Ο γιος του, Damon Hill, έγινε επίσης παγκόσμιος πρωταθλητής Formula 1 το 1996, αποτελώντας το πρώτο δίδυμο πατέρα-γιου πρωταθλητών στην F1."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CF%81%CE%AC%CF%87%CE%B1%CE%BC_%CE%A7%CE%B9%CE%BB",
    "locale": "el-GR",
    "tags": ["graham-hill", "triple-crown", "motorsport"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_049",
    "text": "Ποια αθλήτρια κατέχει το ρεκόρ παραμονής στο Νο. 1 της παγκόσμιας κατάταξης στο γυναικείο τένις (WTA) με 377 εβδομάδες;",
    "answers": ["Σερένα Ουίλιαμς", "Μαρτίνα Ναβρατίλοβα", "Στέφι Γκραφ", "Κρις Έβερτ"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Steffi Graf κυριάρχησε επί σειρά ετών στο παγκόσμιο τένις και διατηρεί το απόλυτο ρεκόρ στην ιστορία του γυναικείου τένις με 377 εβδομάδες στην κορυφή.",
    "funFacts": [
      "Ακολουθεί η Martina Navratilova με 332 εβδομάδες και η Serena Williams με 319 εβδομάδες.",
      "Είναι η μοναδική τενίστρια που έχει κερδίσει καθένα από τα τέσσερα τουρνουά Grand Slam τουλάχιστον 4 φορές."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AD%CF%86%CE%B9_%CE%93%CE%BA%CF%81%CE%B1%CF%86",
    "locale": "el-GR",
    "tags": ["steffi-graf", "wta-rankings", "tennis-records"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_050",
    "text": "Σε ποιους Ολυμπιακούς Αγώνες κατέκτησε η Εθνική Ελλάδας ανδρών στην υδατοσφαίριση το πρώτο της ιστορικό ασημένιο ολυμπιακό μετάλλιο;",
    "answers": ["Στην Αθήνα το 2004", "Στο Ρίο το 2016", "Στο Πεκίνο το 2008", "Στο Τόκιο το 2021"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στους Ολυμπιακούς Αγώνες του Τόκιο το 2021, η ελληνική ομάδα πόλο υπό τον Θοδωρή Βλάχο έφτασε στον τελικό κερδίζοντας το ασημένιο μετάλλιο απέναντι στη Σερβία.",
    "funFacts": [
      "Στον ημιτελικό συνέτριψε την Ουγγαρία με 9-6 εξασφαλίζοντας το πρώτο ολυμπιακό μετάλλιο στην ιστορία της ανδρικής υδατοσφαίρισης.",
      "Ο αρχηγός Γιάννης Φουντούλης και ο τερματοφύλακας Μάνος Ζερδεβάς συμπεριλήφθηκαν στην κορυφαία επτάδα του ολυμπιακού τουρνουά."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B8%CE%BD%CE%B9%CE%BA%CE%AE_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1%CF%82_(%CF%85%CE%B4%CE%B1%CF%84%CE%BF%CF%83%CF%86%CE%B1%CE%AF%CF%81%CE%B9%CF%83%CE%B7_%CE%B1%CE%BD%CE%B4%CF%81%CF%8E%CE%BD)",
    "locale": "el-GR",
    "tags": ["greek-waterpolo", "tokyo-2020", "olympic-silver"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_051",
    "text": "Ποιος Αμερικανός άλτης κατέχει το παγκόσμιο ρεκόρ στο άλμα εις μήκος ανδρών με 8,95 μέτρα από το αξέχαστο Παγκόσμιο Πρωτάθλημα του Τόκιο το 1991;",
    "answers": ["Μάικ Πάουελ", "Καρλ Λιούις", "Ιβάν Πεντρόσο", "Ντουάιτ Φίλιπς"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 30 Αυγούστου 1991, ο Mike Powell κατέρριψε το ρεκόρ του Bob Beamon από το 1968 σε μια ιστορική μονομαχία με τον Carl Lewis.",
    "funFacts": [
      "Ο Carl Lewis είχε επίσης άλμα στα 8,91μ στον ίδιο αγώνα, αλλά με ευνοϊκό άνεμο άνω του επιτρεπτού ορίου (+2,9 m/s).",
      "Το ρεκόρ του Powell (8,95 μέτρα) διατηρείται για περισσότερα από 35 χρόνια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%B9%CE%BA_%CE%A0%CE%AC%CE%BF%CF%85%CE%B5%CE%BB",
    "locale": "el-GR",
    "tags": ["mike-powell", "long-jump", "world-records", "tokyo-1991"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_052",
    "text": "Ποια αγγλική ομάδα ολοκλήρωσε ολόκληρη τη σεζόν της Premier League αήττητη (26 νίκες, 12 ισοπαλίες) το 2003-04 κερδίζοντας το προσωνύμιο 'The Invincibles';",
    "answers": ["Μάντσεστερ Γιουνάιτεντ", "Άρσεναλ", "Τσέλσι", "Λίβερπουλ"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η Arsenal του Arsène Wenger με πρωταγωνιστές τους Thierry Henry, Patrick Vieira και Dennis Bergkamp κατέκτησε τον τίτλο χωρίς ούτε μία ήττα.",
    "funFacts": [
      "Η Premier League απένειμε στην Άρσεναλ ένα μοναδικό ολόχρυσο αντίγραφο του τροπαίου του πρωταθλήματος για αυτό το κατόρθωμα.",
      "Το αήττητο σερί της ομάδας διήρκεσε συνολικά 49 αγώνες πρωταθλήματος (Μάιος 2003 – Οκτώβριος 2004)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%86%CF%81%CF%83%CE%B5%CE%BD%CE%B1%CE%BB_%CE%A6%CE%9A",
    "locale": "el-GR",
    "tags": ["arsenal", "invincibles", "premier-league-2004"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_053",
    "text": "Ποιος Σέρβος προπονητής είναι ο πολυνίκης στην ιστορία της EuroLeague με 9 κατακτήσεις τροπαίων με 5 διαφορετικές ομάδες;",
    "answers": ["Ντούσαν Ίβκοβιτς", "Έτορε Μεσίνα", "Ζέλικο Ομπράντοβιτς", "Σβέτισλαβ Πέσιτς"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Željko Obradović κατέκτησε την EuroLeague με την Παρτιζάν (1992), τη Ζουβεντούτ Μπανταλόνα (1994), τη Ρεάλ Μαδρίτης (1995), τον Παναθηναϊκό (2000, 2002, 2007, 2009, 2011) και τη Φενέρμπαχτσε (2017).",
    "funFacts": [
      "Πέρασε 13 ένδοξα χρόνια στον πάγκο του Παναθηναϊκού (1999–2012) κερδίζοντας επίσης 11 Πρωταθλήματα και 7 Κύπελλα Ελλάδας.",
      "Είναι γνωστός στον μπασκετικό κόσμο με το προσωνύμιο 'Ζοτς' (Zoc)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%96%CE%AD%CE%BB%CE%B9%CE%BA%CE%BF_%CE%9F%CE%BC%CF%80%CF%81%CE%AC%CE%BD%CF%84%CE%BF%CE%B2%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["obradovic", "euroleague", "panathinaikos", "coaches"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_054",
    "text": "Σε ποια γερμανική πόλη διεξήχθησαν οι Ολυμπιακοί Αγώνες του 1972 που σημαδεύτηκαν από την τρομοκρατική επίθεση εναντίον της ισραηλινής αποστολής;",
    "answers": ["Στο Βερολίνο", "Στη Φρανκφούρτη", "Στο Αμβούργο", "Στο Μόναχο"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Η τρομοκρατική οργάνωση 'Μαύρος Σεπτέμβρης' εισέβαλε στο Ολυμπιακό Χωριό του Μονάχου στις 5 Σεπτεμβρίου 1972, οδηγώντας στον τραγικό θάνατο 11 Ισραηλινών αθλητών και προπονητών.",
    "funFacts": [
      "Παρά την τραγωδία, ο πρόεδρος της ΔΟΕ Έιβερι Μπράντεϊτζ ανακοίνωσε ότι 'Οι Αγώνες πρέπει να συνεχιστούν' μετά από 34ωρη διακοπή.",
      "Το Ολυμπιακό Στάδιο του Μονάχου ξεχώρισε αρχιτεκτονικά για την πρωτοποριακή ημιδιαφανή οροφή του σε σχήμα τέντας."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1972",
    "locale": "el-GR",
    "tags": ["munich-1972", "olympics-history", "munich-massacre"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_055",
    "text": "Ποιος Φιλιππινέζος πυγμάχος είναι ο μοναδικός στην ιστορία που κατέκτησε παγκόσμιους τίτλους σε 8 διαφορετικές κατηγορίες βάρους;",
    "answers": ["Μάνι Πακιάο (Manny Pacquiao)", "Φλόιντ Μεϊγουέδερ", "Χουάν Μανουέλ Μάρκες", "Όσκαρ Ντε Λα Χόγια"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Manny Pacquiao ('Pac-Man') κέρδισε παγκόσμιους τίτλους από τα 50 κιλά (μύγας) μέχρι τα 69 κιλά (ημιμεσαίων βαρών), ένα αδιανόητο επίτευγμα στην πυγμαχία.",
    "funFacts": [
      "Είναι ο μόνος πυγμάχος που κέρδισε παγκόσμιους τίτλους σε τέσσερις διαφορετικές δεκαετίες (1990s, 2000s, 2010s, 2020s).",
      "Εκλέχθηκε γερουσιαστής στις Φιλιππίνες το 2016 και διεκδίκησε την προεδρία της χώρας το 2022."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%AC%CE%BD%CE%B9_%CE%A0%CE%B1%CE%BA%CE%B9%CE%AC%CE%BF",
    "locale": "el-GR",
    "tags": ["pacquiao", "boxing", "eight-division"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_056",
    "text": "Ποιος Ισπανός μέσος πέτυχε το νικητήριο γκολ στο 116ο λεπτό της παράτασης στον τελικό του Μουντιάλ 2010 εναντίον της Ολλανδίας;",
    "answers": ["Τσάβι Ερνάντεθ", "Αντρές Ινιέστα", "Τσάμπι Αλόνσο", "Νταβίντ Βίγια"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Andrés Iniesta χάρισε στην Ισπανία το πρώτο Παγκόσμιο Κύπελλο της ιστορίας της στο Γιοχάνεσμπουργκ της Νότιας Αφρικής.",
    "funFacts": [
      "Στον πανηγυρισμό του έβγαλε τη φανέλα του αποκαλύπτοντας το μήνυμα 'Dani Jarque siempre con nosotros' προς τιμήν του αδικοχαμένου αρχηγού της Εσπανιόλ.",
      "Η Ισπανία έγινε η πρώτη ευρωπαϊκή ομάδα που κέρδισε Παγκόσμιο Κύπελλο εκτός ευρωπαϊκού εδάφους."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CF%81%CE%AD%CF%82_%CE%99%CE%BD%CE%B9%CE%AD%CF%83%CF%84%CE%B1",
    "locale": "el-GR",
    "tags": ["iniesta", "world-cup-2010", "spain-football"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_057",
    "text": "Ποια μυθική βουνοκορφή των Γαλλικών Άλπεων είναι παγκοσμίως διάσημη για τις 21 χαρακτηριστικές απότομες στροφές της (φουρκέτες) στον Γύρο της Γαλλίας;",
    "answers": ["Μον Βεντού (Mont Ventoux)", "Κολ ντου Τουρμαλέ (Col du Tourmalet)", "Αλπ ντ' Ουέζ (Alpe d'Huez)", "Κολ ντε Γκαλιμπιέ (Col du Galibier)"],
    "correctAnswerIndex": 2,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Το Alpe d'Huez αποτελεί μια από τις πιο θρυλικές αναβάσεις στο Tour de France, με μήκος 13,8 χλμ. και μέση κλίση 8,1%.",
    "funFacts": [
      "Κάθε μία από τις 21 αριθμημένες στροφές φέρει τιμητική πλακέτα με τα ονόματα των νικητών του ετάπ σε αυτή την κορυφή.",
      "Η στροφή 7 είναι γνωστή ως 'Dutch Corner' επειδή χιλιάδες Ολλανδοί φίλαθλοι κατασκηνώνουν εκεί ντυμένοι στα πορτοκαλί."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CF%80_%CE%BD%CF%84%27_%CE%9F%CF%85%CE%AD%CE%B6",
    "locale": "el-GR",
    "tags": ["alpe-d-huez", "tour-de-france", "cycling"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_058",
    "text": "Σε ποια χρονιά και σε ποια ισπανική πόλη πανηγύρισε η Ελλάδα δύο ιστορικά χρυσά ολυμπιακά μετάλλια με την Πατουλίδου και τον Δήμα;",
    "answers": ["Το 1988 στη Μαδρίτη", "Το 1996 στη Σεβίλλη", "Το 2000 στη Βαλένθια", "Το 1992 στη Βαρκελώνη"],
    "correctAnswerIndex": 3,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Οι Ολυμπιακοί Αγώνες της Βαρκελώνης το 1992 σηματοδότησαν την αναγέννηση του ελληνικού ολυμπιακού αθλητισμού με δύο αξέχαστα χρυσά μετάλλια.",
    "funFacts": [
      "Η Βούλα Πατουλίδου κέρδισε τα 100μ με εμπόδια στις 6 Αυγούστου 1992, λίγες ημέρες μετά το χρυσό του Πύρρου Δήμα στην άρση βαρών (82,5 κιλά).",
      "Στην ίδια διοργάνωση αγωνίστηκε για πρώτη φορά και η περίφημη αυθεντική 'Dream Team' του αμερικανικού μπάσκετ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CE%AF_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CE%AF_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1992",
    "locale": "el-GR",
    "tags": ["barcelona-1992", "patoulidou", "pyrros-dimas", "olympics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_059",
    "text": "Ποιος Αμερικανός κολυμβητής έγινε στους Ολυμπιακούς του Μόντρεαλ το 1976 ο πρώτος άνθρωπος στην ιστορία που 'έσπασε' το φράγμα των 50 δευτερολέπτων στα 100μ ελεύθερο;",
    "answers": ["Τζιμ Μοντγκόμερι", "Μαρκ Σπιτς", "Ρόουντι Γκέινς", "Ματ Μπιόντι"],
    "correctAnswerIndex": 0,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Στις 25 Ιουλίου 1976, ο Jim Montgomery κέρδισε το χρυσό μετάλλιο στα 100μ ελεύθερο με χρόνο 49,99 δευτερόλεπτα.",
    "funFacts": [
      "Το ιστορικό αυτό όριο συγκρινόταν στην εποχή του με το σπάσιμο του μιλίου κάτω από 4 λεπτά στον στίβο.",
      "Στο Μόντρεαλ κέρδισε συνολικά 3 χρυσά μετάλλια και ένα χάλκινο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BF%CE%BB%CF%8D%CE%BC%CE%B2%CE%B7%CF%83%CE%B7_%CF%83%CF%84%CE%BF%CF%85%CF%82_%CE%98%CE%B5%CF%81%CE%B9%CE%BD%CE%BF%CF%8D%CF%82_%CE%9F%CE%BB%CF%85%CE%BC%CF%80%CE%B9%CE%B1%CE%BA%CE%BF%CF%8D%CF%82_%CE%91%CE%B3%CF%8E%CE%BD%CE%B5%CF%82_1976",
    "locale": "el-GR",
    "tags": ["montgomery", "swimming-history", "100m-freestyle"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "sports_med_060",
    "text": "Ποιος θρυλικός Κροάτης γκαρντ αποκλήθηκε 'Ο Μότσαρτ του Μπάσκετ' και έχασε τραγικά τη ζωή του σε τροχαίο δυστύχημα στη Γερμανία το 1993;",
    "answers": ["Τόνι Κούκοτς", "Ντράζεν Πέτροβιτς", "Ντίνο Ράτζα", "Στόγιαν Βράνκοβιτς"],
    "correctAnswerIndex": 1,
    "categoryId": "sports",
    "difficulty": 3,
    "explanation": "Ο Dražen Petrović θεωρείται ένας από τους πιο χαρισματικούς σκόρερ στην ιστορία του παγκόσμιου μπάσκετ, διαπρέποντας στην Τσιμπόνα, τη Ρεάλ Μαδρίτης και τους New Jersey Nets.",
    "funFacts": [
      "Σε έναν αγώνα του γιουγκοσλαβικού πρωταθλήματος το 1985 με την Τσιμπόνα εναντίον της Ολίμπια Λιουμπλιάνα σημείωσε 112 πόντους.",
      "Εισήχθη μετά θάνατον στο Naismith Memorial Basketball Hall of Fame το 2002."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%84%CF%81%CE%AC%CE%B6%CE%B5%CE%BD_%CE%A0%CE%AD%CF%84%CF%81%CE%BF%CE%B2%CE%B9%CF%84%CF%82",
    "locale": "el-GR",
    "tags": ["petrovic", "basketball-legends", "croatia"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == '__main__':
    validate_and_append('sports', 'medium', 3, questions)

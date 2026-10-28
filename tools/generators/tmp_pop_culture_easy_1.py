# -*- coding: utf-8 -*-
from tools.generators.base_generator import validate_and_append

questions = [
  {
    "id": "pop_culture_easy_011",
    "text": "Ποιο μαγικό αντικείμενο πρέπει να καταστρέψει ο Φρόντο Μπάγκινς στο 'Ο Άρχοντας των Δαχτυλιδιών';",
    "answers": [
      "Το Ένα Δαχτυλίδι",
      "Το Πετράδι του Αρκενστόουν",
      "Το Σπαθί του Άντουριλ",
      "Τη Σφαίρα του Παλαντίρ"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Φρόντο αναλαμβάνει να μεταφέρει και να καταστρέψει το Ένα Δαχτυλίδι (The One Ring) στη λάβα του Βουνού του Χαμού (Mount Doom).",
    "funFacts": [
      "Η επιγραφή στο Ένα Δαχτυλίδι είναι γραμμένη στη Μαύρη Γλώσσα της Μόρντορ με χαρακτήρες του Τένγκβαρ.",
      "Η κινηματογραφική τριλογία του Πίτερ Τζάκσον κέρδισε συνολικά 17 βραβεία Όσκαρ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%88%CE%BD%CE%B1_%CE%94%CE%B1%CF%87%CF%84%CF%85%CE%BB%CE%AF%CE%B4%CE%B9",
    "locale": "el-GR",
    "tags": ["lord_of_the_rings", "cinema", "fantasy", "books"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_012",
    "text": "Ποιος σκηνοθέτησε την εισπρακτική επιτυχία του 1997 'Τιτανικός' (Titanic);",
    "answers": [
      "Στίβεν Σπίλμπεργκ",
      "Τζέιμς Κάμερον",
      "Μάρτιν Σκορσέζε",
      "Ρίντλεϊ Σκοτ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Τζέιμς Κάμερον έγραψε και σκηνοθέτησε τον 'Τιτανικό', που έγινε η πρώτη ταινία στην ιστορία με εισπράξεις άνω του 1 δισεκατομμυρίου δολαρίων.",
    "funFacts": [
      "Ο Τζέιμς Κάμερον έκανε δεκάδες καταδύσεις στο πραγματικό ναυάγιο του Τιτανικού για να κινηματογραφήσει αυθεντικά πλάνα.",
      "Η ταινία ισοφάρισε το ρεκόρ των περισσότερων βραβείων Όσκαρ στην ιστορία, κερδίζοντας συνολικά 11 αγαλματίδια."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9%CF%84%CE%B1%CE%BD%CE%B9%CE%BA%CF%8C%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1,_1997)",
    "locale": "el-GR",
    "tags": ["titanic", "cinema", "james_cameron", "hollywood"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_013",
    "text": "Στην ταινία 'The Matrix' (1999), τι χρώμα έχει το χάπι που επιλέγει ο Neo για να μάθει την αλήθεια για τον κόσμο;",
    "answers": [
      "Μπλε",
      "Πράσινο",
      "Κόκκινο",
      "Κίτρινο"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μορφέας προσφέρει στον Neo την επιλογή ανάμεσα στο μπλε χάπι (επιστροφή στην ψευδαίσθηση) και το κόκκινο χάπι (αφύπνιση στην αλήθεια).",
    "funFacts": [
      "Η έννοια του 'red pill' εισήλθε στη σύγχρονη ποπ κουλτούρα ως μεταφορά για τη συνειδητοποίηση μιας κρυφής πραγματικότητας.",
      "Ο Keanu Reeves έκανε εντατική εκπαίδευση πολεμικών τεχνών για μήνες πριν ξεκινήσουν τα γυρίσματα της ταινίας."
    ],
    "source": "https://en.wikipedia.org/wiki/Red_pill_and_blue_pill",
    "locale": "el-GR",
    "tags": ["the_matrix", "cinema", "sci_fi", "keanu_reeves"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_014",
    "text": "Ποιο είναι το όνομα του διάσημου διαστημόπλοιου του Han Solo στον 'Πόλεμο των Άστρων' (Star Wars);",
    "answers": [
      "USS Enterprise",
      "Serenity",
      "Nostromo",
      "Millennium Falcon"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Millennium Falcon (Γεράκι της Χιλιετίας) είναι το θρυλικό διαστημόπλοιο που κυβερνούν ο Han Solo και ο συγκυβερνήτης του Chewbacca.",
    "funFacts": [
      "Ο Han Solo περηφανευόταν ότι το Millennium Falcon ολοκλήρωσε το Kessel Run σε λιγότερο από 12 parsec.",
      "Ο σχεδιασμός του σκάφους εμπνεύστηκε από ένα μισοφαγωμένο χάμπουργκερ με μια ελιά καρφωμένη στο πλάι."
    ],
    "source": "https://en.wikipedia.org/wiki/Millennium_Falcon",
    "locale": "el-GR",
    "tags": ["star_wars", "cinema", "sci_fi", "han_solo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_015",
    "text": "Από ποιο απολιθωμένο έντομο αντλήθηκε το DNA δεινοσαύρων στην ταινία 'Jurassic Park' (1993);",
    "answers": [
      "Κουνούπι παγιδευμένο σε κεχριμπάρι",
      "Μέλισσα παγιδευμένη σε πάγο",
      "Λιβελούλα παγιδευμένη σε ρητίνη",
      "Μυρμήγκι παγιδευμένο σε ηφαιστειακή στάχτη"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στο Jurassic Park, οι επιστήμονες ανακτούν αίμα δεινοσαύρων από προϊστορικά κουνούπια που είχαν απολιθωθεί μέσα σε κεχριμπάρι.",
    "funFacts": [
      "Τα κενά στο αρχαίο DNA των δεινοσαύρων συμπληρώθηκαν στην ταινία με DNA από βατράχους.",
      "Ο σκηνοθέτης Στίβεν Σπίλμπεργκ χρησιμοποίησε συνδυασμό ψηφιακών εφέ CGI και γιγάντιων animatronics για τα γυρίσματα."
    ],
    "source": "https://en.wikipedia.org/wiki/Jurassic_Park_(film)",
    "locale": "el-GR",
    "tags": ["jurassic_park", "cinema", "spielberg", "dinosaurs"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_016",
    "text": "Από ποια αποβάθρα του σταθμού King's Cross αναχωρεί το τρένο Hogwarts Express για τη σχολή μαγείας;",
    "answers": [
      "Πλατφόρμα 7 1/2",
      "Πλατφόρμα 9 3/4",
      "Πλατφόρμα 10 1/4",
      "Πλατφόρμα 8 2/3"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι μαθητές του Χόγκουαρτς περνούν μέσα από τον τοίχο ανάμεσα στις πλατφόρμες 9 και 10 για να φτάσουν στην πλατφόρμα 9 3/4.",
    "funFacts": [
      "Στον πραγματικό σταθμό King's Cross του Λονδίνου υπάρχει ειδική πινακίδα και μισό καρότσι αποσκευών στον τοίχο για αναμνηστικές φωτογραφίες.",
      "Η συγγραφέας Τζ. Κ. Ρόουλινγκ έχει παραδεχτεί πως κατά τη συγγραφή μπέρδεψε τη διάταξη των αποβαθρών του King's Cross με τον σταθμό Euston."
    ],
    "source": "https://en.wikipedia.org/wiki/Hogwarts_Express",
    "locale": "el-GR",
    "tags": ["harry_potter", "books", "cinema", "london"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_017",
    "text": "Πώς προτιμά να πίνει το βότκα μαρτίνι του ο μυστικός πράκτορας James Bond;",
    "answers": [
      "Ανακατεμένο στο κουτάλι",
      "Με πάγο και σόδα",
      "Χτυπημένο, όχι ανακατεμένο (Shaken, not stirred)",
      "Ζεστό χωρίς λεμόνι"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η κλασική φράση του James Bond για την παραγγελία του μαρτίνι είναι 'shaken, not stirred'.",
    "funFacts": [
      "Η πρώτη φορά που ακούστηκε η ατάκα σε ταινία ήταν στο 'Dr. No' (1962), αλλά ειπώθηκε αρχικά από τον κακό της ταινίας.",
      "Στο βιβλίο 'Casino Royale' (1953), ο Ίαν Φλέμινγκ περιγράφει το κοκτέιλ 'Vesper', το οποίο περιέχει τζιν, βότκα και Kina Lillet."
    ],
    "source": "https://en.wikipedia.org/wiki/Shaken,_not_stirred",
    "locale": "el-GR",
    "tags": ["james_bond", "cinema", "quotes", "cocktails"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_018",
    "text": "Ποιος ηθοποιός ενσάρκωσε τον εμβληματικό πειρατή Τζακ Σπάροου στις ταινίες 'Οι Πειρατές της Καραϊβικής';",
    "answers": [
      "Ορλάντο Μπλουμ",
      "Τζέφρι Ρας",
      "Κόλιν Φάρελ",
      "Τζόνι Ντεπ"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Τζόνι Ντεπ υποδύθηκε τον κάπτεν Τζακ Σπάροου, ρόλος που του χάρισε υποψηφιότητα για Όσκαρ Α' Ανδρικού Ρόλου.",
    "funFacts": [
      "Ο Ντεπ βάσισε τον εκκεντρικό χαρακτήρα και την κίνηση του Jack Sparrow στον κιθαρίστα των Rolling Stones, Keith Richards.",
      "Οι υπεύθυνοι της Disney αρχικά φοβήθηκαν ότι η ερμηνεία του Ντεπ θα κατέστρεφε την ταινία, πριν γίνει τεράστια επιτυχία."
    ],
    "source": "https://en.wikipedia.org/wiki/Jack_Sparrow",
    "locale": "el-GR",
    "tags": ["pirates_of_the_caribbean", "cinema", "johnny_depp", "disney"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_019",
    "text": "Ποιο είναι το χαρακτηριστικό όπλο και εξάρτημα του αρχαιολόγου Ιντιάνα Τζόουνς μαζί με το καπέλο φεντόρα;",
    "answers": [
      "Μαστίγιο",
      "Τόξο και βέλη",
      "Μπούμερανγκ",
      "Ξίφος σαμουράι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Ιντιάνα Τζόουνς (Χάρισον Φορντ) είναι παγκοσμίως αναγνωρίσιμος από το δερμάτινο μαστίγιο (bullwhip) και το καπέλο φεντόρα του.",
    "funFacts": [
      "Ο διάσημος ήχος του μαστιγίου δημιουργείται όταν η άκρη του σπάει το φράγμα του ήχου, φτάνοντας ταχύτητα άνω των 1.200 χλμ/ώρα.",
      "Το όνομα Indiana προήλθε από τον σκύλο ράτσας Alaskan Malamute που είχε τότε ο παραγωγός Τζορτζ Λούκας."
    ],
    "source": "https://en.wikipedia.org/wiki/Indiana_Jones",
    "locale": "el-GR",
    "tags": ["indiana_jones", "cinema", "harrison_ford", "adventure"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_020",
    "text": "Ποιος θρυλικός ηθοποιός ενσάρκωσε τον Don Vito Corleone στην κλασική ταινία 'Ο Νονός' (The Godfather, 1972);",
    "answers": [
      "Αλ Πατσίνο",
      "Μάρλον Μπράντο",
      "Ρόμπερτ Ντε Νίρο",
      "Τζο Πέσι"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Μάρλον Μπράντο κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου για την ανεπανάληπτη ερμηνεία του ως Βίτο Κορλεόνε.",
    "funFacts": [
      "Ο Μπράντο αρνήθηκε να παραλάβει το Όσκαρ του, στέλνοντας την ακτιβίστρια Sacheen Littlefeather ως διαμαρτυρία για την απεικόνιση των ιθαγενών Αμερικανών.",
      "Για την οντισιόν του, ο Μπράντο έβαλε βαμβάκι στα μάγουλά του για να δώσει στον Νονό τη χαρακτηριστική όψη μπουλντόγκ."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%9F_%CE%9D%CE%BF%CE%BD%CF%8C%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
    "locale": "el-GR",
    "tags": ["the_godfather", "cinema", "marlon_brando", "classics"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_021",
    "text": "Ποιο αυτοκίνητο μετατράπηκε σε χρονομηχανή από τον Dr. Emmett Brown στην ταινία 'Επιστροφή στο Μέλλον' (Back to the Future);",
    "answers": [
      "Ford Mustang",
      "Chevrolet Corvette",
      "DeLorean DMC-12",
      "Pontiac Firebird"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Doc Brown επέλεξε το DeLorean DMC-12 με τις πόρτες 'gull-wing' από ανοξείδωτο ατσάλι επειδή ήθελε η χρονομηχανή να έχει στυλ.",
    "funFacts": [
      "Για να ενεργοποιηθεί το ταξίδι στον χρόνο, το DeLorean έπρεπε να πιάσει ταχύτητα 88 μιλίων την ώρα (περίπου 142 χλμ/ώρα).",
      "Στα πρώτα προσχέδια του σεναρίου, η χρονομηχανή δεν ήταν αυτοκίνητο, αλλά ένα παλιό ψυγείο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%83%CF%84%CF%81%CE%BF%CF%86%CE%AE_%CF%83%CF%84%CE%BF_%CE%9C%CE%AD%CE%BB%CE%BB%CE%BF%CE%BD",
    "locale": "el-GR",
    "tags": ["back_to_the_future", "cinema", "delorean", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_022",
    "text": "Ποιος υπερήρωας έχει την πραγματική μυστική ταυτότητα του εκκεντρικού δισεκατομμυριούχου Tony Stark;",
    "answers": [
      "Captain America",
      "Batman",
      "Spider-Man",
      "Iron Man"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Tony Stark είναι ο ιδιοφυής εφευρέτης και βιομήχανος που κατασκεύασε την πανοπλία του Iron Man.",
    "funFacts": [
      "Η φράση 'I am Iron Man' στο φινάλε της πρώτης ταινίας (2008) ήταν αυτοσχεδιασμός του Ρόμπερτ Ντάουνι Τζούνιορ που ενθουσίασε τον σκηνοθέτη.",
      "Η τεράστια επιτυχία του Iron Man το 2008 έθεσε τα θεμέλια για ολόκληρο το Κινηματογραφικό Σύμπαν της Marvel (MCU)."
    ],
    "source": "https://en.wikipedia.org/wiki/Tony_Stark_(Marvel_Cinematic_Universe)",
    "locale": "el-GR",
    "tags": ["marvel", "iron_man", "superheroes", "mcu"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_023",
    "text": "Ποια διάσημη συμβουλή έδωσε ο θείος Μπεν στον Πίτερ Πάρκερ στα κόμικς και τις ταινίες του Spider-Man;",
    "answers": [
      "Με μεγάλη δύναμη έρχεται μεγάλη ευθύνη",
      "Η γνώση είναι η απόλυτη δύναμη",
      "Ποτέ μην εγκαταλείπεις τους φίλους σου",
      "Ο σκοπός αγιάζει τα μέσα"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η φράση 'With great power comes great responsibility' αποτελεί τον πυρήνα της ηθικής στάσης του Spider-Man.",
    "funFacts": [
      "Στο αρχικό κόμικ Amazing Fantasy #15 (1962), η φράση εμφανίστηκε ως κείμενο του αφηγητή και όχι στα λόγια του θείου Μπεν.",
      "Ο Σπάιντερμαν δημιουργήθηκε από τον Σταν Λι και τον καλλιτέχνη Στιβ Ντίτκο."
    ],
    "source": "https://en.wikipedia.org/wiki/With_great_power_comes_great_responsibility",
    "locale": "el-GR",
    "tags": ["spider_man", "marvel", "comics", "quotes"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_024",
    "text": "Σε ποια φανταστική πόλη δραστηριοποιείται ο Batman προστατεύοντας τους κατοίκους από το έγκλημα;",
    "answers": [
      "Metropolis",
      "Gotham City",
      "Central City",
      "Star City"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Gotham City είναι η σκοτεινή μητρόπολη που προστατεύει ο Batman (Bruce Wayne) από εγκληματίες όπως ο Joker.",
    "funFacts": [
      "Το όνομα 'Gotham' προήλθε από έναν τηλεφωνικό κατάλογο της Νέας Υόρκης, όπου ο συγγραφέας Bill Finger είδε την επωνυμία 'Gotham Jewelers'.",
      "Η αντίπαλη διάσημη πόλη Metropolis στα κόμικς της DC αποτελεί την έδρα του Superman."
    ],
    "source": "https://en.wikipedia.org/wiki/Gotham_City",
    "locale": "el-GR",
    "tags": ["batman", "dc_comics", "superheroes", "gotham"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_025",
    "text": "Ποιο παρατσούκλι δόθηκε στο μαζικό κινηματογραφικό φαινόμενο της ταυτόχρονης πρεμιέρας των ταινιών 'Barbie' και 'Oppenheimer' το 2023;",
    "answers": [
      "Bartopper",
      "Nolangerwig",
      "Barbenheimer",
      "PinkBomb"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Barbenheimer' ένωσε τους τίτλους των δύο εντελώς αντίθετων σε ύφος ταινιών που έκαναν πρεμιέρα την ίδια ημέρα (21 Ιουλίου 2023).",
    "funFacts": [
      "Εκατομμύρια θεατές παγκοσμίως αγόρασαν εισιτήρια για να δουν και τις δύο ταινίες back-to-back την ίδια μέρα.",
      "Και οι δύο ταινίες σημείωσαν τεράστια εισπρακτική επιτυχία και απέσπασαν πλήθος βραβείων Όσκαρ."
    ],
    "source": "https://en.wikipedia.org/wiki/Barbenheimer",
    "locale": "el-GR",
    "tags": ["barbenheimer", "cinema", "barbie", "oppenheimer"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_026",
    "text": "Ποια σουαχίλι φράση διδάσκουν ο Τιμόν και ο Πούμπα στον Σίμπα στην ταινία 'Ο Βασιλιάς των Λιονταριών' (The Lion King);",
    "answers": [
      "Asante Sana",
      "Jambo Bwana",
      "Kuna Matata",
      "Hakuna Matata"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η φράση 'Hakuna Matata' στα σουαχίλι σημαίνει 'κανένα πρόβλημα' ή 'μη σε νοιάζει'.",
    "funFacts": [
      "Το ομώνυμο τραγούδι γράφτηκε από τον Έλτον Τζον και τον Τιμ Ράις και προτάθηκε για Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού.",
      "Η ταινία The Lion King (1994) παραμένει η πιο επιτυχημένη παραδοσιακά σχεδιασμένη ταινία κινουμένων σχεδίων όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/Hakuna_Matata",
    "locale": "el-GR",
    "tags": ["the_lion_king", "disney", "animation", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_027",
    "text": "Ποιο διάσημο τραγούδι ερμηνεύει η βασίλισσα Έλσα στην ταινία κινουμένων σχεδίων 'Frozen' (2013) χτίζοντας το παγωμένο της κάστρο;",
    "answers": [
      "Let It Go",
      "Into the Unknown",
      "A Whole New World",
      "Part of Your World"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το τραγούδι 'Let It Go' ερμηνεύτηκε από την Idina Menzel και έγινε παγκόσμιο μουσικό φαινόμενο, κερδίζοντας Όσκαρ.",
    "funFacts": [
      "Στην ελληνική μεταγλώττιση της ταινίας, το τραγούδι απέκτησε τον τίτλο 'Και ξεχνώ' με ερμηνεύτρια τη Σία Κοσκινά.",
      "Αρχικά η Έλσα προοριζόταν να είναι η κακιά της ταινίας, αλλά οι δημιουργοί άλλαξαν την ιστορία μόλις άκουσαν το 'Let It Go'."
    ],
    "source": "https://en.wikipedia.org/wiki/Let_It_Go",
    "locale": "el-GR",
    "tags": ["frozen", "disney", "animation", "music"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_028",
    "text": "Ποιο είδος παιχνιδιού είναι ο Γούντι (Woody) στην πρωτοποριακή ταινία κινουμένων σχεδίων 'Toy Story' (1995);",
    "answers": [
      "Αστροναύτης",
      "Κάουμποϊ κούκλα με κορδόνι",
      "Πλαστικός δεινόσαυρος",
      "Στρατιωτάκι"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Γούντι είναι μια κλασική πάνινη κούκλα κάουμποϊ με κορδόνι στην πλάτη που αναπαράγει φωνητικές ατάκες.",
    "funFacts": [
      "Το Toy Story ήταν η πρώτη ταινία μεγάλου μήκους στην ιστορία του κινηματογράφου κατασκευασμένη εξ ολοκλήρου σε υπολογιστή (CGI).",
      "Τη φωνή του Γούντι στην αγγλική έκδοση δανείζει ο βραβευμένος με Όσκαρ ηθοποιός Τομ Χανκς."
    ],
    "source": "https://en.wikipedia.org/wiki/Toy_Story",
    "locale": "el-GR",
    "tags": ["toy_story", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_029",
    "text": "Τι είδος ψαριού είναι ο Νέμο και ο πατέρας του Μάρλιν στην ταινία της Pixar 'Ψάχνοντας τον Νέμο' (Finding Nemo);",
    "answers": [
      "Χρυσόψαρο",
      "Μπλε τανγκ",
      "Ψάρι κλόουν (αμφιπρίονας)",
      "Ξιφίας"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Νέμο και ο πατέρας του Μάρλιν είναι ψάρια κλόουν (Amphiprion ocellaris) που ζουν προστατευμένα μέσα σε θαλάσσιες ανεμώνες.",
    "funFacts": [
      "Η συμπρωταγωνίστρια Ντόρι, που πάσχει από απώλεια πρόσφατης μνήμης, είναι ψάρι του είδους μπλε τανγκ (Paracanthurus hepatus).",
      "Η ταινία σημείωσε τέτοια επιτυχία που η ζήτηση για ψάρια κλόουν ως κατοικίδια ενυδρείου αυξήθηκε δραματικά παγκοσμίως."
    ],
    "source": "https://en.wikipedia.org/wiki/Finding_Nemo",
    "locale": "el-GR",
    "tags": ["finding_nemo", "pixar", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_030",
    "text": "Ποια είναι η πατρίδα και ο αγαπημένος βιότοπος του πράσινου τέρατος Σρεκ (Shrek);",
    "answers": [
      "Ένα σκοτεινό κάστρο",
      "Μια βαθιά σπηλιά",
      "Ένα μαγεμένο δάσος",
      "Ένας απομονωμένος βάλτος"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Σρεκ ζει απομονωμένος και ευτυχισμένος στον βάλτο του (swamp) μέχρι που εξορίζονται εκεί τα παραμυθένια πλάσματα.",
    "funFacts": [
      "Η ταινία Shrek κέρδισε το πρώτο στην ιστορία Βραβείο Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων το 2002.",
      "Το όνομα Shrek προέρχεται από τη γερμανική και γίντις λέξη 'Schreck' / 'Shrek', που σημαίνει φόβος ή τρόμος."
    ],
    "source": "https://en.wikipedia.org/wiki/Shrek",
    "locale": "el-GR",
    "tags": ["shrek", "dreamworks", "animation", "cinema"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_031",
    "text": "Ποιο είναι το έμβλημα του Οίκου των Σταρκ στη δημοφιλή σειρά φαντασίας 'Game of Thrones';",
    "answers": [
      "Ανταριασμένος λύκος (Direwolf)",
      "Χρυσό λιοντάρι",
      "Τρικέφαλος δράκος",
      "Εστεμμένο ελάφι"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το έμβλημα του Οίκου των Σταρκ του Γουίντερφελ είναι ο γκρίζος ανταριασμένος λύκος (direwolf) και το ρητό τους 'Winter is Coming'.",
    "funFacts": [
      "Ο Σιδερένιος Θρόνος (Iron Throne) στη σειρά υποτίθεται πως σφυρηλατήθηκε από χίλια σπαθιά παραδομένων εχθρών με τη φωτιά του δράκου Balerion.",
      "Η σειρά κέρδισε συνολικά 59 βραβεία Primetime Emmy, σημειώνοντας ρεκόρ για δραματική τηλεοπτική σειρά."
    ],
    "source": "https://en.wikipedia.org/wiki/House_Stark",
    "locale": "el-GR",
    "tags": ["game_of_thrones", "tv", "fantasy", "hbo"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_032",
    "text": "Ποιο ψευδώνυμο χρησιμοποιεί ο καθηγητής χημείας Walter White στον υπόκοσμο στη σειρά 'Breaking Bad';",
    "answers": [
      "Σκάρφεϊς",
      "Χάιζενμπεργκ",
      "Κάιζερ Σόζε",
      "Ελ Τσάπο"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Walter White επέλεξε το ψευδώνυμο Heisenberg προς τιμήν του νομπελίστα φυσικού Werner Heisenberg (αρχή της αβεβαιότητας).",
    "funFacts": [
      "Το διάσημο σήμα κατατεθέν της παραγωγής του Walter White ήταν η κρυσταλλική μεθαμφεταμίνη μπλε χρώματος με καθαρότητα 99,1%.",
      "Στα γυρίσματα, η περιβόητη μπλε μεθαμφεταμίνη ήταν στην πραγματικότητα σπασμένες καραμέλες ζάχαρης με γεύση μαλλί της γριάς."
    ],
    "source": "https://en.wikipedia.org/wiki/Walter_White_(Breaking_Bad)",
    "locale": "el-GR",
    "tags": ["breaking_bad", "tv", "series", "walter_white"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_033",
    "text": "Πώς ονομάζεται η παράλληλη σκοτεινή διάσταση στη σειρά του Netflix 'Stranger Things';",
    "answers": [
      "The Nether",
      "The Shadow Realm",
      "The Upside Down (Πάνω-Κάτω)",
      "The Twilight Zone"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Upside Down' είναι μια σκοτεινή κατοπτρική διάσταση της κωμόπολης του Hawkins γεμάτη τέρατα όπως το Demogorgon.",
    "funFacts": [
      "Η ηθοποιός Millie Bobby Brown ξύρισε εντελώς το κεφάλι της για να ενσαρκώσει τον χαρακτήρα της Eleven στην πρώτη σεζόν.",
      "Η σειρά εκτόξευσε ξανά στην κορυφή των παγκόσμιων charts το τραγούδι 'Running Up That Hill' της Kate Bush σχεδόν 40 χρόνια μετά την κυκλοφορία του."
    ],
    "source": "https://en.wikipedia.org/wiki/Stranger_Things",
    "locale": "el-GR",
    "tags": ["stranger_things", "netflix", "tv", "sci_fi"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_034",
    "text": "Ποια είναι η αγαπημένη λιχουδιά του Homer Simpson στη μακροβιότερη σειρά κινουμένων σχεδίων 'The Simpsons';",
    "answers": [
      "Χάμπουργκερ",
      "Πίτσα πεπερόνι",
      "Χοτ ντογκ",
      "Ντόνατς με ροζ γλάσο"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το ροζ ντόνατ με πολύχρωμη τρούφα (pink frosted donut with sprinkles) είναι το απόλυτο αγαπημένο φαγητό του Homer Simpson.",
    "funFacts": [
      "Η επιφωνηματική κραυγή αγανάκτησης του Homer 'D'oh!' προστέθηκε επισήμως στο Αγγλικό Λεξικό της Οξφόρδης (Oxford English Dictionary) το 2001.",
      "Οι χαρακτήρες της σειράς σχεδιάστηκαν με έντονο κίτρινο δέρμα ώστε να τραβούν αμέσως την προσοχή του τηλεθεατή στο ζάπινγκ."
    ],
    "source": "https://en.wikipedia.org/wiki/Homer_Simpson",
    "locale": "el-GR",
    "tags": ["the_simpsons", "animation", "tv", "comedy"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_035",
    "text": "Ποια μάσκα ιστορικής προσωπικότητας φορούν οι ληστές στην ισπανική σειρά 'La Casa de Papel' (Τέλεια Ληστεία);",
    "answers": [
      "Του Σαλβαδόρ Νταλί",
      "Του Πάμπλο Πικάσο",
      "Του Βίνσεντ βαν Γκογκ",
      "Του Μιχαήλ Αγγέλου"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι πρωταγωνιστές φορούν κόκκινες ολόσωμες φόρμες και μάσκες του σουρεαλιστή ζωγράφου Σαλβαδόρ Νταλί.",
    "funFacts": [
      "Το παλιό ιταλικό αντιφασιστικό τραγούδι 'Bella Ciao' έγινε παγκόσμιος ποπ ύμνος μετά τη χρήση του στη σειρά.",
      "Όλα τα μέλη της συμμορίας χρησιμοποιούσαν ως κωδικά ονόματα ονόματα διάσημων πόλεων (Τόκιο, Βερολίνο, Ναϊρόμπι κ.ά.)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%AD%CE%BB%CE%B5%CE%B9%CE%B1_%CE%9B%CE%B7%CF%83%CF%84%CE%B5%CE%AF%CE%B1",
    "locale": "el-GR",
    "tags": ["la_casa_de_papel", "netflix", "tv", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_036",
    "text": "Σε ποια φανταστική εταιρεία χαρτιού εκτυλίσσονται τα γεγονότα της αμερικανικής κωμικής σειράς 'The Office';",
    "answers": [
      "Initech",
      "Dunder Mifflin",
      "Sterling Cooper",
      "Pied Piper"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η σειρά παρακολουθεί την καθημερινότητα των εργαζομένων στο υποκατάστημα του Scranton της εταιρείας χάρτου Dunder Mifflin.",
    "funFacts": [
      "Το γραφείο του διευθυντή Michael Scott περιλάμβανε μια διάσημη κούπα με τη φράση 'World's Best Boss' την οποία είχε αγοράσει ο ίδιος.",
      "Η σειρά αποτελεί προσαρμογή της ομώνυμης βρετανικής σειράς που δημιούργησαν οι Ricky Gervais και Stephen Merchant."
    ],
    "source": "https://en.wikipedia.org/wiki/The_Office_(American_TV_series)",
    "locale": "el-GR",
    "tags": ["the_office", "tv", "comedy", "sitcom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_037",
    "text": "Πώς ονομάζεται το αυτόνομο ζωντανό χέρι που συνοδεύει τη Wednesday Addams στη σειρά 'Wednesday' του Netflix;",
    "answers": [
      "Palm",
      "Handy",
      "Thing (Πράγμα)",
      "Claw"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Thing' είναι ένα αποκομμένο αλλά πλήρως ζωντανό και εκφραστικό ανθρώπινο χέρι, πιστός σύντροφος της οικογένειας Addams.",
    "funFacts": [
      "Στη σειρά του Netflix, το Thing υποδύθηκε ο επαγγελματίας ταχυδακτυλουργός Victor Dorobantu φορώντας ειδικό μπλε κοστούμι για να αφαιρεθεί ψηφιακά το σώμα του.",
      "Ο διάσημος viral χορός της Jenna Ortega στο τραγούδι 'Goo Goo Muck' χορογραφήθηκε από την ίδια την ηθοποιό."
    ],
    "source": "https://en.wikipedia.org/wiki/Wednesday_(TV_series)",
    "locale": "el-GR",
    "tags": ["wednesday", "netflix", "tv", "addams_family"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_038",
    "text": "Ποιος ήταν ο αριθμός της μοιραίας πτήσης της Oceanic Airlines που συνετρίβη στο μυστηριώδες νησί της σειράς 'Lost';",
    "answers": [
      "Flight 777",
      "Flight 101",
      "Flight 404",
      "Flight 815"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η πτήση Oceanic 815 από το Σίδνεϊ προς το Λος Άντζελες συνετρίβη σε ένα αχαρτογράφητο τροπικό νησί.",
    "funFacts": [
      "Οι μυστηριώδεις αριθμοί της σειράς (4, 8, 15, 16, 23, 42) περιλαμβάνουν τον αριθμό της πτήσης 815 (8 και 15).",
      "Το επεισόδιο πιλότος του Lost ήταν το πιο ακριβό στην ιστορία της τηλεόρασης μέχρι τότε, κοστίζοντας πάνω από 12 εκατομμύρια δολάρια."
    ],
    "source": "https://en.wikipedia.org/wiki/Lost_(2004_TV_series)",
    "locale": "el-GR",
    "tags": ["lost", "tv", "mystery", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_039",
    "text": "Σε ποιο νησάκι της Κρήτης ήταν εγκατεστημένη η αποικία χανσενικών (λεπρών) στην ιστορική σειρά 'Το Νησί' του Mega;",
    "answers": [
      "Στη Σπιναλόγκα",
      "Στη Γαύδο",
      "Στη Χρυσή (Γαϊδουρονήσι)",
      "Στα Κουφονήσια"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "'Το Νησί', βασισμένο στο ομώνυμο μυθιστόρημα της Βικτόρια Χίσλοπ, εξιστορεί τη ζωή των λεπρών στο νησάκι της Σπιναλόγκας.",
    "funFacts": [
      "Η σειρά αποτέλεσε μία από τις ακριβότερες και πιο επιτυχημένες παραγωγές στην ιστορία της ελληνικής τηλεόρασης.",
      "Το μυθιστόρημα της Victoria Hislop έγινε διεθνές best seller και μεταφράστηκε σε περισσότερες από 35 γλώσσες."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%9D%CE%B7%CF%83%CE%AF_(%CF%84%CE%B7%CE%BB%CE%B5%CE%BF%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CF%83%CE%B5%CE%B9%CF%81%CE%AC)",
    "locale": "el-GR",
    "tags": ["to_nisi", "greek_tv", "series", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_040",
    "text": "Ποια εκκεντρική πλούσια κληρονόμο υποδύθηκε η Σμαράγδα Καρύδη στην κλασική κωμική σειρά 'Στο Παρά 5';",
    "answers": [
      "Ζουμπουλία Αμπατζίδου",
      "Ντάλια Χατζηαλεξάνδρου",
      "Αγγέλα Ιωακειμίδου",
      "Αμαλία Αντωνοπούλου"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Σμαράγδα Καρύδη ενσάρκωσε την αφελή δισεκατομμυριούχο Ντάλια Χατζηαλεξάνδρου στο 'Στο Παρά 5' του Γιώργου Καπουτζίδη.",
    "funFacts": [
      "Η σειρά σημείωσε τηλεθέαση ρεκόρ που ξεπέρασε το 60% στο φινάλε της το 2007.",
      "Το πατρικό σπίτι της Ντάλιας στη σειρά υποτίθεται ότι διέθετε δεκάδες δωμάτια, ελικοδρόμιο και ιδιωτικό ζωολογικό κήπο."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%BF_%CE%A0%CE%B1%CF%81%CE%AC_5",
    "locale": "el-GR",
    "tags": ["sto_para_pente", "greek_tv", "comedy", "kapoutzidis"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_041",
    "text": "Ποιο ήταν το όνομα της λαϊκής κοπέλας από τη Μελβούρνη που αντάλλαξε ρόλους με τη Βίκυ στη σειρά 'Είσαι το Ταίρι μου';",
    "answers": [
      "Σούλα",
      "Αννέτα",
      "Στέλλα",
      "Τζένη"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Στέλλα (Βίκυ Σταυροπούλου) συμφώνησε να ανταλλάξει ταυτότητα με τη φίλη της Βίκυ (Κατερίνα Λέχου) στο ταξίδι τους για την Ελλάδα.",
    "funFacts": [
      "Η σειρά εκτόξευσε την αναγνωρισιμότητα των πρωταγωνιστών της και καθιέρωσε τον σεναριογράφο Θοδωρή Πετρόπουλο.",
      "Ο ρόλος του εκκεντρικού Λάζαρου (Άρης Σερβετάλης) με το χαρακτηριστικό μαλλί μοϊκάνα και το ιγκουάνα 'Μήτσο' έγινε σύμβολο της νεανικής κουλτούρας των 00s."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%95%CE%AF%CF%83%CE%B1%CE%B9_%CF%84%CE%BF_%CF%84%CE%AC%CE%B9%CF%81%CE%B9_%CE%BC%CE%BF%CF%85",
    "locale": "el-GR",
    "tags": ["eisai_to_tairi_mou", "greek_tv", "comedy", "series"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_042",
    "text": "Ποιο τηλεοπτικό μαγκαζίνο παρουσίαζε η Μαρίνα Κουντουράτου (Εβελίνα Παπούλια) στη σειρά 'Δύο Ξένοι';",
    "answers": [
      "Πρωινό Καφέ",
      "Καλημέρα Ελλάδα",
      "Όμορφος Κόσμος",
      "Πρωινό Χαμόγελο"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Μαρίνα Κουντουράτου ήταν η ξανθιά παρουσιάστρια της πρωινής εκπομπής 'Πρωινό Χαμόγελο' που ερωτεύτηκε τον θεατρικό σκηνοθέτη Κωνσταντίνο Μαρκορά.",
    "funFacts": [
      "Τον ρόλο του διανοούμενου θεατρικού σκηνοθέτη Κωνσταντίνου Μαρκορά υποδύθηκε ο Νίκος Σεργιανόπουλος.",
      "Η σειρά των Αλέξανδρου Ρήγα και Δημήτρη Αποστόλου παραμένει μία από τις πιο δημοφιλείς κωμωδίες στην ιστορία του Mega Channel."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%94%CF%85%CE%BF_%CE%9E%CE%AD%CE%BD%CE%BF%CE%B9",
    "locale": "el-GR",
    "tags": ["dyo_xenoi", "greek_tv", "comedy", "mega"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_043",
    "text": "Σε ποιο φανταστικό ορεινό χωριό της Αρκαδίας ήταν δήμαρχος ο Περίανδρος Πώποτας στη σειρά 'Το Καφέ της Χαράς';",
    "answers": [
      "Στο Κολοκοτρωνίτσι",
      "Στην Κάτω Ραχούλα",
      "Στο Πλατάνι",
      "Στον Άγιο Μηνά"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο συντηρητικός δήμαρχος Περίανδρος Πώποτας (Χάρης Ρώμας) κυβερνούσε το Κολοκοτρωνίτσι με το δόγμα 'Τάξις και Ηθική'.",
    "funFacts": [
      "Τα εξωτερικά γυρίσματα του χωριού Κολοκοτρωνίτσι πραγματοποιήθηκαν κυρίως στην ιστορική Καρυά Αργολίδας.",
      "Το διάσημο καφέ που άνοιξε η πρωτευουσιάνα Χαρά Χάσκα ήταν η αφορμή για όλες τις πολιτισμικές συγκρούσεις στο χωριό."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CE%BA%CE%B1%CF%86%CE%AD_%CF%84%CE%B7%CF%82_%CE%A7%CE%B1%CF%81%CE%AC%CF%82",
    "locale": "el-GR",
    "tags": ["to_kafe_tis_charas", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_044",
    "text": "Ποιο στρατιωτικό αξίωμα κατείχε ο χαρακτήρας του Γιάννη Μπέζου στη σειρά 'Της Ελλάδος τα Παιδιά';",
    "answers": [
      "Ταξίαρχος",
      "Σμήναρχος",
      "Λοχαγός",
      "Ναύαρχος"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Γιάννης Μπέζος υποδύθηκε τον Σμήναρχο Επαμεινώνδα Κάκαλο στην Πολεμική Αεροπορία στο Γραφείο Ενημέρωσης Αεροπορίας.",
    "funFacts": [
      "Η ατάκα 'Όχι άλλο Κάκαλο!' έγινε ένα από τα πιο γνωστά catchphrases της ελληνικής τηλεόρασης της δεκαετίας του 1990.",
      "Στη σειρά πρωταγωνιστούσαν επίσης οι Κώστας Ευριπιώτης (Γεώργιος Βλάχος), Νίκος Αλεξίου (Πλαπούτας) και Γιάννης Σαββιδάκης (Ντάλας)."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82_%CF%84%CE%B1_%CF%80%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC",
    "locale": "el-GR",
    "tags": ["tis_ellados_ta_paidia", "greek_tv", "comedy", "ant1"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_045",
    "text": "Ποιος από τους παρακάτω σεφ ΔΕΝ ανήκει στην κλασική τριάδα κριτών του 'MasterChef Greece';",
    "answers": [
      "Σωτήρης Κοντιζάς",
      "Πάνος Ιωαννίδης",
      "Έκτορας Μποτρίνι",
      "Λεωνίδας Κουτσόπουλος"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η δημοφιλής κριτική επιτροπή του MasterChef Greece αποτελείται από τους Σωτήρη Κοντιζά, Πάνο Ιωαννίδη και Λεωνίδα Κουτσόπουλο. Ο Έκτορας Μποτρίνι έγινε γνωστός από το 'Εφιάλτης στην Κουζίνα'.",
    "funFacts": [
      "Η τριάδα των κριτών συνεργάζεται ανελλιπώς από το 2018 (όταν προστέθηκε ο Λεωνίδας Κουτσόπουλος) γνωρίζοντας τεράστια επιτυχία.",
      "Το MasterChef Greece προβλήθηκε για πρώτη φορά το 2010 στο Mega πριν μεταφερθεί με νέα μορφή στο Star το 2017."
    ],
    "source": "https://el.wikipedia.org/wiki/MasterChef_Greece",
    "locale": "el-GR",
    "tags": ["masterchef", "greek_tv", "reality", "cooking"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_046",
    "text": "Ποιο άλμπουμ του Michael Jackson, που κυκλοφόρησε το 1982, παραμένει το άλμπουμ με τις μεγαλύτερες πωλήσεις στην ιστορία της μουσικής;",
    "answers": [
      "Bad",
      "Off the Wall",
      "Dangerous",
      "Thriller"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Thriller' του Michael Jackson έχει πουλήσει πάνω από 70 εκατομμύρια αντίτυπα παγκοσμίως και περιλαμβάνει επιτυχίες όπως τα 'Billie Jean' και 'Beat It'.",
    "funFacts": [
      "Το μουσικό βίντεο κλιπ διάρκειας 14 λεπτών του 'Thriller' σκηνοθετήθηκε από τον John Landis και άλλαξε για πάντα τη βιομηχανία των music videos.",
      "Στο ομώνυμο τραγούδι, ο θρυλικός ηθοποιός ταινιών τρόμου Vincent Price πραγματοποίησε τη διάσημη τρομακτική αφήγηση και το γέλιο."
    ],
    "source": "https://el.wikipedia.org/wiki/Thriller_(%CE%AC%CE%BB%CE%BC%CF%80%CE%BF%CF%85%CE%BC)",
    "locale": "el-GR",
    "tags": ["michael_jackson", "thriller", "music", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_047",
    "text": "Ποιο διάσημο τραγούδι της Madonna κυκλοφόρησε το 1984 και εκτόξευσε την καριέρα της ως 'Βασίλισσα της Ποπ';",
    "answers": [
      "Like a Virgin",
      "Vogue",
      "Material Girl",
      "Hung Up"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το 'Like a Virgin' αποτέλεσε το πρώτο νούμερο ένα single της Madonna στο αμερικανικό Billboard Hot 100.",
    "funFacts": [
      "Η ερμηνεία της στα πρώτα MTV Video Music Awards το 1984 με νυφικό πάνω σε μια τεράστια γαμήλια τούρτα έγραψε τηλεοπτική ιστορία.",
      "Το περιοδικό Rolling Stone και το MTV κατέταξαν το 'Like a Virgin' ανάμεσα στα πιο επιδραστικά ποπ τραγούδια όλων των εποχών."
    ],
    "source": "https://en.wikipedia.org/wiki/Like_a_Virgin_(song)",
    "locale": "el-GR",
    "tags": ["madonna", "music", "pop", "80s"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_048",
    "text": "Ποιος ήταν ο χαρισματικός τραγουδιστής και frontman του θρυλικού ροκ συγκροτήματος Queen;",
    "answers": [
      "Μπράιαν Μέι",
      "Φρέντι Μέρκιουρι",
      "Ντέιβιντ Μπόουι",
      "Ρότζερ Τέιλορ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Freddie Mercury (Φρέντι Μέρκιουρι) ήταν ο τραγουδιστής και πιανίστας των Queen, διάσημος για το εκπληκτικό φωνητικό του εύρος.",
    "funFacts": [
      "Η εμφάνιση των Queen στη συναυλία Live Aid στο στάδιο Wembley το 1985 ψηφίστηκε ως η σπουδαιότερη ζωντανή ροκ εμφάνιση όλων των εποχών.",
      "Το πραγματικό όνομα του Freddie Mercury ήταν Farrokh Bulsara και είχε γεννηθεί στη Ζανζιβάρη."
    ],
    "source": "https://el.wikipedia.org/wiki/%CE%A6%CF%81%CE%AD%CE%BD%CF%84%CE%B9_%CE%9C%CF%80%CE%AD%CF%81%CE%BA%CE%B9%CE%BF%CF%85%CF%81%CE%B9",
    "locale": "el-GR",
    "tags": ["queen", "freddie_mercury", "music", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_049",
    "text": "Από ποια βρετανική πόλη ξεκίνησε την πορεία του το ιστορικό συγκρότημα The Beatles;",
    "answers": [
      "Λονδίνο",
      "Μάντσεστερ",
      "Λίβερπουλ",
      "Μπέρμιγχαμ"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Τα τέσσερα 'σκαθάρια' (John Lennon, Paul McCartney, George Harrison, Ringo Starr) σχημάτισαν τους Beatles στο Λίβερπουλ το 1960.",
    "funFacts": [
      "Το διάσημο Cavern Club στο Λίβερπουλ φιλοξένησε σχεδόν 300 ζωντανές εμφανίσεις των Beatles στα πρώτα τους βήματα.",
      "Η φωτογραφία των Beatles να διασχίζουν τη διάβαση πεζών στο Abbey Road έγινε ένα από τα πιο αναγνωρίσιμα εξώφυλλα άλμπουμ στην ιστορία."
    ],
    "source": "https://el.wikipedia.org/wiki/The_Beatles",
    "locale": "el-GR",
    "tags": ["the_beatles", "music", "liverpool", "rock"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_050",
    "text": "Με ποιο τραγούδι κέρδισε το σουηδικό συγκρότημα ABBA τον Διαγωνισμό Τραγουδιού της Eurovision το 1974;",
    "answers": [
      "Mamma Mia",
      "Dancing Queen",
      "Gimme! Gimme! Gimme!",
      "Waterloo"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Οι ABBA κατέκτησαν την 1η θέση στη Eurovision του 1974 στο Μπράιτον με το τραγούδι 'Waterloo', ξεκινώντας την παγκόσμια καριέρα τους.",
    "funFacts": [
      "Το όνομα ABBA είναι ακρωνύμιο των πρώτων γραμμάτων των ονομάτων των τεσσάρων μελών: Agnetha, Björn, Benny, Anni-Frid.",
      "Το 2005, το 'Waterloo' ψηφίστηκε ως το καλύτερο τραγούδι στην 50χρονη ιστορία του διαγωνισμού της Eurovision."
    ],
    "source": "https://en.wikipedia.org/wiki/Waterloo_(ABBA_song)",
    "locale": "el-GR",
    "tags": ["abba", "eurovision", "music", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_051",
    "text": "Σε ποιο γυναικείο r&b συγκρότημα ξεκίνησε την καριέρα της η Beyoncé πριν ακολουθήσει σόλο πορεία;",
    "answers": [
      "Destiny's Child",
      "TLC",
      "Spice Girls",
      "The Pussycat Dolls"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Beyoncé Knowles ήταν η βασική τραγουδίστρια των Destiny's Child, οι οποίες γνώρισαν τεράστια επιτυχία με τραγούδια όπως το 'Survivor'.",
    "funFacts": [
      "Η Beyoncé κατέχει το ρεκόρ για τα περισσότερα βραβεία Grammy στην ιστορία της μουσικής (32 βραβεία).",
      "Το άλμπουμ της 'Renaissance' (2022) απέσπασε διθυραμβικές κριτικές αποτίοντας φόρο τιμής στην queer και ballroom κουλτούρα της μαύρης μουσικής σκηνής."
    ],
    "source": "https://en.wikipedia.org/wiki/Beyonc%C3%A9",
    "locale": "el-GR",
    "tags": ["beyonce", "destinys_child", "music", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_052",
    "text": "Ποιο είναι το αγαπημένο φαγητό της γάτας Garfield στο ομώνυμο διάσημο κόμικ;",
    "answers": [
      "Πίτσα",
      "Λαζάνια",
      "Μακαρόνια με κιμά",
      "Χάμπουργκερ"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Garfield, ο πορτοκαλί γάτος του Jim Davis, λατρεύει παθολογικά τα λαζάνια και μισεί τις Δευτέρες.",
    "funFacts": [
      "Ο Garfield γεννήθηκε στην κουζίνα ενός ιταλικού εστιατορίου (Mama Leoni's), γεγονός που εξηγεί το πάθος του για τα λαζάνια.",
      "Το κόμικ του Garfield κατέχει το Ρεκόρ Γκίνες ως το πιο ευρέως διανεμημένο κόμικ στριπ στον κόσμο, σε πάνω από 2.500 εφημερίδες."
    ],
    "source": "https://en.wikipedia.org/wiki/Garfield",
    "locale": "el-GR",
    "tags": ["garfield", "comics", "animation", "pop"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_053",
    "text": "Σε ποια έπαυλη στο Μέμφις του Τενεσί έζησε και τάφηκε ο 'Βασιλιάς του Ροκ εν Ρολ' Elvis Presley;",
    "answers": [
      "Neverland",
      "Paisley Park",
      "Graceland",
      "Skywalker Ranch"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Graceland ήταν η θρυλική κατοικία του Elvis Presley και σήμερα αποτελεί ένα από τα πιο δημοφιλή μουσεία στις ΗΠΑ.",
    "funFacts": [
      "Η Graceland είναι η δεύτερη πιο επισκέψιμη ιδιωτική κατοικία στις ΗΠΑ, πίσω μόνο από τον Λευκό Οίκο.",
      "Ο Elvis Presley αγόρασε το κτήμα Graceland το 1957 στην ηλικία των μόλις 22 ετών."
    ],
    "source": "https://en.wikipedia.org/wiki/Graceland",
    "locale": "el-GR",
    "tags": ["elvis_presley", "music", "graceland", "rock_and_roll"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_054",
    "text": "Πώς αποκαλεί η Lady Gaga τους πιστούς θαυμαστές της σε όλο τον κόσμο;",
    "answers": [
      "Swifties",
      "Beliebers",
      "Barbs",
      "Little Monsters"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Η Lady Gaga ονομάζει τους θαυμαστές της 'Little Monsters', ενώ η ίδια αυτοαποκαλείται συχνά 'Mother Monster'.",
    "funFacts": [
      "Το όνομα προήλθε μετά την κυκλοφορία του εξαιρετικά επιτυχημένου EP της 'The Fame Monster' το 2009.",
      "Η Lady Gaga έχει κάνει τατουάζ τη φράση 'Little Monsters' στο αριστερό της μπράτσο ως φόρο τιμής στο κοινό της."
    ],
    "source": "https://en.wikipedia.org/wiki/Lady_Gaga",
    "locale": "el-GR",
    "tags": ["lady_gaga", "music", "pop", "fandom"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_055",
    "text": "Ποιο είναι το επάγγελμα του Super Mario στα διάσημα βιντεοπαιχνίδια της Nintendo;",
    "answers": [
      "Υδραυλικός",
      "Ηλεκτρολόγος",
      "Μαραγκός",
      "Μηχανικός αυτοκινήτων"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Super Mario και ο αδελφός του Luigi είναι Ιταλοαμερικανοί υδραυλικοί που ταξιδεύουν μέσα από σωλήνες στο Mushroom Kingdom.",
    "funFacts": [
      "Στην πρώτη του εμφάνιση στο παιχνίδι Donkey Kong (1981), ο χαρακτήρας ονομαζόταν 'Jumpman' και ήταν ξυλουργός.",
      "Το μουστάκι και το καπέλο του Mario σχεδιάστηκαν επειδή ήταν αδύνατο να αποδοθούν λεπτομέρειες προσώπου και μαλλιών στα 8-bit γραφικά."
    ],
    "source": "https://en.wikipedia.org/wiki/Mario",
    "locale": "el-GR",
    "tags": ["mario", "nintendo", "gaming", "video_games"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_056",
    "text": "Ποιο Pokémon είναι ο μόνιμος σύντροφος του Ash Ketchum που αρνείται να μπει μέσα σε Poké Ball;",
    "answers": [
      "Charmander",
      "Pikachu",
      "Squirtle",
      "Bulbasaur"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Ο Pikachu είναι ο πιστός ηλεκτρικός σύντροφος του Ash, ο οποίος προτιμά να ταξιδεύει στον ώμο του παρά μέσα σε Poké Ball.",
    "funFacts": [
      "Ο Pikachu εκπέμπει ισχυρές ηλεκτρικές εκκενώσεις από τα κόκκινα κυκλικά μάγουλά του.",
      "Αρχικά, η μασκότ του franchise Pokémon προοριζόταν να είναι το Clefairy, αλλά ο Pikachu επιλέχθηκε λόγω της ευρύτερης γοητείας του."
    ],
    "source": "https://en.wikipedia.org/wiki/Pikachu",
    "locale": "el-GR",
    "tags": ["pokemon", "pikachu", "anime", "gaming"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_057",
    "text": "Ποιο από τα παρακάτω ΔΕΝ είναι ένα από τα τέσσερα κλασικά φαντάσματα στο βιντεοπαιχνίδι 'Pac-Man';",
    "answers": [
      "Blinky (κόκκινο)",
      "Pinky (ροζ)",
      "Casper (άσπρο)",
      "Inky (γαλάζιο)"
    ],
    "correctAnswerIndex": 2,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Τα τέσσερα φαντάσματα του Pac-Man είναι οι Blinky (κόκκινο), Pinky (ροζ), Inky (γαλάζιο) και Clyde (πορτοκαλί). Ο Casper είναι χαρακτήρας κινουμένων σχεδίων.",
    "funFacts": [
      "Κάθε φάντασμα στο Pac-Man έχει διαφορετικό πρόγραμμα τεχνητής νοημοσύνης (ο Blinky κυνηγά άμεσα, ο Pinky στήνει ενέδρα κ.λπ.).",
      "Το σχήμα του Pac-Man εμπνεύστηκε από μια πίτσα στην οποία έλειπε ένα κομμάτι."
    ],
    "source": "https://en.wikipedia.org/wiki/Pac-Man",
    "locale": "el-GR",
    "tags": ["pac_man", "gaming", "arcade", "retro"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_058",
    "text": "Ποιο εχθρικό πλάσμα στο βιντεοπαιχνίδι 'Minecraft' πλησιάζει αθόρυβα τον παίκτη και εκρήγνυται;",
    "answers": [
      "Zombie",
      "Skeleton",
      "Enderman",
      "Creeper"
    ],
    "correctAnswerIndex": 3,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Creeper είναι ένα πράσινο, σιωπηλό πλάσμα που σφυρίζει λίγο πριν εκραγεί καταστρέφοντας ό,τι βρίσκεται γύρω του.",
    "funFacts": [
      "Το Creeper δημιουργήθηκε κατά λάθος από τον προγραμματιστή Notch, όταν έβαλε λάθος διαστάσεις ύψους και μήκους σε ένα μοντέλο γουρουνιού.",
      "Το Minecraft είναι το βιντεοπαιχνίδι με τις περισσότερες πωλήσεις όλων των εποχών, ξεπερνώντας τα 300 εκατομμύρια αντίτυπα."
    ],
    "source": "https://en.wikipedia.org/wiki/Creeper_(Minecraft)",
    "locale": "el-GR",
    "tags": ["minecraft", "gaming", "video_games", "mojang"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_059",
    "text": "Πόσοι παίκτες πέφτουν από το λεωφορείο μάχης (Battle Bus) σε έναν τυπικό αγώνα Battle Royale του 'Fortnite';",
    "answers": [
      "100 παίκτες",
      "50 παίκτες",
      "64 παίκτες",
      "150 παίκτες"
    ],
    "correctAnswerIndex": 0,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Στη λειτουργία Battle Royale του Fortnite, 100 παίκτες πέφτουν με αλεξίπτωτο στο νησί και πολεμούν μέχρι να μείνει μόνο ένας νικητής.",
    "funFacts": [
      "Το Fortnite της Epic Games πραγματοποίησε ιστορικές εικονικές συναυλίες εντός παιχνιδιού με καλλιτέχνες όπως ο Travis Scott και η Ariana Grande.",
      "Οι χοροί και τα emoticons του Fortnite έγιναν παγκόσμιο φαινόμενο στη σύγχρονη νεανική κουλτούρα."
    ],
    "source": "https://en.wikipedia.org/wiki/Fortnite_Battle_Royale",
    "locale": "el-GR",
    "tags": ["fortnite", "gaming", "epic_games", "battle_royale"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  },
  {
    "id": "pop_culture_easy_060",
    "text": "Ποια είναι η πιο διάσημη ενεργειακή επίθεση του Son Goku στη σειρά άνιμε 'Dragon Ball';",
    "answers": [
      "Spirit Bomb (Genki Dama)",
      "Kamehameha",
      "Final Flash",
      "Special Beam Cannon"
    ],
    "correctAnswerIndex": 1,
    "categoryId": "pop_culture",
    "difficulty": 1,
    "explanation": "Το Kamehameha είναι η χαρακτηριστική επίθεση συμπυκνωμένης ενέργειας του Goku, την οποία διδάχθηκε από τον Master Roshi.",
    "funFacts": [
      "Το όνομα Kamehameha προτάθηκε στον δημιουργό Akira Toriyama από τη σύζυγό του, παρμένο από τον ιστορικό βασιλιά της Χαβάης Kamehameha I.",
      "Στα ιαπωνικά, η λέξη Kamehameha περιέχει τη λέξη 'Kame' που σημαίνει χελώνα, παραπέμποντας στη Σχολή της Χελώνας (Turtle School)."
    ],
    "source": "https://en.wikipedia.org/wiki/Kamehameha_(Dragon_Ball)",
    "locale": "el-GR",
    "tags": ["dragon_ball", "anime", "goku", "manga"],
    "status": "reviewed",
    "verifiedAt": "2026-10-25"
  }
]

if __name__ == "__main__":
    validate_and_append('pop_culture', 'easy', 1, questions)

# -*- coding: utf-8 -*-
"""Generator for music_hard batch 3 (IDs 311-360)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_generator import validate_and_append

QUESTIONS = [
    {
        "id": "music_hard_311",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος αρχαίος Έλληνας θεωρητικός της μουσικής ανέπτυξε το σύστημα των δεκαπέντε «τόνων» και συνέγραψε τα «Αρμονικά» σε τρία βιβλία τον 2ο αιώνα μ.Χ.;",
        "answers": ["Κλαύδιος Πτολεμαίος", "Αριστόξενος ο Ταραντίνος", "Νικόμαχος ο Γερασηνός", "Αλύπιος"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Κλαύδιος Πτολεμαίος στα «Αρμονικά» του άσκησε κριτική τόσο στους Πυθαγόρειους όσο και στους Αριστοξενικούς, αναπτύσσοντας ένα λεπτομερές μαθηματικό σύστημα διαστημάτων και τόνων.",
        "funFacts": [
            "Ο Πτολεμαίος συνέδεσε τους μουσικούς φθόγγους με την κίνηση των ουράνιων σφαιρών.",
            "Τα «Αρμονικά» του διασώθηκαν και αποτέλεσαν θεμελιώδη πηγή για τη δυτική αναγεννησιακή θεωρία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%B1%CF%8D%CE%B4%CE%B9%CE%BF%CF%82_%CE%A0%CF%84%CE%BF%CE%BB%CE%B5%CE%BC%CE%B1%CE%AF%CE%BF%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["ancient-greece", "music-theory", "ptolemy", "harmonics"]
    },
    {
        "id": "music_hard_312",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στη βυζαντινή μουσική θεωρία, ποιο είναι το ακριβές μέγεθος του «ελάχιστου τόνου» σύμφωνα με την κλίμακα των 72 μορίων της Πατριαρχικής Επιτροπής του 1881;",
        "answers": ["7 μόρια", "9 μόρια", "12 μόρια", "5 μόρια"],
        "correctAnswerIndex": 0,
        "explanation": "Στην κλίμακα 72 κομμάτων/μορίων της Πατριαρχικής Επιτροπής του 1881, ο μείζων τόνος έχει 12 μόρια, ο ελάσσων 9 μόρια και ο ελάχιστος τόνος 7 μόρια.",
        "funFacts": [
            "Η υποδιαίρεση της οκτάβας σε 72 ίσα τμήματα επιτρέπει τη μαθηματική περιγραφή των μικροδιαστημάτων της ψαλτικής.",
            "Τα 7 μόρια αντιστοιχούν κατά προσέγγιση σε περίπου 116,7 cents."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CF%85%CE%B6%CE%B1%CE%BD%CF%84%CE%B9%CE%BD%CE%AE_%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["byzantine-music", "microtones", "music-theory"]
    },
    {
        "id": "music_hard_313",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο καινοτόμο ηλεκτρονικό ηχητικό σύστημα σχεδίασε και υλοποίησε ο Ιάννης Ξενάκης στο CEMAMu το 1977, επιτρέποντας τη σύνθεση μουσικής μέσω γραφικών σχεδίων σε ψηφιοποιητή;",
        "answers": ["UPIC", "Synthesizer 100", "Polytopos", "Groupe de Recherches Musicales"],
        "correctAnswerIndex": 0,
        "explanation": "Το σύστημα UPIC (Unité Polyagogique Informatique du CEMAMu) επέτρεπε στους συνθέτες να σχεδιάζουν γραφικές κυματομορφές και μουσικές δομές που μετατρέπονταν άμεσα σε ήχο.",
        "funFacts": [
            "Το γνωστό έργο του Ξενάκη «Μυκήνες Άλφα» (1978) συντέθηκε εξ ολοκλήρου με το σύστημα UPIC.",
            "Το UPIC χρησιμοποιήθηκε επίσης ως παιδαγωγικό εργαλείο για παιδιά χωρίς μουσικές γνώσεις σημειογραφίας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%99%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%9E%CE%B5%CE%BD%CE%AC%CE%BA%CE%B7%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["xenakis", "avant-garde", "electronic-music", "upic"]
    },
    {
        "id": "music_hard_314",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στη σειραϊκή τεχνική και το δωδεκαφθογγισμό, ποιος όρος δηλώνει τη διαδοχή των φθόγγων της βασικής σειράς από το τέλος προς την αρχή;",
        "answers": ["Καρκινική μορφή (Retrograde)", "Αναστροφή (Inversion)", "Καρκινική αναστροφή (Retrograde Inversion)", "Μεταφορά (Transposition)"],
        "correctAnswerIndex": 0,
        "explanation": "Η καρκινική μορφή (retrograde ή Cancrizans) προκύπτει όταν διαβάζουμε τη δωδεκάφθογγη σειρά από τον τελευταίο φθόγγο προς τον πρώτο.",
        "funFacts": [
            "Ο όρος «καρκινικός» προέρχεται από την κίνηση του κάβουρα (καρκίνου) προς τα πίσω.",
            "Κάθε δωδεκάφθογγη σειρά διαθέτει 48 βασικές παραλλαγές μέσω αναστροφών, καρκίνων και μεταφορών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CF%89%CE%B4%CE%B5%CE%BA%CE%B1%CF%86%CE%B8%CE%BF%CE%B3%CE%B3%CE%B9%CF%83%CE%BC%CF%8C%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["twelve-tone", "serialism", "music-theory", "schoenberg"]
    },
    {
        "id": "music_hard_315",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Arnold Schoenberg (1912) καθιέρωσε τη φωνητική τεχνική «Sprechstimme» (ομιλούσα φωνή) σε ποίηση Albert Giraud;",
        "answers": ["Pierrot Lunaire", "Erwartung", "Moses und Aron", "Gurre-Lieder"],
        "correctAnswerIndex": 0,
        "explanation": "Το Pierrot Lunaire (έργο 21) για αφηγήτρια και οργανικό σύνολο αξιοποιεί συστηματικά το Sprechstimme, όπου οι νότες προφέρονται αλλά δεν διατηρούν καθαρό τραγουδιστό τόνο.",
        "funFacts": [
            "Στην παρτιτούρα, οι νότες του Sprechstimme συμβολίζονται με ένα μικρό «x» στο στέλεχος της νότας.",
            "Το οργανικό σύνολο περιλαμβάνει φλάουτο/πίκολο, κλαρινέτο/μπάσο κλαρινέτο, βιολί/βιόλα, τσέλο και πιάνο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%86%CF%81%CE%BD%CE%BF%CE%BB%CE%BD%CF%84_%CE%A3%CE%AD%CE%BD%CE%BC%CF%80%CE%B5%CF%81%CE%B3%CE%BA",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["schoenberg", "sprechstimme", "modernism", "opera"]
    },
    {
        "id": "music_hard_316",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια είναι η ακριβής διάταξη τόνων και ημιτονίων στην οκτατονική κλίμακα (κλίμακα Korsakov/Petrushka) όταν ξεκινά με ημιτόνιο;",
        "answers": ["Ημιτόνιο - Τόνος - Ημιτόνιο - Τόνος - Ημιτόνιο - Τόνος - Ημιτόνιο - Τόνος", "Τόνος - Τόνος - Ημιτόνιο - Τόνος - Τόνος - Τόνος - Ημιτόνιο", "Ημιτόνιο - Τριημιτόνιο - Ημιτόνιο - Τόνος - Ημιτόνιο - Τριημιτόνιο - Τόνος", "Τόνος - Ημιτόνιο - Ημιτόνιο - Τόνος - Ημιτόνιο - Τόνος - Ημιτόνιο - Τόνος"],
        "correctAnswerIndex": 0,
        "explanation": "Η οκτατονική κλίμακα αποτελείται από εναλλασσόμενα ημιτόνια και τόνους (είτε ημιτόνιο-τόνος είτε τόνος-ημιτόνιο), περιέχοντας 8 φθόγγους στην οκτάβα.",
        "funFacts": [
            "Αποτελεί μία από τις έξι συμμετρικές «κλίμακες περιορισμένων μεταφορών» κατά τον Olivier Messiaen (Mode 2).",
            "Χρησιμοποιήθηκε εκτενώς από τους Ρίμσκι-Κόρσακοφ, Στραβίνσκι και Μπάρτοκ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%99%CE%B3%CE%BA%CF%8C%CF%81_%CE%A3%CF%84%CF%81%CE%B1%CE%B2%CE%AF%CE%BD%CF%83%CE%BA%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["octatonic", "music-theory", "stravinsky", "messiaen"]
    },
    {
        "id": "music_hard_317",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος Έλληνας συνθέτης και θεωρητικός εισήγαγε τη δεκαπενταφωνική κλίμακα και ίδρυσε τη «Μουσική Εταιρεία Αθηνών» το 1871;",
        "answers": ["Αλέξανδρος Κατακουζηνός", "Σπυρίδων Ξύνδας", "Νικόλαος Μάντζαρος", "Παύλος Καρρέρ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Αλέξανδρος Κατακουζηνός (1824–1892) υπήρξε πρωτοπόρος μουσικοδιδάσκαλος, χοράρχης και συνθέτης που επεχείρησε τη θεωρητική γεφύρωση δυτικής και βυζαντινής μουσικής.",
        "funFacts": [
            "Δίδαξε στην Οδησσό και στην Αθήνα, συμβάλλοντας καθοριστικά στην τετράφωνη εκκλησιαστική μουσική.",
            "Υπήρξε από τους ιδρυτές του Ωδείου Αθηνών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A9%CE%B4%CE%B5%CE%AF%CE%BF_%CE%91%CE%B8%CE%B7%CE%BD%CF%8E%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["greek-classical", "19th-century", "athens-conservatory"]
    },
    {
        "id": "music_hard_318",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος ήταν ο πρώτος διευθυντής του Ωδείου Αθηνών κατά την ίδρυσή του το 1871;",
        "answers": ["Αλέξανδρος Κατακουζηνός", "Γεώργιος Νάζος", "Διονύσιος Λαυράγκας", "Μανώλης Καλομοίρης"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Αλέξανδρος Κατακουζηνός ήταν ο πρώτος μουσικός διευθυντής του Ωδείου Αθηνών κατά τα εγκαίνιά του το 1871.",
        "funFacts": [
            "Αργότερα, υπό τη διεύθυνση του Γεωργίου Νάζου (από το 1891), το Ωδείο αναδιοργανώθηκε κατά τα γερμανικά πρότυπα.",
            "Το Ωδείο Αθηνών είναι το αρχαιότερο μουσικοεκπαιδευτικό ίδρυμα της νεότερης Ελλάδας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A9%CE%B4%CE%B5%CE%AF%CE%BF_%CE%91%CE%B8%CE%B7%CE%BD%CF%8E%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["athens-conservatory", "institutions", "history"]
    },
    {
        "id": "music_hard_319",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο όνομα φέρει η διάσημη συγχορδία «F - B - D# - G#» που ακούγεται στην έναρξη της όπερας του Richard Wagner «Τριστάνος και Ιζόλδη»;",
        "answers": ["Συγχορδία του Τριστάνου", "Συγχορδία του Προμηθέα", "Συγχορδία του Πέτρουσκα", "Μυστική συγχορδία"],
        "correctAnswerIndex": 0,
        "explanation": "Η «συγχορδία του Τριστάνου» (Tristan chord) αποτελεί σημείο καμπής στην αρμονία του 19ου αιώνα λόγω της τονικής της αμφισημίας και της καθυστέρησης της λύσης της.",
        "funFacts": [
            "Αναλύεται συχνά ως ημι-ελαττωμένη έβδομης ή ως τροποποιημένη προπαρασκευαστική της δεσπόζουσας (γαλλική 6η).",
            "Θεωρείται ιστορικά η απαρχή της διάλυσης της παραδοσιακής λειτουργικής αρμονίας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A1%CE%AF%CF%87%CE%B1%CF%81%CE%BD%CF%84_%CE%92%CE%AC%CE%B3%CE%BA%CE%BD%CE%B5%CF%81",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["wagner", "harmony", "opera", "tristan"]
    },
    {
        "id": "music_hard_320",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια εξαφθογγική συγχορδία (C - F# - Bb - E - A - D) χρησιμοποίησε ο Alexander Scriabin ως αρμονική βάση στο συμφωνικό ποίημα «Προμηθεύς: Το Ποίημα της Φωτιάς»;",
        "answers": ["Μυστική συγχορδία (Mystic chord)", "Συγχορδία Τριστάνου", "Ηλεκτρική συγχορδία", "Συγχορδία Elektra"],
        "correctAnswerIndex": 0,
        "explanation": "Η «Μυστική συγχορδία» (Mystic chord ή Συγχορδία του Προμηθέα) προκύπτει από διαδοχικά διαστήματα τετάρτων (αυξημένης, ελαττωμένης, καθαρής) και καθόρισε το ύστερο στιλ του Σκριάμπιν.",
        "funFacts": [
            "Ο Σκριάμπιν συνέδεσε τη συγχορδία αυτή με τη θεοσοφία και το φαινόμενο της συναισθησίας (χρώμα-ήχος).",
            "Για την εκτέλεση του έργου προβλεπόταν ειδικό «πληκτρολόγιο φωτός» (clavier à lumières)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B5%CE%BE%CE%AC%CE%BD%CF%84%CF%81_%CE%A3%CE%BA%CF%81%CE%B9%CE%AC%CE%BC%CF%80%CE%B9%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["scriabin", "mystic-chord", "harmony", "synesthesia"]
    },
    {
        "id": "music_hard_321",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος Έλληνας συνθέτης ίδρυσε το 1965 το «Εργαστήριο Σύγχρονης Μουσικής» στο Ινστιτούτο Γκαίτε Αθηνών και προώθησε έντονα την πρωτοποριακή μουσική;",
        "answers": ["Γιάννης Γ. Παπαϊωάννου", "Μιχάλης Αδάμης", "Θόδωρος Αντωνίου", "Γιώργος Σισιλιάνος"],
        "correctAnswerIndex": 0,
        "explanation": "Ο μουσικολόγος και αρχιτέκτονας Γιάννης Γ. Παπαϊωάννου (1910–1989) υπήρξε πρόεδρος του Ελληνικού Συνδέσμου Σύγχρονης Μουσικής και κινητήριος μοχλός των πρωτοποριακών συναυλιών στο Ινστιτούτο Γκαίτε.",
        "funFacts": [
            "Διοργάνωσε τις ιστορικές «Εβδομάδες Σύγχρονης Μουσικής» στην Αθήνα μεταξύ 1966 και 1976.",
            "Υπήρξε βαθύς μελετητής και βιογράφος του Νίκου Σκαλκώτα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%93._%CE%A0%CE%B1%CF%80%CE%B1%CF%8A%CF%89%CE%AC%CE%BD%CE%BD%CE%BF%CF%85_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%BF%CE%BB%CF%8C%CE%B3%CE%BF%CF%82)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["greek-avant-garde", "contemporary-music", "musicology"]
    },
    {
        "id": "music_hard_322",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο πρωτοποριακό έργο ηλεκτροακουστικής μουσικής συνέθεσε ο Μιχάλης Αδάμης το 1968, συνδυάζοντας βυζαντινή ψαλτική και ηλεκτρονικούς ήχους;",
        "answers": ["Κράτημα", "Αποκάλυψη", "Μεταλλάξεις", "Γένεσις"],
        "correctAnswerIndex": 0,
        "explanation": "Το «Κράτημα» (1968) του Μιχάλη Αδάμη για ψάλτη και μαγνητοταινία αποτελεί ορόσημο της ελληνικής ηλεκτροακουστικής μουσικής, ενσωματώνοντας βυζαντινά φωνητικά ιδιώματα σε ηλεκτρονικό περιβάλλον.",
        "funFacts": [
            "Ο ψάλτης στο έργο τραγουδά παραδοσιακούς τερετισμούς (νανά, τορορό) χωρίς λεξικό νόημα.",
            "Ο Αδάμης είχε ιδρύσει το πρώτο ιδιωτικό στούντιο ηλεκτρονικής μουσικής στην Αθήνα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CF%87%CE%AC%CE%BB%CE%B7%CF%82_%CE%91%CE%B4%CE%AC%CE%BC%CE%B7%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["adamis", "electroacoustic", "byzantine-music"]
    },
    {
        "id": "music_hard_323",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Πώς ονομάζεται στην αναγεννησιακή πολυφωνία η τεχνική όπου μια μελωδία εκτελείται ταυτόχρονα σε διαφορετικές ταχύτητες (π.χ. αξίες διπλάσιας διάρκειας) από διαφορετικές φωνές;",
        "answers": ["Κανόνας αναλογιών (Mensuration canon)", "Κανόνας αινιγματικός", "Αντίστιξη καθ' υπερβολήν", "Ομοφωνία"],
        "correctAnswerIndex": 0,
        "explanation": "Ο κανόνας αναλογιών (mensuration ή prolation canon) χαρακτηρίζεται από φωνές που ξεκινούν ταυτόχρονα το ίδιο θέμα αλλά σε διαφορετικά μέτρα ή ρυθμικές υποδιαιρέσεις (όπως στη Missa Prolationum του Ockeghem).",
        "funFacts": [
            "Ο Johannes Ockeghem θεωρείται ο κορυφαίος δεξιοτέχνης αυτού του είδους αντίστιξης.",
            "Στην παρτιτούρα γραφόταν συχνά μόνο μία μελωδική γραμμή με πολλαπλά ρυθμικά σύμβολα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB%CF%85%CF%86%CF%89%CE%BD%CE%AF%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["polyphony", "counterpoint", "renaissance", "canon"]
    },
    {
        "id": "music_hard_324",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στο στυλ του Palestrina (prima pratica), ποιος κανόνας διέπει αυστηρά την προετοιμασία και τη λύση μιας παραφωνίας;",
        "answers": ["Η παραφωνία πρέπει να προετοιμάζεται σε άρση ως σύμφωνος φθόγγος, να δένεται στη θέση και να λύνεται κατιόντως κατά βήμα", "Η παραφωνία εισάγεται ελεύθερα με πήδημα και λύνεται ανιόντως", "Επιτρέπεται οποιαδήποτε παραφωνία αρκεί να διπλασιάζεται στο μπάσο", "Η παραφωνία μπορεί να εμφανιστεί μόνο στον πρώτο χρόνο του μέτρου χωρίς προετοιμασία"],
        "correctAnswerIndex": 0,
        "explanation": "Στην αυστηρή αντίστιξη (Palestrina style), η καθυστέρηση (suspension) απαιτεί προετοιμασία σε σύμφωνη νότα, κράτημα στον ισχυρό χρόνο ως παραφωνία και υποχρεωτική βαθμιαία πτώση (λύση) κατά δεύτερη προς τα κάτω.",
        "funFacts": [
            "Ο Johann Joseph Fux τυποποίησε αυτούς τους κανόνες στο περίφημο σύγγραμμα «Gradus ad Parnassum» (1725).",
            "Ο Μπετόβεν, ο Μότσαρτ και ο Χάυντν εκπαιδεύτηκαν όλοι πάνω σε αυτούς τους αυστηρούς κανόνες."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%B2%CE%AC%CE%BD%CE%B9_%CE%A0%CE%B9%CE%B5%CF%81%CE%BB%CE%BF%CF%85%CE%AF%CF%84%CE%B6%CE%B9_%CE%BD%CF%84%CE%B1_%CE%A0%CE%B1%CE%BB%CE%B5%CF%83%CF%84%CF%81%CE%AF%CE%BD%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["palestrina", "counterpoint", "music-theory", "renaissance"]
    },
    {
        "id": "music_hard_325",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο εκκλησιαστικό έργο του Giovanni Pierluigi da Palestrina (περ. 1562) πιστώνεται παραδοσιακά ότι «έσωσε την πολυφωνία» στη Σύνοδο του Τριδέντου;",
        "answers": ["Missa Papae Marcelli", "Missa Brevis", "Stabat Mater", "Missa Assumpta est Maria"],
        "correctAnswerIndex": 0,
        "explanation": "Η Λειτουργία του Πάπα Μαρκέλλου (Missa Papae Marcelli) συντέθηκε έτσι ώστε τα λόγια να παραμένουν απολύτως κατανοητά παρά την εξαφωνική πολυφωνική πλοκή.",
        "funFacts": [
            "Η Σύνοδος του Τριδέντου είχε εξετάσει την πλήρη απαγόρευση της πολυφωνίας λόγω της ακαταληψίας των κειμένων.",
            "Ο Hans Pfitzner συνέθεσε το 1917 την όπερα «Palestrina» βασισμένος σε αυτόν τον θρύλο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%B2%CE%AC%CE%BD%CE%B9_%CE%A0%CE%B9%CE%B5%CF%81%CE%BB%CE%BF%CF%85%CE%AF%CF%84%CE%B6%CE%B9_%CE%BD%CF%84%CE%B1_%CE%A0%CE%B1%CE%BB%CE%B5%CF%83%CF%84%CF%81%CE%AF%CE%BD%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["palestrina", "polyphony", "sacred-music", "renaissance"]
    },
    {
        "id": "music_hard_326",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του αρχαιότερου πλήρους σωζόμενου μουσικού κομματιού με σημειογραφία και στίχους, χαραγμένου σε κυλινδρική επιτύμβια στήλη (1ος-2ος αι. μ.Χ.);",
        "answers": ["Επιτάφιος του Σεικίλου", "Ύμνοι της Οξυρρύγχου", "Δελφικοί Ύμνοι", "Παιάν του Μεσομήδους"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Επιτάφιος του Σεικίλου ανακαλύφθηκε κοντά στις Τράλλεις της Μικράς Ασίας και περιέχει πλήρη μελωδία και επίγραμμα σημειωμένα με αρχαία ελληνικά μουσικά σύμβολα.",
        "funFacts": [
            "Το κείμενο ξεκινά με τη φράση: «Ὅσον ζῇς φαίνου, μηδὲν ὅλως σὺ λυποῦ...».",
            "Σήμερα η πρωτότυπη στήλη φυλάσσεται στο Εθνικό Μουσείο της Δανίας στην Κοπεγχάγη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B9%CF%84%CE%AC%CF%86%CE%B9%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%B5%CE%B9%CE%BA%CE%AF%CE%BB%CE%BF%CF%85",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["ancient-greece", "seikilos", "notation", "archaeology"]
    },
    {
        "id": "music_hard_327",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το θεμελιώδες χαρακτηριστικό της μορφής σονάτας που διαφοροποιεί την Επανέκθεση (Recapitulation) από την Έκθεση (Exposition);",
        "answers": ["Το δεύτερο θέμα επανεκτίθεται στην αρχική τονικότητα (τονική) αντί της δεσπόζουσας ή σχετικής", "Το πρώτο θέμα παραλείπεται εντελώς στην επανέκθεση", "Όλα τα θέματα μεταφέρονται υποχρεωτικά σε ελάσσονα τρόπο", "Η επανέκθεση παίζεται αποκλειστικά από σόλο όργανο"],
        "correctAnswerIndex": 0,
        "explanation": "Στην Έκθεση το δεύτερο θέμα παρουσιάζεται σε άλλη τονικότητα (συνήθως δεσπόζουσα ή σχετική μείζονα), ενώ στην Επανέκθεση επιστρέφει στην κύρια τονικότητα (τονική) επιλύοντας την τονική ένταση.",
        "funFacts": [
            "Αυτή η τονική επίλυση ονομάζεται στη μουσικολογία «σονάτα-αρχή» (sonata principle).",
            "Η κλασική μορφή σονάτας αποκρυσταλλώθηκε στα έργα των Χάυντν, Μότσαρτ και Μπετόβεν."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CF%81%CF%86%CE%AE_%CF%83%CE%BF%CE%BD%CE%AC%CF%84%CE%B1%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["sonata-form", "music-theory", "classical-era"]
    },
    {
        "id": "music_hard_328",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια είναι η ακριβής διάκριση μεταξύ της αυθεντικής και της πλάγιας μορφής των αρχαιοελληνικών και εκκλησιαστικών τρόπων;",
        "answers": ["Ο πλάγιος τρόπος έχει έκταση από την υποδεσπόζουσα/δεσπόζουσα κάτω από την τονική (υποκείμενη 4η/5η), διατηρώντας την ίδια τελική (finalis)", "Ο πλάγιος τρόπος είναι γραμμένος πάντοτε σε ελάσσονα οπλισμό", "Ο αυθεντικός τρόπος δεν χρησιμοποιεί ποτέ διαστήματα ημιτονίου", "Ο πλάγιος τρόπος χρησιμοποιεί μόνο πέντε φθόγγους"],
        "correctAnswerIndex": 0,
        "explanation": "Στους γρηγοριανούς τρόπους, ο αυθεντικός έχει ambitus από τη finalis μέχρι την οκτάβα της, ενώ ο πλάγιος εκτείνεται από μία τέταρτη κάτω από τη finalis έως μία πέμπτη πάνω από αυτήν, έχοντας διαφορετική δεσπόζουσα (repercussio).",
        "funFacts": [
            "Το οκτωηχικό σύστημα διακρίνει 4 αυθεντικούς (Protus, Deuterus, Tritus, Tetrardus) και 4 αντίστοιχους πλάγιους.",
            "Η διάκριση αυτή επηρέασε τόσο τη βυζαντινή όσο και τη δυτική μεσαιωνική θεωρία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CF%8C%CF%80%CE%BF%CF%82_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["modes", "music-theory", "medieval", "gregorian-chant"]
    },
    {
        "id": "music_hard_329",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Johann Sebastian Bach περιλαμβάνει 14 κανόνες και 4 φούγκες πάνω σε ένα μοναδικό θέμα σε ρε ελάσσονα, χωρίς καθορισμένη ενορχήστρωση;",
        "answers": ["Η Τέχνη της Φούγκας (Die Kunst der Fuge)", "Το Καλοκουρδισμένο Κλειδοκύμβαλο", "Μουσική Προσφορά", "Παραλλαγές Γκόλντμπεργκ"],
        "correctAnswerIndex": 0,
        "explanation": "Η «Τέχνη της Φούγκας» (BWV 1080) αποτελεί την κορυφαία μελέτη αντίστιξης του Μπαχ, αποτελούμενη από Contrapuncti και κανόνες πάνω στο ίδιο βασικό μοτίβο.",
        "funFacts": [
            "Ο Μπαχ πέθανε πριν ολοκληρώσει την τελική τετραπλή φούγκα (Contrapunctus XIV), όπου εισήγαγε το μοτίβο B-A-C-H.",
            "Το έργο εκδόθηκε μετά θάνατον το 1751 σε ανοιχτή παρτιτούρα τεσσάρων πενταγράμμων."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CF%87%CE%B1%CE%BD_%CE%A3%CE%B5%CE%BC%CF%80%CE%AC%CF%83%CF%84%CE%B9%CE%B1%CE%BD_%CE%9C%CF%80%CE%B1%CF%87",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["bach", "fuga", "counterpoint", "baroque"]
    },
    {
        "id": "music_hard_330",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιες νότες απαρτίζουν το περίφημο μουσικό κρυπτόγραμμα «B-A-C-H» σύμφωνα με τη γερμανική ονοματολογία των φθόγγων;",
        "answers": ["Σι ύφεση - Λα - Ντο - Σι φυσικό", "Σι φυσικό - Λα - Ντο - Σι ύφεση", "Σι - Λα - Ντο - Σολ", "Σι - Λα - Μι - Σι"],
        "correctAnswerIndex": 0,
        "explanation": "Στη γερμανική μουσική ονοματολογία, το B είναι το Σι ύφεση (Bb) και το H είναι το Σι φυσικό (B natural). Έτσι το B-A-C-H αντιστοιχεί στις νότες Σιb - Λα - Ντο - Σι.",
        "funFacts": [
            "Πλήθος συνθετών (όπως οι Schumann, Liszt, Reger, Brahms και Webern) έγραψαν έργα βασισμένα στο θέμα BACH.",
            "Αποτελεί ένα χρωματικό μοτίβο εξαιρετικής αρμονικής πυκνότητας."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8C%CF%87%CE%B1%CE%BD_%CE%A3%CE%B5%CE%BC%CF%80%CE%AC%CF%83%CF%84%CE%B9%CE%B1%CE%BD_%CE%9C%CF%80%CE%B1%CF%87",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["bach", "cryptogram", "music-theory"]
    },
    {
        "id": "music_hard_331",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Έλληνας πιανίστας κέρδισε το 1962 το Α' Βραβείο στον διεθνή διαγωνισμό Tchaikovsky στη Μόσχα (εξ ημισείας με τον John Ogdon);",
        "answers": ["Βλαντίμιρ Ασκενάζι", "Δημήτρης Σγούρος", "Βασίλης Τσαμπρόπουλος", "Γιάννης Βακαρέλης"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Βλαντίμιρ Ασκενάζι μοιράστηκε το 1ο βραβείο με τον John Ogdon το 1962 (αν και ρωσικής καταγωγής, πολιτογραφήθηκε Ισλανδός).",
        "funFacts": [
            "Ο διαγωνισμός Τσαϊκόφσκι του 1962 ήταν ο δεύτερος στην ιστορία του θεσμού.",
            "Ο Ασκενάζι διηύθυνε αργότερα πολλές κορυφαίες ορχήστρες παγκοσμίως."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%BB%CE%B1%CE%BD%CF%84%CE%AF%CE%BC%CE%B9%CF%81_%CE%91%CF%83%CE%BA%CE%B5%CE%BD%CE%AC%CE%B6%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["piano", "competitions", "tchaikovsky"]
    },
    {
        "id": "music_hard_332",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Igor Stravinsky (1920), βασισμένο σε μουσικά αποσπάσματα αποδιδόμενα στον Pergolesi, εγκαινίασε την νεοκλασική του περίοδο;",
        "answers": ["Πουλτσινέλα (Pulcinella)", "Απόλλων Μουσηγέτης", "Το Παιχνίδι των Χαρτιών", "Ορφέας"],
        "correctAnswerIndex": 0,
        "explanation": "Το μπαλέτο «Πουλτσινέλα» (1920) σε ανάθεση του Σεργκέι Ντιαγκίλεφ σηματοδότησε την αποφασιστική στροφή του Στραβίνσκι προς τον νεοκλασικισμό.",
        "funFacts": [
            "Τα σκηνικά και τα κοστούμια της πρώτης παράστασης στο Παρίσι σχεδίασε ο Πάμπλο Πικάσο.",
            "Πολλά από τα κομμάτια που τότε θεωρούνταν του Περγκολέζι ανήκουν στην πραγματικότητα σε συνθέτες όπως ο Gallo και ο Wassenaer."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%99%CE%B3%CE%BA%CF%8C%CF%81_%CE%A3%CF%84%CF%81%CE%B1%CE%B2%CE%AF%CE%BD%CF%83%CE%BA%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["stravinsky", "neoclassicism", "ballet", "pergolesi"]
    },
    {
        "id": "music_hard_333",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στη μουσική ακουστική, πώς ονομάζεται το μικροσκοπικό ακουστικό διάστημα κατά το οποίο δώδεκα καθαρές πέμπτες υπερβαίνουν επτά καθαρές οκτάβες;",
        "answers": ["Πυθαγόρειο κόμμα (Pythagorean comma)", "Συντονικό κόμμα (Didymean comma)", "Δίεση (Diesis)", "Σχίσμα"],
        "correctAnswerIndex": 0,
        "explanation": "Το Πυθαγόρειο κόμμα ισούται με την αναλογία (3/2)^12 / 2^7 = 531441 / 524288, δηλαδή περίπου 23,46 cents, καθιστώντας αδύνατο το κλείσιμο του κύκλου των πεμπτών σε καθαρό κούρδισμα.",
        "funFacts": [
            "Αυτή η διαφορά οδήγησε στην εφεύρεση των συστημάτων συγκερασμού, με αποκορύφωμα το ισοσυγκερασμένο σύστημα (Equal Temperament).",
            "Το συντονικό κόμμα αντίθετα είναι η διαφορά μεταξύ τεσσάρων πεμπτών και δύο οκτάβων συν μιας φυσικής μεγάλης τρίτης (περίπου 21,51 cents)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8C%CE%BC%CE%BC%CE%B1_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["acoustics", "temperament", "pythagorean-comma", "intervals"]
    },
    {
        "id": "music_hard_334",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είδος μεσαιωνικού πολυφωνικού τραγουδιού του 14ου αιώνα (Ars Nova) περιλαμβάνει συνήθως δύο φωνές σε αυστηρό κανόνα και μία ελεύθερη οργανική γραμμή τενόρου;",
        "answers": ["Caccia", "Madrigal", "Ballata", "Rondeau"],
        "correctAnswerIndex": 0,
        "explanation": "Η Caccia (κυνήγι) στην ιταλική Ars Nova περιγράφει σκηνές κυνηγιού ή υπαίθρου με δύο φωνές που «κυνηγούν» η μία την άλλη σε κανονική μίμηση πάνω από έναν ανεξάρτητο οργανικό τενόρο.",
        "funFacts": [
            "Ονομάστηκε έτσι τόσο λόγω της θεματολογίας (κυνήγι) όσο και λόγω της μουσικής μορφής του κανόνα.",
            "Κορυφαίος συνθέτης του είδους ήταν ο τυφλός οργανίστας Francesco Landini."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB%CF%85%CF%86%CF%89%CE%BD%CE%AF%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["medieval", "ars-nova", "caccia", "counterpoint"]
    },
    {
        "id": "music_hard_335",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στη θεωρία της τζαζ αρμονίας, ποια τεχνική αντικατάστασης αλλάζει μια δεσπόζουσα συγχορδία 7ης με μια άλλη συγχορδία 7ης που βρίσκεται ένα τρίτονο μακριά;",
        "answers": ["Αντικατάσταση τριτόνου (Tritone substitution)", "Αντικατάσταση Coltrane", "Πλαγία πτώση", "Δευτερεύουσα δεσπόζουσα"],
        "correctAnswerIndex": 0,
        "explanation": "Η αντικατάσταση τριτόνου (subV) λειτουργεί επειδή οι δύο συγχορδίες (π.χ. G7 και Db7) μοιράζονται τον ίδιο ακριβώς οδηγό φθόγγο (tritone: F και B/Cb), επιτρέποντας χρωματική πτωτική κίνηση προς την τονική.",
        "funFacts": [
            "Είναι θεμελιώδες στοιχείο του ιδιώματος Bebop και Hard Bop.",
            "Στο μπάσο δημιουργεί ομαλό κατιόν ημιτονιακό βηματισμό (Db -> C αντί για G -> C)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%B1%CE%B6",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["jazz-harmony", "tritone-sub", "chords"]
    },
    {
        "id": "music_hard_336",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου κύκλου συγχορδιών που επινόησε ο John Coltrane στο κομμάτι «Giant Steps» (1960), βασισμένου σε συμμετρική διαίρεση της οκτάβας σε μείζονες τρίτες;",
        "answers": ["Coltrane changes", "Bird blues", "Rhythm changes", "Backdoor progression"],
        "correctAnswerIndex": 0,
        "explanation": "Οι «αλλαγές του Coltrane» (Coltrane changes) κινούνται γρήγορα ανάμεσα σε τρία τονικά κέντρα που απέχουν μεταξύ τους κατά διάστημα μεγάλης τρίτης (π.χ. B - G - Eb), σχηματίζοντας ισόπλευρο τρίγωνο στον κύκλο των πεμπτών.",
        "funFacts": [
            "Το σόλο στο «Giant Steps» θεωρείται από τα πιο απαιτητικά τεχνικά τεστ για κάθε μουσικό της τζαζ.",
            "Ο πιανίστας Tommy Flanagan δυσκολεύτηκε εμφανώς κατά την αρχική ιστορική ηχογράφηση του κομματιού."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%9A%CE%BF%CE%BB%CF%84%CF%81%CE%AD%CE%B9%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["jazz", "coltrane", "harmony", "improvisation"]
    },
    {
        "id": "music_hard_337",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Alban Berg (1935) αφιερώθηκε «στη μνήμη ενός αγγέλου» (Manon Gropius) και ενσωματώνει ένα κοράλ του J.S. Bach στη δωδεκάφθογγη δομή του;",
        "answers": ["Κοντσέρτο για βιολί", "Σουίτα Λυρική", "Wozzeck", "Lulu"],
        "correctAnswerIndex": 0,
        "explanation": "Το Κοντσέρτο για βιολί του Alban Berg γράφτηκε μετά τον θάνατο της 18χρονης κόρης της Alma Mahler και του Walter Gropius, ενσωματώνοντας το μπαχικό κοράλ «Es ist genug!» στο φινάλε.",
        "funFacts": [
            "Η δωδεκάφθογγη σειρά του έργου περιέχει μείζονες και ελάσσονες τριάδες, γεφυρώνοντας τονικότητα και σειραϊσμό.",
            "Ήταν το τελευταίο ολοκληρωμένο έργο του Μπεργκ πριν από τον πρόωρο θάνατό του."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BB%CE%BC%CF%80%CE%B1%CE%BD_%CE%9C%CF%80%CE%B5%CF%81%CE%B3%CE%BA",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["berg", "violin-concerto", "twelve-tone", "second-viennese-school"]
    },
    {
        "id": "music_hard_338",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στην παραδοσιακή ελληνική δημοτική μουσική, τι είναι ο «σκάρος»;",
        "answers": ["Ελεύθερος ποιμενικός οργανικός σκοπός χωρίς αυστηρό μέτρο που παιζόταν κατά τη νυχτερινή βοσκή των κοπαδιών", "Γρήγορος αντικριστός γαμήλιος χορός της Θράκης", "Νεκρικό μοιρολόι που τραγουδιέται αποκλειστικά από γυναίκες στη Μάνη", "Τελετουργικός χορός του κλήδονα στα νησιά"],
        "correctAnswerIndex": 0,
        "explanation": "Ο σκάρος είναι ηπειρώτικος ή ρουμελιώτικος αυτοσχεδιαστικός ποιμενικός σκοπός του κλαρίνου ή της φλογέρας, συνδεδεμένος με το νυχτερινό ξενύχτι και τη βοσκή (σκάρισμα) των προβάτων.",
        "funFacts": [
            "Μιμείται τους ήχους της φύσης, τα κουδούνια των κοπαδιών και το θρόισμα των φύλλων.",
            "Κορυφαίοι δεξιοτέχνες όπως ο Τάσος Χαλκιάς και ο Βασίλης Σαλέας ανέδειξαν τον σκάρο σε υψηλή τέχνη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%97%CF%80%CE%B5%CE%B9%CF%81%CF%8E%CF%84%CE%B9%CE%BA%CE%B7_%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE_%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%BF%CF%83%CE%B7",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["folk-music", "epirus", "clarinet", "tradition"]
    },
    {
        "id": "music_hard_339",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το ιδιαίτερο δομικό χαρακτηριστικό της νησιωτικής «τσαμπούνας» σε σύγκριση με τη θρακιώτικη ή μακεδονική «γκάιντα»;",
        "answers": ["Η τσαμπούνα έχει δύο παράλληλους αυλούς στο επιστόμιο (χωρίς ξεχωριστό ισοκράτη-μπάσο μπουριά)", "Η τσαμπούνα έχει μεταλλικό ασκό αντί για δέρμα κατσίκας", "Η τσαμπούνα δεν διαθέτει τρύπες στα δάχτυλα", "Η τσαμπούνα παίζεται αποκλειστικά με φυσούνες ποδιού"],
        "correctAnswerIndex": 0,
        "explanation": "Στην τσαμπούνα του Αιγαίου, ο αυλός αποτελείται από δύο καλάμια τοποθετημένα δίπλα-δίπλα στην ίδια ξύλινη βάση, χωρίς να υπάρχει το μακρύ ξεχωριστό μπάσο ισοκράτημα (μπουριά/τρομπέτα) της ηπειρωτικής γκάιντας.",
        "funFacts": [
            "Ο ένας αυλός μπορεί να παίζει μελωδία ενώ ο δεύτερος κρατά ισοκράτημα ή παίζουν ταυτόχρονα σε διφωνία.",
            "Είναι ένα από τα αρχαιότερα πνευστά όργανα που επιβιώνουν αδιάλειπτα στις Κυκλάδες και τα Δωδεκάνησα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%83%CE%B1%CE%BC%CF%80%CE%BF%CF%8D%CE%BD%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["tsambouna", "instruments", "greek-folk", "aegean"]
    },
    {
        "id": "music_hard_340",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το παραδοσιακό κούρδισμα των τεσσάρων χορδών της ποντιακής λύρας (κεμετζέ) από την ψηλότερη προς τη χαμηλότερη φωνή;",
        "answers": ["Κούρδισμα σε καθαρές τέταρτες", "Κούρδισμα σε καθαρές πέμπτες", "Κούρδισμα σε μείζονες τρίτες", "Κούρδισμα σε οκτάβες"],
        "correctAnswerIndex": 0,
        "explanation": "Η ποντιακή λύρα είναι τρίχορδη και κουρδίζεται παραδοσιακά σε καθαρές τέταρτες (π.χ. Σι - Μι - Λα), σε αντίθεση με το βιολί και την κρητική λύρα που κουρδίζονται σε πέμπτες.",
        "funFacts": [
            "Το παίξιμο γίνεται συχνά πιέζοντας δύο χορδές ταυτόχρονα, παράγοντας χαρακτηριστική παράλληλη τεταρτοφωνία.",
            "Οι χορδές πιέζονται με το νύχι ή την ψίχα του δακτύλου από το πλάι."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BD%CF%84%CE%B9%CE%B1%CE%BA%CE%AE_%CE%BB%CF%8D%CF%81%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pontic-lyra", "instruments", "tuning", "pontus"]
    },
    {
        "id": "music_hard_341",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το θεμελιώδες χαρακτηριστικό του «γαλλικού ανοίγματος» (French Overture) που καθιέρωσε ο Jean-Baptiste Lully στην αυλή του Λουδοβίκου ΙΔ΄;",
        "answers": ["Ένα αργό πρώτο μέρος με έντονα παρεστιγμένους ρυθμούς που ακολουθείται από ένα γρήγορο φουγκάτο μέρος", "Ένα γρήγορο βιρτουόζικο allegro ακολουθούμενο από adagio", "Μια σειρά από άσχετους μεταξύ τους λαϊκούς χορούς", "Ένα σόλο τσέμπαλου χωρίς συνοδεία ορχήστρας"],
        "correctAnswerIndex": 0,
        "explanation": "Η γαλλική εισαγωγή διακρίνεται από τη διμερή της δομή: ένα μεγαλοπρεπές αργό τμήμα με παρεστιγμένους ρυθμούς (dotted rhythms) και ένα ζωηρό αντιστικτικό (μιμητικό/φουγκάτο) γρήγορο τμήμα.",
        "funFacts": [
            "Ο Lully την καθιέρωσε ως εισαγωγή στις τραγωδίες με μουσική (tragédies en musique).",
            "Ο J.S. Bach χρησιμοποίησε τη φόρμα στις Ορχηστρικές Σουίτες του και στις Παραλλαγές Γκόλντμπεργκ (παραλλαγή 16)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B1%CE%BD-%CE%9C%CF%80%CE%B1%CF%84%CE%AF%CF%83%CF%84_%CE%9B%CF%85%CE%BB%CE%AF",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["baroque", "lully", "french-overture", "orchestral"]
    },
    {
        "id": "music_hard_342",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος Γάλλος συνθέτης και θεωρητικός δημοσίευσε το 1722 το θεμελιώδες «Traité de l'harmonie réduite à ses principes naturels», θεμελιώνοντας τη σύγχρονη θεωρία των συγχορδιών και των αναστροφών;",
        "answers": ["Jean-Philippe Rameau", "François Couperin", "Marc-Antoine Charpentier", "Marin Marais"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Ζαν-Φιλίπ Ραμώ θεμελίωσε με το έργο αυτό τη θεωρία της θεμελιώδους βάσης (basse fondamentale) και απέδειξε ότι μια συγχορδία διατηρεί την ταυτότητά της σε όλες τις αναστροφές της.",
        "funFacts": [
            "Ο Ραμώ υπήρξε ταυτόχρονα ένας από τους κορυφαίους συνθέτες όπερας της εποχής του (π.χ. «Ιππόλυτος και Αρικία»).",
            "Η θεωρία του προκάλεσε έντονες φιλοσοφικές διαμάχες με τους Εγκυκλοπαιδιστές και τον Ζαν-Ζακ Ρουσσώ."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%96%CE%B1%CE%BD-%CE%A6%CE%B9%CE%BB%CE%AF%CF%80_%CE%A1%CE%B1%CE%BC%CF%8E",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["rameau", "harmony", "treatise", "baroque"]
    },
    {
        "id": "music_hard_343",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Γκιγιώμ ντε Μασώ (Guillaume de Machaut, περ. 1365) αποτελεί την παλαιότερη γνωστή πλήρη πολυφωνική λειτουργία που συντέθηκε εξ ολοκλήρου από έναν μόνο συνθέτη;",
        "answers": ["Messe de Nostre Dame", "Missa Tournai", "Missa L'homme armé", "Messe de Requiem"],
        "correctAnswerIndex": 0,
        "explanation": "Η «Messe de Nostre Dame» του Machaut αποτελείται από τα πέντε μέρη του Ordinarium (Kyrie, Gloria, Credo, Sanctus, Agnus Dei) και το Ite Missa Est, σε τετράφωνη ισορρυθμική πολυφωνία.",
        "funFacts": [
            "Μέχρι τότε, τα διάφορα μέρη της λειτουργίας συγκεντρώνονταν ανώνυμα από διάφορες πηγές.",
            "Συντέθηκε πιθανότατα για τον καθεδρικό ναό της Ρενς όπου ο Μασώ ήταν ιερέας και κανόνικος."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%B9%CE%B3%CE%B9%CF%8E%CE%BC_%CE%BD%CF%84%CE%B5_%CE%9C%CE%B1%CF%83%CF%8E",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["machaut", "ars-nova", "mass", "medieval"]
    },
    {
        "id": "music_hard_344",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στη μεσαιωνική ισορρυθμική τεχνική (isorhythm), πώς ονομάζεται η επαναλαμβανόμενη μελωδική ακολουθία φθόγγων και πώς το επαναλαμβανόμενο ρυθμικό μοτίβο;",
        "answers": ["Color η μελωδική ακολουθία και Talea το ρυθμικό μοτίβο", "Talea η μελωδική ακολουθία και Color το ρυθμικό μοτίβο", "Cantus firmus και Tenor", "Dux και Comes"],
        "correctAnswerIndex": 0,
        "explanation": "Στο ισορρυθμικό μοτέτο, η Talea είναι το σταθερό ρυθμικό σχήμα (σειρά αξιών) και το Color είναι η μελωδική σειρά φθόγγων. Όταν οι διάρκειες Talea και Color δεν συμπίπτουν αριθμητικά, δημιουργούνται σύνθετες παραλλαγές.",
        "funFacts": [
            "Ο όρος συστηματοποιήθηκε από τους θεωρητικούς της Ars Nova όπως ο Philippe de Vitry.",
            "Αυτή η τεχνική θεωρείται πρόδρομος των σειραϊκών διαδικασιών του 20ού αιώνα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CE%BB%CF%85%CF%86%CF%89%CE%BD%CE%AF%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["isorhythm", "medieval", "music-theory", "ars-nova"]
    },
    {
        "id": "music_hard_345",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα της ιταλικής αυλικής πολυφωνικής φόρμας του 16ου αιώνα, πρόδρομου του μαδριγαλιού, που χαρακτηριζόταν από απλή συλλαβική και ομοφωνική υφή;",
        "answers": ["Frottola", "Canzona", "Ricercar", "Villanella"],
        "correctAnswerIndex": 0,
        "explanation": "Η Frottola άκμασε στη Μάντοβα και τη βόρεια Ιταλία στα τέλη του 15ου και αρχές 16ου αιώνα, με την ανώτερη φωνή να τραγουδά συλλαβικά και τις υπόλοιπες να συνοδεύουν συχνά με λαούτο.",
        "funFacts": [
            "Η Ισαβέλλα των Έστε (Isabella d'Este) υπήρξε η σημαντικότερη προστάτιδα της frottola.",
            "Από την εξέλιξη και την εκλέπτυνση της frottola γεννήθηκε το αναγεννησιακό μαδριγάλι."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CE%B4%CF%81%CE%B9%CE%B3%CE%AC%CE%BB%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["renaissance", "frottola", "secular-music", "italy"]
    },
    {
        "id": "music_hard_346",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο οπερατικό έργο του Claudio Monteverdi (1642) θεωρείται το τελευταίο του αριστούργημα και πραγματεύεται την άνοδο μιας φιλόδοξης εταίρας στον αυτοκρατορικό θρόνο της Ρώμης;",
        "answers": ["Η Στέψη της Ποππαίας (L'incoronazione di Poppea)", "Ορφέας (L'Orfeo)", "Η Επιστροφή του Οδυσσέα στην Πατρίδα", "Η Αριάδνη"],
        "correctAnswerIndex": 0,
        "explanation": "Το «L'incoronazione di Poppea» παρουσιάστηκε στη Βενετία το 1642 και διακρίνεται για τον ρεαλισμό, την ψυχολογική διείσδυση και το περίφημο τελικό ντουέτο «Pur ti miro».",
        "funFacts": [
            "Είναι μία από τις πρώτες όπερες στην ιστορία που βασίστηκε σε ιστορικά πρόσωπα και όχι στη μυθολογία.",
            "Ο ρόλος του Νέρωνα γράφτηκε αρχικά για καστράτο σοπράνο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%BB%CE%AC%CE%BF%CF%85%CE%BD%CF%84%CE%B9%CE%BF_%CE%9C%CE%BF%CE%BD%CF%84%CE%B5%CE%B2%CE%AD%CF%81%CE%BD%CF%84%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["monteverdi", "opera", "baroque", "poppea"]
    },
    {
        "id": "music_hard_347",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του Ludwig van Beethoven (έργο 133) γράφτηκε αρχικά ως το φινάλε του Κουαρτέτου Εγχόρδων αρ. 13 (έργο 130), αλλά αποσπάστηκε λόγω της τεράστιας δυσκολίας του;",
        "answers": ["Μεγάλη Φούγκα (Große Fuge)", "Φαντασία για πιάνο, χορωδία και ορχήστρα", "Missa Solemnis", "Σονάτα Hammerklavier"],
        "correctAnswerIndex": 0,
        "explanation": "Η «Große Fuge» σε σι ύφεση μείζονα ήταν τόσο απαιτητική και ριζοσπαστική για την εποχή της, που ο εκδότης Artaria έπεισε τον Μπετόβεν να γράψει νέο φινάλε και να την εκδώσει χωριστά ως έργο 133.",
        "funFacts": [
            "Ο Ιγκόρ Στραβίνσκι δήλωσε ότι η Μεγάλη Φούγκα παραμένει «ένα απολύτως σύγχρονο κομμάτι μουσικής που θα είναι σύγχρονο για πάντα».",
            "Η πρεμιέρα της έγινε το 1826 από το κουαρτέτο Schuppanzigh."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CF%8D%CE%BD%CF%84%CE%B2%CE%B9%CF%87_%CE%B2%CE%B1%CE%BD_%CE%9C%CF%80%CE%B5%CF%84%CF%8C%CE%B2%CE%B5%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["beethoven", "string-quartet", "grosse-fuge", "counterpoint"]
    },
    {
        "id": "music_hard_348",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος κορυφαίος Ούγγρος συνθέτης και πιανίστας ανέπτυξε το «σύστημα των αξόνων» (axis system) στην αρμονική ανάλυση των έργων του, όπως περιέγραψε ο Ernő Lendvai;",
        "answers": ["Béla Bartók", "Zoltán Kodály", "Franz Liszt", "György Ligeti"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Béla Bartók οργάνωσε την αρμονία του γύρω από άξονες τονικοτήτων που συνδέονται με διαστήματα τρίτονων και ελάσσονων τρίτων, αντικαθιστώντας τη συμβατική διατονική ιεραρχία.",
        "funFacts": [
            "Ο Lendvai υποστήριξε ότι ο Bartók δόμησε επίσης τις μορφές του πάνω στη χρυσή τομή και την ακολουθία Fibonacci.",
            "Το «Κοντσέρτο για Ορχήστρα» και η «Μουσική για έγχορδα, κρουστά και τσελέστα» αποτελούν υποδειγματικά παραδείγματα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%AD%CE%BB%CE%B1_%CE%9C%CF%80%CE%AC%CF%81%CF%84%CE%BF%CE%BA",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["bartok", "music-theory", "axis-system", "20th-century"]
    },
    {
        "id": "music_hard_349",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο έργο του György Ligeti (1961) για μεγάλη ορχήστρα καθιέρωσε την τεχνική του «μικροπολυφωνισμού» (micropolyphony) και χρησιμοποιήθηκε στην ταινία «2001: A Space Odyssey»;",
        "answers": ["Atmosphères", "Lontano", "Apparitions", "Requiem"],
        "correctAnswerIndex": 0,
        "explanation": "Το «Atmosphères» καταργεί την παραδοσιακή μελωδία και τον ρυθμό υπέρ πυκνών ηχητικών μαζών και ηχοχρωμάτων, όπου δεκάδες όργανα κινούνται σε εξαιρετικά στενούς κανόνες μικροπολυφωνίας.",
        "funFacts": [
            "Ο Stanley Kubrick χρησιμοποίησε το κομμάτι χωρίς την αρχική άδεια του συνθέτη, οδηγώντας σε δικαστικό συμβιβασμό.",
            "Στην παρτιτούρα δεν υπάρχει ούτε μία συμβατική συγχορδία ή μελωδικό θέμα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%BA%CE%B9%CE%AD%CF%81%CE%B3%CE%BA%CE%B9_%CE%9B%CE%AF%CE%B3%CE%BA%CE%B5%CF%84%CE%B9",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["ligeti", "avant-garde", "micropolyphony", "sound-mass"]
    },
    {
        "id": "music_hard_350",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο όνομα φέρει η πρωτοποριακή σύνθεση του John Cage (1951) για 12 ραδιοφωνικούς δέκτες και 24 εκτελεστές;",
        "answers": ["Imaginary Landscape No. 4", "Music of Changes", "Cartridge Music", "Variations I"],
        "correctAnswerIndex": 0,
        "explanation": "Το «Imaginary Landscape No. 4» χρησιμοποιεί 12 ραδιόφωνα όπου δύο εκτελεστές ανά ραδιόφωνο χειρίζονται τις συχνότητες και την ένταση ακολουθώντας παρτιτούρα παραγμένη μέσω του I Ching.",
        "funFacts": [
            "Το ηχητικό αποτέλεσμα εξαρτάται πλήρως από το τι εκπέμπεται στα ραδιοκύματα κατά τη στιγμή της συναυλίας.",
            "Στην πρεμιέρα στη Νέα Υόρκη, επειδή ήταν αργά τη νύχτα, πολλοί σταθμοί είχαν κλείσει με αποτέλεσμα το έργο να αποτελείται κυρίως από παράσιτα και σιωπή."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%BD_%CE%9A%CE%AD%CE%B9%CF%84%CE%B6",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["cage", "aleatoric", "avant-garde", "electronic-music"]
    },
    {
        "id": "music_hard_351",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια είναι η ακριβής ονομασία της κλίμακας του 4ου εκκλησιαστικού τρόπου (Υποφρύγιος) με τελική (finalis) τη νότα Μι;",
        "answers": ["Υποφρύγιος τρόπος", "Δώριος τρόπος", "Λύδιος τρόπος", "Μιξολύδιος τρόπος"],
        "correctAnswerIndex": 0,
        "explanation": "Ο 4ος τρόπος (Hypophrygian) έχει finalis το Μι, ambitus από Σι κάτω από το Μι έως Ντο πάνω, και δεσπόζουσα (repercussio) τη νότα Λα.",
        "funFacts": [
            "Στο οκτωηχικό σύστημα αντιστοιχεί στον 4ο τρόπο (πλάγιο του δευτέρου κατά το δυτικό σύστημα).",
            "Η απουσία καθαρής 5ης πάνω από τη χαμηλότερη υποκείμενη νότα προσδίδει στον τρόπο ιδιαίτερο μυστικιστικό ηχόχρωμα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CF%8C%CF%80%CE%BF%CF%82_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["church-modes", "gregorian", "music-theory"]
    },
    {
        "id": "music_hard_352",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Στην αρμονία της κλασικής περιόδου, πώς ονομάζεται η αυξημένη έκτη συγχορδία που περιέχει, εκτός από τη θεμέλιο και τη μεγάλη τρίτη, αυξημένη τέταρτη (π.χ. Ab - C - D - F#);",
        "answers": ["Γαλλική έκτη", "Ιταλική έκτη", "Γερμανική έκτη", "Νεαπολιτάνικη έκτη"],
        "correctAnswerIndex": 0,
        "explanation": "Η Γαλλική αυξημένη έκτη περιέχει τις νότες 1, 3, #4 και #6 (π.χ. Ab-C-D-F# στην ντο μείζονα/ελάσσονα), διαθέτοντας χαρακτηριστικό άκουσμα λόγω του εμπεριεχόμενου τριτόνου.",
        "funFacts": [
            "Η Ιταλική έκτη περιέχει μόνο 3 φθόγγους (Ab-C-F#), ενώ η Γερμανική περιέχει καθαρή πέμπτη (Ab-C-Eb-F#).",
            "Όλες οι αυξημένες έκτες λύνονται συνήθως στην καθαρή οκτάβα της δεσπόζουσας (G-G)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%B3%CF%87%CE%BF%CF%81%CE%B4%CE%AF%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["harmony", "augmented-sixth", "chords", "music-theory"]
    },
    {
        "id": "music_hard_353",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποια είναι η δομή της Νεαπολιτάνικης συγχορδίας (Neapolitan chord) στην κλασική αρμονία;",
        "answers": ["Μείζονα συγχορδία στην ελαττωμένη δεύτερη βαθμίδα (bII), συνήθως σε πρώτη αναστροφή (bII6)", "Ελαττωμένη συγχορδία στην έβδομη βαθμίδα", "Αυξημένη συγχορδία στην τρίτη βαθμίδα", "Μείζονα συγχορδία στην τέταρτη βαθμίδα με πρόσθετη έκτη"],
        "correctAnswerIndex": 0,
        "explanation": "Η Νεαπολιτάνικη συγχορδία (N6) είναι μια μείζονα συγχορδία χτισμένη πάνω στη χαμηλωμένη δεύτερη βαθμίδα (π.χ. Db-F-Ab στην ντο ελάσσονα) και χρησιμοποιείται κατά κανόνα σε πρώτη αναστροφή ως υποδεσπόζουσα.",
        "funFacts": [
            "Πήρε το όνομά της από τη σχολή όπερας της Νάπολης του 18ου αιώνα (Scarlatti κ.ά.).",
            "Χρησιμοποιήθηκε εκτεταμένα από τον Μπετόβεν, όπως στην έναρξη της Σονάτας του Σεληνόφωτος και της Σονάτας Appassionata."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%85%CE%B3%CF%87%CE%BF%CF%81%CE%B4%CE%AF%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["harmony", "neapolitan-chord", "chords", "music-theory"]
    },
    {
        "id": "music_hard_354",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το θεμελιώδες χαρακτηριστικό της τεχνικής «Klangfarbenmelodie» (μελωδία ηχοχρωμάτων) που εισήγαγε ο Arnold Schoenberg;",
        "answers": ["Η διανομή των φθόγγων μιας μελωδικής γραμμής σε διαδοχικά διαφορετικά όργανα, ώστε το ηχόχρωμα να αποτελεί πρωτεύον δομικό στοιχείο", "Η ταυτόχρονη εκτέλεση της μελωδίας από όλα τα χάλκινα πνευστά", "Η χρήση προηχογραφημένων φυσικών ήχων αντί για μουσικά όργανα", "Η αλλαγή του κουρδίσματος των εγχόρδων κατά τη διάρκεια της εκτέλεσης"],
        "correctAnswerIndex": 0,
        "explanation": "Στην Klangfarbenmelodie, η μελωδική ροή δεν ορίζεται μόνο από τα τονικά ύψη αλλά από τη συνεχή εναλλαγή ηχοχρωμάτων μεταξύ διαφόρων οργάνων (όπως στο 3ο από τα 5 Ορχηστρικά Κομμάτια op. 16 του Schoenberg).",
        "funFacts": [
            "Ο Anton Webern εξέλιξε την τεχνική σε ακραίο σημείο στη δική του ενορχήστρωση του Ricercar από τη «Μουσική Προσφορά» του Bach.",
            "Αποτέλεσε τη βάση για τον μεταγενέστερο πουαντιγισμό (pointillism) στη μεταπολεμική μουσική."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%86%CF%81%CE%BD%CE%BF%CE%BB%CE%BD%CF%84_%CE%A3%CE%AD%CE%BD%CE%BC%CF%80%CE%B5%CF%81%CE%B3%CE%BA",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["schoenberg", "orchestration", "klangfarbenmelodie", "avant-garde"]
    },
    {
        "id": "music_hard_355",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο διάσημο έργο του Karlheinz Stockhausen (1955–1956) συνδυάζει ηχογραφημένη φωνή αγοριού που ψάλλει από το Βιβλίο του Δανιήλ με ηλεκτρονικά παραγόμενους ήχους σε πενταφωνική διάταξη;",
        "answers": ["Gesang der Jünglinge", "Kontakte", "Mantra", "Stimmung"],
        "correctAnswerIndex": 0,
        "explanation": "Το «Gesang der Jünglinge» (Το τραγούδι των παίδων εν καμίνω) αποτελεί ιστορικό ορόσημο, γεφυρώνοντας για πρώτη φορά τη γαλλική «musique concrète» με τη γερμανική «elektronische Musik».",
        "funFacts": [
            "Συντέθηκε στο στούντιο ηλεκτρονικής μουσικής της WDR στην Κολωνία.",
            "Ήταν το πρώτο σημαντικό έργο που αξιοποίησε τον χωρικό εντοπισμό του ήχου με περιφερειακά τοποθετημένα μεγάφωνα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%81%CE%BB%CF%87%CE%AC%CE%B9%CE%BD%CF%84%CF%82_%CE%A3%CF%84%CE%BF%CE%BA%CF%87%CE%AC%CE%BF%CF%85%CE%B6%CE%B5%CE%BD",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["stockhausen", "electronic-music", "avant-garde", "spatial-audio"]
    },
    {
        "id": "music_hard_356",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιος Έλληνας συνθέτης, μαθητής του Olivier Messiaen, έγραψε το εμβληματικό έργο «Αναρροές» (1962) και υπήρξε πρωτεργάτης του ελληνικού μουσικού μοντερνισμού;",
        "answers": ["Γιώργος Σισιλιάνος", "Νίκος Σκαλκώτας", "Δημήτρης Μητρόπουλος", "Μάνος Χατζιδάκις"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Γιώργος Σισιλιάνος (1920–2005) σπούδασε στο Παρίσι και τη Ρώμη και εισήγαγε σύγχρονες σειραϊκές και μετασειραϊκές τεχνικές στη μεταπολεμική ελληνική λόγια μουσική.",
        "funFacts": [
            "Υπήρξε γενικός γραμματέας και αντιπρόεδρος της Ένωσης Ελλήνων Μουσουργών.",
            "Τα έργα του εκτελέστηκαν από κορυφαίες ορχήστρες στην Ευρώπη και την Αμερική (όπως η Φιλαρμονική της Νέας Υόρκης υπό τον Μητρόπουλο)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CF%8E%CF%81%CE%B3%CE%BF%CF%82_%CE%A3%CE%B9%CF%83%CE%B9%CE%BB%CE%B9%CE%AC%CE%BD%CE%BF%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["greek-classical", "modernism", "serialism", "sicilianos"]
    },
    {
        "id": "music_hard_357",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του εκκλησιαστικού οργάνου χειρός της αρχαίας Ρώμης και του Βυζαντίου, που λειτουργούσε με πίεση νερού για τη σταθεροποίηση του αέρα;",
        "answers": ["Ύδραυλις", "Σάλπιγξ", "Πανδούρα", "Αυλός"],
        "correctAnswerIndex": 0,
        "explanation": "Η ύδραυλις (ύδραυλος) εφευρέθηκε στην Αλεξάνδρεια τον 3ο αιώνα π.Χ. από τον Κτησίβιο και αποτελεί τον άμεσο πρόγονο του εκκλησιαστικού οργάνου.",
        "funFacts": [
            "Το 1992 ανακαλύφθηκε στο Δίον της Πιερίας η αρχαιότερη σωζόμενη ύδραυλις στον κόσμο (1ου αι. π.Χ.).",
            "Στο Βυζάντιο η ύδραυλις παιζόταν στην αυτοκρατορική αυλή και στον Ιππόδρομο ως σύμβολο κύρους."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%8E%CE%B4%CF%81%CE%B1%CF%85%CE%BB%CE%B9%CF%82",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["hydraulis", "ancient-greece", "byzantine", "instruments"]
    },
    {
        "id": "music_hard_358",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο θεωρητικό έργο του Gioseffo Zarlino (1558) καθόρισε το σύστημα του φυσικού συγκερασμού (just intonation) και τη διαίρεση του senario (αριθμοί 1-6);",
        "answers": ["Le Istitutioni Harmoniche", "Dimostrationi harmoniche", "Dodecachordon", "Musica getutscht"],
        "correctAnswerIndex": 0,
        "explanation": "Στο μνημειώδες σύγγραμμα «Le Istitutioni Harmoniche» (1558), ο Τζοζέφο Τσαρλίνο νομιμοποίησε θεωρητικά τις μείζονες και ελάσσονες τρίτες ως τέλειες συμφωνίες βασισμένος στις μαθηματικές αναλογίες του senario.",
        "funFacts": [
            "Ο Zarlino υπήρξε maestro di cappella στον Άγιο Μάρκο της Βενετίας.",
            "Υπήρξε δάσκαλος κορυφαίων μορφών όπως ο Vincenzo Galilei και ο Claudio Merulo."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B6%CE%BF%CE%B6%CE%AD%CF%86%CE%BF_%CE%A4%CF%83%CE%B1%CF%81%CE%BB%CE%AF%CE%BD%CE%BF",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["zarlino", "renaissance", "music-theory", "just-intonation"]
    },
    {
        "id": "music_hard_359",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο ιστορικό βιβλίο του Ελβετού ουμανιστή Heinrich Glarean (Glareanus, 1547) επέκτεινε το παραδοσιακό σύστημα των 8 εκκλησιαστικών τρόπων σε 12, προσθέτοντας τον Ιώνιο και τον Αιολικό τρόπο;",
        "answers": ["Dodecachordon", "Micrologus", "Musica Enchiriadis", "Harmonie Universelle"],
        "correctAnswerIndex": 0,
        "explanation": "Στο «Dodecachordon» (1547), ο Glareanus αναγνώρισε επίσημα τους τρόπους με βάση το Ντο (Ιώνιος) και το Λα (Αιολικός), θέτοντας τις βάσεις για τη μετέπειτα μείζονα και ελάσσονα τονικότητα.",
        "funFacts": [
            "Ο τίτλος σημαίνει στα ελληνικά «όργανο με δώδεκα χορδές».",
            "Περιέχει αναλύσεις έργων κορυφαίων συνθετών της εποχής, ιδίως του Josquin des Prez."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CF%8C%CF%80%CE%BF%CF%82_(%CE%BC%CE%BF%CF%85%CF%83%CE%B9%CE%BA%CE%AE)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["modes", "glareanus", "dodecachordon", "renaissance"]
    },
    {
        "id": "music_hard_360",
        "categoryId": "music",
        "difficulty": 5,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα της τεχνικής εκτέλεσης στα έγχορδα κατά την οποία ο εκτελεστής χτυπά τις χορδές με το ξύλο του δοξαριού αντί για τις τρίχες;",
        "answers": ["Col legno", "Sul ponticello", "Sul tasto", "Flautando"],
        "correctAnswerIndex": 0,
        "explanation": "Η οδηγία «col legno battuto» προστάζει το χτύπημα των χορδών με το ξύλινο στέλεχος του δοξαριού, παράγοντας έναν ξηρό, κρουστό και απόκοσμο ήχο.",
        "funFacts": [
            "Διάσημη χρήση γίνεται στο «Όνειρο μιας νύχτας Σαββάτου» της Φανταστικής Συμφωνίας του Berlioz και στον «Άρη» του Gustav Holst.",
            "Υπάρχει επίσης η τεχνική «col legno tratto» όπου το ξύλο σύρεται πάνω στη χορδή."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%88%CE%B3%CF%87%CE%BF%CF%81%CE%B4%CE%B1",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["strings", "extended-techniques", "orchestration", "col-legno"]
    }
]

if __name__ == "__main__":
    target_file = os.path.join(
        os.path.dirname(__file__), "..", "..", "content", "questions", "el-GR", "music_hard.json"
    )
    print(f"Loaded {len(QUESTIONS)} questions for music_hard batch 3.")
    validate_and_append("music", "hard", 5, QUESTIONS)

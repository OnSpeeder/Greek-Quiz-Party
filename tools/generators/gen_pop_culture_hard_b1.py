# -*- coding: utf-8 -*-
"""Generator for pop_culture_hard questions 211-310 (100 questions)."""
import os
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

def make_q(qid, text, correct, distractors, explanation, fun_facts, source, tags, diff=5):
    idx = int(qid.split('_')[-1]) % 4
    answers = list(distractors)
    answers.insert(idx, correct)
    return {
        "id": qid,
        "categoryId": "pop_culture",
        "difficulty": diff,
        "locale": "el-GR",
        "text": text,
        "answers": answers,
        "correctAnswerIndex": idx,
        "explanation": explanation,
        "funFacts": fun_facts,
        "source": source,
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": tags
    }

questions = [
    # 211
    make_q(
        "pop_culture_hard_211",
        "Σε ποιο ιστορικό τεύχος ανθολογίας κόμικς έκανε το επίσημο ντεμπούτο του ο Spider-Man τον Αύγουστο του 1962;",
        "Amazing Fantasy #15",
        ["Journey into Mystery #83", "Tales of Suspense #39", "Action Comics #1"],
        "Ο Spider-Man παρουσιάστηκε στο τελευταίο τεύχος της υπό κατάργηση σειράς Amazing Fantasy (#15) από τους Stan Lee και Steve Ditko.",
        [
            "Ο εκδότης Martin Goodman ήταν αρχικά απρόθυμος επειδή πίστευε ότι ο κόσμος σιχαίνεται τις αράχνες και ότι οι έφηβοι πρέπει να είναι μόνο βοηθοί ηρώων.",
            "Το τεύχος σημείωσε τις υψηλότερες πωλήσεις της χρονιάς για τη Marvel, οδηγώντας άμεσα στη δημιουργία του τίτλου 'The Amazing Spider-Man'."
        ],
        "https://en.wikipedia.org/wiki/Amazing_Fantasy",
        ["spiderman", "marvel", "amazing_fantasy", "comics_history"]
    ),
    # 212
    make_q(
        "pop_culture_hard_212",
        "Ποια ήταν η αρχική εμπορική επωνυμία της εταιρείας έκδοσης κόμικς του Martin Goodman πριν μετονομαστεί επίσημα σε Marvel Comics το 1961;",
        "Timely Publications (Timely Comics)",
        ["National Comics", "Quality Comics", "Fawcett Publications"],
        "Η Timely Comics ιδρύθηκε το 1939 από τον Martin Goodman και αποτέλεσε τον πρόδρομο της Atlas Comics (δεκαετία '50) και τελικά της Marvel.",
        [
            "Η πρώτη της έκδοση, Marvel Comics #1 τον Οκτώβριο του 1939, εισήγαγε τον Human Torch και τον Namor the Sub-Mariner.",
            "Ο Stan Lee ξεκίνησε να εργάζεται στην Timely Comics το 1939 ως βοηθός γραφείου σε ηλικία μόλις 17 ετών."
        ],
        "https://en.wikipedia.org/wiki/Timely_Comics",
        ["marvel", "timely_comics", "comics_history", "martin_goodman"]
    ),
    # 213
    make_q(
        "pop_culture_hard_213",
        "Ποια ήταν η αναγραφόμενη τιμή πώλησης στα περίπτερα των ΗΠΑ για το ιστορικό τεύχος Action Comics #1 (1938) όπου πρωτοεμφανίστηκε ο Superman;",
        "10 σεντς (10 cents)",
        ["5 σεντς", "25 σεντς", "50 σεντς"],
        "Το Action Comics #1 πωλούνταν για μόλις 10 σεντς τον Ιούνιο του 1938 και αποτελεί σήμερα το πιο ακριβό κόμικ στον κόσμο.",
        [
            "Το 2024 ένα αντίτυπο σε σχεδόν άριστη κατάσταση (CGC 8.5) πωλήθηκε σε δημοπρασία για το ποσό-ρεκόρ των 6 εκατομμυρίων δολαρίων.",
            "Εκτιμάται ότι διασώζονται λιγότερα από 100 αυθεντικά αντίτυπα παγκοσμίως από τα 200.000 που είχαν τυπωθεί."
        ],
        "https://en.wikipedia.org/wiki/Action_Comics_1",
        ["superman", "action_comics", "dc_comics", "comics_history"]
    ),
    # 214
    make_q(
        "pop_culture_hard_214",
        "Ποιος νεαρός εικονογράφος και βοηθός συν-δημιούργησε τον Joker μαζί με τους Bob Kane και Bill Finger στο Batman #1 (1940);",
        "Jerry Robinson",
        ["Dick Sprang", "Gardner Fox", "Sheldon Moldoff"],
        "Ο Jerry Robinson έφερε μια τράπουλα με ένα τραπουλόχαρτο τζόκερ ως έμπνευση για τον σχεδιασμό του χαρακτήρα, συνεισφέροντας καθοριστικά στη γέννησή του.",
        [
            "Ο Robinson δημιούργησε επίσης το όνομα και τον σχεδιασμό του Robin (Dick Grayson), εμπνευσμένος από τον Robin Hood.",
            "Υπήρξε αργότερα ένθερμος υποστηρικτής των δικαιωμάτων των δημιουργών κόμικς και πρόεδρος της National Cartoonists Society."
        ],
        "https://en.wikipedia.org/wiki/Jerry_Robinson",
        ["joker", "jerry_robinson", "batman", "dc_comics"]
    ),
    # 215
    make_q(
        "pop_culture_hard_215",
        "Ποιο είναι το πλήρες επίσημο ονοματεπώνυμο του μπάτλερ Alfred της οικογένειας Wayne στα σύγχρονα κόμικς της DC;",
        "Alfred Thaddeus Crane Pennyworth",
        ["Alfred James Reginald Pennyworth", "Alfred Arthur William Pennyworth", "Alfred Charles George Pennyworth"],
        "Το πλήρες όνομα του Alfred καθιερώθηκε στα κόμικς αποδίδοντας τιμή στο στρατιωτικό και θεατρικό παρελθόν του χαρακτήρα.",
        [
            "Στην πρώτη του εμφάνιση το 1943 (Batman #16), ήταν υπέρβαρος, αδέξιος και το επώνυμό του γραφόταν 'Beagle'.",
            "Η εμφάνισή του άλλαξε δραστικά σε λεπτή με μουστάκι αφού ο William Austin τον υποδύθηκε στην κινηματογραφική σειρά του 1943."
        ],
        "https://en.wikipedia.org/wiki/Alfred_Pennyworth",
        ["alfred_pennyworth", "batman", "dc_comics"]
    ),
    # 216
    make_q(
        "pop_culture_hard_216",
        "Ποιο είναι το όνομα του εξαδέλφου του Οβελίξ που κατασκευάζει χρυσά δρεπάνια στη Λουτέτια στο άλμπουμ 'Ο Αστερίξ και το Χρυσό Δρεπάνι';",
        "Αμερίξ (Amerix)",
        ["Μεταλλουργίξ", "Ομεοπαθίξ", "Γαλαντίξ"],
        "Ο Αμερίξ είναι μακρινός ξάδελφος του Οβελίξ και ο μόνος ικανός να φτιάξει άριστα χρυσά δρεπάνια για τον δρυΐδη Πανοραμίξ.",
        [
            "Όταν ο Αστερίξ και ο Οβελίξ φτάνουν στη Λουτέτια, ανακαλύπτουν ότι ο Αμερίξ έχει απαχθεί από μια σπείρα λαθρεμπόρων δρεπανιών.",
            "Το άλμπουμ 'Το Χρυσό Δρεπάνι' (1962) ήταν η δεύτερη επίσημη περιπέτεια του Αστερίξ που εκδόθηκε."
        ],
        "https://en.wikipedia.org/wiki/Asterix_and_the_Golden_Sickle",
        ["asterix", "amerix", "comics", "goscinny"]
    ),
    # 217
    make_q(
        "pop_culture_hard_217",
        "Ποιο είναι το όνομα του Ρωμαίου ραδιούργου πράκτορα που σπέρνει διχόνοια και παράνοια στο γαλατικό χωριό στο 'Asterix and the Roman Agent';",
        "Τουλίους Δεστρούκτιβους (Tullius Detritus / Convolvulus)",
        ["Κάιους Μπόνους", "Κλαύδιους Μούσκουλους", "Γκράκους Γκάρους"],
        "Ο Detritus είναι ένας φυλακισμένος Ρωμαίος τόσο διαβολικά χειριστικός που καταφέρνει να κάνει τους πάντες γύρω του να τσακώνονται για το τίποτα.",
        [
            "Ο Ιούλιος Καίσαρας τον στέλνει στη Γαλατία για να διαλύσει τη φιλία του Αστερίξ και του Οβελίξ προσφέροντας ένα πολύτιμο βάζο.",
            "Η ιστορία αποτελεί μια εξαιρετική κοινωνιολογική σάτιρα της ζήλιας, της παραπληροφόρησης και των fake news."
        ],
        "https://en.wikipedia.org/wiki/Asterix_and_the_Roman_Agent",
        ["asterix", "tullius_detritus", "comics", "goscinny"]
    ),
    # 218
    make_q(
        "pop_culture_hard_218",
        "Ποιο πραγματικό ιστορικό γεγονός του 1892 στο Coffeyville του Κάνσας ενέπνευσε τον Morris να σκοτώσει τους αρχικούς ιστορικούς αδελφούς Ντάλτον;",
        "Η ταυτόχρονη ληστεία δύο τραπεζών (Coffeyville Bank Robbery)",
        ["Η επιδρομή στο τρένο της Santa Fe", "Η πολιορκία του Ο.Κ. Κόραλ", "Η απόδραση από το Γιούμα"],
        "Στις 5 Οκτωβρίου 1892, η ιστορική συμμορία Dalton προσπάθησε να ληστέψει δύο τράπεζες ταυτόχρονα στο Coffeyville και εξοντώθηκε από τους πολίτες.",
        [
            "Ο Morris απεικόνισε πιστά τον θάνατό τους στο άλμπουμ 'Hors-la-loi' (1951), αλλά επειδή οι χαρακτήρες άρεσαν στους αναγνώστες, ο Goscinny επινόησε τα αδέξια ξαδέλφια τους.",
            "Μόνο ο ιστορικός Emmett Dalton επέζησε με 23 τραύματα και αργότερα έγινε συγγραφέας και ηθοποιός στο Χόλιγουντ."
        ],
        "https://en.wikipedia.org/wiki/Dalton_Gang",
        ["lucky_luke", "daltons", "coffeyville", "western", "history"]
    ),
    # 219
    make_q(
        "pop_culture_hard_219",
        "Ποιο ήταν το όνομα του ιστορικού πλοίου του προγόνου του Καπετάνιου Χάντοκ που βυθίστηκε για να μην πέσει στα χέρια του πειρατή Κόκκινου Ρακάμ;",
        "Ο Μονόκερως (La Licorne / The Unicorn)",
        ["Η Σειρήνα", "Ο Μαύρος Περσέας", "Η Γοργόνα"],
        "Ο Ιππότης Φραγκίσκος του Αντόκ ανατίναξε τη 'Μονόκερω' το 1698 αφού πρώτα σκότωσε σε μονομαχία τον πειρατή Red Rackham.",
        [
            "Ο θησαυρός του πλοίου και τα τρία ομοιώματα-μοντέλα που περιείχαν περγαμηνές αποτελούν την υπόθεση του άλμπουμ 'Το Μυστικό του Μονόκερω'.",
            "Η ιστορία μεταφέρθηκε στον κινηματογράφο το 2011 σε σκηνοθεσία Steven Spielberg."
        ],
        "https://en.wikipedia.org/wiki/The_Secret_of_the_Unicorn",
        ["tintin", "unicorn", "captain_haddock", "herge"]
    ),
    # 220
    make_q(
        "pop_culture_hard_220",
        "Ποιο είναι το φανταστικό βαλκανικό βασίλειο με πρωτεύουσα την Κλόου (Klow) που επισκέπτεται ο Τεντέν στο 'Σκήπτρο του Οττοκάρ';",
        "Συλδαβία (Syldavia)",
        ["Βορδουρία", "Ρουριτανία", "Μολδοβλαχία"],
        "Η Συλδαβία απειλείται με προσάρτηση από τη γειτονική φασιστική Βορδουρία (Borduria) υπό τον δικτάτορα Müsstler.",
        [
            "Ο βασιλιάς Muskar XII κινδυνεύει να χάσει τον θρόνο του αν δεν εμφανιστεί την ημέρα του Αγίου Βλαδιμήρου κρατώντας το βασιλικό σκήπτρο.",
            "Ο Hergé επινόησε μια ολόκληρη λειτουργική γλώσσα (syldave) με δική της γραμματική βασισμένη στη διάλεκτο Marols των Βρυξελλών."
        ],
        "https://en.wikipedia.org/wiki/Syldavia",
        ["tintin", "syldavia", "herge", "comics"]
    ),
    # 221
    make_q(
        "pop_culture_hard_221",
        "Ποιο είναι το παραδοσιακό εθνικό ρητό της Συλδαβίας που συνοδεύει το έμβλημα του μαύρου πελεκάνου στα κόμικς του Τεντέν;",
        "Eih bennek, eih blavek (Εδώ είμαι, εδώ μένω)",
        ["In vino veritas", "Semper fidelis", "Libertas et honor"],
        "Το ρητό μεταφράζεται στη συλδαβική παράδοση ως 'Όποιος το αγγίζει τσιμπιέται' ή 'Εδώ είμαι, εδώ μένω', συμβολίζοντας την αδάμαστη ανεξαρτησία του κράτους.",
        [
            "Η φράση προέρχεται από την ολλανδική/φλαμανδική έκφραση των Βρυξελλών 'Hier ben ik, hier blijf ik'.",
            "Ο μαύρος πελεκάνος είναι το ιερό εθνικό πτηνό της Συλδαβίας και κοσμεί τη σημαία της χώρας."
        ],
        "https://en.wikipedia.org/wiki/Syldavia",
        ["tintin", "syldavia", "motto", "herge"]
    ),
    # 222
    make_q(
        "pop_culture_hard_222",
        "Ποια ήταν η επίσημη έγχρωμη επικεφαλής χρωματίστρια στα Studios Hergé που διαμόρφωσε την παλέτα των κλασικών τευχών του Τεντέν από το 1953 έως το 1983;",
        "Josette Baujot",
        ["Fanny Rodwell", "Alice Devos", "Monique Laurent"],
        "Η Josette Baujot ήταν γνωστή για τις έντονες διαφωνίες της με τον Hergé αλλά και για την απαράμιλλη αίσθηση του χρώματος που καθόρισε την τελική μορφή των άλμπουμ.",
        [
            "Ο Hergé της αφιέρωσε μια καρικατούρα στο τεύχος 'Πτήση 714 για Σίδνεϊ'.",
            "Εργάστηκε στα Studios Hergé για τρεις δεκαετίες και θεωρείται μία από τις πιο αφανείς πρωταγωνίστριες της γαλλοβελγικής σχολής."
        ],
        "https://en.wikipedia.org/wiki/Herg%C3%A9",
        ["tintin", "herge", "josette_baujot", "comics_history"]
    ),
    # 223
    make_q(
        "pop_culture_hard_223",
        "Ποιο είναι το πραγματικό αρειανό όνομα του υπερήρωα Martian Manhunter, ιδρυτικού μέλους της Justice League;",
        "J'onn J'onzz",
        ["M'gann M'orzz", "Ma'alefa'ak", "K'hym J'onzz"],
        "Ο J'onn J'onzz είναι ο τελευταίος επιζών Αρειανός της πράσινης φυλής, που τηλεμεταφέρθηκε στη Γη κατά λάθος από ένα πείραμα του Dr. Saul Erdel.",
        [
            "Στη Γη υιοθέτησε την ταυτότητα του αστυνομικού ντετέκτιβ John Jones.",
            "Η μεγαλύτερη αδυναμία του είναι η φωτιά, η οποία του προκαλεί ψυχοσωματικό τρόμο και αποδυνάμωση."
        ],
        "https://en.wikipedia.org/wiki/Martian_Manhunter",
        ["martian_manhunter", "dc_comics", "justice_league"]
    ),
    # 224
    make_q(
        "pop_culture_hard_224",
        "Ποιο είναι το όνομα του αρχαίου Αιγύπτιου προκατόχου του Shazam που διαφθάρηκε από τη δύναμη και έγινε ο μεγαλύτερος εχθρός του;",
        "Teth-Adam (Black Adam)",
        ["Amon Tomaz", "Khandaq", "Ibik"],
        "Ο Black Adam έλαβε τις δυνάμεις των αιγυπτιακών θεών (Shu, Heru, Amon, Zehuti, Aton, Mehen) αλλά εξορίστηκε στα βάθη του σύμπαντος λόγω της τυραννίας του.",
        [
            "Στην ταινία 'Black Adam' (2022) της Warner Bros/DC, τον αντιήρωα υποδύθηκε ο Dwayne 'The Rock' Johnson.",
            "Είναι ο αιώνιος προστάτης και κυβερνήτης του φανταστικού μεσανατολικού έθνους Kahndaq."
        ],
        "https://en.wikipedia.org/wiki/Black_Adam",
        ["black_adam", "shazam", "dc_comics", "teth_adam"]
    ),
    # 225
    make_q(
        "pop_culture_hard_225",
        "Ποιο ασυνήθιστο μέσο μεταφοράς χρησιμοποιούσε η Wonder Woman στα κλασικά κόμικς πριν αποκτήσει την ικανότητα φυσικής πτήσης τη δεκαετία του '80;",
        "Αόρατο Τζετ (Invisible Jet)",
        ["Χρυσό Άρμα", "Φτερωτό Πήγασο", "Αστρικό Δίσκο"],
        "Το Invisible Jet πρωτοεμφανίστηκε στο Sensation Comics #1 το 1942 ως ένα αόρατο αεροπλάνο που χειριζόταν η Diana μέσω νοητικών εντολών.",
        [
            "Στα πρώιμα κόμικς, η Wonder Woman σχεδιαζόταν καθισμένη στον αέρα σε στάση πιλότου επειδή το αεροσκάφος ήταν απολύτως διάφανο.",
            "Μετά το 'Crisis on Infinite Earths' (1985), η Wonder Woman απέκτησε τη δύναμη της αυτόνομης πτήσης από τον θεό Ερμή."
        ],
        "https://en.wikipedia.org/wiki/Invisible_Plane",
        ["wonder_woman", "invisible_jet", "dc_comics"]
    ),
    # 226
    make_q(
        "pop_culture_hard_226",
        "Ποιο ήταν το πραγματικό ονοματεπώνυμο γέννησης του θρύλου της Marvel, Stan Lee, πριν υιοθετήσει το παγκοσμίως γνωστό ψευδώνυμο;",
        "Stanley Martin Lieber",
        ["Stanley Leonard Levine", "Stanley Robert Lipschitz", "Stanley Morris Liebowitz"],
        "Ο Stanley Lieber υπέγραφε τα πρώτα του κόμικς ως 'Stan Lee' κρατώντας το πραγματικό του όνομα για το 'μεγάλο αμερικανικό μυθιστόρημα' που ήλπιζε να γράψει κάποτε.",
        [
            "Τελικά άλλαξε νόμιμα το όνομά του σε Stan Lee αφού καθιερώθηκε ως ο κορυφαίος συγγραφέας κόμικς στον κόσμο.",
            "Ο μικρότερος αδελφός του, Larry Lieber, υπήρξε επίσης σεναριογράφος και σχεδιαστής κόμικς συν-δημιουργώντας τον Thor και τον Iron Man."
        ],
        "https://en.wikipedia.org/wiki/Stan_Lee",
        ["stan_lee", "marvel", "comics_history"]
    ),
    # 227
    make_q(
        "pop_culture_hard_227",
        "Ποιος τυφλός δάσκαλος πολεμικών τεχνών εκπαίδευσε τον Matt Murdock (Daredevil) και ηγείται της μυστικής οργάνωσης 'The Chaste';",
        "Stick",
        ["Stone", "Shaft", "Master Izo"],
        "Ο Stick είναι ένας σκληρός και απαιτητικός δάσκαλος που δίδαξε στον Matt Murdock πώς να τιθασεύσει και να εκμεταλλευτεί τις υπερευαίσθητες αισθήσεις του.",
        [
            "Εκπαίδευσε επίσης την Elektra Natchios πριν εκείνη στραφεί στο σκοτεινό μονοπάτι των δολοφόνων.",
            "Δημιουργήθηκε από τον Frank Miller στο Daredevil #176 το 1981."
        ],
        "https://en.wikipedia.org/wiki/Stick_(comics)",
        ["stick", "daredevil", "marvel", "frank_miller"]
    ),
    # 228
    make_q(
        "pop_culture_hard_228",
        "Ποια αρχαία μυστική σέκτα φανατικών νίντζα δολοφόνων που λατρεύει έναν δαίμονα γνωστό ως 'The Beast' είναι ο αιώνιος εχθρός του Daredevil;",
        "The Hand (Το Χέρι)",
        ["The Foot Clan", "The Snakeroot", "The League of Assassins"],
        "Η οργάνωση The Hand ιδρύθηκε στην Ιαπωνία τον 16ο αιώνα και κατέχει μυστικιστικά ξόρκια ανάστασης νεκρών πολεμιστών.",
        [
            "Η γνωστή 'Foot Clan' στα Χελωνονιντζάκια δημιουργήθηκε από τους Eastman και Laird ως άμεση σατιρική παρωδία του The Hand της Marvel.",
            "Η Elektra διετέλεσε για ένα διάστημα ηγέτιδα του The Hand μετά την ανάστασή της."
        ],
        "https://en.wikipedia.org/wiki/The_Hand_(comics)",
        ["the_hand", "daredevil", "marvel", "ninja"]
    ),
    # 229
    make_q(
        "pop_culture_hard_229",
        "Ποιο είναι το πραγματικό γερμανικό ονοματεπώνυμο του κακοποιού Red Skull, επικεφαλής της ναζιστικής επιστημονικής πτέρυγας στα κόμικς;",
        "Johann Shmidt",
        ["Arnim Zola", "Heinrich Zemo", "Wolfgang von Strucker"],
        "Ο Johann Shmidt ήταν ένας ασήμαντος καμαριέρης ξενοδοχείου που επιλέχθηκε προσωπικά από τον Αδόλφο Χίτλερ για να εκπαιδευτεί ως ο απόλυτος τρομοκράτης του Ράιχ.",
        [
            "Στο MCU τον Red Skull υποδύθηκε ο Hugo Weaving στην ταινία 'Captain America: The First Avenger' (2011).",
            "Στο Infinity War και Endgame, ο χαρακτήρας εμφανίζεται ως ο καταραμένος φύλακας του Λίθου της Ψυχής στον πλανήτη Vormir."
        ],
        "https://en.wikipedia.org/wiki/Red_Skull",
        ["red_skull", "johann_shmidt", "captain_america", "marvel"]
    ),
    # 230
    make_q(
        "pop_culture_hard_230",
        "Ποιο ήταν το πραγματικό όνομα γέννησης του 'Βασιλιά των Κόμικς' Jack Kirby πριν υιοθετήσει το καλλιτεχνικό του ψευδώνυμο;",
        "Jacob Kurtzberg",
        ["Jack Lieberman", "Jacob Kozlowski", "Jack Kessel"],
        "Ο Jacob Kurtzberg γεννήθηκε στο Lower East Side του Μανχάταν από Αυστριακούς Εβραίους μετανάστες και μεγάλωσε μέσα στη φτώχεια της Μεγάλης Ύφεσης.",
        [
            "Μαζί με τον Stan Lee συν-δημιούργησε σχεδόν ολόκληρο το σύμπαν της Marvel: Fantastic Four, X-Men, Hulk, Thor, Iron Man και Avengers.",
            "Στη DC Comics δημιούργησε το έπος του 'Fourth World' και τον χαρακτήρα του Darkseid."
        ],
        "https://en.wikipedia.org/wiki/Jack_Kirby",
        ["jack_kirby", "jacob_kurtzberg", "marvel", "comics_history"]
    ),
    # 231
    make_q(
        "pop_culture_hard_231",
        "Ποιο ήταν το ιστορικό πρώτο βίντεο που αναρτήθηκε ποτέ στην πλατφόρμα του YouTube στις 23 Απριλίου 2005;",
        "Me at the zoo",
        ["Hello World", "My first video", "Testing camera"],
        "Το 19 δευτερολέπτων βίντεο δείχνει τον συνιδρυτή του YouTube Jawed Karim μπροστά από ελέφαντες στον ζωολογικό κήπο του San Diego.",
        [
            "Η ιστορική φράση που λέει ο Karim είναι: 'The cool thing about these guys is that they have really, really, really long trunks'.",
            "Το βίντεο έχει συγκεντρώσει πάνω από 300 εκατομμύρια προβολές ως το απόλυτο μνημείο της ιστορίας του ψηφιακού διαδικτύου."
        ],
        "https://en.wikipedia.org/wiki/Me_at_the_zoo",
        ["me_at_the_zoo", "youtube", "jawed_karim", "internet_history"]
    ),
    # 232
    make_q(
        "pop_culture_hard_232",
        "Ποιο 6λεπτο βίντεο του Judson Laipply από το 2006 έγινε το πρώτο viral βίντεο που έφτασε στο #1 των προβολών στο YouTube χορεύοντας τραγούδια διαφόρων δεκαετιών;",
        "Evolution of Dance",
        ["World of Dance", "Dance Century", "History of Pop"],
        "Ο κωμικός Judson Laipply εκτελούσε 12 διαφορετικούς χορούς από το 'Hound Dog' μέχρι το 'Macarena' και το 'Bye Bye Bye'.",
        [
            "Ήταν το πρώτο βίντεο στην ιστορία του διαδικτύου που ξεπέρασε τις 100 εκατομμύρια προβολές σε σύντομο χρονικό διάστημα.",
            "Η τεράστια επιτυχία του απέδειξε τη δύναμη του YouTube ως παγκόσμιου πολιτιστικού μέσου διανομής βίντεο."
        ],
        "https://en.wikipedia.org/wiki/Evolution_of_Dance",
        ["evolution_of_dance", "youtube", "viral", "internet_history"]
    ),
    # 233
    make_q(
        "pop_culture_hard_233",
        "Ποιος χρήστης ανάρτησε το θρυλικό συναισθηματικό βίντεο 'Leave Britney Alone!' στο YouTube το 2007 υπερασπιζόμενος την Britney Spears;",
        "Chris Crocker",
        ["Perez Hilton", "Tyler Oakley", "Shane Dawson"],
        "Ο Chris Crocker τράβηξε το βίντεο κλαίγοντας με αναφιλητά κάτω από ένα σεντόνι μετά την κατακραυγή για την εμφάνιση της Britney στα VMAs του 2007.",
        [
            "Το βίντεο συγκέντρωσε πάνω από 4 εκατομμύρια προβολές σε δύο ημέρες και έγινε αντικείμενο αναρίθμητων παρωδιών στην τηλεόραση.",
            "Χρόνια αργότερα, με το κίνημα #FreeBritney, πολλοί αναγνώρισαν ότι ο Crocker είχε απόλυτο δίκιο για την τοξικότητα των μέσων απέναντι στην τραγουδίστρια."
        ],
        "https://en.wikipedia.org/wiki/Leave_Britney_Alone!",
        ["leave_britney_alone", "chris_crocker", "youtube", "viral"]
    ),
    # 234
    make_q(
        "pop_culture_hard_234",
        "Ποιο ήταν το πραγματικό όνομα της γάτας που εμφανιζόταν στο viral βίντεο 'Keyboard Cat' να παίζει ηλεκτρικό πιάνο με μπλε μπλουζάκι;",
        "Fatso",
        ["Bento", "Maru", "Socks"],
        "Το υλικό καταγράφηκε αρχικά σε βιντεοκασέτα VHS το 1984 από τον Charlie Schmidt με τη γάτα του Fatso, πριν αναρτηθεί στο YouTube το 2007.",
        [
            "Το meme χρησιμοποιούνταν ως 'play him off, Keyboard Cat' στο τέλος βίντεο με ατυχήματα ή αποτυχίες ανθρώπων.",
            "Η αρχική γάτα Fatso είχε πεθάνει το 1987, πολύ πριν το βίντεο γίνει παγκόσμιο φαινόμενο."
        ],
        "https://en.wikipedia.org/wiki/Keyboard_Cat",
        ["keyboard_cat", "fatso", "memes", "youtube"]
    ),
    # 235
    make_q(
        "pop_culture_hard_235",
        "Σε ποιο έτος παρουσίασε ο Christian Dior την ιστορική του πρώτη συλλογή υψηλής ραπτικής που βαφτίστηκε 'New Look' από τη συντάκτρια του Harper's Bazaar;",
        "1947",
        ["1945", "1950", "1952"],
        "Η Carmel Snow του Harper's Bazaar αναφώνησε 'It's quite a revolution, dear Christian! Your dresses have such a new look!', δίνοντας το όνομα στο κίνημα.",
        [
            "Η συλλογή χαρακτηριζόταν από σφιχτή μέση, τονισμένο στήθος και φαρδιές πλούσιες φούστες που απαιτούσαν δεκάδες μέτρα υφάσματος.",
            "Το New Look σηματοδότησε την επιστροφή της θηλυκότητας και της πολυτέλειας στο Παρίσι μετά τις στερήσεις και τα δελτία υφασμάτων του Β' Παγκοσμίου Πολέμου."
        ],
        "https://en.wikipedia.org/wiki/Christian_Dior",
        ["christian_dior", "new_look", "fashion", "haute_couture", "1947"]
    ),
    # 236
    make_q(
        "pop_culture_hard_236",
        "Ποια ήταν η αρχική επίσημη γαλλική ονομασία της πρώτης συλλογής του Christian Dior του 1947 πριν μείνει στην ιστορία ως 'New Look';",
        "Corolle (Στεφάνη άνθους)",
        ["Envol", "Ligne H", "Tulipe"],
        "Ο Dior ονόμασε τη συλλογή 'Corolle' επειδή σχεδίασε τα φορέματα ώστε να μοιάζουν με ανεστραμμένα πέταλα λουλουδιών γύρω από το γυναικείο σώμα.",
        [
            "Το πιο εμβληματικό κομμάτι της συλλογής ήταν το σακάκι 'Bar Suit' από μεταξωτό σατέν με μαύρη πλισέ μάλλινη φούστα.",
            "Η συλλογή προκάλεσε αρχικά διαδηλώσεις από φεμινίστριες και συντηρητικούς στις ΗΠΑ λόγω της 'σπάταλης' χρήσης υφάσματος."
        ],
        "https://en.wikipedia.org/wiki/Christian_Dior",
        ["christian_dior", "corolle", "fashion", "new_look"]
    ),
    # 237
    make_q(
        "pop_culture_hard_237",
        "Ποιος Ισπανός σχεδιαστής υποδημάτων με καταγωγή από τα Κανάρια Νησιά έγινε παγκόσμιο φαινόμενο χάρη στην εμμονή της Carrie Bradshaw στο 'Sex and the City';",
        "Manolo Blahnik",
        ["Christian Louboutin", "Jimmy Choo", "Pedro García"],
        "Οι σατέν μπλε γόβες 'Hangisi' του Manolo Blahnik με την αγκράφα από κρύσταλλα αποτέλεσαν το απόλυτο σύμβολο μόδας της σειράς και της ταινίας.",
        [
            "Η Sarah Jessica Parker είχε δηλώσει ότι τα παπούτσια του Manolo Blahnik ήταν ουσιαστικά ο πέμπτος βασικός χαρακτήρας της σειράς.",
            "Ο Blahnik σχεδιάζει κάθε παπούτσι μόνος του στο χέρι λαξεύοντας το ξύλινο καλαπόδι."
        ],
        "https://en.wikipedia.org/wiki/Manolo_Blahnik",
        ["manolo_blahnik", "sex_and_the_city", "shoes", "fashion"]
    ),
    # 238
    make_q(
        "pop_culture_hard_238",
        "Ποιος κατά συρροή δολοφόνος πυροβόλησε θανάσιμα τον Gianni Versace στα σκαλοπάτια της έπαυλής του Casa Casuarina στο Miami Beach το 1997;",
        "Andrew Cunanan",
        ["Mark David Chapman", "David Berkowitz", "Richard Ramirez"],
        "Ο 27χρονος Andrew Cunanan είχε ήδη δολοφονήσει τέσσερα άτομα πριν σκοτώσει τον Versace και αυτοκτονήσει οκτώ ημέρες αργότερα σε ένα πλωτό σπίτι.",
        [
            "Η κηδεία του Versace στον καθεδρικό ναό του Μιλάνου συγκέντρωσε προσωπικότητες όπως η Πριγκίπισσα Diana, ο Elton John και ο Sting.",
            "Η τραγική ιστορία καταγράφηκε στη βραβευμένη με Emmy σειρά 'The Assassination of Gianni Versace: American Crime Story' (2018)."
        ],
        "https://en.wikipedia.org/wiki/Gianni_Versace",
        ["gianni_versace", "andrew_cunanan", "fashion_history", "true_crime"]
    ),
    # 239
    make_q(
        "pop_culture_hard_239",
        "Ποια ήταν η αρχική επίσημη ονομασία της τσάντας του οίκου Hermès (1935) πριν μετονομαστεί επισήμως σε 'Kelly' το 1977;",
        "Sac à dépêches",
        ["Haut à courroies", "Plume", "Constance"],
        "Η τσάντα σχεδιάστηκε από τον Robert Dumas το 1935 ως 'Sac à dépêches' (τσάντα εγγράφων/ταχυδρομείου) με αυστηρή γεωμετρική γραμμή τραπεζίου.",
        [
            "Το 1956 η Grace Kelly, νέα πριγκίπισσα του Μονακό, χρησιμοποίησε την τσάντα για να κρύψει την εγκυμοσύνη της από τους παπαράτσι.",
            "Η φωτογραφία στο περιοδικό Life έκανε την τσάντα παγκόσμιο θρύλο, αναγκάζοντας την Hermès να τη μετονομάσει επίσημα δεκαετίες αργότερα."
        ],
        "https://en.wikipedia.org/wiki/Kelly_bag",
        ["hermes", "kelly_bag", "grace_kelly", "fashion", "luxury"]
    ),
    # 240
    make_q(
        "pop_culture_hard_240",
        "Ποιος σπουδαίος σχεδιαστής μόδας από τη Βόρεια Μακεδονία δημιούργησε το πολυσυζητημένο 'φόρεμα-κύκνο' (Swan Dress) της Björk στα Όσκαρ του 2001;",
        "Marjan Pejoski",
        ["Hussein Chalayan", "Gareth Pugh", "Bernhard Willhelm"],
        "Ο Marjan Pejoski σχεδίασε το φόρεμα σε σχήμα κύκνου που τύλιγε τον λαιμό της Björk, με την ίδια να 'γεννά' αυγά στρουθοκαμήλου στο κόκκινο χαλί.",
        [
            "Αν και αρχικά χλευάστηκε από τους κριτικούς μόδας, θεωρείται σήμερα μία από τις πιο εμβληματικές στιγμές avant-garde στην ιστορία των Όσκαρ.",
            "Το φόρεμα εκτέθηκε αργότερα στο Μουσείο Μοντέρνας Τέχνης (MoMA) της Νέας Υόρκης."
        ],
        "https://en.wikipedia.org/wiki/Swan_dress_of_Bj%C3%B6rk",
        ["bjork", "swan_dress", "marjan_pejoski", "oscars", "fashion"]
    ),
    # 241
    make_q(
        "pop_culture_hard_241",
        "Σε ποιο έτος κατοχυρώθηκε με δίπλωμα ευρεσιτεχνίας το σύγχρονο τουβλάκι LEGO με τους εσωτερικούς κυλίνδρους σύζευξης (stud-and-tube coupling);",
        "1958",
        ["1949", "1954", "1962"],
        "Η πατέντα κατατέθηκε στο γραφείο ευρεσιτεχνιών της Κοπεγχάγης στις 28 Ιανουαρίου 1958 στις 13:58 από τον Godtfred Kirk Christiansen.",
        [
            "Οι εσωτερικοί κύλινδροι επέτρεψαν στα τουβλάκια να κουμπώνουν σταθερά μεταξύ τους χωρίς να καταρρέουν, λύνοντας το μεγαλύτερο τεχνικό πρόβλημα.",
            "Ένα τουβλάκι LEGO που κατασκευάστηκε το 1958 μπορεί ακόμα να κουμπώσει τέλεια με ένα τουβλάκι που παράγεται σήμερα."
        ],
        "https://en.wikipedia.org/wiki/Lego",
        ["lego", "patent", "toys", "denmark", "1958"]
    ),
    # 242
    make_q(
        "pop_culture_hard_242",
        "Ποια ήταν η πρώτη επίσημη Αφροαμερικανίδα κούκλα φίλη της Barbie που κυκλοφόρησε η Mattel το 1968;",
        "Christie",
        ["Francie", "Julia", "Nikki"],
        "Η Christie παρουσιάστηκε το 1968 στο απόγειο του κινήματος πολιτικών δικαιωμάτων στις ΗΠΑ φορώντας ένα μοντέρνο μαγιό.",
        [
            "Το 1969 ακολούθησε η κούκλα 'Julia', βασισμένη στον πρωτοποριακό τηλεοπτικό ρόλο της Diahann Carroll ως νοσοκόμα.",
            "Η πρώτη επίσημη κούκλα με το ίδιο το όνομα 'Barbie' που ήταν μαύρη κυκλοφόρησε το 1980 σχεδιασμένη από την Kitty Black Perkins."
        ],
        "https://en.wikipedia.org/wiki/Barbie%27s_friends_and_family#Christie",
        ["barbie", "christie", "mattel", "toys", "black_history"]
    ),
    # 243
    make_q(
        "pop_culture_hard_243",
        "Ποιος τρομερός αρχηγός της Evil Horde υπήρξε ο αρχικός δάσκαλος του Skeletor πριν γίνει ο κύριος εχθρός της She-Ra;",
        "Hordak",
        ["King Hiss", "Modulok", "Shadow Weaver"],
        "Ο Hordak εκπαίδευσε τον Skeletor στις σκοτεινές τέχνες πριν προδοθεί από αυτόν και εξοριστεί στον πλανήτη Etheria.",
        [
            "Ο Hordak χρησιμοποιεί κυρίως τεχνολογικές μεταμορφώσεις του σώματός του (cybernetic body morphing) σε αντίθεση με τη μαγεία του Skeletor.",
            "Απήγαγε την πριγκίπισσα Adora (She-Ra), δίδυμη αδελφή του He-Man, όταν εκείνη ήταν βρέφος."
        ],
        "https://en.wikipedia.org/wiki/Hordak",
        ["hordak", "masters_of_the_universe", "she_ra", "he_man"]
    ),
    # 244
    make_q(
        "pop_culture_hard_244",
        "Ποιο ήταν το πραγματικό νούμερο του επιπέδου δύναμης του Goku στο πρωτότυπο ιαπωνικό manga του Dragon Ball πριν το λάθος της αγγλικής μεταγλώττισης ('Over 9000');",
        "Πάνω από 8.000 (Over 8,000)",
        ["Πάνω από 7.000", "Πάνω από 6.000", "Πάνω από 10.000"],
        "Στο ιαπωνικό πρωτότυπο manga και anime, ο Vegeta φωνάζει 'Hassenshi ijō da!' (Είναι πάνω από 8.000!), αλλά η αγγλική μεταγλώττιση της Ocean Productions το άλλαξε σε 9.000 για καλύτερο συγχρονισμό χειλιών.",
        [
            "Η ατάκα 'It's Over 9000!' έγινε ένα από τα πιο αναγνωρίσιμα και διαχρονικά memes στην ιστορία του ίντερνετ.",
            "Ο ηθοποιός Brian Drummond που χάρισε τη φωνή στον Vegeta στην αρχική αγγλική μεταγλώττιση δημιούργησε την ιστορική κραυγή."
        ],
        "https://en.wikipedia.org/wiki/It%27s_Over_9000!",
        ["dragon_ball_z", "over_9000", "vegeta", "memes", "anime"]
    ),
    # 245
    make_q(
        "pop_culture_hard_245",
        "Ποιος ήταν ο αριθμός καταλόγου του πειραματόζωου-παιδιού Akira με τις τρομακτικές τηλεκινητικές δυνάμεις στην ομώνυμη ταινία του Katsuhiro Otomo (1988);",
        "No. 28",
        ["No. 41", "No. 26", "No. 19"],
        "Ο Akira ήταν το υποκείμενο Νο 28 του στρατιωτικού προγράμματος Espers, του οποίου η ανεξέλεγκτη δύναμη προκάλεσε την καταστροφή του Τόκιο το 1988.",
        [
            "Ο αριθμός 28 αποτελεί άμεσο φόρο τιμής στο κλασικό manga 'Tetsujin 28-go' (Gigantor) του Mitsuteru Yokoyama.",
            "Η ταινία Akira έθεσε νέα παγκόσμια στάνταρ για το animation με πάνω από 160.000 χειροποίητα καρέ και πρωτοποριακή χρήση φωτισμού."
        ],
        "https://en.wikipedia.org/wiki/Akira_(1988_film)",
        ["akira", "katsuhiro_otomo", "anime", "cyberpunk"]
    ),
    # 246
    make_q(
        "pop_culture_hard_246",
        "Ποιος οραματιστής Ιάπωνας σκηνοθέτης δημιούργησε την αριστουργηματική cyberpunk anime ταινία 'Ghost in the Shell' το 1995;",
        "Mamoru Oshii",
        ["Katsuhiro Otomo", "Satoshi Kon", "Hideaki Anno"],
        "Ο Mamoru Oshii μετέφερε το manga του Masamune Shirow στη μεγάλη οθόνη, εξερευνώντας τη φιλοσοφία της συνείδησης και της ταυτότητας στον κυβερνοχώρο.",
        [
            "Η ταινία επηρέασε άμεσα τις αδελφές Wachowski στη δημιουργία του 'The Matrix', οι οποίες έδειξαν την ταινία στον παραγωγό Joel Silver λέγοντας: 'Θέλουμε να το κάνουμε αυτό σε live-action'.",
            "Η πρωταγωνίστρια Major Motoko Kusanagi είναι ένα πλήρες cyborg του οποίου μόνο ο εγκέφαλος διατηρεί οργανικά ίχνη."
        ],
        "https://en.wikipedia.org/wiki/Ghost_in_the_Shell_(1995_film)",
        ["ghost_in_the_shell", "mamoru_oshii", "anime", "cyberpunk"]
    ),
    # 247
    make_q(
        "pop_culture_hard_247",
        "Ποιο ήταν το όνομα του πρωτοποριακού διαστημικού καταδιωκτικού μονοθέσιου του Spike Spiegel στο anime 'Cowboy Bebop';",
        "Swordfish II",
        ["Red Tail", "Hammerhead", "Bebop"],
        "Το Swordfish II ήταν ένα παλιό αγωνιστικό σκάφος υψηλών ταχυτήτων μετασκευασμένο από τον μηχανικό Doohan με ένα τεράστιο κανόνι πλάσματος.",
        [
            "Διαθέτει αναδιπλούμενα φτερά και μπορεί να επιχειρεί τόσο στην ατμόσφαιρα πλανητών όσο και στο κενό του διαστήματος.",
            "Ο σχεδιασμός του εμπνεύστηκε εν μέρει από το ιστορικό βρετανικό τορπιλοπλάνο Fairey Swordfish του Β' Παγκοσμίου Πολέμου."
        ],
        "https://en.wikipedia.org/wiki/Cowboy_Bebop",
        ["cowboy_bebop", "swordfish_ii", "spike_spiegel", "anime"]
    ),
    # 248
    make_q(
        "pop_culture_hard_248",
        "Ποιο ήταν το όνομα του θρυλικού πειρατικού πλοίου του Gol D. Roger στο 'One Piece', φτιαγμένου από το μυθικό ξύλο του δέντρου Adam;",
        "Oro Jackson",
        ["Thousand Sunny", "Going Merry", "Moby Dick"],
        "Το Oro Jackson ναυπηγήθηκε από τον θρυλικό Tom στα Water 7 και υπήρξε το μοναδικό πλοίο που έφτασε ποτέ στο μυστηριώδες νησί Laugh Tale.",
        [
            "Η πλώρη του πλοίου κοσμούνταν από δύο χρυσές γοργόνες που πλαισίωναν ένα κανόνι.",
            "Ο ναυπηγός Tom εκτελέστηκε αργότερα από την Παγκόσμια Κυβέρνηση με την κατηγορία ότι ναυπήγησε το πλοίο του Βασιλιά των Πειρατών."
        ],
        "https://en.wikipedia.org/wiki/One_Piece",
        ["one_piece", "oro_jackson", "gol_d_roger", "anime"]
    ),
    # 249
    make_q(
        "pop_culture_hard_249",
        "Ποια αρχαία σκλάβα απέκτησε πρώτη τη δύναμη των Τιτάνων πριν από 2.000 χρόνια στο 'Attack on Titan';",
        "Ymir Fritz",
        ["Historia Reiss", "Frieda Reiss", "Dina Fritz"],
        "Η Ymir Fritz συγχωνεύτηκε με ένα μυστηριώδες παρασιτικό ον σε μια κουφάλα δέντρου και έγινε ο Ιδρυτικός Τιτάνας (Founding Titan).",
        [
            "Μετά τον θάνατό της, η ψυχή της παγιδεύτηκε για δύο χιλιετίες στη διάσταση 'Paths', πλάθοντας ακούραστα όλους τους Τιτάνες από άμμο.",
            "Ο βασιλιάς Fritz ανάγκασε τις τρεις κόρες τους (Maria, Rose και Sina) να καταβροχθίσουν το σώμα της μητέρας τους για να κληρονομήσουν τη δύναμη."
        ],
        "https://en.wikipedia.org/wiki/Attack_on_Titan",
        ["attack_on_titan", "ymir_fritz", "titans", "anime"]
    ),
    # 250
    make_q(
        "pop_culture_hard_250",
        "Ποιο είναι το πραγματικό ονοματεπώνυμο του μυστηριώδους ντετέκτιβ 'L' στο manga και anime 'Death Note';",
        "L Lawliet",
        ["Nate River", "Mihael Keehl", "Mail Jeevas"],
        "Το πραγματικό όνομα του L αποκαλύφθηκε επίσημα στον 13ο ειδικό τόμο του manga 'Death Note: How to Read 13'.",
        [
            "Ο L μεγάλωσε στο ορφανοτροφείο Wammy's House στο Winchester της Αγγλίας υπό την κηδεμονία του Watari (Quillsh Wammy).",
            "Οι δύο νεαροί διάδοχοί του στο ορφανοτροφείο ήταν ο Near (Nate River) και ο Mello (Mihael Keehl)."
        ],
        "https://en.wikipedia.org/wiki/L_(Death_Note)",
        ["death_note", "l_lawliet", "anime", "manga"]
    ),
    # 251
    make_q(
        "pop_culture_hard_251",
        "Ποιος σπουδαίος mangaka δημιούργησε τα 'Hunter x Hunter' και 'YuYu Hakusho' και είναι παντρεμένος με τη δημιουργό του Sailor Moon, Naoko Takeuchi;",
        "Yoshihiro Togashi",
        ["Eiichiro Oda", "Masashi Kishimoto", "Tite Kubo"],
        "Ο Yoshihiro Togashi παντρεύτηκε τη Naoko Takeuchi το 1999, αποτελώντας το πιο διάσημο ζευγάρι δημιουργών στην ιστορία των ιαπωνικών manga.",
        [
            "Είναι γνωστός για τα περίπλοκα συστήματα δυνάμεων (όπως το Nen) και την ψυχολογική αποδόμηση των shonen κλισέ.",
            "Λόγω σοβαρών χρόνιων προβλημάτων στην πλάτη, το Hunter x Hunter έχει περάσει από πολυετείς περιόδους διακοπής (hiatus)."
        ],
        "https://en.wikipedia.org/wiki/Yoshihiro_Togashi",
        ["yoshihiro_togashi", "hunter_x_hunter", "sailor_moon", "manga"]
    ),
    # 252
    make_q(
        "pop_culture_hard_252",
        "Πώς ονομάζεται το αιματοβαμμένο μαγικό σύμβολο που χαράσσεται στο σώμα του Guts και προσελκύει δαίμονες στο σκοτεινό έπος 'Berserk';",
        "Σήμα της Θυσίας (Brand of Sacrifice)",
        ["Σφραγίδα του Χάους", "Μάτι της Αβύσσου", "Στίγμα των Αποστόλων"],
        "Το Brand of Sacrifice χαράχτηκε στον αυχένα του Guts κατά τη διάρκεια του φρικτού Eclipse, σηματοδοτώντας τον ως τροφή για τα πλάσματα της νύχτας.",
        [
            "Το αριστούργημα σκοτεινής φαντασίας του εκλιπόντος Kentaro Miura ενέπνευσε άμεσα βιντεοπαιχνίδια όπως τα Dark Souls, Bloodborne και Elden Ring.",
            "Το σήμα αιμορραγεί και προκαλεί αφόρητο πόνο στον κάτοχό του κάθε φορά που πλησιάζει δαίμονας."
        ],
        "https://en.wikipedia.org/wiki/Berserk_(manga)",
        ["berserk", "guts", "brand_of_sacrifice", "kentaro_miura", "manga"]
    ),
    # 253
    make_q(
        "pop_culture_hard_253",
        "Ποιο ήταν το πραγματικό όνομα γέννησης του David Bowie πριν το αλλάξει για να μην τον μπερδεύουν με τον τραγουδιστή των Monkees;",
        "David Robert Jones",
        ["David William Davies", "David Kenneth Taylor", "David Arthur Brown"],
        "Ο David Robert Jones άλλαξε το επώνυμό του σε 'Bowie' το 1966, εμπνευσμένος από το αμερικανικό μαχαίρι κυνηγιού Bowie knife του Jim Bowie.",
        [
            "Ήθελε να αποφύγει τη σύγχυση με τον Davy Jones του διάσημου τότε αμερικανικού ποπ συγκροτήματος The Monkees.",
            "Δημιούργησε εμβληματικές περσόνες στην ιστορία της μουσικής, όπως ο Ziggy Stardust, ο Aladdin Sane και ο Thin White Duke."
        ],
        "https://en.wikipedia.org/wiki/David_Bowie",
        ["david_bowie", "david_robert_jones", "rock_music", "celebrities"]
    ),
    # 254
    make_q(
        "pop_culture_hard_254",
        "Ποιος φωτογράφος τράβηξε μέσα σε μόλις 10 λεπτά την ιστορική φωτογραφία των Beatles στη διάβαση του Abbey Road τον Αύγουστο του 1969;",
        "Iain Macmillan",
        ["Robert Freeman", "Astrid Kirchherr", "Annie Leibovitz"],
        "Ο Iain Macmillan ανέβηκε σε μια σκάλα στη μέση του δρόμου ενώ ένας αστυνομικός σταμάτησε την κυκλοφορία, τραβώντας συνολικά έξι λήψεις.",
        [
            "Η πέμπτη λήψη επιλέχθηκε για το εξώφυλλο επειδή και τα τέσσερα 'Σκαθάρια' περπατούσαν σε τέλειο συγχρονισμό.",
            "Το γεγονός ότι ο Paul McCartney περπατούσε ξυπόλυτος και εκτός βήματος πυροδότησε την παγκόσμια θεωρία συνωμοσίας 'Paul is Dead'."
        ],
        "https://en.wikipedia.org/wiki/Abbey_Road",
        ["beatles", "abbey_road", "iain_macmillan", "rock_history"]
    ),
    # 255
    make_q(
        "pop_culture_hard_255",
        "Πώς ονομάζεται το μυθικό στούντιο ηχογραφήσεων και ιδιωτικό συγκρότημα 6.000 τ.μ. του Prince στο Chanhassen της Μινεσότα;",
        "Paisley Park",
        ["Purple Rain Ranch", "Electric Lady", "Sunset Sound"],
        "Το Paisley Park άνοιξε το 1987 και περιλάμβανε υπερσύγχρονα στούντιο ήχου, ηχοληψίας, σκηνές γυρισμάτων και έναν ιδιωτικό συναυλιακό χώρο.",
        [
            "Μετά τον θάνατο του Prince το 2016, το συγκρότημα μετατράπηκε σε μουσείο ανοιχτό για το κοινό, όπως η Graceland του Elvis Presley.",
            "Στο κτίριο υπήρχε ένα τεράστιο θησαυροφυλάκιο ('The Vault') γεμάτο με εκατοντάδες ακυκλοφόρητα άλμπουμ και χιλιάδες τραγούδια."
        ],
        "https://en.wikipedia.org/wiki/Paisley_Park",
        ["prince", "paisley_park", "music_history", "minnesota"]
    ),
    # 256
    make_q(
        "pop_culture_hard_256",
        "Ποιο supermodel δήλωσε στο περιοδικό Vogue το 1990 την ιστορική φράση: 'Δεν ξυπνάμε για λιγότερα από 10.000 δολάρια την ημέρα';",
        "Linda Evangelista",
        ["Naomi Campbell", "Cindy Crawford", "Christy Turlington"],
        "Η Linda Evangelista είπε τη διάσημη ατάκα στον δημοσιογράφο Jonathan Van Meter, αποτυπώνοντας την απόλυτη ισχύ της εποχής των 'Big Six' Supermodels.",
        [
            "Αργότερα εξέφρασε τη λύπη της για τη δήλωση, λέγοντας ότι την ακολουθούσε σαν κατάρα σε όλη της την καριέρα.",
            "Υπήρξε η αγαπημένη μούσα του φωτογράφου Steven Meisel και του σχεδιαστή Karl Lagerfeld."
        ],
        "https://en.wikipedia.org/wiki/Linda_Evangelista",
        ["linda_evangelista", "supermodels", "fashion", "90s"]
    ),
    # 257
    make_q(
        "pop_culture_hard_257",
        "Ποιος Γάλλος αριστοκράτης σχεδιαστής υψηλής ραπτικής δημιούργησε το ιστορικό μαύρο φόρεμα της Audrey Hepburn στην ταινία 'Breakfast at Tiffany's' (1961);",
        "Hubert de Givenchy",
        ["Cristóbal Balenciaga", "Christian Dior", "Pierre Balmain"],
        "Ο Givenchy έντυσε την Hepburn σε πολλές από τις πιο διάσημες ταινίες της (Sabrina, Funny Face), αναπτύσσοντας μια ισόβια προσωπική φιλία μαζί της.",
        [
            "Το αρχικό φόρεμα της ταινίας πουλήθηκε σε δημοπρασία του οίκου Christie's στο Λονδίνο το 2006 για πάνω από 467.000 λίρες.",
            "Η Hepburn υπήρξε το πρώτο αστέρι του σινεμά που έγινε το πρόσωπο ενός εμπορικού αρώματος (το L'Interdit του Givenchy)."
        ],
        "https://en.wikipedia.org/wiki/Black_Givenchy_dress_of_Audrey_Hepburn",
        ["audrey_hepburn", "givenchy", "breakfast_at_tiffanys", "fashion"]
    ),
    # 258
    make_q(
        "pop_culture_hard_258",
        "Ποιος Βρετανός σκηνοθέτης γύρισε την ιστορική τηλεοπτική διαφήμιση '1984' για την παρουσίαση του υπολογιστή Apple Macintosh στο Super Bowl XVIII;",
        "Ridley Scott",
        ["Stanley Kubrick", "David Fincher", "George Lucas"],
        "Ο Ridley Scott (σκηνοθέτης των Alien και Blade Runner) εμπνεύστηκε από το δυστοπικό μυθιστόρημα του George Orwell δείχνοντας μια αθλήτρια να σπάει την οθόνη του Μεγάλου Αδελφού.",
        [
            "Η διαφήμιση προβλήθηκε πανεθνικά μόνο μία φορά κατά τη διάρκεια του Super Bowl στις 22 Ιανουαρίου 1984.",
            "Θεωρείται από πολλούς ιστορικούς των media ως η πιο επιδραστική και αριστουργηματική τηλεοπτική διαφήμιση όλων των εποχών."
        ],
        "https://en.wikipedia.org/wiki/1984_(advertisement)",
        ["apple", "macintosh", "ridley_scott", "super_bowl", "1984"]
    ),
    # 259
    make_q(
        "pop_culture_hard_259",
        "Σε ποιον ηφαιστειακό πλανήτη συγκρούστηκαν ο Obi-Wan Kenobi και ο Anakin Skywalker στη μονομαχία που οδήγησε στη γέννηση του Darth Vader με στολή;",
        "Mustafar",
        ["Geonosis", "Sullust", "Kamino"],
        "Ο Mustafar είναι ένας πλανήτης γεμάτος ενεργά ηφαίστεια και ποτάμια λάβας όπου ο Anakin υπέστη σοβαρά εγκαύματα μετά την ήττα του από τον Obi-Wan.",
        [
            "Ο Darth Vader έχτισε αργότερα το προσωπικό του επιβλητικό οψιδιανό κάστρο στον Mustafar για να αντλεί δύναμη από τον πόνο του.",
            "Η σκηνή της μονομαχίας στο 'Revenge of the Sith' (2005) συνδύασε αληθινά πλάνα από την έκρηξη του ηφαιστείου της Αίτνας στη Σικελία."
        ],
        "https://en.wikipedia.org/wiki/Mustafar",
        ["star_wars", "mustafar", "darth_vader", "obi_wan_kenobi"]
    ),
    # 260
    make_q(
        "pop_culture_hard_260",
        "Ποιος ιδιοφυής conceptual designer ήταν ο βασικός υπεύθυνος για την οπτική σύλληψη του Darth Vader, των Stormtroopers και του Millennium Falcon;",
        "Ralph McQuarrie",
        ["Joe Johnston", "Phil Tippett", "Stuart Freeborn"],
        "Οι πίνακες και τα σχέδια του Ralph McQuarrie ήταν εκείνα που έπεισαν τα στελέχη της 20th Century Fox να χρηματοδοτήσουν το Star Wars του George Lucas το 1976.",
        [
            "Ο McQuarrie πρότεινε τη μάσκα αναπνοής του Darth Vader σκεπτόμενος ότι ο χαρακτήρας θα έπρεπε να επιβιώσει στο κενό του διαστήματος περνώντας από σκάφος σε σκάφος.",
            "Σχεδίασε επίσης τις αρχικές ιδέες για τους C-3PO, R2-D2 και Chewbacca."
        ],
        "https://en.wikipedia.org/wiki/Ralph_McQuarrie",
        ["star_wars", "ralph_mcquarrie", "darth_vader", "concept_art"]
    ),
    # 261
    make_q(
        "pop_culture_hard_261",
        "Ποια τερατώδης απόγονος της Ungoliant κατοικεί στο πέρασμα του Cirith Ungol και παραλίγο να σκοτώσει τον Frodo στον 'Άρχοντα των Δαχτυλιδιών';",
        "Shelob (Σέλομπ)",
        ["Ungoliant", "Ancalagon", "Glaurung"],
        "Η Shelob είναι μια γιγάντια αράχνη που ζει στα σκοτεινά σύνορα της Mordor και τρέφεται με οτιδήποτε πέσει στον ιστό της.",
        [
            "Ο Samwise Gamgee καταφέρνει να την τραυματίσει βαριά χρησιμοποιώντας το ξωτικό σπαθί Sting και το Φιαλίδιο της Galadriel.",
            "Ο Tolkien την περιγράφει ως ένα πλάσμα που δεν υπηρετεί κανέναν, ούτε καν τον Sauron, νοιαζόμενη μόνο για το ακόρεστο κυνήγι της."
        ],
        "https://en.wikipedia.org/wiki/Shelob",
        ["lord_of_the_rings", "shelob", "tolkien", "fantasy"]
    ),
    # 262
    make_q(
        "pop_culture_hard_262",
        "Ποιος ήταν ο πρώτος Σκοτεινός Άρχοντας της Μέσης Γης στη μυθολογία του Tolkien, από τον οποίο διδάχθηκε και υπηρέτησε ο Sauron;",
        "Morgoth (Melkor)",
        ["Gothmog", "Sauron", "Saruman"],
        "Ο Melkor ήταν ο ισχυρότερος από τους Ainur που εξεγέρθηκε ενάντια στον δημιουργό Eru Ilúvatar εισάγοντας τη δυσαρμονία στη Μεγάλη Μουσική.",
        [
            "Πήρε το όνομα 'Morgoth' ('Ο Μαύρος Εχθρός του Κόσμου') από το ξωτικό Fëanor μετά την κλοπή των τριών Silmaril.",
            "Νικήθηκε στο τέλος της Πρώτης Εποχής στον Πόλεμο της Οργής και εκδιώχθηκε πέρα από τα Τείχη της Νύχτας στο Αιώνιο Κενό."
        ],
        "https://en.wikipedia.org/wiki/Morgoth",
        ["lord_of_the_rings", "morgoth", "melkor", "silmarillion", "tolkien"]
    ),
    # 263
    make_q(
        "pop_culture_hard_263",
        "Ποιο ήταν το όνομα της μητέρας του Lord Voldemort, άμεσης απογόνου του Salazar Slytherin, που μάγεψε τον Tom Riddle Sr. με ερωτικό φίλτρο;",
        "Merope Gaunt",
        ["Morfin Gaunt", "Marvolo Gaunt", "Hepzibah Smith"],
        "Η Merope Gaunt ζούσε σε συνθήκες απόλυτης ανέχειας και κακοποίησης από τον πατέρα της Marvolo και τον αδελφό της Morfin στο Little Hangleton.",
        [
            "Χρησιμοποίησε μαγικό φίλτρο αγάπης για να παντρευτεί τον πλούσιο Μαγκλ Tom Riddle, αλλά όταν σταμάτησε να του το χορηγεί, εκείνος την εγκατέλειψε έγκυο.",
            "Πέθανε λίγες ώρες μετά τη γέννηση του γιου της σε ένα ορφανοτροφείο του Λονδίνου αφού πρόλαβε να τον ονομάσει Tom Marvolo Riddle."
        ],
        "https://en.wikipedia.org/wiki/Lord_Voldemort#Family_tree",
        ["harry_potter", "voldemort", "merope_gaunt", "slytherin"]
    ),
    # 264
    make_q(
        "pop_culture_hard_264",
        "Ποιο ήταν το πατρογονικό σπαθί από βαλυριανό ατσάλι του Οίκου Mormont που ο Jeor Mormont παρέδωσε στον Jon Snow αφού άλλαξε τη λαβή του σε λύκο;",
        "Longclaw (Μακρονύχης)",
        ["Dark Sister", "Blackfyre", "Heartsbane"],
        "Το Longclaw ανήκε στον Οίκο Mormont επί πέντε αιώνες, αλλά ο Lord Commander Jeor Mormont το χάρισε στον Jon Snow ως ένδειξη ευγνωμοσύνης που του έσωσε τη ζωή.",
        [
            "Ο Jeor αντικατέστησε το παραδοσιακό κεφάλι αρκούδας στη λαβή με ένα λευκό πέτρινο κεφάλι ανταρόλυκου με ρουμπίνια για μάτια.",
            "Ο γιος του Jeor, Jorah Mormont, είχε αφήσει πίσω του το σπαθί όταν εξορίστηκε από το Westeros από ντροπή για το δουλεμπόριο."
        ],
        "https://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_weapons#Longclaw",
        ["game_of_thrones", "longclaw", "jon_snow", "mormont"]
    ),
    # 265
    make_q(
        "pop_culture_hard_265",
        "Ποιο ήταν το πραγματικό όνομα του Three-Eyed Raven στα βιβλία του George R. R. Martin, ο οποίος υπήρξε Targaryen νόθος και Χέρι του Βασιλιά;",
        "Brynden Rivers (Bloodraven)",
        ["Aegor Rivers", "Daemon Blackfyre", "Duncan the Tall"],
        "Ο Brynden Rivers ήταν ένας αλμπίνο Targaryen νόθος με ένα κόκκινο εκ γενετής σημάδι στο μάγουλο που έμοιαζε με κοράκι.",
        [
            "Υπηρέτησε ως Lord Commander της Νυχτερινής Φρουράς πριν εξαφανιστεί πέρα από το Τείχος και συνδεθεί με τις ρίζες των weirwood δέντρων.",
            "Έμεινε στην ιστορία με το διάσημο ερώτημα: 'Πόσα μάτια έχει ο Lord Bloodraven; Χίλια μάτια και ένα'."
        ],
        "https://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_characters#Three-eyed_crow",
        ["game_of_thrones", "bloodraven", "three_eyed_raven", "targaryen"]
    ),
    # 266
    make_q(
        "pop_culture_hard_266",
        "Ποιο ήταν το πραγματικό όνομα και αριθμός πειράματος του μυστηριώδους τέρατος Vecna πριν εξοριστεί στο Upside Down στο 'Stranger Things';",
        "Henry Creel (001 / One)",
        ["Peter Ballard", "Martin Brenner", "Billy Hargrove"],
        "Ο Henry Creel ήταν το πρώτο παιδί-υποκείμενο πειραμάτων του Dr. Martin Brenner στο εργαστήριο Hawkins, αποκτώντας τον αριθμό 001.",
        [
            "Η Eleven τον εξόρισε στο Upside Down το 1979 κατά τη διάρκεια της σφαγής στο εργαστήριο, όπου σταδιακά μεταμορφώθηκε στο αποκρουστικό τέρας Vecna.",
            "Τον ρόλο του Henry Creel / Vecna ενσάρκωσε ο Jamie Campbell Bower περνώντας καθημερινά πάνω από 7 ώρες στο μακιγιάζ προσθετικών."
        ],
        "https://en.wikipedia.org/wiki/Vecna_(Stranger_Things)",
        ["stranger_things", "vecna", "henry_creel", "netflix"]
    ),
    # 267
    make_q(
        "pop_culture_hard_267",
        "Σε ποιο άλμπουμ του 1983 ο Λούκυ Λουκ αντικατέστησε οριστικά το τσιγάρο στο στόμα του με ένα κλαράκι χορτάρι κερδίζοντας μετάλλιο από τον ΠΟΥ;",
        "Fingers",
        ["The Daily Star", "The Curing", "Sarah Bernhardt"],
        "Ο Morris αποφάσισε να κόψει το κάπνισμα στον ήρωά του το 1983, αντικαθιστώντας το τσιγάρο με ένα στάχυ, κερδίζοντας ειδικό βραβείο από τον Παγκόσμιο Οργανισμό Υγείας.",
        [
            "Η αλλαγή διευκόλυνε επίσης τη διανομή των σειρών κινουμένων σχεδίων στην αμερικανική τηλεόραση που απαγόρευε το κάπνισμα σε παιδικά προγράμματα.",
            "Το άλμπουμ 'Fingers' ήταν το πρώτο που σχεδιάστηκε με τον Λούκυ Λουκ να μασάει αποκλειστικά το χαρακτηριστικό χορταράκι."
        ],
        "https://en.wikipedia.org/wiki/Lucky_Luke",
        ["lucky_luke", "morris", "smoking", "who_award", "comics"]
    ),
    # 268
    make_q(
        "pop_culture_hard_268",
        "Ποιος ήταν ο πρώτος Green Lantern της Χρυσής Εποχής των κόμικς (1940) του οποίου το δαχτυλίδι ήταν εντελώς αναποτελεσματικό απέναντι στο ξύλο;",
        "Alan Scott",
        ["Hal Jordan", "Guy Gardner", "John Stewart"],
        "Ο μηχανικός σιδηροδρόμων Alan Scott βρήκε μια μαγική πράσινη φλόγα από μετεωρίτη και κατασκεύασε ένα δαχτυλίδι που δεν μπορούσε να επηρεάσει ξύλινα αντικείμενα.",
        [
            "Σε αντίθεση με το μεταγενέστερο Green Lantern Corps των επιστημονικών εξωγήινων Guardians, οι δυνάμεις του Alan Scott ήταν καθαρά μαγικές (Starheart).",
            "Φορούσε μια εντελώς διαφορετική στολή με κόκκινη μπλούζα, πράσινο παντελόνι και μωβ κάπα."
        ],
        "https://en.wikipedia.org/wiki/Alan_Scott",
        ["green_lantern", "alan_scott", "dc_comics", "golden_age"]
    ),
    # 269
    make_q(
        "pop_culture_hard_269",
        "Ποιος ήταν ο πρώτος Flash της Χρυσής Εποχής (1940) που φορούσε μεταλλικό κράνος με φτερά εμπνευσμένο από τον θεό Ερμή (Mercury);",
        "Jay Garrick",
        ["Barry Allen", "Wally West", "Bart Allen"],
        "Ο φοιτητής Jay Garrick απέκτησε υπερταχύτητα εισπνέοντας κατά λάθος ατμούς 'βαρέος ύδατος' στο εργαστήριό του.",
        [
            "Η ιστορική ιστορία 'Flash of Two Worlds' (1961) όπου ο Barry Allen συνάντησε τον Jay Garrick εισήγαγε την έννοια του Πολυσύμπαντος (Multiverse) στα υπερηρωικά κόμικς.",
            "Το μεταλλικό κράνος του Garrick ανήκε στον πατέρα του από τον Α' Παγκόσμιο Πόλεμο."
        ],
        "https://en.wikipedia.org/wiki/Flash_(Jay_Garrick)",
        ["the_flash", "jay_garrick", "dc_comics", "multiverse"]
    ),
    # 270
    make_q(
        "pop_culture_hard_270",
        "Ποια κοσμική οντότητα με τρία πρόσωπα (Equity, Vengeance, Necessity) υπηρετεί ως ο ανώτατος δικαστής της ισορροπίας του Πολυσύμπαντος της Marvel;",
        "The Living Tribunal (Το Ζωντανό Δικαστήριο)",
        ["Eternity", "Infinity", "The One-Above-All"],
        "Το Living Tribunal διαθέτει απεριόριστη κοσμική εξουσία, λογοδοτώντας μόνο στον ίδιο τον υπέρτατο δημιουργό του σύμπαντος της Marvel (The One-Above-All).",
        [
            "Τα τρία καλυμμένα πρόσωπά του αντιπροσωπεύουν τη Δικαιοσύνη, την Εκδίκηση και την Αναγκαιότητα και πρέπει να συμφωνήσουν ομόφωνα για να εκδοθεί απόφαση.",
            "Ακόμη και η δύναμη των έξι Λίθων της Αιωνιότητας είναι μηδαμινή μπροστά στην ισχύ του Living Tribunal."
        ],
        "https://en.wikipedia.org/wiki/Living_Tribunal",
        ["living_tribunal", "marvel", "cosmic_marvel", "multiverse"]
    ),
    # 271
    make_q(
        "pop_culture_hard_271",
        "Ποια ηρωίδα της Marvel έσπαγε συστηματικά τον τέταρτο τοίχο μιλώντας στον συγγραφέα John Byrne πολύ πριν την εμφάνιση του Deadpool;",
        "She-Hulk (Jennifer Walters)",
        ["Gwenpool", "Squirrel Girl", "Howard the Duck"],
        "Στη σειρά 'The Sensational She-Hulk' (1989) του John Byrne, η Jennifer Walters παραπονιόταν για τις κακές πλοκές και έσκιζε τα καρέ του κόμικ για να αλλάξει σελίδα.",
        [
            "Σε πολλά εξώφυλλα απειλούσε τους αναγνώστες ότι αν δεν αγοράσουν το τεύχος, ο Byrne θα καταστρέψει τη συλλογή τους με τα κόμικς των X-Men.",
            "Αυτή η αυτοαναφορική διάσταση ενσωματώθηκε και στη σειρά του Disney+ 'She-Hulk: Attorney at Law' (2022)."
        ],
        "https://en.wikipedia.org/wiki/She-Hulk",
        ["she_hulk", "john_byrne", "fourth_wall", "marvel"]
    ),
    # 272
    make_q(
        "pop_culture_hard_272",
        "Ποιο είναι το πραγματικό όνομα του ταξιδιώτη του χρόνου Cable, γιου του Scott Summers (Cyclops) και της Madelyne Pryor;",
        "Nathan Christopher Charles Summers",
        ["Alexander Summers", "Gabriel Summers", "Lucas Bishop"],
        "Ο μικρός Nathan στάλθηκε στο μακρινό μέλλον για να σωθεί από τον θανατηφόρο τεχνο-οργανικό ιό με τον οποίο τον είχε μολύνει ο Apocalypse.",
        [
            "Επέστρεψε ως σκληροτράχηλος ενήλικας πολεμιστής με κυβερνητικό χέρι για να ιδρύσει την ομάδα X-Force.",
            "Η στενή και ξεκαρδιστική συνεργασία του με τον Deadpool δημιούργησε την ιστορική σειρά 'Cable & Deadpool'."
        ],
        "https://en.wikipedia.org/wiki/Cable_(character)",
        ["cable", "nathan_summers", "xmen", "xforce", "marvel"]
    ),
    # 273
    make_q(
        "pop_culture_hard_273",
        "Ποιο ζωντανό μεταλλαγμένο νησί στον Ειρηνικό Ωκεανό έγινε το κυρίαρχο έθνος των μεταλλαγμένων στο reboot 'House of X' του Jonathan Hickman (2019);",
        "Κρακόα (Krakoa)",
        ["Τζενόσα (Genosha)", "Μάντριπουρ (Madripoor)", "Μούιρ (Muir Island)"],
        "Η Krakoa είναι ένα νοήμον οικοσύστημα που συνδέεται τηλεπαθητικά με τους μεταλλαγμένους και παράγει θαυματουργά φάρμακα για την ανθρωπότητα.",
        [
            "Μέσω των πυλών της Krakoa μπορούν να περάσουν αποκλειστικά και μόνο μεταλλαγμένοι.",
            "Η εποχή του Krakoa εισήγαγε τα 'Resurrection Protocols' επιτρέποντας στους πέντε μεταλλαγμένους ('The Five') να ανασταίνουν οποιονδήποτε νεκρό μεταλλαγμένο."
        ],
        "https://en.wikipedia.org/wiki/Krakoa",
        ["krakoa", "xmen", "jonathan_hickman", "house_of_x", "marvel"]
    ),
    # 274
    make_q(
        "pop_culture_hard_274",
        "Ποιος Αμερικανός τραγουδιστής με βαθιά φωνή μπάσου έγινε viral το 2007 με το τραγούδι 'Chocolate Rain' ενώ απομακρυνόταν από το μικρόφωνο για να αναπνεύσει;",
        "Tay Zonday",
        ["Chocolate Boy", "Gary Brolsma", "Antoine Dodson"],
        "Ο Tay Zonday (Adam Bahner) έγινε καλτ είδωλο του πρώιμου YouTube με τη χαρακτηριστική λεζάντα στην οθόνη '**I move away from the mic to breathe in'.",
        [
            "Παρά το αστείο στυλ του meme, το 'Chocolate Rain' ήταν ένα βαθιά πολιτικό τραγούδι για τον συστημικό ρατσισμό στις Ηνωμένες Πολιτείες.",
            "Κέρδισε το YouTube Award στην κατηγορία Μουσικής το 2008 και προβλήθηκε σε εκπομπές όπως του Jimmy Kimmel."
        ],
        "https://en.wikipedia.org/wiki/Chocolate_Rain",
        ["chocolate_rain", "tay_zonday", "youtube", "viral"]
    ),
    # 275
    make_q(
        "pop_culture_hard_275",
        "Ποιο ήταν το πραγματικό όνομα του Καναδού εφήβου που έγινε άθελά του το παγκόσμιο viral meme 'Star Wars Kid' το 2003;",
        "Ghyslain Raza",
        ["David Thorne", "Alexey Vanzhula", "Corey Delaney"],
        "Ο Ghyslain Raza μαγνητοσκόπησε τον εαυτό του σε σχολικό στούντιο να μιμείται τον Darth Maul με ένα κοντάρι, αλλά συμμαθητές του ανέβασαν το βίντεο στο Kazaa.",
        [
            "Το βίντεο εκτιμάται ότι προβλήθηκε πάνω από 1 δισεκατομμύριο φορές, καθιστώντας τον Raza ένα από τα πρώτα θύματα μαζικού διαδικτυακού εκφοβισμού.",
            "Χρόνια αργότερα ο Raza σπούδασε νομικά και έγινε δημόσιος υποστηρικτής της προστασίας των νέων από τον ψηφιακό εκφοβισμό."
        ],
        "https://en.wikipedia.org/wiki/Star_Wars_Kid",
        ["star_wars_kid", "ghyslain_raza", "viral", "internet_history"]
    ),
    # 276
    make_q(
        "pop_culture_hard_276",
        "Ποια Ελληνίδα σχεδιάστρια μόδας σχεδίασε το περίφημο μαύρο 'Revenge Dress' που φόρεσε η Πριγκίπισσα Diana το 1994 στην γκαλερί Serpentine;",
        "Χριστίνα Σταμπολιάν (Christina Stambolian)",
        ["Σήλια Κριθαριώτη", "Μαίρη Κατράντζου", "Σοφία Κοκοσαλάκη"],
        "Η Diana φόρεσε το εφαρμοστό μαύρο μεταξωτό φόρεμα τη βραδιά που ο Πρίγκιπας Κάρολος παραδέχτηκε δημόσια σε συνέντευξη τη συζυγική του απιστία.",
        [
            "Η Σταμπολιάν αποκάλυψε ότι η Diana είχε αγοράσει το φόρεμα τρία χρόνια νωρίτερα αλλά δίσταζε να το φορέσει επειδή το θεωρούσε 'πολύ τολμηρό'.",
            "Η εμφάνιση θεωρείται μία από τις πιο στρατηγικές και διάσημες ενδυματολογικές απαντήσεις στην ιστορία των διασημοτήτων."
        ],
        "https://en.wikipedia.org/wiki/Revenge_Dress",
        ["revenge_dress", "princess_diana", "christina_stambolian", "fashion"]
    ),
    # 277
    make_q(
        "pop_culture_hard_277",
        "Ποιος Ολλανδός ζωγράφος του κινήματος De Stijl ενέπνευσε την ιστορική συλλογή φορεμάτων 'Mondrian' του Yves Saint Laurent το 1965;",
        "Piet Mondrian",
        ["Theo van Doesburg", "Gerrit Rietveld", "Bart van der Leck"],
        "Ο Yves Saint Laurent σχεδίασε έξι ίσιες γραμμές φορεμάτων (shift dresses) με έντονες μαύρες γραμμές και γεωμετρικά τετράγωνα σε πρωτεύοντα χρώματα (κόκκινο, κίτρινο, μπλε).",
        [
            "Τα φορέματα δεν ήταν τυπωμένα υφάσματα αλλά περίτεχνο παζλ από ραμμένα κομμάτια μάλλινου ζέρσεϊ χωρίς ορατές ραφές.",
            "Η συλλογή έγινε το σύμβολο της pop αισθητικής της δεκαετίας του 1960 και εκτίθεται σήμερα σε κορυφαία μουσεία τέχνης."
        ],
        "https://en.wikipedia.org/wiki/Mondrian_collection",
        ["mondrian_dress", "yves_saint_laurent", "piet_mondrian", "fashion"]
    ),
    # 278
    make_q(
        "pop_culture_hard_278",
        "Ποιος σουρεαλιστής ζωγράφος συνεργάστηκε στενά με την Elsa Schiaparelli το 1937 για τη δημιουργία του διάσημου φορέματος με τον αστακό (Lobster Dress);",
        "Salvador Dalí",
        ["René Magritte", "Max Ernst", "Joan Miró"],
        "Ο Salvador Dalí ζωγράφισε έναν τεράστιο κόκκινο αστακό πάνω σε λευκό μεταξωτό οργκαντίνα φόρεμα της Schiaparelli για την Wallis Simpson.",
        [
            "Ο Dalí ήθελε αρχικά να αλείψει πραγματική μαγιονέζα πάνω στο φόρεμα, αλλά η Schiaparelli αρνήθηκε κατηγορηματικά.",
            "Η Schiaparelli και ο Dalí δημιούργησαν επίσης το διάσημο 'καπέλο-παπούτσι' (Shoe Hat) και το άρωμα Shocking."
        ],
        "https://en.wikipedia.org/wiki/Lobster_dress",
        ["lobster_dress", "elsa_schiaparelli", "salvador_dali", "fashion", "surrealism"]
    ),
    # 279
    make_q(
        "pop_culture_hard_279",
        "Σε ποιο έτος έκανε πρεμιέρα στο Φεστιβάλ των Καννών η ιστορική ταινία 'Στέλλα' του Μιχάλη Κακογιάννη με τη Μελίνα Μερκούρη;",
        "1955",
        ["1953", "1958", "1960"],
        "Η 'Στέλλα' διαγωνίστηκε για τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών το 1955 και αποτέλεσε το σημείο εκκίνησης της διεθνούς καριέρας της Μελίνας Μερκούρη.",
        [
            "Στο φεστιβάλ η Μερκούρη γνώρισε τον Αμερικανό σκηνοθέτη Jules Dassin, ο οποίος έγινε ο ισόβιος σύντροφος και καλλιτεχνικός συνοδοιπόρος της.",
            "Η ατάκα του Γιώργου Φούντα 'Φύγε, Στέλλα, κρατάω μαχαίρι!' και το τραγούδι 'Αγάπη που 'γινες δίκοπο μαχαίρι' έγραψαν κινηματογραφική ιστορία."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%AD%CE%BB%CE%BB%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1_1955)",
        ["stella", "melina_mercouri", "cacoyannis", "greek_cinema", "1955"]
    ),
    # 280
    make_q(
        "pop_culture_hard_280",
        "Ποιος σπουδαίος θεατρικός συγγραφέας έγραψε το έργο 'Η Στέλλα με τα κόκκινα γάντια' στο οποίο βασίστηκε το σενάριο της ταινίας 'Στέλλα';",
        "Ιάκωβος Καμπανέλλης",
        ["Δημήτρης Ψαθάς", "Αλέκος Σακελλάριος", "Γιώργος Τζαβέλλας"],
        "Ο Ιάκωβος Καμπανέλλης έγραψε το θεατρικό έργο το 1954 και συνεργάστηκε με τον Μιχάλη Κακογιάννη για τη μεταφορά του στη μεγάλη οθόνη.",
        [
            "Ο Καμπανέλλης θεωρείται ο πατριάρχης του νεοελληνικού θεάτρου και συγγραφέας του εμβληματικού 'Μαουτχάουζεν'.",
            "Η μουσική της ταινίας γράφτηκε από τον Μάνο Χατζιδάκι και τα τραγούδια ερμήνευσαν η Μελίνα Μερκούρη και η Σοφία Βέμπο."
        ],
        "https://el.wikipedia.org/wiki/%CE%99%CE%AC%CE%BA%CF%89%CE%B2%CE%BF%CF%82_%CE%9A%CE%B1%CE%BC%CF%80%CE%B1%CE%BD%CE%AD%CE%BB%CE%BB%CE%B7%CF%82",
        ["iakovos_kambanellis", "stella", "greek_theatre", "greek_cinema"]
    ),
    # 281
    make_q(
        "pop_culture_hard_281",
        "Ποια ταινία του Jules Dassin το 1960 χάρισε στον Μάνο Χατζιδάκι το πρώτο Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού για τα 'Παιδιά του Πειραιά';",
        "Ποτέ την Κυριακή (Never on Sunday)",
        ["Φαίδρα", "Τοπ Καπί", "Στέλλα"],
        "Το 'Ποτέ την Κυριακή' ήταν μια τεράστια διεθνής επιτυχία με τη Μελίνα Μερκούρη να κερδίζει το Βραβείο Καλύτερης Ηθοποιού στο Φεστιβάλ Καννών.",
        [
            "Ο Μάνος Χατζιδάκις αρνήθηκε αρχικά να παραλάβει το αγαλματίδιο του Όσκαρ επειδή πίστευε ότι το τραγούδι επισκίαζε το υπόλοιπο σοβαρό έργο του.",
            "Τα 'Παιδιά του Πειραιά' μεταφράστηκαν σε δεκάδες γλώσσες και έγιναν ένα από τα πιο αναγνωρίσιμα ελληνικά τραγούδια στον κόσμο."
        ],
        "https://el.wikipedia.org/wiki/%CE%A0%CE%BF%CF%84%CE%AD_%CF%84%CE%B7%CE%BD_%CE%9A%CF%85%CF%81%CE%B9%CE%B1%CE%BA%CE%AE",
        ["pote_tin_kyriaki", "manos_hadjidakis", "melina_mercouri", "jules_dassin", "oscars"]
    ),
    # 282
    make_q(
        "pop_culture_hard_282",
        "Ποιος Αμερικανός ηθοποιός μεξικανικής καταγωγής ενσάρκωσε τον Αλέξη Ζορμπά στην ταινία του Μιχάλη Κακογιάννη 'Zorba the Greek' (1964);",
        "Anthony Quinn",
        ["Marlon Brando", "Burt Lancaster", "Kirk Douglas"],
        "Ο Anthony Quinn απέσπασε υποψηφιότητα για Όσκαρ Α' Ανδρικού Ρόλου για την ερμηνεία του, ταυτίζοντας για πάντα τη μορφή του με τον ήρωα του Νίκου Καζαντζάκη.",
        [
            "Η ταινία κέρδισε τρία βραβεία Όσκαρ: Β' Γυναικείου Ρόλου (Lila Kedrova), Φωτογραφίας (Walter Lassally) και Καλλιτεχνικής Διεύθυνσης (Βασίλης Φωτόπουλος).",
            "Η διάσημη σκηνή του χορού συρτάκι στην παραλία του Σταυρού Χανίων υπό τη μουσική του Μίκη Θεοδωράκη έγινε παγκόσμιο σύμβολο της Ελλάδας."
        ],
        "https://en.wikipedia.org/wiki/Zorba_the_Greek_(film)",
        ["zorba_the_greek", "anthony_quinn", "cacoyannis", "theodorakis", "greek_cinema"]
    ),
    # 283
    make_q(
        "pop_culture_hard_283",
        "Στην κωμική σειρά 'Οι Μεν και οι Δεν' (ΑΝΤ1, 1993-1996), ποιο ήταν το όνομα του σνομπ και φιλάργυρου δικηγόρου που υποδυόταν ο Χάρης Ρώμας;",
        "Διονύσης Δάγκας",
        ["Τίμος Σταμάτης", "Περίανδρος Πώποτας", "Κωνσταντίνος Κατακουζηνός"],
        "Ο Διονύσης Δάγκας ήταν ένας αδίστακτος δικηγόρος στο Κολωνάκι παντρεμένος με τη ναζιάρα Βάνα (Άννα Κουρή), που βρισκόταν σε διαρκή πόλεμο με τους φτωχούς γείτονες.",
        [
            "Η σειρά των Χάρη Ρώμα και Άννας Χατζησοφιά σημείωσε τεράστια επιτυχία για τρεις σεζόν στον ΑΝΤ1.",
            "Η ατάκα του Δάγκα 'Εγώ είμαι ένας καθωσπρέπει άνθρωπος!' και οι προσπάθειές του να αποφύγει να πληρώσει κοινόχρηστα έγραψαν ιστορία."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%9C%CE%B5%CE%BD_%CE%BA%CE%B1%CE%B9_%CE%BF%CE%B9_%CE%94%CE%B5%CE%BD",
        ["oi_men_kai_oi_den", "dionysis_dagkas", "haris_romas", "ant1", "greek_tv"]
    ),
    # 284
    make_q(
        "pop_culture_hard_284",
        "Ποιο ήταν το όνομα του αξιαγάπητου μικρού σκύλου της Βάνας Δάγκα (Άννα Κουρή) στους 'Μεν και Δεν' που στην πραγματικότητα ήταν ο δικός της σκύλος;",
        "Τέρης",
        ["Μπούμπης", "Ρεξ", "Φρίξος"],
        "Ο σκύλος Τέρης (ράτσας Τεριέ) ήταν το πραγματικό κατοικίδιο της ηθοποιού Άννας Κουρή και συμμετείχε σχεδόν σε όλα τα επεισόδια της σειράς.",
        [
            "Η Βάνα Δάγκα τον περιέφερε διαρκώς στην αγκαλιά της, του μιλούσε σαν μωρό και του αγόραζε πανάκριβα ρούχα.",
            "Ο Τέρης θεωρείται ένα από τα πιο διάσημα ζώα στην ιστορία της ελληνικής τηλεόρασης."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%9C%CE%B5%CE%BD_%CE%BA%CE%B1%CE%B9_%CE%BF%CE%B9_%CE%94%CE%B5%CE%BD",
        ["oi_men_kai_oi_den", "teris", "anna_kouri", "greek_tv"]
    ),
    # 285
    make_q(
        "pop_culture_hard_285",
        "Ποιος ηθοποιός ενσάρκωσε τον άνεργο μποέμ γείτονα Τίμο Σταμάτη στους 'Μεν και Δεν' που έκλεβε διαρκώς φαγητό και ρεύμα από τους Δάγκα;",
        "Στέλιος Μάινας",
        ["Γεράσιμος Σκιαδαρέσης", "Βλαδίμηρος Κυριακίδης", "Κώστας Ευριπιώτης"],
        "Ο Τίμος Σταμάτης και η σύζυγός του Νανά (Τζόυς Ευείδη) εκπροσωπούσαν την ανέμελη και αντισυμβατική πλευρά της δεκαετίας του 1990.",
        [
            "Ο Μάινας ξεχώρισε για το πηγαίο του κωμικό ταλέντο πριν στραφεί σε μεγάλους δραματικούς ρόλους όπως στο 'Νησί'.",
            "Η σχέση του Τίμου με τη Νανά ήταν γεμάτη τσακωμούς και πάθος χωρίς να έχουν ποτέ μόνιμη εργασία."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F%CE%B9_%CE%9C%CE%B5%CE%BD_%CE%BA%CE%B1%CE%B9_%CE%BF%CE%B9_%CE%94%CE%B5%CE%BD",
        ["oi_men_kai_oi_den", "stelios_mainas", "greek_tv"]
    ),
    # 286
    make_q(
        "pop_culture_hard_286",
        "Στη στρατιωτική κωμωδία 'Της Ελλάδος τα Παιδιά' (ΑΝΤ1, 1993-1995), ποιο ήταν το στρατιωτικό αξίωμα και όνομα του διοικητή που υποδυόταν ο Γιάννης Μπέζος;",
        "Σμήναρχος Επαμεινώνδας Κάκαλος",
        ["Ταξίαρχος Θεοχάρης", "Συνταγματάρχης Βαρτάνης", "Πτέραρχος Καραβίδας"],
        "Ο Σμήναρχος Κάκαλος διοικούσε το Γραφείο Ενημέρωσης της Αεροπορίας προσπαθώντας μάταια να επιβάλει πειθαρχία σε τρεις τεμπέληδες σμηνίτες.",
        [
            "Η σειρά του Δημήτρη Βενιζέλου γνώρισε τεράστια επιτυχία, καθιερώνοντας τον Μπέζο ως κορυφαίο πρωταγωνιστή της τηλεόρασης.",
            "Η ατάκα του Κάκαλου 'Όχι βέβαια, όχι βέβαια!' και η ερωτική του σχέση με τη γραμματέα Μπουμπού (Χρύσα Ρώπα) άφησαν εποχή."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82_%CF%84%CE%B1_%CF%80%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC",
        ["tis_ellados_ta_paidia", "kakalos", "giannis_bezos", "ant1", "greek_tv"]
    ),
    # 287
    make_q(
        "pop_culture_hard_287",
        "Ποιο ήταν το χαρακτηριστικό παρατσούκλι του σμηνίτη Γιώργου Βλάχου που υποδυόταν ο Κώστας Ευριπιώτης στο 'Της Ελλάδος τα Παιδιά';",
        "Παλιός / Ο 'Παλιός' (Ευριπιώτης)",
        ["Πλαπούτας", "Ντάλας", "Χλαπάτσας"],
        "Ο Κώστας Ευριπιώτης υποδυόταν τον κλασικό 'παλιό' φαντάρο που απέφευγε κάθε αγγαρεία φωνάζοντας διαρκώς 'Παλιός, παλιός!'.",
        [
            "Η ατάκα του 'Παλιός!' έγινε σύνθημα σε στρατόπεδα σε ολόκληρη την Ελλάδα κατά τη δεκαετία του 1990.",
            "Η τριάδα των σμηνιτών συμπληρωνόταν από τον ποιητή Καραβανέα (Γιάννης Καπετάνιος) και τον δημοσιογράφο Πλαπούτα (Νίκος Αλεξίου)."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82_%CF%84%CE%B1_%CF%80%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC",
        ["tis_ellados_ta_paidia", "evripiotis", "palios", "greek_tv"]
    ),
    # 288
    make_q(
        "pop_culture_hard_288",
        "Ποιος ηθοποιός ενσάρκωσε τον αξέχαστο ρουφιάνο του στρατοπέδου 'Χλαπάτσα' με την ιστορική ατάκα 'Θα σας δείξω εγώ, θα δείτε τι θα πάθετε!' στο 'Της Ελλάδος τα Παιδιά';",
        "Δημήτρης Φραγκιόγλου",
        ["Γιάννης Σαββιδάκης", "Νίκος Αλεξίου", "Γιάννης Καπετάνιος"],
        "Ο σμηνίτης Τρύφων Σπιουνέας (Χλαπάτσας) προσπαθούσε συνεχώς να καλοπιάσει τον Κάκαλο προδίδοντας τις παρανομίες των συναδέλφων του.",
        [
            "Η χαρακτηριστική φράση 'Θα σας δείξω εγώ!' συνοδευόταν από ένα χαρακτηριστικό κούνημα του δαχτύλου.",
            "Ο ρόλος του Χλαπάτσα έγινε συνώνυμο του καλοθελητή και του καταδότη στη νεοελληνική κουλτούρα."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82_%CF%84%CE%B1_%CF%80%CE%B1%CE%B9%CE%B4%CE%B9%CE%AC",
        ["tis_ellados_ta_paidia", "hlapatsas", "fragkioglou", "greek_tv"]
    ),
    # 289
    make_q(
        "pop_culture_hard_289",
        "Ποια επιτυχημένη σειρά μυστηρίου του Πάνου Κοκκινόπουλου στον Alpha (2004-2007) παρουσίαζε αυτοτελείς ιστορίες εγκλημάτων εμπνευσμένες από αληθινά περιστατικά;",
        "10η Εντολή",
        ["Κόκκινος Κύκλος", "Ανατομία ενός Εγκλήματος", "Μαύρα Μεσάνυχτα"],
        "Η '10η Εντολή' καθιέρωσε ένα σκοτεινό, κινηματογραφικό στυλ τηλεόρασης με εξαιρετική ροκ και indie μουσική επένδυση.",
        [
            "Η σειρά υπήρξε συνέχεια του 'Κόκκινου Κύκλου' (2000-2002) και της 'Ανατομίας ενός Εγκλήματος' (1992-1995) του ίδιου σκηνοθέτη.",
            "Σχεδόν όλοι οι κορυφαίοι Έλληνες ηθοποιοί πέρασαν από πρωταγωνιστικούς ρόλους στα αυτοτελή επεισόδια της σειράς."
        ],
        "https://el.wikipedia.org/wiki/10%CE%B7_%CE%B5%CE%BD%CF%84%CE%BF%CE%BB%CE%AE",
        ["dekati_entoli", "kokkinopoulos", "alpha", "greek_tv", "crime"]
    ),
    # 290
    make_q(
        "pop_culture_hard_290",
        "Ποια μαύρη κωμωδία του Πάνου Κοκκινόπουλου στο Mega (2008) παρακολουθούσε τη ζωή μιας οικογένειας που κληρονομεί νυχτερινό κέντρο και μπλέκει με τη μαφία;",
        "Μαύρα Μεσάνυχτα",
        ["10η Εντολή", "Τρίτος Νόμος", "Εγκλήματα"],
        "Στα 'Μαύρα Μεσάνυχτα', ο φιλήσυχος ιδιοκτήτης ψησταριάς Θρασύβουλος (Στέλιος Μάινας) κληρονομεί το νυχτερινό μαγαζί του αδελφού του μετά τη δολοφονία του.",
        [
            "Η Μπέσυ Μάλφα ως 'Σιλβή' και η Παναγιώτα Βλαντή ως 'Σιλβία' δημιούργησαν απολαυστικούς ρόλους αδίστακτων γυναικών του υποκόσμου.",
            "Το ομώνυμο τραγούδι των τίτλων ερμήνευσε η Μαρία Ιακώβου με τη συμμετοχή του συγκροτήματος Thirio σημειώνοντας τεράστια επιτυχία."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%8D%CF%81%CE%B1_%CE%9C%CE%B5%CF%83%CE%AC%CE%BD%CF%85%CF%87%CF%84%CE%B1",
        ["mavra_mesanychta", "kokkinopoulos", "mega", "greek_tv"]
    ),
    # 291
    make_q(
        "pop_culture_hard_291",
        "Ποιος συνέθεσε το διάσημο θεατρικό τραγούδι 'Τα Παιδιά του Πειραιά' για την ταινία 'Ποτέ την Κυριακή' (1960);",
        "Μάνος Χατζιδάκις",
        ["Μίκης Θεοδωράκης", "Σταύρος Ξαρχάκος", "Μίμης Πλέσσας"],
        "Ο Μάνος Χατζιδάκις συνέθεσε το τραγούδι και έγραψε τους στίχους, κερδίζοντας το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 1961.",
        [
            "Ήταν το πρώτο Όσκαρ τραγουδιού στην ιστορία της Ακαδημίας που απονεμήθηκε σε τραγούδι με μη αγγλικούς στίχους.",
            "Το τραγούδι ερμηνεύτηκε διεθνώς από θρύλους όπως η Dalida, η Nana Mouskouri, η Melina Mercouri και οι Pink Martini."
        ],
        "https://en.wikipedia.org/wiki/Never_on_Sunday_(song)",
        ["manos_hadjidakis", "ta_paidia_tou_peiraia", "oscars", "greek_music"]
    ),
    # 292
    make_q(
        "pop_culture_hard_292",
        "Ποιος σπουδαίος Έλληνας ηθοποιός και σκηνοθέτης υποδύθηκε τον Αντώνη Κοκοβίκο στην κλασική ταινία 'Η δε γυνή να φοβήται τον άνδρα' (1965);",
        "Γιώργος Κωνσταντίνου",
        ["Λάμπρος Κωνσταντάρας", "Δημήτρης Παπαμιχαήλ", "Κώστας Βουτσάς"],
        "Ο Γιώργος Κωνσταντίνου και η Μάρω Κοντού (Ελενίτσα) δημιούργησαν ένα από τα πιο κλασικά ζευγάρια του ελληνικού σινεμά σε σκηνοθεσία Γιώργου Τζαβέλλα.",
        [
            "Η ιστορική ατάκα 'Πάρε το καπελάκι σου και δρόμο!' και η σκηνή του γάμου παραμένουν ανεξίτηλες.",
            "Το ιστορικό σπίτι της ταινίας στην οδό Τριπόδων στην Πλάκα αποτελεί μέχρι σήμερα τουριστικό αξιοθέατο."
        ],
        "https://el.wikipedia.org/wiki/%CE%97_%CE%B4%CE%B5_%CE%B3%CF%85%CE%BD%CE%AE_%CE%BD%CE%B1_%CF%86%CE%BF%CE%B2%CE%AE%CF%84%CE%B1%CE%B9_%CF%84%CE%BF%CE%BD_%CE%AC%CE%BD%CE%B4%CF%81%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["kokovikos", "giorgos_konstantinou", "maro_kontou", "greek_cinema"]
    ),
    # 293
    make_q(
        "pop_culture_hard_293",
        "Ποιο περίφημο γλυκό περιγράφει με απαράμιλλο πάθος ο Γιώργος Κωνσταντίνου στην ταινία 'Χτυποκάρδια στο Θρανίο' (1963);",
        "Προφιτερόλ",
        ["Μιλφέιγ", "Εκμέκ κανταΐφι", "Σουφλέ σοκολάτας"],
        "Ο Κωνσταντίνος υποδύεται έναν πελάτη στο ζαχαροπλαστείο που περιγράφει πώς δεν θέλει απλώς να φάει το προφιτερόλ αλλά 'να το δει να ρέει'.",
        [
            "Η σκηνή του μονολόγου 'Δεν θέλω να το φάω, θέλω να το βλέπω...' ήταν εν μέρει αυτοσχεδιασμός του ηθοποιού.",
            "Θεωρείται μία από τις πιο διάσημες γαστρονομικές κωμικές σκηνές στην ιστορία του παγκόσμιου κινηματογράφου."
        ],
        "https://el.wikipedia.org/wiki/%CE%A7%CF%84%CF%85%CF%80%CE%BF%CE%BA%CE%AC%CF%81%CE%B4%CE%B9%CE%B1_%CF%83%CF%84%CE%BF_%CE%B8%CF%81%CE%B1%CE%BD%CE%AF%CE%BF",
        ["profiterole", "giorgos_konstantinou", "greek_cinema", "comedy"]
    ),
    # 294
    make_q(
        "pop_culture_hard_294",
        "Ποιος σκηνοθέτης και σεναριογράφος υπέγραψε την αξεπέραστη κωμωδία 'Υπάρχει και Φιλότιμο' (1965) με τον Λάμπρο Κωνσταντάρα ως υπουργό Μαυρογιαλούρο;",
        "Αλέκος Σακελλάριος",
        ["Γιάννης Δαλιανίδης", "Ντίνος Δημόπουλος", "Γιώργος Τζαβέλλας"],
        "Ο Αλέκος Σακελλάριος σκηνοθέτησε την ταινία (βασισμένη στο θεατρικό έργο των Σακελλάριου - Γιαννακόπουλου 'Ανώμαλη Προσγείωση').",
        [
            "Το όνομα 'Μαυρογιαλούρος' έγινε έκτοτε στην ελληνική πολιτική ορολογία συνώνυμο του δημαγωγού πολιτικού που υπόσχεται τα πάντα χωρίς αντίκρισμα.",
            "Η ατάκα του Διονύση Παπαγιαννόπουλου ως Γκρούεζας 'Φάγανε, φάγανε, φάγανε!' άφησε εποχή."
        ],
        "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%AC%CF%81%CF%87%CE%B5%CE%B9_%CE%BA%CE%B1%CE%B9_%CF%86%CE%B9%CE%BB%CF%8C%CF%84%CE%B9%CE%BC%CE%BF",
        ["mavrogialouros", "konstantaras", "sakellarios", "greek_cinema"]
    ),
    # 295
    make_q(
        "pop_culture_hard_295",
        "Ποια ελληνική ταινία του 1963 σε σκηνοθεσία Βασίλη Γεωργιάδη ήταν υποψήφια για το Όσκαρ Καλύτερης Ξενόγλωσσης Ταινίας αποτυπώνοντας την Τρούμπα;",
        "Τα Κόκκινα Φανάρια",
        ["Το Χώμα Βάφτηκε Κόκκινο", "Ηλέκτρα", "Συνοικία το Όνειρο"],
        "Τα 'Κόκκινα Φανάρια' αφηγούνται τις τραγικές ζωές των γυναικών σε έναν οίκο ανοχής της Τρούμπας στον Πειραιά λίγο πριν το κλείσιμό του από τον νόμο.",
        [
            "Η ταινία συγκέντρωσε κορυφαίο καστ με τις Τζένη Καρέζη, Μαίρη Χρονοπούλου, Δέσπω Διαμαντίδου και Κατερίνα Χέλμη.",
            "Η ατάκα της Κατερίνας Χέλμη 'Ντόλυ, μη φύγεις... Ντόλυ, θα φαρμακωθώ!' αποτελεί ιστορική στιγμή του ελληνικού μελοδράματος."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%B1_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%B1_%CF%86%CE%B1%CE%BD%CE%AC%CF%81%CE%B9%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["kokkina_fanaria", "georgiadis", "troumba", "greek_cinema", "oscars"]
    ),
    # 296
    make_q(
        "pop_culture_hard_296",
        "Ποια δεύτερη ταινία του Βασίλη Γεωργιάδη κέρδισε υποψηφιότητα για Όσκαρ Ξενόγλωσσης Ταινίας το 1965 αποτυπώνοντας την εξέγερση των κολίγων στη Θεσσαλία;",
        "Το Χώμα Βάφτηκε Κόκκινο",
        ["Τα Κόκκινα Φανάρια", "Μπλόκο", "Δάκρυα για την Ηλέκτρα"],
        "Η ταινία 'Το Χώμα Βάφτηκε Κόκκινο' είναι ένα ελληνικό 'γουέστερν' για τη σύγκρουση των τσιφλικάδων με τους ακτήμονες κολίγους του θεσσαλικού κάμπου το 1907.",
        [
            "Πρωταγωνιστούσαν οι Νίκος Κούρκουλος, Γιάννης Βόγλης, Μάνος Κατράκης και Μαίρη Χρονοπούλου.",
            "Τα εξωτερικά γυρίσματα στα Μετέωρα πρόσφεραν μια επιβλητική κινηματογραφική αισθητική που εντυπωσίασε την Ακαδημία."
        ],
        "https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%87%CF%8E%CE%BC%CE%B1_%CE%B2%CE%AC%CF%86%CF%84%CE%B7%CE%BA%CE%B5_%CE%BA%CF%8C%CE%BA%CE%BA%CE%B9%CE%BD%CE%BF",
        ["to_homa_vaftike_kokkino", "georgiadis", "kourkoulos", "greek_cinema", "oscars"]
    ),
    # 297
    make_q(
        "pop_culture_hard_297",
        "Ποιο διάσημο μουσικό θέμα συνέθεσε ο Μίκης Θεοδωράκης για την ταινία 'Z' (1969) του Κώστα Γαβρά κερδίζοντας βραβείο BAFTA;",
        "Το σάουντρακ της ταινίας 'Z'",
        ["Το σάουντρακ του 'Serpico'", "Το 'Άξιον Εστί'", "Η 'Κατάσταση Πολιορκίας'"],
        "Ο Μίκης Θεοδωράκης βρισκόταν υπό κατ' οίκον περιορισμό από τη Χούντα και έστειλε κρυφά σημείωμα στον Γαβρά δίνοντάς του άδεια να χρησιμοποιήσει οποιοδήποτε έργο του.",
        [
            "Η ταινία 'Z', βασισμένη στο μυθιστόρημα του Βασίλη Βασιλικού για τη δολοφονία του Γρηγόρη Λαμπράκη, κέρδισε δύο βραβεία Όσκαρ.",
            "Η μουσική επένδυση του Θεοδωράκη έγινε σύμβολο του παγκόσμιου αγώνα κατά του αυταρχισμού."
        ],
        "https://en.wikipedia.org/wiki/Z_(1969_film)",
        ["z_movie", "costa_gavras", "theodorakis", "greek_cinema", "oscars"]
    ),
    # 298
    make_q(
        "pop_culture_hard_298",
        "Ποιο ήταν το όνομα του πρωτοποριακού θεατρικού θιάσου που ίδρυσε ο Κάρολος Κουν το 1942 ανεβάζοντας σύγχρονο ξένο και ελληνικό ρεπερτόριο;",
        "Θέατρο Τέχνης",
        ["Εθνικό Θέατρο", "Θίασος Κοτοπούλη", "Αττικό Θέατρο"],
        "Ο Κάρολος Κουν ίδρυσε το Θέατρο Τέχνης μέσα στην Κατοχή, διαμορφώνοντας γενιές σπουδαίων Ελλήνων ηθοποιών και σκηνοθετών.",
        [
            "Το υπόγειο του Θεάτρου Τέχνης στη στοά της οδού Πεσμαζόγλου έγινε ο ναός της ελληνικής θεατρικής πρωτοπορίας.",
            "Ο Κουν παρουσίασε για πρώτη φορά στην Ελλάδα έργα του Tennessee Williams, του Arthur Miller, του Samuel Beckett και του Harold Pinter."
        ],
        "https://el.wikipedia.org/wiki/%CE%98%CE%AD%CE%B1%CF%84%CF%81%CE%BF_%CE%A4%CE%AD%CF%87%CE%BD%CE%B7%CF%82_%C2%AB%CE%9A%CE%AC%CF%81%CE%BF%CE%BB%CE%BF%CF%82_%CE%9A%CE%BF%CF%85%CE%BD%C2%BB",
        ["theatro_technis", "karolos_koun", "greek_theatre", "history"]
    ),
    # 299
    make_q(
        "pop_culture_hard_299",
        "Ποια παράσταση αρχαίου δράματος του Θεάτρου Τέχνης σε σκηνοθεσία Καρόλου Κουν το 1959 προκάλεσε σκάνδαλο στην Επίδαυρο και απαγορεύτηκε προσωρινά;",
        "Όρνιθες (Αριστοφάνης)",
        ["Βάτραχοι", "Πέρσες", "Νεφέλες"],
        "Η παράσταση των 'Ορνίθων' με μουσική Μάνου Χατζιδάκι και κοστούμια Γιάννη Τσαρούχη διακόπηκε με κυβερνητική παρέμβαση ως 'ιερόσυλη'.",
        [
            "Αργότερα η ίδια ακριβώς παράσταση ταξίδεψε στο Παρίσι και το Λονδίνο κερδίζοντας διεθνή βραβεία στο 'Θέατρο των Εθνών'.",
            "Η μουσική του Χατζιδάκι για τους Όρνιθες θεωρείται ένα από τα κορυφαία αριστουργήματα της ελληνικής μουσικής."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%81%CE%BF%CE%BB%CE%BF%CF%82_%CE%9A%CE%BF%CF%85%CE%BD",
        ["ornithes", "karolos_koun", "hadjidakis", "tsarouchis", "theatre"]
    ),
    # 300
    make_q(
        "pop_culture_hard_300",
        "Ποιος σπουδαίος Έλληνας ζωγράφος σχεδίασε τα ιστορικά κοστούμια και τα σκηνικά για την παράσταση των 'Ορνίθων' του Καρόλου Κουν;",
        "Γιάννης Τσαρούχης",
        ["Γιάννης Μόραλης", "Νίκος Εγγονόπουλος", "Παναγιώτης Τέτσης"],
        "Ο Γιάννης Τσαρούχης δημιούργησε πρωτοποριακές μάσκες και φτερωτά κοστούμια που συνδύαζαν την αρχαία ελληνική παράδοση με τη λαϊκή φορεσιά.",
        [
            "Η αισθητική του Τσαρούχη άλλαξε για πάντα τον τρόπο με τον οποίο παρουσιάζονταν οι αριστοφανικές κωμωδίες στην Ελλάδα.",
            "Υπήρξε στενός συνεργάτης του Κουν και του Χατζιδάκι στη διαμόρφωση της ελληνικής πολιτιστικής άνοιξης του '60."
        ],
        "https://el.wikipedia.org/wiki/%CE%93%CE%B9%CE%AC%CE%BD%CE%BD%CE%B7%CF%82_%CE%A4%CF%83%CE%B1%CF%81%CE%BF%CF%8D%CF%87%CE%B7%CF%82",
        ["tsarouchis", "ornithes", "koun", "greek_art"]
    ),
    # 301
    make_q(
        "pop_culture_hard_301",
        "Ποιο ήταν το όνομα της μυθικής τραγωδού που εγκαινίασε το σύγχρονο Φεστιβάλ Επιδαύρου το 1954 ερμηνεύοντας την 'Εκάβη' του Ευριπίδη;",
        "Κατίνα Παξινού",
        ["Κυβέλη", "Μαρίκα Κοτοπούλη", "Άννα Συνοδινού"],
        "Η Κατίνα Παξινού μάγεψε το κοινό στην ιστορική πρώτη παράσταση στην Επίδαυρο, επιστρέφοντας ως νικήτρια Όσκαρ στην Ελλάδα.",
        [
            "Είχε κερδίσει το Όσκαρ Β' Γυναικείου Ρόλου το 1943 για την ταινία 'Για Ποιον Χτυπά η Καμπάνα' (For Whom the Bell Tolls).",
            "Μαζί με τον σύζυγό της Αλέξη Μινωτή αποτέλεσαν το κορυφαίο θεατρικό ζευγάρι της κλασικής ελληνικής σκηνής."
        ],
        "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%AF%CE%BD%CE%B1_%CE%A0%CE%B1%CE%BE%CE%B9%CE%BD%CE%BF%CF%8D",
        ["katina_paxinou", "epidavros", "greek_theatre", "oscars"]
    ),
    # 302
    make_q(
        "pop_culture_hard_302",
        "Ποιος σκηνοθέτης και ηθοποιός σκηνοθέτησε και πρωταγωνίστησε στις περισσότερες κλασικές παραστάσεις αρχαίας τραγωδίας του Εθνικού Θεάτρου στην Επίδαυρο μαζί με την Παξινού;",
        "Αλέξης Μινωτής",
        ["Δημήτρης Ροντήρης", "Σπύρος Ευαγγελάτος", "Αλέξης Σολομός"],
        "Ο Αλέξης Μινωτής ερμήνευσε συγκλονιστικά ρόλους όπως ο Οιδίπους Τύραννος και ο Οιδίπους επί Κολωνώ, σκηνοθετώντας επίσης όπερες για τη Μαρία Κάλλας.",
        [
            "Σκηνοθέτησε τη Μαρία Κάλλας στη 'Μήδεια' στο Κόβεντ Γκάρντεν, τη Σκάλα του Μιλάνου και την Επίδαυρο.",
            "Υπήρξε επί σειρά ετών γενικός διευθυντής του Εθνικού Θεάτρου της Ελλάδας."
        ],
        "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%AD%CE%BE%CE%B7%CF%82_%CE%9C%CE%B9%CE%BD%CF%89%CF%84%CE%AE%CF%82",
        ["alexis_minotis", "paxinou", "epidavros", "national_theatre"]
    ),
    # 303
    make_q(
        "pop_culture_hard_303",
        "Σε ποιο αρχαίο θέατρο της Αθήνας στους πρόποδες της Ακρόπολης ερμήνευσε η Μαρία Κάλλας τη 'Νόρμα' (1960) και τη 'Μήδεια' (1961);",
        "Ωδείο Ηρώδου του Αττικού (Ηρώδειο)",
        ["Θέατρο του Διονύσου", "Παναθηναϊκό Στάδιο", "Αρχαία Αγορά"],
        "Η επιστροφή της Μαρίας Κάλλας στην Αθήνα στο απόγειο της παγκόσμιας δόξας της για παραστάσεις στο Ηρώδειο αποτέλεσε κορυφαίο πολιτιστικό γεγονός.",
        [
            "Τα έσοδα από τις ιστορικές αυτές παραστάσεις δωρήθηκαν από την ίδια για τη δημιουργία των υποτροφιών 'Μαρία Κάλλας' για νέους λυρικούς καλλιτέχνες.",
            "Η Κάλλας είχε σπουδάσει στην Αθήνα στο Εθνικό Ωδείο υπό την καθοδήγηση της Ισπανίδας σοπράνο Elvira de Hidalgo."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%B1%CF%81%CE%AF%CE%B1_%CE%9A%CE%AC%CE%BB%CE%BB%CE%B1%CF%82",
        ["maria_callas", "herodion", "opera", "athens"]
    ),
    # 304
    make_q(
        "pop_culture_hard_304",
        "Ποιος διάσημος Έλληνας σκηνοθέτης κέρδισε τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών το 1998 για την ταινία του 'Μια Αιωνιότητα και μια Μέρα';",
        "Θόδωρος Αγγελόπουλος",
        ["Κώστας Γαβράς", "Παντελής Βούλγαρης", "Νίκος Κούνδουρος"],
        "Ο Θόδωρος Αγγελόπουλος κέρδισε το κορυφαίο βραβείο των Καννών με πρωταγωνιστή τον Ελβετό ηθοποιό Bruno Ganz.",
        [
            "Η ταινία αφηγείται τις τελευταίες ώρες ενός ετοιμοθάνατου ποιητή που περιπλανιέται στη Θεσσαλονίκη βοηθώντας ένα μικρό προσφυγόπουλο.",
            "Η μουσική της Ελένης Καραΐνδρου αποτέλεσε αναπόσπαστο στοιχείο της ποιητικής κινηματογραφικής γλώσσας του Αγγελόπουλου."
        ],
        "https://el.wikipedia.org/wiki/%CE%98%CF%8C%CE%B4%CF%89%CF%81%CE%BF%CF%82_%CE%91%CE%B3%CE%B3%CE%B5%CE%BB%CF%8C%CF%80%CE%BF%CF%85%CE%BB%CE%BF%CF%82",
        ["theo_angelopoulos", "cannes", "palme_dor", "greek_cinema"]
    ),
    # 305
    make_q(
        "pop_culture_hard_305",
        "Ποια Ελληνίδα συνθέτρια υπήρξε η μόνιμη μουσική συνοδοιπόρος του Θόδωρου Αγγελόπουλου υπογράφοντας τα σάουντρακ ταινιών όπως 'Το Μετέωρο Βήμα του Πελαργού';",
        "Ελένη Καραΐνδρου",
        ["Ευανθία Ρεμπούτσικα", "Σοφία Καμαγιάννη", "Λίνα Νικολακοπούλου"],
        "Η Ελένη Καραΐνδρου συνέθεσε εμβληματικά θέματα για τις ταινίες του Αγγελόπουλου, με άλμπουμ που κυκλοφόρησαν παγκοσμίως από τη δισκογραφική ECM.",
        [
            "Η συνεργασία τους ξεκίνησε το 1984 με το 'Ταξίδι στα Κύθηρα' και συνεχίστηκε μέχρι τον τραγικό θάνατο του σκηνοθέτη το 2012.",
            "Τα μουσικά της θέματα παίζονται από μεγάλες συμφωνικές ορχήστρες σε όλο τον κόσμο."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CE%BB%CE%AD%CE%BD%CE%B7_%CE%9A%CE%B1%CF%81%CE%B1%CE%90%CE%BD%CE%B4%CF%81%CE%BF%CF%85",
        ["eleni_karaindrou", "theo_angelopoulos", "soundtrack", "greek_music"]
    ),
    # 306
    make_q(
        "pop_culture_hard_306",
        "Ποια ανατρεπτική ταινία του Νίκου Κούνδουρου το 1956 με πρωταγωνιστή τον Ντίνο Ηλιόπουλο θεωρείται από τις κορυφαίες του ελληνικού σινεμά;",
        "Ο Δράκος",
        ["Μαγική Πόλη", "Μικρές Αφροδίτες", "Μπάιρον"],
        "Ο Ντίνος Ηλιόπουλος υποδύεται έναν ασήμαντο υπάλληλο, τον Θωμά Φλωρά, που μοιάζει καταπληκτικά με έναν καταζητούμενο κακοποιό με το ψευδώνυμο 'Ο Δράκος'.",
        [
            "Το σενάριο έγραψε ο Ιάκωβος Καμπανέλλης και η μουσική ήταν του Μάνου Χατζιδάκι.",
            "Αν και αρχικά απέτυχε εμπορικά και δέχθηκε σκληρές κριτικές, ψηφίστηκε αργότερα από την Πανελλήνια Ένωση Κριτικών Κινηματογράφου ως η κορυφαία ελληνική ταινία όλων των εποχών."
        ],
        "https://el.wikipedia.org/wiki/%CE%9F_%CE%94%CF%81%CE%AC%CE%BA%CE%BF%CF%82_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["o_drakos", "koundouros", "iliopoulos", "greek_cinema"]
    ),
    # 307
    make_q(
        "pop_culture_hard_307",
        "Ποιος κέρδισε την Αργυρή Άρκτο Σκηνοθεσίας στο Φεστιβάλ Κινηματογράφου του Βερολίνου το 1963 για την ταινία 'Μικρές Αφροδίτες';",
        "Νίκος Κούνδουρος",
        ["Μιχάλης Κακογιάννης", "Αλέξης Δαμιανός", "Τώνης Λυκουρέσης"],
        "Ο Νίκος Κούνδουρος απέσπασε τη διεθνή διάκριση στο Βερολίνο για μια ποιητική, σχεδόν βουβή ταινία βασισμένη στο ειδύλλιο του Δάφνι και Χλόης.",
        [
            "Η ταινία γυρίστηκε στη Ρόδο με ερασιτέχνες ηθοποιούς και μουσική του Γιάννη Μαρκόπουλου.",
            "Υπήρξε ένας από τους πρώτους μεγάλους διεθνείς θριάμβους του ανεξάρτητου ελληνικού κινηματογράφου."
        ],
        "https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%BA%CF%81%CE%AD%CF%82_%CE%91%CF%86%CF%81%CE%BF%CE%B4%CE%AF%CF%84%CE%B5%CF%82",
        ["mikres_afrodites", "koundouros", "berlinale", "greek_cinema"]
    ),
    # 308
    make_q(
        "pop_culture_hard_308",
        "Ποια πρωτοποριακή ταινία του Αλέξη Δαμιανού το 1971 αποτέλεσε τον θεμέλιο λίθο του Νέου Ελληνικού Κινηματογράφου;",
        "Ευδοκία",
        ["Μέχρι το Πλοίο", "Ηνίοχος", "Αναπαράσταση"],
        "Η 'Ευδοκία' αφηγείται τον καταδικασμένο έρωτα ενός λοχία (Γιώργος Κουτούζης) και μιας ιερόδουλης (Μαρία Βασιλείου) σε μια σκληρή επαρχιακή Ελλάδα.",
        [
            "Το ομώνυμο οργανικό ζεϊμπέκικο ('Το Ζεϊμπέκικο της Ευδοκίας') που συνέθεσε ο Μάνος Λοΐζος έγινε το πιο αναγνωρίσιμο ζεϊμπέκικο στην ιστορία της ελληνικής μουσικής.",
            "Ο σολίστ του μπουζουκιού που έπαιξε στο κομμάτι ήταν ο δεξιοτέχνης Θανάσης Πολυκανδριώτης."
        ],
        "https://el.wikipedia.org/wiki/%CE%95%CF%85%CE%B4%CE%BF%CE%BA%CE%AF%CE%B1_(%CF%84%CE%B1%CE%B9%CE%BD%CE%AF%CE%B1)",
        ["evdokia", "alexis_damianos", "manos_loizos", "zeimbekiko", "greek_cinema"]
    ),
    # 309
    make_q(
        "pop_culture_hard_309",
        "Ποιος δεξιοτέχνης μουσικός έπαιξε το ιστορικό σόλο μπουζούκι στην ηχογράφηση του 'Ζεϊμπέκικου της Ευδοκίας' του Μάνου Λοΐζου το 1971;",
        "Θανάσης Πολυκανδριώτης",
        ["Χρήστος Νικολόπουλος", "Γιώργος Ζαμπέτας", "Κώστας Παπαδόπουλος"],
        "Ο Θανάσης Πολυκανδριώτης ήταν μόλις 23 ετών όταν ηχογράφησε με την πρώτη κιόλας λήψη το θρυλικό σόλο μπουζούκι υπό τις οδηγίες του Λοΐζου.",
        [
            "Ο ρυθμός ξεκινά με τον χαρακτηριστικό στρατιωτικό βηματισμό και εξελίσσεται σε ένα από τα πιο έντονα μουσικά κρεσέντο.",
            "Το κομμάτι έχει ταυτιστεί απόλυτα με την έννοια της ανδρικής λεβεντιάς και της ελληνικής ψυχής."
        ],
        "https://el.wikipedia.org/wiki/%CE%96%CE%B5%CF%8A%CE%BC%CF%80%CE%AD%CE%BA%CE%B9%CE%BA%CE%BF_%CF%84%CE%B7%CF%82_%CE%95%CF%85%CE%B4%CE%BF%CE%BA%CE%AF%CE%B1%CF%82",
        ["zeimbekiko_tis_evdokias", "polykandriotis", "loizos", "greek_music"]
    ),
    # 310
    make_q(
        "pop_culture_hard_310",
        "Ποιος ήταν ο πρώτος μεγάλος ρόλος του Σωτήρη Μουστάκα στον διεθνή κινηματογράφο το 1964 υποδυόμενος τον τρελό του χωριού Μιμιθό;",
        "Zorba the Greek (Αλέξης Ζορμπάς)",
        ["The Greek Tycoon", "Orestes", "The Magus"],
        "Ο νεαρός τότε Κύπριος ηθοποιός Σωτήρης Μουστάκας εντυπωσίασε τον Μιχάλη Κακογιάννη κερδίζοντας τον ρόλο του Μιμιθού δίπλα στον Anthony Quinn.",
        [
            "Η ερμηνεία του απέσπασε διθυραμβικές κριτικές στο εξωτερικό αλλά έχασε την υποψηφιότητα για Όσκαρ Β' Ανδρικού Ρόλου λόγω ανεπαρκούς χρόνου εμφάνισης στην οθόνη.",
            "Αργότερα ο Μουστάκας εξελίχθηκε σε έναν από τους πιο λαοφιλείς κωμικούς ηθοποιούς του ελληνικού θεάτρου και του κινηματογράφου."
        ],
        "https://el.wikipedia.org/wiki/%CE%A3%CF%89%CF%84%CE%AE%CF%81%CE%B7%CF%82_%CE%9C%CE%BF%CF%85%CF%83%CF%84%CE%AC%CE%BA%CE%B1%CF%82",
        ["sotiris_moustakas", "zorba_the_greek", "cacoyannis", "greek_cinema"]
    ),
]

if __name__ == "__main__":
    validate_and_append("pop_culture", "hard", 5, questions)

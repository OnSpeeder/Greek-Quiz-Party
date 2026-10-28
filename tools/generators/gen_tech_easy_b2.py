# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# Batch 2: technology_easy_261 to technology_easy_310 (50 questions)
raw_questions = [
    {
        "id": "technology_easy_261",
        "text": "Ποιο πρότυπο καλωδίου και θύρας χρησιμοποιείται ευρέως για τη μεταφορά ψηφιακής εικόνας και ήχου υψηλής ευκρίνειας από υπολογιστές και κονσόλες σε τηλεοράσεις;",
        "correct": "HDMI",
        "distractors": ["VGA", "SCART", "RCA"],
        "explanation": "Το HDMI (High-Definition Multimedia Interface) επιτρέπει τη συνδυασμένη ψηφιακή μετάδοση ασυμπίεστου βίντεο και πολυκάναλου ήχου μέσω ενός μόνο καλωδίου.",
        "funFacts": [
            "Κυκλοφόρησε για πρώτη φορά στα τέλη του 2002 από κοινοπραξία εταιρειών όπως οι Sony, Philips και Panasonic.",
            "Αντικατέστησε τα παλαιότερα αναλογικά πρότυπα όπως το VGA και το SCART."
        ],
        "source": "https://el.wikipedia.org/wiki/HDMI",
        "tags": ["technology", "hardware", "hdmi", "cables"]
    },
    {
        "id": "technology_easy_262",
        "text": "Ποια διάσημη μορφή συμπίεσης ψηφιακού ήχου έφερε επανάσταση στη μουσική βιομηχανία τη δεκαετία του 1990 μειώνοντας δραστικά το μέγεθος των τραγουδιών;",
        "correct": "MP3",
        "distractors": ["WAV", "MIDI", "FLAC"],
        "explanation": "Το MP3 (MPEG-1 Audio Layer III) αναπτύχθηκε κυρίως από το γερμανικό ινστιτούτο Fraunhofer και χρησιμοποιεί ψυχοακουστική συμπίεση για να αφαιρεί ήχους που δεν ακούει το ανθρώπινο αυτί.",
        "funFacts": [
            "Το πρώτο τραγούδι που χρησιμοποιήθηκε για τη δοκιμή και βελτίωση του αλγορίθμου MP3 ήταν το 'Tom's Diner' της Suzanne Vega.",
            "Κατάφερε να μειώσει το μέγεθος ενός ασυμπίεστου αρχείου CD κατά περίπου 90% με ελάχιστη απώλεια αντιληπτής ποιότητας."
        ],
        "source": "https://el.wikipedia.org/wiki/MP3",
        "tags": ["technology", "audio", "mp3", "compression"]
    },
    {
        "id": "technology_easy_263",
        "text": "Πώς ονομάζεται το τυπικό καλώδιο με το βύσμα RJ-45 που χρησιμοποιείται για την ενσύρματη σύνδεση υπολογιστών σε τοπικό δίκτυο και ρούτερ;",
        "correct": "Καλώδιο Ethernet",
        "distractors": ["Καλώδιο ομοαξονικό", "Καλώδιο DVI", "Καλώδιο SATA"],
        "explanation": "Το καλώδιο Ethernet (συνήθως συνεστραμμένου ζεύγους Cat5e, Cat6 ή Cat7) παρέχει σταθερή και υψηλής ταχύτητας ενσύρματη σύνδεση δικτύου.",
        "funFacts": [
            "Η τεχνολογία Ethernet εφευρέθηκε το 1973 από τον Robert Metcalfe στο ιστορικό ερευνητικό κέντρο Xerox PARC.",
            "Σε αντίθεση με το Wi-Fi, η ενσύρματη σύνδεση Ethernet δεν επηρεάζεται από τοίχους ή παρεμβολές άλλων ασύρματων συσκευών."
        ],
        "source": "https://el.wikipedia.org/wiki/Ethernet",
        "tags": ["technology", "networking", "ethernet", "hardware"]
    },
    {
        "id": "technology_easy_264",
        "text": "Ποιο ήταν το αρχικό όριο χαρακτήρων ανά ανάρτηση (tweet) όταν ξεκίνησε η πλατφόρμα Twitter το 2006;",
        "correct": "140 χαρακτήρες",
        "distractors": ["70 χαρακτήρες", "280 χαρακτήρες", "500 χαρακτήρες"],
        "explanation": "Το Twitter έθεσε αρχικά το όριο στους 140 χαρακτήρες ώστε κάθε tweet να χωράει ολόκληρο σε ένα κλασικό μήνυμα SMS (που είχε όριο 160 χαρακτήρες), αφήνοντας 20 χαρακτήρες για το όνομα χρήστη.",
        "funFacts": [
            "Το 2017 το όριο διπλασιάστηκε στους 280 χαρακτήρες για τις περισσότερες γλώσσες.",
            "Το πρώτο tweet στην ιστορία στάλθηκε στις 21 Μαρτίου 2006 από τον συνιδρυτή Jack Dorsey και έγραφε: 'just setting up my twttr'."
        ],
        "source": "https://el.wikipedia.org/wiki/Twitter",
        "tags": ["technology", "twitter", "social_media", "internet"]
    },
    {
        "id": "technology_easy_265",
        "text": "Με ποιο επιχειρηματικό μοντέλο ξεκίνησε η συνδρομητική υπηρεσία Netflix όταν ιδρύθηκε το 1997;",
        "correct": "Ταχυδρομική ενοικίαση ταινιών σε DVD",
        "distractors": ["Ζωντανές μεταδόσεις αθλητικών αγώνων", "Πώληση εισιτηρίων κινηματογράφου", "Παραγωγή κασετών VHS"],
        "explanation": "Το Netflix ιδρύθηκε από τους Reed Hastings και Marc Randolph ως πρωτοποριακή υπηρεσία ενοικίασης DVD μέσω ταχυδρομείου χωρίς πρόστιμα καθυστέρησης, πριν εισαγάγει το streaming το 2007.",
        "funFacts": [
            "Το 2000 οι ιδρυτές του Netflix πρότειναν στην αλυσίδα Blockbuster να την εξαγοράσει για 50 εκατομμύρια δολάρια, αλλά η πρόταση απορρίφθηκε περιφρονητικά.",
            "Σήμερα το Netflix διαθέτει πάνω από 260 εκατομμύρια συνδρομητές παγκοσμίως."
        ],
        "source": "https://el.wikipedia.org/wiki/Netflix",
        "tags": ["technology", "netflix", "streaming", "history"]
    },
    {
        "id": "technology_easy_266",
        "text": "Τι απεικονίζει η πασίγνωστη πράσινη μασκότ του λειτουργικού συστήματος Android της Google;",
        "correct": "Ένα μικρό πράσινο ρομπότ",
        "distractors": ["Ένα μήλο", "Έναν πιγκουίνο", "Μια αλεπού"],
        "explanation": "Η μασκότ του Android, γνωστή ως 'Bugdroid' ή 'the Android robot', σχεδιάστηκε το 2007 από την Irina Blok στην Google.",
        "funFacts": [
            "Η Blok εμπνεύστηκε τη σχεδίαση από τα απλά παγκόσμια εικονογράμματα ανδρών και γυναικών στις πόρτες των δημόσιων τουαλετών.",
            "Το λογότυπο διατέθηκε εσκεμμένα υπό άδεια Creative Commons ώστε ο καθένας να μπορεί να το προσαρμόζει ελεύθερα."
        ],
        "source": "https://en.wikipedia.org/wiki/Android_(operating_system)",
        "tags": ["technology", "google", "android", "design"]
    },
    {
        "id": "technology_easy_267",
        "text": "Ποιος Βρετανός επιστήμονας υπολογιστών εφηύρε τον Παγκόσμιο Ιστό (World Wide Web) το 1989 όσο εργαζόταν στο CERN;",
        "correct": "Tim Berners-Lee",
        "distractors": ["Alan Turing", "Vint Cerf", "Linus Torvalds"],
        "explanation": "Ο Sir Tim Berners-Lee επινόησε το πρωτόκολλο HTTP, τη γλώσσα HTML, τις διευθύνσεις URI/URL και έστησε τον πρώτο web server και browser στον κόσμο.",
        "funFacts": [
            "Ο πρώτος ιστότοπος στον κόσμο φιλοξενήθηκε σε έναν υπολογιστή NeXT στο CERN και είχε διεύθυνση info.cern.ch.",
            "Ο Berners-Lee επέμεινε να προσφερθεί η τεχνολογία του Παγκόσμιου Ιστού εντελώς ελεύθερα και χωρίς δικαιώματα εκμετάλλευσης (royalty-free)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B9%CE%BC_%CE%9C%CF%80%CE%AD%CF%81%CE%BD%CE%B5%CF%81%CF%82_%CE%9B%CE%B9",
        "tags": ["technology", "internet", "world_wide_web", "pioneers"]
    },
    {
        "id": "technology_easy_268",
        "text": "Τι σημαίνουν τα αρχικά του όρου URL που χρησιμοποιούμε για να αναφερθούμε σε μια διεύθυνση ιστοσελίδας;",
        "correct": "Uniform Resource Locator",
        "distractors": ["Universal Radio Link", "Unified Routing Level", "User Request Line"],
        "explanation": "Το URL (Ενιαίος Εντοπιστής Πόρων) προσδιορίζει τη μοναδική διεύθυνση και το πρωτόκολλο πρόσβασης ενός πόρου στο διαδίκτυο.",
        "funFacts": [
            "Κάθε URL αποτελείται από το πρωτόκολλο (π.χ. https), το όνομα τομέα (domain name) και συχνά μια συγκεκριμένη διαδρομή αρχείου.",
            "Ο δημιουργός του Tim Berners-Lee εξέφρασε αργότερα τη μεταμέλειά του για τις δύο περιττές καθέτους (//) μετά το http: λέγοντας ότι θα μπορούσαν να είχαν παραλειφθεί εξοικονομώντας χρόνο."
        ],
        "source": "https://el.wikipedia.org/wiki/URL",
        "tags": ["technology", "internet", "web", "url"]
    },
    {
        "id": "technology_easy_269",
        "text": "Ποια τεχνολογία οθόνης αφής χρησιμοποιείται στα σύγχρονα smartphones και ανταποκρίνεται στο ηλεκτρικό φορτίο των δαχτύλων;",
        "correct": "Χωρητική οθόνη αφής (Capacitive)",
        "distractors": ["Αντιστατική οθόνη (Resistive)", "Υπέρυθρη οθόνη (Infrared)", "Ηχοκυματική οθόνη (SAW)"],
        "explanation": "Οι χωρητικές οθόνες αφής εντοπίζουν τη μεταβολή του ηλεκτροστατικού πεδίου όταν τις αγγίζει ένα αγώγιμο σώμα, όπως το ανθρώπινο δάχτυλο.",
        "funFacts": [
            "Επειδή βασίζονται στην ηλεκτρική αγωγιμότητα, δεν λειτουργούν εύκολα όταν φοράμε κανονικά υφασμάτινα γάντια χωρίς ειδικές αγώγιμες ίνες.",
            "Υποστηρίζουν φυσικά λειτουργίες πολλαπλής αφής (multi-touch), όπως το τσίμπημα για μεγέθυνση (pinch-to-zoom)."
        ],
        "source": "https://en.wikipedia.org/wiki/Touchscreen",
        "tags": ["technology", "smartphones", "touchscreens", "hardware"]
    },
    {
        "id": "technology_easy_270",
        "text": "Τι κάνει η λειτουργία 'Πτήσης' (Airplane Mode) όταν ενεργοποιείται σε ένα κινητό τηλέφωνο ή τάμπλετ;",
        "correct": "Απενεργοποιεί όλες τις ασύρματες μεταδόσεις (κινητή τηλεφωνία, Wi-Fi, Bluetooth)",
        "distractors": ["Σβήνει εντελώς την οθόνη της συσκευής", "Διαγράφει όλα τα προσωρινά αρχεία", "Ενεργοποιεί αυτόματα το GPS σε μέγιστη ακρίβεια"],
        "explanation": "Η λειτουργία πτήσης διακόπτει όλους τους πομπούς ραδιοσυχνοτήτων της συσκευής ώστε να αποφεύγονται τυχόν παρεμβολές στα συστήματα πλοήγησης και επικοινωνίας του αεροσκάφους.",
        "funFacts": [
            "Επιτρέπει στη συσκευή να φορτίζει αισθητά πιο γρήγορα, καθώς δεν καταναλώνει ενέργεια αναζητώντας σήμα δικτύου.",
            "Οι σύγχρονες συσκευές επιτρέπουν στον χρήστη να ενεργοποιήσει ξανά επιλεκτικά το Wi-Fi ή το Bluetooth ακόμη και με τη λειτουργία πτήσης αναμμένη."
        ],
        "source": "https://en.wikipedia.org/wiki/Airplane_mode",
        "tags": ["technology", "smartphones", "airplane_mode", "settings"]
    },
    {
        "id": "technology_easy_271",
        "text": "Πώς ονομάζεται η μοναδική αριθμητική διεύθυνση που αποδίδεται σε κάθε συσκευή που συνδέεται σε ένα δίκτυο υπολογιστών;",
        "correct": "Διεύθυνση IP (IP Address)",
        "distractors": ["Κωδικός PIN", "Σειριακός αριθμός BIOS", "Αριθμός IMEI"],
        "explanation": "Η διεύθυνση IP (Internet Protocol) λειτουργεί όπως η ταχυδρομική διεύθυνση ενός σπιτιού, καθορίζοντας την ταυτότητα και τη θέση μιας συσκευής στο παγκόσμιο διαδίκτυο.",
        "funFacts": [
            "Η κλασική μορφή IPv4 αποτελείται από 4 αριθμούς από 0 έως 255 διαχωρισμένους με τελείες (π.χ. 192.168.1.1).",
            "Λόγω της εξάντλησης των 4,3 δισεκατομμυρίων διευθύνσεων IPv4, υιοθετείται σταδιακά το IPv6, το οποίο προσφέρει σχεδόν άπειρες διευθύνσεις (περίπου 340 undecillion)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B5%CF%85%CE%B8%CF%85%CE%BD%CF%83%CE%B9%CE%BF%CE%B4%CF%8C%CF%84%CE%B7%CF%83%CE%B7_IP",
        "tags": ["technology", "networking", "ip_address", "internet"]
    },
    {
        "id": "technology_easy_272",
        "text": "Πώς ονομάζεται η κυβερνοεπίθεση όπου οι απατεώνες προσποιούνται αξιόπιστους οργανισμούς (π.χ. τράπεζες) για να κλέψουν κωδικούς πρόσβασης;",
        "correct": "Phishing (Ηλεκτρονικό 'ψάρεμα')",
        "distractors": ["Overclocking", "Buffering", "Defragmentation"],
        "explanation": "Το Phishing είναι μορφή κοινωνικής μηχανικής όπου ο επιτιθέμενος αποστέλλει παραπλανητικά μηνύματα με πλαστούς συνδέσμους για να υποκλέψει ευαίσθητα τραπεζικά δεδομένα.",
        "funFacts": [
            "Ο όρος είναι λογοπαίγνιο με τη λέξη 'fishing' (ψάρεμα), με το 'ph' να παραπέμπει στους παλιούς χάκερ τηλεφωνικών δικτύων γνωστούς ως 'phreaks'.",
            "Πάνω από το 80% των καταγεγραμμένων περιστατικών παραβίασης ασφάλειας παγκοσμίως ξεκινούν από επιθέσεις phishing."
        ],
        "source": "https://el.wikipedia.org/wiki/Phishing",
        "tags": ["technology", "security", "phishing", "cybercrime"]
    },
    {
        "id": "technology_easy_273",
        "text": "Ποιο μέτρο κυβερνοασφάλειας απαιτεί έναν επιπλέον κωδικό μιας χρήσης (π.χ. μέσω SMS ή εφαρμογής) πέρα από τον κύριο κωδικό πρόσβασης;",
        "correct": "Έλεγχος ταυτότητας δύο παραγόντων (2FA)",
        "distractors": ["Κρυπτογράφηση σκληρού δίσκου", "Anti-aliasing", "Συμπίεση RAR"],
        "explanation": "Ο έλεγχος 2FA (Two-Factor Authentication) προσθέτει ένα κρίσιμο δεύτερο επίπεδο άμυνας, ώστε ακόμα κι αν κάποιος υποκλέψει τον κωδικό σας, να μην μπορεί να συνδεθεί χωρίς τη φυσική σας συσκευή.",
        "funFacts": [
            "Βασίζεται στον συνδυασμό τουλάχιστον δύο διαφορετικών στοιχείων: κάτι που ξέρετε (κωδικός), κάτι που έχετε (τηλέφωνο/token) ή κάτι που είστε (δακτυλικό αποτύπωμα).",
            "Μειώνει τον κίνδυνο παραβίασης λογαριασμού από αυτοματοποιημένα bot κατά σχεδόν 99%."
        ],
        "source": "https://en.wikipedia.org/wiki/Multi-factor_authentication",
        "tags": ["technology", "security", "2fa", "authentication"]
    },
    {
        "id": "technology_easy_274",
        "text": "Ποια είναι η κεντρική πλακέτα κυκλωμάτων ενός ηλεκτρονικού υπολογιστή πάνω στην οποία συνδέονται όλα τα επιμέρους εξαρτήματα;",
        "correct": "Μητρική κάρτα (Motherboard)",
        "distractors": ["Τροφοδοτικό", "Κάρτα ήχου", "Ψύκτρα επεξεργαστή"],
        "explanation": "Η μητρική κάρτα φιλοξενεί τον επεξεργαστή, τη μνήμη RAM, τις θύρες επέκτασης και επιτρέπει σε όλα τα υποσυστήματα να επικοινωνούν μεταξύ τους.",
        "funFacts": [
            "Ονομάζεται συχνά στην καθομιλουμένη των τεχνικών 'mobo' (από το motherboard).",
            "Περιέχει ένα μικρό τσιπ μνήμης ROM που αποθηκεύει το υλικολογισμικό BIOS ή UEFI για την αρχική εκκίνηση του συστήματος."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B7%CF%84%CF%81%CE%B9%CE%BA%CE%AE_%CE%BA%CE%AC%CF%81%CF%84%CE%B1",
        "tags": ["technology", "hardware", "motherboard", "components"]
    },
    {
        "id": "technology_easy_275",
        "text": "Ποιο σύστημα του διαδικτύου λειτουργεί ως 'τηλεφωνικός κατάλογος', μετατρέποντας εύκολα κατανοητά ονόματα ιστοσελίδων σε αριθμητικές διευθύνσεις IP;",
        "correct": "DNS (Domain Name System)",
        "distractors": ["DHCP", "FTP", "SNMP"],
        "explanation": "Το DNS μεταφράζει ονόματα τομέα όπως το 'google.com' στην αντίστοιχη διεύθυνση IP (π.χ. 142.250.180.206) ώστε οι υπολογιστές να μπορούν να δρομολογούν τα αιτήματα.",
        "funFacts": [
            "Χωρίς το DNS, οι χρήστες θα έπρεπε να απομνημονεύουν δεκαδικούς αριθμούς για να επισκεφθούν κάθε μεμονωμένη ιστοσελίδα.",
            "Σχεδιάστηκε το 1983 από τον Paul Mockapetris."
        ],
        "source": "https://el.wikipedia.org/wiki/Domain_Name_System",
        "tags": ["technology", "networking", "dns", "internet"]
    },
    {
        "id": "technology_easy_276",
        "text": "Ποια τεχνολογία βυθίζει τον χρήστη σε έναν πλήρως ψηφιακό, τρισδιάστατο τεχνητό κόσμο μέσω ειδικής μάσκας/κράνους;",
        "correct": "Εικονική Πραγματικότητα (Virtual Reality - VR)",
        "distractors": ["Επαυξημένη Πραγματικότητα (AR)", "Ολογραφία", "Τηλεδιάσκεψη"],
        "explanation": "Η Εικονική Πραγματικότητα (VR) χρησιμοποιεί οθόνες στερεοσκοπικής όρασης και αισθητήρες κίνησης κεφαλής για να δημιουργήσει την πλήρη ψευδαίσθηση παρουσίας σε έναν ψηφιακό χώρο.",
        "funFacts": [
            "Σε αντίθεση με την Επαυξημένη Πραγματικότητα (AR) που προβάλλει γραφικά πάνω στον πραγματικό κόσμο, το VR απομονώνει εντελώς το οπτικό πεδίο του χρήστη.",
            "Τα σύγχρονα αυτόνομα VR headsets όπως το Meta Quest διαθέτουν ενσωματωμένο επεξεργαστή και μπαταρία χωρίς ανάγκη καλωδίων σύνδεσης με PC."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CE%B9%CE%BA%CE%BF%CE%BD%CE%B9%CE%BA%CE%AE_%CF%80%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1",
        "tags": ["technology", "vr", "virtual_reality", "gaming"]
    },
    {
        "id": "technology_easy_277",
        "text": "Πώς ονομάζεται η διαδικασία δημιουργίας φυσικών τρισδιάστατων αντικειμένων μέσω διαδοχικής εναπόθεσης στρωμάτων υλικού (π.χ. πλαστικού);",
        "correct": "Τρισδιάστατη εκτύπωση (3D Printing)",
        "distractors": ["Φωτοτυπία", "Λιθογραφία", "Χύτευση"],
        "explanation": "Η τρισδιάστατη εκτύπωση, γνωστή και ως προσθετική κατασκευή (additive manufacturing), κατασκευάζει αντικείμενα στρώση προς στρώση βάσει ενός ψηφιακού μοντέλου CAD.",
        "funFacts": [
            "Ο Chuck Hull εφηύρε την πρώτη μέθοδο 3D εκτύπωσης (στερεολιθογραφία - SLA) το 1983 και ίδρυσε την 3D Systems.",
            "Σήμερα χρησιμοποιείται από την αεροδιαστημική και την ιατρική (κατασκευή προσθετικών μελών) μέχρι την εκτύπωση σπιτιών με σκυρόδεμα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CF%81%CE%B9%CF%83%CE%B4%CE%B9%CE%AC%CF%83%CF%84%CE%B1%CF%84%CE%B7_%CE%B5%CE%BA%CF%84%CF%85%CF%80%CF%89%CF%83%CE%B7",
        "tags": ["technology", "hardware", "3d_printing", "manufacturing"]
    },
    {
        "id": "technology_easy_278",
        "text": "Πώς ονομάζεται η παροχή υπολογιστικών υπηρεσιών (αποθήκευση, επεξεργασία, βάσεις δεδομένων) μέσω διαδικτύου αντί για τοπικούς σκληρούς δίσκους;",
        "correct": "Υπολογιστικό νέφος (Cloud Computing)",
        "distractors": ["Grid Computing", "P2P Computing", "Edge Caching"],
        "explanation": "Το Cloud Computing επιτρέπει στις επιχειρήσεις και τους καταναλωτές να νοικιάζουν υπολογιστικούς πόρους από απομακρυσμένα κέντρα δεδομένων εταιρειών όπως η Amazon (AWS), η Microsoft (Azure) και η Google.",
        "funFacts": [
            "Ο όρος 'cloud' προήλθε από τα διαγράμματα ροής δικτύων της δεκαετίας του 1990, όπου το διαδίκτυο συμβολιζόταν παραδοσιακά με ένα σύννεφο.",
            "Εξαλείφει την ανάγκη για ακριβή αγορά και συντήρηση ιδιόκτητων φυσικών servers."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%B9%CE%BA%CF%8C_%CE%BD%CE%AD%CF%86%CE%BF%CF%82",
        "tags": ["technology", "cloud", "servers", "internet"]
    },
    {
        "id": "technology_easy_279",
        "text": "Ποια λειτουργία των προγραμμάτων περιήγησης (browsers) αποτρέπει την αποθήκευση του ιστορικού περιήγησης και των cookies στην τοπική συσκευή;",
        "correct": "Ανώνυμη περιήγηση (Incognito / Private Browsing)",
        "distractors": ["Ασφαλής λειτουργία (Safe Mode)", "Λειτουργία πτήσης", "Λειτουργία εξοικονόμησης δεδομένων"],
        "explanation": "Η ανώνυμη περιήγηση διαγράφει το ιστορικό, τα cookies και τα δεδομένα φορμών μόλις κλείσει το παράθυρο, προστατεύοντας το απόρρητο από άλλους χρήστες της ίδιας συσκευής.",
        "funFacts": [
            "Δεν καθιστά τον χρήστη αόρατο στο διαδίκτυο: οι πάροχοι internet (ISP), οι διαχειριστές δικτύου και οι ίδιες οι ιστοσελίδες εξακολουθούν να βλέπουν τη διεύθυνση IP του.",
            "Η Google εισήγαγε τη λειτουργία Incognito με το χαρακτηριστικό εικονίδιο κατασκόπου στο Chrome το 2008."
        ],
        "source": "https://en.wikipedia.org/wiki/Private_browsing",
        "tags": ["technology", "browsers", "privacy", "incognito"]
    },
    {
        "id": "technology_easy_280",
        "text": "Πώς ονομάζεται ο τύπος προσωρινής μνήμης υψηλής ταχύτητας που αποθηκεύει πρόσφατα δεδομένα για ταχύτερη ανάκτηση στο μέλλον;",
        "correct": "Κρυφή μνήμη (Cache)",
        "distractors": ["Εικονική μνήμη", "Μητρώο (Registry)", "Buffer"],
        "explanation": "Η Cache μπορεί να είναι είτε υλικό (όπως η ταχύτατη μνήμη L1/L2/L3 του επεξεργαστή) είτε λογισμικό (όπως η cache εικόνων ενός web browser).",
        "funFacts": [
            "Η λέξη προέρχεται από το γαλλικό ρήμα 'cacher' που σημαίνει 'κρύβω'.",
            "Όταν ένα πρόγραμμα βρίσκει τα δεδομένα που ψάχνει απευθείας στην cache, το γεγονός ονομάζεται 'cache hit', ενώ όταν λείπουν ονομάζεται 'cache miss'."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%81%CF%85%CF%86%CE%AE_%CE%BC%CE%BD%CE%AE%CE%BC%CE%B7",
        "tags": ["technology", "hardware", "software", "cache"]
    },
    {
        "id": "technology_easy_281",
        "text": "Ποια συσκευή δικτύου κατευθύνει και δρομολογεί τα πακέτα δεδομένων ανάμεσα στο τοπικό σας οικιακό δίκτυο και το διαδίκτυο;",
        "correct": "Δρομολογητής (Router)",
        "distractors": ["Εκτυπωτής", "Κάρτα ήχου", "Webcam"],
        "explanation": "Ο router εξετάζει τη διεύθυνση προορισμού κάθε πακέτου δεδομένων και καθορίζει την καλύτερη διαδρομή για να φτάσει στον στόχο του.",
        "funFacts": [
            "Τα περισσότερα οικιακά 'ρούτερ' είναι στην πραγματικότητα συνδυαστικές συσκευές 3-σε-1: μόντεμ, ρούτερ και ασύρματο σημείο πρόσβασης Wi-Fi.",
            "Ο πρώτος εξειδικευμένος πρόδρομος του ρούτερ ήταν ο IMP (Interface Message Processor) που κατασκευάστηκε για το ARPANET το 1969."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CF%81%CE%BF%CE%BC%CE%BF%CE%BB%CE%BF%CE%B3%CE%B7%CF%84%CE%AE%CF%82",
        "tags": ["technology", "networking", "router", "hardware"]
    },
    {
        "id": "technology_easy_282",
        "text": "Ποιο είναι το κύριο πλεονέκτημα χρήσης της 'Σκοτεινής λειτουργίας' (Dark Mode) στις οθόνες τεχνολογίας OLED;",
        "correct": "Σημαντική εξοικονόμηση ενέργειας της μπαταρίας",
        "distractors": ["Αύξηση της ταχύτητας του Wi-Fi", "Αυτόματη εκκαθάριση ιών", "Βελτίωση της ποιότητας των ηχείων"],
        "explanation": "Στις οθόνες OLED, τα εικονοστοιχεία (pixels) είναι αυτόφωτα και απενεργοποιούνται εντελώς όταν προβάλλουν μαύρο χρώμα, μηδενίζοντας την κατανάλωση ρεύματος σε εκείνα τα σημεία.",
        "funFacts": [
            "Εκτός από εξοικονόμηση μπαταρίας, μειώνει την κόπωση των ματιών σε περιβάλλοντα με χαμηλό φωτισμό.",
            "Στις παλιές οθόνες LCD, το Dark Mode δεν εξοικονομεί σχεδόν καθόλου ρεύμα επειδή ο οπίσθιος φωτισμός (backlight) παραμένει πάντα αναμμένος."
        ],
        "source": "https://en.wikipedia.org/wiki/Light-on-dark_color_scheme",
        "tags": ["technology", "smartphones", "oled", "display"]
    },
    {
        "id": "technology_easy_283",
        "text": "Πώς ονομάζονται τα μικρά αρχεία κειμένου που αποθηκεύει μια ιστοσελίδα στον υπολογιστή σας για να θυμάται τις προτιμήσεις ή τη σύνδεσή σας;",
        "correct": "Cookies",
        "distractors": ["Worms", "Applets", "Widgets"],
        "explanation": "Τα HTTP cookies δημιουργήθηκαν το 1994 από τον Lou Montulli στη Netscape για να επιτρέψουν στις ιστοσελίδες να διατηρούν κατάσταση, όπως το καλάθι αγορών σε ένα e-shop.",
        "funFacts": [
            "Ο όρος προέρχεται από τα 'magic cookies' του λειτουργικού συστήματος Unix.",
            "Ο αυστηρός ευρωπαϊκός κανονισμός GDPR επέβαλε σε όλες τις ιστοσελίδες να ζητούν τη ρητή συγκατάθεση των χρηστών πριν αποθηκεύσουν cookies παρακολούθησης διαφημίσεων."
        ],
        "source": "https://el.wikipedia.org/wiki/Cookie",
        "tags": ["technology", "web", "cookies", "internet"]
    },
    {
        "id": "technology_easy_284",
        "text": "Πόσα Megabits (Mb) αντιστοιχούν σε 1 Megabyte (MB) αποθηκευτικού χώρου ή ταχύτητας;",
        "correct": "8",
        "distractors": ["2", "4", "10"],
        "explanation": "Επειδή κάθε Byte αποτελείται από 8 bits, 1 Megabyte (MB) ισούται ακριβώς με 8 Megabits (Mb).",
        "funFacts": [
            "Οι πάροχοι internet διαφημίζουν τις ταχύτητες σύνδεσης σε Megabits ανά δευτερόλεπτο (Mbps), γι' αυτό μια γραμμή 100 Mbps κατεβάζει αρχεία με μέγιστη ταχύτητα περίπου 12,5 Megabytes ανά δευτερόλεπτο (MB/s).",
            "Η σύγχυση ανάμεσα στο κεφαλαίο 'B' (Byte) και το πεζό 'b' (bit) είναι μία από τις πιο συχνές παρανοήσεις στην τεχνολογία."
        ],
        "source": "https://el.wikipedia.org/wiki/Megabyte",
        "tags": ["technology", "computer_science", "units", "data"]
    },
    {
        "id": "technology_easy_285",
        "text": "Ποιο έξυπνο ηχείο της Amazon εισήγαγε τη φωνητική βοηθό Alexa στα σπίτια εκατομμυρίων χρηστών;",
        "correct": "Amazon Echo",
        "distractors": ["Google Home", "Apple HomePod", "Sonos Move"],
        "explanation": "Το Amazon Echo κυκλοφόρησε το 2014 και ανταποκρίνεται στη λέξη αφύπνισης 'Alexa', εκτελώντας εντολές για αναπαραγωγή μουσικής, ρύθμιση έξυπνων λαμπτήρων και καιρό.",
        "funFacts": [
            "Το όνομα Alexa επιλέχθηκε επειδή περιέχει το σπάνιο σύμφωνο 'X', το οποίο αναγνωρίζεται ευκολότερα από τους αλγορίθμους φωνητικής αναγνώρισης με ελάχιστες ψευδείς ενεργοποιήσεις.",
            "Εμπνεύστηκε επίσης από τη διάσημη αρχαία Βιβλιοθήκη της Αλεξάνδρειας."
        ],
        "source": "https://en.wikipedia.org/wiki/Amazon_Echo",
        "tags": ["technology", "amazon", "alexa", "smart_home"]
    },
    {
        "id": "technology_easy_286",
        "text": "Ποια διάσημη σειρά οικιακών κονσολών βιντεοπαιχνιδιών κυκλοφόρησε για πρώτη φορά από τη Sony στην Ιαπωνία το 1994;",
        "correct": "PlayStation",
        "distractors": ["Xbox", "Sega Saturn", "Nintendo GameCube"],
        "explanation": "Το αρχικό PlayStation (PS1) δημιουργήθηκε υπό την καθοδήγηση του Ken Kutaragi και έγινε η πρώτη κονσόλα στην ιστορία που ξεπέρασε τα 100 εκατομμύρια πωλήσεις.",
        "funFacts": [
            "Ξεκίνησε αρχικά ως κοινό εγχείρημα με τη Nintendo για τη δημιουργία ενός CD-ROM πρόσθετου για το Super Nintendo, αλλά η Nintendo ακύρωσε ξαφνικά τη συμφωνία.",
            "Τα τέσσερα γεωμετρικά σύμβολα στα κουμπιά του χειριστηρίου (τρίγωνο, κύκλος, χι, τετράγωνο) σχεδιάστηκαν από τον Teiyu Goto για να αντιπροσωπεύουν οπτική γωνία, ναι, όχι και μενού αντίστοιχα."
        ],
        "source": "https://el.wikipedia.org/wiki/PlayStation",
        "tags": ["technology", "sony", "playstation", "gaming"]
    },
    {
        "id": "technology_easy_287",
        "text": "Πώς ονομάζεται το αυτοματοποιημένο τεστ με παραμορφωμένα γράμματα ή εικόνες που διαπιστώνει αν ένας χρήστης στο ίντερνετ είναι άνθρωπος ή υπολογιστικό πρόγραμμα (bot);",
        "correct": "CAPTCHA",
        "distractors": ["Benchmark", "Algorand", "Speedtest"],
        "explanation": "Το CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) προστατεύει ιστοσελίδες από κακόβουλα αυτοματοποιημένα bots spamming.",
        "funFacts": [
            "Αναπτύχθηκε στο Πανεπιστήμιο Carnegie Mellon από ομάδα με επικεφαλής τον Luis von Ahn το 2000.",
            "Η εξέλιξή του, το reCAPTCHA της Google, χρησιμοποιήθηκε για την ψηφιοποίηση παλιών βιβλίων και την εκπαίδευση συστημάτων όρασης αυτόνομων οχημάτων μέσω αναγνώρισης φαναριών και διαβάσεων."
        ],
        "source": "https://el.wikipedia.org/wiki/CAPTCHA",
        "tags": ["technology", "security", "captcha", "internet"]
    },
    {
        "id": "technology_easy_288",
        "text": "Πώς ονομάζεται η ειδική ψηφιακή γραφίδα που χρησιμοποιείται για ζωγραφική, γραφή και ακριβή πλοήγηση σε οθόνες αφής tablet;",
        "correct": "Stylus (Γραφίδα)",
        "distractors": ["Trackball", "Gamepad", "Scanner"],
        "explanation": "Η γραφίδα (stylus), όπως το Apple Pencil ή το S-Pen της Samsung, προσφέρει εξαιρετική ακρίβεια και ανίχνευση πίεσης και κλίσης για ψηφιακούς καλλιτέχνες.",
        "funFacts": [
            "Ο Steve Jobs είχε πει περίφημα κατά την παρουσίαση του πρώτου iPhone το 2007: 'Who wants a stylus? You have to get 'em, put 'em away, you lose 'em. Yuck! Nobody wants a stylus.'",
            "Οκτώ χρόνια αργότερα, το 2015, η Apple κυκλοφόρησε το δικό της πολυτελές Apple Pencil για το iPad Pro."
        ],
        "source": "https://en.wikipedia.org/wiki/Stylus_(computing)",
        "tags": ["technology", "hardware", "stylus", "tablets"]
    },
    {
        "id": "technology_easy_289",
        "text": "Ποια δημοφιλής μορφή αρχείου εικόνας επιτρέπει σύντομες κινούμενες επαναλήψεις (animation) χωρίς ήχο στο διαδίκτυο;",
        "correct": "GIF",
        "distractors": ["JPEG", "BMP", "TIFF"],
        "explanation": "Το GIF (Graphics Interchange Format) δημιουργήθηκε το 1987 από τον Steve Wilhite στην εταιρεία CompuServe και υποστηρίζει παλέτα έως 256 χρωμάτων.",
        "funFacts": [
            "Ο δημιουργός του, Steve Wilhite, ξεκαθάρισε το 2013 ότι η σωστή προφορά του είναι με μαλακό 'τζ' ('Jif') και όχι με σκληρό 'γκ'.",
            "Παρά τους περιορισμούς της παλέτας χρωμάτων του, παραμένει εξαιρετικά δημοφιλές μέσο έκφρασης και meme στα social media."
        ],
        "source": "https://el.wikipedia.org/wiki/GIF",
        "tags": ["technology", "graphics", "gif", "internet"]
    },
    {
        "id": "technology_easy_290",
        "text": "Ποια είναι η πιο συνηθισμένη μορφή συμπιεσμένου αρχείου αρχειοθήκης που συγκεντρώνει πολλά αρχεία σε ένα με επέκταση .zip;",
        "correct": "Αρχείο ZIP",
        "distractors": ["Αρχείο EXE", "Αρχείο DLL", "Αρχείο ISO"],
        "explanation": "Η μορφή ZIP επιτρέπει τη συμπίεση δεδομένων χωρίς απώλειες (lossless), διευκολύνοντας την αποστολή και αποθήκευση πολλαπλών αρχείων και φακέλων.",
        "funFacts": [
            "Σχεδιάστηκε το 1989 από τον Phil Katz για το πρόγραμμα PKZIP.",
            "Τα περισσότερα σύγχρονα λειτουργικά συστήματα (Windows, macOS, Linux) έχουν ενσωματωμένη υποστήριξη για άνοιγμα αρχείων ZIP χωρίς εξωτερικό λογισμικό."
        ],
        "source": "https://el.wikipedia.org/wiki/ZIP",
        "tags": ["technology", "software", "compression", "files"]
    },
    {
        "id": "technology_easy_291",
        "text": "Πώς ονομάζεται η φορητή εξωτερική επαναφορτιζόμενη μπαταρία που χρησιμοποιείται για τη φόρτιση κινητών τηλεφώνων εν κινήσει;",
        "correct": "Power bank",
        "distractors": ["Inverter", "Alternator", "Stabilizer"],
        "explanation": "Το power bank ενσωματώνει μπαταρίες ιόντων λιθίου ή πολυμερών λιθίου με κύκλωμα ελέγχου τάσης για ασφαλή φόρτιση συσκευών μέσω θυρών USB.",
        "funFacts": [
            "Το πρώτο καταγεγραμμένο power bank συναρμολογήθηκε το 2001 από φοιτητές στην Κίνα συνδέοντας μπαταρίες ΑΑ σε ένα κύκλωμα για να τροφοδοτήσουν μια ψηφιακή κάμερα.",
            "Οι διεθνείς κανονισμοί αεροπορικών ταξιδιών επιτρέπουν τα power banks μόνο στη χειραποσκευή και απαγορεύουν την τοποθέτησή τους στις παραδοτέες βαλίτσες για λόγους πυρασφάλειας."
        ],
        "source": "https://en.wikipedia.org/wiki/Battery_charger#Power_bank",
        "tags": ["technology", "gadgets", "battery", "power_bank"]
    },
    {
        "id": "technology_easy_292",
        "text": "Ποια κατηγορία φορετής τεχνολογίας (wearable) περιλαμβάνει συσκευές καρπού που μετρούν βήματα, καρδιακούς παλμούς και προβάλλουν ειδοποιήσεις κινητού;",
        "correct": "Έξυπνο ρολόι (Smartwatch)",
        "distractors": ["Smart Ring", "VR Headset", "Action Camera"],
        "explanation": "Τα έξυπνα ρολόγια συνδέονται μέσω Bluetooth με το smartphone και προσφέρουν παρακολούθηση φυσικής κατάστασης, κλήσεις, μηνύματα και ανέπαφες πληρωμές.",
        "funFacts": [
            "Το Apple Watch, που κυκλοφόρησε το 2015, ξεπέρασε σε ετήσιες πωλήσεις ολόκληρη την παραδοσιακή ελβετική βιομηχανία ρολογιών μαζί.",
            "Πολλά σύγχρονα smartwatches διαθέτουν αισθητήρα ηλεκτροκαρδιογραφήματος (ECG) εγκεκριμένο για ανίχνευση κολπικής μαρμαρυγής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%88%CE%BE%CF%85%CF%80%CE%BD%CE%BF_%CF%81%CE%BF%CE%BB%CF%8C%CE%B9",
        "tags": ["technology", "wearables", "smartwatch", "gadgets"]
    },
    {
        "id": "technology_easy_293",
        "text": "Πώς ονομάζεται το μη επανδρωμένο τηλεκατευθυνόμενο ιπτάμενο όχημα με πολλαπλούς έλικες (multirotor) που χρησιμοποιείται ευρέως για εναέρια βιντεοσκόπηση;",
        "correct": "Drone (ή Quadcopter)",
        "distractors": ["Hovercraft", "Zeppelin", "Glider"],
        "explanation": "Τα καταναλωτικά drones διαθέτουν συνήθως τέσσερις έλικες (quadcopters), κάμερα υψηλής ανάλυσης με σταθεροποιητή gimbal και πλοήγηση GPS.",
        "funFacts": [
            "Η λέξη 'drone' σημαίνει κυριολεκτικά 'κηφήνας' στα αγγλικά, λόγω του χαρακτηριστικού βουητού των ελίκων κατά την πτήση.",
            "Η εταιρεία DJI, που ιδρύθηκε στη Σεντζέν της Κίνας από τον Frank Wang, κατέχει πάνω από το 70% της παγκόσμιας αγοράς καταναλωτικών drones."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%B7_%CE%B5%CF%80%CE%B1%CE%BD%CE%B4%CF%81%CF%89%CE%BC%CE%AD%CE%BD%CE%BF_%CE%B1%CE%B5%CF%81%CE%BF%CF%83%CE%BA%CE%AC%CF%86%CE%BF%CF%82",
        "tags": ["technology", "drones", "hardware", "gadgets"]
    },
    {
        "id": "technology_easy_294",
        "text": "Πώς ονομάζεται η τεχνολογία λογισμικού που αναγνωρίζει τυπωμένο ή χειρόγραφο κείμενο μέσα σε μια εικόνα ή σκαναρισμένο έγγραφο;",
        "correct": "Οπτική αναγνώριση χαρακτήρων (OCR)",
        "distractors": ["CGI", "VoIP", "RFID"],
        "explanation": "Το OCR (Optical Character Recognition) μετατρέπει φωτογραφίες εγγράφων ή σελίδες βιβλίων σε επεξεργάσιμο ψηφιακό κείμενο.",
        "funFacts": [
            "Ο Ray Kurzweil ανέπτυξε το 1974 το πρώτο σύστημα OCR παντός τύπου γραμματοσειράς μαζί με μια μηχανή ανάγνωσης κειμένου σε ομιλία για τυφλούς.",
            "Εφαρμογές όπως το Google Lens χρησιμοποιούν OCR σε πραγματικό χρόνο για άμεση μετάφραση πινακίδων και μενού εστιατορίων από την κάμερα του κινητού."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9F%CF%80%CF%84%CE%B9%CE%BA%CE%AE_%CE%B1%CE%BD%CE%B1%CE%B3%CE%BD%CF%8E%CF%81%CE%B9%CF%83%CE%B7_%CF%87%CE%B1%CF%81%CE%B1%CE%BA%CF%84%CE%AE%CF%81%CF%89%CE%BD",
        "tags": ["technology", "software", "ocr", "ai"]
    },
    {
        "id": "technology_easy_295",
        "text": "Ποια εφαρμογή τηλεδιασκέψεων που ιδρύθηκε από τον Eric Yuan γνώρισε εκρηκτική παγκόσμια διάδοση κατά την πανδημία COVID-19 το 2020;",
        "correct": "Zoom",
        "distractors": ["Skype", "Google Meet", "Webex"],
        "explanation": "Το Zoom Video Communications ιδρύθηκε το 2011 και έγινε η de facto πλατφόρμα για εξ αποστάσεως εργασία, τηλεκπαίδευση και οικογενειακές συγκεντρώσεις το 2020.",
        "funFacts": [
            "Ο Eric Yuan εμπνεύστηκε την εφαρμογή όταν ήταν φοιτητής και έπρεπε να ταξιδεύει 10 ώρες με το τρένο για να δει την κοπέλα του.",
            "Οι ημερήσιοι συμμετέχοντες σε συναντήσεις Zoom εκτοξεύθηκαν από 10 εκατομμύρια τον Δεκέμβριο του 2019 σε πάνω από 300 εκατομμύρια τον Απρίλιο του 2020."
        ],
        "source": "https://el.wikipedia.org/wiki/Zoom_Video_Communications",
        "tags": ["technology", "zoom", "telecommunications", "video"]
    },
    {
        "id": "technology_easy_296",
        "text": "Ποιος δημοφιλής ιστότοπος κοινωνικής δικτύωσης και φόρουμ αυτοαποκαλείται 'η πρώτη σελίδα του διαδικτύου' (the front page of the internet);",
        "correct": "Reddit",
        "distractors": ["Digg", "Quora", "4chan"],
        "explanation": "Το Reddit ιδρύθηκε το 2005 από τους Steve Huffman και Alexis Ohanian και είναι οργανωμένο σε χιλιάδες επιμέρους κοινότητες θεμάτων γνωστές ως 'subreddits'.",
        "funFacts": [
            "Η μασκότ του Reddit είναι ένα χαριτωμένο εξωγήινο πλάσμα που ονομάζεται 'Snoo'.",
            "Οι χρήστες ψηφίζουν θετικά (upvote) ή αρνητικά (downvote) σε αναρτήσεις και σχόλια, καθορίζοντας ποια θέματα εμφανίζονται στην κορυφή."
        ],
        "source": "https://el.wikipedia.org/wiki/Reddit",
        "tags": ["technology", "reddit", "social_media", "internet"]
    },
    {
        "id": "technology_easy_297",
        "text": "Ποια διαδικτυακή πλατφόρμα λειτουργεί ως εικονικός πίνακας ανακοινώσεων επιτρέποντας στους χρήστες να 'καρφιτσώνουν' (pin) ιδέες, συνταγές και φωτογραφίες;",
        "correct": "Pinterest",
        "distractors": ["Flickr", "DeviantArt", "Imgur"],
        "explanation": "Το Pinterest ιδρύθηκε από τους Ben Silbermann, Evan Sharp και Paul Sciarra και επιτρέπει τη δημιουργία θεματικών πινάκων για έμπνευση και σχεδίαση έργων.",
        "funFacts": [
            "Ξεκίνησε το 2010 και αρχικά λειτουργούσε μόνο με πρόσκληση από υπάρχοντα μέλη.",
            "Κάθε καρφίτσα (pin) συνδέεται συνήθως άμεσα με την αρχική ιστοσελίδα προέλευσης της εικόνας."
        ],
        "source": "https://el.wikipedia.org/wiki/Pinterest",
        "tags": ["technology", "pinterest", "social_media", "internet"]
    },
    {
        "id": "technology_easy_298",
        "text": "Ποια πρωτοποριακή υπηρεσία αποθήκευσης cloud ιδρύθηκε από τον Drew Houston το 2007 επειδή ξεχνούσε συνεχώς το USB φλασάκι του;",
        "correct": "Dropbox",
        "distractors": ["Box", "Mega", "MediaFire"],
        "explanation": "Το Dropbox απλοποίησε τον συγχρονισμό αρχείων δημιουργώντας έναν ειδικό φάκελο στον υπολογιστή που συγχρονίζεται αυτόματα με το cloud.",
        "funFacts": [
            "Ο Steve Jobs είχε συναντηθεί με τον Drew Houston το 2009 και προσπάθησε να εξαγοράσει το Dropbox, αποκαλώντας το 'ένα χαρακτηριστικό, όχι ένα προϊόν'.",
            "Η εταιρεία απέρριψε την πρόταση της Apple και εξελίχθηκε σε ανεξάρτητο κολοσσό πολλών δισεκατομμυρίων."
        ],
        "source": "https://el.wikipedia.org/wiki/Dropbox",
        "tags": ["technology", "dropbox", "cloud", "software"]
    },
    {
        "id": "technology_easy_299",
        "text": "Ποια διάσημη εφαρμογή για κινητά μπορεί να ακούσει ένα τραγούδι που παίζει στο περιβάλλον και να αναγνωρίσει τον τίτλο και τον καλλιτέχνη σε δευτερόλεπτα;",
        "correct": "Shazam",
        "distractors": ["SoundHound", "Musixmatch", "Genius"],
        "explanation": "Το Shazam δημιουργεί ένα ψηφιακό ακουστικό αποτύπωμα (audio fingerprint) του δείγματος ήχου και το συγκρίνει με μια κεντρική βάση δεδομένων δεκάδων εκατομμυρίων τραγουδιών.",
        "funFacts": [
            "Ιδρύθηκε το 1999 στο Λονδίνο, πολύ πριν από τα smartphones: αρχικά οι χρήστες καλούσαν τον αριθμό 2580, κρατούσαν το τηλέφωνο κοντά στο ηχείο και λάμβαναν SMS με τον τίτλο.",
            "Εξαγοράστηκε από την Apple το 2018 έναντι περίπου 400 εκατομμυρίων δολαρίων."
        ],
        "source": "https://el.wikipedia.org/wiki/Shazam_(%CE%B5%CF%86%CE%B1%CF%81%CE%BC%CE%BF%CE%B3%CE%AE)",
        "tags": ["technology", "music", "shazam", "apps"]
    },
    {
        "id": "technology_easy_300",
        "text": "Ποια διάσημη εφαρμογή εκμάθησης γλωσσών χρησιμοποιεί παιχνιδοποίηση (gamification) με μασκότ μια πράσινη κουκουβάγια;",
        "correct": "Duolingo",
        "distractors": ["Babbel", "Rosetta Stone", "Memrise"],
        "explanation": "Το Duolingo ιδρύθηκε από τον Luis von Ahn και τον Severin Hacker και προσφέρει διασκεδαστικά μαθήματα γλωσσών με καθημερινά σερί, πόντους εμπειρίας και διαγωνισμούς.",
        "funFacts": [
            "Η πράσινη κουκουβάγια ονομάζεται επίσημα 'Duo' και έχει γίνει διάσημη για τα επίμονα χιουμοριστικά μηνύματα υπενθύμισης προς τους χρήστες.",
            "Προσφέρει επίσης μαθήματα σε φανταστικές γλώσσες όπως τα High Valyrian από το Game of Thrones και τα Klingon από το Star Trek."
        ],
        "source": "https://el.wikipedia.org/wiki/Duolingo",
        "tags": ["technology", "duolingo", "education", "apps"]
    },
    {
        "id": "technology_easy_301",
        "text": "Ποια είναι η μεγαλύτερη δωρεάν διαδικτυακή εγκυκλοπαίδεια στον κόσμο, που γράφεται και συντηρείται συλλογικά από εθελοντές;",
        "correct": "Βικιπαίδεια (Wikipedia)",
        "distractors": ["Britannica Online", "Encarta", "Citizendium"],
        "explanation": "Η Wikipedia ξεκίνησε στις 15 Ιανουαρίου 2001 από τους Jimmy Wales και Larry Sanger και περιέχει σήμερα δεκάδες εκατομμύρια άρθρα σε περισσότερες από 300 γλώσσες.",
        "funFacts": [
            "Η λέξη είναι σύνθεση της χαβανέζικης λέξης 'wiki' (που σημαίνει γρήγορα) και της λέξης 'encyclopedia'.",
            "Λειτουργεί υπό το μη κερδοσκοπικό Ίδρυμα Wikimedia και συντηρείται αποκλειστικά από δωρεές αναγνωστών χωρίς διαφημίσεις."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%92%CE%B9%CE%BA%CE%B9%CF%80%CE%B1%CE%AF%CE%B4%CE%B5%CE%B9%CE%B1",
        "tags": ["technology", "wikipedia", "internet", "encyclopedia"]
    },
    {
        "id": "technology_easy_302",
        "text": "Πώς ονομάζεται το λογισμικό του οποίου ο πηγαίος κώδικας διατίθεται ελεύθερα ώστε ο καθένας να μπορεί να τον εξετάσει, να τον τροποποιήσει και να τον διανείμει;",
        "correct": "Λογισμικό ανοιχτού κώδικα (Open Source)",
        "distractors": ["Ιδιοταγές λογισμικό (Proprietary)", "Freeware", "Shareware"],
        "explanation": "Το λογισμικό ανοιχτού κώδικα (όπως το Linux, το Android και το Blender) προωθεί τη διαφάνεια, τη συλλογική βελτίωση και την ελευθερία χρήσης.",
        "funFacts": [
            "Η πρωτοβουλία Open Source Initiative (OSI) ιδρύθηκε το 1998 από τους Bruce Perens και Eric S. Raymond.",
            "Τα μεγαλύτερα τμήματα της σύγχρονης διαδικτυακής υποδομής (όπως servers, βάσεις δεδομένων και λειτουργικά συστήματα cloud) τρέχουν σε λογισμικό ανοιχτού κώδικα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CE%B3%CE%B9%CF%83%CE%BC%CE%B9%CE%BA%CF%8C_%CE%B1%CE%BD%CE%BF%CE%B9%CE%BA%CF%84%CE%BF%CF%81_%CE%BA%CF%8E%CE%B4%CE%B9%CE%BA%CE%B1",
        "tags": ["technology", "open_source", "software", "licensing"]
    },
    {
        "id": "technology_easy_303",
        "text": "Πώς ονομάζεται το κακόβουλο πρόγραμμα που εξαπατά τον χρήστη εμφανιζόμενο ως χρήσιμη ή αβλαβής εφαρμογή για να εισχωρήσει στο σύστημα;",
        "correct": "Δούρειος Ίππος (Trojan Horse)",
        "distractors": ["Spyware", "Adware", "Rootkit"],
        "explanation": "Ο Δούρειος Ίππος (Trojan) παίρνει το όνομά του από τον μύθο της Τροίας και ανοίγει κρυφές κερκόπορτες (backdoors) για τον έλεγχο του υπολογιστή από εισβολείς.",
        "funFacts": [
            "Σε αντίθεση με τους ιούς και τα σκουλήκια (worms), τα trojans συνήθως δεν αυτοαναπαράγονται, αλλά βασίζονται στην εξαπάτηση του χρήστη για να εκτελεστούν.",
            "Συχνά μεταμφιέζονται σε 'σπασμένα' παιχνίδια, ταινίες ή υποτιθέμενες ενημερώσεις λογισμικού."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%BF%CF%8D%CF%81%CE%B5%CE%B9%CE%BF%CF%82_%CE%88%CF%80%CF%80%CE%BF%CF%82_(%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AD%CF%82)",
        "tags": ["technology", "security", "malware", "trojan"]
    },
    {
        "id": "technology_easy_304",
        "text": "Ποιο είδος κακόβουλου λογισμικού κρυπτογραφεί όλα τα αρχεία του χρήστη και απαιτεί πληρωμή λύτρων (συνήθως σε κρυπτονόμισμα) για το ξεκλείδωμά τους;",
        "correct": "Ransomware (Λογισμικό λύτρων)",
        "distractors": ["Keylogger", "Adware", "Dialer"],
        "explanation": "Το Ransomware αποτελεί τεράστια απειλή για επιχειρήσεις και νοσοκομεία, καθώς καθιστά τα αρχεία απροσπέλαστα χωρίς το ιδιωτικό κλειδί αποκρυπτογράφησης.",
        "funFacts": [
            "Η παγκόσμια επίθεση WannaCry το 2017 μόλυνε πάνω από 200.000 υπολογιστές σε 150 χώρες μέσα σε λίγες ώρες, παραλύοντας το εθνικό σύστημα υγείας της Βρετανίας (NHS).",
            "Η καλύτερη άμυνα ενάντια στο ransomware είναι η τακτική διατήρηση αντιγράφων ασφαλείας (backups) σε αποσυνδεδεμένους εξωτερικούς δίσκους."
        ],
        "source": "https://el.wikipedia.org/wiki/Ransomware",
        "tags": ["technology", "security", "ransomware", "malware"]
    },
    {
        "id": "technology_easy_305",
        "text": "Πώς ονομάζεται το μέγιστο εύρος διαμεταγωγής δεδομένων που μπορεί να μεταφέρει μια σύνδεση δικτύου σε δεδομένο χρονικό διάστημα;",
        "correct": "Εύρος ζώνης (Bandwidth)",
        "distractors": ["Latency (Καθυστέρηση)", "Jitter", "Attenuation"],
        "explanation": "Το bandwidth μετράται συνήθως σε Mbps ή Gbps και μοιάζει με το πλάτος ενός αυτοκινητόδρομου: όσο μεγαλύτερο είναι, τόσα περισσότερα δεδομένα μπορούν να περάσουν ταυτόχρονα.",
        "funFacts": [
            "Αν και συχνά συγχέεται με την 'ταχύτητα', το bandwidth αφορά τον όγκο δεδομένων ανά μονάδα χρόνου, ενώ η ταχύτητα απόκρισης καθορίζεται από την καθυστέρηση (latency/ping).",
            "Η μετάβαση από το χάλκινο ADSL στις οπτικές ίνες (FTTH) πολλαπλασίασε το διαθέσιμο bandwidth των νοικοκυριών."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CF%8D%CF%81%CE%BF%CF%82_%CE%B6%CF%8E%CE%BD%CE%B7%CF%82",
        "tags": ["technology", "networking", "bandwidth", "internet"]
    },
    {
        "id": "technology_easy_306",
        "text": "Ποιο βασικό εργαλείο δικτύου μετρά τον χρόνο που χρειάζεται ένα πακέτο δεδομένων για να ταξιδέψει σε έναν απομακρυσμένο διακομιστή και να επιστρέψει;",
        "correct": "Ping (Latency test)",
        "distractors": ["Ipconfig", "Traceroute", "Netstat"],
        "explanation": "Το Ping μετρά τον χρόνο απόκρισης (round-trip time) σε χιλιοστά του δευτερολέπτου (ms), κάτι κρίσιμο για διαδικτυακά παιχνίδια και βιντεοκλήσεις.",
        "funFacts": [
            "Δημιουργήθηκε το 1983 από τον Mike Muuss, ο οποίος εμπνεύστηκε το όνομα από τον ήχο ηχοεντοπισμού (sonar) των υποβρυχίων.",
            "Χρησιμοποιεί πακέτα Echo Request και Echo Reply του πρωτοκόλλου ICMP."
        ],
        "source": "https://el.wikipedia.org/wiki/Ping",
        "tags": ["technology", "networking", "ping", "latency"]
    },
    {
        "id": "technology_easy_307",
        "text": "Πόσα περίπου εικονοστοιχεία (pixels) κατά πλάτος διαθέτει μια οθόνη ανάλυσης 4K Ultra HD;",
        "correct": "Περίπου 4.000 (3.840 x 2.160)",
        "distractors": ["Περίπου 1.000 (1.280 x 720)", "Περίπου 2.000 (1.920 x 1.080)", "Περίπου 8.000 (7.680 x 4.320)"],
        "explanation": "Η ανάλυση 4K UHD στις τηλεοράσεις είναι 3840x2160 pixels, προσφέροντας ακριβώς τετραπλάσια εικονοστοιχεία σε σύγκριση με το παραδοσιακό Full HD (1080p).",
        "funFacts": [
            "Ονομάστηκε '4K' επειδή η οριζόντια ανάλυση πλησιάζει τα 4.000 εικονοστοιχεία.",
            "Στον κινηματογράφο, το πρότυπο DCI 4K ορίζει ελαφρώς διαφορετική ανάλυση 4096x2160 pixels."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CE%AC%CE%BB%CF%85%CF%83%CE%B7_4K",
        "tags": ["technology", "hardware", "display", "resolution"]
    },
    {
        "id": "technology_easy_308",
        "text": "Ποιο είναι το βασικό χαρακτηριστικό των πάνελ οθόνης τεχνολογίας OLED σε σύγκριση με τις κλασικές οθόνες LCD;",
        "correct": "Κάθε πίξελ εκπέμπει το δικό του φως αυτόνομα χωρίς κοινό οπίσθιο φωτισμό",
        "distractors": ["Χρειάζονται ειδικά γυαλιά για προβολή", "Λειτουργούν μόνο σε ασπρόμαυρο χρώμα", "Χρησιμοποιούν υδράργυρο και λάμπες φθορισμού"],
        "explanation": "Στις οθόνες OLED (Organic Light Emitting Diode), κάθε εικονοστοιχείο ανάβει και σβήνει μεμονωμένα, επιτυγχάνοντας τέλειο απόλυτο μαύρο και άπειρη αντίθεση.",
        "funFacts": [
            "Επειδή δεν απαιτούν ξεχωριστό στρώμα οπίσθιου φωτισμού, οι οθόνες OLED μπορούν να είναι εξαιρετικά λεπτές και ακόμη και εύκαμπτες ή αναδιπλούμενες.",
            "Η τεχνολογία αναπτύχθηκε αρχικά στα εργαστήρια της Eastman Kodak από τους Ching W. Tang και Steven Van Slyke τη δεκαετία του 1980."
        ],
        "source": "https://el.wikipedia.org/wiki/OLED",
        "tags": ["technology", "hardware", "oled", "display"]
    },
    {
        "id": "technology_easy_309",
        "text": "Τι υποδηλώνει ο ρυθμός ανανέωσης 120Hz (Hertz) σε μια σύγχρονη οθόνη υπολογιστή ή smartphone;",
        "correct": "Η εικόνα στην οθόνη ανανεώνεται 120 φορές το δευτερόλεπτο",
        "distractors": ["Η οθόνη αντέχει 120 βαθμούς θερμοκρασία", "Η οθόνη καταναλώνει 120 Watt ρεύμα", "Η οθόνη διαθέτει 120 εκατομμύρια πίξελ"],
        "explanation": "Ο ρυθμός ανανέωσης (Refresh Rate) μετράται σε Hertz και δηλώνει πόσες φορές ανά δευτερόλεπτο σχεδιάζεται εκ νέου το περιεχόμενο της οθόνης, προσφέροντας εξαιρετικά ομαλή κίνηση.",
        "funFacts": [
            "Το παραδοσιακό πρότυπο για οθόνες υπολογιστών και τηλεοράσεων ήταν για δεκαετίες τα 60Hz.",
            "Στα smartphones, λειτουργίες όπως το ProMotion της Apple μεταβάλλουν δυναμικά τον ρυθμό από 1Hz (σε στατικές εικόνες για εξοικονόμηση) έως 120Hz (στο σκρολάρισμα)."
        ],
        "source": "https://en.wikipedia.org/wiki/Refresh_rate",
        "tags": ["technology", "hardware", "display", "refresh_rate"]
    },
    {
        "id": "technology_easy_310",
        "text": "Ποιο είναι το όνομα του δορυφορικού συστήματος παροχής διαδικτύου παγκόσμιας κάλυψης που αναπτύσσει η εταιρεία SpaceX του Elon Musk;",
        "correct": "Starlink",
        "distractors": ["OneWeb", "Kuiper", "Iridium"],
        "explanation": "Το Starlink αποτελείται από έναν γιγάντιο αστερισμό χιλιάδων μικρών δορυφόρων σε χαμηλή γήινη τροχιά (LEO), προσφέροντας γρήγορο ίντερνετ χαμηλής καθυστέρησης ακόμη και στις πιο απομακρυσμένες περιοχές.",
        "funFacts": [
            "Οι δορυφόροι πετούν σε ύψος μόλις περίπου 550 χλμ. πάνω από τη Γη, εξασφαλίζοντας πολύ χαμηλότερο ping σε σχέση με τους παραδοσιακούς γεωστάσιμους δορυφόρους στα 36.000 χλμ.",
            "Κάθε εκτόξευση πυραύλου Falcon 9 θέτει σε τροχιά περίπου 20 έως 60 νέους δορυφόρους Starlink ταυτόχρονα."
        ],
        "source": "https://el.wikipedia.org/wiki/Starlink",
        "tags": ["technology", "spacex", "starlink", "satellites"]
    }
]

questions = []
for q in raw_questions:
    opts = [q["correct"]] + q["distractors"]
    random.shuffle(opts)
    c_idx = opts.index(q["correct"])
    questions.append({
        "id": q["id"],
        "categoryId": "technology",
        "difficulty": 1,
        "locale": "el-GR",
        "text": q["text"],
        "answers": opts,
        "correctAnswerIndex": c_idx,
        "explanation": q["explanation"],
        "funFacts": q["funFacts"],
        "source": q["source"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": q["tags"]
    })

if __name__ == "__main__":
    print(f"Loaded {len(questions)} questions for technology_easy batch 2 (261-310).")
    validate_and_append("technology", "easy", 1, questions)

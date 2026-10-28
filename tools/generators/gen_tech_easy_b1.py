# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# Batch 1: technology_easy_211 to technology_easy_260 (50 questions)
raw_questions = [
    {
        "id": "technology_easy_211",
        "text": "Ποια αμερικανική εταιρεία τεχνολογίας κυκλοφόρησε το πρώτο iPhone το 2007;",
        "correct": "Apple",
        "distractors": ["Microsoft", "Google", "IBM"],
        "explanation": "Το πρώτο iPhone παρουσιάστηκε από τον Steve Jobs στις 9 Ιανουαρίου 2007 και κυκλοφόρησε στην αγορά των ΗΠΑ τον Ιούνιο του ίδιου έτους.",
        "funFacts": [
            "Ο Steve Jobs παρουσίασε τη συσκευή ως τρία προϊόντα σε ένα: ένα επαναστατικό κινητό τηλέφωνο, ένα widescreen iPod με οθόνη αφής και μια συσκευή επικοινωνίας μέσω διαδικτύου.",
            "Το πρώτο μοντέλο δεν υποστήριζε συνδέσεις 3G ούτε καταγραφή βίντεο."
        ],
        "source": "https://el.wikipedia.org/wiki/IPhone",
        "tags": ["technology", "apple", "iphone", "smartphones"]
    },
    {
        "id": "technology_easy_212",
        "text": "Πώς ονομάζεται το δημοφιλές λειτουργικό σύστημα για υπολογιστές που αναπτύσσει η Microsoft;",
        "correct": "Windows",
        "distractors": ["Android", "macOS", "Ubuntu"],
        "explanation": "Τα Microsoft Windows κυκλοφόρησαν για πρώτη φορά το 1985 ως γραφικό περιβάλλον για το MS-DOS και παραμένουν το πιο διαδεδομένο λειτουργικό σύστημα για προσωπικούς υπολογιστές.",
        "funFacts": [
            "Τα Windows 95 ήταν η πρώτη έκδοση που εισήγαγε το εμβληματικό κουμπί 'Έναρξη' (Start button) και τη γραμμή εργασιών.",
            "Ο ήχος εκκίνησης των Windows 95 συντέθηκε από τον διάσημο μουσικό Brian Eno."
        ],
        "source": "https://el.wikipedia.org/wiki/Microsoft_Windows",
        "tags": ["technology", "microsoft", "windows", "operating_systems"]
    },
    {
        "id": "technology_easy_213",
        "text": "Ποιο πλήκτρο στο πληκτρολόγιο ενός υπολογιστή χρησιμοποιείται συνήθως για τη διαγραφή του χαρακτήρα στα αριστερά του δρομέα;",
        "correct": "Backspace",
        "distractors": ["Delete", "Enter", "Shift"],
        "explanation": "Το πλήκτρο Backspace διαγράφει χαρακτήρες προς τα πίσω (αριστερά), ενώ το πλήκτρο Delete διαγράφει συνήθως προς τα εμπρός (δεξιά).",
        "funFacts": [
            "Στις παλιές γραφομηχανές, το Backspace απλώς μετακινούσε το φορείο ένα διάστημα πίσω χωρίς να σβήνει μελάνι.",
            "Σε αρκετά πληκτρολόγια της Apple το πλήκτρο ονομάζεται απλώς 'Delete'."
        ],
        "source": "https://en.wikipedia.org/wiki/Backspace",
        "tags": ["technology", "keyboard", "hardware", "peripherals"]
    },
    {
        "id": "technology_easy_214",
        "text": "Ποιο είναι το όνομα του δημοφιλούς προγράμματος περιήγησης ιστού (web browser) που έχει αναπτύξει η Google;",
        "correct": "Google Chrome",
        "distractors": ["Safari", "Mozilla Firefox", "Opera"],
        "explanation": "Το Google Chrome κυκλοφόρησε για πρώτη φορά τον Σεπτέμβριο του 2008 και βασίζεται στο λογισμικό ανοιχτού κώδικα Chromium.",
        "funFacts": [
            "Όταν κυκλοφόρησε, η Google εξέδωσε ένα 38σέλιδο κόμικ από τον Scott McCloud για να εξηγήσει την καινοτόμο αρχιτεκτονική πολλαπλών διεργασιών του περιηγητή.",
            "Είναι σήμερα το πιο ευρέως χρησιμοποιούμενο πρόγραμμα περιήγησης στον κόσμο με μερίδιο αγοράς άνω του 60%."
        ],
        "source": "https://el.wikipedia.org/wiki/Google_Chrome",
        "tags": ["technology", "google", "chrome", "browsers"]
    },
    {
        "id": "technology_easy_215",
        "text": "Τι είδους συσκευή είναι το Amazon Kindle;",
        "correct": "Ηλεκτρονικός αναγνώστης βιβλίων (e-reader)",
        "distractors": ["Έξυπνο ρολόι", "Κονσόλα παιχνιδιών", "Ασύρματο ποντίκι"],
        "explanation": "Το Kindle είναι σειρά συσκευών ηλεκτρονικής ανάγνωσης της Amazon που χρησιμοποιεί τεχνολογία ηλεκτρονικής μελάνης (E Ink) για ξεκούραστη ανάγνωση χωρίς έντονο οπίσθιο φωτισμό.",
        "funFacts": [
            "Το πρώτο Kindle κυκλοφόρησε τον Νοέμβριο του 2007 και εξαντλήθηκε μέσα σε μόλις πεντέμισι ώρες.",
            "Η οθόνη E Ink καταναλώνει ρεύμα σχεδόν αποκλειστικά κατά την αλλαγή της σελίδας, εξασφαλίζοντας αυτονομία εβδομάδων."
        ],
        "source": "https://el.wikipedia.org/wiki/Amazon_Kindle",
        "tags": ["technology", "amazon", "kindle", "gadgets"]
    },
    {
        "id": "technology_easy_216",
        "text": "Ποιο εξάρτημα του υπολογιστή θεωρείται ο 'εγκέφαλός' του και εκτελεί τις περισσότερες εντολές των προγραμμάτων;",
        "correct": "Κεντρική Μονάδα Επεξεργασίας (CPU)",
        "distractors": ["Τροφοδοτικό (PSU)", "Μνήμη RAM", "Σκληρός δίσκος (HDD)"],
        "explanation": "Η CPU (Central Processing Unit) εκτελεί τις βασικές αριθμητικές, λογικές και εντολές ελέγχου εισόδου/εξόδου που ορίζονται από το λογισμικό.",
        "funFacts": [
            "Ο πρώτος εμπορικός μονολιθικός μικροεπεξεργαστής ήταν ο Intel 4004, που κυκλοφόρησε το 1971 με μόλις 2.300 τρανζίστορ.",
            "Οι σύγχρονοι επεξεργαστές υπολογιστών περιέχουν δεκάδες δισεκατομμύρια τρανζίστορ σε επιφάνεια όσο ένα γραμματόσημο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CE%AE_%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CE%95%CF%80%CE%B5%CE%BE%CE%B5%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82",
        "tags": ["technology", "hardware", "cpu", "processors"]
    },
    {
        "id": "technology_easy_217",
        "text": "Ποια εφαρμογή ανταλλαγής μηνυμάτων ανήκει στην εταιρεία Meta (πρώην Facebook) και χρησιμοποιεί τον τηλεφωνικό αριθμό του χρήστη ως αναγνωριστικό;",
        "correct": "WhatsApp",
        "distractors": ["Snapchat", "WeChat", "Slack"],
        "explanation": "Το WhatsApp εξαγοράστηκε από τη Meta (τότε Facebook) το 2014 έναντι περίπου 19 δισεκατομμυρίων δολαρίων και ξεπερνά τους 2 δισεκατομμύρια ενεργούς χρήστες.",
        "funFacts": [
            "Ιδρύθηκε το 2009 από τους Jan Koum και Brian Acton, πρώην εργαζόμενους της Yahoo.",
            "Χρησιμοποιεί από προεπιλογή κρυπτογράφηση από άκρο σε άκρο (end-to-end encryption) για όλα τα μηνύματα και τις κλήσεις."
        ],
        "source": "https://el.wikipedia.org/wiki/WhatsApp",
        "tags": ["technology", "whatsapp", "meta", "messaging"]
    },
    {
        "id": "technology_easy_218",
        "text": "Τι σημαίνουν τα αρχικά του όρου Wi-Fi που χρησιμοποιείται ευρέως για ασύρματη δικτύωση;",
        "correct": "Wireless Fidelity",
        "distractors": ["Wired Fiber", "Wide Internet Fiber", "World Internet Frequency"],
        "explanation": "Αν και το 'Wi-Fi' ξεκίνησε ως λογοπαίγνιο με το 'Hi-Fi' (High Fidelity) από την εταιρεία μάρκετινγκ Interbrand για τη Wi-Fi Alliance, συχνά αναφέρεται ως Wireless Fidelity.",
        "funFacts": [
            "Το πρότυπο πίσω από το Wi-Fi ονομάζεται επίσημα IEEE 802.11.",
            "Τα πρώτα πειράματα που οδήγησαν στην τεχνολογία του Wi-Fi πραγματοποιήθηκαν από ερευνητές ραδιοαστρονομίας στην Αυστραλία."
        ],
        "source": "https://el.wikipedia.org/wiki/Wi-Fi",
        "tags": ["technology", "networking", "wifi", "wireless"]
    },
    {
        "id": "technology_easy_219",
        "text": "Ποιος είναι ο συνιδρυτής της Microsoft που διετέλεσε επί σειρά ετών διευθύνων σύμβουλός της και ένας από τους πλουσιότερους ανθρώπους στον κόσμο;",
        "correct": "Bill Gates",
        "distractors": ["Steve Ballmer", "Larry Ellison", "Jeff Bezos"],
        "explanation": "Ο Bill Gates ίδρυσε τη Microsoft μαζί με τον παιδικό του φίλο Paul Allen το 1975 στο Αλμπουκέρκι του Νέου Μεξικού.",
        "funFacts": [
            "Έγραψε το πρώτο του πρόγραμμα υπολογιστή σε ηλικία 13 ετών, μια εκδοχή της τρίλιζας σε γλώσσα BASIC.",
            "Μετά την αποχώρησή του από την καθημερινή διοίκηση της Microsoft, ίδρυσε το Ίδρυμα Bill & Melinda Gates για παγκόσμια φιλανθρωπία."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CF%80%CE%B9%CE%BB_%CE%93%CE%BA%CE%AD%CE%B9%CF%84%CF%82",
        "tags": ["technology", "microsoft", "bill_gates", "people"]
    },
    {
        "id": "technology_easy_220",
        "text": "Ποιος τύπος υποδοχής καλωδίου αποτελεί το σύγχρονο αναστρέψιμο πρότυπο σύνδεσης και φόρτισης σε τηλέφωνα Android και νεότερα iPhone;",
        "correct": "USB Type-C",
        "distractors": ["Micro-USB", "Mini-USB", "FireWire"],
        "explanation": "Το USB Type-C (ή USB-C) διαθέτει αναστρέψιμο βύσμα 24 ακίδων που επιτρέπει γρήγορη φόρτιση, μεταφορά δεδομένων υψηλής ταχύτητας και έξοδο βίντεο.",
        "funFacts": [
            "Η Ευρωπαϊκή Ένωση θέσπισε νόμο που καθιστά το USB-C κοινό φορτιστή για όλες τις φορητές ηλεκτρονικές συσκευές από το τέλος του 2024.",
            "Σε αντίθεση με τα παλαιότερα USB Type-A, το USB-C εισάγεται και με τις δύο πλευρές χωρίς να χρειάζεται να το γυρίσετε."
        ],
        "source": "https://el.wikipedia.org/wiki/USB-C",
        "tags": ["technology", "hardware", "usb", "cables"]
    },
    {
        "id": "technology_easy_221",
        "text": "Ποια διάσημη πλατφόρμα κοινοποίησης βίντεο ιδρύθηκε το 2005 και εξαγοράστηκε από την Google το 2006;",
        "correct": "YouTube",
        "distractors": ["Vimeo", "Dailymotion", "Twitch"],
        "explanation": "Το YouTube ιδρύθηκε από τους Chad Hurley, Steve Chen και Jawed Karim, πρώην υπαλλήλους της PayPal, και εξαγοράστηκε από την Google έναντι 1,65 δισ. δολαρίων.",
        "funFacts": [
            "Το πρώτο βίντεο που ανέβηκε ποτέ στην πλατφόρμα είχε τίτλο 'Me at the zoo' και δείχνει τον συνιδρυτή Jawed Karim μπροστά σε ελέφαντες στον ζωολογικό κήπο του Σαν Ντιέγκο.",
            "Κάθε λεπτό ανεβαίνουν στο YouTube πάνω από 500 ώρες νέου περιεχομένου βίντεο."
        ],
        "source": "https://el.wikipedia.org/wiki/YouTube",
        "tags": ["technology", "google", "youtube", "video"]
    },
    {
        "id": "technology_easy_222",
        "text": "Πώς ονομάζεται η προσωρινή μνήμη εργασίας του υπολογιστή που χάνει τα δεδομένα της όταν κλείνει το ρεύμα;",
        "correct": "RAM",
        "distractors": ["ROM", "SSD", "Flash Drive"],
        "explanation": "Η RAM (Random Access Memory) είναι πτητική (volatile) μνήμη τυχαίας προσπέλασης που χρησιμοποιείται από τον επεξεργαστή για την άμεση εκτέλεση εφαρμογών.",
        "funFacts": [
            "Ονομάζεται 'τυχαίας προσπέλασης' επειδή οποιοδήποτε byte μνήμης μπορεί να διαβαστεί ή να γραφτεί στον ίδιο ακριβώς χρόνο ανεξάρτητα από τη θέση του.",
            "Στα πρώτα στάδια της πληροφορικής, ως μνήμη RAM χρησιμοποιούνταν μαγνητικοί πυρήνες φερρίτη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BD%CE%AE%CE%BC%CE%B7_%CF%84%CF%85%CF%87%CE%B1%CE%AF%CE%B1%CF%82_%CF%80%CF%81%CE%BF%CF%83%CF%80%CE%AD%CE%BB%CE%B1%CF%83%CE%B7%CF%82",
        "tags": ["technology", "hardware", "ram", "memory"]
    },
    {
        "id": "technology_easy_223",
        "text": "Ποιο σύστημα δορυφορικής πλοήγησης αναπτύχθηκε αρχικά από το Υπουργείο Άμυνας των ΗΠΑ και χρησιμοποιείται παγκοσμίως για εντοπισμό θέσης;",
        "correct": "GPS",
        "distractors": ["Galileo", "GLONASS", "BeiDou"],
        "explanation": "Το GPS (Global Positioning System) αποτελείται από έναν αστερισμό τουλάχιστον 24 δορυφόρων σε τροχιά γύρω από τη Γη που επιτρέπουν σε συμβατές συσκευές να υπολογίζουν τη θέση τους.",
        "funFacts": [
            "Για τον ακριβή προσδιορισμό θέσης σε τρεις διαστάσεις και χρόνο απαιτείται σήμα από τουλάχιστον 4 δορυφόρους ταυτόχρονα.",
            "Τα ατομικά ρολόγια των δορυφόρων GPS πρέπει να ρυθμίζονται λαμβάνοντας υπόψη τη Θεωρία της Σχετικότητας του Einstein για να μη χάνουν περίπου 38 μικροδευτερόλεπτα την ημέρα."
        ],
        "source": "https://el.wikipedia.org/wiki/GPS",
        "tags": ["technology", "gps", "navigation", "satellites"]
    },
    {
        "id": "technology_easy_224",
        "text": "Ποια είναι η δημοφιλής εφαρμογή περιήγησης και χαρτών της Apple που είναι προεγκατεστημένη σε συσκευές iPhone και iPad;",
        "correct": "Apple Maps",
        "distractors": ["Waze", "HERE WeGo", "MapQuest"],
        "explanation": "Οι Apple Maps κυκλοφόρησαν το 2012 αντικαθιστώντας τους Google Maps ως την προεπιλεγμένη εφαρμογή πλοήγησης στο iOS.",
        "funFacts": [
            "Κατά την αρχική κυκλοφορία του το 2012 το σύστημα είχε αρκετά λάθη σε τοπωνύμια, οδηγώντας τον CEO Tim Cook σε δημόσια απολογία.",
            "Σήμερα προσφέρει εξαιρετικά λεπτομερείς τρισδιάστατες απεικονίσεις κτιρίων και πόλεων (Flyover)."
        ],
        "source": "https://en.wikipedia.org/wiki/Apple_Maps",
        "tags": ["technology", "apple", "maps", "navigation"]
    },
    {
        "id": "technology_easy_225",
        "text": "Πώς ονομάζεται το κακόβουλο λογισμικό που μολύνει έναν υπολογιστή και μπορεί να αντιγράψει τον εαυτό του;",
        "correct": "Ιός υπολογιστή (Computer Virus)",
        "distractors": ["Firewall", "Driver", "Codec"],
        "explanation": "Ο ιός υπολογιστή είναι τύπος κακόβουλου λογισμικού (malware) που, όταν εκτελεστεί, αναπαράγεται τροποποιώντας άλλα προγράμματα και εισάγοντας τον δικό του κώδικα.",
        "funFacts": [
            "Ο πρώτος γνωστός ιός για προσωπικούς υπολογιστές PC ονομαζόταν 'Brain' και δημιουργήθηκε το 1986 στο Πακιστάν από δύο αδέρφια.",
            "Ο όρος 'computer virus' επινοήθηκε επίσημα το 1983 από τον καθηγητή Fred Cohen."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%99%CF%8C%CF%82_%CF%85%CF%80%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CF%83%CF%84%CE%AE",
        "tags": ["technology", "security", "malware", "virus"]
    },
    {
        "id": "technology_easy_226",
        "text": "Ποια εταιρεία κατασκευάζει τα δημοφιλή smartphones της σειράς 'Galaxy';",
        "correct": "Samsung",
        "distractors": ["Xiaomi", "Huawei", "Sony"],
        "explanation": "Η Samsung Electronics, με έδρα τη Νότια Κορέα, κυκλοφόρησε το πρώτο smartphone της σειράς Samsung Galaxy το 2009 βασισμένο στο λειτουργικό Android.",
        "funFacts": [
            "Η Samsung ξεκίνησε το 1938 ως εμπορική εταιρεία που εξήγαγε αποξηραμένα ψάρια, λαχανικά και νουντλς.",
            "Η λέξη 'Samsung' στα κορεατικά σημαίνει 'τρία αστέρια'."
        ],
        "source": "https://el.wikipedia.org/wiki/Samsung",
        "tags": ["technology", "samsung", "galaxy", "smartphones"]
    },
    {
        "id": "technology_easy_227",
        "text": "Ποια είναι η μονάδα μέτρησης της ανάλυσης μιας ψηφιακής φωτογραφικής κάμερας που ισούται με ένα εκατομμύριο εικονοστοιχεία;",
        "correct": "Megapixel",
        "distractors": ["Gigahertz", "Terabyte", "Milliamperώριο"],
        "explanation": "Το Megapixel (MP) αντιστοιχεί σε 1.000.000 pixel και καθορίζει τη μέγιστη λεπτομέρεια και διαστάσεις της ψηφιακής εικόνας που καταγράφει ο αισθητήρας.",
        "funFacts": [
            "Μια εικόνα Full HD (1920x1080) αντιστοιχεί σε περίπου 2,07 Megapixels.",
            "Η πρώτη ψηφιακή κάμερα που κατασκεύασε ο Steven Sasson στην Kodak το 1975 είχε ανάλυση μόλις 0,01 Megapixels (100x100 pixel)."
        ],
        "source": "https://el.wikipedia.org/wiki/Pixel",
        "tags": ["technology", "cameras", "photography", "pixels"]
    },
    {
        "id": "technology_easy_228",
        "text": "Ποια διάσημη πλατφόρμα κοινωνικής δικτύωσης ίδρυσε ο Mark Zuckerberg το 2004 όσο ήταν φοιτητής στο Χάρβαρντ;",
        "correct": "Facebook",
        "distractors": ["MySpace", "LinkedIn", "Tumblr"],
        "explanation": "Το Facebook ξεκίνησε ως 'Thefacebook' τον Φεβρουάριο του 2004 για τους φοιτητές του Πανεπιστημίου Harvard και αργότερα επεκτάθηκε παγκοσμίως.",
        "funFacts": [
            "Το μπλε χρώμα επιλέχθηκε ως κυρίαρχο επειδή ο Mark Zuckerberg έχει δυσχρωματοψία στο κόκκινο και το πράσινο και βλέπει καλύτερα το μπλε.",
            "Το 2021 η μητρική εταιρεία μετονομάστηκε σε Meta Platforms ώστε να αντικατοπτρίζει την εστίασή της στο Metaverse."
        ],
        "source": "https://el.wikipedia.org/wiki/Facebook",
        "tags": ["technology", "meta", "facebook", "social_media"]
    },
    {
        "id": "technology_easy_229",
        "text": "Ποια είναι η πιο συνηθισμένη μορφή αρχείων για ηλεκτρονικά έγγραφα σταθερής διάταξης που δημιουργήθηκε από την Adobe;",
        "correct": "PDF",
        "distractors": ["DOCX", "TXT", "XLSX"],
        "explanation": "Το PDF (Portable Document Format) αναπτύχθηκε από την Adobe το 1993 για να παρουσιάζει έγγραφα ανεξάρτητα από λειτουργικό σύστημα ή υλικό.",
        "funFacts": [
            "Το 2008 το πρότυπο PDF έγινε επίσημα ανοιχτό διεθνές πρότυπο ISO (ISO 32000-1).",
            "Ο αρχικός συνιδρυτής της Adobe, John Warnock, ξεκίνησε το πρότζεκτ με την κωδική ονομασία 'Camelot'."
        ],
        "source": "https://el.wikipedia.org/wiki/PDF",
        "tags": ["technology", "adobe", "pdf", "documents"]
    },
    {
        "id": "technology_easy_230",
        "text": "Ποιο σύμβολο χρησιμοποιείται υποχρεωτικά σε κάθε διεύθυνση ηλεκτρονικού ταχυδρομείου (email) για να διαχωρίζει το όνομα χρήστη από τον τομέα;",
        "correct": "@ (παπάκι)",
        "distractors": ["# (δίεση)", "& (και)", "$ (δολάριο)"],
        "explanation": "Το σύμβολο @ (at sign) επιλέχθηκε από τον Ray Tomlinson το 1971 κατά την αποστολή του πρώτου μηνύματος δικτυακού ηλεκτρονικού ταχυδρομείου μέσω ARPANET.",
        "funFacts": [
            "Στα ελληνικά αποκαλείται χαϊδευτικά 'παπάκι', στα ιταλικά 'chiocciola' (σαλιγκάρι) και στα εβραϊκά 'strudel'.",
            "Πριν την εποχή του email, το σύμβολο χρησιμοποιούνταν κυρίως στο εμπόριο για να δηλώσει τιμή ανά μονάδα (π.χ. 5 apples @ 10 cents)."
        ],
        "source": "https://el.wikipedia.org/wiki/@",
        "tags": ["technology", "email", "internet", "history"]
    },
    {
        "id": "technology_easy_231",
        "text": "Ποιο εξάρτημα αποθήκευσης δεν έχει κινούμενα μηχανικά μέρη και είναι πολύ ταχύτερο από τον παραδοσιακό σκληρό δίσκο (HDD);",
        "correct": "SSD (Solid State Drive)",
        "distractors": ["Οπτικός δίσκος CD", "Μαγνητική ταινία", "Δισκέτα (Floppy Disk)"],
        "explanation": "Οι δίσκοι SSD χρησιμοποιούν μνήμη flash NAND για να αποθηκεύουν δεδομένα ηλεκτρονικά, προσφέροντας σχεδόν μηδενικό χρόνο αναζήτησης και πολύ μεγαλύτερη αξιοπιστία.",
        "funFacts": [
            "Επειδή δεν έχουν μηχανικές κεφαλές και περιστρεφόμενους δίσκους, οι SSD είναι απολύτως αθόρυβοι και αντέχουν σε πτώσεις.",
            "Η ταχύτητα ανάγνωσης ενός σύγχρονου NVMe SSD μπορεί να ξεπεράσει τα 7.000 MB/s, έναντι μόλις 150-200 MB/s ενός κλασικού HDD."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1_%CF%83%CF%84%CE%B5%CF%81%CE%B5%CE%AC%CF%82_%CE%BA%CE%B1%CF%84%CE%AC%CF%83%CF%84%CE%B1%CF%83%CE%B7%CF%82",
        "tags": ["technology", "hardware", "ssd", "storage"]
    },
    {
        "id": "technology_easy_232",
        "text": "Πώς ονομάζεται η ψηφιακή βοηθός φωνητικών εντολών που είναι ενσωματωμένη στις συσκευές της Apple;",
        "correct": "Siri",
        "distractors": ["Alexa", "Cortana", "Bixby"],
        "explanation": "Η Siri ενσωματώθηκε για πρώτη φορά στο iPhone 4S το 2011, επιτρέποντας στους χρήστες να στέλνουν μηνύματα, να ρυθμίζουν υπενθυμίσεις και να κάνουν αναζητήσεις μέσω φωνής.",
        "funFacts": [
            "Η Siri αναπτύχθηκε αρχικά ως ανεξάρτητη εφαρμογή από το SRI International Artificial Intelligence Center πριν εξαγοραστεί από την Apple.",
            "Το όνομα 'Siri' είναι σκανδιναβικής προέλευσης και σημαίνει 'όμορφη νικήτρια'."
        ],
        "source": "https://el.wikipedia.org/wiki/Siri",
        "tags": ["technology", "apple", "siri", "voice_assistant"]
    },
    {
        "id": "technology_easy_233",
        "text": "Ποιος είναι ο συνιδρυτής της Apple που παρουσίασε ιστορικά προϊόντα όπως ο Macintosh, το iPod και το iPad φορώντας συχνά μαύρο ζιβάγκο;",
        "correct": "Steve Jobs",
        "distractors": ["Tim Cook", "Jony Ive", "Steve Wozniak"],
        "explanation": "Ο Steve Jobs συνίδρυσε την Apple το 1976 στο γκαράζ των γονιών του και υπήρξε ηγετική μορφή στην επανάσταση των προσωπικών υπολογιστών και smartphones.",
        "funFacts": [
            "Είχε αγοράσει και χρηματοδοτήσει την εταιρεία κινούμενων σχεδίων Pixar, η οποία δημιούργησε το Toy Story, καθιστώντας τον δισεκατομμυριούχο.",
            "Τα χαρακτηριστικά μαύρα ζιβάγκο που φορούσε είχαν σχεδιαστεί αποκλειστικά για εκείνον από τον Ιάπωνα σχεδιαστή Issey Miyake."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A3%CF%84%CE%B9%CE%B2_%CE%A4%CE%B6%CE%BF%CE%BC%CF%80%CF%82",
        "tags": ["technology", "apple", "steve_jobs", "people"]
    },
    {
        "id": "technology_easy_234",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ασφαλούς επικοινωνίας στο διαδίκτυο που εμφανίζει ένα λουκέτο στη γραμμή διευθύνσεων του browser;",
        "correct": "HTTPS",
        "distractors": ["FTP", "SMTP", "Telnet"],
        "explanation": "Το HTTPS (Hypertext Transfer Protocol Secure) κρυπτογραφεί τα δεδομένα που ανταλλάσσονται μεταξύ του προγράμματος περιήγησης και του διακομιστή χρησιμοποιώντας TLS/SSL.",
        "funFacts": [
            "Χωρίς το 'S' (HTTPS), οποιοσδήποτε ενδιάμεσος στο ίδιο δίκτυο (π.χ. σε δημόσιο Wi-Fi) θα μπορούσε να διαβάσει τους κωδικούς σας σε απλό κείμενο.",
            "Σήμερα πάνω από το 95% της παγκόσμιας κίνησης στο διαδίκτυο διεξάγεται μέσω HTTPS."
        ],
        "source": "https://el.wikipedia.org/wiki/HTTPS",
        "tags": ["technology", "internet", "security", "https"]
    },
    {
        "id": "technology_easy_235",
        "text": "Ποια διάσημη πλατφόρμα αναπαραγωγής μουσικής και podcast ιδρύθηκε στη Σουηδία το 2006 από τους Daniel Ek και Martin Lorentzon;",
        "correct": "Spotify",
        "distractors": ["Deezer", "Tidal", "SoundCloud"],
        "explanation": "Το Spotify έφερε επανάσταση στη μουσική βιομηχανία προσφέροντας νόμιμο streaming εκατομμυρίων τραγουδιών με μηνιαία συνδρομή ή δωρεάν με διαφημίσεις.",
        "funFacts": [
            "Το όνομα 'Spotify' προέκυψε κατά λάθος όταν ο Daniel Ek παρερμήνευσε μια λέξη που φώναξε ο Martin Lorentzon από άλλο δωμάτιο.",
            "Το τραγούδι 'Blinding Lights' του The Weeknd ήταν το πρώτο κομμάτι στην ιστορία της πλατφόρμας που ξεπέρασε τα 4 δισεκατομμύρια streams."
        ],
        "source": "https://el.wikipedia.org/wiki/Spotify",
        "tags": ["technology", "spotify", "music", "streaming"]
    },
    {
        "id": "technology_easy_236",
        "text": "Πώς ονομάζεται το σύστημα οπτικής αναγνώρισης δισδιάστατου γραμμωτού κώδικα (matrix barcode) που διαβάζεται εύκολα από κάμερες κινητών;",
        "correct": "QR Code",
        "distractors": ["RFID", "UPC Barcode", "NFC Tag"],
        "explanation": "Το QR Code (Quick Response Code) αναπτύχθηκε το 1994 από την ιαπωνική εταιρεία Denso Wave για την παρακολούθηση εξαρτημάτων στην αυτοκινητοβιομηχανία.",
        "funFacts": [
            "Ο δημιουργός του, Masahiro Hara, εμπνεύστηκε τη σχεδίασή του από το παραδοσιακό επιτραπέζιο παιχνίδι Go.",
            "Τα τρία μεγάλα τετράγωνα στις γωνίες χρησιμεύουν ώστε ο αναγνώστης να αντιλαμβάνεται άμεσα τον προσανατολισμό και τη γωνία του κωδικού."
        ],
        "source": "https://el.wikipedia.org/wiki/QR_code",
        "tags": ["technology", "qr_code", "barcodes", "gadgets"]
    },
    {
        "id": "technology_easy_237",
        "text": "Ποιο είναι το όνομα του δημοφιλούς προγράμματος υπολογιστικών φύλλων της σουίτας Microsoft Office;",
        "correct": "Excel",
        "distractors": ["Word", "PowerPoint", "Access"],
        "explanation": "Το Microsoft Excel κυκλοφόρησε για πρώτη φορά το 1985 για υπολογιστές Macintosh και το 1987 για τα Windows, αποτελώντας το κυρίαρχο λογισμικό φύλλων εργασίας παγκοσμίως.",
        "funFacts": [
            "Κάθε φύλλο εργασίας στο σύγχρονο Excel διαθέτει ακριβώς 1.048.576 γραμμές και 16.384 στήλες.",
            "Υπάρχει παγκόσμιο πρωτάθλημα στο Excel (Financial Modeling World Cup) που μεταδίδεται ζωντανά όπως τα esports."
        ],
        "source": "https://el.wikipedia.org/wiki/Microsoft_Excel",
        "tags": ["technology", "microsoft", "excel", "software"]
    },
    {
        "id": "technology_easy_238",
        "text": "Ποια τεχνολογία ασύρματης επικοινωνίας μικρής εμβέλειας χρησιμοποιείται στα smartphones για ανέπαφες πληρωμές σε τερματικά POS;",
        "correct": "NFC",
        "distractors": ["Infrared (IR)", "Zigbee", "WiMax"],
        "explanation": "Το NFC (Near Field Communication) επιτρέπει σε δύο ηλεκτρονικές συσκευές να επικοινωνούν ασύρματα σε απόσταση λίγων εκατοστών (συνήθως κάτω από 4 εκ.).",
        "funFacts": [
            "Βασίζεται στην αρχή της ηλεκτρομαγνητικής επαγωγής από την τεχνολογία RFID.",
            "Εκτός από πληρωμές μέσω Apple Pay και Google Wallet, χρησιμοποιείται και για άμεση σύζευξη αξεσουάρ ή ανάγνωση ηλεκτρονικών εισιτηρίων."
        ],
        "source": "https://el.wikipedia.org/wiki/NFC",
        "tags": ["technology", "nfc", "smartphones", "payments"]
    },
    {
        "id": "technology_easy_239",
        "text": "Ποια μηχανή αναζήτησης στο διαδίκτυο αναπτύσσει και συντηρεί η Microsoft;",
        "correct": "Bing",
        "distractors": ["Yahoo!", "DuckDuckGo", "Baidu"],
        "explanation": "Το Bing κυκλοφόρησε από τη Microsoft το 2009 ως διάδοχος των προηγούμενων υπηρεσιών Live Search και MSN Search.",
        "funFacts": [
            "Το Bing ήταν από τις πρώτες μεγάλες μηχανές αναζήτησης που ενσωμάτωσαν μοντέλο τεχνητής νοημοσύνης (Copilot) βασισμένο στο GPT-4 το 2023.",
            "Η αρχική σελίδα του Bing ξεχωρίζει καθημερινά για την υψηλής ανάλυσης φωτογραφία τοπίου ή άγριας ζωής που προβάλλει."
        ],
        "source": "https://el.wikipedia.org/wiki/Bing",
        "tags": ["technology", "microsoft", "bing", "search"]
    },
    {
        "id": "technology_easy_240",
        "text": "Πώς ονομάζεται το μικρό φορητό μέσο αποθήκευσης που συνδέεται απευθείας σε θύρα υπολογιστή και λέγεται συχνά 'φλασάκι';",
        "correct": "USB Flash Drive",
        "distractors": ["Punch card", "Zip disk", "Magnetic tape"],
        "explanation": "Το USB flash drive ενσωματώνει μνήμη flash με διεπαφή USB, αντικαθιστώντας πλήρως τις παλιές δισκέτες και τα επανεγγράψιμα CD/DVD.",
        "funFacts": [
            "Κυκλοφόρησε εμπορικά γύρω στο 2000 με χωρητικότητα μόλις 8 Megabytes.",
            "Μία από τις πρωτοπόρες εταιρείες στην κατοχύρωση της πατέντας του ήταν η ισραηλινή M-Systems."
        ],
        "source": "https://el.wikipedia.org/wiki/USB_flash_drive",
        "tags": ["technology", "hardware", "usb", "storage"]
    },
    {
        "id": "technology_easy_241",
        "text": "Ποιο είναι το όνομα του διαβόητου τύπου ανεπιθύμητων ηλεκτρονικών μηνυμάτων που αποστέλλονται μαζικά σε εκατομμύρια παραλήπτες;",
        "correct": "Spam",
        "distractors": ["Bait", "Scrap", "Trash"],
        "explanation": "Ο όρος 'spam' για τα ανεπιθύμητα μαζικά μηνύματα καθιερώθηκε από ένα διάσημο σκετς των Monty Python, όπου οι χαρακτήρες επαναλάμβαναν ενοχλητικά τη λέξη SPAM.",
        "funFacts": [
            "Το SPAM είναι στην πραγματικότητα εμπορικό σήμα κονσερβοποιημένου χοιρινού κρέατος της αμερικανικής εταιρείας Hormel Foods από το 1937.",
            "Υπολογίζεται ότι πάνω από το 45% του συνόλου των email που αποστέλλονται καθημερινά παγκοσμίως αποτελούν spam."
        ],
        "source": "https://el.wikipedia.org/wiki/Spam",
        "tags": ["technology", "email", "security", "spam"]
    },
    {
        "id": "technology_easy_242",
        "text": "Ποια είναι η δημοφιλής υπηρεσία αποθήκευσης και συγχρονισμού αρχείων στο cloud που προσφέρει η Apple;",
        "correct": "iCloud",
        "distractors": ["Google Drive", "OneDrive", "Dropbox"],
        "explanation": "Το iCloud κυκλοφόρησε το 2011 από την Apple και επιτρέπει στους χρήστες να αποθηκεύουν φωτογραφίες, έγγραφα και αντίγραφα ασφαλείας συσκευών.",
        "funFacts": [
            "Αντικατέστησε την παλαιότερη συνδρομητική υπηρεσία MobileMe της Apple.",
            "Κάθε κάτοχος Apple ID λαμβάνει δωρεάν 5 GB αποθηκευτικού χώρου στο cloud."
        ],
        "source": "https://el.wikipedia.org/wiki/ICloud",
        "tags": ["technology", "apple", "icloud", "cloud"]
    },
    {
        "id": "technology_easy_243",
        "text": "Ποιο εξάρτημα ενός υπολογιστή είναι υπεύθυνο για την απόδοση γραφικών και τη σύνδεση με την οθόνη;",
        "correct": "Κάρτα γραφικών (GPU)",
        "distractors": ["Κάρτα ήχου", "Τροφοδοτικό", "Κάρτα δικτύου"],
        "explanation": "Η GPU (Graphics Processing Unit) ή κάρτα γραφικών αναλαμβάνει τη σύνθεση και επεξεργασία εικόνων, 3D γραφικών και βίντεο για προβολή στην οθόνη.",
        "funFacts": [
            "Λόγω της παράλληλης αρχιτεκτονικής τους με χιλιάδες μικρούς πυρήνες, οι σύγχρονες GPUs χρησιμοποιούνται εντατικά στην εκπαίδευση μοντέλων τεχνητής νοημοσύνης.",
            "Ο όρος 'GPU' διαδόθηκε ευρέως από την Nvidia το 1999 με την κυκλοφορία της GeForce 256."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CE%AC%CF%81%CF%84%CE%B1_%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CF%8E%CE%BD",
        "tags": ["technology", "hardware", "gpu", "graphics"]
    },
    {
        "id": "technology_easy_244",
        "text": "Ποια είναι η επίσημη ψηφιακή πλατφόρμα λήψης εφαρμογών για κινητά τηλέφωνα και τάμπλετ με λειτουργικό Android;",
        "correct": "Google Play Store",
        "distractors": ["App Store", "Microsoft Store", "Steam"],
        "explanation": "Το Google Play Store (αρχικά γνωστό ως Android Market) κυκλοφόρησε το 2008 και φιλοξενεί εκατομμύρια εφαρμογές, παιχνίδια και βιβλία.",
        "funFacts": [
            "Η μετονομασία από Android Market σε Google Play έγινε τον Μάρτιο του 2012.",
            "Μέχρι σήμερα έχουν καταγραφεί πάνω από 2,5 εκατομμύρια διαθέσιμες εφαρμογές στην πλατφόρμα."
        ],
        "source": "https://el.wikipedia.org/wiki/Google_Play",
        "tags": ["technology", "google", "android", "apps"]
    },
    {
        "id": "technology_easy_245",
        "text": "Ποιο εργαλείο ασφαλείας δικτύου ελέγχει την εισερχόμενη και εξερχόμενη κίνηση και μπλοκάρει μη εξουσιοδοτημένες συνδέσεις;",
        "correct": "Τείχος προστασίας (Firewall)",
        "distractors": ["Webcam", "Bluetooth Dongle", "Repeater"],
        "explanation": "Το Firewall λειτουργεί ως προστατευτικό φράγμα μεταξύ ενός ασφαλούς εσωτερικού δικτύου και μη αξιόπιστων εξωτερικών δικτύων όπως το διαδίκτυο.",
        "funFacts": [
            "Ο όρος προέρχεται από την αρχιτεκτονική και την πυροπροστασία, όπου τα 'τείχη πυρός' εμποδίζουν την εξάπλωση μιας πυρκαγιάς από ένα κτίριο σε άλλο.",
            "Μπορεί να υλοποιηθεί είτε ως πρόγραμμα λογισμικού είτε ως εξειδικευμένη αυτόνομη συσκευή υλικού (hardware appliance)."
        ],
        "source": "https://el.wikipedia.org/wiki/Firewall",
        "tags": ["technology", "security", "firewall", "networking"]
    },
    {
        "id": "technology_easy_246",
        "text": "Ποιο σύστημα βιομετρικής ασφάλειας αναγνώρισης προσώπου εισήγαγε η Apple με το iPhone X το 2017;",
        "correct": "Face ID",
        "distractors": ["Touch ID", "Iris Scan", "Knock Code"],
        "explanation": "Το Face ID χρησιμοποιεί την κάμερα TrueDepth, έναν προβολέα κουκκίδων υπέρυθρου φωτός και νευρωνικά δίκτυα για να αναγνωρίζει τρισδιάστατα το πρόσωπο του χρήστη.",
        "funFacts": [
            "Προβάλλει περισσότερες από 30.000 αόρατες κουκκίδες υπερύθρων στο πρόσωπο για να δημιουργήσει έναν λεπτομερή τρισδιάστατο χάρτη βάθους.",
            "Σύμφωνα με την Apple, η πιθανότητα τυχαίου ξεκλειδώματος από άλλον άνθρωπο είναι μία στο εκατομμύριο (έναντι μίας στις 50.000 για το δακτυλικό αποτύπωμα Touch ID)."
        ],
        "source": "https://en.wikipedia.org/wiki/Face_ID",
        "tags": ["technology", "apple", "face_id", "biometrics"]
    },
    {
        "id": "technology_easy_247",
        "text": "Ποια είναι η βασική μονάδα ψηφιακής πληροφορίας σε έναν υπολογιστή που μπορεί να πάρει μόνο την τιμή 0 ή 1;",
        "correct": "Bit",
        "distractors": ["Byte", "Hertz", "Baud"],
        "explanation": "Το Bit (συντομογραφία του Binary Digit) είναι το θεμελιώδες στοιχείο δεδομένων στην ψηφιακή τεχνολογία, ενώ 8 bits σχηματίζουν ένα Byte.",
        "funFacts": [
            "Ο όρος 'bit' προτάθηκε για πρώτη φορά το 1946 από τον στατιστικολόγο John Tukey σε ένα υπόμνημα των Bell Labs.",
            "Η έννοια του δυαδικού ψηφίου θεμελιώθηκε μαθηματικά από τον Claude Shannon στο μνημειώδες άρθρο του για τη θεωρία της πληροφορίας το 1948."
        ],
        "source": "https://el.wikipedia.org/wiki/Bit",
        "tags": ["technology", "computer_science", "bit", "data"]
    },
    {
        "id": "technology_easy_248",
        "text": "Πόσα bits αντιστοιχούν σε ένα Byte πληροφορίας;",
        "correct": "8",
        "distractors": ["4", "16", "32"],
        "explanation": "Ένα Byte αποτελείται από 8 bits και μπορεί να αναπαραστήσει 256 (2^8) διαφορετικές τιμές, επαρκείς για την κωδικοποίηση ενός χαρακτήρα κειμένου ASCII.",
        "funFacts": [
            "Μια ομάδα 4 bits (μισό Byte) ονομάζεται χαριτολογώντας 'Nibble' (ή nybble).",
            "Ο όρος 'byte' επινοήθηκε από τον Werner Buchholz το 1956 κατά τη σχεδίαση του υπολογιστή IBM Stretch."
        ],
        "source": "https://el.wikipedia.org/wiki/Byte",
        "tags": ["technology", "computer_science", "byte", "data"]
    },
    {
        "id": "technology_easy_249",
        "text": "Ποια πλατφόρμα κοινωνικής δικτύωσης επικεντρώνεται στην επαγγελματική δικτύωση και αναζήτηση θέσεων εργασίας;",
        "correct": "LinkedIn",
        "distractors": ["TikTok", "Snapchat", "Instagram"],
        "explanation": "Το LinkedIn ιδρύθηκε το 2002 από τον Reid Hoffman και μέλη της ομάδας της PayPal και εξαγοράστηκε από τη Microsoft το 2016 έναντι 26,2 δισ. δολαρίων.",
        "funFacts": [
            "Είναι η αρχαιότερη από τις μεγάλες σημερινές πλατφόρμες κοινωνικής δικτύωσης, έχοντας ξεκινήσει επίσημα τον Μάιο του 2003.",
            "Αριθμεί πάνω από 900 εκατομμύρια εγγεγραμμένους επαγγελματίες από περισσότερες από 200 χώρες."
        ],
        "source": "https://el.wikipedia.org/wiki/LinkedIn",
        "tags": ["technology", "microsoft", "linkedin", "social_media"]
    },
    {
        "id": "technology_easy_250",
        "text": "Ποιο δημοφιλές μοντέλο τεχνητής νοημοσύνης συνομιλίας κυκλοφόρησε από την εταιρεία OpenAI τον Νοέμβριο του 2022;",
        "correct": "ChatGPT",
        "distractors": ["Watson", "Deep Blue", "AlphaGo"],
        "explanation": "Το ChatGPT βασίζεται σε μεγάλα γλωσσικά μοντέλα (LLMs) και έσπασε ρεκόρ ταχύτερα αναπτυσσόμενης καταναλωτικής εφαρμογής φτάνοντας τα 100 εκατομμύρια χρήστες σε δύο μήνες.",
        "funFacts": [
            "Τα αρχικά 'GPT' σημαίνουν Generative Pre-trained Transformer, αναφερόμενα στην αρχιτεκτονική νευρωνικών δικτύων Transformer.",
            "Η αρχική έκδοση που κυκλοφόρησε δωρεάν στο κοινό βασιζόταν στο μοντέλο GPT-3.5."
        ],
        "source": "https://el.wikipedia.org/wiki/ChatGPT",
        "tags": ["technology", "ai", "chatgpt", "openai"]
    },
    {
        "id": "technology_easy_251",
        "text": "Ποια λειτουργία ενός smartphone επιτρέπει τη μετατροπή του σε σημείο πρόσβασης Wi-Fi για σύνδεση άλλων συσκευών στο ίντερνετ;",
        "correct": "Hotspot (Tethering)",
        "distractors": ["Flight mode", "Do Not Disturb", "Screen mirroring"],
        "explanation": "Η λειτουργία Personal Hotspot επιτρέπει σε φορητούς υπολογιστές ή τάμπλετ να συνδέονται στο διαδίκτυο μέσω των δεδομένων κινητής τηλεφωνίας (4G/5G) του smartphone.",
        "funFacts": [
            "Μπορεί να υλοποιηθεί ασύρματα μέσω Wi-Fi ή Bluetooth, αλλά και ενσύρματα μέσω καλωδίου USB.",
            "Καταναλώνει σημαντική ποσότητα μπαταρίας και δεδομένων, γι' αυτό πολλές συσκευές απενεργοποιούν αυτόματα το hotspot όταν δεν υπάρχουν συνδεδεμένες συσκευές."
        ],
        "source": "https://en.wikipedia.org/wiki/Tethering",
        "tags": ["technology", "smartphones", "hotspot", "networking"]
    },
    {
        "id": "technology_easy_252",
        "text": "Ποιο είναι το όνομα του δημοφιλούς προγράμματος επεξεργασίας κειμένου της σουίτας Microsoft Office;",
        "correct": "Microsoft Word",
        "distractors": ["Photoshop", "Outlook", "Illustrator"],
        "explanation": "Το Microsoft Word κυκλοφόρησε για πρώτη φορά το 1983 για το λειτουργικό σύστημα Xenix και MS-DOS και εισήγαγε τη χρήση του ποντικιού στην επεξεργασία κειμένου.",
        "funFacts": [
            "Ήταν από τα πρώτα προγράμματα που υποστήριξαν την αρχή WYSIWYG ('What You See Is What You Get').",
            "Η προεπιλεγμένη γραμματοσειρά του Word άλλαξε το 2007 από Times New Roman σε Calibri, και το 2024 αντικαταστάθηκε από την Aptos."
        ],
        "source": "https://el.wikipedia.org/wiki/Microsoft_Word",
        "tags": ["technology", "microsoft", "word", "software"]
    },
    {
        "id": "technology_easy_253",
        "text": "Ποια από τις παρακάτω εταιρείες είναι παγκοσμίως διάσημη για την παραγωγή επεξεργαστών για προσωπικούς υπολογιστές και διακομιστές;",
        "correct": "Intel",
        "distractors": ["Adobe", "Spotify", "Netflix"],
        "explanation": "Η Intel Corporation ιδρύθηκε το 1968 από τους Gordon Moore και Robert Noyce και κυριαρχεί στην αρχιτεκτονική επεξεργαστών x86.",
        "funFacts": [
            "Το όνομα 'Intel' προέρχεται από τη σύντμηση των λέξεων Integrated Electronics.",
            "Η πασίγνωστη διαφημιστική εκστρατεία 'Intel Inside' της δεκαετίας του 1990 έκανε τους καταναλωτές να αναζητούν συγκεκριμένη μάρκα επεξεργαστή μέσα στον υπολογιστή τους."
        ],
        "source": "https://el.wikipedia.org/wiki/Intel",
        "tags": ["technology", "intel", "hardware", "processors"]
    },
    {
        "id": "technology_easy_254",
        "text": "Ποιο σύστημα κρυπτογραφημένου ψηφιακού νομίσματος ήταν το πρώτο αποκεντρωμένο κρυπτονόμισμα και δημιουργήθηκε το 2009;",
        "correct": "Bitcoin",
        "distractors": ["Ethereum", "Ripple", "Dogecoin"],
        "explanation": "Το Bitcoin δημιουργήθηκε από ένα άγνωστο άτομο ή ομάδα με το ψευδώνυμο Satoshi Nakamoto και λειτουργεί πάνω σε τεχνολογία blockchain.",
        "funFacts": [
            "Ο μέγιστος αριθμός Bitcoin που θα παραχθούν ποτέ είναι αυστηρά προγραμματισμένος σε 21 εκατομμύρια νομίσματα.",
            "Η πρώτη πραγματική εμπορική συναλλαγή με Bitcoin έγινε το 2010, όταν ένας προγραμματιστής αγόρασε δύο πίτσες για 10.000 Bitcoin."
        ],
        "source": "https://el.wikipedia.org/wiki/Bitcoin",
        "tags": ["technology", "bitcoin", "cryptocurrency", "blockchain"]
    },
    {
        "id": "technology_easy_255",
        "text": "Ποια διάσημη πλατφόρμα κλήσης οχημάτων με οδηγό μέσω εφαρμογής smartphone ιδρύθηκε το 2009 στο Σαν Φρανσίσκο από τους Travis Kalanick και Garrett Camp;",
        "correct": "Uber",
        "distractors": ["Lyft", "Bolt", "Cabify"],
        "explanation": "Η Uber ξεκίνησε αρχικά ως 'UberCab' προσφέροντας πολυτελείς μαύρες κούρσες κατόπιν παραγγελίας από κινητό, φέρνοντας επανάσταση στις αστικές μετακινήσεις.",
        "funFacts": [
            "Η ιδέα γεννήθηκε όταν οι ιδρυτές της δεν μπορούσαν να βρουν ταξί σε μια χιονισμένη νύχτα στο Παρίσι το 2008.",
            "Η Uber επεκτάθηκε αργότερα και στη διανομή φαγητού μέσω της εξαιρετικά επιτυχημένης υπηρεσίας Uber Eats."
        ],
        "source": "https://el.wikipedia.org/wiki/Uber",
        "tags": ["technology", "uber", "apps", "transportation"]
    },
    {
        "id": "technology_easy_256",
        "text": "Ποια είναι η λειτουργία της συντόμευσης πληκτρολογίου Ctrl + C (ή Cmd + C σε Mac) στα περισσότερα λειτουργικά συστήματα;",
        "correct": "Αντιγραφή (Copy)",
        "distractors": ["Επικόλληση (Paste)", "Αποκοπή (Cut)", "Αναίρεση (Undo)"],
        "explanation": "Η συντόμευση Ctrl + C αντιγράφει το επιλεγμένο κείμενο ή αρχείο στο πρόχειρο (clipboard) του λειτουργικού συστήματος χωρίς να το διαγράψει.",
        "funFacts": [
            "Η έννοια της αποκοπής, αντιγραφής και επικόλλησης επινοήθηκε από τον Larry Tesler στο ερευνητικό κέντρο Xerox PARC στις αρχές της δεκαετίας του 1970.",
            "Το αντίστοιχο πλήκτρο επικόλλησης είναι το Ctrl + V, το οποίο επιλέχθηκε επειδή το πλήκτρο 'V' βρίσκεται ακριβώς δίπλα στο 'C' στο πληκτρολόγιο QWERTY."
        ],
        "source": "https://en.wikipedia.org/wiki/Cut,_copy,_and_paste",
        "tags": ["technology", "software", "shortcuts", "keyboard"]
    },
    {
        "id": "technology_easy_257",
        "text": "Ποια είναι η λειτουργία της συντόμευσης πληκτρολογίου Ctrl + Z στα περισσότερα προγράμματα υπολογιστή;",
        "correct": "Αναίρεση της τελευταίας ενέργειας (Undo)",
        "distractors": ["Αποθήκευση αρχείου", "Εκτύπωση εγγράφου", "Κλείσιμο παραθύρου"],
        "explanation": "Η συντόμευση Ctrl + Z αναιρεί την αμέσως προηγούμενη ενέργεια του χρήστη, όπως διαγραφή κειμένου ή σχεδιαστική αλλαγή.",
        "funFacts": [
            "Η επαναφορά της ενέργειας που αναιρέθηκε (Redo) γίνεται συνήθως με τη συντόμευση Ctrl + Y (ή Ctrl + Shift + Z).",
            "Εισήχθη για πρώτη φορά στους υπολογιστές Apple Lisa και Macintosh από την ομάδα της Apple."
        ],
        "source": "https://en.wikipedia.org/wiki/Undo",
        "tags": ["technology", "software", "shortcuts", "keyboard"]
    },
    {
        "id": "technology_easy_258",
        "text": "Πώς ονομάζεται το μικρό γραφικό εικονίδιο ή σύμβολο που χρησιμοποιείται στα ψηφιακά μηνύματα για να εκφράσει συναισθήματα ή αντικείμενα;",
        "correct": "Emoji",
        "distractors": ["Pixel", "Avatar", "Glitch"],
        "explanation": "Τα emojis δημιουργήθηκαν στην Ιαπωνία στα τέλη της δεκαετίας του 1990 και ενσωματώθηκαν επίσημα στο παγκόσμιο πρότυπο Unicode το 2010.",
        "funFacts": [
            "Η λέξη 'emoji' προέρχεται από τις ιαπωνικές λέξεις 'e' (εικόνα) και 'moji' (χαρακτήρας).",
            "Το πρώτο σετ 176 emojis σχεδιάστηκε το 1999 από τον Shigetaka Kurita για την ιαπωνική εταιρεία κινητής τηλεφωνίας NTT DoCoMo και σήμερα εκτίθεται στο Μουσείο Μοντέρνας Τέχνης (MoMA) της Νέας Υόρκης."
        ],
        "source": "https://el.wikipedia.org/wiki/Emoji",
        "tags": ["technology", "emoji", "messaging", "culture"]
    },
    {
        "id": "technology_easy_259",
        "text": "Ποια είναι η επίσημη ψηφιακή πλατφόρμα λήψης εφαρμογών για συσκευές iPhone και iPad της Apple;",
        "correct": "App Store",
        "distractors": ["Galaxy Store", "Amazon Appstore", "Ubuntu Software Center"],
        "explanation": "Το App Store της Apple άνοιξε τις πύλες του τον Ιούλιο του 2008 με μόλις 500 εφαρμογές, εγκαινιάζοντας το σύγχρονο οικοσύστημα εφαρμογών για κινητά.",
        "funFacts": [
            "Μέσα στις πρώτες τρεις ημέρες λειτουργίας του καταγράφηκαν πάνω από 10 εκατομμύρια λήψεις εφαρμογών.",
            "Η διάσημη διαφημιστική ατάκα της Apple 'There's an app for that' κατοχυρώθηκε ως εμπορικό σήμα το 2010."
        ],
        "source": "https://el.wikipedia.org/wiki/App_Store",
        "tags": ["technology", "apple", "app_store", "smartphones"]
    },
    {
        "id": "technology_easy_260",
        "text": "Ποιος κολοσσός του ηλεκτρονικού εμπορίου ιδρύθηκε από τον Jeff Bezos το 1994, αρχικά ως διαδικτυακό βιβλιοπωλείο;",
        "correct": "Amazon",
        "distractors": ["eBay", "Alibaba", "Rakuten"],
        "explanation": "Η Amazon ξεκίνησε τη λειτουργία της από το γκαράζ του Jeff Bezos στο Σιάτλ πουλώντας βιβλία στο ίντερνετ και εξελίχθηκε στον μεγαλύτερο έμπορο λιανικής και πάροχο cloud υποδομών στον κόσμο.",
        "funFacts": [
            "Το αρχικό όνομα που είχε επιλέξει ο Bezos για την εταιρεία ήταν 'Cadabra' (από το abracadabra), αλλά το άλλαξε επειδή ακουγόταν σαν 'cadaver' (πτώμα).",
            "Το βέλος στο λογότυπο της Amazon σχηματίζει χαμόγελο και δείχνει από το γράμμα 'A' στο 'Z', υποδηλώνοντας ότι διαθέτει τα πάντα."
        ],
        "source": "https://el.wikipedia.org/wiki/Amazon",
        "tags": ["technology", "amazon", "ecommerce", "jeff_bezos"]
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
    print(f"Loaded {len(questions)} questions for technology_easy batch 1 (211-260).")
    validate_and_append("technology", "easy", 1, questions)

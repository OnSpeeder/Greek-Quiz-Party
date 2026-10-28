# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_211",
        "text": "Ποιο τεχνικό χαρακτηριστικό της αρχιτεκτονικής του Sega Saturn (1994) με δύο επεξεργαστές Hitachi SH-2 κατέστησε τον προγραμματισμό 3D εξαιρετικά δυσχερή για τους δημιουργούς;",
        "correct": "Η έλλειψη διαμοιραζόμενης μνήμης cache και η απόδοση τετραπλεύρων (quads) αντί για τρίγωνα",
        "distractors": [
            "Η αποκλειστική χρήση 16-bit registers χωρίς υποστήριξη πολυγωνικών πινάκων",
            "Η υποχρεωτική κωδικοποίηση μόνο σε γλώσσα Assembly χωρίς C compiler",
            "Η αδυναμία χρήσης textures πάνω σε τρισδιάστατα μοντέλα"
        ],
        "explanation": "Ο Saturn σχεδιάστηκε αρχικά ως πανίσχυρο 2D μηχάνημα και η προσθήκη δεύτερου SH-2 CPU την τελευταία στιγμή δημιούργησε συμφόρηση στον δίαυλο, ενώ η απόδοση παραμορφωμένων τετραπλεύρων (quads) δυσκόλευε τη μεταφορά παιχνιδιών από PC και PlayStation.",
        "funFacts": [
            "Ο Yu Suzuki είχε δηλώσει ότι μόνο ένα ελάχιστο ποσοστό προγραμματιστών μπορούσε να αξιοποιήσει πλήρως και τους δύο επεξεργαστές του Saturn ταυτόχρονα.",
            "Η Sony εκμεταλλεύτηκε αυτή τη δυσκολία προσφέροντας εξαιρετικές βιβλιοθήκες C και εύκολη γεωμετρία τριγώνων στο PlayStation."
        ],
        "source": "https://en.wikipedia.org/wiki/Sega_Saturn",
        "tags": ["gaming", "sega", "saturn", "hardware", "architecture"]
    },
    {
        "id": "gaming_hard_212",
        "text": "Ποια πρωτοποριακή εταιρεία υπολογιστών γραφικών σχεδίασε το τσιπ Reality Coprocessor (RCP) που τροφοδοτούσε τα γραφικά του Nintendo 64;",
        "correct": "Silicon Graphics International (SGI)",
        "distractors": ["3dfx Interactive", "Nvidia", "ATI Technologies"],
        "explanation": "Η Silicon Graphics του Jim Clark σχεδίασε το RCP (χωρισμένο σε RSP για γεωμετρία και RDP για rasterization), προσφέροντας στο N64 δυνατότητες όπως z-buffering και anti-aliasing.",
        "funFacts": [
            "Η SGI είχε προτείνει αρχικά την τεχνολογία αυτή στον Tom Kalinske της Sega, αλλά η ιαπωνική ηγεσία της Sega την απέρριψε, οδηγώντας την SGI στη Nintendo.",
            "Το πρότζεκτ ήταν γνωστό κατά την ανάπτυξή του με την κωδική ονομασία 'Project Reality' και αργότερα 'Nintendo Ultra 64'."
        ],
        "source": "https://en.wikipedia.org/wiki/Nintendo_64_technical_specifications",
        "tags": ["gaming", "nintendo", "n64", "hardware", "sgi"]
    },
    {
        "id": "gaming_hard_213",
        "text": "Ποιο είναι το όνομα του διαβόητου αστικού μύθου για μια υποτιθέμενη κυβερνητική arcade καμπίνα του 1981 στο Πόρτλαντ του Όρεγκον που προκαλούσε αμνησία και εφιάλτες;",
        "correct": "Polybius",
        "distractors": ["Killswitch", "Pale Luna", "Petscop"],
        "explanation": "Ο αστικός μύθος του Polybius ισχυριζόταν ότι μυστηριώδεις άντρες με μαύρα κοστούμια συνέλεγαν δεδομένα από τις καμπίνες για λογαριασμό μυστικών υπηρεσιών των ΗΠΑ.",
        "funFacts": [
            "Δεν έχει βρεθεί ποτέ καμία πραγματική πλακέτα ή ROM του παιχνιδιού, επιβεβαιώνοντας ότι πρόκειται για καθαρό ιντερνετικό θρύλο.",
            "Το 2017, ο διάσημος προγραμματιστής Jeff Minter δημιούργησε ένα πραγματικό ψυχεδελικό παιχνίδι VR με το όνομα Polybius για το PlayStation 4."
        ],
        "source": "https://en.wikipedia.org/wiki/Polybius_(urban_legend)",
        "tags": ["gaming", "polybius", "urban_legend", "arcade", "retro"]
    },
    {
        "id": "gaming_hard_214",
        "text": "Σε ποια πόλη του Νέου Μεξικού έθαψε η Atari εκατοντάδες χιλιάδες απούλητες κασέτες (όπως το 'E.T.') το 1983, οι οποίες ανασκάφηκαν επίσημα το 2014;",
        "correct": "Αλαμογκόρντο (Alamogordo)",
        "distractors": ["Ρόσγουελ (Roswell)", "Σάντα Φε (Santa Fe)", "Αλμπουκέρκη (Albuquerque)"],
        "explanation": "Η ταφή των κασετών στο Alamogordo θεωρούνταν αστικός μύθος για δεκαετίες, μέχρι που η ανασκαφή του 2014 για το ντοκιμαντέρ 'Atari: Game Over' έφερε στο φως χιλιάδες άθικτες κασέτες.",
        "funFacts": [
            "Ο προγραμματιστής Howard Scott Warshaw είχε μόλις πέντε εβδομάδες στη διάθεσή του για να σχεδιάσει και να προγραμματίσει ολόκληρο το παιχνίδι E.T. για το Atari 2600.",
            "Μερικές από τις ανακτημένες κασέτες πουλήθηκαν σε δημοπρασίες και εκτίθενται σήμερα στο Μουσείο Smithsonian."
        ],
        "source": "https://en.wikipedia.org/wiki/Atari_video_game_burial",
        "tags": ["gaming", "atari", "history", "retro", "et"]
    },
    {
        "id": "gaming_hard_215",
        "text": "Ποιο τεχνικό φαινόμενο στο 'Space Invaders' (1978) του Tomohiro Nishikado δημιούργησε κατά λάθος την πρώτη κλιμακούμενη καμπύλη δυσκολίας στην ιστορία;",
        "correct": "Ο επεξεργαστής σχεδίαζε ταχύτερα τα εναπομείναντα sprites καθώς λιγόστευαν οι εξωγήινοι στην οθόνη",
        "distractors": [
            "Ένα σφάλμα στον χρονιστή που διπλασίαζε τη συχνότητα ρολογιού",
            "Η εξάντληση της μνήμης RAM που επιτάχυνε τον κώδικα κίνησης",
            "Μια κρυφή υπορουτίνα που αύξανε τα frames ανά δευτερόλεπτο"
        ],
        "explanation": "Το υλικό της εποχής δυσκολευόταν να σχεδιάσει και τους 55 εξωγήινους ταυτόχρονα, προκαλώντας επιβράδυνση· καθώς ο παίκτης τους εξόντωνε, ο επεξεργαστής ελάφρυνε και οι υπόλοιποι κινούνταν αυτόματα ταχύτερα.",
        "funFacts": [
            "Αντί να διορθώσει το φαινόμενο, ο Nishikado συνειδητοποίησε ότι έκανε το παιχνίδι συναρπαστικό και το άφησε ως βασικό μηχανισμό.",
            "Το παιχνίδι ήταν τόσο δημοφιλές στην Ιαπωνία που προκάλεσε προσωρινή έλλειψη στα κέρματα των 100 γεν."
        ],
        "source": "https://en.wikipedia.org/wiki/Space_Invaders",
        "tags": ["gaming", "space_invaders", "taito", "retro", "arcade"]
    },
    {
        "id": "gaming_hard_216",
        "text": "Πώς έλυσε ο Chris Roberts ένα επίμονο memory leak crash κατά την έξοδο από το 'Wing Commander' (1990) στο DOS;",
        "correct": "Άλλαξε το μήνυμα σφάλματος του συστήματος σε 'Thank you for playing Wing Commander!'",
        "distractors": [
            "Πρόσθεσε μια εντολή καθαρισμού BIOS πριν το κλείσιμο",
            "Ανακατεύθυνε τη μνήμη σε μια κενή διεύθυνση EMS",
            "Έκανε αναγκαστική επανεκκίνηση του υπολογιστή στο παρασκήνιο"
        ],
        "explanation": "Επειδή το crash συνέβαινε μόνο κατά την έξοδο στο DOS και η προθεσμία κυκλοφορίας πίεζε αφόρητα, ένας προγραμματιστής έκανε hex edit στο μήνυμα σφάλματος ώστε το κείμενο να μοιάζει με ευγενικό χαιρετισμό.",
        "funFacts": [
            "Το τέχνασμα λειτούργησε άψογα και κανένας παίκτης δεν παραπονέθηκε ποτέ για το κρασάρισμα.",
            "Το Wing Commander ήταν ένα από τα πρώτα παιχνίδια PC που εκμεταλλεύτηκαν πλήρως τις κάρτες γραφικών VGA 256 χρωμάτων και τις κάρτες ήχου Sound Blaster."
        ],
        "source": "https://en.wikipedia.org/wiki/Wing_Commander_(video_game)",
        "tags": ["gaming", "wing_commander", "origin_systems", "pc", "programming"]
    },
    {
        "id": "gaming_hard_217",
        "text": "Για ποιο λόγο ο Hironobu Sakaguchi επέλεξε τον τίτλο 'Final Fantasy' για το RPG της Square το 1987 στο Famicom;",
        "correct": "Σκόπευε να παραιτηθεί από τη βιομηχανία αν αποτύγχανε, ενώ και η Square βρισκόταν στα πρόθυρα χρεοκοπίας",
        "distractors": [
            "Επειδή ήταν το τελευταίο παιχνίδι σε μια προγραμματισμένη τριλογία",
            "Λόγω διαφωνίας πνευματικών δικαιωμάτων με τον τίτλο 'Fighting Fantasy'",
            "Επειδή βασιζόταν σε ένα αποκαλυπτικό μυθιστόρημα για το τέλος του κόσμου"
        ],
        "explanation": "Ο Sakaguchi είχε αποφασίσει ότι αν το παιχνίδι δεν πουλούσε θα εγκατέλειπε την ανάπτυξη παιχνιδιών και θα επέστρεφε στο πανεπιστήμιο, κάνοντας αυτό το εγχείρημα την 'τελευταία του φαντασίωση'.",
        "funFacts": [
            "Η αρχική προτίμηση για τον τίτλο ήταν 'Fighting Fantasy', αλλά ήταν ήδη κατοχυρωμένος από μια δημοφιλή σειρά επιτραπέζιων βιβλίων-παιχνιδιών.",
            "Η επιτυχία του Final Fantasy έσωσε τη Square από τη χρεοκοπία πουλώντας πάνω από 500.000 αντίτυπα στην Ιαπωνία."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_(video_game)",
        "tags": ["gaming", "final_fantasy", "square", "sakaguchi", "history"]
    },
    {
        "id": "gaming_hard_218",
        "text": "Μέσα σε πόσο χρονικό διάστημα συνέθεσε ο Koichi Sugiyama ολόκληρο το ιστορικό 8-κομμάτι συμφωνικό soundtrack του πρώτου 'Dragon Quest' (1986);",
        "correct": "Μέσα σε μία εβδομάδα",
        "distractors": ["Μέσα σε έναν μήνα", "Μέσα σε τρεις μήνες", "Μέσα σε μία ημέρα"],
        "explanation": "Ο καταξιωμένος συνθέτης τηλεόρασης και κλασικής μουσικής Koichi Sugiyama έγραψε όλα τα εμβληματικά θέματα του Famicom (συμπεριλαμβανομένου του 'Overture') σε μόλις μία εβδομάδα.",
        "funFacts": [
            "Ο Sugiyama έγινε ο γηραιότερος εν ενεργεία συνθέτης βιντεοπαιχνιδιών στον κόσμο σύμφωνα με το Ρεκόρ Guinness.",
            "Η μουσική του Dragon Quest παρουσιάστηκε ζωντανά στην τελετή έναρξης των Ολυμπιακών Αγώνων του Τόκιο το 2021."
        ],
        "source": "https://en.wikipedia.org/wiki/Koichi_Sugiyama",
        "tags": ["gaming", "dragon_quest", "koichi_sugiyama", "music", "retro"]
    },
    {
        "id": "gaming_hard_219",
        "text": "Ποιο είναι το μυστικό δώρο που λαμβάνει ο παίκτης όταν συλλέξει και τα 120 αστέρια στο 'Super Mario 64' (1996) και εκτοξευτεί στην ταράτσα του κάστρου;",
        "correct": "Συναντά τον Yoshi που του χαρίζει 100 ζωές και ένα ενισχυμένο τριπλό άλμα με λάμψεις",
        "distractors": [
            "Ξεκλειδώνει τον Luigi ως πλήρως διαθέσιμο χαρακτήρα",
            "Αποκτά ένα χρυσό καπέλο με απεριόριστη πτήση",
            "Μπορεί να επισκεφθεί το Mushroom Kingdom σε 2D μορφή"
        ],
        "explanation": "Το κανόνι στον κήπο του κάστρου ανοίγει, εκτοξεύοντας τον Mario στην οροφή όπου ο Yoshi του δίνει 100 ζωές και ένα λαμπερό τριπλό άλμα που αποτρέπει τη ζημιά από πτώση.",
        "funFacts": [
            "Η απουσία του Luigi από το παιχνίδι δημιούργησε τον θρυλικό αστικό μύθο 'L is real 2040' βασισμένο σε μια θολή επιγραφή στο σιντριβάνι της αυλής.",
            "Το 2020, κατά τη διαρροή πηγαίου κώδικα της Nintendo (Gigaleak), βρέθηκαν όντως αρχεία και 3D μοντέλα του Luigi για το Super Mario 64 ακριβώς 24 χρόνια και 1 μήνα μετά την κυκλοφορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_64",
        "tags": ["gaming", "mario", "nintendo", "n64", "secrets"]
    },
    {
        "id": "gaming_hard_220",
        "text": "Ποιο όνομα πρέπει να καταχωρίσει ο παίκτης στην αρχική οθόνη του 'The Legend of Zelda' (1986) στο NES για να παίξει απευθείας το δυσκολότερο 'Second Quest';",
        "correct": "ZELDA",
        "distractors": ["LINK", "GANON", "HYRULE"],
        "explanation": "Ονομάζοντας το αρχείο αποθήκευσης 'ZELDA', ο παίκτης παρακάμπτει το κανονικό παιχνίδι και ξεκινά αμέσως το Second Quest με αναδιαταγμένα μπουντρούμια, νέες παγίδες και αόρατους τοίχους.",
        "funFacts": [
            "Το Second Quest δημιουργήθηκε επειδή ο προγραμματιστής Takashi Tezuka συνειδητοποίησε ότι είχε χρησιμοποιήσει μόνο τη μισή διαθέσιμη χωρητικότητα μνήμης του cartridge.",
            "Στο Second Quest, οι κάτοψεις των πέντε πρώτων μπουντρουμιών σχηματίζουν τα γράμματα Z-E-L-D-A."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)",
        "tags": ["gaming", "zelda", "nintendo", "nes", "secrets"]
    },
    {
        "id": "gaming_hard_221",
        "text": "Ποιον μαθηματικό αλγόριθμο υπολογιστικής γεωμετρίας εφάρμοσε ο John Carmack στο 'Doom' (1993) για την ταχύτατη απόδοση επιφανειών χωρίς z-buffering;",
        "correct": "Binary Space Partitioning (BSP Trees)",
        "distractors": ["Ray Marching", "Octree Voxelization", "Painter's Sorting Algorithm"],
        "explanation": "Τα BSP δέντρα επέτρεπαν στην engine του Doom να ταξινομεί προκαταβολικά όλες τις γραμμές του χάρτη, σχεδιάζοντας τις επιφάνειες από εμπρός προς τα πίσω χωρίς να επανασχεδιάζει τα ίδια pixels (overdraw).",
        "funFacts": [
            "Ο Carmack διάβασε για πρώτη φορά για τα BSP δέντρα σε μια επιστημονική δημοσίευση του Bruce Naylor του 1990 και κατάφερε να τα υλοποιήσει σε λίγες μόλις εβδομάδες.",
            "Χάρη στο BSP, το Doom μπορούσε να τρέχει με ομαλά 35 καρέ ανά δευτερόλεπτο σε απλούς επεξεργαστές Intel 486."
        ],
        "source": "https://en.wikipedia.org/wiki/Doom_engine",
        "tags": ["gaming", "doom", "john_carmack", "programming", "algorithms"]
    },
    {
        "id": "gaming_hard_222",
        "text": "Ποια είναι η διαβόητη δεκαεξαδική σταθερά στον αλγόριθμο ταχείας αντίστροφης τετραγωνικής ρίζας (Fast Inverse Square Root) στον κώδικα του 'Quake III Arena';",
        "correct": "0x5f3759df",
        "distractors": ["0xdeadbeef", "0x3f800000", "0x5f375a86"],
        "explanation": "Η γραμμή 'i = 0x5f3759df - ( i >> 1 );' συνοδευόταν από το ιστορικό σχόλιο στον κώδικα '// what the fuck?', υπολογίζοντας με ακραία ακρίβεια την προσέγγιση του 1/sqrt(x) μέσω της μεθόδου Newton-Raphson.",
        "funFacts": [
            "Αν και αποδόθηκε αρχικά στον John Carmack, η προέλευση του μαγικού αριθμού εντοπίστηκε αργότερα στον Gary Tarolli της 3dfx και στον Greg Walsh της Ardent Computer.",
            "Ο αλγόριθμος ήταν κρίσιμος για τον υπολογισμό γωνιών αντανάκλασης φωτισμού και φυσικής διανυσμάτων σε πραγματικό χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Fast_inverse_square_root",
        "tags": ["gaming", "quake", "programming", "algorithms", "carmack"]
    },
    {
        "id": "gaming_hard_223",
        "text": "Ποιος τεχνικός περιορισμός του υπολογιστή MSX2 οδήγησε τον Hideo Kojima να εφεύρει το gameplay απόκρυψης (stealth) στο αρχικό 'Metal Gear' (1987);",
        "correct": "Ο υπολογιστής μπορούσε να εμφανίσει μόνο περιορισμένα sprites στην ίδια οριζόντια γραμμή πριν αρχίσουν να τρεμοπαίζουν",
        "distractors": [
            "Η έλλειψη κυλιόμενης οθόνης (scrolling) απαιτούσε στατικά δωμάτια",
            "Η κάρτα ήχου δεν υποστήριζε εφέ πυροβολισμών και εκρήξεων",
            "Η μνήμη RAM των 64KB δεν επαρκούσε για την αποθήκευση σφαιρών"
        ],
        "explanation": "Η Konami ζήτησε ένα παιχνίδι δράσης τύπου Commando, αλλά επειδή το hardware του MSX2 δεν άντεχε πολλούς εχθρούς και σφαίρες ταυτόχρονα, ο Kojima αποφάσισε ότι ο παίκτης έπρεπε να αποφεύγει τη μάχη.",
        "funFacts": [
            "Η ηγεσία της Konami ήταν αρχικά τόσο αντίθετη με την ιδέα ενός πολεμικού παιχνιδιού χωρίς διαρκείς πυροβολισμούς που απείλησε να ακυρώσει το έργο.",
            "Η εισαγωγή του θαυμαστικού '!' και του χαρακτηριστικού ήχου συναγερμού παραμένει από τότε το σήμα κατατεθέν της σειράς."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_(video_game)",
        "tags": ["gaming", "metal_gear", "hideo_kojima", "msx", "history"]
    },
    {
        "id": "gaming_hard_224",
        "text": "Ποιο Famicom παιχνίδι τρόμου του 1989 της Capcom, σκηνοθετημένο από τον Tokuro Fujiwara, αποτέλεσε την άμεση πηγή έμπνευσης για το 'Resident Evil';",
        "correct": "Sweet Home",
        "distractors": ["Clock Tower", "Alone in the Dark", "Splatterhouse"],
        "explanation": "Το Sweet Home περιλάμβανε έρευνα σε μια στοιχειωμένη έπαυλη, περιορισμένο χώρο αντικειμένων (inventory), σημειώσεις ημερολογίων και το εμβληματικό animation ανοίγματος πόρτας για τη φόρτωση δωματίων.",
        "funFacts": [
            "Το Resident Evil ξεκίνησε αρχικά ως επίσημο remake του Sweet Home πριν εξελιχθεί σε αυτόνομο franchise με ζόμπι.",
            "Ο Shinji Mikami προσλήφθηκε από τον Tokuro Fujiwara ειδικά για να αναλάβει τη σκηνοθεσία του νέου αυτού πρότζεκτ στο PlayStation."
        ],
        "source": "https://en.wikipedia.org/wiki/Sweet_Home_(video_game)",
        "tags": ["gaming", "resident_evil", "capcom", "sweet_home", "retro"]
    },
    {
        "id": "gaming_hard_225",
        "text": "Ποιος Ιάπωνας δημιουργός έγραψε και σκηνοθέτησε το αρχικό 'Silent Hill' (1999) πριν αποχωρήσει από την Konami για να δημιουργήσει τις σειρές 'Siren' και 'Gravity Rush';",
        "correct": "Keiichiro Toyama",
        "distractors": ["Akira Yamaoka", "Takayoshi Sato", "Masahiro Ito"],
        "explanation": "Ο Keiichiro Toyama ηγήθηκε της νεοσύστατης 'Team Silent', εμπνευσμένος από τη δυτική λογοτεχνία τρόμου (Stephen King, Dean Koontz) και τις ταινίες του David Lynch.",
        "funFacts": [
            "Ο Toyama εντάχθηκε στα Japan Studio της Sony και αργότερα ίδρυσε το ανεξάρτητο στούντιο Bokeh Game Studio αναπτύσσοντας το Slitterhead.",
            "Ο σχεδιαστής χαρακτήρων Takayoshi Sato κοιμόταν στο γραφείο για μήνες για να δημιουργήσει μόνος του τα CGI cutscenes του πρώτου και δεύτερου παιχνιδιού."
        ],
        "source": "https://en.wikipedia.org/wiki/Keiichiro_Toyama",
        "tags": ["gaming", "silent_hill", "keiichiro_toyama", "team_silent", "creators"]
    },
    {
        "id": "gaming_hard_226",
        "text": "Ποιο βρετανικό στούντιο υπό τον Jez San ανέπτυξε το συνεπεξεργαστή Super FX (τσιπ επιτάχυνσης 3D) για το cartridge του 'Star Fox' (1993) στο SNES;",
        "correct": "Argonaut Games",
        "distractors": ["Rare", "Psygnosis", "Factor 5"],
        "explanation": "Η Argonaut Software σχεδίασε το τσιπ Super FX (αρχικά με κωδικό MARS - Mathematical Applications Racing System), επιτρέποντας στο Super Nintendo να σχεδιάζει εκατοντάδες 3D πολύγωνα το δευτερόλεπτο.",
        "funFacts": [
            "Το τσιπ Super FX ήταν στην πραγματικότητα ταχύτερο από τον ίδιο τον κεντρικό επεξεργαστή του Super Nintendo.",
            "Η Argonaut ανέπτυξε αργότερα το τρισδιάστατο platformer 'Croc: Legend of the Gobbos', το οποίο ξεκίνησε αρχικά ως πρωτότυπο παιχνίδι με τον Yoshi για τη Nintendo."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_FX",
        "tags": ["gaming", "star_fox", "argonaut", "nintendo", "hardware"]
    },
    {
        "id": "gaming_hard_227",
        "text": "Ποιος διαβόητος κωδικός πρόσβασης στο πρώτο 'Metroid' (1986) του NES εμφάνιζε τη Samus χωρίς την πανοπλία της φορώντας ροζ κορμάκι;",
        "correct": "JUSTIN BAILEY ------ ------",
        "distractors": ["NARPAS SWORD0 000000 000000", "SAMUS ARAN00 000000 000000", "METROID SUIT0 000000 000000"],
        "explanation": "Ο κωδικός 'JUSTIN BAILEY' εκμεταλλευόταν τη δομή του αλγορίθμου κρυπτογράφησης των passwords του NES, δίνοντας στη Samus όλες τις αναβαθμίσεις και μέγιστους πυραύλους.",
        "funFacts": [
            "Για χρόνια κυκλοφορούσε ο μύθος ότι ο Justin Bailey ήταν προγραμματιστής της Nintendo, αλλά στην πραγματικότητα ήταν απλώς μια τυχαία φράση που ταίριαζε στα byte patterns.",
            "Ο επίσημος κωδικός ατρωσίας που είχαν προγραμματίσει οι δημιουργοί ήταν το 'NARPAS SWORD'."
        ],
        "source": "https://en.wikipedia.org/wiki/Metroid_(video_game)",
        "tags": ["gaming", "metroid", "nintendo", "nes", "cheats"]
    },
    {
        "id": "gaming_hard_228",
        "text": "Ποιοι υπερυπολογιστές σταθμών εργασίας της Silicon Graphics χρησιμοποιήθηκαν από την Rare για την προσχεδίαση των 3D γραφικών του 'Donkey Kong Country' (1994);",
        "correct": "SGI Challenge και Indigo",
        "distractors": ["Cray-1 Supercomputers", "Sun Microsystems Ultra", "IBM Deep Blue"],
        "explanation": "Οι αδελφοί Tim και Chris Stamper επένδυσαν τεράστια ποσά σε σταθμούς SGI, δημιουργώντας φωτορεαλιστικά τρισδιάστατα μοντέλα τα οποία στη συνέχεια συμπίεσαν σε 2D sprites για το 16-bit SNES.",
        "funFacts": [
            "Όταν στελέχη της Nintendo είδαν για πρώτη φορά τα γραφικά, υπέθεσαν ότι έτρεχαν σε κάποια μυστική μελλοντική κονσόλα 64-bit και όχι στο Super Nintendo.",
            "Η επιτυχία του παιχνιδιού οδήγησε τη Nintendo να εξαγοράσει το 49% της Rare, καθιστώντας την κορυφαίο second-party developer."
        ],
        "source": "https://en.wikipedia.org/wiki/Donkey_Kong_Country",
        "tags": ["gaming", "donkey_kong", "rare", "snes", "sgi"]
    },
    {
        "id": "gaming_hard_229",
        "text": "Ποια ήταν η μοναδική απαίτηση υλικού που καθιστούσε υποχρεωτική την αγορά του 4MB Expansion Pak για την εκστρατεία μονού παίκτη του 'Perfect Dark' (2000);",
        "correct": "Χωρίς το Expansion Pak, ο παίκτης είχε πρόσβαση μόνο σε ένα περιορισμένο split-screen combat mode",
        "distractors": [
            "Το παιχνίδι δεν εκκινούσε καθόλου εμφανίζοντας μαύρη οθόνη",
            "Απενεργοποιούνταν εντελώς η δυνατότητα αποθήκευσης προόδου",
            "Τα γραφικά υποβαθμίζονταν αυτόματα σε ασπρόμαυρη ανάλυση"
        ],
        "explanation": "Το Perfect Dark αξιοποιούσε τα επιπλέον 4MB RAM για υψηλότερη ανάλυση, προηγμένο AI εχθρών, δυναμικούς φωτισμούς και εκτεταμένα voice-overs, καθιστώντας το 8MB σύνολο απαραίτητο για το 90% του περιεχομένου.",
        "funFacts": [
            "Το παιχνίδι περιλάμβανε καινοτόμα όπλα επιστημονικής φαντασίας, όπως το Laptop Gun που μπορούσε να τοποθετηθεί ως αυτόματο turret και το Farsight XR-20 που πυροβολούσε μέσα από τοίχους.",
            "Σχεδιαζόταν αρχικά μια λειτουργία 'Face-In' που θα επέτρεπε στους παίκτες να φωτογραφίζουν το πρόσωπό τους με το Game Boy Camera και να το βάζουν στο παιχνίδι, αλλά ακυρώθηκε για λόγους ασφαλείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Perfect_Dark_(video_game)",
        "tags": ["gaming", "perfect_dark", "rare", "n64", "hardware"]
    },
    {
        "id": "gaming_hard_230",
        "text": "Ως τι είδους παιχνίδι ξεκίνησε αρχικά η ανάπτυξη του 'Shenmue' στο Sega Saturn πριν μεταφερθεί στο Dreamcast;",
        "correct": "Ως RPG στο σύμπαν του Virtua Fighter με τίτλο 'Project Berkeley'",
        "distractors": [
            "Ως spin-off της σειράς Out Run με ανοιχτό κόσμο",
            "Ως παιχνίδι μάχης της σειράς Streets of Rage σε 3D",
            "Ως ιστορικό adventure για τη μεσαιωνική Ιαπωνία"
        ],
        "explanation": "Ο Yu Suzuki σχεδίασε το παιχνίδι αρχικά γύρω από τον Akira Yuki του Virtua Fighter, εξερευνώντας το παρελθόν και την εκπαίδευσή του στις πολεμικές τέχνες πριν δημιουργήσει τον πρωτότυπο χαρακτήρα Ryo Hazuki.",
        "funFacts": [
            "Ένα πλήρως λειτουργικό πρωτότυπο του Shenmue στο Sega Saturn αποκαλύφθηκε χρόνια αργότερα ως bonus βίντεο στο Shenmue II.",
            "Τα γραφικά του πρωτοτύπου στο Saturn ήταν εντυπωσιακά για την κονσόλα αλλά ξεπερνούσαν κατά πολύ τα τεχνικά της όρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Shenmue_(video_game)",
        "tags": ["gaming", "shenmue", "sega", "saturn", "yu_suzuki"]
    },
    {
        "id": "gaming_hard_231",
        "text": "Για ποιο λόγο το αριστουργηματικό RPG 'Panzer Dragoon Saga' (1998) του Sega Saturn δεν επανακυκλοφόρησε ποτέ σε σύγχρονες πλατφόρμες;",
        "correct": "Ο αυθεντικός πηγαίος κώδικας του παιχνιδιού χάθηκε οριστικά από τα αρχεία της Sega",
        "distractors": [
            "Λόγω ανεπίλυτων δικαιωμάτων πνευματικής ιδιοκτησίας με τη Moebius Productions",
            "Επειδή η μηχανή γραφικών βασιζόταν σε κατοχυρωμένες πατέντες της Lockheed Martin",
            "Λόγω νομικής διαμάχης με την οικογένεια του σκηνοθέτη"
        ],
        "explanation": "Ο σκηνοθέτης Yukio Futatsugi επιβεβαίωσε ότι ο πηγαίος κώδικας χάθηκε μετά τη διάλυση της Team Andromeda, καθιστώντας οποιοδήποτε port αδύνατο χωρίς αντίστροφη μηχανική από το μηδέν.",
        "funFacts": [
            "Το παιχνίδι κυκλοφόρησε σε εξαιρετικά περιορισμένα αντίτυπα στη Δύση (λιγότερα από 20.000 αντίτυπα στις ΗΠΑ), κάνοντάς το ένα από τα πιο ακριβά συλλεκτικά παιχνίδια στον κόσμο.",
            "Απλωνόταν σε 4 οπτικούς δίσκους CD-ROM και συνδύαζε turn-based τακτικές μάχες με ελεύθερη πτήση πάνω σε δράκο σε 360 μοίρες."
        ],
        "source": "https://en.wikipedia.org/wiki/Panzer_Dragoon_Saga",
        "tags": ["gaming", "sega", "saturn", "panzer_dragoon", "lost_media"]
    },
    {
        "id": "gaming_hard_232",
        "text": "Ποια ήταν η θεμελιώδης φιλοσοφία σχεδιασμού που εφάρμοσε ο Fumito Ueda κατά τη δημιουργία του 'Ico' (2001) στο PlayStation 2;",
        "correct": "Σχεδιασμός μέσω αφαίρεσης (Design by Subtraction)",
        "distractors": [
            "Πλήρης εμβύθιση μέσω φωτορεαλισμού",
            "Πολυεπίπεδη αφήγηση μέσω διακλαδούμενων μονοπατιών",
            "Μηχανική πρόκληση μέσω αυστηρών στατιστικών RPG"
        ],
        "explanation": "Ο Ueda αφαίρεσε οποιοδήποτε στοιχείο αποσπούσε την προσοχή από τον συναισθηματικό δεσμό του Ico και της Yorda: δεν υπάρχουν ενδείξεις υγείας στην οθόνη (HUD), μίνι-χάρτες, μετρητές ή περίπλοκα συστήματα inventory.",
        "funFacts": [
            "Ο παίκτης καθοδηγεί τη Yorda κρατώντας πατημένο το κουμπί R1, κάνοντας τον Ico να την κρατά κυριολεκτικά από το χέρι.",
            "Το Ico ενέπνευσε βαθιά κορυφαίους δημιουργούς της βιομηχανίας, όπως τον Hidetaka Miyazaki (που δήλωσε ότι αποφάσισε να ασχοληθεί με τα video games αφού έπαιξε το Ico) και τον Eiji Aonuma."
        ],
        "source": "https://en.wikipedia.org/wiki/Ico",
        "tags": ["gaming", "ico", "fumito_ueda", "team_ico", "design"]
    },
    {
        "id": "gaming_hard_233",
        "text": "Πώς προγραμμάτισε η Team Ico την τεχνητή νοημοσύνη του αλόγου Agro στο 'Shadow of the Colossus' (2005) για να ενισχύσει τον ρεαλισμό;",
        "correct": "Το άλογο δεν κατευθυνόταν σαν αυτοκίνητο αλλά απέφευγε αυτόνομα φυσικά εμπόδια και δέντρα",
        "distractors": [
            "Το άλογο απαιτούσε τακτικό τάισμα και περιποίηση για να υπακούει",
            "Η ταχύτητά του εξαρτιόταν από το βάρος των όπλων του Wander",
            "Αντιδρούσε αποκλειστικά σε φωνητικές εντολές μέσω του μικροφώνου USB"
        ],
        "explanation": "Ο παίκτης δεν 'οδηγούσε' το άλογο, αλλά παρότρυνε τον Wander να κλωτσήσει τα πλευρά του, ενώ το ίδιο το άλογο είχε δική του αυτοσυντήρηση και απέφευγε γκρεμούς και βράχους αυτόνομα.",
        "funFacts": [
            "Στη δραματική σκηνή της κατάρρευσης της πέτρινης γέφυρας πριν τον 16ο Κολοσσό, το Agro πετάει τον Wander στην απέναντι πλευρά θυσιάζοντας τον εαυτό του και πέφτοντας στον γκρεμό.",
            "Η ιαπωνική ράτσα του αλόγου θεωρείται ότι βασίστηκε σε άλογο τύπου Kiso."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_of_the_Colossus",
        "tags": ["gaming", "shadow_of_the_colossus", "team_ico", "ai", "agro"]
    },
    {
        "id": "gaming_hard_234",
        "text": "Ποια ήταν η πραγματική χρήση του αρχικού δώρου 'Pendant' (Μενταγιόν) στο πρώτο 'Dark Souls', σύμφωνα με δήλωση του ίδιου του Hidetaka Miyazaki;",
        "correct": "Δεν είχε απολύτως καμία λειτουργία εντός παιχνιδιού",
        "distractors": [
            "Ξεκλείδωνε έναν μυστικό διάλογο με τη Gwynevere",
            "Αύξανε ανεπαίσθητα την πιθανότητα drop σπάνιων όπλων",
            "Προστάτευε από την πρώτη επίθεση κατάρας των Basilisk"
        ],
        "explanation": "Ο Miyazaki είχε πει περιπαικτικά σε μια συνέντευξη ότι εκείνος θα επέλεγε το Pendant, οδηγώντας χιλιάδες παίκτες σε μάταιες έρευνες μηνών πριν παραδεχτεί τελικά ότι επρόκειτο για φάρσα.",
        "funFacts": [
            "Η περιγραφή του αντικειμένου ανέφερε απλώς: 'Ένα απλό μενταγιόν χωρίς καμία δύναμη... αλλά οι ευχάριστες αναμνήσεις βοηθούν τον κουρασμένο ταξιδιώτη'.",
            "Η FromSoftware επανέλαβε παρόμοια αινιγματικά αντικείμενα χωρίς χρήση σε μετέπειτα τίτλους της."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "hidetaka_miyazaki", "lore", "fromsoftware"]
    },
    {
        "id": "gaming_hard_235",
        "text": "Ποια νουβέλα κοσμικού τρόμου του H.P. Lovecraft αποτέλεσε την κύρια έμπνευση για την περιοχή Fishing Hamlet στο DLC 'The Old Hunters' του 'Bloodborne';",
        "correct": "The Shadow over Innsmouth (Η Σκιά πάνω από το Ίνσμουθ)",
        "distractors": ["At the Mountains of Madness", "The Dunwich Horror", "The Call of Cthulhu"],
        "explanation": "Το Fishing Hamlet κατοικείται από παραμορφωμένους ιχθυόμορφους ψαράδες που λατρεύουν το πτώμα του Μεγάλου Kos, αποτίοντας άμεσο φόρο τιμής στο Innsmouth του Lovecraft.",
        "funFacts": [
            "Το τελικό αφεντικό Orphan of Kos γεννιέται μέσα από τη μήτρα του νεκρού πλάσματος Kos και κλαίει κοιτάζοντας το φεγγάρι πριν επιτεθεί.",
            "Το Bloodborne ξεκινά φαινομενικά ως ιστορία γοτθικού λυκανθρωπισμού και σταδιακά μετατρέπεται σε καθαρό Lovecraftian κοσμικό τρόμο καθώς ανεβαίνει το στατιστικό Insight του παίκτη."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodborne",
        "tags": ["gaming", "bloodborne", "lovecraft", "fromsoftware", "the_old_hunters"]
    },
    {
        "id": "gaming_hard_236",
        "text": "Στο 'Sekiro: Shadows Die Twice', ποια θανατηφόρα επιδημία εξαπλώνεται στους φιλικούς NPCs κάθε φορά που ο Wolf πεθαίνει και ανασταίνεται επανειλημμένα;",
        "correct": "Dragonrot (Δρακοσήψη / Ryūkan)",
        "distractors": ["Scarlet Rot", "Abyssal Blight", "Ashina Fever"],
        "explanation": "Η ανάσταση του Wolf τροφοδοτείται από την ουράνια κληρονομιά του Kuro· όταν ο Wolf πεθαίνει πολλές φορές, αντλεί ζωτική ενέργεια από τους ανθρώπους γύρω του, προκαλώντας τους βήχα με μαύρο αίμα.",
        "funFacts": [
            "Καθώς εξαπλώνεται το Dragonrot, μειώνεται το ποσοστό της 'Αόρατης Βοήθειας' (Unseen Aid) που αποτρέπει την απώλεια χρημάτων και XP κατά τον θάνατο.",
            "Η γιατρός Emma αναπτύσσει μια θεραπεία χρησιμοποιώντας σταγόνες δακρύων του Δράκου (Dragon's Blood Droplet) στους βωμούς Sculptor's Idols."
        ],
        "source": "https://en.wikipedia.org/wiki/Sekiro:_Shadows_Die_Twice",
        "tags": ["gaming", "sekiro", "fromsoftware", "mechanics"]
    },
    {
        "id": "gaming_hard_237",
        "text": "Ποιο είναι το αρχικό σενάριο που πρότειναν ο Tetsuya Takahashi και η Kaori Tanaka το 1995 για το 'Final Fantasy VII' πριν απορριφθεί και εξελιχθεί στο 'Xenogears';",
        "correct": "Μια σκοτεινή, ψυχαναλυτική ιστορία με γιγάντια mecha που κρίθηκε ακατάλληλη για τη βασική σειρά FF",
        "distractors": [
            "Ένα σενάριο με ταξίδια στον χρόνο που έγινε τελικά το Chrono Cross",
            "Μια ιστορία με πειρατές και αερόπλοια που έγινε το Skies of Arcadia",
            "Ένα μεσαιωνικό στρατηγικό δράμα που έγινε το Final Fantasy Tactics"
        ],
        "explanation": "Η διοίκηση της Square έκρινε ότι το σενάριο του Takahashi ήταν υπερβολικά περίπλοκο, σκοτεινό και φιλοσοφικό για Final Fantasy, αλλά του έδωσε το πράσινο φως να το αναπτύξει ως αυτόνομο νέο τίτλο (Project Noah / Xenogears).",
        "funFacts": [
            "Το δεύτερο CD του Xenogears αναγκάστηκε να παρουσιάσει μεγάλο μέρος της πλοκής με τη μορφή μονολόγων μπροστά από στατικές εικόνες λόγω έλλειψης χρόνου και προϋπολογισμού.",
            "Στο τέλος του παιχνιδιού εμφανίζεται η επιγραφή 'Xenogears: Episode V', καθώς το σενάριο είχε σχεδιαστεί ως το πέμπτο μέρος ενός έπους έξι επεισοδίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Xenogears",
        "tags": ["gaming", "xenogears", "square", "final_fantasy", "history"]
    },
    {
        "id": "gaming_hard_238",
        "text": "Ποιο ιστορικό αγγλικό εμφύλιο πόλεμο χρησιμοποίησε ως κεντρική έμπνευση ο Yasumi Matsuno για τον 'Πόλεμο των Λεόντων' στο 'Final Fantasy Tactics' (1997);",
        "correct": "Τον Πόλεμο των Ρόδων (Wars of the Roses)",
        "distractors": ["Τον Εκατονταετή Πόλεμο", "Τον Αγγλικό Εμφύλιο Πόλεμο του Κρόμγουελ", "Τον Πόλεμο των Βαρόνων"],
        "explanation": "Η σύγκρουση μεταξύ του Μαύρου Λέοντα (Prince Goltanna) και του Λευκού Λέοντα (Prince Larg) για τον θρόνο του Ivalice αντικατοπτρίζει τη διαμάχη μεταξύ των οίκων του Lancaster και του York.",
        "funFacts": [
            "Ο πρωταγωνιστής Ramza Beoulve διαγράφηκε σκόπιμα από τα επίσημα ιστορικά αρχεία της εκκλησίας ως αιρετικός, παρά το γεγονός ότι έσωσε τον κόσμο από τους Lucavi.",
            "Ο Matsuno δημιούργησε αργότερα τα Vagrant Story και Final Fantasy XII, όλα τοποθετημένα στον κοινό κόσμο του Ivalice."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_Tactics",
        "tags": ["gaming", "final_fantasy_tactics", "square", "yasumi_matsuno", "history"]
    },
    {
        "id": "gaming_hard_239",
        "text": "Στο αριστουργηματικό 'Vagrant Story' (2000) του Yasumi Matsuno στο PS1, ποιο είναι το επάγγελμα και ο τίτλος του πρωταγωνιστή Ashley Riot;",
        "correct": "Riskbreaker των Valendia Knights of the Peace (VKP)",
        "distractors": ["Inquisitor", "Holy Blade", "Bounty Agent"],
        "explanation": "Οι Riskbreakers είναι επίλεκτοι πράκτορες που αποστέλλονται μόνοι τους σε αποστολές υψηλού κινδύνου. Ο Ashley Riot διεισδύει στην ερειπωμένη μεσαιωνική πόλη Leá Monde.",
        "funFacts": [
            "Το παιχνίδι είναι το μοναδικό παιχνίδι του αρχικού PlayStation που απέσπασε την απόλυτη τέλεια βαθμολογία 40/40 από το ιαπωνικό περιοδικό Famitsu.",
            "Το σύστημα μάχης βασιζόταν στη στόχευση συγκεκριμένων μελών του σώματος των εχθρών (κεφάλι, χέρια, πόδια) και στη διαχείριση του μετρητή Risk."
        ],
        "source": "https://en.wikipedia.org/wiki/Vagrant_Story",
        "tags": ["gaming", "vagrant_story", "square", "playstation", "matsuno"]
    },
    {
        "id": "gaming_hard_240",
        "text": "Στο 'Suikoden II' (1998) της Konami, ποιος σαδιστής πρίγκιπας του Highland απαιτεί τρεις διαδοχικές μάχες με 18 συνολικά μαχητές για να εξοντωθεί;",
        "correct": "Luca Blight",
        "distractors": ["Jowy Atreides", "Neclord", "Culgan"],
        "explanation": "Ο Luca Blight επιβιώνει από νυχτερινή ενέδρα με χιλιάδες βέλη, νικάει διαδοχικά τρεις ξεχωριστές ομάδες έξι παικτών του πρωταγωνιστή και τελικά πέφτει μόνο σε μονομαχία ένας-προς-έναν.",
        "funFacts": [
            "Η διάσημη ατάκα του Luca Blight πριν πεθάνει είναι: 'It took hundreds of you to kill me, but look at you! You're trembling!'.",
            "Το Suikoden βασίζεται στο κλασικό κινεζικό μυθιστόρημα 'Water Margin' (Outlaws of the Marsh) και περιλαμβάνει 108 στρατολογήσιμους χαρακτήρες (108 Stars of Destiny)."
        ],
        "source": "https://en.wikipedia.org/wiki/Suikoden_II",
        "tags": ["gaming", "suikoden", "konami", "playstation", "jrpg"]
    },
    {
        "id": "gaming_hard_241",
        "text": "Στο 'Valkyrie Profile' (1999) της tri-Ace, ποια Βαλκυρία επιλέγει τις ψυχές πεσόντων πολεμιστών (Einherjar) στο Midgard για να τις στείλει στον πόλεμο του Ragnarok;",
        "correct": "Lenneth Valkyrie",
        "distractors": ["Silmeria", "Hrist", "Freya"],
        "explanation": "Η Lenneth ακούει τις τελευταίες σκέψεις θνητών που πεθαίνουν τραγικά και τους στρατολογεί, εκπαιδεύοντάς τους πριν τους στείλει στον παράδεισο της Valhalla υπό τις εντολές του Odin.",
        "funFacts": [
            "Το παιχνίδι έχει αυστηρό σύστημα κεφαλαίων και περιόδων (Periods) που μετρούν αντίστροφα προς το αναπόφευκτο τέλος του κόσμου.",
            "Για να ξεκλειδώσει ο παίκτης το πραγματικό 'Ending A', απαιτείται η ακριβής διαχείριση του κρυφού στατιστικού 'Seal Value' της Lenneth."
        ],
        "source": "https://en.wikipedia.org/wiki/Valkyrie_Profile",
        "tags": ["gaming", "valkyrie_profile", "tri_ace", "enix", "rpg"]
    },
    {
        "id": "gaming_hard_242",
        "text": "Ποιος διάσημος guest χαρακτήρας άλλης σειράς προστέθηκε στην αναβαθμισμένη έκδοση 'Shin Megami Tensei III: Nocturne Maniax' (2004) στο PS2;",
        "correct": "Dante (από το Devil May Cry)",
        "distractors": ["Raidou Kuzunoha", "Alucard", "Solid Snake"],
        "explanation": "Η Atlus συνεργάστηκε με την Capcom και πρόσθεσε τον Dante ως μισθοφόρο κυνηγό δαιμόνων που καταδιώκει και αργότερα μπορεί να συμμαχήσει με τον Demi-fiend.",
        "funFacts": [
            "Το λογότυπο του παιχνιδιού με το αυτοκόλλητο 'Featuring Dante from the Devil May Cry series' έγινε ένα από τα διασημότερα gaming memes όλων των εποχών.",
            "Στο remaster του 2020, οι παίκτες μπορούσαν να επιλέξουν ανάμεσα στον Dante και τον Raidou Kuzunoha της Atlus."
        ],
        "source": "https://en.wikipedia.org/wiki/Shin_Megami_Tensei_III:_Nocturne",
        "tags": ["gaming", "shin_megami_tensei", "atlus", "dante", "playstation2"]
    },
    {
        "id": "gaming_hard_243",
        "text": "Ποιο καινοτόμο σύστημα διάδοσης φημών εφάρμοσε η Atlus στο 'Persona 2: Innocent Sin' (1999) στο PlayStation;",
        "correct": "Οι φήμες που διαδίδουν οι μαθητές στην πόλη μετατρέπονται σε πραγματικά γεγονότα μέσω του Rumor Agency",
        "distractors": [
            "Οι φήμες αλλάζουν αυτόματα τις τιμές στα καταστήματα της πόλης",
            "Οι παίκτες μπορούν να εκβιάζουν αστυνομικούς με πλαστές ειδήσεις",
            "Οι φήμες αυξάνουν τα στατιστικά των Personas ανάλογα με τον καιρό"
        ],
        "explanation": "Στη Sumaru City, όποια φήμη συζητιέται αρκετά γίνεται πραγματικότητα λόγω της επιρροής του Nyarlathotep, επιτρέποντας στους ήρωες να μετατρέπουν π.χ. ένα κατάστημα ράφτη σε οπλοπωλείο.",
        "funFacts": [
            "Το Innocent Sin δεν κυκλοφόρησε αρχικά στη Βόρεια Αμερική το 1999 εν μέρει λόγω αμφιλεγόμενων θεμάτων, όπως η εμφάνιση του Αδόλφου Χίτλερ ως boss κρατώντας τη Λόγχη του Πεπρωμένου.",
            "Η άμεση συνέχειά του, το 'Persona 2: Eternal Punishment', κυκλοφόρησε κανονικά στις ΗΠΑ το 2000."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_2:_Innocent_Sin",
        "tags": ["gaming", "persona", "atlus", "playstation", "rumor_system"]
    },
    {
        "id": "gaming_hard_244",
        "text": "Ποιο μοναδικό σύστημα ρυθμικής μάχης εισήγαγε το καλτ RPG 'Mother 3' (2006) του Shigesato Itoi στο Game Boy Advance;",
        "correct": "Ο παίκτης πατάει το κουμπί επίθεσης στον ρυθμό του μουσικού θέματος μάχης για combos έως και 16 χτυπημάτων",
        "distractors": [
            "Ο παίκτης πρέπει να τραγουδάει στο μικρόφωνο του GBA",
            "Οι επιθέσεις καθορίζονται από το ύψος των νοτών του εχθρού",
            "Η μουσική επιταχύνει ή επιβραδύνει ανάλογα με το HP"
        ],
        "explanation": "Κάθε εχθρός στο Mother 3 έχει το δικό του soundtrack με ιδιαίτερο μέτρο (μερικά σε παράξενους ρυθμούς όπως 5/8 ή 7/8), και πατώντας στον παλμό της καρδιάς του εχθρού πετυχαίνεις 16-hit combos.",
        "funFacts": [
            "Παρά τις έντονες εκκλήσεις των οπαδών για σχεδόν δύο δεκαετίες, η Nintendo δεν κυκλοφόρησε ποτέ επίσημη αγγλική μετάφραση του Mother 3 στη Δύση.",
            "Μια ομάδα οπαδών υπό τον επαγγελματία μεταφραστή Clyde Mandelin (Tomato) κυκλοφόρησε μια θρυλική, άψογη ανεπίσημη μετάφραση (fan translation) το 2008."
        ],
        "source": "https://en.wikipedia.org/wiki/Mother_3",
        "tags": ["gaming", "mother_3", "nintendo", "gba", "shigesato_itoi"]
    },
    {
        "id": "gaming_hard_245",
        "text": "Ποιο παιδικό τραύμα του δημιουργού Shigesato Itoi ενέπνευσε τον τρομακτικό, ακατανόητο σχεδιασμό του τελικού αφεντικού Giygas στο 'EarthBound' (Mother 2);",
        "correct": "Η κατά λάθος παρακολούθηση μιας τραυματικής σκηνής σεξουαλικής βίας σε κινηματογραφική ταινία όταν ήταν παιδί",
        "distractors": [
            "Ένας εφιάλτης με ένα παραμορφωμένο πρόσωπο σε σπασμένη τηλεόραση",
            "Μια εμπειρία παρ' ολίγον πνιγμού σε ποτάμι",
            "Ο θάνατος του αγαπημένου του σκύλου από ασθένεια"
        ],
        "explanation": "Ο Itoi μπήκε κατά λάθος σε λάθος αίθουσα σινεμά ως παιδί και είδε μια σκηνή φόνου από την ιαπωνική ταινία 'The Military Policeman and the Dismembered Beauty', ένα σοκ που μετουσίωσε στην αλλόκοτη φιγούρα του Giygas.",
        "funFacts": [
            "Οι ατάκες του Giygas στη μάχη ('It hurts, Ness...', 'I'm so sad...') αποδίδουν την απόλυτη απώλεια της λογικής του από την υπερβολική δύναμη.",
            "Ο Giygas μπορεί να νικηθεί μόνο αν η Paula προσευχηθεί επανειλημμένα, καλώντας τη βοήθεια και την αγάπη όλων των ανθρώπων του κόσμου και του ίδιου του παίκτη."
        ],
        "source": "https://en.wikipedia.org/wiki/Giygas",
        "tags": ["gaming", "earthbound", "nintendo", "snes", "giygas"]
    },
    {
        "id": "gaming_hard_246",
        "text": "Ποια πρωτοποριακή μηχανική πολικότητας (Polarity) καθιέρωσε το θρυλικό shoot 'em up 'Ikaruga' (2001) της Treasure;",
        "correct": "Το σκάφος αλλάζει χρώμα ανάμεσα σε μαύρο και άσπρο απορροφώντας τα βλήματα του ίδιου χρώματος",
        "distractors": [
            "Το σκάφος μαγνητίζει τα εχθρικά συντρίμμια για να φτιάξει ασπίδα",
            "Η βαρύτητα αλλάζει κατεύθυνση ανάμεσα σε πάνω και κάτω",
            "Οι σφαίρες παγώνουν στον χρόνο αν περάσουν μέσα από ενεργειακές πύλες"
        ],
        "explanation": "Απορροφώντας σφαίρες του ίδιου χρώματος, ο παίκτης γεμίζει το ειδικό ενεργειακό λέιζερ Homing Lasers, ενώ πυροβολώντας εχθρούς αντίθετου χρώματος προκαλεί διπλάσια ζημιά.",
        "funFacts": [
            "Το παιχνίδι λειτουργεί ουσιαστικά ως puzzle game υψηλών ταχυτήτων, όπου η καταστροφή τριών εχθρών του ίδιου χρώματος στη σειρά δίνει chain combos.",
            "Το Ikaruga αναπτύχθηκε από μια ομάδα μόλις τριών βασικών δημιουργών στην εταιρεία Treasure."
        ],
        "source": "https://en.wikipedia.org/wiki/Ikaruga",
        "tags": ["gaming", "ikaruga", "treasure", "shmup", "dreamcast"]
    },
    {
        "id": "gaming_hard_247",
        "text": "Στο αριστούργημα της Treasure 'Radiant Silvergun' (1998) στο Sega Saturn, πόσα διαφορετικά όπλα έχει στη διάθεσή του ο παίκτης εξαρχής χωρίς pickups;",
        "correct": "7 όπλα",
        "distractors": ["3 όπλα", "5 όπλα", "9 όπλα"],
        "explanation": "Ο παίκτης έχει άμεση πρόσβαση σε επτά όπλα συνδυάζοντας τα τρία βασικά κουμπιά (A, B, C και τους συνδυασμούς τους AB, BC, AC, ABC για το Radiant Sword).",
        "funFacts": [
            "Τα όπλα αναβαθμίζονται σε επίπεδα (levels) καθώς χρησιμοποιούνται, ενσωματώνοντας στοιχεία RPG μέσα σε κλασικό arcade shmup.",
            "Το παιχνίδι ακολουθεί μη γραμμική χρονολογική αφήγηση, ξεκινώντας από το Κεφάλαιο 3, πηγαίνοντας πίσω στα Κεφάλαια 1 και 2 και μετά στα 4, 5 και 6."
        ],
        "source": "https://en.wikipedia.org/wiki/Radiant_Silvergun",
        "tags": ["gaming", "radiant_silvergun", "treasure", "saturn", "shmup"]
    },
    {
        "id": "gaming_hard_248",
        "text": "Ποια είναι η ακριβής διάταξη των έξι αναβαθμίσεων στη γραμμή ισχύος (Power Meter) του ιστορικού shoot 'em up 'Gradius' (1985) της Konami;",
        "correct": "Speed Up, Missile, Double, Laser, Option, Shield",
        "distractors": [
            "Speed Up, Laser, Double, Missile, Shield, Option",
            "Missile, Speed Up, Shield, Double, Laser, Option",
            "Option, Speed Up, Missile, Double, Laser, Shield"
        ],
        "explanation": "Κάθε πορτοκαλί κάψουλα μετακινεί τον δείκτη κατά μία θέση προς τα δεξιά, επιτρέποντας στον παίκτη να επιλέξει στρατηγικά πότε θα ενεργοποιήσει την αναβάθμιση.",
        "funFacts": [
            "Τα 'Options' είναι φωτεινές πορτοκαλί ενεργειακές σφαίρες που ακολουθούν πιστά τις κινήσεις του Vic Viper και διπλασιάζουν τα πυρά του.",
            "Ο προγραμματιστής Kazuhisa Hashimoto επινόησε τον Konami Code κατά τη μεταφορά του Gradius στο Famicom επειδή δυσκολευόταν να δοκιμάσει το παιχνίδι."
        ],
        "source": "https://en.wikipedia.org/wiki/Gradius_(video_game)",
        "tags": ["gaming", "gradius", "konami", "shmup", "nes"]
    },
    {
        "id": "gaming_hard_249",
        "text": "Ποιο καινοτόμο αποσπώμενο αμυντικό εξάρτημα εισήγαγε το 'R-Type' (1987) της Irem, το οποίο μπορεί να κουμπώσει εμπρός ή πίσω από το σκάφος R-9;",
        "correct": "The Force (Η Δύναμη)",
        "distractors": ["The Option", "The Bit", "The Pod"],
        "explanation": "Το Force είναι ένας άτρωτος ενεργειακός πορτοκαλί οργανισμός που μπορεί να απορροφά εχθρικές σφαίρες, να εκτοξεύεται ως αυτόνομο πυροβόλο ή να κουμπώνει στο σκάφος.",
        "funFacts": [
            "Κρατώντας πατημένο το κουμπί βολής, το R-9 φορτίζει το καταστροφικό 'Wave Cannon' που απελευθερώνει μια τεράστια ακτίνα πλάσματος.",
            "Ο σχεδιασμός των εχθρών Bydo επηρεάστηκε άμεσα από τα βιομηχανικά έργα του H.R. Giger για την ταινία Alien."
        ],
        "source": "https://en.wikipedia.org/wiki/R-Type",
        "tags": ["gaming", "r_type", "irem", "shmup", "retro"]
    },
    {
        "id": "gaming_hard_250",
        "text": "Ποιο εντυπωσιακό χαρακτηριστικό διέθετε η αυθεντική arcade καμπίνα του 'Darius' (1986) της Taito για να προβάλλει την πανοραμική εικόνα του παιχνιδιού;",
        "correct": "Τρεις συνδεδεμένες οθόνες CRT σε σειρά με καθρέφτες χωρίς ορατά κενά",
        "distractors": [
            "Μια κυρτή οθόνη προβολής 180 μοιρών",
            "Δύο κάθετες οθόνες τοποθετημένες υπό γωνία 90 μοιρών",
            "Έναν πρωτότυπο ολογραφικό περιστρεφόμενο κύλινδρο"
        ],
        "explanation": "Η Taito χρησιμοποίησε ένα έξυπνο οπτικό σύστημα με τρεις οθόνες και ημιδιαπερατούς καθρέφτες που εξάλειφαν τα πλαίσια, δημιουργώντας μια υπερευρεία αναλογία διαστάσεων 12:3.",
        "funFacts": [
            "Το κάθισμα της καμπίνας διέθετε ενσωματωμένο υπογούφερ δόνησης 'Bodysonic' που έκανε τον παίκτη να νιώθει στο σώμα του τις εκρήξεις.",
            "Όλα τα γιγάντια αφεντικά του Darius είναι ρομποτικά θαλάσσια πλάσματα, με πιο διάσημο τον μηχανικό κοιλάκανθο 'King Fossil'."
        ],
        "source": "https://en.wikipedia.org/wiki/Darius_(video_game)",
        "tags": ["gaming", "darius", "taito", "arcade", "retro"]
    },
    {
        "id": "gaming_hard_251",
        "text": "Ποιο ήταν το κωδικό όνομα του πρωτοποριακού συνεπεξεργαστή της Nintendo (Super FX) κατά την αρχική του ανάπτυξη από την Argonaut Software;",
        "correct": "MARS (Mathematical Applications Racing System)",
        "distractors": ["JUPITER", "SATURN", "NEPTUNE"],
        "explanation": "Το πρότζεκτ ονομαζόταν αρχικά MARS και σχεδιάστηκε από τους Ben Cheese, Rob Macaulay και James Hakewill για λογαριασμό της εταιρείας του Jez San.",
        "funFacts": [
            "Το πρώτο παιχνίδι που χρησιμοποίησε το τσιπ ήταν το Star Fox (1993), ακολουθούμενο από τα Stunt Race FX και Yoshi's Island (Super FX 2).",
            "Η επιτυχία του τσιπ ήταν τόσο μεγάλη ώστε ο Jez San ίδρυσε την εταιρεία ARC International για την αδειοδότηση παρόμοιων επεξεργαστών RISC."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_FX",
        "tags": ["gaming", "nintendo", "hardware", "super_fx", "argonaut"]
    },
    {
        "id": "gaming_hard_252",
        "text": "Ποιο ήταν το πρώτο εμπορικό βιντεοπαιχνίδι arcade με διανυσματικά γραφικά (vector graphics) που κυκλοφόρησε από την Cinematronics το 1977;",
        "correct": "Space Wars",
        "distractors": ["Asteroids", "Lunar Lander", "Battlezone"],
        "explanation": "Το Space Wars αναπτύχθηκε από τον Larry Rosenthal και βασίστηκε στο ιστορικό Spacewar! (1962) του MIT, χρησιμοποιώντας το σύστημα διανυσματικών γραφικών Vectorbeam.",
        "funFacts": [
            "Ο Rosenthal κατασκεύασε τον δικό του επεξεργαστή TTL επειδή οι μικροεπεξεργαστές της εποχής ήταν πολύ αργοί για να σχεδιάσουν διανύσματα σε πραγματικό χρόνο.",
            "Τα διανυσματικά γραφικά δεν χρησιμοποιούσαν pixels, αλλά σχεδίαζαν φωτεινές γραμμές απευθείας στην οθόνη μέσω της δέσμης ηλεκτρονίων του καθοδικού σωλήνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Space_Wars",
        "tags": ["gaming", "space_wars", "arcade", "vector", "retro"]
    },
    {
        "id": "gaming_hard_253",
        "text": "Ποια πρωτοποριακή τεχνολογία αποθήκευσης οπτικών δίσκων χρησιμοποίησε το arcade παιχνίδι 'Dragon's Lair' (1983) του Don Bluth;",
        "correct": "LaserDisc (Λέιζερντισκ)",
        "distractors": ["CD-ROM", "VHD", "SelectaVision CED"],
        "explanation": "Το LaserDisc επέτρεπε την άμεση ανάγνωση αναλογικού βίντεο κινουμένων σχεδίων υψηλής ποιότητας κινηματογράφου, απαιτώντας από τον παίκτη να πατήσει το σωστό κουμπί την κατάλληλη στιγμή.",
        "funFacts": [
            "Ο σχεδιαστής και βετεράνος animator της Disney Don Bluth δημιούργησε όλα τα animations στο χέρι.",
            "Οι συσκευές ανάγνωσης LaserDisc στις καμπίνες χαλούσαν συχνά λόγω της συνεχούς καταπόνησης της κεφαλής λέιζερ από τα απότομα άλματα σκηνών."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon%27s_Lair_(1983_video_game)",
        "tags": ["gaming", "dragons_lair", "don_bluth", "laserdisc", "arcade"]
    },
    {
        "id": "gaming_hard_254",
        "text": "Στο πρωτοποριακό RPG 'Ultima IV: Quest of the Avatar' (1985) του Richard Garriott, ποιος ήταν ο τελικός στόχος του παίκτη αντί για την εξόντωση ενός κακού;",
        "correct": "Να γίνει το ηθικό πρότυπο κατακτώντας τις Οκτώ Αρετές (Eight Virtues)",
        "distractors": [
            "Να κατακτήσει και να ενώσει τα τέσσερα βασίλεια της Britannia",
            "Να ανακαλύψει το χαμένο Δισκοπότηρο της σοφίας",
            "Να αποκτήσει αμύθητα πλούτη και να χτίσει τον δικό του ναό"
        ],
        "explanation": "Ο Garriott απογοητεύτηκε από επιστολές γονέων για τη βία στα παιχνίδια και σχεδίασε το Ultima IV όπου ο ήρωας έπρεπε να τελειοποιηθεί στην Ειλικρίνεια, τη Συμπόνια, τη Γενναιότητα, τη Δικαιοσύνη, τη Θυσία, την Τιμή, την Πνευματικότητα και την Ταπεινότητα.",
        "funFacts": [
            "Το παιχνίδι ξεκινούσε με μια τσιγγάνα που έκανε ερωτήσεις ηθικών διλημμάτων με κάρτες ταρώ για να καθορίσει την αρχική κλάση του χαρακτήρα.",
            "Αν ο παίκτης έκλεβε ή σκότωνε αθώους, έχανε πόντους αρετής και δεν μπορούσε να γίνει ο 'Avatar'."
        ],
        "source": "https://en.wikipedia.org/wiki/Ultima_IV:_Quest_of_the_Avatar",
        "tags": ["gaming", "ultima", "richard_garriott", "rpg", "retro"]
    },
    {
        "id": "gaming_hard_255",
        "text": "Ποιο ήταν το πρώτο βιντεοπαιχνίδι στην ιστορία που περιλάμβανε επίσημα πιστωμένο το όνομα του δημιουργού του ως κρυφό 'Easter Egg';",
        "correct": "Adventure (1979) στο Atari 2600 από τον Warren Robinett",
        "distractors": ["Colossal Cave Adventure", "Pong", "Haunted House"],
        "explanation": "Επειδή η Atari αρνούνταν να αναγράφει τα ονόματα των προγραμματιστών στα κουτιά για να μην τους κλέψουν οι ανταγωνιστές, ο Robinett έκρυψε ένα μυστικό δωμάτιο με την επιγραφή 'Created by Warren Robinett'.",
        "funFacts": [
            "Για να μπει στο μυστικό δωμάτιο, ο παίκτης έπρεπε να βρει μια αόρατη κουκκίδα 1-pixel (The Gray Dot) και να τη μεταφέρει μέσα από έναν τοίχο.",
            "Όταν η Atari το ανακάλυψε, το κόστος για την επανακατασκευή των ROMs ήταν απαγορευτικό, οπότε ο υπεύθυνος πρότεινε να το διαφημίσουν ως 'Easter Egg' ενθαρρύνοντας τους παίκτες να το βρουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Adventure_(1979_video_game)",
        "tags": ["gaming", "adventure", "atari", "warren_robinett", "easter_egg"]
    },
    {
        "id": "gaming_hard_256",
        "text": "Ποια είναι η επίσημη ονομασία του εικονικού κίτρινου τέρατος που κυνηγάει τον παίκτη στον λαβύρινθο του 'Adventure' (1979) στο Atari 2600 και μοιάζει κωμικά με πάπια;",
        "correct": "Yorgle (ο κίτρινος δράκος)",
        "distractors": ["Grundle", "Rhindle", "Duckfoot"],
        "explanation": "Λόγω των ακραίων περιορισμών ανάλυσης του Atari 2600, οι τρεις δράκοι (Yorgle, Grundle, Rhindle) σχεδιάστηκαν με μεγάλο ράμφος και μοιάζουν με γιγάντιες πάπιες.",
        "funFacts": [
            "Ο Yorgle φοβάται το χρυσό κλειδί και τρέχει μακριά του όταν το κρατάει ο παίκτης.",
            "Το Adventure ήταν το πρώτο παιχνίδι δράσης-περιπέτειας που εισήγαγε τη χρήση αντικειμένων που κουβαλάει ο ήρωας σε πραγματικό χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Adventure_(1979_video_game)",
        "tags": ["gaming", "adventure", "atari", "retro", "dragons"]
    },
    {
        "id": "gaming_hard_257",
        "text": "Ποιο ήταν το όνομα του πρωτοποριακού text adventure της Infocom (1980) που διαδραματιζόταν στο Great Underground Empire;",
        "correct": "Zork: The Great Underground Empire",
        "distractors": ["Colossal Cave", "The Lurking Horror", "Enchanter"],
        "explanation": "Το Zork δημιουργήθηκε από φοιτητές του MIT (Marc Blank, Dave Lebling, Tim Anderson, Bruce Daniels) και έγινε διάσημο για τον εξαιρετικά ευφυή αναλυτή κειμένου (parser) που κατανοούσε σύνθετες αγγλικές προτάσεις.",
        "funFacts": [
            "Η πιο διάσημη προειδοποίηση του παιχνιδιού είναι: 'It is pitch black. You are likely to be eaten by a grue.'.",
            "Η Infocom χρησιμοποιούσε μια εικονική μηχανή (Z-Machine) που επέτρεπε στα παιχνίδια της να τρέχουν σε δεκάδες διαφορετικούς οικιακούς υπολογιστές της δεκαετίας του '80."
        ],
        "source": "https://en.wikipedia.org/wiki/Zork",
        "tags": ["gaming", "zork", "infocom", "text_adventure", "retro"]
    },
    {
        "id": "gaming_hard_258",
        "text": "Ποιο εξαιρετικά επιδραστικό space trading και combat παιχνίδι ανέπτυξαν οι David Braben και Ian Bell το 1984 για το BBC Micro;",
        "correct": "Elite",
        "distractors": ["Wing Commander", "Star Citizen", "Privateer"],
        "explanation": "Το Elite χρησιμοποίησε διαδικαστική παραγωγή (procedural generation) μέσω συναρτήσεων Fibonacci για να χωρέσει οκτώ ολόκληρους γαλαξίες με 256 πλανήτες ο καθένας σε μόλις 22 kilobytes μνήμης!",
        "funFacts": [
            "Οι παίκτες ξεκινούσαν με το διαστημόπλοιο Cobra Mk III και 100 credits, προσπαθώντας να φτάσουν στον κορυφαίο βαθμό μάχης 'Elite'.",
            "Το σύστημα σύνδεσης με τους περιστρεφόμενους διαστημικούς σταθμούς (Coriolis stations) ήταν εμπνευσμένο από την ταινία '2001: A Space Odyssey'."
        ],
        "source": "https://en.wikipedia.org/wiki/Elite_(video_game)",
        "tags": ["gaming", "elite", "david_braben", "bbc_micro", "procedural"]
    },
    {
        "id": "gaming_hard_259",
        "text": "Ποιο είναι το όνομα του πρώτου dungeon crawl RPG με γραφικά πρώτου προσώπου σε πραγματικό χρόνο που κυκλοφόρησε η FTL Games το 1987 για το Atari ST;",
        "correct": "Dungeon Master",
        "distractors": ["Eye of the Beholder", "Wizardry", "The Bard's Tale"],
        "explanation": "Το Dungeon Master εγκατέλειψε τις παραδοσιακές turn-based μάχες των παλιών RPGs και εισήγαγε μάχη σε πραγματικό χρόνο, 3D ήχο και διαχείριση αποθέματος μέσω drag-and-drop με ποντίκι.",
        "funFacts": [
            "Το σύστημα μαγείας χρησιμοποιούσε συνδυασμούς τεσσάρων ρούνων (Ισχύς, Στοιχείο, Μορφή, Κατεύθυνση) για τη σύνθεση ξορκιών.",
            "Έγινε το παιχνίδι με τις περισσότερες πωλήσεις στην ιστορία της πλατφόρμας Atari ST."
        ],
        "source": "https://en.wikipedia.org/wiki/Dungeon_Master_(video_game)",
        "tags": ["gaming", "dungeon_master", "ftl_games", "atari_st", "rpg"]
    },
    {
        "id": "gaming_hard_260",
        "text": "Ποιο είναι το όνομα του πρώτου point-and-click adventure της Lucasfilm Games (1986) για το οποίο ο Ron Gilbert και ο Aric Wilmunder δημιούργησαν τη μηχανή SCUMM;",
        "correct": "Maniac Mansion",
        "distractors": ["The Secret of Monkey Island", "Zak McKracken", "Loom"],
        "explanation": "Το SCUMM σημαίνει 'Script Creation Utility for Maniac Mansion' και αποτέλεσε τη ραχοκοκαλιά όλων των θρυλικών adventures της LucasArts για την επόμενη δεκαετία.",
        "funFacts": [
            "Το Maniac Mansion περιλάμβανε ένα διαβόητο παζλ όπου ο παίκτης μπορούσε να βάλει το χάμστερ του Weird Ed μέσα στον φούρνο μικροκυμάτων.",
            "Ήταν από τα πρώτα παιχνίδια που επέτρεπαν στον παίκτη να επιλέξει μια ομάδα τριών χαρακτήρων από τους επτά διαθέσιμους, οδηγώντας σε πολλαπλές λύσεις και τέλη."
        ],
        "source": "https://en.wikipedia.org/wiki/Maniac_Mansion",
        "tags": ["gaming", "maniac_mansion", "lucasarts", "scumm", "ron_gilbert"]
    }
]

questions = []
for q in raw_questions:
    opts = [q["correct"]] + q["distractors"]
    random.shuffle(opts)
    c_idx = opts.index(q["correct"])
    questions.append({
        "id": q["id"],
        "categoryId": "gaming",
        "difficulty": 5,
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 1.")
    validate_and_append("gaming", "hard", 5, questions)

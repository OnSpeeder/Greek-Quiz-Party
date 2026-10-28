# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_361",
        "text": "Ποια ήταν η αρχική φοιτήτρια και οδηγός μοτοσικλέτας που προοριζόταν για συμπρωταγωνίστρια του Leon S. Kennedy στην ακυρωμένη έκδοση 'Resident Evil 1.5' πριν αντικατασταθεί από την Claire Redfield;",
        "correct": "Elza Walker",
        "distractors": ["Rebecca Chambers", "Cindy Lennox", "Rita Phillips"],
        "explanation": "Η Elza Walker ήταν φοιτήτρια στο πανεπιστήμιο της Raccoon City και λάτρης των αγώνων μοτοσικλέτας· όταν το αρχικό project του Resident Evil 2 ακυρώθηκε στο 65-80% της ανάπτυξής του, ανασχεδιάστηκε πλήρως και η Elza αντικαταστάθηκε από την Claire Redfield για να συνδεθεί η πλοκή με τον Chris.",
        "funFacts": [
            "Στο remake του 'Resident Evil 2' (2019), η Capcom συμπεριέλαβε τη στολή της Elza Walker ως εναλλακτική εμφάνιση DLC για την Claire.",
            "Το 'Resident Evil 1.5' είχε διαφορετική διαρρύθμιση του αστυνομικού τμήματος RPD, σχεδιασμένο ως ένα σύγχρονο γραφειοκρατικό κτίριο αντί για πρώην μουσείο τέχνης."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_2#Development",
        "tags": ["gaming", "resident_evil", "capcom", "elza_walker", "development"]
    },
    {
        "id": "gaming_hard_362",
        "text": "Στο αποκλειστικό για PlayStation 2 expansion 'Half-Life: Decay' (2001) από την Gearbox Software, ποιες δύο επιστήμονες ελέγχουν οι παίκτες σε λειτουργία split-screen συνεργασίας;",
        "correct": "Την Dr. Gina Cross και την Dr. Colette Green",
        "distractors": [
            "Την Dr. Judith Mossman και την Dr. Elena Reed",
            "Την Dr. Catherine Sommers και την Dr. Lisa Fox",
            "Την Dr. Alyx Vance και την Dr. Helen Cho"
        ],
        "explanation": "Οι Gina Cross και Colette Green φορούν στολές Hazard Suits (HEV) και βρίσκονται κάτω από τον θάλαμο δοκιμών του Black Mesa για να παραδώσουν το δείγμα GG-3883 και να βοηθήσουν τον Dr. Richard Keller να περιορίσει το Resonance Cascade.",
        "funFacts": [
            "Το Decay ήταν το μόνο επίσημο κεφάλαιο της σειράς Half-Life που σχεδιάστηκε εξαρχής αποκλειστικά για δύο παίκτες σε co-op.",
            "Η Dr. Gina Cross ήταν επίσης το μοντέλο του ολογράμματος εκπαίδευσης Hazard Course στο αρχικό Half-Life."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life:_Decay",
        "tags": ["gaming", "half_life", "gearbox", "playstation_2", "coop"]
    },
    {
        "id": "gaming_hard_363",
        "text": "Στο 'Quake II' (1997) της id Software, ποιο είναι το όνομα του κυβερνο-εξωγήινου είδους που πολεμά ο πεζοναύτης Bitterman στον αφιλόξενο πλανήτη Stroggos;",
        "correct": "Strogg",
        "distractors": ["Scrin", "Necris", "Covenant"],
        "explanation": "Οι Strogg είναι ένας στρατιωτικός πολιτισμός κυβερνο-μεταλλαγμένων που απάγει άλλες νοήμονες μορφές ζωής και τις ακρωτηριάζει βίαια (strogification) για να τις συγχωνεύσει με μηχανικά εξαρτήματα.",
        "funFacts": [
            "Το Quake II αρχικά αναπτυσσόταν ως εντελώς νέο franchise, αλλά η id Software αποφάσισε να κρατήσει το όνομα 'Quake' για εμπορικούς λόγους επειδή δεν μπορούσε να κατοχυρώσει εμπορικά τους άλλους υποψήφιους τίτλους.",
            "Το παιχνίδι χρησιμοποίησε τη μηχανή γραφικών id Tech 2, εισάγοντας έγχρωμο δυναμικό φωτισμό OpenGL και υποστήριξη επιτάχυνσης 3Dfx Voodoo."
        ],
        "source": "https://en.wikipedia.org/wiki/Quake_II",
        "tags": ["gaming", "quake_2", "id_software", "strogg", "id_tech"]
    },
    {
        "id": "gaming_hard_364",
        "text": "Στο cyberpunk tactical παιχνίδι 'Syndicate Wars' (1996) της Bullfrog, ποια μυστηριώδης θρησκευτική αίρεση μάχεται ενάντια στον κολοσσό EuroCorp για τον έλεγχο των μυαλών του πληθυσμού;",
        "correct": "Church of the New Epoch",
        "distractors": ["Children of the Cathedral", "The Brotherhood of Steel", "The Order of Dagon"],
        "explanation": "Η Church of the New Epoch εκμεταλλεύεται έναν καταστροφικό ιό που απενεργοποιεί το δίκτυο Utopia της EuroCorp, απελευθερώνοντας τους πολίτες από τον τεχνητό έλεγχο για να τους προσηλυτίσει στις δικές της τάξεις.",
        "funFacts": [
            "Οι παίκτες χρησιμοποιούσαν το διαβόητο gadget 'Persuade-o-Tron' για να ελέγξουν το μυαλό ανυποψίαστων περαστικών και να τους μετατρέψουν σε οπλισμένο στρατό κρέατος.",
            "Το παιχνίδι διέθετε πλήρως καταστρέψιμα cyberpunk κτίρια χάρη σε μια πρωτοποριακή 3D μηχανή που επέτρεπε την κατάρρευση ουρανοξυστών με πυρηνικά όπλα."
        ],
        "source": "https://en.wikipedia.org/wiki/Syndicate_Wars",
        "tags": ["gaming", "syndicate_wars", "bullfrog", "peter_molyneux", "cyberpunk"]
    },
    {
        "id": "gaming_hard_365",
        "text": "Στο 'Thief II: The Metal Age' (2000), ποιος φανατικός θρησκευτικός ηγέτης των Mechanists σχεδίασε το φονικό 'Rust Gas' με σκοπό να αφανίσει κάθε οργανική ζωή στην Πόλη;",
        "correct": "Father Karras",
        "distractors": ["Father Grigori", "High Priest Constantine", "Brother Murus"],
        "explanation": "Ο Father Karras, πρώην Hammerite, ίδρυσε το τάγμα των Mechanists και δημιούργησε μηχανικούς υπηρέτες που έκρυβαν δοχεία με αέριο σκουριάς (Rust Gas) για να μετατρέψουν όλους τους ανθρώπους σε σκόνη και να αφήσουν μόνο μέταλλο.",
        "funFacts": [
            "Ο ηθοποιός Stephen Russell δάνεισε τη φωνή του τόσο στον κεντρικό ήρωα Garrett όσο και στον παρανοϊκό κακό Father Karras, αλλά και στους φρουρούς και τα Mechanist ρομπότ.",
            "Το Thief II πρόσθεσε το gadget 'Scouting Orb', μια μηχανική κάμερα-μάτι που ο Garrett μπορούσε να πετάξει σε άλλα δωμάτια για να κατασκοπεύσει τους εχθρούς."
        ],
        "source": "https://en.wikipedia.org/wiki/Thief_II:_The_Metal_Age",
        "tags": ["gaming", "thief_2", "looking_glass", "stealth", "father_karras"]
    },
    {
        "id": "gaming_hard_366",
        "text": "Ποιο steampunk RPG του 2001 από την Troika Games (των Tim Cain και Leonard Boyarsky) ξεκινά με την κατάρριψη του πολυτελούς αερόπλοιου IFS Zephyr;",
        "correct": "Arcanum: Of Steamworks and Magick Obscura",
        "distractors": ["Septerra Core", "Anachronox", "Nox"],
        "explanation": "Το Arcanum εξερευνά τη σύγκρουση ανάμεσα στη μαγεία και τη βιομηχανική επανάσταση, όπου η χρήση τεχνολογίας διαταράσσει τους νόμους της μαγείας και αντίστροφα.",
        "funFacts": [
            "Εάν ο παίκτης είχε εξαιρετικά χαμηλό Intelligence (κάτω από 4), όλοι οι διάλογοι του παιχνιδιού άλλαζαν σε ασυνάρτητους ήχους ανθρώπου των σπηλαίων, με τους NPCs να αντιδρούν με οίκτο ή εκνευρισμό.",
            "Η Troika Games ιδρύθηκε από τρεις βασικούς δημιουργούς του αρχικού Fallout (Tim Cain, Leonard Boyarsky και Jason Anderson) μετά την αποχώρησή τους από την Interplay."
        ],
        "source": "https://en.wikipedia.org/wiki/Arcanum:_Of_Steamworks_and_Magick_Obscura",
        "tags": ["gaming", "arcanum", "troika_games", "tim_cain", "steampunk"]
    },
    {
        "id": "gaming_hard_367",
        "text": "Ποιο κλασικό επιτραπέζιο σενάριο D&D του Gary Gygax μετέφερε η Troika Games σε turn-based RPG για PC το 2003, χρησιμοποιώντας τους κανόνες D&D 3.5 Edition;",
        "correct": "The Temple of Elemental Evil",
        "distractors": ["The Keep on the Borderlands", "Tomb of Horrors", "Expedition to the Barrier Peaks"],
        "explanation": "Το The Temple of Elemental Evil διαδραματίζεται στον κόσμο του Greyhawk γύρω από το χωριό Hommlet και θεωρείται μια από τις πιο πιστές ψηφιακές αναπαραστάσεις των κανόνων D&D 3.5e.",
        "funFacts": [
            "Το παιχνίδι εισήγαγε ένα μοναδικό ακτινωτό κυκλικό μενού (radial menu) για την επιλογή ξορκιών, επιθέσεων και ικανοτήτων μάχης.",
            "Η αρχική κυκλοφορία υπέφερε από πολλά bugs, οδηγώντας την κοινότητα των modders να ιδρύσει την ομάδα 'Circle of Eight' (Co8), η οποία διόρθωσε και επέκτεινε το παιχνίδι επί δεκαετίες."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Temple_of_Elemental_Evil_(video_game)",
        "tags": ["gaming", "temple_of_elemental_evil", "troika_games", "dnd", "rpg"]
    },
    {
        "id": "gaming_hard_368",
        "text": "Στο ατμοσφαιρικό γερμανικό RPG 'Gothic' (2001) της Piranha Bytes, ποιο υπερφυσικό εμπόδιο παγιδεύει τους κρατούμενους και τους μάγους μέσα στην κοιλάδα των ορυχείων Khorinis;",
        "correct": "Ένας μαγικός ημισφαιρικός θόλος (The Barrier) που επιτρέπει μόνο την είσοδο",
        "distractors": [
            "Μια ζώνη μόνιμης χιονοθύελλας και ψύχους",
            "Ένα δαχτυλίδι από ενεργά ηφαίστεια και λάβα",
            "Ένα πέπλο δηλητηριώδους αερίου που διαλύει τη σάρκα"
        ],
        "explanation": "Δώδεκα μάγοι προσπάθησαν να δημιουργήσουν ένα μαγικό φράγμα γύρω από τα ορυχεία μαγικού μεταλλεύματος, αλλά η μαγεία ξέφυγε από τον έλεγχό τους, καλύπτοντας ολόκληρη την κοιλάδα και παγιδεύοντας και τους ίδιους μέσα.",
        "funFacts": [
            "Οι παγιδευμένοι κρατούμενοι εξεγέρθηκαν, σκότωσαν τους φρουρούς και χωρίστηκαν σε τρεις ανταγωνιστικές φατρίες: το Old Camp, το New Camp και το Swamp Camp.",
            "Το Gothic διέθετε ένα πρωτοποριακό σύστημα καθημερινής ρουτίνας για τους NPCs, οι οποίοι ξυπνούσαν, μαγείρευαν, δούλευαν, κάπνιζαν βότανα και πήγαιναν για ύπνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Gothic_(video_game)",
        "tags": ["gaming", "gothic", "piranha_bytes", "rpg", "khorinis"]
    },
    {
        "id": "gaming_hard_369",
        "text": "Στο πρωτοποριακό action-adventure 'Outcast' (1999) της βελγικής Appeal, ποιο είναι το όνομα του πρώην κομάντο του US Navy SEAL που ταξιδεύει στον εξωγήινο πλανήτη Adelpha;",
        "correct": "Cutter Slade",
        "distractors": ["Jack Slate", "Nick Scryer", "Kurt Hectic"],
        "explanation": "Ο Cutter Slade συνοδεύει μια επιστημονική αποστολή σε μια παράλληλη διάσταση για να επισκευάσει έναν δορυφόρο, αλλά καταλήγει να θεωρείται ο μυθικός μεσσίας 'Ulukaï' από την εξωγήινη φυλή των Talan.",
        "funFacts": [
            "Το Outcast δεν χρησιμοποίησε πολυγωνική επιτάχυνση 3D κάρτας, αλλά μια ιδιόκτητη ray-casting voxel μηχανή γραφικών που υπολογιζόταν εξ ολοκλήρου από τον επεξεργαστή (CPU).",
            "Η συμφωνική μουσική του παιχνιδιού ηχογραφήθηκε από τη Συμφωνική Ορχήστρα της Μόσχας με 80 μουσικούς και 24μελή χορωδία."
        ],
        "source": "https://en.wikipedia.org/wiki/Outcast_(video_game)",
        "tags": ["gaming", "outcast", "appeal", "cutter_slade", "voxels"]
    },
    {
        "id": "gaming_hard_370",
        "text": "Στο θεότρελο sequel δράσης 'MDK2' (2000) που αναπτύχθηκε από τη BioWare, ποιοι είναι οι τρεις playable χαρακτήρες με εντελώς διαφορετικό gameplay ο καθένας;",
        "correct": "Kurt Hectic, Dr. Fluke Hawkins και Max (ένας ρομποτικός σκύλος με 6 πόδια)",
        "distractors": [
            "Jim, Bob και Peter Puppy",
            "Sly Boots, PAL-18 και Grumpos",
            "Razputin, Sasha Nein και Milla Vodello"
        ],
        "explanation": "Ο Kurt βασίζεται σε ακροβατικά άλματα με αλεξίπτωτο κορδέλας και sniper rifle, ο Dr. Hawkins λύνει γρίφους συνδυάζοντας αντικείμενα (όπως τοστιέρες και πυρηνικές μπαταρίες), και ο Max πυροβολεί με τέσσερα όπλα ταυτόχρονα.",
        "funFacts": [
            "Το MDK2 ήταν ένα από τα ελάχιστα παιχνίδια δράσης που ανέπτυξε η BioWare, γνωστή σχεδόν αποκλειστικά για βαθιά RPG όπως το Baldur's Gate και το Mass Effect.",
            "Το ακρωνύμιο 'MDK' είχε πολλές ανεπίσημες ερμηνείες από τους δημιουργούς, όπως 'Murder, Death, Kill' ή 'Mission: Deliver Kindness'."
        ],
        "source": "https://en.wikipedia.org/wiki/MDK2",
        "tags": ["gaming", "mdk2", "bioware", "interplay", "action"]
    },
    {
        "id": "gaming_hard_371",
        "text": "Στο καινοτόμο 3D real-time strategy παιχνίδι 'Sacrifice' (2000) της Shiny Entertainment, ποιος είναι ο βασικός μηχανισμός για να κερδίσει ο μάγος του παίκτη ενέργεια και νέα minions;",
        "correct": "Η θυσία των ψυχών των νεκρών εχθρών στον βωμό του παίκτη (Desecration)",
        "distractors": [
            "Η εξόρυξη κρυστάλλων από υπόγειες φλέβες",
            "Η κατασκευή ναών και η είσπραξη φόρων από πιστούς",
            "Η κατανάλωση μαγικών φίλτρων από τοπικά πηγάδια"
        ],
        "explanation": "Στο Sacrifice, οι ψυχές των πεσόντων πολεμιστών συλλέγονται από Sacrodoctors και μεταφέρονται στον βωμό του παίκτη· αν ο βωμός του αντιπάλου βεβηλωθεί πλήρως με θυσία, ο εχθρικός μάγος εξοστρακίζεται.",
        "funFacts": [
            "Ο παίκτης μπορούσε να υπηρετήσει πέντε διαφορετικούς θεούς: Charnel (θάνατος), James (γη), Pyro (φωτιά), Persephone (ζωή) και Stratos (αέρας).",
            "Το παιχνίδι ήταν ένα από τα πρώτα που απαίτησε κάρτα γραφικών με Hardware Transform & Lighting (T&L)."
        ],
        "source": "https://en.wikipedia.org/wiki/Sacrifice_(video_game)",
        "tags": ["gaming", "sacrifice", "shiny_entertainment", "strategy", "retro"]
    },
    {
        "id": "gaming_hard_372",
        "text": "Στο stand-alone expansion 'Homeworld: Cataclysm' (2000) από την Barking Dog Studios, ποιο ερευνητικό/εξορυκτικό σκάφος του Kiith Somtaaw βρίσκεται αντιμέτωπο με τον εφιάλτη;",
        "correct": "Kuun-Lan",
        "distractors": ["Khar-Selim", "Sajuuk-Khar", "Taiidan Flagship"],
        "explanation": "Το Kuun-Lan, ένα ταπεινό σκάφος εξόρυξης μεταλλευμάτων, ανακαλύπτει μια αρχαία διαστημική κάψουλα που απελευθερώνει το 'The Beast', έναν τεχνο-οργανικό ιό που μολύνει και αφομοιώνει μηχανικά σκάφη και πληρώματα.",
        "funFacts": [
            "Το Homeworld: Cataclysm μετονομάστηκε αργότερα σε 'Homeworld: Emergence' για την ψηφιακή επανακυκλοφορία του στο GOG, καθώς η Blizzard είχε κατοχυρώσει το εμπορικό σήμα 'Cataclysm' για το World of Warcraft.",
            "Η Barking Dog Studios μετονομάστηκε αργότερα σε Rockstar Vancouver και ανέπτυξε το 'Bully'."
        ],
        "source": "https://en.wikipedia.org/wiki/Homeworld:_Cataclysm",
        "tags": ["gaming", "homeworld", "cataclysm", "barking_dog", "sci_fi"]
    },
    {
        "id": "gaming_hard_373",
        "text": "Στο αρχικό 'System Shock' (1994) της Looking Glass Studios, ποιος είναι ο πρώτος τετραψήφιος κωδικός πόρτας που συναντά ο παίκτης, ο οποίος έγινε διάσημο 'easter egg' σε δεκάδες μετέπειτα παιχνίδια;",
        "correct": "451 (ή 0451)",
        "distractors": ["1984", "0070", "1337"],
        "explanation": "Ο κωδικός 0451 ήταν ένας φόρος τιμής στο δυστοπικό μυθιστόρημα 'Fahrenheit 451' του Ray Bradbury και χρησιμοποιήθηκε αργότερα ως ο πρώτος κωδικός πρόσβασης στα Deus Ex, BioShock, Dishonored και Prey.",
        "funFacts": [
            "Σύμφωνα με τον Warren Spector, ο κωδικός 451 ήταν επίσης ο πραγματικός κωδικός της πόρτας των γραφείων της Looking Glass Studios στο Cambridge της Μασαχουσέτης.",
            "Το System Shock τοποθέτησε τον παίκτη στον διαστημικό σταθμό Citadel Station που ελέγχεται από την παρανοϊκή AI SHODAN."
        ],
        "source": "https://en.wikipedia.org/wiki/System_Shock",
        "tags": ["gaming", "system_shock", "looking_glass", "shodan", "easter_egg"]
    },
    {
        "id": "gaming_hard_374",
        "text": "Στο θρυλικό RPG 'Ultima VII: The Black Gate' (1992) του Richard Garriott, ποια ύπουλη φιλοσοφική/θρησκευτική οργάνωση λειτουργεί ως βιτρίνα για την εισβολή του Guardian στην Britannia;",
        "correct": "The Fellowship",
        "distractors": ["The Silver Hand", "The Order of the Silver Twilight", "The Children of the Sun"],
        "explanation": "Η Fellowship, με ηγέτη τον Batlin, κηρύττει ένα φιλοσοφικό σύστημα 'εσωτερικής γαλήνης' που στην πραγματικότητα υπονομεύει τις Οκτώ Αρετές της Britannia και επιτρέπει στον Guardian να κατασκευάσει τη Μαύρη Πύλη.",
        "funFacts": [
            "Ο Richard Garriott σχεδίασε τους δύο βασικούς κακούς Elizabeth και Abraham έτσι ώστε τα αρχικά τους να σχηματίζουν το 'EA', ως σάτιρα κατά της εκδότριας Electronic Arts.",
            "Το Ultima VII είχε έναν από τους πιο διαδραστικούς κόσμους στην ιστορία: οι παίκτες μπορούσαν να ψήσουν ψωμί από αλεύρι και νερό ή να σφυρηλατήσουν σπαθιά σε καμίνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Ultima_VII:_The_Black_Gate",
        "tags": ["gaming", "ultima", "richard_garriott", "origin_systems", "rpg"]
    },
    {
        "id": "gaming_hard_375",
        "text": "Στο 'Wizardry VII: Crusaders of the Dark Savant' (1992) της Sir-Tech, ποιο πανίσχυρο κοσμικό τεχνούργημα που μπορεί να αλλάξει τη μοίρα του σύμπαντος αναζητούν όλοι στον πλανήτη Guardia;",
        "correct": "Astral Dominae",
        "distractors": ["Cosmic Forge", "Destiny Wand", "Chaos Orb"],
        "explanation": "Το Astral Dominae δημιουργήθηκε από τον ίδιο τον Άρχοντα της Δημιουργίας (Phoonzang) και περιέχει το μυστικό της ζωής και της συμπαντικής δύναμης, κάνοντας τον Dark Savant να το καταδιώκει αμείλικτα.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον David W. Bradley και ήταν ένα από τα πρώτα RPG όπου άλλες ομάδες NPCs κινούνταν ανεξάρτητα στον χάρτη αναζητώντας αντικείμενα πριν από τον παίκτη.",
            "Οι παίκτες μπορούσαν να εισαγάγουν το save file της ομάδας τους απευθείας από το προηγούμενο παιχνίδι 'Wizardry VI: Bane of the Cosmic Forge'."
        ],
        "source": "https://en.wikipedia.org/wiki/Wizardry_VII:_Crusaders_of_the_Dark_Savant",
        "tags": ["gaming", "wizardry", "sir_tech", "david_w_bradley", "rpg"]
    },
    {
        "id": "gaming_hard_376",
        "text": "Στο κλασικό open-world RPG 'Might and Magic VI: The Mandate of Heaven' (1998) της New World Computing, σε ποιον φανταστικό κόσμο εξελίσσεται η περιπέτεια της ομάδας των τεσσάρων ηρώων;",
        "correct": "Enroth",
        "distractors": ["Axeoth", "Antagarich", "Jadame"],
        "explanation": "Το Mandate of Heaven τοποθετείται στην ήπειρο Enroth μετά την εξαφάνιση του βασιλιά Roland Ironfist, όπου οι παίκτες πρέπει να σταματήσουν την αίρεση Baa και την εισβολή των εξωγήινων δαιμόνων Kreegan.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον Jon Van Caneghem και συνδύαζε μάχη πρώτου προσώπου σε πραγματικό χρόνο αλλά και σε γύρους (turn-based) με το πάτημα του Enter.",
            "Τα γεγονότα του Might and Magic VI συνδέονται άμεσα με τη στρατηγική σειρά 'Heroes of Might and Magic'."
        ],
        "source": "https://en.wikipedia.org/wiki/Might_and_Magic_VI:_The_Mandate_of_Heaven",
        "tags": ["gaming", "might_and_magic", "new_world_computing", "enroth", "rpg"]
    },
    {
        "id": "gaming_hard_377",
        "text": "Στο αριστούργημα turn-based στρατηγικής 'Heroes of Might and Magic III' (1999), ποια βασίλισσα επιστρέφει στην πατρίδα της για να απελευθερώσει το βασίλειο μετά τη δολοφονία του πατέρα της King Gryphonheart;",
        "correct": "Queen Catherine Ironfist",
        "distractors": ["Queen Isabel", "Lady Audrey", "Queen Adrienne"],
        "explanation": "Η βασίλισσα Catherine Ironfist (σύζυγος του Roland) ηγείται των στρατευμάτων του Castle στην εκστρατεία 'The Restoration of Erathia' ενάντια στους εισβολείς Nighon, Eeofol και τους νεκρομάντες της Deyja.",
        "funFacts": [
            "Ο πατέρας της, Βασιλιάς Nicolas Gryphonheart, δηλητηριάστηκε από προδότες και αναστήθηκε ως απέθαντος βασιλιάς-Lich από τους νεκρομάντες.",
            "Το HoMM3 θεωρείται ευρέως από τους κριτικούς και τους παίκτες ως το κορυφαίο turn-based strategy παιχνίδι φαντασίας όλων των εποχών."
        ],
        "source": "https://en.wikipedia.org/wiki/Heroes_of_Might_and_Magic_III",
        "tags": ["gaming", "homm3", "heroes_of_might_and_magic", "strategy", "catherine_ironfist"]
    },
    {
        "id": "gaming_hard_378",
        "text": "Στο πρωτοποριακό 4X strategy 'Master of Magic' (1994) της SimTex, ποιοι είναι οι δύο παράλληλοι κόσμοι/διαστάσεις που συνδέονται μεταξύ τους μέσω μαγικών πύργων (Towers of Wizardry);",
        "correct": "Arcanus και Myrror",
        "distractors": ["Aethel και Umbra", "Gaia και Tartarus", "Elysium και Nether"],
        "explanation": "Ο Arcanus είναι ένας φυσικός κόσμος με εύφορα εδάφη και συμβατικές φυλές, ενώ ο Myrror είναι ένας σκοτεινός, πλούσιος σε μαγεία κόσμος γεμάτος τέρατα και σπάνια ορυχεία adamantium.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον Steve Barcia (δημιουργό του Master of Orion) και περιλάμβανε πάνω από 200 διαφορετικά ξόρκια σε πέντε σχολές μαγείας.",
            "Οι παίκτες μπορούσαν να κερδίσουν το παιχνίδι ερευνώντας και εκτελώντας το τιτάνιο ξόρκι 'Spell of Mastery'."
        ],
        "source": "https://en.wikipedia.org/wiki/Master_of_Magic",
        "tags": ["gaming", "master_of_magic", "simtex", "4x", "strategy"]
    },
    {
        "id": "gaming_hard_379",
        "text": "Ποιο ολλανδικό στούντιο ανάπτυξης δημιούργησε το ιστορικό turn-based fantasy 4X strategy 'Age of Wonders' (1999) και τις συνέχειές του;",
        "correct": "Triumph Studios",
        "distractors": ["Guerrilla Games", "Spil Games", "Engine Software"],
        "explanation": "Η Triumph Studios (των Lennart Sas και Arno van Wingerden) ανέπτυξε το Age of Wonders σε συνεργασία με την Epic Games, εισάγοντας ένα βαθύ σύστημα τακτικών μαχών σε εξαγωνικό πλέγμα.",
        "funFacts": [
            "Η ιστορία του πρώτου παιχνιδιού επικεντρώνεται στον εμφύλιο σπαραγμό των Ξωτικών μετά τη δολοφονία του βασιλιά Inioch, χωρίζοντάς τα στους Keepers και στο εκδικητικό Cult of Storms.",
            "Η Triumph Studios εξαγοράστηκε το 2017 από την Paradox Interactive."
        ],
        "source": "https://en.wikipedia.org/wiki/Age_of_Wonders_(video_game)",
        "tags": ["gaming", "age_of_wonders", "triumph_studios", "strategy", "4x"]
    },
    {
        "id": "gaming_hard_380",
        "text": "Στο αριστούργημα τακτικής 'Jagged Alliance 2' (1999) της Sir-Tech, ποια αδίστακτη βασίλισσα-δικτάτορας κυβερνά με σιδηρά πυγμή τη φανταστική χώρα Arulco;",
        "correct": "Queen Deidranna Reitman",
        "distractors": ["General Sofia", "Baroness Von Trotha", "Madam Chen"],
        "explanation": "Ο έκπτωτος σύζυγός της Enrico Chivaldori προσλαμβάνει τον παίκτη και μια ομάδα μισθοφόρων μέσω της ψηφιακής υπηρεσίας A.I.M. για να χρηματοδοτήσουν την εξέγερση και να εκθρονίσουν τη Deidranna.",
        "funFacts": [
            "Κάθε μισθοφόρος στο Jagged Alliance 2 είχε μοναδική προσωπικότητα, συμπάθειες, αντιπάθειες και φωνητικές γραμμές, αρνούμενος να συνεργαστεί με μισθοφόρους που μισούσε.",
            "Το παιχνίδι προσομοίωνε λεπτομερώς τη βαλλιστική τροχιά κάθε σφαίρας, τη φθορά όπλων, τη θερμοκρασία και τα τραύματα."
        ],
        "source": "https://en.wikipedia.org/wiki/Jagged_Alliance_2",
        "tags": ["gaming", "jagged_alliance_2", "sir_tech", "tactical", "arulco"]
    },
    {
        "id": "gaming_hard_381",
        "text": "Στο θρυλικό stealth τακτικής 'Commandos: Behind Enemy Lines' (1998) της ισπανικής Pyro Studios, ποιο είναι το κωδικό όνομα και το παρατσούκλι του σκληροτράχηλου Green Beret;",
        "correct": "Tiny (Jack O'Hara)",
        "distractors": ["Duke (René Duchamp)", "Spooky (Thomas Hancock)", "Fins (James Blackwood)"],
        "explanation": "Ο Tiny (Jack O'Hara) είναι ο επικεφαλής της ομάδας των Commandos, ικανός να μεταφέρει βαρέλια καυσίμων, να μαχαιρώνει σιωπηλά τους ναζί στρατιώτες και να θάβεται κάτω από το χιόνι ή την άμμο.",
        "funFacts": [
            "Το παιχνίδι εισήγαγε τους διάσημους κώνους όρασης των εχθρών (vision cones), χωρισμένους σε πράσινο (ασφαλές σε πρηνηδόν θέση) και σκούρο πράσινο (άμεσος εντοπισμός).",
            "Η Pyro Studios ιδρύθηκε στη Μαδρίτη και το Behind Enemy Lines έγινε ένα από τα μεγαλύτερα ευρωπαϊκά blockbusters της εποχής του."
        ],
        "source": "https://en.wikipedia.org/wiki/Commandos:_Behind_Enemy_Lines",
        "tags": ["gaming", "commandos", "pyro_studios", "stealth", "tactical"]
    },
    {
        "id": "gaming_hard_382",
        "text": "Ποιο είναι το όνομα του πιστολέρο πρωταγωνιστή στο Western real-time stealth τακτικής 'Desperados: Wanted Dead or Alive' (2001) της Spellbound Entertainment;",
        "correct": "John Cooper",
        "distractors": ["Doc McCoy", "Sam Williams", "Sanchez"],
        "explanation": "Ο John Cooper αναλαμβάνει για λογαριασμό της εταιρείας σιδηροδρόμων Twinnings & Co να σταματήσει τις μυστηριώδεις ληστείες τρένων από τον ασύλληπτο ληστή El Diablo, σχηματίζοντας μια συμμορία έμπιστων φίλων.",
        "funFacts": [
            "Ο Cooper μπορούσε να πετάξει το μαχαίρι του με απόλυτη ακρίβεια ή να παραπλανήσει τους φρουρούς κουρδίζοντας το μουσικό του ρολόι τσέπης.",
            "Η Spellbound Entertainment χρησιμοποίησε το ίδιο στυλ ισομετρικής stealth τακτικής αργότερα στο 'Robin Hood: The Legend of Sherwood'."
        ],
        "source": "https://en.wikipedia.org/wiki/Desperados:_Wanted_Dead_or_Alive",
        "tags": ["gaming", "desperados", "spellbound", "western", "tactical"]
    },
    {
        "id": "gaming_hard_383",
        "text": "Στο stealth τακτικής 'Robin Hood: The Legend of Sherwood' (2002) της Spellbound, ποιο πρωτότυπο σύστημα χρησιμοποιούσε ο παίκτης για τις μονομαχίες με σπαθί;",
        "correct": "Σχεδιασμό χειρονομιών με τον κέρσορα του ποντικιού (Mouse Gestures)",
        "distractors": [
            "Πάτημα ρυθμικών πλήκτρων σε quick-time events",
            "Σύστημα καρτών επιθέσεων με πόντους δράσης",
            "Αυτόματους υπολογισμούς ζαριών D20 στο παρασκήνιο"
        ],
        "explanation": "Σχεδιάζοντας μια ευθεία γραμμή προς τα εμπρός ο παίκτης εκτελούσε τρύπημα (thrust), σχεδιάζοντας κύκλο έκανε περιστροφική επίθεση (spin attack), ενώ με πλάγια κίνηση έκανε κόψιμο (slash).",
        "funFacts": [
            "Ο Ρομπέν μπορούσε να δωροδοκήσει ζητιάνους ή να ρίξει πουγκιά με χρυσά νομίσματα στους φρουρούς για να μαλώσουν μεταξύ τους και να ανοίξει ο δρόμος.",
            "Αν ο παίκτης ολοκλήρωνε αποστολές χωρίς να σκοτώνει εχθρούς (απλώς αναισθητοποιώντας τους), περισσότεροι παράνομοι προσχωρούσαν στη συμμορία του στο δάσος του Σέργουντ."
        ],
        "source": "https://en.wikipedia.org/wiki/Robin_Hood:_The_Legend_of_Sherwood",
        "tags": ["gaming", "robin_hood", "spellbound", "stealth", "tactical"]
    },
    {
        "id": "gaming_hard_384",
        "text": "Στο πρωτοποριακό adventure 'Blade Runner' (1997) της Westwood Studios, ποιος ντετέκτιβ ερευνά μια υπόθεση δολοφονίας ζώων σε ένα σκοτεινό cyberpunk Los Angeles;",
        "correct": "Ray McCoy",
        "distractors": ["Rick Deckard", "Gaff", "Leon Kowalski"],
        "explanation": "Ο πρωτοετής Blade Runner Ray McCoy αναλαμβάνει να ερευνήσει μια ομάδα εξεγερμένων Replicants με αρχηγό τον Clovis, ενώ ταυτόχρονα διασταυρώνεται με χαρακτήρες από την κλασική ταινία του Ridley Scott.",
        "funFacts": [
            "Σε κάθε νέο πέρασμα του παιχνιδιού, ο αλγόριθμος επέλεγε τυχαία ποιοι χαρακτήρες (ακόμα και ο ίδιος ο πρωταγωνιστής Ray McCoy!) ήταν άνθρωποι και ποιοι Replicants.",
            "Η Westwood χρησιμοποίησε voxels για να αποδώσει ρεαλιστικά τα μοντέλα των χαρακτήρων χωρίς τις παραμορφώσεις των τότε 3D επιταχυντών."
        ],
        "source": "https://en.wikipedia.org/wiki/Blade_Runner_(1997_video_game)",
        "tags": ["gaming", "blade_runner", "westwood_studios", "cyberpunk", "adventure"]
    },
    {
        "id": "gaming_hard_385",
        "text": "Στο ποιητικό adventure 'The Longest Journey' (1999) του Ragnar Tørnquist, ποιοι είναι οι δύο παράλληλοι δίδυμοι κόσμοι ανάμεσα στους οποίους ταξιδεύει η April Ryan;",
        "correct": "Stark (επιστήμη/τάξη) και Arcadia (μαγεία/χάος)",
        "distractors": ["Anor και Londo", "Ghyran και Shyish", "Midkemia και Kelewan"],
        "explanation": "Η April Ryan ανακαλύπτει ότι είναι μια 'Shifter' που μπορεί να ταξιδεύει ανάμεσα στον Stark (τη φουτουριστική βιομηχανική Γη) και την Arcadia (τον μαγικό κόσμο του φανταστικού), αποκαθιστώντας την Ισορροπία (Balance).",
        "funFacts": [
            "Ο δημιουργός Ragnar Tørnquist έγραψε ένα σενάριο εκατοντάδων σελίδων για τη Funcom, καθιστώντας το ένα από τα πιο πλούσια σε διάλογο adventures όλων των εποχών.",
            "Η συνέχεια του παιχνιδιού, το 'Dreamfall: The Longest Journey', κυκλοφόρησε το 2006 προσθέτοντας τη Zoë Castillo ως νέα ηρωίδα."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Longest_Journey",
        "tags": ["gaming", "the_longest_journey", "funcom", "ragnar_tornquist", "adventure"]
    },
    {
        "id": "gaming_hard_386",
        "text": "Στο πανέμορφο steampunk adventure 'Syberia' (2002) του Benoît Sokal, ποια Νεοϋορκέζα δικηγόρος ταξιδεύει στην Ευρώπη για να ολοκληρώσει την εξαγορά ενός εργοστασίου αυτομάτων;",
        "correct": "Kate Walker",
        "distractors": ["Victoria McPherson", "Nicole Collard", "Mia Fey"],
        "explanation": "Η Kate Walker αναζητά τον ιδιοφυή εφευρέτη Hans Voralberg σε ένα ταξίδι με ένα μηχανικό τρένο κουρδίσματος που τη φέρνει μέχρι τα βάθη της Σιβηρίας αναζητώντας ζωντανά μαμούθ.",
        "funFacts": [
            "Ο δημιουργός Benoît Sokal ήταν διάσημος Βέλγος καλλιτέχνης κόμικς, και ο μοναδικός εικαστικός του σχεδιασμός χάρισε στο παιχνίδι μια μελαγχολική art nouveau ατμόσφαιρα.",
            "Ο μηχανικός οδηγός του τρένου, το αυτόματο Oscar, έχει εμμονή με τα επίσημα εισιτήρια και τους κανονισμούς ασφαλείας."
        ],
        "source": "https://en.wikipedia.org/wiki/Syberia",
        "tags": ["gaming", "syberia", "benoit_sokal", "kate_walker", "adventure"]
    },
    {
        "id": "gaming_hard_387",
        "text": "Στο ψυχολογικό horror adventure 'Sanitarium' (1998) της DreamForge Intertainment, ποιο είναι το πραγματικό όνομα του αμνησιακού πρωταγωνιστή που ξυπνά σε ένα εφιαλτικό άσυλο;",
        "correct": "Max Laughton",
        "distractors": ["Daniel Lamb", "James Sunderland", "Edward Carnby"],
        "explanation": "Ο Max Laughton έχει ένα σοβαρό τροχαίο δυστύχημα και ξυπνά με επιδέσμους στο πρόσωπο μέσα σε ένα σουρεαλιστικό άσυλο, ταξιδεύοντας μέσα από παραισθήσεις που συνδέονται με την έρευνά του για μια θανατηφόρα ασθένεια.",
        "funFacts": [
            "Σε διαφορετικά κεφάλαια των παραισθήσεών του, ο παίκτης ελέγχει ένα μικρό κορίτσι (Sarah), έναν τετραπλό εξωγήινο πολεμιστή (Olmec) και τον θεό Anubis.",
            "Το παιχνίδι θεωρείται ένα από τα πιο ατμοσφαιρικά και διαταραγμένα ψυχολογικά θρίλερ στην ιστορία των PC point-and-click."
        ],
        "source": "https://en.wikipedia.org/wiki/Sanitarium_(video_game)",
        "tags": ["gaming", "sanitarium", "dreamforge", "horror", "adventure"]
    },
    {
        "id": "gaming_hard_388",
        "text": "Στο ιδιόρρυθμο FMV adventure 'Bad Mojo' (1996) της Pulse Entertainment, σε ποιο πλάσμα μεταμορφώνεται μυστηριωδώς ο πρωταγωνιστής εντομολόγος Roger Samms;",
        "correct": "Σε κατσαρίδα",
        "distractors": ["Σε αράχνη", "Σε μύγα", "Σε σκορπιό"],
        "explanation": "Ο Roger Samms προσπαθεί να διαφύγει με κλεμμένα χρήματα από ένα άθλιο μπαρ του Σαν Φρανσίσκο, αλλά ένα αρχαίο φυλαχτό τον μεταμορφώνει σε κατσαρίδα, αναγκάζοντάς τον να περιηγηθεί σε βρώμικους σωλήνες, ποντικοπαγίδες και κουζίνες.",
        "funFacts": [
            "Το παιχνίδι αποτελεί μια μοντέρνα, γκροτέσκα αναφορά στη 'Μεταμόρφωση' του Franz Kafka.",
            "Οι προγραμματιστές φωτογράφισαν πραγματικές επιφάνειες και αποχετεύσεις σε μακρο-φακό για να δημιουργήσουν τα φωτορεαλιστικά περιβάλλοντα του παιχνιδιού."
        ],
        "source": "https://en.wikipedia.org/wiki/Bad_Mojo",
        "tags": ["gaming", "bad_mojo", "pulse_entertainment", "adventure", "retro"]
    },
    {
        "id": "gaming_hard_389",
        "text": "Ποιος θρυλικός Ελβετός σουρεαλιστής καλλιτέχνης σχεδίασε τον εφιαλτικό βιομηχανικό 'Dark World' στο horror adventure 'Dark Seed' (1992) της Cyberdreams;",
        "correct": "H.R. Giger",
        "distractors": ["Clive Barker", "Zdzisław Beksiński", "Moebius"],
        "explanation": "Ο H.R. Giger παραχώρησε τα δικαιώματα του χαρακτηριστικού βιομηχανικού/εξωγήινου έργου τέχνης του στην Cyberdreams, όπου ο συγγραφέας Mike Dawson ανακαλύπτει ότι οι 'Ancients' έχουν εμφυτεύσει ένα εξωγήινο έμβρυο στον εγκέφαλό του.",
        "funFacts": [
            "Ο κεντρικός ήρωας Mike Dawson πήρε το όνομά του από τον πραγματικό επικεφαλής σχεδιαστή και παραγωγό του παιχνιδιού, ο οποίος δάνεισε και το πρόσωπό του στα γραφικά.",
            "Το παιχνίδι είχε αυστηρό χρονικό περιθώριο τριών ημερών εντός του παιχνιδιού πριν το έμβρυο εκκολαφθεί και σκοτώσει τον πρωταγωνιστή."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Seed_(video_game)",
        "tags": ["gaming", "dark_seed", "hr_giger", "cyberdreams", "horror"]
    },
    {
        "id": "gaming_hard_390",
        "text": "Στο ακραία βίαιο και σουρεαλιστικό FMV adventure 'Harvester' (1996) της DigiFX Interactive, ποιο είναι το όνομα της φαινομενικά ειδυλλιακής αμερικανικής πόλης του 1953 όπου ξυπνά ο Steve Mason;",
        "correct": "Harvest",
        "distractors": ["Silent Hill", "Twin Peaks", "Pleasantville"],
        "explanation": "Ο Steve ξυπνά χωρίς μνήμη στην πόλη Harvest, όπου όλοι οι κάτοικοι συμπεριφέρονται παράνοια και βίαια, αναγκάζοντάς τον να εκτελέσει αποτρόπαιες πράξεις για να γίνει μέλος του 'Order of the Harvest Moon'.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από τον Gilbert P. Austin ως μια κατάμαυρη σάτιρα της τότε ηθικολογικής υστερίας των ΜΜΕ σχετικά με τη βία στα βιντεοπαιχνίδια.",
            "Λόγω της υπερβολικής ποσότητας αίματος και των σκηνών κανιβαλισμού, το παιχνίδι λογοκρίθηκε ή απαγορεύτηκε σε πολλές ευρωπαϊκές χώρες."
        ],
        "source": "https://en.wikipedia.org/wiki/Harvester_(video_game)",
        "tags": ["gaming", "harvester", "fmv", "horror", "satire"]
    },
    {
        "id": "gaming_hard_391",
        "text": "Στο κλασικό point-and-click survival horror 'Clock Tower' (1995) του Hifumi Kono για το Super Famicom, ποιος μανιακός δολοφόνος καταδιώκει τη Jennifer Simpson στην έπαυλη Barrows;",
        "correct": "Scissorman (Bobby Barrows)",
        "distractors": ["Leatherface", "Pyramid Head", "The Butcher"],
        "explanation": "Ο Scissorman είναι ένα παραμορφωμένο αγόρι οπλισμένο με ένα γιγάντιο ψαλίδι κηπουρικής που καταδιώκει ασταμάτητα τη Jennifer, αναγκάζοντάς την να κρύβεται σε ντουλάπες χωρίς καμία δυνατότητα άμεσης μάχης.",
        "funFacts": [
            "Ο σκηνοθέτης Hifumi Kono εμπνεύστηκε άμεσα την αισθητική και τη μουσική του παιχνιδιού από την ταινία τρόμου 'Phenomena' (1985) του Dario Argento.",
            "Η εμφάνιση της Jennifer Simpson βασίστηκε στην εμφάνιση της νεαρής Jennifer Connelly στην ταινία Phenomena."
        ],
        "source": "https://en.wikipedia.org/wiki/Clock_Tower_(1995_video_game)",
        "tags": ["gaming", "clock_tower", "hifumi_kono", "scissorman", "survival_horror"]
    },
    {
        "id": "gaming_hard_392",
        "text": "Στο καινοτόμο time-travel adventure 'Shadow of Memories' (γνωστό ως 'Shadow of Destiny' στις ΗΠΑ, 2001) της Konami, ποια μυστηριώδης συσκευή επιτρέπει στον Eike Kusch να ταξιδεύει στον χρόνο;",
        "correct": "Z-Pad",
        "distractors": ["Time Spinner", "Chronos Stone", "Ouroboros Dial"],
        "explanation": "Αφού δολοφονείται στην αρχή του παιχνιδιού, ο Eike λαμβάνει το Z-Pad από ένα μυστηριώδες ον με το όνομα Homunculus, ταξιδεύοντας πίσω στον χρόνο (στο 1580, 1902, 1979 και στο σήμερα) για να αποτρέψει τις αλλεπάλληλες απόπειρες δολοφονίας του.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε και γράφτηκε από τη σκηνοθέτιδα Junko Kawano, γνωστή από τη σειρά Suikoden.",
            "Διαθέτει οκτώ διαφορετικά φινάλε ανάλογα με τις ενέργειες του παίκτη στις διάφορες ιστορικές περιόδους της γερμανικής πόλης Lebensbaum."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_of_Memories",
        "tags": ["gaming", "shadow_of_memories", "konami", "time_travel", "junko_kawano"]
    },
    {
        "id": "gaming_hard_393",
        "text": "Στο ατμοσφαιρικό adventure τρόμου πρώτου προσώπου 'Echo Night' (1998) της FromSoftware, σε ποιο πολυτελές επιβατηγό πλοίο-φάντασμα διεξάγεται η έρευνα του Richard Osmond;",
        "correct": "Orpheus",
        "distractors": ["Queen Mary", "Charon", "Poseidon"],
        "explanation": "Ο Richard ταξιδεύει στο παρελθόν μέσα στο πλοίο Orpheus που εξαφανίστηκε μυστηριωδώς το 1913, ελευθερώνοντας τις ψυχές των νεκρών επιβατών εκπληρώνοντας τις τελευταίες τους επιθυμίες αντί να τους πολεμά.",
        "funFacts": [
            "Το Echo Night αναπτύχθηκε από την ομάδα της FromSoftware παράλληλα με τη σειρά King's Field, πριν γίνουν παγκοσμίως διάσημοι με τα Demon's Souls και Dark Souls.",
            "Το παιχνίδι δεν διέθετε όπλα ή μάχη· αν ένα κακόβουλο πνεύμα πλησίαζε, ο παίκτης έπρεπε να ανάψει τα φώτα του δωματίου για να το εξαφανίσει."
        ],
        "source": "https://en.wikipedia.org/wiki/Echo_Night",
        "tags": ["gaming", "echo_night", "fromsoftware", "horror", "playstation"]
    },
    {
        "id": "gaming_hard_394",
        "text": "Στο survival horror 'Haunting Ground' (2005) της Capcom, ποιο είναι το όνομα του λευκού τσοπανόσκυλου (White Swiss Shepherd) που βοηθά τη Fiona Belli να επιβιώσει στο κάστρο Belli;",
        "correct": "Hewie",
        "distractors": ["Brown", "Shadow", "Angelo"],
        "explanation": "Η Fiona πρέπει να εκπαιδεύσει και να φροντίζει τον Hewie δίνοντάς του εντολές να επιτεθεί σε διώκτες (όπως ο Debilitas), να αναζητήσει αντικείμενα ή να πατήσει διακόπτες.",
        "funFacts": [
            "Το Haunting Ground θεωρείται πνευματικός διάδοχος της σειράς Clock Tower και εισήγαγε μετρητή πανικού (Panic Meter) που θόλωνε την οθόνη και έκανε τη Fiona να σκοντάφτει ανεξέλεγκτα.",
            "Το animation και τα μοντέλα του Hewie επαναχρησιμοποιήθηκαν εν μέρει από τον σκύλο που σώζει ο Leon στο 'Resident Evil 4'."
        ],
        "source": "https://en.wikipedia.org/wiki/Haunting_Ground",
        "tags": ["gaming", "haunting_ground", "capcom", "survival_horror", "hewie"]
    },
    {
        "id": "gaming_hard_395",
        "text": "Στο ψυχολογικό horror 'Rule of Rose' (2006) της Punchline, ποια σαδιστική ιεραρχία κοριτσιών βασανίζει τη νεαρή Jennifer μέσα σε ένα τεράστιο αερόπλοιο της δεκαετίας του 1930;",
        "correct": "Red Crayon Aristocrats (Αριστοκράτισσες της Κόκκινης Κηρομπογιάς)",
        "distractors": [
            "Black Rose Society",
            "The Dolls of Saint Gabriel",
            "The Crimson Sisterhood"
        ],
        "explanation": "Η Jennifer πρέπει να προσφέρει κάθε μήνα ένα πολύτιμο 'δώρο' στο συμβούλιο των Red Crayon Aristocrats (όπως πεταλούδες ή πουλιά) για να μην τιμωρηθεί βάναυσα από τα υπόλοιπα ορφανά κορίτσια.",
        "funFacts": [
            "Ο πιστός σκύλος της Jennifer, ο Brown, μπορεί να μυρίσει αντικείμενα στο πάτωμα για να οδηγήσει την παίκτρια στα ίχνη βασικών στοιχείων της πλοκής.",
            "Το παιχνίδι υπήρξε θύμα μιας τεράστιας εκστρατείας παραπληροφόρησης στα ευρωπαϊκά ΜΜΕ, με αποτέλεσμα την ακύρωση της κυκλοφορίας του στο Ηνωμένο Βασίλειο."
        ],
        "source": "https://en.wikipedia.org/wiki/Rule_of_Rose",
        "tags": ["gaming", "rule_of_rose", "punchline", "horror", "playstation_2"]
    },
    {
        "id": "gaming_hard_396",
        "text": "Στο ιδιαίτερο stealth/horror comedy 'Gregory Horror Show' (2003) της Capcom, ποιο ποντίκι-ξενοδόχος υποδέχεται τον παίκτη στο παράξενο ξενοδοχείο Gregory House;",
        "correct": "Gregory",
        "distractors": ["James", "Judas", "Bartholomew"],
        "explanation": "Ο παίκτης έχει χάσει τη μνήμη του και ο Gregory μαζί με τον Χάρο (Death) του υπόσχονται ότι θα επιστρέψει στον πραγματικό κόσμο αν κατασκοπεύσει τους τερατώδεις ενοίκους και τους κλέψει τα μπουκάλια με τις ψυχές τους.",
        "funFacts": [
            "Το παιχνίδι βασίστηκε στην ομώνυμη CGI τηλεοπτική σειρά anime του Naomi Iwata, με όλους τους χαρακτήρες να έχουν κυβικό σχήμα τύπου 'papercraft'.",
            "Ο παίκτης έπρεπε να κρυφοκοιτάζει από τις κλειδαρότρυπες των δωματίων για να μάθει τις συνήθειες και τις αδυναμίες κάθε ενοίκου."
        ],
        "source": "https://en.wikipedia.org/wiki/Gregory_Horror_Show_(video_game)",
        "tags": ["gaming", "gregory_horror_show", "capcom", "stealth", "cult"]
    },
    {
        "id": "gaming_hard_397",
        "text": "Στο σουρεαλιστικό 'Killer7' (2005) του Goichi Suda (Suda51), ποιο είναι το όνομα του ηλικιωμένου άνδρα σε αναπηρικό καροτσάκι του οποίου οι επτά δολοφονικές προσωπικότητες εκτελούν αποστολές;",
        "correct": "Harman Smith",
        "distractors": ["Dan Smith", "Kun Lan", "Garcian Smith"],
        "explanation": "Ο Harman Smith διαθέτει τη μοναδική ικανότητα να υλοποιεί σωματικά επτά διαφορετικούς εκτελεστές (τον 'Smith Syndicate'), πολεμώντας τους αυτοκτονικούς τρομοκράτες 'Heaven Smile' για λογαριασμό της αμερικανικής κυβέρνησης.",
        "funFacts": [
            "Ήταν μέρος των περίφημων 'Capcom Five', μιας σειράς πέντε αποκλειστικών παιχνιδιών που ανακοινώθηκαν αρχικά για το Nintendo GameCube.",
            "Το παιχνίδι χρησιμοποιούσε ένα εξαιρετικά αντισυμβατικό σύστημα κίνησης 'on-rails' όπου ο παίκτης πατούσε ένα κουμπί για να τρέξει πάνω σε προκαθορισμένες διακλαδώσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Killer7",
        "tags": ["gaming", "killer7", "suda51", "grasshopper", "gamecube"]
    },
    {
        "id": "gaming_hard_398",
        "text": "Στο καλτ beat 'em up 'God Hand' (2006) της Clover Studio, ποιο είναι το όνομα του αλαζονικού πρωταγωνιστή που του ακρωτηρίασαν το δεξί χέρι και απέκτησε το θεϊκό God Hand;",
        "correct": "Gene",
        "distractors": ["Shannon", "Azel", "Elvis"],
        "explanation": "Ο Gene προστατεύει τη νεαρή Olivia και πολεμά τους Four Devas των δαιμόνων, διαθέτοντας ένα πανίσχυρο οπλοστάσιο από εκατοντάδες παραμετροποιήσιμες πολεμικές κινήσεις και επιθέσεις ρουλέτας (God Reel).",
        "funFacts": [
            "Το παιχνίδι διέθετε δυναμικό σύστημα δυσκολίας που αυξανόταν σε πραγματικό χρόνο (από Level 1 έως Level Die) όσο καλύτερα έπαιζε ο παίκτης χωρίς να δέχεται χτυπήματα.",
            "Ήταν το τελευταίο παιχνίδι που κυκλοφόρησε η Clover Studio πριν κλείσει από την Capcom και οι βασικοί δημιουργοί της ιδρύσουν την PlatinumGames."
        ],
        "source": "https://en.wikipedia.org/wiki/God_Hand",
        "tags": ["gaming", "god_hand", "clover_studio", "action", "beat_em_up"]
    },
    {
        "id": "gaming_hard_399",
        "text": "Στο action platformer 'Viewtiful Joe' (2003) της Clover Studio και της Capcom, ποιες είναι οι τρεις μοναδικές υπερδυνάμεις 'VFX Powers' που χειρίζεται ο Joe;",
        "correct": "Slow, Mach Speed και Zoom In",
        "distractors": [
            "Fast Forward, Rewind και Pause",
            "Invisibility, Double Jump και Super Punch",
            "Freeze, Hyper Speed και Mega Blast"
        ],
        "explanation": "Οι δυνάμεις VFX του Joe βασίζονται σε τεχνικές επεξεργασίας ταινιών δράσης: το Slow επιβραδύνει τον χρόνο και πολλαπλασιάζει τη ζημιά, το Mach Speed δημιουργεί πολλαπλά είδωλα με φωτιά, και το Zoom In ξεκλειδώνει νέες καταστροφικές κλωτσιές.",
        "funFacts": [
            "Ο σκηνοθέτης Hideki Kamiya εμπνεύστηκε τον χαρακτήρα από τα κλασικά ιαπωνικά Tokusatsu σόου υπερηρώων, όπως το Kamen Rider και το Ultraman.",
            "Το περίφημο σύνθημα μεταμόρφωσης του Joe είναι: 'Henshin-a-go-go, baby!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Viewtiful_Joe_(video_game)",
        "tags": ["gaming", "viewtiful_joe", "clover_studio", "hideki_kamiya", "gamecube"]
    },
    {
        "id": "gaming_hard_400",
        "text": "Στο υβρίδιο στρατηγικής και δράσης 'Hostile Waters: Antaeus Rising' (2001) της Rage Software, ποιος θρυλικός ηθοποιός (διάσημος ως ο 4ος Doctor Who) χαρίζει τη φωνή του ως αφηγητής και κεντρικός υπολογιστής;",
        "correct": "Tom Baker",
        "distractors": ["Patrick Stewart", "Christopher Lee", "John Hurt"],
        "explanation": "Ο Tom Baker δανείζει τη βαθιά, επιβλητική φωνή του στο Antaeus, ένα τεράστιο προσαρμόσιμο πολεμικό καταδρομικό/νανο-εργοστάσιο που ανακαλεί τις συνειδήσεις νεκρών στρατιωτών μέσω 'soulchips' για να πιλοτάρουν άρματα μάχης και ελικόπτερα.",
        "funFacts": [
            "Το σενάριο του παιχνιδιού γράφτηκε από τον διάσημο Βρετανό συγγραφέα κόμικς Warren Ellis (γνωστό από το Transmetropolitan).",
            "Ο παίκτης μπορούσε να σχεδιάσει την τακτική σε έναν 3D χάρτη και ταυτόχρονα να πάρει τον άμεσο έλεγχο οποιασδήποτε μονάδας σε πρώτο ή τρίτο πρόσωπο."
        ],
        "source": "https://en.wikipedia.org/wiki/Hostile_Waters:_Antaeus_Rising",
        "tags": ["gaming", "hostile_waters", "rage_software", "tom_baker", "strategy"]
    },
    {
        "id": "gaming_hard_401",
        "text": "Στο rail-shooter 'Panzer Dragoon Orta' (2002) της Smilebit για το αρχικό Xbox, ποιες είναι οι τρεις βασικές μορφές στις οποίες μπορεί να μεταμορφωθεί ο δράκος του παίκτη εν πτήσει;",
        "correct": "Base Wing, Heavy Wing και Glide Wing",
        "distractors": [
            "Fire Wing, Ice Wing και Thunder Wing",
            "Alpha Form, Beta Form και Omega Form",
            "Speed Drake, Armor Drake και Mystic Drake"
        ],
        "explanation": "Το Base Wing προσφέρει ισορροπία, το Heavy Wing δίνει πανίσχυρη δύναμη πυρός και berserk επιθέσεις με μειωμένη ευκινησία, ενώ το Glide Wing παρέχει μέγιστη ταχύτητα και ευκολία αποφυγής εχθρικών πυρών.",
        "funFacts": [
            "Το παιχνίδι περιλάμβανε ως ξεκλείδωτο bonus ολόκληρο το αυθεντικό 'Panzer Dragoon' του Sega Saturn του 1995.",
            "Η πρωταγωνίστρια Orta αποκαλύπτεται ότι είναι η κόρη της Azel από το αριστουργηματικό RPG 'Panzer Dragoon Saga'."
        ],
        "source": "https://en.wikipedia.org/wiki/Panzer_Dragoon_Orta",
        "tags": ["gaming", "panzer_dragoon_orta", "smilebit", "sega", "xbox"]
    },
    {
        "id": "gaming_hard_402",
        "text": "Στο 'Jet Set Radio Future' (2002) της Smilebit για το Xbox, ποιος εκκεντρικός πειρατής DJ εκπέμπει ασταμάτητα funk, hip-hop και ηλεκτρονική μουσική για τους GG skaters;",
        "correct": "DJ Professor K",
        "distractors": ["DJ Atomika", "DJ Cyber-X", "DJ Soundwave"],
        "explanation": "Ο DJ Professor K είναι η φωνή του υπόγειου ραδιοφωνικού σταθμού 'Jet Set Radio' στο φουτουριστικό Τόκιο του 2024, ενθαρρύνοντας τις συμμορίες inline skaters να ζωγραφίσουν γκράφιτι και να αντισταθούν στον όμιλο Rokkaku.",
        "funFacts": [
            "Το soundtrack περιλάμβανε θρυλικά κομμάτια από τον συνθέτη Hideki Naganuma καθώς και συγκροτήματα όπως οι The Crows και οι Guitar Vader.",
            "Το JSRF κυκλοφόρησε σε ένα διάσημο διπλό πακέτο δίσκου (bundle) μαζί με το 'Sega GT 2002', συνοδεύοντας εκατομμύρια κονσόλες Xbox."
        ],
        "source": "https://en.wikipedia.org/wiki/Jet_Set_Radio_Future",
        "tags": ["gaming", "jet_set_radio_future", "smilebit", "sega", "xbox"]
    },
    {
        "id": "gaming_hard_403",
        "text": "Ποιο απαιτητικό 3D sci-fi action shooter της Smilebit (2002) για το Xbox απαιτούσε ταυτόχρονη χρήση των δύο αναλογικών μοχλών για συνεχή boost dashes στον αέρα;",
        "correct": "Gunvalkyrie",
        "distractors": ["Otogi", "Phantom Crash", "Breakdown"],
        "explanation": "Στο Gunvalkyrie, οι πράκτορες Kelly O'Ryan και Saburouta Yashiro πολεμούν μεταλλαγμένα έντομα σε μια εναλλακτική βικτωριανή steampunk εποχή, χρησιμοποιώντας ένα από τα πιο απαιτητικά συστήματα ώθησης jetpack που σχεδιάστηκαν ποτέ.",
        "funFacts": [
            "Το Gunvalkyrie σχεδιαζόταν αρχικά για το Sega Dreamcast με υποστήριξη ειδικού χειριστηρίου με dual-analog/light-gun πριν μεταφερθεί στο Xbox.",
            "Ο βαθμός δυσκολίας του ήταν τόσο υψηλός που πολλοί παίκτες και κριτικοί δυσκολεύονταν να ολοκληρώσουν ακόμα και τις πρώτες αποστολές."
        ],
        "source": "https://en.wikipedia.org/wiki/Gunvalkyrie",
        "tags": ["gaming", "gunvalkyrie", "smilebit", "sega", "xbox"]
    },
    {
        "id": "gaming_hard_404",
        "text": "Στο hack-and-slash παιχνίδι δράσης 'Otogi: Myth of Demons' (2002) της FromSoftware για το Xbox, ποιος απέθαντος πολεμιστής πολεμά δαίμονες στην περίοδο Heian της Ιαπωνίας;",
        "correct": "Raikoh Minamoto",
        "distractors": ["Minamoto no Yoshitsune", "Taira no Masakado", "Abe no Seimei"],
        "explanation": "Ο Raikoh εκτελέστηκε επειδή αρνήθηκε να δολοφονήσει την ίδια του τη φυλή, αλλά ανασταίνεται από μια μυστηριώδη πριγκίπισσα για να καθαρίσει την Ιαπωνία από τους δαίμονες που απελευθερώθηκαν μετά τη θραύση μιας ιερής σφραγίδας.",
        "funFacts": [
            "Το Otogi εντυπωσίασε τους παίκτες με τα πλήρως καταστρέψιμα περιβάλλοντά του: σχεδόν κάθε δέντρο, ναός, βράχος και τοίχος μπορούσε να θρυμματιστεί σε κομμάτια.",
            "Το παιχνίδι απέκτησε sequel το 2003 με τίτλο 'Otogi 2: Immortal Warriors', προσθέτοντας πέντε νέους playable πολεμιστές."
        ],
        "source": "https://en.wikipedia.org/wiki/Otogi:_Myth_of_Demons",
        "tags": ["gaming", "otogi", "fromsoftware", "xbox", "action"]
    },
    {
        "id": "gaming_hard_405",
        "text": "Ποιο παιχνίδι προσομοίωσης mecha (Vertical Tank) της Capcom (2002) για το Xbox έγινε διάσημο για το κολοσσιαίο χειριστήριό του με 40 κουμπιά, 2 joysticks, 3 ποδομοχλούς και κουμπί εκτίναξης;",
        "correct": "Steel Battalion",
        "distractors": ["MechAssault", "Chromehounds", "Armored Core: Nexus"],
        "explanation": "Το Steel Battalion απαιτούσε από τον παίκτη να ακολουθήσει μια ολόκληρη διαδικασία εκκίνησης 15 δευτερολέπτων με διακόπτες και κουμπιά· αν ο παίκτης δεν πατούσε εγκαίρως το κουμπί εκτίναξης (Eject Button) πριν καταστραφεί το mecha, το save file του διαγραφόταν οριστικά!",
        "funFacts": [
            "Το κουμπί Eject καλυπτόταν από ένα προστατευτικό διαφανές πλαστικό καπάκι για να αποτρέπονται τα κατά λάθος πατήματα κατά τη διάρκεια σκληρών μαχών.",
            "Το παιχνίδι κυκλοφόρησε σε ένα τεράστιο κουτί βάρους περίπου 10 κιλών και κόστιζε 200 δολάρια κατά την κυκλοφορία του."
        ],
        "source": "https://en.wikipedia.org/wiki/Steel_Battalion",
        "tags": ["gaming", "steel_battalion", "capcom", "mecha", "controller"]
    },
    {
        "id": "gaming_hard_406",
        "text": "Στο aerial combat adventure 'Crimson Skies: High Road to Revenge' (2003) της FASA Studio για το Xbox, ποιος είναι ο γοητευτικός πειρατής των αιθέρων που πιλοτάρει το αεροπλάνο Devastator;",
        "correct": "Nathan Zachary",
        "distractors": ["Tenzing Fowles", "Jonathan Paladin", "Jack Malone"],
        "explanation": "Ο Nathan Zachary είναι ο ηγέτης των Fortune Hunters σε μια εναλλακτική δεκαετία του 1930 όπου οι ΗΠΑ έχουν διασπαστεί σε ανεξάρτητα κυρίαρχα κράτη και τα zeppelins και αεροπλάνα κυριαρχούν στις μεταφορές.",
        "funFacts": [
            "Το παιχνίδι υπήρξε μία από τις πρώτες μεγάλες επιδείξεις της υπηρεσίας Xbox Live, υποστηρίζοντας αερομαχίες έως και 16 παικτών.",
            "Η σειρά Crimson Skies ξεκίνησε αρχικά ως επιτραπέζιο παιχνίδι στρατηγικής με μινιατούρες από τη FASA Corporation."
        ],
        "source": "https://en.wikipedia.org/wiki/Crimson_Skies:_High_Road_to_Revenge",
        "tags": ["gaming", "crimson_skies", "fasa_studio", "xbox", "flight"]
    },
    {
        "id": "gaming_hard_407",
        "text": "Ποιο παιχνίδι δράσης με mecha του 2002 από την Day 1 Studios και τη Microsoft Games υπήρξε το πρώτο παιχνίδι που υποστήριξε την online υπηρεσία Xbox Live κατά το λανσάρισμά της;",
        "correct": "MechAssault",
        "distractors": ["Steel Battalion", "Unreal Championship", "Tom Clancy's Ghost Recon"],
        "explanation": "Το MechAssault, βασισμένο στο σύμπαν του BattleTech, κυκλοφόρησε τον Νοέμβριο του 2002 την ίδια ημέρα με την έναρξη λειτουργίας του Xbox Live, επιτρέποντας σε παίκτες να πολεμούν με BattleMechs (όπως το Timber Wolf/Mad Cat) μέσω voice chat.",
        "funFacts": [
            "Μια ευπάθεια buffer overflow στο αρχικό save file του MechAssault ήταν ένα από τα πρώτα και πιο δημοφιλή μέσα για το softmodding της κονσόλας Xbox.",
            "Το soundtrack του παιχνιδιού περιλάμβανε τραγούδια από συγκροτήματα όπως οι Papa Roach και οι Korn."
        ],
        "source": "https://en.wikipedia.org/wiki/MechAssault",
        "tags": ["gaming", "mechassault", "day_1_studios", "xbox_live", "battletech"]
    },
    {
        "id": "gaming_hard_408",
        "text": "Στο cult post-apocalyptic action παιχνίδι 'Phantom Dust' (2004) του Yukio Futatsugi για το Xbox, ποιος μηχανισμός συνδυάστηκε με μάχες τρίτου προσώπου σε καταστρέψιμες αρένες;",
        "correct": "Συλλογή και χτίσιμο τράπουλας καρτών (Deck-building με πάνω από 300 ικανότητες)",
        "distractors": [
            "Turn-based τακτική τοποθέτηση μονάδων σε πλέγμα",
            "Χρήση ρυθμικών συνδυασμών πλήκτρων (QTEs)",
            "Οδήγηση εξοπλισμένων buggy οχημάτων"
        ],
        "explanation": "Στο Phantom Dust, οι παίκτες φτιάχνουν 'Arsenal' (τράπουλες) με κάψουλες ικανοτήτων (επιθέσεις, άμυνες, buffs) που εμφανίζονται τυχαία σε 4 κουμπιά κατά τη διάρκεια έντονων μαχών σε πραγματικό χρόνο.",
        "funFacts": [
            "Ο δημιουργός Yukio Futatsugi ήταν ο σκηνοθέτης της ιστορικής σειράς Panzer Dragoon.",
            "Το παιχνίδι κυκλοφόρησε εκ νέου ως δωρεάν ανανεωμένη έκδοση (remaster) για Xbox One και Windows 10 το 2017."
        ],
        "source": "https://en.wikipedia.org/wiki/Phantom_Dust",
        "tags": ["gaming", "phantom_dust", "yukio_futatsugi", "xbox", "deck_building"]
    },
    {
        "id": "gaming_hard_409",
        "text": "Στο πρωτοποριακό FPS/brawler 'Breakdown' (2004) της Namco για το Xbox, ποιο στοιχείο σχεδιασμού εφάρμοσε αυστηρά η ομάδα ανάπτυξης καθ' όλη τη διάρκεια της εμπειρίας;",
        "correct": "Αποκλειστική οπτική πρώτου προσώπου χωρίς διακοπή (ακόμα και όταν ο παίκτης τρώει, πίνει ή πέφτει στο έδαφος)",
        "distractors": [
            "Πλήρη απουσία μουσικής υπόκρουσης και ηχητικών εφέ",
            "Μόνιμο θάνατο (permadeath) χωρίς δυνατότητα αποθήκευσης",
            "Έλεγχο αποκλειστικά μέσω φωνητικών εντολών μικροφώνου"
        ],
        "explanation": "Ο πρωταγωνιστής Derrick Cole δεν βγαίνει ποτέ από την οπτική πρώτου προσώπου: όταν πίνει ένα κουτάκι αναψυκτικό, όταν κάνει εμετό, όταν ξυλοκοπείται και πέφτει ανάσκελα ή όταν σκαρφαλώνει σκάλες, η κάμερα παραμένει απόλυτα προσαρτημένη στα μάτια του.",
        "funFacts": [
            "Το σύστημα μάχης σώμα με σώμα σε πρώτο πρόσωπο ενέπνευσε μετέπειτα παιχνίδια όπως τα Condemned: Criminal Origins και Mirror's Edge.",
            "Η πλοκή αφορά μια μυστηριώδη υπερδύναμη που ονομάζεται 'T' και εξωγήινους πολεμιστές γνωστούς ως T'lan."
        ],
        "source": "https://en.wikipedia.org/wiki/Breakdown_(video_game)",
        "tags": ["gaming", "breakdown", "namco", "xbox", "fps"]
    },
    {
        "id": "gaming_hard_410",
        "text": "Στο αριστούργημα 'Shenmue II' (2001) της Sega AM2 σε σκηνοθεσία Yu Suzuki, σε ποιο θρυλικό και δαιδαλώδες πυκνοκατοικημένο αστικό γκέτο του Χονγκ Κονγκ ταξιδεύει ο Ryo Hazuki αναζητώντας τον Yuanda Zhu;",
        "correct": "Kowloon Walled City (Περιτειχισμένη Πόλη του Καουλούν)",
        "distractors": ["Aberdeen Harbour", "Wan Chai", "Mong Kok"],
        "explanation": "Ο Ryo φτάνει στην Περιτειχισμένη Πόλη του Kowloon, μια πραγματική ιστορική πολυώροφη μεγαλοδομή ανεξέλεγκτης δόμησης και εγκλήματος, όπου συνεργάζεται με τον συμμορίτη Ren of Heavens για να αντιμετωπίσει τη μαφία Yellow Head.",
        "funFacts": [
            "Η πραγματική Περιτειχισμένη Πόλη του Καουλούν κατεδαφίστηκε μεταξύ 1993 και 1994, και το Shenmue II παραμένει μία από τις πιο πιστές και ατμοσφαιρικές ψηφιακές αναπαραστάσεις της στην ιστορία των βιντεοπαιχνιδιών.",
            "Στη Βόρεια Αμερική, το Shenmue II δεν κυκλοφόρησε ποτέ στο Dreamcast αλλά μεταφέρθηκε αποκλειστικά στο Microsoft Xbox το 2002, περιλαμβάνοντας ένα DVD με την ταινία Shenmue The Movie."
        ],
        "source": "https://en.wikipedia.org/wiki/Shenmue_II",
        "tags": ["gaming", "shenmue_2", "yu_suzuki", "sega", "kowloon"]
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 4.")
    validate_and_append("gaming", "hard", 5, questions)

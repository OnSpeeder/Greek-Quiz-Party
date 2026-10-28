# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_med_311",
        "text": "Στο τέλος του 'Half-Life 2: Episode Two' (2007), ποιος αγαπημένος κεντρικός χαρακτήρας και ηγέτης της αντίστασης σκοτώνεται μπροστά στα μάτια της κόρης του από έναν Combine Advisor;",
        "correct": "Ο Eli Vance",
        "distractors": ["Ο Isaac Kleiner", "Ο Arne Magnusson", "Ο Barney Calhoun"],
        "explanation": "Ο πατέρας της Alyx, Eli Vance, δολοφονείται τραγικά από έναν Advisor στο υπόστεγο εκτόξευσης πυραύλων, αφήνοντας τους παίκτες σε ένα βασανιστικό cliffhanger για 13 χρόνια.",
        "funFacts": [
            "Το τέλος αυτό ανατράπηκε με εντυπωσιακό τρόπο στο VR παιχνίδι 'Half-Life: Alyx' (2020) μέσω της παρέμβασης του G-Man.",
            "Ο Eli Vance ήταν ο πρώτος άνθρωπος που ίδρυσε το εργαστήριο Black Mesa East στην City 17."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_2:_Episode_Two",
        "tags": ["gaming", "half_life", "valve", "eli_vance", "story"]
    },
    {
        "id": "gaming_med_312",
        "text": "Στο πρωτοποριακό VR παιχνίδι 'Half-Life: Alyx' (2020), ποιο ζευγάρι γαντιών χειρισμού βαρύτητας χρησιμοποιεί η Alyx για να τραβάει αντικείμενα από μακριά;",
        "correct": "The Russells (Τα Ράσελ)",
        "distractors": ["The Gravity Gloves", "The Vectrons", "The Manupods"],
        "explanation": "Τα γάντια κατασκευάστηκαν από τον εκκεντρικό εφευρέτη Russell και επιτρέπουν στον παίκτη να στοχεύει ένα αντικείμενο, να τινάζει τον καρπό του και να το πιάνει στον αέρα.",
        "funFacts": [
            "Ο Russell επέμενε να ονομαστούν τα γάντια με το δικό του επώνυμο ('The Russells') παρά τις αντιρρήσεις της Alyx.",
            "Τα γάντια διαθέτουν φωτεινή ένδειξη LED στο πίσω μέρος του χεριού που δείχνει τα αποθέματα υγείας και πυρομαχικών της Alyx."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life:_Alyx",
        "tags": ["gaming", "half_life", "valve", "vr", "weapons"]
    },
    {
        "id": "gaming_med_313",
        "text": "Στο 'Left 4 Dead 2' (2009), ποια πόλη του αμερικανικού Νότου διασχίζουν οι επιζώντες στην εκστρατεία 'The Parish' με τελικό προορισμό μια τεράστια γέφυρα;",
        "correct": "Νέα Ορλεάνη (New Orleans)",
        "distractors": ["Ατλάντα", "Σαβάνα", "Μαϊάμι"],
        "explanation": "Η εκστρατεία The Parish διαδραματίζεται στη Γαλλική Συνοικία της Νέας Ορλεάνης και ολοκληρώνεται με ένα δραματικό σπριντ πάνω στη γέφυρα εν μέσω βομβαρδισμών από τον στρατό.",
        "funFacts": [
            "Το Left 4 Dead 2 πρόσθεσε τρία νέα ειδικά μολυσμένα ζόμπι: τον Charger, τη Spitter και τον Jockey.",
            "Πρόσθεσε επίσης για πρώτη φορά όπλα σώμα με σώμα (melee), όπως τηγάνια, ματσέτες, τσεκούρια και ένα μπαστούνι του κρίκετ."
        ],
        "source": "https://en.wikipedia.org/wiki/Left_4_Dead_2",
        "tags": ["gaming", "left_4_dead", "valve", "campaign", "zombies"]
    },
    {
        "id": "gaming_med_314",
        "text": "Ποιο είναι το διαβόητο τουφέκι ελεύθερου σκοπευτή στο 'Counter-Strike' που προσφέρει ακαριαίο θάνατο με ένα μόνο χτύπημα στον κορμό;",
        "correct": "AWP (Arctic Warfare Police / Magnum Sniper Rifle)",
        "distractors": ["Scout", "SG 550", "G3SG1"],
        "explanation": "Το AWP είναι το πιο ακριβό και καθοριστικό όπλο στο ανταγωνιστικό Counter-Strike, ικανό να κρίνει ολόκληρους γύρους στα χέρια ενός ικανού sniper.",
        "funFacts": [
            "Στο Counter-Strike: Global Offensive, το skin 'AWP | Dragon Lore' έγινε ένα από τα πιο ακριβά ψηφιακά αντικείμενα στον κόσμο, φτάνοντας τιμές δεκάδων χιλιάδων δολαρίων.",
            "Η ταχύτητα κίνησης του παίκτη μειώνεται δραματικά όταν κρατάει το AWP, ενώ ο πυροβολισμός χωρίς σκόπευση (no-scope) έχει τεράστια απόκλιση."
        ],
        "source": "https://en.wikipedia.org/wiki/Counter-Strike",
        "tags": ["gaming", "counter_strike", "valve", "esports", "weapons"]
    },
    {
        "id": "gaming_med_315",
        "text": "Πώς ονομάζεται το πολυπόθητο τρόπαιο που απονέμεται στους παγκόσμιους πρωταθλητές του ετήσιου τουρνουά 'The International' στο 'Dota 2';",
        "correct": "Aegis of Champions (Η Αιγίδα των Πρωταθλητών)",
        "distractors": ["The Summoner's Cup", "The Crystal Chalice", "The Divine Rapier"],
        "explanation": "Το Aegis of Champions είναι μια μπρούντζινη και ασημένια ασπίδα πάνω στην οποία χαράσσονται τα ονόματα των νικητών κάθε χρονιάς.",
        "funFacts": [
            "Το The International 2021 κατέχει το απόλυτο ιστορικό ρεκόρ χρηματικού επάθλου στα esports, ξεπερνώντας τα 40 εκατομμύρια δολάρια.",
            "Κάθε μέλος της νικήτριας ομάδας λαμβάνει ένα ακριβές μικρότερο μεταλλικό αντίγραφο της ασπίδας."
        ],
        "source": "https://en.wikipedia.org/wiki/The_International_(Dota_2)",
        "tags": ["gaming", "dota_2", "valve", "esports", "the_international"]
    },
    {
        "id": "gaming_med_316",
        "text": "Ποιες δύο αδελφές πρωταγωνιστούν στη βραβευμένη σειρά κινουμένων σχεδίων 'Arcane' που βασίζεται στο σύμπαν του 'League of Legends';",
        "correct": "Vi και Jinx (Powder)",
        "distractors": ["Kayle και Morgana", "Lux και Katarina", "Ashe και Sejuani"],
        "explanation": "Η σειρά του Netflix και της Riot Games εξερευνά την τραγική διάσπαση των δύο ορφανών αδελφών ανάμεσα στην πλούσια πόλη Piltover και τον υπόκοσμο του Zaun.",
        "funFacts": [
            "Το Arcane απέσπασε τέσσερα βραβεία Primetime Emmy, γράφοντας ιστορία ως η πρώτη σειρά βασισμένη σε βιντεοπαιχνίδι που κερδίζει Emmy εξαιρετικού προγράμματος κινουμένων σχεδίων.",
            "Το τραγούδι των τίτλων 'Enemy' ερμηνεύτηκε από τους Imagine Dragons σε συνεργασία με τον ράπερ JID."
        ],
        "source": "https://en.wikipedia.org/wiki/Arcane_(TV_series)",
        "tags": ["gaming", "league_of_legends", "riot_games", "arcane"]
    },
    {
        "id": "gaming_med_317",
        "text": "Ποια είναι τα πρώτα λόγια που απαγγέλλει ο βασιλιάς Terenas Menethil στο διάσημο cinematic εισαγωγής του 'Wrath of the Lich King';",
        "correct": "My son, the day you were born, the very forests of Lordaeron whispered the name... Arthas",
        "distractors": [
            "No king rules forever, my son",
            "Behold the power of the frozen throne",
            "A dark shadow has fallen upon our lands"
        ],
        "explanation": "Η απαγγελία του Terenas για το πεπρωμένο του γιου του να κυβερνήσει με σοφία και δικαιοσύνη έρχεται σε συγκλονιστική αντίθεση με τις εικόνες του Arthas να ξυπνά τον δράκο Sindragosa.",
        "funFacts": [
            "Το cinematic του Wrath of the Lich King θεωρείται ένα από τα σπουδαιότερα τρέιλερ κινουμένων σχεδίων στην ιστορία της βιομηχανίας.",
            "Η προειδοποίηση του Terenas 'No king rules forever' επαληθεύεται στο τέλος όταν ο Arthas πεθαίνει στα χέρια του πατέρα του."
        ],
        "source": "https://en.wikipedia.org/wiki/World_of_Warcraft:_Wrath_of_the_Lich_King",
        "tags": ["gaming", "world_of_warcraft", "blizzard", "arthas", "cinematics"]
    },
    {
        "id": "gaming_med_318",
        "text": "Ποια αμφιλεγόμενη λειτουργία συναλλαγών με πραγματικά χρήματα εισήγαγε η Blizzard στο 'Diablo III' (2012) και αναγκάστηκε να καταργήσει δύο χρόνια αργότερα;",
        "correct": "Real-Money Auction House (RMAH)",
        "distractors": ["Loot Boxes", "Battle Pass", "Pay-to-Win Gems"],
        "explanation": "Το Auction House επέτρεπε στους παίκτες να αγοράζουν και να πωλούν εξοπλισμό με πραγματικά δολάρια και ευρώ, καταστρέφοντας όμως τον βασικό ενθουσιασμό του κυνηγιού λαφύρων.",
        "funFacts": [
            "Ο διευθυντής του παιχνιδιού Josh Mosqueira έκλεισε οριστικά το Auction House με την κυκλοφορία του expansion 'Reaper of Souls' το 2014, σώζοντας τη φήμη του τίτλου.",
            "Το σύστημα 'Loot 2.0' που ακολούθησε έκανε τα αντικείμενα να πέφτουν προσαρμοσμένα στην κλάση του παίκτη (smart loot)."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_III",
        "tags": ["gaming", "diablo", "blizzard", "controversy", "arpg"]
    },
    {
        "id": "gaming_med_319",
        "text": "Ποιο είναι το όνομα της ναυαρχίδας Battlecruiser που χρησιμοποιεί ο Jim Raynor ως βάση επιχειρήσεων στο 'StarCraft II: Wings of Liberty' (2010);",
        "correct": "Hyperion",
        "distractors": ["Norad II", "Gantrithor", "Bucephalus"],
        "explanation": "Στο Hyperion, οι παίκτες μπορούν να επισκεφθούν τη γέφυρα, την καντίνα (με το jukebox και τα νέα της UNN), το οπλοστάσιο και το εργαστήριο του Stetmann μεταξύ αποστολών.",
        "funFacts": [
            "Ο πιστός φίλος και μηχανικός του Raynor στο Hyperion είναι ο Rory Swann.",
            "Το Hyperion είχε κλαπεί αρχικά από τον αυτοκράτορα Arcturus Mengsk κατά τη διάρκεια της επανάστασης των Sons of Korhal στο πρώτο παιχνίδι."
        ],
        "source": "https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty",
        "tags": ["gaming", "starcraft", "blizzard", "raynor", "rts"]
    },
    {
        "id": "gaming_med_320",
        "text": "Στο 'Dark Souls II' (2014), ποιος ήταν ο τραγικός βασιλιάς του Drangleic που κατέληξε ένα περιπλανώμενο, άμυαλο Hollow στον σκοτεινό τάφο του Undead Crypt;",
        "correct": "King Vendrick",
        "distractors": ["Lord Aldia", "Old Iron King", "Ivory King"],
        "explanation": "Ο Vendrick παραπλανήθηκε από τη σύζυγό του Nashandra (ένα κομμάτι του Manus), έκλεψε τη δύναμη των Γιγάντων και τελικά κλείδωσε τον εαυτό του στον τάφο για να μην παραδώσει την ψυχή του.",
        "funFacts": [
            "Η άμυνα του Vendrick στη μάχη είναι εξαιρετικά υψηλή και μειώνεται μόνο όσο περισσότερες ψυχές Γιγάντων (Souls of a Giant) κουβαλάει ο παίκτης στο inventory.",
            "Ο αδελφός του Vendrick, Aldia (Scholar of the First Sin), έγινε πλάσμα από φωτιά και ρίζες αναζητώντας διέξοδο από τον κύκλο της φωτιάς και του σκότους."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls_II",
        "tags": ["gaming", "dark_souls", "fromsoftware", "lore", "vendrick"]
    },
    {
        "id": "gaming_med_321",
        "text": "Στο 'Dark Souls III' (2016), ποιος ήταν ο μόνος Lord of Cinder που παρέμεινε οικειοθελώς στον θρόνο του στο Firelink Shrine;",
        "correct": "Ludleth of Courland",
        "distractors": ["Abyss Watchers", "Yhorm the Giant", "Aldrich, Devourer of Gods"],
        "explanation": "Ο Ludleth είναι ένας μικρόσωμος άντρας χωρίς πόδια που δέχεται πρόθυμα τη μοίρα του να καεί ξανά για να συντηρήσει τη φωτιά και μετατρέπει ψυχές αφεντικών σε όπλα (transposition).",
        "funFacts": [
            "Οι Abyss Watchers, εμπνευσμένοι από τον Artorias, κατέληξαν να σφαγιάζουν ο ένας τον άλλον αέναα λόγω της μόλυνσης από την Άβυσσο.",
            "Ο Yhorm the Giant μπορεί να νικηθεί ταχύτατα αν ο παίκτης χρησιμοποιήσει το ειδικό σπαθί ανέμου Storm Ruler."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls_III",
        "tags": ["gaming", "dark_souls", "fromsoftware", "ludleth", "bosses"]
    },
    {
        "id": "gaming_med_322",
        "text": "Ποια είναι η πανίσχυρη ημίθεος στο 'Elden Ring' που είναι γνωστή ως 'Blade of Miquella' και χρησιμοποιεί την καταστροφική κίνηση Waterfowl Dance;",
        "correct": "Malenia",
        "distractors": ["Ranni the Witch", "Marika", "Rennala"],
        "explanation": "Η Malenia πάσχει από τη سرخσήψη (Scarlet Rot) που κατέστρεψε τα άκρα της και ολόκληρη την περιοχή Caelid στη μονομαχία της με τον General Radahn.",
        "funFacts": [
            "Η φράση της 'I am Malenia, Blade of Miquella, and I have never known defeat' ακούστηκε αμέτρητες φορές από παίκτες που πέθαναν επανειλημμένα εναντίον της.",
            "Ένας θρυλικός παίκτης της κοινότητας με το ψευδώνυμο 'Let Me Solo Her' έγινε παγκόσμιο ίνδαλμα βοηθώντας χιλιάδες άλλους παίκτες να τη νικήσουν φορώντας μόνο ένα πιθάρι στο κεφάλι."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "tags": ["gaming", "elden_ring", "fromsoftware", "malenia", "bosses"]
    },
    {
        "id": "gaming_med_323",
        "text": "Στο 'Elden Ring', ποιος τερατώδης πολέμαρχος συγκρατεί τη μοίρα και τα αστέρια στον ουρανό με τη μαγεία της βαρύτητας παρά το ότι έχει τρελαθεί από το Scarlet Rot;",
        "correct": "Starscourge Radahn (Στρατηγός Ραντάν)",
        "distractors": ["Godrick the Grafted", "Rykkard", "Morgott"],
        "explanation": "Ο Στρατηγός Radahn ιππεύει το αγαπημένο του μικρό άλογο Leonard χρησιμοποιώντας βαρυτική μαγεία για να μην το πλακώνει το γιγάντιο βάρος του.",
        "funFacts": [
            "Η μάχη εναντίον του στο Redmane Castle έχει τη μορφή φεστιβάλ (Radahn Festival) όπου ο παίκτης μπορεί να καλέσει ταυτόχρονα δεκάδες NPCs στη μάχη.",
            "Στη δεύτερη φάση της μάχης, ο Radahn εκτοξεύεται στην ατμόσφαιρα και πέφτει πίσω στο πεδίο σαν φλεγόμενος μετεωρίτης."
        ],
        "source": "https://en.wikipedia.org/wiki/Elden_Ring",
        "tags": ["gaming", "elden_ring", "fromsoftware", "radahn", "bosses"]
    },
    {
        "id": "gaming_med_324",
        "text": "Στο 'Demon's Souls' (2009) του PS3, ποια τυφλή γυναίκα με κερί στα χέρια λέει τη φράση 'Soul of the mind, key to life's ether' για να αναβαθμίσει τον ήρωα;",
        "correct": "Maiden in Black (Η Κόρη στα Μαύρα)",
        "distractors": ["The Doll", "Fire Keeper", "Emerald Herald"],
        "explanation": "Η Maiden in Black κατοικεί στο Nexus και καθοδηγεί τον Slayer of Demons, κρατώντας τα μάτια της καλυμμένα με σκληρυμένο κερί.",
        "funFacts": [
            "Το Demon's Souls θεωρήθηκε αρχικά αποτυχία από τη Sony και ο Shuhei Yoshida το χαρακτήρισε 'απίστευτα κακό παιχνίδι' πριν η επιτυχία από στόμα σε στόμα το κάνει cult κλασικό.",
            "Το 2020 κυκλοφόρησε ένα εκπληκτικό οπτικό remake του Demon's Souls από την Bluepoint Games για το λανσάρισμα του PlayStation 5."
        ],
        "source": "https://en.wikipedia.org/wiki/Demon%27s_Souls",
        "tags": ["gaming", "demons_souls", "fromsoftware", "playstation", "soulsborne"]
    },
    {
        "id": "gaming_med_325",
        "text": "Στο 'Final Fantasy IV' (1991), σε ποιο ιερό βουνό ανεβαίνει ο Cecil Harvey για να απαλλαγεί από τη σκοτεινή του φύση και να γίνει Paladin;",
        "correct": "Mt. Ordeals (Όρος των Δοκιμασιών)",
        "distractors": ["Mt. Gulg", "Mt. Hobs", "Mt. Gagazet"],
        "explanation": "Στην κορυφή του Mt. Ordeals, ο Cecil αντιμετωπίζει σε μονομαχία την ίδια του τη σκοτεινή αντανάκλαση και αρνούμενος να επιτεθεί ολοκληρώνει τη μεταμόρφωσή του σε Ιππότη του Φωτός.",
        "funFacts": [
            "Όταν ο Cecil γίνεται Paladin, το επίπεδό του (Level) επανέρχεται προσωρινά στο 1, αλλά αποκτά λευκή μαγεία και ικανότητα προστασίας των αδύναμων συμπαικτών.",
            "Το Final Fantasy IV ήταν το πρώτο παιχνίδι της σειράς που χρησιμοποίησε το πρωτοποριακό σύστημα Active Time Battle (ATB) του Hiroyuki Ito."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_IV",
        "tags": ["gaming", "final_fantasy", "square", "snes", "cecil"]
    },
    {
        "id": "gaming_med_326",
        "text": "Ποιος Ιάπωνας παραγωγός και σκηνοθέτης ανέλαβε το καταστροφικό λανσάρισμα του 'Final Fantasy XIV' και το αναγέννησε ως το τεράστιο MMO 'A Realm Reborn';",
        "correct": "Naoki Yoshida (Yoshi-P)",
        "distractors": ["Tetsuya Nomura", "Hajime Tabata", "Motomu Toriyama"],
        "explanation": "Ο Yoshi-P αποφάσισε να καταστρέψει κυριολεκτικά τον παλιό κόσμο με έναν μετεωρίτη στο παιχνίδι (Seventh Umbral Calamity) και να ξαναχτίσει ολόκληρη τη μηχανή και το gameplay από το μηδέν.",
        "funFacts": [
            "Το Final Fantasy XIV ξεπέρασε σε ενεργούς συνδρομητές το World of Warcraft κατά τη διάρκεια της επέκτασης Endwalker (2021).",
            "Ο Yoshida είναι τόσο αγαπητός στους παίκτες που συχνά συγκινείται μέχρι δακρύων στις ζωντανές παρουσιάσεις των επεκτάσεων (Fan Festivals)."
        ],
        "source": "https://en.wikipedia.org/wiki/Naoki_Yoshida",
        "tags": ["gaming", "final_fantasy", "square_enix", "mmorpg", "yoshida"]
    },
    {
        "id": "gaming_med_327",
        "text": "Στο 'The Legend of Zelda: Twilight Princess' (2006), σε ποιο ζώο μεταμορφώνεται ο Link όταν εισέρχεται στο βασίλειο του Λυκόφωτος (Twilight Realm);",
        "correct": "Σε λύκο (Wolf Link)",
        "distractors": ["Σε κουνέλι", "Σε αετό", "Σε πάνθηρα"],
        "explanation": "Ο Link αποκτά τη μορφή λύκου με ενισχυμένες αισθήσεις όσφρησης και τη σκανταλιάρα imp Midna καβάλα στην πλάτη του.",
        "funFacts": [
            "Στο A Link to the Past στο SNES, ο Link μεταμορφωνόταν σε ένα ανυπεράσπιστο ροζ κουνελάκι όταν έμπαινε στον Σκοτεινό Κόσμο (Dark World).",
            "Η Midna αποκαλύπτεται στο τέλος ότι είναι η νόμιμη πριγκίπισσα της φυλής Twili στην πραγματική της ανθρώπινη μορφή."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Twilight_Princess",
        "tags": ["gaming", "zelda", "twilight_princess", "nintendo", "midna"]
    },
    {
        "id": "gaming_med_328",
        "text": "Ποια είναι η κοσμική προστάτιδα των αστεριών Lumas και φύλακας του Comet Observatory στο 'Super Mario Galaxy' (2007) του Wii;",
        "correct": "Rosalina (Ροζαλίνα)",
        "distractors": ["Pauline", "Princess Daisy", "Queen Merelda"],
        "explanation": "Η Rosalina ταξιδεύει στο σύμπαν με το παρατηρητήριο κομητών και διαβάζει στον Mario ένα πανέμορφο, μελαγχολικό παραμύθι για την παιδική της ηλικία και τη μητέρα της.",
        "funFacts": [
            "Το Super Mario Galaxy είναι ένα από τα παιχνίδια με την υψηλότερη βαθμολογία όλων των εποχών, με μέσο όρο 97% στο Metacritic.",
            "Η ορχηστρική μουσική του παιχνιδιού ηχογραφήθηκε από ζωντανή συμφωνική ορχήστρα 50 οργάνων υπό τη διεύθυνση του Mahito Yokota."
        ],
        "source": "https://en.wikipedia.org/wiki/Rosalina_(Mario)",
        "tags": ["gaming", "mario", "nintendo", "galaxy", "rosalina"]
    },
    {
        "id": "gaming_med_329",
        "text": "Στο 'Super Mario Sunshine' (2002) στο GameCube, ποια συσκευή αντλίας νερού κουβαλάει ο Mario στην πλάτη του για να καθαρίζει το Isle Delfino;",
        "correct": "F.L.U.D.D. (Flash Liquidizer Ultra Dousing Device)",
        "distractors": ["Poltergust 3000", "Hydro Cannon", "Aqua Jet"],
        "explanation": "Το FLUDD εφευρέθηκε από τον καθηγητή E. Gadd και επιτρέπει στον Mario να ψεκάζει νερό, να αιωρείται στον αέρα (Hover Nozzle) και να εκτοξεύεται σαν πύραυλος (Rocket Nozzle).",
        "funFacts": [
            "Ο Bowser Jr. εμφανίζεται για πρώτη φορά σε αυτό το παιχνίδι μεταμφιεσμένος σε Shadow Mario χρησιμοποιώντας μια μαγική πινελιά.",
            "Το FLUDD διαθέτει τεχνητή νοημοσύνη και μιλάει με φιλική ρομποτική φωνή καθοδηγώντας τον Mario."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_Sunshine",
        "tags": ["gaming", "mario", "nintendo", "gamecube", "fludd"]
    },
    {
        "id": "gaming_med_330",
        "text": "Στο 'Metroid Fusion' (2002) στο Game Boy Advance, ποιος εφιαλτικός εχθρός κυνηγάει τη Samus, αποτελώντας ένα πανομοιότυπο κλώνο της με την πλήρη της δύναμη;",
        "correct": "SA-X",
        "distractors": ["Dark Samus", "Phantoon", "Mother Brain"],
        "explanation": "Το παράσιτο X μόλυνε την αρχική στολή της Samus και δημιούργησε το SA-X, το οποίο διαθέτει όλες τις μέγιστες αναβαθμίσεις (Ice Beam, Super Missiles) αναγκάζοντας την αποδυναμωμένη Samus να κρύβεται.",
        "funFacts": [
            "Οι στιγμές όπου η Samus κρύβεται πίσω από τοίχους ακούγοντας τα βαριά μεταλλικά βήματα του SA-X έφεραν στοιχεία καθαρού survival horror στη σειρά Metroid.",
            "Η Samus σώθηκε από τη μόλυνση των X χαρίς σε ένα εμβόλιο φτιαγμένο από κύτταρα του τελευταίου μωρού Metroid."
        ],
        "source": "https://en.wikipedia.org/wiki/Metroid_Fusion",
        "tags": ["gaming", "metroid", "nintendo", "gba", "samus_aran"]
    },
    {
        "id": "gaming_med_331",
        "text": "Ποιο ισπανικό στούντιο ανάπτυξης δημιούργησε σε συνεργασία με τη Nintendo τα 'Metroid: Samus Returns' (3DS) και 'Metroid Dread' (Switch);",
        "correct": "MercurySteam",
        "distractors": ["Next Level Games", "WayForward", "PlatinumGames"],
        "explanation": "Η MercurySteam ανέπτυξε το Metroid Dread (2021), το οποίο ολοκλήρωσε τη βασική ιστορία 5 μερών του 2D Metroid που ξεκίνησε το 1986.",
        "funFacts": [
            "Τα ανίκητα ρομπότ έρευνας E.M.M.I. περιπολούν σε ειδικές ζώνες και μπορούν να εξοντώσουν τη Samus ακαριαία αν την πιάσουν.",
            "Το Metroid Dread σχεδιαζόταν αρχικά για το Nintendo DS στα μέσα της δεκαετίας του 2000 αλλά είχε ακυρωθεί λόγω τεχνικών περιορισμών."
        ],
        "source": "https://en.wikipedia.org/wiki/Metroid_Dread",
        "tags": ["gaming", "metroid", "mercurysteam", "nintendo", "switch"]
    },
    {
        "id": "gaming_med_332",
        "text": "Ποιος είναι ο συνθέτης της Rare που έγραψε το θρυλικό 'DK Rap' για την εισαγωγή του 'Donkey Kong 64' (1999);",
        "correct": "Grant Kirkhope",
        "distractors": ["David Wise", "Robin Beanland", "Koji Kondo"],
        "explanation": "Ο Grant Kirkhope έγραψε το DK Rap ως μια αστεία, αυτοσαρκαστική εισαγωγή παρουσίασης των πέντε Kongs, η οποία έγινε ένα από τα πιο διάσημα μουσικά κομμάτια του Nintendo 64.",
        "funFacts": [
            "Ο Kirkhope συνέθεσε επίσης τη μουσική των Banjo-Kazooie, GoldenEye 007 και Mario + Rabbids Kingdom Battle.",
            "Ο στίχος 'He has no style, he has no grace, this Kong has a funny face' αναφέρεται στον Lanky Kong."
        ],
        "source": "https://en.wikipedia.org/wiki/DK_Rap",
        "tags": ["gaming", "donkey_kong", "rare", "grant_kirkhope", "music"]
    },
    {
        "id": "gaming_med_333",
        "text": "Ποιος χαρακτήρας στο multiplayer του 'GoldenEye 007' (1997) στο Nintendo 64 απαγορευόταν άτυπα μεταξύ φίλων λόγω του υπερβολικά κοντού του αναστήματος;",
        "correct": "Oddjob",
        "distractors": ["Jaws", "Baron Samedi", "Boris Grishenko"],
        "explanation": "Ο Oddjob ήταν τόσο κοντός που η αυτόματη στόχευση των όπλων αστοχούσε περνώντας πάνω από το κεφάλι του, δίνοντας αθέμιτο πλεονέκτημα σε όποιον τον επέλεγε.",
        "funFacts": [
            "Οι προγραμματιστές της Rare παραδέχτηκαν αργότερα σε συνεντεύξεις ότι ο Oddjob ήταν όντως αθέμιτα ισχυρός (cheating).",
            "Το multiplayer mode του GoldenEye προστέθηκε κρυφά τους τελευταίους μήνες της ανάπτυξης από έναν μόνο προγραμματιστή (Steve Ellis) χωρίς επίσημη έγκριση."
        ],
        "source": "https://en.wikipedia.org/wiki/GoldenEye_007_(1997_video_game)",
        "tags": ["gaming", "goldeneye_007", "rare", "n64", "multiplayer"]
    },
    {
        "id": "gaming_med_334",
        "text": "Ποιο είναι το αμφιλεγόμενο, αυστηρά ακατάλληλο για ανηλίκους platformer της Rare (2001) με πρωταγωνιστή έναν μεθυσμένο σκίουρο;",
        "correct": "Conker's Bad Fur Day",
        "distractors": ["Banjo-Kazooie", "Gex: Enter the Gecko", "Earthworm Jim"],
        "explanation": "Το Conker's Bad Fur Day ξεκίνησε ως χαριτωμένο παιδικό παιχνίδι αλλά μετατράπηκε σε παρωδία γεμάτη αλκοόλ, βωμολοχίες και σινεφίλ αναφορές (Matrix, Saving Private Ryan).",
        "funFacts": [
            "Το πιο διάσημο αφεντικό του παιχνιδιού είναι το 'The Great Mighty Poo', ένα γιγάντιο βουνό περιττωμάτων που τραγουδάει άριες όπερας πετώντας κόπρανα.",
            "Η Nintendo δίστασε τόσο πολύ να διαφημίσει το παιχνίδι που περιόρισε το μάρκετινγκ σε περιοδικά όπως το Playboy."
        ],
        "source": "https://en.wikipedia.org/wiki/Conker%27s_Bad_Fur_Day",
        "tags": ["gaming", "conker", "rare", "n64", "retro"]
    },
    {
        "id": "gaming_med_335",
        "text": "Στο πρωτοποριακό ανοιχτό παιχνίδι 'Shenmue' (1999) του Yu Suzuki στο Dreamcast, ποιον αναζητά ο Ryo Hazuki στην πόλη Yokosuka για να εκδικηθεί τον φόνο του πατέρα του;",
        "correct": "Lan Di",
        "distractors": ["Goro Majima", "Heihachi Mishima", "Lao Gui"],
        "explanation": "Ο Ryo αναζητά τον Κινέζο πολέμαρχο Lan Di που σκότωσε τον πατέρα του Iwao και έκλεψε τον μυστηριώδη καθρέφτη Dragon Mirror.",
        "funFacts": [
            "Το Shenmue κόστισε πάνω από 47 εκατομμύρια δολάρια, αποτελώντας το πιο ακριβό βιντεοπαιχνίδι που είχε παραχθεί μέχρι τότε.",
            "Εισήγαγε τον όρο Quick Time Events (QTE) και διέθετε πλήρη προσομοίωση καιρού, ρουτίνας για κάθε NPC και λειτουργικά arcade της Sega."
        ],
        "source": "https://en.wikipedia.org/wiki/Shenmue_(video_game)",
        "tags": ["gaming", "shenmue", "sega", "dreamcast", "yu_suzuki"]
    },
    {
        "id": "gaming_med_336",
        "text": "Ποιος είναι ο εμβληματικός πρωταγωνιστής της σειράς 'Yakuza' (Like a Dragon), γνωστός ως ο 'Δράκος της Dojima' (Dragon of Dojima);",
        "correct": "Kazuma Kiryu",
        "distractors": ["Goro Majima", "Ichiban Kasuga", "Taiga Saejima"],
        "explanation": "Ο Kiryu είναι ένας έντιμος μαφιόζος της Yakuza με τατουάζ δράκου στην πλάτη που προσπαθεί διαρκώς να προστατεύσει την υιοθετημένη του κόρη Haruka στη συνοικία Kamurocho.",
        "funFacts": [
            "Ο αιώνιος αντίζηλος και φίλος του Goro Majima έχει το παρατσούκλι 'The Mad Dog of Shimano' και φοράει δερμάτινο σακάκι φιδιού και κάλυμμα ματιού.",
            "Στο 'Yakuza: Like a Dragon' (2020), ο νέος πρωταγωνιστής Ichiban Kasuga βλέπει τον κόσμο σαν turn-based RPG επειδή λατρεύει το Dragon Quest."
        ],
        "source": "https://en.wikipedia.org/wiki/Kazuma_Kiryu",
        "tags": ["gaming", "yakuza", "sega", "kiryu", "action"]
    },
    {
        "id": "gaming_med_337",
        "text": "Ποιο μοναδικό οπτικό στυλ καθιέρωσε το 'Jet Set Radio' (2000) της Sega στο Dreamcast, κάνοντας το 3D παιχνίδι να μοιάζει με ζωντανό κόμικ;",
        "correct": "Cel-shading (Κελ-σέιντινγκ)",
        "distractors": ["Pixel art", "Ray tracing", "Voxel graphics"],
        "explanation": "Το Jet Set Radio ήταν το πρώτο παιχνίδι που έκανε ευρέως γνωστή την τεχνική cel-shading, χρησιμοποιώντας έντονα μαύρα περιγράμματα και επίπεδες χρωματικές διαβαθμίσεις.",
        "funFacts": [
            "Οι παίκτες κάνουν πατινάζ με μαγνητικά inline skates στους δρόμους του Tokyo-to ψεκάζοντας γκράφιτι και αποφεύγοντας τον αρχηγό της αστυνομίας Captain Onishima.",
            "Το εκρηκτικό soundtrack συντέθηκε από τον Hideki Naganuma συνδυάζοντας funk, hip-hop και J-pop."
        ],
        "source": "https://en.wikipedia.org/wiki/Jet_Set_Radio",
        "tags": ["gaming", "jet_set_radio", "sega", "dreamcast", "art_style"]
    },
    {
        "id": "gaming_med_338",
        "text": "Στο arcade racing παιχνίδι 'Crazy Taxi' (1999) της Sega, ποια διάσημα punk rock συγκροτήματα κυριαρχούσαν στο αυθεντικό soundtrack;",
        "correct": "The Offspring και Bad Religion",
        "distractors": ["Green Day και Blink-182", "Red Hot Chili Peppers και Nirvana", "Sum 41 και Linkin Park"],
        "explanation": "Τραγούδια όπως το 'All I Want' των The Offspring και το 'Ten in 2010' των Bad Religion ταυτίστηκαν απόλυτα με το ταχύτατο gameplay παράδοσης επιβατών.",
        "funFacts": [
            "Οι τέσσερις οδηγοί ταξί που μπορεί να επιλέξει ο παίκτης είναι οι Axel, B.D. Joe, Gena και Gus.",
            "Το παιχνίδι περιλάμβανε πραγματικούς εμπορικούς προορισμούς, όπως καταστήματα Pizza Hut, KFC, Levi's και Tower Records."
        ],
        "source": "https://en.wikipedia.org/wiki/Crazy_Taxi_(video_game)",
        "tags": ["gaming", "crazy_taxi", "sega", "arcade", "music"]
    },
    {
        "id": "gaming_med_339",
        "text": "Στο 'Resident Evil – Code: Veronica' (2000), σε ποιο απομονωμένο νησί-φυλακή της Umbrella Corporation ξεκινά η περιπέτεια της Claire Redfield;",
        "correct": "Rockfort Island",
        "distractors": ["Sheena Island", "Raccoon Island", "Sushestvovanie Island"],
        "explanation": "Η Claire φυλακίζεται στο Rockfort Island, το οποίο διοικείται από τον ψυχικά διαταραγμένο Alfred Ashford και την αδελφή του Alexia.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε αρχικά για το Sega Dreamcast και ήταν το πρώτο Resident Evil με πλήρως πολυγωνικά 3D περιβάλλοντα αντί για προ-σχεδιασμένα στατικά φόντα.",
            "Η Alexia Ashford δημιούργησε τον ιό T-Veronica συνδυάζοντας τον ιό Progenitor με DNA αρχαίων μυρμηγκιών."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_%E2%80%93_Code:_Veronica",
        "tags": ["gaming", "resident_evil", "capcom", "claire_redfield", "dreamcast"]
    },
    {
        "id": "gaming_med_340",
        "text": "Ποια επιβλητική γυναίκα βαμπίρ ύψους 2,9 μέτρων στο 'Resident Evil Village' (2021) έγινε παγκόσμιο φαινόμενο στο διαδίκτυο πριν καν κυκλοφορήσει το παιχνίδι;",
        "correct": "Lady Alcina Dimitrescu",
        "distractors": ["Mother Miranda", "Donna Beneviento", "Salvatore Moreau"],
        "explanation": "Η Lady Dimitrescu ζει στο γοτθικό της κάστρο στη Ρουμανία μαζί με τις τρεις κόρες της (Bela, Cassandra, Daniela) και καταδιώκει τον Ethan Winters.",
        "funFacts": [
            "Η ηθοποιός Maggie Robertson που χάρισε τη φωνή και την ερμηνεία motion capture στη Lady Dimitrescu κέρδισε το βραβείο Best Performance στα The Game Awards 2021.",
            "Η επίσημη επιβεβαίωση του ύψους της στα 2,9 μέτρα (9 πόδια και 6 ίντσες) έγινε από τον ίδιο τον καλλιτεχνικό διευθυντή Tomonori Takano."
        ],
        "source": "https://en.wikipedia.org/wiki/Lady_Dimitrescu",
        "tags": ["gaming", "resident_evil", "capcom", "lady_dimitrescu"]
    },
    {
        "id": "gaming_med_341",
        "text": "Στο 'Silent Hill 4: The Room' (2004), ποιο είναι το νούμερο του διαμερίσματος στο οποίο βρίσκεται μυστηριωδώς κλειδωμένος από μέσα ο Henry Townshend;",
        "correct": "Διαμέρισμα 302 (Room 302)",
        "distractors": ["Διαμέρισμα 204", "Διαμέρισμα 101", "Διαμέρισμα 404"],
        "explanation": "Ο Henry δεν μπορεί να ανοίξει την εξώπορτα που είναι αλυσοδεμένη από μέσα και η μόνη του διαφυγή είναι μια παράξενη τρύπα στον τοίχο του μπάνιου.",
        "funFacts": [
            "Ο κατά συρροή δολοφόνος Walter Sullivan θεωρεί το διαμέρισμα 302 ως τη βιολογική του μητέρα και προσπαθεί να ολοκληρώσει το τελετουργικό των 21 Sacraments.",
            "Το παιχνίδι χρησιμοποιεί οπτική πρώτου προσώπου (first-person) μέσα στο διαμέρισμα και τρίτου προσώπου στους εφιαλτικούς άλλους κόσμους."
        ],
        "source": "https://en.wikipedia.org/wiki/Silent_Hill_4:_The_Room",
        "tags": ["gaming", "silent_hill", "konami", "survival_horror"]
    },
    {
        "id": "gaming_med_342",
        "text": "Στο 'Castlevania: Aria of Sorrow' (2003) στο Game Boy Advance, ποια μοναδική ικανότητα διαθέτει ο νεαρός μαθητής Soma Cruz;",
        "correct": "Την ικανότητα να απορροφά και να χρησιμοποιεί τις ψυχές των εχθρών (Tactical Soul)",
        "distractors": ["Την ικανότητα να χειρίζεται το ιερό μαστίγιο Belmont", "Την ικανότητα να σταματά τον χρόνο με μαγικό ρολόι", "Την ικανότητα να καλεί αγγέλους"],
        "explanation": "Ο Soma Cruz ανακαλύπτει ότι κάθε τέρας που σκοτώνει μπορεί να αφήσει πίσω του την ψυχή του, δίνοντάς του νέες επιθέσεις, ασπίδες ή παθητικές ικανότητες.",
        "funFacts": [
            "Στο τέλος του παιχνιδιού αποκαλύπτεται η συγκλονιστική αλήθεια ότι ο ίδιος ο Soma είναι η μετενσάρκωση του ίδιου του Κόμη Δράκουλα.",
            "Το Aria of Sorrow διαδραματίζεται στο μέλλον, το έτος 2035, μέσα σε μια ολική έκλειψη ηλίου στην Ιαπωνία."
        ],
        "source": "https://en.wikipedia.org/wiki/Castlevania:_Aria_of_Sorrow",
        "tags": ["gaming", "castlevania", "konami", "gba", "metroidvania"]
    },
    {
        "id": "gaming_med_343",
        "text": "Ποια είναι η πιο διάσημη ιαχή που φωνάζει ο δικηγόρος Phoenix Wright χτυπώντας το γραφείο του όταν εντοπίζει αντίφαση σε κατάθεση μάρτυρα;",
        "correct": "OBJECTION! (Ένσταση!)",
        "distractors": ["HOLD IT!", "TAKE THAT!", "GUILTY!"],
        "explanation": "Το 'OBJECTION!' εμφανίζεται με τεράστια κόκκινα γράμματα και τον Phoenix να δείχνει εμφατικά με το δάχτυλο τον μάρτυρα, συνοδευόμενο από δραματική μουσική.",
        "funFacts": [
            "Ο δημιουργός της σειράς Shu Takumi δάνεισε τη δική του φωνή για το ιαπωνικό 'Igiari!' (Objection) στα πρώτα παιχνίδια του Game Boy Advance.",
            "Ο αντίπαλος εισαγγελέας και παιδικός φίλος του Phoenix είναι ο Miles Edgeworth."
        ],
        "source": "https://en.wikipedia.org/wiki/Phoenix_Wright",
        "tags": ["gaming", "ace_attorney", "capcom", "phoenix_wright"]
    },
    {
        "id": "gaming_med_344",
        "text": "Ποιο είναι το όνομα του σαδιστή μηχανικού αρκούδου με τη διχρωμία (μισός λευκός, μισός μαύρος) που διευθύνει τα θανατηφόρα παιχνίδια στο 'Danganronpa';",
        "correct": "Monokuma",
        "distractors": ["Kuma", "Teddie", "Freddy Fazbear"],
        "explanation": "Ο Monokuma αυτοανακηρύσσεται διευθυντής της Ακαδημίας Hope's Peak και αναγκάζει τους μαθητές να δολοφονήσουν έναν συμμαθητή τους χωρίς να πιαστούν στις δίκες (Class Trials).",
        "funFacts": [
            "Το χαρακτηριστικό γέλιο του Monokuma είναι: 'Upupupu!'.",
            "Αν οι μαθητές ψηφίσουν λάθος ένοχο στη δίκη, εκτελούνται όλοι εκτός από τον πραγματικό δολοφόνο που κερδίζει την ελευθερία του."
        ],
        "source": "https://en.wikipedia.org/wiki/Danganronpa",
        "tags": ["gaming", "danganronpa", "spike_chunsoft", "visual_novel", "monokuma"]
    },
    {
        "id": "gaming_med_345",
        "text": "Στο αριστούργημα στρατηγικής 'Civilization' του Sid Meier, ποιος ιστορικός ηγέτης έγινε διαβόητος για την τάση του να εξαπολύει ξαφνικά πυρηνικές επιθέσεις λόγω ενός αρχικού bug;",
        "correct": "Μαχάτμα Γκάντι (Mahatma Gandhi)",
        "distractors": ["Ιωσήφ Στάλιν", "Μέγας Αλέξανδρος", "Ιούλιος Καίσαρας"],
        "explanation": "Στο πρώτο Civilization, η επιθετικότητα του Γκάντι ήταν στο κατώτατο όριο (1)· όταν όμως υιοθετούσε Δημοκρατία που μείωνε την επιθετικότητα κατά 2, προκαλούνταν υπερχείλιση ακεραίου (underflow) ανεβάζοντάς την στο μέγιστο (255)!",
        "funFacts": [
            "Ο μύθος του 'Nuclear Gandhi' έγινε τόσο αγαπητός στους παίκτες που οι δημιουργοί τον ενσωμάτωσαν σκόπιμα ως επίσημο easter egg σε όλα τα επόμενα Civilization.",
            "Το μότο του Sid Meier για τον σχεδιασμό παιχνιδιών είναι: 'A game is a series of interesting decisions'."
        ],
        "source": "https://en.wikipedia.org/wiki/Nuclear_Gandhi",
        "tags": ["gaming", "civilization", "sid_meier", "memes", "strategy"]
    },
    {
        "id": "gaming_med_346",
        "text": "Ποιο είναι το όνομα του κυβερνο-νίντζα με το εξωσκελετικό κράνος και τη στολή υψηλής συχνότητας που πρωτοεμφανίστηκε ως αντίπαλος και σύμμαχος στο 'Metal Gear Solid';",
        "correct": "Gray Fox (Frank Jaeger)",
        "distractors": ["Raiden", "Solidus Snake", "Vamp"],
        "explanation": "Ο Frank Jaeger, ο μόνος στρατιώτης που έλαβε τον τίτλο 'Fox' στη μονάδα FOXHOUND, αναστήθηκε ως κυβερνοπολεμιστής οπλισμένος με σπαθί υψηλής συχνότητας (HF Blade).",
        "funFacts": [
            "Στη δραματική αναμέτρηση με το Metal Gear REX, ο Gray Fox συνθλίβεται από το πόδι του ρομπότ λέγοντας στον Snake: 'We're not tools of the government, or anyone else. Fighting was the only thing I was good at...'.",
            "Η κραυγή του 'Hurt me more!' κατά τη μάχη σώμα με σώμα με τον Snake έδειχνε την απελπισμένη του ανάγκη να νιώσει ξανά ζωντανός."
        ],
        "source": "https://en.wikipedia.org/wiki/Gray_Fox_(Metal_Gear)",
        "tags": ["gaming", "metal_gear_solid", "konami", "hideo_kojima", "characters"]
    },
    {
        "id": "gaming_med_347",
        "text": "Στο 'Chrono Trigger', ποιος υπερμεγέθης εξωγήινος παρασιτικός οργανισμός κοιμάται στα βάθη της Γης από την προϊστορία και ξυπνά το 1999 μ.Χ. καταστρέφοντας τον κόσμο;",
        "correct": "Lavos",
        "distractors": ["Jenova", "Sin", "Zanza"],
        "explanation": "Ο Lavos έπεσε στη Γη ως μετεωρίτης στην προϊστορική εποχή (65.000.000 π.Χ.) και απομυζά σταδιακά την ενέργεια του πλανήτη μέχρι την Ημέρα του Lavos το 1999 μ.Χ.",
        "funFacts": [
            "Η ομάδα του Crono ταξιδεύει στον χρόνο με τη χρονομηχανή Epoch για να προλάβει και να αλλάξει τη μοίρα της ανθρωπότητας.",
            "Το όνομα 'Lavos' σημαίνει στη γλώσσα των προϊστορικών ανθρώπων 'Μεγάλη Φωτιά' (La = φωτιά, Vos = μεγάλο)."
        ],
        "source": "https://en.wikipedia.org/wiki/Chrono_Trigger",
        "tags": ["gaming", "chrono_trigger", "square", "lavos", "rpg"]
    },
    {
        "id": "gaming_med_348",
        "text": "Στο 'The Witcher 3', ποιο αγαπημένο μίνι παιχνίδι καρτών των ταβερνών έγινε τόσο δημοφιλές ώστε κυκλοφόρησε αργότερα ως αυτόνομο παιχνίδι από την CD Projekt Red;",
        "correct": "Gwent",
        "distractors": ["Dice Poker", "Pazaak", "Caravan"],
        "explanation": "Το Gwent προσομοιώνει μια μάχη στρατών σε τρεις σειρές (Melee, Ranged, Siege) όπου οι παίκτες πρέπει να κερδίσουν δύο από τους τρεις γύρους.",
        "funFacts": [
            "Ο Geralt μπορεί να ρωτήσει σχεδόν οποιονδήποτε έμπορο ή χωρικό αν θέλει να παίξει Gwent, ακόμη και εν μέσω τραγικών ή επειγουσών καταστάσεων.",
            "Το παιχνίδι αναπτύχθηκε αρχικά μέσα σε ένα σαββατοκύριακο από δύο σχεδιαστές της CD Projekt Red (Damien Monnier και Rafał Jaki)."
        ],
        "source": "https://en.wikipedia.org/wiki/Gwent:_The_Witcher_Card_Game",
        "tags": ["gaming", "the_witcher", "cd_projekt_red", "gwent", "card_game"]
    },
    {
        "id": "gaming_med_349",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο 'BioShock 2' (2010), ενός αρχικού πρωτότυπου Big Daddy της σειράς Alpha που επανασυνδέεται με τη Little Sister του;",
        "correct": "Subject Delta",
        "distractors": ["Subject Sigma", "Subject Omega", "Jack"],
        "explanation": "Ο Subject Delta είναι συνδεδεμένος ψυχολογικά με την Eleanor Lamb και ξυπνά δέκα χρόνια μετά τα γεγονότα του πρώτου BioShock για να τη βρει στην παρακμάζουσα Rapture.",
        "funFacts": [
            "Σε αντίθεση με τους κανονικούς Big Daddies, ο Subject Delta μπορεί να χειρίζεται όπλα στο ένα χέρι και Plasmids στο άλλο ταυτόχρονα.",
            "Οι Big Sisters είναι μεγαλωμένες Little Sisters που κινούνται με απίστευτη ταχύτητα και ευκινησία."
        ],
        "source": "https://en.wikipedia.org/wiki/BioShock_2",
        "tags": ["gaming", "bioshock", "2k_games", "fps"]
    },
    {
        "id": "gaming_med_350",
        "text": "Στο 'Resident Evil Village' (2021), ποιος άρχοντας ελέγχει ένα τεράστιο υπόγειο εργοστάσιο κυβερνο-μεταλλαγμένων και διαθέτει μαγνητικές δυνάμεις;",
        "correct": "Karl Heisenberg",
        "distractors": ["Salvatore Moreau", "Donna Beneviento", "Urias"],
        "explanation": "Ο Heisenberg μισεί τη Mother Miranda και προτείνει στον Ethan Winters να συμμαχήσουν χρησιμοποιώντας τη μικρή Rose για να την καταστρέψουν.",
        "funFacts": [
            "Ο Heisenberg χειρίζεται ένα τεράστιο μηχανικό σφυρί και μπορεί να αιωρεί μέταλλα όπως ο Magneto των X-Men.",
            "Ο Ethan μάχεται ενάντια στον μεταλλαγμένο Heisenberg οδηγώντας ένα αυτοσχέδιο τανκ κατασκευασμένο από τον Chris Redfield."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_Village",
        "tags": ["gaming", "resident_evil", "capcom", "heisenberg"]
    },
    {
        "id": "gaming_med_351",
        "text": "Ποιοι είναι οι τρεις μαθητευόμενοι Keyblade Masters που πρωταγωνιστούν στο πρίκουελ 'Kingdom Hearts Birth by Sleep' (2010) στο PSP;",
        "correct": "Terra, Ventus και Aqua",
        "distractors": ["Sora, Riku και Kairi", "Roxas, Axel και Xion", "Hayner, Pence και Olette"],
        "explanation": "Οι τρεις φίλοι εκπαιδεύονται υπό τον Master Eraqus στο Land of Departure, αλλά πέφτουν θύματα των σκοτεινών σχεδίων του Master Xehanort.",
        "funFacts": [
            "Η Aqua είναι η μόνη από τους τρεις που περνάει επιτυχώς τις εξετάσεις Mark of Mastery στην αρχή του παιχνιδιού.",
            "Η καρδιά του Ventus καταφεύγει στο τέλος μέσα στο σώμα του νεαρού Sora για να αναρρώσει, εξηγώντας γιατί ο Roxas μοιάζει εμφανισιακά στον Ventus."
        ],
        "source": "https://en.wikipedia.org/wiki/Kingdom_Hearts_Birth_by_Sleep",
        "tags": ["gaming", "kingdom_hearts", "square_enix", "psp"]
    },
    {
        "id": "gaming_med_352",
        "text": "Στο 'Dragon Quest VIII: Journey of the Cursed King' (2004), ποιος αυλικός γελωτοποιός κλέβει το μαγικό σκήπτρο και καταριέται το κάστρο Trodain;",
        "correct": "Dhoulmagus",
        "distractors": ["Rhapthorne", "Marcello", "Keeleon"],
        "explanation": "Ο Dhoulmagus μεταμορφώνει τον βασιλιά Trode σε πράσινο τερατάκι και την πριγκίπισσα Medea σε λευκό άλογο, ξεκινώντας το ταξίδι του σιωπηλού ήρωα.",
        "funFacts": [
            "Το παιχνίδι σχεδιάστηκε από την Level-5 και ήταν το πρώτο Dragon Quest με πλήρως τρισδιάστατα cel-shaded γραφικά.",
            "Στη δυτική έκδοση του PS2, η Square Enix συμπεριέλαβε ορχηστρικό soundtrack και πλήρη αγγλική μεταγλώττιση, καθώς και ένα demo δισκάκι του Final Fantasy XII."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon_Quest_VIII:_Journey_of_the_Cursed_King",
        "tags": ["gaming", "dragon_quest", "square_enix", "level_5", "rpg"]
    },
    {
        "id": "gaming_med_353",
        "text": "Στο 'Chrono Cross' (1999) στο PlayStation, ποια συγκλονιστική πράξη εκτελεί ο κακός Lynx στο Fort Dragonia αλλάζοντας τη μοίρα του πρωταγωνιστή Serge;",
        "correct": "Ανταλλάσσει σώματα με τον Serge",
        "distractors": ["Στέλνει τον Serge 1.000 χρόνια στο μέλλον", "Σβήνει τις αναμνήσεις όλων των συντρόφων του", "Κλέβει το Frozen Flame"],
        "explanation": "Ο Lynx παγιδεύει τον Serge στο δικό του σώμα (ανθρωπόμορφος πάνθηρας), αναγκάζοντας τους φίλους του Serge να στραφούν εναντίον του καθώς νομίζουν ότι είναι ο εχθρός.",
        "funFacts": [
            "Το Chrono Cross περιλαμβάνει πάνω από 40 στρατολογήσιμους χαρακτήρες και διαδραματίζεται σε δύο παράλληλες διαστάσεις: Home World και Another World.",
            "Το soundtrack του Yasunori Mitsuda θεωρείται από τα σπουδαιότερα μουσικά έργα στην ιστορία των JRPGs."
        ],
        "source": "https://en.wikipedia.org/wiki/Chrono_Cross",
        "tags": ["gaming", "chrono_cross", "square", "playstation", "rpg"]
    },
    {
        "id": "gaming_med_354",
        "text": "Στο φιλοσοφικό mecha RPG 'Xenogears' (1998) της Square, ποιο είναι το καταστροφικό alter ego που κρύβεται στο υποσυνείδητο του πρωταγωνιστή Fei Fong Wong;",
        "correct": "Id",
        "distractors": ["Grahf", "Krelian", "Lacan"],
        "explanation": "Ο Id δημιουργήθηκε ως ψυχικός μηχανισμός άμυνας στα βασανιστήρια της παιδικής ηλικίας του Fei και οδηγεί το κατακόκκινο Gear Weltall-Id σκορπώντας την απόλυτη καταστροφή.",
        "funFacts": [
            "Το Xenogears αντλεί έντονη επιρροή από τη χριστιανική θεολογία, τον γνωστικισμό και τις θεωρίες του Sigmund Freud και του Carl Jung.",
            "Ο δημιουργός Tetsuya Takahashi ίδρυσε αργότερα τη Monolith Soft και δημιούργησε τις σειρές Xenosaga και Xenoblade Chronicles."
        ],
        "source": "https://en.wikipedia.org/wiki/Xenogears",
        "tags": ["gaming", "xenogears", "square", "playstation", "rpg"]
    },
    {
        "id": "gaming_med_355",
        "text": "Στο 'Armored Core VI: Fires of Rubicon' (2023) της FromSoftware, ποια είναι η πολύτιμη ενεργειακή ουσία στον πλανήτη Rubicon 3 για την οποία μάχονται οι εταιρείες;",
        "correct": "Coral (Κοράλλι)",
        "distractors": ["Mako", "Kojima Particles", "Tiberium"],
        "explanation": "Το Coral είναι μια μυστηριώδης ουσία που χρησιμεύει ως υπερ-καύσιμο και αγωγός δεδομένων, αλλά προκάλεσε την ιστορική πυρκαγιά που κατέκαψε το αστρικό σύστημα (Fires of Ibis).",
        "funFacts": [
            "Ο παίκτης χειρίζεται έναν γενετικά τροποποιημένο μισθοφόρο πιλότο με τον κωδικό C4-621 υπό τις εντολές του Handler Walter.",
            "Το Armored Core VI σημείωσε ρεκόρ πωλήσεων για ολόκληρη τη μακρόχρονη σειρά mech της FromSoftware."
        ],
        "source": "https://en.wikipedia.org/wiki/Armored_Core_VI:_Fires_of_Rubicon",
        "tags": ["gaming", "armored_core", "fromsoftware", "action"]
    },
    {
        "id": "gaming_med_356",
        "text": "Στο 'Overwatch', ποιος Ολλανδός αστροφυσικός που υπέστη εγκεφαλική βλάβη από πείραμα μαύρης τρύπας φωνάζει 'Het universum zingt voor mij!';",
        "correct": "Sigma (Siebren de Kuiper)",
        "distractors": ["Reinhardt", "Torbjörn", "Ramattra"],
        "explanation": "Ο Sigma χειρίζεται τη βαρύτητα εκτοξεύοντας σφαίρες βαρυτικής μάζας (Hyperspheres) και σηκώνοντας ολόκληρη την αντίπαλη ομάδα στον αέρα με το Gravitic Flux.",
        "funFacts": [
            "Η ολλανδική φράση που φωνάζει σημαίνει: 'Το σύμπαν τραγουδάει για μένα!'.",
            "Ο Sigma ακούει συνεχώς στο μυαλό του μια παράξενη μελωδία πιάνου ('What is that melody?')."
        ],
        "source": "https://en.wikipedia.org/wiki/Characters_of_Overwatch#Sigma",
        "tags": ["gaming", "overwatch", "blizzard", "sigma", "characters"]
    },
    {
        "id": "gaming_med_357",
        "text": "Ποια διάσημη ουδέτερη θρυλική κάρτα στο 'Hearthstone' εισήγαγε το battlecry που καλεί δύο δρακοντάκια (1/1 Whelps) για τον αντίπαλο φωνάζοντας το όνομά της;",
        "correct": "Leeroy Jenkins",
        "distractors": ["Ragnaros the Firelord", "Sylvanas Windrunner", "Bloodmage Thalnos"],
        "explanation": "Η κάρτα αποτελεί φόρο τιμής στο θρυλικό βίντεο viral του World of Warcraft (2005) όπου ο Leeroy Jenkins καταστρέφει το σχέδιο της ομάδας του φωνάζοντας 'Leeeeeroy Jenkins!'.",
        "funFacts": [
            "Η κάρτα είχε Charge, 6 Attack και κόστος μόλις 4 (αργότερα 5) Mana, καθιστώντας την την πιο δημοφιλή finisher κάρτα για επιθετικές aggro τράπουλες.",
            "Το 2020 η Blizzard έστειλε την κάρτα στο 'Hall of Fame' για να ανανεώσει τη μεταβαλλόμενη competitive meta του Standard."
        ],
        "source": "https://en.wikipedia.org/wiki/Leeroy_Jenkins",
        "tags": ["gaming", "hearthstone", "blizzard", "memes", "card_game"]
    },
    {
        "id": "gaming_med_358",
        "text": "Ποιος πρώην Αρχάγγελος της Σοφίας επιστρέφει ως η Πτυχή του Θανάτου (Aspect of Death) στο expansion 'Diablo III: Reaper of Souls' (2014);",
        "correct": "Malthael",
        "distractors": ["Tyrael", "Imperius", "Auriel"],
        "explanation": "Ο Malthael κλέβει το Black Soulstone και προσπαθεί να εξοντώσει ολόκληρη την ανθρωπότητα θεωρώντας τους ανθρώπους απογόνους δαιμόνων (Nephalem).",
        "funFacts": [
            "Ο Malthael μάχεται κρατώντας δύο δρεπάνια ψυχών και απορροφά τις ψυχές των νεκρών στο τέλος της μάχης στο Pandemonium Fortress.",
            "Το Reaper of Souls πρόσθεσε την κλάση του Crusader και τη λειτουργία Adventure Mode με Bounties και Nephalem Rifts."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_III:_Reaper_of_Souls",
        "tags": ["gaming", "diablo", "blizzard", "reaper_of_souls", "bosses"]
    },
    {
        "id": "gaming_med_359",
        "text": "Στο αποκορύφωμα της αρχικής εκστρατείας του 'StarCraft' (1998), πώς θυσιάζεται ο High Templar Tassadar για να εξοντώσει οριστικά το Zerg Overmind στον Aiur;",
        "correct": "Συντρίβει τη ναυαρχίδα του Gantrithor πάνω στο Overmind διοχετεύοντας ενέργειες Khala και Void",
        "distractors": [
            "Πυροδοτεί έναν κβαντικό πυρηνικό αντιδραστήρα",
            "Χρησιμοποιεί έναν αρχαίο κρύσταλλο των Xel'Naga",
            "Επικαλείται μια υπερμεγέθη ψιονική καταιγίδα Psionic Storm"
        ],
        "explanation": "Ο Tassadar συνδύασε τις φαινομενικά ασυμβίβαστες δυνάμεις του φωτεινού Khala και του σκοτεινού Void των Dark Templar, θυσιάζοντας τη ζωή του για να σώσει την πατρίδα των Protoss.",
        "funFacts": [
            "Η θυσία του Tassadar ενέπνευσε τον επίσημο χαιρετισμό τιμής των Protoss: 'En Taro Tassadar!'.",
            "Στο StarCraft II αποκαλύπτεται ότι μια ψευδής προβολή του Tassadar χρησιμοποιήθηκε από τον Xel'Naga Ouros για να καθοδηγήσει τον Zeratul."
        ],
        "source": "https://en.wikipedia.org/wiki/StarCraft_(video_game)",
        "tags": ["gaming", "starcraft", "blizzard", "tassadar", "lore"]
    },
    {
        "id": "gaming_med_360",
        "text": "Στο 'Persona 3' (2006), ποια παράξενη συσκευή που μοιάζει με πιστόλι (Evoker) χρησιμοποιούν οι μαθητές στο κεφάλι τους για να καλέσουν τα Personas τους;",
        "correct": "Evoker",
        "distractors": ["MetaNav", "Tarot Gun", "Shadow Blaster"],
        "explanation": "Το Evoker προσομοιώνει το ακραίο σοκ και την εμπειρία του θανάτου, αναγκάζοντας την ανθρώπινη ψυχή να απελευθερώσει το Persona της κατά τη διάρκεια του Dark Hour.",
        "funFacts": [
            "Ο σκοτεινός 25ος κρυφός χρόνος της ημέρας όπου οι άνθρωποι μετατρέπονται σε φέρετρα ονομάζεται The Dark Hour.",
            "Ο τεράστιος πύργος που εμφανίζεται στο κέντρο του σχολείου Gekkoukan High ονομάζεται Tartarus και έχει πάνω από 250 ορόφους."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_3",
        "tags": ["gaming", "persona", "atlus", "jrpg", "playstation"]
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
        "difficulty": 3,
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
    print(f"Loaded {len(questions)} questions for gaming_medium batch 3.")
    validate_and_append("gaming", "medium", 3, questions)

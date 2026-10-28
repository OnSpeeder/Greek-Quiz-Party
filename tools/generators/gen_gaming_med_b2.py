# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_med_261",
        "text": "Στο πρώτο 'Half-Life' (1998), ποιο καταστροφικό φαινόμενο προκαλείται στα εργαστήρια της Black Mesa κατά τη δοκιμή του δείγματος GG-3883;",
        "correct": "Resonance Cascade (Καταρράκτης Συντονισμού)",
        "distractors": [
            "Quantum Collapse (Κβαντική Κατάρρευση)",
            "Subatomic Rupture (Υποατομική Ρήξη)",
            "Dimensional Void (Διαστατικό Κενό)"
        ],
        "explanation": "Ο Gordon Freeman σπρώχνει το δείγμα στον Anti-Mass Spectrometer, προκαλώντας το Resonance Cascade που ανοίγει ρήγμα με τη διάσταση Xen και επιτρέπει την εισβολή εξωγήινων.",
        "funFacts": [
            "Το συμβάν του Resonance Cascade τράβηξε αργότερα την προσοχή της πανίσχυρης διαγαλαξιακής αυτοκρατορίας Combine, οδηγώντας στον Επτάωρο Πόλεμο (Seven Hour War).",
            "Ο μυστηριώδης άντρας με το κουστούμι και το χαρτοφύλακα, G-Man, ήταν αυτός που παρείχε το εξωγήινο δείγμα στους επιστήμονες της Black Mesa."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life_(video_game)",
        "tags": ["gaming", "half_life", "valve", "black_mesa", "lore"]
    },
    {
        "id": "gaming_med_262",
        "text": "Στο 'The Legend of Zelda: The Wind Waker' (2002), ποιο είναι το όνομα του ομιλούντος κόκκινου καραβιού που καθοδηγεί τον Link στον Μεγάλο Ωκεανό;",
        "correct": "King of Red Lions (Βασιλιάς των Κόκκινων Λεόντων)",
        "distractors": ["Linebeck", "Spirit Train", "Phantom Vessel"],
        "explanation": "Το πλοίο με την κεφαλή κόκκινου λιονταριού αποκαλύπτεται ότι ελέγχεται από το πνεύμα του βασιλιά της Hyrule, Daphnes Nohansen Hyrule.",
        "funFacts": [
            "Το Wind Waker προκάλεσε έντονες αντιδράσεις πριν την κυκλοφορία του λόγω των cel-shaded γραφικών του (που οι θαυμαστές αποκάλεσαν κοροϊδευτικά 'Celda'), αλλά αργότερα αναγνωρίστηκε ως αριστούργημα.",
            "Ο Link χρησιμοποιεί τη μαγική μπαγκέτα Wind Waker για να αλλάζει την κατεύθυνση των ανέμων ώστε να ταξιδεύει γρήγορα με τα πανιά."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_The_Wind_Waker",
        "tags": ["gaming", "zelda", "wind_waker", "nintendo", "gamecube"]
    },
    {
        "id": "gaming_med_263",
        "text": "Ποιο είναι το διαβόητο δίδυμο αφεντικών στον καθεδρικό ναό του Anor Londo που δοκιμάζει σκληρά την υπομονή των παικτών στο πρώτο 'Dark Souls';",
        "correct": "Ornstein και Smough",
        "distractors": [
            "Artorias και Sif",
            "Bell Gargoyles",
            "Twin Princes (Lorian & Lothric)"
        ],
        "explanation": "Ο ταχύτατος Dragon Slayer Ornstein με το ηλεκτρικό δόρυ και ο ογκώδης Executioner Smough με το γιγάντιο σφυρί πολεμούν ταυτόχρονα, και όποιος πεθάνει πρώτος απορροφάται από τον άλλον.",
        "funFacts": [
            "Αν ο παίκτης σκοτώσει πρώτα τον Smough, ο Ornstein μεγαλώνει σε γιγάντιο μέγεθος, ενώ αν σκοτώσει πρώτα τον Ornstein, ο Smough αποκτά ηλεκτρικές επιθέσεις στο σφυρί του.",
            "Η πανοπλία του Smough έχει μάτια σχεδιασμένα στον λαιμό και όχι στο πρόσωπο του κράνους, κάτι που πολλοί παίκτες δεν προσέχουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Dark_Souls",
        "tags": ["gaming", "dark_souls", "fromsoftware", "bosses"]
    },
    {
        "id": "gaming_med_264",
        "text": "Στο 'Bloodborne', ποιος ισχυρός θρησκευτικός θεσμός του Yharnam ξεκίνησε τη θεραπεία μέσω αίματος (Blood Ministration) που οδήγησε στη μάστιγα των θηρίων;",
        "correct": "Η Εκκλησία της Θεραπείας (Healing Church)",
        "distractors": ["Το Κολλέγιο Byrgenwerth", "Η Σχολή Mensis", "Η Χορωδία (The Choir)"],
        "explanation": "Η Healing Church ιδρύθηκε από τον Laurence μετά το σχίσμα του με τον Master Willem του Byrgenwerth, διαδίδοντας τη χρήση του αρχαίου εξωγήινου αίματος (Old Blood).",
        "funFacts": [
            "Η προειδοποιητική φράση του Master Willem προς τον Laurence ήταν: 'Fear the Old Blood' (Φοβού το Αρχαίο Αίμα).",
            "Η Εκκλησία ίδρυσε μυστικά τάγματα κυνηγών, με επικεφαλής μορφές όπως ο Ludwig και ο Simon."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloodborne",
        "tags": ["gaming", "bloodborne", "fromsoftware", "lore"]
    },
    {
        "id": "gaming_med_265",
        "text": "Ποιος είναι ο κεντρικός πρωταγωνιστής στο 'Sekiro: Shadows Die Twice' (2019), ένας μονόχειρας shinobi που υπηρετεί τον νεαρό άρχοντα Kuro;",
        "correct": "Wolf (Okami / Sekiro)",
        "distractors": ["Genichiro Ashina", "Isshin Ashina", "Owl"],
        "explanation": "Ο Wolf χάνει το αριστερό του χέρι σε μονομαχία με τον Genichiro και αποκτά το Shinobi Prosthetic, ένα προσθετικό μέλος εξοπλισμένο με γάντζο, shurikens και τσεκούρι.",
        "funFacts": [
            "Η λέξη 'Sekiro' είναι συντομογραφία της ιαπωνικής φράσης που σημαίνει 'Μονόχειρας Λύκος'.",
            "Το Sekiro απέσπασε το κορυφαίο βραβείο Game of the Year στα The Game Awards 2019."
        ],
        "source": "https://en.wikipedia.org/wiki/Sekiro:_Shadows_Die_Twice",
        "tags": ["gaming", "sekiro", "fromsoftware", "action"]
    },
    {
        "id": "gaming_med_266",
        "text": "Ποιο καταραμένο ρουνικό ξίφος άντλησε ο πρίγκιπας Arthas Menethil στις παγωμένες ερημιές του Northrend, σφραγίζοντας την πτώση του στο σκοτάδι;",
        "correct": "Frostmourne",
        "distractors": ["Shadowmourne", "Ashbringer", "Atiesh"],
        "explanation": "Το Frostmourne καταβρόχθισε την ίδια την ψυχή του Arthas, μετατρέποντάς τον στον πρώτο Ιππότη του Θανάτου (Death Knight) και μετέπειτα στον απόλυτο Lich King.",
        "funFacts": [
            "Στο τέλος του raid Icecrown Citadel στο Wrath of the Lich King, το Frostmourne θρυμματίζεται από το ιερό ξίφος Ashbringer του Tirion Fordring.",
            "Οι ψυχές που είχαν παγιδευτεί μέσα στο σπαθί απελευθερώνονται, συμπεριλαμβανομένου του πνεύματος του βασιλιά Terenas Menethil που βοηθά τους παίκτες."
        ],
        "source": "https://en.wikipedia.org/wiki/Arthas_Menethil",
        "tags": ["gaming", "warcraft", "world_of_warcraft", "blizzard", "frostmourne"]
    },
    {
        "id": "gaming_med_267",
        "text": "Ποια διάσημη πολεμική κραυγή απευθύνει ο Illidan Stormrage στους παίκτες στο cinematic τρέιλερ του 'World of Warcraft: The Burning Crusade' (2007);",
        "correct": "You are not prepared! (Δεν είστε προετοιμασμένοι!)",
        "distractors": ["Feel the hatred of ten thousand years!", "Tremble before the Betrayer!", "Your journey ends here!"],
        "explanation": "Ο Illidan Stormrage (The Betrayer) κυβερνά τον διαλυμένο κόσμο του Outland κρατώντας τα διπλά Warglaives of Azzinoth και προειδοποιεί τους εισβολείς ότι δεν είναι έτοιμοι.",
        "funFacts": [
            "Ο Illidan ήταν φυλακισμένος στα υπόγεια κελιά του Hyjal για 10.000 χρόνια υπό την άγρυπνη φρούρηση της Maiev Shadowsong.",
            "Η ατάκα 'You are not prepared!' έγινε μία από τις πιο γνωστές φράσεις σε ολόκληρη την ιστορία των MMORPGs."
        ],
        "source": "https://en.wikipedia.org/wiki/World_of_Warcraft:_The_Burning_Crusade",
        "tags": ["gaming", "world_of_warcraft", "blizzard", "illidan", "quotes"]
    },
    {
        "id": "gaming_med_268",
        "text": "Στο 'StarCraft', ποιος είναι ο ψιονικός κοινόχρηστος δεσμός που ενώνει τα συναισθήματα και τις σκέψεις όλων των Protoss της παράταξης Khalai;",
        "correct": "Khala (Το Μονοπάτι της Ανάτασης)",
        "distractors": ["The Overmind", "Void Resonance", "Psionic Matrix"],
        "explanation": "Το Khala επιτρέπει στους Protoss να μοιράζονται όλες τις εμπειρίες τους, ενώ οι Dark Templar (Nerazim) έκοψαν συνειδητά τα νευρικά τους κοτσίδια για να διατηρήσουν την ατομικότητά τους.",
        "funFacts": [
            "Στο StarCraft II: Legacy of the Void, ο σκοτεινός θεός Amon μολύνει το Khala, αναγκάζοντας τον Artanis και τους Khalai να κόψουν κι εκείνοι τα κοτσίδια τους.",
            "Ο φιλόσοφος Khas ήταν αυτός που ανακάλυψε εκ νέου τους κρυστάλλους Khaydarin και καθιέρωσε το Khala τερματίζοντας τον εμφύλιο πόλεμο Aeon of Strife."
        ],
        "source": "https://en.wikipedia.org/wiki/StarCraft",
        "tags": ["gaming", "starcraft", "blizzard", "protoss", "lore"]
    },
    {
        "id": "gaming_med_269",
        "text": "Στη σειρά 'Diablo', ποιο αρχαίο ιερό τάγμα μάγων και σοφών ίδρυσε ο Αρχάγγελος Tyrael για να αιχμαλωτίσει τα Τρία Πρωταρχικά Κακά στα Soulstones;",
        "correct": "Οι Horadrim (Χοράντριμ)",
        "distractors": ["Οι Iron Wolves", "Οι Zakarum", "Οι Crusaders"],
        "explanation": "Το τάγμα των Horadrim (με ηγέτες τους Tal Rasha, Jered Cain και Zoltan Kulle) φυλάκισε τον Diablo, τον Mephisto και τον Baal μέσα στις ψυχόπετρες (Soulstones).",
        "funFacts": [
            "Ο Deckard Cain ήταν ο τελευταίος επιζών απόγονος των αρχικών Horadrim μέχρι τον θάνατό του στο Diablo III.",
            "Το μαγικό τεχνούργημα Horadric Cube επιτρέπει τη μεταστοιχείωση και σύνθεση νέων αντικειμένων, πετραδιών και ρουνών."
        ],
        "source": "https://en.wikipedia.org/wiki/Diablo_(video_game_series)",
        "tags": ["gaming", "diablo", "blizzard", "lore", "horadrim"]
    },
    {
        "id": "gaming_med_270",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή στο 'Fallout: New Vegas' (2010), ο οποίος πυροβολείται στο κεφάλι στην αρχή του παιχνιδιού για ένα τσιπ πλατίνας;",
        "correct": "The Courier (Ο Ταχυδρόμος)",
        "distractors": ["The Lone Wanderer", "The Sole Survivor", "The Chosen One"],
        "explanation": "Ο Courier μεταφέρει ένα μυστηριώδες Platinum Chip στο New Vegas, αλλά πέφτει σε ενέδρα από τον γκάνγκστερ Benny (με τη φωνή του Matthew Perry) και θάβεται ζωντανός στο Goodsprings.",
        "funFacts": [
            "Τον Courier ξεθάβει και περιθάλπει ο καλοκάγαθος γιατρός Doc Mitchell στη μικρή κοινότητα του Goodsprings.",
            "Το παιχνίδι αναπτύχθηκε από την Obsidian Entertainment σε μόλις 18 μήνες και θεωρείται από πολλούς ως το καλύτερο RPG της σύγχρονης σειράς Fallout."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout:_New_Vegas",
        "tags": ["gaming", "fallout", "obsidian", "new_vegas", "rpg"]
    },
    {
        "id": "gaming_med_271",
        "text": "Στο 'Mass Effect', ποιο βιολογικό όπλο στειρότητας δημιούργησαν οι Salarians και εξαπέλυσαν οι Turians για να ελέγξουν τον πληθυσμό των Krogan;",
        "correct": "Genophage",
        "distractors": ["Phage-X", "Reaper Blight", "Krogan Plague"],
        "explanation": "Το Genophage μεταλλάσσει γενετικά τους Krogan ώστε μόνο μία στις χίλιες εγκυμοσύνες να καταλήγει σε ζωντανή γέννα, οδηγώντας το πολεμικό αυτό είδος σε αργό μαρασμό.",
        "funFacts": [
            "Ο Salarian επιστήμονας Mordin Solus είχε βοηθήσει στην τροποποίηση του Genophage αλλά αργότερα θυσιάζεται στο Mass Effect 3 για να το θεραπεύσει ('Had to be me. Someone else might have gotten it wrong').",
            "Η απόφαση του παίκτη να υποστηρίξει ή να σαμποτάρει τη θεραπεία του Genophage αποτελεί μια από τις πιο φορτισμένες ηθικές επιλογές στη σειρά."
        ],
        "source": "https://en.wikipedia.org/wiki/Mass_Effect",
        "tags": ["gaming", "mass_effect", "bioware", "lore", "sci_fi"]
    },
    {
        "id": "gaming_med_272",
        "text": "Στο 'Dragon Age: Origins' (2009) της BioWare, ποια θανάσιμη τελετή μύησης απαιτεί από τους υποψήφιους Grey Wardens να πιουν αίμα Darkspawn;",
        "correct": "The Joining (Η Ένωση)",
        "distractors": ["The Harrowing", "The Rite of Tranquility", "The Calling"],
        "explanation": "Το Joining συνδέει τον Grey Warden με το Darkspawn Hive Mind και του επιτρέπει να αισθάνεται τον Archdemon, αλλά πολλοί δόκιμοι πεθαίνουν ακαριαία από τη δηλητηρίαση.",
        "funFacts": [
            "Όταν οι Grey Wardens φτάνουν στα γεράματά τους και αρχίζουν να ακούνε το 'Κάλεσμα' (The Calling), ταξιδεύουν στα Deep Roads για να πεθάνουν πολεμώντας.",
            "Ο Archdemon μπορεί να εξοντωθεί μόνιμα μόνο αν σκοτωθεί από έναν Grey Warden, ο οποίος απορροφά την ψυχή του τέρατος και πεθαίνει μαζί του."
        ],
        "source": "https://en.wikipedia.org/wiki/Dragon_Age:_Origins",
        "tags": ["gaming", "dragon_age", "bioware", "rpg", "lore"]
    },
    {
        "id": "gaming_med_273",
        "text": "Ποιος Daedric Prince της καταστροφής και της αλλαγής προσπαθεί να εισβάλει στον κόσμο του Tamriel στο 'The Elder Scrolls IV: Oblivion' (2006);",
        "correct": "Mehrunes Dagon",
        "distractors": ["Molag Bal", "Sheogorath", "Hermaeus Mora"],
        "explanation": "Ο Mehrunes Dagon υποστηρίζεται από τη φανατική αίρεση Mythic Dawn του Mankar Camoran, η οποία δολοφονεί τον Αυτοκράτορα Uriel Septim VII για να σβήσει τις Dragonfires.",
        "funFacts": [
            "Ο Martin Septim (νόθος γιος του Αυτοκράτορα, με τη φωνή του Sean Bean) θυσιάζεται στο τέλος παίρνοντας τη μορφή του avatar του Akatosh.",
            "Στο κορυφαίο expansion 'Shivering Isles', οι παίκτες ταξιδεύουν στο βασίλειο της τρέλας του Sheogorath."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Elder_Scrolls_IV:_Oblivion",
        "tags": ["gaming", "oblivion", "bethesda", "elder_scrolls", "rpg"]
    },
    {
        "id": "gaming_med_274",
        "text": "Ποιο είναι το επαναστατικό σύστημα μάχης σώμα με σώμα που καθιέρωσε η Rocksteady Studios στο 'Batman: Arkham Asylum' (2009);",
        "correct": "FreeFlow Combat",
        "distractors": ["Dynamic Brawl", "Shadow Strike", "Combo Link"],
        "explanation": "Το σύστημα FreeFlow επέτρεπε στον Batman να γλιστρά ομαλά ανάμεσα σε δεκάδες εχθρούς με αυτόματη στόχευση, αντεπιθέσεις (counters) και gadgets χωρίς διακοπή του combo.",
        "funFacts": [
            "Το σύστημα FreeFlow αντιγράφηκε και επηρέασε δεκάδες μεταγενέστερα παιχνίδια δράσης, όπως τα Assassin's Creed, Middle-earth: Shadow of Mordor και Marvel's Spider-Man.",
            "Τη φωνή του Batman έκανε ο θρυλικός Kevin Conroy και του Joker ο Mark Hamill."
        ],
        "source": "https://en.wikipedia.org/wiki/Batman:_Arkham_Asylum",
        "tags": ["gaming", "batman", "arkham", "rocksteady", "action"]
    },
    {
        "id": "gaming_med_275",
        "text": "Στο 'Metal Gear Solid 3: Snake Eater' (2004), σε ποιο περιβάλλον μάχεται ο Naked Snake στην τελική αναμέτρηση με τη μέντορά του, The Boss;",
        "correct": "Σε ένα λιβάδι γεμάτο ολόλευκα λουλούδια (Star of Bethlehem)",
        "distractors": ["Στην κορυφή ενός πυρηνικού σιλό", "Μέσα στα συντρίμμια του Shagohod", "Στη γέφυρα Dolinovodno"],
        "explanation": "Η δεκάλεπτη αναμέτρηση εκτυλίσσεται σε ένα πανέμορφο λιβάδι με λευκά κρίνα, τα οποία βάφονται κόκκινα στο σημείο όπου πέφτει νεκρή η The Boss.",
        "funFacts": [
            "Ο παίκτης είναι υποχρεωμένος να πατήσει ο ίδιος το κουμπί της σκανδάλης για να ρίξει την τελική χαριστική βολή στην The Boss μετά τη μάχη.",
            "Ο Snake Eater εισήγαγε το σύστημα καμουφλάζ (Camo Index), επιβίωσης (κυνήγι φιδιών και ζώων) και θεραπείας καταγμάτων και τραυμάτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_3:_Snake_Eater",
        "tags": ["gaming", "metal_gear", "hideo_kojima", "bosses", "snake_eater"]
    },
    {
        "id": "gaming_med_276",
        "text": "Ποιο τολμηρό αφηγηματικό τέχνασμα εφάρμοσε ο Hideo Kojima στο 'Metal Gear Solid 2: Sons of Liberty' (2001) που εξέπληξε τους παίκτες παγκοσμίως;",
        "correct": "Αντικατέστησε τον Solid Snake με τον νεαρό πράκτορα Raiden για το 90% του παιχνιδιού",
        "distractors": [
            "Σκότωσε τον Snake στα πρώτα πέντε λεπτά του παιχνιδιού",
            "Μετέτρεψε το παιχνίδι σε first-person shooter χωρίς προειδοποίηση",
            "Αποκάλυψε ότι ο Snake ήταν ρομπότ από την αρχή"
        ],
        "explanation": "Μετά το κεφάλαιο του Tanker με τον Snake, ο έλεγχος περνά στον Raiden στην υπεράκτια εγκατάσταση Big Shell, μια ανατροπή που είχε κρατηθεί εντελώς μυστική στα τρέιλερ.",
        "funFacts": [
            "Ο Kojima έκρυψε την ύπαρξη του Raiden σε όλες τις διαφημίσεις και τα pre-release demos, αντικαθιστώντας το μοντέλο του με τον Snake.",
            "Το σενάριο του MGS2 προέβλεψε με εκπληκτική ακρίβεια τη διάδοση των fake news, των αλγορίθμων κοινωνικών δικτύων και της ψηφιακής παραπληροφόρησης δεκαετίες πριν συμβούν."
        ],
        "source": "https://en.wikipedia.org/wiki/Metal_Gear_Solid_2:_Sons_of_Liberty",
        "tags": ["gaming", "metal_gear", "hideo_kojima", "raiden", "story"]
    },
    {
        "id": "gaming_med_277",
        "text": "Στο 'Dead Space', τι είναι τα μυστηριώδη εξωγήινα τεχνουργήματα σε σχήμα διπλής έλικας (Markers) που προκαλούν παράνοια και επιθετικότητα;",
        "correct": "Αναμεταδότες που αναδιατάσσουν νεκρό ιστό σε Necromorphs",
        "distractors": ["Μηχανές τηλεμεταφοράς άλλων διαστάσεων", "Αρχαία πυρηνικά όπλα", "Ενεργειακές πηγές διαστημοπλοίων"],
        "explanation": "Τα Markers εκπέμπουν ένα ηλεκτρομαγνητικό σήμα που οδηγεί τους ανθρώπους στην παράνοια και την αυτοκτονία, ενεργοποιώντας στη συνέχεια τον ανασυνδυασμό των πτωμάτων σε Necromorphs.",
        "funFacts": [
            "Τα πρώτα γράμματα των τίτλων των κεφαλαίων του Dead Space (1) σχηματίζουν το ακροστιχίδιο 'NICOLE IS DEAD', αποκαλύπτοντας το μεγάλο plot twist του τέλους.",
            "Το αρχικό αυθεντικό Marker που βρέθηκε στη Γη στον κρατήρα Chicxulub ήταν το Black Marker, ενώ όλα τα υπόλοιπα ήταν τεχνητά αντίγραφα (Red Markers)."
        ],
        "source": "https://en.wikipedia.org/wiki/Dead_Space_(2008_video_game)",
        "tags": ["gaming", "dead_space", "ea", "visceral_games", "horror"]
    },
    {
        "id": "gaming_med_278",
        "text": "Στο 'Resident Evil 7: Biohazard' (2017), ποια διεστραμμένη οικογένεια κρατά αιχμάλωτο τον Ethan Winters σε μια απομονωμένη έπαυλη στη Λουιζιάνα;",
        "correct": "Η οικογένεια Baker (The Bakers)",
        "distractors": ["Η οικογένεια Dimitrescu", "Η οικογένεια Spencer", "Η οικογένεια Ashford"],
        "explanation": "Ο Jack, η Marguerite και ο Lucas Baker έχουν μολυνθεί και ελέγχονται νοητικά από ένα βιολογικό όπλο σε μορφή μικρού κοριτσιού, την Eveline (E-001).",
        "funFacts": [
            "Η σκηνή του οικογενειακού δείπνου στην αρχή του παιχνιδιού αποτελεί άμεσο φόρο τιμής στην κλασική ταινία τρόμου 'The Texas Chain Saw Massacre'.",
            "Η ατάκα του Jack Baker καθώς γκρεμίζει έναν τοίχο με το τσεκούρι είναι: 'Welcome to the family, son!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_7:_Biohazard",
        "tags": ["gaming", "resident_evil", "capcom", "survival_horror"]
    },
    {
        "id": "gaming_med_279",
        "text": "Ποιο είναι το διαβόητο μυστικό φονικό χτύπημα του Akuma (Gouki) στο 'Street Fighter' που μαυρίζει την οθόνη και εμφανίζει το ιαπωνικό σύμβολο 'Ten' (Ουρανός);",
        "correct": "Shun Goku Satsu (Raging Demon)",
        "distractors": ["Messatsu Gou Hadou", "Kongou Kokuretsuzan", "Tatsumaki Gou Rasen"],
        "explanation": "Το Shun Goku Satsu καταστρέφει την ψυχή του θύματος εκμεταλλευόμενο το βάρος των αμαρτιών του· εκτελείται με τον συνδυασμό: LP, LP, Forward, LK, HP.",
        "funFacts": [
            "Το ιαπωνικό κάντζι 天 (Ten) που ανάβει στην πλάτη του Akuma μετά την κίνηση σημαίνει 'Ουρανός' ή 'Απόλυτη Θεότητα'.",
            "Ο Akuma εμφανίστηκε για πρώτη φορά ως μυστικό κρυφό αφεντικό στο Super Street Fighter II Turbo (1994)."
        ],
        "source": "https://en.wikipedia.org/wiki/Akuma_(Street_Fighter)",
        "tags": ["gaming", "street_fighter", "capcom", "akuma", "fighting"]
    },
    {
        "id": "gaming_med_280",
        "text": "Ποια υπερφυσική γενετική κατάρα μοιράζονται ο Kazuya Mishima και ο γιος του Jin Kazama στη σειρά μαχών 'Tekken';",
        "correct": "The Devil Gene (Το Γονίδιο του Διαβόλου)",
        "distractors": ["The Mishima Curse", "The Ogre Blood", "The Tengu Spirit"],
        "explanation": "Το Devil Gene κληροδοτήθηκε από τη μητέρα του Kazuya, Kazumi Hachijo, και επιτρέπει στους φορείς του να μεταμορφώνονται σε δαίμονες με φτερά και ακτίνες λέιζερ.",
        "funFacts": [
            "Ο Heihachi Mishima δεν διαθέτει το Devil Gene, αλλά προσπαθούσε διαρκώς να το κλέψει για να αποκτήσει αθανασία.",
            "Η εσωτερική πάλη του Jin Kazama με το Devil Gene αποτελεί τον κεντρικό δραματικό άξονα της ιστορίας από το Tekken 3 και έπειτα."
        ],
        "source": "https://en.wikipedia.org/wiki/Tekken",
        "tags": ["gaming", "tekken", "bandai_namco", "kazuya", "jin_kazama"]
    },
    {
        "id": "gaming_med_281",
        "text": "Ποιο είναι το χαρακτηριστικό υβριδικό όπλο που κρατάει ο Squall Leonhart στο 'Final Fantasy VIII' (1999);",
        "correct": "Gunblade (Γκάνμπλεϊντ)",
        "distractors": ["Buster Sword", "Keyblade", "Masamune"],
        "explanation": "Το Gunblade είναι ένα σπαθί με μηχανισμό περιστρόφου στη λαβή· όταν ο παίκτης πατάει τη σκανδάλη (R1) ακριβώς τη στιγμή του χτυπήματος, στέλνει ωστικό κύμα δόνησης στη λεπίδα για κρίσιμη ζημιά.",
        "funFacts": [
            "Σε αντίθεση με ό,τι νομίζουν πολλοί, το παραδοσιακό Gunblade του Squall δεν εκτοξεύει σφαίρες ως βλήματα από μακριά, αλλά πυροδοτεί φυσίγγια για να δονεί τη λεπίδα.",
            "Ο αιώνιος αντίζηλος του Squall στη στρατιωτική ακαδημία Balamb Garden, Seifer Almasy, χειρίζεται επίσης ένα Gunblade μοντέλου Hyperion."
        ],
        "source": "https://en.wikipedia.org/wiki/Squall_Leonhart",
        "tags": ["gaming", "final_fantasy", "square_enix", "squall", "weapons"]
    },
    {
        "id": "gaming_med_282",
        "text": "Ποιο είναι το όνομα του μικρού μαύρου μάγου με το μυτερό καπέλο και τα φωτεινά κίτρινα μάτια στο 'Final Fantasy IX' που συγκίνησε με τα υπαρξιακά του διλήμματα;",
        "correct": "Vivi Ornitier",
        "distractors": ["Zidane Tribal", "Steiner", "Freya Crescent"],
        "explanation": "Ο Vivi ανακαλύπτει ότι είναι ένα τεχνητό κατασκεύασμα μαγείας με περιορισμένη διάρκεια ζωής, εξερευνώντας βαθιά φιλοσοφικά ερωτήματα για τον θάνατο και το νόημα της ύπαρξης.",
        "funFacts": [
            "Ο δημιουργός της σειράς Hironobu Sakaguchi έχει δηλώσει ότι το Final Fantasy IX είναι το αγαπημένο του παιχνίδι στη σειρά και ο Vivi ο αγαπημένος του χαρακτήρας.",
            "Η επιστολή του Vivi στους τίτλους τέλους θεωρείται ένα από τα πιο συγκινητικά κείμενα στην ιστορία των βιντεοπαιχνιδιών."
        ],
        "source": "https://en.wikipedia.org/wiki/Vivi_Ornitier",
        "tags": ["gaming", "final_fantasy", "square_enix", "vivi", "characters"]
    },
    {
        "id": "gaming_med_283",
        "text": "Στο 'Kingdom Hearts II' (2005), πού περνάει ο Roxas τις τελευταίες επτά ημέρες των καλοκαιρινών του διακοπών πριν συγχωνευτεί ξανά με τον Sora;",
        "correct": "Σε μια εικονική προσομοίωση του Twilight Town",
        "distractors": ["Στο Traverse Town", "Στο Hollow Bastion", "Στο Destiny Islands"],
        "explanation": "Ο DiZ (Ansem the Wise) είχε τοποθετήσει τον Roxas μέσα σε μια ψηφιακή προσομοίωση του Twilight Town για να αποκαταστήσει τις αναμνήσεις του Sora.",
        "funFacts": [
            "Η εισαγωγή με τον Roxas διαρκεί περίπου 2-3 ώρες και θεωρείται ένα από τα πιο μελαγχολικά και ατμοσφαιρικά κεφάλαια της σειράς.",
            "Η διάσημη τελευταία φράση του Roxas πριν παραδώσει τη συνείδησή του είναι: 'Looks like my summer vacation is... over'."
        ],
        "source": "https://en.wikipedia.org/wiki/Roxas_(Kingdom_Hearts)",
        "tags": ["gaming", "kingdom_hearts", "square_enix", "roxas"]
    },
    {
        "id": "gaming_med_284",
        "text": "Ποιος είναι ο χαρισματικός νεαρός ηγέτης της Team Plasma στα 'Pokémon Black & White' που πιστεύει ότι τα Pokémon πρέπει να απελευθερωθούν από τους ανθρώπους;",
        "correct": "N (Natural Harmonia Gropius)",
        "distractors": ["Ghetsis", "Colress", "Lysandre"],
        "explanation": "Ο N μπορεί να ακούει και να κατανοεί τις φωνές των Pokémon και επιδιώκει τη δημιουργία δύο ξεχωριστών κόσμων για να σταματήσει η εκμετάλλευσή τους.",
        "funFacts": [
            "Στο τέλος του παιχνιδιού αποκαλύπτεται ότι ο N ήταν απλώς πιόνι στα χέρια του θετού πατέρα του Ghetsis, ο οποίος ήθελε να αφοπλίσει τον κόσμο για να τον κατακτήσει.",
            "Τα Black & White επαινέθηκαν ιδιαίτερα από τους κριτικούς για το πιο ώριμο και φιλοσοφικό τους σενάριο."
        ],
        "source": "https://en.wikipedia.org/wiki/Pok%C3%A9mon_Black_and_White",
        "tags": ["gaming", "pokemon", "nintendo", "characters", "story"]
    },
    {
        "id": "gaming_med_285",
        "text": "Ποιος ήταν ο διασημότερος αστικός μύθος στα πρώτα 'Pokémon Red και Blue' σχετικά με το πού κρυβόταν το μυθικό Pokémon Mew;",
        "correct": "Κάτω από ένα σταθμευμένο φορτηγό δίπλα στο πλοίο S.S. Anne",
        "distractors": [
            "Στην κορυφή του Pokémon Tower στο Lavender Town",
            "Πίσω από τον φράχτη του Professor Oak στο Pallet Town",
            "Στο βάθος του Safari Zone χρησιμοποιώντας Surf"
        ],
        "explanation": "Υπήρχε όντως ένα μοναδικό φορτηγό ζωγραφισμένο στο λιμάνι του S.S. Anne χωρίς προφανή σκοπό, πυροδοτώντας φήμες ότι χρησιμοποιώντας Strength μπορούσες να βρεις το Mew.",
        "funFacts": [
            "Στην πραγματικότητα, το Mew είχε προστεθεί κρυφά στον κώδικα από τον Shigeki Morimoto μόλις λίγες ημέρες πριν την ολοκλήρωση του παιχνιδιού χωρίς να το ξέρει η Nintendo.",
            "Οι παίκτες μπορούσαν τελικά να πιάσουν το Mew μέσω ενός πραγματικού glitch μνήμης (Mew Glitch) με το Trainer-Fly."
        ],
        "source": "https://en.wikipedia.org/wiki/Mew_(Pok%C3%A9mon)",
        "tags": ["gaming", "pokemon", "game_boy", "urban_legend", "retro"]
    },
    {
        "id": "gaming_med_286",
        "text": "Ποια είναι η κακόφημη πόλη-λιμάνι που λειτουργεί ως κεντρικός κόμβος (hub) στο 'Paper Mario: The Thousand-Year Door' (2004) του GameCube;",
        "correct": "Rogueport",
        "distractors": ["Toad Town", "Flipside", "Decalburg"],
        "explanation": "Το Rogueport είναι μια παρακμιακή πόλη γεμάτη απατεώνες, κλέφτες και μια αγχόνη στην κεντρική πλατεία, κάτω από την οποία κρύβονται τα αρχαία ερείπια και η Χιλιετής Πύλη.",
        "funFacts": [
            "Το παιχνίδι επανακυκλοφόρησε με πλήρες remake στο Nintendo Switch το 2024 γνωρίζοντας τεράστια εμπορική επιτυχία.",
            "Οι μάχες στο παιχνίδι διαδραματίζονται πάνω σε μια θεατρική σκηνή με ζωντανό κοινό που πετάει αντικείμενα ή φεύγει αν βαρεθεί."
        ],
        "source": "https://en.wikipedia.org/wiki/Paper_Mario:_The_Thousand-Year_Door",
        "tags": ["gaming", "paper_mario", "nintendo", "gamecube", "rpg"]
    },
    {
        "id": "gaming_med_287",
        "text": "Ποιο παιχνίδι στρατηγικής της Intelligent Systems στο Nintendo 3DS (2012) έσωσε ολόκληρο το franchise 'Fire Emblem' από οριστική ακύρωση;",
        "correct": "Fire Emblem: Awakening",
        "distractors": ["Fire Emblem: Fates", "Fire Emblem: Three Houses", "Fire Emblem: Shadow Dragon"],
        "explanation": "Η Nintendo είχε προειδοποιήσει την ομάδα ότι αν το παιχνίδι δεν πουλούσε τουλάχιστον 250.000 αντίτυπα, η σειρά θα τερματιζόταν· το Awakening πούλησε τελικά πάνω από 2 εκατομμύρια αντίτυπα.",
        "funFacts": [
            "Το παιχνίδι εισήγαγε το 'Casual Mode' όπου οι χαρακτήρες δεν πέθαιναν οριστικά (permadeath), προσελκύοντας εκατομμύρια νέους παίκτες.",
            "Εισήγαγε επίσης ένα πλούσιο σύστημα σχέσεων και γάμων μεταξύ χαρακτήρων που παρήγαγε παιδιά-μαχητές από το μέλλον."
        ],
        "source": "https://en.wikipedia.org/wiki/Fire_Emblem_Awakening",
        "tags": ["gaming", "fire_emblem", "nintendo", "3ds", "strategy"]
    },
    {
        "id": "gaming_med_288",
        "text": "Ποιο είναι το θρυλικό ενεργειακό σπαθί που κρατάει ο Shulk στο 'Xenoblade Chronicles' (2010), προσφέροντάς του οράματα για το μέλλον;",
        "correct": "Monado",
        "distractors": ["Aegis", "Zohar", "Soul Edge"],
        "explanation": "Το Monado είναι το μόνο όπλο που μπορεί να διαπεράσει τη μηχανική πανοπλία των Mechon και επιτρέπει στον Shulk να βλέπει εχθρικές επιθέσεις δευτερόλεπτα πριν συμβούν.",
        "funFacts": [
            "Ο κόσμος του Xenoblade Chronicles αποτελείται εξ ολοκλήρου από τα σώματα δύο απολιθωμένων γιγάντων: του Bionis και του Mechonis.",
            "Η διάσημη ατάκα του Shulk στο Super Smash Bros. είναι: 'I'm really feeling it!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Xenoblade_Chronicles",
        "tags": ["gaming", "xenoblade", "monolith_soft", "nintendo", "rpg"]
    },
    {
        "id": "gaming_med_289",
        "text": "Ποιο ανεξάρτητο παιχνίδι του Derek Yu (2008) καθιέρωσε τις αρχές των σύγχρονων Roguelike platformers με διαδικαστικά παραγόμενα επίπεδα σπηλαίων;",
        "correct": "Spelunky",
        "distractors": ["Cave Story", "Rogue Legacy", "Terraria"],
        "explanation": "Στο Spelunky, ο παίκτης εξερευνά επικίνδυνες σπηλιές με μαστίγιο, βόμβες και σχοινιά, όπου κάθε θάνατος είναι μόνιμος και κάθε διαδρομή μοναδική.",
        "funFacts": [
            "Αν ο παίκτης εξοργίσει τον καταστηματάρχη (Shopkeeper) κλέβοντας ένα αντικείμενο, εκείνος μετατρέπεται σε πάνοπλο εφιάλτη με καραμπίνα σε όλες τις επόμενες πίστες.",
            "Το Spelunky ξεκίνησε ως δωρεάν παιχνίδι φτιαγμένο στο GameMaker πριν αποκτήσει πλήρη εμπορική HD έκδοση."
        ],
        "source": "https://en.wikipedia.org/wiki/Spelunky",
        "tags": ["gaming", "spelunky", "indie", "roguelike", "derek_yu"]
    },
    {
        "id": "gaming_med_290",
        "text": "Στο παιχνίδι 'Hotline Miami' (2012), σε ποια δεκαετία διαδραματίζονται οι αιματηρές αποστολές του πρωταγωνιστή 'Jacket' με τις μάσκες ζώων;",
        "correct": "Δεκαετία του 1980 (1989)",
        "distractors": ["Δεκαετία του 1970", "Δεκαετία του 1990", "Δεκαετία του 2000"],
        "explanation": "Το Hotline Miami διαδραματίζεται το 1989 στο Μαϊάμι, συνοδευόμενο από έντονα νέον χρώματα, βία ενός χτυπήματος και ένα εκρηκτικό synthwave soundtrack.",
        "funFacts": [
            "Ο πρωταγωνιστής λαμβάνει κρυπτικά μηνύματα στον τηλεφωνητή του που του αναθέτουν διευθύνσεις της ρωσικής μαφίας.",
            "Η ερώτηση που θέτει η μυστηριώδης φιγούρα με τη μάσκα κόκορα Richard είναι: 'Do you like hurting other people?'."
        ],
        "source": "https://en.wikipedia.org/wiki/Hotline_Miami",
        "tags": ["gaming", "hotline_miami", "devolver_digital", "indie", "retro"]
    },
    {
        "id": "gaming_med_291",
        "text": "Ποιο είναι το όνομα του μοναδικού δημιουργού (γνωστού ως ConcernedApe) που ανέπτυξε εξ ολοκλήρου μόνος του το αγαπημένο 'Stardew Valley' (2016);",
        "correct": "Eric Barone",
        "distractors": ["Lucas Pope", "Toby Fox", "Thomas Happ"],
        "explanation": "Ο Eric Barone εργάστηκε για 4,5 χρόνια ολομόναχος σχεδιάζοντας τον κώδικα, τα pixel art γραφικά, τη μουσική και το σενάριο του παιχνιδιού εμπνευσμένος από το Harvest Moon.",
        "funFacts": [
            "Το Stardew Valley έχει πουλήσει πάνω από 30 εκατομμύρια αντίτυπα παγκοσμίως.",
            "Ο Barone συνεχίζει να παρέχει τεράστιες δωρεάν αναβαθμίσεις περιεχομένου στους παίκτες πολλά χρόνια μετά την κυκλοφορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Stardew_Valley",
        "tags": ["gaming", "stardew_valley", "concernedape", "indie", "simulation"]
    },
    {
        "id": "gaming_med_292",
        "text": "Στο παιχνίδι sandbox 'Terraria', ποιο γιγάντιο εφιαλτικό αφεντικό στον Κάτω Κόσμο πρέπει να νικήσει ο παίκτης για να ενεργοποιήσει το 'Hardmode';",
        "correct": "Wall of Flesh (Τοίχος της Σάρκας)",
        "distractors": ["Eye of Cthulhu", "Skeletron Prime", "Moon Lord"],
        "explanation": "Πετώντας την κούκλα Voodoo του οδηγού (Guide Voodoo Doll) στη λάβα του Underworld, εμφανίζεται το Wall of Flesh που σαρώνει οριζόντια την οθόνη.",
        "funFacts": [
            "Η νίκη επί του Wall of Flesh απελευθερώνει τα αρχαία πνεύματα φωτός και σκότους, δημιουργώντας τα biomes Hallow και Underground Corruption/Crimson.",
            "Το Terraria συγκαταλέγεται στα ελάχιστα παιχνίδια στην ιστορία με πάνω από 40 εκατομμύρια πωλήσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Terraria",
        "tags": ["gaming", "terraria", "re_logic", "indie", "sandbox"]
    },
    {
        "id": "gaming_med_293",
        "text": "Ποιο roguelike deck-builder της MegaCrit (2019) καθιέρωσε το είδος όπου οι παίκτες ανεβαίνουν έναν πύργο επιλέγοντας κάρτες και κειμήλια (relics);",
        "correct": "Slay the Spire",
        "distractors": ["Monster Train", "Inscryption", "Balatro"],
        "explanation": "Στο Slay the Spire, οι παίκτες επιλέγουν ανάμεσα σε χαρακτήρες όπως ο Ironclad, η Silent, ο Defect και η Watcher, πολεμώντας τέρατα με συνδυασμούς καρτών.",
        "funFacts": [
            "Το παιχνίδι εισήγαγε τον μηχανισμό πρόθεσης εχθρών (intent system), όπου ο παίκτης βλέπει ακριβώς τι κίνηση θα κάνει ο εχθρός στον επόμενο γύρο.",
            "Το Slay the Spire ενέπνευσε μια ολόκληρη νέα γενιά deckbuilders σε υπολογιστές και κονσόλες."
        ],
        "source": "https://en.wikipedia.org/wiki/Slay_the_Spire",
        "tags": ["gaming", "slay_the_spire", "indie", "card_game", "roguelike"]
    },
    {
        "id": "gaming_med_294",
        "text": "Ποιο είναι το όνομα του μυστηριώδους πλοίου της Εταιρείας Ανατολικών Ινδιών στο ομώνυμο αστυνομικό παζλ του Lucas Pope (2018);",
        "correct": "Obra Dinn",
        "distractors": ["Mary Celeste", "Flying Dutchman", "San Juan"],
        "explanation": "Στο 'Return of the Obra Dinn', ο παίκτης είναι ένας εκτιμητής ασφαλειών που επιβιβάζεται στο ακυβέρνητο πλοίο Obra Dinn για να ανακαλύψει τη μοίρα και των 60 επιβαινόντων.",
        "funFacts": [
            "Ο παίκτης χρησιμοποιεί το μαγικό ρολόι τσέπης 'Memento Mortem' που του επιτρέπει να δει και να περπατήσει μέσα στην ακριβή στιγμή του θανάτου κάθε ανθρώπου.",
            "Το παιχνίδι αποδίδεται με αυθεντικά 1-bit μονοχρωματικά γραφικά εμπνευσμένα από τους πρώτους υπολογιστές Macintosh."
        ],
        "source": "https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn",
        "tags": ["gaming", "obra_dinn", "lucas_pope", "indie", "puzzle"]
    },
    {
        "id": "gaming_med_295",
        "text": "Ποιο είναι το δυστοπικό παιχνίδι συνοριακού ελέγχου του Lucas Pope (2013) όπου ο παίκτης ελέγχει διαβατήρια στη χώρα Arstotzka;",
        "correct": "Papers, Please",
        "distractors": ["Beholder", "Not Tonight", "Orwell"],
        "explanation": "Στο Papers, Please, ο παίκτης εργάζεται ως επιθεωρητής μετανάστευσης στο συνοριακό φυλάκιο του Grestin, προσπαθώντας να συντηρήσει την οικογένειά του υπό ένα αυταρχικό καθεστώς.",
        "funFacts": [
            "Η εμβληματική φράση που συνοδεύει το παιχνίδι είναι: 'Glory to Arstotzka!'.",
            "Ο παίκτης αντιμετωπίζει διαρκώς ηθικά διλήμματα, όπως το αν θα δεχτεί δωροδοκίες ή αν θα επιτρέψει σε πολιτικούς πρόσφυγες να εισέλθουν χωρίς νόμιμα έγγραφα."
        ],
        "source": "https://en.wikipedia.org/wiki/Papers,_Please",
        "tags": ["gaming", "papers_please", "lucas_pope", "indie", "simulation"]
    },
    {
        "id": "gaming_med_296",
        "text": "Στο 'Super Mario RPG: Legend of the Seven Stars' (1996), ποιος μυστηριώδης ξύλινος κούκλος ζωντανεύει από ένα πεφταστέρι και συμμαχεί με τον Mario;",
        "correct": "Geno",
        "distractors": ["Mallow", "Smithy", "Booster"],
        "explanation": "Ο Geno είναι ένα πνεύμα από το Star Road που καταλαμβάνει μια ξύλινη μαριονέτα και μπορεί να εκτοξεύει ακτίνες ενέργειας από τα χέρια του (Geno Beam).",
        "funFacts": [
            "Το παιχνίδι αναπτύχθηκε σε στενή συνεργασία μεταξύ της Square και της Nintendo για το Super Nintendo.",
            "Ο Geno έγινε ένας από τους πιο περιζήτητους χαρακτήρες για προσθήκη στη σειρά Super Smash Bros., εμφανιζόμενος τελικά ως Mii Fighter costume."
        ],
        "source": "https://en.wikipedia.org/wiki/Super_Mario_RPG",
        "tags": ["gaming", "mario", "square", "snes", "rpg", "geno"]
    },
    {
        "id": "gaming_med_297",
        "text": "Ποιος είναι ο πιστός αιλουροειδής σύντροφος του κυνηγού στη σειρά 'Monster Hunter' που μαγειρεύει γεύματα και πολεμάει στο πλευρό του;",
        "correct": "Palico (Felyne)",
        "distractors": ["Palamute", "Poogie", "Moofah"],
        "explanation": "Οι Palicoes ανήκουν στη φυλή των Felyne και είναι ανθρωπόμορφοι γάτοι που προσφέρουν υποστήριξη, θεραπείες και επιθέσεις κατά τη διάρκεια του κυνηγιού.",
        "funFacts": [
            "Στο Monster Hunter Rise (2021) προστέθηκαν και οι πιστοί κυνικοί σύντροφοι Palamutes, τους οποίους οι παίκτες μπορούν να ιππεύουν.",
            "Οι παίκτες μπορούν να ντύσουν τους Palicoes τους με πανοπλίες και όπλα φτιαγμένα από υλικά τεράτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Monster_Hunter",
        "tags": ["gaming", "monster_hunter", "capcom", "palico"]
    },
    {
        "id": "gaming_med_298",
        "text": "Ποια είναι τα δύο αδέλφια πουλιά ντόντο που διαχειρίζονται το αεροδρόμιο Dodo Airlines στο 'Animal Crossing: New Horizons' (2020);",
        "correct": "Orville και Wilbur",
        "distractors": ["Tom και Nook", "Timmy και Tommy", "Blathers και Celeste"],
        "explanation": "Ο Orville εξυπηρετεί στη ρεσεψιόν του αεροδρομίου και ο Wilbur είναι ο πιλότος του υδροπλάνου που μεταφέρει τους παίκτες σε μυστηριώδη νησιά.",
        "funFacts": [
            "Τα ονόματά τους αποτελούν άμεσο φόρο τιμής στους αδελφούς Wright (Orville και Wilbur Wright), τους πρωτοπόρους της αεροπορίας.",
            "Το μότο της αεροπορικής εταιρείας είναι: 'We're not happy until you're happy!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Animal_Crossing:_New_Horizons",
        "tags": ["gaming", "animal_crossing", "nintendo", "switch"]
    },
    {
        "id": "gaming_med_299",
        "text": "Στο 'Final Fantasy VII', ποιο πανίσχυρο διαστημικό ξόρκι επικαλείται ο Sephiroth για να καταστρέψει τον πλανήτη Gaia;",
        "correct": "Meteor (Μετεωρίτης)",
        "distractors": ["Holy", "Ultima", "Flare"],
        "explanation": "Ο Sephiroth χρησιμοποιεί το Black Materia για να καλέσει τον Meteor, εξαναγκάζοντας την Aerith να θυσιαστεί επικαλούμενη το αντίθετο λευκό ξόρκι, Holy.",
        "funFacts": [
            "Το σύμβολο του επερχόμενου Meteor αποτελεί το επίσημο κεντρικό λογότυπο του Final Fantasy VII.",
            "Στο τέλος του παιχνιδιού, το Holy δεν επαρκεί μόνο του για να σταματήσει τον μετεωρίτη και ο ίδιος ο πλανήτης αντιδρά επιστρατεύοντας το Lifestream."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_VII",
        "tags": ["gaming", "final_fantasy", "square_enix", "lore", "sephiroth"]
    },
    {
        "id": "gaming_med_300",
        "text": "Ποιο διαστημικό παιχνίδι στρατηγικής της Subset Games (2012) βάζει τον παίκτη να κυβερνά ένα σκάφος διαφεύγοντας από τον επαναστατικό στόλο;",
        "correct": "FTL: Faster Than Light",
        "distractors": ["Into the Breach", "Everspace", "Starbound"],
        "explanation": "Στο FTL, ο παίκτης διαχειρίζεται τα συστήματα του σκάφους (ενέργεια, ασπίδες, οξυγόνο, όπλα) και το πλήρωμα καθώς πηδά από τομέα σε τομέα.",
        "funFacts": [
            "Το παιχνίδι χρηματοδοτήθηκε επιτυχώς στο Kickstarter συγκεντρώνοντας 20 φορές τον αρχικό στόχο.",
            "Η Subset Games δημιούργησε στη συνέχεια το εξαιρετικό turn-based παιχνίδι τακτικής 'Into the Breach'."
        ],
        "source": "https://en.wikipedia.org/wiki/FTL:_Faster_Than_Light",
        "tags": ["gaming", "ftl", "subset_games", "indie", "sci_fi"]
    },
    {
        "id": "gaming_med_301",
        "text": "Στο παιχνίδι προσομοίωσης εργοστασίων 'Factorio' (2020), τι προσελκύει και εξαγριώνει τα εξωγήινα έντομα (Biters) ώστε να επιτίθενται στις εγκαταστάσεις;",
        "correct": "Η ρύπανση που παράγουν τα εργοστάσια (Pollution)",
        "distractors": ["Το ηλεκτρικό ρεύμα", "Τα ηχητικά κύματα των τρένων", "Τα φωτεινά ραντάρ"],
        "explanation": "Καθώς τα μηχανήματα και οι λέβητες καίνε κάρβουνο, ένα νέφος ρύπανσης απλώνεται στον χάρτη· όταν αγγίξει φωλιές Biters, εκείνα οργανώνουν επιθέσεις.",
        "funFacts": [
            "Ο τελικός στόχος στο Factorio είναι η κατασκευή και εκτόξευση ενός πυραύλου στο διάστημα.",
            "Το μότο της κοινότητας των παικτών για τον εθισμό του παιχνιδιού είναι: 'The factory must grow'."
        ],
        "source": "https://en.wikipedia.org/wiki/Factorio",
        "tags": ["gaming", "factorio", "wube_software", "simulation", "indie"]
    },
    {
        "id": "gaming_med_302",
        "text": "Στο puzzle game 'The Witness' (2016) του Jonathan Blow, τι είδους γρίφους καλείται να λύσει ο παίκτης πάνω σε πάνελ αλλά και στο ίδιο το περιβάλλον του νησιού;",
        "correct": "Γρίφους χάραξης γραμμών σε πλέγματα (Line Puzzles)",
        "distractors": ["Γρίφους συναρμολόγησης γραναζιών", "Γρίφους αντανάκλασης ακτίνων λέιζερ", "Γρίφους μετακίνησης κύβων"],
        "explanation": "Ο παίκτης χαράσσει διαδρομές από ένα σημείο εκκίνησης σε ένα τέλος, ανακαλύπτοντας σταδιακά τους κρυφούς κανόνες και περιβαλλοντικές γραμμές στο τοπίο.",
        "funFacts": [
            "Το παιχνίδι περιλαμβάνει πάνω από 650 γρίφους και δεν διαθέτει ούτε μία γραμμή κειμένου οδηγιών.",
            "Τα περιβαλλοντικά παζλ (Environmental Puzzles) κρύβονται σε δέντρα, ποτάμια και σκιές που αποκαλύπτονται μόνο από συγκεκριμένη οπτική γωνία."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Witness_(2016_video_game)",
        "tags": ["gaming", "the_witness", "jonathan_blow", "indie", "puzzle"]
    },
    {
        "id": "gaming_med_303",
        "text": "Ποιο εφιαλτικό deck-building παιχνίδι του Daniel Mullins (2021) ξεκινά σε μια σκοτεινή καλύβα όπου μια μυστηριώδης φιγούρα (Leshy) αναγκάζει τον παίκτη να παίξει χαρτιά;",
        "correct": "Inscryption",
        "distractors": ["Pony Island", "The Hex", "Buckshot Roulette"],
        "explanation": "Το Inscryption συνδυάζει παιχνίδι καρτών, στοιχεία escape room και ARG μυστηρίου, αλλάζοντας ριζικά μορφή και γραφικά καθώς προχωρά η ιστορία.",
        "funFacts": [
            "Ο παίκτης μπορεί να θυσιάσει δόντια ή ακόμα και το μάτι του με ειδικά εργαλεία για να γείρει την πλάστιγγα της ζυγαριάς υπέρ του.",
            "Το παιχνίδι κέρδισε το κορυφαίο βραβείο Seumas McNally Grand Prize στο Independent Games Festival το 2022."
        ],
        "source": "https://en.wikipedia.org/wiki/Inscryption",
        "tags": ["gaming", "inscryption", "daniel_mullins", "indie", "horror"]
    },
    {
        "id": "gaming_med_304",
        "text": "Ποιο απλό roguelite του Luca Galante (poncle, 2022) με αυτόματες επιθέσεις ενάντια σε χιλιάδες τέρατα δημιούργησε το δημοφιλές υποείδος 'bullet heaven';",
        "correct": "Vampire Survivors",
        "distractors": ["Brotato", "Halls of Torment", "20 Minutes Till Dawn"],
        "explanation": "Στο Vampire Survivors, ο παίκτης ελέγχει μόνο την κίνηση του χαρακτήρα ενώ τα όπλα πυροβολούν αυτόματα, προσπαθώντας να επιβιώσει για 30 λεπτά.",
        "funFacts": [
            "Στο 30ό λεπτό κάθε διαδρομής εμφανίζεται ο ανίκητος Χάρος (Red Death) για να αποτελειώσει τον παίκτη με ένα χτύπημα.",
            "Το παιχνίδι απέσπασε το βραβείο Best Game στα BAFTA Games Awards 2023, επικρατώντας απέναντι σε υπερπαραγωγές εκατομμυρίων δολαρίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Vampire_Survivors",
        "tags": ["gaming", "vampire_survivors", "poncle", "indie", "action"]
    },
    {
        "id": "gaming_med_305",
        "text": "Στο roguevania 'Dead Cells' (2018) της Motion Twin, ποια άμορφη οντότητα ελέγχει τα αποκεφαλισμένα πτώματα φυλακισμένων στο καταραμένο νησί;",
        "correct": "The Beheaded (Ο Ακέφαλος / Homunculus)",
        "distractors": ["The Collector", "The King", "The Alchemist"],
        "explanation": "Ο πρωταγωνιστής είναι ένα πράσινο παρασιτικό πλάσμα (Homunculus) που προσκολλάται σε πτώματα φυλακισμένων και συλλέγει κύτταρα (cells) για μόνιμες αναβαθμίσεις.",
        "funFacts": [
            "Το στούντιο Motion Twin λειτουργεί ως εργατικός συνεταιρισμός (co-op) όπου όλοι οι εργαζόμενοι έχουν ίσο μισθό και δικαίωμα ψήφου.",
            "Το παιχνίδι απέκτησε ένα εξαιρετικό επίσημο expansion σε συνεργασία με την Konami με τίτλο 'Return to Castlevania'."
        ],
        "source": "https://en.wikipedia.org/wiki/Dead_Cells",
        "tags": ["gaming", "dead_cells", "motion_twin", "indie", "roguelite"]
    },
    {
        "id": "gaming_med_306",
        "text": "Στο neo-noir action platformer 'Katana Zero' (2019), ποιο πειραματικό φάρμακο επιτρέπει στον δολοφόνο Zero να χειρίζεται τον χρόνο και να προβλέπει το μέλλον;",
        "correct": "Chronos",
        "distractors": ["Slo-Mo", "Plasmids", "Titan"],
        "explanation": "Το Chronos επιτρέπει στον Zero να επιβραδύνει τον χρόνο και να σχεδιάζει τις κινήσεις του με απόλυτη ακρίβεια, αλλά τα συμπτώματα στέρησης είναι εφιαλτικά.",
        "funFacts": [
            "Κάθε πίστα που παίζει ο παίκτης αποτελεί στην πραγματικότητα την πρόβλεψη στο μυαλό του Zero ('Yes, that will work').",
            "Ο παίκτης μπορεί να διακόπτει τους διαλόγους των χαρακτήρων νωρίτερα, επιλέγοντας πιο επιθετικές απαντήσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Katana_Zero",
        "tags": ["gaming", "katana_zero", "devolver_digital", "indie", "action"]
    },
    {
        "id": "gaming_med_307",
        "text": "Στο 'Outer Wilds', πώς επικοινωνούν και εντοπίζουν ο ένας τον άλλον οι αστροναύτες του προγράμματος Outer Wilds Ventures στο διάστημα;",
        "correct": "Παίζοντας ο καθένας διαφορετικό μουσικό όργανο (Signalscope)",
        "distractors": [
            "Εκπέμποντας ραδιοφωνικά σήματα κώδικα Morse",
            "Ανάβοντας πυρσούς στους πόλους των πλανητών",
            "Αφήνοντας γραπτά σημειώματα σε κάψουλες"
        ],
        "explanation": "Χρησιμοποιώντας το Signalscope, ο παίκτης ακούει το μπάντζο του Riebeck, το φλάουτο του Gabbio, το τύμπανο του Chert και τη φυσαρμόνικα του Feldspar να συνθέτουν μια κοινή μελωδία.",
        "funFacts": [
            "Το μουσικό θέμα των τίτλων τέλους ενώνει όλα τα όργανα των ταξιδιωτών σε ένα αρμονικό τραγούδι γύρω από τη φωτιά.",
            "Το παιχνίδι ξεκίνησε αρχικά ως πτυχιακή εργασία του Alex Beachum στο Πανεπιστήμιο της Νότιας Καλιφόρνιας (USC)."
        ],
        "source": "https://en.wikipedia.org/wiki/Outer_Wilds",
        "tags": ["gaming", "outer_wilds", "mobius_digital", "music", "indie"]
    },
    {
        "id": "gaming_med_308",
        "text": "Στο 'God of War III' (2010), τι απελευθέρωσε ο Kratos όταν άνοιξε το Κουτί της Πανδώρας στο πρώτο παιχνίδι, μολύνοντας τους θεούς του Ολύμπου;",
        "correct": "Τα αρχέγονα Κακά του Τιτανο-Θεϊκού πολέμου (Φόβος, Απληστία, Μίσος)",
        "distractors": ["Τις ψυχές των νεκρών Τιτάνων", "Τον Μαύρο Ήλιο του Κάτω Κόσμου", "Την κατάρα της αθανασίας"],
        "explanation": "Η Αθηνά αποκαλύπτει ότι τα κακά μόλυναν τους θεούς (κάνοντας τον Δία παρανοϊκό από φόβο), ενώ ο Kratos είχε απορροφήσει άθελά του το ισχυρότερο όπλο όλων: την Ελπίδα (Hope).",
        "funFacts": [
            "Στο τέλος του παιχνιδιού, ο Kratos καρφώνει τον εαυτό του με το Blade of Olympus για να χαρίσει την Ελπίδα στην ανθρωπότητα αντί να την παραδώσει στην Αθηνά.",
            "Η μάχη στην αρχή του God of War III διαδραματίζεται πάνω στο κινούμενο σώμα της Γαίας καθώς σκαρφαλώνει στον Όλυμπο."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_III",
        "tags": ["gaming", "god_of_war", "playstation", "santa_monica", "kratos"]
    },
    {
        "id": "gaming_med_309",
        "text": "Στο 'Batman: Arkham City' (2011), από ποια θανατηφόρα ασθένεια πεθαίνει ο Joker αναγκάζοντας τον Batman να αναζητήσει αντίδοτο;",
        "correct": "Δηλητηρίαση από τη χημική ουσία Titan",
        "distractors": ["Έκθεση στο αέριο φόβου του Scarecrow", "Μόλυνση από το αίμα του Ra's al Ghul", "Δηλητηρίαση από το Venom του Bane"],
        "explanation": "Η υπερβολική δόση της ουσίας Titan που πήρε ο Joker στο Arkham Asylum προκάλεσε ανεπανόρθωτη σήψη στο αίμα του, το οποίο μόλυνε και τον Batman.",
        "funFacts": [
            "Στο τέλος του παιχνιδιού, ο Joker καταστρέφει κατά λάθος το μοναδικό φιαλίδιο με το αντίδοτο, με τον Batman να λέει ότι θα τον είχε σώσει παρ' όλα αυτά.",
            "Η εικόνα του Batman να μεταφέρει το άψυχο σώμα του Joker έξω από το Arkham City αποτελεί μια από τις πιο εμβληματικές στιγμές στη σύγχρονη ιστορία του ήρωα."
        ],
        "source": "https://en.wikipedia.org/wiki/Batman:_Arkham_City",
        "tags": ["gaming", "batman", "arkham", "rocksteady", "joker"]
    },
    {
        "id": "gaming_med_310",
        "text": "Ποιο είναι το όνομα του δημοφιλούς roguelike card game με θέμα το πόκερ που δημιουργήθηκε από τον LocalThunk το 2024;",
        "correct": "Balatro",
        "distractors": ["Inscryption", "Slay the Spire", "Stacklands"],
        "explanation": "Στο Balatro, οι παίκτες παίζουν παραδοσιακά χέρια πόκερ συνδυάζοντάς τα με κάρτες Joker που προσφέρουν τρελούς πολλαπλασιαστές πόντων.",
        "funFacts": [
            "Το παιχνίδι ξεπέρασε το ένα εκατομμύριο πωλήσεις μέσα σε λιγότερο από έναν μήνα από την κυκλοφορία του.",
            "Η λέξη 'Balatro' προέρχεται από τα λατινικά και σημαίνει 'γελωτοποιός' ή 'παλιάτσος'."
        ],
        "source": "https://en.wikipedia.org/wiki/Balatro_(video_game)",
        "tags": ["gaming", "balatro", "indie", "roguelike", "localthunk"]
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
    print(f"Loaded {len(questions)} questions for gaming_medium batch 2.")
    validate_and_append("gaming", "medium", 3, questions)

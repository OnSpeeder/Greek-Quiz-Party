# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# 50 pop culture medium questions: pop_culture_med_111 to pop_culture_med_160
QUESTIONS = [
    {
        "id": "pop_culture_med_111",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός υποδύθηκε τον Joker στην ταινία 'Ο Σκοτεινός Ιππότης' (The Dark Knight) του 2008;",
        "answers": ["Χιθ Λέτζερ", "Χοακίν Φίνιξ", "Τζακ Νίκολσον", "Τζάρεντ Λέτο"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Χιθ Λέτζερ έδωσε μια συγκλονιστική ερμηνεία ως Joker στο 'The Dark Knight' του Κρίστοφερ Νόλαν, για την οποία κέρδισε μεταθανάτια το Όσκαρ Β' Ανδρικού Ρόλου.",
        "funFacts": [
            "Ο Λέτζερ κλείστηκε μόνος του σε δωμάτιο ξενοδοχείου για έξι εβδομάδες για να αναπτύξει τη φωνή και τη στάση του σώματος του χαρακτήρα.",
            "Ήταν ο πρώτος ηθοποιός που κέρδισε ποτέ Όσκαρ για ρόλο σε ταινία βασισμένη σε υπερήρωα κόμικ."
        ],
        "source": "https://en.wikipedia.org/wiki/Heath_Ledger",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "batman"]
    },
    {
        "id": "pop_culture_med_112",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο μουσικό συγκρότημα κυκλοφόρησε το άλμπουμ 'Nevermind' το 1991;",
        "answers": ["Pearl Jam", "Nirvana", "Soundgarden", "Alice in Chains"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Nevermind' των Nirvana, με επικεφαλής τον Κερτ Κομπέιν, εκτόξευσε το grunge κίνημα και τη σκηνή του Σιάτλ στην παγκόσμια κορυφή.",
        "funFacts": [
            "Το άλμπουμ εκθρόνισε το 'Dangerous' του Μάικλ Τζάκσον από την πρώτη θέση του Billboard 200 τον Ιανουάριο του 1992.",
            "Το μωρό στο εξώφυλλο του άλμπουμ, ο Σπένσερ Έλντεν, φωτογραφήθηκε σε ηλικία μόλις 4 μηνών."
        ],
        "source": "https://en.wikipedia.org/wiki/Nevermind",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "grunge"]
    },
    {
        "id": "pop_culture_med_113",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος είναι ο δημιουργός της παγκοσμίως επιτυχημένης σειράς manga και anime 'One Piece';",
        "answers": ["Μασάσι Κισιμότο", "Ακίρα Τοριγιάμα", "Εϊτσίρο Όντα", "Χαγιάο Μιγιαζάκι"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Εϊτσίρο Όντα (Eiichiro Oda) ξεκίνησε το 'One Piece' το 1997 στο περιοδικό Weekly Shonen Jump, δημιουργώντας το πιο επιτυχημένο manga στην ιστορία.",
        "funFacts": [
            "Το One Piece κατέχει το ρεκόρ Γκίνες για τα περισσότερα αντίτυπα που έχουν εκδοθεί για την ίδια σειρά κόμικς από έναν μόνο συγγραφέα.",
            "Έχει πουλήσει πάνω από 516 εκατομμύρια αντίτυπα παγκοσμίως."
        ],
        "source": "https://en.wikipedia.org/wiki/One_Piece",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "anime", "manga"]
    },
    {
        "id": "pop_culture_med_114",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ποπ σταρ έγινε γνωστή με το ψευδώνυμο 'Hannah Montana' στην ομώνυμη τηλεοπτική σειρά του Disney Channel;",
        "answers": ["Σελίνα Γκόμεζ", "Ντέμι Λοβάτο", "Αριάνα Γκράντε", "Μάιλι Σάιρους"],
        "correctAnswerIndex": 3,
        "explanation": "Η Μάιλι Σάιρους πρωταγωνίστησε ως η έφηβη Μάιλι Στιούαρτ που ζούσε διπλή ζωή ως η διάσημη ποπ σταρ Χάνα Μοντάνα από το 2006 έως το 2011.",
        "funFacts": [
            "Ο πραγματικός της πατέρας, ο τραγουδιστής κάντρι Μπίλι Ρέι Σάιρους, υποδύθηκε τον πατέρα της και στη σειρά.",
            "Το πρώτο της επίσημο όνομα ήταν Destiny Hope Cyrus πριν το αλλάξει νόμιμα σε Miley."
        ],
        "source": "https://en.wikipedia.org/wiki/Hannah_Montana",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "disney"]
    },
    {
        "id": "pop_culture_med_115",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος σκηνοθέτησε την καλτ ταινία 'Pulp Fiction' του 1994;",
        "answers": ["Κουέντιν Ταραντίνο", "Μάρτιν Σκορσέζε", "Ντέιβιντ Φίντσερ", "Στίβεν Σπίλμπεργκ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Κουέντιν Ταραντίνο σκηνοθέτησε το 'Pulp Fiction', κερδίζοντας τον Χρυσό Φοίνικα στο Φεστιβάλ Καννών και το Όσκαρ Καλύτερου Πρωτότυπου Σεναρίου.",
        "funFacts": [
            "Η ταινία αναβίωσε θεαματικά την καριέρα του Τζον Τραβόλτα στο Χόλιγουντ.",
            "Το περίφημο πορτοφόλι του Jules (Σάμιουελ Τζάκσον) με την επιγραφή 'Bad Motherfucker' ανήκε προσωπικά στον Ταραντίνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Pulp_Fiction",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "tarantino"]
    },
    {
        "id": "pop_culture_med_116",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια τηλεοπτική σειρά φαντασίας του HBO βασίστηκε στη σειρά βιβλίων 'Το Τραγούδι της Φωτιάς και του Πάγου' του Τζορτζ Ρ. Ρ. Μάρτιν;",
        "answers": ["The Witcher", "Game of Thrones", "The Wheel of Time", "Outlander"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Game of Thrones' έκανε πρεμιέρα το 2011 στο HBO και αποτέλεσε ένα από τα μεγαλύτερα παγκόσμια τηλεοπτικά φαινόμενα της δεκαετίας.",
        "funFacts": [
            "Η σειρά κέρδισε συνολικά 59 βραβεία Emmy, ρεκόρ για δραματική σειρά prime time.",
            "Η τεχνητή γλώσσα Ντοθράκι που ακούγεται στη σειρά δημιουργήθηκε από τον γλωσσολόγο Ντέιβιντ Τζ. Πίτερσον."
        ],
        "source": "https://en.wikipedia.org/wiki/Game_of_Thrones",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "fantasy"]
    },
    {
        "id": "pop_culture_med_117",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είδος κατοικίδιου ζώου ήταν ο 'Γκάρφιλντ' στο διάσημο κόμικ του Τζιμ Ντέιβις;",
        "answers": ["Σκύλος", "Κουνέλι", "Γάτος", "Παπαγάλος"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Γκάρφιλντ είναι ένας πορτοκαλί, τεμπέλης και κυνικός γάτος που λατρεύει τα λαζάνια και μισεί τις Δευτέρες.",
        "funFacts": [
            "Ο Garfield κατέχει το ρεκόρ Γκίνες ως το πιο ευρέως αναδημοσιευμένο κόμικ στριπ στον κόσμο, εμφανιζόμενο σε πάνω από 2.500 εφημερίδες.",
            "Ο Τζιμ Ντέιβις ονόμασε τον Garfield από τον παππού του, Τζέιμς Γκάρφιλντ Ντέιβις, ο οποίος είχε πάρει το όνομά του από τον πρόεδρο των ΗΠΑ Τζέιμς Γκάρφιλντ."
        ],
        "source": "https://en.wikipedia.org/wiki/Garfield",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics"]
    },
    {
        "id": "pop_culture_med_118",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το πραγματικό όνομα της τραγουδίστριας Lady Gaga;",
        "answers": ["Κέιτι Πέρι", "Οντρέι Χέπμπορν", "Νόρμα Τζιν Μόρτενσον", "Στέφανι Τζερμανότα"],
        "correctAnswerIndex": 3,
        "explanation": "Το πλήρες όνομα της Lady Gaga είναι Στέφανι Τζοάν Αντζελίνα Τζερμανότα (Stefani Joanne Angelina Germanotta).",
        "funFacts": [
            "Το καλλιτεχνικό της ψευδώνυμο 'Lady Gaga' είναι εμπνευσμένο από το τραγούδι 'Radio Ga Ga' των Queen.",
            "Είναι η πρώτη γυναίκα στην ιστορία που κέρδισε Όσκαρ, Grammy, BAFTA και Χρυσή Σφαίρα την ίδια χρονιά (για το τραγούδι 'Shallow' το 2019)."
        ],
        "source": "https://en.wikipedia.org/wiki/Lady_Gaga",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "celebrities"]
    },
    {
        "id": "pop_culture_med_119",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο animation στούντιο δημιούργησε τις ταινίες 'Toy Story', 'Finding Nemo' και 'Up';",
        "answers": ["Pixar", "DreamWorks", "Illumination", "Blue Sky Studios"],
        "correctAnswerIndex": 0,
        "explanation": "Η Pixar Animation Studios πρωτοπόρησε στον τομέα των ψηφιακών κινουμένων σχεδίων κυκλοφορώντας το Toy Story το 1995, την πρώτη ταινία μεγάλου μήκους εξ ολοκλήρου από υπολογιστή.",
        "funFacts": [
            "Ο Στιβ Τζομπς ήταν ο κύριος χρηματοδότης και πρόεδρος της Pixar πριν την εξαγορά της από τη Disney το 2006.",
            "Η περίφημη μασκότ της Pixar είναι μια επιτραπέζια λάμπα με το όνομα Luxo Jr."
        ],
        "source": "https://en.wikipedia.org/wiki/Pixar",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "pixar"]
    },
    {
        "id": "pop_culture_med_120",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ηρωίδα υποδύεται η Τζένιφερ Λόρενς στη σειρά κινηματογραφικών ταινιών 'The Hunger Games';",
        "answers": ["Μπέλα Σουάν", "Κάτνις Έβερντιν", "Τρις Πράιορ", "Χερμιόνη Γκρέιντζερ"],
        "correctAnswerIndex": 1,
        "explanation": "Η Τζένιφερ Λόρενς υποδύθηκε την Κάτνις Έβερντιν (Katniss Everdeen), τη νεαρή τοξοβόλο από τον Τομέα 12, βασισμένη στην τριλογία βιβλίων της Σούζαν Κόλινς.",
        "funFacts": [
            "Η Λόρενς εκπαιδεύτηκε στην τοξοβολία από την τέσσερις φορές Ολυμπιονίκη Χατούνα Λόριγκ.",
            "Η επιτυχία της ταινίας κατέστησε την Κάτνις την πιο κερδοφόρα ηρωίδα δράσης όλων των εποχών στο παγκόσμιο box office."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Hunger_Games_(film_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "hunger_games"]
    },
    {
        "id": "pop_culture_med_121",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διαστημικού σκάφους του Χαν Σόλο και του Τσουμπάκα στο σύμπαν του Star Wars;",
        "answers": ["Star Destroyer", "X-Wing", "Millennium Falcon", "TIE Fighter"],
        "correctAnswerIndex": 2,
        "explanation": "Το Millennium Falcon (Γεράκι της Χιλιετίας) είναι ένα βαριά τροποποιημένο φορτηγό σκάφος YT-1300, διάσημο ως το γρηγορότερο σκάφος στον γαλαξία.",
        "funFacts": [
            "Ο Τζορτζ Λούκας εμπνεύστηκε το αρχικό σχήμα του Millennium Falcon από ένα μισοφαγωμένο χάμπουργκερ με μια ελιά καρφωμένη στο πλάι.",
            "Ο Χαν Σόλο καυχιέται ότι το σκάφος έκανε τη διαδρομή Κέσελ (Kessel Run) σε λιγότερο από 12 παρσέκ."
        ],
        "source": "https://en.wikipedia.org/wiki/Millennium_Falcon",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "star_wars", "sci_fi"]
    },
    {
        "id": "pop_culture_med_122",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το δημοφιλές reality show μόδας στο οποίο μοντέλα διαγωνίζονται υπό την καθοδήγηση της Τάιρα Μπανκς;",
        "answers": ["Project Runway", "RuPaul's Drag Race", "The Voice", "America's Next Top Model"],
        "correctAnswerIndex": 3,
        "explanation": "Το America's Next Top Model (ANTM) δημιουργήθηκε και παρουσιάστηκε από το supermodel Τάιρα Μπανκς από το 2003 έως το 2018.",
        "funFacts": [
            "Η Τάιρα Μπανκς εισήγαγε στην ποπ κουλτούρα τον όρο 'smize' (χαμόγελο με τα μάτια).",
            "Το franchise μεταφέρθηκε σε δεκάδες χώρες σε όλο τον κόσμο, συμπεριλαμβανομένης της Ελλάδας (GNTM)."
        ],
        "source": "https://en.wikipedia.org/wiki/America%27s_Next_Top_Model",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "reality"]
    },
    {
        "id": "pop_culture_med_123",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος βρετανός ηθοποιός υποδύεται τον ιδιόρρυθμο ντετέκτιβ Σέρλοκ Χολμς στη σειρά 'Sherlock' του BBC (2010-2017);",
        "answers": ["Μπένεντικτ Κάμπερμπατς", "Μάρτιν Φρίμαν", "Τομ Χίντλστον", "Έντι Ρέντμεϊν"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μπένεντικτ Κάμπερμπατς υποδύθηκε τον σύγχρονο Σέρλοκ Χολμς, ρόλος που τον εκτόξευσε στη διεθνή αναγνωρισιμότητα.",
        "funFacts": [
            "Ο συμπαίκτης του Μάρτιν Φρίμαν, που υποδύθηκε τον Δρ. Γουάτσον, έπαιξε αργότερα μαζί του στην τριλογία του 'Hobbit'.",
            "Η σειρά μεταφέρει τις κλασικές ιστορίες του Σερ Άρθουρ Κόναν Ντόιλ στο σύγχρονο Λονδίνο του 21ου αιώνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Sherlock_(TV_series)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "sherlock"]
    },
    {
        "id": "pop_culture_med_124",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βιντεοπαιχνίδι battle royale της Epic Games έγινε παγκόσμιο πολιτιστικό φαινόμενο από το 2017;",
        "answers": ["Apex Legends", "Fortnite", "PUBG", "Call of Duty: Warzone"],
        "correctAnswerIndex": 1,
        "explanation": "Το Fortnite Battle Royale κυκλοφόρησε τον Σεπτέμβριο του 2017 και εξελίχθηκε σε κοινωνικό και ποπ φαινόμενο με εκατοντάδες εκατομμύρια παίκτες.",
        "funFacts": [
            "Οι χοροί (emotes) του Fortnite, όπως το 'Floss', έγιναν viral σε σχολεία και αθλητικούς αγώνες παγκοσμίως.",
            "Το παιχνίδι έχει φιλοξενήσει ζωντανές εικονικές συναυλίες καλλιτεχνών όπως ο Τράβις Σκοτ και η Αριάνα Γκράντε με δεκάδες εκατομμύρια θεατές."
        ],
        "source": "https://en.wikipedia.org/wiki/Fortnite_Battle_Royale",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "fortnite"]
    },
    {
        "id": "pop_culture_med_125",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη ηθοποιός υποδύθηκε τη Ρέιτσελ Γκριν στη θρυλική κωμική σειρά 'Τα Φιλαράκια' (Friends);",
        "answers": ["Κόρτνεϊ Κοξ", "Λίζα Κούντροου", "Τζένιφερ Άνιστον", "Σάρα Τζέσικα Πάρκερ"],
        "correctAnswerIndex": 2,
        "explanation": "Η Τζένιφερ Άνιστον υποδύθηκε τη Ρέιτσελ Γκριν και για τον ρόλο αυτό κέρδισε βραβείο Emmy και Χρυσή Σφαίρα.",
        "funFacts": [
            "Το χαρακτηριστικό κούρεμα της Ρέιτσελ τη δεκαετία του '90 έγινε παγκόσμια μόδα και έμεινε γνωστό ως 'The Rachel'.",
            "Η ίδια η Άνιστον έχει δηλώσει αργότερα ότι δυσκολευόταν να συντηρήσει αυτό το χτένισμα μόνη της."
        ],
        "source": "https://en.wikipedia.org/wiki/Jennifer_Aniston",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "friends"]
    },
    {
        "id": "pop_culture_med_126",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του φανταστικού βασιλείου στο οποίο διαδραματίζεται η ταινία κινουμένων σχεδίων 'Frozen' της Disney;",
        "answers": ["Κορώνα", "Αγραμπά", "Ατλαντίδα", "Αρεντέλ"],
        "correctAnswerIndex": 3,
        "explanation": "Το Frozen διαδραματίζεται στο σκανδιναβικής έμπνευσης βασίλειο της Αρεντέλ (Arendelle), πατρίδα των πριγκιπισσών Έλσα και Άννα.",
        "funFacts": [
            "Οι δημιουργοί της ταινίας επισκέφθηκαν τη Νορβηγία για να αντλήσουν έμπνευση από τα τοπία, τα φιόρδ και την παραδοσιακή αρχιτεκτονική.",
            "Το τραγούδι 'Let It Go' κέρδισε το Όσκαρ Καλύτερου Πρωτότυπου Τραγουδιού το 2014."
        ],
        "source": "https://en.wikipedia.org/wiki/Frozen_(2013_film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "disney"]
    },
    {
        "id": "pop_culture_med_127",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο superhero franchise ανήκει στον δισεκατομμυριούχο Τόνι Σταρκ;",
        "answers": ["Iron Man", "Batman", "Captain America", "Doctor Strange"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Τόνι Σταρκ είναι ο Iron Man στο σύμπαν της Marvel, τον οποίο ενσάρκωσε με τεράστια επιτυχία ο Ρόμπερτ Ντάουνι Τζούνιορ από το 2008.",
        "funFacts": [
            "Ο Σταν Λι εμπνεύστηκε εν μέρει τον χαρακτήρα του Τόνι Σταρκ από τον επιχειρηματία και αεροπόρο Χάουαρντ Χιουζ.",
            "Η ταινία Iron Man (2008) αποτέλεσε την αφετηρία του κινηματογραφικού σύμπαντος της Marvel (MCU)."
        ],
        "source": "https://en.wikipedia.org/wiki/Iron_Man",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "superheroes"]
    },
    {
        "id": "pop_culture_med_128",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο κορεατικό τραγούδι του Psy έγινε το πρώτο βίντεο στην ιστορία του YouTube που ξεπέρασε το 1 δισεκατομμύριο προβολές το 2012;",
        "answers": ["Dynamite", "Gangnam Style", "Gentleman", "Ddu-Du Ddu-Du"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Gangnam Style' του Νοτιοκορεάτη ράπερ Psy κυκλοφόρησε τον Ιούλιο του 2012 και έσπασε το φράγμα του 1 δισεκατομμυρίου προβολών τον Δεκέμβριο του 2012.",
        "funFacts": [
            "Η τεράστια επισκεψιμότητα του βίντεο ανάγκασε το YouTube να αναβαθμίσει τον μετρητή προβολών του από 32-bit ακέραιο σε 64-bit.",
            "Ο χορός των 'αόρατων αλόγων' του Psy υιοθετήθηκε από πολιτικούς, αθλητές και διασημότητες σε όλο τον κόσμο."
        ],
        "source": "https://en.wikipedia.org/wiki/Gangnam_Style",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "youtube", "kpop"]
    },
    {
        "id": "pop_culture_med_129",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του σχολείου μαγείας στο οποίο φοιτά ο Χάρι Πότερ;",
        "answers": ["Ντάρμστρανγκ", "Μπομπατόν", "Χόγκουαρτς", "Ίλβερμορνι"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Χάρι Πότερ φοιτά στο Hogwarts School of Witchcraft and Wizardry (Σχολή Χόγκουαρτς για Μαγείες και Ξόρκια), ιδρυμένο στη Σκωτία.",
        "funFacts": [
            "Το Χόγκουαρτς χωρίζεται σε τέσσερις κοιτώνες: Γκρίφιντορ, Χάφλπαφ, Ρέιβενκλο και Σλίθεριν.",
            "Το μότο του σχολείου στα λατινικά είναι 'Draco Dormiens Nunquam Titillandus' (Ποτέ μην γαργαλάς έναν δράκο που κοιμάται)."
        ],
        "source": "https://en.wikipedia.org/wiki/Hogwarts",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "harry_potter", "fantasy"]
    },
    {
        "id": "pop_culture_med_130",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του πιστού σκύλου του Τεντέν στα κόμικς του Ερζέ;",
        "answers": ["Ραντανπλάν", "Ιντεφίξ", "Σνούπι", "Μιλού"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Μιλού (Milou, γνωστός ως Snowy στα αγγλικά) είναι ένα λευκό Fox Terrier που συνοδεύει πιστά τον νεαρό ρεπόρτερ Τεντέν.",
        "funFacts": [
            "Ο Ερζέ ονόμασε τον σκύλο από το υποκοριστικό της πρώτης του συντρόφου, Μαρί-Λουίζ Βαν Κούτσεν.",
            "Ο Μιλού συχνά μιλάει με σκέψεις που διαβάζει ο αναγνώστης και έχει αδυναμία στο ουίσκι Loch Lomond."
        ],
        "source": "https://en.wikipedia.org/wiki/Snowy_(character)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics", "tintin"]
    },
    {
        "id": "pop_culture_med_131",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο συγκρότημα K-pop έγινε το πρώτο κορεατικό σχήμα που κατέκτησε την πρώτη θέση στο Billboard Hot 100 των ΗΠΑ με το τραγούδι 'Dynamite' το 2020;",
        "answers": ["BTS", "Blackpink", "EXO", "Stray Kids"],
        "correctAnswerIndex": 0,
        "explanation": "Οι BTS (Bangtan Sonyeondan) έγραψαν ιστορία τον Σεπτέμβριο του 2020 όταν το αγγλόφωνο single τους 'Dynamite' έκανε ντεμπούτο στο νούμερο 1 του Billboard Hot 100.",
        "funFacts": [
            "Η επίσημη βάση θαυμαστών των BTS ονομάζεται 'ARMY' (Adorable Representative M.C. for Youth).",
            "Οι BTS ήταν οι πρώτοι Νοτιοκορεάτες καλλιτέχνες που έλαβαν υποψηφιότητα για βραβείο Grammy."
        ],
        "source": "https://en.wikipedia.org/wiki/BTS",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "kpop"]
    },
    {
        "id": "pop_culture_med_132",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον εμβληματικό πράκτορα James Bond σε πέντε ταινίες από το 2006 έως το 2021;",
        "answers": ["Πιρς Μπρόσναν", "Ντάνιελ Κρεγκ", "Σον Κόνερι", "Ρότζερ Μουρ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Ντάνιελ Κρεγκ ξεκίνησε τη θητεία του ως 007 στο 'Casino Royale' (2006) και την ολοκλήρωσε στο 'No Time to Die' (2021).",
        "funFacts": [
            "Όταν ανακοινώθηκε αρχικά ο Κρεγκ το 2005, υπήρξαν έντονες αντιδράσεις από μερίδα κοινού επειδή ήταν ξανθός.",
            "Η ταινία Skyfall (2012) με τον Κρεγκ έγινε η πιο εμπορική ταινία Bond όλων των εποχών, ξεπερνώντας το 1,1 δισεκατομμύριο δολάρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Daniel_Craig",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "james_bond"]
    },
    {
        "id": "pop_culture_med_133",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο franchise ταινιών επιστημονικής φαντασίας παρουσιάζει τον 'Neo', τον 'Morpheus' και την 'Trinity';",
        "answers": ["Terminator", "Blade Runner", "The Matrix", "Inception"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'The Matrix' (1999) των αδελφών Γουατσόφσκι αποτελεί σταθμό στην ιστορία του κινηματογράφου δράσης και επιστημονικής φαντασίας.",
        "funFacts": [
            "Η πρωτοποριακή τεχνική λήψης 'bullet time' με πολλαπλές κάμερες σε κυκλική διάταξη επηρέασε δεκάδες ταινίες και βιντεοπαιχνίδια.",
            "Η επιλογή ανάμεσα στο κόκκινο και το μπλε χάπι έχει καταστεί δημοφιλής μεταφορά στην ποπ κουλτούρα και τη φιλοσοφία."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Matrix",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "sci_fi"]
    },
    {
        "id": "pop_culture_med_134",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ποπ τραγουδίστρια κυκλοφόρησε τα επιτυχημένα άλμπουμ '1989', 'Reputation' και 'Midnights';",
        "answers": ["Αντέλ", "Μπίλι Άιλις", "Ντούα Λίπα", "Τέιλορ Σουίφτ"],
        "correctAnswerIndex": 3,
        "explanation": "Η Τέιλορ Σουίφτ είναι μία από τις πιο επιτυχημένες και επιδραστικές καλλιτέχνιδες του 21ου αιώνα, με ρεκόρ πωλήσεων και βραβείων.",
        "funFacts": [
            "Είναι η μόνη καλλιτέχνιδα που έχει κερδίσει 4 φορές το βραβείο Grammy για το Άλμπουμ της Χρονιάς.",
            "Η παγκόσμια περιοδεία της 'The Eras Tour' (2023-2024) έγινε η πρώτη συναυλιακή περιοδεία στην ιστορία που ξεπέρασε το 1 δισεκατομμύριο δολάρια σε εισπράξεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Taylor_Swift",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "taylor_swift"]
    },
    {
        "id": "pop_culture_med_135",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ήταν ο δημιουργός του χαρακτήρα του Μπάτμαν για την DC Comics το 1939;",
        "answers": ["Μπομπ Κέιν και Μπιλ Φίνγκερ", "Σταν Λι και Τζακ Κίρμπι", "Τζέρι Σίγκελ και Τζο Σούστερ", "Στιβ Ντίτκο"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Μπομπ Κέιν και ο σεναριογράφος Μπιλ Φίνγκερ δημιούργησαν τον Μπάτμαν, ο οποίος έκανε το ντεμπούτο του στο Detective Comics #27 τον Μάιο του 1939.",
        "funFacts": [
            "Ο Μπιλ Φίνγκερ ήταν υπεύθυνος για τη σκοτεινή στολή, τη μάσκα με τα αυτιά νυχτερίδας και την ιστορία του Μπρους Γουέιν.",
            "Για δεκαετίες μόνο ο Μπομπ Κέιν αναφερόταν επίσημα ως δημιουργός, μέχρι το 2015 όταν η DC Comics αναγνώρισε επίσημα τον Φίνγκερ."
        ],
        "source": "https://en.wikipedia.org/wiki/Batman",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics", "batman"]
    },
    {
        "id": "pop_culture_med_136",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια τηλεοπτική σειρά επιστημονικής φαντασίας του Netflix διαδραματίζεται στην πόλη Χόκινς της Ιντιάνα τη δεκαετία του '80;",
        "answers": ["Dark", "Stranger Things", "Black Mirror", "The Umbrella Academy"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Stranger Things' των αδελφών Duffer έκανε πρεμιέρα το 2016, συνδυάζοντας νοσταλγία των 80s, υπερφυσικά μυστήρια και αναφορές στον Στίβεν Κινγκ και τον Σπίλμπεργκ.",
        "funFacts": [
            "Η παράλληλη σκοτεινή διάσταση στη σειρά ονομάζεται 'Upside Down' (Ανάποδος Κόσμος).",
            "Η εμφάνιση του τραγουδιού 'Running Up That Hill' της Κέιτ Μπους στην 4η σεζόν το επανέφερε στο νούμερο 1 των charts μετά από 37 χρόνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Stranger_Things",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "stranger_things"]
    },
    {
        "id": "pop_culture_med_137",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου καφέ όπου συναντιούνται καθημερινά οι χαρακτήρες στη σειρά 'Τα Φιλαράκια';",
        "answers": ["Monk's Diner", "MacLaren's Pub", "Central Perk", "Café Nervosa"],
        "correctAnswerIndex": 2,
        "explanation": "Το Central Perk είναι το φανταστικό καφέ στο Greenwich Village της Νέας Υόρκης, όπου εργάζονταν η Ρέιτσελ και ο Γκάνθερ.",
        "funFacts": [
            "Ο περίφημος πορτοκαλί καναπές του Central Perk βρέθηκε τυχαία στο υπόγειο των στούντιο της Warner Bros.",
            "Αντίγραφα του Central Perk έχουν ανοίξει ως πραγματικά καφέ σε πόλεις όπως το Λονδίνο, η Νέα Υόρκη και το Σίδνεϊ."
        ],
        "source": "https://en.wikipedia.org/wiki/Central_Perk",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "friends"]
    },
    {
        "id": "pop_culture_med_138",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο διάσημο παιχνίδι καρτών της Mattel απαιτεί από τους παίκτες να φωνάξουν το όνομά του όταν τους απομένει μόνο μία κάρτα;",
        "answers": ["Phase 10", "Skip-Bo", "Exploding Kittens", "UNO"],
        "correctAnswerIndex": 3,
        "explanation": "Το UNO δημιουργήθηκε το 1971 από τον Μερλ Ρόμπινς στο Οχάιο και αποτελεί ένα από τα πιο δημοφιλή παιχνίδια καρτών στον κόσμο.",
        "funFacts": [
            "Αν ένας παίκτης δεν φωνάξει 'UNO' πριν παίξει ο επόμενος και τον πιάσουν, αναγκάζεται να τραβήξει δύο κάρτες ποινής.",
            "Η Mattel έχει επιβεβαιώσει επίσημα ότι δεν επιτρέπεται να στοιβάζονται κάρτες Draw Two (+2) πάνω σε Draw Four (+4), αν και πολλοί παίζουν με παραλλαγμένους κανόνες."
        ],
        "source": "https://en.wikipedia.org/wiki/Uno_(card_game)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "board_games", "uno"]
    },
    {
        "id": "pop_culture_med_139",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια βραβευμένη με Όσκαρ ηθοποιός ενσάρκωσε την Μπάρμπι στην ομώνυμη live-action ταινία του 2023 της Γκρέτα Γκέργουιγκ;",
        "answers": ["Μάργκο Ρόμπι", "Έμμα Στόουν", "Σίρσα Ρόναν", "Αν Χάθαγουεϊ"],
        "correctAnswerIndex": 0,
        "explanation": "Η Αυστραλή ηθοποιός Μάργκο Ρόμπι πρωταγωνίστησε ως η Στερεοτυπική Μπάρμπι στην ταινία 'Barbie', η οποία ξεπέρασε το 1,44 δισεκατομμύριο δολάρια σε εισπράξεις.",
        "funFacts": [
            "Η ταυτόχρονη κυκλοφορία του 'Barbie' και του 'Oppenheimer' δημιούργησε το παγκόσμιο φαινόμενο 'Barbenheimer'.",
            "Η παραγωγή της ταινίας προκάλεσε παγκόσμια έλλειψη στη φθορίζουσα ροζ απόχρωση μπογιάς της εταιρείας Rosco."
        ],
        "source": "https://en.wikipedia.org/wiki/Barbie_(film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "barbie"]
    },
    {
        "id": "pop_culture_med_140",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το είδος ζώου του 'Master Shifu' στη σειρά ταινιών κινουμένων σχεδίων 'Kung Fu Panda';",
        "answers": ["Γιγάντιο Πάντα", "Κόκκινο Πάντα", "Λεοπάρδαλη του Χιονιού", "Ασβός"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Master Shifu είναι ένα κόκκινο πάντα (Ailurus fulgens), παρόλο που πολλοί θεατές τον περνούν λανθασμένα για ρακούν ή αλεπού.",
        "funFacts": [
            "Η λέξη 'Shifu' στα κινεζικά (师傅) σημαίνει κυριολεκτικά 'δάσκαλος' ή 'μάστερ'.",
            "Τη φωνή του Shifu στην αγγλική έκδοση δανείζει ο διάσημος ηθοποιός Ντάστιν Χόφμαν."
        ],
        "source": "https://en.wikipedia.org/wiki/Kung_Fu_Panda_(film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "animation", "kung_fu_panda"]
    },
    {
        "id": "pop_culture_med_141",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο άλμπουμ του Μάικλ Τζάκσον που κυκλοφόρησε το 1982 παραμένει το άλμπουμ με τις μεγαλύτερες πωλήσεις όλων των εποχών;",
        "answers": ["Bad", "Off the Wall", "Thriller", "Dangerous"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Thriller' του Μάικλ Τζάκσον, σε παραγωγή Κουίνσι Τζόουνς, έχει πουλήσει εκτιμώμενα 70 εκατομμύρια αντίτυπα παγκοσμίως.",
        "funFacts": [
            "Το ομώνυμο 14λεπτο μουσικό βίντεο σε σκηνοθεσία Τζον Λάντις άλλαξε ριζικά τη μορφή των μουσικών βίντεο κλιπ.",
            "Το άλμπουμ απέφερε επτά top-10 singles στο Billboard Hot 100, συμπεριλαμβανομένων των 'Billie Jean' και 'Beat It'."
        ],
        "source": "https://en.wikipedia.org/wiki/Thriller_(album)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "michael_jackson"]
    },
    {
        "id": "pop_culture_med_142",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος είναι ο κύριος κακός και άρχοντας του Μόρντορ στην τριλογία 'Ο Άρχοντας των Δαχτυλιδιών' του Τζ. Ρ. Ρ. Τόλκιν;",
        "answers": ["Σάρουμαν", "Γκόλουμ", "Μέλκορ", "Σάουρον"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Σάουρον είναι ο Σκοτεινός Άρχοντας του Μόρντορ και ο κατασκευαστής του Ενός Δαχτυλιδιού με σκοπό την υποδούλωση της Μέσης Γης.",
        "funFacts": [
            "Ο Σάουρον ήταν αρχικά ένας ισχυρός Μάια (πνεύμα) της τάξης του Αούλε πριν διαφθαρεί από τον Μόργκοθ.",
            "Στις ταινίες του Πίτερ Τζάκσον, ο Σάουρον απεικονίζεται κυρίως ως ένα τεράστιο, φλεγόμενο μάτι στην κορυφή του πύργου Μπάραντ-ντουρ."
        ],
        "source": "https://en.wikipedia.org/wiki/Sauron",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "fantasy", "lord_of_the_rings"]
    },
    {
        "id": "pop_culture_med_143",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη πλατφόρμα streaming ξεκίνησε τη λειτουργία της το 1997 ως υπηρεσία ενοικίασης DVD μέσω ταχυδρομείου;",
        "answers": ["Netflix", "Hulu", "Amazon Prime", "Disney+"],
        "correctAnswerIndex": 0,
        "explanation": "Το Netflix ιδρύθηκε από τους Ριντ Χέιστινγκς και Μαρκ Ράντολφ το 1997 στέλνοντας DVD με το ταχυδρομείο, προτού ξεκινήσει το streaming το 2007.",
        "funFacts": [
            "Το 2000, η Blockbuster είχε την ευκαιρία να εξαγοράσει το Netflix για μόλις 50 εκατομμύρια δολάρια, αλλά απέρριψε την πρόταση.",
            "Η πρώτη πρωτότυπη σειρά παραγωγής του Netflix ήταν το πολιτικό δράμα 'House of Cards' το 2013."
        ],
        "source": "https://en.wikipedia.org/wiki/Netflix",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tech", "streaming", "netflix"]
    },
    {
        "id": "pop_culture_med_144",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος σκηνοθέτης είναι γνωστός για ταινίες όπως τα 'Inception', 'Interstellar', 'Memento' και 'Oppenheimer';",
        "answers": ["Ντενί Βιλνέβ", "Κρίστοφερ Νόλαν", "Ντέιβιντ Φίντσερ", "Ρίντλεϊ Σκοτ"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Κρίστοφερ Νόλαν είναι ένας από τους πιο επιδραστικούς δημιουργούς του σύγχρονου σινεμά, γνωστός για τη χρήση πρακτικών εφέ και μη γραμμικής αφήγησης.",
        "funFacts": [
            "Ο Νόλαν κέρδισε τα πρώτα του Όσκαρ Σκηνοθεσίας και Καλύτερης Ταινίας για το 'Oppenheimer' το 2024.",
            "Είναι διάσημος για την επιμονή του να γυρίζει ταινίες σε φιλμ 70mm IMAX και να αποφεύγει όσο το δυνατόν τα ψηφιακά εφέ (CGI)."
        ],
        "source": "https://en.wikipedia.org/wiki/Christopher_Nolan",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "nolan"]
    },
    {
        "id": "pop_culture_med_145",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του μαγικού σπαθιού του Βασιλιά Αρθούρου στους κελτικούς και μεσαιωνικούς θρύλους;",
        "answers": ["Αντούριλ", "Γκλάμντρινγκ", "Εξκάλιμπερ", "Στινγκ"],
        "correctAnswerIndex": 2,
        "explanation": "Το Εξκάλιμπερ (Excalibur) είναι το θρυλικό σπαθί του Βασιλιά Αρθούρου, που συχνά ταυτίζεται ή συνδέεται με την Κυρά της Λίμνης.",
        "funFacts": [
            "Σε πολλές πρώιμες παραδόσεις, το σπαθί που τράβηξε ο Αρθούρος από τον βράχο διακρίνεται από το Εξκάλιμπερ που του έδωσε αργότερα η Κυρά της Λίμνης.",
            "Η θήκη του Εξκάλιμπερ λεγόταν ότι προστάτευε τον κάτοχό της από κάθε αιμορραγία και θανάσιμο τραύμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Excalibur",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "mythology", "legends"]
    },
    {
        "id": "pop_culture_med_146",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά βιντεοπαιχνιδιών της Nintendo παρουσιάζει τον Link, την Πριγκίπισσα Zelda και το Triforce;",
        "answers": ["Super Mario", "Metroid", "Fire Emblem", "The Legend of Zelda"],
        "correctAnswerIndex": 3,
        "explanation": "Η σειρά The Legend of Zelda δημιουργήθηκε από τον Σιγκέρου Μιγιαμότο και τον Τακάσι Τεζούκα το 1986 για το NES.",
        "funFacts": [
            "Πολλοί μη εξοικειωμένοι παίκτες μπερδεύουν τον πρωταγωνιστή Link, νομίζοντας ότι ονομάζεται Zelda (το όνομα της πριγκίπισσας).",
            "Ο Μιγιαμότο ονόμασε την πριγκίπισσα Zelda από τη Ζέλντα Φιτζέραλντ, σύζυγο του διάσημου συγγραφέα Φ. Σκοτ Φιτζέραλντ."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Legend_of_Zelda",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "gaming", "zelda"]
    },
    {
        "id": "pop_culture_med_147",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον εμβληματικό ρόλο του Forrest Gump στην ομώνυμη ταινία του 1994;",
        "answers": ["Τομ Χανκς", "Ρόμπιν Ουίλιαμς", "Τζον Τραβόλτα", "Μπιλ Μάρεϊ"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Τομ Χανκς κέρδισε το Όσκαρ Α' Ανδρικού Ρόλου για την ερμηνεία του ως Φόρεστ Γκαμπ, έναν χρόνο μετά το πρώτο του Όσκαρ για το 'Philadelphia'.",
        "funFacts": [
            "Ο Τομ Χανκς έγινε μόλις ο δεύτερος ηθοποιός στην ιστορία που κέρδισε διαδοχικά Όσκαρ Α' Ανδρικού Ρόλου (μετά τον Σπένσερ Τρέισι το 1937-1938).",
            "Η περίφημη ατάκα 'Η ζωή είναι σαν ένα κουτί σοκολατάκια' κατατάσσεται στις πιο αξιομνημόνευτες ατάκες του κινηματογράφου."
        ],
        "source": "https://en.wikipedia.org/wiki/Forrest_Gump",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "tom_hanks"]
    },
    {
        "id": "pop_culture_med_148",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο βρετανικό συγκρότημα ηλεκτρονικής μουσικής κυκλοφόρησε το 1997 το θρυλικό άλμπουμ 'The Fat of the Land';",
        "answers": ["The Chemical Brothers", "The Prodigy", "Fatboy Slim", "Underworld"],
        "correctAnswerIndex": 1,
        "explanation": "Οι The Prodigy, με επικεφαλής τον Λίαμ Χάουλετ και τον τραγουδιστή Κιθ Φλιντ, κυκλοφόρησαν το 'The Fat of the Land' με τεράστια επιτυχία παγκοσμίως.",
        "funFacts": [
            "Το άλμπουμ περιλαμβάνει ιστορικά dance κομμάτια όπως τα 'Firestarter', 'Breathe' και 'Smack My Bitch Up'.",
            "Το 'The Fat of the Land' έκανε ντεμπούτο στο νούμερο 1 του αμερικανικού Billboard 200, σπάνιο κατόρθωμα για βρετανικό dance συγκρότημα."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Fat_of_the_Land",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "electronic"]
    },
    {
        "id": "pop_culture_med_149",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο franchise τρόμου περιλαμβάνει τον διαβόητο δολοφόνο με τη μάσκα του χόκεϊ, Jason Voorhees;",
        "answers": ["Halloween", "A Nightmare on Elm Street", "Friday the 13th", "The Texas Chain Saw Massacre"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Τζέισον Βόρχις είναι ο κεντρικός ανταγωνιστής του franchise 'Friday the 13th' (Παρασκευή και 13), που τρομοκρατεί την κατασκήνωση Camp Crystal Lake.",
        "funFacts": [
            "Στην πρώτη πρωτότυπη ταινία του 1980, ο δολοφόνος δεν ήταν ο Τζέισον αλλά η μητέρα του, Πάμελα Βόρχις.",
            "Ο Τζέισον φόρεσε την εμβληματική μάσκα του χόκεϊ για πρώτη φορά στην τρίτη ταινία της σειράς (Part III, 1982)."
        ],
        "source": "https://en.wikipedia.org/wiki/Friday_the_13th_(franchise)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "horror"]
    },
    {
        "id": "pop_culture_med_150",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του διάσημου καλλιτεχνικού διευθυντή και σχεδιαστή μόδας του οίκου Chanel από το 1983 έως τον θάνατό του το 2019;",
        "answers": ["Ιβ Σεν Λοράν", "Τζιάνι Βερσάτσε", "Κρίστιαν Ντιόρ", "Καρλ Λάγκερφελντ"],
        "correctAnswerIndex": 3,
        "explanation": "Ο Καρλ Λάγκερφελντ (Karl Lagerfeld) αναβίωσε τον οίκο Chanel και υπήρξε μία από τις πιο αναγνωρίσιμες φιγούρες στην παγκόσμια μόδα με τα μαύρα γυαλιά και τη λευκή αλογοουρά.",
        "funFacts": [
            "Η αγαπημένη του γάτα, η Choupette, κληρονόμησε μέρος της περιουσίας του και είχε δικούς της λογαριασμούς στα social media.",
            "Σχεδίαζε παράλληλα συλλογές για τον ιταλικό οίκο Fendi καθώς και για το δικό του ομώνυμο brand."
        ],
        "source": "https://en.wikipedia.org/wiki/Karl_Lagerfeld",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "fashion", "celebrities"]
    },
    {
        "id": "pop_culture_med_151",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του αρχηγού των Autobots στο franchise των Transformers;",
        "answers": ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Optimus Prime είναι ο γενναίος ηγέτης των Autobots που μεταμορφώνεται συνήθως σε κόκκινο και μπλε φορτηγό (semi-truck).",
        "funFacts": [
            "Τη χαρακτηριστική φωνή του Optimus Prime δανείζει ο ηθοποιός Πίτερ Κάλεν από την αρχική σειρά κινουμένων σχεδίων του 1984.",
            "Το μότο του είναι 'Freedom is the right of all sentient beings' (Η ελευθερία είναι δικαίωμα όλων των νοημόνων όντων)."
        ],
        "source": "https://en.wikipedia.org/wiki/Optimus_Prime",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "transformers", "animation"]
    },
    {
        "id": "pop_culture_med_152",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια διάσημη σειρά κόμικς του Ρενέ Γκοσινί και του Αλμπέρ Ουντερζό εξιστορεί τις περιπέτειες ενός ανυπότακτου γαλατικού χωριού;",
        "answers": ["Λούκυ Λουκ", "Αστερίξ", "Ιζνογκούντ", "Τεντέν"],
        "correctAnswerIndex": 1,
        "explanation": "Το 'Αστερίξ' (Astérix) ξεκίνησε το 1959 και ακολουθεί τον Αστερίξ και τον Οβελίξ που αντιστέκονται στη ρωμαϊκή κατοχή με τη βοήθεια του μαγικού ζωμού.",
        "funFacts": [
            "Ο πρώτος γαλλικός τεχνητός δορυφόρος, που εκτοξεύτηκε το 1965, ονομάστηκε 'Astérix' προς τιμήν του ήρωα.",
            "Τα κόμικς του Αστερίξ έχουν μεταφραστεί σε περισσότερες από 110 γλώσσες και διαλέκτους, συμπεριλαμβανομένων των αρχαίων ελληνικών."
        ],
        "source": "https://en.wikipedia.org/wiki/Asterix",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics", "asterix"]
    },
    {
        "id": "pop_culture_med_153",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ηθοποιός υποδύθηκε τη Carrie Bradshaw στη δημοφιλή τηλεοπτική σειρά 'Sex and the City';",
        "answers": ["Κιμ Κατράλ", "Κριστίν Ντέιβις", "Σάρα Τζέσικα Πάρκερ", "Σίνθια Νίξον"],
        "correctAnswerIndex": 2,
        "explanation": "Η Σάρα Τζέσικα Πάρκερ πρωταγωνίστησε ως η αρθρογράφος και λάτρης της μόδας Κάρι Μπράντσοου στο HBO από το 1998 έως το 2004.",
        "funFacts": [
            "Η αγάπη του χαρακτήρα για τα παπούτσια Manolo Blahnik εκτόξευσε τις πωλήσεις του σχεδιαστή παγκοσμίως.",
            "Η σειρά βασίστηκε στην ομώνυμη στήλη εφημερίδας και βιβλίο της Κάντας Μπούσνελ."
        ],
        "source": "https://en.wikipedia.org/wiki/Sex_and_the_City",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "fashion"]
    },
    {
        "id": "pop_culture_med_154",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του φανταστικού χωριού των μικρών μπλε πλασμάτων που δημιούργησε ο Βέλγος κομίστας Peyo;",
        "answers": ["Στρουμφοχωριό", "Στρουμφόπολη", "Στρουμφοδάσος", "Στρουμφοκάστρο"],
        "correctAnswerIndex": 0,
        "explanation": "Τα Στρουμφάκια (Les Schtroumpfs) ζουν στο Στρουμφοχωριό, κρυμμένο μέσα σε μυστικό δάσος, σε σπιτάκια από μανιτάρια.",
        "funFacts": [
            "Τα Στρουμφάκια πρωτοεμφανίστηκαν το 1958 ως δευτερεύοντες χαρακτήρες στο κόμικ 'Johan et Pirlouit'.",
            "Ο αιώνιος εχθρός τους είναι ο κακός μάγος Δρακουμέλ (Gargamel) και ο γάτος του Ψιψινέλ (Azrael)."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Smurfs",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "comics", "smurfs"]
    },
    {
        "id": "pop_culture_med_155",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος καλλιτέχνης κυκλοφόρησε το παγκόσμιο hit 'Shape of You' το 2017;",
        "answers": ["Τζάστιν Μπίμπερ", "Εντ Σίραν", "Χάρι Στάιλς", "Σον Μέντες"],
        "correctAnswerIndex": 1,
        "explanation": "Ο Βρετανός τραγουδοποιός Εντ Σίραν (Ed Sheeran) κυκλοφόρησε το 'Shape of You' ως μέρος του άλμπουμ '÷' (Divide), κατακτώντας την κορυφή σε 34 χώρες.",
        "funFacts": [
            "Το 'Shape of You' έγινε το τραγούδι με τα περισσότερα streams στην ιστορία του Spotify εκείνη την εποχή, ξεπερνώντας τα 3 δισεκατομμύρια streams.",
            "Ο Σίραν έγραψε αρχικά το κομμάτι με την πρόθεση να το δώσει στη Ριάνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Shape_of_You",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "music", "ed_sheeran"]
    },
    {
        "id": "pop_culture_med_156",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποια ταινία του Τζέιμς Κάμερον που κυκλοφόρησε το 2009 έγινε η πιο επιτυχημένη εμπορικά ταινία όλων των εποχών;",
        "answers": ["Τιτανικός", "Terminator 2", "Avatar", "Aliens"],
        "correctAnswerIndex": 2,
        "explanation": "Το 'Avatar' έφερε επανάσταση στην τεχνολογία του τρισδιάστατου (3D) κινηματογράφου και παραμένει η ταινία με τις υψηλότερες εισπράξεις στην ιστορία, ξεπερνώντας τα 2,9 δισεκατομμύρια δολάρια.",
        "funFacts": [
            "Ο γλωσσολόγος Πολ Φρόμερ δημιούργησε μια πλήρη, λειτουργική γλώσσα με πάνω από 1.000 λέξεις για τους εξωγήινους Na'vi.",
            "Ο Κάμερον περίμενε πάνω από μια δεκαετία για να γυρίσει την ταινία μέχρι να εξελιχθεί επαρκώς η τεχνολογία motion capture."
        ],
        "source": "https://en.wikipedia.org/wiki/Avatar_(2009_film)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "avatar"]
    },
    {
        "id": "pop_culture_med_157",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος είναι ο διάσημος μυστικός πράκτορας με αμνησία που υποδύθηκε ο Ματ Ντέιμον στην κινηματογραφική σειρά κατασκοπείας;",
        "answers": ["Τζακ Ρίτσερ", "Ίθαν Χαντ", "Τζέισον Μπορν", "Τζέιμς Μποντ"],
        "correctAnswerIndex": 2,
        "explanation": "Ο Ματ Ντέιμον υποδύθηκε τον Τζέισον Μπορν (Jason Bourne) ξεκινώντας με το 'The Bourne Identity' το 2002, βασισμένο στα βιβλία του Ρόμπερτ Λάντλαμ.",
        "funFacts": [
            "Το γρήγορο μοντάζ και οι ρεαλιστικές χορογραφίες μάχης των ταινιών Bourne άλλαξαν το στυλ ολόκληρου του είδους δράσης του Χόλιγουντ.",
            "Ο Ματ Ντέιμον εκπαιδεύτηκε για μήνες στις πολεμικές τέχνες Kali και πυγμαχία για τον ρόλο."
        ],
        "source": "https://en.wikipedia.org/wiki/Bourne_(franchise)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "cinema", "action"]
    },
    {
        "id": "pop_culture_med_158",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο είναι το όνομα του γλυκύτατου εξωγήινου χαρακτήρα στη σειρά 'The Mandalorian' που το κοινό ονόμασε ανεπίσημα 'Baby Yoda';",
        "answers": ["Μπόμπα Φετ", "Άσοκα Τάνο", "Έζρα Μπρίτζερ", "Γκρόγκου"],
        "correctAnswerIndex": 3,
        "explanation": "Το πραγματικό όνομα του χαρακτήρα αποκαλύφθηκε στη δεύτερη σεζόν ότι είναι Γκρόγκου (Grogu).",
        "funFacts": [
            "Ο δημιουργός της σειράς Τζον Φαβρό κράτησε την ύπαρξη του χαρακτήρα απόλυτο μυστικό μέχρι την πρεμιέρα του πρώτου επεισοδίου.",
            "Η κούκλα animatronic του Grogu κόστισε στην παραγωγή περίπου 5 εκατομμύρια δολάρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Grogu",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "star_wars", "mandalorian"]
    },
    {
        "id": "pop_culture_med_159",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιος ηθοποιός ενσάρκωσε τον Wolverine στην κινηματογραφική σειρά των X-Men για πάνω από 20 χρόνια;",
        "answers": ["Χιου Τζάκμαν", "Ράιαν Ρέινολντς", "Κρίστιαν Μπέιλ", "Τομ Χάρντι"],
        "correctAnswerIndex": 0,
        "explanation": "Ο Αυστραλός ηθοποιός Χιου Τζάκμαν ανέλαβε τον ρόλο του Wolverine στο 'X-Men' (2000) και τον υποδύθηκε σε πολυάριθμες ταινίες, συμπεριλαμβανομένου του 'Deadpool & Wolverine' (2024).",
        "funFacts": [
            "Ο Τζάκμαν κατέχει το ρεκόρ Γκίνες για τη μεγαλύτερη σε διάρκεια καριέρα ως live-action υπερήρωας της Marvel.",
            "Στα κόμικς ο Wolverine έχει ύψος μόλις 1,60 μ., ενώ ο Χιου Τζάκμαν έχει ύψος σχεδόν 1,90 μ."
        ],
        "source": "https://en.wikipedia.org/wiki/Hugh_Jackman",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "marvel", "x_men"]
    },
    {
        "id": "pop_culture_med_160",
        "categoryId": "pop_culture",
        "difficulty": 3,
        "locale": "el-GR",
        "text": "Ποιο reality τηλεπαιχνίδι επιβίωσης ξεκίνησε διεθνώς από τη Σουηδία (ως Expedition Robinson) και σημείωσε τεράστια επιτυχία παγκοσμίως;",
        "answers": ["Big Brother", "Survivor", "The Amazing Race", "I'm a Celebrity...Get Me Out of Here!"],
        "correctAnswerIndex": 1,
        "explanation": "Το Survivor δημιουργήθηκε το 1997 από τον Βρετανό τηλεοπτικό παραγωγό Τσάρλι Πάρσονς και πρωτοπροβλήθηκε στη Σουηδία, εξελισσόμενο σε ένα από τα πιο επιτυχημένα reality formats στην ιστορία.",
        "funFacts": [
            "Η αμερικανική εκδοχή του Survivor με παρουσιαστή τον Τζεφ Προμπστ προβάλλεται αδιάλειπτα από το 2000 με πάνω από 45 σεζόν.",
            "Στην Ελλάδα, το Survivor προβλήθηκε για πρώτη φορά το 2003 από το Mega και σημείωσε ιστορικά ρεκόρ τηλεθέασης στον ΣΚΑΪ το 2017."
        ],
        "source": "https://en.wikipedia.org/wiki/Survivor_(franchise)",
        "status": "reviewed",
        "verifiedAt": "2026-10-25",
        "tags": ["pop_culture", "tv", "survivor"]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(QUESTIONS)} questions for pop_culture_medium.")
    validate_and_append("pop_culture", "medium", 3, QUESTIONS)

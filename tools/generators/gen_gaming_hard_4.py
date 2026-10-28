# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_156",
        "text": "Ποιο καινοτόμο σύστημα προγραμματισμού τεχνητής νοημοσύνης εφάρμοσε ο Hiroyuki Ito στο σύστημα μάχης του 'Final Fantasy XII' (2006) στο PlayStation 2;",
        "correct": "Το σύστημα Gambits (εντολές 'Εάν... τότε...' με συνθήκες προτεραιότητας)",
        "distractors": [
            "Το σύστημα Sphere Grid AI",
            "Το σύστημα Paradigm Shift",
            "Το σύστημα Junctioning"
        ],
        "explanation": "Το σύστημα Gambit επέτρεπε στον παίκτη να προγραμματίζει αυτόνομες συμπεριφορές για κάθε μέλος της ομάδας (π.χ. 'Αν σύμμαχος έχει HP < 30% -> Cure', 'Αν εχθρός είναι αδύναμος στη φωτιά -> Fire').",
        "funFacts": [
            "Το σύστημα Gambits ήταν τόσο ισχυρό ώστε καλοκουρδισμένες ομάδες μπορούσαν να νικήσουν ακόμη και το αφεντικό Yiazmat με τα 50 εκατομμύρια HP χωρίς ανθρώπινη παρέμβαση.",
            "Ο Hiroyuki Ito ήταν επίσης ο εμπνευστής του ιστορικού συστήματος Active Time Battle (ATB) στο Final Fantasy IV."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_XII",
        "tags": ["gaming", "final_fantasy", "square_enix", "mechanics", "playstation2"]
    },
    {
        "id": "gaming_hard_157",
        "text": "Ποιο επαναστατικό σύστημα αφήγησης εφάρμοσε ο Cory Barlog στο 'God of War' (2018) στο PlayStation 4, προσφέροντας πρωτοφανή κινηματογραφική εμβύθιση;",
        "correct": "Ένα μονοπλάνο χωρίς καμία διακοπή κάμερας ή cutscene cut (One Continuous Shot)",
        "distractors": [
            "Πλήρης αφήγηση σε πρώτο πρόσωπο μέσα από τα μάτια του Kratos",
            "Αποκλειστική χρήση split-screen για την ταυτόχρονη παρακολούθηση του Atreus",
            "Διαδραστικές επιλογές διαλόγων με σύστημα ηθικής karma"
        ],
        "explanation": "Ο Barlog και η Santa Monica Studio γύρισαν ολόκληρο το παιχνίδι σαν ένα αδιάκοπο μονοπλάνο (one-shot take): η κάμερα δεν κόβει ποτέ, ακολουθώντας ομαλά τον Kratos και τον Atreus από το gameplay στις σκηνές διαλόγων και πίσω.",
        "funFacts": [
            "Η ηγεσία της Sony ήταν αρχικά εξαιρετικά σκεπτική για την τεχνική δυσκολία του εγχειρήματος, αλλά το αποτέλεσμα απέσπασε πάνω από 190 βραβεία Game of the Year.",
            "Το νέο βασικό όπλο του Kratos, το Leviathan Axe, σχεδιάστηκε για να επιστρέφει στο χέρι του όπως το σφυρί Mjolnir του Thor."
        ],
        "source": "https://en.wikipedia.org/wiki/God_of_War_(2018_video_game)",
        "tags": ["gaming", "god_of_war", "playstation4", "santa_monica", "cory_barlog"]
    },
    {
        "id": "gaming_hard_158",
        "text": "Ποιο καινοτόμο σύστημα τεχνητής νοημοσύνης ανέπτυξε η Turtle Rock Studios και η Valve για το συνεργατικό shooter ζόμπι 'Left 4 Dead' (2008);",
        "correct": "The AI Director (δυναμικός ρυθμιστής έντασης, spawns και αντικειμένων)",
        "distractors": [
            "Swarm Mind AI",
            "Infection Controller",
            "Horde Pathmaker"
        ],
        "explanation": "Ο AI Director παρακολουθεί συνεχώς το άγχος, την υγεία, την ακρίβεια και την τοποθεσία των τεσσάρων επιζώντων, αποφασίζοντας δυναμικά πότε θα στείλει ορδές ζόμπι, ειδικά μολυσμένα τέρατα ή κουτιά πρώτων βοηθειών.",
        "funFacts": [
            "Χάρη στον AI Director, κανένα playthrough μιας πίστας δεν είναι ποτέ πανομοιότυπο με το προηγούμενο.",
            "Ο ήχος κλάματος της Witch σχεδιάστηκε για να προκαλεί άμεσο ενστικτώδη τρόμο και αποφυγή φωτισμού με φακούς."
        ],
        "source": "https://en.wikipedia.org/wiki/Left_4_Dead",
        "tags": ["gaming", "valve", "left_4_dead", "ai", "coop"]
    },
    {
        "id": "gaming_hard_159",
        "text": "Ποιοι δύο φοιτητές δημιούργησαν το 1999 το αρχικό mod 'Counter-Strike' πάνω στη μηχανή GoldSrc του Half-Life, το οποίο εξαγοράστηκε από τη Valve και έγινε το μακροβιότερο tactical FPS στον κόσμο;",
        "correct": "Minh Le (Gooseman) και Jess Cliffe",
        "distractors": [
            "Robin Walker και John Cook",
            "Gabe Newell και Mike Harrington",
            "Cliff Bleszinski και Tim Sweeney"
        ],
        "explanation": "Ο Minh Le σχεδίασε τα 3D μοντέλα και τα όπλα, ενώ ο Jess Cliffe δημιούργησε την ιστοσελίδα, τους ήχους και δάνεισε τη φωνή του στις εμβληματικές ατάκες ('Bomb has been planted', 'Counter-Terrorists win').",
        "funFacts": [
            "Η θρυλική πίστα 'de_dust' σχεδιάστηκε από τον David Johnston (DaveJ) εμπνευσμένη από φωτογραφίες της Αιγύπτου.",
            "Το όπλο AWP (Arctic Warfare Police) έγινε το πιο επίφοβο και πολυσυζητημένο sniper rifle στα esports για το one-shot kill στο σώμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Counter-Strike_(video_game)",
        "tags": ["gaming", "counter_strike", "valve", "mod", "esports"]
    },
    {
        "id": "gaming_hard_160",
        "text": "Ποιο mod του 'Arma 2' που δημιούργησε ο Νεοζηλανδός Dean 'Rocket' Hall το 2012 γέννησε τη σύγχρονη μανία των multiplayer survival παιχνιδιών ανοιχτού κόσμου;",
        "correct": "DayZ",
        "distractors": [
            "Rust",
            "The Forest",
            "Ark: Survival Evolved"
        ],
        "explanation": "Ο Dean Hall άντλησε έμπνευση από τις σκληρές εμπειρίες του κατά την εκπαίδευση επιβίωσης στον στρατό της Νέας Ζηλανδίας, δημιουργώντας έναν αμείλικτο κόσμο (Chernarus) όπου η πείνα, οι ασθένειες και οι άλλοι παίκτες ήταν πιο επικίνδυνοι από τα ζόμπι.",
        "funFacts": [
            "Η τεράστια επιτυχία του mod εκτόξευσε τις πωλήσεις του Arma 2 κατά πάνω από 500% μήνες μετά την κυκλοφορία του.",
            "Το DayZ αποτέλεσε το άμεσο εφαλτήριο για τη δημιουργία των Battle Royale παιχνιδιών."
        ],
        "source": "https://en.wikipedia.org/wiki/DayZ_(mod)",
        "tags": ["gaming", "dayz", "dean_hall", "survival", "arma"]
    },
    {
        "id": "gaming_hard_161",
        "text": "Ποιος Ιρλανδός προγραμματιστής, γνωστός ως 'PlayerUnknown', δημιούργησε τα mods Battle Royale σε Arma 2 και DayZ προτού αναπτύξει το 'PUBG: Battlegrounds' (2017);",
        "correct": "Brendan Greene",
        "distractors": [
            "Dean Hall",
            "Garry Newman",
            "Cliff Bleszinski"
        ],
        "explanation": "Ο Brendan Greene εμπνεύστηκε από την ιαπωνική καλτ ταινία 'Battle Royale' (2000) και δημιούργησε έναν μηχανισμό όπου 100 παίκτες πέφτουν με αλεξίπτωτο σε ένα νησί και πολεμούν μέχρι τον τελευταίο επιζώντα μέσα σε μια συρρικνούμενη ζώνη.",
        "funFacts": [
            "Η νικητήρια φράση 'Winner Winner Chicken Dinner' προέρχεται από παλιά αργκό των τζογαδόρων της εποχής της Μεγάλης Ύφεσης.",
            "Το PUBG κατέχει το απόλυτο ιστορικό ρεκόρ ταυτόχρονων παικτών στο Steam με πάνω από 3,2 εκατομμύρια παίκτες online."
        ],
        "source": "https://en.wikipedia.org/wiki/PUBG:_Battlegrounds",
        "tags": ["gaming", "pubg", "brendan_greene", "battle_royale", "esports"]
    },
    {
        "id": "gaming_hard_162",
        "text": "Ποιος μυστηριώδης, ανώνυμος προγραμματιστής ανέλαβε την εξέλιξη, τον σχεδιασμό και την εξισορρόπηση του αρχικού mod 'Defense of the Ancients: Allstars' (DotA) από το 2005 και ηγήθηκε του Dota 2 στη Valve;",
        "correct": "IceFrog",
        "distractors": [
            "Eul",
            "Guinsoo (Steve Feak)",
            "Pendragon (Steve Mescon)"
        ],
        "explanation": "Ο IceFrog διατήρησε την απόλυτη ανωνυμία του για πάνω από μια δεκαετία ενώ εξέλισσε το DotA. Το 2009 προσλήφθηκε από τη Valve για να σχεδιάσει το αυτόνομο Dota 2 στη Source Engine.",
        "funFacts": [
            "Το πρώτο τουρνουά Dota 2 της Valve, 'The International 2011' στην Κολωνία, σόκαρε τη βιομηχανία προσφέροντας το πρωτοφανές χρηματικό έπαθλο του 1.000.000 δολαρίων στην ουκρανική ομάδα Na'Vi.",
            "Το DotA γεννήθηκε αρχικά ως custom map του Warcraft III: Reign of Chaos από έναν modder με το όνομα Eul το 2003."
        ],
        "source": "https://en.wikipedia.org/wiki/IceFrog",
        "tags": ["gaming", "dota2", "valve", "icefrog", "moba"]
    },
    {
        "id": "gaming_hard_163",
        "text": "Ποιο πρωτοποριακό RPG του 2019 από το στούντιο ZA/UM της Εσθονίας εξάλειψε πλήρως το παραδοσιακό σύστημα μάχης, αντικαθιστώντας το με εσωτερικούς διαλόγους μεταξύ 24 διαφορετικών πτυχών της ψυχής του ντετέκτιβ στο 'Thought Cabinet';",
        "correct": "Disco Elysium",
        "distractors": [
            "Planescape: Torment",
            "Pillars of Eternity",
            "Gamedec"
        ],
        "explanation": "Στο Disco Elysium του Robert Kurvitz, ο αμνησιακός ντετέκτιβ Harrier Du Bois ερευνά έναν φόνο στην πόλη Revachol. Οι δεξιότητες του μυαλού του (Logic, Inland Empire, Shivers κ.ά.) μιλούν μεταξύ τους σαν αυτόνομες φωνές στη συνείδησή του.",
        "funFacts": [
            "Κατά την παραλαβή του βραβείου Best Narrative στα The Game Awards 2019, οι δημιουργοί ευχαρίστησαν δημόσια τον Karl Marx και τον Friedrich Engels για την πολιτική τους παιδεία.",
            "Το σενάριο του παιχνιδιού περιλαμβάνει πάνω από 1.000.000 λέξεις εξαιρετικής λογοτεχνικής ποιότητας."
        ],
        "source": "https://en.wikipedia.org/wiki/Disco_Elysium",
        "tags": ["gaming", "disco_elysium", "zaum", "rpg", "writing"]
    },
    {
        "id": "gaming_hard_164",
        "text": "Ποιο αριστουργηματικό sci-fi space exploration puzzle game του 2019 από τη Mobius Digital εξελίσσεται σε έναν συνεχή χρονικό βρόχο ακριβώς 22 λεπτών, στο τέλος του οποίου ο ήλιος εκρήγνυται σε σουπερνόβα;",
        "correct": "Outer Wilds",
        "distractors": [
            "The Outer Worlds",
            "No Man's Sky",
            "Astroneer"
        ],
        "explanation": "Στο Outer Wilds του Alex Beachum, ο παίκτης εξερευνά ένα μικροσκοπικό ηλιακό σύστημα με πραγματική νευτώνεια βαρύτητα, ανακαλύπτοντας τα μυστικά του εξαφανισμένου αρχαίου πολιτισμού των Nomai πριν την αναπόφευκτη κατάρρευση του άστρου.",
        "funFacts": [
            "Το παιχνίδι δεν διαθέτει unlocks ή στατιστικά: η μόνη πρόοδος που αποκομίζει ο παίκτης σε κάθε κύκλο είναι η ίδια η γνώση που καταγράφεται στο ημερολόγιο του σκάφους.",
            "Ξεκίνησε ως η διπλωματική εργασία του Alex Beachum στο Πανεπιστήμιο της Νότιας Καλιφόρνιας (USC)."
        ],
        "source": "https://en.wikipedia.org/wiki/Outer_Wilds",
        "tags": ["gaming", "outer_wilds", "indie", "sci_fi", "puzzle"]
    },
    {
        "id": "gaming_hard_165",
        "text": "Ποιο indie puzzle mystery game του Lucas Pope (2018) χρησιμοποίησε μονόχρωμα γραφικά 1-bit dithering σε στυλ παλιού Macintosh και μια μαγική κλεψύδρα τσέπης (Memento Mortem) για να εξιχνιάσει τη μοίρα 60 επιβατών;",
        "correct": "Return of the Obra Dinn",
        "distractors": [
            "Papers, Please",
            "The Case of the Golden Idol",
            "Her Story"
        ],
        "explanation": "Ο παίκτης υποδύεται έναν εκτιμητή ζημιών της Εταιρείας Ανατολικών Ινδιών το 1807. Αγγίζοντας ένα πτώμα με το Memento Mortem, μεταφέρεται στην ακριβή στιγμή του θανάτου του για να ταυτοποιήσει το όνομα και την αιτία θανάτου και των 60 ναυτικών.",
        "funFacts": [
            "Ο Lucas Pope συνέθεσε μόνος του το επικό ορχηστρικό ναυτικό soundtrack χρησιμοποιώντας ψηφιακά synthesizers.",
            "Ο Pope ήταν επίσης ο δημιουργός του πασίγνωστου δυστοπικού 'εξομοιωτή γραφειοκρατίας' Papers, Please (2013)."
        ],
        "source": "https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn",
        "tags": ["gaming", "lucas_pope", "obra_dinn", "indie", "puzzle"]
    },
    {
        "id": "gaming_hard_166",
        "text": "Ποιο rogue-like action RPG της Supergiant Games (2020) πέτυχε την ιδιοφυή ενσωμάτωση της αφήγησης στον θάνατο, κάνοντας κάθε αποτυχημένη απόδραση του Ζαγρέα από τον Κάτω Κόσμο να προχωρά την ιστορία;",
        "correct": "Hades",
        "distractors": [
            "Bastion",
            "Transistor",
            "Pyre"
        ],
        "explanation": "Στο Hades του Greg Kasavin, ο Ζαγρέας προσπαθεί να αποδράσει από το βασίλειο του πατέρα του Άδη για να βρει τη μητέρα του Περσεφόνη. Κάθε θάνατος τον επιστρέφει στο Παλάτι, ξεκλειδώνοντας νέους πλήρως ηχογραφημένους διαλόγους με τους Ολύμπιους θεούς.",
        "funFacts": [
            "Το παιχνίδι περιέχει πάνω από 300.000 λέξεις διαλόγων χωρίς ο παίκτης να ακούσει σχεδόν ποτέ την ίδια ατάκα δύο φορές.",
            "Έγινε το πρώτο βιντεοπαιχνίδι στην ιστορία που τιμήθηκε με το κορυφαίο λογοτεχνικό βραβείο επιστημονικής φαντασίας Hugo Award το 2021."
        ],
        "source": "https://en.wikipedia.org/wiki/Hades_(video_game)",
        "tags": ["gaming", "hades", "supergiant", "greek_mythology", "roguelike"]
    },
    {
        "id": "gaming_hard_167",
        "text": "Ποιο franchise JRPG της Atlus υπό τον Katsura Hashino συνδύασε dungeon crawling με έναν λεπτομερή προσομοιωτή μαθητικής ζωής στο Τόκιο και δεσμούς φιλίας (Social Links / Confidants);",
        "correct": "Persona (Shin Megami Tensei: Persona)",
        "distractors": [
            "Shin Megami Tensei",
            "Digital Devil Saga",
            "Soul Hackers"
        ],
        "explanation": "Με το Persona 3 (2006) και τα Persona 4 και 5, η Atlus καθιέρωσε τη φόρμουλα όπου ο πρωταγωνιστής πηγαίνει σχολείο, δίνει εξετάσεις και χτίζει σχέσεις την ημέρα, αντλώντας από αυτές δύναμη για τις μάχες τη νύχτα.",
        "funFacts": [
            "Τα soundtracks των Persona 3, 4 και 5 συντέθηκαν από τον Shoji Meguro, συνδυάζοντας J-pop, jazz, acid rock και hip-hop.",
            "Στο Persona 3, οι χαρακτήρες καλούν τις Personas τους πυροβολώντας τον εαυτό τους στο κεφάλι με μια συσκευή που μοιάζει με πιστόλι ('Evoker')."
        ],
        "source": "https://en.wikipedia.org/wiki/Persona_(series)",
        "tags": ["gaming", "persona", "atlus", "rpg", "japan"]
    },
    {
        "id": "gaming_hard_168",
        "text": "Πώς γεννήθηκε η ιδέα της συνεργασίας της Square με τη Disney για τη δημιουργία της σειράς 'Kingdom Hearts' (2002);",
        "correct": "Από μια τυχαία συζήτηση σε ασανσέρ μεταξύ στελεχών της Square και της Disney που μοιράζονταν το ίδιο κτίριο στο Τόκιο",
        "distractors": [
            "Από επίσημη δημοπρασία δικαιωμάτων της Disney στην έκθεση E3 του 1999",
            "Από προσωπική επιστολή του Michael Eisner στον Hironobu Sakaguchi",
            "Από παραγγελία της Sony για την προώθηση του DVD player του PS2"
        ],
        "explanation": "Η Square και η Disney Japan είχαν τα γραφεία τους στο ίδιο συγκρότημα κτιρίων Meguro στο Τόκιο. Ο Shinji Hashimoto και ο Hironobu Sakaguchi συζητούσαν σε ένα ασανσέρ για έναν χαρακτήρα που θα μπορούσε να ανταγωνιστεί τον Mario, όταν συνάντησαν ένα στέλεχος της Disney.",
        "funFacts": [
            "Ο Tetsuya Nomura άκουσε τη συζήτηση και ζήτησε αμέσως να αναλάβει τη διεύθυνση του project, δημιουργώντας το Keyblade και τον Sora.",
            "Το αρχικό σχέδιο της Disney ήταν να πρωταγωνιστεί ο Donald Duck, ενώ η Square ήθελε τον Mickey Mouse, πριν ο Nomura σχεδιάσει έναν νέο ανθρώπινο ήρωα."
        ],
        "source": "https://en.wikipedia.org/wiki/Kingdom_Hearts",
        "tags": ["gaming", "kingdom_hearts", "square_enix", "disney", "nomura"]
    },
    {
        "id": "gaming_hard_169",
        "text": "Ποιο noir action shooter της Remedy Entertainment (2001) σε σενάριο Sam Lake εισήγαγε τη μηχανική του 'Bullet Time' (επιβράδυνση χρόνου κατά τη διάρκεια πυροβολισμών) στα video games, εμπνευσμένο από το The Matrix;",
        "correct": "Max Payne",
        "distractors": [
            "Alan Wake",
            "Stranglehold",
            "Dead to Rights"
        ],
        "explanation": "Το Max Payne έφερε κινηματογραφική δράση slow-motion με τον Max να εκτελεί άλματα shoot-dodge. Ο ίδιος ο σεναριογράφος Sam Lake δάνεισε το πρόσωπό του για το 3D μοντέλο του Max Payne στο πρώτο παιχνίδι.",
        "funFacts": [
            "Λόγω περιορισμένου budget, η Remedy χρησιμοποίησε μέλη της ομάδας και συγγενείς τους για όλους τους χαρακτήρες των graphic novel cutscenes (η μητέρα του Sam Lake υποδύθηκε τη Nicole Horne).",
            "Η φωνή του Max Payne ανήκε στον ηθοποιό James McCaffrey, ο οποίος συνεργάστηκε με τη Remedy μέχρι τον θάνατό του το 2023."
        ],
        "source": "https://en.wikipedia.org/wiki/Max_Payne_(video_game)",
        "tags": ["gaming", "max_payne", "remedy", "sam_lake", "bullet_time"]
    },
    {
        "id": "gaming_hard_170",
        "text": "Ποια διάσημη σειρά παιχνιδιών δράσης της Sega από τον Toshihiro Nagoshi διαδραματίζεται στην περιοχή Kamurocho, η οποία αποτελεί σχεδόν πιστή αναπαράσταση της συνοικίας κόκκινων φαναριών Kabukicho στο Shinjuku του Τόκιο;",
        "correct": "Yakuza (Ryū ga Gotoku / Like a Dragon)",
        "distractors": [
            "Shenmue",
            "Sleeping Dogs",
            "Judgment"
        ],
        "explanation": "Ο Kazuma Kiryu (ο Δράκος της Dojima) περιπλανιέται στο Kamurocho προστατεύοντας τους δικούς του ανθρώπους. Η Sega αναπαρήγαγε πιστά τα νέον φώτα, τα καταστήματα Don Quijote, τα μπαρ και τα στενά της πραγματικής συνοικίας του Τόκιο.",
        "funFacts": [
            "Ο Nagoshi έπρεπε να παλέψει σκληρά με τη διοίκηση της Sega για να εγκριθεί το παιχνίδι, καθώς απευθυνόταν αποκλειστικά σε ενήλικο ιαπωνικό κοινό.",
            "Η σειρά είναι διάσημη για την αντίθεση ανάμεσα στη σοβαρή, μελοδραματική κεντρική ιστορία και τα εντελώς ξεκαρδιστικά και παράλογα substories."
        ],
        "source": "https://en.wikipedia.org/wiki/Like_a_Dragon",
        "tags": ["gaming", "yakuza", "sega", "kiryu", "japan"]
    },
    {
        "id": "gaming_hard_171",
        "text": "Ποιο ήταν το όνομα του ακυκλοφόρητου sex minigame κώδικα στο 'Grand Theft Auto: San Andreas' (2004), το οποίο ξεκλειδώθηκε από modders στο PC και προκάλεσε τεράστιο πολιτικό σκάνδαλο στις ΗΠΑ;",
        "correct": "Hot Coffee",
        "distractors": [
            "Warm Milk",
            "Hidden Romance",
            "San Andreas Uncut"
        ],
        "explanation": "Ο Ολλανδός modder Patrick Wildenborg ανακάλυψε ότι ο κώδικας για το minigame υπήρχε ήδη μέσα στο δισκάκι του παιχνιδιού. Το ESRB άλλαξε τη διαβάθμιση σε Adults Only (AO), αναγκάζοντας τη Rockstar να αποσύρει εκατομμύρια αντίτυπα.",
        "funFacts": [
            "Η τότε γερουσιαστής Hillary Clinton ζήτησε επίσημη ομοσπονδιακή έρευνα από την FTC κατά της Rockstar και της Take-Two Interactive.",
            "Η Take-Two κατέληξε σε συμβιβασμό εκατομμυρίων δολαρίων με μετόχους και καταναλωτές για να κλείσει η υπόθεση."
        ],
        "source": "https://en.wikipedia.org/wiki/Hot_Coffee_(minigame)",
        "tags": ["gaming", "gta", "rockstar", "controversy", "history"]
    },
    {
        "id": "gaming_hard_172",
        "text": "Ποια πρωτοποριακή μηχανή φυσικής ανθρώπινου σώματος (physics animation engine) της NaturalMotion χρησιμοποίησε η Rockstar Games στα 'Grand Theft Auto IV' και 'Red Dead Redemption';",
        "correct": "Euphoria",
        "distractors": [
            "Havok",
            "PhysX",
            "Ragdoll Pro"
        ],
        "explanation": "Η μηχανή Euphoria δεν χρησιμοποιούσε προκαθορισμένα animations ragdoll. Αντίθετα, εξομοίωνε ένα ζωντανό νευρικό σύστημα: οι χαρακτήρες προσπαθούσαν να κρατήσουν την ισορροπία τους, πιάνονταν από κάγκελα όταν έπεφταν ή προστάτευαν το κεφάλι τους.",
        "funFacts": [
            "Χάρη στο Euphoria, κάθε πυροβολισμός σε εχθρό στο Red Dead Redemption προκαλούσε μοναδικές φυσικές αντιδράσεις ανάλογα με το σημείο τραυματισμού.",
            "Η τεχνολογία χρησιμοποιήθηκε επίσης στο Star Wars: The Force Unleashed για την απόδοση των Stormtroopers."
        ],
        "source": "https://en.wikipedia.org/wiki/Euphoria_(software)",
        "tags": ["gaming", "rockstar", "gta4", "red_dead_redemption", "physics"]
    },
    {
        "id": "gaming_hard_173",
        "text": "Ποιο ήταν το πρώτο παιχνίδι στη σειρά Grand Theft Auto που εγκατέλειψε την κάτοψη από ψηλά (top-down) και μετέφερε τη δράση σε έναν πλήρως τρισδιάστατο (3D) ανοιχτό κόσμο στη Liberty City το 2001;",
        "correct": "Grand Theft Auto III",
        "distractors": [
            "Grand Theft Auto: Vice City",
            "Grand Theft Auto 2",
            "Grand Theft Auto: London 1969"
        ],
        "explanation": "Το GTA III της DMA Design (μετέπειτα Rockstar North) καθόρισε τα σύγχρονα open-world 3D παιχνίδια, προσφέροντας πρωτοφανή ελευθερία κινήσεων, οδήγησης, ραδιοφωνικών σταθμών και αποστολών στη Liberty City.",
        "funFacts": [
            "Ο πρωταγωνιστής Claude δεν μιλούσε καθόλου σε όλη τη διάρκεια του παιχνιδιού, επιλογή που έγινε για λόγους οικονομίας χρόνου ανάπτυξης.",
            "Η κυκλοφορία του καθυστέρησε ελαφρώς μετά τις επιθέσεις της 11ης Σεπτεμβρίου 2001 για να αλλάξουν τα χρώματα των περιπολικών και να αφαιρεθεί μια αποστολή με τρομοκράτες."
        ],
        "source": "https://en.wikipedia.org/wiki/Grand_Theft_Auto_III",
        "tags": ["gaming", "gta", "rockstar", "open_world", "playstation2"]
    },
    {
        "id": "gaming_hard_174",
        "text": "Ποιο αριστουργηματικό παιχνίδι της Clover Studio και της Capcom (2006) σε σκηνοθεσία Hideki Kamiya υιοθέτησε το παραδοσιακό ιαπωνικό στυλ ζωγραφικής με μελάνι Sumi-e και τον μηχανισμό του Ουράνιου Πινέλου (Celestial Brush);",
        "correct": "Ōkami",
        "distractors": [
            "Viewtiful Joe",
            "God Hand",
            "Muramasa: The Demon Blade"
        ],
        "explanation": "Στο Okami ο παίκτης ελέγχει τη θεά του ήλιου Amaterasu με τη μορφή λευκού λύκου. Παγώνοντας τον χρόνο, μπορούσε να ζωγραφίσει με το Celestial Brush σύμβολα στην οθόνη για να κόψει δέντρα, να ανθίσει λουλούδια ή να επιτεθεί σε δαίμονες.",
        "funFacts": [
            "Παρά τις διθυραμβικές κριτικές, οι χαμηλές πωλήσεις του Okami συνέβαλαν στο κλείσιμο της Clover Studio από την Capcom.",
            "Η αμερικανική έκδοση του Wii περιείχε κατά λάθος στο εξώφυλλο ένα ανεπαίσθητο υδατογράφημα του λογοτύπου της ιστοσελίδας IGN, προκαλώντας γκάφα μεγατόνων."
        ],
        "source": "https://en.wikipedia.org/wiki/%C5%8Ckami",
        "tags": ["gaming", "capcom", "okami", "kamiya", "art"]
    },
    {
        "id": "gaming_hard_175",
        "text": "Στο 'The Witcher 3: Wild Hunt' (CD Projekt Red, 2015), ποια τραγική αλυσίδα αποστολών στο Velen θεωρείται από τις κορυφαίες στιγμές γραφής στην ιστορία των σύγχρονων RPGs;",
        "correct": "Η ιστορία του Ματωμένου Βαρώνου (Bloody Baron / Phillip Strenger)",
        "distractors": [
            "Η Μάχη του Kaer Morhen",
            "Το Κυνήγι των Crones of Crookback Bog",
            "Η Στέψη του Βασιλιά στο Skellige"
        ],
        "explanation": "Η ιστορία του Phillip Strenger (Bloody Baron), γραμμένη από τον Karolina Stachyra και τον Paweł Sasko, εξερευνά τον αλκοολισμό, την ενδοοικογενειακή βία, τη συγχώρεση και τη λύτρωση χωρίς καμία απόλυτα 'καλή' ή 'κακή' κατάληξη.",
        "funFacts": [
            "Το τέρας 'Botchling' (αγέννητο καταραμένο βρέφος) βασίζεται απευθείας σε έναν αρχαίο σλαβικό μύθο για τα Poroniec.",
            "Το The Witcher 3 απέσπασε πάνω από 250 βραβεία Game of the Year, καθιερώνοντας την πολωνική CD Projekt Red στην παγκόσμια ελίτ."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt",
        "tags": ["gaming", "witcher", "cd_projekt_red", "rpg", "writing"]
    },
    {
        "id": "gaming_hard_176",
        "text": "Ποιο φιλοσοφικό κεντρικό ερώτημα θέτει η Ravel Puzzlewell στον Nameless One στο μνημειώδες RPG 'Planescape: Torment' (Black Isle Studios, 1999) σε σενάριο Chris Avellone;",
        "correct": "'What can change the nature of a man?' (Τι μπορεί να αλλάξει τη φύση ενός ανθρώπου;)",
        "distractors": [
            "'What is the price of immortality?'",
            "'Where does the soul travel after Sigil falls?'",
            "'Why do gods fear the Lady of Pain?'"
        ],
        "explanation": "Το Planescape: Torment θεωρείται ένα από τα σπουδαιότερα λογοτεχνικά έργα των video games. Ο αθάνατος Nameless One αναζητά τους λόγους των αμέτρητων θανάτων του, με το ερώτημα της Ravel να αποτελεί τον κεντρικό θεματικό άξονα.",
        "funFacts": [
            "Ο πρωταγωνιστής συνοδεύεται από ένα αιωρούμενο σαρκαστικό κρανίο με το όνομα Morte (φωνή του Mitch Pileggi).",
            "Σχεδόν κάθε σύγκρουση στο παιχνίδι, συμπεριλαμβανομένης της τελικής αναμέτρησης με την Υπέρτατη Σκιά, μπορεί να επιλυθεί αποκλειστικά μέσω διαλόγου και φιλοσοφικών επιχειρημάτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Planescape:_Torment",
        "tags": ["gaming", "planescape_torment", "black_isle", "rpg", "avellone"]
    },
    {
        "id": "gaming_hard_177",
        "text": "Πόσους μήνες είχε στη διάθεσή της η Obsidian Entertainment για να αναπτύξει το αριστουργηματικό post-apocalyptic RPG 'Fallout: New Vegas' (2010);",
        "correct": "18 μήνες",
        "distractors": [
            "36 μήνες",
            "12 μήνες",
            "24 μήνες"
        ],
        "explanation": "Υπό την ηγεσία του Josh Sawyer και του Chris Avellone, η Obsidian παρέδωσε ένα από τα πιο πλούσια σε επιλογές RPGs όλων των εποχών μέσα σε μόλις 18 μήνες, βασισμένη στη μηχανή του Fallout 3.",
        "funFacts": [
            "Η Obsidian έχασε ένα τεράστιο οικονομικό bonus από την εκδότρια Bethesda επειδή το παιχνίδι πέτυχε βαθμολογία 84 στο Metacritic αντί του απαιτούμενου 85 (για μία μόνο μονάδα).",
            "Πολλοί από τους βασικούς δημιουργούς του New Vegas ήταν οι ίδιοι άνθρωποι που είχαν φτιάξει τα αρχικά Fallout 1 και 2 στην Interplay και Black Isle Studios."
        ],
        "source": "https://en.wikipedia.org/wiki/Fallout:_New_Vegas",
        "tags": ["gaming", "fallout_new_vegas", "obsidian", "rpg", "history"]
    },
    {
        "id": "gaming_hard_178",
        "text": "Ποιο boss στο JRPG 'Suikoden II' (Konami, 1998) θεωρείται ένα από τα πιο αδίστακτα και σκληρά αφεντικά στην ιστορία των RPGs, απαιτώντας από τον παίκτη να παρατάξει τρεις διαδοχικές ομάδες των 6 χαρακτήρων (18 μαχητές συνολικά);",
        "correct": "Luca Blight (ο Mad Prince του Highland)",
        "distractors": [
            "Jowy Atreides",
            "Neclord the Vampire",
            "Barbarossa Rugner"
        ],
        "explanation": "Ο Luca Blight επιβιώνει από νυχτερινή ενέδρα, βροχή από εκατοντάδες βέλη και μάχες με 18 διαφορετικούς συμμάχους του παίκτη προτού τελικά πέσει σε μια δραματική μονομαχία ένας προς έναν με τον πρωταγωνιστή Riou.",
        "funFacts": [
            "Η διάσημη ατάκα του Luca Blight πριν πεθάνει ('Χρειάστηκαν εκατοντάδες από εσάς μόνο και μόνο για να με σκοτώσετε!') επισφράγισε τη φήμη του ως ο απόλυτος κακός.",
            "Το Suikoden II θεωρείται από πολλούς κριτικούς το κορυφαίο JRPG του PlayStation 1 για την ώριμη πολιτική του πλοκή."
        ],
        "source": "https://en.wikipedia.org/wiki/Suikoden_II",
        "tags": ["gaming", "suikoden", "konami", "rpg", "bosses"]
    },
    {
        "id": "gaming_hard_179",
        "text": "Ποιο σύστημα εξέλιξης χαρακτήρων αντικατέστησε τα παραδοσιακά επίπεδα (levels) και πόντους εμπειρίας στο 'Final Fantasy X' (2001) στο PlayStation 2;",
        "correct": "Sphere Grid",
        "distractors": [
            "License Board",
            "Materia Matrix",
            "Crystarium"
        ],
        "explanation": "Στο Sphere Grid, οι χαρακτήρες κινούνται πάνω σε ένα τεράστιο κυκλικό διάγραμμα ξεκλειδώνοντας κόμβους στατιστικών (Strength, Agility, Magic) και ικανοτήτων χρησιμοποιώντας Sphere Levels και Power/Mana Spheres.",
        "funFacts": [
            "Στην έκδοση International και στα Remasters προστέθηκε το 'Expert Sphere Grid', επιτρέποντας στους παίκτες να κατευθύνουν οποιονδήποτε χαρακτήρα σε οποιοδήποτε ρόλο από την αρχή.",
            "Το Final Fantasy X ήταν το πρώτο παιχνίδι στη σειρά που διέθετε πλήρη φωνητική ηθοποιία (voice acting)."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_X",
        "tags": ["gaming", "final_fantasy", "square", "sphere_grid", "playstation2"]
    },
    {
        "id": "gaming_hard_180",
        "text": "Ποιο tactical RPG της Square (1997) σε σκηνοθεσία Yasumi Matsuno διαδραματίζεται στον μεσαιωνικό κόσμο της Ivalice και αφηγείται τον εμφύλιο 'Πόλεμο των Λεόντων' (The War of the Lions), εμπνευσμένο από τον πραγματικό αγγλικό Πόλεμο των Ρόδων;",
        "correct": "Final Fantasy Tactics",
        "distractors": [
            "Tactics Ogre: Let Us Cling Together",
            "Vandal Hearts",
            "Front Mission 3"
        ],
        "explanation": "Ο Yasumi Matsuno δημιούργησε ένα σκοτεινό πολιτικό αριστούργημα με τον Ramza Beoulve και τον Delita Heiral, συνδυάζοντας turn-based ισομετρική μάχη με ένα απίστευτα βαθύ σύστημα κλάσεων (Job System).",
        "funFacts": [
            "Ο Cloud Strife από το Final Fantasy VII εμφανίζεται ως μυστικός ξεκλείδωτος χαρακτήρας.",
            "Η μάχη στο Riovanes Castle εναντίον του Wiegraf θεωρείται ένα από τα πιο διαβόητα σημεία 'soft-lock' στα video games αν ο παίκτης έκανε save χωρίς δεύτερο slot."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_Tactics",
        "tags": ["gaming", "final_fantasy_tactics", "matsuno", "square", "rpg"]
    },
    {
        "id": "gaming_hard_181",
        "text": "Ποιο αριστούργημα της Square (2000) στο PlayStation 1 από τον Yasumi Matsuno παρακολουθούσε τον Riskbreaker Ashley Riot στα ερείπια της μεσαιωνικής πόλης Léa Monde, συνδυάζοντας ρυθμική στόχευση άκρων και ένα εξαιρετικά βαθύ σύστημα crafting όπλων;",
        "correct": "Vagrant Story",
        "distractors": [
            "Parasite Eve",
            "Koudelka",
            "Shadow Tower"
        ],
        "explanation": "Το Vagrant Story ήταν ένα τεχνικό θαύμα για το PS1, αποδίδοντας πλήρως τρισδιάστατα μοντέλα με πανέμορφα textures χωρίς προ-αποδοσμένα backgrounds. Ήταν το μόνο παιχνίδι του PS1 που έλαβε τέλειο σκορ 40/40 από το ιαπωνικό περιοδικό Famitsu.",
        "funFacts": [
            "Το σύστημα 'Risk' αύξανε την πιθανότητα critical hits αλλά μείωνε δραστικά την άμυνα του Ashley όσο συνέχιζε αδιάκοπα τα Chain Abilities.",
            "Η Léa Monde εντάχθηκε αργότερα επίσημα στο σύμπαν της Ivalice μαζί με το Final Fantasy Tactics και το FFXII."
        ],
        "source": "https://en.wikipedia.org/wiki/Vagrant_Story",
        "tags": ["gaming", "vagrant_story", "square", "matsuno", "playstation"]
    },
    {
        "id": "gaming_hard_182",
        "text": "Ποιο cinematic RPG της Square (1998) στο PlayStation 1, βασισμένο στο ομώνυμο επιστημονικό μυθιστόρημα τρόμου του Hideaki Sena, ακολουθούσε την αστυνομικό Aya Brea στο Μανχάταν καθώς τα μιτοχόνδρια των κυττάρων επαναστατούσαν ενάντια στην ανθρωπότητα;",
        "correct": "Parasite Eve",
        "distractors": [
            "Dino Crisis",
            "Galerians",
            "Fear Effect"
        ],
        "explanation": "Το Parasite Eve διαφημίστηκε ως 'The Cinematic RPG', συνδυάζοντας survival horror ατμόσφαιρα τύπου Resident Evil με το σύστημα μάχης Active Time Battle (ATB) και μουσική της Yoko Shimomura.",
        "funFacts": [
            "Η διάσημη εναρκτήρια σκηνή διαδραματίζεται στην Όπερα Carnegie Hall της Νέας Υόρκης, όπου όλοι οι θεατές αυτοαναφλέγονται μυστηριωδώς εκτός από την Aya.",
            "Το μυστικό 77-story dungeon 'Chrysler Building' στο New Game+ αποκάλυπτε την πραγματική μητέρα των μεταλλαγμένων μιτοχονδρίων."
        ],
        "source": "https://en.wikipedia.org/wiki/Parasite_Eve_(video_game)",
        "tags": ["gaming", "parasite_eve", "square", "horror", "rpg"]
    },
    {
        "id": "gaming_hard_183",
        "text": "Ποιο survival horror της Capcom (1999) σε σκηνοθεσία Shinji Mikami αντικατέστησε τα ζόμπι με αιμοδιψείς, ταχύτατους δεινόσαυρους (Velociraptors) και παρουσίασε την πράκτορα Regina, οριζόμενο ως 'Panic Horror';",
        "correct": "Dino Crisis",
        "distractors": [
            "Turok: Dinosaur Hunter",
            "Carnivores",
            "Jurassic Park: Trespasser"
        ],
        "explanation": "Σε αντίθεση με τα αργά ζόμπι του Resident Evil, οι δεινόσαυροι στο Dino Crisis μπορούσαν να καταδιώκουν τη Regina από δωμάτιο σε δωμάτιο, να της ρίχνουν το όπλο από τα χέρια και να υπερπηδούν εμπόδια.",
        "funFacts": [
            "Το Dino Crisis χρησιμοποίησε πλήρως τρισδιάστατα περιβάλλοντα σε πραγματικό χρόνο αντί για τα προ-αποδοσμένα 2D backgrounds των πρώτων Resident Evil.",
            "Η Regina έγινε μια από τις πιο δημοφιλείς ηρωίδες της Capcom, κάνοντας εμφανίσεις και στο tactical RPG Namco × Capcom."
        ],
        "source": "https://en.wikipedia.org/wiki/Dino_Crisis",
        "tags": ["gaming", "capcom", "dino_crisis", "mikami", "horror"]
    },
    {
        "id": "gaming_hard_184",
        "text": "Ποιο ιαπωνικό survival horror franchise της Tecmo (2001) εξόπλισε τους πρωταγωνιστές αποκλειστικά με μια φωτογραφική μηχανή (Camera Obscura) για να εξορκίζουν και να καταστρέφουν εκδικητικά πνεύματα;",
        "correct": "Fatal Frame (Project Zero)",
        "distractors": [
            "Siren (Forbidden Siren)",
            "Kuon",
            "Clock Tower"
        ],
        "explanation": "Στο Fatal Frame ο παίκτης έπρεπε να κοιτάξει τα φαντάσματα κατάματα μέσα από το σκόπευτρο της Camera Obscura. Όσο πιο κοντά περίμενε να πλησιάσει το φάντασμα πριν πατήσει το κλείστρο ('Fatal Frame' shot), τόσο μεγαλύτερη ζημιά προκαλούσε.",
        "funFacts": [
            "Ο παραγωγός Keisuke Kikuchi δήλωσε ότι εμπνεύστηκε το παιχνίδι από προσωπικές παραφυσικές εμπειρίες και παραδοσιακές ιαπωνικές τελετές εξαγνισμού.",
            "Στην Ιαπωνία η σειρά ονομάζεται 'Zero' και στην Ευρώπη 'Project Zero'."
        ],
        "source": "https://en.wikipedia.org/wiki/Fatal_Frame",
        "tags": ["gaming", "fatal_frame", "tecmo", "horror", "japan"]
    },
    {
        "id": "gaming_hard_185",
        "text": "Ποιο εξαιρετικά τρομακτικό stealth survival horror της Sony Japan (2003) από τον Keiichiro Toyama (δημιουργό του αρχικού Silent Hill) εισήγαγε τον μοναδικό μηχανισμό 'Sightjacking';",
        "correct": "Siren (Forbidden Siren)",
        "distractors": [
            "Rule of Rose",
            "Haunting Ground",
            "Echo Night"
        ],
        "explanation": "Στο Siren, οι κάτοικοι του καταραμένου χωριού Hanuda μετατρέπονται σε αθάνατα τέρατα Shibito. Με το Sightjacking, ο παίκτης συντονίζει τη συχνότητα του μυαλού του για να δει και να ακούσει μέσα από τα μάτια των ίδιων των Shibito που τον κυνηγούν.",
        "funFacts": [
            "Τα πρόσωπα όλων των χαρακτήρων δημιουργήθηκαν με ψηφιακή αποτύπωση φωτογραφιών πραγματικών Ιαπώνων ηθοποιών πάνω στα 3D πολυγωνικά μοντέλα.",
            "Η πλοκή εκτυλίσσεται μη-γραμμικά μέσα από 10 διαφορετικούς επιζώντες σε ένα χρονικό διάστημα τριών ημερών."
        ],
        "source": "https://en.wikipedia.org/wiki/Siren_(video_game)",
        "tags": ["gaming", "siren", "sony", "horror", "sightjacking"]
    },
    {
        "id": "gaming_hard_186",
        "text": "Ποιο επαναστατικό VR flagship game της Valve (2020) επανέφερε το σύμπαν του Half-Life μετά από 13 χρόνια αναμονής, εισάγοντας τα μαγνητικά γάντια 'Gravity Gloves' (Russells);",
        "correct": "Half-Life: Alyx",
        "distractors": [
            "Half-Life 2: Episode Three",
            "Boneworks",
            "The Walking Dead: Saints & Sinners"
        ],
        "explanation": "Το Half-Life: Alyx σχεδιάστηκε αποκλειστικά για συστήματα Virtual Reality. Τα Gravity Gloves επέτρεπαν στην Alyx Vance να στοχεύει μακρινά αντικείμενα (σφαίρες, ρητίνη, όπλα) και να τα τραβάει στον αέρα πιάνοντάς τα με φυσική κίνηση του χεριού.",
        "funFacts": [
            "Η φυσική προσομοίωσης υγρών μέσα στα μπουκάλια του παιχνιδιού προκάλεσε παγκόσμιο θαυμασμό στην κοινότητα των προγραμματιστών γραφικών.",
            "Το παιχνίδι άλλαξε το σοκαριστικό cliffhanger τέλος του Half-Life 2: Episode Two (2007) σχετικά με τη μοίρα του Eli Vance."
        ],
        "source": "https://en.wikipedia.org/wiki/Half-Life:_Alyx",
        "tags": ["gaming", "half_life", "valve", "vr", "alyx"]
    },
    {
        "id": "gaming_hard_187",
        "text": "Ποιο διάσημο studio της Remedy Entertainment (2019) δημιούργησε το action adventure 'Control', τοποθετημένο στο 'Oldest House' και βαθιά επηρεασμένο από τα μυθοπλαστικά αρχεία του SCP Foundation;",
        "correct": "Remedy Entertainment",
        "distractors": [
            "Arkane Studios",
            "Bungie",
            "Housemarque"
        ],
        "explanation": "Στο Control η Jesse Faden γίνεται διευθύντρια του Federal Bureau of Control (FBC), ενός μυστικού οργανισμού που ερευνά υπερφυσικά αντικείμενα ισχύος (Objects of Power) μέσα σε έναν διαρκώς μεταβαλλόμενο μπρουταλιστικό ουρανοξύστη.",
        "funFacts": [
            "Η περίφημη αποστολή 'Ashtray Maze' (Λαβύρινθος του Τασάκι) συνοδεύεται από το εκρηκτικό ροκ κομμάτι 'Take Control' του φανταστικού συγκροτήματος Old Gods of Asgard (Poets of the Fall).",
            "Το Control συνδέεται επίσημα στο ίδιο αφηγηματικό σύμπαν ('Remedy Connected Universe') με το Alan Wake."
        ],
        "source": "https://en.wikipedia.org/wiki/Control_(video_game)",
        "tags": ["gaming", "remedy", "control", "sam_lake", "scp"]
    },
    {
        "id": "gaming_hard_188",
        "text": "Ποιος σχεδιαστής επιτραπέζιων RPGs δημιούργησε το cyberpunk σύμπαν 'Cyberpunk 2020' (1988), συνεργαζόμενος στενά με την CD Projekt Red για το 'Cyberpunk 2077';",
        "correct": "Mike Pondsmith",
        "distractors": [
            "Gary Gygax",
            "Steve Jackson",
            "Monte Cook"
        ],
        "explanation": "Ο Mike Pondsmith εμπνεύστηκε τη Night City και το επιτραπέζιο Cyberpunk από τα έργα του William Gibson και του Philip K. Dick. Στο Cyberpunk 2077 δάνεισε επίσης τη φωνή του στον ραδιοφωνικό παραγωγό Maximum Mike.",
        "funFacts": [
            "Ο Keanu Reeves ενσάρκωσε τον εμβληματικό rockerboy Johnny Silverhand, κάνοντας motion capture και ηχογραφώντας δεκάδες ώρες διαλόγων.",
            "Η anime σειρά 'Cyberpunk: Edgerunners' του Studio Trigger το 2022 αναζωογόνησε θεαματικά το ενδιαφέρον των παικτών για το παιχνίδι."
        ],
        "source": "https://en.wikipedia.org/wiki/Mike_Pondsmith",
        "tags": ["gaming", "cyberpunk_2077", "cd_projekt_red", "mike_pondsmith", "rpg"]
    },
    {
        "id": "gaming_hard_189",
        "text": "Ποιος κορυφαίος Βρετανός ηθοποιός (διάσημος από ταινίες όπως το 'Titanic' και το 'The Omen') δάνεισε τη φωνή του στον κακό Jon Irenicus στο θρυλικό RPG 'Baldur's Gate II: Shadows of Amn' (2000);",
        "correct": "David Warner",
        "distractors": [
            "Patrick Stewart",
            "Ian McKellen",
            "Christopher Lee"
        ],
        "explanation": "Ο David Warner παρέδωσε μία από τις πιο ανατριχιαστικές και αναγνωρίσιμες ερμηνείες κακού στα video games ('Ah, the child of Bhaal has awoken... It is time for more experiments').",
        "funFacts": [
            "Το Baldur's Gate II περιείχε σχεδόν 300 ώρες περιεχομένου και πάνω από 1,2 εκατομμύρια λέξεις σεναρίου.",
            "Η BioWare πρόσθεσε για πρώτη φορά πλήρως ανεπτυγμένα συστήματα ειδυλλίων (romances) ανάμεσα στον πρωταγωνιστή και τους συντρόφους του (Aerie, Jaheira, Viconia, Anomen)."
        ],
        "source": "https://en.wikipedia.org/wiki/Baldur%27s_Gate_II:_Shadows_of_Amn",
        "tags": ["gaming", "bioware", "baldurs_gate", "voice_acting", "rpg"]
    },
    {
        "id": "gaming_hard_190",
        "text": "Ποιο είναι το όνομα της τυφλής Jedi Master και Sith Lord (Darth Traya) στο 'Star Wars Knights of the Old Republic II: The Sith Lords' (2004) του Chris Avellone, η οποία αποδομεί ολόκληρη τη φιλοσοφία της Δύναμης;",
        "correct": "Kreia",
        "distractors": [
            "Atris",
            "Visas Marr",
            "Darth Sion"
        ],
        "explanation": "Η Kreia θεωρείται ένας από τους πιο πολυεπίπεδους και συναρπαστικούς χαρακτήρες στην ιστορία του Star Wars. Περιφρονεί τόσο τους Jedi όσο και τους Sith, θεωρώντας ότι η ίδια η Δύναμη είναι ένας χειριστικός κοσμικός τύραννος που πρέπει να καταστραφεί.",
        "funFacts": [
            "Η φωνή της Kreia ανήκει στην ηθοποιό Sara Kestelman, η οποία έδωσε μια θεατρική, σχεδόν σαιξπηρική διάσταση στις διδασκαλίες της.",
            "Το παιχνίδι ολοκληρώθηκε εσπευσμένα μέσα σε μόλις 14 μήνες, με το περίφημο 'Restored Content Mod' (TSLRCM) να επαναφέρει αργότερα ώρες κομμένου περιεχομένου."
        ],
        "source": "https://en.wikipedia.org/wiki/Kreia",
        "tags": ["gaming", "star_wars", "kotor2", "obsidian", "avellone"]
    },
    {
        "id": "gaming_hard_191",
        "text": "Ποιο μοναδικό action rhythm platformer της Clover Studio στο GameCube (2003) από τον Hideki Kamiya συνδύασε δράση υπερηρώων με τις δυνάμεις VFX (Slow, Mach Speed, Zoom In);",
        "correct": "Viewtiful Joe",
        "distractors": [
            "God Hand",
            "MadWorld",
            "P.N.03"
        ],
        "explanation": "Ο Joe αποκτά το ρολόι V-Watch και μεταμορφώνεται σε υπερήρωα ταινιών δράσης. Χρησιμοποιώντας τις δυνάμεις σκηνοθεσίας (VFX), ο παίκτης επιβράδυνε τον χρόνο για να αποφεύγει σφαίρες ή έκανε Zoom In για να εξαπολύσει καταστροφικές επιθέσεις.",
        "funFacts": [
            "Το σύνθημα μεταμόρφωσης του Joe ήταν 'Henshin a go-go, baby!'.",
            "Το Viewtiful Joe ήταν μέλος των περίφημων 'Capcom Five', πέντε αποκλειστικών παιχνιδιών που ανακοίνωσε η Capcom για το GameCube (μαζί με το Resident Evil 4 και το Killer7)."
        ],
        "source": "https://en.wikipedia.org/wiki/Viewtiful_Joe_(video_game)",
        "tags": ["gaming", "capcom", "viewtiful_joe", "kamiya", "gamecube"]
    },
    {
        "id": "gaming_hard_192",
        "text": "Ποιο ιστορικό JRPG της Square (2000) στο PlayStation 1 επέστρεψε στις κλασικές ρίζες του high fantasy με μεσαιωνικό στυλ και εισήγαγε το σύστημα 'Active Time Event' (ATE);",
        "correct": "Final Fantasy IX",
        "distractors": [
            "Final Fantasy VIII",
            "Final Fantasy VII",
            "Chrono Cross"
        ],
        "explanation": "Ο σκηνοθέτης Hiroyuki Ito δημιούργησε το Final Fantasy IX ως φόρο τιμής σε όλη την κλασική εποχή της σειράς. Το σύστημα ATE επέτρεπε στον παίκτη να παρακολουθεί τι συνέβαινε σε άλλα μέλη της ομάδας (Zidane, Vivi, Steiner, Garnet) σε διαφορετικά σημεία της πόλης ταυτόχρονα.",
        "funFacts": [
            "Ο δημιουργός της σειράς Hironobu Sakaguchi έχει δηλώσει επανειλημμένα ότι το Final Fantasy IX είναι το αγαπημένο του παιχνίδι από όλα όσα δημιούργησε.",
            "Ο μικρός μάγος Vivi Ornitier θεωρείται ένας από τους πιο συγκινητικούς και αγαπημένους χαρακτήρες της σειράς για τη φιλοσοφική αναζήτηση του νοήματος της θνητότητας."
        ],
        "source": "https://en.wikipedia.org/wiki/Final_Fantasy_IX",
        "tags": ["gaming", "final_fantasy", "square", "playstation", "sakaguchi"]
    },
    {
        "id": "gaming_hard_193",
        "text": "Ποιο σύστημα μάχης χρησιμοποίησε η Square στο 'Chrono Cross' (1999), το οποίο δεν είχε MP (Magic Points) αλλά βασιζόταν σε χρωματικά στοιχεία και ένα πεδίο 'Field Effect';",
        "correct": "Element Grid και Stamina System",
        "distractors": [
            "Materia Ring",
            "Junction Drawing",
            "Mana Wheel"
        ],
        "explanation": "Στο Chrono Cross, κάθε ξόρκι ήταν ένα Element (White, Black, Red, Blue, Green, Yellow) τοποθετημένο σε ένα πλέγμα επιπέδων. Χρησιμοποιώντας ξόρκια του ίδιου χρώματος, ο παίκτης άλλαζε το χρώμα του πεδίου μάχης (Field Effect) για να καλέσει πανίσχυρα Summons.",
        "funFacts": [
            "Το Chrono Cross περιλάμβανε τον εκπληκτικό αριθμό των 45 διαφορετικών στρατολογήσιμων χαρακτήρων.",
            "Το ονειρικό soundtrack του Yasunori Mitsuda (με κομμάτια όπως το 'Scars of Time') θεωρείται ευρέως ένα από τα σπουδαιότερα στην ιστορία της μουσικής των video games."
        ],
        "source": "https://en.wikipedia.org/wiki/Chrono_Cross",
        "tags": ["gaming", "chrono_cross", "square", "mitsuda", "rpg"]
    },
    {
        "id": "gaming_hard_194",
        "text": "Ποιο ήταν το όνομα της μυθικής πόλης στην αρχή του 'Uncharted 2: Among Thieves' (2009), του οποίου η εναρκτήρια σκηνή δείχνει τον Nathan Drake τραυματισμένο μέσα σε ένα βαγόνι τρένου που κρέμεται πάνω από έναν χιονισμένο γκρεμό;",
        "correct": "Shambhala (Σαμπάλα)",
        "distractors": [
            "El Dorado",
            "Iram of the Pillars",
            "Libertalia"
        ],
        "explanation": "Στο Uncharted 2 της Naughty Dog (σκηνοθεσία Bruce Straley και Amy Hennig), ο Drake ακολουθεί τα ίχνη του χαμένου στόλου του Μάρκο Πόλο για να βρει τη μυθική Σαμπάλα και τον λίθο Cintamani Stone στα Ιμαλάια.",
        "funFacts": [
            "Η εναρκτήρια σκηνή του κρεμάμενου τρένου ξεκινά 'in media res' και θεωρείται μία από τις πιο συναρπαστικές εισαγωγές στην ιστορία των video games.",
            "Το παιχνίδι κέρδισε πάνω από 300 βραβεία Game of the Year και εδραίωσε τη Naughty Dog ως το κορυφαίο cinematic action studio της Sony."
        ],
        "source": "https://en.wikipedia.org/wiki/Uncharted_2:_Among_Thieves",
        "tags": ["gaming", "uncharted", "naughty_dog", "playstation3", "action"]
    },
    {
        "id": "gaming_hard_195",
        "text": "Ποιος πραγματικός παρασιτικός μύκητας αποτέλεσε την επιστημονική έμπνευση του Neil Druckmann για τη μόλυνση των Infected στο 'The Last of Us' (2013);",
        "correct": "Ophiocordyceps unilateralis (Κορντίσεψ)",
        "distractors": [
            "Claviceps purpurea",
            "Aspergillus fumigatus",
            "Toxoplasma gondii"
        ],
        "explanation": "Ο Druckmann παρακολούθησε ένα ντοκιμαντέρ του BBC Planet Earth που έδειχνε πώς ο μύκητας Cordyceps μολύνει τα μυρμήγκια, ελέγχει τον εγκέφαλό τους και εκρήγνυται από το κρανίο τους. Αναρωτήθηκε τι θα συνέβαινε αν ο μύκητας μεταπηδούσε στους ανθρώπους.",
        "funFacts": [
            "Ο ανατριχιαστικός ήχος 'κλικ-κλικ' των Clickers δημιουργήθηκε από την ηθοποιό φωνής Misty Lee και τον Phillip Kovats.",
            "Το soundtrack συντέθηκε από τον δύο φορές βραβευμένο με Όσκαρ Gustavo Santaolalla, χρησιμοποιώντας παραδοσιακό ακουστικό roncoco."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Last_of_Us",
        "tags": ["gaming", "the_last_of_us", "naughty_dog", "cordyceps", "playstation"]
    },
    {
        "id": "gaming_hard_196",
        "text": "Ποιο open-world παιχνίδι δράσης της Rockstar Games (2006), τοποθετημένο στο οικοτροφείο Bullworth Academy, έβαλε τον παίκτη στον ρόλο του απείθαρχου μαθητή Jimmy Hopkins;",
        "correct": "Bully (Canis Canem Edit)",
        "distractors": [
            "The Warriors",
            "Manhunt",
            "State of Emergency"
        ],
        "explanation": "Στο Bully ο Jimmy αντιμετωπίζει τις κλίκες του σχολείου (Nerds, Preppies, Greasers, Jocks) παρακολουθώντας υποχρεωτικά μαθήματα (Αγγλικά, Χημεία, Γυμναστική) και κυκλοφορώντας με skateboard και σφεντόνα.",
        "funFacts": [
            "Στην Ευρώπη κυκλοφόρησε με τον τίτλο 'Canis Canem Edit' (Σκύλος τρώει σκύλο στα λατινικά) λόγω αντιδράσεων για τον τίτλο Bully.",
            "Ο ακτιβιστής Jack Thompson προσπάθησε ανεπιτυχώς να απαγορεύσει το παιχνίδι στη Φλόριντα, ισχυριζόμενος ότι ήταν 'εξομοιωτής σχολικής βίας'."
        ],
        "source": "https://en.wikipedia.org/wiki/Bully_(video_game)",
        "tags": ["gaming", "rockstar", "bully", "playstation2", "action"]
    },
    {
        "id": "gaming_hard_197",
        "text": "Ποιο ψυχολογικό θρίλερ της Remedy Entertainment (2010) χρησιμοποίησε το φως (φακός, φωτοβολίδες, προβολείς) ως το μοναδικό μέσο για να αφαιρεθεί η σκοτεινή ασπίδα των εχθρών Taken;",
        "correct": "Alan Wake",
        "distractors": [
            "Alone in the Dark",
            "Deadly Premonition",
            "The Evil Within"
        ],
        "explanation": "Στο Alan Wake, ο συγγραφέας Alan Wake αναζητά τη γυναίκα του στην πόλη Bright Falls. Οι εχθροί προστατεύονται από ένα πέπλο σκοταδιού, αναγκάζοντας τον παίκτη να τους φωτίσει με τον φακό μέχρι να σπάσει η ασπίδα πριν πυροβολήσει.",
        "funFacts": [
            "Το παιχνίδι δομήθηκε σαν τηλεοπτική σειρά με επεισόδια, cliffhangers και το τραγούδι των τίτλων τέλους σε κάθε κεφάλαιο.",
            "Η ιστορία άντλησε τεράστια έμπνευση από το Twin Peaks του David Lynch και τα μυθιστορήματα του Stephen King."
        ],
        "source": "https://en.wikipedia.org/wiki/Alan_Wake",
        "tags": ["gaming", "alan_wake", "remedy", "xbox360", "horror"]
    },
    {
        "id": "gaming_hard_198",
        "text": "Ποιο μοναδικό όχημα-αγωνιστικό ποδόσφαιρο παιχνίδι της Psyonix (2015) ξεκίνησε ως sequel του παιχνιδιού 'Supersonic Acrobatic Rocket-Powered Battle-Cars' και έγινε ένα από τα πιο επιτυχημένα esports στον κόσμο;",
        "correct": "Rocket League",
        "distractors": [
            "Destruction Derby",
            "TrackMania",
            "Wreckfest"
        ],
        "explanation": "Το Rocket League απλοποίησε το όνομα του προκατόχου του, τελειοποίησε τη φυσική της μπάλας και των πυραυλοκίνητων αυτοκινήτων (aerials, wall-riding) και εκτοξεύτηκε σε δημοτικότητα όταν διατέθηκε δωρεάν στο PlayStation Plus κατά την κυκλοφορία του.",
        "funFacts": [
            "Το Rocket League είναι απόλυτα βασισμένο στη δεξιότητα (zero RNG), καθώς όλα τα αυτοκίνητα μοιράζονται πανομοιότυπα στατιστικά ταχύτητας εντός της κατηγορίας hitbox τους.",
            "Η Psyonix εξαγοράστηκε από την Epic Games το 2019."
        ],
        "source": "https://en.wikipedia.org/wiki/Rocket_League",
        "tags": ["gaming", "rocket_league", "psyonix", "esports", "physics"]
    },
    {
        "id": "gaming_hard_199",
        "text": "Ποιο ψηφιακό trading card game της Blizzard (2014), δημιουργία μιας μικρής πειραματικής ομάδας ('Team 5') υπό τους Eric Dodds και Ben Brode, προκάλεσε την παγκόσμια έκρηξη των online card battlers;",
        "correct": "Hearthstone (Heroes of Warcraft)",
        "distractors": [
            "Magic: The Gathering Arena",
            "Artifact",
            "Gwent"
        ],
        "explanation": "Το Hearthstone απλοποίησε τους σύνθετους κανόνες του Magic: The Gathering, εισήγαγε δυναμικά animations, ήχους και χιούμορ από το σύμπαν του Warcraft και σχεδιάστηκε για άμεσο cross-play σε PC, iPad και κινητά τηλέφωνα.",
        "funFacts": [
            "Η Team 5 ξεκίνησε με μόλις 15 άτομα μέσα στη Blizzard, λειτουργώντας σαν ανεξάρτητο indie στούντιο.",
            "Η κάρτα 'Leeroy Jenkins' με charge και summon δύο welps για τον αντίπαλο έγινε μία από τις πιο εμβληματικές κάρτες finish."
        ],
        "source": "https://en.wikipedia.org/wiki/Hearthstone",
        "tags": ["gaming", "hearthstone", "blizzard", "card_game", "warcraft"]
    },
    {
        "id": "gaming_hard_200",
        "text": "Ποιος Ιάπωνας δημιουργός της PlatinumGames σκηνοθέτησε το θεαματικό action game 'Bayonetta' (2009), εισάγοντας τον μηχανισμό 'Witch Time' που επιβραδύνει τον χρόνο όταν ο παίκτης αποφεύγει μια επίθεση στο τελευταίο κλάσμα του δευτερολέπτου;",
        "correct": "Hideki Kamiya",
        "distractors": [
            "Shinji Mikami",
            "Tomonobu Itagaki",
            "Yoko Taro"
        ],
        "explanation": "Ο Hideki Kamiya (δημιουργός του Devil May Cry) εξέλιξε τη φιλοσοφία του stylish action με τη μάγισσα Bayonetta. Το Witch Time αντάμειβε το τέλειο dodge με λίγα δευτερόλεπτα ακινησίας των αγγελικών εχθρών, επιτρέποντας εξωφρενικά Wicked Weave combos.",
        "funFacts": [
            "Τα μαλλιά της Bayonetta αποτελούν ταυτόχρονα το κοστούμι της και το μέσο επίκλησης των γιγάντιων δαιμόνων Madama Butterfly.",
            "Όταν η Sega αρνήθηκε να χρηματοδοτήσει το Bayonetta 2, η Nintendo παρενέβη και έσωσε το project ως αποκλειστικό τίτλο του Wii U."
        ],
        "source": "https://en.wikipedia.org/wiki/Bayonetta_(video_game)",
        "tags": ["gaming", "bayonetta", "platinumgames", "kamiya", "action"]
    },
    {
        "id": "gaming_hard_201",
        "text": "Ποιο stealth action franchise της IO Interactive παρακολουθεί τον γενετικά τροποποιημένο εκτελεστή Agent 47, διαβόητο για το barcode στο πίσω μέρος του φαλακρού κρανίου του και τη μέθοδο εξόντωσης με χορδή πιάνου (fiber wire);",
        "correct": "Hitman",
        "distractors": [
            "Splinter Cell",
            "Sniper Elite",
            "Syphon Filter"
        ],
        "explanation": "Το Hitman (ξεκινώντας με το 'Hitman: Codename 47' το 2000) πρωτοπόρησε με το σύστημα μεταμφιέσεων (disguises), επιτρέποντας στον παίκτη να κλέβει τα ρούχα φρουρών, σερβιτόρων ή γιατρών για να κινείται ανενόχλητος σε κοινωνικούς χώρους (social stealth).",
        "funFacts": [
            "Το barcode του Agent 47 τελειώνει στον αριθμό '640509-040147', με τα δύο τελευταία ψηφία να δηλώνουν ότι είναι ο 47ος κλώνος της σειράς.",
            "Στο 'Hitman: Blood Money' (2006), η εφημερίδα στο τέλος κάθε πίστας περιέγραφε αναλυτικά τις πράξεις του παίκτη, το επίπεδο θορύβου και τις μαρτυρίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Hitman_(franchise)",
        "tags": ["gaming", "hitman", "io_interactive", "stealth", "agent_47"]
    },
    {
        "id": "gaming_hard_202",
        "text": "Ποια διάσημη σειρά stealth action της Ubisoft, βασισμένη στα βιβλία του Tom Clancy, παρουσίασε τον πράκτορα Sam Fisher της Third Echelon με τα εμβληματικά νυχτερινά γυαλιά τριών πράσινων φακών (trifocal goggles);",
        "correct": "Tom Clancy's Splinter Cell",
        "distractors": [
            "Rainbow Six",
            "Ghost Recon",
            "The Division"
        ],
        "explanation": "Το αρχικό Splinter Cell (2002) ανέπτυξε έναν επαναστατικό φωτισμό δυναμικών σκιών όπου ο Sam Fisher μπορούσε να κρυφτεί στο απόλυτο σκοτάδι (light meter) και να εκτελέσει το χαρακτηριστικό άλμα split jump ανάμεσα σε τοίχους.",
        "funFacts": [
            "Η χαρακτηριστική βαθιά φωνή του Sam Fisher ανήκε στον ηθοποιό Michael Ironside.",
            "Το 'Splinter Cell: Chaos Theory' (2005) θεωρείται από πολλούς το απόγειο της σειράς, συνοδευόμενο από soundtrack του Amon Tobin."
        ],
        "source": "https://en.wikipedia.org/wiki/Tom_Clancy%27s_Splinter_Cell",
        "tags": ["gaming", "splinter_cell", "ubisoft", "stealth", "sam_fisher"]
    },
    {
        "id": "gaming_hard_203",
        "text": "Ποιο arcade space combat shooter της Atari το 1983 υπήρξε το πρώτο παιχνίδι βασισμένο σε ταινία που χρησιμοποίησε έγχρωμα 3D διανυσματικά γραφικά (color vector graphics) και αυθεντική ψηφιοποιημένη φωνή του James Earl Jones ως Darth Vader;",
        "correct": "Star Wars (1983 arcade)",
        "distractors": [
            "Star Wars: The Empire Strikes Back",
            "Space Harrier",
            "I, Robot"
        ],
        "explanation": "Το Star Wars arcade του Mike Hally έβαλε τον παίκτη στο X-Wing του Luke Skywalker σε τρεις φάσεις: dogfight στο διάστημα, πτήση πάνω από την επιφάνεια του Death Star και το θρυλικό trench run για να ρίξει τις τορπίλες πρωτονίων στον εξαερισμό.",
        "funFacts": [
            "Η καμπίνα sit-down cockpit έδινε στον παίκτη την απόλυτη ψευδαίσθηση ότι πιλοτάρει πραγματικό X-Wing.",
            "Χρησιμοποίησε αυθεντικά ηχητικά δείγματα από την ταινία, συμπεριλαμβανομένης της φωνής του Alec Guinness ως Obi-Wan ('Use the Force, Luke')."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars_(1983_video_game)",
        "tags": ["gaming", "atari", "star_wars", "arcade", "vector"]
    },
    {
        "id": "gaming_hard_204",
        "text": "Ποιο ήταν το πρώτο εμπορικό video game στην ιστορία που χρησιμοποίησε πλήρως τρισδιάστατα πολύγωνα με textured mapping σε arcade πλακέτα (Namco System 22, 1993);",
        "correct": "Ridge Racer",
        "distractors": [
            "Daytona USA",
            "Virtua Racing",
            "Sega Rally"
        ],
        "explanation": "Ενώ το Virtua Racing της Sega χρησιμοποίησε flat polygons, το Ridge Racer της Namco ήταν το πρώτο arcade racer με πλήρως επικολλημένα textures (gouraud shading και texture filtering), εντυπωσιάζοντας τους παίκτες με τα drifts και τη μουσική.",
        "funFacts": [
            "Η μεταφορά του Ridge Racer στο PlayStation 1 το 1994 υπήρξε ο κύριος launch τίτλος που απέδειξε την υπεροχή της νέας κονσόλας της Sony.",
            "Στο loading screen του Ridge Racer στο PS1, ο παίκτης μπορούσε να παίξει ένα πλήρες minigame του κλασικού Galaxian."
        ],
        "source": "https://en.wikipedia.org/wiki/Ridge_Racer_(1993_video_game)",
        "tags": ["gaming", "namco", "ridge_racer", "arcade", "playstation"]
    },
    {
        "id": "gaming_hard_205",
        "text": "Ποιο πρωτοποριακό survival horror της Capcom (1998) σε σκηνοθεσία Hideki Kamiya εισήγαγε το σύστημα 'Zapping System' (Scenario A και Scenario B), όπου οι πράξεις του Leon επηρέαζαν άμεσα το playthrough της Claire;",
        "correct": "Resident Evil 2",
        "distractors": [
            "Resident Evil 3: Nemesis",
            "Resident Evil Code: Veronica",
            "Resident Evil Zero"
        ],
        "explanation": "Στο Resident Evil 2, η επιλογή όπλων ή ενεργειών στο Scenario A (π.χ. αν ο παίκτης έπαιρνε το machine gun στο αστυνομικό τμήμα R.P.D.) άλλαζε τα διαθέσιμα αντικείμενα στο Scenario B του άλλου χαρακτήρα, προσφέροντας 4 διαφορετικά σενάρια.",
        "funFacts": [
            "Η αρχική έκδοση του παιχνιδιού ('Resident Evil 1.5') ακυρώθηκε όταν είχε ολοκληρωθεί κατά 70% επειδή ο Shinji Mikami έκρινε ότι το σκηνικό ήταν υπερβολικά βαρετό.",
            "Στο Resident Evil 2 εμφανίστηκε για πρώτη φορά ο τρομακτικός Licker με τον εκτεθειμένο εγκέφαλο και τη μακριά γλώσσα."
        ],
        "source": "https://en.wikipedia.org/wiki/Resident_Evil_2",
        "tags": ["gaming", "resident_evil", "capcom", "kamiya", "playstation"]
    },
    {
        "id": "gaming_hard_206",
        "text": "Ποιο επικό action RPG της Square (1995) για το Super Famicom από τον Koichi Ishii χρησιμοποίησε κυκλικό μενού δακτυλίου (Ring Command) και μάχη σε πραγματικό χρόνο για τρεις ταυτόχρονους παίκτες;",
        "correct": "Secret of Mana (Seiken Densetsu 2)",
        "distractors": [
            "Trials of Mana",
            "Terranigma",
            "Illusion of Gaia"
        ],
        "explanation": "Το Secret of Mana ήταν πρωτοποριακό: υποστήριζε 3 παίκτες ταυτόχρονα μέσω του Super Multitap του SNES, διέθετε το καινοτόμο σύστημα μενού Ring Command που πάγωνε τη δράση και ένα ονειρικό soundtrack από τον Hiroki Kikuta.",
        "funFacts": [
            "Το παιχνίδι αναπτυσσόταν αρχικά για το ακυρωμένο CD-ROM add-on του Super Nintendo (SNES-CD / Nintendo PlayStation). Όταν η συμφωνία ναυάγησε, η Square αναγκάστηκε να κόψει σχεδόν το 40% του περιεχομένου.",
            "Το εναρκτήριο κομμάτι 'Fear of the Heavens' με το κάλεσμα της φάλαινας και το μελαγχολικό πιάνο θεωρείται κλασικό αριστούργημα των 16-bit."
        ],
        "source": "https://en.wikipedia.org/wiki/Secret_of_Mana",
        "tags": ["gaming", "snes", "square", "secret_of_mana", "rpg"]
    },
    {
        "id": "gaming_hard_207",
        "text": "Ποιο κλασικό point-and-click adventure της LucasArts (1993) από τους Tim Schafer και Dave Grossman παρακολουθούσε τους Bernard, Hoagie και Laverne σε τρεις διαφορετικές χρονικές εποχές (παρελθόν, παρόν, μέλλον) συνδεδεμένες με τις χρονομηχανές Chron-o-John;",
        "correct": "Day of the Tentacle (Maniac Mansion II)",
        "distractors": [
            "Sam & Max Hit the Road",
            "Full Throttle",
            "The Dig"
        ],
        "explanation": "Στο Day of the Tentacle, οι γρίφοι βασίζονταν στη μεταβολή του χρόνου: ο παίκτης έπλενε ένα άμαξα στο παρελθόν για να βρέξει στο μέλλον, άλλαζε το σχέδιο της αμερικανικής σημαίας για να φορέσει κοστούμι πλοκαμιού η Laverne ή έβαζε κρασί σε χρονοκάψουλα για να γίνει ξύδι.",
        "funFacts": [
            "Μέσα στο παιχνίδι, ο παίκτης μπορούσε να παίξει ολόκληρο το αρχικό 'Maniac Mansion' (1987) στον υπολογιστή του δωματίου του Ed Edison.",
            "Το Purple Tentacle απέκτησε υπερνοημοσύνη και πόθους για παγκόσμια κυριαρχία πίνοντας μολυσμένα τοξικά απόβλητα από το ποτάμι."
        ],
        "source": "https://en.wikipedia.org/wiki/Day_of_the_Tentacle",
        "tags": ["gaming", "lucasarts", "day_of_the_tentacle", "schafer", "adventure"]
    },
    {
        "id": "gaming_hard_208",
        "text": "Ποιο ήταν το όνομα της επαναστατικής μηχανής adventure games της Sierra On-Line που διαδέχτηκε το AGI το 1988, εισάγοντας ανάλυση 320x200 στα 16 χρώματα, υποστήριξη καρτών ήχου Roland MT-32 και πλήρη έλεγχο με ποντίκι;",
        "correct": "SCI (Sierra Creative Interpreter)",
        "distractors": [
            "SCUMM",
            "AGI 2.0",
            "Virtual Theater"
        ],
        "explanation": "Το SCI (Sierra Creative Interpreter), γραμμένο από τον Jeff Stephenson, επέτρεψε στη Sierra να περάσει από τον απλό text parser στον χειρισμό με ποντίκι και σε πολυφωνική ορχηστρική μουσική, ξεκινώντας με το 'King's Quest IV: The Perils of Rosella'.",
        "funFacts": [
            "Το King's Quest IV ήταν το πρώτο παιχνίδι για PC στην ιστορία που υποστήριξε την κάρτα ήχου Roland MT-32, αφήνοντας άφωνους τους παίκτες με την ποιότητα της μουσικής.",
            "Η πρωταγωνίστρια Rosella ήταν η πρώτη γυναίκα πρωταγωνίστρια σε mainstream graphic adventure game."
        ],
        "source": "https://en.wikipedia.org/wiki/Sierra%27s_Creative_Interpreter",
        "tags": ["gaming", "sierra", "sci", "adventure", "hardware"]
    },
    {
        "id": "gaming_hard_209",
        "text": "Ποιο επικό platformer της Nintendo στο Super Nintendo (1995), σχεδιασμένο από τον Takashi Tezuka και τον Shigeru Miyamoto, χρησιμοποίησε χειροποίητο στυλ γραφικών με κηρομπογιές και νερομπογιές για να αντιταχθεί στα προσχεδιασμένα γραφικά του Donkey Kong Country;",
        "correct": "Super Mario World 2: Yoshi's Island",
        "distractors": [
            "Super Mario RPG",
            "Donkey Kong Country 2",
            "Kirby's Dream Land 3"
        ],
        "explanation": "Όταν η διοίκηση της Nintendo ζήτησε φωτορεαλιστικά προσχεδιασμένα γραφικά τύπου SGI όπως το DKC, ο Miyamoto εξοργίστηκε και σχεδίασε σκόπιμα το Yoshi's Island με ένα εκπληκτικό παιδικό στυλ παστέλ και κηρομπογιάς, υποστηριζόμενο από το τσιπ Super FX 2.",
        "funFacts": [
            "Το χαρακτηριστικό κλάμα του Baby Mario όταν πέφτει από την πλάτη του Yoshi έγινε ένα από τα πιο νευρικά ηχητικά εφέ στα platformers.",
            "Το παιχνίδι χρησιμοποίησε το τσιπ Super FX 2 για παραμορφώσεις sprites (morphing), περιστροφές και γιγάντια bosses."
        ],
        "source": "https://en.wikipedia.org/wiki/Yoshi%27s_Island",
        "tags": ["gaming", "snes", "yoshi", "mario", "miyamoto"]
    },
    {
        "id": "gaming_hard_210",
        "text": "Ποιο είναι το όνομα του ιστορικού πρώτου side-scrolling beat 'em up της Technōs Japan (1987) από τον Yoshihisa Kishimoto, το οποίο καθιέρωσε τις αρχές του είδους με τους δίδυμους Billy και Jimmy Lee να πολεμούν τη συμμορία Black Warriors;",
        "correct": "Double Dragon",
        "distractors": [
            "Final Fight",
            "Streets of Rage",
            "Renegade (Nekketsu Kōha Kunio-kun)"
        ],
        "explanation": "Το Double Dragon εισήγαγε το συνεργατικό παιχνίδι δύο παικτών ταυτόχρονα (co-op), όπλα που έπεφταν από τους εχθρούς (ρόπαλα, μαχαίρια, μαστίγια) και τη διάσημη τελική αναμέτρηση όπου οι δύο αδελφοί μονομαχούσαν μεταξύ τους για το φιλί της Marian.",
        "funFacts": [
            "Ο Kishimoto άντλησε έμπνευση για τον Billy Lee από τον Bruce Lee και για τον τίτλο από την ταινία Enter the Dragon (1973).",
            "Η κλωτσιά με αγκωνιά (elbow punch) ήταν τόσο ισχυρή στην αρχική έκδοση arcade που οι έμπειροι παίκτες μπορούσαν να τερματίσουν το παιχνίδι χρησιμοποιώντας σχεδόν αποκλειστικά αυτήν την κίνηση."
        ],
        "source": "https://en.wikipedia.org/wiki/Double_Dragon",
        "tags": ["gaming", "arcade", "double_dragon", "beat_em_up", "retro"]
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

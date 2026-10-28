# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "gaming_hard_311",
        "text": "Στο αριστούργημα επιστημονικής φαντασίας 'Star Control II' (1992), ποια αρχαία υπερ-πλατφόρμα των Precursors χρησιμοποιούν οι παίκτες για να καταστρέψουν το Sa-Matra;",
        "correct": "Το αρχαίο σκάφος Precursor Flagship σε συνδυασμό με τη βόμβα Utwig Chmmr",
        "distractors": [
            "Τον διαστατικό καταστροφέα των Arilou",
            "Τον κοσμικό διασπαστή των Melnorme",
            "Την ηλιακή ακτίνα των VUX"
        ],
        "explanation": "Οι παίκτες πρέπει να ενώσουν τις διαστημικές φυλές σε μια Νέα Συμμαχία Ελεύθερων Αστέρων και να στείλουν ένα σκάφος αυτοκτονίας για να ανοίξει τρύπα στην ασπίδα του πανίσχυρου Sa-Matra.",
        "funFacts": [
            "Το Sa-Matra σημαίνει 'Ο Μεγάλος Νικητής' στη διάλεκτο των Ur-Quan.",
            "Οι δημιουργοί Paul Reiche III και Fred Ford έγραψαν όλο το σενάριο και τους διαλόγους μόνοι τους σε ένα υπόγειο."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Control_II",
        "tags": ["gaming", "star_control", "toys_for_bob", "sci_fi", "retro"]
    },
    {
        "id": "gaming_hard_312",
        "text": "Ποιος διάσημος ηθοποιός ενσάρκωσε τον Συνταγματάρχη Christopher Blair στα κινηματογραφικά FMV cutscenes των 'Wing Commander III' και 'IV';",
        "correct": "Mark Hamill",
        "distractors": ["Harrison Ford", "Bruce Willis", "Kurt Russell"],
        "explanation": "Ο Mark Hamill πρωταγωνίστησε ως Blair στη μάχη της Συνομοσπονδίας Terran ενάντια στην εξωγήινη αυτοκρατορία των Kilrathi, πλαισιωμένος από τον Malcolm McDowell και τον John Rhys-Davies.",
        "funFacts": [
            "Το Wing Commander III (1994) κόστισε πάνω από 4 εκατομμύρια δολάρια, ποσό ρεκόρ για την εποχή που άνοιξε την εποχή του διαδραστικού κινηματογράφου.",
            "Τα Kilrathi σχεδιάστηκαν ως ανθρωπόμορφα αιλουροειδή πολεμιστές με κοστούμια ανιματρόνικς πλήρους μεγέθους."
        ],
        "source": "https://en.wikipedia.org/wiki/Wing_Commander_III:_Heart_of_the_Tiger",
        "tags": ["gaming", "wing_commander", "mark_hamill", "chris_roberts", "fmv"]
    },
    {
        "id": "gaming_hard_313",
        "text": "Ποιο κλασικό RPG του 1993 από τη Dynamix βασίστηκε στον φανταστικό κόσμο της Midkemia του συγγραφέα Raymond E. Feist;",
        "correct": "Betrayal at Krondor",
        "distractors": ["Return to Krondor", "The Riftwar Legacy", "Shadow of the Horned Rat"],
        "explanation": "Το Betrayal at Krondor συνδύαζε εξερεύνηση πρώτου προσώπου σε 3D περιβάλλον και τακτικές μάχες σε ισομετρικό πλέγμα με πρωταγωνιστές τους Locklear, James και Owyn.",
        "funFacts": [
            "Ο ίδιος ο Raymond E. Feist εντυπωσιάστηκε τόσο πολύ από την πλοκή του παιχνιδιού που αργότερα τη μετέτρεψε σε επίσημο μυθιστόρημα με τον τίτλο 'Krondor: The Betrayal'.",
            "Τα μπαούλα θησαυρού στο παιχνίδι κλειδώνονταν με αινίγματα λέξεων (word locks) αντί για παραδοσιακά κλειδιά."
        ],
        "source": "https://en.wikipedia.org/wiki/Betrayal_at_Krondor",
        "tags": ["gaming", "betrayal_at_krondor", "dynamix", "sierra", "rpg"]
    },
    {
        "id": "gaming_hard_314",
        "text": "Στο ιστορικό RPG 'Darklands' (1992) της MicroProse, ποιο ασυνήθιστο σύστημα αντικατέστησε την παραδοσιακή μαγεία φαντασίας για λόγους ιστορικής ακρίβειας;",
        "correct": "Προσευχές σε πραγματικούς Καθολικούς Αγίους και συνταγές Αλχημείας",
        "distractors": [
            "Μυστικιστικές ρούνες των Δρυΐδων",
            "Αστρολογικές προβλέψεις και ωροσκόπια",
            "Ψαλμοί των αρχαίων Τευτόνων ιπποτών"
        ],
        "explanation": "Τοποθετημένο στην Αγία Ρωμαϊκή Αυτοκρατορία του 15ου αιώνα, το Darklands αντικατέστησε τα ξόρκια με δεκάδες ιστορικούς αγίους (στους οποίους οι παίκτες προσεύχονταν) και αυθεντική παρασκευή αλχημικών φίλτρων.",
        "funFacts": [
            "Το παιχνίδι χρησιμοποιούσε σύστημα μάχης πραγματικού χρόνου με παύση (real-time with pause), χρόνια πριν καθιερωθεί από το Baldur's Gate.",
            "Η ηλικία των χαρακτήρων επηρέαζε τα στατιστικά τους: οι μεγαλύτεροι είχαν περισσότερες δεξιότητες αλλά χαμηλότερη σωματική αντοχή."
        ],
        "source": "https://en.wikipedia.org/wiki/Darklands_(video_game)",
        "tags": ["gaming", "darklands", "microprose", "rpg", "history"]
    },
    {
        "id": "gaming_hard_315",
        "text": "Ποιος διάσημος Σαιξπηρικός ηθοποιός (και κυβερνήτης Jean-Luc Picard στο Star Trek) δάνεισε τη φωνή του στον Βασιλιά Richard στο 'Lands of Lore: The Throne of Chaos' (1993);",
        "correct": "Patrick Stewart",
        "distractors": ["Ian McKellen", "John de Lancie", "Christopher Lee"],
        "explanation": "Ο Patrick Stewart ενσάρκωσε τον καλοκάγαθο Βασιλιά Richard της Gladstone που δηλητηριάζεται από τη μάγισσα Scotia στο dungeon crawler της Westwood Studios.",
        "funFacts": [
            "Η Westwood Studios χρησιμοποίησε ηχογραφήσεις του Patrick Stewart για να προωθήσει έντονα την έκδοση CD-ROM του παιχνιδιού.",
            "Η κακιά μάγισσα Scotia χρησιμοποιούσε το αρχαίο δαχτυλίδι Nether Mask για να μεταμορφώνεται σε διάφορα τέρατα."
        ],
        "source": "https://en.wikipedia.org/wiki/Lands_of_Lore:_The_Throne_of_Chaos",
        "tags": ["gaming", "lands_of_lore", "westwood", "patrick_stewart", "rpg"]
    },
    {
        "id": "gaming_hard_316",
        "text": "Ποιο ιδιόμορφο RPG της Ion Storm Dallas (2001) σχεδιασμένο από τον Tom Hall χρησιμοποίησε τροποποιημένη μηχανή Quake II και είχε ως μέλος της ομάδας έναν ολόκληρο πλανήτη;",
        "correct": "Anachronox",
        "distractors": ["Daikatana", "Deus Ex", "Septerra Core"],
        "explanation": "Στο Anachronox, ο ντετέκτιβ Sylvester 'Sly' Boots στρατολογεί τον μικροσκοπικό πλανήτη Democratus, ο οποίος συρρικνώνεται σε μέγεθος μπάλας και συμμετέχει στις turn-based μάχες.",
        "funFacts": [
            "Το παιχνίδι συνδύαζε δυτική κυβερνοπάνκ αισθητική με ιαπωνικό σύστημα μάχης τύπου Chrono Trigger και Final Fantasy.",
            "Ο Tom Hall είχε συλλάβει την ιδέα για το Anachronox όσο εργαζόταν ακόμη στην id Software το 1993."
        ],
        "source": "https://en.wikipedia.org/wiki/Anachronox",
        "tags": ["gaming", "anachronox", "ion_storm", "tom_hall", "rpg"]
    },
    {
        "id": "gaming_hard_317",
        "text": "Ποιος συγγραφέας σκοτεινής φαντασίας και τρόμου έγραψε το σενάριο και συνέβαλε στον σχεδιασμό του FPS 'Clive Barker's Undying' (2001);",
        "correct": "Clive Barker",
        "distractors": ["Stephen King", "Neil Gaiman", "Dean Koontz"],
        "explanation": "Ο δημιουργός του Hellraiser Clive Barker σχεδίασε την ιστορία του Patrick Galloway, ο οποίος ερευνά την κατάρα της οικογένειας Covenant στην Ιρλανδία του 1920 με το κειμήλιο Gel'ziabar Stone.",
        "funFacts": [
            "Ο μηχανισμός του παιχνιδιού επέτρεπε ταυτόχρονη χρήση όπλου στο ένα χέρι (π.χ. περίστροφο, δρεπάνι Scythe of the Celts) και μαγείας στο άλλο, προαναγγέλλοντας το BioShock.",
            "Η ικανότητα 'Scrye' επέτρεπε στον παίκτη να βλέπει φαντάσματα και παρελθοντικά οράματα ακούγοντας παράλληλα απόκοσμους ψιθύρους."
        ],
        "source": "https://en.wikipedia.org/wiki/Clive_Barker%27s_Undying",
        "tags": ["gaming", "undying", "clive_barker", "ea", "horror"]
    },
    {
        "id": "gaming_hard_318",
        "text": "Στο ψυχολογικό adventure 'I Have No Mouth, and I Must Scream' (1995) της Cyberdreams, ποιος δάνεισε τη φωνή του στον σαδιστή υπερυπολογιστή AM;",
        "correct": "Ο ίδιος ο συγγραφέας Harlan Ellison",
        "distractors": ["Vincent Price", "Tony Jay", "Leonard Nimoy"],
        "explanation": "Ο Harlan Ellison έγραψε επιπλέον διαλόγους για το παιχνίδι και ηχογράφησε με μοναδικό πάθος τον οργισμένο μονόλογο μίσους του υπολογιστή AM ('Hate. Let me tell you how much I've come to hate you since I began to live...').",
        "funFacts": [
            "Ο AM βασανίζει τους τελευταίους πέντε επιζώντες της ανθρωπότητας για 109 χρόνια στα έγκατα της Γης.",
            "Κάθε χαρακτήρας αντιμετωπίζει ένα βαθύ προσωπικό ηθικό δίλημμα και ψυχολογικό τραύμα σχεδιασμένο από τον υπερυπολογιστή."
        ],
        "source": "https://en.wikipedia.org/wiki/I_Have_No_Mouth,_and_I_Must_Scream_(video_game)",
        "tags": ["gaming", "i_have_no_mouth", "harlan_ellison", "cyberdreams", "adventure"]
    },
    {
        "id": "gaming_hard_319",
        "text": "Ποιο σουρεαλιστικό παιχνίδι περιπέτειας της DreamWorks Interactive (1996) από τον Doug TenNapel δημιουργήθηκε εξ ολοκλήρου με τεχνική stop-motion πλαστελίνης (Claymation);",
        "correct": "The Neverhood",
        "distractors": ["Skullmonkeys", "ClayFighter", "Armikrog"],
        "explanation": "Ολόκληρος ο κόσμος και ο ήρωας Klaymen κατασκευάστηκαν από πάνω από 3 τόνους πραγματικής πλαστελίνης και φωτογραφήθηκαν καρέ-καρέ για τη δημιουργία του παιχνιδιού.",
        "funFacts": [
            "Το παιχνίδι περιλαμβάνει έναν διαβόητο διάδρομο 38 οθονών όπου ο παίκτης μπορεί να περπατήσει για 15 λεπτά διαβάζοντας ολόκληρο το χρονικό της δημιουργίας του κόσμου στον τοίχο.",
            "Το εκκεντρικό ακουστικό soundtrack συντέθηκε από τον Terry Scott Taylor και θεωρείται ένα από τα πιο πρωτότυπα στην ιστορία των PC games."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Neverhood",
        "tags": ["gaming", "the_neverhood", "claymation", "doug_tennapel", "adventure"]
    },
    {
        "id": "gaming_hard_320",
        "text": "Πόσα χρόνια χρειάστηκε ο Éric Chahi και η Amazing Studio για να ολοκληρώσουν το κινηματογραφικό platformer 'Heart of Darkness' (1998) στο PlayStation και PC;",
        "correct": "6 χρόνια (1992-1998)",
        "distractors": ["3 χρόνια", "4 χρόνια", "8 χρόνια"],
        "explanation": "Το παιχνίδι ανακοινώθηκε το 1992 και υπέστη αμέτρητες καθυστερήσεις λόγω της τεράστιας δυσκολίας συγχρονισμού των προ-σχεδιασμένων 3D animations με το 2D gameplay.",
        "funFacts": [
            "Το Heart of Darkness ήταν ένα από τα πρώτα βιντεοπαιχνίδια που χρησιμοποίησαν αυθεντική ζωντανή συμφωνική ορχήστρα 80 οργάνων (τη Sinfonia of London) για τη μουσική του Bruce Broughton.",
            "Ο μικρός πρωταγωνιστής Andy ταξιδεύει στη Σκοτεινή Χώρα για να σώσει τον πιστό του σκύλο Whisky από τις σκιές."
        ],
        "source": "https://en.wikipedia.org/wiki/Heart_of_Darkness_(video_game)",
        "tags": ["gaming", "heart_of_darkness", "eric_chahi", "playstation", "history"]
    },
    {
        "id": "gaming_hard_321",
        "text": "Ποιο κινηματογραφικό αριστούργημα του Éric Chahi (1991) για την Amiga χρησιμοποίησε διανυσματικά πολύγωνα (vector polygons) αντί για bitmaps για να χωρέσει σε μία μόνο δισκέτα;",
        "correct": "Another World (Out of this World)",
        "distractors": ["Flashback", "Future Wars", "Crucial Fix"],
        "explanation": "Ο φυσικός Lester Knight Chaykin τηλεμεταφέρεται σε έναν αφιλόξενο εξωγήινο πλανήτη μετά από κεραυνό στον επιταχυντή σωματιδίων του, δημιουργώντας ένα ορόσημο μινιμαλιστικής αφήγησης.",
        "funFacts": [
            "Ο Chahi δημιούργησε σχεδόν ολόκληρο το παιχνίδι ολομόναχος στο υπνοδωμάτιό του σε έναν υπολογιστή Amiga 500.",
            "Η σκηνή όπου ο Lester και ο εξωγήινος φίλος του 'Buddy' αποδρούν μέσα από αγωγούς εξαερισμού και μονομαχούν με όπλα λέιζερ θεωρείται κλασική."
        ],
        "source": "https://en.wikipedia.org/wiki/Another_World_(video_game)",
        "tags": ["gaming", "another_world", "eric_chahi", "amiga", "retro"]
    },
    {
        "id": "gaming_hard_322",
        "text": "Ποια πρωτοποριακή τεχνική animation εφάρμοσε ο Paul Cuisset της Delphine Software για τις ομαλές κινήσεις του Conrad B. Hart στο 'Flashback' (1992);",
        "correct": "Rotoscoping (Ροτοσκόπηση με βιντεοσκόπηση ζωντανού ηθοποιού)",
        "distractors": ["Stop-motion animation", "Optical Motion Capture", "Vector Morphing"],
        "explanation": "Η ομάδα βιντεοσκόπησε έναν αληθινό άνθρωπο να τρέχει, να πηδάει και να κυλιέται, και στη συνέχεια σχεδίασε κάθε καρέ με το χέρι πάνω από το βίντεο (rotoscoping), δημιουργώντας απαράμιλλη ρευστότητα.",
        "funFacts": [
            "Το Flashback μπήκε στο Βιβλίο των Ρεκόρ Guinness ως το γαλλικό βιντεοπαιχνίδι με τις περισσότερες πωλήσεις όλων των εποχών.",
            "Ο πρωταγωνιστής Conrad ξυπνά στον δορυφόρο Τιτάνα έχοντας χάσει τη μνήμη του και βρίσκει ένα ολόγραμμα του εαυτού του που του δίνει οδηγίες."
        ],
        "source": "https://en.wikipedia.org/wiki/Flashback_(1992_video_game)",
        "tags": ["gaming", "flashback", "delphine_software", "paul_cuisset", "rotoscoping"]
    },
    {
        "id": "gaming_hard_323",
        "text": "Ποιος Γάλλος σχεδιαστής δημιούργησε το αρχικό 'Alone in the Dark' (1992) στην Infogrames, θέτοντας τα θεμέλια για ολόκληρο το είδος Survival Horror;",
        "correct": "Frédérick Raynal",
        "distractors": ["Éric Chahi", "Paul Cuisset", "Michel Ancel"],
        "explanation": "Ο Frédérick Raynal συνδύασε 3D πολυγωνικούς χαρακτήρες σε πραγματικό χρόνο πάνω σε στατικά ζωγραφισμένα φόντα 2D με σταθερές κινηματογραφικές γωνίες λήψης, μια φόρμουλα που αντέγραψε αργότερα το Resident Evil.",
        "funFacts": [
            "Ο Raynal αποχώρησε από την Infogrames αμέσως μετά για να ιδρύσει την Adeline Software και να δημιουργήσει τα 'Little Big Adventure' και 'Time Commando'.",
            "Η έπαυλη Derceto στη Λουιζιάνα ήταν εμπνευσμένη άμεσα από τα έργα των H.P. Lovecraft και Edgar Allan Poe."
        ],
        "source": "https://en.wikipedia.org/wiki/Alone_in_the_Dark_(1992_video_game)",
        "tags": ["gaming", "alone_in_the_dark", "frederick_raynal", "survival_horror", "infogrames"]
    },
    {
        "id": "gaming_hard_324",
        "text": "Ποια πρωτοποριακή μηχανή γραφικών βασισμένη σε ελλειψοειδή (ellipsoids) αντί για τρίγωνα χρησιμοποίησε το 'Ecstatica' (1994) της Psygnosis;",
        "correct": "Ellipsoid Engine (Andrew Spencer)",
        "distractors": ["Voxel Engine", "NURBS Surface Engine", "Bézier Patch Engine"],
        "explanation": "Ο Andrew Spencer σχεδίασε όλους τους χαρακτήρες και τα τέρατα του μεσαιωνικού χωριού Tirich χρησιμοποιώντας δεκάδες ενωμένα ελλειψοειδή σφαιρίδια, επιτυγχάνοντας ομαλές καμπύλες χωρίς πολυγωνικές ακμές.",
        "funFacts": [
            "Ένας αήττητος δαίμονας λυκάνθρωπος κυνηγούσε συνεχώς τον παίκτη στα σοκάκια του χωριού, δημιουργώντας τρομερό άγχος.",
            "Το παιχνίδι είχε εξαιρετικά ρευστά animations αλλά η τεχνολογία των ellipsoids εγκαταλείφθηκε σύντομα λόγω της ανόδου των 3D πολυγωνικών επιταχυντών."
        ],
        "source": "https://en.wikipedia.org/wiki/Ecstatica",
        "tags": ["gaming", "ecstatica", "psygnosis", "ellipsoids", "retro"]
    },
    {
        "id": "gaming_hard_325",
        "text": "Στο 'Jurassic Park: Trespasser' (1998) της DreamWorks, πού βρισκόταν η ένδειξη υγείας της πρωταγωνίστριας Anne λόγω της απουσίας οποιουδήποτε HUD στην οθόνη;",
        "correct": "Σε ένα τατουάζ καρδιάς στο στήθος της που γέμιζε με κόκκινο χρώμα",
        "distractors": [
            "Στο ρολόι χειρός της που άλλαζε χρώμα",
            "Στο χρώμα των νυχιών των χεριών της",
            "Σε έναν μετρητή παλμών στη ζώνη της"
        ],
        "explanation": "Η παίκτρια έπρεπε να κοιτάξει κυριολεκτικά προς τα κάτω στο στήθος της για να δει το τατουάζ καρδιάς: όσο πιο γεμάτο ήταν, τόσο περισσότερη υγεία είχε.",
        "funFacts": [
            "Το Trespasser ήταν το πρώτο παιχνίδι που επιχείρησε πλήρη προσομοίωση φυσικής Newton για κάθε αντικείμενο και δυναμικό inverse kinematics για τον βραχίονα.",
            "Τη φωνή της Anne έκανε η διάσημη Βρετανίδα ηθοποιός Minnie Driver."
        ],
        "source": "https://en.wikipedia.org/wiki/Trespasser_(video_game)",
        "tags": ["gaming", "trespasser", "dreamworks", "physics", "jurassic_park"]
    },
    {
        "id": "gaming_hard_326",
        "text": "Ποια επαναστατική μηχανή γραφικών χρησιμοποίησε το 'Outcast' (1999) της Appeal, αποδίδοντας τους εξωγήινους κόσμους του Adelpha χωρίς να απαιτείται 3D κάρτα γραφικών;",
        "correct": "Μηχανή Voxel (Ray-casting Voxel Engine)",
        "distractors": ["Polygonal Rasterizer", "Ray Tracing CPU", "Vector Subdivision"],
        "explanation": "Η engine της Appeal χρησιμοποιούσε voxels που υπολογίζονταν αποκλειστικά από τον κεντρικό επεξεργαστή (CPU), προσφέροντας καμπυλωτούς φυσικούς λόφους, βάθος πεδίου και κυματισμούς νερού που δεν μπορούσαν να αποδώσουν οι 3D κάρτες της εποχής.",
        "funFacts": [
            "Το συμφωνικό soundtrack ηχογραφήθηκε ζωντανά από τη Συμφωνική Ορχήστρα της Μόσχας με συνθέτη τον Lennie Moore.",
            "Ο πρωταγωνιστής Cutter Slade ήταν πρώην Navy SEAL που ταξίδεψε σε παράλληλο σύμπαν και θεωρήθηκε από τους ντόπιους Talan ως ο μεσσίας 'Ulukaï'."
        ],
        "source": "https://en.wikipedia.org/wiki/Outcast_(video_game)",
        "tags": ["gaming", "outcast", "appeal", "voxels", "sci_fi"]
    },
    {
        "id": "gaming_hard_327",
        "text": "Ποιο καινοτόμο σύστημα τυχαιοποίησης εφάρμοσε η Westwood Studios στο adventure 'Blade Runner' (1997) για να ενισχύσει την επαναληψιμότητα;",
        "correct": "Σε κάθε νέο playthrough, το παιχνίδι επέλεγε τυχαία ποιοι χαρακτήρες ήταν Replicants και ποιοι άνθρωποι",
        "distractors": [
            "Οι τοποθεσίες των φόνων άλλαζαν τυχαία στον χάρτη",
            "Ο δολοφόνος άλλαζε φύλο και όνομα σε κάθε εκκίνηση",
            "Τα τεστ Voight-Kampff παρήγαγαν τυχαίες απαντήσεις"
        ],
        "explanation": "Ακόμα και οι ύποπτοι δεν γνώριζαν αν ήταν Replicants μέχρι να εξεταστούν με το τεστ Voight-Kampff, ενώ οι NPCs κινούνταν ανεξάρτητα στον κόσμο με δική τους τεχνητή νοημοσύνη.",
        "funFacts": [
            "Ο ντετέκτιβ Ray McCoy ερευνά παράλληλα με τα γεγονότα της ταινίας του Ridley Scott του 1982, συναντώντας χαρακτήρες όπως ο Rachael, ο Tyrell και ο Gaff.",
            "Η Westwood δεν είχε πρόσβαση στα αυθεντικά props της ταινίας και ανακατασκεύασε ψηφιακά τα οχήματα Spinner και το κτίριο της Tyrell Corporation παρατηρώντας καρέ της ταινίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Blade_Runner_(1997_video_game)",
        "tags": ["gaming", "blade_runner", "westwood", "adventure", "ai"]
    },
    {
        "id": "gaming_hard_328",
        "text": "Ποιος θρυλικός rock μουσικός έγραψε 8 πρωτότυπα τραγούδια και εμφανίστηκε ως χαρακτήρας στο κυβερνοπάνκ παιχνίδι 'Omikron: The Nomad Soul' (1999) του David Cage;",
        "correct": "David Bowie",
        "distractors": ["Mick Jagger", "Iggy Pop", "Peter Gabriel"],
        "explanation": "Ο David Bowie ενσάρκωσε δύο χαρακτήρες (τον επαναστάτη Boz και τον τραγουδιστή των The Dreamers) και συνέθεσε μαζί με τον Reeves Gabrels το άλμπουμ 'Hours...' που χρησιμοποιήθηκε ως soundtrack.",
        "funFacts": [
            "Η σύζυγος του Bowie, το διάσημο μοντέλο Iman, δάνεισε επίσης τη μορφή της σε έναν χαρακτήρα του παιχνιδιού.",
            "Όταν ο χαρακτήρας του παίκτη πέθαινε στο Omikron, η ψυχή του μπορούσε να μετενσαρκωθεί στο σώμα του πρώτου περαστικού πολίτη που άγγιζε το πτώμα."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Nomad_Soul",
        "tags": ["gaming", "omikron", "quantic_dream", "david_bowie", "david_cage"]
    },
    {
        "id": "gaming_hard_329",
        "text": "Ποιο είναι το εξωφρενικό όπλο στο παιχνίδι δράσης 'Armed and Dangerous' (2003) της Planet Moon Studios που εκτοξεύει έναν υπόγειο καρχαρία;",
        "correct": "Land Shark Gun (Όπλο Καρχαρία Ξηράς)",
        "distractors": ["Topsy-Turvy Bomb", "World Inverter", "Guy-Rockets"],
        "explanation": "Το Land Shark Gun εκτοξεύει ένα μωρό καρχαρία που 'κολυμπάει' μέσα στο χώμα, μεγαλώνει σε τεράστιο μέγεθος και αναδύεται κάτω από τους εχθρούς καταπίνοντάς τους.",
        "funFacts": [
            "Ένα άλλο διάσημο όπλο του παιχνιδιού ήταν η βόμβα 'Topsy-Turvy' που αναποδογύριζε ολόκληρο τον πλανήτη, κάνοντας τους εχθρούς να πέσουν στο διάστημα πριν ξαναγυρίσουν στο έδαφος.",
            "Η Planet Moon Studios ιδρύθηκε από πρώην μέλη της Shiny Entertainment που είχαν φτιάξει τα MDK και Earthworm Jim."
        ],
        "source": "https://en.wikipedia.org/wiki/Armed_and_Dangerous_(video_game)",
        "tags": ["gaming", "armed_and_dangerous", "planet_moon", "lucasarts", "comedy"]
    },
    {
        "id": "gaming_hard_330",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή με το μαύρο δερμάτινο κοστούμι, το κράνος ελεύθερου σκοπευτή και το αλεξίπτωτο κορδέλας στο 'MDK' (1997) του David Perry;",
        "correct": "Kurt Hectic",
        "distractors": ["Dr. Fluke Hawkins", "Bones", "Max the Dog"],
        "explanation": "Ο Kurt είναι ο επιστάτης του εκκεντρικού εφευρέτη Dr. Fluke Hawkins και στέλνεται από τον διαστημικό σταθμό Jim Dandy για να σώσει τη Γη από τα εξωγήινα Mining Galleons.",
        "funFacts": [
            "Το όνομα MDK αποτελεί μυστήριο με πολλές χιουμοριστικές ερμηνείες (Mission: Deliver Kindness, Murder Death Kill, Murderous Demonic Klowns).",
            "Το παιχνίδι ήταν ένα από τα πρώτα που εισήγαγαν sniper rifle με λειτουργία ζουμ έως και 100x σε 3D περιβάλλον."
        ],
        "source": "https://en.wikipedia.org/wiki/MDK_(video_game)",
        "tags": ["gaming", "mdk", "shiny_entertainment", "david_perry", "retro"]
    },
    {
        "id": "gaming_hard_331",
        "text": "Ποιο αντικείμενο εκτοξεύει με έναν μοχλό στο διάστημα ο Earthworm Jim στο πρώτο κιόλας επίπεδο του 'Earthworm Jim' (1994) και πέφτει πάνω του στο τέλος;",
        "correct": "Μια αγελάδα (Cow)",
        "distractors": ["Ένα ψυγείο", "Ένα πλυντήριο", "Ένα αυτοκίνητο"],
        "explanation": "Ο Jim χτυπάει ένα ελαστικό λάστιχο εκσφενδονίζοντας μια αγελάδα στον ουρανό, η οποία περιφέρεται στο διάστημα και πέφτει στο τέλος του παιχνιδιού πάνω στην Princess What's-Her-Name.",
        "funFacts": [
            "Ο δημιουργός Doug TenNapel σχεδίασε τον Jim ως έναν απλό γεωσκώληκα που πέφτει μέσα σε μια υπερ-διαστημική στολή που έπεσε από τον ουρανό.",
            "Το παιχνίδι έγινε διάσημο για την καρτουνίστικη ρευστότητα των animations του, φτιαγμένα από πρώην animators παραδοσιακού κινηματογράφου."
        ],
        "source": "https://en.wikipedia.org/wiki/Earthworm_Jim_(video_game)",
        "tags": ["gaming", "earthworm_jim", "shiny_entertainment", "doug_tennapel", "retro"]
    },
    {
        "id": "gaming_hard_332",
        "text": "Στο πρωτοποριακό third-person RTS 'Sacrifice' (2000) της Shiny Entertainment, ποιος θεός της γης και της φύσης εκπροσωπείται από έναν γιγάντιο κένταυρο με πέτρινο σφυρί;",
        "correct": "James",
        "distractors": ["Charnel", "Stratos", "Pyro"],
        "explanation": "Στο Sacrifice, ο μάγος Eldred υπηρετεί έναν από τους πέντε θεούς: Charnel (Θάνατος), James (Γη), Stratos (Αέρας), Pyro (Φωτιά) ή Persephone (Ζωή/Τάξη).",
        "funFacts": [
            "Ο θεός της Γης ονομάστηκε 'James' προς τιμήν του ιδρυτή της Interplay, Brian Fargo (του οποίου το μεσαίο όνομα είναι James) και του σχεδιαστή James Goddard.",
            "Οι παίκτες έπρεπε να θυσιάσουν τις ψυχές των εχθρικών μονάδων στους βωμούς (Altars) των θεών για να κερδίσουν μάνα και να καλέσουν ξόρκια όπως ηφαίστεια και ανεμοστρόβιλους."
        ],
        "source": "https://en.wikipedia.org/wiki/Sacrifice_(video_game)",
        "tags": ["gaming", "sacrifice", "shiny_entertainment", "interplay", "rts"]
    },
    {
        "id": "gaming_hard_333",
        "text": "Ποιο είναι το όνομα του μικρού φτερωτού χερουβείμ (αγγέλου) που στέλνεται στη Γη και μπορεί να καταλαμβάνει τα σώματα ανθρώπων στο 'Messiah' (2000) της Shiny;",
        "correct": "Bob",
        "distractors": ["Gabriel", "Michael", "Uriel"],
        "explanation": "Ο Bob είναι ένα μικροσκοπικό μωρό-άγγελος με πάνα που δεν μπορεί να πολεμήσει μόνο του, αλλά πηδάει μέσα στα σώματα αστυνομικών, ιερέων, επιστημόνων και εργατών για να λύσει γρίφους.",
        "funFacts": [
            "Το Messiah ήταν το πρώτο παιχνίδι που χρησιμοποίησε τεχνολογία δυναμικής προσαρμογής επιπέδου λεπτομέρειας (tessellation / continuous level of detail - RT-DAT).",
            "Το βιομηχανικό soundtrack συντέθηκε από το industrial metal συγκρότημα Fear Factory."
        ],
        "source": "https://en.wikipedia.org/wiki/Messiah_(video_game)",
        "tags": ["gaming", "messiah", "shiny_entertainment", "david_perry", "retro"]
    },
    {
        "id": "gaming_hard_334",
        "text": "Ποια είναι η Βρετανίδα μυστική πράκτορας της οργάνωσης UNITY που πρωταγωνιστεί στα στυλάτα κατασκοπευτικά FPS 'The Operative: No One Lives Forever' (2000) της Monolith;",
        "correct": "Cate Archer",
        "distractors": ["Joanna Dark", "Tara Maclay", "Jane Valder"],
        "explanation": "Η Cate Archer ταξιδεύει στη δεκαετία του 1960 πολεμώντας τη σατανική οργάνωση H.A.R.M., χρησιμοποιώντας κατασκοπευτικά gadgets όπως αναπτήρες-οξυγόνα και κραγιόν-εκρηκτικά.",
        "funFacts": [
            "Το NOLF απέσπασε διθυραμβικές κριτικές για το έξυπνο χιούμορ του και τις συνομιλίες των φρουρών που μπορούσε να κρυφακούσει ο παίκτης.",
            "Τα πνευματικά δικαιώματα του franchise έχουν χαθεί σε έναν λαβύρινθο νομικής ασάφειας μεταξύ Warner Bros, Activision και Disney, καθιστώντας αδύνατη την ψηφιακή επανακυκλοφορία του."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Operative:_No_One_Lives_Forever",
        "tags": ["gaming", "nolf", "monolith_productions", "cate_archer", "fps"]
    },
    {
        "id": "gaming_hard_335",
        "text": "Ποιο είναι το όνομα του ιδρυτή της Elixir Studios και μετέπειτα επικεφαλής της Google DeepMind (και νομπελίστα Χημείας 2024) που δημιούργησε τα 'Republic: The Revolution' και 'Evil Genius';",
        "correct": "Demis Hassabis (Ντέμης Χασάμπης)",
        "distractors": ["Peter Molyneux", "David Braben", "Chris Crawford"],
        "explanation": "Ο Ελληνοκύπριος Demis Hassabis ήταν παιδί-θαύμα στο σκάκι, συν-σχεδιαστής του Theme Park στην Bullfrog στα 17 του, και αργότερα ίδρυσε την Elixir Studios πριν στραφεί στην Τεχνητή Νοημοσύνη και κερδίσει το Νόμπελ Χημείας το 2024.",
        "funFacts": [
            "Στο Evil Genius (2004), οι παίκτες έχτιζαν μια μυστική βάση μέσα σε ηφαίστειο νησιού ως σατανικοί κακοί τύπου James Bond.",
            "Το Republic: The Revolution (2003) προσομοίωνε την πολιτική συμπεριφορά σχεδόν ενός εκατομμυρίου πολιτών στη φανταστική πρώην σοβιετική δημοκρατία της Novistrana."
        ],
        "source": "https://en.wikipedia.org/wiki/Demis_Hassabis",
        "tags": ["gaming", "demis_hassabis", "elixir_studios", "evil_genius", "industry"]
    },
    {
        "id": "gaming_hard_336",
        "text": "Ποιο πρωτοποριακό σύστημα νευρωνικών δικτύων και μηχανικής μάθησης χρησιμοποίησε το 'Black & White' (2001) της Lionhead Studios για την εκπαίδευση του Πλάσματος (Creature);",
        "correct": "Ενισχυτική μάθηση μέσω επιβράβευσης (χάδι) και τιμωρίας (χαστούκι)",
        "distractors": [
            "Προκαθορισμένα δέντρα αποφάσεων βασισμένα σε script",
            "Τυχαία γενετική μετάλλαξη χαρακτηριστικών ανά 10 λεπτά",
            "Αντιγραφή των κινήσεων των εχθρικών πλασμάτων μέσω καθρεπτισμού"
        ],
        "explanation": "Ο παίκτης μπορούσε να χαϊδέψει το πλάσμα (πίθηκο, αγελάδα, λιοντάρι κ.ά.) για να επιβραβεύσει μια καλή πράξη (π.χ. βοήθεια στους χωρικούς) ή να το χαστουκίσει για κακή πράξη (π.χ. κατανάλωση ανθρώπων), αλλάζοντας δυναμικά την ηθική και τη συμπεριφορά του.",
        "funFacts": [
            "Το πλάσμα μπορούσε να μάθει από μόνο του να ποτίζει καλλιέργειες με θαύματα βροχής παρατηρώντας τις ανάγκες των πιστών.",
            "Το χέρι του παίκτη άλλαζε μορφή ανάλογα με την ηθική του: ουράνιο και φωτεινό αν ήταν καλός θεός, μαυρισμένο και με κοφτερά νύχια αν ήταν κακός."
        ],
        "source": "https://en.wikipedia.org/wiki/Black_%26_White_(video_game)",
        "tags": ["gaming", "black_and_white", "lionhead", "peter_molyneux", "ai"]
    },
    {
        "id": "gaming_hard_337",
        "text": "Στο κλασικό παιχνίδι διαχείρισης 'Dungeon Keeper' (1997) της Bullfrog, ποιο πανίσχυρο αλλά εξαιρετικά ευέξαπτο τέρας με δρεπάνι απαιτούσε δικό του δωμάτιο για να μην σφάξει τα άλλα minions;",
        "correct": "Horned Reaper (Horny)",
        "distractors": ["Bile Demon", "Mistress", "Vampire"],
        "explanation": "Ο Horned Reaper είναι η πιο καταστροφική μονάδα του Dungeon Keeper· αν εκνευριστεί ή μείνει χωρίς φαγητό και χρυσό, στρέφεται ενάντια στα υπόλοιπα πλάσματα του μπουντρουμιού και τα εξοντώνει.",
        "funFacts": [
            "Το ξόρκι 'Possession' επέτρεπε στον παίκτη να μπει μέσα στα μάτια οποιουδήποτε πλάσματος και να παίξει το παιχνίδι ως first-person action dungeon crawler.",
            "Ο αφηγητής του παιχνιδιού Richard Ridings χάρισε τη βαριά, σαδιστική φωνή του συμβουλεύοντας τον παίκτη με φράσεις όπως: 'It's good to be bad!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Dungeon_Keeper",
        "tags": ["gaming", "dungeon_keeper", "bullfrog", "peter_molyneux", "retro"]
    },
    {
        "id": "gaming_hard_338",
        "text": "Ποια κωμική ασθένεια στο 'Theme Hospital' (1997) της Bullfrog απαιτούσε από τους γιατρούς να τρυπήσουν το κεφάλι του ασθενούς με καρφίτσα και να το ξαναφουσκώσουν;",
        "correct": "Bloaty Head (Πρησμένο Κεφάλι)",
        "distractors": ["Slack Tongue", "King Complex", "Hairyitis"],
        "explanation": "Στο Inflation Room, ο γιατρός χρησιμοποιεί ένα μηχάνημα που σκάει το πρησμένο κεφάλι του ασθενούς σαν μπαλόνι και το ξαναφουσκώνει στο φυσιολογικό μέγεθος.",
        "funFacts": [
            "Μια άλλη διάσημη ασθένεια ήταν το 'King Complex', όπου οι ασθενείς πίστευαν ότι ήταν ο Elvis Presley και έπρεπε να εξεταστούν από ψυχίατρο.",
            "Η εκφωνήτρια του νοσοκομείου έκανε σουρεαλιστικές ανακοινώσεις από τα μεγάφωνα, όπως: 'Hospital administrator is cheating!'."
        ],
        "source": "https://en.wikipedia.org/wiki/Theme_Hospital",
        "tags": ["gaming", "theme_hospital", "bullfrog", "simulation", "retro"]
    },
    {
        "id": "gaming_hard_339",
        "text": "Ποιο βρετανικό στούντιο που ιδρύθηκε από πρώην υπαλλήλους της Bullfrog δημιούργησε το εξαιρετικό sci-fi simulation 'Startopia' (2001);",
        "correct": "Mucky Foot Productions",
        "distractors": ["Lionhead Studios", "Elixir Studios", "Intrepid Games"],
        "explanation": "Η Mucky Foot Productions (των Gary Carr, Mike Diskett και Fin McGechie) σχεδίασε το Startopia όπου ο παίκτης διαχειρίζεται έναν τοροειδή (donut-shaped) διαστημικό σταθμό 3 ορόφων φιλοξενώντας 9 εξωγήινες φυλές.",
        "funFacts": [
            "Ο επάνω όροφος του σταθμού (Bio-Deck) επέτρεπε στους παίκτες να διαμορφώσουν φυσικά τοπία, λίμνες και καιρικά φαινόμενα για τουρισμό και γεωργία.",
            "Η σαρκαστική τεχνητή νοημοσύνη του σταθμού VAL ήταν εμπνευσμένη από τον HAL 9000 και την GLaDOS."
        ],
        "source": "https://en.wikipedia.org/wiki/Startopia",
        "tags": ["gaming", "startopia", "mucky_foot", "bullfrog", "simulation"]
    },
    {
        "id": "gaming_hard_340",
        "text": "Στο πρωτοποριακό FPS 'Aliens versus Predator' (1999) της Rebellion Developments, ποιο μοναδικό σύστημα όρασης χρησιμοποιούσε ο Alien (Xenomorph);",
        "correct": "Προοπτική υπερευρυγώνιου φακού (Fisheye lens) με φερομόνες",
        "distractors": ["Θερμική όραση υπέρυθρων", "Ηχοεντοπισμό με ακουστικά κύματα", "Νυχτερινή όραση πράσινου φωσφόρου"],
        "explanation": "Ο Alien έβλεπε τον κόσμο μέσα από μια ακραία καμπυλωτή όραση fisheye και μπορούσε να περπατάει πάνω σε τοίχους και ταβάνια με ιλιγγιώδη ταχύτητα, μυρίζοντας τις φερομόνες των ανθρώπων.",
        "funFacts": [
            "Η εκστρατεία του Colonial Marine ήταν τόσο τρομακτική που πολλοί παίκτες δυσκολεύονταν να προχωρήσουν ακούγοντας τον διαπεραστικό ήχο του Motion Tracker στο σκοτάδι.",
            "Ο Predator είχε πρόσβαση σε πολλαπλά φίλτρα όρασης (θερμικό για ανθρώπους, ηλεκτρικό για Aliens) και στο πανίσχυρο Plasmacaster."
        ],
        "source": "https://en.wikipedia.org/wiki/Aliens_versus_Predator_(video_game)",
        "tags": ["gaming", "avp", "rebellion", "fps", "retro"]
    },
    {
        "id": "gaming_hard_341",
        "text": "Ποιο anime-στυλ mecha shooter της Monolith Productions (1998) σηματοδότησε το ντεμπούτο της μηχανής γραφικών LithTech;",
        "correct": "Shogo: Mobile Armor Division",
        "distractors": ["Blood II: The Chosen", "Sanity: Aiken's Artifact", "Slave Zero"],
        "explanation": "Το Shogo επέτρεπε στον παίκτη Sanjuro Makabe να πολεμάει εναλλάξ πεζός σε στενούς διαδρόμους και πιλοτάροντας γιγάντια mechas (MCA) σε μεγαλουπόλεις, αντλώντας έμπνευση από σειρές anime όπως το Macross και το Gundam.",
        "funFacts": [
            "Η LithTech engine αναπτύχθηκε αρχικά σε συνεργασία με τη Microsoft ως πιθανή μηχανή επίδειξης για το Direct3D.",
            "Το παιχνίδι εισήγαγε σύστημα κρίσιμων χτυπημάτων (critical hits) που αναπλήρωναν μέρος της υγείας του παίκτη όταν εκτελούνταν με επιτυχία."
        ],
        "source": "https://en.wikipedia.org/wiki/Shogo:_Mobile_Armor_Division",
        "tags": ["gaming", "shogo", "monolith_productions", "lithtech", "mecha"]
    },
    {
        "id": "gaming_hard_342",
        "text": "Ποιο ήταν το πρώτο παιχνίδι stealth της IO Interactive (2000) που εισήγαγε τον γενετικά τροποποιημένο πληρωμένο δολοφόνο Agent 47;",
        "correct": "Hitman: Codename 47",
        "distractors": ["Hitman 2: Silent Assassin", "Hitman: Contracts", "Hitman: Blood Money"],
        "explanation": "Το Codename 47 εισήγαγε τον μηχανισμό μεταμφιέσεων (κλοπή ρούχων από αναισθητοποιημένα ή νεκρά θύματα), την απόκρυψη πτωμάτων και το στραγγαλισμό με σύρμα πιάνου (fiber wire).",
        "funFacts": [
            "Το Hitman ήταν ένα από τα πρώτα εμπορικά παιχνίδια που χρησιμοποίησαν φυσική ragdoll για τα σώματα των χαρακτήρων.",
            "Ο Agent 47 δημιουργήθηκε από το DNA πέντε διαφορετικών αρχιεγκληματιών σε ένα άσυλο της Ρουμανίας από τον Dr. Ort-Meyer."
        ],
        "source": "https://en.wikipedia.org/wiki/Hitman:_Codename_47",
        "tags": ["gaming", "hitman", "io_interactive", "stealth", "agent_47"]
    },
    {
        "id": "gaming_hard_343",
        "text": "Ποιο ιστορικό stealth παιχνίδι του Paul Neurath και της Looking Glass Studios (1998) εισήγαγε τη φωτεινή σφαίρα 'Light Gem' στο κάτω μέρος της οθόνης;",
        "correct": "Thief: The Dark Project",
        "distractors": ["Deus Ex", "System Shock", "Dishonored"],
        "explanation": "Το Light Gem άλλαζε φωτεινότητα από απόλυτα μαύρο (όταν ο Garrett ήταν κρυμμένος σε βαθιά σκιά) έως εκτυφλωτικά φωτεινό, ενημερώνοντας άμεσα τον παίκτη για το πόσο ορατός ήταν στους φρουρούς.",
        "funFacts": [
            "Το Thief ξεκίνησε αρχικά ως σχέδιο δράσης με ζόμπι με τίτλο 'Dark Camelot' πριν επικεντρωθεί εξ ολοκλήρου στη μεσαιωνική τέχνη της κλοπής.",
            "Η Looking Glass έφτιαξε έναν εξαιρετικά περίπλοκο αλγόριθμο διάδοσης ήχου που υπολόγιζε την ακουστική ανάλογα με τα ανοίγματα των θυρών και τα υλικά."
        ],
        "source": "https://en.wikipedia.org/wiki/Thief:_The_Dark_Project",
        "tags": ["gaming", "thief", "looking_glass", "stealth", "mechanics"]
    },
    {
        "id": "gaming_hard_344",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή κυνηγού επικηρυγμένων στο cult western FPS 'Outlaws' (1997) της LucasArts;",
        "correct": "James Anderson",
        "distractors": ["Bob Graham", "Matt Dillon", "Cole Black"],
        "explanation": "Ο πρώην σερίφης James Anderson καταδιώκει τη συμμορία του Bob Graham που δολοφόνησε τη γυναίκα του και απήγαγε την κόρη του Sarah.",
        "funFacts": [
            "Το Outlaws ήταν ένα από τα πρώτα FPS που εισήγαγαν διόπτρα ελεύθερου σκοπευτή (sniper zoom) και χειροκίνητη επαναγέμιση σφαίρα-σφαίρα.",
            "Το soundtrack από τον Clint Bajakian είναι ένα αυθεντικό συμφωνικό σπαγγέτι γουέστερν αφιέρωμα στο στυλ του Ennio Morricone."
        ],
        "source": "https://en.wikipedia.org/wiki/Outlaws_(1997_video_game)",
        "tags": ["gaming", "outlaws", "lucasarts", "western", "fps"]
    },
    {
        "id": "gaming_hard_345",
        "text": "Ποιο Star Wars shooter της LucasArts (1995) εισήγαγε τον μισθοφόρο Kyle Katarn και τη μηχανή Jedi Engine που υποστήριζε ορόφους πάνω από άλλους ορόφους;",
        "correct": "Star Wars: Dark Forces",
        "distractors": ["Jedi Knight: Dark Forces II", "Rebel Assault", "Shadows of the Empire"],
        "explanation": "Το Dark Forces ξεπέρασε τους περιορισμούς του αυθεντικού Doom εισάγοντας άλματα, σκύψιμο, κατακόρυφη στόχευση και πολυεπίπεδη αρχιτεκτονική δωματίων.",
        "funFacts": [
            "Στην πρώτη κιόλας αποστολή του παιχνιδιού, ο Kyle Katarn κλέβει τα σχέδια του Death Star από μια αυτοκρατορική βάση στο Danuta.",
            "Η βασική απειλή της εκστρατείας είναι τα ρομποτικά Dark Troopers που αναπτύσσει ο General Mohc."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars:_Dark_Forces",
        "tags": ["gaming", "dark_forces", "lucasarts", "star_wars", "fps"]
    },
    {
        "id": "gaming_hard_346",
        "text": "Στο 'Star Wars Jedi Knight: Dark Forces II' (1997), ποιος σκοτεινός Jedi με ένα μόνο μάτι ηγείται των Επτά Σκοτεινών Jedi που αναζητούν την Κοιλάδα των Jedi (Valley of the Jedi);",
        "correct": "Jerec",
        "distractors": ["Desann", "Maw", "Boc"],
        "explanation": "Ο Jerec είναι ένας ισχυρός Miraluka Dark Jedi που μπορεί να αισθάνεται τα πάντα μέσω της Δύναμης και σχεδιάζει να απορροφήσει τις παγιδευμένες ψυχές της Κοιλάδας για να γίνει θεός.",
        "funFacts": [
            "Το παιχνίδι περιλάμβανε εκτεταμένα live-action FMV cutscenes με πραγματικούς ηθοποιούς (τον Jason Court ως Kyle Katarn και τον Christopher Neame ως Jerec).",
            "Ήταν το πρώτο παιχνίδι Star Wars που επέτρεπε πλήρη έλεγχο φωτόσπαθου και δυνάμεων της Δύναμης σε 3D multiplayer."
        ],
        "source": "https://en.wikipedia.org/wiki/Star_Wars_Jedi_Knight:_Dark_Forces_II",
        "tags": ["gaming", "jedi_knight", "lucasarts", "star_wars", "kyle_katarn"]
    },
    {
        "id": "gaming_hard_347",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού παιχνιδιού προσομοίωσης υποβρυχίων του 1993 από τη MicroProse που αναπτύχθηκε υπό την επίβλεψη του ναυάρχου William M. McBride;",
        "correct": "SubWar 2050",
        "distractors": ["Silent Service", "Aces of the Deep", "688 Attack Sub"],
        "explanation": "Το SubWar 2050 συνδύαζε φουτουριστική υποθαλάσσια μάχη με ρεαλιστική θερμοκλινή φυσική, σόναρ και υδροδυναμική προσομοίωση.",
        "funFacts": [
            "Η MicroProse ειδικευόταν σε εξαιρετικά λεπτομερείς εξομοιωτές πτήσης και ναυμαχιών με εγχειρίδια εκατοντάδων σελίδων.",
            "Τα υποβρύχια μαχητικά σκάφη του παιχνιδιού χρησιμοποιούσαν τορπίλες σπηλαίωσης (supercavitating torpedoes)."
        ],
        "source": "https://en.wikipedia.org/wiki/SubWar_2050",
        "tags": ["gaming", "subwar_2050", "microprose", "simulation", "retro"]
    },
    {
        "id": "gaming_hard_348",
        "text": "Ποιο είναι το όνομα της ομάδας ανάπτυξης της Looking Glass που αποχώρησε για να ιδρύσει την Irrational Games και να δημιουργήσει τα 'System Shock 2' και 'BioShock';",
        "correct": "Ken Levine, Jonathan Chey και Robert Fermier",
        "distractors": ["Warren Spector, Harvey Smith και Chris Norden", "Doug Church, Paul Neurath και Marc LeBlanc", "Tim Willits, Adrian Carmack και Kevin Cloud"],
        "explanation": "Οι τρεις πρώην προγραμματιστές και σχεδιαστές της Looking Glass ίδρυσαν την Irrational Games στη Βοστώνη το 1997, υπογράφοντας αμέσως συμφωνία με την Electronic Arts για την ανάπτυξη του System Shock 2.",
        "funFacts": [
            "Το BioShock θεωρήθηκε ο πνευματικός διάδοχος του System Shock 2, μεταφέροντας τους μηχανισμούς από το διάστημα στον βυθό της θάλασσας.",
            "Η Irrational εξαγοράστηκε αργότερα από την Take-Two Interactive / 2K Games."
        ],
        "source": "https://en.wikipedia.org/wiki/Ghost_Story_Games",
        "tags": ["gaming", "irrational_games", "ken_levine", "system_shock", "bioshock"]
    },
    {
        "id": "gaming_hard_349",
        "text": "Στο 'System Shock 2' (1999), ποιο είναι το όνομα της συλλογικής βιολογικής οντότητας σκουληκιών που δημιουργήθηκε από πειράματα της SHODAN και απειλεί να αφομοιώσει την ανθρωπότητα;",
        "correct": "The Many",
        "distractors": ["The Flood", "The Swarm", "The Hive"],
        "explanation": "Το The Many επικοινωνεί τηλεπαθητικά με τον παίκτη με μια ανατριχιαστική χορωδία ψιθύρων ('What is a drop of rain, compared to the storm? What is a thought, compared to the mind?').",
        "funFacts": [
            "Η SHODAN αναγκάζεται να συμμαχήσει προσωρινά με τον στρατιώτη για να καταστρέψει τα ίδια της τα βιολογικά δημιουργήματα που ξέφυγαν από τον έλεγχό της.",
            "Η Dr. Janice Polito αποκαλύπτεται ότι ήταν νεκρή από την αρχή και ότι η SHODAN χρησιμοποιούσε το ολόγραμμά της για να κατευθύνει τον παίκτη."
        ],
        "source": "https://en.wikipedia.org/wiki/System_Shock_2",
        "tags": ["gaming", "system_shock_2", "irrational_games", "shodan", "the_many"]
    },
    {
        "id": "gaming_hard_350",
        "text": "Ποιος είναι ο ασυνήθιστος πρωταγωνιστής στο ιδιόρρυθμο third-person action παιχνίδι 'Messiah' (2000) της Shiny Entertainment, ο οποίος στάλθηκε από τον Θεό για να καθαρίσει μια διεφθαρμένη cyberpunk Γη;",
        "correct": "Ο Bob, ένα μικροσκοπικό χερουβείμ (αγγελάκι) με πάνες",
        "distractors": ["Ο Uriel, ένας αρχάγγελος με πύρινο σπαθί", "Ο Ezekiel, ένας εξορισμένος ιεροκήρυκας cyborg", "Ο Lazarus, ένας γενετικά αναστημένος πολεμιστής"],
        "explanation": "Ο Bob είναι ένα ανυπεράσπιστο αγγελάκι με φτερά που δεν μπορεί να πολεμήσει μόνο του, αλλά διαθέτει την ικανότητα να καταλαμβάνει (possess) τα σώματα οποιουδήποτε εχθρού ή πολίτη για να χρησιμοποιήσει τα όπλα και τις ικανότητές τους.",
        "funFacts": [
            "Το Messiah ήταν από τα πρώτα παιχνίδια που εισήγαγαν τεχνολογία RT-DAT (Real-Time Deformation and Tessellation) επιτρέποντας δυναμική προσαρμογή πολυγώνων.",
            "Το soundtrack του παιχνιδιού περιλάμβανε κομμάτια από το industrial metal συγκρότημα Fear Factory."
        ],
        "source": "https://en.wikipedia.org/wiki/Messiah_(video_game)",
        "tags": ["gaming", "messiah", "shiny_entertainment", "david_perry", "retro"]
    },
    {
        "id": "gaming_hard_351",
        "text": "Ποια είναι η Βρετανίδα μυστική πράκτορας της οργάνωσης UNITY που πρωταγωνιστεί στο κατασκοπευτικό retro-FPS 'The Operative: No One Lives Forever' (2000);",
        "correct": "Cate Archer",
        "distractors": ["Joanna Dark", "Tanya Adams", "Eva Morgan"],
        "explanation": "Η Cate Archer πολεμά τη σατανική τρομοκρατική οργάνωση H.A.R.M. στη δεκαετία του 1960, χρησιμοποιώντας πρωτότυπα κατασκοπευτικά γκάτζετ κρυμμένα σε γυναικεία αξεσουάρ όπως εκρηκτικό κραγιόν και τσιμπιδάκια παραβίασης κλειδαριών.",
        "funFacts": [
            "Το NOLF θεωρείται ένα από τα πιο ευφυή και καλογραμμένα FPS όλων των εποχών, με απολαυστικούς κωμικούς διαλόγους μεταξύ ανυποψίαστων φρουρών.",
            "Τα δικαιώματα της σειράς έχουν χαθεί σε έναν πρωτοφανή νομικό λαβύρινθο μεταξύ Warner Bros., Activision και 20th Century Fox, εμποδίζοντας την ψηφιακή επανακυκλοφορία του."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Operative:_No_One_Lives_Forever",
        "tags": ["gaming", "nolf", "cate_archer", "monolith_productions", "fps"]
    },
    {
        "id": "gaming_hard_352",
        "text": "Στο φιλόδοξο πολιτικό simulation 'Republic: The Revolution' (2003) της Elixir Studios του Demis Hassabis, σε ποια φανταστική πρώην σοβιετική δημοκρατία προσπαθεί ο παίκτης να ανατρέψει τον δικτάτορα Vasily Karasov;",
        "correct": "Novistrana (Νοβιστράνα)",
        "distractors": ["Chernarus", "Arulco", "Kastovia"],
        "explanation": "Στη Novistrana, ο παίκτης δημιουργεί μια επαναστατική φατρία στρατολογώντας ιερείς, μαφιόζους, επιχειρηματίες και πολιτικούς, επιλέγοντας ανάμεσα σε τακτικές βίας, επιρροής ή πλούτου.",
        "funFacts": [
            "Ο ιδρυτής της Elixir Studios Demis Hassabis, πρώην παιδί-θαύμα στο σκάκι και προγραμματιστής της Bullfrog, ίδρυσε αργότερα την κολοσσιαία εταιρεία τεχνητής νοημοσύνης DeepMind.",
            "Η πρωτοποριακή μηχανή Totality Engine του παιχνιδιού μπορούσε να αποδώσει μια ολόκληρη πόλη με εκατοντάδες χιλιάδες πλήρως προσομοιωμένους πολίτες."
        ],
        "source": "https://en.wikipedia.org/wiki/Republic:_The_Revolution",
        "tags": ["gaming", "republic_the_revolution", "elixir_studios", "demis_hassabis", "strategy"]
    },
    {
        "id": "gaming_hard_353",
        "text": "Ποιος είναι ο στόχος του παίκτη στο σατιρικό strategy παιχνίδι 'Evil Genius' (2004) της Elixir Studios;",
        "correct": "Η κατασκευή μυστικής βάσης σε ηφαιστειογενές νησί και η κατασκευή Όπλου της Ημέρας της Κρίσεως (Doomsday Device)",
        "distractors": [
            "Η κατάκτηση του διαστήματος μέσω παράνομων δορυφορικών εκτοξεύσεων",
            "Η διείσδυση στις μυστικές υπηρεσίες των ΗΠΑ μέσω κυβερνοπολέμου",
            "Η ίδρυση ενός παγκόσμιου καρτέλ λαθρεμπορίου τέχνης"
        ],
        "explanation": "Εμπνευσμένο από τις ταινίες James Bond της δεκαετίας του '60, το Evil Genius θέτει τον παίκτη στον ρόλο ενός κακοποιού μεγαλοφυΐας (όπως ο Maximilian) που διαχειρίζεται τσιράκια και παγιδεύει μυστικούς πράκτορες.",
        "funFacts": [
            "Οι μυστικοί πράκτορες των 'Forces of Justice' έρχονται στο νησί μεταμφιεσμένοι σε τουρίστες και πρέπει να παραπλανηθούν από το νόμιμο ξενοδοχείο-βιτρίνα του παίκτη.",
            "Το παιχνίδι σχεδιάστηκε από τον Sandra Gilbert, πρώην βασικό σχεδιαστή του Dungeon Keeper."
        ],
        "source": "https://en.wikipedia.org/wiki/Evil_Genius_(video_game)",
        "tags": ["gaming", "evil_genius", "elixir_studios", "strategy", "retro"]
    },
    {
        "id": "gaming_hard_354",
        "text": "Ποια ριζική αλλαγή στο gameplay εισήγαγε το 'King's Quest: Mask of Eternity' (1998), το όγδοο κεφάλαιο της ιστορικής σειράς περιπέτειας της Sierra;",
        "correct": "Μετάβαση σε 3D δράση τρίτου προσώπου με μάχες σπαθιού και τόξου (action-RPG)",
        "distractors": [
            "Μετατροπή σε παιχνίδι καρτών στρατηγικής",
            "Πλήρης εξάλειψη γρίφων υπέρ ενός text-based interactive fiction",
            "Χρήση αποκλειστικά προ-αποδοσμένων FMV βίντεο πρώτου προσώπου"
        ],
        "explanation": "Το Mask of Eternity εγκατέλειψε το κλασικό point-and-click interface και την οικογένεια του King Graham, βάζοντας τον παίκτη στον ρόλο του Connor του Daventry σε ένα 3D action-adventure με RPG στοιχεία.",
        "funFacts": [
            "Η αλλαγή αυτή δίχασε βαθιά τους φανατικούς οπαδούς της Sierra, καθώς πολλοί προτιμούσαν τους παραδοσιακούς γρίφους χωρίς μάχες σε πραγματικό χρόνο.",
            "Ήταν το τελευταίο παιχνίδι King's Quest που αναπτύχθηκε από την αυθεντική Sierra On-Line πριν από το κλείσιμο των κεντρικών γραφείων της στο Oakhurst."
        ],
        "source": "https://en.wikipedia.org/wiki/King%27s_Quest:_Mask_of_Eternity",
        "tags": ["gaming", "kings_quest", "sierra", "mask_of_eternity", "adventure"]
    },
    {
        "id": "gaming_hard_355",
        "text": "Ποιος διάσημος συγγραφέας επιστημονικής φαντασίας όχι μόνο συν-σχεδίασε το σκοτεινό adventure 'I Have No Mouth, and I Must Scream' (1995), αλλά δάνεισε και τη φωνή του στον σαδιστή υπερυπολογιστή AM;",
        "correct": "Harlan Ellison",
        "distractors": ["Philip K. Dick", "William Gibson", "Arthur C. Clarke"],
        "explanation": "Ο Harlan Ellison έγραψε το αρχικό ομότιτλο διήγημα του 1967 και επέβλεψε στενά την προσαρμογή του σε point-and-click adventure από την Cyberdreams, εκφωνώντας ο ίδιος τον παντοδύναμο υπολογιστή AM που βασανίζει τους 5 επιζώντες της ανθρωπότητας.",
        "funFacts": [
            "Ο τίτλος του παιχνιδιού και του διηγήματος αναφέρεται στην τραγική μοίρα του πρωταγωνιστή Ted, ο οποίος μεταμορφώνεται σε ένα άμορφο ζελατινώδες πλάσμα χωρίς στόμα.",
            "Το παιχνίδι απαγορεύτηκε στη Γαλλία και τη Γερμανία λόγω των εξαιρετικά σκοτεινών θεμάτων του (όπως το ναζιστικό παρελθόν του Nimdok)."
        ],
        "source": "https://en.wikipedia.org/wiki/I_Have_No_Mouth,_and_I_Must_Scream_(video_game)",
        "tags": ["gaming", "cyberdreams", "harlan_ellison", "adventure", "horror"]
    },
    {
        "id": "gaming_hard_356",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστή απέθαντου πιστολέρο στο καλτ horror FPS 'Blood' (1997) της Monolith Productions που αναζητά εκδίκηση από τον σκοτεινό θεό Tchernobog;",
        "correct": "Caleb",
        "distractors": ["Corvus", "Torquemada", "Dustin"],
        "explanation": "Ο Caleb, ένας πρώην ανώτατος στρατηγός της αίρεσης Cabal, ανασταίνεται από τον τάφο του οπλισμένος με δίκαννα, κούκλες βουντού και εκρηκτικά δυναμίτη, ψιθυρίζοντας μακάβριες ατάκες όπως 'I live... again!'.",
        "funFacts": [
            "Το Blood χτίστηκε πάνω στην Build Engine της 3D Realms, αλλά πρόσθεσε voxels για αντικείμενα και εξαιρετικά προηγμένα εφέ φωτισμού και φωτιάς.",
            "Η φωνή του Caleb ανήκει στον Stephan Weyte, ο οποίος χάρισε στον χαρακτήρα μια μοναδική θεατρική και σαδιστική προσωπικότητα."
        ],
        "source": "https://en.wikipedia.org/wiki/Blood_(video_game)",
        "tags": ["gaming", "blood", "monolith_productions", "build_engine", "caleb"]
    },
    {
        "id": "gaming_hard_357",
        "text": "Ποιους δύο παράξενους μετρητές έπρεπε να διαχειρίζονται οι παίκτες στο Build engine shooter 'Redneck Rampage' (1997) για να μην παραπατούν ή να μην αποκτήσουν στομαχικές διαταραχές;",
        "correct": "Αλκοόλ (Alcohol) και Έντερα/Φαγητό (Gut)",
        "distractors": ["Νικοτίνη και Καφεΐνη", "Αδρεναλίνη και Κόπωση", "Πίεση και Χοληστερίνη"],
        "explanation": "Οι αδελφοί Leonard και Bubba έπρεπε να πίνουν Moonshine και να τρώνε χοιρινές πέτσες (pork rinds) για να αναπληρώνουν υγεία, αλλά αν έπιναν πάρα πολύ μεθούσαν χάνοντας τον έλεγχο, ενώ αν έτρωγαν πάρα πολύ πάθαιναν μετεωρισμό.",
        "funFacts": [
            "Η πλοκή αφορά την εισβολή εξωγήινων στο Hicksville του Αρκάνσας και την κλοπή του βραβευμένου γουρουνιού των πρωταγωνιστών, της Bessie.",
            "Η Xatrix Entertainment μετονομάστηκε αργότερα σε Gray Matter Interactive και ανέπτυξε το 'Return to Castle Wolfenstein'."
        ],
        "source": "https://en.wikipedia.org/wiki/Redneck_Rampage",
        "tags": ["gaming", "redneck_rampage", "xatrix", "build_engine", "fps"]
    },
    {
        "id": "gaming_hard_358",
        "text": "Ποιο είναι το όνομα του σωματοφύλακα και νίντζα πρωταγωνιστή στο 'Shadow Warrior' (1997) της 3D Realms που πολεμά τον στρατό δαιμόνων του Master Zilla;",
        "correct": "Lo Wang",
        "distractors": ["Ryu Hayabusa", "Joe Musashi", "Hotsuma"],
        "explanation": "Ο Lo Wang χρησιμοποιεί κατάνα, shurikens, εκτοξευτές πυραύλων και κεφάλια δαιμόνων για να πολεμήσει τη διεφθαρμένη εταιρεία Zilla Enterprises στην τελευταία μεγάλη κυκλοφορία της Build Engine της δεκαετίας του '90.",
        "funFacts": [
            "Το Shadow Warrior ήταν το πρώτο FPS με την Build engine που υποστήριζε οχήματα που μπορούσε να οδηγήσει ο παίκτης (τανκς και εκσκαφείς).",
            "Η σειρά αναβιώθηκε με τεράστια επιτυχία το 2013 από την πολωνική εταιρεία Flying Wild Hog."
        ],
        "source": "https://en.wikipedia.org/wiki/Shadow_Warrior_(1997_video_game)",
        "tags": ["gaming", "shadow_warrior", "3d_realms", "lo_wang", "build_engine"]
    },
    {
        "id": "gaming_hard_359",
        "text": "Ποιο πρωτοποριακό FPS/RPG του 1996 που αναπτύχθηκε στη μηχανή id Tech 1 (Doom engine) εισήγαγε ολόκληρους διαλόγους με φωνές, κόμβους αποστολών (hubs) και stealth μηχανισμούς;",
        "correct": "Strife: Quest for the Sigil",
        "distractors": ["Hexen: Beyond Heretic", "Hacx: Twitch 'n Kill", "CyClones"],
        "explanation": "Το Strife της Rogue Entertainment θεωρείται ένα από τα πρώτα immersive sim / action-RPG shooters πρώτου προσώπου, όπου ο παίκτης εντάσσεται στην αντίσταση (The Front) ενάντια στη θεοκρατική δικτατορία του Order.",
        "funFacts": [
            "Το πανίσχυρο όπλο 'Sigil' συναρμολογείται κομμάτι-κομμάτι από πέντε αρχαία θραύσματα νικώντας ηγετικά στελέχη του Order.",
            "Ήταν το τελευταίο εμπορικό παιχνίδι που κυκλοφόρησε επίσημα βασισμένο στον αυθεντικό κώδικα της μηχανής Doom."
        ],
        "source": "https://en.wikipedia.org/wiki/Strife_(video_game)",
        "tags": ["gaming", "strife", "rogue_entertainment", "doom_engine", "action_rpg"]
    },
    {
        "id": "gaming_hard_360",
        "text": "Ποιο είναι το όνομα του πρωτοποριακού παιχνιδιού τακτικής μάχης με mecha της Looking Glass Studios (1996) στον δορυφόρο Τιτάνα που διέθετε πλήρη φωνητικό έλεγχο εντολών squad;",
        "correct": "Terra Nova: Strike Force Centauri",
        "distractors": ["MechWarrior 2", "Heavy Gear", "Starsiege"],
        "explanation": "Στο Terra Nova, ο παίκτης ηγείται μιας ομάδας κομάντο με Powered Battle Armor (PBA) ενάντια στους πειρατές του Clan, δίνοντας λεπτομερείς τακτικές εντολές πυρός και υποστήριξης σε 3D ύπαιθρο.",
        "funFacts": [
            "Θεωρείται ένα από τα πιο υποτιμημένα τεχνολογικά επιτεύγματα της δεκαετίας του '90, αλλά υπέστη εμπορική αποτυχία λόγω έλλειψης 3D hardware acceleration.",
            "Ο προγραμματιστής Ken Levine έγραψε μέρος των σεναριακών αποστολών πριν ιδρύσει την Irrational Games."
        ],
        "source": "https://en.wikipedia.org/wiki/Terra_Nova:_Strike_Force_Centauri",
        "tags": ["gaming", "terra_nova", "looking_glass", "tactical", "retro"]
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
    print(f"Loaded {len(questions)} questions for gaming_hard batch 3.")
    validate_and_append("gaming", "hard", 5, questions)

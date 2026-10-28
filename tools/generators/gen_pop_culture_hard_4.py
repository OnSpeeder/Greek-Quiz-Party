# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "pop_culture_hard_161",
        "text": "Ποιο είναι το πραγματικό όνομα του υπερήρωα Deadpool στα κόμικς της Marvel;",
        "correct": "Wade Wilson",
        "distractors": ["Slade Wilson", "Jack Monroe", "Frank Simpson"],
        "explanation": "Ο Deadpool ονομάζεται Wade Wilson, ένα εσκεμμένο λογοπαίγνιο και φόρος τιμής/παρωδία στον Deathstroke της DC Comics του οποίου το όνομα είναι Slade Wilson.",
        "funFacts": [
            "Ο δημιουργός Rob Liefeld ήταν μεγάλος θαυμαστής των Teen Titans και του Deathstroke.",
            "Ο Deadpool έκανε το ντεμπούτο του στο 'The New Mutants' #98 τον Φεβρουάριο του 1991 ως κακός."
        ],
        "source": "https://en.wikipedia.org/wiki/Deadpool",
        "tags": ["comics", "marvel", "deadpool"]
    },
    {
        "id": "pop_culture_hard_162",
        "text": "Ποια είναι η μοναδική ταινία κινουμένων σχεδίων στην ιστορία που κέρδισε το Χρυσό Λιοντάρι στο Φεστιβάλ Βενετίας ή τη Χρυσή Άρκτο στο Φεστιβάλ Βερολίνου;",
        "correct": "Ταξίδι στη Χώρα των Θαυμάτων (Spirited Away)",
        "distractors": ["Πριγκίπισσα Μονονόκε", "Ο Τάφος των Πυγολαμπίδων", "Το Κινούμενο Κάστρο"],
        "explanation": "Το 'Spirited Away' (2001) του Hayao Miyazaki κέρδισε τη Χρυσή Άρκτο στο Φεστιβάλ Κινηματογράφου του Βερολίνου το 2002 (από κοινού με το Bloody Sunday).",
        "funFacts": [
            "Παραμένει η μοναδική ταινία anime που κέρδισε τόσο Χρυσή Άρκτο όσο και Όσκαρ Καλύτερης Ταινίας Κινουμένων Σχεδίων.",
            "Ο Miyazaki δημιούργησε την ιστορία εμπνευσμένος από τη 10χρονη κόρη ενός φίλου του."
        ],
        "source": "https://en.wikipedia.org/wiki/Spirited_Away",
        "tags": ["anime", "cinema", "miyazaki"]
    },
    {
        "id": "pop_culture_hard_163",
        "text": "Ποιο viral βίντεο του 2007 έγινε ένα από τα πρώτα παγκόσμια memes με ένα μωρό να δαγκώνει το δάχτυλο του αδελφού του;",
        "correct": "Charlie Bit My Finger",
        "distractors": ["David After Dentist", "Sneezing Baby Panda", "Evolution of Dance"],
        "explanation": "Το βίντεο 'Charlie Bit My Finger - again !' αναρτήθηκε στο YouTube τον Μάιο του 2007 και για χρόνια ήταν το πιο προβεβλημένο μη μουσικό βίντεο της πλατφόρμας.",
        "funFacts": [
            "Ανέβηκε στο YouTube από τον πατέρα των παιδιών μόνο επειδή το αρχείο ήταν πολύ μεγάλο για να σταλεί μέσω email στους παππούδες.",
            "Το 2021 το βίντεο πωλήθηκε ως NFT για πάνω από 760.000 δολάρια."
        ],
        "source": "https://en.wikipedia.org/wiki/Charlie_Bit_My_Finger",
        "tags": ["internet", "memes", "youtube"]
    },
    {
        "id": "pop_culture_hard_164",
        "text": "Στη σειρά 'Doctor Who', ποιο είναι το είδος των εξωγήινων όντων που μπορούν να κινούνται μόνο όταν κανείς δεν τα κοιτάζει;",
        "correct": "Weeping Angels",
        "distractors": ["Silence", "Cybermen", "Sontarans"],
        "explanation": "Οι Weeping Angels (Κλαίοντες Άγγελοι) εισήχθησαν στο επεισόδιο 'Blink' (2007) και είναι 'κβαντικά κλειδωμένοι' σε πέτρινα αγάλματα όποτε παρατηρούνται από οποιοδήποτε ον.",
        "funFacts": [
            "Το επεισόδιο 'Blink' θεωρείται συχνά από κριτικούς και κοινό ως ένα από τα καλύτερα στην ιστορία του Doctor Who.",
            "Το μότο τους είναι 'Don't blink. Blink and you're dead'."
        ],
        "source": "https://en.wikipedia.org/wiki/Weeping_Angel",
        "tags": ["doctor who", "television", "sci-fi"]
    },
    {
        "id": "pop_culture_hard_165",
        "text": "Ποιος καλλιτέχνης δημιούργησε το εξώφυλλο του θρυλικού άλμπουμ των Velvet Underground με τη διάσημη ξεφλουδιζόμενη μπανάνα;",
        "correct": "Andy Warhol",
        "distractors": ["Roy Lichtenstein", "Keith Haring", "Jean-Michel Basquiat"],
        "explanation": "Ο Andy Warhol σχεδίασε το εμβληματικό εξώφυλλο του 'The Velvet Underground & Nico' (1967), όπου οι ακροατές μπορούσαν να ξεκολλήσουν ένα αυτοκόλλητο μπανάνας.",
        "funFacts": [
            "Κάτω από τη φλούδα της μπανάνας υπήρχε μια σαρκώδης ροζ μπανάνα.",
            "Ο Warhol ήταν επίσης ο παραγωγός και μάνατζερ του συγκροτήματος εκείνη την περίοδο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Velvet_Underground_%26_Nico",
        "tags": ["pop art", "music", "andy warhol"]
    },
    {
        "id": "pop_culture_hard_166",
        "text": "Ποιο franchise κόμικς εισήγαγε για πρώτη φορά την έννοια του 'Multiverse' στη σύγχρονη ποπ κουλτούρα με την ιστορία 'Flash of Two Worlds' το 1961;",
        "correct": "DC Comics",
        "distractors": ["Marvel Comics", "Dark Horse", "Image Comics"],
        "explanation": "Το τεύχος 'The Flash' #123 (Σεπτέμβριος 1961) της DC Comics ένωσε τον Barry Allen (Silver Age Flash) με τον Jay Garrick (Golden Age Flash), εγκαθιδρύοντας το Multiverse (Earth-One και Earth-Two).",
        "funFacts": [
            "Η ιστορία γράφτηκε από τον Gardner Fox και σχεδιάστηκε από τον Carmine Infantino.",
            "Αυτή η ιδέα οδήγησε δεκαετίες αργότερα στο θρυλικό crossover 'Crisis on Infinite Earths'."
        ],
        "source": "https://en.wikipedia.org/wiki/Flash_of_Two_Worlds",
        "tags": ["comics", "dc", "multiverse"]
    },
    {
        "id": "pop_culture_hard_167",
        "text": "Ποιος σκηνοθέτης δημιούργησε την cult ταινία 'The Room' (2003), η οποία χαρακτηρίζεται συχνά ως 'ο Πολίτης Κέιν των κακών ταινιών';",
        "correct": "Tommy Wiseau",
        "distractors": ["Ed Wood", "Neil Breen", "Uwe Boll"],
        "explanation": "Ο Tommy Wiseau έγραψε, σκηνοθέτησε, παρήγαγε και πρωταγωνίστησε στο 'The Room', το οποίο απέκτησε παγκόσμια cult λατρεία για τους αλλοπρόσαλλους διαλόγους και την ερμηνεία του.",
        "funFacts": [
            "Ο ηθοποιός Greg Sestero έγραψε βιβλίο για τα γυρίσματα με τίτλο 'The Disaster Artist', το οποίο έγινε και βραβευμένη ταινία.",
            "Ο Wiseau χρηματοδότησε την ταινία μόνος του με πάνω από 6 εκατομμύρια δολάρια από άγνωστες αρχικά πηγές."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Room",
        "tags": ["cult cinema", "movies", "tommy wiseau"]
    },
    {
        "id": "pop_culture_hard_168",
        "text": "Ποιο ήταν το όνομα του πρώτου χαρακτήρα που δημιούργησε ο Walt Disney πριν τον Mickey Mouse και για τον οποίο έχασε τα πνευματικά δικαιώματα από τη Universal;",
        "correct": "Oswald the Lucky Rabbit",
        "distractors": ["Pete the Cat", "Julius the Cat", "Flip the Frog"],
        "explanation": "Ο Oswald the Lucky Rabbit δημιουργήθηκε το 1927 από τον Disney και τον Ub Iwerks. Όταν ο διανομέας Charles Mintz πήρε τα δικαιώματα, ο Disney δημιούργησε τον Mickey Mouse ως αντικαταστάτη.",
        "funFacts": [
            "Η Disney ανέκτησε τα δικαιώματα του Oswald μόλις το 2006, ανταλλάσσοντας τον αθλητικό σχολιαστή Al Michaels με το NBCUniversal!",
            "Ο Oswald πρωταγωνίστησε ξανά στο βιντεοπαιχνίδι Epic Mickey το 2010."
        ],
        "source": "https://en.wikipedia.org/wiki/Oswald_the_Lucky_Rabbit",
        "tags": ["animation", "disney", "history"]
    },
    {
        "id": "pop_culture_hard_169",
        "text": "Ποιο είναι το όνομα του φανταστικού περιοδικού μόδας στο οποίο διαδραματίζεται η ταινία 'The Devil Wears Prada';",
        "correct": "Runway",
        "distractors": ["Vogue", "Catwalk", "Couture"],
        "explanation": "Στο 'The Devil Wears Prada' (2006), η Miranda Priestly (Meryl Streep) είναι η πανίσχυρη αρχισυντάκτρια του φανταστικού περιοδικού 'Runway', εμπνευσμένου από τη Vogue.",
        "funFacts": [
            "Ο χαρακτήρας βασίζεται στην Anna Wintour, την επί δεκαετίες αρχισυντάκτρια της αμερικανικής Vogue.",
            "Η Meryl Streep κέρδισε υποψηφιότητα για Όσκαρ Α' Γυναικείου Ρόλου για την ερμηνεία της."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Devil_Wears_Prada_(film)",
        "tags": ["cinema", "fashion", "movies"]
    },
    {
        "id": "pop_culture_hard_170",
        "text": "Ποια διάσημη σειρά manga και anime του Kentaro Miura εξερευνά τον σκοτεινό κόσμο της σκοτεινής φαντασίας (dark fantasy) με πρωταγωνιστή τον Guts;",
        "correct": "Berserk",
        "distractors": ["Claymore", "Vinland Saga", "Vagabond"],
        "explanation": "Το 'Berserk' ξεκίνησε τη σειριοποίησή του το 1989 και θεωρείται ευρέως ένα από τα μεγαλύτερα αριστουργήματα του dark fantasy manga παγκοσμίως.",
        "funFacts": [
            "Το τεράστιο σπαθί του Guts ονομάζεται 'Dragon Slayer'.",
            "Το Berserk επηρέασε βαθιά βιντεοπαιχνίδια όπως η σειρά Dark Souls και το Elden Ring του Hidetaka Miyazaki."
        ],
        "source": "https://en.wikipedia.org/wiki/Berserk_(manga)",
        "tags": ["manga", "anime", "berserk"]
    },
    {
        "id": "pop_culture_hard_171",
        "text": "Ποιο τραγούδι της Kate Bush γνώρισε τεράστια παγκόσμια αναβίωση στα charts το 2022 χάρη στην 4η σεζόν της σειράς 'Stranger Things';",
        "correct": "Running Up That Hill (A Deal with God)",
        "distractors": ["Wuthering Heights", "Babooshka", "Cloudbusting"],
        "explanation": "Το τραγούδι του 1985 'Running Up That Hill' έφτασε στο #1 των βρετανικών charts 37 χρόνια μετά την κυκλοφορία του, αφού έσωσε τη Max από τον Vecna στο Stranger Things.",
        "funFacts": [
            "Έσπασε το ρεκόρ για το μεγαλύτερο χρονικό διάστημα που χρειάστηκε ποτέ ένα τραγούδι για να φτάσει στο #1 στο Ηνωμένο Βασίλειο.",
            "Η Kate Bush εξέφρασε δημόσια τη χαρά και την ευγνωμοσύνη της στους δημιουργούς της σειράς Duffer Brothers."
        ],
        "source": "https://en.wikipedia.org/wiki/Running_Up_That_Hill",
        "tags": ["stranger things", "music", "pop culture"]
    },
    {
        "id": "pop_culture_hard_172",
        "text": "Στο franchise 'Star Trek', ποιος είναι ο όρος για τον άγραφο υπέρτατο νόμο της Αστροστόλου που απαγορεύει την παρέμβαση στην εξέλιξη λιγότερο προηγμένων πολιτισμών;",
        "correct": "Prime Directive",
        "distractors": ["Omega Directive", "Temporal Accord", "First Protocol"],
        "explanation": "Η 'Prime Directive' (Πρωταρχική Οδηγία ή General Order 1) απαγορεύει ρητά στα μέλη της Starfleet να επεμβαίνουν στη φυσική και τεχνολογική ανάπτυξη προ-διαστημικών πολιτισμών.",
        "funFacts": [
            "Εισήχθη για πρώτη φορά στο επεισόδιο 'The Return of the Archons' της πρώτης σεζόν της αρχικής σειράς το 1967.",
            "Σχεδόν κάθε καπετάνιος του Star Trek έχει παραβιάσει την Prime Directive σε κρίσιμες ηθικές στιγμές."
        ],
        "source": "https://en.wikipedia.org/wiki/Prime_Directive",
        "tags": ["star trek", "sci-fi", "pop culture"]
    },
    {
        "id": "pop_culture_hard_173",
        "text": "Ποιο graphic novel του Frank Miller το 1986 επανεφηύρε τον Batman ως έναν 55χρονο γερασμένο και σκληροτράχηλο τιμωρό;",
        "correct": "The Dark Knight Returns",
        "distractors": ["Batman: Year One", "The Killing Joke", "The Long Halloween"],
        "explanation": "Το 'The Dark Knight Returns' (1986) του Frank Miller άλλαξε για πάντα τη βιομηχανία των κόμικς, εισάγοντας έναν πιο σκοτεινό, ώριμο και πολιτικό τόνο.",
        "funFacts": [
            "Στο κόμικ αυτό παρουσιάστηκε η Carrie Kelley ως η πρώτη επίσημη θηλυκή Robin.",
            "Η κλιμάκωση της σειράς περιλαμβάνει τη θρυλική αναμέτρηση μεταξύ Batman και Superman."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Dark_Knight_Returns",
        "tags": ["comics", "batman", "graphic novel"]
    },
    {
        "id": "pop_culture_hard_174",
        "text": "Ποια διάσημη ηθοποιός υποδύθηκε τη μητέρα της Rachel Green (Sandra Green) στην κωμική σειρά 'Τα Φιλαράκια' (Friends);",
        "correct": "Marlo Thomas",
        "distractors": ["Kathleen Turner", "Morgan Fairchild", "Christina Pickles"],
        "explanation": "Η Marlo Thomas υποδύθηκε τη Sandra Green, τη μητέρα της Rachel (Jennifer Aniston), σε guest εμφανίσεις στη σειρά Friends.",
        "funFacts": [
            "Η Morgan Fairchild υποδυόταν τη μητέρα του Chandler Bing (Nora Tyler Bing).",
            "Η Kathleen Turner υποδυόταν τον πατέρα του Chandler (Charles Bing)."
        ],
        "source": "https://en.wikipedia.org/wiki/Friends",
        "tags": ["friends", "sitcom", "television"]
    },
    {
        "id": "pop_culture_hard_175",
        "text": "Ποιο είναι το όνομα του σκύλου της οικογένειας Simpsons που υιοθετήθηκε στο πρώτο επεισόδιο της σειράς ('Simpsons Roasting on an Open Fire');",
        "correct": "Santa's Little Helper",
        "distractors": ["Snowball II", "Laddie", "Blinky"],
        "explanation": "Ο Santa's Little Helper είναι ένα λαγωνικό (greyhound) που υιοθέτησε ο Homer από κυνοδρομίες όταν ο σκύλος τερμάτισε τελευταίος στο χριστουγεννιάτικο επεισόδιο του 1989.",
        "funFacts": [
            "Το επεισόδιο αυτό ήταν το πρώτο επίσημο επεισόδιο πλήρους διάρκειας της σειράς The Simpsons.",
            "Η φωνή του σκύλου προέρχεται από διάφορους ηθοποιούς, κυρίως τον Dan Castellaneta και τον Frank Welker."
        ],
        "source": "https://en.wikipedia.org/wiki/Santa%27s_Little_Helper",
        "tags": ["the simpsons", "animation", "television"]
    },
    {
        "id": "pop_culture_hard_176",
        "text": "Ποιο διάσημο reality show του MTV, που προβλήθηκε για πρώτη φορά το 1992, θεωρείται ο θεμέλιος λίθος των σύγχρονων reality τηλεόρασης;",
        "correct": "The Real World",
        "distractors": ["Road Rules", "Survivor", "Big Brother"],
        "explanation": "Το 'The Real World' του MTV έκανε πρεμιέρα το 1992 με το σλόγκαν: 'This is the true story of seven strangers picked to live in a house...'.",
        "funFacts": [
            "Ήταν η μακροβιότερη σειρά στην ιστορία του MTV και διαμόρφωσε το είδος του reality τηλεόρασης.",
            "Η τρίτη σεζόν στο Σαν Φρανσίσκο (1994) έγραψε ιστορία με τον Pedro Zamora, έναν ανοιχτά ομοφυλόφιλο ακτιβιστή που ζούσε με HIV."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Real_World_(TV_series)",
        "tags": ["mtv", "reality tv", "television"]
    },
    {
        "id": "pop_culture_hard_177",
        "text": "Ποιος συγγραφέας δημιούργησε τον χαρακτήρα του Jason Bourne στα αρχικά βιβλία κατασκοπείας;",
        "correct": "Robert Ludlum",
        "distractors": ["Tom Clancy", "John le Carré", "Ian Fleming"],
        "explanation": "Ο Robert Ludlum έγραψε το μυθιστόρημα 'The Bourne Identity' το 1980, ξεκινώντας την τριλογία του Jason Bourne πριν το franchise συνεχιστεί από άλλους συγγραφείς και τον κινηματογράφο.",
        "funFacts": [
            "Ο Ludlum έγραψε συνολικά τρία βιβλία Bourne πριν τον θάνατό του το 2001.",
            "Η σειρά βιβλίων συνεχίστηκε μετά το 2004 από τον συγγραφέα Eric Van Lustbader."
        ],
        "source": "https://en.wikipedia.org/wiki/Jason_Bourne",
        "tags": ["literature", "cinema", "jason bourne"]
    },
    {
        "id": "pop_culture_hard_178",
        "text": "Στο κινηματογραφικό σύμπαν της Marvel (MCU), ποιος χαρακτήρας θυσιάζεται στον πλανήτη Vormir για να αποκτήσουν οι Εκδικητές το Soul Stone στο 'Avengers: Endgame';",
        "correct": "Black Widow (Natasha Romanoff)",
        "distractors": ["Hawkeye (Clint Barton)", "Gamora", "Nebula"],
        "explanation": "Στο 'Avengers: Endgame' (2019), η Natasha Romanoff (Black Widow) θυσιάζεται πέφτοντας στον γκρεμό του Vormir, ώστε ο Clint Barton να πάρει το Soul Stone.",
        "funFacts": [
            "Η Gamora είχε θυσιαστεί στον ίδιο γκρεμό από τον Thanos στην προηγούμενη ταινία 'Infinity War'.",
            "Η Scarlett Johansson υποδύθηκε τη Natasha Romanoff σε 9 ταινίες του MCU."
        ],
        "source": "https://en.wikipedia.org/wiki/Avengers:_Endgame",
        "tags": ["mcu", "marvel", "cinema"]
    },
    {
        "id": "pop_culture_hard_179",
        "text": "Ποιο είναι το όνομα του επιτραπέζιου παιχνιδιού στρατηγικής που δημιούργησε ο Klaus Teuber το 1995 και έγινε παγκόσμιο φαινόμενο;",
        "correct": "The Settlers of Catan",
        "distractors": ["Carcassonne", "Ticket to Ride", "Pandemic"],
        "explanation": "Το 'The Settlers of Catan' (σήμερα γνωστό απλά ως Catan) κυκλοφόρησε στη Γερμανία το 1995 και πυροδότησε την παγκόσμια αναγέννηση των σύγχρονων επιτραπέζιων παιχνιδιών (Eurogames).",
        "funFacts": [
            "Έχει μεταφραστεί σε περισσότερες από 40 γλώσσες και έχει πουλήσει πάνω από 40 εκατομμύρια αντίτυπα.",
            "Ο Teuber ήταν αρχικά οδοντοτεχνίτης και σχεδίαζε παιχνίδια στο υπόγειό του ως χόμπι."
        ],
        "source": "https://en.wikipedia.org/wiki/Catan",
        "tags": ["board games", "catan", "pop culture"]
    },
    {
        "id": "pop_culture_hard_180",
        "text": "Ποιος σκηνοθέτης υπογράφει το μουσικό βίντεο κλιπ του τραγουδιού 'Bad' (1987) του Michael Jackson, διάρκειας 18 λεπτών;",
        "correct": "Martin Scorsese",
        "distractors": ["John Landis", "David Fincher", "Spike Lee"],
        "explanation": "Ο Martin Scorsese σκηνοθέτησε το 18λεπτο βίντεο κλιπ για το 'Bad' του Michael Jackson, το οποίο γυρίστηκε σε σταθμό του μετρό στο Μπρούκλιν.",
        "funFacts": [
            "Στο βίντεο κλιπ έκανε το κινηματογραφικό του ντεμπούτο ο τότε άγνωστος Wesley Snipes ως ο αντίπαλος Mini Max.",
            "Το σενάριο του κλιπ έγραψε ο διάσημος μυθιστοριογράφος Richard Price."
        ],
        "source": "https://en.wikipedia.org/wiki/Bad_(Michael_Jackson_song)",
        "tags": ["michael jackson", "music video", "martin scorsese"]
    },
    {
        "id": "pop_culture_hard_181",
        "text": "Ποιο είναι το όνομα του διάσημου anime σκηνοθέτη που δημιούργησε τις ταινίες 'Perfect Blue', 'Millennium Actress' και 'Paprika';",
        "correct": "Satoshi Kon",
        "distractors": ["Mamoru Hosoda", "Makoto Shinkai", "Hideaki Anno"],
        "explanation": "Ο Satoshi Kon (1963-2010) ήταν ένας πρωτοποριακός δημιουργός anime του οποίου το οπτικό στυλ και η ανάμειξη πραγματικότητας και ψευδαίσθησης επηρέασαν σκηνοθέτες όπως ο Christopher Nolan και ο Darren Aronofsky.",
        "funFacts": [
            "Η ταινία 'Inception' του Nolan έχει έντονες θεματικές και οπτικές ομοιότητες με το 'Paprika' του Kon.",
            "Ο Kon απεβίωσε πρόωρα σε ηλικία μόλις 46 ετών από καρκίνο του παγκρέατος."
        ],
        "source": "https://en.wikipedia.org/wiki/Satoshi_Kon",
        "tags": ["anime", "cinema", "satoshi kon"]
    },
    {
        "id": "pop_culture_hard_182",
        "text": "Στη σειρά 'Breaking Bad', ποιο είναι το ψευδώνυμο που χρησιμοποιεί ο Walter White όταν μπαίνει στον υπόκοσμο των ναρκωτικών;",
        "correct": "Heisenberg",
        "distractors": ["Oppenheimer", "Schrödinger", "Fermi"],
        "explanation": "Ο Walter White επιλέγει το ψευδώνυμο 'Heisenberg' προς τιμήν του Werner Heisenberg, του διάσημου Γερμανού θεωρητικού φυσικού και θεμελιωτή της Αρχής της Απροσδιοριστίας.",
        "funFacts": [
            "Το μαύρο καπέλο pork pie και τα γυαλιά ηλίου έγιναν το εμβληματικό οπτικό σύμβολο του χαρακτήρα.",
            "Ο Bryan Cranston κέρδισε 4 βραβεία Primetime Emmy Α' Ανδρικού Ρόλου για την ερμηνεία του."
        ],
        "source": "https://en.wikipedia.org/wiki/Walter_White_(Breaking_Bad)",
        "tags": ["breaking bad", "television", "series"]
    },
    {
        "id": "pop_culture_hard_183",
        "text": "Ποιο είναι το όνομα του fictional συγκροτήματος heavy metal στην κλασική mockumentary ταινία του Rob Reiner το 1984;",
        "correct": "Spinal Tap",
        "distractors": ["Steel Dragon", "Bad News", "Crucial Taunt"],
        "explanation": "Η ταινία 'This Is Spinal Tap' (1984) παρακολουθεί το φανταστικό βρετανικό συγκρότημα Spinal Tap και δημιούργησε την πασίγνωστη ατάκα 'These go to eleven!'.",
        "funFacts": [
            "Το συγκρότημα έγινε τόσο δημοφιλές που οι ηθοποιοί (Christopher Guest, Michael McKean, Harry Shearer) έκαναν πραγματικές περιοδείες και έβγαλαν άλμπουμ.",
            "Το 2002 η ταινία επιλέχθηκε για διατήρηση στο National Film Registry των ΗΠΑ."
        ],
        "source": "https://en.wikipedia.org/wiki/This_Is_Spinal_Tap",
        "tags": ["cinema", "rock", "mockumentary"]
    },
    {
        "id": "pop_culture_hard_184",
        "text": "Ποιο διάσημο διαστημικό όχημα πιλοτάρει ο Han Solo και ο Chewbacca στο έπος του Star Wars;",
        "correct": "Millennium Falcon",
        "distractors": ["Slave I", "Ghost", "Outrider"],
        "explanation": "Το Millennium Falcon είναι ένα τροποποιημένο φορτηγό σκάφος τύπου YT-1300 που κατέχει τη φήμη ότι έκανε το 'Kessel Run σε λιγότερο από 12 parsecs'.",
        "funFacts": [
            "Ο George Lucas εμπνεύστηκε το αρχικό σχήμα του σκάφους από ένα χάμπουργκερ με μια ελιά καρφωμένη στο πλάι.",
            "Στο σκάφος υπήρχε το γνωστό ολογραφικό επιτραπέζιο παιχνίδι Dejarik."
        ],
        "source": "https://en.wikipedia.org/wiki/Millennium_Falcon",
        "tags": ["star wars", "sci-fi", "cinema"]
    },
    {
        "id": "pop_culture_hard_185",
        "text": "Ποιος ηθοποιός υποδύθηκε τον Joker στην ταινία 'Ο Σκοτεινός Ιππότης' (The Dark Knight, 2008) και κέρδισε μεταθανάτιο Όσκαρ Β' Ανδρικού Ρόλου;",
        "correct": "Heath Ledger",
        "distractors": ["Joaquin Phoenix", "Jack Nicholson", "Jared Leto"],
        "explanation": "Ο Heath Ledger έδωσε μια συγκλονιστική ερμηνεία ως Joker στο 'The Dark Knight', κερδίζοντας το Όσκαρ Β' Ανδρικού Ρόλου μετά τον τραγικό του θάνατο τον Ιανουάριο του 2008.",
        "funFacts": [
            "Ήταν ο πρώτος ηθοποιός που κέρδισε Όσκαρ για ρόλο σε ταινία βασισμένη σε κόμικς.",
            "Κλειδώθηκε σε δωμάτιο ξενοδοχείου στο Λονδίνο για περίπου ένα μήνα κρατώντας ημερολόγιο για να μπει στην ψυχοσύνθεση του Joker."
        ],
        "source": "https://en.wikipedia.org/wiki/Heath_Ledger",
        "tags": ["batman", "cinema", "oscars"]
    },
    {
        "id": "pop_culture_hard_186",
        "text": "Ποιο είναι το όνομα της φανταστικής πόλης στην οποία διαδραματίζεται η σειρά κινουμένων σχεδίων 'South Park';",
        "correct": "South Park, Κολοράντο",
        "distractors": ["Springfield, Όρεγκον", "Quahog, Ρόουντ Άιλαντ", "Arlen, Τέξας"],
        "explanation": "Η σειρά 'South Park' των Trey Parker και Matt Stone διαδραματίζεται σε μια ορεινή πόλη της κομητείας Park στο Κολοράντο.",
        "funFacts": [
            "Η παραγωγή των περισσότερων επεισοδίων του South Park διαρκεί μόλις 6 ημέρες, επιτρέποντάς τους να σχολιάζουν άμεσα την επικαιρότητα.",
            "Η σειρά έκανε πρεμιέρα τον Αύγουστο του 1997 στο Comedy Central."
        ],
        "source": "https://en.wikipedia.org/wiki/South_Park",
        "tags": ["south park", "animation", "television"]
    },
    {
        "id": "pop_culture_hard_187",
        "text": "Ποιος συγγραφέας έγραψε το δυστοπικό graphic novel 'V for Vendetta', εικονογραφημένο από τον David Lloyd;",
        "correct": "Alan Moore",
        "distractors": ["Neil Gaiman", "Grant Morrison", "Warren Ellis"],
        "explanation": "Το 'V for Vendetta' γράφτηκε από τον Alan Moore και εκδόθηκε μεταξύ 1982 και 1989. Η μάσκα του Guy Fawkes που σχεδίασε ο David Lloyd έγινε παγκόσμιο σύμβολο διαμαρτυρίας.",
        "funFacts": [
            "Η μάσκα υιοθετήθηκε αργότερα από την ομάδα χάκερ Anonymous και κινήματα όπως το Occupy Wall Street.",
            "Ο Alan Moore ζήτησε να αφαιρεθεί το όνομά του από τους τίτλους της κινηματογραφικής μεταφοράς του 2005."
        ],
        "source": "https://en.wikipedia.org/wiki/V_for_Vendetta",
        "tags": ["alan moore", "graphic novel", "comics"]
    },
    {
        "id": "pop_culture_hard_188",
        "text": "Ποιο διάσημο τραγούδι των Queen συμπεριλήφθηκε στην εμβληματική σκηνή του αυτοκινήτου στην ταινία 'Wayne's World' (1992);",
        "correct": "Bohemian Rhapsody",
        "distractors": ["We Will Rock You", "Don't Stop Me Now", "Radio Ga Ga"],
        "explanation": "Η σκηνή όπου ο Wayne και ο Garth τραγουδούν με πάθος το 'Bohemian Rhapsody' μέσα στο αυτοκίνητο AMC Pacer επανέφερε το τραγούδι στην κορυφή των charts στις ΗΠΑ.",
        "funFacts": [
            "Ο Mike Myers απείλησε να εγκαταλείψει την παραγωγή αν το στούντιο αντικαθιστούσε το κομμάτι με τραγούδι των Guns N' Roses.",
            "Ο Freddie Mercury είχε δει και εγκρίνει τη σκηνή λίγο πριν τον θάνατό του το 1991."
        ],
        "source": "https://en.wikipedia.org/wiki/Wayne%27s_World_(film)",
        "tags": ["queen", "cinema", "waynes world"]
    },
    {
        "id": "pop_culture_hard_189",
        "text": "Ποιο είναι το όνομα του μυστηριώδους τέρατος που τρομοκρατεί την πόλη Hawkins στην 1η σεζόν του 'Stranger Things';",
        "correct": "Demogorgon",
        "distractors": ["Mind Flayer", "Vecna", "Beholder"],
        "explanation": "Τα παιδιά στη σειρά ονομάζουν το ανθρωπόμορφο πλάσμα με το κεφάλι που ανοίγει σαν πέταλα λουλουδιού 'Demogorgon', από το ομώνυμο τέρας του Dungeons & Dragons.",
        "funFacts": [
            "Το κοστούμι του Demogorgon φορέθηκε από τον ηθοποιό Mark Steger με ειδικά πρακτικά εφέ animatronics.",
            "Στο D&D, ο Demogorgon είναι ένας ισχυρός Demon Lord με δύο κεφάλια μπαμπουίνου."
        ],
        "source": "https://en.wikipedia.org/wiki/Stranger_Things",
        "tags": ["stranger things", "netflix", "pop culture"]
    },
    {
        "id": "pop_culture_hard_190",
        "text": "Ποιο ήταν το πρώτο μουσικό βίντεο κλιπ που μεταδόθηκε ποτέ από το κανάλι MTV κατά την έναρξη των εκπομπών του την 1η Αυγούστου 1981;",
        "correct": "Video Killed the Radio Star (The Buggles)",
        "distractors": ["Money for Nothing (Dire Straits)", "Take On Me (A-ha)", "Billie Jean (Michael Jackson)"],
        "explanation": "Το MTV ξεκίνησε τη λειτουργία του στις 12:01 π.μ. την 1η Αυγούστου 1981 με τα λόγια 'Ladies and gentlemen, rock and roll' και αμέσως μετά έπαιξε το 'Video Killed the Radio Star' των The Buggles.",
        "funFacts": [
            "Το δεύτερο βίντεο που έπαιξε ποτέ στο κανάλι ήταν το 'You Better Run' της Pat Benatar.",
            "Ο Trevor Horn, συνιδρυτής των Buggles, έγινε αργότερα ένας από τους πιο επιδραστικούς παραγωγούς στην ιστορία της ποπ."
        ],
        "source": "https://en.wikipedia.org/wiki/Video_Killed_the_Radio_Star",
        "tags": ["mtv", "music", "history"]
    },
    {
        "id": "pop_culture_hard_191",
        "text": "Ποιο είναι το όνομα του υπερηρωικού οργανισμού των Minutemen και Crimebusters στο graphic novel 'Watchmen';",
        "correct": "Crimebusters",
        "distractors": ["The Justice League", "The Seven", "The Champions"],
        "explanation": "Στο 'Watchmen' του Alan Moore, η αρχική ομάδα της δεκαετίας του 1940 ήταν οι 'Minutemen', ενώ η απόπειρα σχηματισμού νέας ομάδας το 1966 ονομάστηκε 'Crimebusters'.",
        "funFacts": [
            "Το Watchmen είναι το μοναδικό graphic novel που συμπεριλήφθηκε στη λίστα του περιοδικού Time με τα 100 καλύτερα αγγλόφωνα μυθιστορήματα από το 1923.",
            "Ο χαρακτήρας του Rorschach βασίστηκε στους χαρακτήρες Question και Mr. A του Steve Ditko."
        ],
        "source": "https://en.wikipedia.org/wiki/Watchmen",
        "tags": ["watchmen", "comics", "alan moore"]
    },
    {
        "id": "pop_culture_hard_192",
        "text": "Στο franchise 'The Matrix', ποιο είναι το όνομα του hovercraft σκάφους του οποίου καπετάνιος είναι ο Morpheus;",
        "correct": "Nebuchadnezzar",
        "distractors": ["Mjolnir", "Logos", "Osiris"],
        "explanation": "Το σκάφος του Morpheus ονομάζεται 'Nebuchadnezzar' (Ναβουχοδονόσορας), φέροντας μια πλακέτα με την επιγραφή 'Mark III No. 11 - Made in the USA - Year 2069'.",
        "funFacts": [
            "Το όνομα είναι βιβλική αναφορά στον βασιλιά Ναβουχοδονόσορα της Βαβυλώνας, ο οποίος αναζητούσε την ερμηνεία των ονείρων του.",
            "Το σκάφος καταστρέφεται στο τέλος της ταινίας 'The Matrix Reloaded'."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Matrix_(franchise)",
        "tags": ["the matrix", "sci-fi", "cinema"]
    },
    {
        "id": "pop_culture_hard_193",
        "text": "Ποιος είναι ο τίτλος του πρώτου viral meme βίντεο στο διαδίκτυο (1996) που απεικόνιζε ένα τρισδιάστατο μωρό να χορεύει cha-cha;",
        "correct": "Dancing Baby (Baby Cha-Cha)",
        "distractors": ["Hamster Dance", "Crazy Frog", "Nyan Cat"],
        "explanation": "Το 'Dancing Baby' δημιουργήθηκε το 1996 από τους Michael Girard και Robert Lurye ως δείγμα δυνατοτήτων 3D animation και εμφανίστηκε ακόμη και στην τηλεοπτική σειρά Ally McBeal.",
        "funFacts": [
            "Διαδόθηκε αρχικά μέσω emails και ιστοσελίδων ως κινούμενο αρχείο GIF.",
            "Στην τηλεοπτική σειρά 'Ally McBeal', το μωρό εμφανιζόταν ως παραισθητική ενσάρκωση του βιολογικού ρολογιού της πρωταγωνίστριας."
        ],
        "source": "https://en.wikipedia.org/wiki/Dancing_baby",
        "tags": ["internet", "memes", "history"]
    },
    {
        "id": "pop_culture_hard_194",
        "text": "Ποια διάσημη ηθοποιός και μοντέλο πρωταγωνίστησε στον ρόλο της Leeloo στην καλτ ταινία επιστημονικής φαντασίας 'Το Πέμπτο Στοιχείο' (The Fifth Element, 1997);",
        "correct": "Milla Jovovich",
        "distractors": ["Charlize Theron", "Uma Thurman", "Natalie Portman"],
        "explanation": "Η Milla Jovovich υποδύθηκε τη Leeloo στο 'The Fifth Element' του Luc Besson, μιλώντας μια φανταστική θεϊκή γλώσσα 400 λέξεων που επινόησαν μαζί με τον σκηνοθέτη.",
        "funFacts": [
            "Τα εμβληματικά κοστούμια της ταινίας σχεδιάστηκαν από τον θρυλικό σχεδιαστή μόδας Jean-Paul Gaultier.",
            "Η Jovovich και ο Besson εξασκούσαν τη φανταστική γλώσσα γράφοντας γράμματα ο ένας στον άλλο."
        ],
        "source": "https://en.wikipedia.org/wiki/The_Fifth_Element",
        "tags": ["cinema", "sci-fi", "cult movies"]
    },
    {
        "id": "pop_culture_hard_195",
        "text": "Ποιο είναι το όνομα του φανταστικού βασιλείου του Black Panther στα κόμικς της Marvel;",
        "correct": "Wakanda",
        "distractors": ["Latveria", "Genosha", "Sokovia"],
        "explanation": "Η Wakanda είναι ένα τεχνολογικά υπερεξελιγμένο αφρικανικό έθνος που κρατά την τεχνολογία του κρυφή και διαθέτει τα μοναδικά κοιτάσματα vibranium στον πλανήτη.",
        "funFacts": [
            "Ο χαρακτήρας του Black Panther (T'Challa) δημιουργήθηκε από τον Stan Lee και τον Jack Kirby το 1966.",
            "Η ταινία 'Black Panther' (2018) ήταν η πρώτη ταινία υπερηρώων που προτάθηκε για Όσκαρ Καλύτερης Ταινίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Wakanda",
        "tags": ["marvel", "black panther", "comics"]
    },
    {
        "id": "pop_culture_hard_196",
        "text": "Ποιο viral φαινόμενο του 2014 περιλάμβανε ανθρώπους να ρίχνουν έναν κουβά παγωμένο νερό στο κεφάλι τους για να ευαισθητοποιήσουν το κοινό για ποια ασθένεια;",
        "correct": "Αμυοτροφική Πλευρική Σκλήρυνση (ALS)",
        "distractors": ["Σκλήρυνση κατά Πλάκας (MS)", "Νόσος του Πάρκινσον", "Νόσος του Αλτσχάιμερ"],
        "explanation": "Το 'ALS Ice Bucket Challenge' έγινε παγκόσμιο viral φαινόμενο το καλοκαίρι του 2014 και συγκέντρωσε πάνω από 200 εκατομμύρια δολάρια για την έρευνα της νόσου ALS παγκοσμίως.",
        "funFacts": [
            "Στην πρόκληση συμμετείχαν εξέχουσες προσωπικότητες όπως ο Bill Gates, ο Mark Zuckerberg και ο Stephen Hawking.",
            "Η χρηματοδότηση από το challenge οδήγησε άμεσα στην ανακάλυψη νέων γονιδίων που συνδέονται με τη νόσο (όπως το NEK1)."
        ],
        "source": "https://en.wikipedia.org/wiki/Ice_Bucket_Challenge",
        "tags": ["viral", "internet", "charity"]
    },
    {
        "id": "pop_culture_hard_197",
        "text": "Στη σειρά 'Game of Thrones', ποιο είναι το όνομα του σπαθιού από βαλυριανό ατσάλι που ανήκε πατρογονικά στον οίκο Stark;",
        "correct": "Ice",
        "distractors": ["Longclaw", "Needle", "Oathkeeper"],
        "explanation": "Το 'Ice' ήταν το τεράστιο προγονικό δίχειρο σπαθί του Lord Eddard Stark, το οποίο έλιωσε ο Tywin Lannister μετά την εκτέλεση του Ned για να φτιάξει δύο νέα σπαθιά (Widow's Wail και Oathkeeper).",
        "funFacts": [
            "Το Longclaw είναι το σπαθί του οίκου Mormont που δόθηκε στον Jon Snow από τον Jeor Mormont.",
            "Το Needle είναι το λεπτό σπαθί που έκανε δώρο ο Jon Snow στην Arya Stark."
        ],
        "source": "https://en.wikipedia.org/wiki/Game_of_Thrones",
        "tags": ["game of thrones", "tv series", "fantasy"]
    },
    {
        "id": "pop_culture_hard_198",
        "text": "Ποιο franchise παιχνιδιών και ταινιών δημιούργησε η εταιρεία Hasbro το 1984 με ρομπότ που μεταμορφώνονται σε οχήματα;",
        "correct": "Transformers",
        "distractors": ["GoBots", "Gundam", "Voltron"],
        "explanation": "Οι Transformers γεννήθηκαν το 1984 όταν η Hasbro αγόρασε τα δικαιώματα των ιαπωνικών σειρών παιχνιδιών Diaclone και Microman της Takara και δημιούργησε το franchise.",
        "funFacts": [
            "Ο Peter Cullen έχει δώσει τη φωνή του στον Optimus Prime από την πρώτη σειρά κινουμένων σχεδίων του 1984 μέχρι τις σύγχρονες ταινίες.",
            "Τα ονόματα πολλών χαρακτήρων όπως Optimus Prime και Megatron επινοήθηκαν από συγγραφείς της Marvel Comics (Bob Budiansky)."
        ],
        "source": "https://en.wikipedia.org/wiki/Transformers",
        "tags": ["transformers", "hasbro", "animation"]
    },
    {
        "id": "pop_culture_hard_199",
        "text": "Ποιο είναι το όνομα της γάτας στο διαδίκτυο που έγινε παγκόσμιο meme το 2012 λόγω της μόνιμα συνοφρυωμένης έκφρασής της;",
        "correct": "Grumpy Cat",
        "distractors": ["Keyboard Cat", "Nyan Cat", "Lil Bub"],
        "explanation": "Η Grumpy Cat (πραγματικό όνομα Tardar Sauce) έγινε διάσημη όταν ο αδερφός της ιδιοκτήτριάς της ανάρτησε φωτογραφία της στο Reddit τον Σεπτέμβριο του 2012.",
        "funFacts": [
            "Η μόνιμη έκφρασή της οφειλόταν σε νανισμό της γάτας (feline dwarfism) και προγναθισμό.",
            "Κέρδισε εκατομμύρια δολάρια από διαφημίσεις, βιβλία, ακόμη και τηλεοπτική χριστουγεννιάτικη ταινία."
        ],
        "source": "https://en.wikipedia.org/wiki/Grumpy_Cat",
        "tags": ["grumpy cat", "memes", "internet"]
    },
    {
        "id": "pop_culture_hard_200",
        "text": "Ποιος σκηνοθέτης είναι γνωστός για τη συνεργασία του με τον ηθοποιό Johnny Depp σε 8 ταινίες, ξεκινώντας από το 'Edward Scissorhands' (1990);",
        "correct": "Tim Burton",
        "distractors": ["Terry Gilliam", "David Lynch", "Wes Anderson"],
        "explanation": "Ο Tim Burton και ο Johnny Depp συνεργάστηκαν στενά σε εμβληματικές γοτθικές και εκκεντρικές ταινίες, όπως τα Edward Scissorhands, Ed Wood, Sleepy Hollow, Charlie and the Chocolate Factory και Sweeney Todd.",
        "funFacts": [
            "Σε πολλές από αυτές τις ταινίες συμμετείχε επίσης η τότε σύντροφος του Burton, Helena Bonham Carter.",
            "Η μουσική των περισσότερων ταινιών του Burton έχει γραφτεί από τον Danny Elfman."
        ],
        "source": "https://en.wikipedia.org/wiki/Tim_Burton",
        "tags": ["tim burton", "johnny depp", "cinema"]
    },
    {
        "id": "pop_culture_hard_201",
        "text": "Ποιο είναι το όνομα του εικονικού καναλιού του YouTube που εκπέμπει ασταμάτητα χαλαρωτική μουσική lo-fi hip hop με μια anime κοπέλα να διαβάζει;",
        "correct": "Lofi Girl (ChilledCow)",
        "distractors": ["Chillhop Raccoon", "Study Beats TV", "Anime Chill Vibes"],
        "explanation": "Το κανάλι Lofi Girl (αρχικά γνωστό ως ChilledCow) ξεκίνησε το 2017 και έγινε σύμβολο για εκατομμύρια μαθητές και εργαζόμενους παγκοσμίως για συγκέντρωση και μελέτη.",
        "funFacts": [
            "Ο χαρακτήρας της μαθήτριας που γράφει στο γραφείο σχεδιάστηκε από τον Juan Pablo Machado και εμπνεύστηκε από την ταινία Whisper of the Heart του Studio Ghibli.",
            "Η ζωντανή ροή έχει διακοπεί ελάχιστες φορές, συγκεντρώνοντας δεκάδες χιλιάδες ώρες συνεχούς εκπομπής."
        ],
        "source": "https://en.wikipedia.org/wiki/Lofi_Girl",
        "tags": ["lofi girl", "internet", "youtube"]
    },
    {
        "id": "pop_culture_hard_202",
        "text": "Ποιος ηθοποιός υποδύθηκε τον Gandalf στην κινηματογραφική τριλογία 'Ο Άρχοντας των Δαχτυλιδιών' του Peter Jackson;",
        "correct": "Ian McKellen",
        "distractors": ["Christopher Lee", "Michael Gambon", "Patrick Stewart"],
        "explanation": "Ο Sir Ian McKellen ενσάρκωσε τον Gandalf the Grey και Gandalf the White στην τριλογία του Άρχοντα των Δαχτυλιδιών και αργότερα στην τριλογία του Hobbit.",
        "funFacts": [
            "Ήταν υποψήφιος για Όσκαρ Β' Ανδρικού Ρόλου για την ερμηνεία του στην 'Συντροφιά του Δαχτυλιδιού'.",
            "Ο ρόλος είχε αρχικά προταθεί στον Sean Connery, ο οποίος τον απέρριψε δηλώνοντας ότι δεν κατάλαβε το σενάριο."
        ],
        "source": "https://en.wikipedia.org/wiki/Ian_McKellen",
        "tags": ["lord of the rings", "cinema", "gandalf"]
    },
    {
        "id": "pop_culture_hard_203",
        "text": "Ποιος έγραψε το εμβληματικό τραγούδι των Beatles 'Yesterday' (1965), του οποίου η μελωδία του ήρθε στον ύπνο του;",
        "correct": "Paul McCartney",
        "distractors": ["John Lennon", "George Harrison", "Ringo Starr"],
        "explanation": "Ο Paul McCartney ξύπνησε ένα πρωί με τη μελωδία του 'Yesterday' ολοκληρωμένη στο κεφάλι του, χρησιμοποιώντας αρχικά τους πρόχειρους στίχους 'Scrambled eggs, oh my baby how I love your legs'.",
        "funFacts": [
            "Είναι ένα από τα πιο διασκευασμένα τραγούδια στην ιστορία της ηχογραφημένης μουσικής, με πάνω από 2.200 διασκευές.",
            "Κανένα άλλο μέλος των Beatles δεν έπαιξε στο κομμάτι· περιλαμβάνει μόνο τον McCartney με ακουστική κιθάρα και ένα κουαρτέτο εγχόρδων."
        ],
        "source": "https://en.wikipedia.org/wiki/Yesterday_(Beatles_song)",
        "tags": ["the beatles", "paul mccartney", "music"]
    },
    {
        "id": "pop_culture_hard_204",
        "text": "Ποια είναι η ταυτότητα του μυστηριώδους δολοφόνου 'Ghostface' στην πρώτη ταινία 'Scream' (1996) του Wes Craven;",
        "correct": "Billy Loomis και Stu Macher",
        "distractors": ["Roman Bridger", "Mickey Altieri", "Jill Roberts"],
        "explanation": "Στο πρωτοποριακό twist του 'Scream' (1996), αποκαλύπτεται ότι ο Ghostface δεν ήταν ένα άτομο αλλά δύο: ο φίλος της Sidney, Billy Loomis, και ο συνεργός του Stu Macher.",
        "funFacts": [
            "Η ταινία αναζωογόνησε ολόκληρο το είδος των ταινιών slasher στη δεκαετία του 1990.",
            "Η μάσκα του Ghostface ανακαλύφθηκε τυχαία από την παραγωγό Marianne Maddalena σε ένα εγκαταλελειμμένο σπίτι κατά την αναζήτηση τοποθεσιών."
        ],
        "source": "https://en.wikipedia.org/wiki/Scream_(1996_film)",
        "tags": ["scream", "horror", "cinema"]
    },
    {
        "id": "pop_culture_hard_205",
        "text": "Ποια βρετανική σειρά επιστημονικής φαντασίας του Charlie Brooker εξερευνά τις σκοτεινές και απρόβλεπτες συνέπειες της σύγχρονης τεχνολογίας;",
        "correct": "Black Mirror",
        "distractors": ["Utopia", "Humans", "Inside No. 9"],
        "explanation": "Το 'Black Mirror' ξεκίνησε το 2011 από το Channel 4 και αργότερα πέρασε στο Netflix, αποτελώντας ανθολογία δυστοπικών ιστοριών για την τεχνολογία και την ανθρώπινη φύση.",
        "funFacts": [
            "Ο τίτλος 'Black Mirror' αναφέρεται στη μαύρη οθόνη μιας απενεργοποιημένης τηλεόρασης, υπολογιστή ή smartphone που αντανακλά το πρόσωπο του χρήστη.",
            "Το 2018 κυκλοφόρησε η διαδραστική ταινία 'Bandersnatch' όπου οι θεατές επέλεγαν την πορεία της πλοκής."
        ],
        "source": "https://en.wikipedia.org/wiki/Black_Mirror",
        "tags": ["black mirror", "television", "sci-fi"]
    },
    {
        "id": "pop_culture_hard_206",
        "text": "Ποιος χαρακτήρας του Star Wars εισήγαγε για πρώτη φορά το φωτόσπαθο διπλής λεπίδας (double-bladed lightsaber) στην ταινία 'The Phantom Menace' (1999);",
        "correct": "Darth Maul",
        "distractors": ["Count Dooku", "General Grievous", "Kylo Ren"],
        "explanation": "Ο Darth Maul (υποδυόμενος από τον Ray Park) άναψε το κόκκινο φωτόσπαθο διπλής λεπίδας στη θρυλική μονομαχία 'Duel of the Fates' εναντίον των Qui-Gon Jinn και Obi-Wan Kenobi.",
        "funFacts": [
            "Ο Ray Park ήταν εκπαιδευμένος πολεμικών τεχνών και κασκαντέρ, γεγονός που έδωσε μοναδική ακροβατική χορογραφία στη σκηνή.",
            "Τη φωνή του Maul στην ταινία έκανε ο Peter Serafinowicz."
        ],
        "source": "https://en.wikipedia.org/wiki/Darth_Maul",
        "tags": ["star wars", "cinema", "lightsaber"]
    },
    {
        "id": "pop_culture_hard_207",
        "text": "Ποιο είναι το όνομα του χαρακτήρα anime που φιλοδοξεί να γίνει ο 'Βασιλιάς των Πειρατών' και να βρει τον θησαυρό One Piece;",
        "correct": "Monkey D. Luffy",
        "distractors": ["Roronoa Zoro", "Portgas D. Ace", "Trafalgar Law"],
        "explanation": "Ο Monkey D. Luffy είναι ο πρωταγωνιστής του 'One Piece' του Eiichiro Oda, ο οποίος απέκτησε ελαστικό σώμα αφού έφαγε κατά λάθος το Devil Fruit 'Gomu Gomu no Mi'.",
        "funFacts": [
            "Το One Piece είναι το πιο επιτυχημένο manga στην ιστορία, έχοντας πουλήσει πάνω από 516 εκατομμύρια αντίτυπα παγκοσμίως.",
            "Ο Luffy ηγείται του πληρώματος των Straw Hat Pirates (Πειρατές της Ψάθινης Κούκλας)."
        ],
        "source": "https://en.wikipedia.org/wiki/One_Piece",
        "tags": ["one piece", "anime", "manga"]
    },
    {
        "id": "pop_culture_hard_208",
        "text": "Ποιο τραγούδι της Lady Gaga έγινε το πρώτο της παγκόσμιο #1 hit το 2008 από το ντεμπούτο άλμπουμ της 'The Fame';",
        "correct": "Just Dance",
        "distractors": ["Poker Face", "Bad Romance", "Paparazzi"],
        "explanation": "Το 'Just Dance' (με συμμετοχή του Colby O'Donis) κυκλοφόρησε τον Απρίλιο του 2008 και εκτόξευσε τη Lady Gaga στην παγκόσμια μουσική σκηνή.",
        "funFacts": [
            "Η Gaga έγραψε το τραγούδι μέσα σε μόλις 10 λεπτά ενώ βρισκόταν σε στούντιο στο Χόλιγουντ.",
            "Ακολούθησε το 'Poker Face', το οποίο έγινε το πιο εμπορικό single παγκοσμίως για το 2009."
        ],
        "source": "https://en.wikipedia.org/wiki/Just_Dance_(song)",
        "tags": ["lady gaga", "music", "pop"]
    },
    {
        "id": "pop_culture_hard_209",
        "text": "Ποιο είναι το όνομα του πρωταγωνιστικού χαρακτήρα στο franchise 'Alien' που ενσαρκώνει η Sigourney Weaver;",
        "correct": "Ellen Ripley",
        "distractors": ["Sarah Connor", "Dana Scully", "Laurie Strode"],
        "explanation": "Η Ellen Ripley είναι η υποπλοίαρχος του εμπορικού σκάφους Nostromo στην ταινία 'Alien' (1979) του Ridley Scott και θεωρείται μία από τις σπουδαιότερες γυναικείες ηρωίδες στην ιστορία του κινηματογράφου.",
        "funFacts": [
            "Η Sigourney Weaver προτάθηκε για Όσκαρ Α' Γυναικείου Ρόλου για το 'Aliens' (1986), κάτι πρωτοφανές για ταινία επιστημονικής φαντασίας και δράσης.",
            "Ο ρόλος αρχικά είχε γραφτεί ως ανδρικός χαρακτήρας στο αρχικό προσχέδιο του σεναρίου."
        ],
        "source": "https://en.wikipedia.org/wiki/Ellen_Ripley",
        "tags": ["alien", "cinema", "sci-fi"]
    },
    {
        "id": "pop_culture_hard_210",
        "text": "Ποιο είναι το όνομα της φανταστικής εφημερίδας στην οποία εργάζεται ο Clark Kent (Superman) ως δημοσιογράφος;",
        "correct": "Daily Planet",
        "distractors": ["Daily Bugle", "Gotham Gazette", "The Daily Globe"],
        "explanation": "Ο Clark Kent εργάζεται στην εφημερίδα 'Daily Planet' της πόλης Metropolis, υπό την καθοδήγηση του αρχισυντάκτη Perry White και μαζί με τη Lois Lane.",
        "funFacts": [
            "Το Daily Bugle είναι η αντίστοιχη φανταστική εφημερίδα της Marvel στη Νέα Υόρκη, όπου εργάζεται ο Peter Parker (Spider-Man).",
            "Το εμβληματικό κτίριο της Daily Planet χαρακτηρίζεται από μια τεράστια περιστρεφόμενη υδρόγειο σφαίρα στην κορυφή του."
        ],
        "source": "https://en.wikipedia.org/wiki/Daily_Planet",
        "tags": ["superman", "dc comics", "comics"]
    }
]

questions = []
for q in raw_questions:
    opts = [q["correct"]] + q["distractors"]
    random.shuffle(opts)
    c_idx = opts.index(q["correct"])
    questions.append({
        "id": q["id"],
        "categoryId": "pop_culture",
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
    print(f"Loaded {len(questions)} questions for pop_culture_hard batch 4.")
    validate_and_append("pop_culture", "hard", 5, questions)

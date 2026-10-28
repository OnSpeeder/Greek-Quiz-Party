# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# Batch 1: tech_hard_211 to tech_hard_260 (50 questions)
raw_questions = [
    {
        "id": "tech_hard_211",
        "text": "Ποιο θεμελιώδες θεώρημα της υπολογιστικής πολυπλοκότητας διατυπώθηκε από τους Stephen Cook (1971) και Leonid Levin, αποδεικνύοντας ότι το πρόβλημα ικανοποιησιμότητας Boole (Boolean SAT) είναι NP-πλήρες;",
        "correct": "Θεώρημα Cook-Levin",
        "distractors": ["Θεώρημα της Μη Πληρότητας του Gödel", "Θεώρημα του Master", "Θεώρημα του Shannon-Hartley"],
        "explanation": "Το θεώρημα Cook-Levin έδειξε ότι οποιοδήποτε πρόβλημα που μπορεί να επιλυθεί σε πολυωνυμικό χρόνο από μια μη ντετερμινιστική μηχανή Turing μπορεί να αναχθεί σε πολυωνυμικό χρόνο στο πρόβλημα SAT, θεμελιώνοντας την κλάση NP-Complete.",
        "funFacts": [
            "Το ερώτημα αν P = NP αποτελεί ένα από τα επτά Προβλήματα της Χιλιετίας του Ινστιτούτου Clay, με έπαθλο 1.000.000 δολαρίων για τη λύση του.",
            "Ο Leonid Levin ανακάλυψε ανεξάρτητα το θεώρημα στη Σοβιετική Ένωση περίπου την ίδια περίοδο με τον Cook στις ΗΠΑ, αλλά η εργασία του άργησε να γίνει γνωστή στη Δύση."
        ],
        "source": "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem",
        "tags": ["technology", "computer_science", "complexity", "algorithms"]
    },
    {
        "id": "tech_hard_212",
        "text": "Ποιο ιστορικό πρόβλημα απέδειξε ο Alan Turing το 1936 ότι είναι αλγοριθμικά μη επιλύσιμο (undecidable), καταρρίπτοντας το Entscheidungsproblem του David Hilbert;",
        "correct": "Το Πρόβλημα του Τερματισμού (Halting Problem)",
        "distractors": ["Το Πρόβλημα των Τεσσάρων Χρωμάτων", "Η Υπόθεση του Συνεχούς", "Το Πρόβλημα του Περιοδεύοντος Πωλητή"],
        "explanation": "Ο Turing απέδειξε μέσω της μεθόδου της διαγωνιοποίησης ότι είναι αδύνατο να γραφτεί ένα γενικό υπολογιστικό πρόγραμμα που να αποφασίζει με βεβαιότητα αν ένα οποιοδήποτε άλλο αυθαίρετο πρόγραμμα θα τερματίσει ή θα εκτελείται επ' άπειρον.",
        "funFacts": [
            "Για να διατυπώσει την απόδειξη, ο Turing επινόησε την αφηρημένη έννοια της Μηχανής Turing, θέτοντας τα μαθηματικά θεμέλια της σύγχρονης επιστήμης υπολογιστών.",
            "Άμεση συνέπεια του Halting Problem είναι το Θεώρημα του Rice, το οποίο αποδεικνύει ότι οποιαδήποτε μη τετριμμένη σημασιολογική ιδιότητα ενός προγράμματος είναι μη αποφασίσιμη."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CF%8C%CE%B2%CE%BB%CE%B7%CE%BC%CE%B1_%CF%84%CE%BF%CF%85_%CF%84%CE%B5%CF%81%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%8D",
        "tags": ["technology", "computer_science", "turing", "theory"]
    },
    {
        "id": "tech_hard_213",
        "text": "Ποιο μαθηματικό θεώρημα της θεωρίας υπολογισμού που διατυπώθηκε από τον Henry Gordon Rice το 1953 δηλώνει ότι οποιαδήποτε μη τετριμμένη σημασιολογική ιδιότητα της συμπεριφοράς ενός προγράμματος είναι γενικά μη αποφασίσιμη;",
        "correct": "Θεώρημα του Ράις (Rice's Theorem)",
        "distractors": ["Θεώρημα του Καντόρ", "Θεώρημα του Μπράουερ", "Θεώρημα του Πουανκαρέ"],
        "explanation": "Το θεώρημα του Rice αποδεικνύει ότι δεν μπορεί να υπάρξει αλγόριθμος που να εξετάζει τον πηγαίο κώδικα ενός προγράμματος και να απαντά με απόλυτη βεβαιότητα αν αυτό είναι απαλλαγμένο από σφάλματα διαίρεσης με το μηδέν, διαρροές μνήμης ή ιούς.",
        "funFacts": [
            "Εξηγεί θεωρητικά γιατί τα εργαλεία στατικής ανάλυσης κώδικα και τα προγράμματα antivirus πρέπει αναγκαστικά να βασίζονται σε ευρετικές μεθόδους, έχοντας ψευδώς θετικά ή ψευδώς αρνητικά αποτελέσματα.",
            "Αποτελεί γενίκευση του Προβλήματος του Τερματισμού (Halting Problem)."
        ],
        "source": "https://en.wikipedia.org/wiki/Rice%27s_theorem",
        "tags": ["technology", "computer_science", "theory", "rice_theorem"]
    },
    {
        "id": "tech_hard_214",
        "text": "Ποιο θεμέλιο της θεωρίας τύπων και των συναρτησιακών γλωσσών αναπτύχθηκε από τον Alonzo Church τη δεκαετία του 1930, βασισμένο σε αφηρημένες συναρτήσεις και μεταβλητές;",
        "correct": "Λογισμός Λάμδα (Lambda Calculus)",
        "distractors": ["Άλγεβρα Boole", "Πολυωνυμικός Λογισμός", "Διαφορικός Λογισμός"],
        "explanation": "Ο Λογισμός Λάμδα αποδείχθηκε από τον Church ότι είναι υπολογιστικά ισοδύναμος με τη Μηχανή Turing (Θέση Church-Turing), αποτελώντας τη βάση όλων των συναρτησιακών γλωσσών όπως Lisp, Haskell και OCaml.",
        "funFacts": [
            "Στον καθαρό λογισμό λάμδα δεν υπάρχουν αριθμοί, πράξεις ή δομές δεδομένων: τα πάντα, συμπεριλαμβανομένων των φυσικών αριθμών (Church numerals) και των τιμών True/False (Church booleans), ορίζονται αποκλειστικά ως συναρτήσεις!",
            "Η βασική πράξη υπολογισμού ονομάζεται βήτα-αναγωγή (beta-reduction) και αντιστοιχεί στην εφαρμογή μιας συνάρτησης σε ένα όρισμα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CE%B3%CE%B9%CF%83%CE%BC%CF%8C%CF%82_%CE%BB%CE%AC%CE%BC%CE%B4%CE%B1",
        "tags": ["technology", "computer_science", "lambda_calculus", "functional_programming"]
    },
    {
        "id": "tech_hard_215",
        "text": "Ποια βαθιά θεωρητική αντιστοιχία (ισομορφισμός) συνδέει τα προγράμματα υπολογιστή με τις μαθηματικές αποδείξεις και τους τύπους δεδομένων με τις λογικές προτάσεις;",
        "correct": "Ισομορφισμός Curry-Howard",
        "distractors": ["Θεώρημα Church-Rosser", "Δυαδικότητα Pontryagin", "Αντιστοιχία AdS/CFT"],
        "explanation": "Ο ισομορφισμός Curry-Howard ('Proofs-as-Programs') αποδεικνύει ότι η συγγραφή ενός έγκυρου προγράμματος σε ένα αυστηρό σύστημα τύπων ισοδυναμεί απόλυτα με την κατασκευή μιας μαθηματικής απόδειξης στη διαισθητική λογική.",
        "funFacts": [
            "Αποτελεί το θεμέλιο σύγχρονων διαδραστικών βοηθών μαθηματικών αποδείξεων (proof assistants) όπως το Coq, το Lean και το Agda.",
            "Επεκτάθηκε αργότερα από τον Philip Wadler ώστε να συμπεριλάβει την κλασική λογική μέσω ελέγχου συνέχειας (continuations)."
        ],
        "source": "https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence",
        "tags": ["technology", "computer_science", "type_theory", "curry_howard"]
    },
    {
        "id": "tech_hard_216",
        "text": "Ποιος διάσημος αλγόριθμος εξαγωγής τύπων (type inference) επιτρέπει σε γλώσσες όπως η Haskell και η OCaml να συμπεραίνουν αυτόματα τους πιο γενικούς τύπους δεδομένων (principal types) χωρίς δηλώσεις τύπων από τον προγραμματιστή;",
        "correct": "Αλγόριθμος Hindley-Milner (Αλγόριθμος W)",
        "distractors": ["Αλγόριθμος Knuth-Morris-Pratt", "Αλγόριθμος Tarjan", "Αλγόριθμος Aho-Corasick"],
        "explanation": "Ο αλγόριθμος των J. Roger Hindley και Robin Milner συνδυάζει την ενοποίηση (unification του Robinson) με πολυμορφισμό τύπων Parametric Polymorphism, προσφέροντας απόλυτη στατική ασφάλεια τύπων με τη συντακτική ευκολία δυναμικών γλωσσών.",
        "funFacts": [
            "Ο Robin Milner τιμήθηκε με το Βραβείο Turing το 1991 για τη σχεδίαση της γλώσσας ML και του συστήματος τύπων Hindley-Milner.",
            "Ο αλγόριθμος εγγυάται ότι αν ένα πρόγραμμα γίνει αποδεκτό από τον compiler, δεν θα παρουσιάσει ποτέ σφάλματα αναντιστοιχίας τύπων κατά τον χρόνο εκτέλεσης ('well-typed programs cannot go wrong')."
        ],
        "source": "https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system",
        "tags": ["technology", "type_systems", "programming_languages", "compilers"]
    },
    {
        "id": "tech_hard_217",
        "text": "Ποια μαθηματική έννοια από τη θεωρία κατηγοριών εισήχθη στην επιστήμη υπολογιστών από τον Eugenio Moggi και εκλαϊκεύτηκε στη γλώσσα Haskell από τον Philip Wadler για τη διαχείριση παρενεργειών (side effects);",
        "correct": "Μονάδα (Monad)",
        "distractors": ["Functor", "Μονοειδές (Monoid)", "Ενδομορφισμός (Endomorphism)"],
        "explanation": "Οι μονάδες (Monads) επιτρέπουν σε αμιγώς συναρτησιακές γλώσσες (όπου οι συναρτήσεις είναι μαθηματικά καθαρές χωρίς κατάσταση) να διαχειρίζονται πράξεις εισόδου/εξόδου (I/O), μεταλλάξιμη κατάσταση και διαχείριση σφαλμάτων με καθαρό τρόπο.",
        "funFacts": [
            "Μια διάσημη χιουμοριστική ατάκα του James Iry ορίζει τη μονάδα ως 'ένα μονοειδές στην κατηγορία των ενδοσυναρτητών (monoid in the category of endofunctors)'.",
            "Κάθε Monad στη Haskell πρέπει να ικανοποιεί τρεις μαθηματικούς νόμους: αριστερή ταυτότητα, δεξιά ταυτότητα και προσεταιριστικότητα."
        ],
        "source": "https://en.wikipedia.org/wiki/Monad_(functional_programming)",
        "tags": ["technology", "functional_programming", "monads", "haskell"]
    },
    {
        "id": "tech_hard_218",
        "text": "Ποιος κλασικός αλγόριθμος συλλογής απορριμμάτων (Garbage Collection) διατυπώθηκε από τον Edsger Dijkstra το 1978, χωρίζοντας τα αντικείμενα μνήμης σε λευκό, γκρι και μαύρο σύνολο;",
        "correct": "Αλγόριθμος μαρκαρίσματος τριών χρωμάτων (Tri-color Marking)",
        "distractors": ["Αλγόριθμος Baker", "Αλγόριθμος Cheneys", "Αλγόριθμος Boehm-Demers-Weiser"],
        "explanation": "Στον αλγόριθμο Tri-color, τα λευκά αντικείμενα είναι υποψήφια για διαγραφή, τα γκρι έχουν επισκεφθεί αλλά δεν έχουν ελεγχθεί οι δείκτες τους, και τα μαύρα έχουν επιβιώσει πλήρως, επιτρέποντας στον GC να τρέχει ταυτόχρονα με την εφαρμογή (concurrent GC).",
        "funFacts": [
            "Αποτελεί τη θεωρητική βάση των σύγχρονων concurrent συλλεκτών απορριμμάτων σε προηγμένες εικονικές μηχανές, όπως ο ZGC του Java HotSpot και ο GC της γλώσσας Go.",
            "Απαιτεί τη χρήση 'φραγμών εγγραφής' (write barriers) για να αποτρέπει την κατάσταση όπου η εφαρμογή συνδέει κρυφά ένα λευκό αντικείμενο απευθείας σε ένα μαύρο αντικείμενο."
        ],
        "source": "https://en.wikipedia.org/wiki/Tracing_garbage_collection#Tri-color_marking",
        "tags": ["technology", "garbage_collection", "memory_management", "algorithms"]
    },
    {
        "id": "tech_hard_219",
        "text": "Ποια είναι η θεμελιώδης εμπειρική παρατήρηση στη διαχείριση μνήμης, γνωστή ως 'Αδύναμη Γενεαλογική Υπόθεση' (Weak Generational Hypothesis);",
        "correct": "Η συντριπτική πλειονότητα των αντικειμένων που δεσμεύονται στη μνήμη πεθαίνουν (καθίστανται άχρηστα) σχεδόν αμέσως μετά τη δημιουργία τους",
        "distractors": ["Τα αντικείμενα που επιβιώνουν για 10 δευτερόλεπτα διαγράφονται αυτόματα", "Η μνήμη RAM γεμίζει πάντα με εκθετικό ρυθμό", "Κάθε γενιά επεξεργαστών διαθέτει τη μισή κρυφή μνήμη"],
        "explanation": "Σύμφωνα με αυτή την υπόθεση (επαληθευμένη σε πάνω από το 95% των προγραμμάτων), τα αντικείμενα χωρίζονται σε 'Νέα Γενιά' (Young Gen) και 'Παλιά Γενιά' (Old Gen). Ο GC σαρώνει ταχύτατα μόνο τη νέα γενιά (Minor GC), επιτυγχάνοντας ελάχιστες παύσεις.",
        "funFacts": [
            "Αντικείμενα όπως τοπικές μεταβλητές συναρτήσεων και προσωρινοί υπολογισμοί πεθαίνουν μέσα σε κλάσματα χιλιοστοδευτερολέπτου.",
            "Όσα ελάχιστα αντικείμενα επιβιώνουν από διαδοχικούς κύκλους συλλογής 'προάγονται' (promoted) στην παλιά γενιά (Tenured generation)."
        ],
        "source": "https://en.wikipedia.org/wiki/Tracing_garbage_collection#Generational_GC",
        "tags": ["technology", "garbage_collection", "java", "memory"]
    },
    {
        "id": "tech_hard_220",
        "text": "Ποιος υβριδικός αλγόριθμος ταξινόμησης σχεδιάστηκε από τον Tim Peters το 2002 για τη γλώσσα Python, συνδυάζοντας την ταξινόμηση συγχώνευσης (Merge Sort) με την ταξινόμηση με εισαγωγή (Insertion Sort);",
        "correct": "Timsort",
        "distractors": ["Introsort", "Smoothsort", "Block Sort"],
        "explanation": "Το Timsort εκμεταλλεύεται φυσικά προϋπάρχουσες ταξινομημένες ακολουθίες (natural runs) στα πραγματικά δεδομένα, προσφέροντας γραμμικό χρόνο O(n) στα ήδη ταξινομημένα σύνολα και O(n log n) στη χειρότερη περίπτωση.",
        "funFacts": [
            "Υιοθετήθηκε αργότερα ως ο επίσημος προεπιλεγμένος αλγόριθμος ταξινόμησης πινάκων αντικειμένων στη Java SE 7 και στο λειτουργικό Android.",
            "Το 2015, ερευνητές χρησιμοποίησαν τυπική επαλήθευση (formal verification) και ανακάλυψαν ένα λεπτό bug υπερχείλισης στοίβας που υπήρχε κρυμμένο στον κώδικα του Timsort για πάνω από μια δεκαετία."
        ],
        "source": "https://el.wikipedia.org/wiki/Timsort",
        "tags": ["technology", "algorithms", "sorting", "python"]
    },
    {
        "id": "tech_hard_221",
        "text": "Ποιος βέλτιστος αλγόριθμος συμπίεσης δεδομένων χωρίς απώλειες αναπτύχθηκε από τον David Huffman το 1952 ως εργασία εξαμήνου στο μάθημα του Robert Fano στο MIT;",
        "correct": "Κωδικοποίηση Χάφμαν (Huffman Coding)",
        "distractors": ["Αριθμητική κωδικοποίηση", "Κωδικοποίηση Golomb", "Κωδικοποίηση Shannon-Fano"],
        "explanation": "Η κωδικοποίηση Huffman κατασκευάζει ένα δυαδικό δέντρο ελαχίστου πλεονασμού, αποδίδοντας συντομότερους δυαδικούς κωδικούς (λιγότερα bits) στους χαρακτήρες που εμφανίζονται πιο συχνά.",
        "funFacts": [
            "Ο David Huffman ανακάλυψε τον αλγόριθμο λίγο πριν εγκαταλείψει την προσπάθεια και παραδοθεί στον καθηγητή του, καταφέρνοντας να ξεπεράσει τον ίδιο τον καθηγητή του Robert Fano και τον Claude Shannon!",
            "Χρησιμοποιείται ως το τελικό βήμα συμπίεσης σε πανταχού παρόντα πρότυπα όπως το JPEG, το MP3 και το DEFLATE (ZIP/GZIP)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%89%CE%B4%CE%B9%CE%BA%CE%BF%CF%80%CE%BF%CE%AF%CE%B7%CF%83%CE%B7_%CE%A7%CE%AC%CF%86%CE%BC%CE%B1%CE%BD",
        "tags": ["technology", "compression", "algorithms", "huffman"]
    },
    {
        "id": "tech_hard_222",
        "text": "Ποιος αλγόριθμος συμπίεσης λεξικού δημοσιεύθηκε από τους Terry Welch, Abraham Lempel και Jacob Ziv το 1984, αποτελώντας τη βάση για τη μορφή εικόνας GIF και την εντολή compress του Unix;",
        "correct": "LZW (Lempel-Ziv-Welch)",
        "distractors": ["LZ77", "LZMA", "Brotli"],
        "explanation": "Ο LZW διαβάζει τα δεδομένα εισόδου και δημιουργεί δυναμικά ένα λεξικό επαναλαμβανόμενων συμβολοσειρών κατά τη διάρκεια της σάρωσης, αντικαθιστώντας τις ακολουθίες με σύντομους δείκτες κώδικα σταθερού μεγέθους.",
        "funFacts": [
            "Η εταιρεία Unisys, η οποία κατείχε το δίπλωμα ευρεσιτεχνίας για τον LZW, απαίτησε αιφνιδίως δικαιώματα εκμετάλλευσης το 1994 από προγραμματιστές λογισμικού που υποστήριζαν εικόνες GIF.",
            "Αυτός ο 'φόρος στο GIF' οδήγησε την κοινότητα ανοιχτού κώδικα στη δημιουργία της νέας, ανώτερης και ελεύθερης από πατέντες μορφής PNG (Portable Network Graphics)."
        ],
        "source": "https://el.wikipedia.org/wiki/LZW",
        "tags": ["technology", "compression", "lzw", "algorithms"]
    },
    {
        "id": "tech_hard_223",
        "text": "Ποιο μαθηματικό πρόβλημα της θεωρίας αριθμών αποτελεί τη βάση της ασφάλειας του πρωτοκόλλου ανταλλαγής κλειδιών Diffie-Hellman;",
        "correct": "Το πρόβλημα του διακριτού λογαρίθμου (Discrete Logarithm Problem) σε πεπερασμένα σώματα",
        "distractors": ["Η παραγοντοποίηση πρώτων αριθμών", "Το πρόβλημα του σακιδίου (Knapsack problem)", "Ο υπολογισμός των ριζών πολυωνύμων Riemann"],
        "explanation": "Ενώ ο υπολογισμός της modular ύψωσης σε δύναμη g^a mod p είναι εξαιρετικά γρήγορος, η αντίστροφη εύρεση του εκθέτη 'a' όταν είναι γνωστό μόνο το αποτέλεσμα είναι υπολογιστικά ανεπίλυτη για τεράστιους πρώτους αριθμούς.",
        "funFacts": [
            "Δημοσιεύθηκε το 1976 από τους Whitfield Diffie και Martin Hellman, ανοίγοντας την εποχή της κρυπτογραφίας δημόσιου κλειδιού.",
            "Η παραλλαγή του πάνω σε ελλειπτικές καμπύλες ονομάζεται ECDH (Elliptic Curve Diffie-Hellman) και χρησιμοποιείται σήμερα σε σχεδόν κάθε ασφαλή σύνδεση TLS 1.3."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BD%CF%84%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE_%CE%BA%CE%BB%CE%B5%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD_%CE%9D%CF%84%CE%AF%CF%86%CE%B9-%CE%A7%CE%AD%CE%BB%CE%BC%CE%B1%CE%BD",
        "tags": ["technology", "cryptography", "diffie_hellman", "math"]
    },
    {
        "id": "tech_hard_224",
        "text": "Ποια συγκεκριμένη ελλειπτική καμπύλη Koblitz (τυποποιημένη από το SECG) επέλεξε ο Satoshi Nakamoto για τις ψηφιακές υπογραφές ECDSA στο δίκτυο του Bitcoin;",
        "correct": "secp256k1",
        "distractors": ["P-256 (secp256r1)", "Curve25519", "Ed448"],
        "explanation": "Η καμπύλη secp256k1 ορίζεται από την εξίσωση y^2 = x^3 + 7 πάνω σε πεπερασμένο σώμα. Ο Nakamoto την προτίμησε επειδή, σε αντίθεση με την καμπύλη P-256 του NIST, οι σταθερές της δεν είχαν επιλεγεί με αδιαφανή τρόπο από κυβερνητικές υπηρεσίες των ΗΠΑ.",
        "funFacts": [
            "Προσφέρει επίπεδο ασφάλειας περίπου 128 bits, ισοδύναμο με κλειδί RSA μεγέθους 3.072 bits, αλλά με μέγεθος κλειδιού μόλις 256 bits (32 bytes).",
            "Η δομή της επιτρέπει αποδοτικότερους υπολογισμούς σημείων χάρη σε ειδικούς ενδομορφισμούς (GLV endomorphism)."
        ],
        "source": "https://en.wikipedia.org/wiki/Secp256k1",
        "tags": ["technology", "cryptography", "bitcoin", "ecc"]
    },
    {
        "id": "tech_hard_225",
        "text": "Ποιο κρυπτογραφικό πρωτόκολλο που προτάθηκε από τους Shafi Goldwasser, Silvio Micali και Charles Rackoff το 1985 επιτρέπει σε έναν αποδείκτη να πείσει έναν επαληθευτή ότι γνωρίζει ένα μυστικό χωρίς να αποκαλύψει καμία απολύτως πληροφορία για το ίδιο το μυστικό;",
        "correct": "Απόδειξη Μηδενικής Γνώσης (Zero-Knowledge Proof - ZKP)",
        "distractors": ["Ψηφιακή Υπογραφή Schnorr", "Τυφλή Υπογραφή Chaum", "Μυστικός Διαμοιρασμός Shamir"],
        "explanation": "Μια απόδειξη ZKP ικανοποιεί τρεις αυστηρές ιδιότητες: Πληρότητα (Completeness), Ορθότητα (Soundness) και Μηδενική Γνώση (Zero-Knowledge).",
        "funFacts": [
            "Οι δημιουργοί του τιμήθηκαν με το Βραβείο Turing το 2012 για τη θεμελίωση της σύγχρονης θεωρίας πολυπλοκότητας και κρυπτογραφίας.",
            "Σύγχρονες συμπαγείς παραλλαγές μη αλληλεπιδραστικών αποδείξεων (zk-SNARKs και zk-STARKs) χρησιμοποιούνται ευρύτατα σε κρυπτονομίσματα ιδιωτικότητας (Zcash) και σε Layer 2 rollups του Ethereum."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CF%80%CF%8C%CE%B4%CE%B5%CE%B9%CE%BE%CE%B7_%CE%BC%CE%B7%CE%B4%CE%B5%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%B3%CE%BD%CF%8E%CF%83%CE%B7%CF%82",
        "tags": ["technology", "cryptography", "zkp", "zero_knowledge"]
    },
    {
        "id": "tech_hard_226",
        "text": "Ποια δενδρική δομή κατακερματισμού που κατοχυρώθηκε από τον Ralph Merkle το 1979 επιτρέπει την αποτελεσματική και ασφαλή επαλήθευση μεγάλων συνόλων δεδομένων χρησιμοποιώντας κρυπτογραφικά hashes;",
        "correct": "Δέντρο Μερκλ (Merkle Tree / Hash Tree)",
        "distractors": ["Δέντρο Radix", "Δέντρο Fenwick", "Δέντρο Van Emde Boas"],
        "explanation": "Σε ένα Merkle Tree, κάθε φύλλο είναι το hash ενός μπλοκ δεδομένων, και κάθε εσωτερικός κόμβος είναι το hash των δύο παιδιών του, καταλήγοντας σε μια ενιαία ριζική τιμή κατακερματισμού (Merkle Root).",
        "funFacts": [
            "Επιτρέπει την επαλήθευση ότι μια συναλλαγή ανήκει σε ένα μπλοκ του Bitcoin εξετάζοντας μόλις O(log n) hashes μέσω ενός 'Merkle Proof' (SPV clients).",
            "Χρησιμοποιείται επίσης στο σύστημα ελέγχου εκδόσεων Git, στο σύστημα αρχείων ZFS και στο πρωτόκολλο BitTorrent."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BD%CF%84%CF%81%CE%BF_%CE%9C%CE%AD%CF%81%CE%BA%CE%BB",
        "tags": ["technology", "cryptography", "merkle_tree", "blockchain"]
    },
    {
        "id": "tech_hard_227",
        "text": "Στο κλασικό πρόβλημα των Βυζαντινών Στρατηγών (Byzantine Fault Tolerance) των Lamport, Shostak και Pease (1982), ποιο είναι το ελάχιστο ποσοστό τίμιων κόμβων που απαιτείται για την επίτευξη συναίνεσης όταν υπάρχουν f προδότες;",
        "correct": "Απαιτούνται αυστηρά τουλάχιστον 3f + 1 συνολικοί κόμβοι (δηλαδή πάνω από τα 2/3 να είναι τίμιοι)",
        "distractors": ["Απαιτούνται τουλάχιστον 2f + 1 κόμβοι (απλή πλειοψηφία)", "Απαιτούνται τουλάχιστον f + 1 κόμβοι", "Απαιτούνται τουλάχιστον 4f + 1 κόμβοι"],
        "explanation": "Αν υπάρχουν f κόμβοι που μπορούν να στέλνουν αντικρουόμενα ή κακόβουλα μηνύματα, ένα ασύγχρονο κατανεμημένο σύστημα χρειάζεται τουλάχιστον 2f+1 τίμιους κόμβους (συνολικά 3f+1) για να εξασφαλίσει ασφάλεια και ζωντάνια (safety and liveness).",
        "funFacts": [
            "Ο Satoshi Nakamoto επέλυσε το πρόβλημα των Βυζαντινών Στρατηγών σε ανοιχτά παγκόσμια δίκτυα χωρίς προκαθορισμένους κόμβους εισάγοντας τον μηχανισμό Proof-of-Work (Nakamoto Consensus).",
            "Κλασικοί αλγόριθμοι BFT περιλαμβάνουν τον PBFT (Practical Byzantine Fault Tolerance) του Miguel Castro και της Barbara Liskov το 1999."
        ],
        "source": "https://en.wikipedia.org/wiki/Byzantine_fault",
        "tags": ["technology", "distributed_systems", "bft", "consensus"]
    },
    {
        "id": "tech_hard_228",
        "text": "Ποιος σύγχρονος αλγόριθμος κατανεμημένης συναίνεσης σχεδιάστηκε από τους Diego Ongaro και John Ousterhout στο Πανεπιστήμιο Στάνφορντ το 2014 ειδικά ως μια πιο κατανοητή εναλλακτική λύση του Paxos;",
        "correct": "Raft",
        "distractors": ["Paxos", "Zab", "Viewstamped Replication"],
        "explanation": "Το Raft διασπά το πρόβλημα της συναίνεσης σε διακριτά υποπροβλήματα: εκλογή ηγέτη (Leader Election), αναπαραγωγή ημερολογίου (Log Replication) και ασφάλεια, κάνοντας τον σχεδιασμό και την υλοποίησή του πολύ πιο προσιτή.",
        "funFacts": [
            "Χρησιμοποιείται από κρίσιμα κατανεμημένα συστήματα υποδομής όπως το etcd (η καρδιά του Kubernetes), το Consul και το CockroachDB.",
            "Κάθε κόμβος στο Raft βρίσκεται σε μία από τρεις καταστάσεις: Leader, Follower ή Candidate."
        ],
        "source": "https://en.wikipedia.org/wiki/Raft_(algorithm)",
        "tags": ["technology", "distributed_systems", "raft", "consensus"]
    },
    {
        "id": "tech_hard_229",
        "text": "Ποιο μαθηματικό εργαλείο πρότεινε ο Leslie Lamport το 1978 για τον καθορισμό της αιτιώδους διάταξης γεγονότων (happened-before relation) σε κατανεμημένα συστήματα χωρίς συντονισμένα φυσικά ρολόγια;",
        "correct": "Λογικά ρολόγια Λάμπορτ (Lamport Timestamps)",
        "distractors": ["Ατομικά ρολόγια GPS", "Εικονικά ρολόγια PTP", "Κρυπτογραφικές σφραγίδες χρόνου"],
        "explanation": "Τα ρολόγια Lamport αποδίδουν έναν μονοτονικά αυξανόμενο ακέραιο αριθμό σε κάθε γεγονός. Αν το γεγονός Α προκαλεί το γεγονός Β, τότε C(A) < C(B), επιτρέποντας μερική διάταξη γεγονότων στο σύστημα.",
        "funFacts": [
            "Η ιστορική δημοσίευση του Lamport 'Time, Clocks, and the Ordering of Events in a Distributed System' είναι μία από τις πιο αναφερόμενες εργασίες σε ολόκληρη την ιστορία της επιστήμης υπολογιστών.",
            "Η εξέλιξή τους, τα διανυσματικά ρολόγια (Vector Clocks), επιτρέπει τον ακριβή εντοπισμό ταυτόχρονων γεγονότων που δεν έχουν αιτιώδη σχέση μεταξύ τους."
        ],
        "source": "https://en.wikipedia.org/wiki/Lamport_timestamp",
        "tags": ["technology", "distributed_systems", "lamport", "clocks"]
    },
    {
        "id": "tech_hard_230",
        "text": "Ποια τεχνική ελέγχου ταυτοχρονισμού χρησιμοποιείται σε σύγχρονες μηχανές βάσεων δεδομένων (όπως PostgreSQL και MySQL InnoDB), όπου κάθε συναλλαγή βλέπει ένα συνεπές στιγμιότυπο των δεδομένων χωρίς οι αναγνώστες να μπλοκάρουν τους συγγραφείς;",
        "correct": "MVCC (Multiversion Concurrency Control)",
        "distractors": ["Strict Two-Phase Locking (S2PL)", "Timestamp Ordering", "Optimistic Locking"],
        "explanation": "Στο MVCC, όταν μια συναλλαγή τροποποιεί μια γραμμή, η βάση δεδομένων δεν αντικαθιστά τα δεδομένα αλλά δημιουργεί μια νέα έκδοση της γραμμής με χρονική σήμανση (xmin/xmax), επιτρέποντας ταυτόχρονες αναγνώσεις χωρίς κλειδώματα.",
        "funFacts": [
            "Επειδή οι παλιές εκδόσεις γραμμών (dead tuples) συσσωρεύονται με τον χρόνο, η PostgreSQL απαιτεί τη διεργασία 'VACUUM' για να καθαρίζει τον άχρηστο χώρο.",
            "Προτάθηκε αρχικά στη διδακτορική διατριβή του David P. Reed στο MIT το 1978."
        ],
        "source": "https://en.wikipedia.org/wiki/Multiversion_concurrency_control",
        "tags": ["technology", "databases", "mvcc", "concurrency"]
    },
    {
        "id": "tech_hard_231",
        "text": "Ποια δομή δεδομένων αποθήκευσης δίσκου που σχεδιάστηκε από τον Patrick O'Neil το 1996 χρησιμοποιείται από βάσεις δεδομένων NoSQL (όπως RocksDB, Cassandra και Bigtable) για μέγιστη ταχύτητα σειριακών εγγραφών;",
        "correct": "LSM-Tree (Log-Structured Merge-tree)",
        "distractors": ["B-Tree", "R-Tree", "Radix Tree"],
        "explanation": "Το LSM-Tree συγκεντρώνει όλες τις νέες εγγραφές σε μια ταξινομημένη δομή μνήμης RAM (MemTable) και στη συνέχεια τις αδειάζει σειριακά στον δίσκο ως αμετάβλητα αρχεία SSTables, εκτελώντας περιοδική συγχώνευση (compaction).",
        "funFacts": [
            "Αποφεύγει τις τυχαίες εγγραφές (random writes) που είναι καταστροφικές για τους μηχανικούς δίσκους και φθείρουν τα κελιά των SSDs.",
            "Για να αποφύγει την αργή αναζήτηση ανύπαρκτων κλειδιών σε πολλαπλά SSTables, συνδυάζεται υποχρεωτικά με Φίλτρα Bloom (Bloom Filters) στη μνήμη."
        ],
        "source": "https://en.wikipedia.org/wiki/Log-structured_merge-tree",
        "tags": ["technology", "databases", "lsm_tree", "storage"]
    },
    {
        "id": "tech_hard_232",
        "text": "Ποια πιθανοτική δομή δεδομένων εξαιρετικά αποδοτικής μνήμης επινοήθηκε από τον Burton Howard Bloom το 1970, η οποία μπορεί να εγγυηθεί με βεβαιότητα αν ένα στοιχείο ΔΕΝ ανήκει σε ένα σύνολο (μηδέν ψευδώς αρνητικά);",
        "correct": "Φίλτρο Μπλουμ (Bloom Filter)",
        "distractors": ["Count-Min Sketch", "Cuckoo Filter", "HyperLogLog"],
        "explanation": "Το Bloom Filter χρησιμοποιεί έναν πίνακα bits και k ανεξάρτητες συναρτήσεις κατακερματισμού: μπορεί να έχει ψευδώς θετικά αποτελέσματα (μπορεί να πει ότι ένα στοιχείο υπάρχει ενώ δεν υπάρχει), αλλά ποτέ ψευδώς αρνητικά.",
        "funFacts": [
            "Χρησιμοποιείται από προγράμματα περιήγησης (όπως το Google Chrome) για άμεσο τοπικό έλεγχο αν ένα URL είναι κακόβουλο πριν στείλει ερώτημα στους κεντρικούς servers.",
            "Εξοικονομεί τεράστιο χρόνο εισόδου/εξόδου σε βάσεις δεδομένων ελέγχοντας αν ένα κλειδί λείπει από έναν δίσκο χωρίς να διαβάσει το αρχείο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A6%CE%AF%CE%BB%CF%84%CF%81%CE%BF_%CE%9C%CF%80%CE%BB%CE%BF%CF%85%CE%BC",
        "tags": ["technology", "algorithms", "data_structures", "bloom_filter"]
    },
    {
        "id": "tech_hard_233",
        "text": "Ποιος πιθανοτικός αλγόριθμος που αναπτύχθηκε από τον Philippe Flajolet το 2007 μπορεί να εκτιμήσει την πληθικότητα (τον αριθμό μοναδικών στοιχείων) δισεκατομμυρίων εγγραφών με σφάλμα κάτω του 1% χρησιμοποιώντας μόλις 1,5 KB μνήμης;",
        "correct": "HyperLogLog",
        "distractors": ["LogLog", "MinHash", "SimHash"],
        "explanation": "Το HyperLogLog παρατηρεί τον μέγιστο αριθμό συνεχόμενων μηδενικών στην αρχή των τιμών hash των στοιχείων, εκμεταλλευόμενο το γεγονός ότι μια ακολουθία k μηδενικών εμφανίζεται στατιστικά μία φορά κάθε 2^k στοιχεία.",
        "funFacts": [
            "Είναι ενσωματωμένο ως εγγενής τύπος δεδομένων στο Redis (εντολή PFCOUNT).",
            "Επιτρέπει σε γίγαντες του διαδικτύου να μετρούν μοναδικούς επισκέπτες σε πραγματικό χρόνο χωρίς να αποθηκεύουν τεράστιες λίστες από διευθύνσεις IP ή αναγνωριστικά χρηστών."
        ],
        "source": "https://en.wikipedia.org/wiki/HyperLogLog",
        "tags": ["technology", "algorithms", "hyperloglog", "big_data"]
    },
    {
        "id": "tech_hard_234",
        "text": "Ποια τεχνική κατακερματισμού (Consistent Hashing) που επινοήθηκε στο MIT από τον David Karger και τους συνεργάτες του το 1997 οργανώνει τους διακομιστές σε έναν λογικό κύκλο, ελαχιστοποιώντας την ανακατανομή κλειδιών όταν προστίθεται ή αφαιρείται ένας κόμβος;",
        "correct": "Συνεπής Κατακερματισμός (Consistent Hashing)",
        "distractors": ["Linear Hashing", "Cuckoo Hashing", "Rendezvous Hashing"],
        "explanation": "Σε αντίθεση με την παραδοσιακή μέθοδο hash(k) mod N (όπου οποιαδήποτε αλλαγή στο N απαιτεί μετακίνηση σχεδόν του 100% των δεδομένων), ο συνεπής κατακερματισμός απαιτεί τη μετακίνηση μόλις K/N κλειδιών κατά μέσο όρο.",
        "funFacts": [
            "Αποτέλεσε τη βάση για τη δημιουργία της Akamai Technologies και του παγκόσμιου δικτύου CDN της.",
            "Χρησιμοποιείται σε κατανεμημένες βάσεις δεδομένων NoSQL όπως το Amazon DynamoDB και το Apache Cassandra."
        ],
        "source": "https://en.wikipedia.org/wiki/Consistent_hashing",
        "tags": ["technology", "distributed_systems", "algorithms", "consistent_hashing"]
    },
    {
        "id": "tech_hard_235",
        "text": "Ποιος κλασικός αλγόριθμος υλικού που σχεδιάστηκε από τον Robert Tomasulo στην IBM το 1967 επιτρέπει την εκτέλεση εντολών εκτός σειράς (Out-of-Order Execution) χρησιμοποιώντας σταθμούς κράτησης (reservation stations) και μετονομασία καταχωρητών;",
        "correct": "Αλγόριθμος Τομασούλο (Tomasulo's Algorithm)",
        "distractors": ["Scoreboarding", "Αλγόριθμος Petri", "Αλγόριθμος Viterbi"],
        "explanation": "Ο αλγόριθμος του Tomasulo εξαλείφει τις ψευδείς εξαρτήσεις δεδομένων WAR (Write After Read) και WAW (Write After Write) αντιστοιχίζοντας δυναμικά τους λογικούς καταχωρητές της αρχιτεκτονικής σε φυσικούς σταθμούς κράτησης.",
        "funFacts": [
            "Υλοποιήθηκε για πρώτη φορά στη μονάδα κινητής υποδιαστολής του ιστορικού υπερυπολογιστή IBM System/360 Model 91.",
            "Αποτελεί τον πυρήνα της λειτουργίας όλων των σύγχρονων επεξεργαστών υψηλής απόδοσης Intel Core, AMD Zen και Apple Silicon."
        ],
        "source": "https://en.wikipedia.org/wiki/Tomasulo%27s_algorithm",
        "tags": ["technology", "hardware", "cpu_microarchitecture", "tomasulo"]
    },
    {
        "id": "tech_hard_236",
        "text": "Ποιο πρωτόκολλο συνοχής κρυφής μνήμης (Cache Coherence) χρησιμοποιείται ευρύτατα σε πολυπύρηνους επεξεργαστές, ορίζοντας τέσσερις πιθανές καταστάσεις για κάθε γραμμή cache: Modified, Exclusive, Shared και Invalid;",
        "correct": "Πρωτόκολλο MESI",
        "distractors": ["Πρωτόκολλο MOESI", "Πρωτόκολλο Dragon", "Πρωτόκολλο Firefly"],
        "explanation": "Το πρωτόκολλο MESI (γνωστό και ως πρωτόκολλο Illinois) διασφαλίζει ότι όλοι οι πυρήνες βλέπουν πάντα μια συνεπή εικόνα της μνήμης RAM, υποκλέπτοντας (snooping) τις συναλλαγές στον κοινό δίαυλο επικοινωνίας.",
        "funFacts": [
            "Στην κατάσταση Modified, η γραμμή cache περιέχει νεότερα δεδομένα που δεν έχουν γραφτεί ακόμα στην κύρια μνήμη RAM (dirty cache line).",
            "Η AMD χρησιμοποιεί την επέκταση MOESI, προσθέτοντας την κατάσταση 'Owner' για απευθείας διαμοιρασμό τροποποιημένων δεδομένων μεταξύ πυρήνων χωρίς εγγραφή στη RAM."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CF%89%CF%84%CF%8C%CE%BA%CE%BF%CE%BB%CE%BB%CE%BF_MESI",
        "tags": ["technology", "hardware", "cpu", "cache_coherence"]
    },
    {
        "id": "tech_hard_237",
        "text": "Ποια πρωτοποριακή επίθεση υλικού σε μνήμες DRAM αποκαλύφθηκε από τον Yoongu Kim και ερευνητές του CMU το 2014, όπου η ταχύτατη επανειλημμένη πρόσβαση σε μία γραμμή μνήμης προκαλεί ηλεκτρομαγνητική διαρροή και αναστροφή bits (bit-flips) σε γειτονικές γραμμές;",
        "correct": "Rowhammer",
        "distractors": ["Spectre", "Meltdown", "VoltJockey"],
        "explanation": "Η επίθεση Rowhammer εκμεταλλεύεται τη φυσική εγγύτητα των μικροσκοπικών πυκνωτών στις σύγχρονες πυκνές μνήμες DRAM: η επαναλαμβανόμενη ενεργοποίηση μιας σειράς ('σφυρηλάτηση') διαρρέει ηλεκτρικό φορτίο, αλλάζοντας κρυφά bits σε γειτονικές θέσεις μνήμης χωρίς εξουσιοδότηση.",
        "funFacts": [
            "Απέδειξε ότι ένα φυσικό ελάττωμα πυριτίου μπορεί να χρησιμοποιηθεί από απλό λογισμικό (ακόμη και μέσω JavaScript σε browser!) για απόκτηση πλήρων προνομίων root στο λειτουργικό σύστημα.",
            "Οδήγησε τους κατασκευαστές στην ανάπτυξη μηχανισμών άμυνας όπως το TRR (Target Row Refresh)."
        ],
        "source": "https://en.wikipedia.org/wiki/Row_hammer",
        "tags": ["technology", "security", "rowhammer", "hardware"]
    },
    {
        "id": "tech_hard_238",
        "text": "Πώς ονομάζεται η θεμελιώδης δομή δεδομένων ενός συστήματος αρχείων Unix/Linux που αποθηκεύει όλα τα μεταδεδομένα ενός αρχείου (μέγεθος, δικαιώματα, ιδιοκτήτη, δείκτες σε blocks δίσκου) ΕΚΤΟΣ από το ίδιο το όνομα του αρχείου;",
        "correct": "Κόμβος ευρετηρίου (inode)",
        "distractors": ["Superblock", "Directory Entry (dentry)", "File Descriptor"],
        "explanation": "Στα λειτουργικά συστήματα Unix, το όνομα ενός αρχείου δεν αποθηκεύεται μέσα στο inode, αλλά αποτελεί απλώς μια καταχώριση σε έναν κατάλογο που συσχετίζει ένα όνομα κειμένου με τον αντίστοιχο αριθμό inode.",
        "funFacts": [
            "Γι' αυτό ακριβώς υπάρχουν τα 'σκληρά δεσμά' (hard links): πολλαπλά διαφορετικά ονόματα αρχείων σε διαφορετικούς φακέλους μπορούν να δείχνουν στον ίδιο ακριβώς αριθμό inode.",
            "Αν εξαντληθούν οι διαθέσιμοι κόμβοι inodes σε έναν δίσκο, δεν μπορείτε να δημιουργήσετε νέα αρχεία, ακόμη κι αν υπάρχουν εκατοντάδες Gigabytes ελεύθερου χώρου!"
        ],
        "source": "https://el.wikipedia.org/wiki/Inode",
        "tags": ["technology", "linux", "unix", "file_systems"]
    },
    {
        "id": "tech_hard_239",
        "text": "Ποια πρωτοποριακή κλήση συστήματος του πυρήνα Linux εισήχθη στην έκδοση 2.5.44 για κλιμακούμενη πολυπλεξία εισόδου/εξόδου (I/O multiplexing), επιτυγχάνοντας πολυπλοκότητα O(1) ανεξάρτητα από τον αριθμό των παρακολουθούμενων περιγραφέων αρχείων;",
        "correct": "epoll",
        "distractors": ["select", "poll", "kqueue"],
        "explanation": "Ενώ οι παλαιότερες κλήσεις select και poll απαιτούσαν γραμμική σάρωση O(n) όλων των file descriptors σε κάθε κύκλο, το epoll ειδοποιεί άμεσα μόνο για τους descriptors που είχαν πραγματική δραστηριότητα μέσω δομών κόκκινων-μαύρων δέντρων και λιστών έτοιμων συμβάντων.",
        "funFacts": [
            "Αποτέλεσε το θεμέλιο της εκρηκτικής απόδοσης σύγχρονων servers όπως το Nginx και το Node.js.",
            "Το αντίστοιχο εξαιρετικά αποδοτικό υποσύστημα στα λειτουργικά συστήματα BSD και macOS ονομάζεται kqueue."
        ],
        "source": "https://en.wikipedia.org/wiki/Epoll",
        "tags": ["technology", "linux", "kernel", "epoll"]
    },
    {
        "id": "tech_hard_240",
        "text": "Ποια επαναστατική τεχνολογία του πυρήνα Linux επιτρέπει την ασφαλή εκτέλεση προσαρμοσμένου bytecode μέσα στον χώρο του πυρήνα (kernel space) χωρίς τροποποίηση του πηγαίου κώδικα ή φόρτωση εξωτερικών kernel modules;",
        "correct": "eBPF (Extended Berkeley Packet Filter)",
        "distractors": ["KVM", "AppArmor", "SELinux"],
        "explanation": "Το eBPF λειτουργεί σαν μια 'εικονική μηχανή JavaScript μέσα στον πυρήνα', επαληθεύοντας στατικά την ασφάλεια του κώδικα (verifier) πριν τον εκτελέσει με JIT μεταγλώττιση για παρακολούθηση δικτύου, ασφάλεια και ανάλυση επιδόσεων.",
        "funFacts": [
            "Χρησιμοποιείται από κολοσσούς όπως η Meta, το Netflix και η Cloudflare για δρομολόγηση πακέτων επιπέδου Layer 4 και προστασία από επιθέσεις DDoS.",
            "Το εργαλείο δικτύωσης Cilium για το Kubernetes βασίζεται εξ ολοκλήρου στο eBPF για να παρακάμψει το βαρύ υποσύστημα iptables του Linux."
        ],
        "source": "https://en.wikipedia.org/wiki/EBPF",
        "tags": ["technology", "linux", "ebpf", "kernel"]
    },
    {
        "id": "tech_hard_241",
        "text": "Ποιο χαρακτηριστικό του πυρήνα Linux που αναπτύχθηκε αρχικά από μηχανικούς της Google (Paul Menage και Rohit Seth) το 2007 επιτρέπει τον περιορισμό, την κατανομή και την απομόνωση πόρων (CPU, μνήμη, δίσκος) σε ομάδες διεργασιών;",
        "correct": "cgroups (Control Groups)",
        "distractors": ["chroot", "seccomp", "capabilities"],
        "explanation": "Τα cgroups αποτελούν, μαζί με τα Linux Namespaces, τα δύο θεμελιώδη δομικά στοιχεία του πυρήνα πάνω στα οποία χτίστηκε ολόκληρη η σύγχρονη επανάσταση των containers και του Docker.",
        "funFacts": [
            "Αρχικά ονομαζόταν 'Process Containers' αλλά μετονομάστηκε σε 'Control Groups' για να αποφευχθεί η σύγχυση με άλλες έννοιες virtualization.",
            "Η έκδοση cgroups v2 ενοποίησε την ιεραρχία των ελεγκτών σε μια ενιαία καθαρή δομή δέντρου."
        ],
        "source": "https://el.wikipedia.org/wiki/Cgroups",
        "tags": ["technology", "linux", "cgroups", "containers"]
    },
    {
        "id": "tech_hard_242",
        "text": "Ποιος μηχανισμός ασφαλείας του πυρήνα Linux (Secure Computing Mode) περιορίζει τις κλήσεις συστήματος (system calls) που επιτρέπεται να εκτελέσει μια διεργασία, ελαχιστοποιώντας την επιφάνεια επίθεσης;",
        "correct": "seccomp (ή seccomp-bpf)",
        "distractors": ["AppArmor", "grsecurity", "chroot"],
        "explanation": "Μέσω φίλτρων BPF, το seccomp επιτρέπει σε προγράμματα (όπως browsers και κοντέινερ Docker) να απομονώνονται σε αυστηρά sandboxes: αν η διεργασία επιχειρήσει να καλέσει μια μη εγκεκριμένη κλήση συστήματος, ο πυρήνας τη σκοτώνει ακαριαία (SIGSYS).",
        "funFacts": [
            "Ενσωματώθηκε αρχικά στον πυρήνα Linux 2.6.12 το 2005 από τον Andrea Arcangeli για τη μίσθωση αχρησιμοποίητου χρόνου CPU.",
            "Κάθε καρτέλα περιήγησης στο Google Chrome τρέχει μέσα σε ένα αυστηρό seccomp sandbox."
        ],
        "source": "https://en.wikipedia.org/wiki/Seccomp",
        "tags": ["technology", "linux", "security", "seccomp"]
    },
    {
        "id": "tech_hard_243",
        "text": "Ποιο σύστημα κρυπτογραφικής απόδειξης ταυτότητας σε επίπεδο δικτύου επινοήθηκε από τον Ralph Merkle το 1979, χρησιμοποιώντας δέντρα Merkle για την παραγωγή ψηφιακών υπογραφών μίας χρήσης με αντοχή σε κβαντικούς υπολογιστές;",
        "correct": "Υπογραφές Merkle (Merkle Signature Scheme)",
        "distractors": ["Υπογραφές Lamport", "Υπογραφές ElGamal", "Υπογραφές Rabin"],
        "explanation": "Το σχήμα υπογραφών Merkle συνδυάζει πολλαπλές υπογραφές μίας χρήσης (One-Time Signatures όπως οι Lamport/Winternitz) σε ένα δέντρο Merkle, αποτελώντας τη βάση για σύγχρονα μετα-κβαντικά πρότυπα ψηφιακών υπογραφών (SPHINCS+ και XMSS).",
        "funFacts": [
            "Βασίζεται αποκλειστικά στην ασφάλεια κρυπτογραφικών συναρτήσεων κατακερματισμού (hash-based cryptography) και δεν επηρεάζεται από τον κβαντικό αλγόριθμο του Shor.",
            "Κάθε κλειδί μπορεί να χρησιμοποιηθεί μόνο για έναν προκαθορισμένο μέγιστο αριθμό υπογραφών (stateful signature scheme)."
        ],
        "source": "https://en.wikipedia.org/wiki/Merkle_signature_scheme",
        "tags": ["technology", "cryptography", "quantum_resistant", "merkle"]
    },
    {
        "id": "tech_hard_244",
        "text": "Ποιος κβαντικός αλγόριθμος που διατυπώθηκε από τον Peter Shor το 1994 απέδειξε ότι ένας επαρκώς μεγάλος κβαντικός υπολογιστής μπορεί να παραγοντοποιήσει ακεραίους σε πολυωνυμικό χρόνο, καταστρέφοντας την ασφάλεια του RSA και του ECC;",
        "correct": "Αλγόριθμος του Shor",
        "distractors": ["Αλγόριθμος του Grover", "Αλγόριθμος Deutsch-Jozsa", "Αλγόριθμος Simon"],
        "explanation": "Ο αλγόριθμος του Shor εκμεταλλεύεται τον κβαντικό μετασχηματισμό Fourier (QFT) για να επιλύσει το πρόβλημα εύρεσης περιόδου συνάρτησης σε χρόνο O((log N)^3), σπάζοντας την κρυπτογραφία δημοσίου κλειδιού που προστατεύει σήμερα το παγκόσμιο διαδίκτυο.",
        "funFacts": [
            "Οδήγησε το NIST στη διεξαγωγή ενός πολυετούς παγκόσμιου διαγωνισμού για την τυποποίηση αλγορίθμων Μετα-Κβαντικής Κρυπτογραφίας (Post-Quantum Cryptography - PQC).",
            "Αντίθετα, ο αλγόριθμος του Grover προσφέρει τετραγωνική μόνο επιτάχυνση στην αναζήτηση, μειώνοντας την ασφάλεια του AES-256 στο ισοδύναμο των 128 bits, το οποίο παραμένει απόλυτα ασφαλές."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%BF%CF%81",
        "tags": ["technology", "quantum_computing", "cryptography", "shor_algorithm"]
    },
    {
        "id": "tech_hard_245",
        "text": "Ποια μαθηματική οικογένεια προβλημάτων πλεγμάτων (Lattice-based cryptography), όπως το Learning With Errors (LWE), αποτελεί τη βάση των νέων προτύπων Μετα-Κβαντικής Κρυπτογραφίας (ML-KEM / Kyber);",
        "correct": "Κρυπτογραφία βασισμένη σε πλέγματα (Lattice-based Cryptography)",
        "distractors": ["Κρυπτογραφία ισογενειών (Isogeny-based)", "Πολυμεταβλητή κρυπτογραφία", "Κρυπτογραφία κωδίκων (Code-based)"],
        "explanation": "Το πρόβλημα LWE (Εκμάθηση με Σφάλματα) που πρότεινε ο Oded Regev το 2005 θεωρείται εξαιρετικά δύσκολο τόσο για κλασικούς όσο και για κβαντικούς υπολογιστές, αποτελώντας τη ραχοκοκαλιά του προτύπου ML-KEM (CRYSTALS-Kyber) του NIST.",
        "funFacts": [
            "Επιτρέπει επίσης την υλοποίηση της Πλήρως Ομομορφικής Κρυπτογράφησης (Fully Homomorphic Encryption - FHE).",
            "Η FHE επιτρέπει σε διακομιστές στο cloud να εκτελούν μαθηματικούς υπολογισμούς πάνω σε κρυπτογραφημένα δεδομένα χωρίς να τα αποκρυπτογραφήσουν ποτέ!"
        ],
        "source": "https://en.wikipedia.org/wiki/Lattice-based_cryptography",
        "tags": ["technology", "cryptography", "post_quantum", "lattices"]
    },
    {
        "id": "tech_hard_246",
        "text": "Ποιο πρωτόκολλο επικοινωνίας δικτύου επιπέδου μεταφοράς που αναπτύχθηκε αρχικά από τη Google και τυποποιήθηκε από την IETF ως RFC 9000 αποτελεί τη βάση του HTTP/3 πάνω από UDP;",
        "correct": "QUIC",
        "distractors": ["SCTP", "DCCP", "RSVP"],
        "explanation": "Το QUIC επιλύει το χρόνιο πρόβλημα 'Head-of-Line Blocking' του TCP ενσωματώνοντας ανεξάρτητα streams, κρυπτογράφηση TLS 1.3 και ταχύτατη αποκατάσταση συνδέσεων σε ένα ενιαίο πρωτόκολλο πάνω από πακέτα UDP.",
        "funFacts": [
            "Επιτρέπει την αλλαγή δικτύου (π.χ. από Wi-Fi σε δεδομένα κινητής 4G/5G) χωρίς να διακοπεί η λήψη του αρχείου ή η βιντεοκλήση χάρη στα Connection IDs.",
            "Σήμερα εξυπηρετεί πάνω από το 25% της συνολικής παγκόσμιας κίνησης στο διαδίκτυο."
        ],
        "source": "https://el.wikipedia.org/wiki/QUIC",
        "tags": ["technology", "networking", "quic", "http3"]
    },
    {
        "id": "tech_hard_247",
        "text": "Πώς ονομάζεται το πρόβλημα στα πρωτόκολλα ελέγχου ροής όπως το TCP, όπου ένα και μόνο χαμένο πακέτο στην αρχή μιας ουράς καθυστερεί την παράδοση όλων των επόμενων πακέτων;",
        "correct": "Εμπλοκή στην κεφαλή της γραμμής (Head-of-Line Blocking - HoL Blocking)",
        "distractors": ["Starvation", "Jitter", "Split-Brain"],
        "explanation": "Στο TCP, επειδή όλα τα δεδομένα παραδίδονται αυστηρά με τη σωστή σειρά, αν ένα πακέτο χαθεί, ολόκληρη η ροή παγώνει μέχρι να αναμεταδοθεί το χαμένο πακέτο, ακόμη κι αν όλα τα υπόλοιπα έχουν φτάσει άθικτα.",
        "funFacts": [
            "Το πρόβλημα έγινε ιδιαίτερα έντονο στο HTTP/2, όπου δεκάδες αρχεία πολυπλέκονταν πάνω σε μία μόνο σύνδεση TCP.",
            "Η αντικατάσταση του TCP από το QUIC στο HTTP/3 εξάλειψε οριστικά το HoL Blocking σε επίπεδο μεταφοράς."
        ],
        "source": "https://en.wikipedia.org/wiki/Head-of-line_blocking",
        "tags": ["technology", "networking", "tcp", "hol_blocking"]
    },
    {
        "id": "tech_hard_248",
        "text": "Ποιος πρωτοποριακός αλγόριθμος ελέγχου συμφόρησης TCP (Congestion Control) αναπτύχθηκε από μηχανικούς της Google το 2016, βασισμένος στη μέτρηση του εύρους ζώνης συμφόρησης και του ελάχιστου χρόνου RTT αντί για απώλειες πακέτων;",
        "correct": "BBR (Bottleneck Bandwidth and RTT)",
        "distractors": ["TCP Cubic", "TCP Reno", "TCP Vegas"],
        "explanation": "Σε αντίθεση με παραδοσιακούς αλγορίθμους όπως ο Cubic που γεμίζουν τις ουρές των routers μέχρι να πέσουν πακέτα (bufferbloat), ο BBR διατηρεί τη ροή ακριβώς στο βέλτιστο όριο του bottleneck bandwidth με ελάχιστη καθυστέρηση.",
        "funFacts": [
            "Η υιοθέτησή του στο YouTube αύξησε το παγκόσμιο throughput των βίντεο κατά μέσο όρο κατά 4% έως και πάνω από 14% σε χώρες με υποδεέστερες υποδομές δικτύου.",
            "Αναπτύχθηκε υπό την καθοδήγηση του Neal Cardwell και του πρωτοπόρου Van Jacobson."
        ],
        "source": "https://en.wikipedia.org/wiki/BBR_(congestion_control)",
        "tags": ["technology", "networking", "tcp", "bbr"]
    },
    {
        "id": "tech_hard_249",
        "text": "Ποιο φαινόμενο υπερφόρτωσης δικτύου προκαλείται όταν οι δρομολογητές διαθέτουν υπερβολικά μεγάλες ενδιάμεσες μνήμες (buffers), οδηγώντας σε τεράστιες καθυστερήσεις (latency spikes) και jitter;",
        "correct": "Bufferbloat",
        "distractors": ["Bandwidth Throttling", "Packet Storm", "Routing Loop"],
        "explanation": "Το bufferbloat συμβαίνει όταν πακέτα λιμνάζουν σε τεράστιες ουρές περιμένοντας να μεταδοθούν, καθυστερώντας κρίσιμα πακέτα VoIP και gaming κατά εκατοντάδες χιλιοστά του δευτερολέπτου, ενώ ταυτόχρονα εμποδίζουν τους αλγορίθμους TCP να αντιληφθούν τη συμφόρηση.",
        "funFacts": [
            "Ο όρος επινοήθηκε το 2010 από τον Jim Gettys.",
            "Αντιμετωπίζεται με σύγχρονους αλγορίθμους ενεργής διαχείρισης ουρών (AQM) όπως το CoDel (Controlled Delay) και το FQ-CoDel."
        ],
        "source": "https://en.wikipedia.org/wiki/Bufferbloat",
        "tags": ["technology", "networking", "bufferbloat", "latency"]
    },
    {
        "id": "tech_hard_250",
        "text": "Ποιο σύστημα κρυπτογραφικής ασφάλειας του πρωτοκόλλου BGP χρησιμοποιεί μια ιεραρχία ψηφιακών πιστοποιητικών X.509 για να αποτρέπει την πειρατεία διαδρομών IP (BGP Route Hijacking);",
        "correct": "RPKI (Resource Public Key Infrastructure)",
        "distractors": ["DNSSEC", "IPsec", "MACsec"],
        "explanation": "Το RPKI επιτρέπει στους κατόχους διευθύνσεων IP να δημοσιεύουν υπογεγραμμένα αντικείμενα ROA (Route Origin Authorization), εξουσιοδοτώντας ποια Αυτόνομα Συστήματα (ASNs) έχουν νόμιμο δικαίωμα να ανακοινώνουν τα προθέματά τους στο παγκόσμιο BGP.",
        "funFacts": [
            "Χωρίς επικύρωση RPKI, ένα τυχαίο λάθος διαμόρφωσης ή μια σκόπιμη επίθεση μπορεί να ανακατευθύνει παγκόσμια τραπεζική κίνηση ή κρυπτονομίσματα σε κακόβουλους servers (όπως συνέβη στο περιστατικό του MyEtherWallet το 2018).",
            "Διαχειρίζεται σε παγκόσμιο επίπεδο από τα πέντε Περιφερειακά Μητρώα Διαδικτύου (RIRs, όπως το RIPE NCC στην Ευρώπη)."
        ],
        "source": "https://en.wikipedia.org/wiki/Resource_Public_Key_Infrastructure",
        "tags": ["technology", "networking", "rpki", "bgp"]
    },
    {
        "id": "tech_hard_251",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου πιστοποίησης κατάστασης ψηφιακών πιστοποιητικών TLS σε πραγματικό χρόνο που αντικατέστησε τις ογκώδεις λίστες ανάκλησης (CRLs);",
        "correct": "OCSP (Online Certificate Status Protocol)",
        "distractors": ["ACME", "SCEP", "EST"],
        "explanation": "Το OCSP (RFC 6960) επιτρέπει στον browser να ρωτά άμεσα τον διακομιστή της εκδότριας αρχής αν ένα συγκεκριμένο πιστοποιητικό έχει ανακληθεί πριν τη λήξη του.",
        "funFacts": [
            "Για να αποφευχθεί η διαρροή του ιστορικού περιήγησης στην εκδότρια αρχή και η καθυστέρηση σύνδεσης, χρησιμοποιείται η τεχνική 'OCSP Stapling', όπου ο ίδιος ο web server σερβίρει μια πρόσφατη υπογεγραμμένη βεβαίωση εγκυρότητας μαζί με το πιστοποιητικό.",
            "Εισήχθη ως βελτίωση έναντι των παραδοσιακών λιστών CRL που απαιτούσαν το κατέβασμα αρχείων πολλών Megabytes."
        ],
        "source": "https://el.wikipedia.org/wiki/OCSP",
        "tags": ["technology", "security", "ocsp", "tls"]
    },
    {
        "id": "tech_hard_252",
        "text": "Ποια επέκταση του πρωτοκόλλου TLS επιτρέπει στον client να δηλώνει το όνομα τομέα (domain name) του διακομιστή με τον οποίο επιθυμεί να συνδεθεί στην αρχική χειραψία, επιτρέποντας σε μία μόνο IP να φιλοξενεί πολλαπλά πιστοποιητικά SSL;",
        "correct": "SNI (Server Name Indication)",
        "distractors": ["ALPN", "HSTS", "HPKP"],
        "explanation": "Το SNI (RFC 6066) επιλύει το πρόβλημα φιλοξενίας πολλαπλών ασφαλών ιστότοπων στην ίδια φυσική IP: ο server διαβάζει το όνομα τομέα στο αρχικό μήνυμα ClientHello και απαντά με το σωστό πιστοποιητικό TLS.",
        "funFacts": [
            "Επειδή το παραδοσιακό SNI μεταδίδεται σε απλό μη κρυπτογραφημένο κείμενο, αποτελεί εργαλείο παρακολούθησης και λογοκρισίας από αυταρχικά καθεστώτα.",
            "Η σύγχρονη επέκταση ECH (Encrypted Client Hello) κρυπτογραφεί ολόκληρο το μήνυμα ClientHello, αποκρύπτοντας οριστικά το όνομα του ιστότοπου από τρίτους παρατηρητές."
        ],
        "source": "https://en.wikipedia.org/wiki/Server_Name_Indication",
        "tags": ["technology", "security", "sni", "tls"]
    },
    {
        "id": "tech_hard_253",
        "text": "Ποια πρωτοποριακή τεχνολογία ημιαγωγών διαδέχεται τα τρανζίστορ FinFET στους προηγμένους κόμβους 2 νανομέτρων, περιβάλλοντας πλήρως τα κανάλια πυριτίου με νανοφύλλα (nanosheets);",
        "correct": "GAAFET (Gate-All-Around FET)",
        "distractors": ["FinFET", "Planar MOSFET", "BJT"],
        "explanation": "Στα τρανζίστορ GAAFET (όπως το MBCFET της Samsung και το RibbonFET της Intel), η πύλη ελέγχου περιβάλλει ολόκληρο το κανάλι πυριτίου και από τις τέσσερις πλευρές, εξαλείφοντας σχεδόν ολοκληρωτικά τη διαρροή ηλεκτρικού ρεύματος σε υποατομική κλίμακα.",
        "funFacts": [
            "Η Samsung ξεκίνησε την εμπορική παραγωγή GAAFET στα 3nm το 2022, ενώ η TSMC υιοθετεί την τεχνολογία στον κόμβο N2 (2nm).",
            "Επιτρέπει στους κατασκευαστές να συνεχίσουν τη σμίκρυνση των τσιπ ξεπερνώντας τα φυσικά όρια που σταμάτησαν την εξέλιξη των FinFET."
        ],
        "source": "https://en.wikipedia.org/wiki/Gate-all-around_FET",
        "tags": ["technology", "hardware", "semiconductors", "gaafet"]
    },
    {
        "id": "tech_hard_254",
        "text": "Ποιο είναι το μήκος κύματος της ακραίας υπεριώδους ακτινοβολίας (EUV) που χρησιμοποιείται στα πιο προηγμένα μηχανήματα φωτολιθογραφίας της ASML για την εγχάραξη μικροτσίπ;",
        "correct": "13,5 νανόμετρα (nm)",
        "distractors": ["193 νανόμετρα (nm)", "248 νανόμετρα (nm)", "365 νανόμετρα (nm)"],
        "explanation": "Το φως EUV των 13,5 nm απορροφάται σχεδόν από οποιαδήποτε ουσία (ακόμη και από τον αέρα ή το κοινό γυαλί), γι' αυτό ολόκληρη η διαδικασία εκτελείται σε απόλυτο κενό χρησιμοποιώντας υπερπολυτελή κάτοπτρα πολλαπλών επιστρώσεων μολυβδαινίου-πυριτίου της Zeiss.",
        "funFacts": [
            "Τα κάτοπτρα αυτά είναι τα πιο λεία ανθρώπινα κατασκευάσματα στον κόσμο: αν είχαν το μέγεθος της Γερμανίας, η ψηλότερη ανωμαλία στην επιφάνειά τους δεν θα ξεπερνούσε το ένα χιλιοστό!",
            "Αντικατέστησε τα παλαιότερα λέιζερ DUV φθοριούχου αργού (ArF) των 193 nm."
        ],
        "source": "https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography",
        "tags": ["technology", "hardware", "euv", "lithography"]
    },
    {
        "id": "tech_hard_255",
        "text": "Ποια πρωτοποριακή τεχνολογία τροφοδοσίας ημιαγωγών μεταφέρει ολόκληρο το δίκτυο διανομής ηλεκτρικού ρεύματος (Power Delivery Network) στην πίσω πλευρά της γκοφρέτας πυριτίου (backside power delivery);",
        "correct": "Intel PowerVia (ή BS-PDN)",
        "distractors": ["Intel Foveros", "TSMC CoWoS", "AMD 3D V-Cache"],
        "explanation": "Το Backside Power Delivery διαχωρίζει πλήρως τις γραμμές ρεύματος από τα καλώδια σηματοδοσίας δεδομένων, εξαλείφοντας τη συμφόρηση καλωδίωσης στην επάνω επιφάνεια του τσιπ και μειώνοντας την πτώση τάσης (IR drop).",
        "funFacts": [
            "Χρησιμοποιεί νανοσκοπικές διόδους πυριτίου μέσω της πίσω πλευράς γνωστές ως Nano-TSVs.",
            "Η Intel υλοποίησε πρώτη την τεχνολογία στον κόμβο Intel 20A / 18A υπό το όνομα PowerVia, με την TSMC να ακολουθεί με την τεχνολογία A16."
        ],
        "source": "https://en.wikipedia.org/wiki/Backside_power_delivery_network",
        "tags": ["technology", "hardware", "semiconductors", "powervia"]
    },
    {
        "id": "tech_hard_256",
        "text": "Ποια προηγμένη τεχνολογία συσκευασίας 3D (3D packaging) χρησιμοποιεί η AMD στους επεξεργαστές Ryzen 'X3D' για να τοποθετήσει επιπλέον 64 MB κρυφής μνήμης L3 (SRAM) απευθείας πάνω στους πυρήνες CPU;",
        "correct": "AMD 3D V-Cache",
        "distractors": ["Infinity Fabric", "Smart Access Memory", "Precision Boost"],
        "explanation": "Η τεχνολογία 3D V-Cache χρησιμοποιεί απευθείας υβριδική συγκόλληση χαλκού-προς-χαλκό (Direct Copper-to-Copper Bonding) της TSMC χωρίς σφαιρίδια συγκόλλησης, επιτυγχάνοντας ασύλληπτο bandwidth άνω των 2 TB/s μεταξύ των στρωμάτων πυριτίου.",
        "funFacts": [
            "Το πάχος του επεξεργαστή τροχίζεται με ακρίβεια μικρομέτρων ώστε το τελικό τσιπ με την πρόσθετη μνήμη να έχει ακριβώς το ίδιο ύψος με τους απλούς επεξεργαστές.",
            "Προσφέρει τεράστιο άλμα επιδόσεων στα βιντεοπαιχνίδια, καθώς ο επεξεργαστής βρίσκει τα δεδομένα του παιχνιδιού άμεσα στην L3 cache χωρίς να περιμένει την αργή κύρια μνήμη RAM."
        ],
        "source": "https://en.wikipedia.org/wiki/Ryzen#Zen_3",
        "tags": ["technology", "hardware", "amd", "cpu_cache"]
    },
    {
        "id": "tech_hard_257",
        "text": "Ποιο υποσύστημα του πυρήνα του λειτουργικού συστήματος είναι υπεύθυνο για την επιλογή της επόμενης έτοιμης διεργασίας που θα εκτελεστεί στην CPU, εφαρμόζοντας αλγορίθμους όπως ο Completely Fair Scheduler (CFS);",
        "correct": "Χρονοπρογραμματιστής διεργασιών (Process Scheduler)",
        "distractors": ["Διαχειριστής εικονικής μνήμης", "Ελεγκτής διακοπών (APIC)", "Πρόγραμμα εκκίνησης (Bootloader)"],
        "explanation": "Ο χρονοπρογραμματιστής (Scheduler) εξασφαλίζει δίκαιη κατανομή χρόνου επεξεργαστή σε εκατοντάδες ταυτόχρονες διεργασίες. Ο κλασικός CFS του Linux χρησιμοποιεί ένα αυτο-εξισορροπούμενο κόκκινο-μαύρο δέντρο βασισμένο στον εικονικό χρόνο εκτέλεσης (vruntime).",
        "funFacts": [
            "Ο CFS αναπτύχθηκε από τον Ingo Molnar και εισήχθη στον πυρήνα Linux 2.6.23.",
            "Στον πυρήνα Linux 6.6 (2023), ο CFS αντικαταστάθηκε από τον νεότερο χρονοπρογραμματιστή EEVDF (Earliest Eligible Virtual Deadline First) του Peter Zijlstra."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A7%CF%81%CE%BF%CE%BD%CE%BF%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CF%8C%CF%82_(%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%AE)",
        "tags": ["technology", "linux", "operating_systems", "scheduler"]
    },
    {
        "id": "tech_hard_258",
        "text": "Πώς ονομάζεται η διαδικασία αποθήκευσης της κατάστασης μιας διεργασίας (καταχωρητές, δείκτης στοίβας, μετρητής προγράμματος) και φόρτωσης της κατάστασης μιας άλλης κατά την εναλλαγή εκτέλεσης στην CPU;",
        "correct": "Εναλλαγή περιβάλλοντος (Context Switch)",
        "distractors": ["Διακλάδωση εντολής (Branching)", "Διακοπή ρολογιού (Clock Interrupt)", "Εναλλαγή σελίδας (Paging)"],
        "explanation": "Το Context Switch είναι μια υπολογιστικά ακριβή λειτουργία, καθώς εκτός από την αποθήκευση δεκάδων καταχωρητών συστήματος, μπορεί να προκαλέσει ακύρωση των περιεχομένων του TLB και απώλεια αποδοτικότητας της κρυφής μνήμης CPU.",
        "funFacts": [
            "Σε έναν σύγχρονο υπολογιστή εκτελούνται δεκάδες χιλιάδες context switches κάθε δευτερόλεπτο.",
            "Οι ελαφριές διεργασίες όπως τα 'goroutines' στη Go εκτελούν context switching στο επίπεδο χρήστη (userspace) καταναλώνοντας μόλις λίγα νανοδευτερόλεπτα, σε αντίθεση με τα βαριά context switches του λειτουργικού συστήματος."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BD%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CE%AE_%CF%80%CE%BB%CE%B1%CE%B9%CF%83%CE%AF%CE%BF%CF%85",
        "tags": ["technology", "operating_systems", "context_switch", "cpu"]
    },
    {
        "id": "tech_hard_259",
        "text": "Ποια είναι η λειτουργία του μηχανισμού 'Copy-on-Write' (CoW) κατά την εκτέλεση της κλήσης συστήματος fork() στο λειτουργικό σύστημα Unix;",
        "correct": "Η θυγατρική διεργασία μοιράζεται τις ίδιες φυσικές σελίδες μνήμης με τη γονική, και μια νέα σελίδα δεσμεύεται μόνο όταν κάποια από τις δύο επιχειρήσει να γράψει δεδομένα",
        "distractors": ["Αντιγράφει ακαριαία ολόκληρη τη μνήμη RAM στον σκληρό δίσκο", "Διαγράφει όλες τις προηγούμενες μεταβλητές για εξοικονόμηση χώρου", "Κλειδώνει τη μητρική κάρτα μέχρι να ολοκληρωθεί η εκτέλεση"],
        "explanation": "Χωρίς το Copy-on-Write, κάθε κλήση fork() θα απαιτούσε την πλήρη και αργή αντιγραφή ολόκληρης της μνήμης της διεργασίας, κάτι εντελώς σπάταλο δεδομένου ότι συνήθως ακολουθείται αμέσως από την κλήση exec() για εκτέλεση νέου προγράμματος.",
        "funFacts": [
            "Υλοποιείται σε επίπεδο υλικού μαρκάροντας τις σελίδες μνήμης ως 'read-only' στον πίνακα σελίδων: όταν μια διεργασία επιχειρεί εγγραφή, παράγεται ένα Page Fault και ο πυρήνας αναλαμβάνει να αντιγράψει μόνο τη συγκεκριμένη σελίδα.",
            "Χρησιμοποιείται επίσης σε προηγμένα συστήματα αρχείων όπως το ZFS και το Btrfs για τη δημιουργία στιγμιοτύπων (snapshots) με μηδενικό κόστος χώρου."
        ],
        "source": "https://en.wikipedia.org/wiki/Copy-on-write",
        "tags": ["technology", "operating_systems", "copy_on_write", "virtual_memory"]
    },
    {
        "id": "tech_hard_260",
        "text": "Ποιο είναι το θεμελιώδες όριο του John von Neumann στη σχεδίαση υπολογιστών, γνωστό ως 'Σημείο Συμφόρησης Von Neumann' (Von Neumann Bottleneck);",
        "correct": "Ο περιορισμός της συνολικής απόδοσης του συστήματος λόγω του περιορισμένου εύρους ζώνης του κοινού διαύλου επικοινωνίας μεταξύ CPU και κύριας μνήμης",
        "distractors": ["Η αδυναμία των επεξεργαστών να ξεπεράσουν τους 100 βαθμούς Κελσίου", "Η αδυναμία των μαθηματικών να αναπαραστήσουν αρνητικούς αριθμούς σε δυαδικό σύστημα", "Ο περιορισμός του μεγέθους των οθονών υπολογιστή"],
        "explanation": "Ενώ η υπολογιστική ταχύτητα των επεξεργαστών αυξανόταν εκθετικά επί δεκαετίες, η ταχύτητα μεταφοράς δεδομένων από τη μνήμη RAM βελτιωνόταν πολύ πιο αργά (Memory Wall), αναγκάζοντας την CPU να παραμένει σε κατάσταση αναμονής δεδομένων.",
        "funFacts": [
            "Ο όρος επινοήθηκε από τον John Backus στη διάλεξή του για το Βραβείο Turing το 1977.",
            "Η χρήση τεράστιων πολυεπίπεδων κρυφών μνημών (L1, L2, L3 cache) και αρχιτεκτονικών Compute-In-Memory σχεδιάστηκαν ακριβώς για να αμβλύνουν αυτό το σημείο συμφόρησης."
        ],
        "source": "https://en.wikipedia.org/wiki/Von_Neumann_architecture#Von_Neumann_bottleneck",
        "tags": ["technology", "hardware", "von_neumann", "computer_architecture"]
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
    print(f"Loaded {len(questions)} questions for technology_hard batch 1 (211-260).")
    validate_and_append("technology", "hard", 5, questions)

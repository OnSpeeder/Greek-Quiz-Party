# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# Batch 3: tech_hard_311 to tech_hard_360 (50 questions)
raw_questions = [
    {
        "id": "tech_hard_311",
        "text": "Ποιο μαθηματικό πρόβλημα πλεγμάτων (lattices) που εισήγαγε ο Oded Regev το 2005 αποτελεί τη βάση για τη συντριπτική πλειονότητα των σύγχρονων μετα-κβαντικών κρυπτοσυστημάτων (Post-Quantum Cryptography);",
        "correct": "Learning With Errors (LWE)",
        "distractors": ["Shortest Vector Problem (SVP)", "Closest Vector Problem (CVP)", "Subset Sum Problem"],
        "explanation": "Το πρόβλημα LWE (Μάθηση με Σφάλματα) συνίσταται στην εύρεση ενός μυστικού διανύσματος μέσα από ένα υπερκαθορισμένο σύστημα γραμμικών εξισώσεων στο οποίο έχει προστεθεί μικρός τυχαίος θόρυβος, κάτι που αποδεδειγμένα παραμένει υπολογιστικά δυσεπίλυτο και για κβαντικούς υπολογιστές.",
        "funFacts": [
            "Ο Oded Regev τιμήθηκε με το διάσημο βραβείο Gödel το 2018 για την ανακάλυψη του LWE και των κβαντικών αναγωγών του.",
            "Η παραλλαγή Ring-LWE επιτρέπει δραματική μείωση του μεγέθους των κλειδιών αντικαθιστώντας τους πίνακες με πολυώνυμα πάνω σε κυκλοτομικούς δακτυλίους."
        ],
        "source": "https://en.wikipedia.org/wiki/Learning_with_errors",
        "tags": ["technology", "cryptography", "post_quantum", "lwe"]
    },
    {
        "id": "tech_hard_312",
        "text": "Ποιος αλγόριθμος κρυπτογράφησης δημόσιου κλειδιού επελέγη από το NIST το 2022 ως το κύριο παγκόσμιο πρότυπο για γενική μετα-κβαντική κρυπτογράφηση και τυποποιήθηκε ως FIPS 203 (ML-KEM);",
        "correct": "CRYSTALS-Kyber",
        "distractors": ["NTRU", "Classic McEliece", "SABER"],
        "explanation": "Το CRYSTALS-Kyber βασίζεται στη μαθηματική σκληρότητα του προβλήματος Module Learning With Errors (M-LWE) πάνω σε κυκλοτομικούς δακτυλίους πολυωνύμων.",
        "funFacts": [
            "Το Kyber σχεδιάστηκε από διεθνή κοινοπραξία κρυπτογράφων και πήρε το όνομά του από τους κρυστάλλους 'kyber' που τροφοδοτούν τα φωτόσπαθα στο σύμπαν του Star Wars.",
            "Προγράμματα περιήγησης όπως το Chrome και υπηρεσίες όπως το Cloudflare έχουν ήδη ενσωματώσει υβριδική κρυπτογράφηση Kyber για συνδέσεις TLS 1.3."
        ],
        "source": "https://en.wikipedia.org/wiki/Kyber",
        "tags": ["technology", "cryptography", "post_quantum", "kyber"]
    },
    {
        "id": "tech_hard_313",
        "text": "Ποιο σύστημα μετα-κβαντικών ψηφιακών υπογραφών επιλέχθηκε από το NIST ως το βασικό πρότυπο γενικής χρήσης και τυποποιήθηκε ως FIPS 204 (ML-DSA);",
        "correct": "CRYSTALS-Dilithium",
        "distractors": ["Falcon", "Rainbow", "GeMSS"],
        "explanation": "Το CRYSTALS-Dilithium χρησιμοποιεί το παράδειγμα 'Fiat-Shamir with Aborts' πάνω σε πλέγματα τύπου Module-LWE και Module-SIS, προσφέροντας ισχυρή ασφάλεια έναντι κβαντικών επιθέσεων.",
        "funFacts": [
            "Όπως και το Kyber, το Dilithium δανείστηκε το όνομά του από την επιστημονική φαντασία, συγκεκριμένα από τους κρυστάλλους 'dilithium' που τροφοδοτούν τις μηχανές στρέβλωσης (warp drive) στο Star Trek.",
            "Σε αντίθεση με τις υπογραφές RSA που έχουν μέγεθος 256-512 bytes, μια υπογραφή Dilithium απαιτεί περίπου 2,4 έως 4,6 KB."
        ],
        "source": "https://en.wikipedia.org/wiki/CRYSTALS-Dilithium",
        "tags": ["technology", "cryptography", "post_quantum", "dilithium"]
    },
    {
        "id": "tech_hard_314",
        "text": "Ποιο πρότυπο μετα-κβαντικών ψηφιακών υπογραφών (FIPS 205 / SLH-DSA) βασίζεται αποκλειστικά στην ασφάλεια κρυπτογραφικών συναρτήσεων κατακερματισμού (hash-based) και σε ιεραρχικά δέντρα Merkle χωρίς να βασίζεται σε πλέγματα;",
        "correct": "SPHINCS+",
        "distractors": ["Falcon", "BIKE", "HQC"],
        "explanation": "Το SPHINCS+ είναι ένα stateless σχήμα υπογραφών βασισμένο σε συναρτήσεις κατακερματισμού, παρέχοντας μια εξαιρετικά συντηρητική και αξιόπιστη εναλλακτική σε περίπτωση που ανακαλυφθεί κάποια θεωρητική αδυναμία στα πλέγματα.",
        "funFacts": [
            "Ονομάζεται 'stateless' επειδή ο υπογράφων δεν χρειάζεται να διατηρεί κατάσταση μετρητή των υπογραφών που έχει ήδη παράγει, αποτρέποντας καταστροφικές επαναχρησιμοποιήσεις ιδιωτικών κλειδιών.",
            "Το μέγεθος της υπογραφής SPHINCS+ είναι σχετικά μεγάλο, φτάνοντας τα 8 έως 30 KB ανάλογα με το επιθυμητό επίπεδο ασφάλειας."
        ],
        "source": "https://en.wikipedia.org/wiki/SPHINCS",
        "tags": ["technology", "cryptography", "sphincs", "hash_based"]
    },
    {
        "id": "tech_hard_315",
        "text": "Ποιο είναι το θεμελιώδες πλεονέκτημα των αποδείξεων μηδενικής γνώσης τύπου zk-STARKs σε σχέση με τα κλασικά zk-SNARKs (όπως το Groth16);",
        "correct": "Δεν απαιτούν αξιόπιστη τελετή αρχικοποίησης (Trusted Setup) και είναι κβαντικά ανθεκτικά",
        "distractors": [
            "Έχουν δραματικά μικρότερο μέγεθος απόδειξης σε bytes",
            "Απαιτούν λιγότερη υπολογιστική μνήμη RAM από τον prover",
            "Βασίζονται σε ελλειπτικές καμπύλες και ζεύγη Weil"
        ],
        "explanation": "Τα STARKs (Scalable Transparent Arguments of Knowledge) είναι 'Transparent' επειδή χρησιμοποιούν μόνο δημόσια τυχαιότητα και συναρτήσεις κατακερματισμού, εξαλείφοντας την ανάγκη για επικίνδυνη τελετή Trusted Setup.",
        "funFacts": [
            "Επινοήθηκαν από τον Eli Ben-Sasson και την ερευνητική του ομάδα, οδηγώντας στην ίδρυση της StarkWare.",
            "Αν και είναι διαφανή και κβαντικά ασφαλή, οι αποδείξεις STARKs καταλαμβάνουν δεκάδες kilobytes, συγκριτικά με τα μόλις ~130 bytes μιας απόδειξης Groth16 SNARK."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-knowledge_proof",
        "tags": ["technology", "cryptography", "zero_knowledge", "starks", "snarks"]
    },
    {
        "id": "tech_hard_316",
        "text": "Ποιο φορμαλιστικό μαθηματικό σύστημα αναπαράστασης υπολογιστικών κυκλωμάτων χρησιμοποιείται ως ενδιάμεση βαθμίδα στα zk-SNARKs, όπου κάθε περιορισμός εκφράζεται ως (A * s) * (B * s) - (C * s) = 0;",
        "correct": "Rank-1 Constraint System (R1CS)",
        "distractors": ["Boolean Satisfiability (SAT)", "Abstract Syntax Tree (AST)", "Finite State Automaton (FSA)"],
        "explanation": "Στο R1CS, ένας αυθαίρετος υπολογισμός μετατρέπεται σε σύστημα εξισώσεων διανυσματικών γινομένων πάνω από πεπερασμένα σώματα, όπου κάθε εξίσωση επιτρέπει το πολύ έναν πολλαπλασιασμό.",
        "funFacts": [
            "Οποιοδήποτε πρόγραμμα γραμμένο σε γλώσσες μηδενικής γνώσης όπως το Circom ή το ZoKrates μεταγλωττίζεται πρώτα σε περιορισμούς R1CS.",
            "Το R1CS στη συνέχεια μετατρέπεται μέσω παρεμβολής Lagrange σε QAP (Quadratic Arithmetic Program) για τη δημιουργία της απόδειξης."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-knowledge_proof",
        "tags": ["technology", "cryptography", "zero_knowledge", "r1cs"]
    },
    {
        "id": "tech_hard_317",
        "text": "Ποιο σύστημα αποδείξεων μηδενικής γνώσης, που εισήγαγαν οι Ariel Gabizon, Zac Williamson και Oana Ciobotaru το 2019, εισήγαγε καθολική και ανανεώσιμη αξιόπιστη αρχικοποίηση (Universal and Updateable Trusted Setup);",
        "correct": "PLONK",
        "distractors": ["Groth16", "Bulletproofs", "Sonic"],
        "explanation": "Το PLONK (Permutations over Lagrange-bases for O(n) Non-interactive arguments of Knowledge) επέτρεψε μία μοναδική τελετή αρχικοποίησης (SRS) που μπορεί να επαναχρησιμοποιηθεί για οποιοδήποτε πρόγραμμα μέχρι ένα μέγιστο μέγεθος.",
        "funFacts": [
            "Πριν το PLONK, πρωτόκολλα όπως το Groth16 απαιτούσαν ξεχωριστή, περίπλοκη τελετή παραγωγής τυχαίων παραμέτρων ('toxic waste') για κάθε μεμονωμένο έξυπνο συμβόλαιο.",
            "Το PLONK βασίζεται σε ελέγχους μετάθεσης (permutation checks) και πολυωνυμικές δεσμεύσεις KZG."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-knowledge_proof",
        "tags": ["technology", "cryptography", "plonk", "zero_knowledge"]
    },
    {
        "id": "tech_hard_318",
        "text": "Ποιο διαδραστικό πρωτόκολλο εγγύτητας (IOP) χρησιμοποιούν τα zk-STARKs για να αποδείξουν γρήγορα ότι ένας πίνακας τιμών αντιστοιχεί σε πολυώνυμο χαμηλού βαθμού;",
        "correct": "Fast Reed-Solomon Interactive Oracle Proof of Proximity (FRI)",
        "distractors": ["KZG Polynomial Commitment", "Inner Product Argument (IPA)", "Bulletproofs Multi-exponentiation"],
        "explanation": "Το πρωτόκολλο FRI επιτρέπει στον ελεγκτή (verifier) να πειστεί με λογαριθμικό αριθμό δειγματοληψιών ότι μια συνάρτηση βρίσκεται εξαιρετικά κοντά σε έναν κώδικα Reed-Solomon.",
        "funFacts": [
            "Το FRI δεν απαιτεί καμία άλγεβρα ελλειπτικών καμπυλών, στηριζόμενο εξ ολοκλήρου σε Merkle δέντρα και συναρτήσεις κατακερματισμού.",
            "Αποτελεί την κινητήρια δύναμη πίσω από τα Starknet και Polygon Miden rollups στο Ethereum."
        ],
        "source": "https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction",
        "tags": ["technology", "cryptography", "fri", "starks"]
    },
    {
        "id": "tech_hard_319",
        "text": "Ποια κρυπτογραφική δέσμευση πολυωνύμων (Polynomial Commitment Scheme - PCS) χρησιμοποιεί ζεύγη ελλειπτικών καμπυλών (bilinear pairings) και επιτρέπει απόδειξη σταθερού μεγέθους ενός μόνο στοιχείου ομάδας;",
        "correct": "Δέσμευση KZG (Kate-Zaverucha-Goldberg)",
        "distractors": ["Δέσμευση Bulletproofs", "Δέσμευση FRI", "Δέσμευση Dory"],
        "explanation": "Το σχήμα KZG επιτρέπει τη δέσμευση σε ένα πολυώνυμο οποιουδήποτε βαθμού με ένα ενιαίο σημείο καμπύλης και την απόδειξη της τιμής του P(z) = y επίσης με ένα μόνο σημείο ομάδας.",
        "funFacts": [
            "Χρησιμοποιείται στο αναβαθμισμένο πρωτόκολλο του Ethereum (EIP-4844 / Proto-Danksharding) για την επαλήθευση των data blobs.",
            "Η τελετή αρχικοποίησης του Ethereum KZG το 2023 συγκέντρωσε πάνω από 140.000 συμμετέχοντες, αποτελώντας τη μεγαλύτερη κρυπτογραφική τελετή στην ιστορία."
        ],
        "source": "https://en.wikipedia.org/wiki/Commitment_scheme",
        "tags": ["technology", "cryptography", "kzg", "polynomials"]
    },
    {
        "id": "tech_hard_320",
        "text": "Ποια ενδιάμεση μορφή αναπαράστασης κώδικα (Intermediate Representation) σε μεταγλωττιστές απαιτεί κάθε μεταβλητή να ορίζεται αυστηρά μία και μοναδική φορά, διευκολύνοντας δραστικά τις βελτιστοποιήσεις;",
        "correct": "Static Single Assignment form (SSA)",
        "distractors": ["Three-Address Code (TAC)", "Continuation-Passing Style (CPS)", "Abstract Syntax Tree (AST)"],
        "explanation": "Στη μορφή SSA (Στατική Ενιαία Ανάθεση), κάθε ανάθεση σε μια μεταβλητή δημιουργεί μια νέα έκδοσή της (π.χ. x1, x2), απλοποιώντας τον υπολογισμό ανάλυσης ροής δεδομένων.",
        "funFacts": [
            "Αναπτύχθηκε στα τέλη της δεκαετίας του 1980 από ερευνητές της IBM (Ron Cytron, Jeanne Ferrante κ.ά.).",
            "Όλοι οι σύγχρονοι βελτιστοποιητικοί μεταγλωττιστές παραγωγής, συμπεριλαμβανομένων των LLVM, GCC, HotSpot JVM και V8, μετατρέπουν τον κώδικα σε μορφή SSA."
        ],
        "source": "https://en.wikipedia.org/wiki/Static_single-assignment_form",
        "tags": ["technology", "compilers", "ssa", "optimization"]
    },
    {
        "id": "tech_hard_321",
        "text": "Ποια ειδική συνάρτηση/εντολή εισάγεται στα σημεία συνένωσης ροής ελέγχου σε μορφή SSA για να επιλέξει τη σωστή τιμή μιας μεταβλητής ανάλογα με το από ποιο βασικό μπλοκ (basic block) προήλθε η εκτέλεση;",
        "correct": "Συνάρτηση Phi (phi-node / φ-function)",
        "distractors": ["Συνάρτηση Lambda (λ-function)", "Συνάρτηση Mu (μ-function)", "Συνάρτηση Delta (δ-function)"],
        "explanation": "Όταν δύο διαφορετικά μονοπάτια ενός if-else συγκλίνουν, το phi-node x3 = φ(x1, x2) αναθέτει στο x3 είτε την τιμή του x1 είτε του x2 ανάλογα με τη διαδρομή εκτέλεσης.",
        "funFacts": [
            "Οι συναρτήσεις phi δεν αντιστοιχούν σε πραγματικές εντολές μηχανής και εξαλείφονται κατά το στάδιο παραγωγής τελικού κώδικα μέσω κατανομής καταχωρητών.",
            "Τα σημεία τοποθέτησης των κόμβων phi υπολογίζονται με βάση τα σύνορα κυριαρχίας (dominance frontiers) του γράφου ροής ελέγχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Static_single-assignment_form",
        "tags": ["technology", "compilers", "ssa", "phi_function"]
    },
    {
        "id": "tech_hard_322",
        "text": "Πώς ονομάζεται η μεταγλωττιστική βελτιστοποίηση που εντοπίζει εκφράσεις εντός ενός βρόχου των οποίων τα ορίσματα δεν μεταβάλλονται και τις μετακινεί έξω από τον βρόχο;",
        "correct": "Loop-Invariant Code Motion (LICM)",
        "distractors": ["Loop Unrolling", "Loop Fission", "Loop Peeling"],
        "explanation": "Η LICM αναγνωρίζει υπολογισμούς μέσα στο σώμα ενός βρόχου που παράγουν πανομοιότυπο αποτέλεσμα σε κάθε επανάληψη και τους εκτελεί μία μόνο φορά πριν από την είσοδο στον βρόχο (pre-header).",
        "funFacts": [
            "Εξοικονομεί τεράστιο αριθμό κύκλων επεξεργαστή σε βρόχους με εκατομμύρια επαναλήψεις.",
            "Για να εφαρμοστεί με ασφάλεια, ο μεταγλωττιστής πρέπει να αποδείξει ότι η έκφραση δεν προκαλεί παρενέργειες (όπως διαίρεση με το μηδέν ή εξαίρεση πρόσβασης μνήμης)."
        ],
        "source": "https://en.wikipedia.org/wiki/Loop-invariant_code_motion",
        "tags": ["technology", "compilers", "optimization", "loops"]
    },
    {
        "id": "tech_hard_323",
        "text": "Ποια μεταγλωττιστική τεχνική βελτιστοποίησης αντικαθιστά ακριβές αριθμητικές πράξεις (όπως πολλαπλασιασμό ή διαίρεση) με φθηνότερες ισοδύναμες πράξεις (όπως πρόσθεση ή δυαδική ολίσθηση bit);",
        "correct": "Μείωση Ισχύος (Strength Reduction)",
        "distractors": ["Συνεπαγωγή Σταθερών (Constant Folding)", "Εξάλειψη Νεκρού Κώδικα (DCE)", "Ευθυγράμμιση Βρόχου"],
        "explanation": "Για παράδειγμα, η έκφραση x * 2 αντικαθίσταται από x << 1, ή σε έναν βρόχο for (i=0; i<n; i++) ο πολλαπλασιασμός i * 4 αντικαθίσταται από διαδοχικές προσθέσεις +4 σε κάθε βήμα.",
        "funFacts": [
            "Αποτελεί μία από τις παλαιότερες και πιο αποτελεσματικές τεχνικές βελτιστοποίησης σε μεταγλωττιστές από την εποχή του FORTRAN.",
            "Σε παλαιότερους επεξεργαστές, ένας πολλαπλασιασμός χρειαζόταν δεκάδες κύκλους ρολογιού, καθιστώντας τη μείωση ισχύος κρίσιμη για την ταχύτητα."
        ],
        "source": "https://en.wikipedia.org/wiki/Strength_reduction",
        "tags": ["technology", "compilers", "strength_reduction", "optimization"]
    },
    {
        "id": "tech_hard_324",
        "text": "Ποιο μαθηματικό πλαίσιο ανάλυσης επιτρέπει σε προηγμένους μεταγλωττιστές να αντιμετωπίζουν φωλιασμένους βρόχους ως γεωμετρικά πολύτοπα για ακραίες βελτιστοποιήσεις παραλληλισμού και κρυφής μνήμης;",
        "correct": "Πολυεδρικό Μοντέλο (Polyhedral Model)",
        "distractors": ["Ανάλυση Fourier", "Αλγεβρική Τοπολογία", "Θεωρία Γράφων Πεπερασμένων Καταστάσεων"],
        "explanation": "Το πολυεδρικό μοντέλο (polyhedral compilation) αναπαριστά τις επαναλήψεις των βρόχων ως ακέραια σημεία μέσα σε πολύεδρα Z-πολυτόπων, επιτρέποντας αφηρημένους γεωμετρικούς μετασχηματισμούς (loop tiling, skewing).",
        "funFacts": [
            "Χρησιμοποιείται στο υποσύστημα Polly του LLVM και στο Graphite του GCC για αυτόματο παραλληλισμό σε κάρτες γραφικών GPU και επιταχυντές AI.",
            "Επινοήθηκε αρχικά από τους Richard Karp, Raymond Miller και Leslie Lamport στα τέλη της δεκαετίας του 1960."
        ],
        "source": "https://en.wikipedia.org/wiki/Polytope_model",
        "tags": ["technology", "compilers", "polyhedral", "optimization"]
    },
    {
        "id": "tech_hard_325",
        "text": "Ποιος μηχανισμός ασφαλείας σε επίπεδο υλικού και λογισμικού διασφαλίζει ότι η ροή εκτέλεσης ενός προγράμματος ακολουθεί αποκλειστικά έγκυρες διαδρομές του γράφου ροής ελέγχου (CFG);",
        "correct": "Ακεραιότητα Ροής Ελέγχου (Control Flow Integrity - CFI)",
        "distractors": ["Address Space Layout Randomization (ASLR)", "Data Execution Prevention (DEP)", "Stack Canaries"],
        "explanation": "Το CFI εμποδίζει επιθέσεις όπως ROP (Return-Oriented Programming) και JOP (Jump-Oriented Programming) ελέγχοντας αν οι έμμεσες κλήσεις και οι επιστροφές συναρτήσεων στοχεύουν σε νόμιμες διευθύνσεις.",
        "funFacts": [
            "Προτάθηκε το 2005 από ερευνητές της Microsoft Research (Abadi, Budiu, Erlingsson, Ligatti).",
            "Ο πυρήνας του Linux και το Android χρησιμοποιούν Clang CFI για να αποτρέψουν εκμετάλλευση ευπαθειών αλλοίωσης μνήμης."
        ],
        "source": "https://en.wikipedia.org/wiki/Control-flow_integrity",
        "tags": ["technology", "security", "cfi", "exploit_mitigation"]
    },
    {
        "id": "tech_hard_326",
        "text": "Ποια τεχνολογία υλικού εισήγαγε η Intel στους επεξεργαστές 11ης γενιάς για προστασία από επιθέσεις ROP μέσω μιας απομονωμένης δεύτερης στοίβας μνήμης υλικού;",
        "correct": "Control-flow Enforcement Technology (Intel CET) με Shadow Stack",
        "distractors": ["Memory Protection Extensions (MPX)", "Software Guard Extensions (SGX)", "Total Memory Encryption (TME)"],
        "explanation": "Το Shadow Stack του Intel CET αποθηκεύει αυτόματα τις διευθύνσεις επιστροφής συναρτήσεων σε μια κλειδωμένη περιοχή μνήμης υλικού και τις συγκρίνει κατά την εντολή RET, τερματίζοντας το πρόγραμμα αν διαπιστωθεί αναντιστοιχία.",
        "funFacts": [
            "Εκτός από το Shadow Stack, το CET περιλαμβάνει το Indirect Branch Tracking (IBT) με ειδική εντολή ENDBR για προστασία από άλματα JOP.",
            "Η Microsoft ενσωμάτωσε υποστήριξη για το Intel CET στα Windows 10 και 11 υπό την ονομασία 'Hardware-enforced Stack Protection'."
        ],
        "source": "https://en.wikipedia.org/wiki/Control-flow_Enforcement_Technology",
        "tags": ["technology", "hardware", "intel_cet", "security"]
    },
    {
        "id": "tech_hard_327",
        "text": "Πώς ονομάζεται η τεχνική επιτάχυνσης επεξεργαστών Out-of-Order όπου μια εντολή φόρτωσης (load) παίρνει δεδομένα απευθείας από μια προηγούμενη εντολή αποθήκευσης (store) στον store buffer χωρίς να περιμένει την εγγραφή στην L1 cache;",
        "correct": "Προώθηση Αποθήκευσης (Store Forwarding)",
        "distractors": ["Αποσαφήνιση Μνήμης (Memory Disambiguation)", "Εικαστική Εκτέλεση (Speculative Execution)", "Διακλάδωση Branch Prediction"],
        "explanation": "Όταν μια εντολή load διαβάζει από την ίδια ακριβώς διεύθυνση μνήμης στην οποία μόλις έγραψε μια εντολή store που εκκρεμεί στον store buffer, τα δεδομένα προωθούνται άμεσα παρακάμπτοντας την ιεραρχία της κρυφής μνήμης.",
        "funFacts": [
            "Αν το μέγεθος ή η ευθυγράμμιση των bytes δεν ταιριάζει απόλυτα, συμβαίνει 'store forwarding stall', επιβραδύνοντας την εκτέλεση κατά 10-20 κύκλους ρολογιού.",
            "Αποτελεί έναν από τους πιο κρίσιμους μηχανισμούς για την επίτευξη υψηλής απόδοσης IPC σε σύγχρονους υπερβαθμωτούς επεξεργαστές."
        ],
        "source": "https://en.wikipedia.org/wiki/Store_buffer",
        "tags": ["technology", "cpu", "microarchitecture", "hardware"]
    },
    {
        "id": "tech_hard_328",
        "text": "Ποιο φαινόμενο υποβάθμισης απόδοσης συμβαίνει σε επεξεργαστές x86 όταν δύο διευθύνσεις μνήμης έχουν διαφορά ακριβώς πολλαπλάσιο των 4096 bytes (4 KB), προκαλώντας σύγκρουση στους ελεγκτές των pipelines φόρτωσης/αποθήκευσης;",
        "correct": "4K Aliasing (Ψευδώνυμο 4KB)",
        "distractors": ["Cache Miss Thrashing", "Page Fault Loop", "TLB Miss Storm"],
        "explanation": "Επειδή οι επεξεργαστές ελέγχουν τα χαμηλότερα 12 bits της εικονικής διεύθυνσης για να ανιχνεύσουν γρήγορα πιθανές συγκρούσεις store-to-load, δύο διευθύνσεις με απόσταση πολλαπλάσιο του 4K φαίνονται ίδιες, προκαλώντας ψευδή σύγκρουση και σοβαρή καθυστέρηση.",
        "funFacts": [
            "Μπορεί να ρίξει την ταχύτητα επεξεργασίας σε ευαίσθητους αλγορίθμους επεξεργασίας εικόνας ή πινάκων κατά πάνω από 300%.",
            "Η λύση είναι η κατάλληλη στοίχιση (padding) των πινάκων ώστε οι γραμμές να μην απέχουν ακριβώς πολλαπλάσια των 4096 bytes."
        ],
        "source": "https://en.wikipedia.org/wiki/Pipeline_stall",
        "tags": ["technology", "cpu", "microarchitecture", "optimization"]
    },
    {
        "id": "tech_hard_329",
        "text": "Πώς ονομάζεται το πρόβλημα πολυνηματικού προγραμματισμού όπου δύο ανεξάρτητα νήματα σε διαφορετικούς πυρήνες τροποποιούν διαφορετικές μεταβλητές, οι οποίες όμως τυχαίνει να μοιράζονται την ίδια γραμμή κρυφής μνήμης (cache line);",
        "correct": "Ψευδής Διαμοιρασμός (False Sharing)",
        "distractors": ["Αδιέξοδο (Deadlock)", "Συνθήκη Ανταγωνισμού (Race Condition)", "Λιμοκτονία (Starvation)"],
        "explanation": "Στο False Sharing, το πρωτόκολλο συνοχής κρυφής μνήμης (MESI/MOESI) ακυρώνει διαρκώς ολόκληρη τη γραμμή κρυφής μνήμης 64 bytes μεταξύ των πυρήνων ('ping-pong'), καταστρέφοντας την απόδοση παρόλο που τα νήματα δεν μοιράζονται καμία κοινή μεταβλητή.",
        "funFacts": [
            "Αντιμετωπίζεται εισάγοντας κενό χώρο (padding) μεταξύ των μεταβλητών ή χρησιμοποιώντας την οδηγία alignas(64) στη C++.",
            "Είναι ένα από τα πιο ύπουλα σφάλματα απόδοσης καθώς δεν προκαλεί λάθος υπολογιστικά αποτελέσματα, παρά μόνο τεράστια επιβράδυνση."
        ],
        "source": "https://en.wikipedia.org/wiki/False_sharing",
        "tags": ["technology", "concurrency", "cpu_cache", "performance"]
    },
    {
        "id": "tech_hard_330",
        "text": "Ποιες ειδικές εντολές επεξεργαστή (όπως οι MOVNTQ/MOVNTDQ στα x86) χρησιμοποιούνται για εγγραφή τεράστιου όγκου δεδομένων απευθείας στη RAM παρακάμπτοντας πλήρως την ιεραρχία των cache για να μην μολυνθεί η κρυφή μνήμη;",
        "correct": "Μη-χρονικές αποθηκεύσεις (Non-Temporal Stores)",
        "distractors": ["Ατομικές αποθηκεύσεις (Atomic Stores)", "Προ-ανακτήσεις μνήμης (Prefetching)", "Εντολές DMA"],
        "explanation": "Οι Non-temporal stores (ή streaming stores) γράφουν δεδομένα απευθείας στη μνήμη RAM μέσω των write-combining buffers, αποτρέποντας την εκδίωξη χρήσιμων δεδομένων από τις L1/L2/L3 caches.",
        "funFacts": [
            "Χρησιμοποιούνται εκτενώς σε αλγορίθμους αντιγραφής μνήμης (memcpy) μεγάλων αρχείων και rendering βίντεο.",
            "Επειδή παρακάμπτουν τη συνοχή της κρυφής μνήμης, απαιτούν εντολή φράγματος μνήμης (SFENCE) για να διασφαλιστεί ότι οι εγγραφές έγιναν ορατές στους άλλους πυρήνες."
        ],
        "source": "https://en.wikipedia.org/wiki/Non-temporal_store",
        "tags": ["technology", "cpu", "hardware", "memory"]
    },
    {
        "id": "tech_hard_331",
        "text": "Ποιος μηχανισμός συγχρονισμού του πυρήνα Linux, που εισήχθη το 2002, επιτρέπει γρήγορο κλείδωμα mutex στο userspace χωρίς context switch σε system call αν δεν υπάρχει διαμάχη (contention);",
        "correct": "Futex (Fast Userspace Mutex)",
        "distractors": ["Spinlock", "Semaphore", "Eventfd"],
        "explanation": "Το futex ελέγχει πρώτα μια ακέραια τιμή στη μνήμη του χρήστη με μια ατομική εντολή (π.χ. compare-and-swap). Μόνο εάν υπάρχει διαμάχη καλείται ο πυρήνας Linux για να βάλει το νήμα σε κατάσταση ύπνου.",
        "funFacts": [
            "Σχεδιάστηκε από τους Rusty Russell, Ulrich Drepper και Ingo Molnar.",
            "Όλες οι υλοποιήσεις pthread_mutex_t στη βιβλιοθήκη glibc του Linux βασίζονται εσωτερικά σε futexes."
        ],
        "source": "https://en.wikipedia.org/wiki/Futex",
        "tags": ["technology", "operating_systems", "linux", "concurrency"]
    },
    {
        "id": "tech_hard_332",
        "text": "Ποιος μηχανισμός του πυρήνα Linux αντιστοιχίζει έναν εικονικό κοινόχρηστο χώρο μνήμης σε κάθε διεργασία χρήστη ώστε κλήσεις όπως η gettimeofday() να εκτελούνται χωρίς context switch στον πυρήνα;",
        "correct": "vDSO (virtual Dynamic Shared Object)",
        "distractors": ["VFS (Virtual File System)", "POSIX Shared Memory", "Kernel Ring Buffer"],
        "explanation": "Το vDSO παρέχει ένα σύνολο ασφαλών συναρτήσεων πυρήνα απευθείας στο χώρο διευθύνσεων του χρήστη, επιτρέποντας την ανάγνωση του χρόνου ή του TSC χωρίς το κόστος εναλλαγής καταστάσεων του επεξεργαστή.",
        "funFacts": [
            "Αντικατέστησε τον παλαιότερο μηχανισμό vsyscall που είχε σταθερές διευθύνσεις μνήμης και αποτελούσε κίνδυνο ασφαλείας για υπερχείλιση buffer.",
            "Χάρη στο vDSO, η μέτρηση του χρόνου στο Linux είναι έως και 20 φορές ταχύτερη από μια κανονική κλήση συστήματος."
        ],
        "source": "https://en.wikipedia.org/wiki/VDSO",
        "tags": ["technology", "operating_systems", "linux", "vdso"]
    },
    {
        "id": "tech_hard_333",
        "text": "Ποια πρωτοποριακή τεχνική συγχρονισμού χωρίς κλειδώματα (lockless) χρησιμοποιεί εντατικά ο πυρήνας Linux, επιτρέποντας σε αναγνώστες να διαβάζουν δομές δεδομένων χωρίς κλείδωμα ενώ ένας εγγραφέας ενημερώνει αντίγραφο;",
        "correct": "Read-Copy-Update (RCU)",
        "distractors": ["Hazard Pointers", "Software Transactional Memory", "Epoch-based Reclamation"],
        "explanation": "Στο RCU, οι αναγνώστες δεν χρησιμοποιούν ποτέ locks ή ατομικές εντολές διαύλου. Ο εγγραφέας τροποποιεί ένα αντίγραφο, αλλάζει τον δείκτη και περιμένει μια 'περίοδο χάριτος' (grace period) πριν αποδεσμεύσει την παλιά μνήμη.",
        "funFacts": [
            "Προτάθηκε και εξελίχθηκε από τον Paul E. McKenney και ενσωματώθηκε στον πυρήνα Linux 2.6.",
            "Είναι υπεύθυνο για την εξαιρετική κλιμακωσιμότητα του δικτυακού υποσυστήματος και της δρομολόγησης του Linux σε υπερυπολογιστές με χιλιάδες πυρήνες."
        ],
        "source": "https://en.wikipedia.org/wiki/Read-copy-update",
        "tags": ["technology", "operating_systems", "linux", "rcu", "concurrency"]
    },
    {
        "id": "tech_hard_334",
        "text": "Ποιος τύπος κλειδώματος επιτρέπει στους αναγνώστες να διαβάζουν χωρίς κλείδωμα ελέγχοντας έναν μετρητή ακολουθίας πριν και μετά την ανάγνωση για να διαπιστώσουν αν μεσολάβησε εγγραφή;",
        "correct": "Κλείδωμα Ακολουθίας (Seqlock)",
        "distractors": ["Spinlock", "Mutex", "Semaphore"],
        "explanation": "Στο seqlock, ο συγγραφέας αυξάνει έναν ακέραιο μετρητή κατά την έναρξη (καθιστώντας τον περιττό) και κατά τη λήξη (καθιστώντας τον άρτιο). Αν ο αναγνώστης δει περιττό νούμερο ή διαφορετική τιμή στο τέλος, απλώς επαναλαμβάνει την ανάγνωση.",
        "funFacts": [
            "Οι seqlocks δίνουν απόλυτη προτεραιότητα στον εγγραφέα, πράγμα που σημαίνει ότι ο συγγραφέας δεν περιμένει ποτέ τους αναγνώστες.",
            "Χρησιμοποιούνται στον πυρήνα Linux για την ανάγνωση των μεταβλητών jiffies και των ρολογιών συστήματος."
        ],
        "source": "https://en.wikipedia.org/wiki/Seqlock",
        "tags": ["technology", "operating_systems", "concurrency", "seqlock"]
    },
    {
        "id": "tech_hard_335",
        "text": "Ποιος μηχανισμός ασφαλείας του υποσυστήματος eBPF στον πυρήνα Linux αναλύει στατικά το bytecode πριν από την εκτέλεση για να εγγυηθεί ότι το πρόγραμμα δεν θα πέσει σε ατέρμονα βρόχο και δεν θα παραβιάσει τη μνήμη;",
        "correct": "eBPF Verifier (Επαληθευτής eBPF)",
        "distractors": ["eBPF JIT Compiler", "eBPF Sandbox", "eBPF Watchdog"],
        "explanation": "Ο verifier εκτελεί αφηρημένη προσομοίωση όλων των πιθανών διαδρομών εκτέλεσης (Directed Acyclic Graph) του κώδικα eBPF, απορρίπτοντας οποιοδήποτε πρόγραμμα περιέχει μη ασφαλείς προσβάσεις μνήμης ή μη οριοθετημένους βρόχους.",
        "funFacts": [
            "Ο verifier θέτει αυστηρό ανώτατο όριο στον αριθμό των εντολών που αναλύει (μέχρι 1 εκατομμύριο καταστάσεις) για να αποτρέψει επιθέσεις άρνησης εξυπηρέτησης στον πυρήνα.",
            "Επιτρέπει την ασφαλή εκτέλεση κώδικα που παρέχεται από χρήστες απευθείας μέσα στο χώρο του πυρήνα χωρίς ανάγκη φόρτωσης kernel modules."
        ],
        "source": "https://en.wikipedia.org/wiki/EBPF",
        "tags": ["technology", "operating_systems", "ebpf", "linux", "security"]
    },
    {
        "id": "tech_hard_336",
        "text": "Ποιο μέτρο μετριασμού υλοποιήθηκε στα λειτουργικά συστήματα για την αντιμετώπιση της ευπάθειας Meltdown, διαχωρίζοντας πλήρως τους πίνακες σελίδων του χώρου χρήστη από τον χώρο πυρήνα;",
        "correct": "Kernel Page-Table Isolation (KPTI)",
        "distractors": ["Address Space Randomization (ASLR)", "Retpoline", "Speculative Store Bypass Disable"],
        "explanation": "Το KPTI (αρχικά γνωστό ως KAISER) αποτρέπει την ανάγνωση της μνήμης του πυρήνα μέσω εικαστικής εκτέλεσης (Meltdown), αφαιρώντας τη μνήμη πυρήνα από τον πίνακα σελίδων όσο εκτελείται κώδικας χρήστη.",
        "funFacts": [
            "Προκάλεσε αρχικά πτώση απόδοσης 5% έως 30% σε εφαρμογές με πολλές κλήσεις συστήματος, καθώς κάθε μετάβαση στον πυρήνα απαιτεί πλέον εναλλαγή CR3 και TLB flush.",
            "Επεξεργαστές με υποστήριξη PCID (Process-Context Identifiers) μείωσαν σημαντικά το κόστος απόδοσης του KPTI."
        ],
        "source": "https://en.wikipedia.org/wiki/Kernel_page-table_isolation",
        "tags": ["technology", "security", "kpti", "meltdown", "cpu"]
    },
    {
        "id": "tech_hard_337",
        "text": "Ποια τεχνική λογισμικού επινόησε ο Paul Turner της Google για να προστατεύσει προγράμματα από την ευπάθεια Spectre Variant 2 (branch target injection) αντικαθιστώντας τα έμμεσα άλματα με ειδικές ακολουθίες εντολών επιστροφής;",
        "correct": "Retpoline (Return Trampoline)",
        "distractors": ["Shadow Stack", "ROP Chain", "Jump Pad"],
        "explanation": "Το Retpoline χρησιμοποιεί μια ειδικά κατασκευασμένη εντολή CALL και PAUSE που παγιδεύει τον εικαστικό προβλεπτή διακλαδώσεων σε έναν ακίνδυνο ατέρμονα βρόχο μέχρι να επιλυθεί η πραγματική διεύθυνση επιστροφής.",
        "funFacts": [
            "Το όνομα 'retpoline' είναι λογοπαίγνιο μεταξύ του 'return' και του 'trampoline'.",
            "Υιοθετήθηκε άμεσα από όλους τους μεγάλους μεταγλωττιστές (GCC, Clang, MSVC) και από τους πυρήνες Linux και Windows."
        ],
        "source": "https://en.wikipedia.org/wiki/Retpoline",
        "tags": ["technology", "security", "spectre", "retpoline", "cpu"]
    },
    {
        "id": "tech_hard_338",
        "text": "Ποια τεχνική διαμόρφωσης κυκλοφορίας (traffic engineering) χρησιμοποιούν οι μηχανικοί δικτύων στο πρωτόκολλο BGP εισάγοντας πολλαπλές φορές το δικό τους αυτόνομο σύστημα στη διαδρομή για να αποτρέψουν εισερχόμενη κίνηση;",
        "correct": "AS-Path Prepending",
        "distractors": ["Route Poisoning", "Split Horizon", "Hold-Down Timers"],
        "explanation": "Επειδή το BGP προτιμά διαδρομές με μικρότερο μήκος AS-Path, ένας διαχειριστής δικτύου προσθέτει τεχνητά το δικό του Autonomous System Number πολλές φορές, κάνοντας τη γραμμή να φαίνεται λιγότερο ελκυστική.",
        "funFacts": [
            "Αν και δημοφιλής μέθοδος, συχνά αγνοείται αν οι γειτονικοί πάροχοι εφαρμόζουν πολιτικές Local Preference, οι οποίες υπερισχύουν του μήκους AS-Path.",
            "Το AS-Path Prepending μπορεί να αυξήσει άσκοπα το μέγεθος του παγκόσμιου πίνακα δρομολόγησης BGP (DFZ)."
        ],
        "source": "https://en.wikipedia.org/wiki/Border_Gateway_Protocol",
        "tags": ["technology", "networking", "bgp", "routing"]
    },
    {
        "id": "tech_hard_339",
        "text": "Ποιο χαρακτηριστικό (attribute) στο πρωτόκολλο BGP εξετάζεται πρώτο κατά τη διαδικασία επιλογής της καλύτερης διαδρομής (BGP Best Path Selection) σε έναν δρομολογητή;",
        "correct": "Weight (στη Cisco) / Local Preference (στο πρότυπο)",
        "distractors": ["AS-Path Length", "Origin Code", "MED (Multi-Exit Discriminator)"],
        "explanation": "Στον επίσημο αλγόριθμο BGP, το Local Preference είναι το πρώτο τυποποιημένο κριτήριο (υψηλότερη τιμή κερδίζει). Σε συσκευές Cisco, το ιδιοταγές χαρακτηριστικό Weight έχει ακόμη υψηλότερη προτεραιότητα τοπικά.",
        "funFacts": [
            "Το Local Preference μεταδίδεται αποκλειστικά εντός του ίδιου αυτόνομου συστήματος μέσω iBGP και δεν διαφημίζεται ποτέ σε εξωτερικούς eBGP γείτονες.",
            "Η προεπιλεγμένη τιμή Local Preference είναι συνήθως 100."
        ],
        "source": "https://en.wikipedia.org/wiki/BGP_attributes#Local_preference",
        "tags": ["technology", "networking", "bgp", "routing"]
    },
    {
        "id": "tech_hard_340",
        "text": "Ποιο μη μεταβατικό χαρακτηριστικό του BGP χρησιμοποιείται από ένα αυτόνομο σύστημα για να υποδείξει σε έναν εξωτερικό γείτονα ποια είσοδος είναι προτιμότερη όταν υπάρχουν πολλαπλοί σύνδεσμοι μεταξύ τους;",
        "correct": "Multi-Exit Discriminator (MED)",
        "distractors": ["Community String", "Atomic Aggregate", "Aggregator ID"],
        "explanation": "Το MED (γνωστό και ως BGP Metric) προτείνει στον γειτονικό πάροχο ποιο σημείο εισόδου να προτιμήσει (χαμηλότερη τιμή κερδίζει), αλλά ο γείτονας δεν είναι υποχρεωμένος να το σεβαστεί.",
        "funFacts": [
            "Το MED δεν μεταδίδεται πέρα από το γειτονικό AS (non-transitive).",
            "Αν δύο διαδρομές προέρχονται από διαφορετικά αυτόνομα συστήματα, οι δρομολογητές BGP από προεπιλογή δεν συγκρίνουν τις τιμές MED τους, εκτός αν ενεργοποιηθεί η εντολή bgp always-compare-med."
        ],
        "source": "https://en.wikipedia.org/wiki/BGP_attributes#Multi-exit_discriminator",
        "tags": ["technology", "networking", "bgp", "med"]
    },
    {
        "id": "tech_hard_341",
        "text": "Ποια επέκταση του πρωτοκόλλου TCP (RFC 2018) επιτρέπει στον παραλήπτη να ενημερώνει τον αποστολέα για όλα τα μεμονωμένα πακέτα που έλαβε επιτυχώς, αποτρέποντας την άσκοπη επανεκπομπή ολόκληρου του παραθύρου;",
        "correct": "TCP SACK (Selective Acknowledgment)",
        "distractors": ["TCP ECN (Explicit Congestion Notification)", "TCP Nagle Algorithm", "TCP Fast Open"],
        "explanation": "Χωρίς SACK, το TCP χρησιμοποιεί μόνο σωρευτικές επιβεβαιώσεις (cumulative ACKs). Με το SACK, ο αποστολέας μαθαίνει ακριβώς ποια τμήματα χάθηκαν και επανεκπέμπει μόνο αυτά.",
        "funFacts": [
            "Βελτίωσε θεαματικά την απόδοση του Διαδικτύου σε συνδέσεις με υψηλή απώλεια πακέτων, όπως δορυφορικά και ασύρματα δίκτυα.",
            "Τα μπλοκ SACK μεταφέρονται μέσα στο πεδίο TCP Options της κεφαλίδας, χωρώντας έως 4 μη συνεχόμενα διαστήματα ληφθέντων bytes."
        ],
        "source": "https://en.wikipedia.org/wiki/TCP_Selective_Acknowledgment",
        "tags": ["technology", "networking", "tcp", "sack"]
    },
    {
        "id": "tech_hard_342",
        "text": "Ποιος πρωτοποριακός αλγόριθμος ελέγχου συμφόρησης TCP αναπτύχθηκε από την Google το 2016, ρυθμίζοντας τον ρυθμό αποστολής με βάση το Bottleneck Bandwidth και το Round-Trip Time αντί για τις απώλειες πακέτων;",
        "correct": "BBR (Bottleneck Bandwidth and RTT)",
        "distractors": ["TCP Cubic", "TCP Reno", "TCP Westwood"],
        "explanation": "Σε αντίθεση με αλγορίθμους όπως το Reno και το Cubic που μειώνουν την ταχύτητα μόνο όταν χαθούν πακέτα, το BBR κατασκευάζει ένα ρητό μοντέλο του καναλιού και διατηρεί τους buffers των routers άδειους.",
        "funFacts": [
            "Η εφαρμογή του BBR στο YouTube αύξησε τη μέση παγκόσμια ταχύτητα ροής βίντεο κατά 4% και σε ορισμένες χώρες κατά πάνω από 14%.",
            "Αποτρέπει πλήρως το φαινόμενο Bufferbloat σε οικιακά και διηπειρωτικά δίκτυα."
        ],
        "source": "https://en.wikipedia.org/wiki/BBR_(congestion_control)",
        "tags": ["technology", "networking", "tcp", "bbr", "google"]
    },
    {
        "id": "tech_hard_343",
        "text": "Πώς ονομάζεται το φαινόμενο στα δίκτυα υπολογιστών όπου οι υπερβολικά μεγάλοι buffers στους δρομολογητές γεμίζουν με πακέτα, προκαλώντας τεράστια αύξηση στην καθυστέρηση (latency) χωρίς αύξηση στη διαμεταγωγή;",
        "correct": "Bufferbloat",
        "distractors": ["Jitter", "Packet Loss Storm", "Head-of-Line Blocking"],
        "explanation": "Το Bufferbloat συμβαίνει όταν αλγόριθμοι TCP γεμίζουν ακατάσχετα τους buffers των routers, μετατρέποντας μια σύνδεση με φυσικό latency 20ms σε εφιάλτη 1500ms καθυστέρησης.",
        "funFacts": [
            "Ο όρος καθιερώθηκε το 2010 από τον ερευνητή δικτύων Jim Gettys.",
            "Επιλύθηκε οριστικά με σύγχρονους αλγορίθμους Active Queue Management (AQM) όπως το CoDel και το fq_codel."
        ],
        "source": "https://en.wikipedia.org/wiki/Bufferbloat",
        "tags": ["technology", "networking", "bufferbloat", "latency"]
    },
    {
        "id": "tech_hard_344",
        "text": "Ποιος σοβαρός κίνδυνος ασφαλείας απειλεί τη λειτουργία 0-RTT Connection Resumption στο πρωτόκολλο QUIC και στο TLS 1.3, απαιτώντας ειδική μέριμνα από τις εφαρμογές;",
        "correct": "Επίθεση Επανάληψης (Replay Attack)",
        "distractors": ["Επίθεση Man-in-the-Middle", "Αποκρυπτογράφηση Master Key", "Επίθεση Padding Oracle"],
        "explanation": "Στο 0-RTT, τα δεδομένα εφαρμογής στέλνονται πριν ολοκληρωθεί η νέα χειραψία. Ένας επιτιθέμενος μπορεί να υποκλέψει τα πακέτα 0-RTT και να τα αναμεταδώσει (replay) στον διακομιστή.",
        "funFacts": [
            "Για τον λόγο αυτό, τα πρότυπα IETF απαγορεύουν αυστηρά τη χρήση μη-αμετάβλητων αιτημάτων HTTP (όπως POST πληρωμής) μέσα σε δεδομένα 0-RTT.",
            "Τα ασφαλή συστήματα χρησιμοποιούν anti-replay mechanisms όπως strike-registers και monotic timestamps."
        ],
        "source": "https://en.wikipedia.org/wiki/QUIC",
        "tags": ["technology", "networking", "quic", "security"]
    },
    {
        "id": "tech_hard_345",
        "text": "Ποιο θεώρημα κατανεμημένων συστημάτων, που διατύπωσε ο Eric Brewer το 2000, αποδεικνύει ότι είναι αδύνατο ένα κατανεμημένο σύστημα δεδομένων να παρέχει ταυτόχρονα Συνέπεια (Consistency), Διαθεσιμότητα (Availability) και Ανοχή Κατάτμησης (Partition Tolerance);",
        "correct": "Θεώρημα CAP (CAP Theorem)",
        "distractors": ["Θεώρημα FLP", "Θεώρημα PACELC", "Θεώρημα Shannon"],
        "explanation": "Σε ένα πραγματικό δίκτυο η κατάτμηση (Partition) είναι αναπόφευκτη λόγω βλαβών, επομένως ένα κατανεμημένο σύστημα πρέπει να επιλέξει αναγκαστικά είτε μεταξύ Συνέπειας (CP) είτε μεταξύ Διαθεσιμότητας (AP).",
        "funFacts": [
            "Το θεώρημα αποδείχθηκε αυστηρά μαθηματικά το 2002 από τους Seth Gilbert και Nancy Lynch του MIT.",
            "Βάσεις δεδομένων όπως το Cassandra επέλεξαν AP, ενώ συστήματα όπως το Google Spanner και το HBase επέλεξαν CP."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%98%CE%B5%CF%8E%CF%81%CE%B7%CE%BC%CE%B1_CAP",
        "tags": ["technology", "distributed_systems", "cap_theorem", "databases"]
    },
    {
        "id": "tech_hard_346",
        "text": "Ποια επέκταση του θεωρήματος CAP διατύπωσε ο Daniel Abadi το 2012, περιγράφοντας τους συμβιβασμούς ενός συστήματος όχι μόνο κατά τη διάρκεια κατάτμησης αλλά και υπό κανονικές συνθήκες (Latency vs Consistency);",
        "correct": "Θεώρημα PACELC",
        "distractors": ["Θεώρημα FLP Impossibility", "Αξίωμα Lamport", "Μοντέλο Raft"],
        "explanation": "Το PACELC δηλώνει: If there is a Partition (P), choose Availability (A) or Consistency (C); Else (E), choose Latency (L) or Consistency (C).",
        "funFacts": [
            "Εξηγεί γιατί ακόμη και όταν δεν υπάρχει καμία βλάβη δικτύου, συστήματα όπως το DynamoDB θυσιάζουν τη συνέπεια για χάρη της ταχύτητας απόκρισης (χαμηλό latency).",
            "Αποτελεί τον πληρέστερο οδηγό αξιολόγησης αρχιτεκτονικής NoSQL και NewSQL βάσεων δεδομένων."
        ],
        "source": "https://en.wikipedia.org/wiki/PACELC_theorem",
        "tags": ["technology", "distributed_systems", "pacelc", "databases"]
    },
    {
        "id": "tech_hard_347",
        "text": "Ποιος ιστορικός αλγόριθμος αμοιβαίου αποκλεισμού, που επινόησε ο Leslie Lamport το 1974, επιλύει το πρόβλημα κρίσιμης περιοχής για N νήματα χωρίς να απαιτεί καμία εντολή υλικού τύπου Test-and-Set ή CAS;",
        "correct": "Αλγόριθμος του Αρτοποιείου (Lamport's Bakery Algorithm)",
        "distractors": ["Αλγόριθμος του Peterson", "Αλγόριθμος του Dekker", "Σηματοφορείς του Dijkstra"],
        "explanation": "Ο αλγόριθμος προσομοιώνει ένα παραδοσιακό αρτοποιείο όπου κάθε πελάτης (νήμα) παίρνει έναν αριθμό προτεραιότητας κατά την είσοδό του και εξυπηρετείται αυτός με τον μικρότερο αριθμό.",
        "funFacts": [
            "Ο Lamport δήλωσε ότι εμπνεύστηκε τον αλγόριθμο παρατηρώντας τη σειρά εξυπηρέτησης σε ένα ιταλικό αρτοποιείο.",
            "Είναι αξιοσημείωτος επειδή αποδεικνύει ότι ο αμοιβαίος αποκλεισμός είναι εφικτός καθαρά σε επίπεδο λογισμικού με απλές ατομικές αναγνώσεις και εγγραφές μνήμης."
        ],
        "source": "https://en.wikipedia.org/wiki/Lamport%27s_bakery_algorithm",
        "tags": ["technology", "concurrency", "algorithms", "lamport"]
    },
    {
        "id": "tech_hard_348",
        "text": "Ποια λογική δομή χρονισμού σε κατανεμημένα συστήματα, που επινόησαν ανεξάρτητα οι Colin Fidge και Friedemann Mattern το 1988, επιτρέπει τον καθορισμό της αιτιώδους σχέσης (causal ordering) μεταξύ συμβάντων;",
        "correct": "Διανυσματικά Ρολόγια (Vector Clocks)",
        "distractors": ["Λογικά Ρολόγια Lamport", "Ρολόγια TrueTime", "Σφραγίδες Hybrid Logical Clocks"],
        "explanation": "Σε αντίθεση με τα απλά ρολόγια Lamport που προσφέρουν μόνο μερική διάταξη, τα Vector Clocks διατηρούν ένα διάνυσμα με τις καταστάσεις όλων των κόμβων, επιτρέποντας την ανίχνευση ταυτόχρονων (concurrent) συγκρουόμενων γεγονότων.",
        "funFacts": [
            "Χρησιμοποιούνται από συστήματα αποθήκευσης όπως το Amazon Dynamo για την ανίχνευση συγκρούσεων σε εκδόσεις αντικειμένων.",
            "Το κύριο μειονέκτημά τους είναι ότι το μέγεθος του διανύσματος αυξάνεται γραμμικά με τον αριθμό των κόμβων στο δίκτυο."
        ],
        "source": "https://en.wikipedia.org/wiki/Vector_clock",
        "tags": ["technology", "distributed_systems", "vector_clocks", "concurrency"]
    },
    {
        "id": "tech_hard_349",
        "text": "Ποιος διάσημος αλγόριθμος κατανεμημένων συστημάτων επιτρέπει τη λήψη ενός συνεπή παγκόσμιου στιγμιότυπου (consistent global snapshot) χωρίς να παγώσει η λειτουργία και οι επικοινωνίες του συστήματος;",
        "correct": "Αλγόριθμος Chandy-Lamport",
        "distractors": ["Αλγόριθμος Paxos", "Αλγόριθμος Bully", "Αλγόριθμος Ricart-Agrawala"],
        "explanation": "Ο αλγόριθμος Chandy-Lamport χρησιμοποιεί ειδικά μηνύματα δείκτη (marker messages) που κυκλοφορούν στα κανάλια FIFO για να καταγράψει τόσο την τοπική κατάσταση κάθε διεργασίας όσο και τα μηνύματα που βρίσκονται εν πτήσει στα κανάλια.",
        "funFacts": [
            "Δημοσιεύτηκε το 1985 από τους K. Mani Chandy και Leslie Lamport.",
            "Αποτελεί τη θεωρητική βάση για τα κατανεμημένα checkpoints και την ανάκαμψη από σφάλματα σε συστήματα ροής δεδομένων όπως το Apache Flink."
        ],
        "source": "https://en.wikipedia.org/wiki/Chandy%E2%80%93Lamport_algorithm",
        "tags": ["technology", "distributed_systems", "chandy_lamport", "algorithms"]
    },
    {
        "id": "tech_hard_350",
        "text": "Ποιος αλγόριθμος κατανεμημένης συναίνεσης σχεδιάστηκε από τους Diego Ongaro και John Ousterhout στο Stanford το 2014 ειδικά ως μια πιο κατανοητή και πρακτική εναλλακτική στον κλασικό Paxos;",
        "correct": "Raft",
        "distractors": ["Zab", "Viewstamped Replication", "Byzantine Fault Tolerance"],
        "explanation": "Ο Raft διαχωρίζει τη συναίνεση σε διακριτά ανεξάρτητα υποπροβλήματα: εκλογή ηγέτη (Leader Election), αναπαραγωγή ημερολογίου (Log Replication) και ασφάλεια (Safety).",
        "funFacts": [
            "Χρησιμοποιείται σήμερα στον πυρήνα του etcd (το θεμέλιο του Kubernetes), του HashiCorp Consul και του TiKV.",
            "Δημιουργήθηκε επειδή οι ερευνητές διαπίστωσαν ότι σχεδόν κανείς φοιτητής ή μηχανικός δεν μπορούσε να κατανοήσει και να υλοποιήσει σωστά τον Paxos."
        ],
        "source": "https://en.wikipedia.org/wiki/Raft_(algorithm)",
        "tags": ["technology", "distributed_systems", "raft", "consensus"]
    },
    {
        "id": "tech_hard_351",
        "text": "Ποιο καταστροφικό σενάριο σε κατανεμημένα συστήματα συμβαίνει όταν μια διακοπή επικοινωνίας χωρίζει το cluster σε δύο απομονωμένα υποσύνολα και τα δύο πιστεύουν ότι είναι ο νόμιμος ηγέτης, γράφοντας αντικρουόμενα δεδομένα;",
        "correct": "Σύνδρομο Διχοτόμησης Εγκεφάλου (Split-Brain)",
        "distractors": ["Βυζαντινή Βλάβη (Byzantine Failure)", "Αδιέξοδο Δικτύου (Deadlock)", "Κατάρρευση Cascading Failure"],
        "explanation": "Το Split-brain οδηγεί σε άμεση καταστροφή και αλλοίωση δεδομένων. Αντιμετωπίζεται απαιτώντας αυστηρή απαρτία (Quorum = N/2 + 1 κόμβοι) για οποιαδήποτε εγγραφή ή εκλογή ηγέτη.",
        "funFacts": [
            "Για να αποφευχθεί το split-brain, τα clusters απαιτούν σχεδόν πάντα περιττό αριθμό κόμβων (π.χ. 3, 5 ή 7).",
            "Σε συστήματα υψηλής διαθεσιμότητας χρησιμοποιείται επίσης ο μηχανισμός STONITH ('Shoot The Other Node In The Head') για να απενεργοποιεί βίαια τον αποκομμένο κόμβο."
        ],
        "source": "https://en.wikipedia.org/wiki/Split-brain_(computing)",
        "tags": ["technology", "distributed_systems", "split_brain", "high_availability"]
    },
    {
        "id": "tech_hard_352",
        "text": "Ποια ανωμαλία συγχρονισμού συμβαίνει στο επίπεδο απομόνωσης Snapshot Isolation των βάσεων δεδομένων, όπου δύο συναλλαγές διαβάζουν επικαλυπτόμενα δεδομένα και κάνουν ασύνδετες ενημερώσεις που παραβιάζουν έναν γενικό περιορισμό;",
        "correct": "Ανωμαλία Παραμόρφωσης Εγγραφής (Write Skew)",
        "distractors": ["Βρώμικη Ανάγνωση (Dirty Read)", "Μη-Επαναλήψιμη Ανάγνωση (Non-Repeatable Read)", "Ανάγνωση Φάντασμα (Phantom Read)"],
        "explanation": "Στο Write Skew, δύο γιατροί που εφημερεύουν ζητούν ταυτόχρονα άδεια. Και οι δύο βλέπουν ότι υπάρχουν 2 ενεργοί γιατροί (απαιτείται τουλάχιστον 1) και αποχωρούν και οι δύο, αφήνοντας το νοσοκομείο χωρίς γιατρό, παρόλο που καμία συναλλαγή δεν έγραψε στην ίδια εγγραφή.",
        "funFacts": [
            "Αποδεικνύει ότι το Snapshot Isolation δεν ισοδυναμεί με πραγματικό Serializable isolation.",
            "Αντιμετωπίζεται σε σύγχρονες βάσεις δεδομένων (όπως η PostgreSQL) με το Serializable Snapshot Isolation (SSI)."
        ],
        "source": "https://en.wikipedia.org/wiki/Snapshot_isolation",
        "tags": ["technology", "databases", "acid", "write_skew"]
    },
    {
        "id": "tech_hard_353",
        "text": "Ποιο επίπεδο απομόνωσης ANSI SQL απαιτείται αυστηρά για να αποτραπεί το φαινόμενο των 'Αναγνώσεων-Φαντασμάτων' (Phantom Reads), όπου μια νέα εγγραφή εισάγεται από άλλη συναλλαγή και ικανοποιεί το ίδιο κριτήριο αναζήτησης;",
        "correct": "Serializable",
        "distractors": ["Repeatable Read", "Read Committed", "Read Uncommitted"],
        "explanation": "Το επίπεδο Serializable αποτρέπει πλήρως τα phantoms χρησιμοποιώντας κλειδώματα εύρους δεικτών (Predicate Locks ή Range Locks), διασφαλίζοντας ότι το αποτέλεσμα είναι ταυτόσημο με σειριακή εκτέλεση των συναλλαγών.",
        "funFacts": [
            "Αν και το Repeatable Read αποτρέπει την αλλαγή υπαρχόντων εγγραφών, στο πρότυπο ANSI SQL δεν εγγυάται την αποτροπή εισαγωγής νέων εγγραφών.",
            "Στην πράξη, πολλές βάσεις δεδομένων χρησιμοποιούν ως προεπιλογή το Read Committed για λόγους απόδοσης."
        ],
        "source": "https://en.wikipedia.org/wiki/Isolation_(database_systems)#Phantom_reads",
        "tags": ["technology", "databases", "sql", "acid"]
    },
    {
        "id": "tech_hard_354",
        "text": "Ποια είναι η θεμελιώδης διαφορά μεταξύ του Two-Phase Locking (2PL) και του Two-Phase Commit (2PC);",
        "correct": "Το 2PL αφορά τον έλεγχο ταυτοχρονισμού σε έναν κόμβο, ενώ το 2PC αφορά την ατομικότητα συναλλαγών σε πολλούς κατανεμημένους κόμβους",
        "distractors": [
            "Το 2PL χρησιμοποιείται μόνο σε NoSQL βάσεις, ενώ το 2PC σε σχεσιακές βάσεις",
            "Το 2PL είναι αλγόριθμος χωρίς κλειδώματα, ενώ το 2PC χρησιμοποιεί spinlocks",
            "Το 2PC διαχειρίζεται την κρυφή μνήμη της CPU, ενώ το 2PL τους δίσκους SSD"
        ],
        "explanation": "Παρά το παρόμοιο όνομα, το Two-Phase Locking εγγυάται σειριοποιησιμότητα αποκτώντας και απελευθερώνοντας κλειδώματα, ενώ το Two-Phase Commit είναι πρωτόκολλο κατανεμημένης συναίνεσης (Prepare / Commit) για διασφάλιση ατομικότητας (All-or-Nothing).",
        "funFacts": [
            "Είναι μια από τις πιο συχνές παρανοήσεις σε συνεντεύξεις αρχιτεκτονικής λογισμικού.",
            "Το βασικό πρόβλημα του κλασικού 2PC είναι ότι είναι πρωτόκολλο αποκλεισμού (blocking): αν ο συντονιστής καταρρεύσει στη φάση prepare, οι κόμβοι μένουν κλειδωμένοι επ' αόριστον."
        ],
        "source": "https://en.wikipedia.org/wiki/Two-phase_commit_protocol",
        "tags": ["technology", "databases", "concurrency", "distributed_systems"]
    },
    {
        "id": "tech_hard_355",
        "text": "Ποια δομή δεδομένων αποθήκευσης, που επινόησαν οι Patrick O'Neil, Edward O'Neil και Gerhard Weikum το 1996, βελτιστοποιεί τις εγγραφές μετατρέποντας τυχαίες εγγραφές σε σειριακές και χρησιμοποιείται σε Big Data βάσεις όπως RocksDB και Cassandra;",
        "correct": "Log-Structured Merge-tree (LSM-Tree)",
        "distractors": ["B+ Tree", "R-Tree", "Radix Tree"],
        "explanation": "Το LSM-Tree δέχεται εγγραφές πρώτα σε μια ταξινομημένη δομή μνήμης (MemTable) και ένα log προσαρτήσεων (WAL), και στη συνέχεια αδειάζει τα δεδομένα στο δίσκο σε αμετάβλητα αρχεία SSTables μέσω περιοδικής συγχώνευσης (compaction).",
        "funFacts": [
            "Υπερέχει δραματικά των B-Trees σε ρυθμό εγγραφών, αλλά εισάγει το φαινόμενο του 'Write Amplification' λόγω των διαρκών επανασυγχωνεύσεων.",
            "Αποτελεί την καρδιά μηχανών αποθήκευσης όπως το LevelDB της Google και το RocksDB της Meta."
        ],
        "source": "https://en.wikipedia.org/wiki/Log-structured_merge-tree",
        "tags": ["technology", "databases", "data_structures", "lsm_tree"]
    },
    {
        "id": "tech_hard_356",
        "text": "Ποια πιθανοτική δομή δεδομένων που επινόησε ο Burton Howard Bloom το 1970 ελέγχει αν ένα στοιχείο ανήκει σε ένα σύνολο, έχοντας μηδενικά ψευδώς αρνητικά αποτελέσματα αλλά πιθανότητα ψευδώς θετικών;",
        "correct": "Φίλτρο Bloom (Bloom Filter)",
        "distractors": ["HyperLogLog", "Count-Min Sketch", "Cuckoo Filter"],
        "explanation": "Ένα Bloom filter χρησιμοποιεί έναν πίνακα bits και k ανεξάρτητες συναρτήσεις κατακερματισμού. Αν επιστρέψει 'όχι', το στοιχείο σίγουρα δεν υπάρχει. Αν επιστρέψει 'ναι', υπάρχει ισχυρή πιθανότητα να υπάρχει.",
        "funFacts": [
            "Οι βάσεις δεδομένων (π.χ. Cassandra, RocksDB) το χρησιμοποιούν για να αποφύγουν ακριβές αναζητήσεις SSTable στο δίσκο για κλειδιά που δεν υπάρχουν.",
            "Ο βέλτιστος αριθμός συναρτήσεων κατακερματισμού δίνεται από τον τύπο k = (m/n) * ln(2)."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloom_filter",
        "tags": ["technology", "data_structures", "bloom_filter", "algorithms"]
    },
    {
        "id": "tech_hard_357",
        "text": "Ποια πιθανοτική δομή δεδομένων συνεχούς ροής (streaming), που πρότειναν οι Cormode και Muthukrishnan το 2005, χρησιμοποιεί δισδιάστατο πίνακα μετρητών για εκτίμηση της συχνότητας εμφάνισης στοιχείων σε υπογραμμικό χώρο μνήμης;",
        "correct": "Count-Min Sketch",
        "distractors": ["HyperLogLog", "Reservoir Sampling", "Treap"],
        "explanation": "Το Count-Min Sketch λειτουργεί σαν ένας πιθανοτικός πίνακας κατακερματισμού που μπορεί να εκτιμήσει τη συχνότητα στοιχείων σε τεράστιες ροές δεδομένων δικτύου χωρίς να αποθηκεύει τα ίδια τα στοιχεία.",
        "funFacts": [
            "Χρησιμοποιείται σε δρομολογητές κορμού και συστήματα DDoS για τον εντοπισμό 'heavy hitters' (διευθύνσεων IP που καταναλώνουν υπερβολικό bandwidth).",
            "Η εκτίμηση συχνότητας που επιστρέφει είναι εγγυημένα μεγαλύτερη ή ίση με την πραγματική (δεν υποτιμά ποτέ τη συχνότητα)."
        ],
        "source": "https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch",
        "tags": ["technology", "algorithms", "data_structures", "streaming"]
    },
    {
        "id": "tech_hard_358",
        "text": "Ποιος αλγόριθμος εκτίμησης πληθικότητας (cardinality estimation), που εισήγαγαν οι Flajolet et al. το 2007, επιτρέπει τη μέτρηση δισεκατομμυρίων μοναδικών στοιχείων με σφάλμα κάτω από 1% χρησιμοποιώντας μόλις 1,5 KB μνήμης;",
        "correct": "HyperLogLog",
        "distractors": ["MinHash", "SimHash", "SkipList"],
        "explanation": "Το HyperLogLog παρατηρεί τον μέγιστο αριθμό συνεχόμενων μηδενικών στην αρχή των κατακερματισμένων δυαδικών τιμών και εφαρμόζει αρμονικό μέσο για να εξαλείψει την επίδραση ακραίων τιμών.",
        "funFacts": [
            "Είναι ενσωματωμένο ως εντολή (PFADD, PFCOUNT) στη Redis.",
            "Χρησιμοποιείται από την Google και το Facebook για να μετρούν πόσοι μοναδικοί χρήστες έκαναν μια αναζήτηση ή είδαν μια διαφήμιση σε πραγματικό χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/HyperLogLog",
        "tags": ["technology", "algorithms", "hyperloglog", "data_structures"]
    },
    {
        "id": "tech_hard_359",
        "text": "Ποια παραλλαγή του φίλτρου Bloom επιτρέπει τόσο τη διαγραφή στοιχείων όσο και υψηλότερη αξιοποίηση χώρου, χρησιμοποιώντας cuckoo hashing για την αποθήκευση αποτυπωμάτων (fingerprints);",
        "correct": "Φίλτρο Cuckoo (Cuckoo Filter)",
        "distractors": ["Quotient Filter", "Counting Bloom Filter", "Xor Filter"],
        "explanation": "Το Cuckoo filter αποθηκεύει μικρά fingerprints στοιχείων σε πίνακες χρησιμοποιώντας δύο πιθανές θέσεις cuckoo hashing, επιτρέποντας δυναμική διαγραφή στοιχείων χωρίς να υποβαθμίζεται η δομή.",
        "funFacts": [
            "Επινοήθηκε το 2014 από ερευνητές του Carnegie Mellon (Fan, Andersen, Kaminsky, Mitzenmacher).",
            "Ξεπερνά σε ταχύτητα αναζήτησης και αποδοτικότητα χώρου τα παραδοσιακά Bloom filters όταν απαιτείται χαμηλό false positive rate."
        ],
        "source": "https://en.wikipedia.org/wiki/Cuckoo_filter",
        "tags": ["technology", "data_structures", "cuckoo_filter", "algorithms"]
    },
    {
        "id": "tech_hard_360",
        "text": "Ποιος είναι ο κύριος περιορισμός του πρωτοκόλλου συναίνεσης Paxos που επιλύει η παραλλαγή Multi-Paxos;",
        "correct": "Επιτρέπει τη συμφωνία σε μια συνεχή ακολουθία τιμών (log) παρακάμπτοντας τη φάση Prepare για κάθε τιμή μετά την εκλογή σταθερού ηγέτη",
        "distractors": [
            "Επιλύει το πρόβλημα των βυζαντινών προδοτών σε περιβάλλον χωρίς εμπιστοσύνη",
            "Μειώνει τον απαιτούμενο αριθμό κόμβων απαρτίας σε N/3 αντί για N/2 + 1",
            "Καταργεί την ανάγκη για μη πτητική μνήμη (δίσκο) στους κόμβους"
        ],
        "explanation": "Στον κλασικό Basic Paxos, κάθε μεμονωμένη απόφαση απαιτεί 2 πλήρεις γύρους μηνυμάτων (Prepare/Promise και Propose/Accept). Το Multi-Paxos εκτελεί τη φάση Prepare μία φορά για ολόκληρη τη θητεία ενός ηγέτη, μειώνοντας δραστικά την καθυστέρηση.",
        "funFacts": [
            "Αν και ο Leslie Lamport περιέγραψε συνοπτικά το Multi-Paxos στη διάσημη εργασία του 'The Part-Time Parliament', άφησε πολλές λεπτομέρειες υλοποίησης ανοιχτές, οδηγώντας σε δεκαετίες ερευνών.",
            "Αποτέλεσε τη βάση για το Chubby lock service της Google και το Apache ZooKeeper."
        ],
        "source": "https://en.wikipedia.org/wiki/Paxos_(computer_science)#Multi-Paxos",
        "tags": ["technology", "distributed_systems", "paxos", "consensus"]
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
    print(f"Loaded {len(questions)} questions for technology_hard batch 3 (311-360).")
    validate_and_append("technology", "hard", 5, questions)

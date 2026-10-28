# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "tech_hard_111",
        "text": "Στο θεώρημα CAP του Έρικ Μπρούερ για τα κατανεμημένα συστήματα δεδομένων, ποια τρία χαρακτηριστικά δηλώνεται ότι είναι αδύνατον να εξασφαλιστούν ταυτόχρονα σε περίπτωση κατάτμησης δικτύου;",
        "correct": "Συνέπεια, Διαθεσιμότητα, Ανοχή στην Κατάτμηση (Consistency, Availability, Partition tolerance)",
        "distractors": [
            "Ατομικότητα, Συνέπεια, Απομόνωση",
            "Ταχύτητα, Αξιοπιστία, Επεκτασιμότητα",
            "Ασφάλεια, Ισορροπία, Ανοχή Σφαλμάτων"
        ],
        "explanation": "Το θεώρημα CAP αποδεικνύει ότι όταν συμβαίνει μια αναπόφευκτη διακοπή επικοινωνίας (Partition), ένα κατανεμημένο σύστημα πρέπει να επιλέξει ανάμεσα στη Συνέπεια (όλοι βλέπουν τα ίδια δεδομένα) ή τη Διαθεσιμότητα (όλοι λαμβάνουν απάντηση).",
        "funFacts": [
            "Διατυπώθηκε ως εικασία το 2000 από τον Eric Brewer και αποδείχθηκε τυπικά και μαθηματικά το 2002 από τους Seth Gilbert και Nancy Lynch.",
            "Τα παραδοσιακά σχεσιακά συστήματα (RDBMS) συνήθως επιλέγουν CA, ενώ τα σύγχρονα NoSQL συστήματα επιλέγουν AP (π.χ. Cassandra) ή CP (π.χ. MongoDB)."
        ],
        "source": "https://en.wikipedia.org/wiki/CAP_theorem",
        "tags": ["technology", "distributed_systems", "cap_theorem", "databases"]
    },
    {
        "id": "tech_hard_112",
        "text": "Ποια πιθανοτική δομή δεδομένων (probabilistic data structure) χρησιμοποιείται για τον έλεγχο συμμετοχής ενός στοιχείου σε ένα σύνολο, έχοντας πιθανότητα ψευδώς θετικών αποτελεσμάτων (false positives) αλλά ποτέ ψευδώς αρνητικών;",
        "correct": "Φίλτρο Bloom (Bloom filter)",
        "distractors": ["Πίνακας Κατακερματισμού (Hash Table)", "Δέντρο Merkle", "HyperLogLog"],
        "explanation": "Το φίλτρο Bloom χρησιμοποιεί έναν πίνακα bit και πολλαπλές συναρτήσεις κατακερματισμού (hash functions) για να ελέγχει με εξαιρετικά μικρό χώρο μνήμης εάν ένα στοιχείο 'πιθανόν ανήκει' ή 'σίγουρα δεν ανήκει' στο σύνολο.",
        "funFacts": [
            "Επινοήθηκε από τον Burton Howard Bloom το 1970.",
            "Χρησιμοποιείται εκτεταμένα σε βάσεις δεδομένων όπως η Cassandra και η RocksDB για να αποφεύγονται περιττές και δαπανηρές αναγνώσεις από τον δίσκο εάν ένα κλειδί δεν υπάρχει."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloom_filter",
        "tags": ["technology", "data_structures", "algorithms", "bloom_filter"]
    },
    {
        "id": "tech_hard_113",
        "text": "Ποιος αλγόριθμος συναίνεσης (consensus algorithm), που αναπτύχθηκε από τους Ongaro και Ousterhout στο Στάνφορντ το 2014, σχεδιάστηκε ειδικά για να είναι πιο κατανοητός και εύκολα υλοποιήσιμος από τον Paxos;",
        "correct": "Raft",
        "distractors": ["Zab", "PBFT", "Chubby"],
        "explanation": "Ο Raft επιτυγχάνει συναίνεση σε κατανεμημένα συστήματα διαιρώντας το πρόβλημα σε τρία ανεξάρτητα υποπροβλήματα: εκλογή ηγέτη (Leader Election), αντιγραφή καταγραφής (Log Replication) και ασφάλεια (Safety).",
        "funFacts": [
            "Χρησιμοποιείται ευρέως σε θεμελιώδη σύγχρονα συστήματα υποδομής, όπως το etcd (το 'μυαλό' του Kubernetes) και το Consul της HashiCorp.",
            "Οι κόμβοι στον Raft μπορούν να βρίσκονται σε μία από τρεις καταστάσεις: Leader (Ηγέτης), Follower (Ακόλουθος) ή Candidate (Υποψήφιος)."
        ],
        "source": "https://en.wikipedia.org/wiki/Raft_(algorithm)",
        "tags": ["technology", "distributed_systems", "raft", "consensus"]
    },
    {
        "id": "tech_hard_114",
        "text": "Ποια διάσημη ευπάθεια ασφαλείας επεξεργαστών (CVE-2017-5754), που αποκαλύφθηκε το 2018, εκμεταλλεύεται την κερδοσκοπική εκτέλεση (speculative execution) και τη διαφυγή της μνήμης cache για την ανάγνωση προστατευμένης μνήμης πυρήνα;",
        "correct": "Meltdown",
        "distractors": ["Spectre", "Heartbleed", "Dirty COW"],
        "explanation": "Το Meltdown 'λιώνει' τα όρια ασφαλείας υλικού ανάμεσα στις εφαρμογές χρήστη και το λειτουργικό σύστημα, επιτρέποντας σε μη εξουσιοδοτημένο πρόγραμμα να διαβάσει οποιαδήποτε θέση της μνήμης του υπολογιστή.",
        "funFacts": [
            "Επηρέασε σχεδόν όλους τους επεξεργαστές Intel που κατασκευάστηκαν από το 1995 έως το 2018.",
            "Για την αντιμετώπισή του σε επίπεδο λογισμικού αναπτύχθηκε ο μηχανισμός KPTI (Kernel Page-Table Isolation), ο οποίος διαχωρίζει πλήρως τους πίνακες σελίδων χρήστη και πυρήνα."
        ],
        "source": "https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)",
        "tags": ["technology", "security", "cpu", "vulnerabilities", "hardware"]
    },
    {
        "id": "tech_hard_115",
        "text": "Ποιος αλγόριθμος εκτίμησης πληθικότητας (cardinality estimation) επιτρέπει τον υπολογισμό του αριθμού των μοναδικών στοιχείων σε ένα τεράστιο σύνολο δεδομένων δισεκατομμυρίων εγγραφών με σφάλμα κάτω από 2% χρησιμοποιώντας λιγότερο από 1,5 KB μνήμης;",
        "correct": "HyperLogLog",
        "distractors": ["Count-Min Sketch", "SimHash", "MinHash"],
        "explanation": "Ο HyperLogLog (Flajolet et al., 2007) εκμεταλλεύεται τον αριθμό των συνεχόμενων μηδενικών στην αρχή των κατακερματισμένων δυαδικών τιμών για να συμπεράνει τον συνολικό αριθμό των μοναδικών στοιχείων.",
        "funFacts": [
            "Χρησιμοποιείται από τον Redis (εντολές PFADD, PFCOUNT) και την Google για την καταμέτρηση μοναδικών αναζητήσεων και επισκεπτών σε πραγματικό χρόνο.",
            "Η προηγούμενη έκδοσή του από τον Philippe Flajolet το 1985 ονομαζόταν αλγόριθμος Flajolet–Martin."
        ],
        "source": "https://en.wikipedia.org/wiki/HyperLogLog",
        "tags": ["technology", "algorithms", "big_data", "hyperloglog"]
    },
    {
        "id": "tech_hard_116",
        "text": "Ποια είναι η βασική αρχιτεκτονική δομή αποθήκευσης που χρησιμοποιείται σε βάσεις δεδομένων υψηλής ταχύτητας εγγραφών (όπως LevelDB, RocksDB και Cassandra), αντικαθιστώντας τα παραδοσιακά B-Trees;",
        "correct": "Δέντρο LSM (Log-Structured Merge-Tree)",
        "distractors": ["R-Tree", "B+ Tree", "Radix Tree"],
        "explanation": "Το LSM-Tree μετατρέπει τις τυχαίες εγγραφές δίσκου σε σειριακές εγγράφοντας πρώτα στη μνήμη RAM (MemTable) και στη συνέχεια ξεπλένοντας ταξινομημένα αρχεία στον δίσκο (SSTables) μέσω συγχώνευσης (Compaction).",
        "funFacts": [
            "Επινοήθηκε από τους Patrick O'Neil, Edward O'Neil και Gerhard Weikum το 1996.",
            "Προσφέρει τεράστια απόδοση σε βαριά φόρτα εγγραφών (write throughput), αλλά υποφέρει από το φαινόμενο του 'write amplification' κατά τις διαδικασίες compaction."
        ],
        "source": "https://en.wikipedia.org/wiki/Log-structured_merge-tree",
        "tags": ["technology", "databases", "storage", "lsm_tree"]
    },
    {
        "id": "tech_hard_117",
        "text": "Ποιο σύγχρονο πρωτόκολλο δικτύου επιπέδου μεταφοράς, που αναπτύχθηκε αρχικά από την Google και τυποποιήθηκε από την IETF, λειτουργεί πάνω από UDP και αποτελεί τη βάση του HTTP/3;",
        "correct": "QUIC",
        "distractors": ["SCTP", "DCCP", "SPDY"],
        "explanation": "Το QUIC ενσωματώνει κρυπτογράφηση TLS 1.3 και παρέχει πολλαπλά ανεξάρτητα streams δεδομένων χωρίς το φαινόμενο του 'μπλοκαρίσματος επικεφαλής γραμμής' (Head-of-Line blocking) του TCP.",
        "funFacts": [
            "Μειώνει δραματικά τον χρόνο εγκαθίδρυσης σύνδεσης σε μηδενικό χρόνο (0-RTT) για επαναλαμβανόμενες συνδέσεις.",
            "Επιτρέπει την απρόσκοπτη μεταφορά σύνδεσης (Connection Migration) όταν μια φορητή συσκευή αλλάζει δίκτυο (π.χ. από Wi-Fi σε 4G/5G) χωρίς να διακοπεί η λήψη."
        ],
        "source": "https://en.wikipedia.org/wiki/QUIC",
        "tags": ["technology", "networking", "quic", "http3", "protocols"]
    },
    {
        "id": "tech_hard_118",
        "text": "Ποιο σύστημα παγκόσμιας κατανεμημένης σχεσιακής βάσης δεδομένων της Google χρησιμοποιεί το API 'TrueTime' (με ατομικά ρολόγια και δέκτες GPS) για να εγγυηθεί αυστηρή σειριοποιησιμότητα (Strict Serializability) σε όλο τον κόσμο;",
        "correct": "Google Spanner",
        "distractors": ["Google Bigtable", "CockroachDB", "Amazon Aurora"],
        "explanation": "Το Google Spanner ήταν το πρώτο σύστημα που πέτυχε εξωτερική συνέπεια συναλλαγών (external consistency) σε παγκόσμια κλίμακα, αντιμετωπίζοντας την αβεβαιότητα των ρολογιών με χρονικά παράθυρα αβεβαιότητας TrueTime.",
        "funFacts": [
            "Κάθε κέντρο δεδομένων της Google που φιλοξενεί Spanner διαθέτει τόσο εξειδικευμένους δέκτες GPS όσο και τοπικά ατομικά ρολόγια ρουβιδίου για περιπτώσεις απώλειας δορυφορικού σήματος.",
            "Η αρχιτεκτονική του Spanner περιγράφηκε στο ιστορικό ερευνητικό paper του OSDI το 2012."
        ],
        "source": "https://en.wikipedia.org/wiki/Spanner_(database)",
        "tags": ["technology", "distributed_systems", "google_spanner", "databases"]
    },
    {
        "id": "tech_hard_119",
        "text": "Ποια κβαντική πύλη (quantum gate) ενός qubit δημιουργεί υπέρθεση καταστάσεων μετατρέποντας τη βασική κατάσταση |0⟩ σε (|0⟩ + |1⟩)/√2;",
        "correct": "Πύλη Hadamard (H)",
        "distractors": ["Πύλη Pauli-X", "Πύλη Phase (S)", "Πύλη CNOT"],
        "explanation": "Η πύλη Hadamard αποτελεί τη θεμελιώδη πύλη στον κβαντικό υπολογισμό για τη δημιουργία ίσων υπερθέσεων και χρησιμοποιείται στην έναρξη σχεδόν όλων των κβαντικών αλγορίθμων.",
        "funFacts": [
            "Αν εφαρμοστεί δύο φορές διαδοχικά στο ίδιο qubit, επιστρέφει το qubit στην αρχική του κατάσταση (H² = I, είναι αυτοαντίστροφη).",
            "Πήρε το όνομά της από τον Γάλλο μαθηματικό Ζακ Ανταμάρ (Jacques Hadamard)."
        ],
        "source": "https://en.wikipedia.org/wiki/Quantum_logic_gate#Hadamard_gate",
        "tags": ["technology", "quantum_computing", "qubits", "quantum_gates"]
    },
    {
        "id": "tech_hard_120",
        "text": "Ποιος αλγόριθμος κβαντικού υπολογισμού, που αναπτύχθηκε το 1994 από τον Peter Shor, μπορεί να παραγοντοποιήσει ακέραιους αριθμούς σε πολυωνυμικό χρόνο, απειλώντας την κρυπτογραφία RSA;",
        "correct": "Αλγόριθμος του Shor",
        "distractors": ["Αλγόριθμος του Grover", "Αλγόριθμος Deutsch-Jozsa", "Αλγόριθμος Simon"],
        "explanation": "Ο αλγόριθμος του Shor ανάγει το πρόβλημα της παραγοντοποίησης στην εύρεση περιόδου μιας συνάρτησης χρησιμοποιώντας τον Κβαντικό Μετασχηματισμό Fourier (QFT), επιτυγχάνοντας εκθετική επιτάχυνση σε σχέση με τους κλασικούς υπολογιστές.",
        "funFacts": [
            "Για να σπάσει ένα κλειδί RSA 2048-bit εκτιμάται ότι θα απαιτηθεί ένας κβαντικός υπολογιστής με περίπου 4.000 λογικά (ή εκατομμύρια φυσικά) qubits.",
            "Η απειλή αυτή οδήγησε το NIST στη διεθνή διαδικασία τυποποίησης μετα-κβαντικής κρυπτογραφίας (Post-Quantum Cryptography)."
        ],
        "source": "https://en.wikipedia.org/wiki/Shor%27s_algorithm",
        "tags": ["technology", "quantum_computing", "cryptography", "shors_algorithm"]
    },
    {
        "id": "tech_hard_121",
        "text": "Ποια πρωτοποριακή ελλειπτική καμπύλη (Twisted Edwards curve), που σχεδιάστηκε από τον καθηγητή Daniel J. Bernstein (djb) το 2011, χρησιμοποιείται ευρέως στο σχήμα ψηφιακής υπογραφής Ed25519;",
        "correct": "Curve25519 / Ed25519",
        "distractors": ["secp256k1", "NIST P-256", "Brainpool P256r1"],
        "explanation": "Η Curve25519 σχεδιάστηκε ειδικά για να επιτυγχάνει μέγιστη ταχύτητα, να είναι απρόσβλητη σε επιθέσεις χρονισμού (constant-time execution) και να μην περιέχει ανεξήγητες 'μαγικές σταθερές' όπως οι καμπύλες του NIST.",
        "funFacts": [
            "Χρησιμοποιείται ως προεπιλογή στο πρωτόκολλο SSH, στο Signal, στο WhatsApp και στο Tor.",
            "Η καμπύλη λειτουργεί πάνω από το πρώτο σώμα μεγέθους 2^255 - 19, εξ ου και το όνομά της."
        ],
        "source": "https://en.wikipedia.org/wiki/Curve25519",
        "tags": ["technology", "cryptography", "elliptic_curves", "security"]
    },
    {
        "id": "tech_hard_122",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δρομολόγησης εξωτερικής πύλης (EGP) που αποτελεί τη ραχοκοκαλιά του παγκόσμιου Διαδικτύου, ανταλλάσσοντας πληροφορίες δρομολόγησης μεταξύ Αυτόνομων Συστημάτων (AS);",
        "correct": "BGP (Border Gateway Protocol)",
        "distractors": ["OSPF", "IS-IS", "RIP"],
        "explanation": "Το BGP είναι πρωτόκολλο διανύσματος διαδρομής (path-vector protocol) που αποφασίζει τις διαδρομές βάσει πολιτικών δικτύου και κανόνων εμπιστοσύνης μεταξύ των παρόχων.",
        "funFacts": [
            "Σφάλματα διαμόρφωσης στο BGP (BGP misconfiguration) ή πειρατεία διαδρομών (BGP hijacking) έχουν 'εξαφανίσει' κατά καιρούς γίγαντες του διαδικτύου όπως το Facebook και η Google από τον παγκόσμιο χάρτη για ώρες.",
            "Η τρέχουσα έκδοση BGP-4 υποστηρίζει το Classless Inter-Domain Routing (CIDR) από το 1993."
        ],
        "source": "https://en.wikipedia.org/wiki/Border_Gateway_Protocol",
        "tags": ["technology", "networking", "bgp", "internet_routing"]
    },
    {
        "id": "tech_hard_123",
        "text": "Ποιο είδος επίθεσης υλικού στη μνήμη RAM (DRAM), που αποκαλύφθηκε το 2014, καταφέρνει να αλλάξει τιμές bit σε γειτονικές γραμμές μνήμης ενεργοποιώντας επανειλημμένα την ίδια σειρά κελιών με μεγάλη ταχύτητα;",
        "correct": "Rowhammer",
        "distractors": ["Spectre", "Meltdown", "Cold Boot Attack"],
        "explanation": "Η επίθεση Rowhammer εκμεταλλεύεται την ηλεκτρική διαρροή ανάμεσα σε πυκνά τοποθετημένους μικροσκοπικούς πυκνωτές της σύγχρονης DRAM, επιτρέποντας την κλιμάκωση προνομίων χωρίς σφάλμα λογισμικού.",
        "funFacts": [
            "Αποτέλεσε την πρώτη απόδειξη ότι μια αμιγώς φυσική ατέλεια πυριτίου μπορεί να χρησιμοποιηθεί αξιόπιστα για πλήρη παραβίαση της ασφάλειας λογισμικού.",
            "Οι κατασκευαστές μνήμης απάντησαν αναπτύσσοντας τον μηχανισμό TRR (Target Row Refresh)."
        ],
        "source": "https://en.wikipedia.org/wiki/Row_hammer",
        "tags": ["technology", "security", "dram", "hardware", "rowhammer"]
    },
    {
        "id": "tech_hard_124",
        "text": "Ποιος είναι ο επίσημος κρυπτογραφικός αλγόριθμος κατακερματισμού (hash) που ανακηρύχθηκε νικητής του διαγωνισμού SHA-3 του NIST το 2012, βασισμένος στην πρωτοποριακή κατασκευή σπόγγου (sponge construction);",
        "correct": "Keccak",
        "distractors": ["BLAKE", "Skein", "Grøstl"],
        "explanation": "Ο Keccak (Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche) υιοθέτησε μια εντελώς διαφορετική δομή από την παραδοσιακή κατασκευή Merkle-Damgård των SHA-1 και SHA-2.",
        "funFacts": [
            "Ο Joan Daemen ήταν επίσης ένας από τους δύο βασικούς δημιουργούς του κρυπτογραφικού προτύπου AES (Rijndael).",
            "Μια παραλλαγή του Keccak (Keccak-256) χρησιμοποιείται ως ο κύριος αλγόριθμος κατακερματισμού στο blockchain του Ethereum."
        ],
        "source": "https://en.wikipedia.org/wiki/SHA-3",
        "tags": ["technology", "cryptography", "sha3", "keccak", "hashing"]
    },
    {
        "id": "tech_hard_125",
        "text": "Στη θεωρία μεταγλωττιστών (compiler design), ποια ενδιάμεση αναπαράσταση (IR) απαιτεί κάθε μεταβλητή να ορίζεται αυστηρά μόνο μία φορά και χρησιμοποιεί 'συναρτήσεις φ' (phi nodes) στα σημεία συνένωσης ροής ελέγχου;",
        "correct": "Στατική Μοναδική Ανάθεση (Static Single Assignment - SSA)",
        "distractors": ["Κώδικας Τριών Διευθύνσεων (TAC)", "Αφηρημένο Συντακτικό Δέντρο (AST)", "Reverse Polish Notation (RPN)"],
        "explanation": "Η μορφή SSA απλοποιεί δραστικά τις βελτιστοποιήσεις μεταγλωττιστή (όπως constant propagation, dead code elimination και register allocation) και χρησιμοποιείται εσωτερικά από το LLVM και το GCC.",
        "funFacts": [
            "Αναπτύχθηκε στα τέλη της δεκαετίας του 1980 από ερευνητές της IBM (Cytron, Ferrante, Rosen, Wegman, Zadeck).",
            "Η μετατροπή ενός προγράμματος σε SSA βασίζεται στον αλγόριθμο υπολογισμού του 'μετώπου κυριαρχίας' (dominance frontier) στο γράφημα ροής ελέγχου."
        ],
        "source": "https://en.wikipedia.org/wiki/Static_single-assignment_form",
        "tags": ["technology", "compilers", "ssa", "computer_science"]
    },
    {
        "id": "tech_hard_126",
        "text": "Ποιο κλασικό παράδοξο των αλγορίθμων αντικατάστασης σελίδων μνήμης δείχνει ότι η αύξηση του αριθμού των πλαισίων σελίδων (page frames) μπορεί παραδόξως να αυξήσει τον αριθμό των σφαλμάτων σελίδας (page faults) στον αλγόριθμο FIFO;",
        "correct": "Ανωμαλία του Μπελάντι (Bélády's anomaly)",
        "distractors": ["Παράδοξο του Κόρεϊ", "Παράδοξο του Μουρ", "Φαινόμενο Convoy"],
        "explanation": "Η ανωμαλία του Bélády (László Bélády, 1969) αποδεικνύει ότι ο αλγόριθμος FIFO δεν ανήκει στην κατηγορία των 'stack algorithms' (όπως ο LRU), όπου το σύνολο σελίδων για μέγεθος m περιέχεται πάντα στο σύνολο για μέγεθος m+1.",
        "funFacts": [
            "Ο László Bélády επινόησε επίσης τον θεωρητικά βέλτιστο αλγόριθμο αντικατάστασης σελίδας (Bélády's Optimal / MIN), ο οποίος αντικαθιστά τη σελίδα που δεν θα χρησιμοποιηθεί για το μεγαλύτερο χρονικό διάστημα στο μέλλον.",
            "Αν και ο MIN δεν μπορεί να υλοποιηθεί στην πράξη γιατί απαιτεί γνώση του μέλλοντος, χρησιμοποιείται ως σημείο αναφοράς (benchmark) για άλλους αλγορίθμους."
        ],
        "source": "https://en.wikipedia.org/wiki/B%C3%A9l%C3%A1dy%27s_anomaly",
        "tags": ["technology", "operating_systems", "virtual_memory", "algorithms"]
    },
    {
        "id": "tech_hard_127",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου επικοινωνίας και διεπαφής που σχεδιάστηκε ειδικά για γρήγορους δίσκους στερεάς κατάστασης (SSD), υποστηρίζοντας έως και 64.000 παράλληλες ουρές με 64.000 εντολές ανά ουρά μέσω του διαύλου PCIe;",
        "correct": "NVMe (Non-Volatile Memory Express)",
        "distractors": ["AHCI (SATA)", "SCSI", "SAS"],
        "explanation": "Το NVMe αντικατέστησε το παλιό πρωτόκολλο AHCI (το οποίο υποστήριζε μόνο μία ουρά 32 εντολών και σχεδιάστηκε για μηχανικούς δίσκους), απελευθερώνοντας την πλήρη παράλληλη ισχύ της μνήμης flash.",
        "funFacts": [
            "Απαιτεί λιγότερες από τις μισές εντολές CPU για την εκτέλεση μιας λειτουργίας I/O σε σύγκριση με το SATA/AHCI.",
            "Υποστηρίζει επίσης προηγμένες τεχνολογίες όπως το NVMe-oF (NVMe over Fabrics) για άμεση επικοινωνία αποθηκευτικών μέσων μέσω Ethernet ή InfiniBand σε data centers."
        ],
        "source": "https://en.wikipedia.org/wiki/NVM_Express",
        "tags": ["technology", "storage", "nvme", "hardware", "ssd"]
    },
    {
        "id": "tech_hard_128",
        "text": "Ποιος αλγόριθμος εύρεσης διαδρομής (pathfinding) αποτελεί γενίκευση του αλγορίθμου του Dijkstra χρησιμοποιώντας μια ευρετική συνάρτηση h(n) για να κατευθύνει την αναζήτηση ταχύτερα προς τον στόχο;",
        "correct": "Αλγόριθμος A* (A-Star)",
        "distractors": ["Αλγόριθμος Bellman-Ford", "Αλγόριθμος Floyd-Warshall", "Αλγόριθμος Kruskal"],
        "explanation": "Ο αλγόριθμος A* (Hart, Nilsson, Raphael, 1968) αξιολογεί τους κόμβους βάσει της συνάρτησης f(n) = g(n) + h(n), εγγυώμενος τη βέλτιστη διαδρομή εφόσον η ευρετική είναι παραδεκτή (admissible).",
        "funFacts": [
            "Αποτελεί τον πιο διαδεδομένο αλγόριθμο πλοήγησης και τεχνητής νοημοσύνης σε βιντεοπαιχνίδια στρατηγικής και χάρτες.",
            "Αναπτύχθηκε αρχικά για το πρόγραμμα του Shakey the Robot, του πρώτου ρομπότ γενικής χρήσης με τεχνητή νοημοσύνη στο SRI International."
        ],
        "source": "https://en.wikipedia.org/wiki/A*_search_algorithm",
        "tags": ["technology", "algorithms", "ai", "pathfinding", "graph_theory"]
    },
    {
        "id": "tech_hard_129",
        "text": "Ποιο κλασικό πρόβλημα συγχρονισμού σε πολυνηματικά συστήματα χωρίς κλειδώματα (lock-free) συμβαίνει όταν μια θέση μνήμης διαβάζεται ως τιμή Α, αλλάζει σε Β και επαναφέρεται σε Α πριν από μια λειτουργία Compare-And-Swap (CAS);",
        "correct": "Το πρόβλημα ABA (ABA problem)",
        "distractors": ["Το πρόβλημα των Δειπνοσοφιστών", "Το πρόβλημα Παραγωγού-Καταναλωτή", "Κούρσα δεδομένων (Data Race)"],
        "explanation": "Στο πρόβλημα ABA, η εντολή CAS πετυχαίνει νομίζοντας ότι η κατάσταση δεν άλλαξε καθόλου, παρότι ενδιάμεσες τροποποιήσεις μπορεί να έχουν αλλοιώσει τη συνοχή δομών δεδομένων (όπως συνδεδεμένες λίστες).",
        "funFacts": [
            "Μια κλασική μέθοδος επίλυσης είναι η προσθήκη ενός μετρητή τροποποιήσεων (version tag) μαζί με τον δείκτη (Tagged Pointer ή Double-word CAS).",
            "Εναλλακτικά χρησιμοποιούνται δείκτες κινδύνου (Hazard Pointers) ή τεχνικές Read-Copy-Update (RCU)."
        ],
        "source": "https://en.wikipedia.org/wiki/ABA_problem",
        "tags": ["technology", "concurrency", "lock_free", "multithreading"]
    },
    {
        "id": "tech_hard_130",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ψηφιακής πιστοποίησης DNS που προσθέτει κρυπτογραφικές υπογραφές στις εγγραφές DNS (DNSSEC) για την αποτροπή επιθέσεων DNS spoofing και cache poisoning;",
        "correct": "DNSSEC (DNS Security Extensions)",
        "distractors": ["DoH (DNS over HTTPS)", "DoT (DNS over TLS)", "DNScrypt"],
        "explanation": "Το DNSSEC χρησιμοποιεί ιεραρχική αλυσίδα εμπιστοσύνης (chain of trust) με εγγραφές RRSIG, DNSKEY και DS, ξεκινώντας από την υπογεγραμμένη ριζική ζώνη (root zone) του διαδικτύου.",
        "funFacts": [
            "Η ριζική ζώνη του διαδικτύου υπογράφηκε επίσημα για πρώτη φορά το 2010 σε μια αυστηρά ελεγχόμενη τελετή (Root Signing Ceremony) από την ICANN.",
            "Υπάρχουν 14 'φύλακες των κλειδιών' στον κόσμο (Cryptographic Officers) που κατέχουν φυσικά κλειδιά σε κάρτες ασφαλείας για την ανάκτηση του ριζικού κλειδιού σε περίπτωση καταστροφής."
        ],
        "source": "https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions",
        "tags": ["technology", "networking", "dns", "dnssec", "security"]
    },
    {
        "id": "tech_hard_131",
        "text": "Ποιο είναι το όνομα της τεχνικής διαχείρισης μνήμης στον πυρήνα του Linux που επιτρέπει την ειδοποίηση γεγονότων εισόδου/εξόδου σε πολλούς περιγραφείς αρχείων (file descriptors) σε χρόνο O(1), αντικαθιστώντας τις αργές κλήσεις select() και poll();",
        "correct": "epoll",
        "distractors": ["kqueue", "IOCP", "io_uring"],
        "explanation": "Το epoll χρησιμοποιεί εσωτερικά ένα κόκκινο-μαύρο δέντρο και μια λίστα ετοιμότητας (ready list), επιτρέποντας την αποτελεσματική εξυπηρέτηση δεκάδων χιλιάδων ταυτόχρονων συνδέσεων (το περίφημο πρόβλημα C10K).",
        "funFacts": [
            "Αποτελεί τη μυστική βάση της εξαιρετικής ταχύτητας σύγχρονων διακομιστών όπως ο Nginx, το Node.js (μέσω της libuv) και το Netty.",
            "Στο macOS και το FreeBSD η αντίστοιχη τεχνολογία ονομάζεται kqueue, ενώ στα Windows χρησιμοποιείται το I/O Completion Ports (IOCP)."
        ],
        "source": "https://en.wikipedia.org/wiki/Epoll",
        "tags": ["technology", "linux", "operating_systems", "networking", "epoll"]
    },
    {
        "id": "tech_hard_132",
        "text": "Ποιο είναι το όνομα της ιδιότητας των αυτοεξισορροπούμενων δυαδικών δέντρων αναζήτησης Κόκκινου-Μαύρου (Red-Black Trees), σύμφωνα με την οποία κάθε απλή διαδρομή από έναν κόμβο προς οποιοδήποτε φύλλο περιέχει τον ίδιο ακριβώς αριθμό μαύρων κόμβων;",
        "correct": "Ιδιότητα Μαύρου Ύψους (Black-Height Property)",
        "distractors": ["Ιδιότητα Παράγοντα Ισοζυγίου", "Ιδιότητα Σωρού", "Ιδιότητα Περιστροφής"],
        "explanation": "Η ιδιότητα του μαύρου ύψους διασφαλίζει ότι καμία διαδρομή δεν είναι μεγαλύτερη από το διπλάσιο οποιασδήποτε άλλης, εγγυώμενη χρόνο αναζήτησης, εισαγωγής και διαγραφής σε O(log n).",
        "funFacts": [
            "Επινοήθηκαν το 1972 από τον Rudolf Bayer (ως συμμετρικά δυαδικά δέντρα B) και πήραν το όνομα Red-Black Tree από τους Guibas και Sedgewick το 1978.",
            "Χρησιμοποιούνται στον πυρήνα του Linux για τον χρονοπρογραμματιστή διεργασιών CFS (Completely Fair Scheduler)."
        ],
        "source": "https://en.wikipedia.org/wiki/Red%E2%80%93black_tree",
        "tags": ["technology", "data_structures", "algorithms", "red_black_tree"]
    },
    {
        "id": "tech_hard_133",
        "text": "Ποιο σύστημα κρυπτογράφησης δημόσιου κλειδιού, που βασίζεται σε άλγεβρα πλεγμάτων (Lattice-based cryptography), επιλέχθηκε από το NIST το 2022 ως το κύριο διεθνές πρότυπο για προστασία από επιθέσεις κβαντικών υπολογιστών;",
        "correct": "CRYSTALS-Kyber (ML-KEM)",
        "distractors": ["RSA-4096", "ECDH", "Classic McEliece"],
        "explanation": "Το Kyber βασίζεται στη μαθηματική σκληρότητα του προβλήματος Learning With Errors over Module Lattices (Module-LWE), το οποίο πιστεύεται ότι είναι δυσεπίλυτο τόσο για κλασικούς όσο και για κβαντικούς υπολογιστές.",
        "funFacts": [
            "Τυποποιήθηκε επίσημα από το NIST τον Αύγουστο του 2024 με την κωδική ονομασία FIPS 203 (ML-KEM).",
            "Έχει ήδη ενσωματωθεί πειραματικά σε πρωτόκολλα όπως το Google Chrome και το Cloudflare για την προστασία συνδέσεων TLS."
        ],
        "source": "https://en.wikipedia.org/wiki/Kyber",
        "tags": ["technology", "cryptography", "quantum_computing", "security", "nist"]
    },
    {
        "id": "tech_hard_134",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου χρονισμού και συγχρονισμού που επινοήθηκε από τον Leslie Lamport το 1978, χρησιμοποιώντας μονοτονικά αυξανόμενους ακέραιους για τη μερική διάταξη γεγονότων σε κατανεμημένα συστήματα;",
        "correct": "Λογικά Ρολόγια Lamport (Lamport Timestamps)",
        "distractors": ["Διανυσματικά Ρολόγια (Vector Clocks)", "TrueTime", "NTP"],
        "explanation": "Τα ρολόγια Lamport ορίζουν τη σχέση 'συνέβη-πριν' (happened-before relation, a -> b), εξασφαλίζοντας ότι εάν ένα γεγονός προκάλεσε ένα άλλο, το πρώτο θα έχει μικρότερο χρονικό αποτύπωμα.",
        "funFacts": [
            "Το ιστορικό επιστημονικό άρθρο του Lamport 'Time, Clocks, and the Ordering of Events in a Distributed System' είναι ένα από τα πιο πολυαναφερόμενα papers στην ιστορία της επιστήμης υπολογιστών.",
            "Επειδή δύο γεγονότα με διαφορετικά ρολόγια Lamport μπορεί να είναι ταυτόχρονα χωρίς αιτιώδη σχέση, αργότερα αναπτύχθηκαν τα Διανυσματικά Ρολόγια (Vector Clocks)."
        ],
        "source": "https://en.wikipedia.org/wiki/Lamport_timestamp",
        "tags": ["technology", "distributed_systems", "lamport", "algorithms"]
    },
    {
        "id": "tech_hard_135",
        "text": "Ποιο είναι το όνομα του αλγορίθμου κωδικοποίησης εντροπίας χωρίς απώλειες (lossless data compression) που εκχωρεί κωδικούς μεταβλητού μήκους σε σύμβολα βάσει της συχνότητας εμφάνισής τους, αναπαριστώμενος από ένα δυαδικό δέντρο;",
        "correct": "Κωδικοποίηση Huffman",
        "distractors": ["Αριθμητική Κωδικοποίηση", "LZW", "Run-Length Encoding"],
        "explanation": "Ο David Huffman επινόησε τον αλγόριθμο το 1952 ως φοιτητής στο MIT για μια εργασία εξαμήνου, βρίσκοντας τη βέλτιστη μέθοδο κατασκευής προθεματικών κωδίκων (prefix codes).",
        "funFacts": [
            "Ο καθηγητής του, Robert Fano, του είχε δώσει την επιλογή να δώσει τελική εξέταση ή να προσπαθήσει να λύσει το άλυτο τότε πρόβλημα της εύρεσης του πιο αποδοτικού δυαδικού κώδικα.",
            "Χρησιμοποιείται ως το τελικό στάδιο συμπίεσης σε πανταχού παρόντα φορμά όπως το JPEG, το MP3 και το ZIP (DEFLATE)."
        ],
        "source": "https://en.wikipedia.org/wiki/Huffman_coding",
        "tags": ["technology", "compression", "algorithms", "huffman"]
    },
    {
        "id": "tech_hard_136",
        "text": "Ποιο υποσύστημα του πυρήνα του Linux, που εισήχθη το 2019 από τον Jens Axboe, προσφέρει υπερταχύτατη ασύγχρονη είσοδο/έξοδο (async I/O) χρησιμοποιώντας δύο κοινόχρηστους κυκλικούς δακτυλίους (ring buffers) χωρίς system call overhead;",
        "correct": "io_uring",
        "distractors": ["epoll", "aio", "splice"],
        "explanation": "Το io_uring χρησιμοποιεί έναν δακτύλιο υποβολής (Submission Queue) και έναν δακτύλιο ολοκλήρωσης (Completion Queue) σε κοινόχρηστη μνήμη μεταξύ χρήστη και πυρήνα, εξαλείφοντας τις δαπανηρές εναλλαγές περιβάλλοντος (context switches).",
        "funFacts": [
            "Μπορεί να λειτουργήσει σε λειτουργία polling (IORING_SETUP_SQPOLL), όπου ένα νήμα του πυρήνα ελέγχει συνεχώς για νέες εργασίες χωρίς να χρειαστεί ποτέ ούτε μία κλήση συστήματος enter!",
            "Έχει επιτύχει ταχύτητες άνω των 2-3 εκατομμυρίων IOPS ανά πυρήνα CPU σε σύγχρονους SSDs."
        ],
        "source": "https://en.wikipedia.org/wiki/Io_uring",
        "tags": ["technology", "linux", "operating_systems", "io_uring", "performance"]
    },
    {
        "id": "tech_hard_137",
        "text": "Ποιος αλγόριθμος αναζήτησης συμβολοσειρών (string matching) προεπεξεργάζεται ένα λεξικό πολλαπλών προτύπων κατασκευάζοντας ένα αυτόματο πεπερασμένων καταστάσεων τύπου Trie με συνδέσμους αποτυχίας (failure links) σε γραμμικό χρόνο O(n + m);",
        "correct": "Αλγόριθμος Aho-Corasick",
        "distractors": ["Αλγόριθμος Knuth-Morris-Pratt (KMP)", "Αλγόριθμος Boyer-Moore", "Αλγόριθμος Rabin-Karp"],
        "explanation": "Ο Alfred Aho και η Margaret Corasick επινόησαν τον αλγόριθμο το 1975, επιτρέποντας τον ταυτόχρονο εντοπισμό όλων των λέξεων ενός λεξικού μέσα σε ένα κείμενο σε ένα μόνο πέρασμα.",
        "funFacts": [
            "Αποτελεί την καρδιά του εργαλείου fgrep του Unix και σύγχρονων συστημάτων ανίχνευσης εισβολών όπως το Snort.",
            "Χρησιμοποιείται επίσης σε λογισμικό φίλτρων περιεχομένου και λογοκρισίας για τον ταχύτατο εντοπισμό απαγορευμένων λέξεων σε ροές δεδομένων."
        ],
        "source": "https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm",
        "tags": ["technology", "algorithms", "string_searching", "data_structures"]
    },
    {
        "id": "tech_hard_138",
        "text": "Ποιο κλασικό υπόδειγμα παράλληλου και κατανεμημένου υπολογισμού (Actor Model), που προτάθηκε από τον Carl Hewitt το 1973, αντιμετωπίζει τα 'όντα' (actors) ως αυτόνομες οντότητες που επικοινωνούν αποκλειστικά μέσω ασύγχρονων μηνυμάτων χωρίς κοινόχρηστη μνήμη;",
        "correct": "Μοντέλο Ηθοποιών (Actor Model)",
        "distractors": ["Μοντέλο CSP (Communicating Sequential Processes)", "Μοντέλο MapReduce", "Μοντέλο Fork-Join"],
        "explanation": "Στο Actor Model, κάθε actor έχει μια ιδιωτική ουρά μηνυμάτων (mailbox) και ως απάντηση σε ένα μήνυμα μπορεί μόνο να στείλει μηνύματα, να δημιουργήσει νέους actors ή να αλλάξει την εσωτερική του κατάσταση.",
        "funFacts": [
            "Αποτελεί τη θεμελιώδη αρχιτεκτονική φιλοσοφία της γλώσσας Erlang (και του Elixir), επιτρέποντας την κατασκευή συστημάτων με διαθεσιμότητα 'εννέα εννιάρια' (99.9999999%).",
            "Υλοποιείται επίσης σε συστήματα όπως το Akka (Java/Scala) και το Ray (Python)."
        ],
        "source": "https://en.wikipedia.org/wiki/Actor_model",
        "tags": ["technology", "concurrency", "actor_model", "distributed_systems"]
    },
    {
        "id": "tech_hard_139",
        "text": "Ποιος αλγόριθμος ταξινόμησης (sorting algorithm) επινόησε ο Tim Peters το 2002 για τη γλώσσα Python, συνδυάζοντας την ταξινόμηση συγχώνευσης (Merge Sort) και την ταξινόμηση με εισαγωγή (Insertion Sort) για μέγιστη ταχύτητα σε πραγματικά δεδομένα;",
        "correct": "Timsort",
        "distractors": ["Quicksort", "Introsort", "Heapsort"],
        "explanation": "Ο Timsort εντοπίζει ήδη ταξινομημένες υπο-ακολουθίες (runs) στα φυσικά δεδομένα και τις συγχωνεύει αποδοτικά, πετυχαίνοντας χρόνο O(n) στην καλύτερη περίπτωση και O(n log n) στη χειρότερη.",
        "funFacts": [
            "Λόγω της εξαιρετικής του απόδοσης, υιοθετήθηκε ως ο προεπιλεγμένος αλγόριθμος ταξινόμησης στη Java SE 7 (για μη πρωταρχικούς τύπους), στο Android και στο V8 engine της Google.",
            "Το 2015, ερευνητές ανακάλυψαν ένα λεπτό σφάλμα υπερχείλισης στοίβας στον Timsort που υπήρχε κρυμμένο σε όλες τις υλοποιήσεις για πάνω από 12 χρόνια!"
        ],
        "source": "https://en.wikipedia.org/wiki/Timsort",
        "tags": ["technology", "algorithms", "sorting", "python", "timsort"]
    },
    {
        "id": "tech_hard_140",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ελέγχου συμφόρησης TCP (Congestion Control) που ανέπτυξε η Google το 2016, το οποίο μετρά άμεσα το διαθέσιμο εύρος ζώνης και τον χρόνο καθυστέρησης αντί να βασίζεται στην απώλεια πακέτων;",
        "correct": "BBR (Bottleneck Bandwidth and RTT)",
        "distractors": ["CUBIC", "Reno", "Tahoe"],
        "explanation": "Το BBR αποτρέπει το φαινόμενο του 'Bufferbloat' (υπερπλήρωση ενδιάμεσων buffers των routers), μεγιστοποιώντας τη ροή δεδομένων και ελαχιστοποιώντας την καθυστέρηση (latency).",
        "funFacts": [
            "Όταν η Google ενεργοποίησε το BBR στις υπηρεσίες του YouTube, η μέση ταχύτητα μετάδοσης βίντεο αυξήθηκε κατά 4% παγκοσμίως και πάνω από 14% σε αναπτυσσόμενες χώρες.",
            "Σήμερα αποτελεί τον βασικό αλγόριθμο ελέγχου συμφόρησης στο πρωτόκολλο QUIC και HTTP/3."
        ],
        "source": "https://en.wikipedia.org/wiki/BBR_(congestion_control)",
        "tags": ["technology", "networking", "tcp", "bbr", "congestion_control"]
    },
    {
        "id": "tech_hard_141",
        "text": "Ποια τεχνική γραμμικής άλγεβρας και διόρθωσης σφαλμάτων (forward error correction), που αναπτύχθηκε το 1960, χρησιμοποιεί πράξεις σε πεπερασμένα σώματα Galois (GF) και προστατεύει δεδομένα σε CDs, DVDs, QR codes και δορυφορικές μεταδόσεις;",
        "correct": "Κώδικες Reed-Solomon",
        "distractors": ["Κώδικες Hamming", "Κώδικες Turbo", "Κώδικες LDPC"],
        "explanation": "Οι Irving Reed και Gustave Solomon επινόησαν τους κώδικες Reed-Solomon, οι οποίοι μπορούν να διορθώσουν πολλαπλά διαδοχικά σφάλματα (burst errors) προσθέτοντας πλεονάζοντα σύμβολα σε ένα πολυώνυμο.",
        "funFacts": [
            "Χάρη στους κώδικες Reed-Solomon, ένα CD ήχου μπορεί να παίξει τέλεια ακόμη κι αν έχει γρατσουνιά πλάτους 2 χιλιοστών.",
            "Χρησιμοποιήθηκαν επίσης από τα διαστημόπλοια Voyager για τη μετάδοση των ιστορικών φωτογραφιών του Δία, του Κρόνου και του Ποσειδώνα πίσω στη Γη."
        ],
        "source": "https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction",
        "tags": ["technology", "error_correction", "reed_solomon", "math", "hardware"]
    },
    {
        "id": "tech_hard_142",
        "text": "Ποια είναι η βασική διαφορά στο μοντέλο συνέπειας μνήμης (memory consistency model) ανάμεσα στην αρχιτεκτονική x86 και την αρχιτεκτονική ARM;",
        "correct": "Η x86 ακολουθεί αυστηρότερο μοντέλο TSO (Total Store Order), ενώ η ARM ακολουθεί χαλαρό (weakly-ordered) μοντέλο μνήμης",
        "distractors": [
            "Η x86 είναι πλήρως χαλαρή ενώ η ARM είναι αυστηρά σειριακή",
            "Και οι δύο αρχιτεκτονικές έχουν πανομοιότυπη διαταγή αναγνώσεων και εγγραφών",
            "Η ARM απαγορεύει οποιαδήποτε αναδιάταξη εντολών από το υλικό"
        ],
        "explanation": "Στην x86/x64, οι εγγραφές εμφανίζονται σε όλους τους πυρήνες με την ίδια σειρά (εκτός από reordering Store->Load). Στην ARM, τόσο οι αναγνώσεις όσο και οι εγγραφές μπορούν να αναδιαταχθούν ελεύθερα από το υλικό, απαιτώντας ρητά memory barriers (DMB/DSB).",
        "funFacts": [
            "Αυτός είναι ο λόγος που πολυνηματικός κώδικας C++ με λανθασμένο συγχρονισμό μπορεί να τρέχει 'τυχαία σωστά' σε επεξεργαστές Intel αλλά να καταρρέει σε Apple Silicon (M1/M2/M3).",
            "Η Apple πρόσθεσε ειδικό υλικό mode (ACTLR_EL1 / TSO mode) στους επεξεργαστές Apple Silicon για να τρέχει ταχύτατα κώδικα x86 μέσω του μεταφραστή Rosetta 2."
        ],
        "source": "https://en.wikipedia.org/wiki/Memory_model_(programming)",
        "tags": ["technology", "cpu", "memory_model", "x86", "arm"]
    },
    {
        "id": "tech_hard_143",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δέσμευσης δύο φάσεων (Two-Phase Commit - 2PC) που χρησιμοποιείται σε κατανεμημένες συναλλαγές βάσεων δεδομένων, του οποίου όμως το κύριο μειονέκτημα είναι ότι αποτελεί πρωτόκολλο εμπλοκής (blocking protocol);",
        "correct": "Two-Phase Commit (2PC)",
        "distractors": ["Three-Phase Commit (3PC)", "Saga Pattern", "Eventual Consistency"],
        "explanation": "Στο 2PC, ένας συντονιστής ρωτά όλους τους κόμβους αν είναι έτοιμοι (Prepare Phase) και αν όλοι συμφωνήσουν εκτελείται η Commit Phase. Εάν ο συντονιστής καταρρεύσει στη μέση, οι κόμβοι μένουν αποκλεισμένοι χωρίς να ξέρουν αν πρέπει να δεσμεύσουν ή να απορρίψουν.",
        "funFacts": [
            "Για την αντιμετώπιση του προβλήματος αυτού προτάθηκε το Three-Phase Commit (3PC), το οποίο όμως είναι πιο περίπλοκο και σπάνια χρησιμοποιείται στην πράξη.",
            "Στα σύγχρονα microservices προτιμάται συχνά το μοτίβο Saga (Saga Pattern) με αντισταθμιστικές συναλλαγές (compensating transactions)."
        ],
        "source": "https://en.wikipedia.org/wiki/Two-phase_commit_protocol",
        "tags": ["technology", "databases", "distributed_systems", "transactions"]
    },
    {
        "id": "tech_hard_144",
        "text": "Ποιος αλγόριθμος πρόβλεψης διακλαδώσεων (branch predictor) σε σύγχρονους επεξεργαστές, που σχεδιάστηκε από τον André Seznec, χρησιμοποιεί πολλαπλούς πίνακες ιστορικού με γεωμετρικά αυξανόμενα μήκη και θεωρείται ο κορυφαίος στον κόσμο;",
        "correct": "TAGE (TAgged GEometric)",
        "distractors": ["Gshare", "Perceptron Predictor", "Bimodal Predictor"],
        "explanation": "Ο TAGE χρησιμοποιεί γεωμετρική κλίμακα ιστορικού διακλαδώσεων και ετικέτες (tags), πετυχαίνοντας ποσοστά επιτυχίας πρόβλεψης άνω του 95-98% σε σύγχρονους επεξεργαστές x86 και ARM.",
        "funFacts": [
            "Κερδίζει σταθερά τους διεθνείς διαγωνισμούς Championship Branch Prediction (CBP) από το 2004.",
            "Μια εσφαλμένη πρόβλεψη διακλάδωσης (branch misprediction) κοστίζει 15-20 κύκλους ρολογιού καθώς ολόκληρος ο αγωγός (pipeline) εντολών του επεξεργαστή πρέπει να καθαριστεί (flush)."
        ],
        "source": "https://en.wikipedia.org/wiki/Branch_predictor#TAGE_predictor",
        "tags": ["technology", "cpu", "hardware", "branch_prediction"]
    },
    {
        "id": "tech_hard_145",
        "text": "Ποιο είναι το όνομα των δομών δεδομένων για συνεργατική επεξεργασία (όπως στο Google Docs ή Figma) που εγγυώνται ότι πολλαπλά αντίγραφα μπορούν να τροποποιούνται παράλληλα και να συγκλίνουν στην ίδια κατάσταση χωρίς κεντρικό συντονιστή;",
        "correct": "CRDTs (Conflict-free Replicated Data Types)",
        "distractors": ["Operational Transformation (OT)", "Raft State Machines", "Paxos Registers"],
        "explanation": "Τα CRDTs (Shapiro et al., 2011) βασίζονται σε μαθηματικές δομές ημι-δικτύων (semilattices) με πράξεις που είναι μεταθετικές, προσεταιριστικές και ταυτοδύναμες, καθιστώντας τις συγκρούσεις αδύνατες.",
        "funFacts": [
            "Χρησιμοποιούνται εκτεταμένα σε εφαρμογές 'Local-First', στο chat του Apple Notes και στον collaborative editor του Figma.",
            "Χωρίζονται σε δύο βασικές κατηγορίες: State-based (CvRDT) και Operation-based (CmRDT)."
        ],
        "source": "https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type",
        "tags": ["technology", "distributed_systems", "crdt", "concurrency"]
    },
    {
        "id": "tech_hard_146",
        "text": "Ποιος αλγόριθμος δρομολόγησης πακέτων σε κατανεμημένους πίνακες κατακερματισμού (DHT), που επινοήθηκε από τους Petar Maymounkov και David Mazières το 2002, χρησιμοποιεί την πράξη XOR ως μετρική απόστασης ανάμεσα στους κόμβους;",
        "correct": "Kademlia",
        "distractors": ["Chord", "Pastry", "Tapestry"],
        "explanation": "Το Kademlia ορίζει την απόσταση μεταξύ δύο κόμβων d(x, y) = x ⊕ y, επιτρέποντας τον εντοπισμό οποιουδήποτε κόμβου ή πόρου σε O(log n) μηνύματα.",
        "funFacts": [
            "Αποτελεί τη ραχοκοκαλιά των αποκεντρωμένων δικτύων BitTorrent (Mainline DHT), του IPFS και του μηχανισμού ανακάλυψης κόμβων του Ethereum (Node Discovery Protocol).",
            "Η συμμετρία του XOR [d(x,y) = d(y,x)] απλοποιεί δραστικά τη διατήρηση των πινάκων δρομολόγησης (k-buckets)."
        ],
        "source": "https://en.wikipedia.org/wiki/Kademlia",
        "tags": ["technology", "p2p", "bittorrent", "algorithms", "networking"]
    },
    {
        "id": "tech_hard_147",
        "text": "Ποιο είναι το όνομα του αλγορίθμου ανάλυσης μαθηματικών εκφράσεων που επινόησε ο Edsger Dijkstra το 1961, ο οποίος μετατρέπει παραστάσεις ενθεματικής σημειογραφίας (infix) σε αντίστροφη πολωνική σημειογραφία (RPN);",
        "correct": "Αλγόριθμος Shunting-yard",
        "distractors": ["Αλγόριθμος CYK", "Αλγόριθμος Earley", "Αλγόριθμος LL(k)"],
        "explanation": "Ο αλγόριθμος Shunting-yard χρησιμοποιεί μια στοίβα τελεστών προσομοιώνοντας τη λειτουργία ενός σιδηροδρομικού σταθμού διαλογής βαγονιών (shunting yard), διαχειριζόμενος άψογα προτεραιότητες τελεστών και παρενθέσεις.",
        "funFacts": [
            "Αποτελεί την κλασική μέθοδο που χρησιμοποιείται σε επιστημονικά κομπιουτεράκια και απλούς διερμηνείς γλωσσών προγραμματισμού.",
            "Επιτρέπει τον υπολογισμό μιας έκφρασης σε γραμμικό χρόνο O(n) με ένα μόνο πέρασμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Shunting_yard_algorithm",
        "tags": ["technology", "algorithms", "dijkstra", "parsing", "data_structures"]
    },
    {
        "id": "tech_hard_148",
        "text": "Ποιο είναι το όνομα της επίθεσης πλευρικού καναλιού (side-channel attack) σε υλοποιήσεις κρυπτογραφίας όπου ο επιτιθέμενος μετρά τον ακριβή χρόνο που απαιτείται για την εκτέλεση υπολογισμών για να ανακτήσει μυστικά κλειδιά;",
        "correct": "Επίθεση Χρονισμού (Timing Attack)",
        "distractors": ["Επίθεση Ωμής Βίας (Brute-force)", "Επίθεση Replay", "Επίθεση Man-in-the-Middle"],
        "explanation": "Οι επιθέσεις χρονισμού (Paul Kocher, 1996) εκμεταλλεύονται διαφορές χρόνου που προκύπτουν από διακλαδώσεις if-else ή προσπελάσεις μνήμης cache ανάλογα με τα bit του μυστικού κλειδιού.",
        "funFacts": [
            "Για την προστασία από αυτές τις επιθέσεις, όλοι οι σύγχρονοι κρυπτογραφικοί αλγόριθμοι γράφονται αυστηρά σε κώδικα σταθερού χρόνου (constant-time code).",
            "Μια απλή σύγκριση συμβολοσειρών με την εντολή memcmp() ή == σε κωδικούς πρόσβασης μπορεί να διαρρεύσει πληροφορίες χαρακτήρα προς χαρακτήρα μέσω τέτοιων επιθέσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Timing_attack",
        "tags": ["technology", "cryptography", "security", "side_channel"]
    },
    {
        "id": "tech_hard_149",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου συλλογής απορριμμάτων (Garbage Collection) που χωρίζει τα αντικείμενα της μνήμης σε τρία σύνολα με βάση χρώματα (Λευκό, Γκρι, Μαύρο), επιτρέποντας την εκτέλεση του συλλέκτη ταυτόχρονα με την εφαρμογή;",
        "correct": "Αλγόριθμος Σήμανσης Τριών Χρωμάτων (Tri-color marking)",
        "distractors": ["Μέτρηση Αναφορών (Reference Counting)", "Stop-the-World GC", "Copying GC"],
        "explanation": "Στον αλγόριθμο Tri-color (Dijkstra et al., 1978), τα Λευκά είναι υποψήφια για διαγραφή, τα Γκρι έχουν εντοπιστεί αλλά δεν έχουν εξεταστεί οι αναφορές τους, και τα Μαύρα είναι ζωντανά αντικείμενα των οποίων όλες οι αναφορές έχουν σαρωθεί.",
        "funFacts": [
            "Αποτελεί τη θεωρητική βάση όλων των σύγχρονων concurrent garbage collectors όπως ο ZGC στη Java και ο GC της γλώσσας Go.",
            "Απαιτεί τη χρήση 'φραγμάτων εγγραφής' (write barriers) για να αποτραπεί η περίπτωση ένα μαύρο αντικείμενο να δείξει σε ένα λευκό χωρίς ενδιάμεσο γκρι."
        ],
        "source": "https://en.wikipedia.org/wiki/Tracing_garbage_collection#Tri-color_marking",
        "tags": ["technology", "garbage_collection", "memory_management", "dijkstra"]
    },
    {
        "id": "tech_hard_150",
        "text": "Ποιο είναι το όνομα του διάσημου θεωρήματος του Michael J. Fischer, Nancy Lynch και Michael S. Paterson (FLP Impossibility, 1985) για τα κατανεμημένα συστήματα;",
        "correct": "Κανένας ντετερμινιστικός ασύγχρονος αλγόριθμος συναίνεσης δεν μπορεί να εγγυηθεί συμφωνία με την παρουσία έστω και μίας κατάρρευσης κόμβου",
        "distractors": [
            "Κάθε κατανεμημένο σύστημα απαιτεί τουλάχιστον τρία αντίγραφα δεδομένων",
            "Είναι αδύνατη η κρυπτογράφηση μηνυμάτων χωρίς κοινόχρηστο κλειδί",
            "Η μέγιστη καθυστέρηση δικτύου είναι πάντα ανάλογη του αριθμού των κόμβων"
        ],
        "explanation": "Το θεώρημα FLP απέδειξε ότι σε ένα καθαρά ασύγχρονο δίκτυο (όπου δεν υπάρχει όριο στον χρόνο παράδοσης μηνυμάτων), είναι αδύνατο να διακριθεί ένας κόμβος που κατέρρευσε από έναν που απλώς καθυστερεί υπερβολικά.",
        "funFacts": [
            "Κέρδισε το βραβείο Dijkstra Prize το 2001 για τη θεμελιώδη σημασία του στην επιστήμη των υπολογιστών.",
            "Στην πράξη, όλα τα συστήματα συναίνεσης (όπως το Paxos και το Raft) παρακάμπτουν το FLP υποθέτοντας μερική συγχρονικότητα (timeouts και λογικά ρολόγια)."
        ],
        "source": "https://en.wikipedia.org/wiki/Consensus_(computer_science)#Impossibility_results",
        "tags": ["technology", "distributed_systems", "flp_impossibility", "computer_science"]
    },
    {
        "id": "tech_hard_151",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ανταλλαγής κλειδιών που επινόησαν οι Whitfield Diffie και Martin Hellman το 1976, επιτρέποντας σε δύο μέρη να δημιουργήσουν ένα κοινό μυστικό κλειδί μέσω ενός μη ασφαλούς καναλιού;",
        "correct": "Ανταλλαγή Κλειδιών Diffie-Hellman (DH)",
        "distractors": ["RSA", "ElGamal", "Kerberos"],
        "explanation": "Το πρωτόκολλο Diffie-Hellman βασίζεται στη δυσκολία επίλυσης του προβλήματος του διακριτού λογαρίθμου σε πεπερασμένα κυκλικά σώματα και θεμελίωσε την ασύμμετρη κρυπτογραφία.",
        "funFacts": [
            "Αν και δημοσιεύτηκε το 1976, αποκαλύφθηκε το 1997 ότι η βρετανική μυστική υπηρεσία GCHQ (Malcolm Williamson) το είχε ανακαλύψει κρυφά ήδη από το 1974.",
            "Η σύγχρονη παραλλαγή του χρησιμοποιεί ελλειπτικές καμπύλες (ECDH) για μεγαλύτερη ταχύτητα και μικρότερα κλειδιά."
        ],
        "source": "https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange",
        "tags": ["technology", "cryptography", "diffie_hellman", "security"]
    },
    {
        "id": "tech_hard_152",
        "text": "Ποιος είναι ο αλγόριθμος εκτέλεσης εντολών εκτός σειράς (out-of-order execution) που ανέπτυξε ο Robert Tomasulo στην IBM το 1967 για τον υπερυπολογιστή System/360 Model 91, εισάγοντας τους 'σταθμούς κράτησης' (reservation stations);",
        "correct": "Αλγόριθμος του Tomasulo",
        "distractors": ["Scoreboarding", "Αλγόριθμος Peterson", "Αλγόριθμος Dekker"],
        "explanation": "Ο αλγόριθμος του Tomasulo εξαλείφει τους κινδύνους δεδομένων WAR (Write-After-Read) και WAW (Write-After-Write) με δυναμική μετονομασία καταχωρητών μέσω κοινόχρηστου διαύλου δεδομένων (CDB).",
        "funFacts": [
            "Ο Robert Tomasulo τιμήθηκε με το διάσημο βραβείο Eckert-Mauchly Award το 1997 για την εφεύρεσή του.",
            "Αποτελεί την καρδιά όλων των σύγχρονων επεξεργαστών υψηλής απόδοσης (Intel Core, AMD Ryzen, Apple Silicon)."
        ],
        "source": "https://en.wikipedia.org/wiki/Tomasulo%27s_algorithm",
        "tags": ["technology", "cpu", "hardware", "computer_architecture", "tomasulo"]
    },
    {
        "id": "tech_hard_153",
        "text": "Ποια είναι η τεχνική κρυπτογραφικής απόδειξης όπου ένας αποδείκτης (prover) μπορεί να πείσει έναν επαληθευτή (verifier) ότι μια πρόταση είναι αληθής, χωρίς να αποκαλύψει απολύτως καμία άλλη πληροφορία πέρα από την ίδια την αλήθεια της πρότασης;",
        "correct": "Απόδειξη Μηδενικής Γνώσης (Zero-Knowledge Proof - ZKP)",
        "distractors": ["Ψηφιακή Υπογραφή", "Κρυπτογράφηση Ομόμορφη", "Κωδικός Επαλήθευσης Μηνύματος (MAC)"],
        "explanation": "Οι αποδείξεις μηδενικής γνώσης (Goldwasser, Micali, Rackoff, 1985) πρέπει να πληρούν τρεις ιδιότητες: Πληρότητα (Completeness), Ορθότητα (Soundness) και Μηδενική Γνώση (Zero-Knowledge).",
        "funFacts": [
            "Χρησιμοποιούνται ευρέως σε τεχνολογίες απορρήτου blockchain (όπως Zcash με zk-SNARKs) και σε συστήματα κλιμάκωσης του Ethereum (zk-Rollups).",
            "Οι σύγχρονες μη-διαδραστικές εκδόσεις (zk-STARKs) είναι ανθεκτικές σε κβαντικές επιθέσεις και δεν απαιτούν έμπιστη αρχική ρύθμιση (trusted setup)."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-knowledge_proof",
        "tags": ["technology", "cryptography", "zero_knowledge", "zkp", "blockchain"]
    },
    {
        "id": "tech_hard_154",
        "text": "Ποιο είναι το όνομα του αλγορίθμου κατακερματισμού που επινοήθηκε από τους Karger et al. στο MIT το 1997, όπου η προσθήκη ή αφαίρεση ενός διακομιστή απαιτεί την ανακατανομή μόνο K/n κλειδιών κατά μέσο όρο;",
        "correct": "Συνεπής Κατακερματισμός (Consistent Hashing)",
        "distractors": ["Rendezvous Hashing", "Linear Hashing", "Extendible Hashing"],
        "explanation": "Ο συνεπής κατακερματισμός χαρτογραφεί τόσο τα δεδομένα όσο και τους κόμβους σε έναν νοητό δακτύλιο (hash ring), αποτρέποντας τη μαζική απώλεια κρυφής μνήμης σε κατανεμημένα συστήματα όταν αλλάζει ο αριθμός των εξυπηρετητών.",
        "funFacts": [
            "Αναπτύχθηκε αρχικά για το παγκόσμιο δίκτυο διανομής περιεχομένου (CDN) της Akamai Technologies.",
            "Αποτελεί τη βασική αρχιτεκτονική κατανομής δεδομένων στο Amazon DynamoDB, στο Apache Cassandra και στο Memcached."
        ],
        "source": "https://en.wikipedia.org/wiki/Consistent_hashing",
        "tags": ["technology", "distributed_systems", "algorithms", "caching"]
    },
    {
        "id": "tech_hard_155",
        "text": "Ποιο διάσημο πρωτόκολλο ασφάλειας επιπέδου μεταφοράς στην έκδοση 1.3 (TLS 1.3, 2018) κατήργησε οριστικά την ανταλλαγή στατικών κλειδιών RSA υπέρ του Ephemeral Diffie-Hellman, διασφαλίζοντας ποια κρίσιμη ιδιότητα ασφαλείας;",
        "correct": "Τέλεια Μελλοντική Μυστικότητα (Perfect Forward Secrecy - PFS)",
        "distractors": ["Αποφυγή Replay Attacks", "Πλήρης Ανωνυμία", "Αμφίδρομη Αυθεντικοποίηση"],
        "explanation": "Με το Perfect Forward Secrecy, ακόμη κι αν ένα μακροπρόθεσμο ιδιωτικό κλειδί του διακομιστή κλαπεί στο μέλλον, ο επιτιθέμενος δεν μπορεί να αποκρυπτογραφήσει παρελθούσες επικοινωνίες που είχε καταγράψει.",
        "funFacts": [
            "Το TLS 1.3 αφαίρεσε επίσης όλους τους παρωχημένους και επικίνδυνους αλγορίθμους όπως το RC4, το DES, το 3DES και το SHA-1.",
            "Μείωσε επίσης τη διαδικασία χειραψίας (handshake) από 2 round-trips (2-RTT) σε μόλις 1 round-trip (1-RTT)."
        ],
        "source": "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3",
        "tags": ["technology", "security", "tls", "cryptography", "protocols"]
    },
    {
        "id": "tech_hard_156",
        "text": "Ποια είναι η τεχνολογία άμεσης πρόσβασης στη μνήμη μέσω δικτύου που επιτρέπει σε έναν υπολογιστή να διαβάζει ή να γράφει στη μνήμη ενός άλλου υπολογιστή παρακάμπτοντας εντελώς το λειτουργικό σύστημα και τη CPU και των δύο πλευρών;",
        "correct": "RDMA (Remote Direct Memory Access)",
        "distractors": ["DMA", "DPDK", "Zero-Copy TCP"],
        "explanation": "Το RDMA επιτυγχάνει εξαιρετικά χαμηλή καθυστέρηση (latency κάτω από 1 μικροδευτερόλεπτο) και τεράστιο εύρος ζώνης, χρησιμοποιούμενο σε υπερυπολογιστές και συστάδες εκπαίδευσης τεχνητής νοημοσύνης μέσω InfiniBand ή RoCE.",
        "funFacts": [
            "Είναι απαραίτητο για την εκπαίδευση μεγάλων γλωσσικών μοντέλων (LLMs) σε συστοιχίες χιλιάδων GPUs (όπως τα clusters NVIDIA H100).",
            "Επειδή παρακάμπτει τον πυρήνα (kernel bypass), η μεταφορά δεδομένων γίνεται με μηδενική αντιγραφή (zero-copy) απευθείας από την κάρτα δικτύου στη μνήμη."
        ],
        "source": "https://en.wikipedia.org/wiki/Remote_direct_memory_access",
        "tags": ["technology", "networking", "rdma", "hardware", "hpc"]
    },
    {
        "id": "tech_hard_157",
        "text": "Ποιος αλγόριθμος κβαντικής αναζήτησης, που επινόησε ο Lov Grover το 1996, παρέχει τετραγωνική επιτάχυνση O(√N) για την αναζήτηση ενός στοιχείου σε μια αδόμητη βάση δεδομένων N στοιχείων;",
        "correct": "Αλγόριθμος του Grover",
        "distractors": ["Αλγόριθμος του Shor", "Κβαντικό Περπάτημα (Quantum Walk)", "Αλγόριθμος VQE"],
        "explanation": "Ενώ ένας κλασικός υπολογιστής απαιτεί κατά μέσο όρο N/2 συγκρίσεις (O(N)), ο αλγόριθμος του Grover χρησιμοποιεί τον τελεστή διάχυσης (amplitude amplification) για να εντοπίσει το στοιχείο σε περίπου π/4 √N βήματα.",
        "funFacts": [
            "Σημαίνει ότι ένα συμμετρικό κλειδί κρυπτογράφησης AES-128 προσφέρει επίπεδο ασφάλειας μόνο 64-bit απέναντι σε κβαντικό υπολογιστή με αλγόριθμο Grover.",
            "Αυτός είναι ο λόγος που οι ειδικοί ασφαλείας συστήνουν τη μετάβαση σε AES-256 (που διατηρεί ασφάλεια 128-bit έναντι του Grover)."
        ],
        "source": "https://en.wikipedia.org/wiki/Grover%27s_algorithm",
        "tags": ["technology", "quantum_computing", "grovers_algorithm", "algorithms"]
    },
    {
        "id": "tech_hard_158",
        "text": "Ποιος αλγόριθμος κατακερματισμού εικόνων και κειμένων (Locality-Sensitive Hashing) παράγει παρόμοιες τιμές hash για παρόμοια έγγραφα, επιτρέποντας τον άμεσο εντοπισμό σχεδόν διπλότυπου περιεχομένου (near-duplicate detection) στον ιστό;",
        "correct": "SimHash",
        "distractors": ["MD5", "SHA-256", "Bcrypt"],
        "explanation": "Σε αντίθεση με τους κρυπτογραφικούς κατακερματισμούς όπου μια αλλαγή ενός bit ανατρέπει όλο το hash (avalanche effect), στο SimHash (Moses Charikar, 2002) η απόσταση Hamming ανάμεσα στα hashes είναι ανάλογη της ομοιότητας των κειμένων.",
        "funFacts": [
            "Χρησιμοποιείται από την Google (μέσω του web crawler Googlebot) για να εντοπίζει δισεκατομμύρια ιστοσελίδες με πανομοιότυπο περιεχόμενο και να αποφεύγει την περιττή ευρετηρίαση.",
            "Μια παραλλαγή 64-bit του SimHash μπορεί να εντοπίσει σχεδόν ταυτόσημα κείμενα συγκρίνοντας απλώς εάν διαφέρουν κατά 3 ή λιγότερα bits."
        ],
        "source": "https://en.wikipedia.org/wiki/SimHash",
        "tags": ["technology", "algorithms", "hashing", "google", "information_retrieval"]
    },
    {
        "id": "tech_hard_159",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου συναίνεσης Βυζαντινής Ανοχής Σφαλμάτων (PBFT), που δημοσιεύτηκε από τους Miguel Castro και Barbara Liskov το 1999, επιτρέποντας σε κατανεμημένα συστήματα να λειτουργούν σωστά ακόμη κι αν έως και f από τους 3f+1 κόμβους συμπεριφέρονται κακόβουλα;",
        "correct": "PBFT (Practical Byzantine Fault Tolerance)",
        "distractors": ["Raft", "Paxos", "Proof of Work"],
        "explanation": "Το PBFT ήταν το πρώτο πρακτικό πρωτόκολλο που επέλυσε το πρόβλημα των Βυζαντινών Στρατηγών σε ασύγχρονα δίκτυα με πολυωνυμική πολυπλοκότητα O(R²), χρησιμοποιώντας φάσεις Pre-prepare, Prepare και Commit.",
        "funFacts": [
            "Η Barbara Liskov τιμήθηκε με το βραβείο Turing Award το 2008 για τη θεμελιώδη συνεισφορά της στις γλώσσες προγραμματισμού και τα κατανεμημένα συστήματα.",
            "Αποτέλεσε τη βάση για πολλά σύγχρονα συστήματα κοινοπρακτικού blockchain (permissioned blockchains) όπως το Hyperledger Fabric."
        ],
        "source": "https://en.wikipedia.org/wiki/Byzantine_fault#Practical_Byzantine_fault_tolerance",
        "tags": ["technology", "distributed_systems", "pbft", "byzantine_fault", "liskov"]
    },
    {
        "id": "tech_hard_160",
        "text": "Ποιο είναι το όνομα της παραλλαγής του B-Tree, που προτάθηκε από τους Lehman και Yao το 1981, η οποία προσθέτει δείκτες υψηλού επιπέδου (high keys) και δεξιούς συνδέσμους (right sibling pointers) επιτρέποντας ταυτόχρονες αναγνώσεις χωρίς κανένα κλείδωμα (lock-free reads);",
        "correct": "B-link Tree",
        "distractors": ["B+ Tree", "B* Tree", "2-3 Tree"],
        "explanation": "Στο B-link Tree, όταν ένας κόμβος χωρίζεται (split) στα δύο, οι αναγνώστες μπορούν να εντοπίσουν τα δεδομένα ακολουθώντας τον δεξιό σύνδεσμο χωρίς να χρειάζεται να κλειδωθεί το δέντρο από πάνω προς τα κάτω.",
        "funFacts": [
            "Αποτελεί τη βάση των ταυτόχρονων ευρετηρίων (concurrent B-tree indexes) στη μηχανή βάσης δεδομένων PostgreSQL.",
            "Εξαλείφει πλήρως την ανάγκη για κλειδώματα ανάγνωσης κατά την πλοήγηση στο δέντρο, προσφέροντας τεράστια επεκτασιμότητα σε συστήματα πολλών πυρήνων."
        ],
        "source": "https://en.wikipedia.org/wiki/B-link_tree",
        "tags": ["technology", "databases", "concurrency", "data_structures", "b_tree"]
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
    print(f"Loaded {len(questions)} questions for technology_hard.")
    validate_and_append("technology", "hard", 5, questions)

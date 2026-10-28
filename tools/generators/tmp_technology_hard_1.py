"""Generator for technology_hard questions (Batch 1: tech_hard_011 - tech_hard_060)."""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tools.generators.base_generator import validate_and_append

NEW_QUESTIONS = [
    {
        "id": "tech_hard_011",
        "text": "Ποιο πρωτόκολλο δρομολόγησης διανύσματος διαδρομής (path-vector) διαχειρίζεται την ανταλλαγή δεδομένων μεταξύ Αυτόνομων Συστημάτων (AS) στον κορμό του διαδικτύου;",
        "answers": [
            "BGP (Border Gateway Protocol)",
            "OSPF (Open Shortest Path First)",
            "RIP (Routing Information Protocol)",
            "IS-IS"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρωτόκολλο BGP είναι το θεμέλιο της παγκόσμιας δρομολόγησης του διαδικτύου, συνδέοντας μεταξύ τους ανεξάρτητα αυτόνομα δίκτυα.",
        "funFacts": [
            "Λανθασμένες ρυθμίσεις του BGP (BGP misconfigurations) έχουν προκαλέσει στο παρελθόν παγκόσμια blackout σε γίγαντες όπως η Meta και η Cloudflare.",
            "Σχεδιάστηκε αρχικά το 1989 σε τρεις χαρτοπετσέτες κατά τη διάρκεια ενός συνεδρίου της IETF και ονομάστηκε 'Three-Napkin Protocol'."
        ],
        "source": "https://el.wikipedia.org/wiki/BGP",
        "locale": "el-GR",
        "tags": ["networking", "bgp", "internet-routing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_012",
        "text": "Ποιος κλασικός αλγόριθμος εύρεσης συντομότερης διαδρομής σε γράφους μπορεί να διαχειριστεί ακμές με αρνητικά βάρη και να ανιχνεύσει αρνητικούς κύκλους;",
        "answers": [
            "Αλγόριθμος του Dijkstra",
            "Αλγόριθμος Bellman-Ford",
            "Αλγόριθμος A* (A-star)",
            "Αλγόριθμος Kruskal"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο Bellman-Ford μπορεί να υπολογίσει συντομότερες διαδρομές με αρνητικά βάρη, σε αντίθεση με τον αλγόριθμο του Dijkstra που απαιτεί μη αρνητικά βάρη.",
        "funFacts": [
            "Έχει χρονική πολυπλοκότητα O(V·E), καθιστώντας τον πιο αργό από τον Dijkstra αλλά απαραίτητο για πρωτόκολλα distance-vector όπως το RIP.",
            "Αν μετά από V-1 επαναλήψεις μπορεί να γίνει περαιτέρω χαλάρωση ακμής, ο αλγόριθμος συμπεραίνει ότι υπάρχει αρνητικός κύκλος."
        ],
        "source": "https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm",
        "locale": "el-GR",
        "tags": ["algorithms", "graphs", "bellman-ford"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_013",
        "text": "Ποιον μηχανισμό βελτιστοποίησης επιδόσεων των σύγχρονων επεξεργαστών εκμεταλλεύονται οι κρίσιμες ευπάθειες υλικού Meltdown και Spectre (2018);",
        "answers": [
            "Direct Memory Access (DMA)",
            "Dynamic Voltage Scaling",
            "Εικαστική εκτέλεση (Speculative execution)",
            "Hyper-Threading"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Οι επιθέσεις Meltdown και Spectre διαβάζουν μυστικά δεδομένα από την κρυφή μνήμη εκμεταλλευόμενες την εικαστική εκτέλεση εντολών εκτός σειράς (out-of-order).",
        "funFacts": [
            "Κατά την εικαστική εκτέλεση, η CPU εκτελεί κώδικα πριν βεβαιωθεί για τον έλεγχο δικαιωμάτων και, παρότι απορρίπτει τα αποτελέσματα, αφήνει ίχνη στην κρυφή μνήμη (side-channel).",
            "Η αντιμετώπισή τους σε επίπεδο λογισμικού (όπως το KPTI στο Linux) προκάλεσε αισθητή πτώση επιδόσεων σε ορισμένους φόρτους εργασίας."
        ],
        "source": "https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)",
        "locale": "el-GR",
        "tags": ["cybersecurity", "hardware", "cpu", "spectre"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_014",
        "text": "Ποια κρυπτογραφική μέθοδος επιτρέπει σε ένα μέρος να αποδείξει σε ένα άλλο ότι γνωρίζει μια πληροφορία χωρίς να αποκαλύψει την ίδια την πληροφορία;",
        "answers": [
            "Συμμετρική κρυπτογράφηση AES",
            "Συνάρτηση κατακερματισμού HMAC",
            "Ανταλλαγή κλειδιών Diffie-Hellman",
            "Απόδειξη μηδενικής γνώσης (Zero-knowledge proof)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Μια απόδειξη μηδενικής γνώσης (ZKP) επιβεβαιώνει την αλήθεια μιας δήλωσης χωρίς να μεταδίδει καμία επιπλέον πληροφορία πέρα από την εγκυρότητά της.",
        "funFacts": [
            "Η έννοια εισήχθη το 1985 από τους Shafi Goldwasser, Silvio Micali και Charles Rackoff σε ιστορική επιστημονική δημοσίευση.",
            "Αποτελεί τον πυρήνα σύγχρονων κρυπτογραφικών τεχνολογιών προστασίας ιδιωτικότητας όπως τα zk-SNARKs σε δίκτυα blockchain."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-knowledge_proof",
        "locale": "el-GR",
        "tags": ["cryptography", "zero-knowledge", "privacy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_015",
        "text": "Σύμφωνα με το θεώρημα CAP (Brewer's theorem), ποιες τρεις ιδιότητες είναι αδύνατο να εγγυηθεί ταυτόχρονα ένα κατανεμημένο σύστημα δεδομένων;",
        "answers": [
            "Συνέπεια, Διαθεσιμότητα, Ανοχή σε διαμερισμό (Consistency, Availability, Partition tolerance)",
            "Συμπίεση, Ακρίβεια, Απόδοση (Compression, Accuracy, Performance)",
            "Εμπιστευτικότητα, Ακεραιότητα, Προσβασιμότητα (Confidentiality, Integrity, Accessibility)",
            "Ατομικότητα, Συμβατότητα, Ανθεκτικότητα (Atomicity, Compatibility, Durability)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Σε ένα κατανεμημένο σύστημα όπου μπορεί να υπάρξει αποκοπή επικοινωνίας δικτύου (Partition), πρέπει να γίνει επιλογή μεταξύ Συνέπειας και Διαθεσιμότητας.",
        "funFacts": [
            "Το θεώρημα διατυπώθηκε το 2000 από τον Eric Brewer και αποδείχθηκε μαθηματικά το 2002 από τους Seth Gilbert και Nancy Lynch.",
            "Τα παραδοσιακά σχεσιακά συστήματα RDBMS προτιμούν CA/CP, ενώ πολλά NoSQL συστήματα όπως το Cassandra επιλέγουν AP για μέγιστη διαθεσιμότητα."
        ],
        "source": "https://en.wikipedia.org/wiki/CAP_theorem",
        "locale": "el-GR",
        "tags": ["distributed-systems", "cap-theorem", "databases"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_016",
        "text": "Ποιος δημοφιλής αλγόριθμος κατανεμημένης συναίνεσης (consensus) σχεδιάστηκε το 2014 στο Stanford με ρητό στόχο να είναι πιο κατανοητός από το Paxos;",
        "answers": [
            "Chubby",
            "Raft",
            "Byzantine Paxos",
            "Zab"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος Raft αναπτύχθηκε από τους Diego Ongaro και John Ousterhout ως εναλλακτική του δυσνόητου Paxos για διαχείριση replicated state machines.",
        "funFacts": [
            "Χρησιμοποιείται ευρύτατα σε κρίσιμα κατανεμημένα συστήματα υποδομής όπως το etcd (βάση του Kubernetes) και το CockroachDB.",
            "Χωρίζει τη συναίνεση σε διακριτά υποπροβλήματα: εκλογή ηγέτη (Leader Election), αντιγραφή καταγραφών (Log Replication) και ασφάλεια."
        ],
        "source": "https://en.wikipedia.org/wiki/Raft_(algorithm)",
        "locale": "el-GR",
        "tags": ["distributed-systems", "raft", "consensus"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_017",
        "text": "Πώς ονομάζεται η ενδιάμεση αναπαράσταση κώδικα (Intermediate Representation) που αποτελεί τον πυρήνα της σουίτας μεταγλωττιστών LLVM;",
        "answers": [
            "Java Bytecode",
            "CIL (Common Intermediate Language)",
            "LLVM IR",
            "GIMPLE"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το LLVM IR είναι μια καθολική, ανεξάρτητη από τη γλώσσα και την πλακέτα μορφή, πάνω στην οποία εκτελούνται όλες οι βελτιστοποιήσεις του LLVM.",
        "funFacts": [
            "Το έργο LLVM ξεκίνησε το 2000 στο Πανεπιστήμιο του Illinois από τον Vikram Adve και τον Chris Lattner (δημιουργό της γλώσσας Swift).",
            "Γλώσσες όπως η Rust, η Swift, η Clang (C/C++) και η Julia χρησιμοποιούν το LLVM ως backend για την παραγωγή βελτιστοποιημένου μηχανικού κώδικα."
        ],
        "source": "https://en.wikipedia.org/wiki/LLVM",
        "locale": "el-GR",
        "tags": ["compilers", "llvm", "software-engineering"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_018",
        "text": "Ποια είναι η χρονική πολυπλοκότητα στη χειρότερη περίπτωση (worst-case) του αλγορίθμου ταξινόμησης Quicksort;",
        "answers": [
            "O(n)",
            "O(n log n)",
            "O(log n)",
            "O(n^2)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στη χειρότερη περίπτωση, όταν ο οδηγός (pivot) επιλέγει σταθερά το μικρότερο ή μεγαλύτερο στοιχείο, η πολυπλοκότητα του Quicksort υποβαθμίζεται σε O(n²).",
        "funFacts": [
            "Επινοήθηκε το 1959 από τον Tony Hoare κατά τη διάρκεια εργασίας του στη μετάφραση ρωσικών κειμένων.",
            "Στη μέση περίπτωση ο αλγόριθμος είναι εξαιρετικά αποδοτικός με πολυπλοκότητα O(n log n) και εξαιρετική τοπικότητα κρυφής μνήμης (cache locality)."
        ],
        "source": "https://el.wikipedia.org/wiki/Quicksort",
        "locale": "el-GR",
        "tags": ["algorithms", "quicksort", "complexity"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_019",
        "text": "Ποια θεμελιώδης έννοια της θεωρίας πληροφορίας εισήχθη από τον Claude Shannon το 1948 για τη μέτρηση της αβεβαιότητας ή περιεκτικότητας πληροφορίας μιας πηγής;",
        "answers": [
            "Εντροπία πληροφοριών (Information entropy)",
            "Αμοιβαία πληροφορία (Mutual information)",
            "Απόκλιση Kullback-Leibler",
            "Χωρητικότητα διαύλου (Channel capacity)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η εντροπία Shannon μετρά τη μέση ποσότητα πληροφορίας που παράγεται από μια στοχαστική πηγή δεδομένων, μετριέται σε bits (ή shannons).",
        "funFacts": [
            "Ο John von Neumann φέρεται να πρότεινε στον Shannon να την ονομάσει 'εντροπία' επειδή κανείς δεν καταλάβαινε πλήρως την έννοια της εντροπίας στη φυσική.",
            "Η δημοσίευση του 1948 'A Mathematical Theory of Communication' θεωρείται το ιδρυτικό έγγραφο της ψηφιακής εποχής."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%95%CE%BD%CF%84%CF%81%CE%BF%CF%80%CE%AF%CE%B1_%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CF%8E%CE%BD",
        "locale": "el-GR",
        "tags": ["information-theory", "shannon", "entropy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_020",
        "text": "Ποια τεχνική δρομολόγησης χρησιμοποιεί το δίκτυο ανωνυμίας Tor, κρυπτογραφώντας τα δεδομένα σε διαδοχικά στρώματα μέσω ενδιάμεσων κόμβων;",
        "answers": [
            "Mesh routing",
            "Δρομολόγηση κρεμμυδιού (Onion routing)",
            "Packet hopping",
            "Tunnel flooding"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η δρομολόγηση κρεμμυδιού κρυπτογραφεί τα δεδομένα σε πολλαπλά στρώματα· κάθε κόμβος αποκρυπτογραφεί μόνο το δικό του στρώμα για να μάθει τον επόμενο σταθμό.",
        "funFacts": [
            "Η τεχνολογία αναπτύχθηκε αρχικά στα μέσα της δεκαετίας του 1990 από το Ερευνητικό Εργαστήριο του Πολεμικού Ναυτικού των ΗΠΑ (NRL).",
            "Κανένας μεμονωμένος κόμβος στο κύκλωμα Tor δεν γνωρίζει ταυτόχρονα την πραγματική διεύθυνση IP του αποστολέα και του τελικού παραλήπτη."
        ],
        "source": "https://el.wikipedia.org/wiki/Tor_(%CF%80%CF%81%CF%8C%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1)",
        "locale": "el-GR",
        "tags": ["security", "tor", "onion-routing", "privacy"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_021",
        "text": "Πώς ονομάζεται η βασική μονάδα κβαντικής πληροφορίας που μπορεί να βρίσκεται σε υπέρθεση των καταστάσεων 0 και 1;",
        "answers": [
            "Fermion",
            "Anyon",
            "Qubit (κβαντικό bit)",
            "Plasmon"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το qubit είναι το κβαντικό ανάλογο του κλασικού bit και αξιοποιεί τις ιδιότητες της κβαντικής υπέρθεσης και διεμπλοκής.",
        "funFacts": [
            "Ένα σύστημα n qubits μπορεί να αναπαραστήσει ταυτόχρονα 2ⁿ καταστάσεις, παρέχοντας εκθετικό χώρο καταστάσεων σε σχέση με τους κλασικούς υπολογιστές.",
            "Ο όρος qubit επινοήθηκε από τον θεωρητικό φυσικό Benjamin Schumacher σε επιστημονική δημοσίευση του 1995."
        ],
        "source": "https://el.wikipedia.org/wiki/Qubit",
        "locale": "el-GR",
        "tags": ["quantum-computing", "qubit", "physics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_022",
        "text": "Ποιος κβαντικός αλγόριθμος που προτάθηκε το 1994 μπορεί να παραγοντοποιήσει ακέραιους αριθμούς σε πολυωνυμικό χρόνο, θέτοντας σε κίνδυνο την κρυπτογραφία RSA;",
        "answers": [
            "Αλγόριθμος Grover",
            "Αλγόριθμος Deutsch-Jozsa",
            "Αλγόριθμος Simon",
            "Αλγόριθμος Shor"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος του Peter Shor επιλύει την παραγοντοποίηση πρώτων αριθμών και τους διακριτούς λογαρίθμους σε πολυωνυμικό χρόνο σε κβαντικό υπολογιστή.",
        "funFacts": [
            "Η ανακάλυψη του Shor ώθησε την παγκόσμια κρυπτογραφική κοινότητα και το NIST να αναπτύξουν πρότυπα μετακβαντικής κρυπτογραφίας (Post-Quantum Cryptography).",
            "Χρησιμοποιεί τον Κβαντικό Μετασχηματισμό Fourier (QFT) για την εύρεση της περιόδου μιας συνάρτησης, που ανάγει την παραγοντοποίηση σε υπολογίσιμο πρόβλημα."
        ],
        "source": "https://en.wikipedia.org/wiki/Shor%27s_algorithm",
        "locale": "el-GR",
        "tags": ["quantum-computing", "cryptography", "shors-algorithm"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_023",
        "text": "Για ποιο κύριο λόγο οι δομές δεδομένων B-Tree και B+ Tree προτιμώνται έναντι των δυαδικών δέντρων αναζήτησης στα ευρετήρια βάσεων δεδομένων;",
        "answers": [
            "Ελαχιστοποιούν τις λειτουργίες εισόδου/εξόδου (I/O) σε συσκευές αποθήκευσης μπλοκ",
            "Καταλαμβάνουν πάντα λιγότερο χώρο στη μνήμη RAM από απλές λίστες",
            "Δεν απαιτούν ποτέ επανεξισορρόπηση κατά την εισαγωγή νέων στοιχείων",
            "Εγγυώνται γραμμική αναζήτηση O(n) για μέγιστη προβλεψιμότητα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Τα B-Trees έχουν μεγάλο βαθμό διακλάδωσης (fan-out), επιτρέποντας σε κάθε κόμβο να ταιριάζει ακριβώς σε ένα μπλοκ δίσκου και ελαχιστοποιώντας τα αργά disk seeks.",
        "funFacts": [
            "Επινοήθηκαν το 1970 από τους Rudolf Bayer και Edward M. McCreight στα εργαστήρια Boeing Scientific Research Laboratories.",
            "Στα B+ Trees όλα τα πραγματικά δεδομένα αποθηκεύονται αποκλειστικά στα φύλλα, τα οποία συνδέονται μεταξύ τους ως συνδεδεμένη λίστα για ταχύτατες σαρώσεις εύρους."
        ],
        "source": "https://en.wikipedia.org/wiki/B-tree",
        "locale": "el-GR",
        "tags": ["databases", "data-structures", "b-tree"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_024",
        "text": "Στις ιδιότητες ACID των συναλλαγών βάσεων δεδομένων, τι διασφαλίζει το γράμμα 'I' (Isolation);",
        "answers": [
            "Ότι η βάση απομονώνεται από το δίκτυο κατά τη δημιουργία αντιγράφων ασφαλείας",
            "Ότι οι ταυτόχρονες συναλλαγές δεν επηρεάζουν αρνητικά η μία την άλλη",
            "Ότι τα δεδομένα αποθηκεύονται αποκλειστικά σε απομονωμένους δίσκους SSD",
            "Ότι κάθε εγγραφή έχει μοναδικό κρυπτογραφικό αναγνωριστικό"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η Απομόνωση (Isolation) διασφαλίζει ότι η ταυτόχρονη εκτέλεση συναλλαγών παράγει αποτελέσματα ισοδύναμα με σειριακή εκτέλεση.",
        "funFacts": [
            "Το πρότυπο SQL ορίζει τέσσερα επίπεδα απομόνωσης: Read Uncommitted, Read Committed, Repeatable Read και Serializable.",
            "Χαμηλότερα επίπεδα απομόνωσης επιτρέπουν φαινόμενα όπως dirty reads, non-repeatable reads και phantom reads προς όφελος υψηλότερης ταχύτητας."
        ],
        "source": "https://en.wikipedia.org/wiki/Isolation_(database_systems)",
        "locale": "el-GR",
        "tags": ["databases", "acid", "transactions"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_025",
        "text": "Τι είναι το TLB (Translation Lookaside Buffer) στην αρχιτεκτονική μικροεπεξεργαστών;",
        "answers": [
            "Μια ουρά εντολών για παράλληλη αποκωδικοποίηση SIMD",
            "Ένας επιταχυντής επεξεργασίας γραφικών χαμηλής κατανάλωσης",
            "Μια κρυφή μνήμη υλικού που αποθηκεύει πρόσφατες αντιστοιχίσεις εικονικών σε φυσικές διευθύνσεις",
            "Ένας καταχωρητής ελέγχου σφαλμάτων ισοτιμίας της μνήμης RAM"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το TLB λειτουργεί ως ταχύτατη κρυφή μνήμη (cache) για τη Μονάδα Διαχείρισης Μνήμης (MMU), αποτρέποντας αργές προσπελάσεις στους πίνακες σελίδων (page tables).",
        "funFacts": [
            "Όταν μια διεύθυνση δεν βρίσκεται στο TLB (TLB miss), η CPU πρέπει να διατρέξει τον πίνακα σελίδων στη μνήμη (page table walk), καθυστερώντας την εκτέλεση.",
            "Η χρήση Huge Pages (σελίδων μεγέθους 2MB ή 1GB αντί των κλασικών 4KB) μειώνει δραστικά τα TLB misses σε εφαρμογές υψηλών απαιτήσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Translation_lookaside_buffer",
        "locale": "el-GR",
        "tags": ["hardware", "cpu", "memory-management", "tlb"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_026",
        "text": "Ποιο προηγμένο σύστημα αρχείων της Sun Microsystems (2005) συνδύασε διευθυνσιοδότηση 128-bit, μηχανισμό Copy-on-Write και αυτόματη επιδιόρθωση σιωπηρής αλλοίωσης δεδομένων;",
        "answers": [
            "NTFS",
            "ext4",
            "XFS",
            "ZFS"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το ZFS σχεδιάστηκε αρχικά για το Solaris από την ομάδα του Jeff Bonwick, ενσωματώνοντας διαχείριση τόμων και σύστημα αρχείων με αδιάλειπτη επαλήθευση checksums.",
        "funFacts": [
            "Ο χώρος διευθύνσεων 128-bit του ZFS είναι τόσο τεράστιος που θεωρητικά ξεπερνά τον αριθμό των ατόμων που απαιτούνται για να γεμίσουν τη Γη με αποθηκευτικά μέσα.",
            "Χάρη στην αρχιτεκτονική Copy-on-Write, τα υπάρχοντα δεδομένα δεν αντικαθίστανται ποτέ απευθείας, επιτρέποντας σχεδόν στιγμιαία στιγμιότυπα (snapshots)."
        ],
        "source": "https://en.wikipedia.org/wiki/ZFS",
        "locale": "el-GR",
        "tags": ["operating-systems", "file-systems", "zfs", "storage"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_027",
        "text": "Για ποιο φυσικό λόγο τα κελιά δυναμικής μνήμης DRAM απαιτούν περιοδική επαναφόρτιση (refresh) χιλιάδες φορές το δευτερόλεπτο;",
        "answers": [
            "Επειδή οι μικροσκοπικοί πυκνωτές των κελιών διαρρέουν σταδιακά το ηλεκτρικό τους φορτίο",
            "Επειδή τα τρανζίστορ υπερθερμαίνονται και πρέπει να ψύχονται με ηλεκτρικούς παλμούς",
            "Επειδή οι μαγνητικοί πυρήνες της μνήμης αποπροσανατολίζονται από το γήινο μαγνητικό πεδίο",
            "Επειδή ο δίαυλος δεδομένων απαιτεί συνεχή εκκαθάριση παρασιτικών σημάτων"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Κάθε κελί DRAM αποτελείται από ένα μόνο τρανζίστορ και έναν πυκνωτή· το φορτίο του πυκνωτή διαρρέει φυσικά μέσα σε λίγα χιλιοστά του δευτερολέπτου.",
        "funFacts": [
            "Αυτή η ιδιότητα διαφοροποιεί τη DRAM από την ακριβότερη στατική μνήμη SRAM, η οποία χρησιμοποιεί κυκλώματα flip-flop και δεν απαιτεί refresh.",
            "Η ευπάθεια Rowhammer εκμεταλλεύεται τη διαρροή φορτίου: ταχύτατη επανειλημμένη πρόσβαση σε μία γραμμή DRAM μπορεί να αλλοιώσει bit σε γειτονικές γραμμές."
        ],
        "source": "https://en.wikipedia.org/wiki/Dynamic_random-access_memory",
        "locale": "el-GR",
        "tags": ["hardware", "dram", "memory", "physics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_028",
        "text": "Ποια τρισδιάστατη αρχιτεκτονική τρανζίστορ (με προεξέχον πτερύγιο ημιαγωγού) αντικατέστησε τα επίπεδα MOSFET επιτρέποντας την κλιμάκωση κάτω από τα 22nm;",
        "answers": [
            "Bipolar Junction Transistor (BJT)",
            "FinFET",
            "Vacuum Tube",
            "Junction FET (JFET)"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Τα τρανζίστορ FinFET (Fin Field-Effect Transistor) περικλείουν το κανάλι αγωγιμότητας από τρεις πλευρές, περιορίζοντας δραστικά τις διαρροές ρεύματος.",
        "funFacts": [
            "Η Intel εισήγαγε εμπορικά την τεχνολογία το 2011 στους επεξεργαστές Ivy Bridge υπό την ονομασία 'Tri-Gate'.",
            "Σε ακόμα μικρότερες κλίμακες (κάτω των 3nm), η βιομηχανία μεταβαίνει από το FinFET στα τρανζίστορ τύπου GAAFET (Gate-All-Around / Nanosheets)."
        ],
        "source": "https://en.wikipedia.org/wiki/FinFET",
        "locale": "el-GR",
        "tags": ["semiconductors", "finfet", "hardware", "engineering"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_029",
        "text": "Τι περιγράφει ο όρος 'Στένωμα von Neumann' (Von Neumann bottleneck) στην αρχιτεκτονική υπολογιστών;",
        "answers": [
            "Την αδυναμία της αριθμητικής λογικής μονάδας να εκτελέσει διαίρεση με το μηδέν",
            "Τον περιορισμό του μήκους των καλωδίων τροφοδοσίας στους πρώτους υπερυπολογιστές",
            "Τον περιορισμό απόδοσης λόγω κοινού διαύλου δεδομένων και εντολών μεταξύ επεξεργαστή και μνήμης",
            "Την απώλεια πληροφορίας κατά τη μετατροπή αναλογικών σημάτων σε ψηφιακά"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο επεξεργαστής μπορεί να επεξεργαστεί δεδομένα πολύ ταχύτερα από όσο ο κοινός δίαυλος επικοινωνίας μπορεί να μεταφέρει εντολές και δεδομένα από τη μνήμη RAM.",
        "funFacts": [
            "Ο όρος καθιερώθηκε από τον John Backus στη διάσημη διάλεξη απονομής του βραβείου Turing το 1977.",
            "Για τον μετριασμό του στενώματος αναπτύχθηκαν ιεραρχίες κρυφής μνήμης πολλαπλών επιπέδων (L1, L2, L3 cache) και τεχνικές πρόβλεψης διακλαδώσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Von_Neumann_architecture#Von_Neumann_bottleneck",
        "locale": "el-GR",
        "tags": ["computer-architecture", "von-neumann", "hardware"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_030",
        "text": "Ποιο είναι το καθοριστικό δομικό χαρακτηριστικό της καθαρής αρχιτεκτονικής Harvard που τη διακρίνει από την αρχιτεκτονική Von Neumann;",
        "answers": [
            "Χρησιμοποιεί αποκλειστικά αναλογικούς ενισχυτές αντί για ψηφιακές πύλες",
            "Διαθέτει μία ενιαία κρυφή μνήμη για όλα τα υποσυστήματα",
            "Δεν υποστηρίζει καθόλου αριθμητικές πράξεις κινητής υποδιαστολής",
            "Διαθέτει φυσικά ξεχωριστούς διαύλους και μνήμες για εντολές και δεδομένα"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στην αρχιτεκτονική Harvard, η μνήμη εντολών και η μνήμη δεδομένων είναι πλήρως διαχωρισμένες με ξεχωριστούς διαύλους, επιτρέποντας ταυτόχρονη ανάγνωση.",
        "funFacts": [
            "Πήρε το όνομά της από τον υπολογιστή Harvard Mark I, που αποθήκευε εντολές σε διάτρητη χαρτοταινία και δεδομένα σε ηλεκτρομηχανικούς μετρητές.",
            "Οι σύγχρονοι επεξεργαστές x86 και ARM είναι τροποποιημένης αρχιτεκτονικής Harvard: έχουν ξεχωριστές L1 caches για εντολές (L1i) και δεδομένα (L1d)."
        ],
        "source": "https://en.wikipedia.org/wiki/Harvard_architecture",
        "locale": "el-GR",
        "tags": ["computer-architecture", "harvard-architecture", "hardware"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_031",
        "text": "Ποια διάσημη κρίσιμη ευπάθεια ασφαλείας του 2014 στο OpenSSL επέτρεπε σε επιτιθέμενους να διαβάσουν έως 64KB μνήμης διακομιστή ανά παλμό καρδιάς (heartbeat);",
        "answers": [
            "Heartbleed",
            "Shellshock",
            "POODLE",
            "Dirty COW"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το Heartbleed (CVE-2014-0160) ήταν ένα σφάλμα buffer over-read στην υλοποίηση της επέκτασης Heartbeat του TLS στο OpenSSL.",
        "funFacts": [
            "Επέτρεπε την υποκλοπή ιδιωτικών κλειδιών SSL/TLS, κωδικών πρόσβασης χρηστών και συνεδριών χωρίς να αφήνει κανένα ίχνος στα αρχεία καταγραφής.",
            "Υπολογίστηκε ότι επηρέασε περίπου το 17% όλων των ασφαλών διακομιστών web στο διαδίκτυο κατά την ημέρα αποκάλυψής του."
        ],
        "source": "https://el.wikipedia.org/wiki/Heartbleed",
        "locale": "el-GR",
        "tags": ["cybersecurity", "heartbleed", "openssl", "vulnerabilities"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_032",
        "text": "Ποια υπήρξε η ιστορική σημασία της δημοσίευσης του πρωτοκόλλου ανταλλαγής κλειδιών Diffie-Hellman το 1976;",
        "answers": [
            "Ήταν ο πρώτος αλγόριθμος που επέτυχε συμπίεση αρχείων κειμένου",
            "Ήταν η πρώτη δημόσια μέθοδος ασφαλούς ανταλλαγής κοινού μυστικού μέσω ανασφαλούς καναλιού",
            "Δημιούργησε το πρώτο τείχος προστασίας (firewall) για δίκτυα Ethernet",
            "Απέδειξε ότι η κρυπτογράφηση μιας χρήσης (one-time pad) είναι ανασφαλής"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Οι Whitfield Diffie και Martin Hellman έλυσαν το πανάρχαιο πρόβλημα της ασφαλούς διανομής κλειδιών, γεννώντας την κρυπτογραφία δημοσίου κλειδιού.",
        "funFacts": [
            "Βασίζεται στη δυσκολία υπολογισμού διακριτών λογαρίθμων σε πεπερασμένα πεδία.",
            "Χρόνια αργότερα αποχαρακτηρίστηκαν έγγραφα που έδειξαν ότι η βρετανική μυστική υπηρεσία GCHQ είχε ανακαλύψει παρόμοια μέθοδο από το 1970."
        ],
        "source": "https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange",
        "locale": "el-GR",
        "tags": ["cryptography", "diffie-hellman", "security"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_033",
        "text": "Ποιο είναι το κύριο τεχνολογικό πλεονέκτημα της Κρυπτογραφίας Ελλειπτικών Καμπυλών (ECC) σε σύγκριση με τον παραδοσιακό αλγόριθμο RSA;",
        "answers": [
            "Δεν απαιτεί καμία μαθηματική πράξη για την αποκρυπτογράφηση",
            "Μπορεί να υλοποιηθεί αποκλειστικά σε αναλογικά κυκλώματα",
            "Προσφέρει ισοδύναμο επίπεδο ασφάλειας με σημαντικά μικρότερο μέγεθος κλειδιού",
            "Είναι αποδεδειγμένα απρόσβλητη από κάθε μελλοντικό κβαντικό υπολογιστή"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ένα κλειδί ECC 256-bit προσφέρει ασφάλεια συγκρίσιμη με ένα κλειδί RSA 3072-bit, μειώνοντας δραστικά την υπολογιστική επιβάρυνση.",
        "funFacts": [
            "Το μικρό μέγεθος κλειδιού καθιστά την ECC ιδανική για κάρτες SIM, συσκευές IoT και ασφάλεια κινητών συσκευών.",
            "Το Bitcoin και το Ethereum χρησιμοποιούν την καμπύλη secp256k1 της ECC για τις ψηφιακές υπογραφές των συναλλαγών (ECDSA)."
        ],
        "source": "https://en.wikipedia.org/wiki/Elliptic-curve_cryptography",
        "locale": "el-GR",
        "tags": ["cryptography", "ecc", "security"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_034",
        "text": "Ποια είναι η ακριβής ακολουθία σημάτων (TCP flags) που ανταλλάσσεται κατά την τριμερή χειραψία (3-way handshake) εγκαθίδρυσης σύνδεσης TCP;",
        "answers": [
            "ACK, SYN, FIN",
            "PING, PONG, ACK",
            "RST, SYN, ACK",
            "SYN, SYN-ACK, ACK"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο πελάτης στέλνει SYN, ο διακομιστής απαντά με SYN-ACK και ο πελάτης επιβεβαιώνει με ACK, συγχρονίζοντας τους αριθμούς ακολουθίας (sequence numbers).",
        "funFacts": [
            "Η επίθεση SYN Flood εκμεταλλεύεται αυτή τη διαδικασία στέλνοντας αμέτρητα πακέτα SYN χωρίς να στείλει ποτέ το τελικό ACK, εξαντλώντας τη μνήμη του διακομιστή.",
            "Για την αντιμετώπιση του SYN Flood αναπτύχθηκε ο μηχανισμός SYN cookies, που κωδικοποιεί την κατάσταση σύνδεσης στον αριθμό ακολουθίας χωρίς δέσμευση μνήμης."
        ],
        "source": "https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment",
        "locale": "el-GR",
        "tags": ["networking", "tcp", "protocols"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_035",
        "text": "Ποιο είναι το τυπικό προεπιλεγμένο μέγεθος MTU (Maximum Transmission Unit) σε bytes για ένα τυπικό πλαίσιο δικτύου Ethernet v2;",
        "answers": [
            "1.500 bytes",
            "512 bytes",
            "4.096 bytes",
            "9.000 bytes"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το προεπιλεγμένο MTU του Ethernet είναι 1.500 bytes ωφέλιμου φορτίου IP (χωρίς να συνυπολογίζεται η επικεφαλίδα Ethernet).",
        "funFacts": [
            "Πακέτα μεγαλύτερα από το MTU πρέπει να τεμαχιστούν (fragmentation), εκτός εάν έχει ενεργοποιηθεί η σημαία 'Don't Fragment' (DF).",
            "Σε κέντρα δεδομένων χρησιμοποιούνται συχνά 'Jumbo Frames' με μέγεθος MTU έως 9.000 bytes για μείωση της επιβάρυνσης της CPU."
        ],
        "source": "https://en.wikipedia.org/wiki/Maximum_transmission_unit",
        "locale": "el-GR",
        "tags": ["networking", "ethernet", "mtu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_036",
        "text": "Πόσα bits αποτελούν μια διεύθυνση IPv6, σε σύγκριση με τα 32 bits μιας παραδοσιακής διεύθυνσης IPv4;",
        "answers": [
            "64 bits",
            "128 bits",
            "256 bits",
            "512 bits"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Οι διευθύνσεις IPv6 έχουν μήκος 128 bits, παρέχοντας έναν ασύλληπτα μεγάλο χώρο 2¹²⁸ μοναδικών διευθύνσεων (περίπου 3,4 × 10³⁸).",
        "funFacts": [
            "Ο αριθμός των διευθύνσεων IPv6 αντιστοιχεί σε περισσότερες από 665 δισεκατομμύρια τρισεκατομμύρια διευθύνσεις για κάθε τετραγωνικό μέτρο της επιφάνειας της Γης.",
            "Αναπαρίστανται συνήθως σε δεκαεξαδική μορφή χωρισμένη με άνω και κάτω τελείες (π.χ. 2001:0db8:85a3::8a2e:0370:7334)."
        ],
        "source": "https://el.wikipedia.org/wiki/IPv6",
        "locale": "el-GR",
        "tags": ["networking", "ipv6", "protocols"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_037",
        "text": "Ποια υπόθεση στη διαχείριση δυναμικής μνήμης αποτελεί τη βάση των σύγχρονων γενεαλογικών συλλεκτών απορριμμάτων (Generational Garbage Collectors);",
        "answers": [
            "Όλα τα αντικείμενα έχουν ακριβώς την ίδια πιθανότητα διαγραφής ανά πάσα στιγμή",
            "Τα μεγάλα αντικείμενα ζουν πάντα λιγότερο από τους απλούς ακέραιους αριθμούς",
            "Η πλειονότητα των νεοδημιουργηθέντων αντικειμένων παύει να χρησιμοποιείται πολύ γρήγορα (Weak Generational Hypothesis)",
            "Η μνήμη πρέπει να αναδιατάσσεται μόνο όταν γεμίσει πλήρως ο φυσικός δίσκος"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η ασθενής γενεαλογική υπόθεση διαπιστώνει εμπειρικά ότι τα περισσότερα αντικείμενα πεθαίνουν σχεδόν αμέσως μετά τη δημιουργία τους (Gen 0).",
        "funFacts": [
            "Αυτός ο διαχωρισμός επιτρέπει στον Garbage Collector (π.χ. σε Java και .NET) να σαρώνει τακτικά μόνο τη νεαρή γενιά με ελάχιστο κόστος χρόνου.",
            "Τα αντικείμενα που επιβιώνουν από διαδοχικές σαρώσεις 'προάγονται' σε παλαιότερες γενιές (Gen 1 και Gen 2), οι οποίες ελέγχονται πολύ πιο σπάνια."
        ],
        "source": "https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)#Generational_GC",
        "locale": "el-GR",
        "tags": ["programming-languages", "garbage-collection", "memory-management"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_038",
        "text": "Ποιο μαθηματικό φορμαλιστικό μοντέλο υπολογισμού ανέπτυξε ο Alonzo Church τη δεκαετία του 1930, το οποίο αποδείχθηκε ισοδύναμο σε υπολογιστική ισχύ με τη μηχανή Turing;",
        "answers": [
            "Άλγεβρα Boole",
            "Θεωρία αυτομάτων πεπερασμένων καταστάσεων",
            "Δικτυωτά Petri (Petri nets)",
            "Λογισμός λάμδα (Lambda calculus)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο λογισμός λ (λ-calculus) αποτελεί το θεωρητικό θεμέλιο του συναρτησιακού προγραμματισμού (functional programming) και της θεωρίας υπολογισμού.",
        "funFacts": [
            "Η θέση Church-Turing υποστηρίζει ότι οποιαδήποτε υπολογίσιμη συνάρτηση μπορεί να εκτελεστεί είτε σε μηχανή Turing είτε μέσω λογισμού λάμδα.",
            "Γλώσσες όπως η Lisp, η Haskell και η OCaml βασίζονται άμεσα στις αρχές και τη σύνταξη του λογισμού λάμδα."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9B%CE%BF%CE%B3%CE%B9%CF%83%CE%BC%CF%8C%CF%82_%CE%BB%CE%AC%CE%BC%CE%B4%CE%B1",
        "locale": "el-GR",
        "tags": ["computer-science", "lambda-calculus", "turing-complete"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_039",
        "text": "Τι υπολογίζει ο περίφημος νόμος του Amdahl στον παράλληλο προγραμματισμό και την πολυεπεξεργασία;",
        "answers": [
            "Τη θεωρητική μέγιστη επιτάχυνση ενός προγράμματος συναρτήσει του σειριακού του τμήματος",
            "Την αναμενόμενη κατανάλωση ισχύος ενός επεξεργαστή σε μέγιστη συχνότητα",
            "Τον αριθμό των σφαλμάτων λογισμικού ανά χίλιες γραμμές κώδικα",
            "Τη μέγιστη χωρητικότητα εγγραφής σε μαγνητικά αποθηκευτικά μέσα"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο νόμος του Amdahl δείχνει ότι η επιτάχυνση ενός προγράμματος με πολλούς επεξεργαστές περιορίζεται ανυπέρβλητα από το τμήμα του κώδικα που πρέπει να εκτελεστεί σειριακά.",
        "funFacts": [
            "Αν το 5% ενός προγράμματος είναι σειριακό, η μέγιστη θεωρητική επιτάχυνση δεν μπορεί να υπερβεί το 20x, ακόμη και με άπειρους επεξεργαστές.",
            "Διατυπώθηκε το 1967 από τον Gene Amdahl, κορυφαίο αρχιτέκτονα υπερυπολογιστών της IBM και ιδρυτή της Amdahl Corporation."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9D%CF%8C%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%86%CE%BC%CE%BD%CF%84%CE%B1%CE%BB",
        "locale": "el-GR",
        "tags": ["computer-architecture", "amdahl-law", "parallel-computing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_040",
        "text": "Ποιου φυσικού νόμου κλιμάκωσης η κατάρρευση γύρω στο 2005 τερμάτισε την εποχή της ραγδαίας αύξησης συχνότητας ρολογιού των CPU, οδηγώντας στους πολυπύρηνους επεξεργαστές;",
        "answers": [
            "Νόμος του Moore",
            "Κλιμάκωση Dennard (Dennard scaling)",
            "Νόμος του Metcalfe",
            "Νόμος του Little"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η κλιμάκωση Dennard προέβλεπε ότι καθώς τα τρανζίστορ μίκραιναν, η πυκνότητα ισχύος παρέμενε σταθερή· όταν κατέρρευσε λόγω διαρροών ρεύματος, οι επεξεργαστές χτύπησαν το θερμικό τείχος (power wall).",
        "funFacts": [
            "Ενώ ο νόμος του Moore συνέχισε να αυξάνει τον αριθμό των τρανζίστορ, η αδυναμία αύξησης των gigahertz ανάγκασε τους κατασκευαστές να προσθέσουν πολλαπλούς πυρήνες.",
            "Διατυπώθηκε το 1974 από τον Robert H. Dennard, τον ίδιο άνθρωπο που είχε εφεύρει το κελί μνήμης DRAM το 1968."
        ],
        "source": "https://en.wikipedia.org/wiki/Dennard_scaling",
        "locale": "el-GR",
        "tags": ["hardware", "dennard-scaling", "semiconductors", "cpu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_041",
        "text": "Πώς ονομάζεται το μοντέλο παράλληλης εκτέλεσης των καρτών γραφικών της Nvidia, όπου πολλαπλά νήματα εκτελούν την ίδια εντολή πάνω σε διαφορετικά δεδομένα μέσα σε ένα warp;",
        "answers": [
            "MISD (Multiple Instruction, Single Data)",
            "VLIW (Very Long Instruction Word)",
            "SIMT (Single Instruction, Multiple Threads)",
            "MIMD (Multiple Instruction, Multiple Data)"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το SIMT επιτρέπει σε κάθε νήμα να έχει το δικό του μετρητή εντολών και κατάσταση καταχωρητών, συνδυάζοντας την αποδοτικότητα του SIMD με την ευελιξία του multithreading.",
        "funFacts": [
            "Στην αρχιτεκτονική της Nvidia, τα νήματα ομαδοποιούνται σε μονάδες των 32 που ονομάζονται 'warps'.",
            "Αν νήματα μέσα στο ίδιο warp ακολουθήσουν διαφορετικές διακλαδώσεις κώδικα (branch divergence), η GPU εκτελεί διαδοχικά και τα δύο μονοπάτια, μειώνοντας την απόδοση."
        ],
        "source": "https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads",
        "locale": "el-GR",
        "tags": ["gpu", "simt", "nvidia", "parallel-computing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_042",
        "text": "Ποια είναι η υπολογιστική πολυπλοκότητα υπολογισμού ενός Διακριτού Μετασχηματισμού Fourier μήκους N μέσω του αλγορίθμου FFT (Cooley-Tukey);",
        "answers": [
            "O(N)",
            "O(N^2)",
            "O(N^3)",
            "O(N log N)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος Ταχέος Μετασχηματισμού Fourier (FFT) μειώνει τον απαιτούμενο αριθμό πράξεων από O(N²) σε O(N log N), επιτρέποντας την ψηφιακή επεξεργασία σημάτων σε πραγματικό χρόνο.",
        "funFacts": [
            "Δημοσιεύθηκε το 1965 από τους J. W. Cooley και John Tukey, αν και αργότερα ανακαλύφθηκε ότι ο Carl Friedrich Gauss είχε αναπτύξει παρόμοια μέθοδο το 1805.",
            "Εφαρμόζεται παντού: από την επεξεργασία ήχου και ιατρικές απεικονίσεις MRI μέχρι τη συμπίεση εικόνας JPEG και τις τηλεπικοινωνίες 5G OFDM."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A4%CE%B1%CF%87%CF%8D%CF%82_%CE%BC%CE%B5%CF%84%CE%B1%CF%83%CF%87%CE%B7%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CF%8C%CF%82_%CE%A6%CE%BF%CF%85%CF%81%CE%B9%CE%AD",
        "locale": "el-GR",
        "tags": ["algorithms", "fft", "signal-processing", "math"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_043",
        "text": "Ποια είναι η καθοριστική ιδιότητα της πιθανοτικής δομής δεδομένων Φίλτρο Bloom (Bloom Filter);",
        "answers": [
            "Μπορεί να εμφανίσει ψευδώς θετικά αποτελέσματα (false positives), αλλά ποτέ ψευδώς αρνητικά",
            "Μπορεί να εμφανίσει ψευδώς αρνητικά αποτελέσματα, αλλά ποτέ ψευδώς θετικά",
            "Εγγυάται αποθήκευση στοιχείων με μηδενικό σφάλμα και χωρίς καμία χρήση κατακερματισμού",
            "Επιτρέπει την ανάκτηση του αρχικού κειμένου των στοιχείων ανά πάσα στιγμή"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ένα φίλτρο Bloom μπορεί να απαντήσει με βεβαιότητα αν ένα στοιχείο ΔΕΝ ανήκει σε ένα σύνολο, αλλά αν απαντήσει θετικά υπάρχει μικρή πιθανότητα λάθους.",
        "funFacts": [
            "Επινοήθηκε το 1970 από τον Burton Howard Bloom και χρησιμοποιεί έναν πίνακα bit και πολλαπλές συναρτήσεις κατακερματισμού.",
            "Χρησιμοποιείται σε βάσεις δεδομένων (όπως RocksDB, Cassandra) και browsers (Google Chrome) για γρήγορο έλεγχο ύπαρξης πριν γίνει ακριβή ανάγνωση από το δίσκο."
        ],
        "source": "https://en.wikipedia.org/wiki/Bloom_filter",
        "locale": "el-GR",
        "tags": ["data-structures", "bloom-filter", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_044",
        "text": "Σε ένα αυτό-εξισορροπούμενο Κόκκινο-Μαύρο Δέντρο (Red-Black Tree), ποια είναι η μέγιστη δυνατή αναλογία του μήκους της μακρύτερης διαδρομής προς τη συντομότερη διαδρομή από τη ρίζα προς ένα φύλλο;",
        "answers": [
            "Ακριβώς ίση (1 προς 1)",
            "Το πολύ 2 προς 1 (η μακρύτερη διαδρομή είναι το πολύ διπλάσια)",
            "Έως 10 προς 1",
            "Δεν υπάρχει κανένας περιορισμός"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Επειδή κανένα κόκκινο στοιχείο δεν μπορεί να έχει κόκκινο παιδί και όλες οι διαδρομές έχουν ίσο αριθμό μαύρων κόμβων, η μακρύτερη διαδρομή δεν ξεπερνά το διπλάσιο της συντομότερης.",
        "funFacts": [
            "Αυτός ο αυστηρός κανόνας εγγυάται ότι οι λειτουργίες αναζήτησης, εισαγωγής και διαγραφής εκτελούνται πάντα σε χρόνο O(log n).",
            "Χρησιμοποιείται ως η βασική δομή δεδομένων για υλοποιήσεις όπως το std::map της C++ και ο Completely Fair Scheduler (CFS) του πυρήνα Linux."
        ],
        "source": "https://en.wikipedia.org/wiki/Red%E2%80%93black_tree",
        "locale": "el-GR",
        "tags": ["data-structures", "trees", "red-black-tree", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_045",
        "text": "Ποιο μαθηματικό εργαλείο θεωρίας πιθανοτήτων αποτελεί τον πυρήνα του αλγορίθμου PageRank της Google για τη μοντελοποίηση της περιήγησης ενός τυχαίου χρήστη στον ιστό;",
        "answers": [
            "Γραμμικός προγραμματισμός Simplex",
            "Ανάλυση Fourier",
            "Αλυσίδα Markov (στοχαστικός πίνακας μετάβασης)",
            "Αλγόριθμος Viterbi"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο PageRank μοντελοποιεί τον ιστό ως αλυσίδα Markov, υπολογίζοντας τη στάσιμη κατανομή πιθανοτήτων μέσω της κύριας ιδιοτιμής και ιδιοδιανύσματος του πίνακα υπερσυνδέσμων.",
        "funFacts": [
            "Ο παράγοντας απόσβεσης (damping factor, συνήθως 0,85) εκφράζει την πιθανότητα ο χρήστης να συνεχίσει να κάνει κλικ αντί να επιλέξει τυχαία μια νέα σελίδα.",
            "Ονομάστηκε PageRank τόσο από τη λέξη web page όσο και από το επώνυμο του συνιδρυτή της Google, Larry Page."
        ],
        "source": "https://el.wikipedia.org/wiki/PageRank",
        "locale": "el-GR",
        "tags": ["algorithms", "pagerank", "math", "google"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_046",
        "text": "Ποιος μηχανισμός αντικατέστησε πλήρως τα αναδρομικά (RNN) και συνελικτικά (CNN) στρώματα στην αρχιτεκτονική Transformer (Vaswani et al., 2017 'Attention Is All You Need');",
        "answers": [
            "Dynamic Time Warping",
            "Maximum Likelihood Estimation",
            "Support Vector Classification",
            "Αυτο-προσοχή πολλαπλών κεφαλών (Multi-Head Self-Attention)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο μηχανισμός Self-Attention επιτρέπει στο μοντέλο να υπολογίζει συσχετίσεις μεταξύ όλων των λέξεων μιας ακολουθίας ταυτόχρονα, εξαλείφοντας τον σειριακό περιορισμό των RNNs.",
        "funFacts": [
            "Η παράλληλη φύση του Transformer επέτρεψε την εκπαίδευση γιγαντιαίων μοντέλων σε χιλιάδες GPU ταυτόχρονα, οδηγώντας στα σύγχρονα LLMs (όπως GPT και Claude).",
            "Χρησιμοποιεί τρία διανύσματα για κάθε token: Query (Q), Key (K) και Value (V), υπολογίζοντας τα βάρη προσοχής μέσω εσωτερικών γινομένων κλιμακωμένης μορφής."
        ],
        "source": "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)",
        "locale": "el-GR",
        "tags": ["artificial-intelligence", "deep-learning", "transformer", "nlp"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_047",
        "text": "Ποιος κανόνας του διαφορικού λογισμού εφαρμόζεται αναδρομικά στον αλγόριθμο οπισθοδιάδοσης (Backpropagation) για τον υπολογισμό των κλίσεων της συνάρτησης κόστους σε ένα νευρωνικό δίκτυο;",
        "answers": [
            "Κανόνας της αλυσίδας (Chain rule)",
            "Κανόνας του L'Hôpital",
            "Κανόνας του Simpson",
            "Θεώρημα του Rolle"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο κανόνας της αλυσίδας επιτρέπει τον υπολογισμό των μερικών παραγώγων της συνάρτησης σφάλματος ως προς τα βάρη κάθε επιπέδου, ξεκινώντας από την έξοδο προς την είσοδο.",
        "funFacts": [
            "Αν και η βασική μέθοδος είχε περιγραφεί από τη δεκαετία του 1960, διαδόθηκε ευρέως στην τεχνητή νοημοσύνη το 1986 από τους Rumelhart, Hinton και Williams.",
            "Χωρίς το backpropagation και τον αποδοτικό υπολογισμό του μέσω GPU, η σύγχρονη βαθιά μάθηση (deep learning) θα ήταν υπολογιστικά ανέφικτη."
        ],
        "source": "https://en.wikipedia.org/wiki/Backpropagation",
        "locale": "el-GR",
        "tags": ["artificial-intelligence", "machine-learning", "backpropagation", "math"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_048",
        "text": "Ποια ατομική εντολή υλικού (atomic CPU instruction) συγκρίνει τα περιεχόμενα μιας θέσης μνήμης με μια δεδομένη τιμή και τα ενημερώνει μόνο εάν ταιριάζουν, αποτελώντας τη βάση των lock-free αλγορίθμων;",
        "answers": [
            "Test-and-Set",
            "Compare-and-Swap (CAS)",
            "Fetch-and-Add",
            "Load-Linked / Store-Conditional"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η Compare-and-Swap (CAS, όπως η εντολή CMPXCHG στα x86) εκτελείται αδιαίρετα σε επίπεδο υλικού, επιτρέποντας ασφαλή συγχρονισμό νημάτων χωρίς παραδοσιακά locks.",
        "funFacts": [
            "Ένα γνωστό πρόβλημα των lock-free αλγορίθμων που βασίζονται σε CAS είναι το 'πρόβλημα ABA', όπου μια τιμή αλλάζει σε B και ξανά σε A διαφεύγοντας από τον έλεγχο.",
            "Αποτελεί τον πυρήνα κρίσιμων δομών δεδομένων σε βιβλιοθήκες όπως η `java.util.concurrent` και η `System.Threading` του .NET."
        ],
        "source": "https://en.wikipedia.org/wiki/Compare-and-swap",
        "locale": "el-GR",
        "tags": ["concurrency", "multithreading", "hardware", "cpu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_049",
        "text": "Για ποιο λόγο η κλήση συστήματος `epoll` του Linux κλιμακώνεται εξαιρετικά καλύτερα από την παραδοσιακή `select()` κατά τη διαχείριση δεκάδων χιλιάδων ταυτόχρονων συνδέσεων δικτύου;",
        "answers": [
            "Επειδή παρακάμπτει πλήρως το πρωτόκολλο TCP/IP και στέλνει ανεπεξέργαστα πακέτα UDP",
            "Επειδή κρυπτογραφεί αυτόματα όλα τα δεδομένα απευθείας στο επίπεδο του πυρήνα",
            "Επειδή ειδοποιεί σε χρόνο O(1) μόνο για τους περιγραφείς που είχαν δραστηριότητα, αντί να σαρώνει γραμμικά όλους σε χρόνο O(N)",
            "Επειδή αποθηκεύει τα socket descriptors σε μόνιμη βάση δεδομένων SQL"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το `epoll` καταγράφει συμβάντα μέσω callbacks του πυρήνα και επιστρέφει άμεσα μόνο τα ενεργά sockets, επιλύοντας το περίφημο πρόβλημα C10k.",
        "funFacts": [
            "Εισήχθη στον πυρήνα Linux 2.5.44 και αποτελεί τη ραχοκοκαλιά διακομιστών υψηλών επιδόσεων όπως το Nginx, το Redis και το Node.js (μέσω libuv).",
            "Στο FreeBSD και macOS το αντίστοιχο αποδοτικό σύστημα διαχείρισης συμβάντων ονομάζεται `kqueue`, ενώ στα Windows χρησιμοποιείται το `IOCP`."
        ],
        "source": "https://en.wikipedia.org/wiki/Epoll",
        "locale": "el-GR",
        "tags": ["linux", "operating-systems", "epoll", "networking"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_050",
        "text": "Ποιο κρίσιμο πρόβλημα ασφαλείας του αρχικού συστήματος DNS αντιμετωπίζει η σουίτα επεκτάσεων DNSSEC μέσω ψηφιακών υπογραφών και αλυσίδων εμπιστοσύνης;",
        "answers": [
            "Την υπερθέρμανση των root servers από υπερβολική κίνηση",
            "Την έλλειψη διαθέσιμων διευθύνσεων IPv4",
            "Την καθυστέρηση μετάδοσης σημάτων σε υποθαλάσσια καλώδια",
            "Τη δηλητηρίαση κρυφής μνήμης DNS (DNS cache poisoning / DNS spoofing)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το DNSSEC υπογράφει κρυπτογραφικά τις εγγραφές DNS, διασφαλίζοντας ότι η απάντηση προέρχεται από την αυθεντική ζώνη και δεν έχει παραποιηθεί από τρίτους.",
        "funFacts": [
            "Δεν κρυπτογραφεί τα ερωτήματα για προστασία απορρήτου (γι' αυτό χρησιμοποιείται το DoH ή DoT), αλλά εγγυάται αποκλειστικά την αυθεντικότητα και ακεραιότητα των δεδομένων.",
            "Η ρίζα του DNSSEC υπογράφεται με μια τελετουργική διαδικασία (Root Signing Ceremony) που πραγματοποιείται τέσσερις φορές το χρόνο με αυστηρά μέτρα φυσικής ασφάλειας."
        ],
        "source": "https://el.wikipedia.org/wiki/DNSSEC",
        "locale": "el-GR",
        "tags": ["security", "dns", "dnssec", "networking"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_051",
        "text": "Ποια κεντρική οντότητα στο πρωτόκολλο πιστοποίησης Kerberos εκδίδει εισιτήρια Ticket Granting Tickets (TGT) σε χρήστες που συνδέονται επιτυχώς;",
        "answers": [
            "KDC (Key Distribution Center / Authentication Server)",
            "Certificate Authority (CA)",
            "Radius Proxy Gateway",
            "Network Access Server (NAS)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το KDC (Κέντρο Διανομής Κλειδιών) αποτελείται από τον Authentication Server (AS) και τον Ticket Granting Server (TGS), διαχειριζόμενο κεντρικά τα μυστικά κλειδιά.",
        "funFacts": [
            "Αναπτύχθηκε στο MIT στο πλαίσιο του Project Athena και πήρε το όνομά του από τον Κέρβερο, το μυθικό τρικέφαλο σκυλί που φύλαγε τις πύλες του Άδη.",
            "Αποτελεί το προεπιλεγμένο πρωτόκολλο ελέγχου ταυτότητας σε περιβάλλοντα Microsoft Active Directory από την εποχή των Windows 2000."
        ],
        "source": "https://en.wikipedia.org/wiki/Kerberos_(protocol)",
        "locale": "el-GR",
        "tags": ["security", "kerberos", "authentication", "active-directory"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_052",
        "text": "Ποια οικογένεια μικροπυρήνων (microkernels) δεύτερης γενιάς σχεδιάστηκε από τον Jochen Liedtke τη δεκαετία του 1990 για να αποδείξει ότι η διαδιεργασιακή επικοινωνία (IPC) μπορεί να είναι εξαιρετικά ταχεία;",
        "answers": [
            "Mach",
            "L4",
            "Chorus",
            "Amoeba"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο μικροπύρηνας L4 απέδειξε ότι ένας σωστά σχεδιασμένος μικροπύρηνας μπορεί να εκτελεί IPC έως και 20 φορές ταχύτερα από τον παλαιότερο Mach.",
        "funFacts": [
            "Απόγονοι του L4 (όπως ο μαθηματικά επαληθευμένος seL4) χρησιμοποιούνται σε συστήματα κρίσιμης ασφάλειας, στην αεροδιαστημική και στα secure enclaves smartphone.",
            "Ο πηγαίος κώδικας του seL4 είναι ο πρώτος γενικής χρήσης πυρήνας λειτουργικού συστήματος με πλήρη μαθηματική απόδειξη ορθότητας χωρίς σφάλματα υλοποίησης."
        ],
        "source": "https://en.wikipedia.org/wiki/L4_microkernel_family",
        "locale": "el-GR",
        "tags": ["operating-systems", "microkernel", "l4", "sel4"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_053",
        "text": "Τι σημαίνουν τα αρχικά του διεθνούς προτύπου POSIX (IEEE 1003) που διασφαλίζει τη συμβατότητα λογισμικού μεταξύ διαφορετικών παραλλαγών λειτουργικών συστημάτων Unix;",
        "answers": [
            "Protected Open Source Interface for Unix",
            "Parallel Operations and System Interconnect eXchange",
            "Portable Operating System Interface",
            "Programmable Operating System Integrated Extension"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το POSIX (Portable Operating System Interface) ορίζει μια κοινή διεπαφή προγραμματισμού (API), κελύφους και βοηθητικών προγραμμάτων.",
        "funFacts": [
            "Το εύηχο όνομα POSIX προτάθηκε από τον Richard Stallman, ιδρυτή του Free Software Foundation, όταν το IEEE αναζητούσε μια εύκολη ονομασία.",
            "Συστήματα όπως το macOS, διάφορες διανομές Linux, το BSD καθώς και το QNX συμμορφώνονται σε μεγάλο βαθμό με τις προδιαγραφές του POSIX."
        ],
        "source": "https://el.wikipedia.org/wiki/POSIX",
        "locale": "el-GR",
        "tags": ["operating-systems", "posix", "unix", "standards"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_054",
        "text": "Σύμφωνα με το πρότυπο αριθμητικής κινητής υποδιαστολής IEEE 754, πόσα bits κατανέμονται στον εκθέτη (exponent) ενός αριθμού απλής ακρίβειας 32-bit (float);",
        "answers": [
            "4 bits",
            "11 bits",
            "16 bits",
            "8 bits"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Σε έναν 32-bit float, 1 bit διατίθεται για το πρόσημο (sign), 8 bits για τον εκθέτη (με προκατάληψη bias 127) και 23 bits για το κλάσμα/μαντίσα (mantissa).",
        "funFacts": [
            "Στη διπλή ακρίβεια 64-bit (double), ο εκθέτης έχει μήκος 11 bits και η μαντίσα 52 bits, παρέχοντας περίπου 15-17 σημαντικά δεκαδικά ψηφία.",
            "Ειδικές τιμές του εκθέτη δεσμεύονται για την αναπαράσταση του μηδενός, του απείρου (+/- Infinity) και των μη-αριθμών (NaN - Not a Number)."
        ],
        "source": "https://en.wikipedia.org/wiki/Single-precision_floating-point_format",
        "locale": "el-GR",
        "tags": ["computer-science", "ieee-754", "floating-point", "hardware"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_055",
        "text": "Πόσα bytes μπορεί να καταλάβει ένας μεμονωμένος χαρακτήρας (Unicode code point) κατά την κωδικοποίηση στη μορφή UTF-8;",
        "answers": [
            "Από 1 έως 4 bytes",
            "Ακριβώς και σταθερά 2 bytes",
            "Από 2 έως 8 bytes",
            "Ακριβώς 1 byte για όλες τις γλώσσες"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το UTF-8 είναι κωδικοποίηση μεταβλητού μήκους που χρησιμοποιεί από 1 byte (για χαρακτήρες ASCII) έως 4 bytes για πιο σύνθετα σύμβολα και emojis.",
        "funFacts": [
            "Σχεδιάστηκε το 1992 από τον Ken Thompson και τον Rob Pike σε ένα δείπνο σε εστιατόριο για το λειτουργικό σύστημα Plan 9.",
            "Είναι πλήρως συμβατό προς τα πίσω με το ASCII, γεγονός που συνέβαλε στο να κυριαρχήσει σε πάνω από το 98% όλων των ιστοσελίδων του διαδικτύου."
        ],
        "source": "https://el.wikipedia.org/wiki/UTF-8",
        "locale": "el-GR",
        "tags": ["software-engineering", "utf-8", "unicode", "encoding"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_056",
        "text": "Ποιο ευρέως διαδεδομένο πρότυπο ανταλλαγής μηνυμάτων αποτελεί το defacto εργαλείο προγραμματισμού παράλληλων εφαρμογών σε υπερυπολογιστές και συστάδες κατανεμημένης μνήμης;",
        "answers": [
            "OpenMP",
            "MPI (Message Passing Interface)",
            "CORBA",
            "SOAP"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το MPI είναι ένα τυποποιημένο API επικοινωνίας που επιτρέπει σε ανεξάρτητες διεργασίες σε διαφορετικούς κόμβους να ανταλλάσσουν μηνύματα μέσω δικτύου υψηλής ταχύτητας.",
        "funFacts": [
            "Σε αντίθεση με το OpenMP που απαιτεί κοινόχρηστη μνήμη στον ίδιο υπολογιστή, το MPI σχεδιάστηκε εξαρχής για κατανεμημένη αρχιτεκτονική (cluster computing).",
            "Σχεδόν όλοι οι υπερυπολογιστές της λίστας TOP500 βασίζονται σε υλοποιήσεις MPI (όπως Open MPI ή MPICH) για την εκτέλεση επιστημονικών προσομοιώσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Message_Passing_Interface",
        "locale": "el-GR",
        "tags": ["high-performance-computing", "mpi", "supercomputers", "parallel-computing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_057",
        "text": "Στα συστήματα βάσεων δεδομένων, ποιος είναι ο πρωταρχικός ρόλος του μηχανισμού Write-Ahead Logging (WAL);",
        "answers": [
            "Να συμπιέζει αυτόματα τα παλιά αρχεία καταγραφής για εξοικονόμηση χώρου",
            "Να αποστέλλει αντίγραφα των ερωτημάτων SQL στους διαχειριστές μέσω email",
            "Να διασφαλίζει την Ατομικότητα και την Ανθεκτικότητα (Durability) καταγράφοντας αλλαγές πριν αυτές γραφτούν στις σελίδες δεδομένων",
            "Να αποτρέπει επιθέσεις SQL injection σε πραγματικό χρόνο"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Με το WAL, καμία αλλαγή δεν γράφεται στον κύριο πίνακα δεδομένων εάν δεν καταγραφεί πρώτα σειριακά στο log δίσκου, επιτρέποντας ανάκαμψη μετά από διακοπή ρεύματος.",
        "funFacts": [
            "Επειδή οι εγγραφές στο WAL είναι σειριακές (sequential append-only), είναι τάξεις μεγέθους ταχύτερες από τις τυχαίες εγγραφές (random writes) στις σελίδες δεδομένων.",
            "Χρησιμοποιείται από σχεδόν όλες τις σύγχρονες βάσεις, συμπεριλαμβανομένων των PostgreSQL, SQLite, MySQL (InnoDB redo log) και SQL Server."
        ],
        "source": "https://en.wikipedia.org/wiki/Write-ahead_logging",
        "locale": "el-GR",
        "tags": ["databases", "wal", "storage", "durability"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_058",
        "text": "Ποιες είναι οι δύο διακριτές φάσεις στο κλασικό πρωτόκολλο Two-Phase Commit (2PC) για την ολοκλήρωση συναλλαγών σε κατανεμημένες βάσεις δεδομένων;",
        "answers": [
            "Φάση κρυπτογράφησης και φάση αποκρυπτογράφησης",
            "Φάση συμπίεσης και φάση αποσυμπίεσης",
            "Φάση εκλογής ηγέτη και φάση συγχρονισμού ρολογιών",
            "Φάση προετοιμασίας (Prepare phase) και φάση δέσμευσης (Commit phase)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στην πρώτη φάση ο συντονιστής ρωτά όλους τους κόμβους αν είναι έτοιμοι να δεσμεύσουν την αλλαγή (Prepare/Vote), και στη δεύτερη δίνει την εντολή οριστικής δέσμευσης (Commit) ή ακύρωσης (Rollback).",
        "funFacts": [
            "Το μεγαλύτερο μειονέκτημα του 2PC είναι ότι είναι ένα πρωτόκολλο 'εμπλοκής' (blocking): αν ο συντονιστής καταρρεύσει στη μέση, οι κόμβοι μπορεί να μείνουν σε αδιέξοδο.",
            "Για τον μετριασμό αυτής της εμπλοκής αναπτύχθηκε το πιο πολύπλοκο πρωτόκολλο Three-Phase Commit (3PC)."
        ],
        "source": "https://en.wikipedia.org/wiki/Two-phase_commit_protocol",
        "locale": "el-GR",
        "tags": ["databases", "distributed-systems", "2pc", "transactions"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_059",
        "text": "Ποιο αρνητικό φαινόμενο αποτρέπεται στους σύγχρονους υπερβαθμωτούς (superscalar) επεξεργαστές χάρη στην επιτυχή δυναμική πρόβλεψη διακλαδώσεων (Branch Prediction);",
        "answers": [
            "Το πάγωμα και η εκκαθάριση της σωλήνωσης εντολών (Pipeline stall / Pipeline flush)",
            "Η υπερβολική φόρτιση των πυκνωτών του τροφοδοτικού της μητρικής",
            "Η αυτόματη επανεκκίνηση του λειτουργικού συστήματος λόγω Kernel Panic",
            "Η αλλοίωση των δεδομένων στους εξωτερικούς δίσκους USB"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Σε περίπτωση λανθασμένης πρόβλεψης διακλάδωσης (branch misprediction), όλες οι εντολές που φορτώθηκαν στη σωλήνωση πρέπει να απορριφθούν, σπαταλώντας 10 έως 20 κύκλους ρολογιού.",
        "funFacts": [
            "Οι σύγχρονες CPU χρησιμοποιούν εξαιρετικά εξελιγμένους προβλεπτές βασισμένους σε νευρωνικά δίκτυα τύπου TAGE με ποσοστά ακρίβειας άνω του 95%.",
            "Όσο μεγαλύτερο είναι το βάθος της σωλήνωσης εντολών (pipeline depth), τόσο μεγαλύτερο είναι το κόστος ποινής σε κύκλους ανά αστοχία πρόβλεψης."
        ],
        "source": "https://en.wikipedia.org/wiki/Branch_predictor",
        "locale": "el-GR",
        "tags": ["hardware", "cpu", "branch-prediction", "architecture"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_060",
        "text": "Ποια είναι η ουσιαστική λειτουργία του ελεγκτή DMA (Direct Memory Access) στην αρχιτεκτονική ηλεκτρονικών υπολογιστών;",
        "answers": [
            "Να εκτελεί εντολές μηχανής όταν η κύρια CPU έχει απενεργοποιηθεί λόγω υπερθέρμανσης",
            "Να επιτρέπει σε περιφερειακές συσκευές I/O να μεταφέρουν δεδομένα απευθείας από/προς τη RAM χωρίς συνεχή εμπλοκή της CPU",
            "Να μετατρέπει αυτόματα την αναλογική τάση του ρεύματος σε ψηφιακά δεδομένα",
            "Να κρυπτογραφεί τα δεδομένα της μνήμης σε πραγματικό χρόνο"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το DMA αναλαμβάνει τη μεταφορά μεγάλων όγκων δεδομένων μεταξύ περιφερειακών συσκευών (π.χ. κάρτες δικτύου, δίσκοι) και RAM, απελευθερώνοντας την CPU για άλλες διεργασίες.",
        "funFacts": [
            "Χωρίς DMA, η CPU θα έπρεπε να εκτελεί εντολές ανάγνωσης και εγγραφής byte προς byte για κάθε μεταφορά (Programmed I/O), γονατίζοντας το σύστημα.",
            "Στα σύγχρονα συστήματα χρησιμοποιείται το Bus Mastering και εξειδικευμένες μονάδες IOMMU για προστασία της μνήμης από κακόβουλες συσκευές DMA."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%86%CE%BC%CE%B5%CF%83%CE%B7_%CF%80%CF%81%CE%BF%CF%83%CF%80%CE%AD%CE%BB%CE%B1%CF%83%CE%B7_%CE%BC%CE%BD%CE%AE%CE%BC%CE%B7%CF%82",
        "locale": "el-GR",
        "tags": ["hardware", "dma", "computer-architecture", "memory"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == "__main__":
    print(f"Total questions to append: {len(NEW_QUESTIONS)}")
    validate_and_append("technology", "hard", 5, NEW_QUESTIONS)

# -*- coding: utf-8 -*-
import sys
import os
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

raw_questions = [
    {
        "id": "tech_hard_161",
        "text": "Ποιοι δύο βασικοί μηχανισμοί του πυρήνα του Linux (namespaces και control groups - cgroups) αποτέλεσαν τα θεμέλια για τη δημιουργία της τεχνολογίας απομόνωσης κοντέινερ (containers) όπως το Docker;",
        "correct": "Namespaces και cgroups",
        "distractors": ["Seccomp και AppArmor", "KVM και QEMU", "Systemd και Chroot"],
        "explanation": "Τα Linux namespaces παρέχουν την ψευδαίσθηση απομόνωσης πόρων (διεργασίες, δίκτυο, σημεία προσάρτησης), ενώ τα cgroups (Al Viro, Paul Menage, Rohit Seth) περιορίζουν και καταμετρούν τη χρήση φυσικών πόρων (CPU, μνήμη, I/O).",
        "funFacts": [
            "Τα cgroups αναπτύχθηκαν αρχικά από μηχανικούς της Google το 2006 υπό το όνομα 'process containers' πριν ενσωματωθούν στον πυρήνα Linux 2.6.24.",
            "Υπάρχουν 8 διαφορετικά namespaces στο σύγχρονο Linux: PID, NET, MNT, IPC, UTS, USER, CGROUP και TIME."
        ],
        "source": "https://en.wikipedia.org/wiki/Cgroups",
        "tags": ["technology", "linux", "containers", "docker", "operating_systems"]
    },
    {
        "id": "tech_hard_162",
        "text": "Ποιο σύστημα αρχείων (filesystem) επόμενης γενιάς, που σχεδιάστηκε αρχικά από τη Sun Microsystems για το Solaris, χρησιμοποιεί αντιγραφή κατά την εγγραφή (Copy-on-Write) και κρυπτογραφικό άθροισμα ελέγχου (checksumming) σε όλα τα μπλοκ δεδομένων;",
        "correct": "ZFS",
        "distractors": ["ext4", "NTFS", "XFS"],
        "explanation": "Το ZFS εξαλείφει τη σιωπηλή αλλοίωση δεδομένων (silent data corruption ή bit rot) επαληθεύοντας κάθε μπλοκ κατά την ανάγνωση με Merkle tree checksums και διορθώνοντάς το αυτόματα από εφεδρικά αντίγραφα.",
        "funFacts": [
            "Το 'Z' στο ZFS αντιπροσώπευε αρχικά το 'Zettabyte', υποδηλώνοντας τη σχεδόν απεριόριστη θεωρητική χωρητικότητα 128-bit του συστήματος αρχείων.",
            "Περιλαμβάνει μια υπερσύγχρονη κρυφή μνήμη δύο επιπέδων: το ARC (Adaptive Replacement Cache) στη RAM και το L2ARC σε γρήγορους δίσκους SSD."
        ],
        "source": "https://en.wikipedia.org/wiki/ZFS",
        "tags": ["technology", "storage", "zfs", "filesystems", "operating_systems"]
    },
    {
        "id": "tech_hard_163",
        "text": "Ποιος αλγόριθμος ανάκτησης βάσεων δεδομένων μετά από κατάρρευση (crash recovery), που αναπτύχθηκε από τον C. Mohan στην IBM το 1992, εισήγαγε τη χρήση του Write-Ahead Logging (WAL) με αντιστάθμιση φυσικών και λογικών καταγραφών;",
        "correct": "ARIES (Algorithms for Recovery and Isolation Exploiting Semantics)",
        "distractors": ["2PC", "MVCC", "Shadow Paging"],
        "explanation": "Ο αλγόριθμος ARIES εκτελεί τρεις διαδοχικές φάσεις κατά την ανάκτηση: Φάση Ανάλυσης (Analysis), Φάση Επανάληψης (Redo - επαναφορά της κατάστασης ακριβώς πριν την κατάρρευση) και Φάση Αναίρεσης (Undo - ακύρωση μη δεσμευμένων συναλλαγών).",
        "funFacts": [
            "Αποτελεί το πρότυπο ανάκτησης που υλοποιείται σχεδόν σε όλα τα μεγάλα συστήματα RDBMS όπως το DB2, το Microsoft SQL Server, η PostgreSQL και η MySQL InnoDB.",
            "Εισήγαγε τα Compensation Log Records (CLRs) για να διασφαλίσει ότι οι ενέργειες ακύρωσης δεν θα επαναληφθούν εάν το σύστημα καταρρεύσει ξανά κατά τη διάρκεια της ίδιας της ανάκτησης."
        ],
        "source": "https://en.wikipedia.org/wiki/Algorithms_for_Recovery_and_Isolation_Exploiting_Semantics",
        "tags": ["technology", "databases", "recovery", "aries", "wal"]
    },
    {
        "id": "tech_hard_164",
        "text": "Ποια τεχνική εκμετάλλευσης ευπαθειών μνήμης (binary exploitation) παρακάμπτει την προστασία μη-εκτελέσιμης στοίβας (DEP/NX bit) συνδέοντας μικρές ακολουθίες υπαρχουσών εντολών μηχανής που καταλήγουν σε εντολή 'ret' (gadgets);",
        "correct": "Προγραμματισμός Προσανατολισμένος στην Επιστροφή (Return-Oriented Programming - ROP)",
        "distractors": ["Υπερχείλιση Εικονικού Πίνακα (vtable hijacking)", "Heap Spraying", "Format String Attack"],
        "explanation": "Το ROP (Hovav Shacham, 2007) επιτρέπει σε έναν επιτιθέμενο να εκτελέσει αυθαίρετο υπολογισμό (Turing-complete) τοποθετώντας διευθύνσεις 'gadgets' στη στοίβα, χωρίς να εισάγει καθόλου νέο εκτελέσιμο κώδικα.",
        "funFacts": [
            "Για την αντιμετώπιση του ROP αναπτύχθηκε ο συνδυασμός του ASLR (που τυχαιοποιεί τις διευθύνσεις μνήμης) και σύγχρονες τεχνολογίες υλικού όπως το Intel CET (Control-flow Enforcement Technology).",
            "Το πρώτο επιστημονικό άρθρο για το ROP απέδειξε ότι οποιοδήποτε πρόγραμμα στην αρχιτεκτονική x86 περιέχει αρκετά gadgets στη βιβλιοθήκη libc για πλήρη έλεγχο."
        ],
        "source": "https://en.wikipedia.org/wiki/Return-oriented_programming",
        "tags": ["technology", "security", "rop", "exploitation", "hardware"]
    },
    {
        "id": "tech_hard_165",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ταυτοποίησης δικτύου που βασίζεται σε αξιόπιστο τρίτο μέρος (KDC - Key Distribution Center) και εισιτήρια πρόσβασης (tickets), χρησιμοποιούμενο ως η προεπιλεγμένη μέθοδος ελέγχου ταυτότητας στο Active Directory των Windows;",
        "correct": "Kerberos",
        "distractors": ["NTLM", "OAuth 2.0", "RADIUS"],
        "explanation": "Το Kerberos (που αναπτύχθηκε στο MIT στο πλαίσιο του Project Athena) χρησιμοποιεί συμμετρική κρυπτογραφία και Ticket Granting Tickets (TGT) για να επιτρέψει σε κόμβους να πιστοποιούν την ταυτότητά τους χωρίς να στέλνουν κωδικούς πρόσβασης στο δίκτυο.",
        "funFacts": [
            "Πήρε το όνομά του από τον μυθικό τρικέφαλο σκύλο Κέρβερο που φύλαγε τις πύλες του Άδη, συμβολίζοντας τα τρία μέρη του πρωτοκόλλου: τον Πελάτη, τον Διακομιστή και το KDC.",
            "Είναι εξαιρετικά ευαίσθητο στον συγχρονισμό ώρας: εάν το ρολόι του υπολογιστή διαφέρει περισσότερο από 5 λεπτά από τον διακομιστή, η ταυτοποίηση αποτυγχάνει."
        ],
        "source": "https://en.wikipedia.org/wiki/Kerberos_(protocol)",
        "tags": ["technology", "security", "kerberos", "authentication", "networking"]
    },
    {
        "id": "tech_hard_166",
        "text": "Ποιο είναι το όνομα της τεχνολογίας του πυρήνα του Linux που επιτρέπει την ασφαλή εκτέλεση προσαρμοσμένου bytecode μέσα στον ίδιο τον πυρήνα χωρίς αλλαγή του πηγαίου κώδικα ή φόρτωση εξωτερικών kernel modules;",
        "correct": "eBPF (extended Berkeley Packet Filter)",
        "distractors": ["Kprobes", "Ftrace", "SystemTap"],
        "explanation": "Το eBPF επαληθεύεται από έναν αυστηρό in-kernel verifier (για να διασφαλιστεί ότι δεν περιέχει ατέρμονες βρόχους ή παράνομες προσπελάσεις μνήμης) και μεταγλωττίζεται JIT σε native κώδικα μηχανής για παρατήρηση (observability), ασφάλεια και ταχύτατη δρομολόγηση δικτύου (XDP).",
        "funFacts": [
            "Χαρακτηρίστηκε από τον δημιουργό του Linux, Linus Torvalds, και άλλους κορυφαίους μηχανικούς ως 'το JavaScript του πυρήνα του Linux'.",
            "Χρησιμοποιείται από κολοσσούς όπως το Facebook, το Netflix και το Cloudflare για την προστασία από επιθέσεις DDoS και την παρακολούθηση μικροϋπηρεσιών (Cilium)."
        ],
        "source": "https://en.wikipedia.org/wiki/EBPF",
        "tags": ["technology", "linux", "ebpf", "kernel", "networking"]
    },
    {
        "id": "tech_hard_167",
        "text": "Ποιος αλγόριθμος κατακερματισμού κωδικών πρόσβασης (password hashing), που κέρδισε τον διεθνή διαγωνισμό Password Hashing Competition (PHC) το 2015, σχεδιάστηκε ειδικά για να είναι ανθεκτικός σε επιθέσεις μέσω GPUs και ASICs όντας 'memory-hard';",
        "correct": "Argon2 (Argon2id)",
        "distractors": ["PBKDF2", "bcrypt", "scrypt"],
        "explanation": "Το Argon2 (Alex Biryukov, Daniel Dinu, Dmitry Khovratovich) επιτρέπει τη ρύθμιση του χρόνου εκτέλεσης, της απαίτησης μνήμης και του αριθμού παράλληλων νημάτων, καθιστώντας τις μαζικές επιθέσεις υλικού εξαιρετικά ασύμφορες οικονομικά.",
        "funFacts": [
            "Η έκδοση Argon2d προστατεύει από GPU cracking χρησιμοποιώντας προσπελάσεις μνήμης εξαρτώμενες από δεδομένα, ενώ η Argon2i προστατεύει από timing attacks.",
            "Η υβριδική έκδοση Argon2id συνδυάζει τα καλύτερα χαρακτηριστικά και αποτελεί τη διεθνή προτεινόμενη βέλτιστη πρακτική από τον οργανισμό OWASP."
        ],
        "source": "https://en.wikipedia.org/wiki/Argon2",
        "tags": ["technology", "cryptography", "security", "passwords", "argon2"]
    },
    {
        "id": "tech_hard_168",
        "text": "Ποιο είναι το όνομα του νόμου της παράλληλης επεξεργασίας, που διατυπώθηκε από τον Gene Amdahl το 1967, ο οποίος θέτει το θεωρητικό ανώτατο όριο επιτάχυνσης ενός προγράμματος από την ύπαρξη του σειριακού (μη παραλληλοποιήσιμου) τμήματός του;",
        "correct": "Νόμος του Άμνταλ (Amdahl's law)",
        "distractors": ["Νόμος του Γκούσταφσον", "Νόμος του Μουρ", "Νόμος του Μέτκαλφ"],
        "explanation": "Ο Νόμος του Amdahl δηλώνει ότι εάν το 10% ενός προγράμματος είναι αυστηρά σειριακό, η μέγιστη θεωρητική επιτάχυνση δεν μπορεί ποτέ να υπερβεί το 10x, ανεξάρτητα από το αν θα χρησιμοποιηθούν χιλιάδες επεξεργαστές.",
        "funFacts": [
            "Σε απάντηση στον νόμο του Amdahl, ο John Gustafson διατύπωσε το 1988 τον Νόμο του Gustafson, υποστηρίζοντας ότι σε μεγάλα προβλήματα το μέγεθος του παράλληλου τμήματος αυξάνεται όσο αυξάνονται οι διαθέσιμοι πόροι.",
            "Ο Amdahl ήταν ο επικεφαλής αρχιτέκτονας του θρυλικού mainframe υπολογιστή IBM System/360."
        ],
        "source": "https://en.wikipedia.org/wiki/Amdahl%27s_law",
        "tags": ["technology", "parallel_computing", "amdahls_law", "cpu", "performance"]
    },
    {
        "id": "tech_hard_169",
        "text": "Ποιο είναι το όνομα της δομής δεδομένων κατευθυνόμενου ακυκλικού γραφήματος βασισμένου σε περιεχόμενο (Content-Addressed Merkle DAG) που χρησιμοποιείται εσωτερικά από το σύστημα ελέγχου εκδόσεων Git για την αναπαράσταση αρχείων, καταλόγων και commits;",
        "correct": "Merkle DAG",
        "distractors": ["B-Tree", "Skip List", "Red-Black Tree"],
        "explanation": "Στο Git, κάθε αντικείμενο (blob, tree, commit) ταυτοποιείται μοναδικά από το κρυπτογραφικό του hash SHA-1 (ή SHA-256), καθιστώντας ολόκληρο το ιστορικό ένα αμετάβλητο Merkle DAG όπου κάθε αλλαγή αλλάζει όλα τα μεταγενέστερα hashes.",
        "funFacts": [
            "Αυτός ο σχεδιασμός επιτρέπει στο Git να ανιχνεύει άμεσα οποιαδήποτε αλλοίωση ή παραποίηση ιστορικού.",
            "Η ίδια αρχιτεκτονική Merkle DAG χρησιμοποιείται επίσης από το διαπλανητικό σύστημα αρχείων IPFS."
        ],
        "source": "https://en.wikipedia.org/wiki/Merkle_tree#Directed_acyclic_graph",
        "tags": ["technology", "git", "merkle_dag", "data_structures", "cryptography"]
    },
    {
        "id": "tech_hard_170",
        "text": "Ποιος αλγόριθμος κατανομής καταχωρητών (Register Allocation) σε μεταγλωττιστές, που επινοήθηκε από τον Gregory Chaitin στην IBM το 1981, ανάγει το πρόβλημα της ανάθεσης μεταβλητών στους φυσικούς καταχωρητές της CPU στο πρόβλημα χρωματισμού γραφήματος;",
        "correct": "Αλγόριθμος Chaitin (Graph Coloring Register Allocation)",
        "distractors": ["Linear Scan Allocation", "Belady Spill Algorithm", "Tree Rewriting"],
        "explanation": "Ο αλγόριθμος κατασκευάζει ένα γράφημα παρεμβολής (interference graph) όπου οι κόμβοι είναι οι μεταβλητές και οι ακμές συνδέουν μεταβλητές που είναι ταυτόχρονα ενεργές (live), προσπαθώντας να το χρωματίσει με k χρώματα (όπου k ο αριθμός των διαθέσιμων καταχωρητών).",
        "funFacts": [
            "Επειδή ο χρωματισμός γραφήματος είναι NP-πλήρες πρόβλημα, χρησιμοποιούνται αποδοτικές ευρετικές μέθοδοι βασισμένες στο θεώρημα του Kempe.",
            "Εάν ένα γράφημα δεν μπορεί να χρωματιστεί με k χρώματα, επιλέγονται μεταβλητές για 'διαρροή' (spilling) στη μνήμη RAM."
        ],
        "source": "https://en.wikipedia.org/wiki/Register_allocation#Graph_coloring",
        "tags": ["technology", "compilers", "register_allocation", "graph_theory", "chaitin"]
    },
    {
        "id": "tech_hard_171",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου άμυνας κατά των επιθέσεων SYN Flood στο TCP, το οποίο επινόησε ο Daniel J. Bernstein το 1996, κωδικοποιώντας τις παραμέτρους της σύνδεσης μέσα στον αρχικό αριθμό σειράς (Initial Sequence Number) χωρίς να δεσμεύει μνήμη στον διακομιστή;",
        "correct": "SYN Cookies",
        "distractors": ["TCP Fast Open", "SYN Cache", "Random Drop"],
        "explanation": "Με τα SYN Cookies, ο διακομιστής δεν αποθηκεύει καμία κατάσταση στον πίνακα συνδέσεων κατά τη λήψη του πακέτου SYN, αλλά ανακατασκευάζει την εγκυρότητα της σύνδεσης μόνο όταν λάβει το τελικό πακέτο ACK του πελάτη.",
        "funFacts": [
            "Αποτρέπει την εξάντληση της μνήμης (SYN backlog exhaustion) ακόμη κι αν ο διακομιστής δέχεται εκατομμύρια πλαστά πακέτα SYN το δευτερόλεπτο.",
            "Μικρό μειονέκτημά του είναι ότι περιορίζει ελαφρώς ορισμένες προηγμένες επιλογές TCP, όπως το μέγεθος του παραθύρου (Window Scale), εκτός αν χρησιμοποιηθούν TCP Timestamps."
        ],
        "source": "https://en.wikipedia.org/wiki/SYN_cookies",
        "tags": ["technology", "networking", "security", "tcp", "ddos"]
    },
    {
        "id": "tech_hard_172",
        "text": "Ποια είναι η βασική αρχή του σχήματος διαμοιρασμού μυστικού του Adi Shamir (Shamir's Secret Sharing, 1979), σύμφωνα με την οποία ένα μυστικό χωρίζεται σε n μερίδια και απαιτούνται τουλάχιστον k από αυτά για την ανάκτησή του;",
        "correct": "Παρεμβολή Πολυωνύμου Lagrange βαθμού k-1 πάνω από ένα πεπερασμένο σώμα",
        "distractors": [
            "Παραγοντοποίηση πρώτων αριθμών RSA",
            "Διαίρεση μυστικού με απλή πράξη XOR",
            "Πολλαπλασιασμός ελλειπτικών καμπυλών"
        ],
        "explanation": "Στο σχήμα του Shamir (k, n threshold), το μυστικό είναι ο σταθερός όρος ενός τυχαίου πολυωνύμου βαθμού k-1. Οποιαδήποτε k σημεία μπορούν να ανακατασκευάσουν μοναδικά το πολυώνυμο μέσω Lagrange interpolation, ενώ k-1 σημεία δεν αποκαλύπτουν απολύτως καμία πληροφορία.",
        "funFacts": [
            "Προσφέρει πληροφοριακά τέλεια ασφάλεια (Information-theoretic security), που σημαίνει ότι δεν μπορεί να σπάσει ούτε με άπειρη υπολογιστική ισχύ.",
            "Χρησιμοποιείται για την ασφαλή φύλαξη ριζικών κλειδιών κρυπτογράφησης, εκτοξεύσεων πυρηνικών όπλων και master keys σε οργανισμούς."
        ],
        "source": "https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing",
        "tags": ["technology", "cryptography", "shamir", "math", "security"]
    },
    {
        "id": "tech_hard_173",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ελέγχου ταυτότητας και εξουσιοδότησης PKI όπου ο πελάτης λαμβάνει την κατάσταση ανάκλησης ενός πιστοποιητικού SSL/TLS απευθείας από τον ίδιο τον διακομιστή ιστού αντί να ρωτά την Αρχή Πιστοποίησης (CA);",
        "correct": "OCSP Stapling",
        "distractors": ["CRL (Certificate Revocation List)", "DNSSEC", "Certificate Transparency"],
        "explanation": "Το OCSP Stapling (TLS Certificate Status Request) επιτρέπει στον διακομιστή να επισυνάπτει μια πρόσφατη, ψηφιακά υπογεγραμμένη απάντηση OCSP από την CA απευθείας στη χειραψία TLS, βελτιώνοντας την ταχύτητα και το απόρρητο του χρήστη.",
        "funFacts": [
            "Αποτρέπει τη διαρροή του ιστορικού περιήγησης του χρήστη στην Αρχή Πιστοποίησης (CA), καθώς η CA δεν βλέπει πλέον ποιος χρήστης επισκέπτεται ποιον ιστότοπο.",
            "Εξαλείφει επίσης την καθυστέρηση ενός επιπλέον DNS lookup και HTTP αιτήματος προς τον διακομιστή OCSP κατά τη φόρτωση της σελίδας."
        ],
        "source": "https://en.wikipedia.org/wiki/OCSP_stapling",
        "tags": ["technology", "security", "tls", "pki", "networking"]
    },
    {
        "id": "tech_hard_174",
        "text": "Ποιο κλασικό θεώρημα της αρχιτεκτονικής GPU αναφέρει ότι όταν νήματα μέσα στο ίδιο Warp (ομάδα 32 νημάτων) ακολουθούν διαφορετικά μονοπάτια διακλάδωσης (if-else), οι διαφορετικές διαδρομές εκτελούνται σειριακά απενεργοποιώντας τα υπόλοιπα νήματα;",
        "correct": "Απόκλιση Νημάτων (Warp Divergence)",
        "distractors": ["Race Condition", "Bank Conflict", "Pipeline Stall"],
        "explanation": "Στο υπολογιστικό μοντέλο SIMT (Single Instruction, Multiple Threads) των GPUs, όλα τα 32 νήματα ενός warp πρέπει να εκτελούν την ίδια εντολή στον ίδιο κύκλο. Αν διαφωνήσουν, ο επεξεργαστής εκτελεί διαδοχικά και τα δύο κλαδιά με μάσκες απενεργοποίησης (predication), μειώνοντας την απόδοση.",
        "funFacts": [
            "Αποτελεί τον νούμερο ένα παράγοντα απώλειας απόδοσης σε υπολογιστικούς πυρήνες CUDA και OpenCL.",
            "Οι αρχιτεκτονικές NVIDIA Volta και νεότερες εισήγαγαν το Independent Thread Scheduling, επιτρέποντας στα νήματα να διατηρούν ανεξάρτητο Program Counter αλλά το κόστος της απόκλισης παραμένει."
        ],
        "source": "https://en.wikipedia.org/wiki/Single_instruction,_multiple_threads",
        "tags": ["technology", "gpu", "cuda", "hardware", "parallel_computing"]
    },
    {
        "id": "tech_hard_175",
        "text": "Ποιο είδος κρυπτογράφησης, που επιλύθηκε πλήρως για πρώτη φορά από τον Craig Gentry το 2009 χρησιμοποιώντας άλγεβρα ιδεωδών πλεγμάτων, επιτρέπει την εκτέλεση αυθαίρετων μαθηματικών υπολογισμών απευθείας πάνω σε κρυπτογραφημένα δεδομένα χωρίς να αποκρυπτογραφηθούν ποτέ;",
        "correct": "Πλήρως Ομόμορφη Κρυπτογράφηση (Fully Homomorphic Encryption - FHE)",
        "distractors": ["Κρυπτογράφηση Δημόσιου Κλειδιού", "Απόδειξη Μηδενικής Γνώσης", "Κρυπτογραφία Κατωφλίου"],
        "explanation": "Η FHE επιτρέπει σε έναν μη έμπιστο πάροχο cloud να επεξεργαστεί δεδομένα [υπολογίζοντας f(Enc(m)) = Enc(f(m))] επιστρέφοντας το αποτέλεσμα στον χρήστη, ο οποίος είναι ο μόνος που κατέχει το κλειδί αποκρυπτογράφησης.",
        "funFacts": [
            "Ο Craig Gentry ανέπτυξε την πρώτη πρακτική κατασκευή FHE στη διδακτορική του διατριβή στο Στάνφορντ το 2009, λύνοντας ένα ανοιχτό πρόβλημα 30 ετών.",
            "Αν και είναι υπολογιστικά εξαιρετικά απαιτητική (συχνά 1.000 έως 100.000 φορές πιο αργή από τους απλούς υπολογισμούς), χρησιμοποιείται ήδη σε ασφαλείς ιατρικές αναλύσεις και μηχανική μάθηση."
        ],
        "source": "https://en.wikipedia.org/wiki/Homomorphic_encryption",
        "tags": ["technology", "cryptography", "fhe", "security", "homomorphic_encryption"]
    },
    {
        "id": "tech_hard_176",
        "text": "Ποιο είναι το όνομα του επιπέδου απομόνωσης συναλλαγών SQL (Transaction Isolation Level) όπου μια συναλλαγή διαβάζει τα δεδομένα όπως υπήρχαν σε ένα σταθερό σημείο του χρόνου (συνήθως κατά την έναρξη της συναλλαγής), χρησιμοποιώντας MVCC;",
        "correct": "Απομόνωση Στιγμιότυπου (Snapshot Isolation)",
        "distractors": ["Read Uncommitted", "Read Committed", "Serializable"],
        "explanation": "Στο Snapshot Isolation οι αναγνώσεις δεν μπλοκάρουν ποτέ τις εγγραφές και οι εγγραφές δεν μπλοκάρουν τις αναγνώσεις. Ωστόσο, μπορεί να εμφανιστεί η ανωμαλία της 'κλίσης εγγραφής' (Write Skew), η οποία αποτρέπεται μόνο σε πλήρη σειριοποιησιμότητα (Serializable).",
        "funFacts": [
            "Επινοήθηκε το 1995 από τους Berenson, Bernstein, Gray, Melton, O'Neil και O'Neil στην ιστορική κριτική του προτύπου ANSI SQL-92.",
            "Αποτελεί την πραγματική βάση της λειτουργίας 'Repeatable Read' στην PostgreSQL και στη MySQL InnoDB."
        ],
        "source": "https://en.wikipedia.org/wiki/Snapshot_isolation",
        "tags": ["technology", "databases", "sql", "transactions", "mvcc"]
    },
    {
        "id": "tech_hard_177",
        "text": "Ποιος αλγόριθμος εύρεσης ισχυρά συνεκτικών συνιστωσών (Strongly Connected Components - SCC) σε έναν κατευθυνόμενο γράφο, που σχεδιάστηκε από τον Robert Tarjan το 1972, επιτυγχάνει γραμμικό χρόνο O(V + E) χρησιμοποιώντας ένα μόνο πέρασμα κατά βάθος αναζήτησης (DFS);",
        "correct": "Αλγόριθμος του Tarjan",
        "distractors": ["Αλγόριθμος Kosaraju-Sharir", "Αλγόριθμος Bellman-Ford", "Αλγόριθμος Floyd-Warshall"],
        "explanation": "Ο αλγόριθμος του Tarjan χρησιμοποιεί μια στοίβα κόμβων και παρακολουθεί δύο δείκτες ανά κόμβο: τον αριθμό ανακάλυψης (index) και τη χαμηλότερη προσβάσιμη τιμή δείκτη (lowlink).",
        "funFacts": [
            "Ο Robert Tarjan τιμήθηκε με το βραβείο Turing Award το 1986 μαζί με τον John Hopcroft για τη θεμελιώδη συνεισφορά τους στον σχεδιασμό και ανάλυση αλγορίθμων και δομών δεδομένων.",
            "Σε αντίθεση με τον αλγόριθμο Kosaraju, ο οποίος απαιτεί δύο ξεχωριστά περάσματα DFS και αναστροφή του γραφήματος, ο Tarjan ολοκληρώνει τον εντοπισμό σε ένα μόνο πέρασμα."
        ],
        "source": "https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm",
        "tags": ["technology", "algorithms", "graph_theory", "tarjan", "dfs"]
    },
    {
        "id": "tech_hard_178",
        "text": "Ποια είναι η τεχνική βελτιστοποίησης δυναμικής μεταγλώττισης (JIT compilation) που επιτρέπει στον διερμηνέα να αντικαταστήσει μια ενεργή συνάρτηση με βελτιστοποιημένο κώδικα μηχανής ενώ αυτή εκτελείται ήδη μέσα σε έναν επαναληπτικό βρόχο;",
        "correct": "Αντικατάσταση επί της Στοίβας (On-Stack Replacement - OSR)",
        "distractors": ["Inlining", "Escape Analysis", "Loop Unrolling"],
        "explanation": "Το OSR μεταφέρει την κατάσταση των τοπικών μεταβλητών και της στοίβας από το περιβάλλον του διερμηνέα κατευθείαν στο πλαίσιο στοίβας (stack frame) του μεταγλωττισμένου κώδικα μηχανής χωρίς να περιμένει να ολοκληρωθεί η συνάρτηση.",
        "funFacts": [
            "Είναι κρίσιμο για μακροχρόνιους βρόχους (long-running loops) σε γλώσσες όπως η Java (HotSpot JVM) και η JavaScript (V8 engine).",
            "Η αντίστροφη διαδικασία (Deoptimization) χρησιμοποιείται όταν οι αισιόδοξες παραδοχές του μεταγλωττιστή καταρρίπτονται, επιστρέφοντας με ασφάλεια πίσω στον διερμηνέα."
        ],
        "source": "https://en.wikipedia.org/wiki/On-stack_replacement",
        "tags": ["technology", "compilers", "jit", "jvm", "performance"]
    },
    {
        "id": "tech_hard_179",
        "text": "Ποιος αλγόριθμος ταχείας μετατροπής σημάτων από το πεδίο του χρόνου στο πεδίο της συχνότητας, που ανακαλύφθηκε ξανά από τους James Cooley και John Tukey το 1965, μείωσε την πολυπλοκότητα του Διακριτού Μετασχηματισμού Fourier από O(N²) σε O(N log N);",
        "correct": "Αλγόριθμος Cooley-Tukey (FFT)",
        "distractors": ["Αλγόριθμος Rader", "Αλγόριθμος Bluestein", "Αλγόριθμος Karatsuba"],
        "explanation": "Ο αλγόριθμος Cooley-Tukey FFT χρησιμοποιεί διαίρει και βασίλευε διαχωρίζοντας αναδρομικά τον μετασχηματισμό σε άρτιους και περιττούς δείκτες, επιτρέποντας την επεξεργασία ψηφιακού σήματος σε πραγματικό χρόνο.",
        "funFacts": [
            "Ο διάσημος μαθηματικός Καρλ Φρίντριχ Γκάους είχε επινοήσει την ίδια ακριβώς μέθοδο ήδη από το 1805 για τον υπολογισμό τροχιών αστεροειδών, αλλά δεν την είχε δημοσιεύσει ποτέ επίσημα.",
            "Θεωρείται ένας από τους 10 σημαντικότερους αλγορίθμους του 20ού αιώνα, καθώς χρησιμοποιείται σε Wi-Fi, 5G, συμπίεση MP3/JPEG και ιατρικές απεικονίσεις MRI."
        ],
        "source": "https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm",
        "tags": ["technology", "algorithms", "dsp", "fft", "math"]
    },
    {
        "id": "tech_hard_180",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ελέγχου ροής στο TCP (Nagle's algorithm) που συνδυάζει μικρά εξερχόμενα μηνύματα και καθυστερεί την αποστολή τους μέχρι να ληφθεί επιβεβαίωση (ACK) για το προηγούμενο πακέτο, προκαλώντας συχνά ανεπιθύμητη καθυστέρηση εάν συνδυαστεί με το Delayed ACK;",
        "correct": "Αλγόριθμος του Nagle",
        "distractors": ["Αλγόριθμος του Jacobson", "Αλγόριθμος του Karn", "Sliding Window"],
        "explanation": "Ο αλγόριθμος του Nagle (John Nagle, 1984) σχεδιάστηκε για να αποτρέψει το πρόβλημα των μικροσκοπικών πακέτων (tinygrams) στο διαδίκτυο. Σε εφαρμογές πραγματικού χρόνου (παιχνίδια, financial trading) απενεργοποιείται ρητά με την επιλογή socket TCP_NODELAY.",
        "funFacts": [
            "Η προβληματική αλληλεπίδραση ανάμεσα στον αλγόριθμο του Nagle και το Delayed ACK του TCP μπορεί να εισαγάγει μια τεχνητή καθυστέρηση ακριβώς 200 έως 500 χιλιοστών του δευτερολέπτου σε κάθε αίτημα.",
            "Ο ίδιος ο John Nagle δήλωσε αργότερα ότι η συνύπαρξη των δύο αυτών μηχανισμών ήταν ένα από τα μεγαλύτερα σχεδιαστικά ατυχήματα στην ιστορία των δικτύων."
        ],
        "source": "https://en.wikipedia.org/wiki/Nagle%27s_algorithm",
        "tags": ["technology", "networking", "tcp", "nagle", "protocols"]
    },
    {
        "id": "tech_hard_181",
        "text": "Ποιο είναι το όνομα της ευπάθειας κρυπτογραφικών συναρτήσεων κατακερματισμού βασισμένων στην κατασκευή Merkle-Damgård (όπως MD5, SHA-1 και SHA-256), όπου ένας επιτιθέμενος μπορεί να προσθέσει νέα δεδομένα σε ένα υπογεγραμμένο μήνυμα χωρίς να γνωρίζει το μυστικό κλειδί;",
        "correct": "Επίθεση Επέκτασης Μήκους (Length Extension Attack)",
        "distractors": ["Επίθεση Γενεθλίων (Birthday Attack)", "Επίθεση Σύγκρουσης (Collision Attack)", "Επίθεση Preimage"],
        "explanation": "Στις συναρτήσεις Merkle-Damgård, η τελική έξοδος είναι ακριβώς η εσωτερική κατάσταση της συνάρτησης, επιτρέποντας στον επιτιθέμενο να συνεχίσει τον κατακερματισμό προσθέτοντας νέα μπλοκ. Για τον λόγο αυτό αναπτύχθηκε το HMAC και η κατασκευή σπόγγου του SHA-3.",
        "funFacts": [
            "Αυτή η ευπάθεια κατέστησε εντελώς ανασφαλείς τις απλές κατασκευές ελέγχου ταυτότητας της μορφής H(key || message).",
            "Το πρωτόκολλο HMAC προστατεύει από αυτή την επίθεση εφαρμόζοντας διπλό, εμφωλευμένο κατακερματισμό: H(K' ⊕ opad || H(K' ⊕ ipad || message))."
        ],
        "source": "https://en.wikipedia.org/wiki/Length_extension_attack",
        "tags": ["technology", "cryptography", "security", "hashing", "hmac"]
    },
    {
        "id": "tech_hard_182",
        "text": "Ποια είναι η μονάδα προστασίας μνήμης σε επίπεδο υλικού (Hardware Enclave) στους σύγχρονους επεξεργαστές Intel, η οποία επιτρέπει την εκτέλεση κώδικα σε απομονωμένες περιοχές (Enclaves) κρυπτογραφημένες απευθείας στη RAM, προστατεύοντας τα δεδομένα ακόμη κι αν το ίδιο το λειτουργικό σύστημα παραβιαστεί;",
        "correct": "Intel SGX (Software Guard Extensions)",
        "distractors": ["ARM TrustZone", "AMD SEV", "Apple Secure Enclave"],
        "explanation": "Το Intel SGX κρυπτογραφεί τα δεδομένα της μνήμης Enclave Page Cache (EPC) χρησιμοποιώντας τον μηχανισμό Memory Encryption Engine (MEE), αποτρέποντας φυσικές επιθέσεις snooping στο δίαυλο μνήμης.",
        "funFacts": [
            "Χρησιμοποιείται σε υπολογιστικό νέφος εμπιστευτικότητας (Confidential Computing) για την εκτέλεση ευαίσθητων συναλλαγών και ασφαλών κλειδιών.",
            "Τα τελευταία χρόνια έχει δεχθεί πολλαπλές επιθέσεις πλευρικού καναλιού (όπως Foreshadow και Plundervolt), οδηγώντας την Intel στην απόσυρσή του από τους καταναλωτικούς επεξεργαστές 11ης και 12ης γενιάς."
        ],
        "source": "https://en.wikipedia.org/wiki/Software_Guard_Extensions",
        "tags": ["technology", "hardware", "security", "intel", "sgx"]
    },
    {
        "id": "tech_hard_183",
        "text": "Ποιος αλγόριθμος πολλαπλασιασμού πινάκων, που ανακαλύφθηκε από τον Volker Strassen το 1969, κατέρριψε για πρώτη φορά το ιστορικό όριο πολυπλοκότητας O(n³), πετυχαίνοντας χρόνο O(n^2.807);",
        "correct": "Αλγόριθμος του Strassen",
        "distractors": ["Αλγόριθμος Coppersmith-Winograd", "Αλγόριθμος Karatsuba", "Αλγόριθμος Toom-Cook"],
        "explanation": "Ο Strassen έδειξε ότι δύο πίνακες 2x2 μπορούν να πολλαπλασιαστούν με μόλις 7 βαθμωτούς πολλαπλασιασμούς αντί για τους παραδοσιακούς 8, μειώνοντας δραστικά την ασυμπτωτική πολυπλοκότητα.",
        "funFacts": [
            "Μέχρι το 1969, η παγκόσμια μαθηματική κοινότητα πίστευε ευρέως ότι το O(n³) ήταν το απόλυτο κατώτατο όριο για τον πολλαπλασιασμό πινάκων.",
            "Το 2022, η DeepMind χρησιμοποίησε το νευρωνικό δίκτυο AlphaTensor για να ανακαλύψει αυτόνομα νέους αλγορίθμους πολλαπλασιασμού πινάκων ταχύτερους από τον αλγόριθμο του Strassen για συγκεκριμένα μεγέθη."
        ],
        "source": "https://en.wikipedia.org/wiki/Strassen_algorithm",
        "tags": ["technology", "algorithms", "linear_algebra", "strassen", "math"]
    },
    {
        "id": "tech_hard_184",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δρομολόγησης εσωτερικής πύλης (IGP) που χρησιμοποιεί τον αλγόριθμο Dijkstra (SPF) για τον υπολογισμό της συντομότερης διαδρομής, διατηρώντας μια πλήρη βάση δεδομένων της τοπολογίας του δικτύου (LSDB);",
        "correct": "OSPF (Open Shortest Path First)",
        "distractors": ["BGP", "RIP", "EIGRP"],
        "explanation": "Το OSPF είναι πρωτόκολλο κατάστασης συνδέσμου (link-state routing protocol) ανοιχτού προτύπου, που χωρίζει τα δίκτυα σε ιεραρχικές περιοχές (Areas) με κορμό την Area 0 (Backbone).",
        "funFacts": [
            "Σε αντίθεση με το παλιότερο RIP που βασίζεται μόνο σε αριθμό αλμάτων (hop count, max 15), το OSPF υπολογίζει το κόστος διαδρομής βάσει του πραγματικού εύρους ζώνης (bandwidth) των συνδέσεων.",
            "Συγκλίνει εξαιρετικά γρήγορα στέλνοντας ενημερώσεις Link-State Advertisements (LSAs) μόνο όταν αλλάζει η κατάσταση μιας γραμμής."
        ],
        "source": "https://en.wikipedia.org/wiki/Open_Shortest_Path_First",
        "tags": ["technology", "networking", "ospf", "routing", "protocols"]
    },
    {
        "id": "tech_hard_185",
        "text": "Ποια είναι η τεχνική προστασίας μνήμης σε επίπεδο μεταγλωττιστή που τοποθετεί μια τυχαία τιμή ελέγχου (canary) στη στοίβα ακριβώς πριν από τη διεύθυνση επιστροφής για να ανιχνεύσει υπερχειλίσεις προσωρινής μνήμης (buffer overflows);",
        "correct": "Stack Canaries (StackGuard)",
        "distractors": ["ASLR", "Shadow Stack", "SafeSEH"],
        "explanation": "Εάν ένας επιτιθέμενος υπερχειλίσει έναν πίνακα στη στοίβα για να αλλάξει τη διεύθυνση επιστροφής, αναγκαστικά θα αλλοιώσει και την τιμή του canary. Η συνάρτηση ελέγχει την τιμή πριν επιστρέψει και αν έχει αλλάξει τερματίζει άμεσα το πρόγραμμα (__stack_chk_fail).",
        "funFacts": [
            "Ονομάστηκε έτσι κατά αναλογία με τα καναρίνια που χρησιμοποιούσαν οι ανθρακωρύχοι στα ορυχεία για να ανιχνεύουν έγκαιρα δηλητηριώδη αέρια.",
            "Ενεργοποιείται αυτόματα στους σύγχρονους μεταγλωττιστές GCC και Clang με τη σημαία -fstack-protector."
        ],
        "source": "https://en.wikipedia.org/wiki/Buffer_overflow_protection#Stack_canaries",
        "tags": ["technology", "security", "compilers", "stack_canary", "buffer_overflow"]
    },
    {
        "id": "tech_hard_186",
        "text": "Ποιο είναι το όνομα του αλγορίθμου συμπίεσης δεδομένων χωρίς απώλειες που αναπτύχθηκε από τον Yann Collet στη Meta το 2015, συνδυάζοντας την κωδικοποίηση Finite State Entropy (FSE) με εξαιρετικά γρήγορους ρυθμούς αποσυμπίεσης;",
        "correct": "Zstandard (zstd)",
        "distractors": ["Brotli", "Snappy", "LZ4"],
        "explanation": "Το Zstandard προσφέρει λόγο συμπίεσης εφάμιλλο του zlib/DEFLATE αλλά με ταχύτητες συμπίεσης και αποσυμπίεσης που φτάνουν πολλαπλάσια GB/sec ανά πυρήνα CPU.",
        "funFacts": [
            "Ο Yann Collet ήταν επίσης ο δημιουργός του υπερταχέος αλγορίθμου συμπίεσης LZ4.",
            "Υιοθετήθηκε ευρέως ως η προεπιλογή στον πυρήνα του Linux, σε διανομές όπως το Fedora και το Arch Linux (για πακέτα), καθώς και σε βάσεις δεδομένων όπως η RocksDB."
        ],
        "source": "https://en.wikipedia.org/wiki/Zstandard",
        "tags": ["technology", "compression", "algorithms", "zstd", "meta"]
    },
    {
        "id": "tech_hard_187",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου χρονισμού ακριβείας μέσω δικτύου (PTP - IEEE 1588) που επιτυγχάνει συγχρονισμό ρολογιών με ακρίβεια κάτω του ενός μικροδευτερολέπτου (sub-microsecond) χρησιμοποιώντας υλικό χρονοσήμανσης (hardware timestamping);",
        "correct": "PTP (Precision Time Protocol)",
        "distractors": ["NTP (Network Time Protocol)", "SNTP", "TrueTime"],
        "explanation": "Σε αντίθεση με το παραδοσιακό NTP που επιτυγχάνει ακρίβεια χιλιοστών του δευτερολέπτου μέσω λογισμικού, το PTP χρησιμοποιεί κάρτες δικτύου που σημαδεύουν τα πακέτα ακριβώς τη στιγμή που διέρχονται από το φυσικό στρώμα PHY.",
        "funFacts": [
            "Είναι ζωτικής σημασίας για τα δίκτυα υψηλής συχνότητας συναλλαγών στο χρηματιστήριο (HFT), τα δίκτυα κινητής τηλεφωνίας 5G και τον συγχρονισμό του ηλεκτρικού δικτύου.",
            "Μια παραλλαγή του, το 'White Rabbit PTP' που αναπτύχθηκε στο CERN, επιτυγχάνει συγχρονισμό με ακρίβεια υπο-νανοδευτερολέπτου (sub-nanosecond) σε αποστάσεις άνω των 10 χλμ."
        ],
        "source": "https://en.wikipedia.org/wiki/Precision_Time_Protocol",
        "tags": ["technology", "networking", "time_synchronization", "ptp", "hardware"]
    },
    {
        "id": "tech_hard_188",
        "text": "Ποια διάσημη τεχνική βελτιστοποίησης επεξεργαστών χρησιμοποιεί έναν πίνακα ετικετών (Translation Lookaside Buffer - TLB) για να επιταχύνει τη μετάφραση των εικονικών διευθύνσεων μνήμης σε φυσικές διευθύνσεις;",
        "correct": "TLB (Translation Lookaside Buffer)",
        "distractors": ["L1 Cache", "Branch Target Buffer", "Page Table Entry"],
        "explanation": "Χωρίς το TLB, κάθε προσπέλαση μνήμης σε ένα λειτουργικό σύστημα 64-bit με πίνακες σελίδων 4 ή 5 επιπέδων θα απαιτούσε 4 έως 5 διαδοχικές αναγνώσεις μνήμης μόνο για την εύρεση της φυσικής διεύθυνσης.",
        "funFacts": [
            "Ένα 'TLB Miss' αναγκάζει το υλικό (Page Table Walker) να διασχίσει ολόκληρη τη δομή των πινάκων σελίδων στη RAM, προκαλώντας τεράστια καθυστέρηση.",
            "Για να μειωθούν τα TLB misses σε εφαρμογές με τεράστια μνήμη (όπως βάσεις δεδομένων), χρησιμοποιούνται Huge Pages μεγέθους 2MB ή 1GB αντί των κλασικών 4KB."
        ],
        "source": "https://en.wikipedia.org/wiki/Translation_lookaside_buffer",
        "tags": ["technology", "cpu", "virtual_memory", "hardware", "tlb"]
    },
    {
        "id": "tech_hard_189",
        "text": "Ποια είναι η οικογένεια επεκτάσεων συνόλου εντολών SIMD της Intel που επεξεργάζεται διανύσματα πλάτους 512 bit σε μία μόνο εντολή κύκλου ρολογιού, επιτρέποντας την ταυτόχρονη εκτέλεση 16 πράξεων κινητής υποδιαστολής απλής ακρίβειας;",
        "correct": "AVX-512",
        "distractors": ["AVX2", "SSE4.2", "MMX"],
        "explanation": "Το AVX-512 εισήγαγε 32 νέους διανυσματικούς καταχωρητές των 512 bit (zmm0-zmm31) και προηγμένες εντολές μάσκας (opmask registers k0-k7) για επιτάχυνση επιστημονικών υπολογισμών και μηχανικής μάθησης.",
        "funFacts": [
            "Στους πρώτους επεξεργαστές Intel Skylake-X, η βαριά χρήση εντολών AVX-512 προκαλούσε πτώση της συχνότητας ρολογιού (AVX frequency offset/downclocking) λόγω της τεράστιας κατανάλωσης ρεύματος και θερμότητας.",
            "Η AMD εισήγαγε πλήρη υποστήριξη AVX-512 στην αρχιτεκτονική Zen 4 (Ryzen 7000) χωρίς καμία πτώση συχνότητας ρολογιού."
        ],
        "source": "https://en.wikipedia.org/wiki/AVX-512",
        "tags": ["technology", "cpu", "simd", "avx512", "hardware", "intel"]
    },
    {
        "id": "tech_hard_190",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δρομολόγησης πακέτων σε δίκτυα αποθήκευσης (SAN) που ενσωματώνει εγγενή πλαίσια Fibre Channel απευθείας μέσα σε τυπικά πακέτα Ethernet 10/40/100 Gbps χωρίς απώλειες;",
        "correct": "FCoE (Fibre Channel over Ethernet)",
        "distractors": ["iSCSI", "InfiniBand", "NVMe-oF"],
        "explanation": "Το FCoE ενοποιεί την κίνηση LAN και SAN πάνω από την ίδια φυσική υποδομή καλωδίωσης Ethernet, απαιτώντας επεκτάσεις Ethernet χωρίς απώλειες (Data Center Bridging - DCB και Priority-based Flow Control).",
        "funFacts": [
            "Λειτουργεί στο Επίπεδο 2 του μοντέλου OSI και δεν χρησιμοποιεί IP ή TCP επικεφαλίδες, μειώνοντας το overhead επεξεργασίας.",
            "Αν και υποστηρίχθηκε θερμά από τη Cisco για χρόνια, σήμερα αντικαθίσταται σταδιακά από τα πρωτόκολλα NVMe over Fabrics."
        ],
        "source": "https://en.wikipedia.org/wiki/Fibre_Channel_over_Ethernet",
        "tags": ["technology", "networking", "storage", "san", "fcoe"]
    },
    {
        "id": "tech_hard_191",
        "text": "Ποιος είναι ο αλγόριθμος εύρεσης ελαχίστου κόστους ροής (minimum-cost flow) και μέγιστης ροής σε δίκτυα που επινοήθηκε από τους Jack Edmonds και Richard Karp το 1972, εξειδικεύοντας τον αλγόριθμο Ford-Fulkerson χρησιμοποιώντας BFS σε χρόνο O(V E²);",
        "correct": "Αλγόριθμος Edmonds-Karp",
        "distractors": ["Αλγόριθμος Dinic", "Αλγόριθμος Push-Relabel", "Αλγόριθμος Hopcroft-Karp"],
        "explanation": "Ο αλγόριθμος Edmonds-Karp εγγυάται ότι η μέθοδος Ford-Fulkerson θα τερματίσει σε πολυωνυμικό χρόνο ακόμη κι αν οι χωρητικότητες των ακμών είναι άρρητοι αριθμοί, επιλέγοντας πάντα το συντομότερο μονοπάτι επαύξησης (shortest augmenting path).",
        "funFacts": [
            "Αποτέλεσε ιστορικό ορόσημο στη θεωρία γραφημάτων και επιχειρησιακή έρευνα για τη βελτιστοποίηση δικτύων μεταφορών και τηλεπικοινωνιών.",
            "Ο Richard Karp τιμήθηκε με το βραβείο Turing Award το 1985 για τη μνημειώδη συνεισφορά του στη θεωρία NP-πληρότητας (τα 21 NP-πλήρη προβλήματα του Karp)."
        ],
        "source": "https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm",
        "tags": ["technology", "algorithms", "graph_theory", "max_flow", "edmonds_karp"]
    },
    {
        "id": "tech_hard_192",
        "text": "Ποιο είναι το όνομα του ανοιχτού συστήματος αρχειοθέτησης και επαλήθευσης πιστοποιητικών SSL/TLS (Certificate Transparency - CT) που καθιστά αδύνατη την κρυφή έκδοση πλαστών πιστοποιητικών από παραβιασμένες CAs χρησιμοποιώντας προσαρτήσιμα αρχεία καταγραφής Merkle Tree;",
        "correct": "Certificate Transparency (CT)",
        "distractors": ["DANE (DNS-based Authentication)", "HPKP (HTTP Public Key Pinning)", "CAA Records"],
        "explanation": "Το Certificate Transparency (RFC 6962, σχεδιασμένο από μηχανικούς της Google) απαιτεί από όλες τις CAs να δημοσιεύουν δημόσια κάθε πιστοποιητικό που εκδίδουν σε αδιάβλητα logs, αλλιώς τα προγράμματα περιήγησης (όπως ο Chrome) αρνούνται να το εμπιστευτούν.",
        "funFacts": [
            "Οδήγησε στον εντοπισμό πολλαπλών παραβιάσεων και παράνομων εκδόσεων πιστοποιητικών από μεγάλες CAs, όπως η Symantec, η οποία τελικά υποχρεώθηκε να πουλήσει τη δραστηριότητα CAs της στην DigiCert.",
            "Τα logs είναι δομημένα ως Merkle Trees, επιτρέποντας αποδείξεις συμπερίληψης και συνέπειας σε λογαριθμικό χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Certificate_Transparency",
        "tags": ["technology", "security", "tls", "pki", "certificate_transparency"]
    },
    {
        "id": "tech_hard_193",
        "text": "Ποιο είναι το όνομα της τεχνικής διαχείρισης διεργασιών και μνήμης όπου μια διεργασία παιδί που δημιουργείται με την κλήση συστήματος fork() μοιράζεται τις ίδιες φυσικές σελίδες μνήμης με τη μητρική διεργασία μέχρι οποιαδήποτε από τις δύο να επιχειρήσει τροποποίηση;",
        "correct": "Αντιγραφή κατά την Εγγραφή (Copy-on-Write - COW)",
        "distractors": ["Lazy Loading", "Demand Paging", "Memory Deduplication"],
        "explanation": "Στο Copy-on-Write, οι σελίδες μνήμης επισημαίνονται αρχικά ως μόνο για ανάγνωση (read-only) και για τις δύο διεργασίες. Όταν κάποια προσπαθήσει να γράψει, η CPU προκαλεί εξαίρεση page fault και ο πυρήνας αντιγράφει μόνο τη συγκεκριμένη σελίδα.",
        "funFacts": [
            "Καθιστά την κλήση fork() στο Unix σχεδόν στιγμιαία, ανεξάρτητα από το μέγεθος της μνήμης που χρησιμοποιεί η αρχική διεργασία.",
            "Χρησιμοποιείται επίσης εκτεταμένα από τη βάση δεδομένων Redis για τη δημιουργία στιγμιοτύπων ασφαλείας στον δίσκο (BGSAVE) χωρίς να παγώνει η εκτέλεση εντολών."
        ],
        "source": "https://en.wikipedia.org/wiki/Copy-on-write",
        "tags": ["technology", "operating_systems", "virtual_memory", "linux", "copy_on_write"]
    },
    {
        "id": "tech_hard_194",
        "text": "Ποιος αλγόριθμος παράλληλου προγραμματισμού επιλύει το πρόβλημα του αμοιβαίου αποκλεισμού (Mutual Exclusion) για n διεργασίες αποκλειστικά σε επίπεδο λογισμικού χωρίς καμία ειδική εντολή υλικού, προσομοιώνοντας τη λειτουργία σειράς προτεραιότητας με αριθμούς σε αρτοποιείο;",
        "correct": "Αλγόριθμος Αρτοποιείου του Λάμπορτ (Lamport's Bakery Algorithm)",
        "distractors": ["Αλγόριθμος Dekker", "Αλγόριθμος Peterson", "Αλγόριθμος Szymanski"],
        "explanation": "Ο Leslie Lamport επινόησε τον αλγόριθμο Bakery το 1974, εξασφαλίζοντας δικαιοσύνη πρώτης εισόδου - πρώτης εξυπηρέτησης (FIFO) και πλήρη αποφυγή λιμοκτονίας (starvation-freedom) ακόμη κι αν οι διεργασίες διαβάζουν ασυνεπείς τιμές κατά τη διάρκεια εγγραφών.",
        "funFacts": [
            "Ήταν ο πρώτος αλγόριθμος αμοιβαίου αποκλεισμού που απέδειξε ότι δεν απαιτείται καμία ατομικότητα σε επίπεδο υλικού καταχωρητών (ακόμη και με flaky memory registers).",
            "Ενέπνευσε τη μεταγενέστερη θεωρία του Lamport για τη συνέπεια μνήμης (Sequential Consistency)."
        ],
        "source": "https://en.wikipedia.org/wiki/Lamport%27s_bakery_algorithm",
        "tags": ["technology", "concurrency", "algorithms", "lamport", "mutual_exclusion"]
    },
    {
        "id": "tech_hard_195",
        "text": "Ποιο είναι το όνομα του υποσυστήματος ασφαλείας του πυρήνα του Linux (Secure Computing Mode) που περιορίζει δραστικά τις κλήσεις συστήματος (system calls) που επιτρέπεται να εκτελέσει μια διεργασία, χρησιμοποιώντας φίλτρα BPF;",
        "correct": "Seccomp (Seccomp-BPF)",
        "distractors": ["AppArmor", "SELinux", "Capabilities"],
        "explanation": "Το Seccomp-BPF επιτρέπει σε προγράμματα (όπως το Google Chrome Sandbox και τα κοντέινερ Docker) να απομονώνονται ορίζοντας μια αυστηρή λευκή λίστα επιτρεπόμενων κλήσεων συστήματος, αποτρέποντας εκμεταλλεύσεις ευπαθειών του πυρήνα.",
        "funFacts": [
            "Στην αρχική του λειτουργία (Seccomp mode 1), μια διεργασία μπορούσε να εκτελέσει μόνο 4 κλήσεις συστήματος: read(), write(), _exit() και sigreturn()!",
            "Με την προσθήκη φίλτρων BPF το 2012, έγινε ένα από τα πιο ισχυρά και ευέλικτα εργαλεία sandboxing στο οικοσύστημα του Linux."
        ],
        "source": "https://en.wikipedia.org/wiki/Seccomp",
        "tags": ["technology", "linux", "security", "seccomp", "sandboxing"]
    },
    {
        "id": "tech_hard_196",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δρομολόγησης BGP όπου ένας κεντρικός δρομολογητής (Route Reflector) αναδιανέμει τις διαδρομές iBGP σε άλλους εσωτερικούς δρομολογητές, καταργώντας την ανάγκη για ένα πλήρες πλέγμα συνδέσεων (Full Mesh iBGP);",
        "correct": "BGP Route Reflector (RR)",
        "distractors": ["BGP Confederation", "BGP Anycast", "BGP EVPN"],
        "explanation": "Χωρίς Route Reflectors, ένα δίκτυο με N δρομολογητές iBGP απαιτεί N*(N-1)/2 συνδέσεις peering, κάτι που καθιστά τη διαχείριση αδύνατη σε μεγάλα δίκτυα παρόχων. Ο Route Reflector μειώνει την πολυπλοκότητα σε O(N).",
        "funFacts": [
            "Εισήχθη επίσημα στο πρότυπο RFC 1966 (και RFC 4456) για την κλιμάκωση των δικτύων παρόχων Tier-1 και Tier-2.",
            "Για την αποτροπή βρόχων δρομολόγησης (routing loops), εισάγει δύο νέα προαιρετικά μη μεταβατικά χαρακτηριστικά: το ORIGINATOR_ID και το CLUSTER_LIST."
        ],
        "source": "https://en.wikipedia.org/wiki/BGP_route_reflector",
        "tags": ["technology", "networking", "bgp", "routing", "internet"]
    },
    {
        "id": "tech_hard_197",
        "text": "Ποιο είναι το όνομα της επίθεσης δικτύου όπου ένας κακόβουλος κόμβος σε ένα τοπικό δίκτυο Ethernet στέλνει πλαστά μηνύματα ARP απάντησης (Gratuitous ARP), συσχετίζοντας τη δική του MAC διεύθυνση με την IP διεύθυνση της προεπιλεγμένης πύλης (Default Gateway);",
        "correct": "ARP Spoofing (ARP Poisoning)",
        "distractors": ["DNS Spoofing", "IP Spoofing", "DHCP Starvation"],
        "explanation": "Το ARP Spoofing επιτρέπει στον εισβολέα να εκτελέσει επίθεση ενδιάμεσου (Man-in-the-Middle - MitM) υποκλέπτοντας, τροποποιώντας ή διακόπτοντας όλη την κίνηση των χρηστών του τοπικού δικτύου προς το διαδίκτυο.",
        "funFacts": [
            "Οφείλεται στο γεγονός ότι το πρωτόκολλο ARP (1982) δεν διαθέτει κανέναν εγγενή μηχανισμό πιστοποίησης ταυτότητας και αποδέχεται απαντήσεις ακόμη κι αν δεν τις έχει ζητήσει ποτέ.",
            "Στα σύγχρονα εταιρικά δίκτυα αντιμετωπίζεται με τη λειτουργία Dynamic ARP Inspection (DAI) στα managed switches, σε συνδυασμό με DHCP Snooping."
        ],
        "source": "https://en.wikipedia.org/wiki/ARP_spoofing",
        "tags": ["technology", "networking", "security", "arp_spoofing", "ethernet"]
    },
    {
        "id": "tech_hard_198",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου εξουσιοδότησης (OAuth 2.0 extension) που εισήγαγε το 'Proof Key for Code Exchange' (PKCE) για την προστασία της ροής κωδικού εξουσιοδότησης σε δημόσιους πελάτες όπως εφαρμογές για κινητά και Single Page Apps;",
        "correct": "OAuth 2.0 PKCE (Proof Key for Code Exchange)",
        "distractors": ["OpenID Connect", "OAuth 1.0a", "SAML 2.0"],
        "explanation": "Το PKCE (RFC 7636) αποτρέπει την υποκλοπή του κωδικού εξουσιοδότησης (authorization code interception attack) δημιουργώντας ένα δυναμικό μυστικό κλειδί (code verifier) και το κρυπτογραφικό του hash (code challenge) κατά την εκκίνηση της σύνδεσης.",
        "funFacts": [
            "Αρχικά σχεδιάστηκε για native εφαρμογές smartphones, αλλά σήμερα θεωρείται υποχρεωτική βέλτιστη πρακτική για όλους τους τύπους πελατών OAuth, συμπεριλαμβανομένων των web apps.",
            "Κατήργησε ουσιαστικά την ανάγκη για την παρωχημένη και ανασφαλή ροή Implicit Flow."
        ],
        "source": "https://en.wikipedia.org/wiki/Proof_Key_for_Code_Exchange",
        "tags": ["technology", "security", "oauth", "pkce", "authentication"]
    },
    {
        "id": "tech_hard_199",
        "text": "Ποιο είναι το όνομα του αλγορίθμου δυναμικού προγραμματισμού που υπολογίζει την ελάχιστη απόσταση επεξεργασίας (Levenshtein distance) μεταξύ δύο συμβολοσειρών σε χρόνο O(m*n), κατασκευάζοντας έναν δισδιάστατο πίνακα πράξεων εισαγωγής, διαγραφής και αντικατάστασης;",
        "correct": "Αλγόριθμος Wagner-Fischer",
        "distractors": ["Αλγόριθμος Needleman-Wunsch", "Αλγόριθμος Smith-Waterman", "Αλγόριθμος Hirschberg"],
        "explanation": "Ο αλγόριθμος Wagner-Fischer (1974) επιλύει αποδοτικά τον υπολογισμό του κόστους μετατροπής μιας λέξης σε μια άλλη και αποτελεί τη βάση των διορθωτών ορθογραφίας και των εργαλείων fuzzy search.",
        "funFacts": [
            "Μπορεί να βελτιστοποιηθεί ως προς τον χώρο μνήμης σε μόλις O(min(m, n)) διατηρώντας μόνο τις δύο τελευταίες γραμμές του πίνακα.",
            "Χρησιμοποιείται εκτεταμένα στη βιοπληροφορική για τη στοίχιση αλληλουχιών DNA και πρωτεϊνών."
        ],
        "source": "https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm",
        "tags": ["technology", "algorithms", "dynamic_programming", "levenshtein", "strings"]
    },
    {
        "id": "tech_hard_200",
        "text": "Ποιο είναι το όνομα της τεχνικής ασφάλειας του πυρήνα του Linux (Kernel Address Space Layout Randomization - KASLR) που τυχαιοποιεί τη θέση των κρίσιμων δομών του πυρήνα στη μνήμη κατά την εκκίνηση για την αποτροπή επιθέσεων εκμετάλλευσης;",
        "correct": "KASLR",
        "distractors": ["ASLR", "KPTI", "SMEP"],
        "explanation": "Το KASLR επεκτείνει το παραδοσιακό ASLR των εφαρμογών χρήστη και στον ίδιο τον πυρήνα του λειτουργικού συστήματος, καθιστώντας αδύνατη την πρόβλεψη διευθύνσεων μνήμης για επιθέσεις Return-to-libc ή ROP χωρίς προηγούμενη διαρροή μνήμης (information leak).",
        "funFacts": [
            "Ενσωματώθηκε επίσημα στον πυρήνα του Linux στην έκδοση 3.14 το 2014.",
            "Συνδυάζεται στενά με τεχνολογίες υλικού της CPU όπως το SMEP (Supervisor Mode Execution Prevention) και SMAP (Supervisor Mode Access Prevention)."
        ],
        "source": "https://en.wikipedia.org/wiki/Address_space_layout_randomization#Kernel_ASLR",
        "tags": ["technology", "linux", "security", "kaslr", "operating_systems"]
    },
    {
        "id": "tech_hard_201",
        "text": "Ποιο είναι το όνομα της ευπάθειας hardware σε παράλληλες συστοιχίες δίσκων RAID 5, όπου μια διακοπή ρεύματος κατά τη διάρκεια εγγραφής αφήνει τα δεδομένα και τα parity blocks ασύμβατα μεταξύ τους χωρίς ένδειξη σφάλματος;",
        "correct": "Η Τρύπα Εγγραφής RAID (RAID 5 Write Hole)",
        "distractors": ["Bit Rot", "Split Brain", "Rebuild Stall"],
        "explanation": "Επειδή η εγγραφή του μπλοκ δεδομένων και του μπλοκ ισοτιμίας (parity) δεν γίνεται ατομικά, αν υπάρξει κατάρρευση ανάμεσα στις δύο εγγραφές, η ισοτιμία καθίσταται άκυρη, καταστρέφοντας δεδομένα κατά την επόμενη ανακατασκευή δίσκου.",
        "funFacts": [
            "Αντιμετωπίζεται με μνήμη cache που υποστηρίζεται από μπαταρία (BBU) στους RAID controllers ή με σύγχρονα συστήματα Copy-on-Write όπως το ZFS (RAID-Z).",
            "Το ZFS σχεδιάστηκε από την αρχή με στόχο να εξαλείψει οριστικά το πρόβλημα του write hole χωρίς να απαιτείται ειδικό υλικό."
        ],
        "source": "https://en.wikipedia.org/wiki/RAID#RAID_write_hole",
        "tags": ["technology", "storage", "raid", "hardware", "data_integrity"]
    },
    {
        "id": "tech_hard_202",
        "text": "Ποιο είναι το όνομα της κρυπτογραφικής τεχνικής ψηφιακής υπογραφής που επινοήθηκε από τον David Chaum το 1983, όπου το περιεχόμενο ενός μηνύματος συγκαλύπτεται (τυφλώνεται) πριν υπογραφεί, αποτελώντας τη βάση του πρώτου ανώνυμου ψηφιακού χρήματος (DigiCash);",
        "correct": "Τυφλές Υπογραφές (Blind Signatures)",
        "distractors": ["Δακτυλιοειδείς Υπογραφές (Ring Signatures)", "Πολυ-υπογραφές (Multisig)", "Threshold Signatures"],
        "explanation": "Στις τυφλές υπογραφές, η υπογράφουσα αρχή (π.χ. τράπεζα) επικυρώνει ένα ψηφιακό νόμισμα χωρίς να γνωρίζει τη σειρά ή τα στοιχεία του, εξασφαλίζοντας μαθηματικά ότι το νόμισμα δεν μπορεί να συνδεθεί με τον κάτοχό του.",
        "funFacts": [
            "Ο David Chaum θεωρείται ο 'νονός των Cypherpunks' και ο πνευματικός πατέρας των κρυπτονομισμάτων.",
            "Χρησιμοποιούνται επίσης σε ηλεκτρονικά συστήματα ψηφοφορίας για να διασφαλιστεί ότι η ψήφος είναι έγκυρη χωρίς να αποκαλύπτεται ποιος ψήφισε τι."
        ],
        "source": "https://en.wikipedia.org/wiki/Blind_signature",
        "tags": ["technology", "cryptography", "blind_signatures", "privacy", "david_chaum"]
    },
    {
        "id": "tech_hard_203",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δικτύου που επιτρέπει σε πολλαπλούς φυσικούς διακομιστές σε διαφορετικές τοποθεσίες του πλανήτη να μοιράζονται την ίδια ακριβώς διεύθυνση IP, με τους δρομολογητές BGP να κατευθύνουν αυτόματα τον πελάτη στον πλησιέστερο κόμβο;",
        "correct": "Anycast (BGP Anycast)",
        "distractors": ["Multicast", "Unicast", "Broadcast"],
        "explanation": "Το Anycast ανακοινώνει το ίδιο πρόθεμα IP από πολλαπλά σημεία παρουσίας (PoPs), επιτρέποντας στο BGP να επιλέγει τη βέλτιστη διαδρομή και παρέχοντας φυσική εξισορρόπηση φορτίου και ανοχή σε επιθέσεις DDoS.",
        "funFacts": [
            "Αποτελεί την τεχνολογία στην οποία βασίζονται και οι 13 ριζικοί διακομιστές DNS (Root DNS Servers) παγκοσμίως, οι οποίοι στην πραγματικότητα λειτουργούν σε εκατοντάδες φυσικές τοποθεσίες.",
            "Χρησιμοποιείται ευρέως από μεγάλα δίκτυα διανομής περιεχομένου (όπως Cloudflare και Fastly) και δημόσια DNS (1.1.1.1, 8.8.8.8)."
        ],
        "source": "https://en.wikipedia.org/wiki/Anycast",
        "tags": ["technology", "networking", "anycast", "bgp", "dns"]
    },
    {
        "id": "tech_hard_204",
        "text": "Ποιο είναι το όνομα της ιδιότητας μη-αποκλεισμού (non-blocking) στον πολυνηματικό προγραμματισμό που εγγυάται ότι τουλάχιστον ένα νήμα του συστήματος θα σημειώνει πάντα πρόοδο σε πεπερασμένο αριθμό βημάτων, αποτρέποντας το καθολικό πάγωμα (deadlock/livelock);",
        "correct": "Χωρίς Κλειδώματα (Lock-free)",
        "distractors": ["Χωρίς Αναμονή (Wait-free)", "Χωρίς Εμπόδια (Obstruction-free)", "Deadlock-free"],
        "explanation": "Σε ένα σύστημα lock-free, μεμονωμένα νήματα μπορεί να υποφέρουν προσωρινά από λιμοκτονία (starvation), αλλά το σύνολο του συστήματος προχωρά πάντα. Η αυστηρότερη βαθμίδα 'Wait-free' εγγυάται ότι κάθε μεμονωμένο νήμα θα σημειώνει πρόοδο σε πεπερασμένο χρόνο.",
        "funFacts": [
            "Ο Maurice Herlihy απέδειξε το 1991 τη 'συναίνεση ιεραρχίας' (Consensus Hierarchy), δείχνοντας ποιες ατομικές εντολές υλικού (όπως CAS) είναι ικανές να υλοποιήσουν wait-free δομές για άπειρα νήματα.",
            "Υλοποιούνται συνήθως με εντολές Compare-And-Swap (CAS) ή Load-Linked/Store-Conditional (LL/SC)."
        ],
        "source": "https://en.wikipedia.org/wiki/Non-blocking_algorithm",
        "tags": ["technology", "concurrency", "lock_free", "multithreading", "algorithms"]
    },
    {
        "id": "tech_hard_205",
        "text": "Ποιος αλγόριθμος εύρεσης όλων των συντομότερων διαδρομών μεταξύ όλων των ζευγών κόμβων (All-Pairs Shortest Path) σε έναν κατευθυνόμενο γράφο με θετικά ή αρνητικά βάρη (χωρίς αρνητικούς κύκλους) λειτουργεί σε χρόνο O(V³) μέσω δυναμικού προγραμματισμού;",
        "correct": "Αλγόριθμος Floyd-Warshall",
        "distractors": ["Αλγόριθμος Dijkstra", "Αλγόριθμος Bellman-Ford", "Αλγόριθμος Johnson"],
        "explanation": "Ο αλγόριθμος Floyd-Warshall (1962) βασίζεται σε μια απλή τριπλή εμφωλευμένη επανάληψη συγκρίνοντας σταδιακά αν η διαδρομή μέσω ενός ενδιάμεσου κόμβου k είναι συντομότερη από την τρέχουσα διαδρομή ανάμεσα στους κόμβους i και j.",
        "funFacts": [
            "Μπορεί επίσης να χρησιμοποιηθεί για τον υπολογισμό της μεταβατικής κλειστότητας (transitive closure) ενός γραφήματος (αλγόριθμος Warshall).",
            "Εάν μετά την ολοκλήρωση του αλγορίθμου η απόσταση ενός κόμβου προς τον εαυτό του γίνει αρνητική [d(i, i) < 0], τότε το γράφημα περιέχει αρνητικό κύκλο."
        ],
        "source": "https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm",
        "tags": ["technology", "algorithms", "graph_theory", "dynamic_programming", "floyd_warshall"]
    },
    {
        "id": "tech_hard_206",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ελέγχου πρόσβασης στο μέσο (MAC) που χρησιμοποιείται στα ενσύρματα δίκτυα Ethernet (IEEE 802.3), όπου οι κόμβοι ακούν το κανάλι πριν μεταδώσουν και ανιχνεύουν συγκρούσεις κατά τη μετάδοση;",
        "correct": "CSMA/CD (Carrier Sense Multiple Access with Collision Detection)",
        "distractors": ["CSMA/CA", "Token Ring", "ALOHA"],
        "explanation": "Στο CSMA/CD, όταν ανιχνευθεί σύγκρουση δύο σημάτων στο καλώδιο, οι κόμβοι στέλνουν ένα σήμα εμπλοκής (jam signal) και περιμένουν ένα τυχαίο χρονικό διάστημα βάσει του αλγορίθμου δυαδικής εκθετικής οπισθοχώρησης (Binary Exponential Backoff).",
        "funFacts": [
            "Με τη μετάβαση σε switches πλήρους αμφίδρομης επικοινωνίας (Full-Duplex Ethernet) και οπτικές ίνες, οι συγκρούσεις εξαλείφθηκαν και το CSMA/CD δεν χρησιμοποιείται πλέον στα σύγχρονα ενσύρματα δίκτυα.",
            "Στα ασύρματα δίκτυα Wi-Fi χρησιμοποιείται η παραλλαγή CSMA/CA (Collision Avoidance) επειδή οι ασύρματοι πομποδέκτες δεν μπορούν να ακούν ενώ εκπέμπουν."
        ],
        "source": "https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection",
        "tags": ["technology", "networking", "ethernet", "csmacd", "protocols"]
    },
    {
        "id": "tech_hard_207",
        "text": "Ποια διάσημη ανωμαλία ταυτόχρονων συναλλαγών σε βάσεις δεδομένων (Concurrency Anomaly) συμβαίνει όταν δύο συναλλαγές διαβάζουν επικαλυπτόμενα δεδομένα, παίρνουν αποφάσεις βάσει αυτών και γράφουν σε μη επικαλυπτόμενα πεδία παραβιάζοντας έναν γενικό περιορισμό ακεραιότητας;",
        "correct": "Κλίση Εγγραφής (Write Skew)",
        "distractors": ["Βρώμικη Ανάγνωση (Dirty Read)", "Μη Επαναλήψιμη Ανάγνωση (Non-repeatable Read)", "Χαμένη Ενημέρωση (Lost Update)"],
        "explanation": "Το κλασικό παράδειγμα Write Skew είναι δύο εφημερεύοντες γιατροί που ζητούν ταυτόχρονα άδεια: και οι δύο βλέπουν ότι υπάρχουν 2 ενεργοί γιατροί και το σύστημα εγκρίνει και τις δύο αιτήσεις, αφήνοντας το νοσοκομείο με μηδέν γιατρούς.",
        "funFacts": [
            "Αποτελεί την πιο διαβόητη ανωμαλία που επιτρέπεται στο επίπεδο απομόνωσης Snapshot Isolation.",
            "Αποτρέπεται μόνο με πλήρη σειριοποιησιμότητα (Serializable Isolation) ή με ρητό κλείδωμα επιλογής (SELECT ... FOR UPDATE)."
        ],
        "source": "https://en.wikipedia.org/wiki/Snapshot_isolation#Write_skew",
        "tags": ["technology", "databases", "transactions", "concurrency", "write_skew"]
    },
    {
        "id": "tech_hard_208",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου δρομολόγησης πακέτων στο διαδίκτυο όπου οι δρομολογητές προωθούν πακέτα βάσει σύντομων ετικετών σταθερού μήκους (labels) αντί για περίπλοκες αναζητήσεις πινάκων IP διευθύνσεων μεγάλου μήκους;",
        "correct": "MPLS (Multiprotocol Label Switching)",
        "distractors": ["ATM", "Frame Relay", "SDN"],
        "explanation": "Το MPLS λειτουργεί στο λεγόμενο επίπεδο '2.5' ανάμεσα στο επίπεδο ζεύξης και δικτύου, εισάγοντας ετικέτες (labels) που επιτρέπουν εξαιρετικά γρήγορη προώθηση πακέτων, διαχείριση κίνησης (Traffic Engineering) και εικονικά ιδιωτικά δίκτυα (MPLS VPNs).",
        "funFacts": [
            "Στο MPLS, η απόφαση δρομολόγησης λαμβάνεται μόνο μία φορά στην είσοδο του δικτύου (Ingress Label Edge Router), και οι ενδιάμεσοι κόμβοι απλώς αλλάζουν ετικέτες (label swapping).",
            "Παραμένει η βασική τεχνολογία κορμού τηλεπικοινωνιακών παρόχων παγκοσμίως για τη διασύνδεση επιχειρησιακών δικτύων με εγγυημένο QoS."
        ],
        "source": "https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching",
        "tags": ["technology", "networking", "mpls", "routing", "telecommunications"]
    },
    {
        "id": "tech_hard_209",
        "text": "Ποιο είναι το όνομα της τεχνικής βελτιστοποίησης μεταγλωττιστών που αναλύει εάν οι δείκτες προς ένα δυναμικά δεσμευμένο αντικείμενο στη μνήμη σωρού (heap) παραμένουν αυστηρά εντός του τρέχοντος μεθόδου, επιτρέποντας την ασφαλή δέσμευσή του στη στοίβα (stack);",
        "correct": "Ανάλυση Διαφυγής (Escape Analysis)",
        "distractors": ["Ανάλυση Ενεργών Μεταβλητών (Liveness Analysis)", "Constant Folding", "Tail Call Optimization"],
        "explanation": "Η Ανάλυση Διαφυγής (Escape Analysis) επιτρέπει σε προηγμένους runtime JIT compilers (όπως η Java HotSpot JVM και η Go) να αποφεύγουν τη δέσμευση μνήμης στον σωρό, καταργώντας το κόστος του Garbage Collection μέσω stack allocation ή scalar replacement.",
        "funFacts": [
            "Επιτρέπει επίσης τη βελτιστοποίηση Lock Elision: εάν διαπιστωθεί ότι ένα αντικείμενο δεν διαφεύγει σε άλλα νήματα, ο μεταγλωττιστής αφαιρεί αυτόματα όλα τα κλειδώματα συγχρονισμού (synchronized) πάνω του.",
            "Εισήχθη στη Java 6u14 και βελτιστοποιήθηκε σημαντικά στη Java 8 και νεότερες."
        ],
        "source": "https://en.wikipedia.org/wiki/Escape_analysis",
        "tags": ["technology", "compilers", "jvm", "optimization", "escape_analysis"]
    },
    {
        "id": "tech_hard_210",
        "text": "Ποιο είναι το όνομα του πρωτοκόλλου ανταλλαγής μηνυμάτων και σηματοδοσίας που σχεδιάστηκε από τον Radia Perlman το 1985 (IEEE 802.1D) για την αποτροπή καταστροφικών βρόχων γεφύρωσης (bridge loops) και καταιγίδων αναμετάδοσης (broadcast storms) σε τοπικά δίκτυα Ethernet;",
        "correct": "STP (Spanning Tree Protocol)",
        "distractors": ["TRILL", "LACP", "VTP"],
        "explanation": "Το STP απενεργοποιεί επιλεκτικά πλεονάζουσες φυσικές γραμμές δικτύου δημιουργώντας μια λογική δομή δέντρου χωρίς βρόχους, ενεργοποιώντας τις εφεδρικές γραμμές αυτόματα εάν μια ενεργή γραμμή αποτύχει.",
        "funFacts": [
            "Η δημιουργός του, Radia Perlman, αποκαλείται συχνά 'η μητέρα του Διαδικτύου' και συνόδευσε την παρουσίαση του αλγορίθμου με ένα ποίημα που έγραψε η ίδια, το 'Algorhyme'.",
            "Η σύγχρονη ταχύτερη παραλλαγή του ονομάζεται RSTP (Rapid Spanning Tree Protocol - IEEE 802.1w) και μειώνει τον χρόνο σύγκλισης από 30-50 δευτερόλεπτα σε λίγα χιλιοστά του δευτερολέπτου."
        ],
        "source": "https://en.wikipedia.org/wiki/Spanning_Tree_Protocol",
        "tags": ["technology", "networking", "stp", "ethernet", "radia_perlman"]
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

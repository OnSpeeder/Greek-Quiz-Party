"""Generator for technology_hard questions (Batch 2: tech_hard_061 - tech_hard_110)."""
# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from tools.generators.base_generator import validate_and_append

NEW_QUESTIONS = [
    {
        "id": "tech_hard_061",
        "text": "Ποιο κλασικό πρωτόκολλο συνοχής κρυφής μνήμης (cache coherency) βασίζεται στις τέσσερις καταστάσεις Modified, Exclusive, Shared και Invalid;",
        "answers": [
            "Πρωτόκολλο MESI",
            "Πρωτόκολλο Dragon",
            "Πρωτόκολλο Firefly",
            "Πρωτόκολλο Token Coherence"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρωτόκολλο MESI (γνωστό και ως πρωτόκολλο Illinois) διασφαλίζει ότι όλοι οι επεξεργαστές βλέπουν συνεπή αντίγραφα των κοινόχρηστων γραμμών μνήμης.",
        "funFacts": [
            "Αποτελεί τη βάση πολλών σύγχρονων παραλλαγών, όπως το πρωτόκολλο MOESI (που προσθέτει την κατάσταση Owned) στους επεξεργαστές AMD.",
            "Χρησιμοποιεί τεχνικές bus snooping (παρακολούθηση διαύλου) ή directory-based καταλόγους σε πολυπύρηνα συστήματα πολλών socket."
        ],
        "source": "https://en.wikipedia.org/wiki/MESI_protocol",
        "locale": "el-GR",
        "tags": ["cpu", "hardware", "cache-coherence", "mesi"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_062",
        "text": "Στις τέσσερις συνθήκες Coffman για την εμφάνιση αδιεξόδου (Deadlock), ποια συνθήκη δηλώνει ότι ένας πόρος μπορεί να αποδεσμευτεί μόνο οικειοθελώς από τη διεργασία που τον κατέχει;",
        "answers": [
            "Αμοιβαίος αποκλεισμός (Mutual Exclusion)",
            "Μη προαίρεση (No Preemption)",
            "Κυκλική αναμονή (Circular Wait)",
            "Διακράτηση και αναμονή (Hold and Wait)"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η συνθήκη της μη προαίρεσης (No Preemption) σημαίνει ότι το λειτουργικό σύστημα δεν μπορεί να αφαιρέσει βίαια έναν πόρο από μια διεργασία που τον χρησιμοποιεί.",
        "funFacts": [
            "Οι τέσσερις συνθήκες διατυπώθηκαν το 1971 από τον Edward G. Coffman Jr. και τους συνεργάτες του σε ιστορική επιστημονική δημοσίευση.",
            "Για να εκδηλωθεί αδιέξοδο πρέπει να ισχύουν ταυτόχρονα και οι τέσσερις συνθήκες· η κατάρριψη έστω και μίας αποτρέπει πλήρως το αδιέξοδο."
        ],
        "source": "https://en.wikipedia.org/wiki/Deadlock#Coffman_conditions",
        "locale": "el-GR",
        "tags": ["operating-systems", "deadlock", "concurrency", "coffman"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_063",
        "text": "Ποιος συγκεκριμένος μηχανισμός ασφαλείας του υλικού παρακάμπτεται στην επίθεση Meltdown, επιτρέποντας σε κώδικα χρήστη να διαβάσει μνήμη πυρήνα;",
        "answers": [
            "Ο έλεγχος parity bit στη μνήμη ECC",
            "Η προστασία εγγραφής του BIOS",
            "Ο έλεγχος δικαιωμάτων επιπέδου σελίδας (Supervisor-only) κατά την εκτέλεση εκτός σειράς",
            "Το τείχος προστασίας της κάρτας δικτύου"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η CPU εκτελεί εκτός σειράς την ανάγνωση από τη μνήμη του πυρήνα πριν ολοκληρωθεί ο έλεγχος δικαιωμάτων και, παρότι προκαλείται page fault, τα δεδομένα παραμένουν στην cache.",
        "funFacts": [
            "Ονομάστηκε Meltdown επειδή ουσιαστικά 'έλιωσε' τα θεμελιώδη όρια ασφαλείας που επέβαλλε το υλικό μεταξύ εφαρμογών και λειτουργικού συστήματος.",
            "Επηρέασε σχεδόν όλους τους σύγχρονους επεξεργαστές Intel που κατασκευάστηκαν από το 1995 έως το 2018 (με εξαίρεση τους αρχικούς Itanium και Atom)."
        ],
        "source": "https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)",
        "locale": "el-GR",
        "tags": ["cybersecurity", "meltdown", "hardware", "cpu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_064",
        "text": "Στο κλασικό πρόβλημα των Βυζαντινών Στρατηγών (Lamport et al., 1982), ποιο είναι το ελάχιστο ποσοστό πιστών κόμβων που απαιτείται για την επίτευξη συναίνεσης σε σύγχρονο δίκτυο;",
        "answers": [
            "Τουλάχιστον 50% συν ένας κόμβος",
            "Ακριβώς 100% (μηδενική ανοχή σε προδότες)",
            "Τουλάχιστον 75% των κόμβων",
            "Πάνω από τα δύο τρίτα των κόμβων (αυστηρά περισσότεροι από 2/3)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Αποδείχθηκε μαθηματικά ότι για m προδότες/βυζαντινούς κόμβους απαιτούνται συνολικά τουλάχιστον 3m + 1 κόμβοι (δηλαδή πάνω από τα 2/3 πιστών).",
        "funFacts": [
            "Αν υπάρχουν 3 στρατηγοί και 1 προδότης, η συναίνεση είναι αδύνατη χωρίς τη χρήση κρυπτογραφικών ψηφιακών υπογραφών.",
            "Ο όρος 'Βυζαντινό πρόβλημα' επιλέχθηκε από τον Leslie Lamport για να αντικαταστήσει το αρχικό 'Albanian Generals Problem' ώστε να αποφευχθούν πολιτικές παρεξηγήσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Byzantine_fault",
        "locale": "el-GR",
        "tags": ["distributed-systems", "byzantine-fault", "consensus", "lamport"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_065",
        "text": "Ποια μαθηματική οικογένεια αλγορίθμων αποτελεί τη βάση του προτύπου ML-KEM (CRYSTALS-Kyber) που επέλεξε το NIST για μετακβαντική ασφαλή ανταλλαγή κλειδιών;",
        "answers": [
            "Κρυπτογραφία βασισμένη σε πλέγματα (Lattice-based cryptography)",
            "Κρυπτογραφία ισογενειών ελλειπτικών καμπυλών (Isogeny-based)",
            "Κρυπτογραφία πολυωνυμικών εξισώσεων πολλών μεταβλητών",
            "Κρυπτογραφία βασισμένη σε κώδικες διόρθωσης σφαλμάτων"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρόβλημα Learning With Errors (LWE) σε πλέγματα θεωρείται υπολογιστικά δυσεπίλυτο τόσο για κλασικούς όσο και για κβαντικούς υπολογιστές.",
        "funFacts": [
            "Το NIST τυποποίησε επίσημα το ML-KEM τον Αύγουστο του 2024 ως FIPS 203, σηματοδοτώντας τη μετάβαση στην εποχή μετά το RSA.",
            "Ακόμη και ο κβαντικός αλγόριθμος του Shor δεν προσφέρει πολυωνυμική επιτάχυνση στην επίλυση των προβλημάτων μικρότερου διανύσματος σε πλέγματα υψηλών διαστάσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Kyber",
        "locale": "el-GR",
        "tags": ["cryptography", "post-quantum", "lattices", "nist"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_066",
        "text": "Πώς ονομάζεται ο κορυφαίος κατακερματισμός (root hash) σε ένα κρυπτογραφικό δέντρο Merkle, ο οποίος συνοψίζει μοναδικά ολόκληρο το σύνολο δεδομένων;",
        "answers": [
            "Genesis Hash",
            "Merkle Root",
            "Leaf Anchor",
            "Branch Checksum"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το Merkle Root είναι ο ενιαίος κρυπτογραφικός κατακερματισμός στη ρίζα του δέντρου που επαληθεύει την ακεραιότητα όλων των επιμέρους φύλλων.",
        "funFacts": [
            "Επινοήθηκε το 1979 από τον Ralph Merkle και κατοχυρώθηκε με δίπλωμα ευρεσιτεχνίας το 1982.",
            "Επιτρέπει σε κόμβους ελαφρού βάρους (SPV nodes) στο Bitcoin να επαληθεύουν την ύπαρξη μιας συναλλαγής λαμβάνοντας μόνο έναν λογαριθμικό δρόμο αποδείξεων (Merkle proof)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%94%CE%AD%CE%BD%CF%84%CF%81%CE%BF_Merkle",
        "locale": "el-GR",
        "tags": ["cryptography", "merkle-tree", "data-structures", "blockchain"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_067",
        "text": "Ποιος είναι ο κύριος σκοπός της χρήσης εντολών φραγής μνήμης (Memory Barriers ή Memory Fences) σε πολυνηματικό λογισμικό σε σύγχρονες CPU;",
        "answers": [
            "Να προστατεύουν το λειτουργικό σύστημα από υπερχείλιση στοίβας (stack overflow)",
            "Να διαγράφουν άμεσα όλα τα δεδομένα της μνήμης RAM κατά τον τερματισμό",
            "Να επιβάλλουν αυστηρή σειρά εκτέλεσης πράξεων μνήμης, αποτρέποντας την αναδιάταξη εντολών από τον επεξεργαστή ή τον μεταγλωττιστή",
            "Να αυξάνουν αυτόματα το μέγεθος της φυσικής μνήμης RAM"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Οι επεξεργαστές αναδιατάσσουν εντολές ανάγνωσης/εγγραφής για βελτιστοποίηση· τα barriers εγγυώνται ότι όλες οι προηγούμενες προσπελάσεις ολοκληρώθηκαν πριν τις επόμενες.",
        "funFacts": [
            "Στην αρχιτεκτονική x86 το μοντέλο μνήμης είναι σχετικά ισχυρό (TSO - Total Store Order), ενώ στην ARM είναι ασθενές (weakly ordered), κάνοντας τα fences απαραίτητα.",
            "Σε γλώσσες όπως C++ και C#, λέξεις-κλειδιά όπως `volatile` ή συναρτήσεις τύπου `Thread.MemoryBarrier()` εισάγουν τέτοιες εντολές υλικού."
        ],
        "source": "https://en.wikipedia.org/wiki/Memory_barrier",
        "locale": "el-GR",
        "tags": ["cpu", "concurrency", "memory-barrier", "hardware"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_068",
        "text": "Ποιο είναι το πλάτος σε bits των διανυσματικών καταχωρητών ZMM που εισήγαγε η επέκταση AVX-512 στους επεξεργαστές x86;",
        "answers": [
            "128 bits",
            "256 bits",
            "384 bits",
            "512 bits"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Οι καταχωρητές ZMM έχουν πλάτος 512 bits, επιτρέποντας την ταυτόχρονη εκτέλεση πράξεων σε 16 αριθμούς κινητής υποδιαστολής απλής ακρίβειας (float) ή 8 διπλής ακρίβειας (double).",
        "funFacts": [
            "Στους παλαιότερους επεξεργαστές Intel, η εντατική εκτέλεση εντολών AVX-512 προκαλούσε αυτόματη μείωση της συχνότητας ρολογιού (AVX frequency offset) λόγω τεράστιας κατανάλωσης ισχύος.",
            "Οι προκάτοχοι του AVX-512 ήταν το SSE με καταχωρητές XMM των 128 bits και το AVX/AVX2 με καταχωρητές YMM των 256 bits."
        ],
        "source": "https://en.wikipedia.org/wiki/AVX-512",
        "locale": "el-GR",
        "tags": ["hardware", "cpu", "simd", "avx-512"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_069",
        "text": "Ποια ιδιότητα εγγυάται μαθηματικά η κωδικοποίηση Huffman (Huffman coding) για ένα δεδομένο αλφάβητο γνωστών συχνοτήτων εμφάνισης συμβόλων;",
        "answers": [
            "Παράγει έναν βέλτιστο κώδικα προθέματος (prefix code) ελάχιστου μέσου μήκους",
            "Εξαλείφει πλήρως την ανάγκη για πίνακα αποκωδικοποίησης στον παραλήπτη",
            "Επιτυγχάνει πάντα λόγο συμπίεσης άνω του 90% ανεξαρτήτως εντροπίας",
            "Κρυπτογραφεί ταυτόχρονα το κείμενο με αλγόριθμο μηδενικής γνώσης"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος Huffman κατασκευάζει ένα δυαδικό δέντρο όπου τα συχνότερα σύμβολα λαμβάνουν τις συντομότερες κωδικές λέξεις χωρίς καμία κωδική λέξη να αποτελεί πρόθεμα άλλης.",
        "funFacts": [
            "Αναπτύχθηκε το 1951 από τον David A. Huffman ενώ ήταν φοιτητής στο MIT, ως εργασία εξαμήνου για να αποφύγει την τελική εξέταση του καθηγητή Robert Fano.",
            "Αποτελεί απαραίτητο στάδιο συμπίεσης εντροπίας σε μορφές όπως JPEG, MP3, GZIP και DEFLATE."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CE%B4%CE%B9%CE%BA%CE%B1%CF%82_%CE%A7%CE%AC%CF%86%CE%BC%CE%B1%CE%BD",
        "locale": "el-GR",
        "tags": ["algorithms", "compression", "huffman", "information-theory"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_070",
        "text": "Τι απέδειξε ο Alan Turing το 1936 σχετικά με το περίφημο Πρόβλημα του Τερματισμού (Halting Problem);",
        "answers": [
            "Ότι κάθε πρόγραμμα υπολογιστή τερματίζει σε πεπερασμένο αριθμό βημάτων",
            "Ότι είναι υπολογιστικά μη αποφασίσιμο (undecidable) και κανένας γενικός αλγόριθμος δεν μπορεί να το επιλύσει",
            "Ότι μπορεί να επιλυθεί μόνο με χρήση κβαντικών επεξεργαστών",
            "Ότι ισχύει αποκλειστικά για μηχανές με λιγότερα από 64KB μνήμης"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο Turing απέδειξε μέσω εις άτοπον απαγωγής και διαγωνιοποίησης του Cantor ότι είναι αδύνατο να υπάρξει πρόγραμμα που να αποφασίζει αν ένα τυχαίο πρόγραμμα θα τερματίσει.",
        "funFacts": [
            "Η απόδειξη αυτή έδωσε αρνητική απάντηση στο ιστορικό πρόβλημα Entscheidungsproblem που είχε θέσει ο David Hilbert το 1928.",
            "Αποτέλεσε το πρώτο παράδειγμα μαθηματικού προβλήματος που αποδείχθηκε εγγενώς ανεπίλυτο από οποιονδήποτε μελλοντικό αλγόριθμο."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CF%8C%CE%B2%CE%BB%CE%B7%CE%BC%CE%B1_%CF%84%CE%B5%CF%81%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%81",
        "locale": "el-GR",
        "tags": ["computer-science", "turing", "halting-problem", "theory-of-computation"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_071",
        "text": "Στον κλασικό αλγόριθμο τριχρωματικής σήμανσης (Tri-color marking) για παράλληλη συλλογή απορριμμάτων (Garbage Collection), τι αντιπροσωπεύουν τα τρία χρώματα;",
        "answers": [
            "Κόκκινο (επικίνδυνο), Κίτρινο (σε αναμονή), Πράσινο (ασφαλές)",
            "Μπλε (στατικό), Κίτρινο (δυναμικό), Πράσινο (προσωρινό)",
            "Άσπρο (υποψήφιο προς διαγραφή), Γκρι (προσβάσιμο αλλά ανεξερεύνητο), Μαύρο (προσβάσιμο και πλήρως σαρωμένο)",
            "Μαύρο (κρυπτογραφημένο), Γκρι (συμπιεσμένο), Άσπρο (ασυμπίεστο)"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στο τέλος της φάσης σήμανσης, όλα τα αντικείμενα που παραμένουν άσπρα δεν έχουν διαδρομή από τις ρίζες και απελευθερώνονται με ασφάλεια.",
        "funFacts": [
            "Διατυπώθηκε το 1978 από τον Edsger W. Dijkstra, τον Leslie Lamport και άλλους σε μια από τις πρώτες δημοσιεύσεις για on-the-fly garbage collection.",
            "Αποτελεί το εννοιολογικό θεμέλιο σύγχρονων συλλεκτών χαμηλής καθυστέρησης όπως ο ZGC του Java HotSpot και ο Golang GC."
        ],
        "source": "https://en.wikipedia.org/wiki/Tracing_garbage_collection#Tri-color_marking",
        "locale": "el-GR",
        "tags": ["garbage-collection", "algorithms", "dijkstra", "memory-management"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_072",
        "text": "Ποιος αλγόριθμος αναζήτησης συμβολοσειρών κατασκευάζει ένα πεπερασμένο αυτόματο τύπου Trie με μεταβάσεις αποτυχίας (failure links) για ταυτόχρονη αντιστοίχιση πολλαπλών λέξεων κλειδιών σε γραμμικό χρόνο;",
        "answers": [
            "Αλγόριθμος Boyer-Moore",
            "Αλγόριθμος Rabin-Karp",
            "Αλγόριθμος Needleman-Wunsch",
            "Αλγόριθμος Aho-Corasick"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος Aho-Corasick εντοπίζει όλες τις εμφανίσεις ενός συνόλου λέξεων μέσα σε ένα κείμενο μήκους n σε χρόνο O(n + m + z), ανεξάρτητα από τον αριθμό των λέξεων.",
        "funFacts": [
            "Αναπτύχθηκε το 1975 από τους Alfred Aho και Margaret Corasick στα Bell Labs.",
            "Αποτελεί την κινητήρια δύναμη πίσω από το κλασικό εργαλείο `fgrep` του Unix, καθώς και συστήματα ανίχνευσης εισβολών όπως το Snort."
        ],
        "source": "https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm",
        "locale": "el-GR",
        "tags": ["algorithms", "string-searching", "aho-corasick", "trie"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_073",
        "text": "Ποιος μαθηματικός κανόνας ελέγχου συμφόρησης διέπει τη φάση αποφυγής συμφόρησης (Congestion Avoidance) στο κλασικό πρωτόκολλο TCP Reno;",
        "answers": [
            "AIMD (Additive Increase, Multiplicative Decrease)",
            "MIMD (Multiplicative Increase, Multiplicative Decrease)",
            "AIAD (Additive Increase, Additive Decrease)",
            "MIAD (Multiplicative Increase, Additive Decrease)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στο AIMD, το μέγεθος του παραθύρου συμφόρησης αυξάνεται γραμμικά κατά 1 MSS ανά RTT, αλλά υποδιπλασιάζεται ακαριαία (πολλαπλασιαστικά) σε περίπτωση απώλειας πακέτου.",
        "funFacts": [
            "Αποδείχθηκε από τον Chiu και τον Jain το 1989 ότι ο AIMD είναι ο μόνος κανόνας απόκρισης που εγγυάται σταθερότητα και δικαιοσύνη (fairness) μεταξύ ανταγωνιστικών ροών.",
            "Νεότεροι αλγόριθμοι όπως το BBR της Google βασίζονται στη μέτρηση του διαθέσιμου εύρους ζώνης και της καθυστέρησης RTT αντί για απώλειες πακέτων."
        ],
        "source": "https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease",
        "locale": "el-GR",
        "tags": ["networking", "tcp", "aimd", "congestion-control"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_074",
        "text": "Για ποιο κύριο λόγο τα σύγχρονα συστήματα βάσεων δεδομένων υψηλής έντασης εγγραφών (όπως Bigtable, RocksDB, Cassandra) προτιμούν δομές LSM-Tree έναντι των παραδοσιακών B-Trees;",
        "answers": [
            "Επειδή καταργούν εντελώς την ανάγκη χρήσης δίσκων SSD",
            "Επειδή μετατρέπουν τις τυχαίες εγγραφές σε σειριακές εγγραφές προσάρτησης (append-only), ελαχιστοποιώντας την καθυστέρηση I/O",
            "Επειδή εγγυώνται άμεση εκτέλεση αναζητήσεων χωρίς κανένα ευρετήριο μνήμης",
            "Επειδή δεν απαιτούν ποτέ διαδικασία συμπίεσης ή συγχώνευσης δεδομένων"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Τα LSM-Trees (Log-Structured Merge-trees) συγκρατούν τις εγγραφές σε ένα MemTable στη RAM και τις ξεπλένουν σειριακά στο δίσκο ως αμετάβλητα αρχεία SSTable.",
        "funFacts": [
            "Παρουσιάστηκαν αρχικά το 1996 από τους Patrick O'Neil, Edward O'Neil και Gerhard Weikum.",
            "Απαιτούν μια περιοδική παρασκηνιακή διαδικασία που ονομάζεται 'Compaction' για να διαγράφει παλιές εκδόσεις εγγραφών και να ενοποιεί τα αρχεία SSTable."
        ],
        "source": "https://en.wikipedia.org/wiki/Log-structured_merge-tree",
        "locale": "el-GR",
        "tags": ["databases", "lsm-tree", "storage", "performance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_075",
        "text": "Ποια τεχνική διάσχισης γράφων χρησιμοποιεί ο αλγόριθμος του Robert Tarjan για τον εντοπισμό όλων των ισχυρά συνεκτικών συνιστωσών (SCCs) σε έναν κατευθυνόμενο γράφο σε χρόνο O(V + E);",
        "answers": [
            "Αναζήτηση κατά πλάτος (Breadth-First Search / BFS)",
            "Δυαδική αναζήτηση (Binary Search)",
            "Αναζήτηση κατά βάθος (Depth-First Search / DFS) με τιμές low-link και στοίβα",
            "Αλγόριθμος Floyd-Warshall"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος του Tarjan εκτελεί μία μόνο διάσχιση DFS, διατηρώντας για κάθε κόμβο τον δείκτη ανακάλυψης και τη χαμηλότερη προσβάσιμη κορυφή (low-link).",
        "funFacts": [
            "Δημοσιεύθηκε το 1972 από τον Robert Tarjan, ο οποίος αργότερα βραβεύτηκε με το Βραβείο Turing (1986).",
            "Μια εναλλακτική μέθοδος για το ίδιο πρόβλημα είναι ο αλγόριθμος Kosaraju, ο οποίος όμως απαιτεί δύο πλήρεις διελεύσεις DFS (μία στον αρχικό και μία στον ανάστροφο γράφο)."
        ],
        "source": "https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm",
        "locale": "el-GR",
        "tags": ["algorithms", "graphs", "tarjan", "dfs"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_076",
        "text": "Για ποιο θεμελιώδη λόγο η ευπάθεια Spectre είναι εγγενώς πολύ δυσκολότερο να επιδιορθωθεί στο υλικό σε σχέση με την ευπάθεια Meltdown;",
        "answers": [
            "Επειδή το Spectre προσβάλλει μόνο κάρτες γραφικών και όχι επεξεργαστές",
            "Επειδή απαιτεί την πλήρη κατάργηση των λειτουργικών συστημάτων 64-bit",
            "Επειδή δημιουργήθηκε σκόπιμα από κατασκευαστές αντιικών προγραμμάτων",
            "Επειδή εκμεταλλεύεται την ίδια την πρόβλεψη διακλαδώσεων, η οποία δεν μπορεί να απενεργοποιηθεί χωρίς δραματική κατάρρευση των επιδόσεων της CPU"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ενώ το Meltdown οφειλόταν σε ελαττωματική παράλειψη ελέγχου δικαιωμάτων (που διορθώθηκε στο πυρίτιο), το Spectre χειραγωγεί την πρόβλεψη διακλαδώσεων που αποτελεί αναγκαίο θεμέλιο των σύγχρονων CPU.",
        "funFacts": [
            "Η αντιμετώπιση του Spectre απαίτησε τεχνικές όπως το 'Retpoline' (return trampoline) σε μεταγλωττιστές και μικροκώδικα (microcode updates) για περιορισμό της εικαστικής εκτέλεσης.",
            "Αποκαλύφθηκε ταυτόχρονα με το Meltdown τον Ιανουάριο του 2018 από ανεξάρτητους ερευνητές του Google Project Zero και του Πανεπιστημίου του Graz."
        ],
        "source": "https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)",
        "locale": "el-GR",
        "tags": ["cybersecurity", "spectre", "hardware", "cpu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_077",
        "text": "Στη μαθηματική θεμελίωση του αλγορίθμου RSA, πώς υπολογίζεται η τιμή της συνάρτησης Euler φ(n) για το μέτρο n = p * q, όπου p και q είναι διακριτοί πρώτοι αριθμοί;",
        "answers": [
            "φ(n) = (p - 1) * (q - 1)",
            "φ(n) = p + q - 1",
            "φ(n) = (p * q) - 1",
            "φ(n) = (p + 1) * (q + 1)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Επειδή η συνάρτηση φ του Euler είναι πολλαπλασιαστική και για πρώτο p ισχύει φ(p) = p - 1, έχουμε φ(n) = φ(p)*φ(q) = (p - 1)*(q - 1).",
        "funFacts": [
            "Το ιδιωτικό κλειδί d υπολογίζεται ως ο πολλαπλασιαστικός αντίστροφος του e modulo φ(n), δηλαδή d * e ≡ 1 (mod φ(n)).",
            "Αν κάποιος επιτιθέμενος μπορέσει να παραγοντοποιήσει το n στα p και q, υπολογίζει αμέσως το φ(n) και συνεπώς το μυστικό ιδιωτικό κλειδί d."
        ],
        "source": "https://el.wikipedia.org/wiki/RSA_(%CE%B1%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82)",
        "locale": "el-GR",
        "tags": ["cryptography", "rsa", "math", "euler"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_078",
        "text": "Τι συμβαίνει στο υλικό και το λογισμικό όταν μια διεργασία προσπαθεί να προσπελάσει μια εικονική διεύθυνση μνήμης της οποίας η σελίδα δεν είναι φορτωμένη στη φυσική RAM;",
        "answers": [
            "Ο υπολογιστής απενεργοποιείται αυτόματα για λόγους πυρασφάλειας",
            "Η MMU εγείρει μια διακοπή Page Fault και ο πυρήνας του λειτουργικού συστήματος φορτώνει τη σελίδα από το δίσκο (swap/backing store)",
            "Η CPU αγνοεί την εντολή και συνεχίζει στην επόμενη γραμμή χωρίς καμία ενέργεια",
            "Η διεργασία διαγράφεται αμετάκλητα και στέλνεται αναφορά σφάλματος στο BIOS"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το Page Fault είναι μια εξαίρεση υλικού που καλεί το handler του πυρήνα για να εκτελέσει demand paging και να ενημερώσει τον πίνακα σελίδων.",
        "funFacts": [
            "Αν η διεύθυνση είναι εντελώς εκτός των έγκυρων ορίων μνήμης της διεργασίας, ο πυρήνας παράγει ένα σφάλμα κατάτμησης (Segmentation Fault / SIGSEGV).",
            "Όταν η μνήμη RAM εξαντληθεί και το σύστημα ξοδεύει όλο το χρόνο του φορτώνοντας και εκφορτώνοντας σελίδες από το δίσκο, το φαινόμενο ονομάζεται 'Thrashing'."
        ],
        "source": "https://en.wikipedia.org/wiki/Page_fault",
        "locale": "el-GR",
        "tags": ["operating-systems", "virtual-memory", "page-fault", "mmu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_079",
        "text": "Ποια θεμελιώδη σχέση μεταξύ γεγονότων σε ένα κατανεμημένο σύστημα εισήγαγε ο Leslie Lamport το 1978 μέσω των λογικών ρολογιών (Lamport timestamps);",
        "answers": [
            "Σχέση απόλυτου συγχρονισμού GPS",
            "Σχέση ισοτιμίας Hamming",
            "Σχέση 'συνέβη-πριν' (Happened-Before relation / μερική διάταξη αιτιότητας)",
            "Σχέση κυκλικής κρυπτογράφησης"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η σχέση 'happened-before' (συμβολίζεται ως →) ορίζει μια μερική αιτιατή διάταξη γεγονότων χωρίς να απαιτούνται απόλυτα συγχρονισμένα φυσικά ρολόγια.",
        "funFacts": [
            "Η δημοσίευση του 1978 'Time, Clocks, and the Ordering of Events in a Distributed System' είναι μια από τις πλέον αναφερόμενες στην επιστήμη υπολογιστών.",
            "Αν δύο γεγονότα a και b δεν σχετίζονται αιτιατά (δηλαδή ούτε a → b ούτε b → a), τότε θεωρούνται ταυτόχρονα (concurrent)."
        ],
        "source": "https://en.wikipedia.org/wiki/Lamport_timestamp",
        "locale": "el-GR",
        "tags": ["distributed-systems", "lamport", "clocks", "concurrency"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_080",
        "text": "Ποιο είναι το μέγιστο επιτρεπόμενο όριο σωματιδίων σκόνης μεγέθους 0,1 μικρομέτρων ανά κυβικό μέτρο αέρα σε ένα περιβάλλον καθαρού δωματίου ISO Class 1 (όπως απαιτείται στη λιθογραφία ημιαγωγών αιχμής);",
        "answers": [
            "Έως 1.000.000 σωματίδια",
            "Έως 10.000 σωματίδια",
            "Έως 500 σωματίδια",
            "Το πολύ 10 σωματίδια ανά κυβικό μέτρο"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρότυπο ISO 14644-1 Class 1 είναι το αυστηρότερο στον κόσμο, επιτρέποντας το πολύ 10 σωματίδια των 0,1 μm ανά m³ για να μην καταστραφούν τα τσιπ νανομέτρων.",
        "funFacts": [
            "Συγκριτικά, ο συνηθισμένος αστικός αέρας που αναπνέουμε περιέχει συνήθως πάνω από 35.000.000 σωματίδια ανά κυβικό μέτρο.",
            "Οι εργαζόμενοι φορούν ειδικές ολόσωμες στολές 'bunny suits' με φίλτρα αέρα για να μην απελευθερώνουν νεκρά κύτταρα δέρματος ή ίνες ρούχων."
        ],
        "source": "https://en.wikipedia.org/wiki/Cleanroom",
        "locale": "el-GR",
        "tags": ["semiconductors", "cleanroom", "hardware", "manufacturing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_081",
        "text": "Ποιο είναι το καθοριστικό πλεονέκτημα της τεχνικής Συνεπούς Κατακερματισμού (Consistent Hashing) σε κατανεμημένες κρυφές μνήμες και βάσεις δεδομένων;",
        "answers": [
            "Κατά την προσθήκη ή αφαίρεση ενός κόμβου, χρειάζεται να μετακινηθεί κατά μέσο όρο μόνο το K/n κλειδιά",
            "Δεν απαιτεί καμία συνάρτηση κατακερματισμού για την αποθήκευση δεδομένων",
            "Κρυπτογραφεί αυτόματα όλα τα δεδομένα με κλειδιά μιας χρήσης",
            "Εγγυάται ότι όλοι οι διακομιστές έχουν ακριβώς την ίδια διεύθυνση IP"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Σε αντίθεση με το απλό modulo (hash % n) όπου η αλλαγή του n επανατοποθετεί σχεδόν όλα τα κλειδιά, το consistent hashing αντιστοιχίζει κόμβους και κλειδιά σε έναν νοητό δακτύλιο.",
        "funFacts": [
            "Εισήχθη το 1997 από τον David Karger και άλλους στο MIT για χρήση σε δίκτυα διανομής περιεχομένου (CDN) και οδήγησε στην ίδρυση της Akamai Technologies.",
            "Χρησιμοποιείται σε κατανεμημένα συστήματα αποθήκευσης όπως το Amazon DynamoDB, το Apache Cassandra και το Memcached."
        ],
        "source": "https://en.wikipedia.org/wiki/Consistent_hashing",
        "locale": "el-GR",
        "tags": ["distributed-systems", "consistent-hashing", "databases", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_082",
        "text": "Για ποιο λόγο οι κλασικές αρχιτεκτονικές επεξεργαστών RISC (όπως MIPS, SPARC και αρχικές ARM) χρησιμοποιούν αυστηρά εντολές σταθερού μήκους (π.χ. 32-bit);",
        "answers": [
            "Για να μπορούν να εκτελούν μόνο πράξεις πρόσθεσης και ποτέ πολλαπλασιασμού",
            "Για να απλοποιείται ριζικά το υλικό αποκωδικοποίησης και να διευκολύνεται η διοχέτευση (pipelining)",
            "Επειδή οι διαχειριστές μνήμης δεν μπορούν να διαβάσουν αριθμούς που δεν διαιρούνται με το 8",
            "Για να μην μπορούν οι χρήστες να γράψουν προγράμματα άνω των 1000 γραμμών"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Με εντολές σταθερού μήκους, ο επεξεργαστής γνωρίζει τη θέση της επόμενης εντολής πριν καν αποκωδικοποιήσει την τρέχουσα, απλοποιώντας το pipeline fetching.",
        "funFacts": [
            "Αντίθετα, η αρχιτεκτονική x86 (CISC) έχει εντολές μεταβλητού μήκους από 1 έως 15 bytes, απαιτώντας πολύπλοκους αποκωδικοποιητές στο πυρίτιο.",
            "Οι σύγχρονες CPU x86 μεταφράζουν εσωτερικά τις πολύπλοκες εντολές x86 σε απλούστερες εσωτερικές εντολές σταθερότερης μορφής τύπου RISC, γνωστές ως micro-ops (μ-ops)."
        ],
        "source": "https://en.wikipedia.org/wiki/Reduced_instruction_set_computer",
        "locale": "el-GR",
        "tags": ["computer-architecture", "risc", "cisc", "cpu"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_083",
        "text": "Ποιος προϋπολογισμένος πίνακας επιτρέπει στον αλγόριθμο Knuth-Morris-Pratt (KMP) να μην οπισθοδρομεί ποτέ τον δείκτη του κυρίως κειμένου κατά την αναζήτηση προτύπου;",
        "answers": [
            "Ο πίνακας κατακερματισμού Murmur3",
            "Ο πίνακας Huffman frequencies",
            "Ο πίνακας μερικής αντιστοίχισης (π table / failure function)",
            "Ο πίνακας γειτνίασης γραφήματος"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο πίνακας π καταγράφει το μήκος του μακρύτερου γνήσιου προθέματος που είναι ταυτόχρονα και επίθεμα του προτύπου, επιτρέποντας άμεσα άλματα σε περίπτωση αναντιστοιχίας.",
        "funFacts": [
            "Δημοσιεύθηκε το 1977 από τους Donald Knuth, James H. Morris και Vaughan Pratt.",
            "Εγγυάται αυστηρή χρονική πολυπλοκότητα O(n + m) στη χειρότερη περίπτωση, σε αντίθεση με την απλοϊκή αναζήτηση που μπορεί να χρειαστεί O(n * m)."
        ],
        "source": "https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm",
        "locale": "el-GR",
        "tags": ["algorithms", "kmp", "string-searching", "knuth"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_084",
        "text": "Ποιο κρίσιμο πρόβλημα σε ασύγχρονα κατανεμημένα συστήματα επιλύει ο αλγόριθμος Chandy-Lamport (1985);",
        "answers": [
            "Την αυτόματη συμπίεση όλων των αρχείων ήχου στο δίκτυο",
            "Την αποτροπή κυβερνοεπιθέσεων άρνησης εξυπηρέτησης (DDoS)",
            "Την ασύρματη φόρτιση των φορητών συσκευών",
            "Την καταγραφή ενός συνεπούς καθολικού στιγμιοτύπου (global snapshot) της κατάστασης χωρίς πάγωμα του συστήματος"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Χρησιμοποιεί ειδικά μηνύματα-σημαδούρες (markers) στα κανάλια επικοινωνίας για να καταγράψει τις τοπικές καταστάσεις και τα μηνύματα εν πτήσει, δημιουργώντας ένα συνεπές checkpoint.",
        "funFacts": [
            "Αποτελεί θεμέλιο για τον εντοπισμό τερματισμού, την ανίχνευση αδιεξόδων (deadlocks) και μηχανισμούς checkpoint/recovery σε κατανεμημένα περιβάλλοντα.",
            "Ο Leslie Lamport έχει δηλώσει ότι η ιδέα γεννήθηκε σε ένα δείπνο όταν ο Mani Chandy του ανέφερε το πρόβλημα καταγραφής στιγμιοτύπου."
        ],
        "source": "https://en.wikipedia.org/wiki/Chandy%E2%80%93Lamport_algorithm",
        "locale": "el-GR",
        "tags": ["distributed-systems", "chandy-lamport", "snapshots", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_085",
        "text": "Ποιος μηχανισμός του πυρήνα Linux εισήχθη ως άμεση άμυνα λογισμικού κατά της ευπάθειας Meltdown, διαχωρίζοντας πλήρως τους πίνακες σελίδων χρήστη και πυρήνα;",
        "answers": [
            "KPTI (Kernel Page Table Isolation)",
            "SELinux (Security-Enhanced Linux)",
            "AppArmor",
            "Control Groups (cgroups)"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το KPTI απομονώνει πλήρως τον χώρο διευθύνσεων του πυρήνα όταν εκτελείται κώδικας χρήστη, ώστε να μην υπάρχει τίποτα ευαίσθητο προς ανάγνωση μέσω side-channel.",
        "funFacts": [
            "Αρχικά αναπτύχθηκε υπό το χιουμοριστικό όνομα KAISER από ερευνητές του TU Graz πριν γίνει γνωστή δημοσίως η ύπαρξη του Meltdown.",
            "Επέβαλε κόστος επιδόσεων έως και 30% σε εφαρμογές με πολλές κλήσεις συστήματος (system calls), καθώς κάθε μετάβαση απαιτούσε αλλαγή CR3 και εκκαθάριση του TLB."
        ],
        "source": "https://en.wikipedia.org/wiki/Kernel_page-table_isolation",
        "locale": "el-GR",
        "tags": ["linux", "kpti", "meltdown", "cybersecurity", "kernel"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_086",
        "text": "Ποιο είναι το κύριο πλεονέκτημα των συλλεκτών απορριμμάτων τύπου Mark-Compact έναντι των απλών συλλεκτών Mark-Sweep;",
        "answers": [
            "Εκτελούνται πάντα σε μηδενικό χρόνο CPU",
            "Εξαλείφουν τον κατακερματισμό μνήμης (memory fragmentation) συμπιέζοντας τα ζωντανά αντικείμενα σε συνεχόμενο χώρο",
            "Δεν χρειάζονται ποτέ να διατρέξουν τις ρίζες αντικειμένων",
            "Μπορούν να λειτουργήσουν χωρίς καμία υποστήριξη λειτουργικού συστήματος"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο Mark-Sweep αφήνει κενά (τρύπες) στη μνήμη μετά τη διαγραφή, ενώ ο Mark-Compact μετακινεί όλα τα ζωντανά αντικείμενα στην αρχή του σωρού, κάνοντας τις νέες δεσμεύσεις ταχύτατες.",
        "funFacts": [
            "Το τίμημα του Mark-Compact είναι ότι πρέπει να ενημερώσει όλους τους δείκτες (references) προς τα μετακινηθέντα αντικείμενα, αυξάνοντας τον χρόνο παύσης.",
            "Χρησιμοποιείται συνήθως στην παλαιότερη γενιά (Old Generation / Gen 2) εικονικών μηχανών όπως το CLR του .NET και το JVM."
        ],
        "source": "https://en.wikipedia.org/wiki/Mark-compact_algorithm",
        "locale": "el-GR",
        "tags": ["garbage-collection", "mark-compact", "memory-management", "compilers"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_087",
        "text": "Πόσοι κύκλοι επικοινωνίας μετ' επιστροφής (Round-Trip Times - RTT) απαιτούνται για την ολοκλήρωση της πλήρους αρχικής χειραψίας στο πρωτόκολλο TLS 1.3 σε σύγκριση με το TLS 1.2;",
        "answers": [
            "3 RTT έναντι 4 RTT",
            "0 RTT πάντα για όλες τις νέες συνδέσεις",
            "1 RTT στο TLS 1.3 έναντι 2 RTT στο TLS 1.2",
            "Ακριβώς 5 RTT και στα δύο πρωτόκολλα"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το TLS 1.3 συνδύασε την ανταλλαγή κλειδιών απευθείας στο πρώτο μήκος μηνύματος ClientHello, μειώνοντας την καθυστέρηση εγκαθίδρυσης στο μισό (1 RTT).",
        "funFacts": [
            "Το TLS 1.3 υποστηρίζει επίσης τη λειτουργία 0-RTT Resumption (Early Data) για προηγουμένως συνδεδεμένους πελάτες, στέλνοντας δεδομένα εφαρμογής στο πρώτο πακέτο.",
            "Κατήργησε εντελώς παρωχημένους και επικίνδυνους αλγορίθμους όπως το RSA key exchange, το RC4, το DES, το 3DES, το MD5 και το SHA-1."
        ],
        "source": "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3",
        "locale": "el-GR",
        "tags": ["security", "tls", "networking", "protocols"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_088",
        "text": "Ποιες είναι οι τρεις κλασικές κατηγορίες κινδύνων (Hazards) που μπορούν να προκαλέσουν καθυστέρηση ή πάγωμα στη διοχέτευση εντολών (Instruction Pipeline) ενός επεξεργαστή;",
        "answers": [
            "Θερμικοί, Ηλεκτρικοί και Μαγνητικοί κίνδυνοι",
            "Συντακτικοί, Λογικοί και Μεταγλωττιστικοί κίνδυνοι",
            "Κρυπτογραφικοί, Δικτυακοί και Πρωτοκολλικοί κίνδυνοι",
            "Δομικοί κίνδυνοι, Κίνδυνοι δεδομένων και Κίνδυνοι ελέγχου (Structural, Data, Control hazards)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Δομικοί κίνδυνοι προκύπτουν από σύγκρουση υλικού, κίνδυνοι δεδομένων από εξαρτήσεις εντολών (RAW, WAR, WAW) και κίνδυνοι ελέγχου από διακλαδώσεις.",
        "funFacts": [
            "Για την αντιμετώπιση των κινδύνων δεδομένων οι CPU χρησιμοποιούν τεχνικές προώθησης δεδομένων (Data Forwarding / Bypassing).",
            "Οι κίνδυνοι ελέγχου αντιμετωπίζονται με πρόβλεψη διακλαδώσεων και καθυστερημένες διακλαδώσεις (branch delay slots) σε παλαιότερα RISC τσιπ."
        ],
        "source": "https://en.wikipedia.org/wiki/Hazard_(computer_architecture)",
        "locale": "el-GR",
        "tags": ["computer-architecture", "cpu", "pipeline", "hazards"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_089",
        "text": "Μέσω ποιου φυσικού διαύλου υψηλής ταχύτητας επικοινωνούν απευθείας οι σύγχρονοι δίσκοι στερεάς κατάστασης NVMe με τον επεξεργαστή, παρακάμπτοντας τους παλιούς ελεγκτές SATA;",
        "answers": [
            "PCIe (PCI Express)",
            "USB 2.0",
            "FireWire 800",
            "RS-232 Serial Port"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρωτόκολλο NVMe σχεδιάστηκε ειδικά για γρήγορη μνήμη flash και αξιοποιεί απευθείας τις γραμμές του διαύλου PCI Express, προσφέροντας τεράστιο bandwidth και χαμηλό latency.",
        "funFacts": [
            "Ενώ το SATA AHCI υποστήριζε μόνο 1 ουρά εντολών βάθους 32 εντολών, το NVMe υποστηρίζει έως 64.000 ουρές με 64.000 εντολές ανά ουρά.",
            "Ένας δίσκος NVMe PCIe 4.0 x4 μπορεί να ξεπεράσει τα 7.000 MB/s, έναντι του θεωρητικού ορίου των 600 MB/s του SATA 3.0."
        ],
        "source": "https://el.wikipedia.org/wiki/NVM_Express",
        "locale": "el-GR",
        "tags": ["hardware", "storage", "nvme", "pcie", "ssd"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_090",
        "text": "Ποιο υπήρξε το πρώτο υπολογιστικό πρόβλημα που αποδείχθηκε ότι είναι NP-πλήρες (NP-complete) μέσω του ιστορικού θεωρήματος Cook-Levin το 1971;",
        "answers": [
            "Το πρόβλημα του περιοδεύοντος πωλητή (Traveling Salesperson Problem)",
            "Το πρόβλημα ικανοποιησιμότητας προτασιακών τύπων Boole (Boolean Satisfiability Problem / SAT)",
            "Ο χρωματισμός γραφημάτων (Graph Coloring)",
            "Το πρόβλημα της στάσης (Halting Problem)"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο Stephen Cook (και ανεξάρτητα ο Leonid Levin) απέδειξε ότι οποιοδήποτε πρόβλημα στην κλάση NP μπορεί να αναχθεί σε πολυωνυμικό χρόνο στο πρόβλημα SAT.",
        "funFacts": [
            "Ένα χρόνο αργότερα, το 1972, ο Richard Karp χρησιμοποίησε το θεώρημα Cook-Levin για να αποδείξει την NP-πληρότητα 21 κλασικών προβλημάτων (Karp's 21 NP-complete problems).",
            "Αν βρεθεί ποτέ πολυωνυμικός αλγόριθμος για το SAT, τότε αυτομάτως P = NP, επιλύοντας το μεγαλύτερο ανοιχτό πρόβλημα της πληροφορικής."
        ],
        "source": "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem",
        "locale": "el-GR",
        "tags": ["computer-science", "np-complete", "sat", "cook-levin"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_091",
        "text": "Στις πολιτικές αντικατάστασης γραμμών κρυφής μνήμης (cache replacement policies), τι αποθηκεύει και παρακολουθεί η πολιτική LRU;",
        "answers": [
            "Τη γραμμή με το μεγαλύτερο μέγεθος αρχείου σε megabytes",
            "Τη γραμμή που διαβάστηκε από το BIOS κατά την εκκίνηση",
            "Τη γραμμή που χρησιμοποιήθηκε πιο πρόσφατα στο παρελθόν, εκδιώκοντας εκείνη με την πιο παλιά τελευταία πρόσβαση (Least Recently Used)",
            "Μια εντελώς τυχαία επιλεγμένη γραμμή μέσω γεννήτριας θορύβου"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η LRU (Least Recently Used) εκδιώκει το στοιχείο που έχει παραμείνει αδρανές για το μεγαλύτερο χρονικό διάστημα, βασιζόμενη στην αρχή της χρονικής τοπικότητας.",
        "funFacts": [
            "Επειδή η πλήρης υλοποίηση της LRU σε υλικό απαιτεί υπερβολικά πολλά transistors και καλωδιώσεις, οι CPU χρησιμοποιούν προσεγγιστικές μεθόδους όπως το Pseudo-LRU (PLRU).",
            "Το Pseudo-LRU χρησιμοποιεί ένα δυαδικό δέντρο δεικτών ανά σετ κρυφής μνήμης, απαιτώντας μόνο n-1 bits για ένα σετ n γραμμών."
        ],
        "source": "https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)",
        "locale": "el-GR",
        "tags": ["cpu", "cache", "hardware", "lru", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_092",
        "text": "Στο κλασικό πρωτόκολλο πρόσβασης κοινόχρηστου μέσου CSMA/CD του παραδοσιακού Ethernet, τι σημαίνουν τα αρχικά 'CD';",
        "answers": [
            "Compact Disc",
            "Carrier Disruption",
            "Continuous Delivery",
            "Collision Detection (Ανίχνευση Σύγκρουσης)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το Collision Detection επιτρέπει στις κάρτες δικτύου να ανιχνεύουν αν δύο σταθμοί μετέδωσαν ταυτόχρονα και να διακόπτουν τη μετάδοση εκτελώντας τυχαία καθυστέρηση (exponential backoff).",
        "funFacts": [
            "Με την καθιέρωση των Ethernet switches πλήρους αμφίδρομης επικοινωνίας (Full-Duplex), το CSMA/CD έπαψε ουσιαστικά να είναι απαραίτητο στα σύγχρονα ενσύρματα δίκτυα.",
            "Στα ασύρματα δίκτυα Wi-Fi χρησιμοποιείται η παραλλαγή CSMA/CA (Collision Avoidance), επειδή ένας ραδιοπομπός δεν μπορεί εύκολα να ακούει συγκρούσεις ενώ εκπέμπει."
        ],
        "source": "https://el.wikipedia.org/wiki/CSMA/CD",
        "locale": "el-GR",
        "tags": ["networking", "ethernet", "csmacd", "protocols"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_093",
        "text": "Ποιο σύγχρονο υποσύστημα ασύγχρονης εισόδου/εξόδου υψηλής απόδοσης προστέθηκε στον πυρήνα Linux 5.1 (από τον Jens Axboe), αξιοποιώντας κοινόχρηστες κυκλικές ουρές (ring buffers) χωρίς κλειδώματα;",
        "answers": [
            "io_uring",
            "aio_compat",
            "kqueue",
            "DirectX DirectStorage"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το `io_uring` επιτρέπει την υποβολή και ολοκλήρωση αιτημάτων I/O χωρίς καμία κλήση συστήματος (system call overhead) σε λειτουργία polling.",
        "funFacts": [
            "Χρησιμοποιεί δύο κύριες ουρές που μοιράζονται μεταξύ user-space και kernel: την ουρά υποβολής (Submission Queue) και την ουρά ολοκλήρωσης (Completion Queue).",
            "Έχει υιοθετηθεί από βάσεις δεδομένων και διακομιστές υψηλών ταχυτήτων όπως το PostgreSQL, το Netty και το RocksDB για εκτόξευση των IOPS."
        ],
        "source": "https://en.wikipedia.org/wiki/Io_uring",
        "locale": "el-GR",
        "tags": ["linux", "kernel", "io-uring", "operating-systems", "performance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_094",
        "text": "Ποιο ιστορικό πρωτόκολλο Κβαντικής Διανομής Κλειδιών (QKD) προτάθηκε το 1984 από τους Charles Bennett και Gilles Brassard, χρησιμοποιώντας καταστάσεις πόλωσης φωτονίων;",
        "answers": [
            "Πρωτόκολλο E91",
            "Πρωτόκολλο BB84",
            "Πρωτόκολλο B92",
            "Πρωτόκολλο SARG04"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το πρωτόκολλο BB84 εκμεταλλεύεται το θεώρημα μη-κλωνοποίησης (no-cloning theorem) και την αρχή απροσδιοριστίας του Heisenberg, ώστε οποιαδήποτε υποκλοπή να γίνεται αμέσως αντιληπτή.",
        "funFacts": [
            "Αν ένας τρίτος (η 'Eve') προσπαθήσει να μετρήσει τα φωτόνια εν πτήσει, αναπόφευκτα διαταράσσει την κβαντική τους κατάσταση και εισάγει ανιχνεύσιμα σφάλματα.",
            "Ήταν το πρώτο λειτουργικό πρωτόκολλο κβαντικής κρυπτογραφίας στην ιστορία και δοκιμάστηκε πειραματικά σε εργαστήριο της IBM το 1989."
        ],
        "source": "https://en.wikipedia.org/wiki/BB84",
        "locale": "el-GR",
        "tags": ["quantum-computing", "cryptography", "bb84", "physics"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_095",
        "text": "Στον σχεδιασμό σχεσιακών βάσεων δεδομένων, ποια είναι η αυστηρή απαίτηση για να βρίσκεται ένας πίνακας στην Κανονική Μορφή Boyce-Codd (BCNF);",
        "answers": [
            "Να μην περιέχει κανέναν αριθμητικό πίνακα",
            "Όλα τα κλειδιά να είναι κρυπτογραφημένα με SHA-256",
            "Για κάθε μη τετριμμένη συναρτησιακή εξάρτηση X → Y, το X πρέπει να είναι υπερκλειδί (superkey)",
            "Να διαθέτει τουλάχιστον τρία εξωτερικά κλειδιά (foreign keys)"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η BCNF (γνωστή και ως 3.5NF) είναι μια ελαφρώς αυστηρότερη έκδοση της Τρίτης Κανονικής Μορφής (3NF), εξαλείφοντας κάθε πλεονασμό που οφείλεται σε συναρτησιακές εξαρτήσεις.",
        "funFacts": [
            "Ονομάστηκε προς τιμήν των Raymond F. Boyce και Edgar F. Codd (του θεμελιωτή του σχεσιακού μοντέλου βάσεων δεδομένων).",
            "Σε σπάνιες περιπτώσεις, η διάσπαση ενός πίνακα σε BCNF μπορεί να μην διατηρεί όλες τις αρχικές συναρτησιακές εξαρτήσεις, οπότε προτιμάται η 3NF."
        ],
        "source": "https://en.wikipedia.org/wiki/Boyce%E2%80%93Codd_normal_form",
        "locale": "el-GR",
        "tags": ["databases", "normalization", "bcnf", "relational-model"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_096",
        "text": "Ποια συναρτησιακή γλώσσα προγραμματισμού της Ericsson (1986) σχεδιάστηκε ειδικά γύρω από το Μοντέλο Ηθοποιών (Actor Model) για να προσφέρει τηλεπικοινωνιακή διαθεσιμότητα 'εννέα εννιάρια' (99.9999999%);",
        "answers": [
            "Fortran",
            "Prolog",
            "Ada",
            "Erlang"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η Erlang (μαζί με την πλατφόρμα OTP) υλοποιεί ανεξάρτητους ηθοποιούς που επικοινωνούν αποκλειστικά μέσω ασύγχρονων μηνυμάτων και εποπτεύονται από δέντρα επίβλεψης (supervisors).",
        "funFacts": [
            "Η φιλοσοφία διαχείρισης σφαλμάτων της Erlang συνοψίζεται στη διάσημη αρχή: 'Let it crash' (άφησέ το να καταρρεύσει και άσε τον επόπτη να το επανεκκινήσει).",
            "Πάνω στην εικονική μηχανή BEAM της Erlang βασίστηκαν η γλώσσα Elixir και το backend του WhatsApp, εξυπηρετώντας δισεκατομμύρια χρήστες με ελάχιστους διακομιστές."
        ],
        "source": "https://el.wikipedia.org/wiki/Erlang",
        "locale": "el-GR",
        "tags": ["programming-languages", "erlang", "actor-model", "concurrency"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_097",
        "text": "Τι δηλώνει η θεμελιώδης Αρχή του Kerckhoffs (1883) στη σύγχρονη κρυπτογραφία;",
        "answers": [
            "Ένα κρυπτοσύστημα πρέπει να είναι ασφαλές ακόμη και αν τα πάντα σχετικά με τον αλγόριθμο είναι δημόσια γνωστά, εκτός από το μυστικό κλειδί",
            "Τα κρυπτογραφικά κλειδιά πρέπει να αλλάζουν υποχρεωτικά κάθε 24 ώρες",
            "Κανένας υπολογιστής δεν επιτρέπεται να εκτελεί πάνω από έναν αλγόριθμο ταυτόχρονα",
            "Η κρυπτογράφηση επιτρέπεται μόνο για στρατιωτικές τηλεπικοινωνίες"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η ασφάλεια μέσω αφάνειας (security through obscurity) απορρίπτεται· η αξιοπιστία ενός συστήματος εξαρτάται αποκλειστικά από τη διατήρηση της μυστικότητας του κλειδιού.",
        "funFacts": [
            "Διατυπώθηκε από τον Ολλανδό στρατιωτικό κρυπτογράφο Auguste Kerckhoffs στο άρθρο 'La Cryptographie militaire'.",
            "Επαναδιατυπώθηκε από τον Claude Shannon ως 'Shannon's Maxim': 'Ο εχθρός γνωρίζει το σύστημα' ('The enemy knows the system')."
        ],
        "source": "https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle",
        "locale": "el-GR",
        "tags": ["cryptography", "security", "kerckhoffs", "principles"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_098",
        "text": "Πώς ονομάζεται ο τύπος κατακερματισμού μνήμης που προκύπτει όταν ο χώρος που δεσμεύεται σε μια σελίδα μνήμης είναι μεγαλύτερος από τα πραγματικά δεδομένα που χρειάζεται η διεργασία;",
        "answers": [
            "Εξωτερικός κατακερματισμός (External fragmentation)",
            "Εσωτερικός κατακερματισμός (Internal fragmentation)",
            "Εικονικός κατακερματισμός (Virtual fragmentation)",
            "Δυναμικός κατακερματισμός (Dynamic fragmentation)"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο εσωτερικός κατακερματισμός αφορά τον αχρησιμοποίητο χώρο μέσα σε ένα εκχωρημένο μπλοκ ή σελίδα (π.χ. όταν ζητούνται 100 bytes αλλά δεσμεύεται ολόκληρη σελίδα 4KB).",
        "funFacts": [
            "Αντίθετα, ο εξωτερικός κατακερματισμός εμφανίζεται στην τμηματοποίηση (segmentation), όταν υπάρχει αρκετή συνολική ελεύθερη μνήμη αλλά είναι κατακερματισμένη σε μη συνεχόμενα κομμάτια.",
            "Η χρήση συστημάτων Buddy Allocator και Slab Allocator στον πυρήνα βοηθά στη δραστική μείωση του εσωτερικού κατακερματισμού."
        ],
        "source": "https://en.wikipedia.org/wiki/Fragmentation_(computing)#Internal_fragmentation",
        "locale": "el-GR",
        "tags": ["operating-systems", "memory-management", "fragmentation"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_099",
        "text": "Ποια εξειδικευμένη κλήση συστήματος (system call) στο Linux μεταφέρει δεδομένα απευθείας από έναν περιγραφέα αρχείου σε ένα socket δικτύου εξ ολοκλήρου μέσα στον πυρήνα (Zero-Copy);",
        "answers": [
            "read()",
            "fork()",
            "sendfile()",
            "select()"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η `sendfile()` αντιγράφει δεδομένα απευθείας από την προσωρινή μνήμη σελίδων (page cache) στην ουρά της κάρτας δικτύου, χωρίς αντιγραφή στο user space.",
        "funFacts": [
            "Εξαλείφει δύο περιττές εναλλαγές περιβάλλοντος (context switches) και δύο περιττές αντιγραφές μνήμης ανά λειτουργία μεταφοράς.",
            "Αποτελεί τον πυρήνα της κορυφαίας ταχύτητας σερβιρίσματος στατικών αρχείων σε δημοφιλείς web servers όπως το Nginx και το Apache."
        ],
        "source": "https://en.wikipedia.org/wiki/Zero-copy",
        "locale": "el-GR",
        "tags": ["linux", "zero-copy", "sendfile", "operating-systems", "performance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_100",
        "text": "Ποια πληροφορία αποθηκεύει ειδικά ο πίνακας BTB (Branch Target Buffer) στη μονάδα πρόβλεψης διακλαδώσεων μιας σύγχρονης CPU;",
        "answers": [
            "Το μέγεθος της κρυφής μνήμης L3",
            "Την ταχύτητα περιστροφής των ανεμιστήρων του συστήματος",
            "Τον κωδικό πρόσβασης του λογαριασμού διαχειριστή",
            "Την προβλεπόμενη διεύθυνση προορισμού (target address) της εντολής διακλάδωσης"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το BTB λειτουργεί ως κρυφή μνήμη που αντιστοιχίζει τη διεύθυνση μιας εντολής άλματος με τη διεύθυνση στην οποία αναμένεται να μεταβεί η εκτέλεση.",
        "funFacts": [
            "Ενώ ο προβλεπτής κατεύθυνσης (Direction Predictor) αποφασίζει αν η διακλάδωση θα ληφθεί (Taken ή Not Taken), το BTB παρέχει άμεσα το 'πού' θα πάει.",
            "Χωρίς το BTB, ο επεξεργαστής θα έπρεπε να περιμένει μέχρι τη φάση αποκωδικοποίησης για να υπολογίσει τη διεύθυνση προορισμού, χάνοντας πολύτιμους κύκλους."
        ],
        "source": "https://en.wikipedia.org/wiki/Branch_target_predictor",
        "locale": "el-GR",
        "tags": ["cpu", "hardware", "branch-prediction", "btb"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_101",
        "text": "Ποιο καταστροφικό φαινόμενο δικτύου αποτρέπει το πρωτόκολλο Spanning Tree Protocol (STP, IEEE 802.1D) της Radia Perlman σε τοπικά δίκτυα Ethernet με περιττές συνδέσεις;",
        "answers": [
            "Τους βρόχους γεφύρωσης και τις καταιγίδες εκπομπής (Bridge loops / Broadcast storms)",
            "Την υποκλοπή κωδικών πρόσβασης μέσω sniffing",
            "Την αποσύνδεση των καλωδίων οπτικών ινών από κραδασμούς",
            "Την υπερβολική κατανάλωση ρεύματος από τα switch"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το STP απενεργοποιεί λογικά τις περιττές φυσικές συνδέσεις ώστε να σχηματίζεται ένα δέντρο χωρίς κύκλους, αποτρέποντας τον ατέρμονα πολλαπλασιασμό πακέτων εκπομπής.",
        "funFacts": [
            "Επινοήθηκε το 1985 από τη Radia Perlman, η οποία συνόδευσε την ανακάλυψή της με ένα διάσημο ποίημα με τίτλο 'Algorhyme'.",
            "Αν μια ενεργή σύνδεση κοπεί, το STP επαναϋπολογίζει αυτόματα την τοπολογία και ενεργοποιεί την εφεδρική γραμμή μέσα σε λίγα δευτερόλεπτα (ή χιλιοστά με το Rapid STP)."
        ],
        "source": "https://el.wikipedia.org/wiki/Spanning_Tree_Protocol",
        "locale": "el-GR",
        "tags": ["networking", "stp", "ethernet", "radia-perlman"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_102",
        "text": "Ποιο είναι το ουσιαστικό πλεονέκτημα των διανυσματικών ρολογιών (Vector Clocks) σε σύγκριση με τα απλά βαθμωτά λογικά ρολόγια του Lamport;",
        "answers": [
            "Μπορούν να λειτουργήσουν χωρίς καμία σύνδεση δικτύου",
            "Μπορούν να ανιχνεύσουν εάν δύο γεγονότα είναι ταυτόχρονα/ανεξάρτητα ή αν συνδέονται αιτιατά",
            "Συγχρονίζονται αυτόματα με τα ατομικά ρολόγια καισίου",
            "Χρησιμοποιούν αποκλειστικά έναν μόνο ακέραιο αριθμό 8-bit"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Στα διανυσματικά ρολόγια, κάθε διεργασία διατηρεί ένα διάνυσμα με τις καταστάσεις όλων των κόμβων, επιτρέποντας την πλήρη αναγνώριση ταυτόχρονων (concurrent) συγκρούσεων.",
        "funFacts": [
            "Αναπτύχθηκαν ανεξάρτητα το 1988 από τον Colin Fidge και τον Friedemann Mattern.",
            "Χρησιμοποιούνται ευρύτατα σε κατανεμημένες βάσεις δεδομένων NoSQL (όπως το Dynamo και το Riak) για την ανίχνευση αντικρουόμενων εκδόσεων εγγράφων."
        ],
        "source": "https://en.wikipedia.org/wiki/Vector_clock",
        "locale": "el-GR",
        "tags": ["distributed-systems", "vector-clocks", "concurrency", "algorithms"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_103",
        "text": "Στη θεωρία υπολογιστικής πολυπλοκότητας, ποια είναι η ακριβής περιγραφή της κλάσης προβλημάτων P;",
        "answers": [
            "Προβλήματα που μπορούν να επιλυθούν μόνο με κβαντικό υπολογιστή",
            "Προβλήματα των οποίων η λύση απαιτεί εκθετικό χρόνο σε όλες τις περιπτώσεις",
            "Προβλήματα αποφάσεως που μπορούν να επιλυθούν σε πολυωνυμικό χρόνο από μια αιτιοκρατική μηχανή Turing",
            "Προβλήματα που είναι αποδεδειγμένα αδύνατο να επιλυθούν ποτέ"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η κλάση P (Polynomial Time) περιλαμβάνει όλα τα προβλήματα που θεωρούνται πρακτικά υπολογίσιμα (tractable) με αλγορίθμους O(n^k).",
        "funFacts": [
            "Αντίθετα, η κλάση NP περιλαμβάνει προβλήματα των οποίων η λύση μπορεί να επαληθευτεί (και όχι απαραίτητα να βρεθεί) σε πολυωνυμικό χρόνο.",
            "Το ερώτημα εάν P = NP αποτελεί ένα από τα επτά Προβλήματα της Χιλιετίας του Ινστιτούτου Clay, συνοδευόμενο από έπαθλο 1.000.000 δολαρίων."
        ],
        "source": "https://el.wikipedia.org/wiki/P_(%CE%BA%CE%BB%CE%AC%CF%83%CE%B7_%CF%80%CE%BF%CE%BB%CF%85%CF%80%CE%BB%CE%BF%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82)",
        "locale": "el-GR",
        "tags": ["computer-science", "complexity-theory", "p-vs-np", "turing"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_104",
        "text": "Ποιους φυσικούς πόρους διπλασιάζει στο πυρίτιο η τεχνολογία ταυτόχρονης πολυνημάτωσης (SMT / Hyper-Threading) ανά λογικό πυρήνα;",
        "answers": [
            "Ολόκληρη την αριθμητική λογική μονάδα (ALU) και τους αποκωδικοποιητές",
            "Την εξωτερική παροχή ρεύματος και τους ακροδέκτες της μητρικής",
            "Την οθόνη του υπολογιστή και την κάρτα γραφικών",
            "Την αρχιτεκτονική κατάσταση καταχωρητών (architectural state) και τον μετρητή προγράμματος (instruction pointer)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το SMT διπλασιάζει μόνο τους καταχωρητές κατάστασης, επιτρέποντας σε δύο νήματα να μοιράζονται δυναμικά τις ίδιες μονάδες εκτέλεσης (ALUs, FPUs) και caches.",
        "funFacts": [
            "Η Intel εισήγαγε το Hyper-Threading στους επεξεργαστές Xeon και Pentium 4 (Northwood) το 2002.",
            "Προσφέρει τυπική αύξηση επιδόσεων 15-30% αξιοποιώντας κύκλους όπου ένας πυρήνας θα παρέμενε αδρανής περιμένοντας δεδομένα από τη μνήμη."
        ],
        "source": "https://en.wikipedia.org/wiki/Simultaneous_multithreading",
        "locale": "el-GR",
        "tags": ["hardware", "cpu", "hyper-threading", "smt"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_105",
        "text": "Ποιο δυσεπίλυτο μαθηματικό πρόβλημα αποτελεί τη βάση ασφάλειας του κλασικού αλγορίθμου ανταλλαγής κλειδιών Diffie-Hellman σε πολλαπλασιαστικές ομάδες;",
        "answers": [
            "Το πρόβλημα του διακριτού λογαρίθμου (Discrete Logarithm Problem)",
            "Η επίλυση εξισώσεων τρίτου βαθμού με τύπους Cardano",
            "Η διαίρεση με το μηδέν σε μιγαδικούς αριθμούς",
            "Ο υπολογισμός των δεκαδικών ψηφίων του αριθμού π"
        ],
        "correctAnswerIndex": 0,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Είναι εύκολο να υπολογιστεί το g^a mod p, αλλά υπολογιστικά εξαιρετικά δύσκολο να βρεθεί ο εκθέτης a γνωρίζοντας μόνο το αποτέλεσμα g^a mod p, τη βάση g και το πρώτο μέτρο p.",
        "funFacts": [
            "Οι καλύτεροι γνωστοί κλασικοί αλγόριθμοι επίλυσης (όπως το General Number Field Sieve) έχουν υποεκθετική πολυπλοκότητα.",
            "Σε έναν ιδανικό κβαντικό υπολογιστή, ο αλγόριθμος του Shor μπορεί να επιλύσει το πρόβλημα διακριτού λογαρίθμου σε πολυωνυμικό χρόνο."
        ],
        "source": "https://en.wikipedia.org/wiki/Discrete_logarithm",
        "locale": "el-GR",
        "tags": ["cryptography", "math", "diffie-hellman", "discrete-logarithm"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_106",
        "text": "Πώς διαχειρίζεται τη μνήμη ο μηχανισμός Copy-on-Write (CoW) κατά την κλήση συστήματος `fork()` στα σύγχρονα λειτουργικά συστήματα Unix/Linux;",
        "answers": [
            "Αντιγράφει άμεσα και πλήρως όλα τα megabytes της μνήμης στη νέα διεργασία",
            "Μοιράζει τις ίδιες φυσικές σελίδες ως μόνο για ανάγνωση (read-only) και αντιγράφει μια σελίδα μόνο τη στιγμή που κάποια διεργασία επιχειρεί να γράψει σε αυτήν",
            "Αποθηκεύει ολόκληρη τη διεργασία σε εξωτερικό διακομιστή cloud",
            "Διαγράφει τη μνήμη της γονικής διεργασίας για εξοικονόμηση χώρου"
        ],
        "correctAnswerIndex": 1,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το CoW καθιστά το `fork()` σχεδόν στιγμιαίο, αποφεύγοντας την περιττή αντιγραφή μνήμης όταν η θυγατρική διεργασία εκτελεί αμέσως την κλήση `exec()`.",
        "funFacts": [
            "Όταν επιχειρείται εγγραφή σε μια σελίδα CoW, η MMU εγείρει ένα προστατευτικό page fault, επιτρέποντας στον πυρήνα να δεσμεύσει νέα φυσική σελίδα και να αντιγράψει τα δεδομένα.",
            "Η ευπάθεια Dirty COW (CVE-2016-5195) στο Linux εκμεταλλευόταν μια συνθήκη ανταγωνισμού (race condition) στον μηχανισμό CoW για απόκτηση δικαιωμάτων root."
        ],
        "source": "https://en.wikipedia.org/wiki/Copy-on-write",
        "locale": "el-GR",
        "tags": ["operating-systems", "linux", "copy-on-write", "virtual-memory"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_107",
        "text": "Ποιος άπληστος αλγόριθμος (greedy algorithm) κατασκευάζει ένα Ελάχιστο Συνδετικό Δέντρο (MST) ξεκινώντας από έναν αρχικό κόμβο και προσθέτοντας διαδοχικά τη φθηνότερη ακμή που συνδέει το δέντρο με έναν νέο κόμβο;",
        "answers": [
            "Αλγόριθμος Bellman-Ford",
            "Αλγόριθμος Floyd-Warshall",
            "Αλγόριθμος του Prim",
            "Αλγόριθμος PageRank"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Ο αλγόριθμος του Prim επεκτείνει σταδιακά ένα ενιαίο δέντρο, σε αντίθεση με τον αλγόριθμο του Kruskal που συνενώνει ξεχωριστά δάση ταξινομώντας όλες τις ακμές.",
        "funFacts": [
            "Αναπτύχθηκε αρχικά το 1930 από τον Τσέχο μαθηματικό Vojtěch Jarník και ανακαλύφθηκε ξανά ανεξάρτητα από τον Robert Prim το 1957 και τον Edsger Dijkstra το 1959.",
            "Με τη χρήση σωρού Fibonacci (Fibonacci heap), η χρονική πολυπλοκότητα του αλγορίθμου Prim βελτιστοποιείται σε O(E + V log V)."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%91%CE%BB%CE%B3%CF%8C%CF%81%CE%B9%CE%B8%CE%BC%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A0%CF%81%CE%B9%CE%BC",
        "locale": "el-GR",
        "tags": ["algorithms", "graphs", "minimum-spanning-tree", "prim"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_108",
        "text": "Πώς επιτυγχάνεται ο δυναμικός πολυμορφισμός και η δυναμική αποστολή μεθόδων (dynamic dispatch) σε αντικείμενα κλάσεων με εικονικές συναρτήσεις στη C++;",
        "answers": [
            "Με σειριακή αναζήτηση κειμένου σε αρχεία πηγαίου κώδικα κατά την εκτέλεση",
            "Με αποστολή μηνυμάτων μέσω πρωτοκόλλου HTTP localhost",
            "Με επαναμεταγλώττιση ολόκληρου του προγράμματος σε κάθε κλήση μεθόδου",
            "Μέσω ενός κρυφού δείκτη (vptr) μέσα στο αντικείμενο που δείχνει στον πίνακα εικονικών μεθόδων (vtable)"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Κάθε πολυμορφικό αντικείμενο περιέχει έναν δείκτη `vptr` που παραπέμπει στον πίνακα `vtable` της κλάσης του, ο οποίος περιέχει δείκτες συναρτήσεων στις υλοποιήσεις των μεθόδων.",
        "funFacts": [
            "Η κλήση εικονικής μεθόδου εισάγει μια ελαφρά επιβάρυνση (indirection overhead) και μπορεί να εμποδίσει το inlining από τον μεταγλωττιστή.",
            "Αν μια κλάση περιέχει τουλάχιστον μία αμιγώς εικονική συνάρτηση (`= 0`), καθίσταται αφηρημένη (abstract) και δεν μπορεί να δημιουργηθεί στιγμιότυπό της."
        ],
        "source": "https://en.wikipedia.org/wiki/Virtual_method_table",
        "locale": "el-GR",
        "tags": ["cpp", "programming-languages", "vtable", "polymorphism"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_109",
        "text": "Ποιο είναι το θεμελιώδες πλεονέκτημα της διάταξης RAID 6 σε σχέση με το RAID 5 στην αποθήκευση δεδομένων;",
        "answers": [
            "Δεν απαιτεί καθόλου σκληρούς δίσκους",
            "Προσφέρει διπλάσια ταχύτητα εγγραφής από το RAID 0",
            "Χρησιμοποιεί διπλή ισοτιμία (dual parity), αντέχοντας την ταυτόχρονη απώλεια έως και δύο δίσκων χωρίς απώλεια δεδομένων",
            "Μπορεί να αποθηκεύσει απεριόριστα δεδομένα ανεξαρτήτως χωρητικότητας"
        ],
        "correctAnswerIndex": 2,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Το RAID 6 δημιουργεί δύο ανεξάρτητα μπλοκ ισοτιμίας (συνήθως ένα με XOR και ένα με κώδικα Reed-Solomon), επιτρέποντας πλήρη επιβίωση από αστοχία δύο μονάδων.",
        "funFacts": [
            "Απαιτεί τουλάχιστον τέσσερις φυσικούς δίσκους για να υλοποιηθεί.",
            "Είναι κρίσιμης σημασίας σε μεγάλες συστοιχίες δίσκων πολλών terabytes, όπου ο χρόνος ανακατασκευής (rebuild) είναι πολύωρος και ο κίνδυνος δεύτερης βλάβης αυξημένος."
        ],
        "source": "https://el.wikipedia.org/wiki/RAID#RAID_6",
        "locale": "el-GR",
        "tags": ["storage", "raid", "hardware", "fault-tolerance"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    },
    {
        "id": "tech_hard_110",
        "text": "Ποια κλασική δομή κατασκευής επαναληπτικού κατακερματισμού (hash construction) αποτελεί τη βάση των συναρτήσεων ασφαλούς κατακερματισμού SHA-1 και SHA-256;",
        "answers": [
            "Κατασκευή Sponge (Σπόγγου)",
            "Δέντρο Merkle-Patricia",
            "Αλγόριθμος Booth",
            "Κατασκευή Merkle-Damgård"
        ],
        "correctAnswerIndex": 3,
        "categoryId": "technology",
        "difficulty": 5,
        "explanation": "Η κατασκευή Merkle-Damgård χωρίζει το μήνυμα σε μπλοκ σταθερού μεγέθους και εφαρμόζει επαναληπτικά μια συνάρτηση συμπίεσης ενός δρόμου.",
        "funFacts": [
            "Ένα γνωστό μειονέκτημα της Merkle-Damgård είναι η ευπάθεια σε επιθέσεις επέκτασης μήκους (length-extension attacks) εάν δεν χρησιμοποιηθεί μηχανισμός HMAC.",
            "Αντίθετα, η νεότερη οικογένεια SHA-3 βασίζεται στην κατασκευή σπόγγου (Sponge construction / αλγόριθμος Keccak), που δεν επηρεάζεται από αυτές τις επιθέσεις."
        ],
        "source": "https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction",
        "locale": "el-GR",
        "tags": ["cryptography", "sha-256", "merkle-damgard", "hash-functions"],
        "status": "reviewed",
        "verifiedAt": "2026-10-25"
    }
]

if __name__ == "__main__":
    print(f"Total questions to append: {len(NEW_QUESTIONS)}")
    validate_and_append("technology", "hard", 5, NEW_QUESTIONS)

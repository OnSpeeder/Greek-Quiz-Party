# -*- coding: utf-8 -*-
import os
import random
import sys

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append

# Batch 4: tech_hard_361 to tech_hard_410 (50 questions)
raw_questions = [
    {
        "id": "tech_hard_361",
        "text": "Ποιο θεμελιώδες θεώρημα της κβαντικής μηχανικής, που διατυπώθηκε το 1982 από τους Wootters, Zurek και Dieks, απαγορεύει τη δημιουργία ακριβούς αντιγράφου μιας αυθαίρετης άγνωστης κβαντικής κατάστασης;",
        "correct": "Θεώρημα Μη-Κλωνοποίησης (No-Cloning Theorem)",
        "distractors": ["Αρχή της Απροσδιοριστίας", "Θεώρημα Bell", "Θεώρημα της Αποσυνοχής"],
        "explanation": "Το θεώρημα μη-κλωνοποίησης απορρέει άμεσα από τη γραμμικότητα των κβαντικών τελεστών και αποτελεί τον πυρήνα της ασφάλειας της κβαντικής κρυπτογραφίας, καθώς καθιστά αδύνατη την υποκλοπή χωρίς ανίχνευση.",
        "funFacts": [
            "Αποτέλεσε απάντηση σε μια πρόταση του Nick Herbert για κατασκευή διάταξης ταχύτερης από το φως (υπερφωτεινή επικοινωνία).",
            "Σημαίνει επίσης ότι στους κβαντικούς υπολογιστές δεν μπορεί να εφαρμοστεί κλασική εντολή 'αντιγραφής' (copy-paste) μεταβλητών μνήμης."
        ],
        "source": "https://en.wikipedia.org/wiki/No-cloning_theorem",
        "tags": ["technology", "quantum_computing", "physics", "no_cloning"]
    },
    {
        "id": "tech_hard_362",
        "text": "Ποια θεμελιώδης κβαντική πύλη ενός qubit μετατρέπει μια βασική κατάσταση |0> σε ισοπίθανη κβαντική υπέρθεση (|0> + |1>)/√2 και αντίστροφα;",
        "correct": "Πύλη Hadamard (H Gate)",
        "distractors": ["Πύλη Pauli-X", "Πύλη Phase (S)", "Πύλη T"],
        "explanation": "Η πύλη Hadamard είναι η βασικότερη πύλη δημιουργίας υπέρθεσης στους κβαντικούς υπολογιστές και εφαρμόζεται συνήθως σε όλα τα qubits στην έναρξη σχεδόν κάθε κβαντικού αλγορίθμου.",
        "funFacts": [
            "Πήρε το όνομά της από τον Γάλλο μαθηματικό Jacques Hadamard.",
            "Είναι αυτο-αντίστροφη: αν εφαρμοστεί δύο συνεχόμενες φορές στο ίδιο qubit, το επαναφέρει στην αρχική του κατάσταση (H * H = I)."
        ],
        "source": "https://en.wikipedia.org/wiki/Quantum_logic_gate#Hadamard_gate",
        "tags": ["technology", "quantum_computing", "quantum_gates", "hadamard"]
    },
    {
        "id": "tech_hard_363",
        "text": "Ποια καθολική κβαντική πύλη δύο qubits αναστρέφει την κατάσταση του δεύτερου qubit (target) εάν και μόνο εάν το πρώτο qubit (control) βρίσκεται στην κατάσταση |1>, επιτρέποντας τη δημιουργία κβαντικής διεμπλοκής;",
        "correct": "Πύλη CNOT (Controlled-NOT)",
        "distractors": ["Πύλη Toffoli", "Πύλη SWAP", "Πύλη Fredkin"],
        "explanation": "Η πύλη CNOT, σε συνδυασμό με την πύλη Hadamard, επιτρέπει τη δημιουργία των τεσσάρων διάσημων διεμπλεγμένων καταστάσεων Bell (Bell states).",
        "funFacts": [
            "Μαζί με οποιεσδήποτε πύλες περιστροφής ενός qubit, η CNOT σχηματίζει ένα πλήρες σύνολο καθολικών κβαντικών πυλών (universal quantum gate set).",
            "Αντιστοιχεί στην κλασική πύλη XOR, αλλά διατηρεί αυστηρά την αναστρεψιμότητα των κβαντικών καταστάσεων."
        ],
        "source": "https://en.wikipedia.org/wiki/Controlled_NOT_gate",
        "tags": ["technology", "quantum_computing", "cnot", "entanglement"]
    },
    {
        "id": "tech_hard_364",
        "text": "Ποιος κβαντικός αλγόριθμος, που ανακαλύφθηκε από τον Peter Shor το 1994, επιτρέπει την παραγοντοποίηση ακεραίων αριθμών σε πολυωνυμικό χρόνο O((log N)^3), απειλώντας την ασφάλεια των κλασικών κρυπτοσυστημάτων RSA και ECC;",
        "correct": "Αλγόριθμος του Shor (Shor's Algorithm)",
        "distractors": ["Αλγόριθμος του Grover", "Αλγόριθμος Deutsch-Jozsa", "Αλγόριθμος Simon"],
        "explanation": "Ο αλγόριθμος του Shor χρησιμοποιεί τον Κβαντικό Μετασχηματισμό Fourier (QFT) για να επιλύσει το πρόβλημα εύρεσης περιόδου συνάρτησης εκθετικά ταχύτερα από οποιονδήποτε γνωστό κλασικό αλγόριθμο.",
        "funFacts": [
            "Η δημοσίευση του αλγορίθμου το 1994 προκάλεσε επανάσταση και οδήγησε τις κυβερνήσεις παγκοσμίως να χρηματοδοτήσουν την έρευνα κβαντικών υπολογιστών.",
            "Για να σπάσει ένα κλειδί RSA-2048, εκτιμάται ότι απαιτείται ένας κβαντικός υπολογιστής με περίπου 4.000 λογικά (ή μερικά εκατομμύρια φυσικά) qubits."
        ],
        "source": "https://en.wikipedia.org/wiki/Shor%27s_algorithm",
        "tags": ["technology", "quantum_computing", "shors_algorithm", "cryptography"]
    },
    {
        "id": "tech_hard_365",
        "text": "Ποιος κβαντικός αλγόριθμος που επινόησε ο Lov Grover το 1996 προσφέρει τετραγωνική επιτάχυνση O(√N) για την αναζήτηση ενός στοιχείου μέσα σε μια μη δομημένη βάση δεδομένων N στοιχείων;",
        "correct": "Αλγόριθμος του Grover (Grover's Algorithm)",
        "distractors": ["Αλγόριθμος του Shor", "Αλγόριθμος QAOA", "Αλγόριθμος HHL"],
        "explanation": "Ενώ ένας κλασικός υπολογιστής χρειάζεται κατά μέσο όρο N/2 συγκρίσεις, ο αλγόριθμος του Grover χρησιμοποιεί διαδοχική ενίσχυση πλάτους πιθανότητας (amplitude amplification) βρίσκοντας το στοιχείο σε τάξη O(√N) βημάτων.",
        "funFacts": [
            "Λόγω του αλγορίθμου Grover, το αποτελεσματικό επίπεδο ασφάλειας συμμετρικών κρυπτοσυστημάτων (όπως το AES) υποδιπλασιάζεται, γι' αυτό το AES-256 θεωρείται απαραίτητο για μετα-κβαντική ασφάλεια.",
            "Έχει αποδειχθεί μαθηματικά ότι η τετραγωνική επιτάχυνση του Grover είναι το απόλυτο μέγιστο όριο για μη δομημένη αναζήτηση."
        ],
        "source": "https://en.wikipedia.org/wiki/Grover%27s_algorithm",
        "tags": ["technology", "quantum_computing", "grover", "algorithms"]
    },
    {
        "id": "tech_hard_366",
        "text": "Στη φυσική των qubits, ποιος δείκτης χρόνου μετρά τη διάρκεια χαλάρωσης (longitudinal relaxation time) κατά την οποία ένα qubit χάνει ενέργεια και καταπίπτει από τη διεγερμένη κατάσταση |1> στη βασική |0>;",
        "correct": "Χρόνος T1 (T1 Relaxation Time)",
        "distractors": ["Χρόνος T2 (Dephasing Time)", "Χρόνος coherence gate", "Χρόνος Ramsey"],
        "explanation": "Ο χρόνος T1 αντιπροσωπεύει τη θερμική χαλάρωση και απώλεια ενέργειας του συστήματος προς το περιβάλλον, θέτοντας ένα σκληρό ανώτατο όριο στο πόσο διάστημα μπορεί ένα qubit να διατηρήσει κβαντική πληροφορία.",
        "funFacts": [
            "Ο χρόνος T2 (χρόνος αποφασισμού ή dephasing) μετρά την απώλεια της κβαντικής φάσης και είναι πάντα μικρότερος ή ίσος με 2*T1.",
            "Στα υπεραγώγιμα qubits, η αύξηση των χρόνων T1 και T2 από μερικά νανοδευτερόλεπτα σε εκατοντάδες μικροδευτερόλεπτα αποτέλεσε τεράστιο τεχνολογικό άλμα δεκαετιών."
        ],
        "source": "https://en.wikipedia.org/wiki/Relaxation_(physics)#In_NMR_and_MRI",
        "tags": ["technology", "quantum_computing", "qubits", "physics"]
    },
    {
        "id": "tech_hard_367",
        "text": "Ποιος τύπος υπεραγώγιμου qubit, που αναπτύχθηκε στο Yale το 2007 από τους Michel Devoret, Rob Schoelkopf και Robert Koch, μείωσε δραστικά την ευαισθησία στον θόρυβο φορτίου συνδέοντας έναν πυκνωτή μεγάλου μεγέθους παράλληλα με επαφή Josephson;",
        "correct": "Transmon Qubit",
        "distractors": ["Flux Qubit", "Phase Qubit", "Charge Qubit (Cooper-pair box)"],
        "explanation": "Το transmon λειτουργεί στην περιοχή όπου η ενέργεια Josephson (Ej) είναι πολύ μεγαλύτερη από την ενέργεια φόρτισης (Ec), καθιστώντας τα ενεργειακά επίπεδα σχεδόν ανεπηρέαστα από τυχαίες διακυμάνσεις φορτίου.",
        "funFacts": [
            "Αποτελεί την τεχνολογία qubit που χρησιμοποιούν οι επεξεργαστές κβαντικών υπολογιστών της IBM, της Google (Sycamore) και της Rigetti.",
            "Λειτουργεί σε θερμοκρασίες κάτω από 15 millikelvin, ψυχρότερες ακόμη και από το βαθύ διάστημα, μέσα σε κρυοστάτες αραίωσης ηλίου."
        ],
        "source": "https://en.wikipedia.org/wiki/Transmon",
        "tags": ["technology", "quantum_computing", "transmon", "hardware"]
    },
    {
        "id": "tech_hard_368",
        "text": "Ποιο μήκος κύματος ηλεκτρομαγνητικής ακτινοβολίας χρησιμοποιείται στις υπερσύγχρονες μηχανές φωτολιθογραφίας EUV (Extreme Ultraviolet) της ASML για την κατασκευή τσιπ κάτω των 7 νανομέτρων;",
        "correct": "13,5 νανόμετρα (nm)",
        "distractors": ["193 νανόμετρα (nm)", "248 νανόμετρα (nm)", "4,5 νανόμετρα (nm)"],
        "explanation": "Η ακτινοβολία EUV παράγεται βομβαρδίζοντας μικροσκοπικά σταγονίδια λιωμένου κασσίτερου με πανίσχυρα λέιζερ CO2 50.000 φορές το δευτερόλεπτο, παράγοντας πλάσμα υψηλής θερμοκρασίας που εκπέμπει φως στα 13,5 nm.",
        "funFacts": [
            "Επειδή το φως των 13,5 nm απορροφάται σχεδόν από όλα τα υλικά, ακόμη και από τον αέρα, ολόκληρη η διαδικασία εκτελείται σε απόλυτο κενό χρησιμοποιώντας εξαιρετικά λεία κάτοπτρα πολλαπλών στρώσεων μολυβδαινίου-πυριτίου.",
            "Η ολλανδική εταιρεία ASML είναι η μοναδική εταιρεία στον κόσμο που κατέχει την τεχνογνωσία παραγωγής μηχανών EUV."
        ],
        "source": "https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography",
        "tags": ["technology", "semiconductors", "euv", "asml", "lithography"]
    },
    {
        "id": "tech_hard_369",
        "text": "Ποια πρωτοποριακή εξέλιξη στα συστήματα EUV εισήγαγε η ASML με τα μηχανήματα High-NA EUV (όπως το Twinscan EXE:5000), αυξάνοντας το αριθμητικό άνοιγμα του φακού από 0,33 σε ποια τιμή;",
        "correct": "0,55 NA",
        "distractors": ["0,45 NA", "0,85 NA", "1,20 NA"],
        "explanation": "Η αύξηση του αριθμητικού ανοίγματος (Numerical Aperture) σε 0,55 επιτρέπει την εκτύπωση γραμμών με ανάλυση κάτω των 8 νανομέτρων με ένα μόνο πέρασμα (single exposure).",
        "funFacts": [
            "Κάθε μηχάνημα High-NA EUV κοστίζει πάνω από 350 εκατομμύρια δολάρια και έχει μέγεθος διώροφου λεωφορείου.",
            "Η Intel ήταν ο πρώτος πελάτης παγκοσμίως που παρέλαβε και εγκατέστησε εμπορικό μηχάνημα High-NA EUV στα εργοστάσιά της στο Όρεγκον το 2024."
        ],
        "source": "https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography#High-NA_EUV",
        "tags": ["technology", "semiconductors", "high_na_euv", "asml", "intel"]
    },
    {
        "id": "tech_hard_370",
        "text": "Ποια αρχιτεκτονική τρανζίστορ 3D διαδέχθηκε τα FinFET στις προηγμένες λιθογραφίες (π.χ. TSMC N2, Samsung 3nm, Intel 20A), περιβάλλοντας πλήρως το κανάλι πυριτίου με πολλαπλά οριζόντια νανοφύλλα (nanosheets);",
        "correct": "Gate-All-Around FET (GAAFET / Nanosheet)",
        "distractors": ["Planar MOSFET", "Bipolar Junction Transistor", "Carbon Nanotube FET"],
        "explanation": "Στα GAAFETs, η πύλη αγκαλιάζει ολόκληρη την περίμετρο του καναλιού και από τις 4 πλευρές, εξαλείφοντας σχεδόν πλήρως τα ρεύματα διαρροής (leakage currents) και επιτρέποντας περαιτέρω σμίκρυνση της τάσης λειτουργίας.",
        "funFacts": [
            "Η Samsung ονόμασε τη δική της υλοποίηση MBCFET (Multi-Bridge-Channel FET), ενώ η Intel την ονόμασε RibbonFET.",
            "Επιτρέπει στους σχεδιαστές να προσαρμόζουν το πλάτος των νανοφύλλων για να επιτύχουν βέλτιστη ισορροπία μεταξύ υψηλής ταχύτητας και χαμηλής κατανάλωσης ενέργειας."
        ],
        "source": "https://en.wikipedia.org/wiki/Multigate_device#Gate-all-around_FET_(GAAFET)",
        "tags": ["technology", "semiconductors", "gaafet", "hardware", "transistors"]
    },
    {
        "id": "tech_hard_371",
        "text": "Ποια αρχιτεκτονική κατασκευής τσιπ μεταφέρει ολόκληρο το δίκτυο τροφοδοσίας ρεύματος στην πίσω πλευρά του πλακιδίου πυριτίου (wafer), απελευθερώνοντας την μπροστινή πλευρά αποκλειστικά για συνδέσεις σημάτων δεδομένων;",
        "correct": "Backside Power Delivery Network (BSPDN / PowerVia)",
        "distractors": ["Through-Silicon Vias (TSV)", "Flip-Chip Bumping", "Wire Bonding"],
        "explanation": "Το Backside Power Delivery (όπως το Intel PowerVia και το TSMC A16) μειώνει την πτώση τάσης IR drop, αποτρέπει παρεμβολές σημάτων και επιτρέπει υψηλότερη πυκνότητα κυκλωμάτων και συχνότητες λειτουργίας.",
        "funFacts": [
            "Απαιτεί το υπερβολικό τρόχισμα του πλακιδίου πυριτίου (wafer thinning) ώστε το πάχος του να μειωθεί σε ελάχιστα νανόμετρα πριν κατασκευαστούν οι πίσω αγωγοί.",
            "Θεωρείται μία από τις μεγαλύτερες επαναστάσεις στην αρχιτεκτονική ολοκληρωμένων κυκλωμάτων των τελευταίων 20 ετών."
        ],
        "source": "https://en.wikipedia.org/wiki/Integrated_circuit",
        "tags": ["technology", "semiconductors", "powervia", "bspdn", "hardware"]
    },
    {
        "id": "tech_hard_372",
        "text": "Ποιο υλικό υψηλής διηλεκτρικής σταθεράς (High-k Dielectric) εισήγαγε η Intel το 2007 στα τσιπ 45 νανομέτρων για να αντικαταστήσει το παραδοσιακό διοξείδιο του πυριτίου (SiO2) στην πύλη των τρανζίστορ;",
        "correct": "Οξείδιο του Αφνίου (HfO2 - Hafnium Oxide)",
        "distractors": ["Οξείδιο του Τιτανίου", "Οξείδιο του Αργιλίου", "Νιτρίδιο του Γαλλίου"],
        "explanation": "Καθώς το SiO2 έφτασε σε πάχος μόλις 1 νανομέτρου (5 ατόμων), τα κβαντικά φαινόμενα σήραγγας προκαλούσαν τεράστια διαρροή ρεύματος. Το οξείδιο του αφνίου επέτρεψε παχύτερο μονωτικό στρώμα με ισοδύναμη χωρητικότητα.",
        "funFacts": [
            "Ο Gordon Moore χαρακτήρισε τη χρήση High-k διηλεκτρικών βασισμένων στο άφνιο ως τη μεγαλύτερη αλλαγή στην τεχνολογία τρανζίστορ από τα τέλη της δεκαετίας του 1960.",
            "Συνδυάστηκε με μεταλλικές πύλες (Metal Gate), δημιουργώντας την τεχνολογία HKMG."
        ],
        "source": "https://en.wikipedia.org/wiki/High-k_dielectric",
        "tags": ["technology", "semiconductors", "hkmg", "intel", "materials"]
    },
    {
        "id": "tech_hard_373",
        "text": "Ποια υπολογιστική τεχνική λιθογραφίας (Computational Lithography) τροποποιεί σκόπιμα τα γεωμετρικά σχήματα πάνω στις φωτομάσκες (προσθέτοντας serifs και ακμές) για να αντισταθμίσει τα φαινόμενα περίθλασης του φωτός;",
        "correct": "Οπτική Διόρθωση Εγγύτητας (Optical Proximity Correction - OPC)",
        "distractors": ["Φωτοανθεκτική Εξάχνωση", "Χημική Μηχανική Στίλβωση (CMP)", "Απόθεση Ατομικού Στρώματος (ALD)"],
        "explanation": "Σε νανομετρικές κλίμακες, ένα τέλειο τετράγωνο στη μάσκα θα εκτυπωνόταν ως θολός κύκλος στο πυρίτιο. Το OPC παραμορφώνει προληπτικά το σχήμα στη μάσκα ώστε το φως να αποτυπώσει το επιθυμητό ορθογώνιο.",
        "funFacts": [
            "Οι αλγόριθμοι Inverse Lithography Technology (ILT) υπολογίζουν μαθηματικά την αντίστροφη διάδοση των κυμάτων φωτός χρησιμοποιώντας συστοιχίες GPUs.",
            "Τα αρχεία δεδομένων των σύγχρονων μασκών με OPC καταλαμβάνουν πολλά terabytes."
        ],
        "source": "https://en.wikipedia.org/wiki/Optical_proximity_correction",
        "tags": ["technology", "semiconductors", "opc", "lithography"]
    },
    {
        "id": "tech_hard_374",
        "text": "Ποια τεχνολογία δικτύωσης επιτρέπει σε έναν υπολογιστή να διαβάζει ή να γράφει απευθείας στην κύρια μνήμη RAM ενός άλλου απομακρυσμένου υπολογιστή χωρίς καμία συμμετοχή του λειτουργικού συστήματος ή της CPU;",
        "correct": "Remote Direct Memory Access (RDMA)",
        "distractors": ["Network File System (NFS)", "Direct Memory Access (DMA)", "Common Internet File System (CIFS)"],
        "explanation": "Το RDMA παρακάμπτει πλήρως το TCP stack και τον πυρήνα του λειτουργικού συστήματος (kernel bypass and zero-copy), επιτυγχάνοντας καθυστερήσεις υπο-μικροδευτερολέπτου (sub-microsecond latencies).",
        "funFacts": [
            "Αποτελεί την κινητήρια δύναμη πίσω από την εκπαίδευση μεγάλων γλωσσικών μοντέλων (LLMs) σε συστάδες χιλιάδων καρτών γραφικών Nvidia H100.",
            "Υλοποιείται σε περιβάλλοντα Ethernet μέσω του πρωτοκόλλου RoCE (RDMA over Converged Ethernet) ή μέσω εξειδικευμένου υλικού InfiniBand."
        ],
        "source": "https://en.wikipedia.org/wiki/Remote_direct_memory_access",
        "tags": ["technology", "networking", "rdma", "hpc", "hardware"]
    },
    {
        "id": "tech_hard_375",
        "text": "Ποια έκδοση του πρωτοκόλλου RoCE ενσωματώνει τα πακέτα RDMA μέσα σε datagrams UDP (θύρα 4791), επιτρέποντας δρομολόγηση Layer 3 σε διαφορετικά υποδίκτυα IP;",
        "correct": "RoCEv2 (Routable RoCE)",
        "distractors": ["RoCEv1", "InfiniBand Native", "iWARP"],
        "explanation": "Ενώ το αρχικό RoCEv1 περιοριζόταν αποκλειστικά στο ίδιο Layer 2 broadcast domain (μόνο με Ethernet frames), το RoCEv2 πρόσθεσε κεφαλίδα IP/UDP επιτρέποντας δρομολόγηση σε σύγχρονα hyperscale data centers.",
        "funFacts": [
            "Απαιτεί συνήθως υποστήριξη Priority Flow Control (PFC) και Explicit Congestion Notification (ECN) στους διακόπτες για να εξασφαλιστεί δίκτυο χωρίς απώλειες πακέτων (lossless Ethernet).",
            "Χρησιμοποιείται κατά κόρον από τη Microsoft στο Azure για την υποδομή AI."
        ],
        "source": "https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet",
        "tags": ["technology", "networking", "roce", "rdma", "datacenter"]
    },
    {
        "id": "tech_hard_376",
        "text": "Ποιο υποσύστημα ασύγχρονης εισόδου/εξόδου (Async I/O) εισήγαγε ο Jens Axboe στον πυρήνα Linux 5.1 το 2019, χρησιμοποιώντας δύο κοινόχρηστους κυκλικούς buffers (Submission Queue & Completion Queue) για ακραία ταχύτητα χωρίς system calls;",
        "correct": "io_uring",
        "distractors": ["epoll", "aio (POSIX AIO)", "kqueue"],
        "explanation": "Το io_uring επιτρέπει σε εφαρμογές χρήστη να υποβάλλουν αιτήματα I/O και να λαμβάνουν αποτελέσματα γράφοντας απευθείας σε memory-mapped ring buffers, μειώνοντας δραστικά το overhead των κλήσεων συστήματος.",
        "funFacts": [
            "Μπορεί να λειτουργήσει σε λειτουργία polling (IORING_SETUP_SQPOLL), όπου ένα νήμα πυρήνα διαβάζει συνεχώς τον buffer, επιτυγχάνοντας πλήρως zero-syscall λειτουργία.",
            "Βάσεις δεδομένων όπως το RocksDB και διακομιστές web έχουν δει πάνω από 100% αύξηση στο IOPS χάρη στο io_uring."
        ],
        "source": "https://en.wikipedia.org/wiki/Io_uring",
        "tags": ["technology", "operating_systems", "linux", "io_uring", "performance"]
    },
    {
        "id": "tech_hard_377",
        "text": "Ποιος δείκτης μέτρησης στα Solid-State Drives (SSDs) εκφράζει τον λόγο του πραγματικού όγκου δεδομένων που εγγράφονται στη μνήμη flash NAND προς τον όγκο δεδομένων που ζήτησε να γράψει το λειτουργικό σύστημα;",
        "correct": "Συντελεστής Ενίσχυσης Εγγραφής (Write Amplification Factor - WAF)",
        "distractors": ["Over-Provisioning Ratio", "Wear Leveling Index", "Flash Translation Overhead"],
        "explanation": "Επειδή οι SSDs μπορούν να διαγράψουν δεδομένα μόνο σε ολόκληρα blocks αλλά γράφουν σε pages, η αποκομιδή απορριμμάτων (garbage collection) αναγκάζει τον δίσκο να αντιγράφει ξανά έγκυρα pages, ανεβάζοντας το WAF πάνω από 1.0.",
        "funFacts": [
            "Ένα υψηλό WAF μειώνει δραματικά τη διάρκεια ζωής των NAND flash τσιπ και ρίχνει την ταχύτητα εγγραφής.",
            "Η εντολή TRIM και τεχνολογίες όπως τα Zoned Namespaces (ZNS) σχεδιάστηκαν ειδικά για να μειώσουν το WAF όσο το δυνατόν πιο κοντά στο 1.0."
        ],
        "source": "https://en.wikipedia.org/wiki/Write_amplification",
        "tags": ["technology", "hardware", "ssd", "waf", "storage"]
    },
    {
        "id": "tech_hard_378",
        "text": "Ποιο πρότυπο διεπαφής NVMe εξαλείφει την ανάγκη για Flash Translation Layer (FTL) στον δίσκο, απαιτώντας από το λειτουργικό σύστημα να γράφει δεδομένα αυστηρά σειριακά μέσα σε προκαθορισμένες ζώνες (zones);",
        "correct": "NVMe ZNS (Zoned Namespaces)",
        "distractors": ["NVMe-oF", "Open-Channel SSD", "DirectPath NVMe"],
        "explanation": "Τα ZNS ευθυγραμμίζουν τις εγγραφές της εφαρμογής απευθείας με τη φυσική γεωμετρία διαγραφής της flash μνήμης, εξαλείφοντας πλήρως την εσωτερική αποκομιδή απορριμμάτων του SSD και μειώνοντας το κόστος RAM.",
        "funFacts": [
            "Μειώνει το κόστος των SSDs σε επίπεδο hyperscale data centers μειώνοντας την ανάγκη για over-provisioning από 28% σε κάτω από 1%.",
            "Βασίζεται στις προδιαγραφές Zoned Block Commands (ZBC) και Zoned Device ATA (ZAC)."
        ],
        "source": "https://en.wikipedia.org/wiki/Zoned_storage",
        "tags": ["technology", "storage", "nvme", "zns", "hardware"]
    },
    {
        "id": "tech_hard_379",
        "text": "Ποιος μηχανισμός του πυρήνα Linux επεμβαίνει όταν η φυσική μνήμη RAM και το swap εξαντληθούν πλήρως, επιλέγοντας και τερματίζοντας βίαια διεργασίες βάσει μιας βαθμολογίας 'κακής συμπεριφοράς' (badness score);",
        "correct": "OOM Killer (Out-Of-Memory Killer)",
        "distractors": ["Kswapd", "Memory Compactor", "Page Reclaimer"],
        "explanation": "Ο OOM Killer υπολογίζει ένα σκορ για κάθε διεργασία με βάση το ποσοστό μνήμης που καταναλώνει και την τιμή oom_score_adj, στέλνοντας σήμα SIGKILL (kill -9) στην πιο δαπανηρή διεργασία για να σώσει το σύστημα από ολικό πάγωμα.",
        "funFacts": [
            "Μπορείτε να προστατέψετε μια κρίσιμη διεργασία (π.χ. sshd ή βάση δεδομένων) από τον OOM Killer ορίζοντας το /proc/[pid]/oom_score_adj σε -1000.",
            "Συχνά στοχεύει περιηγητές όπως ο Chrome ή βάσεις δεδομένων που χρησιμοποιούν πολύ RAM."
        ],
        "source": "https://en.wikipedia.org/wiki/Out_of_memory",
        "tags": ["technology", "operating_systems", "linux", "oom_killer", "memory"]
    },
    {
        "id": "tech_hard_380",
        "text": "Ποιο μέγεθος σελίδας μνήμης χρησιμοποιούν συνήθως τα Standard HugePages στην αρχιτεκτονική x86-64 για να μειώσουν τις αστοχίες TLB (TLB misses) σε εφαρμογές έντασης μνήμης όπως βάσεις δεδομένων;",
        "correct": "2 Megabytes (2 MB)",
        "distractors": ["64 Kilobytes (64 KB)", "16 Megabytes (16 MB)", "1 Gigabyte (1 GB) ως μόνη επιλογή"],
        "explanation": "Ενώ το προεπιλεγμένο μέγεθος σελίδας είναι 4 KB, οι σελίδες HugePages των 2 MB καλύπτουν 512 φορές περισσότερη μνήμη ανά καταχώριση στον buffer TLB, μειώνοντας δραστικά το κόστος μετάφρασης διευθύνσεων.",
        "funFacts": [
            "Η αρχιτεκτονική x86-64 υποστηρίζει επίσης HugePages μεγέθους 1 GB, τα οποία χρησιμοποιούνται σε υπερυπολογιστές και συστήματα virtualization.",
            "Τα Transparent Huge Pages (THP) του Linux προσπαθούν να συνενώσουν αυτόματα σελίδες 4KB σε 2MB στο παρασκήνιο."
        ],
        "source": "https://en.wikipedia.org/wiki/Page_(computer_memory)#Huge_pages",
        "tags": ["technology", "operating_systems", "memory", "hugepages", "linux"]
    },
    {
        "id": "tech_hard_381",
        "text": "Ποια θεμελιώδης υπόθεση στη διαχείριση μνήμης (Weak Generational Hypothesis) αποτελεί τη βάση για όλους τους σύγχρονους generational garbage collectors (όπως σε Java, .NET, V8);",
        "correct": "Η συντριπτική πλειονότητα των αντικειμένων πεθαίνει σχεδόν αμέσως μετά τη δημιουργία της",
        "distractors": [
            "Όλα τα αντικείμενα έχουν τον ίδιο χρόνο ζωής",
            "Τα μεγαλύτερα σε μέγεθος αντικείμενα πεθαίνουν γρηγορότερα",
            "Οι δείκτες αναφοράς κατευθύνονται πάντα από παλαιότερα προς νεότερα αντικείμενα"
        ],
        "explanation": "Παρατηρήθηκε εμπειρικά ότι πάνω από το 90-95% των αντικειμένων που δεσμεύονται σε ένα πρόγραμμα είναι προσωρινά (π.χ. μεταβλητές μέσα σε μεθόδους) και καθίστανται άχρηστα σε ελάχιστα χιλιοστά του δευτερολέπτου.",
        "funFacts": [
            "Αυτός είναι ο λόγος που η μνήμη χωρίζεται σε Young Generation (Eden) και Old Generation, επιτρέποντας ταχύτατες συλλογές μόνο στη νέα γενιά.",
            "Αν ένα αντικείμενο επιβιώσει από μερικούς κύκλους συλλογής, προάγεται στην παλιά γενιά (tenured)."
        ],
        "source": "https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)#Generational_GC",
        "tags": ["technology", "programming", "garbage_collection", "memory"]
    },
    {
        "id": "tech_hard_382",
        "text": "Ποιος μηχανισμός χρησιμοποιείται στους generational garbage collectors για να παρακολουθεί αναφορές δεικτών από παλαιότερα αντικείμενα (Old Gen) προς νεότερα (Young Gen) χωρίς να χρειάζεται σάρωση ολόκληρης της παλιάς γενιάς;",
        "correct": "Σημείωση Καρτών (Card Marking) και Remembered Sets",
        "distractors": ["Reference Counting", "Mark-Sweep Table", "Phantom References"],
        "explanation": "Η μνήμη της παλιάς γενιάς χωρίζεται σε 'κάρτες' (συνήθως 512 bytes). Όταν ένας δείκτης τροποποιείται μέσω ενός write barrier, η αντίστοιχη κάρτα σημειώνεται ως 'βρώμικη' (dirty) στον πίνακα καρτών (card table).",
        "funFacts": [
            "Ο write barrier που εκτελείται σε κάθε ανάθεση δείκτη απαιτεί συνήθως μόλις 2-3 εντολές assembly (π.χ. SHR και MOV byte).",
            "Χωρίς το card marking, κάθε μικρή συλλογή (minor GC) θα έπρεπε να διαβάσει ολόκληρη τη μνήμη gigabytes της παλιάς γενιάς."
        ],
        "source": "https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)#Generational_GC",
        "tags": ["technology", "programming", "garbage_collection", "jvm", "memory"]
    },
    {
        "id": "tech_hard_383",
        "text": "Ποιο καινοτόμο χαρακτηριστικό χρησιμοποιεί ο συλλέκτης απορριμμάτων ZGC (Z Garbage Collector) του Java Virtual Machine για να επιτυγχάνει παύσεις εκτέλεσης (STW) κάτω του 1 χιλιοστού του δευτερολέπτου σε terabytes μνήμης;",
        "correct": "Έγχρωμους δείκτες (Colored Pointers) και φράγματα φόρτωσης (Load Barriers)",
        "distractors": ["Αποκλειστικό Reference Counting", "Στατική κατανομή στοίβας", "Πλήρες πάγωμα νημάτων"],
        "explanation": "Ο ZGC αποθηκεύει μεταδεδομένα κατάστασης του αντικειμένου (π.χ. αν έχει μετακινηθεί ή μαρκαριστεί) απευθείας στα ανώτερα αχρησιμοποίητα bits των δεικτών 64-bit (colored pointers).",
        "funFacts": [
            "Όταν ένα νήμα εφαρμογής διαβάζει έναν δείκτη που δείχνει σε παλιά θέση, ο Load Barrier τον διορθώνει άμεσα 'στο φτερό' (self-healing pointer).",
            "Μπορεί να διαχειριστεί heaps μεγέθους έως και 16 Terabytes με χρόνο παύσης σταθερά κάτω από 1 ms."
        ],
        "source": "https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)",
        "tags": ["technology", "java", "zgc", "garbage_collection", "performance"]
    },
    {
        "id": "tech_hard_384",
        "text": "Ποια διάσημη ευπάθεια ασφαλείας υλικού (CVE-2017-5754) εκμεταλλεύτηκε το γεγονός ότι οι επεξεργαστές Intel εκτελούσαν εικαστικά εντολές ανάγνωσης μνήμης πυρήνα πριν ολοκληρωθεί ο έλεγχος δικαιωμάτων πρόσβασης;",
        "correct": "Meltdown",
        "distractors": ["Spectre", "Foreshadow", "Rowhammer"],
        "explanation": "Το Meltdown έσπασε το θεμελιώδες τείχος προστασίας μεταξύ εφαρμογών χρήστη και πυρήνα λειτουργικού συστήματος, επιτρέποντας σε οποιοδήποτε απλό πρόγραμμα να διαβάσει κωδικούς και κλειδιά από τη μνήμη του συστήματος.",
        "funFacts": [
            "Αποκαλύφθηκε ταυτόχρονα με το Spectre τον Ιανουάριο του 2018.",
            "Ονομάστηκε έτσι επειδή κυριολεκτικά 'έλιωσε' (melt down) τα όρια ασφαλείας που θεωρούνταν ακλόνητα επί δεκαετίες στο υλικό."
        ],
        "source": "https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)",
        "tags": ["technology", "security", "meltdown", "cpu", "hardware"]
    },
    {
        "id": "tech_hard_385",
        "text": "Ποιο φαινόμενο ασφαλείας σε μνήμες DRAM επιτρέπει την αλλοίωση περιεχομένου γειτονικών κελιών μνήμης (bit-flipping) μέσω συνεχούς και ταχύτατης ενεργοποίησης συγκεκριμένων γραμμών διευθύνσεων;",
        "correct": "Rowhammer",
        "distractors": ["Bit Rot", "Cosmic Ray Inversion", "Cold Boot Attack"],
        "explanation": "Λόγω της εξαιρετικά υψηλής πυκνότητας των σύγχρονων τσιπ DRAM, η επανειλημμένη φόρτιση μιας γραμμής διαρρέει ηλεκτρικό φορτίο σε γειτονικούς πυκνωτές, αλλάζοντας bits από 0 σε 1 ή αντίστροφα χωρίς άδεια εγγραφής.",
        "funFacts": [
            "Ανακαλύφθηκε το 2014 από ερευνητές του Carnegie Mellon και της Intel.",
            "Επιτρέπει σε μη προνομιούχες διεργασίες (ή ακόμη και JavaScript σε ιστοσελίδες) να αποκτήσουν δικαιώματα root μετατρέποντας κρίσιμα bits σε πίνακες σελίδων."
        ],
        "source": "https://en.wikipedia.org/wiki/Row_hammer",
        "tags": ["technology", "security", "rowhammer", "hardware", "dram"]
    },
    {
        "id": "tech_hard_386",
        "text": "Ποια ευπάθεια ασφαλείας επεξεργαστών Intel (CVE-2022-40982), γνωστή ως Gather Data Sampling, επέτρεψε τη διαρροή ευαίσθητων δεδομένων από άλλες διεργασίες μέσω της εντολής διανυσματικής συγκέντρωσης AVX Gather;",
        "correct": "Downfall",
        "distractors": ["Fallout", "ZombieLoad", "RIDL"],
        "explanation": "Το Downfall εκμεταλλεύεται τον κοινόχρηστο εσωτερικό καταχωρητή συγκέντρωσης δεδομένων (Vector Register File), ο οποίος αποκάλυπτε υπολείμματα δεδομένων προηγούμενων διεργασιών κατά την εκτέλεση εντολών AVX2/AVX-512.",
        "funFacts": [
            "Ανακαλύφθηκε από τον Daniel Moghimi της Google.",
            "Η επιδιόρθωση microcode της Intel μείωσε την απόδοση ορισμένων διανυσματικών υπολογισμών έως και 50%."
        ],
        "source": "https://en.wikipedia.org/wiki/Downfall_(security_vulnerability)",
        "tags": ["technology", "security", "downfall", "cpu", "intel"]
    },
    {
        "id": "tech_hard_387",
        "text": "Ποια ελλειπτική καμπύλη τύπου Montgomery, που σχεδίασε ο Daniel J. Bernstein το 2006, προσφέρει 128-bit ασφάλεια και εκτελείται εξ ορισμού σε σταθερό χρόνο προστατεύοντας από side-channel επιθέσεις;",
        "correct": "Curve25519 (X25519)",
        "distractors": ["secp256k1", "NIST P-256", "Brainpool P256"],
        "explanation": "Η καμπύλη Curve25519 ορίζεται πάνω από το πρώτο σώμα 2^255 - 19 και σχεδιάστηκε ειδικά για να αποφύγει τυχόν κερκόπορτες (backdoors) των προτύπων NIST και να υλοποιείται ταχύτατα χωρίς διακλαδώσεις εξαρτώμενες από δεδομένα.",
        "funFacts": [
            "Χρησιμοποιείται σχεδόν παντού σήμερα: στο πρωτόκολλο Noise, στο Signal, στο WhatsApp, στο WireGuard και στις συνδέσεις SSH/TLS.",
            "Ο αλγόριθμος ψηφιακής υπογραφής που βασίζεται στην ισοδύναμη καμπύλη Edwards ονομάζεται Ed25519."
        ],
        "source": "https://en.wikipedia.org/wiki/Curve25519",
        "tags": ["technology", "cryptography", "curve25519", "security"]
    },
    {
        "id": "tech_hard_388",
        "text": "Ποιος αλγόριθμος κρυπτογραφικής κατακερμάτισης κωδικών πρόσβασης (Password Hashing) κέρδισε το Password Hashing Competition το 2015 χάρη στην αντίστασή του σε επιθέσεις GPU/ASIC μέσω μνήμης (Memory-Hard Function);",
        "correct": "Argon2",
        "distractors": ["Bcrypt", "Scrypt", "PBKDF2"],
        "explanation": "Το Argon2 σχεδιάστηκε από τους Biryukov, Dinu και Khovratovich, παρέχοντας δύο κύριες παραλλαγές: το Argon2d (μέγιστη αντίσταση σε cracking με GPU) και το Argon2i (αντίσταση σε side-channel timing επιθέσεις).",
        "funFacts": [
            "Η υβριδική του μορφή Argon2id συνιστάται επισήμως από το IETF (RFC 9106) και το OWASP ως το ασφαλέστερο πρότυπο αποθήκευσης κωδικών.",
            "Αναγκάζει τον επιτιθέμενο να δεσμεύσει τεράστιες ποσότητες γρήγορης μνήμης RAM, εξουδετερώνοντας το πλεονέκτημα παραλληλισμού των ASIC miners."
        ],
        "source": "https://en.wikipedia.org/wiki/Argon2",
        "tags": ["technology", "cryptography", "argon2", "security"]
    },
    {
        "id": "tech_hard_389",
        "text": "Ποιο σύστημα κρυπτογραφικών υπογραφών που βασίζεται σε διγραμμικές απεικονίσεις (bilinear pairings) επιτρέπει τη συνένωση χιλιάδων υπογραφών από διαφορετικούς υπογράφοντες σε μία ενιαία συμπαγή υπογραφή σταθερού μεγέθους;",
        "correct": "Υπογραφές BLS (Boneh-Lynn-Shacham)",
        "distractors": ["Υπογραφές Schnorr", "Υπογραφές Lamport", "Υπογραφές RSA"],
        "explanation": "Οι υπογραφές BLS επιτρέπουν μη διαδραστική συγκέντρωση (non-interactive aggregation), όπου ένας επαληθευτής μπορεί να ελέγξει ότι χιλιάδες κόμβοι υπέγραψαν ένα μπλοκ κάνοντας έναν μόνο συγκεντρωτικό μαθηματικό έλεγχο.",
        "funFacts": [
            "Αποτελούν τη ραχοκοκαλιά του αλγορίθμου συναίνεσης Proof-of-Stake του Ethereum (Casper / Beacon Chain), επιτρέποντας σε εκατοντάδες χιλιάδες επικυρωτές να ψηφίζουν ταυτόχρονα.",
            "Επινοήθηκαν το 2001 από τους Dan Boneh, Ben Lynn και Hovav Shacham."
        ],
        "source": "https://en.wikipedia.org/wiki/BLS_digital_signature",
        "tags": ["technology", "cryptography", "bls", "signatures", "blockchain"]
    },
    {
        "id": "tech_hard_390",
        "text": "Ποιος μηχανισμός του πυρήνα Linux επιτρέπει τον περιορισμό των κλήσεων συστήματος (system calls) που επιτρέπεται να εκτελέσει μια διεργασία, χρησιμοποιώντας φίλτρα BPF για τη δημιουργία απομονωμένων sandboxes;",
        "correct": "Seccomp-BPF (Secure Computing Mode)",
        "distractors": ["AppArmor", "SELinux", "cgroups"],
        "explanation": "Το seccomp-BPF επιτρέπει σε ένα πρόγραμμα να δηλώσει ποιες ακριβώς syscalls επιτρέπονται και με ποια ορίσματα. Οποιαδήποτε άλλη κλήση τερματίζει ακαριαία τη διεργασία με σήμα SIGSYS.",
        "funFacts": [
            "Κάθε καρτέλα στον Google Chrome και κάθε container στο Docker χρησιμοποιεί αυστηρά φίλτρα seccomp για να περιορίσει την επιφάνεια επίθεσης στον πυρήνα.",
            "Αν ένας χάκερ εκτελέσει shellcode μέσα σε παραβιασμένο container, το seccomp αποτρέπει τη χρήση κλήσεων όπως reboot() ή ptrace()."
        ],
        "source": "https://en.wikipedia.org/wiki/Seccomp",
        "tags": ["technology", "operating_systems", "linux", "seccomp", "security"]
    },
    {
        "id": "tech_hard_391",
        "text": "Ποιες δύο βασικές τεχνολογίες του πυρήνα Linux συνδυάζονται για να καταστήσουν εφικτά τα Docker containers: η μία για την απομόνωση των πόρων (τι βλέπει η διεργασία) και η άλλη για τον περιορισμό χρήσης πόρων (πόσο καταναλώνει);",
        "correct": "Linux Namespaces και Control Groups (cgroups)",
        "distractors": ["Chroot και KVM", "eBPF και AppArmor", "OverlayFS και Seccomp"],
        "explanation": "Τα Namespaces (PID, Mount, Net, User κ.λπ.) παρέχουν την ψευδαίσθηση ότι η διεργασία τρέχει μόνη της σε ξεχωριστό μηχάνημα, ενώ τα cgroups περιορίζουν την ποσότητα CPU, RAM και I/O που επιτρέπεται να καταναλώσει.",
        "funFacts": [
            "Τα cgroups αναπτύχθηκαν αρχικά από μηχανικούς της Google το 2006 υπό το όνομα 'Process Containers' πριν ενσωματωθούν στον πυρήνα Linux.",
            "Τα containers δεν είναι εικονικές μηχανές: μοιράζονται τον ίδιο ακριβώς πυρήνα με το κεντρικό λειτουργικό σύστημα."
        ],
        "source": "https://en.wikipedia.org/wiki/Linux_namespaces",
        "tags": ["technology", "operating_systems", "linux", "docker", "containers"]
    },
    {
        "id": "tech_hard_392",
        "text": "Ποιο σύστημα αρχείων ένωσης (Union Mount Filesystem) χρησιμοποιείται κατά κόρον από το Docker για τη στοίβαξη των στρωμάτων εικόνας (image layers) σε ένα ενοποιημένο σημείο προσάρτησης;",
        "correct": "OverlayFS",
        "distractors": ["AUFS", "ZFS", "SquashFS"],
        "explanation": "Το OverlayFS συνδυάζει ένα ή περισσότερα στρώματα μόνο για ανάγνωση (lowerdir) με ένα τροποποιήσιμο στρώμα εγγραφής (upperdir), εμφανίζοντάς τα ως ενιαίο κατάλογο στο container.",
        "funFacts": [
            "Ενσωματώθηκε επίσημα στον πυρήνα Linux 3.18 το 2014, αντικαθιστώντας παλαιότερα εξωτερικά modules όπως το AUFS.",
            "Όταν ένα αρχείο τροποποιείται στο container, αντιγράφεται αυτόματα από το κάτω στρώμα στο πάνω στρώμα (copy-up operation)."
        ],
        "source": "https://en.wikipedia.org/wiki/OverlayFS",
        "tags": ["technology", "operating_systems", "overlayfs", "docker", "storage"]
    },
    {
        "id": "tech_hard_393",
        "text": "Πώς ονομάζεται η τεχνική μεταγλώττισης (όπως χρησιμοποιείται στη Rust και στην C++) κατά την οποία παράγεται ξεχωριστός, εξειδικευμένος κώδικας μηχανής για κάθε συγκεκριμένο τύπο δεδομένων που χρησιμοποιείται σε μια γενική συνάρτηση (generics);",
        "correct": "Μονομορφοποίηση (Monomorphization)",
        "distractors": ["Δυναμική Αποστολή (Dynamic Dispatch)", "Διαγραφή Τύπων (Type Erasure)", "Εικονική Πολυμορφία (Virtual Polymorphism)"],
        "explanation": "Η μονομορφοποίηση επιτρέπει μέγιστη ταχύτητα εκτέλεσης (μηδενικό κόστος runtime) και επιθετικές βελτιστοποιήσεις inlining, με τίμημα όμως μεγαλύτερο μέγεθος εκτελέσιμου αρχείου (code bloat) και πιο αργή μεταγλώττιση.",
        "funFacts": [
            "Σε αντίθεση με τη Rust και τη C++, η Java χρησιμοποιεί 'Type Erasure', αντικαθιστώντας όλους τους generic τύπους με Object και χρησιμοποιώντας type casts στο παρασκήνιο.",
            "Επιτρέπει στον μεταγλωττιστή να γνωρίζει το ακριβές μέγεθος μνήμης των δομών κατά τον χρόνο μεταγλώττισης."
        ],
        "source": "https://en.wikipedia.org/wiki/Monomorphization",
        "tags": ["technology", "compilers", "rust", "cpp", "generics"]
    },
    {
        "id": "tech_hard_394",
        "text": "Ποια διαμόρφωση σήματος (signal modulation) υιοθετήθηκε στο πρότυπο PCI Express 6.0, διπλασιάζοντας το bandwidth στα 64 GT/s κωδικοποιώντας 2 bits ανά κύκλο ρολογιού με 4 επίπεδα τάσης;",
        "correct": "PAM-4 (Pulse Amplitude Modulation 4-level)",
        "distractors": ["NRZ (Non-Return-to-Zero)", "QAM-16", "Manchester Encoding"],
        "explanation": "Σε αντίθεση με όλες τις προηγούμενες γενιές PCIe (1.0 έως 5.0) που χρησιμοποιούσαν δυαδική διαμόρφωση NRZ (2 επίπεδα), το PCIe 6.0 χρησιμοποιεί PAM-4 σε συνδυασμό με διόρθωση σφαλμάτων FEC (Forward Error Correction).",
        "funFacts": [
            "Το PAM-4 είναι πολύ πιο ευαίσθητο σε ηλεκτρικό θόρυβο, γι' αυτό και η προσθήκη Low-Latency FEC ήταν υποχρεωτική.",
            "Επιτρέπει σε μια υποδοχή PCIe 6.0 x16 να μεταφέρει έως και 256 GB/s αμφίδρομης διαμεταγωγής δεδομένων."
        ],
        "source": "https://en.wikipedia.org/wiki/PCI_Express#PCI_Express_6.0",
        "tags": ["technology", "hardware", "pcie", "pam4"]
    },
    {
        "id": "tech_hard_395",
        "text": "Ποιο ανοιχτό βιομηχανικό πρότυπο διασύνδεσης (βασισμένο στο φυσικό στρώμα του PCIe) επιτρέπει τη συνεκτική κοινή χρήση μνήμης (cache-coherent memory sharing) μεταξύ επεξεργαστών CPU, επιταχυντών GPU και επεκτάσεων μνήμης;",
        "correct": "Compute Express Link (CXL)",
        "distractors": ["InfiniBand", "Thunderbolt", "QuickPath Interconnect (QPI)"],
        "explanation": "Το CXL υποστηρίζει τρία πρωτόκολλα (CXL.io, CXL.cache, CXL.memory), επιτρέποντας σε εξωτερικές κάρτες και μνήμες να συμμετέχουν άμεσα στο πρωτόκολλο συνοχής κρυφής μνήμης του επεξεργαστή.",
        "funFacts": [
            "Επιτρέπει τη δημιουργία 'δεξαμενών μνήμης' (memory pooling) σε data centers, όπου διακομιστές δανείζονται δυναμικά RAM από κοινόχρηστες συστοιχίες.",
            "Υποστηρίζεται από όλους τους κολοσσούς της βιομηχανίας: Intel, AMD, ARM, Nvidia, Google, Microsoft και Meta."
        ],
        "source": "https://en.wikipedia.org/wiki/Compute_Express_Link",
        "tags": ["technology", "hardware", "cxl", "memory", "pcie"]
    },
    {
        "id": "tech_hard_396",
        "text": "Ποια τεχνολογία μνήμης DRAM στοιβάζει πολλαπλά στρώματα τσιπ πυριτίου κάθετα το ένα πάνω στο άλλο, συνδέοντάς τα μέσω χιλιάδων μικροσκοπικών διαμπερών οπών πυριτίου (TSVs) πάνω σε έναν παρεμβολέα (silicon interposer);",
        "correct": "High Bandwidth Memory (HBM)",
        "distractors": ["GDDR6X", "DDR5 ECC", "LPDDR5T"],
        "explanation": "Η HBM επιτυγχάνει τεράστιο εύρος διαύλου (1024 bits ανά στοίβα) και πρωτοφανείς ταχύτητες άνω των terabytes/sec, αποτελώντας αναντικατάστατο εξάρτημα σε AI επιταχυντές όπως οι Nvidia H100 και AMD MI300X.",
        "funFacts": [
            "Αναπτύχθηκε αρχικά από την SK Hynix και την AMD το 2013.",
            "Κάθε στοίβα HBM3e περιλαμβάνει έως και 12 ή 16 στρώματα DRAM κολλημένα με ακρίβεια νανομέτρου σε ένα chiplet."
        ],
        "source": "https://en.wikipedia.org/wiki/High_Bandwidth_Memory",
        "tags": ["technology", "hardware", "hbm", "memory", "ai"]
    },
    {
        "id": "tech_hard_397",
        "text": "Ποιο φυσικό φαινόμενο, που περιγράφηκε από τους Bennett et al. το 1993, επιτρέπει τη μεταφορά μιας άγνωστης κβαντικής κατάστασης σε έναν απομακρυσμένο προορισμό χρησιμοποιώντας κβαντική διεμπλοκή και δύο κλασικά bits πληροφορίας;",
        "correct": "Κβαντική Τηλεμεταφορά (Quantum Teleportation)",
        "distractors": ["Κβαντική Σήραγγα (Quantum Tunneling)", "Κβαντική Αποσυνοχή", "Κβαντικός Διακλαδισμός"],
        "explanation": "Η κβαντική τηλεμεταφορά δεν παραβιάζει το όριο ταχύτητας του φωτός ούτε το θεώρημα μη-κλωνοποίησης, καθώς η αρχική κατάσταση καταστρέφεται κατά τη μέτρηση Bell και η ανακατασκευή απαιτεί τη λήψη κλασικών bits.",
        "funFacts": [
            "Επαληθεύτηκε πειραματικά για πρώτη φορά το 1997 από την ομάδα του Anton Zeilinger στο Ίνσμπρουκ.",
            "Κινέζοι επιστήμονες πέτυχαν κβαντική τηλεμεταφορά φωτονίων από τη Γη σε τροχιακό δορυφόρο (Micius) σε απόσταση άνω των 1.400 χιλιομέτρων."
        ],
        "source": "https://en.wikipedia.org/wiki/Quantum_teleportation",
        "tags": ["technology", "quantum_computing", "physics", "teleportation"]
    },
    {
        "id": "tech_hard_398",
        "text": "Στο κλασικό πρόβλημα των Βυζαντινών Στρατηγών (Lamport, Shostak, Pease 1982), ποιο είναι το ελάχιστο συνολικό πλήθος στρατηγών N που απαιτείται αυστηρά για να επιτευχθεί συναίνεση παρουσία m προδοτών σε ασύγχρονο δίκτυο χωρίς ψηφιακές υπογραφές;",
        "correct": "N >= 3m + 1",
        "distractors": ["N >= 2m + 1", "N >= 4m + 1", "N >= m + 1"],
        "explanation": "Έχει αποδειχθεί μαθηματικά ότι εάν το ένα τρίτο ή περισσότεροι στρατηγοί είναι κακόβουλοι ή αποστέλλουν αντικρουόμενες εντολές, είναι αδύνατο για τους πιστούς στρατηγούς να καταλήξουν σε συμφωνία χωρίς κρυπτογραφικές αποδείξεις.",
        "funFacts": [
            "Αυτό σημαίνει ότι για να αντέξει ένα σύστημα 1 προδότη (m=1), απαιτούνται τουλάχιστον 4 κόμβοι.",
            "Αποτέλεσε τη θεμελιώδη μαθηματική πρόκληση που έλυσε το Bitcoin εισάγοντας τον μηχανισμό Proof-of-Work."
        ],
        "source": "https://en.wikipedia.org/wiki/Byzantine_fault",
        "tags": ["technology", "distributed_systems", "byzantine", "algorithms"]
    },
    {
        "id": "tech_hard_399",
        "text": "Ποιο σύστημα κρυπτογράφησης ροής (Stream Cipher), σχεδιασμένο από τον D. J. Bernstein, συνδυάζεται συνήθως με τον πιστοποιητή Poly1305 σχηματίζοντας έναν ταχύτατο αλγόριθμο αυθεντικοποιημένης κρυπτογράφησης (AEAD) χωρίς ευπάθεια σε χρονικές επιθέσεις;",
        "correct": "ChaCha20",
        "distractors": ["Salsa20", "RC4", "A5/1"],
        "explanation": "Το ChaCha20 είναι μια βελτιωμένη παραλλαγή του Salsa20 που χρησιμοποιεί έναν εσωτερικό πίνακα 16 λέξεων και πράξεις ARX (Add-Rotate-Xor), επιτυγχάνοντας εξαιρετική ταχύτητα σε επεξεργαστές κινητών τηλεφώνων που στερούνται επιτάχυνσης υλικού AES.",
        "funFacts": [
            "Η Google το υιοθέτησε το 2014 για όλες τις συνδέσεις HTTPS στο Chrome και στο Android.",
            "Αποτελεί τον κύριο αλγόριθμο κρυπτογράφησης στο πρωτόκολλο WireGuard VPN."
        ],
        "source": "https://en.wikipedia.org/wiki/ChaCha20-Poly1305",
        "tags": ["technology", "cryptography", "chacha20", "security"]
    },
    {
        "id": "tech_hard_400",
        "text": "Ποια είναι η λειτουργία του αλγορίθμου PageRank που δημιούργησαν οι Larry Page και Sergey Brin στο Stanford το 1996 για την κατάταξη ιστοσελίδων στη μηχανή αναζήτησης Google;",
        "correct": "Μοντελοποιεί έναν τυχαίο περιηγητή (Random Surfer) και υπολογίζει το κύριο ιδιοδιάνυσμα του στοχαστικού πίνακα μεταβάσεων του ιστού",
        "distractors": [
            "Μετρά αποκλειστικά τον αριθμό των φορών που εμφανίζονται οι λέξεις-κλειδιά στον τίτλο HTML",
            "Κατατάσσει τις ιστοσελίδες με βάση την ταχύτητα απόκρισης DNS του διακομιστή",
            "Υπολογίζει τη συντομότερη διαδρομή Dijkstra μεταξύ όλων των κόμβων του διαδικτύου"
        ],
        "explanation": "Το PageRank εκχωρεί μια αριθμητική βαρύτητα σε κάθε ιστοσελίδα θεωρώντας ότι ένας υπερσύνδεσμος λειτουργεί ως 'ψήφος εμπιστοσύνης', λαμβάνοντας υπόψη και έναν παράγοντα απόσβεσης (damping factor, συνήθως 0.85) για την πιθανότητα ο χρήστης να κάνει τυχαίο άλμα.",
        "funFacts": [
            "Το όνομα 'PageRank' είναι διπλό λογοπαίγνιο: αναφέρεται τόσο στις ιστοσελίδες (web pages) όσο και στο επώνυμο του συνιδρυτή Larry Page.",
            "Η αρχική πατέντα ανήκε στο Πανεπιστήμιο του Stanford, το οποίο έλαβε 1,8 εκατομμύρια μετοχές της Google σε αντάλλαγμα για την άδεια χρήσης."
        ],
        "source": "https://el.wikipedia.org/wiki/PageRank",
        "tags": ["technology", "google", "algorithms", "pagerank", "internet"]
    },
    {
        "id": "tech_hard_401",
        "text": "Ποιο θεμελιώδες πρόβλημα στη θεωρία υπολογισιμότητας, που απέδειξε ο Alan Turing το 1936, δηλώνει ότι είναι αδύνατο να υπάρξει γενικός αλγόριθμος που να αποφασίζει εάν ένα αυθαίρετο πρόγραμμα θα τερματίσει ή θα εκτελείται επ' άπειρον;",
        "correct": "Πρόβλημα Τερματισμού (Halting Problem)",
        "distractors": ["Πρόβλημα P vs NP", "Πρόβλημα Αντιστοιχίας Post", "Εικασία του Collatz"],
        "explanation": "Ο Turing απέδειξε μέσω διαγωνιοποίησης (diagonalization reductio ad absurdum) ότι αν υπήρχε τέτοιος αλγόριθμος, θα μπορούσε να κατασκευαστεί ένα πρόγραμμα που διαψεύδει την ίδια του την πρόβλεψη, οδηγώντας σε μαθηματικό παράδοξο.",
        "funFacts": [
            "Αποτέλεσε το πρώτο καταγεγραμμένο παράδειγμα 'μη αποφασίσιμου προβλήματος' (undecidable problem) στην ιστορία της επιστήμης υπολογιστών.",
            "Δημοσιεύτηκε στην ίδια ιστορική εργασία του 1936 όπου ο Turing εισήγαγε για πρώτη φορά την έννοια της Μηχανής Turing."
        ],
        "source": "https://el.wikipedia.org/wiki/%CE%A0%CF%81%CF%8C%CE%B2%CE%BB%CE%B7%CE%BC%CE%B1_%CF%84%CE%B5%CF%81%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%8D",
        "tags": ["technology", "computer_science", "turing", "halting_problem", "algorithms"]
    },
    {
        "id": "tech_hard_402",
        "text": "Ποιο θεώρημα της θεωρητικής πληροφορικής, που διατύπωσε ο Henry Gordon Rice το 1953, δηλώνει ότι οποιαδήποτε μη τετριμμένη σημασιολογική ιδιότητα της συμπεριφοράς ενός προγράμματος είναι γενικά μη αποφασίσιμη;",
        "correct": "Θεώρημα του Rice (Rice's Theorem)",
        "distractors": ["Θεώρημα Μη-Πληρότητας του Gödel", "Θεώρημα Cook-Levin", "Θεώρημα Master"],
        "explanation": "Το θεώρημα του Rice επεκτείνει το πρόβλημα τερματισμού, αποδεικνύοντας ότι είναι αδύνατο να γραφτεί ένα πρόγραμμα που να ελέγχει αυτόματα αν ένας αυθαίρετος κώδικας περιέχει ιούς, διαρροές μνήμης ή υπολογίζει μια συγκεκριμένη συνάρτηση.",
        "funFacts": [
            "Εξηγεί γιατί τα προγράμματα antivirus και οι στατικοί αναλυτές κώδικα αναγκαστικά καταφεύγουν σε προσεγγιστικές μεθόδους (heuristics), παράγοντας ψευδώς θετικά ή ψευδώς αρνητικά αποτελέσματα.",
            "Ισχύει για όλες τις Turing-complete γλώσσες προγραμματισμού."
        ],
        "source": "https://en.wikipedia.org/wiki/Rice%27s_theorem",
        "tags": ["technology", "computer_science", "theory", "rices_theorem"]
    },
    {
        "id": "tech_hard_403",
        "text": "Ποια κατηγορία υπολογιστικής πολυπλοκότητας περιλαμβάνει τα προβλήματα απόφασης για τα οποία μια προτεινόμενη λύση μπορεί να επαληθευτεί σε πολυωνυμικό χρόνο από μια ντετερμινιστική Μηχανή Turing;",
        "correct": "NP (Nondeterministic Polynomial time)",
        "distractors": ["P (Polynomial time)", "PSPACE", "EXPTIME"],
        "explanation": "Ενώ η κλάση P περιλαμβάνει προβλήματα που επιλύονται εύκολα σε πολυωνυμικό χρόνο, η κλάση NP περιλαμβάνει προβλήματα των οποίων η επαλήθευση της λύσης (πιστοποιητικό) είναι εύκολη, ακόμη κι αν η εύρεση της λύσης είναι δυσεπίλυτη.",
        "funFacts": [
            "Το ερώτημα εάν P = NP αποτελεί ένα από τα επτά Προβλήματα της Χιλιετίας του Ινστιτούτου Clay, με έπαθλο 1.000.000 δολαρίων για τη λύση του.",
            "Η συντριπτική πλειονότητα των επιστημόνων υπολογιστών πιστεύει ότι P ≠ NP."
        ],
        "source": "https://el.wikipedia.org/wiki/NP_(%CF%80%CE%BF%CE%BB%CF%85%CF%80%CE%BB%CE%BF%CE%BA%CF%8C%CF%84%CE%B7%CF%84%CE%B1)",
        "tags": ["technology", "computer_science", "complexity", "algorithms"]
    },
    {
        "id": "tech_hard_404",
        "text": "Ποιο θεώρημα, που αποδείχθηκε ανεξάρτητα από τους Stephen Cook (1971) και Leonid Levin (1973), απέδειξε ότι το πρόβλημα ικανοποιησιμότητας λογικών συναρτήσεων (Boolean SAT) είναι NP-πλήρες (NP-complete);",
        "correct": "Θεώρημα Cook-Levin",
        "distractors": ["Θεώρημα Turing", "Θεώρημα Karp", "Θεώρημα Shannon"],
        "explanation": "Το θεώρημα Cook-Levin απέδειξε ότι οποιοδήποτε πρόβλημα στην κλάση NP μπορεί να αναχθεί σε πολυωνυμικό χρόνο στο πρόβλημα Boolean SAT, καθιστώντας το SAT το πρώτο γνωστό NP-πλήρες πρόβλημα στην ιστορία.",
        "funFacts": [
            "Ο Richard Karp βασίστηκε σε αυτό το θεώρημα το 1972 για να αποδείξει ότι άλλα 21 διάσημα συνδυαστικά προβλήματα είναι επίσης NP-πλήρη (Karp's 21 NP-complete problems).",
            "Ο Stephen Cook τιμήθηκε με το βραβείο Turing το 1982 για αυτή τη θεμελιώδη ανακάλυψη."
        ],
        "source": "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem",
        "tags": ["technology", "computer_science", "cook_levin", "complexity", "algorithms"]
    },
    {
        "id": "tech_hard_405",
        "text": "Ποιο θεμελιώδες θεώρημα κατανεμημένων συστημάτων, που διατύπωσαν οι Fischer, Lynch και Paterson (FLP) το 1985, απέδειξε ότι είναι αδύνατο να επιτευχθεί ντετερμινιστική συναίνεση σε ένα ασύγχρονο δίκτυο ακόμη κι αν αποτύχει έστω και ένας μόνο κόμβος;",
        "correct": "Θεώρημα Αδυναμίας FLP (FLP Impossibility)",
        "distractors": ["Θεώρημα CAP", "Θεώρημα Paxos", "Θεώρημα Lamport"],
        "explanation": "Το αποτέλεσμα FLP αποδεικνύει ότι σε ένα καθαρά ασύγχρονο δίκτυο (όπου τα μηνύματα μπορούν να καθυστερήσουν επ' αόριστον), κανένας ντετερμινιστικός αλγόριθμος συναίνεσης δεν μπορεί να εγγυηθεί ταυτόχρονα ασφάλεια, ζωντάνια και ανοχή σε βλάβες.",
        "funFacts": [
            "Οι σύγχρονοι αλγόριθμοι συναίνεσης (όπως Paxos και Raft) παρακάμπτουν το όριο FLP κάνοντας υποθέσεις μερικής συγχρονικότητας (partial synchrony) χρησιμοποιώντας timeouts.",
            "Κέρδισε το βραβείο Dijkstra το 2001 για τη διαχρονική του επίδραση στην επιστήμη υπολογιστών."
        ],
        "source": "https://en.wikipedia.org/wiki/Fischer%E2%80%93Lynch%E2%80%93Paterson_impossibility_result",
        "tags": ["technology", "distributed_systems", "flp_impossibility", "consensus"]
    },
    {
        "id": "tech_hard_406",
        "text": "Ποιος αλγόριθμος δρομολόγησης κατάστασης συνδέσμου (Link-State) χρησιμοποιεί τον αλγόριθμο του Dijkstra και επιτρέπει ιεραρχική διαίρεση ενός δικτύου IP σε περιοχές (Areas), με την Area 0 να λειτουργεί ως κεντρικός κορμός (Backbone);",
        "correct": "Open Shortest Path First (OSPF)",
        "distractors": ["Routing Information Protocol (RIP)", "Border Gateway Protocol (BGP)", "Interior Gateway Routing Protocol (IGRP)"],
        "explanation": "Το OSPF είναι ένα πρωτόκολλο IGP (Interior Gateway Protocol) όπου κάθε δρομολογητής διατηρεί μια πλήρη τοπολογική βάση δεδομένων (LSDB) και υπολογίζει το συντομότερο δέντρο μονοπατιών προς κάθε προορισμό.",
        "funFacts": [
            "Αντικατέστησε το παλιό πρωτόκολλο RIP που περιοριζόταν σε μέγιστο όριο 15 αλμάτων (hop count).",
            "Όλες οι περιοχές σε ένα δίκτυο OSPF πρέπει υποχρεωτικά να συνδέονται φυσικά ή μέσω εικονικών συνδέσμων (virtual links) με την Backbone Area 0."
        ],
        "source": "https://el.wikipedia.org/wiki/OSPF",
        "tags": ["technology", "networking", "ospf", "routing"]
    },
    {
        "id": "tech_hard_407",
        "text": "Ποιος μηχανισμός του πρωτοκόλλου TCP (RFC 793) εισήχθη από τον John Nagle το 1984 για να αποτρέψει τη συμφόρηση του δικτύου από την αποστολή πληθώρας μικροσκοπικών πακέτων (small packet problem);",
        "correct": "Αλγόριθμος του Nagle (Nagle's Algorithm)",
        "distractors": ["Αλγόριθμος του Jacobson", "Αλγόριθμος Karn", "Αλγόριθμος Floyd"],
        "explanation": "Ο αλγόριθμος του Nagle συνενώνει μικρά εξερχόμενα μηνύματα και καθυστερεί την αποστολή τους μέχρι είτε να συμπληρωθεί ένα πλήρες πακέτο MSS είτε να ληφθεί ACK για το προηγούμενο πακέτο.",
        "funFacts": [
            "Σε δικτυακά παιχνίδια και εφαρμογές πραγματικού χρόνου απενεργοποιείται ρητά μέσω της επιλογής TCP_NODELAY για να εξαλειφθεί η καθυστέρηση (latency).",
            "Η ατυχής αλληλεπίδραση του αλγορίθμου Nagle με τον μηχανισμό Delayed ACK του TCP μπορεί να προσθέσει τεχνητή καθυστέρηση 200 έως 500 ms σε κάθε αίτημα."
        ],
        "source": "https://en.wikipedia.org/wiki/Nagle%27s_algorithm",
        "tags": ["technology", "networking", "tcp", "nagle", "algorithms"]
    },
    {
        "id": "tech_hard_408",
        "text": "Ποιος αλγόριθμος εκτίμησης χρόνου επιστροφής (RTT) και χρονικού ορίου αναμετάδοσης (RTO) στο TCP επιλύει την αμφισημία αναγνώρισης (retransmission ambiguity) αγνοώντας μετρήσεις RTT για πακέτα που χρειάστηκε να επανεκπεμφθούν;",
        "correct": "Αλγόριθμος του Karn (Karn's Algorithm)",
        "distractors": ["Αλγόριθμος του Nagle", "Αλγόριθμος Clark", "Αλγόριθμος Chandy"],
        "explanation": "Ο Phil Karn επινόησε τον αλγόριθμο το 1987 παρατηρώντας ότι αν ένα πακέτο σταλεί δύο φορές, ο αποστολέας δεν μπορεί να γνωρίζει αν το ACK που έλαβε αντιστοιχεί στην πρώτη ή στη δεύτερη εκπομπή.",
        "funFacts": [
            "Συνδυάζεται με εκθετική οπισθοχώρηση χρονομέτρου (timer backoff), διπλασιάζοντας το RTO σε κάθε αποτυχημένη επανεκπομπή.",
            "Αποτέλεσε σωτήρια βελτίωση που έσωσε το ARPANET/Internet από την επαπειλούμενη κατάρρευση συμφόρησης στα τέλη της δεκαετίας του 1980."
        ],
        "source": "https://en.wikipedia.org/wiki/Karn%27s_algorithm",
        "tags": ["technology", "networking", "tcp", "karns_algorithm"]
    },
    {
        "id": "tech_hard_409",
        "text": "Ποιο επίπεδο κανονικοποίησης σχεσιακών βάσεων δεδομένων (Boyce-Codd Normal Form - BCNF) αποτελεί μια αυστηρότερη παραλλαγή της Τρίτης Κανονικής Μορφής (3NF), απαιτώντας κάθε ορίζουσα (determinant) να είναι υποψήφιο κλειδί;",
        "correct": "Κανονική Μορφή Boyce-Codd (BCNF)",
        "distractors": ["Τέταρτη Κανονική Μορφή (4NF)", "Δεύτερη Κανονική Μορφή (2NF)", "Πέμπτη Κανονική Μορφή (5NF)"],
        "explanation": "Η BCNF επιλύει ανωμαλίες που εμφανίζονται στην 3NF όταν ένας πίνακας έχει πολλαπλά, αλληλεπικαλυπτόμενα υποψήφια σύνθετα κλειδιά, εξασφαλίζοντας ότι όλες οι συναρτησιακές εξαρτήσεις εξαρτώνται αποκλειστικά από υπερκλειδιά.",
        "funFacts": [
            "Διατυπώθηκε το 1974 από τους Raymond F. Boyce και Edgar F. Codd (τον εφευρέτη του σχεσιακού μοντέλου).",
            "Σε σπάνιες περιπτώσεις, η μετατροπή ενός πίνακα σε BCNF μπορεί να οδηγήσει σε απώλεια ορισμένων συναρτησιακών εξαρτήσεων (dependency preservation issue)."
        ],
        "source": "https://el.wikipedia.org/wiki/BCNF",
        "tags": ["technology", "databases", "bcnf", "normalization", "sql"]
    },
    {
        "id": "tech_hard_410",
        "text": "Ποιο θεώρημα βάσεων δεδομένων, που διατύπωσε ο Michael Stonebraker το 2011, υποστηρίζει ότι η εποχή της μιας ενιαίας παραδοσιακής σχεσιακής μηχανής (RDBMS) για όλες τις χρήσεις έχει παρέλθει οριστικά;",
        "correct": "'One Size Fits All' Is an Idea Whose Time Has Come and Gone",
        "distractors": ["Θεώρημα CAP", "Κανόνες του Codd", "Αρχή ACID"],
        "explanation": "Ο Michael Stonebraker (δημιουργός των Ingres, Postgres και Vertica) απέδειξε ότι εξειδικευμένες μηχανές αποθήκευσης (στήλης για analytics, μνήμης για OLTP, γράφων για σχέσεις) υπερτερούν κατά μία έως δύο τάξεις μεγέθους σε σχέση με γενικής χρήσης βάσεις.",
        "funFacts": [
            "Η εργασία αυτή άνοιξε τον δρόμο για τη σύγχρονη έκρηξη των NoSQL, NewSQL και Column-oriented βάσεων δεδομένων.",
            "Ο Stonebraker τιμήθηκε με το Βραβείο Turing το 2014 για τις θεμελιώδεις συνεισφορές του στην αρχιτεκτονική συστημάτων βάσεων δεδομένων."
        ],
        "source": "https://en.wikipedia.org/wiki/Michael_Stonebraker",
        "tags": ["technology", "databases", "stonebraker", "architecture", "data"]
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
    print(f"Loaded {len(questions)} questions for technology_hard batch 4 (361-410).")
    validate_and_append("technology", "hard", 5, questions)

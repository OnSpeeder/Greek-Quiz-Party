# Εξαγωγή QuizParty για Windows και Android

Οι εντολές εκτελούνται σε PowerShell από `C:\chatgpt_projects\QuizParty`.
Τα απλά exports είναι δοκιμαστικές εκδόσεις debug. Το `-Release` παράγει έκδοση
διανομής σε ξεχωριστό υποφάκελο `Release`, χωρίς να αντικαθιστά τα debug πακέτα.

## 1. Έλεγχος περιβάλλοντος

```powershell
Set-Location C:\chatgpt_projects\QuizParty
./scripts/doctor.ps1
./scripts/build.ps1
./scripts/test.ps1 -IncludeGodot
```

Το συγκεκριμένο repository χρησιμοποιεί Godot **4.7.2 .NET**, τα αντίστοιχα
**mono export templates** και το .NET SDK του `global.json` (10.0.401).
Windows/Core στοχεύουν .NET 8· το Android project στοχεύει .NET 9, όπως έχει ήδη
επαληθευτεί σε πραγματική συσκευή. Ο παραλήπτης του πακέτου δεν εγκαθιστά SDK.

Στον τρέχοντα υπολογιστή το Godot βρίσκεται στο `C:\Godot`. Σε νέο υπολογιστή
εγκατάστησε την ίδια έκδοση .NET και τα matching export templates από
**Editor → Manage Export Templates**. Για Android χρειάζονται JDK 17, Android SDK
και τα πακέτα που απαιτεί η συγκεκριμένη έκδοση Godot. Η επαληθευμένη τοπική
εγκατάσταση έχει Platform 36 και Build Tools 36.1.0. Ρύθμισε
**Editor Settings → Export → Android → Java SDK Path / Android SDK Path**.

## 2. Windows

Για δοκιμή:

```powershell
./scripts/export.ps1 -Platform Windows
```

Άνοιξε `artifacts\exports\Windows\QuizParty.exe`. Για να το στείλεις σε άλλον
υπολογιστή, συμπίεσε **όλον τον φάκελο του παιχνιδιού**: το `.exe`, το `.pck`
και τον φάκελο με τα συνοδευτικά αρχεία C#. Μην στείλεις μόνο το `.exe`.
Τα `*.log` είναι διαγνωστικά και δεν χρειάζονται στον παραλήπτη.

Για έκδοση διανομής:

```powershell
./scripts/export.ps1 -Platform Windows -Release
```

Το αποτέλεσμα βρίσκεται στο `artifacts\exports\Windows\Release\`.
Το υπάρχον preset είναι Windows x86_64. Η υπογραφή Windows δεν είναι ρυθμισμένη·
για υπογεγραμμένη διανομή χρειάζεται δικό σου πιστοποιητικό και ρύθμιση Code Sign
στο Windows export preset. Έλεγξε εκκίνηση και LAN παιχνίδι στο πακέτο που θα στείλεις.

## 3. Android για εγκατάσταση / δοκιμή

```powershell
./scripts/export.ps1 -Platform Android
```

Το APK βρίσκεται στο `artifacts\exports\Android\QuizParty.apk`.
Είναι ARM64, με package ID `org.quizparty.game` και debug υπογραφή.
Μετέφερέ το στο κινητό και επίτρεψε την εγκατάσταση για την εφαρμογή που το ανοίγει,
ή σύνδεσε εξουσιοδοτημένη συσκευή USB με USB debugging και εκτέλεσε:

```powershell
./scripts/android-install.ps1
```

Ο host και τα κινητά πρέπει να τρέχουν την ίδια έκδοση πρωτοκόλλου (τώρα 12) και να είναι
στο ίδιο LAN/Wi-Fi. Στα Windows επίτρεψε το παιχνίδι στο ιδιωτικό δίκτυο όταν
ζητηθεί πρόσβαση από το firewall.

## 4. Android release APK

1. Δημιούργησε **δικό σου release keystore**, έξω από το repository:

   ```powershell
   keytool -genkeypair -v -keystore C:\QuizPartySigning\quizparty.keystore -alias quizparty -keyalg RSA -keysize 2048 -validity 10000
   ```

   Ο φάκελος πρέπει να υπάρχει. Φύλαξε ασφαλές αντίγραφο του keystore και του
   κωδικού. Χρησιμοποίησε τον ίδιο κωδικό για store/key σύμφωνα με τις απαιτήσεις
   του Godot. Μην αποθηκεύσεις κωδικό σε script ή σε αρχείο του repository.

2. Όρισε στο τρέχον PowerShell τα στοιχεία υπογραφής:

   ```powershell
   $env:GODOT_ANDROID_KEYSTORE_RELEASE_PATH = 'C:\QuizPartySigning\quizparty.keystore'
   $env:GODOT_ANDROID_KEYSTORE_RELEASE_USER = 'quizparty'
   $quizPartySigningSecret = Read-Host 'Κωδικός keystore' -AsSecureString
   $env:GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD = [System.Net.NetworkCredential]::new('', $quizPartySigningSecret).Password
   try {
       ./scripts/export.ps1 -Platform Android -Release
   } finally {
       Remove-Item Env:GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD -ErrorAction SilentlyContinue
       $quizPartySigningSecret.Dispose()
   }
   ```

3. Το υπογεγραμμένο APK γράφεται στο `artifacts\exports\Android\Release\QuizParty.apk`.
   Το συγκεκριμένο release απαιτεί το δικό σου κλειδί και δεν έχει παραχθεί με
   πλαστό ή προσωρινό production κλειδί. Αν υπάρχει εγκατάσταση με διαφορετική
   υπογραφή, το Android δεν επιτρέπει ενημέρωση από πάνω· για δοκιμή μπορεί να
   χρειαστεί απεγκατάσταση της παλιάς debug έκδοσης, που διαγράφει τις τοπικές ρυθμίσεις.

## 5. Google Play / εξαγωγή μέσα από Godot

Άνοιξε `src\QuizParty.Godot\project.godot` με Godot .NET και επίλεξε
**Project → Export → Windows ή Android → Export Project**.
Για release απενεργοποίησε **Export With Debug**. Για Google Play το πακέτο είναι
**AAB**, όχι APK: στο Android preset όρισε **Gradle Build → Export Format → AAB**,
αύξησε **Version Code**, όρισε **Version Name** και εξήγαγε σε `.aab` με release
υπογραφή. Το παρόν script παράγει APK· η διαδρομή AAB γίνεται από τον editor.
Η υπογραφή, η καταχώριση Play Console και τα store/release acceptance gates
παραμένουν ξεχωριστά βήματα πριν από δημόσια κυκλοφορία.

Πηγές: [Godot Android export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html),
[Godot Windows export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_windows.html).
Το `docs/TOOLCHAIN_STATUS.md` καταγράφει τις ακριβείς εκδόσεις που έχουν δοκιμαστεί εδώ.

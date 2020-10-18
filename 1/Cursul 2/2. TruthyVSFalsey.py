# Atunci cand folosim un if, avem nevoie de valori booleene pentru a putea rula if-ul
# De aceea Python, face conversie la bool in ciuda faptului ca poate variabila noastra este una de tip string
# Exemplu:

am_mancat = "Da, am mancat"

# Daca afisam aceasta variabila, dupa ce am facut conversia la bool, am_mancat v-a fi True -> Asta inseamna Truthy

print(f"Variabila am_mancat string este: {am_mancat}")
print(f"Variabila am_mancat bool este: {bool(am_mancat)}")

# Falsey -> Daca variabila noastra este goala sau este 0, atunci vom avea fals

lucruri_facute_azi = "" # N-am facut nimic, deci las string-ul gol

print(f"Variabila lucruri_facute_azi string este: {lucruri_facute_azi}") # E un string gol
print(f"Variabila lucruri_facute_azi bool este: {bool(lucruri_facute_azi)}")

# De ce trebuie sa stim asta? Pt a scrie cod mai bun si mai aratos, ca si tine
# Exemplu
# Avem un formular de creare a unui utilizator. Acesta trebuie sa aiba un nume de cont si o parola

nume_cont = "andreea99"
parola = "feb1999"

if nume_cont and parola: # Daca nume_cont si parola exista atunci afisam ca s-a creat contul
    print("Cont creat cu succes!")
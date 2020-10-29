# Primul principiul al Programarii Orientate pe Obiecte
# Incapsularea
# Folosita pentru ca datele sa fie private de vederea altora rau voitori, pentru a nu avea acces la codul nostru

class Jucator:
    # Atribut comun tuturor claselor
    e_membru = True

    def __init__(self, nume, varsta):  # Constructor. Functie ce se apeleaza atunci cand cream un OBIECT de tipul astaa
            # nume si varsta sunt atributele unei clase
            self.varsta = varsta
            # Seteaza numele caracterului
            self.nume = nume

    def alearga(self):
        print("alearga")

    def tipa(self):
        print(f"{self.nume} tipa:AAAAAAAA")

# Principiu pentru a putea incapsula toate datele unei clase.
# Spre exemplu, un Jucator poate avea diferite campuri precum numele si varsta, dar poate si sa faca anumite actiuni: alearga, tipa

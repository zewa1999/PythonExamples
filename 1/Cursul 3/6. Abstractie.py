# Abilitatea de a oferi utilizatorului doar datele de care are nevoie
# Sa nu aiba acces la date ce sunt folosite doar de aplicatia noastra
# Al doilea principiu al POO

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

    def vorbeste(self):
        print(f"Numele meu este {self.nume} si am {self.varsta} ani")


jucator1 = Jucator("Andreea", 21)

# Utilizatorului ii va aparea doar datele de care are nevoie " Numele meu este Andreea si am 21 de ani"
# Nu-l intereseaza cum se ajunge acolo.
jucator1.vorbeste()
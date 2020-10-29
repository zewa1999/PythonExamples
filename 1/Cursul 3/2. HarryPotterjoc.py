# Programare orientata pe obiecte

# Cream clasa pentru retinerea unui caracter al unui jucator

class Jucator:
    # Atribut comun tuturor claselor
    e_membru = True

    def __init__(self, nume, varsta):  # Constructor. Functie ce se apeleaza atunci cand cream un OBIECT de tipul astaa

      if varsta >=18 and self.e_membru == True: # Daca jucatorul are cel putin 18 ani si e_membru e adevarat atunci cream caracterul
        # nume si varsta sunt atributele unei clase
        self.varsta = varsta
        # Seteaza numele caracterului
        self.nume = nume


    def alearga(self, unde_alearga):
        print(f"{self.nume} alearga catre {unde_alearga}!")

    def striga(self): # Trebuie sa trecem self ca si parametru
        print(f"Numele meu este {self.nume}")
       # print(f"Numele meu este {Jucator.nume}") # Nu merge intrucat nume nu este o variabila comuna tuturor obiectelor ci este doar in constructo



jucator1 = Jucator("Andrei", 20)
print(jucator1)  # Afiseaza unde se salveaza jucatorul
print(jucator1.nume, jucator1.varsta)  # Afiseaza numele jucatorului

jucator2 = Jucator("Andreea", 21)
print(jucator2)
print(jucator2.nume, jucator2.varsta)

print(jucator1.e_membru)

print(jucator2.e_membru) # True

jucator1.striga()
jucator2.striga()

jucator1.alearga(unde_alearga="Reghin")
jucator2.alearga("Brasov ")
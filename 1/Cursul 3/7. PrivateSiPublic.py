# Ce se intampla daca cineva vine si ne schimba o bucata din cod?
class Jucator:
    # Atribut comun tuturor claselor
    e_membru = True

    def __init__(self, nume, varsta):  # Constructor. Functie ce se apeleaza atunci cand cream un OBIECT de tipul astaa
            # nume si varsta sunt atributele unei clase
            self._varsta = varsta
            # Seteaza numele caracterului
            self._nume = nume

    def _alearga(self):
        print("alearga")

    def vorbeste(self):
        print(f"Numele meu este {self._nume} si am {self._varsta} ani")

# Exemplu:

juc1 = Jucator("Andrei", 20)
juc1.vorbeste = "ALAIII TATII"

print(juc1.vorbeste) # De ce se afiseaza ALAIII TATII??

# Nu prea e corect ce se intampla, nu-i asa?

# Fata de alte limbaje, Python nu ofera suport pentru variabile private
# Dar putem spune altor programatori ca variabila aceea nu trebuie schimbata
# Este un fel de conventie

juc2 = Jucator("Andreea", 21)

print(juc2.vorbeste())
juc2.vorbeste = "Tot nu merge"
print(juc2.vorbeste)

# Cum am zis, nu exista variabile private, dar putem oferi o idee ca variabila aceea este privata si nu ar trebui sa fie atinsa



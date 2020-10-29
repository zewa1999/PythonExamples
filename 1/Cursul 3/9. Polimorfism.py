# Al treile pricipiu al POO
# In jocul nostru, un utilizator poate fi ori Arcas ori Vrajitor
# Deci Vrajitorul si Arcasul trebuie si el sa se logheze
# Si nu dorim sa rescriem aceeasi functie pentru celelalte 2 clase
# De aceea folosim mostenirea
class Utilizator():
    # Nu cream o functie init daca nu vom avea nevoie sa instantam un obiect de acest tip
    def logare(self):
        print("Te-ai logat")

# Vrajitor si Arcas mai pot fi numite si subclase ale Utilizator sau clase derivate din Utilizator
class Vrajitor(Utilizator):  # Vrajitorul mosteneste un Utilizator
    def __init__(self, nume, putere):
        self.nume = nume
        self.putere = putere

    def ataca(self):
        # Folosind polimorfismul putem folosi si functia clasei de baza, ataca
        print(f"Ataca cu puterea {self.putere}")


class Arcas(Utilizator):  # Arcasul mosteneste un Utilizator
    def __init__(self, nume, numar_sageti):
        self.nume = nume
        self.numar_sageti = numar_sageti

    def ataca(self):
        self.numar_sageti -= 1
        if self.numar_sageti < 1:
            print("Numai ai sageti")
        else:
            print(f"Ataca cu sageti - Sageti ramase: {self.numar_sageti}")

# Cream un vrajitor si un arcas
vrajitor1 = Vrajitor("Merlin", "Frostbite")
arcas1 = Arcas("Gigel", 14)

def caracter_ataca(utilizator): # In functie de ce obiect primeste ca si parametru, v-a folosi functia ataca al obiectului respectiv
    utilizator.ataca()

caracter_ataca(vrajitor1)
caracter_ataca(arcas1)

for caracter in [vrajitor1, arcas1]:
    caracter.ataca() # inspectam obiectul si ne prezinta toate metodele si atributele obiectului
    
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


vrajitor1 = Vrajitor("Gandalf", "Bila de Foc")
# Practic am mostenit de la utilizator functionalitatea de logare
print(vrajitor1.logare())  # Vrajitorul s-a logat
vrajitor1.ataca()
arcas = Arcas("Robin Hood", 2)
print(arcas.logare())
print(f"Ai {arcas.numar_sageti} sageti")
arcas.ataca()
arcas.ataca()
arcas.ataca()

# Pentru a verifica daca tipul de date este unul pe care il cunoasteam, putem folosi functia isinstance

print(isinstance(vrajitor1, Vrajitor)) # vrajitor este un tip Vrajitor
print(isinstance(vrajitor1, Utilizator)) # vrajitor este un tip Utilizator pentru ca clasa Vrajitor este o subclasa a clasei Utilizator

# Totul din Python este bazat pe clasa object, deci:
print(isinstance(vrajitor1, object))
# object este un parinte a tuturor obiectelor existente
# putem observa asta intrucat:

[].__repr__()
Vrajitor.__repr__()

# Ambele clase, Vrajitor si lista au 2 functii care deja sunt existente


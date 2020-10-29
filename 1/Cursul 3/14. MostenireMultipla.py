class Utilizator():
    def logare(self):
        print("Te-ai logat")

class Vrajitor(Utilizator):
    def __init__(self, nume, putere):
        self.nume = nume
        self.putere = putere

    def ataca(self):
        print(f"Ataca cu puterea {self.putere}")


class Arcas(Utilizator):
    def __init__(self, nume, numar_sageti):
        self.nume = nume
        self.numar_sageti = numar_sageti

    def ataca(self):
        self.numar_sageti -= 1
        if self.numar_sageti < 1:
            print("Numai ai sageti")
        else:
            print(f"Ataca cu sageti - Sageti ramase: {self.numar_sageti}")

class Hibrid(Arcas, Vrajitor): # O clasa hibrida ce mosteneste si de la vrajitor cat si de la Arcas
    def __init__(self, nume, putere, numar_sageti):
        Arcas.__init__(self,nume, numar_sageti)
        Vrajitor.__init__(self,nume, putere)

vrajitor1 = Vrajitor("Gandalf", "Bila de Foc")
vrajitor1.ataca()
arcas = Arcas("Robin Hood", 2)
print(arcas.logare())
print(f"Ai {arcas.numar_sageti} sageti")
arcas.ataca()
arcas.ataca()
arcas.ataca()

hibrid1 = Hibrid("Helios", 70, 20)
print(hibrid1.logare())
print(hibrid1.numar_sageti)
print(hibrid1.putere)
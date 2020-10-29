# Folosirea constructorului clasei de baza pentru a nu fi nevoiti sa scriem de mai multe ori acelasi cod

class Utilizator:
    def __init__(self, nume, email):
        self.nume = nume
        self.email = email
        print("Constructor utilizator")

    def logare(self):
        print("Te-ai logat")

class Vrajitor(Utilizator):
    def __init__(self, nume, putere, email):
        super().__init__(nume, email)
        self.putere = putere

    def ataca(self):
        print(f"Ataca cu puterea {self.putere}")


class Arcas(Utilizator):  # Arcasul mosteneste un Utilizator
    def __init__(self, nume, numar_sageti, email):
        super().__init__(nume, email)
        self.numar_sageti = numar_sageti

    def ataca(self):
        self.numar_sageti -= 1
        if self.numar_sageti < 1:
            print("Numai ai sageti")
        else:
            print(f"Ataca cu sageti - Sageti ramase: {self.numar_sageti}")

# Cream un vrajitor si un arcas
vrajitor1 = Vrajitor("Merlin", "Frostbite", "email")
arcas1 = Arcas("Gigel", 14, "email")

def caracter_ataca(utilizator):
    utilizator.ataca()

caracter_ataca(vrajitor1)
caracter_ataca(arcas1)

for caracter in [vrajitor1, arcas1]:
    caracter.ataca()

# Introspecite - link-are la run time

print(dir(vrajitor1))
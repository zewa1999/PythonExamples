# Incep cu @
# adauga o functionalitate noua functie ce este declarata folosind un decorator
# @classmethod
# @staticmethod

# Putem salva o functie intr-o variabila

def salut():
    print("Saluttttttt")

buna = salut()

print(buna)

# Higher Order Function HOC
# O functie ce este de o ordine mai mare fata de cea de inauntrul ei
# Este o functie ce preia ca si parametru o functie sau returneaza o functie 
def salut1(functie):
    functie()

def salut2():
    def functie():
        return 5
    return functie()
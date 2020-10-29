class Jucator:
    # Atribut comun tuturor claselor
    e_membru = True

    def __init__(self, nume, varsta):  # Constructor. Functie ce se apeleaza atunci cand cream un OBIECT de tipul astaa
            # nume si varsta sunt atributele unei clase
            self.varsta = varsta
            # Seteaza numele caracterului
            self.nume = nume

    @classmethod  # Asta e un decorator ce specifica ca urmatoarea functie v-a fi o metoda
    def suma(cls, n1, n2): # Poate modifica anumite detalii din clasa existenta
        return cls("Andreea", n1 + n2)

    @staticmethod
    def suma2(n1, n2): # Nu poate modifica campuri sau functii din clasa in care au fost create
        return n1 + n2


# Functia suma o putem apela fara a fi nevoie de a crea un obiect de tipul jucator, ci folosind doar numele clasei in care se afla

# classmethod poate fi folosita si ca o metoda statica, dar poate crea si un obiect de tipul clasei respective
juc = Jucator.suma(3, 4)
print(juc.varsta)
print(Jucator.suma(1, 2))

# staticmethod nu e nevoita sa creeze un obiect pentru a putea accesa o functie din cadrul obiectului respectiv
# EXEMPLU:
print(Jucator.suma2(6,7))

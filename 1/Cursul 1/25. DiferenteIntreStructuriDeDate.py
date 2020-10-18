# Diferente intre dictionare si liste

# Daca dorim sa salvam o lista de oameni ce sunt angajati la magazinul nostru
# Si poate in viitor dorim sa ii sortam
# Ce ar trebui sa folosim, lista sau dictionarul?
# Diferenta majora intre lista si dictionar este ca lista POATE fi sortata, pe cand dictionarul nu

lista = [9,8,7,6,5,4,3,2,1]

dictionar = {
    "nr1": 6,
    "nr2": 5,
    "nr3": 4,
    "nr4": 3,
    "nr5": 2,
    "nr6": 1,

}

# Exista o metoda de sortare la lista, dar la dictionar nu exista

lista.sort()
#dictionar.sort()

# Cand folosim un dictionar?
# Sa spunem ca avem o platforma de tipul facebook, si fiecare utilizator are mai multe atribute
# Are nume, prenume, data de nastere, si alte lucruri
# Aici este o metoda buna de a folosi un dictionar, intrucat datele acelea nu avem nevoie sa fie in ordine
# Exemplu:

utilizator = {
    "Nume":"Berar",
    "Prenume":"Andreea Marioara",
    "Data Nastere":"01-Februarie-1999"
}
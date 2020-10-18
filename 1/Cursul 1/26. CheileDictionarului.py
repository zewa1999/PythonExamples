# Un dictionar poate fi format din mai multe chei si valori
# O valoare nu poate exista fara o cheie

dictionar = {
    "cheie" : "valoare"
}

# Practic cheia este elementul cu care accesam valoarea

# Dar o cheie poate fi doar de tipul string?
# Hai sa vedem

dictionar2 = {
    1 : "valoare",
    True : "alta valoare"#,
    #[1,2,3] : "lista" # Nu merge
}

# De ce nu merge oare lista ca si o cheie?
# Deoarece o cheie poate fi doar o variabila ce are proprietatea ca nu se poate schimba!!!
# De aceea putem folosi, numere intregi, stringuri sau valori booleene


# Ce se intampla daca avem doua chei identice?
# Exemplu:

dictionar3 = {
    1 : True,
    1: False
}

print(dictionar3[1])

# Se afiseaza False! Pentru ca o data ce scriem aceeasi cheie intr-un dictionar, valoarea de inainte, care in cazul nostru era True
# Se va modifica si va deveni ultima gasita in dictionar, care e False


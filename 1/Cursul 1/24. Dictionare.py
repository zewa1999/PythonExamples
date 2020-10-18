# Un tip de date ce are la baza o structura de date

dictionar = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "Andreea e isteata si invata pitonul" : 56789
}

# Ne putem da seama ca este un dictionar daca:
# 1. Are acolade, nu paranteze patrate ca si la liste
# 2. In loc de index, ca la liste, putem accesa o valoare folosind un string
# Exemplu: Cream o lista pentru o intelegere mai buna

lista = [1,2,3,4]

# Pentru a afisa elementul de pe pozitia 0 din lista folosim astfel

print(lista[0])

# Dar in dictionar, putem accesa folosind string-ul

print(dictionar["a"])

# Smecher, nu?

# Daca afisam o valoare ce nu exista ne arunca o exceptie, adica ne afiseaza eroare

#print(dictionar["e"])

# Un DICTIONAR este o structura de date neordonata Listele merg in mod liniar de la indexul 0 pana la ultimul index
# Un dictionar poate avea ca si cheie, adica string, orice valoare
# Exemplu:
print(dictionar["Andreea e isteata si invata pitonul"])

# Putem avea structuri de date in structuri de date
# Spre exemplu daca avem o platforma gen facebook, un utilizator are o lista de prieteni ce fiecare poate si-a setat anumite informatii si altii nu

prieteni_utilizator = [
    {
        "Nume":"Gigel",
        "Prenume":"Marcel",
        "Data Nastere":"19-Aprilie-2001"
    },
{
        "Nume":"Andrei",
        "Prenume":"Costache",
        "Data Nastere":"26-Iunie-2009"
    }

]

# Putem afisa valori dintr-o structura de genul de mai sus?
# Da, putem. Incearca sa si intelegi

# Afisam date din interiorul dictionarului de la indexul 0 din lista de dictionare
# Practic avem elementul de la indexul 0 si dupa afisam lista elementului de la indexul 0
print(prieteni_utilizator[0]["Nume"])
print(prieteni_utilizator[1]["Prenume"])


# Putem afisa si dictionarul
print(dictionar)
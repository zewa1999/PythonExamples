lista1 = [1, 2, 3]
lista2 = [10, 20, 30]

lista_de_perechi = list(zip(lista1, lista2))
print(lista_de_perechi)

tuple1 = (4, 5, 6)
tuple2 = [40, 50, 60]

lista_de_perechi2 = list(zip(tuple1, tuple2))
print(lista_de_perechi2)

dict1 = {
    "nume" : "Andrei",
    "varsta" : 20,
    "Hobby" : "Programare"
}

dict2 = {
    "nume" : "Andreea",
    "varsta" : 21
}

lista_de_dictionare = list(zip(dict1.values(), dict2.values())) # Face tuple-uri din valorile dictionarului
print(lista_de_dictionare) # Daca nu exista element in ambele structuri de date, nu se face un tuple doar cu unul singur

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

lista_de_set = list(zip(set1, set2))
print(lista_de_set)

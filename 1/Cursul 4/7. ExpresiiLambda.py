# functii anonime ce nu avem nevoie de mai multe ori de ele

# lambda parametrul1, parametrul2, parametrul3, etc: actiune(parametru)

# Nu e nevoie sa cream o intreaga functie noua
# EXEMPLU:

# Metoda I

from functools import reduce

def inmultire_cu_2(el):
    return el*2

print(list(map(inmultire_cu_2, [1, 2, 3])))

# Metoda Lambda

print(list(map(lambda item1: item1*2, [1, 2, 3])))

print(reduce(lambda acc, item: acc + item , [1,2,3], 0))


# Exercitiu: Creati o functie lambda si folositi-o pentru a ridica la patrat fiecare element dintr-o lista

lista = [9,8,7,6,5,4,3,2,1]

lista_patrat = list(map(lambda item: item*item, lista))

print(lista_patrat)

# Exercitiu: Sortati o lista de tuple-uri bazandu-va pe elementul secundar din tuple

lista_tuple = [ (9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4)]

lista_tuple.sort(key= lambda el: el[1])
print(lista_tuple)
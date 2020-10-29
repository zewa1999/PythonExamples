from functools import reduce
lista = [1, 2, 3]

def inmultire_cu_doi(item):
    return item*2

def doar_impar(item):
    return item % 2 !=0

def suma(acc, item):
    print(acc, item)
    return acc + item

print(reduce(suma, lista, 0 ))

# reduce e folosit pentru aplicarea unei functii pe care o dorim noi pentru a face diferite operatii pe o multime
# mai sus facem suma intregii liste. Suma la inceput are valoarea 0

lista2 = [24, 15, 9]

def diferenta(acc, item):
    return acc - item

print("Rezultatul va fi 1: 49 - 24 - 15- 9 = 1 ")
print(reduce(diferenta, lista2, 49))


# Crearea unui map folosind functia reduce

# Nu prea vrea sa-mi iasa
# lista_noua = []
# lista_veche = [1, 2, 3]
#
# def map_functie(acc, item):
#     return acc * item
#
#
# for i in lista_veche:
#     lista_noua.append(reduce(map_functie, lista_veche, 1 ))
#
# print(lista_noua)
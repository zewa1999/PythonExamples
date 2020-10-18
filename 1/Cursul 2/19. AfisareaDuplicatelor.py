# Afisati duplicatele din lista data
# Duplicatele sa fie salvate intr-o lista si dupa sa fie afisate parcurgand lista

lista = [2, 2, 3, 4, 5, 6, 7, 7, 8, 8]

duplicate = []
for nr in lista:
    if lista.count(nr) > 1:
        if nr not in duplicate:
            duplicate.append(nr)

print(duplicate)

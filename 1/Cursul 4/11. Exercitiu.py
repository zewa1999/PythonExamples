# Folosind Comprehension afisati duplicatele dintr-o lista

lista = ['1', '4', '7', '3', '2', '1', '9', '13', '21', '4', '6']

# Solutie
duplicate = set([nr for nr in lista
             if lista.count(nr) > 1])
print(duplicate)

# Folosim setul pentru a nu avea elemente duplicate dupa ce le am adaugat
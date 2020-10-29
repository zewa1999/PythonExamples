# La fel ca la liste

lista2 = { char for char in "salutt" }

set_nr = {nr for nr in range(0, 10)}
print(set_nr)


set_putere = {nr ** 2 for nr in range(0, 10)}
print(set_putere)

set_pare = {nr for nr in range(0, 50)
            if nr % 2 == 0}
print(set_pare)
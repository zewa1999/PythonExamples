# Break are rolul de a opri din rulare o structura repetitiva de tipul for sau while

# Ni se cere sa afisam raspunsul unei ecuatii foarte grele. Ni se da o ecuatie si dupa o lista de raspunsuri.
# Noi trebuie sa afisam raspunsul corect din lista respectiva

ecuatie = "f(x) = 3x+2, undex x = 4" # -> f(4) = 14

lista_raspunsuri = [6, 19, 4, 14, 27, 31]

# Iteram prin lista si cautam raspunsul corect
# Facem o varianta prin for si una prin while

# 1. For

for raspuns in lista_raspunsuri:
    if raspuns == 14:
        print(f"Raspunsul este {raspuns}")
        break

# Cand gasim raspunsul 14 ne oprim, intrucat nu mai are rost sa verificam si celelalte raspunsuri de dupa, aici ne ajuta break, opreste verificarile urmatoare

# 2. While

i =0
while i < len(lista_raspunsuri):
    if lista_raspunsuri[i] == 14:
        print(f"Raspunsul este {lista_raspunsuri[i]}")
        break
    i+=1

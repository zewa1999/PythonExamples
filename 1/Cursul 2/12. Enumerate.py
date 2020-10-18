# Afisam un tuple format din indexul si elementul de la indexul repectiv
for element in enumerate([4,2,1,5,6,3,9]):
    print(element)

# Cum se afiseaza un tuple, il putem despacheta

for index, caracter in enumerate([4,2,1,5,6,3,9]):
    print(f"Index: {index} Caracter: {caracter}")

# Exercitiu: Creati o lista cu 100 de elemente si afisati elementul cu indexul 50

for element in enumerate(range(5423, 5523)):
    if element[0] == 50:
        print(f'Elementul cu indexul 50 este: {element[1]}')

# Tema pentru tine, fa acelasi lucru, numai ca trebuie sa despachetezi tuple-ul
                                # ---------------------------------------------------------------------------------------------------------------------#
# De cele mai multe ori, o imagine poate fi reprezentata folosind o matrice
# De aceea acum vom avea un exercitiu
# Trebuie sa se parcurga matricea si pentru fiecare element din matrice trebuiesc facute urmatoarele:
# Daca elementul este 0 afisati ' '
# Daca elementul este 1 afisati *

pictura = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for imagine in pictura:  # O imagine este o lista din pictura
    for pixel in imagine:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Un cod bun si acceptat trebuie sa aiba mai multe calitati:
# 1. Curat
# 2. Lizibil si usor de citit -> Nume bune la variabile, comentarii
# 3. Predictibil. Codul trebuie sa fie predictibil
# 4. DRY -> DO NOT REPEAT YOURSELF. Nu te repeta!
# 5. Codul trebuie sa fie modular. Bazat pe functii!!
# Putem lua codul de la aplicatia de inainte si sa facem o diferenta intre el si
# cateva modificari care il pot aduce la o valoare mai buna prin folosirea bunelor practici mentionate mai sus

# Cod inainte de modificari

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


 # Cod dupa de modificari
# Modularitate, daca doream sa afisam steluta de mai multe ori in cod, trebuia sa modificam peste tot unde apare steluta
# Asa putem sa punem un nume general si chiar putem folosi alte caractere in loc de steluta, modificand doar intr-un singur loc

plin = '&'
gol = ' '
for imagine in pictura:  # O imagine este o lista din pictura
    for pixel in imagine:
        if pixel: # Este o variabila Truthy, deci nu-i nevoie sa vedem ca e egala cu 1
            print(plin, end='')
        else:
            print(gol, end='')
    print()
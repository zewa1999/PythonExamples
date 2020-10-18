# Prin intermediul range putem sa ii spunem la for de unde pana unde sa itereze
for numar in range(0, 10):
    print(numar)

print('\n')
for numar in range(4, 10):
    print(numar)

# Daca dorim ca for-ul nostru sa mearga din 2 in 2 sau din 5 in 5 sau etc, mai putem sa punem un al 3 lea parametru la range

print('\n')
for nr in range(0,100,5): # Merge din 5 in 5 de la 0 la 99
    print(nr)

print('\n')
for nr in range(10,0,-1): # Merge de la 10 la 1 si scade cate 1
    print(nr)

print('\n')
for _ in range(2): # Afisam 2 liste cu range de la 0 la 10
    print(list(range(10)))
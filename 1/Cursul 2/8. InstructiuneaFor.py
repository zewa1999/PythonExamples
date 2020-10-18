# Instructiunea repetitiva for

# for element in multime_iterabila

for litera in "Andreea e iubita mea":
    print(litera)
print('\n')
for numar in [1,2,3,4,4,5,6]:
    print(numar)
print('\n')

for numar_set in {7,8,9,10,11}:
    print(numar_set)
print('\n')

for numar_tuple in (12,13,14,15):
    print(numar_tuple)
print('\n')

for element in[16,17,18,19]: # Pentru fiecare element se ia x-urile pe rand. Ruleaza ca sa vezi cum merge
    for x in ['a', 'n', 'd', 'r', 'e', 'e', 'a']:
        print(element, x)
    print('\n') # La sfarsitul fiecarui al 2 lea for cu litere, se lasa o linie libera

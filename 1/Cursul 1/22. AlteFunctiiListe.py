litere = ["x", "c", "d", "a", "z", "y"]

# Sortam literele
litere.sort()

# Intoarcem lista
litere.reverse()

# Afisam lista in sens invers
# Daca dorim doar sa vedem lista in sens invers, putem s-o afisam in sens invers
print(litere[ : : -1])

# Crearea unei liste cu valori date intr-un interval dorit
# Folosim functia range() ce pe romaneste inseamna interval
# In functie de ce ii punem inainte de functia range, python va crea tipul acela de variabila
# Spre exemplu daca dorim sa facem o lista de la 1 la 99 vom avea list(range(1,100))

lista_intamplare = list(range(1,100))
print(lista_intamplare)


# Lista la intamplare de la 0 la 100

lista_intamplare = list(range(100))
print(lista_intamplare)


# Crearea unui string folosind o lista

propozitie = ' '.join(["Buna", "numele", "meu", "este", "Andrei"])
print(propozitie)
# Variabila propozitie este creat dintr-o lista de string-uri. Intre fiecare string se pune caracterul de inainte de .join, care la noi este un spatiu
# Daca punem un semn al exclamarii ce se va afisa?

propozitie = '!'.join(["Buna", "numele", "meu", "este", "Andrei"])
print(propozitie)
#Dupa fiecare string se va pune un semn al exclamarii



# Despachetarea listelor - Am facut si la variabile doar ca aici e mult mai necesar

a, b, c = [1,2,3]
print(f"Variabila a este: {a}")
print(f"Variabila b este: {b}")
print(f"Variabila c este: {c}")

# Daca dorim sa luam doar anumite variabile elemente din lista, dar nu vrem sa facem variabile pt fiecare

a, b, c, *alte_numere = [1,2,3,4,5,6,7,8,9]

print(f"\nVariabila a este: {a}")
print(f"Variabila b este: {b}")
print(f"Variabila c este: {c}")
print(f"Restul numerelor sunt salvate in lista {alte_numere}")

# Poate dorim sa salvam ultimul sau penultimul numar intr-o variabila si nu intr-o lista
a, b, c, *alte_numere, penultimul, ultimul = [1,2,3,4,5,6,7,8,9]

print(f"\nVariabila a este: {a}")
print(f"Variabila b este: {b}")
print(f"Variabila c este: {c}")
print(f"Penultima cifra este: {penultimul}")
print(f"Ultima cifra este: {ultimul}")
print(f"Restul numerelor sunt salvate in lista {alte_numere}")

# Exercitiu
# Refaceti secventa de cod de mai jos pentru a se afisa lista sortata de prieteni

prieteni = ['Anca', 'Ioana', 'Andreea', 'Andrei', 'Anton', 'Florin']

prieten_nou = ['Elena']

print(prieteni.sort() + prieten_nou)

# Sunt mai multe metode de a rezolva exercitiul asta
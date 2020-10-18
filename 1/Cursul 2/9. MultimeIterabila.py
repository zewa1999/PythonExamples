# O multime iterabila este o multime prin care putem trece unul cate unul si putem face ceva cu elementul din multimea respectiva
# Multimile iterabile sunt: Liste, Dictionare, Set-uri, Tuple-uri, String-uri
# O iteratie este actiunea de a trece de la un element la altu

# Cum iteram printr-un dictionar?

utilizator = {
    "nume" : "Andrei",
    "varsta" : 20,
    "poate_inota" : False
}

for element in utilizator: # Imi afiseaza cheile
    print(element)

# Dictionarul are 3 metode de a il parcurge:

#1. items - parcurge si cheia si valoarea

for element in utilizator.items(): # Returneaza un tuple
    print(element)
print('\n')

#2. keys - parcurge cheile

for cheie in utilizator.keys():
    print(cheie)
print('\n')


#3. values - parcurge valorile

for valoare in utilizator.values():
    print(valoare)
print('\n')

# Ce se intampla daca dorim sa afisam cheia si valoarea separat sau sa le retinem intr-o variabila separat?

for element in utilizator.items():
    cheie = element[0]
    valoare = element[1]
    print(f"Cheia: {cheie}  Valoare: {valoare}")
print('\n')

# O metoda de scriere mai usoara este daca facem despachetarea tuple-ului

for cheie, valoare in utilizator.items(): # Mult mai simpla si mai rapid de scris
    print(f"Cheia: {cheie}  Valoare: {valoare}")
print('\n')

# Ce se afiseaza in urma secventei urmatoare de cod?

for e in 50: # Eroare, 50 este de tipul int si NU este o multime iterabila
    print(e)
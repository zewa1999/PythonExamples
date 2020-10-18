# Tuple-urile sunt niste liste ce nu pot fi modificate
# Spre deosebire de liste unde se folosesc [] si dictionar unde se folosesc {}, la tuple uri se folosesc ()

tupleul_meu = (1, 2, 3, 4, 5, 5, 5)
#tupleul_meu[0] = 6 # Nu merge intrucat tuple-urile nu pot fi modificate

print(tupleul_meu[2]) # Afiseaza elementul de la indexul 2

print(5 in tupleul_meu) # Exista 5 in tupleul_meu -> True

# Sunt mai rapide fata de liste
# Dar nu se poate modifica, sorta, sa intoarcem de la sfarsit

print(tupleul_meu)

# Deoarece nu se pot modifica, acestea pot fi folosite ca si chei in dictionare
# Exemplu

dictionar = {
    ("Tuple",2) : "Acesta este un tuple"
}

# Afisam valoarea cheii ("Tuple",2)

print(dictionar[("Tuple",2)])
# Putem face aproape aceleasi operatii ca si la liste

tuple_nou = tupleul_meu[0:]
print(tuple_nou)

x, y, z, *altele = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(altele)

# Functii

# Afiseaza de cate ori a gasit valoarea data ca si parametru
print(tupleul_meu.count(5))

# Afiseaza indexul unde a gasit prima data valorarea data ca si parametru

print(tupleul_meu.index(5))
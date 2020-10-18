# Simularea unui quiz

# Practici de folosit cand codam in Python

# Numirea variabilelor folosind tipul snake_case: Toate literele sunt mici si cuvintele despartite cu underline sau underscore. EX:

iq_andreea = 190
iq_andrei = 190

# Pot avea in componenta: litere, numere sau underscore. EX:

iq_andreea2 = 185
iq_andrei2 = 185

_iq_andreea3_ = 187

# Variabilele sunt diferentiate in functie de nume. Daca sunt 2 variabile cu acelasi nume, dar chiar si cu un caracter diferit, atunci sunt variabile diferite. EX:

iq_andreea_4 = 195
iq_Andreea_4 = 196

print("iq_andreea_4: " + str(iq_andreea_4) + " iq_Andreea_4: " + str(iq_Andreea_4))

# constantele in LITERE MARI

PI = 3.14

# Nu folosim 2 underscore unul dupa altul cand cream o variabila

__varsta__mos__costache = 20  # Am 20 de ani dar nu trebuie sa numim asa variabilele ci cum e mai jos
_varsta_mos_costache = 20 # sau
varsta_mos_costache = 20

# Putem initializa variabile si asa - Se numeste despachetare

a, b, c, d = 1, 2, 3, "Andreea e superba" # isi da singur seama ce tip de variabila e si cum sa le initializeze in functie de virgula

print(a)
print(b)
print(c)
print(d)
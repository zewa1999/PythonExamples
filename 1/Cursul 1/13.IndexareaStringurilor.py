#Avem urmatorul string sau sir de caractere pe romaneste

secventa_de_numere = "0123456789"

# Pe noi ne intereseaza sa afisam doar o parte a acelui sir de caractere, sa spunem numarul de pe prima pozitie si cel de pe ultima

print(f"Numarul de pe prima pozitie este {secventa_de_numere[0]} si cel de pe ultima este {secventa_de_numere[9]}")

# Mai exista si alte functionalitati precum:

# Putem avea mai multe lucruri intre parantezele patrate: [start:stop:nr_pasi_de_sariti]

# Aratam in urmatoarele exemple cum putem folosi notatia de mai sus

print(secventa_de_numere[0:3]) # Afisam numerele de la indexul 0 la indexul 3
print(secventa_de_numere[1:6]) # Afisam numerele de la indexul 1 la indexul 6
print(secventa_de_numere[0:9:2]) # Afisam din 2 in 2 caracterele dintre indexul 0 la indexul 9


#Daca nu scriem una dintre valori, avem o valoare implicita care este 0 pentru start, ultimul numar de index pt stop si 1 la nr_pasi_sariti

print(secventa_de_numere[ : 5]) # Afisam de la 0 la 5
print(secventa_de_numere[ : : ]) # Afisam toate numerele de la 0 la 9 cu cate un pas

# Ce am scris mai sus putem scrie si astfel
print(secventa_de_numere[0 : 10 : 1])

# Daca indexul dat este cu minus, atunci inseamna ca se refera de la sfarsit, de asta se afiseaza 9... Stiu e ciudat, dar nu stiu cum sa explic mai bine, poate daca arat pe o foaie
print(secventa_de_numere[-1])

# Daca dorim sa afisam in ordine inversa
print(secventa_de_numere[ : : -1]) # Se afiseaza de la caracterul cu indexul 0 la caracterul cu indexul 10 in ordine inversa, adica cate unul
# Cum indexul va scadea si nu va creste, inseamna ca se va afisa caractere de la sfarsit


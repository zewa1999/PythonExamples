# Se creeaza la fel ca si dictionarul, numai ca nu avem chei si valori ci doar valori
# Este o multime de elemente neordonata si cu elemente unice, nu pot exista duplicate

set1 = {1, 2, 3, 4, 5, 5, 5, 5, } # Daca rulam, o sa avem 5 doar o singura data
print(set1)
# Daca incercam sa adaugam elemente noi in setul nostru si acesta se repeta cu unul deja existent, acel element nu se va adauga

set1.add(2)
set1.add(100)
print(set1)

# Exercitiu: Daca avem spre exemplu o lista cu elemente si dorim sa stergem duplicatele din ea, cum facem?

lista_mea = [5,12,5,9,2,7,6,2,3]

# Putem crea un set pe baza listei noastre

setul_meu = set(lista_mea) # Practic facem o conversie. Cum facem conversie de la int la string, asa facem si de la lista la set

print(setul_meu)

# Structura asta de date este foarte importanta
# Spre exemplu sa ne gandim ca pe platforma noastra de socializare nu pot exista persoane cu acelasi numar de telefon
# Putem salva fiecare numar de telefon al persoanei si atunci cand adaugam unul ce deja exista ii dam o eroare utilizatorului
# Spunandu-i ca acest numar de telefon deja exista si sa adauge altul nou

# Intrucat setul este o multime neordonata, nu putem accesa elementele folosind indexul
# Exemplu:

#print(setul_meu[3]) #-> Eroare

#Putem vedea daca elementul se afla in set astfel:

print(5 in setul_meu) # -> True pentru ca 5 se afla in setul_meu

# Putem obtine si lungimea setului

print(len(setul_meu))


# De altfel, daca dorim, putem face conversie de la un set la o lista

lista_mea2 = list(setul_meu)
lista_mea2.append(2) # Adaug pe 2 in lista
print(lista_mea2)

# Putem copia si setul

set_nou = setul_meu.copy()


# Stergerea elementelor dintr-un set

setul_meu.clear()
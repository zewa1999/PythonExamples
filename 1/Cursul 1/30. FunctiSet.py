# De decomentat daca doresti sa vezi ce fac functiile
setul_meu = {1, 2, 3, 4, 5}
setul_tau = {4, 5, 6, 7, 8, 8, 9}

# Diferenta dintre setul_meu si setul_tau. Ce se afla in setul meu si nu se afla in setul tau. Returneaza un nou set
# set_nou = setul_meu.difference(setul_tau)
# print(set_nou)

# Stergerea unui element daca exista in set
# setul_meu.discard(5)
# print(setul_meu)

# Sterge toate elementele din set CARE nu se regasesc in ambele seturi si afiseaza setul ramas. Modificarile le face pe setul actual
# setul_meu.difference_update(setul_tau)
# print(setul_meu)

# Intersectia
# print(setul_meu.intersection(setul_tau))
# Putem scrie si asa
# print(setul_meu & setul_tau)

# Nu exista elemente comune in set. Daca exista se returneaza False, daca nu exista se returneaza True
# print(setul_meu.isdisjoint(setul_tau)) #-> False

# Reuniunea seturilor
# print(setul_meu.union(setul_tau))
# Putem scrie si astfel
# print(setul_meu | setul_tau


# Includere setul_meu este inclus in setul_tau

# print(setul_meu.issubset(setul_tau)) #->False

# Includere, setul_tau are elementele din setul_meu

# print(setul_meu.issuperset(setul_tau)) #->False

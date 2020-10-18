# Ce se afiseaza in urmat liniilor de cod de mai jos?

print(True == 1) # 1 se converteste la bool si devine True
print('' == 1) # se convertesc ambele la bool, '' este Falsey si 1 este Truthy
print([] == 1) # [] este Falsey, intrucat o lista goala este Falsey si 1 este True
print(10 == 10.0) # 10 se converteste la float si va deveni 10.0, deci sunt egale si respectiv adevarate
print([] == []) # Falsey este egal cu  Falsey deci este Truthy

# Daca punem in loc de == is e vreo diferenta?

print(True is 1) # False -> True este 1? NU -> True este doar True
print('' is 1) # False -> '' este 1? NU -> '' este doar ''
print([] is 1) # False -> O lista este la fel ca si 1? -> NU
print(10 is 10.0) # False -> 10 este la fel ca 10.0?

lista1 = []
lista2 = []
print(lista1 is lista2) # False -> lista1 este lista 2? -> NU
print(lista1 == lista2) # Adevarat, valorile din lista sunt la fel.
# Diferenta intre cele 2 este:
# == cauta egalitatea intre cele 2 valori
# is cauta sa vada daca locatia in memorie este aceeasi la ambele
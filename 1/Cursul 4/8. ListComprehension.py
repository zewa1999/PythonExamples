# Metoda mai rapida de creare a unei liste
lista1 = []

for char in "salutt":
    lista1.append(char)

print(lista1)

lista2 = [ char for char in "salutt" ]
# char este o variabila creata
# pentru fiecare char din string-ul "salutt" adauga in lista la sfarsit
# o metoda mai scurta dar si mai rapida de a face asta

lista_nr = [ nr for nr in range(0, 10)]
print(lista_nr)

# Ridicarea la putere a elementelor dintr-un range folosind comprehension

lista_putere = [nr**2 for nr in range(0, 10)]
print(lista_putere)

# Creaza o lista cu elementele pare intre 0 si 49
lista_pare = [nr for nr in range(0,50)
              if nr % 2 ==0]
print(lista_pare)
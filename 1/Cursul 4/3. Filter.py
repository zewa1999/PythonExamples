# Filter filtreaza diferite obiecte pentru noi

lista_mea = [5, 8, 10, 9]
def impar(item):
    return item%2==1 # restul impartirii lui 2 este 1? Daca da se returneaza True, altfel se returneaza False

lista_mea = list(filter(impar, lista_mea))
print(lista_mea) # Se afiseaza doar 5 si 9 pt ca doar alea sunt impare

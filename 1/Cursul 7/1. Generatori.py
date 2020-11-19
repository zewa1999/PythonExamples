# pentru a face o multime iterabila, trebuie sa implementam metoda __iter__
# generatorii sunt iterabili
# range este un generator
def creaza_lista(num):
    result = []
    for i in range(num):
        result.append(i *2)
    return result

lista_mea = creaza_lista(100)
print(lista_mea)
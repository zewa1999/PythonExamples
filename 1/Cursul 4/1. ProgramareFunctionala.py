# Bazata pe functii
# Separarea datelor primite de program si logicii acestuia
# Logica se face folosind functii pure
# Outpul-ul trebuie sa fie la fel ca input-ul
# Functia nu trebuie sa aiba efecte secundare

def inmultire_cu_2(lista):
    lista_noua =[]
    for i in lista:
        lista_noua.append(i*2)
    return lista_noua

print(inmultire_cu_2([1,2,3]))
# Functia are acelasi output ca si input-ul
# Nu are efecte secundare, intrucat nu folosim ceva din afara functiei
# O functie ce foloseste efecte secundare este urmatoarea

def inmultire_cu_2(lista):
    lista_noua =[]
    for i in lista:
        lista_noua.append(i*2)
    return print(lista_noua) # Folosim functia print, ce nu este definita in funcita noastra, deci folosim ceva din afara functiei


# SAU daca am defini lista_noua in afara functiei
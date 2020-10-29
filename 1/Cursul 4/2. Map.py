# Maparea unor actiuni, un fel de enum din C++

# def inmultire_cu_2(lista):
#     lista_noua =[]
#     for i in lista:
#         lista_noua.append(i*2)
#     return lista_noua

# EROARE
# print(list(map(inmultire_cu_2, [1,2,3])))

# map aplica o functie pentru fiecare element din colectia data la al 2 lea parametru

lista = [1, 2, 3]
def inmultire_cu_2_map(item):
    return item*2

print(list(map(inmultire_cu_2_map, lista))) # Parametrul din cadrul functiei este luat  din lista
print(lista) # Se afiseaza [1,2,3] deoarece, functia noastra nu afecteaza ce este in afara, deci lista v-a fi la fel ca inainte

lista = list(map(inmultire_cu_2_map, lista)) # Lista devine [2, 4, 6]
print(lista)
#Listele sunt vectorii din C++. Sunt o multime de diferite elemente sau de acelasi tip,
# depinzand de ceea ce vrea sa faca utilizatorul

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["a", "b", "c"]
lista_3 = [1, 2, " a", True]

# Exercitiu. Sa ne imaginam ca suntem pe Emag si  punem mai multe lucruri
# in cosul nostru de cumparaturi. Cum putem sa facem lucrul asta intr-un mod eficient si simplu?
# Putem folosi listele

cos_cumparaturi = ["Laptop Acer", "Aer conditionat pentru laptop", "Papusa Andreea e frumoasaaaaaaa"]

# Putem accesa lucruri din cosul de cumparaturi la fel ca si la string-uri
# Exemplu:

print(cos_cumparaturi[0])
print(cos_cumparaturi[1])
print(cos_cumparaturi[2])
# print(cos_cumparaturi[3]) Eroare, nu exista un element la indexul 3

# Append in engleza inseamna lipire. Deci lipim la lista noastra cos_cumparaturi inca un string, si anume string-ul "ochelari de soare"
cos_cumparaturi.append("Ochelari de soare")
print(cos_cumparaturi[3])
cos_cumparaturi.append("O carte despre suflet")
cos_cumparaturi.append("Jurnalul unui Andrei")
cos_cumparaturi.append("Andreea. Zeita pantalonilor sexy")
cos_cumparaturi.append("Inainte de intalnire")

# Afisarea listei intregi

print(cos_cumparaturi)

# Afisarea doar anumitor elemente liniar. La fel ca la string-uri

print(cos_cumparaturi[0 : 2])

print(cos_cumparaturi[: : 2]) # De la inceput pana la sfarsit din 2 in 2

print(cos_cumparaturi[: : -1]) # De la inceput pana la sfarsit in sens invers

# Spre deosebire de string-uri care nu se pot modifica, listele pot
# Exemplu
# Poate numai dorim ca sa ne cumparam un Laptop Acer ci vrem sa ne cumparam un laptop ce nu e Acer
# Procedam astfel:

cos_cumparaturi[0] = "Laptop care nu e Acer"

print(cos_cumparaturi) # Afisam lista din nou

# Pentru crearea unei liste pe baza altei liste exista 2 metode, FOARTE DIFERITE
# Intrebarea asta poate pica la un interviu

# METODA I
cos_nou_de_cumparaturi = cos_cumparaturi # Cream o variabila ce este exact la fel cu cost_cumparaturi
# Ce se intampla daca facem diferite operatii pe noua lista?

cos_nou_de_cumparaturi.remove("Laptop care nu e Acer") # Stergem o valoare data din lista

# Observam ca se sterge din ambele liste!!!
print(cos_nou_de_cumparaturi)
print(cos_cumparaturi)
# Acest lucru se intampla pentru ca prin crearea listei noi folosind metoda de mai sus
# Practic cream o variabila ce este la adresa de memorie la fel ca cos_cumparaturi, astfel ca daca se modifica ceva in una din ele 2 se va modifica si in cealalta

# METODA II

# Crearea pe baza unei copieri

cos_nou_de_cumparaturi_copie = cos_cumparaturi[ : ] # Se copie element cu element in noua lista. Putem face si asa = cos_cumparaturi[ 0: len(cos_cumparaturi]

cos_nou_de_cumparaturi_copie.remove("Ochelari de soare")
cos_nou_de_cumparaturi_copie.remove("Inainte de intalnire")

print(cos_nou_de_cumparaturi_copie)
print(cos_cumparaturi)

# In acest caz se face o lista noua in totalitate si daca se modifica ceva in ea, modificarea va exista doar in ea
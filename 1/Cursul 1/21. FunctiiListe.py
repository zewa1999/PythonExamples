cos_cumparaturi = ["Laptop Acer", "Aer conditionat pentru laptop", "Papusa Andreea e frumoasaaaaaaa"]

# Afisarea lungimii listei
print(len(cos_cumparaturi))

# Adaugarea in lista la sfarsitul listei
cos_cumparaturi.append("Andrei si Andreea sunt frumosi impreuna")

# Adaugarea la un index specific in lista

cos_cumparaturi.insert(1, "Moara cu noroc si peripetiile lui Ghita") # Adaugam la indexul 1 string ul dat dupa virgula. Nu uita sa pui string-ul intre ghilimele sau apostrof
print(cos_cumparaturi)

# Extinde lista noastra cu niste elemente date - De tinut minte, putem extinde o lista cu alte liste!!

lista_extindere = ["Ciorapi", "Pantaloni sexy"]
cos_cumparaturi.extend(lista_extindere)
print(cos_cumparaturi)

# Stergere de la un anumit index sau de la sfarsit

cos_cumparaturi.pop(3) # Sterge elementul de la indexul 3
ultimul_element = cos_cumparaturi.pop() # Sterge elementul ultim si salveaza in variabila ultimul_element ceea ce sterge
print(cos_cumparaturi)
#Readaugam valoarea din ultimul_element
cos_cumparaturi.insert(0,ultimul_element)
print(cos_cumparaturi)



# Stergerea unei anumite valori din lista

cos_cumparaturi.remove("Ciorapi") # Am sters ciorapi din lista
print(cos_cumparaturi)

# Returnarea index-ului unui element cautat. Format functie ->  .index(valoare_cautata, index_interval_de_inceput,  index_interval_de_sfarsit)

index_el_cautat = cos_cumparaturi.index("Pantaloni sexy")
print(index_el_cautat)

# Putem cauta si intr-un anumit interval

index_el_cautat = cos_cumparaturi.index("Aer conditionat pentru laptop", 1 ) # De la intervalul 0 pana la sfarsitul listei.
# Daca nu scriem un index se va lua valoarea implicita
print(index_el_cautat)

#index_el_cautat = cos_cumparaturi.index("Aer conditionat pentru laptop", 0, 1) # Se arunca o exceptie pentru ca elementul nu se afla in intervalul [0,1]



# Rotirea tuturor elementelor unei liste

cos_cumparaturi.reverse()
print(cos_cumparaturi)



# Crearea unei copii a listei printr-o functie

lista_noua = cos_cumparaturi.copy()
print(f"Lista copiata este: {lista_noua}")



# Numara de cate ori este valoarea data intr-o lista

nr_aparitii = cos_cumparaturi.count("Pantaloni sexy")
print(f"Numarul de aparitii este {nr_aparitii}")



# Sortarea unei liste. Se poate folosi mai multe metode de sortare, dar le vom regasi mai tarziu in curs

cos_cumparaturi.sort() # Sorteaza lista in mod lexicografic
print(cos_cumparaturi)



# Stergerea tuturor elementelor dintr-o lista

# Comentez linia de mai jos ca sa nu mi stearga toata lista deja creata
#cos_cumparaturi.clear()
print(cos_cumparaturi)


# Cautarea unei valori intr-o lista

print("L" in "Laptop Acer")  # Este litera L in string-ul "Laptop Acer"?



# O alta metoda de sortare
# Sorted este un cuvant rezervat si il putem folosi si pe alte tipuri, nu doar pe liste
# Sorted produce o lista noua, spre deosebire de metoda sort
# Explicatie

#Intoarcem lista pentru a putea vedea diferenta intre cele 2 metode
cos_cumparaturi.reverse()

print(f"Lista dupa reverse este: {cos_cumparaturi}")
sorted(cos_cumparaturi)
print(f"Lista dupa sortare este {cos_cumparaturi}")

# Arata la fel, nu? Asta se intampla pentru ca sorted creaza o lista noua, si nu o sorteaza pe cea data ca si parametru
# Putem salva lista sortata intr-o alta variabila

lista_noua = sorted(cos_cumparaturi)
print(f"Lista noua sortata este: {lista_noua}")
# Acum lista noua e sortata
# Tipul acesta de date inseamna ca nu exista nimic in variabila aceea
# Poate fi folosit pentru a face o verificare
# Spre exemplu, dorim sa afisam o lista, dar daca aceasta este goala, nu mai are rost sa o afisam

lista = None
if lista is None:
    print("Lista este goala")
else:
    print(lista)

# Astfel, putem face niste verificari care nu ne pot duce la erori ce mai tarziu ne-ar lua ore sa stam sa ne dam seama de la ce este
# Mai sus am folosit un Daca -> Daca lista este Goala, adica retine in ea None atunci afiseaza Lista este goala, altfel afiseaza lista
# Invatam mai tarziu mai multe despre daca, pentru si cat timp
# Presupunem o simulare simplista a platformei Facebook
# Sa le faci din nou singura, fara sa te uiti
nume = "Andrei Costache"
grad_relatie = "Luat de Andreea"

# Daca tipul de relatie se schimba

grad_relatie = "Insurat cu Andreea"


# Afisam tipul de relatie

print(grad_relatie)

# Citim de la tastatura anul de nastere

an_nastere = input("In ce an ai fost nascut?\n")

# Exercitiul 1: Afisati numele utilizatorului si in ce an s-a nascut

print("Nume utilizator: " + nume + " " +  str(an_nastere))

# Exercitiul 2: Afisati numele, anul de nastere si varsta utilizatorului

an_curent = 2020 # Pentru o mai buna utilizare a numerelor putem crea o variabila noua ce stocheaza anul in care ne aflam

varsta =  an_curent - int(an_nastere) # El va salva varsta ca fiind un string, de aceea trebuie sa ii facem conversie la int

print("Varsta acestui utilizator este " + str(varsta))

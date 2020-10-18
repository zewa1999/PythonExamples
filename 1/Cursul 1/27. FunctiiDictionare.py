 # Daca dorim sa afisam o valoare dintr-un dictionar, dar nu stim daca cheia este una ce exista
 # Exemplu

utilizator = {
    "Nume" : "Berar",
    "Prenume" : "Andreea Marioara",
    "Data Nastere" : "01-Februarie-1999"
}

# Poate dorim sa stim statusul relatiei in care este
#print(utilizator["Status Relatie"])

# Ni se va da o exceptie, intrucat cheia Status Relatie nu exista, adica utilizatorul nu a setat nimic in privinta Statusului relatiei
# Pentru a evita erorile si a nu se ajunge la oprirea programului, putem folosi functia get
# Exemplu

print(utilizator.get("Status Relatie"))
# Daca ni se returneaza None, inseamna ca nu exista o cheie de tipul acela in dictionarul utilizator
# Dar, daca nu exista si totusi dorim sa ni se ofere o valoare implicita atunci putem pune un al doilea parametru cu statusul relatiei in functia get
print(utilizator.get("Status Relatie", "Intr-o relatie"))

# Nu se prea foloseste, dar mai exista o metoda de creeare a dictionarelor
# Exemplu

utilizator2 = dict(Nume = "Berar",
    Prenume = "Andreea Marioara",
    DataNastere = "01-Februarie-1999")

# Observam ca cheile, desi sunt string-uri nu se mai pun in ghilimele sau apostroafe si in loc de : se foloseste =
# Metoda aceasta nu se prea foloseste, dar e buna de stiut


# Cautam sa vedem daca o cheie exista intr-un dictionar
# Exemplu:

print("Status Relatie" in utilizator) # Cheia Status Relatie nu exista in dictionarul utilizator -> False
print("Data Nastere" in utilizator) # Cheia Data Nastere exista in dictionarul utilizator -> True

# Putem face si alte lucruri folosind sintaxa de mai sus

print("Data Nastere" in utilizator.keys()) # Cheia Data Nastere exista in cheile utilizatorului? keys = chei -> True

print("16-Noiembrie-2004" in utilizator.values()) # Valoarea "16-Noiembrie-2004 exista in valorile utilizatorului? values = valori -> False

print(utilizator.items()) # Afisarea cheilor si valorile asociate lor

# Crearea unui dictionar prin copierea altuia

utilizator_copie = utilizator.copy()
print(utilizator)
print(utilizator_copie)

# Stergerea unei chei si valoare pe baza cheii

element_dictionar = utilizator.pop("Nume")
print(element_dictionar)
print(utilizator) # Observam ca cheia si valoare ce retinea Numele nu mai exista

# Stergerea unei chei si valoare la nimereala
element_dictionar = utilizator.popitem()
print(element_dictionar)
print(utilizator) # Observam ca cheia si valoare ce retinea Numele nu mai exista

# Actualizarea unei valori a unei chei
print(utilizator.update({"Prenume" : "Andrei Costache"}))

# Daca cheia data ca si parametru nu exista, pitonul o va crea folosind datele date
print(utilizator.update({"Data Nastere" : "26-Noiembrie-1999"}))
print(utilizator)


# Sterge tot ce se afla in dictionar
utilizator.clear()
print(utilizator)

# Exercitiu: Creati un user pentru un joc cu urmatoarele chei:
# age = varsta, username = numele contului, weapons = armele, is_active = contul mai este activ?, clan = clanul din care face parte
user = {
    'age': 22,
    'username': 'Shogun',
    'weapons': ['katana', 'shuriken'],
    'is_active': True,
    'clan': 'Japan'
}
# Afisati toate cheile din user
print(user.keys())

# Adaugati o arma noua in arsenalul jucatorului
user['weapons'].append('shield')
print(user)

# Adaugati cheia is_banned si setati-o ca fiind falsa
user.update({'is_banned': False})
print(user)

# Setati contul ca fiind banat
user['is_banned'] = True
print(user)

# Creati o copie a contului si actualizati campurile age si username
user2 = user.copy()
user2.update({'age': 100, 'username': 'Timbo'})
print(user2)
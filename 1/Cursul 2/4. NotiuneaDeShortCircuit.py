# Cuvantul or este un cuvant rezervat la fel ca si and
# or pe romaneste inseamna sau si and inseamna si
# or este mai eficient intrucat intr-o conditie de tipul if doar una dintre conditii trebuie sa fie adevarata
# O data ce evalueaza expresia si vede ca e adevarata, se opreste si trece pe ramura urmatoare
# Exemplu:

sunt_baiat = True
sunt_om = True

if sunt_baiat or sunt_om:
    print("Conditie adevarata!")
# Interpretatorul de Python, se uita la prima conditie care este sunt_baiat, o evalueaza si daca vede ca este adevarata, nu-l mai intereseaza ce se afla dupa ca si conditii
# Acelasi lucru se intampla si pentru and. Daca se regaseste o variabila ca fiind falsa, atunci nu se mai evalueaza ce este dupa asta

sunt_om = False

if sunt_om and sunt_baiat: # Aici nu se afiseaza pt ca e fals
    print("Conditie Falsa")
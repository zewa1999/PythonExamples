# Parametrii unei functii sunt niste variabile pe care le putem oferi functiei pentru a le modifica sau sa facem alte operatii cu ele

def spune_salut(nume):  # Parametrii sunt datele ce sunt nevoite pentru ca functia sa functioneze
    print(f"Saluta {nume}!")


spune_salut("Andreea")  # Atentie la cum indentam codul


# Andreea este un argument, datele pe care le primeste functia

def functie1(nume, varsta):
    print(f"Tu esti {nume} si ai {varsta} ani!")


# Daca apelam functia astfel, ce se afiseaza?

functie1(14, "Andreea")

# Poate ca am uitat in ce ordine am pus parametrii, dar putem sa facem acest lucru in cazul asta

functie1(varsta=14, nume="Andreea")  # Nu trebuie sa facem asta, e o metoda proasta de a scrie cod


# Parametri impliciti:

def functie2(nume="Andrei", varsta=20):
    print(f"Eu sunt {nume} si am {varsta} ani!")


# Daca nu dorim sa folosim o valoare de a noastra, putem apela functie2 fara a mai scrie nici-un parametru

functie2()

# Daca dorim sa punem doar numele

functie2("Alex")

# Daca dorim sa punem doar varsta

functie2(varsta=21)

# Sau ambele
functie2("Gigel", 15)

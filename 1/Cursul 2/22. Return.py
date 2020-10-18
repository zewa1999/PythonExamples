# Return este o modalitate de a returna o valoare dupa sfarsitul unei functii
# Este o buna practica ca orice functie sa returneze ceva
# O functie este de preferat sa faca un singur lucru

def suma(nr1, nr2): # Returnam o valoare de tipul celor 2 valori date ca si parametru
    return nr1 + nr2
    print("Ceva dupa return")

print(suma(1,2))

# Ce se afiseaza aici?

print(suma(1,2) + suma(3,4))

# Nu se afiseaza ceea ce este dupa return, return reprezinta sfarsitul functiei

def checkDriverAge(varsta = 0):
    if int(varsta) < 18:
        print("Scuze, nu ai varsta necesara pentru a putea conduce")
    elif  int(varsta) > 18:
        print("HAIDEEEEEEEEE!!!")
    elif int(varsta) == 18:
        print("Primul an de condus, bineee baaaaaaa!!")


checkDriverAge(21)

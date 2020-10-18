# Daca ajungem sa avem o multitudine de functii si poate nu mai stim ce face fiecare putem
# folosi docstring pentru a pune o definitie a functiei

string = 'A inceput facultatea. O sa ne vedemmmmmmmm'
len(string)
# Daca ne ducem cu mouse-ul peste len si asteptam putin o sa vedem ca ne spune ca functia returneaza
# lungimea tipului respectiv de date
# si noi putem face acest lucru folosind docstring
# python foloseste acelasi lucru

def afisare(parametru):
    """
    INFO:Afiseaza tipul de date dat ca parametru
    """
    print(parametru)


afisare("Incepe facultatea")

print(afisare.__doc__) # Afisam mesajul cu informatii
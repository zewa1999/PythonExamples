# Putem folosi si ghilimele cat si apostrof
# Nu rula, incearca sa iti dai seama ce se intampla singura

print(type("Andreea e frumoasa si e iubita mea")) # -> tip str
nume = "Costache"
prenume = 'Stelian Andrei'
long_string = '''
WOW
0  0
 --
 '''
print(long_string)

nume_intreg = nume + ' ' +  prenume # Nume + Spatiu + Prenume
print(nume_intreg)

# Concatenarea string-urilor

nume_intreg_andreea = "Berar" + " " + "Andreea" + " " + "Maria"
print(nume_intreg_andreea)

#Conversia unui tip de date catre string

#Print poate afisa doar un tip de date o singura data, deci nu poate afisa si un int cat si un str in acelasi timp. O sa crape daca facem asa. EX:
numar_intreg = 6789
#print("Numarul meu este: " + numar_intreg) # Nu merge intrucat numar_intreg este un numar. Nu putem afisa 2 tipuri de date in acelasi timp
#print(type(numar_intreg))
print("Numarul meu este: " + str(numar_intreg)) # Merge, intrucat am facut conversia de la un numar la un str si practic acum si numar_intreg este un str


# Exercitiu: Ce se afiseaza in urma urmatoarei secvente de cod?
# Ne aducem aminte ca functia type() retine tipul de date al unei variabile

a = str(100)
b = int(a)
c = type(b)
print(c)
# Facem o aplicatie pentru a putea vedea daca cineva are varsta necesara pentru a putea conduce o masina

varsta_necesara = int(input("Ce varsta ai?\n"))
are_permis = input("Ai luat permisul?\n 1 daca da, 0 daca nu.\n")

if are_permis =="1": # Daca are_permis e 1 atunci devine True, atfel nu
    are_permis = True
else:
    are_permis = False

# Daca varsta citita este mai mare sau egala cu 18 si utilizatorul are permis atunci afisam ce se afla pe ramura if, altfel afisam ce se afla pe else
if varsta_necesara >= 18 and are_permis is True:
    print("Poti conduce!")
elif varsta_necesara >=18 and are_permis is False: # Daca are varsta necesara, dar nu are permisul luat atunci afisam ca nu are permisul luat
    print("Nu ai permisul luat!")
else:
    print("Nu poti conduce!")

print("Sfarsit program!")
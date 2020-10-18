# Scrieti o functie ce returneaza daca numarul este par

def numar_par1(numar):
    if numar % 2 == 0:
        return True
    elif numar % 2 == 1:
        return False

# Functia face ce trebuie, dar cum putem scrie un cod mai compact pentru functionalitatea asta?

def numar_par2(numar): # Daca numarul se imparte exact la 2, afisam True, altfel in orice alt caz afisam False
    if numar % 2 == 0:
        return True
    return False

def numar_par3(numar): # Returnam direct un tip bool( True sau False) in functie de rezultatul restului impartirii la 2
    return numar % 2 ==0
# Daca numarul se imparte la 2, inseamna ca se returneaza True, daca nu se returneaza False

# Diferenta in linii scrise este foarte mare, ultima varianta fiind cea mai compacta

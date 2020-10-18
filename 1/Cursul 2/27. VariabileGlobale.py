# Ce se intampla in urmatorul exemplu?

# total = 0
#
# def numar_aparitii():
#     total +=1
#     return total
#
# numar_aparitii()

# Nu merge, este?
# Daca dorim sa modificam variabila total fara a o da drept parametru, putem folosi
# Cuvantul global
# EX:

total = 0

def numar_aparitii():
    global total # Se refera la total declarat inaintea functiei
    total +=1
    return total

print(numar_aparitii())

# O metoda mai simpla este folosind dependinte intejectoare

total1 = 0

def numar_aparitii(total1):
    total1 +=1
    return total1

print(numar_aparitii(numar_aparitii(total1))) # Se afiseaza 2 pentru ca apelam functia de 2 ori
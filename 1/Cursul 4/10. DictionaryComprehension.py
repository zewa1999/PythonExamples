dictionar_simplu = {
    'a' : 1,
    'b' : 2
}

# I-a elementele din dictionar_simplu si le inmulteste valoarea si daca valoarea este para atunci le adauga in dictionar

dictionar = {key:value**2 for key,value in dictionar_simplu.items()
             if value % 2==0}

print(dictionar)

alt_dictionar = {nr:nr*2 for nr in [1, 2, 3]} # Cream un dictionar care are ca si cheie numarul si valoare numarul inmultit cu 2
print(alt_dictionar)


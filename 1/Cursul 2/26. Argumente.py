# *args **kwargs
# Folosit daca nu stim cate argumente avem intr-o functie

def super_functie(*args, **kwargs): # **kwargs - Cuvinte de tip argument
    print(args) # Se afiseaza numerele din multimea de tip Tuple in care sunt salvate
    print(*args) # Se afiseaza numerele

    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k}: {v}")
    return sum(args) # sum e o functie ce exista deja in Python

print(super_functie(1,2,3,4,5,6, nr1 = 5, nr2 = 6))

# Regula: Parametrii intr-o functie ce foloseste * args si **kwargs trebuie sa aiba forma asta la parametrii
# parametrii ce ii vrei tu, *args,parametrii default , **kwargs
# Exemplu:

def functie_arg(nume, varsta, *args, facultate="Matematica-Informatica", **kwargs):
    print(f"Numele meu este {nume}, am varsta de {varsta} ani si studiez la Facultatea de {facultate}")
    print(f"Suma notelor mele este {sum(args)}")
    print(f"Persoanele la care tin sunt: {kwargs.keys()}")

functie_arg("Andreea", 16, 9,5,8,7,el1="Ma ma",el2="Tata",el3="Anton",el4="Florin",el5="Andrei")
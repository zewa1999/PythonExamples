# In Python exista o multitudine de erori pe care le poate face programatorul
# Ce s-ar intampla daca programul nostru ar avea o simpla eroare si ar crapa totul?
# Ceva ce nu e bun
# Poate ca facem o aplicatie de tipul unui calculator si din greseala impartim la 0
# Nu dorim ca sa crape toata aplicatia ci spunem doar faptul ca, nu se poate face impartirea la 0
# Cum putem face ca aplicatia noastra sa functioneze in continuare, chiar daca se face impartirea la 0?

# Folosind try - except
# Exemplu:

# Ierarhie de exceptii
while True:  # Loop infinit
    try:
        varsta = int(input("Ce varsta aveti?"))
        print(varsta)
        15/0
    except ValueError:
        print("Adaugati o varsta corecta!")
    except ZeroDivisionError:
        print("Adaugati va rugam o varsta mai mare de 0!")
    else:
        print("Multumim")
        break
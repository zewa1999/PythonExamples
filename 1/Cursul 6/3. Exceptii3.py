while True:  # Loop infinit
    try:
        varsta = int(input("Ce varsta aveti?"))
        print(varsta)
        15/0
        raise ValueError("Exceptie aruncata de noi")
    except ValueError:
        print("Adaugati o varsta corecta!") # Ajunge aici
        continue # Continua rularea programului
    except ZeroDivisionError:
        print("Nu poti imparti cu 0")
    else:
        print("Multumim")
        break
    finally:
        print("Gataa boss!") # continue nu iese din loop, deci ajunge aici
    print("Ma auzi?")
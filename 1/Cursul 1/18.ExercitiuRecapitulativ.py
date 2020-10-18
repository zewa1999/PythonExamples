# Vom face o aplicatie ce va verifica parolele

nume_cont = input("Numele contului dvs este:\n")
parola = input("Parola este:\n")

parola_codata = "*" * len(parola) # Inmultim caracterul "*" de 10 ori si il salvam in variabila parola_codata


print(f"Numele contului:{nume_cont}\nParola {parola_codata}\n Lungimea parolei este de {len(parola)} caractere")
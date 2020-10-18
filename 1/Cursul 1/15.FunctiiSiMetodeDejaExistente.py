# Functii deja existente in Python

# Afisarea lungimii unui string

print(len("andreea este superba si andreea este draguta")) # Incepe si numara cate caractere sunt de la 1

stringul_meu = "Saluttttttttttttttt!"
print(stringul_meu[0:len(stringul_meu)]) # merge de la 0 pana la ultimul caracter si afiseaza tot


intrebare = "A fi sau a nu fi, asta e intrebarea."

# Putem accesa o metoda al unui tip de date folosing numele campului urmat de "."


print(intrebare.upper()) # FACE TOATE LITERELE MARI

intrebare.capitalize()
print(intrebare) # Face prima litera a stringului mare


print(intrebare.find('b')) # Imi afiseaza la ce index a gasit prima data valoare data in paranteza

print(stringul_meu.replace("Salu", "ttttttttttt")) # A inlocuit din string ul salutttttttt partea de "salu" cu mai multi de t
# Atentie, inlocuiestie nu doar prima aparitie ci toate aparitiile din string

# Cum am invatat inainte, stringurile nu se pot schimba, deci in continuare avem un exercitiu la care
# sa imi spui ce se afiseaza fara a da run si mai apoi sa vezi daca ai raspuns corect

intrebare.replace("fi", "bea")
print(intrebare) # Cum va arata stringul asta dupa executare?

intrebare.upper() # Dar acum?
print(intrebare)
intrebare = intrebare.replace("fi", "bea")
intrebare = intrebare.upper()

print(intrebare)


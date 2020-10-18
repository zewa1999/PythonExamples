# Continue inseamna in romana continua
# Are rolul de a-i spune lui Python ca orice s-ar intampla intr-o instructiune repetitiva, el sa se intoarca la inceputul instructiunii
# Exemplu:

string = "Andreea e iubita mea"

for caracter in string:
    continue
    print(caracter)

i =0
while i < len(string):
    continue
    print(caracter)

# Daca rulam nu se afiseaza nimic, intrucat cand se ajunge la linia cu continue, se trimite rularea instructiunii repetitive direct la inceput fara a se mai rula ce este sub ea
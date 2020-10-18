# Primul caz: Aici pare ca se pot schimba string-urile, nu-i asa?

un_string = "Andreea si Andrei sunt impreuna de 8 luni"

print(un_string)

un_string = "100"

print(un_string)

# Al doilea caz: Aici de ce nu se pot schimba si crapa?

# alt_string = "Andreea e superba"

# alt_string[0] = "B"

# In primul caz nu crapa intrucat Python ne lasa sa schimbam un string cu totul, deci in loc de Andreea si Andrei sunt impreuna de 8 luni
# avem un cu totul alt string salvat in memorie ce retine "100"

# In cel de al doilea caz crapa intrucat se doreste a se schimba o valoare din string-ul nostru, adica dorim ca si caracterul situat la indexul 0, adica "A" sa devina "B"
# Python nu accepta acest lucru.

# Putem sa facem o smecherie, dar in spate, practic este acelasi lucru ca si in primul caz

un_al_treilea_string = "Imi plac gogosile"

un_al_treilea_string += " si piersicile"  # Observam folosirea operatorului +=

print(un_al_treilea_string)

# In acest ultim caz, practic Python salveaza stringul "Imi plac gogosile" intr-o copie, sterge tot ce se afla in un_al_treilea_string
# si creaza un nou string pe baza copiei create si celui de al doilea string " si piersicile"
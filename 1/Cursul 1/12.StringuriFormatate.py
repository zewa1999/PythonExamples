# Pentru a putea afisa numele si alte date ale unui utilizator nu suntem nevoiti sa retinem toate numele din lume si sa il alegem pe cel potrivit
nume = "Gigel Mare Randament"
varsta = 15

# Tipul asta de afisare se numeste afisare dinamica, adica se afiseaza date in functie de ce utilizator avem
print("Salut " + nume + ". Ai " + str(varsta) + " ani!" )

# O alta metoda mai rapida, fara a fi nevoie de a converti varsta si de a pune atatea plusuri intr-o instructiune print este folosind string-urile formatate. EX:

print(f"Salut {nume}. Ai {varsta} ani!")#Tot ce trebuie sa facem e ca la inceputul lui print vom pune "f"
# Unde avema acolade se inlocuieste cu variabila scria inauntrul acoladelor
# Astfel, in loc de {nume} v-a aparea "Gigel mare randament" si in loc de {varsta} va aparea 15
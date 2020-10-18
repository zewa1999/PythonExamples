# Avem un joc cu vrajitori de facut

este_magician = True
este_expert = False

# Afiseaza " esti un maestru magician" daca esti magician si expert
# Afiseaza " Incet incet vei ajunge si tu expert" daca esti magician si NU expert
# Afiseaza "Ai nevoie de puteri magice pentru a fi magician" daca esti nu magician
if este_expert and este_magician:
    print("Esti un maestru magician")
elif este_magician and not este_expert:
    print("Incet incet vei ajunge si tu expert")
else:
    print("Ai nevoie de puteri magice pentru a fi magician")
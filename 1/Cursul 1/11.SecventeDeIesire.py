# Sa presupunem ca facem o aplicatie in limba engleza in care prezentam vremea
# Vremea in momentul asta este insorita, deci aplicatia noastra trebuie sa afiseze in engleza 'It's Sunny!'
# Hai sa incercam asta

#vreme_actuala = 'It's Sunny! # Putem observa ca nu putem adauga 2 apostroafe, deci avem o problema
# Exista 2 metode: 1. Sa folosim ghilimele in loc de apostrof in aceste cazuri
vreme_actuala = "It's Sunny!"
# SAU: Sa folosim '\' inainte de apostroful din cadrul cuvantului
vreme_actuala = 'It\'s Sunny!'


# De preferat este sa folosim cea de a 2 a metoda, intrucat daca folosim ghilimelele pentru a pune in ghilimele si niste cuvinte ajungem la aceeasi problema. EX:

vreme_actuala = "It's " "kind of" "Sunny!" # Corect ar fi ca mai jos

vreme_actuala= "It's \"kind of\" Sunny!" # "kind of" e ca un paragraf ce trebuie pus intre ghilimele

print(vreme_actuala)

# O alta secventa de iesire importanta este si \n. EX:

vreme_actuala= "It's \"kind \n of\" Sunny!" # Trimite afisarea pe urmatoarea linie
print(vreme_actuala)

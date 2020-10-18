# Un if doar ca scrii mai putin. Se mai numesc si expresii conditionale

# Forma: conditie_daca_adevarat if conditie else conditie_daca_fals

# Determinam daca un utilizator ne este prieten

este_prieten = True

print("Imi este prieten") if este_prieten is True else print("Nu imi este prieten")
# Afisam imi este prieten daca este_prieten e True, daca nu este True atunci afisam Nu imi este prieten
# Mai putem face si o conditie ce este salvata

raspuns = print("Imi este prieten") if este_prieten else print("Nu imi este prieten")

print(f"Raspunsul este {raspuns}")
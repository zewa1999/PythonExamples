class SuperLista(list):
    def __len__(self):
        return 5000

super_lista = SuperLista()
super_lista.append(5)
print(super_lista)
print(issubclass(SuperLista, list)) # Este SuperLista o subclasa a list
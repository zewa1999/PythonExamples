
def decoratorul_meu(functie):
    def wrap_function(nume):
        print("********")
        functie(nume)
        print(f"***{nume}*****")
    return wrap_function
#
# @decoratorul_meu
# def salut():
#     print("Salut!!")
#
# salut()

# print("",end='\n\n')
# @decoratorul_meu
# def paa():
#     print("La revedere!!!")
#
# paa()

# # Nu se afiseaza doar ce face functia salut, ci si alte functionalitati ce sunt scrise in declaratia decoratorului meu

# print("",end='\n\n')
# salut2 = decoratorul_meu(salut)
# salut2()
#
# print("",end='\n\n')
# decoratorul_meu(salut2)()

nume = "Andreea"
@decoratorul_meu
def buna(un_salut):
    print(un_salut)

buna(nume)

# Ce facem daca dorim sa avem mai multi parametrii
# Folosim *args si **kwargs

# Decorator Pattern
def alt_decorator(functie):
    def wrap_function(*args, **kwargs):
        functie(*args, **kwargs)
    return wrap_function

@alt_decorator
def nr_nelimitat_param(salut, emoji=":)", ):
    print(salut, emoji)

nr_nelimitat_param("Bunaaa")
from time import time

# Folositi pentru o viteza mult mai mare

def performance(function):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = function(*args, **kwargs)
        time2 = time()
        print(f"Timp estimat al functiei: {time2 - time1} secunde")
        return result
    return wrapper


@performance
def functie_lunga1():
    print("1")
    for i in range(10000000):
        i*5


@performance
def functie_lunga2():
    print("2")
    for i in list(range(10000000)):
        i*5

functie_lunga1()
functie_lunga2()



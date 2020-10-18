# int and float
# isi da seama in functie de virgula ce tip de date e
import math

print('Ce tipuri de date sunt: ')

print(type(6))  # int
print(type(2 - 4))  # int
print(type(2 * 4))  # int
print(type(2 / 4))  # float
print(type(0.000001))  # float

print('Operatori: ')
print(2 ** 2)  # putere: 2^2

print(2 ** 3)  # putere: 2^3

print(2 // 4)  # imparte pe 2 la 4 si rotunjeste dupa asta -> rezultat e 0

print(5 % 4)  # restul impartirii lui 5 la 4

# functii matematice sau actiuni

# Rotunjire

print('Round 3.1:')
print(round(3.1))

print('Round 3.4:')
print(round(3.4))

print('Round 3.5')
print(round(3.5))

print('Round 3.8')
print(round(3.8))

# Modul sau valoare absoluta

print('Modul |-31|')
print(abs(-31))

# Factorial

print('Factorial de 3!')
print(math.factorial(3))

# Copiere semn: Se dau 2 numere (1, -0). Se afiseaza primul numar cu semnul de la al doilea

print("Math.copysign:")
print(math.copysign(1.2, -2.0))

# Returneaza cel mai mare divizor comun a 2 numere

print("CMMDC pentru 24 cu 6; 32 cu 5; 0 cu 0")
print(math.gcd(24, 6))
print(math.gcd(32, 5))
print(math.gcd(0, 0))

# Cel mai mic multiplu comun: Se afla folosind formula: (nr1*nr2) / cmmdc
print("Cel mai mare multiplu comun al numerelor n1 si n2 -> Se citesc de la tastatura:")
# trebuie sa transformam tipul de date ce il primim de la tastatura intr-unul de care avem noi nevoie, adica int...ex:

n3: int = input() # este de tipul str
print(type(n3))

n1: int = int(input())
n2: int = int(input())

print(abs(n1*n2) / math.gcd(n1,n2))

# Returneaza suma unei multimi de numere

print("Suma a 0.1 de 9 ori: ")
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

# Functii trigonometrice, radicali, logaritmi, puteri, hiperbolice, valori ale lui Pi, tau sau altele le gasim aici:
# https://docs.python.org/3/library/math.html

# Avand clasa urmatoare data
class Pisica:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.varsta = age


def find_oldest_cat(c1, c2, c3):
    if c1.varsta > c2.varsta and c1.varsta > c3.varsta:
        print(f"{c1.name} este cea mai in varsta si are varsta de {c1.varsta} ani!")
    elif c2.varsta > c1.varsta and c2.varsta > c3.varsta:
        print(f"{c2.name} este cea mai in varsta si are varsta de {c2.varsta} ani!")
    elif c3.varsta > c1.varsta and c3.varsta > c2.varsta:
        print(f"{c3.name} este cea mai in varsta si are varsta de {c3.varsta} ani!")


# Creati 3 pisici
pisica1 = Pisica("Misa", 11)
pisica2 = Pisica("Lisa", 9)
pisica3 = Pisica("Mary", 2)

# Creati o functie ce afiseaza numele si varsta celei mai in varsta pisica

find_oldest_cat(pisica1, pisica2, pisica3)

# Pentru toti manelariiiiiiiiiii:
# https://www.youtube.com/watch?v=il_eu0sf0zA&ab_channel=NicolaeGutabyBIGMAN



# SAU ASA

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")

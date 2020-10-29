from functools import reduce

#1 Fa literele mari la fiecare string din lista
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capit(name):
  return name.capitalize()
print(list(map(capit,my_pets)))


#2 Alipeste listele dar sorteaza elementele din my_numbers
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

#3 Filtreaza scorurile peste 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score_over_fifty(el):
  return el > 50

print(list(filter(score_over_fifty, scores)))


#4 Fa totalul unei liste din element

def total(acc, item):
  return acc + item
print(reduce(total, my_numbers, 0))


def functie_generator(num):
    for i in range(num):
        yield i*2

g = functie_generator(100) # apelam functia
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
# for item in functie_generator(1000):
#     print(item)
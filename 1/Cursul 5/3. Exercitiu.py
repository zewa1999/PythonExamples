from time import time


# Decorator Exercitiu


def performance(function):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = function(*args, **kwargs)
        time2 = time()
        print(f"Timp estimat al functiei: {time2 - time1} secunde")
        return result
    return wrapper


@performance
def functie_lunga():
    for i in range(100000000):
        i*5

functie_lunga() # Functia v-a lua mult timp pana se va rula


# Exercitiul 2
# Apelati o functie folosind un decorator bazandu-va pe o valoare dintr-un dictionar dat

user1 = {
    'name': 'Sorna',
    'valid': False
}

def authenticated(fn):
  def wrapper(user):
    if user["valid"] is True:
      fn(user)
    elif user["valid"] is False:
      print("Valid is not true")
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
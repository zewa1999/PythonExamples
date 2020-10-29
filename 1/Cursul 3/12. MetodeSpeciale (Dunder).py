#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Jucarie():
  def __init__(self, culoare, vechime):
    self.culoare = culoare
    self.vechime = vechime
    self.dictionarul_meu = {
        'nume':'Yoyo',
        'are_animale': False,
    }

  def __str__(self):
    return f"{self.culoare}"

  def __len__(self):
    return 5

  def __del__(self):
    return "Sters"

  def __call__(self):
      return 'yes??'

  def __getitem__(self,i):
      return self.dictionarul_meu[i]


action_figure = Jucarie('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['nume'])
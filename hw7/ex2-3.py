
from abc import ABC, abstractmethod

class Closes(ABC):
    result = 0
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass
    def __add__(self, other):
        Closes.result += self.consumption + other.consumption
        return Costume(0)
    def __str__(self):
        return f"{Closes.result}"
class Coat(Closes):
    @property
    def consumption(self):
        return round(self.param/6.5)+0.5
class Costume(Closes):
    @property
    def consumption(self):
        return round((2*self.param+0.3)/100)
coat = Coat(42)
costume =Costume(170)
print(coat+costume)
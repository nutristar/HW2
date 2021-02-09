from abc import  ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass
    def __add__(self, other):
        return self.raschet+other.raschet
class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if size < 40:
            print("на детей не шьем  Начнем с 40")
            self.__size =40
        elif size > 58:
            print("58 - maximum")
            self.__size = 58
        else:
            self.__size=size
        @property
        def raschet(self):

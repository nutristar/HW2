""" Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определенное название. К типам одежды в этом проекте относятся пальто
 и костюм. У этих типов одежды существуют параметры: размер (для пальто) и
  рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
 методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Odejda(ABC):

    def __init__(self, v=100):
        self.v = v


    @property
    @abstractmethod
    def consumption_Coat(self,v):
        pass

    @property
    @ abstractmethod
    def consumption_Costum(self, v):
        pass
    @property
    def consumption(self):
        return self.consumption_Coat+self.consumption_Costum

 

class Coat(Odejda):
    @property
    def consumption(self):
        result = round(self.v / 6.5 + 0.5 , 2)
        Odejda.consumption_Coat = result
        return f"для пальто размера{self.v} ненобходимо {result} ткани"

class  Costum(Odejda):
    @property
    def consumption(self):
        result = round(2*self.v+0.3,2)
        Odejda.consumption_Costum = result
        return round((self.v *2) + 0.3)/100

coat_our=Coat(52)
costum_our=Costum(1.8)
print(costum_our, coat_our)
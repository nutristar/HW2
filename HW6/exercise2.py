""" Реализовать класс Road (дорога), в котором определить атрибуты:
 length (длина), width (ширина). Значения данных атрибутов должны
 передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
  Определить метод расчета массы асфальта, необходимого для покрытия всего
  дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
   покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
   Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road:
    def __init__(self, lenth, width):
        self._lenth=lenth
        self._width = width
    def get_full_prof(self):
        return f"{self._lenth}m*{self._width}m *25kg*5cm= {(self._lenth*self._width*25*5)/1000}t"

road1=Road(5000,20)
print(road1.get_full_prof())

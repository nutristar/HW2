"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

spis = [1, "vasili", {False: 333}, True, "babuin"]
for i in spis:
    print(type(i))
    
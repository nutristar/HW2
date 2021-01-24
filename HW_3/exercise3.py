"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""
def my_func(x,y,z):
    
    lst_min=min(x,y,z)
    #print(lst_min)
    if lst_min==x:
        return y+z
    if lst_min==y:
        return x+z
    if lst_min==z:
        return x+y
print(my_func(1,2,3))
"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint

with open("fith.txt",mode="w+",encoding="utf-8") as my:
    my_list=[randint(1,100) for _ in range(100)]
    my.write(" ".join(map(str,my_list)))
    my.seek(0)
    print(sum(map(int,my.readline().split())))
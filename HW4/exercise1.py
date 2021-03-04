""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv
#worker_info={name: "Вася Пупкин", time:160, rate_per_hour: 5, bonus:1.1}
#script_name,time,rate,bonus= argv
def salary_calculator (**kwargs):
    try:
        time, rate, bonus = map(float, argv[1:])
        print(time*rate+bonus)

    except ValueError:
        print("enter 3 arguments  not string")


salary_calculator()
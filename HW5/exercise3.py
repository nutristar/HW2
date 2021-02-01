""" Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("workers.txt","r",encoding="utf-8") as ob:
    salary_dict={line.split()[0]:float(line.split()[1]) for line in ob}
    #print(salary_dict)
    for e in salary_dict.items():
        if e[1]<20000:
            print(f"{e[0]}  зарабатывает менее 20к")
    print(f"average sallary{round(sum(salary_dict.values())/len(salary_dict), 3)}")



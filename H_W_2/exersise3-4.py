"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
  Напишите решения через list и через dict.
"""

month=int(input("введите месяц от 1 до 12"))
year={"summer":[6,7,8],"autumn":[9,10,11],"winter":[12,1,2],"spring":[3,4,5]}

for key, value in year.items():
    if month in value:
        print(f"введенный вами месяц это {key}")
"""____________________________________________________"""
"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

stroka= "шла саша по шосссе".split()
stroka=enumerate(stroka,1)
print(type(stroka))
print(stroka)
for n ,i in stroka:
    #print(n,i) if len(i)<10 else print(n,i[:10])
    print(f"{n}.{i[:10]}")
"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
"""

from googletrans import Translator

with open("RazDva.txt", "w", encoding="utf-8") as razdva:
    with open("OneTwo.txt", "r",encoding="utf-8" ) as ontw:

        txt=ontw.read()
    try:
        razdva.write(Translator().translate(txt, dest="ru").text)
    except AttributeError:
        print("ддос ататка")

"""не работает - code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'   ПОЧЕМУ?"""
rus_dic={"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
with open("RazDva.txt", "+", encoding="utf-8") as razdva:
    with open("OneTwo.txt", "r",encoding="utf-8" ) as ontw:
        razdva.writelines(line.replace(line.split()[0],rus_dic.get(line.split()[0]))for line in ontw)

        print(razdva.read) #почему не печатает?

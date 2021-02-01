"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке."""


"""with open("python.txt","r",encoding="utf-8")as ob:
    с=0
    for line, count in enumerate(ob,1):

        с+=1
        print(f"{line} строка, в ней {len(count.split())} слов")
    print(f"всего строк{с}")"""

with open("python.txt","r",encoding="utf-8")as ob:
    spis=[f"{line}я строка,  в ней {len(count.split())} слов"
          for line, count in enumerate(ob,1)]
    print(*spis,f"всего строк{len(spis)}", sep="\n")


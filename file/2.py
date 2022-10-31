"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('sad_blabla.txt', 'w+') as amogus:
    amogus.write('но у меня не получается')
    amogus.seek(0)
    sad = amogus.read()
with open('blabla.txt', 'r') as happyamogus:
    happy = happyamogus.read()
with open('mega_blabla.txt', 'w+') as verysadamogus:
    verysadamogus.write(happy + ' ' + sad)
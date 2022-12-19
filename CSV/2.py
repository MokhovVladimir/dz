import csv

"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
slov = {}
with open('1.csv', encoding= 'UTF-8') as f:
    test = csv.reader(f, delimiter=';')
    for i in test:
        slov[(i[0], i[1])] = {i[2]: i[3]}

print(slov)
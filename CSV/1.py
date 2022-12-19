import csv

"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""

with open('1.csv', encoding= "UTF-8") as f:
    test = csv.reader(f, delimiter=';')
    for i in test:
        print(f'{i[0]} - {i[3]}')

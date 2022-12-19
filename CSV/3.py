"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv
import random


data = [
    ['питон', 'Бобченок', 11],
    ['Администрирование ИТ систем', 'Кибердед', random.randint(5, 10)],
    ['Сети и протоколы', 'Головин', random.randint(7, 10)],
    ['Алгоритмы', 'Шабрашин', random.randint(9,10)]
]

with open('lyubov_k_prepodam.csv', 'w', encoding="UTF-8") as f:
    test = csv.writer(f)
    for row in data:
        test.writerow(row)

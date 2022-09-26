"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
slov = {'name': 'Vladimir', 'job': 'student', 'age': '18', 'cat': 'Baks', 'uvl': 'Coding'}
l = list(slov.items())
del l[1]
slov = dict(l)
slov['name'], slov['uvl'] = slov['uvl'], slov['name']
slov.setdefault('new_key', 'new_value')
print(slov)


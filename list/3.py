n = [int(i) for i in input('Введите оценки через пробел: ').split()]
print(n.count(5))
print(n.count(5) / len(n) * 100)
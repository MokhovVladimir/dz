n =[int(i) for i in input('Введите оценки через пробел: ').split()]
kol = []
for i in range(3, 6):
    kol.append(n.count(i))
usp = (kol[0] + kol[1] + kol[2])/4 * 100
print(n, kol, usp, sep='\n')
info = []
for i in range(3):
    if i == 0:
        fio = input('Ваша фамилия: ')
        info.append([fio])
    elif i == 1:
        dol = input('Ваша должность: ')
        info.append([dol])
    elif i == 2:
        count = input('Количество студентов: ')
        info.append([count])
print(info)
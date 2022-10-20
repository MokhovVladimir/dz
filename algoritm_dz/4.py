''' Алгоритм основывается на переводе числа из одной системы исчисления в другую и автоматической сумме его цифр '''


def sumBase(n: int, k: int) -> int:
    count = 0  # Переменная для суммы цифр числа
    while n != 0:  # Пока число полностью не сократилось, мы уменьшаем и делим
        count += n % k # записываем остаток от деления, что и будет числом в k-ой системе исчесления
        n = n // k
    return count


print(sumBase(int(input()), int(input())))

''' Сложность логорифма O(n) из-за одного цикла'''
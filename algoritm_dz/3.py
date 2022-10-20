''' Алгоритм основывается на сравнении камня с драгоценными камнями и перебору каждого из них'''


def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    stack = list(jewels)  # создаем стек для работы с буквами и драгоценными камнями и счетчки для их подсчета
    for i in stones:
        if i in stack:  # Проверяем наличие буквы-камня в стеке и добавляем в счетчик при необходимости
            count += 1
    return count  # Возвращаем счетчик


print(numJewelsInStones(input(), input()))

''' Сложность алгоритма О(n) из-за одного цикла'''
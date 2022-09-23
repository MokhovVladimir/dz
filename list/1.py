game = []
while True:
    n = input('Введите название игры: ')
    if n in game:
        print('Эта игра уже записана')
    elif n == '0':
        sorted(n)
        print(*game)
        break
    else:
        game.append(n)
        print('Ваша игра записана')


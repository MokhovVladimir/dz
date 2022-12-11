"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""


class Hero():
    def __init__(self, hp, armor):
        self.hp = hp
        self.armor = armor

    def lol(self):
        print(123)


class Magican(Hero):
    def hello(self):
        print('Бла бла, я маг')

    def attack(self):
        print('Атака')


mas = Magican(10, 1)
mas.attack()
mas.hello()
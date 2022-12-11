"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:
    def __init__(self, space):
        self.space = space


class Star(SpaceObject):
    def __init__(self, space, light):
        super(Star, self).__init__(space)
        self.light = light

    def show_light(self):
        print(f'Яркость звезды: {self.light}')


class Planet(SpaceObject):
    def __init__(self, space, age, vec):
        super(Planet, self).__init__(space)
        self.age = age
        self.vec = vec

    def newAge(self):
        print(f'За один земной год возраст планеты увеличился на {self.vec} и теперь равен {self.age + self.vec}')
        self.age = self.age + self.vec


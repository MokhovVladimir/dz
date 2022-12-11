"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
import time, random


class Weapon():
    def __init__(self, name, power, endurance, procent):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.procent = procent
        self.reborn = endurance

    def recovery(self):
        self.endurance = self.reborn


Kingsbane = Weapon('Kingsbane', 6, 4, 80)
Gorehowl = Weapon('Gorehowl', 15, 4, 50)
Sulfuras = Weapon('Frostmorn', 10, 6, 90)
Swordfish = Weapon('Swordfish', 4, 10, 101)
dif_weapon = {Kingsbane.name: Kingsbane,
              Gorehowl.name: Gorehowl,
              Sulfuras.name: Sulfuras,
              Swordfish.name: Swordfish
              }

def show_weapon():
    print('Оружие на выбор:')
    for i in dif_weapon:
        print(f'Оружие {i}')
        print(f'Характеристики: \n'
              f'Урон: {dif_weapon[i].power}, Прочность: {dif_weapon[i].endurance}, Процент промаха: {100 // dif_weapon[i].procent}')
        print()
        time.sleep(1)


class Hero():
    def __init__(self, name, class_hero,  health, armor, rank):

        self.name = name
        self.class_hero = class_hero
        self.health = health
        self.armor = armor
        show_weapon()
        self.weapon = dif_weapon[input('Выберите оружие: ')]
        self.max_hp = health
        self.__rank = rank


    def setter(self):
        self.__rank = "Победитель арены"

    def getter(self):
        return self.__rank

    def deliter(self):
        del self.__rank

    def print_info(self):
        print(self.name)
        print(self.class_hero)


    def battle(self, enemy):
        print(f'{self.name} атакует -> {enemy.name} на {self.weapon.power}')
        if random.randint(1, 100) > self.weapon.procent == 0:
            print(f'Игрок {self.name} увернулся')
        else:
            enemy.armor -= self.weapon.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            self.weapon.endurance -= 1


    def pokazatel(self):
        print(f'Броня: {self.armor}')
        print(f'Здоровье {self.name}: {self.health}')


    def hero_power(self):
        self.armor += 4

    def lose(self):
        if self.health <= 0:
            print('Вы проиграли')

    def game(self, enemy):

        while self.health > 0 and enemy.health > 0:
            start = time.time()
            print(f'Ход {self.name}')
            while time.time() - start < 30:
                if self.weapon.endurance == 0:
                    print()
                    print('Выберите новое оружие и пропустите ход')
                    print()
                    time.sleep(1)
                    self.weapon.recovery()
                    show_weapon()
                    self.weapon = dif_weapon[input('Оружие: ')]
                    break
                else:
                    k = input('Введите ваше действие: ')
                    if k.lower() == 'удар':
                        self.battle(enemy)
                        break
                    elif k.lower() == 'сила героя':
                        self.hero_power()
                        break
                    elif k.lower() == 'инфо' or k.lower() == 'info':
                        print('Команда "удар" наносит урон равный атаке вашего оружия')
                        print('Команда "сила героя" добавляет вам 4 брони')
                        print('Команда "противник" показывает здоровье противника')
                        print('Команда "оружие" показывет урон и прочность оружия')
                        print()
                    elif k.lower() == 'противник':
                        enemy.pokazatel()
                    elif k.lower() == 'оружие':
                        print(f'Название {self.weapon.name}, Урон: {self.weapon.power}, Прочность: {self.weapon.endurance}')
                    elif k.lower() == 'kill':
                        enemy.health = 0
                    else:
                        print('Неизвестная команда')
                if enemy.health <= 0:
                    print(f'Победа игрока {self.name}')
                    if self.health + 5 < self.max_hp:
                        self.health = self.max_hp
                    else:
                        self.health += 5
                    break
            if enemy.health <= 0:
                break
            print()
            print('Смена хода')
            time.sleep(2)
            print()
            print(f'Ход {enemy.name}')
            enemy.pokazatel()
            time.sleep(1.5)

            enemy.hit(self)

            if self.health <= 0:
                print(f'Победа игрока {enemy.name}')
                self.lose()
                break
            time.sleep(1.5)


class Boss:
    def __init__(self, attack, hp, name, armor):
        self.name = name
        self.attack = attack
        self.health = hp
        self.armor = armor

    def hit(self, hero):
        print(f'{self.name} атакует -> {hero.name} на {self.attack}')
        hero.armor -= self.attack
        if hero.armor < 0:
            hero.health += hero.armor
            hero.armor = 0

    def pokazatel(self):
        print(f'Броня: {self.armor}')
        print(f'Здоровье {self.name}: {self.health}')



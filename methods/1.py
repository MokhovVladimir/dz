"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def new_person(cls, name):
        cls(name, today().datetime)

    @staticmethod
    def is_old_pers(person):
        return person.age >= 18

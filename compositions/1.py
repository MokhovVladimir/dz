"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""


class Profile:
    def __init__(self, name, last_name, age, pasport = ''):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.pasport = pasport

    def print_info(self):
        print(f'Yours last_name: {self.last_name}\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Passport: {self.pasport}')


class Address:
    def __init__(self, city = '', street = '', zipcode = ''):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:
    def __init__(self, role = '', hours_worked = 0):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount:
    def __init__(self, card_number = None, balance = 0):
        self.card_number = card_number
        self.balace = balance


class Order:
    def __init__(self):
        self.price = 0
        self.item = 0
        self.delivery = 0
        self.date = 0

    def new_order(self, price, items, delivery, date):
        self.date = date
        self.price = price
        self.item = items
        self.delivery = delivery

class User:
    def __init__(self, name, last_name, age, pasport = ''):
        self.profile = Profile(name, last_name, age, pasport)
        self.orders = []
        self.bank_account = []
        self.role = []
        self.address = []

    def add_adderss(self, city = '', street = '', zipcode = ''):
        self.address.append(Address(city, street, zipcode))

    def add_role(self, role = '', hours_worked = 0):
        self.role.append(Role(role, hours_worked))

"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class BankAccount():
    def __init__(self, name, balance, pasport, password):
        self.name = name
        self.__balance = balance
        self.__pasport = pasport
        self.__password = password

    def getbalce(self):
        return self.__balance

    def setbalance(self, newbalance):
        self.__balance += newbalance

    def delbalance(self):
        del self.__balance

    def setpasport(self, pasw, new_pas):
        if pasw == self.__password:
            self.__pasport = new_pas
        else:
            print('Вы ошиблись')

    def getpasport(self):
        return self.__pasport

    def delpasport(self, new_pas):
        if new_pas == self.__password:
            del self.__pasport
        else:
            print("Вы ошиблись")

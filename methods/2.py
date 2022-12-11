"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Координата x: {self.x} \nКоордината y: {self.y}\nКоордината z: {self.z}'

    def __add__(self, other):
        self.x = self.x + other.x
        self. y = self.y + other.y
        self.z = self.z + other.z
        return f'Новый вектор: \nКоордината x: {self.x} \nКоордината y: {self.y}\nКоордината z: {self.z}'

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.z = self.z - other.z
        return f'Новый вектор: \nКоордината x: {self.x} \nКоордината y: {self.y}\nКоордината z: {self.z}'

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

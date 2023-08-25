""" Задание №6
    📌 Доработайте прошлую задачу.
    📌 Добавьте сравнение прямоугольников по площади
    📌 Должны работать все шесть операций сравнения"""


class Square:

    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def square(self):
        """Метода, возвращающие площадь"""
        return self.length * self.width

    def perimetr(self):
        """Метода, возвращающие периметр"""
        return 2*(self.length + self.width)

    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Square(new_length, new_width)

    def __sub__(self, other):
        if self.length - other.length < 0 or self.width - other.width < 0:
            raise ValueError
        new_length = self.length - other.length
        new_width = self.width - other.width
        return Square(new_length, new_width)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() <= other.square()

    def __le__(self, other):
        return self.square() >= other.square()


square_1 = Square(10, 6)
square_2 = Square(2, 1)

square_3 = square_1 + square_2
square_4 = square_1 - square_2

print(square_3.perimetr())
print(square_4.perimetr())

print(square_1 > square_2)
print(square_1 < square_2)
print(square_1 == square_2)
print(square_1 != square_2)
print(square_1 >= square_2)
print(square_1 <= square_2)

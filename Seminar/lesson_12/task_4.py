""" Задание №4
    📌 Доработайте класс прямоугольник из прошлых семинаров.
    📌 Добавьте возможность изменять длину и ширину
       прямоугольника и встройте контроль недопустимых значений (отрицательных).
    📌 Используйте декораторы свойств."""


class Square:

    def __init__(self, a, b=None):
        self._lenght = a
        if b:
            self._width = b
        else:
            self._width = a

    @property
    def lenght(self):
        return self._lenght

    @property
    def width(self):
        return self._width

    @lenght.setter
    def lenght(self, value):
        if value > 0:
            self._lenght = value
        else:
            raise ValueError

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError

    def square(self):
        return self._lenght * self._width

    def perimeter(self):
        return 2*(self._lenght + self._width)


sq = Square(1, 2)
print(sq.square())
print(sq.perimeter())
sq.lenght = 5
print(sq.square())
print(sq.perimeter())
sq.lenght = -5
print(sq.square())
print(sq.perimeter())

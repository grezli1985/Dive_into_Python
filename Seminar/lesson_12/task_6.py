""" Задание №6
    📌 Изменяем класс прямоугольника.
    📌 Заменяем пару декораторов проверяющих длину и ширину
       на дескриптор с валидацией размера."""


class Value:

    def __init__(self, min_value=1):
        self.min_value = min_value

    def __set_name__(self, owner, name):  # length width
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')


class Square:

    # __slots__ = ['_lenght', '_width']
    _length = Value(1)
    _width = Value(1)

    def __init__(self, a, b=None):
        self._lenght = a
        if b:
            self._width = b
        else:
            self._width = self._lenght

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


sq = Square(1, -2)
print(sq.square())
print(sq.perimeter())
sq.lenght = 5
print(sq.square())
print(sq.perimeter())

sq.size = 20
print(sq.size)

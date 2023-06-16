import decimal
import math
from decimal import Decimal, getcontext

"""Задание №4
    ✔ Напишите программу, которая вычисляет площадь
      круга и длину окружности по введённому диаметру.
    ✔ Диаметр не превышает 1000 у.е.
    ✔ Точность вычислений должна составлять
      не менее 42 знаков после запятой."""

# S = π * D**2/4


getcontext().prec = 42

diametr = float(input('Введите диаметр: '))


def circle(diametr):
    result = diametr * math.pi
    area = ((diametr / 2) ** 2) * math.pi
    return Decimal(result), Decimal(area)


print(circle(diametr))
print(len(str(diametr)))

# def circle(d: decimal) -> tuple[decimal, decimal]:
#     decimal.getcontext().prec = 42
#     _pi = decimal.Decimal(math.pi)
#     if d <= 1000:
#         s = (_pi * d ** 2) / 4
#         l = _pi * d
#
#     return decimal.Decimal(s), decimal.Decimal(l)
#
# print(circle(5))

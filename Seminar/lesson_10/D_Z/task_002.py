"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить
является ли треугольник разносторонним, равнобедренным или равносторонним."""


# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))
#
# if a <= b + c and b <= a + c and c <= a + b:
#     print('Треугольник существует')
#     if a == b == c:
#         print('Треугольник равносторонний')
#     elif a == b or b == c or c == a:
#         print('Треугольник равнобедренный')
#     else:
#         print('Треугольник разносторонний')
# else:
#     print('треугольника с такими сторонами не существует')


class Triangle:
    # a = int(input('Введите a: '))
    # b = int(input('Введите b: '))
    # c = int(input('Введите c: '))

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    @staticmethod
    def triangle_check(side_a, side_b, side_c):
        if side_a <= side_b + side_c and side_b <= side_a + side_c and side_c <= side_a + side_b:
            print('Треугольник существует')
            if side_a == side_b == side_c:
                return print('Треугольник равносторонний')
            elif side_a == side_b or side_b == side_c or side_c == side_a:
                return print('Треугольник равнобедренный')
            else:
                return print('Треугольник разносторонний')
        else:
            return print('треугольника с такими сторонами не существует')


a = int(input('Введите side_a: '))
b = int(input('Введите side_b: '))
c = int(input('Введите side_c: '))

triangle = Triangle(a, b, c)
print(triangle.triangle_check(a, b, c))

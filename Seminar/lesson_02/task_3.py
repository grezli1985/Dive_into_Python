"""Задание №3
    ✔ Напишите программу, которая получает целое число и возвращает
      его двоичное, восьмеричное строковое представление.
    ✔ Функции bin и oct используйте для проверки своего
      результата, а не для решения.

Дополнительно:

    ✔ Попробуйте избежать дублирования кода
      в преобразованиях к разным системам счисления
    ✔ Избегайте, магических чисел
    ✔ Добавьте, аннотацию типов, где это возможно"""

number = int(input('Введите десятичное число: '))

b = bin(number)
o = oct(number)
h = hex(number)
print(b, o, h, sep='\n')


def gonext(number, sustem):
    result = 0
    ost = 0
    rezString = ''
    while True:
        result = number // sustem
        ost = number % sustem
        if result < sustem:
            rezString = rezString + str(ost) + str(result)
            break
        else:
            number = result
            rezString = rezString + str(ost)
    return rezString[::-1]


print(gonext(number, 2))
print(gonext(number, 8))


# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits): return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result
#
# print(convert_to(10, 2))
# print(convert_to(10, 8))
# print(convert_to(10, 16))

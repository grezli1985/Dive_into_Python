"""Задача 1

    ✔ Напишите программу, которая получает целое
      число и возвращает его шестнадцатеричное
      строковое представление. Функцию hex
      используйте для проверки своего результата."""

number = int(input('Введите десятичное число: '))

b = bin(number)
o = oct(number)
h = hex(number)
print(b, o, h, sep='\n')

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

print(convert_to(number, 2))
print(convert_to(number, 8))
print(convert_to(number, 16))

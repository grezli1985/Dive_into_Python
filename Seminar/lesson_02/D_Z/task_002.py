import fractions

"""Задача 2

    ✔ Напишите программу, которая принимает две строки
      вида “a/b” — дробь с числителем и знаменателем.
      Программа должна возвращать сумму
      и произведение дробей. Для проверки своего
      кода используйте модуль fractions"""

a = int(input('Введите 1-й числитель: '))
b = int(input('Введите 1-й знаменатель: '))
c = int(input('Введите 2-й числитель: '))
d = int(input('Введите 2-й знаменатель: '))


def plus(a, b, c, d):
    if b != d:
        m = a * d + c * b
        n = b * d
    else:
        m = a + c
        n = b

    for i in range(2, max(m, n) + 1):
        if m % i == 0 and n % i == 0:
            m //= i
            n //= i

    print('{}/{}'.format(m, n))


def multiply(a, b, c, d):
    m = a * c
    n = b * d

    for i in range(2, max(m, n) + 1):
        if m % i == 0 and n % i == 0:
            m //= i
            n //= i

    return print('{}/{}'.format(m, n))


f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)

plus(a, b, c, d)
multiply(a, b, c, d)
print()
print(f1 + f2)
print(f1 * f2)

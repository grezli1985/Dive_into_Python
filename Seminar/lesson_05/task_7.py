""" Задание №7 """
""" ✔ Создайте функцию-генератор.
    ✔ Функция генерирует N простых чисел,
    начиная с числа 2.
    ✔ Для проверки числа на простоту используйте
    правило: «число является простым, если делится
    нацело только на единицу и на себя»."""


def is_prime(number):
    if number == 1:
        return False
    if number % 2 == 0:
        return False
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def numerated_generator(N: int):
    count = 1
    i = 2
    while count <= N:
        if i == 2:
            yield 2
            count += 1
        if is_prime(i):
            yield i
            count += 1
        i += 1


l = numerated_generator(100)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print()
print(len([*l]))

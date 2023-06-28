""" Задание 3 """
""" ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""

num = int(input('Введи число от 1 до 100: '))


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        b = a + b
        a = b - a


print(list(fib(num)))


# def fibonacci(n):
#     """Функция Фибоначчи"""
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print([fibonacci(n) for n in range(num)])

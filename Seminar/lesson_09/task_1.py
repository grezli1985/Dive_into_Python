""" Задание №1
📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
    ○ от 1 до 100 для загадывания,
    ○ от 1 до 10 для количества попыток

📌 Функция возвращает функцию, которая через консоль просит
    угадать загаданное число за указанное число попыток. """
from typing import Callable
from random import randint


def outer() -> Callable:
    num_range = int(input('Введите диапазон от 1 до 100: '))
    attempts = int(input('Введите число попыток (1 -- 10): '))
    num_sc = randint(1, num_range)

    def inner() -> None:
        nonlocal num_range, attempts
        while attempts:
            print(f'{attempts}-я попытка.', end=' ')
            attempts -= 1
            num = int(input('Введите число: '))
            if num == num_sc:
                print(f'Номер найден: {num}')
                break
            else:
                advice = ['больше', 'меньше']
                print(f'Ваше число {advice[num > num_sc]}')
        else:
            print(f'Ты проиграл. Правильный номер {num_sc}')
    return inner


def main():
    game = outer()
    game()


if __name__ == '__main__':
    main()







# import random
#
#
# def count(num: int = 1):
#     def deco(func):
#         def wrapper(*args, **kwargs):
#             result = random.randint(0, 100)
#             print(result)
#             for _ in range(num):
#                 if result < func(*args, **kwargs):
#                     print('Введите число меньше')
#                 elif result > func(*args, **kwargs):
#                     print('Введите число больше')
#                 else:
#                     print('YES!!! Вы угадали')
#                     break
#             return result
#         return wrapper
#     return deco
#
#
# @count(10)
# def guess():
#     my_guess = int(input('Введите число от 0 до 100 '))
#     return my_guess
#
#
# print(guess())

""" Задание №2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декораторе.
📌 Он должен проверять входят ли переданные в функцию угадайку числа
    в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами из диапазонов."""
from typing import Callable
from random import randint


def outer(func: Callable) -> Callable:

    def wrapper(guess: int, attempts: int):
        if 1 < guess < 100:
            guess = guess
        else:
            randint(1, 100)
        if 1 < attempts < 10:
            attempts = attempts
        else:
            randint(1, 10)
        return func(guess, attempts)
    return wrapper


@outer
def game_guess(num_sc, attempts) -> None:
    while attempts:
        print(f'{attempts} попыток.', end=' ')
        attempts -= 1
        num = int(input('Введите число: '))
        if num == num_sc:
            print(f'Число найдено: {num}')
            break
        else:
            advice = ['больше', 'меньше']
            print(f'Ваше число {advice[num > num_sc]}')
    else:
        print(f'Ты проиграл. Правильный номер {num_sc}')


if __name__ == '__main__':
    game_guess(200, 300)

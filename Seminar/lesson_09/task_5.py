""" Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
    ○ декораторами для сохранения параметров,
    ○ декоратором контроля значений и
    ○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов."""
import json
import os
from random import randint
from typing import Callable


def counter(number):
    def dec(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(number):
                print(f'Игра началась!-{i + 1}')
                results.append(func(*args, **kwargs))

            return tuple(results)
        return wrapper
    return dec


def checker(func: Callable) -> Callable:

    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        return func(guess, attempts)
    return wrapper


def writer(file_name) -> Callable:

    def inner_func(func):

        def wrapper(number, tries):
            my_dict = {str(func(number, tries)): (number, tries)}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=4, ensure_ascii=False)
            return func(number, tries)
        return wrapper
    return inner_func

@counter(3)
@writer('game_guess.json')
@checker
def game_guess(num_sc, attempts):

    result_attempts = 1
    while attempts:
        print(f'{attempts} попыток.', end=' ')
        attempts -= 1
        num = int(input('Введите число: '))
        if num == num_sc:
            print(f'Число найдено: {num}')
            return result_attempts
        else:
            advice = ['больше', 'меньше']
            print(f'Ваше число {advice[num > num_sc]}')
            result_attempts += 1
    else:
        print(f'Ты проиграл. Правильный номер {num_sc}')

    return result_attempts


if __name__ == '__main__':
    game_guess(10, 567)

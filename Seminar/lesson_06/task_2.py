""" Задание №2
    📌 Создайте модуль с функцией внутри.
    📌 Функция принимает на вход три целых числа: нижнюю и верхнюю
       границу и количество попыток.
    📌 Внутри генерируется случайное число в указанных границах и
       пользователь должен угадать его за заданное число попыток.
    📌 Функция выводит подсказки “больше” и “меньше”.
    📌 Если число угадано, возвращается истина, а если попытки исчерпаны - ложь."""

import random


def guess(tries=3, maximum=10,  minimum=1):  # Все значения поо умолчанию идут справа, не прерываясь
    number = random.randint(minimum, maximum)
    while tries:
        answer = int(input('Какое число загадано? '))
        if answer == number:
            print('Вы угадали!')
            break
        else:
            if answer > number:
                print('меньше')
            else:
                print('больше')
        tries -= 1

    else:
        print('Вы не угадали( ')
        print('Было загадано ', number)


if __name__ == '__main__':
    guess(1, 10, 3)

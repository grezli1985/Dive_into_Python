"""Задание №1
    📌 Напишите программу, которая использует модуль logging для
       вывода сообщения об ошибке в файл.
    📌 Например отлавливаем ошибку деления на ноль."""
import logging
import random


def by_zero():
    number = int(input('Введите целое число: '))
    if number == 0:
        logging.basicConfig(filename='for_log.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
        logging.info('ZeroDivisionError: division by zero')
    for_number = random.randint(1, 100)/number
    return for_number


by_zero()

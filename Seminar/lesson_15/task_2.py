"""Задание №2
    📌 На семинаре про, декораторы был создан логирующий декоратор.
       Он сохранял аргументы функции и результат её работы в файл.
    📌 Напишите аналогичный декоратор, но внутри используйте
       модуль logging."""
import logging
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='log_factorial.log',
                            encoding='utf-8',
                            level=logging.DEBUG)
        logging.info(f'Запуск функции {func.__name__} с аргументом {args}')
        result = func(*args, **kwargs)
        logging.info(f'Результат функции {func.__name__}: {result}')
        logging.info(f'Завершение функции {func.__name__}')
        return result

    return wrapper


@main
def my_factorial(number: int):
    if number == 1:
        return 1
    else:
        return number * my_factorial(number - 1)


if __name__ == '__main__':
    print(my_factorial(8))

"""Задание №3
    📌 Доработаем задачу 2.
    📌 Сохраняйте в лог файл раздельно:
        ○ уровень логирования,
        ○ дату события,
        ○ имя функции (не декоратора),
        ○ аргументы вызова,
        ○ результат."""
import logging
from datetime import datetime
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='log_factorial_1.log',
                            encoding='utf-8',
                            level=logging.DEBUG)
        my_datetime = datetime.now()
        logging.info(f'Запуск функции {func.__name__} с аргументом {args} дата {my_datetime}')
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

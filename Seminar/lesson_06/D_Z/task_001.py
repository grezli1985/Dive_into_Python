""" Задание №1
📌 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
даты на проверку."""
import sys
from sys import argv


def _leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True


def my_date(data: str):
    day, month, year = list(map(int, data.split('.')))
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            return _leap_year(year) and day <= 2


if __name__ == '__main__':
    print(my_date('25.12.1986'))
    print(my_date('29.2.2023'))
    print(my_date('29.2.2020'))
    print(my_date('32.5.2020'))

    if len(argv) == 2:
        _, date = argv
        print(my_date(date))
    else:
        print("Дата для проверки не указана!")

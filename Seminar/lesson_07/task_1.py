""" Задание №1"""
import random

""" ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
    ✔ Первое число int, второе - float разделены вертикальной чертой.
    ✔ Минимальное число - -1000, максимальное - +1000.
    ✔ Количество строк и имя файла передаются как аргументы функции. """


def new_file(strings_number, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(strings_number):
            intput_numbers = (str(random.randint(-1000, 1001)), str(random.uniform(-1000, 1001)))
            f.write(" | ".join(intput_numbers) + "\n")


if __name__ == '__main__':
    new_file(10, "file.txt")

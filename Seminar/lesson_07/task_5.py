""" Задание №5 """
import random
from random import randint, randbytes, sample, choice
from string import ascii_letters
import os

""" ✔ Доработаем предыдущую задачу.
    ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
    ✔ Расширения и количество файлов функция принимает в качестве параметров.
    ✔ Количество переданных расширений может быть любым.
    ✔ Количество файлов для каждого расширения различно.
    ✔ Внутри используйте вызов функции из прошлой задачи."""


def random_extension(list_ext: list[str]) -> str:
    return random.choice(list_ext)


def create_file(extension: list[str], min_name: int = 6, max_name: int = 30,
                min_size: int = 256, max_size: int = 4096, amount: int = 42):
    for _ in range(amount):
        name_size = randint(min_name, max_name)
        ext = random_extension(extension)
        file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
        file_name = os.path.join('D_Z/data', file_name)
        with open(file_name, 'ab') as file:
            size = randint(min_size, max_size)
            result = randbytes(size)
            file.write(result)


create_file(['txt', 'doc', 'md', 'rtf'], amount=12)

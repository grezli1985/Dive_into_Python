import os

""" Задание 1 """
""" ✔ Напишите функцию, которая принимает на вход строку —
    абсолютный путь до файла. Функция возвращает кортеж из трёх
    элементов: путь, имя файла, расширение файла."""


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


p = os.path.abspath('file.txt ')
print(file_info(p))

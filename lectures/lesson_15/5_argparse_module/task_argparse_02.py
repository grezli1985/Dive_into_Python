"""Создаём парсер, ArgumentParser
При создании экземпляра из класса ArgumentParser можно 13 различных
аргументов. Но большинство из них имеют оптимальные настройки по умолчанию.
Если что-то и стоит добавить, то дополнительное описание, которое выводится при
вызове справки."""
import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser',
                                 epilog='Returns the arithmetic mean')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

"""
Пример запуска в терминале:
python task_argparse_02.py --help


● prog — заменяет название файла в первой строке справки на переданное имя,
● description — описание в начале справки
● epilog — описание в конце справки"""

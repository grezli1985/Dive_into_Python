"""Рассмотрим ещё один вариант полиморфизма."""

path_1 = '/home/user'
path_2 = '/my_project/workdir'
result = path_1 / path_2  # TypeError: unsupported operand type(s) for /: 'str' and 'str'

"""Python не поддерживает деление строк. Но мы уже сталкивались с тем как класс
Path из модуля pathlib создавал новый путь используя символ деления. """

"""Методы __init__ и __str__ в классах своих
исключений
Чтобы исключение давало подробную информацию об ошибке, будем передавать
ему проблемную переменную. Класс User доработаем в строках подъёма ошибок."""
from task_error_01 import UserNameError, UserAgeError


class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise UserNameError(name)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User('Яков', '-12')

"""Благодаря наследованию переданные в исключение переменные могут выводится
в тексте ошибки.
raise UserNameError(name)
error.UserNameError: Яков"""

"""🔥 Внимание! В классе User надо исправит строку вызова ошибки имени,
чтобы код сработал верно. Иначе исключение вернёт нам исключение
TypeError: UserNameError.__init__() missing 2 required positional arguments:
'lower' and 'upper'
...
def __init__(self, name, age):
if self.MIN_LEN < len(name) < self.MAX_LEN:
self.name = name
else:
raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
..."""
from task_error_04 import UserNameError, UserAgeError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User('Яков', '-12')

""" Задание №3
    📌 Создайте класс с базовым исключением и дочерние классы исключения:
        ○ ошибка уровня,
        ○ ошибка доступа."""


class ErrorDefault(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self):
        return 'Я родился'


class ErrorLevel(ErrorDefault):
    def __str__(self, string: str = '') -> str:
        return 'Error level ' + string


class ErrorAccess(ErrorDefault):
    def __str__(self, string: str = '') -> str:
        return 'Error Access ' + string


d = 0
raise ErrorAccess('error')

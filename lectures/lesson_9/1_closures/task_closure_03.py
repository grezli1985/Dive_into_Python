from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str


print(add_one_str('Hello')('world!'))

"""Результат получили такой же, но код работает иначе.

    ● Функция add_one_str принимает на вход один параметр в качестве начала
      строки и возвращает локальную функцию add_two_str. Обратите внимание на
      отсутствие круглых скобок. Функцию передаём , а не вызываем.
    ● Функция add_two_str принимает вторую часть строки, соединяет её с первой
      и возвращает ответ.
    ● При вызове функций значения указывается в отдельных круглых скобках.
      Первое попадает в параметр a. Далее часть строки: add_one_str('Hello')
      возвращает функцию add_two_str и уже она вызывается и принимает
      аргумент во вторых скобках.
    
Благодаря передаче одной функции другой мы можем создавать замыкания."""

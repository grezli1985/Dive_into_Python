""" Что такое замыкания?"""
""" Области видимости и функции первого класса
Замыкание (англ. closure) в программировании — функция первого класса,
в теле которой присутствуют ссылки на переменные, объявленные вне тела
этой функции в окружающем коде и не являющиеся её параметрами."""

""" Области видимости """


def func(a):
    x = 1
    res = x + a
    return res


x = 100
print(func(5))

"""В этом примере глобальная переменная x равна 73, но при сложении внутри
функции к значению a прибавляется 42 — значение локальной переменной x."""
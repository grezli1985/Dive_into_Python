""" Функция как объект высшего порядка
Рассмотрим, простой пример функции: """


def add_str(a: str, b: str) -> str:
    return a + ' ' + b


print(add_str('Hello', 'world!'))

"""На вход передаём две строки и возвращаем новую из двух старый и пробела
посередине. Но функцию можно переписать иначе. Вспомним, что в Python все
функции высшего порядка. А это значит, что их можно передавать как объекты в
другие функции:"""

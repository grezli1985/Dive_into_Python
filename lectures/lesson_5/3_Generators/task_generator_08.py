""" Dict comprehensions """
"""Ещё один вариант синтаксического сахара — генерация словаря."""

my_dictcomp = {i: chr(i) for i in range(97, 123)}       # генерации словаря {key: value }
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')

"""Запись похожа на создание множества, но в качестве выражения для добавления
указываются две переменные через двоеточие: key: value. Благодаря такой записи
Python понимает, что надо создать словарь.

🔥 Важно! Стоит помнить, что ключи словаря должны быть объектами неизменяемого типа.
Во всём остальном для генерации словарей в одну строку действуют те же правила,
что и для других типов данных."""

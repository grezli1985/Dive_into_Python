""" ● Функция filter() """
"""filter(function, iterable) — принимает на вход функцию и последовательность. Если
функция возвращает истину, элемент остаётся в последовательности. Как и map
возвращает объект итератор."""

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)

"""Лямбда фильтрует элементы больше нуля. Функция tuple преобразует итератор к
кортежу с положительными числами."""
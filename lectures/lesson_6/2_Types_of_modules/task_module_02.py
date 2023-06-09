""" Варианты импорта
Рассмотрим, особенности импорта пакетов и модулей."""

from mathematical import base_math

x = base_math.div(10, 2)
print(x)

"""Если импортировать пакет верхнего уровня, для работы с функциями необходимо
указать всю цепочку через точечную нотацию: имя пакета, имя модуля, имя
объекта.
Для сокращения объема кода обычно импортируют нужные модули или объекты
модуля через точечную нотацию после import."""

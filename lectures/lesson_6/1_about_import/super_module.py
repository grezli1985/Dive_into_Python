""" Плохой import * (импорт звёздочка)
Ещё один вариант импорта: from имя_модуля import *
Подобная запись импортирует из модуля все глобальные объекты за исключением
тех, чьи имена начинаются с символа подчёркивания. Рассмотрим на примере.
● Файл super_module.py"""
from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)

""" В модуле есть следующие объекты:
● глобальная функция randint
● глобальная константа SIZE
● глобальная защищенная переменная _secret
● глобальная приватная переменная __top_secret
● глобальная функция func
● локальные параметры функции a и b
● локальная переменная функции z
● глобальная переменная result

🔥 Внимание! Если название объекта (переменной, функции и т.п.)
начинается с символа подчёркивания, объект становится защищённым. Если
имя начинается с двух подчёркиваний, объект становится приватным. Объекты
без подчёркивания в начале имени — публичные. Подробнее разберём на
лекциях по ООП."""


""" Переменная __all__

✔ __all__ = ['func', '_secret', '...']
Cписок имён объектов, заключённых в кавычки,
т.е. строки для импорта через «звёздочку».

При необходимости разработчик модуля может явно указать какие объекты нужно
импортировать при использовании стиля from module import *. Для этого
используется магическая переменная __all__ (два нижних подчёркивания до, слово
all и два нижних подчёркивания после). Изменим код модуля super_module.py,
добавив строку с __all__

Переменной __all__ присваивается список имён объектов, заключённых в кавычки,
т.е. str типа. В основной модуль попадут только указанные в списке имена,
независимо от того являются они публичными, защищёнными или приватными. При
этом объект должен быть глобальным. Если указать в списке имя локального
объекта, например переменную z — локальную переменную функции func, получим
ошибку.

Список __all__ в приведённом примере используется для формирования списка
импортируемых объектов модуля. Кроме этого __all__ применяется для импорта
модулей из пакета. Рассмотрим вариант импорта модулей из пакета далее на
лекции."""
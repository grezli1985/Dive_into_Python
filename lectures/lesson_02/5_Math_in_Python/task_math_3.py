import fractions

""" Математические модули

В Python есть несколько модулей в стандартной
библиотеке, которые облегчают математические
расчёты. Для доступа к ним необходимо выполнить
импорт в начале файла.
import math
import decimal
import fractions"""

""" Модуль fraction

Запись дробей вида ⅓, ⅗ и т.п.
f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)"""

f1 = fractions.Fraction(1, 3)
print(f1)                           # 1/3
f2 = fractions.Fraction(3, 5)
print(f2)                           # 3/5
print(f1 * f2)                      # 1/5

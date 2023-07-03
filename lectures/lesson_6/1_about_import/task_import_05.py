""" Кроме выборочного импорта можно создавать псевдонимы для объектов через
зарезервированное слово as. При этом доступ к объекту будет возможен только
через псевдоним. Один объект — одно имя."""
import random as rnd
from sys import builtin_module_names as bmn, path as p

print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
print(path)  # NameError: name 'path' is not defined
print(sys.path)  # NameError: name 'sys' is not defined

"""В первой строке импортировали модуль random и присвоили ему имя rnd внутри
текущей области видимости. Во второй строке импортировали переменную
builtin_module_names под именем bmn и переменную path под именем p. Последние
две строки вызывают ошибку имени. Мы не можем обратиться к переменной path,
потому что дали ей другое имя — p. И обращение к модулю sys не работает, ведь мы
его не импортировали. Только объекты из модуля.

🔥 Важно! Не стоит давать переменным короткие понятные лишь вам
имена. Код должен легко читаться другими разработчиками. Исключения —
общепризнанные сокращения, например import numpy as np."""
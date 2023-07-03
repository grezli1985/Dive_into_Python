""" Использование from и as
Помимо обычного импорта можно использовать более подробную форму записи.
Зарезервированное слово from указывает на имя модуля или пакета, далее import и
имена импортируемых объектов. """

from sys import builtin_module_names, path

print(builtin_module_names)
print(*path, sep='\n')

"""Теперь при обращении к импортированным объектам не нужно указывать имя
модуля. Мы явно добавили их в наш код, включили имена в область видимости.

💡 PEP-8! Конструкция from import допускает перечисление импортируемых
имён объектов через запятую в одной строке. После from всегда указывается
один модуль."""

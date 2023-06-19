""" Метод format """
""" Метод формат является строковым методом и позволяет соединять заранее
заготовленный текст с переменными. Долгое время был основным способом
форматирования. До версии Python 3.6, если быть точным."""

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)     # Меня зовут Alex и мне 12 лет

""" В строке используются фигурные скобки как место для подстановки значений.
Далее для строки вызывается метод format. В качестве аргументов метод получает
нужное количество переменных."""

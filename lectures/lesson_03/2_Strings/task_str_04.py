""" Форматирование через % """
""" Форматирование с использованием символа % является старым способом указания
формата. Его вы можете встретить в коде, который писали очень давно. В
настоящее время он используется лишь в некоторых модулях для задания формата
вывода данных."""

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)     # Меня зовут Alex и мне 12 лет

""" В строке текста используется знак % с символом типа после него. s — строка, d —
число и т.п. После строки указывается символ % и перечисляются переменные. Если
переменных больше одной, они заключаются в круглые скобки и разделяются
запятой — передаётся кортеж."""
"""Размер строки в памяти

object.__sizeof__() — метод возвращает
размер объекта в байтах

Размер строки в памяти. 48 байт служебной
информации для х64 Python. Далее 1, 2
или 4 байта на каждый символ в зависимости
от кодировки"""

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())       # 49
print(en_str.__sizeof__())          # 53
print(ru_str.__sizeof__())          # 84
print(unicode_str.__sizeof__())     # 92

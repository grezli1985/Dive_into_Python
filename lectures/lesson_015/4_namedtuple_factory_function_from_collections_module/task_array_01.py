"""Модуль array
А вот ещё один модуль, предоставляющий доступ к типу данных массив. Как вы
помните список list является массивом ссылок на объекты. А сами объекты хранятся
отдельно, вне массива. array из модуля array является классическим массивом.
Внутри него можно хранить целые или вещественные числа, а также символы
Unicode."""
from array import array, typecodes

byte_array = array('B', (1, 2, 3, 255))

print(byte_array)   # array('B', [1, 2, 3, 255])
print(typecodes)    # bBuhHiIlLqQfd

"""Первый аргумент — строковой символ код типа. Буква указывает на то какие
данные хранятся в массиве и выделяет нужное число байт под данные.
Вторым аргументом передают последовательность для помещения в массив.

Переменная typecodes выводит все допустимые коды типа:

● 'b' — целое со знаком, 1 байт
● 'B' — целое без знака, 1 байт
● 'u' — Юникод-символ в 2 или 4 байта
● 'h' — целое со знаком, 2 байта
● 'H' — целое без знака, 2 байта
● 'i' — целое со знаком, 4 байта
● 'I' — целое без знака, 4 байта
● 'l' — целое со знаком, 4 байта
● 'L' — целое без знака, 4 байта
● 'q' — целое со знаком, 8 байт
● 'Q' — целое без знака, 8 байт
● 'f' — вещественное обычной точности, 4 байта
● 'd' — вещественное двойной точности, 8 байт"""

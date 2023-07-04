""" Работа с каталогами
Операции по работе с файлами и папками должны иметь полный, абсолютный путь
к объекту начиная от корневой директории. Или же можно задать относительный
путь. Так мы делали в первой части лекции. Файл с кодом и файлы для чтения и
записи находились в одном каталоге.
● Текущий каталог
Для получения информации о текущем каталоге можно использовать модуль os или pathlib"""
import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())

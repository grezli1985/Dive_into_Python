'''
        Целые числа
✔ int(x, base=10) — возвращает целочисленный
  объект, созданный из числа или строки x,
  или возвращает значение 0, если аргументы
  не заданы. base — основание системы счисления,
  от 2 до 36.
'''


x = int("42")                   # 42
y = int(3.1415)                 # 3
z = int("hello", base=30)       # 14167554
print(x, y, z, sep='\n')
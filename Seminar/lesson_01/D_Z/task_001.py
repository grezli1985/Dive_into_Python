#   Задание №8
# Нарисовать, в консоли ёлку спросив
# у пользователя количество рядов.
#   Пример результата:
#  Сколько рядов у ёлки? 5
#                 *
#                ***
#               *****
#              *******
#             *********

num = int(input('Введите Сколько рядов у ёлки: '))
count = num
for i in range(1, num + 1):
    print(' ' * count + '*' * i + '*' * (i - 1) )
    count -= 1
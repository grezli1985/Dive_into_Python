# Задание №7
#   Пользователь вводит число от 1 до 999. Используя операции с числами
#   сообщите что введено: цифра, двузначное число или трёхзначное число.
#   Для цифры верните её квадрат, например 5 - 25
#   Для двузначного числа произведение цифр, например 30 - 0
#   Для трёхзначного числа его зеркальное отображение, например 520 - 25
#   Если число не из диапазона, запросите новое число.
#   Откажитесь от магических чисел
#   В коде должны быть один input и один print

# while True:
#     num = int(input('Введите число от 1 до 999: '))
#     lenght = 0
#     res = 0
#     if num > 0 and num < 1000:
#         break
#         # length = -1
# if 0 < num < 10:
#     lenght = 'цифра'
#     res = num ** 2
# elif 9 < num < 100:
#     lenght = 'двузначное число'
#     res = (num % 10) * (num // 10)
# else:
#     lenght = 'трёхзначное число'
#     a = num // 100
#     b = num // 10 % 10
#     c = num % 10
#     res = c * 100 + b * 10 + a
#
# print('введено ', lenght, num, ' - ', res)

while True:
    num = int(input('Введите число от 1 до 999: '))
    if 0 < num < 1000:
        break
if 0 < num < 10:
    lenght = 'цифра'
    res = num ** 2
elif 9 < num < 100:
    lenght = 'двузначное число'
    res = (num % 10) * (num // 10)
else:
    lenght = 'трёхзначное число'
    res = num % 10 * 100 + (num // 10 * 10 - num // 100 * 100) + num // 100

print('введено ', lenght, num, ' - ', res)

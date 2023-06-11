""" Напишите код, который запрашивает число и сообщает,
является ли оно простым или составным.
Используйте правило для проверки: “Число является простым,
если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """


while True:
    num = int(input('Введите число от 1 до 100000: '))
    if 0 < num < 100001:
        break
simpl = True
i = 2
while i < num:
    if num % i == 0:
        simpl = False
    i += 1
if simpl:
    print('является простым')
else:
    print('не является')



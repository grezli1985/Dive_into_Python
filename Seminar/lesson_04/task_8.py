""" Задание №8 """

""" ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
    ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
      оканчивающихся на s (кроме переменной из одной буквы s) на None.
    ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""

max_ = 0
my_strings = 'ffff'
numbers = 89
s = 'Супер'

print('\nДо изменения\n')
# for var, value in globals().copy().items():
#     if not var.startswith('__'):
#         print(var, value)
print(f'{max_=}')
print(f'{my_strings=}')
print(f'{numbers=}')
print(f'{s=}')

for item in globals().copy():
    if not item.startswith('__'):
        if item.endswith('s'):
            if len(item) > 1:
                new_name = item[:-1]
                globals()[new_name] = None
            else:
                globals()[item] = globals().get(item)

print('\nПосле изменения\n')
# for var, value in globals().copy().items():
#     if not var.startswith('__'):
#         print(var, value)
print(f'{max_=}')
print(f'{my_strings=}')
print(f'{numbers=}')
print(f'{s=}')
print(f'{my_string=}')
print(f'{number=}')
print(globals())

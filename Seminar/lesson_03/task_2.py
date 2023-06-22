""" Задание №2

Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
    ✔ Целое положительное число
    ✔ Вещественное положительное или отрицательное число
    ✔ Строку в нижнем регистре, если в строке есть
    хотя бы одна заглавная буква
    ✔ Строку в нижнем регистре в остальных случаях"""

user_input = input('Введите данные: ')

if user_input.isdigit():
    print('Целое положительное число: ', user_input)

elif user_input.replace(".", "").replace("-", "").isdigit():
    print('Вещественное положительное или отрицательное число: ', user_input)

elif user_input == user_input.lower():
    print('Строку в нижнем регистре: ', user_input)
else:
    print('в строке есть хотя бы одна заглавная буква: ', user_input)
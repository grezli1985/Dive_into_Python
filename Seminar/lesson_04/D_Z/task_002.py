""" Задание 2 """
""" ✔ Напишите функцию принимающую на вход только ключевые
      параметры и возвращающую словарь, где ключ — значение
      переданного аргумента, а значение — имя аргумента. Если
      ключ не хешируем, используйте его строковое представление."""


# def returning_dictionary(one, two):
#     dictum = {
#         f'{one}': id(one),
#         f'{two}': id(two)
#     }
#     return dictum
#
#
# a = 4
# b = 8
#
# print(temp := returning_dictionary(a, b))

def function_dict(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


print(function_dict(a=1, b=2))
print(function_dict(a=1, b=[1, 2]))
print(function_dict(arg1="Hello", arg2=2, arg3="123", arg4=[1, 2, 3, 4, 5]))

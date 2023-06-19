""" Работа со словарями """
""" Метод values() - возвращает объект-итератор dict_values

Метод values похож на keys, но возвращает значения в виде объекта итератора
dict_values, а не ключи."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())             # dict_values([1, 2, 3, 4, 10])
for value in my_dict.values():
    print(value)                    # 1
                                    # 2
                                    # 3
                                    # 4
                                    # 10

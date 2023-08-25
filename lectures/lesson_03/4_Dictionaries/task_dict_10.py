""" Работа со словарями """
""" Метод pop() - Удаляет пару ключ-значение по ключу"""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')     # spam = 2	my_dict={'one': 1, 'three': 3, 'four': 4, 'ten': 10}
# err = my_dict.pop('six')    # KeyError: 'six'
# err = my_dict.pop()         # TypeError: pop expected at least 1 argument, got 0

""" Если указать несуществующий ключ, получим ошибку KeyError. В отличии от метода
pop у списков list, dict.pop вызовет ошибку TypeError. Для удаление последнего
элемента нужен метод popitem."""
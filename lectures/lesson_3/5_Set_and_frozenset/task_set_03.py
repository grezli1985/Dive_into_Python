""" Работа с множествами """
""" Метод remove() - Удаляет элемент

Для удаления элемента множества используют метод remove."""

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)       # {1, 2, 3, 4, 6, 7}
my_set.remove(10)   # KeyError: 10

""" При передаче несуществующего объекта получим ошибку KeyErro"""
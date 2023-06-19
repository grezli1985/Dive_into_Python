""" Функция sorted() """

""" Функция sorted принимает на вход любую коллекцию по которой можно
итерироваться и возвращает отсортированный список.

🔥 Важно! Функция sorted может принимать не только списки, но и другие
последовательности: строки, множества, кортежи, словари и т.п.. При этом
функция всегда возвращает список."""

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)                 # [4, 8, 2, 9, 1, 7, 2]
print(my_list, sort_list, sep='\n')         # [1, 2, 2, 4, 7, 8, 9]
rev_list = sorted(my_list, reverse=True)    # [4, 8, 2, 9, 1, 7, 2]
print(my_list, rev_list, sep='\n')          # [9, 8, 7, 4, 2, 2, 1]

""" Переданная в функцию коллекция остаётся неизменной после результата работы
функции. Если в функцию передать дополнительный аргумент reverse=True,
сортировка происходит по убыванию.
Внутри функции используется алгоритм сортировки Timsort — гибридная
устойчивая сортировка с временной асимптотикой O(n log n). Дополнительно
тратится O(n) памяти на создание нового отсортированного списка."""

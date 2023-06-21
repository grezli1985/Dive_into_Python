import collections
import random

""" Задание 1 """

""" ✔ Дан список повторяющихся элементов. 
    Вернуть список с дублирующимися элементами. 
    В результирующем списке не должно быть дубликатов. """

my_list = [1, 2, 3, 4, 6, 8, 2, 3, 4, 8, 9]
new_list = collections.Counter(my_list)

for i in set(my_list):
    if my_list.count(i) > 1:
        print(i)

# print([i for i in new_list if new_list[i] > 1])








# print(my_list := [random.randint(0, 20) for _ in range(20)])
# print([item for item in set(my_list) if my_list.count(item) > 1])


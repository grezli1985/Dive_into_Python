""" Метод copy() """
""" Метод copy создаёт поверхностную копию списка. Начнём с плохого примера, чтобы
понять пользу копий."""

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list                  # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list, new_list, sep='\n')  # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# my_list[2] = 555                    # [2, 4, 555, 2, 8, 10, 12, 14, 16, 18]
# print(my_list, new_list, sep='\n')  # [2, 4, 555, 2, 8, 10, 12, 14, 16, 18]

""" Мы скопировали в переменную new_list указатель на список my_list. Далее мы
изменили элемент в исходном списке. Новый список также оказался изменённым.
Как вы помните list — изменяемый тип данных и подобное поведение нормально.
Что делать, если нужно менять оригинал, но не затрагивать копию. Верно. Метод
copy."""

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()           # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list, new_list, sep='\n')  # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
my_list[2] = 555                    # [2, 4, 555, 2, 8, 10, 12, 14, 16, 18]
print(my_list, new_list, sep='\n')  # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]

""" Теперь изменяется лишь один список. """
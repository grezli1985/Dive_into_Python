"""Метод append()
Добавление одного элемента в конец"""

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)          # [None, 42]
my_list.append(b)
print(my_list)          # [None, 42, 'Hello world!']
my_list.append(c)
print(my_list)          # [None, 42, 'Hello world!', [1, 3, 5, 7]]


"""Ниже пример плохого кода. Мы добавили в список сам себя."""

my_list.append(my_list)
print(my_list)          # [None, 42, 'Hello world!', [1, 3, 5, 7], [...]]

"""Многоточие в выводе говорит о рекурсивной ссылке. Явный намёк на то, что
программист сделал что-то неверно своей программе.
Метод append имеет константную асимптотику O(1)."""
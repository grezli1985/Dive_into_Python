""" Задание №6 """

""" Пользователь вводит строку текста. Вывести каждое слово с новой строки.

    ✔ Строки нумеруются начиная с единицы.
    ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова 
    был один пробел между ним и номером строки."""

stroka = input('input str: ').lower().split(' ')
stroka.sort()
max_length = len(max(stroka, key=len))
for i, item in enumerate(stroka, 1):
    print(f' {i:>2} {item :>{max_length}}')
    # print(f' {i:>2} {item :*>{max_length}}')

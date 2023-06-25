""" Задание №2 """

""" ✔ Напишите функцию, которая принимает строку текста.
    ✔ Сформируйте список с уникальными кодами Unicode каждого
      символа введённой строки отсортированный по убыванию."""

text = 'У нам все хорошо!'


def sorted_unicode(text):
    my_list = []
    for i in text:
        if ord(i) not in my_list:
            my_list.append(ord(i))
    my_list.sort()
    return my_list


print(sorted_unicode(text))

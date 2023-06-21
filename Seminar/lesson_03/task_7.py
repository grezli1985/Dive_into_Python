""" Задание №7 """
""" 
    ✔ Пользователь вводит строку текста.
    ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
    ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
    ✔ Обратите внимание на порядок ключей.
    Объясните почему они совпадают или не совпадают в ваших решениях."""

text = 'Объясните почему они совпадают или не совпадают в ваших решениях.'
my_dict = {}

new_text = text.replace(' ', '').lower()
for i in set(new_text):
    my_dict[i] = new_text.count(i)

print(my_dict)

my_dict_1 = {}

for i in new_text:
    if i not in my_dict_1.keys():
        my_dict_1[i] = 1
    else:
        my_dict_1[i] += 1

print(my_dict_1)

my_dict_2 = {}

for ch in new_text:
    my_dict_2[ch] = my_dict_2.get(ch, 0) + 1

print(my_dict_2)

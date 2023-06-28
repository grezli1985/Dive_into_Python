""" Задание №3 """
""" ✔ Продолжаем развивать задачу 2.
    ✔ Возьмите словарь, который вы получили.
    Сохраните его итераторатор.
    ✔ Далее выведите первые 5 пар ключ-значение,
    обращаясь к итератору, а не к словарю."""

text = "rghgfeggbb"

dict_result = {i: ord(i) for i in text}

print(dict_result)

new_dict = iter(dict_result.items())
for _ in range(5):
    print(next(new_dict))

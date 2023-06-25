""" Задание №7 """

""" ✔ Функция получает на вход словарь с названием компании в качестве ключа
      и списком с доходами и расходами (3-10 чисел) в качестве значения.
    ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
      прибыльные, верните истину, а если хотя бы одна убыточная — ложь."""

dicdionari_of_cap = {'intel': (1000, 29393, 12745697, -10),
                     'balalaika_compani': (1000, -56787596788392, 568),
                     'gigabit': (324, 5708679, 4576)}


def sum_og_items(list_):
    summa = 0
    for value in list_:
        summa += value
    return summa


def get_plus_of_companis(dicts_of_comp):
    for value in dicts_of_comp.values():
        if sum_og_items(value) < 0:
            return False
    return True


print(get_plus_of_companis(dicdionari_of_cap))

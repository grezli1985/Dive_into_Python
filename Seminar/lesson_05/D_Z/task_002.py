""" Задание 2 """
""" ✔ Напишите однострочный генератор словаря, который принимает
    на вход три списка одинаковой длины: имена str, ставка int,
    премия str с указанием процентов вида «10.25%». В результате
    получаем словарь с именем в качестве ключа и суммой
    премии в качестве значения. Сумма рассчитывается
    как ставка умноженная на процент премии"""


def premia(list_names: list[str], list_stavca: list[int], list_persents: list[str]):
    dict_premia = {}
    for index, name in enumerate(list_names):
        dict_premia[name] = list_stavca[index] * (float(list_persents[index][0:-1]) + 100) / 100
    return dict_premia


names = ['test1', 'test2', 'test3']
stavca = [1000, 2000, 3000]
persents = ['10.23%', '10.23%', '10.23%']

# print(premia(names, stavca, persents))

print({name: money * perc for name, money, perc in zip(names, stavca, (((float(i[0:-1]) + 100) / 100)
                                                                       for i in persents))})

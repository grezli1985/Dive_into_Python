from itertools import chain, combinations

""" Задание 3 """
""" Создайте словарь со списком вещей для похода в качестве
    ключа и их массой в качестве значения. Определите какие
    вещи влезут в рюкзак передав его максимальную
    грузоподъёмность. Достаточно вернуть один допустимый вариант."""

things = {'зажигалка': 2, 'компас': 10, 'фрукты': 50, 'рубашка': 30,
          'термос': 10, 'аптечка': 20, 'куртка': 60, 'бинокль': 40, 'удочка': 12,
          'салфетки': 4, 'бутерброды': 20, 'палатка': 55, 'спальный мешок': 22, 'жвачка': 10}

ves = int(input('Вес: '))

sorted_things = dict(sorted(things.items(), key=lambda x: x[1]))
for k, v in sorted_things.items():
    if v <= ves:
        print(k, v)
    ves -= v







# items = {'Спальник': 5.0,
#          'Палатка': 10.0,
#          'Топор': 2.5,
#          'Еда': 7.0,
#          'Вода': 5.0,
#          'Бадминтон': 1.5,
#          'Радио': 3.0}
#
#
# def max_cargo(inventory: dict[str, float], capacity: int) -> list[list[str], float]:
#     backpack = [[], 0]
#     for item, weight in inventory.items():
#         if backpack[1] + weight <= capacity:
#             backpack[0].append(item)
#             backpack[1] += weight
#         else:
#             break
#     return backpack
#
#
# print(max_cargo(items, 30))
#
#
# def powerset(inventory: list[str]):
#     return chain.from_iterable(combinations(inventory, r) for r in range(1, len(inventory) + 1))
#
#
# def all_options(inventory: dict[str, float], capacity: int):
#     result = []
#     for cup_option in powerset(list(inventory)):
#         weight = 0
#         for item in cup_option:
#             weight += inventory.get(item)
#         if (capacity - min(inventory.values())) <= weight <= capacity:
#             result.append((cup_option, weight))
#     return result
#
#
# for option in all_options(items, 30):
#     print(option)

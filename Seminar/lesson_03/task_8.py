""" Задание №8 """

""" ✔ Три друга взяли вещи в поход. Сформируйте
    словарь, где ключ — имя друга, а значение —
    кортеж вещей. Ответьте на вопросы:
        ✔ Какие вещи взяли все три друга
        ✔ Какие вещи уникальны, есть только у одного друга
        ✔ Какие вещи есть у всех друзей кроме одного
        и имя того, у кого данная вещь отсутствует
        ✔ Для решения используйте операции
        с множествами. Код должен расширяться
        на любое большее количество друзей."""

friends = {'Кирилл': ('спальник', 'топор', 'еда', 'нож', 'вода'),
           'Максим': ('спальник', 'пила', 'еда', 'нож', 'вода'),
           'Владимир': ('спальник', 'топор', 'водка', 'вода'),
           'Олег': ('спальник', 'топор', 'еда', 'нож', 'спички')}

all_items = tuple()
for pack in [items for items in friends.values()]:
    all_items += pack
all_items = set(all_items)


# print(all_items)


def all_have(inventory: dict[str, tuple]) -> str:
    popular = all_items.copy()
    for value in inventory.values():
        popular.intersection_update(value)
    return 'Вещи, которые есть у всех:\n' + ', '.join(list(popular))


def unique_one(inventory: dict[str, tuple]) -> str:
    unique_list = []
    for friend, value in inventory.items():
        my_inventory = set(value)
        for cur_friend, cur_value in inventory.items():
            if friend != cur_friend:
                my_inventory.difference_update(cur_value)
        unique_list.append((friend, my_inventory if my_inventory else {'Уникальных вещей нет'}))

    return 'Список уникальных вещей:\n' + '\n'.join([f'{items[0]}: 'f'{", ".join([item for item in list(items[1])])}'
                                                     for items in unique_list])


def all_except_one(inventory: dict[str, tuple]) -> str:
    result = {}
    for name, items in inventory.items():
        cur_inventory = all_items.copy()
        for cur_name, cur_items in inventory.items():
            if name != cur_name:
                cur_inventory.intersection_update(set(cur_items))
        result[name] = cur_inventory.difference(items)
    return 'Вещи, которые есть у всех кроме:\n' + \
        '\n'.join(f'{name}: {", ".join([item for item in items])}' for name, items in result.items())


print(all_have(friends))
print()
print(unique_one(friends))
print()
print(all_except_one(friends))
print()
